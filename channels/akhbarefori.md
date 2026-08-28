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
<img src="https://cdn4.telesco.pe/file/Lyd0c-CriHUXK2VkYFKWyH4p3wY1vPpPrCzXxrUg0FAyrq0mCX6tfHTAImzgXE-2FyviHljmKUhoN-ZsedfAzr6PD-cfbQEyXoMsIVYEh03ASEV9aNSdaT9Bmo_rP3BxlOjNP1YjIWkxSPgRSp9c_XndbLyyGWJEiCneMlqyRWn1o1bZbONK9vgdwqLJrNNAKaDHurS8P4XC-2RqRwJacfFTLUxGVdy6Ed166dhNpjlo5DfyzXLqMVCDx5fK46A5gM0WbwcYtaNVwFpgzgFURzytCZwpNQCpY-vkLeqW4tzktsM0v5msaLfNL6TtrRSM7gNHFXb-LDZk1AuT5d5iqw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.37M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-07 02:49:00</div>
<hr>

<div class="tg-post" id="msg-685151">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
دستبرد ترامپ به ثروت ملی ونزوئلا؛ غارت ۶۵ میلیارد بشکه نفت
🔹
دونالد ترامپ، رئیس دولت تروریستی آمریکا، در جدیدترین اقدام خود برای تاراج منابع کشورهای مستقل، مدعی دستیابی به توافقی با ونزوئلا شده است که از آن به عنوان «عظیم‌ترین معامله تاریخ جهان» یاد می‌کند.
🔹
ترامپ با افتخار اعلام کرد که وزرای امور خارجه و جنگ او موفق شده‌اند دسترسی واشنگتن به بیش از ۶۵ میلیارد بشکه از ذخایر قطعی نفت ونزوئلا را تضمین کنند.
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/akhbarefori/685151" target="_blank">📅 02:31 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685150">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
وزیر جنگ آمریکا در اندیشه تصاحب کاخ سفید
ان‌بی‌سی:
🔹
پیت هگست، وزیر جنگ ایالات متحده، در محافل خصوصی از احتمال نامزدی خود برای انتخابات ریاست‌جمهوری سال ۲۰۲۸ سخن گفته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/akhbarefori/685150" target="_blank">📅 01:45 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685148">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RANkznHi4COtf8dNXi2k-SE_0kpYAT_8C3nwuwZxlYUIlcqk2FqOVjAgOajyXY1inCzvTZBmUKheIB0QyvfxOQvQgWNSsE9LgObyoHUmlpjWdzXT1ai0NGgkmA-o9dI_ullOv7J1oS_232E8K1-Cw-6-sDRovn-IOIqrIlldypxf2-MRP8eXAi8R5Qw374d46PkSpebaG0OMKgC3oBTScPYH2RxC_IZsLAQU3Jg5hA5VpEC4qV3pTM-6GrKQ8GvmNLZ_58I9gDrbwVQQFswd00raKHAneN5QeUYvgY_atTrHLR5ogdxaW2bsDpuwuMI7_8shi0qU5UWj66ycg-FLnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرمان قاطعانه
🔹
رهبر معظم انقلاب اسلامی در پیامی به مناسبت هفته دولت ضمن قدردانی از اقدامات شایسته دولت به ویژه رئیس جمهور صادق و دلسوز فرمودند: قاطعانه اعلام میکنم ارتکاب هر آنچه به ضرر انسجام اجتماعی باشد، ممنوع است. ایشان در فراز دیگری از این پیام فرمودند: هر دوگانه‌سازی موهوم از قبیل جنگ یا مذاکره، وفاق یا تندروی سازش یا جنگ‌طلبی می‌تواند به مردم عزیزمان خسارت هایی بی‌واسطه یا با واسطه وارد سازد
🔹
هشتصدوچهل‌وششمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/685148" target="_blank">📅 01:29 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685147">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b99343099.mp4?token=vNxTl3ElvwVQ3OhqCugYa-eau-pZFtlkkE_jumH4Xj06Kssz3cAWuNglHSR_Hm7e6_U00Py4y3cEy6IoHyCUY5m56wYZteR3Py_x9GQ8bBdI3tiBey9jy35Hwd_kyyOmvk_ZA0WvsA-qzo-nAGi0tIaP68RqZdUkDm9Y5eY6OiY_If0eqxb2WmC2grnFXB43ENLjZih2cMxFdt5KZLuyPkVginox4ddqL7wRQ0f0JAN8FoGAZKouzsbZHy4qT6E8gtuGrfp58S4c6DR_juyVGl0OCurxaz_XzBTfAg5GI53_sxfZK4Ax_qNyu4wpd_IvZki4wj_hejpkiicXXd_WnIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b99343099.mp4?token=vNxTl3ElvwVQ3OhqCugYa-eau-pZFtlkkE_jumH4Xj06Kssz3cAWuNglHSR_Hm7e6_U00Py4y3cEy6IoHyCUY5m56wYZteR3Py_x9GQ8bBdI3tiBey9jy35Hwd_kyyOmvk_ZA0WvsA-qzo-nAGi0tIaP68RqZdUkDm9Y5eY6OiY_If0eqxb2WmC2grnFXB43ENLjZih2cMxFdt5KZLuyPkVginox4ddqL7wRQ0f0JAN8FoGAZKouzsbZHy4qT6E8gtuGrfp58S4c6DR_juyVGl0OCurxaz_XzBTfAg5GI53_sxfZK4Ax_qNyu4wpd_IvZki4wj_hejpkiicXXd_WnIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر تکان‌دهنده از طوفان ویرانگر در مالاتیا ترکیه
🔹
ساعاتی پیش، وقوع یک طوفان بسیار شدید در شهر مالاتیا ترکیه، تصاویر وحشتناکی از شدت قدرت باد و خسارات وارده منتشر کرد.
🔹
تصاویر منتشر شده نشان می‌دهد که شدت باد به حدی بوده که تابلوها و اشیاء سنگین با سرعت بالا در میان آسمان به پرواز درآمده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/akhbarefori/685147" target="_blank">📅 01:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685146">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9170b3a64e.mp4?token=DU1OXWmU0kY37Nhcjbu2Cjgk60pAORQxXi6CQVoTmiQDYh4fqrXdpfiBNYdK0UOSok9ZwMf1QQUjVSILZw76I_mTdXL9XecFJUehRPoJmJ1Z1OdK6k_ek-BvfgmiGVDOEN89d81zlFe4sHrfouBCtuDFAwzy7cKrRcaLfZ3s_BUsGz0xXzZdkP51o3dbTm-xUe6BknwSIP3rzl9eNy7NvC7ouufBv3lZAU5v92Ug-kPfjhKWnClF0eK6D5e6XKCH3ISQrHP4VMziwH-xth-4edwIdPirKLazPDlnKnUzTHjLdxUedgUk8I7kbVhCy70HrnUk6ZHRneYXTcYZOPbNKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9170b3a64e.mp4?token=DU1OXWmU0kY37Nhcjbu2Cjgk60pAORQxXi6CQVoTmiQDYh4fqrXdpfiBNYdK0UOSok9ZwMf1QQUjVSILZw76I_mTdXL9XecFJUehRPoJmJ1Z1OdK6k_ek-BvfgmiGVDOEN89d81zlFe4sHrfouBCtuDFAwzy7cKrRcaLfZ3s_BUsGz0xXzZdkP51o3dbTm-xUe6BknwSIP3rzl9eNy7NvC7ouufBv3lZAU5v92Ug-kPfjhKWnClF0eK6D5e6XKCH3ISQrHP4VMziwH-xth-4edwIdPirKLazPDlnKnUzTHjLdxUedgUk8I7kbVhCy70HrnUk6ZHRneYXTcYZOPbNKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس‌جمهور: من نمی‌توانم جواب خدا را بدهم، اگر نتوانیم مشکلات مردم را حل کنیم ولی درگیر دعواهای سیاسی باشیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/akhbarefori/685146" target="_blank">📅 01:07 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685145">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6324af0fc4.mp4?token=SVMzYeBRGDSX30eYEWIXuviFaVesjXjWo735g_eVsipdbY8afdYll2uFUvU7lFYONzTdEckDDKWJi9pzs2hN4Ayj_m_3S3WxUpPZqml7DDnz4J8odK2_0tWEUVvZUYHvv1oIK2-cJ2zmZMDXeogu8wN3X0qfU_hYeaNMkwUVK9IqXEnlnEHNwoEx9Ul3DvIXrE5UAv0Ud2_oRLgLNWnLYghTFGNR44LeNzSUDF16LzuxRM9ygCMxSOgxpan7MpriYaVMHbvz3jg7XEFIyItA2Zuf4_VN2Z7kivw8AXdtMwrfhJBYvzydvN3vk5J-qPJzTNgpobe4srLvA1lFoIPA6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6324af0fc4.mp4?token=SVMzYeBRGDSX30eYEWIXuviFaVesjXjWo735g_eVsipdbY8afdYll2uFUvU7lFYONzTdEckDDKWJi9pzs2hN4Ayj_m_3S3WxUpPZqml7DDnz4J8odK2_0tWEUVvZUYHvv1oIK2-cJ2zmZMDXeogu8wN3X0qfU_hYeaNMkwUVK9IqXEnlnEHNwoEx9Ul3DvIXrE5UAv0Ud2_oRLgLNWnLYghTFGNR44LeNzSUDF16LzuxRM9ygCMxSOgxpan7MpriYaVMHbvz3jg7XEFIyItA2Zuf4_VN2Z7kivw8AXdtMwrfhJBYvzydvN3vk5J-qPJzTNgpobe4srLvA1lFoIPA6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: به جهان نشان دادیم که آمریکا و اسرائیل قادر به مقابله با موشک‌های ما نیستند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/685145" target="_blank">📅 00:56 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685144">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d6d2108a7.mp4?token=p21JwKRVOS_linALRuOWdm1et1OqwiCnd2Q9au9d81XFMbKs5_FWGVfJii0CGtOljLdwwG3jc1WtVQ4yfhmsgZny3Z0mo_ps5zKvQlNogWZT7U_iWcwd_EMsMGJC_PnrebKR-HyE6yBIERAHF-cV5cxW4z9imsxEyMFCHGbNQ2c-JEKcftQhdl2E0GY0uLrhH0ldpckq8ROKHPUbl4wf8H_qmffaa_ayA_JKtfb5Gydfxi7CbS6gQiWZa3bzdEcE54DpNPgsAWIwQIw4Sefoiwwf5gyZm4ROByUMJG6jZ1XA0bLndwI6AINT6yiG1CKxjGRBpPdNkeRoEMwEnonNQwk9zVR_KvGmC_XZOtXoevUAtr1FSdogo1rQ0-65qAweZKA-rxSg22KkeOjMA3U5kPD7O3U9a9FVbWMrV6CQVT34K33oYrh-dGOCOCB4BmwTh9w__QnRq4wq8Ym-TK5cJK_bUZygw09cLXNs1K2F5QFqwQFVLmndSa9AdFxiO2Rusa9Ui2h0f3DWK6dHQ0E6DgD7uuxVGh-USCaNwT_9Nz7gFe69UkNY3qk5hrxHclVoij8IGfPJ9QQMZPMAFRnKMWeZnwMW52Hlp66sugVArgik35dj-Xn5k4fl4DHkf8sME3ayKJLWd9sgePAy1BOXfgvcPAHoRIBS5GaSegf7Z8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d6d2108a7.mp4?token=p21JwKRVOS_linALRuOWdm1et1OqwiCnd2Q9au9d81XFMbKs5_FWGVfJii0CGtOljLdwwG3jc1WtVQ4yfhmsgZny3Z0mo_ps5zKvQlNogWZT7U_iWcwd_EMsMGJC_PnrebKR-HyE6yBIERAHF-cV5cxW4z9imsxEyMFCHGbNQ2c-JEKcftQhdl2E0GY0uLrhH0ldpckq8ROKHPUbl4wf8H_qmffaa_ayA_JKtfb5Gydfxi7CbS6gQiWZa3bzdEcE54DpNPgsAWIwQIw4Sefoiwwf5gyZm4ROByUMJG6jZ1XA0bLndwI6AINT6yiG1CKxjGRBpPdNkeRoEMwEnonNQwk9zVR_KvGmC_XZOtXoevUAtr1FSdogo1rQ0-65qAweZKA-rxSg22KkeOjMA3U5kPD7O3U9a9FVbWMrV6CQVT34K33oYrh-dGOCOCB4BmwTh9w__QnRq4wq8Ym-TK5cJK_bUZygw09cLXNs1K2F5QFqwQFVLmndSa9AdFxiO2Rusa9Ui2h0f3DWK6dHQ0E6DgD7uuxVGh-USCaNwT_9Nz7gFe69UkNY3qk5hrxHclVoij8IGfPJ9QQMZPMAFRnKMWeZnwMW52Hlp66sugVArgik35dj-Xn5k4fl4DHkf8sME3ayKJLWd9sgePAy1BOXfgvcPAHoRIBS5GaSegf7Z8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دلیل اجرا نشدن طرح پزشک خانواده از زبان رئیس‌جمهور
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/685144" target="_blank">📅 00:51 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685143">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b28c66f962.mp4?token=SygC8-CWQX1si0buHYkwboavECxbRRfFLAchcOcqeB_kjQFj0Aw4bJtbla630CB3IlTSvtlpo9vbeeuvGlb8IQP_mHXOHIEDg2AlmclTFwsKF20Gz40kiGZ32qq_xogaMuhBCuK8XxoW2Q290xVEoIx4vk5p_OjQqi3GU2HrsUjcWlqj-sv73ULteuXUAaq3F1eVr2fmtFRnrqlW4FY5n7ZMYNqK0ULgnHoKCwhqUFJzUn6niizhwIaQKn07aTSKe4z7l1ahCA3-45Gsio5qveyMzXP71W9KDZfva4IzlE3KcPrC_ufJePVkpy0UsZeS4PmWLAV3L1nxdS1-kZ86EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b28c66f962.mp4?token=SygC8-CWQX1si0buHYkwboavECxbRRfFLAchcOcqeB_kjQFj0Aw4bJtbla630CB3IlTSvtlpo9vbeeuvGlb8IQP_mHXOHIEDg2AlmclTFwsKF20Gz40kiGZ32qq_xogaMuhBCuK8XxoW2Q290xVEoIx4vk5p_OjQqi3GU2HrsUjcWlqj-sv73ULteuXUAaq3F1eVr2fmtFRnrqlW4FY5n7ZMYNqK0ULgnHoKCwhqUFJzUn6niizhwIaQKn07aTSKe4z7l1ahCA3-45Gsio5qveyMzXP71W9KDZfva4IzlE3KcPrC_ufJePVkpy0UsZeS4PmWLAV3L1nxdS1-kZ86EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: در این جنگ موشک‌های ما امتحان خود را به خوبی پس دادند و به خوبی از کشور دفاع کردند
🔹
یک نکتۀ مهم ثابت شد؛ هر آنچه در داخل کشور تولید شده بود، بهترین کارایی را داشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/685143" target="_blank">📅 00:36 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685142">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cb44ce39b.mp4?token=WuKuCAhVLqxUNwkgwRu70CPGiSMhtDJAvoVnRXiG4huNKF6SMclK5CvB0boblSHYOCE2VfF58AViqFL6veh-L19fYCWdxFYw9WtGgVaw4LVUZFJZwSxC-GykltIUbP-X76hiMPMarPF29Jsvxwmp7-y6YVoVVFvd9efLqj7_XOaULtfyhiJ6KzyX8JOL48NiwaiHmSR6P9Fr9vxSuS59JI78Ymnjz8QkP4D2T-DC7FUARvUiTRhkmy7VnbF9D1rrvQsNm4JIurFMN-CdD480ONCUqVVhRz_N46DoZrf74qs84aIEtcrXdThTyC8k3vLNJ7it5B4tU5doiSqaDGRmXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cb44ce39b.mp4?token=WuKuCAhVLqxUNwkgwRu70CPGiSMhtDJAvoVnRXiG4huNKF6SMclK5CvB0boblSHYOCE2VfF58AViqFL6veh-L19fYCWdxFYw9WtGgVaw4LVUZFJZwSxC-GykltIUbP-X76hiMPMarPF29Jsvxwmp7-y6YVoVVFvd9efLqj7_XOaULtfyhiJ6KzyX8JOL48NiwaiHmSR6P9Fr9vxSuS59JI78Ymnjz8QkP4D2T-DC7FUARvUiTRhkmy7VnbF9D1rrvQsNm4JIurFMN-CdD480ONCUqVVhRz_N46DoZrf74qs84aIEtcrXdThTyC8k3vLNJ7it5B4tU5doiSqaDGRmXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک انفجار بزرگ در کی‌یف، در نزدیکی بزرگراه ژیتومیر، پس از حمله روسیه به یک انبار مهمات اوکراینی رخ داد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/685142" target="_blank">📅 00:25 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685141">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cb2b55416.mp4?token=ojAMTa70htpZp5x_bAHRBN3AU_E3-zUFdHK3kIp35xB4UFaErxzKjQdzSsk__Gk4AY43AkWqZb9F5S9xyXr1za1Cu1z03usQUZvJtNYGdPXa8R1I6-8m58Vvflcg0K2PnscBEuOtP_pOIcy9zIx-zE_Tu41SYWZ7L1tAyL1LuqQvAIQrj-sc3Plw0g3KIXM5EA36q5mIVXpAWaMrFaGzkznQgDd4YSIRsZ9cLMYZ2c1KyFO_wIr9fIfVqQL2HnfGgW717TA2HPPsZgjScERJJ6V-GsGVPV6iOMHe3GPjO7ZZXH-IAtR5uFDi4agjkkhkMzukH3doz5r598N_Zd08G560E37WfIzvxecIjTEKSgZVEMgM_sgK47wvX9f_fRZdgaTWwOxA0EpaEVW6-76_xhKOuirCkK1bArZZQXv3AYngMHJgfTu6k8w9qiR60MkOcom0qJo_vzkwem8ZaaOBQd0TypGoTm6xP6-nG0T3_OpUpEv4bbmMJSeZdjP-jG7_U8jU9y9Wa0KvCypQqtNUECD-pSDEp-vieHjjOhdZ50_Hi7L6DKA5pUxE0W3Qx_TbyhIo4bLseMpdWqvzCSILgqK4b_vtPZjIH3_i1EELSAK2iDkSLlDk42PT34JmThjIQqIR0LdLEuRCMUfzsOIsI1DIzuMmpCLt2u5hmHTxqSM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cb2b55416.mp4?token=ojAMTa70htpZp5x_bAHRBN3AU_E3-zUFdHK3kIp35xB4UFaErxzKjQdzSsk__Gk4AY43AkWqZb9F5S9xyXr1za1Cu1z03usQUZvJtNYGdPXa8R1I6-8m58Vvflcg0K2PnscBEuOtP_pOIcy9zIx-zE_Tu41SYWZ7L1tAyL1LuqQvAIQrj-sc3Plw0g3KIXM5EA36q5mIVXpAWaMrFaGzkznQgDd4YSIRsZ9cLMYZ2c1KyFO_wIr9fIfVqQL2HnfGgW717TA2HPPsZgjScERJJ6V-GsGVPV6iOMHe3GPjO7ZZXH-IAtR5uFDi4agjkkhkMzukH3doz5r598N_Zd08G560E37WfIzvxecIjTEKSgZVEMgM_sgK47wvX9f_fRZdgaTWwOxA0EpaEVW6-76_xhKOuirCkK1bArZZQXv3AYngMHJgfTu6k8w9qiR60MkOcom0qJo_vzkwem8ZaaOBQd0TypGoTm6xP6-nG0T3_OpUpEv4bbmMJSeZdjP-jG7_U8jU9y9Wa0KvCypQqtNUECD-pSDEp-vieHjjOhdZ50_Hi7L6DKA5pUxE0W3Qx_TbyhIo4bLseMpdWqvzCSILgqK4b_vtPZjIH3_i1EELSAK2iDkSLlDk42PT34JmThjIQqIR0LdLEuRCMUfzsOIsI1DIzuMmpCLt2u5hmHTxqSM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درگیری خداداد عزیزی با خبرنگاران یزدی پس از بازی با چادرملو
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/685141" target="_blank">📅 00:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685140">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FY47LK3v6tBvOzo2zsDBa88jDbeSSVc-9HyklJZYWmcJXp62ZAYfdcUx2hSLks9awzCM5R9H3aHOsnGL3dXqrUnbCXNktIj-jlj429gbUcRiKgpmiDmssCgqkoAQWn46URHeVfxvMMoHBxOql10jk13dcbj3NQS-bMavI6c-4o62hBsHI87yobvxz4f0aNJiiU5VFLguEFdlWHmbF6P9N9PZQboyxu94EkmLksrwpj8RHOtzowsgGh4-EHgnK34_VUkv0sVMRSX3iRhd5XygvyOeJs8-k9Rlz-ushYYMko8USi5p28_k8t8rIEghdnVGi8xF339s09pt6bvaUqb2cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/akhbarefori/685140" target="_blank">📅 00:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685139">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78f44195a3.mp4?token=Pqu74Vn8ZiFp-rvA6Y4s6fuDUDt08H0o8O1XRGgx1J6ruDeUaTeR0l_g_t-LT1_bbko2Qh0GFtQn6P38MVmI-YiQHpHB5Xk9XoizPCk6x53iXSKfu4shUTQaFfCw27Ou2mkVxlGpdxRvJxTw3ncczvuQ5JDskaueYV0Sbtc_p0KhzzsavZeylhJ-bM8eMlCip5ce3eAlqdplUuRfQKvVpTBPSAgpIQ7gNLcQ5HBq1gYI_J4iRBPfkuyCMI3ZT3_YFEgpJPg24rMQJYzSiJ4ig7m8eoHfLfEK_z2pkHSRsww0QH4KtzOoP9F-v7dJUR-aZqr8HDA9T6r3fbNrF-Icuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78f44195a3.mp4?token=Pqu74Vn8ZiFp-rvA6Y4s6fuDUDt08H0o8O1XRGgx1J6ruDeUaTeR0l_g_t-LT1_bbko2Qh0GFtQn6P38MVmI-YiQHpHB5Xk9XoizPCk6x53iXSKfu4shUTQaFfCw27Ou2mkVxlGpdxRvJxTw3ncczvuQ5JDskaueYV0Sbtc_p0KhzzsavZeylhJ-bM8eMlCip5ce3eAlqdplUuRfQKvVpTBPSAgpIQ7gNLcQ5HBq1gYI_J4iRBPfkuyCMI3ZT3_YFEgpJPg24rMQJYzSiJ4ig7m8eoHfLfEK_z2pkHSRsww0QH4KtzOoP9F-v7dJUR-aZqr8HDA9T6r3fbNrF-Icuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: کالابرگ را برای برخی از دهک‌ها افزایش خواهیم داد
🔹
از اینکه نتوانستیم کالابرگ را افزایش دهیم، شرمندۀ مردم هستیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/685139" target="_blank">📅 23:59 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685138">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V3GohR8AWk0ioaSrl2yOGQ56WjydsKh1h4rs7nkU3Omal_wpDvYczasRv8EVi7vuk8uAb4CKupTaPCJjw2CyvEGGMuvRH-Teziir-Q6tI3IctBuTWpr7owWvvXoxrxzuvcImccZX-lp5idAe6GDa6ReYIGgTBdYOU4nIGPdzw6h9duwRMCbTj0SVvbIp-g8TTm5uein7TBsoASoXy61qc12dsqVsRYE3mLXNPPXu7vKCnh3y1ZAaL3_VJbulm2nDUd2XNqRpzR8CpTjDnwyqQJVJUMQixJrALDBru__6Q0Dxw7OjcoA-wTypZdVGnxClBEZP1YXYh1XDRoYd7Q8KmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سرلشکر رضایی: تاکیدات امروز رهبر معظم انقلاب روشن و غیرقابل تفسیر است‏
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/685138" target="_blank">📅 23:56 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685137">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rEYVGbxTZ63Y7TUGT54QKXe4kt7407-8iEuFWXU1zraoV_Ojhsxaf5npgKVE2XpOr6EOvVajF6x5B5AzRXHR8MfyK8QOXgNmGhexRxlqNNFCJma7--fqJJNDtgKVk5CofuP2goyHFRqSg6WFTygxvLh7eMb4MVrBBrH9AHPxEjlYL1J8a-Q2WtyFyNEF3R3cnuQOoKts2Z9uYX3yTw7YLwmIOBgoh9UPBGD7ywrNjPQwfIpdE0sm1eUtxJ7-ShadfZnx9ucWXgH-PNYlT2Dd1nXgoAbd3hgK_yNt9LSWYvhXEjNIxERPB3JzTGrUjejJ3B8umWaHAQYZ5I9gV6_Ehg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جزئیات تصمیم نهایی دولت درباره قیمت بنزین / از کاهش سهمیه‌ها تا افزایش نرخ سوم / تکلیف سهمیه خودروهای فرسوده چیست؟
🔹
با اظهارات امشب مسعود پزشکیان، حالا روشن است که بنزین احتمالا همزمان با کاهش سهمیه‌ها، رشد دو برابری نرخ سوم را تجربه خواهد کرد.
در وبسایت خبرفوری بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3241164</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/685137" target="_blank">📅 23:55 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685136">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GpmnIRNOsYTCkhVPBjfdxeZXmAD59DJa-HR-UM9h9GtlDSJcSfp0W8w7fTyupWp_ZSappahDjhp4gNr3JbLG9Ihd6Af02EpkCw7aiDhKccepNNPK9hi-T_1gxIN2l_Z53SEfDDSKkoTaR9jOrw1RQAAyGDJwRJjai9Kk6nLHn8bZP4MOP6Zw9vgGkTCg_N9drGlH563s_H2vok-t5X3WkV6y0_8FF-u_E5noMxN8czKs3O1R0Z97tUx8hkyVJu8kzTyR5VfQT3-KwMNE9NBJ_NcrOFTKfXNDqqaHhmeVXJTEzY5AYwmwRzoxZjkuFzpgiuQlmqQZtuUO9DrayYouqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیروی دریایی سپاه پاسداران انقلاب اسلامی: تسلط رزمندگان اسلام بر آبراه راهبردی تنگه هرمز کاملا قاطع است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/685136" target="_blank">📅 23:53 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685135">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03a6df5145.mp4?token=TX66tLL6vvPCjnm6XEUR_rEfJQxp6kWQWsHDg9rwcuVZV9jxa_HiTz07jKpbVYEVY8gBhwAeN9REKdx9VFQovAuQjejW7C0ihk8BYVIwBGuCNF6HUJ2e_FQKW95RJ8brbVtS2sswdh4YKLiIqFXP5EVuv83q398t6sPJZhBdxduz8KTOqlCwKViSi17_m4dHKQ0gLiC7QOZkL6wIGTWmqNZtqd9LB-QQyoBpQRzrFQnSORKUoteKXsZq1ZKcspUIQ4x-zuWbbDDO9Ai85WBubd-PhpWiqGhZSKyQ6sXz20tfD4NAJmZHc2Gu7WXRkZS37Qd9mfwAYrqj3tccEBrWz4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03a6df5145.mp4?token=TX66tLL6vvPCjnm6XEUR_rEfJQxp6kWQWsHDg9rwcuVZV9jxa_HiTz07jKpbVYEVY8gBhwAeN9REKdx9VFQovAuQjejW7C0ihk8BYVIwBGuCNF6HUJ2e_FQKW95RJ8brbVtS2sswdh4YKLiIqFXP5EVuv83q398t6sPJZhBdxduz8KTOqlCwKViSi17_m4dHKQ0gLiC7QOZkL6wIGTWmqNZtqd9LB-QQyoBpQRzrFQnSORKUoteKXsZq1ZKcspUIQ4x-zuWbbDDO9Ai85WBubd-PhpWiqGhZSKyQ6sXz20tfD4NAJmZHc2Gu7WXRkZS37Qd9mfwAYrqj3tccEBrWz4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر یک مقدار صرفه‌جویی کنیم، از بحران عبور می‌کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/685135" target="_blank">📅 23:52 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685134">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bj1M8fiw_udQTEql3DXqDlEBvHpolEAJElUZeb6TVHb4hJyP__mDICd33sfubUx6jP5ce1eMd7hz8omgELs-1tGhBTiRMlmUdf8GxHIMYEddCZjT6CYw_Hu9ie5G_epV-HJSFKWrFqO7ljhtQ5jDg5cbKXKWHt5wPQO7LJjKYYV-tglLPbMLx7JLkBaSzDpE9de_Q1DnqfODVU5ECjp7SHLro8XDE5enksw2NF24L6tDT02dTqOwyjvJYIeHCQaj6gdW9CuY0cMrydatWmFXWM-yhsckQr51wC2jsQ83cR_O70pMmMZxxZljKp11iszWYiu7N1xaC4BlRQ9uLDC-KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سناتور آمریکایی: وقت پایان جنگ با ایران رسیده است
آدام شف، سناتور دموکرات آمریکایی:
🔹
پس از شش ماه بدون راهبرد مشخص و در حالی که هزینه‌ها افزایش یافته و نیروهای نظامی آمریکا از خانواده‌هایشان دور هستند، زمان پایان جنگ و بازگرداندن نیروها به خانه فرا رسیده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/685134" target="_blank">📅 23:52 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685133">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a41d8f1090.mp4?token=nQPIxH6ZNSVceSAoafXsEH9mvB2ytMkHomerjVtugrjp1RPiLIyWgnRZXKFmHAQk5Z6tkQdMe7pF8ehVRoBqyxIKPie3eHDSlMyNJZwRachLzINdqY1NlmFW1HgHMtX6XmEEgvhJfEQnPeDCAXPtSP1-foujUUOr9bSw7pWovQ6f1fC3j_IvCwMPDclS0E-mJTXSBeuwt4gaNGNtXutORXmRByRN6MplN7tWto-_ThkbSkdrU-ZDQJsfLr4M76ZIvXjWAJOKAwbU3OKQc2Fo5LgIHnDSrDTItREuV-TdluOD8F2EsQSlujFGKQJWZElYlH7xmyM8wmg8lG6wtVf_kDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a41d8f1090.mp4?token=nQPIxH6ZNSVceSAoafXsEH9mvB2ytMkHomerjVtugrjp1RPiLIyWgnRZXKFmHAQk5Z6tkQdMe7pF8ehVRoBqyxIKPie3eHDSlMyNJZwRachLzINdqY1NlmFW1HgHMtX6XmEEgvhJfEQnPeDCAXPtSP1-foujUUOr9bSw7pWovQ6f1fC3j_IvCwMPDclS0E-mJTXSBeuwt4gaNGNtXutORXmRByRN6MplN7tWto-_ThkbSkdrU-ZDQJsfLr4M76ZIvXjWAJOKAwbU3OKQc2Fo5LgIHnDSrDTItREuV-TdluOD8F2EsQSlujFGKQJWZElYlH7xmyM8wmg8lG6wtVf_kDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس‌جمهور: اصلاحِ کشت شدنی اما زمان‌بر است
🔹
واردات و صادرات ۲۵ تا ۳۵ درصد کاهش یافته است
🔹
خود من زمین کشاورزی دارم؛ هیچ وقت از آن سودی نبردیم/ کشاورزان ما اگر خودشان کار نکنند، کشاورزی هیچ سودی برایشان ندارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/685133" target="_blank">📅 23:39 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685132">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
دبیرکل حزب‌الله لبنان: حزب‌الله مانع اشغال بیروت شد  شیخ نعیم قاسم:
🔹
ما این دستاورد را به دست آوردیم که مانع شدیم آنها به پایتخت، بیروت، برسند. ما مانع شدیم آنها ما را از قدرت و سلاحمان خلع کنند؛ زیرا در این صورت لبنان ضعیف می‌شد، آنها بر لبنان مسلط می‌شدند…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/685132" target="_blank">📅 23:37 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685131">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5F3yv_Rk98uJ_VU954AUSkLPgbcVOqVDY7L72vT8ziNq7W6lffQyJbwZ-_qHLrxn7RuN-EwB_whVIBq5ZNl7wPOiWdQZMHlpE4l6cDkirJrnBoiNLWw6ySCp946jHcLBWn4OtRWLLhKZWroOnGsaEzC6UZJ_1sSayMg_O4AN2ZS9xTulLyAeyll24XBzneXsAJxnQOonl9thZ4-sgdowZO4VKw15hNJWHIGVpel3v-JR8ML_OfKxiNETNWCaXbHQyTiBTbveuTfuNq5EQKPt8yI0oJWQMWooXWHfgxLxoNzZFAUH4dYDdwm6bn96XJyoOGmANb23v_HxsZpuHUYog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جدول لیگ برتر پس از بازی‌های امروز
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/685131" target="_blank">📅 23:33 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685130">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b6efd56ed.mp4?token=na0ZFHbT54-KPhvP8C1-5xhRae2yeNfkKHVZsx9Mn3TX4DniQrNHk6P-zI8kcbDcSBp4d3x7Q0CHBJ6LJM3TPTU_3S7FvqHpCZNiScR6eBuDSyeIxY0H0rtLnc6YAdPEqKwF_9OBxbF4-LFEpnHWkESHdonnEUS2QOinz86JVghTOADccvGvw76d1TZfjdYWVIRchsshkcW_H7zVezWeUne9gsvSA63PRGFr_3ZH_x4oEQYuxsJrxWfQ6F7mwVT_1H3p2EcvRXDgRRwQgZVo5Xz22Ptzy4VqROILqZReEbUpJ1E2A9w7Wn1oknidR1KmmfnpGIjQs76rUeyTMmJQRJvJ2nC8UaJjh0hLS4KlDIp-pwpAqapAF2B4pHJ0FUtHV0_Nf7KZh0U1Nhu5KCuRRVHT4QWRlzjHZfpgsvcW6usZhwu3NLB4y63AEN2KVM_5slQxzuMECDeRajtTXsE5u1yV9-W99kVwsj4gRET2CW5XAJURsEQj8HXDn-hS6RXMIX9jWy2C1TPg4efPLfH61GR0ve3KrRECX3qKhDduXq2I3jI9VQEHe00Nabew8qEH1k4OIf3ZnQbnnd73ICbfrJwPtXk70zuOCQkfNGhNBby9QRkQJOXPEc8M_neMXWRj0Ht9gnIVGO-ysZa71Tt9FEzClCkaceP1GT6rii5bVV4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b6efd56ed.mp4?token=na0ZFHbT54-KPhvP8C1-5xhRae2yeNfkKHVZsx9Mn3TX4DniQrNHk6P-zI8kcbDcSBp4d3x7Q0CHBJ6LJM3TPTU_3S7FvqHpCZNiScR6eBuDSyeIxY0H0rtLnc6YAdPEqKwF_9OBxbF4-LFEpnHWkESHdonnEUS2QOinz86JVghTOADccvGvw76d1TZfjdYWVIRchsshkcW_H7zVezWeUne9gsvSA63PRGFr_3ZH_x4oEQYuxsJrxWfQ6F7mwVT_1H3p2EcvRXDgRRwQgZVo5Xz22Ptzy4VqROILqZReEbUpJ1E2A9w7Wn1oknidR1KmmfnpGIjQs76rUeyTMmJQRJvJ2nC8UaJjh0hLS4KlDIp-pwpAqapAF2B4pHJ0FUtHV0_Nf7KZh0U1Nhu5KCuRRVHT4QWRlzjHZfpgsvcW6usZhwu3NLB4y63AEN2KVM_5slQxzuMECDeRajtTXsE5u1yV9-W99kVwsj4gRET2CW5XAJURsEQj8HXDn-hS6RXMIX9jWy2C1TPg4efPLfH61GR0ve3KrRECX3qKhDduXq2I3jI9VQEHe00Nabew8qEH1k4OIf3ZnQbnnd73ICbfrJwPtXk70zuOCQkfNGhNBby9QRkQJOXPEc8M_neMXWRj0Ht9gnIVGO-ysZa71Tt9FEzClCkaceP1GT6rii5bVV4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دلایل گرانی‌های اخیر از زبان رئیس‌جمهور
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/685130" target="_blank">📅 23:30 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685129">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
پزشکیان: واردات و صادرات ۲۵ تا ۳۵ درصد کاهش یافته است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/685129" target="_blank">📅 23:28 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685128">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔹
در لابلای خبرها، داغ‌ترین‌ها را ازدست ندهید
🔹
🔹
ترامپ درِ بازگشت به توافق اسلام آباد را بست‌/ حالا چه می شود؟
👇
khabarfoori.com/fa/tiny/news-3240972
🔹
پزشکیان برای نرخ سوم بنزین، سقف تعیین کرد
👇
khabarfoori.com/fa/tiny/news-3241156
🔹
علی کریمی؛ از لگد به ساک پزشکی تا دعوا با دایی و رضا پهلوی/ تاریخچه قهرهای تمام‌نشدنی جادوگر همیشه عصبانی
👇
khabarfoori.com/fa/tiny/news-3241154
🔹
هنگامه قاضیانی به ایران بازگشت
👇
khabarfoori.com/fa/tiny/news-3241083
🔹
قدردانی مادر زهرا متقی از پلیس و مردم پس از پیدا شدن دختر ۱۱ ساله‌اش
👇
khabarfoori.com/fa/tiny/news-3241033
🔹
همه خبرهای جنگ و مذاکره را اینجا مرور کنید
🔹
https://share.google/8EImhrm9fBFYjsyZr</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/685128" target="_blank">📅 23:22 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685127">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c72f71a5bc.mp4?token=ZV-7Rt7wV-DSDI6i0vTk_hp24C5V1ggNbeZYoiwbgO8590bKKXwXAp7ZlsPLUv6Dna_6Dp45X_8Bw3U27lpz-7ly5V52UJ7c8laKfqm-HafcG5AdeyQmUlk9AUOvVSxJOGwob4c2rtKFpJNB3Wqz5j1nBxKwmn0em-o4Juj6jwOmWuC8PGzldO5CztMx-pKbLjxYxwDPJvjjYmL5_ZQJ_CcMjkIblI63nucEi8yZTsfXwcPnu9SUeLqrQi0d6Cz2j-c6mudbWhBqHDDuEOhi1LAcheIllYOvQbBsykAqCn_NgxTb4RDg7p0Vz_2qz3KzTlqveX9vSemuS7rj2gCRjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c72f71a5bc.mp4?token=ZV-7Rt7wV-DSDI6i0vTk_hp24C5V1ggNbeZYoiwbgO8590bKKXwXAp7ZlsPLUv6Dna_6Dp45X_8Bw3U27lpz-7ly5V52UJ7c8laKfqm-HafcG5AdeyQmUlk9AUOvVSxJOGwob4c2rtKFpJNB3Wqz5j1nBxKwmn0em-o4Juj6jwOmWuC8PGzldO5CztMx-pKbLjxYxwDPJvjjYmL5_ZQJ_CcMjkIblI63nucEi8yZTsfXwcPnu9SUeLqrQi0d6Cz2j-c6mudbWhBqHDDuEOhi1LAcheIllYOvQbBsykAqCn_NgxTb4RDg7p0Vz_2qz3KzTlqveX9vSemuS7rj2gCRjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: افرادی که دستی بر آتش ندارند، تحلیل‌هایشان در جیبشان بگذارند
🔹
طرح نمی‌خواهم؛ اگر کسی می‌تواند مشکلات را با شرایط موجود حل کند، به او اختیار می‌دهم.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/685127" target="_blank">📅 23:17 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685126">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
رئیس‌جمهور: نزدیک ۹۰ میلیون بشکه نفت در زمان اجرای تفاهم‌نامه فروختیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/685126" target="_blank">📅 23:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685125">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJuqod4Ic3bamXBtnIADJ1RppTNHjocnrVpdfbRnxpcHhPfoBf-cmMTH9fv4lH6-2Nd33tAWicblZJ8EzSUe7lheQCoDEaInNyLPbX96KDwSybo_e68fozm5qUPxZfFhfFYiIK0uFP7xY31fKnPuUQs2vE2i6a2vYf6yQcGjVpNDWaDVX5hbi8rZDiP3q10VMc9EiOhG6AAyl9XPR2JkCifcKrzdmpZDXWBnqYs6n2HaN8mcglLPMG2FmenEgqMroJ06l3omnuviBzo2zLKcdTO2WQ1Y_N9RerdGCB-w-zEY2ZreIz-tcClI6r7Ac7aVicWCK4GZH8sNIlfFcIC3Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ماجرای بازگشت غیرمنتظره محسن نامجو؛ «عادی‌سازی» یا غم غربت؟ |‌ معین، عطاالله مهاجرانی و سروش؛ چه کسانی در صف بازگشتند؟
🔹
انتشار خبر بازگشت محسن نامجو، خواننده و آهنگساز ساختارشکن و نام‌آشنای موسیقی تلفیقی به تهران، شوک بزرگی به فضای رسانه‌ای، شبکه‌های اجتماعی و محافل فرهنگی وارد کرد.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3241125</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/685125" target="_blank">📅 23:08 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685124">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c70ff699e0.mp4?token=RCow7DnVmdr_ivs3YDIm0YtB_G_R0M5JP06vbD5KMLbnnPdcjgdVQ9snd0OimtMXnJbKrYIroZmjm7yuY48uA_eS2CcrKwwZdSfFZFZTEN8FBqNQHSwMqhfb4QdZ63tEfeH1HrIM4ysKfqx-X0BVvoImaGsOfjs2aVV1YravdRy29TMfHLpP1rWgrJhWndgAgWpQtv9xzpoHdQVkhbYFsbl3IqCGPcaLatDXcDxSV6i3ImpontsPCjLANSHQYbFYAcLpdb9JbDzhbrc2FcTPB_0Z7wB7XtTMxQuqsX7sc4Ii7Hjoz1m0_hdNRVXxjcL_IS_gwzDhn5oRQQVdMLiqVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c70ff699e0.mp4?token=RCow7DnVmdr_ivs3YDIm0YtB_G_R0M5JP06vbD5KMLbnnPdcjgdVQ9snd0OimtMXnJbKrYIroZmjm7yuY48uA_eS2CcrKwwZdSfFZFZTEN8FBqNQHSwMqhfb4QdZ63tEfeH1HrIM4ysKfqx-X0BVvoImaGsOfjs2aVV1YravdRy29TMfHLpP1rWgrJhWndgAgWpQtv9xzpoHdQVkhbYFsbl3IqCGPcaLatDXcDxSV6i3ImpontsPCjLANSHQYbFYAcLpdb9JbDzhbrc2FcTPB_0Z7wB7XtTMxQuqsX7sc4Ii7Hjoz1m0_hdNRVXxjcL_IS_gwzDhn5oRQQVdMLiqVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: نباید نگاه صفر و صدی به مذاکرات داشته باشیم؛ اگر به تعهدات عمل نکنند، ما هم عمل نمی‌کنیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/685124" target="_blank">📅 23:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685123">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32ccb595ab.mp4?token=M7tvtUoVKvFj3ba6aqNZPlxaLD-d6glq7RwBViiCKBdqd7rQyJIcK1IcXPiTUutqDesfOvZPs2d8RUwC1c--hv_iC0h7qsM_zSnn5H8iZle_WNSHeQyAwTbH_-9ah-3Jflv7ZRLty_j4BT3gFfqZIMn8zMxfZiCoOb7qBy36ax5TJkjMgahVLIfjQv_67z2oNZ7Nw83R-xyL74R5ixm7zfcq2y29YR9rkiWCVYFpK8xE23ZgHDfhlMyaTibK3BAIvomWGHdvE4q38wzQ1Y33Pxro2fKS8QDnS1qvjam7DmDc1TbmzEyLoc8l1H1uwvxHNoib3-cFdiDvcGquqRvefIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32ccb595ab.mp4?token=M7tvtUoVKvFj3ba6aqNZPlxaLD-d6glq7RwBViiCKBdqd7rQyJIcK1IcXPiTUutqDesfOvZPs2d8RUwC1c--hv_iC0h7qsM_zSnn5H8iZle_WNSHeQyAwTbH_-9ah-3Jflv7ZRLty_j4BT3gFfqZIMn8zMxfZiCoOb7qBy36ax5TJkjMgahVLIfjQv_67z2oNZ7Nw83R-xyL74R5ixm7zfcq2y29YR9rkiWCVYFpK8xE23ZgHDfhlMyaTibK3BAIvomWGHdvE4q38wzQ1Y33Pxro2fKS8QDnS1qvjam7DmDc1TbmzEyLoc8l1H1uwvxHNoib3-cFdiDvcGquqRvefIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزارت رفاه پاشنه آشیل دولت خواهد شد/ مدیرکل دفتر وزیر رفاه تاثیر و مداخله‌اش در اداره وزارتخانه بیشتر است
مجید نصیرپور، عضو کمیسیون اجتماعی مجلس در
#گفتگو
با خبرفوری:
🔹
صندوق‌های بازنشستگی ما از یکی از مسائلی که رنج می‌برد تعدد قوانین استخدامی و بازنشستگی است.
🔹
چندین صندوق داریم حتی یک شرکت دولتی به اسم شرکت هواپیمایی جمهوری اسلامی برای خودش صندوق دارد و درحال حاضر با نزدیک به ۱۰۰ هزار بازنشسته ورشکسته هستند.
🔹
وزیر رفاه توانایی لازم برای اداره موسسات اقتصادی خود را ندارد و در تراز وزارت باید یک جانبه جایی صورت بگیرد.
🔹
گزارش اخیر دیوان محاسبات اعلام می‌کند که که بخش عمده ای از اعضای هیئت مدیرانی که در شرکت‌های مختلف منصوب شده‌اند، تشریفات اداری را طی نکرده‌اند.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/685123" target="_blank">📅 23:00 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685122">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/998f235100.mp4?token=Yb9RiNPA7lGMEeZoD7F_guQz7DmTwg28j7R35U3YF9o2v_KcQu-_FaFnwyAghTpyLM7qA4BrRe22xAYW_TT4RRanFQbCBbo5azYEbB2JbpBPjYmltmyWJ-2bZRYWgRUgH6Cf7Ek8Gc_d8zfrPt6TuyOlM4nqJEBZWPCd8Ac02R1veoXJ9_Sxf77zG9oA57JN8KAXPukg6svik6W8JzQpg36KGEobTxRdBEUA5sg46XsnQvTdfQa40E3cBKgR2bZq1u81dp1a_fWeCVF3hOXqHdykLzY5He9F74AAawwCMGXTE4YGJVieDhx-inBwDOf24ZPhEDmsifU2-2EVq1PeOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/998f235100.mp4?token=Yb9RiNPA7lGMEeZoD7F_guQz7DmTwg28j7R35U3YF9o2v_KcQu-_FaFnwyAghTpyLM7qA4BrRe22xAYW_TT4RRanFQbCBbo5azYEbB2JbpBPjYmltmyWJ-2bZRYWgRUgH6Cf7Ek8Gc_d8zfrPt6TuyOlM4nqJEBZWPCd8Ac02R1veoXJ9_Sxf77zG9oA57JN8KAXPukg6svik6W8JzQpg36KGEobTxRdBEUA5sg46XsnQvTdfQa40E3cBKgR2bZq1u81dp1a_fWeCVF3hOXqHdykLzY5He9F74AAawwCMGXTE4YGJVieDhx-inBwDOf24ZPhEDmsifU2-2EVq1PeOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: کاهش مصرف از راهکارهای اصلی مدیریت مساله بنزین است
🔹
روزانه ‌۲ میلیون ماشین وارد تهران می‌شود و برمی‌گردد؛ اگر کارمندان ما در اداره مربوطه در شهر خود بمانند، کسری بنزین جبران می‌شود.
🔹
طرحی داریم که با کمک شهری کارمندان هفته‌ای یک روز با حمل‌ونقل…</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/685122" target="_blank">📅 22:59 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685121">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTechnolife.com | تکنولایف</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/APFrftlNx3lOc1gPJYxXe2GiinWuZxgJ2-AzxXtzLQaDnV55a0QudEkxSzOmUunU76qUSEjZ2dkztNtOqDyFFyB8e6UT8-igrzj37oK8bDqnXGSvxla3yENgtxmd4KRB6USynSULmNELlGKAFN39q60v09xLdh0A3rpjrGd6kvwVsYAgKcqwPLf_oAOaobZUmejd1d-o5w0m8JdzMoleNdV8gtK1AMV5N2izhZfHUQYoMcgfFEPtpOoOH-qIut3WkXHG8HKUtlZBX8NTqGwIGPAUWqF4E9NCRhdrkbZItV59qrPSBBAaRpwKDtv-q_CB4z2QQnAi4lflZzmkso2-ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
یک خرید؛ شانس بردن آیفون و BMW!
✅
تا
۱۰ شهریور
، از تکنولایف با تخفیف‌های ویژه و قیمت‌های کف بازار خرید کنید و شانس بردن
آیفون ۱۷ پرومکس
رو از دست ندید.
✅
اگر پرداختتون رو از درگاه اسنپ‌پی انجام بدید، علاوه‌بر قرعه‌کشی آیفون، در قرعه‌کشی
یک دستگاه BMW
هم حضور خواهید داشت.
🚘
http://tchl.ir/HNgrp7
http://tchl.ir/HNgrp7
http://tchl.ir/HNgrp7</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/685121" target="_blank">📅 22:56 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685120">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f393c4474.mp4?token=k1ahRljjVGMWLWqRGmscrlUw_d97V7y_LCQ8fjmcwAl8VUjG_ydUtsc_q0zhMEuiKyKfpIhOMvutNN_Bzp-pJpNOP_K0VyXXQhQeOYDkMACvH0JJB5DH23P85n_P8fkp-_cKqkYlLgl56R9MXpB2xJcv0DljgFfYTHE2RceDjAmYq_PX-xV16dQoWlLXPFDAeHnhbk5oyXPkgbUY9ClOI8QhFH-W0k8AWQqrdCLwt-corwHBqi6hRDUyIEtB55TAxRR40SyF5cHoA8sCtYJNlLbQOqp_MY6vhR8n1WP9C7DfqHzSthdoEsNBk2JS1wr91SQX3omXHtRwr6B_6uK9rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f393c4474.mp4?token=k1ahRljjVGMWLWqRGmscrlUw_d97V7y_LCQ8fjmcwAl8VUjG_ydUtsc_q0zhMEuiKyKfpIhOMvutNN_Bzp-pJpNOP_K0VyXXQhQeOYDkMACvH0JJB5DH23P85n_P8fkp-_cKqkYlLgl56R9MXpB2xJcv0DljgFfYTHE2RceDjAmYq_PX-xV16dQoWlLXPFDAeHnhbk5oyXPkgbUY9ClOI8QhFH-W0k8AWQqrdCLwt-corwHBqi6hRDUyIEtB55TAxRR40SyF5cHoA8sCtYJNlLbQOqp_MY6vhR8n1WP9C7DfqHzSthdoEsNBk2JS1wr91SQX3omXHtRwr6B_6uK9rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🛑
واکنش تند حسین شمقدری مستند ساز به جنجال اخیر علی کریمی و رضا پهلوی :
علی کریمی میگه  « من مثل کشته‌شده‌های ۱۸ـ۱۹ دی نیستم؛ که هرکاری خواستید بکنم ! »
همین؟ اینهمه جوون کشته شد ...
💔
بازم از پهلوی و علی کریمی باید خط بگیریم؟
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/685120" target="_blank">📅 22:55 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685119">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">دبیرکل حزب‌الله لبنان: ایران و نیروهای مقاومت در حال مقابله با توطئه آمریکایی صهیونیستی هستند.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/685119" target="_blank">📅 22:54 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685118">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb39bc1a2a.mp4?token=nXZgAHjDYzGo_gWuDSxVaZVJbBVddAJpMQ7LdJgX4Q-8EQKEz4K6mQg-kO05UeXOO5r8VJ2PfS7gziQReuchqt2ub29aBdr1keLB4tSjcxhCera_cYwgtazhD_-JmxDyYyV_K_lpqG3T_KC3E0HnbF4noPAU5VAPWkGzNvKhVMlId29CxPNf_M7iJc0Bmi4N9zBYrL79imZkslJ8rHD5vO6GAR65o5Gu2hg1WmQjXuqe3EDXrpPR_64zaEDpNcB1GRXxQmD6nOS8yyqHB0Eh-uBfTV8kFRoIsasNsojdijkEo3QE-RvV4NLi-qxhIyeLUt5lAnGgGJLtO55Ai5E6uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb39bc1a2a.mp4?token=nXZgAHjDYzGo_gWuDSxVaZVJbBVddAJpMQ7LdJgX4Q-8EQKEz4K6mQg-kO05UeXOO5r8VJ2PfS7gziQReuchqt2ub29aBdr1keLB4tSjcxhCera_cYwgtazhD_-JmxDyYyV_K_lpqG3T_KC3E0HnbF4noPAU5VAPWkGzNvKhVMlId29CxPNf_M7iJc0Bmi4N9zBYrL79imZkslJ8rHD5vO6GAR65o5Gu2hg1WmQjXuqe3EDXrpPR_64zaEDpNcB1GRXxQmD6nOS8yyqHB0Eh-uBfTV8kFRoIsasNsojdijkEo3QE-RvV4NLi-qxhIyeLUt5lAnGgGJLtO55Ai5E6uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: محاسبه دشمن برای بهم ریختن کشور غلط نبود، اما با مشارکت مردم و هدایت رهبری ایستادیم
🔹
کسانی که با استفاده از هوش مصنوعی این مطالعات را انجام داده بودند، بی‌حساب حمله نکردند. با محاسبات آن‌ها، کشور ما باید به هم می‌ریخت؛ اما با مشارکت مردم، رهبری…</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/685118" target="_blank">📅 22:40 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685117">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
تأکید رئیس‌جمهور درباره لزوم مدیریت مصرف بنزین
🔹
باید به تفاهم و نگاه مشترک برسیم و با کمترین نارضایتی موضوعاتی مانند بنزین را حل کنیم.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/685117" target="_blank">📅 22:36 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685116">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74cb9cace8.mp4?token=voFHsrHCm5r-52UBvFKIepjVPbhsL5n0ZEdR4C8_qlYAMKN4OYesUPwrUypYg12SGDESfN2fCI-dGwgET-WJsxqUKLHGOggZapd7b_C6UYu9r5oPwz3lGYbbewQizXLSrHj0eZwVzVCWNYvAZWUpqmLuiO1kfnBDfnfmAVtC1A-vc5vVof8Jp0tVArWkzPPI1rFZCd57U5rOnJMJ2I2ESN4bu-qacEx5lVxQbu7MT4RLajwmz4u0ybORH2gS2jeFyQdYetHikt3SnGSvNFJm38psmqcNJQjpV52Z9wznLsTCU6r_NeTYRlo8sWlkxN4GAETvvCwLtFmK3_Jv3M6dIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74cb9cace8.mp4?token=voFHsrHCm5r-52UBvFKIepjVPbhsL5n0ZEdR4C8_qlYAMKN4OYesUPwrUypYg12SGDESfN2fCI-dGwgET-WJsxqUKLHGOggZapd7b_C6UYu9r5oPwz3lGYbbewQizXLSrHj0eZwVzVCWNYvAZWUpqmLuiO1kfnBDfnfmAVtC1A-vc5vVof8Jp0tVArWkzPPI1rFZCd57U5rOnJMJ2I2ESN4bu-qacEx5lVxQbu7MT4RLajwmz4u0ybORH2gS2jeFyQdYetHikt3SnGSvNFJm38psmqcNJQjpV52Z9wznLsTCU6r_NeTYRlo8sWlkxN4GAETvvCwLtFmK3_Jv3M6dIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: نرخ سوم بنزین بیش از ۱۰ هزار تومان نخواهد بود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/685116" target="_blank">📅 22:31 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685115">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
دبیرکل حزب‌الله لبنان: ایران و نیروهای مقاومت در حال مقابله با توطئه آمریکایی صهیونیستی هستند.
🔹
عراقچی: در میدان دیپلماسی با قدرت از منافع ملت ایران دفاع می‌کنیم.
🔹
سخنگوی دولت: دولت «فقدان رهبری شهید» را سنگین‌ترین هزینه جنگ می‌داند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/685115" target="_blank">📅 22:29 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685114">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o9HX0wERBiNN09taF3rZsnzNXMZ3CLxdh3rT0-jm4ONQnVBV9KBLhAg2uTaYxCHvTY1mjCcQiwMNhganEhXnRbk1Evnys1OzJsoPOjulgnUgiz2lT3erirHWve0XAWRXbBW8rQoS8nCWauyXD_iniiHbrT3flxQ8VmBZ8V-7LqW4k7RjNhiydPkwhaHh3Mcm20s8lXJswRSvmlC67_Ug8qkGzlVfqDko63fcCogmT-X57odnkDDlHoWNBCZgJOP5cHuN_ztjU6ghx4UskoX17QPMF4LKAkNmEp9npqs_uW6oLmXG927POIwG9y-vNwlxtelEniVxNfF3LE8EYGIa1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">14050606پیام_رهبر_معظم_انقلاب_به‌مناسبت_هفته_دولت.pdf</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/685114" target="_blank">📅 22:27 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685113">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رهبر انقلاب اسلامی</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">14050606پیام_رهبر_معظم_انقلاب_به‌مناسبت_هفته_دولت.pdf</div>
  <div class="tg-doc-extra">169.2 KB</div>
</div>
<a href="https://t.me/akhbarefori/685113" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📖
متن کامل پیام رهبر معظّم انقلاب به‌مناسبت هفته دولت
🔗
https://rahbar.ir/s/1849
💻
Rahbar.ir
|
📲
@Rahbar_ir</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/685113" target="_blank">📅 22:26 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685112">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5e065d304.mp4?token=Z5tRAlkJYodo2Motx-lrehUpEML1e8tsmEEqSu3Isz45PRQVUuFVLYyN-uJ7fhbMDLE_xOe3cts9pvmz49BjTouLN3KzyzN4euKpEYccj7ZI-mQC8fwKB55ZHEcd4GVieVvp5wJXo7WzlL9D4T53VMarYcxsu8tRFa-gK7pUBtxWyAKdO2V9ebsOBiHy-XYXqb1EqwUOdg5hEQ8hB4qSm9Qap-KGqE9XBCzVQR62TH5SboYgzkwUTTHSIDhAEXoEpTUE6ESxLJScU3yLyl_gKjF9vzC78odnY8RTdX1qs4FsRrLsusbvUu_QzPZnwkY6cvpQ-90WCn5fyGftoC2CIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5e065d304.mp4?token=Z5tRAlkJYodo2Motx-lrehUpEML1e8tsmEEqSu3Isz45PRQVUuFVLYyN-uJ7fhbMDLE_xOe3cts9pvmz49BjTouLN3KzyzN4euKpEYccj7ZI-mQC8fwKB55ZHEcd4GVieVvp5wJXo7WzlL9D4T53VMarYcxsu8tRFa-gK7pUBtxWyAKdO2V9ebsOBiHy-XYXqb1EqwUOdg5hEQ8hB4qSm9Qap-KGqE9XBCzVQR62TH5SboYgzkwUTTHSIDhAEXoEpTUE6ESxLJScU3yLyl_gKjF9vzC78odnY8RTdX1qs4FsRrLsusbvUu_QzPZnwkY6cvpQ-90WCn5fyGftoC2CIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس‌جمهور در گفت‌وگو با مردم: با آمدن آقای محسن رضایی نگاه‌ها در حوزه دیپلماسی به هم نزدیک می‌شود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/685112" target="_blank">📅 22:25 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685111">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
ویدویی جالب و عجیب از تمرینات تکاوری یک گروه در جنگل‌های هیرکانی شمال کشور
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/685111" target="_blank">📅 22:25 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685110">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46f66d1ad5.mp4?token=QC-FhPuS9HqtUIt4an4f2FqgY67YE6F38jUWPDW8y0SbDxOsnhK3UFWZ098xB8r2FoN---P6fj4U3uTXqEEgw7ztgIG260O9L8nBC1jLI_uHJ3e4KIRMgf-IyfHVopzlkJ9Ya0okj8NE-3pbfUfoErzIiRGxDjTtUt46CS6PColrSg19eg6t7EYmwFo87tppruJBHs-4iqY234l6AIJWcdROti3Gs4uRkGACBNINB8mMz8-qcn6PUB0juiOA5J-pxYdjf6ZH0QrW-M37DkCzXCz7rqKqeRIsX3zS3jxZTBSGS1FGQLSd6bCBV24kkGjH3tABcJTBYzAzTtfsGD_tpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46f66d1ad5.mp4?token=QC-FhPuS9HqtUIt4an4f2FqgY67YE6F38jUWPDW8y0SbDxOsnhK3UFWZ098xB8r2FoN---P6fj4U3uTXqEEgw7ztgIG260O9L8nBC1jLI_uHJ3e4KIRMgf-IyfHVopzlkJ9Ya0okj8NE-3pbfUfoErzIiRGxDjTtUt46CS6PColrSg19eg6t7EYmwFo87tppruJBHs-4iqY234l6AIJWcdROti3Gs4uRkGACBNINB8mMz8-qcn6PUB0juiOA5J-pxYdjf6ZH0QrW-M37DkCzXCz7rqKqeRIsX3zS3jxZTBSGS1FGQLSd6bCBV24kkGjH3tABcJTBYzAzTtfsGD_tpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس‌جمهور در گفت‌وگو با مردم: با آمدن آقای محسن رضایی نگاه‌ها در حوزه دیپلماسی به هم نزدیک می‌شود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/685110" target="_blank">📅 22:21 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685109">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba21c05183.mp4?token=GNz8HY-a0JuV1YtFnKJu9ThIOrG5FoSPH0i6mVozkhRjT6Qs3rUVqeRq7FF5Di6dI8N6lKooLGooONkegFQvVZueROWwsUHkbjz0Z7I4lUY4WwWgebybco-A41029jfBCQ7xGgI1QcbLxUfbqtb8Mpz3El3WrnUAz7DG5qUCbJurrMqGIZJTnuTVgjtOssIYQLn4tKJWDLgOJgWp0d_abJlQ3wvVbmNdLG6Ea3yP4YsFsf9m61CbDd0EBAQj18ZYrxPWeoM1F-zXugMdJVpISLZPJTexRuTDv8ODCxZB_BVBv3s0caygAegW9-WRYqqnRK8iVe7aK8530s7vWSXD8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba21c05183.mp4?token=GNz8HY-a0JuV1YtFnKJu9ThIOrG5FoSPH0i6mVozkhRjT6Qs3rUVqeRq7FF5Di6dI8N6lKooLGooONkegFQvVZueROWwsUHkbjz0Z7I4lUY4WwWgebybco-A41029jfBCQ7xGgI1QcbLxUfbqtb8Mpz3El3WrnUAz7DG5qUCbJurrMqGIZJTnuTVgjtOssIYQLn4tKJWDLgOJgWp0d_abJlQ3wvVbmNdLG6Ea3yP4YsFsf9m61CbDd0EBAQj18ZYrxPWeoM1F-zXugMdJVpISLZPJTexRuTDv8ODCxZB_BVBv3s0caygAegW9-WRYqqnRK8iVe7aK8530s7vWSXD8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طرف عمانی قبول دارد که باید تنگه هرمز بر اساس تفاهم‌نامه اسلام‌آباد اداره شود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/685109" target="_blank">📅 22:17 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685108">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0be1c613eb.mp4?token=tV6mRj53lqLeypJmU4yarbjo2Wk41JKcgJkE8ocP6AqtdM_1dUZeMY8UxuN0e5biOz7mTtqBNwvkBL_KT5ZOprMdVFCjpR4eHstakN7kzSXJnHKxaEdbCcQZ0qToMPIXEUeec-NYxwuWqP6u_iOdePUXuVJm6_oD_nymDXBv0ElI5KeNZ6GCoqxVdvoRtDlJeEh3mMyyEiVmbfu13JCOTIGl2JTwKZdZC1ny1ECqa5fHyq3hnfjzmXahRoJurHENBW96_bQWL8jm6H7esroMT6afTb5WY-9e1h_Q325DZtFyewqByda9wAmmHfQkY6YIr1E70EarcYg9qs9YONpzVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0be1c613eb.mp4?token=tV6mRj53lqLeypJmU4yarbjo2Wk41JKcgJkE8ocP6AqtdM_1dUZeMY8UxuN0e5biOz7mTtqBNwvkBL_KT5ZOprMdVFCjpR4eHstakN7kzSXJnHKxaEdbCcQZ0qToMPIXEUeec-NYxwuWqP6u_iOdePUXuVJm6_oD_nymDXBv0ElI5KeNZ6GCoqxVdvoRtDlJeEh3mMyyEiVmbfu13JCOTIGl2JTwKZdZC1ny1ECqa5fHyq3hnfjzmXahRoJurHENBW96_bQWL8jm6H7esroMT6afTb5WY-9e1h_Q325DZtFyewqByda9wAmmHfQkY6YIr1E70EarcYg9qs9YONpzVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت رئیس‌جمهور از شکل‌گیری تفاهم‌نامه اسلام‌آباد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/685108" target="_blank">📅 22:09 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685107">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
روایت رئیس‌جمهور از شکل‌گیری تفاهم‌نامه اسلام‌آباد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/685107" target="_blank">📅 22:07 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685106">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c7a4d0973.mp4?token=tZTAw0qCLf5kfz2TJIe9qKIxDwxyy8ZNkxVkRb0nEAieDJZoZbkvlW-uBT4zPvSe16Ri32ItL_2wmYx_I6B_5sxLyXcaT6MyqMcDQvI57_hK8ipmcKFpw3b1Vw-A0vn-qzbmpZV8WZcbQ7cbeZD4cAqbOSqewY4riKRb_S33DFaHuIJKlezuBSRyZNU0yjCrBfqVb8DSgzpUWwzLFVVm-aE85_5Z-FId6mE8VtwnWBjpHlwWsZ-_j1kMkVxOEv7qNz2K6EHr6zjW9W5Vo73u8BERGVZY48e8u6CmUMYnH3Lc-N7WnmVxI1usUzH0SEqN1IY-wR0mFm0bdinHxOiPwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c7a4d0973.mp4?token=tZTAw0qCLf5kfz2TJIe9qKIxDwxyy8ZNkxVkRb0nEAieDJZoZbkvlW-uBT4zPvSe16Ri32ItL_2wmYx_I6B_5sxLyXcaT6MyqMcDQvI57_hK8ipmcKFpw3b1Vw-A0vn-qzbmpZV8WZcbQ7cbeZD4cAqbOSqewY4riKRb_S33DFaHuIJKlezuBSRyZNU0yjCrBfqVb8DSgzpUWwzLFVVm-aE85_5Z-FId6mE8VtwnWBjpHlwWsZ-_j1kMkVxOEv7qNz2K6EHr6zjW9W5Vo73u8BERGVZY48e8u6CmUMYnH3Lc-N7WnmVxI1usUzH0SEqN1IY-wR0mFm0bdinHxOiPwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک پهپاد و پایان وحشتناک یک سخنرانی!
🔹
همه‌چیز از یک پهپاد بازی شروع شد؛ اما چند ثانیه بعد، انفجاری مهیب، سخنرانی را به کابوسی غیرمنتظره تبدیل کرد #کابوس_ترامپ
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/685106" target="_blank">📅 22:06 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685103">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
ادعای وزارت خارجه آمریکا: افراد و نهادهایی را که از طرف ایران به فعالیت‌های مالی غیرقانونی مبادرت می‌کنند، هدف قرار خواهیم داد/ انتخاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/685103" target="_blank">📅 21:41 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685102">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
کالابرگ مردادماه افرادی که احراز سکونت خود را تا ۳ شهریور ثبت کرده‌اند واریز شد
🔹
کسانی‌که در ‌۳ و ۴  شهریور اقدام به ثبت محل سکونت خود کرده‌اند نیز در هفتۀ آینده کالابرگ خود را دریافت خواهد کرد./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/685102" target="_blank">📅 21:40 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685101">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/093df67196.mp4?token=Uf1PweASlSVltjsKCBbV1lIEkbWSbqxGwpN0PKJRfSR7GOjc8Z6v2Wa7Vnhk-4pftYpqhIEyQfHvX9P-CAPT0-N_Ec1pE5Skh2wbFcr_QA1H777a6jTHcUlqE6JwvEgxVA6T7VLILSbIZ5-p9pkZ00lwXmP7v6DsDQbUaLzwMLgVkMGwYPOnUhAjxu7n-MxtHzPgfRqmlNmKv6ig9CPdWin4Jh61UqIjA25VIy0z5KiMGWlwfD6STyNdXZ_O522yGNy4ajs7ywDdOiBhlBVexBI5RchxjLi7EA38XGecByCwteDUUiQ2Ypg4XUQJmXkeWoVDJKhxNIhvv-YlafE3vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/093df67196.mp4?token=Uf1PweASlSVltjsKCBbV1lIEkbWSbqxGwpN0PKJRfSR7GOjc8Z6v2Wa7Vnhk-4pftYpqhIEyQfHvX9P-CAPT0-N_Ec1pE5Skh2wbFcr_QA1H777a6jTHcUlqE6JwvEgxVA6T7VLILSbIZ5-p9pkZ00lwXmP7v6DsDQbUaLzwMLgVkMGwYPOnUhAjxu7n-MxtHzPgfRqmlNmKv6ig9CPdWin4Jh61UqIjA25VIy0z5KiMGWlwfD6STyNdXZ_O522yGNy4ajs7ywDdOiBhlBVexBI5RchxjLi7EA38XGecByCwteDUUiQ2Ypg4XUQJmXkeWoVDJKhxNIhvv-YlafE3vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی وحشتناک از حبس یک خانواده در میان سیل عظیم نپال
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/685101" target="_blank">📅 21:27 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685100">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
لینک یاب فایل های صوتی گنجینه معنوی کانال
:
🔹
زندگی پس از زندگی
فصل یک | فصل دو
| فصل سوم
|
فصل چهارم
|
فصل ششم
🔹
چله علم و نور  "یک"
،
چله"دوم"
،
چله"سوم"
🔹
مستند شنود
🔹
آن ۳۱۳ نفر
🔹
تفسیر سوره‌های صف
|
مسد
🔹
سنت‌های الهی خداوند
🔹
شرح به وقت شام ۱
و
شرح به وقت ایران ۲
🔹
پادکست کسب‌وکار رادیو کار نکن
🔹
ادعیه روزهای هفته
🔹
برنامه کتاب‌باز
🔹
شرح و تفسیر کتب:
"سه دقیقه در قیامت"
،
"آن سوی مرگ"
🔹
چگونه با عبادت تفریح کنیم؟
🔹
حال خوش معنوی در زندگی
🔹
چله جوشن کبیر اول
و
چله دوم
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/685100" target="_blank">📅 21:27 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685099">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vi9kGT05MJ3niSxlmAD-MHnUq6Nw03NZxLIr0wSl2YVAK7VG8gTiw_VWzpewmYWJCHh4mU2im8ANR0twYjPZU9Q8JGqDrkKpW8GXENWZSc6cHEvM2-0wA_wHyRdntEFmebVzw7r5yYuTivB-KjnrXg0TzJRZIt-ZQy3d7ukMgPv5e8KTpRT1zSDJGV7UsbkOebiNnhjdwL4X4asD1HajCY1UsiD6Au_zaFW0OYO4KYRyQTm1qGwzAcJJ9s23uOn1jzujAk-js5Erky6hQUWspQvBk7YNmqIPdfFlhEXdcTqrSKv3rSesE1dkEAtDLuu-9vGj7AEkKlWwYqeKmkIQVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
🔻
مشاوره رایگان پزشکی برای متقاضیان کاهش وزن با آمپول‌های لاغری
🔹
با توجه به سیر صعودی مصرف خودسرانه آمپول های لاغری و با همکاری شرکت های دانش بنیان دوراپزشکی ، این امکان فراهم شده تا افرادی که قصد استفاده از آمپول های لاغری را دارند به صورت کاملا رایگان و آنلاین توسط پزشک ویزیت شوند.
🔸
کاربران در این سامانه با تکمیل فرم کوتاه ارزیابی، شرایط خود را از نظر BMI، سوابق بیماری و داروهای مصرفی بررسی کرده و سپس با مشاوره رایگان توسط پزشک از شرایط مصرف آمپول های لاغری با خبر می شوند.
👈
شروع ارزیابی</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/685099" target="_blank">📅 21:20 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685098">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBimebazar</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VcB9UXd6eALX4GO19Y2zMTlTXqZ-6dwALxuJdX2-k69dFHLnkCPTapHUOx1RFKfLMCtIsaRSdWu-yt1lWtezyV5bNOxtWnkNw3Uj3c0qHEM99LpfAoRbb_JP2oeWJ4b7DXXYxjXwH-4bIo33MOZ7JpHgyh3pSw7PRurVkJN6Nxv8ZF0t_lfCBSl-iKNVagWU6F8hN5OkpIGFcN8-UeOAO6ebBKuqoIML7k8TS8wo9mCl7eGhUxEmopuOoQyIK27RhPvYMX3Mkk_44LV94NeKRerN7id_VW6i8hYCnEVqZx9VWBE63y2Ie1eTEcPpYTvP2AIdtMJXQsZG-kIw7tkmZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
بخشودگی ۱۰۰٪ جریمه بیمه شخص ثالث!
📢
طبق اعلام بیمه مرکزی،
از ۲ تا ۱۳ شهریور ۱۴۰۵
✅
تمام جرایم دیرکرد وسایل نقلیه فاقد بیمه،
به‌طور کامل بخشیده
می‌شود!
فقط کافیه در این بازه زمانی، بیمه‌تون رو تمدید کنید.
✔️
تا 2میلیون تومان تخفیف با کد
pnsc
👈
تمدید بیمه شخص ثالث
#بیمه_بازار
🟡
@bimebazarco</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/akhbarefori/685098" target="_blank">📅 21:19 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685097">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
روسیه: پوتین ۱۰ شهریور با پزشکیان دیدار می‌کند
🔹
دستیار رئیس‌جمهور روسیه روز جمعه اعلام کرد که «ولادیمیر پوتین» رئیس‌جمهور روسیه قرار است در تاریخ ۱ سپتامبر (۱۰ شهریورماه) با «مسعود پزشکیان» رئیس‌جمهور ایران دیدار داشته باشد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/685097" target="_blank">📅 21:19 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685096">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
رهبر معظم انقلاب: توجّه به نقش بانوان خانه‌دار که ظریف‌ترین اجزاء نقش و نگار فرهنگ زیبا و مطلوب آینده را در حریم منازل به تک تک فرزندان این مرز و بوم می‌آموزند نیز واجد چنین اهمّیتی است
🔹
امید است به‌کار بستن این مطالب و سایر مطالب مفیدی که بحمدالله در فهرست…</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/685096" target="_blank">📅 21:18 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685095">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de8fc458d0.mp4?token=sB0XahtsKUid2K8st09oGsgDMzDmPTb-5-rfccFEl1ZoJg3TvLRqKrrFR8-v41egZav0-a-_0OCtNpmyxznXAkJN8d_8MW75KXBhZe2LpAv7hDnCWMoaakP1Pjk07n_ACQXsd8Kiw9i5os11z6SkUMLlyI3JkATYtWA0qzxwL4Gh22vQe4OvdSSfoywA75gs8fULQ3y7SjbYSgRPb3F6gDj85DqYB0uSLNRkpIMWvaFUQDKnIucQSfMAij56KD_juT7GhBNfWYGfRBybdT9LxqDFJIO6JLrD5yLKceeWOEy7wwP6qKsUoi-CjYg5mr-O9jdxN0ZcAhOcBs6TVJ7cX4av9PVa7lMY8VYQiLyd-a7Q-eNee5zeBxWwFHLLEFvYeAsHP9lqQIzs8BfmZdO4a-K3uLdpKEIfuzOITtXRXtyRNee_eSAOonuaoNqskgeV36Gkz-38u7EFdckQB6dhhquqG8hhYbUFQPLe0XGnlfN_QKvZvZvJZmHn-KWIF8nfdP8ppAdyqoQ33dhkdDcXU8IkuQji6iFeel0ikdhEmkovZk3QZnesF7xbi8418kRF8TM0Wb77-K6Rg78wxW9iv8FvTxYj1tYmDu8HbFWjVuWbRqe7B2ZDWwMYnsDkpyVyqGlWYiUOyh0SEsqSIFr3IAnzuGwXctkW8AJ-0rmgL1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de8fc458d0.mp4?token=sB0XahtsKUid2K8st09oGsgDMzDmPTb-5-rfccFEl1ZoJg3TvLRqKrrFR8-v41egZav0-a-_0OCtNpmyxznXAkJN8d_8MW75KXBhZe2LpAv7hDnCWMoaakP1Pjk07n_ACQXsd8Kiw9i5os11z6SkUMLlyI3JkATYtWA0qzxwL4Gh22vQe4OvdSSfoywA75gs8fULQ3y7SjbYSgRPb3F6gDj85DqYB0uSLNRkpIMWvaFUQDKnIucQSfMAij56KD_juT7GhBNfWYGfRBybdT9LxqDFJIO6JLrD5yLKceeWOEy7wwP6qKsUoi-CjYg5mr-O9jdxN0ZcAhOcBs6TVJ7cX4av9PVa7lMY8VYQiLyd-a7Q-eNee5zeBxWwFHLLEFvYeAsHP9lqQIzs8BfmZdO4a-K3uLdpKEIfuzOITtXRXtyRNee_eSAOonuaoNqskgeV36Gkz-38u7EFdckQB6dhhquqG8hhYbUFQPLe0XGnlfN_QKvZvZvJZmHn-KWIF8nfdP8ppAdyqoQ33dhkdDcXU8IkuQji6iFeel0ikdhEmkovZk3QZnesF7xbi8418kRF8TM0Wb77-K6Rg78wxW9iv8FvTxYj1tYmDu8HbFWjVuWbRqe7B2ZDWwMYnsDkpyVyqGlWYiUOyh0SEsqSIFr3IAnzuGwXctkW8AJ-0rmgL1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حذف چهره‌های نسل اول انقلاب یک بی‌اخلاقی بود/ بسیاری از چهره‌های شاخص کشور خانه نشین هستند
نصیرپور، عضو کمیسیون اجتماعی مجلس در
#گفتگو
با خبرفوری :
🔹
نمی‌شود بنگاه‌های بزرگ اقتصادی دولتی- حاکمیتی باشد و بعد بگوییم مسائل خرد را دست مردم بدهیم.
🔹
در دور جدیدی از مدیریت با توجه به دسترسی به فضای مجازی یک بی‌اخلاقی را رواج دادیم که یکی از آثار آن حذف چهره‌های نسل اول انقلاب بود؛ نمونه آن آیت الله هاشمی.
🔹
ما در یک رقابت غیراخلاقی سیاسی یکی از بزرگترین سرمایه‌های‌مان را تا مرز اینکه از دستمان برود، رقم زدیم و خیلی از کنشگران سیاسی از این رفتار حمایت کردند؛ البته همه امروز از دفاع از آن شرایط پرهیز می‌کنند.
🔹
امروز شاهد هستیم بسیاری از چهره‌های شاخص کشورمان خانه نشین هستند به طور مثال حجت الاسلام ناطق نوری و حجت الاسلام ابوترابی کجا هستند؟
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/685095" target="_blank">📅 21:01 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685094">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f85050182.mp4?token=llSl0s-LES3Vk8VC6aWTw-j3Q9w-8Xa71NaTJMJaA8MX1RbF5mDl1Bvi1Z6hhZRfZy8Tbaj7M4qxV91SzYQW5Lr8qZvlIv4HlfCU8DCvhEobxA1JnqC8Sk1-eYkZZPsfxUvatdUnsZPkp7krwpQXVWxbksgTTQ8Gy3hiS6bdcrs4juDpHW3U2B2xz5KrNOFckjiTpQqI1AS3mb4OLwfjEcRW9vPwxjjm3mQhJeqOk7w4h8-QkEI_tHktHNqY7h-4sU5yVsAtKYJWOJwZd98HgNOyP7t9fNIEyP5u3VENO2mOg1id2xZpglreEE53j9d-N_mvyJP9C6ErLHJnU3eehAN4se_SD2cqQl0eVKZga-LLFmT39537ep1Ff3wroL-1uxJN_SgrtvPOsp_yZroaxjtoDrLqClP8OirR2ShwHc5_xA7QD8NliBjkqBgAYaSrX5VTWtjDJx-rKeAvKMkyzkUlTH_Ew1CO3H_YB-f8sMTSFWQ1e7YAsWFI5hjJv4TqnECRzynmfiA0mGBUrgZZd4MjCjAULfqA09HaLB38-8WpZ3EOfKMtfALsrOXngmC9UrilDtzWvA82yvVpk30L4cCwNNbtR5t05VrwBaC_o3FDfYo4kQMxoiZQEF87FBJRc165iy6F_AUHxmBfXoykpxAWXXgUcJnS-izVQFZLtvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f85050182.mp4?token=llSl0s-LES3Vk8VC6aWTw-j3Q9w-8Xa71NaTJMJaA8MX1RbF5mDl1Bvi1Z6hhZRfZy8Tbaj7M4qxV91SzYQW5Lr8qZvlIv4HlfCU8DCvhEobxA1JnqC8Sk1-eYkZZPsfxUvatdUnsZPkp7krwpQXVWxbksgTTQ8Gy3hiS6bdcrs4juDpHW3U2B2xz5KrNOFckjiTpQqI1AS3mb4OLwfjEcRW9vPwxjjm3mQhJeqOk7w4h8-QkEI_tHktHNqY7h-4sU5yVsAtKYJWOJwZd98HgNOyP7t9fNIEyP5u3VENO2mOg1id2xZpglreEE53j9d-N_mvyJP9C6ErLHJnU3eehAN4se_SD2cqQl0eVKZga-LLFmT39537ep1Ff3wroL-1uxJN_SgrtvPOsp_yZroaxjtoDrLqClP8OirR2ShwHc5_xA7QD8NliBjkqBgAYaSrX5VTWtjDJx-rKeAvKMkyzkUlTH_Ew1CO3H_YB-f8sMTSFWQ1e7YAsWFI5hjJv4TqnECRzynmfiA0mGBUrgZZd4MjCjAULfqA09HaLB38-8WpZ3EOfKMtfALsrOXngmC9UrilDtzWvA82yvVpk30L4cCwNNbtR5t05VrwBaC_o3FDfYo4kQMxoiZQEF87FBJRc165iy6F_AUHxmBfXoykpxAWXXgUcJnS-izVQFZLtvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاسخ به حاشیه‌ها؛ مردم حق دارند و اگر باعث رنجش احساسات جریان انقلابی شدم
#متاسفم
/ حل مشکلات اقتصادی مسیر خون‌خواهی رهبر شهید را هموار می‌کند
امیرابراهیم رسولی:
🔹
حرف من روشن است: اگر قرار است بر آرمان‌ها، خون‌خواهی شهدا و رهبری ایستادگی کنیم، باید برای کاهش مشکلات مردم و بهبود شرایط اقتصادی نیز تلاش کنیم. اتفاقاً حل مشکلات مردم، ما را به آرمان‌ها نزدیک‌تر می‌کند.
🔹
هم آرمان‌گرایی لازم است و هم واقع‌گرایی. نباید با دیدن صرفِ مشکلات، مردم را ناامید کرد و از سوی دیگر، نباید گرانی، فشار اقتصادی و مشکلات واقعی مردم را نادیده گرفت.
🔹
مردم حق دارند ناراحت شوند و متاسفم اگر مثالی که برای تبیین این موضوع مطرح کردم باعث جریحه‌دار شدن احساسات جریان انقلابی شد.
🔹
من محکم پای مواضع منطقی، اصولی و انقلابی خود ایستاده‌ام و معتقدم با حفظ وحدت، روزهای خوبی برای ایران در پیش است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/685094" target="_blank">📅 21:01 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685093">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ihZlkj1lQrbua-2U-TbQPDl3XLGyTJR6KvK5KlWww-8OUWusfUzdCbGNvmem6cTyONd51xnGtpy_08h9IGC_rlUj131anD5_TV8pWx3MUCmKS3541wG5SILUBtHKCeSf4Ltn0ka4_2X7CkC5DIYxSIZS0vL1zJyhpRRjv1sggWntPZjofD3YXgsEnAba_T4-5xj5BEUYjRmZlfDfR1XMOA4-4zPF0X55SP3K84POl8tPtzY0pm9fGsbsbRricrseo4HLj4h3d0wuz90rE_zjuqrk8WqSZsb5gvIrFfnvzko0v0vTmJbkAW7lO3ia0vL_Fc48gFuCEuDYorVxDUJ7mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس‌جمهور: پیام پرمهر و مدبرانه رهبر عالی‌قدر نظام به دولت چهاردهم و اینجانب امتداد حمایت سازنده و بی‌مانند رهبر عظیم الشأن شهید انقلاب اسلامی است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/685093" target="_blank">📅 21:00 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685092">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
رهبر انقلاب: هر اقدام در هر یک از کلان‌عرصه‌های فرهنگی، اجتماعی، سیاسی، امنیتی، و اقتصادی "باید" با ملاحظه‌ی پیوست مربوط به انسجام اجتماعی صورت بگیرد
🔹
بعضی از اقدامات که ممکن است در ظاهر، طرفدارانی هم در بین برخی از اقشار کشور داشته باشد، در صورتی‌که فاقد…</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/685092" target="_blank">📅 20:49 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685091">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
رهبر معظم انقلاب: هر دوگانه‌سازی‌ موهوم از قبیل جنگ یا مذاکره، وفاق یا تندروی، سازش یا جنگ‌طلبی می‌تواند به مردم عزیزمان خسارتهایی بی‌واسطه یا باواسطه وارد سازد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/685091" target="_blank">📅 20:48 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685090">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
رهبر معظم انقلاب: دشمن سعی میکند القاء کند که مسیر پیشرفت از خواسته‌های نابجایش میگذرد؛ در حالی که مشاهده‌ی آنچه او  بر سر این کشور و منابع آن آورده، خلاف این را نشان می‌دهد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/685090" target="_blank">📅 20:47 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685089">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
رهبر معظم انقلاب: عیار حقیقی مردم ایران در شش ماه گذشته آشکار شد  رهبر معظم انقلاب:
🔹
مردم عزیز ایران که در شش‌ماه گذشته عیار حقیقی خود را در جلوه‌های مختلف جهاد با دشمن، حضور در میادین، انسجام و همدلی و همراهی خود آشکار نموده‌اند، شایسته و مستحقّ آن هستند…</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/685089" target="_blank">📅 20:44 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685088">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
رهبر معظم انقلاب: گاه بیان صادقانه ضعف‌های خود در وقتی که دشمن به روحیّه نیاز دارد، کمک بزرگی به او است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/685088" target="_blank">📅 20:41 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685087">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
رهبر معظم انقلاب: قاطعانه اعلام می‌کنم ارتکاب هرآنچه به ضرر انسجام اجتماعی باشد، ممنوع است
🔹
رهبر معظم انقلاب اسلامی در پیامی به مناسبت هفته دولت ضمن قدردانی از اقدامات شایسته دولت به‌ویژه رئیس جمهور صادق و دلسوز که به‌رغم همه محدودیت‌ها و دسیسه‌های گوناگون…</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/685087" target="_blank">📅 20:39 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685086">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
رهبر معظم انقلاب: قاطعانه اعلام می‌کنم ارتکاب هرآنچه به ضرر انسجام اجتماعی باشد، ممنوع است
🔹
رهبر معظم انقلاب اسلامی در پیامی به مناسبت هفته دولت ضمن قدردانی از اقدامات شایسته دولت به‌ویژه رئیس جمهور صادق و دلسوز که به‌رغم همه محدودیت‌ها و دسیسه‌های گوناگون دشمن آمریکایی-صهیونی و تشدید تحریم ها و محاصره ها انجام شده است، بر لزوم تبیین و روایت «قدرت و قوت ایران» و برجسته سازی آن و پرهیز از  هرگونه سخن «ناامید کننده وتضعیف کننده انگیزه های ملی وعمومی » و «دوگانه سازی های موهوم» تاکید کردند: قاطعانه اعلام می‌کنم؛ ارتکاب هرآنچه به ضرر انسجام اجتماعی باشد، ممنوع است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/685086" target="_blank">📅 20:37 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685085">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db894ba0b0.mp4?token=msy_InvUCD4GimSjLFl4AYfVglYxzsV5oVaWWGXWxrUWELemwLdIJkeBXcqakM7osn6sGQkJkmRAJYaUKksH7KaOHAuPLHA0dBzOfNR9pc2U3HKbcoWEGUiPHqyTXiMKi_LwVFc15CIUX_WzWS-jh4j-C2JTqj-7BMf6Krn2lfSYnaX49FPe0TqDEVwK3JfWirPuzE_ceFxmPDlJRaBl4U2-qL05ZcMHpFHPdjy0U8wCBSTjrP8L6qq-CqPCuMyrId5Hj8wgorKnKeUZPAF4K5BcFjjR-RUkClS54ZJQiByMYB8QK0LSxWAh0TV515zpHg3h2vKWo4gh6XOAz_j3qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db894ba0b0.mp4?token=msy_InvUCD4GimSjLFl4AYfVglYxzsV5oVaWWGXWxrUWELemwLdIJkeBXcqakM7osn6sGQkJkmRAJYaUKksH7KaOHAuPLHA0dBzOfNR9pc2U3HKbcoWEGUiPHqyTXiMKi_LwVFc15CIUX_WzWS-jh4j-C2JTqj-7BMf6Krn2lfSYnaX49FPe0TqDEVwK3JfWirPuzE_ceFxmPDlJRaBl4U2-qL05ZcMHpFHPdjy0U8wCBSTjrP8L6qq-CqPCuMyrId5Hj8wgorKnKeUZPAF4K5BcFjjR-RUkClS54ZJQiByMYB8QK0LSxWAh0TV515zpHg3h2vKWo4gh6XOAz_j3qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اردوغان: اسرائیل به جنگ افروزی اعتیاد دارد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/685085" target="_blank">📅 20:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685084">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
نتانیاهو: تأسیسات نظامی را به زیر زمین منتقل می‌کنیم.
🔹
مقامات اروپایی: هیچ شواهدی از حمله احتمالی روسیه به ناتو وجود ندارد.
🔹
خبرگزاری فرانسه: چین اهرم‌های مناسب را برای تقابل با اقدامات ضد ایرانی آمریکا  دارد.
🔹
منابع خبری: پهپادهای یمن مقر مزدوران سعودی در المخا را هدف قرار دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/685084" target="_blank">📅 20:26 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685083">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
سقف فروش ارز به بالای ۱۸ ساله‌ها چقدر است؟
🔹
بانک مرکزی با اصلاح دستورالعمل نحوه خرید و فروش ارز به‌صورت اسکناس، سقف فروش ارز به اشخاص حقوقی ایرانی را از یک هزار یورو به پنج هزار یورو یا معادل آن به سایر ارزها افزایش داد.
🔹
سقف فروش ارز به اشخاص حقیقی ایرانی مقیم بالای ۱۸ سال تغییری نکرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/685083" target="_blank">📅 20:23 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685082">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4ca010c5f.mp4?token=ExILbQgzy3WCL_0oef9k7QnMDjMx9-9m8n8GUBR1KS6ZmeX2GnSbjehXAAq4o37LlzCJagVXLtiKHx1t843bVBUppPUTqPJO7mFxRsmWlMIoOaYnlh_TkqTzhRx3WyXOh12voPBIklW5Zebx8_nw8FgvFeQr6HtRO1nKGuypwCM3Y1yHz0l4p6e1ox0FmqPuat5GgvGpgWEL8LlM6cHfzql-TKhEe2RDrD1q8FnzX-zq7sT3rvcs5aCZ5P8IjLaMUZYU0k0YSB8xerefjGsSzijjYrSvZ9ODYrigJQqHTCyTliFTOA8Fbkexb0CwQ0wfks10SYMZXtHQrUYm0Nd0_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4ca010c5f.mp4?token=ExILbQgzy3WCL_0oef9k7QnMDjMx9-9m8n8GUBR1KS6ZmeX2GnSbjehXAAq4o37LlzCJagVXLtiKHx1t843bVBUppPUTqPJO7mFxRsmWlMIoOaYnlh_TkqTzhRx3WyXOh12voPBIklW5Zebx8_nw8FgvFeQr6HtRO1nKGuypwCM3Y1yHz0l4p6e1ox0FmqPuat5GgvGpgWEL8LlM6cHfzql-TKhEe2RDrD1q8FnzX-zq7sT3rvcs5aCZ5P8IjLaMUZYU0k0YSB8xerefjGsSzijjYrSvZ9ODYrigJQqHTCyTliFTOA8Fbkexb0CwQ0wfks10SYMZXtHQrUYm0Nd0_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعزام نیروهای مردمی به تنگه هرمز در پاسخ به اظهارات ترامپ
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/685082" target="_blank">📅 20:19 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685081">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZChmz7i62tGmyzlYtqQsq2t3Cj4kDzTVRxrO3cTzX5W2p4iZckRKvjuoD4N_JWpdTwFiKrgae06RkgHm6l5Vr3fSA298E_oxx9png4X0OLDOwyLoPonkNkh6VH8mBvVbPUQ5LOhPzx_SNSngUVPAnpSdc7eO5IcSSiQczenQq949OY4LAt_VQ9d5CqJXjYuVsfQt1C5IF4Eb5g4YO84mdHvhQWGw3ohjTah3WOAeTrLXTqxMQRUE-0l64Aax7R1jpo_vGBhCgCK3NQBP2QtWFuDL-V76czFZRkayRgjJVZ7UZtOFtVQNEDzWD1ZXDHLktfqqBsVemDNpfSTptEVszw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سرقت ماهرانه گردنبند تاریخی ملکه مصر از نمایشگاه "شاهکارها" در وین
🔹
گردنبند چند میلیون دلاری ملکه سابق مصر که به عنوان بخشی از نمایشگاه ویژه "شاهکارها" پشت شیشه ضد گلوله در موزه وین به نمایش گذاشته شده بود توسط  دوسارق حرفه‌ای که به عنوان بازدیدکنندگان "عادی" در این موزه حضور پیدا کرده بوند به سرقت رفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/685081" target="_blank">📅 20:18 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685080">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
دولت صنعاء: با هر هزینه‌ای به مقاومت ادامه خواهیم داد
🔹
دولت یمن امروز جمعه در نخستین سالگرد شهادت احمد غالب الرهوی، نخست‌وزیر سابق این کشور‌ و شماری از وزیران دولت بر ادامه مسیر رهبران شهید و پایبندی به مواضع خود تأکید کرد.
🔹
دولت یمن تأکید کرد که یمن، محل تولید قهرمانان و رهبران است و هر فرمانده‌ای که در میدان جهاد به شهادت برسد، به لطف خدا ده‌ها فرمانده جایگزین او خواهند شد؛ در راه خدا نه عقب‌نشینی وجود دارد، نه ضعف و نه سستی./ تسنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/685080" target="_blank">📅 20:16 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685075">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uFHAvI6tNWZshzwS023qteT8bJRCgee5mHeP-RojIDj8t7FcT5ow0PEv8zWKJkLJvTd02MxgpeF-gURzvSgj1ljXxnRFQ0m9klbKoEIj0srz7dvq5UnB2bCgGxOx2dwRAyGyOR6YuDkC_wMmRAKX5tifpe5Ghjkwe--Uj6EG-NiChrCmYm4YnX5uXluOW2q9HDM-c5Qal9vu57wxN24X62cFOYcCdrA4XdTjWUdZb7V5cbERb7x8OcbVC1kBQCh5nydQ9zvc0YtlPaXnhPFccj5ofXfHe1Sj76m7jhgoMOx_mCvYWq60iSP7wu0E8XO5nrSEc3ab6zBbAY4KxbCMsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qEDjol2I94fuT73bg-9cADr-CBrOam8p8gF3BLMXXq_SsZTMQY9F0pk7SPhin9aivAwdHw7CYfG3nZHwmAiyaU5UneHGGFsAt16K7eAQrg5Qk1q3EUPXhGd8BtmMg5dnuZDNu5qWNSukXBmH9Kyephb3nX8LfzzEQiGlN80pZEJSXu79XPcJxh4Ea9wFsoMDl3lREXNDNgGs7xuBPWSI8E56qnyMEd7jWYNP17UOAkIsZuv3uQDsXIxGW3iiZ4ZwcPTtEvyAmRoyNgqepgSOWCSNKs_XsH8XK57P06etGaQ5NoZgytdLJsLQ6PX5skINP4EMwIX5t4kOgX3SoGO_OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b6YDDj2-gzaqTdc_-pffay7OxbeJqll9y7tFTM9spq4IZZGq8_4Ig5IxM4atB9UXUSzfyE2WlT8KvpRTRWDATtqifBqlQSsNlogqn9Kves2dlNX-Zerpj6c3O3vr0Z9xXyZwS02y8-DT6QuJGtJ1cmOPFu_asyvQTx3yWzyL7FnWZMY1rB4MOj5fTRUpxMxT488PgocNRiu1ouC-CFLTAFwgaOM5cbj623z-CAseCr1R8ZpgxZhTfI_6TvRiHo6fsEbLZESL0mX203lGnuWgnbHzffY6Lnu1jJCV4jHRVmYGWX3VMR9ZSgtSlaA27ERXUyiJw-xmU2KXohy8-5l5-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j6FRZPu0Z1HvY0bZffoDs6qa_0wRWUQwya4U4mRW66u3gZEHjr78IEMhQZGsu8U6B7z1T7jGX6PPRfv7zW86mGxPgYT12rFZpQ4sFfsDYsBzVQLO4Fe_TNCX_8z83G8Wkvr3QXRqdU-l3QokPKtEkFv0TdeiY4sJ14VhvpAILoAgsZl2UzeBN-YA5KyKR9H5cRkK9h8f3MB6NUDgFeIw6pDekTfHGVDStzVrg5LAbjt5-LbvHpm6JgfXtO9is5E1FRlvZAtdazQGJ6IBUdiUeLsOlUGmn58fxxFmyB8Z_f09o7todBHxPRDXOdsHcGxdWwx0sKBIl525bruLeO8jgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/saS0Z9JpPCqBKGyhZDKr4SRAdo1gxUdqaSy7Shws2vNnTYAU0djDd3spDWPm-k9G0yASeGssZ9siEwSyVBlKLAGx55fY-1duybGweNAdIDnNgmsuXDLyzeOKRs1gNQeHJti3Nx62PjhSg34yfPOAbjdlbk4MvFFtJVnNofrhyRNxp6eAcwJxEZr0L-KZ9Ysoh-AB6XCLkCi7ocgFt4hZyCovfM7R_ECBLX7_p8vyrJuiqJRGNSV8YFrD4VS9JVGA1qszwT4Qf9FhovVj74w83jiQQbDWe1vAF5UvuewxiYi2mWBhSc2HfSeNb5OASyWo8AOBvW8tpHQMYiRaV3nX4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پاستیل کاملا سالم و خانگی بدون شکر و رنگ افزودنی
🤩
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/685075" target="_blank">📅 20:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685073">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">07-1 Ane Manaee (1403-09-01) Marghade Sheikh Sadoogh</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/685073" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه هفتم
حجت‌الاسلام امینی‌خواه:
🔹
سوره محمد (صل‌الله‌علیه‌وآله): روایت عمل و پاسخ عمل [2:09]
🔹
ضرورت؛ نیروی پنهان پشت هر عمل [7:27]
🔹
حس نیاز؛ خالق ضرورت و عامل حرکت [9:36]
🔹
از کنسرت تا رفع فیلترینگ؛ عملیات نیازسازی در انتخابات [11:10]
🔹
انتخاب‌های ۲۴ ساعته در زندگی؛ مدیریت عقل یا اسارت هوا؟ [13:02]
🔹
فرعون‌ها همیشه هستند؛ مدیریت جامعه با فریب و نیازسازی کاذب [17:57]
🔹
طبقه‌بندی انسان‌ها؛ از فراعنه باستان تا حاکمان امروزی [19:24]
🔹
از استادیوم تا خیابان؛ نبرد بر سر فرهنگ و هویت ملی [26:15]
🔹
ایمان فقط در ذهن نیست؛ "عمل" کلید ماندگاری باورها [34:26]
🔹
سید جمال‌الدین گلپایگانی: داستان نور، عطر و یک معاشرت اشتباه [44:40]
🔹
حافظ و لطافت ایمان؛ قلب شلوغ، خانه ایمان نیست [47:47]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/685073" target="_blank">📅 20:08 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685072">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e90251a38.mp4?token=NM3Ml5gZ2YPkMVKCi3q2RuqpuRMgs3LZISeaj7qcFeIR3NZBhHuQUr9V5OOG-pxmfFNo0fVidkOlb4V6-DbGrHp2LA9R48qP8kxUbWunrY3uZXQSJjpyQQDdT5kLhGmB0vq6JgwlWNxoJkohsnA37DPLNhL04KReg4jBZF-eLsTkNF26lD6yy0Yn_D0lu1KesaxynXcS_Wce-qD8KKTuSHe6tlsS0jF0lvsETbV09Q7sPp29HlHbZqwiDRquWcQAf6-FuD8ncrezgUuJnkI3yAhRlEJo8flSqVssNLdi-LNy--ZPZTbtwQh3ExsIQmqz0-kq7VCRxZd6ZHuQbLRd9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e90251a38.mp4?token=NM3Ml5gZ2YPkMVKCi3q2RuqpuRMgs3LZISeaj7qcFeIR3NZBhHuQUr9V5OOG-pxmfFNo0fVidkOlb4V6-DbGrHp2LA9R48qP8kxUbWunrY3uZXQSJjpyQQDdT5kLhGmB0vq6JgwlWNxoJkohsnA37DPLNhL04KReg4jBZF-eLsTkNF26lD6yy0Yn_D0lu1KesaxynXcS_Wce-qD8KKTuSHe6tlsS0jF0lvsETbV09Q7sPp29HlHbZqwiDRquWcQAf6-FuD8ncrezgUuJnkI3yAhRlEJo8flSqVssNLdi-LNy--ZPZTbtwQh3ExsIQmqz0-kq7VCRxZd6ZHuQbLRd9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کافه خواهران بابک زنجانی پلمب شد!
🔹
برخلاف آنچه در برخی روایت‌ها مطرح شده، این کافه تازه متولدشده نیست؛ سال‌هاست فعالیت می‌کند و مالکیت آن متعلق به خواهران بابک زنجانی است.
🔹
حالا کافه تنها چند روز پس از افتتاح مجدد، پلمب شده.
🔹
برخی منابع مدعی شدند این پلمپ بخاطر موضوع حجاب پلمپ شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/685072" target="_blank">📅 20:07 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685071">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4775207fb6.mp4?token=u9NoEVZA2pX9fLaFoz896CkX0bGqMgakn6RThP4QvgxFj4BgVRckWXAMc8NobHmoH43QS18f8ItRWf0Dd4TyqY8fk3HXVXNS7BMkhVWy1ES2sNnLyuva2v6X0UMsKlub7kap50Jwg9hoTqHiDf_YfV0cWt5CMZ2YctMhb0K_iJzcmLGeV86-8eowyZjBqSjgqRA2YZ8yKWzvGji1u33QyDWPXWeqnpJnen-IUZXWOTqiHsGjPWykOUMO2RWZblDuUUPviaKrRwm781s1yy0T2jwcw15UPeNeQfWAireZ5WzJHpUq2Jgoz01rYwv3v1FK9z_BUcmcuYWuSlWKNp-HaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4775207fb6.mp4?token=u9NoEVZA2pX9fLaFoz896CkX0bGqMgakn6RThP4QvgxFj4BgVRckWXAMc8NobHmoH43QS18f8ItRWf0Dd4TyqY8fk3HXVXNS7BMkhVWy1ES2sNnLyuva2v6X0UMsKlub7kap50Jwg9hoTqHiDf_YfV0cWt5CMZ2YctMhb0K_iJzcmLGeV86-8eowyZjBqSjgqRA2YZ8yKWzvGji1u33QyDWPXWeqnpJnen-IUZXWOTqiHsGjPWykOUMO2RWZblDuUUPviaKrRwm781s1yy0T2jwcw15UPeNeQfWAireZ5WzJHpUq2Jgoz01rYwv3v1FK9z_BUcmcuYWuSlWKNp-HaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سعدالله زارعی، کارشناس مسائل منطقه: افرادی که صحبت از صلح شرافتمندانه می‌کنند بدانند که در شرایط کنونی صلح به معنای تسلیم است/ هدف آمریکا تسلیم جمهوری اسلامی ایران است و هم‌زمان با پیشنهاد مذاکره، تهدیدات و فشارهای خود را بالا می‌برد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/685071" target="_blank">📅 20:01 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685069">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
به گفته برخی منابع، یک افسر امنیتی اسرائیل در یافا کشته شده است
🔹
طبق این گزارش‌ها، تیراندازی با سلاح گرم انجام شده و عامل پس از تعقیب پلیس با پرتاب نارنجک از محل گریخته است؛ با این حال، روایت رسمی رژیم صهیونسیتیاین حادثه را یک قتل جنایی شخصی توصیف کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/685069" target="_blank">📅 19:59 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685068">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
پیام رهبر معظم انقلاب به مناسبت هفته دولت تا دقایقی دیگر منتشر خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/685068" target="_blank">📅 19:58 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685061">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I6hZLEPbQoL4l2_izi5jTnY4YbYEpopRieWpNoJyw9iM8TeIvTAqZRpllzVAoXi6sDD7ButJolfaNJzf6VzY3wES-2A8T3G2MQMzZNbsZxPOFxmpUEEMIhG_aT-T_XdQYf1GJFdDMjWVnB70THGwQYjHFTJB8TOsTSVqBxNtXo1h6rJXsZyNmQGG6WzrRAoxCkntnXXhEktlN-c2QbWADuLvVK2qPYmpTNkrpUkeVNnsWxPHVmJK2kq1ucd5vqoJWT6MyimnZCalz421XOUyMVM29YphxV6Jr05oPnP9hpwWtGL3KR908NDKK_7R3uKLh2lfZUqwxjd29rndzX_Thg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WPXVEPyPg09V90qodF9TMjrW9vpKBaUfht5RxG9oTqpiwUETmRiWU77A1Wmi1QsO0Ij9R8rIE_WHIGsv7h1wL6FSm0Jx0Vz8oUw0rfUavN0aYsI4m9FBTShC34EPwMH2TPExDZuapHMGjy06f56B5K3opK6zpFtn5QYXtkbMKJyHGGdMIgOBY2mfl7EbPesQIzUTqIPVKduBjawm4Fp6jhsusBeugvbTgpZOyzApJjvZeaC4HUjR5bpKKdRCOCUT8Kx6NM56uJZYy8a6vwUbf25NcZeNpT1e9bNzi9TvsmzCGVUZ-0U9HqBZlCxTthSOUS4YLGBq_a9-Zg9v9pylHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FKkNU58sg6oD3GxEXE2d6-ebe31FdQpJ91h2OW8-TNTI69MggLWH-2UNBT0gb_rY_nAeVWGXvgY9zQWFSTCR99zW9DS8vTDQH6uWNeZ7K5I1j7t9DYPHpOkbQ-cyth3o4wsRhXrQooMtsWqFrwQZhZqNY0Qy-4_TDR3mu0jI-bV6bBlESdH5lLjxjy_UuBNt9eegnUYN_GujyYfNdMm-A93vMj579b5Io08NUvozgPdk8TlyuiKtgn08rBlS7vQa4iOLL-eSbrXgjQrFU8i0sfTlJd718ixfWP2KaAn9uWuMFtEJAWPlcqVhYp8IOvW6TpZ_PXox-6_VtjeHPUyuQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MWgUIcOmtYVkQShJCKMSAoXo_VOrVSU3Hs8XJdhnHGzKJ8I32fabOgDlYpQyOiZf8pmJoUChea61Af1L7K8nTQLe251a8fa44n-Y2EKiys4UKEVHWFXZwmWDqyL2URYJJQxRwaFOO6uXpQU29KGT12KNzJSh04cWYJ_qSkXXd486Y08PoMo20Si23unmugoAEhLLeGQAmFF0whnVOnYxq9fdBUc6kM3_X8pbu4OMPDeq0qjo4OvgmpFLJTdJO8njKqI9vkNgwJ_s9ZsXNP2_LAC03hJlLp0znsd-Le7_xcMphM63XWqAvwJrAlFdF8-Pb6EfsX1EAJ1jPBBPBh_Vpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/En1hR94stz2xEs03qOR6BTanfkWhOi737cy45wdyed4CFOmENhnlJR_D3j8N5JrNk4GLRp0wAzRnVmUHFN6H2soY1zreSpuVNHGBGSXru6_AZ8WIKPKD3MJLdD9c1uLi0bx4G0wSPq_6SeCAeC5Rw8euAqhMErd1YoiOWYQvc3Zfyj3FhwxJy5gpSBKrwwI5epenHM6t0oY7-GF1qvN_dnt_oFSKCVvQ8dluf_ZE7WImcAlrIe8422jCd7ye_rJTZ-pi7X7g6izcc9apxK51Xld22J66u5NnIm97Ff-d5Q9PUkW1gs0coE4e4bAtI8x0V48iDIgfeEH6pg1hDlwzNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nRwVCGHTPu8NxbUC8nUQRA4cq4d739Wyly8uH7WT09LTsFCXi2hA8i-VQDB1IY-oGI5LtrhAeCqiGnjxPAwibu3SO6QKktWFRVle34xjZrCieFQV1P0H6mZIu2rinqjoi7zu8GOD2Zy0wSFF3m3oO42bVeyF4-9hCVJ_6eslhcpb01kcD9xU74rbNDxdA3Pp1cwNnpJTYRej-ouoPOw3oBhnFanWMgbrvD47KQnhv0kgWFs8U4Z3rVjZtzFP3ikXefsu8-x1826_OB7FJAnFFS80s0aB5WQJY9tZ8or5EjSObRYJ1g3t787zhW6hc-91OcaKua0tXScEJyvjNltuiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NoZ7PU9003sayvqrIU1UApUWddCdwOtkIyy2Cwt1Vg93P5HWhe5MP1x8Lr1eZ9STuuYDjKlxsJoennASa5txtvtGCBWoRuL66MtESzmWo_hHz41ntZHQ4RB6RYfQS1txgXz0C8IqX2fxrRXbqoCsQbl9IfeO8CbE5jg1OqQH8vpKLqHZSLcD66bLl2nk9UY0oPaOR-HlIGcd7-a3G4R5XXN-YuQ5pg86R5bfLVZuRBWefbgLnCYIWgfQUOPJMt4e8Dteu0NXvcgv7yUYjoRXYgh_kzoI6g1ICZFa5HWDnf8Hho9-QQbEjLLD0F1rSf3rqxsnAW8iMUOCoqxefgRGRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💫
روایت اثرِ یک همراهی
💫
✨
هر همراهی، وقتی به نیت خیر گره می‌خورد، می‌تواند اثری ماندگار بر جای بگذارد.
🌱
#هیات_قرار
با همراهی شما مردم عزیز، هر روز با نذر و قربانی و توزیع گوشت قربانی، در مسیر حمایت از خانواده‌های حائز صلاحیت، این اثر را ماندگار می‌کند.
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇🏻
@Heyate_ghararr
شما نیز میتوانید در این کار خیر سهیم باشید
👇🏻
5029087002135690</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/685061" target="_blank">📅 19:55 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685060">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
هلاکت ۱ نفر و بازداشت ۶ نفر از گروهک تروریستی جیش الظلم
سخنگوی فراجا:
🔹
ساعاتی پیش، در درگیری مسلحانه دلاور مردان انتظامی سراوان که با همکاری سپاه و سربازان گمنام امام زمان (عج ) شهرستان با گروهک تروریستی جیش الظلم صورت گرفت، طی دو عملیات ضربتی و غافلگیرانه، یک نفر از اعضای گروهک به هلاکت رسید و تعداد ۶ نفر نیز بازداشت شدند.
🔹
در این عملیات، مقادیر زیادی سلاح و مهمات از جمله ده‌ها قبضه کلاشینکف،  نارنجک دستی، آرپی جی ۷، حدد ۲۰ ‌کیلو گرم مواد منفجره سی فور، ۱۵۰ تیر فشنگ جنگی و چند دستگاه ماهواره استارلینک نیز کشف و ضبط گردید.
🔹
نفرات بازداشت شده، از عوامل شهادت همکاران انتظامی در فروردین ماه گذشته در سروان و نیز عامل شهادت یکی از کارکنان سپاه پاسداران در ماه گذشته می‌باشند.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@akhbar_sob</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/685060" target="_blank">📅 19:51 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685057">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5Ym-RsEzrBa8tKRANjtfFfyHOOmJ-NUtxJuerdymg6JSF2h9f4EFcaM29QNNwinX8Y0TEfUTJQiYaXmTsAyK9BrGApNPYJdQpeOfhk8D6eqfXXLTX7LbD-evBGjCbfkm89JI2XrjNwDuma4067J1dST4dsQZ02YX5IrejCVjHFRPZP16qwjEpa5oeoZPyeVgeGrCZTadTZiEpLND1fDJUQc9yrP2xfBqr5fvy-NtDHArHZXMqlQoveP79h6Jgol1aKO7ILdI1hDHBsa2t6LTUzLJkU3U_Jtc5GhNG5i4jU4gAqHrAlVBlV8CTtgKpW8JB4i3bVi0p53JJPh-DedBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاربر آمریکایی: ایران آمریکا را در جبهه اخلاقی شکست داده است
🔹
ایران حتی یک غیرنظامی، یک بیمارستان یا یک کودک را نکشته است؛ ایران برای همیشه بساط موعظه‌های اخلاقی آمریکا برای دیگر کشورهای جهان را برچید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/685057" target="_blank">📅 19:39 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685056">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
در سفر وزیر کشور به خراسان جنوبی چه گذشت؟
🔹
در سفر اسکندر مومنی به این استان، به مناسبت هفته دولت، ضمن افتتاح چند طرح از جمله کارخانه تولید کاشی و سرامیک، واحد هیدروکربن، اعطای سه مجوز سرمایه گذاری بی نام، نیروگاه خورشیدی ده مگاواتی و بهره برداری از ۱۷۸۲ واحد نهضت ملی مسکن، به مدیران استان‌ها ماموریت داده شد تا نگاه‌شان صرفاً به استان‌های همجوار کشورهای همسایه محدود نشود بلکه باید ظرفیت کشورهای منطقه نیز مورد توجه قرار گیرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/685056" target="_blank">📅 19:38 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685047">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KMtEMMM95Cloe5eHI-pTM-ObtmLCXzfI580CsKX_BEVa4-UO0G8wBCgg3hivEIt970kNlAMQuy2AZk7X0gMgT3081dL5cI1DsMphHKEnm6nJR7ASo6TYHiN554BAOpAellshftchnhfdWsGxLGKFhFB5nhrpjr_i-oeODfKLa5Qu5XA0D9VukhEydyCG3yBR7HzsyddZGhxw1dSF3tvhRLasJpKTC21Il-bGLL33cVnYTSVP-4IvLNo2lj9xwIPH1IRTeaTUJg7zxIZ-thQtc8HKNPQ2LkrqEsA4hBpLmHtmemY3CkKYUXcPo9moTUufEkJSBSbKXoXImTHFFzcVcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
والیبالیست‌های زیر ۱۷ سال ایران فینالیست جهان شدند
🔹
تیم ملی والیبال زیر ۱۷ سال ایران در مرحله نیمه نهایی والیبال قهرمانی جهان با نتیجه ۳ بر صفر موفق به شکست آرژانتین شد و به فینال این رقابت‌ها صعود کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/685047" target="_blank">📅 19:29 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685046">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c3e46a6a8.mp4?token=aZmYegDUwYqRC2buf_nsb6JB7fqOZ8eDgAP8dovrPIRY9shWZ0h4V-OINna3cVKlHianzGOO-8SSkCdx-_jyD2ua2afRdm0Fty6tnFPwBzCBvD1AQdkW1DqCzbkb4vFhfzKXPgQZSUmX4GGCMfnp-9bSUtv-2Hh9YM3ChJ8MRhQojz_yceu-5yg_2lVgDndrx4OXnkvVoajkw7ONt9poInqn9VoadXwfpv1ZtQxn2gZyeYlUFl6xrW_uZOCVnOjPwnCxoVycqe7bQi22Z_RYDiFVWwEwhdCVmeQ09eCXljAGIuqSXRsJ1SMUxH_ms3k0vAZG50PzprZwPIhjFGhwKTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c3e46a6a8.mp4?token=aZmYegDUwYqRC2buf_nsb6JB7fqOZ8eDgAP8dovrPIRY9shWZ0h4V-OINna3cVKlHianzGOO-8SSkCdx-_jyD2ua2afRdm0Fty6tnFPwBzCBvD1AQdkW1DqCzbkb4vFhfzKXPgQZSUmX4GGCMfnp-9bSUtv-2Hh9YM3ChJ8MRhQojz_yceu-5yg_2lVgDndrx4OXnkvVoajkw7ONt9poInqn9VoadXwfpv1ZtQxn2gZyeYlUFl6xrW_uZOCVnOjPwnCxoVycqe7bQi22Z_RYDiFVWwEwhdCVmeQ09eCXljAGIuqSXRsJ1SMUxH_ms3k0vAZG50PzprZwPIhjFGhwKTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
می‌دونستی که نشاسته این همه خواص داره؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/685046" target="_blank">📅 19:27 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685045">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
الیاس حضرتی: پزشکیان در این مقطع حساس و پرحادثه با دو مؤلفه صداقت و سلامت توانست اعتماد مردم را جلب کند
رئیس شورای اطلاع‌رسانی دولت:
🔹
پزشکیان با سیاست گوش شنوا، راستگویی و دعوا نکردن امید را پایه‌گذاری کرد.
🔹
نسخۀ دکتر پزشکیان برای مسائل حل‌نشده، همدلی، هم‌زبانی، همبستگی و اعتماد است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/685045" target="_blank">📅 19:26 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685044">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
سازمان بین‌المللی دریانوردی: هزاران دریانورد همچنان در تنگه هرمز گرفتارند
🔹
حدود ۶۰۰۰ ملوان و دریانورد در ۴۰۰ کشتی، همچنان قادر به ترک تنگه هرمز نیستند.
🔹
وخامت امنیت دریایی در سراسر جهان از دریای سیاه گرفته تا دریای سرخ و خلیج عدن برای همه ما زیان‌بار است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/685044" target="_blank">📅 19:22 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685043">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
ان‌بی‌سی‌نیوز: محبوبیت ترامپ پس از جنگ با ایران هیچ‌وقت بهتر نشد
ان‌بی‌سی‌نیوز:
🔹
آمریکایی‌ها از همان ابتدا به جنگ ایران تردید داشتند و از آن زمان تاکنون، اعداد محبوبیت ترامپ بهبود نیافته است.
🔹
آمریکایی‌ها پس از شش ماه، همچنان نسبت به جنگ ایران و نحوه مدیریت این درگیری توسط دونالد ترامپ، دیدگاهی منفی دارند و همچنان می‌گویند که با این اقدام نظامی مخالف هستند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/685043" target="_blank">📅 19:18 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685042">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمداحی نور</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بی تو ای صاحب زمان،بیقرارم هرزمان(واحد)</div>
  <div class="tg-doc-extra">@javadmoghadam_tehran</div>
</div>
<a href="https://t.me/akhbarefori/685042" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بی تو ای صاحب الزمان، بی قرارم هر زمان
از غم هجر تو من دل خسته ام؛
هم چو مرغی بال و پر بشکسته ام</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/685042" target="_blank">📅 19:10 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685041">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kb_PTVwAjikxaUYKdlQrpyiaKsJovPwOcNbhlKb1Sc22mRucKIjuDx_p7YtZya0htm1TBzP1Jout47wgHFV1DjU7JN-ceoLH7YQdwLubQw9lGB1Sp3_Ay8oytYPxBUpVeUoZBNxQPY2z6yE1wK7VW8xVhtrmLYcr4K-VLlZg_7SMmWaNhxW9lyGhWNaQ0BIqZ4Q4Rz9aMRKRCYMHRpeEhJA6dI72U1uTd78bBvzq1Bd6m0G04AMxjwXaGUZ6jcaMJSlodh_9QMU6Ctr_vD1HKezAY_zuV0Av5NpGuUkKuO2GG2N9_C3Kv5Ylsxv5UMvU0aaAERy9PMnGjVuWivedRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شرط ازدواج شهید لاریجانی رفتن به آمریکا بود
همسر شهید لاریجانی:
🔹
یکی از شروط ازدواج ما این بود که ایشان برای مقطع دکتری به آمریکا برود، اما با پیروزی انقلاب و شهادت شهید مطهری، این مسئله را کنار گذاشت و گفت: از امروز برای جمهوری اسلامی کار خواهم کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/685041" target="_blank">📅 19:09 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685040">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
مرشایمر، دانشمند علوم سیاسی: تقریباً تمامی کشورهای جهان حامی ایران هستند و در برابر آمریکا موضع گرفته‌اند.
🔹
نوجوانان هندبالیست ایران به یک چهارم نهایی مسابقات آسیایی صعود کردند.
🔹
روسیه: پیشنهادی برای شروع مذاکرات با اوکراین نگرفتیم.
🔹
جنگنده‌های اف۱۶ یونان در واکنش به ورود پهپاد ترکیه به حریم هوایی این کشور به پرواز درآمدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/685040" target="_blank">📅 19:07 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685039">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نظام پاسخگویی ما نظام دقیقی نیست/ سه قوه در حداکثر اختیار هستند که این پاسخگویی را کمرنگ می‌کند
مجید نصیرپور، عضو کمیسیون اجتماعی مجلس در
#گفتگو
با خبرفوری:
🔹
به یکی  از روسای جمهور گفتم می‌توانیم شما و دولت‌تان را استیضاح  کنیم و عدم کفایت بدهیم، شما در مقابل ما چه حقی دارید؟
🔹
با اینکه نفر اول اجرایی کشور مستقیم توسط مردم انتخاب شده، آن گاه مجلس می‌تواند عدم کفایت رییس جمهور را اعلام کند، اما رئیس جمهور هیچ حقی ندارد.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/685039" target="_blank">📅 19:04 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685035">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HhgV6hwiDTxb54o0tQQUvJpE-sXAdenwG6HxQ3LZG4BeM4Xi5WMPOJTo3GYAuChDuoZVD6HvA5zatYOJQweNZ66x7OYyPwdBtCrW-L3MEPzCJdwTuQwsy7LKP_eEFprpr3hwEJSy8oOHlfrhR8fhzKglGqS6K-fBJVpk6aV5ZJfENg-PRO87Kz73Pt3ElZXspFWl50hCywCjwZUcP6f5lEj29MJogjYQ6Z1_cVGEutjRfSj72UqtbcxVTQfYCjquFtW1wWtWOPQFupAmA9aOs5F7AiIdi_M_yGBUoU9LbwY3--txrQFfzrXHu2EbT85EEfbVf1eggrqmvqzUO8J7jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بورس آمریکا قرمز شد
کوین وارش، رئیس فدرال رزرو:
🔹
تورم هنوز به اندازه کافی کاهش نیافته و اگر فشارهای تورمی ادامه پیدا کند، فدرال رزرو ممکن است برای بازگرداندن تورم به هدف ۲٪ سیاست پولی سخت‌گیرانه‌تری اتخاذ کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/685035" target="_blank">📅 18:56 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685034">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eebf909cc1.mp4?token=OV9-CHbj6Yd6XRSb1UJcmQ_sQMWs-uLhIR_Wi6gdFlB85ex76xD7DG9ijASVu6Dx_MhTEbxzo7GJvPqSaIq39YAosPvIb--r_7mm6jifZfx5Dps675MmQmb7I6H7DAVijR92wEUUrHtWIDjIwBmGunmbyPX2LBkptqgqBcvJJjV1blmezA8ME92W4DHzRxp4CBWBVdzRSDRUJ6ZBljKFt-c0Da4tyzbUDiocJr3r2Ma4vl__dtmbZtv4pPGRyELC4qS0KrAtumCdjHlubvd9h3RB-7mFLQh-xa6qb4lCjug6qJgqlQz6sYupfRMTn8AOHZuzqpoOhAYEy7QqUV-9MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eebf909cc1.mp4?token=OV9-CHbj6Yd6XRSb1UJcmQ_sQMWs-uLhIR_Wi6gdFlB85ex76xD7DG9ijASVu6Dx_MhTEbxzo7GJvPqSaIq39YAosPvIb--r_7mm6jifZfx5Dps675MmQmb7I6H7DAVijR92wEUUrHtWIDjIwBmGunmbyPX2LBkptqgqBcvJJjV1blmezA8ME92W4DHzRxp4CBWBVdzRSDRUJ6ZBljKFt-c0Da4tyzbUDiocJr3r2Ma4vl__dtmbZtv4pPGRyELC4qS0KrAtumCdjHlubvd9h3RB-7mFLQh-xa6qb4lCjug6qJgqlQz6sYupfRMTn8AOHZuzqpoOhAYEy7QqUV-9MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شاهین نجفی سال ۱۴۰۱ خطاب به رضا پهلوی: پول توجیبی‌ات را هم از دیگران می گیری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/685034" target="_blank">📅 18:41 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685032">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c905721e7.mp4?token=OAUJj8qNJWQ6fzwxP6UqD4R833uL3gEsrmcQqodRNb3iXNVpp7QZS4Tjv_U6ooCprz6nzEzg1YOXokwgszbCxgPFNz0Co2CIfxGTUA0VDzRFMQ4-FAilmUylJ5EMAF0GGLkm3YSU9A3U_4cNHuUEgHFnHV5GPIRH43OR4XqyxvCp6suMtW79elzAluD1uXOgK7g-8XXYD19HEGszhSAVJLxhpE3Xa5noj5h6a2EttrqJWsjkhvxdOliGW4jhLc091SHoKgXbXd0cyzPR1_5qXI662kqjpXziybdpc4vWJh_trIU4FR6fpt2xgSTFHTm5jkLPg_S4-S4ENfL4yr9EpFGk40Tn3QuETP6F6wtgBAb5L15Oj5U62Vew1pwo87CSw5iMwNl65qNr_Sd5KeQ9BmwpStpAhFoKy6W1v-K_H51LQWZdtDidbzZz1zLGLk6OpUQ1WvUcYfWcIF6FkSs-Ckgs4E73R7r0fq3iM-ICvcMjlvABIs9AGScu5XIUFi8OafG0PHFJtMV6heURntBp1p_tDuBedM8gyUGbnb2916XAgy1aGTs2X6zGKPOORCTDfhMk3ZXY1hq7xY8WbMREjq2qjXZjncGcgnb8-sWD07TOH_tNf5QNpcQkW8OOQPZaFR9bHWoyjtId11b7yCPWR1T1OFoXxsBXL24b7fwLJP0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c905721e7.mp4?token=OAUJj8qNJWQ6fzwxP6UqD4R833uL3gEsrmcQqodRNb3iXNVpp7QZS4Tjv_U6ooCprz6nzEzg1YOXokwgszbCxgPFNz0Co2CIfxGTUA0VDzRFMQ4-FAilmUylJ5EMAF0GGLkm3YSU9A3U_4cNHuUEgHFnHV5GPIRH43OR4XqyxvCp6suMtW79elzAluD1uXOgK7g-8XXYD19HEGszhSAVJLxhpE3Xa5noj5h6a2EttrqJWsjkhvxdOliGW4jhLc091SHoKgXbXd0cyzPR1_5qXI662kqjpXziybdpc4vWJh_trIU4FR6fpt2xgSTFHTm5jkLPg_S4-S4ENfL4yr9EpFGk40Tn3QuETP6F6wtgBAb5L15Oj5U62Vew1pwo87CSw5iMwNl65qNr_Sd5KeQ9BmwpStpAhFoKy6W1v-K_H51LQWZdtDidbzZz1zLGLk6OpUQ1WvUcYfWcIF6FkSs-Ckgs4E73R7r0fq3iM-ICvcMjlvABIs9AGScu5XIUFi8OafG0PHFJtMV6heURntBp1p_tDuBedM8gyUGbnb2916XAgy1aGTs2X6zGKPOORCTDfhMk3ZXY1hq7xY8WbMREjq2qjXZjncGcgnb8-sWD07TOH_tNf5QNpcQkW8OOQPZaFR9bHWoyjtId11b7yCPWR1T1OFoXxsBXL24b7fwLJP0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تهیه شیره خرما به روش هزار سال پیش؛ یکی از قدیمی‌ترین روش‌های شیره‌گیری خرما
🌴
🍯
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/685032" target="_blank">📅 18:27 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685031">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
۷۵ درصد واحدهای پتروشیمی از مدار خارج شده در جنگ، به مدار تولید بازگشتند
احمد مهدوی ابهری، دبیرکل انجمن صنفی کارفرمایی صنعت پتروشیمی در
#گفتگو
با خبرفوری:
🔹
در روزهای نخست حمله به واحدهای پتروشیمی و تولید انرژی، حدود ۷۵ درصد واحدهای پتروشیمی از مدار خارج شدند اما کمتر از دو هفته بعد با تأمین برق از شبکه و نیروگاه‌های دیگر و مدیریت تولید بخار، همه واحدها به مدار بازگشتند.
🔹
واحدهای پایین‌دستی نیز برای مدتی دچار مشکل شدند اما با بازگشت سریع تولید، صنایع پتروشیمی اجازه ندادند نیروهایشان بیکار شوند و اشتغال خود را حفظ کردند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/685031" target="_blank">📅 18:20 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685029">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f71897428c.mp4?token=Br3Yhd7O6X_AfA3eIZ4wjniq9gidyxIonFT1opul8-5i5LBU58sPOHK4ytOcajdJVgFWZsvx2gAp_pp_TpCT7qpxyy9gwkwBRsp1GhN7c6t86zc69qJwvRsNC2kEzektKABhfZXyQq-WhDka8k2Ns-gZZMeP8h3sFG3DnDhfMfRj5P75y1rDv1rhjGLtlZJCbIwxa5H65T_U9hrhIRjUFP4zq8aqW_81VpaZb11X3LK3b4bTTszvh1bbMYywQc7KkRM5_HjiaLIC5ac6Y29EKyrfuaP9IBKrimDhC-iQomae9Z2PSF-FuuV2wUz_KiFov2HV5S-V887-uPbuRN53UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f71897428c.mp4?token=Br3Yhd7O6X_AfA3eIZ4wjniq9gidyxIonFT1opul8-5i5LBU58sPOHK4ytOcajdJVgFWZsvx2gAp_pp_TpCT7qpxyy9gwkwBRsp1GhN7c6t86zc69qJwvRsNC2kEzektKABhfZXyQq-WhDka8k2Ns-gZZMeP8h3sFG3DnDhfMfRj5P75y1rDv1rhjGLtlZJCbIwxa5H65T_U9hrhIRjUFP4zq8aqW_81VpaZb11X3LK3b4bTTszvh1bbMYywQc7KkRM5_HjiaLIC5ac6Y29EKyrfuaP9IBKrimDhC-iQomae9Z2PSF-FuuV2wUz_KiFov2HV5S-V887-uPbuRN53UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شکست دو آزمایش اولیه پهپاد ADD کره‌جنوبی
🔹
هر دو نمونه آزمایشی پس از پرتاب سقوط کردند؛ بررسی‌ها علت احتمالی را مشکل کنترل در ثانیه‌های ابتدایی پرواز اعلام کرده‌اند.
🔹
گفته شده هزینه ساخت این دو نمونه آزمایشی حدود ۳۵ میلیون دلار بوده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/685029" target="_blank">📅 18:15 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685028">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
ادامه خصومت دولت تروریستی آمریکا با ایران   الجزیره انگلیسی:
🔹
دولت تروریستی آمریکا در راستای ادامه سیاست‌های ضد ایرانی،  تحریم‌های مرتبط با ایران را علیه یک فرد و شرکت دیگر اعمال کرد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/685028" target="_blank">📅 18:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685027">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EfnU3XRQpAK7sLO9a0BkvCIRwngtvyD0jEQBpLBIs-0Ez-pUKwy3oa8u7TZrLuSN8EAswJN6HViw6tcPq6gEs6eS1-KhW2hjFf0R3Kzd6Sudn13meBaLLhRdK_6Uz8YXIdHtDpjDiJHJ2Pt3zfaylhlGexsdraVowmzpQrxpzHukE4-0KVie5kznS-HwCs0EmRAfxF2Y0HUnsiXmOieMkPz1Wze-MLcnsuzUUX5AZuTbzQ5v40KlOFhGIHQgVWZVxen19HJgmEyjQB9o2w2CEIosSZt1vGhhfjuvngZ-urkwbqTyiZLeDXefVjEBxRZg1pVlAcFREvMewMP6LUMQ_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بحران هرمز به قلب بازارهای جهانی رسید
🔹
تداوم بحران هرمز می‌تواند موج تازه‌ای از تورم، افزایش نرخ بهره و فشار بر بازارهای مالی جهان ایجاد کرده است.
🔹
بازده اوراق بلندمدت دولت‌های آمریکا، انگلیس، فرانسه و ژاپن که طی سال‌های اخیر تحت تأثیر فشارهای تورمی روندی صعودی داشتند، از ابتدای ۲۰۲۶ و همزمان با جنگ ایران، فشار بیشتری را تجربه کرده‌اند.
🔹
در آمریکا، بازده اوراق ۳۰ساله حتی به بالاترین محدوده از سال ۲۰۰۷ رسید، سطحی که پس از اقدام خزانه‌داری آمریکا عقب‌نشینی کرد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/685027" target="_blank">📅 18:01 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685026">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
بسنت: هیچ‌کس از تحریم‌های آمریکا علیه ایران در امان نیست  وزیر خزانه‌داری آمریکا، درباره چین و ایران:
🔹
می‌خواهیم امروز به‌صراحت اعلام کنیم که هیچ‌کس خارج از دسترس تحریم‌های آمریکا نیست. هر فرد یا نهادی که معاملات را تسهیل کند و بخشی از شبکه‌ای باشد که نفت…</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/685026" target="_blank">📅 17:58 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685025">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76cc24ec18.mp4?token=c6fcKm6Nz_e2H9CbjLlftvGfnT2xxN8ttRB7PJMNXRGgGXJu4u_EwxBWP-tCZW-RUau63loN88eWd0EQnpT4AIZBENimTmci6CJBjNS7ACqKWBdDfcjXpSPkU9WViSSsFzrWV7eLLZPf6ug1CW0g3kp5uDGz5K4gPVwLtTe8GaLbbgypnmL3W9lEYCzvM3HgxJP44U445UbHRdjDhlZ861TOAsb8AKOPOd1wiByet8cPsQB2d6mCbozjO8rYKnES1sjnXdo8R6DCIRLukbkOdcjkDjbz8meSB-1jlZEOswuNWQWxwSo-Uv5iSA_LbE43Q5pIp8hgCPwI2VZ-Po2djA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76cc24ec18.mp4?token=c6fcKm6Nz_e2H9CbjLlftvGfnT2xxN8ttRB7PJMNXRGgGXJu4u_EwxBWP-tCZW-RUau63loN88eWd0EQnpT4AIZBENimTmci6CJBjNS7ACqKWBdDfcjXpSPkU9WViSSsFzrWV7eLLZPf6ug1CW0g3kp5uDGz5K4gPVwLtTe8GaLbbgypnmL3W9lEYCzvM3HgxJP44U445UbHRdjDhlZ861TOAsb8AKOPOd1wiByet8cPsQB2d6mCbozjO8rYKnES1sjnXdo8R6DCIRLukbkOdcjkDjbz8meSB-1jlZEOswuNWQWxwSo-Uv5iSA_LbE43Q5pIp8hgCPwI2VZ-Po2djA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این روش پارک کردن برای فضاهای باریک کاملاً مناسبه
🚗
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/685025" target="_blank">📅 17:57 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685024">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K948eQLpzac1xf3eW71oteKhCJrShUld3yJjORZm9iOyrITqVBoH6y_m9hR2w5LyvaKgmncEzuRjdAtfhLKPgoG7oH-thuz5-7zwZYZJLQ5hAUM2IIzr0AzX-krTzyuMSRhXby0ZzErLFcIn17Df8rhf6_EKICqmyqmY9NPLIgnOjeEEM7f3lj6qPOeCFum3iGn7T0zJCvOiqilWF3X1WJKC6Og3-ez3MzHyezvQ2SApQsA1-Yp_KXMQcShHQj7tRPolnzLvqAd3kJlFCa4AZv_zdLk4XP38Piil9B5oDTTw3zMjKfloJgOnrHFtae342stkl0lOl8y4B6pnC-TFOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعداد کارکنان نهادهای محتلف کشور
🔸
وزارت آموزش و پرورش با بیش از ۱ میلیون و ۱۹ هزار کارمند با فاصله از بیش‌ترین تعداد کارکنان برخوردار است و پس از آن، قوه قضائیه با ۸۸ هزار و وزارت نفت با ۸۳ هزار در رتبه‌های بعدی قرار دارند.
🔸
در سوی دیگر این آمار، دستگاه‌هایی مانند وزارت ورزش و جوانان، قوه مقننه و وزارت میراث فرهنگی و گردشگری هر کدام با کمتر از ۵ هزار نیرو، کوچک‌ترین بدنه پرسنلی را در میان نهادهای بررسی‌شده دارند.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/685024" target="_blank">📅 17:50 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685023">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h4_hqUW3FmbT_MK0jQDayWEfzH_SMcbr9adanKjR-f3AezoiBGqDdB7GmrHt6vxgXeJHVmGQFwaG0rV4n6Zcv6FOdNQS_7rnTQPLGIa8iBfctWceuyrPTYZxxNObX1-mJC-QWcNJcpdpqvgg5kuffDE1f8wQeXTZpLjrcIjGZNlTp5YD_kxHR4C0NqNPHkdWEkRsNPiTp66bl6vg8T8IlkDdhwfQMr2GkzvfGjKHe0MHNkp0Hdx2d0hhF91Wmx9ohe0YOYo-xUmNOKO_pJqzXgRccvlGApLJviYaBwCfrf436-oaJpSXODhzoGUiN24aJZk3U1Uiy-buqzBz5FFAtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دولینگو (معروفترین برنامه آموزش زبان) اعلام کرد آزمون‌های این برنامه از ۱ سپتامبر (۱۰ شهریور) برای تمام ایرانی‌ها متوقف خواهد شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/685023" target="_blank">📅 17:48 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685022">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمُندَمِج</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FuLtY6c0cBus4wlE0ytQBEoX--K8aZT85f-fga9Pz8mfQH5pJPjSvUsI6xrA112CsW14Hv2gplfGfBksZHozhvsofiauLPv5wnmkpdTHUk-yVhPmIJk_ijOCKpxGIAO_vJISNpuZM8MDeBgNm9WZBlzXn12cHIVe7l2GnhtHyBDCq1ZvFzhzbXoCa3BcEOFVguw8cqYFcK935vhiFdCaHkgwUAO3JFd-lUhfjG7Lf3SXf-xxOmBHKKw6nbt17PAC-y-KZfMrmY8uWfSM39E9fMMo3NtdLaedpFHCNRniFPkHFP_jD2ggXutqdwmkDFCRDRzcevF2gvXkrzdmG7Niuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توصیه‌ای از میرزا محمدعلی شاه آبادی رحمة‌الله‌علیه
امضای ذیل دعا از فرزند ایشان مرحوم آیت الله آقا نصرالله شاه آبادی
اللهمَّ صلِّ علی محمّدٍ و آلِ محمّدٍ
اللهم أدْفَعْ عَنَّا البَلاءَ المُبْرَمَ مِن
السَّماءِ إنَّكَ عَلى کُلِّ شَئٍ قَدِیرٌ
اللهمَّ صلِّ علی محمّدٍ و آلِ محمّدٍ</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/685022" target="_blank">📅 17:47 · 06 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
