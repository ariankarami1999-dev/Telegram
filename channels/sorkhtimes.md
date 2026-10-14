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
<img src="https://cdn4.telesco.pe/file/Kct_bWr6bykHBygcjDHUMRQEj27Rhf0q548toW-pVlLwFTc5BIeGRfdPRfw-4ZFWxi8nqN4NWrRj2wjydoBBWl6UDHts2mnyxxEtV2OY4GS62ncw9LsoubH-w-T1LlUprFFf6obJbxga73hqg6pEhhTNU00CIDqnv5NoEbh7Ph0oBsT2PWficvlV6qHug8oNr0QNBbL9p91DOaHjyeX5etkS1vw8Ht0AkNdWWYZ0iirf0QXEWpCZ6pbU9UGaJO_WS-RmMEEOcAP8gea_7ljWokjLWaC64c-_leSOg4SKS8t9OOGtC2INTf9Pfx0enX64Xu_LbEnN8QYi9ZOq6uXLSw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-23 01:19:55</div>
<hr>

<div class="tg-post" id="msg-141479">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lu2PcLrsT3GRiKtRE5y3GWeqitvblZ2kZvWAChNQRsT10bafmmFt106IAfEN8rujBKjz4iXRn8ZpMhZzzWcABZ0vt552YG1dOi_5OZ_xe7hu4rhAVidXCF0402nrvh_Q-sZtdoO1iJZMIgBH4UslfezPzWmfC3uuUIVx3dX5Y1meXXNoMyOlydARvLrVScW8IZpAnBIZi6joVSH6rVKBzgr2Li0S98i9_6E2LG--VOdpF4YPP8vf_OgEVqjmUgJZhQbPrirXhyQw2wOPX0RXMXyZcB3H0TJ_QtXG2urycH93P5p-Lr4eL2syR0akKMfII5LIEFKkyB2h2iO0OEzkWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
طبق نمرات متریکا؛ پوریا شهرآبادی بهترین بازیکن پرسپولیس در بازی با خیبر خرم آباد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 883 · <a href="https://t.me/SorkhTimes/141479" target="_blank">📅 00:53 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141478">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔔
با توجه شرایط منطقه مجوز پرواز شبانه به هواپیمای حامل پرسپولیس داده نشد تا تیم امشب خرم آباد بمونه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/SorkhTimes/141478" target="_blank">📅 00:47 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141477">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
چه فوتبالی بود رئال و رم .تا دقیقه 83 رم سه بر یک از رئال جلو بود ...رئال تو ده دقیقه کامبک عجیب و غریبی زد و بازی چهار بر سه برد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/SorkhTimes/141477" target="_blank">📅 00:40 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141476">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
اینترنت چرا امشب اینقدر ضعیف شده
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/SorkhTimes/141476" target="_blank">📅 00:36 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141475">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
یعنی خبریه
🤔
🤔
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/SorkhTimes/141475" target="_blank">📅 23:52 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141474">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔔
با توجه شرایط منطقه مجوز پرواز شبانه به هواپیمای حامل پرسپولیس داده نشد تا تیم امشب خرم آباد بمونه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/SorkhTimes/141474" target="_blank">📅 23:50 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141473">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R8SPWwm3iPOB29Wf6CZwDKVuUS7CSlUs3zatFjmR5QO9qGx3wA2FgmKaT1Gt5ayscK-dIWe1lhETmL9pQ5ur62CvbX44FnE9QM8kH8p_TDSGnyk_ilRjEaPpbnhe9DBIFN7MCs7zkNIGpYUWUIS2rbwT5bp-aBSeA8SJiUgkhf7R6RvYMPuFE_YJMKFKR8xjXfCyqtHGufKQhpgIbaVkD2vID3rDVllfVLL6uzUed_SjCIY2Xb1TuBD7-g3VyBPHFV2SFK95VJUGVlg0r56pyqyS6COrzrgbwjD-xbpdcCi8KHSxPJIq5zL3aSEPzHNyVO8tSz4Pb1p7LO79UjIxiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔔
با توجه شرایط منطقه مجوز پرواز شبانه به هواپیمای حامل پرسپولیس داده نشد تا تیم امشب خرم آباد بمونه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/SorkhTimes/141473" target="_blank">📅 23:49 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141472">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
ترامپ: حمله میکنم کاسه صبرم لبریز شده
❌
❌
ترامپ در یک گردهمایی انتخاباتی در آلاسکا: «منتظر باشید ببینید با ایران چه می‌کنیم. حسابی حالشان را جا می‌آوریم. منتظر باشید ببینید با ایران چه می‌کنیم؛ چون دیگر کاسه صبرمان لبریز شده است.»
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/SorkhTimes/141472" target="_blank">📅 23:40 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141470">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bFo6iPrBsrr432C9mvgf0gAHT1L5OXINUN14xAY6RRw0GYBinZKXdDW2tq50FBOV7hizvW2KZ-amH1X1PRejpfABmorRQHo8JN-1jbqPMvgob-x75Kt6mxidGzhh4BXnwqDFnhLea-rGH9SYGMrsYhwZeUczMWXjBmXGh9O-Me-yc5KuIlxzZQSsxD7341FeNmpdWGCDbWA2-1Lj8IPR_MaxzTdf1fhm-DsmU-7MTuzl7SNmeMcFF1iBULoyZNMCo3615YGAE9y44Pj5SANDiQqWx_wU6ExjCHbXtE-KpJtIDlVauo0PiNKZBqr3LAzApVXFw-jMmvsbPAsida2ysQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
🎥
لحظاتی از عملکرد تیمی سرخ‌ها و فرصت‌های گلزنی ازدست‌رفته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/SorkhTimes/141470" target="_blank">📅 23:22 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141469">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tLxYFitgV7foJ_nJO4kTXv-7yf5QKBmkngv_hBO2O0i4DYj1_TJp7bwQN0FspxfFkwwS93FSgwV8N8nP-jxP7Ql2QRkz9jO1dOBSjtxkd1CtOrwtN7jkMeympsbOBCGKvYM0OSepnOfnz3GuoHguHFpAJK-saooawwor_QO1ZIqBOf7GExO0td2e2XOvPNIck49EWHyk6Wdp7JF5YY2p_0-zpzCfKwE3EnSCOdoJpTJgxkSgHy8P7SpdjucErv-opLBLK-7zVJgOtJ_tPHwi0pjXrz_FU1GXGCFgYTqqg5WESOdOATskHYEluNtcIGShvq4zp1pfyJp2ZKla6k0Zag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
✅
️ اپراتورها خواستار افزایش ۱۰۰ درصدی تعرفه موبایل شدند
‏
✅
همراه اول، ایرانسل و رایتل اعلام کردند درخواست افزایش ۱۰۰ درصدی تعرفه خدمات موبایل را ارائه کرده‌اند؛ در حالی که خبرهای منتشرشده از افزایش ۴۰ درصدی حکایت داشت.
‏
✅
اپراتورها افزایش هزینه تجهیزات، نوسانات ارزی، تحریم‌ها و آسیب‌های جنگ به زیرساخت‌های ارتباطی را از دلایل این درخواست عنوان کرده‌اند.
‏
✅
هرگونه افزایش تعرفه منوط به دریافت مجوزهای قانونی است. / دیجیاتو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/SorkhTimes/141469" target="_blank">📅 23:21 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141466">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxBfUDsDFT4iB-sQpRdxQ3Kg8exUa5-yEWGnK08JudSWwDoTEusi_PFDh1BCFFP9eVOeyO1auJa0uNiQf-dOHUzLbmi7d3d0EogPLIJTBKGMW2B8CsOcIDi9fl-BS_aYDGvThVI4kE3YvezYxZVcp7vO70RpvYs-v-y3JIDOR6CXZgiC2yVaz47vsfbc0zMnyyjh_JmqfJg3_2-y0np_LoCPHsJIZq6OHsny1K-ekLdXiTvq-UGsfUB1ymndKvYR8SAnBsN371i0T32AOygeCsp_0IXrzXn0IyzvHR0isYOS7HRbmG9Dd_DH7aViSevRLWa61EogEsHswZ1Ts4z66w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔴
خبرگزاری جماران:
🔹
⛔️
احتمالا از ساعت ۱۲ امشب، قیمت اینترنت ۴۰ درصد افزایش خواهد یافت!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/SorkhTimes/141466" target="_blank">📅 23:16 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141465">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❤️
🎥
لحظاتی از عملکرد تیمی سرخ‌ها و فرصت‌های گلزنی ازدست‌رفته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/SorkhTimes/141465" target="_blank">📅 23:09 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141464">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
سیدجلال: دیگر کریم باقری تکرار نمی‌شود
🔴
سیدجلال حسینی از فداکاری و تعهد آقا کریم گفت؛ کسی که همیشه پرسپولیس را در اولویت قرار داده است
🔴
حفظ نظم و مدیریت حواشی باشگاهی مثل پرسپولیس کار هر کسی نیست؛ کریم باقری تکرارنشدنی است
❤️
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/SorkhTimes/141464" target="_blank">📅 21:56 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141463">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/foVff5A6yqqtpQLmdnMCCuYuZ_zVwGGJ7C9HEZY9n54iDe5bAGf7GR7TJ8A0S-iVNXcwNAGyRcnhikH2beqN24beZCAQ8N7umXx_JRKWkwjukmEeFUu7pgzECt4EKtT3XVI4rqSYjfMkGOjWAO76hHpuDGxBBkGt71jCDdZEttyRf5QdynzqdK2YaFQYKAXdh8Dk9AqhN8fKHoP3v13VPPf3fRZ5B8EqjD7AgdhXY7D71gthQmYHGTcy_biaaU3Jf678Y3tXAV3aNYmbhMvdvny_Ca-eUMAP1clfNPPr44eIrmHONm5LqxI8L70QDGpo9Os7cMzjz-YF5XzQ34Kkiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشت افتضاح بود و تو مخی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/SorkhTimes/141463" target="_blank">📅 21:49 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141462">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7aa361d650.mp4?token=jfmvTcf1Ybc_X4tjvJFtVTTrc0BAk6zdlf3ccipTNZyt3XIe_lJHo18hZNH_15Gy8Rd5Y2F8mrjEw5am_5zZ0t8ihNFiDqXyTTT0-FiYRDz3a70QZzBjbVca66edzeFgmBdVC6CdKdulj7BhNHK66B1YRYU7_s3biKY6XU-HLTXtxLlkCTkW98OMTHPVK2FCZkOOVsTvh1Dc_qtD-R4eO6x_Td8IWanIA-M8VLnCl-8lnumlM3kQRZSMDmyzcVV7Sm4tvWWA69IYTQAnitXKDa_vYV8fNAi7Tuy7pYQYOW47_Wu3QXKU3hh2TQ-U5pCK51OVShAQwTd1NCNVXIvcTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7aa361d650.mp4?token=jfmvTcf1Ybc_X4tjvJFtVTTrc0BAk6zdlf3ccipTNZyt3XIe_lJHo18hZNH_15Gy8Rd5Y2F8mrjEw5am_5zZ0t8ihNFiDqXyTTT0-FiYRDz3a70QZzBjbVca66edzeFgmBdVC6CdKdulj7BhNHK66B1YRYU7_s3biKY6XU-HLTXtxLlkCTkW98OMTHPVK2FCZkOOVsTvh1Dc_qtD-R4eO6x_Td8IWanIA-M8VLnCl-8lnumlM3kQRZSMDmyzcVV7Sm4tvWWA69IYTQAnitXKDa_vYV8fNAi7Tuy7pYQYOW47_Wu3QXKU3hh2TQ-U5pCK51OVShAQwTd1NCNVXIvcTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🔴
مسعود عبدی، مالک باشگاه خیبر: پرسپولیس مدعی اصلی قهرمانی است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SorkhTimes/141462" target="_blank">📅 21:39 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141461">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🎙
پایان بازی، کار گل گهر برای صعود سخت شد
🔴
المحرق بحرین 2 _ 0 گل گهر
🔵
گل گهر از دقیقه 55 با اخراج عرفان معصومی ده نفره شده بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SorkhTimes/141461" target="_blank">📅 21:36 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141460">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMani</strong></div>
<div class="tg-text">آنچنان تلاشی هم برای دریبل کردن و کارهای ترکیبی نمیکنه قبلنا جسورتر بود برای دریبل زدن</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SorkhTimes/141460" target="_blank">📅 21:34 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141459">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">⚽
🇮🇷
امروز
به معنای واقعی توپ هامون تو گل نرفت البته که نباید ساده از این فرصت سوزی ها گذشت،کم پیش میاد چنین فرصت هایی که تیم به صدر بره هم استقلال آمادست و تراکتور اگر درگیر حاشیه نشه، ساده نباید از این بازی ها رد شد…
‼️
دوتا بازی این مدلی تیم نتیجه لازم رو نگیره هوادار میگه کادر فنی چه گوهی میخوره که مهاجم تو شش قدم توپو نمیچسبونه به تور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SorkhTimes/141459" target="_blank">📅 21:33 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141458">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‼️
🤩
به عقیده من اورونوف در خدمت تیم نیست! داره کم کاری میکنه کاملا تو استارت ها و موقعیت ها مشهوده که ۴۰ درصد توانش هم نمیزاره روی توپ ها
⛔️
این اورونوف کجا اون اورونوفی که میزد تو دفاع کجا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮…</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SorkhTimes/141458" target="_blank">📅 21:29 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141456">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❤️
امروز برخلاف اغلب بازی های گذشته وسط خوب بودیم ولی جلوی رقبای بزرگ تا اینجا مشخصه که وسط باگ داریم و باید تقویت بشه خط هافبک نیم فصل
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SorkhTimes/141456" target="_blank">📅 21:27 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141455">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‼️
🤩
به عقیده من اورونوف در خدمت تیم نیست! داره کم کاری میکنه کاملا تو استارت ها و موقعیت ها مشهوده که ۴۰ درصد توانش هم نمیزاره روی توپ ها
⛔️
این اورونوف کجا اون اورونوفی که میزد تو دفاع کجا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SorkhTimes/141455" target="_blank">📅 21:26 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141454">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
کمالوند سرمربی خیبر: بعد از پرسپولیس زمان برانکو این پرسپولیس واقعا تیم خوبی است و به مهدی تارتار تبریک می گویم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SorkhTimes/141454" target="_blank">📅 21:23 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141453">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iPLKL8_rQhoJr6b6yZZi8733faDhA0ZxYYAAfSZ3zaitDGI5knArtlF3NoUUOJQ0KzxRDHqwU9ridwX6CsjQBbQ8eTH7NfDHbGuY3icFXUt0Op6gOmdMxhxC0TJzqLy8qcbrPFk_HWsaQTMgGqFhgPXcf0Dqw-GfgMm9JkMcPCK99uvnLf_hNqjFno2xE9K-hfI1h9Glam4dnx_zi1N2jja6gMmqMU4tunVW2WmyV-md994ITRcHc33SkZVwvhF_kG1HSMylCcNfanWB2EGRChmkCgVJ9w5JWj2eIATt5mXpjJF8k-AmxOYJiZ7GFIVKrPv02B1yOpxcMYj9iAoRdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
عکس تیمی پرسپولیس پیش از بازی امروز
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SorkhTimes/141453" target="_blank">📅 21:21 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141452">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d462da9e2.mp4?token=kP5oPJRubPg-wYOPvy1_xkudOYoD6NM96BvGPyUr02l8JGIkKDVfmdzSJFrjuDfaHo_L81epQ-5PNOTsdFM-3R_ma0c_2np2ZVNMueyMCzY3_q9ar3qqZU2rMl553KM7mTUGkfMn4io7pnL0DrNQkhDCw9Qt3W9oGV-2PPutUOy5a_rQA7NJItDmDyOygHdoRJWfjefUFalrDAVQ0zH3_LS0h18R2353uFRH5FA4sktPBRshcvUhtOpiffSNluxA8Bjl40f_Ug4ogyMqQ4TnlzOs9hrx49D1UjUFyuv7KpQc_pF-J1bdy4GaQyGXrRGxB0-hlGoDl7vd1GYgLD0iYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d462da9e2.mp4?token=kP5oPJRubPg-wYOPvy1_xkudOYoD6NM96BvGPyUr02l8JGIkKDVfmdzSJFrjuDfaHo_L81epQ-5PNOTsdFM-3R_ma0c_2np2ZVNMueyMCzY3_q9ar3qqZU2rMl553KM7mTUGkfMn4io7pnL0DrNQkhDCw9Qt3W9oGV-2PPutUOy5a_rQA7NJItDmDyOygHdoRJWfjefUFalrDAVQ0zH3_LS0h18R2353uFRH5FA4sktPBRshcvUhtOpiffSNluxA8Bjl40f_Ug4ogyMqQ4TnlzOs9hrx49D1UjUFyuv7KpQc_pF-J1bdy4GaQyGXrRGxB0-hlGoDl7vd1GYgLD0iYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
کمالوند سرمربی خیبر: بعد از پرسپولیس زمان برانکو این پرسپولیس واقعا تیم خوبی است و به مهدی تارتار تبریک می گویم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SorkhTimes/141452" target="_blank">📅 20:18 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141451">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
مهدی تارتار:
🔴
خداشکر صدرنشین هستیم و باید به همین روند ادامه بدیم.
🔴
باید تیم ما تنوع تاکتیکی داشته باشه.
🔴
از کیفیت بازی امروز راضی نیستم.
🔴
از بازیکنان ممنونم چون این بازی سنگین بود.
🔴
من مخالف برگزاری جام‌حذفی نیستم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SorkhTimes/141451" target="_blank">📅 20:17 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141450">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
مهدی تارتار: در نیمه دوم شرایط ما بهتر شد و موقعیت هایی را از دست دادیم که افسوس میخوریم که چرا گل تبدیل نشد/ خدارا شکر صدرنشین لیگ هستیم و باید همین روند را ادامه دهیم
❌
باید تنوع تاکتیکی داشته باشیم که بتواتیم 3 امتیاز را به دست بیاوریم نه یک امتیاز
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SorkhTimes/141450" target="_blank">📅 20:14 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141449">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eb247kGYx058cLBBsRLDToRxW4skz7zWwci0IPbp9Jqe6uJHl3NzLYLDIE3NIFR67LlOq1dDulO6xD_6Rpy5ShQFjUg89PAF0bv50gM4AZ2RLZMRdA_bWq33gvSwy4pq4rMqihHqRt689ywVrU9ZN2PJK2_c4HO7NUvG1uaxwU5tNlQ9P8wRDTzdYNmH7NW8q6vmwcAxpJJxZOurEjLbF8eroa8z-pl30YK8fpKriNQyWsHuOV1nb-y4UPLgmsBoq4WkZLOSsdeachcW9FlK43XsyGGiUf88LvKcdd9GYEfynYaAe4AfVpReZN3ksqIU0Z0UPYn1mNtlno1rZFM4yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
میکس ویژه وینکوبت آماده‌ست؛ جدال بزرگ امشب با یک میکس اختصاصی!
🔵
Man City
🆚
🔵
PSG
⏰
Tonight 22:30
🏟
Etihad Stadium
⚽️
سیتی با ۸ برد متوالی و پیروزی ۳ - ۰ مقابل لیورپول، با آمادگی بالایی به این جدال می‌رسد؛ در سوی مقابل، پاری‌سن‌ژرمن با میانگین مالکیت ۷۲.۱٪ در نخستین بازی اروپایی، توانایی بالایی در کنترل جریان مسابقه نشان داده است. سیتی در ۴ میزبانی قبلی از پی‌اس‌جی شکست نخورده، اما خط حمله پرتحرک پاریسی‌ها می‌تواند دفاع میزبان را به چالش بکشد. نبرد اصلی در کنترل میانه میدان و استفاده از فضاهای پشت مدافعان شکل می‌گیرد.
✅
[ MIX CODE ]:
cfe622
🎁
کد میکس بالا رو کپی کنید و داخل برگه شرط خود، در سایت وارد کنید و از میکس پیشنهادی بازی‌های امشب نهایت استفاده رو ببرید.
🔗
همین حالا وارد سایت وینکوبت شو و فرصت رو از دست نده و دیدار جذاب امشب رو پیش‌بینی کن:
👇
🟣
Wincobet.com
🤖
ربات رسمی مینی‌اپ وینکوبت برای ورود سریعتر به سایت:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SorkhTimes/141449" target="_blank">📅 20:01 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141448">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69b9030706.mp4?token=ebuWDmigGV9qx_sbGYvY61iclmkcihnD6rCiWYYRDPgw8c1aRHVJ-oInbLYP-lqR9rHvtgVIFmQMVZBK08pDioTRFtr3sj5qhQK-QVTq-vt4Lln6sO5rv7pBKsytlBQsCKQkKpBg1CPu57MJOlf6OP6Y5_0mupSPNrzm9UksfSOP-7t6yvQsU3krUsMvWEZZ7gxMOih0m6FhCqB1FK7OmLWXSmjFC1F-h6aHPze463IpZR6SjxKsle0LB9iDjeU1oOanVVYFakdMtIND78ryaWO2kBX6c_BPVXw66SA7iL-BiXCrOM9i9R6wD252p8Umryz-NgPu6QlmoEwwYgR_VhetRXKiIaWSOdfMC5zzra1Jh-NjEBvoVx1kvc8-AeQnwJhBjaUE_5J5TcMpNGJXnbYDqgZ6nwfcmDV3ICb4rq3TfcdMPehOTj6prYRqPRSKyFkeit9wm6FxzSNuz7t_j7JLHz_KEnY_C_rCviOsDuIuQBY8pT4k2UfZ0YgnEngf8Yj_4sGvpt_hq3M4lH1op2Mra25iTMgBx7K9wNGqSEXL4q-IXp2LgfxQYxeux_YO1_DQAYJlh-7qs6-LH2fTcqp1SoaT3j2dwX0uSDfkM1VuAG-0gLvkHJMcsPpqD0L60suKjdELcFjWgSy77P7_39KONpSBJgur2TS0W4_O_lo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69b9030706.mp4?token=ebuWDmigGV9qx_sbGYvY61iclmkcihnD6rCiWYYRDPgw8c1aRHVJ-oInbLYP-lqR9rHvtgVIFmQMVZBK08pDioTRFtr3sj5qhQK-QVTq-vt4Lln6sO5rv7pBKsytlBQsCKQkKpBg1CPu57MJOlf6OP6Y5_0mupSPNrzm9UksfSOP-7t6yvQsU3krUsMvWEZZ7gxMOih0m6FhCqB1FK7OmLWXSmjFC1F-h6aHPze463IpZR6SjxKsle0LB9iDjeU1oOanVVYFakdMtIND78ryaWO2kBX6c_BPVXw66SA7iL-BiXCrOM9i9R6wD252p8Umryz-NgPu6QlmoEwwYgR_VhetRXKiIaWSOdfMC5zzra1Jh-NjEBvoVx1kvc8-AeQnwJhBjaUE_5J5TcMpNGJXnbYDqgZ6nwfcmDV3ICb4rq3TfcdMPehOTj6prYRqPRSKyFkeit9wm6FxzSNuz7t_j7JLHz_KEnY_C_rCviOsDuIuQBY8pT4k2UfZ0YgnEngf8Yj_4sGvpt_hq3M4lH1op2Mra25iTMgBx7K9wNGqSEXL4q-IXp2LgfxQYxeux_YO1_DQAYJlh-7qs6-LH2fTcqp1SoaT3j2dwX0uSDfkM1VuAG-0gLvkHJMcsPpqD0L60suKjdELcFjWgSy77P7_39KONpSBJgur2TS0W4_O_lo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
مهدی تارتار: در نیمه دوم شرایط ما بهتر شد و موقعیت هایی را از دست دادیم که افسوس میخوریم که چرا گل تبدیل نشد/ خدارا شکر صدرنشین لیگ هستیم و باید همین روند را ادامه دهیم
❌
باید تنوع تاکتیکی داشته باشیم که بتواتیم 3 امتیاز را به دست بیاوریم نه یک امتیاز
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SorkhTimes/141448" target="_blank">📅 19:48 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141447">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0297291b4.mp4?token=ES6VuCBCsUEzIQzF9MTj5wvs6SaSkG8wVijDXa4xhKTRO0bPCi5tRsgnkmMkWi2GWchRSjR3nUjtjS6syT95w5edAG5rKhjzfazcvCKT3Agl5oCx6v--RB4_qiW1PPMpbpxQtgnlPMr-3ViZ-cAfHSp6cpqXWoZaas2I7WX32VLKH7DKlHXvMvEwe1sYpFrVGDnXH5-YvQl9DvCq1AjH0BWZJlD-0Zvf6TDRfUCtCTiGGMhQUs5TcPOgjy7R_6Bc3zh1_7vdywGHuYaSOLCfIfIceZdew9okYnE83XA7AqKWxV2tqOzmYUCjHz49BHAHhAeFIRoOrewHMDBcJIXaOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0297291b4.mp4?token=ES6VuCBCsUEzIQzF9MTj5wvs6SaSkG8wVijDXa4xhKTRO0bPCi5tRsgnkmMkWi2GWchRSjR3nUjtjS6syT95w5edAG5rKhjzfazcvCKT3Agl5oCx6v--RB4_qiW1PPMpbpxQtgnlPMr-3ViZ-cAfHSp6cpqXWoZaas2I7WX32VLKH7DKlHXvMvEwe1sYpFrVGDnXH5-YvQl9DvCq1AjH0BWZJlD-0Zvf6TDRfUCtCTiGGMhQUs5TcPOgjy7R_6Bc3zh1_7vdywGHuYaSOLCfIfIceZdew9okYnE83XA7AqKWxV2tqOzmYUCjHz49BHAHhAeFIRoOrewHMDBcJIXaOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
مهدی تارتار: بازی امروز خیلی پرفشار بود/ می دانستیم خیبر در خانه تیم دونده ای است/ خیبر  با توجه به تاکتیک هایی که دارد تیم ها را در خانه اش اذیت می کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SorkhTimes/141447" target="_blank">📅 19:47 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141446">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UkEECENC-n49T_-iqjQpHiy6SQlWiufE6n0I3meUhsshQPuJ1VHCT0kOn5CXo5ccqErn1tJQP4vOFxpV3Lx7vS7UWqXmHe7pId_y8bgWkubJoLCBOVuEBQ4z3FxCE-B5geCook0wDVVa0HTlNPORZEhoF-HMZdg1nvpqvCf_hpUdmtBmE39nvbqPlMuuvM4hWYV_sL_g141FYstm2TWvHC8Ez7UmH28FnNtOK315_q7YlQNr_uLQOP-pgDAUyfQk0fE0ECFEmQPGnAoXxA9p7tKepbGkVlzV0J1lZkT3mn3ui38DSRLeZD8GqDC0VUBho0nHnJJWumK9Bc08MFCLOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جدول لیگ برتر فوتبال ایران بعد از برگزاری بازی معوقه هفته هفتم خیبر و پرسپولیس که با تفاضل گل بهتر صدرنشین شدیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SorkhTimes/141446" target="_blank">📅 19:30 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141445">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dda191766.mp4?token=pJOkvSQi1L21OU_A3M0UvnhCPWhMxDozmCwFndzPEytEKIfFsdfYyocQY0V4S1FKHLLZw6OqiH_bcc8BNlnkVnFWJc2IWTJAFDdybavj_hdXVh6Fp_D_KuEiWxxojEs41adxypQwuTVsMeT4ytVcsG2XnS6j24WfIi4lQd6MmQ7tLwqn-lKXqGXdPiFGhs5F0ChdDuLtTgDhuymvZ7jCpS9nsOGsjhkBYskIuSzB4mJDNH7g0T8Fvv6xVoFxLTysdIYMLySwE5ig7eC0_mJgl2EenKwvMpeVMQ5_pVRIqej0iHjnUz3VT4UxN4Pa6_4X5GnXTxXfRcHb4UCSA2RyVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dda191766.mp4?token=pJOkvSQi1L21OU_A3M0UvnhCPWhMxDozmCwFndzPEytEKIfFsdfYyocQY0V4S1FKHLLZw6OqiH_bcc8BNlnkVnFWJc2IWTJAFDdybavj_hdXVh6Fp_D_KuEiWxxojEs41adxypQwuTVsMeT4ytVcsG2XnS6j24WfIi4lQd6MmQ7tLwqn-lKXqGXdPiFGhs5F0ChdDuLtTgDhuymvZ7jCpS9nsOGsjhkBYskIuSzB4mJDNH7g0T8Fvv6xVoFxLTysdIYMLySwE5ig7eC0_mJgl2EenKwvMpeVMQ5_pVRIqej0iHjnUz3VT4UxN4Pa6_4X5GnXTxXfRcHb4UCSA2RyVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
**حسرت تارتار در پایان تقابل خیبر و پرسپولیس**
❌
از دست رفتن موقعیت‌های پرتعداد توسط شاگردان؛ پایانی پر از افسوس برای خیبر.⠀
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SorkhTimes/141445" target="_blank">📅 19:29 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141444">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a38f3d6db4.mp4?token=IpcfQrjB1WjpfqxUTZmzLi-BKdEn41pNeEptqyN81UtnKatQVm7dNPWtrnoTuO8tp_tnk8npwgtWsuULJDZMzjCmJ0blrjXEmeyDjjDEkpySoyP8DWIKVAyjgER-gbjN8qOsyBj7zkF1bFKlG7W-F2I-W3ceQpY13iL6-rL8Az62_cxEHLmWfTUf6oHM1I_bm4OqMq6o4JZS_Rz6EOTeFIOXS2nAhi23B2PGS1Pm8Kd3cPoW0pi0-g2cU5RXc4EMxg-ZnoAW9IRTzKhcDA9hnp0bp1lt_-UjdSbypziOvdM0VfkVwFAxdtsq-3h7KIMzeWHAh45dNyEylKpz5_djbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a38f3d6db4.mp4?token=IpcfQrjB1WjpfqxUTZmzLi-BKdEn41pNeEptqyN81UtnKatQVm7dNPWtrnoTuO8tp_tnk8npwgtWsuULJDZMzjCmJ0blrjXEmeyDjjDEkpySoyP8DWIKVAyjgER-gbjN8qOsyBj7zkF1bFKlG7W-F2I-W3ceQpY13iL6-rL8Az62_cxEHLmWfTUf6oHM1I_bm4OqMq6o4JZS_Rz6EOTeFIOXS2nAhi23B2PGS1Pm8Kd3cPoW0pi0-g2cU5RXc4EMxg-ZnoAW9IRTzKhcDA9hnp0bp1lt_-UjdSbypziOvdM0VfkVwFAxdtsq-3h7KIMzeWHAh45dNyEylKpz5_djbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
اینبار بیفوما هم نفهمید موقعیتش چگونه گل نشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/141444" target="_blank">📅 19:05 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141443">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
بریم سراغ نیمه دوم انشالله ببریم بازی و
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SorkhTimes/141443" target="_blank">📅 19:03 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141442">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
نیمه اول خیلی سرد و بی روح بدون هیچ نتیجه ای تمام شد ..صفر بر صفر ..
❌
چمن داغون اجازه بازی زیبا رو نمی‌ده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/141442" target="_blank">📅 18:10 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141441">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">✔️
پنالتی واضح روی اوستون اورونوف
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/141441" target="_blank">📅 18:09 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141440">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab522e8e81.mp4?token=tAkiU4M5EPkpATeg4_CTfcX2KNg-RR9EhhCNlozgFUxVjLF0mGUJNkFZ7s3TXipSqCkQqUdTrnuRmDX_ca7kxdP69uH4CQP_iVhrvXSJn9rDC2uyWp0kZUzYPbp_hcpc2L9cXVfVjyLPZSBG0OOvSeIRSofOgH_8VGBhsnE9_fSngpJJ9UxmejQjUThwS36BmEwFktYrGuVd-qXQP9RZjGQSONoQ0LSnBCdMmRbmPgc9HWio9aI85FnVOEw-pUAEwAWmIMmxpWhYyb7P_KklP8DPcQOSkDaXeFIce-ZQWGopNLXr3qqL05V72xgg2abRUhPS4j1BjIwdlNVf2fhS1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab522e8e81.mp4?token=tAkiU4M5EPkpATeg4_CTfcX2KNg-RR9EhhCNlozgFUxVjLF0mGUJNkFZ7s3TXipSqCkQqUdTrnuRmDX_ca7kxdP69uH4CQP_iVhrvXSJn9rDC2uyWp0kZUzYPbp_hcpc2L9cXVfVjyLPZSBG0OOvSeIRSofOgH_8VGBhsnE9_fSngpJJ9UxmejQjUThwS36BmEwFktYrGuVd-qXQP9RZjGQSONoQ0LSnBCdMmRbmPgc9HWio9aI85FnVOEw-pUAEwAWmIMmxpWhYyb7P_KklP8DPcQOSkDaXeFIce-ZQWGopNLXr3qqL05V72xgg2abRUhPS4j1BjIwdlNVf2fhS1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
پنالتی واضح روی اوستون اورونوف
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/141440" target="_blank">📅 18:09 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141439">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b881eeb179.mp4?token=qF366Lb9UDGLbj0cKN2PR7Dqk8CYA7pWuTCcUmfZH5HQMISWUCWMCwM9sZN18ObpDUbCnUNKuy3-dpnj79xihUYTSTNcAjlCmjK4jLXwU4-XRoNb6i2NMLWfuDBQU1TLICUPWAM2wG9MDv56eI6gPaHoKoZ-21bl_Zfy6MN4KkN_Jemjq8gDRPramlpAA4IB1nFaISssAacJmze1fVL19bsAMl5ckWcBQBUzVrj_aytHQVfsS7A3h6rONUGiUW0-A_55NnXfqZObHdDeTziRrqr79SsqnEVpRfGZd05zlUzNUPdvBMLYMnaqr3_lUKzfuYn7e8wIItgtABoCzHmjmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b881eeb179.mp4?token=qF366Lb9UDGLbj0cKN2PR7Dqk8CYA7pWuTCcUmfZH5HQMISWUCWMCwM9sZN18ObpDUbCnUNKuy3-dpnj79xihUYTSTNcAjlCmjK4jLXwU4-XRoNb6i2NMLWfuDBQU1TLICUPWAM2wG9MDv56eI6gPaHoKoZ-21bl_Zfy6MN4KkN_Jemjq8gDRPramlpAA4IB1nFaISssAacJmze1fVL19bsAMl5ckWcBQBUzVrj_aytHQVfsS7A3h6rONUGiUW0-A_55NnXfqZObHdDeTziRrqr79SsqnEVpRfGZd05zlUzNUPdvBMLYMnaqr3_lUKzfuYn7e8wIItgtABoCzHmjmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
❤️
پشماممممممم از قیچی برگردون اورونوف که توپ گل نشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/141439" target="_blank">📅 17:57 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141438">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
برای تیمی که روی زمین بازی می‌کنه این کیفیت زمین از خود حریف بدتره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SorkhTimes/141438" target="_blank">📅 17:56 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141437">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
چمن از بس داغونه چهارتا پاس نمیتونن بهم بدن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SorkhTimes/141437" target="_blank">📅 17:29 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141436">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
بریم برای بازی حساس و سرنوشت ساز بازی ..الهی به امید توووووو...سه امتیازی که مارو به صدر جدول می‌بره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SorkhTimes/141436" target="_blank">📅 17:13 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141435">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
اعلام ترکیب پرسپولیس برای مصاف با خیبر
🔻
پیام نیازمند، محمد‌مهدی زارع، حسین ابرقویی‌نژاد، مجید عیدی، مهدی تیکدری‌نژاد، پویا پورعلی، محمد خدابنده‌لو، محمد‌مهدی محبی، اوستون اورونوف، ایگور سرگیف و علی علیپور.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/141435" target="_blank">📅 17:00 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141434">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
ترکیب پرسپولیس مقابل خیبر از دید ورزش سه
📊
سیستم 442
⏺
پیام نیازمند
⏺
مجید عیدی
⏺
مهدی زارع
⏺
حسین ابرقویی
⏺
مهدی تیکدری
⏺
پویا پورعلی
⏺
محمد خدابنده‌لو
⏺
محمدمهدی محبی
⏺
اوستون اورونوف
⏺
علی علیپور
⏺
ایگور سرگیف
🗣
نظرررتون؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SorkhTimes/141434" target="_blank">📅 16:48 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141433">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce91480d30.mp4?token=ukegiRalGgXUFcIWAoHLIGZbIFsgqfxFY6_OCXcfdiKZ2mm_RZoVS7k3G5GRsOeLImmv-nhJ1k9nyLyDmvZdJ2Eo1tzblwBw1mqCTTq1vF7vfMjR2QrYKNwKtbdt8zYY23d6ZpEOiPSUbC6rbH2JGjSlNjcwgQiem6SzOJguEu1zhXQO0R7hk5O6PA44WTzr-Y64YejKjEifFXeA5NHmUVqN7OWZpSc5ttnVE4WU2Xji5r7aHq63n4DU9CLEb_pkhFpu-Emz1RhN4wG15_mn_g2gRbpxda0iKEJS18NIAc0Lmz0RwMCGFAOCPPwn-yiBn0eqbObxaXokB99Y2mkw_B_zkiO_Yr6kcFqEKSFIRS4_ArksQhfh5yKtRQXLgR7_oPj9Rev9Z1C11YeVuLkMd9TK-upMvTv639wtV5MtROVms9M5MOojGRRJz8N420YUywAO1Pzje-OVbm3s7im7D87ylGjqWHctAz8v-tZdsDTAHLgAtAclCQ5ux-fz5EBZvlFbgruAo0cExdnoXXZojfCOWCkNfsWQ6R9wwvQ3aHm_P-AU8UxdwWETj80Rg1UtayE9dIG7fCSD_N_bGi0K82pLGcZDsXOznPDWAUZ6b_9GHGUaek3PZpmwyQJBREglQdhhZdjIWBAk90jhW-8OKqihBOgnuXNsvZs3ACpGebA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce91480d30.mp4?token=ukegiRalGgXUFcIWAoHLIGZbIFsgqfxFY6_OCXcfdiKZ2mm_RZoVS7k3G5GRsOeLImmv-nhJ1k9nyLyDmvZdJ2Eo1tzblwBw1mqCTTq1vF7vfMjR2QrYKNwKtbdt8zYY23d6ZpEOiPSUbC6rbH2JGjSlNjcwgQiem6SzOJguEu1zhXQO0R7hk5O6PA44WTzr-Y64YejKjEifFXeA5NHmUVqN7OWZpSc5ttnVE4WU2Xji5r7aHq63n4DU9CLEb_pkhFpu-Emz1RhN4wG15_mn_g2gRbpxda0iKEJS18NIAc0Lmz0RwMCGFAOCPPwn-yiBn0eqbObxaXokB99Y2mkw_B_zkiO_Yr6kcFqEKSFIRS4_ArksQhfh5yKtRQXLgR7_oPj9Rev9Z1C11YeVuLkMd9TK-upMvTv639wtV5MtROVms9M5MOojGRRJz8N420YUywAO1Pzje-OVbm3s7im7D87ylGjqWHctAz8v-tZdsDTAHLgAtAclCQ5ux-fz5EBZvlFbgruAo0cExdnoXXZojfCOWCkNfsWQ6R9wwvQ3aHm_P-AU8UxdwWETj80Rg1UtayE9dIG7fCSD_N_bGi0K82pLGcZDsXOznPDWAUZ6b_9GHGUaek3PZpmwyQJBREglQdhhZdjIWBAk90jhW-8OKqihBOgnuXNsvZs3ACpGebA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎦
ترمیم تورهای دروازه ورزشگاه تختی خرم‌آباد پیش از شروع بازی!!!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SorkhTimes/141433" target="_blank">📅 15:48 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141432">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/995cae6ace.mp4?token=TOAE_d2niwlghTt2KeBkEyMHhKlbTkMmvwUxlSD4inc_DsQ3y627-9foRiXLVDfsbj9Gs8_YrPpu89C6ERxMuYxZuvhcJAV0qejPtAiaw3AhXuJ9vzaLwSSv3NWEvMHnJBRFf-sAzs18l8qo-myidWn6U-1IRoBP1BsDcEfYYrfsketg6QhjQwN9ZhScwBIa0l3LYSn2U-JXT549StePEm2aXJ1mRFRAEWS-08HmbCCGLg0eJ5xR71zm4h2zESLDqGkqJ5oXayoOEO-DAJuvmP030uQ_RriJKYvi5oq72q9Ofxb51F_Yh_DNNaj_HkGv9MKY_ezBGCcnX_OA-EBhqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/995cae6ace.mp4?token=TOAE_d2niwlghTt2KeBkEyMHhKlbTkMmvwUxlSD4inc_DsQ3y627-9foRiXLVDfsbj9Gs8_YrPpu89C6ERxMuYxZuvhcJAV0qejPtAiaw3AhXuJ9vzaLwSSv3NWEvMHnJBRFf-sAzs18l8qo-myidWn6U-1IRoBP1BsDcEfYYrfsketg6QhjQwN9ZhScwBIa0l3LYSn2U-JXT549StePEm2aXJ1mRFRAEWS-08HmbCCGLg0eJ5xR71zm4h2zESLDqGkqJ5oXayoOEO-DAJuvmP030uQ_RriJKYvi5oq72q9Ofxb51F_Yh_DNNaj_HkGv9MKY_ezBGCcnX_OA-EBhqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎦
هوادار خیبر: اینجا اصلا پرسپولیسی نداریم؛ بیرانوند بچه سوم را بیاورد و معاف شود
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SorkhTimes/141432" target="_blank">📅 15:46 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141431">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
محمدحسین میثاقی:
🚨
روز گذشته بیرانوند با مدیران تیم فوتبال نیروی زمینی تهران صحت کرده است که از اول آبان به این تیم برود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SorkhTimes/141431" target="_blank">📅 15:45 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141430">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b71aafa3.mp4?token=FB2kkHmgfA_YXJjm27xffsxslJHGN2xOK6NlBAOoOxXHfhnF0x0-Jgg3Vr-7YhI01EAJvMkL02eWu78IzgtVwIqaXfpTrJQg-a5UbsBqpvxzsBINHN_GNDPywn8_s3oPO7vCl0lBgyJlgIuMnZUHBtRDhGF1eVv0tohugy8mDMXR_vLWi8bJzvzf9ypky5qYeAQIqZZo7btdXM2fKPz7I0IN2X0tgK9m3MT8mJv6CrrGQa_w2iav3p6JJI7hAXxTaZV1aD3LIxfuCDrpVo1eP0trjKyCfJvrCnFulXdlgXkR6o8mTB3w6eknMmyeH4Cdicq0xjzfMM6RzmAXe0OFZmPtJrmtPbfSqyUyk5u3zhHWlnYsCQMuia6ncGSzqQ_cUDukKNSrpp-h09_aciUwHkOaPxF72kxsBkEtCkkCr00l6-xReaoxgQrYV-hGOF72CevjDszeLOV4dSZTndG5yd75a2KTekMV6trHAEWMKEJLCvsVrzw48itvZw2SpzK9JuumoF1QmKBI5waZbIkXhekUJs5fmtURSYVgwoPLJBN9uB_FFHtikOKOYGsDkXtAGEOem-F7bh3GRPYMpcizKldMhBbWG9wsNpGbxtibCu-til0u2W2C3zZmiSPLNxE4Q1RLEhRAIhbhmBwagNJ2GpPqKaBHhhO5XuxfjViuvIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b71aafa3.mp4?token=FB2kkHmgfA_YXJjm27xffsxslJHGN2xOK6NlBAOoOxXHfhnF0x0-Jgg3Vr-7YhI01EAJvMkL02eWu78IzgtVwIqaXfpTrJQg-a5UbsBqpvxzsBINHN_GNDPywn8_s3oPO7vCl0lBgyJlgIuMnZUHBtRDhGF1eVv0tohugy8mDMXR_vLWi8bJzvzf9ypky5qYeAQIqZZo7btdXM2fKPz7I0IN2X0tgK9m3MT8mJv6CrrGQa_w2iav3p6JJI7hAXxTaZV1aD3LIxfuCDrpVo1eP0trjKyCfJvrCnFulXdlgXkR6o8mTB3w6eknMmyeH4Cdicq0xjzfMM6RzmAXe0OFZmPtJrmtPbfSqyUyk5u3zhHWlnYsCQMuia6ncGSzqQ_cUDukKNSrpp-h09_aciUwHkOaPxF72kxsBkEtCkkCr00l6-xReaoxgQrYV-hGOF72CevjDszeLOV4dSZTndG5yd75a2KTekMV6trHAEWMKEJLCvsVrzw48itvZw2SpzK9JuumoF1QmKBI5waZbIkXhekUJs5fmtURSYVgwoPLJBN9uB_FFHtikOKOYGsDkXtAGEOem-F7bh3GRPYMpcizKldMhBbWG9wsNpGbxtibCu-til0u2W2C3zZmiSPLNxE4Q1RLEhRAIhbhmBwagNJ2GpPqKaBHhhO5XuxfjViuvIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏟
⚪️
🟥
آخرین وضعیت ورزشگاه تختی خرم آباد در آستانه بازی خیبر و پرسپولیس
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SorkhTimes/141430" target="_blank">📅 14:58 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141429">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🔴
🎙
پیمان حدادی: از اول فصل تیم گرفتیم هر یک از تیم‌های فوتبال پرسپولیس گل بزنه، یک زندانی آزاد کنیم و تا الان ۴۳ زندانی رو آزاد کردیم.   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SorkhTimes/141429" target="_blank">📅 14:57 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141428">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
ترامپ درباره ایران: ما باید این موضوع را به پایان برسانیم، و این فقط به این بستگی دارد که ما می‌خواهیم این کار را به چه روشی انجام دهیم: روشی دوستانه یا روشی که آنقدرها هم دوستانه نیست.
❌
شما خیلی زود متوجه خواهید شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SorkhTimes/141428" target="_blank">📅 14:48 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141427">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🤩
✅
معوقه هفته‌هفتم لیگ‌برتر فوتبال
🤩
پرسپولیس
🆚
خیبر خرم‌آباد
🇮🇷
🗓
تاریخ چهارشنبه ۲۲ مهر
⏰
ساعت ۱۷
🏟
میزبان خرم‌آباد  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SorkhTimes/141427" target="_blank">📅 14:23 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141426">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">💥
💥
سید جلال حسینی دستیار امیر قلعه‌نویی در تیم ملی شد و قراره در جام ملتهای آسیا قلعه نویی رو همراهی کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SorkhTimes/141426" target="_blank">📅 14:22 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141425">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9oL2s9yrds__65d4075YJHidiQfiFEdILvtxzia-XXOMfGheYq9KQNOTzH5E1cVpD2zvbg91pO2OCFA21AYPcQccRKpad_lce1FcHtA1vjq5QDxucH7giAjNCD2Y3KbEUEiiaKGyEf7uSOVnK97Lq_HXkG72eWdFblEGTT9VSJb9Vvk_phStyGGDs9shWtYf1aeGUu1S9Dwmyc-48x7ijCJse4YdNdGEkTOF1CnKVqTN306bNA-TY8k6SFfbJp9-hr7W62Q2NEzjJ9UWBqy6J1YMv2ismi9a-MBFJMM8gr0iNwyn_WM6ZRPiqsQxWbtaIOuCaJmT3mRtb70nR_3nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
نبرد غول‌ها در اتحاد؛ سیتی و پاریس برای سلطه بر اروپا!
🔥
⚡️
[
منچسترسیتی
🔵
🆚
🔵
پاری‌سن‌ژرمن
]
⚽️
[ نکات کلیدی و مهم ]:
👇
1⃣
.
نبرد مالکیت توپ:
سیتی با پاس‌کاری سریع و پرس از جلو به‌دنبال کنترل ریتم بازی است؛ پاریس روی انتقال سریع حساب می‌کند.
2⃣
.
فضاهای پشت دفاع:
سرعت مهاجمان پاریس می‌تواند خط دفاع سیتی را در ضدحملات به دردسر بیندازد.
3⃣
.
نبرد خط میانی:
تیمی که توپ‌های دوم و دوئل‌های میانه زمین را بیشتر ببرد، شانس بیشتری برای کنترل مسابقه دارد.
4⃣
.
موقعیت‌سازی و گلزنی:
کیفیت ضربات آخر و استفاده از فرصت‌های داخل محوطه، عامل تعیین‌کننده نتیجه خواهد بود.
5⃣
.
سناریوی بازی:
با توجه به سبک هجومی دو تیم، گلزنی برای هردو تیم محتمل است.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/141425" target="_blank">📅 13:28 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141424">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
به ادعای خبرگزاری هفت ورزشی مهدی تیکدری از بازی کردن در‌دفاع چپ ناراضی است.
✍️
هفت ورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SorkhTimes/141424" target="_blank">📅 12:21 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141423">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
محسن خلیلی، سرپرست پرسپولیس:
❌
یاسر آسانی؟ باشگاه تمام مسائل را از صفر تا صد پیگیری می کند. داخل کشور به نتیجه نرسیم صددرصد در دادگاه عالی ورزش دنبال می کنیم. ما نگفتیم این پرونده پایان یافته است. مندیت آسانی به پرسپولیس؟ بله او مندیت را داشت اما زمان همه…</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/141423" target="_blank">📅 10:44 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141422">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cuku6xdhsxQTab1anp_BrB8k2Z0t_CHQEYg_xPDPo9vvWbGhyxXTpurq1jogba8-p8ePAMgU-XaWKY5GSkq3g-_hNW_q3at36iiBSDZFeQIwvYvHxlWtbcTMsTRM10WR7zmsSIQZMA060nGXEV12Tsqi72vREC_-Ha6A4AwIB2KPqz_R0HP8rXXZMW5YrX4jKLBEK453HsEQvJVnyCc4ZWV7ANnYTrrYOHBY4X7IBWhqc1HqMSIC1yUH2YCxxJZIsrexZvCyOse9sqip_XU8byjlf7AvtJaIvAo2_YOMXjgqbWUij-IlDPh9V7DCA5VB7LyYa2_cjdJ8bmkOJueP9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ورزش‌سه: دنیل‌گرا به مرز آمادگی رسیده
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/141422" target="_blank">📅 10:42 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141421">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
حمله تند امیر قلعه‌نویی به عادل فردوسی‌پور: قرارداد من رو گفتی، درآمد خودت را هم بگو. بگو اسپانسرات به کجا وصل هستن. بگو در جام‌جهانی چقدر پول در آوردی. تو فقط ابزاری. هر وقت بخوان میزارنت داخل کمد، هر وقت بخوان میارنت بیرون.   «سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/141421" target="_blank">📅 09:18 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141420">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🎙
امیر قلعه نویی، سرمربی تیم ملی فوتبال:
◽️
عدم حضور در لیگ‌های معتبر؟ بازیکنانی که در امارات هستند با اسناد نشان می دهیم نسبت به بازی با مصر 25 درصد افت داشتند
◽️
تغییر در همکاران؟ نه چرا باید تغییر کنند؟/ در جلسه هیات رئیسه من 10 دقیقه توضیح دادم و یکی یک…</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/141420" target="_blank">📅 09:18 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141419">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🤩
✅
معوقه هفته‌هفتم لیگ‌برتر فوتبال
🤩
پرسپولیس
🆚
خیبر خرم‌آباد
🇮🇷
🗓
تاریخ چهارشنبه ۲۲ مهر
⏰
ساعت ۱۷
🏟
میزبان خرم‌آباد  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/141419" target="_blank">📅 09:14 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141418">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n9Lubq9W30-f15IYlmnAsUAGcMuZuAXbrYiHe0rz3IRvz-qSSLS9w8CeEiLwS7qCjmqFaQPlYnQ_9kZs3eFwYzE3J0BFujqM4-9kwUtgjzPPQb3SlNXeXL8Sl9xVG9eko1538hlJvu7hGqqhl_uTMJV-vHmSg_3cASzU1VqBMFWIXUS1xwa8-5_R46Dy3Ec0WtUirHOqz78shFcns4LkSwdfhDd2eyxeh5SBIhupAbNm48wJoQuXe_e4XoMXMrFRHCmaZqcavcELi5YJwlyCB36v2cC8RCalETSUTZlN700wg91tNc5lrMgdy4hPL7BdZEb7QIvc9ri0VNpu5FRQBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
فرداشب، لیگ قهرمانان اروپا در اوج هیجان؛ از نبرد سیتی و پاریس تا جدال تاریخی رم و رئال، یک شب تمام‌عیار برای عاشقان فوتبال!
🔥
⚽️
نبرد سیتی و پی‌اس‌جی، تقابل سرعت هجومی و کنترل میانه میدانه؛ جایی که کوچک‌ترین اشتباه دفاعی می‌تونه تعیین‌کننده باشه. رئال مقابل رم از برتری تجربه و کیفیت فردی برخورداره، درحالی‌که لیورپول با وجود غیبت چند مهره مهم، شانس بیشتری برابر لاسک داره. دورتموند هم روی کاغذ برتره، اما ضدحملات بودوگلیمت می‌تونه معادلات بازی رو تغییر بده.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی بازیای فرداشب همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/141418" target="_blank">📅 01:17 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141417">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t_8XUgHFF_x1E8BKK7lCL3JsKhm0F-QFdd_lWba-tYDhOrXFNw2awu4uUxktcFYA2mvvZksEdAdpnjga7UBeX7nxnrZjPOJqT5K930cPxl842bJtDebr2TguIeLNgC9eUqlyMwqm0I5QOwdIESAxHvnODiZRfFzlve4XD0zF6tqDhpafOJbRNQ7IlWfuC1oDLpnp1brPkcrsb2OEQUhFWiwaM0diQqxkrZSXzZudfzrO4e7Tc9AbO9aQ8cPvSeVxmWhzs2A1fKZx7YAcKo-dQ1EeYp5XQBQVvwMT_YV9IrJ8uYtvOn3HaAqHGMprhRmzFbusJa8Dh9jc3VgVyJ7l-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
مقایسه نیکمت پرسپولیس و کیسه در دوران محرومیت
❌
کیسه بجز ترکیب اصلی فقط حدود یک همت قرارداد بازیکنان ذخیرشه ، این وسط هم دو سه تا جوان هم گذاشتن روی نیمکت که مثلا ما هم اره...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/141417" target="_blank">📅 00:35 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141416">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpdLel2Dje8Ghf_mMM-EPkmAZP60AyuPsp7aCFkO5ri3aA6nVaouPru-IJWcESp7tKqJXRRbVobk58yWT7-FeUUYOWbmbpN2Gi4vm-dBKr4L00QsPFjJp8ckJ_rD5s-xo5Jki1M2V7RfN3FAuCDv9Zy9VHlGJbIMk0uR8bdDg0FalwBKMdyZYbk9RnKhQghFNoTFCcJGhYpSa3BRQmWXwWtX4BoCbx1Hj81ZZQBO_09Nu-EEmXj_jBGkB46J38lkH0mYQcUta27Ynuvvtpbquj2_wO3kPyWdj5GiawO0oE87bMWHuq_3Z7iRBCcZBFGszp4anypytDnwvZz55cbH3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کریستیانو رونالدو : من کامل‌ترین بازیکن تاریخ فوتبالم! اگه کسی مسی، پله یا مارادونا رو ترجیح می‌ده، این دیگه سلیقه شخصیشه و منم بهش احترام می‌ذارم. اما اینکه یکی بگه کریستیانو رونالدو بازیکن کاملی نیست، یه دروغ محضه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/141416" target="_blank">📅 00:33 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141415">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KrTtQHO5kNU0F_647Q2qP3T_ZPFKvjxrTf-SG-o2HwiOT2gv4yG0jIREtqae069BZn-6U5WuG3O-zEZvSw9nWVqTHMbgPYRTMCCBmmNngjhXyii1kWValZvbqqgPU-Zq4bAbPmImNEPW2JlKnxKvCqRVVoVg2vR73R02KohOiizuFbfXoo5fXwe7uJsetKHOML4ExsPUtYyepHFvYUQK6j21CEqjj5WGywVlPOeJXhtLb7y86AkBX36T3l-cGcGpxeziOgvh2umgLGXNIYJI2E1GVTdgkRvJkVmOeL_weB-Wn9L14ug0dqtte7jLUBH4HuzOI4CAj-Le94Mk1ijDfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📘
⭕️
سعیدی: هیچ‌ نمونه مثبت یا حتی مشکوک در لیگ برتر فوتبال نداریم
📘
دکتر رضا سعیدی قائم‌مقام ستاد ملی مبارزه با دوپینگ ایران، وضعیت کنترل و مبارزه با دوپینگ در فوتبال ایران داشت تاکید کرد: در این فصل از رقابت‌های لیگ برتر و لیگ آزادگان هیچ نمونه دوپینگ مثبت یا مشکوکی نداشته‌ایم. باید اعلام کنم به طور کلی در ۲-۳ فصل اخیر هیچ‌نمونه دوپینگی در لیگ برتر و لیگ آزادگان مثبت اعلام نشده است
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/141415" target="_blank">📅 00:16 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141414">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🚨
خسته نباشی آقای تارتار
🚨
🚨
🚨
با وجود انتقادهای ابتدای فصل، تارتار تونسته پرسپولیس رو به شرایط خوبی برسونه؛ از اعتماد به جوون ۱۷ ساله‌ای مثل پویا اسمی تا احیای بیفوما و خدابنده‌لو و مدیریت شرایط اورونوف. حالا سرخ‌ها با یک بازی کمتر، فقط یک امتیاز با صدر…</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/141414" target="_blank">📅 23:06 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141413">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9243295073.mp4?token=fot_Mvyqgs7MFpvRv_GEXh7hVn7yUUuS-0pLVNRanZP1cIN-qGIbNm9R2GnlEsUkIURSDjvUlCCNl38SlyV0IUPBhXskEOG2BhsuSWFBqE-k0YllKEk_vyLql0rigH6Z6PCgG86JYpIs8cfKOzfccPa_BkVdQMHrlvl-33qX_SOtOaIfL7F2TdXYv4zDf19sZNrGXKn0ifO05rt8wXJyuwGOwAcOSPIVlmlsJqv_1byDpiB0H4pnE8AGnPbQtNDHhS7j_nXwtYq24HpTs92FpzOszDs4bwgOYuktpo0e7tI-z-Qk-t9e9LUhjeYNMjGro20bZcXrzD5EOcX5pSn_TXwEvicPlM9IZPut8s1LiDHZhYyRPulMqRWNUqOt0-r7pgHyccmQNNoe4tH50vnEImAq-kBm8t6VjvRq5ZD3rs8vby3jFjMoVDn-GARySmIrV6U0lEyZLDYalKrke52l66kG_DvKt_N1g5Us_thwlFOGb-UczVAShpH34dnG310EWtbwZcIIeA7l_CGd7LwZWM1TzMn-HRKxFuIQxHqocXe9WPip2PUgdws6RTyPL8a2KUOdRUgzpOBOKRmNdG2jx5oFEJQf6LqqJJgoQzkH8yXc47a0Fbz38LJAZcT_rc_F4vXlECgr3mJ_VWCh5JUTSAcJi6tUl3s-bzcvPN83d5s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9243295073.mp4?token=fot_Mvyqgs7MFpvRv_GEXh7hVn7yUUuS-0pLVNRanZP1cIN-qGIbNm9R2GnlEsUkIURSDjvUlCCNl38SlyV0IUPBhXskEOG2BhsuSWFBqE-k0YllKEk_vyLql0rigH6Z6PCgG86JYpIs8cfKOzfccPa_BkVdQMHrlvl-33qX_SOtOaIfL7F2TdXYv4zDf19sZNrGXKn0ifO05rt8wXJyuwGOwAcOSPIVlmlsJqv_1byDpiB0H4pnE8AGnPbQtNDHhS7j_nXwtYq24HpTs92FpzOszDs4bwgOYuktpo0e7tI-z-Qk-t9e9LUhjeYNMjGro20bZcXrzD5EOcX5pSn_TXwEvicPlM9IZPut8s1LiDHZhYyRPulMqRWNUqOt0-r7pgHyccmQNNoe4tH50vnEImAq-kBm8t6VjvRq5ZD3rs8vby3jFjMoVDn-GARySmIrV6U0lEyZLDYalKrke52l66kG_DvKt_N1g5Us_thwlFOGb-UczVAShpH34dnG310EWtbwZcIIeA7l_CGd7LwZWM1TzMn-HRKxFuIQxHqocXe9WPip2PUgdws6RTyPL8a2KUOdRUgzpOBOKRmNdG2jx5oFEJQf6LqqJJgoQzkH8yXc47a0Fbz38LJAZcT_rc_F4vXlECgr3mJ_VWCh5JUTSAcJi6tUl3s-bzcvPN83d5s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟢
فراز کمالوند: پرسپولیس آماده‌ترین تیم لیگ است؛ شناخت کافی از پرسپولیس داریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/141413" target="_blank">📅 22:22 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141412">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
دبل سردار آزمون جلوی الاتحاد توی ۱۶ دقیقه ابتدایی روی پاس غندی پور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/141412" target="_blank">📅 22:17 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141411">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
ترکیب پرسپولیس مقابل خیبر از دید ورزش سه
📊
سیستم 442
⏺
پیام نیازمند
⏺
مجید عیدی
⏺
مهدی زارع
⏺
حسین ابرقویی
⏺
مهدی تیکدری
⏺
پویا پورعلی
⏺
محمد خدابنده‌لو
⏺
محمدمهدی محبی
⏺
اوستون اورونوف
⏺
علی علیپور
⏺
ایگور سرگیف
🗣
نظرررتون؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/141411" target="_blank">📅 22:12 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141410">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
تعلیق دو جلسه باقی‌مانده محرومیت امید عالیشاه
🔻
کمیته انضباطی فدراسیون فوتبال با درخواست باشگاه گل‌گهر سیرجان برای تعلیق دو جلسه باقی‌مانده محرومیت امید عالیشاه موافقت کرد.
🔻
کمیته انضباطی پس از بررسی درخواست باشگاه، با توجه به سپری‌شدن دو جلسه از محرومیت…</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/141410" target="_blank">📅 22:08 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141409">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
از تهران تا خرم‌آباد با کاروان پرسپولیس
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/141409" target="_blank">📅 22:04 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141408">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❌
❌
❌
محسن بنگر : امید عالیشاه اهل فحاشی نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/141408" target="_blank">📅 22:02 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141407">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/785f027d31.mp4?token=q1CkzkFBKzyBlA2m9GzeTJZ-afl9K_tKl-wq5CNHhwiQfGBpmkGb3y4aMHVXOB8UjrmZ6Owi5diky-6Soj8SqE25i1nm4XUcKO71Bph-l0B_CjJ-ceTHW7XmMk_0GZ8LIx28_AZm4TmMxEEllq-PBHMGOOWIutcD-yA4g59Y8M1I8e40bPOAovY-9SbQLG7SpDqL1MWZvDwQOklZbR67dYZjSHucMlli010naVorMDsMnF1jiRz34TQWmXSjPfaEBA3eWUlzbUT6po0NUEyXTdmnXRalIrutA8fMQtCFYGFhr2tHYAG2PGEVS-IIORZJhJZCuLgo7_q2xaedOr9-mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/785f027d31.mp4?token=q1CkzkFBKzyBlA2m9GzeTJZ-afl9K_tKl-wq5CNHhwiQfGBpmkGb3y4aMHVXOB8UjrmZ6Owi5diky-6Soj8SqE25i1nm4XUcKO71Bph-l0B_CjJ-ceTHW7XmMk_0GZ8LIx28_AZm4TmMxEEllq-PBHMGOOWIutcD-yA4g59Y8M1I8e40bPOAovY-9SbQLG7SpDqL1MWZvDwQOklZbR67dYZjSHucMlli010naVorMDsMnF1jiRz34TQWmXSjPfaEBA3eWUlzbUT6po0NUEyXTdmnXRalIrutA8fMQtCFYGFhr2tHYAG2PGEVS-IIORZJhJZCuLgo7_q2xaedOr9-mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
وحید امیری بازیکن سابق پرسپولیس پس از ۷۰۳ روز موفق به گلزنی در لیگ‌برتر اینبار با پیراهن فولاد خوزستان شد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/141407" target="_blank">📅 21:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141406">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCD770vG45vxqFvUCyTgHT886_yRW1DNfdzGQMU9yXxgFPw5u0yo7wu0C85dDKWTyjaUrcVuUbqJgoX-vlYOLBUwvXn-UGG6xCuyC9XXJzPQpCIKeoQf85yCLajrQlLhqxSpoqBeISJOnyWaGMRSxMJc8FW_W-CPmSsOrmvetWscWOmKWf-UeLq4LfUAF8JPS9cKsg7E9MrNk_hIh0-6TZqlGWgvgzNOGCcoGTVLThfvNx5TsX5CD5RDQr9dBk1JnejFu6A3Y5FpQvRVsshA9HmXvOP8ElJYnKSVdnG_8A7xQH7oZicXNNCiV1yHqnbuij8xIGlwlJWBnh_ktUYRgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تارتار به نشست خبری بازی با خیبر نرسید.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/141406" target="_blank">📅 21:11 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141405">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N7HAxt2tYf13AF9g5oZlF5yhIf1fMchFxhEq_PaLIu26hdKXUZ9-OKD4uZWsf_ZpDrrz-pkxSLqUtD2LveHfMgmLtKFAJkVZtfylK0NR1KdPdcy8Vom0IS1tqQ6llL4Egu_OQMsC4BsWu4LtiYAMb-kFuQQeUsY804DZG8Wr1HFw9bXYER3pgBlhfAigiG65IXaD7IsszW-a4KM4GLgKe3f_GkKraplvofuFfZPhlphG_MgMXBaVv3ZZDrR-ZQIgex-z2ny9dYX3xGizsbiZUEioXKFJ93KNFTZaFcse2dHJ06HR1tQl_WjkpK7EbFhk7im4cdzyos9bbgrSsx_IiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
جهنم استانبول در انتظار غول کاتالان!
🔥
[
گالاتاسرای
🟠
🆚
🔵
بارسلونا
]
⚽️
از نظر آماری، بارسلونا در ۵ بازی اخیرش در لیگ قهرمانان و لالیگا ۵ برد داشته و در مجموع ۲۴ گل زده؛ گالاتاسرای هم در شروع اروپایی‌اش ۳ - ۱ به اسپورتینگ باخته است. بارسا در ۱۰ تقابل قبلی دو تیم، ۶ برد مقابل یک برد گالاتاسرای دارد؛ با این حال، فشار هواداران در استانبول می‌تواند بازی را پیچیده کند.
سناریوی محتمل: برد شاگردان هانسی‌فلیک.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/141405" target="_blank">📅 21:01 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141404">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
🚨
مهدی تارتار: از فدراسیون می‌خوام که جام‌حذفی رو برگزار کنه و مام حاضریم فقط با جوانان مون بازی کنیم.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/141404" target="_blank">📅 19:56 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141403">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f8f94fff6.mp4?token=lzNof_GNSLU9iPB830j1vsWFA-NKadlG5xrIaOD4plfTSI1P8mPaNYjLXAOHsK50rEHhxjPGH-HNW0btTk5R76PaEgkBYN0rEqtkofni4QDf77MMPud7aAyjG4By8-pC5GuXMv0X8VfcKIq32fSU8V54rxCHzq6ohVxGgUeo-QvRNtmDESLFL3tWqaD9VFw7CwPDE9k85r7M3KrKwpMLdPJINlhVZ6aun3oAluOo_sZvlB0osvrfNJNwbLZ1jA-8HmxUDoA-ACG3_scHV_49g7jgMK_8kX61cFRTwJvCcPci6-rbuGvs20QzS6zKyPPjOtVswZ-VUBQ8OJnnSVNmrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f8f94fff6.mp4?token=lzNof_GNSLU9iPB830j1vsWFA-NKadlG5xrIaOD4plfTSI1P8mPaNYjLXAOHsK50rEHhxjPGH-HNW0btTk5R76PaEgkBYN0rEqtkofni4QDf77MMPud7aAyjG4By8-pC5GuXMv0X8VfcKIq32fSU8V54rxCHzq6ohVxGgUeo-QvRNtmDESLFL3tWqaD9VFw7CwPDE9k85r7M3KrKwpMLdPJINlhVZ6aun3oAluOo_sZvlB0osvrfNJNwbLZ1jA-8HmxUDoA-ACG3_scHV_49g7jgMK_8kX61cFRTwJvCcPci6-rbuGvs20QzS6zKyPPjOtVswZ-VUBQ8OJnnSVNmrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
وضعیت درب محل اقامت باشگاه پرسپولیس هنگام رسیدن تیم پرسپولیس در خرم آباد با حضور هواداران خیبری
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/141403" target="_blank">📅 19:52 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141402">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
تارتار : بچه هامون دارن به تناوب بازی میکنن، دست یه مربیم اونقدر باز نیست که بتونه 15 تا بازیکن رو بذاره تو ترکیب، انصافا استون هم تو تمرینات داره تلاش میکنه، من دارم میبینم همین قدری که تیوی بیفوما داره تلاش میکنه استون هم تلاش میکنه ولی به هر حال گوی سبقت…</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/141402" target="_blank">📅 19:51 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141401">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V3sIxDJ1yKsp8zdokVLKuEyLBsTKj2u3_WjoRwCzp8bpNw0uIWe0EdYQpkJkvlKW7-cM3gYeyVIE60bB7Fy4Bw1GUFqgnAN5B_ExhXFja9VJ6-Db-RNG21m56fiO_O1541kWWNmULgBXeKAc8JP6htqPP_39iwG5fEdK1GxxbBb0uIRRzaOdUbJGhS9NLyGPhoK8pHwEeH8rcgdVm-1vkcrKwzDohTkO0e9PtnjetK1XEkQ3DASGya2kigcCU-FRXSHX0kRveYjVnDPQQTfkbMkcf0mjkTUZ6r9kOdyyukMLEFdGuvshPblyyjAxT62VWsRa0LGPFYukQgOyq37hIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☑️
جدول لیگ پس از پایان ۳ بازی معوقه هفته هفتم
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/141401" target="_blank">📅 19:45 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141400">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
بیفوما در آستانه دیدار مقابل خیبر دچار سرماخوردگی شده  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/141400" target="_blank">📅 17:16 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141399">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
شایعات : بیفوما با برخورد با یکی از بازیکن های جوان پرسپولیس مصدوم شد و بازی فردا رو از دست داد   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/141399" target="_blank">📅 16:47 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141398">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🚨
خسته نباشی آقای تارتار
🚨
🚨
🚨
با وجود انتقادهای ابتدای فصل، تارتار تونسته پرسپولیس رو به شرایط خوبی برسونه؛ از اعتماد به جوون ۱۷ ساله‌ای مثل پویا اسمی تا احیای بیفوما و خدابنده‌لو و مدیریت شرایط اورونوف. حالا سرخ‌ها با یک بازی کمتر، فقط یک امتیاز با صدر…</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/141398" target="_blank">📅 16:38 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141397">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">✔️
✔️
✔️
منهای ورزش :همراه اول تو جدیدترین شاهکارش، سقف مصرف بسته اینترنت ۷ روزه «نامحدود» شبانه رو از ۱۰۰ گیگ رسونده به ۲۰ گیگ!
✔️
اینترنت نامحدود تو ایران = ۲۰ گیگابایت!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/141397" target="_blank">📅 16:33 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141396">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iwf8cI8aLabU-w2aIpT5FfqEPVnKqsJZlnshGQfkwC0p0NKTZfjmlztq9c9qnaPqgT-vpty2Gb6CuyzkQKAiy39jDkvlhVUQma0-4BOjefcRwnfVukpQaUNSbRVLoUmtB6wzyD4UsSegq5HuZ3vs_yzWgZvuzdTTJz6AZ4CQbuFGEsiYmIuhDuPHXpXV4nY_Grq_vlYvJjqgQjILo080zFOfRFijKl38LkFqPcLh34mU53iUK8j0biIA66nJP1gDZ2csFhmbmWYwt1Suam-f3VXP4BYWcj9tSKEayzG0TD2_XZNeQMORRcik8vK7utcZflLym9_np_Vqyk6NGzpU_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مهدی عبدی در دیدار فردا در ترکیب خیبر مقابل پرسپولیس حضور خواهد داشت/ورزش‌سه
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/141396" target="_blank">📅 16:32 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141395">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🎙
امیر قلعه نویی، سرمربی تیم ملی فوتبال:
◽️
عدم حضور در لیگ‌های معتبر؟ بازیکنانی که در امارات هستند با اسناد نشان می دهیم نسبت به بازی با مصر 25 درصد افت داشتند
◽️
تغییر در همکاران؟ نه چرا باید تغییر کنند؟/ در جلسه هیات رئیسه من 10 دقیقه توضیح دادم و یکی یک…</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/141395" target="_blank">📅 15:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141394">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IBuodz7hzO3XD4aXT2oKzAvAq8U5ovvr0sbo0Qd_qUd5VjstPmV0uNR5TloyHv-cxeCw1gu1-P-8IlOPQ0W-EQFXX11CV19JMajizuWqEbOFBUfh11V4JfGHnDX66hYBmKC_maLqTktD88SQARGDbXTmg5xfAkDcsK-YkCcoF2VHJo6IWHuDC544NJUp-0B2c0xHMvqmJ0RHp3KbcpAqPEyH5cb79NlpF9fx9l_a1120ESdHs6ZzpRAmARa_8QE5XM9fI7ozmdBSSArB18g0Xd_O_dvDh9Wob0vsie6qiUDhRhlZ-wI7U7W339SJ5VBccXfQz5A53e_VtxIIcdebsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دانیال ایری به تمرینات پرسپولیس برگشت.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/141394" target="_blank">📅 15:43 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141393">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
حسین کنعانی در صورتی که فردا بتونه در تمرینات گروهی شرکت کنه مقابل خیبر بازی خواهد کرد اما اگه انفرادی تمرین کنه به بازی روز چهارشنبه نخواهد رسید
✍️
خبرگزاری فارس  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/141393" target="_blank">📅 15:41 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141392">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9wGNy0Ct6K0tsCdOfyBKfbfNS5aM5szU7OVh2Z4PT4l6A-PtUKndHvISgI9yJCc9q5fLzEEm_hVD4h299lU_zx2seFG5pDbd5pmJfeJffOSoaWQK5Bamv6IbHDCDjwqOtMEIdyf9k6huk8Ow5q71B5nEryM9xtJX2h8KSQGDPHlP4sBqnJEwpv8IOGd3V97GJLgFsaA51YXvWZ3kzoK7xapNyVza3ZGtif09INNllcqhrwTtjI6SM9MBSL-VnoNiJKC1TO65C8k2GcymbO_9GgBhIKBpX5rQ9Y2uuWEMRQSHXGcgx7RNmVlBrO2PkejS0hbWQgHmoPSoh1_FSdrvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
برنامه چهار دیدار معوقه هفته هفتم لیگ برتر
❌
پرسپولیس در دیدار معوقه هفته هفتم از ساعت ۱۷ روز چهارشنبه به مصاف خیبر خواهد رفت. پرسپولیس درصورت برد مقابل خیبر، با 19 امتیاز بالاتر از استقلال و تراکتور صدرنشین خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/141392" target="_blank">📅 15:39 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141391">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
رسیدگی به پرونده محرومیت بیرانوند اول آبان در CAS
❌
❌
دادگاه عالی ورزش اول آبان‌ماه با حضور نمایندگان حقوقی علیرضا بیرانوند، پرسپولیس و فدراسیون فوتبال، دفاعیات طرفین درباره حکم محرومیت چهارماهه این دروازه‌بان را بررسی می‌کند. امکان حضور آنلاین نیز برای…</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/141391" target="_blank">📅 14:37 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141390">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
به ادعای خبرگزاری هفت ورزشی مهدی تیکدری از بازی کردن در‌دفاع چپ ناراضی است.
✍️
هفت ورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/141390" target="_blank">📅 11:50 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141389">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb1d8d44f8.mp4?token=Uskyovm29XHiFN4qrlYEo11zuj3DZK5pYQ7fm7i7Yg8JfoNgGuDJSx7_VPpgXT9goXW8M9RltFmJxgrdMt9d3Kdl6OOi8qP3kjxI6eOOZgcYha2qQB6-j-sAXAYgv0FL-OVET2DcwqMOjMOZRcbkmdvlf3wXtK5gXL2lxp5s9kAnILKH4D1nWyW7LHSxiCh4fThlPYddn_nqpXQ9BiDlPITWBDnRLMDBO-RtmvinCNaf1r08IyGO8bpbI-RYBJbTQy9hh-qAyS87JTrAVG8MV06Am87_pdvfGNczzY7A-FzUu4vOQenym4mTaszujAtdDq8zDyAnL2hvvAEwaY9Rxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb1d8d44f8.mp4?token=Uskyovm29XHiFN4qrlYEo11zuj3DZK5pYQ7fm7i7Yg8JfoNgGuDJSx7_VPpgXT9goXW8M9RltFmJxgrdMt9d3Kdl6OOi8qP3kjxI6eOOZgcYha2qQB6-j-sAXAYgv0FL-OVET2DcwqMOjMOZRcbkmdvlf3wXtK5gXL2lxp5s9kAnILKH4D1nWyW7LHSxiCh4fThlPYddn_nqpXQ9BiDlPITWBDnRLMDBO-RtmvinCNaf1r08IyGO8bpbI-RYBJbTQy9hh-qAyS87JTrAVG8MV06Am87_pdvfGNczzY7A-FzUu4vOQenym4mTaszujAtdDq8zDyAnL2hvvAEwaY9Rxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
کلیدواژه همیشگی مصاحبه‌های بیرو
درصد، دلار، ماشین، میلیارد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/141389" target="_blank">📅 10:29 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141388">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
افشاگری میثاقی از نامه وکیل آسانی و فسخ قرارداد با استقلال در تاریخ 14 جولای!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/141388" target="_blank">📅 10:27 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141387">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EJTHIFqqyjMAw922rlZODeOwRNw36ZVfRtqFQEoxevI3-LwzVTZO2O_vn7hQQ2QkDuhZ_NetZKyJaQJlHIwpFAJbWq0_meZKE0EODqnqS_C8kD_DNWeLb1aB1rBUC4x86BZwBHa2ZLqQSRsVLBYCoIPZU-B4QljUNLaXJwcuU_4cjkL_UHna35f2On7Wb6a8zwnKmUcNYM2Whfhk5oG11rO0_MSn98Tb8jwyW-NxpwT-CZOGZ8Nbe8vQEVFRryb6aUxUd_yA1MBnHvr5tdx3L8qqi879uWs6wn0w3LIVsffzvUci7dzsM1taoXnSQ9DY3s7IwjCXYyE6nr-kYnO-xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📘
⭕️
همین یک‌ قاب از تلویزیون و دوخطِ پشت‌سر میثاقی که نوشته « با اثر فوری فسخ کرده است» کافیه برای حقانیت شاکیان و غیرقانونی بودن این آلبانیایی شارلاتان. همین یک صحنه بسه و دیگر هیچ‌!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/141387" target="_blank">📅 10:23 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141386">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
افشاگری میثاقی از نامه وکیل آسانی و فسخ قرارداد با استقلال در تاریخ 14 جولای!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/141386" target="_blank">📅 09:38 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141385">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🎙
امیر قلعه نویی، سرمربی تیم ملی فوتبال:
◽️
عدم حضور در لیگ‌های معتبر؟ بازیکنانی که در امارات هستند با اسناد نشان می دهیم نسبت به بازی با مصر 25 درصد افت داشتند
◽️
تغییر در همکاران؟ نه چرا باید تغییر کنند؟/ در جلسه هیات رئیسه من 10 دقیقه توضیح دادم و یکی یک سوال نکرد .من گفتم توضیح فنی و گزارش را دادم و اگر کاری نیست برویم چون قرار بود تصمیم گیری کنند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/141385" target="_blank">📅 09:35 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141384">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🎥
امیر قلعه نویی، سرمربی تیم ملی فوتبال:
🚨
ماجرای بیرانوند و وساطت برای او در بحث سربازی؟ به هیچ عنوان، وقتی قانونی هست باید یکسان برای همه باشد
❌
بیرانوند باید شرایط قانونی سربازی را انجام دهد
❌
او تمرکز لازم را در این چند وقت نداشته است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/141384" target="_blank">📅 09:30 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141383">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65a8965627.mp4?token=TWZMJ2DbkUu6R0FJoPdXkqH2uvTp80eyUfMTyCQ5oHh4u20WWEaTYxUCEN9s73mmwh0GtUqUPqJKwEGZDB3GPa4VwAeEuaz7EvIOSa37U38mpc0s2JtDyQ5j8unHBs-I8pmuyx3-q17-FE9yvwNzNZcjPkjRAJCNva7Epzj73nrK7ojZp2RlBrgF3tTbej4j1p0TcwU32dtzf6CBQfP-p9l1JNp1tGHL0ymwTotGezO8a6OlgCV9d76RVJS_CsTD_qBXzoijc_lMjAX1DX9mJHvoaatiGZf15F6CbPbTxsRAyksNOIPz-85Jpyvx7fs6XdRpcVimyXCXVqtxC-5qag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65a8965627.mp4?token=TWZMJ2DbkUu6R0FJoPdXkqH2uvTp80eyUfMTyCQ5oHh4u20WWEaTYxUCEN9s73mmwh0GtUqUPqJKwEGZDB3GPa4VwAeEuaz7EvIOSa37U38mpc0s2JtDyQ5j8unHBs-I8pmuyx3-q17-FE9yvwNzNZcjPkjRAJCNva7Epzj73nrK7ojZp2RlBrgF3tTbej4j1p0TcwU32dtzf6CBQfP-p9l1JNp1tGHL0ymwTotGezO8a6OlgCV9d76RVJS_CsTD_qBXzoijc_lMjAX1DX9mJHvoaatiGZf15F6CbPbTxsRAyksNOIPz-85Jpyvx7fs6XdRpcVimyXCXVqtxC-5qag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
امیر قلعه‌نویی: کنعانی زادگان و علیپور؟ کاش تیم پزشکی بود و می گفتند که آنها مصدوم بودند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/141383" target="_blank">📅 09:25 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141382">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e06a6489f2.mp4?token=SCBRZCEcEXosIwh1hWogYdNoYlmYgaKr9BqP97NWkRzO93i4tWtCIQbFxL5N5p7lMmUEM1_qf5wlFV59N3qCd_gGXQQC_Nih1sz9HcjOrbWaypQZ92ROh0XVhIPCTrfPNsgsVif3WcZ5D9mLnHo8eRibFZIKkkbh9cAdimfrwIR20m41zauUBOKEt-bVYaGxXK8C5wqjgdhBTTkBPTZngg62jrVMYGL8tHgMoiPJNmH9Hb9fADaajdJambd9pgaZ1iEOdfNmf-uM_9KdR2rSJjlPrX9eL-a9b_M5-7ETbFv1OTq1_wmZEigj23Z4rHU7YcNzUx2jZ5soH1U1kP1QrRWqHIMvUSiK4oh5sCWnG-Oe9giOG4dab7-q0XQGyaiCii6xunx2NFDUL7-C9rypKRY4yHs_52nKNBuAEqL4ZFGtrOsicpC5Jl-zVbY1I491GOrYMdHSbm9I6T_-OLB6T7bMzy-SoXCmrZswhq4WUpsS8ZA9kUybNncDuStfo6ospNXmXMZfojXXrZ_tsE8bC-Lcg1nxMbGBmBXftXHFOGgtKIp52SMKrwXUMz2Nz4lFQdUyJ74ZT-AF40YGOFPyi-Dl9_t7KUKo1-NiiHCi3VOIpHMgZqX3V2I2zRYYBnJWkw-yiNPoLP1DI2glVt2zrj63QBJu_8_AAetgW1wfzj4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e06a6489f2.mp4?token=SCBRZCEcEXosIwh1hWogYdNoYlmYgaKr9BqP97NWkRzO93i4tWtCIQbFxL5N5p7lMmUEM1_qf5wlFV59N3qCd_gGXQQC_Nih1sz9HcjOrbWaypQZ92ROh0XVhIPCTrfPNsgsVif3WcZ5D9mLnHo8eRibFZIKkkbh9cAdimfrwIR20m41zauUBOKEt-bVYaGxXK8C5wqjgdhBTTkBPTZngg62jrVMYGL8tHgMoiPJNmH9Hb9fADaajdJambd9pgaZ1iEOdfNmf-uM_9KdR2rSJjlPrX9eL-a9b_M5-7ETbFv1OTq1_wmZEigj23Z4rHU7YcNzUx2jZ5soH1U1kP1QrRWqHIMvUSiK4oh5sCWnG-Oe9giOG4dab7-q0XQGyaiCii6xunx2NFDUL7-C9rypKRY4yHs_52nKNBuAEqL4ZFGtrOsicpC5Jl-zVbY1I491GOrYMdHSbm9I6T_-OLB6T7bMzy-SoXCmrZswhq4WUpsS8ZA9kUybNncDuStfo6ospNXmXMZfojXXrZ_tsE8bC-Lcg1nxMbGBmBXftXHFOGgtKIp52SMKrwXUMz2Nz4lFQdUyJ74ZT-AF40YGOFPyi-Dl9_t7KUKo1-NiiHCi3VOIpHMgZqX3V2I2zRYYBnJWkw-yiNPoLP1DI2glVt2zrj63QBJu_8_AAetgW1wfzj4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امیر قلعه‌نویی: در پست خدابنده‌لو، عزت‌اللهی، قربانی، حاجی‌عیدی و نورافکن را داریم و به همین دلیل دعوت نشد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/141382" target="_blank">📅 09:24 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141381">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B0-byZVj11Bu6-CHes9o5GEy1SsXt4cqvOzKRLSriuCjzn77WjkdFFYwaQnp8tfArvRSF9xoy4pWStjsuYZr8scX5B_w20G7z3ERXPnucF8FBUVPLXaWLqg0OkUlJD1P4nJ6iLRJDL2IeZKkr3cTM4LvDhtRM3lcbCrU1dmc5hPk_fOEqab9tepwFkZNbMV44Ken5TJKOZ-HGaNgEq5VmSgOMXduOwdZd40WalQci_KZZseFLSX7LWdyRg9EDxLRjUP0lMRdjSh2tsbgHd89KLTR1cavmGxh9NfleEJiZI0YBW-8YsfIipsDI2ApdDfJSjMYXTOKnpHKcIwyqE-6zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
‼️
به رئیست بگو خر خودتی…دستتون رو شده؛۳۰ مهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/141381" target="_blank">📅 08:25 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141380">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/arqIHsFf4ryrYSQPJtDJ5MotB6bHM5KAtAK6Y4hcztiZikVsotzcX8_MV0XT2jkcc1XG8t3WVxih2VFVVq2qKeu9Sa5h8dQJNxmMHe1WQgNIkKB1K-tqB30RjCsub7jijmAYM8oDEq3SmUQKCLuSOgmf5dSQ334XH0cyhCEwvP4r5uxzHjk07Q2vRSyZCh1pMu5M99MMOsbzDKgTMqlNC4Lk8PnwnjDL2P7ZO0KBYPVOsZvl_dQu1FKwho7uHfSO9jnPIlZKR5o1Ulo-g1je6rt44Si2xEuB-88vC9Ybb_qTmDaY6ip5opVkGeYJaM3hCKQ2M9Sys3crQl4nZqyFAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
فرداشب اروپا در تب‌وتاب شب‌های سرنوشت‌ساز؛ جایی که غفلت، تاوانی به قیمت امتیاز دارد!
🔥
⚽️
فرداشب آرسنال با ضریب ۱.۲۱ و اینتر با ضریب ۱.۲۳ از نگاه ضرایب، مدعیان اصلی پیروزی هستن؛ بارسلونا هم با ضریب ۱.۲۶ شانس بالایی مقابل گالاتاسرای دارد. تقابل اتلتیکو مادرید و منچستریونایتد با ضرایب ۱.۹۱ و ۳.۶۴، از جذاب‌ترین بازی‌های فرداشبه؛ درحالیکه ویارئال و ناپولی با ضرایب نزدیک‌تر، رقابتی متعادل‌تر رو نشون می‌دهد. دیدار لانس و اسپورتینگ هم اختلاف ضرایب چندان زیاد ندارند و همین موضوع، این مسابقه رو به یکی از دیدارهای قابل‌توجه کنداکتور تبدیل خواهد کرد.
📌
مسابقات را فقط تماشا نکن؛ همین حالا وارد مینی‌اپ وینکوبت شو و با اولین شارژ خود و دریافت ۱۰٪ بونوس ویژه این دیدار‌هارو رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/141380" target="_blank">📅 01:08 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141379">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
گویا یحیی گل‌محمدی در یک قدمی سرمربیگری تیم ملی امید قرار گرفته است. فقط کاش یحیای عزیز حواسش باشد همه بازیکنان این تیم باید زیر 23 سال باشند. این دیگر اجباری است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/141379" target="_blank">📅 01:01 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141378">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">⭕️
⭕️
⭕️
هومن هدایتی مشاور حقوقی ورزشی:
⭕️
استقلال تخلف کرده و باید منتظر حکم سنگین باشه   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/141378" target="_blank">📅 00:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141377">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
با توجه به مصدومیت حسین کنعانی و دانیال ایری، زوج خط دفاعی پرسپولیس برابر صنعت نفت آبادان، محمدمهدی زارع و حسین ابرقویی هستند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/141377" target="_blank">📅 00:58 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141376">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
آسانی که مصدوم بود و جای رزاقی نیا اومد تو زمین ...خود آسانی مصدوم شد و از بازی خارج شد
😎
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/141376" target="_blank">📅 23:55 · 20 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
