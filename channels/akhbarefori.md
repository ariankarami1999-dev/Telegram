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
<img src="https://cdn4.telesco.pe/file/XGPjN6iDDvlF36BxpIbKJCAM1I_B4lkDcU8sD0Rxpo6ta4_3BU8iZQegmZvgsTK0EVBP2Gt6dgD4ouxlRPrZugqZNsluAVjbaPorTawDZpPGT43efdiQLXGnrCTMm9V9hoXkruQY0_3UUWXjgz3cmm67fGIKyjKnHreVVx3XfPnc4-hQGYS_IttutZ2A3Q6w6kx-LxV05vg42CaHhdsdpVL1Ok2MluVEFwDCa-wMJufGXSBWi4qTPWy4e5rFYRh6HkUlyFXBKeBb92c9TQbSTUcxnqbzdHi6QczU21GZ2CwSqYjhfyW1SJP3yPje1FhBmyDOUqd7dSwBHCV58jV7FQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.21M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-19 13:59:26</div>
<hr>

<div class="tg-post" id="msg-657619">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
سقوط بالگرد نظامی آمریکا در نزدیکی تنگۀ هرمز
🔹
طبق گزارش نیویورک تایمز، یک بالگرد آپاچی ارتش آمریکا در نزدیکی تنگه هرمز سقوط کرد اما هر دو خدمه آن به سلامت به محل امن منتقل شدند./ فارس
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20 · <a href="https://t.me/akhbarefori/657619" target="_blank">📅 13:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657617">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pIqpqE4fsWCdjypQHWWCfcRG9X-1WiQI3RGNNbdBOvbvfmGfozDAGOWgAiwKqlyzKVNyUfAhWWdEWPM_lDl39iiLWjHV6nxozQolnQk4wfrCkOn7paQocBTukmZvWzyl5omdm86W4HgsiPC65GCujuN96je3Ri8v0AWiRJ6Wn2RWYAHHvVw2jOCG3JFJtMUi0c_car1kPsAqzuV2njFVCBSfkPnNehZoOSygDtNYggno7ghp5gJXXRvJZHTOxpGfuu54XSOhlZj5Qbaj52AyymRTjmgouuAxDugIBdGK8iqCY3Tf1IY5xsBgTmFVo5aTPeoiH1h1fZg-8GK_D6TwqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جدول مسابقات هفته اول مرحله گروهی جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/akhbarefori/657617" target="_blank">📅 13:42 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657616">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
زیاده‌گویی ترامپ درباره ایران: اگر برویم و بمباران کنیم، اگر بخواهیم خیلی آسان می‌توانیم این کار را انجام دهیم
🔹
اما تنگه برای ماه‌ها باز نخواهد بود. اگر بمباران کنیم، می‌دانید، افراد زیادی کشته خواهند شد. چه کسی می‌خواهد این کار را بکند؟ من نمی‌خواهم.
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/akhbarefori/657616" target="_blank">📅 13:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657615">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qy6-ThwUF6iI1PUEQvgPx1GIZk1UAk2Zn6YLs55H7_ueo5E8_MemODN3TG_P_6gHmDUQcZI5QrhrfypkG4qbkrwBaQ6TGRIBrGY0O-HRezkbmMYLsMEHYoYykaT9sgx-QEYQpoyZEXfmGztbpqsCXpxVFkYo1UgZf5CYLBI3vwV9Ej43HW85LUy8NcDSr94326wOgVYcrUeF2CyghlqmrJIH0r2TimcFB-16nfJ2VmWYf9MD42Gdv9RmruVFAJZIxcGoNBvGH-2uquk1-oSBVan7Y1CuSM_gJl8rKlc8gzdT5mVuUGAx-FPrK2_lFzJGKYlGChAYv35hyhLf1aFdGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بقائی به نخست‌وزیر آلبانی: آرام باشید و به درک و شعور مردم خود احترام بگذارید
سخنگوی وزارت خارجه در واکنش به اتهام‌زنی تکراری نخست‌وزیر آلبانی علیه ایران:
🔹
آرام باشید آقای نخست‌وزیر؛ این شما بودید که شروع کردید، پس پیامدهایش را هم بپذیرید.
🔹
بهتر است برای درک و شعور مردم خود به‌عنوان ملتی بافرهنگ و دارای تاریخ غنی احترام قائل شوید؛ مردمی که می‌توانند راست را از ناراست تشخیص دهند.
🔹
اگر می‌خواهید حاکمیت ملی خود را بفروشید به خودتان مربوط است، اما هنگام مواجهه با خشم افکار عمومی برای فرار از پاسخگویی دیگران را متهم نکنید و به شعارهای معترضان در خیابان‌ها مانند «با فساد مخالفیم»، «خواستار عدالتیم» و «راما برو» توجه کنید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/akhbarefori/657615" target="_blank">📅 13:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657614">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
پروازهای فرودگاه امام(ره) طبق برنامه انجام می‌شود
مدیر روابط عمومی فرودگاه امام خمینی(ره):
🔹
با صدور اطلاعیه هوانوردی توسط سازمان هواپیمایی کشور در شب گذشته پروازها در فرودگاه امام(ره) به حالت عادی بازگشت و طبق برنامه انجام می‌شود.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/657614" target="_blank">📅 13:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657613">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XIMunG7UH--pLa51_AKBF99YfAL-AsxpMAFVCrkpvINsTxU2asC9E6y6gpH4QxmDme-zoS8YQRtP_V2VjLxnlVZVOzGM-l17WfxuueRss76860cOSxHk2Dd-Gq_HA_GNhNjQKMbTlGmXTAFTNlvlguL76XMhhn7VZQK4wnBoY0BX-7YnnDTr3yqaCghXZaoHy4DHxGOPjrhxMOFSxzp6v4GbEhgy4_HI1Qc49IEDjLE337RzHr0VKc7NQrGgz_vGe8FJT98XqNmYSDRnBJimyiun64zsimXrnE5oEfFiyCXv3RCQ5hc8EV4V4CMk309I-eIM_k7BITqJvS9-K-cdOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عبدالله گنجی: روایت منتشرشده دربارهٔ جراحت پای رهبر انقلاب غیر واقعی است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/657613" target="_blank">📅 13:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657612">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f95b7e84d.mp4?token=nGq5QnJ9be_RacKYo-cKdw1kw3bVKgcF8YQ4QgkOX8_RfgtWa5W5DcOU2gV6ngJzKniJKFkd6J0sLYCXNZ2SaRpDF--hurb40ZvsXQoLgFJbGktXyR5cEieQybEiSasxAyNKgSqrUVu1-zElDlnSYlZkWs9atVJsD5qjlYezPx9XKW7W-UE18kZeHcnrhVBAp0lAN-8GdR0u2GDIkcvNOsmvU7COixkemAaCnguq6FxqQLdV-H-jUXlOEnOS3HJCj05NZ9iAsL7l7W7UVdGcIpkOuu3cYmFJi3C0G0XAi7gRMZ2FIVvZlUTGBmULTfymIJWGaza0jxV2wIyCDnK0HIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f95b7e84d.mp4?token=nGq5QnJ9be_RacKYo-cKdw1kw3bVKgcF8YQ4QgkOX8_RfgtWa5W5DcOU2gV6ngJzKniJKFkd6J0sLYCXNZ2SaRpDF--hurb40ZvsXQoLgFJbGktXyR5cEieQybEiSasxAyNKgSqrUVu1-zElDlnSYlZkWs9atVJsD5qjlYezPx9XKW7W-UE18kZeHcnrhVBAp0lAN-8GdR0u2GDIkcvNOsmvU7COixkemAaCnguq6FxqQLdV-H-jUXlOEnOS3HJCj05NZ9iAsL7l7W7UVdGcIpkOuu3cYmFJi3C0G0XAi7gRMZ2FIVvZlUTGBmULTfymIJWGaza0jxV2wIyCDnK0HIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار مرگبار خودروی بمب‌گذاری شده در مسکو
🔹
همزمان با ادامه جنگ روسیه و اوکراین، مقامات روس اعلام کردند که یک نفر بر اثر انفجار خودروی بمب‌گذاری شده در حومه شرقی مسکو کشته شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/657612" target="_blank">📅 13:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657611">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLf9FzWqqqTw-HWEJ02qDl_xfCMQ2naJof59m3cOzZs5xupNBh7mgBV5zbEA4oexQ26PjVazP5eVZkO3kdH78euu55LsKCvo90YWEyhnlwFH6mq-ANOX3bwdghGRC5nw8tDLq6vLXl62VLxixVYvtlCjZO92RIUcMMwSTUF3Ov-wp8s4rz0yHVXusNII1VsomN-AShKJjqHY7xSnlB6RFsSISH7FPcv_USgf3-F4oCBks-HfsB1-D67jVZqMiqUKtFeOQ0YgPOHD6EbP70eBUyRYqKkrHZWfXslA01Oqd0IAiCeSnbARmEqkKyaO62UmZryuSy_MLkYUhZF9SXQ36Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت برنت به ۹۲.۱۹ دلار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/657611" target="_blank">📅 13:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657609">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
پروازهای فرودگاه شهید هاشمی‌نژاد مشهد به روال عادی بازگشت
مدیر روابط عمومی فرودگاه بین‌المللی شهید هاشمی‌نژاد مشهد:
🔹
با فراهم شدن شرایط ایمن و انجام هماهنگی‌های لازم با نهادهای ذی‌ربط، محدودیت‌های پروازی رفع شده و فعالیت‌های هوانوردی در فرودگاه بین‌المللی شهید هاشمی‌نژاد مشهد طبق برنامه به روال عادی بازگشته است.
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/657609" target="_blank">📅 13:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657608">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
تصاویر اولیه از کشتی مورد هدف قرار گرفته
🔹
بر اساس اعلام اتحادیه ملوانان فوروارد هند، تعدادی از خدمه این کشتی را شهروندان هندی تشکیل می‌دهند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/657608" target="_blank">📅 12:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657607">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tmOjuzZ1uMgtbBnuanDeZ1ljHZN3ApPbV16z1Ib1rMey4lXrRyzPUZOw4e0A6grvZ_cD5SIMiKs2HuJlT0N58mlbMHQC6_oQCkXy5mv8k6gIBaChFBrC7iEyDFr7WMOOuwC8Ub56lKMZdGfa9BHasxaYEG_3_hoAn59E_dq5tRE822afG0-SrRUAH2Mn6q7eRGzXhQlkhL22aQl-0LzRNnQc6FUsUFm7VZWPDOeSeI5FJw7axoG76ENJq8-0qw7qbGL1l6RTkLnIKHPVfkC4G3ukubR1xg4LFlNdfSdtX7_atU_I6MTZqOQuv8SbyNBt-tOsefLNCmiamRHHxV6MQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حقیقت پشت اعداد؛ چگونه آمار و نقل‌قول‌های جعلی را شناسایی کنیم؟ #آگاهی_رسانه‌ای
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/657607" target="_blank">📅 12:48 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657606">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
یوتیوب رفع فیلتر می‌شود
مصطفی پوردهقان، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
وزیر ارتباطات در کمیسیون قول دادند که فضا را به شرایط عادی برگردانند و بعد از رفع فیلتر واتساپ، رفع فیلتر یوتیوب هم در دستور کار بود. منتظر هستیم گزارش وزیر را در یکشنبه آینده داشته باشیم که به چه نحوی پیش می‌رود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/657606" target="_blank">📅 12:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657605">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fm2noI5aoECLi4K8wv-EdiK2EmHtE4o6Ku_eH2h__5uUp5e5bEPyGd1VM7mEqAtuH7oc6eWST45EretFv_g_wOsu9A8xj-WDXshlTSdxL7tB1NPf6RejaIOdjADPWOKjWGO98f3DuViNx3lkP6QZeYqsZvLbU0ikc6CLUhu2tda92rugKBfCypThl9lX2B58xw1F5gmGjUp0jyLhrMbgIQsrpcgseV-fdy3sNysvFcqE1Cmiwgn3Tr--A7Q7PvxsivGiNKd50DeoKZqNK4tkBTBtbzmVVN3Ke4mwbRRgxYtBn4U37AJaYn42gvGJSG29sm_UWNncpD1eBKIUFJFwPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شهادت دو تن از رزمندگان پدافند هوایی ارتش در دفاع از آسمان کشور
🔹
شهیدان والامقام «سید بهمن حسینی» و «علیرضا عبیری» از کارکنان نیروی پدافند هوایی ارتش، در جریان مأموریت دفاع از مرزهای هوایی ایران و مقابله با تجاوز رژیم صهیونیستی دیروز به فیض شهادت رسیدند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/657605" target="_blank">📅 12:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657604">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LsdGNJ58JzRT7NLeTSVzJJo3tq61Rx1C-VGJEmJG4W7pqNZLP9jQb5z4Q7mj4elap0r4L--eW9GzmU4UG6U4lHyGYz1Kq4FwYGnVoYZ4Gf6GSbq4P74r5XtouSaH8dRe7TqwudxaJaEum_VHSlekP90mG9z0BrmAYOhIpj596WMx5pCy-lfkSntndxNa8vH4Wtbq_9dQOrO_mLkLh2QaOJyPiStfQzUxo06rMjKGOI3bOOfOY0rLMLzGrmOI5HGojnarypgtS1J3b5mJ-GUzlIISrzXiSM7CUYY-inQHHlyh4HFESDtxMI3gH-0rPOA47vEugCzBavRry1vV9A-d9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بورس با جهش سه‌رقمی ۴.۵ میلیونی شد
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۱۱۵ هزار واحدی به ۴ میلیون و ۵۴۱ هزار واحد رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/657604" target="_blank">📅 12:34 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657603">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45a9998b2c.mp4?token=CJA85mnm3X4-UPEz2M7tVvx-WjGwPt2xVASCHjSGbyfxQP3tnI3SJbCchcMSRunIBaIr33ck2yxW1un1EHS3-rVWZrzGA_6VTbPLJc2lCCLoz8dH8AqeeWJdeMDtF47ghEYr_L7Nio8bbaIa_wI1zA7QoknRSL95j7crFVU47q5O-bVUyF-OYK3uqCDlfmxuPj2BsnK2Cwvg19MMIW4DD59BOr1QCiric4x5MscBJv2m6tUG1hYTUxUtdHLgIRuwOwH9SvPyHmr0V27uUaKSMaksfJy3Kh7hCqsvxbY5AOMJ_Rga-iTkIr6kRL_fTUNgbH_Of1ZlxLsdh3C0wefHxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45a9998b2c.mp4?token=CJA85mnm3X4-UPEz2M7tVvx-WjGwPt2xVASCHjSGbyfxQP3tnI3SJbCchcMSRunIBaIr33ck2yxW1un1EHS3-rVWZrzGA_6VTbPLJc2lCCLoz8dH8AqeeWJdeMDtF47ghEYr_L7Nio8bbaIa_wI1zA7QoknRSL95j7crFVU47q5O-bVUyF-OYK3uqCDlfmxuPj2BsnK2Cwvg19MMIW4DD59BOr1QCiric4x5MscBJv2m6tUG1hYTUxUtdHLgIRuwOwH9SvPyHmr0V27uUaKSMaksfJy3Kh7hCqsvxbY5AOMJ_Rga-iTkIr6kRL_fTUNgbH_Of1ZlxLsdh3C0wefHxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیوی دیدنی تیم ملی نروژ برای جام‌جهانی به تقلید از وایکینگ‌ها
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/657603" target="_blank">📅 12:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657602">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
کاهش زمان جلسه محاکمه نتانیاهو
کانال ۱۲ تلویزیون رژیم صهیونیستی:
🔹
دادگاه مرکزی قدس تصمیم گرفته است جلسه محاکمه «بنیامین نتانیاهو»، نخست ‌وزیر این رژیم در پرونده‌های فساد، به جای ساعت ۱۶:۰۰، ساعت ۱۴:۰۰ پایان یابد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/657602" target="_blank">📅 12:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657601">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
اعزام محرمانه چتربازان آمریکا به اسرائیل در اوج جنگ با ایران
ادعای کنت کلیپنستاین، خبرنگار آمریکایی:
🔹
آمریکا در اوج جنگ با ایران بخشی از نیروهای لشکر ۸۲ هوابرد را به‌طور محرمانه به اسرائیل فرستاده است؛ این اقدام با طرح احتمالی تصرف جزیره خارگ و ایجاد منطقه ساحلی در داخل ایران مرتبط بوده است./ فارس
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/657601" target="_blank">📅 12:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657600">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BsUMn0OYlrSUdVTUx1wFxO3gRcGO0onF6drcD4R7AysriQN_3Gtdor8trLEQ201Xiu9iAA6kQcyFTeNOCcNwXqZuHrAi1B9gnNRwYa4C4G4TytTnoElJ_ppC16Pcpu7Hphdn05G7d_iBRvGTPScc7JhzwDAtzAG3G7JcvkRe39pd5uJaI-rEoOpM4-gIASiE_WUWY_broLr1taaVTx3HRogA5F05oTRYwrogqD75t3gcOwpLXkGlp5VVEZn2BT8GKntE-cUuZoyhi7_bU4H4YQG_cKGlKwJRV-Lw-8pxykg857Zs79L3TVfrJR4GP7aUNzDQyb_J42jy_csPvBHUjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازیکنان حاضر در جام جهانی ۲۰۲۶ با سابقه قهرمانی
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/657600" target="_blank">📅 12:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657599">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
تغییر مهم در ثبت‌نام حج ۱۴۰۶؛ تأیید استطاعت جسمی زائران پیش از واریز وجه و ثبت‌نام نهایی
رئیس سازمان حج و زیارت:
🔹
تأیید استطاعت جسمی زائران پیش از واریز وجه، شرط ثبت‌نام نهایی حج ۱۴۰۶ خواهد بود.
🔹
برنامه‌ریزی حج ۱۴۰۶ مطابق زمان‌بندی و دستورالعمل‌های وزارت حج و عمره عربستان انجام خواهد شد .
🔹
فراخوان متقاضیان و اقدامات مقدماتی پیش‌ثبت‌نام حج ۱۴۰۶ از تیرماه آغاز می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/657599" target="_blank">📅 12:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657598">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mt6Eit1Nc4QwaACtSsEAR5vGF814x24z-PMvz3xEf5v8018AUOanVlOcMcThl4azwxiIVIfDeyQ_TNuWa8z9nYtLZvaoyIv5YXRu8xBIV0ws8A4Tc20rsLQvc6Jq5vQgz1zUpynyoDmNCw5r5rXf4_BjzXoxwLqVpEwAM_vob9Lsaw3mPZIPhnH-LMWFOp0TTn4kZlV6C2-XGpzrD5ozw-DN32e-byDG0loSgNFk37bmPu_vkAVRzCS6MwL-nFqMtAMD5qNeRyzyu5YBkxybLJB1CNqtoWRHpLbpwXjG7fXNTHTfZSbYsSa09DLDhBwlr7Mu3v2RP8CAarwGIzdZfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۵ گیگ اینترنت هدیه بدون قرعه‌کشی منتظرته!
🎁
با پیش‌بینی بازی‌های جام جهانی در اپلیکیشن «همراه من»، ۵ گیگ اینترنت رایگان هدیه بگیر؛ به همین راحتی.
اما این فقط شروع بازیه…
با ادامه پیش‌بینی مسابقه‌ها می‌تونی شانس بردن میلیاردها جایزه هیجان‌انگیز دیگه رو هم داشته باشی.
🏆
زمین بازی در «همراه من» منتظر توئه!
⚽️
👇
https://www.mci.ir/-4S0XAJB</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/657598" target="_blank">📅 12:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657596">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S02-06ulBGUSYAowcf9Q7xo4I2fiJGS8L02F0Rpj0j0DEkSdsHY1Ni4A1RuQca1rFJEw92QFg6xdZBXwDuVtZIA9ypfzwQ3bbml-4pydMvWJi1IcjQy-NI3HrFiDfGvVbCjgdPhFsVTEPGxgGEQvjE32y8Z131WJS9RrF1kpy44C0t3IPNUft0tum7YlNIfMhfIJDENm6FGSkkuCik0Jj1lhMJvLejxmzMr97mmun5KtuJd6Kq0ZH3Z4ZyMCkhcqgXyzn0r6ZB7NaIRLVYNwhZ3wA_FilUZmOZEeBQe4wlCW58GYSVEpTbrLpnqW7bfHtdwZIDFtfJHcM1kedLezGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قلعه میران، گلستان
🇮🇷
#ایران_زیبا
#اخبار_گلستان
در فضای مجازی
👇
@akhbaregolestan</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/657596" target="_blank">📅 11:57 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657594">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/757ddf32fc.mp4?token=ABiMFp6i5wgaNq7u0LvoKp5NnSAMkbdSZoq6RPtjotutqcLT3Rpjj-G5jAE8Kvw9nl4IuDzWNZmRGfaDmtHcrRtO4RiwupLZ5OlPs4CCmEx6bNPZgRFTUwejGvHcdzf9QjucCqUQIq1FAaup_Oqk9wWd2d_5bUta1rco-wgvQSZDmLneWS6Ivw8XnQY5fhdgYpnV_U_F0dHT4h9GYI20XdRIVs-_IndCZow59xEyKjZUQDVp5J3z5G8DEaDAeMJWjlgAMPuNNfezxPQuNg3AqmfHCgyqHd76WqzvzndXlHL5G9G7d0VYgdvBM4uBBmwh9OtPVJKJfQrK7A8-8x4AEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/757ddf32fc.mp4?token=ABiMFp6i5wgaNq7u0LvoKp5NnSAMkbdSZoq6RPtjotutqcLT3Rpjj-G5jAE8Kvw9nl4IuDzWNZmRGfaDmtHcrRtO4RiwupLZ5OlPs4CCmEx6bNPZgRFTUwejGvHcdzf9QjucCqUQIq1FAaup_Oqk9wWd2d_5bUta1rco-wgvQSZDmLneWS6Ivw8XnQY5fhdgYpnV_U_F0dHT4h9GYI20XdRIVs-_IndCZow59xEyKjZUQDVp5J3z5G8DEaDAeMJWjlgAMPuNNfezxPQuNg3AqmfHCgyqHd76WqzvzndXlHL5G9G7d0VYgdvBM4uBBmwh9OtPVJKJfQrK7A8-8x4AEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر ارتباطات: ترافیک استارلینک با اینترنت بین‌الملل در مرزها برابری می‌کرد
هاشمی:
🔹
ترافیک اینترنت بین‌الملل قبل از ۴ خرداد با ترافیکی که از مسیر استارلینک از شبکه‌های مرزی خارج می‌شد، برابری می‌کرد؛ این تهدید جدی برای امنیت نظام حکمرانی است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/657594" target="_blank">📅 11:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657593">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fG3_NsJCyyyOLCo3MuItN3jXbxqVvPyxKxY-RJLSEU2U2Zz8vWo6IZn1fdnuID7P3SI-_QA_u8dk1W2_cOmeE6tjkdUUohVY0KuM5tPOp_9XrLZFoq5N7WVvpL88-wt6SGrHmqJgC-4QKgy552INFLVFKR2qet28pOQIJXhLysk5_F-4-cvELBEudw8YnP4Q0rypaa7C4ZMm0Vdozfso34JjvzcXBh5Nbq3DDxzTaG7YQdD9sbYgkeOCyyKIBKYOJKblAZ-Uzw_x5PkPsXEPaxFG9ao5kufLHjw3VhLerDGsDDwU2sHkj5caemceNL69tWrmJeHZflOwWyYW8znCxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سی‌ان‌ان: ترامپ ۳۷ بار از «نزدیکی توافق با ایران» سخن گفته است
سی‌ان‌ان:
🔹
دونالد ترامپ از آغاز تنش‌ها با ایران دست‌کم ۳۷ بار مدعی نزدیک بودن توافق شده، اما این اظهارات تاکنون به نتیجه ملموسی نرسیده است.
🔹
تحلیلگران می‌گویند تکرار این وعده‌ها به اعتبار دیپلماتیک او آسیب زده و موجب افزایش تردید ناظران شده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/657593" target="_blank">📅 11:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657592">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
مراسم وداع و تشییع رهبر شهید انقلاب پس از دهه اول محرم برگزار می‌شود
ستاد بزرگداشت عروج رهبر شهید انقلاب:
🔹
زمان و جزئیات منتشرشده درباره مراسم وداع، تشییع و تدفین رهبر شهید انقلاب و شهدای خانواده ایشان در فضای رسانه‌ای معتبر نیست.
🔹
با توجه به ایام عزاداری محرم، این مراسم پس از دهه اول محرم و پس از هماهنگی نهایی دستگاه‌های مسئول برگزار خواهد شد و جزئیات آن متعاقباً اعلام می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/657592" target="_blank">📅 11:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657591">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NyzhUi6maudcW6Kgj2axgA6DE87sH8w7aMCB_VrOCw6Jpaew4Bwz_cRFQGc0cAX6qCaMwLKE0HKir-bt3xNwPfeEx87veU1r74tlXJrcK6DRIval7HJs_pv4Zet5FR94EIE0Pcc6bCJZThFSI1QC1Vv2rk-YA-88rcypUimwf-oDE5wNw168apyd25ZlYoQEQwJNU_4HlVmlsahIFiFg3Mrv4A2cpzdJA8lhjPAMP06ZKMErL_NZp4W6VLYNrMWcDMFtkcvtVgtdfPRTsZenp9S-V07nH9CthItGSKolUxnsgMXjkHH5bSnecnnL3CbXX9IQLvJrAwrWlxehdnse8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۰ خطای وحشتناک در جام جهانی که فوتبال را فراتر از یک بازی کردند | از تکل‌های مرگبار تا جنجال‌های فراموش‌نشدنی
🔹
جام جهانی فوتبال فقط میدان نمایش مهارت نیست؛ بلکه صحنه‌ای است که در آن فشار روانی، غرور ملی و رقابت شدید می‌تواند منجر به برخوردهایی شود که گاهی از مرز ورزش فراتر می‌روند.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3221244</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/657591" target="_blank">📅 11:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657590">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cBqSzl3WqvaPZNAiuzNepX418yqbWIp6pYgrZU_3Z5XDm3KnrlLlI-qt1GBM_OjnxtjFLOSSqW1O5Jwd-Qz-cPfu78ad4ql2rROx8quVedKe2Qklxf9-UYAjoWEi1dDdxRUeH0Szi0GL0cBs0bE3fujPUYViZzLa3uRLKWZ7i7T-gpHRTLwoXSCvi8Z15zi4ZlBUxEcqprkgLmwdsIb4TzhOHk7uNtCoUaWLhk3kQoyguAuLJPDTpb9FdiUpq8sXMCz9j1zVk2tmy94DBwYuR9et7TkCBHjprQM5rV_bSa3idQrvaD9Pk-QB2g5F3JzwVneQaMQNk0kTj_tvBXae2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ذخایر استراتژیک نفت آمریکا در آستانه کف ۴۰ ساله
🔹
ذخایر استراتژیک نفت آمریکا در هفته گذشته با کاهش ۷.۹ میلیون بشکه‌ای به ۳۴۹ میلیون بشکه تا ۵ ژوئن رسید. با ادامه این روند، سطح ذخایر طی روزهای آینده به پایین‌ترین میزان خود از سال ۱۹۸۳، زمان آغاز پر شدن این مخازن، خواهد رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/657590" target="_blank">📅 11:07 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657589">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
چین: مذاکرات ایران و آمریکا در مرحله‌ای حساس است
سخنگوی وزارت امور خارجه چین:
🔹
مذاکرات میان ایران و آمریکا در مرحله‌ای مهم قرار دارد و هیچ طرفی نباید زمینه‌ساز ازسرگیری تنش‌ها شود.
🔹
استفاده بی‌رویه از زور، مناقشه میان آمریکا، اسرائیل و ایران را پیچیده‌تر می‌کند و از همه طرف‌ها خواست با حفظ خویشتنداری، از هر اقدامی که به تشدید تنش در خاورمیانه منجر می‌شود، پرهیز کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/657589" target="_blank">📅 11:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657584">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T9ItIpGLM9g11RF1zd2wtCEL5GUzIQHZNArIDw0li-8HYZsAtVTzbKPZHtmnPAclwLs7t67tWLNsVWaDGGGe-OFvDguRzRl0JYnNh8KbbxI6ML8WvliOJDXCZNUUx7QFVCc4LkFw4UGuSsVFTv-5kgFVWaI9YEpLSn-rz0Ol_VvxaZGCtnRwbFBMhL5BG7FWOV3KPJqYA4EOQqeMYyxmZJnqFKiX1vZasn212iydtd11lpLO2jSAtpmQXw5gNjjdqwkrVrpDum1Uzr8nRIGsXtt0xJQV62pZK90jigXQjh-3TwJD9SuOMY2ioIRgitXG8C8itMgZF3xambolU3hKUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I4VzG121G9nMW0r4bR_Ncqded6eSOwDynJUcaJUNNERQMyvCBbves4gikpNV3LWpmhgh9UxHdCjYpcNvOIf3Nhqmh3mGBZQrjtCcgEn-zsOfoY5U187nM5eTpgypdUd8Q_6APqthvCDOf85uba-sU0UVX33KqAOeoyo7JvEe_Rc3y7vN3JF9b9uokTzIE6JriR4P2vpX0ArwwXKGVY5CLbYPOm8eo-okgRezZRi2Un9z0D1S0oL55zxX_8jHhmJJljzmmQ9pvaQlfCEBmY4mVAu9zhSP8Z9f6ZT3aPhTy40rMOK2uh4ykAHCf6G0aFd4KFcGXA1e6KyT_oYkMI5N0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TUamUxSyAfxL3Wb0IwpycB0gEY3bJEiXu9zp9h037CWUgVmgriK536DDCw5MutNkm2cwzRAMsaRdzvQbsO5wql8hiBn2itGOYnUwCDig6DxKSei7OBGmhpiP-7uoEGbnhNrDFVpsphNGFs_TsJSMmygbftiAS1yJS-VS9MWl0LDvinMYd6FCN2BdSGklUyItWO0ih91Xj9kStI8l-_V6YKGat19i2udE6uW1kGK7XSvnwPKR8mNwapnO43QldIlz16OENWb3G3BhiGqsEf-d4lXHme7hUZoKirnBWXGE9XrfG64P2xLQvnZ_NGWJSeV7jmt1LI3g1CELvssfErLO1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ih32R6xb47fZCv2VT74o7u64s7r6bhukcWj1D_NZlJX5xTsEmc1Xb2_5axE-lpuEfFpUP_EPhEtkI0puBDqFixBejBjjM91t0v7KYNAwtc_vb9aERh14N1Z-rbmNiNM8Oj-XgN93I0tBRCEEHEvep2ykrObx50AYAoQZ5GVDUaenZMNEcHAHESBXfSdYbJhldM9-hGCVlqF690YZk7oM6H-i9HViISi9TGeSVWtZTxWd0T0zdr8WpP1JW_Jmru84AHMaRy8MiR9J-_Uxu_h3P6O7jX0KQe603Yvu0kNLMD5DhkWBEZ3TRVUWqIIUmjAHCb1MPdblegCKRxrMNXxtlg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6a4abb628.mp4?token=bwhVQ1lhtItSZ92HL7D6n4DGN-Tk2R2DfR8YUgNa5hmdtmCDnN0ZkbY0G8Li5TzIquQmZYEoOctjh7PImZXew3xfqbk-KdstFN-yzieJMl4UHcjdczEoADZFuHi1sDWBzsImELGi9NorErCd0b7PNppW5oF-MTSFOaN_6G2TGGb-TTH0rxywaukmAjRoEuZ9b3BepCxlQP1y8bp3yMr_Dy-eBsP_pk9DIhjgM91vtoZTANDK6soJCGwM1Ey_PS4bY5zDbjpktfB_9LH7nbYjnx6TYV5clPdC3OQiMnPikCYkDeeJIJzn_48dftk0vmo0wJGpklVueaJfPh5fLdtn-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6a4abb628.mp4?token=bwhVQ1lhtItSZ92HL7D6n4DGN-Tk2R2DfR8YUgNa5hmdtmCDnN0ZkbY0G8Li5TzIquQmZYEoOctjh7PImZXew3xfqbk-KdstFN-yzieJMl4UHcjdczEoADZFuHi1sDWBzsImELGi9NorErCd0b7PNppW5oF-MTSFOaN_6G2TGGb-TTH0rxywaukmAjRoEuZ9b3BepCxlQP1y8bp3yMr_Dy-eBsP_pk9DIhjgM91vtoZTANDK6soJCGwM1Ey_PS4bY5zDbjpktfB_9LH7nbYjnx6TYV5clPdC3OQiMnPikCYkDeeJIJzn_48dftk0vmo0wJGpklVueaJfPh5fLdtn-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شست‌وشوی گنبد حرم حضرت اباالفضل العباس (علیه‌السلام) در آستانه ماه محرم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/657584" target="_blank">📅 11:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657583">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56c7cabe88.mp4?token=YxORp_1JalS0aWxgc4rmMwLHiT1fzjDPsZnUakZmZAxQYEywWqM33yGcpEHDeOXRXliHcQfzzJGq5nWsqO4JoGnGqa9rF4leTLtSBJJk8mSVVhCe6eVQmZXKujBgwPmNjGWDzSZkg3BZ9f8V1mSMLMNSmi2S-SDU32prO_EBvdkFyCwBiGBAnzyf9wCRp6epSIvG2XH0x5xbn6lVZFnjibi2J4eSHzVQFHmRy6zEAKCdMROHCuhjEvqQfWPo5excLy5Tk4qDlv_zAsth6d-PqkVTYs-pVrsU_DX-pmsc9-9FcN8_vw7Ouq2DwFRhByE9kUnbGRGqmDix7IucjOJ69g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56c7cabe88.mp4?token=YxORp_1JalS0aWxgc4rmMwLHiT1fzjDPsZnUakZmZAxQYEywWqM33yGcpEHDeOXRXliHcQfzzJGq5nWsqO4JoGnGqa9rF4leTLtSBJJk8mSVVhCe6eVQmZXKujBgwPmNjGWDzSZkg3BZ9f8V1mSMLMNSmi2S-SDU32prO_EBvdkFyCwBiGBAnzyf9wCRp6epSIvG2XH0x5xbn6lVZFnjibi2J4eSHzVQFHmRy6zEAKCdMROHCuhjEvqQfWPo5excLy5Tk4qDlv_zAsth6d-PqkVTYs-pVrsU_DX-pmsc9-9FcN8_vw7Ouq2DwFRhByE9kUnbGRGqmDix7IucjOJ69g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فوران آتشفشان لووتوبا در اندونزی
🔹
آتشفشان لووتوبا در اندونزی با ۹ بار فوران، خاکستر را تا ارتفاع ۳.۸ کیلومتر پرتاب کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/657583" target="_blank">📅 10:57 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657582">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
درخواست ایران از فیفا برای بستن بازوبند مشکی مقابل مصر
🔹
فدراسیون فوتبال ایران به‌طور رسمی از فیفا خواست مجوز بستن بازوبند مشکی توسط بازیکنان تیم ملی در دیدار برابر مصر را صادر کند.
🔹
این مسابقه پنجم تیر و همزمان با عاشورا در سیاتل برگزار می‌شود و ایران اعلام کرده بازیکنان به احترام این روز با بازوبند مشکی وارد زمین خواهند شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/657582" target="_blank">📅 10:51 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657581">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e36a1fb33.mp4?token=F5vLAs2FddjDWOXp5LqfxezdAWH1RgQVaHDSp-Gj6HemhUUtpCIe9407NyKQbYnbO_MJpF_C5DpPb4LUTWCvf8c3GDDsHxJNrdPu6NQ02qRkLnDsAi9r2DbGu1-0ud0HqiFk1vfLiyphSYUEPmm7IYGBmWlDsvWBk6YIEHaQ-LzPYmeFD0_jLcGXFkj_kf_9jAnUE_6EQM4PU5LFQF22b_CuY48y6Ulnhmy_w_YEm1a6Tdh0T8ROVSgg8FuCpy81CE3Kok-qptgJ2GFVby1eBAoDc2EFgX2WVguLwtoJvIXxiSBPFyIJ3XZT6u-JqHd4QYwqvFM9fixbKaBSePgUmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e36a1fb33.mp4?token=F5vLAs2FddjDWOXp5LqfxezdAWH1RgQVaHDSp-Gj6HemhUUtpCIe9407NyKQbYnbO_MJpF_C5DpPb4LUTWCvf8c3GDDsHxJNrdPu6NQ02qRkLnDsAi9r2DbGu1-0ud0HqiFk1vfLiyphSYUEPmm7IYGBmWlDsvWBk6YIEHaQ-LzPYmeFD0_jLcGXFkj_kf_9jAnUE_6EQM4PU5LFQF22b_CuY48y6Ulnhmy_w_YEm1a6Tdh0T8ROVSgg8FuCpy81CE3Kok-qptgJ2GFVby1eBAoDc2EFgX2WVguLwtoJvIXxiSBPFyIJ3XZT6u-JqHd4QYwqvFM9fixbKaBSePgUmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آماده‌سازی صحن‌های حرم مطهر و منور رضوی با نزدیک شده به ماه محرم
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/657581" target="_blank">📅 10:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657579">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85cba66719.mp4?token=MIceP1lSdJTXFpmbF7MKrRlCUQMCQSL9pkOkTHUJCgX_qQHFFqz0BLn3Yopz-ssnW8-YNvxjIskU4BgUaiflJ0ofs7wWs9zO7YxoT2z1eiKsfs_virvZPEebzPTPIvnlMX_48UF1q9dEm9xbLkG9kWPAkENs1nUF93wlOB-wEDxOj0T0VSzBEHROvqs1ImyDSOPAoH0iOva4YtuBsXK7lMmsH7YoNMzsQKWTqKCx2hytNM9mH7FAP9GMkmMxP_xo1BMOvSPjwuW6W9Ti85lco7NlxTHzluIoccDo5byXkb28KBPXzd73rkx1k5vFKlOHDbswpUAthb6IcdbEEU-NIzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85cba66719.mp4?token=MIceP1lSdJTXFpmbF7MKrRlCUQMCQSL9pkOkTHUJCgX_qQHFFqz0BLn3Yopz-ssnW8-YNvxjIskU4BgUaiflJ0ofs7wWs9zO7YxoT2z1eiKsfs_virvZPEebzPTPIvnlMX_48UF1q9dEm9xbLkG9kWPAkENs1nUF93wlOB-wEDxOj0T0VSzBEHROvqs1ImyDSOPAoH0iOva4YtuBsXK7lMmsH7YoNMzsQKWTqKCx2hytNM9mH7FAP9GMkmMxP_xo1BMOvSPjwuW6W9Ti85lco7NlxTHzluIoccDo5byXkb28KBPXzd73rkx1k5vFKlOHDbswpUAthb6IcdbEEU-NIzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رژیم صهیونیستی خواستار تخلیه دوباره شهر صور شد
🔹
شهر و بندر صور چهارمین شهر بزرگ لبنان محسوب می‌شود که پیش از این نیز دهها هزار نفر از ساکنانش مجبور به تخلیه و حرکت به سمت مناطق شمالی شده بودند.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/657579" target="_blank">📅 10:37 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657576">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N1HdFFsnUrwu9Kmsb4QcGutH_AvAEd89eRxsO7fKK29qpZzrHZKuBE6FpnrIq_as1ru9zcWZHimNY4t5Hqt_gyM-6N0_0kEDCjwv6UuySJ2Ay006B7YCr9x6kPfuAr2OIArQZItSmU8Rm_Oz1PcLjcEhpcG_Uj98WuolKe6KaJ83_vW70iXY6Ucq5Zali2Zts8vpGHLZDlSCVtm-IW4cKxYwqBCYVeiI_84ExEL4pJ2FE4W07doqu6GW8ifh2dXJCzQNSVakzelpH5OGCizl3r4r5Om9V7_KSKxbt8f9SeH9ax-_w58QVaPiYmJ9A_NVTJDKeP3NxLmMrAxcT2s3kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3b41b0975.mp4?token=glciAscnLaC20B8B_HzneiML5KnPb2fUJgGZey0WsJt8ZA1wOz3dN2ZPYDIUm74Mearoae6H2VB2Tcss13wBsMDHinoo0voN3NK1zray6UMuFnf_wu896wM5uidXl8ThfvP1vUQrZArElLGIVJO6xQzllAD3IAXkLjXdAvT9rRWktjNryp1WFGZMTmwSIBV_n8wZhN0iJPd9BCdyxXnc7HQvTRdVJSa0PdFbvN6SOBagZFBB_Z4BvHYOgxlEFvIAnhqyX6WhbL1syqDm09beTub6ff2-DI53glztif-Ux0qnUIpUEKaE3slHER6kKTKq26E_8ZvaYluQwOp79k2bug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3b41b0975.mp4?token=glciAscnLaC20B8B_HzneiML5KnPb2fUJgGZey0WsJt8ZA1wOz3dN2ZPYDIUm74Mearoae6H2VB2Tcss13wBsMDHinoo0voN3NK1zray6UMuFnf_wu896wM5uidXl8ThfvP1vUQrZArElLGIVJO6xQzllAD3IAXkLjXdAvT9rRWktjNryp1WFGZMTmwSIBV_n8wZhN0iJPd9BCdyxXnc7HQvTRdVJSa0PdFbvN6SOBagZFBB_Z4BvHYOgxlEFvIAnhqyX6WhbL1syqDm09beTub6ff2-DI53glztif-Ux0qnUIpUEKaE3slHER6kKTKq26E_8ZvaYluQwOp79k2bug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بخش دیگری از اموال علی کریمی به نفع مردم توقیف شد
🔹
پیش از این نیز ۲ واحد تجاری و ۴ واحد مسکونی از علی کریمی شناسایی و به دستور قضایی به نفع مردم توقیف شده بود که یکی از املاک شناسایی شده یک پلاک ثبتی  شامل دو واحد تجاری و ۴ واحد مسکونی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/657576" target="_blank">📅 10:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657575">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PFOmoem8QGMUR7zS96i68O2eVSzYZd3O5jf8Epurt0hrBdlbT9Gp1oZKkINEhPRvuAwUiWHbpT_1P60aq9v3Uyj__cjBxMSwf5qMekOVirZOdqn5pwe1xGyT5hNmlKk0ToOhnJGc0YJctesaer08EUpIvtODqA_Trcmg28gRrUgDrlwlQs_rjiT9CT6DUi1XvnvAVHz0AIkP57D2YPKStm0EERrchuIpRcHFbUx6QlN8yuU3jxTuCVgoKy_6DN5uWHv0MWO0sMt7ffhyalHeZGf8Py5CIaOAOgzh6rWDFbtJ9g930mBw7wO9JMM2kkTEwQt7R6N578Sfeenze05H8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رژیم صهیونیستی خواستار تخلیه دوباره شهر صور شد
🔹
شهر و بندر صور چهارمین شهر بزرگ لبنان محسوب می‌شود که پیش از این نیز دهها هزار نفر از ساکنانش مجبور به تخلیه و حرکت به سمت مناطق شمالی شده بودند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/657575" target="_blank">📅 10:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657574">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
دیدار تدارکاتی ایران - گرنادا لغو شد/ گرنادا به دلیل آماده نبودن نفراتش نتوانست راهی مکزیک شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/657574" target="_blank">📅 10:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657573">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d289f2dfff.mp4?token=W7hyvx5s8-nBPqKuLcCsnLx8T2eR7pg5FAhpboAfRXEXO6ii3uHEDqOSs8DhKE8SQmxTBxeZqYGsdBKUFNPz_AMV4rL9qpNXNnNQGfZLXI5AwCbq9XKZmzDu5RJBKXOMEAi-mR8B8EanBZB7hd3MTYyjCm9u1lppa8yXNKPbei6PlGl-kLZMfU2EUlGPQZY1B-eMF2KBTCosoTpylM0_uyNym-pj6O_fuBnIgVN3D2_N5P_5Z-4P0tBQbBNAQiF7gV58rictScwfHdICFX-yojLrK1NF_Qf0OrJ5cEuCnYN4LYnjzgQroj8IYTm_aU6P5RPcxIacuxsQGVbyDSsvgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d289f2dfff.mp4?token=W7hyvx5s8-nBPqKuLcCsnLx8T2eR7pg5FAhpboAfRXEXO6ii3uHEDqOSs8DhKE8SQmxTBxeZqYGsdBKUFNPz_AMV4rL9qpNXNnNQGfZLXI5AwCbq9XKZmzDu5RJBKXOMEAi-mR8B8EanBZB7hd3MTYyjCm9u1lppa8yXNKPbei6PlGl-kLZMfU2EUlGPQZY1B-eMF2KBTCosoTpylM0_uyNym-pj6O_fuBnIgVN3D2_N5P_5Z-4P0tBQbBNAQiF7gV58rictScwfHdICFX-yojLrK1NF_Qf0OrJ5cEuCnYN4LYnjzgQroj8IYTm_aU6P5RPcxIacuxsQGVbyDSsvgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از شوخی رامین رضاییان با قایدی تا فارسی صحبت کردن دنیس درگاهی
🔹
تصاویری از بازیکنان تیم ملی پیش از ترک اردوی خود آنتالیا ترکیه و سفر به تیخوانا مکزیک
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/657573" target="_blank">📅 10:08 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657572">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f212e28708.mp4?token=nqna1BJsl6pSBN69CHrFmVVqLSnVCZaYD55xAXRrfYsvzkfn4JDt4a7F_T7QNNaDc52d8FAIJ51KkUgHbtL_1MddQOsn-96WZ7Kmzvivo0nq_AnjoTyu3Mq79M2PufgCIBf0djQZyD9UoCC_VP3B3fSZO_2Oc87N_1jcT5MiszD3aCEJrY6a5boO4rPCvLy8Lh2Oq0t7GRont8-Nv_jEchKOVqKB74aTTFL53Lk9atm_VaNBS5m1XhvoyHACxTZMS-7El_5jCMOreIwpYH2oMpVIIQz9YxhrLzESkmiU-FI3JN03At1ct7acqapGa_y8m8G4TqOrkop6U0KQboNakg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f212e28708.mp4?token=nqna1BJsl6pSBN69CHrFmVVqLSnVCZaYD55xAXRrfYsvzkfn4JDt4a7F_T7QNNaDc52d8FAIJ51KkUgHbtL_1MddQOsn-96WZ7Kmzvivo0nq_AnjoTyu3Mq79M2PufgCIBf0djQZyD9UoCC_VP3B3fSZO_2Oc87N_1jcT5MiszD3aCEJrY6a5boO4rPCvLy8Lh2Oq0t7GRont8-Nv_jEchKOVqKB74aTTFL53Lk9atm_VaNBS5m1XhvoyHACxTZMS-7El_5jCMOreIwpYH2oMpVIIQz9YxhrLzESkmiU-FI3JN03At1ct7acqapGa_y8m8G4TqOrkop6U0KQboNakg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
كمال‌گرایی همیشه نشونه‌ تلاش برای بهتر بودن نیست، گاهی ترس پنهانیه از اشتباه کردن، قضاوت شدن و کافی نبودن #سلامت_روان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/657572" target="_blank">📅 10:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657571">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
فدراسیون فوتبال ایران: سهمیه بلیت هواداران ایران برای مسابقات تیم ملی در جام جهانی ۲۰۲۶ لغو شده است
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/657571" target="_blank">📅 10:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657570">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-F4iGcDRfPc7mq03aP7IUlopYw7BhwoNrUsPdR6DJ8_5E6lgyQdBfqxRHLe40Jrzh3oSFa_XcNR8lZ2M_fcSBQ0NQpBmvGoRmqTnv1tUJ5i1vID1eYatGef36vKFmvbmkcLJfi4matpPhRSe75IF1mnNNcbPgjzhwQaTt4pxZp6Jh_tfjTllAzgSyaufq79Fe7_-3cn-On1r7NxkZCvoOUxf-hv98Hr-WgbSTq6Y_RMmyMD0CdDbs0BH-F3f7pMOAuXdcVq-VzFm1Sw6i74ltNeqv2sl4-fXOKswpYc5OYogRZ14LY1bBQrRWRkhjxnexXFhArt1Vo5FztM3rxKKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگر به‌دنبال تبلیغاتی مؤثر و دیده‌شدن واقعی هستید
این کانال آماده همکاری با مجموعه‌ها و برندها و تیم های تبلیغاتی بزرگ است
🎯
مخاطب فعال |
📊
بازدید بالا |
💼
همکاری حرفه‌ای
📩
برای رزرو و هماهنگی پیام دهید
👇
@newsadmin</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/657570" target="_blank">📅 09:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657569">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
واکنش دبیر شورای عالی انقلاب فرهنگی به بازگشت برخی هنرمندان به کشور: ایران، کشورِ امن تمام ایرانیان است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/657569" target="_blank">📅 09:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657568">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
فردا چهارشنبه، کالابرگ کد ملی‌های ۳، ۴، ۵ و ۶ شارژ می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/657568" target="_blank">📅 09:51 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657567">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
سخنگوی کمیسیون انرژی مجلس: هیچ تصمیمی برای اصلاح قیمت انرژی گرفته نشده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/657567" target="_blank">📅 09:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657561">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Of4RCdL2vMCvGhC_cQUUC5hBVa5L39UivN8h_oIdyAGnx6ESMhPrhwq4atICfbyaI82899NXjBgKff5PpELJ9ZCjLBsWPMu7FMlwbz8v46Zupdkr4p3wg-nc2U3HEkOuRfVq0pW5v8XLK-OuxziygrZZrKk-MgeBR98UzJqG3ZGlAfP6Eu3l0x9HM8HLDlnBJnpXDX6r8QsnC_6wLkxR5cxMIMmYGELtnbMzTxRj_hlkfIBFdeqj_wQjwo_foH52U3FKNt31WJL0FLbYqv6hznC7wmfS1JNE3Ko9hmMUTsiJrhJzuFhXGHW1PwbtkbvD8RqPDeuyRT_UTxriM-ct7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DapmaDnYgcDEF5pl3Zcnjg5ZDY7lfq6L-lJCI84gyJnZpZNfDifJXUj8P6VsEXJMaZNvYyuU_JlA3deBSef85S-e0lKJLSx3Zd0CahIwGzuk_no23Uo3X87FJBlguKiABDThzy6igJZV7TBeQ1-2uiew0Oaob7O2sp_jOJQEKKcJGfCu24-NWijntH1r1ao89RQUeuSJTZRNWlz9Oh-OHIzUKdvbV9D29_oVihG6m6erOxnyhvzEzuoM5f853DmbEjuTSxMnzT2we4y7pSL6AwnOhbczU7J76ixlKzFDFia78vQEJfv7Du5nZGubkZtP52aQQXF5gP_IiFUDPwQQBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GhsE90a4zpGHvUInIMcP-U8NRnBtTyiEcECfFT6A2jkHTxrF22N4Lbik04aZyb0YH-MwZkKYWsXQEkWtHXeH98TJ8f2Zn-0_G2e15mXGkJPnMIFLw1K1zZNGhIE-8AlIhXNYj-xVRLJefdmy7DNGSuBOAyesH4FAttMvrmv3bFPcRVGWnZpzlcdzcv2Wbjho-2arHvCN8rsxaXU8kO-rrvLxN4FQz7LsC4LiiCK0HLFTVMTRoiXX0n7yuJMpJ-PPM-vVyb2qSaeFa8fN2fIGi7trSH-EDDBaTJ1PxtEAm1n5_tCl3wT2aWVEXkGjtjL1eO_x3LlhYpOcgOrbmghmMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WoCe8PqZxgMpcw1_f3ZtuQMkxx2GFtITLxsN8PJG3nQgpFnUqg9BrIdukNUNzCihKQzOOllGxz97ZnJdtj8jmcjosjKwd-oTlZ0Sr0BYFkIbIqVLYIss5Ds4Ycyvd3Vq1YXRecICMtC1--dqHZane-oNR2xuc1IErFzGk7WM-N-mjorpKjWA3rjUEIHbksEWbEqiEeSQvwSWBGYUptYz0DSlcHwpiafzgNYhq8m4UR5dUQDcsTx_jnK7zI1IMZxCYJALRd3PA9nCbSwrJrGe7v-t3ksdApW85b2sEGvsXVjTPIyVXRwkHw_kb5KAPGRvqwi5rKO0Eg197pDV0SuQiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hheUf4b0xiPKs0MkHD2b1AKzHgpBlxdq44qEi4pnNN4rUMNgDziuxFSQ3qCMcLC1R_VfTAHzmgG7JFxxFs9oI9gCF5TWYCRm88CARXuEa_eMZ8zRDXyEfD1h7LKpt69KPJuQ3Xz7phwlra2rtJDTlAvQpxodHu30Emc6kaTMMkIiB-_jDLzggP4cn65dBAPQmAb1j9OlhpkrFWb5u5hGlF8qT0Wi5SrRO_pooWkUA7He_IAwY_QnA7JZqe8sCsfR3AeQPNEKJ58sPTOqosDiUjiowpXxoBq3A9Ro2oz1NES2_ocKQ9K4z2IQhbpZ3oJtYN-lKOeXAJ7OjncZVXL1SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ooWsGhlygta8MZH70OpT_BOp5FzT1SULmmUeuaPmZUeOvjK-f7ZAKzKbFXAyhbgNuzlyzuEmElwtcjckODiP3H1dYPLNLsbT0Q5nugw6GOej4Qqq0tFeuGnYvZuw4_vdmbwj-oqouPQ7LJeiKhbPvt0K9hOLrQw0icDcN70moxn10BCj60XcMVrzaSBnd9G4dQzr9RuFwkj5XFcUd5OD2szNvJEcjULWL-UbXN99RwDPkzDUqiIQkHvBr9pru4RAB_E9lPMuPX8ZnIxl6dYHqTJCt3U9XV1gMMdR-gTj1Nje4rD45ZlkUVCdtX9g9Ka7mYquh-Lf9FPOdxOuH4nSeA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
خوراکی‌های کلیدی برای سلامت اندام‌های حیاتی بدن را بشناسیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/657561" target="_blank">📅 09:45 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657560">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3RPuPeBuO3NuaqNwZXEmw1eTwECaFLdsyJAAgYdQW_E7Th3jaKhhEZkHPpBRi-4EuN5fJ-6uSXIHhVolusjtZAUCWBrgjSjVLVRTn5t-bi7MkcHVwY6nHJ1dU3mlKoMfZlesYwfzPXKr5PNM4ERHY7Ckf3ECjLAu-gvmWgbhZDAHP__64pHSzAmP7Q8wz4mTXVWnQaYVDZAq8ELvOqpKjpWMTEh7S6FesrfJUoeRt62RdGBfp-zc_ND3Y8EfojlVut_Qlkgr0oyYOlDv9_WGuNs2MicdIfsPx9Jb9RCG8K5biMMSM99jzl1JV5KFt2EEOZKlfUlzm5LCQ_tLxckQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تحلیلگر سیاسی آمریکایی در واکنش به ادعای یک سناتور که گفته بود ایران ضعیف شده
‌
🔹
می‌توانی تمام روز به خودت دروغ بگویی، اما واقعیت این است که ایران امروز از قبلِ این جنگ قوی‌تر شده و آمریکا هزینه سنگینی پرداخته است.
🔹
به جای پذیرش شکست، آن را موفقیت جلوه می‌دهی؛ اما این روایت ساختگی دوام زیادی نخواهد داشت.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/657560" target="_blank">📅 09:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657558">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25c62decf3.mp4?token=diQ698F-sADxZXHfDCgvD8Pnk3k94QGLZ94ZAbYCftH6gc0VMU3SV0Gc61dMuQjSlRChQvCPO2iUmsrsBGN78pPpH7PP7nPIAPeBivhDM_YtvVt22Vvgt3piJwmr6HfGpvUx05i1ImxUWsjikBkijoe4esBUlNRY_A4FkaqSGtXWi47NCQsDLct-rkW2G_gfgytx2ar73Sd3_o7EXqj1ZCSTnlgCEMYkMzJVXvNh-Y6WpK5Pc8m5bOZzF4-XSMmeqmKH_X71ikQvXU6PRs8ZNTfzHnOMO2J2S2Ci3a9I3SQEaT9moHw74cxDnTny7YEg-_aHs5Vgj-P0kfo9eBOu7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25c62decf3.mp4?token=diQ698F-sADxZXHfDCgvD8Pnk3k94QGLZ94ZAbYCftH6gc0VMU3SV0Gc61dMuQjSlRChQvCPO2iUmsrsBGN78pPpH7PP7nPIAPeBivhDM_YtvVt22Vvgt3piJwmr6HfGpvUx05i1ImxUWsjikBkijoe4esBUlNRY_A4FkaqSGtXWi47NCQsDLct-rkW2G_gfgytx2ar73Sd3_o7EXqj1ZCSTnlgCEMYkMzJVXvNh-Y6WpK5Pc8m5bOZzF4-XSMmeqmKH_X71ikQvXU6PRs8ZNTfzHnOMO2J2S2Ci3a9I3SQEaT9moHw74cxDnTny7YEg-_aHs5Vgj-P0kfo9eBOu7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تظاهرات ضددولتی هزاران نفری در برلین
🔹
خواسته‌های آنها شامل معرفی دموکراسی مستقیم، پایان دادن به پذیرش مهاجران و «پاسخگویی دقیق سیاسی» بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/657558" target="_blank">📅 09:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657557">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bec543b729.mp4?token=sseMS3C8tSEqPY-E5J1uHjrsm1PSUV0clVq8NVdk4raoHe7lhZOXSLi_UvePvEiFTz8QtG6tzcoA5ZtUeBmQu-jmq7JpaFGOZdIsEij8mPyJN_gUqr6wK5MbhLo-1l2YtB2dG-icZMs5ekjsR1tIGGfoUUgDq9JZiAoKuRabtM1GAMz-TRc_MhLCbgYdHGopHSafGYwbqsZb8Y7KZ5fg01FFqG8jyHM0vvTIMar_frT1eAxPragOFSm7IXvJR6QUgLTUSZTvDezoabSedBrTxQg1UeCOluu1J7MCw3NacTUcJW_JCO2yW4DeZUrG4eHoZM3818yguC7ewLem4EHIDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bec543b729.mp4?token=sseMS3C8tSEqPY-E5J1uHjrsm1PSUV0clVq8NVdk4raoHe7lhZOXSLi_UvePvEiFTz8QtG6tzcoA5ZtUeBmQu-jmq7JpaFGOZdIsEij8mPyJN_gUqr6wK5MbhLo-1l2YtB2dG-icZMs5ekjsR1tIGGfoUUgDq9JZiAoKuRabtM1GAMz-TRc_MhLCbgYdHGopHSafGYwbqsZb8Y7KZ5fg01FFqG8jyHM0vvTIMar_frT1eAxPragOFSm7IXvJR6QUgLTUSZTvDezoabSedBrTxQg1UeCOluu1J7MCw3NacTUcJW_JCO2yW4DeZUrG4eHoZM3818yguC7ewLem4EHIDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚫
اتفاق عجیب روی آنتن زنده
🚫
😮
توی شبکه سلامت مجری از یک کرم استفاده میکنه که مهمون برنامه گفته چین و چروک رو توی 2 دقیقه از بین میبره. منم تا نتیجه اش رو ندیدم باورم نشد ولی واقعا توی 2 دقیقه 10 سال جوون‌ترش کرد.
😳
☘
این محصول گیاهی توی ایران خودمون تولید میشه
🇮🇷
و متخصصاش دارن به مردم مشاوره 100 درصد رایگان میدن.این فرصت محدود رو از دست نده.
👇
👇
bam30.net/ads/landings/22565-2e958
bam30.net/ads/landings/22565-2e958
bam30.net/ads/landings/22565-2e958</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/657557" target="_blank">📅 09:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657556">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
منابع لبنانی از دو حمله جنگنده‌های رژیم صهیونیستی به شهر النبطیه در جنوب لبنان خبر دادند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/657556" target="_blank">📅 09:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657555">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozWdhUSq8_NriRREoPVkZ_IGelPE9q_ppolAjMOc1EOFKOBNYTWE1spuIx9XZU6M0NZLjSbPMerNuYc4z-kTQvjK37a06Tm2JYn-fJ8CFTNanTRzP9wwykJQq5nepSTnrrAOHnhvN95F5Zd4Z-yBAnm9J11fHU2yKSuVi0sLcu1blz7zsMAclUa6OZ5hY-503wDvSLzuJDNebTTfUKlQDB15eLwzPRtSBWnDJhS2tzZ8t3r9ZTRrQwFMreH46Nr34dmcnlNG9GngrhfVUBx4Vnq03LKUJoflINTkq0_pZqnTpDpezYnvsorwHez3UsJqzKqC_gDn1ZKC-Uv-vL1Jkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شاخص بورس وارد کانال ۴.۵ میلیون واحد شد
🔹
شاخص کل بورس تهران با رشد ۹۰ هزار واحدی روز متفاوتی را رقم زد و ۹۶ درصد بازار سبز پوش شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/657555" target="_blank">📅 09:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657554">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/794b8b8bec.mp4?token=Ei_b3nLIIELrFOeYTnBU_Vg7IZDpzj4zsZUzWKY17CunX9UqdWIQ0tPdhfMPCHXXlFl0hVshKmZYTF0oRf75O-Htu-3QEa8NGB8GZR85M7-BTLrbWF31ShDIOrQa5kggeuqv-UwiSj__B3BYbykqYMCrrvEE3qGPGyoWvlBhKxLXaiCv7QCnDe_EUh9OwAk40jN7u4bSSTB4ql1-HXg8SSMhktnZFPVzqIbuE0fK-r0QJP-QSNc6L940XlHDXYKBfLxednIFNiciNv3roU5EGE8xmuotNM1F3dxEyPGTtmIVwaKiNGyJOUtCHUB7PIHIu33cYrBDBDko7M9yOI2Izw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/794b8b8bec.mp4?token=Ei_b3nLIIELrFOeYTnBU_Vg7IZDpzj4zsZUzWKY17CunX9UqdWIQ0tPdhfMPCHXXlFl0hVshKmZYTF0oRf75O-Htu-3QEa8NGB8GZR85M7-BTLrbWF31ShDIOrQa5kggeuqv-UwiSj__B3BYbykqYMCrrvEE3qGPGyoWvlBhKxLXaiCv7QCnDe_EUh9OwAk40jN7u4bSSTB4ql1-HXg8SSMhktnZFPVzqIbuE0fK-r0QJP-QSNc6L940XlHDXYKBfLxednIFNiciNv3roU5EGE8xmuotNM1F3dxEyPGTtmIVwaKiNGyJOUtCHUB7PIHIu33cYrBDBDko7M9yOI2Izw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ در فینال NBA هو شد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/657554" target="_blank">📅 09:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657553">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
دبیرکل فیفا: جلسه مثبتی با تاج داشتیم
‌
🔹
فیفا همچنان به گفت‌وگو و همکاری با فدراسیون فوتبال ایران ادامه می‌دهد تا اطمینان حاصل کند که تیم و کاروان ایران، از تجربه‌ای مثبت بهره می‌برند و همه شرایط لازم برای رقابت در زمین را دارند. ما مشتاقانه منتظر هفته‌های آینده هستیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/657553" target="_blank">📅 09:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657552">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b0e58cb23.mp4?token=PDVVfCukyxLWcQGN3dvON_f73yiXkaM4Vd9DwJUBy2F9XjA8EV9yAUxFf8hgoUTWI1LZn-SHCAPDa0e28aLo-Nn3GsOV2Ta7eSuBShPjE0vpTeLy2ca8ZSOqlMOvyMQl3Bnlrr5cDgJiDAfQiQvQdl1xhdp41uBu_WgjMdCcA-hhhHuoBrpdVf8OAhX_FN3IdKGpD2V5TKllhz0A5j7d8KKcrEKyS4v6RWt0urzzrmiGbEpmaUb1pGkYOWhf90VICn61yHj_QcWPVZRi3By3oNi8iiJJBXwpgq98U-rwSiEDhuKw4OBdvX-3MjJZx_1mQ5mBz7mI0WU_O6E3Yw9xKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b0e58cb23.mp4?token=PDVVfCukyxLWcQGN3dvON_f73yiXkaM4Vd9DwJUBy2F9XjA8EV9yAUxFf8hgoUTWI1LZn-SHCAPDa0e28aLo-Nn3GsOV2Ta7eSuBShPjE0vpTeLy2ca8ZSOqlMOvyMQl3Bnlrr5cDgJiDAfQiQvQdl1xhdp41uBu_WgjMdCcA-hhhHuoBrpdVf8OAhX_FN3IdKGpD2V5TKllhz0A5j7d8KKcrEKyS4v6RWt0urzzrmiGbEpmaUb1pGkYOWhf90VICn61yHj_QcWPVZRi3By3oNi8iiJJBXwpgq98U-rwSiEDhuKw4OBdvX-3MjJZx_1mQ5mBz7mI0WU_O6E3Yw9xKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی از چاقو خوردن الهه منصوریان در فدراسیون ووشو!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/657552" target="_blank">📅 08:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657551">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a3750d770.mp4?token=eRZHWL7QmMyFOmEUrVwQb8zpV6yfkbk_RIJ3Nu-FFIETyyQfGSUBUrh9-ckhRIRgQ6vYwUB9syXGrlr4sOSyS3nhsk3YlAIpBac3aWyicE1VQP9DUZbAoKg5VWReg6G7XuaAt_k1nReOmOH8vmhUHKsWB68OEZdhdE8ZLw-dGuxceEuWYRmX8F1vBzVnMrQRyg7EFxQvYMVPMkveyN-v3gHmmwM09EknHmGxCJkAt76x91pcQBfy0Fcudu9C9RubJe0PS4zQX2-7tZ4VGZTGTcV7dokoqIDlycSIE0meC7kHxrktdx6stUQdKaU9KLuQiLJ6B_S32_23GrZZ7YSpLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a3750d770.mp4?token=eRZHWL7QmMyFOmEUrVwQb8zpV6yfkbk_RIJ3Nu-FFIETyyQfGSUBUrh9-ckhRIRgQ6vYwUB9syXGrlr4sOSyS3nhsk3YlAIpBac3aWyicE1VQP9DUZbAoKg5VWReg6G7XuaAt_k1nReOmOH8vmhUHKsWB68OEZdhdE8ZLw-dGuxceEuWYRmX8F1vBzVnMrQRyg7EFxQvYMVPMkveyN-v3gHmmwM09EknHmGxCJkAt76x91pcQBfy0Fcudu9C9RubJe0PS4zQX2-7tZ4VGZTGTcV7dokoqIDlycSIE0meC7kHxrktdx6stUQdKaU9KLuQiLJ6B_S32_23GrZZ7YSpLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دیپلمات ارشد سابق آمریکا در گفتگو با بی‌بی‌سی: ایران با این حملات، قواعد جنگ را بازنویسی کرد و این پیام را رساند که هروقت صلاح بداند می‌تواند به اسرائیل حمله بکند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/657551" target="_blank">📅 08:51 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657550">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/299e25219a.mp4?token=bOgzRj-JuOvvo7_iJsLylKdAGCnCFInkjYV90KsXOEDwDaBCIeZ3RYGW08z4bxrGyLdxAhZKJUtsO-MCsa-BCw1tcpYzivVGK3U7kI-VZThkQ_pEutUVL4bVNhaQwdjNaiwChhO5Y_a53uG4ROrLrxRTcYJpH6yRX2_pv9VyOmGQTuTaUrDu-B6rZ68J-2TJRY6oV3r7y6yIbXf3KQdyXaEgAEwkXuLgRKObFdInSxyRuuMUCVhqE-PO1bC8We5cXB-QiQFIVLe3XpTIiPPpkXMyw-QFfVeOtC2FaoRYYkNiZELdhTzZkSck3CwL9igekaXWZpOx0BR8z8zSZGw1Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/299e25219a.mp4?token=bOgzRj-JuOvvo7_iJsLylKdAGCnCFInkjYV90KsXOEDwDaBCIeZ3RYGW08z4bxrGyLdxAhZKJUtsO-MCsa-BCw1tcpYzivVGK3U7kI-VZThkQ_pEutUVL4bVNhaQwdjNaiwChhO5Y_a53uG4ROrLrxRTcYJpH6yRX2_pv9VyOmGQTuTaUrDu-B6rZ68J-2TJRY6oV3r7y6yIbXf3KQdyXaEgAEwkXuLgRKObFdInSxyRuuMUCVhqE-PO1bC8We5cXB-QiQFIVLe3XpTIiPPpkXMyw-QFfVeOtC2FaoRYYkNiZELdhTzZkSck3CwL9igekaXWZpOx0BR8z8zSZGw1Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی مجلس: هرگونه خطای محاسباتی علیه امنیت ملی ایران، با پاسخی به‌مراتب سخت‌تر و پشیمان‌کننده‌تر از عملیات‌های پیشین مواجه خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/657550" target="_blank">📅 08:45 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657549">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
اسرائیل هیوم: حمله به حومه جنوبی بیروت با واشنگتن هماهنگ شده بود و روبیو ترامپ را متقاعد کرد که در پاسخ به ایران از اسرائیل حمایت کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/657549" target="_blank">📅 08:41 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657548">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd4a89c288.mp4?token=sN7b3kH4RZ_oRYDUFjbjIzwRlXdYmYOk9Zw9jCa8yaHbUmrlFiMqf1aTUi7h_xjhInFpYX_wl8Si0dNx0_ypgpEIIJiXr28vcZvRwh48kIme_exGN_o9IXfUhauxU9ch0D-1CjIpkhQzWtcQZ2a9n-Cv1rt0iFDETrq8bz5GzCpp0y8PpJXmpITRram_1-a2obOAK3QVWCfLeKM7uUEbVII0sU2EeaS4tJJo_m8Z68zEGYxgxOpWrNaQ5Fq0lUUc4UMgLLH2Z-5lq_VPP2UgKemDapYP-4RFxayszNkO_LxoXSKdlFibR4-hDZwozZXcFnkEfejiAp3CJWGEH86iqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd4a89c288.mp4?token=sN7b3kH4RZ_oRYDUFjbjIzwRlXdYmYOk9Zw9jCa8yaHbUmrlFiMqf1aTUi7h_xjhInFpYX_wl8Si0dNx0_ypgpEIIJiXr28vcZvRwh48kIme_exGN_o9IXfUhauxU9ch0D-1CjIpkhQzWtcQZ2a9n-Cv1rt0iFDETrq8bz5GzCpp0y8PpJXmpITRram_1-a2obOAK3QVWCfLeKM7uUEbVII0sU2EeaS4tJJo_m8Z68zEGYxgxOpWrNaQ5Fq0lUUc4UMgLLH2Z-5lq_VPP2UgKemDapYP-4RFxayszNkO_LxoXSKdlFibR4-hDZwozZXcFnkEfejiAp3CJWGEH86iqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر هر روز یک دقیقه این حرکات رو بزنی پاسچرت(حالت قرار گرفتن بدنت) اصلاح میشه #ورزش_صبحگاهی
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/657548" target="_blank">📅 08:29 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657546">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A2mvbwYr30zL1SYm0cIBn7TfTVqA6DZ07vWUYs0RvxUUYRdyLlIU8JxKFfNJZpg98Q_SLPyBu4xq9v-2-zGU-dDvm-x4rwNAjU2F2BU2L-xqdrjU9kBsIMKX8eynIhkqDG6T-nZc-oBqmbronNoBnY4wEGnX2-aM8LCfqZTMOSv1lXkOs1FrprZoetZ-4vC23hN3nyk_geqcv4n2shbt8f-1Ttfax8zNEoEtkU5lN_4pbKcMHyhM6kBoWlJtKntHxJ8HrsWYXnyGg49JBSAslkU3nXOB14iqfeQ5cO2a7I5lxZf5mupGVXh75_kSu12YGPM-iFi_XiCZ-PTYwOzV5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جوسازی لس‌آنجلس‌تایمز برای تیم ملی ایران
لس‌آنجلس‌تایمز:
🔹
تیم ایران با سنجاق سینه‌های طلایی شماره ۱۶۸ به یاد کودکان جان‌باخته در حمله موشکی به یک مدرسه ابتدایی در میناب، همزمان با آغاز آماده‌سازی برای جام جهانی، وارد تیخوانا شد.
🔹
حرکت یادبود بازیکنان، ممنوعیت فیفا در مورد پیام‌های سیاسی را آزمایش می‌کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/657546" target="_blank">📅 08:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657545">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
سقوط بالگرد نظامی آمریکا در نزدیکی تنگۀ هرمز
🔹
طبق گزارش نیویورک تایمز، یک بالگرد آپاچی ارتش آمریکا در نزدیکی تنگه هرمز سقوط کرد اما هر دو خدمه آن به سلامت به محل امن منتقل شدند./ فارس
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/657545" target="_blank">📅 08:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657544">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iS1j_77YWqbxlvXRd0QpE5yzzy93nunBcagEmVtdXjemJGUUtMVhu4YnamcYHVDFthdOqeE3yehS-pYoav1h31AWEWnTrJz-VWZDiekzx4Pk4nmo991JDSRHjcw8Qr5A8UpMKW3FaexGw56oA-cSSYBVyGP1Ench7aHXYngWTwD-JxTibt0NqccRrjnWq7A3Ls8YQr0AX_sTYo759_Mf8SFqKKyMC98s-9Hl0Nbns-5QdKUyZzC0Dsil__c7vzyT49niJ7yOfmdWvV-tGYiHiN0qNK4XEdnoBPSyam-hVZ9ZPrmmFbWuPz_9r0PAfeY3SaYyiqfF7peglJ9D32g9qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: همه ما در قبال حفاظت از محیط زیست مسئولیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/657544" target="_blank">📅 08:09 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657543">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
پرواز‌های شهر فرودگاهی امام خمینی (ره) برقرار شد
🔹
هزینه صد روز نخست جنگ آمریکا علیه ایران از ۱۰۵ میلیارد دلار عبور کرد
🔹
تیم ملی امید از بازی دوستانه با بحرین انصراف داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/657543" target="_blank">📅 08:08 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657542">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
شهردار نیویورک: ویزای یک‌روزه با روح جام‌جهانی تعارض دارد
زهران ممدانی، شهردار مسلمان نیویورک:
🔹
صدور ویزای یک‌روزه برای ایران با روح جام‌جهانی در تضاد است.
🔹
پیش از آغاز مسابقات، کارشکنی‌ها و برخوردهای آمریکا با انتقادهایی روبه‌رو شده و میزبانی این کشور را زیر سؤال برده است.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/657542" target="_blank">📅 08:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657535">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KlR2yrDFs7ViD2rrRI32KOFua4GyP1qkTAOPRW2Eqktve-abNpVX8QnmxO-4B1UGJ0JOsy-C5SWW31SVBO1TtsgohsygsqUMfaIVRU00FQUiZ8xjfoUrQeAjgpdcIM4XcEp7MXgISUSScqqXV7mh9m7iiHScgqxqaW-pHEmu9uUcvUO0FQ-yGqwt3m65LWUlLWRatu62NZ89CD59R7fk7e8ooWpa2ymHbTSRQo8QJzenHw21YM_oKl3LedLZ0wM_15alOWcURMTBsw4WK1qvJkE2Lc53Db_ZtLEjYN8wggU7kd5UOc9tdCqLpihVAAGht3jdJEclDgrCMwIbI63hXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eC_Yk-U_QNZuy5jenodlAajEAXBOpchJr8F5BA9OaCt9HDdjgtgAPk-dIqZu3FwzqneguuRRSCudiXeQheY9CgnesiIAx6o9Nq5gfGdbf38QIgjqmCMC1PoxKc7zwytEYeOySjEQpPKoG8p8Qwg6mzHgOk7pp7CpKzOxyLRpQ-hLCdk-9X4Pf-dZrcw2KwR8AjoEqDpJ1GC1b5kQlNoxKbDKSo2C0Glk2XzSQ58nnQVMU1R-FETzUhWvmZT1eQjWr7oVm9tNleMbFvf_fxEhBxjtME_Lq-7T0JegFhewY0DrbtUBmG6BHGClZWrJi_fpDxvbg4hOhfySAsUeR-ZCjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k04wPcdOjnLganSlM9R7E-vzEL2gXK06713PUmUb0rqR-I6qaB0AVUyX7PwOt4MgdJCNKWqyU11NWrCtK0pHuJRYESjMoJ6TelW4Lf3jGQ2En5x8J9LAYMyYKpnP2fYMHZR_YDPU8uX-jigckVhHfkEmkysbozHSvatoa0da8keUvNK13zYupAofNHYxMKjmRstVZlWEYiOslbi5ID6fGZabn8IQyczqWtOkhi5Hpt9zrj72gW0VdN3pMGQJwyq7vJsTmtxcKqo7OtCxlOHxZqIxkVd2MTpbVQlvMifHc4IhhxLyddnD7J6c8-5ilI9F780uK9nQX5kx6O0-EDu3rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sZpE33_ttLTIeYWXuNwLaVLS-2qQj_OJyNEMKDkqzxpboSHydCeVcMNcCwV-lajGW2a5zR6QK_i1qOC3yeDlvgZs-wzLlx-0rkVjOQzuigyK7QuBqBh-vz-4ftxbyr-9Ebxh8L7TzHc5z0xl8zmobRv1jaSQUr7rC5PY6Cr_u-kj6yzdJylfX0eYMQGwE2RzlboY98eDWTrlvtcD7lB5fxQ1fsnu0Z0-bkMmbcvzL_Np3uYEdboZfN-YGwBwxLlL5HXddWThfPpy9tyDjNia5NiwYLQdnXd-NgHdR6qQHTl7OWjFomYuZ6z9ok687AglkLvaotCI8wnph6tChPOfyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XxHeDjZHc7OBhHJbbkYlpX5zO7aJWBQcz4NuxZ0s66SF5hcmNKWnhkODO-x1FZDZF2eKSMmkBIjTKeiGxZ68UZ81ZJhUc6BzflyQRxroS92tIYa29QE5wNXenv28MY3nC0RyQ51GCvhnih4XKTb4DuxAMA4d0O4--CKLjdfZwn4PlhXjsqacAwWJdsyw6uHJfWU5E3hSxQ2BKQ78RjxlBJYc25ABNvP2ulAXAGbLaBWb4xFsMJ4Vc9f5fMLvroefsZK2XoEb8FJg8GX7WYOvboZemRUMftgOdKgfoZSj_pbrOVoVq9vZXZADCebAbNcBHcLOOLXRdVAQYW4gVYDFKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UpCSLcALqzfqfAfySv3YMjaVUPMbip-VijavOpGO-Q29MhbhDiCxbr8XcUoUmpdFnn_jw8BhkGWUH8eIIzHGLsIPWB1he0X7sPdemmMhOQYouXfGmxon-mzFpbpIS5ZMPwGNlWWLjQ4LmhuSFZm4GU4st35BgEFV-1pBPgYznbnnAHBbABchOHW8tXoBTir1cwfHkZ_QkBZIiFXf8PdD9iquK7kaQlHX4za-RBjYQ5qxGBaazkZe-Yn3l9q9_zlUosKpdeW7x9DdsUI-TETtnqMo39peZblMCNTwF0_esEXzHJXtO2jLY8nvtL6V0CvkVlJyLirk_tNzpEYGPt1TSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XxHeDjZHc7OBhHJbbkYlpX5zO7aJWBQcz4NuxZ0s66SF5hcmNKWnhkODO-x1FZDZF2eKSMmkBIjTKeiGxZ68UZ81ZJhUc6BzflyQRxroS92tIYa29QE5wNXenv28MY3nC0RyQ51GCvhnih4XKTb4DuxAMA4d0O4--CKLjdfZwn4PlhXjsqacAwWJdsyw6uHJfWU5E3hSxQ2BKQ78RjxlBJYc25ABNvP2ulAXAGbLaBWb4xFsMJ4Vc9f5fMLvroefsZK2XoEb8FJg8GX7WYOvboZemRUMftgOdKgfoZSj_pbrOVoVq9vZXZADCebAbNcBHcLOOLXRdVAQYW4gVYDFKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
سرنوشت مهاجرت معکوس برخی خوانندگان به ایران
🔹
در سال‌های اخیر برخی خوانندگان ایرانی که خارج از کشور فعالیت می‌کردند، دوباره به ایران بازگشته‌اند.
🔹
این بازگشت‌ها در موارد مختلف، سرنوشت‌های متفاوت و گاهی پرحاشیه‌ای داشته است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/657535" target="_blank">📅 07:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657534">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
خوش‌آمدگویی به سبک آمریکا
آمریکایی‌ها
در ادامه رفتارهای توهین‌آمیز خود به عنوان میزبان جام‌جهانی، با سگ موادیاب و دستگاه‌های فلزیاب از تیم ملی ازبکستان استقبال کردند!
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/657534" target="_blank">📅 07:52 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657533">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
وعده تکراری ترامپ چاشنی نفت؛ ترامپ از «پیروزی کامل» در آینده نزدیک گفت
ادعای تکراری ترامپ:
🔹
«فکر می‌کنم ما در حال پیروزی در این نبرد هستیم، اما شما واقعاً در دو هفته آینده پیروز خواهید شد،
🔹
زمانی که ما پیروزی کامل را اعلام کنیم. این یک پیروزی کامل خواهد بود، خیلی زود اتفاق می‌افتد، و قیمت نفت سقوط خواهد شد.»
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/657533" target="_blank">📅 07:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657532">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
حماس: ایران به ما اطلاع داده که برای توقف جنگ در تمامی جبهه‌ها از جمله غزه تلاش می‌کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/657532" target="_blank">📅 07:45 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657529">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6d9b95d43.mp4?token=pFtTX4rZR16igeZffc2M9ZC2CTy39-SQLzDPWDZ9DOWWBzpH111phwCQcYHLh7Fc_jXu9HjM-dxw8GJoNlqkW4RyIwzyfXzwAkXMjKOFU52tIPDqH9ur0WitbHr-rYrk0ayhguy3P_-SaaUYLykRS8e-ieSbHwZR5SwpXQ2R39RBkFyIN3zmht39ACDuTaUsrZhYE0UScuBhsy37ks9bHBOOp_x33S_9LpzOJ2Yx3qh4UaMZIZlJtiftFqNRnymapAUBetP-ZQu2JjNHoelK-t5KsnwthltHm-YlOFRZq9G8oM8pX4b3tCo_fzzn51mMVXMirSv53QJ81IM2zxvb0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6d9b95d43.mp4?token=pFtTX4rZR16igeZffc2M9ZC2CTy39-SQLzDPWDZ9DOWWBzpH111phwCQcYHLh7Fc_jXu9HjM-dxw8GJoNlqkW4RyIwzyfXzwAkXMjKOFU52tIPDqH9ur0WitbHr-rYrk0ayhguy3P_-SaaUYLykRS8e-ieSbHwZR5SwpXQ2R39RBkFyIN3zmht39ACDuTaUsrZhYE0UScuBhsy37ks9bHBOOp_x33S_9LpzOJ2Yx3qh4UaMZIZlJtiftFqNRnymapAUBetP-ZQu2JjNHoelK-t5KsnwthltHm-YlOFRZq9G8oM8pX4b3tCo_fzzn51mMVXMirSv53QJ81IM2zxvb0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ در فینال NBA هو شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/657529" target="_blank">📅 07:45 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657528">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
ادعای ترامپ متوهم: اسرائیل دیگر به جنگ با ایران باز نمی‌گردد
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/657528" target="_blank">📅 07:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657527">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
ونس: منافع ما در برخی پرونده‌ها با اسرائیل همسو نیست !
دیوید ونس معاون رئیس‌جمهور آمریکا:
🔹
تحولات ماه‌های اخیر، فرصتی برای دستیابی به یک توافق بلندمدت درباره پرونده هسته‌ای ایران ایجاد کرده است. ترامپ معتقد است که می‌توان به چنین توافقی دست یافت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/657527" target="_blank">📅 07:41 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657526">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc7e4651d4.mp4?token=BtBaWuVcHPOzm8-PtUHJy9oJgt1WX8kIVYDz75nBrRyNDmRTOC4-L2VLVUXtfx4bOGNGUMfobRytTai3aWFbRmoGUhudIgQ7bYr4CessST4Ma7qa4gy9aS0YbPKOorYnCqqLqraH-J3J1Qcr7qHY0E8GmfT3N6nBWJp6U09DhlrHJ7Qt6noT1I2rAQtQbPdCNOzlE2aAeY3uLjviJJriQGLqXqhmx3kp_H-5d7RVWuqszxuRSEV0ZvQ7xVcQTirHB9JPbrMY1gVLfswsO--Tz7OtmaNBvWD53j1Skh5_HXZSh86vuTL9LiD5-Uc70WBdCmoV09tuZ-KvqrdrCFtOYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc7e4651d4.mp4?token=BtBaWuVcHPOzm8-PtUHJy9oJgt1WX8kIVYDz75nBrRyNDmRTOC4-L2VLVUXtfx4bOGNGUMfobRytTai3aWFbRmoGUhudIgQ7bYr4CessST4Ma7qa4gy9aS0YbPKOorYnCqqLqraH-J3J1Qcr7qHY0E8GmfT3N6nBWJp6U09DhlrHJ7Qt6noT1I2rAQtQbPdCNOzlE2aAeY3uLjviJJriQGLqXqhmx3kp_H-5d7RVWuqszxuRSEV0ZvQ7xVcQTirHB9JPbrMY1gVLfswsO--Tz7OtmaNBvWD53j1Skh5_HXZSh86vuTL9LiD5-Uc70WBdCmoV09tuZ-KvqrdrCFtOYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بقائی: افتخار به دزدی اموال ایرانیان شرم‌آور است
سخنگوی وزارت خارجه با انتشار ویدئویی از اظهارات وزیر خزانه‌داری آمریکا:
🔹
اکنون او درمی‌یابد که جاه و مقامش بر اندامش زار می‌زند؛ همچون جامهٔ غولی بلندبالا بر تنِ دزدی فرومایه و کوتوله.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/657526" target="_blank">📅 07:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657525">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
سقوط بالگرد نظامی آمریکا در نزدیکی تنگۀ هرمز
🔹
طبق گزارش نیویورک تایمز، یک بالگرد آپاچی ارتش آمریکا در نزدیکی تنگه هرمز سقوط کرد اما هر دو خدمه آن به سلامت به محل امن منتقل شدند./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/657525" target="_blank">📅 07:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657524">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLDtktKPs2RfVS9vK50JXHeKbBIKAmcYpI-cfGLhQh6M3N_JKQqJA-1D2e00sG-orCVCe9wPFaMiKvtqicTAMgwfXxL8KIFqIMRqwvuMAelOOtFKU6CAPJ2J2nAMRUyyVoUliORqEVMBScZRADX9Eieu31HkSRkRUh-GccqPjTFiKftaMu9YPsefKoZP7CEOgeKggXMpPBiNb6raeAU4lWnJjKwpGJR27v7BRgTgISRDRRrhnK058aDuQYrioIhVOQzI6NsyX25XcYfVVjAMDPa16FHcaJfFitPIA1jkMWzWUL8n4DMrPBKm9nQDHP4TyVLBpsXxZBRctLY9uM1J7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طرح روی جلد نشریه آلمانی اشپیگل:
ترامپ، خراب‌کننده‌ جام‌جهانی
چگونه دونالد ترامپ از جام جهانی فوتبال سوءاستفاده می‌کند!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/657524" target="_blank">📅 07:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657521">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XgZpPTOz-e_-5K9RfXmvFDRXiv48JrW01pkYGuGSH8xS8zciLyMwt3eolPW5RIJ_TEctTCdxteNbpCnnIHkbSimY36NJjX75tXOiUcnyX7xMSEkH_ycjSzd-b735z-9e3EgUvHmyAmE3YrxwvhxkgufV2DPwNfNEgTbSzoAm9u7VS8Pwm1GUf6ETQfmM72ypsxA0xZgedadH7oL6nvIiBKJR7SmdtvEjKaAj2yYOjQsDwAhIncIMU5UCbgarTqnnCiH0vciDiJuqUBPRfobC601a0xwKlwczqyDCpDFNnkWofM-36i2uFC0CZ2ya4SPR2oW-pN6budA-dRZN43EysQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز سه‌شنبه
۱۹ خرداد ماه
۲۳ ذی‌الحجه ‌۱۴۴۷
۹ ژوئن ۲۰۲۶
سه‌شنبه‌ها
#دعای_توسل
بخوانیم
⬅️
متن و صوت دعای توسل
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/657521" target="_blank">📅 07:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657520">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXSYQIStSQGd2_usO-JknCcNsoyv7hEF-_p5Gmr2h6kPLpB3e3APqa35Em-uzPWXkgK5eUoz9MitA4_XqTNwjokUFfhJ8z5M-7AqQzbkv13GlwOmb25OuP7hyxc13KgOEbmFIh-kNEEYScPeRtS-GQw7O3T66EcRw4xrs03YqucNrx4RbWOTvgC2IgL403z5b_fghA7091pTkL4Cda8xahiiwUhCdhamHDw-UBZ8dxGuliPIhLXLZ9K8MG_94ioUdlAqc20q6b9nldmchHHe0vNjMeemur-bLZYsnCPI3V1tREG6mvh38HRW3P21_m-csjoXPmb3CV6Y0z7glD9gew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
*نجات جان یک کودک در انتظار مهربانی شما*
اورهانِ ۵ ساله، مبتلا به سرطان خون برای انجام شیمی‌درمانی ماهانه و آزمایش و تصویربرداری مکرر، نیازمند تهیه‌ی دارو از بازار آزاد است
😭
💔
پدرش با حقوق اندک توان پرداخت هزینه‌ درمان را ندارد. با هر مبلغی امید را به این خانواده هدیه کنیم. فقر نباید پایانِ زندگی این کودک ۵ ساله باشد.
🙏
😭
🌹
💳
برای کپی کارت/شبا کلیک کنید
6037691990480709
5892107047084630
IR420190000000216756895002
پرونده بیمار
|
مجوزها
|
پرونده‌های تسویه‌شده
|
تلگرام مهرآمن
|
سایت خیریه
|
برای گزارش پرونده های درمان زیر ۱۸ سال پیام دهید
@PoshtibaniDarman
⚠️
مازاد کمک‌های مردمی صرف امور مؤسسه و یاری به سایر کودکان محروم می‌شود.
💚
کانال ما
👈🏻
https://t.me/mehreamencharityy</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/657520" target="_blank">📅 01:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657519">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromگسترده ماینو</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E-79zIKafRctwv0v-16es0zUKpawSf-htWWNflP4K5BAwpEm4nT1zxD0yHBJ8Ugwpw4GRf9I-99nN8wWFmHEsIPGqrJ1VN577nX3VqNWHdrc88FxQHvIXFeFR_2nvtq09fzLk2WGjm3rXg77cGhaQkxtdftrP0uJ_4SN4tpRvWpR2UrmXFR-3ksJRFc7qfVDOggGfqjNUwU9mZByGm9fzurvRIrjhuXwGrd7cOQQwgrV-lsHSnrYErWqW33jGXiR7t-iQic_WGBZ6a_GTKwo1s3LYeXZ1Gu-OpTZyHMLYU_fpWinZuaoxjXWd9phPMGLgte4rK4k6qFlnz5csq5uew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه می‌خوای بیشتر از همیشه دیده بشی، حتماً پیام بده!
🔺
ماینو با بزرگترین ظرفیت گسترده تبلیغاتی در تمامی پلتفرمها در کنار شما خواهد بود
@gostarde_maino
پشتیبانی 24 ساعته
مشاوره و سفارش:
@Maino_marketer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/657519" target="_blank">📅 01:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657518">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTFyFIUApMPU6Xk3oQG9BSUjNMCq3KYEy1MF7Xy5q2EtXoO-pm7ixN3hcMP27ICaZnJWHFnjJNO-mi4-ZYkLHRxPihDULcnyz3hwrFROXsm0yI7Rt10TF134bOJrf2wsQdkbxVFbi4D9kLUw4xlPKcjWQf7Alk5uCgYsA1G1sUQv7Odx01w8yBDpDvzmzflgq8R39Oz9Ty2YORo3iNVX476iskI2FR0QKxQBT3WucnM7yfyrPkdD6QaNd3iEswxxI1wMRDSffn0g9PYWNdz95Q3zwSmeuGq3xYqvJuasqQW1K4onPPbi2h_eD62YKVq99yDu5RMBYnhXpL33F1T3hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امنیت ملی و‌منطقه ای
با قرارداد و اجاره‌نامه امنیتی ساخته نمی‌شود
#تراب_ذاکری_قشمی
لینک
کامل
یادداشت:
https://t.me/EnduranceNarrative</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/657518" target="_blank">📅 01:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657517">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LscKYBGxhsePS6zdYuxPaK7GDLHWP4jWPsMFzmoxgcXpznrIswz6RvapdtFvT6cb7sTVnOUmaK2g-07No8wutzuffaFOYfoqwPWqojHv-6iqlmoX2Br17qPrqSQ-idMGC58FcUHKQS-DJ3oF_1IHc7Eg8ZfbpT7oTvsPjXsWlLbdqrR4QVo43dC_HuhRS_BLcKe-afHSvseEikF-SWLzqw6GJXJlrxJlvxd9yHNgD5WlDz-wVOvH7HtASmqZEr5O2xxAbsTDDjgL_4L59g8e4sWVBGqBVm4cqx_mPS2xlFJcuGizdqbg-EIhb59TcKC7hJxpspMjeb1Fi1vPVqnrxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سپاه پاسداران اعلام کرد: پایگاه هوایی رامات دیوید، هدف موشک‌های بالستیک قرار گرفت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/657517" target="_blank">📅 00:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657516">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oPVPdT_3rhEuv0tS_qMQ86gMiJqeQHsCDPnj4VJuhkqCh1wU_JVEvYC0_wCirELksyUOuYM8rd82ZnT5j9csYMq6s_izxS_NXGk8xDKhgvF8Tf7VQFmkAlLld8L2v7oSVO7Z7KGN52njm3VBOF2bT4KCV8T5ulX-sS4tLdOwwoT1zxu0sQ166g7StL_4sKUXXk5l7sjcJNCFxrlofGW-EIsdUwdPy6JOjMop3RiC3wbtyNIGQDPwHlW6_xaGQl3GUQtR7YOk_sgxYre9qksNY50PQZ64abmnnSn0O9a7qa07VuPVb9hsHgrO7KGrwV_03W08oKrBK6_kAkGG6wQCSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اپل از iOS 27 رونمایی کرد
🔹
با Siri AI، سرعت بیشتر و قابلیت‌های جدید هوش مصنوعی برای ویرایش عکس.
🔹
آیفون ۱۱ و iPhone SE ۲ هم این آپدیت را دریافت می‌کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/657516" target="_blank">📅 00:51 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657515">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
کشف تجهیزات پشتیبان هدایت جنگنده‌های صهیونیستی در جنگل‌های تنکابن
🔹
تجهیزات پشتیبانی و هدایت جنگنده‌های مهاجم در جنگل‌های تنکابن کشف و جمع‌آوری شد.
🔹
این تجهیزات در یکی از مسیرهای اصلی ورود جنگنده‌های اسرائیلی به حریم هوایی تهران مستقر بوده‌اند./ فارس
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/657515" target="_blank">📅 00:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657513">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc641c2f2.mp4?token=eQqF1hhh6dJB5SGJfQcysoZsK0O2Izpg_snNRI5tBaUZ03xogh4RJc0iw6uFltlAJJQbmzHR-N_DSn1m-I-ochusH4APemK93WE-AbiWuIZ4XaL8w9Heyj7Qd5QBQR-J8Ljv3M3rlv8OITKSeSI0V2lWW4UEWgbHji5wPuhgCs8PxXiOCMMMTIMUO6tNNtNdW6CCsr_uDu_axdLQCDrUtyRmWQbAVphG1A4ZMmNJCopE1gMgl_t8defpEC3Qya1qTRivIvrgoKLV8azv98kLdjQvo7K4tumb9oygGSMJrzvuO65oPOnUyc3gO9yOtkb4wc8KQ0NNanPMwkVmgBIFmY6PBSGhErWUpda-on1aceB4ZKdLx368v-QzlkbO8dB6U_YKl1k8cd70L6mmwnVpk6bir89zVCLu2JxI7A5x9wDbV8pvoT6L-LY_c8PoVCsqFk8xM6cJJ2xzuJH6wVtoaqlwuTarCKgJqVnGj9mAOTNHvHPaVAxtwPeMd_BX_oEeGZkQvNCGwkUc10rt33kdIZB5YkRvwqjddvzcok16IhMG-24fNHUDFSHs6A7O6biYMzqN9EtmxYLcMzf5wTTUo8l8htiEOuF_1JTgDTAgB-nr7rW5bqs-HIQ0U4XfoNcmiDovwRw-9lUSjMgK43bZYqHHF4ePXBLXV-WdvHVINmo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc641c2f2.mp4?token=eQqF1hhh6dJB5SGJfQcysoZsK0O2Izpg_snNRI5tBaUZ03xogh4RJc0iw6uFltlAJJQbmzHR-N_DSn1m-I-ochusH4APemK93WE-AbiWuIZ4XaL8w9Heyj7Qd5QBQR-J8Ljv3M3rlv8OITKSeSI0V2lWW4UEWgbHji5wPuhgCs8PxXiOCMMMTIMUO6tNNtNdW6CCsr_uDu_axdLQCDrUtyRmWQbAVphG1A4ZMmNJCopE1gMgl_t8defpEC3Qya1qTRivIvrgoKLV8azv98kLdjQvo7K4tumb9oygGSMJrzvuO65oPOnUyc3gO9yOtkb4wc8KQ0NNanPMwkVmgBIFmY6PBSGhErWUpda-on1aceB4ZKdLx368v-QzlkbO8dB6U_YKl1k8cd70L6mmwnVpk6bir89zVCLu2JxI7A5x9wDbV8pvoT6L-LY_c8PoVCsqFk8xM6cJJ2xzuJH6wVtoaqlwuTarCKgJqVnGj9mAOTNHvHPaVAxtwPeMd_BX_oEeGZkQvNCGwkUc10rt33kdIZB5YkRvwqjddvzcok16IhMG-24fNHUDFSHs6A7O6biYMzqN9EtmxYLcMzf5wTTUo8l8htiEOuF_1JTgDTAgB-nr7rW5bqs-HIQ0U4XfoNcmiDovwRw-9lUSjMgK43bZYqHHF4ePXBLXV-WdvHVINmo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فاجعه در مونتری مکزیک؛ وضعیت عجیب کمپ تیم ملی ژاپن
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/657513" target="_blank">📅 00:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657511">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
مقام ایرانی: بدون آزادسازی پول‌های بلوکه‌شده و رفع تحریم‌ها، توافقی در کار نخواهد بود
🔹
مقام ایرانی مدعی شد اگر پول‌های بلوکه‌شده ما آزاد نشود و تحریم‌ها برداشته نشود، دستیابی به هیچ توافقی ممکن نیست./ تسنیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/akhbarefori/657511" target="_blank">📅 00:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657510">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JTEHdI-zd8-Dt9Lmvd8ptwJQLmc1Y26mVoU92TTbHObGOaGxSGzhZRpb1T0hb80bjZMGeSKZG_eWbNdGck1e7nDC7XKRNtwR31nqYgTL6BqYMtwO2clfyI4SSpEJPFswX0P1TV3EkgwcSreQhU6hNX1GYd4l56-dtvwVXh3rqqMuhGAqZOgz9HH4dpDXJjODlMFr8sI_pGV5zKKSSC3M5clXCRC6yP4pYoVXaA_3JzpsqcHjsHAUByFB-D4UzQIvl5pAjmbuSveXXtfUF8TTklYRTllXohaLl3orQ-FRv2mycxHhuYuUGxj9PBZkp6wuTyYWctdIEeyVzahL_XayJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک کشتی تجاری پس از آنکه توانست از ایران اجازه‌ی عبور از تنگه هرمز را کسب کند، این عکس را همراه با اظهار قدردانی، برای نهاد مدیریت تنگه هرمز ارسال کرده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/657510" target="_blank">📅 00:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657507">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZH1vOmpadZzYW2cnzI9_YlNr-H71AcLMakllAwQy2Gvvskm-XMLyiadxU_q2XzzNalkhsA_Unf1WPiF0dpuq1tIOqs29_L87KOWnOz9PwLTYFdhRcu5hfKofjAFmUjTFMzQVh2tPX8rP6o11tpqLUjzy7-8_y2G06gku2eLU6akUD8ZHmE1ATMmJT0REk4ZR3c_DQV6mvRt6GVav5D7dbICe-rG0ytZFeYBCiQNTy8vx5xHltqZ4xWfLp0hGnGtEXl5e2NtONE1owgdvpneRYBMtwC-VVw2M_l0F-_wAVtFBO5MsKUTEwwJ3gFjycfjkURZ4Z6WmEvpNw4tRJJZt_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توصیه مهم سردار سیدمجید موسوی به مردم در صدمین شب حضور ملت مبعوث در خیابان
🔹
حضور در خیابان تا زمانی که مقام معظم رهبری اراده می‌کنند حفظ کنید و تلاش داشته باشید که ما بتوانیم با پیوند زدن میدان، خیابان و دیپلماسی دشمن رو از صحنه‌ی تلاش مذبوحانه خود خارج و عزت و اقتدار رو برای ایران و ملت‌های آزاده فراهم کنیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/657507" target="_blank">📅 00:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657506">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nKWPvz0iv-k6SzHoeUikTiSFR1q3QntiMMaM5YoL-7JcAyIz99fFdi_A4I4WKJxVPnrIYXEuPfYbpy8u97TI7U_w4yjyATd0j9gABaDeTNmOpHUJTHkg-hThDFDnJWGL973DYvSkczlE2KxksqiiPPq7aQKdp2fMbaPlDqZowLb-ObZJ1ZJOZKj_v0dhzTAs9q7P9xmo3kUqQjHUB39x0e6P-w5TdB3nDU8VFrPQ3SzyQjm1mUjK4eEbszXcy--kQpagnWMNNlkrjOS5HY4S4oNfRUSLRi-aTQh9M_O9Pbt5-_q1qTSX9Bov0Fe8szUzsFA6QDMgzSX1ivEZYJ7PAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/657506" target="_blank">📅 00:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657503">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
مقام ایرانی: بدون آزادسازی پول‌های بلوکه‌شده و رفع تحریم‌ها، توافقی در کار نخواهد بود
🔹
مقام ایرانی مدعی شد اگر پول‌های بلوکه‌شده ما آزاد نشود و تحریم‌ها برداشته نشود، دستیابی به هیچ توافقی ممکن نیست./ تسنیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/657503" target="_blank">📅 23:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657502">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LnXKvUJUgV2KhqnE-KVVhXNFrW9x3Ru_3_6ASJ2FPPhwclnCT8Rw8kLwKOewezRaGdA2aHVnp7hqdHZXfx54eLl5gmi1CizqiEXDFeS7JmBTPBsd0_piihBsQ1QT6KBniQ5z2a2OGWrVJNn-2BUUhmq5woK64MYwbb3a7nqk7WWWGhBZFvgzdesHS4zC7PcHd46R1PSjh1rYfmjulo21LtN-r7lWIQjVci71FSA2LlIrpEvOoovV7OmJ0bej9N8D-Z_ukXDReeOB8RIbQJLSyu4p1lUBOPAFRRev_J-y-xDufrVzVgt5T1ULdwDDoW-HUDGUvO9w52zEuy8FuS5lAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اپل از iOS 27 رونمایی کرد
🔹
با Siri AI، سرعت بیشتر و قابلیت‌های جدید هوش مصنوعی برای ویرایش عکس.
🔹
آیفون ۱۱ و iPhone SE ۲ هم این آپدیت را دریافت می‌کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/657502" target="_blank">📅 23:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657501">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7dfd000d6.mp4?token=hWFWaahWyqwX0GNAML9LZQdrMIg5UymvjRcf6w0PLMBqIpMMg1eYTt5WoTLDgD4GM6CWNFjBK9RBsEvIotuLt2enfqRzJlNsNK1QnA-Vv_5MQfAyiubpnxX4UJYwVl8XbT_M2tt6blGfFqsc_cYJZaZ7-xibLlZ9tFZ5dd9dCTiuj4XMwdeuuRJ0h3ZEhgAcPs95B_3_BWh_0WnJfwI4zlQFndhduJ0gtPd62hXY8fJucT7to2_zs9zQJq8WqnFP1oUxMx208olJMEdl7JuXRwsfCwhnayMXDqgronYZlpBP8BslwZR_NJuXVT1_p4miX99SVznCIfpyU2SpxDbsxAIrbCW7qrmHknXLcJLRBBQvgQQZ27z1NeAllsWtDlOfzTIPS3eHjVI0rGluiOjFEbJsSZzH-yQq_ew9oR7jUS69h369y32D5TNC2cfCyKC5JMK5g7EVBIPxuORNHWBbSfi1La7_nTeh2kvK2TpE5ZdhXyv6WE3oMn9Gpa0TspQyCB66ytq--siuz2xFXg21bAyEdDTlzvAKX7llhyT-F1or68afGL3ksIDjL9QHe0i-UIFGOiYq4UqMze3vUakr3nPx7kndVZQKumUHDKHawkK4yvOBMzqSqbMiDYbsAJIjzvEQo2RWNb5L-jtTANefniw-gdg6KPZZc2h4FqfLJ4E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7dfd000d6.mp4?token=hWFWaahWyqwX0GNAML9LZQdrMIg5UymvjRcf6w0PLMBqIpMMg1eYTt5WoTLDgD4GM6CWNFjBK9RBsEvIotuLt2enfqRzJlNsNK1QnA-Vv_5MQfAyiubpnxX4UJYwVl8XbT_M2tt6blGfFqsc_cYJZaZ7-xibLlZ9tFZ5dd9dCTiuj4XMwdeuuRJ0h3ZEhgAcPs95B_3_BWh_0WnJfwI4zlQFndhduJ0gtPd62hXY8fJucT7to2_zs9zQJq8WqnFP1oUxMx208olJMEdl7JuXRwsfCwhnayMXDqgronYZlpBP8BslwZR_NJuXVT1_p4miX99SVznCIfpyU2SpxDbsxAIrbCW7qrmHknXLcJLRBBQvgQQZ27z1NeAllsWtDlOfzTIPS3eHjVI0rGluiOjFEbJsSZzH-yQq_ew9oR7jUS69h369y32D5TNC2cfCyKC5JMK5g7EVBIPxuORNHWBbSfi1La7_nTeh2kvK2TpE5ZdhXyv6WE3oMn9Gpa0TspQyCB66ytq--siuz2xFXg21bAyEdDTlzvAKX7llhyT-F1or68afGL3ksIDjL9QHe0i-UIFGOiYq4UqMze3vUakr3nPx7kndVZQKumUHDKHawkK4yvOBMzqSqbMiDYbsAJIjzvEQo2RWNb5L-jtTANefniw-gdg6KPZZc2h4FqfLJ4E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی مجلس: هر اقدام علیه امنیت ملی ایران و جبهه مقاومت با پاسخی قاطع و هزینه‌ساز مواجه خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/657501" target="_blank">📅 23:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657500">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔹
خبرهای داغ امروز را از دست ندهید
🔹
🔹
اسرائیل امروز به کدام مناطق ایران‌ حمله کرد؟ | گزارش لحظه به لحظه از ۱۵ ساعت جنگ
👇
khabarfoori.com/fa/tiny/news-3221360
🔹
پیامد ۱۵ ساعت جنگ ایران و اسرائیل چیست؟ | حالا شاید گره توافق باز شود!
👇
khabarfoori.com/fa/tiny/news-3221587
🔹
ماجرای اتهام تجاوز به یک بازیکن ایرانی چیست؟
👇
khabarfoori.com/fa/tiny/news-3221520
🔹
ترامپ نتانیاهو را تحقیر کرد و مانع ادامه جنگ شد: بی‌بی کاره‌ای نیست!
👇
khabarfoori.com/fa/tiny/news-3221325
🔹
جنجال تازه خواهران منصوریان با حمله به فدراسیون ووشو؛ خودزنی با چاقو! | ویدئویی از لحظه حمله‌ور شدن الهه و شهربانو منصوریان به اتاق ریاست فدراسیون ووشو
👇
khabarfoori.com/fa/tiny/news-3221407
🔹
ویدئوهای جذاب ما را در وبسایت خبرفوری کلیک کنید
🔹
http://aparat.com/akhbar.fori/videos</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/657500" target="_blank">📅 23:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657497">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
یک مقام آمریکایی به آکسیوس: نتانیاهو برای زنده ماندن سیاسی در اسرائیل نیاز دارد که جنگ ادامه یابد، و ترامپ برای زنده ماندن سیاسی در آمریکا نیاز دارد که جنگ پایان یابد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/657497" target="_blank">📅 23:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657493">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad56aba44c.mp4?token=MTTRqp2RrV9P-f2FpywSU3RhNH7NUOasVYhSMFkPfdzzwDPtMZAyaso33bPmgqVrTU6J1Se2DSEzLqU1Dff-N6t3KZluGJzlAhjNeXKb48b2JtytQtGZ-lK2jjgjX-iAKxfEQkKr1TaM97OFDDvzyq3_o_mcQkjgJMUoWeXpfgjI1u2m0ZimxopJk7IzMCxFNIcxYnxxftNtN71syQ11skChbzAP7PqoxjwjOqhxZJpgpYyrBggO0E3JbneESwz08WHtvjv9wGcNXm4XlbryiMvfqLBQHI_qyhWdVtL-NAu4aXDoh4H3r9FyFLkJD36qzLyBcPlEKkiXct7QDDdeXpIRzAE2zQ5o939LEyYf6i79drA-Go55cQIfjIokHhZlFv4i9_h1WTD9ruCDibHxcJ8ifja5seyURF9KkvSI9x7xS5AHxGUyZ8bbfQuw2CE7Jntq8_1TEJNWM6Ko1q9LUeF8_LR9orlKk_ghXFcDucTj2AJJBC-c2Rgse-7dQFS7r_-8R1OWx59LQwRJoc-P2kXQnsOd4HgUoRZQe_W2twWTqRVo1v72t1u0_HakXWtLEQnTYaYO9I-Aw3slZUt6Cg6hXmXWvloeAEYwQweGdXOGwsQ9WrzQj8BYTcibjGrPEl9GiplYFoiJgprgqLYofyWf321OIgrmJWezuRkNaZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad56aba44c.mp4?token=MTTRqp2RrV9P-f2FpywSU3RhNH7NUOasVYhSMFkPfdzzwDPtMZAyaso33bPmgqVrTU6J1Se2DSEzLqU1Dff-N6t3KZluGJzlAhjNeXKb48b2JtytQtGZ-lK2jjgjX-iAKxfEQkKr1TaM97OFDDvzyq3_o_mcQkjgJMUoWeXpfgjI1u2m0ZimxopJk7IzMCxFNIcxYnxxftNtN71syQ11skChbzAP7PqoxjwjOqhxZJpgpYyrBggO0E3JbneESwz08WHtvjv9wGcNXm4XlbryiMvfqLBQHI_qyhWdVtL-NAu4aXDoh4H3r9FyFLkJD36qzLyBcPlEKkiXct7QDDdeXpIRzAE2zQ5o939LEyYf6i79drA-Go55cQIfjIokHhZlFv4i9_h1WTD9ruCDibHxcJ8ifja5seyURF9KkvSI9x7xS5AHxGUyZ8bbfQuw2CE7Jntq8_1TEJNWM6Ko1q9LUeF8_LR9orlKk_ghXFcDucTj2AJJBC-c2Rgse-7dQFS7r_-8R1OWx59LQwRJoc-P2kXQnsOd4HgUoRZQe_W2twWTqRVo1v72t1u0_HakXWtLEQnTYaYO9I-Aw3slZUt6Cg6hXmXWvloeAEYwQweGdXOGwsQ9WrzQj8BYTcibjGrPEl9GiplYFoiJgprgqLYofyWf321OIgrmJWezuRkNaZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واقعیتی پنهان مانده؛ پاکستان دارد از جنگ ایران سود می‌برد؟
🔹
پاکستان این‌ روزها همه‌ هم و غم خود را برای توافق تهران و واشینگتن گذاشته.
🔹
حالا سوال اینجاست، چرا؟ چی چیزی پشت‌پرده این تصمیم است؟ در این ویدئو ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/657493" target="_blank">📅 23:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657492">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
آذربایجان حمله اسرائیل از خاک خود را به ایران تکذیب کرد
🔹
باکو گزارش‌های اخیر مبنی بر اینکه اسرائیل واحدهای نظامی و اطلاعاتی نخبه را در آذربایجان به عنوان بخشی از شبکه‌ای از سایت‌های مخفی برای تسهیل عملیات علیه ایران مستقر کرده است را رد کرد.
🔹
رسانه مدیالاین نوشت که باکو این ادعا را «کاملاً بی‌اساس» خوانده و گفته است که هرگز اجازه نداده است از خاکش برای عملیات نظامی، فعالیت‌های اطلاعاتی یا اهداف خصمانه علیه کشور دیگری استفاده شود./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/657492" target="_blank">📅 23:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657491">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز: اسرائیل خیلی دیر ما را از حملات به ایران مطلع کرد، اما من در نهایت توانستم دامنه آنها را محدود کنم
🔹
کشورهایی که با من تماس گرفتند بسیار نگران بودند و از توافقی که با ایران در حال مذاکره هستیم حمایت می‌کنند.
🔹
ایران می‌خواهد به توافق برسد و این اتفاق می‌تواند به زودی رخ دهد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/657491" target="_blank">📅 23:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657490">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53478ab0e9.mp4?token=CzwmgyD63fs7GBreiYIoL643_dl2GBuyt5-3YticvRFOBas068DwpK0kzWxFyPF98ZikFCSYsCEtP1AO3bFPj6KDLavanzOxyyqqhcRYDfyM5c70LhqnLSokWmS01ZyNpSlVPZIawYV3D_K3UoTygCruKHcVq8nDqwhJAyw3ou4eLOb-QoLUOGu-OkrqxrPBUboi_3zVqQWRe-poMsK1ic5_-dUcZXvaUnG642rnxVPs63WYwr06PB9AgYB0w8luRQFYKvnUkkv9PPJogDzVg1GBv5ObWmINoII2u6rVtCZb3Nitm7TXMRYskt0uPbeJRPSbTzbYyhEZPyy445Jhtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53478ab0e9.mp4?token=CzwmgyD63fs7GBreiYIoL643_dl2GBuyt5-3YticvRFOBas068DwpK0kzWxFyPF98ZikFCSYsCEtP1AO3bFPj6KDLavanzOxyyqqhcRYDfyM5c70LhqnLSokWmS01ZyNpSlVPZIawYV3D_K3UoTygCruKHcVq8nDqwhJAyw3ou4eLOb-QoLUOGu-OkrqxrPBUboi_3zVqQWRe-poMsK1ic5_-dUcZXvaUnG642rnxVPs63WYwr06PB9AgYB0w8luRQFYKvnUkkv9PPJogDzVg1GBv5ObWmINoII2u6rVtCZb3Nitm7TXMRYskt0uPbeJRPSbTzbYyhEZPyy445Jhtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بسکتبالیست زن آمریکایی اسـتقلال، مسلمان شد و در ایران ازدواج کرد!
🔹
"شیا رائل ویتست" بازیکن آمریکایی تیم بسکتبال زنان استقلال اعلام کرد مسلمان شده و با تصویربردار مسابقات ورزشی ازدواج کرد.
#ورزشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/657490" target="_blank">📅 23:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657489">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ms0FGx4cwjGD2mdW3yMyF-ZGf9UVNjCIiQehnyAyxVZE2ExMOiSI2OIXQOXDLe04dw44Grygg4DBR81VBekhOPWHD-lK7srVQTNkbg1-d-MHpgPR2cXrS_bThX3EKIR5vnrD4ELhv9ci0xnM4iOtDZIFwE3FaM_IcEFCNq_ScRoyMrzHYHJZrAY73KEWydjIyHdI4kUISDVr0t4XB4xFf6_9E0lQaeXI8NbplOkEaOGXUBZCa9VoZwUbripaY2CaK3mFfCGQn_gznjtfFJjK2r86UPITJhkDH6qB_FdN8XUX3uIlf12kO9cbzRDwTDH1BNLl0bKBJVj4I0IPfdTuBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جام‌جهانی فوتبال همیشه سیاسی بوده است | از موسولینی تا ترامپ؛ هفت نمونه از سیاست‌بازی‌های یک جام
🔹
جام جهانی فوتبال هرگز رویدادی صرفا ورزشی نبوده و در طول تاریخ همواره به ابزاری برای نمایش قدرت سیاسی، تبلیغات دولتی و ساخت تصویر بین‌المللی کشورها تبدیل شده است.
گزارش خبرفوری را اینجا بخوانید و ببینید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3221464</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/657489" target="_blank">📅 23:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657488">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/070d993c60.mp4?token=gP03gm-kv--piXNYkCcxSVC8VRvi8zrsHCVGjskwkOlN9S155fHh2uz7mTdo1k20ttRI4M1yD03Qsc95DzlyuuhQo166IxIgVoADNaacfLmtdKn9jn6eaaUjWVVBrYaJwbrHpg4SAvFJ8YUsb7WN2t_sSNMXsh0npnbSFZvkZC1rgkikDQk4BClWr13dLTVxFv3QRM9TuwUujP8QDsiDs5WO919BfEFSCYIhLf1lUHEMmJMBXSBZub-5VLoXHFEVq8a3Tir-UvjiyGyPXc0vRcdLgPZHlHTfXxdCv69orWK7owbNRMCaEZa4PHy4aWOmaSU7HBcvIZpl8RPhFRPq1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/070d993c60.mp4?token=gP03gm-kv--piXNYkCcxSVC8VRvi8zrsHCVGjskwkOlN9S155fHh2uz7mTdo1k20ttRI4M1yD03Qsc95DzlyuuhQo166IxIgVoADNaacfLmtdKn9jn6eaaUjWVVBrYaJwbrHpg4SAvFJ8YUsb7WN2t_sSNMXsh0npnbSFZvkZC1rgkikDQk4BClWr13dLTVxFv3QRM9TuwUujP8QDsiDs5WO919BfEFSCYIhLf1lUHEMmJMBXSBZub-5VLoXHFEVq8a3Tir-UvjiyGyPXc0vRcdLgPZHlHTfXxdCv69orWK7owbNRMCaEZa4PHy4aWOmaSU7HBcvIZpl8RPhFRPq1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افزایش تلفات زلزله فیلیپین به ۳۲ کشته و بیش از ۲۰۰ زخمی
🔹
عملیات جستجو و نجات همچنان ادامه دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/657488" target="_blank">📅 23:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657487">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
کارشناس اصولگرا: آمریکا قطعا وارد جنگ با ایران می‌شود!
ابوالقاسم رئوفیان، فعال سیاسی اصولگرا در
#گفتگو
با خبرفوری:
🔹
آمریکا قطعا وارد جنگ با ایران می‌شود و بارها آمریکا ثابت کرده که از جنگ با ایران خارج نمی‌شود و از دوره قاجار و پهلوی آمریکا به دنبال جنگ با ایران بود.
🔹
از صحبت‌های ترامپ می‌شود استنباط کرد که آمریکا شکست خورده و شروع کننده این جنگ آمریکا است و به دنبال تنظیم سیاسی غرب آسیا به نفع اسرائیل است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/657487" target="_blank">📅 23:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657486">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
اروپا تحریم‌های جدیدی علیه ایران اعمال می‌کند
🔹
اتحادیه اروپا در اقدامی خصمانه علیه جمهوری اسلامی ایران، برای  نخستین بار با ادعای نقض آزادی ناوبری دریایی، تحریم‌هایی علیه ایران اعمال خواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/657486" target="_blank">📅 22:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657485">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebda6e9ef5.mp4?token=XVu_wVG4QlKATQTKOGu2yV2v7hNW5uRRWnmdj08g9dCJRwg6M6iOHb78O8iKAFHNOBBm2LoSei7O8HYb2y5_U9PLsSVGsXcSJteX4fv0WaHHfeoY-vH4PcUIxAmUFdtCmynRP8zb8Y2rwyISq8yFCm5tJW_z07eBS6VbxjXnv5rVlHdkHTPznOo3f9z8-H8VinmfWnXjNrJGZjWGtZIi4Lr_aPwwnJDglu23mSrfgK13PSHpVF1FM-eJr4ucL4cudGRJCsPPhrEtAiuJx4sn-68zzeIEEg_6N8O1oKtxmhm-_qaMQ1kVg1MYIOGvVM-1IZ3gML2mAMm3iQHJFFUesw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebda6e9ef5.mp4?token=XVu_wVG4QlKATQTKOGu2yV2v7hNW5uRRWnmdj08g9dCJRwg6M6iOHb78O8iKAFHNOBBm2LoSei7O8HYb2y5_U9PLsSVGsXcSJteX4fv0WaHHfeoY-vH4PcUIxAmUFdtCmynRP8zb8Y2rwyISq8yFCm5tJW_z07eBS6VbxjXnv5rVlHdkHTPznOo3f9z8-H8VinmfWnXjNrJGZjWGtZIi4Lr_aPwwnJDglu23mSrfgK13PSHpVF1FM-eJr4ucL4cudGRJCsPPhrEtAiuJx4sn-68zzeIEEg_6N8O1oKtxmhm-_qaMQ1kVg1MYIOGvVM-1IZ3gML2mAMm3iQHJFFUesw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
ادعای شهربانو منصوریان با انتشار تصویر دست زخمی خواهرش: رئیس فدراسیون ووشو با چاقو به الهه حمله کرده!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/657485" target="_blank">📅 22:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657477">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cIY-qH31K0g9gjKP6iHzhm9ZPDw6VZ4FrEzsCFkV6xzINihRwKjVBuJNzB4jbct-BnrejiCoWQ76BmCIwkdBYRX-jHlglhpj2HKFPr6AbvlsCH4RwNGyzS_So35AbFfeyX9K8lX-wWMqOQ9ERgM7Nm3GL6rrz8vroDtgpOXEpICSvpUNbWJHHB972HAMerELyQ9UzcIoMYd-WgfyKV4OiryUzYbh4ZFLwBEmBtAi--qd4o1ON18hjE6ycfGlGkb2nq0xMzgfaVaIVAqXEpCLNlyUGx9no_1JWLPp1EoNL2NfErOhc0a_h_unxLxt2L8loNoeOL_ty-BzVnjddFEROw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DQDZa5uTUwxu0yp2y00-p3bNfC-IjQzaQ7y7SrxSGmm7lBZyevLblyJ7alS_K7AzSY_CMXzU8LND_esgEo2FYivICO-CPpNyZ3-7oMaQC-NkDvpgDp7iPyC83lnVVVsGF0hQDTjwSU5OjIqflv92EzvlCUl7SJTZDvo1P-ygpUW9oeRei5killF5lByns2gYG13zvOv6B7p_37hMhL82lSSQS9buZM5UKul5R3dssRuUlrbHZWhOm0gVXXA71lYhOznTn8cKUxqgeyDvIwmLMihKsvTwwtw447mtd0689-8K2xD4UUH6gz0aXosjNkJw7Dx9kMHtnV-Vloms3SYZiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n-8URXAEgBtg8MZFEfsCY6cy6EE7GDR_afSZEsb4ezu6T8SFiE3VMouxwmnJZcpmDMi0jUC6VGAeRL-aE-_5xo5FhGFKR4H6wPCQcwQkfxkPiHnPm5XfQHq5x4MUaOYdp_oiOT5yujHc_bMA6s5pgsLzThPpFGIrupcPQHXOpzeE1LuGsVWIDKIL2XMrH3Z0LqEJ6dhNVHzooR_4W-CkZm-b8IiNddVPzqKNSEPi8uLMe5zEdk9E5qP2e1R7nNFg9fxgBet_i3MaOftUmgzZ8HWfG6MVaUWz1nboP7QvpTbZJeo2UKw2q9YzfP7SGMefOVY90D63p_ZsTPeOR-pJrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t9kAIu8vM-gjF9Isi5QJz-rX62YilW7cBimq-qTvJ_fH9dVSPC4l4IF5g778EBoGWag_lK1_yEgBS8mhKy-AWZvquRxOqTIybP2VfcMUFZAXUmTECfMuAMLqREdD5XRsnhMuFVdagtQgZTRx8jYpxuxqtv1a6-tj5w29aMmsm5w3zxx2AQrpcw8JOFvik4Kh67btfnRZun-PixBGjdLw_NMIvTRHYucTsoMT2ZThGm6dUm7GvA5EaQa1TGzhY3v7xXqpx3b2hOILshGGuIqOxu6nz2iBBz6tlkuydg9Bejx4SibCTNubdYiPOV-ajmnOK_E31DQPcTodeB5VPuK8zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oq5gM7Nkz_irj28vwkLU_x2olkebXCO-WFU7yuiZvJCAzGSvYxNW6lBDnJYTRfeDD0TVGvldTlVTJ64u4236vEOKASQ0-DEINbGHNxZ1kEoinJ7TfByXwnAm3SQNjyF-Nf7drPtwE0jHUlSPH9YgHvoYPJOqlNgnnViV72Na4Teh7SgKpWxxV-r0l_UuoMjpC4ZpiQTa5teoRrQLp4lfps8SvhUZzea_QPOgVAO54ge-rL3qv8NewZXFh-nlWnIVFa2CcqLKgGdL8rRjoXg1GefF9-P3CIXLiQzsR6xvbnopqDM90hmxjZqpJvr-IZN0lu8eh6rguCLZfogFN6nCvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fWOx716R9_K2bfPkKC6MLSC79aGdnBhPSgZszphA--OsR4Aaq9MI1hXd4D3I6OXD3bwdzMLR-EiIALtPkcXznCwGns8c1Lb7ayH4Zd-MpiJ7013HpesQGHpQmKuQvEyC2InZ626Y0uDmPazOFVXc8SE3zAcPyfBkq6aeQsgk93cJMfegetxw_CMb_TzOgyw0n16ysmLbLFlDsfGyTndnhzaU65xsi9PUlymLa6GJCK0uOw6Pov5qVYbRaoewDe8GDlZWmCRHHSHJRX--Io5LL6-d448SMZwi7x2FUCpnKjb9_32x-gOiGwu25Oi_uD_ac1Y1ROPfBnXOYyrkYVe4nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r2d8W9i7QK8QCrcrVhqqcR6Qzq-9_mUJqBeXnxh0VWqNTMBe7R7n0OPkgJPw8BNoc7XGGrGVa8_bJsiM1f73hG4FtSHu2KbAH4ehamLNt8-7ci0gROlwcM2yVBfjg_5BSl7_XPGB2EMTW_x_ckB1wO0f0CuCxQOVi9oLN_wTQscUs6xkRzkAwApvWk--C3Ov3zDqCUtOYAgtCR1aw-tPMyWAeJ5VmBULu3UlMac8QsH2PxDqRaGtulMgwcfKKxKELTi29iL6YYn_GZvsM_vOdCZAPQkj-SYb98G9zZ90Ho75qZGprJNJutpI8_31I-ENDM4qXkhnvc4Sof0L26TcEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QSJ1ltNWaqhhFKqrVu7QqgenycXRXj2nnKxUGvICeiG8EI6neyyTIxziA_EN4kaLG5XbjzBexfp7Oie22ibObsIaEItNdijT0DbPo8WE8s1k9oU_hhF5Wl6cvGQ9rj-w7YkvyvfqILeAK_Q9eH4jB72tG_XvQnAAKxH_FwmaSqM86IntjdecVRZkHTH3_7Lcqx6JLmzLNqYvvcenXki2O3z1fhN1DxpJpOjJkvx1XsJUnMFG8vnKWP0SGhSEe4YCbjTQQmAa20HqcYWRBESjRd7__wkXcVPs0OJWESfTp5imL001EpjZAUmQkmopx1X6tyPd-uVcbojAjsNWleuoLA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💫
روایت برکتِ همدلی
💫
هر روز، به پشتوانه
#همدلی
و همراهی شما مردم عزیز،
#هیات_قرار
با ذبح ۳ رأس گوسفند و توزیع گوشت قربانی میان خانواده‌های حائز صلاحیت، گامی در مسیر حمایت از خانواده‌های ایرانی برمی‌دارد.
ادامه این مسیر خیر، حاصل اعتماد و حضور ارزشمند شماست
🤍
💳
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇
@Heyate_gharar
شما نیز میتوانید در این کار خیر سهیم باشید
👇
5029087002135690</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/657477" target="_blank">📅 22:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657475">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14432d14e4.mp4?token=LsTALVonqhD7PjBA9l64WQq2eaYOP64VTOStYCN_K20i7boQwQB76aT-9CvNGHRkNiH2GTgsdqDTVITCyJku9IUzgvUbl27iOmmhIE621EFTs5X7qAifZ6y-zimtVcMkTWYZCQlK3ObeH3my4JbCoJSEh3iqFmiooP6H6v0QKa4Z3G5-WTZ9iPqXIJyDrh4GamrUxpi6Z1PMg8fzVy9KwCQ2ULdguB5fEDZ22CGcZUorCpUs0BUwL0yC3-mq11sl3KNIoYLY6qobFP-UA__oVBFrBYDKFaQz1VBEp8hcIUJzd-7KV5AWN4-VMHzyye0Okd9xGDB9ODJRGU89gbTM9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14432d14e4.mp4?token=LsTALVonqhD7PjBA9l64WQq2eaYOP64VTOStYCN_K20i7boQwQB76aT-9CvNGHRkNiH2GTgsdqDTVITCyJku9IUzgvUbl27iOmmhIE621EFTs5X7qAifZ6y-zimtVcMkTWYZCQlK3ObeH3my4JbCoJSEh3iqFmiooP6H6v0QKa4Z3G5-WTZ9iPqXIJyDrh4GamrUxpi6Z1PMg8fzVy9KwCQ2ULdguB5fEDZ22CGcZUorCpUs0BUwL0yC3-mq11sl3KNIoYLY6qobFP-UA__oVBFrBYDKFaQz1VBEp8hcIUJzd-7KV5AWN4-VMHzyye0Okd9xGDB9ODJRGU89gbTM9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از انفجار در مقر گروه‌های تروریستی در اربیل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/657475" target="_blank">📅 22:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657473">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
رئیس‌جمهور لبنان تاکید کرد که کشورش به‌دنبال روابطی خوب با جمهوری اسلامی ایران است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/657473" target="_blank">📅 22:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657469">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدیدرس</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H_e20kZc7TYICOBGY3ELjetnYiZEQvFFS16R3dShhLQm9BsO2VjXk-dYVFHotiMSITTL20JLujERQXA20Z_I5MDXpfSus5Vn3TvsQGrkPIwxSMgJuBvVS1nnr6mDN1eKU0OHlhbw0GSLMJuM-s_Q8lREF7sE31nTge5i-Pv3jIz46GNz9xRzhN6UPeLAfKffLF-1QA9NdOe2Hjdi4iH6K0EZ_R6Zpg1pxDVzmiD-jKE_S7ZPCcJyBmwtMZXFxKCxegFxrs6O_GBCOQHwiZofra0EKVdFhYTIENUs8ZWX3Qygvrzlfv1vn6h9wmqaFKA7QuyacIpAHpY2LBsuQjWH7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q8LbOMrvblhkYSAx9--1iSzcyTnP_sLxjpRuLPy7nADNb9YKAJnWeDJvyiuo0zIPQxBwVsqKSOAYnFEc45fogukBBLOUeUgwJwdOFfjWBNQ8TJZy8m8wE460eZaM6Lb3FmwO_8staaTtveF75jprPTWmPEPccgjgb9cRNCmpdBasma0lN8ay0q7RlLniOkokSbPh71pakMVOw08T6roxmyb0Xt4OMieLaTq-HHyMIJtM3O6z1s-cd6Ht1oaI7hgsPbxEFI-oxx2ZW_T1F4kerUS7yuicezFnpLQ4p2gMZ6sB_N6YllICkW0M9cdcAf3IW_DZYwFhYK044V88STMxpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TYIc2X-EZtHkjlVQbLpOh1S_3mQGPBoyKAkIV7jXZXVMu4ICral59rYBnMv00Ux5YAju7u4qZcBX9aZxNop9jDfHJGTD8yCqQ9usEZB9-isj8QkMtoLLwQO05poGtlEpxoM9JWT9eHgMufidZqxX8rGLWgTbZ1g2jdc-B_kAnooFlc7m8NUJMol98rfrQcC7JYIUpKylPWRHkZytEUZP6oxVJpPc0xsNz4Q4ZaTaKnpQFd_P14cjr7jvR4hjJ9df1KUAk9akfQe7sKCvtIkujpSMuqnPV586daIjc7_tFamy3LzZve61E35_6PY9kxH9ejplHb8NOTTqLIM3cH0trw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OvKf9u40RU0_DkqAE4CNqOFAUctd3awch7K4tmaqutZVpeZEQ53AteJISQuUbc00ct7tQMMpXPYfPUbI2smKSbUrr2vRa6kAxSqhwWIzvZeLQunWsXuCOl3Pf-du30P6PR1INuTLQCjH-3t7yXK4zAzAg2NjRlSh1GhNLJ8TXNomIiUhszv4SY33cbRKtOVxFrAl3kwB_eK6OavMnrNvcVIJsIprPoFZc7j8KZF4t-kUVZJVm3rWAT7jjQTfVHbEUmtkPK__XQbXvPO3j3zRtLKGDSgOxeN-1kIuTn0OXXaEzDxUFk9DRN-gtTng8Ie9nHM549se65gXulT0y5WypA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔻
جریان معاند و بهره‌گیری از تصاویر و ویدئوهای جعلی یا قدیمی برای دستاوردسازی از حملات رژیم صهیونیستی
🔸
آنچه در وقایع امروز مشاهده شد، استفاده گسترده محور رسانه‌ای دشمن از تصاویر و ویدئوهای جعلی یا قدیمی با عناوین مختلف بود؛ اقدامی که با هدف بزرگ‌نمایی و دستاوردسازی رسانه‌ای از حملات خود صورت گرفت.
🔹
بررسی‌ها نشان می‌دهد هر چهار تصویر و ویدئویی که امروز به‌طور گسترده بازنشر شده‌اند، متعلق به وقایع گذشته بوده و ارتباطی با رخدادهای جاری ندارند.
🔸
در چنین شرایطی، خودداری از بازنشر این محتواها و قطع زنجیره انتشار آن‌ها، مهم‌ترین اقدام در مقابله با عملیات رسانه‌ای دشمن است.
🔹
شبکه مقابله با روایات و اخبار جعلی «دیدرس» از مخاطبان خود درخواست می‌کند در صورت مواجهه با محتواهای مشکوک به جعل، قدیمی بودن، دستکاری یا هرگونه ابهام درباره اصالت و ماهیت محتوا، آن را برای بررسی به شناسه
@Didras_FactCheck
ارسال کنند تا توسط کارشناسان مورد ارزیابی و راستی‌آزمایی قرار گیرد.
🔻
شبکه مقابله با روایات و اخبار جعلی
✅
دیدرس |
@Didras_ir</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/657469" target="_blank">📅 22:38 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
