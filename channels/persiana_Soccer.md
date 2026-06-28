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
<img src="https://cdn4.telesco.pe/file/BuIeljnvCH4Dy_OvHVaKkCoDYWF8q11ZPScvC-zfUvJTqlsv_gMava8bts3q_3ET_PYXygpT28Vrf7fFAyCMwi4vA-MnZWgQ8ZGtb0JWO32SFy-dkGpZUd5pYQ9esOWO12esdIqFud7RukC8159nidbUMSJ87X2O1xxOp-VPEDUB0_D6i1aNd2nOPnMNt8RmgqSiTkbkw-Wf0xx6mFpFUPF23gfV5eqlf_rJiKHNVEhJVUhG-fYlMpxSfo-BC1eB-dflg0TZ5NaZYg1OnU9c9UlkzsW_zaxNpqAesrbXac_j8DTocUQumjei0UWjapwh3QePS4EnAA4yVgewUDMv5A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 335K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-07 23:20:52</div>
<hr>

<div class="tg-post" id="msg-24568">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6tCIl2IGgB-AM4JRDADFC-7H_fSZpdg2XRIdZhw2tCRl7oIGZWR3jcd76J7Q4p2Obi-j-FaKCZ7y3M8TY4kukwsklPQmJ16pTJPLkIpu1LycBQDi_MhWohohXVcFcgFPbUlpRJOYy6e6ZsWOVcMLn1rty-ftlEHVrigUchcuN4qUAabtNatB9aTsS1tvPst4TeDdjN3bsk0V6uNlX-cnlCupP8PunttUVnuh-gn2pBgUhjZFit-d4h_Gx3C7o6SacvY1ECEMNvS7QPnMxR84TrzuACeNY8M8vG4-zEKc814C245zMbcfLM6dCS9yII57u2ktEDXppqw0VGuHTUOBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
باپایان یافتن مرحله گروهی جام جهانی نگاهی بندازین به جدول برترین‌های آسیا در این رقابت‌ها؛ برخلاف عملکرد خیره کننده‌های نماینده های افریقا درآسیا تنها ژاپن و استرالیا راهی مرحله بعد شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/persiana_Soccer/24568" target="_blank">📅 23:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24567">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b02328cf0c.mp4?token=fb3Hn_TjYC5osEdUI1jFtg3fOk6wa_QQzqmZAnXyYheVLMkOrCBivMhSE9JUev0jBZL1WNDBpbCgULx6YaL6EYe1-t7OA7rbDLA9bx_akNHKohFLPMtvdu578VCj5ycncQWpoPdWJu-veE7oCAMTH9Obu8PzLGDWUGYUAXtoBTM1nDZtPtC1X92LiJq-ifWnatgLNAXeGiZmGKk5bU_CcJ39dWCD9WVkYO0rmqVC6A-Eo-6sFP9dCWvuZduCWXgiV_x1_U1AkS3e29EJBPh8hz2vX3u3yI5c0_Tns6T5S4m2KndzaDNbmucZeQ32twWE4bc1-gJGPAJSPCkE7jAZlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b02328cf0c.mp4?token=fb3Hn_TjYC5osEdUI1jFtg3fOk6wa_QQzqmZAnXyYheVLMkOrCBivMhSE9JUev0jBZL1WNDBpbCgULx6YaL6EYe1-t7OA7rbDLA9bx_akNHKohFLPMtvdu578VCj5ycncQWpoPdWJu-veE7oCAMTH9Obu8PzLGDWUGYUAXtoBTM1nDZtPtC1X92LiJq-ifWnatgLNAXeGiZmGKk5bU_CcJ39dWCD9WVkYO0rmqVC6A-Eo-6sFP9dCWvuZduCWXgiV_x1_U1AkS3e29EJBPh8hz2vX3u3yI5c0_Tns6T5S4m2KndzaDNbmucZeQ32twWE4bc1-gJGPAJSPCkE7jAZlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
سانتر خط‌ کشی‌ شده رامین رضاییان ستاره استقلال در بازی بامداد امروز ایران مقابل نیوزیلند؛ خیلی باید روحیه‌جنگندگی داشته باشی که با وجود یک‌فصل‌درخشان دراستقلال به تیم‌ملی دعوت نشی و سکوت کنی و فصل‌بعد با اومدن ریکاردو ساپینتو نیمکت نشین بشی و بازم سکوت کنی…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/24567" target="_blank">📅 22:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24566">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🏐
دربازی‌امشب‌آرژانتین - لهستان در لیگ ملت‌های والیبال ست اول این بازی به شکل برگ ریزونی 50 بر 48 به سود هموطنان لیونل مسی به پایان رسید. قشنگ به اندازه دو ست تو یه ست بازی کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/persiana_Soccer/24566" target="_blank">📅 22:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24565">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9cA1E7sn-nNCA9jf-hLytv5HD03V7PbdSlO2Uhz5y-Wlk6fkg491sdlpWncPeoQ5QgdXgbv6xTE_BOPj6Qe9469gc8b0HKxBGj4GMBsD08p362v6IwMmRUTWP0bo0MpSl_4UuTttcn8PKKeoM5ccHghX4T3LKyyLZMUIp3YDl7s6Bp0NS4i2U1VugZoWpjBa-ueopZIlviWjf_m48ubPUQPNRB1SyUvPt5xwTzS5JU5EEDRopVd5wv-HSLCjORNQLnf25N_1l2GAMs9LHZIrFwi_XdBDAHnU3_vh4uLhez6IE3xdiUbnjXj-SLLf_-KBwqRYxns-9NqzCLpHrcSdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
سرمربی تیم ملی مصر اعصابش از کارت زرد‌های مارسینیاک داور بازی این هفته با ایران بشدت عصبی شد و خواست‌که مشت بزنه دید آهنه گفت نمیصرفه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/persiana_Soccer/24565" target="_blank">📅 22:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24564">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/feee4e8bab.mp4?token=ehmSv33yzP2DgB3amIm0pVakAt_dVo9-mYoa7FkmPjGNJPw6A1MlRzyrQkMGrjoIF445kVovvYY-TBe7W4qx5Sj9CsoYkjbUjX7Wi_FtjBarbO7aAdu4kHy9F16UC89O06YpHTnlefNHjg5biZ-cmBXtUDBwenY4sJjg0i7pGwKnO1LPkZWPibURf-4PWkBpsTGtljN3OR1J6masKPPreVN56mEWmvWVsOa7L-8n4p1iq0mBbGHrOoRJIPQUQuIWpfPd1QsLQ3qA2BpSQEWaN5S2xOpxDtjBr1ItNrv3I47H_U2FfM1__d6PG2smvMZf-0JF9rlmwBjjDvhVgY7TFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/feee4e8bab.mp4?token=ehmSv33yzP2DgB3amIm0pVakAt_dVo9-mYoa7FkmPjGNJPw6A1MlRzyrQkMGrjoIF445kVovvYY-TBe7W4qx5Sj9CsoYkjbUjX7Wi_FtjBarbO7aAdu4kHy9F16UC89O06YpHTnlefNHjg5biZ-cmBXtUDBwenY4sJjg0i7pGwKnO1LPkZWPibURf-4PWkBpsTGtljN3OR1J6masKPPreVN56mEWmvWVsOa7L-8n4p1iq0mBbGHrOoRJIPQUQuIWpfPd1QsLQ3qA2BpSQEWaN5S2xOpxDtjBr1ItNrv3I47H_U2FfM1__d6PG2smvMZf-0JF9rlmwBjjDvhVgY7TFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
🇧🇷
دلداری‌دادن‌کریس رونالدو به رودریگو ستاره جوان رئال مادرید که به‌دلیل مصدومیت جام جهانی رو از دست داد: باید صبور باشی تا موفق شوی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/persiana_Soccer/24564" target="_blank">📅 22:19 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24563">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1f28bba8a.mp4?token=DchEIsKzvBJ7F-K3TlU4laAcR82PD9Az556gFnYhN3NpVcr1j9LDy6KFUGewn7XVuF3nHNAsXJTSjyrc4IbnnvdEUzTwc3UUKK1ZE9SAeQCqP3XLzkVnNbQZTlCnnQvM0LtE6zEcyhCxjvegFxTmfcXVs0dCr74KUBFuoG6v4harEQVz8Q6C4j-Dk-zlzr2Ck9T5E0UHRK_YSr2RqLtwF9E4qThc5AA0NtFOvHE_2uhna8tGSzKfUP_ikX60DeUshAH-4QXnPrQDm859EqpGQXgFANdHNeJVt0VEY_F1limtSznxiilD4goHP0aM4UlWKVz0pLksbv_dEntArXYR2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1f28bba8a.mp4?token=DchEIsKzvBJ7F-K3TlU4laAcR82PD9Az556gFnYhN3NpVcr1j9LDy6KFUGewn7XVuF3nHNAsXJTSjyrc4IbnnvdEUzTwc3UUKK1ZE9SAeQCqP3XLzkVnNbQZTlCnnQvM0LtE6zEcyhCxjvegFxTmfcXVs0dCr74KUBFuoG6v4harEQVz8Q6C4j-Dk-zlzr2Ck9T5E0UHRK_YSr2RqLtwF9E4qThc5AA0NtFOvHE_2uhna8tGSzKfUP_ikX60DeUshAH-4QXnPrQDm859EqpGQXgFANdHNeJVt0VEY_F1limtSznxiilD4goHP0aM4UlWKVz0pLksbv_dEntArXYR2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
کاشته دیدنی لئو مسی دربازی بامداد امروز مقابل اردن درهفته‌سوم‌جام‌جهانی‌از زوایه متفاوت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/persiana_Soccer/24563" target="_blank">📅 22:19 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24562">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T7ZopXmkbb23LkNoUlZHHH3Ii2CIFQKd0vO5wyZcEEnNGAtASVSQs4Zzl-aW8BEi-yPap6f1UU7BQSmBq7aCWetDzGiRq1rXuJSOMvcsRYdUIaj6ukqs-s8LyjtBA1Ba9kgP1hDEHJaKpwAYmd9bMyWjRTVFioPz1_g8qQgD4eF3NKvd-6fS_Aq_fE04BPZIlhcnaHtQixsIgkjWNaePedYkP7Uq2jbLONKQc3p0ACKTfmdbRXEN8o4jVjrY7d9OZ8ryOIRk9q-4lGpSiF4-LXQKcia-Xjnfp25aQ3dDi0PiiiNdG625C3LN3kgZPhwKh4AlKYptTpCevalmoWC9MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمودار کامل مرحله حذفی
🏆
⚽️
در بتگرام پیش بینی کن کدوم تیم قهرمان این رقابتها میشه
⚽️
🔝
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
🚀
پوشش کامل بازی را در بتگرام دنبال کنید.
👉
🌐
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/persiana_Soccer/24562" target="_blank">📅 22:19 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24561">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc1de478f0.mp4?token=ruaUNgxP6iVhOTut6flMGRVYDZAQu5hylq5WW53FhgE19-7zta-Fw_NXqT8lxDkJuUWilCskD9Z64raFQywiwqp7ctd3p3zpTpeI1yVYxkG0MDWXKfRZPcx3FW_YL6NqhTZUvazG21n0OtaSCAlymFhJXQU-GefrY1UO59cjaWpoyAOgnryRpkSBPhZ8inMvKIdllURMlUUt15B9wEMomZ-1hStz0AJF257C-UCBFjn2mBu7XLvI5ElOybSnhyPvE3v8UxINWoxHLkSZ1tsZN4aDehfypVL3H9hYpAXGREP_763U391Op44AT_K0bugTNSTJtoH0DI2Jap_qtjni-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc1de478f0.mp4?token=ruaUNgxP6iVhOTut6flMGRVYDZAQu5hylq5WW53FhgE19-7zta-Fw_NXqT8lxDkJuUWilCskD9Z64raFQywiwqp7ctd3p3zpTpeI1yVYxkG0MDWXKfRZPcx3FW_YL6NqhTZUvazG21n0OtaSCAlymFhJXQU-GefrY1UO59cjaWpoyAOgnryRpkSBPhZ8inMvKIdllURMlUUt15B9wEMomZ-1hStz0AJF257C-UCBFjn2mBu7XLvI5ElOybSnhyPvE3v8UxINWoxHLkSZ1tsZN4aDehfypVL3H9hYpAXGREP_763U391Op44AT_K0bugTNSTJtoH0DI2Jap_qtjni-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌ های تامل برانگیز آیسان اسلامی درباره باخت شاگردان امیرقلعه‌نویی از جام جهانی 2026
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/persiana_Soccer/24561" target="_blank">📅 22:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24560">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc38dbe3cb.mp4?token=hURGrJn4VcBOId_KibUtjCBnGSO84BiFGGexWzQ7ewXjli2y9x4z6idzx54I55uzmLtg5j-ZBXXCHVvubErNemnBQe22D5cDR7fJJJOTxatBedZXTXMv8P48qOdHLTJPIqxovIdVjWNigbLNKlKFByIVJhT-c4c-n-96gQPnt8TeC6KXko2u5-g8cBWaVvCRZ6cSabU2qAt-W3fJARGfsKrRcmEGH7tvDHahB8MwmtOF6dHRVUC5xAisR0feopYRmmFIMBzp-LTzOWYaPsDGwdJw7PIyRP1bG7-Vu2t68AE5a3REqQ1Ys2WLYNmFBCROkvwAvZuRjXRgkeH2LO7Vxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc38dbe3cb.mp4?token=hURGrJn4VcBOId_KibUtjCBnGSO84BiFGGexWzQ7ewXjli2y9x4z6idzx54I55uzmLtg5j-ZBXXCHVvubErNemnBQe22D5cDR7fJJJOTxatBedZXTXMv8P48qOdHLTJPIqxovIdVjWNigbLNKlKFByIVJhT-c4c-n-96gQPnt8TeC6KXko2u5-g8cBWaVvCRZ6cSabU2qAt-W3fJARGfsKrRcmEGH7tvDHahB8MwmtOF6dHRVUC5xAisR0feopYRmmFIMBzp-LTzOWYaPsDGwdJw7PIyRP1bG7-Vu2t68AE5a3REqQ1Ys2WLYNmFBCROkvwAvZuRjXRgkeH2LO7Vxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
یادی کنیم از این ناگفته های عادل فردوسی پور بعد از تعطیلی برنامه دوست داشتنی و محبوب نود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/persiana_Soccer/24560" target="_blank">📅 21:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24559">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ks5Le3iGMEKgPLBOQ4_hxC4JiUancAHWvRQV-Lzahhhmoci4hnSdXx8Je70nplSXdRrfZ1EZGVuD6rhG-FXK1T1veDY5NtiIz3ZzHjTs5Y_BcsiorF_oNMvUT_7l-jXcafHuf9nL39fBVyU9dSBFUACWpy0rkaoNaU7sEgaL3EkBXV5R--AlKZhpGJQxWhD2t7anVHa320JS0sPsciJ_LE2mfYmyS1xmvC6raizHvUR5wPAGGEGUPyauWGFLsndMOxv_goCE2F3nwSUvu9dv1rRW2MWQA3Pd49TBCDKBCd7Kf47aDC8gUTefFk0gayEfYTrJe6o_DjR9iCzWmDu7Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی؛ باشگاه اتحاد کلبا به ایجنت محمد مهدی محبی اعلام کرده که‌حاضراست با دریافت یک میلیون دلار رضایت‌نامه‌این‌بازیکن رو صادر کنه. مبلغ قبلی که باشگاه اعلام کرده بود 1.2 میلیون دلار بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/persiana_Soccer/24559" target="_blank">📅 21:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24558">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EiX51diyPx0-kj4WJmIBBSNDiJXaYR-hvvY8hxeUoqdnln6K-teHhDjVZ2na7NZqxrMJJseR2VP0p6u9i-X1EC6BFTh1nebW4nQR7rzUij8gmZXMYGDiOX6KDix1dPDhh2lrymRca2JiSgPoP5vQssTx7LAqS82pLgzlAudjSIgD04HaeFYIR0uZFlUgx3JQP3h3UJcnpdYHpAmpALAW-m4rV8SVxl0m7d7W3q9-YMGVd6kgkRoGHpItTfdUYxU2BKCGXJKh9AWaX-RzLEllufIWUQUARgWGxyy5M6hj6XcAJjPthAsC0dvuxB2q2oDNQQ35Xk1UH_NMlj0-LqnDWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
باشگاه سپاهان 72 ساعت به سید حسین حسینی دروازه‌بان 33 ساله‌فصل‌گذشته خود فرصت داده تاتصمیم نهایی‌اش‌رو برای موندن یا رفتن از این تیم بگیره. مدیریت سپاهان همچون بقیه بازیکنان از حسینی خواسته رقم قرارداش رو کاهش بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/24558" target="_blank">📅 21:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24557">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MTsEKx_omK7QRzdzED3yCnfGcmUzxjgXLTbO_huRrzOjLEpfc4W2IajkGuAP2p8zGtwdYacsLv0rhVn5gtyu31v3wv5TxbyTe6vqSDC1iGrYL_xNaPPquV2z8yQB2AH_t36w-qTVRrxbzc-wrv6FWVDj8skPkif2RRVYnnpIYkjQ059EM4OJA0wYNuHLehY4n_SestmwftXDPqi_3E-TE0UuOc4Sp5vhlVk-uV507_CDO-t5ULk1-s_wpGL_6gkIKZKrjJjZ5l66L-9zUXcJDJoYH1Zh45XX2NAbryspABtY00DhgWP_Opjz25CioruSuh4DRPPwosdV4P80j5221w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات|رابرت لواندوفسکی با ایجنتش راهی‌آمریکا شده تا با باشگاه شیکاگو فایر مذاکراتی انجام بده و درصورت توافق نهایی با این باشگاه قراردادی دو ساله به ارزش 6M€ امضا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/24557" target="_blank">📅 21:09 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24556">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_52zAoaptBA2uZisKsrNOWGUqakKxq8ArBM8561dKC8MXJwhhuZHH1F4gLpJikvdR7T1J3nUTFLB1QB-iSbMR-e5O1kD4ZRaW-Iq6hfZvd8wubuNlclVyPBaJbEXgVsiE-cwn9rJ04YMZmjRQkwpQ7t3NYBdm0iOX4Kbx13YbastcG3_EmmnjGpDn5IrV4zm8c53KdT4K7KvNSOQJhsiBDz5CAYtEb6gVVpLXC1UF8tDGUfcOmq9inRk5nDQikr1nBDgIKnIkOFBF8PiLNoK5fXkeiAp5hxnaBbRAa9G9bN2-X3pe7KME4jC_Hvapkdu_yh7GKJR2AiV8e_K-EuhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
🏆
#تکمیلی؛ سرمربی تیم‌ملی‌کره‌جنوبی بعد از حذف در مرحله‌گروهی‌جام‌جهانی ضمن عذرخواهی از مردم کشورش از سمت خود کناره‌گیری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/24556" target="_blank">📅 20:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24555">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c72aac9a71.mp4?token=FxkQuneNuJ4mMnsBLQK0h6PlemWEpGB3yG6Lg0XmopeUlCKntSVeH4VFShv3gjZ_m0FszspF8O1gV7DGOYHa16vkCCgyI_HAZwT9yTe2dppxRat-Q1tOePv39_S6FGwsrlyQMqqYcF8EUiH9LvJX8gWvkmXKxt4DdkinMsN9HJ1PEuULDgOLApHlCcnwNn8rtCNMqjjbxqXUb3zWxnOtPd83yrx53PHzeEuSk4xyZVQjYP2K_63F_WcuZHNGCBlvE4G5vdRiKWwmrgYme9zuy3fvqHUfZQnws70jQ6W6LJIAEb3JXzMT-CjSV8CXNg5VSyd_ZmTjzvFZGXYH_zmWYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c72aac9a71.mp4?token=FxkQuneNuJ4mMnsBLQK0h6PlemWEpGB3yG6Lg0XmopeUlCKntSVeH4VFShv3gjZ_m0FszspF8O1gV7DGOYHa16vkCCgyI_HAZwT9yTe2dppxRat-Q1tOePv39_S6FGwsrlyQMqqYcF8EUiH9LvJX8gWvkmXKxt4DdkinMsN9HJ1PEuULDgOLApHlCcnwNn8rtCNMqjjbxqXUb3zWxnOtPd83yrx53PHzeEuSk4xyZVQjYP2K_63F_WcuZHNGCBlvE4G5vdRiKWwmrgYme9zuy3fvqHUfZQnws70jQ6W6LJIAEb3JXzMT-CjSV8CXNg5VSyd_ZmTjzvFZGXYH_zmWYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی‌ازتاریخی‌ترین گزارشای صداوسیما از رقابت های جام جهانی که تا ابد ماندگار شد. ببینید حتما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/24555" target="_blank">📅 20:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24554">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df8b1e3bd0.mp4?token=pY74vQbMDLFrRkC_DrJUluhvkcvv8DuqQ_cKF0eI_YobYzbzKT2cMc4C-YZvKyY8VWYklVN-QosBCCTcle9lABdfkzNW2OkhRNujxKGlQfID0dr2BFLxA6EmPloyWytUwxaHCbGqRv5iPxqtK35xOeYkNapy6Xo3t0llmRMtT99A9zx6Uztme0mjZxcPAadn2zxEBMqxvDgoaoP9iGsY7_gSZJ0Nm5RHjS_ETGZpv28mC4GR7shGIAF6h6GpGooL8oUK5RCkl62jD6T6x9DkjB6dy5QZNvyxgUBGsfXkaEh-j-h3vl0VgMjBLkXI-5mecya_EDOsaupF7gTiMqA2rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df8b1e3bd0.mp4?token=pY74vQbMDLFrRkC_DrJUluhvkcvv8DuqQ_cKF0eI_YobYzbzKT2cMc4C-YZvKyY8VWYklVN-QosBCCTcle9lABdfkzNW2OkhRNujxKGlQfID0dr2BFLxA6EmPloyWytUwxaHCbGqRv5iPxqtK35xOeYkNapy6Xo3t0llmRMtT99A9zx6Uztme0mjZxcPAadn2zxEBMqxvDgoaoP9iGsY7_gSZJ0Nm5RHjS_ETGZpv28mC4GR7shGIAF6h6GpGooL8oUK5RCkl62jD6T6x9DkjB6dy5QZNvyxgUBGsfXkaEh-j-h3vl0VgMjBLkXI-5mecya_EDOsaupF7gTiMqA2rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
باپایان یافتن مرحله گروهی جام جهانی نگاهی بندازین به جدول برترین‌های آسیا در این رقابت‌ها؛ برخلاف عملکرد خیره کننده‌های نماینده های افریقا درآسیا تنها ژاپن و استرالیا راهی مرحله بعد شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/24554" target="_blank">📅 19:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24553">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kr3pfjmshehlFoNMm9ZeEzhq3j072TZwb4RzqyahGwimX6dz1DLrtOsmjM6bOC08NyoouIwaPqfn2lGd4og6qh2u_MyEt1ImBbA-9S2ooCaD8WYa9MFPwjU6ga2o3WCq8Ts0dt-gl9LzqWCFXV1STfnv8l9y9A2CKQb7i87g-Iinh0bJnlGcgoP2YDZs1UnlEs7HDUBo8j8i2_Zg6LKP7YgiArpeH12fsdmQPOfUwkxdfISfdX5EhrWr1YlFXwTmPZTlb0loIHIEsu_82HXJVOZMPiZk-CBKPLY3QAPydfkGu8qFjKErNNa1_KRjp8pA4bnEKKr6KMyYWWJgNy-iLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛ دراگان اسکوچیچ سرمربی فصل گذشته‌تراکتور؛ بادوماگوی دروژدک ستاره گلزن فصل قبل تراکتور صحبت های مفصلی داشته است و درصورتیکه فردا بعنوان سرمربی پرسپولیس انتخاب شود به مدیریت باشگاه خواهد گفت اقدامات لازم رو برای جذب این ستاره کروات 30 ساله انجام…</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/24553" target="_blank">📅 19:22 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24552">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a030de140d.mp4?token=sv-zVu1QxSdR7-Yy-FW0hXP05FJamXpZFaL_Wo3TevtT8LgN7N_GXU65_mj5nbLmYSMTKhWplbmX1ncU3W2MYpeVJnwCpWKNHgfYm3tCI_t7Gg0LJe_bkwfDQi2x2FTRRdcaTf0ArHyeqkutYxYxAmXTwgNtCq9ICzSCEp9UHRaFJdOHECxle5fBGOW6ZvsAR5sAvbp_jqh7fWwrJNmb4t0_oFdyNFi25l-Kb8c63xUwoSNMYPbiK4zWKtS5LyjMPNug25n36n1LJCHGWMACvgMVOFbNW551rfvMnKoG9zMA3RpSoa5ANMiL7fyFIBlMMt-vGXTu6lC-Jv3u0o22Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a030de140d.mp4?token=sv-zVu1QxSdR7-Yy-FW0hXP05FJamXpZFaL_Wo3TevtT8LgN7N_GXU65_mj5nbLmYSMTKhWplbmX1ncU3W2MYpeVJnwCpWKNHgfYm3tCI_t7Gg0LJe_bkwfDQi2x2FTRRdcaTf0ArHyeqkutYxYxAmXTwgNtCq9ICzSCEp9UHRaFJdOHECxle5fBGOW6ZvsAR5sAvbp_jqh7fWwrJNmb4t0_oFdyNFi25l-Kb8c63xUwoSNMYPbiK4zWKtS5LyjMPNug25n36n1LJCHGWMACvgMVOFbNW551rfvMnKoG9zMA3RpSoa5ANMiL7fyFIBlMMt-vGXTu6lC-Jv3u0o22Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
سرمربی تیم ملی مصر اعصابش از کارت زرد‌های مارسینیاک داور بازی این هفته با ایران بشدت عصبی شد و خواست‌که مشت بزنه دید آهنه گفت نمیصرفه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/24552" target="_blank">📅 19:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24551">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96448b3dc3.mp4?token=o0PDx1syGn5Lj_IFQH23Mc1bnOy4JjoeFDfRUmZ5dO5FHnnojGj8O-pbZ5DVOEe1BBcbIs5vamsCQtmEvUBwz5tGZbkEhdXUlNBIWagW4WBDWRMDqz50P7PnHuPwVCTaZ0ck1g7CK1jE4qLDwo9nZjJmx7wT0zbfnWERrqD81N7rCXXfpaeCiba9KN7duUGBvL5O-FCgSIrCP4-H3r6lNVa-3nZItkdPGeuDP92VXyveeCyBgTL-E8KmdcuHdEftKc_o4UNc8Ae3pJgU4PdKookfcPdY6M_lxDKHwL6GDAOd2Hq0h_4NmCA4AI-qO5OoyjXWFq0khIbUcK1GrnYCzDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96448b3dc3.mp4?token=o0PDx1syGn5Lj_IFQH23Mc1bnOy4JjoeFDfRUmZ5dO5FHnnojGj8O-pbZ5DVOEe1BBcbIs5vamsCQtmEvUBwz5tGZbkEhdXUlNBIWagW4WBDWRMDqz50P7PnHuPwVCTaZ0ck1g7CK1jE4qLDwo9nZjJmx7wT0zbfnWERrqD81N7rCXXfpaeCiba9KN7duUGBvL5O-FCgSIrCP4-H3r6lNVa-3nZItkdPGeuDP92VXyveeCyBgTL-E8KmdcuHdEftKc_o4UNc8Ae3pJgU4PdKookfcPdY6M_lxDKHwL6GDAOd2Hq0h_4NmCA4AI-qO5OoyjXWFq0khIbUcK1GrnYCzDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تیمای‌صعودکرده‌به‌مرحله‌یک‌شانزدهم نهایی جام جهانی به‌تفکیک هرکنفدراسیون؛ AFC با 2 تیم از 9 سهمیه عملکرد فاجعه باری را در این جام رقم زد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/24551" target="_blank">📅 18:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24550">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLOnSD2YSKkxkVP9Aglk66lhA4lYYbpPrH4OumNLCsLmEf96X-VYPz1uSo-jJii_j6OR62xDeDli3slJvSM6dDDt2XPOGmrmQuM4DeC4KSEdQ1KxOamUfUInNujuItLjlrKHxyDLTuMGUvZD_N4JxkNT7elSNow9tLhonWLgC-fuGmxG4FAxkx0Hd4Y7SKE_DRfwQfaCDcEsQo55PLNumnWdGsTqO0ljsJVOKXJUAaAzxhB9nZdyZBbIxPSFaBb9E4PG_ARtS8WclGvwDdf3-8BEpaPO5t-gYy5hyjX_IvY1Hoom7hGQl8TN8yJAVxYPHNimLvGCiL627Ac9EeqeHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه پرسپولیس 5 روز پیش پیش نویس قرارداد این باشگاه رو برای دراگان اسکوچیچ فرستاد و مربی‌کروات باامضای‌آن رسما سرمربی این باشگاه‌شد. حالایکی‌از مدیران بانک شهر از این اقدام پیمان حدادی دلخورشده که چرابدون هماهنگی با ما پیش نویس رسمی قرارداد باشگاه…</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/24550" target="_blank">📅 18:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24549">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcVxnK-RyYwR8yIeQtEJ2FAybIklz7xYHryT_NaGHBNYeqsapM6-mN9qhO3BaJArR0HG0qGo1sBqMfOkiHT8gitpWjRY0Lk22vvrT7m48huDcZ1VIymYX89XIhbUHA1-19O7o45P0iINO14h9Amxwma2AkHlxZEm3Vz6zoa7XxNsXbn45uU6W6k_LXUaGTufPT-tj-FB8NjkD9neGGIjGzdB9kmClVG7cZBASoXhDSQoRn1RHQjBCCL1IVsFfr0kzIdw4qdDcOMG-A2RNDi-gjd-kFdmM2SgqferJtdILLvE8zMq0cnaL2Fte1u63mm9q4KhhRMuH2v37r78TOpnJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیمای‌صعودکرده‌به‌مرحله‌یک‌شانزدهم نهایی جام جهانی به‌تفکیک هرکنفدراسیون؛ AFC با 2 تیم از 9 سهمیه عملکرد فاجعه باری را در این جام رقم زد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/24549" target="_blank">📅 18:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24548">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxCT4C-tqUYqJUbXkc43jBbwzEnmm_mPSm4ICE2lpCxh9we37FCqOrDwQuP5py8ZffzYBENu0ob7vdbJPduR52kL9nGh4qCCHSdGlFopCGQAX8twGD8folCQBOK7gAY-6yqqKV00vGDRvHzEJGOQM4STkkbDtlG5VFE1xoSnLgZ4jfiMmmjeY-raJ_elIOv6F5Ne_qgGEAKOeHrr0Oz-YKj-HquhdCQhVX2hrVY9fcbv-XKmLA66YKDmKpGoiCs78ij4LeoIp9H1Bc68mM9bU0r1m9qvSvjjPoxPD8kXTPUaUbOsv6amVvfo99SougyrjIM7hdWor1BeZaSp5aHSpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لیگ‌ملت‌های‌والیبال؛ پیروزی ارزشمند و شیرین تیم‌جوان و بی ادعای پیاتزا مقابل کوبایی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/24548" target="_blank">📅 18:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24547">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Qw4qp4dxEDFqU8Q5JOrcr1CiJOqzRIqTXSDljYLzf_bm_cppHyNSCa5VhaqLJehNL_Fnj4LZAgmCVWOH91EQ9C2kAsye0MFLco3nZcbZvs6IhjejmHjXsPcKYriGJpNqp1DdIhsYsP86tBUt3NE1fJnQQ7qrbAjtw1PzkYiIZufswSqawf4maKWKrbjom_qAcNKOgS6xLLls7apOUvuxfvrT41B79OawQlj8p7cFrxnPRBAOSTFXNkkbyn-YOElxvb7kwB4Y3xvSBP1n5ddJQwNtRGSXjoB5g6cuLP4fm3jPpxAfPFgY0ZyCON9tbRNGPPD1n-m0cwI7GF1-fbSApQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
بالنزبت هیجان بازیهای جام رو چندین برابر کن.
⛏️
بونوس
🛍
0️⃣
0️⃣
2️⃣
خوش آمد گویی
💯
بونوس
🔣
0️⃣
0️⃣
1️⃣
برای هر واریز
🔝
بونوس
🔤
0️⃣
0️⃣
1️⃣
کازینو
💰
کد هدیه
0️⃣
2️⃣
🔤
🔤
بعد از اولین واریز
📇
امتیاز وفاداری با انواع بونوسهای روزانه مخصوص کاربران فعال لنزبت
🍀
🔣
0️⃣
3️⃣
کش بک هفتگی
💵
پشتیبانی از تمامی ارزهای دیجیتال و کارت به کارت آنلاین برای شارژ و برداشت
🔤
🔤
🔤
🔤
🔤
🔤
🔤
📱
@lenzbet_official
📱
https://www.lenzbet8.online</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/24547" target="_blank">📅 18:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24546">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbcff344a4.mp4?token=BxWR46lD21PHPgkoLQpUZ1Z4x_5t8maSD-vETOxJ311QrkK4EHm6O9Gb5fEklmuJ092gUOXk7ZZfUajliTmm9n1b9KdcPerxsb4XK0_kCWgr1MrmJbHRoEjgMkB8hf7hCoMh0sL56CkBquOklpPH6qhaeqfVt8dsIvqaxJJvY7suq5MDHuSQ0nbDU0MSO-PajW9rt-oQbL9p4FTQVFYeKjdtgEFsOCaLMTNzZ6Tz5HazDTNXHEEfsUtjM7ALMlne9Tsyx8accyaWkwYodraxNKQUjGzJNMRzk1_6pHIPsivLlQs_U3IR8RAykg3t6pRfdJuuKSU0Dxof03Kf3NkeLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbcff344a4.mp4?token=BxWR46lD21PHPgkoLQpUZ1Z4x_5t8maSD-vETOxJ311QrkK4EHm6O9Gb5fEklmuJ092gUOXk7ZZfUajliTmm9n1b9KdcPerxsb4XK0_kCWgr1MrmJbHRoEjgMkB8hf7hCoMh0sL56CkBquOklpPH6qhaeqfVt8dsIvqaxJJvY7suq5MDHuSQ0nbDU0MSO-PajW9rt-oQbL9p4FTQVFYeKjdtgEFsOCaLMTNzZ6Tz5HazDTNXHEEfsUtjM7ALMlne9Tsyx8accyaWkwYodraxNKQUjGzJNMRzk1_6pHIPsivLlQs_U3IR8RAykg3t6pRfdJuuKSU0Dxof03Kf3NkeLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سه‌شاهکارتاریخی مهدی طارمی مهاجم 34 ساله تیم ایران در ادوار مختلف رقابت های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/24546" target="_blank">📅 18:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24545">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrhBmrU_nj-bOaY27GX5k5aUml_VCAjwadVgKrbBaU1k8xTeXDfpeR7MZnT1KIchijKo_UcBU0E2eZsATX_YnaJ7kLQ6fczYdroA4N-JMuYp1rwEvbhv2Sx3JvGOscIk33SfE4v60_3O5h7-yBbBLJv2uDBcg75GM-EYMx68netRAbq2pzZOmY95clh73xk4jytbpe4pOvkkSouLRxK3mZTljtEUm-5A3f-QFiYw3b5UxCm-yd0PMNrsuZ0EQj05T08kAvxlhPXLEPf0Dgn7fb0_XMwLzYpW_-IGyxL6f5AlmH8d9s1I81VBUWc7WRBEDItLWZ79ogUCBwdI4yKCIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
جادوگرغنایی: کریس‌رونالدو میتونه راجب من هر حرفی بزنه اما بازهم تاکید میکنم این تیم به دراماتیک‌ترین‌شکل‌ممکنه قهرمان جام جهانی میشه. کیپ ورو مقابل آرژانتین همه رو شوکه خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/24545" target="_blank">📅 18:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24544">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZPf56BPrf1-59603PpxyUyHKwS1TtYA25wh74iUvm2KUSqMN8yGxWe8kX9XHEktlt6qssdM1pQ0oaApPzPgG20LS3zgjjMVqMuwrOf4OFcUyQMKWvtgM6QHtaRA69co35Jjv4NHK0kJfns1Vwc3EhOU2_bB9GBuHMzilqFdflKLQ0UDdQG1CgAFr-9bbDaytNnGKXKKIpBFNLFteuFzEoCurpSzpIhwPq-Pfy_iWiMHbuIUofHLrqEJeMT-TZ7R0rlljtyo80QnVa7It1mZXxZgxK_ff0L_YTpwp5FQVMwKpoP4OQQE8R64zA7qYHY1AhZV6TY8FVIGlTsIlwhJog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇨🇴
صحبت‌های خامس رودریگز ستاره تیم ملی کلمبیا درپایان دیدار با پرتغال و تقابل با رونالدو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/24544" target="_blank">📅 17:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24543">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gH5So_z9XhhmndiOZDLh5eUr_lPiNHJuMoCYuiZwK3oRrzf9NlrHIkpiU-K24sWX114mq0WChpfX0NTAdr9J8-EquCjbMt3dwfFCp96GK-71xbjsNB4SR1Dy-n-d3-zzkPzNjSnaEOl-IcjBX5awku0mr7kciUIvwQDQRk2rN-chLGbQvfW4qaYE1STArHP3Ce8E_9V0q5xYHpxb1kmmH_9YOWRX12plSj_2jPCy6_cjLIf2xE_qWCMxRXwVK4S25O1inOWj08BzXcIp_6eXr57oXgju05WC3ZOarpDR8BTa6QuCzjLickxajmqgXa6Mh4pkl0t7xDTuVDKLnDUtTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مصدومیت دردناک و شدید خاویر کونسپسیون بازیکن تیم والیبال کوبا در جریان بازی با ایران؛ چه زجری داره میکشه بنده خدا. مچ پاش خُرد شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/24543" target="_blank">📅 17:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24542">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XB2sNYM9Xk2wCE9OD1MbVdH1Pl5pKN-OixDNzGtAI3EuI_HodWL50TeyHcR2rM0NzzJdP6TQkWXJo-JtgiFMaWqVmUHWK-sqGm8I-I6yqjZphpPRLQG4Jl1vaB7zdtIz8k-tlt-bNqQnj5Kn6ShsA-SxbBSI0XGeYEFpXQt00oPvEoGBa4d6CTp61IeRmW2HF7QBiextI37N5idZkEU71ZEJiq9lQulWr8kRARK8sfwChUevdUWGlEwEAN9ErW5uNJc_uDfTSTP97JIi-5dpQuT_xfUfOHjMe0y1XIy-hd0-p2z2aB-St2gcVuRujYPMg-ZcmNGpzDfihYrmPN59uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇴
🇨🇴
#اختصاصی_پرشیانا #فوری؛ یکی از مدیربرنامه‌های‌حرفه‌ای و کار درست فوتبال ایران که رابطه‌خوبی باستاره‌های‌بزرگ خارجی داره بار دیگر با خامس رودریگز ستاره34ساله‌کلمبیا و سابق تیم های رئال مادرید و بایرن مونیخ ارتباط بر قرار کرده تا او روبرای آوردن به لیگ‌برتر…</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/24542" target="_blank">📅 17:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24541">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A3vPiA2d4bCGT6_TpNATG6UDDRMXaCrkEKE24y7SiN6v7eJpZZFBsYPWp65ggXzbGzuZ61s8n-kXL_IaL-v00UQ9Qnf0chLvZxQ1tWMAFki-k8VOV_YD0edt398UoFDCCbCrZgCrbNSzaZhe7nqQkp3SWIaAlXMm1IJBxEFUx5XQqUWN1J_L8Uw-JpEQCCtKWudU_VF596CmvUL-Hml6CbckWjmPqYh_cGbVa8Tq_9C9FZitBuxhTwfC-weHSfOnKPeKwWL3jDYByclUEs_MYKb5F2K1XR06mthE4CAxv8xpHSnGi4hNQ8qinFU57Te9qIAfIaIH_R5clER3jg7pnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
ادعای جدید نانا کواکو بونسام جادوگر غنایی: من‌احساس‌میکنم که جام جهانی 2026 برای کریس رونالدو و پرتغاله و آن‌ها قهرمان خواهند شد. قهرمانی‌پرتعال دراماتیک و باورنکردنی خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/24541" target="_blank">📅 17:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24540">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rkv8Jr9mvQSqtIO6vUSZoltkdjsDpF6Zy-oli7vV4LCEyYEacAvK4AfoZ7L47ECOin3uQhOSxi6LMbMYo3WU2hO5KZNDAuJSBAYJePXYj-u-d3Bjw4p4AKHhzlzoRiFicX-GexdyordzIDawETCLOwDHwucgJIXcs9gV6XWh-NuhCkGb4kfxFasSulg8_reCsoHy_jP7YvKXtcAjiw83TkpKC8daNrplLLcf7FJbPBGHCToBo1sOfkcSSijTHGZsfxyS-xXJbt_BszvHmsFhxO5tefZwYdhM_-ul9puGCihHdRW-qpXYHMbPD7hh7z_DEkI7lfF86Gaizja1iIw-Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه‌ مرحله‌ یک‌ شانزدهم نهایی جام‌ جهانی؛ این پست رو سیو کنید و برای دوستانتون بفرستید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/24540" target="_blank">📅 16:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24539">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u0fNSXoWJkbYJpiNZbfbwx-hPUOQqUnVymbF5Ok4PBVFyh1DMrjx3ohyQJpHozCsdWhMbdo0U6ObusxvgqdB6qxX8hROO8vTn--U2X_rEXsxE3s5loU7zdov0kNXbLsMdqSs43pdLKldekH-3Akh433CD1b_L_Q-cD4p1LRbrLRtXT5CBSmRaZP1Ez1Loxe0uvwWgL0J0FYloRlGfxs0SUr6QbE2fDn7n9ZEQp9HiYE00sFxHM_Bn9XH4g8VRzD3uFukZdF1v1KW9JmPeBZbpilOVgodM-eWsMEQvz2ECT41kZGwX24M9TtM0fJ6ZOMLEggAa8F_J0abYBVKe1y96g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
سوپرگل دیدنی لیونل مسی در بازی بامداد امروز مقابل اردن؛ این ششمین گل لئو مسی 39 ساله در جام جهانی 2026 بود و 19 امین گل او در تاریخ رقابت های جام جهانی بود و با اختلاف در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/24539" target="_blank">📅 16:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24538">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gGs_sGU7811nQRntI8rbyg-BF1kb68u-o3Dr9TcXYkd-5rdLwTbOCLWIsOB9roG5E7FQSaPwd0G_8D9OUDCN9DDn5lDgUQZcL3TYg2_zUw0eymVK-AGzm-2AJXkUJlRs1-Mx6n14WWj0Cje6Ys1P2iJwfHEZwDtgEhY2-kGfmsP-mL7XYpb_mNKrnln7ySwEnCxPeDQzq1jJDtotIPps2CQbrUV6dJQxj5I2sQHLG0TSj7h4XChTVoiLTlnouunDwEMAT6DW4Lnd6HKZaaeg7GPBc856nFMWIJWdsjxRJJUHAYallMR4-LPAba9MjyhUwylWBr7ax2-hdIrGEcPufg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قفل کردن تیم قلعه نویی روی عدد سه؛ ایران توی این‌جام‌جهانی ۳ بازی انجام‌داد که با ۳ مساوی ۳ امتیاز گرفت،۳ گل‌زد، ۳ گل‌خورد، ۳ گل آفساید زد، ۳ تیرک‌زد، رتبه ۳‌ گروه‌شد، بازی‌هااز شبکه ۳ پخش شد و برای‌صعودباید منتظر ۳ بازی آینده بود و در نهایت باتساوی ۳ بر…</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/24538" target="_blank">📅 16:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24537">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc88812ea0.mp4?token=u9l6xjiNNQW5IcvOuhd1p03fFyppOz6aTYXcQl-Edzs6qdA-_kcysyqNAspsAtELDVlcGDNfBv8R1sA2OxJQdsyWqAycUPBmoHu_l1VaIK7A-tCy0jRhifZpRANv-_mAimMXGs3504U0-ELLXaauDCQVPYm21RAW4P2JH0lzYm3Enc2tW_C2q20m5HhDKudPOf2qMhgpAfqwt_K5ioVqLh4jSX_jcwa4tqCnSsv7-LuXhOrR1qUckyWIB3eNRpu7FaC3Y13JIfa5jPuBagqsm0qW7vNqH5SVXA6GVmH_WJYIHxJcDZXiFwQfHAuodJjxDlDTne-MCeg1QnDeo6eqrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc88812ea0.mp4?token=u9l6xjiNNQW5IcvOuhd1p03fFyppOz6aTYXcQl-Edzs6qdA-_kcysyqNAspsAtELDVlcGDNfBv8R1sA2OxJQdsyWqAycUPBmoHu_l1VaIK7A-tCy0jRhifZpRANv-_mAimMXGs3504U0-ELLXaauDCQVPYm21RAW4P2JH0lzYm3Enc2tW_C2q20m5HhDKudPOf2qMhgpAfqwt_K5ioVqLh4jSX_jcwa4tqCnSsv7-LuXhOrR1qUckyWIB3eNRpu7FaC3Y13JIfa5jPuBagqsm0qW7vNqH5SVXA6GVmH_WJYIHxJcDZXiFwQfHAuodJjxDlDTne-MCeg1QnDeo6eqrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌دوم‌ لیگ‌ملت‌های‌ والیبال؛ باز هم ثبت یک شکست نزدیک و میلیمتری برابر شاگردان پیاتزا این بارمقابل سامورائی‌ها در پایان پنج ست مسابقه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/24537" target="_blank">📅 16:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24536">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BmeOFFK9VHEi9_u_Drmw8czCotqHFjMjDy8jDeSU6SfnfNSrAYECd2GEgfsqdOCHKjhoEgA6fuRGfQLps2aC8Ds0pNUmT5QirWORzvyb8DCjKOrOkEnmwtzUuXd1DNBjXS_lh62qTrgI6OFlWnm3DYqj0UqjsOyppP6DdqgGplB38fAhyFBFqBDaXR72u3OfkYamYnXa99Ne3YzJ-Ea_S8nOzazFbk0g0SCpnmIEmrXMrrZEH6gfSFA8re8r79asEurQLvowQE1xR7Oyn9X8N9GDYfjtSMRNFayBXoNleFVD-qWtVEirkliCdI-nYO37oHCq-7uILlSmU7cr10Pjxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇴
🇨🇴
#اختصاصی_پرشیانا
#فوری
؛ یکی از مدیربرنامه‌های‌حرفه‌ای و کار درست فوتبال ایران که رابطه‌خوبی باستاره‌های‌بزرگ خارجی داره بار دیگر با خامس رودریگز ستاره34ساله‌کلمبیا و سابق تیم های رئال مادرید و بایرن مونیخ ارتباط بر قرار کرده تا او روبرای آوردن به لیگ‌برتر درفصل جدید متقاعد کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/24536" target="_blank">📅 16:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24535">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W-Xhyf4ABMdcqiX83_fVBFgMcGHRF4zWlmeVZnKUzP_45yWV9dCQcnghRXFrLHpO-taIQ-BTGM2Pvi-WnIguP5B1t81_mgWWNvzuLh5PCGKsjm1-TKFWzi305iBoxR1DryBGq2WWcCgv5OS7yfBBpCz7C7vr410FmpRs3R9IHs_vV06_lAy9RRSNZKBTLTHx4L-0Qf6za7X2o8lrq1pbW1uTiPTmtBMbP1-EU_YveMylypYNMJlfEeGgLBnjqkddv77NCmbP6ckJGHrSq5X6J8AvTiTW1IU07XCNpLZPFo524eFKUpiPP5w1_3GEsXifu3eW6jCcdlDuyJnMCsLlog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درباره اسکوچیچ پرسیدین؛ با پیگیری هایی که داشتیم پیوستن‌این‌مربی‌کروات‌به پرسپولیس منتفی نشده و اوسرمربی‌فصل آتی سرخپوشان خواهد بود. فقط بین مدیران بانک شهر یه اختلاف نظراتی بوده که تو کانال پرشیانا آنلاین بازش خواهیم کرد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/24535" target="_blank">📅 16:01 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24534">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mxu-9fyd2RIiWold2QW5gdk4rlV0t7BihzqycWodwiiDm-EG3iQZmWfUKvViYvpC-VbrztQD5VDL9JloqF8hzazBzADNYEwgeyP4L8qNKKrX4qIzMlzQiujZseCt22yCexEUwzT8IqhiwmUNqIBp5fipceuhDMaXGWmMaqS6st94LyWVeVWRDMjnz8VpFed-5x0W6r0JwGJp74Qe29dYl7dWQFrrHx45Q-qNJHfKrNAzKlhpSL2o30GiODUZ-cjPB_qXno-uH2BhrDekJJp_jXYkEbXMfXADi10yGYNeHxpCqdc-XUiZmdklQiwWgBbgk7mQTCkTR03Z4MAOXpm8tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
برخلاف‌شایعات‌مطرح‌شده؛ پیوستن دراگان اسکوچیچ به پرسپولیس منتفی نشده است اما یکی از مدیران بانک شهر گفته چرا باید این دو شروط اسکوچیچ رو بپذیریم. ولی چیزی منتفی نشده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/24534" target="_blank">📅 15:41 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24533">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🏆
ویدیو کامل گل های روز گذشته رقابت های جام جهانی در روزاخرمرحله‌گروهی این‌رقابت‌های جذاب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/24533" target="_blank">📅 15:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24531">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0xR64TYxR3yF-pFgI4r_Wa9sjPdx-r76UQ_MgUIdHxDrG9uNWtic1CtWUUIsdSVLJIqegXw4-rTtfgQTl2uIOlEsmI090iFNqI9LK5nhSkmUXOen44iuODGYR8XsO7aqh-zWe7_olUlFixYxWcrFimzcS2_QXnsGwXwkBVAq7qYiAhnV6TqxS7vJEkqpbEnHiZ7USVd7uY7eAq4u2yE7JRdoexZrfCHgbjdauGDVBI91M4J0fivP2UDIOXjIMd-Bd267hLR0gOp1gFQ3qx5r8caRYqw27ecvIPLk1YhPIP6QeEpzN0V1Bo0laFVLdwsMEr5xvgeuMQcWdbYazIRow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f11edc5879.mp4?token=WXk74c_PKlGIZw7cCuig1-Sdz7kCgiRhPorSldDmXrn261_dcTu-kXtcJv-psJJksNZEKV8K0s5UpVIcQEbEkz0EZtEzWjxvTQoMvzEJqCZEb22KCW5Df6DsdVHd4eBcHQOJvoaK5uoE94eHT3IMSmbU7wn5RuQBcpnqAKZofeUruO2ryleyf3kvmHVd5oTm9ndVeBJn1yikmzDFIKt4a8D05fe3JE9tjL6hpM9lS8P4eTIEaLWZT5CJNDd3d5VqhJNMqjkIRaRjq-2IHUC7g5bCcaH8M1zwjhvSWBnMetGTDXpOuUUsTlOdaJTko2mu9fDFK-OnmnVdEVzkq8sosA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f11edc5879.mp4?token=WXk74c_PKlGIZw7cCuig1-Sdz7kCgiRhPorSldDmXrn261_dcTu-kXtcJv-psJJksNZEKV8K0s5UpVIcQEbEkz0EZtEzWjxvTQoMvzEJqCZEb22KCW5Df6DsdVHd4eBcHQOJvoaK5uoE94eHT3IMSmbU7wn5RuQBcpnqAKZofeUruO2ryleyf3kvmHVd5oTm9ndVeBJn1yikmzDFIKt4a8D05fe3JE9tjL6hpM9lS8P4eTIEaLWZT5CJNDd3d5VqhJNMqjkIRaRjq-2IHUC7g5bCcaH8M1zwjhvSWBnMetGTDXpOuUUsTlOdaJTko2mu9fDFK-OnmnVdEVzkq8sosA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شایعاتی پخش شده که آقای هنکاپیه بازیکن تیم ملی اکوادور با سابرینا کارپنتر خواننده و بازیگر معروف آمریکایی وارد رابطه شده؛ سابرینا در بازی اکوادور مقابل المان هم حضور داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/24531" target="_blank">📅 15:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24530">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NWUMmcdQy4gbPFnoppVQ4Ql4XXZMb7hDBi2U_u2_Z9TJTuipybnErQIabFUzwCr2cQ8kTjf2UgYd63X2VNFfp5kZgt-3xvXHQOz9VqMEW7emBERC8kkTObEvwp99zS-t19JIpY-WMDB8-KImyG3cckplJbCq8TOzbssuLCYm9PH2tLcBYGI1h888u_xL09yC7RGRq0LuPJaFDpuuYTbZbKgVWveV0Tw5mthm0YOoTvYn-Ui3rgQtKPHQyhQ1tRonEkYiF2ae-Xm7Uz8Zj8Cm4yopaop6UmwU-vZ-JVTUkqkAu2rWWiOVRXmrv_6WoJouegXzneU5YwyRAsp-q94Jxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قفل کردن تیم قلعه نویی روی عدد سه؛ ایران توی این‌جام‌جهانی ۳ بازی انجام‌داد که با ۳ مساوی ۳ امتیاز گرفت،۳ گل‌زد، ۳ گل‌خورد، ۳ گل آفساید زد، ۳ تیرک‌زد، رتبه ۳‌ گروه‌شد، بازی‌هااز شبکه ۳ پخش شد و برای‌صعودباید منتظر ۳ بازی آینده بود و در نهایت باتساوی ۳ بر…</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24530" target="_blank">📅 14:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24529">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sGGsvdKjUPUXisZok6-EkGWh78iGfYDkLpL6aLXs--emFswVnTL9TpVMi_vqzvK7nuea2mfVBMKukK2K8360jGk9ldUPn0fBDVsRBQRjeG1yZJvOizqsF1K-w-vRuyMO_mQb4jcCQ-F5emqh0ltJK08oVtUZ4ICsdZ986LmaCqz-OsnpLklc4Z_aFcOyRy7_EFT-zrq5V71pHeMT3N5LoNqm9o7nbpxyaBgq9jhK29S7oDqtRA4W5oUSeTqvs_k8jWvwwipfIem1i0WLKjN0p-hKxHX50HEcMbLIuSiD8uyBI28ajSIoQ3QG3UoKsHd2ywtsec9DS8-XXFEjD3rvvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار کامل مرحله‌حذفی جام جهانی؛ الجزایر و اتریش در دیدار تماشایی سه بر سه مساوی کردند و همین مساوی باعث شد که تیم ایران حذف شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24529" target="_blank">📅 13:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24528">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aabc5e40eb.mp4?token=oCLNqUquDNa8RogtSEcu6JywF0-UpfT3IFmTygq7T5GR4dG-9EgBDz-Wo8Q_PAsr9Qs2W7_5UjByr2piD0XNgLqpHRlu8VBAUwIbYPuv0qMc2iz46Gu2AhFlb96hM8Fsah9QA0Em0hrrQ3YQL6ps2zeUEejslJtJgn-_fZZjED5BH84_mt8ULbWhdGJg46IIYQfEKsd3L3yWhdvv2SIjuM46MBl8J0g-EX0BL6E2B2WdG2JNnl6yvVydaliXUvsllLTKpWpkVnxPpWEZIQQiJZt96nkUR7f6V69CZWE5vfxoVrDZAAtOxekrXuZHMYt4gprBa8-U6Mb7UYU5TmihuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aabc5e40eb.mp4?token=oCLNqUquDNa8RogtSEcu6JywF0-UpfT3IFmTygq7T5GR4dG-9EgBDz-Wo8Q_PAsr9Qs2W7_5UjByr2piD0XNgLqpHRlu8VBAUwIbYPuv0qMc2iz46Gu2AhFlb96hM8Fsah9QA0Em0hrrQ3YQL6ps2zeUEejslJtJgn-_fZZjED5BH84_mt8ULbWhdGJg46IIYQfEKsd3L3yWhdvv2SIjuM46MBl8J0g-EX0BL6E2B2WdG2JNnl6yvVydaliXUvsllLTKpWpkVnxPpWEZIQQiJZt96nkUR7f6V69CZWE5vfxoVrDZAAtOxekrXuZHMYt4gprBa8-U6Mb7UYU5TmihuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
جدول گروه K و L در پایان مرحله گروهی؛ کرواسی غنا رو برد. انگلیس با درخشش بلینگهام و کین پاناما رو برد. پرتغال مقابل کلمبیا متوقف شد. طلسم کین بالاخره شکسته شد و گل زد.
‼️
باصدرنشین‌نشدن‌پرتغال و صعود بعنوان تیم دوم، تقابل آرژانتین و پرتغال تو یک چهارم نهایی…</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24528" target="_blank">📅 13:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24527">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9a62c2d12.mp4?token=PEZrWQuoFBEL-lbskEedW0_XNRcvzFlQETbkk5XhYTeWdfjIyHrqTM0Q0SHmwYX1HykWrgoA225CTayl6LeWzhcvn5KxEpaQot-nrOOekM2rSs9GHRJzWNNc-WQSwgUF7_5NVXR8d_0UsRJPlztIU1ux30hji4lvMvgwM-fdmiP_J0cfKs8pn4CIx0ItAhWegRJDRB1GbiFmc0NxtMK9EFCmi90iLAkMO50UabTnKmvbPOkMipLCJKmjVVp2L6NYiiUNjiNrRTwA4NDfzqTeDhnfcMj63XGO2_d9XeBN4-CGjm60RlRsjID0CcC2daGVfBlXqPrnVRKbOpBhBXLKxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9a62c2d12.mp4?token=PEZrWQuoFBEL-lbskEedW0_XNRcvzFlQETbkk5XhYTeWdfjIyHrqTM0Q0SHmwYX1HykWrgoA225CTayl6LeWzhcvn5KxEpaQot-nrOOekM2rSs9GHRJzWNNc-WQSwgUF7_5NVXR8d_0UsRJPlztIU1ux30hji4lvMvgwM-fdmiP_J0cfKs8pn4CIx0ItAhWegRJDRB1GbiFmc0NxtMK9EFCmi90iLAkMO50UabTnKmvbPOkMipLCJKmjVVp2L6NYiiUNjiNrRTwA4NDfzqTeDhnfcMj63XGO2_d9XeBN4-CGjm60RlRsjID0CcC2daGVfBlXqPrnVRKbOpBhBXLKxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قفل کردن تیم قلعه نویی روی عدد سه؛
ایران توی این‌جام‌جهانی ۳ بازی انجام‌داد که با ۳ مساوی ۳ امتیاز گرفت،۳ گل‌زد، ۳ گل‌خورد، ۳ گل آفساید زد، ۳ تیرک‌زد، رتبه ۳‌ گروه‌شد، بازی‌هااز شبکه ۳ پخش شد و برای‌صعودباید منتظر ۳ بازی آینده بود و در نهایت باتساوی ۳ بر ۳ الجزایر و اتریش حذف شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24527" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24525">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FQJD-XNYoCD_oJEgupJkYKT5fCRWR_u3-gbc2XB6ZnaaU96gLyxLJ7wAY_MlAkLyi9JY-lpE7muqsV7HajZDMdIAJ1whXThov5YxhpEgUw9blQ5SsTwTe4X_VpNDqDrwIVIW04bawNgcu1MyerrwxMI7LnyVJxbTDvZelr03jYJJU-AUb9uOv4FJxF4zzyS6LURy54VJt_fy8vtyl_MLrTCEvJKntCBsBSDWC0w47tygB4Va2wmnNsE_UDHQ6QRSOZDoK2AWNsJriNWQNxMWoaEueJ-gw0_pt9wXojYIji7aj9qzYFGqz5kbKEBvq9IJ0elrJEmtWaL72gPfncIqEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏که‌مردم‌ایران نفهمن و بی عقل آره؟ خدا هم یجور گذاشت تو کاست که ده سال ترند سوژه های جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/24525" target="_blank">📅 12:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24524">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29e51a32c9.mp4?token=DO72w7Nu1OzOumODPyy9ZqOYRfAUig0B2C3X3OofzD9nq5KuYtVK_M-ZxVAM7-Em5-tU-ktwJAbnGaRj7OqZoPEohsft7LOlo0Nqk5yRpRhBjaxjc9rp3Yea6BfI6Zdwd8AeDFeOEXR7AB76NO2sXRheVn1Vhf1oRCHobuurPkz2bf1rD-XWNWP2sD7m-0Mm3p5iuBv3hxvLYDq_O-JX407Xp4ZRsmz-RzG223JyawMQ7yUZHuN_VBYaajxuWGHlijFWBPGOA_noEMk_6fOnMyC52z_QbkEcE1_fhzbWVUgZlVWpipFzYg2ABFLRHvw0LnVm8X9WUH8zBPlhNzm9VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29e51a32c9.mp4?token=DO72w7Nu1OzOumODPyy9ZqOYRfAUig0B2C3X3OofzD9nq5KuYtVK_M-ZxVAM7-Em5-tU-ktwJAbnGaRj7OqZoPEohsft7LOlo0Nqk5yRpRhBjaxjc9rp3Yea6BfI6Zdwd8AeDFeOEXR7AB76NO2sXRheVn1Vhf1oRCHobuurPkz2bf1rD-XWNWP2sD7m-0Mm3p5iuBv3hxvLYDq_O-JX407Xp4ZRsmz-RzG223JyawMQ7yUZHuN_VBYaajxuWGHlijFWBPGOA_noEMk_6fOnMyC52z_QbkEcE1_fhzbWVUgZlVWpipFzYg2ABFLRHvw0LnVm8X9WUH8zBPlhNzm9VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
وضعیت نهایی گروه های دوازده گانه جام جهانی بعد از اتمام دور گروهی+ جدول تیم‌های برتر سوم جام جهانی 2026 در پایان بازی های مرحله گروهی این‌مسابقات‌فوق‌العاده جذاب
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24524" target="_blank">📅 12:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24523">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pOU4izRwtttGoVd7ZzI-ffRUkapOZMsM2q0T1Y22S4UEEfJ6T3biZ98NksBKgTD60AIZnPgP927EoukPDdaHKcnMmEk6Pfw0dtnli7dwz9SeJe53WK2l2Tr22m9bzuDhPjN1rinnW0Wj5ANPqSGHbotFJHxRD-aiEunTXRERrUjIpPsXoKNEdduMnayjZrkqxPUQdud96K8RITKvxZuNzKyRDmTbX_7pwtf5nBeSRS9bnipAXFsSVnHo1CPQusjFdep-cnMkGDA8CRDt8sHjyOoj9EnNaIZM79AsHLembFAA7w80s0FC8sy1CKGzHh75u-0CHxgR-cvv7QFFF-Mllw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛طبق‌اخباردریافتی‌پرشیانا؛علیرضا بیرانوند به‌مدیران‌دوباشگاه تراکتور و استقلال اعلام کرده دو هفته‌به‌او فرصت بدهند تاتصمیم نهایی خود را برای فصل بعد بگیرد. بیرو هم از تراکتور پیشنهاد تمدید گرفته هم از استقلال پیشنهاد سه ساله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/24523" target="_blank">📅 12:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24522">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vM2ZqFR01UW193olFqzzc50aD2AV8BlaQ0v7HWo4JaB8ye67CyfEWlgbgKmmCxvVrLzTYI99UeIssUoTG2_ewbcVtbDPaVmsUAu8Z-xbIOUHfiJ92j_3Oqo0IHlR7ihBlkDdBZJPc-S5NRs4_vUDKdUTFFZTxow7bClgJE1Uv4ykHoDXgWH9eS8FM9_AqgW_xiO1O9GR1dYCDuzAH8Z_vTvn0JqgltZuoFxP3O2XjNKV9_sZj5j7JVVMxFWh_NuzEBWC9SClka4Ca2_MeSytfEGYR5P9R6tmnt-s-U9H7tcUal7jynIaK_CeU3jSQyypSROhBscL27PTEC0NLpFQBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
خود درگیری‌مدافع‌مسن تیم‌ملی بعدِ بازی با کیپ ورد؛ خلیل‌زاده بعد از اون صحبت‌های گوهربارش در تمرین تیم ملی خطاب به پزشکیان حالا بعد از برد دیشب انواع اقسام توهین‌هارو به مردم کرده.
‼️
حالا این‌کیپ‌وردبود که بزور بردین. فکر کنم اگه تو جام جهانی یه برد بیارن…</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24522" target="_blank">📅 11:42 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24521">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jXYCNIFGcpNRv6ZN7pvY4VD0vWIM6tMu3tEa_8-RcCqV2jGDIQ2g4Q-qJqlbZg8LNjYVh89Gxqr-UN9M7zKLjo4B7fgNk6Vk40jnlmOnXBcvgtbhmguAhPAAFqmrTUy9-kFsvLj3LkLbTkDQuDh81_jZQHV_qH1tR80j6oEv0JdW-Yythh19GIG0lIKwnMNo-jAuR-QQjRpk3KELsXYdZkVv-xb6pLDnenl0QmmSmxDFuoTuugUd3ZLAVEXCIi45xccrQlU3m5YJeckJTx7nbxgX5_aoIMQDEppM712pMwC8lW6aBR0rZqbHSxUMl94JqiDcmFpqIS-tLW5ISRy37w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#فوری #اختصاصی_پرشیانا؛قول بزرگ وکیل علیرضا بیرانوند به تاجرنیا رئیس هیات مدیره باشگاه استقلال: پنجره باشگاه‌ تون باز شود بیرو بعد از جام‌جهانی با تیم استقلال سه ساله خواهد بست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24521" target="_blank">📅 11:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24520">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‼️
خوشحالی بازیکنان تیم ایران ازگل دقیقه 90+3 الجزایز به اتریش قبل از گل مساوی اتریشی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24520" target="_blank">📅 11:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24519">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EdRe54BJIw1XVvCzDk3pUvyF0v5YWsVxQCLHSox7-IJ5Ji3muWi6cBRJXQIYlUYE_Y_aFzHb5p7mP0G7GUR5xh9DGNqzx2bCSRby9JEtBiDyViIlatLQhpBRLmEie0pCQrIGCca8lZ2QS-sguBJYGpIzMkkNEQ9Do1fDH5xmXgs9DXzDv2gnfjog-173uREAizy7ezxw3N2Jq2oue6t-LRWQvH_JZMW7rJ2-1ghkY_RL58hXNg83Oxksp3YUISkz6jGn0DaWpyYw89Sk2O8adZrJd8cGz73nd9ON0gp7xgl79tETo2H9cxXQdJwn_tISTfI6F_KSgTfAm9VfUisHng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
‏3 قهرمانی‌پیاپی‌جام ملت‌های آسیا؛ ‏صعود بعنوان تنها نماینده‌آسیا و اقیانوسیه به‌جمع 16 تیم برتر جام جهانی؛ ‏صعود به‌جمع‌هشت تیم المپیک؛ ‏صعود به سه المپیک پیاپی؛ ‏بهترین نسل تاریخ فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24519" target="_blank">📅 11:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24518">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/317abd2bf5.mp4?token=FtPHhG1KHTTG8LV2m4jJzJ6cKqBrj_8jbhUAJ_f4d2J0u9cXey55K-6pUVFBFiu8TGqUX4vfcsQU1XrVbE2TOBweOAm5GHTPFNaxVOIVwddMh47uUteSFY7ZNVA_Bf1MRZFBj8KjoQWxX3zZzMQoFf9QK5gTcRN6MV_acI9TmBCHJH3NwB-IbLKrGblUg-NrSeh29huj1hzeSj4pZocTqq3fQ_MRyZjpA_uU97j1b90gDqfLtKYtmikj_Szy8W4UAUKDsYEuNG_VJV_0Ts2pROR0sDI-ttWFmnrx5VgvY9-qpSMn1ft-Hbuehcl5UC6jogOdTrW6lNFxN3yydtH3vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/317abd2bf5.mp4?token=FtPHhG1KHTTG8LV2m4jJzJ6cKqBrj_8jbhUAJ_f4d2J0u9cXey55K-6pUVFBFiu8TGqUX4vfcsQU1XrVbE2TOBweOAm5GHTPFNaxVOIVwddMh47uUteSFY7ZNVA_Bf1MRZFBj8KjoQWxX3zZzMQoFf9QK5gTcRN6MV_acI9TmBCHJH3NwB-IbLKrGblUg-NrSeh29huj1hzeSj4pZocTqq3fQ_MRyZjpA_uU97j1b90gDqfLtKYtmikj_Szy8W4UAUKDsYEuNG_VJV_0Ts2pROR0sDI-ttWFmnrx5VgvY9-qpSMn1ft-Hbuehcl5UC6jogOdTrW6lNFxN3yydtH3vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بهترین‌میم‌از بازی و تساوی پرگل تیم‌های الجزایر - اتریش که توسط پیج‌های خارجی ساخته شده:)
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24518" target="_blank">📅 11:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24517">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">چرااین‌روزهاسایت
MelBet
رو انتخاب میکنن
⁉️
🎁
شارژ هدیه 130 دلاری اولین واریز
🎁
شارژ هدیه 100 دلاری در روز های یکشنبه و چهارشنبه
🎁
و ده ها بانس ارزنده دیگر...
🥇
متنوع ترین آپشن های ورزشی
🖥
پخش زنده مسابقات
🎮
بیش از 80 نوع ورزش مجازی با پخش زنده
⭐
کاملترین کازینو آنلاین
🛡
امنیت فوق العاده بالات
🌐
اسپانسر رسمی جام جهانی
💵
واریز آنی جوایز با بیش از 30 روش شارژ و برداشت،
از جمله کارت بکارت
🎁
کد هدیه 100 دلاری: Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24517" target="_blank">📅 11:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24516">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24998fe60d.mp4?token=lqiNi7GSUO2MD7jGHv1rZmCnYK82Fh5nr8TYzAnlanQAVyh67-36-79pCrcebJQl_9QFdTy6mTsvuZet6Bl3PuauQZ8J4BT3i5g0gOd9a-NwXHMi4cKh9gKOKp2Rx4rc3B5FJrPOZU6E2MklZgzUaKQaIvEiCZWbqIIZwYQw5h9mokvonesTGkryLpDAuhL3jV5PrO1f0fKxVoCSQgtQd_mSKXp-_G2UiOY5MSCnvyGaaK4OP_vdMTKARldibL7EQExejNkeDq3J8cYKQQzgsnaFcrtJCRq7b11pLcY3xfkZlP3Fe_NBz63SOvQllZp7mISzM_MiUvI8JO9KtV_odw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24998fe60d.mp4?token=lqiNi7GSUO2MD7jGHv1rZmCnYK82Fh5nr8TYzAnlanQAVyh67-36-79pCrcebJQl_9QFdTy6mTsvuZet6Bl3PuauQZ8J4BT3i5g0gOd9a-NwXHMi4cKh9gKOKp2Rx4rc3B5FJrPOZU6E2MklZgzUaKQaIvEiCZWbqIIZwYQw5h9mokvonesTGkryLpDAuhL3jV5PrO1f0fKxVoCSQgtQd_mSKXp-_G2UiOY5MSCnvyGaaK4OP_vdMTKARldibL7EQExejNkeDq3J8cYKQQzgsnaFcrtJCRq7b11pLcY3xfkZlP3Fe_NBz63SOvQllZp7mISzM_MiUvI8JO9KtV_odw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های ژنرال به زودی بعد برگشتن به ایران راجب بازی‌هاشون و حذف زودهنگام از جام‌جهانی:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24516" target="_blank">📅 10:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24515">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4da3d833bf.mp4?token=UVC1Tq1yErtd2KWie-Uag36yXNDdrxIretO-ZcnwrAqNGKwgmkgp25y1rBuUrc0GAlgAnEFMiHHskc-_iBTsVgEtnrKYViVin9G1RM_3S79mZUIRx2ED8zyP9buI74ez_kYELtdg4xOgIWRayDF4dBl4xBgIoC-R779vY4v4QDxQucII4opuBGpEhBWNTQS7dhZqKlxKVrblskHz323uDgFWlz7TU12_qA7aUWQQuAMtcHZmCbVWFtmkmTLr09g5di8iCl-8gEBkImSQhTr0Q2M_gAuGTtA6CcNffo-tAOxygd-5VRfEpw0GuxHE7ZztJ-C2nZsxYUnHFwpo0x9tew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4da3d833bf.mp4?token=UVC1Tq1yErtd2KWie-Uag36yXNDdrxIretO-ZcnwrAqNGKwgmkgp25y1rBuUrc0GAlgAnEFMiHHskc-_iBTsVgEtnrKYViVin9G1RM_3S79mZUIRx2ED8zyP9buI74ez_kYELtdg4xOgIWRayDF4dBl4xBgIoC-R779vY4v4QDxQucII4opuBGpEhBWNTQS7dhZqKlxKVrblskHz323uDgFWlz7TU12_qA7aUWQQuAMtcHZmCbVWFtmkmTLr09g5di8iCl-8gEBkImSQhTr0Q2M_gAuGTtA6CcNffo-tAOxygd-5VRfEpw0GuxHE7ZztJ-C2nZsxYUnHFwpo0x9tew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
باحذف‌قطعی‌ایران از جام جهانی و بازگشت آن‌ها ظرف 24 ساعت آینده به کشور منتظر اخبار جذاب لحظه‌ای پرشیانا درباره نقل و انتقالات باشید.
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/24515" target="_blank">📅 10:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24514">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/947e6ca793.mp4?token=anzz0DLdh1kFXN8lfihdjwmoS5RUYFShnQXhe8aAceZrLTLrPBGCvCb4Td00TboOr93TR5MQvuMqqxxQ3m15g7S8nZw2AkjxuPjgIE5W9yJhicTGQlsYCmID5kV135w5UnBPpw7qZxNY3xr6AAH0codaFedb1Iqo3jwziddefVmDcns-WrMlkCSuP7oBYsRG9760xxJFX47iYjfeh7ntQicHp0Bslo37R2Z0pVcZPKJckbrtl8L7eNMgX3tIM8SFigJ_GnsTByDAfSrUMlk1w5McF6DGh10Y9aAHeeLzm1urikR1ZzOGmmAo9jbgxA_4z6eWQK-Fh-nTQoIrcYoIiGAr6pu0C7hEzbK8Ca8nbpSrgcMhhFbbofvyOvIKTqlwEGMNmjUmAizUHk9iKd23WXJj_dVheRBRE6u5dA0QEA5XcGjL5UzbxW6evtrYYXzuugjOu1KxCC0npCKq-KSV-vQl5d-DeTKIbeLiyqd96aqEgWEeuxTRdBN2P_eQ8Pn4QaU1RInkQCXKfNYFPGd0EVHLRyIG-eWVyCo4e2uIV0WvWJb77XZuiz56T1i7tiqM94tU5WdIjzxqDMGRTyHvZpxt_wmswggzfJBfN07BXby7_4N4Xh4VWGHi5kWaUH25hb7-NDFpUO9HG7K_xXdi346ntoA0hNizEL_iY7eZQ60" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/947e6ca793.mp4?token=anzz0DLdh1kFXN8lfihdjwmoS5RUYFShnQXhe8aAceZrLTLrPBGCvCb4Td00TboOr93TR5MQvuMqqxxQ3m15g7S8nZw2AkjxuPjgIE5W9yJhicTGQlsYCmID5kV135w5UnBPpw7qZxNY3xr6AAH0codaFedb1Iqo3jwziddefVmDcns-WrMlkCSuP7oBYsRG9760xxJFX47iYjfeh7ntQicHp0Bslo37R2Z0pVcZPKJckbrtl8L7eNMgX3tIM8SFigJ_GnsTByDAfSrUMlk1w5McF6DGh10Y9aAHeeLzm1urikR1ZzOGmmAo9jbgxA_4z6eWQK-Fh-nTQoIrcYoIiGAr6pu0C7hEzbK8Ca8nbpSrgcMhhFbbofvyOvIKTqlwEGMNmjUmAizUHk9iKd23WXJj_dVheRBRE6u5dA0QEA5XcGjL5UzbxW6evtrYYXzuugjOu1KxCC0npCKq-KSV-vQl5d-DeTKIbeLiyqd96aqEgWEeuxTRdBN2P_eQ8Pn4QaU1RInkQCXKfNYFPGd0EVHLRyIG-eWVyCo4e2uIV0WvWJb77XZuiz56T1i7tiqM94tU5WdIjzxqDMGRTyHvZpxt_wmswggzfJBfN07BXby7_4N4Xh4VWGHi5kWaUH25hb7-NDFpUO9HG7K_xXdi346ntoA0hNizEL_iY7eZQ60" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این‌ مجری بی‌ریخت و مفت‌خور صداوسیما که بیس چارساعته خدا گوه‌خوری میکرد اینجوری روی آنتن‌زنده‌شبکه‌دو صداوسیما ضایع شد. می‌ثاقی هم که کلا فشاری شده بود گفته بود دو تیم بت زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24514" target="_blank">📅 10:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24512">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fpf1zkL-fA3vKscrtyXDVIPKWdIMMgkAYvWFrkCtBMUcW6qUoVvAXfzO-ZT_NuuXDnioOGRJJI-3Nk0L2afPoMuqMEvUGcWeysY5sKqYXiEowUYNCi9Dz01tKXLabFaZIle4qxoBm6wjxQuILfH2ibFEhF5g9koaAIOop52iBUoir_wFNWwQ0EsDSjDKzNYP9SHDG_60zmJMFZfgbaYmiIu6fpUW6_Mjm5P5wACrB2aVduyIyFj0gsuy9yeIMoxpRBLHhGzHSQo7vOG-0i95OcuRi9WrrxG7Y3EabEn-B1aPR_3De2i5RORoulxhiFEruDWwh1ZjpUTexprA1OvVCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقه 92 وقت‌الجزایر گل‌برتری زد؛ گزارشگر: 7 تیر رویادتون‌باشه؛ یه‌تیم مسلمون باعث صعود یه تیم مسلمون دیگه شد. دو دقیقه بعدش اتریش گل زد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24512" target="_blank">📅 09:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24511">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QE50qnfkX3639Agk8yCnjbcl9fIIGTQMscHwBRw0ZyVH9axII5cVekWlvAX10r1xBl8zdMxiPF7t2J_RSrVAtXPVYAFTjkl6ddQPZpJQ_rlqc6OxNJeFRbQV1TY_FYI0DLB6PC0dSVdfb6BNeEv9adkk28ZHdyl53bDsrI8gnDbvUepZyQ713eHFeSVRsbvJQtgzWpz1zzwl6iXUifSrN0qvll68zL7xY2s3ssbjNa0OGmAU5v0F5fqxhLQfDlI8Ms4LUJRsFd6HEo7-GDWbbxUSFILZFlo4dBCbNgIDTjA6PA3bvIG8sjlnjp8udebhh8QVEpRNUPb_5c_OcQA70Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه‌ مرحله‌ یک‌ شانزدهم نهایی جام‌ جهانی؛
این پست رو سیو کنید و برای دوستانتون بفرستید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24511" target="_blank">📅 09:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24509">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eoIpbkLzSy2DSR94m5mNZdB1IVfBscqrut-KIz0_krRcSB59BegJ4f9UaKLQc13F0lLcxvSjNjtBiRqYhZrO0R65xvfDATQeWq4SuFHlqYfxJhyca5uK-zbsDJhqCH2PSdIGYKhpb-3GpUQU37yXzkphPIFnClhNoaYf5jiuDmgp3ZbB8fEQU2geb44CKAN_nbHALruZl36PpeyTe8ODsj84PBVqvTqRiPHaVFNwqm1D217egHPZm81bRNInXj_xoPKXXauLivSOS7C6JafFP-zGDYdT6JJfo-n79l8cgcG-judtERFO5ne5ykgdWDCOutIr399oMV7bl31hRIDQxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YS9ElVH43GF0dItH1sLvsFYixcNu1SDJD0AD95K9fx-KWnTPM4gPib5fbUFntCqRYM7i9fHORalOEM5XPwODeW5FgPR73_lNLTXsI9xDati8XoHSTft64e7ZBkn41FAUEHhFpdfmTmlDImfUyM3oCFK-z8caekFH30NWlYqKNOaO6kj75C4vpXa22ZjwVCwnveg2TAY-LUOgrMkpzAxKJflREHYXSsTM1M5dxmfypLDd1YVwnqW8nE6NOvK3tcl_bFVQjGZOVzgmoXJNbcBwld8g2igkDFmVdPwWYjgDWBpeRV6dVyuBPusI8kCkeLOG-JVxWc-1olkMNknIAJOuNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نمودار کامل مرحله‌حذفی جام جهانی؛ الجزایر و اتریش در دیدار تماشایی سه بر سه مساوی کردند و همین مساوی باعث شد که تیم ایران حذف شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/24509" target="_blank">📅 09:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24508">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‼️
دقیقه 92 وقت‌الجزایر گل‌برتری زد؛
گزارشگر: 7 تیر رویادتون‌باشه؛ یه‌تیم مسلمون باعث صعود یه تیم مسلمون دیگه شد. دو دقیقه بعدش اتریش گل زد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24508" target="_blank">📅 09:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24507">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🏆
نمودار کامل مرحله‌حذفی جام جهانی؛ الجزایر و اتریش در دیدار تماشایی سه بر سه مساوی کردند و همین مساوی باعث شد که تیم ایران حذف شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24507" target="_blank">📅 09:09 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24506">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c8d7762a7.mp4?token=XwEeNQqmAUj0tnDfzXmo78CeEQwwxg6t38p1Wg7uTfpbT-riq-Uxgd7D5JLjFqHsU4P1QAUoR7rdYw1x1KxPeKEfISpY9kX9-H2uMGbi_qEKnU4bGH-27pCzA7FynovZDuOZqIayJlvCJqQ2rQFSdLLtlSqfoaSQXmPyLSOPY62_ZLcvgr8xZLm2PNWONWoM1U9UUQy-ScEnnhn0PFAKdCZiJLDbaqqj6PRQ97Axcd01ydFeYyXCF0vi9rwMt1b4NomPB7g_PYqBD59buw6olVCqkpSfFCrO525sg8sUD8dmaO38CwoVtzdh1qRbibG3-SItJgG2y6v8sxE6TMAAnrbWqG4fRZKDW7Jh-3g2xfbp8tLiE-NyETdyV_a4A63DYv-fmOo5UhdGS6MnWCLCOTQqPgSDlbZQBRxwI2IeOlyqHYkAiodZRS3YMY8ddPRKvWomAilf_4zQJSivcq0KMIPSymwFiBL2mDKdJmVqxI9IEwgnD_PiVNq_XP3cn7PrI8RtGYarwwT6QG6fiZKrsH2xE9xu-bzxiERdmj7qj9vAtVgdDDIAxdU7LYJsLqLy_P2kZbzbKaJLT7ySI3Y7yYjjDSThcw2tGlUFh120KopMOsuoyJC-agAO4ddofHn2mOiQof8J3zt_ToYHwjs4sCM8PJbyDq6OuTFu1UHtsnY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c8d7762a7.mp4?token=XwEeNQqmAUj0tnDfzXmo78CeEQwwxg6t38p1Wg7uTfpbT-riq-Uxgd7D5JLjFqHsU4P1QAUoR7rdYw1x1KxPeKEfISpY9kX9-H2uMGbi_qEKnU4bGH-27pCzA7FynovZDuOZqIayJlvCJqQ2rQFSdLLtlSqfoaSQXmPyLSOPY62_ZLcvgr8xZLm2PNWONWoM1U9UUQy-ScEnnhn0PFAKdCZiJLDbaqqj6PRQ97Axcd01ydFeYyXCF0vi9rwMt1b4NomPB7g_PYqBD59buw6olVCqkpSfFCrO525sg8sUD8dmaO38CwoVtzdh1qRbibG3-SItJgG2y6v8sxE6TMAAnrbWqG4fRZKDW7Jh-3g2xfbp8tLiE-NyETdyV_a4A63DYv-fmOo5UhdGS6MnWCLCOTQqPgSDlbZQBRxwI2IeOlyqHYkAiodZRS3YMY8ddPRKvWomAilf_4zQJSivcq0KMIPSymwFiBL2mDKdJmVqxI9IEwgnD_PiVNq_XP3cn7PrI8RtGYarwwT6QG6fiZKrsH2xE9xu-bzxiERdmj7qj9vAtVgdDDIAxdU7LYJsLqLy_P2kZbzbKaJLT7ySI3Y7yYjjDSThcw2tGlUFh120KopMOsuoyJC-agAO4ddofHn2mOiQof8J3zt_ToYHwjs4sCM8PJbyDq6OuTFu1UHtsnY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
نمودارمرحله‌حذفی‌جام‌جهانی؛پرتغال‌به‌کرواسی خورد و دیگه تافینال احتمالی شاهده تقابل آرژانتین - پرتغال نخواهیم بود. کره‌جنوبی از جام جهانی کنار رفت. هرنتیجه بجز تساوی در بازی الجزایر و اتریش رقم بخورد ایران به دور بعدی صعود خواهد کرد.
‼️
حالاالجزایرمساوی‌کنه‌میخوره…</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24506" target="_blank">📅 09:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24505">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iNwJKurvAAXLCSjweE1GHs_IDzk3ST3G0N83UMznjsGtEsr1tHnhqAXei3cmqnUB2xBPlFqwOCLkZK9XljT1LizkbZLCEiCwSQ8t7KAn041W3EbGeAVBHs9Nj85Z8D6dm7dSZT3NHrP1dqvhJ5fQBE1hvDi5E1KNiT1Nql7Fe-grSu4Ms-zXDBdTbhnTBDhX-UO7Dk-Vf00-2GBrV0adbyA1obO7USYCXbrzMWn1HTgubU9WGU-xTKqPbjuKekzFvGKEF0daF2f7ZdEfqVze3LYPCgFUqb2UsiLSYeKMpQDyStWZZqXAGOdI3kTSMCrOnH7RDzATd1boV8iMIkJMfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودارمرحله‌حذفی‌جام‌جهانی؛پرتغال‌به‌کرواسی خورد و دیگه تافینال احتمالی شاهده تقابل آرژانتین - پرتغال نخواهیم بود. کره‌جنوبی از جام جهانی کنار رفت. هرنتیجه بجز تساوی در بازی الجزایر و اتریش رقم بخورد ایران به دور بعدی صعود خواهد کرد.
‼️
حالاالجزایرمساوی‌کنه‌میخوره…</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24505" target="_blank">📅 08:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24504">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb1d0295ee.mp4?token=Y7CONP7ywq7Pyt8M8Q4fXma_GJ_wyibB3jbt8nWEydSw1EoAjmpKLNAKjLtUEJ4ckQtjr4d4mRO9PvzDF9NSOep0c02fxT5cCnNGvGNSO7BO6Fawl7G-GPaOhWVpgq-HZLpFhlc2Sx8YsyFVgJNybzi05K_OV2PTy_ahm1EU5fmJ2-FGRya60Qukn4t9Ifs7HEzzoHRJTdw2z6X8NewCnFH2HxWmnzyCbGBP63qfMeZAQXRwaMmWXoCESR2TCu5Qc1KVdrffUqG3TPOtEEsje1LDhg7ZsAuLWBMGuAWWzHNCtX0iV7bnT4nGCEDmVklPTiYl-Mv2B_wtO3WLw05P9EK-V9RjT3jTt9Bsm60hjUBR8alyZ-XiOQP63RRorSZjSW-da-j11InuMb15fADf-ZwqZVsG487fdJHNvZeG5qxGFVqQqgDChs-JWLav5GXyleVACACHWHPoZBYijjk2bPUOtN3EDFz5TxfRKPtwboKYL-9O2-o-NH92GMHufeioJRq5ZUG9c9E4tUrNiKkqo185rPCTdiPdz1RhezukDu7_zwQ4JjbksOjTW3IekypK9AXSM05fDsU9oZP4OsPNNmyNGG62p9Q_RHM6gI9HCVQqBMcpSsPne9bxK5jxDITk5AhV_Rjw_eWYLQ-3tTbtaxz6hWX79jLDeVFilEukUc4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb1d0295ee.mp4?token=Y7CONP7ywq7Pyt8M8Q4fXma_GJ_wyibB3jbt8nWEydSw1EoAjmpKLNAKjLtUEJ4ckQtjr4d4mRO9PvzDF9NSOep0c02fxT5cCnNGvGNSO7BO6Fawl7G-GPaOhWVpgq-HZLpFhlc2Sx8YsyFVgJNybzi05K_OV2PTy_ahm1EU5fmJ2-FGRya60Qukn4t9Ifs7HEzzoHRJTdw2z6X8NewCnFH2HxWmnzyCbGBP63qfMeZAQXRwaMmWXoCESR2TCu5Qc1KVdrffUqG3TPOtEEsje1LDhg7ZsAuLWBMGuAWWzHNCtX0iV7bnT4nGCEDmVklPTiYl-Mv2B_wtO3WLw05P9EK-V9RjT3jTt9Bsm60hjUBR8alyZ-XiOQP63RRorSZjSW-da-j11InuMb15fADf-ZwqZVsG487fdJHNvZeG5qxGFVqQqgDChs-JWLav5GXyleVACACHWHPoZBYijjk2bPUOtN3EDFz5TxfRKPtwboKYL-9O2-o-NH92GMHufeioJRq5ZUG9c9E4tUrNiKkqo185rPCTdiPdz1RhezukDu7_zwQ4JjbksOjTW3IekypK9AXSM05fDsU9oZP4OsPNNmyNGG62p9Q_RHM6gI9HCVQqBMcpSsPne9bxK5jxDITk5AhV_Rjw_eWYLQ-3tTbtaxz6hWX79jLDeVFilEukUc4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
جدول گروه K و L در پایان مرحله گروهی؛ کرواسی غنا رو برد. انگلیس با درخشش بلینگهام و کین پاناما رو برد. پرتغال مقابل کلمبیا متوقف شد. طلسم کین بالاخره شکسته شد و گل زد.
‼️
باصدرنشین‌نشدن‌پرتغال و صعود بعنوان تیم دوم، تقابل آرژانتین و پرتغال تو یک چهارم نهایی…</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/24504" target="_blank">📅 06:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24503">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jAVf9zTYDX50ZFUKIytSA6H4cAwYBpLFjP5rT_H3W6PyPfoQUtJWt6enFTAffg8R5ItvCb4pfjm1Yj0YS0lc6ecakwxKK2XY7xs1mz5Qqj14beWktm2SDZjRHNZlN47fAzJceY3IKubFzfMpyq1tqZSZAdi5YHElyfl2N7ggAgJLewG51veB49neCV3l4NLwMZVcOndvT8rcUELhUx6WpupbfgnhAbotAbRffjlUbqac6GmOFqntmeEHMXbqMLovaz3h1FfVNXrlwz9B4UpjqvZdsO3g5pgNRvT4r1uXMSdUNgbHArXYuao8jv9OSXI8ybvFB2NrqG4odhD25JKz1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول گروه K و L در پایان مرحله گروهی؛ کرواسی غنا رو برد. انگلیس با درخشش بلینگهام و کین پاناما رو برد. پرتغال مقابل کلمبیا متوقف شد. طلسم کین بالاخره شکسته شد و گل زد.
‼️
باصدرنشین‌نشدن‌پرتغال و صعود بعنوان تیم دوم، تقابل آرژانتین و پرتغال تو یک چهارم نهایی…</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/24503" target="_blank">📅 05:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24500">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OVizT3rgbZ7QVP2pPbAg4IqsAUOwBqfWyJ34HMWIoqsCJEw-DY85_J7Z60kO2GNnxQr5oAGA58gf2YhRddLecHXucVw9Tud4LCBX31AC02ZLp0jwueTHIsZh73A-sfGFixU123t0k6BwIU42jATZk7XoxsCpvZa8myfhVLclm66XVauekcx2KOWvS0M8v0wJgBiVXPOiWr7d5OxDyEd-B_ZLnQS1y2_4L9OQFy7WaZOfWXJAHSueAib6QE9LmqF8AhDKBsm87wfSI2Nxzb0cvuIPPsQTSW_9ayreRtCm-LxkIt7XVYPUUVhnBcDm1dgcwYJaK5GGlWr_1yI6xn9sGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o8U1Ri6tJmlE4GrT4HktqAp-KjBN-7oIS4_2FnIOPL3-UrTUWP6lnlcKHRGsnrbfcw-7LS2q1CINwSOkZXB9SDKLKinxiL5FUkcwZiF_shAmz7FbtG0y9FGz2MPY_QQlPNkq3GbCwQiiLWq1DmF1cZ8Ezih8Fs4u3Jbvmtk7gUQMxwlf1vGpJQuiL9nHi8OzsAhbepwxTOg4RrBmSSHu-ux7HLMHCTkLiVxvpiWCGyoZgp0M0tVgCLobIp5s-H_xKpbLjbYP63kLTtpeqFpPfl0Y0X4fcaji-ve4N-nOF8RZcQpEJmnLAXWV3IGfggd2WCa0qmDQ25zV9nTLvcREag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
جدول گروه K و L در پایان مرحله گروهی؛ کرواسی غنا رو برد. انگلیس با درخشش بلینگهام و کین پاناما رو برد. پرتغال مقابل کلمبیا متوقف شد. طلسم کین بالاخره شکسته شد و گل زد.
‼️
باصدرنشین‌نشدن‌پرتغال و صعود بعنوان تیم دوم، تقابل آرژانتین و پرتغال تو یک چهارم نهایی کنسله. این دو تیم دیگه تا فینال به هم نمیخورن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/24500" target="_blank">📅 05:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24499">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hat4TulFspe5bBB9yAxD9OKIwlqfm4bR__7J9BIhaAZPv36bkt_7KoIVq_jQrho7DnBTAG8qPngu7nkgsIC3BzCmRs2-RNpNv7J9UVyD4VAW0_KK66-dyyxlgWEb21dD9Zn9qkIYM_GnodE9dKBrgW50PMdxQYP10TzURQy7adUpdRdQwlFDOBMpjk-dZ3DhRUXaN6CIArK1h8siI93TRclBt_sSWI0F4mDYHQ5j8X9bmnhBkGzhcthDWNt0Y2UqWotZooIblRitEnpY-xC-FzH8mMtk_dTY2eF-QuazGHbt88-vRBrA0PSwfTazvJ8ICTKqtEe0xKEW7MOYWxB2Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ طبق اخبار دریافتی رسانه پرشیانا؛ دراگان اسکوچیچ سرمربی جدید پرسپولیس قراره تا آخر هفته جاری لیست ورودی و خروجی سرخپوشان پایتخت برای فصل جدید رو به مدیریت بدهد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/24499" target="_blank">📅 01:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24496">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‼️
خداداد عزیزی کارشناس ویژه برنامه جام جهانی پادرمیونی کرده جواد خیابانی و پژمان راهبر رو باهم آشتی داده. دم صبی دعوای ظاهری بین این دو شکل گرفت که خیابانی کلا قهر کرد و برنامه رو ترک کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/24496" target="_blank">📅 00:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24495">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nkgg3qf2AFz-F4CvoOwW06OyPJX02oGeow4PQ28vgwBh52c5ZEuB16nxRWojxjz5Qfx_GQMXYl6XxiKAXWHB0d7LndEFIGwzi_Xp242CeEzTLM57p1ptGPmPztMi1MSJ7ydjeZzrdsFOiEBPRuWQ-blp5LXb5siHr0eUPaUxWiHrNmBCFZXBbkdcnBgkYFbTApXLCr3QGatfI1PBoqJBSo0IaV3aSBwxtOREi4vTv3tXLBqg_iaZ-bPORUBJ0TOCVDMnhZ3IizYRAZxaRX37Lf4RJB8ERa6UorAnBTg8AH243cupMIQcOaTuFl7VhdW-fO9c3wGsKwePTCmQpd7KVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
ادعای جدید نانا کواکو بونسام جادوگر غنایی: من‌احساس‌میکنم که جام جهانی 2026 برای کریس رونالدو و پرتغاله و آن‌ها قهرمان خواهند شد. قهرمانی‌پرتعال دراماتیک و باورنکردنی خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/24495" target="_blank">📅 00:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24494">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RNSboTPj6EunEFVeBpOpqqIQrR_hhodJVrr3qUZkOOa07Yl4pXbZ399f7cDj5Ow09B_BTYOUOQpQVBtYxELkpxUwNqkABx3lmLv72aIN6Fj-sQf3b2AhxjEW-dp-xpzF9YdZKdGwqM9CA9ND0fqkfvFTmetQunFpFFYgpwSNY3Ve60sW8csVOCxIuD8y0OLms8_pZbtfvriJQ0WcdbTFDaysbLPDqL_q_oQt-aQg7hfDbof9eJC-y_02nukdSwzY-Y3jwDJG-PXqT9I4eacQihbA-FPYCVNxbNwxuCJDlJSCtqjtduYLTZ8j3CDScpzE4sTF0hH5m8vUkn_Q473q8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خداداد عزیزی کارشناس ویژه برنامه جام جهانی پادرمیونی کرده جواد خیابانی و پژمان راهبر رو باهم آشتی داده. دم صبی دعوای ظاهری بین این دو شکل گرفت که خیابانی کلا قهر کرد و برنامه رو ترک کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/24494" target="_blank">📅 00:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24493">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tOwXUzQG_XYSVpUuFg9B1182-9h7Zhz-xLDRj_Upx4xA-TZQ-5rBGTOFjgcQ_cxnkFBnZ-tcMOTw7Mjg7A_eKSgnCosTSB5poyNevnInf7pk8rcU3zcSCHrCjJpsLW95TAXbF3pKFvIqKRfKV_HQCTB7PNcj9espd5l71AMT9_hiroERIFHO3ZQl7KhWam7-aqp9Yatd5zUmsiHO0uIFaFlDGi8o3dgm8zfAWJIlCb05NOGDkSurkVbxNPdJ0jC7FH9yYFciQhrGOM1gmSxYjH7rlGenDOESZh_0q6sXn7SYJ1XxfP4xjL42otfnvkOyhDtG7zKMRl5c82pTG_EAoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ایجنت‌نزدیک‌به‌مدیریت‌استقلال به‌ما خبر داد که ظرف 72 ساعت‌آینده گابریل پین قرار داد خود را با باشگاه استقلال امضا خواهد کرد. همچنین به محض باز شدن‌پنجره‌تیم، چهار ستاره ایرانی رو به استقلال خواهد اورد و ممکنه که یه مهاجم خارجی نیز بیاره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/24493" target="_blank">📅 00:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24492">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f250d91879.mp4?token=eMJLIVINyReQr50L3L0jHORkecAnBmPnLdYr3ghJ8dnDg51bKOoWCmAgas7uX7N1oRplrO4lCjdc7Z9o9F5CAbQEdvZRWMOR1c_NJJnMEMEEYYObc5UCDP9QglnXNhREKlRzuO-2_v1f0dV4Vo5sPL7nFJGLNdj66I34Mx7IddWlWUJogihzEDWShJuDij5Mazp9a5VQieycW_11b8XLOwkNjMFqAkZNcb6k7WzkmemH3qPMyOe8DDqCxAM8SCRFkhezPdKZlCQE0oqL9kFhF__CThkWqWzHOh8m2VM7fN7U5RmQ_fnMFh3sKLOAuurpu2mydah5ple6lCUHOnQa9pcQpfKR1QoU_Yx5hmkkc3olgiXw5EHxD9Oh_WLfiZZi8nM9oFdMH8l4OscFU2TT5zzqDLxi5Kc9rS8cXiJQUuP1_1RWqC09blAiDPzz5BRo2wJKby_WcCe7fvKxcMeZSCnrVm3MDjOEwoh8if_sokbFJ5srnkFlSqMBBcubQKsXGMNG4YvxRiNU9FmPjE_rH3v7tAKgZQw6Fo0qdmXp6rSSnebrCLtBH3XGLFcPB5y-lsa7cBZryOU5DES8wA9TCMt-odzW56lHhHabrHzFhx1ks1fKQsgooQRloNMw8lE9YstCSmkTzM_wzk0JfqR3aF7Jv3uEVQPEpDjZDgdzx-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f250d91879.mp4?token=eMJLIVINyReQr50L3L0jHORkecAnBmPnLdYr3ghJ8dnDg51bKOoWCmAgas7uX7N1oRplrO4lCjdc7Z9o9F5CAbQEdvZRWMOR1c_NJJnMEMEEYYObc5UCDP9QglnXNhREKlRzuO-2_v1f0dV4Vo5sPL7nFJGLNdj66I34Mx7IddWlWUJogihzEDWShJuDij5Mazp9a5VQieycW_11b8XLOwkNjMFqAkZNcb6k7WzkmemH3qPMyOe8DDqCxAM8SCRFkhezPdKZlCQE0oqL9kFhF__CThkWqWzHOh8m2VM7fN7U5RmQ_fnMFh3sKLOAuurpu2mydah5ple6lCUHOnQa9pcQpfKR1QoU_Yx5hmkkc3olgiXw5EHxD9Oh_WLfiZZi8nM9oFdMH8l4OscFU2TT5zzqDLxi5Kc9rS8cXiJQUuP1_1RWqC09blAiDPzz5BRo2wJKby_WcCe7fvKxcMeZSCnrVm3MDjOEwoh8if_sokbFJ5srnkFlSqMBBcubQKsXGMNG4YvxRiNU9FmPjE_rH3v7tAKgZQw6Fo0qdmXp6rSSnebrCLtBH3XGLFcPB5y-lsa7cBZryOU5DES8wA9TCMt-odzW56lHhHabrHzFhx1ks1fKQsgooQRloNMw8lE9YstCSmkTzM_wzk0JfqR3aF7Jv3uEVQPEpDjZDgdzx-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خداداد عزیزی کارشناس ویژه برنامه جام جهانی پادرمیونی کرده جواد خیابانی و پژمان راهبر رو باهم آشتی داده. دم صبی دعوای ظاهری بین این دو شکل گرفت که خیابانی کلا قهر کرد و برنامه رو ترک کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24492" target="_blank">📅 23:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24491">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a1CyeJTd-lqFJe757ACqJ4cHEUbNEvN1O1ppgU_OLj-cWFDNYjpRRTi3z-RZMpauTNLNApNOf0-fRcScWjBMQFFqj2sRfyWINcBhYM0gPpzuBaRSiRNH66rBfBwZ92na7mCvqn01F_h0QcCZbCVOym7XSex6NpfPd4IdoYuig63xkOaWGlgQ8utp-K5WPzsioYLXjbpSgu02bbbstBgHFy0GR6nbj7OedhxS7kpEEdx7sAiPZsgHwpPckKRDmSdt_1kZHctSDlHDhBSRk5_GX0_Z75ZUE-RVMgTsY-k44O80KqlG2j_FxutsoknMASyVdCgAMq6noErlYsY95-Tj7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدارها‌ی‌ امروز؛
دوئل فوق‌العاده حساس دو تیم پرتغال و کلمبیا با قضاوت علیرضا فغانی
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24491" target="_blank">📅 23:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24490">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSDciVL8b5C47INHEi11jLpW2wjwPh8joJGtjT3u3-wIOOwlDQuh2F2oc2wjI0dmDDUxf4nlVkzaabsCeZUwoCRh-50VwgHLVZID5JOIEkr3ImVe69z7dokkvEiB11aVLhV3rfKESuXbWnoUsFvLgZoXTL1zhm1ImdMvAEwHmxyiga8Ad6Dp8lzGml1WvLDm2vWAz1gbUNZuUUnzCxu5gHqU9YuCtINh8q_Cw7f0Uw_1IMwisVFGQK_WnYh3vnjfA3n6UcB9MWSvOrAoXv5Lu2U_Zc5Xm6hK70g01wNIFNs_39KP3-wC71O5VDCVTM-UGmOYIDsebyrbYKMvzkVTQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌ دیدارهای‌‌‌‌دیروز؛
ازنمایش ناامیدکننده یاران والورده تا تقسیم امتیازات در جدال ایران و مصر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24490" target="_blank">📅 23:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24489">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/apg30h6DE5lW9goKQO0uGWSsXTx_PIsWVFQonTTHT8dqVIg75ntCgqZIMjnEV3pnmWGZjV-j-hQT1Kn8Cyfxhr6M9g0m8DLLQ2OF7dZVybEaoCjyYHIR0K_EqA-DgqF703KtSOyCtdMXbqc_IcESseRaCGXNbJrdfw0QXYkAOheiiRO912zdk0lzGLL_wCuap0kTVEQKK9cgmXMxuUHsyiCMd4w-EjwmD9I3WxQ9epiZyabqRZ22rrt05XTGgtGGhwAynF7cvpGko7q1-R9_pDo3hBJlva7k3nYFT2oY9-9MNoS73x23jJnEB9Y3yC7iR-aneb9Zl4M6p6SYoidpZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏳
هنوز چند ساعت نفس‌گیر دیگر تا مشخص شدن سرنوشت صعود ایران باقی مانده…
‏
🇮🇷
ایران برای صعود به مرحله حذفی تنها به یکی از این نتایج نیاز دارد:
‏
✅
🇬🇭
غنا،
🇭🇷
کرواسی را شکست دهد.
‏
✅
🇦🇹
اتریش و
🇩🇿
الجزایر مساوی نکنند.
‏
✅
🇨🇩
کنگو نتواند
🇺🇿
ازبکستان را شکست دهد.
‏
🔥
🇮🇷
شانس صعود ایران: بیش از ۸۰٪
‏
📅
تمام این مسابقات روز ۷ تیر برگزار خواهد شد.
‏
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
‏با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽
👉
betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/24489" target="_blank">📅 23:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24488">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c851ba0755.mp4?token=Ji88v4nciCUQKaiO4oA9l3177oyOq-p-AtKtylSCpetIHt0igE4ficYT5_Sh_YDuoBpdYjRZGmaExfernsehGaKwQPiZGT1w6NU3KfvSszNRH65TBKNQzNEnnybxAWV5Cpm9owVywKvBA8xuHwcCHVYuJlqHUgvoDxOT38wjKFJbRx72okl5HZyHLl0-61J_ndpaMlLWkdICQc4_yqAnM43wgq2XqPbk8_r9v8kZ9eyD8pIbWC-ZJ1xjqIUenfueLJ1koGm2Fw2v_tHKpcOk0HnGHsvxDPUcVtVeyA0SHMOk2CVUa6BukYXnjc9Uzvt5OHbLMnWr81pP103SxIc-VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c851ba0755.mp4?token=Ji88v4nciCUQKaiO4oA9l3177oyOq-p-AtKtylSCpetIHt0igE4ficYT5_Sh_YDuoBpdYjRZGmaExfernsehGaKwQPiZGT1w6NU3KfvSszNRH65TBKNQzNEnnybxAWV5Cpm9owVywKvBA8xuHwcCHVYuJlqHUgvoDxOT38wjKFJbRx72okl5HZyHLl0-61J_ndpaMlLWkdICQc4_yqAnM43wgq2XqPbk8_r9v8kZ9eyD8pIbWC-ZJ1xjqIUenfueLJ1koGm2Fw2v_tHKpcOk0HnGHsvxDPUcVtVeyA0SHMOk2CVUa6BukYXnjc9Uzvt5OHbLMnWr81pP103SxIc-VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویدیویی‌متفاوت‌ازگل رامین‌رضاییان به مصر؛
جدا از ضربه دیدنی و زاویه بسته رضاییان به شوت زاویه دار میلاد محمدی با پای راست توجه کنید که دروازه‌بان آماده مصری ها رو مجبور به دفع آن کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24488" target="_blank">📅 23:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24487">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hEBCHodmtFGMbzigKvMj_rhVAUeBVmyx73kH7-32uf7CGuszxemtE_etNdrO0TtRKKOROiJC8SbBaqJMlkAtq_y402WlOMnsLYDnuqBbJZ6RmKE5B1xniAAg4VDn7fAWo50dOR99GT-omiLEe0NjYg28_Y2GhUMwVXgOsu5N-WzFGatobGY9eCETstDHItcaDbqg0ehMUAx5g0Ca8nBWx7KOdx10-iu4aPP1Y0WAvqvzOOuO0pre7TNidjZDNRebygdKzfxYuYigGKYr4g4n6-fOmLou4K7uKa31q31WOVTkF5e_yw7qsFzeb4CDmcG1Ra-E8tDih0BeYmR4kvBXig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
مهدی طارمی استاد خرابکارب در بازی‌ های بزرگ: خراب کردن موقعیت مقابل پرتغال در جام جهانی 2018، اخطار گرفتن قبل از دیدار با ژاپن در جام ملت های 2019 و تضعیف‌تیم‌مقابل ژاپن، اخطار گرفتن قبل از دیدار با ژاپن در جام ملت‌های 2019 و تضعیف ایران مقابل ژاپن، خراب‌کردن…</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24487" target="_blank">📅 23:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24486">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJoOF3eakJscWW4_AZ3VVYZm_-_xjyz2wGsOBIMiIANuyaD05ZYhliFv2-YYDQp_uKPYPcE_baJmKrqVlrwe8myY51uk7Cenu-rc17Spexaru4YvlGUhqpag1CPEQhZaSfNsKqvez3OVxq8OKX3bbi_o0nJtUEV1cxW2wltn8O8_mp0fZCtG16gZvVff700UaWD1SZNHxeiFNTd6DpCz1VXYMa5AutFtqsDN_zIbklIHrSfd0GfW7NZJiyc5g0SxaQ3VejvK2GbDgdx3CeLz72ozpphdZePo1MhLfwsUKVHQENtcldKpoJrIFIzZv2_0w4LXwxksFWt1Qe5njSOe2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بعدازبازگشت‌زودهنگام‌نساجی به لیگ‌برتر؛
حالا درفاصله سه‌هفته تاپایان‌لیگ صعود باشگاه مس شهر بابک به لیگ‌برتر نیز قطعی‌شد. اگه جدول همینجوری بمونه صنعت‌نفت آبادان در دیداری پلی آف به مصاف مس میره و برنده اون بازی لیگ برتری خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24486" target="_blank">📅 22:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24485">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hNW8XpcSVxDmdkSAHm-mVeBKVs1ycBqS-JcTKzHPsEwz-zrF2td6Zdb8iGiYGnjcCxFQ6K8UFdo_wWTkxr9rYJEYAyH25bXjkeBr_LBPC2LzVlzMXsvzAmIunrpYoISKWAMmHrNpXD7vg4t7e5W1711dqiD1kljGvZdCBcwF2MDP9LSSDdcQbFTMoq8pMT0hR-LURMVPXyU602Wle2teasr_QQlHKe6Zb7xExknue6QBhUaXuSvnNu2-Bax7PJhO4zqmyG-IVLWE3MyGl3SwBrGpVG_GF2TzbfNpSbyKQNSdq9llVBKZZPlpcB83EdOqPUDIEjfaFeqt0zqh5574LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق پیگیری‌های رسانه پرشیانا؛ این‌استوری‌جدید اوسمار ویرا مربوط به آخرین بازی اوروی نیمکت باشگاه پرسپولیسه. اوسمار به حدادی اعلام کرده با دریافت رقم توافق شده 900 هزاردلار فسخ خواهدکرد. ضمن‌اینکه نماینده اوسمار با باشگاه تراکتور مذاکرات مفصلی داشته…</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/24485" target="_blank">📅 22:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24484">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EScO5Kgh_AD_MY7xuS2zP1uFaUqycVeuB4F7lmJjiQngC-M72qrZBKxrLcBJN1QZi405WYy1MHEksY1yYlgrE9yZ4ffC_f8eC2d9rIqIbvCO4s1vh9awRu3OqWERB_uOGb189z8H1AyUWcTiJIJD6lVH82XPus6kge9gXLNBrT5D44zttyCejZvVXOFb_5L0oPEoVpHYqoTw-K6zA6878XIsD2iUMfPy2S4Tq40LgjOeiIwYL9gaeuncGWgvL2zvlCuneykB47bpw98MLcpsDOgs2-LNaG0P7bOQGytBeyFW4yoiXAqC9vmLW56qmV9rAP28yuzHHlLndDw49tH4TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگاتون‌بریزه؛
یه زن‌وشوهر جوان تو شهر قرچک که تازه هم ازدواج‌کرده‌بودن بخاطر اینکه زنه طرفدار تیم ایران در جام جهانی 2026 آمریکا بوده و شوهره دوس داشته که تیم قلعه نویی ببازه از شوهرش جدا شده و گفته دیگه خوشم نمیاد باهاش زندگی کنم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/24484" target="_blank">📅 21:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24483">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KlSgIqZ_y-q8Jw1sWaf_aS8xDyRTS_yF16mqR8VoFQz3VwWTMSLOlTDNCX2AfpY3EpbvMgjGniJVoOqswzCSt9W5R8WmyAX2QqJr0li1siLL4J9qhdUWUcO5rvXrdIqHS8xYafPWv1_MZwzpB_1EgUdyZdde8mE1jrNankDKO1zcfAsopahOQa4s7xQ-KfOvGTI6myE9EGwe9z4QVLqqXdO7WJCJf6_RaYpR6Y_E5auuPYJq5ub1wprct2qIw4yKO1P__7LhqN2VU7Za6uDkMF29dQLwpvuKVy-GPyITKvOiWuGBLK4LKdnjBHwJfHdaCdnkHLVDtbworLF0yVVJGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇨🇦
بااعلام‌فلورین پلتنبرگ
: بایرن مونیخ میخواد در این پنجره الفونسو دیویس مدافع چپ 25 ساله خود را بفروشه و جدایی او از بایرن قطعی شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24483" target="_blank">📅 21:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24481">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vEozt2sL_drz7UVld7CjnI3rG4Sg48i7IGkbcSURH6aqECEsfj5sC0Wb2TZenmk_KbKqv1m8cwKPitFR41TYQblkljksjI3bWlvNa0z4COrVmBNgJv5zw_WCVC6H8z1RVCtt_l_RunHbTyJ0kmatLInGlU9GzIhI6WW_U9WfWXyIxxS_SAohSpTWP8X0rkH-3IsAJdDTOUZlAyPpTFfqechye_PLZ6Up4qHaCNTxv09hadAbz1hOdWI4a_7injsfKjv-0iE2p5mhSYm3fLg62nvW5bm41luquamk6o5Vfd3iYcSFjJWO6buogjrS9mEGSSafcW1g6wjD_W8buttBmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🎙
نادیا خمز دختر پاکو خمز: من علاقه زیادی به‌فوتبال ندارم اماامروز همراه‌پدرم بازی ایران مقابل مصر رو دیدم.ایرانیاخیلی‌خوب بازی‌کردند اما شانس باآن‌هایارنبود وگرنه میتونستند با اختلاف دو الی سه گل مصر رو شکست بدهند. امیدوارم ایران به مرحله بعدی صعود کنه و…</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/24481" target="_blank">📅 21:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24480">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g0C7LYUhvlx6yBLzeUVeVEeDjEECawHGe6bWRCYfaOx5FfG66gA-RsmZANpYDi0Mo5nxECKn_1rripCZHgle-TmKjm96SeqnPeH6Wk4Gc5rErWpDNr1j7HfUm6HyuZCDbaOBE4cR1dBE5VwjPE2iP6EQQaMBYt__FotO0LzkqXfILsraK3w1BfOKc9jRycEZ-a0x3F7qmqVInQEjkamMybWIRonS4v0dnD03xCqsu4XWTd5_B3XQpeEz6dpAeaaNtcyewskfKOVkoiFm52SYe_qPfrILe0YEkAz6oNLJnTnb2dRsmyOP5nILELbQxJmE0ejOE64MSajAplaZTI-2EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یه‌نگاهی‌کلی‌داشته‌باشیم به تیم‌های صعود کرده به‌مرحله‌حذفی و تیم هایی که در لیست انتظارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24480" target="_blank">📅 20:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24479">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kkYe85gCQyhbGMBijAufJG_i25iWikVd-b8nFjBiVD4pKI3BTR9h9-1J2CzZRS_WqF6xO4o-juhk3iP5xklrxiA1p5PgtGwtPVxlPK7ks6oQ3FPR5_jE8FpJITngjsIC7-Ivx3yIgEw0C01t2i_I4Mq0aR1zv8DxY4968cuzZCTAZnYlFjNQunN3rrXYT-2ejxo2JsSe8fTRPAcPQFkiOApMYiHhamgR-rNHO9yhR4ouRe1s5pZt41yVd6IrWm0jGPgPMNDWv-9fy7suwXEuMfYAHlebcFExcx-s1Zz0FqAnxhvZBSiLycoYlRIBOZgXT0Y7tYbslDCoe140e4l8GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خبرعقدقرارداد باشگاه استقلال با گابریل پین که از امروز صبح تو رسانه‌ها پخش شده رو شش روز در کانال پرشیانا اعلام‌کردیم؛ مدیریت آبی ها قصد داره بااین مربی ایتالیایی قراردادی دو ساله امضا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24479" target="_blank">📅 20:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24477">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79f3bfadea.mp4?token=nwpmbMnVwadn_F2ohvWLoOr88IqTEHm8v_sUMj7fp7J6qB297ey4nT89pablqkkT29ObKLNGXO2KgM7Gv2Z8ccE9y5NNLLonLv4pem1NCJxvMKvBz4fS4Nvpo3YY-TjBBIdhjH-wf45HgJYStkgG5ODYqHfGUbBUSz6ip2WVcs3u2MdQAQR8NDnVb1l3puz8vqIbjnFEpR7t7sdX-2DkayUsgtxw3ILFOSktQadTnnoPCCBz_yu7QwtICIXoAy9p4sH87Kcp0tbEykk2hubrSVA5_oRHcWI8yi-9OFUP6H8AIh90yMt5Q3WaXYvXwVHPL6YQszxXO_SK-nYQBRlDnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79f3bfadea.mp4?token=nwpmbMnVwadn_F2ohvWLoOr88IqTEHm8v_sUMj7fp7J6qB297ey4nT89pablqkkT29ObKLNGXO2KgM7Gv2Z8ccE9y5NNLLonLv4pem1NCJxvMKvBz4fS4Nvpo3YY-TjBBIdhjH-wf45HgJYStkgG5ODYqHfGUbBUSz6ip2WVcs3u2MdQAQR8NDnVb1l3puz8vqIbjnFEpR7t7sdX-2DkayUsgtxw3ILFOSktQadTnnoPCCBz_yu7QwtICIXoAy9p4sH87Kcp0tbEykk2hubrSVA5_oRHcWI8yi-9OFUP6H8AIh90yMt5Q3WaXYvXwVHPL6YQszxXO_SK-nYQBRlDnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
اینطوری که پیش میره مکزیک سال بعد یه افزایش جمعیت چشم گیر رو خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24477" target="_blank">📅 19:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24476">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWAP6bPZMqfEXlsjWyshhfe6E27yoo9NBLVCBfg2fZ0TV9jBNP7wTBSttfadABSSJ5KEfXkanXbkse5vD6wRM_VCA_pc57-tSWVNV8YkZW-YDQIAqk2CjeNqy1lmotOGCV6xCWXCGnbKz6LTwJrPYYfUstu2CnTkRGT9-PA5NRi72DxSk-f_6ot-meaDl8o6Fj-0UQFZkgeTyIjrN2plwwbAY9If1d1NZvLqqaQ_0FEoAutS2Ve4k2x-HAVsrPsZQ6B8ka6w-pzm_BexwCXf0ir-2ywOUb7WtOhHTE5N-_OjgBAsolKgt0m2hTEk2a8LkFG65cuMJ3n8mErG9YI30w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برای‌صعود شاگردان امیرقلعه‌نویی به مرحله بعد باید یکی از این‌اتفاقات رقم بخوره: الجزایر - اتریش: مسابقه برنده داشته‌باشه؛ کنگو - ازبکستان: تساوی یا برد ازبکستان؛ کرواسی - غنا: پیروزی غنا؛ طبق گفته رسانه‌های خارجی ایران85درصدشانس‌صعود داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24476" target="_blank">📅 19:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24475">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H2zroiwbx1op2QRJlDYbXGeW9ux7T8GvGgaPD5L-xhe_5pHDa9wzpqn0WEUkKRG2aErpqDmfmaY6edqLEil8XNW8FknQHZ0jx6bCtoAofTDXcugN7vhREkxUGxqL31ASU-rQcAoUP1GuB8cheBBllZKKL78RfUZkBqiPZVEewz6b0wYaBm_yIa7kbdSpzB0WoizalDkrVmIT7CcXypLW3MaAIsOBqvbmi6cGPbBbt4DhSl_x4Nry-94eiTq9sbW2UsPVQHlf31_yCjdMmHXViqfqo06FHvr2-Ppx6IVDeCjI4q3dxhZ9Wi6D6_-lRCfjCbXTgeQIlTL2gzZVd07_Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
باشگاه رئال مادرید مذاکرات اولیه خود را با باشگاه چلسی برای فعال کردن بند فسخ قرارداد انرو فرناندز آغاز کرده. باتوجه به اینکه انزو با رئالی‌ها به توافق کامل رسیده انتطار میره بزودی توافق نهایی بین دو باشگاه بر سر این انتقال انجام شود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24475" target="_blank">📅 19:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24474">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DUUQWdN6Q2X8sQDiwM36sqoUw22INGMvy3XdVNhcfLGHa8ME2wSYJnG8EHaXAEWtzeLWHykurZH16_7a3tONA3CfEqNwVyqBCjuM2hpeXibGYn-PJoYjsiIokRk4bj8toMDzHedfDJSVXtONIvv3zQq6Sr7F1TFEFrG76hW3FFxyiyjd0SJ-9_0G_c-uwXWVcXv8Lu2RIhzPlWs-S_SrEJWqkBhO4rqNj-Vuy7s0fdEFMtVJT_LVZ2F2p21zs7KayRzkgmEn7esyBA_2NIASucRIHKCU7f1ZJZX9v_oFicRy3-PYdS-1BSw48ZMEv_nhj0Qi3JHjgU2btf-7b8vA2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کارلوس‌ کیروش سرمربی تیم‌ملی غنا در گفتگو با اسکای: امیدواریم بتونیم از کرواسی امتیاز بگیریم تا تیم ایران به دور بعدی جام جهانی راه پیدا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24474" target="_blank">📅 19:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24473">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BdURMMhgZ-wBcvq4YUSt38sLfCbY7Y_pYsjP1RSJ7j-cj-5lMbExvvFGZyODTh_HsiNu2LxHn4TJq6_-8H9pr4kojXKy51Fp2wOGcQT2aoRWGa1SlTkaYXUNARw_OTTuOuum7oyZJSyJEN48Who4zcd2m_qAqgCwSyvvO6vlqBXrCGJ4c_VzfscEvwZkSPMEExzuUn_hDshK68fuhIBFgA8EyYBeDhjBrTSjofYF-xLMcF7sqgZF0JVkSR_PqJ2vfMK5Cs_rpKLZ-kzAltn8VSL0axu_5nPF6_hQ7THojPIXYCxhck933_l5wP13eCMKJIv6aF5xZimJK6MoCuWv1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دراگان اسکوچیچ کروات‌دقایقی‌قبل‌رسما پیش‌نویس قرارداد دوساله‌اش با باشگاه پرسپولیس رو امضا کرد و رسما سرمربی سرخپوشان شد. باشگاه بعد از فسخ قرارداد با اوسمار ویرا پوستر اسکو رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24473" target="_blank">📅 19:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24472">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e70b182e85.mp4?token=WyzOmefoIQMGnMIQgfSqqP2N1RaPFi7Ro1PYm58H-VwTSSKTdLQmA7qsbStQp6DQKbJ8mJscydKOJEIUQr3q2hU2sUiRRlDuL4J8KdgEC5uylHncDfuYwgORAVsiWI4lm5U4tnICBYUcfe-TqO-vsuHTiNW8be7ebd7-yDMp7haK7kmA_sO-Og60CzMBjQiSqGVOiugSeFh6wAYaqvOwLrOzsToQRiVLhdgbHo-FXw6bujdt03mkNQy8ymZofki1Ok0Zq0jvj8dwj2Plw9Mt26eW75eAkA-o7Zy8NAkXCtzwdoqjkfO4DraQomXIRBWQjxHH5zGTFKSkB3HZv_mobQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e70b182e85.mp4?token=WyzOmefoIQMGnMIQgfSqqP2N1RaPFi7Ro1PYm58H-VwTSSKTdLQmA7qsbStQp6DQKbJ8mJscydKOJEIUQr3q2hU2sUiRRlDuL4J8KdgEC5uylHncDfuYwgORAVsiWI4lm5U4tnICBYUcfe-TqO-vsuHTiNW8be7ebd7-yDMp7haK7kmA_sO-Og60CzMBjQiSqGVOiugSeFh6wAYaqvOwLrOzsToQRiVLhdgbHo-FXw6bujdt03mkNQy8ymZofki1Ok0Zq0jvj8dwj2Plw9Mt26eW75eAkA-o7Zy8NAkXCtzwdoqjkfO4DraQomXIRBWQjxHH5zGTFKSkB3HZv_mobQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زلاتان و تیری هانری هم نتونستن جلو خودشون روبگیرن و تشویق جذاب نروژی‌ها رو انجام دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24472" target="_blank">📅 19:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24470">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GI-HmLSICe4UL4wtfa5SVJGbRsPwQq-hTihGpOmbymJTMwIdQX6GIRsD5M2NIiqfCyQ9Z0-bNnHKdENwG1AEmLlTDmqc7DCHZ8opWnLFuwlnpZ_Ot0d2g57V6bBPi_m1yVYVG9S_Bq7W9QUdLU0xVLY8CuR0CRKk5hyM4w2nBp9EXA1kfGaUXwLDknEulKLOor_LmQTKUjwSnmrZRppdei_vhNpEQc4PPjItHszk-6uAjGTZCvzCo695phbtXlg1mViE1Rm4cHj0psfzVaQRWUBibATSCaTW95Qyld9h69ETdRmTIGGD8fd0jgMV5gwqvIN4bNNOMXgEnt6YokX3Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇺🇸
فدراسیون فوتبال آمریکا در اقدامی جدید به فیفا نامه زده و گفته‌آماده‌ایم که رقابت های جام جهانی 2038 رو به تنهایی در آمریکا برگزار کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24470" target="_blank">📅 17:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24469">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LRRKVD2cyw2V3Kt7Sor02qLy8IDi2_omGrn1GXsNZQRyy0B4XSe9smNpLIb8qD0L7hCO5WpLAPqqZ5cemi9jCnVLz-8pQSe82mApuWUDxCz1MhvD2VGPHE0lG5vcRbt-GYCA0wCGxZMrDeMsgH6dnT6Oq97CyFqGmA63n1NnCYkYx9xJ7Yg_yuRhk06noa2u41SSWIz6W8aImko2MG0AZfBrSlea8xF6umkxPaQ2iug_1iP34d7U0xUPS87WS5lOKY-xK-iSMhFB00aH1TOmSIoxGoQUgtqwZHfFYHNufqbTXB31ShgOeikyW-MHEkzhsFhqdMFgC48Q9rura1LEqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ گابریل پین دستیار فصل گذشته تیم سپاهان از طریق‌نماینده‌رسمی‌اش آمادگی خود را برای عقدقرارداد بااستقلال و اضافه شدن به کادرفنی سهراب‌بختیاری‌زاده اعلام کرده و علی تاجرنیا منتظر پاسخ نهایی سرمربی‌آبی‌ها دراین‌باره است. این مربی ایتالیا از سپاهان…</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/24469" target="_blank">📅 17:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24468">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eTpMjnqPxd39HiPq5rZtsMeWmB_42mwREBStlo9R93Yb0vOr_3Ke8VCRqwHrG2m-cS8N0yjKbdHNBRu9nip8Lz7O5CudnUAiBsODI3pvSQD_KytrlnfH1VPVxRY35Ed5NcIFBYVqu9qCeAuA8B_5gJxx8VsZHndXjmoq-6mCVIwig6JtDFLV3jbJQAcIz7rcQ_LrCkSyYgvn13Akahfq683ka0zb4flPfNdqTmBfEniAOVdA7C7GRjmksisPIz_cYVISkzfpAzqs8h24HzqcXru6S7TNfmKpL5Vd8hcRsZKxmSj4Yi6iN4kQDl3_WBjEke0ozypTADQK7RtIqj9UaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نادیا خمز دخترخانوم پاکو خمز مربی سابق تراکتور در کنار خواهرش؛ بعداز اینکه نادیا گفته بود دوست داره به خاطر رونالدو پرتغال قهرمان جام جهانی بشه رسانه‌های‌اسپانیایی بهش حمله کرده‌بودن‌که‌گفته‌‌من‌‌فقط نظر شخصی خودم رو گفتم و حتی اگ در فینال پرتغال مقابل اسپانیا…</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/24468" target="_blank">📅 16:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24467">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tln7bWuSD_Qh4Jrca2e-tFI_rXqDHvwctQ8ejIXD-BMSX4R1ZLZStBwBk8GV95zYNe6y5nH-iJwA34I26ral6iT8R0Gssdet0F1qSMPX_Jg5RyAT-Zh02EimY6X_z70nkIm1snrrn6aEJHvN0kVoTXg5f5Q1t58KN7Pig9TvIMmL_H5-X_egLG_kLRuWmZ6sPZoTBxvha5XSVxT7iRvzAnnkEAkekDcd1fERkvOBc0HxZhjhLki0jZ7Lq5QG-TSCM2kYYrIqrha1jkXES6AUobm9CCD0-LXPS3-8pOFwsARFV-jO92tOt_be5iIhwhaUP_lxYf6daXhsOKXKJva5KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛ پرز از اشتباهش درباره مارتین اودگارد درست کرد؛ باشگاه رئال مادرید برای انتقال پاز به کومو 60میلیون‌یوروگرفته و یه بندهم تو قرار دادش‌گذاشته که هر وقت نیاز شد با پرداخت مبلغی ناچیز این ستاره آرژانتینی رو به برنابیو برگردونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24467" target="_blank">📅 16:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24466">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFeD71PmCSt_VJsss-G-8ayBmvJ6cdYHKugWCv8O5fCcopc4B1nEhGHkeGo6OkPc5wc_cyGdZQrGpKv1J8YOIGqjJh_GllEhSLi3t9M1LJrcCy3s2oOJLv4DY2Nqk-ym91N_aSAyaZ_MNjTt-Be-uyhByzSC0GLObfxZFkjcsl-lZqhw0Fa3eZABmGXyI6GCMxiiREKHlHnylDxr7VKtUaomkwDb6mROP0P4UcFigZ8ym6y368y_Opg-xeEsi9cE_cEdAegwpMYwwO4XebgYPPb1kpORt7uZjlDnqtf-9jRQQQkNsg3Y4ANPVGAODGwtI6LN4d_nceLpa84Y4kptzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جان سینا اسطوره کشتی کج جهان:
ظرف روز های آینده برای امضای یک قرارداد اسپانسرینگ مهم با همسرم به ایران و شهر زیبای شیراز سفر میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/24466" target="_blank">📅 16:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24465">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dOPWjSvEjuFiv6BJ71pUrWqFp-QVHYgMMbF_OmRM2lah_WkisYk3WyVldXXsPPtilptB6lCSAMvZ8QvYkxPusMnOS0UY8Uz_14oTvIfEs95PzqwULP-LG5WB0w8uI0F9GCfgFWIgskullSY3P3PZBKJF7K1_t8zrYQKfRNubGbRM-JPbp3vcU2wN2GmBdol2pMGHiQ7u2rTwYrf8YQZw7qPpbMnYWdZqEZVQfn8LGZvosHBKIG7PDqhyaZPZgUM4ew1WhsMaCVgvXUhjwpmdSdFw5dOSmHqARG4TyijwS6Z8zp6m73QYHeTIsJA9sJs3yECbF0j38U5L94OOT-CYgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه‌پرسپولیس‌ برای‌دراگان‌اسکوچیچ بلیط گرفته و این‌سرمربی این‌هفته رسما وارد تهران میشه. قرارداد اسکوچیچ با تیم پرسپولیس دو ساله است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/24465" target="_blank">📅 15:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24464">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KDscZUoWL7JXL-wkdlZXRV0A6PlaRVgbpn7ITF2KfS2ueEQ3SNV0GqBzs3bjb36U6u3_q3MA1ZKmeNMcO1y8INAYWAlcpeIB-kmxC9kRT6Tnhdq1JDk0jVnGAcYnza60JSQQbyGKUK2lTeYm1ZVJijXOMsrHM1JuJybhidJu-fWD-Bjz7eyletkyxme6IaGvDiZV8Y9KDOUeZS0yyyzf8Lxc_HAR5lBG-52WByPy6p7DOtBVQTEsPdyr_iQGhbQ8WfPSSTUmAKxurr7cnlU9b21YqcXqHvf6zgca5KHJZG5f8lVN5eHAxfiGL7qBRfR5IPC_v6SwI25ClObhsjoP8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
مهدی طارمی استاد خرابکارب در بازی‌ های بزرگ
: خراب کردن موقعیت مقابل پرتغال در جام جهانی 2018، اخطار گرفتن قبل از دیدار با ژاپن در جام ملت های 2019 و تضعیف‌تیم‌مقابل ژاپن، اخطار گرفتن قبل از دیدار با ژاپن در جام ملت‌های 2019 و تضعیف ایران مقابل ژاپن، خراب‌کردن موقعیت مقابل آمریکا درجام‌جهانی 2022 و عدم‌صعود ایران به دور بعد، گرفتن کارت‌قرمزجلوی‌تیم سوریه و خراب کردن موقعیت ها مقابل قطر در جام ملت های 2023، قرار گرفتن باسن مبارک مهدی طارمی در خط آفساید و مردود شدن گلش مقابل بلژیک در جام جهانی 2026، خراب کردن پنالتی مقابل مصر در جام جهانی 2026 و کشاندن ایران به اما و اگر برای صعود به دور بعد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/24464" target="_blank">📅 15:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24463">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OxxZTmmBb6onJtybKudU2thutiWtf1gw1y7bEKn39RhgkWoTday7gN3jkWjLgpzyDNtZB8XqfRwN0ejTIJlPZEk7Pm6IMLTIV6_zY1wFFSDmNHMIyoDFxb5TFHHljSRFEP1JUamKEb-A2WcTKV-t_goBLFmLoobO2hlR7CP55Pg5tj2Kmgol_sgRWuT19CPg1Ndg3x29CmA8A2U4eoncsNKR_u2SkPrbH5PwrDfGVIzLY2inCs-LZrrh38ub3qJpyTAomDXi7vVKXN1NyA6QUk4Zx6veK0X_oR8WAgTKHn5OvYBBEevorCIKgTxwLnS99VdwtCtSxQIHrKjhncNdog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
#فکت؛ رامین رضاییان36ساله 2 گل در جام جهانی 2026؛ کل اسکواد بارسلونا روی هم 1 گل در جام جهانی 2026؛ تا فکت های بعدی بدرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24463" target="_blank">📅 15:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24462">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30dc88d38c.mp4?token=W_zZcBgzFb_slkri7aItKueaq8VoII1jqEbO7mVlFyb0X64JI5dG84PW0sR3Bjlq_HPw3C4HD9wpMOdLleyjTFsJ6ACuRc8CPLN_0Kz-KCVYEkhDoB2XjCFC5N9dNWk5BNUng26ynquKC3VigPSJg6BCefl8B553Ic5LoJZkuh9Jg-J9jptEozIbyHM9NMsYLbb9Dqk2TjrNpyjfsT64wEW8lKuUJegSPrEENXbrZz0nYkqcWEvBgYvaAwxo_C2qPhLcQrn6H8O6_ioKcvSibv1pZBw8f9HhjejQAmCO_GuHF2TnOCSMBL2qrLOCFCWoKGE-gWER0dUxWiBbvqNIqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30dc88d38c.mp4?token=W_zZcBgzFb_slkri7aItKueaq8VoII1jqEbO7mVlFyb0X64JI5dG84PW0sR3Bjlq_HPw3C4HD9wpMOdLleyjTFsJ6ACuRc8CPLN_0Kz-KCVYEkhDoB2XjCFC5N9dNWk5BNUng26ynquKC3VigPSJg6BCefl8B553Ic5LoJZkuh9Jg-J9jptEozIbyHM9NMsYLbb9Dqk2TjrNpyjfsT64wEW8lKuUJegSPrEENXbrZz0nYkqcWEvBgYvaAwxo_C2qPhLcQrn6H8O6_ioKcvSibv1pZBw8f9HhjejQAmCO_GuHF2TnOCSMBL2qrLOCFCWoKGE-gWER0dUxWiBbvqNIqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
برای‌صعود شاگردان امیرقلعه‌نویی به مرحله بعد باید یکی از این‌اتفاقات رقم بخوره: الجزایر - اتریش: مسابقه برنده داشته‌باشه؛ کنگو - ازبکستان: تساوی یا برد ازبکستان؛ کرواسی - غنا: پیروزی غنا؛ طبق گفته رسانه‌های خارجی ایران85درصدشانس‌صعود داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24462" target="_blank">📅 15:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24461">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/384d776b9f.mp4?token=kqyHfncFPiXjUdr4gbEDP7nlNbLFQnzUEbauRqpM_4dmeaMVmzfyvBueFqpPGS05tIc5QAdfiG38_V9bx94lgU9t1gjIEQdFO29oBuOVM7f4WosvqWMs627KThuX2l_y-wiXD_G8EnKUnjd-73-hpoT1WKYdcyPRbCD9u4V5vzf-v8_gwnLnbtqrq43bXxYlKcoAAiEPzuhLAyRfDEY67psUUv_isz4NS4B6Yg4Nc7JI2bUQ6ZK0q5aJX1t30pznvFuS3xocqJQ7Erqp0Ddj1CrAMWNF9MBb6yE-y46LqYeAawEO4B4jPtZqmwAnp65r1fv6HqqGNGq-Tde_EynC32d8QT0KXqlXQ9TRpbr6LrK25Z9m-JbYmay6M00gabfcOtEMGPWx4R3pBqrV-J_izVdp8V9QPFkNqfWi8b1vmSSSQFtrXYf7R2JadXn0umPIaeyjg0_q_SL303xo5iJmWw7kovILTNZeTd8RK0PkVFiFb5fLlz1tlPFbiYNz5f_EO7Qu548FwKSFUXZ--ZTSP_RQaKCt2Htbb5JfS7P5b6QCQoUK4OM8_amC6HmPItkEbRCw1Qk2E_9b53ux223DxFf-x7tb5b-Hw6fkOlUlqykFSCJeFa7efrRObbIWkL7ClxBKmOvqx250JSsOVBe8qtpdqFRZpb0Xox7YX7NN8Xs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/384d776b9f.mp4?token=kqyHfncFPiXjUdr4gbEDP7nlNbLFQnzUEbauRqpM_4dmeaMVmzfyvBueFqpPGS05tIc5QAdfiG38_V9bx94lgU9t1gjIEQdFO29oBuOVM7f4WosvqWMs627KThuX2l_y-wiXD_G8EnKUnjd-73-hpoT1WKYdcyPRbCD9u4V5vzf-v8_gwnLnbtqrq43bXxYlKcoAAiEPzuhLAyRfDEY67psUUv_isz4NS4B6Yg4Nc7JI2bUQ6ZK0q5aJX1t30pznvFuS3xocqJQ7Erqp0Ddj1CrAMWNF9MBb6yE-y46LqYeAawEO4B4jPtZqmwAnp65r1fv6HqqGNGq-Tde_EynC32d8QT0KXqlXQ9TRpbr6LrK25Z9m-JbYmay6M00gabfcOtEMGPWx4R3pBqrV-J_izVdp8V9QPFkNqfWi8b1vmSSSQFtrXYf7R2JadXn0umPIaeyjg0_q_SL303xo5iJmWw7kovILTNZeTd8RK0PkVFiFb5fLlz1tlPFbiYNz5f_EO7Qu548FwKSFUXZ--ZTSP_RQaKCt2Htbb5JfS7P5b6QCQoUK4OM8_amC6HmPItkEbRCw1Qk2E_9b53ux223DxFf-x7tb5b-Hw6fkOlUlqykFSCJeFa7efrRObbIWkL7ClxBKmOvqx250JSsOVBe8qtpdqFRZpb0Xox7YX7NN8Xs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دعوای دم صبی جواد خیابانی و پژمان راهبر از این صحبت های امیر قلعه نویی شروع شد که گفته خدا باماقهره. جوادخیابانی هم گفت این حرف قلعه نویی چرت و پرت بوده یعنی چه خدا با ما قهره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/24461" target="_blank">📅 14:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24460">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/346c907015.mp4?token=IyadeaK8a4UGIaYBnYFXF3_Rr3ASc-BcK0_UFYvacafC7DDqGgLThieu_1lv8tp475JuGDkh4e3_XnroObt4eBOuX9DeYJUA_ajzJrykeZfvdSv0_mu_UFek05_ELLHTHZeX787CGupVQ8NB7DvOfjYNvX3u7J-3Yisg0BN00F5x8gvsuCpbkVphxH-OsINU-FUmYbEn2E4AuFqFpABLEHSbPqgJguaJ9yXankA-zL2geLBsX_jyYqxEDnRwr5nnVMeMrkpKieUY-8MKp7I7HuS4djiVcBAZOkXTnw1lkHyK7SjaGEN3rgs-vAVs4z9-r-f1tiUCh6N1eYi-M-wuIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/346c907015.mp4?token=IyadeaK8a4UGIaYBnYFXF3_Rr3ASc-BcK0_UFYvacafC7DDqGgLThieu_1lv8tp475JuGDkh4e3_XnroObt4eBOuX9DeYJUA_ajzJrykeZfvdSv0_mu_UFek05_ELLHTHZeX787CGupVQ8NB7DvOfjYNvX3u7J-3Yisg0BN00F5x8gvsuCpbkVphxH-OsINU-FUmYbEn2E4AuFqFpABLEHSbPqgJguaJ9yXankA-zL2geLBsX_jyYqxEDnRwr5nnVMeMrkpKieUY-8MKp7I7HuS4djiVcBAZOkXTnw1lkHyK7SjaGEN3rgs-vAVs4z9-r-f1tiUCh6N1eYi-M-wuIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
مسعود اوزیل هافبک‌ترک‌تبارسابق‌آلمان‌که فراتر از یک هافبک بود، مسعود درتیم‌های وردربرمن، رئال مادريد، آرسنال‌بازی‌کرد‌. اون درقهرمانی آلمان درجام جهانی 2014 هم حضور داشت، اوزیل در خاطراتش میگه وقتی که آلمان میبرد آلمانی بودم ولی وقتی‌که آلمان میباخت یک ترک مهاجر بودم، بهمین دلیل سال 2019 از تیم ملی آلمان خداحافظی کرد و در سال 2023 هم برای همیشه از فوتبال کناری گیری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24460" target="_blank">📅 14:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24459">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bCV082f09aBsG5I8rd7FtiQZX2TLAwTGmegdTCPD3CVDCRBrmFWQ-_KOrFmgTdWg6oHyOfzSJ_zqftfStbdjMTvQE1z5c2iNH1aip_r3Te161NUzzlQKl1xXcxddujJ7Q0W0bGf6BwEsA6WZYGeNDvyTILFuvGcI_FbMQgmz9B8ThUpcp1CAE4nhY-Cya5XFV3bxaDoe5Zsyc0eO3PjYwlWCLbhDw4DC8ur-8EJQMAmUgOpITGA_a0wYtWdZL7-K_w2luyo5s0yPlwDiJcFFhdFmPyUO1VLe_6xM_ixFgPjm301oAlGctBhromk7PY2OwLzQiksPhzCGngDExAL_0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کارلوس‌ کیروش سرمربی تیم‌ملی غنا در گفتگو با اسکای: امیدواریم بتونیم از کرواسی امتیاز بگیریم تا تیم ایران به دور بعدی جام جهانی راه پیدا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24459" target="_blank">📅 14:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24458">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S1H1WkiUnN31G04RIlnddpv3hv7oqDD7xru8KoINt67RLZyl598Jjag0CmfKThiJjG8puMEQYrsuYz-wA7YxN0bBrUevZ0cDJbseoZhs_gFT8v5cEcwXHaDC47ITmsS786zeDsgoUXSxtCLOvKD57Snia5p_Mh0d-GoWfPZnjCEGXCIcIOKzACg7yB5aEVnDd4F_wfADCwqfxoSIkm2XYaOPgh2pg2c-Ddn7XhyMWVpkDNldc_SVFwNxVjF7Zjsd9Udizv-v1HNcUvYFucJUYHGIcqsrFTzOOVKlJzf9loomezvztSUFiJmuv0JC_OlK_8dNKyqHIj47B5iIKd2hvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برونا مندونسا مدل ترنس اعلام‌کرده که تقریباً دو سال رابطه پنهانی با یک بازیکن سابق تیم ملی برزیل داشته و اون‌هم برای رازداری 100 هزار دلار دریافت کرده که البته گفته بدلیل علاقه‌مم بوده این رازداری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24458" target="_blank">📅 14:10 · 06 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
