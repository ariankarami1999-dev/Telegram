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
<img src="https://cdn5.telesco.pe/file/Q9ju-4Oqm_lw00WxzMmgyUZk5Jeo7lqM-ZDBghPgnkcQWI0S48yKFphb9NmxOFi88r2_UaEqKM89SrnTAi7_L5ZIqO5WAXulhtSFVz5wbngaf3myJMBLnXeYRQWGDnYk98crWjMW_aCUeUc94BkyQsqfCMZbdsm34RsaKsckLMqk7Dk8VjOWkb0k73uxK-41Z93f9YtyyfKeDvICh7BOJyawxI8GFNyuoJcneqpCK03vtovT6JbQm1GrpYjPARbPskhMv9gu_zRSL0j1Rz_tLR379R6RxKwbmqyK3tjrjr6LHyKCe0a8XriGEIaiL1VMakWOSi4HRvzJiI24b4pd9A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 173K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-14 17:08:24</div>
<hr>

<div class="tg-post" id="msg-90904">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4e1409299.mp4?token=U5dxOf8Y2quHfZrQkAa04I4saQ8T9_JTVrHjbG9T7k2imTestgj3e6NkVub7KP26oagrjHrPTCs4sPcbFoZyQQFfzm-4VgloivBsCVeyz7CWqynRRQ7DwYkB_WDxa_HsKaya7x3mzwZdycNcMHD2r1eIhkR3PaCYunX5hkuQ_atG0T4tdlfoBZ6ATDM8ZsCTsWOJxsDo659qzRQAKnnPbruEfdySon8Jv99771K9lmqylfbi_VzU1LbBTgTe8HFN7nxEkXoOB_lBK-mnyPcqK9fQ9EX-gncWH_ZzlJzm4tCio-5atrRPlQPZxwe-_5EA1ermZoG7SohSm5pv4DMGSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4e1409299.mp4?token=U5dxOf8Y2quHfZrQkAa04I4saQ8T9_JTVrHjbG9T7k2imTestgj3e6NkVub7KP26oagrjHrPTCs4sPcbFoZyQQFfzm-4VgloivBsCVeyz7CWqynRRQ7DwYkB_WDxa_HsKaya7x3mzwZdycNcMHD2r1eIhkR3PaCYunX5hkuQ_atG0T4tdlfoBZ6ATDM8ZsCTsWOJxsDo659qzRQAKnnPbruEfdySon8Jv99771K9lmqylfbi_VzU1LbBTgTe8HFN7nxEkXoOB_lBK-mnyPcqK9fQ9EX-gncWH_ZzlJzm4tCio-5atrRPlQPZxwe-_5EA1ermZoG7SohSm5pv4DMGSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازیکنای فرانسه وقتی تو جام جهانی به سنگال گل میزنن:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/Futball180TV/90904" target="_blank">📅 16:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90903">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4ab6aa38c.mp4?token=UVNtp3FFuqn_U6PROxuPv-KQIkjB0A6ykNeKWB_O-fYViG-zdWdO5bqTP1pt7jFPZWlJRkbN1ZgeF27ZjW8exuPQjFa3tC3x062E5MoESuR9nXltnlrigWBFF6PO9rNnrFCP98LYiVw67fCpEWBCA-EkShlD2S2w-Pp9cuvT7XP47cXJED1pBK84x5aVyNqBQsZhwijdolTfCjgrYUyN1e9RMx3cPMOApFeElxMC5tCSkS8tpFaKQRxTPhlqUvBxuBMu23G5erZ6Ew_g7rtvTbR-g-zOgPrPzJHsbHXbK2i21_52BGjCpcW9X48rzOXewK5ejrsxaahxfdafV5q-9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4ab6aa38c.mp4?token=UVNtp3FFuqn_U6PROxuPv-KQIkjB0A6ykNeKWB_O-fYViG-zdWdO5bqTP1pt7jFPZWlJRkbN1ZgeF27ZjW8exuPQjFa3tC3x062E5MoESuR9nXltnlrigWBFF6PO9rNnrFCP98LYiVw67fCpEWBCA-EkShlD2S2w-Pp9cuvT7XP47cXJED1pBK84x5aVyNqBQsZhwijdolTfCjgrYUyN1e9RMx3cPMOApFeElxMC5tCSkS8tpFaKQRxTPhlqUvBxuBMu23G5erZ6Ew_g7rtvTbR-g-zOgPrPzJHsbHXbK2i21_52BGjCpcW9X48rzOXewK5ejrsxaahxfdafV5q-9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دفاع های تیم حریف مقابل فرانسه
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/Futball180TV/90903" target="_blank">📅 16:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90902">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XCOdbfrkQZcCPsuZF7_zSaYhv037Gki8CWhEYhQajqzx3fX2m8M_Fbjw_vronNJ4oPLxsrGBeWfAajaRusiyy56s0VXvIlvT0KKaLlBTfHzlgp9ve-BQKvwe6YX3rkAKfJNUa5_8dweah_Sg2PJgMuf-ZfTgM6-b2oppUN6Bvy4YF_DfdeBKp14qpN-isv-_UgneUJaP61wk6aTynb_dkDujgB73vLZfcTQLhn_vxav4uIbmw9agvKySKx9fsPPOnfE7XTBUinXXO6Kjozb18DNovjDrkbfBjGoxA6EUnMOv0GEU9E2b89tW372KFapky0qiacKqqFkOJPs1gOCknw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/Futball180TV/90902" target="_blank">📅 16:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90901">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZnxL1njXk8RyJACnn8B-tG6Otcq0UWIa_Kp3zx6Gcr4y-ChJ7IRC05VibRE5Q2xbq9dPIAi90E_kAA4RshQe1xUr6R49CbLMb8axDzaKiQ5IQRBbSKQAEM4qntRBWZOY3ogwCwxpKt3FNGcLjt3pGIOOGzJqmWqL2ca8OG2aiO7WJqqGf1hIFr2x6UNXP0CTWUwM9oQTx6zJQVLvYCkSkZIU_MBNmbGMIQS65-MsN9GBQO6hfuHwrtZqtsIdT6kDlgl_9ojWmC9FezvhutC4vWskhUBRsMPkmKmCnmO0KHrqDig5h7oPukwc1K_j5ObS_GKO73aekAfHlN5r-4FMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Out Of Context Football:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/Futball180TV/90901" target="_blank">📅 16:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90900">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1ebbd4911.mp4?token=PPQ1FwURlPksKxxBvw2i6fQeDmhz5sQPDJLar52w1iM8Tl0PLmx-8Iu-YyNos4B6oZ04eMt9Ul1li8azEP8pN8oDdC-uOJ905ICJUuamYhudG4fD5FvTZ2JVHpCDd8gBQ3F83s4aDoDY-ElNK8PNVsECCq1EChwwjdrSjQ7e0_w6l-Wbc9Xv4PXuDW3TYjpKfXL8zIUZ-F9eSsW2cxSo4TTv_t6T0vLNsC-BVV6uKbbV1dL1gVhYAbIpBgpn27RfTy6_u8a151D_nMGekZUsUrdr2lzceEHRRis7iOML0R7aonojNKewki_yywme1o5PNvFrLtjnYijrHfsshNz-ZWkTY8YPrXtmZEEbsorYu-kKnoGdj4MHlF8kR19Htu3z3bS5bd1u2ii10i3ObJE6Xeoc-52AZjSxL1a-JNWRfuvMHOSW22DEQ2TYqE9V7Hi65CmeFnskhs_5keg_y3m8FVXqPyPx906Mr1xI0I0YxS-_A8aZ3-z2ib_aTaWiPo8Sg3wtOjYamKaXFSD9MOA6tH3fvllitCD4TKWyEER7-2OsVQo_lXiSxGA8GJN_at3_NFYcCklr8FrqxGJpmjVoHLAplNQDTElKAwpUExH0XESJ911bu92JEctwi_pzhgahEVDWi2zCwW3hjqkyUKlKVx9JtdRaIjfJO6ILYGrv2ZY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1ebbd4911.mp4?token=PPQ1FwURlPksKxxBvw2i6fQeDmhz5sQPDJLar52w1iM8Tl0PLmx-8Iu-YyNos4B6oZ04eMt9Ul1li8azEP8pN8oDdC-uOJ905ICJUuamYhudG4fD5FvTZ2JVHpCDd8gBQ3F83s4aDoDY-ElNK8PNVsECCq1EChwwjdrSjQ7e0_w6l-Wbc9Xv4PXuDW3TYjpKfXL8zIUZ-F9eSsW2cxSo4TTv_t6T0vLNsC-BVV6uKbbV1dL1gVhYAbIpBgpn27RfTy6_u8a151D_nMGekZUsUrdr2lzceEHRRis7iOML0R7aonojNKewki_yywme1o5PNvFrLtjnYijrHfsshNz-ZWkTY8YPrXtmZEEbsorYu-kKnoGdj4MHlF8kR19Htu3z3bS5bd1u2ii10i3ObJE6Xeoc-52AZjSxL1a-JNWRfuvMHOSW22DEQ2TYqE9V7Hi65CmeFnskhs_5keg_y3m8FVXqPyPx906Mr1xI0I0YxS-_A8aZ3-z2ib_aTaWiPo8Sg3wtOjYamKaXFSD9MOA6tH3fvllitCD4TKWyEER7-2OsVQo_lXiSxGA8GJN_at3_NFYcCklr8FrqxGJpmjVoHLAplNQDTElKAwpUExH0XESJ911bu92JEctwi_pzhgahEVDWi2zCwW3hjqkyUKlKVx9JtdRaIjfJO6ILYGrv2ZY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاراگوئه هم وارد چالش معروف شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/Futball180TV/90900" target="_blank">📅 16:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90899">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvulhqin7OwujodyuJcq9vNd9ZCLUzqTfwylYvSKY7NCGfqUqlsUTHPRPKb1b2H6aRfO30-pFjwy0NoOYbh91P_2EzPaRDaVhMYhTSpcw-Cei1L-xd3xgrQteL7E9wnN62A3wUdaabW_7Jynq3k5w6bePk1iu7Vj7wEZ7X4DESh9yWM-bBIJO6agCh3SJ6anABz7Wituo2xgZDq7khxk6I5m5lNyxEqYTOugKR5VQF6NOXNaY2Q60ysfaD2raj6HqrAX7ldq_Rlbex6OGGOFfrznE_wnNCIKp1-dJzoDr8pTHBBF4gy5qeNM-yXr-VJOzlqpBac9fI_f_OOf_iZ7Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
👀
#دانستنی‌های_جام‌جهانی
🇨🇻
فقط یک یادآوری که کیپ ورد برای اولین بار در تاریخ خود به جام جهانی فیفا راه یافته است و چیزی که این را حتی خاص‌تر می‌کند این است که آنها دومین کشور کوچک‌ترین در تاریخ هستند که به این دستاورد شگفت‌انگیز رسیده‌اند!
🤯
👏
🇨🇻
🌍
کیپ ورد کوچک‌ترین کشور از نظر مساحت زمین (۴۰۳۳ کیلومتر مربع) و دومین کوچک‌ترین از نظر جمعیت است، با تنها حدود ۵۲۵٬۰۰۰ نفر، پشت سر ایسلند، که به جام جهانی راه یافته‌اند!
👀
برای مقایسه، هر ایالت در چین، آمریکا، هند و اندونزی جمعیتی بزرگ‌تر از کل کشور آنها دارد… با این حال کوسه‌های آبی در راه بزرگ‌ترین جشن فوتبال هستند!
✔️
💥
و این اتفاق تصادفی نیست! کیپ ورد سال‌هاست که چیزی خاص ساخته است: دو بار به یک‌چهارم نهایی AFCON رسیده‌اند (۲۰۱۳ و ۲۰۲۴) پیروزی‌های معروفی برابر غنا، مصر و کامرون کسب کرده‌اند.  بازیکنان با استعدادی تولید کرده‌اند که در لیگ‌های برتر اروپا می‌درخشند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/Futball180TV/90899" target="_blank">📅 16:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90898">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3257da74ef.mp4?token=i27EqXvqWBD55WV7s8WClOyyNhPRhK37lNl4TYcQq_XjV5UCZN5SlpP392GFTdtkeUz1gf5zbmcwY6EzOPj9ghej3ufKfBu9Wn8L0sUzxYMLjzynhqt8kWZ4912brTFH_Vpp_DeuvXqaknX1KjhB6TsIhEaJi0blS8jPptmVtCUDHclHn6mOo-Sck0agw1sLJhE7sx7j7m5Qa2f2QdnhcPlYqfJ26RsW7znSk9hE44lg5p_FUuA9waIWPiNdkIyg2E1J98rUbOzFs-1m7sU1TD5KLSj_XY5GdubfIuLFmg7eot6sCnDPl4thngJGQrgTeGJ8o5CrT9ZYB2krfz6gZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3257da74ef.mp4?token=i27EqXvqWBD55WV7s8WClOyyNhPRhK37lNl4TYcQq_XjV5UCZN5SlpP392GFTdtkeUz1gf5zbmcwY6EzOPj9ghej3ufKfBu9Wn8L0sUzxYMLjzynhqt8kWZ4912brTFH_Vpp_DeuvXqaknX1KjhB6TsIhEaJi0blS8jPptmVtCUDHclHn6mOo-Sck0agw1sLJhE7sx7j7m5Qa2f2QdnhcPlYqfJ26RsW7znSk9hE44lg5p_FUuA9waIWPiNdkIyg2E1J98rUbOzFs-1m7sU1TD5KLSj_XY5GdubfIuLFmg7eot6sCnDPl4thngJGQrgTeGJ8o5CrT9ZYB2krfz6gZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
‼️
رضا شاهرودی: علی‌دایی به مادرم فوش داد منم باهاش دعوا کردم
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/Futball180TV/90898" target="_blank">📅 16:01 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90897">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cb836e7b3.mp4?token=qo09oWIUx1v08m4CD4KeT6P1HwwG6RR3ogmbISu74Eu-mGNpiquRA5CzcLWFUGUOPM6_ogJyKNbFoadja47bE50vAVGvvgS6VIaJXvmHXPelApLa3gKDhWTW62_kHMbeSL0l00gkvOgqq_brmX3v40UHDdFtnbdMbYvbx7Z6uOKlUJDh5EX8gPHKN75zpT9s5i0mQ-6iBVjuNtd2C0Gnvu0Yh5khtGz6cKPicRWxOCmJmF_PceEZpUHNyvxgxhw9qpLMe54dCVJfnx9IsmYGSU5dLvX2D0niHi2npDR1l2o_NPKzGHO-s5sRrkHpI3r3netqzC9bp8HVaeX1nGKCjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cb836e7b3.mp4?token=qo09oWIUx1v08m4CD4KeT6P1HwwG6RR3ogmbISu74Eu-mGNpiquRA5CzcLWFUGUOPM6_ogJyKNbFoadja47bE50vAVGvvgS6VIaJXvmHXPelApLa3gKDhWTW62_kHMbeSL0l00gkvOgqq_brmX3v40UHDdFtnbdMbYvbx7Z6uOKlUJDh5EX8gPHKN75zpT9s5i0mQ-6iBVjuNtd2C0Gnvu0Yh5khtGz6cKPicRWxOCmJmF_PceEZpUHNyvxgxhw9qpLMe54dCVJfnx9IsmYGSU5dLvX2D0niHi2npDR1l2o_NPKzGHO-s5sRrkHpI3r3netqzC9bp8HVaeX1nGKCjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇬🇭
حرکات موزون و عجیب کی‌روش سرمربی غنا در تمرینات بعد ریدمان‌های اخیرش
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/Futball180TV/90897" target="_blank">📅 15:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90896">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/guzzSlEWr6yxK9YELKj47kNGpoism0ll__4FC8c-oZarMMQt5SapUVDUcaYNcIeg8Qord_IYpLPePhTrWjWZU9yB8id6KhC1bxQdIkiNevx1ZpVDISw6hSdtyStE7OUPK-EBlsv_4tlw9gwwDfMN0spFElsrkP_6FOaLTMc-OTqpz0oNgQtVQxha0CC7VYykcQqdcQvg8X32Ui5m6y0w7H4DzW-_EX4SFtIWfJdS1zjUCC8sUMd_HW_iLk7U23RANmfJ_twTwRjG0SMB7iXkutno5RUGDUCppgZtafMhR8x_YtaSO21AOjdA8Q4-quIcDwjWR4ZcPnrSH2mZtT4T4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه ادوات بازیکنان نسل فعلی فوتبال و گذشته؛ واقعا نسل‌گذشته چه کله‌خرایی بودن
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/90896" target="_blank">📅 15:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90895">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d49121b221.mp4?token=kv7YA0_ioYwznGAGL8vZytJMOSHKqrIZbxDLqTIvApJ4fYcneaHal79TdwwwdSD7NyMm5kl_X5QLt1NswqfMIsdYTyG2d7V7Y9RTwlxQTCp4aQnr3hWyVe_y7MfztiuOxTl2HEOzUOEEYFjT-5SXOAphkOP1p-c_PhcIoYgvg809eUNsY3SPmwp_kdNTcXT9bHTarr2Mi2u10hjQ2exuW0Nlc3Nl5vJvpFDHG84BNdYbUbgx7FbhdCXAGBofv7GOao66J4G_6PMV1DwMAamb7LpWEqpGzJSBh1k7DG_Tx2KSRVLqpnj1QkJTQXVSP6aXp1LI9PApRgux8owSStO-8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d49121b221.mp4?token=kv7YA0_ioYwznGAGL8vZytJMOSHKqrIZbxDLqTIvApJ4fYcneaHal79TdwwwdSD7NyMm5kl_X5QLt1NswqfMIsdYTyG2d7V7Y9RTwlxQTCp4aQnr3hWyVe_y7MfztiuOxTl2HEOzUOEEYFjT-5SXOAphkOP1p-c_PhcIoYgvg809eUNsY3SPmwp_kdNTcXT9bHTarr2Mi2u10hjQ2exuW0Nlc3Nl5vJvpFDHG84BNdYbUbgx7FbhdCXAGBofv7GOao66J4G_6PMV1DwMAamb7LpWEqpGzJSBh1k7DG_Tx2KSRVLqpnj1QkJTQXVSP6aXp1LI9PApRgux8owSStO-8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🙂
شهروند لُنگ پوش اصفهانی امروز کف زاینده رود: بنده را به ریاست کل بانک مرکزی منصوب کنید تا مشکلات اقتصادی مملکت را در اسرع وقت حل کنم
😐
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90895" target="_blank">📅 15:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90894">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👍
از معدود خبرهای خوب ممکلت اینکه پس از ۱۱ ماه آب در سی و سه پل جاری شده و مردم اصفهان بسیار از این موضوع خوشحالن
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/90894" target="_blank">📅 14:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90892">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6039725c3.mp4?token=KQRncou7pudzOefVGTT7Hnfovt-iQrm6X4lgDTrgC4vFMFVhn4eVeQKgfVJxuLd3dGWx8lXiSe-NYD7XVwT7pvDbppBifXz9dgC2Bq_MIg-6RY75uGGhXdyhBIKXWC1gRUdU8Ps5GYS54Y6o_jI3MEWzwNlqvfUSrK_X_GNgO6gEDFvM5-eV6DWBE9zxX4FLcTVREr3cD47-df2wmsnzPWf51vvcYAj0OMREy2ONdZV9su4TL_-9GKoWX-vGIbGpCNU9QW7Mn7sdif4doiDOyRreHSVZwAv67EqQ3VaK2B4n_eAFNjV5lgX7cjsR0MorTMD_fiFnBEW1iwV3jc_VhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6039725c3.mp4?token=KQRncou7pudzOefVGTT7Hnfovt-iQrm6X4lgDTrgC4vFMFVhn4eVeQKgfVJxuLd3dGWx8lXiSe-NYD7XVwT7pvDbppBifXz9dgC2Bq_MIg-6RY75uGGhXdyhBIKXWC1gRUdU8Ps5GYS54Y6o_jI3MEWzwNlqvfUSrK_X_GNgO6gEDFvM5-eV6DWBE9zxX4FLcTVREr3cD47-df2wmsnzPWf51vvcYAj0OMREy2ONdZV9su4TL_-9GKoWX-vGIbGpCNU9QW7Mn7sdif4doiDOyRreHSVZwAv67EqQ3VaK2B4n_eAFNjV5lgX7cjsR0MorTMD_fiFnBEW1iwV3jc_VhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چالش بامزه بادیگارد مسی و روبرتو کارلوس
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/90892" target="_blank">📅 14:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90891">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VuPQjtIsORYffOqFAHqYsQv8S8rf2YPPP6toAIswEwAYwxKRnxFBNOjuRPg55F-csAaf34mxsZlNmXe4QnunY0v99B8ZHmguLUrM4TSghqNAW0NoHpBbDhqWZfSsFpRbp5scw680mAGfRtfE121zF6wzOe0up1KGa1E7PF0QxHTnYa1PXHTbDjJ3jNO22ktbGH_4qRvul1S917ZDndMumix0-Q8y5RCxp1t_vENi3AnDSjiMb7mKkotYLh0zASZ1Kt_je17u0vrK1PmEgIEIoOo3suR4R45g50RlCTa5rgUQ5aNfHw5NSwcksKIDMIXej8qoQBC6Sytkk6mMppaMRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب در حالی ما با مالی بازی میکنیم دم گوشمون عراق با اسپانیا بازی دوستانه داره!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/90891" target="_blank">📅 14:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90890">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔥
🏆
فرآیند جالب ساخت کاپ‌قهرمانی جام‌جهانی در نسخه‌های کوچیکترش؛ خیلی دیدنیه از دست ندید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/90890" target="_blank">📅 14:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90889">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c49acd8fa4.mp4?token=MCB2NHjqCi3Hmhkvj5VFNBspjKVweCkjuVgbfKuvNkgFx7uiIJe3-xLwA-uZMe37OnAmGW1195VIVvHNep0w7IwsUTTWWDq9IJga7ffCO1otrWKQtfnnhCJRIs43H_K21w_BDzvEguHHw0rexZGk85g6YbsVTDBqDQfpKyV-PBn9Rpxic__O0cUhFts8OxJeZrcfpXBE3WSVOOGK51LYS2x6CD618t8w8ZZThcFslFtzXFr9a_-su7oPqtgP7Xl-yt-0oM_8_t8C-sezqQ0i4UXtEi0wRCmN8AFPNPd0AcJaNhg34To7cWcA70Gx0uCuQy29Kll15i8-nq5eE9FdsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c49acd8fa4.mp4?token=MCB2NHjqCi3Hmhkvj5VFNBspjKVweCkjuVgbfKuvNkgFx7uiIJe3-xLwA-uZMe37OnAmGW1195VIVvHNep0w7IwsUTTWWDq9IJga7ffCO1otrWKQtfnnhCJRIs43H_K21w_BDzvEguHHw0rexZGk85g6YbsVTDBqDQfpKyV-PBn9Rpxic__O0cUhFts8OxJeZrcfpXBE3WSVOOGK51LYS2x6CD618t8w8ZZThcFslFtzXFr9a_-su7oPqtgP7Xl-yt-0oM_8_t8C-sezqQ0i4UXtEi0wRCmN8AFPNPd0AcJaNhg34To7cWcA70Gx0uCuQy29Kll15i8-nq5eE9FdsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
چالش جدید هوادار رئال‌ با موزیک ترند شده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/90889" target="_blank">📅 13:44 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90888">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C31pbG1yvUtARG6ADVJ23Fr6G5IWEMPrvmzS_dgNaNZM-fk4rpxPMmivhcMrYs2_1ItNsH_uFJLzUanaDb_Vzo_Dfa8rOy9tOeGz-TvXXI8_R8YAiIpeXe1AgCypypw72ZihIvA0Wo6XqZutywuqsnyM_Z1qlSSv7DamfGCbqUp8_WLYAYKUuiAHHl_z-HcGJ2UeOdJYVA_3pE51OEg75UQuKzKKz9vNH2PlTkvZAK13YIlodX1Xary1Qt-TbbGPvU23APJUACfYxrTY4zSTMnb5sQ_ZJsw09sK8DCk1SBfa2S-MsOnF55kIYxJKStvG6EI2GtP8MOjsUX7havEwtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
📰
#فووووووری
از اسکای اسپورت:
🇪🇸
بارسلونا نخستین تماس‌های خود را برای جذب آندره‌آ کامبیاسو آغاز کرده است.  این مدافع چپ ایتالیایی در فهرست گزینه‌های باشگاه قرار دارد و مذاکرات اولیه برای بررسی شرایط این انتقال انجام شده است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90888" target="_blank">📅 13:39 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90887">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#فوووووووری
؛ با اعلام نیکولا شیرا خبرنگار سرشناس ایتالیایی، قرارداد ژائو کانسلو با بارسا دائمی و تا 2028 تمدید شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/90887" target="_blank">📅 13:21 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90886">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PvCJQV0Eu5jhrTINrGJ8jR6oYulJ1W5hLSUgZA8Uo8szKt1N7l8AAIrn0AJA6XffMZTWIYhdpAP4nnuXv2lzADbBeyfDWsOIllcOPwtxhqYqZg7eXxh_kEzsBY1UiLDJtqVhFewICysGTm0fMSQ2YX8hOI1PCiXGV_AcpQjGQwowF34iNuzDstuFcaki8tzYODAEuBldQddvBbMybbS0eCSu2V2DJQNB4iiyomx9as-fABy57LpXn_8IBqK9UttIMmNwPgmJoIcQSIr5IXg0N3hj6s56ZluuejdgsZZaFT43i1AInK2s5R-1rGcGZZJs26kf4qETjYUzof33LCm_Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
جوانترین مربیان فعلی جام‌جهانی، نکته پشم‌ریزون اینکه سن نویر از ناگلزمن بیشتره :|
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/90886" target="_blank">📅 13:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90885">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🚨
اسپاتیفای رفع فیلتر شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/90885" target="_blank">📅 13:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90884">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aOTn2tQg_whUJcSHLgjKZ0gloB5FRTWTwCgKXlihuJ4YRe-nFM-oK0z34nWZUGWEo6rQSHxMoR3KG1Zby_lteo12-1SwWoEuHsOJDmR5Fk5W7S6z0A9TxINi6NvO37IAcPDIkyCjWT_xSHdl_OQBVKoCgTEpjMIuWqvvSAJmHkDqwQtSZ5pyesB46VDXjkYENSDtLW6lnU63fnoG0-kYBaCfvBQrjYsGR8LWOF3EFCYO0EMio1e0DwYF8Zqsa8BwX5NCp9IawMun3rUz30aPCkbcWQCvEYvwmNGDhrRhzodEzG5T0h8Q7M-p-YaDNo6XW07RJLpjaELvyQqO_QHCgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات
|تاتنهام بدنبال جذب ساوینیو بازیکن منچسترسیتی رفته. گفته شده اولین پیشنهاد تاتنهام رقمی نزدیک به ۴۰ میلیون یورو هست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/90884" target="_blank">📅 13:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90883">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b04e0d6510.mp4?token=KKP9SJILye4g6LGhuS4ppCLSM2xWte5CjGN_sx9mqSkjNb1tfI1vYh229SauyZpiDUhdSVIKZO5Ifx24c2RPWdkMJ86_Dsfup8nQpPJF3whLJy96omjZr7eXSalTXkJvE_v43uO_tkc7hcpRGGdtsmy7S1W7pPoqnPgZFot9kMNG8dvEc9-g4FKZkfqshD9zpso6ShnayJtrzNWaDejCELbmVeyd3_1G2G9GC2iCmAzR1FPUUGpwaP9kQwfPb6mtDKXgYGo8EtCJSLwxjtSCvjTG7N9rPQIRVGqzi9j1ZCyWjNjE4UUQcY-9zVzwvmSOb3iF68NGXdtdS4CrIKwL3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b04e0d6510.mp4?token=KKP9SJILye4g6LGhuS4ppCLSM2xWte5CjGN_sx9mqSkjNb1tfI1vYh229SauyZpiDUhdSVIKZO5Ifx24c2RPWdkMJ86_Dsfup8nQpPJF3whLJy96omjZr7eXSalTXkJvE_v43uO_tkc7hcpRGGdtsmy7S1W7pPoqnPgZFot9kMNG8dvEc9-g4FKZkfqshD9zpso6ShnayJtrzNWaDejCELbmVeyd3_1G2G9GC2iCmAzR1FPUUGpwaP9kQwfPb6mtDKXgYGo8EtCJSLwxjtSCvjTG7N9rPQIRVGqzi9j1ZCyWjNjE4UUQcY-9zVzwvmSOb3iF68NGXdtdS4CrIKwL3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
چیچاریتو مکزیکی تولدش رو اینجوری به سبک چالش ترند شده فضای مجازی جشن گرفت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/90883" target="_blank">📅 13:01 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90882">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6tl-Jp4OvMFvZ7fAQztMCY8UVuoSUPfgtg-eRIApQ-xBvfzA8zQbtTvQNlM6720vfVAh33k3Yi5tfHcjM9GPoEzydlr1Nn3ZtKxajp6VIYNYzNBW4F4vDXDUBDzKZFA7uBIC3FD7Q19iRGuF-hLvoUA-yFTO2i3eXasNxX4npMICqLG5tg8fZ0S32nowQ12GY9kA8WcgF77NF-Og59fPPD5HPYo1AeHvwmZL_ICObaZeRy1D4_Ef5yQi_BXFmTGulHXky5EoRvtgnAD18-2nrsucOLrX66hIt7cg85nNrrxwIfZVXFM4o_jsFVxAPlOgJRPp7uLxwdsPC_fuCn-Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رتبه اسپانیا تو ادوار مختلف جام جهانی‌
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/90882" target="_blank">📅 12:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90881">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/017a14deff.mp4?token=YJMQQSW4jvxVSk9p_z15-uyFk36kZcoR9JZsayRNhv7p377M9BVNyjsn6aGAhYcAWDm-031P3X_c9rnGImqFpgf8U2saLrfD1-gO_-05t7CubdSVPl52Rs1yE1pVlKxlgHAJVAumTIaVZ9s3lSUzo8La20rS2AqEIP_6-4QoJY-zSc_zrCgOXz3PWPp7RcadHCL3OS0n2i0NgKCQe4eIiL1dhcLm5YXjC0WD9mlNK9z_tbFmzXpMX1sx_fpzMCZfC7OhuBwfhS-QtN5ihq1XAcWVM2Oa4vD52VwoGBBfmkbbft8lUP_S5Cc9m_AkYtvjwsvmj_TkHkeAdmAv715t4iZDprrBdl_28q5Dp3W62Fq-YfKG26ZlEq4OgbI3LjzXq8JzfmoKZVq8_n0j4poAkgpDjYDl7xF8-no0uW2QXBwHyPZOfexENIXXzv0RJknK2LDI-L7xpHVYPHFDa2IB269UHIyZhNSWSclRTfAlk29_pqC5CJzU4mP2DrLW9_8NL55MEaXXX3Jit20JG2_7dbYASBcH86VY1IuSC3u8fvegmfhwve8BqN4T2zUGaDH8LbfMrD1xpax4Aabjasge8fqw6yjTvsqOWfQJmIT_HUidBp-VqM5kKMfUAa5EyWcK64YmLurSohriEoKjamNAg0tMppwOcDWhtTbLTVyq_JM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/017a14deff.mp4?token=YJMQQSW4jvxVSk9p_z15-uyFk36kZcoR9JZsayRNhv7p377M9BVNyjsn6aGAhYcAWDm-031P3X_c9rnGImqFpgf8U2saLrfD1-gO_-05t7CubdSVPl52Rs1yE1pVlKxlgHAJVAumTIaVZ9s3lSUzo8La20rS2AqEIP_6-4QoJY-zSc_zrCgOXz3PWPp7RcadHCL3OS0n2i0NgKCQe4eIiL1dhcLm5YXjC0WD9mlNK9z_tbFmzXpMX1sx_fpzMCZfC7OhuBwfhS-QtN5ihq1XAcWVM2Oa4vD52VwoGBBfmkbbft8lUP_S5Cc9m_AkYtvjwsvmj_TkHkeAdmAv715t4iZDprrBdl_28q5Dp3W62Fq-YfKG26ZlEq4OgbI3LjzXq8JzfmoKZVq8_n0j4poAkgpDjYDl7xF8-no0uW2QXBwHyPZOfexENIXXzv0RJknK2LDI-L7xpHVYPHFDa2IB269UHIyZhNSWSclRTfAlk29_pqC5CJzU4mP2DrLW9_8NL55MEaXXX3Jit20JG2_7dbYASBcH86VY1IuSC3u8fvegmfhwve8BqN4T2zUGaDH8LbfMrD1xpax4Aabjasge8fqw6yjTvsqOWfQJmIT_HUidBp-VqM5kKMfUAa5EyWcK64YmLurSohriEoKjamNAg0tMppwOcDWhtTbLTVyq_JM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
بی‌بی سریال متهم گریخت پس از ۲۱ سال
🥲
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/90881" target="_blank">📅 12:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90880">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/225f01016d.mp4?token=VUm-SgxMCTK7D5FJE4wvKL6Wvh-Kn6tcAjB3Und4kRcXJMpzWc5JvNFmy4boW3iUsUqc86GgPoztoNPI96FcmZJfDouLkCxuU_tENci9WRPGTjEe_bkJeAdAKQGbZjaZjcH_07xxYNTglz3aZaoa5hdReuqpIfoxVW2UcVlhYq4Kb5z8jncjDOiq0r_9knXQaZR4aASsXfAy9sq_wlf7RGrfMBrlh8eewNUktEXuxjKkNHtBA23cEFCshcRQx_hmdC3iybr89pMQb3lY5aghkA615P5MrpjF_NQLppHd0OmrqwhZ7Zurr4DynERCiEGL6IxCTAbQ5sVpHTtEnRH8zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/225f01016d.mp4?token=VUm-SgxMCTK7D5FJE4wvKL6Wvh-Kn6tcAjB3Und4kRcXJMpzWc5JvNFmy4boW3iUsUqc86GgPoztoNPI96FcmZJfDouLkCxuU_tENci9WRPGTjEe_bkJeAdAKQGbZjaZjcH_07xxYNTglz3aZaoa5hdReuqpIfoxVW2UcVlhYq4Kb5z8jncjDOiq0r_9knXQaZR4aASsXfAy9sq_wlf7RGrfMBrlh8eewNUktEXuxjKkNHtBA23cEFCshcRQx_hmdC3iybr89pMQb3lY5aghkA615P5MrpjF_NQLppHd0OmrqwhZ7Zurr4DynERCiEGL6IxCTAbQ5sVpHTtEnRH8zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دهن سرویسا چی میسازن
😂
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/90880" target="_blank">📅 12:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90879">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d81d6976b.mp4?token=bkCIwODZA8xSxDI9rATreXZMNKVVVlT8RLCVG2qtw-JVdfDR_c7Fv3Zg9Y2JDpJeAUgmo0k5ajcrf5wJNYkdJagoV7N2SPSBxc4GSZ1UM_Itss4a7KAwpFs1eFYNPnnalz2E6qNvtdrsmHw6Env3KTaKQVNDolF8RTFZXKQHj5Z-soviSXm0nD4F-FjT0C-hOa1Xzd_FEeDCbGUaw3LThp1IqUTqEn5Yl2_BrxS7F7ntZpWLUqyjz29RZF2O2m-gLek8x9S14nnn8Ysf7g-7o7MWix_Yg2d5QOhO7QBANk_7FLtYkk55Hhu5UrFzPfpYKTybv2X0KbBo7mdtaxWgVpZt3KiwxjGNDH4390jAjVrwRtqdmTl5-G6533Ps_z11xkAaDBE-1uODF5sJtt-cG356QhRpNX1i6AXB-3UKt9hSbU6c7Kp46XpsiULrMMTbsFHZ9I5aZg6pFfblXaPWVYsYO1wPuH1QxWhgdsdnz2ECKyjHGG2W01SJX2_L5oR8o0DhUnu_0wuVmFdzSCmaO82mf3N0t0aoJlv5QmOZin-XsjLDRYgI5BmIIMQhno-So4-jxbmaDVAQgNWLqtFWCfgJ3pfuZl-AOjX6CBxjzlmXw4HqCdN0BUfTQHSnszUCm2O2LsHGCSDUgbRJTlB2kSWwJxuA9p7_8B62rvTGMS8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d81d6976b.mp4?token=bkCIwODZA8xSxDI9rATreXZMNKVVVlT8RLCVG2qtw-JVdfDR_c7Fv3Zg9Y2JDpJeAUgmo0k5ajcrf5wJNYkdJagoV7N2SPSBxc4GSZ1UM_Itss4a7KAwpFs1eFYNPnnalz2E6qNvtdrsmHw6Env3KTaKQVNDolF8RTFZXKQHj5Z-soviSXm0nD4F-FjT0C-hOa1Xzd_FEeDCbGUaw3LThp1IqUTqEn5Yl2_BrxS7F7ntZpWLUqyjz29RZF2O2m-gLek8x9S14nnn8Ysf7g-7o7MWix_Yg2d5QOhO7QBANk_7FLtYkk55Hhu5UrFzPfpYKTybv2X0KbBo7mdtaxWgVpZt3KiwxjGNDH4390jAjVrwRtqdmTl5-G6533Ps_z11xkAaDBE-1uODF5sJtt-cG356QhRpNX1i6AXB-3UKt9hSbU6c7Kp46XpsiULrMMTbsFHZ9I5aZg6pFfblXaPWVYsYO1wPuH1QxWhgdsdnz2ECKyjHGG2W01SJX2_L5oR8o0DhUnu_0wuVmFdzSCmaO82mf3N0t0aoJlv5QmOZin-XsjLDRYgI5BmIIMQhno-So4-jxbmaDVAQgNWLqtFWCfgJ3pfuZl-AOjX6CBxjzlmXw4HqCdN0BUfTQHSnszUCm2O2LsHGCSDUgbRJTlB2kSWwJxuA9p7_8B62rvTGMS8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای دوستان گشادی که به هر دلیلی باشگاه نمیرن و ورزش و سیکس‌پک در خونه میخوان
👆🏻
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/90879" target="_blank">📅 11:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90878">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ARoW9lAPbEdwnj79tDLFsouuX8u3t7Gyw5Wp2wJvv4H4bTiWEPCiRs09acXUnRDqVE-FPtP3fxXjvYJT4Kevdeo49arcBT0x0CTM0dxxpbPm3SSsiGSOLoLVFIMWt6i3cLQNkzvdyX62Tm_3usH3lmEb08ESgR_CBxokX3xml_I5-VwPuFgQ5i6qd9q_GegBf15FVOWC5Pg_KZu_ecLhqYxqGv80ESFl6_7Gjn55boqQUiylbW-V1PtKhrEVsQDzfS-VcnmLfY8lyAfSRvvnqXucfWMAiGS5IsRXEdn7dXYJXAMiKTDcIa_OOedo6XxRav5iQYkChVwWboc2Y6HqgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اتلتیک : اگه تو جام جهانی در فاصله 13 کیلومتری ورزشگاه رعد و برقی ثبت بشه بازی به مدت 30 دقیقه متوقف میشه اگه تو این 30 دقیقه رعد و برق جدیدی ثبت نشه بازی دوباره به جریان می افته
در صورت ثبت رعد و برق جدید شمارش 30 دقیقه از اول انجام میشه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/90878" target="_blank">📅 11:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90877">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da40b1eeeb.mp4?token=v0Q5LKcNJ4vI-9z1uVEhghU7Skh4BhH5MeEomy9J3ihqjnJwkDjsjJ0OSvDPGYhcdboVV8uLLCVtlsC9XdI1MTyMEirqchg0bdjVjpnPI2hHeliiMaXWBcbHvqygd8xVD-IcGGP0Kbo1-68KN8yPhsIMokevm7g0pNHfkBbkDypLL2UrjkLZeiOVtCzKQY4xG5PxZ6Zl8BWhkps2AQxSDCGkHxWIo7wY7TkTyK0EgtKX6TyFiXpZEisfHBd50dUC5hyao7dF1rJA-ZXnzE1R3HdLxIDKgZQtNaxo3NDgsxPXy11KVKVZ-9IL8W7pPvXjB0Vhuzf7GsakVhwigGjKMYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da40b1eeeb.mp4?token=v0Q5LKcNJ4vI-9z1uVEhghU7Skh4BhH5MeEomy9J3ihqjnJwkDjsjJ0OSvDPGYhcdboVV8uLLCVtlsC9XdI1MTyMEirqchg0bdjVjpnPI2hHeliiMaXWBcbHvqygd8xVD-IcGGP0Kbo1-68KN8yPhsIMokevm7g0pNHfkBbkDypLL2UrjkLZeiOVtCzKQY4xG5PxZ6Zl8BWhkps2AQxSDCGkHxWIo7wY7TkTyK0EgtKX6TyFiXpZEisfHBd50dUC5hyao7dF1rJA-ZXnzE1R3HdLxIDKgZQtNaxo3NDgsxPXy11KVKVZ-9IL8W7pPvXjB0Vhuzf7GsakVhwigGjKMYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پشمامممممممممممممم؛ اشتراک تصاویر جوانانی که در کالیفرنیا زانو می‌زنند و ۱۰ تا ۲۰ دلار برای نوشیدن جرعه‌ای آب‌میوه از انگشتان یا پاشنه پای دختران جوان می‌پردازند، در فضای مجازی سر و صدای زیادی به پا کرده است.
😂
😂
😂
😐
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/90877" target="_blank">📅 11:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90876">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
برای توضیحات بیشتر: قرارداد هالند با منچسترسیتی تا سال ۲۰۳۴ معتبره و بند فسخ ۱ میلیارد یورویی داره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/90876" target="_blank">📅 11:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90875">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ax9vu1EzfENjOMmRPaK95EJLr7r_2Fpo2H5p4uOY0veZW0A9UmvYzozP3ILm5FocbwWn1AzbJM1OZ2qUm_XvMFjvfz9HRgrtOFtOe7GuPZ2pXa1k6-E38WMTLfmP8aX4gL1-Ve-2BsoKcR78BEykD7w16adzkpzPjc1S3NZfsMG2DwQ5uW3YV-NlapdjKK9Mhf71c1Vg7UIaQabwrSV5io89aFmaEREegHUMemNuqIVHC3SjVJaVAAuoJ9Sl53Rtb-4vj5I-w9DO48EL5s-2T9oBIWTXcBMpxI7qbsg8lpPsqjgc6KzzcVLviovuKgk82Qx0XTC0WWDWWA8M1b_8wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فووووووووری
؛ رئال‌مادرید درحال آماده‌سازی اولین پیشنهاد خود برای جذب ژائو نوس به مبلغ ۱۵۰ میلیون یورو است. پاری‌سن‌ژرمن برای فروش این بازیکن شرایط سختی تعیین کرده و به راحتی قصد فروش این بازیکن رو نداره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/90875" target="_blank">📅 11:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90874">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dad07bd808.mp4?token=SjZwS0w0pLBh_cY5pZ0YtIfUftoH7ddb560LJ6imWWU1n8u454j7ngRI47WAqV1gqi14XpB5YrLHmdNgy8NssXLD5BUUjcP0LhbKqmVbjmtrEZxvy1akGlvTfpQ4Pu_AJgLMd-j7-C08v1fugB7UvQhyMzRKVeGzqZAZvkfB4scS0neSVQpxFteitRo1OjrqKm9U8BqXJVAs8pUcirdGf1GKUTfE4KIqLWa1dN1Y9HJcAm95o4RYjLcRAu4RKrMF2vKOL-vTc57IsJf5Cxzb2kfiMJ9Rcv6yYdNt_Fg-rewUGgZzKy-SiBgjCuHYsU2iT-TO5s0aqeW9oiW8ElOCgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dad07bd808.mp4?token=SjZwS0w0pLBh_cY5pZ0YtIfUftoH7ddb560LJ6imWWU1n8u454j7ngRI47WAqV1gqi14XpB5YrLHmdNgy8NssXLD5BUUjcP0LhbKqmVbjmtrEZxvy1akGlvTfpQ4Pu_AJgLMd-j7-C08v1fugB7UvQhyMzRKVeGzqZAZvkfB4scS0neSVQpxFteitRo1OjrqKm9U8BqXJVAs8pUcirdGf1GKUTfE4KIqLWa1dN1Y9HJcAm95o4RYjLcRAu4RKrMF2vKOL-vTc57IsJf5Cxzb2kfiMJ9Rcv6yYdNt_Fg-rewUGgZzKy-SiBgjCuHYsU2iT-TO5s0aqeW9oiW8ElOCgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🐸
مازیار لرستانی: از اینکه پسر شدم خیلی خوشحالم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/90874" target="_blank">📅 11:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90873">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XM7WIMrlwvVNx8CtILQZHJ9iidvJx1hDXP_8UBDUenXkyiL39TPGJM2OIsV7v7zDsxRbbVCqNs3nd-Sq_Mqsn4UocKIsAGRw_BOlnm5vM1uvr3IRa6UNlWU9K97Ee98CCVoBl4YZGdkjGQ4tILnCPqGqYIjC4h6qK4zFG6Ee73vczYcnKYxYx_oVBY7ck4EV8aCQJaTPRjybxSsKNO_5i-5-nYMtnw5Ml8x_of0ld5p2G_SQzmUp-0TXaOEr6Jg55wxYPJL_ZcQsF72G2jvFgmaFyfemTlu0FNpM9DRElOZWneYCjWOjzRREOmwwR8igKmbGiFuRM4pWM3w8CF5QIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنا د آرماس با کیت رئال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/90873" target="_blank">📅 10:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90872">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KIM0pf1hyUJTSb_MtJCrg3P5YaqX2q3hknTYHOUNmtA_nTshm4vnOl50QbdUH8rxw8cp_wzXyCcYFzY5-T7uUpw4GbDL6XFXXvs1VEG5TSekIHAsel1k9AfptGsmZsyLL-lrsP8KOBzz3c-edzoBmcabMP7Q6dtoc-BAjnyH1QCmHuwE6kjuJSgKmVRE0dIogW1YBpQvoB0wE4bohQtrvVahVjjZ3629fhPcFH2smbGZlzlAboO3y920rwVT4tif33xRBejdEGgLUj7Mx3qIOAq0wTL7-SXJWOB0RRa68fr0yfPDxOY9lrZ3aXVWVJypvkH0Qt4FXeRZ8ybeXHcrAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
بی‌ارزش‌ترین تیم‌های جام‌جهانی؛ تیم قلعه‌نویی در رده ۴۴‌ام قراره داره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/90872" target="_blank">📅 10:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90871">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gNnr6hb1DNHfVp9DEGkZZgKu4V_4RGPixQlyrOhblGvbvLfwMJ8HY12TDjGMVqT3gQw4HYpL0FqwPGdnLQBWIO5CgSdAopgD375QLfWQiLOyozWKjEVT7USMBifmui4Cq8Clm2ewvoK0PFffwFRdoNmi5aXwrRHDsex9hdMsyUiQXP4AwM51GVAAW_kEonMzs9S71OIvr4NqOvYyHOLNmI8LNdZIq3nBv_-ZHBkaNgZEdxY1dVIbvZ3qnB0L9ie6Z_iqZ84PRit0chvE0NhJlgwGgxgCUVCPr6oXcqv7Vl5oTAv4g9W4OhFeE8AU5T-NjEn-WBI6ZXs1TmnntGmpCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇲🇽
رائول آلونسو خیمنز، که قرار است شماره ۹ اصلی مکزیک در جام جهانی ۲۰۲۶ باشد، تنها ۱۱۶ دقیقه در جام‌های جهانی بازی کرده است. او هرگز در یک بازی به عنوان بازیکن اصلی حضور نداشته است. اگر بازی مقابل آفریقای جنوبی را کامل کند، زمان بازی‌اش در سه جام جهانی قبلی برابر خواهد شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/90871" target="_blank">📅 10:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90870">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qn449nsOAIevUxFpsNgKHoOkVTi55c7U7qT0dm_DATr4YMzxjZWTP44nn5OIoATLjqNR-d3_N5CWzmDsE8V5CtQRewV18BN16_Zvb_0Yc552xG4L2bwpqloKd0kdeDuKjym2MD-fY4LbgAVOXI2iZHvvMOS0Hvt1389pMdvjlbSZk8WxoefT-K6982xs2LABeZGmMyn4Kr7mHPUidLj3ZtmeZ5WQncMF5f0p4v6THFeMyu5FDwVNar45NAfZpigT_y6NFYV3lOwGx09zl3hJk22I7TwqiRHFQMe3Le9oni4YLBOTiOKWF0amz5U8JY5D5qtmnGADyKRFNBSIHXormg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عملکرد ریدمان کی‌روش با غنا در آستانه WC
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/90870" target="_blank">📅 10:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90869">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdfbdee815.mp4?token=K0NixDO-XLjbF53Y6aDg8rCW54f0E1Lnwg6PF8GM1H1IfXsC7ryw-_DblvCCJExcaJEiVppkzPgCYkNqKK8j5H6fPPQIbvcsgsvbHrvGvc7kP7THpQmO6sohLU9Qs5QkXQsRdHAlAZ3O-xdIrEd5wIK51gVsizIOcKWjEldNvve1bMzXUYV5zvEj7_UtY8uSHQ9vCuPgz7jG6gfl1oKtdhVIhH4f0Rz6RREgvFmAhqdI2N6CJoYpNc5OR-IMAnf6BKOpSiGoCAHAn11eiPWlEf0PXlvZIbptMO6ajLKBJvTog7yRTrTIC1qzMlzMzKldnE1vHe0godCEY93MD0BbwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdfbdee815.mp4?token=K0NixDO-XLjbF53Y6aDg8rCW54f0E1Lnwg6PF8GM1H1IfXsC7ryw-_DblvCCJExcaJEiVppkzPgCYkNqKK8j5H6fPPQIbvcsgsvbHrvGvc7kP7THpQmO6sohLU9Qs5QkXQsRdHAlAZ3O-xdIrEd5wIK51gVsizIOcKWjEldNvve1bMzXUYV5zvEj7_UtY8uSHQ9vCuPgz7jG6gfl1oKtdhVIhH4f0Rz6RREgvFmAhqdI2N6CJoYpNc5OR-IMAnf6BKOpSiGoCAHAn11eiPWlEf0PXlvZIbptMO6ajLKBJvTog7yRTrTIC1qzMlzMzKldnE1vHe0godCEY93MD0BbwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🏆
چالش بلاگر آرژانتینی با موزیک جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/90869" target="_blank">📅 09:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90868">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇧🇷
مردم ریودوژانیرو این‌شکلی در آستانه جام‌جهانی؛ خداوکیلی خونه‌هارو میبینم حس خفگی میگیرم
🚬
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/90868" target="_blank">📅 09:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90867">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ce3254dd5.mp4?token=XesQUPQYqmX53tsvsE0QLDt3hctf_7PdRY4m4KyoP1RChC2KDNmUMIVjigiqo4JYF5lGup_-1t0eaf5B3Lx26xVu15xvq_QKJwRjrZf64COV1eO_3IbaJFzz21ksTbwbu5t47TYY_e4zCYlbfknC-9Rm3ffu8uKh_qLTG_wUfiVktIMg9spPEVfxf50rqoRw6Ilq2JFYdIGpK0qEZ7X-hx_BgSDIuj55d5-hC9QWw5VvNqwW15uX2vi_MZYPyMcVWJlTJDiDkvYw9NCzvcDWqNoOByoBN2tXUG24FYKik-p7nszVh_eQVmWpl-PUJ26Tk78H7cAKnUuv--Jh1Mb02g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ce3254dd5.mp4?token=XesQUPQYqmX53tsvsE0QLDt3hctf_7PdRY4m4KyoP1RChC2KDNmUMIVjigiqo4JYF5lGup_-1t0eaf5B3Lx26xVu15xvq_QKJwRjrZf64COV1eO_3IbaJFzz21ksTbwbu5t47TYY_e4zCYlbfknC-9Rm3ffu8uKh_qLTG_wUfiVktIMg9spPEVfxf50rqoRw6Ilq2JFYdIGpK0qEZ7X-hx_BgSDIuj55d5-hC9QWw5VvNqwW15uX2vi_MZYPyMcVWJlTJDiDkvYw9NCzvcDWqNoOByoBN2tXUG24FYKik-p7nszVh_eQVmWpl-PUJ26Tk78H7cAKnUuv--Jh1Mb02g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه بلاگر کانادایی تو استادیوم داشت ویدیو می‌گرفت که اینجوری مامور امنیتی کاسه کوزشو شکوند
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/90867" target="_blank">📅 09:01 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90866">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
رونمایی‌رسمی انریکه ریکلمه از پیراهن ارلینگ هالند با شماره 9
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/90866" target="_blank">📅 02:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90865">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NDWgwGClChlBgA0P9ZutMH1qY65LXcYKGX3HCMc_nYJzjwr7UEccxtArqUU6Qv3SCHsE3wN5VNbPyr0yYXEwZkMG8MX6GGv7U6Kr_EuiHmwLrqMpiNVKVlAQUVUFR4_KSJRPXaKrRNkRhSBMaiD7y8gUeHENafVtDzXyEo0FU3ad88lnfGLiBXKHTTZVForYMU4hNF6gsUFLfHE_dcS4saCQKqrXHgmlTYPmQDkIjbFhSx_K5D-JJPdGCah6V8JPnc6wzgVW2SwKSU8L3Uuhq4M5N8crfi5o9LLLEc6aMWKQg6mOqlpzXRUhO1NR1YIP6TFeD54uw-vBD5Pry_p8iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فووووووری
؛ با اعلام رومانو، کوناته با قراردادی چهار ساله به رئال‌مادرید پیوست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/90865" target="_blank">📅 01:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90864">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
رونمایی‌رسمی انریکه ریکلمه از پیراهن ارلینگ هالند با شماره 9
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/90864" target="_blank">📅 00:49 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90863">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووری؛ ریکلمه: ارلینگ هالند با من قرارداد رسمی امضا کرده. اسنادش موجوده و نمیتونه بزنه زیرش. فصل بعدی شماره ۹ رئال‌مادرید در اختیارشه.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/90863" target="_blank">📅 00:48 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90862">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
رونمایی‌رسمی انریکه ریکلمه از پیراهن ارلینگ هالند با شماره 9
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/90862" target="_blank">📅 00:42 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90861">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FFevIhOOKEfw8fkTjke_KTXh6TE258o56Vbier-ugkU5hLmdOo2hdJXCykwmvBGzgRFX9vqTQHKoESpjEciest1YhPSYWBa6koiDub6ml8kWzrUj6NXcaZMVSNKj3oogp6k2UeDgbWKfp79DQSmV738w4MjP5R3d8GI0heQr0ATq75lL63M9IBj-lnjqgP-c4hoW0Qs5gsZq2iqW2kdwz_cisN49r4lbmsPOBh7DzxyeAl8y50ZIvkvH-2OUCCsZuAG6_0_l7Ny2LLeLfL_9_FQzwSbSe9XVGkv8W5OmF-O7MHUIOAwT6zUyx-zdYZBAJcEZWScC5ZHVAk_MESEZcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
قرارداد بزرگ پرز: کوناته.
‼️
قرارداد بزرگ ریکلمه: هالند.
⁉️
با ریکشن بگید شما: پرز
🔥
یا ریکلمه
❤️
؟
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/90861" target="_blank">📅 00:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90860">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/csHiWrdvYGmThLZDp2ZP4HlUpzDStKhK823YIoeyO5aYXqsyeuH3SunW_FYasRVTzLr1rEJdrlD30ZRv7LcwM3-8yHvsgG5JgKGR1finYnY0XF4YyMBkBF343dau6_SH2F99N44QiTY1zWoocfbS_UdK4rmnsHpu1CHSA19Vvbja09qumJ6KNstB1FOQnmVDMF9fDXkQ6AmuYLZzY0oSzPqJs3aKFfOsWLmj6dcDmlikhwFOWenKVHdKE6j9EE0PfL0UUFAUS6wWEn8doqC1WR32wr27Audh2DRRTCaa4tyi9yDYF8QUBI-fwLG_oGv5eib6zp2r-vQISqBa5XsIag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
رونمایی‌رسمی انریکه ریکلمه از پیراهن ارلینگ هالند با شماره 9
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/90860" target="_blank">📅 00:38 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90859">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">😂
خب دیگه کسشرای ریکمله ارزش پوشش دادن نداره. فقط اینکه ۴ روز دیگه انتخابات رئال برگزار میشه و احتمال ۹۹ درصد پرز با اختلاف این کودن رو شکست میده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/90859" target="_blank">📅 00:35 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90858">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRPQ73-ZbCCdzrN_s02XWyTeLa0hUMWHkO2HcODMkD5Y8avsqeG7uDBRS80-d7HVpbokuuEN-f6NgH4iY4w-O8r4hlMrkCtC6jGLvEvRBtmhUkxsI_pPgfKRKNqaHOtFJJFoWY2FCI4zX7_QQRn-qIdtiwF0oUbvjFeGkvA-nPyTeKdZ_d4Y1U1HcYyemNbpAVPaWNuzy_FkJ4DrSsMT3dp7WHuqAbGjXXIgCWFrtFmMyFnB-s8A5rqoPJyWsDAcPA5WSyDI4ZtYQmc2mCy2UqHI2zRM5MMo62UDObo2kN3SZqeCnhyuG6COzLqhs13MZHhP75yJm4etQetuwNAT-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤲
🚨
👤
استوری سردار آزمون برای مورینیو
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/90858" target="_blank">📅 00:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90857">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">😂
خب دیگه کسشرای ریکمله ارزش پوشش دادن نداره. فقط اینکه ۴ روز دیگه انتخابات رئال برگزار میشه و احتمال ۹۹ درصد پرز با اختلاف این کودن رو شکست میده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/90857" target="_blank">📅 00:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90856">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f8fa88ed9.mp4?token=J22bPypz6W6IXgDW55yV-uMaZCqrO-BCKLH2JHKXTgrb_x80q1m35RkSsV0jaJvWz7gloJYfvKGutEI0kPBFHBsUNG95RLRkD09hCixK5ZmIFpyqVUKqttcjG7XwoOdxZ85icOnD5Emyo2NbrQBnqMfMc2dLiFBjL0dDD3Yalnfe8IGtyfADWoHtR7tArt_ucca0DFXjvWCzcJGfzfqeQ5011SRCAiRK1kzGSUPHAd25uQ5mP5iyKbcgisDM_RQk4ReER3BVngYfR_Ek-Tbm5Cpq8ixpAYHBvZJZuWVNz41mbhq9KV5kVq3UWAOfSls0ImRpaMxxSX6z37tct19Ufg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f8fa88ed9.mp4?token=J22bPypz6W6IXgDW55yV-uMaZCqrO-BCKLH2JHKXTgrb_x80q1m35RkSsV0jaJvWz7gloJYfvKGutEI0kPBFHBsUNG95RLRkD09hCixK5ZmIFpyqVUKqttcjG7XwoOdxZ85icOnD5Emyo2NbrQBnqMfMc2dLiFBjL0dDD3Yalnfe8IGtyfADWoHtR7tArt_ucca0DFXjvWCzcJGfzfqeQ5011SRCAiRK1kzGSUPHAd25uQ5mP5iyKbcgisDM_RQk4ReER3BVngYfR_Ek-Tbm5Cpq8ixpAYHBvZJZuWVNz41mbhq9KV5kVq3UWAOfSls0ImRpaMxxSX6z37tct19Ufg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
خنده‌های عجیب ریکمله به انتصاب مورینیو به عنوان سرمربی جدید پروژه فلورنتینو پرز
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/90856" target="_blank">📅 00:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90855">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#فوووووووری؛ با اعلام ریکلمه، رودری ستاره سیتی در صورت برتری در انتخابات به رئال می‌پیوندد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/90855" target="_blank">📅 00:23 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90854">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FkBYaPx8Qm2ZN6t5uULVnZUTk_tPedpcpmwELDzLFOgEhacatnbZBYKBqj6mc_cIPtCnUpafpSbnUae9jY__t2DFIkAFY8Fb9UGJt6zZtBQhRPbcr8npalp4X1KH3IdzLybaXDL5IQeJP6nzMqXhfeuGEdzr9ORyAs1S7zqePDF7bAr6y0h8xYsKCJgmin5pHxvBm3VVqAZlQJfurKWx8wBV5lUXNXBeFVtktDJ7u55t9-akLSoFD_BHd-k_ScxjKYXgFqIayQa9sbAUt9EMAnD5ZzIe3uT8jzheNEN_-R633C-8itKrhQ3Nbsmtf5-Y-8tcQiGaguQYN-_Okn2-Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ته اجداد ریکلمه رو بگیری به خمینی برمیگرده
😂</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/90854" target="_blank">📅 00:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90853">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
انریکه ریکلمه: سرمربی تیم من بزرگترین و بهترین سرمربی فعلی جهانه!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/90853" target="_blank">📅 00:15 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90852">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
‼️
تیم رویاهای ریکلمه در یک‌نگاه:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/90852" target="_blank">📅 00:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90851">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBDg4AhRlTdzamavKtZhfqO7Bfl1hVcLv80paJBxZwajzOiqlhNz4-dDQZOAlH8yXXfld1h_XF1d4W0uk1uXCV9Uvrk-OHF5JhFnftBg3-5IrGPvFu_K7xrBsOZWSg-yRg-oKAaK7wKZoSnRj2Stgto9dlH0C6VMapk94uOZ0b_vVsSamYPbM1E5Osk0zlucTFWBtCuZAWt27eCrSoYERANx0HujmJcPkKxuGdejByPvRDNReUUELqgT34DmF_F4XMVEF8qvk_EguDf3fmYmIIYMvjSNJKD-axUJ7QkS8rI0H7G57HD_afmBk9LzI1Qg1GX9PRKeuizYB2bryabFAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
تیم رویاهای ریکلمه در یک‌نگاه
:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/90851" target="_blank">📅 00:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90850">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
‼️
انریکه ریکلمه کاندید ریاست رئال: در تاريخ ‌فوتبال تیمی به شرارت و کثیفی بارسلونا ندیدم!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/90850" target="_blank">📅 00:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90849">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‼️
‼️
‼️
🚨
🇪🇸
🇪🇸
انریکه ریکلمه: بارسا تیمی با ۱۲ بازیکن است. یک یار آنها همیشه داور بوده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/90849" target="_blank">📅 00:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90848">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‼️
‼️
‼️
🚨
🇪🇸
🇪🇸
انریکه ریکلمه: بارسا تیمی با ۱۲ بازیکن است. یک یار آنها همیشه داور بوده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/90848" target="_blank">📅 00:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90847">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#فوووووووری
؛ با اعلام ریکلمه، رودری ستاره سیتی در صورت برتری در انتخابات به رئال می‌پیوندد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/90847" target="_blank">📅 00:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90846">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووووری؛ انریکه ریکلمه کاندید ریاست رئال: سرمربی پروژه من شخصی بجز مورینیو است. ژوزه برای رئال‌مادرید کوچک است!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/90846" target="_blank">📅 00:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90845">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووووری
؛ انریکه ریکلمه کاندید ریاست رئال: سرمربی پروژه من شخصی بجز مورینیو است. ژوزه برای رئال‌مادرید کوچک است!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/90845" target="_blank">📅 00:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90844">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
حمایت مورینیو از پرز در انتخابات رئال‌مادرید با پوشیدن پیراهن کهکشانی‌ها
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/90844" target="_blank">📅 23:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90843">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjUbHipFMPrb5FDgsl-ptZTCP5Pp5Mb8s24Utaqti5zVweaB6AtduwqgMwq6tubLF_9NtVQOAsEHocex0JNLyd31lcDL3Dw-YsV3_3-z7cFojUOC9vhu2fMHRh5wmo23smcyIheEOivaH-06YqCfsOnqOO3pvUKpuMyyiuKJwf1zbz3i-FoB1l65Yd3Kf89JLO2shlRitysaRYYPyoc0DpnJTVweL-_pKRewsYIj8WWKLFa6FZp_f6bo_IcWxOgQwkQ6N4Rn0VTu7xJd2F7iXUJVl7f9rgByRY6LF4-dHb2q1GKTCQMzUkLsqLFCDQcyGgaxxejIAR1CF6exJ-TGKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فووووری
؛ پرز فردا از کوناته رونمایی میکنه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/90843" target="_blank">📅 23:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90842">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JHGxewESev4u86IJrjBMlEjfkNyvbxR1Goh1HqW4ZuXZQLxtIpiLjGhkcGNhtrE008c-OWahVEpp890bDVdcZhdH_fm8SIts2Aerl4cdLhz5jjytFkkXQbYb2JfKX1dgBm8uptdX75MTK63mAX1H68fm1XbUDx5gIL6Pa7D0auZ0IIW1YMKzroCbrt1gimrWkMQxs1ozS6ocjfueE_sp-4tL_CCCCVzqMWFa4NmGD_H7JPikdU7TXrfU4TxE7nsebOzpc3CFRkBhANq8vXqro8aRFil9bY_0zBkhO2fKsd-9oJ_FUeyn5SJwUUnsqDkng5qRb_uxav214jLu_exU_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حمایت مورینیو از پرز در انتخابات رئال‌مادرید با پوشیدن پیراهن کهکشانی‌ها
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/90842" target="_blank">📅 23:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90841">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GaBMPN1CHS3hgYecXeEDqx6RRho4-DW5rP9JRbC2WJL9HDS8RQ9tjF9uhZOjoSwV4d0tQ8mxiFK3Yy57in_2UPewsvTDpyy6VRXnWRsOeBWwbpFmy7H-YtrhLoNxTXHIfFkwwPC8lRUvy2fdxolReFNT7FhgdwwxDciMZ4hN5jldeRiGBZFQezK71Zna4oDTMOtGOympb-y0ZR_Zu2GSTx0ITQLMze1V0ASY2Pkpow9HBk-9b6UkWVUnBo1cjrEN2eiTcI4KWjVTEKgJOEQ55lXH2JwG01V9x8x8Q2k0FLAQ3kvozipkYYpcZpu7fgivhWfiC7NL3QWol9Ozftt4Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
14 خیابان در پاریس به افتخار بازیکنان پاریسن ژرمن تغییر نام داده شد
عثمان دمبله تبدیل به بلوار شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/90841" target="_blank">📅 23:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90834">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jX_ivi97C3Vjhg1Ruc31vSA2rqfOyIFqyFbuVk2mNK6I3tALmmlvnXAqnAFk-BwV3IxUAJaBgB4btyqOr2YSVhrAIbMN0GXDkb_uXHFi4tH9Vt5X3tlq0dOxxku2565LoUWDucwerM4zM8Y25LJa9ElDDJ152HY0EU4Hi7cWGfqBFS0okRnzax4aVNiOq77kYuOBgPH6aTpBaGc2iCtkRW5PBhObn3sVFcVhjG_IfCigx-i-fGmnqEI0QRTR6hkwZnHM_smpX8O--P8pq_QKTag-Y8KXkmtoXZVeQAVUV4Vd71r1TWZ-Bq7p7K0yXhmNawRBeX4_tRHfl2-8DlOvCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ou6y1CA2Klc8kE6uJ24bcJJi0iHVaa0eRtwmNv-PzOfpuS6-x4lvqujHNMevK3ObpwdtxZ5gs4QyjbH_9fVXzde0nHJDtgGdjE3SJP9DDVGcNBexTXeqldL79SiCF6B6M7djyoEMdgkgQLyoAElpZgWqqnTpjoZ-N3-lbqRg3DdZzdCeJXnZnNE7Qw8-PgNDQ_wWhAbQQLb2h7LHQYRRMB3UEyhEq1IU3seHRFYtH027MduMdY_jAP3M4qFxT-qIpbsn_B4DfwM-LXicHnj0-2Xc5o7vFgiqI3PPDxhKsX7AlaA670ztBRxHkkbeJI8RM7nZvnzxl4YpMTlCVa8jmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jPZpsBIzuowGuA2htthA-KXmpSn8Dd0iRwfR4fjdR4Q02gIavZ5vrpPR2_GfrLunWwdQkw6EevJ537yENJ_U8nM_09eBJnvsK3WBSUsi_7W2Mb8RJAxDljc7AEsgntc7ByHR73ibDq0PAJRZB7I22no7R0vbOZ5hQSQOhRbs_zRzErm30l3BX2w6kKwO5-M3NmWfVcbF7XGjsHAOyc9UuTNlqEB6gFvFS9HMB6G3ucwOzlXkH27YQtWS8sksvBrsNyFgEW96a83MnTa7SiutXcybi5XIqVP3hxaaGAMDHs4rAB-0INO_19s5aKH21i5Q2DOzSgubqP_DJDe4t_jdbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PCn5xtgpXR2ypbUVQ1neHMxhruLEDKUyz5S-r0r9NUIvj8boEBBwWpk4ZDUzHa_EtR-COE9IhBLkfwfLt-9QcmNZDUmQtjumubqfQcUkiZ1Y-E1wCb-IHjxFqnkwGmNk5Mg0D7VeI15ma3-1ss48y3R3NJyFOl9WnGUomaiwrfmmsHlESUYGSaTrCll9-IpwWFGdDuG2GXGI5ZLVlVvu72zfxJ8H0Yglwiy1prLZMT0IU-LXr6-ENUBqG5aHQS0jXc38CZl96aGjfRRkLCmXqLTiOGNr4ldixDlFEYrv4Sk77eJHs4dhzudG57l8EOr8BC96KTji8oBFN8N1bP-4Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oesGE-aNYOantEkxX-QhyF8151l96hoOjdI1RPzHJOv6L02nHuTokOINJHHxPhSo8onxY_nCYneVWujnZZYDXfhXXoSR8F1nOJ1Sd7P0HN-hD2rt0BdBgjRKQnYtRSbYuEULli0VYMUaPBgRJICpbfZwCBqWQWqaQUUxJk2l6rmrAGiATvkFgC2GhwLz5vnyEcjdjb07vD7PTpRQkZVjgn9bvfVPMzyCrbq1u_5fxu16ayWLbs_3sxuUYQnQsOJr93VruUPnvb97ID0wflCTLFXz1EQCGQm2Pgmjw2KDMP8TxZgkHjbJ27SoQq6L6prdvsC9UcU5nm6eld0ZZS--hw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">8 روز مونده به شروع جام جهانی ۲۰۲۶
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/90834" target="_blank">📅 22:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90833">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSGOcPmiJyYkbEGbsylmrjnXdX_OvSvV5325in-aQEV28alBkS0DBeEkLklhin8FaT0ZQ_AqKzMj7NG5bBjB9_yUgPpFmfA4V-Apb5qh30Ez40Zm4gSmRk0EVIc1Pe9K2wQpOm_iIcPIkgVdMg13XUrAxpceBN0xuuFypYklHXp_jPJA0lniH-KG04YSurh_e2dctJ9J1n73VMUlLZpsXqf6M35i3cQ5dJNSujEJP-maXrvHLGo61pZX6XwrgYUIRkZh8_1BfIuVYph8ub4wyBvlalh-VRML0MaxH-CqgyyBpA-93M4Mt-RebPqJHerVHfrAZ8cNvJX0Mi349hnrwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
شجاع خلیل‌زاده با ارزش‌ ۱۰۰ هزار دلاری، جز کم‌ارزش‌ترین بازیکنان جام جهانی لقب گرفت.
🔥
🔥
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/90833" target="_blank">📅 22:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90832">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2xEsz4ROJgKLf8D7QrgI3RQ8vhPLfD2rGPTSNVNlLc69iA9SK79j5Uc1Jn4Thv-5KH51bkPM1LstNAUMmgZUqHRKnkPfKqHU3D3_T3JaduqQb4BD1pthdJkArT9PVo1OeQcqS2BRES8GFGUxfeaWSyTCgPLCR4xc3K3dhqOZGBSt8gIcZAqRqe0PDtJId9ouO1HpYjNFGPRySOBmTF5pzpA-NDlG86hql_dRQEoodF6G0n7oywUmqZdfiPY6C2ENZSKw4GVFA2X7bgHjgvQaPqYIncmX2dcxEyZp2NWW_sRYTkHFvr3zDzWKT3y8Er0k_Py4OWT_Vat7h2HSREOvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری باشگاه استقلال برای تبریک تولد فرهاد مجیدی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/90832" target="_blank">📅 22:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90831">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v1ACz8BPBaV0JhjH-W3-U-DHKIYifbQUz70I2vqVMgsw0Yu-DqXR9LHD0YDsD4BVcfxwmu1jKBBBOQ7hiwQRUqKr4FQOZYogoOimsPKjbVXwctJs7lMMGhg0nrYkf4HoKU71tDbDheMa-PDzwp7FaFswNSALNL2TlLImD7svLIzQn9nOgi8ISzMHLQrIXCIFk6YEu1wpMhxeIDapUHF41_0QvabY-0YNN5XsEDcozZrDW8MZlmKfO0HQ6Ky3oYB3b7Kt5RMqA4MPe_9b9Uu9Nm8I7_TAAAeNor9-RLWchNUhfim8vGWdbaWdH6hM6LVFWB8TEph3zTIvESyLGw0GAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اسپانیا
🇪🇸
-
🇮🇶
عراق
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
پنجشنبه ساعت ۲۲:۳۰
🏟
ورزشگاه ریازور
🎲
با بیش از ۳۵۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
اسپانیا در
۲۸
بازی اخیر خود در لیگ شکست نخورده است.
✅
عراق در
۷
بازی اخیر خود در لیگ مساوی نکرده است.
📈
میانگین گل در
۱۰
دیدار اخیر اسپانیا
۳.۴
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر عراق
۱.۸
گل در هر بازی بوده است.
🎯
پیشنهاد پیش‌بینی: مجموع گل‌ها: بیشتر از
۲.۵
- ضریب :
۱.۲۹
🧠
پس از باخت، به خودتان زمان بدهید.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90831" target="_blank">📅 22:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90830">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ix5FAU_IPmhGHVSHxoQwfBFz27EgN7n-MRZVJRvfMOw-wodHwZsS1_ODIwlqaAVEdsmXF8hjNylxJ6Zsl3TqugBtm4n0j7LJOk6zNk0-2gtmfvmXp7yr-HeIiGseswHXGsJ65gEnZMuw0OxtKlrT-A-Fi1hQaZbsQZ72PDecthp2Gjwjc0MXte0cIighJY7mzeIB7Mhf01Lj--fiNORqJ4uJFi0O3FhyezT9HuwelhNpkSCdy-ocxvvOKbEWVUSAMi-Hz1q_YNXoRHa2nXbA7TpyugWh-AO3eq4LAFEnmiwIfgE9nzhts5uqzbiVpUm14RE4yz5oolFHI3Dd8WfDMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">TOO FUN🫪
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/90830" target="_blank">📅 21:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90829">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o2tv1VAHacX5vqCE03f2MZjADtBbBjKYGPuz5401KuWgdEFU9PHdY-PEfy-7IdjjwmFjvSOGRQPSOJ-VYe9hLx8DqECLyZ9aGgwwm4aLTGqIRrcrqn0oyJMy_Y-ukNzPos9VSqAbrgAIlcKTm31c-RceZhZR2-CpdwAXr0p7xwoHw5HS8_Jh01N9C5TEaLHsRzM8mvafA4yS0M2yLY1TcW6RoOBXJ1tC7yZbgCp80nzGxnqOFJwb5Q28KX-D9W2_JXhqS1pecmoeL-BiVrG6F2wrrVh11-wrTvennIWBI_wmkZheERNLobRSqjdH-jzYb22AvXXW-dLpRHsqPapq1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رومانو: برناردو سیلوا تصمیم‌گیری درباره آینده‌اش را به بعد از جام جهانی موکول کرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/90829" target="_blank">📅 21:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90826">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nwxUFnYeStkYJ3qKaAH-TT_KCBj9dLjX-pPYIjMH0ZJZzifBheljJhgCZnrzBepWDL1ndr6mjpDrFK7Q3a1H4bLgOFG3VoPCyTWmvGolFZfiKKPTdEjb9sY9d2SJggdQud_rqRCQh0uzUg24ZmhVxK8IQApDCHRrRvR-xIWaAZ4eL9HS2BVzxLds74SK3GsrJmM3cEooQfsDEPJqf3qo3HlPHHTmzkokGKa4SsAaZFjLsg1gMLvMv36tO75u6sTY-xBwNpQa_5elKcl4i-pDH5khJJuhJnHN-bZhOJbeIvM1RK93cL-FTVULEdzsK5VrUtCnVouLTSrXoSlwD7sCWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ACXRhqT5uf_xu0GUNK7NjXwjmrlJYzZOw4mp2xHAdDD1OTKILv5Juc9VMRntrGmvEDGHyQMfila5BBstRjKQQQAKqhnypZT0GY9QgtYdK7J29P4OBb00sThi30PRuuLRZnzJt2NgmpyUQDbUamJMJ1x9UCvIyuSlM6usn6m0N9mFWHlV8CdM-5QIpYxo13UVGrJ5Dy46863o9BzbAGd4BYQZY7YmcwdWcWJEkIuocxwgj0r4xZtOKS3yKBbTirEUjyd0OgMJ3c2aHPWxM2OKfUlVFnLzadIE9_4Raa9dSQuhJW0A2S9QOjDwOLT2NDuiv8zoqes5o6L31S9qQlwGzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rOi_rvgsDDEtLeZv8A8NIp029MoxirOdSr7DBwBylqr20A6YJ2dVaC6Rr56pl59My_Ek1nUkUSa5OIY7v2i3lN5lFuxcF2_7euighHTR7GLH4HwombGF88KqHkPUB0rHh5DMJb3iEBchguGkcHZEbAv2VXGqYaTPs19GKK6yne1zs8Bxg4E_eqar7NrHb0A8uf554AEGu5WNdSfoxs9FQxPTeK6k_Lk9EPpUH0EfTi9qKBaoATrp-qIS9eOzIj968HY_jWanxZmPzUvYsIcvVR3oQIASH-O8XgqOIlxTzyuBkTp4ZV1u_hmG4KwE56Zkl2nZvLvlXWRMRHZxG0PN1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عشق و حال امباپه و بانو
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/90826" target="_blank">📅 21:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90825">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
موناکو در آستانه خرید کاسادو از بارسلونا است، به محض قطعی شدن برناردو سیلوا هم به بارسلونا میپیونده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/90825" target="_blank">📅 20:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90824">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uKw7kQ13yMgi_KUXROgqU7-5KC-ik0vIH1m9hWj8kPHr6m8jwDNAabj-1e10q9kEO8jJ874bonkeEmfpfQMJdqsSb1NBzycOtWcEziWExCt0NAwAjHfalpG6skXiA6cqHYW9_WZASny5QEycGahCt09wR1BYz9Let89VsRrydMid_gQC4zahl2iSLWagD1-BUlD0tcC1-YxuEkMs3opquIPNJrxZELwXzIL7RqMCWRb-zHIpoRn3zTbUOq0bwDEgJGXdMOkTGlYa4x3OjpjElq8OmndkXTedO37bVd7WP8Ib2bczLYyBRPiP3a0zPJKZAL1f3K7pM_ivyE8Qndb_zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فووووووری
؛ در صورت منتفی شدن جذب گواردیول، رئال‌مادرید با درخواست مورینیو بدنبال جذب کالافیوری ستاره آرسنال است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/90824" target="_blank">📅 20:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90823">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b12cb328d9.mp4?token=XknV9kppFKDtZq2XnOlQ6ju7IPtHE5675Mn4Kv7o6g13emHDcX8octh7khK2xwN8iDYTS7jDre-f-85QLe-Dk2a8SOxeKGMbKea7lvwzO09m2gDYSVpwePUEw23Tm1yiq9jRBkluUkNhvhLqWSZiJCWQNCxdK8wK-vB4OiUW5VAO8DhUerYyVjv8A4kz0CKM5PfaSiVRYUoR7VUWRAVEgmCsE3m6hP8KvLHp9DjlGkBOYnOEMxyYJDM8GsxQqcXoA7Ai_WYdXvHHClLzzEqU8fnHDGXWbRGfNwW00aB8JVppVereP7J4aq-Z69mV6E-QB304zd08eAk3bFHiICDMMzk9fwfYjxXTVOTJ8u2Q7IODOezHY8LZMadqq4YZGD5liL7dHvkm0Pqh1eX3T4EcUJeJt6HyrFK8A8YLj_T_TLFGS6ijEAQLOpOlziYS_NFeubWqO5t1hiSfR4f75iJ9mRcR-EF7cNUs3u_D2S7B5PnFxrdH9-mkDXg7s9KGselrxLKDOKHdH44sldCfcWRr8kFV9Ci6jfXJwMeyyjTMcutz01Q7WkaSGnqNEObqTGQYcEn85FR5NTlOv3GVV8OHWy6JFEJrUfPhtwr8WzcTbArEsB3fz8R7Bquhi1uBBqKoY-ZZM4SX0KQ7roTWLIyJwuDQlM3N3NNDGVg8M1I4Ckk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b12cb328d9.mp4?token=XknV9kppFKDtZq2XnOlQ6ju7IPtHE5675Mn4Kv7o6g13emHDcX8octh7khK2xwN8iDYTS7jDre-f-85QLe-Dk2a8SOxeKGMbKea7lvwzO09m2gDYSVpwePUEw23Tm1yiq9jRBkluUkNhvhLqWSZiJCWQNCxdK8wK-vB4OiUW5VAO8DhUerYyVjv8A4kz0CKM5PfaSiVRYUoR7VUWRAVEgmCsE3m6hP8KvLHp9DjlGkBOYnOEMxyYJDM8GsxQqcXoA7Ai_WYdXvHHClLzzEqU8fnHDGXWbRGfNwW00aB8JVppVereP7J4aq-Z69mV6E-QB304zd08eAk3bFHiICDMMzk9fwfYjxXTVOTJ8u2Q7IODOezHY8LZMadqq4YZGD5liL7dHvkm0Pqh1eX3T4EcUJeJt6HyrFK8A8YLj_T_TLFGS6ijEAQLOpOlziYS_NFeubWqO5t1hiSfR4f75iJ9mRcR-EF7cNUs3u_D2S7B5PnFxrdH9-mkDXg7s9KGselrxLKDOKHdH44sldCfcWRr8kFV9Ci6jfXJwMeyyjTMcutz01Q7WkaSGnqNEObqTGQYcEn85FR5NTlOv3GVV8OHWy6JFEJrUfPhtwr8WzcTbArEsB3fz8R7Bquhi1uBBqKoY-ZZM4SX0KQ7roTWLIyJwuDQlM3N3NNDGVg8M1I4Ckk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریدمممم ینی؛
مصاحبه شاهکار این مرد وایرال شده؛ نزدیک خونش رو زدن و اومدن باهاش مصاحبه کنن
😂
😂
😂
+ خبرنگار: شما که خونه نبودین.
_ نه ولی کیرم دهن اسرائیل.
+ خبرنگار عع این حرفا چیه آقا
_ خب الان چی بگم؟ بگم ببخشین آقای نیتینیاهو کصکش؟
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/90823" target="_blank">📅 20:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90822">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64c5ec264c.mp4?token=GiI5rR3ox-0u7hNv2r0785z6mIkD7z0tuurn8EJ-5Ed2hE3g2elr9eRBXw1_TUpkF2lKW3968hZc3UCBtBG3b_M4EXK-HtU_FBJrQ0edcHp4re_BX7Qpxvj7fhAvw5tqbeBZlXoyR-qIen9-7QaHd7bGPFSW4ZvxImM598znThHnIp1aUUycJo28rxt9Hb7M6GsJF0E0CRAEAFvXfaN5j6TOQ3pUdOWcLampg9OzFAhjbUs6AvlL7l5Pi2iWUiR0bMCpkPM3ZaG9mBXfiPDG68NCXvm3VT7Z_MufVH20uwhsY-FCfa3S1f6XvqHGifE0IEMntX7Pw3yLKThaqEiRiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64c5ec264c.mp4?token=GiI5rR3ox-0u7hNv2r0785z6mIkD7z0tuurn8EJ-5Ed2hE3g2elr9eRBXw1_TUpkF2lKW3968hZc3UCBtBG3b_M4EXK-HtU_FBJrQ0edcHp4re_BX7Qpxvj7fhAvw5tqbeBZlXoyR-qIen9-7QaHd7bGPFSW4ZvxImM598znThHnIp1aUUycJo28rxt9Hb7M6GsJF0E0CRAEAFvXfaN5j6TOQ3pUdOWcLampg9OzFAhjbUs6AvlL7l5Pi2iWUiR0bMCpkPM3ZaG9mBXfiPDG68NCXvm3VT7Z_MufVH20uwhsY-FCfa3S1f6XvqHGifE0IEMntX7Pw3yLKThaqEiRiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبلیغ گواردیولا برای پپسی
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/90822" target="_blank">📅 20:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90821">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03866b7fc4.mp4?token=BWFmkzemgkvhpQF6jZxZK_ugJ_EdtAADZj4BCNnDuMd5P0yuPYUtBuiTOFdbBalQw30PvE2OUqXQdSlMmeI7n_-lq6xPHyfy2wLXzgo2BgFtDN5YyJifvfhWOm8bVBK4_tT4TdgS5tMcBMGtk8p8vggcGfksgNU-cvngFLXlzMeiQG6bl6h6SEi7O05PS3hxBGXKYBDB8lBdG1TFLZRSPM_u_MD5l6n--eO4vZ8HX7EihWs0-adlV_JTtd21yvWYryEqPsUI0blxJNesQHHV1pjO9sjZi78fOAjPjHXMeeT_LA5QnkJ2Qoqnsv6i2WwJmVN0sV1HPDo8brKTCRj28Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03866b7fc4.mp4?token=BWFmkzemgkvhpQF6jZxZK_ugJ_EdtAADZj4BCNnDuMd5P0yuPYUtBuiTOFdbBalQw30PvE2OUqXQdSlMmeI7n_-lq6xPHyfy2wLXzgo2BgFtDN5YyJifvfhWOm8bVBK4_tT4TdgS5tMcBMGtk8p8vggcGfksgNU-cvngFLXlzMeiQG6bl6h6SEi7O05PS3hxBGXKYBDB8lBdG1TFLZRSPM_u_MD5l6n--eO4vZ8HX7EihWs0-adlV_JTtd21yvWYryEqPsUI0blxJNesQHHV1pjO9sjZi78fOAjPjHXMeeT_LA5QnkJ2Qoqnsv6i2WwJmVN0sV1HPDo8brKTCRj28Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صف عکاسی با رونالدو توسط بازیکنان زنان پرتغال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90821" target="_blank">📅 20:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90820">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99ea114a31.mp4?token=I-4030WPxZFymLuen4JrXNQ22SwDFYnBLy2Vp1SRT8tKXZ-G3wYaIinIqjSbufIDaSwOgctS2iCdKiBPWkWFpd5TrBCVaHVwfRfoH77K77RrUUFVp7cqc4MkgQxdVPNU1X9hwRTR8aPxN3fTiJWFbs8GhS4gQYcnDn-TjZtvfko43uZ7XM4wj_u2Mzz3qoIP5wdIVcOjVskq6SgCPmbwdGH9jIi1YFQKThvnWBGmfbo59SC2yP1Y-hQd1DFo7lPgpe58Br9AGycjmtuitFZpOuLry3iz3tgnzQiGYB3bOQN2UxCz-bqxda7EQU7AwXJU_1AE9P0bhmv_3yJGFJyVgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99ea114a31.mp4?token=I-4030WPxZFymLuen4JrXNQ22SwDFYnBLy2Vp1SRT8tKXZ-G3wYaIinIqjSbufIDaSwOgctS2iCdKiBPWkWFpd5TrBCVaHVwfRfoH77K77RrUUFVp7cqc4MkgQxdVPNU1X9hwRTR8aPxN3fTiJWFbs8GhS4gQYcnDn-TjZtvfko43uZ7XM4wj_u2Mzz3qoIP5wdIVcOjVskq6SgCPmbwdGH9jIi1YFQKThvnWBGmfbo59SC2yP1Y-hQd1DFo7lPgpe58Br9AGycjmtuitFZpOuLry3iz3tgnzQiGYB3bOQN2UxCz-bqxda7EQU7AwXJU_1AE9P0bhmv_3yJGFJyVgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
ویدیو منتشر شده عجیب از دولا پهنا شدن بازیکنای تیم قهرمان کره‌شمالی با حضور رهبر این کشور
😐
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90820" target="_blank">📅 19:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90819">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNEX VPN</strong></div>
<div class="tg-text">⭕
محدودیتی که لازم بود برداشته بشه برای پایین اومدن قیمت کانفیگ برداشته شد
❗️
گرون نخرید
⭕
طی ساعات آینده قیمت هامون به قیمت های قبل از جنگ برمیگرده
😇
منتظر باشید …
آیدی کانال :
@nexphonevpn
آیدی ربات :
@nexvpnshop_bot</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90819" target="_blank">📅 19:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90818">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🚨
🇫🇷
#فوووووری
؛ باشگاه موناکو فرانسه بدنبال جذب مارک کاسادو هافبک  بارسا؛ احتمالا بارسلونا از فروش این بازیکن رقمی بیش از ۲۰ میلیون یورو درخواست کنه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90818" target="_blank">📅 19:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90817">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🇪🇸
هانسی‌فلیک سرمربی فصل لالیگا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/90817" target="_blank">📅 19:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90816">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wu6MlmYLJDWlyiIQOeK9KAY-VFNxSW8vO1olawCVWDiyxRCjfrdon2uVVCSxpvB9semZ-EyzGCxx2qSDDjcA0UEwo-91jlxmdNBTtN8cO_x1t1DN5i4qRR5iaH_Xa6s--TWWoBNg8TF-7JG1T26wvZMfxi3AYQ4E5N1fyI-B3zsX1rj9L3tc7jmQrt_-NGtZdaQY34KubSpRWNzspnQ9n8LwrgilYVJZNeDEAuR0s3D2GjCmBLYzJMPdACpoYHyRrwtS5bOkC4SYDv7JoomF2OFouuy6IPi0xmf5csarwIK3Elxg2XlABc1MF9cYBtbBfciHGrojZ4hHqDErBEfMfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کونده :
«تا سال ۲۰۳۰ قرارداد دارم. در ذهن من ، موضوع تا حد زیادی روشن است. وقتی در اردوی تیم ملی فرانسه هستم ، این مسائل در حاشیه قرار می‌گیرند. فعلاً تمام تمرکزم روی مسابقات است. من در بارسلونا هستم و امیدوارم به حضورم در آنجا ادامه دهم.»
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/90816" target="_blank">📅 19:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90815">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">تهیه کننده برنامه پاورقی: خبر تجاوز به محمدرضا شهبازی، مجری انقلابی برنامه پاورقی دروغ است و ایشان سالم است و مورد تجاوز قرار نگرفته!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/90815" target="_blank">📅 19:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90814">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5ty10orNqqzttZKsSLqUKZGWg2dLMyX-ByFP0hl-Jf3HVmP_2P2ynp4enrYyvkDywzUmsIBX1N20ABSsNbUI9ptmvcoVZNvB3xFPYwueecSbMs1qG3fspHAorM7sNZZ7N-TywSO7uXw3ASnpv7g2ZfmkOeRdlm0h5WpUBqP_So-EehWrLQERgubOJIp-Ud9y-wOr6zlELHCbC41fsDSPClwxCShm-Y-XSq28mUlSqAa9vfvk9M7WF41UUcL9LlfzxAgx5x7u9bvtJV1i1BPCc1ZrxqrDlqqXQv7_cUU_EKM5VhKzMSCSp6rvHlYuC7HBBBSJoqRMdmHD-9ytKmd1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز هیچکس نفهمیده چرا زبون ویتینیا آبیه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90814" target="_blank">📅 19:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90813">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">تهیه کننده برنامه پاورقی:
خبر تجاوز به محمدرضا شهبازی، مجری انقلابی برنامه پاورقی دروغ است و ایشان سالم است و مورد تجاوز قرار نگرفته!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90813" target="_blank">📅 19:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90810">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lH7vz_TPnPhWkq3GJXcIc8boXkGekdDgNcZ_pO_fr_-xsTnLrKQUHkxOoUKN3N0UyzG_WNOo_HxF31bPi2k6avRNRuv79ZsGxugZK8wOA8yzo6Yfcl2uiM_-88eZB3aqCjYdE_O9ug_e5uHyfy5AFUdYxMUQJEgRVnG9TP37ZuZe_ytzB33XhP8pVMGDKHPKSJZoWQVtdRpN_8kveEu8yEqG9mtI28qduvIYKqbkJ3IhtB3ALfh0kTrv1HKfG-ceM4B4mT5HIGGPRtI0LPDVDBMmvC7S0GcG20O4nU4wl1q380A6UrO7BAr-9IAoDVkIL6TpSb8YZ_h_3N02B9VvQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
هانسی‌فلیک سرمربی فصل لالیگا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/90810" target="_blank">📅 18:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90809">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uy2ynFUlFH7w2-D4Pksq549f_ziW1TgeheRv3Wx2YkNlx67mn-d34abPL-yzMrA7JkdkzphxMiytnXhpAY9Y8A8iZuvuV5jURxlShdxFP84GhRlTYuZh1aMI-IGeuV98e8pDblDPfG4eKc-CK9RLVDH7igFelFsV471r4tU3ZhFpi1s-336nhWiTMD33Yoi2cLjgLK54znA3iU_WKWK6xArfAAuN6TovMbp9zikZid7GVhOU-bD-zeh9iQ16NEJToA0DUV0H6PiAScoc7keMvbmDC7tnc_-I13z6OB1aoNSrcEA8DIdPO8tahtyY3RnMaQSyEeP5LICGO5lqYStSew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محل کمپ ۴۸ تیم حاضر در جام جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/90809" target="_blank">📅 18:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90808">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0n8u-bmXHD8d5rISR2m4877JgzszQE26mHXA09NjcZKFV4q9BTUC16vZIUzgweaFq69lWrZY1BC088S7tYEaJOGoIxmx75XIYQJrEuCMSwLjxeqceUT-Z1olvvyZOPFxy4d63NhepKatJ5ZCWiFjMYxWCrNUxwhP972Q0T8bxqB4mTOCvFCEk_qNzPXDKcpPL-_tQlG02B3btV2_zfSCddSU127XLdeb6G8uQI9P1Lz4RTnyOu36FlGA004bHOz5YFmXhGPjI1SZKpG6KhfkgS2BCRp4ba_EQFCVsgkfrwui9h4rpXkEuz8caYPSA5kIGJDY9O5337UGu9ozJ4ooQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب احتمالی و ثابت تیم اردشیر تو جام جهانی طبق گفته رسانه ها:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90808" target="_blank">📅 17:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90807">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RLvijTXAwGHYMn30zSNAu67J6cHbCjySixJKUDE6dYkyfjUTBnJgOx9QNhzaQV1s0GvSQ6R8ZtQ71NV92cDsKQNBFMk40vkCtYgiv2qd9lXlxM--3nyNBu-ASbcKaR_GHZY92ZaiVtqKIiEW8-iHxsD3bxO1NytV-T13PXrm47XTlFFM1akHjsChzzlma9TJlMEpsdo5YLClLGqXne7PXo81aUvzEGBIEwmyvegFQ35pvWHqM18QAqNjOH7GMkeq_jH2JIGq6m-1cQLACbHLHSn6J8fWcwOX4OnCGjRKJJeJwEbIQajpxUMjyxc_VtMkpffX7OHzFGhTBNHytgkOcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
یحیی گل‌محمدی در آستانه سرمربیگری تیم دهوک عراق قرار دارد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90807" target="_blank">📅 17:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90806">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AMMEDT51N33S0UrmsE2myTokk_CehnKw5M9NhtO83Pj3wlXJWCfrqJy4oUx_capfWF3ObM6DYE7tW6WGn69iw1T_hyMTgFIn5wODoXyNQE9JfnJjISV9I0yrWVB92qJXkXne23TCvRGESACDOnNjT4pgjzmvHdEi8EiqFYslkd702wkqTBa0ljyoFViLO1xY601EOSZROQ6qdthB2Fk6eawmnmVuLsX9L8oXkLL14HOUM7_xHPqOcMrEk_7D_Lx0vf4jga2bBG8_N2ai-0XRZ6n2jEqx92UjFQsE_sYdnkF8VWE_z-7u7QAsgESdVtBuf6P0nD8LDa-9f1ChFYHuWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">4 مربی سابق چلسی که تو این جام جهانی هدایت تیمای مختلف رو به عهده دارن:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/90806" target="_blank">📅 17:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90805">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
یحیی گل‌محمدی در آستانه سرمربیگری تیم دهوک عراق قرار دارد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/90805" target="_blank">📅 17:21 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90804">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZDTs3rPNOCBmM8tb6tYZWs9kYRjfuO7VVN31muVkb288xoKDY8AtrLSyExomAwHN4xQant0R7B7P8PyQwlzjB_r2YlnCgE-g9C5arlDLMUcrUq-HBVr4cLkj5ji-fiu_Us44MUv-gKYEeoSodDBSnzwUi2kmHE_PLBNz22QXASRgksPv_Zh0-ZJeN1dQnWKTDeeYBZOBvUf2SF-JNj1Eu0s2rlPLXdVifyvKT2aYvOShkUTjP6oNaebTEiGRy1kmUCSbBPtTfrbTgBBakQK6ampQsw7oSktFIFx1qpaTvIc2uB7z4xyvv6ZNHzxH1NnOdzqdyaRoKyfhQeF1Jj7mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدربزرگ هالند مثل سیبیه که از وسط نصفش کردن
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90804" target="_blank">📅 17:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90803">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/167838926a.mp4?token=HBUapGxVeWA4dglRZHJtrnsEOje3eJRpHHKVk6IcwSLMM1bC5gU7OGN4sICVzQM5ihcAJCvm1rH7anB6NElajKfFC1Zk4PIZhqWJx_iLFpjoYaGmWhXQPE_f_Ir6p34943Jyhuh54dPPUuQYSOnpexF3iimVTEUQKHoESoDZlErcJ7QTz0JuMekhx1qKjL-p5NZItLnyw4olSUq-Wxr9xCM2LcnPmlrztljIoaPwbg0hOVjslbFQkS-T-49viMjQ0AtUV39C-sDMUqFKp-UGxKjdwlzhEkZ7e3ISLuGHVDnpWHxGqYCdmp6zQmUt7HvCPns2FkiF5cAl0IcDPD8SkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/167838926a.mp4?token=HBUapGxVeWA4dglRZHJtrnsEOje3eJRpHHKVk6IcwSLMM1bC5gU7OGN4sICVzQM5ihcAJCvm1rH7anB6NElajKfFC1Zk4PIZhqWJx_iLFpjoYaGmWhXQPE_f_Ir6p34943Jyhuh54dPPUuQYSOnpexF3iimVTEUQKHoESoDZlErcJ7QTz0JuMekhx1qKjL-p5NZItLnyw4olSUq-Wxr9xCM2LcnPmlrztljIoaPwbg0hOVjslbFQkS-T-49viMjQ0AtUV39C-sDMUqFKp-UGxKjdwlzhEkZ7e3ISLuGHVDnpWHxGqYCdmp6zQmUt7HvCPns2FkiF5cAl0IcDPD8SkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چالش پسر مارسلو با رفقاش به یاد پدر
😍
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90803" target="_blank">📅 16:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90802">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e389c70190.mp4?token=v0jV2mxcNj5sEs44PLEB_TzLvDFXjeorvI2_5xhz5WS6c0xve3mL5KkL9yeKzKxTCpuXheS-ZXGJx6YwaWPKAZ9kGRxS0BeO_Fq74Vu63jIZpBg7n448MktN3ad9zmSbXASQjU5n5yKh0XunDmCuDk1Wjom-MvXhhJPwcUeOr8uo0XUtWbJTPmuZof5U5eTmadHFiVBpCkkxhneuGXQtozjHm_nFv42qqxXuHbP3CLBpo3f9oNr-sQbgc5PEkzpxsWVa6332hRL6EY8OErj4b5EjyZtK4X3PB8-i4mPz57FO_FJSV6fhguzHswBL_vPzewAkcw6pSzu2sdSrobKDtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e389c70190.mp4?token=v0jV2mxcNj5sEs44PLEB_TzLvDFXjeorvI2_5xhz5WS6c0xve3mL5KkL9yeKzKxTCpuXheS-ZXGJx6YwaWPKAZ9kGRxS0BeO_Fq74Vu63jIZpBg7n448MktN3ad9zmSbXASQjU5n5yKh0XunDmCuDk1Wjom-MvXhhJPwcUeOr8uo0XUtWbJTPmuZof5U5eTmadHFiVBpCkkxhneuGXQtozjHm_nFv42qqxXuHbP3CLBpo3f9oNr-sQbgc5PEkzpxsWVa6332hRL6EY8OErj4b5EjyZtK4X3PB8-i4mPz57FO_FJSV6fhguzHswBL_vPzewAkcw6pSzu2sdSrobKDtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
کاش برمیگشتیم به این دوران و این بازی و کلی هیجان و خیال آسوده فوتبال دیدن...
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/90802" target="_blank">📅 16:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90801">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6331bff84f.mp4?token=T4fiN_ig0DOTeuorVrVb9hUgU6n2-n5Ko2GI2jhOkMw3H9WoiS4r3FenyARTDkTlOeHOVXsAxlTlUzvZI4Sjv-LRZwNU-zuBTSSxzxc4NqnRZqXkUuYJuo4f79H5aF5eIL_k6OtmPOhf5juOQ9C00xNpvjyBR4zIP_APxF7M24a5rIvuD1FcR2MV5t5lZV_YREqmV8NRU2J4FM3NI7kI-OXp0T_x78u8m-Ep8JGHn7yGTYPKQ0VOXAj-vJIcnXYaWZ6vuucDCGHIu9z-d9QsxCh71z5O5ep0Bz7zmL7YFZXbl2djGHQA2Qv_6kLQerKUQ50hJmWWBwl6ebIs1Dg_kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6331bff84f.mp4?token=T4fiN_ig0DOTeuorVrVb9hUgU6n2-n5Ko2GI2jhOkMw3H9WoiS4r3FenyARTDkTlOeHOVXsAxlTlUzvZI4Sjv-LRZwNU-zuBTSSxzxc4NqnRZqXkUuYJuo4f79H5aF5eIL_k6OtmPOhf5juOQ9C00xNpvjyBR4zIP_APxF7M24a5rIvuD1FcR2MV5t5lZV_YREqmV8NRU2J4FM3NI7kI-OXp0T_x78u8m-Ep8JGHn7yGTYPKQ0VOXAj-vJIcnXYaWZ6vuucDCGHIu9z-d9QsxCh71z5O5ep0Bz7zmL7YFZXbl2djGHQA2Qv_6kLQerKUQ50hJmWWBwl6ebIs1Dg_kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت مردم آسیا موقع دیدن جام‌جهانی:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/90801" target="_blank">📅 16:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90800">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ke3Tn2Av00gQRAu__SvhYtx8fPJzfPOeIJdc0BiezJzIXPNg-YFAy6xOrTUVLHoX-iwbrUbJSWAC4aNwtfz8YSgujEOq13ZxG-E_28tccMKnkBthJRZP1iUW2PnqUXfcZgJWnUo3de5ASAPb0FT7lQbelOEqOs-N4oxpjfuavWv4TRSF7b7mPP9F0QJ6LSlVrBHs0Lih4dJdhOll-vHoV-OZeal7w0jrC0rEMHGdQgeLf-FoZ98yWuCcySU05ajraXruuJDgZ6Td0f30VprVW-Smo-B3bS075JqwdK8FBAZQYpa8TWWpPi1QTKKHrqno02MaJQmyKT4qwSfsg47OjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ایده 48 تیمه کردن جام جهانی واقعا مسخره بود؛ فک کن سه روز اول اینقدر بازی حساسی نداریم که باید 4.30 صبح پاشی آمریکا-پاراگوئه ببینی:)
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/90800" target="_blank">📅 15:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90799">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e4e72992d.mp4?token=R7IulA0EbV4GaU47jPt-_iS3GMeyi7nWmAHKOLO6_44jZMpM2TQ4Gtv25ZHvq6YmgP_Ew3SumsgCbHoawyUQxwAQkuGd-sc_LjI_ZiGmMGaKEU_QXw-uW9dmPzMytP7tDbvwvTmyV8WI8plGcOVJwDwlvowe6k9_L9jzO8rITwVCS9zkrio6EFtdypLAo-sJUNTICW2-cVyvGauLBLk_7wDyBZA-qQ5CB6RSF5z107XgeYeWrBXxluCSK3peW2aHypbzcK5wcrha-0HaCIygfYnys1nlOrno1E7CoX_DqaL9gfuT4UXvclwCWNg3Lg4kPhnNheQT5MIvE8lAKcIIAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e4e72992d.mp4?token=R7IulA0EbV4GaU47jPt-_iS3GMeyi7nWmAHKOLO6_44jZMpM2TQ4Gtv25ZHvq6YmgP_Ew3SumsgCbHoawyUQxwAQkuGd-sc_LjI_ZiGmMGaKEU_QXw-uW9dmPzMytP7tDbvwvTmyV8WI8plGcOVJwDwlvowe6k9_L9jzO8rITwVCS9zkrio6EFtdypLAo-sJUNTICW2-cVyvGauLBLk_7wDyBZA-qQ5CB6RSF5z107XgeYeWrBXxluCSK3peW2aHypbzcK5wcrha-0HaCIygfYnys1nlOrno1E7CoX_DqaL9gfuT4UXvclwCWNg3Lg4kPhnNheQT5MIvE8lAKcIIAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پیروز قربانی: عاشق تتلو ام و آهنگاشو گوش میدم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/90799" target="_blank">📅 15:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90798">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AsoUgGqT5dt1kybI5xI3AfBgEhF9JzqJuiaJXDmA2BntyxdXK2xPjEy6sWT4zHg2fJLCZDZ56wkkR3Ez0W3KIFan-5dA6udRKzpEkIZJZ7soVc6_nb05WWjYT68RP1LZl4LJXyDu9_dw3JQHrPT3aCXkFOMpkXW4AKQS1CGXdfPfm-XBMiJfxuu69_GUGYVrT1z_r7G3IIhGNdMMWiCTRuVm4acdoXq8fgXaEY372NOxGQqlodje_EozH1DJQW-Id66mWHwuOm_qiah7kFRir9dO097WHMhkNyqkzxYJano7OUromuMP-FVdZgOkRttUizpkS6BKtx1ap06NU7NyMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: افتخار دیدار با آیت‌الله خامنه‌ای را نداشته‌ام. به نظر می‌رسد که ما با آیت‌الله رابطه خوبی داریم و دوست دارم او را ملاقات کنم!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/90798" target="_blank">📅 15:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90797">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bfaf96dd2.mp4?token=OuwwzHdcNyWiOrAmaWJKZi09H21iGKlIOSt4qkS2jUrqeFcDYrOBsaWhcQiavEcFVHYCCyb0GFMJkcwGm_Vyl4iCLnjsI0DNcRDw1xdJwWETaFkkMytw4WDBkMIKe8LYjKK4phF0boiDfsJHxxvc-VqvBzUm-rqfCqqqP4oLVmkVKpsL1tyrxv2S3oNmdo7qCJhA0-Gx2m_fHBbmwxhpUGQzjytiRoCqhZ_iRHLl0lnMzX6UQg9ckO-X2WcjY8OOYtsnVfHIMqd2LTeBViVp4Nu2pyotW2Yld5jDoUmZIoQnxgMEz1syo2Jx2oGHMLJUHkfr4kwDUux0B4zmsOk75w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bfaf96dd2.mp4?token=OuwwzHdcNyWiOrAmaWJKZi09H21iGKlIOSt4qkS2jUrqeFcDYrOBsaWhcQiavEcFVHYCCyb0GFMJkcwGm_Vyl4iCLnjsI0DNcRDw1xdJwWETaFkkMytw4WDBkMIKe8LYjKK4phF0boiDfsJHxxvc-VqvBzUm-rqfCqqqP4oLVmkVKpsL1tyrxv2S3oNmdo7qCJhA0-Gx2m_fHBbmwxhpUGQzjytiRoCqhZ_iRHLl0lnMzX6UQg9ckO-X2WcjY8OOYtsnVfHIMqd2LTeBViVp4Nu2pyotW2Yld5jDoUmZIoQnxgMEz1syo2Jx2oGHMLJUHkfr4kwDUux0B4zmsOk75w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مردها اینجوری بعد باخت خنده و بعد برد گریه میکنن..
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/90797" target="_blank">📅 15:28 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90796">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmXx3LC-Z0YFzVf60C_wOgdIVgICDw4el-TTKgQzhSZmC1mi8rCKuFakKG5KchrcFZSv6KJrAFc3WckkbqvHVHhDlp9nL4GVKiruBI68QWDPggFbvvZKcOLuFDsgCJ4F82L6UW5_1tquW26yfyntmDbbBnXh7KcepgmnnjV6gBU5M6E_eC8YWdITlaL6yI2GVgSFteWiKO78l3OaRuES_9egs3-J1ZFxo8c90lLvBS_2pUZDhmX-s5KyVnN7JRn_-1iYaoF9yr41MoIbsJ2AV_i4Rjej3T6kwx8aOQ-kqPrrPYFYeWR3_oo5AH28eLhYYFmt1uQi9K870V1xP7am4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇯🇵
🏆
سامورایی‌های شگفتی‌ساز که طی چند سال اخیر حداقل یکبار تیم‌های مطرح دنیا رو شکست دادن!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/90796" target="_blank">📅 15:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90795">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
انریکه ریکلمه کاندید ریاست رئال: امشب اعلام خواهم کرد که یک ستاره جهانی درجه یک را جذب کرده‌ایم. من به طور رسمی یک سند قانونی الزام‌آور امضا خواهم کرد که تضمین می‌کند قرارداد با او را نهایی خواهم کرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/90795" target="_blank">📅 14:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90794">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4234f318b3.mp4?token=hJFaWpyH9DytnLDSX2XDm3yVek_gb7GwZaTOo7-5weDW5pxY8VTIHSwOJz4VSJm4FKq8k2iq5AJL8rkFCS7NGrdYDjXf5utGKnUhlrCfEkGLmgkCZ1zZTIZ8XhhL5YC0gm5zblijuacvuMhlsC-lqWTSQMTKyACtGkRYDUstgDMroLy9E8t_tvECVxbtTmM7ytwoGqXLExeFPpaum3Oz3hGXkA-BA5yAB4G4Dyy0PqmTTzid_EW_STJK5ssp76v4xjPamBECi4Ud8Vmh5GrcZy29vCgxrNBV-w7LmWHFWZPhI13KA0FIXlTM97oEJpZSeldzy-YhDhjtEnBhStdzsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4234f318b3.mp4?token=hJFaWpyH9DytnLDSX2XDm3yVek_gb7GwZaTOo7-5weDW5pxY8VTIHSwOJz4VSJm4FKq8k2iq5AJL8rkFCS7NGrdYDjXf5utGKnUhlrCfEkGLmgkCZ1zZTIZ8XhhL5YC0gm5zblijuacvuMhlsC-lqWTSQMTKyACtGkRYDUstgDMroLy9E8t_tvECVxbtTmM7ytwoGqXLExeFPpaum3Oz3hGXkA-BA5yAB4G4Dyy0PqmTTzid_EW_STJK5ssp76v4xjPamBECi4Ud8Vmh5GrcZy29vCgxrNBV-w7LmWHFWZPhI13KA0FIXlTM97oEJpZSeldzy-YhDhjtEnBhStdzsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی که از هم‌باشگاهی هم شانس نیاوردی
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/90794" target="_blank">📅 14:31 · 13 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
