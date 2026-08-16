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
<img src="https://cdn4.telesco.pe/file/ms86JJlYhOMwDwdhKjAuwSRFrJM-QQoBJ4Vksim2gQxrU3u_5tQbS09L1oiDw60ecVAi5yZiRMRaE2jnu2C_fPXsCZGIP3IrOhMqtkaPNR6V7O5FUIxNXe5ZAnq61a-QFtI9g248dTpHZpDpSniHwGNFP0FaxcqsXvZFas0AStdfZsWgk4r9oo8VDRn1jJ1EkS_NYO09CIH1ob1qyPIOGnvTbAbqRAD3oiXbSkZKgwzHtoZCaogcn5VcjuKHqINO-oiADkSpnOa3Qd076Q8jUapUd5Hwvxe5vnPdAtiYzHREJQ8j8TSPI5m11kwutiYfcFXOX20n-MJDbUZzxvVp_g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 633K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-25 10:37:02</div>
<hr>

<div class="tg-post" id="msg-27835">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2GKDnELiGjmozW60hTqxqHrBCrI6AZGMpKPG-16C6cUXBHALrNgzOVYOGdQtFssuTSmBCtMs5HezBkoOINpLeZs4tk5Ckd2s5PbdXF3GgChGRHthEehPIoZ-R9vyMBEe1fdHVgmQdm5n6cagQMGrrLpUPnAjVRgi2HnntDhDnLTBU2jJDPLlA5vCglD_d0_FSJJFZgaaslr9ChczPN_CT-EHv3mv4neEcFrQQ0NiWBtSByo_lKGe5ev_e733WHmcLn9kQETHjR54HFBmYy59qVwXr3y5bH4MoY6y86hTjbrMHSTGLZ657eUG8kXiSAFSdtJ5ja_IzauYxF2LloDng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
لیونل‌مسی‌فوق‌ستاره‌آرژانتینی اینترمیامی با پاس گلی که در بازی بامداد امروز داد تعداد پاس گل های کل دوران حرفه‌ایش رو به 420 رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/persiana_Soccer/27835" target="_blank">📅 10:28 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27834">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNABSD8ZnPplnHcehVXy35o-DrLvNtzYSdMqeTpOrmFnIygbObtuh_5ShG_44_XxBFS5SDU2gpPvHURQi6QV_8YiXiAODEumwwNhF9ccJ82cS5s6RgMJvRVHmBAIQgh5YW3KH3GDsjvqspRRAG9xO9JYopn1qDSMaVbxZQz3wsVtyF0SmTgCmsnlMcKI_WkRgT7_XFtzWyCEXHWt_f8AjxUIz9rSCjtAZNEwRu--45PgMNvcFr_-t2dK6CGnP0okJh0ZAx4N0UNeh__os8zYwQ1BTBg8bU0BN-MEFuEEWR8eLB5qYCvhVdCbDoLdRWApHimrwoU6C5ncuDsngduD-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدشد؛سهراب‌بختیاری‌زاده سرمربی استقلال: اومدن خواکین گیل اسپانیایی به ایران بدلیل شرایط منطقه منتفی‌شد. یک مربی خارجی‌که پرسپولیسی‌ها خوب میشناسنش و روی لیگ‌ایران نیز شناخت خوب داره تا دوشنبه به کادرفنی ما اضافه خواهد شد. من دوست داشتم رامین در استقلال…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/persiana_Soccer/27834" target="_blank">📅 09:55 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27833">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OqiXPZXDOElilrva1KL8CN1yMm3TVLtD9RyXFPBNqMlZj7am_Bq2LYWhCYOHXm4sMOJaOhh-oX8D6b4BtF_aPEWjaGAwbXNst5D3DimSmWTaeA4-Wou1EmQm5nrZTjZn67l0rxJ8soUxp_IzsxBED0E4uBvXHoWYrx1YKq9ZnsB8NCufqRUnWtyQqjVP6hp6tG6rOhtkeXEZco3RB4UwsXXDfD53YALiKTZ1FQoUAAuYOMRjMdZNmbqTfZY3SQeiIBvMARQm5Cl9ScUR5RNUtoKfdVPDqqW-HWYvWf0JORHQ8lRGMnGUylBF75Q-F1E1mRQPoxifCi4qQ-tYHe2IOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته اول لیگ برتر؛ دشت سه امتیازی شاگردان تارتار درگام‌نخست با درخشش ستاره های تازه وارد.
🟢
شمس آذر قزوین
0️⃣
-
2️⃣
پرسپولیس
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/persiana_Soccer/27833" target="_blank">📅 09:47 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27832">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b267889106.mp4?token=T_s-76WfyOD8WAYwCwbThSe1iPGPMllIZb8f6JjSNsgA-bvNA0aXwJW4cP_aBttrtorAykGHZS7zznXpjN3afB9oOquN8TZ3mYGFEu1qR8d7u7Zf9KhnKBdSfk4fwEU4GtxBNxIAgwm36ow0BJlH_vQn_Y_P5ur3wJuA_by_Ffk4WGJTPkd7VlEMTlQdKXH3qlx6TWgvmOj-lPVJAj11T68WoJya9IlaTydxb-UWeFNzzWo1aSscZWZXHFk8NyV8ht-8NTx_6RLClgUwkzG0_KQIDrCvoXVwaNOz1BBK9_eDnRY_HRz399kBWti2HvaMGy3F-8xR2rydFJXA8xF72Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b267889106.mp4?token=T_s-76WfyOD8WAYwCwbThSe1iPGPMllIZb8f6JjSNsgA-bvNA0aXwJW4cP_aBttrtorAykGHZS7zznXpjN3afB9oOquN8TZ3mYGFEu1qR8d7u7Zf9KhnKBdSfk4fwEU4GtxBNxIAgwm36ow0BJlH_vQn_Y_P5ur3wJuA_by_Ffk4WGJTPkd7VlEMTlQdKXH3qlx6TWgvmOj-lPVJAj11T68WoJya9IlaTydxb-UWeFNzzWo1aSscZWZXHFk8NyV8ht-8NTx_6RLClgUwkzG0_KQIDrCvoXVwaNOz1BBK9_eDnRY_HRz399kBWti2HvaMGy3F-8xR2rydFJXA8xF72Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
برگاتون‌بریزه؛توبرنامه‌زنده و صبگاهی شبکه سه صداوسیما مجریان‌برنامه به مفاد قرارداد ازدواج رونالدو پرداخته‌اند و میگن رونالدو زرنگی کرده:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/persiana_Soccer/27832" target="_blank">📅 09:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27831">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJ17O_z1-eCN4u4UoAa2oecQgkBFFE-2RzCa1ApVgB-PYOiUKFaDxGWGscJPc2uEIsrElxDSMKmK5ukQq1K4K52YgK3o2nA5EenawJPceGOapl15HmmRp0HDFKLGmOwtxOldFQOsLWQ_B4dNJ-ysKqSljjMIEglV9FgZwyaC5zLh3vSij9-5e-37HKwyB1MBqnTeRsF9svu24YpC9ZFJsAprYA1pAz7wmhYzFFE1ToCStZZtiBAWrXE1ueDjyyogFQwbGVGt5BqxsWzU8JD7sBzwE_a9NnSZuBOPX087CbOMA3S1iBtA0peEr55oH28nUtJCkaaC_KLjjDb72BzEkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل کارتال ظرف یک سال اخیر با این دو ترکیب کارکرده. جنگ ۱۲ روزه واسه اسماعیل کارتال خیلی خوب شد. فرارکردپشت‌سرشم نگاه نکرد. الان هم به جای کار با علیپور داره با لوکاکو کار میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/persiana_Soccer/27831" target="_blank">📅 09:24 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27829">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gd2clVtmjwZkQtyui0XIHmaIACOPpzKa26wishnXGqzZ89QGZAr3uA4KBsaa_fb386eiSFTr5S-DO4BwClSI78VV7P57NDSeJtbhdWPYynY5Ot9iuLiEyQO99HuXUrIELz3Jm5je1KPpXuw0QSfJhuPyGdPgtRu2MvVT0bSJvfX3s_mgiOTbD5mIU6WHTGsR8KaWp9rtPoha4VoGak5too4kMtKSNZ-1aKFo9mf-3UCODK025m5M3hWFcX4KTrQQOa8Y3FeWfOQQh_p84e-F7HU1qD2oJvs8o1CXuZu2nkTPVzuCwNDkFirYtxGbbCM1h9Omn72UkwV7D6YEz3Jr7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M7p5AUKQan8HeFpKbp0moUNSjfAiLIHClWGe8OsBkBfyu-TPCffoVX57Co5j39n0s76JRjDNlgX2OluWFbIQhkF-C5jHKEjlR93-_sZ4d4ZqSbhhS-1ES3KGaiTuq8K26a7mSqXvVDLlSJYt0rmU0Arju-9FK_RgCytzqp5LQ252C6YPmkGj8Q_156ePPBc9EqWewMLEQZkdrINjp4iPj2EKlJjqTggYkj5W2K1ZDnSgOiEq8Wpcn1mQzOqHzOZRsh4Eds0c7uYdzyvsgmRMRi4zgQYn4qqN6S1YQ98KY6tLKxNdmreASxHunhPQZRoHhkue_oe8a1bu7r9aPnmEuA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
جالبه‌بدونید با اینکه رونالدو چند روز پیش با جورجینا ازدواج کرد و ده ساله که با اکسش کات کرده ولی هنوز عکساشو با اکسش از پیجش پاک نکرده و گذاشته‌ بمونه! شما تاریخارو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/27829" target="_blank">📅 01:05 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27827">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1915fbd475.mp4?token=e24s3V0k_JlbKlCm0kdQo_lOwaweqiQDRXog-oY_mWD_nXKtEkLTbTW02oB10r9pdz6exda1GyoBRQz0v8AL8Gvi6tjTCuRIpKX9JCKTR0Z3s-z6dPTvkBWnEZsACdqaUsSBsKXgqFEwMkNZP5nNf-FFqJdPmgfXMgx7_JJk5oJVWdRxGuj2xH1pCr7Do3_jc6voWOMW7cAfe8089aWvJ6RVfuuLRX0EHhWrRGi-iD8nQLHV4odpRX8MZBzHB1vzvjTm5de1s_6a9POOTP0FTYtNQDS_F1qXwDv34RFePreDkKe07rqL_B1UFey1Xzfg4BA_UcbxK5yKM6dRe8q6oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1915fbd475.mp4?token=e24s3V0k_JlbKlCm0kdQo_lOwaweqiQDRXog-oY_mWD_nXKtEkLTbTW02oB10r9pdz6exda1GyoBRQz0v8AL8Gvi6tjTCuRIpKX9JCKTR0Z3s-z6dPTvkBWnEZsACdqaUsSBsKXgqFEwMkNZP5nNf-FFqJdPmgfXMgx7_JJk5oJVWdRxGuj2xH1pCr7Do3_jc6voWOMW7cAfe8089aWvJ6RVfuuLRX0EHhWrRGi-iD8nQLHV4odpRX8MZBzHB1vzvjTm5de1s_6a9POOTP0FTYtNQDS_F1qXwDv34RFePreDkKe07rqL_B1UFey1Xzfg4BA_UcbxK5yKM6dRe8q6oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علی‌ اکبری تو مسابقه امشب‌ در عین ناباوری مثل n دفعه قبلی تو راند اول ناک اوت شد و باخت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/27827" target="_blank">📅 00:58 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27826">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v4DqHrfTn-KqnM1xnn3hDR1KEyT2TN0x4bVhLE5JbhwI-yNo9dy_4Iz_u4ncMHBGxGSxHfv8rdGSzj9huRJ178kHiujoDID8GCARovB8puNUt6HC2dspXrmszr6kLq0AbvhVaEB_n29eqn6iKzk9JrTBuaMYpGV1FHDZSmtIWXInLB-5f5HsGeVU3UP6AxWM1cK6wPHaUm8GZ85MmELTfkx2vaJds_obKI_n8f027Z3GsQage2hj4bBRTLWuSK1GZbE7ptXNnU7vwAQC5-pth89odRaKPR6u9YOvDu4_kZk5h1GmoHYXqli5-0L3uZm2cJ4CYqLjGx5YKJw97NCckA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدارها‌ی‌‌ امروز؛
تقابل تماشایی شاگردان میکل آرتتا و مارسکا در کامیونیتی شیلد انگلستان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/27826" target="_blank">📅 00:58 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27825">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/umWM5ftQINTmrymPspciwIBAwboURu4pbaEFn8GO_krOJZXTo0gNBKoS3VHZS_XTuvzkqMIgvpWyzNd7BjhRAIq16jyIMcxjmsLBr4z_ryZFeyXIw6oUAffwpuRh9quwzaUQfCS7UE66wqrHEPm-hLViKbW4RNh72uxVrHQUfqhtmFjJrWj3RmYveF18sPkRD-KbTSgah3FbPf5yoiJV7S3PjtAsHHMmAB4Uo3ZhEDuxAnNvsp5S-OLJNdK2_mzCSUerq_ChQ6OjnWNM8Fsg6PnAUqIakUtlJ-jrvUF8F63IVd1pXgw0y88YplkHhTPH23vnSZWIvEK3lWkm2IzoYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدارهای‌‌دیروز؛
از برد پرسپولیس در گام نخست تا شکست یونایتدی‌ها برابر سرمربی پیشین
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/27825" target="_blank">📅 00:58 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27824">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fj2bapyHsdsk-nTu_T1o98o_6K3RYVQBGX-590pjPy-a9qlWnmO70CHsDNcNtFm2cfd1efemf1nYWtG_DU3a-kUwnAR7llQTcCJac5eLNqhDyVgTxIb9qkQPJJO24SPdwlsvvTYgEkq8PacIIjt1elnfsIQ-OmoIor7nLEl-dWOx08ow1aR6OkPiJrBwpgFlHb86lC2rUIw-COZM_4v8He6HZqbCV1YzBgWOOQ4n86--7wGMRgxz8-x6jjgOeTkkgl1O_Hpi1lgOeiSeXVL7sury4k3t3r_M-TfB8H8YgHa4KsBS6BzzVu4JnUR9Zsd_iFqlDvZrdYNoVMg3vf3ooQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
این شبا همه از پیش بینی فوتبال دارن پول درمیارن
🔥
💖
اگه توم‌دوس‌داری فوتبال لیگ های اروپایی با یه ادم حرفه‌ای پیش‌بینی‌کنی و کسب درامد کنی عضو کانال بکس بت شو
💖
a24
📣
کانال
بکس بت
برای عاشقان فوتبال چون هم فوتبال میبینی هم پیش بینی میکنی و پول در میاری
🔥
💵
‼️
توم میتونی از پیش بینی فوتبال یه پول خوب به جیب بزنی پس با متخصص این کار همراه شو
💖
💖
https://t.me/+F1CivZlkxrgzMTM0
https://t.me/+F1CivZlkxrgzMTM0</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/27824" target="_blank">📅 00:58 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27823">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ac9dd137a.mp4?token=ECGO740KX4s7ol8_YwsVpaorF6pmyauL0-5DL1m9dU2bs_RE8tnQuV-Nlo3X7VfrnBjvHJm7HaQSq8SEdN2t5I2gLLyXKZCmkalE9_xsWBWxl6ykO263nMeAT8s1OumF0ytKq7m2cFrWA0Ko1VB4qIsFomQwBFNIDR_SkQ5ColdanOJq1x8-nf9VqrSMe8YSe7UkB3qgFIalqEczURDejE65R_ZK3Kroza2M5X92do5P816FpYkOUy_YLSq78IQXG90J_AW7mhzQ9_QO29oetj9XlsDml30QdI7rSEMLJFO8rQ8S7jBswd5ydv6JEuRhN2ESXpk1g44-eFLA4EUsMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ac9dd137a.mp4?token=ECGO740KX4s7ol8_YwsVpaorF6pmyauL0-5DL1m9dU2bs_RE8tnQuV-Nlo3X7VfrnBjvHJm7HaQSq8SEdN2t5I2gLLyXKZCmkalE9_xsWBWxl6ykO263nMeAT8s1OumF0ytKq7m2cFrWA0Ko1VB4qIsFomQwBFNIDR_SkQ5ColdanOJq1x8-nf9VqrSMe8YSe7UkB3qgFIalqEczURDejE65R_ZK3Kroza2M5X92do5P816FpYkOUy_YLSq78IQXG90J_AW7mhzQ9_QO29oetj9XlsDml30QdI7rSEMLJFO8rQ8S7jBswd5ydv6JEuRhN2ESXpk1g44-eFLA4EUsMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
برگاتون‌بریزه
؛توبرنامه‌زنده و صبگاهی شبکه سه صداوسیما مجریان‌برنامه به مفاد قرارداد ازدواج رونالدو پرداخته‌اند و میگن رونالدو زرنگی کرده:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/27823" target="_blank">📅 00:38 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27822">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gUSk4kuVPj1lUmY2OzeMigYSCvF-jAk3e2Lt0UDgUWEYIc_FuKgpCadM5aOcOsI-upVhhzTk3E-2krryKx0Fxk-9fY72CuxNLGatY5txMpDIcg6tWUXVYaUFo9Z0QDUBhzO0j5wF5I7Z9pGpLzaj4WPpdAUPV5Sik5egg84thBRTRN2ahMVW0rgYvf-EAKVWjklA0tEJZwclvOdwqkSvOuHx21yTnKbb-abzO6uwbkHVoEvc_5jNmrWBv0wVT8yhw10w07fDP_MkwoMNcz6A9OI32t1CwfhJE2ttV4ehuXZNKkUwqIPv266hHIS05h-42AN3-Yx98VVzaSda6eCLyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇪🇸
🇵🇹
جرارد رومرو: باشگاه بارسلونا در ساعات گذشته برای فعال کردن بندخریدقطعی ژائو کانسلو با الهلال به توافق نهایی رسیده و مدافع پرتغالی الهلال فصل آینده نیز در جمع شاگردان فلیک خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/27822" target="_blank">📅 00:22 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27821">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXFiquJjUjn1ULPc5Vyed8LB7r_4h3utjXJLsmXE0T5pil_tcyd0zwMMh1S8hvjFkcZBW_KEv6cH1E-A6WQPp6tEjEHyhNpUqxA8JE9eb3wGDrHnVGEQ0YhzYw_aFdIx9EOOkw1R72Zh4pxjPDL_c85Je-80OMnmA6sAtLh_KHUerplSryTBKY4y2lula1ejJoRFpfQzjzJvZ2W9fq-8gftg3WJ-EtbHTEdTLGp1qvZVdH9s_Mz9EyuBtNaDN-zau8JryLSPYVZn4-HTfLQ46qMaq_7MQHtQr9e_96bAJKY4dwv2wiSPPNCqX5TXS7xjh3ZUCH7Jq8ZRXBYyrxufJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی_پرشیانا #فوری؛ پیغام جدید محمد قربانی به‌باشگاه‌پرسپولیس بعداز درخشس در دیدار امشب‌مقابل عجمان: پای توافقم با شما هستم. رضایت نامه ام رو بگیرید به تهران خواهم آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/persiana_Soccer/27821" target="_blank">📅 00:12 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27820">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZvuS_di6GQkGkGRFOftAArjPdjQ6DUN7WWbYnqiMY1U_vmruRhvjg4FO7QgcipJWDLI582e3T8L3FpC58zm_ZkI2AhpNk4jKlMjATf4P4cHhzZQ9C0uAp9RoQ7yeTbTOe06r9aIZ-SH_AITdzasCCroBKbVJ-pPijjdOqreOrEzlff5y2Majrtu8YPuhzPiPRf6W9-iKyjn4Y4HkO6kmujDEkjkYaAFX889HZj7WDtqr6ernWXUnKlnZXlMBsFcbgbiv_9x7BH4dWZJ0QexK8SZa8NqW3IoXN8pJe1jOFUgQbrsx9ANg2SHA_iM_I4sgdN_n7i0bEy-zNi9llaO1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#تکمیلی؛ درخصوص وضعیت محمد قربانی زیاد پرسیدید؛ به‌محض‌اینکه باشگاه پرسپولیس مبلغ رضایت‌نامه قربانی رو به حساب الوحده پرداخت کنه هم چون دانیال ایری در کانال خواهیم گفت... فعلا تا جایی که میدونیم بانک‌شهر بودجه رو داده مدیریت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/persiana_Soccer/27820" target="_blank">📅 00:08 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27819">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcgzgO7mhhLtFiLjT1X7_AvBOcLHVR8ZB7ATUyhZk_k52HD2n9vyb8ckuzLRT9Lz9Ps--7d2Yd0ScB-XnPdOAerip8afVaydxI50HTvKPY9loNne3mfAis-YYHFD4MKY2Ey4o4NI5xB7HPgsKUbHAg0x-O56XcmxMoU-OUybkJJXUqEbDnIQio69kEYnM1Vs3Doami_aQIUTo_Bp1ZWZDVTJJn-DLjeWHBtZBDZhSCXPfQykd36EVFoSnHTN8mLqbQ01LqAb1_mrQHYxo1__AKF9Sb9qgrr6vPB1FQVDpQN6XHbghTCdgwF9CRQHV6s5mE1zN5-n--ku7iXyoyeDdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه پاری‌سن ژرمن با انتشار این ویدیو شیک و خفن از فران تورس خرید جدید PSG رونمایی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/persiana_Soccer/27819" target="_blank">📅 23:58 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27818">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pi5W_TC8Rdt_Je76q6Hc_hcZoAIO8vN-oTqcA0O5kbHYUZcpwuMRHsrObaRSCvtEj1vB7Rtxz02DCU9pabyKvOgHDUWmM4c64wvVcLpGnq0tQ3DguQFrrWzlEzLTlk9lvc0TVNAmrKB8KslZskYVcR3-b7tV7XXGTOtRbt_vJMrThKoP196YRO6dAUpCBpwkglwq9-mfjyCKSgpoiEt7XJockDxveNEuvxOhaVM8ywTJcR2Lb2omu_DnfhpC5Nd1kMSKWhgjWbf4kjhkhbd2GY_2FhGhj2QJdXZ8J-P9mhz5CHYXrxeJhrELZJCustvSVPq1eQx49M360uzhND60Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#تکمیلی؛ درخصوص وضعیت محمد قربانی زیاد پرسیدید؛ به‌محض‌اینکه باشگاه پرسپولیس مبلغ رضایت‌نامه قربانی رو به حساب الوحده پرداخت کنه هم چون دانیال ایری در کانال خواهیم گفت... فعلا تا جایی که میدونیم بانک‌شهر بودجه رو داده مدیریت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/persiana_Soccer/27818" target="_blank">📅 23:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27817">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OSjxf7j-mYp-1P2DXkLp1_Zyf72d8Ni062g70AMe3_yKOQPAMpeRZZUHJ2pi1oIV2Z7LX6nJOTVvnqis7rknrRWgx2oQ9P_kjX9684sVamOxJ20lv_kgLaIiVHhxAGAinzRhKKGRo7gnFo44ByyUDevUmtwbENKfTZgBcmr7u9kzMelJlYFet2ZZ_VCa-rmp8ows8ibccdUwcqvGWBUg9kGygmSxMwwdzWtDFwiL7HS1gS8cPUa7HWmF1oW7uggngU7VYr4bWuvzVIyb0vTGn983eyIgJnPJDya-ptKgTR_T0mYSjJYbCA0MRxL6dGtxCfNwfu66M9HMbKc02CZQcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جیف‌بزوس‌بنیانگذارشرکت‌آمازون‌رسما سهامدار ⅓ باشگاه لیورپول شد. پشماتون بریزه که جیف بعد ایلان ماسک و یه‌نفردیگه‌سومین فرد ثروتمند جهانه. دارایی‌های اون چیزی بین 270 تا 290 میلیارد دلار تخمین زده شده. میتونه راحت انگلیس رو بخره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/27817" target="_blank">📅 22:59 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27816">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VhU9tur6VoUiHG4pvvI4kHaq2YEUH_5uT-1ojPzuq0oScuZkw-NieG6WuGbawJHBaUKLXeefPnlHRC3vlo3BrigIv0HXf19RvyotOfnV1okLzb_MZ8vTql6DNnATGLntiLiIO-HmPdyKqoWn6U5ibGOv64CQMLufhLiuDzoCfxJS-9FTzsZ6l1ZByXuPJb9FNKln2mjCmRp7Jxa9olAbcOpxersVcPmovEKGWhbEUIOCpeITgsweackOadzCdnN3u5P47SWxFyTaCiHUb1svQmDHHhcacsuNBHzBdGnpvY_HTuiYDg4rsrYewfTEUFB6p3F3mkDZTvvgOdp__qOunA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته اول لیگ برتر؛ دشت سه امتیازی شاگردان تارتار درگام‌نخست با درخشش ستاره های تازه وارد.
🟢
شمس آذر قزوین
0️⃣
-
2️⃣
پرسپولیس
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/27816" target="_blank">📅 22:31 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27815">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b8f616635.mp4?token=jnXXP9jGmc6p3sKM3w5bvHvgrL-MNzLboOH83lLcbM8f48T0-idh-R_0R3rnXUvbcsbU8FDb65wISz9ZEoAvh1YCfWj_ypHp2GuKT-9lD0Lusbwb7kbEAcEUSaq-Qn3i14ikhSq2FzUAZ6nzWZgln5msvLIfgRjWLlIzLsxi66vrt9Cn8wO9g-xsrDcdk7nf-SiaUdSxy6NQvv9dPjdA9rwK4XPz85O7DWs0Su5uHKG228g1jtYkhz4sZlsCvX0BEncdKWu6_hGTwNuSIGOqv0GVJPqPy37QsDzgqF-CEkjkwE31p4UfeXL_IehcqXEFYbjI5X9J_6bzFjjScNITk41Vp0PN2TukTHZ-ZO3JAuRU997XAafr091rfdmPSShvHTUOvv9kkiZREtalBE99gbjz18y85xBMIGe_xmeZAd8GYsUy_LhrQnntG385c7NNGEi7y4O2ZkvL3m13730tH78By9jzig8Zgik6MCP1WTf426pAgxKJg1w1YG-_25i8h746Y0KPFCjU3abMs35qys_HUHp3w9wkwB_ip6WG132kRHzBt1rtwOfDM0lBHVMPYT8mx-Ekc1563BvaAryUDbhVKSGbViqjagrx8iSZpxA_TfDrEuAPg27daDPr7dP5gCLeLDjy77bYJxW7ZzxKsqaUDhkvC1twehEDgmg0WnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b8f616635.mp4?token=jnXXP9jGmc6p3sKM3w5bvHvgrL-MNzLboOH83lLcbM8f48T0-idh-R_0R3rnXUvbcsbU8FDb65wISz9ZEoAvh1YCfWj_ypHp2GuKT-9lD0Lusbwb7kbEAcEUSaq-Qn3i14ikhSq2FzUAZ6nzWZgln5msvLIfgRjWLlIzLsxi66vrt9Cn8wO9g-xsrDcdk7nf-SiaUdSxy6NQvv9dPjdA9rwK4XPz85O7DWs0Su5uHKG228g1jtYkhz4sZlsCvX0BEncdKWu6_hGTwNuSIGOqv0GVJPqPy37QsDzgqF-CEkjkwE31p4UfeXL_IehcqXEFYbjI5X9J_6bzFjjScNITk41Vp0PN2TukTHZ-ZO3JAuRU997XAafr091rfdmPSShvHTUOvv9kkiZREtalBE99gbjz18y85xBMIGe_xmeZAd8GYsUy_LhrQnntG385c7NNGEi7y4O2ZkvL3m13730tH78By9jzig8Zgik6MCP1WTf426pAgxKJg1w1YG-_25i8h746Y0KPFCjU3abMs35qys_HUHp3w9wkwB_ip6WG132kRHzBt1rtwOfDM0lBHVMPYT8mx-Ekc1563BvaAryUDbhVKSGbViqjagrx8iSZpxA_TfDrEuAPg27daDPr7dP5gCLeLDjy77bYJxW7ZzxKsqaUDhkvC1twehEDgmg0WnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ گوهر خانوم داره تک تک عکساش رو منتشر میکنه. این بازیگر دو رگه عصر امروز مدعی شده بود که رامین رضاییان دنبال رابطه با او بوده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/27815" target="_blank">📅 22:21 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27814">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eos3MsQzCI8vnkaj2eNgCqe1Xxf0c6l15hZeAnoDBHGXjevzAjL3dyGP0p-0uJrhR-uk9W6cKh7_QG62OH7vo-GXV0DzT8mOIO0kATXHQH0HyOtJEvNuPA2g-rRM3R8OnyxBeYwSIqbtEGhB5F5550l4ER9_ogaZ4lEXAxAtSkydRjdGpkZSvHzijZvyIBMDmdDLWYHcRyvFhgIuhKwctu9Ia0R9Zzvcewt4URpMFSAQ38t1FZdSdYLUt0oG0vLxy_0jBGBE2BZAOhipQSrffjpcJaz1Lv59vU8vCGhd40aPu8x-2K9MrZXP2IotZwVnEyoXOd2c9GTSe8oTZOHdFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه دیدارهای هفته دوم رقابت‌های لیگ برتر؛ دیدارهای این هفته 27 و 28 مرداد برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/27814" target="_blank">📅 22:10 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27813">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YMw7oMilZZPcswclkPfvOFpi4GivXSFuOXNg2B1k21JVffCOySLQj2Jiopb6WeG1wTo6FxyILazSwy_1aJByd4OybqKnlIwkrr8BfuimHUYXqQ5pg2mz96NQX4BKme4pLZRBFVcojn6rEqXS0XhRg6oiMSBmOhf9pGztPXIFiv02lVFV6Cbfki2KtuSHXHJYpgh3Rc-BsQr8uVPoG3wiXgXsJ4JaKDIsl-DZQiwZpJqkbtnZbB6C7N4MT224OEfXZfHCsNrAjBvFsSfG83Qk5ELaqhymKoW6xFuqnuGhSaWtaw5CfU2JMym-qM_AWwcsei4KJhsjFYCPL7lz2olgSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه دیدارهای هفته دوم رقابت‌های لیگ برتر؛ دیدارهای این هفته 27 و 28 مرداد برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/27813" target="_blank">📅 21:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27812">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JdEaVUXGlOhckMkscNZMnB4b1qRmmhPDkBqQKyF0xmEP-bNA7151BOE7QCPSVvjrcfFS0WwFXGhDypqKLNr2KEyp42SLtXqEWJfjKgBKPAlSLzpuCFq8U3N8emaZulsPiojXOuGijSEL8Mueh0MxzLZTypmqra1ozzk50fKR9s8tyNJdu8QeY0Z9RTzEJe7mmuXo_M7UyTmhmJUkiIj34uNWCEF5Ihf7vzXdrCQ16Mxs_YTpnpLiyce1Abp7R-EGuG4NH5IruE1j5pjm2k3LczXkpdkDz1gazmaM9rLYrlSGFpNWmaCmMdHZOXPvtzHRQVVBKjmo9N8OZ1nnR-Vxew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇮🇷
#تکمیلی؛ دیشب هم گفتیم ممکنه یه مقداری مبلغ‌رضایت‌نامه محمد قربانی بالابرود اما اینکه گفته میشود باشگاه‌الوحده‌گفته این بازیکن رو نمیفروشیم صحت نداره چون با جانشینش به توافق رسیده اند. مدیر برنامه قربانی هم امروز گفته 800 تا رو سریع واریز کنید تا رضایت…</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/27812" target="_blank">📅 21:53 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27811">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DsDXYNi3GvetYbPxoeSq0fY2qe7BMeMerNkatjJqTTFfLwSaZQNaf007tnHshkrapVi0UuH5u5KrWv2B3AaAXbLjjYN7ym9ZAENt_d_ehN_i4_Bg2yV6lvdLR6ra2hpTEQoyW9ZZbdHh6u8a5tuLzb12S0OazMmKxUWNKIIpOxjMHqdkgM7VX_LhDjP1nMB5JRonbdAz96ASLoZtMkYfeZU5OHtU4FazqHAOTh0uYjL9lEirnHClmLDp1iXLWyLAou1Hddzn9w8qa6J4lCvZwOYbWmWGSvb9fvt2WKNQpgF6I63Dv58pYiWNOomx2wz6bSosfUqYSSpRYihjTiIerg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته اول لیگ برتر؛ دشت سه امتیازی شاگردان تارتار درگام‌نخست با درخشش ستاره های تازه وارد.
🟢
شمس آذر قزوین
0️⃣
-
2️⃣
پرسپولیس
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/27811" target="_blank">📅 21:45 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27810">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CsK9qxMTFR0y9DZDSQy8_hXDS2BqQVXomi1xUgtpw2K-m9-p8j4I3DuyafMotE3k0Liah_MvAXfznxUjM-JgwmhzEGQnTAXWPsaxZ_CSJ__aBxswjFxfEJnQwi_3834BU03EvCaQEQomHuUCFhVPKzEachiv1Mq92sosVqvQGn5h_eEhtlYUshj9mTTLidoyBBF4tuxkFy5qff4ZDC8ccQJw74y7O1RWJ5dYu_4xOSxBTbX1TZitqECOWrTtiPOEaeARkbQxo9Tfcke7Urr-F3VUC3D2FsKl1V_L85EXjgb_42XrZAGSxCopw7SaVTmlMMMU0EABTEcWvI3TpDKVAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
گل دوم پرسپولیس به شمس‌آذر توسط محمد عمری در دقیقه 15 روی توپ گیری خودِ بازیکن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/27810" target="_blank">📅 21:32 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27809">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64bc0e0471.mp4?token=qReI0Bb5JsaP-xt5alFBO8bLdGSMifIGLCxQG2vrHSRqYrA1UqG-rOFk8wlO1dFxOw4LuAXx6YjIhln50N-utGAP8Hlud7x8rMGpHcBVlB4s35rQLTsXZaVC_EnK7sJIAQRgPHpqL5deeeVF_CFFyAHCM2Sg9OgdKC4iVkdVFC5r6duhDqtNIwxo5CMe76SDvsIYr4vb5XX4sfpoLcwvcI7P8tZm8uHkA6nX7AxTscFGOKP6S5nx82ZIKI9IskCcZKrFo_EmdG-SsOw9YLpZ7JP5L4lYalAUKcaPOQj-82N_74Zc2HiHzAkZkfblbEpCwCZFEFvcq7fxNdlbt5yBUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64bc0e0471.mp4?token=qReI0Bb5JsaP-xt5alFBO8bLdGSMifIGLCxQG2vrHSRqYrA1UqG-rOFk8wlO1dFxOw4LuAXx6YjIhln50N-utGAP8Hlud7x8rMGpHcBVlB4s35rQLTsXZaVC_EnK7sJIAQRgPHpqL5deeeVF_CFFyAHCM2Sg9OgdKC4iVkdVFC5r6duhDqtNIwxo5CMe76SDvsIYr4vb5XX4sfpoLcwvcI7P8tZm8uHkA6nX7AxTscFGOKP6S5nx82ZIKI9IskCcZKrFo_EmdG-SsOw9YLpZ7JP5L4lYalAUKcaPOQj-82N_74Zc2HiHzAkZkfblbEpCwCZFEFvcq7fxNdlbt5yBUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
استقبال‌ویژه‌بازیکنان وکادرفنی‌تیم النصر از کریس رونالدو بعد از ازدواج رسمی‌اش با جورجینا؛ وایب صورت CR7 خیلی خوبه. حلقه دستش رو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/27809" target="_blank">📅 21:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27808">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NqDq9i5DdgQv2NSIGnkmyyHxX1eZAgZmKCESqRjV3MaRVbt6DEd7xF94BRsOx1ZetmcS_H3mdJedPaO35qUKcvx7fihyd_xk1QNFgDyuXB6YhOMe72AgNlzWtQY-CRGXsvB2snfmFbO7in9msToqFIDMUCcONVMJ0PYovDp5P_9slWFr6CTItabQY6N3ACL_vrO4Joi-507i3jMywpmVdGqHllGcVcxmUeHyHsQOeo5K1sMPE2tWCdijj8vFDGnn56MKCPSkFTI7e3JflRMhKHYhsFvE3OOGsQbPHdrKNM3xosvqHdCqsdpDChJP7dfXaw5S5ISXy7vOncp3hsMEQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
باشگاه‌سپاهان‌که روزگذشته با کسری طاهری قرارداد امضاکرد به‌خواست‌محرم نویدکیا بار دیگر از فیفا استعلام‌گرفت تا مشکلی برای این تیم در شروع فصل جدید پیش نیاد و با مثبت بودن استعلام فیفا از کسری طاهری رسما رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/27808" target="_blank">📅 20:48 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27807">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">📹
خلاصه‌دیداردوستانه جذب و پرگل امروز دو تیم آث میلان
🆚
منچستریونایتد؛این‌اولین پیروزی میلانِ مدل روبن آموریم در مسابقات پیش فصل بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/27807" target="_blank">📅 20:31 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27806">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed602d7201.mp4?token=j8B7Sv-g7_SBo9xzCm2MGFRHYCWfQ8_kkHg1K0mEcnDbXGu4LUq3NlcQyOKi0JVtEBmUkHxwdW-e4-e1cNfMULmdMyRcv7ftH7Z7uct7Vwd4e2XHwa4L_aliEvas3TOFlIXrwoY2ST21lLfRCAJUOMI2bSbFJbxzc-yQVzv3oGvo4M08coxj4tqkw7TEVGsI7ohiv9q4lIThefOLmbJBA3nNHSCVCJ4Fpen8y9JyYnZnD1x7ypiapAYY3DiUMllHbc7HxQSGbv0GtgI-LO8wstiQGid1Ja3i5xzEPtBjVWtT3r3La3Z605IORqJe6_IuHnbRMJT4OYJ0VN-iJsDSww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed602d7201.mp4?token=j8B7Sv-g7_SBo9xzCm2MGFRHYCWfQ8_kkHg1K0mEcnDbXGu4LUq3NlcQyOKi0JVtEBmUkHxwdW-e4-e1cNfMULmdMyRcv7ftH7Z7uct7Vwd4e2XHwa4L_aliEvas3TOFlIXrwoY2ST21lLfRCAJUOMI2bSbFJbxzc-yQVzv3oGvo4M08coxj4tqkw7TEVGsI7ohiv9q4lIThefOLmbJBA3nNHSCVCJ4Fpen8y9JyYnZnD1x7ypiapAYY3DiUMllHbc7HxQSGbv0GtgI-LO8wstiQGid1Ja3i5xzEPtBjVWtT3r3La3Z605IORqJe6_IuHnbRMJT4OYJ0VN-iJsDSww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
با حاضر نشدن بازیکنان مس رفسنجان در بازی امروز مقابل صنعت‌نفت درپلی‌آف‌لیگ‌برتر؛ بازی سه - هیچ به سودصنعت‌نفت شد و تیم محبوب آبادان بار دیگر به رقابت‌های لیگ برتر خلیج فارس صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/27806" target="_blank">📅 20:20 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27805">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fUTF-EiWQU3L54rMyyyTKj5Nk5fDcFNfvHQZtTcLxKo8BPMFQm62K0XPsFrDrspvPhVT4eAr50Ven7w3K-LqAmglrQfHYThw61IXhSgr81Pz1MPy_n-MAFJY9vzPIJGL7478VSlYv0yFX8ApKipW-TSO9miKgbW7cy3fTt__acAcSS9GN21cVDd0OmTrOXpRYR3vhZCB_Kgdg4kdGG5Pj4uYj1KB_dH3lI-ISn0kUjS2_Hh5k0ts1XFvRxdy22_b2u8s2Owx1K9eWVb742EmzdxHwXrNBJb6vY2hnkeJZRyBjXzQ6BW6M0xn4njQzwBJPlfC4IC2k-fvLEN9DsY6yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
تایید خبر پرشیانا درباره‌محمدجواد حسین نژاد توسط‌مدیرعامل‌تیم‌پرسپولیس: مذاکره کردیم. رقمی خیلی‌بالاتر دومیلیون‌دلار به ما گفتند اما چیزی که برامون مهم بود این بود که خودِ حسین نژاد هیچ علاقه‌‌ای به این‌انتقال نداشت و بما پاسخ منفی داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/27805" target="_blank">📅 20:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27804">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jLwMJYN-6iJM_WtViJr81jUsHkvO6SPlbWcfqex2t5bYgBFpUpUtR20uemjzTVgmWMs_pYfdzaj-RfOBLDUWOS-uuO1tAJHqJyGOE9Kvyb4Necv6oTVkjcWbjNXJ5BWXoz2I8exNjygIPzQQG3VGPi87L1TDOuar0EvthKDBbkGMZ2HzY-Y8ArGTIVWevtodMosbEbETeMgqUsNzqYvTViBvebnW5tsp-jgLkUNj3IRLjmGla63RNis8Ffz4xQMZ6WwRxImaQTmb1MUfuzAbVvhWQSdaIlZ0XkS87Z-FqoOGp49pLfARCFha9ExJfThjE17QLGFKwocnY8lFjIlVaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
🔴
در جذاب ترین دیدار دوستانه امروز؛
تیم منچستریونایتدِ مدل کریک مقابل شاگردان روبن آموریم در آث میلان با نتیجه چهار بر شکست خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/27804" target="_blank">📅 20:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27802">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35ec76430d.mp4?token=AsjNPnIGArbKN-FBc57ykdSKqIvj5FyY8CWkSllb-R8voMq3yD_T5JZLUoXesoKqdQs7PW_eNyrmMWNgg-xr_Jnb5cxL336kyun01V5h62XaqxWArcbRES5ptnK7OBCkFvupiuJ0Hk7zO6sV40S_ulGF1L-BBwEuDlmcrnIGkBXefhkED4LACG9ph10KOWXeUcd9QEG6XSvJIsQRZWV0MhiJnspGqdwBgY4fEDRlaiXKL2CMgXeA_O6FM3xDITsP7nzUGbHJGUQzpLhvf4UFhdhEjDeLcxIfcXtKq25e_bN9vaPmOaxMFJYbRaRJFq-mHCiMU6rOAt23P-w4uQLzhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35ec76430d.mp4?token=AsjNPnIGArbKN-FBc57ykdSKqIvj5FyY8CWkSllb-R8voMq3yD_T5JZLUoXesoKqdQs7PW_eNyrmMWNgg-xr_Jnb5cxL336kyun01V5h62XaqxWArcbRES5ptnK7OBCkFvupiuJ0Hk7zO6sV40S_ulGF1L-BBwEuDlmcrnIGkBXefhkED4LACG9ph10KOWXeUcd9QEG6XSvJIsQRZWV0MhiJnspGqdwBgY4fEDRlaiXKL2CMgXeA_O6FM3xDITsP7nzUGbHJGUQzpLhvf4UFhdhEjDeLcxIfcXtKq25e_bN9vaPmOaxMFJYbRaRJFq-mHCiMU6rOAt23P-w4uQLzhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
گل‌اول‌پرسپولیس به شمس آذر قزوین توسط محمد مهدی محبی در دقیقه 10 روی سانتر جلالی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/27802" target="_blank">📅 19:49 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27801">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5771e6cffe.mp4?token=gddKcZe0zTnJWC44JKkmqn6u1m1hoshVtvVVkBT-_WwGbfHYgEYVozreun2hBe-dRHD2E1By6Yjl7BizLRgIG5BEvi7UuWB8YHqXoQyxZYUmBF-LdqBHbwzUfg-l805MHS3k3-QjOEfJe50o_CXG0brOyG7d4GFCg_7o-3JagVLKXlQgF4TON0Bc7TxOvliB6fojUk7IxcqU9UKc4haOMbu3vgSUWhU2qtfHSivrlhuImiEmLZV5ZSzuJsVXUWpcmjkplHbMZIgkRa9uomWmJYoEjWVIi9CWr8FKhTeypUSsTm-8AX98hUh5z0o3RYVOS77DYO_sx2BLumZ1Ly8DQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5771e6cffe.mp4?token=gddKcZe0zTnJWC44JKkmqn6u1m1hoshVtvVVkBT-_WwGbfHYgEYVozreun2hBe-dRHD2E1By6Yjl7BizLRgIG5BEvi7UuWB8YHqXoQyxZYUmBF-LdqBHbwzUfg-l805MHS3k3-QjOEfJe50o_CXG0brOyG7d4GFCg_7o-3JagVLKXlQgF4TON0Bc7TxOvliB6fojUk7IxcqU9UKc4haOMbu3vgSUWhU2qtfHSivrlhuImiEmLZV5ZSzuJsVXUWpcmjkplHbMZIgkRa9uomWmJYoEjWVIi9CWr8FKhTeypUSsTm-8AX98hUh5z0o3RYVOS77DYO_sx2BLumZ1Ly8DQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
گل‌اول‌پرسپولیس به شمس آذر قزوین توسط محمد مهدی محبی در دقیقه 10 روی سانتر جلالی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/27801" target="_blank">📅 19:44 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27800">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ab0f14bad.mp4?token=qrQDy6kItnwkHatWqIPLqfOekxlJHEnQ12c-E2cl0LJ5KxPL_38oejRul6Oq2V48wYub_8hM0OcKbXO-nXrrAIuyeIRsUpfUaqVZUt7d_qNRVnnvOnfR-JVUYPrYCATsjORwh5rj9HRq0pZUQu5B7ma6cuk9q9o2xJta2v0QTz7rqTHV5DNcFfhi5vGd8uJZ8PMUAaIVcL03GdOPiiNSWsJDqH5MsdXiCTtTdaaOAsdT17eFooVOXHTO-ftJzY79rDiladImwL-hu-R1S8C3QeDoiP6vY3wBWAa6N34ck0Cf0Lk3ObB-BVfj54NSxg_WvVGobjAD4oSXpx8DtlqPpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ab0f14bad.mp4?token=qrQDy6kItnwkHatWqIPLqfOekxlJHEnQ12c-E2cl0LJ5KxPL_38oejRul6Oq2V48wYub_8hM0OcKbXO-nXrrAIuyeIRsUpfUaqVZUt7d_qNRVnnvOnfR-JVUYPrYCATsjORwh5rj9HRq0pZUQu5B7ma6cuk9q9o2xJta2v0QTz7rqTHV5DNcFfhi5vGd8uJZ8PMUAaIVcL03GdOPiiNSWsJDqH5MsdXiCTtTdaaOAsdT17eFooVOXHTO-ftJzY79rDiladImwL-hu-R1S8C3QeDoiP6vY3wBWAa6N34ck0Cf0Lk3ObB-BVfj54NSxg_WvVGobjAD4oSXpx8DtlqPpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ محمد جواد حسین نژاد دقایقی قبل ضمن تشکر از باشگاه پرسپولیس آفر این تیم رو ردکرد و به‌پیمان‌حدادی مدیرعامل‌سرخپوشان اعلام کرده که فعلا قصد نداره به لیگ برتر ایران برگرده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/27800" target="_blank">📅 19:20 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27799">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e06d9e3d33.mp4?token=O5TXeC-1v34JoT4Y6uyq1b-pKHM-ZcXDBusueOGLkQriyvG_-pG2PYMkTdZbgBRicbMhvEQjskqgYieJeNcMTFtWEoXze-YH8__aWxXZ0gTQ5bgb9k9PDOXYC-r9tr7mG6zWjHaYkVU38Yr8jsjVg5nHbo4srcsUbYagmKDHNeghklh0pfmAiRFkQP5iLaSZqYqL_Ry5qo27ByNCPMwAL5ujE05gZ_LqWskkXgqcKDfeJFKrSsDFXr0v-sEWLJdUcGFCJNVqJlBBllYOtPQLB_qQyPIJ7dwC5_3w_W61gKevNzGl_K0EWERce1p6bj5_rJtFBSIvLbzKdo-ZEkvGUQ2DhK7PeXlwnYD4_KJ_utIaJuO72aX8wMJBl9_tZQWajDfrLpmdGucFp7mOi5WFiUIkCNd0yNzTa3l1yoNGNAa0wsRA3x3ILTRPTFy0lMZGAEcXPpJf8860USNH2B9N4jvDrqQMvya88ExQuvdPv4MaI5lTbeClQ4mO8NlekjDT3BsN2G9kf8V3afDWrgOMuuNkEr-MIf2mu-QYpCIH-Bh1EbIiykiFaBDPeTn47DvXyvh8RVsP1Ld5_BSb5mwTRDYJFQ7LE38-BcHjqD_YVxMiIYuLXGKM5MqYGahqxw_h7cr_zEpAVH9VoLjuv4UIXmDE-k6yXb_gpyIT9wxnnoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e06d9e3d33.mp4?token=O5TXeC-1v34JoT4Y6uyq1b-pKHM-ZcXDBusueOGLkQriyvG_-pG2PYMkTdZbgBRicbMhvEQjskqgYieJeNcMTFtWEoXze-YH8__aWxXZ0gTQ5bgb9k9PDOXYC-r9tr7mG6zWjHaYkVU38Yr8jsjVg5nHbo4srcsUbYagmKDHNeghklh0pfmAiRFkQP5iLaSZqYqL_Ry5qo27ByNCPMwAL5ujE05gZ_LqWskkXgqcKDfeJFKrSsDFXr0v-sEWLJdUcGFCJNVqJlBBllYOtPQLB_qQyPIJ7dwC5_3w_W61gKevNzGl_K0EWERce1p6bj5_rJtFBSIvLbzKdo-ZEkvGUQ2DhK7PeXlwnYD4_KJ_utIaJuO72aX8wMJBl9_tZQWajDfrLpmdGucFp7mOi5WFiUIkCNd0yNzTa3l1yoNGNAa0wsRA3x3ILTRPTFy0lMZGAEcXPpJf8860USNH2B9N4jvDrqQMvya88ExQuvdPv4MaI5lTbeClQ4mO8NlekjDT3BsN2G9kf8V3afDWrgOMuuNkEr-MIf2mu-QYpCIH-Bh1EbIiykiFaBDPeTn47DvXyvh8RVsP1Ld5_BSb5mwTRDYJFQ7LE38-BcHjqD_YVxMiIYuLXGKM5MqYGahqxw_h7cr_zEpAVH9VoLjuv4UIXmDE-k6yXb_gpyIT9wxnnoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🇮🇷
#تکمیلی؛ درخصوص وضعیت محمد قربانی زیاد پرسیدید؛ به‌محض‌اینکه باشگاه پرسپولیس مبلغ رضایت‌نامه قربانی رو به حساب الوحده پرداخت کنه هم چون دانیال ایری در کانال خواهیم گفت... فعلا تا جایی که میدونیم بانک‌شهر بودجه رو داده مدیریت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/27799" target="_blank">📅 19:10 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27798">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwwxiLBEmGJM5M0F3hlYrJTbKteoW7QISZUxK6S_dSDre9m728n7OnvomQJWsXW1f7g5_R7of9qJb6mS_uovLHxf6VpxE9zZRNEFNn4TXnRsfsHDGACFMwnfdbEIj02nMHA5VcTVD_KaXgFIfnYKL9sfcFRGfiGYkfbeBcpZHiEzR9CXGaCeTq8Lx6huld3IPxwWxhpD3zvbWV8AkPgaTf2C0BTU5d_SGIndEmInt7q7QG8ynbpu_W0l95e8ycKtcCmuBA6CWCcKq2WoAP2O2wg1v9N_doNq6HGiGP2kXf-40uJJ1woiQtTmri2H14rsr-nX9SfxjcC_whFerJ-7OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته اول لیگ برتر؛ ترکیب تیم پرسپولیس برای دیدار امشب با شمس آذر؛ ساعت 19:30 شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/27798" target="_blank">📅 18:45 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27797">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQ-RToRVSJ-EYwfyrES3lTVXct56j4XbZofUlywquQh3A8GCbYR3j2GNm3zOJ4dWSb1fXl0_sFySt4R6avGclaEP1eI8u6cWW0D6JFsw_Kt-4RcBdI6TvFHgz3fYLTUQq6CA00pplJ2n8eNDjImkOEFtbLi-vcECCJUL5Mb5BKXM2B5goCmlY3U2yQyRKWmxS0s6t1idH5sgvFBz42Oyp-wgZ-qJtGFwl9e3h-EPTG1L7WctCE2rnpnz4XPEpHRPW6U0d4x1U6hYEU9Db0SSUAv2qXGEz0zH_m_H-xChBLwzNcuKCjs3AJAba4XS-gh4ROjQ2QYg-4cih2Gkz6lQKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترکیب احتمالی پرسپولیس برای دیدار امشب با شمس آذر قزوین درهفته‌نخست رقابت‌های لیگ‌برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/27797" target="_blank">📅 18:32 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27796">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tyrbH20wKI6cVf_Zal9gvIlXYZ8odIHIDa2dbedJHdKyQ63R0ITOjpF3eXD1lxUQm5L_MRSVQibEMvw2jruemm7Xzdc3sK9kEb8GpdcLjUOWXmfAnJnpm7Qh5V96MbiDxn4ozaracXZJj1br3LHzkQabAqlLiis4381XzULpU4FzkSpnxBkCIRPFeAJ4Q902XdEjTb5We5WUAlRH5pM0AJx8qXsOFl0u6i7cxo2-wdN2HNG5XS4fJdXRg2ZDhxxOHWgWD-1n0ee4E4X9M9BWt-AW1FTida1XU4-DnnFR3O-wporz1ElittoML7i-LZb1ZxHfvMKrnSwQYPcQ8LsH7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی پرشیانا توسط کارشناسان حقوقی‌فوتبال: آسانی مشکلی برای‌بازی‌کردن ندارد.
🔵
هوشنگ نصیر زاده و رسول باختر دو کارشناس حقوقی فوتبال: بازی‌کردن یاسر آسانی برای استقلال کاملا قانونی است. درصورتیکه قرارداد او در فیفا و سازمان لیگ فسخ میشد و قرارداد…</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/27796" target="_blank">📅 18:15 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27795">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gy9x70o3bUeC0qtrCqp0RAp0mKKGR5AAxlymHTqselgtDpn-KfJTIXNglTrZKLEvWwc61Ia8K6SyHQc3B-1b0IrjGxHpZreMgf9BM3iGb-5ZDiVEsDCFEzV2SwPXIh-fo9yq1OuP1ZbEtfa1bJF6DWiUlAmDe7zX7tpvSvN_fIioYbbv5gqWKJlnSJOe-yqS08Oxak8MXXNxAHUfyh2VIpVX8KUJdJBOdaNhAxYly6WpLrymLptSd1vjIjRjL2rRVD8U-eg5zI1GOnlfbZmCaQCGILSC4molGawkdq6y_zWlNCArFYkkv7LH67vHzwmgfHOYNQVVajI9m3bqVSCXWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛مدیربرنامه‌های‌محمدقربانی دقایقی قبل به پیمان‌حدادی‌مدیرعامل پرسپولیس اعلام کرده باشگاه الوحده رو راضی میکنه که با همون 800 هزار دلار رضایت نامه قربانی رو بگیرد. منتها این پول باید همین امروز واریز شود تا کار انتقال سخت نشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/27795" target="_blank">📅 17:49 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27793">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WmI8s1kGmVIjwEnevwp_hALYN-woNCNebO1e0ZIwLokK9Wzi9y9YXgiR9VRW5IL5k8c8pgB0pY0jl9bznIIVSyY9uiHvw5QXNy3A147fa2XPC_tYngkYr8uxgqERKjhx2v6nZFFkk7E195ELU-GaDolXhefjG0muBRKmZ867I7Ns8PtxxQjC-41olek8c43twLr9je5j1OsPCq-DdXpuABrUIx8YfRV-xdWAKoaPjw1WXK1sgnQxS-JnY8r8oAk9xw3ma7YyBKPL4Mq3XOl03H8TpPO-kkqmmUKQ3NCNqQtDjVYycdlJ_Su0Vb3VoHNP0Xolvxqhgx5KKIKQ6_TW3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HEuPofLfKCWpxaUzt8qbD_btDypRCI25VlNGa1upkKfzF3aC-J39EVuL2x_4xfYyab6pkod4d3BjqIRK2SwHyCuMW9kl6vePjJ1uMDylBSir8Y6Nm_iwpShhr5vGOMsw1Bnp_Y6JvoTPxzqA0v-3addYoN7CcZ6kgizqm3l2wnPVhupC4fA4g3p543i9HN8ppc8Rt1a1hQ_MnWWw4gzYEFIKOSkQXrChgVERiXgfj0pZxu7TCiVNQrXEFlGrPoVAwWIpfQ6L8iSR22J-7j-DQEarDUr2HQ5ITvJSjPuynXtwl4Fy_J7a6Fugiz2eM5KOwsNhkkEJwXH7y9FQa1wZ7w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ویدیویی از گوهر خانوم که رامین رضاییان بزرگ قصد داشتهه تو امریکا ترتیبش رو بده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/27793" target="_blank">📅 17:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27792">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4ce395aae.mp4?token=T60qcUdP3ZHpO05LNiE080arFxVDTy-G6j5KTeDiJW7vn9I85p3b8sfHZXHBQG7tOK5BA47NQb875bkq53uef5wDdtF8JvOt9oPzHw1I_73KiWjGuYH7zA4EJhkNruzeIvy7SnOW5Cpe07dpU0n9Wj7297w_7V9Qn9AlKFaUASRFFlbj4X7Y70BOw3WHae67P6iasZZbiItsDemg68D8WZfUmuvwZYVi2UH0v28Rh88U4DSNLvLYLSmGefEnwqB2TdP5WYB2G0ohEXzoN0upuquW7LBbLR378c6lbD8OIscT3LuEH935UsTwJzaz_iuUswZLSWqS0MiD4FOrJFp9Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4ce395aae.mp4?token=T60qcUdP3ZHpO05LNiE080arFxVDTy-G6j5KTeDiJW7vn9I85p3b8sfHZXHBQG7tOK5BA47NQb875bkq53uef5wDdtF8JvOt9oPzHw1I_73KiWjGuYH7zA4EJhkNruzeIvy7SnOW5Cpe07dpU0n9Wj7297w_7V9Qn9AlKFaUASRFFlbj4X7Y70BOw3WHae67P6iasZZbiItsDemg68D8WZfUmuvwZYVi2UH0v28Rh88U4DSNLvLYLSmGefEnwqB2TdP5WYB2G0ohEXzoN0upuquW7LBbLR378c6lbD8OIscT3LuEH935UsTwJzaz_iuUswZLSWqS0MiD4FOrJFp9Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
«گوهر فرشاد» بازیگر دورگه ایرانی-آمریکایی: رامین‌رضاییان‌جلودوربین‌ها گریه‌میکرد و ادعا میکرد که حاضره برای مردم جونش‌روهم‌از دست بده اما در دایرکت من درخواست‌های زشت و مثبت 18 داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/27792" target="_blank">📅 17:21 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27791">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fzA5Ep8Mm-v34k0gN8zg5W9Q2fQjztM16DnbD6ky-u4M8y_CIxlyFH9wQ9_fN7etj-s0k5FNo2_9C5Di1dY8wo-9rqkT8qtYkxu4euXMq7GrzhuXuNKdONNHA6m-qm0igSTDqfPRJ7yp4CSMAM_X8LUW9OXqHWpDzJdk-ofNXw8T9N2B-Q-LWmwZf2iuuhlkYO5Y3ozwCib9lfEcMJgWFw6Pf3-lrArH6fVuppXm0zYmKOcbI-bY1_FQZ1IfTGmuX8mMroXVmlt8BNNGDVu8t9AHaZu0E7EJeGseuRJqBI3O41CGOcLv6cOGJ-RRlL50CL-TfFeXPgW4BPLZZOu9Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
نیمار ستاره برزیلی:
من آدم رقابت‌طلبی هستم. همیشه دلم‌میخواد برنده‌بشم و تمام توانم رو میذارم. گل میزنم، پاس گل میدم، به تیم کمک میکنم، بحث میکنم، در نهایت اگه هیچکدوم نشد فحش میدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/27791" target="_blank">📅 17:21 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27790">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SrEkvqdF6bJhGOPLTgAlQwjk2HvF_yJy-uI8WiCtzUZ5M8jxzGCistg48qJgTcZ5IvDImqn6uIglT9mCQHgFBHXKmeNByCeoNCdcZ2zf4JGSqW5GxaFLB7KjLdvwoRvDuie1pm5lSjFZG1SCWleXs1W5D2z_drJThWCtJrsALr2CA85SyM7bBh6iOuafDm1BSf8Ljg6ayHTImOn9ffUPD5SEXf7z-LpCfO_X1jqmwq4J1t_YmeYkWNFttqmEdEzMhjtTGDs1_6bTzDYgI2h6IME83f5Ya-5OSuoh4ir7dMkCYEADoFoD2ac87MtdYqvdatiSRzOomg3exONYC539dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
هفته اول لیگ برتر ایران
🇮🇷
شمس آذر
🆚
پرسپولیس
🇮🇷
🗓
شنبه ساعت ۱۹:۳۰
🔴
انواع آپشن پیش‌بینی برای این بازی
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۱۰۰٪ بونوس رایگان اولین واریز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/27790" target="_blank">📅 17:21 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27789">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d76ee0536f.mp4?token=nCHIgSt7sNq0s_styE3MNKTrz8At1mijBgBGc9WlD5jJOaPPFRxIr3mLjlSyBu-9ls7W_pH6Z85tLLZAkT-vX8RdInspoyHYDiwcDMqYK0-HKvcI8U-G6LPOCq_tPt9FvOM5K6_hOAdS4p8nj3rGmOAci-5oHhzNu6Tha1zi-YeEW1Un71DRzw7Y-5R_tlgjW57DuTeXp3lmJbl9_YGNzJ8ltW2YfcfvJl0BVOf2ObHVlWA5zMWKQU3xiHv2JYTnxab1AlgyZgrbLjaWEScW7de3GOdDiYhttVEb88bifwpgthl8SwK4oRRYGJRiDLuudV99CSA-qV-jyTIPnt78VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d76ee0536f.mp4?token=nCHIgSt7sNq0s_styE3MNKTrz8At1mijBgBGc9WlD5jJOaPPFRxIr3mLjlSyBu-9ls7W_pH6Z85tLLZAkT-vX8RdInspoyHYDiwcDMqYK0-HKvcI8U-G6LPOCq_tPt9FvOM5K6_hOAdS4p8nj3rGmOAci-5oHhzNu6Tha1zi-YeEW1Un71DRzw7Y-5R_tlgjW57DuTeXp3lmJbl9_YGNzJ8ltW2YfcfvJl0BVOf2ObHVlWA5zMWKQU3xiHv2JYTnxab1AlgyZgrbLjaWEScW7de3GOdDiYhttVEb88bifwpgthl8SwK4oRRYGJRiDLuudV99CSA-qV-jyTIPnt78VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
«گوهر فرشاد» بازیگر دورگه ایرانی-آمریکایی: رامین‌رضاییان‌جلودوربین‌ها گریه‌میکرد و ادعا میکرد که حاضره برای مردم جونش‌روهم‌از دست بده اما در دایرکت من درخواست‌های زشت و مثبت 18 داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/27789" target="_blank">📅 17:03 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27788">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">✅
تاییدخبر اختصاصی پرشیانا توسط کارشناسان حقوقی‌فوتبال: آسانی مشکلی برای‌بازی‌کردن ندارد.
🔵
هوشنگ نصیر زاده و رسول باختر دو کارشناس حقوقی فوتبال: بازی‌کردن یاسر آسانی برای استقلال کاملا قانونی است. درصورتیکه قرارداد او در فیفا و سازمان لیگ فسخ میشد و قرارداد…</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/27788" target="_blank">📅 16:54 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27787">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLdsD3WJb8Qo27hADt7CHBrg2Il-bULJ6OfUvsKYzhvbeZYKdg4VQIYQTKVinOx0zNoq1kZ_Rj8V7R_B3EZ_0GXHRRqA7aiJZCoSb2bjnPckFCv41WgNTBf_pHoC7EL0xqy01oph2iKGDT3LC7ob1EI_bvq6utURkH7XBJSkrn9IGdr6V7ZRZyI_YSd7sYuaX5yr17NPRjQmoezQGW4IePARAxR9NNozFMtzUg7OAYCtv3U1I10U8qDVs-Vn9MofUNxtN7-ubjBsFedRA8qcdIfI6xdPMFGdHHs6DVFYxHp--FEODItbEqcRDdlJEmK1H_JhdovgcXr2TiqFATIbYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رامین رضاییان بزرگ تو آنتن زنده گفت تو امریکا حاضره بوده که حتی برای مردم ایران جونش رو هم بده اما گویا ما بین بازی‌ها بفکر عشق و حال خودش بوده و خواسته همونجا ترتیب این بازیگره رو بده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/27787" target="_blank">📅 16:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27786">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F992kacYh7ky0eE9OFTD1ytrZLglZlO-_RlJOokYqnjKdl8C3gg6FZ98zB03x40846iXvvQt5aCgeEwm_56_3XAEtRqO7XP2SQzzHtCuWQEZCeH-eNoZ4hXOtd6_FByOkyDvrJh3afMHjC_Ds96S_wNo6HQibmo88vjV1To5WMv3uWabS6PES1Tn9tPxcWLAOgguoXHqi4Kgx8dOmotO4jClmSay2-lznusU5CyQPeK_wfCYUL33gdqK4bKT8VrmgHNQcTjdtAXzcTq7RRd5GLugExLrY2i5zlIT8O0kUX_OugvwEnfZ-TOrJDZ5yopsT1GBNmTXPETxZde6jHOkBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ طبق شنیده‌ های رسانه پرشیانا؛ اوایل هفته‌آینده‌هلدینگ‌خلیج‌فارس مدیرعامل جدید باشگاه‌استقلال روانتخاب خواهد کرد. محمد رجائیان مدیرعامل‌سابق آلومینیوم‌یکی‌ازگزینه‌های‌تاجرنیاست و درصورتی که هلدینگ تایید کنه مدیرعامل میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/27786" target="_blank">📅 16:32 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27785">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JbcuHMmXQGF2AQdFHjuQ20Wk3JXFkwvK1iccFC5vQAXZbKtsjMpn5xQHgQXUqh6JfuRScENxFatjkAoRZodEwZOcP7S9-naBpl7T-5dUn1RxUBx5X758LthC9xt4rFxZOyRvNLyfG1pX_FxoPhEOFsnm-C2kicEYTW98WBeWc11M3zigSYeWwh2q79ayzKgQYVyuFi_zJR1xXOMEegOkRW-hTutwmKFKS08e2urHllm28Yg6_-7csT168Qz4_JH1hBo-0VsR2k7ugCA_5i0l0a0KmOPXWbTW8m_x_NOP1IT1zgFv0N_SdZPmaJPUw3FTxlbv3hLj64nLoT92g7xoKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترکیب احتمالی پرسپولیس برای دیدار امشب با شمس آذر قزوین درهفته‌نخست رقابت‌های لیگ‌برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/27785" target="_blank">📅 15:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27784">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D3GplRFnQd5WPWeCu6vvdTzDNnU4iKLwAIJF-VFm7J2dqFnna-kH2aiUqojD9NDaE1u9ve8io9fS0Zblq2xOSfiaH3XslMvGdEhpbXRxjn86vu2vz0kCsHJutXCrOT2CY6WelNN3vmeJ-wUj9KoWDDKCFJZUb-54R9GEqn4ctIxY3Adz1miFtQRBP50sT9o00f9VO4hep-ZuA50UaxMC5L3fG_hIWmDphPeskzN07LOi73kGumL7co9Yq0GVRgwnSqUe5O7dRy6MQwOfJRnXh-YE47DqZ-IICkkGtKPlYWDasQA6I3A265Pei0hzufTyLt33bQBJ6zyQ0LwATQZ7Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خانمی به اسم‌«گوهر فرشاد» مدعی شده رامین رضاییان تو دایرکتش‌درخواست‌سکس داشته و از او خواسته در ازای دریافت مبلغی باهاش سکس کنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/27784" target="_blank">📅 15:04 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27783">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4420878c6f.mp4?token=CWyjJrpRFHMO3ZBHoYpO7trlbSVeQtG2o0unuZLFBoJXwYmCDP0W0UBAiBGM4caHF4xpUIi6J95VpVXugYRwVmHEx4APzW38m8vZVMW8-pQ_iSXu3iN1bArvUNnDK7xDqiVKbaoqxw-WqsFoaK17F7S7Bc54gzCdLvYYn9ytmQmcgiZzOS_Nz20A5bbqOdUNzM8V3RiOmCl4KgPZGX6an-yhCsOJ7FudSrzzvlkenf3JM2j7PBJMz5WZ0DwpcfFZrMBiDJz4FksRM0TQl0hdr_b2lFOZjcgxLqBb4rHjwV3jmgQBvT2pQTFSMwMh6yOC02A9b9SXEim_YPbZ1Kb7Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4420878c6f.mp4?token=CWyjJrpRFHMO3ZBHoYpO7trlbSVeQtG2o0unuZLFBoJXwYmCDP0W0UBAiBGM4caHF4xpUIi6J95VpVXugYRwVmHEx4APzW38m8vZVMW8-pQ_iSXu3iN1bArvUNnDK7xDqiVKbaoqxw-WqsFoaK17F7S7Bc54gzCdLvYYn9ytmQmcgiZzOS_Nz20A5bbqOdUNzM8V3RiOmCl4KgPZGX6an-yhCsOJ7FudSrzzvlkenf3JM2j7PBJMz5WZ0DwpcfFZrMBiDJz4FksRM0TQl0hdr_b2lFOZjcgxLqBb4rHjwV3jmgQBvT2pQTFSMwMh6yOC02A9b9SXEim_YPbZ1Kb7Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
دیشب‌عروسی‌هرناندزمدافع‌فرانسوی PSG بوده که حماسه‌ها‌خلق‌کرد. امباپه از دیکتاتور به گاو چرون تبدیل شد، حکیمی دی‌جی شد و دمبله خواننده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/27783" target="_blank">📅 14:44 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27782">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AObI6SftixGwqEPLlaYX2cuc6oPNJjlYNuWQKXhX5ro0gxY0m0kkBvgCPToUT_FnDPPDyzzalIxewtpT1vVGPoCrnwlp_r4CNe8Wmr3jHZM3X_tbI-kxYgFxVgBDxYYONMWBwrJ4Nl06oXVQxCUf17Jynq9FxXGqKugHn3xf5DAxyPPW_1nS25EGBMw-Nb4kmAndy7MCYvkaAOVQyKUYvWLwWbq4xh_VeAlfG3ekPWW3E02pjKzGwjiMz31SBgiA4L6oTUvGT3jn2QBpAVB8jRl8bIXMgzvz3OCJ5OKLse_Fw5m80CFOfrXGwXMuHG-4jyn-XY_TGxdOQzsQDQYZnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
ویدیو لبخونیِ لیونل مسی فوق ستاره اینتر میامی که خیلی‌هم وایرال‌شده مسی به پسرش متئو میگه: متئو دیگه‌چی‌میخوای؟ پول ندارم دیگه همون هات داگی که خوردی بسه دیگه به‌همون راضی باش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/27782" target="_blank">📅 13:59 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27780">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kze4zntFW01T1zHhI9H6ZPz0f6lSV4g4JwqrwoFQHdX70zMSrdqIQdr9JVyy26tTkTf0EoRpu2Xu3o3lzwrK9cCUQbp7jpajsmFjUz0OTBCQOcVtPmB7nxcWBmGIUl2i7Igm2GK592WkNRXWHyERly8yFZSLyjxGbaqIVbW_zH9NbWIpJLo9VgPoDw8eUrlDMVP6EJ3DQNA6KuGXnPSMxuUHthi0S5PqJdiWDx0RpJABamr2BqYggUb3KyZ52isyOvQ_aaaTaP-sgpH5DaNCXk1Dm23b7RgsfdBoAozWTmQt0rBw4rdQm1tycaWnMCHyt28tuJHX-tvUnKQnjQEpkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باتوجه به‌ سوالات‌زیادی‌که پرسیدین؛ بعداز پیگیری‌های دقیق از مدیربرنامه یاسر آسانی بااطمینان‌ کامل اعلام میکنیم که‌فسخ‌ قرارداد یاسر آسانی درسامانه فیفا ثبت نشده و تنها یک نوتیس برای باشگاه‌استقلال فرستاده بود و هیچ‌مشکلی برای همراهی…</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/27780" target="_blank">📅 13:27 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27779">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">📊
🔵
سعید سحرخیزان، اسماعیل قلی‌زاده و صالح حردانی بانمرات 8.8، 8.6 و 8.1 سه‌بازیکن‌برتر دیدار امشب استقلال مقابل مس شهر بابک شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/27779" target="_blank">📅 13:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27778">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a46566583a.mp4?token=nGCFCVRJbX5IGx4ao0B-Krm_mH4Axajo80mwgSzpxkLC7WflhqNy1lFQcaaMxHvOP9NnR5DkOFkkGPsLTUNY_ImmlOesIFjvJK9MnSjdRZXdR0mx7UFbboZjzvYSYbcnRCZvdlE0Ftm54fIR8ZAjKLXo-Be6hsaf5Z-uENGjwH8aeIDib4pwdC2Fm4n9-RXNhYVhdCmua2oD_R32e6M56Anzcfd3bVtbnvdtFS5AzKwvBfoV_sKRQz86XtiiCKhm_JmVBeTABFYwuuFoNxnftW4MplUp4UU867XHPHKWrgvUA2JX6GFxG-v2pTmaSZm87qYrcVQfWgBLF9F2emVBjoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a46566583a.mp4?token=nGCFCVRJbX5IGx4ao0B-Krm_mH4Axajo80mwgSzpxkLC7WflhqNy1lFQcaaMxHvOP9NnR5DkOFkkGPsLTUNY_ImmlOesIFjvJK9MnSjdRZXdR0mx7UFbboZjzvYSYbcnRCZvdlE0Ftm54fIR8ZAjKLXo-Be6hsaf5Z-uENGjwH8aeIDib4pwdC2Fm4n9-RXNhYVhdCmua2oD_R32e6M56Anzcfd3bVtbnvdtFS5AzKwvBfoV_sKRQz86XtiiCKhm_JmVBeTABFYwuuFoNxnftW4MplUp4UU867XHPHKWrgvUA2JX6GFxG-v2pTmaSZm87qYrcVQfWgBLF9F2emVBjoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇪🇸
رومانو هم‌تاییدکرد؛ فران تورس با عقد قرار دادی 4 ساله از بارسلونا به PSG پیوست. پاریسی‌ها 55 میلیون یورو بابت این انتقال پرداخت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/27778" target="_blank">📅 12:49 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27777">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FoAVNLYJsQhbzLOxfM1Jb4DybSW85ddkOMYXDOuJwAsGHbyBTN0rC6bDxbS9C4XKQhPqFJgi2KpQXOy830FLgMvqSrGaakoitL5CnKk4MdF6xiUX8sWHUmZsIJeNvtPCeYthiLnGtG-KTrAWhvqMwUURFcS7AKUfY7eCYmOaufyTHUG4al0IscZ0F37Zr5OPBg5p-YYmWL8Ikqy0h-7iv_njKDoysj85SXzwmqNSetUDog1c5l489YPSyi2CbNcNKAiyuFJvFk7lTCxQp8DzvOv0pGg57KCyLWeGhm18BudogxJDtLQruREf4JemncTcgKstZoCUrploW9H2MQwq9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ مدیرعامل بانک‌شهر فرداصبح بودجه لازم رو برای جذب محمد قربانی دراختیار باشگاه پرسپولیس قرار خواهد داد. مدیریت‌باشگاه پرسپولیس‌آماده‌اندتاسقف 800 هزار دلار برای محمدقربانی هزینه‌کنند. این احتمال هست که مدیریت الوحده یه مقداری مبلغ…</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/27777" target="_blank">📅 12:45 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27776">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5fwZgAvzZuWdytjYMM-wL92SxCttp2nQims3sD5KLqVecMQaOnxqv_uHwYeR21Ja810eqLS3HN5T-ygljZT_6inseDIRaZPA0iHSZdUA8wx_AtHAR9JZB2gR3vAmrXipdOd6kumLLGKm645uTIvhfBhTxxU8x2qvmlI7ETuiiwPoBowIfZBhJI-Fmniz5uel6HdatuUqtoQoEysK_5Jmqj-6jqvSAhxP1_p-Uw7OYXdIom6Z7JlCWC98I69Etp6RhG1ZobpNAk-6ZxL5L1sHMbdH6tS1lVERLPt1rZMeeT1JvipGP37WbsiBpXT3mq5TV7crQyjXODU20kBeu3Tpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔴
نتایج پنج دیدار اخیر پرسپولیس
🆚
شمس آذر؛ پرسپولیسی‌ها باچهارمین‌پیروزی متوالی مقابل شمس‌آذر فصل جدید لیگ برتر را شروع می‌کنند؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/27776" target="_blank">📅 12:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27775">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5920f02928.mp4?token=HnDu_aY5YBI4C_7w4bfWpUMHMy41oI_4IbJ6KOucYGpSK9KJy4fAf8dD0Z0x8F_OWrjqsECBUrKSxMBkziDWiudxwoCssmU4NMiLD9Bw0oMhnhxx2quvwKdDsDcONbmEQS2XBiPj9gmRjyNF04WYDSz7qJ90iZBwXdVBMou0bmhA6pynTnDEO58DW1TlBQqvEd1sU_rxgoGkVJOoeSSfl8EjsablJlLfA0A__1RYkt-ZJPeObdgqLroIDsghBNeQdZb_za4Rk6KNoRpZHz9UjpDbpJAcZXU-BMimHIBloOAeiNxi-MjGRuvsIsBpUXR1SqjP6Zup77z1GheRpQ284A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5920f02928.mp4?token=HnDu_aY5YBI4C_7w4bfWpUMHMy41oI_4IbJ6KOucYGpSK9KJy4fAf8dD0Z0x8F_OWrjqsECBUrKSxMBkziDWiudxwoCssmU4NMiLD9Bw0oMhnhxx2quvwKdDsDcONbmEQS2XBiPj9gmRjyNF04WYDSz7qJ90iZBwXdVBMou0bmhA6pynTnDEO58DW1TlBQqvEd1sU_rxgoGkVJOoeSSfl8EjsablJlLfA0A__1RYkt-ZJPeObdgqLroIDsghBNeQdZb_za4Rk6KNoRpZHz9UjpDbpJAcZXU-BMimHIBloOAeiNxi-MjGRuvsIsBpUXR1SqjP6Zup77z1GheRpQ284A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
حضور هر 3 پسر لئومسی درآکادمی اینترمیامی؛ طبق گفته نشریه‌آاس قراره که بزودی هر سه بازیکن باعقدقراردادی‌بلندمدت به آکادمی لاماسیا بپیوندند.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/27775" target="_blank">📅 12:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27774">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LX_fwcd0dS9ncGN7wRtOhU0h8d7_z2VHhypjDPdhBUc8eo-bLLFbafN8VtXVIgLVjzkPxgUaXMvelZHr5Uf7vTUGntQ8xGaJgSCY9RsG3JN661FYbui73zm2wN8D-BBdFDaBBUTKZ5GkiS6bnTM8sy6yQwnmVB401B0YOYYSkgu3j9bRpopgs-5F9lqL5-P9DKLLJkCncJi4SsVAtNKVNwMlQ2t6oe8ax0YeNiRqqjVspd-nSVOBbAk2Ugsa1Yntk6kYaV6m1i60NXw1Iv7pJd9FvqpFhj2TmhidkJV-MvC2rgsshK5YZU2OYkpmXgBb5bi-psFB-zh1m6mW8GHoQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌‌امروز؛ از مصاف شاگردان تارتار با نماینده قزوین تا دوئل کلاسیک میلان و منچستر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/27774" target="_blank">📅 11:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27773">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6R22PfuRzNfVcgCN6G1sfD8CDZQ0BfbSswpR5hllVnEBBsduJ6dY6zBDzaHihRUweG6NY4o5gkhDkdLMUraTGvlaJRkfTCVPTuVqSfUQ_skKjZJ9FbE3lYqksFY6XzPASNotK6n-0kqh0SI8nmVThpEN0gamqYFTrhsckpy4j3xynTybVl6RjzCIUlOvFmfb1tM0pT1gGjLrWK2Xd4JeFKz8tvKbCuKz47jhpSnenRdsvJW_EEffd4q9-fVXbl0O4mjC5vGjDT9zm9iTxodosAPvr3A8fRZTIfNJ4fwrU2EyLy5oErysWiBYVghHYBilJR1b8B4ea8MMGzMOdYK-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
👤
طبق شنیده‌های رسانه پرشیانا؛ باشگاه استقلال تاساعات‌آینده 25 هزار دلار به حساب جوئل کوجو واریز خواهد کرد و پرونده او نیز بسته خواهد شد. همچنین سهراب بختیاری‌زاده بخاطراینکه نازون به‌فیفا شکایت نکنه به‌مدیریت استقلال گفته مشکلی برای بازگشت نازون به جمع آبی‌ها…</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/27773" target="_blank">📅 11:26 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27772">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eECp6p-tcD4YRbL5075kLMu24LlqxttnrcPf07pNM6HtOh11yrbACpXD5qe9iohn-v3FiEONBLgIYZlS5bL5khmhwo1w9UjkBYXdfhM0pvMmg5vVb0me6OUYt_9Cj7v-OWJzyurlxv2cDvAmBaJy4BVK6dvUqU1M_Zj3Ore07S4YuYy7FdIZE36oVShNPgk6DJyHKHMJfZjYvCma4p83YWyNEfKBL0gNCy_UjOPX8eQkG_kCSjwNn5qsNlOkD6cQWC0Zc6pFxI0zKzXoH6aXsaRKIiEzuCzq-fqJoc-sZBXddmGUSz-QZ4RN_nktktPTm4S72WbRAn7kS60UhAEzZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی_پرشیانا #فوری؛ پیغام جدید محمد قربانی به‌باشگاه‌پرسپولیس بعداز درخشس در دیدار امشب‌مقابل عجمان: پای توافقم با شما هستم. رضایت نامه ام رو بگیرید به تهران خواهم آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/27772" target="_blank">📅 11:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27771">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1Y4ssT0rrBz_wexRae9APFqZURUvSeRe0N3GqogMCVVkHGbFE95aOxLS0ohZlQuMpmeOJgumL6_cu9nIDNbgIEI4ll1xBGFhBCIQbA_hjeLSWtqbfOF_hyFnaDosgoC12YoGOYLu9QFPdaO6QGP6C1fJMLoNPw45FpC3bxtjbxo7UmgiB3EkfX5iOlfZTlyAasObUXZui6w0fThCdoDHDN6tNSEv4KHibo4xHNtfBLRZKx42dTaUjcZFYJbD9G7urACRXH0t81ifMGhxWJTweeuZe08RLVeVeEjs3xFSXpAh6ca-X6GsuIEP0MByTlOqZFXLSGFGJ8A-L6HNBISYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
لامین یامال و دوست دخترش در پارتی شب گذشته؛ به محض اینکه تمرین بارسا تموم میشه دست این بچه رو میگیره میبره پارتی‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/27771" target="_blank">📅 11:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27769">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/936415b58a.mp4?token=HxlRvY3_6v1kDk37-tXT6Rzhb0V_m24CSDbANZSsTyJa0iS7ZgMMSnxqcF31wC_-zADy6c1AJbm4QpnnuNIdJvq078cXO6RLJlmxqsX_0Q6cMPzxhlpdtdrBNUb8YtiO_h7esZ6l77CRtJrfleN_DCW65CwtnyWqZ6KIPZ_AT5ZRWIrA9i3H9dJ8t6lowYMvWRXIrsOukZHpEgi8TXJy2Uy5mZbNAkoixMzmYR4S3a07OF8EQ1CMewrXwGdb5tCE5eYsjG0iXDcRSR-lKm9UIW6vPCrUm_tmBYcEz84Cx6s7K4zBtB-cIN55YG793G-anN4tDB9NifzzdFD4TippGlUQwzJC5dCZ6hAY6GhtNjmOms2mhzlTkUOVaJbgMmUDFLsY51MyfCgtoV2a4JFzn01A8Z4ePlddHxinn8amUeLFAMfhQKleymcg5ntxR-F2dWSirU-cIbI2DDrYPmeRtzm6RpnJ97yZEYNs_F_2V7JpyGb_TPKa3Vm3puUaeOr6LslEABvzId6mqBWmeq8QHVVmZRXq92s412u5_uHN8Kh-agsCNh_N_OuARE_Oml6R_kAOW4eSxfYHOG1kfvGxC6GH8eIfHGPgDGX9t-fEXQtm5MNT_HiYenvN0cQ17RoeNA_ykvyIkeFXnWNMAyci31F2dUVQPiRdRgHBkncC4ZM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/936415b58a.mp4?token=HxlRvY3_6v1kDk37-tXT6Rzhb0V_m24CSDbANZSsTyJa0iS7ZgMMSnxqcF31wC_-zADy6c1AJbm4QpnnuNIdJvq078cXO6RLJlmxqsX_0Q6cMPzxhlpdtdrBNUb8YtiO_h7esZ6l77CRtJrfleN_DCW65CwtnyWqZ6KIPZ_AT5ZRWIrA9i3H9dJ8t6lowYMvWRXIrsOukZHpEgi8TXJy2Uy5mZbNAkoixMzmYR4S3a07OF8EQ1CMewrXwGdb5tCE5eYsjG0iXDcRSR-lKm9UIW6vPCrUm_tmBYcEz84Cx6s7K4zBtB-cIN55YG793G-anN4tDB9NifzzdFD4TippGlUQwzJC5dCZ6hAY6GhtNjmOms2mhzlTkUOVaJbgMmUDFLsY51MyfCgtoV2a4JFzn01A8Z4ePlddHxinn8amUeLFAMfhQKleymcg5ntxR-F2dWSirU-cIbI2DDrYPmeRtzm6RpnJ97yZEYNs_F_2V7JpyGb_TPKa3Vm3puUaeOr6LslEABvzId6mqBWmeq8QHVVmZRXq92s412u5_uHN8Kh-agsCNh_N_OuARE_Oml6R_kAOW4eSxfYHOG1kfvGxC6GH8eIfHGPgDGX9t-fEXQtm5MNT_HiYenvN0cQ17RoeNA_ykvyIkeFXnWNMAyci31F2dUVQPiRdRgHBkncC4ZM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ درشرایطی که ماده شش فیفا به برخی بازیکنان اجازه‌میدهد خارج‌از دوره نقل‌وانتقالات ثبت شوند بندچهارم ماده ۱۷ به صراحت می‌گوید باشگاهی که با محرومیت دو پنجره‌ای روبه‌ رو شده، نمی‌ تواند برای ثبت زودتربازیکنان‌از همین استثناها استفاده کند وبه همین دلیل‌باشگاه…</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/27769" target="_blank">📅 11:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27768">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jq8QY5MSJjIR5o5NDj22UTIMtAdnqDAD5r2bPuzDKQUImveJjK3PqEQnmmbNZZJMhgkiiesDXuxEt5wiWbcsL3LAfmrhzJn7QMCdPYVtVsULAiirYxA4PHSutJ6QqF0_ALHxG4S37YbAStnysW6fYOeMR4vxBxOsQKto6P3x9JjIcdN3zi9NEAnMVUnCavFVSJpXS4q5MEHkCcu8iiwv2nZVYmouE9rgCadaJG2atzCho8uxwTmi_XnJbcRZs5d3ynI-HM7KneuZRW5jNOqoCP-Hmh45FbcTYciBbiLDYbFbk0FZU4oWcPYNpr2Xn4CEcBL7ZgMCdpS4d4I75RIa1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ امیر جعفری مدافع چپ گل‌گهر در هفته‌پیش‌رو برای‌انجام‌مذاکرات نهایی و عقد قرارداد باباشگاه‌پرسپولیس‌راهی ساختمان‌این باشگاه خواهد شد. حدادی با ایجنت او مذاکرات مثبتی داشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/27768" target="_blank">📅 10:55 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27767">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4107ef1526.mp4?token=bzOofk-cTaLDf67zHJfi7xVtVssLVXrPp8mmOT0E8md7z3Zmoe0049moGQztlHBH9QwoxyIsle0CJ_02vQPZ3IpDEq4HI2r_2wyKfWelz29dNSQ3uNJ6ZoTaMoQxOSKoul8au7kHlAId7mt0sMKvzxg_XxUQWpSMm_eJlp8F5J1bR113GFa_zg9bhJKe_1R6_72D2szM2NqYW7AisZWWVCJ53Q6RNAJ89eKnstiz4XInJJ2kTN7Ojrg-kTvc2-hqD9sbb0BajrM-eJAoRCLqEUf7anyYPoOVaFptcmbcR7dky7Bq7OT237QvXT7VwEMB7quMYttzeVAIB4P5frbUdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4107ef1526.mp4?token=bzOofk-cTaLDf67zHJfi7xVtVssLVXrPp8mmOT0E8md7z3Zmoe0049moGQztlHBH9QwoxyIsle0CJ_02vQPZ3IpDEq4HI2r_2wyKfWelz29dNSQ3uNJ6ZoTaMoQxOSKoul8au7kHlAId7mt0sMKvzxg_XxUQWpSMm_eJlp8F5J1bR113GFa_zg9bhJKe_1R6_72D2szM2NqYW7AisZWWVCJ53Q6RNAJ89eKnstiz4XInJJ2kTN7Ojrg-kTvc2-hqD9sbb0BajrM-eJAoRCLqEUf7anyYPoOVaFptcmbcR7dky7Bq7OT237QvXT7VwEMB7quMYttzeVAIB4P5frbUdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
🇦🇷
کریستین رومرو با سران اتلتیکو مادرید برای عقد قراردادی چهار ساله با این باشگاه به توافق کامل رسید. رومرو در دوهفته‌گذشته پیشنهادات دو باشگاه آرسنال و بارسلونا رو رد کرده و گفته بود به سیمئونه قول داده بعد از جام‌جهانی‌راهی اتلتیکومادرید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/27767" target="_blank">📅 10:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27766">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GxQmLi1HmQSPjAfcNdqYLZuETMhD00bZ64ZBFg7Cc4mM-rsfju-NMFLLXszOkeA7yzDAjMo7c11qw_ByESclz0mUWJ7UvntQ7tQ42Gq75JiFEkKDM6TBfE8HFo9HxNjP7ju7MXV1T5PR1zbHjlxz1NFAwE-3CfU7KxVCDAB4Ak6F2yzcmuGWS6MuUiONyXLaTjU_R_gYu9D28Y8DczgERKYnBvquml9wmO75Dme_bNIT3CL4d1rsydILY9c37UbYhNbS1-XRCKg27TRTRTpw73C_ogTh2KxC9AWGjs-AhmTHRrjTOuNBBgnwlB2-nVOvic3Zj9_qTuSuKW37o0-kKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعضی‌از دوستان این تصویر از بسته بودن پنجره فرستادن و میگن‌که‌صحت‌داره پنجره نقل و انتقالات نیم فصل نیز بسته خواهد بود؟ جواب خیره! فیفا از نیم‌فصل سال‌گذشته آبی‌هارو به‌بسته‌شدن دو پنجره محکوم کرد به این شکل یعنی پنجره نیم فصل سال گذشته و پنجره تابستونی امسال؛ پنجره آبی‌ها نیم فصل بازخواهدشد. تاریخ بسته شدن رو نگاه کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/27766" target="_blank">📅 10:21 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27764">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B2ud3-uOPtB5-R-SuTWikNb74UQqk_wVjEVx3aXp2gsqZuTWy_ah681zOD_uql63lsDC3FiCBwUMsX2us7MDlJ1SJv1JVZbPZvBvXJWXslBB6FKGuSAYcoe4YRbTaLQFORibCbpyQ9W61Q-rtRdOYvV0hSZDTCgQesDileoiKLwGJ0vqd766x13xj0J1zmZsbCvy2eF_d4ogp9pp2X_Ou5z3mAoBuUFdf5-RSBHtxyekDYCS33r7E8amZ_eWG7Iea9smf_y7ZtRm_Qic4K7OjbS81PBzNkjKOh9CqvnQJeMx__eN-G4Mxgh96HQcGC_flkc1ObhdkEor7nArOg7-wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FnOEQ-xzHePgPI3qEbuGncmevwOof1pXNYDAMlQkPKjk1IJhIe1SDzWVmCp6uvDxgpiIW-xqF1lImIYXo2FiGaG_VMuOw-ouqXNx97yFv-9iKXFwGMK-20vx-CjiH8Px9wt7aqbWdDYpfNAgPgDTD-4UmruIEZ3MHXNekHjdgeCkq_4k6mTyY-L02KaqMQNtYjYXwtMxm60RHCuQWFE8swzt99XJUD_4bwBJERYTh2H4lzIJE5b2NwdFU2PqBDHQS0piCkPiLVhP5Zley8whIOhXUz745gmYdmc10NAwKnamLoOZVJcR2zbeJXz2fFBFqIUnZnXjNc0e6ELdHncKAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
لامین یامال و دوست دخترش در پارتی شب گذشته؛ به محض اینکه تمرین بارسا تموم میشه دست این بچه رو میگیره میبره پارتی‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/27764" target="_blank">📅 10:04 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27763">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NIRHc_UKNE3DU4XyH9t-UHtbNNqS5HjCAlHFJ5-dU5dJLZPlBcdofpud4gNINQ1Rh_vidM60Z2ASxDMlLdfHlB9JoU-p_qDNgQvkujUhQSpQF9TxKDWEvlnEALzCZwfRhMiu1UYHT5Wmwo0yQTdtECPe68C6-c0G6cs8fLcYL0fccmlKnw-kPUmUcvZPu6tvnkfpk1MpM3ltKOujWdvZuuZD1E3kYOjYeTkniOMaSQTSWLIXj3bcWaGylg1XEseedLwhPzhlgMC180MAF57kau6W3Nheo4LLz1vaQe5FOFKO1Fd2HNHtVy0PMYh8NFlfHklEFZFXawqB0FjWhIPzmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
حضور هر 3 پسر لئومسی درآکادمی اینترمیامی؛ طبق گفته نشریه‌آاس قراره که بزودی هر سه بازیکن باعقدقراردادی‌بلندمدت به آکادمی لاماسیا بپیوندند.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/27763" target="_blank">📅 09:48 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27761">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWIYbnKk2eCA_M_IR34yqdvZGZPPRtiyAHNw2yJ1IiVYiTmDK8t5Neapb4vErEyTEeW8YrdC8mMzu_h5VGgaGMI3e2y-CR0xLnz-VkCEJr44liJ008DoJXGRU-g2AZ6WCBQ_m_ssd-L_Mnga9n2Ps-aJq1gennuXw0XAiraeSlpyv6cxsiX_Ycg-QmDq1AVB4qZZPs2tKnnTPV9LT-meHYexGIkP49D946BWddrHyJNSX_sGss3POo2uqWn3vXpj83MJvrzLFbmnJgDt4J6mMlP5t4WCj0kXLI3XhJmWRuvapTUV4dZsTLCg7alRphtx2aNrV1rFTsBblHOu2ABRpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌لیگ‌برتر؛ استارت آبی‌ها در فصل جدید با برد قاطع مقابل مسی‌ها با دبل سعید سحرخیزان؛ فرعباسی با کلین شیت فصل جدید رو شروع کرد.
🔵
استقلال
4️⃣
-
0️⃣
مس شهر بابک
🟠
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/27761" target="_blank">📅 09:22 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27760">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kAG8nOjYCWDKy6zyccdNUiuoKfrA6JHZDlnPvbPjkxur1XUsYdzBz3VqhEK1UOLF657bQHPSQykF2-aKtDuT7xJaN5-uvb30sXUTUdOPH50ZFc7ttXVHbafVVfFGTW814AwR_DB2YYz95-6c7IiTnXfplCO_hDf6Rq0rdgtQMchUUQlj3gk537xRPCDsAhRC9TE1WnJMqHudGavVdMyQEIlXM6Fq1FIJLxZI4UiSWexoPG25dX9S1GuMU3Ye0RQBe62189c-4RjkpKzOkNfL0MsJBfnfLHFlrm3E_5Qcoob_xJedjnqszI_DWrQkra2CB-DAqm_HpRH--lEKCegmcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ مدیرعامل بانک‌شهر فرداصبح بودجه لازم رو برای جذب محمد قربانی دراختیار باشگاه پرسپولیس قرار خواهد داد. مدیریت‌باشگاه پرسپولیس‌آماده‌اندتاسقف 800 هزار دلار برای محمدقربانی هزینه‌کنند. این احتمال هست که مدیریت الوحده یه مقداری مبلغ…</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/27760" target="_blank">📅 09:10 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27759">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3eb80a731.mp4?token=Q-Yfn9BaTZaJUlybX-WsdBWXNcOV_ai7_FxuSpzVb_tRiP5JE7cHa77oV1al_xAwVUmpC81T7PU39UaCH3DEz5mps9AMN_182ftMGMNdQozGrDtHGswjHog340chQUy4fRr8Z_K4UyeVtvORWfHqsJ-ldmJudMUcrNEh4_KmWdcsXIkbmvhGnTpGddeWoJjXgp94db59pIT426S60-B0QAirgjd-Jp3GVcfj5Ktx0_z9LowQ4c2d2dLMD_BxC9qua3K14vkF6zGa06MkP2tSww5N7jkVdTIJVmGl9Jn0e3KN6nDmUwwHKHjya_kQStV-tEESRZfvwmZcEJ9v96GOfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3eb80a731.mp4?token=Q-Yfn9BaTZaJUlybX-WsdBWXNcOV_ai7_FxuSpzVb_tRiP5JE7cHa77oV1al_xAwVUmpC81T7PU39UaCH3DEz5mps9AMN_182ftMGMNdQozGrDtHGswjHog340chQUy4fRr8Z_K4UyeVtvORWfHqsJ-ldmJudMUcrNEh4_KmWdcsXIkbmvhGnTpGddeWoJjXgp94db59pIT426S60-B0QAirgjd-Jp3GVcfj5Ktx0_z9LowQ4c2d2dLMD_BxC9qua3K14vkF6zGa06MkP2tSww5N7jkVdTIJVmGl9Jn0e3KN6nDmUwwHKHjya_kQStV-tEESRZfvwmZcEJ9v96GOfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پریچارد کولون بوکسورسابق‌توسال 2015 آسیب‌ بسیار شدیدی به مغزش وارد شد و پس از گذشت یک دهه‌سختی‌دیروز درسن 33 سالگی درگذشت پریچارد در تمام این سال‌ها توسط مادر و پدرش نگهداری شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/persiana_Soccer/27759" target="_blank">📅 01:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27758">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZogJZSm-_RyeylrNFYew8pig5-T5tF_TZUA7pC5vQ_0ny1FGqrdhJicYwQbFtmYUu4-1nJu3-bLdAAOiI8GT_R-7Jj-8x8PI7leyeXFKfDIteWozG2jJqFOFVT7-hvqrGfvRXcpKA3Z6jliRog0dpWPKbu5lmqz6G8EAf43tyzZOH-FjjpIYVoHbG9aFUa3jXW99Igp4Y7DNBBuYUzp2EnYx7bRT_mJAJCShiCAZbWDBUamCzNl2lAcSPrxi_iQWkev0d9c5Kk71YYR4a6kvI9DUZTsgGOfinvpTKXrn4hLNUQoC6_qy5BcJpYFbUuWNu85fYj50MsGQO70pED_pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اگه‌میخوایدواقعیت‌ماجراروبدونید کسری‌طاهری و دانیال ایری هیچ مشکلی برای عقد قرار داد با هیچ باشگاهی درهمین‌پنجره ندارند. دیگه از فیفا بالاتر که نداریم. استعلام‌گرفتند گفته‌مشکلی برای عقد قرارداد با باشگاه جدید نیست اما چون مثل انتقال پوریا شهر آبادی و پوریاپورعلی…</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/persiana_Soccer/27758" target="_blank">📅 01:12 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27756">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jGb6BCigplHLcn-dVNxwwALDugBWaG828uIlCLMYCtFFoRbWYPr3cBmBEcvSJjXeUHzcuUVwAkABONujjAtfZkqjQMjRk7GNefORlutzJpiDkwka0a0YT-KZEnrPOBg5yJe1hI_ehdzjYbfY2qJrIxBfJaA5awbPAtKayr8clhr71bfWLQ7UXVFscNJqgLlfTng_cIVHxnvRiZmhyhb8Q0buU-kMY9YsYhnRhW1C3NVfgKpcxRhibQt1DR59k6YErsq-e-2ciK44l5kqRxOJjHmpyMEbc31xg8pCnJNBNKaplhU15tj0uFLX0vaat6eiHy4ZB9SY3lDWRu08Qvl-eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌‌امروز؛
از مصاف شاگردان تارتار با نماینده قزوین تا دوئل کلاسیک میلان و منچستر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/persiana_Soccer/27756" target="_blank">📅 01:10 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27755">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WLIdlmspxJsAYzdn30rF6DVDG1SeMzOUSohz7QAE9j1G8CYe5Ro2hE_wmGOWy2Bb9fEYmKJ-rZzdmOCDhYxU53UV-_C9_C02XjJszwGmAECBax5nyFGyR9SOiCj58oKu0ptK_295gA4-bz-b2j_jLvSrQDe73NpawHoPE3CpORmHBj4p4zhWF4Tr4hJherlDxsMoyNg291jc3MzWEM0BTuOb_7iegFJvG_3-GJmO8oGsxr5b_r9nCtvKxtTTfBmCjx5vdY8UqUCuVx3cQW9LpzGFcgvMuviBnkvUNxo6cePbYmrE5sleP9t9Pfm7UA2ylNs41VnmA3j_1ekr-9vWWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدارهای‌ دیروز؛
از برد پرگل آبی‌ها با دبل سحرخیزان تا برتری تراکتور و سپاهان در گام اول
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/27755" target="_blank">📅 01:10 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27753">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BhPKri69ZxMZH5sAuZvJwSqAwFwYzCe5vSrVgaQ_pXpy46UlGm8kUxRkrRsI7CLSg_qWZIvMJ-25r8gxbd0K10O6GDsBdNwRuScZJy15etACofJxXdJMENTu9oe3hrHlf9ejhrwhwpPuPrvFFhsu3BKwFy6n4mx8py9J6AK3nWGsheCcBcR7DfLWEZlr_HqNniBunwwrNe_YerzERMCE0Z9zgd1bRgkr4jzq7ZArMmrU6n3Qv59HezW2HlUbGNelFQli6VP7oWE-iOctaKC2zZEq9i-kJN7XqBwkLe9iokNeW1PFoeZjjE0iHR0sAO8gQAmvlQlkmZfE6IZHlzVUmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#افشاگری؛ علی رغم تاییدیه فیفا مبنی بر اینکه یاسر آسانی هیییچ مشکلی برای همراهی استقلال در فصل جدید نداره و کارت بازی او نیز صادر شده اما علی خطیر مدیر عامل سابق آبی‌ها از مدیران تیم ها خواسته که در پایان هر مسابقه بابت استفاده کردن از یاسر آسانی شکایت کنند…</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/persiana_Soccer/27753" target="_blank">📅 00:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27752">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WtiBd1dAxIwcDlLndzFD1QPxTSxj0eLMk2MM6OHj3w6npMedZDRnI45HOzJX2b4N1zJTO6H1VoQZYb2a8FLaC1BCAINFSqhONtO09l-k99veHAAjIkWqjrLwS2iCdx4xvJFqfOkbU1h-x6bcdbzW9T-P4RhL6RxzHScJA-TRkWDFpUBQ5bF6lCA9gmRjjyTnCUMcecXbRRBeoF03cbqt2k2rhq4brDG--d0P6z1icTc_nEBnuvtTNBfASILjvIgK7iAkJ7coVB1D3Zv4byya7aGqUJBPOsf55QypzbOFzjHYXD4migp6nELfYy6aj10zBPJkpLIPnR0jtHfKPddaSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
🇮🇷
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس پیشنهادی‌سه‌ساله به‌این صورت که فصل اول 55 میلیاردتومان،فصل دوم 90 میلیارد تومان و فصل سوم 130 میلیارد تومان به محمد قربانی داده که مورد موافقت این‌بازیکن قرار گرفته. قربانی روی گرفتن رضایت‌نامه‌اش‌از الوحده تا روز…</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/persiana_Soccer/27752" target="_blank">📅 00:32 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27751">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YdV17DytAppgB6Tvn8h8IR5HEt-n2xGKxtuy0WesdRQ3f63w1io7U874uOIHN6x6VszZvKJG1vrn_GAhkpgT7J0mbRYkKNcqRRhvUVWmWE4WszbOZ6_Osv8fJhzRzXshhYlLlfeEBVU1iHJ2ko8cTuJuW6xFdQOUfteJll0aWGn1nUJbyPvkhyK_cKDfLsJTiRe4KlQP4hkXxLm7UTs1IbnI1xRLytEOo2nuAbgW-GH39cjFzykivJPAs7rGP3Tmv4_mewEn6nl3Rv_ql8tg78EU5S7M4pYu2_3mfENSBb27ONCi4LQD8HIZhC5PZasnA02bOtWnoKVZ7NeF9k3XbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
همانطور که پیش‌تر خبر دادیم؛ رحمتی سرمربی گل گهر امیر جعفری مدافع چپ خود را از لیست این تیم دربازی‌امشب بانساجی خط زد و اعلام کرده این بازیکن میتونه قراردادش رو با پرسپولیس ببنده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/persiana_Soccer/27751" target="_blank">📅 00:11 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27750">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPU5l6Z1nrkTpjNAdoXhxhTyQS-eDlSoqTBUcXuJCs4MgXLRbylXH4gcWn4HsoGae6vWpqJkqQ4mcNqdf6D2grRQxGWTmm06J0yhPmt0ctt8oZh9XzSexAFV10GM0Q05oiAu5wERRUsZWWQObg1WdBRRjZRtMRLG-0hDTyAKgI2KzpHBaG-_JEBPU5OtVDvCkt3Zmhcma86j3Zhx--4OWlbawn02KgJTYM8wak3wlsKUPqmyVzSZTJp8x0Pvw1r_Ap1rXcQwGWLcosVzX0T40fSYBQ5epsIRPzPCjGaPX5U3Scd8jTNcDy9-KgLJZ5VkIGvInew3Gs5h-ZnozD5QiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ تصاویری از رونمایی باشگاه پرسپولیس از کیت جدید خود در فصل جدید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/persiana_Soccer/27750" target="_blank">📅 00:01 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27749">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQbz2MN3vtKvukQ_kjpjwdVLTnk17Jfsuv9_9aFivbsjzhQqR-qq_SgahnU0Eg6HU5RF8HmWnTHtRLS9qP9wCSBHG_9K2QrKAfv4ELOHfLxpgadZDstbBX7Yj_35lcobMRRClXJDGuXAiyN8kNLUIVNZUmNLiAtxRP3OL7RQiiW0j-8PY99fHCPO5r_MZ-O1Xug79ToqA-t9NKNci9DMlwSI7AeUyGeBrSyNYBSgsxGH6G_t6DRzOedyNv7adU88Ebk1EtPr3H2nT6m_HBkzZO2_iUVo2Wk_HkbidsvpnCZ7VO1mSg4VvPTcBwnaCD_TqWKGd2jbnPS0PafFLcaavQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ به احتمال زیاد بخاطر بسته شدن پرونده داکنز نازون و جلوگیری‌از خطر تهدید شکایت به‌ فیفا مدیریت باشگاه استقلال هفته آینده با نازون توافق خواهد کرد و او به جمع آبی‌ها برمیگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/persiana_Soccer/27749" target="_blank">📅 23:57 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27748">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b41af009b6.mp4?token=tA0bPFytlku26MlLP7T2efw1sj5_m-Xqj8ItejcDXG6_YdvANx7zAN-MllF_CdNsQLgRabs6nKI9j1eAhayRo0t4uJemiGWyn2uNZIn6ais11i1o1Mi0jwXJdQyg9SVBkkhlIHI3oUEVPl1YtKQnkreyOgRWHak82EV8gt4uipxaK7f7pJy3yZe02mr_chCZg3sxnFfCWbWOdlWJvc2Hj00Lmr0T-KLqbV7_fBrX56_Kk3Ji-HSuAq3L-NvH2PyWbZVa4ETetA-tRJCC_fyxA_cWbkLkrBmpT0mwQp96YPZ8TwDoMIBrGOq7f3jSoP_0p6Yp1ySUtGp4Lq_AhnhGvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b41af009b6.mp4?token=tA0bPFytlku26MlLP7T2efw1sj5_m-Xqj8ItejcDXG6_YdvANx7zAN-MllF_CdNsQLgRabs6nKI9j1eAhayRo0t4uJemiGWyn2uNZIn6ais11i1o1Mi0jwXJdQyg9SVBkkhlIHI3oUEVPl1YtKQnkreyOgRWHak82EV8gt4uipxaK7f7pJy3yZe02mr_chCZg3sxnFfCWbWOdlWJvc2Hj00Lmr0T-KLqbV7_fBrX56_Kk3Ji-HSuAq3L-NvH2PyWbZVa4ETetA-tRJCC_fyxA_cWbkLkrBmpT0mwQp96YPZ8TwDoMIBrGOq7f3jSoP_0p6Yp1ySUtGp4Lq_AhnhGvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خلیل‌زاده:
اون‌عینک‌لعنتی‌مال حسین کنعانی بود و دادش به من‌که باعث این ماجراها شد اما من بازم میگم اون گل آفساید نبود؛ ویدیو رو حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/persiana_Soccer/27748" target="_blank">📅 23:49 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27745">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MvXvb4SlJb0_ax3Sk2A3WOGE4lB_MLODXBQQZBlTFTRoGdlqg9_d0wJ5vhdsOKZv0K_tDCMWtQKla19gmM810INq8WQxv6G3ReeX5VecjCZKDIlWrnTVQ4PYZHwMPzL8ji-W_j-5rskeu8OuN9ApboGlUyvobT3LwSVStL7--SLrnXRBQLacd8RFx0qYZCxwxcBp0J20ekAe8BJWqt8UohW8lwBwTgt0SHcs-ZJ2TniO1HH818MKy0OOzJ-G8qDMUyokxEHO1NTuz3oPGpu7HAzkNHBCMRXy17glgKVc52jMJVNKBzvP_uRDouqXbgXXlmWfnYyEGNVoWByHpTcGWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RRCPzfxobH09BA55vZvR_bSJ5emTnAL3PIpHub0fdEcZFZpzK4kpI1H9nnukQ40MS28Wbh7i7STruEBalDQbFhlN2aOXSs6-VdgBXpUYRIhtdG-Vrhcrals36Lybh5ZRfvwN6B2BCI1leSbRjzlwQQ61XcNjQq1_8NuE6nER2xiV0zy3dC1BtvcKpUw7xFJfIb5K-U7Z-U30djDoQUk4S-SDWJ1tZFljTrSOPoskMLFKrXVVkryeX6Wqu_u9rK5VoiBwZOiBIDTBAnJjVO0WlRndvhCJ7QXuEXrV7sNjuMGtR6AycLCFasH-2MjsJb6461umOlFuUUi5QKDhfkAyVg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇹🇷
دو ویدیو زیبا از فوق ستاره‌های تیم ملی والیبال بانوان ترکیه با کاپیتانی و رهبری زهرا گونش که اخیر قهرمان لیگ ملت‌ها هم شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/persiana_Soccer/27745" target="_blank">📅 23:40 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27744">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bM1CrGzVdnd0cXph1xtEezZv-hZDjDgn1oiMqJgFO0SAS42lBoTFONEdeJDPYUS90pNd1v5ks8Ac2VoKvdQzvZ7Vp2LybbrZeLrQ6h2KzwZ3gDWBd8R6MIKi4Xunw5vBKo0r-2u0oCVlxUIHuS_B8fuVcWVjWywt97X7L3ca8huQwNMLq63d-DK1uSC3dakIgZPhtc2ZXdYgDtkXyh1bIK7wFurk-qY54t7vNAijUozBzAvktQ1Cn1Up4jL1aIKSYa00JhIhv01tTQnItRytkxVgNrlYMiFNeMyQnLezPYTLmf9qZUAhrodbqawa_m_Gk2CZv9hg7MfX8E4D5w_Npg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
🎙
محسن تنابنده: وقتی‌حال‌مردم کشورم خوب نیست سریال‌ساختن‌ارزشی نداره. دوست داریم فصل جدید مجموعه پایتخت رو بسازیم اما شرایط جامعه به شکلی ست که هیشکی حوصله سریال دیدن نداره. هر زمانی که حال همه خوب بود میسازیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/persiana_Soccer/27744" target="_blank">📅 23:18 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27743">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9IS09trjum9dzIwrUz082q6cr-DcfZP6YBFI2zpCkz6znxYTzNTlqAd45s7p3dp1E6IcnkhWIh_8zCMNjKNakwRFT6WGO9oxMJn4d8i6FqPOCbQu7ZEwUOzwCaR3J4gkjEEbcQu5PMLNc-I0gsaYIif9diZkTWh59YpVzhJOShkv76UfV90RtBj-t1C0m90efe3rR8dsAW0kO99wkoR_eh-W4MhEesMeuhxx2WzdFgWpmnO11ddjRGTjv89u01uRAxr-sLJdc-Gi4-W0FnLLR4J2n14xEo0stUhspug0cmREdche8qVN3HP_DJqHmhxkew_ZlEEGR0aKjus_GbXXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
🇮🇷
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس پیشنهادی‌سه‌ساله به‌این صورت که فصل اول 55 میلیاردتومان،فصل دوم 90 میلیارد تومان و فصل سوم 130 میلیارد تومان به محمد قربانی داده که مورد موافقت این‌بازیکن قرار گرفته. قربانی روی گرفتن رضایت‌نامه‌اش‌از الوحده تا روز…</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/persiana_Soccer/27743" target="_blank">📅 22:57 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27742">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOGNZi4BaHUgKk2Xg0MieMl2bYI3etlNN3Fc98OXxyHsEkICpOiDaCyg2E4-yQ5hXQXCU8IwioTr4MKOc3kFKzIjsa4qRTWsZgwElg5agvzzJNkFASW4-INA2_iZ-4e2PyqpKfc6-537Pm1Qvc5fL-h5Eve2f0mDt7XNWK9--MzntTJspNP0ZMJJzcUlPV_zH0upcsjis3Es7JHylq4J2mDfDPyTcDpRprCO6Q7Li-2w_3zJfk9hdtAoUoqd8b7e45-ga7I8nLdScFUkFbXFkr2Mev8OMuQ_l5fDGNgtI4T1kCVvta6sjNKc5mbWCTzM4z_EQDhQC3KdXMmWvg-eDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#افشاگری؛ علی رغم تاییدیه فیفا مبنی بر اینکه یاسر آسانی هیییچ مشکلی برای همراهی استقلال در فصل جدید نداره و کارت بازی او نیز صادر شده اما علی خطیر مدیر عامل سابق آبی‌ها از مدیران تیم ها خواسته که در پایان هر مسابقه بابت استفاده کردن از یاسر آسانی شکایت کنند…</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/persiana_Soccer/27742" target="_blank">📅 22:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27740">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e4yliy8z5dgkV4SGI1CuhRLNbTpNkQyavvR8w10DixZKefFEuBlT3Xse1RLj-m9DxoUJ55VrRxpCuoTA7MM-kKWS3rAJaqdkZdr9KJCWBtcvTqvu5FMpuOaE9zE-NsyLGEqHCGsnxUK7Z-AAph1hkqKyrVLQ4PaOVyACCazULQc2KYRXLTLxUxFbYAjy9-dIon57_DWxuT37cHuNuibBefdJbbpPNkmseGeTfnUCZF2EjiP24Yd-UcqlgJz_CyyuTXFQUOCzbWrXwIH9WO9NKGSnW0sS1tfeKOIET4-7wGJrT5iB_eZZ5l54g_L6LfV9nH7mdak2nRLU1mVTczIPZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IYqw00693iG2XGVMtWUGgK0XkDF0p65PD7YxvAlHo68AodizSY8wX5wT-L_d-vArGHO3t7Vj0Ns2chCXrTW4LwaU1-B27d8lkwfTR-mFKVIVF0FDpSDCQf1Nlgy_nytDsTZR-j5M6kbts70yR3SFox2auXviwAiD00PSroIpRh32Si4HzBxEa25D6qT-h5NyQhJ1Va_A59pVFe5cRkhzZmjngDvnww3kf248jG8x9z64Ny2lWOSiudzwBurGShryOd0mC7kv2OYH52lk2ckxIAQmQPJV2T051kPfJyeFuR7B5epqx6pxhP4Zl4M0ShlPeJmVE1uCS481dZggmjo5lQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔴
رونمایی رسمی باشگاه پرسپولیس از کیت جدید سرخپوشان برای فصل جدید رقابت‌های لیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/persiana_Soccer/27740" target="_blank">📅 22:43 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27738">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QqmIFOgvlmyVBgBn12n-EnaLubBAkwyjHAO604LG14yr6PPhwBla_C9oNb1xhZPIcvG8YD3kDAbqfnp_2vF83KcIn5eXxkMd-l1mCEOQ7gAdC83IwK03g8onXNk8a_HER5imgWgBzwnVRXNobqw3zCAIS58fWfsFL9-E8B7_G_NXftmFgiPGgGRaG3QNn8hx9P5vjG4ssBJb_9rOHsxFODIqf3TjVOZtpTZvTQzbne6fZKxEorZaGCtvTeJk7kg5F99nwIamYsWHcDEkKUoHTUpVQJdRH4MxzdC57l4_XlZyETmHaNJA90ZQddiwNBgH3B8c5wlbNnngaUcs4Tvw6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b7yKYnlIZPy7LpNkHD1Yc894Quj5H7oW5Bqb4dsqBpwcNGlM9waenYs3BL_IQHFoj-Sty1MY7H_WAwESmKq0FPQ93m2v0a43QvAl2vN35BB6SB8pw5eVs5HTE4mb1UbjuVduq7dGlYNE873UuFNdW7VtKKZ2R84Xsg_-Da05ZgPSy9MyYxN9GLG9U0sCsMmjyIyk4oZ8Wt6u3lmqfFIhhhKBNCciljq0EvTJ3KzP-fDIXM_vZm6MlxQtsz11gcGlYggRlu-Jba6RTF6uA90vDgK-CATtobrlVgXqkof0uuuRk9_ABCABEF8rtkmmMamhsx4JLHPEH8YLO3F8fil-JA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته اول لیگ برتر؛ سوغات سه امتیازی و ارزش مند شاگردان محرم نوید کیا در یزد در گام نخست.
🔵
چادرملو اردکان
0️⃣
-
2️⃣
سپاهان
🟡
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/27738" target="_blank">📅 22:25 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27737">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b99364b6df.mp4?token=mEzYVCgKIN2-QqGQvwcT3tsvLk5M17-1PUz_ZI8qPQ-S_1yLnDw2G4K6gz_oP1voWalo3V5avoYRUvCtd__NRit78DPGtAKnlEobWkn2WgmFjD2fXcze3_nmybd7b1tUzmKTO7yLmUb-VdpHpXpEW8AJE5_kLSunZFqbcTGf0khKW-M-ODY88LLA9kKpO6dQdfYHxQvzkA3GyH8car6S4tovWYRTTpZjsGqVlIIKVLv5uPT7b0I7GKTRsSSb7-G93hlhOHBYgVRF186IlFPACX2QnitLeZlyuHcp4CHVnjmvG94nB4SBFi-5Ibyvy0lhjmLgSVnJ6hCex0O0NB6klA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b99364b6df.mp4?token=mEzYVCgKIN2-QqGQvwcT3tsvLk5M17-1PUz_ZI8qPQ-S_1yLnDw2G4K6gz_oP1voWalo3V5avoYRUvCtd__NRit78DPGtAKnlEobWkn2WgmFjD2fXcze3_nmybd7b1tUzmKTO7yLmUb-VdpHpXpEW8AJE5_kLSunZFqbcTGf0khKW-M-ODY88LLA9kKpO6dQdfYHxQvzkA3GyH8car6S4tovWYRTTpZjsGqVlIIKVLv5uPT7b0I7GKTRsSSb7-G93hlhOHBYgVRF186IlFPACX2QnitLeZlyuHcp4CHVnjmvG94nB4SBFi-5Ibyvy0lhjmLgSVnJ6hCex0O0NB6klA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
سوپرگل برگ ریزون و فوق العاده تماشایی اللهیار صیادمنش در بازی امشب لخ پوزنان در لیگ لهستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/27737" target="_blank">📅 22:16 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27736">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80eddbb6f7.mp4?token=NJVmmyChnuq5hp3eqPvDRDHJp8i2_QlD8AjPAJ90G25KYbjixy3nc62b0bAOaxmwohqKU-pBm7pzfpJQHNSjoifCUrwDN331oRH3Ri7PRX105J9uWLSo2RlTMpiPPfFc2jtyJ7QkwDTi27hLBHm4W_0_rR2ZX3bLN0KqGWUPD4lAx-B9atXvlbzxTLCPB95Zzbo6JHG8TXlATq1Tha5bVNS8PBNBuvcpYxTaXCQsS5JrtqFvLLGlpB1sFsQxOWPd3K53YKlUMy7tMDCF4TRKSrs5Et3jQw1J9DwE_elyCeWraynZ5Bbp9vtUT-39GTMC8N0evsQBkOG9Ppin6FhtsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80eddbb6f7.mp4?token=NJVmmyChnuq5hp3eqPvDRDHJp8i2_QlD8AjPAJ90G25KYbjixy3nc62b0bAOaxmwohqKU-pBm7pzfpJQHNSjoifCUrwDN331oRH3Ri7PRX105J9uWLSo2RlTMpiPPfFc2jtyJ7QkwDTi27hLBHm4W_0_rR2ZX3bLN0KqGWUPD4lAx-B9atXvlbzxTLCPB95Zzbo6JHG8TXlATq1Tha5bVNS8PBNBuvcpYxTaXCQsS5JrtqFvLLGlpB1sFsQxOWPd3K53YKlUMy7tMDCF4TRKSrs5Et3jQw1J9DwE_elyCeWraynZ5Bbp9vtUT-39GTMC8N0evsQBkOG9Ppin6FhtsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
🇮🇷
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس پیشنهادی‌سه‌ساله به‌این صورت که فصل اول 55 میلیاردتومان،فصل دوم 90 میلیارد تومان و فصل سوم 130 میلیارد تومان به محمد قربانی داده که مورد موافقت این‌بازیکن قرار گرفته. قربانی روی گرفتن رضایت‌نامه‌اش‌از الوحده تا روز…</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/27736" target="_blank">📅 22:08 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27735">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcb2c4a260.mp4?token=HdWthMSGiKCTgv1rK8YT7mtxCMZZvS4B9SQIY-eh4uHTd1rLbB-dmhHnfZIvwYCDrWmZiqtWWbvlcn_a-cCxLYLRs4t26x2W_DaT1SiQXq14FQHXul1clLA6x_LYIWwv1tcIRSDjvg5EBHnGX8kjpPeDpfhwOWBx8wvmDzZD_6OnKlpN9PPKF2n0abNRfr02z3DzAWw6OUC0Kn-VGxn2hU0rXWtJMAM5nKjULVx9bgbgiS3jtzWNgsvQkw9_od8CL6D-9-Yeg-YzLWkM7J00wGT_Ik2MeVW0Otd8Ang7XQxgho8Pe8ldvAU8fvpxRJ3D9jz_bI1DMxlfvXmjv54U9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcb2c4a260.mp4?token=HdWthMSGiKCTgv1rK8YT7mtxCMZZvS4B9SQIY-eh4uHTd1rLbB-dmhHnfZIvwYCDrWmZiqtWWbvlcn_a-cCxLYLRs4t26x2W_DaT1SiQXq14FQHXul1clLA6x_LYIWwv1tcIRSDjvg5EBHnGX8kjpPeDpfhwOWBx8wvmDzZD_6OnKlpN9PPKF2n0abNRfr02z3DzAWw6OUC0Kn-VGxn2hU0rXWtJMAM5nKjULVx9bgbgiS3jtzWNgsvQkw9_od8CL6D-9-Yeg-YzLWkM7J00wGT_Ik2MeVW0Otd8Ang7XQxgho8Pe8ldvAU8fvpxRJ3D9jz_bI1DMxlfvXmjv54U9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته اول لیگ برتر؛ ترکیب سپاهان برای دیدار امشب با چادرملو؛ ساعت 20:00 از شبکه ورزش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/27735" target="_blank">📅 22:05 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27734">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WqBc0ugP3Zic515n19QGwTjgVRGEauWHLnm6kWV1GSYlWETJOQlkmPoyzmfPrnrhacJtrODVJv9hEldEBbYM0eMqMiuuioY3fUn8IHKf6UNU242AqM8jLS7zY1975_KU57cFtYi35iIojLgdsjePqjvBOBR2Rqp8EhlY5f3twZBWW6wGWMaAelryUr_fVkODyO3704zswKlIetfT-Cvpf2PfJ6_1iiL_zuUQ9Ix4m5vWf-DOzuASmDyZg6ACxAwiTCDIl6GZpVtTisb6ZCBPGSMulYGw67UVzCn6Rwv6LR9qxnhNdzTt0Wv97hAX1ysyHMid7E0_nEapX1nGAaUyvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
چیرو ایموبیله مهاجم سابق ایتالیایی‌ها و باشگاه بشیکتاش که‌تابستون‌سال‌گذشته قبل از جنگ دوازده روزه چند تا از ایجنت‌ های مطرح فوتبال ایران تلاش کردند او رو به لیگ برتر بیارند در سن 37 سالگی از دنیای فوتبال و مستطیل سبز خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/27734" target="_blank">📅 21:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27733">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ecmlER1-TdyHzDzDFIz4ufDKEPexx4IwScCiR3YLOFjIGqVyYl4QsRiZpuma5Ug3ktQVlpcq9lGF8sgZHtFM8WvBxs1lxtceMAIM_5y20TtHaxnJ9SSswzoI69pphAkqPyE5-zX32n6NA_oAs1Gste7tqSD904NmcXvqiLIURHl10fLUI_5aZrz_oe7xBHqsfWZbkf3VJJRGRw6uUIpFFmoQ-i-HTvGJvJ-_c7rY1kxlxQt8w7HXF4qUsIHIJ2_KsI8m1nt3iKyI-xroQTyyCTCibNyLII1VdlYf6-KTphgOuZckt0m8vakTge45MJgJL1U7bvA7H4Q4bMe5GJJMoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
طبق شنیده‌های رسانه پرشیانا؛ سید مهدی رحمتی سرمربی گل گهر سیرجان موافقت خود را با فروش امیر جعفری مدافع چپ 24 ساله این باشگاه به‌پرسپولیس اعلام‌کرده‌است. رحمتی در این پست قنبری شاگرد سابق خود در خیبر رو میخواهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/27733" target="_blank">📅 21:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27732">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rtG50tQ32F8sCyTlS0xhdHLrl4sAukSSfHQbC7JRnA-GtdwgHdLuK1tjp1KxDPguFJn9auCAwwHJxP5NSmttAhniS1z89dIHN4ns8tCPHpMQcEcyO5qDX1BEx06VK4ymhcVS2TbiwkWnD24498dfYiUDHp4QX59WcWHZ8FwqgF6rRssZVn76-Ctbbv_C677yXMXMrFFnvaspGq-GgIpjnstOPVl0E6Qnn6ibA0TL1XWDsp4k-cclAMQh6jf4udFKS-wgi6vydslKPKPX1zWwz97ikPLYTbYhCjtyYhPOlfddGzDScBVzXswQ6S1Tu2mMW4fyhaSXnl-7ybeFTA2_0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌لیگ‌برتر؛ استارت آبی‌ها در فصل جدید با برد قاطع مقابل مسی‌ها با دبل سعید سحرخیزان؛ فرعباسی با کلین شیت فصل جدید رو شروع کرد.
🔵
استقلال
4️⃣
-
0️⃣
مس شهر بابک
🟠
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/27732" target="_blank">📅 21:31 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27731">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B3Gnjr9hNSBWWcPxlukRnNzr4n4yXVfv3-EvED3kKDkmxRP3XP0qjdrxFjlX01CFjGlSzTFsMeZFkcF3_ld_aTiszuR1XfXBkuvOSNv99yCQHMcMXY5T76ugqbkgNm5vibv38G1CANr3hjXH5jJABDj6FyztwuPFm4ZJEJBGz8OtEQLrhTn5XIJqVjZI-TRDRFsJt6pp27-YGblFeKpICXGwq8DU97IwkNhf5_iQxcRJZ91I6ulseJdXeIHsgIbUy6ZW8nqV_45SasaAwzz8kF7a8nNbzC7YaBcErCIGb28HWCHxZhXHBZ5PIocaPuma2B4U2-kp7a2EbPiEXwSMVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
دبل‌مهاجم آماده آبی‌ها؛ گل دوم استقلال به مس شهر بابک باز هم توسط سعید سحر خیزان دقیقه 56
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/27731" target="_blank">📅 21:27 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27730">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d884286cc.mp4?token=v4BvIkLPAh59iB3-IqmiKLSRqhVp_ORV6NA7TDyAJWRC4GhDkeOR1brjX-Oqa8L03pBd0OJIQxyjfLGRjoxMSrwpCI6FiZscGpSaOlbJzvLq1ZZobGug34hdJv4rvjOrytoPqkZnT-lbHwARba_V0hsrJnyOnDPDUhD05rJrK-qxRl9RTZiTBrbgbwmKYnvg-kASC4OpXJAayUqzPqIXu_Ssopf8TJlHCv98xQUZjPJftqQdEqERyXhsANQoj3Nyb5bvelitZY6FVG8MGjNwAkg5mpD5Wmlt8JPmYP8G41aDW3UlxT8hcj48zWvPMxiaAoe1VnjqDGZTaYCmhKfTCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d884286cc.mp4?token=v4BvIkLPAh59iB3-IqmiKLSRqhVp_ORV6NA7TDyAJWRC4GhDkeOR1brjX-Oqa8L03pBd0OJIQxyjfLGRjoxMSrwpCI6FiZscGpSaOlbJzvLq1ZZobGug34hdJv4rvjOrytoPqkZnT-lbHwARba_V0hsrJnyOnDPDUhD05rJrK-qxRl9RTZiTBrbgbwmKYnvg-kASC4OpXJAayUqzPqIXu_Ssopf8TJlHCv98xQUZjPJftqQdEqERyXhsANQoj3Nyb5bvelitZY6FVG8MGjNwAkg5mpD5Wmlt8JPmYP8G41aDW3UlxT8hcj48zWvPMxiaAoe1VnjqDGZTaYCmhKfTCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
تازه‌واردهاگلباران‌شدند؛ گل سوم استقلال به مس شهربابک توسط محمدحسین اسلامی دقیقه 88
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/27730" target="_blank">📅 21:27 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27729">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f3f9408f8.mp4?token=iiPmr12OgoGzNGwc5lemS6-Cfx7bW4r_pipo3-EqhfENagtMlVekV1GnDNiiEyUoEkKVkA9k32yF8iBk0l2_8NyvBg9H4mhgekr0Yp0GVUVQXCeXL86kMnBFzXR0PrwhXbllsTSYzQwBetjK6OJ2Kjt9-bZJoBwg9jXhDyzNDnWH7V6kNx5C7fP2tk6JnZL_ot68CvywnOQOTSAoqSZy7l8yC-J49LhnCKM-ZucXCI4wyQoqbu6pGWBIRe7nKyyURR_yEv8JKqycU-dMwplZIDlDQfJ05DcYRxfb4r3WLG3ycF3vqLMOD0PLaTuesCbJilQmkEkxZZ3p_XyUxUC6og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f3f9408f8.mp4?token=iiPmr12OgoGzNGwc5lemS6-Cfx7bW4r_pipo3-EqhfENagtMlVekV1GnDNiiEyUoEkKVkA9k32yF8iBk0l2_8NyvBg9H4mhgekr0Yp0GVUVQXCeXL86kMnBFzXR0PrwhXbllsTSYzQwBetjK6OJ2Kjt9-bZJoBwg9jXhDyzNDnWH7V6kNx5C7fP2tk6JnZL_ot68CvywnOQOTSAoqSZy7l8yC-J49LhnCKM-ZucXCI4wyQoqbu6pGWBIRe7nKyyURR_yEv8JKqycU-dMwplZIDlDQfJ05DcYRxfb4r3WLG3ycF3vqLMOD0PLaTuesCbJilQmkEkxZZ3p_XyUxUC6og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
دبل‌مهاجم آماده آبی‌ها؛ گل دوم استقلال به مس شهر بابک باز هم توسط سعید سحر خیزان دقیقه 56
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/27729" target="_blank">📅 21:23 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27728">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a75e1bc211.mp4?token=mqRgmoopKiCLuE9tXObbtAqZccil-Hz2Uk5V-hfUW6ukuSUsL7s1M-hcwsMjhMqKXtnAPqanJAW97HZBzkYXh_Btm7LM9j3lS_DDReyVUqNkAs8Nk03WOAqD1R-n6yO6Jbhv3RFJuR4yz9YNxa8rpn61d-kGRo_hhnulqGqfYhRqj_4c9kgyAeruBTZBCHbYb3EwtS1TuKLYNGVsPE5VuHUeFr0NyxKdPpLDMY6VNXRikFXSWg4hb-9EExWbSEZJW03K_E8bANiTiF46PnxBGFoYq2KPIqhbwzRWYlBcO_f0ZZRqRc6sFR5PVqVNDIxsutKvnn5KgVrFn546VocZMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a75e1bc211.mp4?token=mqRgmoopKiCLuE9tXObbtAqZccil-Hz2Uk5V-hfUW6ukuSUsL7s1M-hcwsMjhMqKXtnAPqanJAW97HZBzkYXh_Btm7LM9j3lS_DDReyVUqNkAs8Nk03WOAqD1R-n6yO6Jbhv3RFJuR4yz9YNxa8rpn61d-kGRo_hhnulqGqfYhRqj_4c9kgyAeruBTZBCHbYb3EwtS1TuKLYNGVsPE5VuHUeFr0NyxKdPpLDMY6VNXRikFXSWg4hb-9EExWbSEZJW03K_E8bANiTiF46PnxBGFoYq2KPIqhbwzRWYlBcO_f0ZZRqRc6sFR5PVqVNDIxsutKvnn5KgVrFn546VocZMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
رونمایی رسمی باشگاه پرسپولیس از کیت جدید سرخپوشان برای فصل جدید رقابت‌های لیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/27728" target="_blank">📅 20:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27727">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9a0da2836.mp4?token=Xvz9cxoy087o0UHsRJIzv7FamUjvHBBZ_vkm5ylBqPbv_vyt184SK-izuQl9NpR46dsIRInuYYeGkNr4w-a_aGAGJ1BdbnYDMc9U6Mh8NUGCtb49zurylEBXnBRkviMAcfqBAfeBt6ZM-P8O6b82JvflqFEcA8oWafG1kqpdhPIMHWou3LZH_ubUrlXMp1jVcH7EZTpBNi_pDn813MC2aY_ntZO2RuV3GsmIAO6xmyx1X5zFm87_cxhVAjJco1BqRNIuu1KdW8N9diAxprskIJ96RNX7xeDmTeNvBYAD8dbFxu-IeKlnrWxAdc-SpqPeVDBM-p30BAPVS4oqFXkyDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9a0da2836.mp4?token=Xvz9cxoy087o0UHsRJIzv7FamUjvHBBZ_vkm5ylBqPbv_vyt184SK-izuQl9NpR46dsIRInuYYeGkNr4w-a_aGAGJ1BdbnYDMc9U6Mh8NUGCtb49zurylEBXnBRkviMAcfqBAfeBt6ZM-P8O6b82JvflqFEcA8oWafG1kqpdhPIMHWou3LZH_ubUrlXMp1jVcH7EZTpBNi_pDn813MC2aY_ntZO2RuV3GsmIAO6xmyx1X5zFm87_cxhVAjJco1BqRNIuu1KdW8N9diAxprskIJ96RNX7xeDmTeNvBYAD8dbFxu-IeKlnrWxAdc-SpqPeVDBM-p30BAPVS4oqFXkyDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
گل‌اول‌استقلال به مس‌شهربابک توسط سعید سحر خیزان در دقیقه 45 روی سوتی گلر مسی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/27727" target="_blank">📅 20:49 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27726">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DQI4dyhKkFkTwI1EhZJCVZDdrhtvtrEMbHF8ncZ4_pL8a5xzyIn3XBecA2Fgl9I8sitpK4uY70waaUo_CevlDVFU-anpbwZq3tAYhpFWLJqxzOYb67Bfus4qxNILYrr4Iv4weAugYKm54bQag0yo3mEr_16zQgbHWJgHv2aXxEGm8SwfXw16bDcdpjUOh-OpUmJkZarQ6K1Uh7dI3dqBOpd9fhryKo-zl3SzYp-fVHDK8-GAk4EaM8HR7qIzzdL_9p2FoRztJMMismtb1pmlE_ved3LF-KtOFyCWmmOu63EIS1-bwv2YCUQRYCnWoaLmpaBqsGDxoIlD3igZ3c0gug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی‌پرشیانا #فوری؛ بعد از پرداخت رضایت‌نامه؛ دانیال‌ایری مدافع‌میانی 22 ساله نساجی باعقدقراردادی پنج‌ساله رسما به پرسپولیس پیوست.
🔴
باشگاه پرسپولیس دقایقی قبل مبلغ رضایت نامه دانیال ایری رو بعدازکش‌وقوس‌های فراوان به حساب باشگاه نساجی‌واریزکرد و بزودی…</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/27726" target="_blank">📅 20:31 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27725">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e32a2d766b.mp4?token=K2A2YcKNdDikJ1JQVizmPe3mrJB91ZNRyicRiq1lBVctA8acUFSzzNqzDLI4kjqMEmkrYYSzT6eL27zK_oxuaMA18kdgltbBPINZJ4mwJ9z_PAfpS5ARPvVoHpKCtZIcMWpU6i4Q0dpOBFLoCBUbgwOIQFrtIuEicfNG7Q0ZTduyL3aMWn_-AUJsEHQ5tZ090GKHHlZWt6wu3ZA8cWazzpcpSNQgd4I8RrFt81rTvHGW3KDt_9hYBMnFlJhEN9DAglkXJk7VKwz4hXc42wfSQBAKmZjKWCV79UbslBvJN1yvI7wiY7w9aapA2ahSz3uTK2zyplJCTzhV7k0MF9wh7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e32a2d766b.mp4?token=K2A2YcKNdDikJ1JQVizmPe3mrJB91ZNRyicRiq1lBVctA8acUFSzzNqzDLI4kjqMEmkrYYSzT6eL27zK_oxuaMA18kdgltbBPINZJ4mwJ9z_PAfpS5ARPvVoHpKCtZIcMWpU6i4Q0dpOBFLoCBUbgwOIQFrtIuEicfNG7Q0ZTduyL3aMWn_-AUJsEHQ5tZ090GKHHlZWt6wu3ZA8cWazzpcpSNQgd4I8RrFt81rTvHGW3KDt_9hYBMnFlJhEN9DAglkXJk7VKwz4hXc42wfSQBAKmZjKWCV79UbslBvJN1yvI7wiY7w9aapA2ahSz3uTK2zyplJCTzhV7k0MF9wh7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
گل‌اول‌استقلال به مس‌شهربابک توسط سعید سحر خیزان در دقیقه 45 روی سوتی گلر مسی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/27725" target="_blank">📅 20:28 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27724">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32b2ae1951.mp4?token=oIoUh7MKa_RjroA9WqyiWUdExTjiInLHZ1uJNklGUh18Pxa0eczCTNd3JanSQlVsYmYvhpJVvQMxQm0yfDDxrFMQvDBDziwPOI4Q_TjUQdHu_mNpQQYWrz8CwFD4yvcjp70RofjAWgFB6bSO1wZrX8LJPniNqnxlaq4-EURnPCGrJ1BP5RgbUdEqGXimsCmuIvkhhPxhGkDWmEwAhPeBBiJ2Q0-DaN95AAeNoXI5MbwL8iXnGnXFgTiVPJhI76-JAy8bwIWqFyZG3qbqueER_bfgsgbAsws6oNYGNs7Hgujngv2MJVybbQyvhI9sIDlsDYmB2vcZ2Vrc2kQ5vCnC5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32b2ae1951.mp4?token=oIoUh7MKa_RjroA9WqyiWUdExTjiInLHZ1uJNklGUh18Pxa0eczCTNd3JanSQlVsYmYvhpJVvQMxQm0yfDDxrFMQvDBDziwPOI4Q_TjUQdHu_mNpQQYWrz8CwFD4yvcjp70RofjAWgFB6bSO1wZrX8LJPniNqnxlaq4-EURnPCGrJ1BP5RgbUdEqGXimsCmuIvkhhPxhGkDWmEwAhPeBBiJ2Q0-DaN95AAeNoXI5MbwL8iXnGnXFgTiVPJhI76-JAy8bwIWqFyZG3qbqueER_bfgsgbAsws6oNYGNs7Hgujngv2MJVybbQyvhI9sIDlsDYmB2vcZ2Vrc2kQ5vCnC5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
شماتیک ترکیب استقلال برای دیدار امشب مقابل مس شهر بانک در هفته اول رقابت‌های لیگ برتر.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/27724" target="_blank">📅 20:18 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27723">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qnD8hLVy8o3qZXB8OZELZNA6e8dJOasEmSbtFhpDfzwMVJsFPi2fK7E2JjmukEjr39L3hc0Q21k6Xnm2gUqq-11gB5nE6qt5D_Xz8gbqeH1y36qM1uoloQRhbdwXkLx4NWaXJnooz56KDRrhR8DSawnb2KGb5YN2cdPyeyNIjfLa9H9EF553iiJatczOW9mbU1x0GV7bzviMFpT4ZB1xDGvT57HUBZNj5Lh3pT0nWds-J4IxhMXM4RUxHrLAodOwrKMEXVE6ZrUPeVBoXJExo302pxkv3wFzXOiDziHK0zXFX7oT4rLIgZO7dlXEEMkaLNLaYOmXSFqqEm7CJGTvlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
دبل‌ستاره‌بلندقامت‌پرشورها؛گل دوم تراکتور به پیکان توسط شهریار مغانلو در دقیقه 45+1
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/27723" target="_blank">📅 20:10 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27722">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WERTnccRYL9JOYFQOQdSTvLLlqcPVps5ZUcVZvYLnLMAyLXm9eL4obMwX3-_CCw4l4iX7jZBWKhhk4x_rQHzd18T52X0RRhlMFXAdyhwmtduytP474TbL3uUxije35B9HaFfF4ZGY7fUrdM97OdqkBULdEImk-DN_8UcfRV_o_97PieoXFf7KKinWZ6Wlu1bGD51-YdJOtrlSCYdQnpVyH6TvRhD_9Co_mkxfBS_gKd5R-FdFv5I8gj5UjZVmSb4IO53K1Y-F1_SX4cJXm6h3QYUW3LhCqTMzeL65iqutAbsrUldXu2poxwDMC6_nt39boV2DkXo8xofexAn-H6wjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#تکمیلی؛ علاوه بر جذب دانیال ایری و جذب احتمالی محمد قربانی؛ باشگاه پرسپولیس یک بازیکن دیگر نیز جذب خواهد کرد و پرونده نقل و انتقالات تابستانی سرخ‌ها در این فصل بسته خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/27722" target="_blank">📅 19:46 · 23 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
