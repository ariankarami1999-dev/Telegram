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
<img src="https://cdn4.telesco.pe/file/ZrXuPUqlNrc0vh43nv6XWRLjb3nlEoLniLr96zNXgYPtBnJ3gyEWIxVrk1WGopuJLjDaEv2_l2JxUCqQqHUU4z3ukiUC2_xA2x3lO_6xPWRwuS72GJRqTQqL06vgJuXggT5i92JxraNI7LIZcoNWtrVpIV7OsiWJh-38rbDYXOHSuH-Ajmjol2N7KsKDoEniOxTyyxKXYaooz6SWWgaqmfHuVuoHp93voWwzgLglpNWz3bWXu-jYlPBVjaNfyL8TfxCopDqG2QaHZk__Sa81ee5RzxXZaPqs4Tb81UcAEPQFL_CC9_gN_e3BH0FS10LG3Q00_UucsWg08j0YKDNhOw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.4K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 15:50:01</div>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5539" target="_blank">📅 11:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5538">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
حملات موشکی حزب الله به شمال اسرائیل</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5538" target="_blank">📅 00:10 · 24 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5537" target="_blank">📅 22:58 · 23 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5536" target="_blank">📅 22:13 · 23 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5535" target="_blank">📅 21:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5534">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxvMDMbyy1RBGs9z-I4v_VyISib2O9Is0Mg9Q7fvhfhE2irrbBeimiX-jY19R8na68_wfU2gGtblY78-BdkqjkiIq6xWrvwZI8VWf6FzBDuE8WISQoxtkRdNS8zCJ77OCAZTry_v_uONtBfcS05K95DHN33uTtU7fBc-FM2sbzdSFlKNBeVgH8zp7-QfWak-TNUDuYQfjHjTwlnJ3pxgtma5YeGYfqabv0AOZoQZQrf7bHjI0wvOAfjs8es8VDq4hty-oKoghtArPBPpiKBgfKRaHJ8x_aNkFJC_vsUxlHJZXaQXVIKvvsrlz45ifouYzzhuLeG2awBlrB54Xn9yzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: اصرار ترامپ
بر امضای تفاهم‌نامه در حالی است که مقامات ج‌ا  صراحتا گفتن  تفاهم نامه هنوز نهایی نشده</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5534" target="_blank">📅 21:16 · 23 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5533" target="_blank">📅 20:57 · 23 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5532" target="_blank">📅 20:32 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5531">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPPeYhVF2UVVvidUO1MTL_kc03ielRCXbZTP1c_rP6iRd69Pzw0outZj2adyL2jSZsdCBohZVt_0Ej1sElyoR7I2ijoRyKTxSpqvIMr_0Pb7omZ6IsBzU0RP_V93Jh4s3M_OBm9BN4mCcOd27tB-7jmMnsqnJpk9C-1LBbvrc_-hn23GZ_QR1miAUDF0sA8--hjtLY2rrnh0WncA7In4L4E6uoet7G-vGKBvzuAee62vVpYH2e1sV_iYRJ8zT48SfzA5KsTlQa8geHN-XeCRp8KGRHiendeqhm8CT--q9srjBnLtxql5yY_ib3pKWa5CiY4qRwoda_ZZfPnIjCZc_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیسی خطاب به قالیباف نوشته.
نگذارید خط تسلیم و سازش با
قاتلان خامنه‌ای به ثمر برسد.
(نه سازش نه تسلیم - نبرد با آمریکا!)</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5531" target="_blank">📅 20:09 · 23 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5530" target="_blank">📅 19:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5529">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">نخست وزیر پاکستان: تفاهم‌نامه ظرف ۲۴ ساعت آینده امضا می‌شود.
عراقچی : برای ۲۴ ساعت آینده هیچ برنامه خاصی وجود نداره.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5529" target="_blank">📅 17:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5528">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4fd75ecd6.mp4?token=GMoF-QJEDa7V2CnHgOB4Ow7ydDMWlxpvFcX9vQT_gLHh3tjluXJWzXtVg26ipKvyCF5gkgc2S8l3PSXkc_3plS9YITIRaKoZma_RsYyJCNF7eVsWC1LUsLsJIj3STCRgAG1CheLRq-mm33Vp1mrgmTDvdKz4sI1g7GSkhdhub3BvQJS3ouBmDhvJ08G85HX8rWzONPUPTIsFwN_wW__zW1UGEu1pl3vJRsrFcqNnUKFQ4vk2pN-C89NlqxtyTRufoIngbsEVgLCmrNPptNZwCTrFsNaLolgIzRbRksiB_iX7SoRWuxz5a3VchLyppX1ryZB_JrKfzhqn8Wge9NixpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4fd75ecd6.mp4?token=GMoF-QJEDa7V2CnHgOB4Ow7ydDMWlxpvFcX9vQT_gLHh3tjluXJWzXtVg26ipKvyCF5gkgc2S8l3PSXkc_3plS9YITIRaKoZma_RsYyJCNF7eVsWC1LUsLsJIj3STCRgAG1CheLRq-mm33Vp1mrgmTDvdKz4sI1g7GSkhdhub3BvQJS3ouBmDhvJ08G85HX8rWzONPUPTIsFwN_wW__zW1UGEu1pl3vJRsrFcqNnUKFQ4vk2pN-C89NlqxtyTRufoIngbsEVgLCmrNPptNZwCTrFsNaLolgIzRbRksiB_iX7SoRWuxz5a3VchLyppX1ryZB_JrKfzhqn8Wge9NixpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان مناطق اطراف نبطیه رو تخلیه کرد تا در مسیر ارتش اسرائیل نباشه.
این جنگ بین لبنان و اسرائیل نیست.
جنگ میان گروه تروریستی حزب الله لبنانه
که با پول و سلاح جمهوری اسلامی و به خاطر خامنه‌ای، جنگی رو راه انداخت.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5528" target="_blank">📅 15:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5527">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ut9X9J7g361syPqP9n1i45gdwEt0IQf-tOiYnWEZrM4FHAj3GDE0-r0lrKBrYgzhzWmqLuZIQmbbe7Oq8N4w7zISvWZfveXDe7hoJcamk2v833LUYk6P51c2qdG25yoy6hWiNzc-1I0G9Q0314OWG_P0lXMVaz6hExP0PWaVUkDUpOlA1rzBPK0v8YGA6UMSf9rZpPMfF1jbxdzdS6Py03dX46bjp6IEF7DD_kGi-oEt9tcML8kF0vaBGmExQ6ZEnDzgccqqwQTdUltHk4dxLdQ4uO4BY20ghrLWbvCEen2GiSFd4m5rY6r6VM5nOSgrQN4KqzuuB76TKqmPgETAtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی در باز بشه می‌فهمید
مجتبی خامنه‌ای در واقع همون قالیبافه!
چیزی به اسم مجتبی وجود نداره!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5527" target="_blank">📅 15:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5526">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TUJSbjBk7r_HIDphUjPGdWvvF5VVos988X0S-2AylpvGUQ4BnEraRsQegDhuESduNEuCue3ovsc5B67R_Du0z2kAJ95mUS2IcwTL2ldogx2UuwfsAmoMWLuLOVS7xKqZZzS9wpmMxBl2n5eBTzX8Peg_H9bOvNOmxmWHoeIEs6w3lrTE1bYxU-Il0zicEl08bdO_wFf3cWGKuJ6GwLJX7-Y8Y_H7NegJBnB-wuLlChbkCUqUip2m12PWW7kCapUvZJG46Qpc9-MUzRZjSasrsBe4Vf7acFpMQRgl21szGvGjLKuqqrHQt46dNTFTC5D70FhFMfzFhLr_jUF7SiCXYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : ارتش اسرائیل دقایقی پیش
به حومه شهر نبطیه، یکی از بزرگ‌ترین شهرهای جنوب لبنان رسید.
اکثر جمعیت ۹۰ هزار نفری نبطیه،
از چند هفته پیش شهر را ترک کرده بودند.
بعد از حملات موشکی ج‌ا به اسرائیل،
اسرائیل فشار بیشتری بر روی شهرهای بزرگ جنوب چون صور و نبطیه و….. وارد کرد.
ارتش اسرائیل فردای حمله جمهوری اسلامی
دستور تخلیه شهر صور  - بزرگ‌ترین شهر جنوب  لبنان - را صادر کرد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5526" target="_blank">📅 15:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5525">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tNm4aqkl92JGi6Gsge_GInMnhQOUf5VregElWTnBSQEqQhqgO7FxnruV0hPtYQgZRKGYGIwYuFZ6A0KySJzBQlWNd4UpirCDmnondheQGHk0Z7eVPyuTV_766vBOaGSzqXvAM89oSRvyToKODXQoZIDDMnOxCSrsH4UsLbQgAOiTRr_TMBVTIC1lT0vISBsIAYlmIjszOmplPBn8MVdnkcadFwe2ekkPJBqu8mtg7zTYKN1DZyZZ5TU67dLs0AazEHZYcpvrTjqQQ0aRlwP3c2wCxM4D2vVN-6t7CgzleEbF2U4XdnLeUdyym8qD7mOEr8X23EuRXpHyJyEmWqHmDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیات مراسم تدفین خامنه‌ای</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5525" target="_blank">📅 13:58 · 23 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5523" target="_blank">📅 13:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5522">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">عراقچی : در دو جنگ گذشته، «مذاکره» منتهی به جنگ نشد،  بلکه «مقاومت»  منتهی به جنگ ‌شد.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5522" target="_blank">📅 11:07 · 23 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5521" target="_blank">📅 09:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5520">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwyBSdE-TplReEiPuf4ysgIWqcVSBlETdVp2hjSbvkvMAApbrdjajnOY8TQzbA_UBhCGHIBOUWps9uaFUvlf3UfSa0GgcM8yJt4wOleRHhWaVQAuzl2OWU0yrYozSxiZdAVwPgS-WiH8ylPBG_Ehqsr4yru50YRBDvuTTqARsdHl-KwugRr7c0fiSz2RcHLwcGoXOJpqtQulo64kF3jGCtmuGFedA5jOhGy4YQVIz-lp9vx5sfxpiLY0Bl18CYHNYx8xrYpDdeNkkBA60YeYX6DHcVo0IRYZRhm_LF5Hzw2eZxuNzuN21sqbLck21LLF_u5aN_AjJtIjw7ktcQstzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5520" target="_blank">📅 01:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5519">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=lYMLaCbJsCplJtVbJbFm86DAJZBg4RIWMbeqpicgHBCC_basjasaYsWo5GT1NQOVEWLGefV9BlTjgsT25sM2YmmrBvWGrRN_KX6nypOQ973viOfhXen953DNEyKlUqv6AuUcIqhpc6cWy6czkCS5GaJGu50AQQrPO9F1VeISeiUviEecvcYzj3ZvOL7MrP_GRsMUG6_yHrVhxMxfAzNHJ_CHBjv_uFBrXfhEcA947SMnSnXB3qJIHiNZRcokKmvUtH-SXJ2e0yjrJDHd4UKwKi9Qi_enzM_g_HuNV1xCrK9k8u9W2COiWkOLVY7T4YINKs5kao3_DKptvqnlwSbmEnT-TsEESnIXizGGBzmUy1KIoujtWePfZPKVWgG60raoxfo-Nql5jNCu6XerSOFKjXWsWdZsSBkXx-msb8Zpoh8rrCtA5ddmhKbT1tIF2DCosMPolI4gIRiK0aa7YvlfuoLumgPZdflIh8xIr5vTsVw5O_EQ1S33ABB1FK0MNnb6PkZn1RfvB4qCcdFrXA7LO3Rdi6Dp2NdGIp9vVwB66JIPOUntvJZi-liHyUiynVTTwZfqq1ncwumn8xO78mlSxQcrj8raGJSjwt_LrM8BPHAApdszX3p7_rx1bq6GBEnP59EAyw0s74e_EZq3kQZVbBlSmbFCPWZaiA5crhUul-o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=lYMLaCbJsCplJtVbJbFm86DAJZBg4RIWMbeqpicgHBCC_basjasaYsWo5GT1NQOVEWLGefV9BlTjgsT25sM2YmmrBvWGrRN_KX6nypOQ973viOfhXen953DNEyKlUqv6AuUcIqhpc6cWy6czkCS5GaJGu50AQQrPO9F1VeISeiUviEecvcYzj3ZvOL7MrP_GRsMUG6_yHrVhxMxfAzNHJ_CHBjv_uFBrXfhEcA947SMnSnXB3qJIHiNZRcokKmvUtH-SXJ2e0yjrJDHd4UKwKi9Qi_enzM_g_HuNV1xCrK9k8u9W2COiWkOLVY7T4YINKs5kao3_DKptvqnlwSbmEnT-TsEESnIXizGGBzmUy1KIoujtWePfZPKVWgG60raoxfo-Nql5jNCu6XerSOFKjXWsWdZsSBkXx-msb8Zpoh8rrCtA5ddmhKbT1tIF2DCosMPolI4gIRiK0aa7YvlfuoLumgPZdflIh8xIr5vTsVw5O_EQ1S33ABB1FK0MNnb6PkZn1RfvB4qCcdFrXA7LO3Rdi6Dp2NdGIp9vVwB66JIPOUntvJZi-liHyUiynVTTwZfqq1ncwumn8xO78mlSxQcrj8raGJSjwt_LrM8BPHAApdszX3p7_rx1bq6GBEnP59EAyw0s74e_EZq3kQZVbBlSmbFCPWZaiA5crhUul-o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی : در دو جنگ گذشته، «مذاکره» منتهی به جنگ نشد،  بلکه «مقاومت»  منتهی به جنگ ‌شد.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5519" target="_blank">📅 00:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5518">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=VYTyGgvzA77RhFdBuy6zXq7OSAJI5wVlrZmFCrWggLmuyRP7mtU3kE-2a4ytjsY1MO7MFg459FX5EKUEwuTyywCg5TAFc5xJsAwKmuWdzkoF2uYN6bYBAI-zDFocyhwFP3aBW30QYWpf_e8Ij3sWApHjcbQfpHVSpx2E55oWXH_XIC4VJvIZRsW-CzbzM60kN9JzDZMP-nehpid9KYPFMzs8ZSAy5sncdb8spyjTHFQL5E9OuUX8SfmrubaOPfgrfZTTSGgtMi7hfC0GdOcjVFVBwNeFY5oEzUnB8lbKHc0y0Xp4XxtZfM-NTxYwPf5Beykj8ciCxi-uMTcqgX2ZLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=VYTyGgvzA77RhFdBuy6zXq7OSAJI5wVlrZmFCrWggLmuyRP7mtU3kE-2a4ytjsY1MO7MFg459FX5EKUEwuTyywCg5TAFc5xJsAwKmuWdzkoF2uYN6bYBAI-zDFocyhwFP3aBW30QYWpf_e8Ij3sWApHjcbQfpHVSpx2E55oWXH_XIC4VJvIZRsW-CzbzM60kN9JzDZMP-nehpid9KYPFMzs8ZSAy5sncdb8spyjTHFQL5E9OuUX8SfmrubaOPfgrfZTTSGgtMi7hfC0GdOcjVFVBwNeFY5oEzUnB8lbKHc0y0Xp4XxtZfM-NTxYwPf5Beykj8ciCxi-uMTcqgX2ZLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت نبویان از متن توافق ج‌ا و آمریکا :
یک : طبق متن تنگه هرمز باید باز شود.
‏دو : تحریم‌ها برداشته نمی‌شود.
‏سه :در مسأله هسته‌ای مستعمره آمریکا می‌شویم.
چهار: آزاد سازی پول‌ها اعتبار ندارد.
‏پنج: هیچ ضمانتی آمریکا برای اجرای بندها نداده است.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/5518" target="_blank">📅 19:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5517">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">وزیر دفاع اسرائیل: از جنوب لبنان خارج نخواهیم شد!</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5517" target="_blank">📅 19:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5516">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5516" target="_blank">📅 19:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5515">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5515" target="_blank">📅 19:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5514">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
عراقچی : هرگز تا این اندازه به یک توافق نزدیک نشده بودیم.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5514" target="_blank">📅 18:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5513">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7rJ5j5KukvVZtvzoe71v58xb0fQTgfVGB-8ZRiFfNfMjFycmytA6oDuQNFfxtzmXI1VzzX6U3_-_env6qTU8DTbA0o9eeKvIkff626f-lKRtDHCVPc79_5sHAucotOmvxSGpsZM81m2Fuye_3_IATgvSntPLJA1frphqpxSUoVpgvr3wtS4DNElOw5cG2AZvy4WPxwVMcghvzJRWEmCfGfGN8v2ln9dGgtDebBD8b9PipNMR59qh6Zf5oEfeDt2lAul0xrww7in0Cer_LnydS_74j3Ajzbvc3F-vMq95g6ccUxJRjuJ17ZsQ5LDbSpUp3Cw_ZP9Yfgsz55t6_2ckw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ : این مواردی که جمهوری اسلامی منتشر کرده دروغه! اینها یه مشت آدم بی‌شرف هستند، اصلا نباید با اینها مذاکره‌ای بر پایه حسن نیت صورت بگیره.
حواسمون هست که دیشب هم با پهپاد
به یک کشتی هندی حمله کردند.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/5513" target="_blank">📅 18:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5512">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=jdZVwkhjgbh1LXbOlXTxixo-V3db1l0kOnsyjH31Fa7zIPzlv62jbo3xKMCgHZZfHaxS_ugPedRHRNpjla4VGZ3IisYBDfMWt8hxqf18tHNSYoZ6pvhyX9Js3bP7B6LAvje-WNwStEqYQVfGcDUkGP5udfH6jMOjP_mOhcpyZ2yN31ELv5RUMxwGuP8eY52rdJbtqVTnSZR3e5wD1eiP5AavVosax2KBNIPkS8m6f7XrwGlDtMpOKAcM6QKxdOl3WWJseHQuTFdtjuZOnACE4I7Un8lTWcbEmI2WVJ1txWuw6rmnG6THew7WzfD-FLjrRYxUwNF9Fv-b5yfeD1bYOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=jdZVwkhjgbh1LXbOlXTxixo-V3db1l0kOnsyjH31Fa7zIPzlv62jbo3xKMCgHZZfHaxS_ugPedRHRNpjla4VGZ3IisYBDfMWt8hxqf18tHNSYoZ6pvhyX9Js3bP7B6LAvje-WNwStEqYQVfGcDUkGP5udfH6jMOjP_mOhcpyZ2yN31ELv5RUMxwGuP8eY52rdJbtqVTnSZR3e5wD1eiP5AavVosax2KBNIPkS8m6f7XrwGlDtMpOKAcM6QKxdOl3WWJseHQuTFdtjuZOnACE4I7Un8lTWcbEmI2WVJ1txWuw6rmnG6THew7WzfD-FLjrRYxUwNF9Fv-b5yfeD1bYOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات امروز اسرائیل به صور
دیگه نمیخواید بهشون کمک کنید؟</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5512" target="_blank">📅 15:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5511">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
رسانه‌های حکومتی :
جمهوری اسلامی کنترل تنگه هرمز را رها نخواهد.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5511" target="_blank">📅 14:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5510">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qiImKXrZtIrkrrkaAO4ztonCKevvKb0_p0X_EImSS-yOd_cUIWjPfooPil8BjRy7kEaYb58w5E9YxtpQiyhISrOZTyMJ-yZbiriyEeN5LiiIROS8imVm0snsl4t2NQcneY_0nJ1OjHyw7ou_z4XPaonHRzuww6JuAWtpQowun5VJmHVQv4hxmW9Xm1h--IyK7wDDYf-HBUwRxlM8sl1CbEnyWUeYGdgUPj7gLM6tKU0tNp7AFGQk1QoE5N7gmIvtwrHf5mZR21Lc3n61U9ZFKMEej5XhFFydErxMj29l1CO60B6dlyyQXZISqxM5-nKutUhdXlvlEXyw1wr-AiMtEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
قطر خود به تنهایی حدود ۱۰۰ جنگنده بسیار پیشرفته دارد. شامل ۳۶ فروند رافال، ۳۶ فروند اف ۱۵  و ۲۴ فروند تایفون.
🔺
بریتانیا برای حمایت از قطر ۸ فروند تایفون در این کشور مستقر کرده.  قطر همچنین میزبان بزرگ‌ترین پایگاه نظامی آمریکا در منطقه است ولی اجازه استفاده…</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/5510" target="_blank">📅 12:43 · 22 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/farahmand_alipour/5509" target="_blank">📅 09:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5508">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=nmHOD7ImPWRhFghhx7sqjzpi7DIyGu8DHZzHec-LM0tyJoav1hVflLw8AZj3WnHBEY8lLmkNVtz10P2KvnzLwe_8MiTk1H9Vs6FgkRiDKeJ2y9QRlgQV5_Krcle5_uqSxX6-iJGZ5KV2eMlfKfa7vce2r7gCW-F2qBgk7arjmdTPtxrNkvXflaFz_fh_LOVx6HYmxBRlylJpviEf-7MEuxaB-QDWezP95hgeTk8OCCzOBY18YfxmJ_ZDJ0OUM4k7p9wbldclnXvPhHrYTIT9FzOKUKZ7CkDeP8_Dq1zYJJFgk1dp7LkIy2BViRX6Rb4FYPxLQ3ds7sFlK0U0eQ7HoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=nmHOD7ImPWRhFghhx7sqjzpi7DIyGu8DHZzHec-LM0tyJoav1hVflLw8AZj3WnHBEY8lLmkNVtz10P2KvnzLwe_8MiTk1H9Vs6FgkRiDKeJ2y9QRlgQV5_Krcle5_uqSxX6-iJGZ5KV2eMlfKfa7vce2r7gCW-F2qBgk7arjmdTPtxrNkvXflaFz_fh_LOVx6HYmxBRlylJpviEf-7MEuxaB-QDWezP95hgeTk8OCCzOBY18YfxmJ_ZDJ0OUM4k7p9wbldclnXvPhHrYTIT9FzOKUKZ7CkDeP8_Dq1zYJJFgk1dp7LkIy2BViRX6Rb4FYPxLQ3ds7sFlK0U0eQ7HoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاور قالیباف:
دو نگاه وجود داره، نگاهی که میگه بریم صلح کنیم، بسازیم، یه جوری مشکلمون رو حل کنیم.
یه نگاه دیگه اینه که صلحی در کار نیست!
ما قراره با اینها بجنگیم و قراره اینها رو تسلیم کنیم در برابر اراده خودمون.</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/5508" target="_blank">📅 08:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5507">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=gszcXLp0OgN_8VXnPVH97-SRTsxe3n1ggqxrc5f-YmVjQv9mZe8qA3yz7IB8WUA8GA-6JJtQf4jOjsFyCIrwL5Te9xp08GAgDtINjPyoHkBJuHEtcjnVsKS1sI46fIFsox6HWa76M90xqU3OBeogE1PqIVSJswupOIIWJA6HaR0zHouB0LAQACWfEt1ulleg_rpQu37hQ2UFXczEvEeNxGMsLKqFv4nL5fE2wMFJ6ji_ThGDJQMNfyz0wOH7U21X1VMHpfltZD0HeK41q_tTAsBevYB4GMrnA6__Rg536EqRJhAjmSJvMAC-u1pwhSUbsXzMsLIjvE-FybM5Az4aRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=gszcXLp0OgN_8VXnPVH97-SRTsxe3n1ggqxrc5f-YmVjQv9mZe8qA3yz7IB8WUA8GA-6JJtQf4jOjsFyCIrwL5Te9xp08GAgDtINjPyoHkBJuHEtcjnVsKS1sI46fIFsox6HWa76M90xqU3OBeogE1PqIVSJswupOIIWJA6HaR0zHouB0LAQACWfEt1ulleg_rpQu37hQ2UFXczEvEeNxGMsLKqFv4nL5fE2wMFJ6ji_ThGDJQMNfyz0wOH7U21X1VMHpfltZD0HeK41q_tTAsBevYB4GMrnA6__Rg536EqRJhAjmSJvMAC-u1pwhSUbsXzMsLIjvE-FybM5Az4aRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی ظاهرا متقاعد شد که شرط و شروطهای ۱۰ گانه‌اش رو کنار بگذاره.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/5507" target="_blank">📅 08:17 · 22 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/5504" target="_blank">📅 22:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5503">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، به نقل از یک «منبع آگاه» نزدیک به تیم مذاکره‌کننده ایرانی گزارش داد که رژیم در ایران هیچ متنی از توافق را تأیید نکرده است.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5503" target="_blank">📅 22:08 · 21 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fUaLAooSk7AGdDaGEFNqfMFcs_cs4qT9Yb_NCsEEm5FrvHFB0-wsURpcbvGL9nxy2gNi_JCMK3ZhI9KjhufWIV1eYVqw5F1Q_b2Pgz6H8ok0K3SiXQsQS-EiQzkXEjI9xn5EEhSAHSgB7QSGmPXGY2aXnH0piVyJg2Tia1tpVH5hrBLoHUuQk6LQBMo5OzG2MYwalaFo9Dx1FvmKKOvPGcPMyKl2n3LUYb3n4xWBf7wOIxw7sMEyor6kN6s9opaGmT24rAy-oYbt3h02MplDt0YbUXTA6iCJd-nDMbtNn1FGzOjCeMLYHs20p6_w8e39YeLxCzXWtvgrWfrxtZUTiA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=ijp6D4l3I_jjaVlDTi75whmCrgY8JHMrHFnftmsz1LBFxk8PGeRh5zQeWsyjQDKpzEMxY46bdMi2pfE4l-cKDh5T_6ADNKYnmgo2P2tgUJ2HsQY4SLjB-5WtM_zwlaKbjOmR0k799jfa5Kz8MHCXu1-7HQQzMkdboftft52RHoYECiSR49yh5IPgdaD8K5UIXdKD8wcCJzY3p9b1OHYAEJM5O8__Urr78Ldf4kLuJKU_SJIuQ-6R8rDzTfeGP52iDnGfAiYMJliG1zF6cMTVLW5P7ScF8TDeqMfRfqekHMZoxSyz877D3DVRw2rlcdvXYMC2GC25i1NafRSk3YGTCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=ijp6D4l3I_jjaVlDTi75whmCrgY8JHMrHFnftmsz1LBFxk8PGeRh5zQeWsyjQDKpzEMxY46bdMi2pfE4l-cKDh5T_6ADNKYnmgo2P2tgUJ2HsQY4SLjB-5WtM_zwlaKbjOmR0k799jfa5Kz8MHCXu1-7HQQzMkdboftft52RHoYECiSR49yh5IPgdaD8K5UIXdKD8wcCJzY3p9b1OHYAEJM5O8__Urr78Ldf4kLuJKU_SJIuQ-6R8rDzTfeGP52iDnGfAiYMJliG1zF6cMTVLW5P7ScF8TDeqMfRfqekHMZoxSyz877D3DVRw2rlcdvXYMC2GC25i1NafRSk3YGTCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/alvFMhFq032AEyKbhCwvvKdHlUGUlgPZhhlgc2vs0bkkfts8WeROk1Qa-vgMGIdsQqjOE2j4qOQmXUBgXFXciSldMXB76zhKCnwptzTdglE63WnlKBiOUVYn1CnFI4ficdMFYwt9VDGwb7BfWahmEKxx51EKc8qJ97s4NN1_pQVz9uKLqDlDoz2fVhlc1McS3FiXDWyUVtFRcKoDkKKmE4tK7VI647y14_N-8O7rE61MVVqyvDn8L1Ulz1diPixPGM4QR8OF9WP7LJmNBQUKaoFNWA2v6b1ZQGwSXaA21ftnmaNwqSTslCVzq7yFSP0SjMqljShEXeRXJJvalrSHvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه داری آمریکا : خسارات وارده به متحدانمان را از حساب‌های جمهوری اسلامی جبران می‌کنیم.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5495" target="_blank">📅 17:25 · 21 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2JNhxqs8Qa_hOOlbCn9_YFAcLBG9YfqISRGGQLBODjqyH9iyBCZYRc6t-216BVz-l5sfYCBRHZWfwRIxiM3CPXtpOQWQXrJ-ekJ9aUoGBwFxEKv3VctUv7xhVt-iQjnN9TkS5IHVPxY8xrKR5Q-gM40SgcLbOA76UwdrtQv-fBDb6vFr1NHJUkA6AtBuhtlZ9nO63ViXwOQa2L3IEaKNGlkysI6mchUBSNVLeJCc6W-fau5IDs9Q7tk0JgmkN29QO8vdze95HIiJR7X0UlsV4VXF5RwLH2CYg7cSWvzTujaal_-usYQdRfU29D8rDfwPmmInwway5ecBc_0zgvg4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از انفجار در سیریک
مناطقی که در دو شب گذشته مورد حمله آمریکا بودند در واقع حاشیه تنگه هرمز هستند.
جایی که رادارها و سایت‌های موشکی و پهپادی و…برای کنترل تنگه ، متمرکز شده‌اند.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5493" target="_blank">📅 16:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5492">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kxtY_bCNmxJQsWK2xzqv0n29YsE57aA2qNtJli_g5N07Et-33DitqVywvVlzngegkMAUsCK5QK2zY7Xj13EOgs8b-MCjd-7jzyWE7Tamy_sTQ3Qz-nDEfpNy6IkIIdtDxLX5tP-dvbaZd7lleF0q8I7Gyko9Nbfik71VDMVRoYlAubfGFFjEStvbbk0S1llZssEmikdK3wFh0a2yNKrw7idc_Z1F1GquRftkS8v1HPdUAmUg32S4kT_ajSCeOV6t52-DERIqIponp8guo6M5dSbb4ZuNszb2APW3L4CWc9SC_p0yW04UMX8Zc0N1ACBRxOU0jUbBc50YLlKSS778RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اموال ملت ایران! که یا مصادره میشن
یا مفت فروشی میشن به چین
یا غارت و دزدیده میشن !
بقیه‌اش رو هم‌ میدن «مداحان»
و «رجز خوانان»!!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5492" target="_blank">📅 16:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5491">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UFSdFAODC3YhmVw47bREJLrij5mcbPely8j1-VBg9zddt7QCBLNWVxNPQwUP7WR_6QJbLQ0vYbXHam_jdUGxGpnUrRgacLm2SYe1Jg_buoUSC7FHvHFcec1HCH1Y4j2Rb8H1fwyk-xC-Hv-KN7Z6kyrnE4UatWsMT6AYadHWgisg_jnEGR5Ok4VgiXhB8-52Ak5IjGDSX3F8douwfg_Hkzcs1kRSoVCb1AWDRwZJhT_i4c7DpSRJ9poyiV2YhX8FNh3nmcYx9w6j6pHhy-qCqcnlFnUz6QA5TmVTHMbx24bpqfz_JN9vN8FDZcg2wd2JW50ToCJ4gin0isUKc4QUaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5491" target="_blank">📅 16:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5490">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iUj3ky2z91rgc6gld1GgwG3wbgBZeC8FDAWvTvpdFAyxPMLsk5FVU5m0YOkBmfoHtcOmQ4PXVyytJ3u39QtLsKOTqm8arN0q-ds4_TIpDF6Zvhw0y1n1UbENZGIfgC1Q1phOkbTns3ZkiAGATvE48LR7sibRHJnQRz-U_e3QfG78G7gahbXfnubmCEJcsFgElfz88A-6YgKDR-MG2m-ulnCZvaWRZ5HGwMVrhmDusrgjDo9zw7wu6PDM_Fe5syg5B9U1J5r871gtkODXaHCYrQiTUFdyCcvPtm8hgiDwDaHBzdwIdP1t4_65ddKv5FK2MCYTHyMUsiSeEY6rUK6U2g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iEtZSIaXE9sorb-9a-Hy014xOLnLR0OpnjwPXF1BTwn-YWNXW7rumuCCDlnWsa-CzC7lkXA1BAV-7rlyB5HsRqSweUySjouLAikXjWd-uztaY8ixiL8f2TxivjYW2YEcyHmHLtOmOkz20LFjnddHJbg-rKqFVvpvOZ8c9ARpipKuR3MayFozRHTwIyqRXDVVed4B4sBLEHsJxOGkbIpRXeOgbq_gmRHy2GQy2cn7DS9fFstYYNhCzWn_tC2BU6MIda4zGbBSL1F2ceQvmEgh2VB2g1y7Y2nTO8sik-ioh677FXEh35ZlfD8wPbjPG9Th9cEsaYRKCkSPQ4tQ_DtSCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پاسخ به حمله مستقیم جمهوری اسلامی  ۴ روز بعد اسرائیل حمله‌ای بسیار دقیق و هدفمند به ایران انجام داد.  گران‌بها‌ترین و مهم‌ترین سلاح دفاعی جمهوری اسلامی رو یعنی سامانه پدافند موشکی  اس ۳۰۰ رو که جمهوری اسلامی پس از حدود  ۲۰ سال تلاش و کشمکش از روسیه خریده…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5487" target="_blank">📅 10:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5486">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/163555b294.mp4?token=ApjCuJyx15K_Z57KbKHLlzhn3P8SAwU1yWKpnxaL_6N_-r5ddYhg5lxe2X7Q3eZUQwnXUgi1nQjTmT4ZX1fMUSnaH0p8d5litggEU1ueYjGCSd1j2i3aSi-_7nbRSRJ_gBSQ-rlhHkvFqwdBepkzWB1jLWqTz8a7tksnulhh2PUDBCdjSZma1X4QFvJq9SUkc9SbqCC09xjAZl8qx8wVgIm5p83RUnUIipBfvl2hZErnFAcduJaai9b5Ahx3zrTe9RRcYREEQ0zJWjk8I30VY70UduI01nG9HBrm7FLIvzsEESD_Dsog9_8F_Xs6C_f9w6hgTDbKPoLuC764b55WIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/163555b294.mp4?token=ApjCuJyx15K_Z57KbKHLlzhn3P8SAwU1yWKpnxaL_6N_-r5ddYhg5lxe2X7Q3eZUQwnXUgi1nQjTmT4ZX1fMUSnaH0p8d5litggEU1ueYjGCSd1j2i3aSi-_7nbRSRJ_gBSQ-rlhHkvFqwdBepkzWB1jLWqTz8a7tksnulhh2PUDBCdjSZma1X4QFvJq9SUkc9SbqCC09xjAZl8qx8wVgIm5p83RUnUIipBfvl2hZErnFAcduJaai9b5Ahx3zrTe9RRcYREEQ0zJWjk8I30VY70UduI01nG9HBrm7FLIvzsEESD_Dsog9_8F_Xs6C_f9w6hgTDbKPoLuC764b55WIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی از ۲۵ فروردین ۱۴۰۳  رویارویی با اسرائیل را از جنگ نیابتی به یک جنگ مستقیم تبدیل کرد.  در عملیات «وعده صادق ۱» ج‌ا با ۱۷۰ پهپاد، ۱۲۰ موشک بالستیک  و ۳۰ موشک کروز به اسرائیل حمله کرد،  دستور حمله مستقیما از سوی علی خامنه‌ای صادر شد، و جالب اینکه…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5486" target="_blank">📅 10:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5485">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gLKXK0Uyn4PuNVvfiRCCQSopmp-i8WbALbKAZEYyNXTfD4TPQ9tLf5wU93PMF7Bhy6XHYlqbZSLxOGG2NaTrkvduEtUBrgCgP0on2LxQaJAW5RXokcstdumVfwcBHYDgq66lDIfh7dv3JBeHB-KKET21lwPQpQGMm7riiYeqGxoTfi2Kd9m3NuSaksusB_RrndRYgTI9IyXJf__3WojqWiN_TD4KgUYmad1QE7ogwL7EQe6gSeYs8eK_uxcZbPqbIUHPyiRWyPQ4s6aLrQjX59s47ecjDPbW-WJAu1icnapAjbpB9BhtEA2d_hNkszdYSQ5L79HzNgVN54-wN1lEgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ غیر مستقیم با اسرائیل سیاست  جمال عبدالناصر بود.  ناصر فشار سنگینی روی اردن و بعد لبنان آورد تا اجازه دهند، گروه‌های مسلح فلسطینی از مرزهای اردن و لبنان به اسرائیل حمله کنند.  اما مصر خودش چنین اجازه‌ای رو به فلسطینی‌ها نداد! نگذاشت مرزهاش با اسرائیل دچار…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5485" target="_blank">📅 10:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5484">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2q9SKyqqVSnH1BazzEZqzqwAbcol9-0lm6lVwGqf1shMGLWYgYOCOaYR4kft3VOaeHX4czRX1WYCGcbemVRowVXV23ZBKqTB3wAyeXIE66skdBv_XzPxY1o-bcLlBQbg3tc6CSmwlCj8eep68h1d9bFcwS-4UtGLmPQ2aBvtQL9qJQp33ak9KgQKcMBsnjjLjK4y68oH-d9T2RT_MT9KNYiXb3tMmhwR5Uc7ma8BESOsChdziJ27CD9wqUBkO2v9ooKGhcyUv5OiWRX-n6RYlx6ZpeBBxzy11PZTo5P9yJSFwgDrXAus359K0WB5ucligaULHLd8ukWBFfRlMaIwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی در ۲۵ فروردین ۱۴۰۳  برای اولین بار رویارویی با اسرائیل را از یک جنگ و نبرد ده‌ها ساله «نیابتی»  به یک جنگ مستقیم کشوند.  تا قبل از این تاریخ،  جمهوری اسلامی با مسلح کردن گروه‌های تروریستی مثل حماس، جنبش اسلامی، حزب‌الله، حوثی‌ها و….. با اسرائیل…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5484" target="_blank">📅 10:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5483">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EK3PuXOI2PSG4_JZ6QXwVD9zaEn71IDJrLsiivDdWBvGwYlvUjqo-bf4NHNB1ygDTiMqmHqxZfzcmPX4uS3Zz4hJnUX1wrxHtEwrqGVPOqkKDTMqV-jW5wiTY_JbaGb-B6X28v5Rt5IcIRZjwYRUPevEKpWoFKLAl4ftUkza_P6tuPCJf54xo2-KCOr52fpwZpGb17u2luDOozlps6rrPXYpnrRtKb3zWBnoviYEpwfNSMMfk5CrDrWCCRh1JaRiPBQwbLwHvLm_zrz35xV0M4OsHN1---PpXD537Ebmtndy3Rw98-NsYtQeq9IvwciHvfIXaJkzHDaeP_Bm20AMYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از مهم‌ترین پیش‌شرط‌های جمهوری اسلامی در دوره جنگ ۴۰ روزه این بود  که «جنگ باید کامل تموم بشه»  و آمریکا باید تعهد بده که دیگه به ایران حمله نکنه.  منظورش این بود که یک «آتش‌بس» نمیخوایم! «توقف کامل جنگ رو میخوایم»!  این‌ درخواست از اونجایی میاد  که جمهوری…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5483" target="_blank">📅 10:01 · 21 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/5480" target="_blank">📅 01:15 · 21 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5475" target="_blank">📅 01:03 · 21 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J5vybZ2MBGb19WDVu_Np-kVg4a_tRy4XBTKZBQzJWrtMu5eSWpI7qhohYVIyU2K4joijRH_sJ4XadvLWF-loeoJioYNiZBBUcbSDozew45wCiqz6IF2bY5BTGthDYJuCBwHxItUzSLSlyY2DLsitelQNg1NnIq7YwcTqEkZ8UKOWMBymWEcFg1nywUyLkn8s3vt52-jPxLdTwnA9iUXdOgHs_91Vqc-Wze5KPHa5iyMVdT5pgokqzh4cBO9to7qxKphi_UxyA2H9UFXnHr4npqa5Q7CbvvzyWMLEOgqZJfKkkwl1lLnQpSx2S_3PRWXUaSz_yN-0OBYy2DqUFyPjeg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/farahmand_alipour/5472" target="_blank">📅 00:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5471">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
ترامپ  در جلسه‌ای با مقامات ارشد نظامی
- امنیتی آمریکا در «اتاق وضعیت» در حال بررسی  یک اقدام نظامی «گسترده» «اما کوتاه مدت» برای ضربه زدن به جمهوری اسلامی است تا سران ج‌ا را وادار به تغییر مواضع خود
در مذاکرات کند.
🔺
ترامپ همچنین ساعتی پیش به خبرنگاران گفته بود که امروز ضربه سختی به آنها خواهم زد.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/5471" target="_blank">📅 00:11 · 21 Khordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/8d07d6979a.mp4?token=t9CJjtzwVe6jvoo9fJA7m2ZnPt5ubuxvd6Vtu0xIu_to6laQQipY-YRL9z0uUvZqIWcdqNBFG5cGgqupsdtOnMJtxzfthwwfbIOVJE0MAv3yCj6OSUpu-jT4hDBDGuLYozFK9Za8_HeL1Zvzl_zQuEKCoRw0n8YeAtlQg2QHt87fpa4WkmLIrBI_5TdiysXZ6zkW1I-XqROig8Hd1uN7C-ot_uwEI3C9PEv9v8TEsNlNoHdiIak336-tBiZTydDMIoz70YemjQHfz1QpXr-1i6Rm04l3xvpJkhi7LiupNky99GM8b9yLOqn_ZbHCueMYh7ZzxoviMJKr8YnUMaNlng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d07d6979a.mp4?token=t9CJjtzwVe6jvoo9fJA7m2ZnPt5ubuxvd6Vtu0xIu_to6laQQipY-YRL9z0uUvZqIWcdqNBFG5cGgqupsdtOnMJtxzfthwwfbIOVJE0MAv3yCj6OSUpu-jT4hDBDGuLYozFK9Za8_HeL1Zvzl_zQuEKCoRw0n8YeAtlQg2QHt87fpa4WkmLIrBI_5TdiysXZ6zkW1I-XqROig8Hd1uN7C-ot_uwEI3C9PEv9v8TEsNlNoHdiIak336-tBiZTydDMIoz70YemjQHfz1QpXr-1i6Rm04l3xvpJkhi7LiupNky99GM8b9yLOqn_ZbHCueMYh7ZzxoviMJKr8YnUMaNlng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله هدفمند به یک خودرو در شهر صیدون لبنان
برخی رسانه‌ها نوشته‌اند که یکی از اعضای بلندپایه حزب الله در این خودرو بوده
هنوز جزئیات بیشتری منتشر نشده</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5468" target="_blank">📅 15:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5467">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gR8YGZ8y8bsUh1gWsbVuDUPswHrQDIbQqhMsY2sFULfYxC8am5k3CedJu_4R7LGIRS_ORTOGw9kqqPBjx6tsMR9LR0VfpSet3WgqehBpNOQHTEK64xNIzGNTfYlpZkSfB2l0qX0ezwLI70OR-a-Oon0grqPA8CgaRyLvjGAh4ShVZXyY7Y2L3HRCGRSxwXLS9JB7YnsgVNgd6H3hZrC_NSpo-SSg6guJq14J7UO1kzbXr26mCsmlki5mq8qzTMCKJr-nBchASfiZqkMmQefEUVo_myarXW4xMDnDtiK5jNon2jzyoLx4Fxb-vOt6pa6Gxh1Eo_T0crn2WnX8tRTQow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5467" target="_blank">📅 13:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5466">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d5tNFE2_HSvaC9qIO61K-kvDd3ca3ARsGZNX-xq0QTkAtGaLP3_OOHnUXDjzwSj-weG-aLu-ZjT21_DJjfaI24nik1MgWj19VEkI3IKERckKQuAh5nAUF8EhQhkh4mfDwi5nuZZ3AtE2agv_epfgXNYEUP-EHFevP7wAXVa_UMT-RBspF93YUM59n44Goaid4aqexoRguciUo_k-AxtEg1QLqfDcW5ecVPmWiuD5dGQVbtumuBVFmZslmBuoKgt_K4vA4lIQRlbLYXVqdz5gMMKtUInJu136MnzH1KDNnUo_uGs8-48yklXZoqZRR-JGh-zU0wFfsDUCFLi7MmUEvw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5464" target="_blank">📅 12:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5463">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfWgIEaYteAIsPNqoqzuMw-5FayMiHFSzLLfo34h_jirKYF-792nJoD5jwed5LzYde8rSz9EWiPOehKcqoREKI2exySPxxRq2hYv5p1NXcYYL8KT66aPaabgYfXdTDrEnIbuZIqX80RW_gObXC9qbNJyBklEkYO6IVLX4aotmaj6LYm0rZSyx29MdYl9FPl4CWQqlWzxFm_IVCdT6xJVbspTXPghRyp8F1Oe1Qt0M2OGGN6sKb1mBTZvOwm94r2GrzdNuxjakdiNcJ_juViyB6IkYMvFU_5iiE0DRkvdHErUvoM1j5tTsTl4my5YycPbzek9i4TkIpipszIhrQjwPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل به دو روستای شیعه‌نشین
غسانیه و حومین الفوقا در جنوب لبنان
هشدار تخلیه فوری داده ، اینکه اطمینان داشته باشن
حداقل هزار متر از روستا فاصله دارند.
این دو منطقه در مجموع حدود ۴ هزار نفر جمعیت دارند.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5463" target="_blank">📅 12:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5462">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LFv953K8AelRy1eR9gXSrJ6OxCGXDQsdJ18oZ5RW-UXMGlI862wLl0LDTZNouGqPsN1CLuD0vcjLVM_pknPWMXa35_OAzL8_6lhrnvcwDljzh8-PYts0DjiUWRYItmMX86W5bkFymZ1eCRqG6bTIophiX0g54_E4ivaha38OQjZPPAb66OdQAFaipMUov7mx2798zamLFSiWXeb4N4yIWtvO0UXCNXH4hXNoEQlyhDzhJcDdGWBjva9Dg-pMWqT5zZdGic2DRnh6nKPJ3H_ZEOxeAFVUpXwvJM0N6dZE7rt80gZ8qhVBOmonzNr7HLzvc_Q2ncm_Xe8L0KYNnQS5_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب! چه نکته جالبی بود
واقعا چرا آمریکا خطوط قرمز شما رو رعایت نمیکنه ! غرامت و تعهد هم که نمیده!
اسرائیل هم که معادله‌ای که در لبنان اجرا کردید و براش یک پتروشیمی در ماهشهر رو هم فدا کردید‌، که براش تره خورد نکرد.
عجب آدم‌هایی هستن!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5462" target="_blank">📅 11:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5461">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abMB4upv_WG1ERcl-kghfdSQah_a7BvcNiuIxoNUZ8h4iQzbE-WT2mhqN_VCKi6p4Od3cZ5sywJEaixqre7Fxh5-oj-v1QVEV30pRACw4WKJJ7or8nGMgPPNzVP9QR-R6Z25U1vPPhsHr0dlDmspOGYvhTJTJ_r0CyqE2p51iAFXniKuubxZBHBeN4ExIIZRxJ2KStIE9hTta8MuHJw-Xr53ugUccwL4Apv-jJpw7uHhyAXbGKiwrn38j2qt1_TN2oEIxWeXLP9u8pqtdBU8eUXPrh9Tn8UQF59RGN52ZG7V4sv0DKrDJd7p-Fc5QOicvA7vZx0IoTYHQUfaXtpyNw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCENjoa6rN25V3TQzbw1Mh347Mm7BCKVJmlHN5oK57phUG2qXsUKT41RNxRvCXQvdskjrVHjYuJzRVmCbx7paKlk790P8shZsShjcFQjWdvZv8zcWgmJ4HwkRJ2qfYlzCc4-UoQcKrqyN_dsVOUBbreUft_lf8u9Fb13Iiycjb20YNFVLC4NFvfS6Yh2V-u0mf5IW7bUJT_N11GNTonMsEA53-PC11GabD9tuV6CbduNlZKJz564ixmdYS-puQ7gogQQoPodL4Ze-H8LvdLFBjTncsOXswQMfQ8PHJ3nY6LVyPVR5ECmgFexR8Gkwy-OucigzgU8QwTzEQmNRPNbeQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKOK9wId8VmnqdVkDDICKlUylU5srmNXGD5KVRnEMLJJj68zJQOfhTSRpsF1MRxdBgkTgivelWh4F3uXPjtle3xD6_eCgUFXz3rviPdW__H2pjVSvRgBPvYWXMC0LV0fiBlvmCICuSd1fCo4bk4Wtu5eZEMUD1qhp9VWztLrVUwNg2SpzOUosaqus93PSlkyArLEVlFjtebRtHNNn2HGoB4eJRYWNVfzJpsFZOW2wt8gS1cQm2btqbU41OTPnj8nL7YqoEy_a2G5ghsGbBRN6pOD1nvoOlZTkJh4--Z-AlvJczOB456lzNgU6znWB2SynE-eQHHXS2omJ3GB5CGOuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخراج رضا دالمن از دانشگاه شریف به دلیل آویختن عروسک موش
او پیشتر به مدت یک ماه بازداشت شده بود.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5457" target="_blank">📅 08:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5456">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrxZnAvTcSoQpXsfZbw_0a7bQXjSXpK4F1Z5hyRmxzG9zaIf7BlCSVkL2rqga7Gd_iNkSyB6OjxiagzwqVkUaRpC2gVGbHmsdbv4m93R02ergynyBSsnsW8oWyPRYc2tEMmwiVUhX5VxT43hzqyyDNmSpIww7KugzCFnQeRsqudIGbL-PTBNfwnxjGxREwYQU9Lc2rY-uVrWtS0tnLLgnt2NKk4ovnh07BLBMUtb6hmgMlltWvQx0uzUyCVvC6iPM-DLF0s8vzt9E6SC_06XxrTSeiKdRwGzzdkabqDHU-uSUZ7YdPaIPM4hjXPuaI2c7-H4zz_X6rDExLxV-Vnx-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ابراهیم رضایی سخنگوی کمیسیون امنیت ملی و سیاست خارجه مجلس
ساعتی پیش از شروع حملات آمریکا
به جنوب ایران</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5456" target="_blank">📅 08:35 · 20 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/5452" target="_blank">📅 22:53 · 19 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oduoYMokIgoaWYR4nX1C7XJykZ8PX2m9KJ4tkMQE8hXhakB-g-fSW5BZ3C6oVkqyl19O4LX-pkY1DNw_Mss2fUNbwD7DoZeotLPhzHiB3ZiQQWpoF-cqXnZ9dIeyc8bnhBQ1hm9pgIemK7H4u62eAD1BvW79rJXKRpfMlEkD3xGXh9TSNda6XCU3U-dGJK7hkSl_hnx8M-7hqNMywZy00sfNeQhiCuhpNhmlpNWpk1K5kZd4GQ4dZtARE5Ut-wId5I8AaCKO47WsOpGvbZLmB9JM1ePQuY0uy8juM-d3Bqeb9jxksCCJUE6Rp7FLWN2PMpt1Js1zigEZydqXfZ05vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/5449" target="_blank">📅 20:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5448">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VgAECCzap8i7OY_O11005KWTVNuVRLUY9Q2fO_TECMlUJYZLVOyhaGhg4ZxbuSJv6RkQwqPwGQ5Hi1aRzjDFhTWs-coq9RixMyCisH563FqM-rv9Fyo34Gl-oelmmtgpQzvAZwf4EYJJfjQwmctN6SqdcIyPlPqJxRpijTx0qpNKQK8eiwP-ynzAxpt1sNKV4pLjimbLje90mj-Gj0D302uzhvfDV5EssP-zxvCNTHUDXvOz9Bb8KOmRxfrBs_3pF3hRZSRR-1t3GVjdsfTJJChS3lLvlQko1q031Xlk8ELbvSfvqg6Am-UbgxxWgl4aoaWFKRNYR7XdGVkneF1fBg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5447" target="_blank">📅 17:22 · 19 Khordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/4718cad225.mp4?token=hdds8WlzsJ1_QgiCJZiJTL45ZV_uUFqdErTnBGpGagqmm9Ee02ktBfQW4pB-DYcqImhi3g0c1d45hgRaff_mSJRlMSRaX0ji4Dif-PJ974dP7ocpotBY1U5xCWDjOVgOL5KMiVJwPmtW0FnBPTokq_kh95mGBBx7a5gMRGMDz3TYHtKq4F5KuF5ki7YBgQwRWbMfg3bWEZh02Yad546oG1Veg7g7IEQVZHb8YV25uD8rbFtUHPOnpz4a1TdBNGHF3jtBlPizDqYuHjiA7XCjD1EXs8fkLz6awqtX8SzoK5_hMpWKZ08wCS-vu8ssJpc__CDhImpX79W6mYmKQ_5osg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4718cad225.mp4?token=hdds8WlzsJ1_QgiCJZiJTL45ZV_uUFqdErTnBGpGagqmm9Ee02ktBfQW4pB-DYcqImhi3g0c1d45hgRaff_mSJRlMSRaX0ji4Dif-PJ974dP7ocpotBY1U5xCWDjOVgOL5KMiVJwPmtW0FnBPTokq_kh95mGBBx7a5gMRGMDz3TYHtKq4F5KuF5ki7YBgQwRWbMfg3bWEZh02Yad546oG1Veg7g7IEQVZHb8YV25uD8rbFtUHPOnpz4a1TdBNGHF3jtBlPizDqYuHjiA7XCjD1EXs8fkLz6awqtX8SzoK5_hMpWKZ08wCS-vu8ssJpc__CDhImpX79W6mYmKQ_5osg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محله الکریت - صور - جنوب لبنان</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5445" target="_blank">📅 15:26 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5444">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ra3an3mfL4wIFcSznD5MXkbDS1D69NKmM0H4hxUHf5dP67zrNGnHpyPNZM6TjhPrvzcum74cnjgPzdEnt-4UZ4p24igjD8O1ikL9drlvN8Mz4zxr4z-7WAvSXBPupipo6FEHSR5tm05Z7qN-F5ocay8o87flhAOvlHz4MCl6PVbhDu_QOThlCx_Jn4d3v05cLitXfhq7gaCLm_wX5YluNAIRlf08D3tqtPgiABhqyUhHnmxqEn7ZE7FW9D1PmEghOu7izBXGZTfUtTFiC23hPpVYqZ5kanCRTwGfHwnJLjPEQrSHKW2rJwix6TPPGoxl-t0bpLuYsFnqaAbMJUluLg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NfcK9_vXJ1ES4bULa92WvnaQVwWdJPqxSq1fC3MB-PcDkMHHAEXKtLIjjIiY5c58yIqMt1mdbP44XPCgLEAtKMHcECmGQsH2msqWS2zZEi7eqjcEF3q_SXBl_BOyFwIVl2kgk3ihozKxTzt5RpmNkWuoluURQGjifiuF0WF8hEiTrb1IrYs630qtuQeCNf0dF0dUpOsdVtY3iV7jDHMs070uqBcQzJTgMd7lpiiUAlvjuH5iefp4Y-u_H9l7vLEdLAglqEI02StuiHMAS4OXr4mUtr82Q32Peh3FJCRVdqX6GTfcsSBlOlVRuZ8fHs4pimdjiWNoVSfERRZix8e9KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
در حملات دیروز اسرائیل دو عضو
پدافندهوایی ارتش کشته شدند،
اسرائیل گفته بود که به  علاوه بر حمله به مجتمع پتروشیمی ماهشهر به پدافند هوایی نیز
در چند استان حمله کرده.
درگیری اخیر در دفاع از گروه حزب‌الله لبنان صورت گرفت! جمهوری اسلامی با حمله به اسرائیل میخواست مانع از حملات اسرائیل به لبنان شود که عملا در این زمینه ناکام ماند و منجر به حملات اسرائیل به ایران شد.
شهدای دفاع از ضاحیه و جنوب لبنان!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5443" target="_blank">📅 14:08 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5442">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea21582d5d.mp4?token=h4AIy-qCHMUeeTrKAGj4Pgq8nsX-HIKxOriuJxLRKa_kdyZZ1sKU8RUJ4AIEu2bTUYuvbkxURKvMPU8FNK0rIS2V9tNiIAAAR_q_Q-cW4YCz-wE9goJKtFaMoa6QUaHOy7ML8BmhxdCe6ojM4_2vsmWfV5E_kvUwTlwlis1Y9VzqH0mat8PS4SohH_-Kt16-lUeHLw6UAermSHX535g-O1gbRxjZ_Dxwp8krOeHqGWqnrHd-HSoLuUDCy3GcYg6vMl6wlzjWXF2se8c_pIkcNJ83pB7l4087jAMdAm-c-GOEMTkTW2yFYsd-zHdMBwb9ICEOS3BsJwWb36qqfUVvLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea21582d5d.mp4?token=h4AIy-qCHMUeeTrKAGj4Pgq8nsX-HIKxOriuJxLRKa_kdyZZ1sKU8RUJ4AIEu2bTUYuvbkxURKvMPU8FNK0rIS2V9tNiIAAAR_q_Q-cW4YCz-wE9goJKtFaMoa6QUaHOy7ML8BmhxdCe6ojM4_2vsmWfV5E_kvUwTlwlis1Y9VzqH0mat8PS4SohH_-Kt16-lUeHLw6UAermSHX535g-O1gbRxjZ_Dxwp8krOeHqGWqnrHd-HSoLuUDCy3GcYg6vMl6wlzjWXF2se8c_pIkcNJ83pB7l4087jAMdAm-c-GOEMTkTW2yFYsd-zHdMBwb9ICEOS3BsJwWb36qqfUVvLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏جنوب لبنان - امروز
‏حملات جدید اسرائیل به شهرهای نبطیه، حداده، الرمادیه و دیر قانون راس العین.
‏بخش زیادی از این‌ کوبیدن‌ها در جنوب لبنان، در واقع پیام به باقر در تهرانه!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5442" target="_blank">📅 12:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5439">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tGwt8ZTRybg0H8Pdb_gglVV1875--SFmsA9XyHBmJl20ZqaBqPZD3lS7tncnvuoxtUU07RP-GpaKQaAC0hcej0D_5rpy8z7xFR8dw1ygzVitH7ksqKvIDjxKQ-06qvCfzCU7TRgmiL235bmBM_sYM5WNnLNx_cLhR6ae_S8OT9MS9iXfKkxYQE-CO_oCEfINWfdIobMkt5lXUUIDeOVix6isK_65ruNHRav2iUsS_3z4bGsgP9hA3VJn76qO92WyZWZemddWmJeiKUSTBHsYgPLGo8lyQMg13r-QWC5tx9piC68Pnu_LaEL7qngCHoHXU7Cj1YUyLRLbOunfvWcGaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nd7ufvofioe9g14UJbroeQcJEufJuCGq4xQT4URjWKfFnhx2l0IX9oRJPgp_6bQBtyHe5SCVObBe8YXy9igvjU1rUtBAQTFCYPKS4I8prRxY6TSmEvEHn1h1j2ytxDdj4txtW0zjCXL7RYEuWatD0ArssGpFtKnh1SBUCV2Ms2R-lQjUZe-tTLdHDE_pEZ8e766QL3SIz8be4U8oR4TuzX3adGlepJAvFHX3EYY7Sa4gnsGWlRcQSmMK_256mf7IfM7_MWm1fcef1OCkwfXztUL6lW8sOWEZ6LhEi7jaKiz1nuHMpJeFmePzs-KO1z-RsCp2r7oBrac95GWlZPr2fA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874c401e95.mp4?token=qKvkyHY4Da9HurtBbWvX26JMTQkmSrEyA8PyDhA4x2bQNmhGAUi5OseFTGuskbAjceAHuu9cF3l9dfKwln6h48uCY18eot5PEMEuIlS8qn7OqufCuH0qVcLUVHn-dbv5vdvb8JAte0SGdjSBqw1d0dsGHoWgO5W4rleubMhHJdPfDbS81Eod_2Or1DoaTwvVTc_7WE77evIQ9GqahXYmsGckZ41c_TwT5Kxj0a4p3Id8yiWoP94vgzR80u6J4g3sJRtHpceIDI48ZVtPzANV2H6orLgpla3rGvh5IUQmpG8Wd69BqwQzC0Ypib8PyF3II1J4y-vvGUVXwMSbyXtAgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874c401e95.mp4?token=qKvkyHY4Da9HurtBbWvX26JMTQkmSrEyA8PyDhA4x2bQNmhGAUi5OseFTGuskbAjceAHuu9cF3l9dfKwln6h48uCY18eot5PEMEuIlS8qn7OqufCuH0qVcLUVHn-dbv5vdvb8JAte0SGdjSBqw1d0dsGHoWgO5W4rleubMhHJdPfDbS81Eod_2Or1DoaTwvVTc_7WE77evIQ9GqahXYmsGckZ41c_TwT5Kxj0a4p3Id8yiWoP94vgzR80u6J4g3sJRtHpceIDI48ZVtPzANV2H6orLgpla3rGvh5IUQmpG8Wd69BqwQzC0Ypib8PyF3II1J4y-vvGUVXwMSbyXtAgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/INb1sIOM3RI5qR6EuTodX_RYIafCefMFcBzbSZL5be1NsULUMOKa32p-sZc8tNApRfT8b14QgIZzCqVmDfRNmKm_R4pOT8Qg6yuyWYt3lBsVA5FK5ySTkE8MYKwxV2VuGjMoMgs2O7QC977lU5iydO5Ju79PRmStsmPMOCI9vAB9aiW07zuuddDyvFvL2l7vJacoTdhv1sddiTX1jSw7seOrs1tvUT4TXci9oh3v9qH1gHoQjkofkEAGDCAmAx9KVAawewqt3uVMnFgrXP55J_gg-47TtaueT5COWyWqYHS8Ew1sasSYJA2Pk5JxN5teN_IdyaIMyqEzWKRdlzF4QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/saXbYJvahpXghnSmc9aObidzPVI-IEEasmjYpec6Zc3fH5c74lrbvlJJ-1anP9iVYN28GN3i3H4NTMscfvi6YVcPlKu6PyNa_7h8j68oz2vTtmy8MTtQ-aTqVgDyP_kIs8b0zCHaM3pemr-UTYquDOWYxlnOOQZPMLvbNY4RawWJIteHOQBxDvrP_yu2zt9_rmtB5UcalK2soSiTfXSauWttZrzA1FAYtQa1gMj3CBOZpJku0dSs4_cnOewNblGUZQhUB98X4O5kVldssGxg_neUvMfehNuXhH0PAlwtgBa8YxDeIwYsgkVE7KSw3AF6cGmP9dWF09jT161-fkvILA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd790ae501.mp4?token=eWNdkR_FFiFGFP9heLq9GrL6NNRDcdWhCjlX1nbmpS2SMu3XQ3ddeJIqACx5p-Lj1TBr2g8s-KYIHYa8D64HxoLhBNyzs0E0jLXlRerJ_BM3bfzIUitINc8clt6Ze30ybW3CFI_NR_5jPnYOtJILo6mewyoOccYTUZ9PC5fGvOxqczE8zqtSNEvaitv7tyiO-moCM8WiTJCp4gb_d8f-ylScqcc6JtMPXuN8o7FCiWK5mNlplZasGymhyQl-8gqmJCZdb1xzC4A9X98nu6P-xJLCMEuqNI7PUGYtSDF2n94v0pYncdLYrMn92E73Xwtd2sB8Dt9SQYEm509hErl1vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd790ae501.mp4?token=eWNdkR_FFiFGFP9heLq9GrL6NNRDcdWhCjlX1nbmpS2SMu3XQ3ddeJIqACx5p-Lj1TBr2g8s-KYIHYa8D64HxoLhBNyzs0E0jLXlRerJ_BM3bfzIUitINc8clt6Ze30ybW3CFI_NR_5jPnYOtJILo6mewyoOccYTUZ9PC5fGvOxqczE8zqtSNEvaitv7tyiO-moCM8WiTJCp4gb_d8f-ylScqcc6JtMPXuN8o7FCiWK5mNlplZasGymhyQl-8gqmJCZdb1xzC4A9X98nu6P-xJLCMEuqNI7PUGYtSDF2n94v0pYncdLYrMn92E73Xwtd2sB8Dt9SQYEm509hErl1vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gK_j8-dVrjzm9DkCHQ-cldmHmWLDa1F9BLxirr97ghqwTSR838RO0UsuLUtcUwSFcZ4QYSsyesOCPVSenhuvcURpyTtL3W3Too_PIzsvVkpoLvIYCJyIW9qXibcLycuV2vyEXgIK3ktfJty-utkaxA_m-jFn9S62ZRyxZR90m5qlx575mpBytn5fNObaV6R7nbKkQQKvTh_iCVs9g3y7LAYfPBzgHQvziyl4iWsX2q7oas2a47eRHEHnPKJ6NKgV3w-Xc7JMzCexSSH3S5FkRM-rfYMzwZj58QqiYeOQlSGWinQ2EApGU_eUBVCvfU8fpYWwEHdROZcoTN2rMg6oHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسلمانان در سال‌های ابتدایی اسلام  به سمت «معبد یهودیان»  در اورشلیم نماز میخوندند.  شبیه کاری که یهودیان انجام میدادن، مسلمانان می‌گفتند  ما به سمت «بیت‌المقدس» نماز میخوانیم!  که این بیت‌المقدس همون «بیت هامیقداش»  «معبد» یهودیان بود.  جایی که داوود و سلیمان…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5435" target="_blank">📅 10:44 · 19 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
