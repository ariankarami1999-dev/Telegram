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
<img src="https://cdn4.telesco.pe/file/fG3vvJuw8T0fTfzgoZQSwspEbnIiHj6b5SiEaW0aWg04oHDP7d6U2G2L7jAdOlA6vS4QA7a1-vZyMFFrPtFdItfAiyqSl5N7WVLPoZibzYwFJm394cS3r7peijNEgrhumMIzkkCgHwKgn6twj8M2_JdUoriEpI2Hg5WEiuUThUVPAqt2CgzibHpFYMyIHKYRWyNRL3e8PHMT9qf_GstdYDFbQJHdteAIhYVsmC_4mlgTrxcPmBIH053i9w1OkA_KB1GRnlCH_ANgR6Wl1c46eyhEAo9zxmPNha5mg1Mu8B2a4qb3wIG4bQfU_6V8pIUBPMjpfJ03G2pgdjtARIzUrQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 14:01:43</div>
<hr>

<div class="tg-post" id="msg-453100">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hIOz6Z5fTckZ_ip4otdMMCJko3BqIA3bo13k6iF0OYjrWRGpukoh3KagyhbWkxU0myfctmAvbdEYd4nuxqhIiRFSYIQh_kqT9FSW2D5eOSjXjPnNNsLv6j375R5iHVsgNtbVVXtm4B4kVepHLZyBuGcjX_C0s4h_fH7dcqrV0WHwL5otseHqHfBbBGa7DqDuRll64KDnD_j4xiQOGpXTnO-qglQF6EHY7JG7CiFCMTWg2PbnnGYJ050_pkclmKEMxHPQ7eYWPHYxLIT9qsEt4x1IEvA46wCNJ6TameKzEZeXaZgU_N5MUZVf8miOmqwKxmMCMdPgjZC_h5Zlf2oR6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف: تأمین معیشت مردم در دستورکار حاکمیت است
🔹
لازم است مسائل به‌صورت کاملا تخصصی در کمیسیون‌ها بررسی شود تا خروجی آن به‌صورت یک کار کارشناسی شده به صحن برسد.
🔹
برخی قوانین را نیز می‌توان به‌صورت غیردائمی و برای اجرا در مدت چند سال به تصویب رساند تا در…</div>
<div class="tg-footer">👁️ 2 · <a href="https://t.me/farsna/453100" target="_blank">📅 14:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453099">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MLxy-KyFFr2Y1APSKYyOanCzHAL0ONkZPjKuzU7vUsIv4-sgk8eyQ98us8riFGx-N33y9MgryWwNr2j3Xl9UfiBDXAdtE9mEjdi-yJXkaLSWcZe5N8XZV8nP-sWocKd7GlFPcT6klkjvwG3Bm_ZElyc9cg554wI3Y3r-EEYUfpGjJKddwUjKzJzmMDnfD0QheOG2NSOw3vnT4rScyeObgt1_iMM2-wjWsX_yrIwPPlNyC_i-AHcMFG5xj18lj8i_r8T58K1TgQ-2G0TIAskK16BriBuHbJz4vokICSGP1RAD4EdzSwJgUOcc94aHseizb2ZFsmCm8fRFPcGqNCjS7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزییات جلسۀ شورای هماهنگی مجلس با حضور قالیباف
🔹
جوکار، رئیس کمیسیون شوراهای مجلس: در این جلسه که اعضای هیئت رئیسه، روسای کمیسیون‌ها، رئیس دیوان محاسبات کشور، رئیس مرکز پژوهش‌های مجلس و همچنین معاونین و دستیاران رئیس مجلس حضور داشتند، گزارش‌هایی در خصوص مسائل…</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/farsna/453099" target="_blank">📅 13:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453098">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8G1T_FrXR7q8nfYBqkGMxNgKgZpNSX5u4Bw25oWM4iXpStxsuXdNYSDUq4PMs1D5bGtzbtVmbILUH8FtAx4MDmAHyjyYZb-xyRbirdkGZ__V3GrjLGfn6zObm795jjII5D1I4HrEwEHX7zbG2AO7JvhGXt3BUFMI_TpFrI8IMNHlJB3Sq7knWyh7wRnMeOVSYhtJpXLfE9A4mrIUqv_Zk2Ks3tJjYPFfCsujXy_oHin7BluyU_b8_I97ZvtdolO9gTSNVKypMzVG-zchF2Je6j-LNUOPJT-BSd-iJ0B1dz4pVPF4ht8uUptsYl2wtaMxBGWiIf6haoYkxTZY-mDeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام زمان مسابقه پلی‌آف لیگ برتر
🔴
با اعلام سازمان لیگ، دیدار مس رفسنجان و صنعت نفت آبادان برای تعیین هجدهمین تیم لیگ برتر، ساعت ۱۸:۴۵ روز چهارشنبه ۳۱ تیر در ورزشگاه شهر قدس برگزار می‌شود.  @Sportfars</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/farsna/453098" target="_blank">📅 13:16 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453097">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b178446800.mp4?token=TXAOjN3zn_kFFjTCBtPSxn8bd-M4FoJarxmkA3zFd1OPCzmxTmB8Ixc1gmBM4UwFE4LmVgHiiXciLjrrre9P_DXQP4SkbkUcPYTtLyFsAsdiuWAJlXfN6HwGvO6NuojqpSdgsmKoMDALmoRsim3kqAM_YTbeeDO7iZFSqjwUyRAU3bERhk-znqjX1s7MihQ8H8FimxiDtHmA18l1SSEw_lK_338K_50ypSSuxjrfPcHAHYdT_XRPyWJ74OHJqw9gIvXaOOhHnGcKEjGQpB9DSmHvVtAB5zWSYXRr-WkXsPnRzWQKxsiiQXGEEv_3rHPaDQQ2zPLNs0qs5155cTjFpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b178446800.mp4?token=TXAOjN3zn_kFFjTCBtPSxn8bd-M4FoJarxmkA3zFd1OPCzmxTmB8Ixc1gmBM4UwFE4LmVgHiiXciLjrrre9P_DXQP4SkbkUcPYTtLyFsAsdiuWAJlXfN6HwGvO6NuojqpSdgsmKoMDALmoRsim3kqAM_YTbeeDO7iZFSqjwUyRAU3bERhk-znqjX1s7MihQ8H8FimxiDtHmA18l1SSEw_lK_338K_50ypSSuxjrfPcHAHYdT_XRPyWJ74OHJqw9gIvXaOOhHnGcKEjGQpB9DSmHvVtAB5zWSYXRr-WkXsPnRzWQKxsiiQXGEEv_3rHPaDQQ2zPLNs0qs5155cTjFpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای پیام خصوصی رهبر شهید به فتاح  @Farsna - Link</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/farsna/453097" target="_blank">📅 13:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453096">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tR-oKl8Dl27U7KsdfK_LHZM4nbMHekopGRwB4b-74wmcdFTenOOx25fHWm7BuE8DlWa6NJZXLrxJH0AKZxtBB_loPi1TOaCTE4G6uUAi__6iF8tDAWVlu1P5z9lz6QgaWMZw6zSTMlAzmvstJW6nc5D1LNkyhHgp8c3ZhdHsp7IB6mUVUpb__o4y1xdvWtRLZ0CVdniUzznxFcb2h9ERazJ4PpLTLyPFGIwZbZb8a3Y8S3Chyam-F7Yw4hXtmh7HzuAW0fQXxmQ5eXyQ6BfKtMP2xXsjHXEWlmRMKDyBNWK9-hllGgOcCC7-11iPwgbh2bBTiRHdYZrkn1AM6tfzBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
فدراسیون فوتبال فرانسه اعلام کرد زیدان سرمربی جدید تیم ملی فرانسه شده و تا ۲۰۳۰ روی نیمکت خروس‌ها خواهد نشست.
@Farsna</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/farsna/453096" target="_blank">📅 12:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453095">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9fJuO4-2yKnhuIUz11vUY-bakUX_NZHme0zALARyd-IPD89Nq3n6Zl5yDjM3U-HzAh3AwzQDxxr078WjDPnwyfq4p_ow5cy_jL-NYV2OFoq-mXNsRswDO3fskGVjBGn_O0f4gdv0M6BL8j6JZFEhC_CTB2nX2dfyVm8gtfRl54MtZmgL3Fz39V70MjgMCgG5zLXFbCPSHNIiLfUAVFgcXY4XrWj3BMarincI1JiS4S7S0GqhCTrbPHjrwGedNkpwStaEF2ess-so1Q2oopCr6aw4SOtf9h3uNKituctNJl97cZrTsDE59_9canoQ6Kd_KEPa10XGDsW6fup6HHvNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس از ۵ میلیون و ۱۰۰ هزار بالاتر رفت
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۵۷ هزار واحدی به ۵ میلیون و ۱۰۹ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/farsna/453095" target="_blank">📅 12:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453090">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rlcs9MEeBEdgC1WxKswAlWa1AqgguEI_Bp6UMLlTUeKebKxhUEm-tVptn7ti5KJ8DL2Hg-jWBAZ6diVcn71b7D929H8lwV-T-wNUiXwKHSrvx4FV1IeqcNh2PblRVw7pik3xeIqIwVhRN-X6IHatQM0eA5J9tSZH0qtjf4apciWzNXaP2jTU-FwBgCS6HQOOQHmKjR-tS7RphPPbOVn5jR8aAHKX9Ed-NYHBzf4EI9LX5Clp9ItF5zZGsOEhSLtmD_YSlF8psGL1deyGMNYUI6D66WtLRlzdXS7aIMo9KDwB9TEi1PFASpnOMaPhY1UwYBtsINABt2btt0B2uFbNyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JS3gZlPE2bmSXn0sEppaDQKwqk1vP1p-ajX5L8Nr38bYIuJV6WCIbl8IfAIjp1haumzD9l0mobTqyQPJ1jdHDf-PrJD6VDYjjQCaYbdPsphHOztimTTs44Q9Ji4BPxKIWScZ2ZeQZ85crBIQmMjCb8Bhd2Fi65oLYPoFk2TDfvVXGuCkBv-PMgGvhNnJj3i0SaShWc2A53j3Q0CbyVpDglRTA_rwa1HiPnKasJCardfqUFjIJLBBWWjr19ixMeaxWkr15f6iwnlru3CW1N_TZp6cJMxwffmajUxXf93O0gp5Ym2Ojlddol5Q70OWoD7Not3raAC6dzOGEHNpYz9czQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l64KZxuB86xomrqMNznyRze0d2HI6AgFRNVCklkZtX-FfJDKYBCNBey0BtdCuM2xmESoWX15jlGwJ0PHkG7oth1ICqaN7dQ_ahsUTz4Y64yEG1dKpTXb6m-j-1cPOfC0MHqpZI2mW8YbAI1askAvzxxz2ykD3tPxib2nyKhjAuxNHmuWYDEK2PyCu62qICGx9C4whGVRz-TIMfVyaihiEVhsnF_Udj9CvRbw_SB9A1d9sQzXhdtFSsZSRmvtEEDfqEIre7ma9Uy1LT_ai9jchVhEoJLTH6L_Jub3w264T0JNQro2DM6c1Yp5NpTXJMnA65c-TNg0V5MudnwMkKxiwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cPE8P68hC8QI_74IC7rSZj6pVEGbeTz6ntiTIfqkArDqVJmU-2A0THN46G5av4O9xw_FK6uPbt4WfzOLYDZdCZ5cWkcmHZEDA-yUo3cnbHd4TFFNbY3mpTDZiCUDhTctdihuLuJJV4VfoHPrPSbPDfBSzOsn7mJcfPGr3qiSl45h-rbN5c-HXPFTu0kibr4btqCiVw36fAou-PbldqS3ioLPXjIqfn7sV736IS9V7Myv-rnNeoylEo8txuhRUgMeyoLLrzqFE91a4z-729AJdgcBE3ALhpPAvXSV1_51xpKcktrEEJzve8DOhLbgpSVU_PrFkDNHx7TMuSaPf87ylA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cXHSTkjcpvq7zG06P8Qd5hDlYfBQI7-EHQnpFSFVn2jBQlbhrcgtp8dDtoPMl19pBVUSv5dCfZItSIypXS-mfYkgOJ5p9IjXhUAJm2SaOsl6WTNeCtWPwl2jC-Qm0QA4tFuMxBg0fIvrc7AQE2KrfGlDIR_3_4hUJiux5XeaYpqhSNKU8exkbufcbTL9fgea5_J69GHG-Z1gQD6ajmQw9sckyf_iuMWM-cR1lR1kffmqfuiPXn3NLf-3SJHqZ2MteSoRULER21oQaz6YYWfKlmAT7SPLyMkgJykD2bJFNSP6R2PeG_uyrf5zOESOy7mXXLhiaGCF21gCMie81uLx-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
هشتگ
#یالثارات_الحسین
در شبکه‌های اجتماعی ترند شد
🔹
در آستانه اربعین حسینی، کاربران شبکه‌های اجتماعی با داغ‌کردن هشتگ
#یالثارات_الحسین
در شبکه ایکس (توییتر)، فریاد خون‌خواهی سر دادند.
🔹
این هشتگ طی روز جاری به یکی از داغ‌ترین موضوعات شبکه در میان کاربران ایرانی تبدیل شد و کاربران در محورهایی مانند تبیین ماهیت اربعین حسینی، خون‌خواهی رهبر شهید، بیعت با رهبر معظم انقلاب اسلامی، تأکید بر وحدت جهان اسلام و... به تولید و انتشار محتوا پرداختند.
@Farsna</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/farsna/453090" target="_blank">📅 12:16 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453089">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0T5NMGbODD7yvgasN-kRTBkGY6vXQIF1fhhYyJgt52th9tCPPGRRyuX3KuB6P3eWm1_nnJDCEnhnXfFJB1dr5yix7NHyKCwPsy_xfNOjNscXtDcMh-o_-N6w1zbA0lyCYE7pnxP7WbqjMGngynxiVs5ehw3ryTvMbo6hDi8iovM6IepziVZAGNQGDVhISG5fub8YSAZBqpQSkPdBDaWNa7snKCVpYfwcilsuLcRr_fuULKeKUbJ6_juyFCGYFJBpDXb-vf3872CFYWYiaJ94WKWIRovGstvUlEKYewQq44mAsR-8iScUzEKdFXMYYzW_qxsLqAs1rFtx-WEvl8oHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دینار تو بازار کمه؟
🤯
هرجایی دینار نباشه، توی دینارز هست!
خرید راحت و بی‌دردسر دینار از دینارز برای سفر اربعین.
🏴
@dinarz_app
🔹
نرخ و ثبت سفارش:
https://dinrz.ir/ix6
🔹
تلفن پشتیبانی
۰۲۱۲۸۴۲۸۴۱۲
🔹
پشتیبانی در بله
@dinarz_support</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/farsna/453089" target="_blank">📅 12:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453088">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/farsna/453088" target="_blank">📅 12:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453087">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FER0P6RPj4yYA9zJWVWSANPwcebvEKFBlXehOYM-bgyoErQeYvljxxnw_SAH9BJvbXaXhJiWMjnxhfUeUZnSFJsxHklyim318ytX7kwrQfXlfOQu2spJaEC_H7vTSVRHW9KCPnghKvsc2_ZPj9T0dBLNJZGr3nH99zfhdWHvIzKlKWPz1uLRn1tsjlmIaawFSX6xZSBAlrd8Lw2wIEgxm83baihn1jQJfjucE_9m79Hf8aaPP54uBqk-rzRLgEX_EK0VltGI6pVw-xfBwx8XMhm4D1NqJJgvHfqqaHETVahzxLP2ciG5zC2F4AhYooACj1MW8WHAg7bgs-279_TnRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوران وقت‌کشی دروازه‌بان‌ها به پایان رسید
⚽️
فوتبال انگلیس در فصل جدید اجرای آزمایشی قانونی را آغاز می‌کند که هدف آن جلوگیری از استفاده تاکتیکی دروازه‌بان‌ها از مصدومیت برای توقف جریان بازی و برگزاری صحبت‌های تیمی است.
⚽️
براساس این قانون، اگر داور اجازۀ ورود فیزیوتراپ برای مداوای دروازه‌بان را بدهد، مربی تیم ۱۰ ثانیه فرصت دارد یک بازیکن غیر دروازه‌بان را برای خروج از زمین انتخاب کند. این بازیکن پس از شروع دوباره بازی باید یک دقیقه خارج از زمین بماند و تیم در این مدت با یک بازیکن کمتر بازی خواهد کرد.
⚽️
اگر مربی در ۱۰ ثانیه بازیکنی را معرفی نکند، کاپیتان تیم مجبور خواهد بود یک دقیقه زمین مسابقه را ترک کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/farsna/453087" target="_blank">📅 12:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453086">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHHS4we30JUyfXsxAhwxC9edlVhZmzvlBLw1YSPqLTRCYUhIS2HTtVt0Nfm9oWreQFgmGEntfQrQgot3xCr7vSChhUyeSizQ9BkjNrV2F2JaKeWA_hCvwAJgzcvhvbUlDDg911gzxjHy4EX0IcxypjJgNIwmbFb4lv_xpIK9OGJbKWJPG5WiwugH_pOj_peRBgDl5oMqt6JC1R-wzQJrTXVx3O5ICQeTIn2HNwp_4ski45Lbz4w0d9MP0DEuJfnUMFi3rONkr1T6c6lyKbfM9dt9yF7AJGLSxZXKOBjSgAhZeqUji1We1-AeYlldtY9M_JKrHT2iH32BC5rU_ULY7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کریستیانو رونالدو تهیه‌کننده و بازیگر یک سریال فوتبالی شد
🔹
فوق‌ستارهٔ فوتبال پرتغال پس‌از پایان حضورش در جام جهانی وارد مرحلهٔ تازه‌ای از فعالیت حرفه‌ای شده و براساس گزارش‌ها، در حال تولید نخستین سریال داستانی‌اش با همکاری متیو وان، کارگردان مجموعهٔ «کینگزمن» است؛ پروژه‌ای که «دیمین لوئیس» نقش اصلی آن را برعهده دارد.
🔹
براساس این گزارش، تصویر‌برداری پروژه در لندن آغاز شده و قرار است چهره‌های شناخته‌شده‌ای از دنیای فوتبال و موسیقی به‌عنوان بازیگر مهمان در آن حضور داشته باشند؛ از جمله تیری آنری، اسطوره فوتبال فرانسه و دیو، رپر سرشناس بریتانیایی.
🔹
این خبر در حالی منتشر شده که چندی پیش وین دیزل، ستاره و تهیه‌کنندهٔ اصلی مجموعه فیلم‌های «سریع و خشن»، تأیید کرد که برای رونالدو نقشی ویژه در قسمت پایانی این فرانچایز نوشته شده است.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/farsna/453086" target="_blank">📅 11:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453085">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n5oQU4yMXRmpg02rU0d59uW33vmzwAfroxgKP7aazziv9mVVpJ0OcuBbIht34KoykkBvOcc1JIoGO8qUX_zqLzO-ZtHC35xmS-GKZw7hpDMExHZ3wcVR6Ek1J9yFkPWWMoQ_w8qQpj2NKLvoDtDWh2ruzcnuCExD6BwnPAsx01aO0StDgpsn_V0mxflhupLoZG738UVgjAIYR37_bADoTrCjkJCnHDjXoFvi_Thd1JMrItW3tbOE9IbUZP8ribgQB0RCpIo1DBvREf7q0quGnbsx13yzoIUIY2k71JiVt5fjfNWJBGz45_0sZHPhsi1ZUWewOq9wuQUIo_i1eo3eyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزرگ‌ترین تأسیسات پالایشی عربستان از کار افتاد
🔸
شرکت آرامکوی عربستان پس از حملات پهپادی یمن، فعالیت بزرگ‌ترین مجتمع فرآوری نفت خود در بقیق را متوقف کرد.
🔹
ساعاتی پیش یمن اعلام کرد که با پهپاد خط لولۀ انتقال نفت از شرق عربستان یعنی همان خط لو‌له‌ای نفت را…</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/farsna/453085" target="_blank">📅 11:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453084">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/907d714173.mp4?token=HKi0uyEOgFlejFC-m5Utn7_pXQy42dGmFsd0aJObqV7ehwwOLa18NwOoVuAmQ16QnYeDdK-GdL2goAI8evJA3nSsVUTLSBInO1VezPv9rGG55XXgkEeboYG8WxFEPg51oD55vJxSpeFHID9-YUuEXJjj7moA2KBxa85pZubdiK0FqxM7NohBlA8fy6s7iXILcXKXWOQIyUYdr_ZapqqTlg0gbFfzTqjALyGqQ4FrERu7SmSREyV8gb9lcrKWbgvBgEvykLW7_TDlvEuK2KJ0CcvdSuryJV-EgCzno54crZVxXFPCSWfQNK3uuRYZqVVV2By01zbzIWqUDo7vXB-HOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/907d714173.mp4?token=HKi0uyEOgFlejFC-m5Utn7_pXQy42dGmFsd0aJObqV7ehwwOLa18NwOoVuAmQ16QnYeDdK-GdL2goAI8evJA3nSsVUTLSBInO1VezPv9rGG55XXgkEeboYG8WxFEPg51oD55vJxSpeFHID9-YUuEXJjj7moA2KBxa85pZubdiK0FqxM7NohBlA8fy6s7iXILcXKXWOQIyUYdr_ZapqqTlg0gbFfzTqjALyGqQ4FrERu7SmSREyV8gb9lcrKWbgvBgEvykLW7_TDlvEuK2KJ0CcvdSuryJV-EgCzno54crZVxXFPCSWfQNK3uuRYZqVVV2By01zbzIWqUDo7vXB-HOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
تصویری از خدمهٔ کشتی توسکا که ساعتی قبل وارد کشور شدند  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/farsna/453084" target="_blank">📅 11:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453081">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ugeUHeyh_OS3o5DxR6k6BZuG5dCZpuYxMFzyqtiKrDzHcl3eEBiLgfQkVn4j4jTFgTkok1BeWqUvWHMyTc7lmeCtYy6T9O2_DjT62Khv_BgPB2T9oSkuw5lmqJT6W5D76mtfoxBRGKQnYRtbofAnRpqFmbsKRNTQKpSJn22HYwnFJSYownkGRhWp6x1ablDgDdcZ0ObXofLkzEwlPh5Goz4lC8dFi_Rbb91r0Mb0Fmp048pwVn3sddxWfMkgcmwWRRcZRRuCxu5tzo_Ck6st_5N747EfRA7_QyTQCio7KaDbNfx3qB4eP_aK1SCFrw7ELS_Y69bpfxdCEDraSpRb0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XSB4zoyikvDNfE7wDdf3qwrMJjGd8Ajt-B8vBVJd3LCC_0tUsltcUwQiVvT5Z2swgXT5SB0_MGP8iMWOlQfxInnze5TB_2aPfnTPHJPuJ0anjJYLlHbwakrdqaR6Y5NyPbhem-u9eGzDpQYJpLTm0YtdsKCBMV2oGqF9CIdkNs_8RvWex8OTi_XEZAVchAuc8TNGgWIEHTwiORrvOHJBUA0JKQC_RBG6v-tMK-5uKu8nQFQAEny8YUDYFISCJAyyKyePG0jCGbv0q_16BPkMpNJgNV9sF_Rc4KlVUQAFC-R1zNlYGRfIM_i0ZuAr7LmRFwclgsHFhWM7Y7AYZXmPYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H0d9Wtcr70hKXJGgWSdDGWZTqyQU3aqRFLUHkUdzLML07Zpxak44C1N0uIXI5YetYrwUrZWqObUFW_8VL3HqTo4ff04maGk6Uxgc8VmfsOW3vEKMCvTYb2OgNsfuYQYtedKI5feAv3ezlI-tevj18AS6pIro0FdCRrRuAtXOSxI_8jZr9rykKg4_JvPut99fiqCmDRWGbFwIlHdL5CbAicHeuN1zd--s7GOAfu8Obq0OECXFmlDH2oLJsHPpZVZYm0yjCYQVUMnDX5TRwzkiDo2GBXhVH1VHQM6RCqF0i5W_lrptRrLzwj0-17toGtXLmH88SwD4LHZHvyWZPpsXSw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جلسۀ شورای هماهنگی مجلس با حضور قالیباف
🔹
سخنگوی هیئت‌رئیسۀ مجلس: صبح امروز جلسۀ شورای هماهنگی مجلس با حضور قالیباف، اعضای هیئت‌رئیسه و رؤسای کمیسیون‌های تخصصی تشکیل شد.  @Farsna</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/farsna/453081" target="_blank">📅 11:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453080">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H8elwATrHlDVh9zTKxDpVWaSO_kb8lKn4QuNcOTBvdY7eY8TTAQ4zlGsfIZawW5AUNfaPleGnAhPr8iBfQQJW9u5_Y8hCATMj712axKwlNJicPr81NOoI31Ci5LI9dxp5ACBS7gINpZhq4nJO0uqHdpzkn6sqwrWiMG25TZCgKJgSX6v8-cGwwOHvKiYSR4AV58beMhyFfYY_DrsHPI3K_sG8XL5KVjxsAZPnptAtssfaRSB8aTYW5LiU86nQNHbb-2CbHBIdKhjSEJR5PkxLIrfzAd04Rf0Foj1gX-OsmJg-f7LjZ1KOfgPLsJFIPYdod0H4-Nu_MvDKGLKcIAgQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اژه‌ای: اصل «ممنوعیت هرگونه تجسس مگر به حکم قانون» در همهٔ شرایط لازم‌الاجراست
🔹
ما در همه‌حال باید به حقوق مردم احترام بگذاریم؛ مبادا به بهانهٔ اقتضائات حاکم بر شرایط جنگی، خدا را فراموش کنیم و به حقوق مردم بی‌اعتنایی کنیم!
🔹
معنای تحقق و گسترش عدالت، این است که در همهٔ شرایط، حتی شرایط اضطراری ایام جنگ، پاسدار حقوق مردم باشیم.
🔹
اصل ۲۵ قانون اساسی دربارهٔ «ممنوعیت هرگونه تجسس، مگر به حکم قانون» یک اصل مترقی و لازم‌الاجرا در همهٔ شرایط، حتی شرایط جنگی است.
🔹
این اصل، راه را بر هرگونه تجسس خودسرانه و مداخلهٔ غیرقانونی در زندگی شخصی مردم مسدود می‌کند.
🔹
اولاً نباید بی‌محابا با هر درخواست تجسسی موافقت شود؛ ثانیاً اگر ضرورت اقتضا کرد، باید میزان تجسس و فرد یا افراد مورد وثوقی که قرار است به خروجی این تجسس دسترسی داشته باشند، مشخص و معین باشد.
@Farsna</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farsna/453080" target="_blank">📅 11:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453079">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9383d1d6b2.mp4?token=BAtPVDi8XJrF2DQs58MyHqbkV3Ygzuq9C4c41VbiaB0qdMGfNnmZpE_D7IEtlAbsv6BFnwJ2_dPwckilTXm-AKf3IdhUI7pnISVYA2Y_ARjRcdHtaJiS7wQdHpDxb_bVV3CWDSVZHp6JCvgTv3NBp4XpVm_9H2TD76hOKGqz-QTCFNqFcKqJUABKPlAe2FhH2ZjWFmMIngfkT7ZDJfVZTn8ZjNy8pNeabQM5-pTuE3XcWvabe8LtEX1YCHodRYQ0cbU85TNthDsqa040AXm6FTfaCi6Kc1BgO3tca3D42_IS3cyJT8r72GTcvRT0iAg7en1muY-pZ2beo0BjUYWGsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9383d1d6b2.mp4?token=BAtPVDi8XJrF2DQs58MyHqbkV3Ygzuq9C4c41VbiaB0qdMGfNnmZpE_D7IEtlAbsv6BFnwJ2_dPwckilTXm-AKf3IdhUI7pnISVYA2Y_ARjRcdHtaJiS7wQdHpDxb_bVV3CWDSVZHp6JCvgTv3NBp4XpVm_9H2TD76hOKGqz-QTCFNqFcKqJUABKPlAe2FhH2ZjWFmMIngfkT7ZDJfVZTn8ZjNy8pNeabQM5-pTuE3XcWvabe8LtEX1YCHodRYQ0cbU85TNthDsqa040AXm6FTfaCi6Kc1BgO3tca3D42_IS3cyJT8r72GTcvRT0iAg7en1muY-pZ2beo0BjUYWGsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی دولت: قیمت بنزین سهمیه‌ای تغییر نمی‌کند
🔹
در بنزین غیرسهمیه‌ای چنانچه تغییری باشد حتما اعلام می‌شود؛ آنچه تاکنون اتفاق افتاده به جهت آسیب‌هایی که دیدیم کاهش سهمیۀ دوم از ۷۰ لیتر به ۵۰ لیتر است.  @Farsna</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/farsna/453079" target="_blank">📅 11:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453078">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0165bcd616.mp4?token=r_znwMqb-du8xptpyR6O6OKzmSYwythpRmcCLzIyoYomNz-P67ubzuCp9YczI3Dzwei2oj0K2juLCBxUybqCLYLrRLoKhle3zWhcmRN7rVmH3SjMueMzLOVGcyWOl_LxSkP1U-LuEaMgiHUT6867s_zhIHvuZCP7DNh1FHSbQT3PljPxrjoN60DZ0l3cE5TkLk4mEZRCxtcOIotl8gyAo7HmvtnvjJd_43_AFf0TB2DUttzNNO-RjIGiEoa_j0ln6HO7Afvcak_bwJh05piLdfkNzZ-428NAV7kcagw2yeM0Wr2_DNWr7kObieuz1D6UVC6lGxLZiLSKO5GjEwqAIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0165bcd616.mp4?token=r_znwMqb-du8xptpyR6O6OKzmSYwythpRmcCLzIyoYomNz-P67ubzuCp9YczI3Dzwei2oj0K2juLCBxUybqCLYLrRLoKhle3zWhcmRN7rVmH3SjMueMzLOVGcyWOl_LxSkP1U-LuEaMgiHUT6867s_zhIHvuZCP7DNh1FHSbQT3PljPxrjoN60DZ0l3cE5TkLk4mEZRCxtcOIotl8gyAo7HmvtnvjJd_43_AFf0TB2DUttzNNO-RjIGiEoa_j0ln6HO7Afvcak_bwJh05piLdfkNzZ-428NAV7kcagw2yeM0Wr2_DNWr7kObieuz1D6UVC6lGxLZiLSKO5GjEwqAIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ناگفته‌های فتاح از عملیات ویژۀ ستاد اجرایی در جنگ رمضان  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farsna/453078" target="_blank">📅 11:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453077">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abe43742e5.mp4?token=ntgUSQpXHhtZWQ_8j9kuEfwULs6YAGwnQ4VhzLwZylIhmlVFZPpIj9NKVSKVLFGjNL2VQ_VgqS47m9fEWsaTQVuP2gr73VXDDuVk5RwdmIMUT1PNmqaHV10Jx4vfSf6pewmPAZw8EfyaMObGo90P64cz5ihozwX273z4xihsJgXdVaOsxXPaIApEFo5deqg7NkJPi15v3tiQSoB2eK-0oI37Ul_Q54jlYFqlLC68wojgH9ZjGhxkBLgD0tuBR0OM6p1VufKnTsMtFGv3iS83pLMVFe8xD_i2xJIe54UifaKm9wKGkgjMCozx5uNMlb0W5cI9cRVubE25tpTl1Xgs0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abe43742e5.mp4?token=ntgUSQpXHhtZWQ_8j9kuEfwULs6YAGwnQ4VhzLwZylIhmlVFZPpIj9NKVSKVLFGjNL2VQ_VgqS47m9fEWsaTQVuP2gr73VXDDuVk5RwdmIMUT1PNmqaHV10Jx4vfSf6pewmPAZw8EfyaMObGo90P64cz5ihozwX273z4xihsJgXdVaOsxXPaIApEFo5deqg7NkJPi15v3tiQSoB2eK-0oI37Ul_Q54jlYFqlLC68wojgH9ZjGhxkBLgD0tuBR0OM6p1VufKnTsMtFGv3iS83pLMVFe8xD_i2xJIe54UifaKm9wKGkgjMCozx5uNMlb0W5cI9cRVubE25tpTl1Xgs0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی دولت: در ایام جنگ  ۳۵۰ نفر از کارکنان دولت به شهادت رسیدند
🔹
همچنین مردم عادی که داخل ماشین نه موشک داشتند و نه اورانیوم، و تنها در حال عبور از پل بودند، به شهادت رسیدند. @Farsna</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/farsna/453077" target="_blank">📅 11:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453076">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d30a7839a3.mp4?token=mm43JJ8iFVg96E_nygl8NxQL_WrvYTjAfc23rraM87gNZEe0wgzevRd3zahB16QIkRHzE1vx_SUy636ldRAD85YV9wyO1WvUEov_AZnEPLH3JzJCvlv4CKrh5zIMqCWj6eLtooeJdvEh3TZhhEBRaMTO20fpsqA4VHVwlQ4UG1NsEY503wzDKYhghhfQjiQYL0Li8Ey_SF9fJFI26k3D-MjsJ4PuZNp5flwnYnEQDwox1jiDxHHD0M3fWGkbrdexK0DI-QjDAuK0ZNK4Bq2s5dXpdKkILKdjD_Mo4Kr24iSVoy0Mgb72S_7UD3SIHnWxZNHE0qAljTS_N7M_piCURg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d30a7839a3.mp4?token=mm43JJ8iFVg96E_nygl8NxQL_WrvYTjAfc23rraM87gNZEe0wgzevRd3zahB16QIkRHzE1vx_SUy636ldRAD85YV9wyO1WvUEov_AZnEPLH3JzJCvlv4CKrh5zIMqCWj6eLtooeJdvEh3TZhhEBRaMTO20fpsqA4VHVwlQ4UG1NsEY503wzDKYhghhfQjiQYL0Li8Ey_SF9fJFI26k3D-MjsJ4PuZNp5flwnYnEQDwox1jiDxHHD0M3fWGkbrdexK0DI-QjDAuK0ZNK4Bq2s5dXpdKkILKdjD_Mo4Kr24iSVoy0Mgb72S_7UD3SIHnWxZNHE0qAljTS_N7M_piCURg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قطع سخنرانی ترامپ با شعار علیه کودک‌آزاری
🔹
قطع سخنرانی ترامپ در تجمع انتخاباتی جمهوری‌خواهان در میشیگان با فریادهای معترض آمریکایی دربارهٔ پروندهٔ اپستین، باعث مداخلهٔ نیروهای امنیتی و بازداشت او شد.
🔹
درحالی‌که ترامپ در این سخنرانی مشغول تمجید خودش بود، یک معترض با اشاره به پرونده قاچاق جنسی کودکان توسط اپستین، ترامپ را «محافظ کودک‌آزار» خواند.
🔹
پس‌از قطع سخنرانی ترامپ و بازداشت یک معترض توسط نیروهای امنیتی، رئیس‌جمهور آمریکا به‌سمت او گفت: «او یک کمونیست است؛ او یک کمونیست است.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/453076" target="_blank">📅 10:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453075">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7849caf617.mp4?token=e0kQ1YK5ooZkklrR-Y29rF36TtJziYyIHII9ZmNiqqAVF6dgGN1Wa2VyjY9WUk0-D5PJNaSMmhbYBLZhX8ah9PNU-uYmtrQdRlbgTabRla7UMWewAqr69cDMoz0ONhHGzxXz1oixX4W93AzGGMKbrVYNtp6LudOT_fQ5bGP9wqeGUFnx48lR2cMpBS6flVw8rIg-HLbyFU11Cpv-L6ywZfzDLQDIFhkK7W_kuutQ57X_1IyXrAvBYwBL96X8Pq98eW0GlHZGlfI25L9bp92BUabOp5aOYFAjhCqEzoWQCgSg12LHSBSvys1CJorT8iwzfsgn96IX9Kl1RGsU2TTkIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7849caf617.mp4?token=e0kQ1YK5ooZkklrR-Y29rF36TtJziYyIHII9ZmNiqqAVF6dgGN1Wa2VyjY9WUk0-D5PJNaSMmhbYBLZhX8ah9PNU-uYmtrQdRlbgTabRla7UMWewAqr69cDMoz0ONhHGzxXz1oixX4W93AzGGMKbrVYNtp6LudOT_fQ5bGP9wqeGUFnx48lR2cMpBS6flVw8rIg-HLbyFU11Cpv-L6ywZfzDLQDIFhkK7W_kuutQ57X_1IyXrAvBYwBL96X8Pq98eW0GlHZGlfI25L9bp92BUabOp5aOYFAjhCqEzoWQCgSg12LHSBSvys1CJorT8iwzfsgn96IX9Kl1RGsU2TTkIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی دولت: فرودگاه بوشهر از مدار خدمت‌رسانی کاملاً خارج است
🔹
فرودگاه بوشهر از مدار خدمت‌رسانی کاملاً خارج است و هواپیمایی که به‌تازگی خریداری شده بود مورد اصابت موشک دشمن قرار گرفت و تنها قسمتی از دم آن باقی مانده است.  @Farsna</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/farsna/453075" target="_blank">📅 10:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453074">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3db12c4819.mp4?token=UOvTgUV7qGMicGxfr8HkHYQl4NXQhh9wz9Qf2rHzHdYTu3QGg79NQ4SoRndFHjpUEDwru58DtlSxkanh2xBXUh-U6ZwMC0Ld6BGaJgmfX7BC41clqHWDHgtJG9RZi80epapBRMPac4DJs-LMD9Go_8Z7zS_aWpVjc0Jth6enFpqrspLfiiQ4Yyd8x7tyuIhHbiloSFmzmmb39gzzSlTU9aNKp8pLYVJwH0Dk1OVGaJGnGLwyKGl63dv8G6y_d-9TlHOR6WfG4DmExFfolX6ARGtL1t-npTsNCy7nWY1V29Ynwzz0lKS2dq_2PlSp9GNXsc40AVR0FZZnopDo1gM5OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3db12c4819.mp4?token=UOvTgUV7qGMicGxfr8HkHYQl4NXQhh9wz9Qf2rHzHdYTu3QGg79NQ4SoRndFHjpUEDwru58DtlSxkanh2xBXUh-U6ZwMC0Ld6BGaJgmfX7BC41clqHWDHgtJG9RZi80epapBRMPac4DJs-LMD9Go_8Z7zS_aWpVjc0Jth6enFpqrspLfiiQ4Yyd8x7tyuIhHbiloSFmzmmb39gzzSlTU9aNKp8pLYVJwH0Dk1OVGaJGnGLwyKGl63dv8G6y_d-9TlHOR6WfG4DmExFfolX6ARGtL1t-npTsNCy7nWY1V29Ynwzz0lKS2dq_2PlSp9GNXsc40AVR0FZZnopDo1gM5OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی دولت: فرودگاه بوشهر از مدار خدمت‌رسانی کاملاً خارج است
🔹
فرودگاه بوشهر از مدار خدمت‌رسانی کاملاً خارج است و هواپیمایی که به‌تازگی خریداری شده بود مورد اصابت موشک دشمن قرار گرفت و تنها قسمتی از دم آن باقی مانده است.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/453074" target="_blank">📅 10:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453070">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3d321b0eb.mp4?token=KBLr_6E7Rny8eOCbFrtlXhcxtRMUhRrU2WKHcJN25FKZxDloTDmRMrlt7UKUaLGWVQnT6wpZV3MeYkSc6SKD__lTZF_yDh_tTtGzq7oUr1paGIXPPnFqEzav4sWT2YxyifLLHAjBSzWpTWbUCxjSSwcO0qGly5ai-SAtrDH4B0Kfmw2zkK6-lIvfA95X36Zgu4a26YGyW4klUTmu25i06nz_FnetdCu0I8xHAvZ7foe5dAfNlLMXmO05VHimsA10mTLfxyXLF5CUNs_0H3Qr_MCpwd57bLK9p6YuEQut_cB7Yx9Js8Rve14ykoADtWeaMruKcaJ-011gmOUiZojkBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3d321b0eb.mp4?token=KBLr_6E7Rny8eOCbFrtlXhcxtRMUhRrU2WKHcJN25FKZxDloTDmRMrlt7UKUaLGWVQnT6wpZV3MeYkSc6SKD__lTZF_yDh_tTtGzq7oUr1paGIXPPnFqEzav4sWT2YxyifLLHAjBSzWpTWbUCxjSSwcO0qGly5ai-SAtrDH4B0Kfmw2zkK6-lIvfA95X36Zgu4a26YGyW4klUTmu25i06nz_FnetdCu0I8xHAvZ7foe5dAfNlLMXmO05VHimsA10mTLfxyXLF5CUNs_0H3Qr_MCpwd57bLK9p6YuEQut_cB7Yx9Js8Rve14ykoADtWeaMruKcaJ-011gmOUiZojkBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملهٔ ۴۰۰ پهپاد اوکراینی به مسکو پیش‌از دیدار زلنسکی با ترامپ
🔹
سوبیانین، شهردار مسکو اعلام کرد که «بیش از ۳۹۰ پهپاد دیشب منطقهٔ مسکو را هدف قرار دادند»؛ حمله‌ای که تنها چند ساعت پیش‌از دیدار برنامه‌ریزی‌شدهٔ رئیس‌جمهور اوکراین با ترامپ انجام شد.
🔹
آندری وروبیوف، فرماندار منطقه مسکو، اعلام کرد که حملات پهپادی به چند ساختمان مسکونی در شهر چخوف و روستای واولوو خسارت وارد کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/453070" target="_blank">📅 10:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453069">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">انفجارهای کنترل‌شده در امیدیۀ خوزستان
🔹
فرمانداری امیدیه: صدای انفجارهای امروز ناشی از عملیات کنترل‌شدۀ انهدام مهمات عمل‌نکرده است و نگرانی برای شهروندان وجود ندارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/453069" target="_blank">📅 10:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453068">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/055057e6bb.mp4?token=f6Xd5TISptfFGL7gpott_2lG3oYJ7PnmvyAmPJk2-iCAOF4XHMF1IWWurM4e13N_Yraac_8Gk9DgNZ9jVMrQp7RB7yAyUoq0PM8aHPLn2cQSCH7dw3GRsdVByk_vB0_N0KrcPACFn846L9B0iEzBeFed1PVqWXGUL2lfQUx3Wt-p8a0wYJO_SQp9lknJaxaXdMMuJkWfjSEDeys0h3GeW7ifrEbsUy5s9GYeabF1XLZrSV2Q8dVjhImdiqitiahZaO11gOq_gBq7PZUQ6jJj7nUR6saaaO1u-OG3XmO1EaSA7C2yB7yPeRMR8kKud7JtGpSNzzwTAgKN4JMbtbm0_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/055057e6bb.mp4?token=f6Xd5TISptfFGL7gpott_2lG3oYJ7PnmvyAmPJk2-iCAOF4XHMF1IWWurM4e13N_Yraac_8Gk9DgNZ9jVMrQp7RB7yAyUoq0PM8aHPLn2cQSCH7dw3GRsdVByk_vB0_N0KrcPACFn846L9B0iEzBeFed1PVqWXGUL2lfQUx3Wt-p8a0wYJO_SQp9lknJaxaXdMMuJkWfjSEDeys0h3GeW7ifrEbsUy5s9GYeabF1XLZrSV2Q8dVjhImdiqitiahZaO11gOq_gBq7PZUQ6jJj7nUR6saaaO1u-OG3XmO1EaSA7C2yB7yPeRMR8kKud7JtGpSNzzwTAgKN4JMbtbm0_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شریعتمداری: بی‌تفاوتی به خون‌خواهی، مجوزی برای ادامۀ جنایت دشمنان است
🔹
مدیرمسئول روزنامۀ کیهان: رهبر معظم انقلاب در بیانیه‌های اخیر، خطوط و محورهای اصلی را به‌روشنی تبیین کرده‌اند و برای شناخت این محورها نیازی به دسترسی به مسائل محرمانه نیست، چرا که بخش قابل توجهی از آن به‌صورت شفاف بیان شده است.
@Farspolitics
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/453068" target="_blank">📅 10:23 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453067">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/922699c9bb.mp4?token=vsaWk4xeCyAephYgLv0rGZE5oXf8tPgb9VwrJbXLg9X3ehtDq9njRAfg8PBwA7YIyrkFcQzJ6nnKPmEo9Gcqad0S20CxguVRFc7VoO-0pvSAUmvSnaqgVk-ml0kQc8T-8uSpWVyRxBYf7r0UUf0jlZO3gPFA9sjXc-klVo88SYD-vrdwtSB1xUbWqTUWYrM_M_APJ6S4p1dH86s7ZDvMzIZqfBOBPQi-E0mbTUXXg1W_rBB9erELHiVmbyqB_obhB7xCPt2rQw3dBr_wCb1YY1U9lDbZ7kgl24Mc8qCapFZfQsqzc6FIk5IFYlZrIiJN1sMwEI5TSZa_EmiPkY53UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/922699c9bb.mp4?token=vsaWk4xeCyAephYgLv0rGZE5oXf8tPgb9VwrJbXLg9X3ehtDq9njRAfg8PBwA7YIyrkFcQzJ6nnKPmEo9Gcqad0S20CxguVRFc7VoO-0pvSAUmvSnaqgVk-ml0kQc8T-8uSpWVyRxBYf7r0UUf0jlZO3gPFA9sjXc-klVo88SYD-vrdwtSB1xUbWqTUWYrM_M_APJ6S4p1dH86s7ZDvMzIZqfBOBPQi-E0mbTUXXg1W_rBB9erELHiVmbyqB_obhB7xCPt2rQw3dBr_wCb1YY1U9lDbZ7kgl24Mc8qCapFZfQsqzc6FIk5IFYlZrIiJN1sMwEI5TSZa_EmiPkY53UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پوتین جنگ نامتقارن دریایی ایران را تحسین کرد
🔹
رئیس‌جمهور روسیه در دیدار با افسران نیروی دریایی این کشور، از «ناوگان پشه‌ٔ ایران» (اصطلاحی که تحلیلگران غربی به‌کار می‌برند) تمجید کرد و گفت: این ناوگان در منطقهٔ درگیری‌های خاورمیانه «عملکردی بسیار مؤثر» داشته است.
🔹
پوتین در این دیدار گفت: مسئلۀ فناوری‌های جدید است و روسیه هم در حال توسعهٔ توانمندی‌های مشابه است؛ شناورهای کوچکی که به تسلیحات پیشرفته‌ای مانند موشک‌های کالیبر مجهز هستند و می‌توانند ضربات دقیق و سنگینی به هر دشمنی وارد کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/453067" target="_blank">📅 10:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453066">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2067ac5a04.mp4?token=vAa5VK8oMHBDW-m8T1JnNJQ6tJYJc_uLmOlHsZ-76FFgXhvnl3ugzm88zwPaKMRwfm2LgqkUX1a1hVfuM97RIVYW0uXGqoibNOk2xooli1Hd4ctXPs5CzTiNdJDretG_n4QJtkWEmYXp15IwEEoOIZfd5LHgOeSiLqWUTPRtpIX5JhKf9-LjAvpHSXESS_KEZvlMrZVivra1UM2PQ2rhviTZDIwo0kbJmY47usgrdLrPMFrWQjwP5v4POMtMJKGFjzg-F-K9M-BE0yfMPBALQThK02tmiR0Pz3_FeNnCikrTBZdGG69hVpakjPEd1rDEDOp1tmnIV5h-Vow0zhb5gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2067ac5a04.mp4?token=vAa5VK8oMHBDW-m8T1JnNJQ6tJYJc_uLmOlHsZ-76FFgXhvnl3ugzm88zwPaKMRwfm2LgqkUX1a1hVfuM97RIVYW0uXGqoibNOk2xooli1Hd4ctXPs5CzTiNdJDretG_n4QJtkWEmYXp15IwEEoOIZfd5LHgOeSiLqWUTPRtpIX5JhKf9-LjAvpHSXESS_KEZvlMrZVivra1UM2PQ2rhviTZDIwo0kbJmY47usgrdLrPMFrWQjwP5v4POMtMJKGFjzg-F-K9M-BE0yfMPBALQThK02tmiR0Pz3_FeNnCikrTBZdGG69hVpakjPEd1rDEDOp1tmnIV5h-Vow0zhb5gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۳ قلاده خرس قهوه‌ای در ارتفاعات جنگل‌های هیرکانی لنگرود مقابل دوربین‌ها ظاهر شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/453066" target="_blank">📅 10:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453065">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">جلسۀ شورای هماهنگی مجلس با حضور قالیباف
🔹
سخنگوی هیئت‌رئیسۀ مجلس: صبح امروز جلسۀ شورای هماهنگی مجلس با حضور قالیباف، اعضای هیئت‌رئیسه و رؤسای کمیسیون‌های تخصصی تشکیل شد.
@Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/453065" target="_blank">📅 09:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453064">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4f35d89bb.mp4?token=sVfC5nApamHxKC5pvbcfsNRq2QWkn81ebsNe3d2myWq1TNwoNutKHuer6AvFn5vV08bxwZ_9il2sOkKojzHTYp5jKTNEKbBAfzexxjR9Y3kDz3LiSUnqsTupHD6G5yGP4qcfHTjf16Gvjwv0GH94IxejNDv6Jy7JXmxg7sNyZr9L8CbmVWyh9SzrNeFAi6IHS2toq0bN27yRm-fpZz0mmvGuutonPYYWlPJrwRqjzSnKu4LnhGnJOSHDBxXJ0M6XrxaAOKGQOzt4hA-RxNVfcPt6TU6S1ABYqaj1wnmoJp61VTN-0x1YxCJeSvIotTxQd1SxTS0IN9iT6uzsVtoJpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4f35d89bb.mp4?token=sVfC5nApamHxKC5pvbcfsNRq2QWkn81ebsNe3d2myWq1TNwoNutKHuer6AvFn5vV08bxwZ_9il2sOkKojzHTYp5jKTNEKbBAfzexxjR9Y3kDz3LiSUnqsTupHD6G5yGP4qcfHTjf16Gvjwv0GH94IxejNDv6Jy7JXmxg7sNyZr9L8CbmVWyh9SzrNeFAi6IHS2toq0bN27yRm-fpZz0mmvGuutonPYYWlPJrwRqjzSnKu4LnhGnJOSHDBxXJ0M6XrxaAOKGQOzt4hA-RxNVfcPt6TU6S1ABYqaj1wnmoJp61VTN-0x1YxCJeSvIotTxQd1SxTS0IN9iT6uzsVtoJpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش‌سوزی در مهم‌ترین تاسیسات نفت عربستان
🔹
تصاویر ماهواره‌ای ستون‌هایی از دود و آتش در تاسیسات ابقیق عربستان که ساعاتی پیش هدف حملات پهپادی و موشکی قرار گرفت را نشان می‌دهد.
🔸
تأسیسات ابقیق که توسط شرکت آرامکو اداره می‌شود، تنگهٔ هرمز را دور می‌زند و نفت را…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/453064" target="_blank">📅 09:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453063">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGo-1C_y-Sz_To87ocHmVtmW2WYV-kw44hHqVbw1DiHfPm4qs5o86X_22fEurCSnh2gJsYpSrX1D-jANpLziVM-ib7fvlBB3r5VS0cSmX_rtmXOg3oJ48ua2jn-eGLtv0-i_9KOy5-DYsGxS7TwcfQfz_j5OvSUnY8MZSDhT1pmVcFA91ecexgpN8YGtkWl20_ESMK-RA2xFPX-BswaAE8OLO206Ezu-jufgU3d6fv0IEui9nEmFVs5Jajfqh44GwC0mbO_7Rs07ilJy0nSDHf1dFoF0yAOy7Ey0DrLqp7ybv8O8jM69X6Gq4Nj-aqXNWGXQi6McWVXlhH7OqUP4rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا از جلسهٔ شورای امنیت سازمان ملل قهر کرد و رفت!
🔹
دیپلمات‌های آمریکایی هنگام سخنرانی نمایندهٔ فرانسه در نشست شورای امنیت سازمان ملل دربارهٔ جنگ اوکراین، جلسه را ترک کردند.
🔹
طبق گزارش الجزیره، این خروج تنها ۲ روز پس‌از یک تبادل‌نظر تند مجازی میان مقام‌های آمریکایی و فرانسوی رخ داد. اختلاف بر سر رأی منفی واشنگتن به تمدید دورهٔ چهارسالهٔ مسئول حقوق بشر سازمان ملل بالا گرفته بود.
🔹
هیئت نمایندگی فرانسه در سازمان ملل در ژنو، شنبه در پیامی نوشته بود که «آمریکا دیگر مشعل‌دار حقوق بشر نیست و در کنار کشورهایی چون کره شمالی، نیکاراگوئه، مالی و روسیه در انزوا قرار گرفته است».
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/453063" target="_blank">📅 09:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453062">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‌
🔴
ارتش اردن مدعی شد که ۲ پهپاد را در آسمان این کشور ساقط کرده و خساراتی در پی نداشته است.  @Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/453062" target="_blank">📅 09:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453061">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RWIExjH5E3Rj1Yv6sQSgbTqXnxFM7yIfCq7nafZHYZrqnJFoHIO56IByyqOfXh4KvapDkToAfoeKAk1nSOiTtEZi0lkOzDZ59NLWrrCgcfDQey7VmcaBmrIay-ai7uNGFM_ClliE7Tw0DMY2gDIYdJlIYZIVGeW28bWq3663K25EvhY_wB2Hw6Gvy8OF0uRtr1C3N60HkmWGtQjyQeKtrcKqUMwU--LwliZXLjYQDr-HJozkiUbZj0DyWdNLwNqHAkYEElBoXQGZG6yh02XMeqLHfd9Akvt0OSOByX2iY4HtTghEtQK64ua4DbiACAO0FkHs5gckvpVsZox89gBGrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی با همتایان عربستانی و عمانی گفت‌وگو کرد
🔹
وزیر خارجهٔ کشورمان در تماس‌های جداگانه با البوسعیدی و بن‌فرحان، ضمن بررسی آخرین تحولات دوجانبه و منطقه‌ای بر ضرورت تقویت همکاری و پیشبرد تلاش‌های دیپلماتیک مشترک برای برقراری ثبات در منطقه و رفع ناامنی تحمیلی بر تنگهٔ هرمز ناشی از اقدامات تجاوزکارانهٔ آمریکا تاکید کرد.
@Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/453061" target="_blank">📅 08:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453060">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">صادرات قند هم آزاد شد
🔹
سازمان توسعه تجارت در نامه‌ای به گمرک با صادرات قند به‌صورت مشروط موافقت کرد.
🔸
۳ روز پیش نیز وزارت صمت ممنوعیت صادرات ۱۵ قلم کالای کشاورزی از جمله کشمش را لغو کرده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/453060" target="_blank">📅 08:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453059">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df15be6725.mp4?token=pHBQvkZBrhjUXrHapnXC2ymrUdtsTL8Cp0fjcMJNf9wLU_YJel9ZLVfvGC_BC3FAMqrA7ps_O8uPKCcgrymsZMYPmQPVK6iY2HD0ruySaj8oUxpseCr-NkpVvHGsZKuh7fbUCQ0r7q3L_-oZk7nDyWyD2dUz8lnp-wkZqxh6Af-nZC8849QwdSzmnupH4-2VWcqrToxfMIpQrcRWNWjAuBU1ZP87J_bsNwGbdYv4F7TWuzLr4LYp7kZGy0TXAshc26PNQwH5Grzu4piXzVMjkOqdeckAfoTPcBTOm9-RWPQ8ZZVv-F4qerw7PI05d6a-wNtCLBSSuwnZpQkBJJRZLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df15be6725.mp4?token=pHBQvkZBrhjUXrHapnXC2ymrUdtsTL8Cp0fjcMJNf9wLU_YJel9ZLVfvGC_BC3FAMqrA7ps_O8uPKCcgrymsZMYPmQPVK6iY2HD0ruySaj8oUxpseCr-NkpVvHGsZKuh7fbUCQ0r7q3L_-oZk7nDyWyD2dUz8lnp-wkZqxh6Af-nZC8849QwdSzmnupH4-2VWcqrToxfMIpQrcRWNWjAuBU1ZP87J_bsNwGbdYv4F7TWuzLr4LYp7kZGy0TXAshc26PNQwH5Grzu4piXzVMjkOqdeckAfoTPcBTOm9-RWPQ8ZZVv-F4qerw7PI05d6a-wNtCLBSSuwnZpQkBJJRZLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: از امروز دما در نیمۀ شمالی کشور خنک می‌شود
🔹
دما در مرزهای اربعینی کشور از ۳۶ تا ۴۹ درجه در نوسان است.
@Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/453059" target="_blank">📅 08:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453058">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd296c7dad.mp4?token=QZ83QatKDCl0HFSUXIA8f09-QLJRtyKi6JoR0DEH11rC6pXAOt1y6PPqzaSN38dpaNgWSTXecad31IdzG6HKvUTagRKExI0Q1IMg0fiIxuXWtPjCLDix9MCYAvr7-kIaMeGljg6jOHi5PKp_k-CPE9A231KrkIwUBcSjEwrKCWXSokI0awUSccQwa1iyuM0reQJkp2JnKN2F-l_STKC7dMuMTk4DDkqG5WGjaZvhokTbZahewgBQInZgqtHQm3riJwuMM3Ri3HH9SDSHtrgYkedyvfsnVpTKrBP3JQlCh3SgG6SOalTRYRg6qxXp1cpTmVshMEzc6bTb7jluj3anVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd296c7dad.mp4?token=QZ83QatKDCl0HFSUXIA8f09-QLJRtyKi6JoR0DEH11rC6pXAOt1y6PPqzaSN38dpaNgWSTXecad31IdzG6HKvUTagRKExI0Q1IMg0fiIxuXWtPjCLDix9MCYAvr7-kIaMeGljg6jOHi5PKp_k-CPE9A231KrkIwUBcSjEwrKCWXSokI0awUSccQwa1iyuM0reQJkp2JnKN2F-l_STKC7dMuMTk4DDkqG5WGjaZvhokTbZahewgBQInZgqtHQm3riJwuMM3Ri3HH9SDSHtrgYkedyvfsnVpTKrBP3JQlCh3SgG6SOalTRYRg6qxXp1cpTmVshMEzc6bTb7jluj3anVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون وزیر رفاه: تمامی فروشگاه‌های زنجیره‌ای و شرکت‌های حقوقی چندشعبه‌ای تا پایان شهریور فرصت دارند به شبکۀ ملی کالابرگ متصل شوند.
@Farsna</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/453058" target="_blank">📅 08:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453057">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9334f5e07.mp4?token=pm9TO-D5GNlBxy_t6ygv4Uu_jnxPNaZx2fx7oTfthj7wgd76RcbeMuoT-h1Ei1x8iWZ2T-yG1dpbPq2p2Ke7dZ3QCqKLWNoLBJtQ7-hyPl2DLxLiEwKCcefmfR21FPl6fMYJIyarsTkseLDDHJrSs0yfG0R0wJ9cHrJURNP-YlpJ1p_jepWpD8JLTYbK3Du61niABqNE9BXUHUVah0ud1lU7eMC5asl72zzdAy2Pi5eJe8jxHM7DMGBOlnehBwITs2HGTdaLYoFYVtBxqJ-tf2P16vqyrnHAO_u8GLkBzij_MbAyYmg_NvGL-5DClJ8ppYEm9vgdIdqMB4W6Dhl_2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9334f5e07.mp4?token=pm9TO-D5GNlBxy_t6ygv4Uu_jnxPNaZx2fx7oTfthj7wgd76RcbeMuoT-h1Ei1x8iWZ2T-yG1dpbPq2p2Ke7dZ3QCqKLWNoLBJtQ7-hyPl2DLxLiEwKCcefmfR21FPl6fMYJIyarsTkseLDDHJrSs0yfG0R0wJ9cHrJURNP-YlpJ1p_jepWpD8JLTYbK3Du61niABqNE9BXUHUVah0ud1lU7eMC5asl72zzdAy2Pi5eJe8jxHM7DMGBOlnehBwITs2HGTdaLYoFYVtBxqJ-tf2P16vqyrnHAO_u8GLkBzij_MbAyYmg_NvGL-5DClJ8ppYEm9vgdIdqMB4W6Dhl_2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خدمت‌رسانی موکب شهدای قدمگاه در جادۀ اراک-بروجرد به زائران اربعین
@Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/453057" target="_blank">📅 08:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453056">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/324870d146.mp4?token=HbUCPvYTfyd2fOM47VqqogsO3IyvIj00rplktW51ElRpIVS29kom8k9DygIB_G8WzeEIbkuHx7slBMRFGj9cUMcnEJYxdxBhcad_nWYplFM5WtHTLgoUUqwEgbYqZ2GIyt01sOiP1MvYg-PNwBddsOPEQsV2k_rAWoVxfay4XGYe4bKPXezsq3bQeoepv-jqcPxa5bbwQGWS_zsjx_uZMMGTwDzIMyZvVUTJfTwnllsfMsI5Jk0iSOZr9gPY2dY4eI_sTflPeSCiELVeNRimBflGbNjZxjhgFLtJpyATdyfoY0bahO0XWVGaRYGoG36uy106daoYfdAdfxcXLFyBsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/324870d146.mp4?token=HbUCPvYTfyd2fOM47VqqogsO3IyvIj00rplktW51ElRpIVS29kom8k9DygIB_G8WzeEIbkuHx7slBMRFGj9cUMcnEJYxdxBhcad_nWYplFM5WtHTLgoUUqwEgbYqZ2GIyt01sOiP1MvYg-PNwBddsOPEQsV2k_rAWoVxfay4XGYe4bKPXezsq3bQeoepv-jqcPxa5bbwQGWS_zsjx_uZMMGTwDzIMyZvVUTJfTwnllsfMsI5Jk0iSOZr9gPY2dY4eI_sTflPeSCiELVeNRimBflGbNjZxjhgFLtJpyATdyfoY0bahO0XWVGaRYGoG36uy106daoYfdAdfxcXLFyBsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
منابع عراقی از حمله به انبار تسلیحات گروهک‌های تروریست تجزیه‌طلب در سلیمانیۀ عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/453056" target="_blank">📅 08:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453055">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8dd86309a.mp4?token=V3hgOBVKtZL4MlQTil4ohKnfWNKQb-xoCbw9xgUBGjkz5ng_8cmFxgkduYdabFppn7-UE0asBNljnvpMfKEcXcDg_Xl8WMusAUYYfM16DbGepYta_Mqr7dSLKXbLkm7H2B3AbdHQV6q19eWKqBXO-15epFrVmKzDflMehQY7QSNwd0We_Y3ldDg_kDjQD3u9tKYAep5ffjsaMoqF_87VV5-RQd7JmhSacga2VnZ0SN2LeOomirUzWV1Wj8qO3qa363diRAQEGBcXI3y7XHbzQ7IKB1yWh9QqPgid2fhILOOfRZV5rzMstjP7-f0Q2mvAXHD4Aw0EmlzSTAfiKrNc0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8dd86309a.mp4?token=V3hgOBVKtZL4MlQTil4ohKnfWNKQb-xoCbw9xgUBGjkz5ng_8cmFxgkduYdabFppn7-UE0asBNljnvpMfKEcXcDg_Xl8WMusAUYYfM16DbGepYta_Mqr7dSLKXbLkm7H2B3AbdHQV6q19eWKqBXO-15epFrVmKzDflMehQY7QSNwd0We_Y3ldDg_kDjQD3u9tKYAep5ffjsaMoqF_87VV5-RQd7JmhSacga2VnZ0SN2LeOomirUzWV1Wj8qO3qa363diRAQEGBcXI3y7XHbzQ7IKB1yWh9QqPgid2fhILOOfRZV5rzMstjP7-f0Q2mvAXHD4Aw0EmlzSTAfiKrNc0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دلیل موشک‌‌باران مدرسۀ میناب اینجاست!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farsna/453055" target="_blank">📅 07:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453054">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">مدارس از مهر حضوری هستند
🔹
وزیر آموزش‌وپرورش: تلاش ما این است که تمام مدارس کشور سال تحصیلی جدید را به‌صورت حضوری و با کمترین دغدغه و مشکل آغاز کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farsna/453054" target="_blank">📅 06:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453053">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
منابع عراقی از حملۀ پهپادی به مقر تروریست‌های تجزیه‌طلب در سلیمانیه عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farsna/453053" target="_blank">📅 06:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453052">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8aa170910.mp4?token=bHEJyEcGe1rmyGdxmyMq-ngPC9_hqZpWlOxtgUOzolgteDSQcrCS8thBuYxxowgDolZojdIS0EI-8_rZgcLIGaAAG01docFg8bIgA2xdsY85gYQkcNfpA4JeGlw9kl9U1-FyhlWBR2DeYQN5kHsfekTuWsSlaw5BO67meZSErSJ-pHsArigmwN8GF8y0lximuBEo7s-3fMOd8myxBZ6Eh1K3qAmZf11vMLKETOeLmM6lL7UJ_kLGGWO1JSQcOhB0S--lwZYHrwU3KK0OWKKOL6Nn_vtmDBQo7a_GwHOg87gWfpsOnHs1FzgYhMoVuoiZoyb9cTFERgbZtm82SDe47rC89x_goKFBfHUQxgF3P56MLohPSItVDXEDgDDjoXSEwfFPURHnsAIC9bG0X9kRNrkoCS5NvSmDRtCRxCQCh-hkA4jRCyGWJhBzrZAPl5zD_wWFk0_EMPsj3fnUun95du5zQqO6pf9pcStnF47whFx5j9qqX2WHnntu2GU9fFowIfF9CGRTVn-xv-zQh7OzPjVsPPaiWgUtd62LjA5HNHCdycYxOPdztxYGnB-dnX_w6fplzvl9po_dIzpioaOORF8mV0J1-cC_tLP_MdXRtB3VdxVmKTGA0GFERCpMhk4Q5lty3JYrN7hS-yjZMJQr977fCaZzVzpG6ynqzv8cgOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8aa170910.mp4?token=bHEJyEcGe1rmyGdxmyMq-ngPC9_hqZpWlOxtgUOzolgteDSQcrCS8thBuYxxowgDolZojdIS0EI-8_rZgcLIGaAAG01docFg8bIgA2xdsY85gYQkcNfpA4JeGlw9kl9U1-FyhlWBR2DeYQN5kHsfekTuWsSlaw5BO67meZSErSJ-pHsArigmwN8GF8y0lximuBEo7s-3fMOd8myxBZ6Eh1K3qAmZf11vMLKETOeLmM6lL7UJ_kLGGWO1JSQcOhB0S--lwZYHrwU3KK0OWKKOL6Nn_vtmDBQo7a_GwHOg87gWfpsOnHs1FzgYhMoVuoiZoyb9cTFERgbZtm82SDe47rC89x_goKFBfHUQxgF3P56MLohPSItVDXEDgDDjoXSEwfFPURHnsAIC9bG0X9kRNrkoCS5NvSmDRtCRxCQCh-hkA4jRCyGWJhBzrZAPl5zD_wWFk0_EMPsj3fnUun95du5zQqO6pf9pcStnF47whFx5j9qqX2WHnntu2GU9fFowIfF9CGRTVn-xv-zQh7OzPjVsPPaiWgUtd62LjA5HNHCdycYxOPdztxYGnB-dnX_w6fplzvl9po_dIzpioaOORF8mV0J1-cC_tLP_MdXRtB3VdxVmKTGA0GFERCpMhk4Q5lty3JYrN7hS-yjZMJQr977fCaZzVzpG6ynqzv8cgOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از جنایات کودتای ۱۸ دی‌ماه ۱۴۰۴ ملک‌شهر اصفهان چه می‌دانیم؟
⤴️
گوشه‌ای از جنایات صورت گرفته در میدان شهید علیخانی اصفهان توسط تروریست‌هایی که امروز به دار مجازات آویخته شدند.
◾️
این جانیان از صحنهٔ جنایات خود و شهادت مأموران انتظامی فیلم‌برداری و برای شبکه‌های وابسته به دشمن ارسال کرده بودند.
@Farsna</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farsna/453052" target="_blank">📅 05:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453051">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">جنایت‌کاران حادثۀ تروریستی دی‌ماه ۱۴۰۴ ملک‌شهر اصفهان اعدام شدند
🔹
دقایقی پیش حکم اعدام «ابوالفضل سپاهی بادجانی» و «امیرحسین صفری حسین‌آبادی»، دوتن از عوامل جنایت فجیع میدان شهید علیخانی اصفهان در کودتای دی‌ماه ۱۴۰۴ اجرا شد.
جرم مجرمان این پرونده چه بود؟
🔹
این افراد، ماموران انتظامی را با طناب به تابلو بسته و پس از مجروح‌کردن آن‌ها با سنگ، روی آن‌ها بنزین ریخته و آتش زده‌اند.
🔹
سپس در حالی که هنوز ماموران تأمین امنیت زنده بودند، آ‌ن‌ها را روی زمین کشیده و بعد با چاقو و قمه، ضربات متعددی بر پیکر آن‌ها وارد کرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/farsna/453051" target="_blank">📅 05:12 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453050">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🎥
وضعیت تردد شبانۀ زائران در مرز چذابه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farsna/453050" target="_blank">📅 03:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453049">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kxkIof2bOTSOYwQewsgroddWY_V9Jcb9XS3aZjX30H_krpuk58O5WJ6eTjcEPC88gD47lwQR8pbF99mfZkW8WFmxJKTV_txRtquuR1bgDxBmxth9tFJL4YJELceWMPwB8kfRSTHmOA4HewlKdNGd8yoL_SuIEj973gl1M5CtL-9zv_rQfPXC9VIuXTnCWMASICBvf31HR6ItekDcCRPP3tID6h1A4ZXFDc5IdEe9tuqN0IN6H7eQTrIVpdc99F7FbkW3TyaobN8l5M_Sm0qgJFUVXSK7pYjyT2t7wjWSRtgAEBgyhHn9e7YXHl3Dt8yuHwsulTu38rUTn6dETRt7VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزرگ‌ترین تأسیسات پالایشی عربستان از کار افتاد
🔸
شرکت آرامکوی عربستان پس از حملات پهپادی یمن، فعالیت بزرگ‌ترین مجتمع فرآوری نفت خود در بقیق را متوقف کرد.
🔹
ساعاتی پیش یمن اعلام کرد که با پهپاد خط لولۀ انتقال نفت از شرق عربستان یعنی همان خط لو‌له‌ای نفت را بدون تنگۀ هرمز به بندر ینبع در دریای سرخ می‌رساند، هدف قرار داده است.
🔹
حالا شرکت آرامکوی تمامی فعالیت خود در این تاسیسات را متوقف و در چندین سایت تولید نفت، عملیات مشعل‌سوزی اضطراری را آغاز کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farsna/453049" target="_blank">📅 02:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453047">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0717616cf6.mp4?token=j5OYPsvSopFMUwES5q1rQmEYiDDPZmgiQGzozfWxjY-YsRZ_GYOrS4JwmHkiTUsLAoRL7iIAIwWIfraJpkxSCETMn81qenP8PVCZy1vs6T4sZPUOPyGz7-HKan9siKEImn9kl_wY11EVwVgTftbb-3k6pjHsXzVpK_p86Hk1gdBpzYAvVc2fNMcp21n0p_cHmXq8zVEN1d2UOpfBZu53Tocr_P8Ewg8IJwe67KwtxKGOcDdkn5UWiaNiAUejAj5Ty-um6Z_S643UFWdQubMonkOwmRI99woL-27QWnHi7ORLm_ixiRqUQBq43SU1pnT7a2CgLvkiB0YT6Ry4FuEofg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0717616cf6.mp4?token=j5OYPsvSopFMUwES5q1rQmEYiDDPZmgiQGzozfWxjY-YsRZ_GYOrS4JwmHkiTUsLAoRL7iIAIwWIfraJpkxSCETMn81qenP8PVCZy1vs6T4sZPUOPyGz7-HKan9siKEImn9kl_wY11EVwVgTftbb-3k6pjHsXzVpK_p86Hk1gdBpzYAvVc2fNMcp21n0p_cHmXq8zVEN1d2UOpfBZu53Tocr_P8Ewg8IJwe67KwtxKGOcDdkn5UWiaNiAUejAj5Ty-um6Z_S643UFWdQubMonkOwmRI99woL-27QWnHi7ORLm_ixiRqUQBq43SU1pnT7a2CgLvkiB0YT6Ry4FuEofg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
منابع عربی از حمله به مواضع تروریست‌های تجزیه‌طلب در اربیل عراق خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farsna/453047" target="_blank">📅 01:59 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453046">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d65ef6bc8b.mp4?token=U4O7bzh9eaDVt9y4BuII99SVWGi13fZ_jjzU_98wTynRxM4dnUFxDBUPzFDp17Z_r2Ke1mzTL6Q9Uqf4iR0fgrA4Z4EMh4l3GYgeaukmNIT7fClL7qcGkw30RHkFxBscfrpBD5WO2c49o8ahajD89a97WM6xDGfWL7oHQppCjb8Fj_ntj-kxXWVHWAVcLhAcTL1IZjXjyN7AonU-FAmnneD8Hpn118Bmc88zQoAIMjY9fLzobsMeVC95Jcn5zieUhB6dCat8mneCmiEev91b16lp8ZboxLreQutxBiHEFI_ik7e22DlCM0s7lRz5PPkH-Kk2QmDfLkYXETCIe-XB1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d65ef6bc8b.mp4?token=U4O7bzh9eaDVt9y4BuII99SVWGi13fZ_jjzU_98wTynRxM4dnUFxDBUPzFDp17Z_r2Ke1mzTL6Q9Uqf4iR0fgrA4Z4EMh4l3GYgeaukmNIT7fClL7qcGkw30RHkFxBscfrpBD5WO2c49o8ahajD89a97WM6xDGfWL7oHQppCjb8Fj_ntj-kxXWVHWAVcLhAcTL1IZjXjyN7AonU-FAmnneD8Hpn118Bmc88zQoAIMjY9fLzobsMeVC95Jcn5zieUhB6dCat8mneCmiEev91b16lp8ZboxLreQutxBiHEFI_ik7e22DlCM0s7lRz5PPkH-Kk2QmDfLkYXETCIe-XB1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زائران ایرانی در مسیر پیاده‌روی اربعین از نجف تا کربلا هم تجمعات شبانه را ترک نکردند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farsna/453046" target="_blank">📅 01:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453045">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">گزارش‌ها از حمله به کنسولگری آمریکا در اربیل
🔹
منابع رسانه‌ای عراقی با اشاره به وقوع بیش از ۷ انفجار در حومۀ اربیل، خبر دادند که کنسولگری آمریکا در این شهر نیز هدف قرار گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farsna/453045" target="_blank">📅 00:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453044">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
منابع عربی از حمله به مواضع تروریست‌های تجزیه‌طلب در اربیل عراق خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farsna/453044" target="_blank">📅 00:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453042">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
منابع عربی از حمله به مواضع تروریست‌های تجزیه‌طلب در اربیل عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farsna/453042" target="_blank">📅 00:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453041">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">گزارش‌ها از حمله به یک میدان گازی در شمال عراق
🔹
منابع محلی از حمله به میدان گازی خورمور در استان سلیمانیه واقع در منطقۀ کردستان عراق خبر دادند.
🔹
همزمان پهپادهای تهاجمی خارجی نیز در آسمان اربیل، مرکز منطقۀ کردستان عراق، به سمت اهداف خود پرواز می‌کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farsna/453041" target="_blank">📅 00:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453039">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27662a2de4.mp4?token=cUqhRIka03w7HrY_TUO-FBAWuegfA_--uk8pSW4A23-9f5rWZBR-19GA3NhJ1UebaIuioIWTEe8t96dK1DVtI1Js5hXDGB3Ayb8xhlRl81mMTNpU2mOmbvUKiPEg_duJrCkbKKwJDsiVNa21mz03oheLrTbaUGpbvcyFIA1mNR5vHpZf5GFTAbJ3He2yBOMJPt4xeOBU9A-uxzLx3ctMfhW57BloI9JAnMoloeYw9zjtxDEMvGgHr0oK2fS2JHYQV13hopo7LULD2To6nVMvIiSRJF56a4Cc-Txtcr3Rk3gD6JP5AHdA9drCJ_SAsnym-0lFF4SueNly6n0LAPfhbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27662a2de4.mp4?token=cUqhRIka03w7HrY_TUO-FBAWuegfA_--uk8pSW4A23-9f5rWZBR-19GA3NhJ1UebaIuioIWTEe8t96dK1DVtI1Js5hXDGB3Ayb8xhlRl81mMTNpU2mOmbvUKiPEg_duJrCkbKKwJDsiVNa21mz03oheLrTbaUGpbvcyFIA1mNR5vHpZf5GFTAbJ3He2yBOMJPt4xeOBU9A-uxzLx3ctMfhW57BloI9JAnMoloeYw9zjtxDEMvGgHr0oK2fS2JHYQV13hopo7LULD2To6nVMvIiSRJF56a4Cc-Txtcr3Rk3gD6JP5AHdA9drCJ_SAsnym-0lFF4SueNly6n0LAPfhbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال و هوای عمود ۳۴۰ مشایه نجف تا کربلا
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farsna/453039" target="_blank">📅 00:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453038">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bf9d824db.mp4?token=UoY4QKpnJ1SRMgRmm39Hz8VztkPqoEn1tXvrST5JrHJxSq6RzzALjfTnaJ5c_0P0CAyouWr85jET2Bidl3BVm8hwidu_a74qB5jW71i67ZW4XYBB83XJH97y5J_uCKg5rm2bBq5mLCsqj-9Jw_tOwzfpuQ7UoQwlLW8DgazJTRGLSZew3-iB8gcmCkneSg5Jz3vFbgQIpVn8CQfV6XCokc7rFOfxjkjJCSrs-FVGkyRIeq9G93GPXGiLssnpon-BYE2zFaZoMbP-wDsnfKfOiagW0RbEwX1Md56U1Qp-kQMKu8YiNvTiP98HgnoYf3fC0F4V8ij45S8wp_LDlyQA7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bf9d824db.mp4?token=UoY4QKpnJ1SRMgRmm39Hz8VztkPqoEn1tXvrST5JrHJxSq6RzzALjfTnaJ5c_0P0CAyouWr85jET2Bidl3BVm8hwidu_a74qB5jW71i67ZW4XYBB83XJH97y5J_uCKg5rm2bBq5mLCsqj-9Jw_tOwzfpuQ7UoQwlLW8DgazJTRGLSZew3-iB8gcmCkneSg5Jz3vFbgQIpVn8CQfV6XCokc7rFOfxjkjJCSrs-FVGkyRIeq9G93GPXGiLssnpon-BYE2zFaZoMbP-wDsnfKfOiagW0RbEwX1Md56U1Qp-kQMKu8YiNvTiP98HgnoYf3fC0F4V8ij45S8wp_LDlyQA7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خبرهایی از سقوط پهپاد آمریکایی در عراق
🔹
رسانه‌های عراقی تصاویری از سقوط پهپاد آمریکایی در نزدیکی سد حدیثه در استان الانبار منتشر کردند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farsna/453038" target="_blank">📅 00:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453037">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/394406b222.mp4?token=dB-RDE7YXb6juqW1OufHAoXwem6nTTQ49VR360yIeaGKpke11k5xhzx-xChyOKDEgXAkkTK0vVxVGegz9xPac5DBAK5WPQRM-yU4WMDyOaHZb7XGFKc-uvVHcxY-lM4dSr8zfwgjyc2oN5VCD_31K5vqHyETugPHDCBkPdz6FxPQi4LeMdy6srdCiFpKnKSltTMl1IMXputFBMqSsX5eVyz4GOqoPeppgmlDGWzIt4K9tHCmlUtHl_mths8LSrUlDJ7o9SQlfGz25yuoEVKoRJdTnWlgm0CWmY4g99nviM82cwBFYlcQ-A1cQ9Fq5vUZSmOfv0bVmMiviAfhpDpJ9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/394406b222.mp4?token=dB-RDE7YXb6juqW1OufHAoXwem6nTTQ49VR360yIeaGKpke11k5xhzx-xChyOKDEgXAkkTK0vVxVGegz9xPac5DBAK5WPQRM-yU4WMDyOaHZb7XGFKc-uvVHcxY-lM4dSr8zfwgjyc2oN5VCD_31K5vqHyETugPHDCBkPdz6FxPQi4LeMdy6srdCiFpKnKSltTMl1IMXputFBMqSsX5eVyz4GOqoPeppgmlDGWzIt4K9tHCmlUtHl_mths8LSrUlDJ7o9SQlfGz25yuoEVKoRJdTnWlgm0CWmY4g99nviM82cwBFYlcQ-A1cQ9Fq5vUZSmOfv0bVmMiviAfhpDpJ9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
افشاگری مقام عراقی دربارهٔ بازداشت گروه‌ خرابکار وابسته به اوکراین
🔹
مشاور امنیت ملی عراق: هسته‌های اطلاعاتی اوکراینی در عراق حملاتی را اجرا می‌کنند و آن را به گروه‌های مقاومت نسبت می‌دهند.
🔹
نهادهای عراقی افراد و عناصری را بازداشت کرده‌اند که در بازجویی‌ها اعتراف کرده‌اند که هسته‌های اوکراینی‌ حملاتی را علیه تاسیسات حاکمیتی عراق انجام داده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/453037" target="_blank">📅 00:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453036">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1387c0f59e.mp4?token=RvMCGI20KqzAWWzJQ3kU2LBnPjhTnOcIUNZjMxLg_PiZfYIQci9NC0KdCIZr2opz4GVwQ9tUC3CG0bh5_sPTEaP71mfTdZywbpTAm3jxlnyCeIYApA9bIKZ_PnkBPTJrgdXNsCpljqaoFMZNlj7NkQ3PQqtcAyxY-rS8qab7tAZKraC8DEAz-Q6Y9mDMkPYO_ol1krTrs9EW_p0iJqzzxP_Ec98z9hwFf55gd8r9-gO1DPo1Ij6hKie9x16tymO9NB4ZCsy_PExPLwCLzSOPUyLcUoJ72eYntUjVHMAwT7Q4aS2VwwIn_-Gznu-3ECZ1kkDsFn7e5zCWwexf9Gwsxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1387c0f59e.mp4?token=RvMCGI20KqzAWWzJQ3kU2LBnPjhTnOcIUNZjMxLg_PiZfYIQci9NC0KdCIZr2opz4GVwQ9tUC3CG0bh5_sPTEaP71mfTdZywbpTAm3jxlnyCeIYApA9bIKZ_PnkBPTJrgdXNsCpljqaoFMZNlj7NkQ3PQqtcAyxY-rS8qab7tAZKraC8DEAz-Q6Y9mDMkPYO_ol1krTrs9EW_p0iJqzzxP_Ec98z9hwFf55gd8r9-gO1DPo1Ij6hKie9x16tymO9NB4ZCsy_PExPLwCLzSOPUyLcUoJ72eYntUjVHMAwT7Q4aS2VwwIn_-Gznu-3ECZ1kkDsFn7e5zCWwexf9Gwsxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تردد شبانهٔ زائران در مرز خسروی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/453036" target="_blank">📅 23:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453035">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3be59b32e3.mp4?token=XFMXNdKRCfWg-c42mB8KSx8cr5tA85yZQWqAYamyuEpWb7t7pJTxZ7alvt2_hRFarRqmGMTG-RlbUr5GWqDVoq_FC92CfycO0x3OJkj6zOx6M8HIZLLNYks0pa8cLtxyfor_4Q4JaomiVGKszO1sR4A7bh4EUr3HVbLubkGAdANaTqUgCIBcFG8UuSKDBczC6JLM_nRWE6iZhog-EkdhlqontqVS5Y2-of6LPcFfpzg86uhIupGvIziIlV1_QVqOXe38Wht7PJQ0vEwE727PYhthdopNeQ8h_jvUSlIQy5smXPhEwfhjuh6mPo7MXoOOzJeCpge-ZpTEmAktDtD_YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3be59b32e3.mp4?token=XFMXNdKRCfWg-c42mB8KSx8cr5tA85yZQWqAYamyuEpWb7t7pJTxZ7alvt2_hRFarRqmGMTG-RlbUr5GWqDVoq_FC92CfycO0x3OJkj6zOx6M8HIZLLNYks0pa8cLtxyfor_4Q4JaomiVGKszO1sR4A7bh4EUr3HVbLubkGAdANaTqUgCIBcFG8UuSKDBczC6JLM_nRWE6iZhog-EkdhlqontqVS5Y2-of6LPcFfpzg86uhIupGvIziIlV1_QVqOXe38Wht7PJQ0vEwE727PYhthdopNeQ8h_jvUSlIQy5smXPhEwfhjuh6mPo7MXoOOzJeCpge-ZpTEmAktDtD_YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عکس شهدای میناب در شهر امیرالمؤمنین(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farsna/453035" target="_blank">📅 23:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453034">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d86351cbbf.mp4?token=mATzoUMKDjdpSKCdg_rNTaq3Mf_nzQkf99jihiPEwfbjF1wz7GzrhTIx6k06QQBJAkAypvMD7KNdQYQPjKnbaWDBNlY8SwVp9GYh2duv4KeJpNlnAjasNREzw24yJdm_-maK3DoqJqzsbaIO0DmODmiAW74a0QyV5zSJ5UWreuKWa7WmWzeV0Ig5p0vm0ANng4YFva7dL1X5_temc0Iu1t8TSMGjMJMMwUjGN2NQi6-uC2N77BjkIRpc0LgHWxzh9bADTs0nHPAEutQUsxR0Dwu2Zh-bzDE8GArR2KUidquxmxeM2uHo8T04QJU-hbdKnksD3Y6HvIeUUlcY-TlsgStdVgvdTbJnaHRLW19Ke6uB1rRtdUD_4EHE_1kypPpBFF3n_wkbbDgnsF8RYt7aLFIG3dPqOSUpqXoDzvlx0ewc91d0H5XZ__Qaz-oG_scH6Y7God-oUi834jfF4ZqmqCGopS6bhtrcB7dTjoxyCGlu-nqoctfUfbh2b_PurLs0VlxcVO5OZK4cS7VR3WfpYhuZpfcUKnHOhByJlEnr2WXQbiZxFS5QbXl7uLCCO8CJkmy1uIJ2C1DTejVuSc-qs7m9h30hQs6yJDPjhgFpGYk8cI8gASuIhsZgxQ8X6SyC7kJ6NI9ePAJte21yl5iK9PrOjAgpiW-Zpt1swHTj91E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d86351cbbf.mp4?token=mATzoUMKDjdpSKCdg_rNTaq3Mf_nzQkf99jihiPEwfbjF1wz7GzrhTIx6k06QQBJAkAypvMD7KNdQYQPjKnbaWDBNlY8SwVp9GYh2duv4KeJpNlnAjasNREzw24yJdm_-maK3DoqJqzsbaIO0DmODmiAW74a0QyV5zSJ5UWreuKWa7WmWzeV0Ig5p0vm0ANng4YFva7dL1X5_temc0Iu1t8TSMGjMJMMwUjGN2NQi6-uC2N77BjkIRpc0LgHWxzh9bADTs0nHPAEutQUsxR0Dwu2Zh-bzDE8GArR2KUidquxmxeM2uHo8T04QJU-hbdKnksD3Y6HvIeUUlcY-TlsgStdVgvdTbJnaHRLW19Ke6uB1rRtdUD_4EHE_1kypPpBFF3n_wkbbDgnsF8RYt7aLFIG3dPqOSUpqXoDzvlx0ewc91d0H5XZ__Qaz-oG_scH6Y7God-oUi834jfF4ZqmqCGopS6bhtrcB7dTjoxyCGlu-nqoctfUfbh2b_PurLs0VlxcVO5OZK4cS7VR3WfpYhuZpfcUKnHOhByJlEnr2WXQbiZxFS5QbXl7uLCCO8CJkmy1uIJ2C1DTejVuSc-qs7m9h30hQs6yJDPjhgFpGYk8cI8gASuIhsZgxQ8X6SyC7kJ6NI9ePAJte21yl5iK9PrOjAgpiW-Zpt1swHTj91E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نایب‌رئیس مجلس: نباید اجازه دهیم آمریکا هرموقع دلش خواست حمله کند و هرموقع به مشکل خورد عقب برود
@Farsna</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/453034" target="_blank">📅 23:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453033">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f820943e2.mp4?token=ag1pxXJLwwWBcQgRGiQDXzrDlMyLflUDiN1Q5oaZ7xqmOMutQDmagLiYU09AQeVvuri97tSKKun29lFKzcsnoTgROP8666N1whhDMe-JzZtlPtjO3NxfSVjlxeal0WGwiUPepcrhm52cgkgaWcY2BmCVqTYwYEIW5T-v0lm6Bhpbsi0Zi3Nz4PbWWe9SfZA0KSwspCzJ9vhNcaYM55iXD2k70YQ5NZeXmODberXMEc7LL8sQ1myifleZ2_4dy7FlguFt1AT4ovV5Ec3gTGiJBmkAnjaZL4eiMhvK8ecHzGLiKsPK5EB1SMtnoYb2nd0se-IOLjyWPp64EytUjgntuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f820943e2.mp4?token=ag1pxXJLwwWBcQgRGiQDXzrDlMyLflUDiN1Q5oaZ7xqmOMutQDmagLiYU09AQeVvuri97tSKKun29lFKzcsnoTgROP8666N1whhDMe-JzZtlPtjO3NxfSVjlxeal0WGwiUPepcrhm52cgkgaWcY2BmCVqTYwYEIW5T-v0lm6Bhpbsi0Zi3Nz4PbWWe9SfZA0KSwspCzJ9vhNcaYM55iXD2k70YQ5NZeXmODberXMEc7LL8sQ1myifleZ2_4dy7FlguFt1AT4ovV5Ec3gTGiJBmkAnjaZL4eiMhvK8ecHzGLiKsPK5EB1SMtnoYb2nd0se-IOLjyWPp64EytUjgntuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حمایت مردم از رزمندگان اسلام و خون‌خواهی امام شهید به ۱۴۹ شب رسید
@Farsna</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/453033" target="_blank">📅 23:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453032">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e4ffd812c.mp4?token=lcrfid4bfgbXuvfoySyz_K3WKSfxrRVg8qsfne74SdbLDGfLs_X8Q-rMufeKwhlNNaCn3Pp5vwUNglCdMmB0li0n6RnYgI0PLRdCcRicrDoZDe4Ic7uioQLts428xmQ14RE-TXoKlrmw8wB5N1kaXPbkzTZI_gicOMtC1Y9Lgg8EMN2pAIw_zjca726d7WLCy8Hc7GkMmI1rthZ2ob_GdQQNCjenwVhOn43xzNH3uF2ZqzGGNWRgdLGfKsdNaeJR0dX7q--91Q4E5IxYbTGin3zI26Y2ollwRPieTOXHg2ZnHSmvGN7-gK3IPjVi1iNMedNMrWan1msWYKPElaUPqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e4ffd812c.mp4?token=lcrfid4bfgbXuvfoySyz_K3WKSfxrRVg8qsfne74SdbLDGfLs_X8Q-rMufeKwhlNNaCn3Pp5vwUNglCdMmB0li0n6RnYgI0PLRdCcRicrDoZDe4Ic7uioQLts428xmQ14RE-TXoKlrmw8wB5N1kaXPbkzTZI_gicOMtC1Y9Lgg8EMN2pAIw_zjca726d7WLCy8Hc7GkMmI1rthZ2ob_GdQQNCjenwVhOn43xzNH3uF2ZqzGGNWRgdLGfKsdNaeJR0dX7q--91Q4E5IxYbTGin3zI26Y2ollwRPieTOXHg2ZnHSmvGN7-gK3IPjVi1iNMedNMrWan1msWYKPElaUPqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم خون‌خواهی همچنان در میدان سلیمانی کرمان بالاست
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/453032" target="_blank">📅 23:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453031">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bqT41hv8pqcCXOH48yiW2pYbqqlXtZQ_bVrohJWcWRWkjkYjF5h6YydtujpJK0BOw1yTyWGg5GyDZ_T2dXtjXEakL3kkUYrt5UJpweFSRm5p051y1vNCzYrfIe3JHbu0lbfjvS-VEFzwQtFL68wy4eCgwqgBqLib3ymu7bou6Yz80ykWQHpOV1kjYimQLp1-GdWMduVCTJpOazMLfl6pF_7b4Oh6HIe0tafH99-j_nkXj3sHp5gGQsCzY_uej6r11v1e-KRhYaLvvmWe_oRip5T7D8fUGSMBx6-aTbTJGsAFWHh7Xql3PoTu-FLU2rybnMEVMWrxdVHZZwNZW9_cXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
مقاومت اسلامی عراق: هر اقدام احمقانه سعودی‌ها با پاسخی قاطع روبه‌رو می‌شود
🔹
رژیم سعودی ادعا می‌کند که عراق منبع حملاتی به برخی تاسیسات نفتی آن است؛ این ادعاهای بی‌اساس، تلاشی برای توجیه ناتوانی در پاسخ دادن به حملات موثر یمن به زیرساخت‌های عمیق آنهاست.
🔹
ما در مقاومت اسلامی به رژیم سعودی هشدار روشنی می‌دهیم که هر اقدام احمقانۀ آن‌ها با پاسخی قاطع مواجه خواهد شد که آن‌ها را وادار به پشیمانی خواهد کرد.
🔹
شما امروز بیش از هر زمان دیگری به لغو محاصره ظالمانه بر مردم یمن نیاز دارید، به‌جای اینکه به این‌سو و آن‌سو اتهام بزنید تا شکست خود را توجیه کنید.
@Farsna</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/453031" target="_blank">📅 23:21 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453030">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ad1f2e048.mp4?token=TdeeFA2Mlj6yZv92zhxVe2I4QW5k9bAbaYZ4OVN47D96ZDubMpuohjvkHbpi5FlO4CTH-prZMSGDwXu2nhQvL_HQ4r1M_YTPh99VyHFyPcXpNttxJ-FUQk5c9dRQF4ori2d0O4_3NOzYjBfXe-FOYDi908JFQ-vH66rH-cdYHxiY6sXGKRpmeet6KKAcfTQAW261R9GSHMcvD6oNKP2Ihz4ZrRdUsLqYmMpWVSyoQj5s98ArhATwVJCuYYJlGW6L6sH_jE5W_QeYCyh-g_Pp43quluy2Sc1Dvc5q7ByZeeUzn1cM1gwd9eOo3G_ZHOPz33gvp9vyIFR8Q3mLoOcMAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ad1f2e048.mp4?token=TdeeFA2Mlj6yZv92zhxVe2I4QW5k9bAbaYZ4OVN47D96ZDubMpuohjvkHbpi5FlO4CTH-prZMSGDwXu2nhQvL_HQ4r1M_YTPh99VyHFyPcXpNttxJ-FUQk5c9dRQF4ori2d0O4_3NOzYjBfXe-FOYDi908JFQ-vH66rH-cdYHxiY6sXGKRpmeet6KKAcfTQAW261R9GSHMcvD6oNKP2Ihz4ZrRdUsLqYmMpWVSyoQj5s98ArhATwVJCuYYJlGW6L6sH_jE5W_QeYCyh-g_Pp43quluy2Sc1Dvc5q7ByZeeUzn1cM1gwd9eOo3G_ZHOPz33gvp9vyIFR8Q3mLoOcMAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نمایش پایداری بروجردی‌ها در شب ۱۴۹
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/453030" target="_blank">📅 23:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453028">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
منابع عراقی از انهدام یک پهپاد آمریکایی در استان الانبار در غرب عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/453028" target="_blank">📅 23:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453027">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b065ff32e8.mp4?token=BLMWIh3pZMQ6H6qEp6dNdIAtdasuwYOvsKuUxW5A7g67LvqcQJkumTkIs-8uEhdf7wMt16x5wEdRO_5Dvjiv5cJQrKlCG6m6JPMItl8K1AdDaLtwVLFF0aZfjpPMT7eD0wjcxxcrdMSDOUR_0BOSw5vBJhbuXAslbswbm8seofuzFSGBrm3UnUtSUkSZIotdIwIXko-KfYgH8-rV_4-MXO_6kZr9MftFH9GMHHAOZpM8OjhtFJxPKn9TaXxb56UMWqzuGspiXLObfVVnvn13LqgDKnujcZYP1mr9aUOHtpLSIbXol2NbVrtPeXTKfjRG_p6RTiv0bPxjEx3vfSO7Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b065ff32e8.mp4?token=BLMWIh3pZMQ6H6qEp6dNdIAtdasuwYOvsKuUxW5A7g67LvqcQJkumTkIs-8uEhdf7wMt16x5wEdRO_5Dvjiv5cJQrKlCG6m6JPMItl8K1AdDaLtwVLFF0aZfjpPMT7eD0wjcxxcrdMSDOUR_0BOSw5vBJhbuXAslbswbm8seofuzFSGBrm3UnUtSUkSZIotdIwIXko-KfYgH8-rV_4-MXO_6kZr9MftFH9GMHHAOZpM8OjhtFJxPKn9TaXxb56UMWqzuGspiXLObfVVnvn13LqgDKnujcZYP1mr9aUOHtpLSIbXol2NbVrtPeXTKfjRG_p6RTiv0bPxjEx3vfSO7Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما چندین میلیارد دلار از ونزوئلا درآمد به‌دست می‌آوریم؛ این اتفاق دربارۀ ایران هم خواهد افتاد  @Farsna</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/453027" target="_blank">📅 23:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453026">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🎥
ایستگاه ۱۴۹ تربتی‌ها در قرار شبانۀ خیابان
@Farsna
-
link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/453026" target="_blank">📅 22:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453025">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6cf4aed0f.mp4?token=GS-vEglauT9x1viZwUwhVI_Ac-ryPVhHVsqQzngPkEt-zZjOJkXYu0HlEEMYisn2KHYxy_YyJq20oULBjIUgb8VSMTqC6mnIeMgZQJD85qimacqDkuHk4HLpiB4eSAYTYJYKNGPwq-Rkku05jchkcUU2ZKi1pvnlRsVeCLHpP6fuTm9h8pA2p7jfst06Qr1j1b4gpAXtNR7OptdxsC3ICn9OybkSRdoZnSTzlmd6a22p6vFYZI2DYmoqFwSS1jY89IxwT9tr5XNfNZlYTSzzENVobbUMy6y0JN25TIsSdL5eD2zZfFm3FNu70ISTmHjZXpPGREY7g6_hsuCzkDTquGv-6v6q1Ek5csTAxFp18k1HEfnz59P7XFQzFdBwbv2lIxYoJofnLPTN5Tr02h8TLAsTVxCfGCz30PEyLWYWQchDfZgKb9cTo2mud3bG9dLL-LwN8giTof9-dT3Zrcl2pMcz_we1nnKpsh2Y_92xmfpGXCotd2nLU3PpBvVXIJpLRmL_Xn8nXa-ChcpkzJT2amUs91f4VUd6RLnN-_abuvvjVrWoB-D_o-3oBLtOGYqorfLQg63LIpH7uwgGTDBX-_74QdEbm9TDrny2xCMAWXi8SNNgUP4tNa5lhRKoQBcp7JUwPKItp3JQLSWsbZgHmbAvb63FDSfzLqjy3t2mRv4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6cf4aed0f.mp4?token=GS-vEglauT9x1viZwUwhVI_Ac-ryPVhHVsqQzngPkEt-zZjOJkXYu0HlEEMYisn2KHYxy_YyJq20oULBjIUgb8VSMTqC6mnIeMgZQJD85qimacqDkuHk4HLpiB4eSAYTYJYKNGPwq-Rkku05jchkcUU2ZKi1pvnlRsVeCLHpP6fuTm9h8pA2p7jfst06Qr1j1b4gpAXtNR7OptdxsC3ICn9OybkSRdoZnSTzlmd6a22p6vFYZI2DYmoqFwSS1jY89IxwT9tr5XNfNZlYTSzzENVobbUMy6y0JN25TIsSdL5eD2zZfFm3FNu70ISTmHjZXpPGREY7g6_hsuCzkDTquGv-6v6q1Ek5csTAxFp18k1HEfnz59P7XFQzFdBwbv2lIxYoJofnLPTN5Tr02h8TLAsTVxCfGCz30PEyLWYWQchDfZgKb9cTo2mud3bG9dLL-LwN8giTof9-dT3Zrcl2pMcz_we1nnKpsh2Y_92xmfpGXCotd2nLU3PpBvVXIJpLRmL_Xn8nXa-ChcpkzJT2amUs91f4VUd6RLnN-_abuvvjVrWoB-D_o-3oBLtOGYqorfLQg63LIpH7uwgGTDBX-_74QdEbm9TDrny2xCMAWXi8SNNgUP4tNa5lhRKoQBcp7JUwPKItp3JQLSWsbZgHmbAvb63FDSfzLqjy3t2mRv4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرزند ارشد شهید سیدحسن نصرالله
:
شهادت امام خامنه‌ای مردم کشورهای عربی را بیدار کرد
🔸
در بعضی کشورهای عربی مردم می‌گفتند ما را فریب دادند، چشممان را بستند و عمداً کاری کردند که رهبر شهید را نشناسیم.
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/453025" target="_blank">📅 22:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453024">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a9ab4a2b5.mp4?token=na5xRncszAN9DA4vs52C9e4mx4rITP968f6r1b9nvbLYGgAcW3U3NO51ZxNBZFnx05p-WwBuJODPG6qNysN6MAHRhyA92vmI4weBRZ7rMaPTXkYKspvvKGTkX3n9asIq2UGONmRf220nBqW31AmOVkXFJVGv03i0BlmOm-BpDUoJgUrQBcgyjUjW4Db_KjpcOwlStrpKwLw9ZyjWnm34BDCm_KsCWS_oaheRS6vdFvEC6HwAbstmPGIkSwDQ4qKMRIKqy9-xiINbYXKLB903TbvSGinSGZ0nO5DKQ8qYq2B6KQX5I_R8S8-soIhHyOIq-n27QbPNDFttBARE71UTSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a9ab4a2b5.mp4?token=na5xRncszAN9DA4vs52C9e4mx4rITP968f6r1b9nvbLYGgAcW3U3NO51ZxNBZFnx05p-WwBuJODPG6qNysN6MAHRhyA92vmI4weBRZ7rMaPTXkYKspvvKGTkX3n9asIq2UGONmRf220nBqW31AmOVkXFJVGv03i0BlmOm-BpDUoJgUrQBcgyjUjW4Db_KjpcOwlStrpKwLw9ZyjWnm34BDCm_KsCWS_oaheRS6vdFvEC6HwAbstmPGIkSwDQ4qKMRIKqy9-xiINbYXKLB903TbvSGinSGZ0nO5DKQ8qYq2B6KQX5I_R8S8-soIhHyOIq-n27QbPNDFttBARE71UTSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رمی جمرات ۲ شیطان بزرگ در مسیر اربعین
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/453024" target="_blank">📅 22:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453023">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5eb24ad700.mp4?token=OXX5KsYLXUp1yT1-bBqVTHCnFFfc_j_pTglzzlTL4BTLpSBHERcn9xbNIe-JYp7S4O3_nN_mXB9e-oAAEAFjccglCXAnysqXpo0m5A1TYlvVkZJZPGbG5j2jYdr2IHyOrghuhW8wIYuu4CUvFby-Zb-AAPSWTs21CIJ-OfJ6ofD4ArjR4by7RYZB0VF1ZMPIpjtuErN2jrbutRgGvqx0kJDSgEbaVZKN9j4PEKQoFSoI-5l-uW2icJd3DflzFIZfaUJQK5rthUpSgqrnWI6vtk052YG7BGr_hQfOArAjgORC3oFFnOQg2jhz02Ag2-zt-tje5OymtMuvvNd7zKVdJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5eb24ad700.mp4?token=OXX5KsYLXUp1yT1-bBqVTHCnFFfc_j_pTglzzlTL4BTLpSBHERcn9xbNIe-JYp7S4O3_nN_mXB9e-oAAEAFjccglCXAnysqXpo0m5A1TYlvVkZJZPGbG5j2jYdr2IHyOrghuhW8wIYuu4CUvFby-Zb-AAPSWTs21CIJ-OfJ6ofD4ArjR4by7RYZB0VF1ZMPIpjtuErN2jrbutRgGvqx0kJDSgEbaVZKN9j4PEKQoFSoI-5l-uW2icJd3DflzFIZfaUJQK5rthUpSgqrnWI6vtk052YG7BGr_hQfOArAjgORC3oFFnOQg2jhz02Ag2-zt-tje5OymtMuvvNd7zKVdJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قرار شبانهٔ مردم زرند در شب ۱۴۹
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/453023" target="_blank">📅 22:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453022">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9-HbuXtkpsvjxgymZKwixr64vcfj34wz0PAOKi2Wz1sTFeaiuW102VS3XS7Hj3bQqp7DaDv4JEstMsVNTdZrxmo6UAZ4kHiv4eDssQhf7UowRClmZDDb4W8nI79XUMtBLRmvJjcDZET0OX-n2OcExFn86PA0OyycPDVL-dkeuMeKE3jM-5BTzm5RQKWCsgeRR8wq05kh5TPqZiTe192ygXraiaMy_RbfyNGdnCLvf2oGqNi8ws8bqeCkCXcjttqm7wNPUGX4veu3_U2zvTWIUEdjuWtU359AjkJFn1YbVIQ4yEmI6rfSo5rl2kVa2dPSv59j8UVAE7dqFi5CY_p2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قرارگاه خاتم: تهدیدهای آمریکا را بی‌پاسخ نمی‌گذاریم
🔹
قرارگاه مرکزی حضرت خاتم‌الانبیا : آمریکا در تداوم شرارت و ناامنی در منطقه و به‌دنبال اجرای محاصره غیرقانونی دریایی ایران، طی ۳ روز گذشته اقدام به تهدید شناورها و کشتی های تجاری و نفتکش ایران در آب‌های ساحلی و سرزمینی کشور ما نموده است.
🔹
هشدار می‌دهیم این اقدام آمریکا به منزله توسعه جنگ در منطقه تلقی می‌گردد و همان‌طور که نیروهای مسلح جمهوری اسلامی ایران در میدان عمل ثابت نمودند هرگونه تهدید و شرارت ارتش تروریست آن کشور را بی پاسخ نمی‌گذارند و با آن برخورد خواهند نمود.
@Farsna</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/453022" target="_blank">📅 22:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453021">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/186282342d.mp4?token=SfSEBDaE6HuyFNzvAjY6NU5Cd84-JB9lZ_vX3xaGUjlMxkgypK0g2xo86H4ZidEOkqPxmDgEVhrd9h4NUHYMRY0l-KyGXtf6-nDkuA6_qo-o0Glm9zJ57Qo93GImCtC5Vt6U0jw2Qi6-lUq4jmx5T0WMOhdu6mZW-LTnmx0MOilDXz_RyHzNTHZv52hmFdb_n6VpVJaxW6soFG8aMlH3xRTTZefSArnAjrmHatLOLKOfhBMoNOLAJ8cHvdJRSpcBu4rubsmTujhDRMM1dLACImBPZwXyNic-_L-Jcp-RIUoHMOusg1hY11eqPJ-9EBiNO1o4tPaxuEFix5-nyEONFTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/186282342d.mp4?token=SfSEBDaE6HuyFNzvAjY6NU5Cd84-JB9lZ_vX3xaGUjlMxkgypK0g2xo86H4ZidEOkqPxmDgEVhrd9h4NUHYMRY0l-KyGXtf6-nDkuA6_qo-o0Glm9zJ57Qo93GImCtC5Vt6U0jw2Qi6-lUq4jmx5T0WMOhdu6mZW-LTnmx0MOilDXz_RyHzNTHZv52hmFdb_n6VpVJaxW6soFG8aMlH3xRTTZefSArnAjrmHatLOLKOfhBMoNOLAJ8cHvdJRSpcBu4rubsmTujhDRMM1dLACImBPZwXyNic-_L-Jcp-RIUoHMOusg1hY11eqPJ-9EBiNO1o4tPaxuEFix5-nyEONFTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اینجا تهران است نه کربلا
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/453021" target="_blank">📅 22:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453020">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3009ae4044.mp4?token=itStAlEUIrdvOq_ukJomkoE_8waORZR9eoWr2NE6UM_PTDUP02yG-bLngpuI36Q6OibRZW_3Fg7Occwysc8BR9w3zaO3PVACjZlydyWoCgT_2dj7CFX3sIzbL1-9wvNyLAHTnBp5uCGhV7xaTSRJc9x-oRW5GLqxNrTnWQ18Cj3jzGLG-SHoVxXg_-plvoE2Xc0mxdBylFINqGGazcMhQ0Eqdlnay3DbweH3jSzKBDI3pBOb3ELNx8INyRXqIXxc36O9hksETpN8ZmkbExOzfAMEiknanOLltSRlVM3iyAa8q7FGMZoPrLAPcumxpVEZO7uYSP4U6H0LpMsO8AL8Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3009ae4044.mp4?token=itStAlEUIrdvOq_ukJomkoE_8waORZR9eoWr2NE6UM_PTDUP02yG-bLngpuI36Q6OibRZW_3Fg7Occwysc8BR9w3zaO3PVACjZlydyWoCgT_2dj7CFX3sIzbL1-9wvNyLAHTnBp5uCGhV7xaTSRJc9x-oRW5GLqxNrTnWQ18Cj3jzGLG-SHoVxXg_-plvoE2Xc0mxdBylFINqGGazcMhQ0Eqdlnay3DbweH3jSzKBDI3pBOb3ELNx8INyRXqIXxc36O9hksETpN8ZmkbExOzfAMEiknanOLltSRlVM3iyAa8q7FGMZoPrLAPcumxpVEZO7uYSP4U6H0LpMsO8AL8Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نماینده ولی‌فقیه در خوزستان برای زائران اربعین نان پخت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/453020" target="_blank">📅 22:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453013">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v_FRW_txJ2mr5ordR7uDXbnrdoF9-OkfTr_XPQwBD1MzXEaeazi2nX4Fbzvw-KWGcib6M50rL7aLzR0WX1xEU2GXw9Nq1pechYkMo5l7M57WkZlCloRijEdANm-__R9xGndwJwn_kkj5113ZSDOadKfdbChTDtRxh1Il9R4Y0GjLG0uOihpZgNfwBXrsMkXKxHsvUcsIGMKb7bBqYZtioLNdVj0NXgSwIJ5sPZxv42QYIxixJ76bY_KE8mwQ40Dhd2qTf33kbsb7crZ6d43jDdqJjaUGoMhh_tmZZdoD0m4LFE40Yn-g7WaNMYjryjgRmluSWuW53Uvfas4s7KF7lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jd5pnphMwcweqQA41RnFiEdiFrTi_udbq0bPs6aTlW7pIAghJgAU6sgbbs2BTvMXZtCpyMovACSOL38rEpSNycAKHNrMy2mTe_jiwOmuU6p67MUfEI-HN9G3ZxyoCzl2n5nr8obNjAWbN9rAU3WS3YC7m3i-zMP_10f866Z_1zuSnZICJmquEFCH4wAVDzy6Vbg81u1U5SSW_V9EbMdOPjb9q25RmlpMMdcOBkmQCDJaxNyLiGrj9LlYJfanqPebpd4wWDZc1C2cfkE-ShvH3uYR3EZS9yeXkmm1b-oVhd9xWCArDUNXSIJup_8fLoEWa8_jkJiGr99RQqAa6_JK9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Md4v4FJIPW_2tYqvzL14Ep74rRRcPXV0tHgLhrWTujDO3IvC9pYH6MVrsykM7aBjOsJCwxCYPINbPTUlcrKGrYI52CCA5lR0YvOfq2_AGgF8Sv1NfUM-Ds34Vs-KO4WJd4-Zo0ony5ZIrk2Ux8F1O-YmSK8-XJ5srIVZJSHi2eBqlb3hHE6fXmvNtML74kvBD_MQkIFJvUo8FDfahyhjU8XbEEigrriCYGolPGwK_2DUF0U9B1622p-s6KI86y4S-EIz0mSxTKAWdtaqaFwkwcDEDmN-T1CBK3dqyDAZyayE-RBtyQQ_BhIUJrMlVIoe3RKfECWX57S9v4AIg_68sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g1OXDUeD2YuqBO2kPP8PXzESpKQdj-Cg3ffWXGvbX9JYUchgoL4rh4tahAajSWHLclD0KaKre7iOLGv3YCP8rZPsXMfgPQRk_lae0GmlS0jsHcNJ1PH6qqQSg42f2265ds4cpbrOy2RQSnHGySC_OhEzjXJffx-K6HhHu-sScoT2M84ndfeMjzKvAaKcaa4wOLNm6Ly58bFAJ1VRZpnUmt2nwplt136N0W0znjv370qwcXBEy6HmpmWQYLBC_LLRnrvesBArPg3OvAgwumaLn-u760hS05nKEdD4fjr-1CCpIzFACANxdjbO9AQYFk8qjgZ9jhMlDaPRzlmp61RfBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SbDrr8xQju2KZOPSoSHLHPzrNOnzMCam3dQETlZc2BxGkO0uAkqI4_I_NlhOQI7JiaiZE4VbxSWjFMhu0hWmgwgYQSfpicc8fqan_4VaeIGCkVuqGLy1WfxaDWH2CHwUfAPYELSVgrI_eHh6wMGEE1GCqshZhBMg0Ahw1RmKgAudJcttl6D4kWdLanY7yQltyVOZ3Xy7GIJpH7LXL9aHAIOxHYV8jO-ktP_R9_zd1VTtwGlIzSawNT8ggKrQAVZXlhPWHDmovFugANhjjXGertX4QNCdBOiZARzOVaEAnE2KQ11TmBlS_x2HneHO3ssWHnOx0FFkmyOBVLbxDurtog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/erWyqcXWka971_mFXHGnSDmnWJjwGfWapdvoqicMBYbRWVvpuTvBCk9ZpWIqzGeXgSOqGhELU2LoG7dR4KkA2HKGydEjWXmd2LT9I7qb65DK8lUiP-_p_UztboZERsxWZwJZEhJIr9rKuLWatIT-Fhuo0jwG_TkQAKuINx6fod-Fhg3KoOfdlUADdiBWNjHO3BHSvYkmwaAhQg-TNxyQLS8Kp_IoZ34fqpH_t8cxMpO0nERd1a9-Ssiyaw3_O2XEC5rauXnAPnPhcNlZx53EBxkA_jNQT08MtPY7FhTRE9nOooVyoWaYpHiJeTLge_zy8hSZl0_n_gMyuydwpq5Cow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KA1wmvNlfa_OJaXMndHNtNSxnyspt1QLEJSP7mZlY6QI3Y0HPSDjNzBSO9LKCtRKjyyVjBGxUKyUqW0D032RtBR2JSBc7gZdQMkS6pG4mD7VgBNVZ7fqy__Aqyy_70x2J6jQVPZ1li6GGAC2001r48Q5WoFnFcZcOSU_9eYL1xCC62DAB4C9tcPfEfn1NkCBMxqOVL8Q01Lx_bQXtoC_sBrzULHNi1BjZgESgUBLV_2pw3tiCK8woIXA1eDtgPgKOvTkfX8fW19L1EibFRUozxaahptLl22TzHxoP80LhONvoEWvfXc8NkPZEcJNiQ_UUEzFbCszrjyprHGx2gUuVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تردد شبانۀ زائران از مرز شلمچه
عکس:
فرید حمودی
@Farsna</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/453013" target="_blank">📅 22:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453012">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XlcjTJ5ipWbfyx7JIeebZok_IyGFOZG1zJhSDZcSiUq80Abfhuid8K_3fVukTpxPbZ2DM5f5w9_W1MQvfl4W96JasxfuwmCPOuccmDrG3oyN28_MaFsDETV-qoNYe7TWTpTWUI-dmcZpYAe0xPEWjIwour84N-VT4UmqI0B3AM0dPJ6QKnSM_Ktu7GbNTNovMZIA631I3kTxP6ac2hkPhdm0yiCJKdnfTbxTLobTFrN8oyOQrZkW-TrBoXis3qVVl1SMl4DuSoDpc6ikPpr2PviSAnAWtQtbTG6P9y-oe0n--lPJi4vOCsHYIZyZXq2_hDxuCwfZj3D6_sWwcbFt0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سخنگوی شهرداری تهران: طرح ترافیک برای موتورسیکلت‌ها در اولویت نیست
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/453012" target="_blank">📅 22:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453011">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e84696860e.mp4?token=bNK_zNOFlF6D_eaxY5CBfKLgBt1-sXDODP0NP1L5YYfUwMFgIJEwjBGaB2mfIdIsIqChqK_kONkVxNBfhqkL_eFvCBtTi7vprFv7uRH2ck_wCMgGqqO-yQJWMP1lSCVyONbjVePBO3ddarX1YT21Z6DklZCSv9xY8smas1BAKCf6USWeiBOBXFmtLfM2AS6U7p2xS73nKK8DLxyjPj4zFopI8TSjFPslY9T5bctNQZsad8eQgwzP9GJ8ok8tEZ-pIVtAPNCVhr9YnEyQMqrmKzMLEPD9V4wNgC6H2hKnOqkZvurVeRNaBGZX7ZvlSA2Yz4DUjER_Y3ZtWpJXRTM4Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e84696860e.mp4?token=bNK_zNOFlF6D_eaxY5CBfKLgBt1-sXDODP0NP1L5YYfUwMFgIJEwjBGaB2mfIdIsIqChqK_kONkVxNBfhqkL_eFvCBtTi7vprFv7uRH2ck_wCMgGqqO-yQJWMP1lSCVyONbjVePBO3ddarX1YT21Z6DklZCSv9xY8smas1BAKCf6USWeiBOBXFmtLfM2AS6U7p2xS73nKK8DLxyjPj4zFopI8TSjFPslY9T5bctNQZsad8eQgwzP9GJ8ok8tEZ-pIVtAPNCVhr9YnEyQMqrmKzMLEPD9V4wNgC6H2hKnOqkZvurVeRNaBGZX7ZvlSA2Yz4DUjER_Y3ZtWpJXRTM4Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بهادری جهرمی: همهٔ نهادهای حقوقی گارد جنگی بگیرند و برای آمریکا هزینه بسازند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/453011" target="_blank">📅 22:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453003">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcliUg_wBmfqCfKgM9qjObJmp-XAj_KBDwbMdylh9KUzzP0HbNlY8rpLtLd75DXV5Vip4YUQfuf_aUVBfAwCjXeeP9RWNXeBZmZfFJ4cosRWW2NZBR3iHFidmDWz7xUToQHA1ucDSSs1wkdd_Wn4-GxTxO7pW0YWMHXjnmyHN8CKioqafTpcIQuOGrKpmMl9AOg46rE6k_SZUlOzdKeGYP9RNZlJRE8Q2g5jtF0SkXdLumYgqNLHjgo9CJ1ATK1fIkTJJRyhAH1QfuDzEqKESfb3SzIpmYkrHcZN82LKr63CK_WGUW9y85DMhjaNad2knfwG6ZPjb0FnZga6kKYJeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: توافق هسته‌ای با عربستان منوط به سازش با اسرائیل است
🔹
توافق هسته‌ای غیرنظامی که میان وزارت انرژی ایالات متحده و عربستان سعودی در دست تنظیم است (که به صراحت متضمن هیچ‌گونه غنی‌سازی مواد نخواهد بود) و تنها به مصارف غیرنظامی اختصاص دارد نظیر آنچه ایران،…</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/453003" target="_blank">📅 22:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453001">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HOx2TlT7yrbfmpt3-4K0KTF-DlK8TW2MsEZJPABdHnNbnoXaO66pj0ywo9InojVTeSZleacucWT4rB9GWWadhyilrPTbsIX_EZaNgAn6UiBS7gbR_6m8qvcfzRlNBZ-lctJEmr4C_KfV7ZfysbO_hw4pUmqkPisF5w8LcVBN1fEo55fR4Q5nJuFb3wVWXjeDVSSHEp9FOpKOvUQO2KXVYLW2VXyPE3hmvKvwXf2ycg8Sc6EOmLb9HR8zwTPnQKQm_9uT8woNB-ZQFwPDvbRBTCnf2HP-G3iFCInEAL8yLw8onv3gsyz9Yz5FQDslwi1d8uzqq3Z_N56BsoUc8qhlsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
یاد آقای شهید ایران در بین‌الحرمین
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/453001" target="_blank">📅 22:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453000">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99d381a99b.mp4?token=fDM1zErNPhpBsWyvZYkqrLvqEKnVawe7Ukgy2jv9djIvKTQWV7-V1Tfx49veyqgslPQH2cIG_xUWEXK_WEWI4S50fvfRQAe9Rib1ZOpzQityry9JI0tguYM3pkB0vHBhtW3VQKI6iZCbgOXKqZ7oAog5SIkKw5iEWixPtMb4Z27r-i2jgRu_-3GLAp74M2QnqfnjTMJUZYl7BzmkKQXk_1xz-ok7Q7X6gx_j6BIVRp-7vP26GTdi5hCo0XZnN6Ruc9VfD5fet-FdmD6xouDm6mJGIyFYzywAtGF-f8r-7wvQx8laGjHa0KTAirwF0wwk6ACxT0oLr0VqPs4lMUhmeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99d381a99b.mp4?token=fDM1zErNPhpBsWyvZYkqrLvqEKnVawe7Ukgy2jv9djIvKTQWV7-V1Tfx49veyqgslPQH2cIG_xUWEXK_WEWI4S50fvfRQAe9Rib1ZOpzQityry9JI0tguYM3pkB0vHBhtW3VQKI6iZCbgOXKqZ7oAog5SIkKw5iEWixPtMb4Z27r-i2jgRu_-3GLAp74M2QnqfnjTMJUZYl7BzmkKQXk_1xz-ok7Q7X6gx_j6BIVRp-7vP26GTdi5hCo0XZnN6Ruc9VfD5fet-FdmD6xouDm6mJGIyFYzywAtGF-f8r-7wvQx8laGjHa0KTAirwF0wwk6ACxT0oLr0VqPs4lMUhmeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اعتبار آمریکا مچاله شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/453000" target="_blank">📅 21:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452999">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bc33c0f9d.mp4?token=TKGXJRkaaVONROedVcZK1pnzQz5IGKLvts7Z-G-ODXyl_uuIApSxj5wuat8RSAilkrQgx9M9Gny8Qegqrc5Y9TZxC4dr1dMZWczmu5eeN3sCeieK7_AE2_eR_6RbFAibGI3Zf0lnxO8__b92BtFC3OpvUOJqGPe_8UmXHpx1r6CVGf97x_OtmETK7zhmulFrKuuugL9E58nptSAZttQciNnjaqYcOBvLPbNHPyB-KB5LnWVIz-5cyfSrm-68pI2gY2epCL_6wR_eGMWIcdwPlkNcws1KxM5t8M1rWuU0zVO8IS6CbiuZ5pr8pyuZZDKyiIf-q2rHKbfvRqXlcyZlKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bc33c0f9d.mp4?token=TKGXJRkaaVONROedVcZK1pnzQz5IGKLvts7Z-G-ODXyl_uuIApSxj5wuat8RSAilkrQgx9M9Gny8Qegqrc5Y9TZxC4dr1dMZWczmu5eeN3sCeieK7_AE2_eR_6RbFAibGI3Zf0lnxO8__b92BtFC3OpvUOJqGPe_8UmXHpx1r6CVGf97x_OtmETK7zhmulFrKuuugL9E58nptSAZttQciNnjaqYcOBvLPbNHPyB-KB5LnWVIz-5cyfSrm-68pI2gY2epCL_6wR_eGMWIcdwPlkNcws1KxM5t8M1rWuU0zVO8IS6CbiuZ5pr8pyuZZDKyiIf-q2rHKbfvRqXlcyZlKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیت‌الله جوادی آملی: رفیق ۷۰ ساله را از دست داده‌ام
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/452999" target="_blank">📅 21:41 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452998">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5343478190.mp4?token=DjPQ5XAkiSjzGi3QS171t_4zfDQdvG5gShAtvbB1MakQXds_mC9sctYarCRX0i2wZ4iirJyevLbBhbzt7AM5F86-W2ztTTMLhOtRbsRJ-ipof3eKsBlV6OemFaQvOkPDUn5ef_lCF6uhHATiueVNRQJUWruaBDZeke3WKaKwXKVGaet9F-p4c7DGALxDK0E3tllLloRQHA0F-orEBl5Onn68ldw1BuZL7rAGkybKt03rNf7jfBc5hHt2hX2mhHMk9v6JxpZgjRXQ8IBF4y9N4gg3T9_TW7Eqq4crcvO-casXAB5pacqMDZTj7kq2G65l_oQqU-Iej9ZPlfyrD1591A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5343478190.mp4?token=DjPQ5XAkiSjzGi3QS171t_4zfDQdvG5gShAtvbB1MakQXds_mC9sctYarCRX0i2wZ4iirJyevLbBhbzt7AM5F86-W2ztTTMLhOtRbsRJ-ipof3eKsBlV6OemFaQvOkPDUn5ef_lCF6uhHATiueVNRQJUWruaBDZeke3WKaKwXKVGaet9F-p4c7DGALxDK0E3tllLloRQHA0F-orEBl5Onn68ldw1BuZL7rAGkybKt03rNf7jfBc5hHt2hX2mhHMk9v6JxpZgjRXQ8IBF4y9N4gg3T9_TW7Eqq4crcvO-casXAB5pacqMDZTj7kq2G65l_oQqU-Iej9ZPlfyrD1591A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
غلبهٔ واژه‌های خارجی بر نوشت‌افزارهای ایرانی
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/452998" target="_blank">📅 21:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452997">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/248e5e9775.mp4?token=p4ChuqD8IOKXHn_ySzNl4iWycq7zXjvPoq3ZNcoJnO-KCu-zZs9-OBBbh6Ma7WZ9nw2sqi2IKGAsgw1BcWGarWXPA6pRMcc44wwaunU3G59q60KGBNvqRPdPFChwsHZNsphfRxTd4w04mfxYR_pc897IlEYK4toPxnOZBCXdn-6Op8_AboEagYWafl529VNx34h3uOKbct6F-kfHcdCHUyMOkN9keyvfJk4hMeI3Suq10lTwk3mApmX9T6c58V-FJINMzqMU5wt_I2XaVmEWMYdPuNcr3O2P5j7V0iFBFc4l8vnvsSysiq-BSR-txg0-R2sXDKa96y2A-BeoPldprDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/248e5e9775.mp4?token=p4ChuqD8IOKXHn_ySzNl4iWycq7zXjvPoq3ZNcoJnO-KCu-zZs9-OBBbh6Ma7WZ9nw2sqi2IKGAsgw1BcWGarWXPA6pRMcc44wwaunU3G59q60KGBNvqRPdPFChwsHZNsphfRxTd4w04mfxYR_pc897IlEYK4toPxnOZBCXdn-6Op8_AboEagYWafl529VNx34h3uOKbct6F-kfHcdCHUyMOkN9keyvfJk4hMeI3Suq10lTwk3mApmX9T6c58V-FJINMzqMU5wt_I2XaVmEWMYdPuNcr3O2P5j7V0iFBFc4l8vnvsSysiq-BSR-txg0-R2sXDKa96y2A-BeoPldprDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وضعیت عبور شبانه‌روزی زائران از مرز خسروی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/452997" target="_blank">📅 21:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452995">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52835c2e20.mp4?token=seVbSO-JKcx_MtRZozuK7MCNzgCtYosmX_MYf8mY-woyidEAZiCmActbbD-XtcAS-mC7OLVQ_Ci9Ojz-fFn9O4BiDi02vQ3qfvaMGrQe6mt9NMEyGFAGspXeqvhY5hLO2-w_V2Ihrn9UIRzJpPU0gBfhj2K59ZTpW7WqPlSAYTNa_VYiOqdr7dqd20By7cmom65Qg8awibP197CVKs4_6oSz5TvbV1Kl_l1lvGTVAMMUqQYrll9XOEnEnyVBRZm-eKQXmG7Hi91RXUvkyxzjWnbocmV37o1xhu4kKS7zoR2ohm64nj68X5C60-7EZdYYOGrRZPgWrRT4FXaMl5rgBIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52835c2e20.mp4?token=seVbSO-JKcx_MtRZozuK7MCNzgCtYosmX_MYf8mY-woyidEAZiCmActbbD-XtcAS-mC7OLVQ_Ci9Ojz-fFn9O4BiDi02vQ3qfvaMGrQe6mt9NMEyGFAGspXeqvhY5hLO2-w_V2Ihrn9UIRzJpPU0gBfhj2K59ZTpW7WqPlSAYTNa_VYiOqdr7dqd20By7cmom65Qg8awibP197CVKs4_6oSz5TvbV1Kl_l1lvGTVAMMUqQYrll9XOEnEnyVBRZm-eKQXmG7Hi91RXUvkyxzjWnbocmV37o1xhu4kKS7zoR2ohm64nj68X5C60-7EZdYYOGrRZPgWrRT4FXaMl5rgBIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
منابع عربی از حملات پهپادی به مقر تروریست‌های تجزیه‌طلب در شمال اربیل خبر دادند.  @Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/452995" target="_blank">📅 21:16 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452994">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e63bc2605.mp4?token=FSHoHAdDSLcTo3hi1NMJbS3qEUcVXJxJBaThO-Jp7pSkUuRpR97Iexj_qmdBWlQOusBLIlucnmUvAe8nSrE6rv20n3C8LLOtp9Uo6ywR7ycRQtOJbVPSov_2CflM36E3zmCwL1wWFHBH3KlUSUmA1GYn-jvwpQVScMOsf0pYNd6IHg6tqqGjih_PcyuG8jDKp35KxNo-faNsUNs2WnWTRyvEQBzzILuW6EkVfk6nCjSRSPDYzqUo7l6U-EmLfb6xChmhyMcPfghPsm5nGWgCPVx6flv2HinLzOl74hbRmIXp2200gtHz9mOOwuJrffLdbP_3V2hoaz_niJm2rRUn2G40zBqGeLpREmJWnDNV8puGlkqFdDTiD42nlJ6FnIU1afAc4c9_lbuhEBTlcEPyMPca7QRAucdUNYnV5EBXzMX_mWzf1A_zp7Do2taACGJE-AW9ecTaeHbKQO1ppPKzPH7jj1Tc_A38Rzqaz4dL4HxmAgBcfMnMHAGFfg9ehlDVK2h6CodpVlLQqJOhWl3TbUOPpyrO7MjsPR1EerwVp_afZtzozQwgVcdXbwp3WqNh_DPfEhwUGuF6R2vnMU-qZ2Mh5hJ0ndLrLpM0Qk2-1wg9TCboAEORaFdjP5prZ-AtiLUCajh6p-ZiuVdPrEPM16Bhrl6klvkaMzu7HjPkW1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e63bc2605.mp4?token=FSHoHAdDSLcTo3hi1NMJbS3qEUcVXJxJBaThO-Jp7pSkUuRpR97Iexj_qmdBWlQOusBLIlucnmUvAe8nSrE6rv20n3C8LLOtp9Uo6ywR7ycRQtOJbVPSov_2CflM36E3zmCwL1wWFHBH3KlUSUmA1GYn-jvwpQVScMOsf0pYNd6IHg6tqqGjih_PcyuG8jDKp35KxNo-faNsUNs2WnWTRyvEQBzzILuW6EkVfk6nCjSRSPDYzqUo7l6U-EmLfb6xChmhyMcPfghPsm5nGWgCPVx6flv2HinLzOl74hbRmIXp2200gtHz9mOOwuJrffLdbP_3V2hoaz_niJm2rRUn2G40zBqGeLpREmJWnDNV8puGlkqFdDTiD42nlJ6FnIU1afAc4c9_lbuhEBTlcEPyMPca7QRAucdUNYnV5EBXzMX_mWzf1A_zp7Do2taACGJE-AW9ecTaeHbKQO1ppPKzPH7jj1Tc_A38Rzqaz4dL4HxmAgBcfMnMHAGFfg9ehlDVK2h6CodpVlLQqJOhWl3TbUOPpyrO7MjsPR1EerwVp_afZtzozQwgVcdXbwp3WqNh_DPfEhwUGuF6R2vnMU-qZ2Mh5hJ0ndLrLpM0Qk2-1wg9TCboAEORaFdjP5prZ-AtiLUCajh6p-ZiuVdPrEPM16Bhrl6klvkaMzu7HjPkW1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایتی از پاسخ رهبر معظم انقلاب به لبیک رزمندگان مقاومت در لبنان
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/452994" target="_blank">📅 21:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452993">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1561c99235.mp4?token=B85k4KsYXBmobbAm8FmX_IBjm8AYs9w1Pvvza1cllsXSi548LAOvbPV5wffRl-cSSrkJO3zu8-UB-xTRbADWwkJo8wynI7McR78MobnT5QqnLMSILnyjhgww6EFVtARMiqCBRftxBkv7Av8o0dTfI7jhZs9UtaoaxSxJChP-FaBgNeB9rrfBREa7kUoR1ncLTPLibnWImmycfdXC7TRpvuXWYKyp36T8HxUDfQDbHpPDea0-WNDNpqrKoHqkyE6yO1MxgQxCGAQiaTIbMUs6qOlNFvJmYxgmxG4skwoYJRp5lYtnz0k7-Vot102N3-TAVfk6Ny8EzN3X00jL4eb98w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1561c99235.mp4?token=B85k4KsYXBmobbAm8FmX_IBjm8AYs9w1Pvvza1cllsXSi548LAOvbPV5wffRl-cSSrkJO3zu8-UB-xTRbADWwkJo8wynI7McR78MobnT5QqnLMSILnyjhgww6EFVtARMiqCBRftxBkv7Av8o0dTfI7jhZs9UtaoaxSxJChP-FaBgNeB9rrfBREa7kUoR1ncLTPLibnWImmycfdXC7TRpvuXWYKyp36T8HxUDfQDbHpPDea0-WNDNpqrKoHqkyE6yO1MxgQxCGAQiaTIbMUs6qOlNFvJmYxgmxG4skwoYJRp5lYtnz0k7-Vot102N3-TAVfk6Ny8EzN3X00jL4eb98w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لامرد همچنان در میدان مقاومت، وفادار به فرمان رهبر
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/452993" target="_blank">📅 21:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452992">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43dd943d6b.mp4?token=MJIJy8hWPlbV0W3eLWkvurAF3Ep6cpu_WQKW56cleJhD47TDSnRshg7OiHF_v1_exMJVapfpGyjA_cG42YqOyz1HmKHU4L_aYRgFoL-PwhGu9BWR5soqPdFNq-rFCBBKT6UhRyip6epeehr9YWdb88iraQpT7FsK82Ur8GKu-VWkb97KznAFktUgRscK74kVbZcD_t1bkcH1zBwA6Y59Jde9aU2uI5ku5_4E89wfAY1SOEvX-WYE8iaYVFsyBhej7CjL6eJzuOi2OB1WqEr6rj7ikvTJ4GYA1WzSvKNaqBh5P_9cG-tqlOz1eaRxn2KdzdY1w_5OIZTe9vpBRXb8Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43dd943d6b.mp4?token=MJIJy8hWPlbV0W3eLWkvurAF3Ep6cpu_WQKW56cleJhD47TDSnRshg7OiHF_v1_exMJVapfpGyjA_cG42YqOyz1HmKHU4L_aYRgFoL-PwhGu9BWR5soqPdFNq-rFCBBKT6UhRyip6epeehr9YWdb88iraQpT7FsK82Ur8GKu-VWkb97KznAFktUgRscK74kVbZcD_t1bkcH1zBwA6Y59Jde9aU2uI5ku5_4E89wfAY1SOEvX-WYE8iaYVFsyBhej7CjL6eJzuOi2OB1WqEr6rj7ikvTJ4GYA1WzSvKNaqBh5P_9cG-tqlOz1eaRxn2KdzdY1w_5OIZTe9vpBRXb8Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس قوه‌قضائیه: با کارگزاران متخلف بدون اغماض برخورد می‌شود
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/452992" target="_blank">📅 20:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452991">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30d5f50cce.mp4?token=OMYr2j0-SaJTyfL2CU4LuahPfHHh1zRH48NEhG3NTYbQQX8yhBU33oYX0R9MgH2IbMvr7b0P_ZXIksxODX6SxSuueyeao5DcLgn_DNs_TdoalhJTdBh69qrwQJ04CR1_h-WZt-5KUudBfqJKDangxWFsv52gMx_zjFJW6w4y3SC1YqX1MXFXR5o1Bh1seMySoT5tq0nGsxjYfVajjpxa6vc4ZJQGb4uF0bIwm8sVry0X_osWdUxm4tr6HVUqHmsVU35X2mCMYgR096j91tXOAedEjupKV7Qh4mRGQ5eFXr0MogbqMHDkRzAgK5tDx3pJl6Eu8Xr12tTHFmh_J5DdOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30d5f50cce.mp4?token=OMYr2j0-SaJTyfL2CU4LuahPfHHh1zRH48NEhG3NTYbQQX8yhBU33oYX0R9MgH2IbMvr7b0P_ZXIksxODX6SxSuueyeao5DcLgn_DNs_TdoalhJTdBh69qrwQJ04CR1_h-WZt-5KUudBfqJKDangxWFsv52gMx_zjFJW6w4y3SC1YqX1MXFXR5o1Bh1seMySoT5tq0nGsxjYfVajjpxa6vc4ZJQGb4uF0bIwm8sVry0X_osWdUxm4tr6HVUqHmsVU35X2mCMYgR096j91tXOAedEjupKV7Qh4mRGQ5eFXr0MogbqMHDkRzAgK5tDx3pJl6Eu8Xr12tTHFmh_J5DdOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از آتش‌سوزی هتل استقلال تا ضرب‌وشتم خبرنگار صداوسیما
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/452991" target="_blank">📅 20:58 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452990">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdda014de4.mp4?token=VAaAFKeGbSLEMbgQrRQZc9Mk9D9gpIy-uO1UEObbpnMrk8XuP7v-MJJs1hqggprxYtCG1SlEWa61pIj7Bq-XENlyc0GWA3BdfSY3vYbXvVUSkzA0Nf3HFDr0yk5gi3-hB99Z8LVsPZsQbbuxx_vexWqDjGAUYeniGnXmas8Mw3ybH8HlaFTnUxj-Jxt1jp-jttUss5-deapWGFj478v-bjXrntKmYfXaxveTsNsRewZXoiRjsyJRFFHu8rH-9zT4YOZ_sTBlZdpQlM-c0VYwnU42B2iGGzAE6DomtPIS4XO4qBQblW3SISUSVp8_LDhVY-FnfT9D8yqeaY4DbaeJXUtrYzaKgMfKOk0ugPRnfhymJTVpsWRtiD5GFqJxbuAk_W2SsAepWlODSBp6HabmygJqqmHb5i4R84ixqjs1FGYpWXYZZ93-YnqgIiJ-0G8Z9HD0zexyyTAqLQkTeHbXEzgBArrscZlNQejZSGswS9056RuxIEVqds16X6X_H-qY8u-Ntfn7dxm4_UXS0fw7pdesbGbjwYSkR7X3NzDaYdHwTpUysDmY9vAzYl_hh5o_Kut0ztZpS4_Wali4n6nSlzfmyHElVa-Zeduh3U4p9pIWke67Nnedek6Opn29ROr6Qc_FLx4K_84zqeedlamdDX0CNiNfK9sL0zsF-CJZRxs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdda014de4.mp4?token=VAaAFKeGbSLEMbgQrRQZc9Mk9D9gpIy-uO1UEObbpnMrk8XuP7v-MJJs1hqggprxYtCG1SlEWa61pIj7Bq-XENlyc0GWA3BdfSY3vYbXvVUSkzA0Nf3HFDr0yk5gi3-hB99Z8LVsPZsQbbuxx_vexWqDjGAUYeniGnXmas8Mw3ybH8HlaFTnUxj-Jxt1jp-jttUss5-deapWGFj478v-bjXrntKmYfXaxveTsNsRewZXoiRjsyJRFFHu8rH-9zT4YOZ_sTBlZdpQlM-c0VYwnU42B2iGGzAE6DomtPIS4XO4qBQblW3SISUSVp8_LDhVY-FnfT9D8yqeaY4DbaeJXUtrYzaKgMfKOk0ugPRnfhymJTVpsWRtiD5GFqJxbuAk_W2SsAepWlODSBp6HabmygJqqmHb5i4R84ixqjs1FGYpWXYZZ93-YnqgIiJ-0G8Z9HD0zexyyTAqLQkTeHbXEzgBArrscZlNQejZSGswS9056RuxIEVqds16X6X_H-qY8u-Ntfn7dxm4_UXS0fw7pdesbGbjwYSkR7X3NzDaYdHwTpUysDmY9vAzYl_hh5o_Kut0ztZpS4_Wali4n6nSlzfmyHElVa-Zeduh3U4p9pIWke67Nnedek6Opn29ROr6Qc_FLx4K_84zqeedlamdDX0CNiNfK9sL0zsF-CJZRxs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روستایی که نانش را نذر زائران کرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/452990" target="_blank">📅 20:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452989">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/221125e133.mp4?token=LK99ctzy-Hf-l7_oCTdI6tuaf4W2wKc1r3jve82WbvjUa1GnW65b126IrdKZQbvyF2stViyqb-ttGXmMRzeVzKuKV4CEGbAm7HtOQZ9OvQl14XQEtG0PGqksErHB7dQfalwfBKesGZT2u4qyueQXrqFaULcdLxpVtYHkTkRaElOh1BkGmc-BMeilBdhamQ12C_iYWY4ubTsxnBq_DXjcdU1zhDAmEx9JInWincI2C99qzgpaMihyFYZFWLWXUn-K2GkdebiVeLY9YGpYEVF3JLt-jyM0bHSdVHReVed0nppniCP2Prk-NxG-nzEkDkcxewfTh8HIeZAJByfN98k5BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/221125e133.mp4?token=LK99ctzy-Hf-l7_oCTdI6tuaf4W2wKc1r3jve82WbvjUa1GnW65b126IrdKZQbvyF2stViyqb-ttGXmMRzeVzKuKV4CEGbAm7HtOQZ9OvQl14XQEtG0PGqksErHB7dQfalwfBKesGZT2u4qyueQXrqFaULcdLxpVtYHkTkRaElOh1BkGmc-BMeilBdhamQ12C_iYWY4ubTsxnBq_DXjcdU1zhDAmEx9JInWincI2C99qzgpaMihyFYZFWLWXUn-K2GkdebiVeLY9YGpYEVF3JLt-jyM0bHSdVHReVed0nppniCP2Prk-NxG-nzEkDkcxewfTh8HIeZAJByfN98k5BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش پاسخ یمن به تجاوز جدید عربستان
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/452989" target="_blank">📅 20:54 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452988">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/774ce2727b.mp4?token=tbwWapLaKy8VBT_ikpgHxh3GafCyRQOwoT1mraXd1mjX5gQJd9ur2DW3aF-QabHIY_fi4_o0Xc4ycX78zFre9I6ebPOM8xjSbtlqKzWSWMTB5vbxbgGpJmnHBPLpBTdrZZBT7-3-ROQw_0yw44nZTHbP37kRJvQixfNGz2JqR1YH9tK8-L42ou9AXdX9XK7OoKC0qEG3SnnI-bm4Ex9Yd6P52JmNwU3dg-ncxSmzlyrlhelzraUhy6hJyqBfNElPFB2tvnc11CAbSLMms2AKjroyFwcqhhOE8Vl6LOv3TKp2HhNMo8EgkCgkXiN5dj2tN_V53r9-Q1Kzj62kmvXo9pG8vxtjBbedwTqJqcyZhEukYFTJ_-sdpoK3ZtdYRUI8AYZRjxWC8YE22jFMeetD_umE29viEZOhJn4r33JzddEvH5QdKl-EYzuL2BpkP_N9EKovpZ5IrJ7Jsmzv_A-c9-TxO5-YFHIlruS5kAbw6v_fm5GCoIMEYptxUahHVvzesyPGGKO27ZeEqZ2XKokDZsEwFC7y88OcLWB4kRwtSG-Wm7yTTNJR84ptaoKxuFJtLpi-3lfuqJLovNRvShXIEjLbvdxPHKRmqvW5y6S0qwFWzpdIfC4-p218n5o3of0JCwBMhp34j8WmHtOuKU6Oz7BFpraRAbdIjgnC6k1gNIY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/774ce2727b.mp4?token=tbwWapLaKy8VBT_ikpgHxh3GafCyRQOwoT1mraXd1mjX5gQJd9ur2DW3aF-QabHIY_fi4_o0Xc4ycX78zFre9I6ebPOM8xjSbtlqKzWSWMTB5vbxbgGpJmnHBPLpBTdrZZBT7-3-ROQw_0yw44nZTHbP37kRJvQixfNGz2JqR1YH9tK8-L42ou9AXdX9XK7OoKC0qEG3SnnI-bm4Ex9Yd6P52JmNwU3dg-ncxSmzlyrlhelzraUhy6hJyqBfNElPFB2tvnc11CAbSLMms2AKjroyFwcqhhOE8Vl6LOv3TKp2HhNMo8EgkCgkXiN5dj2tN_V53r9-Q1Kzj62kmvXo9pG8vxtjBbedwTqJqcyZhEukYFTJ_-sdpoK3ZtdYRUI8AYZRjxWC8YE22jFMeetD_umE29viEZOhJn4r33JzddEvH5QdKl-EYzuL2BpkP_N9EKovpZ5IrJ7Jsmzv_A-c9-TxO5-YFHIlruS5kAbw6v_fm5GCoIMEYptxUahHVvzesyPGGKO27ZeEqZ2XKokDZsEwFC7y88OcLWB4kRwtSG-Wm7yTTNJR84ptaoKxuFJtLpi-3lfuqJLovNRvShXIEjLbvdxPHKRmqvW5y6S0qwFWzpdIfC4-p218n5o3of0JCwBMhp34j8WmHtOuKU6Oz7BFpraRAbdIjgnC6k1gNIY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم در دفاع از ایران، در همهٔ کمین‌گاه‌ها محکم ایستادند
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/452988" target="_blank">📅 20:52 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452987">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fa9vn52DwtMtHK1j8VQOhkRNOHt36ik5RfVRUYINUdMXvIr76_zPKdkzWs35bfuzgsGbXtQUtAnzKSQZMAZgdPcj8hLramwvjzak0KMCJBErkh_UY65EFbD7Boyu4Hb4EFfVDuj6jnxRSSCdLIfjS6BiEPyy2jWn3jKYXFcHIxKjSDNGt3k8FsNKjC68IMMUGyW6dMkzLeDXlF5KQzj4p5_RgqgIVWOjlXYe3M2heZR-ODq_qV0NF3qrfB4Kif5x-ZzhcC351Pe7Cog_eu3Ote3CnksSZLHzjZuea2XwSu9cyRcPwnRY8dXCqQuuxqZ0vhLckbzIypR1rLaxGp-xBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غریب‌آبادی: جنایت‌های جنگ علیه ایران را تا آخر پیگیری می‌کنیم
🔹
معاون حقوقی وزارت خارجه: طبق تاکید رهبر انقلاب حتی اگر پیگیری یک پروندۀ مرتبط با جنایات آمریکا ۱۰ تا ۱۵ سال زمان ببرد، نباید روند رسیدگی متوقف شود.
🔹
تاکنون صدها سند از جنایت‌های جنگی تهیه و بیش از ۱۴۰۰ صفحه گزارش و مستند حقوقی برای ثبت در مجامع بین‌المللی آماده شده است.
🔹
بیش از ۱۲۰ سند دربارۀ نقش برخی کشورهای حوزۀ خلیج فارس در تجاوز اخیر تهیه و در شورای امنیت ثبت شده و در این اسناد، زمان، محل و مبدأ حملات به‌طور دقیق مستند شده است.
🔹
پیشنهاد کردیم برای رسیدگی به پرونده‌های جنایت‌های جنگی آمریکا دادگاه ویژه تشکیل شود. رسیدگی به ده‌ها هزار پرونده نیازمند سازوکار ویژۀ قضایی است.
🔹
ایران پیگیری حقوقی جنایات آمریکا را در سه مسیر دنبال می‌کند: محاکم داخلی، محاکم خارجی بر پایۀ اصل صلاحیت جهانی و طرح دعوا در مراجع بین‌المللی.
🔹
با استناد به کنوانسیون شیکاگو، روند حقوقی لازم برای استفاده از ظرفیت دیوان بین‌المللی دادگستری علیه آمریکا را آغاز کرده‌ایم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/452987" target="_blank">📅 20:48 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452986">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
منابع لبنانی: رژیم صهیونیستی ارتفاعات علی الطاهر در جنوب لبنان را هدف حملۀ توپخانه‌ای قرار داده است.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/452986" target="_blank">📅 20:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452985">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQhDtmidu5xQGILeqkmzKGSiDPChbn-GeD6MSaJRGmHY6H9DEFhBaO-JbEqWTpliBeEierQuHmOnPQSjjlYQcHpwQvpp-NNdmvyLLk4HzSWGg6vY-Q5VEv5ZOKeq-Fh8Qnm2mjHLymrrtGEHWr-Qax2oH1I1i_IvDxdD2FK8hU0V3TLPc-UdGBzUiAD4Zfk2_9zOAFquIJZ5qEXioaDyUTHVF2ZN79P19iJ9CO-iPk8getEZEwPu3HfeE27DV2eMMj671axEYcSeEmMRD5uwIS9v2wmVBtKj9W5B7BEQeIM3bvR6nPl_1Lu89cmj350nBwm5NZSonT_hLv2rh2TOzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ما چندین میلیارد دلار از ونزوئلا درآمد به‌دست می‌آوریم؛ این اتفاق دربارۀ ایران هم خواهد افتاد  @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/452985" target="_blank">📅 20:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452984">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">چرا بخشی از سخنان رئیس‌جمهور و رئیس مجلس در صداوسیما حذف شد؟
🔹
اسفندیاری، رئیس دانشگاه صداوسیما: مطلب مطرح‌شده در سخنرانی رئیس‌جمهور چندی پیش در دیدار با مدیران صداوسیما نیز مطرح شده بود. فیلم آن جلسه را دفتر ریاست‌جمهوری تدوین و برای پخش به صداوسیما ارسال کرده بود.
🔹
جالب این‌که در آن فیلم، دقیقاً همین بخش مورد اشاره حذف شده بود! یعنی این هجمهٔ سنگین علیه صداوسیما به بهانهٔ حذف جمله‌ای برپا شده است که پیش‌تر خودِ دفتر ریاست‌جمهوری هم به‌درستی آن جمله را از سخنرانی ایشان حذف کرده بود.
🔹
جملهٔ مورد اشاره در این سخنرانی، نقل‌قولی از جلسه‌ای خصوصی میان رهبر شهید انقلاب و رئیس‌جمهور بوده است. طبق قواعد و ضوابط حرفه‌ای و پروتکل‌های رایج در تنظیم و انتشار اخبار مربوط به رهبر معظم انقلاب، هرگونه نقل‌قول از جلسات خصوصی و محرمانهٔ ایشان ممنوع است و انتشار چنین مطالبی صرفاً منوط به تأیید دفتر مقام معظم رهبری است.
🔹
این رویه که در زمان حیات رهبر شهید رایج بود، طبعاً در شرایط فعلی و پس از شهادت ایشان باید با حساسیت بیشتری رعایت شود. اگر بنا شود هرکسی برای توجیه اقدامات فعلی خود، نقل‌قولی از جلسات خصوصی با رهبر شهید انقلاب مطرح کند، با هرج‌ومرج و آشفتگی روایت‌ها مواجه خواهیم شد.
🔹
متأسفانه همین نقل‌قول اخیر رئیس‌جمهور محترم نیز دستمایهٔ سوءاستفادهٔ برخی عناصر ضدانقلاب و منافقین خارج از کشور قرار گرفت و زمینه‌ساز اهانت و توهین به رهبر شهید انقلاب شد.
🔹
همهٔ ما بند آخر وصیت‌نامهٔ امام خمینی (ره) را به‌خاطر داریم که ایشان تصریح می‌کنند: «آنچه به من نسبت داده شده یا می‌شود، مورد تصدیق نیست؛ مگر آن‌که صدای من یا خط و امضای من باشد، با تصدیق کارشناسان؛ یا در سیمای جمهوری اسلامی چیزی گفته باشم.» براساس این حکم امام خمینی(ره)، هرگونه انتساب نقل‌قول به رهبری شهید انقلاب که خارج از اسناد و مدارک موجود باشد، باطل و غیرمعتبر است.
🔹
این امر دربارهٔ رهبر شهید نیز طبعاً صادق است و آقای رئیس‌جمهور که خود از پیروان «خط امام» هستند، قطعاً بیش از همه باید به رعایت این اصول و ضوابط در نقل‌قول از رهبر انقلاب پایبند باشند.
🔹
در مورد عدم پخش بخشی از مصاحبهٔ رئیس مجلس نیز سازمان صداوسیما بر اساس برخی سیاست‌های ابلاغی، پیشنهاد حذف ۲ دقیقه از مصاحبهٔ ایشان را مطرح کرده بود که پس از بررسی موضوع در جلسه‌ای با حضور نمایندگان نهادهای مختلف و مراجع ذی‌صلاح، نه‌تنها نظر سازمان صداوسیما صحیح تشخیص داده شد و مورد تأیید قرار گرفت، بلکه مقرر شد ۱۸ دقیقه از آن مصاحبه حذف شود.
🔹
این موضوع همان زمان به اطلاع تیم رسانه‌ای رئیس مجلس نیز رسید؛ لذا در پخش دوم، با وجود انجام این اصلاح، هیچ‌گونه اعتراضی مطرح نشد.
🔹
در مورد پخش مصاحبه‌های وزیر محترم امور خارجه با خبرنگاران خارجی نیز معمولاً با توجه به برخی اظهارنظرهای خلاف واقع، ضد منافع ملی و اظهارات سوگیرانهٔ خبرنگاران خارجی علیه ایران، پخش کامل این مصاحبه‌ها در دستور کار رسانهٔ ملی نبوده است.
🔹
هیچ درخواستی نیز از سوی وزارت خارجه برای پخش کامل این مصاحبه‌ها مطرح نشده است. ضمن این‌که اصولاً پخش کامل مصاحبه‌ای که توسط رسانه‌ای دیگر انجام شده، جز در موارد استثنا، خلاف اصول حرفه‌ای رسانه است. معمولاً رسانه‌ها به پخش بخش‌هایی از مصاحبه‌هایی که توسط دیگران انجام شده، اکتفا می‌کنند.
🔹
اگر از نظر وزیر خارجه، یک مصاحبهٔ خارجی ایشان ارزش پخش کامل در فضای داخلی را داشته، طبعاً می‌توانستند از مرکز رسانه‌ای خود درخواست کنند که آن را طبق نظر خودشان ترجمه کرده و در اختیار رسانه‌های داخلی قرار دهد.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/452984" target="_blank">📅 20:28 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452983">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k5TMuZDtxuYSXgeqlY7hmNTfchLFZPWANB97f-4sbrjGl11Md-8wEPGx9Cy_m33ggCZmNE6GJLDSc958roo4XQiaWWwuuMxOgBQbcPmebcqXBAhoMbX1n1VMVvkClgCNnlGI_lVA3ZmJcsbKx6NwkR_Z0hqAbgVJlsGQZJXKiaqJxwTBOwgBX5JWhZCQJfdQacnsDNr-EUv9IFFa4ZidWOdeGYcL6JgUVDD9hL7XDXASzZdTeeTCH2-dUhG6WTeu_tMX9e3WPqKGIWkNbCn4mDAksmqXscqNcHQMFyqYo0P4VBsScD4AodFDinvuwaXfDbjgmQ_o25TvhhRH3xrENQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این لوازم الکترونیکی را به اربعین نبرید
🔹
قاعده کاربردی بستن کوله‌پشتی اربعین، سبکی و حذف بار اضافه است. در این مسیر طولانی، گوشی هوشمند و یک پاوربانک استاندارد تنها ابزارهای الکترونیکی ضروری شما هستند.
🔹
دوربین عکاسی و لپ‌تاپ را فراموش کنید. وزن زیاد، آسیب‌پذیری در برابر گرما و ضربه، و نبود فضای شارژ، آن‌ها را به باری اضافه تبدیل می‌کند. دوربین موبایل برای عکاسی زائران عادی کاملاً کافی است. همچنین به جای مونوپادهای سنگین و دست‌وپاگیر، در صورت نیاز از پایه‌های کوچک جیبی استفاده کنید.
🔹
برای حفظ آرامش و خلوت معنوی مسیر، همراه داشتن اسپیکر بلوتوثی اصلاً توصیه نمی‌شود؛ هندزفری شخصی بهترین جایگزین است. همچنین از آوردن سشوار که صرفاً فضای کوله را اشغال می‌کند خودداری کنید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/452983" target="_blank">📅 20:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452982">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVO4m5Pr1_Kb4gHEfmjgQ9nCs1dLJoziD0RD2LC1Vnz5szCEuzpodTJ_cSXQT7AL1-crZBRlnCaQdZtsvAwGN62Pl5H4mKqp64-wg-sKtvlG589p0STREyZBoDF2cqLpeColSjhGSA_2q5ZjMLq1bXLkud7KuQizM6hH8HE-PZbHSFqOqrsT-X5vHnv8RvYXMjymauRkdnyaNX15KvjxEJ0feBP6RlX6t9Ter6_xGxQlRCadTSXRFl4gik_ecZlaSjmgxhQmMGstk50JqPepnU6cvBXvabBZCKOf8j-Dt-p4565AIZRuyrRFFoxV3v4eO1Nk_g7gfqCinMFqnU69Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ما چندین میلیارد دلار از ونزوئلا درآمد به‌دست می‌آوریم؛ این اتفاق دربارۀ ایران هم خواهد افتاد
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/452982" target="_blank">📅 20:18 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452981">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4511afd4f2.mp4?token=YVuzrgBT8aHkpKVotdHWtzTsu7oMwd1jmPrNAJNSDOg_97XPQSWGN0bSKo6eM1dIvHL36tWgI8wcKe8hqhmlU4tUVyUFOv_T1FLqQWbAzuD_3hm3ctOARHwpKK0XBLKrG64ys8qrcIk2E760feUnrPN5-vhv49sLlymQz6JZ-NCawI77S-3uuZvYZlycXsFKvRjpc_KAqlkhWbqh-CmqveRizxjt2uhA7d_qDMdTcAFk5Hf_40aLRkl2D6w-KOHtRvA3Z2y6QWUAZOJD__1ei2JE8mDHRAQMB56Zc9OfO6A-zqk1VVMgx3nWxThNZZs3OkZrV4avowrtXs-6X2P4KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4511afd4f2.mp4?token=YVuzrgBT8aHkpKVotdHWtzTsu7oMwd1jmPrNAJNSDOg_97XPQSWGN0bSKo6eM1dIvHL36tWgI8wcKe8hqhmlU4tUVyUFOv_T1FLqQWbAzuD_3hm3ctOARHwpKK0XBLKrG64ys8qrcIk2E760feUnrPN5-vhv49sLlymQz6JZ-NCawI77S-3uuZvYZlycXsFKvRjpc_KAqlkhWbqh-CmqveRizxjt2uhA7d_qDMdTcAFk5Hf_40aLRkl2D6w-KOHtRvA3Z2y6QWUAZOJD__1ei2JE8mDHRAQMB56Zc9OfO6A-zqk1VVMgx3nWxThNZZs3OkZrV4avowrtXs-6X2P4KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
«عمو لیندسی» که امروز مُرد که بود؟  @Farsna - Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/452981" target="_blank">📅 20:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452980">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGvDAKeVGsuko7r0sVR5iHi32sKSYRJXyrAC2cEb8aex6Y60Mn7iikbc7UFODACq5Lcgf0Fwc7KCARaMcFZUePqSOtdM5IxxjUw90763oIcxHQKXcTHyT3TwDypyK72YHkLkCPDqYm7LWP4Dcjzk41UjsPJ3-wAevLq5ZwyofUynTEyhOi6euTRF6riw1VoJP9QNVbQi0YXPhweiSEn2c9fK_kSIXlXwCRniLHHjAP8HwwKY4mbnAXlbKR5_4e8X3La-473OCEl2TPcPC0ihtjwq4cwxMXZyJO6jQvApAfpPemOrCSiC-ToFPwIiwWlW99ycDZLL7BkcF0T-0IPIQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۹۰ درصد درآمد نفتی عربستان دود شد
🔹
شرکت اطلاعات دریایی «وایندوارد» اعلام کرده که بارگیری نفت در بندر ینبع عربستان از ۲۹ تیرماه به بعد حدود ۴۰ درصد کاهش یافته.
🔹
بندر ینبع در غرب عربستان یکی از مهم‌ترین پایانه‌های صادرات نفت این کشور در سایه انسداد تنگه هرمز به شمار می‌رود
🔹
در مجموع صادرات نفت عربستان با بسته‌شدن ۲ آبراه استراتژیک هرمز و باب‌المندب به روی کشتی‌های سعودی از ۸ میلیون بشکه به ۲.۴ میلیون در روز سقوط کرده.
🔹
این یعنی روزانه ۵۰۴ میلیون دلار ضرر که ۹۰ درصد کل درآمد نفتی عربستان را شامل می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/452980" target="_blank">📅 20:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452979">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c8ce517b4.mp4?token=CSNDW86uwaz0uuMEhMFRuHeuRRkOawmPBEY4dFSW7z8L0OuHshtilHu3GEdvRUm7Ck53NqMj1wEgr6xGAepz-HXzBLQh_wJUwtpK9rVsQMCUNz5UoIiHpzqShdOwn64QRoZ3KlSpa_QQoEkeqgjCFNIB7DHle5WZ1DKGXioaS7W4fhYZzMnVbSg12pNb1YSjoh7fUZ9eFWF7XzaAxe266BXEU1Cyus6pfoH4SamUTkb8Z2_UmLS8Z7t8lyuy9zb8LloyJgcWcvFc0BrT1x3KUOUFuglbctoJ9FFXt6bNb7mrjPEkWnX94urz6Fn48C3hV8tAKtoEGwrbaDyyyOHwNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c8ce517b4.mp4?token=CSNDW86uwaz0uuMEhMFRuHeuRRkOawmPBEY4dFSW7z8L0OuHshtilHu3GEdvRUm7Ck53NqMj1wEgr6xGAepz-HXzBLQh_wJUwtpK9rVsQMCUNz5UoIiHpzqShdOwn64QRoZ3KlSpa_QQoEkeqgjCFNIB7DHle5WZ1DKGXioaS7W4fhYZzMnVbSg12pNb1YSjoh7fUZ9eFWF7XzaAxe266BXEU1Cyus6pfoH4SamUTkb8Z2_UmLS8Z7t8lyuy9zb8LloyJgcWcvFc0BrT1x3KUOUFuglbctoJ9FFXt6bNb7mrjPEkWnX94urz6Fn48C3hV8tAKtoEGwrbaDyyyOHwNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نامی که علیه اشغالگری جنگید، اما بر پایگاه اشغالگران نشست
@Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/452979" target="_blank">📅 20:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452978">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c068750ffd.mp4?token=diiwGC4_MHn2sXphdJQ_n7bugkfRJJxkYl__O3fivEs2bcQPuMDAZ1j9oRKTIjXpVZLy6pBCdmaaA_EjeX_lc7s5yuR3iOlEQMubBYMA_ZIqcBgpPgK9CV1fCtkNM7_c5m8IPfpUGL6LbjWjJabUWUuMRWmpkE0LUb93tKo9y99uivvAoG4Q62b_GqI6MnTa7HdgJeOhuitvapo9bE639xoo-FVe8uHPzW7LWSGK5nNt_XhBoanG0fyF_aLH6dGSdE4-frX2G4ecGRFbJHcJW-g70msL-D37Bp0zEbPC23BgdhwPkrQyPQxrdmMX-LTrG2zKxcuDQrfiwzPEWceBaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c068750ffd.mp4?token=diiwGC4_MHn2sXphdJQ_n7bugkfRJJxkYl__O3fivEs2bcQPuMDAZ1j9oRKTIjXpVZLy6pBCdmaaA_EjeX_lc7s5yuR3iOlEQMubBYMA_ZIqcBgpPgK9CV1fCtkNM7_c5m8IPfpUGL6LbjWjJabUWUuMRWmpkE0LUb93tKo9y99uivvAoG4Q62b_GqI6MnTa7HdgJeOhuitvapo9bE639xoo-FVe8uHPzW7LWSGK5nNt_XhBoanG0fyF_aLH6dGSdE4-frX2G4ecGRFbJHcJW-g70msL-D37Bp0zEbPC23BgdhwPkrQyPQxrdmMX-LTrG2zKxcuDQrfiwzPEWceBaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آمریکایی‌‌ها از اسرائیل خسته شده‌اند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/452978" target="_blank">📅 19:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452977">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
منابع سوری: ارتش رژیم صهیونیستی درحال پیشروی به خاک سوریه از سمت حومۀ غربی درعا است.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/452977" target="_blank">📅 19:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452976">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/167fec05e0.mp4?token=IXv5JDayXuihtbls3t3RhDWd586Xcqn2iv6M9GAIhFXSPHn5DF2TL5eHasfWsvp51bBVt4p24towOGZpyCN5RnKl8ne1QwE5ssKJ-UpaCEwaZvfYW88QXHzhfhoOHDzCVVDAc8NXNOyPxhvLhn8grEP4sCeV3YO0GP4H_dewbxmwyAICBro-TRSE-LNwbzC3y-riJayTMBJ1UuNIjb8lxUDA9JCanqMiMhaiozhsHVq6ewWDgdWWPiYk32F3Bj_Ln3cHTjFgby8rqch6Aes5DbBmt90LaZqA8zhBcbmBe0qv8zVI8-LkG8NLi9X42jSx96ml276ag2bu9ZlYk4qFbBtcGBPZuOwFLikQgtV5KQZUtJQkb0wpNcMnDJu_0n9BvfqC1EK-dk_nzYgCtNzwaqOFEZduUMvU4XU9TBmHK6N7ul_ewl1zxGZArQLJecl8THu0UYEjsr3XxpwAEhSRavBf8hxuj557zBtefHnSC3Yuy3vHGMKROYmyiSpF-vn8q1n8vv7ZKQj4tV4BZplDfvof5e6yyw038_drZ06qS0ftInC7tyutfTnWqfWLVBXf5DnNrn7z_qdgDltMQO2_FOE-NdR04kzQxJazWOHlldNMxjHdJaraAGJq6DxZWKBiItUMuR1Pr0URwJS7gSsKdgcQkumiflcDHkDTqdkbVWI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/167fec05e0.mp4?token=IXv5JDayXuihtbls3t3RhDWd586Xcqn2iv6M9GAIhFXSPHn5DF2TL5eHasfWsvp51bBVt4p24towOGZpyCN5RnKl8ne1QwE5ssKJ-UpaCEwaZvfYW88QXHzhfhoOHDzCVVDAc8NXNOyPxhvLhn8grEP4sCeV3YO0GP4H_dewbxmwyAICBro-TRSE-LNwbzC3y-riJayTMBJ1UuNIjb8lxUDA9JCanqMiMhaiozhsHVq6ewWDgdWWPiYk32F3Bj_Ln3cHTjFgby8rqch6Aes5DbBmt90LaZqA8zhBcbmBe0qv8zVI8-LkG8NLi9X42jSx96ml276ag2bu9ZlYk4qFbBtcGBPZuOwFLikQgtV5KQZUtJQkb0wpNcMnDJu_0n9BvfqC1EK-dk_nzYgCtNzwaqOFEZduUMvU4XU9TBmHK6N7ul_ewl1zxGZArQLJecl8THu0UYEjsr3XxpwAEhSRavBf8hxuj557zBtefHnSC3Yuy3vHGMKROYmyiSpF-vn8q1n8vv7ZKQj4tV4BZplDfvof5e6yyw038_drZ06qS0ftInC7tyutfTnWqfWLVBXf5DnNrn7z_qdgDltMQO2_FOE-NdR04kzQxJazWOHlldNMxjHdJaraAGJq6DxZWKBiItUMuR1Pr0URwJS7gSsKdgcQkumiflcDHkDTqdkbVWI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بررسی تصاویری که ابعاد واقعی انهدام پایگاه های آمریکا را فاش می‌کند
🔹
کارشناس کانادایی: انهدام رادارهای راهبردی و دوربرد توسط ایران، شکاف‌های عظیمی در پدافند موشکی آمریکا و اسرائیل ایجاد کرده است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/452976" target="_blank">📅 19:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452975">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bd74a55e6.mp4?token=UjL7orpthD9D7IRr-FVjuTrOdYOH-CielsyQH0Z-LLEJlcVI3-ztxvY03ddPrSsQnaL9JZCCGTDHBPCo0RtOv7Q8LX4cWEbhU7iIpeiZhEwnDxFZGMBmFPCWoVY_m5MqDX9PRful_O0cZszeHo0t1n8taRlROBgKe2GBIUqCjnhtl35hQx_UKrFAaV4Cg74pbtYhD1F0JHgD2uT24zm0ZlzDldkUqg5gi35a1CY3S9C12UAqVt-jM6P2Evr2DWwzypp1GAvGmHBzhMvl8-ipIqBKYSZc5QxfGtBGC5y2Tx7WMDeIwpgRMuUAQSDm9_ez0lRZf8DD4bCuK7ZSPlH6aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bd74a55e6.mp4?token=UjL7orpthD9D7IRr-FVjuTrOdYOH-CielsyQH0Z-LLEJlcVI3-ztxvY03ddPrSsQnaL9JZCCGTDHBPCo0RtOv7Q8LX4cWEbhU7iIpeiZhEwnDxFZGMBmFPCWoVY_m5MqDX9PRful_O0cZszeHo0t1n8taRlROBgKe2GBIUqCjnhtl35hQx_UKrFAaV4Cg74pbtYhD1F0JHgD2uT24zm0ZlzDldkUqg5gi35a1CY3S9C12UAqVt-jM6P2Evr2DWwzypp1GAvGmHBzhMvl8-ipIqBKYSZc5QxfGtBGC5y2Tx7WMDeIwpgRMuUAQSDm9_ez0lRZf8DD4bCuK7ZSPlH6aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
پرچم‌های سرخ «انتقام امام شهید» در دست زائران خسروی  عکاس: بهروز احمدی  @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/452975" target="_blank">📅 19:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452974">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">دادستانی تهران علیه فلاحت‌پیشه و یک رسانه اعلام جرم کرد
🔹
پس از انتشار اظهارات یک نماینده اسبق مجلس که دوره‌ای ریاست کمیسیون امنیت ملی را در زمان نمایندگی‌اش برعهده داشت، دادستانی تهران علیه این فرد اعلام جرم کرد.
🔹
برای فرد مورد اشاره و همچنین رسانه منتشرکننده پرونده قضایی تشکیل شده است و به زودی با حضور در مرجع قضایی تفهیم اتهام خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/452974" target="_blank">📅 19:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-452973">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a95fa2c53.mp4?token=J90C7BaYvwrF0MHC-31BrjzaZykP2Grk8xvmcJ48GnROj84tW4XKYHM0r-KxtHYX_gT11Tx8ACVoJSEV9bEfveah-j1GUVqRkjGhNJDw92wr3HP7DaQJOlQ-diRpPn4k16c778KmUfUPHlhhBON-imNdretl6STJF0adQ7gjZK2h73NskMEOMPnmQ371p7TUEDnGMkpdcYOOLm0PshIe5FSi2Lt51WoftU9hPOdvY8dKowKRkI5hUAmnYVA_0YupO6Frw4zqSuQzVW56hpknZYxM6FO-XvlX2MGLAAwMAB_nuLp8jhXoNIviwGrXOPXRMxS1oTEA5_N1dOZTu8CHNI5C1JP29l7fIqfFtbvw6d0YCzZeD5nH01pOZdvIsx9UzbeuxeaNt8UGZeh2uDdgskeFWD7wJefDqtIt2ru3YpyzYMtDAwqckKrqhgOie69yttxwnG4WhQFzXFBAddfpYKqXCYxqgb9-sxGibEYef5v4zhItXBx_CqZM6Iw6fE2EF0xs1Tu6AnBxfJOsaV14P6Lxa_11seCZ6WAMPtNZbywWZvgoyUbsVjeZ-9ZKZdYs33QPACo89zuPKNlKc-kUuBeg1VWXQzcjeayqtI1MKtJGCzkCBaF2P_ODmtT82UNLv9IbpqiwxdLk3q6X0RO2NoNpOXi7zoSsC4wpNuKsDWo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a95fa2c53.mp4?token=J90C7BaYvwrF0MHC-31BrjzaZykP2Grk8xvmcJ48GnROj84tW4XKYHM0r-KxtHYX_gT11Tx8ACVoJSEV9bEfveah-j1GUVqRkjGhNJDw92wr3HP7DaQJOlQ-diRpPn4k16c778KmUfUPHlhhBON-imNdretl6STJF0adQ7gjZK2h73NskMEOMPnmQ371p7TUEDnGMkpdcYOOLm0PshIe5FSi2Lt51WoftU9hPOdvY8dKowKRkI5hUAmnYVA_0YupO6Frw4zqSuQzVW56hpknZYxM6FO-XvlX2MGLAAwMAB_nuLp8jhXoNIviwGrXOPXRMxS1oTEA5_N1dOZTu8CHNI5C1JP29l7fIqfFtbvw6d0YCzZeD5nH01pOZdvIsx9UzbeuxeaNt8UGZeh2uDdgskeFWD7wJefDqtIt2ru3YpyzYMtDAwqckKrqhgOie69yttxwnG4WhQFzXFBAddfpYKqXCYxqgb9-sxGibEYef5v4zhItXBx_CqZM6Iw6fE2EF0xs1Tu6AnBxfJOsaV14P6Lxa_11seCZ6WAMPtNZbywWZvgoyUbsVjeZ-9ZKZdYs33QPACo89zuPKNlKc-kUuBeg1VWXQzcjeayqtI1MKtJGCzkCBaF2P_ODmtT82UNLv9IbpqiwxdLk3q6X0RO2NoNpOXi7zoSsC4wpNuKsDWo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تنگه هرمز در ۱۴۰۵/۵/۵
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/452973" target="_blank">📅 19:24 · 05 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
