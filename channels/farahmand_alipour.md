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
<img src="https://cdn4.telesco.pe/file/lk9nAbz9cDn0Ek948hnOI4XKAMDGgXn678-DZbg0N74Azp_eWdmiaJTHB7bmkMDOALOapS5GGGbsT4ha1WJGA0REkIg8y2qBWMWlPjLPQscxmemO5cOi5VP3o_2vQNnH-JPuXIAONhMJ1wvPni29pxFmffmWNKRro46c00wP78VGnk1YUxuqlmfLjXhCDST2VDE6JLpn5DdPQJ7Sftv2pA1b_jeLqfqtH95xZd-FEvWKY5KZ_zlA3xC30JlKKOvILASM5xC1nslc31pAJuOeV8jKURa3xq3uQF7teWIFBZkc_pSHLSXsh9OnA-4OoAgPCPIvok0Ubm2tAuNmI7kpzA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.4K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 13:31:37</div>
<hr>

<div class="tg-post" id="msg-5539">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=PpNkWh-LYhcXKzi--__peYv4BM1NW_YOstqn6UkdDmJaqptAg0HsW2UslKaoshBioVMYTDWyyrp7JJC9Hh78PimgGNu6cYN_tQDZbXhKLpckvqW_RnFiq2e--bjJcNQ3nKUGxYnxzy8Cx0WJSEM4F1dYwlJ0Ozth_WgGv02ffoUBskUB2wZqHvtj2mPmwWUaM5lVklkIGgWF0w2uF-X9TIGRjrSD8sOSjlDj14AVu16c33DNFwuHmoa7WiBojQdn3TTX1kFRBhLaYUnpJeZNXqhNAQDoUHTMVLpD7LL7q9T6fxSvfDPLHiwBbfzCq12avdVCxWl4bioahIQACzPWDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=PpNkWh-LYhcXKzi--__peYv4BM1NW_YOstqn6UkdDmJaqptAg0HsW2UslKaoshBioVMYTDWyyrp7JJC9Hh78PimgGNu6cYN_tQDZbXhKLpckvqW_RnFiq2e--bjJcNQ3nKUGxYnxzy8Cx0WJSEM4F1dYwlJ0Ozth_WgGv02ffoUBskUB2wZqHvtj2mPmwWUaM5lVklkIGgWF0w2uF-X9TIGRjrSD8sOSjlDj14AVu16c33DNFwuHmoa7WiBojQdn3TTX1kFRBhLaYUnpJeZNXqhNAQDoUHTMVLpD7LL7q9T6fxSvfDPLHiwBbfzCq12avdVCxWl4bioahIQACzPWDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان : رسول خدا و اصحابش
لت و پار شدن. :)</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/5539" target="_blank">📅 11:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5538">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
حملات موشکی حزب الله به شمال اسرائیل</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5538" target="_blank">📅 00:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5537">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=KcVHTOyTn3MVGouuMMQGKMoHv2d-I2g80VrUGw9qUBnw_rnTJgZyU2TyS2s3jfRvKRo0LRDQBXMASCDD7Jdx7HSwHPPIwx_gdtargChd57G28MsMrdB7KmJPgeTe5OEnjN4HxUCFoD3pg_NLKHC9HwxETeHmTy0S2QaEN1-Km1ddEbAtXbwXHNbjxooLKBldj4UpVqgShwHYh_qO1K7B94_YkdXoo05mUm3hfKkNvxPs8pGab4RSDPAzTXwA_2zNNpbeQSwI5Y0jV-08rIpCCXv6i9Ga3WVxinHh2KJtTtNjbAOBqrWOAYNDBs5HMrbO4P3hP9jd1R44JkDGWAY7BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=KcVHTOyTn3MVGouuMMQGKMoHv2d-I2g80VrUGw9qUBnw_rnTJgZyU2TyS2s3jfRvKRo0LRDQBXMASCDD7Jdx7HSwHPPIwx_gdtargChd57G28MsMrdB7KmJPgeTe5OEnjN4HxUCFoD3pg_NLKHC9HwxETeHmTy0S2QaEN1-Km1ddEbAtXbwXHNbjxooLKBldj4UpVqgShwHYh_qO1K7B94_YkdXoo05mUm3hfKkNvxPs8pGab4RSDPAzTXwA_2zNNpbeQSwI5Y0jV-08rIpCCXv6i9Ga3WVxinHh2KJtTtNjbAOBqrWOAYNDBs5HMrbO4P3hP9jd1R44JkDGWAY7BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زنان کفن‌پوش ولایی در برابر وزارت خارجه و سر دادن شعار : مرگ بر عراقچی بی‌شرف نفوذی</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5537" target="_blank">📅 22:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5536">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8679568b89.mp4?token=Fz-N3D8H7iUlwJu_hco59y0QPHx7WSdzwJUj3GHhJ9bs7LjOPzEZx_37dYx5txWSs9wUiC14KaMyVgrC_zB3kURBzo1-hCt1kQBACxHWS14liF_oEPNSpG5S3fv4H9OL97quzEcnzViM5U_o9Zy8DbKXwMvd1ScReVBYGsdMIC7OR6IJ0E8Nmai8LfUHf-PLflDXjv_8GMQXVkLIExJJ664nnVFkcDYnNE4ELuIdFw7WJLe6SpCVQMyP3NLCVM-ytAdB_wEd4hv-u9_2V2JMN37Ay-Y3uHbv3yUVg1R7_bDGOduOkGQFg924dSjiI03BtcGtsxQJpQAekkCWLoI40g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8679568b89.mp4?token=Fz-N3D8H7iUlwJu_hco59y0QPHx7WSdzwJUj3GHhJ9bs7LjOPzEZx_37dYx5txWSs9wUiC14KaMyVgrC_zB3kURBzo1-hCt1kQBACxHWS14liF_oEPNSpG5S3fv4H9OL97quzEcnzViM5U_o9Zy8DbKXwMvd1ScReVBYGsdMIC7OR6IJ0E8Nmai8LfUHf-PLflDXjv_8GMQXVkLIExJJ664nnVFkcDYnNE4ELuIdFw7WJLe6SpCVQMyP3NLCVM-ytAdB_wEd4hv-u9_2V2JMN37Ay-Y3uHbv3yUVg1R7_bDGOduOkGQFg924dSjiI03BtcGtsxQJpQAekkCWLoI40g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی که گفته بود
به خاطر هسته‌ای
دو بار با ایران وارد جنگ شدند
،
الان با ژست پیروزمندانه! میگه قراره
در داخل خاک ایران، اورانیوم غنی‌سازی شده رو رقیق کنیم!
یک ملت فقیر شد تا اورانیوم اینها غنی بشه، دو تا جنگ راه انداختن،
حالا میگن «در داخل ایران» میخوایم رقیق کنیم! ژست پیروزی هم میگیرن!</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5536" target="_blank">📅 22:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5535">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39d8066c06.mp4?token=VRBqP1E0gokN_Dz6vcM7FMp1ExWfjm9AFCCh4SsgWbGnNZvAd3mcvRptajQP5ZAI523ErHXwfY6VMDc5iIQIHHKAfmd06AcbQ-8mgWzk7GvQlXeFmDhY5A_uvMD1zeZs1DYOwGVt62JeM9lmlrwQhdMP6Vaye_gNLbKVYc4TUrXduhVeWNGaEQE0NBlvoNMSxPnFESqiK6pfQStifT33wv0o3Y3ecpQ5BT8hPxjjgBBJ_HEkGaDRP7JK7qo0-2IDcjBGzd3KBnmdarC9485uT0UUPdlBEqBv5j5QcLWTQqqL8dpNeL1K3JNOS9s2na1x9YaKoPZW3MeJzDs4js9IVSjK1Pys7o8iLxjYOIOToBXmoeGDk2jjeAMvCH2D15uqlr5gz8nukm-dZi-QrF-ubzMK-lR6adqbNfFDmtHd6RT9SGexlOz7cOwkeVmvbki_PFepCN-aJYVEq7klvtxZSzBytgbacvB-0t7Yd9c7yqQxf8c_CoTMzu1yGx-yXPXqrczpQARsO3WIDaoFFZaHd-fj2aCJxayu7wA1usIwxMSRc5IOLWxNWQuMc2v97DQgsdbsHeL-2i2AOdkg0ZVQcnfRsKfURsCuo1JsH_SutHrhriEHRDSRMF3x1Di4ecpsgI0vSSNyAvWfCGH94U-UZof1ddOyWR7dMaLJu0-Zwmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39d8066c06.mp4?token=VRBqP1E0gokN_Dz6vcM7FMp1ExWfjm9AFCCh4SsgWbGnNZvAd3mcvRptajQP5ZAI523ErHXwfY6VMDc5iIQIHHKAfmd06AcbQ-8mgWzk7GvQlXeFmDhY5A_uvMD1zeZs1DYOwGVt62JeM9lmlrwQhdMP6Vaye_gNLbKVYc4TUrXduhVeWNGaEQE0NBlvoNMSxPnFESqiK6pfQStifT33wv0o3Y3ecpQ5BT8hPxjjgBBJ_HEkGaDRP7JK7qo0-2IDcjBGzd3KBnmdarC9485uT0UUPdlBEqBv5j5QcLWTQqqL8dpNeL1K3JNOS9s2na1x9YaKoPZW3MeJzDs4js9IVSjK1Pys7o8iLxjYOIOToBXmoeGDk2jjeAMvCH2D15uqlr5gz8nukm-dZi-QrF-ubzMK-lR6adqbNfFDmtHd6RT9SGexlOz7cOwkeVmvbki_PFepCN-aJYVEq7klvtxZSzBytgbacvB-0t7Yd9c7yqQxf8c_CoTMzu1yGx-yXPXqrczpQARsO3WIDaoFFZaHd-fj2aCJxayu7wA1usIwxMSRc5IOLWxNWQuMc2v97DQgsdbsHeL-2i2AOdkg0ZVQcnfRsKfURsCuo1JsH_SutHrhriEHRDSRMF3x1Di4ecpsgI0vSSNyAvWfCGH94U-UZof1ddOyWR7dMaLJu0-Zwmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توضیحات نبویان در خصوص وضعیت تنگه هرمز در تفاهم‌نامه
- به محض امضای تفاهم نامه، تنگه باید فورا باز شود، بدون حاکمیت ج‌ا، گرفتن دوباره تنگه و اعمال حاکمیت بر آن تقریبا غیرممکن می‌شود.
- هر بار که متن تفاهم عوض شد ج‌ا عقب‌نشینی کرد</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5535" target="_blank">📅 21:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5534">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxvMDMbyy1RBGs9z-I4v_VyISib2O9Is0Mg9Q7fvhfhE2irrbBeimiX-jY19R8na68_wfU2gGtblY78-BdkqjkiIq6xWrvwZI8VWf6FzBDuE8WISQoxtkRdNS8zCJ77OCAZTry_v_uONtBfcS05K95DHN33uTtU7fBc-FM2sbzdSFlKNBeVgH8zp7-QfWak-TNUDuYQfjHjTwlnJ3pxgtma5YeGYfqabv0AOZoQZQrf7bHjI0wvOAfjs8es8VDq4hty-oKoghtArPBPpiKBgfKRaHJ8x_aNkFJC_vsUxlHJZXaQXVIKvvsrlz45ifouYzzhuLeG2awBlrB54Xn9yzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: اصرار ترامپ
بر امضای تفاهم‌نامه در حالی است که مقامات ج‌ا  صراحتا گفتن  تفاهم نامه هنوز نهایی نشده</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5534" target="_blank">📅 21:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5533">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4506bacd1b.mp4?token=LQmMyXxwzeJoQRKEjBKf2kbP_zmJrzVtjIrC34RQpqD_KRnxY96OK0Pvae10eRIQXd7x-aDjtmqNkB4g0en2b7qSjUjOoR46wM79A_-a4i3r4zrGcKA6Sco7jblAGG1NO5rSl71b3FEswXqLQY2tNaUJpkNP83VrtOoPX4v3wYTOsQLc6uloCVQjJUekQFs5Q2RWr0l9OmjDH6SzpCcuOxODWyRTrLf35GGvqJ6J75pstHscAM-dVPK_v0eTfyidZLOQczg7mqoUHmSPDZBht4etwdOfif2hJozPtLtABwF--c5t8eyx-2tY1iwpHO0RynQYqs5xVKzUV2xiLB0bwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4506bacd1b.mp4?token=LQmMyXxwzeJoQRKEjBKf2kbP_zmJrzVtjIrC34RQpqD_KRnxY96OK0Pvae10eRIQXd7x-aDjtmqNkB4g0en2b7qSjUjOoR46wM79A_-a4i3r4zrGcKA6Sco7jblAGG1NO5rSl71b3FEswXqLQY2tNaUJpkNP83VrtOoPX4v3wYTOsQLc6uloCVQjJUekQFs5Q2RWr0l9OmjDH6SzpCcuOxODWyRTrLf35GGvqJ6J75pstHscAM-dVPK_v0eTfyidZLOQczg7mqoUHmSPDZBht4etwdOfif2hJozPtLtABwF--c5t8eyx-2tY1iwpHO0RynQYqs5xVKzUV2xiLB0bwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۹ ماه پیش
بعد از جنگ ۱۲ روزه و قبل از جنگ ۴۰ روزه
این تهدید پذیری اگه به وجود آمد پایان نخواهد داشت.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5533" target="_blank">📅 20:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5532">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lnoSkR-Rj9T4YzlAZkjvyNcX4JyPrVEfnqYg651mUf94GyN_aUlKjffCKg0V_cloFI8zkmrWe8NJkHlPy5deabB5F_J9AJgsiOz2qirxpyiC6Bua1xwS5smaHPj2MWtlEo302W0Krabf7eSAEa44xZczzREEUUiLhFCvMI3mPjxEfiKsEUfYHB-wW--RlWXxMPo16AX6SENU4HC73IElhqqzDvN6aCf-04cbUo1XX6_NaqMRfFVFdQmoq3tses3gOhdpQHgi3IblIUuZlUTQubywHQOaUBpX8hiB2YJCZcp7ObvtpqZIok_RJW2HYXamKQsSaTlKx5EocN9n0l5Tww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ اکنون:
توافق فردا امضا میشه،
هیچ پولی بهشون نمیدیم.
دیگه به سمت سلاح هسته‌ای نخواهند رفت.
تنگه بلافاصله باز میشه.
بعدا هم اورانیوم غنی‌سازی شده رو از زیر آوار
و خاک بیرون میکشیم و نابودشون میکنیم</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5532" target="_blank">📅 20:32 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5531">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPPeYhVF2UVVvidUO1MTL_kc03ielRCXbZTP1c_rP6iRd69Pzw0outZj2adyL2jSZsdCBohZVt_0Ej1sElyoR7I2ijoRyKTxSpqvIMr_0Pb7omZ6IsBzU0RP_V93Jh4s3M_OBm9BN4mCcOd27tB-7jmMnsqnJpk9C-1LBbvrc_-hn23GZ_QR1miAUDF0sA8--hjtLY2rrnh0WncA7In4L4E6uoet7G-vGKBvzuAee62vVpYH2e1sV_iYRJ8zT48SfzA5KsTlQa8geHN-XeCRp8KGRHiendeqhm8CT--q9srjBnLtxql5yY_ib3pKWa5CiY4qRwoda_ZZfPnIjCZc_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیسی خطاب به قالیباف نوشته.
نگذارید خط تسلیم و سازش با
قاتلان خامنه‌ای به ثمر برسد.
(نه سازش نه تسلیم - نبرد با آمریکا!)</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5531" target="_blank">📅 20:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5530">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-L7b5G23Cku8i9d7JEgr3RmzLg3LbwLLzYHZMR06_sUHW80ZZG3uJXy4aVeT87H7syKRFjcMiHaY2tf4v288gD7fK7aVOK4tAMSOWOgo_0BFmgK3ZFmHdv6ulPY7cD6XT-9yWZAX1gtl1JksVfdCCZ6Bn8OIXZu5w9a1Foaci3kgozHAB5Td2393qVlgSSG_n22rhlFfIEosLhzETj2-FwsujX5WdczYUiBwAS1_AbXOVwKvD5-YfiDOhXg73eG36c-OFkQr6sw66VX7xEOCqzzhXPg3s5ZYCRNIY-gJvCkti8apDRuqVdkYEVeXbYAi09shqWYrQxHfwDKXLrkUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوسف رجی  وزیر امور خارجه لبنان:
«حزب‌الله یک نهاد نظامی غیرقانونی
و بازوی مسلح جمهوری اسلامی
برای بی‌ثباتی منطقه است. اقدامات حزب‌الله، لبنان را وارد جنگ‌هایی کرده
که هیچ ربطی به لبنان ندارد.
ما فقط میخواهیم در یک کشور عادی زندگی کنیم! نه اینکه همیشه در جنگ باشیم.
مردم ایران گروگان نظامی
تمامیت‌خواه هستند.»</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5530" target="_blank">📅 19:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5529">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">نخست وزیر پاکستان: تفاهم‌نامه ظرف ۲۴ ساعت آینده امضا می‌شود.
عراقچی : برای ۲۴ ساعت آینده هیچ برنامه خاصی وجود نداره.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5529" target="_blank">📅 17:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5528">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4fd75ecd6.mp4?token=A8uFMRkQpBki5xZH_HjLS8Hxhs1NZhqKiQ-igP56kWc8V5HBC5JEML_U_NpWIJ344bpwcPzkoqku5hJ6x02JYsG133awg93KCBrz7Wo04dU5vyvEGyyPZjKxx-RouMvc_qG52pp_pN-S5fNMObAg9TImDta8BPVA_3v7v8oyTi1o3O4298CAaatEciKgNxdB-XckzUuEDKUIk7dq1how9JPFTPJ2QGDE-Jv0tnsJpDXpOQSoj-1ZDs2olMcX2h4RsLk4Na8730Y4-z5KFvkF9c3q4CVAbShRJKv8M7RO8CyNoXE_SLgtQd-LTHL6rA7JGfjC02op8hRFsHzcveFitQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4fd75ecd6.mp4?token=A8uFMRkQpBki5xZH_HjLS8Hxhs1NZhqKiQ-igP56kWc8V5HBC5JEML_U_NpWIJ344bpwcPzkoqku5hJ6x02JYsG133awg93KCBrz7Wo04dU5vyvEGyyPZjKxx-RouMvc_qG52pp_pN-S5fNMObAg9TImDta8BPVA_3v7v8oyTi1o3O4298CAaatEciKgNxdB-XckzUuEDKUIk7dq1how9JPFTPJ2QGDE-Jv0tnsJpDXpOQSoj-1ZDs2olMcX2h4RsLk4Na8730Y4-z5KFvkF9c3q4CVAbShRJKv8M7RO8CyNoXE_SLgtQd-LTHL6rA7JGfjC02op8hRFsHzcveFitQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان مناطق اطراف نبطیه رو تخلیه کرد تا در مسیر ارتش اسرائیل نباشه.
این جنگ بین لبنان و اسرائیل نیست.
جنگ میان گروه تروریستی حزب الله لبنانه
که با پول و سلاح جمهوری اسلامی و به خاطر خامنه‌ای، جنگی رو راه انداخت.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5528" target="_blank">📅 15:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5527">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMPBtqaOtaiRMApZXl_vXIJlLK9tl7hjDM7I_6x-HEwFq5Gp-k-TfR_TkGqVQxNrz61l1-InDzVwWD4oouL2PNhzz63sqOhG41d8FLE2YuQ6eT3wEdTr6GMllIwWN9IsSBq-ELmGxdHYTmlPwlgpqmhzm3zBm-oyN5sDwprIa2ZxBi0_3rvtSyjpwOi3OHYNVvumG3exUqQoDHs-Cfrd3vuw1yxrXHV-e5T-t-81bpvo4wjZQZg5Di-AABhnkgBTKFKUaBtqfbtoZseSXZ64nYBk93NW-uXFilZzCC-WFSQxwIeEkQgTKNd41Kj9Pu5Kifj1qvZlKSRZAIO7jOlEjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی در باز بشه می‌فهمید
مجتبی خامنه‌ای در واقع همون قالیبافه!
چیزی به اسم مجتبی وجود نداره!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5527" target="_blank">📅 15:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5526">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3bW5-znPUbz7T_mEDYd2u34_9RLx4tJs5lx_UZLZ7157rPzqG6sdXxE2NIZpOKh4Kq0279xNU5Ph-uRr-kXi4gLYbhWr5OfDzBssxAjDQb2cosaVWmVbUXMkBiEcUITjqwsZld5Mu7J6KgjL9a8THz3jNRGQ2Fc33y3Pz1EtH2HAQWDALmncL6NaDO_MjYfg0IMR2989zIUeqwHDxzjjj4DeobnB_-pMoyQPogMJf6ozbumqfmq32CuVquLDhHrXS0qrOwXEUz5CcNxR4W1dbUhmSeDxNVn5jbojfWjY0RJ6u-7HmRbQIWFM_mQgf5_AW0AMXMLGaLlkVC8E3qaLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : ارتش اسرائیل دقایقی پیش
به حومه شهر نبطیه، یکی از بزرگ‌ترین شهرهای جنوب لبنان رسید.
اکثر جمعیت ۹۰ هزار نفری نبطیه،
از چند هفته پیش شهر را ترک کرده بودند.
بعد از حملات موشکی ج‌ا به اسرائیل،
اسرائیل فشار بیشتری بر روی شهرهای بزرگ جنوب چون صور و نبطیه و….. وارد کرد.
ارتش اسرائیل فردای حمله جمهوری اسلامی
دستور تخلیه شهر صور  - بزرگ‌ترین شهر جنوب  لبنان - را صادر کرد.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5526" target="_blank">📅 15:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5525">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hvlyJ8uC6t3SzPtwYFdFwkfNQ11cYhD1SN-g5ZOXQh59YKzFG_gU_u78Qfa5HtIVO0-AjpTDnWNIka4wC9MnTPYANCQBwqYDzBhAjiUO7kHkpBau4Nx08SfudOWeTsCDy1o13GjIZbeo03bEzLuZ5I16uBpD6sge8_wnhgavG4D6XDeqxD8QIT2o9NxvFyHbtJY6oR5kQSF74yUgdaFrT6tyTiWAxkYGLpxWPe8_Ad9ARHXsNFkQDy-g2ItCz6udqiXqb6v2rvvK-gTjx82UnOLh4b4SzudLnE7F5piWNLR8n6DglxayQw9S8TLnYN5NIcs5UunfW5UhCAJOP5kKvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیات مراسم تدفین خامنه‌ای</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5525" target="_blank">📅 13:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5523">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iw82w81zNzL7B9xdO9hOuzML6P6XkvOEVADadsezGhKMInuR4VVEVURK25dlM68Vn9YDfAVdbazAJq06O4zsGWI1U06IYspo_gGSR05CH70Ff2lf0zbElF5poo46MwJOGZG6MuT5UmmfEMCZEKdtrQT4hiP65hhjapHuemR8UB1ohEfwYBFAcRgIza91pNhd1Adwasrk5XeXJj0yP-KFJtgky0s87gbPkZbXxkqcpwaZ6eG-gLoTdS96TE9Nu2v4eV2DEr_dDthAxySXbkKoddL_jseAqzjiwpqyKv7gKkFsau7TG1-pul1xFShSl89-CRluD6Hx02DscNiWdyl2CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a9cd24845.mp4?token=fMdGAERgJMoBKAAKOFBfuL090VHOGiijSn9HQ1jTnBBC-wZZ8tSqM6UMUpd5L0Zq_rmTUw91yh2GsXSzApv2FYjDxU2m-CJFuy2kA_w-ZTJyA7OBcW57ZpIdHXqI4Rw2pE75abp5r4qMgHkwgID2dwKE4w2sNxjd-QYTgbgATWRqnt0WKp1U6_hKBXsfGRVPTyC8IHGkyg4CgYa_pcFaEg_qcAoTHU0An_vBROoc7CPGZwPEhSFFfsgkXpg6ScQ1QQUzELasa20bRboab_ewSiudxq_1NfVPtszQm4ysdQTnZ6sMKIxdxaXbQNf7cXYMuMbjKkW4mdlECf6y0hi4-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a9cd24845.mp4?token=fMdGAERgJMoBKAAKOFBfuL090VHOGiijSn9HQ1jTnBBC-wZZ8tSqM6UMUpd5L0Zq_rmTUw91yh2GsXSzApv2FYjDxU2m-CJFuy2kA_w-ZTJyA7OBcW57ZpIdHXqI4Rw2pE75abp5r4qMgHkwgID2dwKE4w2sNxjd-QYTgbgATWRqnt0WKp1U6_hKBXsfGRVPTyC8IHGkyg4CgYa_pcFaEg_qcAoTHU0An_vBROoc7CPGZwPEhSFFfsgkXpg6ScQ1QQUzELasa20bRboab_ewSiudxq_1NfVPtszQm4ysdQTnZ6sMKIxdxaXbQNf7cXYMuMbjKkW4mdlECf6y0hi4-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز میگن دشمن جمهورى اسلامى
ايران اينترنشناله!
همين چند سال پيش تلگرام دشمن بود!
حتى «روح اللّٰه زم» رو به خاطر داشتن
«يك كانال تلگرامى» ١عدام كردند!
توی صدا و سیمای نکبت‌شون هم گفتند :«شاهرگ رسانه‌های بیگانه»! یک کانال تلگرامی!
قبل‌ترش وبلاگ! ستار بهشتی رو به خاطر نوشتن در یک وبلاگ کشتن!
قبلترش مشكل «روزنامه‌ها» بود!
چندین روزنامه نگار رو كشتن ، دهها روزنامه و نشريه رو بستن!
قبلترش مشكل راديو بود!! دهه ۶۰! امت حزب اللّٰه بیاد گزارش بده كى توى خونه اش راديوهاى وابسته به دشمن رو گوش ميده!
تاريخ جمهورى اسلامى همين نكبته!</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5523" target="_blank">📅 13:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5522">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">عراقچی : در دو جنگ گذشته، «مذاکره» منتهی به جنگ نشد،  بلکه «مقاومت»  منتهی به جنگ ‌شد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5522" target="_blank">📅 11:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5521">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dHEpR0_sRjAMdPLqrSIBWRRuhZv4pky6cu8fXiV4_axef3tj--bMmGReFHVtEW6Vnx2FAqUT946EDigc1K_eqmDwNiZRjp5WAujiHiOZM9XFK-J08Uo7o5z4P_WuppIrOoXukM2EDd6GrfyrkuO_F2bYsCOMGiMK15zFg5qBb8gjV6JVZiMwRk0hTQWMmXHTp4Wl03MlIlxH8mdEXsv17AVIq4FPTw_rmKQYD-Ytdu0pTz3h46Xm0u8W5AFYG91B5zxZDIbAxX2W5sft9d0AAfDtxGaSeh0pGcn9epAiWR-o-DOUQWdevHuvEaW52iYPNAmBKk1n5jwbYDbvL3b6uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگن ترامپ میخواد ۱۰ میلیارد ،
۲۰ میلیارد از سرمایه های بلوکه شده ایران
رو «آزاد» کنه،
و این رو همچون یک پیروزی دارند به حامیانشون القا میکنن،
جمهوری اسلامی بعضا سالانه
۱۰ میلیارد ، ۱۲ میلیارد دلار تخفیف
نفتی به چین میده! از سرمایه‌‌های مردم ایران!
اون بلوکه‌ شده‌ها توسط آمریکا یک روز،
دیروز و زود نقد میشن،
این چوب جراحی که شما به ایران زدید
هرگز برنمیگرده!</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5521" target="_blank">📅 09:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5520">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwyBSdE-TplReEiPuf4ysgIWqcVSBlETdVp2hjSbvkvMAApbrdjajnOY8TQzbA_UBhCGHIBOUWps9uaFUvlf3UfSa0GgcM8yJt4wOleRHhWaVQAuzl2OWU0yrYozSxiZdAVwPgS-WiH8ylPBG_Ehqsr4yru50YRBDvuTTqARsdHl-KwugRr7c0fiSz2RcHLwcGoXOJpqtQulo64kF3jGCtmuGFedA5jOhGy4YQVIz-lp9vx5sfxpiLY0Bl18CYHNYx8xrYpDdeNkkBA60YeYX6DHcVo0IRYZRhm_LF5Hzw2eZxuNzuN21sqbLck21LLF_u5aN_AjJtIjw7ktcQstzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5520" target="_blank">📅 01:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5519">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=PlELX_cnLd0uB7kz0_7ylzcySY5cZ3R8SFoMc49J-tTK5hfZlhjl6LFp1fIdQFqTgkTkyr0sqlXheqa6NZYha8A4GVwVqbEDKc-2aNR1VFF29zMy-VhxoFkYbIXPLT1zB10sbOREDWxRHqpbmaXIuTMPi4wkr0uWmkrvMFIuKiFekFztGSXXBYPaPVCBBc-0Sg0VdAMn2dvZjo8yiUxukkz46j0fCc6VmpAoYyIYU4zdgJYqq_Lzs44KobGWivcbQACakAOl4LvdfdzDSb9f9NjnRnuU8lQ1Vv2siLvLZdMwUsQKViBwb9Imv4XwlE1BoRrGZe8m0_hY9l1f6AnRT2Pm6ho2S0boJgJ1wmmQY-QjyYNpszWTt73PYTKYHPptO1O2yvitTRpBdgb-Zz8EbFhz1Lpkf6roD6pbwGdUT_TKegIDHdi4IUqFNHM88eC0k8R3aiKLctV_nplqHeznEfCkb0_22_j8FioRbPSrW59dsCCk3LLY63WsJZBiqaVLclgSZuTBg9eGIuCHUWAclBb7RsSKM_SQFM3rSKhtmJUdMfNh4DRSegHsAs_yhM4T1j1ARFEE0ozYuKmOS4Acj9jLqW3JYtT8ZArbkzjXVELocWl8BFbHUH3msMOLcreJG5BZmACCxsKhUmNc_8WLvKrESdGNKbxhV19WCQgUr1s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=PlELX_cnLd0uB7kz0_7ylzcySY5cZ3R8SFoMc49J-tTK5hfZlhjl6LFp1fIdQFqTgkTkyr0sqlXheqa6NZYha8A4GVwVqbEDKc-2aNR1VFF29zMy-VhxoFkYbIXPLT1zB10sbOREDWxRHqpbmaXIuTMPi4wkr0uWmkrvMFIuKiFekFztGSXXBYPaPVCBBc-0Sg0VdAMn2dvZjo8yiUxukkz46j0fCc6VmpAoYyIYU4zdgJYqq_Lzs44KobGWivcbQACakAOl4LvdfdzDSb9f9NjnRnuU8lQ1Vv2siLvLZdMwUsQKViBwb9Imv4XwlE1BoRrGZe8m0_hY9l1f6AnRT2Pm6ho2S0boJgJ1wmmQY-QjyYNpszWTt73PYTKYHPptO1O2yvitTRpBdgb-Zz8EbFhz1Lpkf6roD6pbwGdUT_TKegIDHdi4IUqFNHM88eC0k8R3aiKLctV_nplqHeznEfCkb0_22_j8FioRbPSrW59dsCCk3LLY63WsJZBiqaVLclgSZuTBg9eGIuCHUWAclBb7RsSKM_SQFM3rSKhtmJUdMfNh4DRSegHsAs_yhM4T1j1ARFEE0ozYuKmOS4Acj9jLqW3JYtT8ZArbkzjXVELocWl8BFbHUH3msMOLcreJG5BZmACCxsKhUmNc_8WLvKrESdGNKbxhV19WCQgUr1s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی : در دو جنگ گذشته، «مذاکره» منتهی به جنگ نشد،  بلکه «مقاومت»  منتهی به جنگ ‌شد.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5519" target="_blank">📅 00:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5518">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=JF3Aci2zGiSDR9wzDPjRBKqSQalTE4BH__zFgGH-ZMy7c_D4aLgeUtgJOBPd8lKYkjMIlgD4Jp08MXCxgZgOJJ8ZD_7AWzCWberAfywbDh_b2Kmy9b6SmLW4s0eWrdp72MJF620fvD2WQ9_HNxil4RMj5K0XgPIXQA-pkkuAOaKBSUkXpue-nFo1qg0DvyAvIqJBKhUAbXwx0PHrmZN14ZgFtsq21AxPm4iMoo6RVn2W5sSR2IOvK9vNAW2N8_KnkwH559bjrLtT-SMLXvVKkOpumrvRTaASR5TZKOHneKum1A0C4RYKn3PoPmXNkXM5yHynXEcqqIClyKTQ7RX6fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=JF3Aci2zGiSDR9wzDPjRBKqSQalTE4BH__zFgGH-ZMy7c_D4aLgeUtgJOBPd8lKYkjMIlgD4Jp08MXCxgZgOJJ8ZD_7AWzCWberAfywbDh_b2Kmy9b6SmLW4s0eWrdp72MJF620fvD2WQ9_HNxil4RMj5K0XgPIXQA-pkkuAOaKBSUkXpue-nFo1qg0DvyAvIqJBKhUAbXwx0PHrmZN14ZgFtsq21AxPm4iMoo6RVn2W5sSR2IOvK9vNAW2N8_KnkwH559bjrLtT-SMLXvVKkOpumrvRTaASR5TZKOHneKum1A0C4RYKn3PoPmXNkXM5yHynXEcqqIClyKTQ7RX6fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت نبویان از متن توافق ج‌ا و آمریکا :
یک : طبق متن تنگه هرمز باید باز شود.
‏دو : تحریم‌ها برداشته نمی‌شود.
‏سه :در مسأله هسته‌ای مستعمره آمریکا می‌شویم.
چهار: آزاد سازی پول‌ها اعتبار ندارد.
‏پنج: هیچ ضمانتی آمریکا برای اجرای بندها نداده است.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/5518" target="_blank">📅 19:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5517">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">وزیر دفاع اسرائیل: از جنوب لبنان خارج نخواهیم شد!</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5517" target="_blank">📅 19:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5516">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5516" target="_blank">📅 19:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5515">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5515" target="_blank">📅 19:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5514">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
عراقچی : هرگز تا این اندازه به یک توافق نزدیک نشده بودیم.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5514" target="_blank">📅 18:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5513">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVDxrZ50fyADmkzp7iOYbIoGPTjxMVPLjYne7qM_qrvDvPur5l4SSsqivJ42KNpW2v2Z3fndXLwXOANIdD2hHLv90agItp_1qZ7gmTIBlty2Ag2KOKK_97hvw-TwKm7hl58PT8lWuSHI_BP-sj_e7zUN65qFCqDLwAB6iyC8Ej7C-dBtEGH60CuJr6GBUeBdyg_q4BiQ3ChWMGMHx6mEzX5-TAXZuxlxFse2Igf-3kJ-00jC_QbzxNrwc_NjsxT3FCK2-iJhBH10sdZkzdvlwrjGMahm1zqy6CPC-BbYiq-rBfiGJHhoS-aREml3Xe66k7-4g-0B6v0inBJyLibU0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ : این مواردی که جمهوری اسلامی منتشر کرده دروغه! اینها یه مشت آدم بی‌شرف هستند، اصلا نباید با اینها مذاکره‌ای بر پایه حسن نیت صورت بگیره.
حواسمون هست که دیشب هم با پهپاد
به یک کشتی هندی حمله کردند.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/5513" target="_blank">📅 18:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5512">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=FI3U9UsJC0dLrXvNBd0gv4XWU4SVvNuml7nN0RSaUWEgBzwaWb4iM-gkvVrs6kVU0nLUQqJ5L0dMnpnJ1fsUWDOYKMlQAYhmZWFeormiua9ZyFbDZoRcVlfN6cisYdRyfxQlebrvsQgW-H1NytygMQQ2aZshSUMHMsw8otuodJgqbOmNJ_QUw--9vnbIE2su0sZJqJsviv_fFBpuWlq_KEx8-CUmnM2gDPUXw7cE0N6KOb_5Qr8bYHYNRGHaVEPRUDJbCgy_RJMV6s9hSHBeDHIrHQuPkw4K7_MNGRA60VAzzCVhBMgzZKDyvuWLT_ieHNusly464zyyTnaKlJuFug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=FI3U9UsJC0dLrXvNBd0gv4XWU4SVvNuml7nN0RSaUWEgBzwaWb4iM-gkvVrs6kVU0nLUQqJ5L0dMnpnJ1fsUWDOYKMlQAYhmZWFeormiua9ZyFbDZoRcVlfN6cisYdRyfxQlebrvsQgW-H1NytygMQQ2aZshSUMHMsw8otuodJgqbOmNJ_QUw--9vnbIE2su0sZJqJsviv_fFBpuWlq_KEx8-CUmnM2gDPUXw7cE0N6KOb_5Qr8bYHYNRGHaVEPRUDJbCgy_RJMV6s9hSHBeDHIrHQuPkw4K7_MNGRA60VAzzCVhBMgzZKDyvuWLT_ieHNusly464zyyTnaKlJuFug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات امروز اسرائیل به صور
دیگه نمیخواید بهشون کمک کنید؟</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5512" target="_blank">📅 15:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5511">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
رسانه‌های حکومتی :
جمهوری اسلامی کنترل تنگه هرمز را رها نخواهد.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5511" target="_blank">📅 14:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5510">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nuPnS4vDvoVVpLDnCB-yhLB6WX0Tc43Cv0l9yxRROBZPTG42GkxJ4dC1WXaKC_CLcwwBju1sl_VXfMJ1wiW3Ly14kNInNRy3K1jII-XhVw8eNI19P6RxOgSoZ-lbBavKVrC52ZupgPUHoeiHA7zTQ1pRt7MaqkWlTNXP91JAK_Hd9lSckduMbyydi5HN2_janvS7cSgYEIs0LSvnTI7q8hWGbWY3JC-1g_-HgdBFZAstDa2ITR1264_JLpZ7yKSx8jTM2LWdNCi1HBsG7Ad2sc55ahY2bTNzDBKMTaR8SZpfThJUyY2z3u_YSFta_5XFjW_sqOEI9oY196M9S5nuMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
قطر خود به تنهایی حدود ۱۰۰ جنگنده بسیار پیشرفته دارد. شامل ۳۶ فروند رافال، ۳۶ فروند اف ۱۵  و ۲۴ فروند تایفون.
🔺
بریتانیا برای حمایت از قطر ۸ فروند تایفون در این کشور مستقر کرده.  قطر همچنین میزبان بزرگ‌ترین پایگاه نظامی آمریکا در منطقه است ولی اجازه استفاده…</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/5510" target="_blank">📅 12:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5509">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">حتی اگر همین امروز جمعه، جمهوری اسلامی و آمریکا به توافقی برسند و آن را در مکه امضا کنند، بازهم این توافق به شدت شکننده و عمر آن بسیار کوتاه خواهد بود.
آمریکا حتی در بدترین حالت، می‌تواند با یک «جمهوری اسلامی مسلح به سلاح هسته‌ای» کنار بیایید! آمریکا بیش از ۷۰ ساله که رقبایی داره مسلح به سلاح هسته‌ای.
روسیه، چین، کره‌شمالی همگی رقبای بعضا متخاصم آمریکا و غرب هستند و همگی سلاح هسته‌ای دارند!
۲۰ سالی که کره‌شمالی مجهز به سلاح هسته‌ای شده، نتونسته کوچکترین آسیبی به کره‌جنوبی و ژاپن و آمریکا وارد کنه، اما گوری  از انزوا و فقر که برای مردمش کنده بود، عمیق‌تر شد!
کوبا همسایه آمریکاست، ۷۰ ساله شعار ضد آمریکایی میده!  آمریکا اهمیتی نمیده!
مشکل اصلی جمهوری اسلامی، آمریکا و توافق با آمریکا نیست! مشکل اصلی جمهوری اسلامی داشتن سلاح هسته‌ای نیست! می‌توانست حتی، مثل همان راهی که پاکستان رفت، ج‌ا هم برود !
مشکل جمهوری اسلامی دشمنی ذاتی‌اش با اسرائیل است و تهدید موجودیت اسرائیل و مسلح کردن و پول‌پاشی به گروه‌های تروریستی است برای تداوم مبارزه و جنگ با اسرائیل!
آمریکا می‌تواند حتی با یک جمهوری اسلامیِ مسلح به سلاح هسته‌ای هم راه بیاید ، آمریکا عادت دارد!
اسرائیل اما قضیه‌اش فرق می‌کند!
پاکستان ‌و هند ۷۰ ساله در یک درگیری پر نفرت به سر می‌برند اما پاکستان هرگز شعار نداده که «هند را نابود می‌کنیم.»
تا ‌وقتی جمهوری اسلامی دشمنی و خصومت علیه اسرائیل را ادامه دهد، نمی‌توان به هیچ پیمان و توافقی خوش‌بین بود. خصوصا حالا بعد از ۷ اکتبر! بعد از ضربات مرگبار به حزب‌الله لبنان و بعد از  اینکه کار به رویارویی مستقیم ج‌ا و اسرائیل کشیده شد
و بعد از تجربه جنگ ۱۲ روزه که به اسرائیل گفت می‌تواند به تنهایی با ج‌ا وارد جنگ شود.</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/5509" target="_blank">📅 09:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5508">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=o87K0hLA8SuBzxGXS6xGkrqO_yiM7Uw8i9nLVdjeWvBPyaUwFKPcVVkUz5CSPtfSQfDancQ850dXfHXvMvSk0X-7PxVwZaneMd4CWHZFpJoukkDMy8PVlT4-ZuJbXIyCbO3GSmEOEmsowPzd0nucSo07bZWy0_xQ8tMHmN7fJ5SYtyk1bqGeC5PO2Tldmwj8yI0d2vP3oPShK6LsOz8jQ1Ahmk63749esc8Kvmy3K4RmpVJ2f2qEKaSIvAbevcBJCVA-lQGCnmBMcrGGI_tO_VT81eXfJabf6OKdx5DMZMpusnu3FNWCKEOeW7Mc5K8h_kYi2O_oNE1PDCmpkO7ylA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=o87K0hLA8SuBzxGXS6xGkrqO_yiM7Uw8i9nLVdjeWvBPyaUwFKPcVVkUz5CSPtfSQfDancQ850dXfHXvMvSk0X-7PxVwZaneMd4CWHZFpJoukkDMy8PVlT4-ZuJbXIyCbO3GSmEOEmsowPzd0nucSo07bZWy0_xQ8tMHmN7fJ5SYtyk1bqGeC5PO2Tldmwj8yI0d2vP3oPShK6LsOz8jQ1Ahmk63749esc8Kvmy3K4RmpVJ2f2qEKaSIvAbevcBJCVA-lQGCnmBMcrGGI_tO_VT81eXfJabf6OKdx5DMZMpusnu3FNWCKEOeW7Mc5K8h_kYi2O_oNE1PDCmpkO7ylA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاور قالیباف:
دو نگاه وجود داره، نگاهی که میگه بریم صلح کنیم، بسازیم، یه جوری مشکلمون رو حل کنیم.
یه نگاه دیگه اینه که صلحی در کار نیست!
ما قراره با اینها بجنگیم و قراره اینها رو تسلیم کنیم در برابر اراده خودمون.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/5508" target="_blank">📅 08:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5507">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=ExvioieWYNWzO-G9oWYduMAE8RpXhJ3Y8rp9HmKej7I55XvYS7VFfjQwfxgblkmDULVKFMrYtPWWh-DsETpV3iUxskxaD6bIyPoloT5C06lCmT3P9kaEkixPXbx1dBKnxV-8DLAALps6Ukh5pkIH4LXg-OBwFOYWtyfMEyA78EL-74hW1N7IRjS4xZmQc5AEiyiaEDsWb-daEq8e87MkhTYjP1BCbXisk3Gv7gZ8XnOsIHts61F3i4HAqfbMxixvyJjdqnBZWE7ePAiImjSa-PtG6JC6oKHz6mxwUeM6L6i0bOmQWsVk-1aP2d4SOTYoUBhbLK8ccRC6yGzwp0HWLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=ExvioieWYNWzO-G9oWYduMAE8RpXhJ3Y8rp9HmKej7I55XvYS7VFfjQwfxgblkmDULVKFMrYtPWWh-DsETpV3iUxskxaD6bIyPoloT5C06lCmT3P9kaEkixPXbx1dBKnxV-8DLAALps6Ukh5pkIH4LXg-OBwFOYWtyfMEyA78EL-74hW1N7IRjS4xZmQc5AEiyiaEDsWb-daEq8e87MkhTYjP1BCbXisk3Gv7gZ8XnOsIHts61F3i4HAqfbMxixvyJjdqnBZWE7ePAiImjSa-PtG6JC6oKHz6mxwUeM6L6i0bOmQWsVk-1aP2d4SOTYoUBhbLK8ccRC6yGzwp0HWLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی ظاهرا متقاعد شد که شرط و شروطهای ۱۰ گانه‌اش رو کنار بگذاره.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/5507" target="_blank">📅 08:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5506">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">صدا و سیما : شنیده شدن صدای دو انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/5506" target="_blank">📅 01:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5505">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
ترامپ : توافق با ایران باید همین چند روز دیگر امضا شود، با حضور ونس و در یک کشور اروپایی.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/5505" target="_blank">📅 23:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5504">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
نیویورک تایمز:
مدتی کوتاه پیش از آنکه ترامپ حملات به ایران را لغو کند، با پاکستانی‌ها که با ایرانی‌ها میانجیگری می‌کردند، صحبت کرد.
به گفته یک مقام ارشد دولت آمریکا، پاکستانی‌ها به ترامپ گفتند که «ما با ایران به توافق رسیده‌ایم».</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/5504" target="_blank">📅 22:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5503">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، به نقل از یک «منبع آگاه» نزدیک به تیم مذاکره‌کننده ایرانی گزارش داد که رژیم در ایران هیچ متنی از توافق را تأیید نکرده است.</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/5503" target="_blank">📅 22:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5502">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
اکسیوس: ترامپ حمله را لغو کرد، چون قطر گفته بود که به یک توافق رسیده‌ایم و فقط مونده امضای مجتبی خامنه‌ای، اما حملات دو شب گذشته آمریکا،  هم ج‌ا و هم قطر را نسبت به نیت واقعی ترامپ [که جنگ میخواد یا توافق] دچار سوظن کرده بود.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5502" target="_blank">📅 21:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5501">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
ترامپ : حمله برنامه ریزی شده امشب به جمهوری اسلامی را لغو کردم!
گفتگوهایی با رهبران جمهوری اسلامی داشتم.
محاصره دریایی اما همچنان برقرار است.</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/5501" target="_blank">📅 21:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5500">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
ترامپ : هر شب بهشون حمله می‌کنیم، تا اینکه به توافق برسیم.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/5500" target="_blank">📅 20:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5499">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">حمله‌شون هیچ کمکی به لبنان که نکرد هیچ!
هیچ ضربه ای به اسرائیل وارد که نکرد هیچ!
فقط یک پتروشیمی در ماهشهر از بین رفت و اسرائیل فرداش، برای اولین بار دستور تخلیه برای ساکنان یک شهر رو داد!  صور!
دیگه نمیخواید کمک کنید به لبنان؟</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/5499" target="_blank">📅 19:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5498">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qFwcC4coYy4eT8Q1Bwy7O4hOxcUZJYy6P9PYZbhnSHJkiDfdG-bNrKqw-0qqMydf9nsIDzNwzefWkPx8jRftnL28VeAnnPIO27dzZxRi-z6uD63hCaMF2jdhySI4Ne37GnoAj0ku96PIsZC8pHnCKWuo7gS2EpQImR9oXkhFJVuuCKiAN1exAx69FCa8lm9UBTJnkv5jRn8q_HrNW_wAW5kRwrp1jljAMjDKFsvV0IXPTTJUVfl-Er0tuGV6fFJRAwEk64gT7GKgO7OyV5LZsdbECuhvGmemNRyAUV_cZV-BbAV3ViVTwll6CX02Blk9UKgbMpGkZuk9mniBCtKCeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله دقایقی پیش اسرائیل
به شهر صور ۶ تن کشته شدند.
یادآوری : دولت‌های لبنان و اسرائیل  هفته پیش به یک آتش‌بس رسیده بودند
ولی ۳ پ با صدور یک بیانیه،
و حزب‌الله لبنان با صدور یک بیانیه
با این آتش‌بس مخالفت کردند!
جمهوری اسلامی میخواست آتش‌بس
در لبنان رو خودش اعمال کنه!
ولی نتونست!</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5498" target="_blank">📅 18:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5497">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=U_MskHLQ2fp4ivVgYFm18a3q6Tdl7EDAkpFnl_r4g8VvwUiH2sBjRixf5UpHv-1_11ixFhtzugCfUZoq0_mNZSKttHnR07bVPt1Nl9g_frm2AWkXVrxuEDSzwrbaVrNPjOZfgVlHv_VcKpuUO7mZsBIt3HLsIve7RTMw8BPpna5nxfQbwi0BMFWUUflBQLQpquNbWi6Yd20CKlIzh1FOE6R6nXsOQIUKuE7L65MFPRjgrN488aJX6WXxMXc5VaTBZ_Xs54a7PBRGg-gos6k4HdS4UAYZXrDrvCUfzkC_BJnimpu2qHacYXkipBEre2gPXFJNXQbVn0__Vz4wHxNlRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=U_MskHLQ2fp4ivVgYFm18a3q6Tdl7EDAkpFnl_r4g8VvwUiH2sBjRixf5UpHv-1_11ixFhtzugCfUZoq0_mNZSKttHnR07bVPt1Nl9g_frm2AWkXVrxuEDSzwrbaVrNPjOZfgVlHv_VcKpuUO7mZsBIt3HLsIve7RTMw8BPpna5nxfQbwi0BMFWUUflBQLQpquNbWi6Yd20CKlIzh1FOE6R6nXsOQIUKuE7L65MFPRjgrN488aJX6WXxMXc5VaTBZ_Xs54a7PBRGg-gos6k4HdS4UAYZXrDrvCUfzkC_BJnimpu2qHacYXkipBEre2gPXFJNXQbVn0__Vz4wHxNlRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ میگه جمهوری اسلامی
باید بلند و علنی و روشن بگه
ما «تسلیم شدیم، ما تسلیم شدیم» و «
آمریکا بزرگ‌ترین قدرت جهانه الحمدالله
»
باید روشن بگن که رسانه‌های
فیک نیوز همه بفهمن.
😂</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5497" target="_blank">📅 17:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5496">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‏سی‌ان‌ان:
برنامه‌های نظامی آمریکا برای تلاش جهت تصرف جزیره خارک ماه‌هاست که تدوین شده، اما به دلیل این که این عملیات بسیار پرریسک تلقی می‌شد، پیوسته به تعویق افتاده است. این خبر را یک مقام ارشد پنتاگون و دو مقام دولتی به سی‌ان‌ان گفتند.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5496" target="_blank">📅 17:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5495">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V2qnNcbjRtgJpmrkzzK7G3GpZArt_MMhDxx6nofOHfrQAkRZ6kTZhNFdUJUQCDWL8YQq_9g6c5D5jKds2hs9LY9KViiPu69_Ky7qQBBXnv4Usf3zVmf30jSlYbalZ-xqQtfE1gMyt9fVEfEqI-SDaXc32jL1-yyag5HVEe2gHxC5aIlUo22FQyHA9AhuJf1Q5S18D3nEdWjQsAfHqGlLUhXXgZ-loASww1IMZGtEZO_7JftC25i24dlFfsMiEeE65CbGqCqx5OFeFqJz89Y7yHlHYH0W5r33KcYGVSvSU4dyde4pj6c_HQ8wmruLL-465_TTtE4UFIFL2WPld9YRKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه داری آمریکا : خسارات وارده به متحدانمان را از حساب‌های جمهوری اسلامی جبران می‌کنیم.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5495" target="_blank">📅 17:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5494">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ترامپ دلخور از رسانه‌ها :)
‏ ترامپ در گفتگو با فاکس نیوز:
«‏ آنها دارند با ما مذاکره می‌کنند تا به توافق برسند. این کار برایشان سخت است چون آنها مغرور هستند. آنها بسیار مغرورند.
برجام جاده‌ای به سوی سلاح اتمی بود. راه من جاده‌ای به سوی بدون سلاح اتمی است. می‌گوید شما نمی‌توانید سلاح اتمی داشته باشید. بنابراین آنها یک روز با من بر سر این موضوع جنگیدند، و سپس با آن موافقت کردند: شما نمی‌توانید سلاح اتمی بسازید یا خریداری کنید. بنابراین ما همه چیز را به دست آوردیم، اما رسانه‌ها آنقدر دیوانه‌وار پوشش می‌دهند.
‏مهم نیست من چه کار کنم، رسانه‌ها خواهند گفت این یک پیروزی بزرگ برای ایران بوده است.»</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5494" target="_blank">📅 16:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5493">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tkZ7dx3b145R3l7x5g9wMpF69JpSddPuTP-lGkjFYhmnB46RuzfvvSmBnCSPzXS3b1UNWfrMYs2eOEB-d5LydSCE-V5nvppOLKEHwRCyAo-lnzy95diKsS1_ZFM7PS3xRamQpQRrqIxYz-ptIMUIFffI4OdX06QPBIBRdjWG7__9eh_fXOT2eVXgkY1ivLHb1TaBCio0trYv1dwcy4k-09cPnFZfwRtv-e4OAY3UR_mzy6RkPzA-BsgH1eve3vd94ycwiXahm5Cco9savRtJ18SPNc0fyH_8QPOsIM_61viRufm20yzq8mYJhAtateSyHfSG69v5vCiLShK8OgQ7oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از انفجار در سیریک
مناطقی که در دو شب گذشته مورد حمله آمریکا بودند در واقع حاشیه تنگه هرمز هستند.
جایی که رادارها و سایت‌های موشکی و پهپادی و…برای کنترل تنگه ، متمرکز شده‌اند.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5493" target="_blank">📅 16:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5492">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-Q_M914eHJzUCmcHRjWKPJupYcxkMMNma2V3Bq3p4TUGuf4EJ3bBAXqI5sfXX3ZFAZt3K95LNWgh1s0lQyQ6p4n_1wMudXWvzkwnYzj2yXmWmxDsZazw28l_nT5V5Xvz-uLqTKGVNDKpEmZ3Us_HUDWJYNDuhTeD1cpasXRCrVtcAkV1-aQKsLn7sl35IC2niQUe1qddq2i6przNjBeZYqYpAA5bRnAxUrhuYMxeBhA2D5WQ4mMBgbpDdOrgVgZ5Tj7P9jXNT1_l0ZgMjornZcf6dqf3xhqte8hVGkVHJiWRlxSlia65trEUhRWnvIVJD0NBMdbyl3_H3BfzHyPNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اموال ملت ایران! که یا مصادره میشن
یا مفت فروشی میشن به چین
یا غارت و دزدیده میشن !
بقیه‌اش رو هم‌ میدن «مداحان»
و «رجز خوانان»!!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5492" target="_blank">📅 16:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5491">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BWfQraLjI1tjV_AztbS8SOdBwO-hPS21Gs7NT6X15Eq2_0wSm3s1wRiVrxp6VBTOV9_ACsH4cxC0sti-hSqp3UMTfJCatA6e9QGTRugryvbNezr7ANlUcPp1VMLk8sK3bOfYYqpgxXeo7SKmY8zwH4N5wdXenBaeT7AA_3kO6ZLv7D8Aoj99QpY_iNQrqQ5i_DxbvjLrpkUnnhxizsDS1GNQC0iNVflJwa74MzVG20M58p8YxlDRq6cddmPnGQHM_rNyhXxfLRKM7G_CqeMP4mfZrjDv8AWf0TeC5TH9nG4coaBU1KBvOmXQzFzi6HODuUBsOSqB3Z12MNwsxBphqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5491" target="_blank">📅 16:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5490">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bo5d-SGxnIcMp53xowzGqh2TN3GXmSuUH8cLFgLUHB8bb_mcmCOnruDAfPkInfxKAYEyBpj_gOY9yH4C16jZs0d3buvp-vAWGGcupCeSDc9MiE1rTUEK_FqAqsIdjFjyHrwTR1hUUrRJoz9AhbybQcWGW26rxSwH9txJTfRElWsp5qoJbh5hBf-Iv2QArUeww6GCWOr3m_5Egaf0p4C82RWHvv_V_c_CvJ7WtMbkLNgJIr5NQBzQKu7u7YK0UmDgGbkyMgrN6dc2M3BeKpbalgB4Eyw3mXrIzhfsx1G06-VzFOt09FFF-alUtall5ozibb4m-FhkWRlAcPweuG5oag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5490" target="_blank">📅 16:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5489">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">بیانیه ارتش اردن : شب گذشته ۲۰ موشک شلیک شده از سوی جمهوری اسلامی را رهگیری و منهدم کردیم.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5489" target="_blank">📅 15:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5488">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">بعد کار به جنگ ۱۲ روزه کشیده شد در ۲۳ خرداد ۱۴۰۴ ، که دو روز دیگه میشه سالگرد شروع این جنگ.  اسرائیل، آنگونه که نتانیاهو بعدها گفت،  انتظار داشت که در اولین موج‌های حمله چندین جنگنده‌اش توسط پدافندهای بومی و….. ج‌ا سرنگون بشه اما نشد! اسرائیل حدود ۱۰۰۰ سورتی…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5488" target="_blank">📅 10:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5487">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_A29drBlZhXUXUyN68x9g63HJNIFrEWSqpZkmVxcoQtAOBXgnHLgYIK2wAD4hvsTlEID6VzWuF7k2jqWbz5PEOK2mOQSOYmT1OoleRTsKYl87JRK6OmYu9opI0YHrpEp7m4_gHBrgm1ShH2QTrdDyV9KF3nlQ87r-kShtAM8GxNi4FCz6NXFXQqUxjRjICDC8wbO3JMICNzN8CTuD21OYoH0Z_zx9nI0HcDjvK5aIPh2F2qlVlGGODhSesFNJugtcjwT9wihz4JvsT-put4Ux57BY-PMtOgrWFGFfhrcx3i8p-0nyR9NZQQ7Lav0LFDD5WEO_4Uod9uLGcrllJtmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پاسخ به حمله مستقیم جمهوری اسلامی  ۴ روز بعد اسرائیل حمله‌ای بسیار دقیق و هدفمند به ایران انجام داد.  گران‌بها‌ترین و مهم‌ترین سلاح دفاعی جمهوری اسلامی رو یعنی سامانه پدافند موشکی  اس ۳۰۰ رو که جمهوری اسلامی پس از حدود  ۲۰ سال تلاش و کشمکش از روسیه خریده…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5487" target="_blank">📅 10:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5486">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/163555b294.mp4?token=T4WOBOY91MMW19gUh5Qe58X5hXjim5fRUvf8Ev4P_E5lf98zL9bw-H956hhWeNcAHki4RjWdCkYvkHjogs2KCpzzcYkyUtQzqG-DBvAbjEZ3ZAoRdxuuGJ0dzfcIQiOD9dNuJzEWr0Dy2HF8vju2YcKNV7dOhhfVCI41OD4TsDko_i2q_iJJSvteOTYPP71RcXzzy1eFY9xTAErMNeu46n9C3ZH0AOrTVF__ZAHmJ4zXueOYtQ7TBnXDzd6mv_tRy1521BqC1Ru6Ulc3lshT3AOK_keXaSVzZcw-rKChK_nuHyAtYPYMz8JUVvk5thJOG_qkgeTjSEjYAatVr-5caA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/163555b294.mp4?token=T4WOBOY91MMW19gUh5Qe58X5hXjim5fRUvf8Ev4P_E5lf98zL9bw-H956hhWeNcAHki4RjWdCkYvkHjogs2KCpzzcYkyUtQzqG-DBvAbjEZ3ZAoRdxuuGJ0dzfcIQiOD9dNuJzEWr0Dy2HF8vju2YcKNV7dOhhfVCI41OD4TsDko_i2q_iJJSvteOTYPP71RcXzzy1eFY9xTAErMNeu46n9C3ZH0AOrTVF__ZAHmJ4zXueOYtQ7TBnXDzd6mv_tRy1521BqC1Ru6Ulc3lshT3AOK_keXaSVzZcw-rKChK_nuHyAtYPYMz8JUVvk5thJOG_qkgeTjSEjYAatVr-5caA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی از ۲۵ فروردین ۱۴۰۳  رویارویی با اسرائیل را از جنگ نیابتی به یک جنگ مستقیم تبدیل کرد.  در عملیات «وعده صادق ۱» ج‌ا با ۱۷۰ پهپاد، ۱۲۰ موشک بالستیک  و ۳۰ موشک کروز به اسرائیل حمله کرد،  دستور حمله مستقیما از سوی علی خامنه‌ای صادر شد، و جالب اینکه…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5486" target="_blank">📅 10:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5485">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oNfbyNW7M9vZ5GDA5XN7rn2dlo8_s0HeOtxqmvZxVYtf9mdDBXSRjWM8R9Hjva0GTzg6JWNrWjRrrIIvC64hYKRZdhnnG1jLRwaPEoYyu6qnu2i4CAOGvR1nuCMgk6U2SSat28tSJNePDOoPjYHmTVAWucXmLSZ9wOtBnanjke5lgVk4rbTNysiG_0O-2b72OkFDCnn729Wm0jU53CpUF-IYN6ljUY6UJajp1LZkGzIStQM5ISpWnK2-PZgjHJzkWVVBBFq4UuKwq36_JH3vPtRavHFZ1vgmlbIQFX47Hep1Ozw-IQQzg3W8iz7Bn9kgXFEoIAzYN-OdZj1fSudvvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ غیر مستقیم با اسرائیل سیاست  جمال عبدالناصر بود.  ناصر فشار سنگینی روی اردن و بعد لبنان آورد تا اجازه دهند، گروه‌های مسلح فلسطینی از مرزهای اردن و لبنان به اسرائیل حمله کنند.  اما مصر خودش چنین اجازه‌ای رو به فلسطینی‌ها نداد! نگذاشت مرزهاش با اسرائیل دچار…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5485" target="_blank">📅 10:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5484">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7AP5IBNdR9ZwCONLb0e8nWQTorEKmuBvjyDlRnIho4qK8UIuouLmBqkw7htTEO5VPXk3XIOZRiHJgOmef7zU_9AXNphJIqA3LXWnSC7DwI9ABI5RPcLN2k3Yz9xzRT7OjQ2XdqVzCPamWiGkS23jlA8LtQMWUgb3RQ7oOXFshlh7cWjrxJ3WzlGARXMdujzgPg6jFQCGW2_fyvdAXB6CLMjC9r73JgJnoJ5bu2cziVKyZnqBSh2v_Uf_dJ-ZyGuzKDb1lUpPVLjUN1IcpTktGKewK8CvwnbtZuzX2pSFp6ZaImA4yT8Dq199AjUJaiDCnqWpxF8mxvsZ4eCxAeirw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی در ۲۵ فروردین ۱۴۰۳  برای اولین بار رویارویی با اسرائیل را از یک جنگ و نبرد ده‌ها ساله «نیابتی»  به یک جنگ مستقیم کشوند.  تا قبل از این تاریخ،  جمهوری اسلامی با مسلح کردن گروه‌های تروریستی مثل حماس، جنبش اسلامی، حزب‌الله، حوثی‌ها و….. با اسرائیل…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5484" target="_blank">📅 10:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5483">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Go5glEM7eQR6Nf84WBSdBCY9J8cDDJ2Kx6p-lFlcgV1qb5-eMqWxbTh2qasLVcSPUTTxgWvq0XrKbzRkgvFiGsihVyjnySKrELncW0GINCNdDPyHZVfMKArkz-0LJXUAY1IBQO1VISrCKzZmQEzovk7w2GyIU1gBgJ6SdE0Tm080QWvFarVUrpnUR0sirPN6f8SvBgaOjOkCQ6Rscbrzuz4QksoqnfB2-KHgDTp6MSO2dZf4Ui4XvZjgx7UEAjWkzRxLm_gAnSOmkPEv46Ll14qRGTuYGn7y2fHdGCd0aX0nlGwRVCeX-GbdC3200fr2wQ3U53CkaFK0F3aACoo3GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از مهم‌ترین پیش‌شرط‌های جمهوری اسلامی در دوره جنگ ۴۰ روزه این بود  که «جنگ باید کامل تموم بشه»  و آمریکا باید تعهد بده که دیگه به ایران حمله نکنه.  منظورش این بود که یک «آتش‌بس» نمیخوایم! «توقف کامل جنگ رو میخوایم»!  این‌ درخواست از اونجایی میاد  که جمهوری…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5483" target="_blank">📅 10:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5482">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">یکی از مهم‌ترین پیش‌شرط‌های جمهوری اسلامی در دوره جنگ ۴۰ روزه این بود
که «جنگ باید کامل تموم بشه»
و آمریکا باید تعهد بده که دیگه به ایران
حمله نکنه.  منظورش این بود که یک «آتش‌بس» نمیخوایم! «توقف کامل جنگ رو میخوایم»!
این‌ درخواست از اونجایی میاد
که جمهوری اسلامی کاملا فهمیده
که وارد دوره‌ای از جنگ‌های بی‌پایان
و گاه به گاه شده که به سادگی
دامن جمهوری اسلامی رو رها نخواهد کرد!
بگذریم که هیچ رئیس جمهوری در آمریکا نمی‌تونه وارد تعهدی بشه که رئیس‌جمهور بعدی ملزم به اجرای اون باشه!</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5482" target="_blank">📅 09:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5481">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
حمله به کنگان
ظاهرا کل سواحل جنوب رو دارند میزنن.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5481" target="_blank">📅 01:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5480">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">گزارش‌هایی از حمله به تاسیسات پتروشیمی  در عسلویه</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/5480" target="_blank">📅 01:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5479">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
گزارشی از حملات شدید به قشم</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/5479" target="_blank">📅 01:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5478">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
شنیده شدن صدای دو انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5478" target="_blank">📅 01:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5477">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🚨
مقامات آمریکایی آغاز حملات
نظامی را رسما اعلام کردند!</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/5477" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5476">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
ظاهرا جمهوری اسلامی از آذربایجان شرقی موشک شلیک کرده
هنوز مشخص نیست به کجا و…</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/5476" target="_blank">📅 01:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5475">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
خبرگزاری فارس شنیده شدن صدای انفجار در میناب و سیریک را تایید کرد.</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/5475" target="_blank">📅 01:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5474">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در سیریک</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/5474" target="_blank">📅 00:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5473">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
خبرگزاری مهر : فعالیت پدافند هوایی در غرب تهران</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/5473" target="_blank">📅 00:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5472">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ihSh4kD_7vyBYux3eMLB4iVCppjR3PFwBlSUdnYJqukO0YWRPSe_mEtTUJbG5BJl6zVIm9iiYEstqw8RhgYP6WXRAUApHlHDldDOAcnrX55E18Y8cD4GlM9PW8JibRp6x7Zz7o9DPi2Djrf998mMF6UDUbzBdBM9prHj1wISUfevlE5kjhBg9LxBjhsnlI6ufEq1EuI6rDNY_OuOsNNpmgLl0YDcCglwR2RiKmHqZjF9CGVt-m8XpwVh1cCj_UOtuApZLV3lWAYuYhTj7IbUNphFPeGSVhXWT8y0EBDaqRVdNWdY-mF615DHskcJ_OgBnKDYNRlpIgbCxIhbIQR5jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
هگزت - وزیر جنگ آمریکا:
امشب به سختی به جمهوری اسلامی
ضربه خواهیم زد.
فرصت عالی برای توافق داشتند، نخواستند، امشب «بوم، بوم، بوم»
بمبارانشان خواهیم کرد.
این به معنای  از سرگیری جنگ نیست
فقط برای فشار برای رسیدن به توافق  است.</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/farahmand_alipour/5472" target="_blank">📅 00:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5471">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
ترامپ  در جلسه‌ای با مقامات ارشد نظامی
- امنیتی آمریکا در «اتاق وضعیت» در حال بررسی  یک اقدام نظامی «گسترده» «اما کوتاه مدت» برای ضربه زدن به جمهوری اسلامی است تا سران ج‌ا را وادار به تغییر مواضع خود
در مذاکرات کند.
🔺
ترامپ همچنین ساعتی پیش به خبرنگاران گفته بود که امروز ضربه سختی به آنها خواهم زد.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/5471" target="_blank">📅 00:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5470">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران در مذاکره زیادی تعلل کرد و حالا باید بهایش را بپردازد.</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/5470" target="_blank">📅 15:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5469">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران در مذاکره زیادی تعلل کرد و حالا باید بهایش را بپردازد.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5469" target="_blank">📅 15:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5468">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d07d6979a.mp4?token=gSOqs6PtEbEPTdBMPPHDAItqmVfrsCLih-s3PvaoFc6aLXQeJXQTztjHbDqxhAJH1MMpPc1A9yvcwbuWyPywvnURDFsL0uBJoraeBTIOgzLoQXDn-pg8lIxjIxF1a_-Ev_ZaJa3ckXJUZ5A7OgqWds_iawrl--hNySCH3MBLoLdfDlcd8dNQtb9gt4ts_ySjK1gIR-C65Ys0-v4xXBcyQhFgek4xKEngTei-0IcTvy9guVJmgPpo_rN2jJhUqzcE7MoxVDMrAa8ONe4qWUOJu05AMLvvBxDH0tTaV_-MR0urh308kEh_OsF0rhhX4MmpnQZAF5j3rfT0MRkK2aLl2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d07d6979a.mp4?token=gSOqs6PtEbEPTdBMPPHDAItqmVfrsCLih-s3PvaoFc6aLXQeJXQTztjHbDqxhAJH1MMpPc1A9yvcwbuWyPywvnURDFsL0uBJoraeBTIOgzLoQXDn-pg8lIxjIxF1a_-Ev_ZaJa3ckXJUZ5A7OgqWds_iawrl--hNySCH3MBLoLdfDlcd8dNQtb9gt4ts_ySjK1gIR-C65Ys0-v4xXBcyQhFgek4xKEngTei-0IcTvy9guVJmgPpo_rN2jJhUqzcE7MoxVDMrAa8ONe4qWUOJu05AMLvvBxDH0tTaV_-MR0urh308kEh_OsF0rhhX4MmpnQZAF5j3rfT0MRkK2aLl2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله هدفمند به یک خودرو در شهر صیدون لبنان
برخی رسانه‌ها نوشته‌اند که یکی از اعضای بلندپایه حزب الله در این خودرو بوده
هنوز جزئیات بیشتری منتشر نشده</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5468" target="_blank">📅 15:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5467">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nswsHaeAOyW1eTwnIaOq0b5GKtVEKLCUOcId2rJRAmEdKGSYM1zPH5E3wGgpJBsxQS7i-CGRC4p63U2H2ojh-VjGdJ7W39eusDD3A_Z1LzpBwn3irpmwz9r_uNe86tofARXLe7-6Fn_NhTNkqObHsl2ljTEeIHnT9xWjRWcXYmPG6tH_awt-rLaJ5_ogryTD_qbjk3tr4_xwpIuEQ0C9HzhxDXFYnokzuyJpLtXs8mrg_j4KeErAP4ZiTGcugLzclVqWxdnWBDwd6HauArrGexc_yFlZad_VfL-ujmAUmmuBi6EphnlQNIChC8qQLRxpRFIkADecsx4IKyP-LYzvVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیا دولت لبنان، پارلمان لبنان، ارتش لبنان، از جمهوری اسلامی کمک خواسته بودن؟ چنین جنگی رو خواسته بودن؟ نه!
آیا این جنگ به خاطر لبنان و منافع لبنان شروع شده بود؟!
نه به خاطر کشته شدن خامنه‌ای!
آیا سلاح حزب‌اله قادره که جلوی ارتش اسرائیل مقاومت کنه؟
نه! یک چهارم خاک لبنان رو سریع دو دستی تقدیم کردید!
آیا جمهوری اسلامی از مسیر دیپلماسی و از طریق ساعت شنی باقر
⏳
می‌تونه آتش‌بس بیاره برای لبنان؟
نه! نتونستید!
آیا جمهوری اسلامی با موشک‌هاش،
می‌تونه آتش‌بس بیاره در لبنان؟
نه! نتونستید!
پس چرا جنگ راه می‌اندازید و کشورهای دیگه رو‌ هم‌ مثل ایران به بدبختی می‌کشونید؟</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5467" target="_blank">📅 13:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5466">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PQvhAZCzDRkBfJmsIvJjk0BeSBC20RTgKMZ32qJWEjgIej7ke3BtYbSQcOPbfraWwSqj2TwKinrzMBJ8xPpFuLtfauegvBqSSMaryHZ24oLlWZotNB93TpGiGHO1O8PpCylKE2PAGBPXzAXXU2qbjMNuZo9yzpG7-Z-WyBzdKBBqgyl9sInJc_8Q4mV8wYBDF4K0lg-fogR-9eKF1-x0feXP1qiKGPCU-dlXx6K4hcVS7cyii-bXU3XYXp1yK-i-IwNvLEvNODtHR-tdC8GcOC4t8TPcGispkXGYrrGckadHJry2gBpUvwiHuGeAkWyd7JlQtgFS7Ufd4rEL6C7tFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از زمان شروع جنگ گروه تروریستی
حرب‌الله علیه اسرائیل در خونخواهی
و انتقام کشته شدن علی خامنه‌ای،
تا دیروز عصر ۳۶۶۶ لبنانی
جان خود را از دست داده‌اند!
جمهوری اسلامی زیر فشار گسترده
دولت و مردم لبنان است،
دولت لبنان سفیر ج‌ا را از خاک خود اخراج کرده (گرچه سفیر در داخل سفارتخانه مونده و گفته نمیرم) و هرگونه فعالیت ۳ پ رو ممنوع کرده، مردم لبنان
هم این جنگ رو از چشم جمهوری اسلامی،
با پول و سلاح جمهوری اسلامی
و برای منافع جمهوری اسلامی می‌بینند.
جمهوری اسلامی اما قادر نیست آتش‌بسی
در منطقه ایجاد کند و حزب‌الله لبنان نیز چند روز پیش آتش‌بس میان دولت لبنان و اسرائیل را رد کرده بود.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5466" target="_blank">📅 12:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5465">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">گزارش خبرگزاری آسوشیتدپرس از فرار گسترده مردم شهر «صور» از جنوب لبنان پس از هشدار اسرائیل.
🔺
هشدار اسرائیل یک روز پس از حملات موشکی جمهوری اسلامی به اسرائیل صادر شد.
🔺
اسرائیل صبح امروز هم به صور حمله کرد و ۷ تن در این حملات کشته شدند.
🔺
۹۰٪ جمعیت شهر صور…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5465" target="_blank">📅 12:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5464">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">گزارش خبرگزاری آسوشیتدپرس از فرار گسترده مردم شهر «صور» از جنوب لبنان پس از هشدار اسرائیل.
🔺
هشدار اسرائیل یک روز پس از حملات
موشکی جمهوری اسلامی به اسرائیل صادر شد.
🔺
اسرائیل صبح امروز هم به صور حمله کرد و ۷ تن در این حملات کشته شدند.
🔺
۹۰٪ جمعیت شهر صور شیعه هستند
و عمدتا به سمت شهرهای شمالی‌تر
چون صیدا و بیروت می‌روند.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5464" target="_blank">📅 12:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5463">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/stlbO22_AIcS5v8jFYxbY0p3JipcZyFIXJvGKkMzXrppGWKSJZYTRJCv5xsBCRnZL37Dr0PvVZEK6KZqb90ahcHD2f5hoL36ylcRybf8yjLGsddoEBAaCefTRNVhIxvkcHiuDCgnnQQGfLVSwhQOIbQmTKW5pH0C5Yh0paiPiYqBaQjOPphwj7TEhr0Xny297oNn8fI3MKh6EMbckzIWSdB9e8F15zq3qVN4H5tLszw2xTjrci2JI4VYY8vZ-hNQhTtVLB9P1aQ30F7bfY_IwMRWxr65ecpMOk2l28Rfc6dJQtzBCZYvi0ikQ1MqJN4wOEdtbm-ey4-ml1EIrXCnEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل به دو روستای شیعه‌نشین
غسانیه و حومین الفوقا در جنوب لبنان
هشدار تخلیه فوری داده ، اینکه اطمینان داشته باشن
حداقل هزار متر از روستا فاصله دارند.
این دو منطقه در مجموع حدود ۴ هزار نفر جمعیت دارند.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5463" target="_blank">📅 12:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5462">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lhr86-qIXQzASqopBJ4liJ1xmU8OZrrOlO5LwGJVj5GmyrRkrquV7BjxYI-SW8ljDzUW__iOgQwdZD4yuOLPZkPgKUnXiIuH-sXz5QWGMvdapE88hDWkuU5ALAt5gygX8G3--vMwnIpL4_8fLtiPCRi8bPM7r8o8P8DGLrSNOyW7V_gIpKXHi0SBO5zjrAzPz9r0fj_LftWGiS_budmMldou2jUBYjEiUTKSAWb2VYf27STzltm3k-3KFYLjVLDr8EW8zk4LjnWNrvY_SVXpueR1S8kX8Pb3bzg2IDQ1O2qcJ94Qg-LVpm6DRhS_8iVBnDwQsIYu4eCg4CR92twXhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب! چه نکته جالبی بود
واقعا چرا آمریکا خطوط قرمز شما رو رعایت نمیکنه ! غرامت و تعهد هم که نمیده!
اسرائیل هم که معادله‌ای که در لبنان اجرا کردید و براش یک پتروشیمی در ماهشهر رو هم فدا کردید‌، که براش تره خورد نکرد.
عجب آدم‌هایی هستن!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5462" target="_blank">📅 11:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5461">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTHExBqK8jQpjo98B9FgPCv43GjMwXmtgfPGEDXZPHVHbbDbYoVVHpSLpAO-YDkRFXDWNYM8nRVne6Mfs-qFnMKpnPcrjTMEo_ZWmvZUaVqiRs3E0KayzeUWp9CTTwzu8iMo96b9nNa1L90eHYRVGhrLp0g-SWTlmUfjuEJquxh0D2eRWHZs6GH38D6VUUjoND0mCHu6Mb-ntpD-zD4eqon4HtFKTqukOkdT3aR15Jla0P1dSzOPz4FRhHYyveK3aQq370-ygspY0ZO0ZFGjAVwnoNdUQl7fAozxKihPoe3RiMOBRrGJpXXOcRE1eQIQf2F1Iwyxv5tqkcMOMe5RAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خبر فیک به نقل از یک اکانت دست چندم، که اینجا نوشتن رسانه تا بهش اعتبار
و اهمیت بدن رو هم از دیروز
منتشر کردن برای اینکه بگن
چرا دیگه  به امارات حمله نمی‌کنیم!
چرا فقط کویت و بحرین رو میزنیم
و چی شد یهو امارات رو رها کردیم !</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5461" target="_blank">📅 10:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5460">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">توییت ابراهیم رضایی سخنگوی کمیسیون امنیت ملی و سیاست خارجه مجلس ساعتی پیش از شروع حملات آمریکا  به جنوب ایران</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5460" target="_blank">📅 09:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5459">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rq5aE8qrEALTgBEYRzmyzCTwCTorWkCCpWOrIVZ8NCbi-EwLbwtGcxKbqgX3nnAmCJ2u6AxfconQAl-uOZ0jV-dohCSfpnlTJn7gW2oZC2K5AZ7WB6LDEYZn5hewr8xe4ZRtsx1xvgd2sAVu53hcfNQcO_Q0glfn-c09KW0tIv0ts6ffn4WWQPaUBvmG7oSxN75SFtAWjLmzrvaI817kUWFKJVKAetZt_a1N5dVPnfM99SDRJ8lwiS-YCXh4H9-loK8yhOetyZMMU5T-qQyIgOLar7r-i-vj32V0y-IMkB8TsjgRFuwW5aAPpFXUWPTC27X6BPr9-MQB4gHkNgXA8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات گسترده امروز صبح
ارتش اسرائیل به جنوب لبنان،
مقامات جمهوری اسلامی پس از حمله موشکی به اسرائیل مدعی شدند که «معادله‌ای تازه» ایجاد کرده‌اند که اگر اسرائیل به بیروت و یا جنوب لبنان حمله کند، به اسرائیل حمله خواهد کرد.
اسرائیل اما از دیروز بر حجم حملات خود افزوده و ادعای جمهوری اسلامی را به چالش کشیده.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5459" target="_blank">📅 09:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5458">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
جمهوری اسلامی در واکنش به حملات شب گذشته آمریکا، به بحرین، کویت و اردن حملات موشکی و پهپادی انجام داد.
اردن گفته تمام ۵ موشک جمهوری اسلامی رهگیری و ساقط شدند.
کویت و بحرین هم گفتند که اغلب حملات رو خنثی کرده‌اند.
منتظر خبرهای بیشتری می‌مونیم.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5458" target="_blank">📅 08:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5457">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VVbIPGeNX89AZ3RiGTJHhv6r0ZFyH_I6Gt8q9t-QqCdi1NQb_ICLQmxY9Pv91BFqWV0poVx7B5GUvo7VvYyhf63Rl0UwbKZVrFWtAU_WqLFw-WUYdD9-7RLRu8WB1GpZCWvLTb_nGhB4_CgvE_jqWIrg4Rmf7NM9oMF7ZqnsqHC7fVVPx60edl9oD3PKUQHH7zdOCtk5LRs-P_VdpEGTXkAjTtKFh9-GediRm2JkY0tRuNlCbFKppv5ibz8RxNky_PnwCvspGwx_oeZM8utwyelIwr-6wcpy6imcSugyTqXVwLDO4ozhKbGVE1Ub8Fxm7wiFCMV0rLV6WETROcHcIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخراج رضا دالمن از دانشگاه شریف به دلیل آویختن عروسک موش
او پیشتر به مدت یک ماه بازداشت شده بود.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5457" target="_blank">📅 08:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5456">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQgh7y6ZO7Gyu4vXmLsowll_ulUpaqnxGGYaPfJkSAYmNygu2nKOsI9XOFfTpni-PJQH1wfzcwloXkWRVx_nl6RCCFD-lPl8XtlN-vd58SStoTEM60ci2XneV2bZRxHuSb_F63_dsxUgbR1kNjeMKyz-LFvT4-EuRoSThjJiAQgvjSIZcGMYVektxpU-YgUpEim-z8PUD-xpCPLw2qkj2dUjw9fhp7dFQBqcjLRgj-FvceT1ZoHw4DtucSHcVsCO2YSpoDnsSPtkYQ_fjooTkNHuT61M1RJteU9bHHuOMfHulaVSLLFDrbwJKJzTqbu_jDMIEhfHNXhKinoRm_Ox6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ابراهیم رضایی سخنگوی کمیسیون امنیت ملی و سیاست خارجه مجلس
ساعتی پیش از شروع حملات آمریکا
به جنوب ایران</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5456" target="_blank">📅 08:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5455">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته ارتش آمریکا، در پاسخ به حمله به یک هلی‌کوپتر آپاچی خود، مجموعه‌ای از حملات هدفمند را علیه ۲۰ هدف نظامی در داخل ایران انجام داد.
تمرکز اصلی این حملات دکل‌های راداری و تاسیسات ردیابی و نظارتی بود.
ارتش آمریکا با نیروی هوایی و دریایی خود با این اهداف حمله کرد:
بندرعباس
: دفاع هوایی، رادارها و تاسیسات نظامی
جزیره قشم
پایگاه‌های نظامی، ایستگاه‌های کنترل زمینی، رادارهای نظارت و باتری‌های موشکی.
سریک
: پایگاه‌های دریایی و تأسیسات مرتبط.
جاسک:
پایگاه‌های دریایی و نظامی.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5455" target="_blank">📅 08:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5454">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‏
🚨
صداوسیما:
دو نقطه در جاسک و کوه مبارکه مورد اصابت پرتابه دشمن قرار گرفته است.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5454" target="_blank">📅 01:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5453">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🚨
سنتکام از انجام حملاتی در پاسخ به سرنگونی هلی‌کوپتر آمریکایی خبر داده است.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5453" target="_blank">📅 00:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5452">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
جمهوری اسلامی با چند موشک به اقلیم کردستان عراق حمله کرد.</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/5452" target="_blank">📅 22:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5451">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">عراقچی : تنگه هرمز «آبهای بین‌المللی» نیست.
پاسخ هر تهدیدی را خواهیم داد.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/5451" target="_blank">📅 22:34 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5450">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">نتانیاهو: ممکن است مجبور شویم بدون پشتیبانی آمریکا با ایران مقابله کنیم
پس از تماس تلفنی ترامپ برای توقف حملات اسرائیل در پاسخ به حملات موشکی ج‌ا، نتانیاهو به وزیران کابینه خود چنین هشداری داد:
«ممکن است به وضعیتی برسیم که مجبور شویم به تنهایی و بدون پشتیبانی آمریکا با ایرانی‌ها مقابله کنیم، با تمام هزینه‌هایی که این موضوع به همراه دارد، کمبود مهمات و انزوای بین‌المللی. نمی‌خواهیم به آن نقطه برسیم، اما می‌دانیم که ممکن است برسیم.»</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5450" target="_blank">📅 21:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5449">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wfk0RgnnH6b-L_aYCN1m-GMnJMevfEjLMWxYYcMazAUCsyCr4IkRPW-iwb2tGi9Qfa3Rtoqq65rDLdKoDvop5EF2AD322MnqzfVscqr4NKOrpDBVn9eB3IEtZpv8BwOtbN1aXWe2JIXPhmuGUxaTbfLI0TcTwCVcjbQSXj4STuxBuaFhI6_YLEtfZEve-wzCD2YQ5J51_-NdncBTLL0Y-p00D_6ky3ThFAp6hhiE8izzlHsGfURxtS_0xGiqKAC3dPy0szhXeT7pl8_WN6jA54Mjzs3OTqEmbqV0AAEJQad5naBBv8fIvfyxFWZeX6syfG5kR5BuFoIwWFirg7LZig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/5449" target="_blank">📅 20:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5448">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0arLae5RZFoLMy2GUkBXZOF4ojpuOVc1uSYJS2wcSj4B1P8HAe6l3NVGG8BpQ0bDctLUPYEyqbllJdqPt_wMWX4Zx0ItPXsxHIaFtGBaOCcboV04Vggp-sOM9rqyHfvWRUkcbR2zBxM7HE_cUvHw2613bIKspnX6F35H1B1TQ_SxRvR_DDJNdAezCxU0fvqwKbBVcs11CsWAojrsA1EdEX6dQCiZ9yDd2R8x0l8UK-SVrgWILGnBAfs59xo_tnL5JxGpeT2KOTzsdUujWAy38QmRrBUEshYTpIFYMyaHBo6ePd1oevIK443WqMk8baPOblJCp667kHRsyiyzIj5Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : جمهوری اسلامی شب گذشته یک هلی‌کوپتر آپاچی آمریکایی را بر فراز تنگه هرمز سرنگون کرده. هر دو خلبان سالم هستند.
ایالات متحده ناگریز است به این‌ حمله پاسخ دهد.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5448" target="_blank">📅 20:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5447">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">می‌ترسم اینقدر اسرائیل لبنان رو بزنه
که جمهوری اسلامی مجبور بشه
دوباره اینترنت مردم ایران رو قطع کنه!</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5447" target="_blank">📅 17:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5446">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">زن شیعه لبنانی : کشته شدن خامنه‌ای به ما چه …    زینب زنی در جنوب لبنان :  «نمی‌دونم چرا برای کشته شدن خامنه‌ای  رهبر یک کشور دیگه، ما باید وارد جنگ میشدیم  و متحمل این حجم از خسارات میشدیم.  چرا ما لبنانی‌ها باید هزینه کشته شدن خامنه‌ای رو بدیم که اصلا لبنانی…</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5446" target="_blank">📅 16:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5445">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4718cad225.mp4?token=p9C1b7t0yiPhXLxzU7txtjn05bY-iyzYwG6awzc5OTqiTUK8eUCuYdMBlwsPQjdlPTCbFdgLuh1xmt8iPWegoRIdD0aXl5P5HWEk0GfIx4gJqtapV5QlsUUBFa0f2nfaFxbIr4dxZdaAW_40KdwM4w96XG_hvYprgpD1sm_YIWNcMfYEcoU9CBSWUwq2guHAKewZ0E4AIOg5Twm19CxiT9GcGQekl4P3-XrXlkbLpnlyH1uFcRS9q4lmKcWojJPPoqvtqB_QINXSK8CCpGFxx7DoDiPOWCZHWQPqZg7v6dWTKwDfFrEdFuVleOdjyUJ7Jesi1r4ZD9PQ8uvClM0flQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4718cad225.mp4?token=p9C1b7t0yiPhXLxzU7txtjn05bY-iyzYwG6awzc5OTqiTUK8eUCuYdMBlwsPQjdlPTCbFdgLuh1xmt8iPWegoRIdD0aXl5P5HWEk0GfIx4gJqtapV5QlsUUBFa0f2nfaFxbIr4dxZdaAW_40KdwM4w96XG_hvYprgpD1sm_YIWNcMfYEcoU9CBSWUwq2guHAKewZ0E4AIOg5Twm19CxiT9GcGQekl4P3-XrXlkbLpnlyH1uFcRS9q4lmKcWojJPPoqvtqB_QINXSK8CCpGFxx7DoDiPOWCZHWQPqZg7v6dWTKwDfFrEdFuVleOdjyUJ7Jesi1r4ZD9PQ8uvClM0flQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محله الکریت - صور - جنوب لبنان</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5445" target="_blank">📅 15:26 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5444">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUSzAZHbYbmIY3r9SMMCw-7ZVg2A3rorHljoI_OJjG6gNHqnfoySbsyGMJvAQ-zEGK0ii554t_aYFv1rPviWoTg0lRZ3wD440r4ZB1h84otZn-LAhHqxvTuRBOTqNBP-GXJy4lql510uQcoQT5MrVjxPqt8eU-PerTUCXvgpgApL62zVSOENLF0Mx8xMLwbaygTJ6dDYgIm24vowOJJX_qSsLx-LTx0lZoHCz-r9ypN6tlsg9zICtY87qdVn_W8KdMviorPMgRUFcsRmo_cMXprIzjyV7pwPeX3HF0T-rmefkEmkCSIjXVQXViHX2OefazpbmEzutb_ScO5zpTHFPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ارتش اسرائیل از ساکنان شهر صور
در جنوب  لبنان خواسته است تا
فوراً این شهر عمدتا شیعه‌نشین را تخلیه کنند؛
شهری با جمعیتی حدود ۱۷۵ هزار نفر.
🔺
این هشدار شامل محله مسیحی‌نشین
صور نیز شده است؛
محله‌ای با حدود ۷ هزار نفر جمعیت.
برخی رسانه‌های اسرائیلی می‌گویند
که شماری از اعضا و فرماندهان حزب‌الله در مناطق مسیحی‌نشین پناه گرفته‌اند.
🔺
در اطراف صور چند اردوگاه فلسطینی
نیز وجود دارد با جمعیت حدود ۶۰ هزار فلسطینی! آنها هم دستور تخلیه گرفته‌اند.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5444" target="_blank">📅 14:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5443">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJeAyxWOGeXz6qHCcd5gFZKRWL1i_ZD-hZJzfAblFLboXzpqt0lC1JfeTaCE5AJRK7fkXosZkeR0PRLoALo6_eziNnlHITxLyB-PtNwYyDPDodcqGEl4DAJSy4dotVToyw3SQBAes-wYuZAPogyQduFqkryyIN9UoIEr2sGudhE6GgUGrTUB6HToVcUz2teRpQhypiyg53Ug_imRWIlmAAa6b4ap_lw4FM_Y0uuaQzdLJscctq1SnSurMLq-jtkWl-Mng6owBIkCFJ-f2HiMYtVKXFmIhly4dkE9RIA8XjwVbEDoIpRuRUGp3bXtjUypqpsf4k4W7moeHVVQzam0Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
در حملات دیروز اسرائیل دو عضو
پدافندهوایی ارتش کشته شدند،
اسرائیل گفته بود که به  علاوه بر حمله به مجتمع پتروشیمی ماهشهر به پدافند هوایی نیز
در چند استان حمله کرده.
درگیری اخیر در دفاع از گروه حزب‌الله لبنان صورت گرفت! جمهوری اسلامی با حمله به اسرائیل میخواست مانع از حملات اسرائیل به لبنان شود که عملا در این زمینه ناکام ماند و منجر به حملات اسرائیل به ایران شد.
شهدای دفاع از ضاحیه و جنوب لبنان!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5443" target="_blank">📅 14:08 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5442">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea21582d5d.mp4?token=RKwwyFerYVHv9dW1WxoOVEZNd7DvNQBQVgUCfd0ZRRs_GKIvtozLMXzO3vH0lIJG4toujLW3duqZ2TqPnvSXXEif2GYc4UU15tYpR45xKcoRTOfCCgh4DJ_7I4LiHATM86VDoIjuqK3HrIT0u8EbPOj7GVSBT2TnMata0UXt5QDKugXM3z_NRW6qtfMCuywPuMW6YJJ28VP7Jv1O5luGU1oKPeIMrnTuSXc4TNkbGNvV458YMAmJHq0Gc72MugvIAwTFbe-KeGAiE0uTYHQgPQWEMAB58xXPC1EfiOEToTIuzBKLDUBOUwWSLKicNQ_v7WKkhkenrE2pGV4KrLvo3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea21582d5d.mp4?token=RKwwyFerYVHv9dW1WxoOVEZNd7DvNQBQVgUCfd0ZRRs_GKIvtozLMXzO3vH0lIJG4toujLW3duqZ2TqPnvSXXEif2GYc4UU15tYpR45xKcoRTOfCCgh4DJ_7I4LiHATM86VDoIjuqK3HrIT0u8EbPOj7GVSBT2TnMata0UXt5QDKugXM3z_NRW6qtfMCuywPuMW6YJJ28VP7Jv1O5luGU1oKPeIMrnTuSXc4TNkbGNvV458YMAmJHq0Gc72MugvIAwTFbe-KeGAiE0uTYHQgPQWEMAB58xXPC1EfiOEToTIuzBKLDUBOUwWSLKicNQ_v7WKkhkenrE2pGV4KrLvo3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏جنوب لبنان - امروز
‏حملات جدید اسرائیل به شهرهای نبطیه، حداده، الرمادیه و دیر قانون راس العین.
‏بخش زیادی از این‌ کوبیدن‌ها در جنوب لبنان، در واقع پیام به باقر در تهرانه!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5442" target="_blank">📅 12:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5439">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mPQdKMGepqSipe2oTW3XrAh-HZbPtPCuCa5wNmqA52XSr573k999rQ--Pk1s-yFwmaP0TKOAHTnBM_B4Jc1STdrwoRr-MKYYnh-Cj8b7lO7q5U6aiV1O4T47MczWggs2OE-mqqQJSUnnKbH6EGMnbN77nah7GnvaPr7f7WkaYDDR3z9VfcCkwDXjw0LhZIZiLCHYxwAKLLs7o-MVESF36ER4vgEOvjVfVKmZeG39SQSQ-O77_jmUXQJ-pIJsYEfBsSSm051vpaKOJ3-AVCDJ4GjgEINJqG0fDiz7CyQ5CP-7Kj6Z7ZypZSMkAQJAxSIq5-olmJGBUjL4qsm3-Ox8tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aDmVfuBAM3FwrhXOfoQzWCJdOue8E5tqZxBdF_Yy3-fTBmmFe16ekfwSw_6cJI6zggde_L-8xeQJXKYgE36oY-RVMxMdViEvb3hlMwziQTdgghxUv4ogtP4z9bo74qwM__REfbdAUc-7kzS3JlIJE_VrdZv6lG0LiZNawuqJHrmHte7zM2Snz6u8SBH7mI830zvxdZdDpHqDW-WfsEHGc8L0W6YFCCioC_LveFcz-wQ8if8tviy0Q23cUPIuPfoZvYDEUsE-9WRhlKHNDB_xex9eNS76ObeN29Lc-IAhHaSwqCvvss9y7rHHFC0sdy0e406d4RgAmbiuJUIbYWoq4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874c401e95.mp4?token=FB3T86sHfOjPtZ8HQm0ukyFnQDssOlQ4hX19inYndTcHXnbNwXTCbLa2CLgTG2_c9TDGkoU2P1RW6edYi-L2PG5xR9r-6bPIJZjLsNtPEN-pzzuheaOhWZKy5fBwppPOa1eYSpjTmh0qB_KLFAselchU3eOxtuufXwHHn65K-9zaHngyXQqFI2slWl_9fmKoVg6sx4yRu5fisZWQmKnKz7f9HPl7YfIjzYF3pMEWImrcOL_wh7-tkvvU0iv9ZTlDZo_OujCc2q1CUkvTa_6q9OsVcgwk_-9S6E14Cqef-oOTlfQ2lofFsObyMmfaoYZH4AYzfvVmDD7v8Op4TFZ5CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874c401e95.mp4?token=FB3T86sHfOjPtZ8HQm0ukyFnQDssOlQ4hX19inYndTcHXnbNwXTCbLa2CLgTG2_c9TDGkoU2P1RW6edYi-L2PG5xR9r-6bPIJZjLsNtPEN-pzzuheaOhWZKy5fBwppPOa1eYSpjTmh0qB_KLFAselchU3eOxtuufXwHHn65K-9zaHngyXQqFI2slWl_9fmKoVg6sx4yRu5fisZWQmKnKz7f9HPl7YfIjzYF3pMEWImrcOL_wh7-tkvvU0iv9ZTlDZo_OujCc2q1CUkvTa_6q9OsVcgwk_-9S6E14Cqef-oOTlfQ2lofFsObyMmfaoYZH4AYzfvVmDD7v8Op4TFZ5CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله شدید امروز اسرائیل
به شهر صور در جنوب لبنان،
اسرائیل همچنین امروز
ساختمان پلیس دریایی گروه
تروریستی حماس  در غزه را نابود کرد.
جمهوری اسلامی جنگ را به پایان رسانده بود
با این شرط که اسرائیل نه به بیروت
(ضاحیه) و نه به جنوب لبنان، حمله‌ای صورت ندهد!
ویدئو : حمله به پلیس دریایی حماس</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5439" target="_blank">📅 12:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5436">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oV_VXQANMdE2YLlIRhH-pXZdxK8wrX-MAR4rayDBCOnh4r2kV7gHP-LDvLnG85GSWBM0rcJOa1OS2OnWZro97Cwlw_OVzCIoz8xcDElPzfU53PmfeoEb1qgVx4KZvMJtM6Oc4CjfxJjeHTCjGPgjMyIoXQQY_Lf5Wh6wnzRW1Jd8zPjJNsYp8XHT8jfaeKwMcc4YSQzbGonc5_hRWHyqwtbiP4sIKGo_Q1fEpfE2TRJcM0nRCPC7FoP5QSbKjlJ7ZFhqMxeiRoIkStSDCK0r4NjSqjgdQmCTfLQuMdlxUvKGkC3dJ2brSrv9cA9nr2yTcIFYYRVtw9LYfBi4lZRs5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MeekzveJp6fK4JOF1W6s0MmH0Jfi8781qllq2RVr7Y7AHpVoHWs_w9Okz4Kwagptr-gi_wwD-ENDuPgi98qYqF8o5p-Tpz8ad2moeDOXYYiyyZXKNwf4RJT1igf15RptSGK77sIPfmM8FzxrZeGmQPmlufU-Hf-tjd8Am1haXUy2YIRkDfRQhzgtxkHVZCqfNtPK9IF_oPI3N_2R2tiFJTg9_KVIU5eNZLLZTFzE1MIEmnRrGhwqvBg3jb22kfzfMhhGZbA0fUia88_8acCRKE9Q4uAQ1k0HSUE88IP_Bl0LyQ8Mr8vjQHVTw_Nxp3pT5JcyoVr-qOVtv-JE3ZNjgA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd790ae501.mp4?token=PThjrU3yDKosRnXrKJ6n3lYnrxusW3zIf8l2okxckRHbCIe6QHsZGPYgzWKzNC-2xyeO08yY5VoAkT7zw6_jwNmRzzNxU2w6XL0jfibpZqoTPhM8qF8QCgGIVxcN_q6M9CBRGsU98nuLciR_X5hHR1LBVmS4Erg4aWtKUvZOfrlFJQ916KqXtF-gTPQf7Q5_nk_PRDAB4x8KLqqRNrtp-QceAMrwc7fwjq6S3030aARUBdKZw6Sfea69jnuZ9cnll5KNivUyNHT-ooZs2FlYny3l9VPIETjDN02_TGbowhwYmUIC3YEB4hFJNNgULaGZ28vyj9eOgzkpOk0RMnSMDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd790ae501.mp4?token=PThjrU3yDKosRnXrKJ6n3lYnrxusW3zIf8l2okxckRHbCIe6QHsZGPYgzWKzNC-2xyeO08yY5VoAkT7zw6_jwNmRzzNxU2w6XL0jfibpZqoTPhM8qF8QCgGIVxcN_q6M9CBRGsU98nuLciR_X5hHR1LBVmS4Erg4aWtKUvZOfrlFJQ916KqXtF-gTPQf7Q5_nk_PRDAB4x8KLqqRNrtp-QceAMrwc7fwjq6S3030aARUBdKZw6Sfea69jnuZ9cnll5KNivUyNHT-ooZs2FlYny3l9VPIETjDN02_TGbowhwYmUIC3YEB4hFJNNgULaGZ28vyj9eOgzkpOk0RMnSMDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«جنوب لبنان  و پیام اسرائیل به جمهوری اسلامی‌»
اسرائیل امروز روستای شیعه‌نشین و معروف «مارون الراس» رو کاملا نابود کرد.
این منطقه که بر روی مرز اسرائیل است
از نمادهای قدرت و حضور جمهوری اسلامی بود و احمدی‌نژاد هم به آنجا
رفته بود و پارکی را افتتاح کرده بود.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5436" target="_blank">📅 12:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5435">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QXSFMC9DzRZrFPtOZ6qGqLML6GH8iNYl93ee5k_TYJfmj9dPO6MUFEiN1-vvslMnj9MS-2k2YwQTDTck_UySGJjZq0EMi9e8vsZ_xbzrK-ggyScTSaVKRExEMa0JVu8kf5B4lKmgAfN2dDl5d0Zql_MWDONVp6RS5b0hwNFh9A737tZD4MH3FPWLh2hGEjIe2_EuFwEkhWqHNAoVe6V3Dhwvyq7fVI3m1yVMfvYFLRyYe1M1Hmw14mk_ZVXqiwidhb8LyUMz-Zli4SJF6sj-9N5Z4WiiTpFXLphGPzNsuKLSnLk99lR2U4oHHq_Cxd6tUqw2VLKqvxhEQoOHaxI_RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسلمانان در سال‌های ابتدایی اسلام  به سمت «معبد یهودیان»  در اورشلیم نماز میخوندند.  شبیه کاری که یهودیان انجام میدادن، مسلمانان می‌گفتند  ما به سمت «بیت‌المقدس» نماز میخوانیم!  که این بیت‌المقدس همون «بیت هامیقداش»  «معبد» یهودیان بود.  جایی که داوود و سلیمان…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5435" target="_blank">📅 10:44 · 19 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
