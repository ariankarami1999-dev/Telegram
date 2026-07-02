<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn4.telesco.pe/file/Z29MtDzD8kuVCuJ3wbN2RoolRIKGskGCZj8Ozjv9soqkW7eQTKkPEtj3G4r5i_rhUMHNL0Quz-gB5vRP2CG3eHoLIaLgFeLAMOisJzoucDBA2Y_KQKr9vaKKYF4IrXWN9HIEn3EVBhhbKh9QJ5DzhG2fr40VNv3ghKi020_B_2Ysl0SX11ngWVn0_j8dEejfC9u5PeHj_Q2GPXx36J3nY8W5An0KLRUtuTgdtPBh4Z1i4Rs76B0uI0JpSfbKpdgQ-jB2HfX7c4iQruq03uMe3fujVmsBb8R6BOoDZnB-BY7iMyNfPXp_gEPOw58hsB-MyQKCBpRAHqTzmOBqpBQR_A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 214K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 18:05:51</div>
<hr>

<div class="tg-post" id="msg-67196">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9db45e91a.mp4?token=Gzmt4xOIlxonsa4r9jH5c5bhbN5EqPpnD1_q-kbGT7wFk4wVIUu94LUpjSPJ_jKZ11mpEOcjAcRZYp5SL-znPT1ceE625rkSksYGhl3tBXF9626VJpxyGK6VKIllUhQfqF4fuQXIia58bOWtLsngDQY_qufnue7MAJGVBbl82-nVlBsuqLZBGiZ3k61cqX6asZYHDHeAF-fCWGxH8DoVWD2zEEFCDl3c2AuGi9pv5AafpodvIecztbsF0ycqlyzl8xRwDr571Z-lr6WFTXBflpp-x_niXiI-6hSrod8lrrzGq11LTJnfUt4Vcf7QudSgyfIQNrTlr_TW0uvXHKw11A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9db45e91a.mp4?token=Gzmt4xOIlxonsa4r9jH5c5bhbN5EqPpnD1_q-kbGT7wFk4wVIUu94LUpjSPJ_jKZ11mpEOcjAcRZYp5SL-znPT1ceE625rkSksYGhl3tBXF9626VJpxyGK6VKIllUhQfqF4fuQXIia58bOWtLsngDQY_qufnue7MAJGVBbl82-nVlBsuqLZBGiZ3k61cqX6asZYHDHeAF-fCWGxH8DoVWD2zEEFCDl3c2AuGi9pv5AafpodvIecztbsF0ycqlyzl8xRwDr571Z-lr6WFTXBflpp-x_niXiI-6hSrod8lrrzGq11LTJnfUt4Vcf7QudSgyfIQNrTlr_TW0uvXHKw11A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در جریان تجمعات شبانه صیغه یابی راه انداختن و یه نفر یه دخترو به مدت یک ماه صیغه کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/news_hut/67196" target="_blank">📅 17:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67192">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AnhCD1ih_b0XXLpvBDIAZnB4fDiC5H8SeARPt5sTfjdSnyjh7c8SvaS22amE14lYKRALdiB1LUyndlGc7EIoSdodyk-Ix0JYYpNSTu2ESI-dyxzrG0qyzYLicA-oCr0CC2xCJ_4kEMn-oZIlH_rHa6SziBupIydZLbCPDGrTxq9e0npmBMyC-7bwNsDitoSKjVyF4qh3rNn4wd5sck8u5MRal18jsX20GRJij1ZXaYSXY4d2R4wqI2Qws0-PoAm6gdomI-mkgiGmVz2gCk-hCZaUiWFNBB9d4JBTsrXSTAVvsugLS0NYl_CdD4VS8tQuUzsNkAIL5fsjpqvLJVSu5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QqTkhnTZ41JnmVdIDMm5Y45F1mYe3vtoy7AaKuh7n_JVqeJ7iEUHMEvfLeD__GXNy7ulBHagzDoRqtRbWH_z2cN6XYbGJF-h0Eib26G4Z4lVYKYvMHOb4rdT6weZwNiN82AjruA_anoP9PTaKJAOmBQ5OAAop6liPSFC_hmKca35FpH7fq-m4STugYe7dMhxsOheTV4_tQaXnxiUJmsj9kcQHkVVnq8_o_iwrFXiVf_lbBxwY-6d1ILamDKKChAIBpfMkP6WN--Zeofe6qDsqWVnBaeUnlB1teM_2JP2xevHBpRe-LDIT1QGv_H7Sif_eYUNPMn-Ig_8ZQ8Ot6XNWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oUSPj4vuyhkxsW-C7YOxTIkqqMTxNracE_iHXbUY6kd0bM1Ml0qVRD8ekCVyROl6OsrG45gJFCwbRUTGXMUClNgTs2ILMYPjqP4g-Y70JOiZ8sDOJPfGoeUCP76Xa46oFxdEfEyq3rdWWMPX9wA4NgTlYvDMwJtTQh2snM9mwmiB6_TJWX6vf9pjqNIQZzV3CVdL7xarFz4BmX-0huY0lEH7RAHoiK6u3uu8yPkEzitgBUjeeOc7sbwARb60WcV-oYSwHCkKAHzh86SI7cCWmRdKakXOuKGsEmLEasapscfBmUvgnhE_hG19aZ9Fav0VpRKYtFN_F6Y--3aNb7rp8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/543c505f1c.mp4?token=Pt9pv8uvn9x4qAHmPdMCt0p5x_h-mVk_zwSNyT16xjXRkCewNzEdJ6D9Ny6IZjczopqmqtFonUiI_KFwqe7IFynHRXBuAAf4D1bd9f-AXji_FuuTF5CX3kRq1q-Z9Dv8LO436JkZ54m-jqA9vOrIb8WBeaBCOWzj00OPlxLEGw0NWk9bw6LcKEpbMeBJAo0Lxzs0CcssO5so-flZ5zLahLHWraqr_0TOdNvQ9fvrA0jBz5A4GWG9UCR9HhVyCVxiTA_FQKJD4Md_yFgjdO-IH5i2dVJYlh8vw_iK5GQ2g86nAIx0x1Zb_weaRCVSMVOQ_SPoKqZziBmUcnNJ0k0SNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/543c505f1c.mp4?token=Pt9pv8uvn9x4qAHmPdMCt0p5x_h-mVk_zwSNyT16xjXRkCewNzEdJ6D9Ny6IZjczopqmqtFonUiI_KFwqe7IFynHRXBuAAf4D1bd9f-AXji_FuuTF5CX3kRq1q-Z9Dv8LO436JkZ54m-jqA9vOrIb8WBeaBCOWzj00OPlxLEGw0NWk9bw6LcKEpbMeBJAo0Lxzs0CcssO5so-flZ5zLahLHWraqr_0TOdNvQ9fvrA0jBz5A4GWG9UCR9HhVyCVxiTA_FQKJD4Md_yFgjdO-IH5i2dVJYlh8vw_iK5GQ2g86nAIx0x1Zb_weaRCVSMVOQ_SPoKqZziBmUcnNJ0k0SNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیروز این دوتا زوج تو نیویورک رفته بودن بالای یک برج ۴۴۰ متری، که یهو پسره ازش خواستگاری کرد
@News_Hut</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/news_hut/67192" target="_blank">📅 17:04 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67191">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afce812fcb.mp4?token=oAFdhcQR-W6EoxvYh6HHto7yMn6iaO35qobyu_qUA7onTOvslggprGLIXFdzrUhdZj_irVHIH7irFB3hRLYmV2MIWv5B3nI9S2RTg4Z5asEAX2gXuYw71nw6dxykIX7o9fhYsw-Crt3XbEqtv6mAfSWS0XKfhQT6mKXzQawpt3kuJPdwomIJfXL8dOwAuFUCQDSzvNPoYHfGzKq8lovY69fVXQGCPUpO-0CIEJF2KJp_UIYHDo39H5C02aG8MvDkQ49r916BfFXJ0lMBIPt7leCblmhvPm84IGCAxhAdOTIVe1pT6_kRHh6db9zNlZ201LWystgfVMitglii2PEtIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afce812fcb.mp4?token=oAFdhcQR-W6EoxvYh6HHto7yMn6iaO35qobyu_qUA7onTOvslggprGLIXFdzrUhdZj_irVHIH7irFB3hRLYmV2MIWv5B3nI9S2RTg4Z5asEAX2gXuYw71nw6dxykIX7o9fhYsw-Crt3XbEqtv6mAfSWS0XKfhQT6mKXzQawpt3kuJPdwomIJfXL8dOwAuFUCQDSzvNPoYHfGzKq8lovY69fVXQGCPUpO-0CIEJF2KJp_UIYHDo39H5C02aG8MvDkQ49r916BfFXJ0lMBIPt7leCblmhvPm84IGCAxhAdOTIVe1pT6_kRHh6db9zNlZ201LWystgfVMitglii2PEtIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پست جدید ترامپ:
ترامپ پزشک می‌شود و بیماران مبتلا به «سندرم اختلال ترامپ» را درمان می‌کند
🚬
@News_Hut</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/news_hut/67191" target="_blank">📅 16:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67190">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cadc1a3fe.mp4?token=Kl9HAPEDGqhINFhq4GTfEtJo7k21SaGHgFWQ6k93-HPNrKpWp_vG4tRaIsrHsAOpRBxN3jzbAei2q9y2C29L-dmb8skIVgQWjP5TnkR8Vi-xznKbem1o5b-7nWRqi5nZ8A5SSxkdB27HfM3gYptLGUTpY8e2M-TBjmb8HqftJmJNy3xC8WC8v47qTX7kM4j7aTyjFtcmRYDC5OCtJj0kBwI-x_MBXRaxhTCP8EDeaAdN2-Aa7xwezvXEOgWoA_yQGyRCeJVvgLbovsXtKTsn28iddpCE-FMurtxm4kRc6Y2lqEmKwzzxe5HT_ZWJ9Vzxld_lJjqrTcbtd_jOsAi6tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cadc1a3fe.mp4?token=Kl9HAPEDGqhINFhq4GTfEtJo7k21SaGHgFWQ6k93-HPNrKpWp_vG4tRaIsrHsAOpRBxN3jzbAei2q9y2C29L-dmb8skIVgQWjP5TnkR8Vi-xznKbem1o5b-7nWRqi5nZ8A5SSxkdB27HfM3gYptLGUTpY8e2M-TBjmb8HqftJmJNy3xC8WC8v47qTX7kM4j7aTyjFtcmRYDC5OCtJj0kBwI-x_MBXRaxhTCP8EDeaAdN2-Aa7xwezvXEOgWoA_yQGyRCeJVvgLbovsXtKTsn28iddpCE-FMurtxm4kRc6Y2lqEmKwzzxe5HT_ZWJ9Vzxld_lJjqrTcbtd_jOsAi6tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این چیه دیگه
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/news_hut/67190" target="_blank">📅 16:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67189">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcf57c8dbd.mp4?token=pIv9bjCEaqNjU2Bv6mAd9tiWNGfh2XbasiwmrfBWBT0og7PkLLLfYy2Exq7I9DOGQFBbSFpX-GFkMArsfad-EA0tKVHAJw1-R5t-4yDeQGICHQH0yaQvihRbIPiwTcvqFxZxLfKJ8A6EDPaOixzuSVa_LB8n8JuTqpRowx0xxRYXz3nWnxms882Ms_625QfNYLuerOeyLzO37orpCwjof6UZZJCI_Yw7bc0Dto9wDx8o59IQIOSsdfP6GiJX9c3_SCyaL0MB_uCdd2kn07Slqim8uNJJY7AUvX1eq8JeKz2UTqvOYnXNTtf1XmRwetkozjX4vUA-iiZgiV1EcMQI7Ba0ePa7KuJwXpwqpjjtNEDt2zkzAeNwkEA62GYpR2PmZsI8Yq4lYgIGBH-OAPFJI9PESkt4PqBzPWLsTiAKR1Ob7M2FOq9TKMMFkJr-tO3tX7j3AIND_svuIF_ay7RwAkpFUu6LyvRu687qwyH3yf0DTGbfda1kY0E3OCZyQjbjKzneWIJZdLulNvTxBFEdlLmu2UUaOBr0MFIglaT4bBViboUiZrb2Nm4EvviPuOR2i3T45eNd83BjaVIHavcAz3bnvrYEDKeovw8X7E_TJzF-uklbtTNf06w7xxZ-RDQUYzag50qGGVdjY1kVvZ1v3bksBR7HIBTMvCfHB1ELcRM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcf57c8dbd.mp4?token=pIv9bjCEaqNjU2Bv6mAd9tiWNGfh2XbasiwmrfBWBT0og7PkLLLfYy2Exq7I9DOGQFBbSFpX-GFkMArsfad-EA0tKVHAJw1-R5t-4yDeQGICHQH0yaQvihRbIPiwTcvqFxZxLfKJ8A6EDPaOixzuSVa_LB8n8JuTqpRowx0xxRYXz3nWnxms882Ms_625QfNYLuerOeyLzO37orpCwjof6UZZJCI_Yw7bc0Dto9wDx8o59IQIOSsdfP6GiJX9c3_SCyaL0MB_uCdd2kn07Slqim8uNJJY7AUvX1eq8JeKz2UTqvOYnXNTtf1XmRwetkozjX4vUA-iiZgiV1EcMQI7Ba0ePa7KuJwXpwqpjjtNEDt2zkzAeNwkEA62GYpR2PmZsI8Yq4lYgIGBH-OAPFJI9PESkt4PqBzPWLsTiAKR1Ob7M2FOq9TKMMFkJr-tO3tX7j3AIND_svuIF_ay7RwAkpFUu6LyvRu687qwyH3yf0DTGbfda1kY0E3OCZyQjbjKzneWIJZdLulNvTxBFEdlLmu2UUaOBr0MFIglaT4bBViboUiZrb2Nm4EvviPuOR2i3T45eNd83BjaVIHavcAz3bnvrYEDKeovw8X7E_TJzF-uklbtTNf06w7xxZ-RDQUYzag50qGGVdjY1kVvZ1v3bksBR7HIBTMvCfHB1ELcRM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
صحبت های جنجالی
غضنفری، نماینده مجلس جمهوری اسلامی:
عده‌ای میخوان تجمعات شبانه رو جمع کنن. دارن علیه مجتبی خامنه‌ای کودتا میکنن. دارن هزینه‌های سنگینی میکنن و به مداحان و سخنران ها پول دادن تا دیگه تو تجمعات شبانه نیان.
به بسیج نامه زدن که دیگه تو تجمعات شرکت نکنید. مجلس رو هم ۴ ماهه تعطیل کردن که نتونن اعتراض کنن.
قالیباف و پزشکیان میخوان کم کم مجتبی خامنه‌ای رو کنار بزارن و خودشون اداره کشور رو به دست بگیرن.
رهبر از مسئولین قطع امید کرده و الان فقط امیدش به مردمه.
@News_Hut</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/news_hut/67189" target="_blank">📅 15:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67188">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1148d0ce1d.mp4?token=qmFo3scwc71wqM2txzBLrcRbJlApWbStz4dNsk4Sac_xaWim3A45Z-XDUpKwBqnDGDup3BQFnpLVuw8VPRPc5rUh2WAQPcRTlDp1ntpjwE90bUyzvB3rSKYqKOoejZmhmN0PHVCKs32ZmMlf-ZuJVwxuvE32_-6CRygHRIgGmbl-gx0tKzOMhMzMi7-wCgoS9XQkxfX97SwOgxl6JRAAfVO1z7oA3NvWDzcejfj3z8psvEbu9_XC5JWkTeMeZXrxMYQEcURJbt_bukRITM5855WnBbm7x9cqAyse2f3_ocW_snQYtcwFCPZzAuqFJyNUHUJNgHJfc7NlIn_23NyelQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1148d0ce1d.mp4?token=qmFo3scwc71wqM2txzBLrcRbJlApWbStz4dNsk4Sac_xaWim3A45Z-XDUpKwBqnDGDup3BQFnpLVuw8VPRPc5rUh2WAQPcRTlDp1ntpjwE90bUyzvB3rSKYqKOoejZmhmN0PHVCKs32ZmMlf-ZuJVwxuvE32_-6CRygHRIgGmbl-gx0tKzOMhMzMi7-wCgoS9XQkxfX97SwOgxl6JRAAfVO1z7oA3NvWDzcejfj3z8psvEbu9_XC5JWkTeMeZXrxMYQEcURJbt_bukRITM5855WnBbm7x9cqAyse2f3_ocW_snQYtcwFCPZzAuqFJyNUHUJNgHJfc7NlIn_23NyelQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درتجمعات شبانه عرزشی‌ها:
مردها: گندم و جو ارزونیتون
زن‌ها: تنگه، نمیدیم بهتون
😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/67188" target="_blank">📅 15:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67187">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a2c0f9a4.mp4?token=XWi2iawMMrGQer4FcTB3QCtVPgyavb_MKVio1UF3eH0t1GZT_E6HZeZfSXx0iVzqsp7D-sR3m99aMaEXCIJ88xJ4vNpSXptk9EiKf6pGjm0N3fUGh6p7zvNokdzmzkq5Zx7KEvwuCDp1JJ6o5FXifJLVmS6X3jL_hrZunYSGUJ6J5k78kg8ZtfdzHdHpPLcBUk7u2HD7mtwECTedxrd8vqKdhT_3eDXhqCprj3qmVmBlDuQqI7BR60T0d0XVl1J8n2eYx7Scq8BjPwqnlTjAGm_D5D-VDiEJHvHARjEjPntwjTjfq7tY1PffTNtDi7wTlIboRF9wlu3gcUFBYcFGeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a2c0f9a4.mp4?token=XWi2iawMMrGQer4FcTB3QCtVPgyavb_MKVio1UF3eH0t1GZT_E6HZeZfSXx0iVzqsp7D-sR3m99aMaEXCIJ88xJ4vNpSXptk9EiKf6pGjm0N3fUGh6p7zvNokdzmzkq5Zx7KEvwuCDp1JJ6o5FXifJLVmS6X3jL_hrZunYSGUJ6J5k78kg8ZtfdzHdHpPLcBUk7u2HD7mtwECTedxrd8vqKdhT_3eDXhqCprj3qmVmBlDuQqI7BR60T0d0XVl1J8n2eYx7Scq8BjPwqnlTjAGm_D5D-VDiEJHvHARjEjPntwjTjfq7tY1PffTNtDi7wTlIboRF9wlu3gcUFBYcFGeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
رسانه‌های اسرائیل: تصاویر ماهواره‌ای تازه از سایت هسته‌ای اصفهان؛
تصاویر ماهواره‌ای با وضوح بالا شرکت وانتور نشان می‌دهد ورودی‌های اصلی تونل‌ها در سایت هسته‌ای اصفهان، جایی که بر اساس برآوردها بخشی از اورانیوم غنی‌شده رژیم جمهوری اسلامی نگهداری می‌شود، همچنان با خاک پوشانده شده است. این وضعیت نزدیک به یک سال پس از آسیب دیدن این مجموعه در حملات هوایی اسرائیل در عملیات «با شیر» و عملیات آمریکایی «چکش نیمه‌شب» در ژوئن ۲۰۲۵ ادامه دارد. بر اساس این گزارش، جمهوری اسلامی در آغاز سال ۲۰۲۶ به طور عمدی دهانه تونل‌ها را با خاک پر کرده تا آن‌ها را در برابر حملات احتمالی بعدی محافظت کند و ذخایر اورانیوم غنی‌شده را در بخش‌های زیرزمینی پنهان نگه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/news_hut/67187" target="_blank">📅 14:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67186">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMoris News</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s37eul_rWWdfDrZVmqFUsAh1dKNq9i0Uc_p1JU6Lk7eeTu9gZYoNLvX1AueoUDmEjfJpnWaycW9F29th1WUNxfEKeoBDFwpv6nqEfOv1K8XF8vHVNCJjl-oo0gC_Lk18b5K1rq02xPVL38jywoKLDmdIUfMwzxrycGpIPvumW-s3OjpIc4c5vyYv2-NzfazEh3tzcKPXuIsCjOiRiiqJG-s7guVS75UNAVpQM7MEnBGe-dFwLiS16hSR7JlyIXcU5GlAe9KJ8bKeDvTaaUIFF6eYRJRL419GjaWzdviQ8R6iq-E5I3BDGMVPy9PjJRemIYuifUAkXwGwc7D9IGGLXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه جدید یک دوست عزیز و هنرمند که احتیاج به حمایت داره
از دوستان خواهش میکنیم با فالو کردن و شر از این دوستمون حمایت کنید.
@egyptinpersian
در اینستگرام</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/67186" target="_blank">📅 14:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67185">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rH5MCve6-VJD_NCcpwXir5hyjGZCFnRqq1l2ORZM0pnyiFrZgg-DMW8V9gRPbWQTtbsu-WBD9zFsMd2RndOnd31yse-hyQczrEHDrb-rodx1_kV-1ztOT2dl_tftsT-Lxl0PA0Ht95sJQFv2we-NmP3nUFpS8Yc-1ScD40A-R9C3imAgdTyjPiIWSNmABMU1GGQh-DOxjUTyTHSKf_FNCiLYzsyeZnihTBIyb6WAChMlr9wwazIGziQ6m05UmEH3K3CZ83wCtIEj-z6O1DHNt2Ijy53cngu3zJDni5REY77KX8wGgK44RKTK923xyjebhXxNt300fN55Hpp6I5oD5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
العربیه:
دور بعدی مذاکرات ایران و آمریکا ۱۸ ژوئیه برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/67185" target="_blank">📅 14:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67184">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/885b0b0686.mp4?token=MqEyil9GiYDpg-MAX5XVD2mGZFZ2P7LNhMgzk2yySPsnfPBP8uAjZtJrYtgUfUHwwJy8PLSVtGnWawtQ85Gm6aHXqu0kI-P4hTpy5QGjAcLrHjuLbfyonVt9q6iVdaioV9Q-KFog47FojNf4PqauaqILwh-LSrptSS8fb8PQFW0zhnhsrcYVYNJ-84SdXvg_KU5sFAuAw1K8UlQJdXER1XEnOXFyjvDUcXY9cikELBgj66Z9shFdE0pbTDsReNGo1HKaloJSe7y_yohvWWaBCxcPfvetYHfj4ZGrF23RmC-tuY9XhtYFkpOLMz3aXcKLFQrkr5dDmyRAR0dwUyabFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/885b0b0686.mp4?token=MqEyil9GiYDpg-MAX5XVD2mGZFZ2P7LNhMgzk2yySPsnfPBP8uAjZtJrYtgUfUHwwJy8PLSVtGnWawtQ85Gm6aHXqu0kI-P4hTpy5QGjAcLrHjuLbfyonVt9q6iVdaioV9Q-KFog47FojNf4PqauaqILwh-LSrptSS8fb8PQFW0zhnhsrcYVYNJ-84SdXvg_KU5sFAuAw1K8UlQJdXER1XEnOXFyjvDUcXY9cikELBgj66Z9shFdE0pbTDsReNGo1HKaloJSe7y_yohvWWaBCxcPfvetYHfj4ZGrF23RmC-tuY9XhtYFkpOLMz3aXcKLFQrkr5dDmyRAR0dwUyabFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرواز جنگنده های رادار گریز F-35 برفراز ورزشگاه Bay Area سانفرانسیسکو در بازی بوسنی و آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/67184" target="_blank">📅 13:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67183">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dd137decc.mp4?token=Uo4jEnyRDn7DS2O9V_qwaQTmqmAcaEgUV8oqE_x4BbMkj7LnDRxd58bvQTbytSPuWyG7NoWaMGsVcGPFaglNFFsIm8RZiIfuw55iwNznMHdVIabAcuF89hLwA0ZFHmvsXKcytlW-Ctg3yGsQ3tROioCNc7rK_9I8XIKGArteajz19BRL2kKaEP3s2XC9KUdz0SUK6DHoDtUjEwVBuKTfaZd4MOErKQpPVvhTfZNKkYR4214NE8OMix8Wke46ajHU_DqwAeXENEI8zj-g_3n55M-dfEPwvbvhE6VW4J_-SLlh1AjJko5bQvL-CDl51ED0Wr7cIxUevIKL9LCa9ANnxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dd137decc.mp4?token=Uo4jEnyRDn7DS2O9V_qwaQTmqmAcaEgUV8oqE_x4BbMkj7LnDRxd58bvQTbytSPuWyG7NoWaMGsVcGPFaglNFFsIm8RZiIfuw55iwNznMHdVIabAcuF89hLwA0ZFHmvsXKcytlW-Ctg3yGsQ3tROioCNc7rK_9I8XIKGArteajz19BRL2kKaEP3s2XC9KUdz0SUK6DHoDtUjEwVBuKTfaZd4MOErKQpPVvhTfZNKkYR4214NE8OMix8Wke46ajHU_DqwAeXENEI8zj-g_3n55M-dfEPwvbvhE6VW4J_-SLlh1AjJko5bQvL-CDl51ED0Wr7cIxUevIKL9LCa9ANnxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
ما دو بار به ایران وارد شدیم تا خودمان را از نابودی نجات دهیم. در صورت لزوم بار سوم هم این کار را خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/67183" target="_blank">📅 13:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67182">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b216695e17.mp4?token=uWcKFGmZyagnnRpTNBZQ7wqewQoAMv04hba5W_oXjrfS5IR5n3kOQNRti-xFy6zZsvjweKHt2im0cTTUja-7RSJSaGjHP84ppV6LTWwSgwwvG1rsUuBGvXmRAeV6o5bKkO_jdBPImmHfkiDc4DQ8nsr4LGEEImt8gP60PCz2lY2xTtdOGMhKoBXwI56DNNBWKoRr8D0GcsFpeyhxU_CbzTBe7Q1hc2i3gGIa6LhYdeStmKvMgv5BbIHLEHNSXMfpVYIKg47euPYjV8BohSu9N7qSj2kPzgdER0Ts8z8tLTVPgt4qRu-I_ru8_P7gtQ_s2hmNgyd5gNXMvwmqvSUHxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b216695e17.mp4?token=uWcKFGmZyagnnRpTNBZQ7wqewQoAMv04hba5W_oXjrfS5IR5n3kOQNRti-xFy6zZsvjweKHt2im0cTTUja-7RSJSaGjHP84ppV6LTWwSgwwvG1rsUuBGvXmRAeV6o5bKkO_jdBPImmHfkiDc4DQ8nsr4LGEEImt8gP60PCz2lY2xTtdOGMhKoBXwI56DNNBWKoRr8D0GcsFpeyhxU_CbzTBe7Q1hc2i3gGIa6LhYdeStmKvMgv5BbIHLEHNSXMfpVYIKg47euPYjV8BohSu9N7qSj2kPzgdER0Ts8z8tLTVPgt4qRu-I_ru8_P7gtQ_s2hmNgyd5gNXMvwmqvSUHxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
ناموسا این چیه ؟
جدیدا تو تهران یه روش درمان افسردگی به نام "هیپنو‌تراپی" مُد شده که مراجعه‌ کننده رو می‌چسبونن به درخت و میگن گریه کن !
درختی هم چند میلیون می‌گیرن...
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/67182" target="_blank">📅 12:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67181">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
قرارگاه مرکزی خاتم الانبیا:
استمرار حضور جنگنده‌های آمریکا، با سرنشین و بدون سرنشین بر فراز تنگه هرمز، باعث ناامنی این آبراه می‌شود و امنیت منطقه را به خطر خواهد انداخت.
جمهوری اسلامی در صیانت از حق حاکمیت خود در تنگه هرمز، از هیچ اقدامی برای درهم‌کوبیدن هرگونه تعدی و تجاوز توسط ارتش آمریکا و حامیان آن دریغ نخواهد کرد
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/67181" target="_blank">📅 12:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67180">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m880LGFQ7ETwVsVWyYdn6CwjoXnzDJYiBh_ZQQpiXTyKdHRy4LcA-IFD8J77EjiouuNXXV4xt1IJDkTWXUAP_7etjxzwrPmpGSFyS8GaqnQh2mWgpTaL-aucmXXHzbE-M1zAIxNjm4fysUYnRX8DYqZELuaa48J1Vv-_BCWuZw5bAYvoqmzLhr_x3kgACTxK_O-5zVud6vrZWNahgJr-EbclUKMJrRcB2FUEcMXvo070WpHZ6awizS7uQlv1UEFNE8iVr_ZtXorvJNf2mMAkL4KCjaHUHx8zQBn6hNruV7vd1_U4ZwOt9ktlBUBq_ky68clWo7jTKCUnhsMRsU7C7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
‼️
وزارت خارجه پاکستان: مذاکرات غیرمستقیم ایران و آمریکا در دوحه پایان یافت.
ایران و آمریکا در جریان مذاکرات غیرمستقیم دوحه، ضمن دستیابی به پیشرفت‌هایی در موضوعات مرتبط با تفاهم‌نامه اسلام‌آباد، بر سر ادامه گفت‌وگوها توافق کردند.
زمان برگزاری نشست بعدی در اولین فرصت ممکن پس از برگزاری مراسم تشییع رهبر شهید ایران تعیین خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/67180" target="_blank">📅 12:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67179">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d167641bf.mp4?token=QbWGQoXxrJH9XmmL5laEhZK3R1BUlo22n3In9H2s0XbEKepGOKH1o7x88H3_vSjezkb7N3LKLSQLN1nU80d9y1zdcm-X-egBnKJvOfyIjWJ-0PyxikGE6mUMyWgIcjKBwwaB0tw5nFOncYrgYN1vm6--CSggGsDMrRAkZ8gVPI8859FUGPb-fS_wSZ33jUOgwIoPxJfFoYm0Xs0oKeiJqOI77k8wRx9e3qhTdM8Urqxy7QIXzGEaNFBeTEIIpB9hstNjfFdPN7rhlhABEfeEkhmGg0htvIfR27lppPyxBvodGybdxZFUdCg2HXXdiWrJUhAq4SBoWCy-sBYpFbfmeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d167641bf.mp4?token=QbWGQoXxrJH9XmmL5laEhZK3R1BUlo22n3In9H2s0XbEKepGOKH1o7x88H3_vSjezkb7N3LKLSQLN1nU80d9y1zdcm-X-egBnKJvOfyIjWJ-0PyxikGE6mUMyWgIcjKBwwaB0tw5nFOncYrgYN1vm6--CSggGsDMrRAkZ8gVPI8859FUGPb-fS_wSZ33jUOgwIoPxJfFoYm0Xs0oKeiJqOI77k8wRx9e3qhTdM8Urqxy7QIXzGEaNFBeTEIIpB9hstNjfFdPN7rhlhABEfeEkhmGg0htvIfR27lppPyxBvodGybdxZFUdCg2HXXdiWrJUhAq4SBoWCy-sBYpFbfmeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
جی‌دی‌ونس،خطاب به هوانوردان نیروی دریایی:
«رئیس‌جمهور ایالات متحده از شما خواست اطمینان حاصل کنید که توان نظامی متعارف ایران را نابود کرده‌ایم، و امروز که اینجا نشسته‌ایم، نیروی دریایی آنها در کف اقیانوس است و هیچ توانایی برای نمایش قدرت ندارند...»
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/67179" target="_blank">📅 11:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67178">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc4627802a.mp4?token=nbmEACrk60bARkddpqkExgCR29y10IwpdpT9ltq8Wfh_I3rqGtYuh1rOI-B8Mj-KUDrJhp_t92AzZWfCjjPL0xXAdKeCkKk63fkXL-LWC-pfTgBlryg91g8qCvKgK6-3fYo1h6ql-0MYKCxx12dDg-8uy8Lf2c5hL36DWCkttWinCIVvUIWxEe40F6FgneMcNEX_HRAzdh4e1lQBymFPnhRqBEsN2JpENIu0flLQ2IeZRcUtfxU3GTF6OCgvtF58cqW6GOru3kMOdCAoKg8QgfaCtCJHiiujeK1CeNDfTGdrydAvk6S-z73b_peC5s9o36V8turhMPfRTFQwzkxBPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc4627802a.mp4?token=nbmEACrk60bARkddpqkExgCR29y10IwpdpT9ltq8Wfh_I3rqGtYuh1rOI-B8Mj-KUDrJhp_t92AzZWfCjjPL0xXAdKeCkKk63fkXL-LWC-pfTgBlryg91g8qCvKgK6-3fYo1h6ql-0MYKCxx12dDg-8uy8Lf2c5hL36DWCkttWinCIVvUIWxEe40F6FgneMcNEX_HRAzdh4e1lQBymFPnhRqBEsN2JpENIu0flLQ2IeZRcUtfxU3GTF6OCgvtF58cqW6GOru3kMOdCAoKg8QgfaCtCJHiiujeK1CeNDfTGdrydAvk6S-z73b_peC5s9o36V8turhMPfRTFQwzkxBPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اشک‌های مهدی تاج پس از کسب قهرمانی در جام جهانی فوتبال 2026
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/67178" target="_blank">📅 11:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67177">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7280fbe763.mp4?token=fdv7NrbZU3GGtLpOqz5jLp3j-73fUaxLdqWSo-oWMAGoSxCNQcR-9r_WtPiwuQrZ238Gz-1sOQVPj78KbrbCnhzwkH600UMxCb_TsKSbAr5gcVz6-qllreCT9oyBrtnXE62SdAtJvQfGJYsuq7gW4Sx305XvncF6mMDb8Nr2PvKGUteMeRG77GIWRzv5CNQ9ByQQjKB8idw2jo7HKSMoGcB-cGVkrIc9xbcVRRqUTxUia7itx5uBDff_Aw1IgPlOi0I9U0ZaLAs8Jb9YDj_9SgawIG8H-jmAYBA1poQALzZFCequ8ot7RVqrO4l0XunHIP6LO8nrkKVGMZaT6KM4bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7280fbe763.mp4?token=fdv7NrbZU3GGtLpOqz5jLp3j-73fUaxLdqWSo-oWMAGoSxCNQcR-9r_WtPiwuQrZ238Gz-1sOQVPj78KbrbCnhzwkH600UMxCb_TsKSbAr5gcVz6-qllreCT9oyBrtnXE62SdAtJvQfGJYsuq7gW4Sx305XvncF6mMDb8Nr2PvKGUteMeRG77GIWRzv5CNQ9ByQQjKB8idw2jo7HKSMoGcB-cGVkrIc9xbcVRRqUTxUia7itx5uBDff_Aw1IgPlOi0I9U0ZaLAs8Jb9YDj_9SgawIG8H-jmAYBA1poQALzZFCequ8ot7RVqrO4l0XunHIP6LO8nrkKVGMZaT6KM4bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏فرهنگستان زبان و ادبیات فارسی از سال 1369 تأسیس شد
از اون سال کلا 158 کلمه رو تغییر دادن و تو 8 سال اخیر، 2 هزار و 100 میلیارد بودجه گرفته
با ی حساب سرانگشتی کنی، می‌بینی برای تغییر هر کلمه، حدادعادل، 64 میلیارد پول گرفت!
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/67177" target="_blank">📅 10:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67176">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/514f1dff1b.mp4?token=XZln5zzFH2RkUlm_kzkry2K8zj7xlwqSsPuTtaOOi_i0PcXYoI32pyyH9dNXMWMM7-cJbHsUOCjOiZ7nxV7p5DRqnpWnx0JKAKogJgtWnH-vDV4Ouzsf5X3jIWsomV2eCN3Nm2qHJFKqRF5jwqDa0JCQdN1YuxKr0MlFfS1m1SE3OKrTvHkOJhKlpgyDoJmssOD4PmZj6BOO19sdB5Su2bObLlTNXP3IWobjo8PPTaQ0OXDbjKk-T-8ueSMIoQacUzLubpE0TuOFkcneqV-rQw47XOiTtlZfedC9yPRNic5UbNGLSaFA8r-IPgS_YGC_q2Xi5l-OEzNAf_aUiuqe4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/514f1dff1b.mp4?token=XZln5zzFH2RkUlm_kzkry2K8zj7xlwqSsPuTtaOOi_i0PcXYoI32pyyH9dNXMWMM7-cJbHsUOCjOiZ7nxV7p5DRqnpWnx0JKAKogJgtWnH-vDV4Ouzsf5X3jIWsomV2eCN3Nm2qHJFKqRF5jwqDa0JCQdN1YuxKr0MlFfS1m1SE3OKrTvHkOJhKlpgyDoJmssOD4PmZj6BOO19sdB5Su2bObLlTNXP3IWobjo8PPTaQ0OXDbjKk-T-8ueSMIoQacUzLubpE0TuOFkcneqV-rQw47XOiTtlZfedC9yPRNic5UbNGLSaFA8r-IPgS_YGC_q2Xi5l-OEzNAf_aUiuqe4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
حملات سنگین روسیه در طول شب به کیف اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/67176" target="_blank">📅 10:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67175">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRAN ANKER</strong></div>
<div class="tg-text">.
☀️
هوا گرمه ؟
🔥
ما قیمت‌هارو
💲
خنک
🧊
کردیم...
🥳
جشنواره‌ی تابستانه‌ی ایران انکر شروع شد
🤩
برای دریافت لینک جشنواره به لینک زیر مراجعه کنید
.
.
🛍️
تمامی محصولات انکر در این جشنواره انقدر تخفیف خوردن که این گرمای تابستون رو خنک کنن برای شما
❄️
.
.
📍
فرصت جشنواره محدودِ ،
دیر نکنید که این قیمت‌ها حالا حالاها تکرار نمیشه...
👇
لینک ورود به جشنواره
🌐
اینستاگرام
🌐
@iran_anker
#anker
#soundcore
#جشنواره‌ی‌تابستانی
#ایران‌انکر</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/67175" target="_blank">📅 10:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67174">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b45db1d5ff.mp4?token=dbpESipbGQunWxn2s7mYqwL5KxQ-0VdAe-aSMXgvqXbFe0YOxaemL-9JN4UU2hKK0bSvL--4KX5ChgEEpJGsLNwQt0FL8R3YgS9kRkEx22gzxpmdtoou83klx1APdLzT-AIwlNhgzoGFpIKqp7MwWb83-ADpgg8UFURSEYzmwCohe_5Q0LkjZ8aec1YDI_7-ggqqh1iA3qYBItsJGMNOQxsnbU1EFjrRjCnlOdr7a5IVUcjH0tiJpMvh4LEdeMj4ha5ecwmXMvMevLH-PLg5DIgovWTJK6J35T-Wa866ou8cOJP49teXWKBReQccb3zXKQa3VYJU4BYLI54L7nPNTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b45db1d5ff.mp4?token=dbpESipbGQunWxn2s7mYqwL5KxQ-0VdAe-aSMXgvqXbFe0YOxaemL-9JN4UU2hKK0bSvL--4KX5ChgEEpJGsLNwQt0FL8R3YgS9kRkEx22gzxpmdtoou83klx1APdLzT-AIwlNhgzoGFpIKqp7MwWb83-ADpgg8UFURSEYzmwCohe_5Q0LkjZ8aec1YDI_7-ggqqh1iA3qYBItsJGMNOQxsnbU1EFjrRjCnlOdr7a5IVUcjH0tiJpMvh4LEdeMj4ha5ecwmXMvMevLH-PLg5DIgovWTJK6J35T-Wa866ou8cOJP49teXWKBReQccb3zXKQa3VYJU4BYLI54L7nPNTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جلیل محبی:
مهدی محمدی(مشاور قالیباف) جی‌دی‌ونس ایران است!
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/67174" target="_blank">📅 10:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67173">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18665cc14b.mp4?token=fy1a_g45Vf9_wtm16U5e8IeK3483oQQM8OgT7xvO3k_VaJTl0HmPWgzxSURFuGe2wFv_N9t2K6g1lpp0708Pxt4-62p-rv3HRIXH5W7eiJQ_pozgU0NxVsTJPfwT5TzP_SR8xwkSwRI1ZiQK-ebovyOVaCkxlRBxU0REQjtGYmQ9hM6ttSG08Qkx05_giypbZWgHyGVmrZn5X6VtHNtMyeZF-CFwbllUVfKOp80ILofr47GnpOzbPiz4ioRV5RxotFuSXj2A3xf70jy6jdUxEkolmpVymWIZrz-T93Zv0j0l3mdM5csvc7vnwE7NXcoxlBozM73UZWOCtD3KU5VNe4FmGtvSGfz6b1wh7-v9Ho7Z_eOwhz98Cxs9VlaUBFa3rvMkX-7tobDuT7H2OH0jSu7u58CKmOTIwibJ4CqbDLk9ySfdgDReTwvkh6xE3z2CX2BAQSIf5aZOxo0gK1kmwcdRRhv_6EnePJIXVE1DL70vGME6A2gjDonbKOHUnYgFw7TNT1MzbVEQ7vGK9FPctlwYTlawJDj9Q9K2kqEKhDpAdXgDOsG2fqxDDD8NtUgZOI85xqJo_ieUpSNHJNtpOdXZbdT1O0Nfr8psy_k270iyN9KZuXW3kblKwIAqGYKeyE1VqXM173qC2gxUbil4OBTQgcY-xKFNk1AWhHW1TWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18665cc14b.mp4?token=fy1a_g45Vf9_wtm16U5e8IeK3483oQQM8OgT7xvO3k_VaJTl0HmPWgzxSURFuGe2wFv_N9t2K6g1lpp0708Pxt4-62p-rv3HRIXH5W7eiJQ_pozgU0NxVsTJPfwT5TzP_SR8xwkSwRI1ZiQK-ebovyOVaCkxlRBxU0REQjtGYmQ9hM6ttSG08Qkx05_giypbZWgHyGVmrZn5X6VtHNtMyeZF-CFwbllUVfKOp80ILofr47GnpOzbPiz4ioRV5RxotFuSXj2A3xf70jy6jdUxEkolmpVymWIZrz-T93Zv0j0l3mdM5csvc7vnwE7NXcoxlBozM73UZWOCtD3KU5VNe4FmGtvSGfz6b1wh7-v9Ho7Z_eOwhz98Cxs9VlaUBFa3rvMkX-7tobDuT7H2OH0jSu7u58CKmOTIwibJ4CqbDLk9ySfdgDReTwvkh6xE3z2CX2BAQSIf5aZOxo0gK1kmwcdRRhv_6EnePJIXVE1DL70vGME6A2gjDonbKOHUnYgFw7TNT1MzbVEQ7vGK9FPctlwYTlawJDj9Q9K2kqEKhDpAdXgDOsG2fqxDDD8NtUgZOI85xqJo_ieUpSNHJNtpOdXZbdT1O0Nfr8psy_k270iyN9KZuXW3kblKwIAqGYKeyE1VqXM173qC2gxUbil4OBTQgcY-xKFNk1AWhHW1TWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
شادی نروژی ها بعد از صعود تیمشون به مرحله بعد
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/67173" target="_blank">📅 09:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67172">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmLkMlisL9Lh8vG3w12oCoM1P0OTvaKT7nSzLJQl4FjjA0gxQA0ikvaa8LsKbVPyqjSU0kwdm_TcPzcWkpf7niEtqO7NjjexK8L2p-K67wwP0OL0SXl3dBYpVtY3EID-pjcKofm07ijxV1tBmaLNNA6gEl4GAAbfxZaDo2Nio4GmcjLvV_2sCTkUaImgLp4oWcuy7gdcK2kYD8RDDX5R5vYwZEr5SrkHfbvaeg8nVXVL6t8g58v9x3XZ1v1kL9949HpL5r58Myss1vbORtJOC4vlWaT9JSoshXqT_evy5GAf3FoxVji_4eu3FkqvAfW8rcc-J-Zf5V1HWOrlI0XAkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
‏اطلاعیه ناوگان پنجم دریایی آمریکا در بحرین در پی یک سانحه برای یک بالگرد امریکا که طی آن یک تن از پرسنل مفقود شده اند:
🔴
در ساعت ۳:۳۰ بامداد به وقت شرق آمریکا (ET) در اول ژوئیه، خدمه یک بالگرد MH-60S Sea Hawk که به ناو هواپیمابر USS George H.W. Bush (CVN-77) اختصاص دارد، در دریای عرب فرود اضطراری روی آب انجام دادند.
🔴
در حال حاضر هیچ نشانه‌ای وجود ندارد که این وضعیت اضطراری ناشی از اقدام خصمانه یا حمله دشمن بوده باشد.
🔴
سه نفر از چهار خدمه بالگرد نجات یافته‌اند و هم‌اکنون در وضعیت پایدار در ناو جورج اچ. دبلیو. بوش هستند.
🔴
نیروهای دریایی آمریکا در منطقه همچنان در حال جست‌وجوی چهارمین خدمه هستند که هنوز مفقود است.
🔴
علت وقوع این حادثه همچنان در دست بررسی است
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/67172" target="_blank">📅 09:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67171">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
Join Join Join Join Join Join Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/67171" target="_blank">📅 01:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67170">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f10MIMpcOz0kGdTQbmkTzry4i1l4gRfUf8gtOELDdqeIdfZF36YTSDY9LZkyLn35Iabmq66whEmSwMgMK55z8aOnCi2dQv1F1bDNxcVTibRMkIfUx8sjfiL9NFJoCRdlMQxRVKzix4Er-OxPUEsf8cifWpb7LZeBUjjdEt8ffUVeSvZ6trFAHCqEjJBAjgNOTksf2AF-nwBmtCHT618CThl2ZQZ3tve8KM9WMd7tovCuJosfd5TOSDWV2LtZIyBOB2nn4bcDa1EsGWb16DTamj7o3ukvz7yGWPTUOM6p3puoPvOU2jeFjwC4N8InoHqKba-MUYFKw0xRiFAbgj0Isw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
Join Join Join Join Join Join
Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67170" target="_blank">📅 01:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67168">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OteJF0hYRGEzUIQ9egwX3RlFqS2WK8-hIEknzis_US2kKPDCpMNNGP31P9WgUwAKhdT5oFSlr-Jk_pbP5kHnuPuuYlAtAUDxHJABLeR0nkEem9E3Sf9S5Tn6ImyqnHMJSgoyekC7SVMuV_XCyho9M2vaMjwAmk15ynYVpDUbbsX_yLZ__qRRo2mI3XyJmPjY9xEjtstM1JAO3nkuDLflgafviO2znihGK_KfUU9y7yDlmJpGrCk6zQp-lpYw5eaH95Y8U3ghLZ-LoDjmDoLDNwad43MPE70Mun1QLp7M6K76toYv7CjDF3epUzv0GV0LHIVcBFDU9on2BNXXqLbU1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53ac383b11.mp4?token=HK0c4nagj3XPa-KGgzZDpgOmvlkyVl_hVLgrLI7SJKy6UP0R12QRO92HV_Stz-IJxHQuEQGrblFZ1ShjfH37chUhOH3IfUQ3L4NXep__CGENT2hwpV7zyqU6_-VEbMtYBPGmAHlVpCP85swXB-B5dhQuOpxoBITGBS8aYqed_40BbxrpPIHvakkMHidAvcK4iq3lzH7OnDpQ6RRn-6095Yu7N_dMe9MrHxjOEez2zKAA-E-qJMxp0u0GH3bqWOk9X-mhy2c9iqrsxyB6J9Q2s34awFkApKxBK92kxlWmCp6v74gY96rsdJDtn_udBCVwutKLILxIYewsfNOwlNwbNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53ac383b11.mp4?token=HK0c4nagj3XPa-KGgzZDpgOmvlkyVl_hVLgrLI7SJKy6UP0R12QRO92HV_Stz-IJxHQuEQGrblFZ1ShjfH37chUhOH3IfUQ3L4NXep__CGENT2hwpV7zyqU6_-VEbMtYBPGmAHlVpCP85swXB-B5dhQuOpxoBITGBS8aYqed_40BbxrpPIHvakkMHidAvcK4iq3lzH7OnDpQ6RRn-6095Yu7N_dMe9MrHxjOEez2zKAA-E-qJMxp0u0GH3bqWOk9X-mhy2c9iqrsxyB6J9Q2s34awFkApKxBK92kxlWmCp6v74gY96rsdJDtn_udBCVwutKLILxIYewsfNOwlNwbNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملات موشکی سپاه به مواضع کردها درمنطقه کویا در استان اربیل عراق
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67168" target="_blank">📅 01:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67167">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‼️
ویدیو‌ ای که گفته میشه مربوط به پارک ملت تهران هست و هلال احمر چادر های زیادی رو برای پشتیبانی از مراسم دفن کردن علی خامنه ای در آنجا قرار داده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67167" target="_blank">📅 00:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67166">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b0f2d20b2.mp4?token=qYg_L1GxQOUOxAaZtD4T59PF7Z9qlPLwI5jW7gcbQb77BDQXJtFjYkgWR6E0LGjQCnhBenQneOJnI6qSu9pjl8--bLbPInJ4ai5uXGK5U9DNa2jLmOdGqzg-G6krzbac6tqjMFPUCqcTC-zduHr3BImA6QsYi2BDs86SWcv2CGpovWhPsF_TGZrj4JSqiuBt1OhI1Vt2w9GC54TCqJ49r2bu0RuBymoFoFETx6aMIhMt5N53MWOyWRkm1r6annA5OBdsv_DkvHkKjkNK0yqRjoR6KSjoTy3Nf3vsDVEQ80tT70ETNJ6qDRt4RzeD5ddqJBfdbKy9PW6Pc3neSHntag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b0f2d20b2.mp4?token=qYg_L1GxQOUOxAaZtD4T59PF7Z9qlPLwI5jW7gcbQb77BDQXJtFjYkgWR6E0LGjQCnhBenQneOJnI6qSu9pjl8--bLbPInJ4ai5uXGK5U9DNa2jLmOdGqzg-G6krzbac6tqjMFPUCqcTC-zduHr3BImA6QsYi2BDs86SWcv2CGpovWhPsF_TGZrj4JSqiuBt1OhI1Vt2w9GC54TCqJ49r2bu0RuBymoFoFETx6aMIhMt5N53MWOyWRkm1r6annA5OBdsv_DkvHkKjkNK0yqRjoR6KSjoTy3Nf3vsDVEQ80tT70ETNJ6qDRt4RzeD5ddqJBfdbKy9PW6Pc3neSHntag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یک آخوند:
در خانه ای که اسامی محمود،احمد و محمد باشه فقر وجود نداره.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67166" target="_blank">📅 00:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67165">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
🚨
نماز میت بر جنازه علی‌خامنه‌ای توسط یکی از مراجع تقلید خونده میشه و خبری از مجتبی خامنه‌ای نیست
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67165" target="_blank">📅 00:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67164">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44959f900a.mp4?token=DfVlD3sxJDhPTnnGc6qI63aYCxLYrMRQ5wwdUeZ4zHww6_knArVFxipVnyD99OJrFLzigg9NmKXVFtkwDdDCp-Cq-siXg8G3TZZmKRl-vb28tY1Cnagz_YNLzc2RqtjfkdlgEo7M6d9MC2DH75yowgKalgCl6mTCjGDwsu1W7eb3Sy3avVXuNUQ4cKmhzucQx-XNMwdpTih8R36c2w5mUDyya3Hi13yjP75AnI0rU1jfDHkyXbxPIQvPrBz90gAXWlsGy6a81RYyrpKFn0Bkcggr1yYL7evd_Mzyqh3oz3tng-OQ9JG6UMnpmD4m5QI94cd9Oqkzy_bzXsmH_5a5RmG2Dx0fp1QUNpKsLAWIdtkj2mbWhUTS_lYjPxsJmahHrQYNprWk1y8DT4Ir6ywVNaHnubZCOtdjuglRhIclGakrCSxEoUi8JgfmIB0-HJbRDNz5SctwfDll8lYmxdL_fZeDoezfNBfcpc-2Qdk3L-p57rvpXAl5eBTTVm5JogEOJiV3x1jMjwueV5jvvtzdFKGsn5OOJMBT63MKi-y1SgM5pCzoC8ebVTxEsE06Emv4UOb6A-VE2S-nrJ_b0IKHzheG3COIl7FQ9b5BMhfB-oybl0i5HLG3No9W9k2u78cMHjghTUe6vb8h16vKPj9f31ojEVPm8gD_8tounivNRrI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44959f900a.mp4?token=DfVlD3sxJDhPTnnGc6qI63aYCxLYrMRQ5wwdUeZ4zHww6_knArVFxipVnyD99OJrFLzigg9NmKXVFtkwDdDCp-Cq-siXg8G3TZZmKRl-vb28tY1Cnagz_YNLzc2RqtjfkdlgEo7M6d9MC2DH75yowgKalgCl6mTCjGDwsu1W7eb3Sy3avVXuNUQ4cKmhzucQx-XNMwdpTih8R36c2w5mUDyya3Hi13yjP75AnI0rU1jfDHkyXbxPIQvPrBz90gAXWlsGy6a81RYyrpKFn0Bkcggr1yYL7evd_Mzyqh3oz3tng-OQ9JG6UMnpmD4m5QI94cd9Oqkzy_bzXsmH_5a5RmG2Dx0fp1QUNpKsLAWIdtkj2mbWhUTS_lYjPxsJmahHrQYNprWk1y8DT4Ir6ywVNaHnubZCOtdjuglRhIclGakrCSxEoUi8JgfmIB0-HJbRDNz5SctwfDll8lYmxdL_fZeDoezfNBfcpc-2Qdk3L-p57rvpXAl5eBTTVm5JogEOJiV3x1jMjwueV5jvvtzdFKGsn5OOJMBT63MKi-y1SgM5pCzoC8ebVTxEsE06Emv4UOb6A-VE2S-nrJ_b0IKHzheG3COIl7FQ9b5BMhfB-oybl0i5HLG3No9W9k2u78cMHjghTUe6vb8h16vKPj9f31ojEVPm8gD_8tounivNRrI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
قالیباف خطاب به مخالفین مذاکره: بیشتر از این آزار ندهید و حرف‌های ترامپ را هم غرغره نکنید
نه در دیپلماسی کمک می‌کنید؛ نه در جنگ!
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67164" target="_blank">📅 23:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67163">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QholPqlGVaOZzWnusWlo0lwI3YAHYn0HyP36z-tE5JMMO_zX5awY5HZdUbB0NFtSbu6H6DiEoKPJHKaPMDlY539U7iq9TGVnqR7BpZnpytry3cetZU_QToaUpghq-CyAVeUGBANyN0zl16Yafx_JOhleY0UftlKVDgmbxg2ckyGkDmf3bf06reHUsvORUtnjjRymxStIlPhgnX_3rvXUuUSIXtICU8hePzQhcY6rOjtt9nYFlURS2RgGkkf9lpYwyT1uHMCJE9ZQZj9Lp-ekAVPLfGM3hVOk8FVwWubstcc_a7ZvTe0CW45sIW1y2nds5XG2ROTqRUmL2YXnJohTFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
برخی مطرح کردند که چرا اعلام شده ۲۰ میلیون بشکه نفت در اختیار فلان مجموعه قرار گرفته و این موضوع را افشای اطلاعات داخلی دانستند. اگر بار دیگر نیز چنین شرایطی پیش بیاید، نه ۲۰ میلیون بشکه، بلکه ۱۰۰ میلیون بشکه هم در اختیار آنان قرار خواهم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67163" target="_blank">📅 23:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67162">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/076f83ca5a.mp4?token=XDFDKIXpOjeRpaQCs5lqIhMbjDJf2S6fPFf1Z12CkBVOIxHnAlkzXs2zkGci3tYawplQ-3J5HPlKCNo1pkq0hkL_a_CHqBTGfegG4103-zxJGyf0gk6BNBq1mvxmWc_voQUGzwZQOdNcuTrYQxVGY5Jt6nDt2NQW9AT3hucP2j0C_3E8GffqEmONerOMULdTJToCDqrSlu2ufgRM88jqjOEW-Clewjw-CmL3VxkSCxyESx__s-Q1iJYx0ZcULGU2KLJHA4pgNHgr9tGLN6pX0kBTBSzdNGNhEzcyf_Hzi-p4vF0KWPV-YlCKiqCM-zK-xFFHka83-xNn73uyrvM-5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/076f83ca5a.mp4?token=XDFDKIXpOjeRpaQCs5lqIhMbjDJf2S6fPFf1Z12CkBVOIxHnAlkzXs2zkGci3tYawplQ-3J5HPlKCNo1pkq0hkL_a_CHqBTGfegG4103-zxJGyf0gk6BNBq1mvxmWc_voQUGzwZQOdNcuTrYQxVGY5Jt6nDt2NQW9AT3hucP2j0C_3E8GffqEmONerOMULdTJToCDqrSlu2ufgRM88jqjOEW-Clewjw-CmL3VxkSCxyESx__s-Q1iJYx0ZcULGU2KLJHA4pgNHgr9tGLN6pX0kBTBSzdNGNhEzcyf_Hzi-p4vF0KWPV-YlCKiqCM-zK-xFFHka83-xNn73uyrvM-5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمله پسر سردار طاهری به پزشکیان:
مگه نفت بابات بود که می‌گی ۲۰میلیون بشکه نفت دادیم به نیروهای مسلح تا بجنگن؟ اگر نیروهای مسلح نبودن ما نمی‌تونستیم اینجا شعار بدیم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67162" target="_blank">📅 23:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67161">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7f1bdcd52.mp4?token=pRI4kKETA8zYizHEvbUglYguhycBpIX7E-LxavtwYIdBjDDnvf0scPA2Fy1kFI26_phvrtm8gtI5qu_QHW0fFn-sBPurtpSvxqu9oSifjncaPMQabpC0ZeUf5AId39Zny4465yFQzCe7CclZOv90t3k9UGM9SMAGrhzQU8QH2hxutthMGb1ccJA06dGMPGIgS9nbXvb5Q_TUit5BtWWBBl3htnLXTdEL7J_rvwzvaBs5x3a7OcoAP5DOEXt0gMpnenzhnUT9Wi8ems_McvoC1JdRxi0ByrdHV_b6DdikU7wQlZdL7iYqZXJ4iusfiVwSut62Fop8cogqlIa6P5tjMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7f1bdcd52.mp4?token=pRI4kKETA8zYizHEvbUglYguhycBpIX7E-LxavtwYIdBjDDnvf0scPA2Fy1kFI26_phvrtm8gtI5qu_QHW0fFn-sBPurtpSvxqu9oSifjncaPMQabpC0ZeUf5AId39Zny4465yFQzCe7CclZOv90t3k9UGM9SMAGrhzQU8QH2hxutthMGb1ccJA06dGMPGIgS9nbXvb5Q_TUit5BtWWBBl3htnLXTdEL7J_rvwzvaBs5x3a7OcoAP5DOEXt0gMpnenzhnUT9Wi8ems_McvoC1JdRxi0ByrdHV_b6DdikU7wQlZdL7iYqZXJ4iusfiVwSut62Fop8cogqlIa6P5tjMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فیروز کریمی:
قلعه نوعی 5 سانت رو تحمل کرد 10 سانت رو تحمل کرد، 30 سانت رو دیگه کجاش بذاره
🤣
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67161" target="_blank">📅 22:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67160">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7be0c9f31d.mp4?token=VClrxKsRR0psolAiE6Hul4svZ6ux0-YJ4v8JO2aoUZFQJK5rjDmhaFEboj2NTnF5CuQYHV_9X-F3gey1wk-Bn79Jj9CsTECEj7zcaLxsoXfiIh1Tmm7NQ2XXByWEMfqnQoM0EGTTN0s217q2FY39wSvqdgg0mDuvWX7sKUZM54uew9lGjEFWdx1UhhqYPJYrp9e3qBSaw2LeYET9Kt3Rd9K7bbcH7aYWkneOLVqcJ9oFhn04PV68Bhvs3lLU4Nx6eYhQbhoLJjJXd6hOAe86vzQmdwh0YaQtZFy-iz8T8EaqLFOH4ANaO9gW7hIZ8OLbPz6eBBvP-iI8nKMcJutO_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7be0c9f31d.mp4?token=VClrxKsRR0psolAiE6Hul4svZ6ux0-YJ4v8JO2aoUZFQJK5rjDmhaFEboj2NTnF5CuQYHV_9X-F3gey1wk-Bn79Jj9CsTECEj7zcaLxsoXfiIh1Tmm7NQ2XXByWEMfqnQoM0EGTTN0s217q2FY39wSvqdgg0mDuvWX7sKUZM54uew9lGjEFWdx1UhhqYPJYrp9e3qBSaw2LeYET9Kt3Rd9K7bbcH7aYWkneOLVqcJ9oFhn04PV68Bhvs3lLU4Nx6eYhQbhoLJjJXd6hOAe86vzQmdwh0YaQtZFy-iz8T8EaqLFOH4ANaO9gW7hIZ8OLbPz6eBBvP-iI8nKMcJutO_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار: آیا می‌توانید قول بدهید که آمریکا قبل از تمام شدن ۶۰ روز تفاهمنامه، دوباره وارد جنگ تمام‌عیار نشود؟
​
🔴
جی‌دی ونس: ترامپ تا وقتی که مجبور نباشد، نیروهای نظامی را دوباره به جنگ نمی‌فرستد.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67160" target="_blank">📅 21:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67159">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
آکسیوس به نقل‌ از مقام آمریکایی:
در مذاکرات دوحه تفاهمی حاصل شد تا اوضاع هفته آینده آرام بماند تا در اجرای تفاهم‌نامه پیشرفت حاصل شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67159" target="_blank">📅 21:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67158">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HYgyMiJG7s7cogrrlNJkqBgUCIGkbQATJg9RBVbh7zPQ7tpLJXAUclrm-3PmMN0HyGQRbgEXeX91bPCwZ8C_2JxuJhH8FB4lu5JifsnExB-TdqZA2xxuq4W1Xp_x3PRdKDp24vheh2ssg45fK4qALqTqstTLyS2ql9yiIRSce5-bt99HzYZkSbIYbzeOPRl-D2uxg3kqy53YAB2hruu9uffL27AsQe-KijUW5otHzTS77FQdM6KPGbyLFn-4b8kvfHAredIFrrNNev8wuVNMxl6jpxh491G1BxQ0aniTvM47SIf5VGXOMFJqd_YUrMVekEAqmATYjBPlvQC05NaGEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آکسیوس:همزمان با از سرگیری مذاکرات در دوحه، ایالات متحده تلاش می‌کند تا ایران را از پرداخت عوارض منصرف کند.
مذاکره‌کنندگان آمریکایی و ایرانی در دوحه برای مذاکراتی با تمرکز اصلی بر تنگه هرمز حضور دارند و دولت ترامپ مدعی است که ایران از توافق هسته‌ای سود بسیار بیشتری نسبت به عوارض عبور و مرور در این تنگه خواهد برد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67158" target="_blank">📅 21:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67157">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b973f48d61.mp4?token=PklQcGZvz1ltJQPWyoLPeflIi3pMY_6tkKpz58cPWooFO5mODJ19QiEwEm43DRVNaTZr56yWZNEzhQgZ8___x_3PAvt-UnahmYseAchCgbsPtGv2K5wvuN1n-EEluc-G0gllXWCvHPVic6o7O6PrizqApQ2imOk19AO_7t_p7v5hfSzggKlrbwW0YjBpa_UFh86wlMbqIRWJufwL34RZmwgM4Qnc4HIdnLZzWq1hofc7UhRn3zaTwYSGyr2uOALZE1Ql6urzHTGwp2Q6D7l6wJiSfSjU9OeUxCdOhwuqorhRYCPiNeKe1xY0XFFiPGGVLxCMI5iBzCPIoq_y3zzbHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b973f48d61.mp4?token=PklQcGZvz1ltJQPWyoLPeflIi3pMY_6tkKpz58cPWooFO5mODJ19QiEwEm43DRVNaTZr56yWZNEzhQgZ8___x_3PAvt-UnahmYseAchCgbsPtGv2K5wvuN1n-EEluc-G0gllXWCvHPVic6o7O6PrizqApQ2imOk19AO_7t_p7v5hfSzggKlrbwW0YjBpa_UFh86wlMbqIRWJufwL34RZmwgM4Qnc4HIdnLZzWq1hofc7UhRn3zaTwYSGyr2uOALZE1Ql6urzHTGwp2Q6D7l6wJiSfSjU9OeUxCdOhwuqorhRYCPiNeKe1xY0XFFiPGGVLxCMI5iBzCPIoq_y3zzbHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«روند خلع سلاح هسته‌ای ایران به‌خوبی پیش می‌رود... بازار سهام تقریباً هر روز در حال ثبت رکوردهای جدید است. قیمت نفت به‌شدت کاهش یافته است... و اکنون از زمانی که من حمله به ایران را برای جلوگیری از دستیابی آن به سلاح هسته‌ای آغاز کردم نیز پایین‌تر است.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67157" target="_blank">📅 20:27 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67156">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1792b01078.mp4?token=HNo5Z-ROlR8XFJz9v3WwwNlFmdsIE1Y-Lo3-fVdfbqK3qN-Dzn0U5j6V6oD1bPBik7JkMQRDiOMCp9QqdF_5HFy7jDMdlMSBol_t41ACg2hqg1DQ7wImyQflFAeJZjlPMBmXUpQcNjpH0p2nlgqhv3zD_VFyiB5XTlGIQxLxl8ZEi_90owepbC4NxbpCO-Ar1tj-w_bqYNmaPHT7R3nr6nslrECishiNiMTovRvzDNb9jE9Fba8keuTW9iPkRlE38EOB1XXgXIUGPaPAn3b-AWWc4WTrO5NyRtdqHkfJCcq7fAGFI-zoLmc2R3VNjmdEr8MGmuUI22oS5rIRqpzv2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1792b01078.mp4?token=HNo5Z-ROlR8XFJz9v3WwwNlFmdsIE1Y-Lo3-fVdfbqK3qN-Dzn0U5j6V6oD1bPBik7JkMQRDiOMCp9QqdF_5HFy7jDMdlMSBol_t41ACg2hqg1DQ7wImyQflFAeJZjlPMBmXUpQcNjpH0p2nlgqhv3zD_VFyiB5XTlGIQxLxl8ZEi_90owepbC4NxbpCO-Ar1tj-w_bqYNmaPHT7R3nr6nslrECishiNiMTovRvzDNb9jE9Fba8keuTW9iPkRlE38EOB1XXgXIUGPaPAn3b-AWWc4WTrO5NyRtdqHkfJCcq7fAGFI-zoLmc2R3VNjmdEr8MGmuUI22oS5rIRqpzv2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
قائم‌پناه، معاون پزشکیان:
اگر قرار باشد هر آنچه رهبری می‌گوید اجرا کنیم که دیگر نهادی نباید وجود داشته باشد
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67156" target="_blank">📅 20:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67155">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e20aabab5a.mp4?token=DeHILDWTmJL1wk2DNhrzkpBKX9gOcu2M5sNlr-spSobokvWPHD23lqRxai1CBeUZENT6qtJwfvY9XKsfW9FZhZjDEJZx1_1FV972nzS0b_uea5I9qbhuuw-XVdVZpVcdQKWg7uUKqF0TFdupE8XvHe-UIX0Of9ealmjUGDGVjfle2HTwQzUnZwu6tVzvUMOyTppqKY5wBG2odYnf1ErwpKLyoZFGi7pXoySp-p6wFPeoVT7GNRJ9BOC3GORho_2dZgLWPcmpV_sOB3rPYO9JjtoFSxyEAgbx7cxkdWvlbyuqlJm9JICjJlqVDfzD4GdLHdQrROCPUbIquDwAqi9pXRS4M_0cULdUEoqsmpMxqgExav5jrKSalebJHuW4uXvDIR8HaZC-b7EoC7BKe9lsjaCoLGFY7Afi-tVyA48c_DoYCuGC28Z9rURvLAghZlhobvUZW46Qvy7gPl3H--vVR74jh-eog4q2ZnVIJBzHSM4_xQmef5acnm1DypnzhAHEbmcbkg3YrYzw7rpTqv-AHnNJuQ5Tm1CArTyIhzxzn6jSXDK7tqFCH0wlspNrxJFlX3Ng8xziLQ38J9WjHwiPp0TMgHuKpaLCqFAzKrN8YdfEMcwkMvR5u3VFhsEQGWG8Mya3pu10UyQheBYB83IoMMLnmPxZ-5n4rxkWy4pRozU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e20aabab5a.mp4?token=DeHILDWTmJL1wk2DNhrzkpBKX9gOcu2M5sNlr-spSobokvWPHD23lqRxai1CBeUZENT6qtJwfvY9XKsfW9FZhZjDEJZx1_1FV972nzS0b_uea5I9qbhuuw-XVdVZpVcdQKWg7uUKqF0TFdupE8XvHe-UIX0Of9ealmjUGDGVjfle2HTwQzUnZwu6tVzvUMOyTppqKY5wBG2odYnf1ErwpKLyoZFGi7pXoySp-p6wFPeoVT7GNRJ9BOC3GORho_2dZgLWPcmpV_sOB3rPYO9JjtoFSxyEAgbx7cxkdWvlbyuqlJm9JICjJlqVDfzD4GdLHdQrROCPUbIquDwAqi9pXRS4M_0cULdUEoqsmpMxqgExav5jrKSalebJHuW4uXvDIR8HaZC-b7EoC7BKe9lsjaCoLGFY7Afi-tVyA48c_DoYCuGC28Z9rURvLAghZlhobvUZW46Qvy7gPl3H--vVR74jh-eog4q2ZnVIJBzHSM4_xQmef5acnm1DypnzhAHEbmcbkg3YrYzw7rpTqv-AHnNJuQ5Tm1CArTyIhzxzn6jSXDK7tqFCH0wlspNrxJFlX3Ng8xziLQ38J9WjHwiPp0TMgHuKpaLCqFAzKrN8YdfEMcwkMvR5u3VFhsEQGWG8Mya3pu10UyQheBYB83IoMMLnmPxZ-5n4rxkWy4pRozU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی‌دی‌ونس:
«من واقعاً فکر می‌کنم ایالات متحده، فارغ از اینکه مذاکرات در نهایت به چه نتیجه‌ای برسد، در موقعیت بسیار خوبی قرار دارد.
اگر مذاکرات موفقیت‌آمیز باشد، که بدیهی است ما می‌خواهیم چنین باشد، با ایرانی روبه‌رو خواهیم بود که به‌طور دائمی دگرگون شده است.
از سوی دیگر، اگر ایرانی‌ها رفتار مناسبی نداشته باشند، برنامه هسته‌ای آنها همچنان نابود شده است، توان نظامی متعارف آنها همچنان از بین رفته است و ایالات متحده نیز در مقایسه با ایران همچنان در موقعیتی بسیار قدرتمندتر قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67155" target="_blank">📅 19:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67154">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1035b1e35.mp4?token=V40tz_EKFtUbtV8zS1uawXM_D9bgLcy8xWkfLiWuqgrxX9RTEHdG-yxJMfphZB6OFrdcGiZDQdsbtpOBDYPzfFH1BKZqmrR53dJkXncnLZOs_yLImFJ9oAocgin0-A_MSCVqn8ZYtFl8-pfcDa9jeoiWrIoZqG04eU0jGyD4NOf0-Iz3G8atJtYl1wEyjM1aD8Yiz1BJHiMwZafWBRvCtPHX6bM7gJ3LRP-5pQl7dzd6Au--yWcI5v3oJeNbBfcySimkyeVbu9a1A0MXXrouYsRboytYdNcLfnAcW2gj74Kg5via2TWNgev7k-_HzlUVNx3qM7lTmatwOz0d42vUFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1035b1e35.mp4?token=V40tz_EKFtUbtV8zS1uawXM_D9bgLcy8xWkfLiWuqgrxX9RTEHdG-yxJMfphZB6OFrdcGiZDQdsbtpOBDYPzfFH1BKZqmrR53dJkXncnLZOs_yLImFJ9oAocgin0-A_MSCVqn8ZYtFl8-pfcDa9jeoiWrIoZqG04eU0jGyD4NOf0-Iz3G8atJtYl1wEyjM1aD8Yiz1BJHiMwZafWBRvCtPHX6bM7gJ3LRP-5pQl7dzd6Au--yWcI5v3oJeNbBfcySimkyeVbu9a1A0MXXrouYsRboytYdNcLfnAcW2gj74Kg5via2TWNgev7k-_HzlUVNx3qM7lTmatwOz0d42vUFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز یه عده کسخلِ پا شدن رفتن فرودگاه که از بازیکن‌های تیم میلی جمهوری اسلامی استقبال کنن. مثلا می‌خواستن شبیه هواداران تیم ملی نروژ به سبک وایکینگی تشویقشون کنن که اینطوری ریدن
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67154" target="_blank">📅 19:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67153">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aDJsvY-k3nQIop3kZT_kC77Fat9Mw5L827i1q2iH6STE7m1C4SqKsTLKAowN3o6jE_foJ9Ur1Bcbs3BpjpGC3Du-xidc_Mx2QroNjumzy6e_TB5Ppjgs-L0O8XrZZh-MfZAn36qJk5QDxYQX1VtiGdqF_PcQe-gbz_WVst-fKsh7fxrg1fxHh5kOXtsPUSzhx4i12LMH2he5Z5nwKW4W6Xc5T6i3Ea4MDPpmAjbPMJ5Pc_JqnXKcO1ekxxgSbxmDP-GiuGy0yZaBU24Kik0bi1O63fKjtReqmvkFTQAPVmyKQK6L4xGBiBa8lqseBQuA-MSgCqLn5mVQDtCigd35SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
به اعضای تیم ملی فوتبال کشورمان که امروز به ایران عزیز بازگشتند، خداقوت می‌گویم.
تلاش و مبارزه با تمام وجود و تا آخرین لحظه، مهم‌تر از پیروزی است.
کار علمی، حفظ روحیه، رویکرد تحولی و انگیزه بالا شرط پیروزی در آینده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67153" target="_blank">📅 18:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67152">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b5b7ea7b3.mp4?token=Veg60JzaBpjDwOLAon1d2_OiBHZZjIiv3ypvOGvk6IJ9KKRgaED8rPDfRHt7Ra0Jv76sKQ8DK1C_YghNzz3Ej_UWEVJ16A9kkFWruq-qfnqFKTNQfNl6hC0ZJ7yIEV_pB0uzKkB88_0LJEgfAoNoT2HfwotISlzEBsTO_dKpaXWWMb7N3BfEebVQPooz52ZuGWbTrra9TpUlB3UN-sxguCl6qm-Drwdx3R1zqknvXX3_w7BAQi8NM_8FHpoCrZsVgC-vz5CrNoDY62JOEfufOd4umebb6pGxnIgfrOWFj-ehZDjaZfeJoz_DlDO1-DZmk1CvLtjmUz0jiEqNs-qDgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b5b7ea7b3.mp4?token=Veg60JzaBpjDwOLAon1d2_OiBHZZjIiv3ypvOGvk6IJ9KKRgaED8rPDfRHt7Ra0Jv76sKQ8DK1C_YghNzz3Ej_UWEVJ16A9kkFWruq-qfnqFKTNQfNl6hC0ZJ7yIEV_pB0uzKkB88_0LJEgfAoNoT2HfwotISlzEBsTO_dKpaXWWMb7N3BfEebVQPooz52ZuGWbTrra9TpUlB3UN-sxguCl6qm-Drwdx3R1zqknvXX3_w7BAQi8NM_8FHpoCrZsVgC-vz5CrNoDY62JOEfufOd4umebb6pGxnIgfrOWFj-ehZDjaZfeJoz_DlDO1-DZmk1CvLtjmUz0jiEqNs-qDgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی‌دی‌ونس:
ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی، بازارها و مخازن رو از نفت پر کنه،
و بازار سهام و اقتصاد رو درست کنه
بعد تصمیم بگیره با ج‌ا چه کنه!
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67152" target="_blank">📅 18:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67151">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5127a5f793.mp4?token=p2hTUFlammzMYA4DTcWkt35JO8E0D5j2FsBit5v3mV883917rBtX3viAARIyeJlLoJVjjwJI5Xt32UNHTBMJ0eUO87oG17jdaeCu4LYFKyw0OJJIPHMd6-5sVoSfAyxb7nkJu7FK06CFihOqLSc_Xxp84viPdLFI6X-Sx-_EUXvox6Q-OSuRR_elH0-J1rphjxwNi-7HDeq7ByRvtF5gpqZ3z72yGKyktfC5UJnjCQKxmPqswobc3jQYIrrZmD9ic4absy1AXdEdfhm4Y49RO9KM_u_Umeo31JnHMpXmw5WX1AeBdZ7BPrH-4pTWDKeoyw75GlTb8MzjFWvlciC8GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5127a5f793.mp4?token=p2hTUFlammzMYA4DTcWkt35JO8E0D5j2FsBit5v3mV883917rBtX3viAARIyeJlLoJVjjwJI5Xt32UNHTBMJ0eUO87oG17jdaeCu4LYFKyw0OJJIPHMd6-5sVoSfAyxb7nkJu7FK06CFihOqLSc_Xxp84viPdLFI6X-Sx-_EUXvox6Q-OSuRR_elH0-J1rphjxwNi-7HDeq7ByRvtF5gpqZ3z72yGKyktfC5UJnjCQKxmPqswobc3jQYIrrZmD9ic4absy1AXdEdfhm4Y49RO9KM_u_Umeo31JnHMpXmw5WX1AeBdZ7BPrH-4pTWDKeoyw75GlTb8MzjFWvlciC8GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت‌ترامپ :
روند خلع سلاح هسته‌ای ایران به‌خوبی
پیش می‌رود… بازار سهام تقریباً هر روز رکورد تازه‌ای ثبت می‌کند.
برای سه شب هم محکم بهشون حمله کردیم
الان هم روند مذاکرات خیلی خوبه.
قیمت نفت به‌شدت کاهش یافته، حتی نسبت به  زمانی که حمله به ایران را آغاز کردم ،
الان نفت رسیده به ۶۷ دلار،  پایین آمده.
هرگز به سلاح هسته‌ای دست پیدا نخواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/67151" target="_blank">📅 18:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67150">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحاشیه نیوز</strong></div>
<div class="tg-poll">
<h4>📊 نظر شما راجع به عملکرد پزشکیان و دولت او حول و حوش مسائل جاری در کشور چیست؟</h4>
<ul>
<li>✓ بسیار ضعیف</li>
<li>✓ فاجعه بار</li>
<li>✓ شکست مطلق</li>
<li>✓ بعدها شاهد عواقب خوب و بد خواهیم بود</li>
</ul>
</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/67150" target="_blank">📅 18:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67149">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‼️
آخوند قاسمیان:
واشنگتن رو اشغال کنید؛ ترامپ رو دستگیر کنید و بیاریدش پیش مجتبی.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/67149" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67148">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/257f4db3ce.mp4?token=BqldS9hhoblnQvaOnReDgXXe-V-AsqSVTy81EdHnt38CbiEC7vTmoTTYCjyuBEBDKBshPS5wbvBamvorxg4PJwpw1aYchQBGR23xFFSiXNLZMKemb-wEPdkGPydNlBaY5Gmq_Wy8l0sIvuaeylZxRgljCnd9TDFOe8-gWRJFYdlE0lARE9bDN9XVMhu3Un02GhjuUOsowTjCuBJPJaMlqyaBaLBZs3kjLI9g0B6EEL-t2pexM6Whv1nSb-vg3IH8f5CSUALXvlyDDvhcQHxArfNln2vILlHyO2W2DhmGZyQmcjwOoNcYIaOsYadkbBsHvWCjfJHTN-G6jEXAyD-5iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/257f4db3ce.mp4?token=BqldS9hhoblnQvaOnReDgXXe-V-AsqSVTy81EdHnt38CbiEC7vTmoTTYCjyuBEBDKBshPS5wbvBamvorxg4PJwpw1aYchQBGR23xFFSiXNLZMKemb-wEPdkGPydNlBaY5Gmq_Wy8l0sIvuaeylZxRgljCnd9TDFOe8-gWRJFYdlE0lARE9bDN9XVMhu3Un02GhjuUOsowTjCuBJPJaMlqyaBaLBZs3kjLI9g0B6EEL-t2pexM6Whv1nSb-vg3IH8f5CSUALXvlyDDvhcQHxArfNln2vILlHyO2W2DhmGZyQmcjwOoNcYIaOsYadkbBsHvWCjfJHTN-G6jEXAyD-5iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حمله امروز اوکراین به پالایشگاهی در حاشیه مسکو
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/67148" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67147">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
📣
همراه با تست رایگان  جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn @kaviani_vpn</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/67147" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67146">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KZTPfpz5NopvJLsfK3FXX5spMTfp9meLNGOUKe1Ue_4PlUpDF4OZgamr3FGMRUysyxv4v7ACUDacMraIpKYe-QKiVocpKUY-U7ljh9XCeZalhsbBnTbKCJ6xcSqJGTyHRaSkfNylaYapxv3nAUUtLR2mOSlW9X8yaEtNTwRAY8Eu35tnfYt-LYzrN6NDqHnXBxiLjKKBrsR8Y-_ubI4GIXLjEGHuQWDJANyZwUElh9RhZuF3CWQfGMi6RcQ8TCzSpBbvSzGIXjTU2YWT_n5Cm5BzxgP6Nbxm4TeJpjGioMUvO5aSbmKYXOV_2OcwkeJslcKwMHV-0vQjhAYZb5j_Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
📣
همراه با تست رایگان
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/67146" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67145">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/158f79bda3.mp4?token=Naqv0PqVUyAhUoV9SFCkB9WQDGyxxBZvRWq1oEuYY5c_flO8DnJMUuwpH3zUqgZWu6AKsQnskp-5D88n9C_f9hb1GWFskr8Ym2N24VAIFj-H162cMMTlOzEJzOzpolNXFoIrVCS2O3UEANyXFHzOHBOwxD1G4q4al3HPtz19R4ZhSywFzNRVP8zq7aDZjdPajtLSgQ9aSD5APlNgcuf5fwiZf4AtLXnxY70ypE3FxxrlbyLgq87dd-aOSuYI1XROzBsRTt_XQ8x-o9ZR1es4av8xQ3Y0nhzdVGy2ZFMAao2urnoc8726iUuWLEAEna_FvBtEakoXmL9M7fOLN587Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/158f79bda3.mp4?token=Naqv0PqVUyAhUoV9SFCkB9WQDGyxxBZvRWq1oEuYY5c_flO8DnJMUuwpH3zUqgZWu6AKsQnskp-5D88n9C_f9hb1GWFskr8Ym2N24VAIFj-H162cMMTlOzEJzOzpolNXFoIrVCS2O3UEANyXFHzOHBOwxD1G4q4al3HPtz19R4ZhSywFzNRVP8zq7aDZjdPajtLSgQ9aSD5APlNgcuf5fwiZf4AtLXnxY70ypE3FxxrlbyLgq87dd-aOSuYI1XROzBsRTt_XQ8x-o9ZR1es4av8xQ3Y0nhzdVGy2ZFMAao2urnoc8726iUuWLEAEna_FvBtEakoXmL9M7fOLN587Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه تسلیم شدن قوی ترین ارتش جهان رایش سوم (نازی ها)
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/67145" target="_blank">📅 17:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67144">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/44f6e3950e.mp4?token=iazKTzLxoYZpvdhZvtxTglJUp55GWL2jCaDz_kXN9FgtnLWE11OapCm_zffFaRGTfR4Z1QUg-IPAP2wc2HNi1YFVL-EAi3eeKSiBqL2Us01QQ5wM1Jutsr4IFA05CW6GphDGxoTMwzgVjUZT0mqdN2lhzEdOTSpCH8o9GQRaVwF8os8c5Hv9FQaZ4AdCkoDE0GRprBqMVTbt3y_ZK-ClR03dMZhVyB6G2UDEucTyKr9cAaQ_eDdMVL5ViL6DJgfOHX8utxbBrz_8xY7qmuEXlh01cDI6hxrBCScrX6U75PK43Z9at-wl-UMqZWAyX3Q8lhjIAkqxA8cSBk9ylzfIVw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/44f6e3950e.mp4?token=iazKTzLxoYZpvdhZvtxTglJUp55GWL2jCaDz_kXN9FgtnLWE11OapCm_zffFaRGTfR4Z1QUg-IPAP2wc2HNi1YFVL-EAi3eeKSiBqL2Us01QQ5wM1Jutsr4IFA05CW6GphDGxoTMwzgVjUZT0mqdN2lhzEdOTSpCH8o9GQRaVwF8os8c5Hv9FQaZ4AdCkoDE0GRprBqMVTbt3y_ZK-ClR03dMZhVyB6G2UDEucTyKr9cAaQ_eDdMVL5ViL6DJgfOHX8utxbBrz_8xY7qmuEXlh01cDI6hxrBCScrX6U75PK43Z9at-wl-UMqZWAyX3Q8lhjIAkqxA8cSBk9ylzfIVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه جالب و جنجالی یه پسر نوجوون ایرانی که در حال وایرال شدنه:
🔴
خبرنگار: اگه یه دزد خفتت کنه، موبایلتو میدی؟
🔴
پسر بچه: آره، جونم مهم تره
🔴
خبرنگار: خب اونطوری ساعت و دستبند و هر چی داری ازت میخواد.
🔴
پسر بچه: آره ولی جونم مهم تره، اگه ندم به قتل میرسونتم.
🔴
خبرنگار: فرض کنیم آمریکا خفتگیره، الان یعنی ما بیایم موشکی و هسته‌ای رو تحویل بدیم؟
🔴
پسر بچه: وقتی چاقو زیر گلوته و زورت به خفتگیر نمی‌رسه، باید هرچی میخواد بهش بدی، اگه ندی میکُشتت و بعدش خودش وسایلتو برمیداره.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/67144" target="_blank">📅 17:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67143">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1012800172.mp4?token=NutMla6hsUVM3yc1OUNZEAYkXXi1Gla_Y2iMRdIe5wzu9eBBy1NfU9cgRtUl0EIUg71jVxG-SZvKWEtuvqAAQ3DTMDlmz9AqObwOVznLdyNT3P1ZSIPvzEaR0fYtH8Emju3-O3P3GGJcAjI_qQuTBH00hHSbqc7Ozg16ZIl4DBGeuvgOYiHTfqj38Fh2-Fr23wolaL7w8TiAFGhkyVPhQWx-en6OHfWJVxx8Mkxs7cKGF7FevmC4X3r1XCMOQsapBd2VhmxviuxZHpZaiyxDm80dSLR5fQ2BvuvyoKvb4vKHSuKkbHNeQicOu-xQBgvIdEOaYxzTZJvAWivgl6CIZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1012800172.mp4?token=NutMla6hsUVM3yc1OUNZEAYkXXi1Gla_Y2iMRdIe5wzu9eBBy1NfU9cgRtUl0EIUg71jVxG-SZvKWEtuvqAAQ3DTMDlmz9AqObwOVznLdyNT3P1ZSIPvzEaR0fYtH8Emju3-O3P3GGJcAjI_qQuTBH00hHSbqc7Ozg16ZIl4DBGeuvgOYiHTfqj38Fh2-Fr23wolaL7w8TiAFGhkyVPhQWx-en6OHfWJVxx8Mkxs7cKGF7FevmC4X3r1XCMOQsapBd2VhmxviuxZHpZaiyxDm80dSLR5fQ2BvuvyoKvb4vKHSuKkbHNeQicOu-xQBgvIdEOaYxzTZJvAWivgl6CIZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
یک تحلیلگر ژئوپلیتیک چینی می‌گوید امضای تفاهم‌نامه توسط دونالد ترامپ، بیش از آنکه نشانه کاهش تنش باشد، تلاشی برای عبور از «گرمای تابستان» در منطقه است.
🔴
به گفته او، با وجود امضای این تفاهم، نشانه‌های میدانی حاکی از آن است که ایالات متحده همچنان در حال آماده‌سازی گزینه‌های نظامی است. این تحلیلگر معتقد است حدود ۶۰ هزار نیروی آمریکایی در منطقه مستقر شده‌اند و مقدمات لازم برای هرگونه اقدام احتمالی فراهم شده است.
🔴
و پیش‌بینی می‌کند در صورت ادامه روند کنونی، تحولات جدی ممکن است حداکثر تا مارس سال آینده اتفاق بیفتد یا حتی ممکن است از همین دسامبر شروع شود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/67143" target="_blank">📅 16:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67142">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b14da1a69e.mp4?token=iuvrgRjNwJpI2JBNt8ipfIExhl7GRS7XbuH728stjXTzLGA3JBNhhzzjNNw2Mx3Ubt_P0n9e-i92r0BXJzdwrHTHKcjnaKejMvqS_TcOB27lJo5-AZtDXS90RWAO_oEe_nfbWRvCQ5RJDdRNeIWvQpNRG53T8obb-ct_V-eqDO1jYemkCTy5q4ZRAiRajNrZtGXM2XbKTIyMwY4CkkUDUSo51SQGl1x14J42yIk1om3KI6TpfljXhSzs7YSuI-A_phm5UpqFrNpJH3P8zQvdPlgvxnohG4q3-d9JaYAZcZ2VCDH71vJCFD2-pNtAAJiguzn6DyC8xVhXzRn5SQ9TKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b14da1a69e.mp4?token=iuvrgRjNwJpI2JBNt8ipfIExhl7GRS7XbuH728stjXTzLGA3JBNhhzzjNNw2Mx3Ubt_P0n9e-i92r0BXJzdwrHTHKcjnaKejMvqS_TcOB27lJo5-AZtDXS90RWAO_oEe_nfbWRvCQ5RJDdRNeIWvQpNRG53T8obb-ct_V-eqDO1jYemkCTy5q4ZRAiRajNrZtGXM2XbKTIyMwY4CkkUDUSo51SQGl1x14J42yIk1om3KI6TpfljXhSzs7YSuI-A_phm5UpqFrNpJH3P8zQvdPlgvxnohG4q3-d9JaYAZcZ2VCDH71vJCFD2-pNtAAJiguzn6DyC8xVhXzRn5SQ9TKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهریه‌خانم‌چیه؟یه‌پهباد‌ شاهد بخوره‌تو‌قلب تل‌آویو
😐
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/67142" target="_blank">📅 16:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67140">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S-YjiJjv8l7jPGLRKj1h6blr67OGw8vAwtLNm-6Ez0MHSdKPuR3c863yQt-eYcik_Jx_n77wvKZ_LW4MUNxBRHtvgKirBbL89wvZ-yBfVHUKsJT5wl9lzUSnlikupbZEcDivAJfIAWVkR3GT1mNuI4pu5AQssLHy_FheFzn6lun5qIGD9ChnxbfF50gRnlEeELS9J0e_ljHroZthxdGsi1iTkVCQKWtCcU7kG6AY_QGIIzt3eKYAmmPuGKQnNXUjPqL3QL_p33DdHG4EWyfPUc9JUAsfHYQrGfYzKS79DsmWMfL8LsioByWi4-ZSn5sjULW650YhYJf4vURYt8ieEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SWj36e6iRpSAMN98aboWJh9wzUBcdpo9Aqw-56TwYggKQpJ_K57JC4GI3irNFd-mnT4cL4VZlEHNtfd8f4pwmM_oOlmnj3880eiXigHaD1JbxxdjC6suaX6s_OiXwOvaNNAcSiR_dskPFJOV49V7ysBM7sThSIyCZ-DZNn58pd2mVNjuEHZ5ylkw4YanUk7x9KumTGr4_VqAQMwTRRrLPT3zQ50tB6cETAJMsBpn9J7YGs_XNfDGtXgAdH8bAWy8KTIkdX66iVWMIrx5nASOwWipd00WGllFcy1_bDivd8xY_QyJZx2kHT9Cf3Y2D2bhXW3RNMSGemh3KqxpJdwFlg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
کاتز وزیر دفاع اسرائیل:مجتبی خامنه ای برای کشته‌شدن نشان‌گذاری شده.
عباس عراقچی:هر تهدیدی علیه مردم و رهبری ما، پاسخی قدرتمند و فوری دریافت خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67140" target="_blank">📅 15:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67139">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Goq8esVDJKTG_Fwpn_Lh4TD0hByVXxY3ol_GzKD_3O5sdtPP3IXXBJM5mM_UMaq19I9ZmArLJJQF2QZGpV23ufA4J3aJg775qMIw7SIbo7uI0f1MTK3l8R5LKR2JUQeFizJOuuxve5NfBBdaQQSK1sB-psg9uaRB-NWml6gExpU2J-MYB5-9qVx4FzerF5AvF2VQ9OfvE-eta-vPAM5rN7yYWZiIfiNFkgRXt45hp6ZKOIFf7VSVHSwfBt_oUcxWaPh99hvPNZN7V1-iSqcShyEFS0otHjFSh-ZxSknW5UjPEe5JlhikMe-jQXNQRCEwMdVxBX5LuzpDuyQ64L7NaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
علاوه بر ناو باکسر، ناو USS Portland (LPD 27) نیز وارد غرب آسیا شد، کاربرد اصلی این ناو انتقال خودروهای نظامی و تفنگداران از دریا به ساحل است
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67139" target="_blank">📅 14:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67138">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZwuRcwEIrbOvbMCplyQjQDOOLTx_WUDx9eidt0I3Stv3-cvZsNgSRJCWEKQG2EL7ePJ1fhLyRWW9Emc3FKzZWo5BPUtn4M-aEgDLaM76Ns4cxQc_O0QY7p52XGFU2HTvaEnBRI74d2kOw87sVipzI1e0QqW1yS5H7--HSh6rTQhFvHjYJ9HTAD2GXix-XMbouCKdr5pr7akF7pFt9nLAXEBYWAADAoDD5WOsixP5kbf3WXbt3HutjBDnqUA86J-fQV_QBtEvp51l4-rAygxtU_zq9RyenAl6VPh2aM8OriLqVO7uQJw6c2KxRXXE4HceSd_OIWK3yYId8z22NAW1oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عراقچی:
مفاد تفاهم‌نامه اسلام‌آباد کاملاً واضح و برای همه قابل مشاهده است. رئیس‌جمهور آمریکا متعهد شده است که دست‌نشانده‌های خود در تل‌آویو را خفه کند. اگر آنها از ارباب خود سرپیچی کنند، ایران آنها را تربیت خواهد کرد. هرگونه تهدیدی علیه مردم و رهبری ما با پاسخ فوری و قدرتمند مواجه خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67138" target="_blank">📅 14:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67137">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LW03ghaSDhBWidbKEbgGppT4f6LPFRt84fGud3Q9whu97BwI-VVpdls1RKweYjv7T8f97XvitSwqbju-DVDhjAftNnvZHJRopGiGUMwhRgHPmbHYZeQPcPeXPhXXzvYrknMvZEchEMHNnenZ6oy088BU12qdM4pRZ2UYhQ8tXMUQlBd_xsg4OJXgT_xsmgJ5P8oU4ByTUP8U36AqqNPBa4RKeNZ75_7i8pJ7TXNeeEBLUV5HUyGt-8mCsQD76W113Zik4dXc8vjcEEN92vGOv4O5gMDkitiPFocsTAuzXrQXx0IsUZNATFm8DwzdKNclDEhXWN9wTLK8kxO2842B9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
ایران به سرعت در حال بازسازی زیرساخت‌های غیرنظامی خود، ذخیره سازی منابع حیاتی، پیشرفت سیستم‌های تسلیحاتی جدید، جایگزینی هزاران تله نابود شده، به کارگیری فناوری‌های نوظهور و گسترش شبکه پایگاه‌های زیرزمینی و مراکز فرماندهی و کنترل خود است.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67137" target="_blank">📅 13:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67136">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
‏رویترز به نقل از یک منبع آگاه:
گفت‌وگوهای فنی غیرمستقیم میان آمریکا و جمهوری اسلامی در دوحه آغاز شده است
قطر و پاکستان میانجی این مذاکرات هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67136" target="_blank">📅 13:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67135">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc573e7486.mp4?token=uqNGwIKiUOJpoXmT5I6AMqyLetjJGkoc7LCpNqnKPXKLaxCTn7pa_O_j7J5MEVXE_sIopXUMbNL9e5e3NnfEjZ6CRC0tNbsVtlgEgGyQvXRKGGZnYMKK4fsegeUdyCUs3lN7kOTxxk0c2nPYVjqXnwXTdoxCMk_egJRIUhdaTW8rBWQPUCYqHosfpsdR902I9uRREm24LqXnikPKqnmbbKWJu9VHOcL19sI92cGCQbmxfWZIWT0l1AYMYBehkspBPw6gYIoBO20z09J9yrhfK2ZeTsqYPKK1KFGKBzr9m8Z_ooA9__ij8V7VqwVaIvB8lDVDfxKrHLghmxxzyZNrKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc573e7486.mp4?token=uqNGwIKiUOJpoXmT5I6AMqyLetjJGkoc7LCpNqnKPXKLaxCTn7pa_O_j7J5MEVXE_sIopXUMbNL9e5e3NnfEjZ6CRC0tNbsVtlgEgGyQvXRKGGZnYMKK4fsegeUdyCUs3lN7kOTxxk0c2nPYVjqXnwXTdoxCMk_egJRIUhdaTW8rBWQPUCYqHosfpsdR902I9uRREm24LqXnikPKqnmbbKWJu9VHOcL19sI92cGCQbmxfWZIWT0l1AYMYBehkspBPw6gYIoBO20z09J9yrhfK2ZeTsqYPKK1KFGKBzr9m8Z_ooA9__ij8V7VqwVaIvB8lDVDfxKrHLghmxxzyZNrKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
این کلیپای محرم چرا تموم نمیشن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67135" target="_blank">📅 12:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67130">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ahdi-4da1VVeDRjfP0fSks728bq8IR_O5RwMk14P46rgcevRHPMBkZDtd07PP5NikKlVNoMPkH24L-KuWZegOJT3Fp6tTFG65fDZzkHlXgQcEtgUD1F7Uw0QYuBdqmyUdQzZf8F4TdeiKkbYTm5jN-WvAlJ5c3h6AUn40utyKEIJnP6HebfPKfuOWkkB8szgN1gJmAffigTC6axqNNnvt9im_7FlLct9eLYzLoaRwYteBC01qEk4PfJ25P7aKIQ4jHcADoaEbmCg6bfJFJWvPJbCOoKW8l0k1dz05fQef_OJQ1ORaY8eyOd37Diabs9ntHfwrS2VVgfYTYhzh_szOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YqSyDlo9nO8gfEjMA8jnQ1JbTDWcA9xMAmIET_AE8EqMIQQQaNJCdQPs7OYsnhoHcrwxfTcT4HSWjQU2Ih0S-v-wxbX2XbNoWDXw1LeZ4KBqLSzoha5PXsiPO_2ORfogTOmPwkvemEi6IawC4zrMPFic8DDVh4wd0bdOH0oWcdgUzg5w1LWMErzJAwa5T8t3gjzHCbE8wb5kYVyuXFbg8a833OlK_RbpWWMagviLRiblQXVIT47Xbsd9I09RMb7-YrxHWRpJIkYozvWRSJMZp32jLut_cwjRH8bf340uhUkuCbTLeofRaMXCNzso6wTJSxvkU7mF1znFr8SKosgU1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1c8ffd601.mp4?token=jVWNMD4TpStf0QL-W5mWKpwH9SgIFP0A0fkWyg_N-vZo3DbUGxHjUsWk5nch7Nc09Tz15XWjNQl4O4NeNNYrORteNC05dn1irkKpne_N67AKwmgnZeRF5Hai3gRwDplC5c5XppOwe7GmKMV1-1WcklirwMmWi5VSDPlZOFD5kotmeanTTNe9v97lBkgDFs0lxVQtZc61YhPX5QehH8RbhYTJcPfwYmdkXDimF1HUwAgLXPiC_Bu0bZRTaVShHonfc4XMHlYcwSYMExof-5iSK2nJvl4eSg2leShsEekkHelLR-D2JUn9th8RL32DqnQmBErPOtKSH85BqPVt3mNfvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1c8ffd601.mp4?token=jVWNMD4TpStf0QL-W5mWKpwH9SgIFP0A0fkWyg_N-vZo3DbUGxHjUsWk5nch7Nc09Tz15XWjNQl4O4NeNNYrORteNC05dn1irkKpne_N67AKwmgnZeRF5Hai3gRwDplC5c5XppOwe7GmKMV1-1WcklirwMmWi5VSDPlZOFD5kotmeanTTNe9v97lBkgDFs0lxVQtZc61YhPX5QehH8RbhYTJcPfwYmdkXDimF1HUwAgLXPiC_Bu0bZRTaVShHonfc4XMHlYcwSYMExof-5iSK2nJvl4eSg2leShsEekkHelLR-D2JUn9th8RL32DqnQmBErPOtKSH85BqPVt3mNfvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویر منتشرشده از پایتخت ونزوئلا، آسمان کاراکاس را در زمان غروب با رنگ سرخ و نارنجی پررنگ نشان می‌دهد؛ بر اساس‌گزارش‌ها، گردوغبار برخاسته از زمین پس از زمین‌لرزه‌های اخیر با پراکنده‌کردن نور خورشید،این منظره غیرمعمول را بر فراز شهر ایجاد کرده است
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67130" target="_blank">📅 11:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67129">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c160c90364.mp4?token=KsdmAwV0i6bNKoL20HupHNxpGn8zpnqmvviBDRi3OZvXfCrOE0seb_BuELz7Sh20CCf_5ah0SFq7lXTHOXSv_rfPljRt3LGvw6FWvxYr2ke1SUZt5MAnMXxm6b6Z5xt0Oy5dBrBbQaX6kF1DnmPzor9mE5XkSzMJybCLFL5BZbWcGZeB02zUiCIgHAvAXvB6O58jy4C6krcjbct8tuNnjQi-GBdlzw1N-bpHuTvrnvAQnSh7BpY2IV0q9nNeQp46fhqsBO5HS9Amf-dWbS0y5ws_ru9hHX37QmK-FsNMBryGQsTlo_ofiGv8VMnGZ0W8PZ_NjtwTgIXrR21IvhXGeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c160c90364.mp4?token=KsdmAwV0i6bNKoL20HupHNxpGn8zpnqmvviBDRi3OZvXfCrOE0seb_BuELz7Sh20CCf_5ah0SFq7lXTHOXSv_rfPljRt3LGvw6FWvxYr2ke1SUZt5MAnMXxm6b6Z5xt0Oy5dBrBbQaX6kF1DnmPzor9mE5XkSzMJybCLFL5BZbWcGZeB02zUiCIgHAvAXvB6O58jy4C6krcjbct8tuNnjQi-GBdlzw1N-bpHuTvrnvAQnSh7BpY2IV0q9nNeQp46fhqsBO5HS9Amf-dWbS0y5ws_ru9hHX37QmK-FsNMBryGQsTlo_ofiGv8VMnGZ0W8PZ_NjtwTgIXrR21IvhXGeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلعه‌نویی
:
خوشحالم که بزرگان دنیا یعنی آقای مورینیو و
تریلی هانری
از تیمی که من ساختم تعریف کردن.
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67129" target="_blank">📅 11:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67128">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3408dd458e.mp4?token=Zlhe5cgUBkYkkKyTsXHX1lbgmxJIAuji3glU8xvwELHxvC6KkiyeR5ycYWpJQxkJgBC4tevS0XkP87U9J2j7Z2Vkb4DqjcaXOLDVFPydZNusnp-qZQ2wvEH4unOEMwwImjqnZ6pSt1TudvWtshh6HtEMk_XNtvrMAwyl2nzU3h-f__dR0CuPNINBjOq6otAmlH2NIzySaH_evbaEi_LLitzbJEOz3NauRxWo1ZZo6n8BpT9-Jx7ER0jwv6_pO72-p4LYVK24V0YnLB04Quqi691BPbJgO0dlsi4QnMgX9AuX-S9_oOFuMznDISrOF7aU9J1tJJ9jCH5xC18M4lhmvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3408dd458e.mp4?token=Zlhe5cgUBkYkkKyTsXHX1lbgmxJIAuji3glU8xvwELHxvC6KkiyeR5ycYWpJQxkJgBC4tevS0XkP87U9J2j7Z2Vkb4DqjcaXOLDVFPydZNusnp-qZQ2wvEH4unOEMwwImjqnZ6pSt1TudvWtshh6HtEMk_XNtvrMAwyl2nzU3h-f__dR0CuPNINBjOq6otAmlH2NIzySaH_evbaEi_LLitzbJEOz3NauRxWo1ZZo6n8BpT9-Jx7ER0jwv6_pO72-p4LYVK24V0YnLB04Quqi691BPbJgO0dlsi4QnMgX9AuX-S9_oOFuMznDISrOF7aU9J1tJJ9jCH5xC18M4lhmvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یک آخوند:
سازمان انتقال خون باید خون‌های زنانه و مردانه را از هم جدا کند زیرا قاطی شدن این خون‌های نامحرم با هم در رگ‌ها موجب ازدیاد گناه می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67128" target="_blank">📅 11:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67127">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d22600661.mp4?token=pt_1fXmVZTE4IAsyrm6_BMDo5bLseIh3gHvKvjxFmqykhbq8z8sd8HAdjMnvG71OSGGgud9SNBp3B9nIKPZ_OAhB0cgvJ-00dZ7lUEZuFH6vBBTNT3v-ema41VaM4sAMn8Pa6K8YZ5HfNNIfb2HKO3psqHN1C-3pKVRbr4dY27RIfPCpN5pEsKk-JgoVzwtCU5Xs0nVMf84COEdgyhRFHLvrmuO468eX2JktlgOzMIWbTg_TlNH4ErU5rbJCMB5BweDI5cM_kOgBe6ldaHyPnt5l1HaK9q9b4vZaZkqa0pYHveUKCad1PzQVDHn-nq2tZjODinrWq_WhQuD-sOGSWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d22600661.mp4?token=pt_1fXmVZTE4IAsyrm6_BMDo5bLseIh3gHvKvjxFmqykhbq8z8sd8HAdjMnvG71OSGGgud9SNBp3B9nIKPZ_OAhB0cgvJ-00dZ7lUEZuFH6vBBTNT3v-ema41VaM4sAMn8Pa6K8YZ5HfNNIfb2HKO3psqHN1C-3pKVRbr4dY27RIfPCpN5pEsKk-JgoVzwtCU5Xs0nVMf84COEdgyhRFHLvrmuO468eX2JktlgOzMIWbTg_TlNH4ErU5rbJCMB5BweDI5cM_kOgBe6ldaHyPnt5l1HaK9q9b4vZaZkqa0pYHveUKCad1PzQVDHn-nq2tZjODinrWq_WhQuD-sOGSWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نظر ممدانی شهردار مسلمان نیویورک درباره مرگ خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67127" target="_blank">📅 10:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67126">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8383f0c682.mp4?token=M_Y_yLQb-MP6AW0Bfr_ZDA3fBiS4mH3bZ5t7w6sWp7XBXNJEybj2C2jaUL3XMcDbK0VD7egfFQIxB-MzcqwO4CbReBvKdavyypNseoWHBP8SzHKYBDEzVb_7W0VZfRPAtOhXqe9WIuzPBn-qzUMHcBFeeDLDpBryXc9sBbI4ligTZpQAyyY0rClvau4yi5_lorQxawuCJL9MHZNxf3Lsrbe-hhgMhbKlTFdcD83TQEIdu0G2klnIRbxRWicU9y3k44ouKQi15MjZbVl_JrTnXjl2-2tcESCOlndDKUMzrNvg7YQaBS6kXgE_6vLARLVjmVblbTS2CMSzGvLKoOuT-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8383f0c682.mp4?token=M_Y_yLQb-MP6AW0Bfr_ZDA3fBiS4mH3bZ5t7w6sWp7XBXNJEybj2C2jaUL3XMcDbK0VD7egfFQIxB-MzcqwO4CbReBvKdavyypNseoWHBP8SzHKYBDEzVb_7W0VZfRPAtOhXqe9WIuzPBn-qzUMHcBFeeDLDpBryXc9sBbI4ligTZpQAyyY0rClvau4yi5_lorQxawuCJL9MHZNxf3Lsrbe-hhgMhbKlTFdcD83TQEIdu0G2klnIRbxRWicU9y3k44ouKQi15MjZbVl_JrTnXjl2-2tcESCOlndDKUMzrNvg7YQaBS6kXgE_6vLARLVjmVblbTS2CMSzGvLKoOuT-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
نمایشی که قراره بزودی از عرازشه ببینیم:
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67126" target="_blank">📅 10:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67125">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hjEZW-nNx1wrMPTECoiFkCk6kVByc1BKXgSBcj-oOMpRZg00_fwcoxzi0XFSKTiw8CI29gc8-kI5Hs-ksMq2uHgtOqO7nKmvMt1aBKkKFHpuaTnwsPKzLtz0TkSACmJlPfGZqlcMa8PagNhalQGClSX5B-TCfmuS1GVoNwDd5omH3bx3uogCf6MZRaRhMBRA_-R4fcwINSAkrX4BeprP1O8PLxbguhEHaO8QO_aYkxec5kyS5qemf1y1jEw_Nsq0qczBJcZhPA5z9V3dzyKMei8hqxJ2_ABQlTF9MmzsjTR3H7r6qFdXnF5bsWIjUPLbKi5RlmjU1gwkBOxAa7bZNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وال استریت ژورنال:
به گفته مقامات آمریکایی آشنا با این بحث، رئیس جمهور ترامپ بازگشت به جنگ تمام عیار با ایران را بررسی کرده و در روزهای اخیر چندین گفتگو با وزیر دفاع پیت هگست و رئیس ستاد مشترک ارتش ژنرال دن کین در مورد حملات بیشتر داشته است، اما تصمیم گرفته است که فعلاً به مذاکرات دیپلماتیک ادامه دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67125" target="_blank">📅 09:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67124">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GR85dxr_NyqjYdR9I4Mvmll9CLaKbv2ZPcaqN1oofS1ON4aBJv3xUziQH68TXKTK3xh4ORm9QZFTpcavPmxfvuRm_OZNzGaDSUB79n8OyGWHCROOLNZDOqVWfSnM_4LxUi2MECaIw_dK9zzBwxUllxHzcZxyDSfEKkPmFSPIOOuV5pOcZT1XBVsa2KVbco5CAqo7t-KVYkHyq5Y54qhwJ_rtIN1NskIuULjQuxPHzQjXyE2-N05BOiiMdvMZvSw-vJg49JEtQNe6cj_5nJwcTQYFroqR0qKEJFLbOdUyQYV0LfZD5jWl0hzRxVq-eR4HP8Ukrzu2nhdGIo7kWt_7kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
فرماندهی مرکزی ایالات متحده:ناو آبی خاکی USS Boxer آمریکا شامل ۲۲۰۰ تفنگدار دریایی وارد منطقه خاورمیانه شد.
گروه آماده به خدمت آبی-خاکی Boxer (ARG) و یازدهمین واحد اعزامی تفنگداران دریایی در حال حاضر به عنوان بخشی از یک استقرار برنامه‌ریزی شده در خاورمیانه فعالیت می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67124" target="_blank">📅 09:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67123">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
Join Join Join Join Join Join Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67123" target="_blank">📅 02:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67122">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JoI1wzWPQQxAwfgo-0CPF68ork9pb6EW2jnPiy7dfccXwyUv9lMlbKdoSd-73SVKFIMmAQscxeJNrhDIT9QlviIGGOAxeUbh9w9mNFxFOy02Sqwh6SC9WjIq0wyVPA1JlRq1UjDnjT13TKYHH7PbJYDT1gTyo7-3MVJEDeIllYy1sXGDF7WJ19bpR_GGPgvupyNufJvNHXWN1hVERtlBS5LrTmzJ2MVL-tFp_MwetR5iaANqVH3tQvP-XevGKdRBdEVxeKEhVDn7QlpaaZIVLqNLq56e4Fl1RlSpfH2WgKGlRzP016IOq5_VrajLVH8g5CjZYcW5uag7bLMNmc5zdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
Join Join Join Join Join Join
Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67122" target="_blank">📅 02:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67121">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6863c3306.mp4?token=mt0wrZErI92oCyePQI8Xugji_Zkf_PPa9Xgsa4FY0iS9fYSm6PVtSfdqA5QaKm8xbGDvs1oGuz8OA52hE0vgJEMukDvuCZLYSh-zs1992oVmZmJU3F-HLdH0ddkrjQetC9V_stL98IbfSig6nUcqA6ntrV2TQcZnEzjFBewW0MsvV4azRBuHk5lxVpwGCWNsJf_lEuIATRcI8t7aepPeStEy_H0Qs3f-EiAHfQK40DOKgYR0-zSxTsaRHjKI50KimKnOj6b5QFHXdyKZvku_HqoZ4beukmHRsIaNhAFf40KxP4OwJz3W6bxJJatIliFvkUwQetQv6hfGCcnHsZUFSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6863c3306.mp4?token=mt0wrZErI92oCyePQI8Xugji_Zkf_PPa9Xgsa4FY0iS9fYSm6PVtSfdqA5QaKm8xbGDvs1oGuz8OA52hE0vgJEMukDvuCZLYSh-zs1992oVmZmJU3F-HLdH0ddkrjQetC9V_stL98IbfSig6nUcqA6ntrV2TQcZnEzjFBewW0MsvV4azRBuHk5lxVpwGCWNsJf_lEuIATRcI8t7aepPeStEy_H0Qs3f-EiAHfQK40DOKgYR0-zSxTsaRHjKI50KimKnOj6b5QFHXdyKZvku_HqoZ4beukmHRsIaNhAFf40KxP4OwJz3W6bxJJatIliFvkUwQetQv6hfGCcnHsZUFSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
کریس رایت، وزیر انرژی ایالات متحده:
ایران هنوز به هیچ وجه همکاری نکرده است.
جریان نفت از طریق تنگه هرمز به لطف ارتش ایالات متحده است. هنوز هیچ همکاری از سوی ایران صورت نگرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67121" target="_blank">📅 02:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67120">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGmom3N7eMCuKypxJ4gaksF_KAFUucLwZofeP70IfVKeB8BJk4753FGqzYRymfUTP5CB_AHijFbcNvzKSy-U_Jy8ELfW-YNemwGa1uFMx3QUPa26wb4PD_VIbAyxfnMTmfyJc0n4GKc9tUpuoBDTRKK-emXrg9typRJLoJR4ZUbXNBrz-e_4fe4G6A4vODWEgQejBDoXIwBrWaSWTHpgFPT3iGiGVax__IJ0zX-Lhb1OQ1rIvy_UK1TKod8CUCQvFNW3H787grStyD6CpMz6ZEJFwyyu-9yIQb8Ih7oUMlqdmyTdFBckxHHmMF0g1P_oDsHppCwlI7SGeMhXvur0YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تصویر منسوب به تابوت علی‌ خامنه‌ای و خانوادش
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67120" target="_blank">📅 01:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67119">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/387a5265c2.mp4?token=Szn1XrXZF1dX-6kfnqkSjqjNKpadHtHNUOS0o2OOVPweHMZskDsUQQZRhdqAnHltMrLDCGZ--F5UuEJLAS5CnUNzTBq4vMK5A06Rc3SgsHXmSadpsW6MU-gfs5SPHsd2fC3w_fCy6IMsZ-Bmhmg1hg5S9kjb7V9B-FOP1Zg6gkg-y03zakefCkHClS_J-1GsGgQsQ1Kd8fR_b36Jfaum2j7kXwCoTcygHkt_5UTH7f3Oublesb3ZuEI74BArhwYnEBOOKTjgkWc0jkR6J-51CWVyGlefjc346OMH6yCtvVL0gmuytYDLoW-vadMliLnfXJ8HCoFSSt4DWmWVSB7F6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/387a5265c2.mp4?token=Szn1XrXZF1dX-6kfnqkSjqjNKpadHtHNUOS0o2OOVPweHMZskDsUQQZRhdqAnHltMrLDCGZ--F5UuEJLAS5CnUNzTBq4vMK5A06Rc3SgsHXmSadpsW6MU-gfs5SPHsd2fC3w_fCy6IMsZ-Bmhmg1hg5S9kjb7V9B-FOP1Zg6gkg-y03zakefCkHClS_J-1GsGgQsQ1Kd8fR_b36Jfaum2j7kXwCoTcygHkt_5UTH7f3Oublesb3ZuEI74BArhwYnEBOOKTjgkWc0jkR6J-51CWVyGlefjc346OMH6yCtvVL0gmuytYDLoW-vadMliLnfXJ8HCoFSSt4DWmWVSB7F6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
بخش سانسور شده صحبت‌های قالیباف در صداوسیما:
قالیباف در قسمت پخش نشده این سوال، می پرسد: خریدهای قبلی این اقلام که در طول ۱۵ سال گذشته انجام می‌شده، از کجا بوده؟ آیا ال‌سی اینها در لندن باز می شد یا نه؟ چرا الان مهم شد و این حرف‌ها را میزنند؟
🔴
چون نمی‌خواهند بپذیرند با مجوز اوفک صادرات نفت انجام می‌شود.
​
🔴
این قدرت جمهوری اسلامی است به آن افتخار کنید و پای آن بایستید. این سند شکست آمریکاست و ما با عزت آن را انجام دادیم.
​
🔴
گویا حداقل ۲۰دقیقه از این مصاحبه پخش نشده که نکات مهمی را در خود داشته است.
​
🔴
برخی قطع صحبت رییس مجلس را با بازگشت روزی‌طلب به معاونت سیاسی مرتبط می‌دانند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67119" target="_blank">📅 01:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67118">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce4a0d523c.mp4?token=kaF6wnR8yfCVuhRkz6N2b07WTpcm9rPccsXcHN-yH03zHyVa-_E7_LGTPZGWQRfG-pHSSaU74LfraPD5OEz_At82d5Yc3q9lgx30B8KZirAI8_V5aMgZrUp1YjKHX_QACY6sZaHQm3Si6ZVuGpU2yKEa2qGnFW_3RFhzvlTDguArjeA4Oga8YPbWH31fspAPSkaUFvhNQFUJy9Z5ztTsHDbwHR5e_exC6hZh6JYlx1INrvL1MMkq0EuiDLwwcrc45WA4TS5AZT1oLgl7Wy1Tv1cxeJPSTRTinDPnsDjPCVBVQ1loJncxHH4K3EqXUPOMuQpfsBzao4184tstWHuSrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce4a0d523c.mp4?token=kaF6wnR8yfCVuhRkz6N2b07WTpcm9rPccsXcHN-yH03zHyVa-_E7_LGTPZGWQRfG-pHSSaU74LfraPD5OEz_At82d5Yc3q9lgx30B8KZirAI8_V5aMgZrUp1YjKHX_QACY6sZaHQm3Si6ZVuGpU2yKEa2qGnFW_3RFhzvlTDguArjeA4Oga8YPbWH31fspAPSkaUFvhNQFUJy9Z5ztTsHDbwHR5e_exC6hZh6JYlx1INrvL1MMkq0EuiDLwwcrc45WA4TS5AZT1oLgl7Wy1Tv1cxeJPSTRTinDPnsDjPCVBVQ1loJncxHH4K3EqXUPOMuQpfsBzao4184tstWHuSrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
قالیباف وقتی گفت توافق خرید غلات و گندم در ازای پول های بلوکه شده برای دولت سیزدهم بوده است، مصاحبه اش در صداوسیما قطع شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67118" target="_blank">📅 01:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67117">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/640225b559.mp4?token=U-d63GFHQ9vKwszk4adYNIqJXOYLMlWueBzAYlLLXG1TjuLDR_TT7Gs-yrmEkJNWkTe092v0tlR3hrfsTR5ecfveEd0rrpeSYv35ZkPT8CbEqLnWn-Er4h9-ubKBC1OJzxIUMKoXp7gKHoZc-PRrGNXwZIlJQ4xhWDx0hcACW0fzASPstLPGMZ9rY1GfFc2zD7JZ1Zs8dQ9L4UYhmFDtVsl6C-AmyBjEyEp7bIcLR1Dxpxm6YsIEgkRUrCJHIuFLXdZFWlfrCLhen1_wvv337nBEkJdHiE75vxz0M0Xb2qZIHGwnyzGmrmb8ctiMTCOExabreaJfuzW0jU5w3TjPDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/640225b559.mp4?token=U-d63GFHQ9vKwszk4adYNIqJXOYLMlWueBzAYlLLXG1TjuLDR_TT7Gs-yrmEkJNWkTe092v0tlR3hrfsTR5ecfveEd0rrpeSYv35ZkPT8CbEqLnWn-Er4h9-ubKBC1OJzxIUMKoXp7gKHoZc-PRrGNXwZIlJQ4xhWDx0hcACW0fzASPstLPGMZ9rY1GfFc2zD7JZ1Zs8dQ9L4UYhmFDtVsl6C-AmyBjEyEp7bIcLR1Dxpxm6YsIEgkRUrCJHIuFLXdZFWlfrCLhen1_wvv337nBEkJdHiE75vxz0M0Xb2qZIHGwnyzGmrmb8ctiMTCOExabreaJfuzW0jU5w3TjPDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
لحظه قطع شدن گفتگوی محمد باقر قالیباف، توسط صدا و سیما
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67117" target="_blank">📅 00:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67116">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e29288f186.mp4?token=MQ9ee8y1FUVGCb1i6JDj0doqUeUtGj0eBZoNCCbCbLXAidPkjbfI7xWQ95Rh9NNlcBeRIV4aInbAC4B54GaXOzONRIEqiraJpo53gRWHwiakKbZ1tP4m-RcABCL8z6x6ZamMM9ojgNYu3wZWaH_AokakLRy22Vo_tC69sgbpkWXFgsYcMj0iPiDjNbC1o4wclH4xcD1XMMO2uXQfNZ9wW3KU_GZpAs4AKhK0y0cP1CfFh737OlCLXxmwCmIIuC9-DIg6eZfjABq26V1Ln7xlt43T1lw1vTf3-dl1SLuGIfvxZP2E7Hv1828LX6l3VqZpLdLDLc1DzvkpHGy0Br0TnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e29288f186.mp4?token=MQ9ee8y1FUVGCb1i6JDj0doqUeUtGj0eBZoNCCbCbLXAidPkjbfI7xWQ95Rh9NNlcBeRIV4aInbAC4B54GaXOzONRIEqiraJpo53gRWHwiakKbZ1tP4m-RcABCL8z6x6ZamMM9ojgNYu3wZWaH_AokakLRy22Vo_tC69sgbpkWXFgsYcMj0iPiDjNbC1o4wclH4xcD1XMMO2uXQfNZ9wW3KU_GZpAs4AKhK0y0cP1CfFh737OlCLXxmwCmIIuC9-DIg6eZfjABq26V1Ln7xlt43T1lw1vTf3-dl1SLuGIfvxZP2E7Hv1828LX6l3VqZpLdLDLc1DzvkpHGy0Br0TnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
این خانم، عالیه نصیف از چهره های وابسته به رژیم جمهوری اسلامی، شش دوره بدون وقفه نماینده پارلمان عراق است، او در رقابت‌های پارلمانی چند ماه پیش گفت: «کاری می‌کنیم فاسدان از پنجره فرار کنند». حالا خودش به دلیل فساد کلان دستگیر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67116" target="_blank">📅 00:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67115">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e563023c29.mp4?token=joKyiXg0JVVmfj89oZxu9i6OcOeUstRNBXkjErwrJ6z85frAhbAXUENhG6SLxfWjr6Kcn2IhzeSmxCsz98MhkxtEthxCBRUjnRuipJvYU4Nb6wNEtY6RUKwdnJ8CHtyMrdpoBqIlpaXDyMERFR9cBOGXUsb7x1JNAcTPjXdLvftefiBQm77LexXMXQqvCltvRAa3KNeERdl29rjOKztN9HycYfMt2RuXeTaJtdJeImOV9rg-8iOKfbgR4fl7JGtqomZquF99VY3v2TjgkZrkZQrGEulyq8YBItgYPYZ2UuPF30A2xmm2ITeVgbrJvyUODJZ6TNaUoTryk43NMrqnZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e563023c29.mp4?token=joKyiXg0JVVmfj89oZxu9i6OcOeUstRNBXkjErwrJ6z85frAhbAXUENhG6SLxfWjr6Kcn2IhzeSmxCsz98MhkxtEthxCBRUjnRuipJvYU4Nb6wNEtY6RUKwdnJ8CHtyMrdpoBqIlpaXDyMERFR9cBOGXUsb7x1JNAcTPjXdLvftefiBQm77LexXMXQqvCltvRAa3KNeERdl29rjOKztN9HycYfMt2RuXeTaJtdJeImOV9rg-8iOKfbgR4fl7JGtqomZquF99VY3v2TjgkZrkZQrGEulyq8YBItgYPYZ2UuPF30A2xmm2ITeVgbrJvyUODJZ6TNaUoTryk43NMrqnZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سعید آجرلو از اعضای تیم رسانه‌ای مذاکره‌کننده جمهوری اسلامی در اظهاراتی در پخش زنده شبکه خبر رویکرد علی خامنه‌ای رهبر کشته شده جمهوری اسلامی درباره مذاکرات را اشتباه خواند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67115" target="_blank">📅 23:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67114">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iC4jCgbrQOKx7uL9fclG8qpl_LEGMa48ZtVO3olX6Hjo5nrQGkLpTgJgg663pO3NFKSWZJ7YwVdanNgoYvnCQJMbqW1DH9vK-cv5EJMG3KOh9HoBamNl8Z2VsdMN3661ohgaC8Wz08rc9L1n11pyTQFELmHM6m0hpInnSHEj_UhDWrlBTMFT7NDOWmV5emeLmS060Ci7fUVuE7bgi31NiCHsp123fy5NuseX_y8RaAVhqtmShpBthZWYHGrCPXoee_1ILAtCB2T86fKlB0w-UJvQfKKS7BVn9KuPejXDHsZfVvOPwppsGidb2S7BwF2ta_nDEJJL-1Jkk7yl3xWBPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌿
جدیدترین روش ترک اعتیاد  گیاهی
بدون درد، بدون خماری، با انگیزه‌ای نو برای زندگی
🌟
✅
ترک فقط در ۵ روز
✅
درمان کاملاً طبیعی
✅
بدون داروهای شیمیایی
✅
بدون بازگشت
✅
همراه با پشتیبانی روانی و انگیزشی
💚
بازگشت به آرامش، بازگشت به خود واقعی‌ات
💪
تو می‌تونی! ما کنارت هستیم تا دوباره بدرخشی…
♦️
جهت مشاوررایگان فرم زیررا پر کنید
👇🏻
https://app.epoll.ir/74570725
عدد 6 را به شماره زیر ارسال کنید
👇🏻
🆔
@Sahar77631
☎️
09923413672</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67114" target="_blank">📅 23:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67113">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/706602e352.mp4?token=kJmG2bVxV7ql1lFGwsbJcGleg5mzPwNcJ31GTsv-oYGjwX7fxZUkfHAIDpVuhVloAedhgSx4qfaSGpIgly2TmM221LsIADL8T_2lExCm6rHaH588Qn2L5Rgf4JTz8WC-GO1DCYtUih1-iAT9ylwKnp3ScLid2Y_7XDdONsB3XXWDr7C6yFZXsaCBI6Hx0BiJmpgtRFEOAjQk2_gmtf17377j28wBwnBGRgmd_9Mt_ceTaBdMcSInYEGxfWxnKmQwrVFzOd4gO70qiCMHbCDXKgv4h2N4yMPE0JHhnathvBdGz7dH4frzSxquu1y4evIi-LI4x9_O4FC96iWN9CNSYzX9LeBV-rR-hUi0Q2-XJf5kTE6vi6OLpioyB7T19YutZMsuCBHzUk9yqXy8X_o1gXgUoEEKJ6AXHoKaeDx8vTjrNfeoRvxi42v9bETKh6ebyNy0s3JSF73FAExUlVrTnaxupTdWkrlO7z3Vay354bv9CrYd3caZB-8_3qZY1ZvdgIrKWnjvvvDGizbU_THb2baa0mlDVXpRc5cPXrm8PNslFmuZUOVK2dkSYMeXFBTFJZTe0IidLVmSEvAwRYeOpB8E5OXr8W8ejOr7nQNZ_GvtQIhDQU_uzuYf2Tue_1ob6NakZ7gCXT711aqK995mk8KtFkQNX5JyyjGGwtGhidA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/706602e352.mp4?token=kJmG2bVxV7ql1lFGwsbJcGleg5mzPwNcJ31GTsv-oYGjwX7fxZUkfHAIDpVuhVloAedhgSx4qfaSGpIgly2TmM221LsIADL8T_2lExCm6rHaH588Qn2L5Rgf4JTz8WC-GO1DCYtUih1-iAT9ylwKnp3ScLid2Y_7XDdONsB3XXWDr7C6yFZXsaCBI6Hx0BiJmpgtRFEOAjQk2_gmtf17377j28wBwnBGRgmd_9Mt_ceTaBdMcSInYEGxfWxnKmQwrVFzOd4gO70qiCMHbCDXKgv4h2N4yMPE0JHhnathvBdGz7dH4frzSxquu1y4evIi-LI4x9_O4FC96iWN9CNSYzX9LeBV-rR-hUi0Q2-XJf5kTE6vi6OLpioyB7T19YutZMsuCBHzUk9yqXy8X_o1gXgUoEEKJ6AXHoKaeDx8vTjrNfeoRvxi42v9bETKh6ebyNy0s3JSF73FAExUlVrTnaxupTdWkrlO7z3Vay354bv9CrYd3caZB-8_3qZY1ZvdgIrKWnjvvvDGizbU_THb2baa0mlDVXpRc5cPXrm8PNslFmuZUOVK2dkSYMeXFBTFJZTe0IidLVmSEvAwRYeOpB8E5OXr8W8ejOr7nQNZ_GvtQIhDQU_uzuYf2Tue_1ob6NakZ7gCXT711aqK995mk8KtFkQNX5JyyjGGwtGhidA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
دو موشک فلامینگو اوکراینی به یک کارخانه تسلیحاتی روسیه در ولگوگراد اصابت کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67113" target="_blank">📅 23:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67112">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a5fee32db.mp4?token=tS1p8i8wAbqr6aHGV3p-rTlNOy4tuDX0PHuJgd79Hwnr4-r_G20IoB27x5dXLCvlKacDUaY2gsyH7GgnivT8Cear1nm9FRhVg2qyJNjPN-MvOCWREZfI7OBTo0hUenGjVi77HCJ-Z-RKc7ufkZAhNtbYQI8LbW8gPBNEdPDUVlvBBNGD3p_iiL9G1yxzKldwbOuPtabLRSph67u13l5g7F7vlk1_wE1sF2kOBHvrm0t4StyNiYyUV9fx_G4JNt9UIDa7abz6MFgAcrKxSnkpqDFnEss_7-Vq_RWZt0bvPJB7VxNZWOxAciDPcNHApOhifgqLJLqJmH6IZELALHubWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a5fee32db.mp4?token=tS1p8i8wAbqr6aHGV3p-rTlNOy4tuDX0PHuJgd79Hwnr4-r_G20IoB27x5dXLCvlKacDUaY2gsyH7GgnivT8Cear1nm9FRhVg2qyJNjPN-MvOCWREZfI7OBTo0hUenGjVi77HCJ-Z-RKc7ufkZAhNtbYQI8LbW8gPBNEdPDUVlvBBNGD3p_iiL9G1yxzKldwbOuPtabLRSph67u13l5g7F7vlk1_wE1sF2kOBHvrm0t4StyNiYyUV9fx_G4JNt9UIDa7abz6MFgAcrKxSnkpqDFnEss_7-Vq_RWZt0bvPJB7VxNZWOxAciDPcNHApOhifgqLJLqJmH6IZELALHubWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بازدید بنیامین نتانیاهو از منطقه امنیتی در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67112" target="_blank">📅 23:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67111">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eaf19117f.mp4?token=ITAomx_TmKDvrh5A5aLSBC846miqVdlEzXdx6naMDYSWeJtn1drONpHiOx39pnVyij5YrE8zwk2x0CJQU96yMbdGXjzGbyPN-YMnFTdRDxzpe7oQk451PmHRYgtk0eS6f5UXcn0IZJbDbqqyamy7y0oGnv3OLmVPH8PA1GmO3yWH-p-UD_A-5MfR-9QYESMFkulhAFJtO1hujn8Js5WrPtLv4uPeGjuGjcuEKozYM-qUQHrWfO2z_OSYr99bmOslqzDfQU2I1ofouSsF91yttg0aX0McR3BBlY0F4PlZ1EMi1XapRkklebdEcu-oGoWJ6kWJ__M8p5qnYkPh4oEwomdMKJOTCGMBN1Hm4XbzVRU7s99PFbmdIcIt4DoI3lOYwEpez7L8g3G0xjWtKlfCkWTQnLbzmyRMgiRUOlEsScfT5mLRobouTXyiGWASpH8zhSrUiPJroWJLQuyGPACoUhUxBzPHmqbBadbe6EjhJh0wB0c8nvA544Q96A7Gs7_bv8Ff_Twn82Gp4UK1a8qzMhxFSotUNsGvEyxoEQ31c83xG2I5-5iMsKdyUIHQivaYCRuUVy5sKUzkDiRdyHUyyFMgYApytVLpj8I4eeos2CpLPwkbop9EWlvqKsw0pfikzy-UGbk8YV1EmCikbosS75a3BG45TnqVW0pylrU8VQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eaf19117f.mp4?token=ITAomx_TmKDvrh5A5aLSBC846miqVdlEzXdx6naMDYSWeJtn1drONpHiOx39pnVyij5YrE8zwk2x0CJQU96yMbdGXjzGbyPN-YMnFTdRDxzpe7oQk451PmHRYgtk0eS6f5UXcn0IZJbDbqqyamy7y0oGnv3OLmVPH8PA1GmO3yWH-p-UD_A-5MfR-9QYESMFkulhAFJtO1hujn8Js5WrPtLv4uPeGjuGjcuEKozYM-qUQHrWfO2z_OSYr99bmOslqzDfQU2I1ofouSsF91yttg0aX0McR3BBlY0F4PlZ1EMi1XapRkklebdEcu-oGoWJ6kWJ__M8p5qnYkPh4oEwomdMKJOTCGMBN1Hm4XbzVRU7s99PFbmdIcIt4DoI3lOYwEpez7L8g3G0xjWtKlfCkWTQnLbzmyRMgiRUOlEsScfT5mLRobouTXyiGWASpH8zhSrUiPJroWJLQuyGPACoUhUxBzPHmqbBadbe6EjhJh0wB0c8nvA544Q96A7Gs7_bv8Ff_Twn82Gp4UK1a8qzMhxFSotUNsGvEyxoEQ31c83xG2I5-5iMsKdyUIHQivaYCRuUVy5sKUzkDiRdyHUyyFMgYApytVLpj8I4eeos2CpLPwkbop9EWlvqKsw0pfikzy-UGbk8YV1EmCikbosS75a3BG45TnqVW0pylrU8VQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف: اگر می‌توان گره ای را با دست باز کرد چرا با دندان باز کنیم؟
🔴
کسی می تواند خوب مذاکره کند که برای جنگ آماده باشد.
🔴
مذاکره با آمریکا مذاکره با یک دشمن بد عهد است که هر لحظه فرصت پیدا کند علیه ما اقدام خواهد کرد.
🔴
ما در شرایطی با جنگ و آتش اقدامات تلافی جویانه ای را علیه رژیم انجام داده ایم.
🔴
خوب است ببینیم شیخ نعیم قاسم  و مردم لبنان درباره این تفاهم چه می گویند و برخی دوستان ما در داخل چه می گویند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67111" target="_blank">📅 22:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67110">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c10065584.mp4?token=nXpB1lDCuBuKKJcFN4GQLH0tVy8KGZtIO9jeaByKGs7OVdjz8dGG2Jo5cP9fv8xFfXnVKLPnUXc8YYegcWQcVuegG93izcF_9e4d6JrKUE5GlKW5dPeZA3Q6S4Ps46JkfQnaqNC-rup6UoologM_DlI_Mhb22K_USIsJpZa_6mhbrrvvafRALRJbBw_LjHHYsvl9YgUa32gJTvI6SeErtfLS2g98z_cy-3u4Ga-KDAg1jljmm-XpaPjDDnlRA0A2JgWWN8-9AU1FjhwjusCVssNF_0J2ksR0f3c1dE5KPo3bZVCdTwXBAIxmzObEn8J5kDD4BcQcJFGHxBQPqMuhgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c10065584.mp4?token=nXpB1lDCuBuKKJcFN4GQLH0tVy8KGZtIO9jeaByKGs7OVdjz8dGG2Jo5cP9fv8xFfXnVKLPnUXc8YYegcWQcVuegG93izcF_9e4d6JrKUE5GlKW5dPeZA3Q6S4Ps46JkfQnaqNC-rup6UoologM_DlI_Mhb22K_USIsJpZa_6mhbrrvvafRALRJbBw_LjHHYsvl9YgUa32gJTvI6SeErtfLS2g98z_cy-3u4Ga-KDAg1jljmm-XpaPjDDnlRA0A2JgWWN8-9AU1FjhwjusCVssNF_0J2ksR0f3c1dE5KPo3bZVCdTwXBAIxmzObEn8J5kDD4BcQcJFGHxBQPqMuhgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
🔴
تعهد ما نسبت به باز کردن تنگه هرمز و ادامه مذاکرات منوط به پایان جنگ در لبنان است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67110" target="_blank">📅 22:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67109">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
قالیباف:
غنی‌سازی حق ماست و خط قرمز ما در این زمینه مشخصه.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67109" target="_blank">📅 22:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67108">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/205ddcc2be.mp4?token=qrkNNMoWleB1cgZzr0iA8sqm3sfAfGjCOVgEoZwEALoJaaf2zufJuy7BkvUcoot5-qpXuCw3mwe21CjFMrVXo1hD6GLnJT5boIBAC8Ir44KEmxs5m4ppal2y_W_VWJSvfqFCzmcEmxHtxqP5301T4frznjgzk5XB2oTxyM6WS0ijcnCqkNpjpXZBaKW5iWTLsGcFfXWBsyu0HVquYsklp0S8Ob_QqOT5gQSQfqAXHDIfWJUKaPXG8tXYhFYUH3gLA-MSPKQ9KKXLeTUpAP86C6ax89dGmR6dvVq_r4oc2c9VkIocpiyTXLRxl_8yag_hLoPWdph-6F8l-uEWwpb0fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/205ddcc2be.mp4?token=qrkNNMoWleB1cgZzr0iA8sqm3sfAfGjCOVgEoZwEALoJaaf2zufJuy7BkvUcoot5-qpXuCw3mwe21CjFMrVXo1hD6GLnJT5boIBAC8Ir44KEmxs5m4ppal2y_W_VWJSvfqFCzmcEmxHtxqP5301T4frznjgzk5XB2oTxyM6WS0ijcnCqkNpjpXZBaKW5iWTLsGcFfXWBsyu0HVquYsklp0S8Ob_QqOT5gQSQfqAXHDIfWJUKaPXG8tXYhFYUH3gLA-MSPKQ9KKXLeTUpAP86C6ax89dGmR6dvVq_r4oc2c9VkIocpiyTXLRxl_8yag_hLoPWdph-6F8l-uEWwpb0fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
🔴
اگر نخواهند در گفت‌وگو به تعهدات خود عمل کنند، آماده جنگ هستیم.
🔴
اتفاقات شب‌های اخیر خلیج‌فارس را نقض آتش بس می‌دانیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67108" target="_blank">📅 22:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67107">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/745f2de194.mp4?token=phjLKCbFiXf4ghnVLQ7h60vdCD2qDfeBIXihHmMDiyisnW8TbeidwcQfMlYQzQkcoGL6ObHSf8s--V9qsIgXg9JBpCY98sYGSP0oUCKK_ozedWOk7UmwarUX8cpu3EZdrRKIM4_dwqErj2P10zm_g_zackNc3i1EOUZMrhkdlPwL-AFNCg55f_igAEyBOXq8DkkBVHfJYcE_zZYTYvd1CKp0_4O23w6GkXKBtSw593ipsB_pFYxenHRxncBK1gkZ6wZoL6HC8sDcRYAIS3mtppDLvFCPqJMbsqrNWkYOWKtHrniGMMhgfYrSHIJRgGdeVZK_JAIrmX9XeM1vGvugKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/745f2de194.mp4?token=phjLKCbFiXf4ghnVLQ7h60vdCD2qDfeBIXihHmMDiyisnW8TbeidwcQfMlYQzQkcoGL6ObHSf8s--V9qsIgXg9JBpCY98sYGSP0oUCKK_ozedWOk7UmwarUX8cpu3EZdrRKIM4_dwqErj2P10zm_g_zackNc3i1EOUZMrhkdlPwL-AFNCg55f_igAEyBOXq8DkkBVHfJYcE_zZYTYvd1CKp0_4O23w6GkXKBtSw593ipsB_pFYxenHRxncBK1gkZ6wZoL6HC8sDcRYAIS3mtppDLvFCPqJMbsqrNWkYOWKtHrniGMMhgfYrSHIJRgGdeVZK_JAIrmX9XeM1vGvugKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
🔴
دو اقدامی که پس از امضای تفاهم‌نامه، در شامگاه ۲۴ خرداد رخ داد، اعلام پایان جنگ از سوی نخست‌وزیر پاکستان و توییت ترامپ درباره برداشته شدن محاصره دریایی بود که از اتفاقات مهم تفاهم‌نامه به شمار می‌رود.
ما در حال دنبال کردن دوران گفت‌وگو برای تحقق ماده ۱۳ تفاهم‌نامه هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67107" target="_blank">📅 22:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67105">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q9-Zzbb9thtS-H7rUdw1S0_x0-WRQvtymMlBQiuk5L3qxDgraMRt-2pGQfuXk50OL_nS_ImwdJPf9-7PCYT0o66kpBSGmsa7vG8Do3Wc2Bn1YDC0xJ1Pr096IDXVegcvrIPJnQzwWQxApdO1ViKrQv_OXKlTYgos9x5AKtprGGboIpdR8nqt9WICZgREjqlqQQl-jiSmStEqmjoEIC81LMXFThCRDehbXMnmA9IBccByu-z4uycnW43QPZsD4Uvr26XeOcxQUUOH_N7PIF8WVkZFKhfyRGqA2mM8ScJELbDJIXgPXVl7h6ERnmPIYhqcquFjzZ-j9wB2H4tCGV7LMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t0gn7nlMmQjaYCWPSOtBgl0vVNlnooKHNfdT_8EXo_yXGJSXsraP8Hn0H20m3rGYoXaJW20sn9rg_fgRZKtoCcJZI6p3R3YmhVPk6oOpiB6wkE7eMyW4L5cjwxE8Zo0cvhkUO4xyfdaO28QdkjLKDVY7-PbTa9iVXlQTdRFbJBqV_pKdk1Zfb56WEAJb2KJSUdUEjEVqEsAQV4plDi09eW6tdRGq67UFnV3kOLvAXmd95Se-KZq4sI-s4uj_gN2xGLJ86oBPeBF5_jPx3OGcNL_AYzk3-apr5Ft4_juJ5MH2Uekf0s4bprdwHWmPuX7rDP-9qkN6HTr63iKb-T94OA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
صفحه اسرائیل به فارسی:
چرا هر کجا این تصاویر به دیوار است، دزدی و فساد هم هست؟
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67105" target="_blank">📅 22:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67104">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YxW4f0XxMdYcBe1fbiHQe-bzstAzAUwcyUOXOH9_1gRVOgHra1vZzOgIWIh0uYwT7Ne5gLDr4kOSdTtXMDfC8PJ8EVjI96s6-LA9PE5kEXwSqrWmScLSH6qM5zyl8p98IBkEbeQWagdC4kkrU-jE9Hin3UXHQMpcyhkZiyNh7o7hAPw68fVTauRNqq9yPurl43wBf_y60odU8NRpVxU7tPMI0d7f1IasfqIWsmH1UDpdT2U8T_jEmtFRxu_5ctYcmQTsIn9weigISAFn8HHjKzA5KH7pUPQk_ZKSf1PdGueGxWHYUQqtO-l0sdaWb_vl9dUCPGZ2GtjNFnnkb1dztw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وال استریت ژورنال:
اختلاف نظر میان میانه‌روها و تندروهای ایران بر سر اهدافشان در مذاکرات با آمریکا، پیشرفت آنها را کند کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67104" target="_blank">📅 21:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67101">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yp1DLm-zQI0FejIGHDfvchCMOOh7SDhTUuk37rKJme79bVNGlAnPiay9QyPMB4gBKgC4S4kA-r9_JrPzKVmJ9dYgO455wBepCOb_aBFhyfvNGDfg7uZgL0AB48GctgJIrSekvVJCZwMX7pR_Z6YwFypa0G_M0fHISxhiKW8zQMTOht1z2F5e1FWCC_ygSoNh_HrnjO5Q7AIH-Tz_oOrltloU_h3tttsH9xzw9CTWkMCwzNwhPweni03RM-1Qc7EygMzh1hBNrgSbjKmonHjLT8_JSEvC3C-G9_wJl_p7weql9ITGBSuthitvxQ1LNClw1CSwSopkCGsZ8NHLxBkoug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l62GsW9J591gPcfOEExUfj4sc1wRfh4rYPkOWUqt3iC4fN5ldmklRHamArIWO5TpZEoBEb7HG9ECiruuq9g0aNFtVzbxAJr1yzz1ayXNkTjYBR6t2mVCIjllS9Bl9FBI1znDkZcIcaE5RKIU8AOpF47ZBEbFAP0ndIL1wjhRstmrmddUpOZeH01Jspk6bPET6_OcQ8TyTzFbqNojwoqyq7WHyt3BnG-sMGICY5LMdwqLC8p0agpOwMNdofdiD85pIECwKp-GCRaAcTwCdGTbU_9Z9gzDGeiis-7RWplJDtZBGjMlacfoglFTO5TjlL5gcECgzFGdHqwSd7D01rQHrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FJVEPOhd-kqkLh2mQYLre2-dU3QZiMhIyOceBFwXLXB0cAdJ_ahM1PEnxfoaaxySR4EUFX-9h6H6eWcC7RDh_L2jv75I2dHD5Kzp0xDd-L3TJLyXQNKugRLmfSff7B-8w-rK5dJDZB38-X6z30TqSdf6K-Pjn3HxR3uNe2a9nONch_10-GCdcaQawpbHh5jSTlpODXrgi7Kvrmn2yoTq9ZNE7WPrzfhlMw1MeVxOKgvDD8jPxS93GXs3LCA55cqwK0NPyHRVIXNy4gJvqRwn_SY1roo4ebScZZXcLoCE3BT-EgLAXkoEHj0GuqG87eumVWMxpUC_Wrd872_xzsC8tg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
سنتکام تصاویری از آموزش شبانه تفنگداران دریایی ایالات متحده در جایی در خاورمیانه منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67101" target="_blank">📅 21:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67100">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d3efb7db7.mp4?token=DRxLTcPHN_DfvdurtET-rnlt2eQGA4eptSoJLAa5xeTQhpnsq7acWkKGBmtLiOkv5700K21hUBs3KhTDhx4IIyLkfaModwXCRVEMygBOi1t1TSvYpr2E6tQqQRNhdtU4GnQktjTlsr8gKNv3GTRYdVA2wLK48HgSaahC-WdqNJolrJ_yzk4VZGzUFGAFEjj5SsOBm3bw2pCX58C4V082jOpA_rWk2OinzIcTHN9SqPskkTu3pUqs_38SS33QaGUFiuGnGEOX17pJoCDRGOgAf-MLvaiUH0j9THlif8wTZlVOzdO6g5Z8icdMROc4VZto4I8suDgkkA3SCM7pGrU4rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d3efb7db7.mp4?token=DRxLTcPHN_DfvdurtET-rnlt2eQGA4eptSoJLAa5xeTQhpnsq7acWkKGBmtLiOkv5700K21hUBs3KhTDhx4IIyLkfaModwXCRVEMygBOi1t1TSvYpr2E6tQqQRNhdtU4GnQktjTlsr8gKNv3GTRYdVA2wLK48HgSaahC-WdqNJolrJ_yzk4VZGzUFGAFEjj5SsOBm3bw2pCX58C4V082jOpA_rWk2OinzIcTHN9SqPskkTu3pUqs_38SS33QaGUFiuGnGEOX17pJoCDRGOgAf-MLvaiUH0j9THlif8wTZlVOzdO6g5Z8icdMROc4VZto4I8suDgkkA3SCM7pGrU4rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصاحبه با مدیر داخلی بهشت
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67100" target="_blank">📅 20:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67099">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c1232f504.mp4?token=HQfCcwvZEhqjY6KraupaIm51Ug-yr_XRLOCoSQiDi2qUfy3mRt8fx1TwyiKGOdMKKyYtF33jkK9IdIs8ocwG05qAOIj6CGoh6GGY-kxWvXkVYSzbSYGUIx2_Q-ngSb8IY2VousgbCZZ7AjDRaxRYgyX4p9F1irwVflYzTrgbdIN7XPeZtpqL_iA_dzNe2R9MxNL9GUIly_QlsK04ggfhkX_mmKOxmRI2aV-hOtynShFR63IT0qE7RjeenA5_XI5AO_EoX0capVH73fHTU_pbleNAhFIyuamwyku9wLIKYfE_8SXTe0mu9dS1H7SaBgdmk_OPPLSGgFAOz7wsRnPcuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c1232f504.mp4?token=HQfCcwvZEhqjY6KraupaIm51Ug-yr_XRLOCoSQiDi2qUfy3mRt8fx1TwyiKGOdMKKyYtF33jkK9IdIs8ocwG05qAOIj6CGoh6GGY-kxWvXkVYSzbSYGUIx2_Q-ngSb8IY2VousgbCZZ7AjDRaxRYgyX4p9F1irwVflYzTrgbdIN7XPeZtpqL_iA_dzNe2R9MxNL9GUIly_QlsK04ggfhkX_mmKOxmRI2aV-hOtynShFR63IT0qE7RjeenA5_XI5AO_EoX0capVH73fHTU_pbleNAhFIyuamwyku9wLIKYfE_8SXTe0mu9dS1H7SaBgdmk_OPPLSGgFAOz7wsRnPcuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏در فضای مجازی این ویدیو به عنوان لحظه‌ی ترور خالد خالدی نیروی جمهوری اسلامی در پاوه منتشر شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67099" target="_blank">📅 20:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67098">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vpxVj41nhjO8UyyA1Q73YKXXfpUVF4KjLlzTVyZDWRRhOx0HBop66oullcfQDBqtapPP0iZtJ9QwY-dNNFUgmlG9hiImcF9ab_EQ8Dy8qouIN3_CE7uyzWxbChiRF0dReHNHkcVZPc7yNuRP9BWQh3rRAdl0gdcz-m5aeZfDvlk3uL56IbcwhXP54op5m78pqINz-H5ggcMbwbmCM4MDheOo3jtIDHyTgu7AIFTQ1Pq9KnMZmPB_oo6zC2wMidJr_gNZAcaclwxqWp5sg-MXk_nqfJdODZHh5IMihWBTtdJ-WsvtcEtMZqlgGIukdIHDgPHHchDY_yttam7JsaovFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
علی حسین قاضی زاده تحلیلگر اینترنشنال:
‏ایران اینترنشنال نسخه‌ای از دستورالعمل محرمانه شورای عالی امنیت ملی را مشاهده کرده است که از مدیران رسانه‌ها می‌خواهد طی ۴۸ ساعت منتهی به آغاز مراسم تشییع جنازه علی خامنه‌ای اخبار مرتبط با مذاکرات و توافق را از اولویت پوشش خارج کنند و بر پوشش مراسم متمرکز شوند.
ساده اینکه از بازماندگان نظام می‌خواهد که چند روز تکه‌تکه‌ کردن یکدیگر برای تصاحب حکومت را رها کنند و به چال کردن رهبر ملعون‌شان مشغول شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67098" target="_blank">📅 19:48 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67097">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9Buel_rW3nK009s_fhTfDhBcf_KymrMdXDK0wtqPnSQsMvLqwZ3s7o11z9b0d1xaRQkVBSvEvG69UdLD82ZXA9UhEMyTAmss8l5mWiQ51i7hTq9Z5dOkgqf_oKjdaAq4VwMQ9lXymYM-v3T8UIjeuYIF1xrBiH7VE-v-JjLhpTnaTOAUPfTWP2Mr_r4_CFTCJ7f9bllKj4wuww7RDNF_31WP6Jd5lgbP5nKY3ehWNPoEaGFOn1l-p_GAV37-lHaScBnHR2G4VDGHPNFUIjWrnhIhMGKMKJz_4cs3qtrLlaExmXeVJ0MScfyCea9VfTBJhcQgwgaXV6ejBXhWTVRtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
ناو آبی خاکی «یو‌اس‌اس باکسر» آمریکا در حال نزدیک شدن به منطقه
🔴
بر اساس گزارش‌های منتشرشده، ناو آبی خاکی «یو‌اس‌اس باکسر» نیروی دریایی آمریکا در حال نزدیک شدن به منطقه خلیج فارس و آب‌های پیرامون رژیم جمهوری اسلامی است. تاکنون مقام‌های آمریکایی جزئیات بیشتری درباره ماموریت یا مقصد نهایی این شناور نظامی منتشر نکرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67097" target="_blank">📅 19:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67096">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aeafe2956.mp4?token=NjTaKeM55EDFzmFUVN8LzA7yzXc6VNK3uVGYFevtim-S_h6SXrRYEVOvoQDH2JWJYqXPFxujN1lZS_gSiB4KfgyG9X62-lxAMR-L62CmA-XEVO8VVkQXExLeeLyHen7Hm-QCkEkwmDFcejJQZOxo4Rd9m9dEh0M8YQ8DiEyChRZ8C9E3EaQtSnfEBZYjagfOD5Se5k_9gmRl6qh8_apWIECQgF8_qm3p8bBN8dEx555MTvJLn-lReDHX2YPHNuXF5eIrFnj5wfPVP9ZWNyd2EriXEXwzgOzkdwJ3jstKhVom7LXwxxGXsohqTWv5xnDTkBxxL7uCC4NSDdvlRIfkOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aeafe2956.mp4?token=NjTaKeM55EDFzmFUVN8LzA7yzXc6VNK3uVGYFevtim-S_h6SXrRYEVOvoQDH2JWJYqXPFxujN1lZS_gSiB4KfgyG9X62-lxAMR-L62CmA-XEVO8VVkQXExLeeLyHen7Hm-QCkEkwmDFcejJQZOxo4Rd9m9dEh0M8YQ8DiEyChRZ8C9E3EaQtSnfEBZYjagfOD5Se5k_9gmRl6qh8_apWIECQgF8_qm3p8bBN8dEx555MTvJLn-lReDHX2YPHNuXF5eIrFnj5wfPVP9ZWNyd2EriXEXwzgOzkdwJ3jstKhVom7LXwxxGXsohqTWv5xnDTkBxxL7uCC4NSDdvlRIfkOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇺🇸
مارکو روبیو:
تفاوت اصلی این تفاهم‌نامه با برجام اینه که برجام یک توافق واقعی با تعهدات و چارچوب مشخص بود،
اما این یکی عملاً چیزی جز یک کاغذ امضاشده نیست؛
متنی که فقط می‌گه طرفین قرار است درباره ادامه گفت‌وگوها، باز هم گفت‌وگو کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67096" target="_blank">📅 18:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67095">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8eb209b62d.mp4?token=XIoK1B5ZtMcPXxBMFSYYMDfSEUvYJm4S_FDoiHhmwAsciy0n6h2kwnRcj9msC1E4EGBdAyuGacsmsrcuY37uEYusZ4KGcWg8J4p2ksyEdLA5YA0YtiKN7utW3XwCSQNG6aCHqi6DALceLKV8kOZ_SOK9OsrIaP7QejsOX57xWWWtDJ8sTHh58V1tIAIftpcz4C5G63bNCMXwhFOceEj-HTat_UtRBiHXCP31RxTBlHhfVCIQQnxGjx4-HLR45Y9XlPVizp2n60HBfVVwsnL5ni42d56wbFxeYnbK21RulkQ8M1OCa9MKpTpMrFwRrco-kURBekd6_kg25aYMMjX3SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8eb209b62d.mp4?token=XIoK1B5ZtMcPXxBMFSYYMDfSEUvYJm4S_FDoiHhmwAsciy0n6h2kwnRcj9msC1E4EGBdAyuGacsmsrcuY37uEYusZ4KGcWg8J4p2ksyEdLA5YA0YtiKN7utW3XwCSQNG6aCHqi6DALceLKV8kOZ_SOK9OsrIaP7QejsOX57xWWWtDJ8sTHh58V1tIAIftpcz4C5G63bNCMXwhFOceEj-HTat_UtRBiHXCP31RxTBlHhfVCIQQnxGjx4-HLR45Y9XlPVizp2n60HBfVVwsnL5ni42d56wbFxeYnbK21RulkQ8M1OCa9MKpTpMrFwRrco-kURBekd6_kg25aYMMjX3SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حمله پهپادی روسیه در زاپوروژیه اوکراین، صبح امروز
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67095" target="_blank">📅 18:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67094">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d3e8bdc85.mp4?token=MuHsAvC28iEAronQZT6FsJPFMFQ58_MDwvmQ0wTIYnEsTL1E4rR_rEZOrKquQciu_ZpYILb0Eyo_UefMbKXdq9WUasRF_q60Cu3M4brFwoj2Al9DYrRDOCN3vKm7XkY7LJvlY8rRrxwAcNPR0--44nAYjzci-nv4_rCGXrEjryaZ3Or8onJ08Ap81K2m41VIIm-lj0MB2JtqOILErjScLpxywtTilJuaHypWTpV03LMzhVzJSOcMw9Lg9_s1HFW7VBAxH3XsERM3EvrRMel7qKqhvFe5rctlTuxM1oDw53a4ZFVBlLl2aRdzJw2Gd0Zto1P66Bs5Amt1em9bxigHYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d3e8bdc85.mp4?token=MuHsAvC28iEAronQZT6FsJPFMFQ58_MDwvmQ0wTIYnEsTL1E4rR_rEZOrKquQciu_ZpYILb0Eyo_UefMbKXdq9WUasRF_q60Cu3M4brFwoj2Al9DYrRDOCN3vKm7XkY7LJvlY8rRrxwAcNPR0--44nAYjzci-nv4_rCGXrEjryaZ3Or8onJ08Ap81K2m41VIIm-lj0MB2JtqOILErjScLpxywtTilJuaHypWTpV03LMzhVzJSOcMw9Lg9_s1HFW7VBAxH3XsERM3EvrRMel7qKqhvFe5rctlTuxM1oDw53a4ZFVBlLl2aRdzJw2Gd0Zto1P66Bs5Amt1em9bxigHYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
پلیسا شوهر طرفو دستگیر میکنن زنه یهو میرسه به پلیسا میگه وایستید لطفا میخوام باهاش حرف بزنم یهو بعدش...
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67094" target="_blank">📅 17:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67093">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">⏸
🇺🇸
نوه‌ترامپ رفته کاخ‌سفید گردی و با این ویدیو مکان‌های مختلف استقرار بابا بزرگش رو نشون مردم داده
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67093" target="_blank">📅 17:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67092">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c791837da.mp4?token=SrPPbUpR_jEvHgMzwLgBsxwaIK-uQNo0pabrCq9zKZ3TTfyTIu7TS4nNUyQwfYtKVaVC6K559PYLoaCqWZKYVsd_yj-A5sOAfWlGNEXhCXfbW-j43oU1ciYyO1TN-xHCgmLq0eS_p_O969glC_OZQof0t9LxO83HQtXuT4YsAwULHNG07DC-VoAzre1Q8BwZHdIX_Z6QAUU55T69vvCaz84lY_xoEN53-mo-yUnwoQu9UWpjg_k6xxsl2hHfbS-GjFMafUBEEs63r1AbgLdLk3ZQH5XcUR-2Dkq-pj4nj1hS7LU0wpaqiJfwaDFlSHxOK4u7YO0Oh7ut26A82vW95kr1Vwnlqep18JWbbQm_JEn0HTfWeCGKyrXQ04-lM-1Oa5KIYwOZxtgci9EikeGczQj_q4XsV4xqKJdB3Dp9aa3-TkwYXG25hYqGukI-8Geb9yzBfWHydkC2eeGVyNZMs_wOUjuKrv7D-OBbtFOB1c3kVrM0E9t1Y2faaBl0-cgC6mwm8HRT7c0p9Z6L_ZX6vvwNpDFIQYdU_Jb082y1qRM6T6pUm-vtw6NOVihIfE6PKC-4Wl6fmhkHLJwYys2oeRiXBwX1tZerSHPFgxHd12WDQkYtdLbZq_6rRt6hWzT1WwhGGNqfAYFrIm7GsR71nlvO8QOD1_8L6kL9NSFLSu8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c791837da.mp4?token=SrPPbUpR_jEvHgMzwLgBsxwaIK-uQNo0pabrCq9zKZ3TTfyTIu7TS4nNUyQwfYtKVaVC6K559PYLoaCqWZKYVsd_yj-A5sOAfWlGNEXhCXfbW-j43oU1ciYyO1TN-xHCgmLq0eS_p_O969glC_OZQof0t9LxO83HQtXuT4YsAwULHNG07DC-VoAzre1Q8BwZHdIX_Z6QAUU55T69vvCaz84lY_xoEN53-mo-yUnwoQu9UWpjg_k6xxsl2hHfbS-GjFMafUBEEs63r1AbgLdLk3ZQH5XcUR-2Dkq-pj4nj1hS7LU0wpaqiJfwaDFlSHxOK4u7YO0Oh7ut26A82vW95kr1Vwnlqep18JWbbQm_JEn0HTfWeCGKyrXQ04-lM-1Oa5KIYwOZxtgci9EikeGczQj_q4XsV4xqKJdB3Dp9aa3-TkwYXG25hYqGukI-8Geb9yzBfWHydkC2eeGVyNZMs_wOUjuKrv7D-OBbtFOB1c3kVrM0E9t1Y2faaBl0-cgC6mwm8HRT7c0p9Z6L_ZX6vvwNpDFIQYdU_Jb082y1qRM6T6pUm-vtw6NOVihIfE6PKC-4Wl6fmhkHLJwYys2oeRiXBwX1tZerSHPFgxHd12WDQkYtdLbZq_6rRt6hWzT1WwhGGNqfAYFrIm7GsR71nlvO8QOD1_8L6kL9NSFLSu8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
قمه کشی ارازل اوباش میان مردم در شب عاشورا رودبند دزفول که با دخالت پلیس خاتمه یافت
😐
😂
تاریخ ویدیو 1405/3/4 امامزاده رودبند
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67092" target="_blank">📅 17:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67091">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d685f955fc.mp4?token=I7hX5OXDOktwoYktOOEQQB-lG-4jH8I-cyOM8shjpC9y1PFUk8v2l0ZemQfgRk7-TC4QbTGyToRtrjTKULA5KzZOPucmel0WZU7ygZ3VN3FjRQfOZzuiaOy6HrcaWZLgn06G4MlAUiYwxApwuAsk0v3oz8ZNSK-HTGXmjAzM5K1FpEb1tBgK5BL6GlMUn_e3yGxv_vA7zGyo7DVq_eTFzjNLCaxRDWCsBO2-uAJwerOorDox8GKd5UeyYdeko5Fj2OoVLzkWPc3WjyZf3_9aSjE1ZfR7K2cITe2PcEOpp4ojxNaonJ1oeBMAHatbFA3xVonXs38sUTrCkOITEy2sK0LK1B_snB9QVhhd8aNzG86USomFgrOrVJBp5GhmGWs6M21RPmpc6yZSSsIWE2XJ9FBZuEp3tSEJuDoCNW7Oeeo80YlrLvqeqSjbNN_oFn61vbrgJHLXsG7yBAwpmuL8ulu2JGE55yVofsDxH1kObjmtJOlzNTzzUA91cPc4BTBjlDnPFj6kt3879NSIS4rFZVdCbJjqVmlJy8Wkdpex1KwvPbVa7eNciS_shkLWNrezZH6KHY_5ny4fHn-WobZDNytnTjWQ5AX_qD8rBsaoPyt6LlPbwZYP1d3haZHQy6Krt0Nqv4uBo-AAJ9ekW5sp6f8mLqEGWuxfaJ-bEM0oN0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d685f955fc.mp4?token=I7hX5OXDOktwoYktOOEQQB-lG-4jH8I-cyOM8shjpC9y1PFUk8v2l0ZemQfgRk7-TC4QbTGyToRtrjTKULA5KzZOPucmel0WZU7ygZ3VN3FjRQfOZzuiaOy6HrcaWZLgn06G4MlAUiYwxApwuAsk0v3oz8ZNSK-HTGXmjAzM5K1FpEb1tBgK5BL6GlMUn_e3yGxv_vA7zGyo7DVq_eTFzjNLCaxRDWCsBO2-uAJwerOorDox8GKd5UeyYdeko5Fj2OoVLzkWPc3WjyZf3_9aSjE1ZfR7K2cITe2PcEOpp4ojxNaonJ1oeBMAHatbFA3xVonXs38sUTrCkOITEy2sK0LK1B_snB9QVhhd8aNzG86USomFgrOrVJBp5GhmGWs6M21RPmpc6yZSSsIWE2XJ9FBZuEp3tSEJuDoCNW7Oeeo80YlrLvqeqSjbNN_oFn61vbrgJHLXsG7yBAwpmuL8ulu2JGE55yVofsDxH1kObjmtJOlzNTzzUA91cPc4BTBjlDnPFj6kt3879NSIS4rFZVdCbJjqVmlJy8Wkdpex1KwvPbVa7eNciS_shkLWNrezZH6KHY_5ny4fHn-WobZDNytnTjWQ5AX_qD8rBsaoPyt6LlPbwZYP1d3haZHQy6Krt0Nqv4uBo-AAJ9ekW5sp6f8mLqEGWuxfaJ-bEM0oN0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
😳
عاشورا برا این اراذل هرچه نداشته باشه یه خوبی داره و اونم اینه که تا سال‌ها سوژه میتونن دست مردم برا خنده بدن
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67091" target="_blank">📅 16:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67090">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1a57a9722.mp4?token=dKjWMFUDlBX5vxe4awPI3pqJrpTtKKmLgktk03SvCgIr6fEwmtWHD3wHsCjxP7CzXutbkqKqnolFOWkIjcVLIiWsFV362EmTpmFgV23fVuPEXXv9En6pnDolC9MOANETOAyBauuxVzB_EIfIibuQ5cgR90NR59_lfgOXRgj8C7NqkfTkLaDLFZZmW1vkHvS81GRTSnjs3UjFQO23DSrVfOhBrOjgjD2H3v1DTBcUXHUy-GBbgDj9Yp2Vm4a7YpI9dyq4T65ZJ1pcTFEkc3EBX7dxrMTxAdENvZpp7VBg-3FOiFCAVZUuji0-Le20uHSTgtMIUXG2HABLLM4DMGfMiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1a57a9722.mp4?token=dKjWMFUDlBX5vxe4awPI3pqJrpTtKKmLgktk03SvCgIr6fEwmtWHD3wHsCjxP7CzXutbkqKqnolFOWkIjcVLIiWsFV362EmTpmFgV23fVuPEXXv9En6pnDolC9MOANETOAyBauuxVzB_EIfIibuQ5cgR90NR59_lfgOXRgj8C7NqkfTkLaDLFZZmW1vkHvS81GRTSnjs3UjFQO23DSrVfOhBrOjgjD2H3v1DTBcUXHUy-GBbgDj9Yp2Vm4a7YpI9dyq4T65ZJ1pcTFEkc3EBX7dxrMTxAdENvZpp7VBg-3FOiFCAVZUuji0-Le20uHSTgtMIUXG2HABLLM4DMGfMiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سخنگوی وزارت خارجه: اساساً برنامه‌ای برای دیدار با آمریکایی‌ها در هیچ سطحی نداشته‌ایم که بخواهیم از آن منصرف بشویم
🔴
گفت‌وگوهای دوحه دربارهٔ اجرای بندهایی از یادداشت تفاهم است و با هیئت قطری انجام خواهد شد.
🔴
اجرای بند آزادسازی دارایی‌های ایران در حال انجام است و امیدواریم کار به نتیجهٔ مطلوب برسد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67090" target="_blank">📅 16:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67089">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_ASFNZsqc4Ia0YTlXMx8oIV4Us0CxHM_QM0AnR0jQUNVFvn3VX3sGBepbKgdKI9LZTrWL6wKvRW8Xp-J-qczKCf0iCQbORhbDMbdf9JJ4lopFVBi1NUyakbqk0dqPHzWrHaoPW2cEqYvubKQey9_A6tFei_CFIM1nIvOE-cq1gLxiu9o2_kyNzKQIbRVpHi5UoiNcczPJPELEXhY5542hvklIcZz43r_3uLoUuEmT-0Ax4VWQCssbLK4CdNJ0WnxoaMjvax_HkLnBZcDRZOqRI-CCwExhX2Kb9FAqB-iCUUrpqEJ3Nfnt52MwRoawvjlsXbvX309S28SNgmnz-R_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
العربیه:
مذاکرات غیرمستقیم میان هیئت‌های آمریکا و ایران فردا با حضور میانجی‌ها در قطر برگزار می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67089" target="_blank">📅 15:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67088">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_c8enhIkVYeflL6QD9QoPcZdAMpo54kkPQFQlQ1a11cD-rtyr7TsID4TMn7s3D4b1eGBTut_PD6OFLeU2Jlvvt1-AjlGjghw4dzl-up2KpaTkOJyFWST5Syw1dHPMfAg04HVdXo42soqsu9-3GdTXiG9kj8ziYeiWQtrOviPHZHLFCTAvrgvC3F_g3nL_qaMfY_gGyBiLm136P8LihhKgfgfT9uqdvs3BP3S6OVZSzmgcibhtFaoIs-Axx51dgpQFblw15TQ-tDcT4kSrz9dWf2E1ec6llMCLQAqRTQR_0BhsN_JWSfWv8YyJxYCFKoFf4-l15g1l5zFki1TBjQaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه همشهری با این تیتر ترامپ رو تهدید کرد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67088" target="_blank">📅 15:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67087">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6f84963cf.mp4?token=jTw5pnhS3xDme5TSQL_GIasGiNelpLx6vQoxTlltQd0ntqUrsKYq7K6Qp-LtxoXFRXhRt8iUkRtAJgjyeQ2VtpFvBQ1tdDk49EYbDZ7FOVDQBShBE4nTjBh91KSdz3SaZgBeWsRXAgJBmKD82VRdqark8jjbKneEr3hEFmWkyFQAsRL79cVelIHNu7QyCEtv66r2OUwz5fbp3sblR93EAC-9btvL_k5tzUHZo5SuiS5SaQt4gDXFDw-n5WJ0V1t7Ydzm7o3583lpTHuMs2VQ9ssyk-pMWTpTQ-GHPa2Lva-moSwFZhfmLbbvWTuBN_oB8VwUvi5DlywqgdReuE50RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6f84963cf.mp4?token=jTw5pnhS3xDme5TSQL_GIasGiNelpLx6vQoxTlltQd0ntqUrsKYq7K6Qp-LtxoXFRXhRt8iUkRtAJgjyeQ2VtpFvBQ1tdDk49EYbDZ7FOVDQBShBE4nTjBh91KSdz3SaZgBeWsRXAgJBmKD82VRdqark8jjbKneEr3hEFmWkyFQAsRL79cVelIHNu7QyCEtv66r2OUwz5fbp3sblR93EAC-9btvL_k5tzUHZo5SuiS5SaQt4gDXFDw-n5WJ0V1t7Ydzm7o3583lpTHuMs2VQ9ssyk-pMWTpTQ-GHPa2Lva-moSwFZhfmLbbvWTuBN_oB8VwUvi5DlywqgdReuE50RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
ویدیوهای جدید از زلزله ۷.۸ ریشتری که در ۸ ژوئن ونزوئلا را لرزاند، در ساعات اخیر به سرعت در فضای مجازی پخش شده‌اند و لحظات پرتنشی را که در طول این لرزش قدرتمند تجربه شده است، نشان می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67087" target="_blank">📅 14:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67083">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qZhRiVx7CqVGmMWedMMzsJibmmO0fyQ4V_rWw9ObznyHPR4LqQEnv9BqfJN8dJlny7vB2DZgyPJCSgl0ogLI0a3DPGEkHMGkjsh0gNrd9hWo8id82FpiZ5-m4fzBj1vtenskaAx7l39GLqt-i3FCohqjl4zIICxFcCEuvBBOPJJyQrUvs6FmG59j6icNBfB5GR9F3etx1Clw1YldjJpUdOycHZ-9XEVt4U456tSSmtPpvau64VR1LIRlrp1Vo7KKr-KfWfI0QVLmKWeZPZn_epJ_YPmQRSlIoYM240wlZz-8XqyxfX3U-vmyE-Tkjt-xcpX5Njwvlkxdk278YcMFrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o1nB3pvqg2aWain5UR4rK2-ZeNExilUxFjMl9ZGfCknWMSCYERzRsD2bMGThqZ8K9cUC2noxqAjiAEfE95LVPkyYWw4Q51ZGNkBu6-choPCoxEMN5y3Jq_w2-Dl8a9qcDIaFWu0LBPs2_lf9b1d42HAwMJjePu_Oy893GBss8Gsyu_IaxWa2Rjsbspbm5awEpdzGIiJJ6jMAFFMzBjNYWZmneLi-3sve2RPbLF00MB8AIJzHzB8oTG_0c6uRemG5atrmQ9BHXzWdyojsMBODl9D2RJqnGOIZbh98WL8AuOD6Ecn_DYvVZquuq82ES6Cpo3iJSloYaL3qGfVrrFi5nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LTechhJdlE-vYNYBVIZNSKj_8ul7NaC-pfqsWXPgQPr_AP0-Z1NjZpvtDhn-vMLwh9FsHARAbjYwAv9aOcNc1lqjn2Zws0QnH4sgX5I2i1J9XhWs3bvuU1v572wfUockWpkt8Fo4WlkMAxrzWJ1RUyhtXKd2QuLrlBky2QqmXY3PLp7Z12eug2jR1DBE3WQ_wD2mEnam_Wp1FXKlm7jsfSbjXUsAd1-wTxCxpUTPQ1mDuCPaxedLDDCP04P_9y-UuZZhYWcSAfj1OfVeVIhoK02pn-1AxHaJfgMl_CYZONuIRRwMG6rkHqWJ7gOD7qJiAa3mMN5MZSKJN3DizyBJpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r1PZ1BTvYEs7xRwtCtf6duISrv1T_zpqzbxUs1VYvc8Gp323JL6IqfqwlaJzoaSoXsK_55EfKAG8WA9uxiYGMk0NHwaxyHM8ROX866kzfvtBFUTyG3B8LW1Db90k7gHL3dS0vlNjXzH826SS4DAbZ0EtJxRGW0S8X8MoVIECfa7dHtuAuCD7xPcjQOoaQpDYuB1N_hlj0EOuhuay0NfzpqEXGKu7fiWwRsEtAQjDwQJB3-1tuXcWuq9C8klIcCD8GqoapYqGX_JQ6BztauqNX_VGyzzWp_DFdcT0ZnCwzEEGT2rXadzdRvdt7vg5wzFgCQv4Cm1MymIrhzUh4oRN6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😂
یه پسر 19ساله به اسم آقا سامیار، اومده چندتا عکس از تولد خودش به همراه دوستاش تواینستاگرام پست کرده؛
حالا به دلایلی نامعلوم، این پست تولد آقا سامیار تو اینستاگرام فارسی به شدت وایرال شده و بیش از چندمیلیون بازدید گرفته:
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67083" target="_blank">📅 14:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67082">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
⚠️
قالیباف: سوپرانقلابی هایی که هیچ غلطی برای این انقلاب نکردند، ازهمه طلبکار هستند
این ویدیو از قالیباف مربوط به سال ۱۴۰۱ است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67082" target="_blank">📅 14:05 · 09 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
