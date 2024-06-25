import pytest
import cv2
import numpy as np
from preprocessing import (
    sharpen_image, 
    unsharp_mask, 
    threshold_image, 
    contrast_stretching, 
    morphological_operations
)

@pytest.fixture
def sample_image():
    # Import a sample image from the dataset (content/training/00000/00000_00000.jpg)
    img = cv2.imread("content/training/00000/00000_00000.jpg")
    return img

def test_sharpen_image(sample_image):
    processed_img = sharpen_image(sample_image)
    assert processed_img.shape == sample_image.shape
    assert processed_img.dtype == sample_image.dtype

def test_unsharp_mask(sample_image):
    processed_img = unsharp_mask(sample_image)
    assert processed_img.shape == sample_image.shape
    assert processed_img.dtype == sample_image.dtype

def test_threshold_image(sample_image):
    processed_img = threshold_image(sample_image)
    assert processed_img.shape == sample_image.shape
    assert processed_img.dtype == sample_image.dtype
    assert set(np.unique(processed_img)).issubset({0, 255})

def test_contrast_stretching(sample_image):
    processed_img = contrast_stretching(sample_image)
    assert processed_img.shape == sample_image.shape
    assert processed_img.dtype == sample_image.dtype

def test_morphological_operations(sample_image):
    processed_img = morphological_operations(sample_image)
    assert processed_img.shape == sample_image.shape
    assert processed_img.dtype == sample_image.dtype

pytest.main(["-v", "--tb=line", "-rN", __file__])
