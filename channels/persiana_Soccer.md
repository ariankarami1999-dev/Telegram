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
<img src="https://cdn4.telesco.pe/file/EU5c2yAGjUBlWox8KcvH719BvL-vjFYZQNAhIakn7AAq5HIIESIQ14X3JtrDHabn5MUrZmFP2Ih4jn_OnIUWroAlIA944hM19StBUUC16xcCq83NS9uz3_WV7XJyu-h6_4-I_OSZe1kr0f1H807Rfvo0kyDYGkK_RGEjYDBX14Jj2BM2P1x2dL67EIvzeTQGkeQ-_8ecNBSsISO0HWR3fWAygNbUzppnlKHMqwgKUqihvNsxLUrTeVJwMSyt-mecCY-BsVXdRO9BILqPmEfiGeTvbJSoq5LI_EACeEbdwrCESit2_AUK8B7k05npJKTkPvigpGnytCF7AWsyBdbpGw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 323K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 14:39:06</div>
<hr>

<div class="tg-post" id="msg-24459">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aVr-5_FidoL4XTdfSURIEHAXtTbSbYGj8vYv6t_GoZp_7gMwTQJXVYiPSxEZcbrq-jbhENGZIy5hf8G20fG0gPC2KcwcVDcdMMErpgeBkLvAZkIFJMRZCaC8noID7lGl4F2Bplws1M2Suq4w-WpBbrLKKQ2k2eePiAEsB4KrYIdSkMJp7mgDIk5t6WHg-3VM5yH3-0ekTfmH9o_W081bKKjVoaJR2yb6bf_hRgUnkOm8V2PpEEoSQsDoXtf0p4VvBaKEh--QUJ7Gf4jkpWB0_3GEOr6eADylQDzJaUFAYLkq7mrFFAoJOnPf7OXkl5Fp6o1p6Pr_A4G6lHqnf2833g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کارلوس‌ کیروش سرمربی تیم‌ملی غنا در گفتگو با اسکای: امیدواریم بتونیم از کرواسی امتیاز بگیریم تا تیم ایران به دور بعدی جام جهانی راه پیدا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/persiana_Soccer/24459" target="_blank">📅 14:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24458">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l41HJhKF6LnPSmcNwFJ0-rOUKYZeABfHDFoJU0PB_j7rtVEV3v0LOsO4i8QKgXh7w1UEf7iMsh0dkvRU-xxkT8roY7kNQTMtRCOji51F6qpPXjz8b2-5cjI4Q3whTGaaGnRIc0uq15nzmwTj4Feh64ALoDvwIjNMngYBL46X68FhbhanNC7A__jMMxwlFOPJJTzMaphNBv2MzTWOM1MreHMSk5j7vWLBWUfv5qAmq2j07rho0EsH29QIRpXCn3f_QvTaPSjFeiWenM9sc6v8yynv1FxrcYzzXMqUZwPhF3WUipJEx9q6hTVY1Q-1lh0yKi5Gm_pDs9iRCyQrVqZy_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برونا مندونسا مدل ترنس اعلام‌کرده که تقریباً دو سال رابطه پنهانی با یک بازیکن سابق تیم ملی برزیل داشته و اون‌هم برای رازداری 100 هزار دلار دریافت کرده که البته گفته بدلیل علاقه‌مم بوده این رازداری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/24458" target="_blank">📅 14:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24457">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/143e37e8ab.mp4?token=OA57Uhpisx01uSO72TmgsneCyVYAk-qWiXtXkBNvmlAQKyO6nbAdrJgEnOCuhgvalmIW_bNPT6AAh9vIFmsFOpFYrVMpGRMriJBpVx2FRMQ8U8MLNTDf5BG6YNbALDAUbZEPNlOBWeB5JPWOpCPqE6FeN7K3-RUFDe8VcqIhP5C_f3hunCsxTbtlOeQ3ksxSCAYeFQ_4qqhl4PUygjr_hpyUAoYl7-jZeSYu9MZYn1d2QdD8nTdHnVYEOG-A-1FskzZlhAE5CXONEmsXb_PydVEWJPdzD4pVpEJGVX3xlXEBnTqw98iL33B1O5WYbwvxX8nfY5RRp3vnTz9feggOJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/143e37e8ab.mp4?token=OA57Uhpisx01uSO72TmgsneCyVYAk-qWiXtXkBNvmlAQKyO6nbAdrJgEnOCuhgvalmIW_bNPT6AAh9vIFmsFOpFYrVMpGRMriJBpVx2FRMQ8U8MLNTDf5BG6YNbALDAUbZEPNlOBWeB5JPWOpCPqE6FeN7K3-RUFDe8VcqIhP5C_f3hunCsxTbtlOeQ3ksxSCAYeFQ_4qqhl4PUygjr_hpyUAoYl7-jZeSYu9MZYn1d2QdD8nTdHnVYEOG-A-1FskzZlhAE5CXONEmsXb_PydVEWJPdzD4pVpEJGVX3xlXEBnTqw98iL33B1O5WYbwvxX8nfY5RRp3vnTz9feggOJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شمامصاحبه امیر قلعه‌نویی درپایان بازی امروز با مصر رو ببینید؛ از اول‌تاآخر این مصاحبه سم خالصه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/persiana_Soccer/24457" target="_blank">📅 13:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24456">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVsEgcskMcZjVj4q8HerJRkiras4qcDmPj9NS5Wuxl4XtF1ntM7LskFvl7VzCoGnLm9OyPyl85igB6qjwfWfgxnSOCdIDz9d1wK7NDMVi5zZdGDq-B99lTGA3UXcBadsSbjnyMEm1xqudoLOV9UvSE4NxyNp02ZGWPqHYQ3lny7UmvWcFpSPGYZ6DlCkxK7cpY9tKbPQ-3IkJ9Z482kenuXrfK1XMRlDsM-q2ZdDij0asSKIy51v-cGtg4P7Ihf5oZnieZzKAKmWDhNbwCOSGiBZt5_Xd2xP8ouToYQwM86PSpAKJ2B31mi8VeLIiPFfcuTQw6WfaWe0W01fmzGPtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
#فکت؛ رامین رضاییان36ساله 2 گل در جام جهانی 2026؛ کل اسکواد بارسلونا روی هم 1 گل در جام جهانی 2026؛ تا فکت های بعدی بدرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/persiana_Soccer/24456" target="_blank">📅 13:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24455">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SUtu09Gcvr-XXvECxIY5S-qu9iT-cCQwvpzNAmeLaCyn1y5FsZJ5WXIM_EyX92xNh74cInSG8U4MhP41miiCvC54OnXLKbNim1mlJxX-Hdb97qqqmperGF7lPgZv3p5QYWhDJj7nQwUzNotz8DYdM815KAW3mAWZaq75rgu-uYgr90r8cy4Vq31XLb9uzr8JC9Hbvkv_EVJxR-Y2Ocyv3IWvSAS5k_zOjNSz1E70T5VBv9ipDmnbfe-SMixOF2TEp1JFt7JzYn8_cOGMBRthARYfSph3NNNWp4rvJcT7p9KwhQq-cVdi_RrM8sYzkDZKIf2Dff_u9m6_uYEAGMNH_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌گروه‌G‌جام‌جهانی 2026 بعدِ پایان مرحله گروهی؛ ایران در صورت صعود به‌عنوان تیم سوم به صورت قطعی به مصاف سوئیس خواهد رفت.
‼️
تنها درصورتیکه اتفاقات زیر بصورت همزمان در بازی‌های فردا رخ‌دهد ایران به‌عنوان تیم سوم صعود نخواهد کرد: تساوی دو تیم غنا و کرواسی،…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/persiana_Soccer/24455" target="_blank">📅 13:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24454">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qR9mMzi5qSaLMF9PdUiTmG2xTlr02eF5B7kbAd7v_XtQQDGFCtYlRd2EPz_KKSj9cC2oZZth7PnxvbVpQmq6hE5I9bifZCDPEQIbhuAxvgC5OKsVAaDQS-pPmuwjPZux_rc8NR1sxMwvLVzxteuKtCUlfLrRnRuef-l4xOM0ScSoWRx9Xvfb7P3WXjX0Eu3baH4x7nJYF_-OzogmCbCbgZ47oPmOlAJqNIOvIJ0bHaCNKBmBMudIL-LDLWALk0TjHoG4wakxxw_Ehf27x962ImXTqpmzPnZFZ-lL2kKHvnebMOOaNgElLVmRChhoDLU2e36msKycDuoLkugad64REg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/persiana_Soccer/24454" target="_blank">📅 12:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24453">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_GciaDBWBF8yKnGLqJ0LEDxlHCMu228rqShXe6QDcvos5CIXZEzHnIPhaVdoxk5v3DywkYpEqPXZGq_2QXWHSzBsZWdjL6u0v2Ie4EcGH1gJGOl2vYWQ0OspvGEPJvOUdt5MMLToQPGl5FGB5U3Yq0otx2sA_3cdZu95h6tRk4E7jhAJEJ3s3PRcVI8xdNDayBQwhV6Yjcbmp-Ad6bR45kpCN1t1gOd5zYh3cdwKUETqQ83t85dR1KyEgR9-uJEfwjA36u1IWMtr-sBn5TVIaqUmy1GJONHQVBf1-_sY_MJ3ViuV38_-UfILweKAiFg5psaDdvskhB-dJGXbPVfLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛ ابوالفضل رزاق‌پور مدافع چپ 27 ساله فولاد خوزستان درآستانه‌جدایی از این تیم قرار گرفته است. همانطور که پیش‌تر نیز خبر دادیم رزاق پور مدنظر باشگاه پرسپولیس قرار گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/persiana_Soccer/24453" target="_blank">📅 12:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24452">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cvd_VYhXptc6rOMRBFaERu_fG2iTvM7R1mFSGNDrt1ttj7yGai7mPoS62P6k2qz1swxBUPTkiCVvoSiUeE7nZe1StlK_b-JMJH0aNbLhcLm0PnDJQZDiVEYl2ToR5BZSw6dQUd9p275fTlT6w8snfz1E9a4008s0Y9j8dI9C87xdrRZRg9oboTgn5XJx8seVjFvEeqlMH93Ugsk5TeRjzf8qyq46fvWvXVA7fLXDTkXjczz9rC54maXVc0r_AVWQzmzbGR__ThNa01EDBibsHZb79H_LpQBZCLzxqqj3RP0XMqJPWyT_GVFyRU5ZpWg0-Vi7Hatr_cQYoI8hXNr8_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عذرخواهی رامین‌رضاییان ستاره استقلال از مردم ایران بعدازتوقف‌مقابل مصر: شرمندتون شدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/persiana_Soccer/24452" target="_blank">📅 12:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24450">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V12f2BdpS4D4FkCGuYkAIfXHRJC9WUdjZKHfM1OjuenfhIFNf72freQns5J31A53MrKpTLr8ZIMH8aUEsy6nqH8uBLLNsOPAVOPPpOuCGrRYuP2ik9622Xv6rrOMH2Ei4c2KwKAEjpCIWHN6WWVub7zAPGmChcUQZ3XzUFvTDENKFcyrPlM1BIEIxrnRXc0mbrDuhTnDIqYpCrxIJl19tKVATRLzNyxsjO1ZLsfdw5yoYGflEAeMqmuzSTayNpJZKfPfoWBFtoZS6V_jkld-x8nbRXOm_t4wKaRNZSJeiw9_bv8pgtTb8NFLSeqbT9DTepXb1s2pB-s5HeMMcrGlEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/thm8BtiyZ1Ud2gxucbnx8coPNxl9DLJlv_zKnLd7KWu-F8k0UWH1ngBm5uVf3wdWg2_eB1EEs7aAjZz7mJ8QzxDwQLFX4rpw6UrpDptLAAedmeuJdefVenTYEa1XtFze-OIUR12Ax__vM1FmclB0vd8v7DU7KlVWhYcC-T9_AJ86nWg2kXzlQRhUqRukh9HNjr9MVSTbSSye04VRnl9tMyOFGXKgrzca2kUI6fgv_GT6X3C2kRJFzKfXjN76uU2DCKgkurQ20WAdrGHES03rMNbpNWIbu-HhnYmaOevWKmiMMu7aQLyxKlyslr8VhGcenckFefHpwXmYJL351pg4gw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
پارتنر برخی‌ازبازیکنان‌تیم‌ملی‌برزیل؛ جالبه بدونید کارولین لیما با نیمار جورنیور و ادر میلیتائو هم بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/24450" target="_blank">📅 11:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24449">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B41mGB3Kc_RcDu0b0y8ujwIPdm-uIperSWRGY6pWXc7eY7nWQZTvVMfKibLCg6hxJEhwN_AUT4CsQkOBbtccnxeMdYStcn1xs1fr9Ux1A8BVD0hY-Meaa0e6RgChhc342I8uEVEuL1_leirTUINCL6RMdEAmD6AHGwLQ9HiQcEWEOc8C3woT65tMYGuvKBkiwOiREdIrTvQgsxpONY0a687E-kSfSHEDyVwqgS64S1IA3J9t1uinBFg6pRTNKXUKk4eCpr2sihO_OTx79rX_3q4fk73VHBUYTnOLJhjWTk3rsafbPLCTVeFHsRKgQI6coZoAdD-TI_q9WP90mLljxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی رسانه پرشیانا؛ با اعلام پیمان حدادی مدیرعامل باشگاه پرسپولیس اوسمار ویرا رسما از جمع سرخپوشان پایتخت جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/24449" target="_blank">📅 11:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24448">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-gP1YFiFvj0wgAFEXw0aZJNuKCE7hRE-JjTxd0vffue5qz7pqVuf54TzuOiBKoE4p9FBdhAv7aXyCXrIqSou38s5a3hz7KK1jDr5RCtPTIFC4_FlB0fXSHy7gOsS9WIInzugpbc5yA0eoO1L7EIYCedCeuOWrnixDbPCP3KvF524x0rIMyaurcdpzbZk8z12ONbL0q4UAmxxgEkVB1VwzQDk8lDkIE2VUTAVbrwEIDurUUp7wpgqY0nLoX2A4Zy1GjR9vjfhzGbl7Q1KX6lhJCtVLrXO_Z3EAMx45zF8-iUwQU9yTXkb_Jd2XEA95BNX_ncnFLLIkbU63D9HykhEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔵
#تکمیلی؛یوسف مزرعه ستاره‌جوان فولاد به مدیران این تیم اعلام‌کرده که از استقلال آفر رسمی دریافت‌کرده و نمیخواد این‌فرصت‌رو از دست بده و ازباشگاه‌خواسته با فروش او به آبی‌ها موافقت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/24448" target="_blank">📅 10:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24447">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7be445df5c.mp4?token=ruXP6QwfzosqaBYtY1LCeP3wGc9m0qkkffoMYEDmZmKIR-M1GWghX31UkRbCgn_OmKEPtMkqbMaewIg80iZy0ICcSGawkEVEpwzvu5zN4SfRNhip9n6CBxZyg3WD_8itMAWesF1NSu6-UZd6D7MuNF-eWAE41VQ_frwtCZGpkNtESseY7ySkupJO2PB1gsq4BK0Y9LhF74eW06ThfDGb4TuUNMBQvklK2Swu6ivTuLDYI4HJm_B7PIVLfWF_caqT0Du-U4T3km3mcIZlyICFWzewSVg3G-yqn44ofskGcJuBPOyghGXLgDD5__FtIjXQHIeSivW3twGln1FDE9Jo-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7be445df5c.mp4?token=ruXP6QwfzosqaBYtY1LCeP3wGc9m0qkkffoMYEDmZmKIR-M1GWghX31UkRbCgn_OmKEPtMkqbMaewIg80iZy0ICcSGawkEVEpwzvu5zN4SfRNhip9n6CBxZyg3WD_8itMAWesF1NSu6-UZd6D7MuNF-eWAE41VQ_frwtCZGpkNtESseY7ySkupJO2PB1gsq4BK0Y9LhF74eW06ThfDGb4TuUNMBQvklK2Swu6ivTuLDYI4HJm_B7PIVLfWF_caqT0Du-U4T3km3mcIZlyICFWzewSVg3G-yqn44ofskGcJuBPOyghGXLgDD5__FtIjXQHIeSivW3twGln1FDE9Jo-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دعوای جوادخیابانی‌ و پژمان‌راهبر در ویژه برنامه زنده جام جهانی؛ حالا شماها دعواتون رو بکنید ما که میدونیم همش فیلمه که برنامتون بیشتر دیده بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/24447" target="_blank">📅 10:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24446">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12ddb69797.mp4?token=E6K0i-nAfZFlhw5NtmrJMa4DO8u5FkkfMsD24r4IDyN3xGgkyp3g2YuyceVCVSGYAht9Icek2HZA0k16ubOk8EAba2ny05L3jaoh1E68Zoo_CwEvpcv5_AVGx20gC8wH_GQE44hF2eOqVjensenRVkbDh-C8ljsCn0LR4c7B1vpvCnZCGPj8Oqd4it-Rli8Bjas4TcAN6ox8y-2wM53RYiyQsE3SDuOv68m9efn9mdVG54GDOIWNBnlZKrJw_ZwbdXvzcCW44tG6OuJwmK0pv1Kp37SFiMGjQ8FMkdJnefJWGflN_dTvkIJEyDthmxkMcKXikf0ql9Z0Mb8uzXh8aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12ddb69797.mp4?token=E6K0i-nAfZFlhw5NtmrJMa4DO8u5FkkfMsD24r4IDyN3xGgkyp3g2YuyceVCVSGYAht9Icek2HZA0k16ubOk8EAba2ny05L3jaoh1E68Zoo_CwEvpcv5_AVGx20gC8wH_GQE44hF2eOqVjensenRVkbDh-C8ljsCn0LR4c7B1vpvCnZCGPj8Oqd4it-Rli8Bjas4TcAN6ox8y-2wM53RYiyQsE3SDuOv68m9efn9mdVG54GDOIWNBnlZKrJw_ZwbdXvzcCW44tG6OuJwmK0pv1Kp37SFiMGjQ8FMkdJnefJWGflN_dTvkIJEyDthmxkMcKXikf0ql9Z0Mb8uzXh8aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
رامین رضاییان بعنوان‌بهترین‌بازیکن دیدار امروز ایران - مصر انتخاب شد؛ رامین رضاییان نه‌تنها اولین فوتبالیست ایرانی‌ست که در دو جام جهانی گل زده، اولین سه‌گلهٔ ایران در تاریخ جام‌های جهانی‌ست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/24446" target="_blank">📅 10:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24445">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cQpxDpGbqnlgkK3Rbxj2Q9dBwnOsoE3-D5JGXFygACicpziCHJ-9N2s6AsKZfEHsOCODzhh0RVdlEO4dplF9x1BSuauqIwBueXVpsyggjdBMjubB3JTeF351mQRuz5HM50t3ZOCEFxT73z2mQZJK-nHIAdnh70FcvP19POxMBD2SgQ-p6EXpyz91VutIb28UxpjJH5feoYsmSvJmz4UlBZEByfe_S0peqfNc93oVtjRrwCd8goYG9-MJq0nYlGluTZwjPEoxG0M2cev6QpcxvG5crMvFPG9yloMrFgvYoqDrCGdQ2WpcnqRjBzdLgNBLQpKvCgnI2fSiN4FYD94bDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
55 درصد از علاقه‌مندان به فوتبال، فقط 4 سال یکبار شرط میبندن!
حالا چرا جام جهانی
❓
خیلی از نتایج تابلو و قابل حدسه
💯
مافیا که کارش دستکاری کردن نتایجه، زورش به جام‌جهانی نمیرسه و نتایج واقعیه
👀
به دلیل تعداد زیاد بازی ها، دستت بازه و کنترل ریسک و سرمایه آسونه!
🔽
🔼
💡
کافیه یه سایت معتبر پیدا کنی که شارژ کردنش آسون باشه و بدونی پولت امن میمونه، MelBet اسپانسر رسمی جام جهانی، همونیه که دنبالشی!
برای ورود بسایت فیلترشکن خود را خاموش کنید
.
🌐
Link
🔜
MelBet1.net
🌐
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/24445" target="_blank">📅 10:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24444">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_V3YceXbGAM0v0aXqm1KzXLZwW-S7oYD9algK7P6KH79pPTZwBWpF_RLRDFB_kBxuBz33ah7HdogZDBAcDGTsNbI-nnwGFekZQUBfyYzYcOsbdIGJDf0WZP59eibyu0UDMq01bHf2IKwme7vkE7J7u0GSBASKb7mw5_dTlcoR9xV78t-uo4s8NY4-zardFC6AEkt7OUsQqD9EJZwGcG8EixsfIoLMcYNxiR8VhHlpsPW253655gNv7NKUf-h1rEYc9THBOCdW68YA0K_ZuNXHHWguCWOdcVmmwuRKKJY4_i06Wvpv-GF3-uPKVukumNpDroWxvoaGZk9Jiyhsrt_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌گروه‌G‌جام‌جهانی 2026 بعدِ پایان مرحله گروهی؛ ایران در صورت صعود به‌عنوان تیم سوم به صورت قطعی به مصاف سوئیس خواهد رفت.
‼️
تنها درصورتیکه اتفاقات زیر بصورت همزمان در بازی‌های فردا رخ‌دهد ایران به‌عنوان تیم سوم صعود نخواهد کرد: تساوی دو تیم غنا و کرواسی،…</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/24444" target="_blank">📅 10:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24443">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWCPrDrMzlnNd1J7RXDliW_M7dZik636rgxceQ4-6oIipsIHY_mce3g_xYAdiCpb5oN03FmXFAzGSyG_b1smCSSi-Qa42Z2AHCnbv8_kMd0k5q1UvBEpOKlgMxTJaZEdvV3sxM1GH3-huC_SqjXe74pqEs2_J6jx1rxq2zffONTZrKsxSwPOpxU8mFzMweHpa_ETUYTpQds0VCIbNh0pepE0wFRbztzQ6W53rdIHDKwiXmsxNAtLvHroG3i3jCiiCKsqFgbvpu1E8gvsuw7gWsOxdtq3hb8u9-gFvndLb_WMm3qqInps4nRpd_rtqRa4twijk-LMBB51-wbfImgwpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ همان طور که سه روز پیش خبر دادیم؛ دراگان اسکوچیج سرمربی‌فصل آینده باشگاه پرسپولیس خواهد بود و به زودی برای انجام مراسم رونمایی به تهران‌خواهدآمد. اسکوچیچ پیش قرارداد داخلی خود را با سرخپوشان پایتخت امضا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/24443" target="_blank">📅 09:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24442">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5167ec966.mp4?token=U6z5saCjFHR6glbEuXFmN_o4hi_PjqeDgSDdgQSHPW1lrx20LYoWOqqCWwzdcDQymL0yPjr5WW__Q_6reGHDouCkfZKSxna9cbaIQFRUHDQm9rEuUZFkGKdvwgi3F9xJI8AWSzUa9Z62Ot3vY9QxzxWfieSULoroKnd9TOLxwa5nlh9GJRtAva1KOH9tqhwHSj-f5UPLgbfdrj8F1vjy-GrdooSkhFWKIYcTyfk7-zhaUlTgBGXMNRJP_UOjhKMoC3_Gn7C5M_mP6jK6WkGCRP5ZFx7OQrwe9Wp2OnwGAySBXMxIdz7mo_DtBf40n0nQHYU87oPrwGnbkKUjSGCcVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5167ec966.mp4?token=U6z5saCjFHR6glbEuXFmN_o4hi_PjqeDgSDdgQSHPW1lrx20LYoWOqqCWwzdcDQymL0yPjr5WW__Q_6reGHDouCkfZKSxna9cbaIQFRUHDQm9rEuUZFkGKdvwgi3F9xJI8AWSzUa9Z62Ot3vY9QxzxWfieSULoroKnd9TOLxwa5nlh9GJRtAva1KOH9tqhwHSj-f5UPLgbfdrj8F1vjy-GrdooSkhFWKIYcTyfk7-zhaUlTgBGXMNRJP_UOjhKMoC3_Gn7C5M_mP6jK6WkGCRP5ZFx7OQrwe9Wp2OnwGAySBXMxIdz7mo_DtBf40n0nQHYU87oPrwGnbkKUjSGCcVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
امیر رولکس‌ازحرکت‌جدیدومخصوصش رونمایی کرد؛ اینبار دیگه فکر‌کنم گفت خودم که نمیفهمم چی میگم، اینام نمیفهمن ولش‌کنم بهتره، مسخرم نمیکنن. ضمن اینکه ژنرال درسه بازی‌جام‌جهانی روی نیمکت ایران شکست‌ناپذیرماند. رکوردی تاریخی برای او!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/24442" target="_blank">📅 09:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24441">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‼️
شمامصاحبه امیر قلعه‌نویی درپایان بازی امروز با مصر رو ببینید؛ از اول‌تاآخر این مصاحبه سم خالصه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/24441" target="_blank">📅 09:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24440">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdd214fefc.mp4?token=lY8rGEE9L2qi_MHPjvyj0GftcUSW2uuT7e6o2s1snz5AXrDVREyxYBK9cL-O4V-FmX7I-YNEOq1-dzFXrgAc99m6PzJJeX3QuM51Gj33L_O1ge0iTbETHrDenzd-uR5feB1h_26G2y3JRFgtTQ5d4GtB0b1FiGvTgZBPeMk8JF3sXzvS04Oqw92IDQBYTP73mJ1W_I8ylaS_YLIqqQlL_5cWXgzj9M-c3GjZic0_-okPVSk2D115K-XDe7Eb98RTMsdZCkcaYKE7E2MZ6-qYyinXm0jOKM3prIF0DrqhMwmtgEO0HB2vMTpojPaBQQKw-P79MCtLSSlQgyi2yybEFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdd214fefc.mp4?token=lY8rGEE9L2qi_MHPjvyj0GftcUSW2uuT7e6o2s1snz5AXrDVREyxYBK9cL-O4V-FmX7I-YNEOq1-dzFXrgAc99m6PzJJeX3QuM51Gj33L_O1ge0iTbETHrDenzd-uR5feB1h_26G2y3JRFgtTQ5d4GtB0b1FiGvTgZBPeMk8JF3sXzvS04Oqw92IDQBYTP73mJ1W_I8ylaS_YLIqqQlL_5cWXgzj9M-c3GjZic0_-okPVSk2D115K-XDe7Eb98RTMsdZCkcaYKE7E2MZ6-qYyinXm0jOKM3prIF0DrqhMwmtgEO0HB2vMTpojPaBQQKw-P79MCtLSSlQgyi2yybEFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
خلاصه دیدار امروز صبح ایران
🆚
مصر در هفته سوم رقابت‌های جام جهانی 2026؛ اگه یکی از اون سه حالت بالا رخ ندهد ایران صعود خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/24440" target="_blank">📅 09:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24439">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxXGRvLH8Snbgjd5mgOJVwonQH-f6_harj3PiecHDUsD9UjLLN5yThw3qkuTo9ZSYMKfma8tDPQOGM5YYMlMae4p92A-7mY2O1SSuOcPydKL0X-rl6K1zdM0yzZZY7aRSskwnTkOgNZ6KppQxqf46PuGVVD_4onzv6WHV-gu4Mp25RX6XoiNa4GDObUs258kDVsAP7AF0RXza55OfkNAIF8Ly8pzwrBRCmsngITqlAvE0VjmCF-YjwBrvsemM77cgejGvLZR7OUjMcufdbXhlsf8hw0InPWrvm8mRjsx1vyK1LR6L4fG4weVa2Fep6Ff4-lGC5ggoL7ZRn-8m8jSfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
خلاصه دیدار امروز صبح ایران
🆚
مصر در هفته سوم رقابت‌های جام جهانی 2026؛ اگه یکی از اون سه حالت بالا رخ ندهد ایران صعود خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/24439" target="_blank">📅 09:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24437">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">▶️
خلاصه دیدار امروز صبح ایران
🆚
مصر در هفته سوم رقابت‌های جام جهانی 2026؛ اگه یکی از اون سه حالت بالا رخ ندهد ایران صعود خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/24437" target="_blank">📅 08:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24436">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EXb_BbRGDBn4rTzXVb4XhwKGbe3TqhFfteOl781iitFy8lqLh6Mv06ezOu4KHFQ_tJdiF-1FlVVuwTTkd5MLAe-e9p8hOpOGgo_sNvwmfdirXuXF15t-toTQzG6N_obYkV25QrP4TrHI35Y4CYoaaCSQppkmRcrI2DEIvN55wMs0m-p7ZOzw_dasTcn7Df3sRcsXdgch6d_XIHb73wH12t_rLdUxp9m2CfZvbrqtD7F-gUD_JhdSCHPCNJSiQu3FLz6wzFtPgpNXwpm6f6seDf34CEeUaQY476T3jgCbaRL1iSXJ_ax19Jpp5wQzPw59DXDPF_NdkXi5nz-wY51sNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول برترین تیم‌های سوم جام جهانی؛ شاگردان امیر قلعه نویی در رتبه ششم قرار گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/24436" target="_blank">📅 08:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24435">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AJJH6goyXjy6R9jZ3yBDy_xo8msXxmaqdexRl7xg3rICQQnCDGiohZblZFIPeN6mYbZ10rqra9Sxrk7RobvZgKbxk4J0xJKg4SxMdy4d27tWTmjmp1Omvcsaf84Vtm5I12c0bJhq1qdlsZ611AShhk3iYIaLJ73q5TRBUfeuXrFbcRwjJntnR8FsGjIF3FynMqyaHOTj0FtDRjJfm7cLMcMONp5HwzreHUe596-YrzZMnjVpTCny1x2yYec-Rlv3bEjtbsMw8JiYrp-5UGVHMb8OXnV4x14Cs4jkWoHwiUPx8xH9LZFM0vMIeYgNvWicTXHe7hB3e7lsJXE7txuBlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هفته سوم جام جهانی 2026؛ مصر و بلژیک مقتدرانه راهی مرحله حذفی شدند. کار صعود ایران به مرحله بعدی به اما و اگر کشیده شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/24435" target="_blank">📅 08:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24433">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CzbT6Tk2ayTABkq_Wz2sGXnKdTdVY_87WOfL20Ojlqotz6Ar0oaVPqjuIdfNFXVnu6jDfMMkh8bXGTfun0_0xE1dDzq6i9OIDWoaitQWYN2yO7fg_sk06SeHoZ8bj2LSrqx9fJ27L0w1yGa4fVwhM4LK0clv36Fu2yETylR_p1WkdoozNLgOZOz7cQEzwfPSr-rEE4y9JirtMxMzS719Hju4z8L33sS3awE1QHLBvc3yxf8sILuH_S1Va9aMa5Okva-dQcbUUwxSJ_pnbsnSYSjqdCBMhS1FSMuEpeBCri02Rb3J42vxyO-aKW3U_y-vK4qVuORuiHBA0rVIC9D3Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DeElx7aN0rc5SloSe0hFJlGMVJuSTZmT59GoeUx6THAhJSY7BA_13RXwAi5glW5_YV-Dd-rKvf9xZGrwGcXe-LXofJkp62xtELnSl3L0VYIz2RiBbqPIluCByCwNy7EpWPp4d1DuaU9CSd1ILATJLAl5QyyfdJ7-bNlknMwKUsIMYS-e8zWO4NQVm3CPJ5tPcgu3VNxULHapNkGSeviJmbeUVul2SxB2I6NULIezzBPBZYPZU03PN8pxG4Orsw0kUcyk78q-XIn_2MzqEsjhP0DOsN-uIH24Dl2AqMA1oRjHKifvH6WiNP59ZPPVQo_oYJ0w8zvWFpaFY3pOaV2wAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
هفته‌سوم‌جام‌ جهانی2026؛شماتیک ترکیب دو تیم ایران
🆚
مصر؛ ساعت 06:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/24433" target="_blank">📅 08:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24429">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cwTVhMiKYofUrKnlTNb98vPqlSkxNDal1bvrw7u9AUsoWDAzd83MZMIw1VVApbSLyO-o9henudaRbXHeNN0CsYbXxbIpfQMPAALpk9gsCdsQXxc--upwP1ABMB5NL4vmNg7yYmuswFIOrHzK3m03MwmmMxudNYvHLwarwDVEfCopVYhPEZrnpjavLELW8uYDVEGGzkxfefdR-HaxJwd4_qhsV5xV0XdIgqxx0EIMVia_4VaTorvTDHV5lKp44d9L4mBmMa6wgFxKT4s7b3OdPyLxfJTarEs5PR_m7R2sFioyBmyM0ssYLdpeCqRGcNnUg0SFpZMBi9b66hiBU1s_-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدارها‌ی‌ امروز؛ از جدال حساس اسپانیا برابر شاگردان بیلسا تا تقابل ایران و مصر در سیاتل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24429" target="_blank">📅 05:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24428">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVjTH4lAS_MZm1ghiMkdw8DKjiWiJVXQ-RnAWYEZ3fn4D0O78WfFUhFHk4A-DEVua70gdD7La9hEhaRV8drZmHjN9U8FoU8zmg36dSL4ToAl6WmjrmSR-zoRFJbJxGUfwuR4SoHXiklBMDkrKOdknJDTJgProBS25jTpkgJV7vrTNH9ZuxZGO8qgyJiOX4LeWciYskw_fI3j_5pcBYENIwsNCGrUH2qnNDLj6rwG8u2WEfXyc7nSjYnvySAi_96KuUQsWh6vSWrdlRxQyjSru2ZqUUta-c3BZ0y5EhEhuYuimdy7xrQEfleFQyz7-x3LFrKdvkFx6dsF7Lo52dSlAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هفته‌سوم‌جام‌ جهانی2026؛شماتیک ترکیب دو تیم ایران
🆚
مصر؛ ساعت 06:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/24428" target="_blank">📅 05:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24426">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O1uJw8l4yODDIVpYehAUbLN1YWhVnj42aSVZLBIdsUkXqDzBLwMTOcxjTpTmfKM3Q3W4CL3Nv9iD1_0033dji1e2u3Y_Jh3K_G-X-YvpG3Njb4ryaGF6xIVyzkLgawNbic2c6YeuPg-nfLc3KLDMrUi2HFphWqg-8Ftc412BVrnrwrCQiLrHgL86gPab9zs2F1doRi1MkHrL7i3AeIlg7Uj1djesKydumdxJxAwjvoVk85wyP2Rt-47h9Zh4vgw2Be7Q1qu_-5MI4TvKj1Nvni9sB39Ny-QQ4P7-TvNkbHg0Zxf4U-ZJUlK982OdVivHqMjRiqO3uyKPQaYeirw1Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RelPq8vYmQ4NTzaQvBninuixSa0yX9VcNmpn_mxuQdMITFQa9n8oYhidNx_2xLIw02NPXjfEGlCVcvtFcveqLj1FUTyP83QoMiwZdNmWGUpTnbSCscySzEQthfCZ1XoSBz-mOL3NH82szLsf9cJv6I8458qKlr5QI8YmHuSpoXCTvnpqU-sP3ar2uH7P3JKYI5wL0p3B8g6yMRemMTCRJSwI2lAUUQtkcXG7Vja2CBI46KmZx2xe1GmwTb77AhM6jyxWWrisP4AT2y-WAbjXSedZYukJvMRPLPhQg5nFRgi9Op0dQhUxd36WMg9CVQbXW9ik0hZUYpR8yHZ0TLemoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
🇪🇬
عمر مرموش ستاره‌ تیم‌ملی مصر: ایران تیم خوبی داره بازی‌ های قبلیشون رو دیدیم اما ما اینجا هستیم که قاطعانه این‌بازیو ببریم و صدرنشین راهی مرحله بعد شویم. بنظرم بازی رو سه - هیچ میبریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/24426" target="_blank">📅 05:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24425">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W4HVPo3d4IfL61UK2ZeR1l6suOQfc3FVaJi56hjo4jEvDJ21ovvUuK-zpDKSUk69SOiUoHjgELHGzVxofax8L0qFK4jf03c8YPDQsLI_Z7ZZsbmbzNASSEQ4QObu67Zwm_RP2ouGLDyHhoUV7aeV2gfk-KWPrY27ew66_SPOpvrTsvA7cDE0ENPwmn0j0KEzQ4wH_BApNNM7jGV89ttphdHAcHJgKEKgALPWWcA96tsAGKolXNLstyXcW9n50fJjm7EFGSdjCGasnHmFRDJ1QWiCBS11kAGsoKYUUhZyKgt1zwm8ehzgK0BJUTiqXzIr_4MwJXXMWB6DQTapKtyVWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌‌های‌رسانه‌پرشیانا
؛ ابوالفضل جلالی از دو باشگاه اماراتی الشارجه و الوحده پیشنهاد دریافت کرده و درصورتی که مدیریت باشگاه استقلال برای تمدید قرارداد اقدام نکنند لژیونر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/24425" target="_blank">📅 04:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24424">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XEd8Ff4eC6XcCrFX1_oTzfdkdPSYvqpbA8kviTYfhLsrK5oGSXsIhPxfjbg_oEgzQ5r0wub1FpqwdY6ev6EXAH9GQC8UGVtaWyqNkTyQmf_mdV_Ubhh-jZyXA7com58ih-4QyP3N-hk2ZFt9jBddRKgUO3NP-DjDE5X_4ZH6QNe9JOdiSaUMrHJCKxcnUmh9T0N5DeqMLsPjpdW1i0vCYwTLbuwgbqcNHMoIfQFHq8SCZ55vSSKDNoclWh45Xjp6cFK6jMXOcoZIQIO_8djw7dCOJTN6v10j0JOjhVNozFjvkEyx0kGc2azRZFaX38sD18ALvALyTDh8IKxzmoMdkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تورنمنت‌آسیایی؛شکست‌عجیب‌سرخپوشان مقابل جوانان چادرملو؛ فرصت‌آسیایی‌شدن‌از دست رفت. از بین چادرملو و گل‌گهر یکی راهی سطح دو میشوند.
🔴
پرسپولییس
1️⃣
-
2️⃣
چادرملو اردکان
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/24424" target="_blank">📅 03:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24423">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e59cd1cdf5.mp4?token=L9b_biLFgo1tBln0nnlYA-jQYfMTiTfer1AS0W9tNgbR5q9jVIG3PNGsvYqhmPTeauAvKqFciw0aD7O2n_3tvJHLzFbr6w7tXwjMo2UIjGVl5HZhpIxCsOzk4Hyl0CEc66cIs094rvB_mFh488dCn4frCVW1BzjiUFGMh4RGY8h4GgFshySKoNXC1GU9IRrZqjau5S9PqDzVw98p3n3mDzWq_UcBrJ1gK0hWBxpZ2fBO8fwUIUr0WQKhOr3hPpsuAxW_GWigk-MMZxYxx6M7iKZpYgRl9eGfsMry2emLILkTTH2tTms98VVlcBGdxS4q46Irv8bMxh1QQQM7hZXj1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e59cd1cdf5.mp4?token=L9b_biLFgo1tBln0nnlYA-jQYfMTiTfer1AS0W9tNgbR5q9jVIG3PNGsvYqhmPTeauAvKqFciw0aD7O2n_3tvJHLzFbr6w7tXwjMo2UIjGVl5HZhpIxCsOzk4Hyl0CEc66cIs094rvB_mFh488dCn4frCVW1BzjiUFGMh4RGY8h4GgFshySKoNXC1GU9IRrZqjau5S9PqDzVw98p3n3mDzWq_UcBrJ1gK0hWBxpZ2fBO8fwUIUr0WQKhOr3hPpsuAxW_GWigk-MMZxYxx6M7iKZpYgRl9eGfsMry2emLILkTTH2tTms98VVlcBGdxS4q46Irv8bMxh1QQQM7hZXj1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
عارف غلامی بازیکن استقلال به این شکل جواب صحبت‌های مجری‌صداوسیما رو داد: آدم صندلی دزد از مفت بر هم مفت‌بر تره. اشاره به همون شعر شایع.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/24423" target="_blank">📅 03:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24422">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUNMOVAjKJFPpz9CLPzspDZE2TidhB729TLGLqwvsywXuRL0cjcsZ7ybOC7zp2M8W3Dkrp6CMDG9sjtwOBfg-jrqZWhdTX8rlCwjdNRsqZkkByK06bcMS3Q0HDXeeGWdSf-6WNjqO1wUkpjPDA9-E4276-ckSnjiVQKOrQ-EcIU3Q_FN9qoDD626prLxzEr00we2QeLEHAWYVcaDMInofkTCyjv368QImCj9QVhHaSUALwIfzyme-Rk-ySiSh8oUmKs5D0bGJl-ICsGxzJFF2HtKaZNtfoX0S92MR2bRbLoSsTxHLhFINVeug3okZY0kuVTayg1HXSUTbAS64qXG7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
ایران - مصر | نبرد صعود
دو تمدن بزرگ، دو تاریخ کهن، یک میدان سرنوشت‌ساز…
این فقط یک بازی فوتبال نیست؛ جنگی برای بقا، افتخار و رسیدن به مرحله بعد است.
ایران اگر این بازی را ببرد، صعودش قطعی می‌شود؛ یعنی ۹۰ دقیقه تا یک جشن بزرگ ملی
🇮🇷
🎁
شرط رایگان ورزشی
💰
۲۶ میلیون تومان بونوس
🌍
فعالیت در ۴۹ کشور
📡
رسانه بین‌المللی
📺
پخش زنده بدون سانسور بازی داخل کانال تلگرام
📅
ششم تیر
⏰
ساعت ۶:۳۰ صبح
⚽
ایران vs مصر
صبح زود بیدار می‌شیم، چون بعضی بازی‌ها ارزش نخوابیدن دارن.
ایران برای صعود، ایران برای افتخار، ایران برای تاریخ
❤️
🇮🇷
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/24422" target="_blank">📅 03:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24421">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IzjtjrlQmDnNjls3-e6K0oc8ViJwjouX-s333Yl_ClDjrICLDIP_UT3SW1JNGSKjlLY-0jz4_YKmvwBeTTZ5UF-rvN7XrHZVtO0NsOmJPjiMvvnGMfPzmOngLuayQPM7MCL8QLUm4Vbhknuwdj9HoXb61siGlbhy4mLDHpApOqub57I5WRdqTYMfGp_mvxVDVbOCBfNbi9zd04FQ_pUsazuN3-p3HmCtefWdyIUXPYpkF3lEVR0V3V3HAq82i-oR9CVOfYHOpsur8G1xzMKgFfAQmHuR5Gzco1zSXnM_hl7m-AoZB3WjNYYC44GvI1P3k7PyjBR-AvtMyU1_MJILMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
🇵🇹
تمام گل‌های لئو مسی و کریس رونالدو در تاریخ جام‌جهانی مقابل چه تیم‌هایی بوده؟!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/24421" target="_blank">📅 02:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24420">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ed505c820.mp4?token=ej3AHql7a4p7W8hrNJ1wxDrb1Genq5LRQjbWb7R-gcSv9wPkyBe4JOTd8K8jO2AfuVV0dte0EzTUM7fiOYewUBJcxbfi4VAUNKO6d0YAQ50bWkE-CqyUZACSHus_muMjsxLoRikTzUixecLqoUpqvur_FBChs7qko_fLvjjkmouRUXyq5GWJmICTjUqnced3veibETBLDnIEckoFqDZejozH4OLXhoaTbQuAYF9EjQDXBuI_OzpB_4sSX57CbmvCEBNh6e3af-56WRlfahvQ2cIp3kez4D0jRxy9ROxmT1WrgYhEdU8EWSfNNI6m957j7YK4mAQnnkoGT-CDa0Myog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ed505c820.mp4?token=ej3AHql7a4p7W8hrNJ1wxDrb1Genq5LRQjbWb7R-gcSv9wPkyBe4JOTd8K8jO2AfuVV0dte0EzTUM7fiOYewUBJcxbfi4VAUNKO6d0YAQ50bWkE-CqyUZACSHus_muMjsxLoRikTzUixecLqoUpqvur_FBChs7qko_fLvjjkmouRUXyq5GWJmICTjUqnced3veibETBLDnIEckoFqDZejozH4OLXhoaTbQuAYF9EjQDXBuI_OzpB_4sSX57CbmvCEBNh6e3af-56WRlfahvQ2cIp3kez4D0jRxy9ROxmT1WrgYhEdU8EWSfNNI6m957j7YK4mAQnnkoGT-CDa0Myog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
کیلیان امباپه به این شکل به مایکل اولیور داور بازی امشب با نروژ بازوبند کاپیتانیو میده که بره به شوامنی بده؛‌ الحق‌ که لقب دیکتاتورباپه برازنده‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/24420" target="_blank">📅 01:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24419">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VzomeDuZiv297ONE6q6-HsMqZ4Y3OdTItNwvt9wfNGRMW7Q3Q5vbrRV_QJlKFqH7zNyB4Xq6pcngLxNRCo2tqJ0sa7m3IhYfXCW4vjVK-bHVV6EOqqgY4CmQYBdYvcf1C-O-585VgsMw11mufv6R3pNRbWvquPyCNMfzlF9YPfVBcB-DfZcRMipqTqqZy1XFqAOT35ldan8rx-eghFJVnpMxksgVD0ZfwUXwZl1CVbSkxrDxjSj6iT5z6wF1Dla1CQjQtFf07bNDrg40Zg5NxhGfMegP6SQwDOdTBHstzwkWlnj_AhcqEEJot09UJGk6uQQ1OPuBqExG3UJSpsAitA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با برد پنج بر صفر سنگال مقابل عراق؛ حالا اگه بلژیک‌نیوزیلند رونبره‌ ایران برای‌صعود باید حتما مصر رو ببره وگرنه بعنوان تیم سومم صعود نمیکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/24419" target="_blank">📅 01:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24417">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1DnXo8_ROvbYaLUsrXO9HcFtFhyNJvFfYAip7TYj4ISG-_N6FdF1Mp3Mw-9yNr_7ThxX_9dPd2CvWEbP2eCiPGTAXCMdfOH8ORJCeEEEhwV2eZz2i9erkipxPoi-B_ia71zHJONZVEdJs_wZP6-s8b1VvLgCA4z9Ai0nab7SNtwRf7dkIC2YcAc0ZKNu6YSzTgjYowxNgOb8purfnvRjaKuYwbNPMivJQajBXaxX6LS4VT59mhhv_FV3pdZ-VXa9EakPIEG2iVzdGJZpt6nDVHPlqqRfICB7rx2HrgILjcku20lbRf-wF4RttTPTwaKYXpgB3V1Ava7qhiCfTd82g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدارها‌ی‌ امروز؛
از جدال حساس اسپانیا برابر شاگردان بیلسا تا تقابل ایران و مصر در سیاتل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/24417" target="_blank">📅 01:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24416">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SaimqWgzoEWszjoi3c83Wqk8Ai-8FculBEA60tzDEqS84tUS-xY6GV3u8TEcxF8UjURMeZ5su_1NoYRI2t8b7QxPSDoQnt7iXdAPr6RGvmP4QFLEkvOc3cE7o3WWuN2SHQTwj2o2LfRq6mWK8JLZEzTCaQq0IeWCJRf5kqzcixROadxJjGYcJC6wDZiHXSo49WE3b5HCGHV4sQua1qc2PzTkP0-xFmSi6lsnl3PqVyKcevrF-B5VKkj9fS_lZzpofM96SXNAT8yTNXLKR0WR581jnHMqeoGH_sz0Hee0v1BSQCyT0Tg3_WQz133P1ZIK71Hb3_J1Gpi_o1MMSi4ETg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌ دیدارهای‌‌‌‌دیروز؛
از شکست تحقیرآمیز عراق مقابل سنگال تا برد فرانسه برابر نروژ در غیاب هالند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/24416" target="_blank">📅 01:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24415">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DPldQeY7imV9BLF4qFclFd53CPbQFTmDWuJ3YLZpYi_CFoZji2U1G25w3_XO-qLh0N7WFL1-FAuQgpxy4DjCa9-scNNSdrZvwNJUftC4oq_ZNwNUc2TCi4CEMIBWUhPLPuYrLwdgfGTHFKmim76m_8jHHkGXWNs7TVFM-B2FT1l8t6Sn9R9CJU2kDvjptrXmDSqDcDzlPJAg7KYYkHz2ImYEWGDAayBTCws7vOmMYJcQgIHHOB-0TA6YBkOO82M08g1zmLmSHu-xRafsihiDWCvxPWjEdHDj-Ed-UrcQSLVT-XIdvh7U1FbkJ6mBOIcRtFC3pTg3OM2RScoiyX455g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هایلایتی از عملکرد فوق العاده ابراهیم بایش وینگر عراقی الریاض‌عربستان که تاسال 2026 با این باشگاه قرارداد داره اما‌باپرداخت 1.5 میلیون دلار درتابستان پیش‌رو بند فسخ قراردادش فعال خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/24415" target="_blank">📅 01:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24414">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🏆
هفته‌سوم جام‌ جهانی؛ فرانسه مقتدرانه صعود کرد و احتمالا در مرحله بعدی به مصاف سوئد میره. نروژی‌ها هم بعنوان‌تیم‌دوم به ساحل عاج میخوره. سنگال هم‌احتمالابعنوان تیم سوم راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/24414" target="_blank">📅 01:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24413">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3TtugJiI4DRn1b2w2vrTGqmHxAF3qA65CK9XGWKrWKqh-V28bcwsYKNmQ67uYBhSLi96aqcorUrX8VMfitkecUoRB0drR10_55HC9bmIkq79pGyXwDmNcl-N-J9pvjAXuc8q03YNwkLiIJ8z3QPZ4W9UfkMu-4VZKv_fyJJHV4P8K6FH2FeltBgPJ68eICg-0HkzgTtoG-O1QoVjPAomfdGqwDuxHBcbU2wwR9LU6E9jJ3ywLeFFtGou8R3ToaS8XMCtOTEaLXbWTCp-3C046RorLuZ3VNYEINkRNFnlWDYKmGlwdNJEO3_Z2ZL1tDIhRaC9LGI8CC2_iNhYMNDeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
علی‌تاجرنیا رئیس‌هیات‌مدیره آبی‌ها: وکلای ایتالیایی بهم قول دادند تاآخرهفته پنجره باز میشود. انشالله تو هفته آینده خبرهای خوبی خواهید شنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/24413" target="_blank">📅 01:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24412">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PDd1Y7vs8bTLfoO6MiUg_0iB8ywqJyj6k-p-as7GWN9yI_h84MFYzmY75CcISRgclAhcRXRsiT4rh2fUuOEQMdHtQ_410lqebZqUBtOilbXZKASJqEbyDS7VhVJc-LW_t04e1kL_w3ohGJMIr5BJPtqR-3l1xcfrPNrvguRhs7vrtz4DTJsN7_gtnpGUpHOIbPlWnzJRTHKCdTzhpJ09pLmIDbX-R71ofa4TP6ycWQaTd5f8WsZ7IIxawCuBVtlpzUBMSvoA3CBmeQCV5ZDcV6YgQHX8swGkthKU1wpSdjzYjUPvn2p61Z6BsTE55tk2IOnlFD8bj-G7BOP8rG9SQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله‌حذفی‌ رقابت‌های‌جام‌جهانی؛ داره کم‌کم جذاب‌وجذاب‌تر میشه این دوره از رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/24412" target="_blank">📅 01:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24410">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/khKSJC-hVW53aWxtw0_QsQEoxonrPXJA1Fyw_S4pVy_HEy8138r4wTYMfgHsujvNuw1_JTozYrVNAmNmXTTaBPgefTQA4IIebDm4xvsFi8IM-mZ71Xh0SSrJQC04tW6Di2k3BQPrhj1uZ_U3h0ew9Y7PTAmOJJcCBbIU_djPaFIxpHOkpHlfmaKLYcUVgCxzyB71N_tLluuX01VTUjBy1U1e8IkwoIlTa7Vm9S1Aw6bUbeFa7OBLG2k4qDWRmOvaeTS1p_kSIajLO7q5vVU8MKs0O0yjhWs92oPK5wEOrLWRZg5-HUJ2tOwCFaa0Xo9IdIRczK0PahgYOw_8ey8kdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هفته‌سوم جام‌ جهانی؛ فرانسه مقتدرانه صعود کرد و احتمالا در مرحله بعدی به مصاف سوئد میره. نروژی‌ها هم بعنوان‌تیم‌دوم به ساحل عاج میخوره. سنگال هم‌احتمالابعنوان تیم سوم راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/24410" target="_blank">📅 00:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24409">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XR19KrBS0voWMfhLFJMoHUtrDuwxSGQsRdyy4eCLUYjurSwLwKk60yd2gUnoICFXVEYGgEFOKGyzHZNVUj-lqttWk1CSI5JjAdDIIURPFrUDBAQ5uLvKWQwiAEivMo0MRqN6xF-74Nh-kYeLxIYMH4U9w4wgFMZout9GGC-uHWms4JVBW_f-JNcmNF0ArN3G8LrpB4NWycpjQhMRM3So2U3BUasKaENi8FeQCk75fkggCyc9HqsD-jQJPaS1BO55v3eB1AKKeWRHIQbKbgYQNSp5nmtBNBIlESdwyLbLtPovOOICM8vZDJVe4CYOMKjUSpMrVINGJoZBGwWaRNb0kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با برد پنج بر صفر سنگال مقابل عراق؛ حالا اگه بلژیک‌نیوزیلند رونبره‌ ایران برای‌صعود باید حتما مصر رو ببره وگرنه بعنوان تیم سومم صعود نمیکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/24409" target="_blank">📅 00:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24408">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_RZXn0mSUSfvmtCbGKLuuxjLsN7M32UO2Xu5RTWyAYzTm6pCO9z7073b4KcAlOM6H0lqHEXshoL-gzddFmM78MNxbCWGOgQ7l9hLW6TlaZTWBIBwlJHDh3fELQaSUDoro6QIaNwXQ44F4ymJcz-8QAKcOWbd6B2F0BTbNBtyzHJ_XDl9hZg09xMdB91K3UUR8te90Ha6RFG-xuWI5QnOrf98WJcvLz35FfH4JX1E-XAr3cGox2ASF9ZnmtKlYzEwmGUb_c4eeGY5y7y61tuNvhyFLD_4IVAZEcWRhbSvH55dpmJ6ciha_raYf8Pv39ur-_UIbZzSMzRy8i9HzMgyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تمام مسیرهای احتمالی شاگردان امیر قلعه نویی در مرحله حذفی رقابت‌های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24408" target="_blank">📅 00:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24407">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VUmVZuNlBhOjMYvrSgZesMG5Y2HuY18Zu1EQeY0K66a9TBE-ob6UsFZ9I3NoGLyrYLUJjtKv2yWi7zEkPBEiWMgf50Tin8em30rsP_J8sZVHKFNZaSZ9XXSBdbxGaw_Gez1HiJExRSWlbFs9cSs5H0l5WZNymo9UxdnG3i9dTnVSubIJX2MZPCLeEfg2j4btP1Xi85PHzSx-8XZvvpQWYGJXyb9ZkzeiNBpmcpWxm3-8cl5ZwnIceavKfMxy_ua8Wc1JuXmACYxJ5v_a1xnCobNrYtiJKgS41ke3lAqgUZxZSQeaumvLP-z95cPQ4adSW4LgI449NVwE86pxK5Yd2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دراگان اسکوچیچ کروات‌دقایقی‌قبل‌رسما پیش‌نویس قرارداد دوساله‌اش با باشگاه پرسپولیس رو امضا کرد و رسما سرمربی سرخپوشان شد. باشگاه بعد از فسخ قرارداد با اوسمار ویرا پوستر اسکو رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24407" target="_blank">📅 00:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24406">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L41cYLSZ4c4He0uXoHAiecbr4SaXNOwW4QFkDuScbxfOEsGv8hoUeINxYiExjedOhIR-o_RnsS0TmnFOZWi3A6P6wTXTMuik8tTdT-WuzAr_C22SO6pyiNjIITdjmMg14Bob1jWwg0xGJpNm-8YL7rIZSsSxilnB_Hd5MfmURJ_vhUu2zR6Hb1AT4UWUnjbprXcrsX9qVyjso9wlWC1w75SqeL612cZD-FHZ7nehvUBzjvXYGxE3ICG_oLfLBNyqUpHnb3P8clBqUeocdg-99mL0RvKqcDeKkGtzA9Uw7n1c1tK-NL6SlWBrGHl84wNq869LFrQ5rWFuK5yqHPzHGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق پیگیری‌های رسانه پرشیانا؛ این‌استوری‌جدید اوسمار ویرا مربوط به آخرین بازی اوروی نیمکت باشگاه پرسپولیسه. اوسمار به حدادی اعلام کرده با دریافت رقم توافق شده 900 هزاردلار فسخ خواهدکرد. ضمن‌اینکه نماینده اوسمار با باشگاه تراکتور مذاکرات مفصلی داشته…</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24406" target="_blank">📅 23:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24405">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec8965f3fd.mp4?token=OT2v877ZWvfkC-7aDTOVY3GAN-HC9yDeCa5RxzMHWyA2zm17Ek0LYowq4OIkZpccO4-iXmiaxDf1mZv7Cu7oJKB6FkL4bYkn4WDahJdYsHs8M4FiuhDI4Gs6KVdN6PVaLnz9AaRPyWGECJIobKc07ULUOMvrwT6HQkF2qn2oFhov8UHRLw2TLoaxJOG4NJXBCKrAWjVyqz5bHZrJ5gRn0PqoyXggtyxQXLkuIlwv11dojnskRuIwEw1wIGJjtDJLp0MfTMFbMnIcn36wd0CYuWZ0EP0K12HK-2m1nw3tQ-d3o3-c22R_aqs5oPOJjO5Ki6krEms7Ah-YvwrArBOJYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec8965f3fd.mp4?token=OT2v877ZWvfkC-7aDTOVY3GAN-HC9yDeCa5RxzMHWyA2zm17Ek0LYowq4OIkZpccO4-iXmiaxDf1mZv7Cu7oJKB6FkL4bYkn4WDahJdYsHs8M4FiuhDI4Gs6KVdN6PVaLnz9AaRPyWGECJIobKc07ULUOMvrwT6HQkF2qn2oFhov8UHRLw2TLoaxJOG4NJXBCKrAWjVyqz5bHZrJ5gRn0PqoyXggtyxQXLkuIlwv11dojnskRuIwEw1wIGJjtDJLp0MfTMFbMnIcn36wd0CYuWZ0EP0K12HK-2m1nw3tQ-d3o3-c22R_aqs5oPOJjO5Ki6krEms7Ah-YvwrArBOJYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تورنمنت‌آسیایی؛شکست‌عجیب‌سرخپوشان مقابل جوانان چادرملو؛ فرصت‌آسیایی‌شدن‌از دست رفت. از بین چادرملو و گل‌گهر یکی راهی سطح دو میشوند.
🔴
پرسپولییس
1️⃣
-
2️⃣
چادرملو اردکان
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24405" target="_blank">📅 23:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24404">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V3WtZm0aLPu9vwffN7waikkXT3aMhRjOHWl1IUfIgnRLnT1Gc1mrG0-IiZDuHP4CyOMNuHH8bPA27PtQAa8FNyBsMwEDDd6sJbq2RNZ-AIeqkh_uEZuJE9WXeLEx18pgarEBqyb9Nz87IJAsNpdQ8cyBzXKHITjNxJvE8H2OcJ9YDdjre9sousVXtu_8ld5PD_So9AmKlrON2GVSllop1DghxHAbmjkv7k_OC8AbsuNth2v4zN6CQPjXvsSV1iLx2rGyxlD1Wwh4vFpt3x00aCqJZ3StS-n44otgJuqqyXv5naAjZ3FzYJJFyLcNSmPMTsPDLkAM2Gfzj-zUGE-yRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گل اول چادرملو به پرسپولیس توسط سیروس صادقیان در دقیقه 57؛ بازی حالا یک بر یک شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24404" target="_blank">📅 23:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24403">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c65cc2b59.mp4?token=S2Pa8ICYhQelHmk6cvSUH2WPfFzzKX9A9NIenxL1TY51JIy4jETpR7n19tp0qBkIXhI5xMoFveCW4oDkW4pMYt-p8hRGGrSmlDU45_YSREddHDJzcqzhdnX79hVZX9uUJ21U6kTNchbveGQtRalat-hbwaW_w_HVUA4kHQ8UXGtLxUJ8bP8O0zEieSZLl8fkj_WS8BrQQAtT8WFYcOFkq6AUcl6WmzRNFWSYrIHZP3qQHFTUBGeYT4q5B3yeO7bNS5l02mtV75LDMNqB90U2uuNA8Or2H9_n-U2b_58fVegFr47LJy18VnfC0K3wZ9Mxj3lVDvnDkU0oxkFaZ1r0eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c65cc2b59.mp4?token=S2Pa8ICYhQelHmk6cvSUH2WPfFzzKX9A9NIenxL1TY51JIy4jETpR7n19tp0qBkIXhI5xMoFveCW4oDkW4pMYt-p8hRGGrSmlDU45_YSREddHDJzcqzhdnX79hVZX9uUJ21U6kTNchbveGQtRalat-hbwaW_w_HVUA4kHQ8UXGtLxUJ8bP8O0zEieSZLl8fkj_WS8BrQQAtT8WFYcOFkq6AUcl6WmzRNFWSYrIHZP3qQHFTUBGeYT4q5B3yeO7bNS5l02mtV75LDMNqB90U2uuNA8Or2H9_n-U2b_58fVegFr47LJy18VnfC0K3wZ9Mxj3lVDvnDkU0oxkFaZ1r0eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام‌جهانی ۲۰۲۶ رسماًبه‌پُر‌تماشاگرترین‌دوره تاریخ جام جهانی تبدیل‌شد. مجموع‌تماشاگران بازی‌های جام جهانی‌فقط در ۱۵ روز از ۳.۶ میلیون نفر عبور کرد. این عدد رکورد قبلی مربوط به جام جهانی ۱۹۹۴ آمریکا حدود ۳.۵ میلیون نفر رو شکست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24403" target="_blank">📅 22:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24402">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abdda890a5.mp4?token=Znj3x_Jt1d99gdn8lLS5NqNGKwGIo4HSWZV8pX4TQEVGIwgXvBZVlNOAzosUucVxqQMar2UccNNtko_7rsGdy6qEoS8xSwfmUBJlHtM7mFzYoU0TsvyYG9cqH1psdVGOVANkL5aF8YA5V_h10z4nvw8eHl_XA6fyq7wfJuMWeiQ2JKN9h8XTZkK4UGyT46PP1rdxTpZqnE_JD5F5PA3s9_J6FqzZ6T3Ql5T5-xiD2nrKV0v5ovWpm1UVO7BIO2z8FKHwU74jGl_QS-nNpRmFQyRt3PLZY5yOjb8k0_QuUPBD790PoJ-ZpgrvMdPcHWx6RN1W336_cuaf9KvtuojFPrRUnZwPjyUL_iUsTY7N261Ew-a0OJsAuvu-tneNg2sD1xQly3b6YtH0C5nZHske49Qab1mvz3Em-tta5M0KT1A5Dl0yFnA3wMRdSTVV7OWRsq3rtjPCQDG10BhPrTwUhgqPtBNmaVTVMb-t9tRNmjQYMXCFgyf7VqF65Vc45FV3ljEE9TPOkLfET5aAW0FWSYd3gTxgqht5a7m-ZQYbLjbMGqsZC6NX40utYig82hs9eHjK0vkr-LaDW8IbnC5H8TBeg9J-amDZwSJw9Ttd2PPJ7GYBjAdwF1lxVPKZ3Or0MJgNkLdTUcRTr7ADl3hklbhn2WPHcC-1qsOlxVbdlQE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abdda890a5.mp4?token=Znj3x_Jt1d99gdn8lLS5NqNGKwGIo4HSWZV8pX4TQEVGIwgXvBZVlNOAzosUucVxqQMar2UccNNtko_7rsGdy6qEoS8xSwfmUBJlHtM7mFzYoU0TsvyYG9cqH1psdVGOVANkL5aF8YA5V_h10z4nvw8eHl_XA6fyq7wfJuMWeiQ2JKN9h8XTZkK4UGyT46PP1rdxTpZqnE_JD5F5PA3s9_J6FqzZ6T3Ql5T5-xiD2nrKV0v5ovWpm1UVO7BIO2z8FKHwU74jGl_QS-nNpRmFQyRt3PLZY5yOjb8k0_QuUPBD790PoJ-ZpgrvMdPcHWx6RN1W336_cuaf9KvtuojFPrRUnZwPjyUL_iUsTY7N261Ew-a0OJsAuvu-tneNg2sD1xQly3b6YtH0C5nZHske49Qab1mvz3Em-tta5M0KT1A5Dl0yFnA3wMRdSTVV7OWRsq3rtjPCQDG10BhPrTwUhgqPtBNmaVTVMb-t9tRNmjQYMXCFgyf7VqF65Vc45FV3ljEE9TPOkLfET5aAW0FWSYd3gTxgqht5a7m-ZQYbLjbMGqsZC6NX40utYig82hs9eHjK0vkr-LaDW8IbnC5H8TBeg9J-amDZwSJw9Ttd2PPJ7GYBjAdwF1lxVPKZ3Or0MJgNkLdTUcRTr7ADl3hklbhn2WPHcC-1qsOlxVbdlQE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
#نقل‌وانتقالات|رسانه‌‌های عربستانی: عبدالرزاق حمدالله مهاجم کهنه‌کار مراکشی قصد داره در ژانویه قراردادش رو باالشباب‌فسخ‌کنه و از این تیم جدا شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24402" target="_blank">📅 22:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24399">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28a6fd59e1.mp4?token=l8ILcglpNnq9vGMr93S9QuWwYy1ZTBo8n-BObz4JuGBJWFmfwYlFTnxb5z14MI8ZEhBcSkhPW5e3T81d1oj9qiIGwAHqtSFRiTEN2G2uFhPg5swrSRzOJ5-tnNcjzTzbmFOpa-3bTxDOHL5pWkJj65JINiYfZIfI66txsjyYc-75qCyQxWGxwnHTDq0_0TwGB_VHw52xNREYGdgPqctUlncC-tPwOxUWJZqdB2_woGVZgc89uw3ruj-MiIy5KwaYG8f_vUZKCMWRN6odTNIRvEVxj4Nsu4B1Bn-pRg1mZvMagVHQfhl6W3IX1Sg6HWoZdG7f2RcBMUef_ULgsjf4gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28a6fd59e1.mp4?token=l8ILcglpNnq9vGMr93S9QuWwYy1ZTBo8n-BObz4JuGBJWFmfwYlFTnxb5z14MI8ZEhBcSkhPW5e3T81d1oj9qiIGwAHqtSFRiTEN2G2uFhPg5swrSRzOJ5-tnNcjzTzbmFOpa-3bTxDOHL5pWkJj65JINiYfZIfI66txsjyYc-75qCyQxWGxwnHTDq0_0TwGB_VHw52xNREYGdgPqctUlncC-tPwOxUWJZqdB2_woGVZgc89uw3ruj-MiIy5KwaYG8f_vUZKCMWRN6odTNIRvEVxj4Nsu4B1Bn-pRg1mZvMagVHQfhl6W3IX1Sg6HWoZdG7f2RcBMUef_ULgsjf4gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
گل دوم پرسپولیس به چادرملو اردکان توسط محمدامین‌کاظمیان دردقیقه 49 در تورنمنت آسیایی! این گل توسط داور بازی رد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24399" target="_blank">📅 21:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24398">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3569629639.mp4?token=mNMG44ZejQXTNHF1zvCOzDRO_lp3ehfIKhlG4XLQihgI2hd_FnBFcgVCpVoNR3PgRUyljRbiPI74QXGN7EB-pYufRurxPxhJt30fFPJ7-FjeGa2yC2yQJ9IG-rtaXovNzS_6OlJ7s2KolJbktEyBPESaG7_toBa7EWwve4Vl2VVw_PBTpv3jn6r-0J_uwFq-SrHLVyx1xBe1m8KUAuDeng-wMQJxIweDEKjAHbk1rf5LtepPpVYYJ8k_IUoMD1vye_IOMEfFwU07B1X0Bi3qx-BQa35oeg28jZCYlOCQ_3iDaT73NSXAvE_KZgDAdbJ8lipfKjgtbDj1XAYYP8eZB1UdTzoBZ9PLGTjIbYks-wCr8L08-1JagBk0hVjdwtK3lYxdgux8T4o7KfeiWsHPZNiVI1SADcsIlQQ3fDS3JoveWgK3ipkvU8cFTmnqLD02izCkKmPl_zs9kCYoRZBwta9t5mzxm1BTiO71Pnq76SgWecoQTXhba4RV-ejAHjKZdWqssWfP3egFGrNt06o2vyttzck8byc6rM4V_o50W2EiKRjH-785SDF-QiFAd26ZviQfkjiWlF7jghx82YikR_aAaF41kczQ1t_tEsMKjHlGwh7dHbnVWfIc58GL13SVkVBmS1gAZiy3o5XnQmmP699NTMGZBUqNDHkQsiVSgM0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3569629639.mp4?token=mNMG44ZejQXTNHF1zvCOzDRO_lp3ehfIKhlG4XLQihgI2hd_FnBFcgVCpVoNR3PgRUyljRbiPI74QXGN7EB-pYufRurxPxhJt30fFPJ7-FjeGa2yC2yQJ9IG-rtaXovNzS_6OlJ7s2KolJbktEyBPESaG7_toBa7EWwve4Vl2VVw_PBTpv3jn6r-0J_uwFq-SrHLVyx1xBe1m8KUAuDeng-wMQJxIweDEKjAHbk1rf5LtepPpVYYJ8k_IUoMD1vye_IOMEfFwU07B1X0Bi3qx-BQa35oeg28jZCYlOCQ_3iDaT73NSXAvE_KZgDAdbJ8lipfKjgtbDj1XAYYP8eZB1UdTzoBZ9PLGTjIbYks-wCr8L08-1JagBk0hVjdwtK3lYxdgux8T4o7KfeiWsHPZNiVI1SADcsIlQQ3fDS3JoveWgK3ipkvU8cFTmnqLD02izCkKmPl_zs9kCYoRZBwta9t5mzxm1BTiO71Pnq76SgWecoQTXhba4RV-ejAHjKZdWqssWfP3egFGrNt06o2vyttzck8byc6rM4V_o50W2EiKRjH-785SDF-QiFAd26ZviQfkjiWlF7jghx82YikR_aAaF41kczQ1t_tEsMKjHlGwh7dHbnVWfIc58GL13SVkVBmS1gAZiy3o5XnQmmP699NTMGZBUqNDHkQsiVSgM0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
گل دوم پرسپولیس به چادرملو اردکان توسط محمدامین‌کاظمیان دردقیقه 49 در تورنمنت آسیایی! این گل توسط داور بازی رد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24398" target="_blank">📅 21:46 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24397">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3O1Y3mMMu2sVJj0Bw8ELxrLMVeQY0A-14EDl6nmEauZ4QQKZDqmGSVh_7bU8yH-4FISSWQxfluxARRJQfpHvAxvmhXWlAdUub1qTqtgUIWaGXKyJM36B8ookQpI1k6DKZpLGufM1G-2lqyOJ4Ze_0NOKDpnFbRuUDsJFad4q9ODGHsNEn_iOpxKYUiKkgHWtsCrhcCWL-eDhifgrEtJsSHmVucr6AqmoqD3LMdDj5Jyaj2jW7_MlrgztcJnyhEkNzPXw_2qZDS5CnYv1xFMJeJlb-Nbs3bmr10Sn_5r8vk7YTMRW3PDUdh4XerotqN7igj8dE9Se3b_QEoaLD0skg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ ملت‌های والیبال؛ ترکیب تیم ملی والیبال ایران با ژاپن؛ ساعت 18:30 از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24397" target="_blank">📅 21:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24396">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c5878d1c1.mp4?token=TJKHbFYEdWAk66JPMyp3kAKu3ez_BNTyRsgyGemdmQyorScCapdCBOYiQ3mFAIVLTi6g2v6I9AG7Mdfr36PsZWkyyKvQH-Cwwib-etByWrvEtO4BaEcCHyRX271dckZzE-ZGA9BcB4kJ9onqroL22X28u6sgOwB-1lhRYB5c05ek0lreBELRIwM0v8uZkT4cCcfPg0gGghxMDNmWKAmNlSDvS7t3SnV6AsyDniltKnDCGbyPFqGvMmA5b8eVxFebfMm606tmh8F8gB3Plxf6gpudquvwFFDFHz-TeoIUf_UmA1CuJAdNTJl-VvZrCRLpnQ4J2uxPKKpRZNV_NHKUQnDll9OWBUjxxAoqKMzrwzc3OdgUvThZsE_hw9whFmfwTP28mR1KgKVL5LIf7MUlZBNtOur5L7IQYLCVEem-13aa9ObJwOf2EAe4Hud1n3j6Vq6_HFtL5nyTOErgyM8R8ppp39ObLhtY5Ga9pkO_8JP1QtN42W9hZwXeFxUc5oOMI82Qf1QOPD_LI5zbSD1FQzBUnEECwSJPiI_n_sChCkz0oM3qo6qoKL1UXrSw9B1nsD3gyR4_MGMuVzy3wHdcgPIvc7FkSBdrFf5O6AIAzC6LrW5WaAUDAlIdcCJbJgXkRLFahTu_7UnC6udK3m6qGVaD255XVF5iWFB9VMfp7V0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c5878d1c1.mp4?token=TJKHbFYEdWAk66JPMyp3kAKu3ez_BNTyRsgyGemdmQyorScCapdCBOYiQ3mFAIVLTi6g2v6I9AG7Mdfr36PsZWkyyKvQH-Cwwib-etByWrvEtO4BaEcCHyRX271dckZzE-ZGA9BcB4kJ9onqroL22X28u6sgOwB-1lhRYB5c05ek0lreBELRIwM0v8uZkT4cCcfPg0gGghxMDNmWKAmNlSDvS7t3SnV6AsyDniltKnDCGbyPFqGvMmA5b8eVxFebfMm606tmh8F8gB3Plxf6gpudquvwFFDFHz-TeoIUf_UmA1CuJAdNTJl-VvZrCRLpnQ4J2uxPKKpRZNV_NHKUQnDll9OWBUjxxAoqKMzrwzc3OdgUvThZsE_hw9whFmfwTP28mR1KgKVL5LIf7MUlZBNtOur5L7IQYLCVEem-13aa9ObJwOf2EAe4Hud1n3j6Vq6_HFtL5nyTOErgyM8R8ppp39ObLhtY5Ga9pkO_8JP1QtN42W9hZwXeFxUc5oOMI82Qf1QOPD_LI5zbSD1FQzBUnEECwSJPiI_n_sChCkz0oM3qo6qoKL1UXrSw9B1nsD3gyR4_MGMuVzy3wHdcgPIvc7FkSBdrFf5O6AIAzC6LrW5WaAUDAlIdcCJbJgXkRLFahTu_7UnC6udK3m6qGVaD255XVF5iWFB9VMfp7V0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
گل‌اول‌پرسپولیس به چادرملو توسط کاظمیان در دقیقه 28 در تورنمنت سه جانیه سطح دو آسیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24396" target="_blank">📅 21:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24395">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHIcZXBfmwfB3B8CierdjBhmZR09Y-JT614FUEO-XHnPXTZcHLFXMFcTVeq6EE2uy2FEt4lbkn7TiyVrVVnK3iZ0yCDU6P_Q7lpW46mI6ouM94TPc-1UcHS9b3l-18pnJDdWgMaOSHAzGsSIsOUep5V7gZfZgvc7UkjOrRnofE7PKGbczpACgMTVhUVPx8LFeWxfJTe-XL5oHbYC-JIaBjr2c-eVDRt_aqDZgw3c1iIjEN011a6yZ2JGOWXCb0Z1y33qJdIA3OyD1NSxl2fX-VvSISpRkafSffsqurBnPmbU2kRtYGLgrSgXbUebUK16DRfnCkPE_wXJDuTPJGXRXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#نقل‌وانتقالات
|باشگاه آث‌میلان با پرداخت 50 میلیون‌یورو به‌PSGگونزالو راموس مهاجم 25 ساله این تیم رو به خدمت گرفت. قرارداد ستاره پرتغالی باروسونری تا سال 2031 اعتبار خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24395" target="_blank">📅 20:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24394">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bArGO2sCnaG4oftz2ToyAUVuX52hKKL4NYX5c0eAAjWrjuOOi6Cj5rRPoUqkC7zN-ODkWZz2X0Jv92rZ6j6sckLPIzpvLwOD2YhH7tKJeGmM4ehYNatOMHRlUgiOrbRBaKi0l8wEdC0vPHUfnkmL5iM3gc3sFvWEvl3tDQVSl6rtbB6fgb_jbm_MgTU6aN82rqiWJzyHbU6Hww1_ggCiX87lurLAXDuGsAvIudmXUaSqJ9Y3bJ9rEc4_cSnOvr38s-5lQDi-XvjDnuF8HR_CYtRmNEGbghWxBoOb9BQwRNltFXPBAJ66adxMfu4c4NBj7xR89zQvz1W4muzIkXiweQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛ باشگاه پرسپولیس باارسال‌ایمیلی به باشگاه ملوان انزالی خواستار جذب فرهان حعفری هافبک تهاجمی 20 ساله این تیم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24394" target="_blank">📅 20:25 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24392">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z0BdMTz-euLtuEXkhRgrBmVHTVDDXfjtXq2LHbIBBq6NRm-4BwDgRggPtmBihf1_K0EpvBexTvzlv3Xt68VFVugQI9y5_90MgCakmjnBcseFizV-q--zgRcpDjVdGORjZyZaFuZUddVnYzWDY_WfDcJVaSP2Gc1l-ENxqzSgJMfeQ-vDp6AYPCpLzjUhyApYvT0aRUzPa1nK3Nss4N8Y6pjVm6aCJlZ2ugSvy3XBASU4R5zQ5MJriFM6bYvkUdjAKcwV_4TYUAtVLlFO5S3HfTG280xxHiAC5eL4oeThs0DfszMXBnchP9kWEWYPXtnqh9noWHDbVjqqZ0zpRj7FqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vQIqaXi17gB_ogr3DGApHF6s5Yci26VqEz9gqf7YOvfNFQfe8UIUBMRo1yhBsdK-vXKK_zDTYyi8teEytHMdbLelAvoJpc87xNa3iBsQrQ3r6dud7AA0KeevJjBxjB6XsZYN1q5keRnMxIL_7RV0XFTh4QgNzX_8T3_D0vm5vsX3NRdprpV-A6xKOyBjpSpW3WdN6Ci2oXZWagq9QqoTZ5WmoxV6UDUITz2eA8uIgzi_ng4-t1q9iT_Ms-V6q6Ot8Cix__7HrVFqmHaCbM5xD2OnbE-FgwKl2V_nVgDpPuGW4PYz5KdXKNKk-PoEx_BmbiE9hhP006MxXY-8dsbPtw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ناتالیا شادل مدل استرالیایی دوس‌دختر کنان ییلدیز بازیکن یوونتوس. این دو حدود سال ۲۰۲۵ با هم آشنا شدن و رابطه‌شون رو خیلی خصوصی و دور از رسانه نگه داشتند. ناتالیا مدل قدبلند با حدود ۱۸۲ سانتی‌متر هستش و قبلاً شایعه‌هایی درباره رابطه‌هاش با زنان وجود داشته‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24392" target="_blank">📅 20:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24391">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MkCM7xsYj3jhmBthwNMLAJnod8Ygt2Qgw5wdtGKT0CBtRTCdZr5ac0hG7ODMzkU22o0tppR7pIOWNQXubqmX5DgIBo5qcjIKVtuxlqsVGrO5_-gEf4fm2PkW2dBZC7AAbwtDUtjhbKgjQtHylRo07E61ECM6qkhBQOa2v9UqEHWyLq94uBqVJ4ZcN_iWExAWu5h33F6GKH-g-ArOhs52Hg1iYIZCyvnjlUOv3X0wqLcRu-GRB9S1l3azI-ciO8G7VigfTh1SNlh2J-pUkWiIRLMY9mtnsrsBtZzPJZu_ZzKh2zcktPWUU70bF4lzikML0IWwm8XhljfDwZrAl_W8jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
تورنمتت آسیایی؛ لیست بازیکنان کامل دو تیم چادر ملو اردکان
🆚
پرسپولیس برای دیدار امشب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24391" target="_blank">📅 19:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24390">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRMNVuRLlyIjDcLJevbN7H9XCdonfNC0Ssjrnsc0G3b-UCPCTOjeYKsVSeR4kaJBmuw9EWl2U1BCx85NjGrBKNfBBWzwbVBg1ZRCGPqAGQemMRpUJa2LzmWqo32VM4Fax0o14AnrDemmhyu-f8LXdH_2aswSCuyBHni9micsdawPsoEQQJO8FwtaT41ajm5vL2eV-BcV5F-y9lWRen4ODpyVZHOBx2Av7OVkXBzTtuwBT970dWBAyX7hxdgQsPHtnp8ULhhYp1c7o6kYWZPsDf9j69Rs6N1g7eg21bHiSbnDIFwwBF47oN021mlD8dTSyeKj4rnbAQtjppZxHzyHvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
تورنمتت آسیایی؛ لیست بازیکنان کامل دو تیم چادر ملو اردکان
🆚
پرسپولیس برای دیدار امشب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24390" target="_blank">📅 19:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24389">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eqWkZsxG-YPRgQs-KFg9fScRdQfKsktghiZtxHTa5KKJtA1SnttizM1r4QZmCD9DlrA-93v_-r36S1p7n9u5JCghQZrY7XLzW0qK4wK5kU8oVMUV6NtE_DVclJ8fyv9xCCA-ut3JJihhE9Fi_qHeTeGvWp6LdBloitOpF7LWh5EdRDBTlkLDBwevlPX2Sp_UDsbdu9N7o2KcqTn9FWXKTTAs_7YtQbqRhXkOl-3VxkzHpFFmKqPmYnqtJeQphSDbQMVvMNs6AzTbG66vWNNYjglEMLF7AHvn6o_6lHByzPlePEahKaTaf4uJNbhCy9UPcxVs8yE2f32hQZu7_pCdNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب‌احتمالی‌پرسپولیس برای دیدار امروز برابر چادرملو اردکان در تورنمنت سهمیه آسیایی؛ 18:45
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24389" target="_blank">📅 19:26 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24388">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dfUwbJPv8owj4sMJEdr4CKB495CbpMwQRwj0Gzs7EIhdQ58xm3AdCbhTs3tkvgT5gUh57THuIinvsxFAauv3NPt37Q4UkDZ7yhztZ7SMFGSNxfBgp354myPP9z52lxxHOBZIVQDUFd7frHqZiJIK0UqoD10d8S1VP6OtZcRqgmv4uY87IzCxCJxYqx-_Y7Yg44Ii7w3j3aWrCE2SB8bPKGVGrrtQBDWDbAMsQDHmCa27iSCb7LOgddAjSUluDCvr9AS9drhbnfibCzQnbNVExIamh9dQdBxqduAyaofKdUJDSMTHTc6_989ujpjihmfCSkqQbk3hl7HAiFZg6qqFdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌اخباردریافتی‌پرشیانا؛علی تاجرنیا رئیس هیات‌مدیره‌تیم‌ استقلال صحبت‌هایی با مهدی هاشمی نسب پیشکسوت آبی‌ها انجام داده تا درصورت توافق بین دو طرف؛ هاشمی نسب بعنوان یکی از دستیاران سهراب بختیاری زاده به جمع آبی پوشان برگردد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/24388" target="_blank">📅 19:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24387">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-NkNBZf_zhqiJfQX4sAGlTwPwBaCOqES8EDvSxm33aoXTJrAjCPQP6YgTt1Jd07cbNCvf6Vv1NDoHmc0r9zERVsh4QahmEkJTgSHPNWzE1qlPik9I2pUmZaPmyObb6Y7qcPEg5lLzy3LavXOKuLfTDaefEfs7cWQSgNqJFxui-JJ0l17aVK1t0nhaSEdToTLK7k6algC0diw0YM8_QuKFawX3ZKPtboIN0BGQwCXIxJsd58_RUteumBmpYQIahmti2QFbo_Sg9vuS5lveaQugvH9ELxMDGPHscxegqalqgG_hh5XHNPDrTOihSMAe2QsVj71WVBBulU3SEEv_PL9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
ادعای جدید نانا کواکو بونسام جادوگر غنایی: من‌احساس‌میکنم که جام جهانی 2026 برای کریس رونالدو و پرتغاله و آن‌ها قهرمان خواهند شد. قهرمانی‌پرتعال دراماتیک و باورنکردنی خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/24387" target="_blank">📅 19:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24386">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEmek3WLEDfQobskq_xH8DNwBAOB9rg-QVcf2rKf8RvO1I7CDtbiNE0RxF9OYgWq3gjR93jga-ikwXOckvv2fReTOcLrg-E5zwXMxsPsV5szuMEdLCwH53k4ydarPU1pBZzRH-b3aB970VPvPVM6fFFi8uvNZNi-QCiAUapffAADm71a_tMeAIytRIn24VrpWNmSgPYpSlyfAwLnuTUFFWG8GPW9vfZSvr8OWnm1OgHs9daFrsYyvliaIEMVqG13uoJLTBZwlYdTHSN9wS12znwslufe9L0Mb7uYmpcd5qReDuyCVS8Rcv9jE-f-oKUJThrRTS2RB43EDT1OUYS7cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏰
بخاطرمسابقه‌امروز تیم ملی والیبال برابر ژاپن در لیگ‌ملت‌ها؛ بازی‌دوتیم‌پرسپولیس
🆚
چادرملو اردکان از ساعت ۱۸:۴۵ به ساعت ۲۰:۳۰ انداخته شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/24386" target="_blank">📅 19:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24384">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVFRinZkXo6ZbRghdm5LDmjMUdYGs7jFYIRRfuIXxUQKNEXzGT8a5yrWmaiY_ooDDHCYe1iMU21qhe9gFBuIUggQcY-GYpdl21KU-7b8KChvGe84zYiK-TEtCQEU0KO38kea7Opy2WeX6EAl6nFVgiwACR6n1CKWLQTT-Yv0XNdKv-Lh3LmSonDfOonll3w3woaUJxORpwpjRj28MsaS7YuUvVu3wMh_9okizeAcJI8DIhfjxyBJMvlY29PxOCSmgUB6J9U4dosNOkLrzqtfsZOylDzsZfmo59PpRCQ0X3lYhIGHVYGVqwzXONlv7nErCASiyRalDBaxCXrNbQkk4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
آخرین وضعیت تیم‌های صعود کننده و حذف‌ شده جام جهانی ۲۰۲۶
؛ تعدادی از تیم‌ها صعود خود بمرحله یک‌سی‌ودوم‌نهایی‌را قطعی کرده‌اند و برخی دیگر از گردونه رقابت‌ها کنار رفته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/24384" target="_blank">📅 18:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24383">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EXipgoIy7jaqNWcPY7haqUQbLmmoPty98HoUT4Mbb4cvK2-cnsIpvjNEhhMua-m2Corpcl5WNsYh8_nci-SpK4djiH7QceLfZ-ifSQNx4nPHAPXMd8oevn85Wwk-VLWHAAGDtzpf3_HODw7rMfP3FskWDyXj4nneoe-4h5b14JBgkeIETph7zg4WMqhDUt_hrc9SEZUSTJ1yCFYkXarRQyDmONNqZKtlITyAyeAtnTdSQioxVx_n_RWcx70Rp8Hr-qg-yAUxT3h-Hu8jIxpQDbsZ_7RWeTjmk8-9fzN8EiX9E4Qt-O9uLobn7fn9o3WL4_D_2QjyFRW2LKipzpKc3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ ملت‌های والیبال؛
ترکیب تیم ملی والیبال ایران با ژاپن؛ ساعت 18:30 از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/24383" target="_blank">📅 18:11 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24382">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFlonEEbKQifRxGtm8sitZWbBh6kaYt8hHMU87GJncHitSs_EFTRGZgMVngJp5BSztwYUapVsfVrYC4xbYlx-l6RPaOZnP6A2JrLjRWarCuGtmpVfRIgUBxk2Fj4a8sgFdv0WuVSz8ykzSGZSSmMFVThnYq-bZRHyfSCqk7KCty-Qm1rCdMESOkQ8qo_Lui5pEKNRqOFHOfMk01SgFoAzFMxvbq7HE6i_mc_PkVQpFUD6POjTKFBEZbbJZ-VZixrnql5lM5OimswabtYzioJ6iiEr9U54fDoQb9E0MVEtKf5X91laEFK_FJYgbqwd8fiQDrPV2opiFuXKxiD5cgB5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دراگان اسکوچیچ کروات‌دقایقی‌قبل‌رسما پیش‌نویس قرارداد دوساله‌اش با باشگاه پرسپولیس رو امضا کرد و رسما سرمربی سرخپوشان شد. باشگاه بعد از فسخ قرارداد با اوسمار ویرا پوستر اسکو رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24382" target="_blank">📅 17:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24381">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LAkZhOTgLjgIMF8Wg5eHp2D5nZ2Q4YGGZLec5kUQColLJbfImYtExGeY8uQin1Szhjz4sqjIsG8oLnbNEFNsTAlUiPbXYC3IYmZX71SjyIL6F6Ric7LoOlbWB6RtqRrlzpEl5f1zKGct_tpiIROZH2a6DuS_tQ9BvVPPtsB7GGBHtS0zUGwIeyMnzFT-Hgh-rQvPyCtvHx7XdEg_wCsTqULJg_1ftpRuuZGHdunjctz3Ei2zAeMP0RKFyKdyE0_cuy-Wx1ORHsL7zyHUA_VRGadf8n6vovtGFqjw4OuHRhs0aQA4ZxNE6-cmQiLiFQ_IZgpFdQtF_z7SrliB5_l99Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرچم‌حمایت‌ازهمجنسگراهابین‌پرچم‌ایران و مصر قرارگرفت؛ فرداصب قراره ورزشگاه رو از پر از پرچم های رنگین‌کمانی ببینیم. فیفا گفته هرکی از قوانین ما پیروی نکنه بین 250 تا یک میلیون دلار جریمه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/24381" target="_blank">📅 17:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24380">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i4UWl5hPI395RMOBFwy6IdxusScp2jw3ffwYiKpyR_4uzVhZ7yvEhrnxtBpn7j_qOfomJKRDWW0zCPscoq9-i5e43v_68YzcpnLlyD8Xa_BaHYxNGxgif1K0vfy-GsXmjHwrT6QytmsDfr1U5ob5jjRfbriZ1GG2vUfFiEft1j7bhtsGMpy5OrH5mY8l9sMddw-8lmFwsKcDIk04hsix1QLj3u4WFIdOcQwwwR2b37bJixs-T3RsTIPA5yOkLUgcSRqlqzoWWgsD3QwyhQG07yO4ppb3i39Un25eB3GMlPJgX8xLugFreh12qAk7F7A0U1ze4ojtzuodnl5jQzLzOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
🔴
#اختصاصی_پرشیانا #فوری؛ مدیریت‌ باشگاه‌ پرسپولیس روز گذشته با‌ارسال نامه‌ای رسمی به باشگاه الوحده خواستار جذب مبین دهقان هافبک دفاعی جوان و آینده دار این باشگاه اماراتی شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24380" target="_blank">📅 16:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24379">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/psxuWeLs9plwTygSGVrLjY45f_DM8wf-HDliejBUUHHSj23xzkEqd1BeVsvqfno-hqQxF6cKCCVo1Q-rqz2mvZy-OVCS5Ry8_6vOmLZ1czJx5hi-ve5SCChvuG5MZgpDgQDPPy6fOEeR_5oV8ya1B6zkEtI3w26ETGMNR4WuHFIVZEV7_v_KqERdRy_pAyYCqlCAlQ2bzCNLIBrDs6en-IWyQKvC9fQrTladke0CV7Poei96B0mmCvUq5HF872pe4iykrb81q2_V3XuTkdtr0D5KNiuy_gQyvIqU8g3hlTG0j3t5ofWaQn0CP7hm-kDm89qlUcMphSdntszSfwTGTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ داکنز نازون مهاجم 31 ساله تیم استقلال دربازی بامداد امروز مقابل تیم ملی مراکش این‌شلیک وحشتناک‌رو روانه دروازه مراکشی ها کرد که‌با سوپر واکنش استثنایی یاسین بونو مواجه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24379" target="_blank">📅 16:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24378">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d2f7b8fb9.mp4?token=U68jpDEMh6tni17voeF2aW-TbgDJqfDBWXnWzl5Jjk4ObIdkkbTL-O6P_7T8QOfi-svBine_CnzgrI_0DH1tP7iqX0WEOb6Af_qMip94XxEe5YOOT1c_PRg9Z6S2qw6m5AoID15jCQ5bY5DCAg-YysQy9PFTUlCE9axNszPbZIK04qamoJHCCaPbZDaGqLSJGaKaOPneSDdKyPov4RBg9zNFcQRi3iUP2lX5pVQeSmMy7vqztEcevByuxVB1fEx_eVvn-C8uP-1aAna7M6DB9ET_KD2Er8CeW8LJzoPoy6FtjJKYTHh3gvZqu2eQO3c-YD8tkJLXeuBVWHJyNd3E7DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d2f7b8fb9.mp4?token=U68jpDEMh6tni17voeF2aW-TbgDJqfDBWXnWzl5Jjk4ObIdkkbTL-O6P_7T8QOfi-svBine_CnzgrI_0DH1tP7iqX0WEOb6Af_qMip94XxEe5YOOT1c_PRg9Z6S2qw6m5AoID15jCQ5bY5DCAg-YysQy9PFTUlCE9axNszPbZIK04qamoJHCCaPbZDaGqLSJGaKaOPneSDdKyPov4RBg9zNFcQRi3iUP2lX5pVQeSmMy7vqztEcevByuxVB1fEx_eVvn-C8uP-1aAna7M6DB9ET_KD2Er8CeW8LJzoPoy6FtjJKYTHh3gvZqu2eQO3c-YD8tkJLXeuBVWHJyNd3E7DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
توصیه جالب جواد خیابانی به محمد جواد حسین نژاد ستاره باشگاه‌ماخاچ‌قلعه: هیجوقت تنها نمون. همیشه مادرت رو همراه خودت داشته باش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/24378" target="_blank">📅 16:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24377">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vAH3izoyTVmFXKDEcXN3LRdUAggWLreXjOeZSaBb8gInIfIq19nxJJ1lZ_B68F1fHd2V6EXnWfpPfAT4fI09UCWafQKwZjUtymYGrbR-KnPE850m3l9ZlxYH70Ce_zOpWLbemhZDKgaya6TRwLRvmWVMrcT-UNTD50uYybIhvjDlnjP8Kf8hUg021jL7w44EbRcQ5GGNU5lyUz3yyWqFXG8GommgRJxfCYvqQpZsUTCKW4WslGtEbkvDV46d_s9LMkS2mkHtl9KLKz52NnNMQDRtgPdKKQrtjQM8ZarSV4yxob5ZEDtsfX-jhk92t-2hzWw28-tTQ9g4i_y_pTGh6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥳
چیزی به شروع بازی
ایران
-
مصر
نمونده.
🇮🇷
⚽️
🇪🇬
⭐️
با پیش‌بینی این بازی، هم
۲ برابر
امتیاز
می‌گیری و هم وارد
قرعه‌کشی
iPhone 17
می‌شی.
📱
🔥
باجمع‌کردن‌امتیازاین بازی، یک قدم به برنده شدن موتور، توپ طلا، PS5، iPhone17  و ده‌ها جایزه‌ی هیجان‌انگیز دیگه نزدیک‌تر شو.
🛵
📱
🎮
فرصت‌رو از دست‌نده‌والان‌پیش‌بینیت رو ثبت کن
👇
🔗
روی «
لینک
» بزن!
@Snappofficial
🏆</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/24377" target="_blank">📅 16:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24376">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZ9dK_0SzYOQdeEiFyFfr8_Vesv38kNKvpmo8QbWLQsmCUH-gh6ZRYWSZcn6R2BTt2ONchMkX0YDa-_W3cRCcl_VH7aAUsN8UAR1G0D67Lpd6HPf74gQtYzGsXDVDXGSkcWFNho4o3FLHUCRnVMUhfhyaC7eP0kqh8UqlGSVYHT5OfcxJeq-IV7tL0olj0Oh6sHtK7d1_Kdw2Mk_xJNhmXvaGpNzoc_UOszQ-3I9VcJZj4f-2_40GQ8NnMqvQLyzO0cYQeztGktzSACAqi3WMpiplSYSR_wuemWy-eaw7TmfKQhdkmRjLYrfgK82v--2xIm1_YGLYI3LshxyzHa_JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی
؛ پرز از اشتباهش درباره مارتین اودگارد درست کرد؛
باشگاه رئال مادرید برای انتقال پاز به کومو 60میلیون‌یوروگرفته و یه بندهم تو قرار دادش‌گذاشته که هر وقت نیاز شد با پرداخت مبلغی ناچیز این ستاره آرژانتینی رو به برنابیو برگردونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24376" target="_blank">📅 15:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24375">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-UP2sECdGB_G9AL4Q_Ru8Tu4VnV-2d6TaG_mJ-RMThzjTJDe0e7GwFzu4khC8bP-4I3m1rvfvWwGGsOXJlNj3LuI99CIH2FAxCHiU_9sdkHg3RE5CLMjrYliXHtoAmt9QD9Nv2J7zSMZLc-bLCb-Dnd1atCwyVg-azamFSyekYOgFjA9XK0LKRcVd3XPO0LDzjpIA5n37Rpulgb9HUHbyYmSm7-385lQyPrpHfKwNswSibp9O30YBWu36MdFOt4GUl8SLm8YmuU9TfhcBZJw0kein49fmf6t68FaDLl34AvEuCV-pr5Vp450Xz0gG1Akmp6ocjzQAOB4yGBV3kWcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇦🇷
اسکای‌اسپورت:باشگاه‌اینترمیلان آماده است برای‌جذب نیکو پاز ستاره‌آرژانتینی‌رئال مادرید نزدیک 70 میلیون یوروهزینه‌کنه. پرز با دریافت این مبلغ بال در میاره و قطعا ستاره جوان تیمش رو میفروشه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24375" target="_blank">📅 15:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24373">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YkF42FPzJYb5xqT_MMFmBRqMH1M0w4YF5GnRbtg6RvJTxqINN1XBdAsrldmmb8CabmTfdi0zbAVJzn3UxSr49PdbKNszCEdQQbNBa84JFV-6RNiPSbYh49zF2HCfUJxE6I8ccEjguA_sLg8dgKA84GKaWem48T7zH_1QJoBxWjZ3TXt6tUJwQnBrxb325ohbaaBwWp0VGChJXMiJdpWJBD4pH72JRtPO8efAZv6FmPPm22ntk4F-MnjZK1iam1T97BaSUI7qbu71WnMMHhgZniFNPgVgEy3aQYUqFGOqu1QxJONnbON0AYw5brIEgDnDBOWgbeu4Ty5sRo5bYHKmeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cf0fdb6b2.mp4?token=v4FLBYhEkEOKomSFoZhFbhDXrC7llL4mhJe9Nukuod5yaTKqvjexOicDZjx_9-FbR4IpSkK4FppVw9TTyGgo-xpMZvQpNLejh-YdGPnD_2CM59PElX0SftMKRNPiN2QijaoTGvsoWisC0Xn-ucVcc7mKev8PlPgDYgMuQzReXAhinS_TxZJUqhZAJ8oM0wQb2BKQbLPhHbBIs4Z11NzvHbPTv_tbcqHTlkmvmM60W4CwLB3WB-CBcNkFXRY8JnxOv4IWwQbxBoc5xPcSCiS_eWlzE-iEbXcjUzP1Ef6Ll379XB4PGsEr7bqLjiSR72JrvjyrnIXLVe2bbL46ojd47g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cf0fdb6b2.mp4?token=v4FLBYhEkEOKomSFoZhFbhDXrC7llL4mhJe9Nukuod5yaTKqvjexOicDZjx_9-FbR4IpSkK4FppVw9TTyGgo-xpMZvQpNLejh-YdGPnD_2CM59PElX0SftMKRNPiN2QijaoTGvsoWisC0Xn-ucVcc7mKev8PlPgDYgMuQzReXAhinS_TxZJUqhZAJ8oM0wQb2BKQbLPhHbBIs4Z11NzvHbPTv_tbcqHTlkmvmM60W4CwLB3WB-CBcNkFXRY8JnxOv4IWwQbxBoc5xPcSCiS_eWlzE-iEbXcjUzP1Ef6Ll379XB4PGsEr7bqLjiSR72JrvjyrnIXLVe2bbL46ojd47g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سباستین بکاکس؛ سرمربی ۴۵ ساله اکوادور بعد از اینکه دیشب تونستن آلمانی‌ها رو شکست بدن و به مرحله بعد راه پیداکنن اینطوری از بین جمعیت همسرشو پیداکرد و از نرده ها بالا رفت تا بغلش کنه. البته صداوسیما این صحنه ماندگار که تیتر همه‌رسانه‌هاشده روکامل سانسور کرد تا یه وقت تحریک نشیم. برد اکوادور روی احتمال صعود ایران هم تاثیر گذاشته و ایران با مساوی جلوی مصر احتمال صعودش به عنوان تیم سوم فعلا از 90 درصد به 60 درصد رسیده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24373" target="_blank">📅 15:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24372">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0edb018d7.mp4?token=rz_TVTJxhxfwTkQXKJG2kd_Fuvu29XkGLG8Y3AT7ZDtJxKppyv5Y8Xef-PYNJed9gn0a-v2WkYkIWMMIO-bsNc0LDmJZRrGMg0bJD2f48Otrd-p27S3ROG0vm-AJGBuz-QOqzr6bYZunbb7ABbaCEwZI6kwVYZXZgd1fiB3UXx7v_2HcDg1HvpilG2LJZSLbMo1k6o73vtlypc_cnxEYYM66Zo6ztNnVJEYPHDVxJPsMTaGsgq9QaRO6EeXHoYG9BlOj3-m2JMiQgkeeYcSLYAmj-fhZ72mJD6EEygu394c0YhTVTAKdDpnmUaTM0dSqHCf3XGhzfD5tt46k9HeLgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0edb018d7.mp4?token=rz_TVTJxhxfwTkQXKJG2kd_Fuvu29XkGLG8Y3AT7ZDtJxKppyv5Y8Xef-PYNJed9gn0a-v2WkYkIWMMIO-bsNc0LDmJZRrGMg0bJD2f48Otrd-p27S3ROG0vm-AJGBuz-QOqzr6bYZunbb7ABbaCEwZI6kwVYZXZgd1fiB3UXx7v_2HcDg1HvpilG2LJZSLbMo1k6o73vtlypc_cnxEYYM66Zo6ztNnVJEYPHDVxJPsMTaGsgq9QaRO6EeXHoYG9BlOj3-m2JMiQgkeeYcSLYAmj-fhZ72mJD6EEygu394c0YhTVTAKdDpnmUaTM0dSqHCf3XGhzfD5tt46k9HeLgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏰
بیدارموندن‌ساعت 3:30 صبح برای درس خوندن
🆚
بیدار موندن ساعت3:30برای بازیای جام‌جهانی:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24372" target="_blank">📅 15:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24370">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ylo8xPdUe3bmRGldeRdvje_kpriP8VCh3S4YG8E3Q0znjwPlRsyM9zLphbP3s0LynauF3WG1MT9UpogADKN_VPOCPDHUOwjMnPUhKPSmO-oTGY95dMF2dZa8Pe9eMrM9E6rZNhViDGaM_Ou5x2bJJWxauhsOZBBiKc25OeV0fz42ez2t9zff-kKhddVOcN4sEndXLK-psBDqguyCrT_LL7IXutzt7hcN8uHiZtJmiq2Gd6dYGKaDEhKT5yM1u7sRtaOhqwJ7W_RzpmlYlwAKi4Gb6fXjfqFFgbfnXmN-YU13YNNe4Z-yMtZxvpzyW-JWrcBUFv9Y2ikSeOr4z6ACyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UrJDFLn2txK1N_fKEvs0kiklWNHTprngfoHBYhtY5Bq8DFKdhCzpG6Zw1aI0fPx0-jJFZXiWQZQxEsGk5pgqLsv2YLSpUbJu08yqCqBPN2l5lJ3agaI6bh-nSf4E-fVh6RXShFZXs8shSRuNyuJnljD76VNNhdbfZ4yguqgkN17t-KUMExKoLztRTW6JHrWchaFMrt4hIOKd1woOkzH_jBTbIv-MfwrvLT_-47kWvX8TUdcXxclFjjamKf3vkzVLNT31liazvqBaAO0WSq5F_FT8K18vDM_Az9vOW3JmapPGrdR8QO4jAUJQaP0JVzTI2gzwLAmv1NB8ihtPvTq5qg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏰
بخاطرمسابقه‌امروز تیم ملی والیبال برابر ژاپن در لیگ‌ملت‌ها؛ بازی‌دوتیم‌پرسپولیس
🆚
چادرملو اردکان از ساعت ۱۸:۴۵ به ساعت ۲۰:۳۰ انداخته شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24370" target="_blank">📅 15:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24369">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NT42rrEVv7euGKFab3Adn5I6yrtJPm8YIGB1DUeXHaIBGofANszc8gHdESORLwdTsV_5lOSNp32-Ua2n5JFVNno-GdVAJ42WI_Y7agtuKbtk7H-Qc2tQ1OCl1LWugT1DmMu8CphXvdt-ee0jWhlGo8KXAqwMjDOpM1i3h2pBcWq2-6Kfhha7RG_3mYukVzY3uNhTLY0qMb0Ua4NH1MZ8z6It4m2-oCxt0DlvMj9rmZdLf4TgJ-5s9Uios-a0XAiWPI22CgP14gQTlZkJJpM5sV5HTaWTceC7r-sE8XHGjqYqPo4GcZ75aRqjRyKP3nDFeurlosanncen8Jwug48KQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سال ۲۰۱۶ سمیر نصری که‌بصورت‌قرضی‌تو سویا بازی می‌کرد، برای درمان‌سرماخوردگی به یه کلینیک تولس‌آنجلس رفت و بهش سرم ویتامین وصل کردن. بعد از اینکه کلینیک عکسش رو برای تبلیغات منتشر کرد از اکانت توییترنصری چند توییت عجیب منتشر شد که ادعا می‌کرد علاوه بر سرم، «خدمات جنسی» هم بهش ارائه شده! توییت‌ها خیلی زود پاک شدن و نصری گفت‌اکانتش‌هک‌شده.بعضیا هم حدس می‌زدن کار دوست‌دخترش بوده؛ نصری امروز 39 ساله شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24369" target="_blank">📅 14:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24368">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ab6e00db3.mp4?token=E8JHgzRVDw89R02wXCoSYhlxOlU5-VDryrnlSfWw4OQVz16iqenyy9yI6OAtsp-93agJtIJdCYbNv0aQeMTw1wFAYkOSPg3u3_hENyXecX7twRUojRQsuFeHQJ4yFhK-HuSvpAY_ToxrNe8pjDjVB5trhu0o7OMC3UkH5Ii07iWwifhiqr69Vp5gIL5RlHlBA6-45Dia13_u5x5kgy16Mb8WWNKrr78I4aJSks8mk6Rs2B9hSEwaN-Nh8JYugLlJilfIavMGgX-eLDAmLFydC43jRXbhuJ50FqujubejKLLnsqeAy0wK_s0UQqhC4gH3VGXICO9oCWBn9LkFJQ9K4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ab6e00db3.mp4?token=E8JHgzRVDw89R02wXCoSYhlxOlU5-VDryrnlSfWw4OQVz16iqenyy9yI6OAtsp-93agJtIJdCYbNv0aQeMTw1wFAYkOSPg3u3_hENyXecX7twRUojRQsuFeHQJ4yFhK-HuSvpAY_ToxrNe8pjDjVB5trhu0o7OMC3UkH5Ii07iWwifhiqr69Vp5gIL5RlHlBA6-45Dia13_u5x5kgy16Mb8WWNKrr78I4aJSks8mk6Rs2B9hSEwaN-Nh8JYugLlJilfIavMGgX-eLDAmLFydC43jRXbhuJ50FqujubejKLLnsqeAy0wK_s0UQqhC4gH3VGXICO9oCWBn9LkFJQ9K4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تیم‌های ملی ژاپن و برزیل بعد از اینکه از مرحله گروهی خود صعود کردن به همدیگه خوردند و این مصاف جذاب رو رقم بزنند مصافی که قبل ها در کارتون‌محبوب فوتبالیست‌ها پیش‌بینی شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24368" target="_blank">📅 14:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24367">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bb5026706.mp4?token=EIi0QQd6OATt38-DI7Owfe2YpmIKOqrc3uDytCm0puIFfNhaUJggOPyL-3c2mT3p9JLZWLd7Ut-3A0EwP0fUXCGmvTeoIvRFRCS_Lw2QqSjHAYGv7Zy5FYg6D6PGC07P34wI2_4IjlI1OEvKqMXGt7NpOZMT7pYat8UXCNnwn8zWif2O0OeAp__nHuqnIoNZA9tVbQDhw1WGViMaYrxjJFlj_bpviy44vHCo5_OYCA_t2K_eQBSmJQRn3RAk2Fqw40Khw79Z4SsdMSjdi_5Nrckxh1T4GqiMN_iUYGyqFlGv3SDNLVFQ1lColqwrM1Vl6fIJwR_ZiyrsL1-KxyYYHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bb5026706.mp4?token=EIi0QQd6OATt38-DI7Owfe2YpmIKOqrc3uDytCm0puIFfNhaUJggOPyL-3c2mT3p9JLZWLd7Ut-3A0EwP0fUXCGmvTeoIvRFRCS_Lw2QqSjHAYGv7Zy5FYg6D6PGC07P34wI2_4IjlI1OEvKqMXGt7NpOZMT7pYat8UXCNnwn8zWif2O0OeAp__nHuqnIoNZA9tVbQDhw1WGViMaYrxjJFlj_bpviy44vHCo5_OYCA_t2K_eQBSmJQRn3RAk2Fqw40Khw79Z4SsdMSjdi_5Nrckxh1T4GqiMN_iUYGyqFlGv3SDNLVFQ1lColqwrM1Vl6fIJwR_ZiyrsL1-KxyYYHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امیر قلعه نویی درباره حضور پرچم‌های رنگین‌ کمانی‌وبرگزاری‌مراسم‌حمایت از جامعه LGBTQ در ورزشگاه سیاتل گفت: مااینجابرای فوتبال هستیم نه مسائل دیگر. تمرکزمابرروی مسابقه‌وکسب موفقیت است. درخصوص موضوعاتی که در دین ما ممنوع است و وجود ندارد، نمی‌خواهیم صحبت کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24367" target="_blank">📅 14:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24366">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MzOXnGLBbNv5wkJ1duRSN0PUb05go7FzzozxqjiM34gSBRIW7H0ISBdASrnGetSCutzwVGt2DQ9hCbGY3XaY1X1SQYnjoUBem2ELFmwAz-5Qx4r0xCCt2Yb4Y8oi0wABEIdhUgs7j7Jxpu5fySvs2LkQfsfaKqNfW4gqbklzOaE526rN7j8CiFLRAxbGCnDPcaQKvidjs3CmbLrMG3fY5QrXnsDgq6dC01FADr8PdBNPNckBcQBBFLTOSiF5hHYIZikOQqBPauB7wCIGyXGowijGe_Iys-h3uCTGUdcN-RIIMscr9uCj5JMEttnZnLyLXPvyb4kBEP3pmtp7zfPsAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
دو پست کریس رونالدو و لئو مسی در ایستاگرام رکورد داران بیشترین لایک در جام جهانی شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24366" target="_blank">📅 13:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24365">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSqXblyGip1ZD3kSVb2nlTRJHm2rwdLkXEftspaif0i-ylChIbqfL-6qYbHxyT2j3iT3J0FwbEnkwdoPdIk4PU0__KnQdGLO5Vjb2PPnejia3gz_IkyUBemmiffl27oWBoQZ3-CeJuSTAi0oo16wJsZ7moeiu1Ro2e71RSVbvce8YDb4-tNth86VA75L2QU3sT_VUpfEJhfPK7yQLgb-KbulDu-zJ6RSbl15y4ncM-cq5cHEHodbP12VmEJK5zy-wGBHtGFEaeVqYFwARL2hoqS6_tLdIOrgE_CaW4o7jQpLF636ZlRdGLVNJTvGrxthnkkqmtN94TXjLF6AC-esmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇬
عمر مرموش ستاره‌ تیم‌ملی مصر:
ایران تیم خوبی داره بازی‌ های قبلیشون رو دیدیم اما ما اینجا هستیم که قاطعانه این‌بازیو ببریم و صدرنشین راهی مرحله بعد شویم. بنظرم بازی رو سه - هیچ میبریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24365" target="_blank">📅 13:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24364">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VsmGD90uSrkJxcnd6HfosMIpTSii0Oamm3_OzWb8vlemJ65fv_ppaMuQ_UIQVqylBZ9Gu3DQkYMXuCsK5v-RjkRshSX2f3ReJRUPig-kILwGZt63xylwyVKg8jyX_W8NvrTS9h2subyzq1ecmqs6cZDZ_eTSaO1wf4IpR1unJTf0zIvxeLz1x5bW0VDQuYlTKc6GUOe8sd8yo0viY565T_eHftCwzAJKEAyzTJj7w83fzRBVWIjp2bymJonw7G1ZPyec-j9wjwdLSrwTF_v2IghrA0MCU3hSyJR6wYaIl9n5bLnZ2KGD0--2Ghl1qq1JpD2-3SWduCBjQ6z2F8jhng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇦🇷
اسکای‌اسپورت:باشگاه‌اینترمیلان آماده است برای‌جذب نیکو پاز ستاره‌آرژانتینی‌رئال مادرید نزدیک 70 میلیون یوروهزینه‌کنه. پرز با دریافت این مبلغ بال در میاره و قطعا ستاره جوان تیمش رو میفروشه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24364" target="_blank">📅 13:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24363">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9rEE5GZJzxrvMgoKqK3gU7vLFyaOIbv7jryZpUwZUbacpE0aBvMMuPWy5eSzNdQgH3KVXT2RYQH4_SKAWs10oG-ZslnH2Uo0WdO0wnyOrtiN7SMaqfg-up_hAaNORAndo1GOa4jzl0L2p_RvT1qVLdZSJu36vaVlHvsKJgJIpxIPFchHyUrBLczfJN9MwN5p0J_uttRB1Q6x70NoB9oxU8txzCEi65p45XOF4pa7FC6Co5Y-4WFOqDudUUv10gE6-42IwoIitmF7jNeahG11DwQe7upUm5BjEYsK3wxU2lMNJq5pxkC1aBrHLD7WC4pJhJkGmjY6s7pTC9cSTjoPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏰
بخاطرمسابقه‌امروز تیم ملی والیبال برابر ژاپن در لیگ‌ملت‌ها؛ بازی‌دوتیم‌پرسپولیس
🆚
چادرملو اردکان از ساعت ۱۸:۴۵ به ساعت ۲۰:۳۰ انداخته شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/24363" target="_blank">📅 12:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24362">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLxgFTGUkOvfI99Re9wUhdy5CA_Bdlm6sFMrK7xt5Br43d_ujKVxn4twB1rU1Efh1-04coXfmNdSxNpErzPdpkvrSf5WPXjCcnil_POG44vOREMEqOgJ6jpFoTBcB_77v_p1DVSl5pToOvoLMxehHuvtDaTbHg8JvrAU0f3uWOgmK7YoeqJWXluFvdgi1LkVeNhQRXDsUUcHIZknzLIrfgoGUhms0J0D6CpJiYo7cv6VDCOCJ2JiP1zKssoMj6SOFkpZAAotlBXtxIrdSepJS5-9RRrbiyDrtyPONwHCHhRKibZwO3YzOQN2wKjJR1slZDTVF3TtxWgglpjrGL3LIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب‌احتمالی‌پرسپولیس برای دیدار امروز برابر چادرملو اردکان در تورنمنت سهمیه آسیایی؛ 18:45
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24362" target="_blank">📅 12:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24361">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GG7-eL1uhCrze_XXz9XP5YCTnOJhLYPouKwCMlqHaghGJPcSLca9Qcbw9VUcCXmW4WX7S3NyI6CDknYJ3vJ0-2JQ2ge4A-GIs176EyHmTUvBZ4088RhNhhwGCq8ZnGdMDxJu9ABaTpHy8Yva5JRm-X70nTWsCKmyAXY9t_MkSuB92_zOQPf3ecHoU8oM2mJjSlMWdaovsEKt0DBo_J69Ita6vcKOsaKDkzLREIUk5C0s2lw_kJY524o3KYipcHAVARSHcKJOENmitdJFwONguL-Jmv3oe3lxytsB4m06MU3LiRU6sA72rTWeu9JipV98DOt1mL9MmwUbPXECJ8VFDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فدراسیون درآستانه‌دیدار فرداصب با مصر بیانیه داده و گفته‌رژه‌همجنسگراها قبل بازی رنگ پرچم کرنر و پرچم‌های بین تماشاگرا و هرچیزی که مختص این موضوعه به ما ربطی نداره و به اجبار فیفاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24361" target="_blank">📅 12:28 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24360">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b03de0d7d.mp4?token=MN9W9zGFc35SK97XQ2csLZXh1YQQhtAQ6Q6hDEvU_GlXiKrBpuG85BaVjJ1-DSMv1Bwnl-SFrtoBdZSfROi1WPUqe30fu9yJHeQvDPe4pCzHapRNl2OSdLCr_8B7WPNfHBlI4VqzOdZIt6wfKbsp-UjA65cv29PnXP6xzrBBAt6LItW2yR5ixxUC-aaQnKUxAN4VtvxKwJewc43vRqEkcdL9bKjpEZ-SIYjHhQTHzZbhAbt3j1F8HbY3ZcKrb9R4TMA3RxQPG491uCv5a1TNXReyes2iXsLwtUkXOz6YnqhEaXNF-vlqx2w1vKnCvQ-6ZLZEMAjZghpjA1jhWlUR_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b03de0d7d.mp4?token=MN9W9zGFc35SK97XQ2csLZXh1YQQhtAQ6Q6hDEvU_GlXiKrBpuG85BaVjJ1-DSMv1Bwnl-SFrtoBdZSfROi1WPUqe30fu9yJHeQvDPe4pCzHapRNl2OSdLCr_8B7WPNfHBlI4VqzOdZIt6wfKbsp-UjA65cv29PnXP6xzrBBAt6LItW2yR5ixxUC-aaQnKUxAN4VtvxKwJewc43vRqEkcdL9bKjpEZ-SIYjHhQTHzZbhAbt3j1F8HbY3ZcKrb9R4TMA3RxQPG491uCv5a1TNXReyes2iXsLwtUkXOz6YnqhEaXNF-vlqx2w1vKnCvQ-6ZLZEMAjZghpjA1jhWlUR_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیم‌هایی‌که‌کمترین‌درصدمالکیت رو درتمام تاریخ جام‌جهانی داشتن رو ببینید باحضور افتخاری ایران
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24360" target="_blank">📅 12:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24359">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZeAaEiMnt3ZK86tuqiprmQSl4gNeIxSLxdBRUjf8v26h7uOM7DHqwrtoM9ozhcBmAqO76BqCavSyBCR1kmjCxattUcNyGI9G8YNgwJKyoqzF4so2Zi_eRNV1BwV9qk29JL3zrZnPZS-X8UVDWgOJGdT7Sj0fjO3RjH_mLYajZhWgphaouPWxHzqo6s7JMrbhO6ZW7eRv-ABY4wWsP7e9rqUeQEq6cMvitHL8cUkw7wlIj-nfU0HCwPQi8y1ilrK1HPblIwaGmuk5d-JXN_PRu7lLJEK-L-JG-lDROr1OnF6AUzzyV-i8-_9iZS97aYkCy_0fQP-0b06UQxLWFblIVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخبار مثبت 18 و جذاب جام جهانی رو در پرشیانا آنلاین میزاریم. اونایی که جنبش رو دارند اونجا هم جوین‌باشند. ادمیناپست‌های خوبی میزنن.
🫦
🫦
🔘
@Persiana_Pluss
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24359" target="_blank">📅 12:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24358">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DoVh9ztsQOY9rSNTj5Lpcpz-vSbT01kHhIFHXEQcNsWStzSkgF9FgrguYd8fgdaXhuyGL3oZI790zNDK6IURqLqVPZZM1MEnqcZuzWctWf3I4ycieGq-wFOSIXsaVa5MEbjw7_ilg-B37ioSRuYD3a_elNXd0O1fQtA0fZ8KX1eYxSJXyw_ne8m8jG3qpalaRsTn6GHXxAThUHGAIa-FAqHq7u7jIwThMeyZ0aRyT7eYu1KCaXBEvNEY-XLNPYA3uV-u831N-40hkCBkRH4kKe79WumyGNdxYAjyzA6a6FlHZa4Q-F30ZeDwEhXjren5VVT3ukp1vFR-Gu1oPdsWNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تونی کروس: دراوج‌فوتبالم و درسن 34 سالگی خداحافظی کردم تامردم روزهای درخشانم رو از یاد نبرند. موندن نویر درفوتبال درسن40 سالگی نه تنها هیچ کمکی به تیمش نخواهد کرد بلکه باعث خواهد شد که مردم روزهای درخشانش رو از یاد ببرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24358" target="_blank">📅 11:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24357">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLxn0uNUS_b2OJL1TlWyqlS3mrha0jaVaJFurzDo1Y8Ripj3bo_IKU2Y0JHnftkBAac8J-SXQ3gwJGcRmkTg3KZdiIw7dCEaRabScBzOEURBuUY7kB4a6ZnkyH-Yxwc7TjlyG3QRIRR9Df0fmlOPm2sxN4pFyf3RVGXbMoyXVQ7idkDygbzOF0gGAYj2ot52tyzdNuJaHQozb-YU_TlGMPBJa5GKgZy7v7S25Fp-3tiECNkiJy9xvM7nifKL898xwPC11dBETZ-G0VLiqpwPHnpfmLOCv5HDD8K6GVswM1xrUsjhcfz9KUjg6THzlRm9C0F4PjhcOJo52d-yMYUx9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
الانگا بعدازمساوی‌سوئد باژاپن خیلی‌ناراحت بود و فکر میکرد صعود نمیکنن. بعد از بازی رفتن باهاش صحبت کردن گفتن آروم باش، صعود می‌کنیم. پاترم توکنفرانس گفت بهش گفته بودیم مساوی هم کافیه ولی یادش نبوده. بهرحال‌الان می‌دونه و خوشحاله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24357" target="_blank">📅 11:26 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24356">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMMYd9IFH_LAhvLSUFcx51RJR_xxN4_xp6cox7LSYuK-kFc7YdRx1HTlxxN9jIFN_slPC3erlGbNBvXHuwnznFaY46g--hMZ7QQs8NcUvIAwrU4JSzC2EK6tVZ22Ezg3tgCBZn5frmLGKt1wiQlp9DzbXi-yGqqFjelchgJghaOm7Kuczx7BAilyYoFFxcSM4jw2nP6FXTDxuEjLx4KrVXJBhYaeQdJP1i5KnQ-YAZzI-9kf-AHi1LxwQT7mRw9cGItzStHUQ5wzn0y8c5J5dhGLgJrXI-I3v5x-FgEvn8889cpYaMzfhiFKv_H2CdZT9VUA4dKYpeuj-lBdCZhacA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
ستارگان رئال مادرید؛ وینیسیوس، امباپه و بلینگهام در این جام‌جهانی در اوج آمادگی بوده اند و ۶ مورد از ۷ جایزه بهترین بازیکن زمین را برده اند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24356" target="_blank">📅 11:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24355">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-jESBcRCkpRXysYhZQQWfnqjj9k5in1KiyDTTWD_45Jxbmw5ky7Aq9i5P_NAhw6YR3mhKM9Vc9eifpuyZYT_RnqdA1u8tixJUEl5PK1nhNKRByRxgU_si0U94V6FCIAY5GJN88UKyeSVShzQPSRnM3YTnhaFry1duJ7QJ1mqQwIE-iVsxwBlrz9Nd4E75AreAjmkB7dTqIJUIzhEJWLSSB0Fsg4pec9OE5ECFa2wd5RZFGdFcCzl5kXic7y-EkLkZlZfrQc8bJdvRX41sLZ_Pc9WxIg3TmGMklBSFRCLcmGLn-WkhDcQSrh2f-WaqGRrUxBUz8Kz6SHbLbWwk8mEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ مبین دهقان هافبک میانی الوحده امارات از وضعیتش در این تیم رضایت ندارد و به‌دنبال بازگشت به لیگ برتره. دهقان فصل گذشته قبل از عقد قرارداد با الوحده در آستانه پیوستن‌به تیم پرسپولیس قرار داشت اما عدم توافق مالی دوباشگاه‌مانع…</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24355" target="_blank">📅 10:24 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24354">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0e3e7e8d6.mp4?token=hd26wIRlH_qzzAK6-iIYUjrhpGUQ1VzSNSyuQWHcRcx9fAZ_zHt2jVZKNcAmaOtc151Gkfmg4lDvrC0wBIOcRs2sV64XZ-nwBEXznDYJGwH5h7USj23DuE15ZktbOt0_m1CekMnNdPE44XNy-QuNDLTKABDOGk8AJ4eI0c9ZQuDM5Ue9UJxbj01Fuvkns3pthAYMe6JSbnAIQ8YQNNCs-IXpmjC3k56FhLZojClGsKOB-a9oynsrsoLJoTmBpHfMMVysav7yIpwsihmFrjO_m-wm2kvlLMkD42CiK6v8-zQImQ_QO_0gqPb4-2shDWhrmNo0ipoSqgxQzGxaFakwwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0e3e7e8d6.mp4?token=hd26wIRlH_qzzAK6-iIYUjrhpGUQ1VzSNSyuQWHcRcx9fAZ_zHt2jVZKNcAmaOtc151Gkfmg4lDvrC0wBIOcRs2sV64XZ-nwBEXznDYJGwH5h7USj23DuE15ZktbOt0_m1CekMnNdPE44XNy-QuNDLTKABDOGk8AJ4eI0c9ZQuDM5Ue9UJxbj01Fuvkns3pthAYMe6JSbnAIQ8YQNNCs-IXpmjC3k56FhLZojClGsKOB-a9oynsrsoLJoTmBpHfMMVysav7yIpwsihmFrjO_m-wm2kvlLMkD42CiK6v8-zQImQ_QO_0gqPb4-2shDWhrmNo0ipoSqgxQzGxaFakwwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇪🇸
ژوزه‌مورینیو:
من دوست دارم بازیکنای رئال مادرید درجام‌جهانی ببازن و برگردن به تمرینات تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24354" target="_blank">📅 10:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24353">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇵🇹
🇵🇹
سوپرگل دیدنی نونو مندس ستاره تیم ملی پرتغال دربازی‌مقابل ازبکستان رو از نگاهی متفاوت ببینید؛ همشون فکر کردن که رونالدو میخواد بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24353" target="_blank">📅 10:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24351">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NDKvfbthWLzCIM_ozlm2aeB59zzvyNuLyw_VHR7-mcJlVL4WRXlEK4xaovBsBXtouM0VPCbY8oaC_C8L1i8EPxgA_ffSKkWZizNzEIKMCsj174xY38Hgl5KB7QWumdqNzUEXdE9fZnt-QWW3X6s_AsLrv5zqdfPSsdwt-kcJIuqsPcrV3bKQwynuaUw1s1DnzrsICZO3GlU7OIqPsP_piAgssLrP7TT4A50Ep79PyJSRV45ZfCLBs7SvpVZY_f-i515BBGymYhD4DLa_6MiUhrYZ4p3b64sJMRk6LmVDiu4JovZoJMdYlfMoobo2DmLUJYs0LL7-MS2t-U1C285WpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24351" target="_blank">📅 09:39 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24350">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LiAoa0aEp-cUyui119yZwUE4xA7on1Aml5RdXFZDz8H8DJPbR1UeuzqnPpUWTASayeyc0drbMZfJyh0xbXNSvjs51VfTU6MTBHvRpHIdG03JATMWo5UHgFTeuAGfDwS3j4f_X6i_5GB_-kiw8g0T0NFHo4g0gxqw4ld57dbT6QF1u3zOTHEZyW4g-h15nUP-GK9XMoK_spJi9NLcKcij-8SPgZiz6lX6AyYazXV51IggcLz1fvPy3xTijyH2BQc73cH-sje_UHDbMPU2VGvm43oWzKOgUTAoyXhMf7KCXAikRmGpz3KxMVs--76Z8CAmMpZLWhlDGtaYEQ3YyhSHuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله حذفی جام جهانی 2026؛ برزیل در مرحله بعدی به ژاپن خورد. هلند به مراکش.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24350" target="_blank">📅 09:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24349">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7875374a88.mp4?token=M050ux-mivHm-Qfl5tUzdLiXoQ3AyPjNeY22cV5lrXyzJxX9hdRoeW5zyZSeJ3myCmo-IT8g6oPx9sFQ91lbkEf0rD1VMFZ-7w9eRCcOzS2QwibQlM4byjLD1vDiECqoFYOSsIFmYlTi3k5svJzJwRWGQF5OUZ-dL1K6tcKR7_r36gpzWe0-1B0YNkeMtnE5215bDtFOqfFswwf1GhinWCPFROcdZHEjQ04Y2xdOA3b7qTYHiJYfbB9B95tlINAfBku0mwbQIpJyM5FOcRDA0T9SNiRaiB7UAB3wYrx-dRJf5wCfQc6hQQ38I6622Q9ln6cllB7SA3icNNEVCTSfcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7875374a88.mp4?token=M050ux-mivHm-Qfl5tUzdLiXoQ3AyPjNeY22cV5lrXyzJxX9hdRoeW5zyZSeJ3myCmo-IT8g6oPx9sFQ91lbkEf0rD1VMFZ-7w9eRCcOzS2QwibQlM4byjLD1vDiECqoFYOSsIFmYlTi3k5svJzJwRWGQF5OUZ-dL1K6tcKR7_r36gpzWe0-1B0YNkeMtnE5215bDtFOqfFswwf1GhinWCPFROcdZHEjQ04Y2xdOA3b7qTYHiJYfbB9B95tlINAfBku0mwbQIpJyM5FOcRDA0T9SNiRaiB7UAB3wYrx-dRJf5wCfQc6hQQ38I6622Q9ln6cllB7SA3icNNEVCTSfcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
نشریه ESPN: بازی دوتیم ایران - مصر در جام جهانی به احتمال فراوان بازی حمایت از همجنسگرا ها خواهد بود و فیفا نظرش رو تغییر نخواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24349" target="_blank">📅 08:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24348">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rfTVnGNiRgDwtvLhb6XuT39sbSfNgzSIHgJhkbPm5_GB5ydEUbW2FRIONWgBW7OFN8jtbvjPNueWqyqGZvNLIYAw9XfuXDdUXO0WM0m55Xb4PxoMoY41HyyOzsumrP7fXhcTlGjMokNExkOybKeDtERGKHurqqtrljHor67f8xdaYfVheXxZyrX3VWpSSLSq0ifENT0Z6bxgLVVW-e5XbYtyPoHsy2d59T7RyrV4L0c48DpaMRndq4z_gQOmWysCdY6OhvYQNUzDva6uvkh-IAZDg8tv83K8f-02Z0aE9OeqGv73cz_Df0_axmIAcoCOwDqZUklLOwCJSip9FwJx3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم
؛ ۱۲ سال پیش در چنین روزی؛
آخرین حضور جانلوئیجی بوفون درجام‌جهانی؛ آتزوری فقط یک تساوی میخواست، اما ضربهٔ سر گودین در دقیقهٔ ۸۱ همه چیز را تمام کرد. کسی‌آن لحظه نمیدانست آن اشک‌ها اشک وداع همیشگی‌بابزرگترین‌صحنهٔ فوتباله. پنج جام جهانی، یک قهرمانی، و یک خداحافظی تلخ که هنوز از یاد نرفته. پایان یک اسطوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24348" target="_blank">📅 08:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24345">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mp0_14gLXAZe6d3VOQZRQ2JjkVdZpdRQzJflP6vzki-_vSvgKNMNzod9bL7arN0Zr__MDJeX48zCY98rZS-h17a1vFBoMlSPOhUNj6kKQnPnFq3exjrGxQ-QnBOBmwKAiHJcXWDCN1xWytY8foBr2_JPIbHAFLtcoBcKCoiWRjuKpfx43JPPmOVvyx9RGL3XRodup2bXT-dL11S9PI7TeuYwV6bRD0Kb7H_J5ryEa8jgwfVcCaHYo9M1X8SA9ZC6Xv6ksQeaRfPMVidPqFD7Qh8TlMglqJG1v8K4-XXRGO9HAtiOwWgXn4nW6QsyozHa5KjanObpd3bWwnqn7vupCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول گروه F و D رقابت‌های جام جهانی در پایان مرحله‌گروهی؛ترکیه‌بادرخشش آردا گولر سه بر دو آمریکا روشکست‌داد؛ پاراگوئه با استرالیا بدون گل شد؛ هلند سه بر یک از سد تونس گذشت. ژاپن هم با سوئد مساوی کرد ولی جفتشون رفتن بالا.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24345" target="_blank">📅 08:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24344">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQpW0F_BG_UODsKS1eDcDyhyc_TYt6ynOUMTSk1TgwKaFnmbboVs-VMITD3Fz2zdDQyVcjdDGJjgTp6m5Lcgi0OvJ7wqs05ZVHFJ08KNgNLEvTdUn_MZ7evxc3lEfKhptSj8fXVR5kFhvOlfZzEmfcGk08KkrP_L_CCXbmHPSeYeGU8G1BhZuFUHXbuSDp6ZyHnmW94oCihRA21GzAmkPir8dXuPgie_sKUnO27ixRz4sUh_VPWqi1MzR4oWoWrF6egrFh9dVj8sbXCLXMRjySC50DXZnF5ami-jF5UCFs35Y_zXUJv2rQMLxUFj6lvvyeEVHAy9gaxQn4cPqSIpxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌امروز؛ از نبردآمریکا مقابل ترکیه تا دوئل فوق‌العاده جذاب یاران امباپه
🆚
هالند
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24344" target="_blank">📅 08:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24343">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GN4VeaDYIwGZXUwDOGEpWO4PUlVfN8JnoahNopDtC14NHH2IpVkvhd9nkkVHRp9aJxddDBeny2GuCVAkJ-rKHK6cVqD8tOs5-GfqQrD0lXoJ31FSuq3VHo8P-097i7GBaVLCpEciSaeJuucO-XhLzA1lHM2PVAbZCPdrtP8B9whuelK-6AO3hheA5gUStdLEiThr_XmCqsQx7zmJgUNhcfq64dTHZAOpK_OVWjS6nB9qi-2dvb0ZDbeknFR_JGvYMx1AvAkEwvfKOrwoYgLhL53JQh_VoVDguxIMNaCMr3KBhUCTtagSx7fQBM7uSo4Nkg1iKG09Pj_DIOJ26UXZzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
موعودبنیادی‌فربعنوان‌داور وسط و وحید کاطمی بعنوان داور اتاقVARدیدار پرسپولیس و چادرملو در تورنمنت سه‌جانبه انتخابی سهمیه آسیا انتخاب شدند. این دیدار فردا جمعه ساعت 18:45 برگزار می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24343" target="_blank">📅 02:10 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24341">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwYbtibwLoBaaUUz3HL5RMiwhjih7bTNT_57G_c6fYWOqzfz3RRzFIMdEBkSu36SiU7Jx3juxguWpqVpqCzgYl1FB2M9WJW2gXs4X2LBtAwAN0Vqg0XymkXGj1Ay0BBewLE2LCYVJFfhlI8Ftn7urWIKGOy357mKXuMCwhU5gaLUupXOBrFL_ML5Mf7TqVP4Y9FQ79U7eRcAdo5V1ot0uAAaN0M6E4wHN3r0fhuz91Qo-jmFXIz96MXIa-IjZnnlAwGyZu2QJEL56MKnXnFMvCaYK-WoKzK76CE7X57O9c4lyli327L2ljeXJFk4CnkSNe6GWFh87aRQNmznvNFVTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌امروز؛
از نبردآمریکا مقابل ترکیه تا دوئل فوق‌العاده جذاب یاران امباپه
🆚
هالند
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24341" target="_blank">📅 02:01 · 05 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
