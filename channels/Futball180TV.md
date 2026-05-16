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
<img src="https://cdn4.telesco.pe/file/e6SUfmbRsK6FLiL26uxdRMksjctixLZ-TpwmiBcllv1cvb9I64aLanncYJDQBy7g8Z6KoTPHsSrA48edWWfF6GB0twoyZvWL1QYtK298uQctL0OsZfnv84zHEz6Py922qHc9iItKJ5dtPsyuf4t_BYNCj6CTG3sT_p66ajh3l5IqR3xx3TnOZ2J0AKMBmW4Yfc4n9aEh7eGhX_GCl-OHMXj_OLl1tsbmqdR43RAsgQ3FqySmpMir7F1-KM_F_yQpXLhqbKrJ_xLZvArFNOpV3a9nvxDdXAPvnvACEHsyzyIfiFmNggJcRoKqtEQrmd_dk3atQTUE2UTHze5O6tiB8w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 135K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-26 11:21:50</div>
<hr>

<div class="tg-post" id="msg-89988">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O-_t0iZwJQrw1l8xTwApiS91ljc-EgiMpKf14iCjF9nKV8wbzy6dTSqTSrJiOaZr-eVmqB_3RTDxHi5Fej3ZbM7MYmYw3q564hYhZXyyAk1feuRjerchOvKBzIWhiXYuNA6oonxbM0jL82WdZg4HMDhllSto0m9F3sKVXN5PgNswtRdtW-d2awOsAReHE6iniT2-1itZOXK7mV_6EQ50P5zP_aA5RlQF_dZGEIMLjTpPRMTEfJIltlpXKRJiwVhmFLHkHkAkR71HO827rgl80FVR8928y8ad5XQmaG6whM9lUvcOhsKzwc_OujDf82pnz5s5Vj3vsYk7BSMAzI0Nlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
وزارت خارجه آمریکا: ونزوئلا 7340 کیلوگرم اورانیوم غنی‌شدهش رو به آمریکا منتقل کرد!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 935 · <a href="https://t.me/Futball180TV/89988" target="_blank">📅 10:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89987">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">فوت پدرم باعث شد از آلمان برگردم/ کخ سخت‌ترین دوره فوتبالم را رقم زد
مهدی پاشازاده، پیشکسوت باشگاه استقلال: در اوج بودم اما به دلیل مصدومیت‌های پیاپی‌ای که داشتم، وقتی خواستم به استقلال برگردم، آقای کُخ گفت که باید تست بدهی و این برایم خیلی سخت بود.
به ترکیب استقلال برگشتم اما دوباره با دو بار پارگی رباط صلیبی لژیونر شدم.
کخ مربی بادانشی بود اما اطرافیانش خوب چیده نشده بودند.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 966 · <a href="https://t.me/Futball180TV/89987" target="_blank">📅 10:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89986">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromADS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mMDPP9Hy37ypglCxUriouskcNthGeVLM0F05acV5kWPZjXUmki9AKM-wGt1mrSQAZG9ywYW_BuuSIYbRqxyEOBlm1c0ZbtcHYo2eRh0DxJ7A6ZxzgYAjvF6gzQTyx73fMFJ9Rno-FMQJgs0Qiz0Cx8M2q20fpPgOXp3ym93slTsMrbQ134ReUpvwVCIwyQ90ri_XR4QusZOJEuXyMAOVVZplVrN_Gk9o_QwffkHCg5cTf7VVWKbFSnvzODcIOsf0IkMVWxuzEq8HaoTlgdnyJJesJ33Z18puOKE0g7u5QRddiLiCtqmxBJsaGQjHFQcVfd3cdPzM1p4Db_GCzPemoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎉
بونوس ویژه ثبت‌نام – ۵۰۰٬۰۰۰ تومان رایگان
💥
با ثبت‌نام در سایت، ۵۰۰٬۰۰۰ تومان بونوس رایگان دریافت کنید و شانس خود را امتحان کنید.
🔥
چگونه کار می‌کند؟
⬅️
ثبت‌نام کنید
⬅️
بونوس ۵۰۰٬۰۰۰ تومانی دریافت کنید
⬅️
شرط‌بندی کنید و بونوس را به موجودی واقعی تبدیل کنید
🔥
وقتشه بازی رو یه جور دیگه ببینی
⚽️
پوشش کامل مسابقات ورزشی
📊
پیش‌بینی با بهترین ضرایب
⚡️
تجربه سریع و حرفه‌ای
😀
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
A24
😀
کانال تلگرام:
🔴
@winro_io
😀
هدیه خود را با ثبت نام در سایت دریافت کنید:
🔴
Winro.io
سایت اصلی در روزهای آینده بازگشایی خواهد شد
✅</div>
<div class="tg-footer">👁️ 791 · <a href="https://t.me/Futball180TV/89986" target="_blank">📅 10:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89985">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIRYHHIe45nhJi0u67jalMAEWgLf1y8jeP3TBoYq7TsFadKjWdoj-mLQkq-rU26JNG7kujcgYVgJH_S2tusMMCmVtHRZNt4KI6hjDmLal-7qUxQI--_qxhq0wCDOPn5Y6Oooil4MJaPDyyd-xuXXU97CH4Dp1s3BShW3XkVoQZxqn7aOLadRqaEM2yNZt5d6kepZFYEvO3NFMpszurp3CFojO9j63vro896UUfDioZhEvslNOROpAOzily3bDhzge8ryzefd0D27bE46RJ45bo0t4Umb2BC4p6JbziYX42lppW6ConM9xCkZAvyRBQmytNteM2Ot4vQB2OSyHciSRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ژوزه‌مورینیو اعلام کرده که پس از پایان دوران حضور در رئال از سرمربیگری خداحافظی می‌کند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/Futball180TV/89985" target="_blank">📅 09:47 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89984">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">💥
🇹🇷
جشن‌ویژه باشگاه گالاتاسرای برای ایکاردی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/Futball180TV/89984" target="_blank">📅 09:19 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89983">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1mvNgCnIcY1yZMNF_sRDiW1iRXZaoP5MHMq7FsIrH9xG0wyyjZnWyDU2zGG34_SGEBAveXR76YYTJigW1C51YGLGWEa04iQZlrbrcQPWzq1fk3xbUmupEnauAFepprWGkjLcQ8yGN_q96CdopgeXveqyJJwtYw1a9Kb5CK0Z94o8wuhTvVrY7a_LmU7F1UI8Pqh26iWRmyR4MKmDhrls-XrxkCjPx5PjTvvIjwy1REUS-_zkIt20dSFgrozW-ouN_JaxCtVlOAlNJ-rvZKeiJ26yzM_CFcjBnRa0QgaeVa1dXlbM0fvwq3NwE3wbwLfA6ltMYHPKu1iL2bht20FhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مایکل‌کریک سرمربی فصل‌آینده تیم فوتبال منچستریونایتد خواهد بود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/Futball180TV/89983" target="_blank">📅 09:03 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89982">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">تو چنل بتمون هرشب داریم به سایتا تجاوز میکنیم
😄
ما هیچ فروش فرمی نداریم و نخواهیم داشت و کاملا رایگان فعالیت میکنیم که کنار هم به سود برسیم
🤑
🤑
🤑
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/Futball180TV/89982" target="_blank">📅 00:46 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89981">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L3rbPzTCLWuNUS6LAa50nXk33XBRkmJBjyYhN-ejDODo3f3QdPNl9cgkfXq9tbi3Bjesi21NOq5lmKxJz7dPrzQ3YT9vFQMDuzN6lPaQGYKMwgDpN4AUV5WCPsBtOkHs5n0-W2gU-nptN1offsIB_llYwgQy30yC2Z3LYxPzkIFR-N1bxodE6lS39GTwVQwaztjDEK4blqjc1DMRTBZVhw2RH5MGrN7aPspEWw-XuIRJWjQwMyPtZqJ3069jxbygo3MHrs1fFPeEMEKdW1UNf73-k3Rlky_WNUS4pSjauE5m5xODUISGttL5uuGkMH6I2-Q0gnj78XEn6kHJyZ1aRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو چنل بتمون هرشب داریم به سایتا تجاوز میکنیم
😄
ما هیچ فروش فرمی نداریم و نخواهیم داشت و کاملا رایگان فعالیت میکنیم که کنار هم به سود برسیم
🤑
🤑
🤑
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/Futball180TV/89981" target="_blank">📅 00:46 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89980">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0zvE3MvuzDzsSiwUr1nDq8qowH6cPNBVkkUMX2sZPZofaycf4U9muLhPOZxrpgKT7sI07wtIBiUe2uA8DI6z3tco7SOJ2HifQv4ejSn-Ni3gEktydOYqSIa9KdpenoUa1A0oLPgSRnlMGgEI-jIIEJCWw2ToV8pULh7IvoB5Czj5zbOsGwC5nj9xDiKDPJiLAdWHTj41dNeQRCUBXIqsIl3sRs4-nSnlCyj382xLHURGSU_42oYy38fIXTRO7X4CwX8qvbYfEF9F-W4VUxOwprsawpHCDUOxt7Q1mzuvg3DIP3KTU_wYtETmb1nu27i49QpT1CrUBv7gT6ZzEIBng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
استون‌ویلا با برتری قاطع مقابل لیورپول سهمیه لیگ‌قهرمانان اروپا را کسب کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/Futball180TV/89980" target="_blank">📅 00:28 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89979">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nD1psfZJwQN6R4bhhgGuBX0Aa1kVUFfsAlh1sGQsXwwj7fY4Ycj6Ry_2a1ThM7YXwLdaJp5h2JGkUUHhkkxm8mTmA6Dgt71Ef-fl4Bbbehr53V4Xnu7oV9VJ8gdtBOPPpUfGBVLIv4TA7zX-sA_AxSUHJit-f4vyTY2zCL0o7XW9m6IU1v9eZdnUnTqk5rw083g-Xnn3cLiIVB-QhxwTy0C9F2xvBxEBqTlAx_IZXnRIJ9HnvWgRoIDFX1CS5cz8C6egE_AdreCy2iLAngotmaktd-OYa7hTONp2PxkydOtUbBTQCD2hnVkKVU5kQFwVr2pxADClidTtNvR9cI95tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری؛ رسانه‌کوپه‌نزدیک به پرز: ژوزه مورینیو با قراردادی سه‌ساله سرمربی رئال‌مادرید شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/Futball180TV/89979" target="_blank">📅 00:17 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89978">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
‼️
سازمان برنامه‌بودجه به دولت جمهوری اسلامی اعلام کرده که با وجود تورم شدید اخیر، منابع لازم برای افزایش رقم کالابرگ را ندارد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/Futball180TV/89978" target="_blank">📅 00:15 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89977">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/erBzVlPbHs3LY4dAlNcZc2rGmjrBNcInyWVNzrGnvMl_aXAFD4Xq-mMx5-RTjpCJ-wKBXUdGluJjBFlvOy8kQJY8d0WFY6yzEcktndR0r9x0f5w1hm1e6A6PaeAAUaKEvJMKkLFBSw1GCvk1s_MdWKoGKEzyD-wu6f3EBXgH_G546sv2c7vq1JvTVFleSne9xfZo6maeDa9R3J9qN0EQyfD1nrVQ0EbhK0hLxvGghL2nZWP99_4N4Lkmo4fQtGkanKkmkF2iwcoIb9M1KgotnehZDggwwLWIAQhpEU29YB-ojd-gitgn-oELHJuFD-3XXD0aAnkZb-yz6IWJBUoecw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇱
تیم‌ملی لهستان از برگزاری دیدار تدارکاتی با تیم فوتبال جمهوری اسلامی انصراف داد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/Futball180TV/89977" target="_blank">📅 00:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89976">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yqx8dYVhTjvs8PoweF00PoYVMh6YXZ-tfRYHygidytEfOHJQl5-UlijsS3TAjTmKxOhlmH_5bJpqKUA-n-ZcvZIVxxShP-WVJGAw_7KkhbZgx8QrxaXK8f2oLmG6bDGZ3kaRpPjIz0SjsPFGqtwTM46_MDY2bFmQqg-PjLOiTix2nUNTJQI2M9ZjfPSfQAqj5yOPCFUGYYSGkbXWTQfmoUHDL8VuO5ltvHfIDCyISiQ6gIVfBMDrDyetGCK-ER5XDn5ktWn5fLyYGvjk5r6wFzCPwV_a8nMpWaaZNJrqbVHQg5wiVFSSKm1RddNGim4D7LDWS2V60R9DpsYZRD4deg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇭🇹
لیست‌تیم‌ملی هائیتی برای جام‌جهانی با حضور داکنز نازون مهاجم تیم‌فوتبال استقلال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/Futball180TV/89976" target="_blank">📅 19:46 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89975">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b58P2_dgi5bWUqC3pTAqK8qJK5sxFbrwvzmjQIPdSOvGFVAlqUfaXjeQ8DT5_4vXCiq7db7TtOLRdGeg_0HK7GwVRvAKDv-4CyB6IDxxOGjBJxJcxXtNuuqK0fL3MAjGZPMIOBXUo_0QM8N2CMqP_Z4KWdfbvKoErcP8L1HvdFsneCXMEVuY_mZ7zAv6qZ06dqurTS5OLSJnUZazWTmEhN07QkLq4GQcD8HRKdDfKjtmuF3Mp7nLWkkz1oh46TgnlvLETm6BQuhHqKR0TahUffdA82dBER3PHPIUqt0jnFBKE8JyRhakj3qvMGALVVIMo5uK9xgy3DD-moYekrK7Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین گلزنان تاریخ جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/Futball180TV/89975" target="_blank">📅 19:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89974">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/89974" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/Futball180TV/89974" target="_blank">📅 19:44 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89973">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GQImf6x62VQfLKrtC6RXRJNWCJO7TBh4Gogfi0SAkGiSudFa0iV9P3A20MGDMv6uAIhC_KOR8kjkQZ9gyCuy9JLk7VtjwLxTF-iZKzKgVC6gbzEi0HZb0tp1ElLY_lKcXbolUwloQJMrBblAB7fiTelXspY32nY0kVcg49K4Nt696USmxEmkytNvij7mjA9eyEP4kvfHanlbM1ym7Dtncyxw5OewV6AixJtSyOquZNzWZ7M8AbAhlIdgufs9aAs6GvOEQRtZCxImhN32Nd8TdqrhJHBkVu2T6JRCbFDEeJQRGgjcZ3e9fCWsYYWK8_vc336OWqENyJNspoXxtVe53A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیش بینی بدون ریسک بر مبارزه
Verhoeven
🥊
Usyk
🔸
اگر پیش‌بینی شما اشتباه باشد، یک کد شرط رایگان تا سقف 100$ دریافت خواهید کرد!
🎁
💥
با پیش‌بینی بدون ریسک در هر حالتی برنده باشید.
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/Futball180TV/89973" target="_blank">📅 19:44 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89972">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0KBBbmODG4ep8rRBUjckGbYEyReFqkpqUz4CX8EZNqqqT8FyrofoaCOxV7-9ecSm1_4nvMoL-rlvXihg8XB3GAsmo2AOavbJDauF8x2pv2DKVkJ6szQI6urt3YaQdqgUJQvuSmHQmTtNs8CHBiTVbmxs9a7Ux8wRAHrbJekjwGNNzaJ_6c49EqvsrxGo543A94u8KJ7vteDKkRk9viwoZfgxnle1_I8V9V-KLA7z9gbZezlGIZrveDKdyb-P81TiCi-PrnUyLuVijY9YPUx2BDpazr--nzYB5xPXp_fepTpJRndXlsxfqeyv39xyP8dIRd3_j-54ROOmnOn2Y7hEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇮
لیست‌تیم‌ملی ساحل‌عاج برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/Futball180TV/89972" target="_blank">📅 17:01 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89971">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZr2Rn0b0H3g_V12p2s6tvSs8jrSz-jWLTlWKkO9rozFVzbiIggbs5PQr0sE7vPPWszjr58jXZB11dOpPjmcHb8AWwKz9sV2bopu7O1KvOkR8NlUPQBQzPTY2whkpuGLCZtZbeZEUU2ZLvNPJB45Vwf13H0V5hMrr_hjKPVEnyrrk1gSetkiGYHcY4xon6twwKt-1U7aov73MgOHAIJHWV4szfnbR-ZSqzfLtLuKD9Y78acImLZq8kT4mpR4oOdse_v3z_cQZsu-T46IL5C9yYORxvU80b4uR3rbR18PL5QSMfcxfBTLnC7QGyAAHnsqri1XVj6-GOhs8YkNV-8iiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇪
اعلام‌ لیست نهایی بلژیک در جام‌جهانی2026
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/Futball180TV/89971" target="_blank">📅 16:51 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89970">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🇺🇸
فوری/ترامپ: من با تعلیق برنامه هسته‌ای ایران به مدت ۲۰ سال مشکلی ندارم اما باید یک تعهد «واقعی» باشد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/Futball180TV/89970" target="_blank">📅 14:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89969">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hs0SJhAhsMnvqz9L8LuvvBgC5ArdEubgLHVIeiNLFRgT3_OD9lAl2VMnEgI3Imz-gT8t9N1zDEVuIi0n9A555TdMqLc56ELGJLfdEKqvPencPKfNEl_QfC6ljnIThhD6hST4mnYjrWSHY8yX5nDnFlR2S3E6V-cpGxYyEUg9jiXzpRNqOUdP2SbDaWxIQOoQ8i-iMB2E7WpNWEEujjOyWsu8BV6_IfEgZxo3DmEWPjJOtc-F0-3zZ5CRu5PLyL2ay_nrDtUU7xRwA-sHnVbrgMKFKClaeS0iFuWZc7RV2M8r6JkfTFK_FD4S1dY3UiejO14o61MSe8n176-6Z2tJ6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نامزدهای بهترین سرمربی فصل پرمیر لیگ
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/Futball180TV/89969" target="_blank">📅 14:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89968">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/89968" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/Futball180TV/89968" target="_blank">📅 14:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89967">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFrwBF1ii2Enn8BlRrWWLu9KYqGdwg4PwDl8U0wyumk82cd_QlAFOL6OR0UkM8lEcBPVgcOEhk0kiU9xSnz3vYjFpjPE5oS5o4z90fJb0BC2fTwv0olkgoZu9UHeN1XCejy--aWPeqavrOv1k_vMokIg8GyyHneI1QiXKf8vpICU9EiKih5Ozk3i6df7_uq2KWoGYScqN_OP5tx0p8Jn1HN8h_cIFBOMgJ4D8iZnjQZ-ix6-RdR5T2ueLbAbH9hgEra-pi44OGfUE33wxbSgg52QPPbudeH4pgS08wR0_sx3fOymFOFF5VzgAhjTAn2dBTlNabw3JDCZXK9mTfJXEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
وان‌ ایکس بت برترین و خفن ترین سایت پیشبینی بین المللی که به کاربران  ایرانی خدمات میدهد
🔥
🎁
با افتتاح حساب در 1XBET از طریق کد هدیه
1x_1566529
تا سقف ۱۳۰ درصد به شما کاربران گرانقدر  بازپرداخت هدیه میدهد
🌐
Link:
bitly.uk/connect1xbet
🌐
Link:
bitly.uk/connect1xbet
🔑
برای ورود به سایت از کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
⬇️
اپلیکیشن وان‌ایکس بت
🔽
🔽</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/Futball180TV/89967" target="_blank">📅 14:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89966">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T49RNihVRvobmbh2ig94Exdg6Mewvq462xaF1II528lPNWRWcuhbApCuZUrv4BTiCdYsmb_5fpquThn4Bohgz74Sex0NaJMElk8KNUllNU9GWcVRxQ1kb8mq0I97SewwHaBYlXky_CnVpm2LB3TIGvaWPwuk6y57cPHAU2hXvTT7rCqPkN286nAPMqzrTyla32WoKoNuf2eWb6mFfYZEkjYAYppM6fIARRm3NNBOPNGbRi38mXXsm5G184NQN6ZKtop8Wv-LwmemMYRE40A9ox24l-E5MP9mGraMYoYJeW3KaU9kas5RcCr-ZoczmGgPiBVL8RoOQPUkhyu3zTPJ8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇺
کوبا اعلام کرد رئیس سازمان سیا به این کشور سفر کرده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/Futball180TV/89966" target="_blank">📅 12:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89965">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oeFVCFgv5yZ6LbcN9n9lABtrpsuExDH0Sj2P-VvpMaE4oNlB_7NWi-ZLkXaf2OGrBmyrZNoBzU5TZ_ecapggkfSoMrLOK1iAVndbMH15lmUrOsFk2Oyg0o6Vh1OWOQQIcvsWdA84RHhjz-ibVI4ddiwWPqVgIUYc7jBI9_OYr64J1c9kxD84HSiu8SEdBDQPFbE2wkzXowS-LKPL0AWNIREeN9BHGvjbxOb0mkm7sEeuI2Jyo5VmD_pzb7WfhPSRi52LFzf8nopjhRy0FErOPgyouDyhIA9DwsLWY3B67gHQZA9NY-JWyzPQYlIuSH8DwUTAFa-YA4EH0KjTDlfa-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇯🇵
فهرست تیم‌ملی ژاپن برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/Futball180TV/89965" target="_blank">📅 11:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89964">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D91uyzfazfoVYRoAcV1zNkxVCJOFZLufvNVppDQETo3VVe-SVPfppMklg3pCIQODVoJYC3Mp4aHXB1JnIlkFGq768uwuKGadMgkuG1gRApwY1wAaaSDB5q0K_fx40ZVmjhft9p_Bs8Hiia9TYbsMiua4O3OgfI-yzechnFoPSPXoh9_ynFE1ciaaSq_QnKGe9I7J-Sx_dPmOnEjRBjybuGJhaqNVRNqbI74KCF3TGxWcHcZmQS6OkdSCNddCVybYH4TkYwIdzdZYYfO9u7LX-7lqN1VnGnesVTqjgrqYF0yAHj2veAnP24YqEYh0wi1vbbCi6ZI2qs5gMJTnEBpOIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
‼️
امباپه: سوت‌های اعتراضی علیه بازیکن مشهوری مثل‌من عادیه. آربلوآ بهم گفته که مهاجم چهارم تیمم هستی درحالی که همیشه آماده بازی کردن بودم!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/Futball180TV/89964" target="_blank">📅 09:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89963">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
وزارت آموزش‌وپرورش: امتحانات پایه‌های هفتم تا دهم با نظر استانداران با توجه به شرایط هر استان به صورت حضوری یا مجازی برگزار خواهد شد
امتحانات پایه‌یازدهم و دوازدهم تا تیرماه برگزار نخواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/Futball180TV/89963" target="_blank">📅 09:28 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89962">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gWhVjFFM9I_erzZSVVkjZFL8B4O-_e02FidC_kLq9h7mKbyVsE1DS7cRK1rxNGG3FGjRoX0yCcOuGLT8l-nWV8Dq2sIBjWID0YxFvpuO1jAtJUkve1PPQyg_SEI3GgsRWFgMoe3EJvcPFPnmjNUcPAY0bXffyzjsZyGaZogC9C9L-qocZHBAnGjTO6wvfOUyIO_01auGFHYGtsXAAuF-UmI3xpli1zg4ELAjDUf0O4mpNWfSsotFmkh379qkYfHM0Q-jhqA4wsrgnilbn4Gb4_K2uE9cb_wAJ799axH0aWXcZsXppHeci9YSH16YTQ2QaM_Br7pbDLMn2FVz-7tTzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بازیکنانی که بیشترین قهرمانی در رقابت‌های لیگ در ۵ لیگ برتر اروپایی را بدست آورده‌اند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/Futball180TV/89962" target="_blank">📅 09:12 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89958">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🇨🇺
دولت‌کوبا با هشدار تمام شدن مخازن سوختی خود اعلام کرد که برق در سراسر این کشور تا مدتی نامشخص قطع خواهد بود و مردم این کشور در آستانه شورش قرار دارند
+کوبا کشوری‌ست که اخیرا ترامپ اعلام کرده بود سقوط سیستم حاکمیت‌ش بزودی رخ خواهد داد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/Futball180TV/89958" target="_blank">📅 23:55 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89957">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6579d2e780.mp4?token=ZXUMr5Uxm8nGgt2yiC0G1KH3i5zUj3CRVe5vf80a5vW5zFaNUi-3sKC6M_9Ylx0BtAu1p5z8pYzzERIYUKJfKOsWaXpZ6wr2gc4fCP6o0wWs1jUA-RTbW-oYhLLCRKnxNK13qfH2FZ6aY30WZ07gwwHpKbBc4CiQqi5byM4fjuXAbrC1iXw0i7UsFherndMknENmvPylcL4acEfmPQJURCSrxHuMtN3BY4VCkdIOwoG9J302OaxHh9iVZwVSUb2LuHK_MD4v7eecRYrdJXC9Q-5ly67Pps1FCWF-eElCGjl1jOvT0FZ5fU_JxUuvpk1-f2u8Nyk5ugGix8e-nzvikSHUgUcb6C7ehJrmkhuapdCmO4T9k3iipCwWQD8HaxIkceVwaiwSh4M5kDiONMG-Is8c4t798L40wdZQZbPKPSUxsqPdKvgoCvmCneXAeusvUboAEdbtPiBMT97bE8GEmPzeGziDOn8cyl2hD9eMt4IQiF2KqO4NCSJHNkmB7qZJKQyiQhHbAJbzJ9cvckLXnNS4cgkn3DVpZe4eFsRMTgJcts3fK8UHLn3u9iwzdPIQSirgRS7JaYi8Akue4qqBAsBQEEthSRhSU4m9L7KyTs8CdY4SV-31cG_OF5RZxzBwo2-7aMc3H71aZKeig8tZWHmGVzm5Jz5Wg-xcKLEkBx0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6579d2e780.mp4?token=ZXUMr5Uxm8nGgt2yiC0G1KH3i5zUj3CRVe5vf80a5vW5zFaNUi-3sKC6M_9Ylx0BtAu1p5z8pYzzERIYUKJfKOsWaXpZ6wr2gc4fCP6o0wWs1jUA-RTbW-oYhLLCRKnxNK13qfH2FZ6aY30WZ07gwwHpKbBc4CiQqi5byM4fjuXAbrC1iXw0i7UsFherndMknENmvPylcL4acEfmPQJURCSrxHuMtN3BY4VCkdIOwoG9J302OaxHh9iVZwVSUb2LuHK_MD4v7eecRYrdJXC9Q-5ly67Pps1FCWF-eElCGjl1jOvT0FZ5fU_JxUuvpk1-f2u8Nyk5ugGix8e-nzvikSHUgUcb6C7ehJrmkhuapdCmO4T9k3iipCwWQD8HaxIkceVwaiwSh4M5kDiONMG-Is8c4t798L40wdZQZbPKPSUxsqPdKvgoCvmCneXAeusvUboAEdbtPiBMT97bE8GEmPzeGziDOn8cyl2hD9eMt4IQiF2KqO4NCSJHNkmB7qZJKQyiQhHbAJbzJ9cvckLXnNS4cgkn3DVpZe4eFsRMTgJcts3fK8UHLn3u9iwzdPIQSirgRS7JaYi8Akue4qqBAsBQEEthSRhSU4m9L7KyTs8CdY4SV-31cG_OF5RZxzBwo2-7aMc3H71aZKeig8tZWHmGVzm5Jz5Wg-xcKLEkBx0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روایت تلخ یک تولیدکننده در نشست ستاد تسهیل منطقه کاشان
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/Futball180TV/89957" target="_blank">📅 23:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89956">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tsfO765LAYheDpaVz25NK7c6UN-EBFuwfm6fEkzglRn4vzMtsi9mUh_0LL4rfqMvKLYHjYoyYO-AyOMBR_aAsW5IYGPPqOUFlWYWWPGS2z_hwVHTAcgv-fWPVudIzXgrgHtkg-aS0oL1cs9c1U0cfiNasBHe7FTR3JnStmSheWXtmm49Wquq8ar97Eah7RF1KlL4N0_p9fw7ZplhbqgAm_MHGKCdCyTbzh99fBfAfkNdBP2FY_TtmGCqhZzIG2q_Si7bQjNLndD8Q3EP5s3pht7m496yucoticfSq2B0cThHW895d3bQM72ZN-laoLoM-sqFhYqqvKcoWMSzOhE7Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇸🇪
فهرست تیم‌ملی سوئد برای جام‌جهانی ۲۰۲۶
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/Futball180TV/89956" target="_blank">📅 23:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89955">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sOq4_JwenglHigV1vNMDF4fVAqWW7GsSHFnkeaBJm1vi_d9P93BGzEGdncUvXdONVkRNOzLOjOQwzMY89pn2DnZ4VnxfhhT6JWixDRE20-qZVqMECL-zA5rUa733hIGgkJjqqKXi_TPQ3wfirygbDe-RCQ5pREbo7JXGBphxQYZRrMObWGBOqETbedFfBLTj2hGC0lfZPYFDCoUkuBrFoKFKsAlWBjabHM-DULAcJKNz87HSaREkCxurEIVbxoknmUYGQm3OgRQEeck8y-jQPCjwsMzk1LIAoQ2Bv9W5IsfKdh5_FK40oDL0gSMCMEL3h9DxFtrI4U5mupTgGeqsXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیست فرانسه برای جام جهانی بدون حضور کاماوینگا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/Futball180TV/89955" target="_blank">📅 23:08 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89954">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7cda28878.mp4?token=H8ua6ghxsMXgqZZa_6UjwPp2IqLF35m2O7ASR5io2eXyQf5_tHrI19i1CArBy80Mzsqxp9TzXXA_goC-Q_z-fPKpdfB2T8vGRJsFiAzmIX7Hb3H1mjO4a8IVJEcUh-2NhCWgKlhl6HATw3oVhIJ0GP42yEanYxsN2RVnU0rTnoxmwwwl-yYM1jjet2MMtbQZXfIPc_512Tq0HOzNCd6Z0Q7GrmtS5XIn2BpSUnTlZnU1LVB-VMRwsLqnkKJgFclsTeqLYBeblxuk0CeXulgXmkjAzl79_qMV83lRyRd0x1oWGC1Fi5BUjJXvgsrcT-DzNs-FTFeo7Znmp34I6RTg2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7cda28878.mp4?token=H8ua6ghxsMXgqZZa_6UjwPp2IqLF35m2O7ASR5io2eXyQf5_tHrI19i1CArBy80Mzsqxp9TzXXA_goC-Q_z-fPKpdfB2T8vGRJsFiAzmIX7Hb3H1mjO4a8IVJEcUh-2NhCWgKlhl6HATw3oVhIJ0GP42yEanYxsN2RVnU0rTnoxmwwwl-yYM1jjet2MMtbQZXfIPc_512Tq0HOzNCd6Z0Q7GrmtS5XIn2BpSUnTlZnU1LVB-VMRwsLqnkKJgFclsTeqLYBeblxuk0CeXulgXmkjAzl79_qMV83lRyRd0x1oWGC1Fi5BUjJXvgsrcT-DzNs-FTFeo7Znmp34I6RTg2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
کاتس وزیر دفاع اسرائیل  :
ماموریت ما کامل نشده است.
ما برای احتمال اینکه ممکن است مجبور به اقدام دوباره شویم - شاید حتی به زودی - آماده‌ایم.
اگر اهداف تأمین نشوند، دوباره اقدام خواهیم کرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/Futball180TV/89954" target="_blank">📅 22:43 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89951">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKUrKao0YUxEvccJly5XyXxFGLqNwNUSP0e3Em_6egxub-cxJEkoNg2q7P_niKvi3kjdjiZDW7ezIGyOQaQUwuJune5QX9so448uNRGPULJ4GEVg_4ThbhlhaUQDW01wUZIg4WqUVmTemybFRLWJqC0MxQoPeD_yUSgfcBzRathT0gF_HD_3tedSKQqgbpsHg39mgoxF4Acpv_7Um9WPbtihFO9seaGomEn_2fwi9JAGSZ7PjiGr20KrRpyOjXiQpwKt9RamGkvdDYWS90DOor7rHljxVVYR2bVKhQiDmH8qcgIeVi1zW5pw9axuLZOAN8w3kXTCgxVfVQxfZhlOaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
قرارداد آنجلوتی با برزیل تا 2030 تمدید شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/Futball180TV/89951" target="_blank">📅 20:01 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89950">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hlD-3fcY5iAZmqSonN0UaVMbkU6BeLaThmCoNxrfvgoq5_HrkWnGLPUnk8UHSGa8SlYESa9LP6u_6O4eWUQSPK8Wr3362vjSCTPA-Rr5KZQO1MzNyM1oiywkLH1lYOqBR_KSDCrNQhjbkEo49pbPi4bBSfZPXTl_Z_LFpSghkp7J6DaQt6VZhg030pFwO7yOSATEQemFaEDstMN1OWi26QoViaXXLjv3Ha8Wte5Gokk9MNX0XYukePYAvDkqP3IsajLjeRybUTU-1FzXpKfn06m6PEoHuPDZwgLbJhLaXHtrUk4A5Hdji2kyN_8SCJ7fOH61hXZm1t2nAtQS2moQUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇴
فهرست‌ابتدایی کلمبیا برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/Futball180TV/89950" target="_blank">📅 19:57 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89949">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🔵
یاسر‌آسانی در گفتگو با مدیران استقلال اعلام کرده که بلافاصله پس از پایان جنگ به ایران برمی‌گردد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/Futball180TV/89949" target="_blank">📅 19:14 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89948">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IS7zFUeEifLrQO4Pt69HwtWMy3GkmndnHvaac6m7Ek3ei5k6uvEBa-jm2VHNQ2Qr7hd3N-DGhCip5--h7qEbGNqN8UGB3DoLo98qjh3sk1lHtJD0hBhGfFYn5aTBsPUnLmvsMoTXh2NPkDN1UH1tLi6MeHNn0mKys8Hj5KB2KG4rlpxoptH1rk7s5kiTPIynV2Mt1_8wSsWURdvRBRZfSC27aOlIuQjMxGvo50qzgWPyMXUGF46joRds3d_AELOv9jNPTj3LzQcAa7pnlHpXa38kiH8RoXlRPURXKqgwFIyD5HpljVyyQ-3bPV_YKOuMGtkvxP6t3j3YXeekBmqskg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ژائو پدرو ستاره تیم فوتبال چلسی هدف‌بعدی نقل‌وانتقالات بارسلونا در صورت عدم جذب آلوارز است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/Futball180TV/89948" target="_blank">📅 19:05 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89947">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/173bf1e753.mp4?token=INs65be6pg5VB3Ji1IWxosSoCQ3B7Uq6OY36Tn7JHq1JrFa1GncRG_CQh97Z_RM_coN-UIq_1PzlIv1qtsnCY_26LZVvfTUdX6JQdLhzr8NEVHPjT0JL8xNApJDj6KkyNGmZlsV-8RJl7gk0q6vqT1V9K8SX1-tT7HcOGRc-HjhHG_jrn-weN8g9EowAwlX6m3wX3z3Qc5ok7izfkvKkSt5tPZFUHe4TWL3zV0q4BwCh1Q5yuDEJa-_0i1nVOun8iCIu378UmhPw4II3J8PChrMue9s5jLlpBMEEnT6e4tn2L1s6sV-Yf62Q-0rRnqa1_BwO06Q_RzBOxsXD4TWrn5Qvj__45T03JVJV5UsyuOQ0EOvsyvACxZmlU_eMPWoMYszqjV1AisBtIOa9Lf4LJHvWAL3RBwfnHDak9_32F89Gcfn2CQx2I7z9pcOICHtf_p3izzir56m0GJoc1jTI-BIt7JRMNCoNgfc1cNHwi_l37vXXfqM4NwHwlzEyn5mF0VLsAuTcDSNmJDXAx1LUgl7dnllUdeKfS1hnRVulxLvMXT9Yfay-_dVxw9tlujmStaf4CRg_1jAO_FhvhuVd8DInIv0R5JqgDddCEKx3xiKp3vBg-j4M8asX3252zhf7dY5wjEPwiQz3fjL6hqnsTxnTaidZatRzyhJMY9dhxQU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/173bf1e753.mp4?token=INs65be6pg5VB3Ji1IWxosSoCQ3B7Uq6OY36Tn7JHq1JrFa1GncRG_CQh97Z_RM_coN-UIq_1PzlIv1qtsnCY_26LZVvfTUdX6JQdLhzr8NEVHPjT0JL8xNApJDj6KkyNGmZlsV-8RJl7gk0q6vqT1V9K8SX1-tT7HcOGRc-HjhHG_jrn-weN8g9EowAwlX6m3wX3z3Qc5ok7izfkvKkSt5tPZFUHe4TWL3zV0q4BwCh1Q5yuDEJa-_0i1nVOun8iCIu378UmhPw4II3J8PChrMue9s5jLlpBMEEnT6e4tn2L1s6sV-Yf62Q-0rRnqa1_BwO06Q_RzBOxsXD4TWrn5Qvj__45T03JVJV5UsyuOQ0EOvsyvACxZmlU_eMPWoMYszqjV1AisBtIOa9Lf4LJHvWAL3RBwfnHDak9_32F89Gcfn2CQx2I7z9pcOICHtf_p3izzir56m0GJoc1jTI-BIt7JRMNCoNgfc1cNHwi_l37vXXfqM4NwHwlzEyn5mF0VLsAuTcDSNmJDXAx1LUgl7dnllUdeKfS1hnRVulxLvMXT9Yfay-_dVxw9tlujmStaf4CRg_1jAO_FhvhuVd8DInIv0R5JqgDddCEKx3xiKp3vBg-j4M8asX3252zhf7dY5wjEPwiQz3fjL6hqnsTxnTaidZatRzyhJMY9dhxQU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ستاره روی لوگو فقط برای قهرمانی آسیاست؛
تاجرنیا: لیگ برگزار نشود، قهرمانی حق استقلال است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/Futball180TV/89947" target="_blank">📅 17:20 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89946">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tinmbfPdc_YkFZjnNwhVV8cRYCChAtPIrTSYB-rZxjzqYzIsgkKCYGGVHMFO31X-iqK54sthzEbA9W1e5PU4p_uLeGZUmf6g8IeIC1Y-0KiFjYfkNDSnhN08Iz1znotNh11ircB3_HFPfJHIAqPeTNPAIupkA36F91eYO538BpEXBAyg6bilNraBoot0_53S4JYMNV65_BidqKWJbAE9Pp-lGYmSYx1JDzShkO59CJ8HLqKr15oin6lhZebKmW4a5hcyEDWrQwNfHkecp4XyXC9SoSADGwaPwe3ygPea4Qsqb6XRbPL6QwONp7DxHfCmf91M1GTD7ZcxzkpE4e1GCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نامزدهای کسب‌عنوان بهترین بازیکن فصل لیگ‌برتر انگلیس
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/Futball180TV/89946" target="_blank">📅 13:44 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89943">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e925e8e321.mp4?token=d29lgliuOFt5wIkKoAT1QjNUjGCn7OOUzc8g66hRMl2GG6YWscmqCfYL5lfCulW5zwxb4Ex-yTx1SbiqwTwESrUckvjtbbUKcQAYll0CXT8ayxOP28jg5Fh-ESlchovfebQBS_kIocypjjc6cDjxZQ5EecSrRpjEO_QVMHgDcLH_1jrO9KcvUy4pQ1FwOpqQz4KtdUbOh4io4SvRi0fwxze9xA1uNcaK_7ncqAPBUz8KqdNe_VSik3lqr8E8EfdW4FEEWOWo3A6iUfyeWYvK_XP7cXgTNNgMKYIgolCJL2a-yu7W8k3h5OBkvgy6jFahdK1WX1tSDt8DajWVVZpS_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e925e8e321.mp4?token=d29lgliuOFt5wIkKoAT1QjNUjGCn7OOUzc8g66hRMl2GG6YWscmqCfYL5lfCulW5zwxb4Ex-yTx1SbiqwTwESrUckvjtbbUKcQAYll0CXT8ayxOP28jg5Fh-ESlchovfebQBS_kIocypjjc6cDjxZQ5EecSrRpjEO_QVMHgDcLH_1jrO9KcvUy4pQ1FwOpqQz4KtdUbOh4io4SvRi0fwxze9xA1uNcaK_7ncqAPBUz8KqdNe_VSik3lqr8E8EfdW4FEEWOWo3A6iUfyeWYvK_XP7cXgTNNgMKYIgolCJL2a-yu7W8k3h5OBkvgy6jFahdK1WX1tSDt8DajWVVZpS_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تاج: AFC چون زمان نداشت با پیشنهاد ایران برای اعلام سهمیه‌ها موافقت نکرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/Futball180TV/89943" target="_blank">📅 12:52 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89942">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pm2cUN_4-209XTMuPTkcsBNUcGQOINDqyihen-LKGxQEvPxSXHMgre_OwrtP7vkNo5maQL0MEmAXa9N1JGy4Vaa9FsQQ71_q7truMDeDL0W_cv6QuUfZZU99DXdlp75IFE1lEtBfVCHlnlyBz5eRC4uavn-jTrTVFSH2zsCmRdyfSzV5z7rTCrtg3sSkaCr_Hyta9rFjBHJndcriEyPa1TNtL695jYwxEZPK55E0a6TqaIt6_e_Pk28UYU9B5F27-VZPiucGxPyprIB0VDQhpNBdVMIEX4xZLR7oRbnHZ7kmpHQNQuFSMV5RMqcyj5Y4YAmyCjyqk259ji7WXyXvWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ژابی‌آلونسو به چلسی
🔜
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/Futball180TV/89942" target="_blank">📅 12:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89941">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pmFfqD5VbnGY4rlJ0Ms-L-XGn74yK6QTx2YrmGK_OtxlUvpU-q5l_ydQM1SmG6tz1453885liFyyacaCHKL0OUYuCCyRBGvnQEZPC8xK4iTcM-rthzuCXew5Zmi0LG3j4B7LmJdkzWv5J_6FETjpEQiAH-DaepPrAomqL7E2ApwhopGsLT6El1tsmfye-_2rTkWFB0r0IBvFsBeWqRGV8oucx0N2QzaNEBMkw_X9ud5ZatWEqH2Fx9kN89K-xK9KT5Ozi_6uGyplP_x0ABMvlrL3iuqr2zmfW1V5R6Iv39G3fD0VNxQviIIIadiBltdrgP3umbb-BTAgdod3ELTMNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
رونمایی از کیت اول فصل‌آینده منچستریونایتد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/Futball180TV/89941" target="_blank">📅 12:11 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89940">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UoVYqkxoLjZq5xFzIo3D5GeGWocxAkZAVKLSnsVRfFlM7COzv72cBzveV9JgVkonuPh4NAXIg5Wn2HZ5P8KIEVmO5zsNyCFTXC2dEWl_4EAYOJMs5tLCcgZfPUREO-c-QP4ORw_jZLWwiKkn_XaLU11BLXc9jWuLmUWBQTnBO4qGy34L_H1M1uHhAVfQzFXgB7UPXFz6ZTJiK0E6HQacWwg0GAcqJTSg0gH_FCIEgEhtaZeMvNp13BP3O8h3-6r0fFUnwr_1mJPDufSS6O5p7EpXCUlHSNXIwrbN0I_L1-2V07FE-4_5yvG-5kixiDRg7l7oxLuhDx5tjXr9Ticrbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
با اعلام فیفا، در بین نیمه بازی فینال جام‌جهانی، شکیرا، مادونا و گروه BTS اجرا خواهند کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/Futball180TV/89940" target="_blank">📅 11:28 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89939">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eHT4A0CIomfriO9wxRV8DKTie4ZzpIL1wPlPysL0y966SMUzFIDbRMAlaNUKgOvWWxnyJti5sKfp4Wvv1XI-lfsIdyO7LBwQBDeBlUL8ZHA4WUWKg_kUAMV2ia8DWHMQkCD8aLOnMqtgFC8hehsFEzo8MmCTIyfq8_3DdpGm3__g_bAQF8nn71Y3a4D2T9ylnAv6Dz0ervCAvb1CoRVqUCBAAAFPqdhe-QrPqH4u1v3qpY2BPO6fyBVOKAGP7GZK0T_JyF8PPq-hP2vKbnAiTeI2v6BvmzXcQcgleY8lj1wHYuuD6QBSyBojf63CL3eqaL1wVq5CNAyXfHPnEG8QGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اعلام لیست نهایی بازیکنان تیم ملی نیوزیلند، یکی از رقبای ایران برای جام جهانی 2026
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/Futball180TV/89939" target="_blank">📅 11:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89938">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fs5oqtX6yE_5e2K-tRFMXWpyIUhISh5byYQJYyx0RnfkFn_JvcBSUdwMgeelvuMuDxJBS_TxiaYO8449sMUhK-27qzAhuB_s7OBphsFRs_H8BtYefuf5yJO5xvGNUt3ErCjPrD8Q2vi5aY4T6tvBvoG-GVxdo3m0JYWD78IkKNslgMEzbE5VpnLPX9cdriOxJmw5PyylmDstQKAPTgBCnY0hppTOBreUL9iHm8KWVIDLjtfWVATGpuMIhPYUn5XpHJhrTTl3whORTRuCMhRy0L2v1d1qahBEpYeATiGhVEVYtjSlCNAeoLb3h7Ym8oqaK4bolGniyMFfvyT-RJ51oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نصرالله معین خبر خواندن سرود برای تیم جمهوری اسلامی را تکذیب کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/Futball180TV/89938" target="_blank">📅 08:58 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89935">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eMKXlScPIQL5Bb6k1q1dlMh0Al3G2YVfAUvClTt9ySzgtJ-Jy8O7yrY5ETOiF6KfUoBfX9l_js6MYzadNeF2UVs2mJ64pR2yfAfWSD4eGxNwgyzL9OygRFaR3kYsJYe4fjtpd-tUTZAUePJqrK2szj7TrjAq44Gw-8AhUXQUm37Nbmtp4VJ-HKInoUn_fHaf6Qlhe6N1bIcyZX8_4-5jK4PWKu5qVbGWLbJUUg2dTgOgbsXQi632he8g2oGEyg0jhkI8sRw4YDL33u_qG1rLApV2Wwcp9WEkaR1ycbfZedPZGTXrWRKvapV07_KLIVGHPgnXWBRCV9ra-lryq9H-Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
🇫🇷
پاری‌سن‌ژرمن قهرمان لیگ‌فرانسه شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/Futball180TV/89935" target="_blank">📅 00:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89934">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olEyXpojBB25ou-zKuWHpDKEVfn9gbKGjCc3sMlQ9mfgS73ir0b_etDt-YeR0hlFdt1OgnLMkXCCTiQTOnBNJkB7uWmWRwGzUBto_rPyfjjxyNlGrdMZ-ADoRHNren2yCK5PEhW5AIVNXYWilsV0hZ1k_soermZHo40lYjbp2o8QkadlesPxBpPEeUKgU5K0J7j6dCSyUBXwk7tuzltj0uxZ203wlt0voDqpkukcX0e9gZa2ZxExeWatDTMrf0jNWe9XRhxf6OtJDTZrTQVrjr-gGkfXI99NJX2s48k6_fbtUBHgXfmNOdZsiw2mwmF3iYdKYorxgrZL6giWCyTzhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇹
اینتر با برتری دو بر صفر مقابل لاتزیو قهرمان کوپا ایتالیا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/Futball180TV/89934" target="_blank">📅 00:30 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89933">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQZeHcCaBCArBh2HQNe0dy4H8VKpMFI7YPC_pL1Mlc8UqU3LOKxHtRXmHF65hlo9z1FKFIdVsWsglGLSgovFHbtG1-x2Nxxl2qPdN47inMQxr0mrYgQjziSg2W7icMGJyoqNk7uxSJWo-nNde_gD4InZLjKwSGlyVB6G66GNQ5RJ0TYaIbxCJPoqeH3ZDWN2S8pZwZIcQYvzGis4rTWIbhrKILfrrB7exCUPp4Jwk3RHsscH-tr7myViK0mPVCH5WL6_eb5KUY8rQkZEH2ZI3fLEPkyb86BGk3QJeA_H0ohDGRuR86_tk5FHW-XeDvBxSwc4d5NWxSezEkqRjyjftw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مایکل اولیسه به نخستین بازیکن بوندسلیگا از زمان جیدون سانچو تبدیل شد که در یک فصل بیش از ۱۵ گل و پاس گل به ثبت رسانده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/Futball180TV/89933" target="_blank">📅 21:29 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89932">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CauOXVif7nwTtMpDhum-bWdVCm2FHTTG7fYvXkNKQnGWV2daVAL-EhrQS1xObNqHBqC29wuKyWgugLgDCfVM_GFusN_n1tUK3d4MxOyZeAkKV_bJbmBPdq6YBRfyudcKWMrVWbq_XG_KCx1_BQrXKctDqyJrAFqgBPvLKVJVPTXLZDUmY4FmExh3kcKEMpdVa3XPsul_z_xusXhFRdakFUg9_4NK4vfnHH4_CB6Fni0zE-zQ66DjeNWmocrDjwpugYsqoXaRe_3aNFVdK1S-B7ol4LI5gTMmLdhqR4eN0Jsfvl1Cx1ROVGUiHnuwrXIvCpgZNdqvGfgoIOI3YtrYqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمار و عملکرد مارکوس رشفورد در بارسلونا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/Futball180TV/89932" target="_blank">📅 20:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89929">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
باشگاه سلانگور قهرمان فوتبال مالزی با ارائه پیشنهادی خواستار جذب یاسر‌آسانی شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/Futball180TV/89929" target="_blank">📅 17:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89928">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JlGRCKrGC4Qr_Z0RWACEq5J6-vGO-fYKF8guV6-x6nwJrmYOA_dVhXEBnJhhIGIwMLITfHaaGznoWvEUPgcRkBLd-vDLm6fKQdkSlkQDt8_-YimMELqJx_uvq0BnWkNpEbglb8bwbTwQoy1x5GlGquys-vQwKxt-E6mRBeZIW6K09R3nvIKOVEXmHjAQeSgMb9pKj9Rw2i9s2BKRiAw_f6wztlza4StDZJgmCMbFmSjgJBJqN_BgXwlJYK6_0bKQUPbmDpQCETzPfhYgAS_qsZow2JUp0WbPJlbvKsioCk9d3IjmMcwH14-K35ZXg0R0mq0eSfJ9w3GJKiLxoHB88w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
اتلتیکومادرید پیشنهاد تمدید قرارداد با افزایش دستمزد به آلوارز ارائه داده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/Futball180TV/89928" target="_blank">📅 15:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89927">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_ZSuKI9Gs0E6CGlc56d7ab5unSJzhgYpjBgkZYAOwmjewLkHkdRqyWjLhbs9TQsxKW4exhh0buxVC83kll5qQyl3bfq021Ou9SezcbvGf9GjWMpPbqiF15IPV89bFd65YnC3F-6RgZbfsPBJXjkTgE-F3hYkxevr8EYWG8Vcf5hwTqbK22MR3zey9PuMY8_dkoc41egn7iyp-fv00zuRULdi96Cq3TuhdqzWarP3VGaxzrP7zC3En8Zrysa1bqv4_2_cCn_UEa36n3uy3NrlSEVI2J-OPKlfNb9bIEZFJTTYxWz4HsAoIXtHnF0WZ0kFxqmj2y3BCOn7qDjPwPIYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
باشگاه بایرن‌مونیخ درحال تکمیل قرارداد با آنتونی گوردون ستاره نیوکاسل برای فصل بعد است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/Futball180TV/89927" target="_blank">📅 13:43 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89926">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f46b010d42.mp4?token=LhmMRNPfsjtWvyUav5TexuRaCs7Tk0zYZiE878eC5RB2xkco6_67tod0BjzQwt3V93ZvQdrAj_fYceSjWKjWSw6WfugVCekGeoisKYUlj6Sy8Mcj_nMEgai4mxkoywrDYzF1BMtuG3VRRiLHICbKiXsk_X2b6C1jT5b9N7OTAfPZHjGdQsQDFu5giB3mLLpgx6HkAgsQuuvV9_SZrIAsQ1CNZ8ECL7id2sMMOG1r7SgvxJkzfDulpjeMmJVHexzOKnHS29jltJ3lCSF8gl4YezTaaWbpf6VxQSJuT4cMqd-2mGDlZUV0YW4msJ_Dse1r6AjsZ2truldrGv9S-CMfOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f46b010d42.mp4?token=LhmMRNPfsjtWvyUav5TexuRaCs7Tk0zYZiE878eC5RB2xkco6_67tod0BjzQwt3V93ZvQdrAj_fYceSjWKjWSw6WfugVCekGeoisKYUlj6Sy8Mcj_nMEgai4mxkoywrDYzF1BMtuG3VRRiLHICbKiXsk_X2b6C1jT5b9N7OTAfPZHjGdQsQDFu5giB3mLLpgx6HkAgsQuuvV9_SZrIAsQ1CNZ8ECL7id2sMMOG1r7SgvxJkzfDulpjeMmJVHexzOKnHS29jltJ3lCSF8gl4YezTaaWbpf6VxQSJuT4cMqd-2mGDlZUV0YW4msJ_Dse1r6AjsZ2truldrGv9S-CMfOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو در ایام‌آتش‌بس درحال بازی فوتبال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/Futball180TV/89926" target="_blank">📅 13:15 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89925">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VncCjyEK7QBFWZ9m2oKF9pD6JeSl3X-TZ1k8YEEfdiPcSCI9Z0JvNOU0UQvfNPXdJQNHDYgAiO9bw10bOoHinlxp1avdyKFi-_zdzbnzNtyY65oYBzpghMYwrz9KU_nb56KsfjtXTdQoOnaAUhXQ1Qt9zhTo93PHv7QIWXq8r0GGOKceFQwmP7NytXiTRAtrAKvoDSsFvFRksHT4BxHllQlyWaZEZnZagIDCtpaS4LfFJd0CS7WtgrW1pAAO4RunMw0ZOH2l0IWpd97KY5lcORQoTHcs3kkioE16ZsqCd62hsvLfu3GVQgKiaIlnJEhTR8oHOY4yuh-HeTRc-QJY1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
برخلاف اخبار منتشر شده، رئال تا این لحظه اقدامی برای جذب رودری نداشته و این بازیکن بزودی قراردادش با منچسترسیتی تمدید می‌شود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/Futball180TV/89925" target="_blank">📅 13:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89924">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d13c-D0MzN62DhSEEFX8-lwqV_kz05M7nBzaqd0Yd_XVyoBuVc5JvlkdoKrlplMTEZy68tAIvcVCGbBbw6fI8OoU9clKwiUoxkqGlfdqeBjr8KEpbWvyMvNuJ9NkKgpBylLsrsXDjM6PCIA0vdkCvPIP2zwjIt9USw7cFy-rH9Mnmfe4tv5wG67HmW0PjPB_em4kL09nkcmHaMBTkgCFDQQNqgrAW-AGGCo3pWTvJYbRynAPYYQ8YMncBlXFNVsRbJ5-0o00AidmPHZ5oE7TcjnRejueJMeei8NuD3AUgpeRpOlbTfJjYZEZehOhMEJkQsOWipQYvn4Q6QtZ4cAhzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
یک خبرنگار مطرح لهستانی در خبری فوری اعلام کرد رابرت لواندوفسکی پایان فصل از بارسا رفتنی است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/Futball180TV/89924" target="_blank">📅 12:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89923">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CailOLHLJEkSKATByio7M_mxccltXKKjPxAuklOQj1KEcyOUDF6NRxJJqIlcTE5mjmzgl4jld8-GXACGcjOOrW-bfHuBzAL8BXAC-QdvgIPAGu_nKeRYZnCqwEbJJ357VTUZonrDSd3quFbrTkpkjr-tS8KnjhlYbZEHKi5Ac_KEttG_7BVhAzZy6J4rOK7AG7hr5DoiOPyFMU_dlYJAzBm3xHGY9ixsbqqDSflv5m06StfM117adxx2s_8eWSJ6aPljoVpBhDh_Gyxz7VxFo59Dg7fc1ICUNzBiC9z3IWPUI1y5fa0hGGT92NNeaVCPCp5Vq_AgwLTQ1C4rCgZVMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
فلوریان پلتنبرگ: قرارداد مانوئل نویر با بایرن‌مونیخ تا ژوئن سال 2027 تمدید شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/Futball180TV/89923" target="_blank">📅 12:11 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89922">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uka5SnHBckDFdMze-FBvinqhehc1xfvZSe_Vqt17I7QoNLn3QaSW6OrWitHHEwKfjY2Pi1lw27jq0GxcJ3HmRezwc8U-72cm3ifKVNxeeJfQ8kjaYgPEPVGYkxjQg1G69_-0zzR8tTtiGrv1WSzlwLCoGlcShTfzGTta_IZU2U2gfhDO6j81_4P07MdM0zsh_iTN2jAnerN7Bct4AbbFD2QhP76n6imTP-hiXTc0Cx1s9z2y7YYNg9F68WMjCKsouuZejHiT2yBznXdmoAvRqN5qUMxQESEpGaUW9ccUpJ_fUiOWNcJvSyZNfht87BRGkigmQcUujQHPqkQr0H_oHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
پاری‌سن‌ژرمن قصد دارد برای جذب فده والورده از رئال‌مادرید اقدام کند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/Futball180TV/89922" target="_blank">📅 12:10 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89921">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IjIYqhGJlz6pw5HcHNeiQMTNkBn_HfdxX7CMIwf8g3m6CXgneQrtXCetPjCdDTBXVnyKWlLYoQM4Jy914_xQ8VQAssp1j1OwhmQK0ePmxbTECzmMxRpBC3spk4r39FBp2WrOQnt82Hf8r9X0UZG7LIxc660bBHW9at8epHxkwdd19PMlfT5OCA3iCyAkHQUKYOe3lElHEyQ5RnyKE4Br7OVVXv_k-rZ22FKQU7_as6-guEPz988PZDBzf57MG54QFHb2bIVD8dXBpiJF2R8lrY4OGsGfiZwHm9mm6HYQ9D9j9gTPv84u4HH60JJXeKCFR4MT4wYWF_-ZZKGVXI7vBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇪
فهرست اولیه تیم ملی بلژیک برای جام جهانی ٢٠٢۶
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/Futball180TV/89921" target="_blank">📅 12:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89920">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ph_yfIj1InFDeVwOkHWNtkmDd7dcrD3pmHZ2Ec7uzAVHg4T6EAqxdboLdYX5UKC1dCpsWig7Mi4JKvHgApuyVjpEiq7ckxO3fukm7WUgyU_FLb6jmkiu4bayXjrk2_zv4JzoSDpsPgMCC9MuQiYux3mbYxUC3J3kFyJGz_AosRr9QsEJWr6QJ9VxQml7i73244uw1U6EYR5xADHOoChEYOIMenLT8xSHm95uB1TnuswYDIcYXrE3bAWLsXu6elo_HztzGrzvP5sthYzzkQL8a_nFmRSQBTnP0ifaHDlspoRKFky5vbACzWBJPibMrflrumho-UlLLEGwjP1UmmI8JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
پی اس جی مذاکره با اتلتیکو برای جذب آلوارز رو شروع کرده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/Futball180TV/89920" target="_blank">📅 12:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89919">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/89919" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/Futball180TV/89919" target="_blank">📅 12:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89918">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OSl5tFr9fwSHqT8pqXa2TAqH8Sn87mBrFYK8gmPwksNXJrLhfNtvNKrIjGh1Ut8b-mSY7YqRPm5YuizjCtBdk9V7xqBWMooGyot2uVBUhkwmretxcrTaLwzkPFAYy0dD_lBRFXUHi_NsSAPQqvQHXpewdhKtb10JNyup8ey15XB5GOE1jraC1fsVe4GNzBiqtUPE2TXm99tyHZn0Ra3_qYYmqo7lEkgx1T7DI-zIyJAAY8M4s0e2X1NxEn3BuIoBP0e6PENdLlUwXZwI5ig-4cB1n2zIM81ymeqpDUm5l24TauvOCnFSImQKizP_XJHixIYQdNSgjJt3W9vlBaSHoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
وان‌ ایکس بت برترین و خفن ترین سایت پیشبینی بین المللی که به کاربران  ایرانی خدمات میدهد
🔥
🎁
با افتتاح حساب در 1XBET از طریق کد هدیه
1x_1566529
تا سقف ۱۳۰ درصد به شما کاربران گرانقدر  بازپرداخت هدیه میدهد
🌐
Link:
bitly.uk/connect1xbet
🌐
Link:
bitly.uk/connect1xbet
🔑
برای ورود به سایت از کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
⬇️
اپلیکیشن وان‌ایکس بت
🔽
🔽</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/Futball180TV/89918" target="_blank">📅 12:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89917">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇮🇶
آمریکا برای جام جهانی به پنج بازیکن تیم ملی عراق ویزا نداده.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/Futball180TV/89917" target="_blank">📅 11:59 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89916">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/745061c8fb.mp4?token=MHA70ebN0tgQLztWQeCuSR6xoTSAgVjxA8kbqiKbeQviQuL9tnnbJy4Ibht78y5Eto5PWFQwJbSmxPZPJdATX64LI9h66oIm-5-Fa7Mqy9QpYKHMucB57uaTsm_mTrnr8xbWJGfQTqG8215XL44FWYPo08SVtm1KgFNwXwrLvEzCK6d262XQCB_eoLo3xCpNxshkYXZSoD4u06BjCkjUObEOa01IZDk1roQ3wy8Fu9j2pXS3jZ5msRvCPwsU3iZYPdvmcHN7ltLt22HnS-FDs2IzAZDp5AEzT7cEerJ4-pdi3X-EMeBuBlxX4hB1nrKutHw1-EffNkjFgPGSI--7zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/745061c8fb.mp4?token=MHA70ebN0tgQLztWQeCuSR6xoTSAgVjxA8kbqiKbeQviQuL9tnnbJy4Ibht78y5Eto5PWFQwJbSmxPZPJdATX64LI9h66oIm-5-Fa7Mqy9QpYKHMucB57uaTsm_mTrnr8xbWJGfQTqG8215XL44FWYPo08SVtm1KgFNwXwrLvEzCK6d262XQCB_eoLo3xCpNxshkYXZSoD4u06BjCkjUObEOa01IZDk1roQ3wy8Fu9j2pXS3jZ5msRvCPwsU3iZYPdvmcHN7ltLt22HnS-FDs2IzAZDp5AEzT7cEerJ4-pdi3X-EMeBuBlxX4hB1nrKutHw1-EffNkjFgPGSI--7zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
درگیری هواداران الهلال روی سکوها در دیدار شب گذشته الهلال مقابل النصر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/Futball180TV/89916" target="_blank">📅 11:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89915">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zfnp6Jy59_uciKI5GfRKYwEUcp5vbRYO6g1vL1vIbiwMjnJoDxLNK-rythD3gMu_-qX8gU3pf41Jk_flGrGLsSU-nNeaobZsiItlL8YtHFJlkBS2l4x0J8Qocpck0c_PbK99hUOrvkd6QFdbDjLE9iDhEw-bDJECXHIU38tImjtN9Huj3KcqMLB7a3Rukz_VulI0yHXbCLZ7e46i_TUZu7S9yXVVoX9ovUxnF_eoO5pXi1cDzPAAq2tKOpZkVA9JtVWF8hjTu_sb_dss2-x8NVqAtWSMR8tmm9DK0uAwgIUsooivfTstfGqGKEODOn7pwlpxsLPOO3FJ3IDDjKMiwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
با برد ۲-۱ مقابل الچه، رئال بتیس موفق شد بعد از حدود ۲۰ سال غیبت، جواز حضور در لیگ قهرمانان اروپا فصل بعد را بگیرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/Futball180TV/89915" target="_blank">📅 09:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89912">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
🚨
حمله پرز به بارسا:
پرونده نیگررا بدترین رسوایی در تاریخ فوتبال است. باورم نمی‌شود که هنوز حل نشده است. داوران همان دوره نیگررا هنوز قضاوت می‌کنند. آنها هنوز بازی‌ها را مدیریت می‌کنند. این غیرقابل باور است. بارسلونا برای خدمات نیگررا به مدت دو دهه پول پرداخت کرده است و این داوران هنوز در دهه سوم قضاوت می‌کنند.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/Futball180TV/89912" target="_blank">📅 19:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89911">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
پرز: رئال‌مادرید مشهورترین باشگاه دنیا است و سایر مسائل خنده داره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/Futball180TV/89911" target="_blank">📅 19:58 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89910">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
پرز: با هیئت‌مدیره فعلی در انتخابات شرکت میکنم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/Futball180TV/89910" target="_blank">📅 19:57 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89909">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
پرز: دوران ریاست من بجز امسال با کسب ۷۶ جام همراه بوده. هرگز فراموش نکنید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/Futball180TV/89909" target="_blank">📅 19:56 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89908">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
پرز: مثل سگ صبح تا شب کار میکنم(جدی)
😂
😂
😂
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/Futball180TV/89908" target="_blank">📅 19:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89907">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
پرز درخواست برگزاری انتخابات رئال مادريد رو سه سال زودتر اعلام کرد
دوره فعلی حضور پرز تا ۲۰۲۹ هست ولی او برای نشون دادن اقتدار خودش امسال انتخابات برگزار میکنه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/Futball180TV/89907" target="_blank">📅 19:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89906">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
پرز: متاسفانه استعفا نخواهم داد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/Futball180TV/89906" target="_blank">📅 19:52 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89905">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
نشست‌خبری مهم پرز رئیس رئال‌مادرید تا دقایقی دیگه برگزار خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/Futball180TV/89905" target="_blank">📅 19:50 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89904">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z4F8UUndlr-DCnHlIgo_wMybbF21s8bpP1Xjg1JcvzQUUqH9wzq85uS6H5HRv1H8WvX6jSlv9fqfoiLD4Tk7DGu08apkDZF7vSIjZSXNEJe-5bnOcI9BYNtVK6AUMa343nZacNQD7iLvNgZL-TgNsT88MKeKoL1_h9q79f1ensv0DkApsgH1kgDWuPpajfuJtQkJZDnc_B2Do1NYM-E_VoxNU9UszbAtgBQNTdzaOYBs7_iZ5tyI3vnMPKmc4_v48T1M0fWP0IINmR-zJ63oEbS5Bl-Z_jk1Yh0hvGOjHE-qLv1tJCHQGmTuZ75PFEqkfb_dDejwYrKfWe5kOt7Mdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نشست‌خبری مهم پرز رئیس رئال‌مادرید تا دقایقی دیگه برگزار خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/Futball180TV/89904" target="_blank">📅 19:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89903">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H8jEjPpDjjReTpB40M9t7NwI0ZnGkXhmMsbgkWas8Eix7Mig-5u4r2BErLZFmeIrvfJnmoP1mXiGYeqh0yTqxxEd7sgswfTy_THycTJTxdZrAVxUlTGGG-lFNnMh35Sf7sMaFsbcENWRFRjcXZfGqnrGil3lz2YfWU0Tny_KEVrXo0v_00d64yKa0aV-SWx62H5Om23whdJec3Td2IXc_379j0KhEMNqir6QcG-9Gd4vzWSfFrUBYF3YKFvmjkQkrN988m4_LWFOXZ98GRb7eoFDaEwd6N92nkcP7ztoYiDkUN_ufmo0tvTURbe6oUwhEzKVot46B7iUXqvgfZluoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
سرخیو راموس باشگاه سویا را خرید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/Futball180TV/89903" target="_blank">📅 14:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89902">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHMZOooVgiucjusVhCguYGNiLA0F1iNehALy01ArHjCQVNCBXOGA-ONc0VQIQXFk1mPpSH5sWBmtLMqIgG0o5j1P_5D28k1U9617LyPrDqi0VxaEmZcZVJunIKpG9FBLozAp44qtEz7B2kYjXStRDJH1rNgdJJlgD55_zKaJFG99-6dGKUl3bKT8u4w6A_coCMYXGJU_CFaqc-bxd5crmqtBdy5JbFcuaneS-0JYVUqiyjUUlhwMkUIaOVg8XiBnWiZaw6F4wjVEvRUCX6bB3clhYXxB77Rw4fGmjAngYJ6WokAovRLHhobS5jx_ftL1FoPbkMvfm4BBDhkJEw98Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇶🇦
لیست اولیه قطر برای جام‌جهانی ۲۰۲۶
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/Futball180TV/89902" target="_blank">📅 13:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89901">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XfWii5-XUJVdespfV5_wND4HyF9FVTOVaul0NQ3dgHdDtDuxtIWaTqQe7X7OeTbIhSVMmB7Zqaw9w0kRq9HRD5n2nrGHkDFNYQ_MQOYPt5CCfJJSyoNGtRL-sJqomnY9PJZ10ddSOLOcoC4p_htMxYa9W5D44PIbGisItNWnVHKPfTm3GdpIb-F2kQIz3SgX6wGuDbCJKXUxi9pcgQeJfSawpYSV7IMXH-SUnWTn6s3tcXRF3fby7nnOAet0ghD184mFpoFFG0eqLGblbh3fMkIAS-Su2VWmITuSsKbWsY1YbtAi0iSU2P0Y1Jd5a0t5QglK3rwR4C-k35PCgjsQYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
پیراهن اول یوونتوس در فصل‌آینده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/Futball180TV/89901" target="_blank">📅 12:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89900">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UEEKtcTpKOSgiEjQaCG1YrOdbXl_Yotp5B6aQ0LhTE3gf7o05r8eFOk0KAjQdKuehHpj66Y1Cx35qmfNu1SMFGGy8kvTnp0QWDT4CIOpRv1nUaKG-EhYe3AUpn-LF9MwRhJ_X1PigwYvkoUHgQRCedPaU9fR-AXAiey5NKUh2IO-r8k9W2OvDq1YSAKh6JeQc474mTaSGL4CwsFsPs6A5x_CMZV6fF1qgWyLx1_Sm9iM7DvpJ4i_Jmf2kQSorKKqJ1G0pMd9rXJ2kSImf3BAJHPDdejF7saPErjj_0xTYKt9gvkvzuOFTbOag1gJl7kJJN9QKCafMNXp2nmIVcC_cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
چلسی‌خواستار هایجک ژابی‌آلونسو برای هدایت تیمش از لیورپول شده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/Futball180TV/89900" target="_blank">📅 12:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89897">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-1TR6O3lTHM-tU6UGVnjHV5eZnEp9QH8QAz9qMc-mD6kuLhoDmDlppD2zA2akVM9ocFzJpbICuTgydSIc60e82TIqO3270mhaZpD4r8AI8JhvoUxUwCWIQnfFPiQ5Qt51016_iOnXUcvi5j4mMm4Tlo-u5DN5ZPS8pCbWychi1nBj3rREo_Tmf3BlT_9V2f1WlG9RqDFSx76Ql-4rbDP3EY9md0oq1CJ7dT4eyWjNNqObtuV0DyU6TfFtTc7YmQxQhEPaL9hxJX0eKk5NUet4sCW7GFfvruuuN2cIZ0mu713I4Ry9dU53ohczba4TrK02kPBW1wsOaiXNb-3jKtug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
چلسی‌خواستار هایجک ژابی‌آلونسو برای هدایت تیمش از لیورپول شده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/Futball180TV/89897" target="_blank">📅 11:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89896">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQvGUO_7nRnr6pxmZdJ9ZIrKhXmzgfladyFkS45cgb4QCyEPPFHxYUkPgJD1Eeqr15UkyjCnlMfCYi43gOQ3TZSOY_aYDkdzG7rZE1_QusYlLwr6H9SYarqLYM2jzhPuqsmMND-S_AIvXaoOkuO1-ltwC8SCW8Te-3dRaeS6zyZp8uLZS1PtfgcBT5CdYTB0Bo7qi_UD0su250CGaTNc8JTt3S0bKVm9KtlYD3l9AbkHgp2sPXXGA1MARFP7kCBDZjUBKOVOvfqjHxbq3-Pi0xYSL39GK3NgMqBoRV3p-bSHVxJx9dIkH1rnL8osVAf9p7IkDHJydQWb21i2ODSh8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رسانه‌های اسپانیا: امباپه خواستار فروش والورده توسط رئال‌مادرید شده است هرچند وینیسیوس و بلینگهام شدیدا مخالفت کرده‌اند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/Futball180TV/89896" target="_blank">📅 11:30 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89895">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h0WEsOJiuLPLk2FIVO3VJwfAedQQ-8gQgq4U2xfH8hbikb67RGSyQ166brvUgFGAkmv5OjmLi0-l-2AorsFbl58UajdgomtWsJb_9YFdr4po5N4sooFCk0yuRO8CVsTVhg4LQu17I4NC7dKEAfnqjBdQ612gy0KFgjaQ6JZEp58Yg507D3dtDY_dAzBg3ER5tCdFaOd6tZIC9nYUCMFxUNHDA6SvSnM5-yL3K2yiitd6_uGMiUqc3jmxKm0yUuxmharBCRIaufEzyPPNNJ8DgoqypGL7rpNY__zoFOslaYmUAFkJHepkRGiLF3PSA5tIflD_MlwTV49uWL4Ggs0B3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نبرد حساس قهرمانی لیگ‌عربستان
🔵
الهلال - النصر
🟡
🔥
امشب ساعت ۲۱:۳۰
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/Futball180TV/89895" target="_blank">📅 09:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89894">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34d894a4bd.mp4?token=CEhKhOb2uH5s2yZAY9_GfK_Sv4V5cz2gl8m32cTAKpHWlU3EYFzSJXimcJScFLvZUfiqZC2sea4DObxiM1M1CWSdkQuuTJ74AaJiq8ewwh4NYKDM5YBaMD6tRcNc3mrjWB7w67jtSzNW5M4HhsWhmofukNSSl8NnUWkiy33pZ9Ic60bR7WDnuDmnysmFREOdyM-BDVUeY_OKCOlFP7cGN_M-7VpvuXYcXVmQRZm94CssHuKCBfqOzRekUF6Ldhi17Vx4eBIKkb1jv-tgVM1GgDfI0pROSmUKCEk8OpmD1G-DzCNBItDZ8p2kBdWTLNhsMUq5QY8apb2aqi_Ar5_EoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34d894a4bd.mp4?token=CEhKhOb2uH5s2yZAY9_GfK_Sv4V5cz2gl8m32cTAKpHWlU3EYFzSJXimcJScFLvZUfiqZC2sea4DObxiM1M1CWSdkQuuTJ74AaJiq8ewwh4NYKDM5YBaMD6tRcNc3mrjWB7w67jtSzNW5M4HhsWhmofukNSSl8NnUWkiy33pZ9Ic60bR7WDnuDmnysmFREOdyM-BDVUeY_OKCOlFP7cGN_M-7VpvuXYcXVmQRZm94CssHuKCBfqOzRekUF6Ldhi17Vx4eBIKkb1jv-tgVM1GgDfI0pROSmUKCEk8OpmD1G-DzCNBItDZ8p2kBdWTLNhsMUq5QY8apb2aqi_Ar5_EoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
گلزنی محمد قربانی برای الوحده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/Futball180TV/89894" target="_blank">📅 09:16 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89890">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b91a57e968.mp4?token=p6SZ65AAV8ktLJawzSQI4nbziYtrkubANZUAodMXHZU3VxObHu0QO9KzJ7l-coxS0iC8llGDrSHUs1eTxHp3KGMPbvTYXinEFsGw3acSwWBcROdp-RV1S1zrhIbfcZTjiGqGbXb45Z5HBaWVWs9zAJhyklV3YXTt_NsKbexjkbExwWLg2R21hTVFAYXhTrxPDo4-UnNKKszNgagElUIgwxK2QmGsXEk-52F2nJlXGFpQu4BPyuKisEihGFGWg0u81w2UH6R_SZchVU98n0JG5JwmJTrlRLNgksglLm4uAAhGCxn56l567yZuquJB_NishZoYKcB2Du3KrHGG8PVpFLzbSOZ9yiZkNtO1PPPlKPAeLIInfEUhZW_dwJHymSkO4zW5CU9TqQq6t60vzTcN9nth8y9_SmoCdC0lK0SG7HmtLQ2mXwGLGvZk-h41pIAnMGl94PnA10Bt6nBQ8A01QyNixGkCFG8EEddTgt8HzVSGbvW7Lin0qP3zTiKk7LcL8ogw4xQ7Eeq5iI0fhq6ed5lkmze1fs62iXrwN3ecwan5DbE03hylthSW-Y26dMzqrOWpwf4ZMLFy9xYVtlB8Ual4jQDv16XIE0pA6e2LBRKEp5oIQQw8Y9B7WhtzR80OI5qmHHdI7YXUF-1y0ZWAx6e6Rf4xXpVf0md5n4PURs0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b91a57e968.mp4?token=p6SZ65AAV8ktLJawzSQI4nbziYtrkubANZUAodMXHZU3VxObHu0QO9KzJ7l-coxS0iC8llGDrSHUs1eTxHp3KGMPbvTYXinEFsGw3acSwWBcROdp-RV1S1zrhIbfcZTjiGqGbXb45Z5HBaWVWs9zAJhyklV3YXTt_NsKbexjkbExwWLg2R21hTVFAYXhTrxPDo4-UnNKKszNgagElUIgwxK2QmGsXEk-52F2nJlXGFpQu4BPyuKisEihGFGWg0u81w2UH6R_SZchVU98n0JG5JwmJTrlRLNgksglLm4uAAhGCxn56l567yZuquJB_NishZoYKcB2Du3KrHGG8PVpFLzbSOZ9yiZkNtO1PPPlKPAeLIInfEUhZW_dwJHymSkO4zW5CU9TqQq6t60vzTcN9nth8y9_SmoCdC0lK0SG7HmtLQ2mXwGLGvZk-h41pIAnMGl94PnA10Bt6nBQ8A01QyNixGkCFG8EEddTgt8HzVSGbvW7Lin0qP3zTiKk7LcL8ogw4xQ7Eeq5iI0fhq6ed5lkmze1fs62iXrwN3ecwan5DbE03hylthSW-Y26dMzqrOWpwf4ZMLFy9xYVtlB8Ual4jQDv16XIE0pA6e2LBRKEp5oIQQw8Y9B7WhtzR80OI5qmHHdI7YXUF-1y0ZWAx6e6Rf4xXpVf0md5n4PURs0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
درخواست صالح حردانی از مسئولان برای معافیت خدمت سربازی ملی پوشان فوتبال ایران
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/Futball180TV/89890" target="_blank">📅 00:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89889">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf3c6bcff1.mp4?token=f8Uuf1loeKiWJnhrj6y0YBfuyEiFzQ8ci793Qp1AQeyv_LAHYv9yRrbKy2yKgmgsrfW3ZZQmHkNj_lzx8XBGGg81vbeJYFlDiMwPPbeiTO32L4NhIgI2wwODMvu5RmCOz7ADaHX9mAaRnhC7-Rm-f0SJKp-g2MRd5kFVFv4Hki4A20nEgiir4KL7eBetd7Nlk5mfth1SniXiyBZgKgT-agPYix-m-Ue7wX8tvZWL6BTOwPKz1DKJkx64caR7uU-eH6gUlNaoKCRJLZaN627QNBDskDxVQH7kT8gRqsUxu8HWhex8DPIatm4ki3cx-PnBipE1PugbfEjVVJnZ-1hTWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf3c6bcff1.mp4?token=f8Uuf1loeKiWJnhrj6y0YBfuyEiFzQ8ci793Qp1AQeyv_LAHYv9yRrbKy2yKgmgsrfW3ZZQmHkNj_lzx8XBGGg81vbeJYFlDiMwPPbeiTO32L4NhIgI2wwODMvu5RmCOz7ADaHX9mAaRnhC7-Rm-f0SJKp-g2MRd5kFVFv4Hki4A20nEgiir4KL7eBetd7Nlk5mfth1SniXiyBZgKgT-agPYix-m-Ue7wX8tvZWL6BTOwPKz1DKJkx64caR7uU-eH6gUlNaoKCRJLZaN627QNBDskDxVQH7kT8gRqsUxu8HWhex8DPIatm4ki3cx-PnBipE1PugbfEjVVJnZ-1hTWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لامین یامال در جریان جشن قهرمانی بارسا در لالیگای اسپانیا، با در دست داشتن پرچم فلسطین حضور یافت.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/Futball180TV/89889" target="_blank">📅 22:50 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89887">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/381c992189.mp4?token=ZQkz7ejHxnOtsdLwnDFlSqNHSS9rYHIGb1R4yIcImGWVvHWYlrQpVYzasrnaX6WqVqfN9lwqZKArebiNvNFKS38zOe--jvgqa3k1N8F3gPjF9ooI6LzrFd7oVqdjaaBkuKPTi0ntCA4yD6iMQZR1VTlDz9Pw6KWYcNku4NFJY0QI-Y_T4KVCssrLIUuL5uCz2Keg1QN_KpfoofODxJuIzQc1F31be2Sq5EVvO5wEPeHVtsSdU0H4wJYYsghu5j7i04jDzg1NgzuLiosSYQHG7H_DQ_iXyhT8kyxU29ZtAWp-ueK8K9Gzu5cH7b3w9ljAzda-7uE2gNZBBZmg6TLRMBdRSIAogmVsRD_XDF5nPaZxgSYTfnAcIa6OEYqqYFu_lRRarATkPtMFqTA4AfoFns5KGqQmoyL7e_kRtTgNt3hzvzx7JVJzkFjejH9PKBRUF8i3yGxTuuo8JJBRpiox-6I4Jnn8Qj8SYsYmP1XUhyyGkZToA6JX2FGkw3OFtKho5wPhlWo01kVbkm1H3NWTJMioc6tL3IHGsirJ8fLEjGBjBDR4v7Ixe-Ar4huGXhuipd84RbNJ1IN8uchsVbXDH41YNDjIFg-XdkhmqzDKJcHsb_kei3C965NmrOzE9EIQoqWOXBKXx6vX8TifroWaUdLJ0tgnoIFe2iuEnZCNo7U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/381c992189.mp4?token=ZQkz7ejHxnOtsdLwnDFlSqNHSS9rYHIGb1R4yIcImGWVvHWYlrQpVYzasrnaX6WqVqfN9lwqZKArebiNvNFKS38zOe--jvgqa3k1N8F3gPjF9ooI6LzrFd7oVqdjaaBkuKPTi0ntCA4yD6iMQZR1VTlDz9Pw6KWYcNku4NFJY0QI-Y_T4KVCssrLIUuL5uCz2Keg1QN_KpfoofODxJuIzQc1F31be2Sq5EVvO5wEPeHVtsSdU0H4wJYYsghu5j7i04jDzg1NgzuLiosSYQHG7H_DQ_iXyhT8kyxU29ZtAWp-ueK8K9Gzu5cH7b3w9ljAzda-7uE2gNZBBZmg6TLRMBdRSIAogmVsRD_XDF5nPaZxgSYTfnAcIa6OEYqqYFu_lRRarATkPtMFqTA4AfoFns5KGqQmoyL7e_kRtTgNt3hzvzx7JVJzkFjejH9PKBRUF8i3yGxTuuo8JJBRpiox-6I4Jnn8Qj8SYsYmP1XUhyyGkZToA6JX2FGkw3OFtKho5wPhlWo01kVbkm1H3NWTJMioc6tL3IHGsirJ8fLEjGBjBDR4v7Ixe-Ar4huGXhuipd84RbNJ1IN8uchsVbXDH41YNDjIFg-XdkhmqzDKJcHsb_kei3C965NmrOzE9EIQoqWOXBKXx6vX8TifroWaUdLJ0tgnoIFe2iuEnZCNo7U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ: من از کردهایی که به آنها سلاح دادیم تا آن را در داخل ایران تحویل دهند اما آن را نگه داشتند، بسیار ناامید شده‌ام.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/Futball180TV/89887" target="_blank">📅 19:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89886">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/754e02ec47.mp4?token=KKV6WGsB1KAU6Dn1K6Zj6pMr7ZQPSCSepUZ9W0Xa1aLuPs9ZYkybtl_AGpvbpuUGuw_t2HH1aJIP3IDcap6-feYaJYEEqlKaQXiof7XCcIRNRPO5Kyfcxlc2ccgMJxWniajNNwza25bmlSBeO6yguMZ5sTEHgU2lCXiIoYX1am0aXZctC2C2_tWQ3B6uxCTPaxfFUhXyc7pypjKG6qMKf_V3r31zDWzDlisFb20080W8uL7_mnvr6gxU9ROn8g0Kdc_ns_dCGmQ-OvrLKs3kxB6fd9nc488D5omS3dZNXMhC30q0wAHfzznsd36suIPvUhM9LnW8pgFiCrFEexPw4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/754e02ec47.mp4?token=KKV6WGsB1KAU6Dn1K6Zj6pMr7ZQPSCSepUZ9W0Xa1aLuPs9ZYkybtl_AGpvbpuUGuw_t2HH1aJIP3IDcap6-feYaJYEEqlKaQXiof7XCcIRNRPO5Kyfcxlc2ccgMJxWniajNNwza25bmlSBeO6yguMZ5sTEHgU2lCXiIoYX1am0aXZctC2C2_tWQ3B6uxCTPaxfFUhXyc7pypjKG6qMKf_V3r31zDWzDlisFb20080W8uL7_mnvr6gxU9ROn8g0Kdc_ns_dCGmQ-OvrLKs3kxB6fd9nc488D5omS3dZNXMhC30q0wAHfzznsd36suIPvUhM9LnW8pgFiCrFEexPw4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😄
🚬
شزنی‌همین الان وسط جشن قهرمانی بارسا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/Futball180TV/89886" target="_blank">📅 19:13 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89885">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B017ggGCtF-ql0VWi44BAuFEUAhXm0etqCiaHTZkYCDydzHs9M-NWAgJwcijqmfYaqoNsAM2oQDrftPZWnCGr-kd05WlJZJ5mwLUcnbbHdHnvUs8HmTiP9ALlzkoVqQ8Z3W5L-gpXnKHLJo_yHYx8Lv-8oB_39K1EuxZV1qhKWMUX8C8XDgJA_Y3Iy7tMXc5zX3ZhrMGthXJXQqqeobWclq9SuWBArIfPudnvcx1O3PJhoT8hQqzI3wrKvgm6ZdlQ7VIMWFaU7y5QkPc0Ez4Lo5w7oCFjsym2K_NI9Sy4oS726EYHsBR-oHFGzAluppOmiE8pF_JmlJMAOD4nuyRuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
ایدول‌خبرنگار مطرح آرژانتینی: لوئیز انریکه سرمربی پاری‌سن‌ژرمن خواستار جذب آلوارز ستاره اتلتیکومادرید شده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/Futball180TV/89885" target="_blank">📅 19:10 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89884">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AqQadOLtv7x1HAnEcmWps7yqvtLLlZ6DCs6DKDWbxBzQFC17Mwd_SFquZrSQ7hyHyQVn_UJkwX8wMUFuAUbZl5VyqCCBETW7dXMeYLlrr9JALAJu7Oapz7LBX9z6MsQaIm1sT9DsomfCWQu6g9cukahcBuvTDa01RSouoOMayCBXxq-bZ1S-2jV-ffLl_B29HQZ-llzFI5rCBR2Odt58bONWuqLbIEW7M0mJKaOSyfSEy2_eGKw2wThckMci-BHH8helosL3YhRrf_YC0hpWOf6SBsc2Gohfo3lI6XSMFwJXpeaPFkrQ8g1uAIXYoBLq4jAr2CCa56NlS9fLI7IUQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
🇧🇷
لیست‌ابتدایی تیم‌ملی برزیل برای جام‌جهانی با حضور نیمار ستاره این‌کشور
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/Futball180TV/89884" target="_blank">📅 17:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89883">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sB8T29iY-N5mcqLclYuU_ja8OivpIwc---euK3Km-AYUTjgdrOInfg2dHaj0ONtW-oyUrizEFAEFtB4KhEfpmoaYt5yja2Ao1CgE0wTVWqCv-lYJPH4ZrcIxZIQkDeZwA9NSZbmG88uX2qLr0_T_pa-aQr-tOg4nZSPXgR6V-aSUiyLzjo98XOJTKWz1wb3RthahmSN8G1albCgO0NaZ4yT2uJqEF1pODELUdxiynYkHU3urIdH8UH7mHJGyNPGJZtEy7xN2SUkuX-kWfcUPPEHrw_aCqeGRPf7Rqj3UIuvxWIsiMnx6JyNBt2weNB3EmBnRBzXfD3ZxrLSTqv_ncg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
👀
انریکه سرمربی پاریس: باید بگویم که به احتمال 99,99%  قهرمان اروپا خواهیم شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/Futball180TV/89883" target="_blank">📅 17:35 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89882">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yv11Hj8eziA1-8fbVGPVkChJUG6oY2DVF4qilOojx8GqZS7AvjX1x3dWz7W6Tpr2MezSvFk1SfPT7_cO3DS5m7D_3wmP7qJ8zzl5qHdK5-JYu5n9XVm4lYQoH1MC2eukeaIF8LMWFpxXzSomtukuEFQAcpqNy2NLf3ZztWxgNpw4BX4xwNUZIDc2diu7HyZP5fo4FujfiwAb1dBcobQHTDfOb1-RClT0P5DBWxrcALSQJgJ9rLpbpafHkGp39nPP5YrOf4fm9m14tdd7gBUJLiGCA8-7hCVhUozJZOieIXuFkD77o9cBJV4TJYmLN4bbS0kquL6Bhbf2-wAOa9Cj0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👋🏻
خامس‌رودریگز اعلام کرد که پس از جام‌جهانی از میادین فوتبال خداحافظی خواهد کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/Futball180TV/89882" target="_blank">📅 16:43 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89881">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cM1dRoN5kbWE1QzErPud8-lYbM97IEnmr4_MBi26XJZh1qDgF64zj23I6VSaimQaWR_YQIJmuzwQ7Po8E_0kZ5MP5DSSO8cmgqxTP7Eo1sQ7nRa_sgybDWO4rCDS0Wq9ndq8Q8yXDmfRAGbOmWGy3e2SyYU_njLDvzlSaxmhvIG5ECQNT7vD5yJs-4lW1zZt-wS_wJ0zy2CeevPeZ_ad4ZYspwfarjJQuYasVXsElxgAcDmtFmx4AoL8zq6Y67tC49pmH1nrStw5_GPtWC09sk2JbE4JWlmezDS4hmMc4v-h6sjbbJkXEsCakirtG06ZVzit2bVSiCnt_Eh861Njdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
دنیل‌زیبرت آلمانی داور فینال UCL شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/Futball180TV/89881" target="_blank">📅 16:41 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89880">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mEza_QjNiJfa75oOMl8BH3FrYhRsc-CcSMcr3_X3QPflpA-TH4RQngkwKsHZ5iZkw_kRvwI1qJ1SWkbHeaw1wnEbyh-LCqwblwwk8aji0b7o3makWQJlLP4dPMxwht0ENodBOdcMZPk3kmGLq1FBtns1L_zHK7U9Hg49CwJscU_9qjcVC8jc2jADcW1cjqedUj6T0KK4_YdQ64kpSG1HA6OsXJUIpjc4CPy-QMzIKFnX-Pv-fSzKrZdPLs-fB0k9JTcVcaGVreWhoLhLAdpYH36O5Rf93_Y9I_13HwnDFV7YrMNUAMdMldDB99rv2gR2DNHZZJro2lAqOraJvemYPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
فهرست ابتدایی آرژانتین برای جام‌جهانی، دیبالا رسما از لیست خط خورد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/Futball180TV/89880" target="_blank">📅 16:39 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89879">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Frfs3DUR_C9GHJzVKpq305ZnKUcdkV48b4T6osQhY7q8KgxAAYwijxMIgxw4V2QWFG3zflHoaGQ8g5YZN5kGxpmrYi-BG4LyMadk3XlQvLeGOZu0p-pFg1U5coEwCaZndWlBQ4jiv2VSrZB2NvD0wIJheEeKEUnU-ouTwy7c9b11xOhqEIJX9xBX6XeaUI-4v5-jhap5lO1QqF4vuXJ0THj7D5j4FrAPN4v6Dcm4rQbui4wxJT7hVegUNlmtRkOuM5uz1eezRM9LazXJVLDkGAiX1Eymn4g5jx-k0x_kjJzxZ4hB-TzEEC62pn8jIZ5w69LWiQlLVQXTA7JAAfiETQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💼
یک ماه تا شروع جام جهانی 2026
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/Futball180TV/89879" target="_blank">📅 13:59 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89878">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
⚽️
در آستانه جام‌جهانی، یک شهروند آمریکایی به ویروس هانتا مبتلا شده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/Futball180TV/89878" target="_blank">📅 13:35 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89877">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
کنفدراسیون فوتبال آسیا درخواست ایران برای تعویق در اعلام نمایندگان آسیایی را رد کرد و بدین‌ترتیب احتمال بسیار زیاد سه تیم استقلال، تراکتور و سپاهان نمایندگان ایران در فصل بعدی رقابت‌های آسیایی خواهند بود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/Futball180TV/89877" target="_blank">📅 13:20 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89876">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUcWbpIehlqDU14sljux79GcFmhGEltVedMkEpIvyOgmpU1tcrzuON_TH_4oO_RcD-kOmyBQRmDYqQWeS5EbVWAJyfxrGNx9fh3X2Ks3MHke6tR6eEj-3IPB3TAvStdB7j-fyRjYhwspUO_Y89dMNy15tnROxmakisIwjK8M-pWHO1PDM4lOVyQ8HBdYTFxtDro_drZeac5Y_FygYsN0UG8vCQPV4EQ_gycv60GxzvKCQLt1B_-jcoPZH31rEYYCPEshI1xN5IOZ4d9pgQspJ4-6A2NH13vdOhBfyW839VZbGLYjZp2W_igokk8AavehSkc-S68dKJxfXRH7rEk5oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری
؛ رسانه‌کوپه‌نزدیک به پرز: ژوزه مورینیو با قراردادی سه‌ساله سرمربی رئال‌مادرید شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/Futball180TV/89876" target="_blank">📅 12:07 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89875">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rzB_t-dADIXHsnQYKk5fTUptP8GPolvYX_gcYtqbzbfwqd7D8eNiC5DGsZnTqx1_rZXILwp2LN0xsDx6HKtwTmFWbL398Qd668W1MpjjrLR4Hf_0Njk3H3CgC3vemCMezfg7sbQKZ0BWdRbJUQeFNUPZxZeAmizTwEV_qWUlR9dtSJn1pQDLG8dklZcLq635JN2K-e7FbTTM5hW-xyrk6_EKl7ppm12vtNlgWaOhfasBOr3R8EOuauJaLF3Mhp4mhajszZyqwz3uMPOXzFA872OKngTgQBcrWslmwfOrTg9aS4xkPgeLxr_7TdZesFsn55q4Ae9fa1WumbBF8zqOWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
✔️
نیمه‌نهایی سوپرکاپ اسپانیا ۲۰۲۶/۲۷
🇪🇸
بارسلونا X اتلتیکومادرید
🇪🇸
🇪🇸
رئال‌مادرید X رئال‌ سوسیه‌داد
🇪🇸
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/Futball180TV/89875" target="_blank">📅 09:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89874">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rV0zfGq1pXrBU5c5vyZjYqekAT3IZQgNQaM8iVrhmANq0uNLPvp2XbnAv8D1nR-HKHlRIGwF8OhllJxHwbQgH8R9LnM74zRYnWYTRbtLdxTMOE37NOM6Tf7-BqbWy3Kehaouy39npKIf8XSCfyvHT1NqKnK-aK9HVS-pMeuQdyS_bvCSVUfTqwD9oZ2QHZtgsi6tfRh02n9Pr-bchT-8t5jzToGKvUFfJo31UpcANbtVgpr0GLwWTH9SohbSRbadxLbTUFnGXkecsdYMujsDceymxw-QfeO2B74zDnomINlF6EV3KY4KcaWfOgH7Obrv7iYkh7vMO2jyv9oCzfLZJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نیمار در ۱۷ بازی اخیر سانتوس: ۱۱ گل و ۴ پاس‌گل‌
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/Futball180TV/89874" target="_blank">📅 09:21 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89872">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a87231df3.mp4?token=KglxCEXTgafTdNcJ3vjus-YcAnW3auUw2tRx3ks_zxMmtYtnjFH_i-vj3X02Gg57AlFNRwsZMM4GgsTc0uJmArwpYlD7-g0udAsUdbKLB-yO7AUfyunza0lT9SiEit1bKL6vTJZhcIrNCP2YoZ6W6HpUhbHFcgBwVnVy3t3T2u4l2dABAIoEYCuyln6TUn0gImC2ucDi224n4yya5k6TiIli-xjTZusGuNwcyaqmeMkiO6gBCs2fxqB_kkh8qCkPw0IoHGPYnqDH6L52T9jG-8h3sAvoRrypZKHGaW1yvnoUB6-nxagZQ0yD8SmqBxo2olvqCUtXlgL66k-n1ebmDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a87231df3.mp4?token=KglxCEXTgafTdNcJ3vjus-YcAnW3auUw2tRx3ks_zxMmtYtnjFH_i-vj3X02Gg57AlFNRwsZMM4GgsTc0uJmArwpYlD7-g0udAsUdbKLB-yO7AUfyunza0lT9SiEit1bKL6vTJZhcIrNCP2YoZ6W6HpUhbHFcgBwVnVy3t3T2u4l2dABAIoEYCuyln6TUn0gImC2ucDi224n4yya5k6TiIli-xjTZusGuNwcyaqmeMkiO6gBCs2fxqB_kkh8qCkPw0IoHGPYnqDH6L52T9jG-8h3sAvoRrypZKHGaW1yvnoUB6-nxagZQ0yD8SmqBxo2olvqCUtXlgL66k-n1ebmDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
جام‌قهرمانی لالیگا رسما و شرعا تقدیم بارسا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/Futball180TV/89872" target="_blank">📅 00:47 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89871">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FIgELIPM43U5lhRU-205s0Pj3nV720vSt-gHIjxO2WKD39S20pirhoEN-_O2OZmF4ReoXRx7-O0qZIB5Xif927itCM9OZ4ulUOouSt3FAt4YTlwH2-eO0KKEGShIXWx5i80pwUlwWYd4J41Czvug6NtjSVFxitecNs3Xr3ORptqhvDgbKL_LGGuGkx8fcUekoXUXDDpexDHt8kHGUZpn_OrawFS993Iuaw-4AU0EARU4ACOtnyLLzhJPIFZdXwztrFC_RDb9uQltx6qZP9DfxMSswbvj9y88zkWG6XN_iIHY2fJzZ2fy1dzBqTvIbgR-DYzpTdgCFP8xnMHPjxH4-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤯
لواندوفسکی برای سیزدهمین بار قهرمان لیگ داخلی از میان پنج‌لیگ معتبر شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/Futball180TV/89871" target="_blank">📅 00:46 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89870">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PgLdK-PQN4ZNVDSRghkz8qgNZWLl2JG7C2bNqfVv_KoxRwP_Vwddr6M1Hryu0NfolLEvCDLM8GtY_NUoJIpmx7mYh5PNhjtq8JFipjtD8ip7uHcqFuI9zpb3Hb4mhqXNK692T4v8DatHMSjEHET0hbAwtkw-HBZl9_56M2ptBOKgMJtQuWTgmDcryt4j0pOE12KuIr96QcxxwnElzHgieBysZrmBbrgoumXQqwTkyt1MdbRnTuzDVihLB-vG5JolccSdFy0ClDHLYe-pzDL-jFiQP3ZzNn74pBeqoAQnh6-NeXN-7ZCd1SEyDSn-w11S3XRiS4tCYE8zx0SlSW5yNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پرافتخارترین باشگاه‌های اسپانیا در عناوین داخلی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/Futball180TV/89870" target="_blank">📅 00:42 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89869">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-etQJReksp7oB-eIek8BAqWDCKuetUFZE5t8MxBI5sj18MdsnwPhzwo64o8jOvBiPGZcnjNSLayDc4e8bVO_OhlX_gRnaAS3DwaX2eSKoW8f-ngGdgmd1Q7FrcA-Xzr1gVLE18UUhA4lMNF63EvbOX7igwomW9rEcAiLJmDvme_8SuywWBo65o4wa5vC7z0n3iOrWlD4trZtwaKa_OSxnlsaF4h4j4vDf8fqX-calXz0dh2OdSmL6bNQBdhVZ5wlanF6H4wgwsAl06tt0IHmXb1WuJRDOd8jw_b9CJ5KZ1C0davBhpIhhHTRF8aqFQdLLJIhRMngIkSZA-lNsRtYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❤️‍🩹
استوری لیونل‌مسی و تبریک‌قهرمانی بارسا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/Futball180TV/89869" target="_blank">📅 00:40 · 21 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
