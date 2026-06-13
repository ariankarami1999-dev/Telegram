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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 00:15:23</div>
<hr>

<div class="tg-post" id="msg-5538">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
حملات موشکی حزب الله به شمال اسرائیل</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/farahmand_alipour/5538" target="_blank">📅 00:10 · 24 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farahmand_alipour/5537" target="_blank">📅 22:58 · 23 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farahmand_alipour/5536" target="_blank">📅 22:13 · 23 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/5535" target="_blank">📅 21:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5534">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxvMDMbyy1RBGs9z-I4v_VyISib2O9Is0Mg9Q7fvhfhE2irrbBeimiX-jY19R8na68_wfU2gGtblY78-BdkqjkiIq6xWrvwZI8VWf6FzBDuE8WISQoxtkRdNS8zCJ77OCAZTry_v_uONtBfcS05K95DHN33uTtU7fBc-FM2sbzdSFlKNBeVgH8zp7-QfWak-TNUDuYQfjHjTwlnJ3pxgtma5YeGYfqabv0AOZoQZQrf7bHjI0wvOAfjs8es8VDq4hty-oKoghtArPBPpiKBgfKRaHJ8x_aNkFJC_vsUxlHJZXaQXVIKvvsrlz45ifouYzzhuLeG2awBlrB54Xn9yzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: اصرار ترامپ
بر امضای تفاهم‌نامه در حالی است که مقامات ج‌ا  صراحتا گفتن  تفاهم نامه هنوز نهایی نشده</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/5534" target="_blank">📅 21:16 · 23 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/5533" target="_blank">📅 20:57 · 23 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/5532" target="_blank">📅 20:32 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5531">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPPeYhVF2UVVvidUO1MTL_kc03ielRCXbZTP1c_rP6iRd69Pzw0outZj2adyL2jSZsdCBohZVt_0Ej1sElyoR7I2ijoRyKTxSpqvIMr_0Pb7omZ6IsBzU0RP_V93Jh4s3M_OBm9BN4mCcOd27tB-7jmMnsqnJpk9C-1LBbvrc_-hn23GZ_QR1miAUDF0sA8--hjtLY2rrnh0WncA7In4L4E6uoet7G-vGKBvzuAee62vVpYH2e1sV_iYRJ8zT48SfzA5KsTlQa8geHN-XeCRp8KGRHiendeqhm8CT--q9srjBnLtxql5yY_ib3pKWa5CiY4qRwoda_ZZfPnIjCZc_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیسی خطاب به قالیباف نوشته.
نگذارید خط تسلیم و سازش با
قاتلان خامنه‌ای به ثمر برسد.
(نه سازش نه تسلیم - نبرد با آمریکا!)</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/5531" target="_blank">📅 20:09 · 23 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5530" target="_blank">📅 19:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5529">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">نخست وزیر پاکستان: تفاهم‌نامه ظرف ۲۴ ساعت آینده امضا می‌شود.
عراقچی : برای ۲۴ ساعت آینده هیچ برنامه خاصی وجود نداره.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5529" target="_blank">📅 17:03 · 23 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5528" target="_blank">📅 15:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5527">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMPBtqaOtaiRMApZXl_vXIJlLK9tl7hjDM7I_6x-HEwFq5Gp-k-TfR_TkGqVQxNrz61l1-InDzVwWD4oouL2PNhzz63sqOhG41d8FLE2YuQ6eT3wEdTr6GMllIwWN9IsSBq-ELmGxdHYTmlPwlgpqmhzm3zBm-oyN5sDwprIa2ZxBi0_3rvtSyjpwOi3OHYNVvumG3exUqQoDHs-Cfrd3vuw1yxrXHV-e5T-t-81bpvo4wjZQZg5Di-AABhnkgBTKFKUaBtqfbtoZseSXZ64nYBk93NW-uXFilZzCC-WFSQxwIeEkQgTKNd41Kj9Pu5Kifj1qvZlKSRZAIO7jOlEjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی در باز بشه می‌فهمید
مجتبی خامنه‌ای در واقع همون قالیبافه!
چیزی به اسم مجتبی وجود نداره!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5527" target="_blank">📅 15:13 · 23 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5526" target="_blank">📅 15:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5525">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hvlyJ8uC6t3SzPtwYFdFwkfNQ11cYhD1SN-g5ZOXQh59YKzFG_gU_u78Qfa5HtIVO0-AjpTDnWNIka4wC9MnTPYANCQBwqYDzBhAjiUO7kHkpBau4Nx08SfudOWeTsCDy1o13GjIZbeo03bEzLuZ5I16uBpD6sge8_wnhgavG4D6XDeqxD8QIT2o9NxvFyHbtJY6oR5kQSF74yUgdaFrT6tyTiWAxkYGLpxWPe8_Ad9ARHXsNFkQDy-g2ItCz6udqiXqb6v2rvvK-gTjx82UnOLh4b4SzudLnE7F5piWNLR8n6DglxayQw9S8TLnYN5NIcs5UunfW5UhCAJOP5kKvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیات مراسم تدفین خامنه‌ای</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5525" target="_blank">📅 13:58 · 23 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5523" target="_blank">📅 13:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5522">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">عراقچی : در دو جنگ گذشته، «مذاکره» منتهی به جنگ نشد،  بلکه «مقاومت»  منتهی به جنگ ‌شد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5522" target="_blank">📅 11:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5521">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EkQFqqRcsKfbmtLiXb8yeuh1buDJXGpfYy6oU3T-cemFomf-K5owK8D0oC97TxIU0v2nhfKXehHTr8MtmnvXs31kTctCHUvftIvS-Ioeh7jGKyM0MS80YuEoLsoApESMdcJGmc8aioVg75OUmQZmJDyT0bKEtCttIqMhCybsPVAllKyt5UzDGrdzDox7Re80izfZ9cSYVTj2AzXzi6dOc9Tr3lyY_2v-IbyzfR2DVYNWMec7eUOgWeTuIgICeZsJNAzf0XQ8lkbIQ8T8tL7PueuCp3-NaCvmcjaMrwAuTrz9Rw1gf-bbhv32EKH78wZMCmKyOMX5F2xEqv4ERUpTKA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5521" target="_blank">📅 09:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5520">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hhz-5BnrPY5To2QcI4rTr42HJWyZdnFzkMR6L8tIk-ZlEFfvgp4MwjovRhsSqF4faseXwea5MvzjtXV2v3pcmpfw66Uax1JHoudZuSSJnwfyl_e68rXtZfK5F-ANyWoPPOOQoRF0tQK9MSkLThlVNDQYO0dLpNgk4TYyhjbZMmqdYv1WO09uJ16u5GwFm9zZFqEZPqNx_NuulItjKlVn-HD5x4oo1MqCNeuQItMCDVc17kcwmhQntQhHKUe1oZYOtkrs4T_KNtgDA27_9qab2c-L_xD3pm3GqL4xIGjRJrKLcZuBEtTTuJ9rkSPaMY_p3-Ws9OqfrscvfuDk9bG3lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5520" target="_blank">📅 01:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5519">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=Fd-c25WxiOmbKb82CcvNmnEJEsiiTnLXIBtrDa-LbQS5QU27DDXQnRa4lpbpzWPyNb8ybXuaMRNxeUjKpSNGSQoItlUyM1iukilba0sDAxfGnWB0Hve8tHOFnyMNI5gDBnAAW1EnLj2mkL3FahhRBSfv-eZmU8hZGH5BuqABXFDw08quxdbV8azt6mTMG2XVvhPm-F1dJtm5p1NkPtC83v8OymZPPOFmZ5Wo0wnrE8vJCLqilLsBV373HJjOfOWb9pn9zB_34gN3u1xICW-DblYglWZHywINbSZjYSRc66LS8nqXWrh06TXALMJwmj_Ji7itnUwB5HJjzVP3imnWeE3R-Arm8k2yxur1GXGzmZwTdF7gcSeLwLpaCPaL-UxTYpQ3VFzfVJpsxuB0F2Iu2hl2-rKnGJyvWLncq2O7AnDywXvu6qaMxORMVHp9NMJga8ZPv0dUJMrWDmb0RkWceWPtBnKONbDY5K1v1I0zqhHWGtVmT0V3KYCNJ4szWjMMnh32SBrDWlpEucjsAx8YrccCz2jTjMRJbrjb_CU7sTqI1HOYrq1vuJ4f3RdCmArcxa5aUzlmcqYNQI8MthnOhEnshrG2Jfb9ivUZz7elYa76b1EPCXoVvHi9z-snDhDmHBsaKE4euXKpMpd2avV-xegPKPxMQzMgZIUrUto8I8k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbdc11ca82.mp4?token=Fd-c25WxiOmbKb82CcvNmnEJEsiiTnLXIBtrDa-LbQS5QU27DDXQnRa4lpbpzWPyNb8ybXuaMRNxeUjKpSNGSQoItlUyM1iukilba0sDAxfGnWB0Hve8tHOFnyMNI5gDBnAAW1EnLj2mkL3FahhRBSfv-eZmU8hZGH5BuqABXFDw08quxdbV8azt6mTMG2XVvhPm-F1dJtm5p1NkPtC83v8OymZPPOFmZ5Wo0wnrE8vJCLqilLsBV373HJjOfOWb9pn9zB_34gN3u1xICW-DblYglWZHywINbSZjYSRc66LS8nqXWrh06TXALMJwmj_Ji7itnUwB5HJjzVP3imnWeE3R-Arm8k2yxur1GXGzmZwTdF7gcSeLwLpaCPaL-UxTYpQ3VFzfVJpsxuB0F2Iu2hl2-rKnGJyvWLncq2O7AnDywXvu6qaMxORMVHp9NMJga8ZPv0dUJMrWDmb0RkWceWPtBnKONbDY5K1v1I0zqhHWGtVmT0V3KYCNJ4szWjMMnh32SBrDWlpEucjsAx8YrccCz2jTjMRJbrjb_CU7sTqI1HOYrq1vuJ4f3RdCmArcxa5aUzlmcqYNQI8MthnOhEnshrG2Jfb9ivUZz7elYa76b1EPCXoVvHi9z-snDhDmHBsaKE4euXKpMpd2avV-xegPKPxMQzMgZIUrUto8I8k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی : در دو جنگ گذشته، «مذاکره» منتهی به جنگ نشد،  بلکه «مقاومت»  منتهی به جنگ ‌شد.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5519" target="_blank">📅 00:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5518">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=BUfqLCQkNIFspjwpXUc1fOYDG97yYHhgDI6icV7WS0SA-ZnGszmfhcf8VDvmGR6oQCWITl15ZzSz5FMwOTnaSTe8SC7W5piwXB8poFXTBRd-9x_UgJIILI58zxE8W5-BeM0j8j_yJSG4ozJQqkQQD-Gz0ELVYSc9hb-QCBXeQM7NX5G20cLrI0Jl3XJGDcjO3pIzIu52OiiV8BPzkLEJ1zLGeyznj42Xh2k0gLz3g5KjS8zQj6teztaH4fgsBpxbnuRfpg8BxeCY9KZfcZOSUdrOcD9wW_skqQO62t0jzAK6BzzE4MWkDYBD7FSThPajgCvK57HhB05Cj1PDXPpxsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc4528c0a2.mp4?token=BUfqLCQkNIFspjwpXUc1fOYDG97yYHhgDI6icV7WS0SA-ZnGszmfhcf8VDvmGR6oQCWITl15ZzSz5FMwOTnaSTe8SC7W5piwXB8poFXTBRd-9x_UgJIILI58zxE8W5-BeM0j8j_yJSG4ozJQqkQQD-Gz0ELVYSc9hb-QCBXeQM7NX5G20cLrI0Jl3XJGDcjO3pIzIu52OiiV8BPzkLEJ1zLGeyznj42Xh2k0gLz3g5KjS8zQj6teztaH4fgsBpxbnuRfpg8BxeCY9KZfcZOSUdrOcD9wW_skqQO62t0jzAK6BzzE4MWkDYBD7FSThPajgCvK57HhB05Cj1PDXPpxsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت نبویان از متن توافق ج‌ا و آمریکا :
یک : طبق متن تنگه هرمز باید باز شود.
‏دو : تحریم‌ها برداشته نمی‌شود.
‏سه :در مسأله هسته‌ای مستعمره آمریکا می‌شویم.
چهار: آزاد سازی پول‌ها اعتبار ندارد.
‏پنج: هیچ ضمانتی آمریکا برای اجرای بندها نداده است.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/5518" target="_blank">📅 19:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5517">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">وزیر دفاع اسرائیل: از جنوب لبنان خارج نخواهیم شد!</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5517" target="_blank">📅 19:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5516">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5516" target="_blank">📅 19:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5515">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک مقام ارشد دولت ترامپ گزارش داد توافق با جمهوری اسلامی شامل برچیدن برنامه هسته‌ای ایران و پایان دادن به حمایت مالی تهران از گروه‌های تروریستی است.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5515" target="_blank">📅 19:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5514">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
عراقچی : هرگز تا این اندازه به یک توافق نزدیک نشده بودیم.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5514" target="_blank">📅 18:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5513">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JROqX9nSXWzLBuF_oWR_ORjB4s1vZ3I-ZW7ljo2aHpR1kZhrMsnOLsctq73XYZThUqJUS7SWx8Y51ojikaHHy-29cFrn3nSHlgw0FNedQnrlPvpFZYrIkYnkPuD1LmotwoTr_nNlaKdbBNbt8-Kyxa2XKzNMkyCog0cuYNj5VV9hbLACwcafhnVudvO4HmaZ8qhWjyXR6BvjzIyvlXVRT44aj2M-MK1E4SVkQwz39NqnebMTkMbLxc5pONZcYbLk6wxAjEDaJM-ZfgKEQlKerfSWyu2UYBK_h-bW-jXqCKgkDW5j2mq-Kk6XVXt1ZtXjluP4XlZdabvvpPjMLdqQMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ : این مواردی که جمهوری اسلامی منتشر کرده دروغه! اینها یه مشت آدم بی‌شرف هستند، اصلا نباید با اینها مذاکره‌ای بر پایه حسن نیت صورت بگیره.
حواسمون هست که دیشب هم با پهپاد
به یک کشتی هندی حمله کردند.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5513" target="_blank">📅 18:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5512">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=pXj_nTNLbqAKCqzkZufLpTb3dxkSpjG8MUlU7ooRsXENDD-RSZ4ge9ApZ5Veqnb49ahygTjzNSV0rL5DA-_13PLigqSfsbL7ui5Wfu8lDxka1KB0_vESwf-SwgDkqDAUohUrHqbBYo50Ufaevwg0sfLGr225W_Xe7fDUTT68dnWj_iPjct5AEU9MO5gsRdgdWw6F74uPwa3ReCUPaP9afANe8AD6vK5kVT96hprgRQ5BxDFnA9WKnLfekaj8fewnFrD5sbCXVUY5b2OHtRX3hshEQGUNX789wItB8GWqEYsm6Hw-r7PdN8J4ff3bi-itTMcDQmPeCoNbkojW7pA-UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6c4edb632.mp4?token=pXj_nTNLbqAKCqzkZufLpTb3dxkSpjG8MUlU7ooRsXENDD-RSZ4ge9ApZ5Veqnb49ahygTjzNSV0rL5DA-_13PLigqSfsbL7ui5Wfu8lDxka1KB0_vESwf-SwgDkqDAUohUrHqbBYo50Ufaevwg0sfLGr225W_Xe7fDUTT68dnWj_iPjct5AEU9MO5gsRdgdWw6F74uPwa3ReCUPaP9afANe8AD6vK5kVT96hprgRQ5BxDFnA9WKnLfekaj8fewnFrD5sbCXVUY5b2OHtRX3hshEQGUNX789wItB8GWqEYsm6Hw-r7PdN8J4ff3bi-itTMcDQmPeCoNbkojW7pA-UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات امروز اسرائیل به صور
دیگه نمیخواید بهشون کمک کنید؟</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5512" target="_blank">📅 15:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5511">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
رسانه‌های حکومتی :
جمهوری اسلامی کنترل تنگه هرمز را رها نخواهد.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5511" target="_blank">📅 14:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5510">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iq5HbHEhPegI6uQlhloyFBa-GSzrbpQCrtsbnOTMjYW9gQI5ABMedBKtt2iKIrM5ebouAxhTHQJFQCTaOjuVmLiwPrIKuOhSOOA5SwKLnUY6egeer4qBY0IZAvqYRY1N7AcRvIadlZptwOU1-YpOFg_fOpjnzLhmN05JkRTsId5FqXIjg1LMWqXLYemtks4nge8-TarZaDAN-rWnhOjvz2Nt5H1lQnFXqpfZPDF7A1bfIAhh3pAv_0AuZ03EsH1g8osJ1i4i_ZZ4LvVgSyUdo2OGTZs8476E9k9EOJPrjnG-57mAcbtP1MHYOIODXz4HaZjISFS_r1x66Pms4ldDvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
قطر خود به تنهایی حدود ۱۰۰ جنگنده بسیار پیشرفته دارد. شامل ۳۶ فروند رافال، ۳۶ فروند اف ۱۵  و ۲۴ فروند تایفون.
🔺
بریتانیا برای حمایت از قطر ۸ فروند تایفون در این کشور مستقر کرده.  قطر همچنین میزبان بزرگ‌ترین پایگاه نظامی آمریکا در منطقه است ولی اجازه استفاده…</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/5510" target="_blank">📅 12:43 · 22 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/5509" target="_blank">📅 09:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5508">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=CIvDh87ccqHUjEQSbU2c4kpUlsQuGMVHQFcU15AorWJ9PdcnqHSQm8uLst4U2JVf9tQMQY4pkyK_3FyHkta3V3JklTGOcZ0K52H619hMmmCOPfrXD2d6Sbw7bzGo93AWuTjCMD308kbMMbssdE0qFL_rU0eKggl7NUZiyRh_arw-72ZKo_fWwUBegUkX7ckq9Pr7WGpgk1HZ9eSE75szOeD1HIV2xeybU-ge3gcZL4ej6zD3PFIk21YcoXABs1MperStJyRsM6VgwqJO9ljc1HXa4XWgUwVTYNBY8fmoXJxlTahYNWCeUCohOmYeZ4rV0h2EJ2KXJlHaQbwwpk5sGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf945e54a5.mp4?token=CIvDh87ccqHUjEQSbU2c4kpUlsQuGMVHQFcU15AorWJ9PdcnqHSQm8uLst4U2JVf9tQMQY4pkyK_3FyHkta3V3JklTGOcZ0K52H619hMmmCOPfrXD2d6Sbw7bzGo93AWuTjCMD308kbMMbssdE0qFL_rU0eKggl7NUZiyRh_arw-72ZKo_fWwUBegUkX7ckq9Pr7WGpgk1HZ9eSE75szOeD1HIV2xeybU-ge3gcZL4ej6zD3PFIk21YcoXABs1MperStJyRsM6VgwqJO9ljc1HXa4XWgUwVTYNBY8fmoXJxlTahYNWCeUCohOmYeZ4rV0h2EJ2KXJlHaQbwwpk5sGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاور قالیباف:
دو نگاه وجود داره، نگاهی که میگه بریم صلح کنیم، بسازیم، یه جوری مشکلمون رو حل کنیم.
یه نگاه دیگه اینه که صلحی در کار نیست!
ما قراره با اینها بجنگیم و قراره اینها رو تسلیم کنیم در برابر اراده خودمون.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/5508" target="_blank">📅 08:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5507">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=NNDncAPTORDgzgjZgs-abChn4EMp-rWvT8m4ll3FADzG-BSHYUtvBhU-497Sl5uxOVfrWFewTxQuAySOvnSOka8CW0abjo72TTGqYIg1_9w6bB8ipE0SL2tFJrd27MAFUG2YyCjqy0vxNVt-ManOPhoKvUZtAtZ45txg0nU2wXbbEhU7-eAAYel-UB-ikpoFFJ05ge1fUfprsddJnbIVKiHLXVToMEBb2JQ7PAQaoIEvgOnnb0tMAkaWCZvjg1tcWbvq_VEJzhMu5_LX5S3BdnlZcfEorZIzm6s9xgQwzffdSHQ3Ehs76gOukKEQFfBPJ2w9IJXF3FbvkwR6NWrWow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e16eb454aa.mp4?token=NNDncAPTORDgzgjZgs-abChn4EMp-rWvT8m4ll3FADzG-BSHYUtvBhU-497Sl5uxOVfrWFewTxQuAySOvnSOka8CW0abjo72TTGqYIg1_9w6bB8ipE0SL2tFJrd27MAFUG2YyCjqy0vxNVt-ManOPhoKvUZtAtZ45txg0nU2wXbbEhU7-eAAYel-UB-ikpoFFJ05ge1fUfprsddJnbIVKiHLXVToMEBb2JQ7PAQaoIEvgOnnb0tMAkaWCZvjg1tcWbvq_VEJzhMu5_LX5S3BdnlZcfEorZIzm6s9xgQwzffdSHQ3Ehs76gOukKEQFfBPJ2w9IJXF3FbvkwR6NWrWow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی ظاهرا متقاعد شد که شرط و شروطهای ۱۰ گانه‌اش رو کنار بگذاره.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5507" target="_blank">📅 08:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5506">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">صدا و سیما : شنیده شدن صدای دو انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/5506" target="_blank">📅 01:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5505">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
ترامپ : توافق با ایران باید همین چند روز دیگر امضا شود، با حضور ونس و در یک کشور اروپایی.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/5505" target="_blank">📅 23:19 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5504">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
نیویورک تایمز:
مدتی کوتاه پیش از آنکه ترامپ حملات به ایران را لغو کند، با پاکستانی‌ها که با ایرانی‌ها میانجیگری می‌کردند، صحبت کرد.
به گفته یک مقام ارشد دولت آمریکا، پاکستانی‌ها به ترامپ گفتند که «ما با ایران به توافق رسیده‌ایم».</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/5504" target="_blank">📅 22:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5503">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، به نقل از یک «منبع آگاه» نزدیک به تیم مذاکره‌کننده ایرانی گزارش داد که رژیم در ایران هیچ متنی از توافق را تأیید نکرده است.</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/5503" target="_blank">📅 22:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5502">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
اکسیوس: ترامپ حمله را لغو کرد، چون قطر گفته بود که به یک توافق رسیده‌ایم و فقط مونده امضای مجتبی خامنه‌ای، اما حملات دو شب گذشته آمریکا،  هم ج‌ا و هم قطر را نسبت به نیت واقعی ترامپ [که جنگ میخواد یا توافق] دچار سوظن کرده بود.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/5502" target="_blank">📅 21:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5501">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
ترامپ : حمله برنامه ریزی شده امشب به جمهوری اسلامی را لغو کردم!
گفتگوهایی با رهبران جمهوری اسلامی داشتم.
محاصره دریایی اما همچنان برقرار است.</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/5501" target="_blank">📅 21:08 · 21 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/5499" target="_blank">📅 19:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5498">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMD9t2ueDphKNsWCOUAKYmk05hVKkkRRJoCY-nxiaN_RT1RswVBDY558Ma_VaOcUKX-sFGHJAYg3pLE6-cgdDlkTnjRiPbmJtIBH1B6rppvR6ciwAzG8VBY6Gwf9hkp-h79SnRjQWGDMZfIDwFZbGtf99ogYk3eYCKQ__rKV7J3Nogc4UxEJ-q79dmljz3G1ylwhdJoEYBDvDlv371c8KHA14kxs05qDyOymlpdcrPq-PNG7fXPXUGD4qdOSN2FWVTPk8CIdedxEryvpe94HYB-kSNmERbUetrNGblMns3s8LyumTqI9BlcP7-Fpxcwk0wKQfz8gDhyUWMG70-0ZmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله دقایقی پیش اسرائیل
به شهر صور ۶ تن کشته شدند.
یادآوری : دولت‌های لبنان و اسرائیل  هفته پیش به یک آتش‌بس رسیده بودند
ولی ۳ پ با صدور یک بیانیه،
و حزب‌الله لبنان با صدور یک بیانیه
با این آتش‌بس مخالفت کردند!
جمهوری اسلامی میخواست آتش‌بس
در لبنان رو خودش اعمال کنه!
ولی نتونست!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5498" target="_blank">📅 18:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5497">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=TGIfMs53MpLUKvtSMZibR4NFx93hq2NH_DlL275Rv7lKd8vV4S3kb3mE0ozvGZaeuoW9Bsu4Tm5I3o9siS-C_bAdvXS5hrM0FVwJ4Od5eYvfV5ProrAvg06t0UsjGMHXfnH8icurEVK4SkQdhlcZrxQhHFw1YegbS4z8uhoxO5Kjl5BFXJ214GnGvRaHvAMA-twBNxRNKEF_4RJC2O_gJZ0IRMHqw-Z_eoMMRRsffGatb8Z_uMI2rejoiFs8D_eU06EieupnUzAO9hfhILPIhVN28o5jV5k2U0W8shs78jb49zXXU93izTt4DDkhrwgdKqBEGNFR3DjrXrCGKUFNbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3662fbdb97.mp4?token=TGIfMs53MpLUKvtSMZibR4NFx93hq2NH_DlL275Rv7lKd8vV4S3kb3mE0ozvGZaeuoW9Bsu4Tm5I3o9siS-C_bAdvXS5hrM0FVwJ4Od5eYvfV5ProrAvg06t0UsjGMHXfnH8icurEVK4SkQdhlcZrxQhHFw1YegbS4z8uhoxO5Kjl5BFXJ214GnGvRaHvAMA-twBNxRNKEF_4RJC2O_gJZ0IRMHqw-Z_eoMMRRsffGatb8Z_uMI2rejoiFs8D_eU06EieupnUzAO9hfhILPIhVN28o5jV5k2U0W8shs78jb49zXXU93izTt4DDkhrwgdKqBEGNFR3DjrXrCGKUFNbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ میگه جمهوری اسلامی
باید بلند و علنی و روشن بگه
ما «تسلیم شدیم، ما تسلیم شدیم» و «
آمریکا بزرگ‌ترین قدرت جهانه الحمدالله
»
باید روشن بگن که رسانه‌های
فیک نیوز همه بفهمن.
😂</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5497" target="_blank">📅 17:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5496">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‏سی‌ان‌ان:
برنامه‌های نظامی آمریکا برای تلاش جهت تصرف جزیره خارک ماه‌هاست که تدوین شده، اما به دلیل این که این عملیات بسیار پرریسک تلقی می‌شد، پیوسته به تعویق افتاده است. این خبر را یک مقام ارشد پنتاگون و دو مقام دولتی به سی‌ان‌ان گفتند.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5496" target="_blank">📅 17:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5495">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PpxDcXJc-JiupwoD4vyIIGVbeEHOxe3RbFuIBxb5p5-Qe9PwLjW2rK3iI_6Rs_PMkYPXQ9ICjenM8dQmsTGaNWejBcN34Xzr3ZdbpbeJ0zWDsz7PaB1G-GfdAKGKHVpDkPJ0mXg8kG7oFwroQFXpAcBwJfLfcBoFV5U15MwV-rB-IZEfbc3An60R9n8-38oLhUcN8JKfDndjLJLJ6KK7vBfvH6qzHBAxVcR-7u9qQsT2sEjdCMjRrBUqt9ifmwxeFdMuupCQNxoSvervzp244UVdfDK2U2F0oIvWTOjmARug4XkOEJf624avjfa8RoiE8UGhse1sH3H6OzSdxdktgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه داری آمریکا : خسارات وارده به متحدانمان را از حساب‌های جمهوری اسلامی جبران می‌کنیم.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5495" target="_blank">📅 17:25 · 21 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JgPl-pIIVkhCwFHg9RhuBfsi2hCrY5CIGDc6q64goppvaQZ8cdlRxglRodt36PkwUn3CYYTa8gw-0YuUt1_ob4zGKCQg63IZ9xDYm1pSrhWZI15PsVIwtyOfEBCmfxbl6cEJLTSD5adtjSLe7n0jlwBn9o8PWjYGzmgIfhoV-WZ1Lfv3PVRTJWy1EQw2SNewIchFDQ-TUZTTacvin80tg37l-gh-xEu0TctXFcYwFW6xVtMM8pGbAw2t3WZyyaSu_3lTmxl2ol3m1Z0GYqqCr29bHm-QE-PnIQpSBDhxjZF1uCdPpA6-niiTJsd5RtcpHNH06khP2Jl4xFY2hSCX7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از انفجار در سیریک
مناطقی که در دو شب گذشته مورد حمله آمریکا بودند در واقع حاشیه تنگه هرمز هستند.
جایی که رادارها و سایت‌های موشکی و پهپادی و…برای کنترل تنگه ، متمرکز شده‌اند.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5493" target="_blank">📅 16:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5492">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QBkS5vcWSsrohS0a783sbmr442OBWCJr2kthbrgIyLsVqF7EI9ALxs458xzB8jAwtK7TrfgV7h-CnIG_sKaK5M80f0AK3gvbHykZkID5vPrSaGyco3mT7yDgYtWLfA698tstb3RttJjyR3RWwFTQ7Mp7sQ_LXBDV__mwEfr97RgluTaIb3I9hYxEJJGFnq8VQUxTpK2PNWhJfWEvllSxY6hoAZXaEeN_d29tLDNS2n5oY6p3aHbpj_XNkKBlCQJrUg3mSbKIb-U0PzkWVHJu-ZHv2lqsdjHbSJ5D4qdU-384OzsZTfoS0zeaqd7LI2mWfXg1QN2jcy4U61G8kng4WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اموال ملت ایران! که یا مصادره میشن
یا مفت فروشی میشن به چین
یا غارت و دزدیده میشن !
بقیه‌اش رو هم‌ میدن «مداحان»
و «رجز خوانان»!!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5492" target="_blank">📅 16:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5491">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVP-b6B96n6txv1_bDAY5vXO0sFosOzp-IQukfF1JtvRCoHNWcO6Ipy9rtepDxiDcyMHHUy34UlmpRLH3QJ870YZKnAmqso_A24WDTdK81j0beModaQbRMMj_TA3DcBz8k5WX9ukCyAGrGphciS51RRZMtV5vzWuho242btShuLL9XBWPR20brJThVNNmN6ac6lOqUNVrASt1ce6w9biCbOurUlTV2fquHrTijLRqHAd-ihTTcqNKfKlHCD3_o_cB7gRmwBz283Xnm9JT9fbFcDZz9IStDDM8mKlWe7irqP27awcp5PPVQGjDecOj1eR2-23uFvQzPfXmG07TViK4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5491" target="_blank">📅 16:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5490">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e79KPfW57bGxftKAYceraU8lQfaWMANugCuw6HQ6QkSKh9mMj-zx1hUwoLolDaoYttPQrE_ZZXsodZnGGqcjZo59aWVSrmfMkcd4dTUVpqijToVdI_RLoFBxGta8px6QoPnOvGKXsdyzWvaDL70Lxpf_kNDnrNOa9giThCHmoBah_M1waNO0JtsKnJzN_gEfxjCzCrL1YQDaUSKzlUTUFCQ2bRXMoAeAlzJZSloSMiZBOsClwQqautrTfAVEfUzcDoOvPG2wL5q4CFygt7eOEqZAelObQa-iwHaZpO-wG54ANu74ces6JCI6vr2IvUJYyywFK7bFPMK8CgIbcm2bTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :  امشب هم به جمهوری اسلامی حمله خواهیم کرد. خارک را از دستشان خواهیم گرفت.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5490" target="_blank">📅 16:01 · 21 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXUG2eQWiJSZS4qLn7JV3RaNYeTC2GgAc0AIV940M709HTLCEtZDA5Xxv4C9xVQHqRJ2e7F0SfxjEyIjW5K8AvsXfD1x0yxAerjRAbedakYW9sl25MSv_JPRQhK9bv2VPrlJ-js1pvYklUK6c_v8kUgUkL1EYNiSVuW-62czsAXlyR1kkKrWvYzre-DKvHCYflA4m837JmUPz5SeZBwcb7bo0edFhcLSxJdOw8jy4UYTI9awU6fg6kk7vXMcds-D7b5zVWWioF_D3q8L-v-15q3wOsnUpP5UtDX80zWuJ1jqEHqSvsg5srTrwtVaf5BMN6TbUshduirTOBCsjHggYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پاسخ به حمله مستقیم جمهوری اسلامی  ۴ روز بعد اسرائیل حمله‌ای بسیار دقیق و هدفمند به ایران انجام داد.  گران‌بها‌ترین و مهم‌ترین سلاح دفاعی جمهوری اسلامی رو یعنی سامانه پدافند موشکی  اس ۳۰۰ رو که جمهوری اسلامی پس از حدود  ۲۰ سال تلاش و کشمکش از روسیه خریده…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5487" target="_blank">📅 10:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5486">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/163555b294.mp4?token=gl_JpTP5UCcsuwm33sYDPMKEfD4cvIxynGCAlDDvfvvffI7UpgwWkPjimg15Q7cDvvF0GCOMvbRnuZ41uvix4JXg55MvnXIKa4KwwsQybv6eidwvIyZ43UtW-p6u5rucyD1tlXwcAHENKb3Sc80Zl6Nj-OQkxNi3mVlK-h0e2oL4RgTL018pQgrF-OmpyG1GtxmnYdHiFRpb1CfSYS4Hv1FutcEFeguwp_R1yQez1d7y7KXI06s_baVak7aUODs6J_RG7LOiP0GPn5JnGl8bPHSbejQbMBh9HOXDlBE224uu4XQ4iZHEHXGA0kLZWX63Stn576O-y-5NY6vk2DpCHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/163555b294.mp4?token=gl_JpTP5UCcsuwm33sYDPMKEfD4cvIxynGCAlDDvfvvffI7UpgwWkPjimg15Q7cDvvF0GCOMvbRnuZ41uvix4JXg55MvnXIKa4KwwsQybv6eidwvIyZ43UtW-p6u5rucyD1tlXwcAHENKb3Sc80Zl6Nj-OQkxNi3mVlK-h0e2oL4RgTL018pQgrF-OmpyG1GtxmnYdHiFRpb1CfSYS4Hv1FutcEFeguwp_R1yQez1d7y7KXI06s_baVak7aUODs6J_RG7LOiP0GPn5JnGl8bPHSbejQbMBh9HOXDlBE224uu4XQ4iZHEHXGA0kLZWX63Stn576O-y-5NY6vk2DpCHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی از ۲۵ فروردین ۱۴۰۳  رویارویی با اسرائیل را از جنگ نیابتی به یک جنگ مستقیم تبدیل کرد.  در عملیات «وعده صادق ۱» ج‌ا با ۱۷۰ پهپاد، ۱۲۰ موشک بالستیک  و ۳۰ موشک کروز به اسرائیل حمله کرد،  دستور حمله مستقیما از سوی علی خامنه‌ای صادر شد، و جالب اینکه…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5486" target="_blank">📅 10:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5485">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RruJ0Kfkkm3Cd865NHH3hKWaAnQKuDCDXktB_TXkbrd4a1z_VhvzfxKRBJxW35qzcDdqsbnGIFg63idpnPQI5h-brLwerRsU1IVSHYpWrvyH-ULphp_OaPu5VlTEWYr_Ke7VrTyV95Ddhyn0RKSKRQsI2kwtsG9HWmRzruytA16TCmJ2suP_LkzFVKoxMhnCsHFTNgApN6KsG1uX6HOyrkFgJ1eQe8YvJwFG_EiIfCCs7Y5L74CntmZ0Ylv2ydM2OKluOrkScPCKNR5IdTXd25EE6BM9xVnQ7TqmeAF-bZQNl7i5uDUAjBxae6RIIng7gmAf01wkD9QHFP2UJkUC_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ غیر مستقیم با اسرائیل سیاست  جمال عبدالناصر بود.  ناصر فشار سنگینی روی اردن و بعد لبنان آورد تا اجازه دهند، گروه‌های مسلح فلسطینی از مرزهای اردن و لبنان به اسرائیل حمله کنند.  اما مصر خودش چنین اجازه‌ای رو به فلسطینی‌ها نداد! نگذاشت مرزهاش با اسرائیل دچار…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5485" target="_blank">📅 10:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5484">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UO_8i_8Bx73vr4WkubL-V_a6YYhh7ERUiqtevWL20VLll9VqJnzMqDIdGbgaD5Tfj97CkXnlYvQUaw86MDy8SrNta-fd82sZlTtyj211p44gani0Gh88qO63qsdhNniDjCNaZisXuStbuRaLoNlZlQGPacG23eJOFVNyVQK_zq03hgFw7ni5O6SNPsM1kNPz7Xa4Rn0DadBD0vobZ2atqC-e5YQNSEWdUnJkp7G2DcxwqnPjYaG_izE6KbfVmvCU4U6647GkqurNo-zNqXDFsEQMS9r6FJn7OOhdvejOgVmdtzBwH6BiLxskWj3zAAOh6_36tdIOPiD0UL_-GFwAaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی در ۲۵ فروردین ۱۴۰۳  برای اولین بار رویارویی با اسرائیل را از یک جنگ و نبرد ده‌ها ساله «نیابتی»  به یک جنگ مستقیم کشوند.  تا قبل از این تاریخ،  جمهوری اسلامی با مسلح کردن گروه‌های تروریستی مثل حماس، جنبش اسلامی، حزب‌الله، حوثی‌ها و….. با اسرائیل…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5484" target="_blank">📅 10:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5483">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDBgQdYOd6lb-ZZmDNS0u3ZvKPAYyr5j74bLe4ci14_lvChjfQtDns8yUjoxPsD-dGN6hMHx66hZ8WELjG-RwYHRbDqzYfmCEqSaLgP5sOFtNEYIf3HCAnJYtSKMXm5aD2iU88xJfOD-IqEggl65dUeSzL7quo0ypTFYrgF8YpzjQYuYF45XNwAdqfl8_YY4RsuZcxyXQF9YBr6k5WnCagixaVL5RO7LcFf-zbmR3QzJlm89-cORtxB1gwtakZBZ2eX3li-JfV7ku-ln2siHnigBSqj3EUsSQBlr30xE5o8oAhEx2SNtcKEskHanFTPNEOP2654lsYMfOoKmzJaJSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از مهم‌ترین پیش‌شرط‌های جمهوری اسلامی در دوره جنگ ۴۰ روزه این بود  که «جنگ باید کامل تموم بشه»  و آمریکا باید تعهد بده که دیگه به ایران حمله نکنه.  منظورش این بود که یک «آتش‌بس» نمیخوایم! «توقف کامل جنگ رو میخوایم»!  این‌ درخواست از اونجایی میاد  که جمهوری…</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5483" target="_blank">📅 10:01 · 21 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5482" target="_blank">📅 09:58 · 21 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/5480" target="_blank">📅 01:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5479">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
گزارشی از حملات شدید به قشم</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/5479" target="_blank">📅 01:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5478">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
شنیده شدن صدای دو انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/5478" target="_blank">📅 01:08 · 21 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/5475" target="_blank">📅 01:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5474">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در سیریک</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/5474" target="_blank">📅 00:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5473">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
خبرگزاری مهر : فعالیت پدافند هوایی در غرب تهران</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/5473" target="_blank">📅 00:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5472">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JsXLQ7Hdlyu5Gi2YFNJY0caO8TPLOqQwdni7imaiCcQdNo3aJgib0ApwHeogz1ftsXEMAlB7BlQG_o_ioG6_WCOqvH96eselc3zCQzoUk2eR-u9XuKMY_xPlf3vZb3XpGLHRDUOWFsl2fBDlfHRIvsUnfBiJ2fbFm04WXmN-rWaQt-dNgwzgZ5mJUY7e1nX-3xKwB9PEvjkM8QczBu_i71uEQjWeoLlLzGnaWLLBZ4y4Itdr0gR-gWWRKNYyJdp3uHTag34ChB2zuO0jNmOO3oSHciJWRr8TlbpV_U1ofTxV1BI-KC26-tNiHF3FhikRZwAPzqepK3IM4oQltP5Mxg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/farahmand_alipour/5472" target="_blank">📅 00:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5471">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
ترامپ  در جلسه‌ای با مقامات ارشد نظامی
- امنیتی آمریکا در «اتاق وضعیت» در حال بررسی  یک اقدام نظامی «گسترده» «اما کوتاه مدت» برای ضربه زدن به جمهوری اسلامی است تا سران ج‌ا را وادار به تغییر مواضع خود
در مذاکرات کند.
🔺
ترامپ همچنین ساعتی پیش به خبرنگاران گفته بود که امروز ضربه سختی به آنها خواهم زد.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/5471" target="_blank">📅 00:11 · 21 Khordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/8d07d6979a.mp4?token=PC2peBTjxQv4qACQHAf5IpE0tq8jgMuQ_OcKWs9tOiu4rTepMxWApBd5HZIB1qEtkY1gsBn69kgxQtIDx5-yFW6mBQSCjIHHP1uaGe0x3NSDZFxL5ClVorRUpllac3qkg4JE_6nHvzubi_Z2FiSmNRxq9fjeZ2w5TTbcMQaQOnrzwsqp2s_Bd5uU427eoR4ACvJKDVRa4KV2vVH2UIY1uEsQ44buyD4UgCIJFM6jPai2DylvE6_2WqTxQ8-LNb_BNjxoklCJf6YhmCzGlDPyb9pChijl18DRY4ealuGKSxndGwAv4ZHuqZRV3mShwrZfOVzxBhtgLDC9iLzYwrVt5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d07d6979a.mp4?token=PC2peBTjxQv4qACQHAf5IpE0tq8jgMuQ_OcKWs9tOiu4rTepMxWApBd5HZIB1qEtkY1gsBn69kgxQtIDx5-yFW6mBQSCjIHHP1uaGe0x3NSDZFxL5ClVorRUpllac3qkg4JE_6nHvzubi_Z2FiSmNRxq9fjeZ2w5TTbcMQaQOnrzwsqp2s_Bd5uU427eoR4ACvJKDVRa4KV2vVH2UIY1uEsQ44buyD4UgCIJFM6jPai2DylvE6_2WqTxQ8-LNb_BNjxoklCJf6YhmCzGlDPyb9pChijl18DRY4ealuGKSxndGwAv4ZHuqZRV3mShwrZfOVzxBhtgLDC9iLzYwrVt5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله هدفمند به یک خودرو در شهر صیدون لبنان
برخی رسانه‌ها نوشته‌اند که یکی از اعضای بلندپایه حزب الله در این خودرو بوده
هنوز جزئیات بیشتری منتشر نشده</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5468" target="_blank">📅 15:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5467">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2qsdljR5_kgOHMJTsdCO8IBMAn3MfZayGe4_EkpGEnEHmhfA4OemYGXXuVn0FNr9yCepjXQ4k7iK9P94d22wiu-Eg2JMcdesHmZjlqOt6z1DF_EhkQNUQnoMx8mqxVlOSjqrdtOBCyxx3E79nITAoXcjVCdESp4wCaWJPPGejB_QBjtPoDW5IAUq4pe75jquV5zXvXZuiqhxjpxWjvTkhbOBDBEu1csf72ZUWixRK3n4AzvnNdrqd6zQpiqAc3bziMtyCQlrF82HW2NxCRKt-3GN6kksl5k5H7Mbh5YWQuF4vhcTXnyYS2ExbjUH3mOl_e44YBmpdABIaL08w4u1w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nzkbBMh9IRT9HulVicN8VUvXr67mdpjOYebvx0uaYGFgHC1DC0fenbMKoeSH_6HLNeHlLP-Fhpiz_0vE7oqtI1NycwnmCSCLTACITyV3YVn-hG2Q7EotN9XcK9h4V3fR-by5rnj2sY2vVAIl583iBihAAZ5bnoDZqQHbE8vm2CkLrPnRVS5MQVFDbPMdmTZ1nyvfJJypad-oQuDmPSZA8oLevuWoeiocL3va5hkFeyGcZsu_FWMOB6LEh-XreyvJ8ETbeysyv6YpuLWgI2uB1iY36uSfn1fEmthLFbdxHB3izWKNazjdtQ-ccO7AiLrmwh2X8keyzZEBDhrVea8nxw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5465" target="_blank">📅 12:47 · 20 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hkJInrIGEqj64SqZAAhvOrQDYwasUNeb8V-aGGb5RkBGw0o1qjjBIJXeVZ3p27W7-rpHljJegaxfdneVTa8FN3KihhASqRBgOrqDvioXsFyEuDWfnp0AtDwa3Ka4nQ4jdi0o59_sECVtTDLd763I9HOc3rEO9cNWcmpxLgJTt_YbJJ0JXw6fkFWZunWYyGMwq26wmsMmd5NZctIZtJ3pvCh34typ4yQjMkFYvqaYbjULhTYXDQ41vP5NUs0bI4fBbqUoba47Tcvsk_R564pY2ZpxSmpwtjsIiJyAlPOXiPRuyuD1JmLSVAIIKKIBxcJ2F8OoAY4_1pS4AFKSGuSOhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل به دو روستای شیعه‌نشین
غسانیه و حومین الفوقا در جنوب لبنان
هشدار تخلیه فوری داده ، اینکه اطمینان داشته باشن
حداقل هزار متر از روستا فاصله دارند.
این دو منطقه در مجموع حدود ۴ هزار نفر جمعیت دارند.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5463" target="_blank">📅 12:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5462">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uw_sNUJSZ-1crA-yByNfVG9xLL_VdVc8jMNWAAMlixQO4tUZpa3VVbJFl-O4FVvZS4hNlpuxz0RWSR5tFI7XgPOnAf_7IRyreheEGIHlELZeXYd_GN4Jf4ponoeipKj7P8ftpQG1yu0PgA3nc3i4TvvHvx0-4JBSHIRVjhf4gGlCQqv8XBW2_1PTXf6oV5ZncMvrydNpyw4HCVQYbr8jpDs_s10XnaU-tjnD1v3TEMn16Aeg35LcvD6JpJNxgJBcitae12439jzUI1S1YffTeVWRkJDfeMQwDwD9Pqp-JlEFqKuBuEuphdoKqviDtTB91lwmO6h9sn0jPcTwGwvkWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب! چه نکته جالبی بود
واقعا چرا آمریکا خطوط قرمز شما رو رعایت نمیکنه ! غرامت و تعهد هم که نمیده!
اسرائیل هم که معادله‌ای که در لبنان اجرا کردید و براش یک پتروشیمی در ماهشهر رو هم فدا کردید‌، که براش تره خورد نکرد.
عجب آدم‌هایی هستن!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5462" target="_blank">📅 11:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5461">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uemnjTuOOE09ektAjHPV6mtc-MOWvBP5b9qxxfX0uGmQuusS-rp5X3WtRwce2aPyl2MnWTgCOWR3O0-0MY0QlO6UiauqTeGd5jM9hiiFO08qyTBrxzpEnEfqG8K2YZ5aGtZgQDVT915asDkbrAK3slPkQ-1cxnIDvrwsTRRZ__PXcAj_qWHUW394F1ktDHOKEgnUdiaafkh1qg7iKolArEDpHVNEW-ME59mxsTBcvsF6IKpZrtIfcxZQ0pP-ratv8CKHQVdw496ZXu6TtjmYwv3078YRMCCoRiQpmuQlocluHY1LH2TUrASp2hI213z6mnYwRmU5MAtN4v21UXx9Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خبر فیک به نقل از یک اکانت دست چندم، که اینجا نوشتن رسانه تا بهش اعتبار
و اهمیت بدن رو هم از دیروز
منتشر کردن برای اینکه بگن
چرا دیگه  به امارات حمله نمی‌کنیم!
چرا فقط کویت و بحرین رو میزنیم
و چی شد یهو امارات رو رها کردیم !</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5461" target="_blank">📅 10:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5460">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">توییت ابراهیم رضایی سخنگوی کمیسیون امنیت ملی و سیاست خارجه مجلس ساعتی پیش از شروع حملات آمریکا  به جنوب ایران</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5460" target="_blank">📅 09:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5459">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eEn_zfE8B6ZXN-5uZSTIvl4CCCfxJ-LxwVcy5fFKmKc0Q-mG5g1u-non2xlm8LJ09_t6XoRbeuWbAnrJe_9g4WDAM2oiNT2ycSAtbUhiZjlggvtKct8UvQYciXDHk5Qv6RFzjTLgdIqRwkZjUZ8LPw_yC30YIzdl2qu-cF4gIta4nLEagJhhFB6EYChc3zNPiDcZIsyoQEOWOo9yc7hhAqKTLRj5aa5CgTOW_yoV7uHyr8hmRiRpMwmPD6unJYlpm0uwBpJdkpmOFG3QjS4GwB-pWKEmzAJRhcTzHHeSbhP8E9uAmYrH4HfHvxI48mgc9yJN5GwOcGuhP3SUyhO-bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات گسترده امروز صبح
ارتش اسرائیل به جنوب لبنان،
مقامات جمهوری اسلامی پس از حمله موشکی به اسرائیل مدعی شدند که «معادله‌ای تازه» ایجاد کرده‌اند که اگر اسرائیل به بیروت و یا جنوب لبنان حمله کند، به اسرائیل حمله خواهد کرد.
اسرائیل اما از دیروز بر حجم حملات خود افزوده و ادعای جمهوری اسلامی را به چالش کشیده.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5459" target="_blank">📅 09:24 · 20 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RUAnKpz3vLv8pm12L3XvfdLEjECSPmZyDLPWx0iKzoEBHVJm7M_RifZSOjCvLGhzISGAMZWV-_qR2uHZwcr4bqcSU3BQpy3zpVUVI1pc6DaSxXZ_jji9xxTsqglWqvQ24_9FaNrltFS1KKz2Ebrc-_4OlU8K7M1M-4hUkvQThi0joyTOif6HxAXr2adPx_cDL6HO-ApEGJBquWwhhjs42EZZP1S4dZAYktWueopLp7scHjQiFqLBLBBzLkpZ6geyxJWcsVKlVpbtWxmfW1SpwYZITTwn1VfQssrygbd6QKZbIbSXjUbsxlKQLr10a3U_C1ywSNS87uDvaJnIt2UosA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخراج رضا دالمن از دانشگاه شریف به دلیل آویختن عروسک موش
او پیشتر به مدت یک ماه بازداشت شده بود.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5457" target="_blank">📅 08:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5456">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YC7uutuRWZb3aKjLGRv3jNR8H5VSr_IuovolCRWx5Hk0VUO6dS8RG3PbXsCgi5DWztTBgvjsOhijiZaTwdHcYdNkcEEz3S078jSfFEyYhyfnwtwg61JPD84sWyZmE8EK5VwGHYRgqBG7kRTayRs5yQ9TJwsdIVutv3EpNMbJJ16biX8EoOBwyneG0psDGNpbNffM8S9z_yflYFhr8s4gYsLNMIl0oSk6liYdl-2pCt62ZwQ4O8s8bSN_cwoj1AOolW8HD41NwwMp7w9ZEJg5k4JWnEopxRi9PNwcQP-XjiRP2AEmUHg82R8hK0y4FZu6GdoZBH9d0PxSyB-2TVlvEg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5453" target="_blank">📅 00:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5452">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
جمهوری اسلامی با چند موشک به اقلیم کردستان عراق حمله کرد.</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/5452" target="_blank">📅 22:53 · 19 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l7lFMy7PoIJDNi-HGEnLFlDo62FPK0Dn8o27KLpQ_FuIA5KfjFPX1T37FKBfMffK3giLAxc6vU2-JcjwUCRmxHzx4kj0sRZ9L2gJTRpNauC6ViF8tRPxVO8RYVreXBZv7CvjCWPHm_Jo_qcckFEOp6mIGaHF4DFwZdB5hiKkUfyozA52M153WBynvR3QAj3KGYdhVl2LFAOhVNvG_V0uYSPGNIH5Ljx7po8y3rkGl4gLF1wlIPTyF2QsJ_XlvMw35O3dc2VivoqlDhdB7OCNKzhkSVH6etSpFJ0_qyg6Yg7NuSW12aN7KTesthattFGtRczVOrl7qskFmovOH_udlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/5449" target="_blank">📅 20:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5448">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/otA-239AC4sWDme4g6A4-5S0bZmeCxl651aktzDmLSOuSzhQVuCePAaspj2Dry-falksqTDtPPd8vcItiV8nXAjlboZwrxG889r3KcileuIMptk_0PviDfZCgkt7sa6rpGeoTi1elkgDMTdLGX9iVgBpCM2tXAnUouKJnveTT0Akip8DpJ3hfgSPcbqpt4jvHA0kezy7_aKjquQVdaXRNTQINNrM1xfqvX0oIwkVrWpVaJwTG_NlyYLrdXS3_CTUWc_tC6N1cBl3OXPiJhvs9JB7abLhmbHCP7ndXGEUZOPa9PE6b67YHEa-GSGFlC0Og2HdD84Hb8g0qoU8BJscjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : جمهوری اسلامی شب گذشته یک هلی‌کوپتر آپاچی آمریکایی را بر فراز تنگه هرمز سرنگون کرده. هر دو خلبان سالم هستند.
ایالات متحده ناگریز است به این‌ حمله پاسخ دهد.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5448" target="_blank">📅 20:13 · 19 Khordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/4718cad225.mp4?token=E6HzPgOoN96jrAxtl0GdELIxeaWjYij7XIJZio5KHL1vNVJDGyaoN0wN2eWhfdhoXHmAINvE10hXsnr1pCFozHgfh4Cl96YYjTfgNHVoCP0X-PCcsS6Ip_Do43nGyyYPI_4QMT1RIHKHImLBCgrzme7hF0fnHsc1GS0uOY7fC4NrL7bLLMnocPMdVhHUnvGNL0JtcQVUmunXEB9tIPK9Y--MB-6ooikG9kw9_kYzNhrrUQQf2ij8pSmT7K4-IpDNjDoV4dWjiqH_7kafADZ1yci0Mkn39CXP0pLd_G8POIVCvvclPOFhPWs4bwBtDnCMI1oACeoz4HYc9nK23fkoEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4718cad225.mp4?token=E6HzPgOoN96jrAxtl0GdELIxeaWjYij7XIJZio5KHL1vNVJDGyaoN0wN2eWhfdhoXHmAINvE10hXsnr1pCFozHgfh4Cl96YYjTfgNHVoCP0X-PCcsS6Ip_Do43nGyyYPI_4QMT1RIHKHImLBCgrzme7hF0fnHsc1GS0uOY7fC4NrL7bLLMnocPMdVhHUnvGNL0JtcQVUmunXEB9tIPK9Y--MB-6ooikG9kw9_kYzNhrrUQQf2ij8pSmT7K4-IpDNjDoV4dWjiqH_7kafADZ1yci0Mkn39CXP0pLd_G8POIVCvvclPOFhPWs4bwBtDnCMI1oACeoz4HYc9nK23fkoEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محله الکریت - صور - جنوب لبنان</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5445" target="_blank">📅 15:26 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5444">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tbr8j0OciqdZFmEtF3D8qYHjFS16ZwZIuXj7Gj8X5uXsNJ1YK-ZIBbo--ZgYPxmYd4Cy9UGi_TlP-X-tH_6UIRnpjhsxASEtwrGEYEuk5A1ixj2GER8qW327AJg2mqK84ybZt5f-XIo3BkS4i5ZzYlKvNWVR0s1Oe6Vd7fMvO5k-eyM4tf6ROX5mFvyjt5meqK-TK-RHU5csjqRq7T-hTgnnkH5IwrDoN8NuUUJdffUGdstyV-to1sjVopXhRfb3GknUQw2Mrl1Yq9GFEJHapMCyrByAuLIb6NxCWVdCufnZiLhIzz76t0DwcONT-eB-YTdnvr6NmV4hx69xaCDxOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oILW7GdqwzRYtrTRkeae77CtRTIanrPP0nWCwRZYYxC2UpGk_7KdxLn9HTThpDQ1Ioe37VpZt4msFqesnl-xq9MdBJRAQ_0t5aqjDSst6LtDnlyagbPzg_j-vKJMpFlzOl3yIXydeUD897zREvso5XnDm7GUx60qDFJGA9EaRLTjbEfboh96nGYk0_LWpPjYVjczRKaSDMKtXZpkqM-NOdkmwUfDFDpkNvqI4IqEP_lA9V8ILXs569uQWKTOUgZOVNGOQc1BsE89dxqFTTHKuT48pwj5ZxuFAMZ-BuIeOCf18Muj-yqRy-6OSCLe5qC5EeTuZ3q514BqF0oiucdnvg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ea21582d5d.mp4?token=L7eyzap3kfHUH2Jy-CC62uRHNgYEmlLJYoJSlOO7TXjUDhZYusM25Hod1tmvOmKaLzH95AFpMJvhHzADh1J1PdBrxojdUihKMFE67xGl2KyJxiNrUSglhRYjDL6BxpI7oY7vif8wf3CM0aOrTy5W9G2TkWlQs1DxJPI1pdUibAYKbYoFer7Co5JkwohY3N6HZfgbcGAr-X47bzySA4UA-1T4vcT5D6XKsVVBVy-mfX96BBjBuxEht3NmIC_IsCJPrDaXo6h_6tOl7EXMndy9USrHTkqewxSxDVlM2FusClcz2n5MYLlDxl2lKWIJ4BOuVMS6rJANA2Nq7p3-Qgwaqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea21582d5d.mp4?token=L7eyzap3kfHUH2Jy-CC62uRHNgYEmlLJYoJSlOO7TXjUDhZYusM25Hod1tmvOmKaLzH95AFpMJvhHzADh1J1PdBrxojdUihKMFE67xGl2KyJxiNrUSglhRYjDL6BxpI7oY7vif8wf3CM0aOrTy5W9G2TkWlQs1DxJPI1pdUibAYKbYoFer7Co5JkwohY3N6HZfgbcGAr-X47bzySA4UA-1T4vcT5D6XKsVVBVy-mfX96BBjBuxEht3NmIC_IsCJPrDaXo6h_6tOl7EXMndy9USrHTkqewxSxDVlM2FusClcz2n5MYLlDxl2lKWIJ4BOuVMS6rJANA2Nq7p3-Qgwaqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏جنوب لبنان - امروز
‏حملات جدید اسرائیل به شهرهای نبطیه، حداده، الرمادیه و دیر قانون راس العین.
‏بخش زیادی از این‌ کوبیدن‌ها در جنوب لبنان، در واقع پیام به باقر در تهرانه!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5442" target="_blank">📅 12:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5439">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MC1fUFYnszS0T0xblfWjFqDsOhds298ajNrwqZ9Z2i5wXXZJD6p_NdPXi5hzhmk7TvXg29QNiA8d62vW6nImHK9Hsrsh22BawvWx6Y-tBZZSxxwpnl5jz0J2pqOpIgUHFW0kZodJ00GrK5zgMvupLAU45n9bNL25RpKEB7NSQlvYoWth5cv7vNQYkcLqqOHkbFLr6nsrT12GAlDD6W5YEb7Q1PEL9h0yjsu7RETX2G6aIvLbWna5GzwVhAplEvlbvO6qoQ0lOyO69VhtMRMiUYrBO2HqSBd6ASlVmVOW7UTb-JUJ_hkwuNq5x3nHmVgrE11W2SJg9xYO3f_fSChj_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T3yjiWT3CRxaZ1dyocnjA1MzPSnN_DRt_kjagijGdHhs7XXNwEt7XAOIyDIa9EkJzYXJ_GRELfGTwHulLzI6yJ8DC49eAxbulTuUOE_gYOeYrfYXxA-86IcPYtRuoEVmvezugNyX81STopcjE6n0WXuvgdHeh-buTrKiI_oQg9sSMj7X9xuHhGfwR_YDhJ05KwmuhQvLSsZvLLonBMngGmf5yq1NIFwN3ESMzRwK8pqywa2iQTDgPCdeoX8_54h7gUJiCYA9bSySKmxASDGSaFVTya7BDkWpot6hjS-UkTdJnjmV2DaOFKyS7EW_8XHrVM0wao_rNZRMdg2U2naDbw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874c401e95.mp4?token=SCzGNfaiom96RdUlxI05Uj8vgCKaxnTVkrKcDWTMynW9BVjxNMdHIUzHdJ3EHzL1aaaXxsqRgsPOemmPzxRiioe6YhQOrg8xwCeTgclHX5xhwc9Lw70jpAoBbhAtav0Ktz5VFi40oYSkDIUW-dg5t5sADPPSHp8lW_WeJoGuydl9Llr2RK47Q68tc2gVgtVt8c5aBaPAsee86OF4QSh2VNVy21dfC91NmO9TZmfF_P-e9UKdC3_QT3wG3si6y9TwjuEZxblPMAWFyiplE9EbD16wXF1iLk1JXdpIqUrdH1oVd6TK618WsBdIFGDH4TqrsecfSKNYIda7NUBP6A5w0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874c401e95.mp4?token=SCzGNfaiom96RdUlxI05Uj8vgCKaxnTVkrKcDWTMynW9BVjxNMdHIUzHdJ3EHzL1aaaXxsqRgsPOemmPzxRiioe6YhQOrg8xwCeTgclHX5xhwc9Lw70jpAoBbhAtav0Ktz5VFi40oYSkDIUW-dg5t5sADPPSHp8lW_WeJoGuydl9Llr2RK47Q68tc2gVgtVt8c5aBaPAsee86OF4QSh2VNVy21dfC91NmO9TZmfF_P-e9UKdC3_QT3wG3si6y9TwjuEZxblPMAWFyiplE9EbD16wXF1iLk1JXdpIqUrdH1oVd6TK618WsBdIFGDH4TqrsecfSKNYIda7NUBP6A5w0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5439" target="_blank">📅 12:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5436">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ezS_VVsqZx_h3R2qsE5AlmCliqvw8Qn2oG_e9wpi8Wj970CzkSWOCt4wepoORxy-BQB6IXPBF_QANhF9OJGby031x-HaRGwHWWvxG0px_IIZvOCB9gA1Bqxv-WKUzEK_EmDreJd915qTKKXlORZaZ8Qem2ApHRbI-K7YMlPYd6KFDf1HIsrxwZTcILAVZvVNsj6cZnDVf3RKcbqLmDY77VoHw4GvrxKat_IuP-8ig6cXVE0lO141M5hthxPFm-dpyy8wAYxxMTZIgmyFddhebZf-ha8-8NNlhWs1ignrOVDMd6ms85UdD0dzzeqwoX62tcC0nZcMJvjiBpiHrDrAww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JziwgHPHlS6uRZJ-6QcKo4NWw0bBK2tXjERY0_d9DH_TjAqDoFsdNjPFhk2AVTKVpvJEEIEWy9F12oioTG3KHXalIf8OQZZGJAxLRKbCMD4SSbbxrsA-fud02-Vd0K93GimiQCMbyo9BvlE3Sb5NLB3GgugHfYhKBtGzDBTwGRLdXMAYUm11YT5FgqRpBbt7PGWzLv38I-vweeCKwkSO95KEAcj5DkElY7AB11d7wf1QmEEJk6eC7m3UxxivZtdBphsprmXhmvkhfAmZdA1K-N0qy7AIdB_eFn5k6wysVPs-zZjq9rT9HtjbysBYzAe3lySlQQAGM5rAVf314fV6fg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd790ae501.mp4?token=RU8NkBTm4Fq3rvf5MrSkKDVnTJ5ia2PEZuyKFZeTdxX3cpuIEWQCBfxqZJk7GA6OAhPvbbuVSTF34tGcigGhPEHEPSNuSkDsu7F_-I3PMGWXUKcG5zGdxPNSBMiASFJbd9R_LONWGC4mFhn3cUZQHroKGJi5iUQshWKFkjL5Z40EYpBhjz7mtoIG5x5LDtsKKh36Xpc2aJvTwYGYUhSQNy8n3CX4bIH_WN6Cu2GnemIhzGWhXXCYMTiejw3H8PwxfuuA8Bq26DGFgqghyoNG6a9AsI5kI5xpQOtj0TYYS-b6XveS0HGcJVlARUx8tY3Paa-u0_TDl7A2RVTOngbDeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd790ae501.mp4?token=RU8NkBTm4Fq3rvf5MrSkKDVnTJ5ia2PEZuyKFZeTdxX3cpuIEWQCBfxqZJk7GA6OAhPvbbuVSTF34tGcigGhPEHEPSNuSkDsu7F_-I3PMGWXUKcG5zGdxPNSBMiASFJbd9R_LONWGC4mFhn3cUZQHroKGJi5iUQshWKFkjL5Z40EYpBhjz7mtoIG5x5LDtsKKh36Xpc2aJvTwYGYUhSQNy8n3CX4bIH_WN6Cu2GnemIhzGWhXXCYMTiejw3H8PwxfuuA8Bq26DGFgqghyoNG6a9AsI5kI5xpQOtj0TYYS-b6XveS0HGcJVlARUx8tY3Paa-u0_TDl7A2RVTOngbDeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«جنوب لبنان  و پیام اسرائیل به جمهوری اسلامی‌»
اسرائیل امروز روستای شیعه‌نشین و معروف «مارون الراس» رو کاملا نابود کرد.
این منطقه که بر روی مرز اسرائیل است
از نمادهای قدرت و حضور جمهوری اسلامی بود و احمدی‌نژاد هم به آنجا
رفته بود و پارکی را افتتاح کرده بود.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5436" target="_blank">📅 12:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5435">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxYqSvd23ZIpy61wwE7nB8ABLXq6hCQ3o0cKc4paelkIIwDwJ93UL5An_-LWPK4qegbin2t0aDZ58xyLGgSzNjMns0mMkc_HGJwMCYVnIic0QIjHsr7R0zW8keI1conmYWVVaS8htxG0UnVGi4P-UbSUVeWunInfqObcRn2pbz1hiaVjXdVXiVEW3SLNcHI_A2VE7f9IqNQx-Ll3KBx6YlTW37K3J-mfOK57hkDgs0XU1otOyvfP2QjUXLw1xQqXs1cIBjYvMiml1qQaRbx0myCPIGTXwGYLPwcw209PsN0EN2D2jH55t26oKV7T_Lv4MzybN4sL6vV3wuFqdCZKuA.jpg" alt="photo" loading="lazy"/></div>
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
