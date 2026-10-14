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
<img src="https://cdn4.telesco.pe/file/injPJ0msUHQK2sQJ5CHZdNuy4qxVxr3UZPUw_sZXZdx-rRSCltrl4ZSegl0zLgutHRjM3eTn_xm6QlezEUqiujXkZFn3TnzBTKd3xsDTRNjYvDRT5iQqfY41gUKQfqOpvk3SNisFzLHBtGPAfq9dv4bgMERmW3NIOF_kBp0jo7hCZhbO6UFjT_t1KB7QMrax_AEk5e-EO3geUJkkLwWUMf7sBbdYZi8WB0_flLBRUxJmJHz4CjHpuOec1D54oPYKb_nYbFxJoepylMtumPBc6ZFO30EFz-M1krDSkTEtsa6PJ4U3z0uZq0jgz5sSLqJTuRHRm0Azyqd6yvOGff2HBA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 467K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتارتباط با ما:@ads_Persianaaهماهنگی و رزرو تبلیغات:@adspersianaaa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-22 16:41:30</div>
<hr>

<div class="tg-post" id="msg-31558">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kh5Otgxr3IhpJVPvqI7fK22WS74n6p8_wjDloFaX5FCCjYmBqumlz62S4WIlZOJfXTP_d3t4VzJcblVFUbmKkbGuDsRGFMSxlWNlG45THRbrF1Ernn52tLWWievkKLS169XpffHlDl31aCf2MEgvblzb84zKXonknX7IrHdVISXp_tCrWowcEePv5tntUTK-f50psRKT-npzG4HoC2SW33uhPzOavbLhb04ruvUDzf0h5WXuAHBnn4WGC2Q_RAzGRCfJ3OanuVb8BjCQ3ZuuoeFHMTbA7eHw4SXAOKhLWHCFS0oIn6cEDArWaAawUhF3_cdSnGYWBLOzukYM073XQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ کنعانی زادگان، ایری و بیفوما 3 غایب پرسپولیس در بازی فردا عصر مقابل خیبر خرم آباد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/persiana_Soccer/31558" target="_blank">📅 16:19 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31557">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JjrBJWiRwXJcNigbbIAYn7GWP-3I_rQyAL9IlcwJaulziNA_WBEShiZkp44OlvY33-KzyEpTORMNdcZTKYVAM5wgBwb2vWrOnXT3rQbAHf-gaczec70u8NGBeJX4YYV-JZDDmAN5Z9SOi9a1EnYRD_0xxObK9jzRwXKPXxPwInKRqtwOIa-neI0qwsUEOGFDBlPyQiDRM9l1CzFRNyTWZ60zw3kucg--rZ9kGqiILeoomFkjjsqQDbBfjXWRRk35RmafvUd_U5jGcsFUS8vAFRQIXApeEp0pP1tGp9fUm-hGOpgse5plD7z1rvFDdlMOlOrXjEKTK0NGAO2zGVtkzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
معوقه هفته هفتم لیگ؛ ترکیب پرسپولیس برای دیدار مقابل خیبرخرم‌آباد؛ ساعت 17:00 شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/31557" target="_blank">📅 16:06 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31556">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YwV_zY5IDgmIf7GcSb5jlR16iLqmNTiFQavvsXapCkAZG2xTmz43CFLIxtPCzk96gX7sJMCSEcedumrozwERpN41JKx0DjUScDlOmrG9lDxHC4hi-r_dUUhSz5ZTs5OY_HO_7M3MUFSH8Xw6TLloRob_Waydh8KyU4BPRSCoa3BeTrLUupX_GN7Ya36L_A4LYO_sqCvD7gQGbG7j0Zn9P9FJbhKkNBarF25w-UpMXy_9SofzkHLtvEz0yPnONE_nViGFJw1KLT77CmrSY-GLDCKhzHZ7nxxuzjx0lxu8egBjnsO7GaSTJkvF7HulsrGUkpCEuYu8x9Xnz55R8JcnUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب احتمالی پرسپولیس در بازی فردا با خیبر خرم آباد؛ تیوی بیفوما دچارسرماخوردگی شده و اگه به بازی نرسه به‌احتمال‌زیاد اورونوف جایگزین او در ترکیب‌اصلی‌سرخ‌هاخواهدشد. کنعانی زادگان و ایری نیز دیگر غایبان پرسپولیس در این بازی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/31556" target="_blank">📅 15:59 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31555">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LLbx33FXVXtHiWZxaT409qsPVN58o2UfghVFd2Ao1bhyofapzYta7z6DuxWU5VF2nl_ap3lcf7q30klrNo2LD-r9L2r4q-E9FKGPJ69P6hYYem_alNhUxc7LY_sVLwfnd25AgzLRKh-S01ghta4V4J0Q8C3FTnwhWwmpYGvDQGOC9P1jK9ht2-L3doJX2SA-9v92s4Jh2sLQtv1pZrn-EdrDfgCYuDFZ_erSanDApI32TK3g9evTXzpyPSAA1mHoqzX-A8OySBOrWk9pXtAZvSN8p6uIaXpjkpywbkdWJ5zbp7PiJJstH6KksvqAlvLD8bekGev5K3wTqPgIVRdehQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
گالاتاسرایم نتونست نوار پیروزی‌های بارسا فلیک رو پاره کنههه؛ آتش بازی ابی اناری ها در خاک ترکیه با برتری چهار بر یک مقابل یاران رافائل لیائو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/31555" target="_blank">📅 15:58 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31553">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j6BfdiSJIXy4iOdrUQMg25H3yxwV8nul_zmUSV4NTS4YMN0c7wkjxWquN76ONf3R0Auc4Ct6yyaGVbjdjc4iJAw3hyhJKYht8auFY7jPlrEpRLcTKlHBjb58vfiPLSatkGiV-ebh6Oui_XcUf-EyT-MPQtmImaS_Y4XQq0GaWkdy6lzlEmz3IdyVQ6foP8j7aHlCDX1WN5damtBwcZZKv1xxg8ge7hMmpwKPsv6lXqkN7RB5RklIdWZPh0V20-uhyJ392kKFfULYMcNtUU61dE6ffO43MpoDjho513U2mxxi1ZNtYNj-H8-Oj3GOgB8bSa2pVIS0aZkKSh7CGz52vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GHXjg9IqyKjJbWm7Y3dCesyxlnhSjQsIi8rZ80O4QQSss6FYpJCSAPgAVQbD5tU0xCrh15GCnm_oE9KaDuZmbugAJP3ghItLBjYPv4KFrj-Qke-3KnepHWcuir-ckiVhvQiJDjtoPNB_J0vrxcPUjaHqOh--5qX6i5Us51vkEq6kmteswScz41zb2HD8YEfJc1kMJS2qgE2XXul1CJYfFF6sL_XDmXJqLPCbcfvynZKKGVCyKaavwmcBcm1bnPKx6IcfLh5eI6fsBwdHzmUWKK10MeShbmN87uzA2Ca9SJc1d6llge1vzeBTmT_cmMixM34IIdLTGYkxT9rBRCnGGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
هانسی‌فلیک: یامال واقعا یه‌نابغه‌ست. بعضی وقتا یامال پاس‌هایی میده و بازیکن هارو تو موقعیت هایی میبینه که حتی منم قادر به دیدنشون نیستم و اون اینکارو حتی توی تمرینات هم انجام میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/persiana_Soccer/31553" target="_blank">📅 15:38 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31552">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔵
🇳🇴
رسانه‌تلگراف: قرارداد هالند با منچسترسیتی بندفسخ نداره حتی اگه این تیم بره دسته پایین تر باز هم بند فسخ ندارد مگر اینکه سران منچستر سیتی با فروش این بازیکن موافقت کنند. بین رئال و بارسا هر کدوم 200 میلیون‌یورو به سیتی پرداخت‌کنه تمومه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/persiana_Soccer/31552" target="_blank">📅 15:10 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31551">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIodroVAA3_wdq8qZYP4juvFAF-fIJs3wWKnG3hW9t_-Hg9sXgHYj0G7DNAj-GykNsZQRf0QUu4g1BVbNUKK1f3mQaVuL-YHeMvra2MDGg0x-EzWp13re4d2TxEKIXtMD_9J7ahWZJ_6ukqdU54rlg8da86ycTLKQbfdr5jP9m10mpjv6p7bPG7Ki7hyEprsuYLyMUan2TqsNrL5rDJrxatGVAq3-5FTiwyQWX3QP7gfKMg8gWxE4sGVFuerhwN_jngrZZx_joY9pFf4_XqMqgFWXQlKDUALk4Z16kT0tndCrF7Jd5854oq6nQKN0cQRRtgFIyrXMkYWrJnnz5_QxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ درصورتیکه سازمان نظام وظیفه پاسخ مثبت بدهد؛ علیرضا بیرانوند دروازه‌بان 34 ساله تیم ملی با عقد قراردادی تا پایان خدمت سربازی به تیم لیگ یکی نیرو زمینی تهران خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/persiana_Soccer/31551" target="_blank">📅 14:57 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31550">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bkg6I6YkdpjdRUYjjelJSjmspmtOlSTmk2eu62WQrnTnuNxgBg0wtuKu5WciZT3ih9C1k557GJ4x3-EtkJhvC73WJTf81cIqwJI46wIkO19cefQ9KYnnzLyPCjtyACnuY47aBVm5pkPvOggRgtNJCXb7_I1CkW5AacP8fKemjvCZR_aW2SXY3tTeaUzolexZHj3ifsbWuj-B16KHseSfxiW20IXgzVPqndnZENc7cokFM5N3tcvIPsbyO1aUefnqc9BNToPvWc2hoVKtsgt-UfZ1HVgXjPVNmzWEFwafEr7AtTBdsyPBB4jE2Ie__dmkA7a1LE6sncrTPspiju28GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟢
💰
#تکمیلی؛ بعداز موافقت مهدی گودرزی با درخواست سیدمهدی رحمتی برای پیوستن به گل گهر سیرجان؛ مدیریت این باشگاه 80 میلیارد تومان بابت رضایت نامه گودرزی به تیم خیبر خرم آباد پرداخت خواهد کرد و بزودی این انتقال رسمی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/persiana_Soccer/31550" target="_blank">📅 14:57 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31549">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNxLO1-iPiBek8Q3H7jgZwNdNVaAKO56TQLPBFUxtjRhqiJSVff7919VcSv73-4-5tDpOFPqGs7u7rGmWdoVMTgzA98uFEuGbG9Ep-2OlxYj0_J3kX7WU63vxSpRlXa0rUxnZhv0UH0uHix5rCbrp9TZONpKn8zAM4M1njkkf-YNBN0I8Mikt48cJtJK-TCttGC0DnItQIi2b-fu2Mjklad8TlM-JTb5dDR-AQvEk3mlQoeocEBS4CCS6gOGSNMjzFd7RImBYHQERL3SdvdQSV6yskeOUwNjNCvHA4DIE_QrNeTz-wHHLWc7phmbpQikwDuwrzpxw-a17zqnvQl6jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
هفته هفتم لیگ برتر ایران
🇮🇷
خیبر خرم آباد
🆚
پرسپولیس
🇮🇷
⏰
ساعت ۱۷:۰۰
🔴
انواع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۱۰۰٪ بونوس بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🛡
تا ۵ میلیون تومان بیمه شرط
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔺
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/persiana_Soccer/31549" target="_blank">📅 14:57 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31548">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇪🇸
🇪🇸
هانسی‌فلیک: یامال واقعا یه‌نابغه‌ست. بعضی وقتا یامال پاس‌هایی میده و بازیکن هارو تو موقعیت هایی میبینه که حتی منم قادر به دیدنشون نیستم و اون اینکارو حتی توی تمرینات هم انجام میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/persiana_Soccer/31548" target="_blank">📅 13:59 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31547">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YwZz-VUb7GbkPpLjcidexRUWltNRKApUq9eV3W9pIKpBfP2qNb9e7RxpG75d9DHkX72tcwWBr7Ly8Y6lW1KU33lUPvmUWiBc_uRQ8_vVHO3yPFigt94--d1i4mi3CXyooRevvm8bH8FCynpFlSuS7-BbA_teSurNJK1EtxD_5uUTjVopj-zPeF4ylFIkfvo6CsCS11gNNQ_PkJ2FPRage-mKx0KGCWp58I-UlopPL9ffyXw3k9YJn-C3lrDk25ThVG0LsKtPEEemm0g5QV22zuEp0qIPH3iop08eSHpl2ia2ZaAagAhjKbS7wcXpbHjsuLurbaWEilFzSiHdF-X1aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
گل‌های دو دیدار امشب بارسلونا
🆚
گالاتاسرای و اتلتیکومادرید
🆚
منچستریونایتد در هفته دوم UCL
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/31547" target="_blank">📅 13:45 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31546">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDdk6Y_viNBjJvLFSjYuhgal3Nbc0iFo1_hprFKdOqavYTIBDVa0aSMKB2R6J3EjUwFGpUbp6JIm0DW702w4Ql6BldYtQDO-1sRSeaRVnNTGqG2emrmKZxZSJtNbuhgfT4gk9Nzlde4b_kLhJM9szZTcjxVfQPykGUOyG_9BR7FnbBMwgZm7wqYo0NEoDhwQP5Ud8H92J1S_CfOOQuN23gbjbFWKVcevNAOX0o11YS5Z1KKi64JDWcDKHP5R_dp9-4nZw7y86_IvaAjc6nwGRHyHBCCLuMg_Y0PuYA91BT6vbaLCazy5u-IKdVLjtZy8UFynsdub1yMa5gyDmn3bfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
کریس‌رونالدو: اگه‌کسی‌مسی، پله یا مارادونا رو ترجیح می‌ده، این سلیقه شخصیشه. بهش احترام میذارم. اما این که بگید کریستیانو یک بازیکن کامل نیست، یک دروغه. من کامل‌ترین بازیکن تاریخم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/31546" target="_blank">📅 13:18 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31545">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JLMD2k-ybmz6BlqbVQIUJKp_gAD0UTyKCmUyqZ8gIaazZAfTUeCDLWPcLp2qguVfk-sVjOh17ggRIALHV9TIwG3SMIQbX1DyMFrfh5ntkmwx2menDcJyweo9dbeyPPnYPZbZRWO74tYuBzrYdEjVeX5KzMiYtlooGaP9IQGl8YWdFjaJ0Ouh2q1-ixX4_EHFn0iP8E7QBK2YmndgYmluBfCNfK3CNfhfSMcQoOhNOAEeBONA-_Uq6LIiCEvcaa8eI6ubjQL5d8Rvt2jFykHhGgPoSXPLUIfBZDJXY6q8PASuzodcf8cBE3lgvrWfgRNiq_McRrw0j2u_50sKJVTPSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛شهاب زاهدی رو هم‌تراکتور میخواد هم استقلال؛ طبق‌پیگیری‌های‌پرشیانا؛ باشگاه استقلال میخواد علاوه بر جذب یک مهاجم خارجی مهاجم 31 ساله سابق‌پرسپولیس روجانشین محمدرضا آزادی کنه. بختیاری زاده به مدیدیت گفته نیازی به آزادی ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/31545" target="_blank">📅 13:04 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31543">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cp4l0CrjVf2iA-2Az59aILhWTBQXrXQMxxg4Wd5OH463D1DqFoEU9WbeDNXVwfoLLgJdLxR9kUbMQlXCve2bhRotpoAivqUYZYIPm0_j0cM62Lr_rm9Mr4hfASHxpUn-2MpfzpdBOZGdVVcly3-iolDGY-yMuiBxHcDjBb0k6rk8IBsYMMCXp9VE_bMQXK2_HTkbk6xYo3WajyFIgJLgeVnHPiRnM0WEbCFgqbOm2-Uvlz7kgP8pDlKyciCTSkLisrHRzObBnMSmyqZCCmufEJeIqzJOOqJ9b28vNOg4Bs4-I7NDjoXcC2xlrdvgVqfPjAc1wwczt0JOXhcOZwukNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X_kjvKX_LFV4NoPy69N-jDjq_GQ6pCXf7knLsO2Iue4w-WBmd6TQM-9hMx2C5RZm0qSqDkayfXCZ2moCf9PMd3aw5_IyTGg1YZAvT1AZu2HZl0BAKCOFGvGGkeUwDXZ9ajV56PBVj3BWhmxu5og7L4-bgSZndsUYMr-VJxhg4sGRWjNWkEhQ9qPegztaKHhUt1e1njXYDwkh_-iyGijIjYKjAYK3DwZD7DNpDF6h-dUVZfyHD1tFs-5lIW9Z-jkBTNeuefQLTWpC7Q_4dy9BQWHW7LJdwofh2GBKqsVM3sA0Sqvx4Co-v-DXTn0oYdd4uHOAGf_hgsDku1wTY1PAhQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
👤
با گلزنی در بازی دیروز مقابل صنعت نفت؛ اوستون‌اورونوف ازبکستانی باچهارده گل‌زده در کنار گئورگی‌گولسیانی به‌بهترین گلزن خارجی پرسپولیس تبدیل شد. یه گل دیگه‌بزنه به تنهایی به بهترین گلزن خارجی تاریخ سرخپوشان تبدیل خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/31543" target="_blank">📅 12:31 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31542">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sduNwIsTNYBuVXUAaba4s3mzGF0bK5TsvIz7AKJMMnS62Czeh-Dcr5avdneMkGPrf8V7Zp_SfdT3YEFih1_i3pzutGbqayzKFTzyd1_VuKD56fAWKR-zZ3WIiVUrNJrTdfMl3U-mWDRavoE0NZWrS0CXEi09cVbswV0s4eq_WOgj0NAUVMrpgj-REva6EQxZay8mH3GPlByaa2TfwFXQdRpBCWjiuNg4o27PLVYI5Vf1qPVsOoed7C0kJk5QdOsDmHWxP76S1teIA17sPwEG7N3hlZgPyHrKUd0Dy7SZtJQnNjVTQWxexTJokR-hYU62mcXcqO5_eowYTY3_Gk3byw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
واکنش فلیک وقتی تیمش 8 گل به بارسلونا زد:
‼️
واکنس فلیک وقتی تیمش 4 گل به گالا میزنه:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/31542" target="_blank">📅 11:42 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31541">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52b689cf97.mp4?token=BoEYH8o3ZoXWItEBqvrDRRQLnb2MHBtkuNb9Nobt5MMFzWa_mZciNj2I8sS0DFT8gVwH0UBfsEvRgxecKv1WOXq3_gPtKQd53zPPvAszrJ7IZvuXy7AUMHfYXtFwgPpk4rS9m_agBdAj23QLv0YR0pOuSIT4ihkV5y3oMtvyW35iauzlmKhxsH9Sjn2zJdBMnL47adjhlwXzznhq5Y__fPK5P2iALBWklJ3LkZOxhlXZOZdBS_gBAppZKHo-aLuqkex6Lh-ptyTW9bbhc0Qe6u_7XPFZM_6nixb7Muxtxxs9_7n9ObKzjszDJVCX2E9bGFM5ycYJawEfu9JdI9gPPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52b689cf97.mp4?token=BoEYH8o3ZoXWItEBqvrDRRQLnb2MHBtkuNb9Nobt5MMFzWa_mZciNj2I8sS0DFT8gVwH0UBfsEvRgxecKv1WOXq3_gPtKQd53zPPvAszrJ7IZvuXy7AUMHfYXtFwgPpk4rS9m_agBdAj23QLv0YR0pOuSIT4ihkV5y3oMtvyW35iauzlmKhxsH9Sjn2zJdBMnL47adjhlwXzznhq5Y__fPK5P2iALBWklJ3LkZOxhlXZOZdBS_gBAppZKHo-aLuqkex6Lh-ptyTW9bbhc0Qe6u_7XPFZM_6nixb7Muxtxxs9_7n9ObKzjszDJVCX2E9bGFM5ycYJawEfu9JdI9gPPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌پرشیانا؛وکیل‌علیرضا بیرانوند که رابطه نزدیکی با علی‌تاجرنیا داره در تلاشه که قبل ازرفتن علیرضابیرانوند بخدمت سربازی تمام توافقات لازم رو برای پیوستن بیرو به جمع آبی‌ها انجام بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/31541" target="_blank">📅 11:03 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31540">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KiRWcn9xTqREAQcdxKEEVixOOwYcKXq70me6OcNBTIqH7R672jC82Qiq8uHlipCttigEybXzHvTOYXkmq9NFMzZNhn0vNR5CGUZWhKMzsF296i7MoumFDrFArr5XtartAuOduZpWPfLkoP5wORDP0rqa_VePksUtzPSI1h3PUjg7Jqkq9SAMywWx0UVX6VeYDOWpr-hZvzLBGTZSiSPdaSzeB6byhYhmHnAVEmpZq2qMOLNvFRpDljtoLBOM4V5vnAQShIF9vTsaWSVgMb7bpONyMO2eq6nyfBv7jSOCCuwxXtyIE-GjcoMx7_0ACq_PunA3zn9JbFWtz0GyyEXn9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد استثنایی‌بارسلونا درفصل‌جدید رقابت‌ها: 10 مسابقه، 10 پیروزی، 43 گل زده. شاگردان فلیک سوم آبان ماه به مصاف رئال مادرید خواهند رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/31540" target="_blank">📅 10:50 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31539">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETHaa2GVSu89goRugNh9U4yeAQdJdup5Kp53JhN-Onyi2wkIFqWsimaYMe6dax5Um3bv7WTpsKmJlnj05QY5QZ26NHKJghsCwqcbJsbxGb6OZwF6PX8At-k2R5P8iQ9vzT2XE56VfY9g2nHrYcLfIyLD5KCMaCyDhRpSfQhIRDLwoO1HPUb1ifngh9nvjxlSZ7-YKHPPmRSdvd9HF6yqJ5VNmlFM-gY-5pjYDpTNylrWTHEOLurTFKN8MYaRGClBjnsm08_JFqhFgTHVUWiPPu61GIIgw9XqD7zrMEJdYyiVkehQNiggLayc-cvV1aLnR6DfyG2yIYwAWQDxZtYtjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین تعداد گل زده دریک سال تقدیمی در تاریخ فوتبال؛ ۹۱ گل در یک سال؛ رکوردی که انگار برای شکسته نشدن درمستطیل سبز ثبت شده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/31539" target="_blank">📅 10:27 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31538">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLjm1irg_AZO3YKD-fyv0WTvI0XbJ-X2QAjX3eTaEUoUIn-sx9YuFjz1J9VSwcBkbGPreLDKVgs_JElHqEJ5_eBs504ymQ7cQcgbtUyH7JPDKjvKEtcUNYse1_zZdMthUPvHQZDWtT8WEFM3ZIkpzsGuAnC7HzMPYC-vbsANcbf3-rtgsi1RQT3x9iN7cLgyrqYSdLss1jAMEZHMz15mGjR5ceXE5coliKLehxFKUrHkmc70Cu2q_0UwrHGSDgoQlYRjN8CfstiqpAlxGkCMzd1835KzuP5xllBrMtzAqRTTQjzff-ak2iuuy4KSkMH9zXuWEagxvkaRpLSUj9ZCBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
نتایج اسفناک منچستریونایتدِ مایکل کریک در فصل جدید: 9 بازی و تنها 2 پیروزی؛ شیاطین سرخ نیاز به یک شوک از جنس آنتونیو کونته دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/31538" target="_blank">📅 09:42 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31537">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJXx4VALD2BWrg9NmR2DgZS4_G37rTDA_bDLfxdILtWkwJICiV-LnJ-hOpFKxhYS2LgYWvR0W9XeQjSuBO0FyfXkCPhzUE-m-FtTQnfhObbj4GsClIUQz_Sc14sqAirgeqRBBXjllzQgExyDS9saB2QU6S1_6Npza0n85CQua0fnUzR3bfUIsIn-uHGHyV51uVLClvd4pHG12o2jpXVxv0mcnEJcGHHIeyn0Eb2OpOXM6LBBA7Xq5vzedR23u8I4mLT3shFBIqrFNBOQihfZIHyeIZWtXRk5DeZR5lO2NyfUm7DFpt3wB8-sQexm9BhirAl73vzwu-CU0x7KH-cPPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
گالاتاسرایم نتونست نوار پیروزی‌های بارسا فلیک رو پاره کنههه؛ آتش بازی ابی اناری ها در خاک ترکیه با برتری چهار بر یک مقابل یاران رافائل لیائو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/31537" target="_blank">📅 09:31 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31536">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXzo5uDFR8kqU6wy1mKde3KOM-Ok2VxQD3-1GrHWNLwQSLV6lRPp6YavA1MgVqpwIPSVoJ7o6J8NflBi-Nv8r1fzFtWTYR2UNvEoG3nDjCJ8PQmFwm4IWdYTuNZOQuJIVneJ1PfgWkqg4BiNuFCoUYnzMkJ6AYL6tZf_PZU5KeaRil3bCFqUKhiiJ0PfZ2pviSmEn3GPsLcyWUP4LPTHz6E6Y7x7rsapBQfqdpJUX1hGuangM5hsb2I1ESyPR4sQZ5PWTbTfgAiVIDdZM_8zVrTSYdw-ELiFJN3a_388AIEJL5rcb722FF06fiG2LpmdSdls0oKuijjH4K_bLVbGaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌امروز
؛جدال‌معوقه‌پرسپولیسی‌ها برای صدرنشینی‌لیگ و بازگشت آقای‌خاص به شهر رم
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/31536" target="_blank">📅 08:04 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31535">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NuV5zBh-M8qVKrtXsBh00O3wBm399my8_UE9v-HNHNSKd93edSrblpW_82lFjFK8HlSE_NfVuuJPGYDW8_eiTaWoje2liquc85qmg-b3wVA4PZGEAT9bU3eBxwk_ecpQqFLBfMNnaHxT2LuVbLY3T6g8rGW52q9nK_n0xIYHu1BUkGvTQD01ZrHVavtX2jOo0bdZVsvshxbkkSSH4HaDxRW7z-k39dkgDyLLkLyyIVFnB2awspXkGXN8aexbYLndl6pTeHi0govSPeEbq3C52WOaJfViik279blAA1tYDFZJ6jAGJNRQ-Q1wdto1SHe_Swv_RJrl-pwgzcidFjyXlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌دیروز؛
از برد قاطعانه کاتالان‌ها در ترکیه تا توقف شاگردان کمپانی مقابل تیم نروژی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/31535" target="_blank">📅 07:59 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31534">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fshSOYsX8VS5xLJTqCzfHtXmAXPD8nMrHxwVs5DIINZxJ4F9l-YG1qF-9FTULM3K49cAzWrzlBnjTvdpZKTyLK-s5j9b1kya-7UvIoj-hOTxQn50BLSmySNA5tZjAyUS9xju47a9NvB7bS3lsxaCXy_QhdgR9LL_BExc0nLZ9IP33UQkfUJxgUVwCNBoHszNWjjiFpuyZbhix0Ev61b-lsrLhMp63FDcek-iGR3nmn0ukzXgp57j3zjjNrZEyhcYqEUijF9SrL8oAdZnx6BrMEBVGIh_wKOgKrc5XWlBS5DDLzRwzoGBbIilejOe8wXVIk-UbwlnUPCtc9_OFy6H4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
پنج مدعی اصلی دریافت جایزه توپ طلا؛ امباپه بالاتر از همه؛ لامین یامال درتعقیب ستاره فرانسوی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/31534" target="_blank">📅 02:02 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31533">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ot-2_i2wK4qd075cDtNBXU_aTknR334rItngV91AsJWrtBM7uwPAHviAlLa7XrfRjRsCnfANMxR1CUJ1HomD8VWyQwr9ltN_LFvkxW6MfYBRAbNsjKVGp4Z_eB02eYhtZoHohPeky7oXlzRCHP_Hp1MD1693bao2ypUutFWA4G48-lt_gu32b6vD_L46jgkUuCbBBzMSxqZfO1Q2zdKhtrdC3rpjdttzVNtaqHUnyw_jBnTobaBe79e6VtK-c7LmMniHBySau2kNpwiI11aE_Q0jstbDSR1VVmpM1omVh7x7Zt1aZwuND4xUBsKiwtgHY9Ohw2p9315wItomuNfS8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رده‌بندی لیگ نخبگان آسیا در پایان هفته دوم رقابت‌ها؛ الهلال دوبرصفر السد رو شکست داد؛ شباب الاهلی در شب درخشش سردار الاتحاد رو در عربستان شکست داد. آبی ها با پنجره بسته در رتبه دوم. شاگردان جوادنکونام دوازدهم‌جدول‌رده‌بندی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/31533" target="_blank">📅 02:02 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31532">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBussiness Account</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GX1_KnwBeFrJS0P281G5ykccQOTGBP9eLOYbXzPXY-sMrviZA1FtP2qLbP-GVmFpJTSm-nzl0bzSIGNHuvWjv-HsGqXnpIOD5JmoBjouOPwklzSybgcwW1lqs7pKCVklO59hs94QByBc58wCcVI4r-bONY7TVcGWwnGto-OKZCQ9nmcEPo6SvWK4-le6fgvy1BtGdtcjLjntvHkPPrP9_ZhJC9iimYurJMpTpb-oZAqZneUjCsw11G9Q2W-Br1ALdLXEcxZuwJzwxRqnPq64RV50Ac51HY2KwLxIdEcsXF2WffANv6huqa00uYzQBcUEkPOPkjJqblOBWECAXu-AKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
انقلابی در صنعت هوش مصنوعی
🔥
🔥
‼️
تاحالا شده دلت بخواد وارد بازار ترید بشی ولی علم کافیشو نداشته باشی ؟!
💵
چاره ی کار اینجاست!
یه هوش مصنوعی اومده که خودش بازارو تحلیل میکنه و اتومات برات ترید میکنه، اونم رایگان !
❌
دیگه وقت و پولتو صرف یادگیری علم ترید نکن، ترند دنیا الان هوش مصنوعیه ازش عقب بمونی باختی!
⚠️
بیا تو این کانال نتایج رو ببین خودت:
➡️
https://t.me/+gaXi_cMYHks5MDA0</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/31532" target="_blank">📅 02:02 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31531">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EVqdkZNVFOWe2jBZ66xhhugriOYm4c9M8CuEvdKYlOECydVJPnFL6EtzPqWErPgprj3aCnwApLtJO-3xPqCEypp-TkEL1WyormQPMer999C_lf0BHM4ZfK6umNKGhLXkyJICH0mOymDtJ9N8erVu8jI6WRZspwNIyA7bVMT4158HfA0bJe0PrTZu_M3itnoRxD2Q4TDIK8P7j2D_OE6cq7_chztkJt9EZUVU4Ta9z0dkATsfXL8yxXc6CmQXrZu2yz3EIQ9LDIJniWwlnx_2GbFZq5No62dPtau320hukqGhp7b9U-NRfMMZEYfsEmb2V6Pq3EPuR7HJQKAdkrbnYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدارهای امشب هفته دوم لیگ قهرمانان اروپا؛ پیروزی پرگل بارسا مقابل گالاتاسرای در خاک ترکیه و شکست تلخ شیاطین سرخ برابر اتلتیکو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/31531" target="_blank">📅 00:51 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31530">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">📊
نتایج دیدارهای امشب هفته دوم لیگ قهرمانان اروپا؛ پیروزی پرگل بارسا مقابل گالاتاسرای در خاک ترکیه و شکست تلخ شیاطین سرخ برابر اتلتیکو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/31530" target="_blank">📅 00:39 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31529">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RoKGoe9wNgsTYCavQUltQUNJJqQG7mvNjzn-WYBWHdx8aBS_wzX9CxjDTOsQKI9_Ki_sDSV514wQ8ELUJUsPXVb2lZ6MfOisCmhKdCr8eoRgRKE5bx0MzJLFn9TVLqYLdLmnffELd6CE9kpWtVTZ5W9-2Yj7UF_4YXo28GouwpBMBKEG-rJZeNrAwyN4qeU31sqEsUQk9vSscZYaTqKYTVjVKhO8nHmqgMzUuKjJL3vE3YEovHefDefBr5k4YAPHqrPBPxJ-KofZLAMeQAp0hg8-Xms0tESman3jKCnhgvIf67H8ursVg7Q_Z8BWKJqWb5g1M5VRGV2ljSyD18XiDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌نیمه‌اول‌مسابقات‌امشب‌لیگ قهرمانان اروپا؛ شکست یک نیمه ای یونایتد و بایرن و توقف بارسا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/31529" target="_blank">📅 00:29 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31528">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ECpNSFFCdEyyb0Qrc7qnnqSc7McKDDX0j6e3naBJ-YfdR-3SF5SSRrBs13ZofJCN34Z6vwlMS4-fEeBYBv3tTzkIj04tLNGHtJ01NhKzX7pmjLIUEgx0e2KNO0jNYPWOOM4xfHM5mjOAS_9TjU3Aip6oeHG-2XTiJHcX7qz5PDw-rBFo94CQZmnFTUykkDzxf-9v7-fgGXz9diGYHRhVq7GxUKDSbWCluu0zofJPzR2rU3_NWSy3286PGh3Dq8c5K32EOsP-nBo0HbzQMTl8zGeL_nsBnbRDwdFEtSb-kKDjd1MdMU8jaHqNMjKA4QOIvbV-p2gXrk3Ck8hrr4AdcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لیگ‌قهرمانان‌اروپا؛ شماتیک ترکیب دو تیم گالاتاسرای
🆚
بارسلونا؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/31528" target="_blank">📅 00:26 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31527">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSBs2A-6SSItOpGXvvNqRctPJxVNF5l5ilmWS44eDhlIY3kqj939zOU-kOp8pqDIB_EEEjhFuGXT25p58zerhNdZVKh4zrSLXNxIYnQ1c0f8pvgGlDCIqORmstZ1c4CaXzmdfRRw2_ppbSEnAH7KCHIQ43JWekOm2JBZWEkoMAOE5A-ZY8Z_VzHeWzEiNDTbd0rhpMQl0RaMv1PaLDbIRiShVX-I-0gLpEenGOa_TiIgObtwOPHTbm0cNXw1lw4LZTp3IFYbZibuVOnzZ01d0OLsVK2-t-Gkp9iINY8bW-kPC15MA-G9coOQMzaCV27R1kvRebCDCdunIQQPIJVQwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قول حمید مریخ ایجنت یاسر آسانی به مدیریت باشگاه استقلال: در نیم‌فصل یک ستاره خارجی دیگر در حد یاسر آسانی برای خط حمله خواهم آورد.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/31527" target="_blank">📅 00:01 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31526">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_Eik1GpWaPqVfzlHbaE8Dr4ewXtcvJ_Ky8PMY7Qz0oJTE9Gied-iJqRILbnc0bdo9UZL9xFItZjqBpj1FqcZL7E7jvyUgVZoXUrKWS-KqTpk5BqWlID3IvR_i24H0C6Dt07ht9Tunfp5yUJmg2tprorhURmnPiP6uicwR79CCAjNd-nUw7CaBdKHi8f5UdvQyKjPIVHcYZJKgjUhm1r0ySWH6kwovGK_LKPWlZHnvppddTjIlBmsLNa8tNSOTEWu1vdqsDr4LWyUGzyMsxePIa6ntBsbgIMtTpNRIxJhejo7O_N19iDnzvJsN6gm23-2UTCbH6DrK5tiJ8qw9rEUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
دبل‌ تماشایی‌ سردار آزمون مقابل تیم الاتحاد درخاک‌عربستان روی پاس هوشمندانه رضا غندی‌پور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/31526" target="_blank">📅 23:47 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31525">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3UsAJ_mHJ8A94_6Yn3V-e8qP4b4w7lGJj9w6aUIBM1T1wSRhTbb2LSX9eS4PVJX9O7EEqwhhf_tqSt7h9LAdtpbosZD2dsJXu106ULK89t8talorcnr5epjDKr2S4saCBCTCdPyj8ikHTFOTTjOmB5nXbvTYLyKoQOrBWMwlZcKqCAkn30MKSAq4ckeQWdMxq-WcYhE9EQ7VHidfWJcl9CcWW8D_h942_UPixUmTacHTKHSRE4-7nOfGS97c4n9A2561XgbPP53uTafDOE_Ynti6_1kMNGBE82GtwfFbvSWd8BudWgFTJQBsiijlbuk9NeSy0a8Yl7reQnJ0jjHwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لیگ‌قهرمانان‌اروپا؛ شماتیک ترکیب دو تیم گالاتاسرای
🆚
بارسلونا؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/31525" target="_blank">📅 23:26 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31524">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tO-6WOfWYLtyWlEJ-1lL9lmnIlxu-NPNKq7bPjKg2Awv8wsx7D0Jwtdq-L7SrpWT4XUur6sTBfTKXTCbtsxIlB4v2qP8SmamAismRLlH0v8KP3T891xbbsUpw9dV0M2gI6E-luHFtAunBW6ZKocM0Qd1cs3UfCIvDBX2S6B9NUtcWRDKBKDvmHhijkJAXUFkUHu6oBPX2iAIxwEX8gF7LZa1aIVYHYFwKydS4Q_vTfy6VX51onPH1D7MGe452ccwdkC6LAaoBcj4uHegrhDWcs5Jucxr-GDgLIZzxkAmwvomxw6v6caBoIPl1AxeGILnX4J_ML0Jgi_kvbR48Nnxyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب احتمالی پرسپولیس در بازی فردا با خیبر خرم آباد؛ تیوی بیفوما دچارسرماخوردگی شده و اگه به بازی نرسه به‌احتمال‌زیاد اورونوف جایگزین او در ترکیب‌اصلی‌سرخ‌هاخواهدشد. کنعانی زادگان و ایری نیز دیگر غایبان پرسپولیس در این بازی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/31524" target="_blank">📅 23:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31523">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e058158de7.mp4?token=hOMbLefKZ56DtHIf90_mxtXQ3Bh9Jlf91llPF1aWmsqzdZgVMgZIDNvLUsBaUKKAizVje-wuv4o9s4axfq__FgveKxS7dOjzMUN_BS7NaoLEcvSNbt0jnRnqlZ93aTVg0O4SURVsna0BW0TmojvLvJq1t8BATCl9Utg8_Wa7XZQFl1fS5sei1RiQQiqNACvJ6ELlLunaRTf8mbzxDsgaGBV2qL8A9AjJC45GNOsDUHHSAfpcAe3d3iZvZLQh6o5efA4XozpihT0gQONgmkyoqvAs2DYeeCVrNtGDj2XODpIL3SJf6WMW5VxO--qDy71c-Btm8MNZ0tIDvmaB5sVfXV26w0h-NdgyD5-Bh6jYzvIjQTvXZFqvft4LtmiFSlj6V8icrHyirw1C62VRs-APWS_F1Icej-62Wb7UH4x0zMESz_ZbciV4neBQoGbT6nD9SLPCF5E5YZ5WphQ89YB5ctnZ-wvT26Yn7lAHyHY8b3Wnd1mme4_TXTn1kpyf0GsyCXTLPNhAdY_QHWyRzlNT0LLbKCKIN53z7cso_YmHtpdqMTRYpuK3c2XQXfvEOlsMzFYpBUddlGtLBuWQSdBKCto-aKT92_PoEcq8QC2_TjRHuTj4G2fd7Ja1wOnxTudL7XrDq9s2NUU7IwGl-cJ_WerZpMLX-IMqw6rFqRXETFE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e058158de7.mp4?token=hOMbLefKZ56DtHIf90_mxtXQ3Bh9Jlf91llPF1aWmsqzdZgVMgZIDNvLUsBaUKKAizVje-wuv4o9s4axfq__FgveKxS7dOjzMUN_BS7NaoLEcvSNbt0jnRnqlZ93aTVg0O4SURVsna0BW0TmojvLvJq1t8BATCl9Utg8_Wa7XZQFl1fS5sei1RiQQiqNACvJ6ELlLunaRTf8mbzxDsgaGBV2qL8A9AjJC45GNOsDUHHSAfpcAe3d3iZvZLQh6o5efA4XozpihT0gQONgmkyoqvAs2DYeeCVrNtGDj2XODpIL3SJf6WMW5VxO--qDy71c-Btm8MNZ0tIDvmaB5sVfXV26w0h-NdgyD5-Bh6jYzvIjQTvXZFqvft4LtmiFSlj6V8icrHyirw1C62VRs-APWS_F1Icej-62Wb7UH4x0zMESz_ZbciV4neBQoGbT6nD9SLPCF5E5YZ5WphQ89YB5ctnZ-wvT26Yn7lAHyHY8b3Wnd1mme4_TXTn1kpyf0GsyCXTLPNhAdY_QHWyRzlNT0LLbKCKIN53z7cso_YmHtpdqMTRYpuK3c2XQXfvEOlsMzFYpBUddlGtLBuWQSdBKCto-aKT92_PoEcq8QC2_TjRHuTj4G2fd7Ja1wOnxTudL7XrDq9s2NUU7IwGl-cJ_WerZpMLX-IMqw6rFqRXETFE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شباهت‌برگ‌ریزون‌گل‌تماشایی یاسر آسانی در بازی امشب استقلال‌به‌الغرافه به‌سوپرگل‌خاطره انگیز آرین روبن در دوران حضورش در باشگاه بایرن مونیخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/31523" target="_blank">📅 22:42 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31522">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iStkKPFfzBgg3EOcB_9lnltuRf_AAKul0K6FdScq4QRT8Ajr6hQlHcx9P4d25tmmH81g1767LM_JpEIN8in2JdFdazJJwCbfgD22qFdNXetpoIC5iDUPRw6ur-KFr-MDjAUJpYtctLKzDpDmEZcX4IUkw11WPgVUdStCUl8f7ghGkxsNPA3bwV8io31TqJt__4N0xITJNyhGXLH4xK7iZr26JZGCyOGe5lv7RtTuy61ZxDIkpK2h-ePJVDhI5-hSyzfM_uUT5TDRtDkgM9sYFw3HwtlvjobVMfp7mWMDtkmiBMG-diqyXq_NHBamVCyn0-AoOj64qgrnTyBlluxF3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دانیال ایری مدافع جوان تیم پرسپولیس که چند هفته به دلیل مصدومیت دور از میادین بود در فاصله 24 ساعت تا دیدار باخیبرخرم‌آباد به تمرینات گروهی سرخپوشان بازگشت اما به احتمال بسیارزیاد در بازی فردا در ترکیب فیکس حضور نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/31522" target="_blank">📅 22:25 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31521">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d9d3f2c25.mp4?token=TCFNt7eSJavWS2F7HEl6HUmiQ0GVPr2J4KxtmJQAhyVonDWSTNRKuqR0NJcfCrxHgZMIX87mIutC3Omp-TOdsxej31_DRWlqnQf9H0C0AXjTkKwIJ1im9wgXJ7SkDlwYkdhzfFjL4m-m1oq8VPwD0xaEe9iopyyp883ADuFV4FSv6rIjojIW7QxnE2eN5RqUDHpsrujYNK4noEBxuPomkrZAbA_Nhw6RUSCAkR9KZGU7LjhL1Po08d0B0kR7lfAmZWX4BxN4qmPSPz-3e6mR3cXT0QUflEo5D4DYF-zze5N0xO3PhVHefB1F8IfJwtXj16xw9aFe2k48MkA5G6H4EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d9d3f2c25.mp4?token=TCFNt7eSJavWS2F7HEl6HUmiQ0GVPr2J4KxtmJQAhyVonDWSTNRKuqR0NJcfCrxHgZMIX87mIutC3Omp-TOdsxej31_DRWlqnQf9H0C0AXjTkKwIJ1im9wgXJ7SkDlwYkdhzfFjL4m-m1oq8VPwD0xaEe9iopyyp883ADuFV4FSv6rIjojIW7QxnE2eN5RqUDHpsrujYNK4noEBxuPomkrZAbA_Nhw6RUSCAkR9KZGU7LjhL1Po08d0B0kR7lfAmZWX4BxN4qmPSPz-3e6mR3cXT0QUflEo5D4DYF-zze5N0xO3PhVHefB1F8IfJwtXj16xw9aFe2k48MkA5G6H4EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
گلزنی‌سردارآزمون ستاره‌ایرانی شباب الاهلی دربازی امشب‌مقابل الاتحادعربستان در لیگ نخبگان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/31521" target="_blank">📅 22:10 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31520">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/559d04596c.mp4?token=detkJdCRhRETfFVh1hrbBOZ3vIfMLpabX_RuGLYAUJGsNooqQkKV4lBziarWixfgCp6U13V2iXdGuWVjAM4b8eRMwDzMzi3gf-8slqaVbfY9pX6Syx9grj4ODgAK7Rnc5MBJFUL_rAjyddoUiYHHsx1452IeNvt93EOz-x-ZU_c33lkJoKB71xb-whjT0bU1itlWTjjhLhVA9GUVJ2AHEO1Ptt7q8Sf3hLFBksXK3sbcUVXMHnyU5B9ZdCoIZ6-QCVjfs9RDKn9Ie4MduR9lQjgKxFuUPG2kSqEtnkx3-wXAfYEGz6MRiCccAa_guf9X7K1HjtRmrzWNoqGn9B-Mrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/559d04596c.mp4?token=detkJdCRhRETfFVh1hrbBOZ3vIfMLpabX_RuGLYAUJGsNooqQkKV4lBziarWixfgCp6U13V2iXdGuWVjAM4b8eRMwDzMzi3gf-8slqaVbfY9pX6Syx9grj4ODgAK7Rnc5MBJFUL_rAjyddoUiYHHsx1452IeNvt93EOz-x-ZU_c33lkJoKB71xb-whjT0bU1itlWTjjhLhVA9GUVJ2AHEO1Ptt7q8Sf3hLFBksXK3sbcUVXMHnyU5B9ZdCoIZ6-QCVjfs9RDKn9Ie4MduR9lQjgKxFuUPG2kSqEtnkx3-wXAfYEGz6MRiCccAa_guf9X7K1HjtRmrzWNoqGn9B-Mrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
نتایج و جدول لیگ نخبگان آسیا در پایان دیدارهای امشب؛ دو بازی مونده که السد فردا به مصاف الهلال میره و الاتحاد نیز از شباب الاهلی و یاران سردار و سعیدعزت‌میزبانی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/31520" target="_blank">📅 22:00 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31519">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJOisBl_8wzh1Lq2pbDnuDl-89NbHTPW_9Irirmh7Vv33aLTMAwhvA4S92rhbXJq4PKGGCJKSlJLCMKGCuKelw0lodw6AC-WpBi53cBRhvRiH8BtIYn_R3r5TsrI7RvUgZbs09RZjjoKHHmeKlgfbkUlfse93Ea97Mmaps4aC_S3xhvxLFYIA-PlPE2tzD2uvNk1Mcsd9_cW9ITsP8i_nrN0QbmYCVNTvct-sENEFc3ydMSGRJqo_bTwDbO5ygEiH0ZRErK9UCDzjqz7AAiYpygmOu5gAb-eX5CoJ9XoqknwXWjGTUEX4CAuDiY5AOfWWyhw1pLdm14W3pQME1tP3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
تایید شد؛ با اعلام کمیته انضباطی؛ خداداد عزیزی سرپرست‌تیم تراکتور به‌دلیل فحاشی به امید عالیشاه چهار ماه از همراهی پروشورها محروم شد. عالیشاه هم چهار مسابقه گل گهری‌ها محروم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/31519" target="_blank">📅 21:55 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31516">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b6Q_Q9fkpaXF1JALrsKNsRKMSLGmjdbrrhCtK2AeufWEhA0uQdihHwxvCCU_Q8FviO2LpQ9i0rANLgOrONn4VKJh0rlTRrZbLrw8kaPsV743VF1kBvv-TGeKU3hcBKAOqHD75W_-jhOg6cPKjk_0Fq2t1maqky6I0l8djm58eUfx2NO21ljM9ZQRT9COazelNjsMRl6ncWHHUK4hFKYdEGTH3Oho27szLpUx1FXdaQAQ6QwolD9gQp7y9oNjgYn-rFgVxglzl4gsFZzHzLJcn4oyv2TFv5rV1cerPx2ui0GQeHMh9ORCmoVaYpNNVXxy5wWmDsGDcrJZmlxKHTthLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eFvpzyBy3NRK2se3ObbE3TSJ1Jh05fPelp9RdOktibtyVehex10QD4EUdo-uyVTgNMoOFbHxUE0RsggflZqGEadJT26wSLbpHJoM_P6Yksehg1vqgoaLWtYdjzDwme8JyLgVtcgX4EXdQJC-HRYpsRMVy4FHOkqljq3JCqDPbQxD9qxP_HqRPgcSKaVDkRxOIkyfsYLIM_OJvTue1Ul7OPlfrmwTz83bVzOQDHRd4iuxGhJSKx8y8PYpUE1GMQimcmvmTd9X6Q7LwH_-xedu2JepVkYVwRy6Rsq8ywl3zqiYx_UCZfrOIgvb0R2yINezanBnp6W5ch1GRVyWtSITIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌دوم‌لیگ‌قهرمانان‌اروپا
؛ شماتیک ترکیب دو تیم گالاتاسرای
🆚
بارسلونا؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/31516" target="_blank">📅 21:36 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31514">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t6YsgX5r5-A2PJnY43lXRFurMDuTVPA3tb13DfGJYtrOHsCTwt6eJAHRO3sd-IR7YgHK8myRrAm8l4xPwxSTihjuvlnPugWttkYTAtkv7oG-mvcPIiKKOL1z3RUmeQ4taEvmLWMurI-9eQFtMVmPE0-83yETRGWCZHoNbRxT-tktSn2xGA4mwnhQqyWM8psw5txiBkkgedQcBwsbM1BuIGEEq5uGUCVpfV_029Ano1buuYae5pzQF_huPY3SvcaUJ5j3VAFlvmJAAS6XPEFCNWUTmwK5GIGkWjq3TV97G7CG_DYvX6-WFJ-gZY5TtSIcJgylpV4PAUFsx3kE2L3zsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DDGEN6km0mP_o0mKsTMJOp_saY2RE-8aTNV0rv1ewL7YXRiviozvNCVyVFmdsgM4EvPrLOBLjW0fvoWl2Ui7RU65V3XqVYYhsh-Xl2it6UqKNOmBUfobgAC1y5Rt3TG0u61Yl0vepsokX_2mz1bPQMZuCrvYwAkC3OYz_BsK6i3pYFkLtzrVu8aX2v-Skoq7aHBQSwhP-dIt1IH1sWK0qxwFE7TjXio8B-Qq1F40xlPlfQd2G6WKYUxVaFhR1W-qnjZRDnOu1Qccx3D6Kva1U4MR6WlzHBJN9Yn8NHKoeOv5I4BWd1jhOkYvmPajId0T5TNHumOxpgeKkZSW6HIeWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❌
کاکا اسطوره برزیلی باشگاه آث میلان: وقتی همسر سابقم گفت‌که‌میخواد از من جداشه و مجردی زندگی کنه من همه تلاشمو کردم که اون بمونه ولی دیگه لحظه ای فرا رسید که اون گفت: نمیخوام.
‼️
اون روز به درسی از زندگی رسیدم که میخوام به تمامی مردای‌جهان بگم: برای موندن…</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/31514" target="_blank">📅 21:22 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31513">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FV2_VDUBRwKad06vKd9VkSloE7GxbbYfiHfPnmDhPPwcbAT81ln0Ifw87kvlgTs8oAdl1VvHDSewcWd_sN4vBw8pw18zwZ6-A21UxWkc2VFukqUBOTT3NuUEq1vVH5ffZmSdUms3cmt-UDaORYX00rsEhgbni2bf_VJCNaLZOUKG0rKKhedR_0Cn59WPW5OwSBmFsX34ZMTYqvn38h4yJRsCXziE4M0ZKAUy8aT0Fzdc4BQEK_ZYSrpoy6ECWbiDqXtdVb6FGpo9g97skcV6-uWoVmv5l7avnd_II08G62CU4mSUmLp4Dtyj68k3bchKTXje4g_DKC261shajOvROw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🟢
مهدی رجب ‌زاده نیومده اولین شکست فصل پیروز قربانی رورقم‌زد؛ محمدخلیفه هرتوپی اومد رو خورد؛ درخشش فوق العاده یادگاری رستمی که پایه گذار هر دو گل فجرسپاسی به آلومینیوم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/31513" target="_blank">📅 21:00 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31512">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00694d1532.mp4?token=YvbiHmBI59qMD9BvbBA5FNLZs-ajWJoufV2BVSXiVk30kCqhyjxw3qq9tt0ql8Cys1n1OLDpn97Ed67KdDbXhNlR_8qgNYu4FfEY02xltgvdcj6PVZQgK2YUrnoiBZ9wsmz0VVXt_8QN6rbEhtcTp7SgZ_KwPy5xnfvsBg540SYDatdN_ID6eGg-8I1_r5GbxtVxJUqKnjzrvh38LU9enEoQLfxzwJGJ1EgwhrerGZjcgrDwY9GpO4N-ZwK8Tt6fDEpAqs8n1mSgHlfHL3t34o-jmDG21d7bdzYt8_1J5_X6Vlhdol29z-P6olDNFEX3fMyMmfAWliq22biqORYZToi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00694d1532.mp4?token=YvbiHmBI59qMD9BvbBA5FNLZs-ajWJoufV2BVSXiVk30kCqhyjxw3qq9tt0ql8Cys1n1OLDpn97Ed67KdDbXhNlR_8qgNYu4FfEY02xltgvdcj6PVZQgK2YUrnoiBZ9wsmz0VVXt_8QN6rbEhtcTp7SgZ_KwPy5xnfvsBg540SYDatdN_ID6eGg-8I1_r5GbxtVxJUqKnjzrvh38LU9enEoQLfxzwJGJ1EgwhrerGZjcgrDwY9GpO4N-ZwK8Tt6fDEpAqs8n1mSgHlfHL3t34o-jmDG21d7bdzYt8_1J5_X6Vlhdol29z-P6olDNFEX3fMyMmfAWliq22biqORYZToi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های‌امیرقلعه‌نویی‌علیه عادل:
خودشون برنامه‌ دارند و مجوز گرفتن‌ از اسرائیل مجوز گرفتن یا جمهوری اسلامی؟ اسپانسراتونم که مال جمهوری اسلامیه. تا جایی که تونستی تیم ملی رو زدی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/31512" target="_blank">📅 20:53 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31511">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T2YuIYxKccFnBAgqpwMitGhD9G1VCL5wk9fSdIGSACQd4GiXO-DLmaeKkKjeefs7vu7Oj3CgyIABan0cQdY4qCGAW0kGhHR3cGRfq9BuGcXFZN3DJPXvlbzub1h5h9lkSXCQOauDUwpTq-r16gAdV8CPLW69NLx0vxkXCCWIsnn8_Ohs6iUeuhf2tWKQHQ5NPB5dSdjQHdr6cHIzvKBr-aKHqaxaMHBesqG5XVsa1NbA2riFakPQUSvk29BwA4KGhUb58C2aIa5T83csGuMTTHukcXeknp2dnVZ-q4CE4DtAaODrCr4ENRJqd7z58RRriW2aSQ_1JFMiBT-4XY18rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ درصورتیکه سازمان نظام وظیفه پاسخ مثبت بدهد؛ علیرضا بیرانوند دروازه‌بان 34 ساله تیم ملی با عقد قراردادی تا پایان خدمت سربازی به تیم لیگ یکی نیرو زمینی تهران خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/31511" target="_blank">📅 20:43 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31510">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c7f86dd8d.mp4?token=rkh6OAIKklOK5GHir3ZfROIy-ldbVuxCuDn6PlR-A-shzliUpFfkd7w98MkbgnqKVG5D2cbKiAgx9_ZGkCjdUm1i2GDww-dnv6nnBpoaPckrxPHLg-XE1GgODql1ls1yC7x0SK6iiA38cFtspSpi6UoKN6FGTbSg8a7jXZPrhzT6iIS5SMF666LbYo4DAlrt7A9p_IJzoEYzNSu2TQvXii6UWGsXmqu-8o7P4MRH04YZO2tFjrrLl03_1lN9bLIn9cofws9LO2XYZJhXMqnTbACeb7Ej5mmlW8hU7OZQYuJQ_jsHe6g9BT6QCZf6mrvlTAKKeL7FcGROmbPyjNZy4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c7f86dd8d.mp4?token=rkh6OAIKklOK5GHir3ZfROIy-ldbVuxCuDn6PlR-A-shzliUpFfkd7w98MkbgnqKVG5D2cbKiAgx9_ZGkCjdUm1i2GDww-dnv6nnBpoaPckrxPHLg-XE1GgODql1ls1yC7x0SK6iiA38cFtspSpi6UoKN6FGTbSg8a7jXZPrhzT6iIS5SMF666LbYo4DAlrt7A9p_IJzoEYzNSu2TQvXii6UWGsXmqu-8o7P4MRH04YZO2tFjrrLl03_1lN9bLIn9cofws9LO2XYZJhXMqnTbACeb7Ej5mmlW8hU7OZQYuJQ_jsHe6g9BT6QCZf6mrvlTAKKeL7FcGROmbPyjNZy4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مجری‌شبکه‌رسمی‌باشگاه گالاتاسرای ترکیه هستند که گفته‌امشب گالا نوارپیروزی‌های این فصل بارسلوناِ هانسی فلیک رو پاره خواهد کرد و پیروز خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/31510" target="_blank">📅 20:18 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31509">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lu4JCmFWCW6mPtBmYk-9n8mkBaYfbIcV0LuXv38yAhA43ACEx4CCBXz2VAboltDrMOFBjDyBX713H6G3HYjZ13-eHB-O_sTqUdXFkjMXG_HIKETP-VSwpHhVuE8IQQbyEr-LiFqmWHsSIMFObB-vvQXi79Oh1Aq8sgNPmkN9WcijeXCxoNB1ZvDoRv4xZXkgSmMloFJyFP5gn-BViDXEoyRBroCuSfSnqdJgx3yP8qJOrr36pFv28BObBZJ7B92c3ob5RZQIuHzHDIBlUFX2qLTyiioVWIUFtHwjrDPKG3cPO16lD11cpDReAWMxAyg7WOGoyKh-3amlcJCoDnDG6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
از نگاه بیشتر بنگاه‌های شرط‌بندی؛ لامین یامال فوق‌ستاره‌اسپانیایی بارسلونا بالاتر از هری کین و لئو مسی بیشترین شانس گرفتن توپ طلا رو داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/31509" target="_blank">📅 19:56 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31508">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🟡
🟢
مهدی رجب ‌زاده نیومده اولین شکست فصل پیروز قربانی رورقم‌زد؛ محمدخلیفه هرتوپی اومد رو خورد؛ درخشش فوق العاده یادگاری رستمی که پایه گذار هر دو گل فجرسپاسی به آلومینیوم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/31508" target="_blank">📅 19:21 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31507">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">📊
جدول‌ آنلاین‌لیگ‌برتر درپایان دیدار معوقه دوتیم سپاهان
🆚
ذوب؛ فردا در صورت پیروزی پرسپولیس مقابل خیبر خرم‌آباد؛ سرخ‌ها صدرنشین خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/31507" target="_blank">📅 19:02 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31506">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uPvSHUb5nc5nAR6iT6n8k8OqHQw5pzDoSKmFZhYDMma0RG6C9JQG4NDYOm7XqaRwJWioROKbNvPx9KtoP5allg6Domu4udU1HnxNkrEYamVs24Qr0q5Snk0KgqhPuEGp7AWDHZuhxq3gjbe4w3qgiRfRC0VSKGH1wMFaTbl_iFLBMRGToWax-c8D2U9FiXdvyoiw6jxQv8STGu19kLSr4fdkjhAJ0LDcqbSyyHjm_Zr3OTx9HgsvZ2H1AfwrSyKbxDYhd3yKdI7IbQBfNxfNm1ELisL_MYm0DydqyA7MrZlzguw937EZx7uUF5T8BE7G7d_kEPnBcEILZgcl8U2lJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ یاسر آسانی با گلزنی به الغرافه به آمار ۱۱ گل زده در ۱۲ بازی لیگ نخبگان رسید. او حالا بالاتر ازفیرمینو ۱۰ گله و به تنهایی دررده‌سوم بهترین گلزنان‌لیگ‌نخبگان‌قرار داره. ریاض‌محرز با ۱۳ و سالم الدوساری با ۱۲ گل زده بالاتر از آسانی قرار دارند.
⚪️
…</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/31506" target="_blank">📅 18:43 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31505">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AgKkNxiDFGyfpgpffcDQnc9gr4FKi5vNbC5PgI74x7qm2mSM0Tm4fFpd7v_uqjHW3pDtXR0wDiGayCxGAdMHAWGt--etIo8PrtD2uQFKJYO_-vhQ_-1U6eoYMPvi-Yh6V46bsZCHPkotEZXbwti9Jk8XOg8yQ_cphhqOOJyLJqkxn-teI31f7hxTRVW3WfWge_sA4iZ-Vl7wLJBBhrILsZ3GxyCHJkT7wecBprEhIg3C0OT1O5ZBeIJ6LQMK3yGXKN6LDg-AJzddfy8_m6rBaPj6IiMNIyuOf_MbFsq-AMqEfy-BfZV6-p0uphhV1-nj40MxHSIMj8Vyo2MTsJ1Wzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
در شب برد دو بر یک سپاهان مقابل ذوب آهن در شهرآورد اصفهان؛ سیدحسین‌حسینی بازهم نتوانست برای طلایی‌پوشان‌ موفق به کلین‌شیت شود‌. سپاهانِ محرم نوید کیا شیرین با این پیروزی شانزده امتیازی شد و در رتبه چهارم جدول رده بندی قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/31505" target="_blank">📅 18:19 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31504">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🟢
🟡
گل‌اول‌ودوم سپاهان به ذوب آهن در نیمه اول دیدار امروز دوتیم‌توسط مهدی لطفی و کاوه رضایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/31504" target="_blank">📅 18:04 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31502">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PaKdnSQppHZntMlFlTn96duKxphbYbBFmTRN8IWQHSwObJlVGpz8iW44R51-ZelHLIWu1tL6OTCRhqPUHJpJvIr3mD5AH8CVlZwT20dv9fx8l-oUCmDb3amm0lvnLKuuLJ3Tn_NhURQ4XJfnrW9u9nriO6xWQ4rYVLCXY7sTt4VXJDQDuipT0HiURjlg9CCfi26GDMCDXb9S5lsKF4DapOLSQm8NgPkCR8WrxrDD8yMfVBxBNsCRm5WokTDGArVLrqwLo-FafWI4BmUevTARYmHQBQ-GbfChBkyQeVsJyNYauRNdOYdwjytEauNpfdtV5i_0iA7QVEeARmx3GcYUtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مجری‌شبکه‌رسمی‌باشگاه گالاتاسرای ترکیه هستند که گفته‌امشب گالا نوارپیروزی‌های این فصل بارسلوناِ هانسی فلیک رو پاره خواهد کرد و پیروز خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/31502" target="_blank">📅 17:47 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31501">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EoklyWFQ1DG9RcBLeqOwhYpTaKTAy-UnhxF8qbHA_OQgoq5afyFfZMSxtIFeIHNTY7tw_BRtI_z71A79ectVptVx-dXluCtU0CK-_tcUY-uLRoyj9UZ5C_PaPxkPJfeLa8uK0fEaDH3RZ5uT4JRmUvlx6BFOHWqsKaZtb4zRwFFzHpa-nkFlpHDn2XKkAF6SGRKZuW1KPZ6ZaDfCwojcaAx8R3fYPp6PE2GXtC9rEAP7bme09wyNk129RJ91K0SZbMVyO1EELr1cTawBDqCCbomgmOkK9c8wjr60-Bkmv0W6V5Y5BuAQkMO92o8W-D1NgNkdTxIwHZNWRI_Wj-6ysQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عملکرد استقلالِ سهراب بختیاری زاده مقابل سه‌تیم‌مطرح قطری: 3 مسابقه، 3 پیروزی، 7 گل زده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/31501" target="_blank">📅 17:27 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31500">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6451b4b3f5.mp4?token=vHZCiGhJkgia-eanthG3leyr6me1N1D9gmo9Dty-epqcurJG3XwQl4KPM_8aydqIjU90zq23ZhOAgbt17OVE3K-FwQyiTjChUBfqT3UbO0ilJnRMkWRo_vt4dnmBhGIect0HhSejLgspwiO5hmKyw_rLT0EHVsefOLlSouyYYqtY9LZXumYJZZ19FNHh2Bkyd6dMAWN8o3SBCdPtn3XLubq6vsQoFZeYZGa6zxn-mSZNtqoXT2rgwu1-GX6wr3pC4wEtgVXPxWL_PIz-VG5MbZhVEWa5gMAXq-APbBNeZbFckrhXTTzDSnZQTf8h9OS5c07pf5ufqVfAFgxt3KVxZoYc0lLnU1M_5hjzfTuSv-94R_9FB7BXluRpC3gQf3Sng7ogRQslPpIGYkyhS6Cp9aUG-JnQyrDIMxKuL8gbHJL9k0O5gBtbHGQh2NJMiuwbPOTNgWh5uYDl_t460srX6kxYeEsOZ2eOKDkRT0fM0j3AMZxIGzeRGq0cdvN93zlOYTEMe22U0phepo99BfRfqB_QodTio6473DoWLrMmPpLSvfed-8LkkvcAALdj1OJcvE05NcYxYrG7B4vXR-nTNjq7oLEcnuYHTs98rQeVUfnsMeUq2AB8Pk-xPGcj5KaZPDjuPwhxOEG3A_3r0yYTupKy74W8_M9nSfuIrBMayhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6451b4b3f5.mp4?token=vHZCiGhJkgia-eanthG3leyr6me1N1D9gmo9Dty-epqcurJG3XwQl4KPM_8aydqIjU90zq23ZhOAgbt17OVE3K-FwQyiTjChUBfqT3UbO0ilJnRMkWRo_vt4dnmBhGIect0HhSejLgspwiO5hmKyw_rLT0EHVsefOLlSouyYYqtY9LZXumYJZZ19FNHh2Bkyd6dMAWN8o3SBCdPtn3XLubq6vsQoFZeYZGa6zxn-mSZNtqoXT2rgwu1-GX6wr3pC4wEtgVXPxWL_PIz-VG5MbZhVEWa5gMAXq-APbBNeZbFckrhXTTzDSnZQTf8h9OS5c07pf5ufqVfAFgxt3KVxZoYc0lLnU1M_5hjzfTuSv-94R_9FB7BXluRpC3gQf3Sng7ogRQslPpIGYkyhS6Cp9aUG-JnQyrDIMxKuL8gbHJL9k0O5gBtbHGQh2NJMiuwbPOTNgWh5uYDl_t460srX6kxYeEsOZ2eOKDkRT0fM0j3AMZxIGzeRGq0cdvN93zlOYTEMe22U0phepo99BfRfqB_QodTio6473DoWLrMmPpLSvfed-8LkkvcAALdj1OJcvE05NcYxYrG7B4vXR-nTNjq7oLEcnuYHTs98rQeVUfnsMeUq2AB8Pk-xPGcj5KaZPDjuPwhxOEG3A_3r0yYTupKy74W8_M9nSfuIrBMayhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
عملکرد ستاره‌ایرانی جوهور دارالتعظیم؛ شهاب زاهدی از ابتدای فصل تاکنون در پنج بازی سوپر لیگ هفت گل و در دو حضور تعویضی در جام حذفی نیز سه گل زده تا با 10 گل بهترین گلزن این تیم باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/31500" target="_blank">📅 17:09 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31499">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/llY9xqAvZUeSSXWio7ALSXf4WRvQHCamiLrBf1-X7DcWtInWs1oawoX7eObeP6zv89O-re-fwXX3z4GkPwYeRixIuY8EMxDI-cYJE7XDLC64nktvOU7QIuWCUV8b5t-ti6AxSCksXVvJ1hBaWSw5oS3Pmb97niaGEYWIliNYbQN84HZ6d_ZcP0AOp6r_aMPK6v2EWjT_CG6v7a-_jTAW6CU45K2Time1Y0LjbJ8Q3l03rVZWpYwYxbWoXubjdLP_06tq2B5gAE4e0qlNmBQ_ix6QpBoy2HT0QPHUVl4JQa1rg9ibRydz1nMegcmkrmRSJ04OhZSEVV-WzYRG0bVFkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
شماتیک‌ترکیب‌بارسلونا دربازی سال 2022 با گالاتاسرای ترکیه در لیگ قهرمانان اروپا که آبی اناری ها موفق شدند اون مسابقه رو دو بر یک ببرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/31499" target="_blank">📅 17:09 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31498">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">بانک تحصیلات ،بانک  مشاوره اخذ مدارک دانشگاهی. واحدهای معتبر ایران. کارشناسی، کارشناسی ارشد، دکترا.‌ پزشکی عمومی،داروسازی،دندانپزشکی
پیراپزشکی. با استعلام.
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
Telegram :
👇
👇
👇
👇
@banketahsilat
⬇️
⬇️
⬇️
⬇️
⬇️
جهت ارتباط با ادمین
@tahsilat_azad
@tahsilat_azad</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/31498" target="_blank">📅 17:09 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31497">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OGOA3da1C0QnPmsdaLift5MULBs_izn4xEoMdH7g6pSl6NY6tXUD2bBY-taaCoEG938_MX6c0smt9WXR2q4ebdYAFD6f0FN4ZermehkW1c8_XqND3ymUfdWOzSgDVJ_4SS0vRP8_CAEYtSKmPhHCoJb_h5IpxUPa78kY_4pJvVcyNRii3wcGpYaw9dxsdqvABXU9qxDSMHsEkLiMKGmxQTRtf4hxlxGFELAWT5WqGnbdJY3Po3p_jqux4m54Xxg7w6ifKCVmRJgHyXRI5059RSy3kgPQlRnsiR5XO3_FQhYbYVych9ZJIAyOHtkrfAgA5LX0arlyDGPImn2v_YgYJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیدارفرداپرسپولیس
🆚
خیبر؛
ششمین تقابل دو تیم‌است. در ۵ دیدار قبلی خیبر سه برد و پرسپولیس دو پیروزی کسب‌کرده.تقابل‌های پرسپولیس و خیبر ۱۳ گل داشته که سهم پرسپولیس شش گل و خیبر هفت گل بثمر رسانده. اسماعیل بابایی، ایگور سرگیف، علی علیپور،اورونوف و عیسی‌مرادی گلزنان تقابل‌های این دو تیم بودند که در دیدار فردا هم حضور دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/31497" target="_blank">📅 16:50 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31496">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0e5fab635.mp4?token=YuBETCMW97nnD55mcup6gD-Rh8WFRm-Y22MIF34b51FgOmPjvPmDesF8BItl9w92rVWL5DSEPbmcSkqL9-Owxd3LQlmQF657JaghV_jaZ_OFRF2cQqq9bhIxShVngOPvBg4VXUP3MpwNweixcq-GXwdbeQ9XZNXM_O2ATlbbXLeDRkvWJTJXY7gvMZ1lkJDljKbUg24KLn6av2MIsY8FnTrzm2hHIAIXsCWOyRR7ZBEC_O-OMCxG8m-v2EFJQ2uzo-oBsHziMDSgec--SelqFE10Bls_3sNI-Ed-KUPCe9Coz1QTkaY3nbWhf6KULqkcbN6SiU3a0Bie_aiqE-nqPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0e5fab635.mp4?token=YuBETCMW97nnD55mcup6gD-Rh8WFRm-Y22MIF34b51FgOmPjvPmDesF8BItl9w92rVWL5DSEPbmcSkqL9-Owxd3LQlmQF657JaghV_jaZ_OFRF2cQqq9bhIxShVngOPvBg4VXUP3MpwNweixcq-GXwdbeQ9XZNXM_O2ATlbbXLeDRkvWJTJXY7gvMZ1lkJDljKbUg24KLn6av2MIsY8FnTrzm2hHIAIXsCWOyRR7ZBEC_O-OMCxG8m-v2EFJQ2uzo-oBsHziMDSgec--SelqFE10Bls_3sNI-Ed-KUPCe9Coz1QTkaY3nbWhf6KULqkcbN6SiU3a0Bie_aiqE-nqPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
معوقه هفته هفتم لیگ برتر؛ ترکیب سپاهان برای دیدار مقابل ذوب اهن؛ ساعت 16 از شبکه ورزش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/31496" target="_blank">📅 16:44 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31495">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OX4E3htsp-C2CtzRH9LSj_TUIb25RtlRv15fOtaXu9QsMMMCT4h3UuKbhRLPm-X9Za_atP3FVrqcRQEYOqjPiTS_s9ki-OqUN81g9tp6pqk70Z9e5xtS3IewB0FuoSIqVB5XC__d1ivwtc1hJRuNYSQzc_C-A1_fuzIIg2yl_ni7zDznl3AdnpPBfTXjHSoX5nhHOZDuFt_7kKAbh4GYkITnuJleAkT64PIOBfGNm3nJhk-i8PSYekHb-NflYZZx3CnE1oAV7YxNxZLe_UZApqHrmx3PBg7NxX1ngtwB3D13YRJIYeG8Tfd_iwMPej4bJJlxDYgI-lN6ZZaHNzcf8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدشد؛ یاسین جرجانی مدافع‌جوان فصل قبل آلومینیوم با قرار دادی سه ساله به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/31495" target="_blank">📅 15:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31494">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JeHcFqKpiPPPKb8r2RweudaEo0U3ZN0V11rvLp8ugn-AQaXj8QClYfR3H_iJYQ8y0LRkPQoDWYqjA7jKQK_gybJGujsdC8nIaQbls2-bIs3P1CMfkjE-rlcAnOFCGgyyG1Cnz2LmGUZbIfCbZFAdPXhC5aytFpXPtOj3nsUVPN3dE6odCoo3W4WYkOS6K_SAQCnYpBKv_l_BFZ9YzsH-V7lRxIgmw8HPjPYk7TCfmYBiVXJssAZL6ODGbJqCMSJErVqR2pvtygJTgCIsvuWBIqVuNCLPYx1GDy00QrD3Wo0zy7z2zjio51kp5o4DeWRFMOQXXJDbXmFJwjLDkJ-_iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
دانیال ایری و حسین کنعانی‌زادگان دو مدافع میانی پرسپولیس به دلیل مصدومیت دیدار روز چهار شنبه مقابل تیم خیبر خرم آباد رو نیز از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/31494" target="_blank">📅 15:30 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31493">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jsnf31wKTXqmkvPkAjAZmdSV6DQcGGHScmvE-ew4fwP0-AUnind70MRCRhDbUHj5-D6Y5wb-Z_4eYVFkLftOv_CUflu3IxA2NayeUfDMIwmvKaeP9tKkyVniNK9PONz7j_6eYwn3K1FBQ50uBwD4Epg75QpOM0NcyOxY5jh2q7AN9yMYgVZH9uCc_lxMFn97xJU3kI2gP_b26ZdqXbzTgiSPFxZmyo8XlFv-p3jRUTqmlZs4dQIiNeT5JVYqtXIayhwYmH1V1qFsYSqct5pzxEexkuXDPGrN4ZZJjroCmefK7HzyQNZBmNycUB6CZqEZrYGSHMDkWMvght9noQfQ0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ معوقه‌هفته‌هفتم رقابت‌های لیگ برتر که قراره امروز و فردا برگزار بشه. درصورت برد پرسپولیس در بازی فردا سرخ‌ها صدرنشین میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/31493" target="_blank">📅 15:16 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31492">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aMo3Kmd4HnJVos26CRSiLbudwgFDL4sY9DJTfo4ZEb8CZ6Z-F8H3PYr_1ECYeWcGsq0En5fJkBQNMl9rKUCSuQTc3ZMZswN8yhWVDN2cjXv4_ddnacWUCxYhiuUEm-LA5MAey3b9ceL1Djp4WvhHV5eW0SKj9kkZZFV2D8QoZBr8uZ3g7MferhybBxq869LE71y5AslK7CShu3zObUB-bx7OAVBEWVcZ_Sqy2sISOatzhSVQBb8eEurlir7tagKc099XVKzZhXUGskn5oq5h7h2rT5nP_AcQ0iTDmleQGYb0dBAcpNDFG2RvYwzYaj39LWKfwSWJPqN8pY3NUrN_bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پیش بینی جالب بازی‌های امشب هفته دوم لیگ قهرمانان اروپا؛ ببینیم‌چندتاش‌درست‌از آب در میاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/31492" target="_blank">📅 14:50 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31491">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Grue-19ycK-TnVy5CXWTNl7t4biaYV_RP8pYaUpssdzA_3_GBlhnl7KasbR5G6UqstPfGdMI7_qtEFO7gwPOuIyLV-0DqVJ7NrPAbI2RoZ8girjXwWWKvzIjSMkXacEEik90A6IVbyxm8dTixzDgdCwCr3dV01CU39WQAhIdsGAqS9DtO8LapxvoN2hgFdV9s0D8nn1TKYR8yOPUFoMK4pmYrg4BYO1kTfDCSLBFi2NJyhFHOk5wHwiSc-VyxTuZKfwcUSoQ2uj1-l6iGJols9bN47Y0h0bn3-kvUjrmtbMK2grwFdBKNb5evQdwBzQ5J3T6Y3WzHYyNZ8iLZG4k9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عادت بدش روترک‌نکرد! جواد نکونام سرمربی تراکتور: شرایط به‌گونه‌ای‌است که همه چیز به سود الشمال است. چالش امروز ما مقابل الشمال شرایط خیلی سختی است که برای ما به وجود آورده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/31491" target="_blank">📅 14:15 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31490">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSAb2hGp7sXsQ-LJre5aMJIJXN9hi59ILkJG0ndBZbg4llqW31cvNQp5DY1S2wx24SeA35h6AurpYzdUEDxMa19E8jLXDbSQQbFGT3zmQD4AiHcrGYgkKC7PXwSguFL8GXEiQWUoqgLWDPulGQGNXeNLh9H0I61UABAKHklrsMjhGNI9jaaMrSlHAL15jT7pD520QdGPE4pN9O9nlWXgbQtjs4qIk2lceyFkY8d7M7t1NqrKRTsI1N2NxoFv3BdY0SSNqGfbulTmYQuQ4q9icW9D8161WgiZn06fSP6-6KxfLQU_tRJMOS5Pw7rYp2t-FA6MHCwGgEy-ySXugw2JXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تغییر زمان چند دیدار هفته نهم و دهم؛ استقلال و گل گهر بجای یکشنبه روز دوشنبه بازی خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/31490" target="_blank">📅 13:50 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31489">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JbU5fuc2xU_tVHZ68nT4A-emfvcWteH9abU0eupM_xTni4jubvIvDHkbXToqqXPJ8hk6zX6XtbUVuiNZ4_vTBzKDd-SldhpDAl8WnJcQ_8t3IZTVB4CxGWbpBrbJU18Ds_93mR9ShE-C6wn7y_FdtNLEMzD-eIMSX20NPmhyFlWvBthIge4Dv2uwHkRqQTnkTYeVC98kT_WzV273Z4aKqFe0wyr9gmlf14HAvtz1cOmJfwzMBR_Ear5Kqtt-xbjo7f8ALp76aO7o3cVljf5NZVl0NBlVLX-6dTZxbozFjBYtr2zMr6TsvsJvEgscfqWXFSbj2wpy3EI-Iu19HCJt9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛سخنگوی‌نظام‌وظیفه: باتوجه به کسری‌ هایی که علیرضابیرانوندبخاطرمتاهلی و داشتن‌فرزند خورده سربازی او تیرماه سال آینده به پایان میرسد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/31489" target="_blank">📅 13:29 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31488">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kOxhzQ3366uoy0DST_shPXCQD3MLkcTt7OiJTmyoWoEIocMGLhaZat5Sf25aDvPks4UAg_qdZiLtjczOFDXxk569RqBoYaCCKhvdjCmX3HVXT3WrQ07nH19On_Vb2Sm7sxAUcgMZahD9Y8qxCFdH4YysF00oj0TYO9SduVRxhsKqoW3joiQmXRfzbA59tfdfcLi3CkWPOkg4GkLz3WAtW9y8TdTfobaObIbnB1cd_dMTcrRmUzPiW7gQsJpSjnrrqw-tfm9lvQD76hZhs4KDxaG0PqTSwZREnabn8waPY90dL5YqoBNT-jSoXS3bbw9dY5H3pQQ21Ok1SQSQx-hx0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
درهفته‌پنجم‌رقابت‌های‌بوندسلیگا؛ شاگردان نیکو کواچ در دورتموند درحالیکه تا دقیقه 85 دو بر صفر از وردربرمن جلو بود در عرض تنها هفت دقیقه دو گل دریافت کرد و 3 امتیاز شیرین پرید. زنبورها در چهار بازی اخیر خود به پیروزی رسیده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/31488" target="_blank">📅 12:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31487">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/thwRECsTJGi6XUPqN9mLt5AdeC-VGnv_Fl73pQnTm3biMVuGf1N8UAoxCTiMYjC2A-b-Cub-5znkDipMLbWQu9axtkGE0za0_GUO2tp-eEEot9Fb2x1iUUR3s8XF8AN7dHsIa8hlz-egNG-084YD4JM7Hk3sSj7KOMynFoZveS5s9N-zMWx_GiVvh2dRyKj2Mo6sdHr9NWo2P-8SmruWNgL2IFCH9lbAUuKNbig01CJb_0Qp47irsWlQPVK8YvApYXATFjDbIf71Rg4voJ81UvK9Z1yXE60DDG7Wcyy0grashRGA_mXzVtLeu4qIYEtvHEm3tbnOL2dwW8Z4LC0C1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اکثر مسابقات لیگ برتر مصر رو ایشون گزارش میکنه و برای هرمسابقه 5 هزار دلار دریافت میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/31487" target="_blank">📅 12:45 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31486">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mdefnk6r0Un9Fp38aYQJcdzUxqS2HGG5dF_rNJaxZGUf5HynJMii_E5ztdwiXwvhbG8oq3y1JWxsikAllLVtw_Al-rIlsXo-PpsSBH9SvDi5-Tah7FIddk-TVhrgFzrsToNNK5uXRBNRXlOgCG79z-jViRiWbTzjKWCFV5vnBy-7s4sMqW_FFXE-kvKJebVFgIZMeAX6TipPrOf1PRESiImy7B9XsYkBy54ADVtulyZ2I-1M_DV-v-tYAzT04yfRY1TkLuTiO9vkNHb2ljIcH1HjUxSpkaReawy3g5zxaovB1c9FWNS7we1Wl_1LbbVVtg-dFaS10y-sv5qJd44Hgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مسیرسفر گلگهر از سیرجان تا بحرین را مشاهده میکنید. پرواز از سیرجان به تهران، از تهران به نجف، از نجف به بغداد با اتوبوس، از بغداد به مسقط عمان، از عمان به منامه. به همین دلیل خواستار به تعویق افتادن دیدار با استقلال شدند که مخالفت شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/31486" target="_blank">📅 12:28 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31485">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71e001dfa4.mp4?token=nop_MHysKAOu8stozIMRpC87Dv8ZPj2EDO7CinPkLMdRAyG7TwzcDdhTFqtd9zhWFJNwigZC-44zjGQQKjhoMfdDzLq52YtkX3RzzmcelukbmVrqJ_57W2ya3_jeiIYlLyHXUoJOTRRUNsm_UIczWnvjKfSgah1BnawdVf16jdRKlKwFJLoaZps0GqGb-H4ylVetMwZyQk99k2ZSc-SyNpsh7RtKGejKpo8R2tTse_GnbsXCp5qHBRYTT7JiNWzp4_jlDT4Qx8SuacU05PAgMsvhJA33PNDas8kB3GQczli3mmkYlDBNuQpAkvRsEZTPfvKQsAVuxpvwynTfMXyXo0nVbpdPXB5UAQoGrY3-qR31xoaxyqMBvwsDrO7TVvX6_v2S67yWkxZdgLxV52Rbrlg9U16bbpiQFG9wAmSN-9HLhmkh5oCumDOX-Vq9QfmyV-7gx4y59dO9bDArIvfXuGQ6Z3mQLusvw7GAWeOtV_STl0ZAz5ifCkgNr451pWCqzqsYQqx8dmDUaKEubx7_hWjAsq_ou0EZ4GDbNlQPuWTQKd6qnpq4QKO4EPlQWgdDU8cPiuWYEc-_fCmJkXTz15-Q9md2AOwRcTBB7uI-Ch8M_nGTLlo5qArdwUv5cMjeRkw6movtNvGkbSnDeWr1kX-ePyMgR5GlxpNrptuC8m4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71e001dfa4.mp4?token=nop_MHysKAOu8stozIMRpC87Dv8ZPj2EDO7CinPkLMdRAyG7TwzcDdhTFqtd9zhWFJNwigZC-44zjGQQKjhoMfdDzLq52YtkX3RzzmcelukbmVrqJ_57W2ya3_jeiIYlLyHXUoJOTRRUNsm_UIczWnvjKfSgah1BnawdVf16jdRKlKwFJLoaZps0GqGb-H4ylVetMwZyQk99k2ZSc-SyNpsh7RtKGejKpo8R2tTse_GnbsXCp5qHBRYTT7JiNWzp4_jlDT4Qx8SuacU05PAgMsvhJA33PNDas8kB3GQczli3mmkYlDBNuQpAkvRsEZTPfvKQsAVuxpvwynTfMXyXo0nVbpdPXB5UAQoGrY3-qR31xoaxyqMBvwsDrO7TVvX6_v2S67yWkxZdgLxV52Rbrlg9U16bbpiQFG9wAmSN-9HLhmkh5oCumDOX-Vq9QfmyV-7gx4y59dO9bDArIvfXuGQ6Z3mQLusvw7GAWeOtV_STl0ZAz5ifCkgNr451pWCqzqsYQqx8dmDUaKEubx7_hWjAsq_ou0EZ4GDbNlQPuWTQKd6qnpq4QKO4EPlQWgdDU8cPiuWYEc-_fCmJkXTz15-Q9md2AOwRcTBB7uI-Ch8M_nGTLlo5qArdwUv5cMjeRkw6movtNvGkbSnDeWr1kX-ePyMgR5GlxpNrptuC8m4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیش بینی جالب بازی‌های امشب هفته دوم لیگ قهرمانان اروپا؛ ببینیم‌چندتاش‌درست‌از آب در میاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/31485" target="_blank">📅 12:26 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31484">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fpeTw2AV4pHpJx9gHX8ZH6NZlQKgQiKwmQ0-gk0PcpIhDfSS2zG5AvzjyT60QELIQZp1u1sAsGf9kcaNSBQIQgJ41axRwcIKWGEzHBDU_4kEpvHrITn9QBk5hn6hmcKURZ7CYICDsnTJ-1ohgYuqWzTngb54FxU-ATJSJzo3piB6kN1YJvich2jhpllJ0QAKONQ-7eDpqGrQagMJL1m4eNF6ooBEbuqzCSmOab9TAwStm9Cfz7ki9JpXdJt2Jp4wxW45qFg6cYzIk-zYw8O6Ezp5JEA_upK4VXiJ2vMvcNi_WrIUMdYdYh1z4KhPSG0kE1uzcFAvUzzZbNB2q5GJfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
با اعلام رومانو؛ دنی کارواخال مدافع راست رئال مادرید با قراردادی یک ساله به ختافه پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/31484" target="_blank">📅 11:56 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31483">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EIpH7ZNxg_BewHZPgVgTdkTPDsuKZg3X6FYzx_qy6wJ1AyvCG-ufGRndoL0Tv_D_PEulCTYBZTBxtaMdig_zEWT_CCOmZtc7rtj_rLrG6w4-76HhZdp6KmzFmfv1_siFT9ugd-8yFdRHc6-ON9L7S0ROxQQDWlzYNMRtdohK11YFgHCQjkb4WIvPiXZ54UNU54E-pOfXHnXi5x6ejJM5DVMjNKcJT8FnN2HUFg4TKJtk4pAG1-fgABZKnY3844o8iqfhiecI6IXGceG7UHc6LGtOhT_u9GFs3PO3qdu_eF-93DNNQ-vXOmooEiACDEdrZdynglNH8N4PxYHvZlx6gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حمایت‌تمام‌قد کریس‌رونالدو از کشور عربستان در جنگ با حوثی‌های یمن: جنگ هم شود از اینجا نمیرم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/31483" target="_blank">📅 11:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31482">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bie_TvZvGgGhQYB9ReI1WiA-Jbpto2QFcXziwqLB9xhRkBKdmO8RA0j6_YeJpzXUBkV2Ilc1V2ODprgNsaYJnNFF79Ouk9K8dEUgymuwTIdkGizTIvxnTf3Katf12R1uWuC2nMe2Ulj8YGqIa77ldODGNaPcJNchLBTZpdyzi7_pXkJrRW0cSoDYWJTbsnxKhQ6llCUA_wkVc-R3_qps1IgDfFsKKUrpQ2J9h79exKeQj8VVcB3374jqdR0xa7cCdNfpvLIKN838rDixSXR1VuLno_Tvg_8fJDk4kbLRZamH6yuYso76Rxp5tfLXJJxLDK0XLPMvcdI7xAS0ajTKZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بوسه کریس‌رونالدو روشمشیر و درخت نخل نماد عربستان سعودی و ناراحتیش از جنگ تو عربستان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/31482" target="_blank">📅 10:52 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31481">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sm1JOrede-Qn7nKI3jUTNqnmUMFrybLbt-WtGRthuJeAazwkzoRbsSKZxx2SF1miFizRYWNO5HXdZDdSiwNfg5JCuGVZ_cBh_bg_xdLojNr7K4nzYNPGA8sxYTZr_GJTHQt38VX50PrCNVqNncZUPslOTB3R4K8OcaItW8KFDizVxl3DxTQTYYn_MkT8vQxtpsWQpjXZyYuLOD5G2cgsQDU6ZNaMLTj-liz6JjMI6oMkDe3Rsp1fcCgdvI23E_0jt0BdYPBrbrPY5O13g4dVxpo4kIoUdL2YcyMGZmYRtqXlkXZoq7Dvo5euXTlhnBWWgMGyK9VwZ6KlwZrub11etg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
برنامه‌مسابقات‌این هفته رقابت‌های لیگ قهرمانان اروپا که قراره فرداشب و پس فرداشب برگزار بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/31481" target="_blank">📅 10:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31480">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vjug4gvNcAgY49r2J2f30IxFehTC66RRIQTMfRUTCsU_M4xA74rptWmjPmmtB-kA8X080oJdSUbFeToaSSEXyBVWBfqVsM5fvTue-G-5Ei0haxYB9r0jjcctCtvqqccgk_CQv7e4hHEO1gNlnc-aD2w6I6G5fxdaybLWaWPfaS3Syx-lZUCyJjwldt9YyGCva0PQLXcO_GUxvqzgQXphuFr1y7fcQSNIQ287pIy9ZCqgaCqmI-Z1JIH80WgZ9lXEa5y0FHVVpIoOsvrabJjmc4YKSMaxJMuL19sjavIgMh70d53c0lXLuq7GVUsM01rKNn0NObqSalTXwHEwiMDrPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
👤
سعید الهویی دستیار و همه‌کاره کادر فنی امیرقلعه‌نویی رسما گفت که مهدی قایدی بخاطر اون مصاحبه‌اش باامیرحسین قیاسی خط‌خورده است!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/31480" target="_blank">📅 10:30 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31479">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JdQP6F23VVsoGaEtoYmeMXyofZHTgQ5HZmZT-ywArg6eqkHkJzVsJ74opMNisbDr_hRGYBDpPXt4LqBNV06kTGScn6bns_djOTWLLK8HaOgxc7r6mWwffohHLR4b7ZwuP9031BW7kC-49yiLtUrLsEa824FYAZ-cpgymgy-CF4VCwIU4r_omUKQQNfoQ9mqcJX52SWsZ83MCO7Ja0Z1W9WZNqPN6n2tFAGMHH_gNthoSV-tsLsaRKUDN1GhVEtY19f0adtMC56wNE2BTcnF8pP_VtvoxB8kh676rmfZj5xgjMm5TBhpzRdOqquY7R0d_2s3lb6Zl_iUHSleyMAvJQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه دیدارهای هفته نهم و دهم رقابت های لیگ برتر که قراره از شنبه 25 مهرماه استارت بخوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/31479" target="_blank">📅 10:30 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31477">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b74c2dae8.mp4?token=rVTZLMWJNZiDGEPSmM_nnaNzdD2D-sH5uv01eUI_yqC19rd1fnKXiKWd2MzPLadtUtU8i_pNUYFJ1Oz_MGm331bv7T4fO_LuHRc2YmckPMXDtGY_1NV__kNCRw4B8F0fTEXyj6G_KPtNsRlnR7HN5Wy8eaABAO1X8wuSi2J9EEFLrrin1vTGT4G_uR2IYyEvP3kumm_ECxxLv0Yc4lZntUtLNuLqkpkFVeBJ2DJxnvVmlXtP6dSva5aFj9GKqtQ2iSAnLzUblhhd6okly0C7rkSpJVTyTLn890AQsihfsYmo6obGerbGvsmq1t_jug0nZ9mmHVf67zxjE3gm4SneZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b74c2dae8.mp4?token=rVTZLMWJNZiDGEPSmM_nnaNzdD2D-sH5uv01eUI_yqC19rd1fnKXiKWd2MzPLadtUtU8i_pNUYFJ1Oz_MGm331bv7T4fO_LuHRc2YmckPMXDtGY_1NV__kNCRw4B8F0fTEXyj6G_KPtNsRlnR7HN5Wy8eaABAO1X8wuSi2J9EEFLrrin1vTGT4G_uR2IYyEvP3kumm_ECxxLv0Yc4lZntUtLNuLqkpkFVeBJ2DJxnvVmlXtP6dSva5aFj9GKqtQ2iSAnLzUblhhd6okly0C7rkSpJVTyTLn890AQsihfsYmo6obGerbGvsmq1t_jug0nZ9mmHVf67zxjE3gm4SneZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دستور محمدرضا زنوزی مالک تراکتور به حجت کریمی: قرارداد علیرضا بیرانوند روفسخ کن. او دیگر به هیچ عنوان جایگاهی در تراکتور نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/31477" target="_blank">📅 09:53 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31476">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b7c8f6c96.mp4?token=Q_TJo3vvNO8RYG0GmVZTQ9M8i2jNeogHNEPt-lJM-KntkLA9Cyx0cQoR3nzppQw3t8qGFDwAGxNtefQ3biPvxDzwT4H8o4xec2GJXbaDLYI8u3VJA2oefWzH8p_xAT9Tb60OXKIGkokMNR7xsTFdSd69dWNQTZ7q6vpIK0yQf81CCfPQgRPhwbUeOGuQPpme137WU39BfR4SeKPCHBB91Ql5Pz3kvwhFCt0etrupLGxpow6Pcr3DvUTQ-KgfT4xNHdyuWOduC6A13yeRYuBG0lgc7YFZFECpOFcHCHWqQ9e_YfuV-BS7O3C49HIaK74bWg93r9S1q6ckicAAt49LTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7c8f6c96.mp4?token=Q_TJo3vvNO8RYG0GmVZTQ9M8i2jNeogHNEPt-lJM-KntkLA9Cyx0cQoR3nzppQw3t8qGFDwAGxNtefQ3biPvxDzwT4H8o4xec2GJXbaDLYI8u3VJA2oefWzH8p_xAT9Tb60OXKIGkokMNR7xsTFdSd69dWNQTZ7q6vpIK0yQf81CCfPQgRPhwbUeOGuQPpme137WU39BfR4SeKPCHBB91Ql5Pz3kvwhFCt0etrupLGxpow6Pcr3DvUTQ-KgfT4xNHdyuWOduC6A13yeRYuBG0lgc7YFZFECpOFcHCHWqQ9e_YfuV-BS7O3C49HIaK74bWg93r9S1q6ckicAAt49LTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
واکنش حامد لک به صحبت‌های بیرانوند علیه علی دایی: طوری می‌گوید در نوجوانی کارگری کرده که انگارهمه‌فوتبالیست‌های‌ایران در خانواده میلیاردر متولد شده‌اند. ببند دهنت رو بابا. حرف نزن تو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/31476" target="_blank">📅 09:40 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31475">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e5884a83c.mp4?token=hqm8Z72foVRybl4ucHFF93S6_da92oY-MScxQ3qX_OEDRBPiJylbdmc7s4Kaii7OLZYk9najlMsROHfnE7n02OKX8MW8MLYrOOSxNGA9LVsFjVxCDUWfBocwS7hj2LrwOmoxZfRKQI1BV2ju6Rgnw1N5jKRVQVEyHKCTyc75Do8C2bsrcpv5NzEE_K_6EUNnLn9s6CEj2PCh7-T96p7klxrDlnIX5-i64EIgxpGlXo9ebDI4Gr6i7bZjAFAjmzPFPAkgjGW0Shi7OVnc936Xcce_U6a27l2WwIbTb5jKyqiWpo5BqrXCuRS6cmcDLh4XW8-ovG8xX87UmergRsufkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e5884a83c.mp4?token=hqm8Z72foVRybl4ucHFF93S6_da92oY-MScxQ3qX_OEDRBPiJylbdmc7s4Kaii7OLZYk9najlMsROHfnE7n02OKX8MW8MLYrOOSxNGA9LVsFjVxCDUWfBocwS7hj2LrwOmoxZfRKQI1BV2ju6Rgnw1N5jKRVQVEyHKCTyc75Do8C2bsrcpv5NzEE_K_6EUNnLn9s6CEj2PCh7-T96p7klxrDlnIX5-i64EIgxpGlXo9ebDI4Gr6i7bZjAFAjmzPFPAkgjGW0Shi7OVnc936Xcce_U6a27l2WwIbTb5jKyqiWpo5BqrXCuRS6cmcDLh4XW8-ovG8xX87UmergRsufkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
گل‌دیدنی‌کریس‌رونالدو در بازی شب گذشته النصر مقابل نفتچی از زاویه‌ای متفاوت؛ CR7 بدون نگاه به دروازه حریف توپ رو وارد دروازه کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/31475" target="_blank">📅 09:27 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31474">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39e71f827d.mp4?token=Ib8UKInIw_Z_-RAkkKr7c2gn1_x44JeAeK4leF95m4XrQRzgHBjmpaFthMnTQJg698RM_IoVlCOhbEZivBOfma1D9Pw9J_cpKCqiDEdlZgcfxDDq7ryrugss8JuHtOxpBTbp7u5F6HR0rHDvSneV-GDXP3YdFDQTayB0aDwDIKczGspaSu4Tb4UhyIXsS4dUURAfO00T0_jtt2d0Ulw83IVasOuV_3hSyekAOyLGfoNds3VKTtOt27xeAgCLONwXF9l2gi0bbmQ_19U5-z_XZF46pJIT1JPr0rDahMHEywN-uBPQhiE-nClggY1prkYGL-_rwo9xxs8y-9Qzp6gFkg2yWN1M_LcjEq5D8Xt9duXETugKiDoAOPPHIAFPnzMQBnTFU6mJxMr95yQrFBqum8VCU9VVur60gQqh3mtx16_xWmKz3pkmNrTpuOBflMqmwVmnUScA9HuVgEqg9keEdZZxalbOtw2hWuVi3nT5his-Ha4o4XbDgwFfxq-hHDzAnw9f_iSjm7ZL1vBcd34PGCdlJvEvlgGLQRJdgZPE7M-K_zZJIGrSRyKY_4lxRD6lmn8StDkhSTe0i2HQAtoGi54_0kgukKBzpAU8wAiaH5tb89cUuiEKfJHevSELcgk9OZHwmPnbTqD_z1Jp3KGw0Og065paiBL5mPAhq2suObk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39e71f827d.mp4?token=Ib8UKInIw_Z_-RAkkKr7c2gn1_x44JeAeK4leF95m4XrQRzgHBjmpaFthMnTQJg698RM_IoVlCOhbEZivBOfma1D9Pw9J_cpKCqiDEdlZgcfxDDq7ryrugss8JuHtOxpBTbp7u5F6HR0rHDvSneV-GDXP3YdFDQTayB0aDwDIKczGspaSu4Tb4UhyIXsS4dUURAfO00T0_jtt2d0Ulw83IVasOuV_3hSyekAOyLGfoNds3VKTtOt27xeAgCLONwXF9l2gi0bbmQ_19U5-z_XZF46pJIT1JPr0rDahMHEywN-uBPQhiE-nClggY1prkYGL-_rwo9xxs8y-9Qzp6gFkg2yWN1M_LcjEq5D8Xt9duXETugKiDoAOPPHIAFPnzMQBnTFU6mJxMr95yQrFBqum8VCU9VVur60gQqh3mtx16_xWmKz3pkmNrTpuOBflMqmwVmnUScA9HuVgEqg9keEdZZxalbOtw2hWuVi3nT5his-Ha4o4XbDgwFfxq-hHDzAnw9f_iSjm7ZL1vBcd34PGCdlJvEvlgGLQRJdgZPE7M-K_zZJIGrSRyKY_4lxRD6lmn8StDkhSTe0i2HQAtoGi54_0kgukKBzpAU8wAiaH5tb89cUuiEKfJHevSELcgk9OZHwmPnbTqD_z1Jp3KGw0Og065paiBL5mPAhq2suObk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔵
👤
با اعلام مدیر رسانه‌ای باشگاه استقلال؛ مصدومیت یاسرآسانی‌جدی‌نیست و او به دیدار هفته آینده با گلگهر سیرجان در هفته نهم لیگ برتر میرسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/31474" target="_blank">📅 02:06 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31472">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WtfA27tj03F-rZjqsfAqztF3HNzaowWdQ0vT15sE6ZMo-iN4VyOWdgoTnXavDppTGxJmjMeaVtMl_OI6gKKK9FRuGpoFND2pW0rGOPu-7Wy-SGGGgQCQD_h0Dy1yI7M0MIloAMw2tU6z-t7eXYQr6XFPYBciKpuMKy2N7cSjH_Gs3dbTRPii-KaPUTndj9hR6OgJdRlKXRrQQxeDfxtNdAZXmNFpWZ1qaOjWGrpFHJLNt2_p-PAfRPwRQJS1TwOLGaomQ8DAM3h-NswKdLPyMmo3b5uCgXQ21_RueSDO_IfULLX_k0FAfnVJQgZ990meCmMdfbpIiqHO_ul6c2pq8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لیگ نخبگان آسیا؛ دومین پیروزی پیاپی شاگردان بختیای زاده در شب درخشش یاسر آسانی؛ آبی‌ها با پنجره بسته در صدر لیگ نخبگان.
🔸
الغرافه قطر
1️⃣
-
2️⃣
استقلال ایران
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/31472" target="_blank">📅 01:15 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31470">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mPIldAbD-SSsEeQOmBcg69gyTAgTF54OJDwxZ9ARvrxJ27o2yqIQzlbZMfv_jul1QAbfaBQKmzKWjpFCa4tB_rkgWZpWXLSet2KhARuwfFEohh4aSVgdIN8F_mhge3SEVrp2xj39VTKKcUg6UlgMJQYKBrhuDeyHDdyWR3QBxKaFq_QZGOMiaVkEaFCEfnzV07qL5SXVj11cDgkQICJy6YREnPzzsZVs0cNtsOopP-pDBAemW4JfuP9qecQJyn41C8nyTrQj6n2REMqlzTkFkW2ioK-kCRT5LQKIVMnp1HsSbn-pSD-eI_Y76JltXqAHvvQDkkZ3_54XjFNQZlIGPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌امروز
؛ از دوئل تماشایی شیاطین سرخ با شاگردان سیمئونه تا نبرد بارسا و گالاتاسرای‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/31470" target="_blank">📅 01:12 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31469">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KAlZoo-vZQ_hODNYSn-bBcKR3uqdUDFGQiWPTbnzoPnFHiJFhNM8RdAV0Jsvv1iHJGI8mSMbeilSHyXaAPDnigDiVZ0uaHSLyC6CEuul69Wx_T-4zoudhDZLN_uOYcEXdqzVN0p7nKO3NBsIZTM8XYH8JxDPQ-pU-sMxIWFK2kVLietygs2DgidmPVbSHXays8kfb85fPiVs_Z7cZD0-Wsv7Z7YtBfRCNCqKvGD5hlWxwyzMK_Vg4BkcBppuGJhAHYeclqDnuzXDPGrWdKdPi75IeaJ6CAuEntYQCyD4xrHiSuj971YM9SXloobIHMPxZ7eSRJgm44GOYAnVjgK5bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌دیروز؛
دومین برد پیاپی استقلالی‌ ها درلیگ‌نخبگان آسیا 2027 با سهراب بختیاری‌زاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/31469" target="_blank">📅 01:12 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31466">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i9XVoZgr2UsZ9WtLv64Gx9SG-bQs9JgIfKXIFAEq6-n7YXiX23qsK2SeqNIeUrCFOiveDW5dB5Br9ViZqa1m_9CIegygJUCWqEqsZgVD5MuZKmrIypLiyUgTurpCqpTbhmpvO0c2_efDAgj6xj39HUSSLU_yK2mXwPuRf4VXFJ0ZgJrvx7xaGmJn8eXDlLIdxaJtRYCSWW1FSl5Ji6zpnjsgbqEj8DRhibRI0x3rK0-Lno7yke6qy-HU7J24k8ccBRQhZkEz9rWTHVq3QQ9thAyL6PVk64N84pjWo2mTfBbGH4FfTWKhC_Aw0slwjSrZvqYoQofiwLe_TK9PVXtjmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NE7QPYOyDgknZbi7HD7JZYzM3wHyaSSJB17W4CvJ1cyxAcaQGpNBUG9JKIzYhE7EHLWvTdiamAH3_frWMYhW7-LKDDuoMVcgfZokPAa34rn5OpPLFJ2U7q4HlhnOrnOtm2NH5o7Eg0humIETXNiM1IPNjIgB2jDEc2aM7Odxq66v6kV3tBu5VxRcdv07njs776mXBuWtVccpAczQw3f_BcKr5NxQw0RSx40yVMHsKZZv7tVJpiSGyYjBeIecBfi8yWct9Pu1hobUUBmP8tzyFu7UcT1uZ4uSTY4ZSO4uvOlaZOSSsIg8mBGzEFRFgyoDFJuBjsLZcU3wplDbTP4Llg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌دوم‌لیگ نخبگان آسیا؛ دومین پیروزی پیاپی شاگردان بختیای زاده در شب درخشش یاسر آسانی؛ آبی‌ها با پنجره بسته در صدر لیگ نخبگان.
🔸
الغرافه قطر
1️⃣
-
2️⃣
استقلال ایران
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/31466" target="_blank">📅 00:57 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31465">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktiF4FjrCCH737h7yY_4ZWL_9FzDdpKK79HKFCTXYM1bAiBEPKuuxGaSotlNLAWM9iDm9jnqsne0XE_z2xDJQL-aReJzkVhz58lpzTvEyQdiyqC_BWw0WbOS9Qr17oRIzu2_xB9zF86gMMM6_eiQMeZXhTJA--uFP1TauXnw7YIvtdR_EXRQVOpQBWkPLQsmqqyMO-c30mmeo_FKQ6Kd33Nontpf4_l__xoCwv8SxCBseGreN3CXDTkZlSbuHJ79atV7SHOI8s3Gjw8JIRqXZcc6FfTv6FHl9JKrrecbxELUmxuTh0-jmctoe7Iezy9DveurrOZRJwTQWQrZYhhL7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
👤
با اعلام مدیر رسانه‌ای باشگاه استقلال؛ مصدومیت یاسرآسانی‌جدی‌نیست و او به دیدار هفته آینده با گلگهر سیرجان در هفته نهم لیگ برتر میرسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/31465" target="_blank">📅 00:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31463">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzKA33uI8jrHpyuuhle9N_9utQPVnHdLl6MZwsN0QkuTBtCCEqna_CrGjWTly0Iq13qInu_HVMdFQeb3wg8zN3wu7SzkACT7bpCDD5p6mIoc4wJ39zDyrMltFbQ3J3u_6WW-3UT77k8lpN4QlNg_qPogEeXsS02gBUePiK_ZFsTVcHfKoEZoZCc1LQySo5Z9Bpw-HPkC03PHS1nLEYD6q0_AxBm2Y9ww9KkRK_45bWHiotPp--jToOGkFbZY2IeJPzUC7fiaAX22mC1nMvCZjLmRvOag-ZLxaCajmrGsL8dLx_GipO3UM_ePy80pAbc7m1Sn_wwz6fi2b-V2tLMLPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
#تکمیلی؛ یحیی گلمحمدی سرمربی دهوک عراقی توافقی قراردادش رو با این تیم عراقی فسخ کرد و به احتمال فراوان با عقد قراردادی چهار ساله سرمربی تیم امید خواهد شد. فدراسیون با افشین قطبی برای هدایت تیم ملی امید به توافق نرسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/31463" target="_blank">📅 00:37 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31462">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nv427RWFl-GM3z2VMalXQXKMOuyPtF3llqvYl1VKQ-nfHcNnU9tFuZuaqwNdh7S5KOmt-7tdNTEI0iR6zrBCejf_KtlMLjw5tkrNPi5ODeJU-Kt3lhmoawWQE3dGkxD-yq_VSIKIh_iR4ZaqLqmVGOkzWlHunkZT3ykSVKx45uI9foVlxtIs2cSU6SQrki1sJh-s0OoatySMNBk81QuSvRJ4xMdkbBj3Abevn20-i6SfZIy9jthcs9O71pP508qjyIsJb3yrT0vYMvcvfZ8b37tEJdahWTXQVwQuP7OYOGURNGY8hNUrJeyYGSgtEESuF60B-n3d9_O_dmRWSu4mxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگام این چه خبری که منتشر شد؛ آرجی میته، بازیگر نقش پسر والتر وایت در سریال بریکینگ بد، به‌دلیل خودکشی در سن ‌34 سالگی درگذشت.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/31462" target="_blank">📅 00:29 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31461">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e66d7fe407.mp4?token=lDVRBOCF2ZR28_ctrzBdjmMa8qUC_V5yInI8zz6dc_ltmqr1l_POyp048E767N6Lnc7XeVslzCzjDFLOXnKr0lXNedX1lZDUPA7mlrsXE2YE6Kktx-dsFM8OKztqylkdpchxGFTQsg2VuTf-Qs9Ex-Fj-kaI_jngOvfylhPAh1cV0Euqp02FMYDwdIfE0zec4YcQzxRs1Uji9VwLFNA742rFXpDi3Gv15HQDNL4fPle2S6FkgLA1xxAjdgXxfjQW_conhBZ0dQ4sqkiR6GkRf2AAo1yQordS2jZ9obVCLzZAQ4C2DFybhvUCd3AqblodmwRai_mjSvXJeqcsdoss3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e66d7fe407.mp4?token=lDVRBOCF2ZR28_ctrzBdjmMa8qUC_V5yInI8zz6dc_ltmqr1l_POyp048E767N6Lnc7XeVslzCzjDFLOXnKr0lXNedX1lZDUPA7mlrsXE2YE6Kktx-dsFM8OKztqylkdpchxGFTQsg2VuTf-Qs9Ex-Fj-kaI_jngOvfylhPAh1cV0Euqp02FMYDwdIfE0zec4YcQzxRs1Uji9VwLFNA742rFXpDi3Gv15HQDNL4fPle2S6FkgLA1xxAjdgXxfjQW_conhBZ0dQ4sqkiR6GkRf2AAo1yQordS2jZ9obVCLzZAQ4C2DFybhvUCd3AqblodmwRai_mjSvXJeqcsdoss3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
پیش از بازی با گالاسرای در UCL
؛ یکی از خبرنگاران درباره‌وضعیت‌فعلی رئال از هانسی فلیک سوال پرسید که اون‌هم‌عصبی‌شد و گفت امیدوارم بالاخره یه روزی یاد بگیری از این سوالات نپرسی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/31461" target="_blank">📅 00:24 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31460">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nCkl28BHAM8hsi-fr-pQuK0kj1zOQ1-fNgLgNCITI3A8iosvIAFtIRMmg3wcdRaVrcVBT7lpoF9k1nbwGU7FmkO7g1FW4oFSmTH0fqq4tv2gAPr0tpFYyWvAiFMq_jljMlEKkKxbjjEB25KP_7Y0QJENjk5N_uthXgFGMHJ1caB_BA4j6aIdEW2dl02TsOjXO1whTnwnigDwMvUaVyRMAS7BKrscWTY-iQkmMx8Tum4NDjJ88tLcV6lKxIUzjVMPksMVnR6mlATjN8F6ZoZsm2yji-BvJo3HD1jKoVU1Xuh6l0FEiLSd7NtNOWYJKlakwY58GLc77cZT-zRxN3W8Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ یاسر آسانی لنگان لنگان از بازی خارج شد و بجای او محمد حسین اسلامی وارد زمین شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/31460" target="_blank">📅 00:08 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31459">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oz5dYK92vMU5_zjOkR49JscKYqXlN5sosbomeHSe9TfoCLjLkYuya2HWvsaY5xBlHfJ6VDjEfFa8AFkIGvef9Eb63MT51K-pnXmF5llkWq5fHV-KUsUkPEkDk_H7dEa5wZ4sIUQ2Ubb3eBzaJ7Sc56FKiHAxPzss_TVAarRJQ7xvTEp-2Ts-QFKhYwKgE4s4mH29cUZRkuqAHn6utz0jD4Ol9ewZYXLnx9URvhO2WFISxRICh8UTFk3pWy_x1SYzHyJtXikbES0WoZxzLaHYBM9RPRDfcSrrmjlmQEOVNdFbCdVF4C3wLyONPS7givNjHea1AGISHlp9tBP_EDuE5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لیگ نخبگان آسیا؛ دومین پیروزی پیاپی شاگردان بختیای زاده در شب درخشش یاسر آسانی؛ آبی‌ها با پنجره بسته در صدر لیگ نخبگان.
🔸
الغرافه قطر
1️⃣
-
2️⃣
استقلال ایران
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/31459" target="_blank">📅 23:51 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31458">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IF3iKNxWq5iNZmZARsi8SSrjdhriSLuVuXmnwYaYne8RXKlnlAoIiDaqbMXkx2BCbv_4iwf4KNVu5s5zBhyCpcMZjIqGaX8RqlguerZ32X9PXJ2eJE_93qjhmz6kONtXcDNJoJoMvM554wgMzA1S_2iqajBzd686lx7P-zp-0y_qlElkMh89Dn9-EYMgyT-0fUcNycfz_-hNNV46KYYH-IbKqLdUnTm8-a5SK1h0XRQD_aatkhFpvinS6NO4t7XjiGp3JW3S0BfHdu-r3X_9uuEiAuYvqIbVgmtC8_Ka40OkxV3bxS_fxnR-vdojnIPzucWPPX13DL5xpE5P107inw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ یاسر آسانی لنگان لنگان از بازی خارج شد و بجای او محمد حسین اسلامی وارد زمین شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/31458" target="_blank">📅 23:48 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31457">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57855f950d.mp4?token=o5JCBm4sagdE79A7SRcs_rdMVKf8OJdWJl7b7sJC79_il2M_LUzV0JtWMiLoYGlMD0mljeD8Zd7VhA2EFiMd9PqGlUhL-UrQyVs4BJpFfZDEqG9RSJQE0BF5VhXkL4k6O4PdN_tfOI9t798__3FYD7MFKdx5uCDrH4PS46XcW32f38NxRggaf7Jze3mjmwmXpbD9hJaRD-Qmn6QhJCXE9lNb4gwTL_fLlF06Y96lm68TsUum6BraAFcVGedZ3JRuRM5x_6lKI-FTKD7HeamSMAoLsdiygNpmE5_M6HQdcCQ124iyoLdi9dZIIZpgQaEel10d54SMTsLQt4ZTFDVs_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57855f950d.mp4?token=o5JCBm4sagdE79A7SRcs_rdMVKf8OJdWJl7b7sJC79_il2M_LUzV0JtWMiLoYGlMD0mljeD8Zd7VhA2EFiMd9PqGlUhL-UrQyVs4BJpFfZDEqG9RSJQE0BF5VhXkL4k6O4PdN_tfOI9t798__3FYD7MFKdx5uCDrH4PS46XcW32f38NxRggaf7Jze3mjmwmXpbD9hJaRD-Qmn6QhJCXE9lNb4gwTL_fLlF06Y96lm68TsUum6BraAFcVGedZ3JRuRM5x_6lKI-FTKD7HeamSMAoLsdiygNpmE5_M6HQdcCQ124iyoLdi9dZIIZpgQaEel10d54SMTsLQt4ZTFDVs_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بوسه کریس‌رونالدو روشمشیر و درخت نخل نماد عربستان سعودی و ناراحتیش از جنگ تو عربستان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/31457" target="_blank">📅 23:33 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31456">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lbk0OMdSYVI5qh7Cz2gDL1TJd0oqAkG43oq8n-WNkPJjI8K4p7qbWkV5JjaVBpYmYNNKIQ7LoEwMBhfLfzTC1guhl_piCMcKWr9XGDzGsrMad1rEzsUFLrl3-M2caEIbC9q7850XtmEji2O-bCt6BYKRRp6YMBDT7DmDQyxbpFaTqaw2yKX5e5czWGLPvircvCuLhD2QjhCCYFG7soMpnVdzMKIimi1JuC8QkT5NcHVpE_dFJH-QSwpVC6d2YdvVEF2my9sZ8C0ATzW1BG2BUD2FiUY0iWqOgDcS1MUrg5Ftvoqt3zjkG7JFhiGHopOqr7RvnjK5gxKbeWj9X3q7tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ حوثی های یمن: بزودی تمومه ستاره های فوتبال از عربستان خارج میشن. کار میکنیم که عربستان نتونه هیچ‌فوتبالی‌رو درخاکش برگزار کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/31456" target="_blank">📅 23:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31455">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad69f494fa.mp4?token=PBg-afK4HokS4aM0QMdm9Ok-NcxL8712owWEEu1xg3SzKjDqlde5juIyiqAHAWXJ6DPgXVGolYJRnddi9tukukqLAAZaNxSJys705xabCokw-gfvWnahPb53_X15yV3WNV_UcWvWO3Qanx-tT8FQW1igSSrMI7YzRr9mf-7_AiAdA5eachKJTNAvkvg3YFZPqRQGU5CMmACuiJn8gS2ycEAsheFNAHhjaGvHJ7w9-gWUao2c-8InC6QCD2XfQzGuQ5VkdOG9eG5nStTHG0KY7uajOUyeVJ5rC-sq3Wa-EjdnJZQ-9vV9BiCadzk0yKQTEgcunQtatsw8uU1qUX20OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad69f494fa.mp4?token=PBg-afK4HokS4aM0QMdm9Ok-NcxL8712owWEEu1xg3SzKjDqlde5juIyiqAHAWXJ6DPgXVGolYJRnddi9tukukqLAAZaNxSJys705xabCokw-gfvWnahPb53_X15yV3WNV_UcWvWO3Qanx-tT8FQW1igSSrMI7YzRr9mf-7_AiAdA5eachKJTNAvkvg3YFZPqRQGU5CMmACuiJn8gS2ycEAsheFNAHhjaGvHJ7w9-gWUao2c-8InC6QCD2XfQzGuQ5VkdOG9eG5nStTHG0KY7uajOUyeVJ5rC-sq3Wa-EjdnJZQ-9vV9BiCadzk0yKQTEgcunQtatsw8uU1qUX20OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
قطری‌ها خیلی زود دومیم خوردند؛ گل دوم استقلال به الغرافه توسط گودرزی در دقیقه 60
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/31455" target="_blank">📅 23:21 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31454">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c059d16e2.mp4?token=Lukvcm9ygZTSaU1b2xypSxOfzmqCnN7rDv15rArG5gWEezelcpTTPBB2pWonGHECyZ4N31mQzOFQS8isBWQ4ceffDAvH9uoYGSeLv6ZoQu-NVsPQcSjlNpWQ-SHWHD-bHUq2YVDJ9Kd-0VnQ8N86XaSGb3bhAq8TKQlZbN1zoRLk6Nckb8H1VrbDRqq7X9zSExh2j9pMoUs_SKb0KfRFAGEMGM1nejtLGFEZWkDUfwIqYAAqPz5Lqf99j9-WcHy37HAg0N7er-hnKi2FdmZa4dM2M4zbSZ_UQYPOvYT5023qEltIDdcjUZet2itMFkr3nCUuwd2wYWuJCdPoAWruPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c059d16e2.mp4?token=Lukvcm9ygZTSaU1b2xypSxOfzmqCnN7rDv15rArG5gWEezelcpTTPBB2pWonGHECyZ4N31mQzOFQS8isBWQ4ceffDAvH9uoYGSeLv6ZoQu-NVsPQcSjlNpWQ-SHWHD-bHUq2YVDJ9Kd-0VnQ8N86XaSGb3bhAq8TKQlZbN1zoRLk6Nckb8H1VrbDRqq7X9zSExh2j9pMoUs_SKb0KfRFAGEMGM1nejtLGFEZWkDUfwIqYAAqPz5Lqf99j9-WcHy37HAg0N7er-hnKi2FdmZa4dM2M4zbSZ_UQYPOvYT5023qEltIDdcjUZet2itMFkr3nCUuwd2wYWuJCdPoAWruPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آبی‌ها گل مساوی رو از قطری‌ها دریافت کردند؛ گل اول‌الغرافه به استقلال توسط فرجانی ساسی 48
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/31454" target="_blank">📅 23:14 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31453">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1448a1396.mp4?token=r4tx2t2P1RjyETzx7kCt7vdj1qY_RoYX_6cqf6VspgiiXTlFfLtSmjgMACVK6_VcQXnYr0ziYbSCg7L1K4vJSYKJiBRRfB1UP1FrHyy3qiU2hP0URrR7-XdIThH89Xt4Fi5l59LimRNgrUhWoZrf0q0FoHCYNzupIaTt66ReTXtrNqD-CGlke-Mb_mrJ2AbojGlzMvG0PPULTlAH-pw8b-ddkQHq3V9nCHob8QnedL18YeWYCmd8lO-2F8cJQhpkXzAmUVMfixovGljttB4_Q2RVy5cX55QPBTmEFlmA4xcyZFnfG1NU5-mm33_CB7jUXn8xHtJnOs6zDWYl4KYJOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1448a1396.mp4?token=r4tx2t2P1RjyETzx7kCt7vdj1qY_RoYX_6cqf6VspgiiXTlFfLtSmjgMACVK6_VcQXnYr0ziYbSCg7L1K4vJSYKJiBRRfB1UP1FrHyy3qiU2hP0URrR7-XdIThH89Xt4Fi5l59LimRNgrUhWoZrf0q0FoHCYNzupIaTt66ReTXtrNqD-CGlke-Mb_mrJ2AbojGlzMvG0PPULTlAH-pw8b-ddkQHq3V9nCHob8QnedL18YeWYCmd8lO-2F8cJQhpkXzAmUVMfixovGljttB4_Q2RVy5cX55QPBTmEFlmA4xcyZFnfG1NU5-mm33_CB7jUXn8xHtJnOs6zDWYl4KYJOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
زوایای دیدنی از سوپرگل یاسر آسانی به الغرافه قطر؛ نانزد بهترین گل این فصل لیگ نخبگان آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/31453" target="_blank">📅 23:04 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31452">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSqHPxABDv13Dwgy4PSdGzeHXMWl_rD9aeYM-jEW2UGfe-WIqECojSHhFftLg0-465Kpx611x4M_t9rLQs2yz65SrY07RLbuRhUKbhGKPlHeyEy9S8ZdxbPThs5IiTFVJxzSJufCnhRrAGETsVVjE0Ll7CMNYXzi3jgWDRQcHoofzBm6kCA4BhQuRr46KZ7oqsSkQ04gEVIR9a1oPnN1AFdHNk82UIf4GaZdtZJ6jMtQ0u8gRQkaiiRTp7W2tSAQJhh7s5kZ1qu-juS6M41IikFbxZgVL60sO-ytOQRJbzKg1pHN-RENyXepBRL3QiAOD2SlTXQ7slvJjzJxbG4rVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
زوایای دیدنی از سوپرگل یاسر آسانی به الغرافه قطر؛ نانزد بهترین گل این فصل لیگ نخبگان آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/31452" target="_blank">📅 22:48 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31451">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tq4akGGObgYypVRerx5MrfDA_V9TIk15waHdg6VKknaIp8xvNblGQBRXCYLyduSEOZJPSACcj7H0faLg9hKMtZ7LIb03f8D2J3nYNJTnJuXelhmvfA6gyaGZYMLYyTMd89cZGeV_ZcIrOYs0kImIqOgar10i8EncO6peijep3JgreZLkkfwCT-ZJf7-siUHVslNQxJZLavoH5IolcwFsl43XMwbY23VFfSUjHlnxEydGZe5To7acQ5mlLbujk0kVfTHj6Wy2Go4XVD2ZWxM6Rghj_2Hb0_iLyooN2petw4WDD6dZjEvarudS6_NVA_ekZWI3V24Ha_iZ17X4_00-Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی‌امشب النصر درلیگ‌نخبگان‌بخاطر هشدار امنیتی و احتمال حمله‌حوثی‌های‌یمن‌تاخیر خورد. عربستان با این‌وضع 3 ماه‌دیگه‌میخواد جام ملتها رومیزبانی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/31451" target="_blank">📅 22:39 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31450">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔵
👤
سوپرگل پشم ریزون فوق ستاره آلبانیایی تیم استقلال بلافاصله بعد از اومدن به زمین بازی؛ گل اول استقلال به الغرافه توسط یاسر آسانی در دقیقه 38
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/31450" target="_blank">📅 22:31 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31449">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8af2c2d01f.mp4?token=mhee04_wSdH6blawWHD-jXg1T796rtLrtOImlx80V9BB9M9n4g8CltLt0HNtg6jrDsmy16r563sNVYrtRmdISRAYhHe3JIB4Ny8uvWGa_NwWBR7K355Er-Cw_Bya3Z6E-FxWJ8_Mde-Q39_u0e7o_46LUrWR0M43dG6fQv0ch8616DwlZ0EawjUsK8ECLCPPKPZFhaF4HyOQeuKVURZZBvfDJi97Xs7PTVl77XQ5egJ4tVaoeU3fgyqS1erOODsrw8Jgmeigxs9bKSUHRIMGVphUEMHOKDTEuB-ipaNtijzRjN9Qr1XD5BgXlM086VbVTQFAbjS2LA0Pqa14Kn4tVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8af2c2d01f.mp4?token=mhee04_wSdH6blawWHD-jXg1T796rtLrtOImlx80V9BB9M9n4g8CltLt0HNtg6jrDsmy16r563sNVYrtRmdISRAYhHe3JIB4Ny8uvWGa_NwWBR7K355Er-Cw_Bya3Z6E-FxWJ8_Mde-Q39_u0e7o_46LUrWR0M43dG6fQv0ch8616DwlZ0EawjUsK8ECLCPPKPZFhaF4HyOQeuKVURZZBvfDJi97Xs7PTVl77XQ5egJ4tVaoeU3fgyqS1erOODsrw8Jgmeigxs9bKSUHRIMGVphUEMHOKDTEuB-ipaNtijzRjN9Qr1XD5BgXlM086VbVTQFAbjS2LA0Pqa14Kn4tVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
شماتیک ترکیب استقلال برای دیدار حساس امشب مقابل الغرافه قطر در هفته دوم لیگ نخبگان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/31449" target="_blank">📅 22:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31448">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7a4d637ce.mp4?token=KgdEIj6vEWG173tSnFfqDB92H5i3pRMYSxTvo98jsZ31USgtehUtwQ04jOSRBHZ94vgcmSNhAw-hSPGlWDhawPD9DqOUGtjgJlViCbuiKLwLyOzyTtO9fw_WzzjSwo2RbrcRI5s2gzMOIvAEtxukfvaJcPCGeE8JndkFA-5gVfWTVAZfDLlJiWGCp5MaMO6sYbfHRuJlMO1h5aztD4SIZAwpulNmaeaJe9gRhL3rmhcEiTDhkGaev768dqH5oSMHDy2v_Tl4xMJLND_JBuD_x86-CfHkY4KZOgXYpWVjV5rXnw4TsfcvSv-9j_tm1T_BC8HEood6H6JpW4nOQMmvnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7a4d637ce.mp4?token=KgdEIj6vEWG173tSnFfqDB92H5i3pRMYSxTvo98jsZ31USgtehUtwQ04jOSRBHZ94vgcmSNhAw-hSPGlWDhawPD9DqOUGtjgJlViCbuiKLwLyOzyTtO9fw_WzzjSwo2RbrcRI5s2gzMOIvAEtxukfvaJcPCGeE8JndkFA-5gVfWTVAZfDLlJiWGCp5MaMO6sYbfHRuJlMO1h5aztD4SIZAwpulNmaeaJe9gRhL3rmhcEiTDhkGaev768dqH5oSMHDy2v_Tl4xMJLND_JBuD_x86-CfHkY4KZOgXYpWVjV5rXnw4TsfcvSv-9j_tm1T_BC8HEood6H6JpW4nOQMmvnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
به دلیل جنگ اخیر دو کشور عربستان و یمن و شلیک و برخورد چندموشک به‌فرودگاه های عربستان احتمال‌گرفتن‌میزبانی جام ملت های آسیا از عربستان وبرگزاری این مسابقه در یک کشور دیگه وجود داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/31448" target="_blank">📅 22:17 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31447">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30cb6e2f17.mp4?token=qS_HZCgxsyzIEmuV9syYwud5Y1pWuLJ0jpwP09L74owAIf6r_A33GLA1RXSNghL9h5rA54u3qeOFYmP67vUqMtqNtFCqZzj7YHzp0q5LXhPmTQ58tDmNhwRbTZW21dgw1Lf1bNZjp97d7eLhDb35MGRhkrNsp3SCA5QFLQCB2wK1ZdD-Tzq_bPAkQzz6pmziIGCZ_CTaw83Kr8dD9curPuCtBJ6UaHR7LcsnrZF6X_8FCNTbHryUTwjj9gy8X4RcqqQWNRaQglk4Rv-jljLcrqzwnSyJ_ikr3QT7773UQgWI6QVKcOLDlN2bfXg7PGWL2tlJp5UT-tusabiWPtlM_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30cb6e2f17.mp4?token=qS_HZCgxsyzIEmuV9syYwud5Y1pWuLJ0jpwP09L74owAIf6r_A33GLA1RXSNghL9h5rA54u3qeOFYmP67vUqMtqNtFCqZzj7YHzp0q5LXhPmTQ58tDmNhwRbTZW21dgw1Lf1bNZjp97d7eLhDb35MGRhkrNsp3SCA5QFLQCB2wK1ZdD-Tzq_bPAkQzz6pmziIGCZ_CTaw83Kr8dD9curPuCtBJ6UaHR7LcsnrZF6X_8FCNTbHryUTwjj9gy8X4RcqqQWNRaQglk4Rv-jljLcrqzwnSyJ_ikr3QT7773UQgWI6QVKcOLDlN2bfXg7PGWL2tlJp5UT-tusabiWPtlM_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی جالب از فوق ستاره‌های حال حاضر فوتبال اگه خانوم میبودند؛ نیمار خیلی بهش میاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/31447" target="_blank">📅 21:40 · 20 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
