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
<img src="https://cdn4.telesco.pe/file/qNKmOWaOTHMpRDljFzFWi-hyllUcRe13pJSn0i9BJ5_DvHowBMQwcSOnzq9jRKO0oLfpi5HsDPDf3xbVo54lijep5btRql0_7OPBnfgbH04_v3tch8B1Q2AokweTxmDIBpKu38wiYK4-sbquIVun9rnzqU9LvR5mWrQbnRY5X-7obhfDCFUcBc2lxxzYwFnsc7YrV-mP-WOFwYKmClypZY58glGY62jSEw0IGHm-P3R7HaxrBogKotbicYNwnBBvuhYnCH3JPniZnFRwjXtEevNNzWpI7miwq-BE97ZfBORFAfG_B2OKlP8HiXcPDJELwB2d89saCdeZmZ_Bxs6ctw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 633K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-16 12:59:19</div>
<hr>

<div class="tg-post" id="msg-27253">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aM3inFKhoc31SRMJITgY4na4rCvrI4T_2pSC3itfo5x5y1UHdHGJPGfEnn-qLxgSIvRxdJeyhm5CDSxForqj7TSuTa1ZQA0k4NNYjsUKDq8qN5INXOzWwEjamRwE_iGgKWsaKRaPmCu15vyl4Z5_IfryJvCWRqtdc0JgSx7TAfpcuJwu4zouUL3_YpNk-N2L-o6hm4gQaRLLOFfkHspaQ8R6GchqcbSj4EMO3nFLMgH65esAtDkE_o9hYOSbeBVNiy18seXmtdQlwB4itiDnQraYVac0USKvVCSqdUqqyrvV54lnn8V--8XepCFmFfCFH1uoa04JrJfloCX72QMAwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
👤
طبق شنیده‌های پرشیانا؛ بعد از استوری شب‌گذشته محمدجوادحسین‌نژاد؛ سعید سحر خیزان مهاجم‌جوان‌استقلال به‌اوگفته این همه صبر کردی یه نیم فصل دیگه هم صبرکن اگه پنجره باشگاه باز نشد. استوری دیشب حسین نژاد نشون داد که پرسپولیس آفرفرستاده اما اولویت اصلی این بازیکن…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/27253" target="_blank">📅 12:44 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27252">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKVuNdz1TzsNSKp4e4KkTLe_djWi_nybiVo8McLlD5pmvXbT9ch_Ln6KOvRy_GajfZUS_vM_mDWPKtUQSaNMraCsLgFlJGSEU8peC4pgst-DDFLTp8iB-P-N5npvyWGBtNFjVW7vGPtt5lLdNyUPkUr2zXvpmjnO8VHtJcqjX9BgP9NG_28rPAl0GQZi-qZRjtIwL59IpPHf3F2F5tbSDWP3VbKhwTFcIX_X2QR-MVEXi5G32nXklCLWUT0-hToJY0wXs25P4vbd6IhIOKdo0Qmefc876BpfP0Fcb0vvUYWMM4DiMvQdenTnNpOUulLXLLPlnRARoZk8GknANnPHxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
🇪🇬
#تکمیلی؛مدت‌قرارداد محمد صلاح با ترابزون دوساله هست و هفته‌ای 325 هزار یورو دستمزدشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/persiana_Soccer/27252" target="_blank">📅 12:27 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27251">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KM9AUgYpyJ1ppPNMRY78WsLJws2WfHARP0KUOGdw2hmRup52yfmquF7MjAe_86v0X4fcBOnIvS1pMwrZcbMglvMEDRDFtuIlTUDFkCFs0qDXSYifE7Pb8AqwCbtdbSxN2LJ0ubFwxrUYZNTUsq6whQ_hH24M1np5v6uhsfqXT7mdg6BCEco33EG6rU2z_0aZLz0KEbt6I20XF6OfDHsbo6_-ZxX3DlrF073jEz4T99Mzc-9XYG7fPObsOzFJ4rmZfTki_vHQ6iz_mfejaskTvDVC_GAM-FPCpHL4qwyOtQeF22znvQVmaA5Lo7KP-sharQZRaVKai5ptFGAXi0xFBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ به‌ احتمال‌زیاد و اگه اوضاع کشور ملتهب نشه خواکین گیل اسپانیایی به عنوان دستیار سهراب بختیاری‌زاده دراستقلال انتخاب خواهد شد.
❌
مربی‌اسپانیایی آشنایی کامل به فضای فوتبال ما دارد و در کارنامه او همکاری با تیم‌هایی مثل الوصل، بنی یاس، بتیس، پرسپولیس،…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/persiana_Soccer/27251" target="_blank">📅 12:10 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27250">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">📹
دانشجویان فارغ التحصیل دانشگاه الزهرا تهران هم روز گذشته این ویدیو ساختند و منتشر کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/persiana_Soccer/27250" target="_blank">📅 11:46 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27249">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IlQU_ifmQKnNXo0nUs1rS_tUWWj6kk-H8AITl_QKbkuWJhCpmGBRkA6LxDkMpObuM5-WTaqOOOKwHrU_p3nLfRRATTqIIf-UfGlKJGoRBiLTqxZovvUQwFI6rvxtQKln35rYW6AyzsZqlUr89oyuQdcsA4wJJxBSqJXdd-eFqwEti8woFGDjXA3aaeQ8NZnC4k2m2zuhPeI52CNhRpwZYmpAqOuPWkU7oc9R9ra5EvoZIWlBxq9ZTFD3YnAkIkrH6nAuGmBjORaLtmLy0jtMVW7qzUp_shGg8CYZphqhPvOuh2me1nUK287o9-1xLi0YV7qcJeipHxTiRK0wn5nD-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ رضا شکاری بعد از دوجلسه تمرین با تیم پرسپولیس در لیست مازاد مهدی تارتار قرار گرفت و به مدیریت باشگاه اعلام کرده قرارداد این بازیکن رو فسخ کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/27249" target="_blank">📅 11:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27248">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pz0IApkcf4iaX5U7LQLTrngfTCsabpj-l8Zxgq9AA3t-tnsiANfE3deQUsW_Eyagp0Wn3grRoPEkR8jTBnG4yV3xHWHgmZ_ZaDatXNVzKoy3_Bmj_3IObnRWLOtIrta0mkRIYEwNUwtGscZwC0qbpE63nzCGHxzDoxBOvlFsxR_BbJV6zy-BeC1i5-diiuXTC7OMSmmVY3_HYLDpVA51CvwxM1MYhaexpNqhB22vVTxc4sSkO2aKzvTb6yR8-mGERgWcj737pdjhRSaJ6Z2h1igh7ZRNih8mdOPnbZyGOR-vcwV2wQy9y0M9EKildJXQ-XPYh7qlLhIajFO17b76hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ بزودی فابریزیو رومانو خبر پیوستن قطعی رودری به‌بارسلونا رومنتشر خواهد کرد. تمام توافقات شخصی صورت گرفته و توافقات بین دو باشگاه نیز در مراحل پایانی خود قرار داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/persiana_Soccer/27248" target="_blank">📅 11:20 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27247">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6GGuyfsV91dcO7Mh1ZM_TEiua_za599cLG5RgG1EUebDH-XNJr5KtQXyPmeoWrucXzmAO0bGLF7oTLCbr_ERm2HIt_t-NdRvp5jZHmZC-9QZ1zUcJxQfRMZ7dHkc-3dyNOrVEHraj6fQcz5q7gSIU2ZHQT8QoE_475nvF29LJPM3ryoYopt7ey9oKtHCEsS8rYJf7CRYxv9cb6_2SOpD-jcdW7y50NXywlf9HxtVO1-bavrsyLkgvvYUO8u1Ce_CyyxXINQ80w60UE6Vg72ySOXE0wyu0qmPYakG4igiXrBXW_9BVEcFHuK3vY1B7519gj063HCg6WIxgTNUbDS8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
روبرتو مانچینی سرمربی تیم ملی ایتالیا:
🔵
ماجرای‌من و تیم‌ملی‌فوتبال ایتالیا مثل داستان یه‌رابطه عاشقانه است که به خاطر اشتباهات تموم میشه. متاسفم به خاطر اتفاقاتی که در این سه سال رخ داد و تمام تلاشم رو خواهم کرد واسه بازگشت تیم ملی ایتالیا به جایگاهی که شایسته…</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/persiana_Soccer/27247" target="_blank">📅 11:12 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27246">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CswQjuCNJGW6jGllHrLadVgoJZpxbJ-676qdpb2PaDBCcpLLliRmWBBAgCe4ODHwTXKRwU4t47x1N9E3Pg0XgaoIZSFlFcpE7gEPmYlwOL9LEsyVjcqUQT2Pu7QWaNbRBP4TiF46iM8UnBKqVkJzyubRTYyRCIcVmGLhsGGUVCFQxQjncpiQ_oam0KZxN6hMZcPJLVu6K0eYTQCYHUqzVfz3fqIJsQrQn7YOagq7zNPinuvxFFD9dweuoQRRFdKYT1VrK3DJPD6JhbZTXyC8B0EGn1qRCvRMhTSSHLiVYF8pRi3eSyoFmAH_maFHQOzTrHDZikWnWcx7nQjP1HjTEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نشریه کوپه: انتقال رودی به بارسلونا نهایی شده. او دستمزد بسیار بالایی در بارسا دریافت خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/27246" target="_blank">📅 01:45 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27245">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T3UvQO9sJ6X23UQ_Y53XgT07caO_7sjrBOURe7ypu5_RYOu-rClZ0vx_FsUOOhk_GEbRZreHIuiQbh5Iq3oHiYNnHhuOJ17XeypKKg5KX1eBXHXy41b4vL4ml4szz4b8g4gWyUxgqKBiE6G0d-Jz98L316YZ57Z7yDKyUSAzoXHXVy4dcX2Nm0aucoLKl_GKuUjvSzdDj48zMUOgoyM9Qrj1ac4wmpEzGzhyu8u717HFTsWQH2o5vcVnrpFgSW2STG29sk_AzN3nP_-YwGFesoZO-BCGFlQ-DDs9d6cRlNPDh8rhqDSFn2d3eNCB-2QaKzyWYCES22iWXu2wNBJxXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
🇨🇮
نشریه‌مارکا:باجذب‌یان‌دیومانده و تمدید قرار داد وینیسیوس جونیور رئال مادرید به احتمال فراوان دیگر خریدی در این پنجره نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/27245" target="_blank">📅 01:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27244">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1a50e09f5.mp4?token=M_4oi3XmNGOZ--FX_aaFaUdEUBH-KUXJ4Mw2hcs8mdBGNUUoAwaGlxu0nE7g8iE6__bZF6TjXz8JEC09FDTJVbVQ88Tqm5lWm4-58mEFsnUXerlOztYNEwLMO2xNmZGaitrCFoGIQ-cHJKAC_RbTXrBbpv9VIVSY-dd-wqyYrFXGcPCWVeHNIpomZd1O4VJjUe5uwbt8vWitCk8Dyd9yW_2NCbGOkGE93dPov9EajmNEh2HncFpxIveFZ9F-xKi3z8wnzk9M5oVw3-e6nBI9FPWmtQofZbIMFZdQ6T_CWRc-6zBw9kojGLpeFF0_VUap9X5lbDUA_iGCMkCb3j2egQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1a50e09f5.mp4?token=M_4oi3XmNGOZ--FX_aaFaUdEUBH-KUXJ4Mw2hcs8mdBGNUUoAwaGlxu0nE7g8iE6__bZF6TjXz8JEC09FDTJVbVQ88Tqm5lWm4-58mEFsnUXerlOztYNEwLMO2xNmZGaitrCFoGIQ-cHJKAC_RbTXrBbpv9VIVSY-dd-wqyYrFXGcPCWVeHNIpomZd1O4VJjUe5uwbt8vWitCk8Dyd9yW_2NCbGOkGE93dPov9EajmNEh2HncFpxIveFZ9F-xKi3z8wnzk9M5oVw3-e6nBI9FPWmtQofZbIMFZdQ6T_CWRc-6zBw9kojGLpeFF0_VUap9X5lbDUA_iGCMkCb3j2egQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این‌فراری‌قرمزی‌که‌پشتCR7 می‌بینید، یه فراری معمولی نیست. حتی اگه پولش رو هم داشته باشید، لزوماً نمیتونیدبخریدش. این‌مدل بصورت اختصاصی توسط فراری برای مشتری‌های‌خاص و خوش‌حسابش تولید شده و تعداد خیلی محدودی ازش وجود داره. حالا اینا به کنار، نکته جالب ماجرا…</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/27244" target="_blank">📅 01:23 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27243">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wz2Sl3kHYmmjiwvjMGtvfgY7K6Pq3hOvt9wAHEuXvcAVL_VoxJRgjqVOu-hoB0M2NQrwshV97FVdpVOBpc1nC4ctMZ-IW9KBKs2u3bYy7zhX8RJXHuGGvd7zcb8IGm_k6YEU57dgXxgI306jvZteQ3VnGJ5eh9UNlr-7j2Z2D-ni0prgkm98AyDz1h1k-pOu0pzc2gGSjUc8ifkx_QOg_fkHhdrlsZafmInQBHFJcvaBqKyVe-HU-7gH1Drukt3P-oRT_D1BRyD-HAFxSYlRKsEP_G9p0eUABXYzzMVpt-nUkW7-bZ9apjpd6YiewyxBxCfkRv6WNdBqnx8fH7WxGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ بزودی فابریزیو رومانو خبر پیوستن قطعی رودری به‌بارسلونا رومنتشر خواهد کرد. تمام توافقات شخصی صورت گرفته و توافقات بین دو باشگاه نیز در مراحل پایانی خود قرار داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/27243" target="_blank">📅 01:23 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27240">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZmzlUstei67Iyg3qDp0FC1UNzp8EIP4YMscxseu8hBIIsLWk6dE1399DvTCP5bO5_GR8MExoRKNIa4ypv_S3yyJqYl9ffzOiqnLtFi__aEogLKqSn1LnWLnQsSqr5FQq_Z14PXqk0lI50y7tkLEoe8OE2TMErus_C_30o5Wh0qyEZiSn9XJQP5bK8bv66aayduCX6fLP5_n6EnSBgz3G1nRlTwXAkRqNnGOCUA1isncx5fMx4OF9ooTJelkj17cuEGjJpb8UJJwaAU6BJO7Zd02Eywj_6hRUC-4JYc2KqGhEyk_PVKGE24d2Ac9S1N2QRhyOprvCehEPkjjqfVVpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه تنها مسابقه مهم ‌‌‌امروز؛
دوئل دوستانه و جذاب شاگردان اونای‌ امری و کمپانی در هنگ‌ کنگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/27240" target="_blank">📅 00:57 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27239">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iT7pSF3w4rGbkIJajQ51EDliRFmB0ZgESnjsz3LJ_tHWjg_XBbqAGY8msIM_L7NMQQRSX7uOAcPL7aL8SNGcDrhKRfCvFLtKibDn0-jd76QjXW2IoLMyPieGYsKF7NDRYpTORQ33blBz-EtsfIp9MIJafuAxzrIQfXg6Yn78qioai9TipaCRAWzp4UHnAYP-MpM8JUGOBI6q8cWUXKTGx7Zo71PRosvlNShxnCSBVM3sO9AwTX1Cg6NcsTo3NvPZOvGBq7UOsu8ztL1eQCjSyR3X1iyf8WLbTTHaSwY5YthOhJJJyC7fMZ09KdOAxaT_dDek1PkiRz5geRgZi4qzUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدارهای‌ دیروز؛
برد اینترمیامی با نمایش درخشان لیونل مسی و ثبت دو گل و یک پاس‌گل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/27239" target="_blank">📅 00:56 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27238">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pc_gAgRNBvcvsmQLh9aEZJWV2vi9dNLG9df9OGqXDYBd5wS70jUTs98tzH__b4yYZlGOOLaJPnIf7OZGUInoYJAWL8R9-ByjGt7C4NkmCMJpL5NSBNxysEXq3GRrrEz2IAgrvu5MRCDjVzEy-292IHB1uIkwKpSHUnQfwrkPe0qFevNERAALJP-oNstn1uigcw32DFznp9xIMpLjeU428EpzWC1Fu-dcZ9kfowpOOmIaKCjHiNMnfDJaj46WIBrNatdDWO22MwWwN29FYN6Jh-NQejN3pe6_2XZuQFwDEUYeofCV11QoQdvnsvxuEgpIVQjAjRFEDgbEIQERawe85g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
بریز بپاش‌های چلسی طبق معمول ادامه داره؛ بعداز جذب مورگان راجرز بارقم 137 میلیون یورو؛ حالا سران چلسی باپرداخت 60 میلیون‌یورو با عقد قراردادی‌تاسال2032 ماکسنس لاکروا مدافع میانی 26ساله باشگاه کریستال پالاس رو خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/27238" target="_blank">📅 00:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27237">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-IY3vgS9Z9jq3zIk_SJAHJOtD6i5a4aMOUiLkfuBCTi6hccA-x0sN6spTU-3VqbpscGU3JOWG6tW6AHJAd-el8b4IW4-QQv5J9q8FzyVyNz4KDx0cCVihPiF6ub7fui9-RT8AwGqDFVwANY_jy6pGYswlxUy60_ifb7SoVKEJpxrJ04OFVRXf2p1m_sD_tIv8PJ7Yi8Z3iOQWxeFSpHPtcHu5C1slofGLC8Ou6DKadf_TGimVwnY12fHFtLHg3iigjowoOU4MSjg9X_pSUA7JP_PrvaLnIp85v4a4bNsml3Ke09eiNdrSr3jErg1P4kWy0IoBsoJBXYtJYUXR7hgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
وینیسیوس جونیور بعداز تمدید قراردادش: هشت‌سال‌حضور درسانتیاگوبرنابئو برای من کم بود و دوست داشتم شش سال دیگر در برنابئو بمونم. شاید اگر شرایط همینجوری فراهم‌باشد تاابد اینجا بمونم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/27237" target="_blank">📅 00:22 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27236">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XUU1P2ZvzToCtqyGBoe1CY_-Yezo7XVK0_i_zay2AlZkMNTJ_6RBBxwLFRzmgK1BKttouRU68JVPuIst3abrdwWNJYVwUtnq7AsRAS0y6xoMVCsh7RQDmGVGesDVaHUP1wV7sPSDGeT9bKP0pWK3BczsNWg3Cq2WTFrj1CBAFL9AA9szSM2HA8P6-GZFEPRVVZj2i9p5lFXf3hsHknB3SyrgEnTGgpHyinzoo7xFApIuG_k3O903DcOMDqgL__E2MGwDpszwv6YcX95L0YtifE9ttzVSXwCYGAdaAS3ogemcTEDF5oFJhDzjpFMoNecwAO7gJTY5kXevhLsC2Y819A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
متئو مورتو: رودری ستاره لاروخا از صبر کردن برای اینکه‌رئال‌مادریدبامنچسترسیتی به توافق برسد خسته شده بود. بارسا به او تضمین داده که مذاکرات مستقیم با سیتی را آغاز خواهد کرد. هانسی فلیک با رودری تماس گرفته و این بازیکن به او قول داده که قید حضور در رئال رو…</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/27236" target="_blank">📅 00:06 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27235">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EbaK1vfh-SXzQirTme4euouJYoDhY2sjk46N2JYkBUmZZB3xeZBwgFD017gF-Ho3r8d3Z6J-jX1dP625TVxLro_idoZMDjLKppvVQETVQ8pepcmNb8Taa2uCUsv74hlPQrdCf_1Wn2vmfWngSwMnewcPfYZN7JQUwnnzm6RHZuC_zISuGebf4V7h0J895qdFe1QfHxhcR938-jqj7T2gwJH2gzY7kWtffk0wnQe5Uh7mzgjsctR_T6oA81YWJr9oqg2KC45bBv5NiUI-OUUKg_Q5GTPphSBJzntpXUvTEVOizi9n5xS8CaQzfZDF9NQ5_3ZCYhzL6yS4kIyKhm03_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
وینیسیوس جونیور بعداز تمدید قراردادش: هشت‌سال‌حضور درسانتیاگوبرنابئو برای من کم بود و دوست داشتم شش سال دیگر در برنابئو بمونم. شاید اگر شرایط همینجوری فراهم‌باشد تاابد اینجا بمونم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/27235" target="_blank">📅 23:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27234">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqFAt6S20rG_LnA6u5toUVXZ416gRU6mnNw9QEEdTeKoGwJoh-xDZ6Po3N1hoKtp0qPVnojVto49MsKsdU6XvZLc5qbF4VXV0_8l-CXd_YHzey13ytQj8tcoGL_-B-ARz9yhRy4uhrC9zkwA9Dam3vFL0vuh8yw0v9mPkf4DXHlydwlWZGxGKfArWtAV52FG8GS-ZQqq25wa2qPIsd63PI3wT_-L6kSWPWI_pSKwdngT05TzZajPiIFDqaxXKj1uUFhSA-me1s4fgyWWkoYVVlt1JFP-bZ75V1eVOEf237P3NS65flZZlaXdn1ElyfVVTaIBoM8Q04tJDN5QPV3Lvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛کادناسر:پرونده‌پیوستن رودری به رئال مادرید بسته شد و این انتقال انجام نخواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/27234" target="_blank">📅 23:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27233">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e40f288f69.mp4?token=mOxQHbcLoMTzGc_8lnyTGc7LeG0V7fnnG4YkUzARZ5IC0-mx3d8DV3o7dymr1CzqzOEJq4h03TYCR2g7okESXIP1ia_JSsnoXLZUCgS4RSo4UXs0pIlotwvAO36gQxqBcxrao0tO2pkGSVSJuu68hPMBwkr2Rhk0YfWIqsKfdtnf11fHDtM_2bVRcLTM1Im7pRJI-c0WGWZH_mdaM5Sm9kGpOB059HEEo78Z8i9gmEq3Z5IZxtBgQ1_qN8P1qu0dzXLT9fyA8quiAOpHPYagwbPY50orWZUEFZwEZ6kIdoa1fFv5TXsE3YafZJQe8agp7I0v8ACOyt2ywjoG8z8Mqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e40f288f69.mp4?token=mOxQHbcLoMTzGc_8lnyTGc7LeG0V7fnnG4YkUzARZ5IC0-mx3d8DV3o7dymr1CzqzOEJq4h03TYCR2g7okESXIP1ia_JSsnoXLZUCgS4RSo4UXs0pIlotwvAO36gQxqBcxrao0tO2pkGSVSJuu68hPMBwkr2Rhk0YfWIqsKfdtnf11fHDtM_2bVRcLTM1Im7pRJI-c0WGWZH_mdaM5Sm9kGpOB059HEEo78Z8i9gmEq3Z5IZxtBgQ1_qN8P1qu0dzXLT9fyA8quiAOpHPYagwbPY50orWZUEFZwEZ6kIdoa1fFv5TXsE3YafZJQe8agp7I0v8ACOyt2ywjoG8z8Mqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
میلادمحمدی‌که‌ازابتدا در ترکیب ویتبسک حضور داشت با دریافت دو کارت زرد در دقایق 21 و 33 از زمین مسابقه اخراج شد تاویتسبک که 1-0 نیز عقب بود، ده نفره کار سختی برای ادامه بازی داشته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/27233" target="_blank">📅 23:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27232">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/700f42e1af.mp4?token=E0TROxMe53BdLacLnasei9RdAQQQoXMVjCFFswsIDBsRlM2UUamX8Uas_OodVcroK9i24O9UOjCnkXDI6Up1IV8pCOXh_fQHGaXJnIPADyjpKfZsgTw0p9YPRYieNZXfArYShBIGlhPrhE7EZeuIWGruJUgP-xSlsxnLNFJ3Zz-Js_hxtkReRNWBoM2inAHh9BrUH9Dq8OzUb6NCqM4_YOUF64qUqo-4srIKiwmPa7guN0lOJzIbQf_JXnjV6xJGgZkryDjWedia7RAUDgqj6ILlaIcmJGCZaceWqC3wuTL3LW-ipScZa7Bl_qKO3ByBkpJypRgsox4XML5rT2-4Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/700f42e1af.mp4?token=E0TROxMe53BdLacLnasei9RdAQQQoXMVjCFFswsIDBsRlM2UUamX8Uas_OodVcroK9i24O9UOjCnkXDI6Up1IV8pCOXh_fQHGaXJnIPADyjpKfZsgTw0p9YPRYieNZXfArYShBIGlhPrhE7EZeuIWGruJUgP-xSlsxnLNFJ3Zz-Js_hxtkReRNWBoM2inAHh9BrUH9Dq8OzUb6NCqM4_YOUF64qUqo-4srIKiwmPa7guN0lOJzIbQf_JXnjV6xJGgZkryDjWedia7RAUDgqj6ILlaIcmJGCZaceWqC3wuTL3LW-ipScZa7Bl_qKO3ByBkpJypRgsox4XML5rT2-4Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زلاتان ابراهیموویچ اسطوره‌میلان در مصاحبه‌ای جدید از دوران مدرسه گفت؛ زمانی که یکی از معلم‌ هایش آینده‌ ای برای او متصور نبود و تصور می‌کرد این شاگرد پرجنب‌وجوش به‌جایی نمیرسد. اما زلاتان مسیر خودش را ساخت، در بزرگ‌ترین تیم‌های ایتالیا درخشید و ثابت کرد بهترین جواب به ناامیدکننده‌ها، تبدیل‌کردن همان رؤیای دور به واقعیت است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/27232" target="_blank">📅 23:13 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27231">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B1Sgocr8K3lV4p8xf-WLPPEZhGZzzADGagy2j3jUQNjZzLw-pDdMqeKZYbwQSuULcCN-lgeZ6mkoUzXCAVjCJh9hCGWqr5bBbPXn0LUh6_gtKOFTABiHeF0txUXBbBp6PNC__WPv9tiCF9ySogDO9LGcZ6VMYF7kRPqhG_Ko-qumeG0PsHMCBYQnnqdg7NwEvbT1Ai_pbeUdVHse6rregRvrjO6hJTDq13wI0YeZCpRiJGxLh3gBLZU2CY95YPsvYr-cvSRFzKbb90Zg1ujy3kJOuAMcktnFsNo8PKU2GcHaM1des8O6sWEYXkS4U0IKcxNfSFgppTBJgrw3P_BJpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سلطان‌میلادمحمدی‌متخصص‌اوت‌های نامنظم تو یکی‌ازمهم‌ترین بازیهای تیمش تو پلی آف اروپایی تو ۱۲ دقیقه دو کارت زرد گرفت و تیمشو بگا داد:)
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/27231" target="_blank">📅 22:59 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27230">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/902ccfdccd.mp4?token=Bwid9Yg3lZ_bC1n3yjhQftqkaHLDTM0ihJP3bhw9lc65PZf2lbirUSxvMvFth02-OQIzL24JYCTyqhP1C4xde4FPvy4sYurypy8qeWS5wgFWdIGngjXfYcZ0fMr08ys_yisAraA7rFapOCj1RNJymwkHmTryyPPRfQ0XgAi5vKUiphvet192yFeyNuZp54VGtNUJcJP7jNmJ1Jjq0wFavZuBWN9ZrsMzCkGsmHnKQHNcrSPFH5rMAtYAy_oL-7fPx6P_HNZQI_zFg-vtLXtAgXazP10Suby8QwEin0xAtxJp5qY76fcvlxlssPUOil0Jp-Fi17c2lV_Ls9oTI66obg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/902ccfdccd.mp4?token=Bwid9Yg3lZ_bC1n3yjhQftqkaHLDTM0ihJP3bhw9lc65PZf2lbirUSxvMvFth02-OQIzL24JYCTyqhP1C4xde4FPvy4sYurypy8qeWS5wgFWdIGngjXfYcZ0fMr08ys_yisAraA7rFapOCj1RNJymwkHmTryyPPRfQ0XgAi5vKUiphvet192yFeyNuZp54VGtNUJcJP7jNmJ1Jjq0wFavZuBWN9ZrsMzCkGsmHnKQHNcrSPFH5rMAtYAy_oL-7fPx6P_HNZQI_zFg-vtLXtAgXazP10Suby8QwEin0xAtxJp5qY76fcvlxlssPUOil0Jp-Fi17c2lV_Ls9oTI66obg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
🇪🇬
دوویدیو برگ‌ریزون‌از استقبال هواداران تزابزون اسپور از محمد صلاح به محض رسیدن به ترکیه و رونمایی باپیراهن شماره 10 ترابزون
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/27230" target="_blank">📅 22:43 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27229">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f03bqIpc5XJx7tJilsLkXYPJWSHdawwSonbEvrK_y010zU-1OBJw_-Jw3Gj1bMUX4RnZdOvWLRNiidHs4iUVXulTu0SufTclhEfE7kdYx5d_aMa9W9S_7KRp1MZB9PYSYkMQZA2u-UM_6NLALtailIzTh7QB20wFjeH-gNczUz75V4UTmEN7qbr7a9KLvtESLkVepViNdCfBiDKnVWytxzY8k9Ki0TgAypMxLTEc4jYYDTnh7NSecjIT64sdYZsByWvWkYRdUtV8LHH_CK2RAKzv0TlUvK25tnTuKwqmQFFadP5Wb-OfpwG-GKTKb45bY3CUPs4AU0NJeTIfVKsKWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
رونمایی رسمی رسانه باشگاه رئال مادرید از وینیسیوس جونیور؛ وینی به سبک یه گلر ایرانی دو هفته رئالی‌هارو بااخبار رفتنش به آرسنال اذیت کرد اما بالاخره قراردادش رو شش ساله تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/27229" target="_blank">📅 22:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27228">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86333d6363.mp4?token=kVKGiCa9bF_jPlhJ0zZPn4AefWnC1mxQ1wsSYvxizGvLcftrlw2fd-V6hPGKoA9fh4j2YhuyCKtrBoKsoOkX_dm9maOmLCLTJMeaA_Q5GXJOe5WU0BGnvBJsvoIbOqabuSn9jTMb-Bsw-UAsPfvkRdkFOpASNwAlMlus5z4UyQjkSkCuTgTpVADBhM6u6InocX27M7gxonsKK4IH6nrx4SyjYXyf2EGMSNhtspIreMAiO21F2-B8meawcSjPgdCMPEApzW_XB8mkzTN7Uy6H9J6m6R0tW0FAywtW3f2P76ZV7MB36r0eSaLGC2mBOnVNiMyT9nDEWYbgojchJm63wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86333d6363.mp4?token=kVKGiCa9bF_jPlhJ0zZPn4AefWnC1mxQ1wsSYvxizGvLcftrlw2fd-V6hPGKoA9fh4j2YhuyCKtrBoKsoOkX_dm9maOmLCLTJMeaA_Q5GXJOe5WU0BGnvBJsvoIbOqabuSn9jTMb-Bsw-UAsPfvkRdkFOpASNwAlMlus5z4UyQjkSkCuTgTpVADBhM6u6InocX27M7gxonsKK4IH6nrx4SyjYXyf2EGMSNhtspIreMAiO21F2-B8meawcSjPgdCMPEApzW_XB8mkzTN7Uy6H9J6m6R0tW0FAywtW3f2P76ZV7MB36r0eSaLGC2mBOnVNiMyT9nDEWYbgojchJm63wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇳🇴
دو گل استثنایی و مشابه هم از ارلینگ هالند غول نروژی تیم‌منچسترسیتی درلیگ قهرمانان اروپا؛ باباش گفته‌شاید درآینده‌نچندان دور این فوق ستاره نروژی رو با پیراهن باشگاه رئال مادرید ببینیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/27228" target="_blank">📅 21:54 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27227">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🟡
👤
وقتیCR7 از اسباب‌بازی‌هاش رونمایی کرد؛ كريستيانو رونالدو با انتشار پستی در اینستاگرام از ماشین های لوکسش نوشت؛ اسباب بازی های من.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/27227" target="_blank">📅 21:46 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27226">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vOiht7_aVuCan4sYy6B5ggK1sHZfhrT9FpJ21DSi5RXSycvlswDUKCBZbtjTTCxG1GH8EM46tObXSypP2Bqk_smhWlMGhgLr6OnEtnieT8n_-7ZjAFV8uDqxLoZOM8IzXdVAzo1WfIjI1iZTXJUhCHRA56wpzJuOwnNRJlGJm9Vjne70gwwT3GASXYLaGH16DjKg4FGqG_gSvABOf1MdVrSz1Cd94s-S7gh53px5tgbQj8VEkZP7w_GOBLjYhmJiW7WVAc4FYwOlced8fzr5aYS-KnJasIOXCSHqgG5_8DatSHHdGN67fe2c490YI_KV4FXOHwekYmm8SofXOhz7lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
رومانو تایید کرد؛ بالاخره بعد از کش‌و‌قوس‌ های زیاد؛ قرارداد وینیسیوس جونیور با باشگاه رئال مادرید به مدت 6 فصل و تا سال 2032 تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/27226" target="_blank">📅 21:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27225">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KIeS1rED7b-2nkCPMOUZKopiYIPQGfhTk83zehU1w6_B2eqDlHfii1TC_Sd0tF3hW-tNXtErfWGgmDYclJWjjmXS7ulgwB-H8DG17gS2AIrFqOBdr0-QixACzwN-NQlSnX8UN1jzLbCdbfbuiZ7kGo348cgMv3KONrwJdnhXVVO9bUlCdbrxKyRBNK5GelVJvCbENQB-B6EJFQGpne7NEkp7w7lsLTe6uZdEhULt8j6VEV71YO-_nKKuVObVcA4t-JCO0jJ8xUA0g-ovb9bLW6lut1FqBiwnzAGAnrxUoudO-ZaWRjiX5R3mnGCgGLXgXmgSrCXSIaLx-LeBS47bpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هونگ‌میونگ‌بو سرمربی‌کره‌جنوبی درجام جهانی ۲۰۲۶ مجبور شد دربرابرمجلس ملی کره حاضر شود! او توسط نمایندگان مجلس کره جنوبی درباره تک‌تک تصمیمات تاکتیکی‌ اش بازخواست شد. از تعویض‌‌ها و دعوت بازیکنان گرفته تا ترکیب اصلی تیم و سایر تصمیمات فنی اش، همه‌چیز زیر…</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/27225" target="_blank">📅 21:21 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27224">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tKCf-WNPw85Bk-3J3ekF7zhgN_gFrXcqk6bmwP7ujUdEAsdfvupR4AraWivbGTvijjzxW8kSKfaXCdvwVQ_l8Ld5E3P4PojOKGw5NyXNCqOmrxfyRouhY_h5JgrW0ViBBK_p6ZbutIjOA3FplW6WR0P4PcS7mHZKHhC9gF8zf3gIXbKTDN7jxpNC_XT4zuvAtX_M6gCdXu4owDbpqeZtPaT1QA6ky3DooMAxi6eNaTAs4lqwnwyu6Aq42c96d-zXj4_JaDDyJyWGKV8Zw1xeEUJd0yjzwxcMdp31Yo4mDBvMt56xxbofH5c1hYN05bI8wyMPsdYC1YdAvjn3R3zCLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
تیم استقلال امروز دردیداری دوستانه با دبل سعید سحر خیزان و گلزنی یاسر آسانی تیم استقلال خوزستان رو شکست داد. حردانی دو پاس گل داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/27224" target="_blank">📅 20:54 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27223">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oHN57XCN0qvo2LhJuburVvHApjoRTrE7xEzy1MZyVxv68g0umWBYW9K6Fht-scmu6ZpFbOtjPS_o6P1gOZGsD1TWGOnAZV00prcwu0kXGNR8QZ0JVRFCMZ6FnI7lqm0UNvOy6NDuY4cTvv89flxcZq88C-BhdyYoJ2xM4CoARmjnkrdLr6PpUgnAFr4Xy6RGKqoM27YqA42VRg8TlOqwaW25lKYi24AiZ-ggOPZeBq8EniSdP3f7ANvcBVhrDe0AEt8oStHnvepcQEp3O6dHuQXY6tT3O33ebvTYjlbNR5GaPFU3t779VQeBnsxyAxQ38BAtj1bem12x0E8OtDTVjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇧🇷
#فوری؛وینیسیوس جونیور ستاره برزیلی رئال مادرید دقایقی قبل قرارداد خود را به مدت شش فصل‌دیگر باکهکشانی‌ها تمدید کرد. باشگاه بزودی خبر تمدید قرارداد وینیسیوس رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/27223" target="_blank">📅 20:51 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27222">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/883695a5fe.mp4?token=XHG5ew91UgJuBZe19Y10DGQgxeAJua7yeRRZU8HSFVA0Sp-h1f2dKkau5teoD6qr9MkIOCQTzlVSCv8_m3_THMSZUbkJdYucGO8Q2dMeKooySE_KncXwqJZX5QSx1rdcHpyAQlrbOIzYarrfnALyXQjecYxTEbj8MbH_xcrJXBmwSBWGI-dQkXPKjN0LFOgSHnYYEB4Ehg86o0HKEQo805b0HrA2EszYEZush2QYApwuD9TvbBWMQJq19uRkQA3t6M_m5YBsx0Txv2Ji8NxUa82ipQUGjKTxEthPuJy9gXOETEkmhmDyoKvYzbLy6aQSH8c544311HXyrF8h6o5eiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/883695a5fe.mp4?token=XHG5ew91UgJuBZe19Y10DGQgxeAJua7yeRRZU8HSFVA0Sp-h1f2dKkau5teoD6qr9MkIOCQTzlVSCv8_m3_THMSZUbkJdYucGO8Q2dMeKooySE_KncXwqJZX5QSx1rdcHpyAQlrbOIzYarrfnALyXQjecYxTEbj8MbH_xcrJXBmwSBWGI-dQkXPKjN0LFOgSHnYYEB4Ehg86o0HKEQo805b0HrA2EszYEZush2QYApwuD9TvbBWMQJq19uRkQA3t6M_m5YBsx0Txv2Ji8NxUa82ipQUGjKTxEthPuJy9gXOETEkmhmDyoKvYzbLy6aQSH8c544311HXyrF8h6o5eiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحنه‌ای‌جالب در بازی دوستانه اخیر دو تیم رن فرانسه
🆚
گالاتاسرای که‌موقعیت استثتایی داگلاس سارا ستاره گالاتاسرای به طرز عجیبی به گل تبدیل نشد. این‌صحنه سوژه تموم رسانه‌های خارجی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/27222" target="_blank">📅 20:36 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27221">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOTfK6C4PK87lKcOmd6XiibaIaYJld47OVVWBITZZ-VEQfi7mXeXiKf7lJu_a7x5LSjM69auWVAToo0N4ClLRuMoJE8szhaqNfl2TL_-ZOUbi1aHDl-_5nSda9dIysH2atF66Om_6JF1a9UCxzriteQjL81uCs6wykoaY1_ntIlpHJAYi-0xtON_bnDCFEF-EJhRFLU8KJkflSiZs5po531iRWE0v58B7KBzeUMvCG6quka9A8nJwFmuOS5EbgZp_IdYtB2qyu0a0npCLcKNFZckMo0nmXiRx8F-T1A0e1UeoDmaKdmHb1z7gFEzkCj1ZodwPhDF7U2Wb-dH6TO5WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این‌فراری‌قرمزی‌که‌پشتCR7 می‌بینید، یه فراری معمولی نیست. حتی اگه پولش رو هم داشته باشید، لزوماً نمیتونیدبخریدش. این‌مدل بصورت اختصاصی توسط فراری برای مشتری‌های‌خاص و خوش‌حسابش تولید شده و تعداد خیلی محدودی ازش وجود داره. حالا اینا به کنار، نکته جالب ماجرا…</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/27221" target="_blank">📅 20:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27220">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JoBMZPDn03TzWZ-2mc062Wg46jxBQbFT4kPoXDNEwGB8FZ8wWlVlUONvM4bTk0xfIDJTylBUVDMALbmwgzS4t_RV90A0FELIiayuFsveJ7eN9FWd0OPm1qxfxS9PCLT-K_RwgCt88B1_7tN10SfSOfuEIKzpCAQsvu6GfTIbine5S_r2ZW5blycS00Q0p83BK29-tKC1qB3cowhOFVS296O04QhxPW2dq4vUr0gs4bR_hg-CCc7_goHQjRpPk045FFSjbWW_PlpCc-RH50zj38f5oAZBET5kY2oy1VK4P7zYwvAgABdeZlHfCtsIGmwBywiepnFCYgd4XqYt5IlzsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
رامون آلوارز: وینیسیوس جونیور و باشگاه رئال مادرید بر سر تمدید قرارداد به توافق رسیدند و انتظار میره تمدید قرارداد به زودی امضا بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/27220" target="_blank">📅 19:53 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27219">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RHkBAMvx8sJJscm6xjE8q1ZuNmsOaFbLhuOqzJMn6qxwJh724YaJBI3DL4vmpzVR-H1TEOF0I2dZ8jkJOp1s1PUjoY0dnt3ZyyfNg1E3RcfNTSL37blMkuQJ0Eyku1KiAM-Wgfu_ChVTaho3okrf3A2lo2eO0LslWLX6aP9FGIp5Lmlkh6Drl-7xj5RBiuJtHIxHG022y3XQTbI9t7d2nUfH51bh3zmYUqOMpmiKPM-6Lc2pSXFwaUVFqQJ6NPAOQ5j-871hFtTdYrJ8lFuTkvB3r58s_hgpis59WF4JRrc5updHXNsyARJkturmbsXREMmZOZ1BMk2cgxs8SD1NAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه استقلال به آنتونیو آدان گفته با منیر الحدادی صحبت‌کنه تا او و همسرش رو راضی کنه و بهشون بفهمونه که ایران امنه تا برگردن به استقلال.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/27219" target="_blank">📅 19:33 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27217">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJ9IxxeHyBml_iMoNz0rJ6K9enw0uIy8vsxRNHhKt_lEZVMvdCO2NS6rVmi9iXm2yPy7CLybzunBxPDYpHbg77gZkh8ctyCrK7FjqoYDeOgSb1Wcr87LUjtZwfteI6hKJ36krN7N5RTPrw8yXsTlBPpc89lYZmYOTI0GBrrFAGO2xE05isUfR64BzsIJHbS32Rf5Sq97-w6BsGMh0uFSJmT0Cyicgusvi-cT116Ygx6_oHSH-OZdhz4jUCHx-WrVeYMjE0X9-AXJ5b2ateS93I5x4eCMxDF8TSkf8jwLX_VgNh0hW0Cqow8II5fyH1ksMF4IgHZ56NzHc9c8pVei6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛کادناسر:پرونده‌پیوستن رودری به رئال مادرید بسته شد و این انتقال انجام نخواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/27217" target="_blank">📅 19:09 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27216">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgBCjiuoYzaChTrqv8GOBRhWIW8oRFS-0um6zVfvDIGwMNktrwdjDrK-Rj8nfb62RRgi-3MbEMYNER0VSjAWCysHvU7EtmxvgTpXI5dMNzhssC_ViLDmjnWUsODh05TPw4BQD4fTNu037TameicisAAdGbrc-fyZbX6xvBF17O91uvykRjJrkZIwoy1xgbROI3oAc_u1qBECmF8OlOws9GMa8j_D6Mf0sp09-H4gr7mzZ-iAlnsVwF1i3syWjeqUnL2tabxzRaSX1rCtPkQd3HkbrPS6e4aN1-c1kjzvDeYWFqJDC3m7ZNSzN4fD-CeA5Chl7lEeFSeqOYlwRrS-hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
🔥
فقط و فقط ۱۱ روز تا شروع بهترین لیگ دنیا و رقابت‌جذاب تارتتا و سهرابیولا مونده؛ برنامه دیدارهای هفته اول رقابتای لیگ برتر خلیج فارس!
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/27216" target="_blank">📅 18:48 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27215">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DbrJe72ATlNXRExbMmD10EqnSduddVLOV7nQGqHT53xL0PJclnFhcwV5nOmaG18RKFXx4BekVv9YWa4L0t4ilONsi-7e1ihkXUMpAKGl_eXSVrEwrWEtspSDxHOfcV_2nmFN-jSGvSyS-Odj-dUcEVIdA0ne-WGd3ZJpVW81MvQRp_zoYCCdnujk3IaZ-CE6YWquqXcyTbwGLLe9Me-8vkihjNMEW-xG2SAe_573J06cEBbOBwYOmY1nBxkA0yt0BtdkQRG2C819H693PjX8LGWcR012-0nsePW81LhNhqFcbEaJbsshxqW8WMo9lO-sUUefLrVYVafPfD5fYqdDHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛کادناسر:پرونده‌پیوستن رودری به رئال مادرید بسته شد و این انتقال انجام نخواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/27215" target="_blank">📅 18:32 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27214">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pf0Ov2HBIjgI7QcWOX2dXcqTCQ8njSJiJ5taEs0fksNfregdl7rUKbMLvaKZumw1-M7WWbNkUn3PvrdZn19P0vZ8hBWPWEFeXdMo4Zs10krkohh_69xXrWbl7h9eaoQ780FjPM07xGIxe8DEGlQ2WYqp14RFouV6T8xa-qg-Fxf2mfc7GpBONZCarITjvm3y1DNrS6rud-DH-zEs5PSKClfrYhoIaSI5GvJ-A6Jrf8V_Ox_FS21Wg5wQY9kEvLJcYvzHW_20LMqdP3WEIq5DCiK20h7LHfxcuzBr-KcVwOzlX1cnZigeF5Yp5-nJfuc54DimudJ-LSJeBeT2NwM7Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
برخلاف‌خوزه‌فلیکس‌دیاز خبرنگار حوزه رئال مادرید؛ بقیه‌خبرنگاران‌معتبرازجمله رومانو از نزدیک بودن رودری به پیوستن به بارسلونا خبر میدهند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/27214" target="_blank">📅 18:22 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27213">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vgr42q9x4SuKU52o-L0__k-mg2TJH1mzf97Q8kP6MLxVEvQ7HltdNX7-unk6x64xT112Bj6g8yFhvk4xdC5f2civQMJCPGhRU5q3VU3CUcrU2JWI3219o0rHTscfk077N_8XWVmyWG_tbY0-q-OOh7Lg_2GtdPAUCWX5P7yqeJ9yt6cxjFOtlWX-WgANXoQMlMY1wRagvZU8IM3Th-9WuWEwVNR2jJZT0UYTmnxzEyFNYe5FsmyIwJpPs1dv0EBfXRJNmdNdLIptcRtKjT2TMigq_C44G9var1_HpmGB_BSp1HDhobqFQD3SSCTNno8e93H0cgCTIkLOAhwFCTEy9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
یکی‌از مسئولان سازمان لیگ؛ خبر فسخ قرار داد رامین رضاییان با باشگاه در سازمان لیگ رو تایید کرد. بدین ترتیب اگه پنجره باز نشود و رامین بخواهد قرارداد جدیدی با تیم استقلال امضا کند تا نیم فصل مجوز بازی برای آبی پوشان پایتخت نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/27213" target="_blank">📅 18:22 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27211">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ubTWwhIfhj7243BJhAJP2bZJBvW3Q8jcHodQIKaPGR75g31-KUxX22yNOtR7psKwihuDRDVSMkYnhr5xV6f1bIH-Shv-vJq4O8Y7Xx6QPe3SLUV_FTqiAZs6skoCDyf88cnp0ZLDw-9yf3nFj1hFi5txdu-tSopH6wjYo7hF_ZRAvVsChqkB94mfQp_UuXSGWm1ufzrWs2F1s6Z3b4zXVo4XGxKQ-NWS0PKJH57H55gsSle5_UbXRVPwrLA9RKswpDhnHPbogPJazKDD_ia04sUA61z7WqFmBS89BQ76cpznVdIDY-y0av5wr8fnIsVPXkWVErHu4Z70T4bFf5UTbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
پوسترباشگاه رئال‌مادرید برای یان دیومانده ستاره جدید خود؛ قرارداد تا سال 2033 امضا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/27211" target="_blank">📅 18:07 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27210">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RLg-Ouo61JbkzRchKlc4zOdJs6LrLlW3uyAzmbryYkbGHdU_CpuYHZ6SO3ZKfcujZnOXxn4dcod6OQYkrME2M-j4GoNUP2pTJJOfr8gAKtAaknFopCJ8WZyK5fqJgMuiVb1onsRHpPNeimHCCXnClggLcYncwpUC-VFn8qLyhLUQF3K3em-UBVPKhaIQnY4eLv5rCmW7B05tPBWlQ4T28xEbW6tTzfu_OvPJVplqXRwwRnYet8Xrd_nD_tFoF1kkG5YlN9Za9iszZzeOWug7nny4ADNNksf7vczPNpI2lWi3EwCdzpgvIF7G3ZhAO5SVBtNu84xmIM6WoDuyAIqY2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
خوزه فلیکس دیاز: رودری قطعا بازیکن رئال مادرید خواهد شد اما سران منچسترسیتی قصد بازار گرمی دارند و میخوان این‌بازیکن رو با رقم بالاتری به رئال مادرید بدهد. رودری بارها اعلام کرده جز باشگاه رئال مادرید برای هیچ باشگاهی بازی نخواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/27210" target="_blank">📅 17:55 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27209">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NmOT2p6IeYrjXNtUfYTg11WGfRLGBsYOcnKUsCytKyOSiq8u0zcYFTUvMWXSKZRCD9e-ZwKTioZpLs7mJEH0QFi6SM5xAmPoe_0SDhi7q4egqej6MOhL8YVOXShGcx_5VNf3t-cvZSAR9CpL1lk8-Vrf1U7WR6xLCqY9qB3f8MwB0wsVkScEEOYUX7lgyyL8I7mwSpJnNF5jWXmvxvDgCCYQhxqWuTRlUj8VDhzegkqZVYCeQdR-ZtbuF8-W9FRLvSFmtwV5DqOEP8_DTIQejgsLLNA8VgWdFetdE3QXCEtOGhqK4RymVFuoNiCABOveR4xepyeIgJo8huVEsxSDCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
با اعلام رومانو: یان دیومانده با عقد قرار دادی تا سال 2031 رسما به رئال مادرید پیوست و مدیریت این باشگاه بزودی از او رونمایی میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/27209" target="_blank">📅 17:51 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27207">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hkWifa4Av9bBtO1QoZCgcf21lusefxuNnu58NF6vW-UGIxFWucBDKmiz4aL50JMOtnlH-_tu2n5NtHFtuic1RdY6SgngYOp-Vfos-2V3z5kEHxWVGJP3mRecudSqQhApFRokPSRYj125LDBfE3IumnuiuJkPS3O0fUMAYrjyXFqDenD5n3sI_dD39vlFAWjvrRpCfOHHb2vtWZmZwT_ROFTI7DKERNLTqp4jq7IFjbO2j3Dzn2cxoeHBM8M0oaCSTonl1kGkDfbWctu1-55edXSIn7J47kHVyuZnUhlr1eT8ZQWumm0tYZRDz_baU_o_1r_USWy0UuudB_zqMMz06g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
عملکردخیره‌کننده لیونل مسی دربازی بامداد امروز اینترمیامی با به‌ثمررساندن دو گل و یک پاس؛ گل‌هاش رو در کانال دوم گذاشتیم برید ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/27207" target="_blank">📅 17:19 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27206">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f47e64799.mp4?token=JbHRbuyj6s_MPziRhzN-25xHc4mOsuESd2WP7ft2HRRfW1nQ4FH5BFokCMh0BOcxh5F8bk8ttWGKxr6V13kwuMDuQ3Lb7Wn9x46tZ2EFiJsaDuguxDnxnVqRjeV1R4JdULmAgLFMVJMe808EdbIUA0p1Ciqu83IigOB4JSwwWjcQeY2-cnHFyxfUZUVS9Ndm1UF3_6DYhDOMKHflxm3erOHRm1xfmoiEowShArTXNmXwZCvF7OTJEcvp186haA5l_GBu4Yg8NRjz3nwF-dhlCdC_W7yadl2b3UKjVY_Vv07EuW4IjAcKiQCeIf7pBXtlW9IzSUYKBL6ZUpDyMPK_-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f47e64799.mp4?token=JbHRbuyj6s_MPziRhzN-25xHc4mOsuESd2WP7ft2HRRfW1nQ4FH5BFokCMh0BOcxh5F8bk8ttWGKxr6V13kwuMDuQ3Lb7Wn9x46tZ2EFiJsaDuguxDnxnVqRjeV1R4JdULmAgLFMVJMe808EdbIUA0p1Ciqu83IigOB4JSwwWjcQeY2-cnHFyxfUZUVS9Ndm1UF3_6DYhDOMKHflxm3erOHRm1xfmoiEowShArTXNmXwZCvF7OTJEcvp186haA5l_GBu4Yg8NRjz3nwF-dhlCdC_W7yadl2b3UKjVY_Vv07EuW4IjAcKiQCeIf7pBXtlW9IzSUYKBL6ZUpDyMPK_-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
خوزه فلیکس دیاز: رودری قطعا بازیکن رئال مادرید خواهد شد اما سران منچسترسیتی قصد بازار گرمی دارند و میخوان این‌بازیکن رو با رقم بالاتری به رئال مادرید بدهد. رودری بارها اعلام کرده جز باشگاه رئال مادرید برای هیچ باشگاهی بازی نخواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/27206" target="_blank">📅 16:31 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27205">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BF16uMZd9hSbBQLGgJIjR9mkL_-01yUygVhH-cP1JIXjJCpLsJkhhXZRQKkDtDexsh4Icm3EsBAyZocDip5i5wgCZ3qpwIpkuHZC-4fNWF4nBiNw6eT8N9iy_eM7zOdC5UXk7QJKC20Oa0HwYryTnwR9QmDAPCQx4zA909md-ltQRziyPVkE_dvgIRJSej6HImp8wdMZ7QwkiEcGl7mlEf0RlpD-VeQhsrdiiOEasaHx4tn_yu-WPVrq9Q8Yg7dEzWCspOfTaR6rMXMytYVBtn4wzBqjKlyL8EiHfxSxis8V2dydLnRGnl41gZQYaHXbogMtavhIyjx1fqIJtCDsyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیریت تیم‌استقلال باایجنت‌های دیدیه اندونگ، موسی‌چنپو،داکنزنازون و آنتونیوآدان تماس‌‌های خود را آغازکرده و اعلام‌کرده‌هرچهار بازیکن‌رو برای فصل جدید میخواهد. اندونگ، آدان و نازون آمادگی خود را برای بازگشت به تهران اعلام کرده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/27205" target="_blank">📅 16:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27204">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WEiPxiQ0NNORQzZHdEcEEhAf1uCM6XCHz7R-eArO9r1YAAMfYh_pvpdXoX55IgWABM8fT2AKhJbGAghcWciWAh7A0Sn6ZrVmI-76Ew2cnO-xVd-KDHhWdZWO4gVO0ngELPeaTfjHRR2a5vP8OqDgW1BrazfCzDdlilxEz7RsE_6921GH96J7bySYxcyjcSKKCd3mpZbWVGlVU4E9w8US8N6KRjOvfpM3aHlYLhNBGsHItf8kGvYvhWCJmKZhIpP3vFHGU_9tTjx7gwUCgckgkrTkm8aKVAtYmG-4s73yyGiMSV-6pxdJ6Ybiyj-oTCNs8FyNS_E_FrY6B5k6-6L4xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
پابلو گاوی؛بازیکن‌اسپانیاکه‌قبل‌ازجام جهانی گفته بود اگر لاروخا قهرمان‌جهان شود موهای سرش راصورتی میکنه در روز تولدش به قولش عمل کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/27204" target="_blank">📅 16:11 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27203">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcW98M2s8GHK1-VMTAu0AzZuDnQt0BfD7s97UrrFxpGwOxXNXvCUjck-EYdtVzZaGIivhqwFcxdtCG4JRC_BNXqFC6WUS30LIAC3wBPpDAipwp64dLudYuV26w3l1jgLcV_lUFG0EzIvgBHFfEuA0Is6yy46HvQtyEnZecTURckmXAVwBr_w0vvYRUbCjH60IpYm_bu46_p2yybileDc_qqsPml9puWFsjkAW5PNPRuMuskegfSBXJxvNG3o6tw20ImHVMnvoH-rm22sqZzkxYRJMKfLr7t8zQQnySfr0R7wabOwyX9bQdBYwEpcXMHTszAkI5QY1EdOeVKcDp2OdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق آخرین اخبار دریافتی پرشیانا؛ باشگاه استقلال برای‌دیدیه اندونگ هافبک گابنی این‌تیم بلیط تهیه کرده و این‌بازیکن‌ظرف 72 ساعت آینده به تهران خواهد آمد تا بعد از تمدید قراردادش با آبی پوشان در تمدید شاگردان بختیاری زاده حضور پیدا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/27203" target="_blank">📅 15:44 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27202">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EsD5gE_RNIl-hLUik63z368lsJoDOEurCtIreCukbnCSXUXLHdhmtt_7A4T0Pjlh1lcscmPJrQBa2pGapwCGkMbjW4ioESynwYy9Fcqo27z-2jLyJAMKwIqJzHuKagVEprT3ukiLa2qfiNqrxFvrJ2ijj0pH-boEIToaGRXv5mTJPmvpxm89YpAAJvC51tEwXrIfHfNZ4pKj7Tqbl-wMCfLy02WBRzTAwO4pLvtjJUiEwwyPSV0XOCWtwyePiQs7hyx0FsAQckJeVULji3rmu6nfJl0XjdbY-XQxg0gZZ7yuJmmaffkKmmRWbdJcHHbLLhw20DB2da-4ITdBYMtHDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق شنیده‌های پرشیانا؛ بعد از بسته ماندن پنجره نقل و انتقالاتی باشگاه استقلال؛ علی تاجرنیا شب گذشته بامدیربرنامه‌های ایرانی آنتونیو آدان گلر فصل‌قبل آبی‌ها تماس گرفته و ازاو خواسته آدان رو برای‌بازگشت‌به استقلال راضی کنه. به احتمال بسیار زیاد آدان بزودی…</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/27202" target="_blank">📅 15:32 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27201">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97dd42f0c8.mp4?token=XWeIK-sOwb9H3FFDVN1n9ghLAOj_SJsQDQEo8Mgq526i0Sh_idqzjbPEf5qZtNNrsr6Gh7mnxaXUKunS_XWcKD7Hnkwb86A-m3mzXSNTs6Xny0AF0_s9lxmGB_rNacKaXdt0R8NJ0ygFY8irQThaC7Okc_t2KpFc2BO2vaQ_IyQ3pt0BrBvSInf6G0qc9iFr8cho34G2Q_lHes_UUkxlFcQutnaT-yanDXzCUwtxD-qP8dLqaFmsWAJputn8wDDK_QqVtUJ4UONE_eFhMLGiPhpdYvsNzyy2bh-a4qtrOoKEeBAt3QdvDY0-fbsjGn8Nw5opKEaEG2cwFTOcfzDICw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97dd42f0c8.mp4?token=XWeIK-sOwb9H3FFDVN1n9ghLAOj_SJsQDQEo8Mgq526i0Sh_idqzjbPEf5qZtNNrsr6Gh7mnxaXUKunS_XWcKD7Hnkwb86A-m3mzXSNTs6Xny0AF0_s9lxmGB_rNacKaXdt0R8NJ0ygFY8irQThaC7Okc_t2KpFc2BO2vaQ_IyQ3pt0BrBvSInf6G0qc9iFr8cho34G2Q_lHes_UUkxlFcQutnaT-yanDXzCUwtxD-qP8dLqaFmsWAJputn8wDDK_QqVtUJ4UONE_eFhMLGiPhpdYvsNzyy2bh-a4qtrOoKEeBAt3QdvDY0-fbsjGn8Nw5opKEaEG2cwFTOcfzDICw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش پادکستر هوادار محمد صلاح به انتقال او و پیوستن به ترابزون: این چه خبر مزخرفی بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/27201" target="_blank">📅 13:47 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27200">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‼️
واکنش پادکستر هوادار محمد صلاح به انتقال او و پیوستن به ترابزون: این چه خبر مزخرفی بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/27200" target="_blank">📅 13:40 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27199">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dab647f68.mp4?token=tuyH5l5BKPMeesbkeNtHb5OGSKdgfewjzAsXpb2IDijlZ2PacpgdPjUiLk42VIPBj3xaoUIy02cDK4mBIWlIqdhb9SubydtcQrLvBckL53eSexsQPjUaxcgBqX3KzNMUPgdNeppprRa3gwFXthiDklofkqERF7WQwNOhDe6LNxGbLuIIp5hZlr7cVDdt3ZbfYuidOr6EVbNViBoOdnhZO7QGjhtnBnlyQO1gLwg8snKUK-0aJ82QcIYC7X8LTTYOZ5xuL_PDzc6QDKxjD7W7PbbcIp04rDOOis59cEk6Z09-5OQ2Ti9LV46eQQNjUJAVjszNk1lNx-1K4FN2_NN82w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dab647f68.mp4?token=tuyH5l5BKPMeesbkeNtHb5OGSKdgfewjzAsXpb2IDijlZ2PacpgdPjUiLk42VIPBj3xaoUIy02cDK4mBIWlIqdhb9SubydtcQrLvBckL53eSexsQPjUaxcgBqX3KzNMUPgdNeppprRa3gwFXthiDklofkqERF7WQwNOhDe6LNxGbLuIIp5hZlr7cVDdt3ZbfYuidOr6EVbNViBoOdnhZO7QGjhtnBnlyQO1gLwg8snKUK-0aJ82QcIYC7X8LTTYOZ5xuL_PDzc6QDKxjD7W7PbbcIp04rDOOis59cEk6Z09-5OQ2Ti9LV46eQQNjUJAVjszNk1lNx-1K4FN2_NN82w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های‌ تامل‌ برانگیز زنده‌یاد علی انصاریان ستاره فقید استقلال و پرسپولیس درباره حسادت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/27199" target="_blank">📅 13:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27198">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iDihtuSF7fNDNIB6biIWWXEifYrOwKP09EzVPw05YIO9SMTJfpcCi6QPj5gOZhx_e3DgRqKjiMCe16LaZlmRthkyYngsLALCl1niiuasFQ-3jaECuXZqQnSPIvqqbHPhLwANahvNSmTlR0iidxWZT0HMgBm07ffBqZhgwPvNjxDL7SmUQpQF7eypk7muNk1ECgBsB7ADamdVRdXe8WmWuDXPiTwqC5f_Qs6v8H_OlaYZKhhkKEWGwF37EyTJ_jl8-c89ea7pD4XDWrAKKl-zWhwK-1R1tY35ljT_gm-vMcHj-eVU5HSUInRk7IdVEUbdgyLSAeHmDYAC7dk1wtPjyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخبار دریافتی‌رسانه پرشیانا؛ بانک شهر بودجه‌لازم رو برای پرداخت رضایت نامه دانیال ایری دراختیارمدیریت باشگاه پرسپولیس گذاشته و انتطار میرود ظرف 72 ساعت‌آینده این انتقال انجام شود و ایری با قراردادی چهار ساله رسما پرسپولیسی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/27198" target="_blank">📅 12:57 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27197">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WaSf00vB1VcwgmcSijbLJ6ZVd6-k9zgofNQgDnC5SbI2eoHDVGCEYrlDQDcjECVF3pw4LO_ynhc9VXO9sL5HeD3t0grcxjxVeYcLSmrVqtZtYX9dT-3w1LjePxSh3G91fcXRfSz2iwWCSfGx7h75b_ZSjAaENvahhkdRJHqf0vhDw2PVNgxM7AojZeSycN77WCLapfWFruW_ag-czw1_2u9jyEuYyBX7UasQNChAqyiNNATeEh_iclFKuwK-zbDte0E6OfIzNXUjwca9n_OOqWrDpLkwu8kTJufaiBXQQ3mGDw0TwxNCay-reh5CB-Tibb2Fqp2VqyNcFYPD8rX1Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ فابریزیو رومانو: بعد از رئال مادرید، بارسلونا هم برای جذب رودری دست بکار شده و با مدیران باشگاه منچسترسیتی تماس‌گرفته و آمادگی خود را برای فعال‌کردن بند فسخ قرارداد این ستاره اعلام کرده‌اند. حالا همه چی به خودِ رودری بستگی داره که رئال مادرید رو…</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/27197" target="_blank">📅 12:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27196">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWFik_U4KiWnOHzoaAP1JffPZ4o6ho9k2XpR83Sx91NPta5U4WMX6oq8HPZfRQ1k40sBSxLzxQWwnDEZ9YyBdUHpKe_8Keqh2ZMdXWyQZpqfTLox-cnQqM31HMobVf3ln0RRa8ZHxuGBfU6GMr5d_4bkZ010YOA2epEr34FZBqSV9xI4fGe1j2YAB0NRtG4H80CZJ8fG-spi5OKG173yUmt3KUCynn4c4MQ-vUeuZ_Tf5dV5XnSq0V6gPqvzSocVhmHgsnWkoZV7BnYp46HzMpwlGnP30cKl724nc8CS217eLzZj-H0DbE-u-YByWH1XVnVeW2HW_huF4L_i9WAkWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
رودری ستاره اسپانیایی 30 ساله باشگاه منچسترسیتی:من‌تمام‌پیشنهاداتم‌از تیم‌های بارسلونا، پاریسن‌ژرمن و منچسترسیتی ردکرده‌ام و تنها هدفم دراین‌تابستون پیوستن به باشگاه رئال‌مادرید است و مطمئن هستم که این انتقال‌بزودی انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/27196" target="_blank">📅 11:57 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27195">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17c93987d3.mp4?token=CZLT_WaDh2qTXF8gRXvOf0nfC5qFgmTaav-DFST65-1dAa1qZuitghKjuPsYsBGeTaXGif9ONl--x_9a505U628WuArBViyE8ggnhT765u_WkZ5n97oUp2xF7Yp7rTjWsrqtDdg9mLqnV0Cxdx52jGMR5TGFPmehDVh8RlisMjyw8MuZQEJjegBTtmtjHru2nDQIi_7LO6i8Hz0hvkos5Cr3-tKU_Nb08a182uTI-Ua6tIlM5-WkxYkjRdHX4ZXTTnjwF_b6QTMnlEjm8oMFnpfivJTBqYfousjUkNgVXeVVrBQjNnLiYi8eEsWcB91zLNiZOdshyG0m3Hr9uM7zWKBsh7ZwHFg0qdFSuvzP6KtyxsDTJFDtNOANS0qcXqKDHmQyVBADtZG5mzMTz4EHPpr7MzZSmn6wO52MXS5lDWYWqe5jMfev2PLa_Oo7oNhaX-9agURS9u74PIwAVnuJ5I93_hLci6t_5ldvYAYWU0kFz-8otLwPpGlk6KDYPlvfkI6H34pZscOEdJ-JbDTS8SLH3pZDuATLH9MMmBJg1U43T2g5nvSg5TsXLxmqLj4lA9SAxGC7jQYVIMQ9NJYv08pdhrzzGNFNBWIMF4OXXvkfMwF7KAD7uh19dFrYMWXzwpYPd92AX0BgnwDxotllHyplv1IshpSF8Zem-731oqY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17c93987d3.mp4?token=CZLT_WaDh2qTXF8gRXvOf0nfC5qFgmTaav-DFST65-1dAa1qZuitghKjuPsYsBGeTaXGif9ONl--x_9a505U628WuArBViyE8ggnhT765u_WkZ5n97oUp2xF7Yp7rTjWsrqtDdg9mLqnV0Cxdx52jGMR5TGFPmehDVh8RlisMjyw8MuZQEJjegBTtmtjHru2nDQIi_7LO6i8Hz0hvkos5Cr3-tKU_Nb08a182uTI-Ua6tIlM5-WkxYkjRdHX4ZXTTnjwF_b6QTMnlEjm8oMFnpfivJTBqYfousjUkNgVXeVVrBQjNnLiYi8eEsWcB91zLNiZOdshyG0m3Hr9uM7zWKBsh7ZwHFg0qdFSuvzP6KtyxsDTJFDtNOANS0qcXqKDHmQyVBADtZG5mzMTz4EHPpr7MzZSmn6wO52MXS5lDWYWqe5jMfev2PLa_Oo7oNhaX-9agURS9u74PIwAVnuJ5I93_hLci6t_5ldvYAYWU0kFz-8otLwPpGlk6KDYPlvfkI6H34pZscOEdJ-JbDTS8SLH3pZDuATLH9MMmBJg1U43T2g5nvSg5TsXLxmqLj4lA9SAxGC7jQYVIMQ9NJYv08pdhrzzGNFNBWIMF4OXXvkfMwF7KAD7uh19dFrYMWXzwpYPd92AX0BgnwDxotllHyplv1IshpSF8Zem-731oqY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اخیرا دانشجویان رشته علوم ورزشی دانشگاه سنندج به مناسب فارغ التحصیلی این ویدیو زیبا رو ساختن و درپیج‌دانشگاه‌منتشر شد امابلافاصله چنان فشاری به مسئولین دانشگاه از سوی نهادهای امنیتی وارد شد که مجبور به حذف این ویدیو زیبا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/27195" target="_blank">📅 11:47 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27193">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mafn908mvuNFicMBBLm8Il1RExGgf745VQ4_HPa-waICEaYsYwrfdHxLJKa9o-AltlJFb0obAEP5hcluocDNXQtUctfGSCVdxZSIHqDPfTm0zmGSg3b_hMv4vZ4cygF3xv4TrPI0I8-IT1YnNKtzeLWlDRgxsoVpqDTS1gFEpWVSRk4cOS9PxZVMQJ9dRjkiOttgExs3kWDwxXu7da68x9lVn81TOK8UA4xKlrhuPZNLxKr47XFl4YFr9UgdFujK6vI7zqMAC8z4Pb12_9CnuElj4lZUaoM7RDbBzXj-vMO1zZxuT5jDwgzYndy8Vzv-1MpiRsEAnLgy7Hht_rzEzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p02NJN6AfPdtPcUc9dy5N8X4fsGltVIth9AyzfiNWB0wIVG0t9IiQZBPIFIAqZV8H6jqOFL7pGEiHZHer9HGp7905T6C_GN6fneo5MbahaiclogeqovqKeA7VKTz6s8hObNPfbudcn9AwzRBVP8IwBDCK2o66L1jR-G9f14Ti4HMC00p3IFvjHu1A1lSTit_WRSkL38YH_JEoNI0NXtESwH-A_KP09haT_paZeMEbAmZanTNilQQOS2Ndr1EnY492oeF2ENqe-JyR9XIPWBDZBU9aipGLawyeaAhgrkiIBIfqxvbjQNlHiHgrw0lG8h56ltkOfORflqnHXY43bdJhw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
به جورجینا هم اومدن احساس بد بدن راجع به بدنش، در جوابشون گفته: واسه من موفقیت واقعی هیچوقت این نبوده که خودم رو توی یه قالبی جا بدم که معلوم نیست اصلاً کی و چرا ساخته‌تش. موفقیت واقعی یعنی با خیال راحت زندگی کنم. کنار آدم‌هایی باشم که دوستشون دارم. حواسم به خودم و سلامتیم باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/27193" target="_blank">📅 11:21 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27191">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/165da6fec7.mp4?token=P2T2THmIVcObx5NNIQiNuzzgkTaBWziVNZU-lrKbptTnVNumqpw0bAUg3b-erOR4-hcdqWe8Xmm97HEn_5_dn_5I44eiHUc6ixCnS-kcYLPkknTDI5cji9I0FvHQCO0bYa0-s3x7rBUMVZObrrPTjQjckKU1NpfXA3g4huOyGzcJwR-serSUzfFHXX_7Hm5A-r7qDqWIAfsIhxfWkWKEmj_bOay0ChWb2hGrWDS8dE8gstkDLTVrMyQftyYaGIF0tUbbAAet6C4WssMDVIZcAT5ZANniDrbmx6w-pAMmKqZLVLG5FRLYAsRaJfpMdISwqQ1gm-AG6Q806zt4wV007wOx9hbmUrucI9XOgsFYDGNh8AT4awtoQLwu-MNAXsCeh4eMt_JFINgqfyM9InNYNWVsnQO2JlHvfad_goC2Y06OUPRhvlm5kKvdeF3t-KyIICHw3tLRcy2okpDzm5a6-PnDFrp6KVtCndFxRrqw5ByeKkuoHOJ5U9zi6VNzRemQjLi9bhw1pbNhny9hIXBwTsF-aiBZaWS-jHRR1oJjlMIJiaTST9O4hpx260yQ5hWpH21RmAWozBHLancg9Ddxx8f7f-eKoBiJMsmKdaoi5D8K92bgN-u55SwlDorp_2XzrjUaFs6rIen3eq8HwVIs_PcB-ZGP9plB_y5C0PraneA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/165da6fec7.mp4?token=P2T2THmIVcObx5NNIQiNuzzgkTaBWziVNZU-lrKbptTnVNumqpw0bAUg3b-erOR4-hcdqWe8Xmm97HEn_5_dn_5I44eiHUc6ixCnS-kcYLPkknTDI5cji9I0FvHQCO0bYa0-s3x7rBUMVZObrrPTjQjckKU1NpfXA3g4huOyGzcJwR-serSUzfFHXX_7Hm5A-r7qDqWIAfsIhxfWkWKEmj_bOay0ChWb2hGrWDS8dE8gstkDLTVrMyQftyYaGIF0tUbbAAet6C4WssMDVIZcAT5ZANniDrbmx6w-pAMmKqZLVLG5FRLYAsRaJfpMdISwqQ1gm-AG6Q806zt4wV007wOx9hbmUrucI9XOgsFYDGNh8AT4awtoQLwu-MNAXsCeh4eMt_JFINgqfyM9InNYNWVsnQO2JlHvfad_goC2Y06OUPRhvlm5kKvdeF3t-KyIICHw3tLRcy2okpDzm5a6-PnDFrp6KVtCndFxRrqw5ByeKkuoHOJ5U9zi6VNzRemQjLi9bhw1pbNhny9hIXBwTsF-aiBZaWS-jHRR1oJjlMIJiaTST9O4hpx260yQ5hWpH21RmAWozBHLancg9Ddxx8f7f-eKoBiJMsmKdaoi5D8K92bgN-u55SwlDorp_2XzrjUaFs6rIen3eq8HwVIs_PcB-ZGP9plB_y5C0PraneA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#فکت؛ محمد صلاح فوق ستاره مصری تبدیل به سومین بازیکن‌بزرگی‌شدکه‌به‌ترابزون اسپور پیوسته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/27191" target="_blank">📅 10:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27190">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OwIgZ918kU4eLKhysveepqckwHEbHlLCphIkfS_SbH_llAiP0y5RNoc1sWXbfBCHk4WN6ul-EOLFku7yt1JAvZhURaiFt5d9QI8Bj7eYnTgUYjigm_038xcZ5T6N-Ux-6ezAp170ZQfcBudLPGHPOGlAulChiy7An0o27mtBfzEcQVDemio-x-QUHxZ10q0xRdoQg0TdcnMNCg1PoR_Iw_J709cfCC-UArT_Dj82swfHh9mqJvwLtOVAdcRxVIEFo8LG-tgCFN2IZevErHloWCJ22sWC-VgnaysEJXLfIajLSlsqZIH9JZNkrPPRSqh2-CPcDKE9kSayl24OBK5G_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
عملکردخیره‌کننده لیونل مسی دربازی بامداد امروز اینترمیامی با به‌ثمررساندن دو گل و یک پاس؛ گل‌هاش رو در کانال دوم گذاشتیم برید ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/27190" target="_blank">📅 10:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27189">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a1ec418ed.mp4?token=d7pFU2pJpde4SGT9jFENEme4BOL5ohB9FIcgU6fOsMVfi2va7kY0qky6uReGMaWTpoun25fL5VwlUXu5elU-7bTn2wQFidY1NKjcEeoCg6PofCoWqy5iAabaUKuHYtBbH7sL300uZXFbX8jEZ2bLeKDff5UWCFXojzYtphuu9W3zqYyhqkJ5O4riuDwMW8PZvn7W9Q99v8IDu9O7P1SJLuFubaZTel9c75XtDxXWEelviyU1FDAyvRag9UXnZReXjoQ7p28Ss0ajJnmlEUF2kz0yCsY33jlZF3eTM7Ig3bptKCrDQUoFtMzuOGLiYI9IwwElWD_tZtY6t6HJ3LAPgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a1ec418ed.mp4?token=d7pFU2pJpde4SGT9jFENEme4BOL5ohB9FIcgU6fOsMVfi2va7kY0qky6uReGMaWTpoun25fL5VwlUXu5elU-7bTn2wQFidY1NKjcEeoCg6PofCoWqy5iAabaUKuHYtBbH7sL300uZXFbX8jEZ2bLeKDff5UWCFXojzYtphuu9W3zqYyhqkJ5O4riuDwMW8PZvn7W9Q99v8IDu9O7P1SJLuFubaZTel9c75XtDxXWEelviyU1FDAyvRag9UXnZReXjoQ7p28Ss0ajJnmlEUF2kz0yCsY33jlZF3eTM7Ig3bptKCrDQUoFtMzuOGLiYI9IwwElWD_tZtY6t6HJ3LAPgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه بغل کردن جواد عزتی توسط یک دختر در اگران عمومی و تذکر حراست سالن به این هوادار!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/27189" target="_blank">📅 10:10 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27188">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33a3912563.mp4?token=VgUS-dioPCo4yEqSVRzQz7pTobzDOYnER4tR5atqM_s7WAxwjqZIAb4tGX8dLJaeaCMA49z_-I8p_NEG-RuRYyiGrczVrUKQACZUiWZT6LZvIs6TS1HMfN3eY7KyZfpQu1Hbe-LdVRzx7mvDp2RidQX_zZ_MnbNqhoDWuHSO9N8P7IYkFcWD8J3Tj7Ctr9glTicdoewl7CD3ZcxTSDwZoNH9U6nfLWL196vWNsjNYMTCpxcvdWnBYtL9eldnDZNoSmuYhD83q57apm3Mlyt4koZU3f-FypdDCqk7dVKb4-OGuHj8Llq-cTtQjhQxkX7qqo-MFEm5d3rNrlFYhH3BRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33a3912563.mp4?token=VgUS-dioPCo4yEqSVRzQz7pTobzDOYnER4tR5atqM_s7WAxwjqZIAb4tGX8dLJaeaCMA49z_-I8p_NEG-RuRYyiGrczVrUKQACZUiWZT6LZvIs6TS1HMfN3eY7KyZfpQu1Hbe-LdVRzx7mvDp2RidQX_zZ_MnbNqhoDWuHSO9N8P7IYkFcWD8J3Tj7Ctr9glTicdoewl7CD3ZcxTSDwZoNH9U6nfLWL196vWNsjNYMTCpxcvdWnBYtL9eldnDZNoSmuYhD83q57apm3Mlyt4koZU3f-FypdDCqk7dVKb4-OGuHj8Llq-cTtQjhQxkX7qqo-MFEm5d3rNrlFYhH3BRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
پابلو گاوی؛
بازیکن‌اسپانیاکه‌قبل‌ازجام جهانی گفته بود اگر لاروخا قهرمان‌جهان شود موهای سرش راصورتی میکنه در روز تولدش به قولش عمل کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/27188" target="_blank">📅 10:10 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27186">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ise4MtItvG8qaLX1ExFHnH3v3GzUvlddQJ0qc1hRQ_5lW2bdge0J2LwfiYXKcMy2OJ74WfYcd4__ttH0PR51fAh_d5Eu0guGo3kaCFJNRiWIctL3W0mqQqqUgU0hPx1gHlvDeoqcKFwefW0fiuU-iLFPPA3vxbIlm8FmZDRhpHc4VbFIPYswf6R9c2Hl4PekXI6ghNAYigtY1mYyil6Uot8WafhdOln-bUW9Q-1LeEgYAMQ7ctTMa1dZ8DTgk_VVf1U6vc9qnpG3Saf8SviQgJ11NXCSZiNjqkpbRQ0xvAhHOEL9SPw8IMPn-_mad1OpelnXpm9YzrEs7WqIdoAo9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
نزدیکان دانیال ایری از توافق‌شخصی دانیال ایری باباشگاه‌پرسپولیس خبرمیدهند و بانک شهر این باربه‌مدیریت‌نساجی قول‌داده که بزودی رقم رضایت نامه این بازیکن رو به مازندرانی‌ها پرداخت میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/27186" target="_blank">📅 09:53 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27185">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCKqd8XAf7SupMWBoYD3UHNsX-SFsRkZaoTWxdLsYGOmVnFHYyVBn3IN_EeZJ3pthk7AbyIklMG21kDpBV1u6XyvS3M9jzSli88il2_zaS3RzfyL4GvQz12w2Q3I_Ep8ox-NdvgO2s2yX5Xh1I_4tUvybrsKpaAq1JoE4atlLo50bjlcLOn5eASL92SB-gKMuPvZbAwkMCmct_wymoMRdJKIabzcWUqOuhb3jescI9CQOMXHVwzXUb0IeWcoa3-DG7m-o7p-EG1h1mic0kxuKbvbnABHTOUQDzBSihIfzChYMht4QpCCdx1Jbg1D9KF7AcDh1GGuf0ZaeYZGsQHnDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنتونیو آدان گلر سابق استقلال: هیییچ صحبتی با باشگاه برای بازگشت به استقلال نداشته ام. باشگاه استقلال به‌من‌بی‌احترامی کرد. دوبارنوتیس فرستادم اما مدیران‌باشگاه به من‌پاسخی ندادند. بر خلاف میل باطنی‌ام مجبورم از باشگاه استقلال شکایت کنم. اگر جنگ نمیشد استقلال…</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/27185" target="_blank">📅 09:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27184">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XcAHDXnAqR_tttFunoXIjwJzkQXXALlqFEmh1pF_Dva3kKzgWBeZvObTnqENkUk8MvmfZL40IovIm84cXVQ4HV3EhpyI1R_QWFLub3KzNLXR2VpHp7q9tlfbxNMmBzHMxyOT6a1-eJGqM4rPwAeUkvoVzwuGrlC62Sd8UZeedME2E3ExNpGpbvxREbmJvcMKXMvfMNpV5ZSWrizUd0isZeqt8XgfaTGgRASjJSAIF1llye6m2qXso3rN27fnvaMBzymUtWzTCZhYY1wd_xmi3nGN8kKJZNhgbg8PXxsPrPDa04B7zLw62GCq8qIond4ZX_G-IeJpbz5y4oerqPvcog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبل لیونل مسی در اولین بازی‌ بعد از جام‌جهانی که از ابتدا در ترکیب اصلی قرار گرفته؛ همچنین لئو یه پاس گل هم از روی نقطه کرنر به ثبت رسوند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/27184" target="_blank">📅 09:33 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27183">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/syM8TY0OLNNtZxOoE3ygjjSJ6gxmrPVMPcNYmx2X6WFOml_wjihaaOiGxAeXoPqd4jHS0nYYc35Q0eofPhWs8BJCDPhzMOucWZ5TCT2dBvhhbFPJVoe1U2gpUsknU6gY4tJN5TWidnxytnahOExZmCUEB4VZ9eYvGBcbc41D3tc8d4-PvYB4RMdNVuKJP2XmtERi4Rh43OsuGfzQpN8Hizp1IdFXn5FAtDRcMrdBSRK9BawIykc8un_gPTH779PvqVcwWjms5TshkQnzleuiiSi9GDuf4Xk6KyDi5qTDcY465x73dPT-j-s09_B610cVy8KpxRuQd7LZ9zIcoP8cmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ آفر مالی رئال‌مادرید پایین‌تر از ارسنال بود اما وینیسیوس بعد از مشورت با نزدیکان خود از جمله نیمار تصمیم به موندن در رئال مادرید گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/27183" target="_blank">📅 09:26 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27181">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bdKHpxvZ80IU4MCQx67qI-xQ9SzqFChgTnVAlEIX49pPD8QT7PGtG4CeNCUUuow46p4J7GlK0DoRusAtpek_251slzwg4PUs8SqgfirfgsGQa0P3kxN870bdxkOy3Y1Gq0uHaoEraDowjyXdDr2R6LT1dmTc3cJMRYtnRJ9zyBGUQg30Y2PRxD5b1bwGsmm2LELgUAQ1TzmcYyLHjq9WT27BVBxd8ZIt0dqdQgwDtU0xkS4JyioyOgbeXsX7whzcZAy72huf6_ORaFyYN3WMu7apLb6_wrt-j-m9ACLkByxBiU98ohfybCo0JHWu8TukApk-OvXrl4RntbdMNmfv3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4684a0276e.mp4?token=fcjtGspoTeL4tt0lSUOcCsM_MqOMh7sH-Mz4jEf8UoVk8ADWsFznitoLcEOthKbhVfZcdl-ZEUtVNYfVSOouKsqLHSjF6bcV8XtWF1do1CCdfGvquy6mLUEe_iG1OtgU41fUi1-g7tsqgW71vzSXxt8tc_HGVa9h6MjQpwfUOejFxClOfNQod0reIJ6r9F5x6G_ZgkDzKj9d14rNTdCl_uzAzlqGPfIV1i6eZnRL0Z8B3XcnIHkE1kO9ZTJ9SHRPr9MynEWMouijuHokSfM8EHNvDnKcXvrGHtyM-v7Fmn2Iyk0dy-nWXWfFmEypIOpaCxlvxIcX7Q6lixk_AW1yIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4684a0276e.mp4?token=fcjtGspoTeL4tt0lSUOcCsM_MqOMh7sH-Mz4jEf8UoVk8ADWsFznitoLcEOthKbhVfZcdl-ZEUtVNYfVSOouKsqLHSjF6bcV8XtWF1do1CCdfGvquy6mLUEe_iG1OtgU41fUi1-g7tsqgW71vzSXxt8tc_HGVa9h6MjQpwfUOejFxClOfNQod0reIJ6r9F5x6G_ZgkDzKj9d14rNTdCl_uzAzlqGPfIV1i6eZnRL0Z8B3XcnIHkE1kO9ZTJ9SHRPr9MynEWMouijuHokSfM8EHNvDnKcXvrGHtyM-v7Fmn2Iyk0dy-nWXWfFmEypIOpaCxlvxIcX7Q6lixk_AW1yIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
محسن بنگر کاپیتان سابق پرسپولیس در کنار دخترخانمش؛ دخترخانوم بنگر دانشجوی رشته دندان پزشکی دانشگاه روسیه هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/persiana_Soccer/27181" target="_blank">📅 02:45 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27179">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHoUdNzD-Sbdk5nsWjcY_6Z89yICgigRri172Di-EYqYQwinKQek91NZE0G7XBMXZMZbnDj3TCQEiOFIqlHXDrVkly2PXb_nVAsZt5po4ixliKwOcLRVCc0eBWB8CNb-5252xpxzaXHtTUUcl_k7Dy58WoQdhfES8FrIS_Vsyu1x2fVZP3AwIkdlhP7WROkv-rLqxjCgzeJifI4y0wJtzC4QTBFabcbteA6LOJocWqleRy0zgkoOlzxRZi3XlVZa5tq5ctB8ryhDCEjsSTG2sbx9WsqWRTA9ck5AFgJE6qqjqXYOx6JBSvMMqoyGYXMiyPIDPfRCRjisjE2nqackmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ با اصرار زیاد مهدی تارتار؛ مدیریت باشگاه پرسپولیس بار دیگر بامدیریت باشگاه نساجی بر سر انتقال دانیییال ایری به جمع سرخپوشان وارد مذاکره‌‌شده‌اندوقرار شده که این بار پرسپولیس 120 میلیارد تومان پرداخت کند و این انتقال نهایی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/persiana_Soccer/27179" target="_blank">📅 01:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27178">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e55341bcb2.mp4?token=gKaCfjFQB19N1qQJCU4i_WQ02TNeowsamzT4XcflrHlmf-SvD5Q4oZDk96WHsb8ru_T0pDvtGKMDuMsHozxadEPZJY8uxlJM7y9iezDtFJflaFW-MumhixIGIyIG9PVdUeENgNK5vFSDSWdZ7eq9RlkvMTyu99liVyVMYtr-E_1So3g0_S6bSE1EmCXbSaaUt63uKiZkFvndeT7jTbRRoFOtQBi8qgB0II7BeepIhglb09ONY1EkSUpF_08yq4xfZz3f9rVjquh-kg_Mh6DLjobfeUVrcpPAh1_NV2DCMayiZGJVFZmnoWTo_zdM3jjfa8td1XNCvzsZcWIBp0CBfJ5xB37GOXovk3kZvqPXBLNuB9pSGxxA0IlbGiKhqvXYmB2E3K5InXDNyUjE-nLbYkaUSL2j_uyFsNrMRJ8DkKfcQCoMTDLmtuYAH57hUP-CVOD9LHNlzuuRmNo8PCZcnzVjLqpUvX7HclhXGTDA3ze_S-gzR9CdGFoWzKgFXKBqDHwAhBkzRAQRiBnYl9MDrN5Z4lDBOXmTJXt4EX_LUN-j1kk7pakz-HHiPPu5kKl8oIFrwBT2FUfAeI8MBFe4vFMdhkNmKE86yyeGOJLNBTJLgn5CZ-8zoRqTNEIBiLb3JNrrveYNQHUFEIfQA7_omXVlWDTdekq-w93d6zaF9kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e55341bcb2.mp4?token=gKaCfjFQB19N1qQJCU4i_WQ02TNeowsamzT4XcflrHlmf-SvD5Q4oZDk96WHsb8ru_T0pDvtGKMDuMsHozxadEPZJY8uxlJM7y9iezDtFJflaFW-MumhixIGIyIG9PVdUeENgNK5vFSDSWdZ7eq9RlkvMTyu99liVyVMYtr-E_1So3g0_S6bSE1EmCXbSaaUt63uKiZkFvndeT7jTbRRoFOtQBi8qgB0II7BeepIhglb09ONY1EkSUpF_08yq4xfZz3f9rVjquh-kg_Mh6DLjobfeUVrcpPAh1_NV2DCMayiZGJVFZmnoWTo_zdM3jjfa8td1XNCvzsZcWIBp0CBfJ5xB37GOXovk3kZvqPXBLNuB9pSGxxA0IlbGiKhqvXYmB2E3K5InXDNyUjE-nLbYkaUSL2j_uyFsNrMRJ8DkKfcQCoMTDLmtuYAH57hUP-CVOD9LHNlzuuRmNo8PCZcnzVjLqpUvX7HclhXGTDA3ze_S-gzR9CdGFoWzKgFXKBqDHwAhBkzRAQRiBnYl9MDrN5Z4lDBOXmTJXt4EX_LUN-j1kk7pakz-HHiPPu5kKl8oIFrwBT2FUfAeI8MBFe4vFMdhkNmKE86yyeGOJLNBTJLgn5CZ-8zoRqTNEIBiLb3JNrrveYNQHUFEIfQA7_omXVlWDTdekq-w93d6zaF9kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
تعدادی از گل‌ های دیدنی در مستطیل سبز روی شوت‌های فوق‌سنگین‌بازیکنان؛ عالی‌بود حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/persiana_Soccer/27178" target="_blank">📅 01:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27176">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/729a2d9732.mp4?token=WTeuFLcDY3gbULqyrFwDNXQEe9y2cLLlZnWSdGLHCHRu6jU9Nl4QDjL9D99FxHz-CMSqNHode7-esCZkxir_7r5XhFRjRP5HbmuAMvv2j0tDuUMCnlbHdA9VtewtxItSgj10BYgTUolSRKr7hWyzoPR4V_83BTPrTM24ErT2Wcip25Ou7sISIp0cyoufbdDAtnUU68HgspPAirXz6FoZd-dfqEE74YF5et1cCEKGwbJCYbm9fdgkqVlllZgCFdlregoC_lvc6xD5XifgVbAih_sGAcv7vGWqZ-Cj5PqK9_x07CJehXWGeJGbedEsrgpSD6Z2fO3_5a9fvBbBQTetYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/729a2d9732.mp4?token=WTeuFLcDY3gbULqyrFwDNXQEe9y2cLLlZnWSdGLHCHRu6jU9Nl4QDjL9D99FxHz-CMSqNHode7-esCZkxir_7r5XhFRjRP5HbmuAMvv2j0tDuUMCnlbHdA9VtewtxItSgj10BYgTUolSRKr7hWyzoPR4V_83BTPrTM24ErT2Wcip25Ou7sISIp0cyoufbdDAtnUU68HgspPAirXz6FoZd-dfqEE74YF5et1cCEKGwbJCYbm9fdgkqVlllZgCFdlregoC_lvc6xD5XifgVbAih_sGAcv7vGWqZ-Cj5PqK9_x07CJehXWGeJGbedEsrgpSD6Z2fO3_5a9fvBbBQTetYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌پرشیانا؛مدیر ورزشی ماخاچ‌قلعه به‌مدیربرنامه‌های محمد جواد حسین نژاد اعلام کرده که تصمیم این باشگاه برای فروش حسین نژاد قطعیه. هر باشگاهی دومیلیون‌یورو بدهد و خودِ حسین نژاد هم راضی باشه این انتقال انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/persiana_Soccer/27176" target="_blank">📅 00:56 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27175">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vg7gr1-bpxASnZYv9kurd0UoyWOOVJbF3E80kKkL7ttcf1mFeKnyvfALxUTiIS8Hk9hDVIii0fjoJcO1FVhCbs53G61MjqU5bHR23eaDqFA7BIW2M1Ef1KEjvaYKOu6ngdRlM1am_NBh7pry2iIgZePRPfO2owfPXkV-nYfQyxpyMzp4LyLXfukKPxpbDkn65TbDQ2TNJY-MNGmzmNvmlcQCDSaOxIfjUm95-XsaU3uuoen8eyf3JdikEXbxQIGj4eVbyA3KjtnDt2k2Q2zOSzUjFCA2YG9IEz7j1v82klbFGe5lKKXQAOjK0Kj1SC-7L26sMhkZ1Lk_DUAtRQJF6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه ‌‌‌‌دیدار ها‌ی ‌‌‌امروز؛
بازی یاران اللهیار صیاد منش در دور سوم پلی‌اف فصل آینده لیگ اروپا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/persiana_Soccer/27175" target="_blank">📅 00:54 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27174">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LOtY5RhpITtLagGGezCEk8XLdu0dchz8PfMLlVqloLHgFvm1XcXGOYPVmvvqWKGl4h6oPrtOUmwISUCT3-cihxs55OY3Fx14ai8K6nn0X5rTN0B8LJwilCQ0dePC2mCCgEbtilSdi6Efo5lBqlrdCLNI2ZeCLXLzf1OL7YBXAXxgqwaIIRc-6HCZwae_l_7ZmtxTEtEWxs1Nqg0bqpsg31ZYkbXNXbKRWMIndfnd2yFu_raKVjOBica7kDZ7sEFq3LAJaE3WLhfcFmGdSCEYPTuHPHjod_gGW5VD8vdMDl0RwznsJJ8qG_lu0aJGWZtX_LpeBgNlpfUsA9eSc5wqGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدارهای‌ دیروز؛
تساوی در دربی میلان و برتری شاگردان اسپالتی در جدال دوستانه با چلسی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/persiana_Soccer/27174" target="_blank">📅 00:52 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27173">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qVT1xIbvdjKCFN4-bzPa9czxq6y9iTnJMNGS3ixQlsX4SLYTFba0ojjlufosMIVR0QerCYwNnjz4YCQSc1FbvhE0tldGzO2l0UH4xtSzCZAMzeYxu5ISOoWD6Tm-SYL8gFohreJ4QBB5_lib87U2xCIspM98cOGrSCtWCZ11wB9eiv1ZNdZjpVqZIaIBca6MNGO86d5KDgMhiftuXENdF3ntVsLI_uJkBmFuu3LL-B7_4Y_AgXNCuOTdHRJ0edctK23yZ46_WTRtl_IXONYukKcas3j1O73qL_khvXP_l7o10y6MbCDUtiOiJjrx8fn0bqnJy5ycJZ1_OSIdSdeSCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛بیانیه‌جدید باشگاه استقلال: تموم کارهای‌اداری‌مربوط‌به‌بازگشت داکنز نازون انجام داده ایم و منتظر بازگشت این بازیکن به ایران هستیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/persiana_Soccer/27173" target="_blank">📅 00:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27172">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Joh4B1bymKZePsuMPgAWd3H0SsmKNJ39kzjaLy7BNZpNhYNThTRKU5m0CaPBH2m_m-kEtcqgqqYTJQgyuVWmDLVyfXencvnTUAdTuG93YG85cazXj7nMXLMj3QKgyJ3Q90kfQiLQHzMfT-ggG4uFSCoM7n7fajCSaKKgZvOoJ9IJvbPpgNKIkwjmh2Fd66Hjq80e9muuktYDHPYl_HloY8_RfzBUbXudOeHZX_p5R8lLRTM9RcF4mmdwHS6Y7cmwxYpnFujdNO326E8eSkNgd59_NndgK3qziIZHHPXHTkZuKe_kuvcRykqIWhveiuIsd44_L6_sfs2msoGPd7yulA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ با اصرار زیاد مهدی تارتار؛ مدیریت باشگاه پرسپولیس بار دیگر بامدیریت باشگاه نساجی بر سر انتقال دانیییال ایری به جمع سرخپوشان وارد مذاکره‌‌شده‌اندوقرار شده که این بار پرسپولیس 120 میلیارد تومان پرداخت کند و این انتقال نهایی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/persiana_Soccer/27172" target="_blank">📅 00:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27171">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NTH4Gz_mIim-1hl-TpAk4J6ICavekXGWhwP5-a9alKyKw_BtFcE0Z3o0Df9ZEf9Xy5otLIMBliGoIX8am00aKF__fxC9vyYxWm4xL4F1tpQhgXasWse_2Ka2ETUlcR-YfpolxxFrGvQZek6_rC5LE0jGxp6rfrchec2qDK4W_tjnzm1lNgxJJIEHm-FJ5GpgpCuQIuFmBDSKq5wiAw8donerBUfLoDVCU2o_d7mov6LjN0RjmB4LD4_cvRWtS6ASncHDIuHFPYsePVADGKgjt1zWr8ZdOr444SI8Ko5LGbWQwQiMMZySM5tKojFVisHLKQ8H_S5wVEW6vxLNU3OApA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پیرو خبرچند روزپیشی‌که دادیم؛ باشگاه نساجی به احتمال زیاد به‌وعده‌اش عمل خواهد کرد و دانیال ایری رو پیش از شروع فصل خواهد فروخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/persiana_Soccer/27171" target="_blank">📅 00:23 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27170">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQwRQ_4eYDXeA01bciFbMjkfXpjD_BdPZV_DdQ_HjlLlgk8ILC-MRUCFa8Su-hBm92-6E67q-E-VlrSZxnYx026z7gv7T5BDItmGZ0rBXVP3pxND15FKw6EDZNV0XxROj7QAGE0DcpZa8X_7Jvv4hNedrbSInwUWGQ1NYHlfmMpjGIR_5lTn29gU8Ugo86LYMZuwjV_LfCviZlYmBsyilLIb-qa9In6biIiwCFH5Pf_PMqfzpbS6K7spzURHtsN3Ot_LjIlw6YQSbsJSIqqVzctqr5SE2v3jLuv87hIaCfYVJ9DfNNs2NHds5kiAFDqDS5W1cPUYeQieUy2HeNUgMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
وقتیCR7 از اسباب‌بازی‌هاش رونمایی کرد؛ كريستيانو رونالدو با انتشار پستی در اینستاگرام از ماشین های لوکسش نوشت؛ اسباب بازی های من.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 90.5K · <a href="https://t.me/persiana_Soccer/27170" target="_blank">📅 23:52 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27169">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aUH54JPNMDVcHsxZ60HTtn9Jzld_gozrfHLrs1rdsTyP-6nbm4-BFHWTd26BoldIcMc2FVxYKMhrEggzQ3cxsxHE9RyyaSiMND7SjAFn0QcggZzzdCoBNyL-qKf8R8nALikdnl4fs3b33cUMKGOf1oxfeg3ZjCTf7xsBsAEu--b1197txhQDdDrK1SDvhoeBFpKEevWA1ymyk3xxipi18r09L1k9BMOMUvg88glVw_gnELmt9Yo37mqVbRFsYVfiZOzVlAMtHh-sQX2NV5utnx2tGMRT_0RwfMfKFLAmhIJEfWyTyN51Zdfqkmy6zUqxHipMWkue8-fsOc3U-h423Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
توییت‌جدید علی تاجرنیا رئیس هیات مدیره استقلال که غیرمستقیم‌اعلام‌کرد که رای دادگاه عالی ورزش اعلام شد و پنجره تا نیم فصل باز نمیشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/persiana_Soccer/27169" target="_blank">📅 23:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27168">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mUnkj07-mlCjw2pqZl73pgjpodGiIJkdV9JrLaGR3mKq4_HMpZtxGDQMAQIccLyolYLloFiRdY7FSeibIgl6gqkwlm42Ny7Kn3Sj2KeCtA8FxmTq6tXIPICM9SNLxK-GSUDKs8ky1xNVfQw4WUOXOuGJGpkn1ZA6mm4rRjyx4N0LgM4eXWdbArgPHLDjtJCGHge-f2dcwPfYqK8lwHG1jQ7DWNImflNvVPYvyBFxezpJ8ncI8H3iF5zocz0AXsOMdX1wcqcOHO-yLHfDm1_H-G3yxyWJ_DBuWBZ3PCQ8AL877mLF6Lur3XCK_3e1vum_-1vIaHFyNPWev3GqtFEwRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
👤
ساعتی‌قبل کارت‌بازی محمد مهدی زارع و محمدمهدی محبی دوخریدجدید پرسپولیس از اخمت گروژنی روسیه و اتحادکلبا امارات صادر شد و این دو بازیکن جوان مشکلی برای همراهی سرخ‌ها ندارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/persiana_Soccer/27168" target="_blank">📅 23:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27167">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b58266add9.mp4?token=Zu5Ngub-Sn_KAqCqodKBj0Agbwo093hl1WeWjKY6HiFZ4W390El-qrdL3Tlvd0t3pEq-1BYQtdDukqhNzoXa9HQJ4ivR1uvqd2Pw0dG5h_Nopfk5QUjKOuqOPgHvJH5z5e9Wl4whMuKyugs8VutOwxwp9e1IOgPLB-EmtgBWR6g31xeJrLbnO11LxIylLeB77-R2Qcs0D5vxI-QjvKNUdNhWaE5iPMIjKjdT8KTZ97z-kY3WH3ocwfJNk8s_X6l1VLWXG1rKSRRpU5GXN17i76iLFeSxc31lpA-YZ0507-v8HyjtEV5GV8yC4AatXfxiCpTrnJJez3RygDhvLygZvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b58266add9.mp4?token=Zu5Ngub-Sn_KAqCqodKBj0Agbwo093hl1WeWjKY6HiFZ4W390El-qrdL3Tlvd0t3pEq-1BYQtdDukqhNzoXa9HQJ4ivR1uvqd2Pw0dG5h_Nopfk5QUjKOuqOPgHvJH5z5e9Wl4whMuKyugs8VutOwxwp9e1IOgPLB-EmtgBWR6g31xeJrLbnO11LxIylLeB77-R2Qcs0D5vxI-QjvKNUdNhWaE5iPMIjKjdT8KTZ97z-kY3WH3ocwfJNk8s_X6l1VLWXG1rKSRRpU5GXN17i76iLFeSxc31lpA-YZ0507-v8HyjtEV5GV8yC4AatXfxiCpTrnJJez3RygDhvLygZvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
عادل فردوسی‌پور:
🔴
اگه قرار بود که من چاپلوس و دست‌ بوس باشم الان‌صداوسیمابودم‌و نود روداشتم. چراباید دست یه مسئول رو درمقابل‌جمعیت ببوسم؟ چراچنین چیزی روباید باور کنید؟ دست کسی رو نمیبوسم. هجمه عجیبی علیه اومده. همیشه کنار مردم هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/persiana_Soccer/27167" target="_blank">📅 22:51 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27166">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbd4624448.mp4?token=r16xAoLjql6G9KCNwGWgRf4aVenik4pdXonVMMOaaN2Hc29HKfYTEddOycV07vHc4RBWnN2S9jFr68qFKnIqvpa2iVW0gwoCbFyY7Bs1AiM77sXUUH8c1XzIYi4DXu0eS8-u0Z5GF7xCcmpAWyRXd_RMoyBDSVcm5OQH2K9xmupvQCNUMU_LhBywG4GKcS_K5MCGnZjYSBlM9vYQvAMIvFBaH5ozwdJnqUzYerr4rxBMycn36_IsytFJIQVAUf0TlxtKjJzcLJg3pvRGFh9ahb2yumw6aL6asOHWPcedpHXGUQnHIqnD3hV-CgBZiFCpA4Dg2iv86hx4r5ApLq45xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbd4624448.mp4?token=r16xAoLjql6G9KCNwGWgRf4aVenik4pdXonVMMOaaN2Hc29HKfYTEddOycV07vHc4RBWnN2S9jFr68qFKnIqvpa2iVW0gwoCbFyY7Bs1AiM77sXUUH8c1XzIYi4DXu0eS8-u0Z5GF7xCcmpAWyRXd_RMoyBDSVcm5OQH2K9xmupvQCNUMU_LhBywG4GKcS_K5MCGnZjYSBlM9vYQvAMIvFBaH5ozwdJnqUzYerr4rxBMycn36_IsytFJIQVAUf0TlxtKjJzcLJg3pvRGFh9ahb2yumw6aL6asOHWPcedpHXGUQnHIqnD3hV-CgBZiFCpA4Dg2iv86hx4r5ApLq45xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
باشگاه‌فجرسپاسی‌رقم رضایت‌نامه یادگار رستمی وینگر 22 ساله خود را 50 میلیارد تومان اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/27166" target="_blank">📅 22:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27165">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GiYtXVwi5YrM-1s--3Z141fF56IwGy4MKM5T_wq2Y5TSy6E-5NrElC1qf53hSpYFuWqr3rb7HSUdQAnyuYHNdoi54-73zR7lpf2EEov7ZEUjeFHDoNeFeI-D5bibDqbLA0WDWWjmUpaS1s_bnx1zmSN0giYM93pwUDn2A0b6FpUoIF-5sTSYKhgXaDaDy2M6ij-Q0ZdCE_xQ5mfXI1RLsDzjezBQr0b99lRDQyC2GOSvrXDiili5IuVsTDvI7gtNWqNsHZIkCkItvVJNqcQBGTTf0aDIv1dRl0S7uzM0pwq8l8OSH240MLwlXQdmFYBU5qoIr-oz6wc2gsJ1WPMiuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
🔴
مدیریت باشگاه نساجی به دانیال ایری قول داده هر کدوم از دو تیم استقلال یا پرسپولیس رقم مدنظرمدیریت‌نساجی رو پرداخت کنند رضایت نامه این‌بازیکن رو برای آن‌ها صادر خواهد کرد. ایری در شرایطی به نساجی اومده بود که از مدیریت این تیم‌قول گرفته بود که او رو در…</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/27165" target="_blank">📅 22:07 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27164">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s21LKRvGV90vp2A5PscO0pN_h1vrxqeP9-40mSQfCR1Si528VQVVY0GgK6VDYFdf4xs9G-CHobsrmQmHSmSF4Hq5VUhm3mXGJ_j6NNsSeZ_f4sbOzU_NdXqh3LApvAtnIfv-WmoGibnMK9g6EKK2SXIwriayaSkhCwgJeuOBw6P0raSyC3W13XzkwpifxT94uDZdX3k6DHuwloHS-MJxbP1GV_mAw99Imk1f89bK42e46s3bT_BhyduvZmjPki4AOWF7-hsXq4McjqOslIceS9CHzZKo2b3chVZWyJcmyU82A-kjZyH0EGHvSJLnpyb-5NlelBfP_gGnsOrqcvgrww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
🎙
محسن تنابنده:
وقتی‌حال‌مردم کشورم خوب نیست سریال‌ساختن‌ارزشی نداره. دوست داریم فصل جدید مجموعه پایتخت رو بسازیم اما شرایط جامعه به شکلی ست که هیشکی حوصله سریال دیدن نداره. هر زمانی که حال همه خوب بود میسازیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/persiana_Soccer/27164" target="_blank">📅 21:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27163">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aR9nlFaikGhpE0yin3UK1o0y9_WFuc9Wknr61Wwvok4aVz5pzl8-DJxN6DtBJcH7vYg-41mrqCHWLp54sFbjZdezgxGQjtzfYbGue1cP1EGgHZGI0NcNOFO7hxHHCWsQEBeusO544l8Ey5x8nGbFBWuh4cMFdwA52Lat4q2ycZc5f_LtFULJVLRSSJAlRrrW1oOQh-P5_tKjGrY34Mf63LwNxnEXGAYJ8FGd098BjcymcC70sRHzx11GWPQEZtXyKe5GGiwjBC9p1eN_2-daYdUtVntYzob9e4g_DmmBYZfum6v9My_rLo5wl6SGKP582ca7Wpi3CCbaq4M_G7OsvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
اگه‌اتفاق عجیبی رخ نده؛ تموم خبرنگاران و رسانه‌های‌معتبردنیاخبراز موندن وینیسیوس جونیور در باشگاه رئال مادرید میدهند‌. گویا فلورنتینو پرز با رقم درخواستی این فوق‌ستاره موافقت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/persiana_Soccer/27163" target="_blank">📅 21:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27162">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QB9tE9hCIcr1qk9pysl-upzSoepvP899Am65i-lIe-O-5-XE17WwprGZFeI5xIefe0qLEfawrRK-fnhFryjGumMEFzpGtnLxHvXzonv7k4TJD0CpPpEbXyKEnuIh4B_jqbDKXbZqfeDCMKW0TKIPqBYrlvz5Ao3SEYitSYufTZcK7cuxEfAWT_dcygWLxyteuYo3QFPlwXlX1cL25FpPmf9VPHeTZbMCv4k9ViWFmMcY0eRLE2zIeKZA5xNvJ8Hoy2NmdZu4M65UJeyoTs5NH6-TvESLJYuR9HvGrdwsHNMW2tsCrq2upEM-OJfaqkCuIArW1TZtMBXyBpCVkyqioA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق ادعای جدید مدیریت باشگاه استقلال؛ فردا تاظهردادگاه‌عالی‌ورزش"CAS" رای‌نهایی خود را درباره‌پنجره‌آبی‌ها صادر خواهدکرد و به صورت ایمیل به باشگاه استقلال‌ارسال‌خواهدکرد و باشگاه در بیانیه ای اعلام خواهد کرد که پنجره آبی‌ها باز شده یا نه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/27162" target="_blank">📅 20:40 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27161">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ojgSA-s1dk_g51Wy3sIk114no5m9GGKoWVll4NxY18Jph_aI84Jvq20baRvphQsrFIRn9cxhRRWPUFt60sHD9X833X8MVhUYQat4d3-gXiras9AFpCgghaqXyx7zBbNRgXTCAX7OvI-hPRh6OEOCHcjIxIBWcLO2sfnNVUT9dMOvY2BvXsHbDW25PFNRYTS2KLULI5eKbvTw9xGBLDekM3Pf4t1rgd9gc4QN67RSvdzyE4DhuvtbD0vcqFPArkdShPxIcIn5pQOgcZjGg3U2zjCLOZUQVVS3hYYjvZL2tOhCKTJXjbxqTTJUVcdcpBBDaVqL0UA2qtbtlqy2SL4FHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
ادعای اسکای اسپورت: وینیسیوس پس از مذاکرات با سران رئال مادرید دراین‌تیم ماندنی شده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/27161" target="_blank">📅 20:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27160">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vi9-opxWzFt8MvrW2qXkyaJbowNDNxYl_acxZbmospH_dUK0_Cf5IXLndOgIxJh7ABiEjTpepUvsyTKk-2_-Ur3o_xrB0m5XPYmjNM-qlrnPAPhSVO2X8xOMI3YYb69QUN58HD08T39vX6NLirkLtU2FbhHI2gFfHxrApLF5Tg9aQ9n5s3Ndoys1sWS9fbErP8JmdfidhnP0cgC_aI6-p28iSqsTkw2iv-zX48BSbwc1C4krlb65DC6p2xIKWeNTU2J7AA-WeWLsJMIOJkOR0bzRciCAS4DEKmOCQvZ2g3NdHUO-wXfJU7eH_appTcM4rPQbUV-tDe9eulVyQ9uqGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
باشگاه تزابزون اسپور ترکیه با انتشار این ویدیو از محمد صلاح خریدجدید خود رسما رونمایی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/27160" target="_blank">📅 19:53 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27159">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JE55jTj-vdm-D4f0iztcpvs_uk9i71aGdO4L9JABjrpWniWuTI6ClG8Zk-jnXW9tjyzGGAb8nh2GM_kFzGLNI-Sl6KzK5MsNvfaByTW-ur9FnnLapMq-6hAn4FRyg9xEOGg1BmiiOIbR-ujOZsMd_fiTc1MWKMtAvG5SEt6tVlgayg8c47kbRca5C6SSOd4GOABMgo1eh4XszV7F2e199WD8iN2Q3lorhMnR9kmkgAkoJws6F7pAE3L0VUu3XlY9bmGKhtOs58XUhhJ2ibPsi8WcCfv1Clr_ae3XUhRxe9h-9GdOI0fiJ3eNQnID-kghRVw-QTS6bK5oXhovBHXW-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بااعلام باشگاه استقلال؛ رامین رضاییان ستاره 36 ساله آبی‌ ها بعد از 1.5 فصل حضور در این تیم جداشد. مقصدبعدی او بزودی مشخص خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/persiana_Soccer/27159" target="_blank">📅 19:13 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27158">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3Kzrt1fcG2ga0HWsj74JAvO8hxLAvKRY8thA4o9Oj5v4VBFrBJ_Ju-EyFUjF7SfzJiwe8REWLC598fsuOsHco7G6J3oSVfMiRtxeJVep4_hIAjhp4pbQBCbjckU96VYhQPjImGmyFbl11BvgobDWQ3jdctzv2XzihMNbksnH9v1WpSaGnjKnvF1tEsIbzD3NSikJ_Bg5HAEVDLmp5Sh5EfewJnIMG-lDaek8TuxkuY2yylxEfQvvxaSy9-SHuDgzCkTZK7NlHBDvlnE3ZbvPAYKJO0dLQ8TjWaa3uM_VZF6kZSTY_zA1UK79Re2aQKOPGUDo68V9zeEXdFlGcrm2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ امید عالیشاه کاپیتان سابق پرسپولیس باعقدقراردادی 1+1 ساله رسما به تیم گلگهر سیرجان پیوست و شاگرد سید مهدی رحمتی در این تیم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 74K · <a href="https://t.me/persiana_Soccer/27158" target="_blank">📅 18:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27157">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wb9aoGurehpwJEnk998zKko161JaYnMaWhUC5o6M7aozti6lv0XaX5ILPWLXQ6qKMyLX64Pb7bQSE3XsIH4RyjtAVHrgkuPXXtTfG8RftFARevivDEFAjYQhMW_yRx6r5Y80dUSWvML9OgqknuXwht3YO4qXXcINZk93jNT9RHaLsh7GoD1rH93PIR37nYYQnLBmihkJn_-QiFYXQgW93_jkAAvMJ7G1RebAOJXr2_8hNRJ0DfMxkHyd6acfv6wHVbxUkCN9iIlMOFBr8tQVNsCabQl4bBWyfCvdZcodTLUt0TRc4xJ6W0Ihr8mOhtfEjlE8THQQrcn2K5suNbuiUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇧🇷
خوزه فلیکس دیاز: مدیر ورزشی آرسنال به اعضای این تیم قول داده کارهای انتقال وینیسیوس جونیور به این تیم در حال نهایی شدن است و این بازیکن فصل بعد قطعا در آرسنال خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/27157" target="_blank">📅 18:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27156">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ID1Ypr9UlizEmV5Zbe1H6Oj2W0xg3kQfnTYaBy_iN4edYMhh0eqMbubFY4xTNdxwN28Nlu9JKqEm7IXDa9-Zb0CetujGAk7-nvNo__Jj7_jzNAVVCXZnzpLwig8KTiTzwEeEkHxsDn78L2fdncajI1oDE9a6osCtPv3e9gumsoI20FitGOr7XJrt1KoXhLJQ5qER0G17LII3_5Q5zOassRBM5tKNUtDyx9oMtPAxNPUtwHHc-sIrvHF0TJdHeBSgpYHB8O_b93OpVnECC75onjKXNojwcdszyxU45wNTIHAx6clQhhgPHKmlOJDWMbXMLvuIFjv07j91kPv0zEt8wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
بعد از کش‌وقوس‌های فراوان؛ امید عالیشاه برای عقد قراردادی دو ساله با تیم گل گهر سیرجان با مدیریت این باشگاه به توافق نهایی رسید و بزودی از او رونمایی خواهندکرد. بعد از اخباری و گودرزی این سومین خرید گل‌گهری‌ها بود که سید مهدی رحمتی شخصا با بازیکن مدنظرش…</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/27156" target="_blank">📅 17:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27155">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LDdw-Jp8yWiQrxS2B6IjZCGFWvJs2HZctdRvj4NZ6j47xiyCv19RbgGNCRyXH0UxUkWTq3Ep_8IJtQrd6NU081GPgrpf86fyR5k1KZrtl6-PHGbOxtkJ75nG5Q6S6HVQcEjGi03XcTB-ZTmkYufFMxaQ-8YXgQdSt0ojHbs0Lpqfckpd8qBGg6rIKNxBBvyu33EKooDgAcTZXz4OgeoW_v7EUqI6uaJ5WMVjIyM2eUf5nbCneAkg3fvNvdVAdaSRnkJqC4ekWrkLY3fV4oUZ88p4xLNr4CRZ8ejpxUOgeCS-O1DQQFyo_yx45ByLwD0KRMIcgN70N-3-0xFhl_u-lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق‌شنیده‌های رسانه پرشیانا؛ امیر هوشنگ سعادتی مدیربرنامه‌های رامین‌رضاییان این بازیکن رو به مدیریت باشگاه سپاهان پیشنهاد داده و مدیرعامل طلایی پوشان اعلام کرده در صورت موافقت محرم نوید کیا آماده عقد قرارداد با این بازیکن هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/27155" target="_blank">📅 17:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27154">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gfaij5YwW8IUf1a_omY5qPe_KCAGtiToQxxhtbypsLlgee-S22ySYwl8gIOVCAxF5nDg5_SeMp7gXwALezkcI-TwHSJ0WZmqU_6Ea8Dj2gvDPEHQoHugYyJXBAxQ1vpyPc6NDrhQ8iT4KWGxgYeDALCj2Ok9s65ELWpvwE1N34yAl6UFzABlGsmAkI0s1mR0QUBRcsif01ls9vZIwXD05EETCFrVmYmybbtjZ4LrL4NGTcXTUE191blyykKVhvyYDzktQxqpBsQClZOkF_t1zimh91hQOCAnbibCf1DVQ25EnX_ErEiX0kJSQNLXoSaopO0SZel4Mes5baYMoeE08w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
مدیررسانه‌ای‌باشگاه‌ماخاچ‌قلعه: ایرانی‌ها با کامنت‌های پرشماری‌که در اینستاگرام برامون داشتند حقیقتا دهنمون رو سرویس کردند‌. هر باشگاهی که با ما به توافق‌مالی برسد و حسین نژاد نیز راضی به این انتقال شود این بازیکن رو به اون باشگاه میفروشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/27154" target="_blank">📅 17:23 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27153">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b7185f121.mp4?token=DRzGxGgSgvhqKp5ikBf1IRAazEygMwr2Wia5u3j5se8G7codFkTF3oHIaQM2-MdDMfLicZsAeDB_O1x3SIWj94NvZvI74IpfJzwG8yEdi-fsOlMyeCwMj1KJxaVA3ftqj_hs95qQiypt3jF14_DAV4s2rM3h23STY8uCaxJFDhokCxMvK-jY91qkJQ18mJ4eghZAAZzRlmjAJqSFICBUhOmoNoo2HKBdE3YwLcrzyks8GP3MF9F9ap30vVsdgB2pud_9u8Xd7NmJuN5RJnaNDH_cwlcqFbwZxOXEpaReMCuJwu6b13Hm9_ouJNK6zR00V7ixb00cg0v74ND09Wou_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b7185f121.mp4?token=DRzGxGgSgvhqKp5ikBf1IRAazEygMwr2Wia5u3j5se8G7codFkTF3oHIaQM2-MdDMfLicZsAeDB_O1x3SIWj94NvZvI74IpfJzwG8yEdi-fsOlMyeCwMj1KJxaVA3ftqj_hs95qQiypt3jF14_DAV4s2rM3h23STY8uCaxJFDhokCxMvK-jY91qkJQ18mJ4eghZAAZzRlmjAJqSFICBUhOmoNoo2HKBdE3YwLcrzyks8GP3MF9F9ap30vVsdgB2pud_9u8Xd7NmJuN5RJnaNDH_cwlcqFbwZxOXEpaReMCuJwu6b13Hm9_ouJNK6zR00V7ixb00cg0v74ND09Wou_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
نتیجه‌دو دیداردوستانه‌امروز درتور پیش فصل؛ توقف شاگردان‌آموریم مقابل‌افعی‌ها و پیروزی راحت سیتیزن‌هامقابل‌کره‌ای‌ها در دوران پسا پپ گواردیولا!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/27153" target="_blank">📅 17:04 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27152">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KEptYx6vIc2KNC8ad01NOPOT0sCkisLtKcrb8v0Hsr1lHND7f3QK7inpduLs_qdFkyTh9Syg0RJX1NhvzVxZibq15F6LfmipCbVyeXK4m4jOL0Yjs6uQKNyzjst5MEkDwkgmw1tEsJ1nurhGboK4lm7784xdObjGWiRVNH79GyIUCADbkg6ttj7U_Yw5Sq0AEF4uok9g-FTjvvwaxlFK7-Huu18LIXevfGVuwUQ4e-RFqljuQP0g91cU-QEFO-KIpu31JrtWxpPFKAUxB_LpnT136gaNcJT-DeCWMFjq7WXl9Z4_wvxA74-KmGA5f7Gn3MPKuZN_HZZNdVUFAVTdxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌امروز؛ازدربی‌دوستانه دلامادونینا تا دوئل شاگردان ژابی و اسپالتی در کشور هنگ کنگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/27152" target="_blank">📅 16:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27151">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anNa7mpyBdnuV4zqlU3w69MNf8rcvekAPD2Kb8ke7JCFM9KSXcxrrjFYQubDaGVSKkEPryXgsmTDdftYHYROfEXvEA2S5eL-yeQE4Z33cuJsayvJKksgpfqk1WIC5e3tHXfo3plaXZTc0jRgvTQ97HyxRjBsOeMXRit1Y8LcKRUbpJtfUa1wEuajRtPbjh02T_9UxJ_kYkkseuH8SJmEOIm15_w5m9YtZXn1kdyVvvgO3JsqIeDh_nGWMHCD35PVzjuhF2YsLVJEuWbpBkx41JluEa4XrkLIeFIJnHE7FEPHQJFfX4v0S9l12_82GhbEdGdcETsNN_k85zajvBJYbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇪🇸
#تکمیلی؛ امروز سرنوشت وینیسیوس جونیور در رئال‌مادرید و پرونده انتقال خولیان آلوارز به‌بارسلونا تاحدود خیلی زیادی مشخص خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/27151" target="_blank">📅 16:49 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27150">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0d917f67b.mp4?token=MSZj7ZO5jDrfwkSkOMMZlwcedPFNNfAbJJeyDeAynB4e04FXtciR5ETGkYeCxEms_OStJQz1c3rTOsTQx_GQAjz-Ps7NFlAwenMWrhq68c5oOfbMGYrJxJfpLZffnU1ASBzVXKKKLmqY1-diipY6VzgeedySG0dY8KnAE_fonmlGHmZ_AX7Xgt2nEHBMs6gYmN5Uq5KLyklaOrqO-vZ6HZiHPpBGwGv0dbl4lCTtdyENOw5eDjIEU1oahEumvTqZBk1xF6zwb0gFJ57At8bB4ASbqG2y79wsP__OgzO0quadHlRTwGlBRQnk-A23xwKlIGmhQX2dBNL5aeEOOUxdyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0d917f67b.mp4?token=MSZj7ZO5jDrfwkSkOMMZlwcedPFNNfAbJJeyDeAynB4e04FXtciR5ETGkYeCxEms_OStJQz1c3rTOsTQx_GQAjz-Ps7NFlAwenMWrhq68c5oOfbMGYrJxJfpLZffnU1ASBzVXKKKLmqY1-diipY6VzgeedySG0dY8KnAE_fonmlGHmZ_AX7Xgt2nEHBMs6gYmN5Uq5KLyklaOrqO-vZ6HZiHPpBGwGv0dbl4lCTtdyENOw5eDjIEU1oahEumvTqZBk1xF6zwb0gFJ57At8bB4ASbqG2y79wsP__OgzO0quadHlRTwGlBRQnk-A23xwKlIGmhQX2dBNL5aeEOOUxdyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
🔥
فقط و فقط ۱۱ روز تا شروع بهترین لیگ دنیا و رقابت‌جذاب تارتتا و سهرابیولا مونده؛ برنامه دیدارهای هفته اول رقابتای لیگ برتر خلیج فارس!
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/27150" target="_blank">📅 16:29 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27149">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OvSdRB-nBMfQnyyR3a2WXy28CnDRxc_nBpqRJ21mMDVMTiX8LzDKroKbXSTf0q8yHYPoX4tNhcPo0EjsvY9qVPtGQo7lsSR3uy19rPmvd-lWuqJSBkGPL3F7LMJEey4BvDgmoIUkYqcwlMpuiTo8cGmU1ssNCdoaRNg7rU8vzK8c0TEHt-7-AursB_jqw0ibcz_wsMnuVCU9rs6yeiMi0lTggrMlLjbhTzOZ0VJbdnVZCN9VmF_aQlUBr7VO76WETY53HsOvCEarY_xG2q0Rj76Y_cmFEnd2L9_JSM416o24WoK9RaQAMeWOTHLeGoPkpvAjmALvlqX4MFTd7uubrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
چه خبرهه زیر این پست محمد جواد حسین نژاد؛ استقلالی‌ها میگن بیا استقلال، پرسپولیسی‌ ها میگن بیا باشگاه‌ پرسپولیس... اون‌ ویدیو هم فن پیج‌هاش ساختند. انصافا شاه ماهی نقل و انتقالاته. هر تیمی بگیردش برد بزرگی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/27149" target="_blank">📅 16:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27148">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/315f795088.mp4?token=OsaL29hltnvYm65sOYvj3kCyNhlkK16kEu4Nt7wWDKZbo9kixAQloYcrq8Zv_9i0v7d2jbCaLDNJ6G7RvuHCCb-CMY_3_x76bQM3Q5BWNtwZLhMXliZAdt41e3ukYrKE7iJ8KSla9TZQQI7egD1PdNsKuZGXGG6rycIEtjpkQQHgF8vfkhjFUCJ1cLYvfrRG6mvkzOOY7woaCRCYWvnUcJRTY2yRHvSViv4nXGBHD37uQpcmc0WWdQ-OCaymxFyOneg5y-kIjTZTYdhfQhScLoWUwvltnjmr71fA-h0MN_buY_1QFnl0cj-LAZnDRkJ-bOb_QLFag_zXSg1B2Gr0bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/315f795088.mp4?token=OsaL29hltnvYm65sOYvj3kCyNhlkK16kEu4Nt7wWDKZbo9kixAQloYcrq8Zv_9i0v7d2jbCaLDNJ6G7RvuHCCb-CMY_3_x76bQM3Q5BWNtwZLhMXliZAdt41e3ukYrKE7iJ8KSla9TZQQI7egD1PdNsKuZGXGG6rycIEtjpkQQHgF8vfkhjFUCJ1cLYvfrRG6mvkzOOY7woaCRCYWvnUcJRTY2yRHvSViv4nXGBHD37uQpcmc0WWdQ-OCaymxFyOneg5y-kIjTZTYdhfQhScLoWUwvltnjmr71fA-h0MN_buY_1QFnl0cj-LAZnDRkJ-bOb_QLFag_zXSg1B2Gr0bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
امید عالیشاه کاپیتان سابق پرسپولیس بعد از یه‌ دور مذاکره با سپاهان، فولاد و ذوب آهن حالا با مدیران صنعت‌نفت آبادان نیز درحال مذاکره هست و هر تیمی‌ رقم بالاتری پیشنهاد بدهد قرارداد میبنده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/27148" target="_blank">📅 16:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27147">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aee60bdfdc.mp4?token=Rp56JqGTI9L2BCThyxzljasrKZBeHXE4ySWt7s_2cSw144o8si7w88JZlYKKRf7_TM1rl5Y1jc7BQwqwvmD0g5e61ddQ-g6GRYU6EZJgl0qNYD5n_PKZ1dTgRiDz37CQuKlYH2EKmaKgPQ_G5vXxrGrFVetWkAOft7ixtGgqukxIphDKikRtjHMZR3vgO5lyim7ID1oox6wmRu1vaeED18fXHg_pgeVfm9BZeprhJbiGjSBCvafdRHHxaUMNeDFo9r9NeCrp0oDlMFN8sVBViKT3i6h1X1H4WSxxQInZpHuj6HHBEFfydfhDOnTjvY-8z80xUJVQOtsiSB_-qCeOhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aee60bdfdc.mp4?token=Rp56JqGTI9L2BCThyxzljasrKZBeHXE4ySWt7s_2cSw144o8si7w88JZlYKKRf7_TM1rl5Y1jc7BQwqwvmD0g5e61ddQ-g6GRYU6EZJgl0qNYD5n_PKZ1dTgRiDz37CQuKlYH2EKmaKgPQ_G5vXxrGrFVetWkAOft7ixtGgqukxIphDKikRtjHMZR3vgO5lyim7ID1oox6wmRu1vaeED18fXHg_pgeVfm9BZeprhJbiGjSBCvafdRHHxaUMNeDFo9r9NeCrp0oDlMFN8sVBViKT3i6h1X1H4WSxxQInZpHuj6HHBEFfydfhDOnTjvY-8z80xUJVQOtsiSB_-qCeOhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
توضیحاتی‌جالب‌درباره‌پست‌جدید کریستیانو رونالدو در کنار ماشین های لوکس و گرانقیمت خود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/27147" target="_blank">📅 15:46 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27146">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j1Ct_AVszYeThyuqyGBz1oVicC48mlWm1edJTfPbdIuOuFjoQQCfR5tSLHqgJcnEE6OXeXgqHbMtSC14-gtgDaMnWIq71Qc-TH0DV83qhup0DFibgHvzCS-XEMVNSCy3P41t82iESR31GwGmrnJAIxfHAFNXTZpxAJTyZ1w2zFusQmyt0aDZvGxCOiiXWwqopD5komdr6RhnKHlDQFMlt1tVmxVhZNSTgSEicxYaCpTRab7fw7LvMTHMBzDZOiskOlfBEi41KqMflg8YhR5z-l5rkG9uOeIKlGR8lMbtznv8vtpEQiURCmYRy6ypZLcfUv7W9TpAUXCwrjmCUce3UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
فرشیدباقری بادریافت14میلیاردتومان از پیکان قرار دادش رو با خودروسازان یه ساله تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/27146" target="_blank">📅 14:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27145">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6WLRFeQKwJeW-1K_Bug3_nhftta3STrf4br50LCguE8tyVHwfj_4vLSrFc63SOmjgmnQNwd80UbxX1cM8kBjROwemjxJw7a0_XnR2dnO1igrdsD0RbnFReBG50f8of7C1J89gL-M80TUSCpCLgDfUkdrZ4m7q9hQr1OHdGFcJznB1h8s6ZlqtslSrPnQNBcUjqpo1KGyG4RPPPInOfoTvVaCvyfxBFmIxHLV7jXCUD5CDCUTqfPgj_f8-y6Z46QX3PMuMNXsJVd1gnXgY248EDItRuM2Jo-8Xg8_ZmPYBSoCAUjjXHIznD4VyZJUyUWlAbO8o5aEpmX8YuvSQxYig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق‌شنیده‌های رسانه پرشیانا؛
امیر هوشنگ سعادتی مدیربرنامه‌های رامین‌رضاییان این بازیکن رو به مدیریت باشگاه سپاهان پیشنهاد داده و مدیرعامل طلایی پوشان اعلام کرده در صورت موافقت محرم نوید کیا آماده عقد قرارداد با این بازیکن هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/27145" target="_blank">📅 14:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27144">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09ea3c3b07.mp4?token=Snsr9w9hMdlMEsjBH-WvjMUm6FsJMHQfI7LtCRTtFMc829DZtx7AiYK_ygqJfJR-yErJRALRoED8yRe4Gk-vL6H9wWMls4xwV12JKTeemW5OpEIrzCNwv33Dp_Es6Jwoh4IsFu69iQ3ByJ1yydXCOwawfqIzfvJf2fffa4HTZx9-IsblqDDIQQi1wE-lWhwGWXFLW3Rn-QJanbrrmLxpxUX2AkC4Ss0zn0qGPOU8VgcdfFaE1z5JOOwURKUhgpcZOnFbl0hZBlHoyHwhVz5PxRPq8YyDsN1Mhqwbe-b8R3I5FycVzNw0rr_6W4cEx4EXERIz3cez9q6pqBKOTxBBOi8lHl72DDcN8n8TVNIu5YenrycLHZ99_Y8zEDK0LNukmCyKi5yDD3q6xYTnBIfKesFal7j2baZRrGLyw90PwKZ9pifzerlznMA7m4QBbLb0_ShyVzW4W2wT5_JeG2dzDd8tCD5T6Q65CMgfJDlWktaw3b-Q1IbNliw4ywy8Vu16gFleQtFa4IHLA1CCdFjhjJd37c9AJObt7F_lTk7D6Zu1hzQ1vGbGmRB7ZFvWdRwp6LFLT2lacUsqWDkChRZn7GPdybt1ghAslsxpD5826Xt2u5X0vvXPxglwxMJ7zKqw3xoTUcm0jVkwoiyK8vyCN1UsaZW0P0ijI6rTwib95Dc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09ea3c3b07.mp4?token=Snsr9w9hMdlMEsjBH-WvjMUm6FsJMHQfI7LtCRTtFMc829DZtx7AiYK_ygqJfJR-yErJRALRoED8yRe4Gk-vL6H9wWMls4xwV12JKTeemW5OpEIrzCNwv33Dp_Es6Jwoh4IsFu69iQ3ByJ1yydXCOwawfqIzfvJf2fffa4HTZx9-IsblqDDIQQi1wE-lWhwGWXFLW3Rn-QJanbrrmLxpxUX2AkC4Ss0zn0qGPOU8VgcdfFaE1z5JOOwURKUhgpcZOnFbl0hZBlHoyHwhVz5PxRPq8YyDsN1Mhqwbe-b8R3I5FycVzNw0rr_6W4cEx4EXERIz3cez9q6pqBKOTxBBOi8lHl72DDcN8n8TVNIu5YenrycLHZ99_Y8zEDK0LNukmCyKi5yDD3q6xYTnBIfKesFal7j2baZRrGLyw90PwKZ9pifzerlznMA7m4QBbLb0_ShyVzW4W2wT5_JeG2dzDd8tCD5T6Q65CMgfJDlWktaw3b-Q1IbNliw4ywy8Vu16gFleQtFa4IHLA1CCdFjhjJd37c9AJObt7F_lTk7D6Zu1hzQ1vGbGmRB7ZFvWdRwp6LFLT2lacUsqWDkChRZn7GPdybt1ghAslsxpD5826Xt2u5X0vvXPxglwxMJ7zKqw3xoTUcm0jVkwoiyK8vyCN1UsaZW0P0ijI6rTwib95Dc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
به‌بهانه جدایی رامین رضاییان از استقلال نگاهی بیندازیم به لحظاتی‌که این بازیکن در این تیم داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/27144" target="_blank">📅 14:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27143">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u0vI7-61j8k9BNHo7inpIiucFeHgdyTF8MaE0UqypojLnSJWT2vrVU_mcmJ2LE9LXyaaN_Jc219DLsBUf9Klc53HOZxiNySsvqttrh8zUM033RiSGondmi8j2WaOZFn7gLGA4o3kZjcwAgCFXls2_vqIwslZOzTHqyjSdfmSOxm4L2a1wqidJyYHFGWxmlMsJiVmACww7VgcQzi6fTwpWcRy_1DYjtgVlMi3TTVfm6DE2J7-y8AJXrXJ1LTqvoRwqxGEd-bDu5lddaabdhB1ztiGblmfjKbUJ61xN2Uc6AGnkBrbcAqapn6Cfo6xikcCcagj9x9gIhUr7i_Y36tt0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بعدازجذب دنی ولبک؛ چلسی ساعتی قبل جردن هندرسون کاپیتان36ساله‌سابق لیورپول رو به خدمت گرفت. حالاجالبه‌بدونیدکه هدف ژابی آلونسو از خرید ولبک و هندرسون‌بحث‌فنی نیست فقط‌وفقط میخواد تجربه تیمش رو بالا ببره چیزی که توی تیم خیلی کم وجود داره و رختکن تیمش یه رهبر…</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/27143" target="_blank">📅 14:09 · 14 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
