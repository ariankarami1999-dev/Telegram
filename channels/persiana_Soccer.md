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
<img src="https://cdn4.telesco.pe/file/ndtSLrz1COmALWAWEzqQRhSu4IPiVLMHp8zBgunBsh2FfAhH4YdIx5Fw2wUZr4JWQdw_zFXm_Ypvv-VbTmoczi-9PwEQoJ-2j43sk-tdvKdzdA6ysEkDDt8QJR7G9GGJt8DnjpyGHXrDbeWrV5eDEx0SeChFqg6_a9b55KyndRg3TyLYbubHfINyIlrkpzmvKu680ssIWZnumsCbasDiYBw2C2PVhGAz6tQ4mEUZd-dVATMe2WKoaTNEENsNwmojsCSgg9ixByxOBDKzNXZJOvCQEf3078KsjCfF2wEoe_qj9uRMQSLFzVfJd2GoBZX2M6BX-tl7K2WDZf7FENsFkw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 594K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-04 23:39:17</div>
<hr>

<div class="tg-post" id="msg-26576">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d08e79ca3.mp4?token=ge755alZYJgBb5OHgyVcNKs-1Dgg5NUEEhhNm568qPFzMmDusXloeQGZcVg13nBcuxsVbMFV-yBSdGYR6F2dNJMb7n_PUr29k51Bma780s0D-np1XS-a2wmDMDh94iRYF7wRlDraW7Cite3ot-T-sB0s9q4uzsYDVKrY8j3qqDbFObZ8kc6pfFRqW1a8icmKEapI_gSlVQZ97u1g7pZwtrLMXBKA-ZTUYL7oEXfQG_ttGhjC_c-wyfK9jjTJb2nTzXz9YBWalVcFeYRd-lzwHCkrrjAja6rcxaXNUZZ5U4rPhyPKe1tiI6fBTYAteu3OPWaLqyqpU-gvxwGrmHMJFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d08e79ca3.mp4?token=ge755alZYJgBb5OHgyVcNKs-1Dgg5NUEEhhNm568qPFzMmDusXloeQGZcVg13nBcuxsVbMFV-yBSdGYR6F2dNJMb7n_PUr29k51Bma780s0D-np1XS-a2wmDMDh94iRYF7wRlDraW7Cite3ot-T-sB0s9q4uzsYDVKrY8j3qqDbFObZ8kc6pfFRqW1a8icmKEapI_gSlVQZ97u1g7pZwtrLMXBKA-ZTUYL7oEXfQG_ttGhjC_c-wyfK9jjTJb2nTzXz9YBWalVcFeYRd-lzwHCkrrjAja6rcxaXNUZZ5U4rPhyPKe1tiI6fBTYAteu3OPWaLqyqpU-gvxwGrmHMJFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه نزنی ما احمد گوهری رو میاریم به جات!</div>
<div class="tg-footer">👁️ 5 · <a href="https://t.me/persiana_Soccer/26576" target="_blank">📅 23:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26575">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dn5rHbb2iDJYtqEZsWL1Wi24oFbVUXj8w6pNjwpZaTUmnMCn0kZD9U7LDolPVgLL2r3MFkRRUQnD-pCij89W-4Mclktzq9O3hD-o8vU4fvcLnFryF_uoy9DTNd1jjTwT_utquwlNBUIfoBrTXGBBfCG9M6Ld0euvGnAGcjaW2FgzpFFK4B-tg-IinjkCztwIlyUSoJ5rUguP4XRyZJ4Dg86ccaGL0kaHK-J2b62qwQRYhzahYGcazQe6ajQ8bFRbVrabB1fzXP8BFUxBgr9oOnW0K2pdTLLm-0UNgUwnMwo7nzGeH2V2GrHc84LMp6jLaEyIl-yPfRPppR7aKe-rvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ حالا که تموم رسانه‌ها خبر از پیوستن اخباری به گلگهرمیدن لازمه بدونید قضیه چی بوده. مدیر عامل تیم پرسپولیس ساعت یک ظهر با اخباری تماس‌میگیره و میگه قرارداد رومیفرستیم امضا بزن اگه نزنی ما احمد گوهری رو میاریم به جات! اخباری هم میگه اوکیه امضا میزنم.…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/persiana_Soccer/26575" target="_blank">📅 23:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26573">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uhEHM7pxoBmg-k8u12Uxo3Uimsw-86XV_ZBKTriqzD14H-Z1vt55PT__RPpjIyYXcsc15ZUx2Ce185hoCo-yr8ThoK-Qnm0NGUbabarr6ycE_EwjsN1OlLRJGSCxGELOS9C2jKViheBO_bRkLl_MN3xEn1kXENngDC1xMCJw0rPVQC_aDi4kH2Oz3P8VOx10Bngo1xHVBaAhWzNelNTGFQmbRJ8Sm0fqMxUmZpETsX9PpQ4e7sOrq93DmodUT70dv5LN9Wtlg_Anf4voGF3rW1P5F81HtqkpAbjrNMLLG6qBosYBXVVWSxetknqTOCTKe1zPsJXexotglNCGOfQdqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ دقایقی قبل سیدمهدی رحمتی شخصا با محمدرضا اخباری دروازه بان فصل‌قبل سپاهان تماس گرفته و از او خواسته به گل گهر برود و قید حضور در تیم پرسپولیس رو بزند. قرار بود امشب محمدرضا اخباری پرسپولیسی شود ولی به احتمال زیاد راهی گل گهر سیرجان…</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/persiana_Soccer/26573" target="_blank">📅 22:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26572">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HgcfWqFQGCeTroBY2gUDtGkBWlJI0hQgOoZwfGRLRpAMbaFsVSrvrdXaboRJTLimRutZLpAm43RFcmdX6kjWrcRRUtkjJtHJUnPv0fVupZ1RrTyu6sDXeg5Ey2FaZefNaUS638OKiFmfP6syWuWinxtAOGvy2uyiPK35bgllymWONJniperCCQQYxE8UkUlpJGUr6MOi_sBQm57Qso6O31NoD0p-I8REbxlSxTHImuL-wFTuOwylZBRqKl0XblJLy5U2Eb4ohuMLdM_eL2mCX_R-ItRS39HTr6VlO7ggFkGJ7Foe-ybvqNyJkXFr8J04IbqQTu_JTGrMgzzwvkxQtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
#تکمیلی؛ خب دیگه تمومه رومانو هم تایید کرد؛ یان دیومانده 19 ساله با قراردادی شش ساله به رئال‌مادرید پیوست. پرز قراره بزودی پول رو بزنه به حساب باشگاه لایپزیگ و این انتقال رسمی بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/persiana_Soccer/26572" target="_blank">📅 22:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26571">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lMpThjY06ZQsizDoIW9lshH_4VfpygY7tJMqgUs21hZ5HQpRfIqEcod8fMlZQXgMhWBj0aGgiNfEGuJTGS19ZyR87hWmTPzpurxkU-6ycxdShA2bhRh2A-5ReJ-vKLDoOHR9_z3sNH3mlWtfVvdYXxbcp3H8RAxUCcfNB5_lr0cXUQ4gP0MsPFXG2mMhjCWCtIU9oJqy5Gk7JUqSm9SnLDlTbOzEkK7AwpUeH2lTa6N9sswNI7yfAtmFElJme6Oxr7sKCd1JKPgayKSyPESwX4RGbH5HBQNvMow4DCImMjJSsbK1ifmgA-AIjpOEnCibHOKsUUP-rlbdQXFR2YPy6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
مهدی عبدی مهاجم سابق تیم پرسپولیس که در فینال‌لیگ‌قهرمانان‌آسیا هم برای این تیم گل زده بود باعقد قراردادی یک ساله به خیبر خرم‌آباد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/26571" target="_blank">📅 22:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26570">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGc7AFT-iMdMsBazX232IouRdsNmL1eWG2X4yEMcXky3gB93wQPpCO6K2Dm0UwJ57RZYKgnHv0Fs2s7IDI0JAhiF3cORjhwyLx2m9dvH7sBKsdKHmFKKZiSMUs0n3MOvEAD2yva1-NIHqOxBDUvbUCUP_VGCVtur0HmMcdfNE5Zqc5MC0N3Hx5Z-6H7ne1qi5JVB4wa1glqSP-2oeNzpw3qa4BdKoSpnNNi0RE8W2F_NspKm7EaSCoZWpuv148qNI1lQ4hhAXJIHkLUHafTV9Z_1xxlpVSl7A3qIdgA35XTT0ZK91qC7YrVHtJl91Deuw8b8Nw-eYEKrsuaYiy-d-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هروقت فکر کردید بدشانسید یاد آرائوخو مدافع میانی بارسلونا بیفتید که بعداز گلی که به تیم بنفیکا زد اینجوری خوشحالی‌کرد و به خاطر خوشحالی‌اش مصدوم شد، گلش مردود شد و تیمش هم حذف شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/26570" target="_blank">📅 21:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26569">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFp6xTPwwDo9OQXlMymoCM0vT_d6hs-e8KHXXvZua4wG2X4s_lUizT1IJJTm0KZcFBUSw-4YLvlFTzgzSFKzpyrhYU8E3XjWIPMoYo6RS7hBwZGyIFYbwulC4p2RpqWkU6Xu1SZzt70KA8LbNVI0xSUvM03JUM5cJ2Om9GGo8f0Lx5BVhkObNQhxwN0PzuW58KFa8lfNhqXzRINczBDgGw7Gosrdh4Ld3pKs-rRESHKa6r1neOo2SPdTXsJv_VFqT3iQCk8UKd-tebAa1OMMeksqkHjzhdgdrVVwIO76dDmBfLX4UD7FaoFWIoQMcoHhumZ1CJR_o5CEmDmyy3_-vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه‌استقلال به‌وعده‌اش‌عمل‌کرد و امروز پیش پرداختی توافق‌شده رو به یاسرآسانی پرداخت کرد و آسانی نیزتمایل خود را برای تمدیدقراردادش به مدت سه فصل دیگر اعلام کرد. بزودی بعد از انتخاب مدیر عامل کارهای تمدید قرارداد آسانی انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/26569" target="_blank">📅 21:28 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26568">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDZFyFhLC7ZMyUfwXZl-QJhJTcgoz4tOGdOJX7WmAiLYSbzbr38eu96yRNvy6gWqyBA50VEKNp0Aa3SWkNZniohhqDUXIlXdk9H4VWvC0qJtX2nBms7qZCEwj76CiWfHwG-wuFIBvWLlg7I7QX-PI99rBFw0AvPj2RB106pPzVmExqp2euCmegUEJFuYLL5SuqyU31Puia22kk-ldPolwMvQWUoJMdEGTgslrkJaT6XNb63CMPL7vGLFZ7MZJ5p0tZvSfAep3Lt-lmu2X1O2_vTqlIHjrYRoW2MZJuKe3R5_MJy768hoScUGjrHUhHQFvvKE85IZgIut_yKbFzhHEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
#تکمیلی؛ تلگراف: خبر مذاکره آرسنالی‌ها با وینیسیوس جونیور کذب محضه. این بازیکن بزودی قراردادش رو با رئال مادرید تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/26568" target="_blank">📅 21:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26567">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uKfARVaPzLqcYz9YwjHm-qpyiFyFp1xAenj9ZCscACUM2ua3AzGSu4IICvf002d5KhI3fmuZFrICbazASxLeREznPqvhEw50acdGRQYiADwAhjFxpDMgLEOId_c5MbExDoMQeMUBIu46Pa7FeUBUmtBPNDTxHsMoDoGB1wtwKHkLWVByHab_eXTgzsXVYGvxUjBQmkdt0kAPwdTVh0ytyHLEgBz-9xCqdOrX56RCDC-6WSKEHKaZ24VSIyYNR617ileSH2enPh9ir6eqe_7n1Mqw1xJ9kbgtVZtPNMreOawtiLvPpRbpqQlxdqlZlv6yEAmwvBWrixHhtTfUx-GVXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
با اعلام رومانو؛
بایرن مونیخ بارا ساپوکو اندیه پدیده 18 ساله فوتبال سنگال رو با قراردادی 6 ساله به‌خدمت گرفت. پست این بازیکن هافبک میانیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/26567" target="_blank">📅 21:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26566">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xhues1riFAtnITQlE0XVG_46o7jYLPUbzrXJv_Ya1K5vX3VWI8LPLznrQRlvDVrTgYk3sPv3Zu6_PiIa8LRMcjebhlBUQAtcxTk9a6xgarpTohTEFbCd08lZ59rrxhRHmrzOONg8fjs6CGjvF-M4JLihnlyoNrrKDbhC-cGfFCQPaSC6pkkfgot9G4IEJPtb654UCeoquP7XfXgYJxcakYjGt7DW1-WoY8QrRAwTGXvcG-1oO7rU8gOug5d2G_--laozCV-55tkYrSgzi417mo3OR57OulFdmhubXpHLXVeKewis0U5NuVtubIMtK5PQBdilPbs50U_-fqBTFYtUtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه میخواین بدونین کیفیت زندگی، اضطراب، فشار، چقدر روی زندگی‌تاثیرداره، باید بگم تام کروز و اکبر عبدی همسن‌بودن. تام‌کروزهمچنین بهترین تفریحات، بهترین بدن رو داره ولی متاسفانه‌اکبرعبدی‌فوت کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/26566" target="_blank">📅 20:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26564">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TV3Uyn81n5NHSkuLu8bNggPjn4xfoTO6dBzPHSHqnZj9xb9ZMxK_SX1qCn5GcoZKHB3-f-9hsAdTXPDt1cmzMumxEh5mm0128eHwQEGcMbcSKlXvFs_oWfyEn03_5hZnyTNjezJ-194sra1m_FcWUwFDGBygUkJw_LgTTrxQ9xMd9Fr-oJ5wmuBfvdcBpFzXCPPACuVS6lEIf6PSpeehCMC0krf96uyfv5f8fi8dTQCh28wNKStEdbqgbxqNMewe3M9EVpMDfF4YoklDBoOd5sOuAdvM1eA-K69VUYqSYYu503RVaLkejkDElYgyP_1MhTBWYKyj6JADJScXrCQ29Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی20روزپیش رسانه پرشیانا
🔵
محمد خلیفه دروازه‌‌بان ملی‌پوش تیم آلومینیوم باعقدقراردادی به‌مدت پنج سال به استقلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/26564" target="_blank">📅 20:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26563">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2409944d0.mp4?token=hucH-4UszKCQDzeNK6sl85PN3ijoVwh53UvAbHpaUW8Vh-JPfBvtY0cdrpOACNXbpGEcXhSi5aOwKbqarEQdQ6cAWsJAU8sStOcDFSNiJ07mdp1oU0a2xRH-1IbSdy6j5OSaa7_Nr6ACPs4Nl8WwSkZDSWpPTIz26htFrCjpKj2z3pZeSwI-t3pydhfT3R9-45NPlXZ9mbRVomxSeHQMRm2F8JVM2_iEpUMEqRKVIryUVhUS_tcWFGRvDxn_2Aa0sWJTi0o7kOPCdTYXKOiypV0WIloOyoZ83wSiL-Wvlu95Ti4h2f5QnA8-JccbU0FKVY6lmvN7v9rFFary8EBtZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2409944d0.mp4?token=hucH-4UszKCQDzeNK6sl85PN3ijoVwh53UvAbHpaUW8Vh-JPfBvtY0cdrpOACNXbpGEcXhSi5aOwKbqarEQdQ6cAWsJAU8sStOcDFSNiJ07mdp1oU0a2xRH-1IbSdy6j5OSaa7_Nr6ACPs4Nl8WwSkZDSWpPTIz26htFrCjpKj2z3pZeSwI-t3pydhfT3R9-45NPlXZ9mbRVomxSeHQMRm2F8JVM2_iEpUMEqRKVIryUVhUS_tcWFGRvDxn_2Aa0sWJTi0o7kOPCdTYXKOiypV0WIloOyoZ83wSiL-Wvlu95Ti4h2f5QnA8-JccbU0FKVY6lmvN7v9rFFary8EBtZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه نساجی دقایقی قبل رسما بر سررقم رضایت نامه دانیال ایری با باشگاه پرسپولیس به توافق نهایی رسید و به‌زودی رضایت‌نامه این‌بازیکن رو صادر خواهد کرد و باشگاه پرسپولیس پوستر ایری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/26563" target="_blank">📅 19:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26562">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ooS8sSfd_3a_gFTvVI33Z9OVKF9tXlDrnwSYVoeRSceCkFBfHoyT44KhGS6r3HDnViWfkGHxPVXofz-VorJ98jab1t5BsEctVzHzbPiHquqgAvjhp8wJE-lplrrjVli8yV_p1nM8zWoT4dXCiyVwq2kZYrCyop4GDSu0IGcAARNW6yMK6V6tD3NfVwHpT5qMq39XYSzPvZD32q7V0R8wUZY4tbHjLBypIPjhedkWf-r82HC_KVW0G5V1neLY0bYY8PbFF_7quh2OmB-XmBFXR0XMluZNt__Q4pyF7YSWCtDgx2aEw8vYxCewhnRajPoQN3mqKdD9z9-z_9XG2Cznlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی #اختصاصی_پرشیانا؛ طبق پیگیری‌ های رسانه پرشیانا؛ باشگاه استقلال پیش از شروع‌فصل‌جدیدقرارداد یاسر آسانی رورسما تا سال 2029 تمدید خواهدکرد. امروز توافقات حاصل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/26562" target="_blank">📅 19:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26561">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66921272ff.mp4?token=Prr34NRaDEQlZsXpAVf6w4QQMe7N05hshoHKZSKuy2EbLyfDjusFEOioANxjDo-g2jy4M6Yixje1UrpH9p5Vms3c5TxhR_9etmHDaeqh56tCntmSI0qnvu8MZ40w_UgxcjkccLRACYr3SryeowJ3V9bBIbfMxBhnPZ-fzEpp2yLu-q9nRlQbGmGQQqedCILNqtA_PfXZrwRD835vAo54mHjCYo62y8kDP-hi4CmfYPp2GfJGQNQW7HdCcBPi350dFRaxD1Fu2K7bPgd1IBQNWriCjL9RqLQIrYvtJSqzaMxQe5qHpZv4FDycq0mpqhZR8knoNiBNgNEZvmbffgpchw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66921272ff.mp4?token=Prr34NRaDEQlZsXpAVf6w4QQMe7N05hshoHKZSKuy2EbLyfDjusFEOioANxjDo-g2jy4M6Yixje1UrpH9p5Vms3c5TxhR_9etmHDaeqh56tCntmSI0qnvu8MZ40w_UgxcjkccLRACYr3SryeowJ3V9bBIbfMxBhnPZ-fzEpp2yLu-q9nRlQbGmGQQqedCILNqtA_PfXZrwRD835vAo54mHjCYo62y8kDP-hi4CmfYPp2GfJGQNQW7HdCcBPi350dFRaxD1Fu2K7bPgd1IBQNWriCjL9RqLQIrYvtJSqzaMxQe5qHpZv4FDycq0mpqhZR8knoNiBNgNEZvmbffgpchw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
حضور جمعی‌ از بازیگران سینما و تلویزیون در مراسم خاکسپاری خدا بیامرز اکبر عبدی عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/26561" target="_blank">📅 18:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26560">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KiJCH_9-o_I-KfU8hMwx8RminURe5qgAq6RNNdCIaTyY-m4g-PitIBtZmR6hLRJvfycAV4Osf3If2QusbKfZRbvq3e99koFFdArUxf7euPGkP1jdEy64j-KFqkpVR-0xq3KDBKzlzRJmh45-F8awq5x97kehKtn6UP0CzVnQVwAAp9A2nmq8KgHIBWJWseQxi5mtGmkmeTiz0C2WvB8x3j0AD0td4hNWtXhWbaY2fkQv8Svjn5K8ItxBO_eTZhKxoFw3p9EqB8hQhEE6PnXgv8AYlqw3Lu9gwMmWx5HgSP2fDHGlk0fIv2pUVlxt4WMTdgXKLyqkTs_JV8ldxd7T8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
از دوس‌دختر لامین یامال پرسیدن‌چرا نامزدت رو بعد از پنج سال ترک کردی گفته فهمیدم لیاقتم بهتر از اونه و منم حق انتخاب دارم و انتخابم هم یاماله:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/26560" target="_blank">📅 18:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26559">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fzrnZc3PF2ZjbenaLwEfwRr0ifU95f-LXQUwROkdIGfgcy7x1tGhKqZE-qYJjQpNM_ZLNnjas-vP89S4Fdnp0Euw9Laf1VtGcBHshDSBq4__4Ij3RrK5kJvGypp640Bl-6VG1B4cTdw8G-G7l0IA8wzvZ42POH1exwv0tOJEDh7D4zoYgtk01iOrsEm0Rr5XRuaNdRSWgfbRTUclTfO5_4CbGkipFhUYw3QcchpC_7t7S4qEdgp9JvGlREQ8mmTHFjgkOBv4zaVYmVJEIk6Lja5vPBxvOvBCElkrg80AiMMxst5-diX3HfeiA0_h-MLjk8TDv2Pso1599KHsKnFVwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیر ورزشی تیم لایپزیگ: در ازای فروش یان دیومانده به رئال‌مادرید 115 میلیون یورو از باشگاه اسپانیایی دریافت‌خواهیم کرد. توافقات بین طرفین انجام شده و به زودی این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/26559" target="_blank">📅 18:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26558">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKq4T1vZSP1je--aJiVhKfRaQfQR7DEhhrRZPmchhLHIs8VRwCuJIpeSbAntHFaEt1tk0ruB6GXh-h10gXetHvmA0ovMzo96dRhPpUthpssIqfm7i8d57d5Oz-INpKiokqUBHVop_sgDt15GUTjj_dPZ2o7v5kZ1cu6gcxKQvtWVgOFEEFYjDgqNQ9YfZhcp4B7lf6tOuX0yPuKO64DNqImDm4yhSlqF2GEmCRgkAOxQDJNDzAU5QYzbGQ4LL72qiDYkn1O3Ke0QRklaNG6ISLZAWn_uc5uQ7P1ursGPGRVdCUop1dnoVZMGqfbOa97QKajG6kTkLT9-N1QHdRwN4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی‌پرشیانا #فوری؛طبق آخرین پیگیری‌ های رسانه پرشیانا؛ محمدرضا اخباری گلر 33 ساله سابق تراکتور و سپاهان تا ساعات آینده قرار داد ارسالی‌ باشگاه‌پرسپولیس روالکترونیکی‌ امضا خواهد کرد و رسما به جمع شاگردان تارتار اضافه میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/26558" target="_blank">📅 17:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26557">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TjrIlwwzjYCy-iEpbXe1UdW51TGrbHy8uLuod6Xo9JhYlmBRPuZFNKReO8kl4uXt1ELceVv7vsrJ_sEQS4CfPpOyq0gFSqMmD5Ps0ia2XimAogI34cVEVylrou9Nfp5_-Uyxt1woCK9KOuWK53uhNGEipy1yLr0tPW2CFeNCtGfjP0ArEOk6q5WUsLzU2qIV5R_jx1tQtPPRR05uQfMkmALwB0fbkN2yl1-RqCIJ4ouGRW5TOZLrvUQ15EobCmqAt02E-nFhoKJi4NVwQNH6ET1syUsCm8F8h4-pJWWWgyWXgL07oC1A5xRFVy-nABLabASH5NFmsspUBT4pShCnHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باشگاه گلگهر به‌‌درخواست‌ مهدی رحمتی خواستار جذب امیر رضا رفیعی دروازه‌بان جوان پرسپولیس شد. این احتمال وجود دارد که درصورت موافقت خودِ رفیعی، این بازیکن با پوریا لطیفی فر معاوضه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/26557" target="_blank">📅 17:55 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26556">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">📹
ویدیویی‌خاطره‌انگیز و دیدنی از عملکرد ریکاردو کاکا اسطوره‌فوتبال‌برزیل‌دردوران حضورش در میلان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/26556" target="_blank">📅 17:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26555">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b2VW5LJvz0BUEUutl19NASI6Boupbja26bx5avyWVUEeXIRrVN6G8tVQCaX9aanxLeJ9_YOu6hFTlyofvG_gOM3gW3jWd3dZR0me7wx2f_lwp-LOEsA6DgCxqCfgmzrMh4V1wo-8tyMmXx5QWADxgJn6Vf0axmt11OJF8tPReH1D1nmWOu-9FuW-pBOHRCJPjeolWqlPWTKAmyvATvwFQ3EQVK28Ycnwq3DOjYZQbw6VI6JP0UcNM_7MWlRmXJp2TWiQiY9aIV-QBhfjWiNTjJXTD3yMQfsMN7LRxTs5A_YwlOwnvR0uvf3MyCA0Th-uaRh1nGVDvMD6xR6rujldPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ یاسر آسانی برای تمدید قراردادش به‌مدت سه فصل دیگر با مدیریت استقلال به توافق کامل رسید و بزودی رسما قراردادش تمدید میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/26555" target="_blank">📅 17:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26554">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_sbgI_3m5iiuF1qwdZCCWHQJDzRZydvEcz3-rQ_U37iX5Wqs88AaDA7ApNZbGxsZiWe_8iitLuQq0y_d2GCbTyiVMO66kG-mY2sZ1hCbyWpTB6pIoS_si6rMCBlPeElp1K_INKPjKLX6BQAW8SQBS7hyUSQgKtYZsCtqz7lwpNmzMXOL_WqpSsttvHBkzFBX8HN1OUIqB8XNjI2weCRQ0Ml8P9kXf3hPlR3czJ2AimEIyMKtvH3Jcaq4BxXwo1wqEJeQMpIyy06kpvmFUKVKZzvSST-QEFmrQyDr771N-KqkaNTI40WqNPVfL9BfsPIxjBYTWZVZZaGKHjSTzxceg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق‌اخباردریافتی‌پرشیانا؛ باشگاه استقلال برای تمدیدقرارداد روزبه‌ چشمی کاپیتان 32 ساله آبی‌ها به مدت دوفصل باایجنت او به توافق کامل رسید و بعد از بازگشت به ایران قراردادش رو تمدید خواهد کرد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/26554" target="_blank">📅 17:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26553">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/spAe5Zw4JmryIT7TSxJ4faMuko2ehzuzV_gHzfI1eVeXEZgEkHAv5jRZ5lYH472lDzfXvMbe9YlBFV1vMeDC2g_0BpCiqgitkAYM6cP_CzG7zF-NX8CQ5tGW4MmuK8sHP2pX4GhV9Nvm485w8XxSFPUt1zNhjiQZlNO4oHFQvnIsKJbVPU8u8befCldC45RLnzfyVKqtnBZi4AYZFVGd8R86_duQOFbAs7LpdHcN5gpOlbwIMKlkFagQUa4QFB_3uCBfES4c6alZvj1DQu6tNswQp0IqFzTK5ZXHUx4BFA4qhUqqpWvcqP8kSzH1v_dNYxqSy63pKLMhmEYK2MwqsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پیشبینی در سایت بین المللی ریتزوبت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⚡️
فرآیند ثبت نام ساده و آسان
⚡️
آپشن های متنوع با ضریب بالا
⚡️
امکان شارژ حساب با کارت بانکی
⚡️
شرطبندی بدون لیمیت روزانه
♠️
کازینو آنلاین شبانه روزی
⚡️
پشتیبانی از 61 زبان
🎰
بونوس 100% اولین واریز
⚽️
بونوس 100% ورزشی یکشنبه ها
📲
اپلیکیشن موبایل برای اندروید
🌐
http://ejh7qy8d.lol/L?tag=d_4828009m_69797c_&site=4828009&ad=69797
🌍
ریتزوبت؛همراه‌شب‌های‌فراموش‌نشدنی ورزشی
⚡️
@Ritzobets_official</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/26553" target="_blank">📅 17:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26552">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/738d729f53.mp4?token=HiTg12Ms2bV4zUYSu9DEaM8mE5cewgMUo6P_t6ZKLhz0DrUE19fUqonbv98Hw649qhfrn_B9kQ3kZBPAqhvxHgOx4yoTaDNBxnY2UJO_EEk-YCuDQeox6tzwNI0M53e7oujWfS4ZqYeSizOyWw6MaQ4rBIBcK-Lb0AXKJuTB_2_JY03uYQfptUYhlrYJ2uUPdLjuEfJXmXBqjai_MJFk65KV7FC2CIPwGCWcW1HXb5XfQ8ov3Jjr1_rNvwZckNt6hMsEc8Bk-pj4GW3cWa-7etIfJcLbJ1sanrYezo-M7pwuED9fTl08rzX1eSR2p5eNLcDD9YCAuzbyk6ItXH4ELg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/738d729f53.mp4?token=HiTg12Ms2bV4zUYSu9DEaM8mE5cewgMUo6P_t6ZKLhz0DrUE19fUqonbv98Hw649qhfrn_B9kQ3kZBPAqhvxHgOx4yoTaDNBxnY2UJO_EEk-YCuDQeox6tzwNI0M53e7oujWfS4ZqYeSizOyWw6MaQ4rBIBcK-Lb0AXKJuTB_2_JY03uYQfptUYhlrYJ2uUPdLjuEfJXmXBqjai_MJFk65KV7FC2CIPwGCWcW1HXb5XfQ8ov3Jjr1_rNvwZckNt6hMsEc8Bk-pj4GW3cWa-7etIfJcLbJ1sanrYezo-M7pwuED9fTl08rzX1eSR2p5eNLcDD9YCAuzbyk6ItXH4ELg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
یادی‌کنیم‌از این‌صحبت‌های ارزشمند علی آقا دایی در گفتگو سال‌های اخیر با عادل فردوسی پور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/26552" target="_blank">📅 17:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26551">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7014b2e92e.mp4?token=b-e_2oXw33rXDKWTFH_0ywAYWsd6WzP7Cr_95KNaKYzjpMcbbCP1UDphdQNy6lP7bnK_jp0Z5kFUh7qnUbiyedfrCOSdjb325gaFuMSAWkfSzIh99tj3JlAwIW8gpgUMgpdj4iWZs1Mm2o9G5G5nxxtGyrlV86LqZmZMbot_OqerwNTMjYBwwybu-zKsQTeyFIJSbxgm3xe-UYY9y3lneskU1kZ2QpUC4nJYindVzXHumi3iHs11mOE4ennCIu4lV9cUtZ7ZSl_YC-pDRffpoZ9wZrv0MW6j5PZO37ubwTmfNDlVu4TLyrNgX3OKutrim-I-QrlV9DCSRmb60ICAEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7014b2e92e.mp4?token=b-e_2oXw33rXDKWTFH_0ywAYWsd6WzP7Cr_95KNaKYzjpMcbbCP1UDphdQNy6lP7bnK_jp0Z5kFUh7qnUbiyedfrCOSdjb325gaFuMSAWkfSzIh99tj3JlAwIW8gpgUMgpdj4iWZs1Mm2o9G5G5nxxtGyrlV86LqZmZMbot_OqerwNTMjYBwwybu-zKsQTeyFIJSbxgm3xe-UYY9y3lneskU1kZ2QpUC4nJYindVzXHumi3iHs11mOE4ennCIu4lV9cUtZ7ZSl_YC-pDRffpoZ9wZrv0MW6j5PZO37ubwTmfNDlVu4TLyrNgX3OKutrim-I-QrlV9DCSRmb60ICAEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عربستان‌میخوادبرای‌جام‌جهانی۲۰۳۴ ورزشگاهی حیرت انگیز درارتفاع ۳۵۰ متری بسازد. این ورزشگاه باظرفیت۴۶ هزارنفر برفراز یک آسمان‌خراش ساخته میشود. تماشاگران هنگام برگزاری بازیا می توانند در میان ابرها فوتبال‌تماشامیکنند و همزمان چشم‌اندازی وسیع و دیدنی‌از شهر را زیرپای خود خواهند داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/26551" target="_blank">📅 17:16 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26549">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EFyIg9yz0mLAbJarvskX-v6b0-vGO8fs74pidC0m9FfjRMcbS3PGev05929daig8YJUsFFMnKPmbboHp4TvHGhphGbNNP7DIuPoasoSak-LfpYu07GjCAWAmwn2ug1Vmjxebm6enRy55SEsCitBaMnXbglLqic6nsNwMnd8IPlZyTvpPtfI8ehEpMY5xwmUtBTd_lKBEwsb-hKHnirNhZOwPfTnBrtwSDMm5C4WsjsEVAbsJhkFPY8GgkvDgjFV7f8i0l0vG7FycBLYoZ2_lFYbXPxlhakwNaJnX2ZUHYUyhfZ8xQj4EFrZQ-Bge94iRKfHIo3Jxf3FJpKp6LTG15Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی #اختصاصی_پرشیانا #فوری؛ محمدرضا اخباری گلرسابق‌سپاهان‌بعد از تماس مهدی تارتار دقایقی‌قبل موافقت خود را برای عقد قراردادی دو ساله با باشگاه پرسپولیس اعلام کرده و اگر اتفاق خاصی رخ ندهد اخباری بزودی پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/26549" target="_blank">📅 16:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26548">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a750ab04f2.mp4?token=r426Ngk6YBP4aWwxfc7G3T4ZAUB3mhdBd1NeFUhrUIPNdvkiCETj9eg5TMZHfLATP2DhfxQQO7SveQ2v-oB_vkTEn7TfFLcgiGlQKMo7QhKsDDKesSUewshMD5KxLX0Vd6AWqlwDtR7Nvkb8_LTy6df8MAA0U09Z_tcvWY4QVe2wNgIjVq6XFzd4FiCOsL0BRB2Ts3QQKHAqfOsmclN4z_S-KWb1GBRiLqe-Moppa0UUOk4xT0tlrMXjJE4s-ciWts7ufztLhzBbzqXhx4KzimgyWqOlkufFNdhjEc78rXi96f18tUJUM6UyvavgMPrCmwySj3LP98YEy8kRgKK-gXikM9jnSe9E4QUyVC-hwvhxgYp5gMtsN5OyyujBYLY3MRJ5oDtJtlJ7pKQVsMafwq7ZLGye7cPGH3XMjcgwo4lT1Ico6BVLrwjTpVkKN2mNZQiOWDn5UEjN_LlY9C27UIU_X77ihq3OVQzXYu1-UHOP7POpSL2JhhQSuC8om1lvWSh3T21i9iyO7105yJ-BLw2kFzz3IWDhUvAtHUp6f0La7OeIj1BPoyPWgl9nsBmo1USVG1xzgW6kD8x0SNXdt0ipzGGBCmD0k4tZ_l65tz7n19ua0eMqDr-9a_6hgc5plYzOL1K477-GXoexs-7DEwdKDdPxk8AVYhbC9vuoH5s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a750ab04f2.mp4?token=r426Ngk6YBP4aWwxfc7G3T4ZAUB3mhdBd1NeFUhrUIPNdvkiCETj9eg5TMZHfLATP2DhfxQQO7SveQ2v-oB_vkTEn7TfFLcgiGlQKMo7QhKsDDKesSUewshMD5KxLX0Vd6AWqlwDtR7Nvkb8_LTy6df8MAA0U09Z_tcvWY4QVe2wNgIjVq6XFzd4FiCOsL0BRB2Ts3QQKHAqfOsmclN4z_S-KWb1GBRiLqe-Moppa0UUOk4xT0tlrMXjJE4s-ciWts7ufztLhzBbzqXhx4KzimgyWqOlkufFNdhjEc78rXi96f18tUJUM6UyvavgMPrCmwySj3LP98YEy8kRgKK-gXikM9jnSe9E4QUyVC-hwvhxgYp5gMtsN5OyyujBYLY3MRJ5oDtJtlJ7pKQVsMafwq7ZLGye7cPGH3XMjcgwo4lT1Ico6BVLrwjTpVkKN2mNZQiOWDn5UEjN_LlY9C27UIU_X77ihq3OVQzXYu1-UHOP7POpSL2JhhQSuC8om1lvWSh3T21i9iyO7105yJ-BLw2kFzz3IWDhUvAtHUp6f0La7OeIj1BPoyPWgl9nsBmo1USVG1xzgW6kD8x0SNXdt0ipzGGBCmD0k4tZ_l65tz7n19ua0eMqDr-9a_6hgc5plYzOL1K477-GXoexs-7DEwdKDdPxk8AVYhbC9vuoH5s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇵🇹
دقیقا 17 سال پیش در جولای 2009 باشگاه رئال‌مادرید درورزشگاه برنابئو رونالدو رو به 80 هزار هوادار معرفی کرد و دوران طلایی رونالدو آغاز شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/26548" target="_blank">📅 15:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26547">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mjkJkh0qjA_6d4vkFa8nhklDpj6-vu5CknE__AK4VkZxn4et3YjOnLEwgNLDNecKj3CwHaHl4cinPKgFPQy_8ivDcZ9xA-60YNiwFLck6ZaMMgwmuVU5BPwzpbwpxI8QphSP3PEdm6yOcPtLJTjdHsZMeXQDOBpHik5N0FML-KOUUBTuFW_ctJLKmXTI3a0jKtbhjaxXGIgNquQNuh-qqoUCT3oAKx28rTMu-ZHrH9fxBm7UbCudMVbSt0sefxk3FvBJiRgM35Td48CBWNAL1vsAyUE7cZRPNGNyZ1DPb_eS4Zmqfoo0Z2VY1XMFFG9jvLyn9jWCFWKFWYQaZPlx2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ بعد از چند هفته بالاخره، سهراب بختیاری‌زاده‌سرمربی‌‌‌استقلال‌دیروز درخواست تمدید قرارداد دیدیه اندونگ هافبک گابنی فصل گذشته این تیم روداشته. باشگاه استقلال ازفیفااستعلام گرفته و درصورتیکه پاسخ فیفا مثبت‌باشد قرارداد اندونگ به مدت دو فصل با باشگاه…</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/26547" target="_blank">📅 15:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26546">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mWoPgrCrjqds4K2MQoABNBGV6ivdfKIznpVvNneZnNmdqve7YVYIt71shdCVRadwIa1VFsnQjGuxyK-7svyOHsn5YoRt_WYfLZcqdydZK6YwtPJglGwuitJWXN-iMBfXwMOHboDHtItBp6RecWPpZZpPrSDMLDUuBB2ODyU50_YjP39qVuF7VLKEt5BQ8TajfHXe28FyqaYxzWpu0diL55d2ljO8Czusx4QG6LQBHvix9sGM-qk0i42siYM6ezBqjSGJjodQzTYZqovw0jdOx2alVGYgRuIE-0Uno3MaIttj3PEGoYRx9C8IM9bL2Mf0vvwKKHL-qBth_mAM0DrKxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
👤
باشگاه پرسپولیس در دوپنجره قبلی بارها تلاش کرد تا مهدی طارمی رو جذب کنه و حتی به نماینده او گفته بود که در صورت موافقت طارمی رضایت‌نامه‌او پرداخت خواهند کرد اما طارمی پالس مثبت نشون‌نداد حالا باتوجه به‌اینکه در لیست مازاد قرار گرفته و ممکنه بزودی ار المپیاکوس…</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/26546" target="_blank">📅 15:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26545">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LElJA7r2XpTHYq6qzGDo4YfuKN_aUJTuyBSAmC-XqXYOIZxL6dx7inq2qQ0Y8Y6ubt-jwUNEgzPEmm2fFLPYKROYVAlxOlNgSwL3i3K5ruxrJysN25oznwcUBzrK-gWOVzVfSTPEB-Yh96YUEVMOuhlLjxBAFKzEXd9Tlu-ZPFKOoo3yfgwnnPSVQzLDI35ZGU6XWD8ecy-gGix0E2_lQcK65AvEiwig5eDE8KT2mPB96ehN7fHhnxlTQnqrQpgYyVkIS7MQljcOfwZSmgk5_j2GadpUTiaJl1kKeglxRXX3jUXbR-0PhoEt_nuwGOY0ctxW9lOs-PYFTA9PmM1Jfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 22 ساله سابق دو باشگاه ذوب آهن و نساجی دقایقی قبل به‌شکل‌رسمی قرارداد داخلی خود را به مدت چهارسال باباشگاه پرسپولیس امضا کرد. پیمان حدادی به‌باشگاه نساجی قول‌داده فردا مبلغ رضایت نامه ایری رو به حساب قائمشهری ها…</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26545" target="_blank">📅 15:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26544">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a35e208335.mp4?token=upprw1UNEd7HEEHlseFz4eG5UgxPhvph-iv8H2cZmmjW8SoNHJn74drm9ZQBnmtcg7Z8uIZSfir9-PU2yeRW4yS16wvZWpUzpgeTe58bwEF8P_skUdDCVJhsjnliU0PtSKk1jTp5jjuYbAChH8LfagDzD48OB1KaLoRmxwiiFaRL6JvrcWu9AN-8pGbK1qiLMmbt9c9xNecWI2B8PSQoK6Bh9ghmQ-2RA1lh5cxL6aRGPRmiOGFYAoGssXd6I4HfRnJbwu57xvTGRES8FhAHqxg3EcfAYaMPphxkM58YmIv2kou7weFeLMKZyeRsM4GUD7OuE5h4nzGiPTPIBpKPyRHoA69x_Dh2MxzeELOZ5AKYAmMwzLCWy4GkhWIrurWtF4MYRYmR9wHgcuY6GoYnvgYuXzAQbSgAcMrLnwhwJIZevzmEumHahECs_84I17Fz7WH-bYj5xArlw4iBERVzkPAgYz29mnnBuS0hlf0wlUUzvMqHKTBRcAdUnHsUyoUBw78JnyukxzTpugNgVmtlREsgFAzpOdtStciknwhMdjFDIdtC1vA3qq9oq6knDlA7peAJAV-P6dBlwDsozUovOCa4Iw5lr1FVV4PBu-vM5NIEDMOoC9ksXy5yp_hTWlP_g_80Lv1StfEDFlSLSt1pwQG7S0nyc3sRipJmzFCJEZU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a35e208335.mp4?token=upprw1UNEd7HEEHlseFz4eG5UgxPhvph-iv8H2cZmmjW8SoNHJn74drm9ZQBnmtcg7Z8uIZSfir9-PU2yeRW4yS16wvZWpUzpgeTe58bwEF8P_skUdDCVJhsjnliU0PtSKk1jTp5jjuYbAChH8LfagDzD48OB1KaLoRmxwiiFaRL6JvrcWu9AN-8pGbK1qiLMmbt9c9xNecWI2B8PSQoK6Bh9ghmQ-2RA1lh5cxL6aRGPRmiOGFYAoGssXd6I4HfRnJbwu57xvTGRES8FhAHqxg3EcfAYaMPphxkM58YmIv2kou7weFeLMKZyeRsM4GUD7OuE5h4nzGiPTPIBpKPyRHoA69x_Dh2MxzeELOZ5AKYAmMwzLCWy4GkhWIrurWtF4MYRYmR9wHgcuY6GoYnvgYuXzAQbSgAcMrLnwhwJIZevzmEumHahECs_84I17Fz7WH-bYj5xArlw4iBERVzkPAgYz29mnnBuS0hlf0wlUUzvMqHKTBRcAdUnHsUyoUBw78JnyukxzTpugNgVmtlREsgFAzpOdtStciknwhMdjFDIdtC1vA3qq9oq6knDlA7peAJAV-P6dBlwDsozUovOCa4Iw5lr1FVV4PBu-vM5NIEDMOoC9ksXy5yp_hTWlP_g_80Lv1StfEDFlSLSt1pwQG7S0nyc3sRipJmzFCJEZU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
اشک‌های زنده اکبر عبدی برای مردم ایران درباره شرایط اسفناک اقتصادی مملکتمون و گرونی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26544" target="_blank">📅 15:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26543">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOVkt5oWbC11Gtq8YwTWAUq3XmCP1D8_VxYhNGsSIAEXYnuta6Dswv0QojwOqGqdw2gOoLkZCOLY6YSNGTKHOaDripBMiAGw87QfaMelVNghDWeZqqAZOFYwqGG3aHaQDUjiUDCCNalLdA6xeNPZtdHyCGlEU9yPfW-6imxMjjWHwmrtfIs3nbitxc45SGFUJ6kGLhdqovFW7fkkO0aPE4ST7plrAJkHO1Z9JMamDX1GuhxRt1Jh6r1mCqJpx_c6SRa5wEJUDahw1O2mpKLFLNthGyLESSAe0clTVtGjuGnAd9VW8jL3oSvG5z4J_HrqjP9i81NfYh1Wf7mnlMg6WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیر ورزشی تیم لایپزیگ: در ازای فروش یان دیومانده به رئال‌مادرید 115 میلیون یورو از باشگاه اسپانیایی دریافت‌خواهیم کرد. توافقات بین طرفین انجام شده و به زودی این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/26543" target="_blank">📅 14:55 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26542">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g36of68ua5lMn12R2QEpJJfcdDOlHb4evFa_8L8iawR4te7QfV79cHW4ThVM25d60DeY1jT-m4_bOf6pQH9A3xjdTK1UIOHopF3R8FqTycxLR2bni3F8vOX5oyNB0nk4Eb99Q0QpqEEkV8BleoeLazOkdGWMvGTFBxbjnvZH-lCqeQpVHWI2sCOIEhzgnEoMQCa7NXZnvEuXi8eEM6NdXSLxRAYIZqtIRKoJPBTFgBZhcV43ikPvS94tXLnE9utRfu7MYtTlwgmS-qnsR7YjaTTKXFDU5afFcemGwcVscNq5jbXC5TyXLkOdefCO0AXaKodfqqAN-CmFwTN8rlbTpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام فابریزیو رومانو و علی رغم شدید مایکل اولیسه به پیوستن به‌رئال‌مادرید؛ این ستاره فرانسوی این فصل هم دربایرن‌مونیخ موندنی شد اما تابستون سال بعد به احتمال زیاد این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/26542" target="_blank">📅 14:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26541">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FASUWGNvYl_oCB02AJoVO2SqKjSkASIQiWOlXel2FcfeMAhViXL7YfZ3VYazBgE8LdpkWKXz5xIha7_JvY9BzEymRDv_3AOKrvzLs0eOuiijUtsdbnrdeyTdRUHC2bsmpDjaXVTCTiLu2fCqUUZQOiiJtd2acd_YZpFQgJRdOP1tsdML56OlctGe5gRilYKx5AfMtEb6JZMkwgLGT5Efr8kkok3SO_uYi8qCiz_yGnwJXR1CjwsdjCy_4Wxl8Q_OLMAXMFhkCzW69CHgETFE7u0YNmrkadUQDFO68DkkmIwXF0P7LZDba2Xom23RWpXD9HFk3pXhGSonbw8CKziF3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
یاسر آسانی ستاره‌البانیایی‌تیم استقلال برای جلسه‌مهم با علی‌تاجرنیا رئیس هیات مدیره استقلال وارد ساختمان‌باشگاه‌شد. این جلسه مربوط به تمدید قرارداد این فوق ستاره آلبانیایی است و ممکن است همین امروز قرارداد آسانی سه ساله تمدید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26541" target="_blank">📅 14:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26540">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZpXz2VhYRwVLswKz5WCKkVjGJ9wthITakWLRs-dZ6qBZE3ZH1omwizDT2yCkWMgsew_EHE1s_WMFS7ge3qvhtVa3WQqPsFGvJrTqamZgIN9Y2OfNmmbbX7JS80iBpoeRdoDYbSgnJcX4WEjwmtir7HPjICFCDag1gFmBuLKs5uSrO5_hxdzgpa_LSYqgzmm-zZgI_XQw5Fd0w-NugxkFIqwD1RevQ02q_8eFdbDhKt2n-L19cwW4DCh-AzggziInRk0I6GTlaD0Zy8Al3Mkz_RiLSp6wzZ4JrWTjPdJIAet7RnbXd-kbrc-LcaUdjZTKzy9_jmW_GMRe6OFSSrvpRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق گفته رسانه‌های یونانی؛ مهدی طارمی مهاجم 34 ساله المپیاکوس در لیست مازاد این تیم قرار گرفته و باید تا میدون آزادی بدوعه برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26540" target="_blank">📅 13:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26539">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rxgo050yNTgmG1S6slg__7ty9lhixPzR8lPW-Lpfsvs8PtwUv44tVPzzvFAvEy7Tpx1t8K5CWZK9jRqnyzBVboNZvqO-muQT2GwWvrZV-TvXJQ_SBRb07igaTXVhjLoNxUgu6sV62VMlc7A5gHiP4mDpi91ObObhwA7yje9k5-an-HaJKo0qCHiMG_dDiFTNYauxMvUva47sInY_UbgWsBjjya_gvEw3PflUX_yFCl8DrvLeMVYGqijazECWuM6OE4WzacjoLqdM65zdy-WOBf7vDWEuN2sj-i3TEq6VWCNg3JcE4WJCKGPGGJhaY6vIvor1Arp22F1N83OZ0G00bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
مهدی طارمی: حالا که دیگه صعود نکردیم اصلا نباید سوار هواپیما بشیم و تا فرودگاه امام میدوییم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26539" target="_blank">📅 12:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26537">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f40399edf.mp4?token=A2RhUUn5HzdFBZ1q71e_OlYGhBwTL_OwCnfO7HcS-vYXiFr4r7OFs7icCyN81W3dgvBzC4ThpTzEN6a6WDgPo5GmvVrw0ZTyBvAgw29MlVW2Jk4raBHuo-lKqPepI_D_k3_16yt7QzUBimhvmCdpLYzU8kSwWq0GOPQkhPf1xJfrKd5-nuQUreceJYF3plq61IHAg6VxPsHsU63HoAirIhRCE4lDyUHQCbdg8uRUZAlptESqYiZRMnK_IflsSWPv9KxvTPPdZ726NVtcuApk1PLSpegNQj56DIimKDMD2uujynetn729VaC0_fjmuMTRmrEEpGunewEx44MCQzp5ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f40399edf.mp4?token=A2RhUUn5HzdFBZ1q71e_OlYGhBwTL_OwCnfO7HcS-vYXiFr4r7OFs7icCyN81W3dgvBzC4ThpTzEN6a6WDgPo5GmvVrw0ZTyBvAgw29MlVW2Jk4raBHuo-lKqPepI_D_k3_16yt7QzUBimhvmCdpLYzU8kSwWq0GOPQkhPf1xJfrKd5-nuQUreceJYF3plq61IHAg6VxPsHsU63HoAirIhRCE4lDyUHQCbdg8uRUZAlptESqYiZRMnK_IflsSWPv9KxvTPPdZ726NVtcuApk1PLSpegNQj56DIimKDMD2uujynetn729VaC0_fjmuMTRmrEEpGunewEx44MCQzp5ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚫️
فکر میکنی برگردون رونالدو جلو یوونتوس از برگردون تو بهتر بود؟ زلاتان ابراهیموویچ: اگه تو فاصله بیشتراز40متراز دروازه زده، آره بهتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26537" target="_blank">📅 12:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26536">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFmu5_aDKvq--XJSDu4WM0dxgqQoP7GUCNcLSurhd1T34O-3xCuOnH_3jMYv7rFQAK0exxnL16qjAIRRgFX84VEmALkjEerbe9TR5mp3ynl2-_sIlyuvPyv70HcfmvOfm1O-fJIRrg5hhkV-uvYw5-0pyw-EhjAPkWaoEU5q6FYStnRgZkyg-hn3UU8aMFnEnQATVC66-sSlECM1OAqC4-mNKJP1Ah-6WMWn6-6BjV7c4Qzs2prexBUz-0esoEbqfB2gjzy24UPYoqZwcwFXCxP1PmzPrYmyrCFNt2MDNZpwek2Cl7WV4XrJ-XU-yFJ7B_db0qKYIOqXR8m_cJV4bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه‌استقلال به‌وعده‌اش‌عمل‌کرد و امروز پیش پرداختی توافق‌شده رو به یاسرآسانی پرداخت کرد و آسانی نیزتمایل خود را برای تمدیدقراردادش به مدت سه فصل دیگر اعلام کرد. بزودی بعد از انتخاب مدیر عامل کارهای تمدید قرارداد آسانی انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/26536" target="_blank">📅 11:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26535">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kvm7qMvBh54STpGrTFfPTJF0XUh75PqfxHzScoBQaks-17aQpEkXWcJxXD5CaVVcAjkF0PY6LqQaeMOM3A6zD_FP5y-t1Wf57h6dq5PEIErlIV4h1T8NckLujP7Mr5XIB5au4_kBWlcznBwP1dqCKmBHLIxw4VDxMOTLaX2ZgQWOSfg73QuBM2dSpa8-DlRjSpGEVYmiOGVBrcqSY0etXlh-XIo4slVVTAA5KDIclBOZUpAHZzmEwoUt2ahO4gJPEfwZNm_bMt3PZzBAL-S9poFrY1Er9RNJ8U692VYmPC-Vtu9bubgRPhv7mLnPxeUtWUjCLr7EzrzurD6j0CoF9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
طبق‌شنیده‌های‌رسانه‌پرشیانا
؛ سعید آقایی مدافع چپ 31 ساله سپاهان و پرسپولیس برای عقد قرارداد دو ساله با مدیریت تیم فجرسپاسی به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26535" target="_blank">📅 11:17 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26533">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WGrBv0qw5EBvmsPZAHHiEaABL_I2s48PPk9qOfWerO8JL6scoGeJYAHG2IpzLqqlZdyQpkjGWDqjrbbYvKU77ickuz1tbZzQzHtWVZlzdjIkRJIIZayqFEfBGOEBZkTKn2Rrg9ZPTnPaWCx33O_3phPc2feERZ_Iu6BibJFdaOBVMFICXk6ARV1znu3SqJWCjQbFsmLL6ZSl6YL6OrkcHVGNoy2EWvz9Ta6O0IiK3vxw8h9CEB3l_tpzykuXXOraHrJnGCY2XIR_ASqPghJndFgidCHTtqkX0YwxU5Jl2v6hs8Y3WOpARgaX1CjPQbqfx7Xu6amHDeQcR3wpstEPSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مصوبات جدید سازمان لیگ فوتبال در مورد نقل و انتقالات در فصل آینده رقابت‌های لیگ‌برتر:
‼️
افزایش لیست بزرگسالان هر تیم‌لیگ‌برتری از 20 بازیکن به 21 بازیکن؛ افزایش لیست زیر 25 سال هر تیم از دو بازیکن به پنج بازیکن؛ افزایش سهیمه لیگ برتری هرتیم‌از 7 بازیکن…</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26533" target="_blank">📅 10:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26532">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IHhZ7GOGk4lYXHOv0ocxxgLOs6WZIEmBfkxzl-3GCTmmJ9YOvsX_n8CKFNaL1_hFAdFVLM_xQmSn495nXgMfkACs6lJvMl7apRQzlp7QrQO8Q70D_Zzxrz6VLKA3udnLGqFvfVsz5ePB3JHIhC8quR4rYlx_YHE7ROc4k7R38u4KhqSidVI8Oitl37YFMeTVm25J451Qg6f8t3dWGGfHVuMzVy91QbAG2qyswXiUU7j9u_aIj1aZMdo-c9V3crZJHdzWE7codyezOdowkkbtZ7z-1cJi5FWwG054qOZ1v40zuWZh-YnlfpMywGg8xPcXIl0P0gprBvwRt5z6CCR2eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال با ارسال نامه‌ ای رسمی به باشگاه ماخاچ قلعه خواستار جذب‌قطعی محمدجواد حسین‌نژاد ستاره22ساله این باشگاه شد. آبی‌ها با خودِ حسین نژاد به توافق کامل رسیده‌اند و تنها رضایت باشگاه روسی باقی مانده.
🔵
باشگاه استقلال به روس‌ها…</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26532" target="_blank">📅 10:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26531">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T0MivnYc5fAW7cSURrI_dym3YZ1zClx78uaAOn4YRgO1qrwd5PDNTUP_Kff048VFRzn3GY_WrakKELpJCqmvDRUrsaNjCO6MgZCUUY-ryvZYkcK53h2reNcbboRnUoqXkqFxW-zvwvNQt3M1uWtyWtRswa1Wq6kSyzWKz4XR9AYx9JdnclmBgdDE1F2LRNu89KLLroRmN4-zbV7yzCeXWOJBFKj9UvbuDf_CvuQGXkEpL7QSY-Z4X9ZAofVuc317nv-Z0Vm5DWXxcXX-QwYFNrJHaOb2h7TH2KJC2Z1aD0DiELKDzBkil2A_aGB4mRPWk5_yCifajWRxUGvfNeQLDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جالبه‌بدونید بعداز زلزله ویرانگر بم، باشگاه رئال مادرید اونجایه‌مدرسه‌فوتبال‌تاسیس کرد، استادیوم و مجوعه ورزشی ساخت و درنهایت بخاطر فساد و پارتی‌بازی‌مسئولین و فرزندانشون داخل این مدرسه فوتبال، کلا منحل شد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/26531" target="_blank">📅 09:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26529">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84e71d5985.mp4?token=jXv_ko_MxGJiCt85CHDAJlJJUhQ_BSUwsMEw4plM1UGOPTk252raEJA1EItEkc4pJ8FL2ccCybfogj_GarschHuvPZc8qhT_28irXOPeM2QcZwG0SgYtLOwbwAJPq7KjYCZd68TBtsMXL4kyorjRtcAGo-yJn-52wO8Q_UBk_Ee7Iq0KXG9c26MpEog-FBn3D_Frce3c2WgXrsK1hpwGrwkyBYkf2NR3FKj3dGIzLiw68o67-seB6E3f9S3JK_-R3zCemM1eQbk3uGGdH1Sc-z52qIxXwpqAKU34wfWL0HU7-bQ12ct2S41cokCvpfNwnV4AOEqPDV3RvtHLBVIKaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84e71d5985.mp4?token=jXv_ko_MxGJiCt85CHDAJlJJUhQ_BSUwsMEw4plM1UGOPTk252raEJA1EItEkc4pJ8FL2ccCybfogj_GarschHuvPZc8qhT_28irXOPeM2QcZwG0SgYtLOwbwAJPq7KjYCZd68TBtsMXL4kyorjRtcAGo-yJn-52wO8Q_UBk_Ee7Iq0KXG9c26MpEog-FBn3D_Frce3c2WgXrsK1hpwGrwkyBYkf2NR3FKj3dGIzLiw68o67-seB6E3f9S3JK_-R3zCemM1eQbk3uGGdH1Sc-z52qIxXwpqAKU34wfWL0HU7-bQ12ct2S41cokCvpfNwnV4AOEqPDV3RvtHLBVIKaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
ویدیویی نوستالژی و خاطره انگیز از تقابل جذاب نیمار نوجوان مقابل رونالدینیو در لیگ سری‌آ برزیل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/26529" target="_blank">📅 07:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26528">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YLH5r_5UwR-I3CpMpZUUzNe6TYlRbdvnnMLjHEHvNCWoX5iYR7ASx0DgdVgtUZRui3yPEibEtvhiUpBadT2ROnCpjWFguvrlvn0x3897J_JZcFlQqbGtf4MRmpuiWN7ICe5Z-2pR8bHA4NXPk9mSV_2zQYGP0I7Xya38YrKAV7kIlrU7efGA6gbYFREWKIYBCw01JehZ7uJlGxSIenzIDlZHMdmtsr7mZauPnQ9zhsGPz_X103E8HmKgl579_8bNDJbYFj-BxuA_O8pVR7HMRpCTRC4tz-WlwGk628rIILKzhCoNvBnMOExRxNFH8C3FnOZg1T8QxnCPPbDHjhosjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیر ورزشی تیم لایپزیگ: در ازای فروش یان دیومانده به رئال‌مادرید 115 میلیون یورو از باشگاه اسپانیایی دریافت‌خواهیم کرد. توافقات بین طرفین انجام شده و به زودی این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/persiana_Soccer/26528" target="_blank">📅 01:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26526">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WlEJUULg96XRfllX_t1u1NqxgdgS92Zw-TyAiGUTC68rziGg7iOJVzqRwYVmT09SwoM2_ZMT82Fk1GnTg6cVzLRIB9XE6VnYvrIeDCCoUv9vu4kodPjbjyFBGKTfpSkdxUDssemjTMPkXKppIaV-rDyDzejvDaIiwe2JWYS8ynxsvhD685QFGblTQQrNIct4EGK5JgZ9jcVn8fgUDEiR4Mw0I23rIvJN8eZxUJ4m-K0VE2rqZfBzhvFGxgauVrM-yFwdYqO_Gk6C067NIzmKSTN8BLoMDWLZQTH_tLSY4MB_E6rLkMt2oD7Z9LW5PfXsXAjGy1xMD62Ab_tOyfCayg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ جذاب دیدارها‌ی‌‌ امروز؛
مصاف تدارکاتی شاگردان آندونی ایرائولا برابر ساندرلند در آمریکا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/persiana_Soccer/26526" target="_blank">📅 01:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26525">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UKwbJg56lV7ImXE-m0rUzCQmEgs90EZMNSYQm8k5Lm1W5BDHFe3RpNK3JdESeLsuqYE5e8OuEyhvYKbc1MVHgIppIcuSBTSqS2i4WwxBI3ULeyfAnGmarV_mwPnsGP4LlhahWYDPusm0-x-ZsiYHHeIr7gvhG4uwbWmAodNu1fMky_GetYQQLbfzlHOl30Z5KKlhbp9E485I6ehihhBw_aU8pJe12esdmknzDPGwIrvBbUbOcq-nnkgifgEzrKSdW3_BhL2GedfdEjXOELoVeFbUc79qlwVBwfVtJgXzbINUR8hGTdrD9AoRzv8Nz_yuIUedYYvGGY6bE9xMCLGUpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج ‌دیدار های‌ دیروز؛
توقف روسونری مقابل سلتیک و برتری‌ماخاچ‌قلعه‌درحضورکوتاه‌ حسین‌نژاد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/26525" target="_blank">📅 01:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26524">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtaOhdKZjS1qvVYdD3Zop-Maf_n16mzdnyi7co_NfUz_DVxOyfumHyaPxYFjC1PE2ReqMiIWZNFMBfRM4eACwhikJOoRg5IrxjwjEKVSiJ6ggcnJleTr22ZIsdU16R3eotEok7WAAqQQbvmOGiacDlkogzKVFEoxZ-WP_KzeK5pUh2L9D3iMChwDHPy4ezZ9vVp9qVrqYN-NsKb4Ha4kenoHWxFpqNkdE7xGiE7iZV_pd7r69HQvZfiSPjNr0E5QeVRFd2nr3RrxVAdGF5DDnFw0RkbraPsYvs09jKRw012DDLYbAmfmmBa-_EZUNnZ6ARyyvp6Qw5cUyxGOZcEPGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
#تکمیلی؛ محمد محبی هنوزآفر ارسالی باشگاه پرسپولیس روامضا نکرده و مدیریت باشگاه پرسپولیس نیز همچنان منتطر امضا قرارداد توسط ستاره سابق باشگاه سپاهانه. هرلحظه که امضا بشه سریعا توکانال پوشش میدیم. توافقات نهایی انجام شده و فقط امضای خودِ محبی باقی مونده…</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/26524" target="_blank">📅 01:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26523">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvGhYJlW2rsTl80k_IfzbsWVnr0jTv7NdJ4DiAzqNBg8PhrIXjLhpkm7X_rCzF_PAFDSWs8wa3iXkPPoZdtGzo-1R7x9bbM8Kpneh70xAhM-iFSi39iFf4hV-y3z-UtWtUP6bHKd2HiyhifJvDGD2Dsqwr1QUgBbhWWT6DW61x6kMLt_BLi5ygnrG1Z7epmnIMNOITr_B7YGfKd2i6KqNFhxtJIwtTa5pdaIOaTL4ZuoM3LFObChCS_7N-aQw8FoIIOHeRyTqo5-8WIA7mrlLSQp2nsV3EOdB2NsrqWwlzq6g8jPcSU29k5kRvnjN_j11CgY0-FwZoastS46D8FNnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
یکی‌از مسئولان سازمان لیگ؛ خبر فسخ قرار داد رامین رضاییان با باشگاه در سازمان لیگ رو تایید کرد. بدین ترتیب اگه پنجره باز نشود و رامین بخواهد قرارداد جدیدی با تیم استقلال امضا کند تا نیم فصل مجوز بازی برای آبی پوشان پایتخت نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/26523" target="_blank">📅 01:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26522">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKqs8Ux712pLiTfeJDPUuxqCFSyS4TjO2y_2IqTvTK0xsAzNeLGPKkFhiuG09B6DeZzO5Ir8EJpxRaSaW-7AyEYXeNkHwmF1iQ0ZeWBxA9BjksSnKkb5h3LvOL_wFoTn0e2DIMew9HvAuuKP6mFHXz73xHcDTat7GsZLChF9-iC3wZfXNyWJInu_SXLiHl4nM07chZgJs3D0R1mY_tjHcSRmLo_YDeawfTk6vJO-B2Ke2t315QMvdhP5WwIJvDVxlgcNfBhnBvj77WV2burwF-9Ybe2CcJ4D7O5Pfhqyn_PS5bCc9OGceFZO4WLtgmvFKTh2kORrxkAEVW4Agk2e3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
#تکمیلی؛ خب دیگه تمومه رومانو هم تایید کرد؛ یان دیومانده 19 ساله با قراردادی شش ساله به رئال‌مادرید پیوست. پرز قراره بزودی پول رو بزنه به حساب باشگاه لایپزیگ و این انتقال رسمی بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26522" target="_blank">📅 00:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26521">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f34e9fb51c.mp4?token=KzzuT_4bpQc6dOqHFKr-yinkH7ZFHcqmI0Fwu9lqiaOFQsHCpN_mKHm-8p19N12PWhHpUIrNKVsTk8pUhEyFpNEhN90Whfe_zGr9Y_4uoCkoxNLm44j-vBV5rAg0rSoJKnud4EevCRZYXRc0x6i2Hqgchsmi_FHfSD_8XV63dD3_mnoY1URiLdhNlZ-3f0H9yJ51fBMJSNpdPXRU3GOXBv33QizvqmmKFRymuv74ADU2L0OQKgqesdgL4b-8UKHmJVCD_kWu9I-eoxZJDHvYR8SFxIgkPv3YsDSnSGlzvs5Cq8tcL1gRcIk5GxJLe_dpqcyyfv3fnXigKbFzbJ_p9YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f34e9fb51c.mp4?token=KzzuT_4bpQc6dOqHFKr-yinkH7ZFHcqmI0Fwu9lqiaOFQsHCpN_mKHm-8p19N12PWhHpUIrNKVsTk8pUhEyFpNEhN90Whfe_zGr9Y_4uoCkoxNLm44j-vBV5rAg0rSoJKnud4EevCRZYXRc0x6i2Hqgchsmi_FHfSD_8XV63dD3_mnoY1URiLdhNlZ-3f0H9yJ51fBMJSNpdPXRU3GOXBv33QizvqmmKFRymuv74ADU2L0OQKgqesdgL4b-8UKHmJVCD_kWu9I-eoxZJDHvYR8SFxIgkPv3YsDSnSGlzvs5Cq8tcL1gRcIk5GxJLe_dpqcyyfv3fnXigKbFzbJ_p9YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
نادیا خمز دختر خانوم پاکو خمز سرمربی سابق تراکتور هم با پارتنرش ازدواج کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26521" target="_blank">📅 00:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26519">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IGsO1uNSSBTXXLxb-GTe6b3id6TmipEU7Ad6WM6HO7HIKhlzeUQNCnkGUgF3IXtC_0pzloxQbD9VcTnvHWyN6JVVI8vlcLqFNoy68t8ACkksE-m414JUw3tPjebH8ncKni9EZVjUzozMTaABd8myis3RYFnYaZxKe9wNt1wPYt0ACLQZlt8MmA8bq4s2dI7MxSg1qQfgTp9JqJ2szuNkATxO0o3vzNjXdkbiyXPbVSHQI0qZeRRnqMQc0IzQW66JX1o44AGZuks31sp-dYThanka9BjtiE5U7z46ZmUkST3s7YOGenSivAVc80n0B-sEGqEdHJKXusdBj9DXoMFaqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛بعداز رونمایی‌از محمد خلیفه؛ اگر اتفاق‌خاصی‌ رخ ندهد باشگاه‌ استقلال کار های انتقال مهدی گودرزی ستاره جوان خیبر هم نهایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/26519" target="_blank">📅 00:31 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26518">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTTiQO0PEJXhltSrkFvN3snlP_rGFaFgK3h1vyvQRNqznn_fsCfDp5sKMVrBz-XaZMJwczs3oZoD6Ytb_4qQlRzLdK81of3MBJgydeAwfq8hG_3TdD3iuiRVpcfrBJ3CH3-3VVOaubDXp-H90kPti2s39hL2qAifwMCL8C3hg_QItNyDCYyEHqYg85lGDTo4OjmUAkf4FXhta8fzux5GmKKGv0N0fmUnZgiXnGtZl_v0YH7EnV4lIPDFt2xuWuohhxZjiwnBMXYPaa216uR3dgV6x_oudw-qMwLLjVVWxnW2fz_LJaF2Ghj2VWwVjiogd0lmzTxb5YJusC-VNq4lMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
رونالدو و جورجینا هم به این‌شکل در تدارک گرفتن عروسیشون هستند؛ این چه سمی بود اخه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/26518" target="_blank">📅 00:09 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26517">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U3aE0i51AKcEKPyPQkSJRpKqjSpQV8pwBmI8U59eCooPgGrmHu-B6pNKWqw48_ungP8kqkwEY61SP62f8eqo1Re7LhMf-0wGIWHbVZNBcYwOzHev52k_9p4_82RM5pfityegYJiEyxJOLQzAGDjXacNB5SviIYD5n9ChjPjzFBOOsv7ylZ3j-1lCK5cx5HS7uKCcbq0GuTvpWAANBImWjcun7Mxd74OPbLOUXK6GALFcnVQQMl9HfzF3x3MwhHCjXuHa2LYCqKrn7ex7bSgKxCETm6QSuexCTO9Qe3XFQMMJ9jVJ3J6XOGNmnwuBq2xfLaeQS2n8uc-y6gRsUwaDJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
باشگاه‌پرسپولیس‌ازدقایقی‌قبل‌با مدیربرنامه محمد مهدی محبی و خودِ بازیکن تماس گرفته و در تلاشه که زودتر این بازیکن قرارداد رو امضا کند. به محض امضای محبی در کانال خواهیم گفت. دو تیم پرسپولیس و اتحاد کلبا بر سر این انتقال به توافق رسیده اند و فقط امضا محبی…</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/persiana_Soccer/26517" target="_blank">📅 23:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26516">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8R-uRM5bki5uEvY446CAesHN4utKx-PYdNYxIiwCPdl0gSR_gJrRRPb7k_WKiED9MPt6-jwd_Ho9vwohEt9Yaernflkc7dOEOkQOCatDg7PDpuUorfddnj3-e6P4LRm8OyAzLUovczjokFhZPld8gl42QTGAenSRmihJACl1yxd8fCZKFl5DVN24W2qe_jOg1XEnKDE1stm7rjbk-hRbYoW0Ib40H9YomG4AJG-OeZYabiMrjOgNCgKDqDS5cFamiCU-7euuI6LoQRIEyTK8EJz2SLYcOOjuIPSjV6lZfH3ow7AxEN3gqRWmV3cixrs6S4tLZTRcnjMR66b2RKwbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
"هبا عبوک" اکس اشرف حکیمی که دنبال ثروت اشرف بود و بعدفهمید که همه چیز بنام مادرشه، بایک‌شاهزاده قطری که 2 میلیارد دلار ثروت‌داره رسماواردرابطه شده. هبا و شاهزاده تو جریان جام جهانی 2022 با هم آشنا شدند، زمانی که هبا هنوز همسر اشرف بود هم دنبال ثروت اشرف…</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/persiana_Soccer/26516" target="_blank">📅 23:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26515">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBo7B1MPgZaVyw3YRXPFHLLFHWuU3Y-E4xLKemyxKSdSQMKzTYwM7EmD4doNLXgrIUppEOrjFkdIJVnpAn906v3IckZvwq8bfE9L1-mEzBwgyRkLLpf12m2kqsAZ925LkOf0xpL558lNrNWdhk9kSwAPLT0C780YkcRWVFS3UtCpLtkI6mIqdHVqHnxo40w6_cYCIEGMBXQ2jvMhNo9T0GLeiU5P0hQYqCGisLOwOWgTtM8O6XppxdD69QeMYRIdwSC360NtaQncv3oZkqsUd5bnKU4azDXHcdoRXiG1oiPA8L_0K-EX0p10jluGTmYkQxV7f6wVw_RQpQyRTWzdYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رسانه‌های عربستانی:
باشگاه الهلال عربستان در جدید ترین اقدام خود با پیشنهاد سه ساله سالانه به ارزش 65 میلیون یورو به دنبال جذب لوئیز دیازه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/persiana_Soccer/26515" target="_blank">📅 23:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26514">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UlhS05l5eYl9UpUain480ypE7xlK3101znDCktclnKYWkPeoCBuCqqn1yEP1hO1pwt7MnxuGIM6UCRhFmgJo2bUFiTU4gDKAX5JhrHs0m-FpYSrT60sasfK4yjiyzB57pAkOXDB1eVC9Clr_D_0DAIKIvt2b5G6QQUODKUYM_YuXoxCW-dfU2CQeXKXfZVGHfU3-n8CIBNbNCIndWDnXnBGzmx07DLBiyTB_ctiA_wxPygdN3A_Ij1aJ_4T2cpsHwIT1W3aP69RBFf1FgH7-LlFctOwgZdMBm6wa5qCsnS9KIYSjSj9cru-edEPa0KELAFW68eGmtf40T745ZSvVmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
#فوری؛ نشریه ESPN: یان دیومانده ستاره 19 ساله تیم لایپزیگ باعقدقراردادی شش ساله رسما به باشگاه رئال مادرید پیوست. باشگاه بزودی پوستر رونمایی از وینگر جدید خود را منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/persiana_Soccer/26514" target="_blank">📅 22:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26513">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbv4NcFJ5FXY6QhsIKZ61GW6l7PysIIZjz3n-UX7S228V6Az3AKGYkhTSj6nqKcwlzoM58REMt5zFXBmiHvml7dr0cluD4UP8ujgF0lb2xiNGvJM0tSDXamI-ohOKWz450jWM3PrxSaE4dpSpak4IcsmQgxyAacIvVwi00bR0EuYZ7CdEQyUcRH46aTCvkSbr-ZXEidWGKQAPjHNHRN6YAAPuFrp_MhgHl0W4SFa9vwkxscm6RsZ6RNP27ZkIJlaOCB8Ki33Y2crAavsfC1Obhb30K5VhwPBQIUvXjSvA2bVQdn-H2LSzvhisBWam8zeY2ELSuHjepA4KO2wAqZAkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین پیگیری‌ های پرشیانا؛ قراره که امشب حدود ساعت 23:00 محمد محبی قراردادش رو با پرسپولیس امضا کنه و رسما پرسپولیسی بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/persiana_Soccer/26513" target="_blank">📅 22:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26512">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjTvbPVt6mWgGNjpfATbLhEgDuSEhQjytTY_X9aC1HKAlJtkQ5VQm5JNRb115HUhMXUaNLawxMeQBuTZfa_F9U_bbXDdEg8zw7MTKCVFgtjDEBpz6NJ8lv2-zpl9XnlQqFW1CaPANTw98EKshPzAnUrCwBjzdDxCTv5bmZ-iz39OoSIyAIxK3RF4Fu6B6cwy_cO14AqoEpKlLTS8-n39qxd_6EkZT9vxbFlM_xI4Mlkz4HyZRF_AXvoGe7azUs47pjDtmOVaY8c5YXcn-Gqgd5OQEDFrT_w0bGKOTgK63pIaxXngoANbB71NwLc2Syi1YQWQPxAH4amUcIKd1janFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فوتبال ایران عالیه؛ مدیریت گل گهر ساعت 2 با جواد نکونام جلسه داشتند، ساعت پنج به سید مهدی رحمتی زنگ زدندکه‌بیاد داخل جلسه، چند دیقه پیش هم خبرش‌اومدکه‌با رحمتی 3 ساله بستن تموم شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/persiana_Soccer/26512" target="_blank">📅 22:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26511">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KS1hJQQigYoU7rQW4Tzn54p_OOL-VnUgwvRABxNo5kZ0PUAT4uqFja4PE39vuYDt1IMKZCTXTJ84HZksMiclnOTK0ZwYJChSul5eanUsQA0MezK0hRg-TYBV2nX9nNiCvKEdDZ2r6i2RoKNI-H2jkq560HyzBbPTiMKnA3M-WTmhdxBXf4PF95W_yq3qTTpK-tCbGfK7_lmQIw-cywhuUTnx2bZmeMMaY4bk-ReX_oTAoNHTgKrP16dYWuKKWascixC4NW5Efi4NhqWefvayQPm-p-wpIjS9p8ZdzKcnClx_LM6dXgoZ8sES3WnhdmpKeMGf0_Z28fGcOzioQuSmbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
#تکمیلی؛عجب‌روزگاری‌شده؛ دوست دختر لامین یامال برای اینکه نامزد سابقش رو فشاری کنه این ویدیو از خودش و یامال منتشر کرده است. چه دل‌خوشی داره که فکر میکنه یامال پاش میمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/persiana_Soccer/26511" target="_blank">📅 21:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26510">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/srIvFKddqQBfWVfxIw1nKBPrXqdCN6PDn4Aw5gfykFLTDM8ytNWl5a9h3mBqIM3hfIhrp2ImIqPvp9lVmsv_aHOWKOv1kQFnRNxk7i890rtWPvhv9oAPYGfU_cEPPtX727UEsIaBK0QhCBGj0e3Ig0z8Egm24wsovBjj5Ex4rYOFFatLklSAQs-PZt2A38hdmCnU3PaLOHytVC-EUDe0XwlCF3wM5COdGTFWFu04i26eKme9A5DgilvLy8oWF0YQs76UkO6qX0lUFssC7y_LREpiAAnGivcSYV4e991GFNvhRNKcPKMw3uZcXWJ2MFF6QdhFVK5ecev0rCyLkMrkkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی20روزپیش رسانه پرشیانا
🔵
محمد خلیفه دروازه‌‌بان ملی‌پوش تیم آلومینیوم باعقدقراردادی به‌مدت پنج سال به استقلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/persiana_Soccer/26510" target="_blank">📅 21:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26509">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHvfQBmRH7L_UCm0ZRyLwpdRmAVD-rHQ1MFIci65pMo3cTrfTGgpgAS4vCZRZXKkiC_SxrsH9mw7oiKjFkc7GZxDEBEEWKarNhVtyLoG4TVHliApE7LyDQ8jsYR4G40002lJPn1t2sttEow1Qg9d2ez6ET6eRxhVhqCwFac-xKRc07CCzz47HnPm33Nig7ZrZE8zOpyHn6yyui3I7Au7VUd-YKwvZUej8uk3OlROM34hRz9Ij53q727KzViNWv3dYkbyMrXq9QIVzlwELFTQCXpgYgbWzOpAy-cIBOnvd-JoEflCkvOE4rWozdOAOfLlQ9b694UOSEwyvzTDJvdFiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال ساعتی قبل باباشگاه آلومینیوم بر سر انتقال محمد خلیفه دروازه‌بان ملی‌پوش ایرالکو به جمع آبی ها به توافق‌نهایی‌رسیدند‌. باشگاه استقلال بزودی 60 میلیارد تومان به حساب باشگاه اراکی واریز خواهد کرد و رضایت نامه خلیفه دو…</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/persiana_Soccer/26509" target="_blank">📅 21:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26508">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QbYMQFT1QzQonks7OROMiGDJ54dBNAES3_ycETWqKJaFThw0LeVuGpn0DHQibO_2MGlD62sD399rbX44Wyj54D-l2LL6qQAO0heO0MiOnHPtQas10vQYv4QYmoYptshBYEni5Wrm5fegL1vV7P26hp0JCk58pFz73OfAde2hsJr6_LTwplMOSXHla2Qz9Mj4tzdlUQUnnAfFpxJBHJjfYbX7_XZeEz_pe71OOA22G88513irPcP4ms4irtsBrTvgBTbpsE18MjONwhMQCIngZF2R-rj4XpFWsyqDsVp9l-HAyYRizQc4qSdYvAzhcbuLg2J7ryRCeM_zs63cgTlSyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آقای دیومانده بازیکن جدید رئال‌ مادرید هم مثل عثمان دمبله قبلا یه مصاحبه اسیدی کرده: الگوی من رونالدو عه؛ خبرنگار: مسی یا رونالدو؟ قطعا مسی!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/persiana_Soccer/26508" target="_blank">📅 21:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26507">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LGpJTq2NLuPFXpPypJ4P13Yd_GwdLepf2SZjf_7FTb7V-cdbM5gNX6r2sM5ToFbJFGfa1H9TCjSx9Jdfmz8cm3D7x-jzBjKJkUhbimXtJ6HVpzM619Wvfg8h2RXL0Ad9f4oPgdDzRnbTi3y5Pok3xPd16CgAGn5lKNsIcjDX3WhQO4_Igkw0z4rwIifUnP_ZjEay2SHdQn1MTMIFdS7Ic6ndu6Ty_CJA3h8z_a7ER3up-UMlLife6tSBMVNVTUNcgStN9D68yAb0HxilzYFHDZBrVUrJ82A4ty3rsU8G5F1pF8wVH91dDTmMyKPknvTP44xBD56IatqVPDisWlVAdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخ آغاز رقابت‌های فصل‌جدید پنج لیگ معتبر اروپایی؛ تنها سه هفته تا شروع لالیگای اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/persiana_Soccer/26507" target="_blank">📅 21:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26506">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nR6GaErbyWl5gfygXgO-dQJkYATPejZc398WJWrLqZSAXsfLjaVTrUtUPc1zfqooMtdega3_a2Hs8g6dU-hQxqRjhW3y2C7VTTfdbuT3rDzHWlIG4vfgI2QqA-I7qH8rLH3JJQiGeq9cMJY85B2zeDmxwt0t41rSzrncilZjr8EebhiV60ZfLX7Zty3TZRCY6z-TJT-yfeQpBfFqRf5erzoZrBgLe6FhGqqbHXFlPyiK_VU6TUDrfMTCCah9ZstzdclXiOsEg5L6yIbaMXlyhcfe99RAJUP6SiDlfp0_QB9tRxHKY-ZeEW-W7QgLeOEV56ZstPl6KIcWqMYAHTvbAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اسکای‌اسپورت: کارانتقال یان دیومانده به رئال مادرید نهایی شده و طی ساعات آینده کهکشانی‌ ها 115 میلیون یورو به تیم لایپزیگ پرداخت میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/persiana_Soccer/26506" target="_blank">📅 20:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26505">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uO1CJVgR_Sv8-XIlxtQOu9ExenoG7zyygjNgIH1qutBZm9z5yDtO9J7YWHgyjHggTYIShfTSfp2ZTKyUvhxNv3jBQed5cWLfEB0vUkr93rrG13OZKHuZvvgugy3SodpGMt8j5OxOcppL6pGY9iTocz8f5Men6Z-WV9p1RkHe0jQ1x09rwdHlHldJXXHIUUzvGGlco_0VmRiS2dn-gxL9FHE7XNpgy6tFuFq4ovjxNY6ky3GdOdn3K6-0xfxpzKgk7EliUqYs1rgz4JR7Kieb8RHOvSx1YFCs1fJhKGNrJ--SG2Whf3gc0IcHGI70NCFgW_1D1Yyn9L_xqsv-7CSq_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌اخرین‌شنیده‌های‌رسانه پرشیانا؛ مهدی تار تار سرمربی جدید تیم پرسپولیس یک فرصت به محمدجواد کاظمیان داده تاشایستگی‌های‌ خود را در تمرینات نشون‌بده در غیر این صورت او نیز همچون شکاری در لیست مازاد سرخ‌ها قرار خواهد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/persiana_Soccer/26505" target="_blank">📅 20:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26504">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YtCG1W_73jr9nCchNYljg5l_-CwVFAg3xI89PiYt1NYPRWzY44wGS68OgVbRcvv4JgNjV2lCfTlwnnxnQ8IZ-er7RBhDLSMee75GEfQOznnXV15BZsVGbDu7TfnqkZcl0p38uaIaXeCU8nuQLBoq7vdGvKsv870hnMKVje4ISVW7SOys2FWQ6RWiCy2lNla729fvM3mAY9_5-6IPMvfWR3aowrJDvNoeiDFc5iQ2u8nVp2IBVXabLROLUIj_BI_EfP4I1jwy31wBRYSL7SAQg7obk_NRx6eumvM-LOSfsW4XDB4cgH3vn_PJx3fM80iTYmPr0XRPqwEwn9_v5jv5cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛ باشگاه پرسپولیس آمادگی‌خود را برای‌پرداخت رضایت نامه 600 هزار دلاری پوریا لطیفی فر اعلام کرده است و درصورت موافقت‌گلگهر این انتقال بزودی انجام خواهد شد.
‼️
فرهان جعفری، مهدی‌مهدوی، دانیال ایری، مهدی ترابی و محمد قربانی اهداف اصلی سرخ ها…</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/persiana_Soccer/26504" target="_blank">📅 20:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26503">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLdXj3nSSg64Kyhpq4HQxvBKQYeQxamPaJNEL4PE9Y_btA59Y4L1v5NDKmLAlmemWg7fT6T3Y5kALUsDXsun7ioveQoKaGOqSEek5RNqmyWo_jJO4NpKB0psNmWKba-OnqcmV7-CWB0BYb8EQ8GpRHVn3tXCOtC5nYAWuGFl6ty5F6pgd37wwULV9XR7yE02l8WFwRwGANm88vNHFUcLb4JC2uhWkPCfnvjxywIq6l5RO2VzgLUndqnp8E8yiA-yn4AZfcu9LVm3RhuKRpCuWmf3W0ZPHhILxHxv_yDREfiJYJqD5j8dmiphyGi4oJBM3QDc9M1hXBX87qYnQ1lNiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
همانطور 12 روزپیش خبر دادیم؛ مهدی رحمتی پوریا لطیفی فر رو از گل گهر سیرجان کنار گذاشته و این بازیکن بزودی به پرسپولیس خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/persiana_Soccer/26503" target="_blank">📅 20:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26502">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7875374a88.mp4?token=YlypzEtWbxxECEEmVShVFF9F_6n7KjC0V5kPNJS-jhCzX5UiKtcrROneLdEpodVuEcVjZTXwqZTjUj8H1jxTsZCrkbZqyUYG_UaMoC3I0DGPsUhuSFyM66txkUfVp_2mHtsJv4o8HDv5dxeZjTGSk9miEu5V7WfPE1rbSlKxBCHP-PlInaSwamFkrT1p4HErVMzq11IEKbWEaInPrNOHIt8T3ppNMZDsmPtgP4Xp-ZmkUkR6bqn1saxfE0HG_FWXEuH6rPHShuzHI-TWq3jtI32KbQLc1kNQ3nlxanBnHUxpAAUVpm3hd7n4m_C24jYxHQ2OIYaBc4ZdrYYkITE8FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7875374a88.mp4?token=YlypzEtWbxxECEEmVShVFF9F_6n7KjC0V5kPNJS-jhCzX5UiKtcrROneLdEpodVuEcVjZTXwqZTjUj8H1jxTsZCrkbZqyUYG_UaMoC3I0DGPsUhuSFyM66txkUfVp_2mHtsJv4o8HDv5dxeZjTGSk9miEu5V7WfPE1rbSlKxBCHP-PlInaSwamFkrT1p4HErVMzq11IEKbWEaInPrNOHIt8T3ppNMZDsmPtgP4Xp-ZmkUkR6bqn1saxfE0HG_FWXEuH6rPHShuzHI-TWq3jtI32KbQLc1kNQ3nlxanBnHUxpAAUVpm3hd7n4m_C24jYxHQ2OIYaBc4ZdrYYkITE8FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟢
👤
پیروز قربانی سرمربی‌سابق تیم فجرسپاسی باعقد قراردادی دو ساله سالانه به ارزش 60 میلیارد تومان بعنوان سرمربی جدید آلومینیوم انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/persiana_Soccer/26502" target="_blank">📅 20:22 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26501">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3-VZdnXzwPcJIORFdKm0SkhWHzVcXSeV4USM0nEn4GydohnP6_dEgn_cGc_DD8lA92EChkIrn98XZ1TWgKc9lIPo3_DtZc-qmAiz10VaeeqHfVn_9ahCgxMA40tbKocO4WAJyp5OAhnOmGK02xm2ssHRca6ddKj1h3MCz7pJhlHboZD8y40_2j0Hp1H2QpmeGj1IdBnq2CXjHfwBcFkK2tr_G6SVP4A5-HZOe3CpFcD-0R8VXOj0sQNUM_8kyf9RjVVXSteT35rA7Sj3_y1NAoa_JB7tacxhXZqeQYk1p626hQQ3k-GMxXUpPd2_7WSE5M45cWdL9LkmlZEKVGlJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌اخباردریافتی‌رسانه‌پرشیانا؛ یاسر آسانی دقایقی قبل برای‌دریافت مطالباتش و مذاکره با آبی‌ها برای تمدید قراردادش وارد ساختمان این باشگاه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/persiana_Soccer/26501" target="_blank">📅 19:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26499">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOI7ENOg8vgC0Y8LOgYboBxIVTcB2WGJAk8lBv92IkjnOKtFmM4hK53W0NhuoR_KbE2Mgum5dji9WOkNHMrJs_p3jHtZmf8OG8ctdOMHoWH2xScGuBBtEtdePyzHb06CDQJquhfpupfiJmX1YrTbQEUmJVcMwmzQUiT0FS5bhjrM-Oyho63MaOamylmmg7AlZx1itdRKjqBsWjx2XfYtcFwqyMMUkJw22hdgdfWaonz34Yx18gBSjnavc4be6kFzBSUTSNZOU6ijJedlbNFz9cXgZD3n-MnqRAhogLIoDLuC2atgPnxADZ9aJilqwEmf1z7-Vt3ytPEqwz6IirtW-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
#اختصاصی‌پرشیانا #فوری؛رونمایی از تنها آفر اروپایی‌فعلی محمد محبی ستاره تیم ملی ایران
🔵
باشگاه لخ پوزنان سه روز پیش آفری دو ساله به ارزش 1.8 میلیون‌دلار به محمدمحبی داده. رقمی که برای هر فصل 900 هزار دلار به‌ شمار می‌آید. باشگاه استقلال نیز آفری‌سه‌ساله…</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/persiana_Soccer/26499" target="_blank">📅 19:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26498">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtDo25-map3unBv-Quw0V7HWRj6VZBHcXoG65iW66dAwB3pHFhF3WG9xzfAoTzr9pp72mds354q8tVFja0SlMdhUEB1dTyiennduTC7QZpP1kP4jwJEPvZEgxVK98LvPj7JZQrXPmKKo1Yx2WJgNGvx0QdiFcCcKwkuRvRK6zoTszHdL_QJfOqOIBJjSsWtmH_97K0hTVg408YiTXq-KXtJUiX8edF8OramWiZxIl-BSMHtgaGttGeFfOswUez-jp-3UiAo8DGFcIG7T0RB99Jj25qu4UFTlqlzeHwJXPrfjCpkpWK1pRQoflAJQsJXVfVHTpbWp3O6b096MeleCnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: وینیسیوس جونیور تصمیم نهایی خود را گرفته و اعلام کرده بعد از جام جهانی قراردادش رو تا سال 2030 با رئال تمدید میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 74K · <a href="https://t.me/persiana_Soccer/26498" target="_blank">📅 18:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26497">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca99cdbcf8.mp4?token=WSjny4Xx-Bmou-sLdAm4S_Mx7IrJeubOWZ_M4QLCTyAcF0JnbWXJnKrILr-0XSuut6dz8U8DGGNmKqFXX0acBkEpyAf8PEcm1LqPobNrSDlfh-f-o_2JGm6I-jZaQitSi8S5pkPYN_h8SSgNQNsqpCDO1cDJQOrHXCRWJKjkciYRLXgjsjtdwGyGUujlI_ijCFQ13xq9xu2oNAECls0EAN0ecq-NP1uHQ9fLlBL9ER14-OwAiPPfhZ8R2ioEGw5yEek3JTShgkVM0d93lSdYNGmb2S4XIODg020yYRZcHG8FsTqT7-Rm24OCXGgrQIr6xgDKx8uB6lYMop84o7dGfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca99cdbcf8.mp4?token=WSjny4Xx-Bmou-sLdAm4S_Mx7IrJeubOWZ_M4QLCTyAcF0JnbWXJnKrILr-0XSuut6dz8U8DGGNmKqFXX0acBkEpyAf8PEcm1LqPobNrSDlfh-f-o_2JGm6I-jZaQitSi8S5pkPYN_h8SSgNQNsqpCDO1cDJQOrHXCRWJKjkciYRLXgjsjtdwGyGUujlI_ijCFQ13xq9xu2oNAECls0EAN0ecq-NP1uHQ9fLlBL9ER14-OwAiPPfhZ8R2ioEGw5yEek3JTShgkVM0d93lSdYNGmb2S4XIODg020yYRZcHG8FsTqT7-Rm24OCXGgrQIr6xgDKx8uB6lYMop84o7dGfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇨🇮
با اعلام سانتی آئونا فردا باشگاه رئال مادرید انتقال یان دیومانده 19 ساله رو نهایی خواهد کرد و هفته اینده نیز به شکل رسمی از او رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/persiana_Soccer/26497" target="_blank">📅 18:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26496">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JDKSIgDU1-AyOw5I_oM99RL8q_CzTLx07qOFEgnCuCGnqLtJvwrB_vqbSA4msa8KMvH8DNobHTfhg-pQ7NtJRczONW-33k3P6CbRTBfO57vsFJzayK7n-FLW5r4OIMSnf8YMFQihiJFO0UlFl8eMTb4XkhCXXocLpDLZGZPOxe6xyUDJerTz71G3ZD1VGakt9D8yMbV7pok8J3eGTM_L5zTk2axZ_CjfNnAmX2fCTU-jISj-40HUKP5BlJxWLEZSLqES4gG9Am7sxEhMSbi2iX5Q4jlzokDIfciU_VJ4xFHKROeGILpWRfwIbwJG-LCUnsdVouxem-izHEbpJTqnjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛اگر اتفاق عجیب و غریبی رخ ندهد؛ محمد مهدی محبی تاساعات آینده قرارداد سه ساله اش رو با باشگاه پرسپولیس امضا خواهد کرد. لطیفی فر هم صبح رضایت نامه‌اش صادر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/persiana_Soccer/26496" target="_blank">📅 18:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26495">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50d8219701.mp4?token=adJlDnAxhHvmHfJZv3BAha1VHZOIYhW_XWxJSv06IcXpE-2T3b-eMeD7yWnGxNUs_cfyixnvoTavRM6Ul2uCysuVgp0BkqZQqfJHx2NSEqtFc2KVFv_34R8J9Y6tOXtHqQkBIzS_A2P0W-YxlumvL7pMB849ub3g5ZlnkVLoq1BnBIRB1CmBQh5oF-vqEyA3uR8PLXPvL9O_-wp7u6DG_P-DzLbBtlH8X5ARcAyQ5SRAqXPkTIgHOP6bxImRgBvevTdvwvFgp6GquiMspa8LVxnIibsHUJAusvgeYecgldtgvYQcDT8Jov8VF1Syiex-waXnhltKwAC42v2CERMLSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50d8219701.mp4?token=adJlDnAxhHvmHfJZv3BAha1VHZOIYhW_XWxJSv06IcXpE-2T3b-eMeD7yWnGxNUs_cfyixnvoTavRM6Ul2uCysuVgp0BkqZQqfJHx2NSEqtFc2KVFv_34R8J9Y6tOXtHqQkBIzS_A2P0W-YxlumvL7pMB849ub3g5ZlnkVLoq1BnBIRB1CmBQh5oF-vqEyA3uR8PLXPvL9O_-wp7u6DG_P-DzLbBtlH8X5ARcAyQ5SRAqXPkTIgHOP6bxImRgBvevTdvwvFgp6GquiMspa8LVxnIibsHUJAusvgeYecgldtgvYQcDT8Jov8VF1Syiex-waXnhltKwAC42v2CERMLSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇮🇹
ویدیویی زیبا از مراسم ازدواج جانلوئیجی دوناروما‌ در منطقه توریستی لوکوروتوندوی ایتالیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/persiana_Soccer/26495" target="_blank">📅 18:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26493">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yf5tZ8mxa2X_takxRwz9WvsezpAYq5pbocKYh5zdNQfy5aeRJM-qNKYfX15GgcTGeRgjwvTwwlF6V-eJjYYK9MUJfiBtqQ-2mX2kc09MniIG2LbPS6P3gW1NqC1eaUVu2Kx02jSZVzuKr89BwkqEVZ8PKyubQZj4ZxGtOYyc3pPIjQCHP6-Yxrq0QHjrQyieKC4kVT8ee2OEia2JAswKhnaf-OabWfNQjX34kP_WdVRy3RonMhi5MI8pv-9d1bL9rOlMit2I93aPCa8aXcuU8OVMxmxI31vjQ_zxdZ3-pQIW_-G0v400EXKsFK4eWL1KKGn7RH9kZQObLtnLsOpUUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/axkomN6TlPWhDmBUYg4V5DcoT3o0jEcAg3ns-D3jbGCYpWE9r8qTRNXJG8c0f03_Oj_mVNBmxFNFXW1eQgnaSBXjfHD1PkhoB7OE0GGIsjraJ8p4wSDwzNmXRl2HbFbIlhw3YddFIrfa64zi0ckfbEy7V3sg77WnD-CXkrx-B0QO40IayxyU8DAOaVmm4QDMImkA4FfWg_3ZziLe75CXMwYvNIwB7yum0dVPjxjKanDG6JhcR4q4tSt5gaxcwgkFT_sBSC-_HFMYd1YibOmSYdp8I0k5teH5nYLHJUdGlmgj_o2KuVsvg060K0FAhI8uwU2Qsaw9Xq-9S35BdOKPOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
لامین یامال درسن خیلی کم اولین جام جهانی دوران حرفه‌ای‌اش را تجربه کرده است و اگر همه‌چیز خوب پیش برود، این شانس را دارد که در شش جام جهانی دیگر هم بازی کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/26493" target="_blank">📅 18:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26492">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLj7nAyIKyaBlcxNJIN9TzKS73EH9nbFEXI9xjbLSw_4TqIofmqCkbspiN_s3u32prMOPpgmAfOVOk1FAwLlFxYKEVrUy0gqR_OsR6vyLMTX6becMFKQSeeVV1ZN3P42a7lelAPAQLLgc3gXUl_RUoK0LhOtQ3OsKVrpCbfeEULPs35ZYlKN4WEbPPTH4MLbcOMjSpFw1uC51RSxQ7lo5i-sttIN-w61EEg77OrX1IBnSlCdY-BXhceO1AqA0L3BOjnCz_qKpGYdY3BBaQ1x1_H18hqFPqHzbQH-7TwRy_kRUzZ91krgoVo24GunUC7qsHoC_nEmHNIk96dl0grvnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#فوری؛ طبق‌شنیده‌های‌رسانه پرشیانا؛ یاسر آسانی شب‌گذشته‌با منیر الحدادی ستاره‌فصل گذشته استقلال ویدیوکال گرفته و ازشرایط آروم ایران برای او توضیح داده. منیر به یاسر آسانی گفته دو پیشنهاد دریافت کرده و اگه با یکی از این دو باشگاه به توافق نهایی نرسه احتمال…</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26492" target="_blank">📅 18:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26491">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Auwppx99tMjWm_HMsnHf-_1unb465Xxcpl6TaACDQW1MNX73C8xwdO6XwA5_43KsG05zpYQkD2SiRtuUvz42P3JVcjJK6RJaOlvLLZOQCkExlbDCbcgWcNMdEUCve1gxYGgrvrbTMczpVMqE2MGx0evORHwwxo7kDWQmhHOELk9t_9_L6NjaEU2lhQOdRQxDj-1H7gMXWUq8G8IdWYLucEu4ljhZqPafjyeQgozQ5qZCjyc8IgDZSbnI-s40vEliGzbPZPjmwWFkQX4UPy30HVZUJa_Rl8lUb78Q78sI1PHS12v4uV6hNbceVQlEysIjsQG8Pz9gIQgYKJSzFKjYxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پیشبینی در سایت بین المللی ریتزوبت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⚡️
فرآیند ثبت نام ساده و آسان
⚡️
آپشن های متنوع با ضریب بالا
⚡️
امکان شارژ حساب با کارت بانکی
⚡️
شرطبندی بدون لیمیت روزانه
♠️
کازینو آنلاین شبانه روزی
⚡️
پشتیبانی از 61 زبان
🎰
بونوس 100% اولین واریز
⚽️
بونوس 100% ورزشی یکشنبه ها
📲
اپلیکیشن موبایل برای اندروید
🌐
http://ejh7qy8d.lol/L?tag=d_4828009m_69797c_&site=4828009&ad=69797
🌍
ریتزوبت؛ همراه شب‌های فراموش‌نشدنی ورزشی
⚡️
@Ritzobets_official</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26491" target="_blank">📅 18:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26490">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SO4w_t-eDUUeY_ZVQbLbZYupmnb7WFPfUyOxOIZ_G5T4g3ztXRyAF6XINMYRsVI44MmM6VfKGv1XQvo8KQrZmUsCX5trnvKA6m07ywLmlhPUZd-r-vIPqZTNJhjn84Qb8oABkHxU2c4Kothv4NHlcEyFNGxcJvVwGE22IyLfVRS6dicsG2KIXslGaLEduzm3XerP2jj1U9Lo8guZwh9_6YqEiuDMXfojJGvaIfkPOKNFG_ldmDlL5WPdVCfwGVSJkD215BYguP87KSK13IA19coInk0z4mioZbCVOV_uFgI4dZOshPP1qgg3Rb_WiKsY9fs7AFSucpmbhOBGvrWhAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ های قطری: باشگاه الغرافه قطر به دنبال جذب منیز الحدادی ستاره سابق بارسلونا و استقلاله و مذاکرات رو با نماینده او آغاز کرده است. علاوه بر الغرافه یک باشگاه مراکشی دیگر دنبال جذب منیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26490" target="_blank">📅 17:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26488">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BhQNGPCFDh8z2FItxfrpPNUpNN7e9qQa4gTY4-eW6y2f6AiXe76EFkl2swXEKhPc0e_RqPDdGK2OTTEvT8Pm9LC2TN-DqpRYdaduD0tE1ZqPQWYG-1VDOQD4FxhztJC80RDUjcxn-NXjsKMkldJvMuOkVxydCqXhGz53rECHfuAtj6XO9g8B_sFf7S7RY6PbpUdnhPur2qOU9tMZ4UlsaKro-Bf8WG5Ov6TkppCt26AlRBH80ysfat0cnUwpu9bgZncpPAoa3yIZcSbRgGaAjugF79yv-Cxa5KhrL1dbsulfN-GgL8M0QgGvDS7b9lUABI7RvbxnpYt2b3d8LGQs_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی پرشیانا به عنوان اولین رسانه؛ یاسرآسانی‌بجای‌سوپرلیگ‌ترکیه به پرمیرلیگ ایران‌برگشت؛ بااعلام‌باشگاه استقلال ستاره آلبانیایی آبی ها دقایقی قبل‌رسما وارد تهران شد و از فردا در تمرینات آبی پوشان پایتخت حاضر خواهد شد.  پ.ن: یه بنده خدایی رفته…</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/26488" target="_blank">📅 17:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26487">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇪🇸
ویدیویی‌خاطره‌ای‌انگیز ازسوپرگل‌های لئو مسی از روی ضربات ایستگاهی در دوران حضور در بارسا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/persiana_Soccer/26487" target="_blank">📅 16:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26486">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMHMtCXD760-c9DiSGAjSGDJQMVM-EuBT6JMIoL1CTjtfw2J-N1sD5sGkAnYwkfpu0jqCx9U4_jxojCGmn-PLUIGoGoBy9AeN1cTUOK5luPjF6XRjj_TjKCjSmmFUfbvLVLda_PJsKvKBbj-nRq14IMbEmUJmGGJDrOt2SoQEDCC8S50m6voLXZZM_ExMsoo4zpKSDblSMwPWpRi7IcNlaWvWjKZsD5Qe4_b5MYKitz9EuwHJrefE8XwhS1y_Tjjk5AoXBISWp6yrKqKWd3jJSMFiv_B08lnu8ZnWOHFVmtT_5k3cPQH3AdUER-FzriwLQdfFRHC98gxmZ__fTUBtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
مسی و آنتونلا ازکودکی‌و‌ازسال ۱۹۹۲ در روزاریو باهم آشنا شدن. بارفتن‌مسی‌به‌بارسا ازهم دور شدند، اما سال‌ها بعد دوباره به هم رسیدند و در سال ۲۰۰۹ رابطه‌شان را رسمی کردند. آن‌ها ۲۰۱۷ ازدواج کردند و امروز همراه سه فرزندشان، یکی از ماندگارترین داستان‌های عاشقانه…</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26486" target="_blank">📅 16:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26485">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pnIs5p6Ec5cl51UTcGG-yWX8eZTaUY2KQgPKj6KXnUtXNZ0F70TfHB8HL0lnTmdaNZaUSkeuiidIlRcILcksIEYWPmGdPZif_5dRyrMZ-tGsqRoWPA7U9pO7Y4vyeeyEwvMCKDJrXBIS2MLhDwWeCcGC-bXHAuII4MxvVyYNkc57DaAIWPTM8MdhumnR98EpEjDUxGm4n84BeIdShjudkTTaLkiazq-9_ML5fTe_HlaS_F1NpTGimGl7PV_xc8WSdSBEbc5GXxYQ8-knUa6S1TajQXAOqj9QIT5a5o_18ZKawB-LNRmz9aGKbSC9KSPtYN4IIKSj66AgyYo2mx6XfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
⚪️
🇨🇮
بعد از علاقه یان دیومانده به پیوستن به رئال مادرید و مثبت‌پیش‌رفتن مذاکرات بین طرفین؛ باشگاه‌پاریسن‌ژرمن از خرید این فوق ستاره پیشمون شد. بزودی کارهای‌انتقال‌رسمی دیومانده 19 ساله به برنابئو توسط مدیریت رئالی ها انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26485" target="_blank">📅 16:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26484">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4edbaf35ae.mp4?token=v0gQLFbiX37RRzlO2-TyL7RNmE7jUAleH4obmL14Hnb4Q-4vpgQDByU7gWKxH-Llt0zuB3AaT82H-87emtM1qSGK-qDwkJzTP3RFrmRIqLYWgQ1UgvtvZKZdwk46Y7oCbb35YMv4M3n-ngsZ4dbcqRG_VFiaK4XadPycydxT7-DYI1WdYBE199x5q_fFtOFMN4k6Wr66ROfU5sky0E9PtVfRwO8Pod6YQpLdpmXj1hBnH4-E3DXaPZ72zrpqvsK_94Fih5H1BiD9JNW0YHZIKHRhkp3zm38O1ZzA1LeU57eKE-6Hwnt6gwB2OjyPd_l3_an5KV5G3LzuzSuoarjxe7lmWMK1urMK2Pjyh-62muRf8oAVXKKyuaYsdCjGfFo9nliErjBdyisRkBM1U1a7ZOl_1u8Q9VUge1PggGiZxbDA41KRlW_abfu-TQMxg--kukLkzV_g73GQjGiboltLe4kemcA7VnYfEXX-wmqHRtwEZ9uz6A1Wt0KaxR1glGQsUFxj8e5iVUxDWsGQIeHZU-Ie8E7UZv5edr7WRY_iSrpWg2ehydVzHmRN9m_G2dXhAlaHLfGJjPDAI3y5gxUnAsOUmSU8d8wRIa0SBW5XlRwqxlspsvJQGLorKgJxONPlg5ZPRApjZqI4bnt2WcoV6IkHoYvIK4GIkVUMr6NJbv0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4edbaf35ae.mp4?token=v0gQLFbiX37RRzlO2-TyL7RNmE7jUAleH4obmL14Hnb4Q-4vpgQDByU7gWKxH-Llt0zuB3AaT82H-87emtM1qSGK-qDwkJzTP3RFrmRIqLYWgQ1UgvtvZKZdwk46Y7oCbb35YMv4M3n-ngsZ4dbcqRG_VFiaK4XadPycydxT7-DYI1WdYBE199x5q_fFtOFMN4k6Wr66ROfU5sky0E9PtVfRwO8Pod6YQpLdpmXj1hBnH4-E3DXaPZ72zrpqvsK_94Fih5H1BiD9JNW0YHZIKHRhkp3zm38O1ZzA1LeU57eKE-6Hwnt6gwB2OjyPd_l3_an5KV5G3LzuzSuoarjxe7lmWMK1urMK2Pjyh-62muRf8oAVXKKyuaYsdCjGfFo9nliErjBdyisRkBM1U1a7ZOl_1u8Q9VUge1PggGiZxbDA41KRlW_abfu-TQMxg--kukLkzV_g73GQjGiboltLe4kemcA7VnYfEXX-wmqHRtwEZ9uz6A1Wt0KaxR1glGQsUFxj8e5iVUxDWsGQIeHZU-Ie8E7UZv5edr7WRY_iSrpWg2ehydVzHmRN9m_G2dXhAlaHLfGJjPDAI3y5gxUnAsOUmSU8d8wRIa0SBW5XlRwqxlspsvJQGLorKgJxONPlg5ZPRApjZqI4bnt2WcoV6IkHoYvIK4GIkVUMr6NJbv0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇮🇹
ویدیویی زیبا از مراسم ازدواج جانلوئیجی دوناروما‌ در منطقه توریستی لوکوروتوندوی ایتالیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26484" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26483">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FugWr0yO3qexBiqJ4A747OBxtcTpp1ZkDuFhRaUQBHnfNCbUcMqZOjdUVVRKFXzXfiLYzw5UTWzwM6ncSqg1WcVucIVP7rgqjmwpoIeM9npA1HGHG4AiK5O7ssfsQfK4pwqV4o12SYfwhMl5YQJMCBbWwO7ShYpRj4Vrq3MCk-EE3zAoIWdBeUcZoNdMMiSfcF_Pb1CAfTi6MCeIkC1RvUVTwRREgJ9srId0G0E8sRTJ2ZVcmi1rLZAnFLsMYF7MOJR4u874LqCuuTBi6SVXuswOZ9xc2ZckppFQSMvYj8l-uf_JMfeXSUSJrhF2YWPlcUP12KNKecQkZYIe-9AKUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ میلاد زکی‌پور برای عقد قرارداد دو ساله با تیم تراکتور به توافق نهایی رسیده و بزودی از او رونمایی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26483" target="_blank">📅 15:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26482">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dNFkeDtOSsz6iXwpAIggU7G9EJdwhvYshoqQ7St3hZ_mooH61yuBnnNx9SeqDt_k-EWFhWEVwse74iLg27Cplq2Q3j429hhs9RZ5INnt6evHxCSefeaRP1GbNHCMWM0ww4x90Qa78wZIZ09a3WC8VLzOUdB_5OVKKV0ZFTK1D8OtqU9FUCGO4Knyj4ovo3JUH4Um6f1wodRCBVlXaj7WWEgsBHwukvmKizK_LvrhApAXm9L0MX0I7Hmjmyvs3Z1IM0Y9seRqRCrDraAHJ4mmKuxi6CviXzKIDbfhHKWXVqkzYcUAeFnUR1SBE01E2cmMmMJqcuIDfCgHpYbpH-g6lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یعنی نژاد پرست تر از سیاها نداریم. 99 درصد سیاهای پولدار فقط بادختر سفید تو رابطه میرن. اگه نژاد پرست نبودن این آمار باید نزدیک 50 درصد بود. نژادپرستی‌فقط‌واسه‌بقیه بده. واسه خودشون خوبه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/persiana_Soccer/26482" target="_blank">📅 15:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26480">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GXSkLxvT4TGFTzcehb220ixZQldgRTPms5RNKgR1o35RZyW5AsFuUvY09CY_-6YcfDv9MOWA-6e7io0AunEyPdodb0pzw_iuNtw4R7wuB1Gfy2_QN6jWegSj5cVmUd4IYFj1QOO0M9OFuEwaDp85ikdIXfMZS1FPp0z-CwXhxUvhRDRDXxIQ_HrhScGWwQoasM_D9C2WmRqRA4Sp7c5YShlRsR2jWp0-SNgmcGRtTfaunklhq9bIJjQSn9nAvEvZzhKTIje3pz2vp39hoCaRMxkELrNcjgpMgLJrXXuoyfqx4nVGtEAviRlIgsKMVVeXBBFX_9DtOqFl7Fn0ZoJHtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا و پس فردا هوای گرمتر از نرمال میشه و دیگه بعدش برای یه دوره طولانی کاهش محسوس دما و دمای خنک‌تر از نرمال برای اکثر نقاط کشور داریم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26480" target="_blank">📅 15:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26478">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHn4c9bsZ97x8tiRs0buF3TsgBbPkHSqjiW7InMAlMuvaTsIije2e3KtIjJ4EzwdGpL69Wa8FrIlRyNu-soOIDvTSOoxSY8vUTkrE7R_VhKW_ngJyNCIx8rEydqdLG-XcbHymkW7MK89_aKbYzL93hpop-ALDYJDZU3EmY0i51Q-0LRNzq7Zncv-U7k5s_jqdQzW_pS84a36FdB1kTxcJ8YMFsLey2WZv_Ix_B7wBs1WIJ0JkHkaT-2bDxn0Q187EN3gd5EV2iugsILay3A0TOYTPgU4FT_88dugScsxO2Lqgb62JdtQl66IMvsoVYw_Slqiows28WcBZ9q9trKJBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇨🇮
#فوری؛ خوزه‌فلیکس دیاز: باشگاه رئال مادرید بزودی باپرداخت115میلیون‌یورو به لایپزیگ یان دیومانده ستاره19ساله این‌تیم رو جذب خواهد کرد. تمام توافقان بین سه طرف انجام شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26478" target="_blank">📅 14:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26477">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VJlC-XFiCuk00l03Ue2BCM6WTwgbfmO-0e9YZFfJtisMJgnnOP0VD41XaB95WQlcKEui1-bnFu9GChz4EWRIkhik3HaX01IhumKbvkd3R_qgcrED2L9bsY61S61C5ya48J1eWv6zYhuEdk1DMhDTQOg6RvIWPyt2DmPw8MlezQpjVETFR9gkoasYgERbQNKKHbVT9kNjNIowkpqHwpwDmo3hlTWvkCeq0rSL9yaQLJRK2mUaDrL9SqZ_CoPmw3g6YLFtu2YwbWLDs54_fBmbRVGAywl3iUHaXOXQGKiLh-qltby4xngsQGdB1T1bzFaIIJiV_G4zXz2DvsIn_oSPjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ میلاد زکی پور صبح امروز با حضور در سازمان لیگ قراردادش رو با باشگاه سپاهان اصفهان فسخ کرده کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26477" target="_blank">📅 14:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26476">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YkXY2ibzdzVNJT1OiuEg-8mheIQjoQZM7RRlryv8MR9QmOhyKlSX0x60k64dJ1JlT61sfnpRLTSPHYtK0hI0_f9z85HFAsIgKNfHNTjnilxo8RnIA1vgxpKCpRuC94fwUN4-bMeBj7n2eUfF1MiLSDSYlhZFr7kZxw_PpzlXgpFX2QTJ9eOatNjbe7fq5K-lcxpmR3Q-JvpsEtr52mIPlfasLB6R5MENnnPD0-FugqeYDKlkNCu_umcaIo2nl1c7v8cxftvsu3CSfAxRGC6kwBjOmHI08BqDsxSXGHoolFGgMUsBiaJD3wxN-Sc-1BoYfp6s4NgyQh2Z6g4482DyDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ میلاد زکی پور صبح امروز با حضور در سازمان لیگ قراردادش رو با باشگاه سپاهان اصفهان فسخ کرده کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26476" target="_blank">📅 14:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26475">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a536e8783.mp4?token=OBHhs_VxfIisvM77LzCXQdFgWYB7DFras3F_ftRMjsuxFpfVcjyeTljsz-bv-qtAXMBIpSDFLHmgBo1fEmnb25XOEkO1vy2dF7cHafS4gVpxlY-U9sMDFg_ot_TldWHzyoLjLZOY4OXgg370op1unXqCCgvW_4SXQcKFCdZFuyVWfTBg2cnXNkI9hSxv6Y4RR9d_6QcKQdJPvvDy-Ib-Bk4dQeiDO0lT1r-SDmdqf4Y1Aqec6xioToCUllAjQiONtKIBj-Fl-xulqBkxKRIGJA3rNVj37GhTOMzI6YTvCldMKj_hFsLkmIB43dZ1re0sV_n9mcFKs3Em4OzHlmIRoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a536e8783.mp4?token=OBHhs_VxfIisvM77LzCXQdFgWYB7DFras3F_ftRMjsuxFpfVcjyeTljsz-bv-qtAXMBIpSDFLHmgBo1fEmnb25XOEkO1vy2dF7cHafS4gVpxlY-U9sMDFg_ot_TldWHzyoLjLZOY4OXgg370op1unXqCCgvW_4SXQcKFCdZFuyVWfTBg2cnXNkI9hSxv6Y4RR9d_6QcKQdJPvvDy-Ib-Bk4dQeiDO0lT1r-SDmdqf4Y1Aqec6xioToCUllAjQiONtKIBj-Fl-xulqBkxKRIGJA3rNVj37GhTOMzI6YTvCldMKj_hFsLkmIB43dZ1re0sV_n9mcFKs3Em4OzHlmIRoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
شکیرا به بچه هایی که توی اجرا جام جهانی‌ اش بودن قول‌داده‌که میبرشون مادرید باهاشون اجرا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26475" target="_blank">📅 14:25 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26474">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pb_08_1k27JJVym3uVDRI8nKrkH2dOz3a7K7iYB1W0-rZx4GHdwbSaQIBa06f8cpOEij87jR30AA5e-7NttQ5XBr9DEZPOvsj8VgepP4l3y8G2F-lSGJT9Y1OV7SU_MihABM89EEkvUjMP7XlDMxnEB345W24iCpR5EkP_uXd6AilT9KA77dybk-eUZ0M8x2zzFCb2XfXQttQrMmSUgXbIKFlMVZ29ZYwqoq-oxbd6E10bpEPf-ovyczFDUyDVCYTst21v1VqZr2ks98myevU2FgQPn2YdubRAUlaSpmjEfh5ZcNqPdz8ltxxFesBpEtbBhUf8ficmP2i1wnP_aSEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میلاد زکی پور و آرش رضاوند هر کدوم به ترتیب 20 و 15 میلیاردتومان‌به‌باشگاه‌سپاهان تخفیف دادند و در جمع طلایی پوشان زاینده رود موندگار شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26474" target="_blank">📅 14:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26473">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRCOyAR00SXBfJZcBdCpr-FdWb7DhuABGA0gLnUS0tq_MzHblB4oHS8IeEOeJYBRjnZKPvC6EOf4L47sUWsE9FKVpxNMPwF4s3Aice9ni7g87EG2Nz3etx6Iq9x5KgceXk_Qit6p4g6GInyQmIn-_wrn6Wb3rvDIuKufaihybQ7P2770t00Otpb0R4uiCvEJFHJJxmg8jfKGVu3Azc9pJQZtl7a8gOLb_iDv2dHhc8_SuoLzyMERsy2DRhOm3gHDtYKrz8b6uqpM_DfT0kFJ6m6hORI73W7YIP3aCebHjjO12Gjiby-iezt9Y90EcuOGUtE5V0O_bgEbON1v-P2aEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ بعد از عدم موافقت باشگاه تراکتور با پرداخت مبلغ رضایت نامه سنگین‌محمدمهدی محبی؛ مدیران باشگاه پرسپولیس ازشب‌گذشته بامدیربرنامه‌های محبی تماس گرفته‌اند و پشنهاد مالی خود را برای 3 فصل حضور در باشگاه پرسپولیس داده اند. مدیر عامل باشگاه…</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/26473" target="_blank">📅 13:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26472">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0udmizLTO79KKhYKIePpWhE1U6TM71ytQ1CXZo3Wl7XKClGk9C56Ky8SoBZaQkQTACAODQbaiPWbxqnKnduIKXvxyPtqTOpzzk0OCLfPjwP2ikzGG5dcMu3cObhO_Qt36woJ7-QBe-d4gSFwDBp1YBbzf55dCXYmep2SC-YUSZrnawKBMU6Y8zxVKSfdbh_qFujOTy-zEuLJnTMztpF0ExGnv2-3xrE38VlfjM-uAVZfyA1m08VA8BcYL_XXCu_wdg10c6De9yHGw6ANhbaThHMuc6Qakeb2hsHfAi23OsxZy0PfWUPAvJ_1za_tWhSXkynkcZu_CqO5QLjNbSJWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
فلورین‌پلتنبرگ: یان دیومانده به‌سران باشگاه لایپزیگ فشاراورده و میخواد دراین پنجره راهی رئال مادرید بشه. مورینیو هم اوکی نهایی رو برای پیوستن ستاره 19 ساله تیم ملی ساحل عاج داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26472" target="_blank">📅 13:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26471">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXKEDyrbsW6QGFckI2yXTEQzfjDaI1Ef9rT4D3yI_0lI4zxm56EPqghtCL0eF5pfKRVR3vYrNDCZR6vIRwKUL8_OJrmYzLmVEWLIsIBL_LEmiqoBkitjcmi5CoDDRWTKzSYJW3dg2-A1wVreJWP0vNShqjj3TpkyLtT_KKgdcSyCRqKiJ1XdUHd6WspNxr-6rPzRufgCq-b0dhQGNZ41dERd-hIwcNyXZPZCbLd0IQlN2xit-uma01KYvprKlHRiWgvTIF7TCRU_lXk5STiBB-JB0XgC2eY0TilMN7k-KEdq3ypcBFrkQHGWBTCuUfVkKQVSr0Id6BC2hBAEJeRDgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قلعه‌ نویی‌ گفته بد کردم ایثار کردم! آقای قلعه نویی‌محض‌اطلاعتون؛ «ایثار» رو سربازی کرد که تو اوج درگیری و جنگ، با وجود همه خطـ..ـراتش پست نگهـ..ـبانی خودشوترک‌نکرد تا شما الان راحت بشینی پز ایثارگری‌بدی! «ایثار» رو اون پرستاری‌کرد که توی اوج دوران کـ..ـرونا…</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/26471" target="_blank">📅 13:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26470">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQ8838qWZSo2ciRosa9v8w5-snAbXwidxqlOjKMXmL87NbLP2b0wH5pZKgdjVNNAF8tWwL_5isB17bUm7r0eiAtCB3Bm9Y8U9azq8w-Cy34N15bwBOsKzOATmfZH4BYK2xaM8R0XelHtYL9oUOflQCeKpMY_lg_nVj0VlDYSmMidEc6Lo_Iq8NM5vCg4x5hxGp3IsobQWZRn5ZXeXDeGahYk69TNCZNgdIS0S4klDvXJ8N44C_xE2P2L59IytJAUaDlPMpBVOlbBqxacsU1fjmTRqWHKAOCYB7NHC1H6_202SddT6ZPM9J87UhvFAUdWzs4PF04CezKgiarbKSDH8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
👤
پیروز قربانی سرمربی‌سابق تیم فجرسپاسی باعقد قراردادی دو ساله سالانه به ارزش 60 میلیارد تومان بعنوان سرمربی جدید آلومینیوم انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26470" target="_blank">📅 12:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26469">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o4IfH4B0_c80cFx7uudhbLhs8zQe77u28hIRCeI8PwlQir2uZoYbgSxRIs-NtoRvGgiHJa8QDSc79R7WXJ5RdqX7okrJQKICbC0AoiRI8uUaQgPX5zup5KQZgFhAa2a-haINi94yQcoUfU9WW3caCdbB86x0zqmbpGNVnkbFym984Ju5zJCkdaFM_oxZt-S3FnX3JvNkApq4Q4sJt3Y8qAyjlr24SBs7x9-VmRsfEiVi7rkN1BTJZ1HwvHtVsqRA95X5f8uJFpiZogbDp82DmxbYR10mnvPvI-OvbyfvsAPkBRL7Uvh_aPLWihMk2dj70SGJuaM-oYlpPJb24NxhHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ بعد از عدم موافقت باشگاه تراکتور با پرداخت مبلغ رضایت نامه سنگین‌محمدمهدی محبی؛ مدیران باشگاه پرسپولیس ازشب‌گذشته بامدیربرنامه‌های محبی تماس گرفته‌اند و پشنهاد مالی خود را برای 3 فصل حضور در باشگاه پرسپولیس داده اند. مدیر عامل باشگاه…</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26469" target="_blank">📅 12:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26468">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQCJuzzNwjyX6PKPxAv8NMulKRqBqvDcraxK6bu7jAz-8kQ_QXlK3RoJ1g_UKBfx7NMXW2GBeLkPlXhCaLYc7nWwMYG28k1qDFIHI6Ckw9cIJiXRAqWAmAIYkqcDut5a5sUiJ4ATOwdE3_Qz7LoNnEdMx_cV0ny3_pwb7JB2FWT01pQ1xYED10qGtlD-OfYqzpdKzGxE_uRbP89MGXcV48mEk6JF18N4Wa6Has8M6if_OtAjj-CzhKy31RXBDcHzz7rYxZcnyMcP8TlLkBR3GVcRl95UbzBzn3CEB95zzDuEA3sooj0MbISquqRvjg_ulonjchR8H2TzgB6Ajq59Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ دلیل اینکه باشگاه تراکتور هنوز از محمد مهدی محبی رونمایی نکرده رضایت نامه 1.2 میلیون‌دلاری‌اوست‌که اتحاد کلبایی‌ها تعیین کرده‌اند. تراکتوری‌هادر حال مذاکره هستن تا رقم رو کم کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26468" target="_blank">📅 12:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26467">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kf3YsaHfPC0iLxNJIgFjlzN_SIDAr-lCMTHmCtUOEI3UoM0ePetvZZvrz_I6ISspVtG95sjHycoXFTrD3p4ZAdvG_WYJ3r5raccYoh8jwcfgkN2lXLRXnfPZ2Tj8hBtuPL6fn3g3e1oH-Tb5Ic2n2jHH-9Wk_ut7nll6AjV2GfXPHUASIhSWMHBuH6Z2JSHtawxyUHaeWFajLMlzhTcN5RxSBV8Obw14Qh4QHCzfGhBuIT-RwApP2fTIKOCgEo1rQfyIf-zOkJWS5TI80vW41o8rQUMgTNKiU4lvfy5B70lplcTTTGguNdK-NDauCkmWG9dpYbq2FueGqVNXK7SlKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛ با جذب مجتبی فخریان سیدمهدی رحمتی موافقت خود را با فروش پوریا لطیفی فر به پرسپولیس با رقم 600 هزار دلار به‌مدیران تیم گل گهر سیرجان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26467" target="_blank">📅 12:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26466">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RcgomeQBYK_FCaabj6lMwUbek8gLtG3hidlEIxifZ0K2511u-tJMFGp0j7PXtId8Ef2YXCNZaEMRNaUVlMeMYYOSj8zjuJeh-8yKUarQfImcn2zE1RolD0efj0MI_fMZ40g5Nn7zyIuzIgj_AgOtZ_PSnQleBuWQrgPBbuVGjC9EFXogXEU3X_lzE_LS7VChZbI_lRE0IVFaX4yXwpdxNrjUHeN5e8eFu_5QtLqWKlsUR1RnZtGwofm3TTw693wVXms9rwXLU0nCvf3QfK1Tohn3SUWXvVuHEYvNTrQAIAcfktnRy6Y2X3jQiy77jNIUExHxrh4AvhsG_gBwxfFVfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛باشگاه استقلال باردیگر به منیر الحدادی فوق‌ستاره سابق خود تماس گرفته و به او اطمینان خاطر داده که بهترین شرایط برای او و خانواده‌اش در تهران فراهم خواهند کرد و هیچ مشکلی برای او خانواده اش پیش نخواهد آمد‌. بایستی صبر کرد و دید منیر…</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26466" target="_blank">📅 12:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26465">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uqj4mNq0MbFYCukI14OCdCFuet4Aoz5jcVnfdrDxSl-nwiRR8MimNprVp1MWhAfGJIGMknfzUcpjcWEL8eS3rZccHUBsqih4OWpbYlshqwXJ332B-TamsWsmbxSmNhz0FfK_DNyEHvGVR7dMzCSP0Xk_PLuvf_Lt-N0S5pRzQS1mq0Hp5gKDgpAlI-m3JiOSUk2BQtOyWepwzovCoJR5BeJbB0r0GY0p-CiJNmzqCee_ZW6TGFevd9YXFscH9VZSqUkmHPl_AKV4xTDgtjWpgOP5tX9aiO9KfW04PB_gtJlcCJ_JsaogEzaCfX_Ud1WELHH1xQyM9KlBUc3bYyfL2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو برای چهارمین سال متوالی پردرآمدترین ورزشکار سال 2026 معرفی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26465" target="_blank">📅 12:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26464">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/596bd2f9a8.mp4?token=MJeCTwD49Ixu3QHBStvnQCtQWTsStLRnPcjayoFHlmpjKAYnuUWKzIeGjIgp11XJEZiR83ZaA_r8dUe5BEhGJHOI0g90O81h1cdaIa576VuaUfheNHdqx9RUPOs1HbR7o9gWwvhcn8mZZu6hoVfBjUucleLhBYxAHr4GXqZ6Uc2cWErM4u9ALIMDY0D7Br3aiKnNB9px0ymz5RDhWhzitcSqPPh8fhaj9qhlq3V8KPFfw7T_g-uQNuabYFeZTyoRAZZoxDpFPn6teqCmmlxBn2anrC_utJSUmCdLu-omu9ak90GYxMzhVKqm4TcvUy6JBYcpTjTFM_YG5uZ6KS0tYhC3tUlwH-_TyzpeyM0bnV6fRW0oR4opuR-NrAiLjz1YsYRKWJ_bfp6QAmLW_nJy5SEscyHmwAl93eF32S7EtdWnnF7l4BSilBtVkPZMML03zrL3nL23rtXhFVXtmrAPzbIJCgzQRmcEkMMlEh9ber4iVqM2MVL3hlOkUV4Jc7W9if7fyfdjEUeUHRAAH81e1qqkb5p5lFo42F70HlboHjAO-BEP8asUWMEMX68U_YAQf4GMz_IiwU9ymPkkHjlcetWRJoQi9a25a7cKK8cBq1JlgCSee5JWOqV_D0aHOIu9U82ebjOV5pZjEQqPxNOCg65n_WsYzYzZkNT608f3PTo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/596bd2f9a8.mp4?token=MJeCTwD49Ixu3QHBStvnQCtQWTsStLRnPcjayoFHlmpjKAYnuUWKzIeGjIgp11XJEZiR83ZaA_r8dUe5BEhGJHOI0g90O81h1cdaIa576VuaUfheNHdqx9RUPOs1HbR7o9gWwvhcn8mZZu6hoVfBjUucleLhBYxAHr4GXqZ6Uc2cWErM4u9ALIMDY0D7Br3aiKnNB9px0ymz5RDhWhzitcSqPPh8fhaj9qhlq3V8KPFfw7T_g-uQNuabYFeZTyoRAZZoxDpFPn6teqCmmlxBn2anrC_utJSUmCdLu-omu9ak90GYxMzhVKqm4TcvUy6JBYcpTjTFM_YG5uZ6KS0tYhC3tUlwH-_TyzpeyM0bnV6fRW0oR4opuR-NrAiLjz1YsYRKWJ_bfp6QAmLW_nJy5SEscyHmwAl93eF32S7EtdWnnF7l4BSilBtVkPZMML03zrL3nL23rtXhFVXtmrAPzbIJCgzQRmcEkMMlEh9ber4iVqM2MVL3hlOkUV4Jc7W9if7fyfdjEUeUHRAAH81e1qqkb5p5lFo42F70HlboHjAO-BEP8asUWMEMX68U_YAQf4GMz_IiwU9ymPkkHjlcetWRJoQi9a25a7cKK8cBq1JlgCSee5JWOqV_D0aHOIu9U82ebjOV5pZjEQqPxNOCg65n_WsYzYzZkNT608f3PTo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🇩🇪
یورگن کلوپ بایک‌شرط‌هدایت تیم ملی آلمان راپذیرفت؛ احترام به حریم خانواده‌اش. او تأکید کرد اگر این مرز رعایت نشود، بدون درخواست غرامت یا حق فسخ، تیم را ترک خواهد کرد و این مأموریت را آخرین چالش بزرگ دوران مربیگری‌اش می‌داند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26464" target="_blank">📅 11:46 · 03 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
