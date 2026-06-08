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
<img src="https://cdn4.telesco.pe/file/KwC_ryRjtHHEGFN7gU-5iNFhcqsVdZDHRdbcmbtqZTlulhePqA53tfdNmONQlCVsSK6Kv8rTDCbN2_w1ZSBHERQKYEglBcF3xvtCMLQsgGfWDr1ZDRisagrWEBxqkR6FUOV72zLsF-q5-tSglEmBap5dmtTElZHufCB_JdZz8BS86WOIP0PPe7erMsj3U8EEUC3-1C1tiT7pq1Af_mSnBMiquTW0762eZuSjFXJ2KyoSwSHvxxFwvLeuQ2dqRMY0ynqMYYf3kqqTnG3-FfZTPKWaJ5ugkc6XPNoz2tYjvXJpEoqepjmvPjh8uL9Uvls-rgfp9mlTEi9FBTh1dPHW2Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.6K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.✍️کپی کردن با ذکر منبع «سرخ تایمز»🖥جهت تبلیغات🔻@Tab_taems⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 21:14:30</div>
<hr>

<div class="tg-post" id="msg-133070">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
ترامپ : اسرائیلی‌ها وقتی جنگنده‌هاشون تو مسیر ایران بودن، به ما خبر دادن
🔴
من هم سریع وارد عمل شدم و تلاش کردم ابعاد حمله محدودتر بشه
🔴
همچنین پنج کشور منطقه با من تماس گرفتن و خواستن روی نتانیاهو فشار بیارم که حمله نکنه
🔴
من هم با نتانیاهو صحبت کردم و…</div>
<div class="tg-footer">👁️ 369 · <a href="https://t.me/SorkhTimes/133070" target="_blank">📅 21:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133069">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPulseGate</strong></div>
<div class="tg-text">🔰
سرویس اقتصادی
🔰
یک ماهه
25 گیگ 250T کاربر نامحدود
30 گیگ 300T کاربر نامحدود
35 گیگ 350T کاربر نامحدود
55 گیگ 450T کاربر نامحدود
100 گیگ 650T کاربر نامحدود
دوماهه
50 گیگ430T تومن کاربر نامحدود
70 گیگ 500T تومن کاربر نامحدود
150 گیگ 750T تومن کاربر نامحدود
200 گیگ 800T تومن کاربر نامحدود
سه ماهه:
120 گیگ 730T تومن کاربر نامحدود
160 گیگ 780T تومن کاربر نامحدود
230 گیگ 850T تومن کاربر نامحدود
320 گیگ 1T تومن کاربر نامحدود
400 گیگ 1.2T تومن کاربر نامحدود
🛜
مناسب برای تمام سایت ها و اپ ها ،ظرفیت اتصال نامحدود
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 3 · <a href="https://t.me/SorkhTimes/133069" target="_blank">📅 21:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133068">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
ورزش سه: مهدی ترابی مصدوم شده و ممکن است لیست تیم ملی تغییر کند و از بین هادی حبیبی نژاد و امیرحسین محمودی یک نفر مسافر جام جهانی شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 336 · <a href="https://t.me/SorkhTimes/133068" target="_blank">📅 21:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133062">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bjoehhuV5Ch174G0JUnoGU1GKJ29IvpuGQVnX44BCktkHbnoNy5sE7Eb2Ms1JyURkRaH5b_g95p9YBzK2_OOWC9JeRJeubopckp18LZVDsU9vp9yj290zTMo6fHy_0Jk_99OuqzZ4gPk1QC8DJF7PrB0p2TlJzELFafuKyJu9OXp_JXtFA2L523rlVwGdI2reeFwqyzr25IDjz8-u1jL4mzy9u-dNsJ_8iXxhLjauUTy5XIBfWxdq9uaaizVOonvHb2W5iQCO7djOq2ROSHE0e4sdrqf7aRkiEY_3wcS4QaLpgOTvmaUrqAa7o7pj8CYkUpn1o0Jt_P__LQQZC7ndg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JGpjZBAqYGH6NmXCXM9wjGRaV7Bi_rS87-Wm24skT0ddnCPkmtXXJWY4DEB7w0aT90YF7vOdQTfyJQUM9z3FhJV6ydIqIXsUdi8JAvkBv4YkFU6GQdZnEmEyLDdnRJG_OjH0b2RwbzuIFmEfqlnEnJ3ds4aycUzx-O2nOsljker7aPXS5Difqgeitk1b3VZg_l3K5PdwElADb_rxhA4lDuBaYoBWRQMKvTIc4Y1su3GI-5xSNrdNGBmeyxxMlI128h8rxBTv3Y18Wx-4HY2lXcK9wWB7QF5ak0JkTpo6n6DRIvO7aW1aA-C-DENjWT_de1YqV3vjp3e-wAPMtervRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T-5EPzS6FrJnEYZpi5s0Fj1VXFH92th1feflzGloQN-NqFjpD-iXBC8d2LQCJDHXnOgJL_xWpfW_wsQcAZDqQGEztVtBjTyr78fPvFEO8WdCWClTBwlduAKVTzQFpu0pmAn_Lj7J1ROBrh7HdJVcMcipTgVO0vmOy-KGMZM_HqyhG8zuJZT7NWbZjNA8j_-oLh5gk-50Aa5ld9yR9Fm4EH8z5DA1QD6Ct_5yptKrwmsBWDRa_wE9cFcoopK_A1hIdWi5VdSFR9XDtjfyRxi70fnfVpJzAmNtf1cK0lGD7kf36VIYtbu7INZDF0BSHy1kW31PGPGN8m2NEFtIoX_BFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EK6Eb7lbbARqOsGrzTfGUKojHUMwDCUVDtCBO0tnbE6XGSe6R8f7J04JnNVm_VApKQBKdKKORUj_x8N6y9VvcQiJraF6ACSCMuLcTADHMgROZIgP0OS5ZRIDIolHFIb9LttDRim_ITSDy8iNT4daVeWxFFbYKtLiR6T1IM_h_TWo7MjbJ6R36oNPsNzpG9GzaPZDOGtt847E936MXbJh44nXs-KcMVyCdk_MONpJna0SsMJpCiUPQOjsORU_5nQ9bL5Xs3fvZmXrMu3xbjxX_1q_zMEalHGqs4EIhCwrWQWSy79KJcEtU03Xqf8x2B9KuYvzfz_Tk3CsWlfttEmo8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aFmGrZHmbRuU1cyc5ysu7fkojkq-sw7xdprTemskXlXzkuWJNzRgRZ2p6U7mogbUtLb28S_2Exxg1gBswVjoBpXvTMd01recD53ZF3NDsyPWfB2no7IMWYhutPV7GZ58qMrTFXuULkGmAmomvIuY3bW8ejw3LMz8a6cUl27pIFIXGrMgkHZAWtYZCSoy_JcmF0aNzBnB8PXFMNs3qT9jfhY2JFD-gPXeb0l2resZ6swOWRXjrkhBQoCuMUmTBweAFlzUjY7IgmUBFNym6a_kR-hCJhxCCK0gLcafOLHTnBxORLHnluKzFexsJaEZHFXQfgwLsm50po9dsvXnWtXiRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TH9LWtJF1VpzaD5JfjH9ioL6hKEwRPXukKET_SXhJ6Tom3zCh61SK8yhDNwOWsC3xcpTdRpnNM3BWqyCA4Y7pMTHpPmG_VW2FYFd1nP_tf7ofCvB9RAGQy1kcgo6J_i_yJeMzg76WFk-8Kce1XqImxDBw2DRjHsFSrq0TiX9AbQmjA9xCFCrS4VEVXCDEb2Q1EDv8ql9E7boAxP9wLtvHFFCP9JXQAuh6mYw41bcDV3KbMAg4e6nQVJPZh7MXTy2BXVxSbdKrjuNbhAKiwWZd8MysdOEkOtBp2CN0hHqC3nIxZlbavI0d-zzt0-CW1emz4KJheLJjamqkLBuScHbEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❌
آغاز دوباره تمرینات پرسپولیس برای حضور در تورنمنت سه‌جانبه؛ پرسپولیسی‌ها پس از وقفه‌ای چند هفته‌ای، کار خود را از سر گرفتند
.
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 390 · <a href="https://t.me/SorkhTimes/133062" target="_blank">📅 21:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133061">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇺🇸
ترامپ به نیوزنیشن: یک جنگ دیگر را پایان دادم در مجموع ۹‌ جنگ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 424 · <a href="https://t.me/SorkhTimes/133061" target="_blank">📅 21:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133060">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
قالیباف: اگر دیپلماسی را صرفا گفت و گو در اتاق های دربسته و لبخندهای دیپلماتیک بدانیم، از همان ابتدا شکست می خوریم و اگر صرفا به عملیات های نظامی و جنگ تکیه کنیم نمی توانیم از حقوق خود به طور کامل دفاع کنیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 536 · <a href="https://t.me/SorkhTimes/133060" target="_blank">📅 21:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133059">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08f4d5075d.mp4?token=PGUiOZP5V7upv0M8KoyuqM5BpeKHZP4NE_1o3_BrQ0qTU3t0r_mj_osek_P9WMliw2QkMQFTbPKhFpKW_eAdFqzyIBglOirJbbicQOUaeCBumPZSwjTrSRKMPdlr9TKhZHSqnquT08HD0rJbTvBaAHa9MHO1l4cdlnsFJI8OpQRHDUiaB3t2WbeoDtd6Wsz_fOX5bS8RlWnJaZvj2OLFHW4-r330PrPyntyq2YBrVEzs_VXvAuuaqDX0TP3y28qhHaSuUxtHG01DtTVUj2vy8PdDcVBRX_ybuGkV31TGO5LLorr2Flh7SRxfml2bjXp6RkH8wFo1oDzU4cwRL8okTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08f4d5075d.mp4?token=PGUiOZP5V7upv0M8KoyuqM5BpeKHZP4NE_1o3_BrQ0qTU3t0r_mj_osek_P9WMliw2QkMQFTbPKhFpKW_eAdFqzyIBglOirJbbicQOUaeCBumPZSwjTrSRKMPdlr9TKhZHSqnquT08HD0rJbTvBaAHa9MHO1l4cdlnsFJI8OpQRHDUiaB3t2WbeoDtd6Wsz_fOX5bS8RlWnJaZvj2OLFHW4-r330PrPyntyq2YBrVEzs_VXvAuuaqDX0TP3y28qhHaSuUxtHG01DtTVUj2vy8PdDcVBRX_ybuGkV31TGO5LLorr2Flh7SRxfml2bjXp6RkH8wFo1oDzU4cwRL8okTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🕹
گردونه شانس رایگان وینکوبت رو از دست نده، همین الان وارد سایت شو و گردونه رو بچرخون!
🎰
هر ۱۲ ساعت یک‌بار شانس خودتان را امتحان کنید و جوایز نقدی متنوع دریافت کنید.
🎁
تا سقف ۱ میلیون تومان جایزه روزانه
✅
فعال برای تمامی کاربران
📌
برای شرکت در گردونه شانس، وارد ربات وینکوبت شوید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 613 · <a href="https://t.me/SorkhTimes/133059" target="_blank">📅 21:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133057">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‼️
🟪
چلنگر، مترجم برانکو: او نمی‌خواهد به طور کلی سرمربیگری کند
‼️
مذاکره پرسپولیس بسیار محترمانه و خوب بود. حتی برانکو به آقای اینانلو گفت اگر یک سال پیش شخص شما با همین ادبیات و محتویات با من مذاکره می‌کردید شاید الان من سرمربی پرسپولیس بودم!
🟪
اما در مقطع…</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/SorkhTimes/133057" target="_blank">📅 20:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133056">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">حضور وحید امیری در تمرین پرسپولیس  وحید امیری بازیکن پیشین پرسپولیس، برای طی کردن دوران درمان خود در تمرین تیم حاضر شد.  به گزارش رسانه رسمی باشگاه پرسپولیس، در نخستین تمرین تیم فوتبال پرسپولیس بعد از تعطیلات، وحید امیری بازیکن پیشین تیم هم حضور داشت تا روند…</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/SorkhTimes/133056" target="_blank">📅 20:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133055">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇺🇸
ترامپ به نیوزنیشن: یک جنگ دیگر را پایان دادم در مجموع ۹‌ جنگ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/SorkhTimes/133055" target="_blank">📅 20:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133054">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6mxdKQmLkhxTGIKQmunYCm1bzGY1zI0mk2HBsecLBs4xbxekibp4dRPVUMNgkBMo_b_aysuKwBKfEz5Hfj5tvWcDVZIGmJPoOS28jQANokBAZiywlOKM5IE-gMZnFWSFh1P_cicd1WUcZrPR3B68Ts0LEUjvKTMKZRN70VhbHWqdzCo0T-ddAOZ9WdaSAP6oqjnvufiUAx19Mr4SLGAyCevKL9y0yKMvzNs5BpfTo8cOuKb9FOiQByYojSUR46MztGDdSFozUyfszNREQ2-oq-FKE5Y_w5cXGGsyUxscZ6KbooPVF7KHhWESXQQsyDqkSqBlchttMjSGDBEqnxgOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تلنگر | #افشاگری
🚨
‼️
نفر بعدی کسی نیست جز مدیرعامل اسبق باشگاه که در این روز ها تمام تلاش خودشو به کار گرفته تا چوب لای چرخ باشگاه بزاره تا پرسپولیس به آسیا نره و به پرسپولیس برگرده…!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/SorkhTimes/133054" target="_blank">📅 19:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133053">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mh2urITuOubYATEsT5FWdPIVYZG0jSp5BsRXpyY5CP6Ly60x3li-0u4Za4j9n6WHDKOKZUg4B1-tRrb6kUW2jLgl0HAcidaBdU6CkYa4DUTkFzu_qltkSlfaydagJF1mGT7jloHaygI7T1MSAMwGpbMnzTjtdw92suMxABQ_Tt8gkP704-R4AMzO3EKV-lqpGmhjI4M5dre6TBA_2ARydpXNKaWBQ8PV4zdwd16njJYLjBxP_9x7_myFZaZoQJNDfJaxtvLeBll2JcTefilq6yl_0VnkkRPl8DBFdDntXxNMlrYXbBpXH04f99cuUkx5iFdDDNRpErWOXvYipXZLjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تمرین امروز پرسپولیس بدون حضور خارجی‌ها و ملی‌پوشان و سروش رفیعی برگزار می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/SorkhTimes/133053" target="_blank">📅 19:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133051">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
تمرین امروز پرسپولیس بدون حضور خارجی‌ها و ملی‌پوشان و سروش رفیعی برگزار می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/SorkhTimes/133051" target="_blank">📅 18:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133049">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hd2SHtjkCm0MSKCv8VIBq9SHWbUX5_uu6HAf8xy4xWkzsiqJNXSw9O7-YXJ9JQrmOsQk5m9-DU2x4utOepmQwIeekr_-DSJQM7wvzrBCOyRNckLQ-Ba7uypT3aeDmMwV2PnL4AdkFqrF-QsNd88n933HlCWP6z1cGyhhXqYi1wGLD27vDYu_qtCQTJZvFTYN6WTt7s0BLJkmHjFyId1bmS6oNhAbZBA6OAYYGUgFDy95o7umnbjcss8raqcGuSrjNs9_sKq-1LQfz1vBkxcQn6p4HObiZMFZkMkS4qx8d3K6oKqo-83Hru8h0-VqdTwtjrzneREhOdpQE0i-SvSyyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مصطفی قنبرپور، پیشکسوت پرسپولیس و مدیر اسبق این تیم، به‌عنوان سرمربی تیم نونهالان(زیر ۱۵ سال) و مدیر تیم‌های این رده سنی انتخاب شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/SorkhTimes/133049" target="_blank">📅 16:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133048">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
کرمانشاهی، معاون پرسپولیس: بنظرم مسابقات را برگزار کنیم خیلی بهتر است. اینکه سهمیه‌ها براساس جدول فعلی باشد، خوشایند باشگاه پرسپولیس نیست. پرسپولیس روند صعودی داشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/SorkhTimes/133048" target="_blank">📅 15:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133047">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
محسن خلیلی: پرسپولیس همیشه خواهان جذب علی قلی زاده بوده اما خودش نمیاد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/SorkhTimes/133047" target="_blank">📅 15:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133046">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
فوووری   حجت کریمی، عضو هیات رییسه فدراسیون: اگر رای گل‌گهر رد شود، پرسپولیس و چادرملو با هم بازی می‌کنند و برنده آن به مصاف گل‌گهر می‌رود تا سهمیه آسیایی مشخص شود. اگر هم رای تایید شود، گل گهر راهی آسیا خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/SorkhTimes/133046" target="_blank">📅 15:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133045">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDViBqeO_T15yy5Hq45-MLU4MStHSf_uyy6KBwl8EqbzysEoMi_wGD7ucMC3UDhTJ5EX5xv8CzjRTi_EkQc6v9f3vXlhth44a6FolYROWYmFjsbnSFzkD-6KruvqPcQVc-PeioCKLNA9KUaWJSHK-3TM8kfv-kymQKvQcZANxWsCbbME8uuvFimD0slLcajeSdrF0beRPXu_hEBkgaXzTkIujjlBeuDaeH2I2Bkl3LQRRn2AZynUNkzM0PMbob2Kk5vH9HG-FCleTzXlWqlbTT-AB9eOakK8Mj8BzGJMH_4qto9Vbq5MzLzMQrcej9du5PqIFVcQ7pn0jhU1T64Izg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ به نیوزنیشن: یک جنگ دیگر را پایان دادم در مجموع ۹‌ جنگ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/SorkhTimes/133045" target="_blank">📅 15:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133044">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U49eNjBy4cpvZA0hcVTHS2Qq2NRowzyfRmEK-3kU_xSSlgJmb9XD79_jTQDPqEJNrSv695JHtue753VYCeQ5Spaa2yakSFjO6qDHHwc1qEPgKn5OjKFTGy81E0_bnHm9NDYBDOn6CQWi57Pox0VekZkCa2-Rf-cbghff80yqPOBKg7nyjgi2vXcY256g0aNs5oTQHb0AwFTYxj2ogw5wR73VsONsPVAed5SJQTSsFNqdxJk5KKQbX2jISOgdS8ZlxqLjHjapIrLRtNXPNiIaE-sNXiVvuj5ji06p_5n2klQaSxNILC2eZCBD1z9wSIyTReJt2pm5gfFvd7D95a1dCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
PulseGate | اتصال بدون مرز
🔥
اینترنت مخصوص نت ملی
⚡
سرعت بالا
🎮
پینگ پایین
🛡
امنیت بالا
📱
سازگار با همه دستگاه‌ها
♾
کاربر نامحدود
💰
پلن‌های اقتصادی از 250 هزار تومان
📩
ثبت سفارش و پشتیبانی:
@Winstn_Churchill
@PulseGatee
⏳
ظرفیت برخی سرورها محدود است؛ برای فعال‌سازی سریع‌تر پیام بده</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/SorkhTimes/133044" target="_blank">📅 15:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133042">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">✅
🔴
فرشید حقیری: حدادی 3 تا جلسه با خداداد عزیزی برگزار کرده و خودش کامل در جریان امضای قرارداد هستش برای همین نمیاد تکذیبش کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/SorkhTimes/133042" target="_blank">📅 15:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133041">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👀
صلوات بفرستید…..
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/SorkhTimes/133041" target="_blank">📅 15:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133040">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚀
صدا و سیما: جنگ پس از شکست دشمن به پایان رسید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/SorkhTimes/133040" target="_blank">📅 15:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133039">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❌
فووووووری/ با اعلام قرارگاه خانم الانبیا جنگ ۱۲ ساعته و اسراییل تمام شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/SorkhTimes/133039" target="_blank">📅 15:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133038">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
قرارگاه خاتم‌الانبیا: پاسخی دردناک به رژیم داده شد و توقف عملیات نیروهای مسلح اعلام می‌گردد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/SorkhTimes/133038" target="_blank">📅 14:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133037">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
قرارگاه خاتم‌الانبیا: پاسخی دردناک به رژیم داده شد و توقف عملیات نیروهای مسلح اعلام می‌گردد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/SorkhTimes/133037" target="_blank">📅 14:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133036">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">✅
🔴
فوری ترامپ:  هر دو طرف، اسرائیل و ایران، به دنبال آتش بس فوری هستند! مذاکرات نهایی در مورد "صلح" به شرط دوری از ناآگاهی یا حماقت در راه است.   محاصره به قوت خود باقی خواهد ماند تا زمانی که "توافق نهایی" حاصل شود.   همه چیز باید به سرعت حرکت کند. با تشکر…</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/SorkhTimes/133036" target="_blank">📅 14:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133035">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‼️
🇺🇸
ترامپ:  اسرائیل و ایران باید فورا«تیراندازی» رو متوقف کنن رئیس جمهور دونالد جی. ترامپ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/SorkhTimes/133035" target="_blank">📅 14:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133034">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❌
نائب ریس کمیسیون صنایع: امکان قطع اینترنت بین‌الملل وجود دارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/SorkhTimes/133034" target="_blank">📅 14:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133033">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lAVoKfiCzFvNjGFf88b1SyFutiW-lvkYjzMUkcGYcjORb6f1bO0OH2gmcdxlEU8P_AKZtIzo6lQdOHzsE-WfbQt-ksktRJUpsE7HfMlJ9mPxGhHxSPW9OKoA4dsefh0TJMpmmttwxi0zSZa4rv-rZv7QWft346T2R0bIna8mO_2ybQz4e7FSz7JLNiFTyJZzFWo8r3Cj3CMqRPY1knZ7ah1mv0W1sJ4lTrkBlqA5vgPOzGKlxrVmsQGqjjs92DApNry42Eqc_rfEVgHbpmWbmDKhRghxTYf7a7pZwnl07D5aYIfhdhaQJgsac8VrRgAliHx798Rjlj0aO67-3aqm6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تمرین امروز پرسپولیس بدون حضور خارجی‌ها و ملی‌پوشان و سروش رفیعی برگزار می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/SorkhTimes/133033" target="_blank">📅 14:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133031">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">✅
فرشید حقیری: امروز جلسه محرمانه بوده و سرپرست جدید پرسپولیس انتخاب شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/SorkhTimes/133031" target="_blank">📅 13:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133030">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❌
🚨
اسامی ٣٠ بازیکن دعوت‌شده به اردوی نهایی تیم ملی در ترکیه  علیرضا بیرانوند، حسین حسینی، پیام نیازمند، محمد خلیفه  احسان حاج صفی، میلاد محمدی، امید نورافکن، شجاع خلیل زاده، علی نعمتی، حسین کنعانی، دانیال ایری، رامین رضاییان، صالح حردانی  سامان قدوس، روزبه…</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SorkhTimes/133030" target="_blank">📅 13:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133029">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
مدیرعامل و رئیس هیئت مدیره پرسپولیس هیچ اطلاعی از سرپرستی خداداد عزیزی ندارند و تا به حال جلسه‌ای با او نداشته اند.
♦️
اما منابع دیگری به ما اطلاع دادند خداداد عزیزی در روزهای گذشته با شخص احمدی مدیرعامل بانک شهر جلساتی داشته است/شاهین
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/SorkhTimes/133029" target="_blank">📅 13:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133027">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pq2X4yaB5WXUHh-tT9G6vRZHLrwT5oT-MTCzXDEOy5MMqq_yqxHy2fhI_SBkVlJLnNnS8ihOAzMhNOxub_X9wZZCr4mG1BDu9DeGsSy13rzw5MuVF21ukIX8uB_SNzFe30e8NF1Ppp72782XscZHCYtdAImoPMguP0ECzyYjfiZA4LxcyoEzTZ-Y5L4yMu_fyHt-ulVDVL3Vh6roNEZIAZ2i59VEYlNR2wdfu7-XScyGJG9A8s0Wz4JoUDqHhqmXn6jen2bxDhOGMtAqnXOBSaBClatN1jpXB6gAT0hR3bHZrB_9IeOnUu-ut8u6T8mLB7qDot09T43z1CoEZb7vtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
ترامپ:
اسرائیل و ایران باید فورا«تیراندازی» رو متوقف کنن رئیس جمهور دونالد جی. ترامپ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SorkhTimes/133027" target="_blank">📅 13:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133026">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e786c6b741.mp4?token=iHv2CoxggYHSMcNPXttoFqjKcVDz-4sZw-LN2LfsPwmEnjzKb6Zmd32jwz-iOnRORxlNx--5tRyOSvgVx0z_55QQECLaJCpOaExLd6Evg90MX-VSbEXKq8KNmPx1BNg6nHUUJ0NOFPBmKJgItGoHZNJBMEBW2O7m9dusYEqe09edQ3EIEZ1jMbqnZFscJu8huWNFpjLCEhnl8lD9g2KMX1Pe7IhbHi1mIfFiqWq6ZijN3rjn9vmO1rB3_NUz8aYgMZGddR-uW8Y3QVV9PYbDmeIDDbj3UEVPP7_tzHNpAMxCi54hqim5nsTiC1fXYz_pdTQrRhe2hNJVEDwJ7B6L2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e786c6b741.mp4?token=iHv2CoxggYHSMcNPXttoFqjKcVDz-4sZw-LN2LfsPwmEnjzKb6Zmd32jwz-iOnRORxlNx--5tRyOSvgVx0z_55QQECLaJCpOaExLd6Evg90MX-VSbEXKq8KNmPx1BNg6nHUUJ0NOFPBmKJgItGoHZNJBMEBW2O7m9dusYEqe09edQ3EIEZ1jMbqnZFscJu8huWNFpjLCEhnl8lD9g2KMX1Pe7IhbHi1mIfFiqWq6ZijN3rjn9vmO1rB3_NUz8aYgMZGddR-uW8Y3QVV9PYbDmeIDDbj3UEVPP7_tzHNpAMxCi54hqim5nsTiC1fXYz_pdTQrRhe2hNJVEDwJ7B6L2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- همه اون لحظه‌ای که سایت نصفه لود میشه و VPN قاطی میکنه رو تجربه کردیم، مخصوصاً وقتی وسط بازی یا ثبت پیش‌بینی باشی.
😑
- ربات رسمی تلگرام وینکوبت کارو راحت و ورود به سایت رو آسون کرده:
👇
-
🤖
@Wincobet_bot
-
🤖
@Wincobet_bot
- برای کسایی که بیشتر وقتشون توی تلگرامه، خیلی کاربردیه.</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SorkhTimes/133026" target="_blank">📅 13:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133025">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فووووووووووووری
🚨
غیررسمی/ خداداد عزیزی به عنوان سرپرست جدید پرسپولیس انتخاب شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/SorkhTimes/133025" target="_blank">📅 13:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133024">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
اوسمار تا پایان هفته برمیگرده به ایران و تا اون موقع کریم باقری تمرینات پرسپولیس رو برعهده میگیره!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SorkhTimes/133024" target="_blank">📅 12:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133023">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
‼️
اختلال شدید در اینترنت. فیلترشکن های رایگان دارن از کار میفتن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/SorkhTimes/133023" target="_blank">📅 12:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133020">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
برای رفتن به بله و روبیکا آماده اید؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SorkhTimes/133020" target="_blank">📅 12:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133019">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
🚨
فوری؛ انفجار مهیب در غرب تهران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SorkhTimes/133019" target="_blank">📅 11:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133018">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
برای رفتن به بله و روبیکا آماده اید؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SorkhTimes/133018" target="_blank">📅 11:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133017">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
باشگاه پرسپولیس:
‼️
ما با آقای تارتار مذاکره نکردیم. این حرف‌ها برای بازارگرمی است. پرسپولیس تاکنون هیچ‌گونه مذاکره‌ای با تارتار یا هیچکس دیگه‌ای نداشته و این ادعاها صحت ندارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SorkhTimes/133017" target="_blank">📅 11:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133016">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
همزمان با صف شلیک موشکها هموطنان‌ هم صف پمپ بنزین رو تشکیل دادند تا این سنت حسنه و ملی رعایت بشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SorkhTimes/133016" target="_blank">📅 11:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133015">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇮🇷
🇪🇬
🏆
دیدار بین ایران و مصر در سیاتل از سوی کمیته محلی برگزاری این دیدار از جام جهانی بعنوان"مسابقه افتخار"(Pride Match)برای همجنس‌گرایان نامیده شد!
‼️
‼️
پ.ن:طارمی و صلاح باید بازوبندی رنگین کمون(همجنس گرایی)ببندن.
🫣
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SorkhTimes/133015" target="_blank">📅 10:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133014">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووووووری
🚨
آغاز رسمی جنگ
‼️
سپاه پاسداران خبر از آغاز رسمی جنگ با عملیات «نصر» داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SorkhTimes/133014" target="_blank">📅 10:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133013">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❌
🚨
دستیار اوسمار در راه تهران/ ساعت تمرین تغییر کرد
✈️
جولیانو والیم بدنساز برزیلی پرسپولیس فردا ساعت ۱۴ به تهران خواهد رسید تا اولین جلسه تمرینی پرسپولیس برای آماده‌سازی جهت کسب سهمیه آسیایی را برگزار کند.
⏰
تمرین پرسپولیس که قرار بود ساعت ۱۱ برگزار شود به…</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SorkhTimes/133013" target="_blank">📅 10:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133012">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
آن‌ها مداركی به دست آورده‌اند كه نشان می‌دهد چادرملو مجوز قطعی حرفه‌ای نگرفته و مشروط به يك  توافق بدهی حقوق است.
⏺
چادرملو به پيمان بابایی از يک سال قبل بدهی دارد و هنوز سندی در اين مورد ارائه نداده است،اگر چادرملو تا فردا اين سند را ارائه ندهد بعد از شكست…</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SorkhTimes/133012" target="_blank">📅 10:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133011">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❌
🚨
دستیار اوسمار در راه تهران/ ساعت تمرین تغییر کرد
✈️
جولیانو والیم بدنساز برزیلی پرسپولیس فردا ساعت ۱۴ به تهران خواهد رسید تا اولین جلسه تمرینی پرسپولیس برای آماده‌سازی جهت کسب سهمیه آسیایی را برگزار کند.
⏰
تمرین پرسپولیس که قرار بود ساعت ۱۱ برگزار شود به…</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SorkhTimes/133011" target="_blank">📅 09:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133010">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووووووری
🚨
آغاز رسمی جنگ
‼️
سپاه پاسداران خبر از آغاز رسمی جنگ با عملیات «نصر» داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SorkhTimes/133010" target="_blank">📅 08:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133009">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
آغاز جنگ ....اگه دوباره قطع شد همه چیز .مراقب خودتون و خانواده تون باشید ...خدا به همه رحم کنه .بازم جنگ .بازم استرس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SorkhTimes/133009" target="_blank">📅 08:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133008">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e2e80c06fa.mp4?token=SYk28O1FDzGKPf9nutrm3ypaR89p0C80bY7Qx4odyau7BFvFlgMcH8b7p_fK4pezQuJWEMMfBvCc0RAkyEXixEhy0BWKYV4pO1VP8qgEHi3gODlGf7X3Ba8D61j3CGt_00YTzk9gA8j4UyMQJu0zK8KcDUeOJS_1bFbKuokgYkJVYQoaXGqsqu0x_qK38VLJoLo95fHVfR_78PZBSz6aeWxxLxb7yR8pf8jxMWvPKTXKbDT0nAy-ZO3uAj6GRREkNt_AHsBqSCT6kRihBPVneg0-y7ntP8eKi0zgNao4EGOPRujwnEUUQ_nw7yNby8IBVLSygY9d-u6v2zzLUDU4FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e2e80c06fa.mp4?token=SYk28O1FDzGKPf9nutrm3ypaR89p0C80bY7Qx4odyau7BFvFlgMcH8b7p_fK4pezQuJWEMMfBvCc0RAkyEXixEhy0BWKYV4pO1VP8qgEHi3gODlGf7X3Ba8D61j3CGt_00YTzk9gA8j4UyMQJu0zK8KcDUeOJS_1bFbKuokgYkJVYQoaXGqsqu0x_qK38VLJoLo95fHVfR_78PZBSz6aeWxxLxb7yR8pf8jxMWvPKTXKbDT0nAy-ZO3uAj6GRREkNt_AHsBqSCT6kRihBPVneg0-y7ntP8eKi0zgNao4EGOPRujwnEUUQ_nw7yNby8IBVLSygY9d-u6v2zzLUDU4FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
#فوری
| کانال ۱۴ به نقل از یک مقام اسرائیلی:
🔻
ما تأیید می‌کنیم که یک تأسیسات پتروشیمی در ایران هدف قرار گرفته است
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SorkhTimes/133008" target="_blank">📅 08:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133007">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✅
ساعتی پیش ارتش اسرائیل به اهدافی در تهران ، اصفهان ، کرمانشاه و... حمله کرد ؛ این حمله از خاک عراق انجام شد و بسیار محدود بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SorkhTimes/133007" target="_blank">📅 07:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133006">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
فوری، زیرنویس شبکه خبر و تایید شنیده شدن صدای انفجار در تهران، تبریز و اصفهان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SorkhTimes/133006" target="_blank">📅 07:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133005">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1OxG6vMAJdkwBndIrjU1FrfV_7F1OesFRDxkAzh5vvBLAoMn6fXh6WAsJGbADrqtdm5cHf3NrnV-Gcm-4aX-IUX9UTEb3jEDkucGuWnedEumoLd7-AsMV8WagcaQQYEljnCeyMVUWyWc4Tq4cowkq1ksW33CgWw90OncqaKoFbnJHAlQz7T1ARTcqWe8Tzl40jPVIX5W1MLKpAT195QaO84N93ZbPK_UkrC1i8yaH01DnPl7l6BgrvaI0KCCMUJqcJ5jfYonmZjtz_8rzY5N4PwH75dwlQnQLwaSY-QGWQr2SmHflN9PbnCx6ClJq84fPZqFsoZYWowcdNdbA1Lrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری، زیرنویس شبکه خبر و تایید شنیده شدن صدای انفجار در تهران، تبریز و اصفهان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SorkhTimes/133005" target="_blank">📅 07:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133004">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vi3kqbqiq7XUi3qReQQmNqk4MAK3o-ZH4SGMpEbKff0iC4Y2XYaAgw7EFIXhq3ozWUlznMXVpyCgRz7w6eqJXf1vt05cxCvGDBXCstyxtsHCdyJ3MIQWa6swTKU5oUfWSLs02Mkc-VNskPGvA21BsTJ1M1FRurbsk_T5FRUsUxju5ybZVFW22nPBPvoDKXT4Qkj58Ze_lJDXjkS2rOrkJg1Yc5-8pAWYKBjkoyQA5UT_lLgNuwphiSEZ68uq8VNqQLMOxXsF-zhMbtSVHZH5uRtLOJOSwMjIqIb22jU5L9sLh2bPXONEcT7JwJMmkeaEl62WDNngMZd7UuY2rXFJZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس خوش‌آمدگویی برای کاربران جدید
🟢
کاربران جدید وینکوبت پس از ثبت‌نام و اولین واریز خود می‌توانند از بونوس خوش‌آمدگویی استفاده کنند.
📌
میزان بونوس تا ۱۰٪ مبلغ واریزی و تا سقف ۵ میلیون تومان می‌باشد.
📌
شرایط استفاده از بونوس:
حداقل ۱ گردش با ضریب ۱.۸
🔗
همچنین حداکثر مبلغ قابل برداشت از طریق این بونوس، ۱۰ میلیون تومان می‌باشد.
🔗
همین حالا وارد ربات وینکوبت بشید و پس از ثبت‌نام و اولین واریز خود، بونوس خود را دریافت کنید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SorkhTimes/133004" target="_blank">📅 01:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133003">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚀
🔥
الجزیره: امشب ایران حدود ۱۰ موشک بالستیک به شمال اسرائیل شلیک کرد که ۴ اصابت به تأسیسات نظامی دیوید تایید شده و چند نظامی در این حملات مجروح شدن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SorkhTimes/133003" target="_blank">📅 01:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133002">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
محمد عباس زاده با قراردادی 2 ساله به فولاد خوزستان پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚩
⭐
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SorkhTimes/133002" target="_blank">📅 01:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133000">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❌
کانال ۱۲ رژیم: ترامپ و نتانیاهو اکنون در حال گفتگو هستند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SorkhTimes/133000" target="_blank">📅 00:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132999">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❌
باراک راوید، خبرنگار آکسیوس: ترامپ به من خبر داد «الان دارم با نتانیاهو تماس می‌گیرم و به او می‌گویم که در پاسخ به ایران حمله نکند.»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SorkhTimes/132999" target="_blank">📅 00:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132998">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
🎙
بازگشا، سخنگوی باشگاه:  بعد صحبت هایی که با کادرفنی و بازیکنای خارجی داشتیم قرار بر این شد که براشون بلیط بگیریم بیان.  سرپرست شدن محسن خلیلی هم تصمیم آقای حدادی بود که هیئت مدیره هم موافقت کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SorkhTimes/132998" target="_blank">📅 00:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132997">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
✅
عقب‌نشینی ترامپ: حملات اسرائیل به لبنان با من هماهنگ نشده بود  ترامپ در گفت‌وگو با فاکس‌نیوز: از حملات اسرائیل به لبنان خوشحال نیستم و این حملات با هماهنگی ایالات‌متحده انجام نشده‌اند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SorkhTimes/132997" target="_blank">📅 00:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132996">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❌
ترامپ به کان نیوز: فکر می‌کنم اسرائیل به اندازه کافی پاسخ داده است. نیازی به پاسخ بیشتر نیست. ما می‌توانیم پس از ۳۰۰۰ سال به صلح دست یابیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SorkhTimes/132996" target="_blank">📅 00:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132995">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❗️
ترامپ به شبکه 12 اسرائیل
🚨
📰
:   در حمله موشکی هیچکس آسیب ندید. اگر نتانیاهو پاسخ دهد ، این ادامه خواهد داشت و ادامه خواهد داشت  ما بسیار به توافق برای پایان جنگ نزدیک هستیم و این توافق خوبی خواهد بود  نمیخواهم این موضوع توافق را به هم بزند. هر دو طرف حمله…</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SorkhTimes/132995" target="_blank">📅 00:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132994">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❌
باراک راوید، خبرنگار آکسیوس: ترامپ به من خبر داد «الان دارم با نتانیاهو تماس می‌گیرم و به او می‌گویم که در پاسخ به ایران حمله نکند.»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SorkhTimes/132994" target="_blank">📅 23:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132993">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✅
ترامپ: به توافق با ایران نزدیک شده‌ایم و نمی‌خواهم اکنون در مذاکرات اختلال ایجاد کنم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SorkhTimes/132993" target="_blank">📅 23:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132992">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❗️
دونالد ترامپ به Axios گفت که فوراً با نتانیاهو تماس خواهد گرفت تا به او بگوید که به ایران حمله متقابل نکند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SorkhTimes/132992" target="_blank">📅 23:46 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132991">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
ترامپ : موشکاتونو شلیک کردین بسه ، بیاید پای میز مذاکره!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SorkhTimes/132991" target="_blank">📅 23:41 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132990">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
فورییییی
🚨
🚨
ترامپ خطاب به ایران: موشک ها را زدید و دیگر بس است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SorkhTimes/132990" target="_blank">📅 23:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132989">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
#فوری | ارتش اسرائیل:
🔻
آتش بس میان ایران و اسرائیل پایان یافت
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/132989" target="_blank">📅 23:27 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132988">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❗️
🔴
نت بلاکس: ترافیک اینترنت ایران 25درصد کاهش یافت/ اختلالات شدید در اینترنت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SorkhTimes/132988" target="_blank">📅 23:24 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132987">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">❗️
🔴
نت بلاکس: ترافیک اینترنت ایران 25درصد کاهش یافت/ اختلالات شدید در اینترنت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SorkhTimes/132987" target="_blank">📅 23:24 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132986">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
آغاز جنگ ....اگه دوباره قطع شد همه چیز .مراقب خودتون و خانواده تون باشید ...خدا به همه رحم کنه .بازم جنگ .بازم استرس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SorkhTimes/132986" target="_blank">📅 23:21 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132984">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
#فوری | ارتش اسرائیل:
🔻
آتش بس میان ایران و اسرائیل پایان یافت
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SorkhTimes/132984" target="_blank">📅 22:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132983">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6a27b87875.mp4?token=X3LJKk4H7FYZ-balgn-DQhtjzDm744BdxoT3slRH4KiKmlFMqT0CnS7CTntIeokaNe7hTKOlc7jSKCLfpwnKwpIgP6zzCS6ZcfmkndQGG22F8QAYDLV6kqpet0swXKFxK3AkUXJoWbj9EJuek5N2_2vz43rZT30OAMj5X15VRMtYEpHkNAGodHugRA6rm7Sy48Ub2X48PnIXop5FhNIq2jQqL9EM9eWE5tS0MxKs0ZWZ0ioAu0RjmlJ5-Uepakknz8loG7X2epdMuWRmDa7xPnde4ZE44ssb5I-rT6YS2Mbgud80vGJAjcCp2LSeRZcvfTUXV4pXWihAffIkW5Ty0g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6a27b87875.mp4?token=X3LJKk4H7FYZ-balgn-DQhtjzDm744BdxoT3slRH4KiKmlFMqT0CnS7CTntIeokaNe7hTKOlc7jSKCLfpwnKwpIgP6zzCS6ZcfmkndQGG22F8QAYDLV6kqpet0swXKFxK3AkUXJoWbj9EJuek5N2_2vz43rZT30OAMj5X15VRMtYEpHkNAGodHugRA6rm7Sy48Ub2X48PnIXop5FhNIq2jQqL9EM9eWE5tS0MxKs0ZWZ0ioAu0RjmlJ5-Uepakknz8loG7X2epdMuWRmDa7xPnde4ZE44ssb5I-rT6YS2Mbgud80vGJAjcCp2LSeRZcvfTUXV4pXWihAffIkW5Ty0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
#فوری
| ارتش اسرائیل:
🔻
آتش بس میان ایران و اسرائیل پایان یافت
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SorkhTimes/132983" target="_blank">📅 22:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132982">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
فوری/سخنگوی کمیسیون امنیت ملی:  اسرائیل باید تنبیه بشه، امشب آسمان سرزمین‌های اشغالی را نگاه کنید  پ.ن آغاز جنگ
☹️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SorkhTimes/132982" target="_blank">📅 22:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132981">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
#فرهیختگان تکذیب کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SorkhTimes/132981" target="_blank">📅 22:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132980">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">❌
#رسمی
🔴
محسن خلیلی موقتا سرپرست پرسپولیس شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SorkhTimes/132980" target="_blank">📅 22:16 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132979">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">❗️
🔴
کانال ۱۴ اسرائیل:  ما بهتون داریم میگیم اگه ایران بزنه، از الان باید تهران رو تخلیه کنید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SorkhTimes/132979" target="_blank">📅 22:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132978">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9405d969.mp4?token=oxN8rTxEi_GnY98DoJpE4j97ECvDjMjlNbGf7N3lY0JjCnyE9siEl42r6F267biku-HiTp8uDigHIsh3BQuahYGMDvt5W6a9LVU6-PPJrkJ685SWdDgY0_RUo-s0ZTMQZPzaWPrqZyt0hN_Se-NiYqtzbi0aXLgv1DDchMCw6gDP9iZFIOB0NLp3PT9WttfVcFRRPr2mIV09-Wy_VYwbofBFIibuJlTwcWvaOXsxoKDOVc0Be9l4pFfWBzrfXD36TdnTa9jZYyEj77cqlrWWFTGzR30tsLjIdOGnH_vncUP_p1_8HljSYdBmdyq-jxC3JNE75zXgcciOS-JzQpkBSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9405d969.mp4?token=oxN8rTxEi_GnY98DoJpE4j97ECvDjMjlNbGf7N3lY0JjCnyE9siEl42r6F267biku-HiTp8uDigHIsh3BQuahYGMDvt5W6a9LVU6-PPJrkJ685SWdDgY0_RUo-s0ZTMQZPzaWPrqZyt0hN_Se-NiYqtzbi0aXLgv1DDchMCw6gDP9iZFIOB0NLp3PT9WttfVcFRRPr2mIV09-Wy_VYwbofBFIibuJlTwcWvaOXsxoKDOVc0Be9l4pFfWBzrfXD36TdnTa9jZYyEj77cqlrWWFTGzR30tsLjIdOGnH_vncUP_p1_8HljSYdBmdyq-jxC3JNE75zXgcciOS-JzQpkBSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
دیدار دانمارک و اوکراین به دلیل بیهوش شدن کریستین اریکسن متوقف شده است
◻️
اریکسن پیش از این و در یورو 2020 هم دچار حمله قلبی شده بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SorkhTimes/132978" target="_blank">📅 22:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132977">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/irjMv2pCS1YOs_nhLhMsThtyWSLBSM5qja8D1wjnVO4dx14bDaYQPzm6S0Hm6-MlQVcyPxH9NpKDjO3rXDaE5-eGRpiuanPm4kDQpw6QlRUxQQg78ZyikIMyLc4f54yXcstOIxiya2COZRay2TCKglBuTDkHIuXhT1sbwm2aMMa6l28cCrqVms3wa4Dx0kZm_2NvxLiwhwjCkWOILjT8UnwnfIuOru-OxX63Itcx6bPqkrfF30mV1kJc-oe0sZJr6YBghikMDyB4oEUSBTPVRn3Wa9pF8_QJjGaUHKAEB490ye227H83CWGHCP_GG01BFcKW0wL9aJrR4ao-0lRWMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اریکسن دوباره وسط بازی سکته قلبی کرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SorkhTimes/132977" target="_blank">📅 22:12 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132976">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فووووووووووووری
🚨
غیررسمی/ خداداد عزیزی به عنوان سرپرست جدید پرسپولیس انتخاب شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/132976" target="_blank">📅 21:38 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132973">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vq4ciceRGhFTG65T6Ljr3LtqnCAIgZG4zM919pPYyO_j4CZFsxrKuDilj-IRHiMgBM0jRy8mwcOAtRUvo7d1usH2N3AE2BxO59vdAbqClHsF7qGIQfwcKBO1SPPSspQ7x86uDl-WlEhN_JO8MYPLnRePbAmvQPKJBeyxkl7tmU1ZDM7NtzUCCFKa1VWDCR1mAetHyFWnOy-G-3Cb1iYublS_lUkst9dFI-CQGDIh8v-QBxpOPkh_GAhQBWUZTJcvu_GYWr6NMU85LtnRm3caX3eNbKNBjkJy8jZRpLl2uEJVg9q2xlzKyHtGTwEAQmFcupR1LPx5j4cUfEP2c-gzOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚽️
دیدارهای جذاب دوستانه ملی امشب رو با آپشن‌های مختلف در سایت اسپورت نود با بالاترین ضرایب ممکن پیش‌بینی کنید.
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SorkhTimes/132973" target="_blank">📅 21:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132971">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">✅
فرشید حقیری: امروز جلسه محرمانه بوده و سرپرست جدید پرسپولیس انتخاب شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/SorkhTimes/132971" target="_blank">📅 20:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132970">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9383ef4fbd.mp4?token=f8_0_nu4xLxhP2ZFyamOcVpnUlalaYGbYyMe1Rr_MHoQ_SJ6p6RCNEuDBINiNOlVF34EQHy0ZxNaD949i2-Tk5TUBzuDWgTRC6SK8PV44OE4F-W-TJz1WSQnA8pBj5fxkRnrO87z1-OZCKcwdnwlYTEuWRaWfCnz0MvDr0V65DTrX58gPFYLZThXFkb02ouUI-DMAqGTreKnelWt0NV7bI6haMRFfKpg-eSs2NNq5JqPoMjv2LaPWRO3loS4Uvi2THaTr4BU9HnjfsybHMYZ5djZm1nwUN7BVUFKFyLs-bvIppykbfjhQKZIFd0rVSkGn9uT6CIG91quFltdoz8IBx1QKeYmRHQNMG_7S4xyCakGVKNzwSmjZfkeCKk_evsPrWtdpf8XKxg6phWxtHOw3lFCqqxTtj62E6bIiRB7-DSNpEsKP0NOCTvCnSyYHtU4DxzMoLnZhFTGc34SKAqpwfPDRs1CIVkHAoAD_O8CjHET4r5C4kFBz7-BbNTuI1KU4LApKKktWusytG-VgnAf4PX9qmjHQ9itaufsYzyVMOuWoiicPg41_i6_zvg-LXy6yaR3T9kye8iNg2Cc17RXACwQVQuXpyKmVmNeP5is5emx3ETRvREtynaNXBsX_J-byBc5z3F3lHzUX071RbBonjQRnJG0Mtv1_costN_M2Nc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9383ef4fbd.mp4?token=f8_0_nu4xLxhP2ZFyamOcVpnUlalaYGbYyMe1Rr_MHoQ_SJ6p6RCNEuDBINiNOlVF34EQHy0ZxNaD949i2-Tk5TUBzuDWgTRC6SK8PV44OE4F-W-TJz1WSQnA8pBj5fxkRnrO87z1-OZCKcwdnwlYTEuWRaWfCnz0MvDr0V65DTrX58gPFYLZThXFkb02ouUI-DMAqGTreKnelWt0NV7bI6haMRFfKpg-eSs2NNq5JqPoMjv2LaPWRO3loS4Uvi2THaTr4BU9HnjfsybHMYZ5djZm1nwUN7BVUFKFyLs-bvIppykbfjhQKZIFd0rVSkGn9uT6CIG91quFltdoz8IBx1QKeYmRHQNMG_7S4xyCakGVKNzwSmjZfkeCKk_evsPrWtdpf8XKxg6phWxtHOw3lFCqqxTtj62E6bIiRB7-DSNpEsKP0NOCTvCnSyYHtU4DxzMoLnZhFTGc34SKAqpwfPDRs1CIVkHAoAD_O8CjHET4r5C4kFBz7-BbNTuI1KU4LApKKktWusytG-VgnAf4PX9qmjHQ9itaufsYzyVMOuWoiicPg41_i6_zvg-LXy6yaR3T9kye8iNg2Cc17RXACwQVQuXpyKmVmNeP5is5emx3ETRvREtynaNXBsX_J-byBc5z3F3lHzUX071RbBonjQRnJG0Mtv1_costN_M2Nc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نبویان: زمان توافق نهایی در متن مذاکرات نامشخص است و پایان تحریم‌ها به آن موکول شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/132970" target="_blank">📅 20:35 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132969">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f750c48735.mp4?token=FV_jDcVxDe-GUgxjflWJRZpsepQV6Fx3I2UsgIe8adYMFgWu1asFZLHF363hsRQiDp4Q-e3ev8sHTIULbH3NPlbM-flXGXcYcmtLAznK0kGdWBIQW0t-z1-OPeoalpK611zg6vtIKkkXO_ov4ISCmC9GQjfAw8Yc3TfjPlncv7TVXQQGtKOVg270IWfw3tttkMoX7QSjODS6n2i6iF9i150FOe2EkcQN-78VFVI7MBcLHwI-272Zb2BwY7yr-4ofOD7hvrX8ya9bge1NQO5xq3Wp91J1YHgeYZUm3zuqUAlXPFu_oUPE3j6DQ73mlQKL4QUh4uKMlWtFPkR_En-DzEfzwq6EKJGtQEkDvSS6VyKw2HlQkQKcK5ryKVfGlrAb4t_JrvgvQUzYrdEDoxsw6LM33meT7dW0o6du2mk9ySnhkSih0x4qYsGHSYKmqJvssbXvke5rzKXHudyYFzOASBOA3nXnxIo4cZXPWXH7aPfjOUpZBLW5uZyp6TCnSkr-rTLhjf0d8EM0w9LjgtRLXlxdH6zrbQUQ5T4IZa3p-NLGXCcOFOIlXwHRx4CYY5IJ-W15CabVTu0ucMzunjyFj8oVSUSGTpIZLevd4m8mq696KiI0tdP_bAcSdEjSBIYYW1eVLD4Oe4orZcMoeXkwIaFs6kHzhCZdz1R1Fz7EblE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f750c48735.mp4?token=FV_jDcVxDe-GUgxjflWJRZpsepQV6Fx3I2UsgIe8adYMFgWu1asFZLHF363hsRQiDp4Q-e3ev8sHTIULbH3NPlbM-flXGXcYcmtLAznK0kGdWBIQW0t-z1-OPeoalpK611zg6vtIKkkXO_ov4ISCmC9GQjfAw8Yc3TfjPlncv7TVXQQGtKOVg270IWfw3tttkMoX7QSjODS6n2i6iF9i150FOe2EkcQN-78VFVI7MBcLHwI-272Zb2BwY7yr-4ofOD7hvrX8ya9bge1NQO5xq3Wp91J1YHgeYZUm3zuqUAlXPFu_oUPE3j6DQ73mlQKL4QUh4uKMlWtFPkR_En-DzEfzwq6EKJGtQEkDvSS6VyKw2HlQkQKcK5ryKVfGlrAb4t_JrvgvQUzYrdEDoxsw6LM33meT7dW0o6du2mk9ySnhkSih0x4qYsGHSYKmqJvssbXvke5rzKXHudyYFzOASBOA3nXnxIo4cZXPWXH7aPfjOUpZBLW5uZyp6TCnSkr-rTLhjf0d8EM0w9LjgtRLXlxdH6zrbQUQ5T4IZa3p-NLGXCcOFOIlXwHRx4CYY5IJ-W15CabVTu0ucMzunjyFj8oVSUSGTpIZLevd4m8mq696KiI0tdP_bAcSdEjSBIYYW1eVLD4Oe4orZcMoeXkwIaFs6kHzhCZdz1R1Fz7EblE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نبویان: بیشتر پیش‌شرط‌های ما در متن یادداشت تفاهم با آمریکا نیامده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SorkhTimes/132969" target="_blank">📅 20:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132968">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❗️
🔴
کانال ۱۴ اسرائیل:  ما بهتون داریم میگیم اگه ایران بزنه، از الان باید تهران رو تخلیه کنید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SorkhTimes/132968" target="_blank">📅 20:21 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132967">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
فوری/سخنگوی کمیسیون امنیت ملی:  اسرائیل باید تنبیه بشه، امشب آسمان سرزمین‌های اشغالی را نگاه کنید  پ.ن آغاز جنگ
☹️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SorkhTimes/132967" target="_blank">📅 20:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132965">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">✅
اعلام سخنگوی باشگاه پرسپولیس محسن خلیلی بعنوان سرپرست تیم انتخاب شد  پ.ن : علی بازگشا توی مصاحبه اش از واژه فعلا استفاده کرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SorkhTimes/132965" target="_blank">📅 20:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132964">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7496233f9e.mp4?token=tFqdJGfUNWaiWwLaMitZEZtW-CsVgR-IQpIcFQ2Jd1K0mDBehGOPW48BkmXRfaTS2deN3QXDhsQoeEHAyZ8pzdSNPSJUEkIPn0YM1a-1vQ7d5QUsNZDZfN_7etbxEE6RiSD8HAEe6lwgGCjoo7RiKITwB_SjVnXDEBlwVEVE2iw7fcQG0FWWl3jpde-U48CCetZzgsCMJprnucjyKTIrBn9ajLX9wz06hwpT5QUFUF9QQ1_bRQ1YFwdXMzjQOhWq5SFBfXQ8eqH8WFP7Ciggt5xc2kmcn_pefknjuMGbufScxXLwWxPwmxuppRhCwcpAbXuwx-CxpNdaOQOTAwZitw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7496233f9e.mp4?token=tFqdJGfUNWaiWwLaMitZEZtW-CsVgR-IQpIcFQ2Jd1K0mDBehGOPW48BkmXRfaTS2deN3QXDhsQoeEHAyZ8pzdSNPSJUEkIPn0YM1a-1vQ7d5QUsNZDZfN_7etbxEE6RiSD8HAEe6lwgGCjoo7RiKITwB_SjVnXDEBlwVEVE2iw7fcQG0FWWl3jpde-U48CCetZzgsCMJprnucjyKTIrBn9ajLX9wz06hwpT5QUFUF9QQ1_bRQ1YFwdXMzjQOhWq5SFBfXQ8eqH8WFP7Ciggt5xc2kmcn_pefknjuMGbufScxXLwWxPwmxuppRhCwcpAbXuwx-CxpNdaOQOTAwZitw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حضور پرسپولیسی ها در مراسم ختم برادر حبیب کاشانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/SorkhTimes/132964" target="_blank">📅 19:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132963">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
فوری/سخنگوی کمیسیون امنیت ملی:  اسرائیل باید تنبیه بشه، امشب آسمان سرزمین‌های اشغالی را نگاه کنید  پ.ن آغاز جنگ
☹️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SorkhTimes/132963" target="_blank">📅 19:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132962">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✅
سروش رفیعی به تمرینات پرسپولیس فراخوانده شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SorkhTimes/132962" target="_blank">📅 19:26 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132959">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e27207295.mp4?token=m4UMhNBVYPr0rOwJwpbIpSB_j0Qc8p4wUB2pbFQ49uknxddqBSsiExmbfP90o90kkjKoMxGmaitV3UAlL_3MKXhXMqXqwB2gs2NBjIx39xNpGxI3498LLxKhstxJKpB791aVqMkrCuRA-pcwgoGlYLEJEzRaVTZ-A-EBXPOah0wIJf2-lSQHAyKwwdbUCyC5MQnW6OEY4I0KNh070P6M78Kh1ScE-ZcdHezcFTyvpfHr4ISba3JKBKQy8le-lCJ44WdC_yxbMk-o08wnhQYt5AuwFYpcpHHu7tKijj7dFMEr5AkR5ybbTKpsQoKwAXN76WZo4uymXzvQ4BJEkwFuoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e27207295.mp4?token=m4UMhNBVYPr0rOwJwpbIpSB_j0Qc8p4wUB2pbFQ49uknxddqBSsiExmbfP90o90kkjKoMxGmaitV3UAlL_3MKXhXMqXqwB2gs2NBjIx39xNpGxI3498LLxKhstxJKpB791aVqMkrCuRA-pcwgoGlYLEJEzRaVTZ-A-EBXPOah0wIJf2-lSQHAyKwwdbUCyC5MQnW6OEY4I0KNh070P6M78Kh1ScE-ZcdHezcFTyvpfHr4ISba3JKBKQy8le-lCJ44WdC_yxbMk-o08wnhQYt5AuwFYpcpHHu7tKijj7dFMEr5AkR5ybbTKpsQoKwAXN76WZo4uymXzvQ4BJEkwFuoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤍
🎥
ویدیویی از ورود تیم ملی ایران به هتل محل اقامت خود در تیخوانا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/SorkhTimes/132959" target="_blank">📅 18:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132958">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
فوری/سخنگوی کمیسیون امنیت ملی:  اسرائیل باید تنبیه بشه، امشب آسمان سرزمین‌های اشغالی را نگاه کنید  پ.ن آغاز جنگ
☹️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SorkhTimes/132958" target="_blank">📅 18:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132957">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❌
شورای صنفی نمایش، با پخش سه بازی ایران تو جام جهانی در سینماها موافقت کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/SorkhTimes/132957" target="_blank">📅 18:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132955">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
فوری/سخنگوی کمیسیون امنیت ملی:  اسرائیل باید تنبیه بشه، امشب آسمان سرزمین‌های اشغالی را نگاه کنید  پ.ن آغاز جنگ
☹️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/SorkhTimes/132955" target="_blank">📅 18:41 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132954">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
مدیرعامل و رئیس هیئت مدیره پرسپولیس هیچ اطلاعی از سرپرستی خداداد عزیزی ندارند و تا به حال جلسه‌ای با او نداشته اند.
♦️
اما منابع دیگری به ما اطلاع دادند خداداد عزیزی در روزهای گذشته با شخص احمدی مدیرعامل بانک شهر جلساتی داشته است/شاهین
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SorkhTimes/132954" target="_blank">📅 18:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132953">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a52FqRy86PiKVcTkj0pN9bUbwp4v-eXUwjiskiU-cgetLgqXT22mxOAPbxQ3NFTm5CTHuBGsw_RHO6fC-Xx6Fp6ICZLPep0B170k9-w0S2azKfDbPW_Zwx3FruDiuxS8EpsCVb_ejIeAX9xtNIugNtDKelyOXzX12HiwIYpghMrTO-XiGVUwSjKOO6RiTrmKhRnbd24nRPWQa37Uo8o9YTttV4_8tIotd70TBh3LYpy2raN1kDcRNAPjMTqtg46JEQW5mFoCyB-Q20_D00DY4M_69nqvY-IlCpBbJOSDbl3suC3w0T_P4XvpikePwzn5MZ46a4mjVEHO59nxCfgpmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/سخنگوی کمیسیون امنیت ملی:
اسرائیل باید تنبیه بشه، امشب آسمان سرزمین‌های اشغالی را نگاه کنید
پ.ن آغاز جنگ
☹️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SorkhTimes/132953" target="_blank">📅 18:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132952">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
مدیرعامل و رئیس هیئت مدیره پرسپولیس هیچ اطلاعی از سرپرستی خداداد عزیزی ندارند و تا به حال جلسه‌ای با او نداشته اند.
♦️
اما منابع دیگری به ما اطلاع دادند خداداد عزیزی در روزهای گذشته با شخص احمدی مدیرعامل بانک شهر جلساتی داشته
است/شاهین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SorkhTimes/132952" target="_blank">📅 18:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132951">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❗️
🚨
برخی منابع معتبر:   خداداد عزیزی حتی قرارداد هم بسته!
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SorkhTimes/132951" target="_blank">📅 18:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132950">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فووووووووووووری
🚨
غیررسمی/ خداداد عزیزی به عنوان سرپرست جدید پرسپولیس انتخاب شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SorkhTimes/132950" target="_blank">📅 18:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132948">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
یه سری منابع معتبر اعلام کردن که با وجود اینکه محسن خلیلی سرپرست موقت شده، خداداد عزیزی افغانی سرپرست قطعی پرسپولیس میشه!
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SorkhTimes/132948" target="_blank">📅 18:26 · 17 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
