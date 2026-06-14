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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 09:56:35</div>
<hr>

<div class="tg-post" id="msg-5538">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
حملات موشکی حزب الله به شمال اسرائیل</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5538" target="_blank">📅 00:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5537">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=KcVHTOyTn3MVGouuMMQGKMoHv2d-I2g80VrUGw9qUBnw_rnTJgZyU2TyS2s3jfRvKRo0LRDQBXMASCDD7Jdx7HSwHPPIwx_gdtargChd57G28MsMrdB7KmJPgeTe5OEnjN4HxUCFoD3pg_NLKHC9HwxETeHmTy0S2QaEN1-Km1ddEbAtXbwXHNbjxooLKBldj4UpVqgShwHYh_qO1K7B94_YkdXoo05mUm3hfKkNvxPs8pGab4RSDPAzTXwA_2zNNpbeQSwI5Y0jV-08rIpCCXv6i9Ga3WVxinHh2KJtTtNjbAOBqrWOAYNDBs5HMrbO4P3hP9jd1R44JkDGWAY7BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=KcVHTOyTn3MVGouuMMQGKMoHv2d-I2g80VrUGw9qUBnw_rnTJgZyU2TyS2s3jfRvKRo0LRDQBXMASCDD7Jdx7HSwHPPIwx_gdtargChd57G28MsMrdB7KmJPgeTe5OEnjN4HxUCFoD3pg_NLKHC9HwxETeHmTy0S2QaEN1-Km1ddEbAtXbwXHNbjxooLKBldj4UpVqgShwHYh_qO1K7B94_YkdXoo05mUm3hfKkNvxPs8pGab4RSDPAzTXwA_2zNNpbeQSwI5Y0jV-08rIpCCXv6i9Ga3WVxinHh2KJtTtNjbAOBqrWOAYNDBs5HMrbO4P3hP9jd1R44JkDGWAY7BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زنان کفن‌پوش ولایی در برابر وزارت خارجه و سر دادن شعار : مرگ بر عراقچی بی‌شرف نفوذی</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5537" target="_blank">📅 22:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5536">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5536" target="_blank">📅 22:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5535">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5535" target="_blank">📅 21:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5534">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxvMDMbyy1RBGs9z-I4v_VyISib2O9Is0Mg9Q7fvhfhE2irrbBeimiX-jY19R8na68_wfU2gGtblY78-BdkqjkiIq6xWrvwZI8VWf6FzBDuE8WISQoxtkRdNS8zCJ77OCAZTry_v_uONtBfcS05K95DHN33uTtU7fBc-FM2sbzdSFlKNBeVgH8zp7-QfWak-TNUDuYQfjHjTwlnJ3pxgtma5YeGYfqabv0AOZoQZQrf7bHjI0wvOAfjs8es8VDq4hty-oKoghtArPBPpiKBgfKRaHJ8x_aNkFJC_vsUxlHJZXaQXVIKvvsrlz45ifouYzzhuLeG2awBlrB54Xn9yzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: اصرار ترامپ
بر امضای تفاهم‌نامه در حالی است که مقامات ج‌ا  صراحتا گفتن  تفاهم نامه هنوز نهایی نشده</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5534" target="_blank">📅 21:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5533">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5533" target="_blank">📅 20:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5532">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lnoSkR-Rj9T4YzlAZkjvyNcX4JyPrVEfnqYg651mUf94GyN_aUlKjffCKg0V_cloFI8zkmrWe8NJkHlPy5deabB5F_J9AJgsiOz2qirxpyiC6Bua1xwS5smaHPj2MWtlEo302W0Krabf7eSAEa44xZczzREEUUiLhFCvMI3mPjxEfiKsEUfYHB-wW--RlWXxMPo16AX6SENU4HC73IElhqqzDvN6aCf-04cbUo1XX6_NaqMRfFVFdQmoq3tses3gOhdpQHgi3IblIUuZlUTQubywHQOaUBpX8hiB2YJCZcp7ObvtpqZIok_RJW2HYXamKQsSaTlKx5EocN9n0l5Tww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ اکنون:
توافق فردا امضا میشه،
هیچ پولی بهشون نمیدیم.
دیگه به سمت سلاح هسته‌ای نخواهند رفت.
تنگه بلافاصله باز میشه.
بعدا هم اورانیوم غنی‌سازی شده رو از زیر آوار
و خاک بیرون میکشیم و نابودشون میکنیم</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5532" target="_blank">📅 20:32 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5531">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPPeYhVF2UVVvidUO1MTL_kc03ielRCXbZTP1c_rP6iRd69Pzw0outZj2adyL2jSZsdCBohZVt_0Ej1sElyoR7I2ijoRyKTxSpqvIMr_0Pb7omZ6IsBzU0RP_V93Jh4s3M_OBm9BN4mCcOd27tB-7jmMnsqnJpk9C-1LBbvrc_-hn23GZ_QR1miAUDF0sA8--hjtLY2rrnh0WncA7In4L4E6uoet7G-vGKBvzuAee62vVpYH2e1sV_iYRJ8zT48SfzA5KsTlQa8geHN-XeCRp8KGRHiendeqhm8CT--q9srjBnLtxql5yY_ib3pKWa5CiY4qRwoda_ZZfPnIjCZc_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیسی خطاب به قالیباف نوشته.
نگذارید خط تسلیم و سازش با
قاتلان خامنه‌ای به ثمر برسد.
(نه سازش نه تسلیم - نبرد با آمریکا!)</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5531" target="_blank">📅 20:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5530">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-L7b5G23Cku8i9d7JEgr3RmzLg3LbwLLzYHZMR06_sUHW80ZZG3uJXy4aVeT87H7syKRFjcMiHaY2tf4v288gD7fK7aVOK4tAMSOWOgo_0BFmgK3ZFmHdv6ulPY7cD6XT-9yWZAX1gtl1JksVfdCCZ6Bn8OIXZu5w9a1Foaci3kgozHAB5Td2393qVlgSSG_n22rhlFfIEosLhzETj2-FwsujX5WdczYUiBwAS1_AbXOVwKvD5-YfiDOhXg73eG36c-OFkQr6sw66VX7xEOCqzzhXPg3s5ZYCRNIY-gJvCkti8apDRuqVdkYEVeXbYAi09shqWYrQxHfwDKXLrkUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوسف رجی  وزیر امور خارجه لبنان:
«حزب‌الله یک نهاد نظامی غیرقانونی
و بازوی مسلح جمهوری اسلامی
برای بی‌ثباتی منطقه است. اقدامات حزب‌الله، لبنان را وارد جنگ‌هایی کرده
که هیچ ربطی به لبنان ندارد.
ما فقط میخواهیم در یک کشور عادی زندگی کنیم! نه اینکه همیشه در جنگ باشیم.
مردم ایران گروگان نظامی
تمامیت‌خواه هستند.»</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5530" target="_blank">📅 19:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5529">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">نخست وزیر پاکستان: تفاهم‌نامه ظرف ۲۴ ساعت آینده امضا می‌شود.
عراقچی : برای ۲۴ ساعت آینده هیچ برنامه خاصی وجود نداره.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5529" target="_blank">📅 17:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5528">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5528" target="_blank">📅 15:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5527">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMPBtqaOtaiRMApZXl_vXIJlLK9tl7hjDM7I_6x-HEwFq5Gp-k-TfR_TkGqVQxNrz61l1-InDzVwWD4oouL2PNhzz63sqOhG41d8FLE2YuQ6eT3wEdTr6GMllIwWN9IsSBq-ELmGxdHYTmlPwlgpqmhzm3zBm-oyN5sDwprIa2ZxBi0_3rvtSyjpwOi3OHYNVvumG3exUqQoDHs-Cfrd3vuw1yxrXHV-e5T-t-81bpvo4wjZQZg5Di-AABhnkgBTKFKUaBtqfbtoZseSXZ64nYBk93NW-uXFilZzCC-WFSQxwIeEkQgTKNd41Kj9Pu5Kifj1qvZlKSRZAIO7jOlEjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی در باز بشه می‌فهمید
مجتبی خامنه‌ای در واقع همون قالیبافه!
چیزی به اسم مجتبی وجود نداره!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5527" target="_blank">📅 15:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5526">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3bW5-znPUbz7T_mEDYd2u34_9RLx4tJs5lx_UZLZ7157rPzqG6sdXxE2NIZpOKh4Kq0279xNU5Ph-uRr-kXi4gLYbhWr5OfDzBssxAjDQb2cosaVWmVbUXMkBiEcUITjqwsZld5Mu7J6KgjL9a8THz3jNRGQ2Fc33y3Pz1EtH2HAQWDALmncL6NaDO_MjYfg0IMR2989zIUeqwHDxzjjj4DeobnB_-pMoyQPogMJf6ozbumqfmq32CuVquLDhHrXS0qrOwXEUz5CcNxR4W1dbUhmSeDxNVn5jbojfWjY0RJ6u-7HmRbQIWFM_mQgf5_AW0AMXMLGaLlkVC8E3qaLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : ارتش اسرائیل دقایقی پیش
به حومه شهر نبطیه، یکی از بزرگ‌ترین شهرهای جنوب لبنان رسید.
اکثر جمعیت ۹۰ هزار نفری نبطیه،
از چند هفته پیش شهر را ترک کرده بودند.
بعد از حملات موشکی ج‌ا به اسرائیل،
اسرائیل فشار بیشتری بر روی شهرهای بزرگ جنوب چون صور و نبطیه و….. وارد کرد.
ارتش اسرائیل فردای حمله جمهوری اسلامی
دستور تخلیه شهر صور  - بزرگ‌ترین شهر جنوب  لبنان - را صادر کرد.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5526" target="_blank">📅 15:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5525">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hvlyJ8uC6t3SzPtwYFdFwkfNQ11cYhD1SN-g5ZOXQh59YKzFG_gU_u78Qfa5HtIVO0-AjpTDnWNIka4wC9MnTPYANCQBwqYDzBhAjiUO7kHkpBau4Nx08SfudOWeTsCDy1o13GjIZbeo03bEzLuZ5I16uBpD6sge8_wnhgavG4D6XDeqxD8QIT2o9NxvFyHbtJY6oR5kQSF74yUgdaFrT6tyTiWAxkYGLpxWPe8_Ad9ARHXsNFkQDy-g2ItCz6udqiXqb6v2rvvK-gTjx82UnOLh4b4SzudLnE7F5piWNLR8n6DglxayQw9S8TLnYN5NIcs5UunfW5UhCAJOP5kKvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیات مراسم تدفین خامنه‌ای</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5525" target="_blank">📅 13:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5523">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/btJvpq53TuFLqFLcPFEWQzZ5BmWzTeHub4R_sIb5TV9Flme9zlAeGlwO8MtRoNVtsqlGf0GVikyR7CaVhT1eR3UResWxl-3UYJfx7x6ZU1-9gqlMoXWL47zBaVGE8vuOpKboqUGwuxIImbWZFXwJeImtFjgV5jRGCWeD5OrSehOPqG_c4iXjdpUHCojxYIW_MzKOMPJmI9hwk-B43R0XPPGcFFayi78TgnMjwA8CS-XU2FbSWAynrhlKOuLE4XaJ1V4nmzjNUafL_ZM6itAWXFw-Mr2O9c376cF9JSLybLB2Mnuv0KUBp0tg4eILsYiUc9RJDJfdn8-7pKiUwtEXIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a9cd24845.mp4?token=nbnWplrITpTJSizK2Wv1HnADWBxQuyQDihxnDNyvMV45pJdK9pQgovuKywL-ND8vdZIQ3JClYv8BYQQ1Ezkj2xsjs5_y0hzbVXaHK6jKPUv16Ny2fuQ91IkGklTiXjz-d0IIbcQ-za6ZfEQt5n35sOlJK76zdNuY_a9rgf6HGI6wpVCD4VsdpTJMGvEbBSyJQekSnYgoO8_HEB5E2zllV0n3CkdSOJGChQ9Y-MWVDzmBimGhQiMXKd85eU9sgq10I9o9uiThAhRk09w_d8vjwjmE6h1UMLLMHIbxjac3wiqB9bX4Xj0RLxOVBinye9TO8aiyosBqSUwaMkN3be-kaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a9cd24845.mp4?token=nbnWplrITpTJSizK2Wv1HnADWBxQuyQDihxnDNyvMV45pJdK9pQgovuKywL-ND8vdZIQ3JClYv8BYQQ1Ezkj2xsjs5_y0hzbVXaHK6jKPUv16Ny2fuQ91IkGklTiXjz-d0IIbcQ-za6ZfEQt5n35sOlJK76zdNuY_a9rgf6HGI6wpVCD4VsdpTJMGvEbBSyJQekSnYgoO8_HEB5E2zllV0n3CkdSOJGChQ9Y-MWVDzmBimGhQiMXKd85eU9sgq10I9o9uiThAhRk09w_d8vjwjmE6h1UMLLMHIbxjac3wiqB9bX4Xj0RLxOVBinye9TO8aiyosBqSUwaMkN3be-kaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5523" target="_blank">📅 13:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5522">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">عراقچی : در دو جنگ گذشته، «مذاکره» منتهی به جنگ نشد،  بلکه «مقاومت»  منتهی به جنگ ‌شد.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5522" target="_blank">📅 11:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5521">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5521" target="_blank">📅 09:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5520">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwyBSdE-TplReEiPuf4ysgIWqcVSBlETdVp2hjSbvkvMAApbrdjajnOY8TQzbA_UBhCGHIBOUWps9uaFUvlf3UfSa0GgcM8yJt4wOleRHhWaVQAuzl2OWU0yrYozSxiZdAVwPgS-WiH8ylPBG_Ehqsr4yru50YRBDvuTTqARsdHl-KwugRr7c0fiSz2RcHLwcGoXOJpqtQulo64kF3jGCtmuGFedA5jOhGy4YQVIz-lp9vx5sfxpiLY0Bl18CYHNYx8xrYpDdeNkkBA60YeYX6DHcVo0IRYZRhm_LF5Hzw2eZxuNzuN21sqbLck21LLF_u5aN_AjJtIjw7ktcQstzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5520" target="_blank">📅 01:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5519">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=bYoB7uiVgGbi9ZYGvrVY27NLU6Moh42vrV_PXTu7l9D8ZpsOHc9scN0cIp8g2QwOtDzAhExjHZJRTkPFOyQSXYtHsx9k9fhCTEqp_BGtHPMGYIfKR8U5NiZf_9jUIElLT30jm-Tilh-PVktsXxP09fcwX9sYTL5NPoUcQRl9xvnCiDLFJ6sYY-7LXT-eAsj-4RQoRFuXwrK17dXdhsAzdWt7hRyEMnzsA_Rr_d3kg-BhBONvFqNodYcu0dGNI4yd_OlqgO8HrH6I_V0u0gl7ns_VmwQn5PX2ZYQDfU7Ct2EK5UZLQCWI0nEf2HN5obiVF1xy-4V4R_g4OyKFEnZPwUsxEsE-cXyg-Yje2753j1NbRc_I9li4N8cROtlyUyzerP6u8G5QizKfzLSAM00C1NFRrURxzcFGKUvujW04y6LI6GtWgJvCXGunxo7hF88MUN1bbQBliEjRc9jDcAHquh8Jy17d3ptDw2QVDCwB1ffTXqUMPzjRnbxrcygXVVRWjZlQOFKUxCW7aH34dOYJOSM2D-8HMn61Is3x2qb1EiE2tOoskVQTmTkzmS2EVQNX8pjHPizMAMqF-mKbBeneX88XdmVB2x5fXQr3ppfyQfXD4Sjvu9vsRSbg8hsZhjc1PxKbCLSfKQleSl6JjKk9L9odYIze-SC_25kJiqhQyhY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=bYoB7uiVgGbi9ZYGvrVY27NLU6Moh42vrV_PXTu7l9D8ZpsOHc9scN0cIp8g2QwOtDzAhExjHZJRTkPFOyQSXYtHsx9k9fhCTEqp_BGtHPMGYIfKR8U5NiZf_9jUIElLT30jm-Tilh-PVktsXxP09fcwX9sYTL5NPoUcQRl9xvnCiDLFJ6sYY-7LXT-eAsj-4RQoRFuXwrK17dXdhsAzdWt7hRyEMnzsA_Rr_d3kg-BhBONvFqNodYcu0dGNI4yd_OlqgO8HrH6I_V0u0gl7ns_VmwQn5PX2ZYQDfU7Ct2EK5UZLQCWI0nEf2HN5obiVF1xy-4V4R_g4OyKFEnZPwUsxEsE-cXyg-Yje2753j1NbRc_I9li4N8cROtlyUyzerP6u8G5QizKfzLSAM00C1NFRrURxzcFGKUvujW04y6LI6GtWgJvCXGunxo7hF88MUN1bbQBliEjRc9jDcAHquh8Jy17d3ptDw2QVDCwB1ffTXqUMPzjRnbxrcygXVVRWjZlQOFKUxCW7aH34dOYJOSM2D-8HMn61Is3x2qb1EiE2tOoskVQTmTkzmS2EVQNX8pjHPizMAMqF-mKbBeneX88XdmVB2x5fXQr3ppfyQfXD4Sjvu9vsRSbg8hsZhjc1PxKbCLSfKQleSl6JjKk9L9odYIze-SC_25kJiqhQyhY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی : در دو جنگ گذشته، «مذاکره» منتهی به جنگ نشد،  بلکه «مقاومت»  منتهی به جنگ ‌شد.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5519" target="_blank">📅 00:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5518">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=t07D3r71x6txw8xmKdak6SdiaKbrBPfDKhtMtmNI6zY3ilmZ26dH_qTzMVSfNkfPQlaP8wvbVb7Lgy9uE0dd49h2S0Jto_XqsXtV43NKdFpCghr3U7HPsVNoleG2mOvZEKO8cWUYdpnRJGpy3PMZzpodYSHnIvHLM2XobmufDLCDgO50ni7QH6ASuT5MnTRWMGYuLLgSqDeecNrhsSo1siU834PnoycPv_zivP3p0W9trmmkjqX9YGFBLWgBB6b74spmrcr4wt9K2lKhoOVML0jWYYHQH8F8KonQHP2jzC6SIqHZPcCbrQLOmbAL86W2hZIorjejiFUq44FaAAkejQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=t07D3r71x6txw8xmKdak6SdiaKbrBPfDKhtMtmNI6zY3ilmZ26dH_qTzMVSfNkfPQlaP8wvbVb7Lgy9uE0dd49h2S0Jto_XqsXtV43NKdFpCghr3U7HPsVNoleG2mOvZEKO8cWUYdpnRJGpy3PMZzpodYSHnIvHLM2XobmufDLCDgO50ni7QH6ASuT5MnTRWMGYuLLgSqDeecNrhsSo1siU834PnoycPv_zivP3p0W9trmmkjqX9YGFBLWgBB6b74spmrcr4wt9K2lKhoOVML0jWYYHQH8F8KonQHP2jzC6SIqHZPcCbrQLOmbAL86W2hZIorjejiFUq44FaAAkejQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت نبویان از متن توافق ج‌ا و آمریکا :
یک : طبق متن تنگه هرمز باید باز شود.
‏دو : تحریم‌ها برداشته نمی‌شود.
‏سه :در مسأله هسته‌ای مستعمره آمریکا می‌شویم.
چهار: آزاد سازی پول‌ها اعتبار ندارد.
‏پنج: هیچ ضمانتی آمریکا برای اجرای بندها نداده است.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/5518" target="_blank">📅 19:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5517">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">وزیر دفاع اسرائیل: از جنوب لبنان خارج نخواهیم شد!</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5517" target="_blank">📅 19:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5516">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5516" target="_blank">📅 19:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5515">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5515" target="_blank">📅 19:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5514">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
عراقچی : هرگز تا این اندازه به یک توافق نزدیک نشده بودیم.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5514" target="_blank">📅 18:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5513">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SnFk6g8huCeS_yZH1iKrfzaWJDTUN5NScSj_Pcx0UiafMnxeik3VKp_SstYPTWhCeERB2hqQ2w7x04ouYBfw9v-456aUVNqOXu2Lr_RFF8oasriuYz57-ggdhP_jUvfeezSNEyzb6F0clvW_RlC04y9Akt3CzRXBDxJkKc41tXI3-eaxsLnbjNfT6H50X2vuReb-tq0t_pwO0VhpuFVXskwja-1V2XPgdfaeqbp5FmYfKRGdMRU-YuGCgV5XX_KlgTUJ9gafVVigNrszIpz5XuA-oyRqRccViLWTqhgY7GnMSkwrkbqpX8MUBJ0NyGaspUwrTdwWHqKGbCxHjdS75Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ : این مواردی که جمهوری اسلامی منتشر کرده دروغه! اینها یه مشت آدم بی‌شرف هستند، اصلا نباید با اینها مذاکره‌ای بر پایه حسن نیت صورت بگیره.
حواسمون هست که دیشب هم با پهپاد
به یک کشتی هندی حمله کردند.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5513" target="_blank">📅 18:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5512">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=qAJv3NofQKjJSNhXtQm-k6FJmwhSpBjQBdeo-UMPx5Tgz-5UuklYsAXgh_P3gk4EGtOoIF8st5Pohf2scrQqbb5RywzNblZ36MtKHCtQXvDjyZ340y9G36irdo-5WKtADmrYXznaKjh2Qjh6R65bLVunggX-TGxKU5IRJY5hDx_aKNWA6v64ELIU5Z68VZ24K0lk9g8IzC6GF_6ChIdGOogEEUFPnm8Zbu0F9rHobPeqAkjVaLrnFaNZlhBjnsVYexNRthDG1VUV7qWZI_2K0IVbPvglmwSpvwp5VjFw6AxoSEJaqnXTrQoPqgdwreJVMiaSXDh-jLvWMpXmuuFz5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=qAJv3NofQKjJSNhXtQm-k6FJmwhSpBjQBdeo-UMPx5Tgz-5UuklYsAXgh_P3gk4EGtOoIF8st5Pohf2scrQqbb5RywzNblZ36MtKHCtQXvDjyZ340y9G36irdo-5WKtADmrYXznaKjh2Qjh6R65bLVunggX-TGxKU5IRJY5hDx_aKNWA6v64ELIU5Z68VZ24K0lk9g8IzC6GF_6ChIdGOogEEUFPnm8Zbu0F9rHobPeqAkjVaLrnFaNZlhBjnsVYexNRthDG1VUV7qWZI_2K0IVbPvglmwSpvwp5VjFw6AxoSEJaqnXTrQoPqgdwreJVMiaSXDh-jLvWMpXmuuFz5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات امروز اسرائیل به صور
دیگه نمیخواید بهشون کمک کنید؟</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5512" target="_blank">📅 15:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5511">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
رسانه‌های حکومتی :
جمهوری اسلامی کنترل تنگه هرمز را رها نخواهد.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5511" target="_blank">📅 14:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5510">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qP2SDBDy21EsUvkYHHbjYeplxDI5nTG57p64YiSb9lM56itDEvthLTi-2H9GHAmZmR4l_21TRKbwoUoEHGA84kAiD6tIp4iZvNB1XHT-CjzIHG47MX3ctPZOZuyYd1lYfKZUATv-UUWs7uNLWXCbAk8z3vNxEeqn9mWATfz9Fg1IDjXz3dZ8sjaabfqijSK70g9s0f22pz7AoTslD5WCvyc7rFiXF2ZNEnKPzQUpfQ0j9wgOdv9jYUhra57ZkbaM3Zh_CCpg3Zm5JO61nnHePbSV91hg8hAU3hV5by-JlVLFXnllNEPgSfg-KCmSaE-ebxu5MjJa6egKkrYUj2T8Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
قطر خود به تنهایی حدود ۱۰۰ جنگنده بسیار پیشرفته دارد. شامل ۳۶ فروند رافال، ۳۶ فروند اف ۱۵  و ۲۴ فروند تایفون.
🔺
بریتانیا برای حمایت از قطر ۸ فروند تایفون در این کشور مستقر کرده.  قطر همچنین میزبان بزرگ‌ترین پایگاه نظامی آمریکا در منطقه است ولی اجازه استفاده…</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/5510" target="_blank">📅 12:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5509">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/5509" target="_blank">📅 09:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5508">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=shu_gcIU_RRPtnPP8d12AM5qvg7Wl9L5H2-Q8CcqhGxoVneGkwzZTO-ctzz6rnFOanRO05j-NJHdSVyNZA0fYuHxHZQ_CdwVsIDiDFMekbZ_Tn4jfLMDftosPaHGX5WGTCc3kQV1XSWiw_XBYbjCNLBp1LvWXwvS4CAKfsiTGefmJR05OIwXq4hSd6wSsaG4k1lizghvfEktNpEzelkqmsYmSnHq2FMlhNYTgKhNZ7vcMbMO8JPssAVAWEzTBKCwLzLWgAT657GaGR0OHitNzTb4wgLZFtRq38nmiadUSflRtDi-GxGY7XKR9BA8N1keL6CwmaDEjg4PwDpAg5EnIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=shu_gcIU_RRPtnPP8d12AM5qvg7Wl9L5H2-Q8CcqhGxoVneGkwzZTO-ctzz6rnFOanRO05j-NJHdSVyNZA0fYuHxHZQ_CdwVsIDiDFMekbZ_Tn4jfLMDftosPaHGX5WGTCc3kQV1XSWiw_XBYbjCNLBp1LvWXwvS4CAKfsiTGefmJR05OIwXq4hSd6wSsaG4k1lizghvfEktNpEzelkqmsYmSnHq2FMlhNYTgKhNZ7vcMbMO8JPssAVAWEzTBKCwLzLWgAT657GaGR0OHitNzTb4wgLZFtRq38nmiadUSflRtDi-GxGY7XKR9BA8N1keL6CwmaDEjg4PwDpAg5EnIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاور قالیباف:
دو نگاه وجود داره، نگاهی که میگه بریم صلح کنیم، بسازیم، یه جوری مشکلمون رو حل کنیم.
یه نگاه دیگه اینه که صلحی در کار نیست!
ما قراره با اینها بجنگیم و قراره اینها رو تسلیم کنیم در برابر اراده خودمون.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/5508" target="_blank">📅 08:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5507">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=I4rRkdQhPCPBCZ3k-Psd6HUdNlFB2y8DZfX7T2frGGrh0lk0UuifJETiTvdfGOGQHY2-taNzpsVlj63rECbmzzm-ls9NaFhwZ8BK_UIEyB5sYmlYQrw4J7bYRSvuorTP-bwLXD15LP6wcC1v8liE6o6B7s_ctfCuhrQPnKB2Rpj7O8ahky-xWhON0mCUdfo6FeNivuNDtZxNCls8stqRydhKIE-BCcl8pRqv3utLVJC61GIm9TFvs5ZSjnQkNWyfwTL36PzRaNfgHKK37bk988xevYhQA7kRIS9umtGtW13OsZFfZmUtgg4GQUzXZBODDYpsc0dn68KVERugxeHCUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=I4rRkdQhPCPBCZ3k-Psd6HUdNlFB2y8DZfX7T2frGGrh0lk0UuifJETiTvdfGOGQHY2-taNzpsVlj63rECbmzzm-ls9NaFhwZ8BK_UIEyB5sYmlYQrw4J7bYRSvuorTP-bwLXD15LP6wcC1v8liE6o6B7s_ctfCuhrQPnKB2Rpj7O8ahky-xWhON0mCUdfo6FeNivuNDtZxNCls8stqRydhKIE-BCcl8pRqv3utLVJC61GIm9TFvs5ZSjnQkNWyfwTL36PzRaNfgHKK37bk988xevYhQA7kRIS9umtGtW13OsZFfZmUtgg4GQUzXZBODDYpsc0dn68KVERugxeHCUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی ظاهرا متقاعد شد که شرط و شروطهای ۱۰ گانه‌اش رو کنار بگذاره.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5507" target="_blank">📅 08:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5506">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">صدا و سیما : شنیده شدن صدای دو انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/5506" target="_blank">📅 01:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5505">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
ترامپ : توافق با ایران باید همین چند روز دیگر امضا شود، با حضور ونس و در یک کشور اروپایی.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5505" target="_blank">📅 23:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5504">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
نیویورک تایمز:
مدتی کوتاه پیش از آنکه ترامپ حملات به ایران را لغو کند، با پاکستانی‌ها که با ایرانی‌ها میانجیگری می‌کردند، صحبت کرد.
به گفته یک مقام ارشد دولت آمریکا، پاکستانی‌ها به ترامپ گفتند که «ما با ایران به توافق رسیده‌ایم».</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/5504" target="_blank">📅 22:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5503">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، به نقل از یک «منبع آگاه» نزدیک به تیم مذاکره‌کننده ایرانی گزارش داد که رژیم در ایران هیچ متنی از توافق را تأیید نکرده است.</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/5503" target="_blank">📅 22:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5502">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
اکسیوس: ترامپ حمله را لغو کرد، چون قطر گفته بود که به یک توافق رسیده‌ایم و فقط مونده امضای مجتبی خامنه‌ای، اما حملات دو شب گذشته آمریکا،  هم ج‌ا و هم قطر را نسبت به نیت واقعی ترامپ [که جنگ میخواد یا توافق] دچار سوظن کرده بود.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/5502" target="_blank">📅 21:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5501">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
ترامپ : حمله برنامه ریزی شده امشب به جمهوری اسلامی را لغو کردم!
گفتگوهایی با رهبران جمهوری اسلامی داشتم.
محاصره دریایی اما همچنان برقرار است.</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/5501" target="_blank">📅 21:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5500">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
ترامپ : هر شب بهشون حمله می‌کنیم، تا اینکه به توافق برسیم.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5500" target="_blank">📅 20:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5499">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">حمله‌شون هیچ کمکی به لبنان که نکرد هیچ!
هیچ ضربه ای به اسرائیل وارد که نکرد هیچ!
فقط یک پتروشیمی در ماهشهر از بین رفت و اسرائیل فرداش، برای اولین بار دستور تخلیه برای ساکنان یک شهر رو داد!  صور!
دیگه نمیخواید کمک کنید به لبنان؟</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/5499" target="_blank">📅 19:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5498">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aYNLVO4O-Rz1VdTQKNJyiM0fGyXLmIOb_qmRAXqN6GJ6NxgJWG6B167aT0ToDIs53NTFDNldBzfdjXuVXIsuNCL_7YC-YL4CDbQ09N1h7HGnvrtqpw79Gn4uOZuw7YiKWvkc6dDDHUqe8djXtBVBz99VSinEynIAztGRSWGZWeblpsztgObQjRJAwSKPLWX6JAVKgNtY4DpTCJUHivIw6XhR32Lf94Bg_8tREYmZJ4Ub5phQcr0APmeg6v82dQPZ6fSZva4BDziaIEH0ZHZkvBmP0OpdxC8DPctv_F6BBev8Ifh3wsLl2R-FJRdgpx838zf5IizXCOIY0_rxivCmdg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=EHfmwexZYcIx0kPyq5U8gvNAkbODOTP-SxsjS4BpB5tM3Pfc1OIkqBmNyXis73iRyU3SDhmU1v8thQF-q3hsyU4kui6JZNPLKPd4J1rIEyEO5uKLTZKEttLvaZPqvFug9JatjaKrIfIybEC_Hjb3cAOn1FE5LlycJUEt1sKxqOy6BOAm19OtKKWo5ZXPkn11H8VT84YuibKofNEuroPNxcX1kNyNQiVn44p37mAG1yYMW--dp6VbjocfucMes9rTVXMlsN3lwK5RPNMboRrxZvsktXzfflIa7dm9NcbPKFlcCLCeHU_kLSH2q6CSgVqfWfa-0YtbgesMnDu5xxFfRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=EHfmwexZYcIx0kPyq5U8gvNAkbODOTP-SxsjS4BpB5tM3Pfc1OIkqBmNyXis73iRyU3SDhmU1v8thQF-q3hsyU4kui6JZNPLKPd4J1rIEyEO5uKLTZKEttLvaZPqvFug9JatjaKrIfIybEC_Hjb3cAOn1FE5LlycJUEt1sKxqOy6BOAm19OtKKWo5ZXPkn11H8VT84YuibKofNEuroPNxcX1kNyNQiVn44p37mAG1yYMW--dp6VbjocfucMes9rTVXMlsN3lwK5RPNMboRrxZvsktXzfflIa7dm9NcbPKFlcCLCeHU_kLSH2q6CSgVqfWfa-0YtbgesMnDu5xxFfRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‏سی‌ان‌ان:
برنامه‌های نظامی آمریکا برای تلاش جهت تصرف جزیره خارک ماه‌هاست که تدوین شده، اما به دلیل این که این عملیات بسیار پرریسک تلقی می‌شد، پیوسته به تعویق افتاده است. این خبر را یک مقام ارشد پنتاگون و دو مقام دولتی به سی‌ان‌ان گفتند.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5496" target="_blank">📅 17:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5495">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YGKI4cl-zPalqQSSLQCj39ENbT-wSCFK57TbzT72eEw04bMcUizT6SWvcfXfB1GICJC0sCybVu-2K2HKLLpgbWxh185srZT4u8Di9s5I5p-Jvc19rQV_IeoroaUQ4OBxa-YqHxMo-vbnr6AbXw93ejvBg1Cbd0s4yLMNo4dL2f4z1Nixa1_jIU9MqmbIX83XdXSa3FfJpfWB76ykqATkfmZUKqKy_gM2xSCCVGERgfRaGpOQgnc1HMqRobkgJaQgLeZwNKm7qFIzd1fsYG-1JcY0NYNSfBK-Ojqx84dlML6dwQAf9eOqAHkcNJRH5rlx3K98NyiPcQ7ws47XMoM-CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه داری آمریکا : خسارات وارده به متحدانمان را از حساب‌های جمهوری اسلامی جبران می‌کنیم.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5495" target="_blank">📅 17:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5494">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ترامپ دلخور از رسانه‌ها :)
‏ ترامپ در گفتگو با فاکس نیوز:
«‏ آنها دارند با ما مذاکره می‌کنند تا به توافق برسند. این کار برایشان سخت است چون آنها مغرور هستند. آنها بسیار مغرورند.
برجام جاده‌ای به سوی سلاح اتمی بود. راه من جاده‌ای به سوی بدون سلاح اتمی است. می‌گوید شما نمی‌توانید سلاح اتمی داشته باشید. بنابراین آنها یک روز با من بر سر این موضوع جنگیدند، و سپس با آن موافقت کردند: شما نمی‌توانید سلاح اتمی بسازید یا خریداری کنید. بنابراین ما همه چیز را به دست آوردیم، اما رسانه‌ها آنقدر دیوانه‌وار پوشش می‌دهند.
‏مهم نیست من چه کار کنم، رسانه‌ها خواهند گفت این یک پیروزی بزرگ برای ایران بوده است.»</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5494" target="_blank">📅 16:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5493">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IKCEtadEjL2lSXv06Qy-P9aAStKqWpmzXE3G9zOfxD10WkkeE_aT1lSZubFYZdJ8oQN2P1vwheSn3gIJOAVZmVsvdJJlKfxqOWxxgazOSi3cbgSUfldy5j6hpT0jN5Ubdj8WiCYhtAX-Hkq8Kq0V7oR2FDi3T1zzmJuYp4NyYogXCd9OzVk-4wvWWS2rVOjBykcJ8_9k5yG0B7yUDKu_JpI09HRSArhSQo14BWA7e0R2LLQG1HY69yXbqArzZX8VIsbn7FXHqnIqtd4NjmJue3f0SRPr2DWc7pJiaqq1BaSg0jaobpulFx--HNDfQt_4YNvIeUXFx2VHgH9OfrvM2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از انفجار در سیریک
مناطقی که در دو شب گذشته مورد حمله آمریکا بودند در واقع حاشیه تنگه هرمز هستند.
جایی که رادارها و سایت‌های موشکی و پهپادی و…برای کنترل تنگه ، متمرکز شده‌اند.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5493" target="_blank">📅 16:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5492">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrWaYR-4z3g-A7o_U18FpRGS3k56ct3DJRoBwbkOniDNIC9KbtkFwBtmz1-9L3r8k_x1NINdjc7O6y49kSEf3n7ss6qVRWtGbYfttVh9LQr8sQlgAnKSt-BNXImcYUECy_vc2BwCnzW5YuIZ0oKjK7iN3Cqje1fvRm5kxNZY1v1rWGZREl76DXrJkqDY25ut5z8QQVYyd-69y7ewAC66WAjVDBG492kuBPc-UUGoOx58ts1JXXoilYsYuyZhZD96w_2oLLdSXwF7BiRAEs2hSUl9ue513VlAEyZbDg5JtZVnLi9l8MnDAMoMmuMDlGLZLjZZhISWayzNC5OjURmN1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اموال ملت ایران! که یا مصادره میشن
یا مفت فروشی میشن به چین
یا غارت و دزدیده میشن !
بقیه‌اش رو هم‌ میدن «مداحان»
و «رجز خوانان»!!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5492" target="_blank">📅 16:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5491">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cTgkezvf4TFx8wWTkDqxz1U-22lC_Zwgwjyb-8iO3i6LRIYR0lLeOQGJlma2Ff7NeTN4fi-BmwMqYqMHF7eo3y97TtfE6JKNLcdgcnXzgpQTktYHb_hVwLsxPn6u-F1-cvFq2PVwHKvLVQA4DJ2_YtsAYzT7VcRPSROKqPYcvYvb-Zg_hzjV5DOjPzKC9vEknMif5Zd9_iBbpk3RuLEFOmegBdwdnRGYZaQX-ZAx0GGHzkonhaXm8P9aMeXXEbbI5ol4LeMyYPVIlMZXkeFlOohyXYVXxyxNItBHSaWCst5YESN07SkX7e4UWXLpPwIXKYHLncAw-J0vKphhaXJNZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5491" target="_blank">📅 16:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5490">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQAlYD0jRCRgPrj_TlzYyawGMhiZUhN8iCpwZXqvDEm7Hp5Wh4CQ8wS9Acl8dXfP768_UOf5zMsIV6EtAr_bqhlm59YSJn3t1kYxygJHCI5ForH47-2sXkPFkWuK7y9FlNVJgYbRseH2-13Max2i4LBFNbe5goFIQzkVse6zO4Rb23pwoKSDtpc38NDs7nOlv26kATsMSjaUJbeUPIcEGrNwi6GqNJLnd0178TZth43Chh6X2ouCAcaEEm2VEaKYimkdn1YKbYfEu2awroRCrI1Tv_Z9LsClC04BVRtdd8YG2g_8SRBXUirY_xou4o76xAWlkjVaYGNPmpOS3C_Osg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5490" target="_blank">📅 16:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5489">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">بیانیه ارتش اردن : شب گذشته ۲۰ موشک شلیک شده از سوی جمهوری اسلامی را رهگیری و منهدم کردیم.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5489" target="_blank">📅 15:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5488">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">بعد کار به جنگ ۱۲ روزه کشیده شد در ۲۳ خرداد ۱۴۰۴ ، که دو روز دیگه میشه سالگرد شروع این جنگ.  اسرائیل، آنگونه که نتانیاهو بعدها گفت،  انتظار داشت که در اولین موج‌های حمله چندین جنگنده‌اش توسط پدافندهای بومی و….. ج‌ا سرنگون بشه اما نشد! اسرائیل حدود ۱۰۰۰ سورتی…</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5488" target="_blank">📅 10:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5487">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pVCoFXBkkCYOPULrrHm0IcYl22WUriThmNGG3JLlF22xrUAWDwJgULOudEQ8z-LjYZrpNndu6fYS4Jd0_pXx7ybz76RQ2KZIuUin3Z9y-58BVNQVtchmp38_C_jSfmI8r4AhdlAV63j_8AOjDpqkzUxLXlW6U5XxfGD_6Cs23ybS2Gdr31k8Lm3_gYn1FA9WWGnt--qttXI3ONAJVY2QaT2m5KrKV_rNa2IWoPreZLeqzfWIQLvlSkTMo1l2SDI5t0x0wDaAQvtb9iBs89qSZTRM5UdnLv1qN89b73dL1YKbAipdaQ72o1y1_5V4PbiKTl7W0NDlT8anlmfalihgjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پاسخ به حمله مستقیم جمهوری اسلامی  ۴ روز بعد اسرائیل حمله‌ای بسیار دقیق و هدفمند به ایران انجام داد.  گران‌بها‌ترین و مهم‌ترین سلاح دفاعی جمهوری اسلامی رو یعنی سامانه پدافند موشکی  اس ۳۰۰ رو که جمهوری اسلامی پس از حدود  ۲۰ سال تلاش و کشمکش از روسیه خریده…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5487" target="_blank">📅 10:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5486">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/163555b294.mp4?token=UdPjwws3Gc-FEsxW_DRw6wCTJm6PRXff8LwZdpRLrqRt8141SHup7vL5CBLLxNDgsTSXRrFJN0VaVdJTJnauqoFnIR46Bhdg9hsohKh28vUbGs6jsejqGl_ysetpVROMI6xxnYJxAoOL3px8d6VL6n13nEwsWOKy2uY9gwlF8AEo0p7VYnIj8z7ZM5lahOj_wQt_1oUtBXCtRqVBlfRVyqcAuJdg67qPGvHYtPVTdLSaGd93Jt7a7K5rzUiWWheIncIXiC-Td67D0C5alD0QWaqKAomYa0VAS5GHQxRT7sUY0ByuqVriT4z6uISEJXH08kPqAdUWcOuY5ICBRK51gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/163555b294.mp4?token=UdPjwws3Gc-FEsxW_DRw6wCTJm6PRXff8LwZdpRLrqRt8141SHup7vL5CBLLxNDgsTSXRrFJN0VaVdJTJnauqoFnIR46Bhdg9hsohKh28vUbGs6jsejqGl_ysetpVROMI6xxnYJxAoOL3px8d6VL6n13nEwsWOKy2uY9gwlF8AEo0p7VYnIj8z7ZM5lahOj_wQt_1oUtBXCtRqVBlfRVyqcAuJdg67qPGvHYtPVTdLSaGd93Jt7a7K5rzUiWWheIncIXiC-Td67D0C5alD0QWaqKAomYa0VAS5GHQxRT7sUY0ByuqVriT4z6uISEJXH08kPqAdUWcOuY5ICBRK51gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی از ۲۵ فروردین ۱۴۰۳  رویارویی با اسرائیل را از جنگ نیابتی به یک جنگ مستقیم تبدیل کرد.  در عملیات «وعده صادق ۱» ج‌ا با ۱۷۰ پهپاد، ۱۲۰ موشک بالستیک  و ۳۰ موشک کروز به اسرائیل حمله کرد،  دستور حمله مستقیما از سوی علی خامنه‌ای صادر شد، و جالب اینکه…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5486" target="_blank">📅 10:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5485">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l71CMIWSBroGpoFRa3A6PeqCHUlvRFkyXR67s3Z7pL-JK0PDrbvWAT-1sYS9Hi22UeQOoPMX9vORgTIFqebuC4GRguUMV2cB3vuZzGeYAYahiJxP434WpppRPVxxEHpq8i2CHBEveTvnOONC3e4e89VnEgNd9m6eNMylFz_8j7-IQh7AdAFIZzKB-FTGcARf0ioB6p_0qn9TqvUDV1pYl3SSK1EZApe1efAR4MWbSOxKXC1B5pkSB5ZaSYco_zAbN8ICYLNkBQBkCk60uvff68HkJXMzflPmEcDuuaAREQKQsLX8PCARQkIzP9ImEwGYlD0-CN1OEgzL_Em-2w6Rug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ غیر مستقیم با اسرائیل سیاست  جمال عبدالناصر بود.  ناصر فشار سنگینی روی اردن و بعد لبنان آورد تا اجازه دهند، گروه‌های مسلح فلسطینی از مرزهای اردن و لبنان به اسرائیل حمله کنند.  اما مصر خودش چنین اجازه‌ای رو به فلسطینی‌ها نداد! نگذاشت مرزهاش با اسرائیل دچار…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5485" target="_blank">📅 10:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5484">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDd_-J3QO1mVn7DaXXUQa27DPZPKfIrIZaD6JKAIFaG2zvYY5si9Ayd4b1bmN1vSxCFcIN9csreyu-p0GOp9ncArqv-dccC0GL7oBKc4gjXFt0STu6L-8eoXvQ2BkmZrJTqvZUur-rTkMh-YznaiXzyP6G9R6jhtrKC9_YJop22QoslpGki_p47VJ40AYskoi_ZPx-PdPrOPSWDQ-pZ79FcPHoGP1_HTQJ4x-cY17XgepOk-Qd8HN78u095Wl1YJbjAkUI-L4Zw25nDsj4Jf3gOEFH3PNNjwNRIj4tvTU9FTzCvDc8dnZNZbyGVLjHcfw2mJVN3p3iVVdJF4Kk1wqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی در ۲۵ فروردین ۱۴۰۳  برای اولین بار رویارویی با اسرائیل را از یک جنگ و نبرد ده‌ها ساله «نیابتی»  به یک جنگ مستقیم کشوند.  تا قبل از این تاریخ،  جمهوری اسلامی با مسلح کردن گروه‌های تروریستی مثل حماس، جنبش اسلامی، حزب‌الله، حوثی‌ها و….. با اسرائیل…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5484" target="_blank">📅 10:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5483">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TPkCL61OAsU5vfJSSZd3o0s3AivscKJnImA3gCfc1VujTIS3V01A9lURK4TM4ejZXh94hPoArLD-lU23ptWaYUN8tjSnfLb6divQcSZSY4GJYTuznuWFNPBsuReUp6cAbdBMVgBonHYS-ewEtT6y50SP8byjvMPATUaRv9p66ASC6M5HyPIGo8Lod1qXQ2-RXA-z-LraVuIquzHqc0fZAAK4zZAJTUisrqkDOnXvFnKx_8rGeGCXVydeVZUhacQjdPdj_GyTRsMFARW4lMweESAzIStDB0HGXMLHt87s7MKY41p4KQkD17WhbaFRkoywrlpi364bBmzHuc4-iRsaJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از مهم‌ترین پیش‌شرط‌های جمهوری اسلامی در دوره جنگ ۴۰ روزه این بود  که «جنگ باید کامل تموم بشه»  و آمریکا باید تعهد بده که دیگه به ایران حمله نکنه.  منظورش این بود که یک «آتش‌بس» نمیخوایم! «توقف کامل جنگ رو میخوایم»!  این‌ درخواست از اونجایی میاد  که جمهوری…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5483" target="_blank">📅 10:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5482">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5482" target="_blank">📅 09:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5481">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
حمله به کنگان
ظاهرا کل سواحل جنوب رو دارند میزنن.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/5481" target="_blank">📅 01:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5480">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">گزارش‌هایی از حمله به تاسیسات پتروشیمی  در عسلویه</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/5480" target="_blank">📅 01:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5479">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
گزارشی از حملات شدید به قشم</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/5479" target="_blank">📅 01:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5478">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
شنیده شدن صدای دو انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5478" target="_blank">📅 01:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5477">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
مقامات آمریکایی آغاز حملات
نظامی را رسما اعلام کردند!</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/5477" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5476">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
ظاهرا جمهوری اسلامی از آذربایجان شرقی موشک شلیک کرده
هنوز مشخص نیست به کجا و…</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/5476" target="_blank">📅 01:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5475">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
خبرگزاری فارس شنیده شدن صدای انفجار در میناب و سیریک را تایید کرد.</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/5475" target="_blank">📅 01:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5474">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در سیریک</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/5474" target="_blank">📅 00:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5473">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
خبرگزاری مهر : فعالیت پدافند هوایی در غرب تهران</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/5473" target="_blank">📅 00:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5472">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JGOcUQKc4SnHACKgqdnCeCzYdbRGgMNdLfNDJf1XbXiPXpJHiwO_mGEmtkl4yvIgYp7SZJsc2jP7nRwc4Sn8i9Dnp8I5pfAPE-VGzy56y15eeSpB7iNJm1joEVd9_Ri_mUlD4KaAwKiyal9jUrLY19_DVTnM4snMNdEAhcsVeT8I7xCKLGAHoau17VXdKTqzmpfHmbHr5ccEh9qggMnYAvEGvj67ZicrgEnvylchqfMtO2JiNxaFxMkViNmPV9jVA-ilAIVyy1xOxGqCLBSSQBBDthmn1SxviKb8iqlzKMVbx3y8YWGkPn481Cu6kq_3wRwtsE9Qb4tGGnuEZQQIJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/farahmand_alipour/5472" target="_blank">📅 00:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5471">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
ترامپ  در جلسه‌ای با مقامات ارشد نظامی
- امنیتی آمریکا در «اتاق وضعیت» در حال بررسی  یک اقدام نظامی «گسترده» «اما کوتاه مدت» برای ضربه زدن به جمهوری اسلامی است تا سران ج‌ا را وادار به تغییر مواضع خود
در مذاکرات کند.
🔺
ترامپ همچنین ساعتی پیش به خبرنگاران گفته بود که امروز ضربه سختی به آنها خواهم زد.</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/5471" target="_blank">📅 00:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5470">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران در مذاکره زیادی تعلل کرد و حالا باید بهایش را بپردازد.</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/5470" target="_blank">📅 15:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5469">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران در مذاکره زیادی تعلل کرد و حالا باید بهایش را بپردازد.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5469" target="_blank">📅 15:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5468">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d07d6979a.mp4?token=gQf_71wT2vRkeWTCnJm52BORTrHlC52kzignbCIL1zaVKdkohXF1O6ekmDZ-V2uCTriIJYz04IKQqAgKMmYuDwTm-fUb9-SprEyw69J8fxPLbZiCJqvqZrCVkHBghCQEuscEN-rpra_M_A1twSO8MGhnlf5CTn7WzLJQeZL7-jBcgoblZXyP1Uge-0-T9OfEmQGOjItCZ2cFrXnbdYd-MVTWcZ6yBgGrBtfpzcZpqxdaftcECPcmiWRgqA8rlJ2uiH3j1QmLKmktFrF8ma4MpT1l6ofwQx26MsnCcXJyesYjmlAUB_y6yG6K7oDpMCgc3dKnEsWcHi0oyGR30zQdlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d07d6979a.mp4?token=gQf_71wT2vRkeWTCnJm52BORTrHlC52kzignbCIL1zaVKdkohXF1O6ekmDZ-V2uCTriIJYz04IKQqAgKMmYuDwTm-fUb9-SprEyw69J8fxPLbZiCJqvqZrCVkHBghCQEuscEN-rpra_M_A1twSO8MGhnlf5CTn7WzLJQeZL7-jBcgoblZXyP1Uge-0-T9OfEmQGOjItCZ2cFrXnbdYd-MVTWcZ6yBgGrBtfpzcZpqxdaftcECPcmiWRgqA8rlJ2uiH3j1QmLKmktFrF8ma4MpT1l6ofwQx26MsnCcXJyesYjmlAUB_y6yG6K7oDpMCgc3dKnEsWcHi0oyGR30zQdlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله هدفمند به یک خودرو در شهر صیدون لبنان
برخی رسانه‌ها نوشته‌اند که یکی از اعضای بلندپایه حزب الله در این خودرو بوده
هنوز جزئیات بیشتری منتشر نشده</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5468" target="_blank">📅 15:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5467">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJlMiRRxYOvsUaw0l8d5xkW52FkI21ihdkFjdjd2dCuqWS2KZk8xsegx2aFQbKJsDqdtt0ITGhVNoJYdj8yQ6XYPfoS5x0BSClY8ABVRTOTQFfdez4GtPJTJPefXaNVfHw5CDdZGf79g7NB6_GJ58p7j3C5YfhXjyXPr1aJDmpzx2vc8UeV_NW1_GwSe1G5Wxf6o48-Yo3K9iAaDFPW4HcyzTPaxdjAOxlkax_DkFHdiW7c7G11aZfHzxLmBtGJerHjR3QkbyjCbfhEUv9H-R2bVh1joUHVFQEXdErIjHFZrVWUIKpR_2EYrkzqKH5D4L1AVrBR6sCDImYmu2axETA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dkJJw9FTbJaiZMdNQG8WF0VWTGYLO_xfpoYYjxO585WNAABqTJZSKq07Md8MKgAPbJ4Yr5cEo3djWEwcd0wA1pE3PSsnjD81AT6FJk6Rq4mTpiny5cR-VVPpxnCB68mUzblta5mvhOV1HSwcHQ9MEAUXjRCeowK7XX3JpGWZd4LJlP4bcYHjozYFMzGbMZMK5eMfIC0rTjZ1JaNalfqYzPRxwgrxGmVk91O0YqeIkooxa-wyHBN-_3ujbl0rPBIjV0IH-nD0ozcC6vUiacFbFB4RUa8hCd-EFFUGgFDaTYTtMhOM2Mq4zYrlfqu-EPBKj1A3Jq4gI0TfrcRC-6patQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGCWBh6ZQ0r48HS6k5rYqlN_8YBM9eVb6MJaNdkKHWILN_aVBiUrPuVTCjLdp791DLIKE8GXvzQn9DsfWcNJ9q9c-7r1tNLzp-EYsEyTFUBOearMlIiIjW6O2jk3wwgUZWr0v3mQKsbyasThteMcGsXufOWL7j3SPH9aKKHJU-p8HA6_O_aFpcyw8fOONxfuAhF4QIGWRPhrLEyo5DHl2RR_xlEq8jec1PkYHkmORq5uILO8IelsCtzLcFSeiOQR6VtDJA_qLrRvGKa4oJPCWW74TurPnjwGqzZY52kevrqh_b1qnCLTPj3lnWbfJFfZZsr03-8kMyfQHv0HQySVRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل به دو روستای شیعه‌نشین
غسانیه و حومین الفوقا در جنوب لبنان
هشدار تخلیه فوری داده ، اینکه اطمینان داشته باشن
حداقل هزار متر از روستا فاصله دارند.
این دو منطقه در مجموع حدود ۴ هزار نفر جمعیت دارند.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5463" target="_blank">📅 12:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5462">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/POe2gxPd_Yg71B2hnyMdT486QDApKOPrtUvXqrjYot5zXNLBOVQdAWOW30PD1G6MA-M2IF2mUrhG0RbogXgVbozhr4RbVbPgr1vvZ0OCq2W4lBDcw3Co6Cj-QgIUGUJLTO3d14Nq4-eJFM3TbdvihD9xoC-9fDaQUcmE7BjZyGYDraCXlGDUubo-HtlAMtgio0AuDpId2mBhoq8bG0Mu97f-261gsJhwrnYBaFId1yojmw1_graM9BiNutva9eNtWxUReu929U4DJoqpSO4NqOguvY-rCx2mao_YyFlZX1X7EHR6Y8Rl_tOLeQwiBEB4EdNYAwlNwkAo0-oOhq5gcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب! چه نکته جالبی بود
واقعا چرا آمریکا خطوط قرمز شما رو رعایت نمیکنه ! غرامت و تعهد هم که نمیده!
اسرائیل هم که معادله‌ای که در لبنان اجرا کردید و براش یک پتروشیمی در ماهشهر رو هم فدا کردید‌، که براش تره خورد نکرد.
عجب آدم‌هایی هستن!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5462" target="_blank">📅 11:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5461">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q23rkzigOe6h-ESfp4bICT_b3fbpcH7PxCG_C4NYK9ht9tZDvNSaGIPzP3eQQSYVfLs2jDV5fgj3yLx5H4Tew0sPzUN5mh99UTk8hv5YY54djWKvs8hPKGNkgfhusPf6J7px9MZOiMzqHBkqPVx_pJ7jick6BZYt-cSinwAFqEVqpJ4ua7LwRpKUGhk3Juylne-A7fSSoL-W-xqo0JOSyZMKPQXnNKs_l0Df2r3BtTrdRYNeFWV0EzAlm5MCpsCu7UJZH3V8yQ-FapFlAEubPAYsnTV8mxV__5se-vb4mY3-1ayQ8nNBkKBkEuDsgucYv0cV8Ks5J9eO5iNRrwhh9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خبر فیک به نقل از یک اکانت دست چندم، که اینجا نوشتن رسانه تا بهش اعتبار
و اهمیت بدن رو هم از دیروز
منتشر کردن برای اینکه بگن
چرا دیگه  به امارات حمله نمی‌کنیم!
چرا فقط کویت و بحرین رو میزنیم
و چی شد یهو امارات رو رها کردیم !</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5461" target="_blank">📅 10:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5460">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">توییت ابراهیم رضایی سخنگوی کمیسیون امنیت ملی و سیاست خارجه مجلس ساعتی پیش از شروع حملات آمریکا  به جنوب ایران</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5460" target="_blank">📅 09:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5459">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SI8LZGtIibtnTMv_uEjwLNiXHVXhNthguoWMXCYzjaF87tIFOwykIKgsHCKe3cbwfdJI0zlHhb1yO-TzTWUdt8vCov-n8rYBza6--Ip73CZbLIFXxsI-E5gfEzKDolA17A1OtZMRmogNl8J_vzAxGvS2bfogI-PdrSCN7n8TEe-kGMzA5neTF2r_ACzl1cCv9CcT7ZA-MjfOMh09GY28mBzbvfYjad7Pdpkesc2riMw9aOutb0enq4iT8-zhGkWmkBWcyn3KjupJnRUTIs-jXJPK9hMSUhs3oni4CRDtHPw0zBYqgeWC-ins7TMJL8cu_Y_LxHEsbDZCiW0T2pdC-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات گسترده امروز صبح
ارتش اسرائیل به جنوب لبنان،
مقامات جمهوری اسلامی پس از حمله موشکی به اسرائیل مدعی شدند که «معادله‌ای تازه» ایجاد کرده‌اند که اگر اسرائیل به بیروت و یا جنوب لبنان حمله کند، به اسرائیل حمله خواهد کرد.
اسرائیل اما از دیروز بر حجم حملات خود افزوده و ادعای جمهوری اسلامی را به چالش کشیده.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5459" target="_blank">📅 09:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5458">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
جمهوری اسلامی در واکنش به حملات شب گذشته آمریکا، به بحرین، کویت و اردن حملات موشکی و پهپادی انجام داد.
اردن گفته تمام ۵ موشک جمهوری اسلامی رهگیری و ساقط شدند.
کویت و بحرین هم گفتند که اغلب حملات رو خنثی کرده‌اند.
منتظر خبرهای بیشتری می‌مونیم.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5458" target="_blank">📅 08:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5457">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FbTY2Cd16uhV8bZqs4S7UdXZjeLmJrMGqrPgIt9ft8AETgKd7QpZaQgVVlPpJA-SvYpsNLusWIBS-Qzqcry-xszLx9QFhvynqk7bmX_YypD9v_mlbCsqIgzvQ6lao2xTLbVIUwAAxvXrK_LmCtL0NSk9yQsr9pxWSYqCruCQtOYPd--GybFl9jrtP1gQJEljaubWWSzmMJme3gjH3qertDanpU5QoSSAn8ez5_ueHCAkBbEk6BhvD1R2oDl0Nqs4SKMzLYxtOvBFU7YvyjTZBsGx_tYUgx7yLc_XTNSyAXlk2FZrNnhEdKDvo0KnCw77aIeA0OC4JbqZQ0WKM3RULQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخراج رضا دالمن از دانشگاه شریف به دلیل آویختن عروسک موش
او پیشتر به مدت یک ماه بازداشت شده بود.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5457" target="_blank">📅 08:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5456">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3Q8C7oArx1fmFedXR7kUMspTFPz2kmq7AGJt8pssJ14xsFbsNhUOAsoD37RJTihw7_4PELVMgoGiabSTKFWBArq0mDf5SKRe0NjqnVXferMfzbqAHaGcb290F__itwahq0Dge-fB9Y6nzMCO9rQkgughUx85527vhIDRqmMe3HvHhn4zdP2P78xCx287bHAiwbmLwsxUKrRovE3wZlQ2o91-_Fsw7SrYyeOmyFgbzwe-36myB1N1UAk6WUlnxBPfTwRSpOcylqs6vHLsnGLUls496YPdTezpEhET9DxsBVjAlJa_LF7mw_OdOVWRXyuPT9qMCF2IdAiFibH-5vtUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ابراهیم رضایی سخنگوی کمیسیون امنیت ملی و سیاست خارجه مجلس
ساعتی پیش از شروع حملات آمریکا
به جنوب ایران</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5456" target="_blank">📅 08:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5455">
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5455" target="_blank">📅 08:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5454">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‏
🚨
صداوسیما:
دو نقطه در جاسک و کوه مبارکه مورد اصابت پرتابه دشمن قرار گرفته است.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5454" target="_blank">📅 01:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5453">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
🚨
سنتکام از انجام حملاتی در پاسخ به سرنگونی هلی‌کوپتر آمریکایی خبر داده است.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5453" target="_blank">📅 00:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5452">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
جمهوری اسلامی با چند موشک به اقلیم کردستان عراق حمله کرد.</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/5452" target="_blank">📅 22:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5451">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">عراقچی : تنگه هرمز «آبهای بین‌المللی» نیست.
پاسخ هر تهدیدی را خواهیم داد.</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5451" target="_blank">📅 22:34 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5450">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">نتانیاهو: ممکن است مجبور شویم بدون پشتیبانی آمریکا با ایران مقابله کنیم
پس از تماس تلفنی ترامپ برای توقف حملات اسرائیل در پاسخ به حملات موشکی ج‌ا، نتانیاهو به وزیران کابینه خود چنین هشداری داد:
«ممکن است به وضعیتی برسیم که مجبور شویم به تنهایی و بدون پشتیبانی آمریکا با ایرانی‌ها مقابله کنیم، با تمام هزینه‌هایی که این موضوع به همراه دارد، کمبود مهمات و انزوای بین‌المللی. نمی‌خواهیم به آن نقطه برسیم، اما می‌دانیم که ممکن است برسیم.»</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/5450" target="_blank">📅 21:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5449">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sF-2TgXQ-6RGKoh33UV2iBCdTU-QM_FszAkJ9ojmCFD8Zf8MjgB_DXCWXzreLabJ6Fg60CVYENrpTPGKW7XkKHEs1th9wb74WvNMtDe0FtUqzMpat9NTa2YfeJaggi5MqG34NCbW7gQt7PFrXEUSvGu0r08fQvZT8N4IGK8ueW4KFNHJvMkHC68XiHbPtLgyIcFGtLuFEj6x7YJPmyO7fQcf6jeSzBr2MNZXKw_4Qp7E0Aa9ORULBF6CY-wLUE1XFafjLCi0lbQn_Gqffqo3JkJBwTuDFCSyGsy4E4bcRFxvzhUY4qaXy7cnA_v9WxnNCi0BJsvwbmM8PyBmMZdr_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/5449" target="_blank">📅 20:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5448">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DPtBdnvS81ap-V2LfRy-TT7OG6YZfiQx-EhuZzp9yvwuQOi-HwOHHLNm9c2ZPTnFJKn1MG_EghPZfrRwpvUazgn_-P92ACkFLjYe-eL0-YtDPRctFcJA7yIXrilO1CTTh9V10NvcqFTUqRkTTpeCC1YHCjLOhbsooF36L-Ai5fm5_vI-JX80lJnJ3pk1E1nvB16buS1sR03LJw_1mbSvLjF2F7jw0dCqRZnXA36V1iaPn3dtjZX5-JfC6ThsPMpabAUePi6ByM96IiqPjcH9uft0rZ9Yyxg-B9o6NTIj7TGknIdfqTVQboMvD97Cmdza_YJTNxJxt20ISUOXBYyATA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : جمهوری اسلامی شب گذشته یک هلی‌کوپتر آپاچی آمریکایی را بر فراز تنگه هرمز سرنگون کرده. هر دو خلبان سالم هستند.
ایالات متحده ناگریز است به این‌ حمله پاسخ دهد.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5448" target="_blank">📅 20:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5447">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">می‌ترسم اینقدر اسرائیل لبنان رو بزنه
که جمهوری اسلامی مجبور بشه
دوباره اینترنت مردم ایران رو قطع کنه!</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5447" target="_blank">📅 17:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5446">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">زن شیعه لبنانی : کشته شدن خامنه‌ای به ما چه …    زینب زنی در جنوب لبنان :  «نمی‌دونم چرا برای کشته شدن خامنه‌ای  رهبر یک کشور دیگه، ما باید وارد جنگ میشدیم  و متحمل این حجم از خسارات میشدیم.  چرا ما لبنانی‌ها باید هزینه کشته شدن خامنه‌ای رو بدیم که اصلا لبنانی…</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5446" target="_blank">📅 16:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5445">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4718cad225.mp4?token=pv_dGLLg-Od-uIiV60HwAUJoyUK-gcvKEX6fe7j28sUeq72X_piR8C4yEDamnS_Lt0GXiOLhFfFjNJJiCE7t7vTFvNs7eJ4iW3RzPGjFsZdfdGXz7wDwxkei368iHsVsRhsVbkdqIZfXWEpi3_S2Dg2xL0ImKBQjbmLAkDcNr0iVmEiLMpgYUKqOlEMoYr_3looDfnlvqra6C_bv2jBx5vS-oLKhOE27oY2kivHQPqNzySGIP9Yr3I8YNQhLF5LmHedrHFALzYW2xOv7No2siGRvvXcyOAk3YYVR5w6prBkJ_EcZYlyjJ65g6EHleGOQqnVZvaMY2Hv6TODHce9oSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4718cad225.mp4?token=pv_dGLLg-Od-uIiV60HwAUJoyUK-gcvKEX6fe7j28sUeq72X_piR8C4yEDamnS_Lt0GXiOLhFfFjNJJiCE7t7vTFvNs7eJ4iW3RzPGjFsZdfdGXz7wDwxkei368iHsVsRhsVbkdqIZfXWEpi3_S2Dg2xL0ImKBQjbmLAkDcNr0iVmEiLMpgYUKqOlEMoYr_3looDfnlvqra6C_bv2jBx5vS-oLKhOE27oY2kivHQPqNzySGIP9Yr3I8YNQhLF5LmHedrHFALzYW2xOv7No2siGRvvXcyOAk3YYVR5w6prBkJ_EcZYlyjJ65g6EHleGOQqnVZvaMY2Hv6TODHce9oSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محله الکریت - صور - جنوب لبنان</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5445" target="_blank">📅 15:26 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5444">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g6iZqBkX3rGvrcnvul7mzypnShUv4PTVzEEVMKmY4wYcAqz-Vi-b46rAEDF80DgyB4NlRJklHHiVii63unRqdfZjDkSmie5e4lj3lGhl5aoyQjepa0ldROtj2D3jaNCarOuhWPgc9YSb6wY7vbpitsIGuotATlHYdz5jyDgEWSEd9E5b1iiNCxgk34Q67K4e2IsJz8u5ryTWtUsxyLzw5paDZTliIIc8LHLO8-ybv2kVYWbz08KhQJ3Q-sNpUuwjxd0zUHC4noPrqmfA7AbZN7hqjgmRa0kXl-RWACqf2978F9-eExdEu0qgEi4q0YpS5mDgDoQ5l6YhNJYtQhX5dw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-NL5m7kHDquLTQNkmZKEk1cntbdQKwtZguFbacfbvuGnlTvmCFLh3H-HuboECg-zi3e4vCmnF1tx_kCYdTZHx3gredten081NdupopcWjf34BLvioKTODy-0OIgNPWgP2fwnnYMskfosQxHxqEzm_wqZTDyDhxlZTec5ZrzB6jDDPgCp5BKa-dt4JbOlbzNB25poCQw5GGIOY-DNKsaFSU3iyv9dQJhFU3fv8SjzuWDAWZ-QUX7oxpkW37unznFRbJJUrBiH7ilpbddL79v8hcSfDgE9GnrQW9v1ybfeKHlk8TyjMqH5zAXYrQ2zwT7PRVcWUxiVxSd_AQtO0SKcw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea21582d5d.mp4?token=nyzG-YjsBCNB3TodHTdy6crfXYI1oA-0vfXM8-Dd4co062BfAlORcUvLJ4H7gS8BA0-3ml6dd9bJe6FDnBBXpSXB4GZpi_yZPSBhiWjqlOE26zxc1Jd97W0Yhljj3FAuxSQbe2YhPoQdaLjnEIJ9NopT_uwuWsVYCw2JyeGrXvLrzd6HKOl3VXgFzThDiVplQID-DKBH1VpjTE4t0BwYr2KvCwawz-RLeuMSb1uv-MDdvhy3l29NrInFPzOhx8zpYtIWM3oNrjThAOfOu3b8NWGu-xMDUHwwAvwbJL2h-VZJfxX3LF4cZYqQwYQprvNW7wgGgpPNFhuhJ6nw0bXukg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea21582d5d.mp4?token=nyzG-YjsBCNB3TodHTdy6crfXYI1oA-0vfXM8-Dd4co062BfAlORcUvLJ4H7gS8BA0-3ml6dd9bJe6FDnBBXpSXB4GZpi_yZPSBhiWjqlOE26zxc1Jd97W0Yhljj3FAuxSQbe2YhPoQdaLjnEIJ9NopT_uwuWsVYCw2JyeGrXvLrzd6HKOl3VXgFzThDiVplQID-DKBH1VpjTE4t0BwYr2KvCwawz-RLeuMSb1uv-MDdvhy3l29NrInFPzOhx8zpYtIWM3oNrjThAOfOu3b8NWGu-xMDUHwwAvwbJL2h-VZJfxX3LF4cZYqQwYQprvNW7wgGgpPNFhuhJ6nw0bXukg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏جنوب لبنان - امروز
‏حملات جدید اسرائیل به شهرهای نبطیه، حداده، الرمادیه و دیر قانون راس العین.
‏بخش زیادی از این‌ کوبیدن‌ها در جنوب لبنان، در واقع پیام به باقر در تهرانه!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5442" target="_blank">📅 12:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5439">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sqJKDP1A7PJCaPP8asWeQYhg7Nv85wKacFGzrk8zt_irBRvjUvqPmQfrznYxCgMuCGNCNPbGt45rHFvJphtShkYiZnMUuZXi2u9NMMABej0Org2XrG1dOVVByqGzLHl2yRlq6ws20KWyMZU3pU5-Q-wNUg8mtaFUaKK8GBkjDVSDBv2IbTKg4cagFH9oV36wyjfLongot5p-HOBTaqAiFuiy9uXRmfueuqz_ktTaI7bP3nei0S3bO4XBuMGEUgXzs0U4kG1H7JestRXCkg57DwKB84k6NSDa2KWg-8zUK34a_QS7TuSk2iK5XbM9KD6ZgnoO_iISQJs4M3-UwwbZwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WhDK5cXuj4DCfM-dGSa3S3ktMknr9wHynAe6lUJoXhP8VGtzMn-haLI9RDhgqSrziscGVV0UFCXMfxtC90y7blh8Rkqt8YXy5R-TsBsf6H5chZCFnUdgBv8UesMuuQn640ici6Q5fPNdfqtyCkv686m7L2l__mnEW0ewA3MbT-1aYwS5bAO6Qb6wZzpafi5SLXrnKemP6rz1U_Xwam3WNUG_O_MN0bG3wQtxO_QVHtvXgPsxO5CfhzBXp1z-QLdMLY5d2Q7HYg5yEtZQVNg3SWOA7hODn42FC1vTAE-YscaKVcMu8L8pn5qujGz4YAsskq0QYMbo1N6B44tKOf7PMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874c401e95.mp4?token=CApD8x7g15rVZIRO5dtJTqupwLwRbjSFDOOq4QjEYCZac5574T2gfukLEjXKxXA4_T_TkqeQ5L-qPzE_Avqqlg_HG546KA8pZwsYCkN-lrojKLvbuTEnZtqPQdYpAstlzypL6SLbwltOBb1nVqJJV5p3tD-ir9CY28owNLSsUg0T4386Sj04Frg8p-jEIPimD8rnIm0aX5dGmJuTc5gSN5s1YWKEGuiEHYugjOddYNH1pE3czwOMEnPHVRjOnu5nmhw9LotjsFlwTn-gXROOB1zjyYENV_dcFUBcr__T-JFttPwXgrXi-ml3mRBygBwtFEErqo9hElbaP_Um0EpQ0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874c401e95.mp4?token=CApD8x7g15rVZIRO5dtJTqupwLwRbjSFDOOq4QjEYCZac5574T2gfukLEjXKxXA4_T_TkqeQ5L-qPzE_Avqqlg_HG546KA8pZwsYCkN-lrojKLvbuTEnZtqPQdYpAstlzypL6SLbwltOBb1nVqJJV5p3tD-ir9CY28owNLSsUg0T4386Sj04Frg8p-jEIPimD8rnIm0aX5dGmJuTc5gSN5s1YWKEGuiEHYugjOddYNH1pE3czwOMEnPHVRjOnu5nmhw9LotjsFlwTn-gXROOB1zjyYENV_dcFUBcr__T-JFttPwXgrXi-ml3mRBygBwtFEErqo9hElbaP_Um0EpQ0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ov7MuoV2aFEfVpar4wsYz5eRqE3rbOxD-eWjgwI7gVSKOuVq_cftCObCYnE52fxa2uwgGmkE2_BM6PmWys2DL1EpPOgeYHeHLDttiPW3y8BMmn2HLSMJrTqXc5FmRQzjVTmCjTQc_U8fKJYPwTR-nVZX_wW_aH-tvD7J2jKCQbL_04dbVcGPtVdCnuJkEwjzIivTkxHiqjdnbB5OlHeKtIFoBkJTBfxIGTPnfmIy4gizUj4E1Rkv8kan6dzh0hDSPVtV8xkkTqb3_3ne27n3jLdDxb4_0vCDmfCdrIeQI5WigrY68uyY-8-oaAgJVrWe8Pn2mqYjpMJ4udG1unhTqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V8Vv20O6Tse3Wkdn6ZIBJuS-uLJmdRHDoFeeinmlZj2UWtowIcFnDnnukdDSSDRe2ykybxaIkRPjovtpXJV90JhrRkQg55f7Y07U6UecyDOG4RsKGT9AghR5Jt1XL0jvIiSdXmDm4hZGht3UfSWlZnzSXeLxogAdA01XtCti2kpN4cMnlnPZ_DUBs98vHY6tYD1_P9eUdT1lJONVwn6PAvRW0n3BpGXxhYSHA5b4UTW_BHYQUSLtoEJqZLKvFfZ9FsXOIWMinqegpWWelr57ttLfOzd1mAj0hcCmIW46ZaPMdE17n6qfRHVmLNegP7XzP0oG9dEQ5Yo1vTBlivazyQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd790ae501.mp4?token=azjycwDNfpcl3GCAhkJ3SdNIAOPv84LM381-rporDZ53xPBuglwZmHpZW3EROc9UzbzkWRmzaAQxTt24DZMy33tB_I6KfaD7tqexoNK_f3CW1Q89RAnpDfCwxtaj_4Rx2ukK_t4SmlAck9CeV_Tv771iqEDQvPhlAXsk73mzg3oEa8TvSUDlGPowEpwYtIL5Y1L4eOgC-sbQVauWvOYwDQuM00_6HvtWdf8t1bP2Mj5chrhIQe2vV6X_rF0p5sNDTLA5H8U0daLtpy7kO8SoiPzZmAE9oT-lYNDtwdYGZbTcoVYu0KaSc1KWB8rl4pno1HUm-oqq4ew2nzzKXb1HJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd790ae501.mp4?token=azjycwDNfpcl3GCAhkJ3SdNIAOPv84LM381-rporDZ53xPBuglwZmHpZW3EROc9UzbzkWRmzaAQxTt24DZMy33tB_I6KfaD7tqexoNK_f3CW1Q89RAnpDfCwxtaj_4Rx2ukK_t4SmlAck9CeV_Tv771iqEDQvPhlAXsk73mzg3oEa8TvSUDlGPowEpwYtIL5Y1L4eOgC-sbQVauWvOYwDQuM00_6HvtWdf8t1bP2Mj5chrhIQe2vV6X_rF0p5sNDTLA5H8U0daLtpy7kO8SoiPzZmAE9oT-lYNDtwdYGZbTcoVYu0KaSc1KWB8rl4pno1HUm-oqq4ew2nzzKXb1HJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«جنوب لبنان  و پیام اسرائیل به جمهوری اسلامی‌»
اسرائیل امروز روستای شیعه‌نشین و معروف «مارون الراس» رو کاملا نابود کرد.
این منطقه که بر روی مرز اسرائیل است
از نمادهای قدرت و حضور جمهوری اسلامی بود و احمدی‌نژاد هم به آنجا
رفته بود و پارکی را افتتاح کرده بود.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5436" target="_blank">📅 12:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5435">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZhdWB7k46isqYwPbQ-HOP3RC7Xq-4gBE7VloSXweW8HMRg5cX9UjNCCjZy-TSX8pksHS5zatbDY845ag7v0QIeXIoW7pKDYjJrTrKPmeFjcFEqkkMFBNVaEjTf7m0HHY0FO-W2PWpMWV5ly_Lz6pUgch5yKhDInioS6PxzAu-ZINZytqsYt2v6QhlxWzdy2VdAGZZlImwB4cBXdITwzE5Tk4g61X6x9TVIRwcFAECyPQQg72hHQRCZ27VBgMuZQU0ie-IT4dPy5ySe1VD-YMa7CHCKVWfYLUZcUz6TUIhY-E21iJLfq3Atth726mXtLBLfCpHZXDkGCctAP5aiGhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسلمانان در سال‌های ابتدایی اسلام  به سمت «معبد یهودیان»  در اورشلیم نماز میخوندند.  شبیه کاری که یهودیان انجام میدادن، مسلمانان می‌گفتند  ما به سمت «بیت‌المقدس» نماز میخوانیم!  که این بیت‌المقدس همون «بیت هامیقداش»  «معبد» یهودیان بود.  جایی که داوود و سلیمان…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5435" target="_blank">📅 10:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5434">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">یه نکنه جالب :)  در قرآن، به طور جزئی اشاره شده که دلیل اینکه بنی‌اسرائیل حاضر نشدند بجنگند، «ترس» اونها بود، خدا هم میخواست بهشون شجاعت بده که برید بجنگید. (در آیه ۲۳ سوره مائده)  بنی‌اسرائیل میخواست توی یک  مناطقی از کنعان / فلسطین ساکن بشه ولی وارد جنگ…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5434" target="_blank">📅 10:36 · 19 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
