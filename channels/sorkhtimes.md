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
<img src="https://cdn4.telesco.pe/file/juL6CwcSNZRXMyHzuHQwjjODoRcgp_V-iTa0oOmT2KivM8zFOWZ6c9IF0pHVokfMbrP_oZBKvwxgnEKtpa8Sr51SmLAmuzzCiBlfc2GTWT5gBOQtzF6OHRWX09AhCxwC5zYg8pSZS_WVwJfuBax0sIrcddyiqK_ySSFUeqERiMPttb2HMQ5T6vLgzak1VE-2PmohPbj-J9AWb2NafoGWShs4NWuSPZn9K0oAXxE3MMGVeXOKSDkHX32EL9JTIjUpR5xg62o4bBG3Fo65B1CpnV4OemAVj3msk6TtgGd1oYUHV0T_nPqauIlUsX1aWsGO6nRfoL6fMf_GOu2pd-l_VQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-02 17:59:56</div>
<hr>

<div class="tg-post" id="msg-134153">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
داور فینال جام جهانی قطر
❗️
سیمون مارسینیاک از لهستان داور دیدار ایران و مصر شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 851 · <a href="https://t.me/SorkhTimes/134153" target="_blank">📅 17:41 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134152">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❗️
باشگاه شاید قرارداد میلاد محمدی رو تمدید نکنه.چون قیمتش بالاست ...سر همین داستان دنبال جذب ابوالفضل رزاق پوره///قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/SorkhTimes/134152" target="_blank">📅 16:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134151">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❌
باشگاه تمایل به فسخ قرارداد و قطع همکاری با اوسمار ویرا دارد.
🔴
🔴
به گزارش خبرنگار قرمزآنلاین، قرار بود اوسمار ویرا در باشگاه حضور پیدا کند، اما هنوز این اتفاق نیفتاده است.گویا مدیران باشگاه هم تصمیم داشتند جلسه ای را برگزار کنند که این نشست به ساعات دیگری…</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/SorkhTimes/134151" target="_blank">📅 16:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134150">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
ورزش‌سه:
🔴
اوسمار ویرا از پرسپولیس جدا شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/SorkhTimes/134150" target="_blank">📅 16:36 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134149">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PhOGzOvS4cQV7WCi4kRLkV4K8S_8_8IJV64p7EhUdVzCkvMwJ8c5vtVasPdMQZxcEOWQropEGn7oLe6prGb410kPxvZVaMa6SBthvBSmRVv30M97vSj8rPSKjNKs00aUPK86O1Sl8hSYKqET9-fyeNO7Obya2njzlRXtTzZzJ_h0jGYV4WJvujDHMHemSwVVbUvnC_AshBabOEfw9v9vTP6Pl6W8pq9XZ0VdqZ5nVhc9a_uKcI7Q4sxW4U-Oyn3NhGnmn7EOOrIpNneWdSkKuSFzF3okgKNrzzsKhyhXpqk3swtJKWrOGI8diqKLVsp5kd7FjktpdUPYzId5pMdMTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
داور فینال جام جهانی قطر
❗️
سیمون مارسینیاک از لهستان داور دیدار ایران و مصر شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/SorkhTimes/134149" target="_blank">📅 16:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134148">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2dW-s3O6ZfxVIA2Y9BNxdXUAQOGeNEQe3GNxoraWdMnJ8LV8_ImFmWlFK5gV4Dj4yf2oJyLnD8xP-44lad2FVFhnCX0J-GowV7YDmzuOGg8pff_e6P7WU4Vvubp1Q-kMApJLOeanOhbM3o2cwTEeCSkfx2hjW1UARsETZLD3Mww8DnTDz9LxkcWM_538YxbXXipfkZUfF5PwKFIL4UottI6333ZTeadvd_TQbsC8ApELb_HiinG2zq-O1dHK3tCaO7ORWrIadbyzz0acu8PMg2iAUrg8yvAV0IGFw0SItOVKcTXB72cud_SFR1EhQt02FUX4dyX-U5dt276_wdbPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
رده‌بندی تیم‌های لیگ ملت‌های والیبال 2026 در پایان هفته نخست
🔴
ایران در رتبه پانزدهم جدول
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/SorkhTimes/134148" target="_blank">📅 16:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134147">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRNiQB5bad-Jl7XN1f1PZCiuG6YBDk0Fklk2MMr3pz7QyTonbM3gr4m1HCtmv5kWZZ_52voC_vlPhwB4nfi0pBS2DScfSxV3dPgzdLUg0ZIkfajWlj42rEIsdBKXuQw_BnNIYEPiZsjoOp55z_NVZJ4Agpe_3pxrPDkspJId9WU107gzeT9F6KXuJfMHjbH7zgwoCpZS9qvDN6eRTeATD26DQFDJ00HMF-nWg_gFzu3P4BN3kuG7StL0Mls3pH7fhJM1Ms2L8sbpIYNRhgGabPyBWqBqlBrJ-IBJ38zSy0dhgnjvatJMn-MxSCAzPPk2SBynk9u2sx4ZM_mpLNg-JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
درصورت جدایی اوسمار، کریم باقری با توجه به این که اسکوچیج بارها از او تمجید کرده است، ماندنی خواهد بود.
✍️
ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/SorkhTimes/134147" target="_blank">📅 16:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134146">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d841d0291.mp4?token=VQ5tjXT-lPKYMk2B4DAmAsvDTzt2MxxrXff4efAzBM4akOxDfmjHNQtD3jDaTW5-kj8NAyQ25HpGolX9kmuZvv8wUPS6DY-XcR29Ce7AqbgcggnletdrcTOfUp3DOyaoGFFmDfBBTU0TTbV8bZE_lXCqdADtEExAvDwnL9C-tlENBe7Fa4p1EYnIrehWv0hSRrQ27fGMoicnp01aKK6vpUjZTr14TpEqf8aEAK6FDTVQHBntF4mnXBZk9RrBIJgbpB6N7uGAhO12O6XFKVRyGsYwFVOMi6PlyuZDM-D9fPAe08xkf3zh1FmBC_ApT5AJEQqA87WAzaL0lmG2ngX8jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d841d0291.mp4?token=VQ5tjXT-lPKYMk2B4DAmAsvDTzt2MxxrXff4efAzBM4akOxDfmjHNQtD3jDaTW5-kj8NAyQ25HpGolX9kmuZvv8wUPS6DY-XcR29Ce7AqbgcggnletdrcTOfUp3DOyaoGFFmDfBBTU0TTbV8bZE_lXCqdADtEExAvDwnL9C-tlENBe7Fa4p1EYnIrehWv0hSRrQ27fGMoicnp01aKK6vpUjZTr14TpEqf8aEAK6FDTVQHBntF4mnXBZk9RrBIJgbpB6N7uGAhO12O6XFKVRyGsYwFVOMi6PlyuZDM-D9fPAe08xkf3zh1FmBC_ApT5AJEQqA87WAzaL0lmG2ngX8jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
محمدرضا اخباری
: کارهای انتقالم به پرسپولیس تمام شده بود اما در نهایت آقای تارتار با جدایی‌ام مخالفت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/SorkhTimes/134146" target="_blank">📅 16:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134145">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❌
#فوووووووووووووری
🔴
با اعلام رسمی پایان فصل؛ قرارداد امید عالیشاه با پرسپولیس یک فصل دیگر به طور خودکار تمدید شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/SorkhTimes/134145" target="_blank">📅 16:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134144">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❗️
مسن ترین بازیکنان حال حاضر پرسپولیس:
🔴
عالیشاه(34)
🔴
پورعلی گنجی(34)
🔴
بیفوما(34)
🔴
سرگیف(33)
🔴
کنعانی(32)
🔴
محمدی(32)
🔴
باکیچ(32)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/SorkhTimes/134144" target="_blank">📅 16:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134143">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
مذاکرات پرسپولیس با اسکوچیچ مثبت شد
🔴
مذاکرات پرسپولیس با اسکوچیچ داره بهتر می‌شه. اسکوچیچ که سر بند فورس ماژور جنگ و مدت قرارداد بحث داشت، ظاهراً با باشگاه به تفاهم رسیده و فرداست که همه چیز نهایی بشه.
🔴
اوسمار هم که قبلاً می‌گفت می‌تونه برای بند تمدید…</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/SorkhTimes/134143" target="_blank">📅 15:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134142">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❗️
❗️
#منهای_ورزش
✅
اختلال گسترده در خدمات بانکی؛ بانک صادرات، ملی، ملت، تجارت و کشاورزی باز هم قطع شدند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/SorkhTimes/134142" target="_blank">📅 15:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134141">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❗️
خبرنگار الجزیره: ظهر امروز به وقت محلی قرار است مراسم نمادین امضا و مبادله متن توافق مرحله اول میان دو هیات ایران و آمریکا برگزار شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/SorkhTimes/134141" target="_blank">📅 15:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134140">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❌
❌
واکنش باشگاه چادرملو به برگزاری پلی‌آف آسیایی؛ بازی را عقب بیاندازید.
✅
ما هفته گذشته فراخوان دادیم، اما بازیکنان مطمئن نبودند که این بازی واقعاً برگزار می‌شود یا نه و اصلاً فرصتی برای آماده‌سازی وجود نداشت. قرار بود بازیکنان پس از مراسم عزاداری امام حسین…</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SorkhTimes/134140" target="_blank">📅 15:06 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134139">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYGpHLZ2zlMTaMIKHtHUpf4mJ1PPiplAp1I6hG2n8AC0UOjqQz1Wy8qvq4JsjlkvNBkNmziwqKdYUMk3iPOw9JY-vp9cIPGoPDcK3k0rIOchc4k21iHlihTWaE8343v6Nc1OE4fJ6tbtHM0_MQHqNyBU7dfmDvD9lA8zHM4Opu_3tMTKl1sg08NsW_N1Vb_W6JDisE93DgYdTd7uulEDGRAYDnAegOyYSC6zqvoWNbzhIQkIkrbwatACOo3a2w_hHpn8QEb7nj-wPq-NsNZteV4KZVprRCqREiVmoAgFW51DrhNuZFYaceyuwx4r2DlZFYTPRyYIsudb1IvNkA74TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📱
توئیت کاربر بلژیکی با نزدیک دو میلیون بازدید:
🔴
ما نتونستیم ایرانو شکست بدیم اما حداقل (مثل دولت آمریکا) ۳۰۰ میلیارد دلار هزینه نکردیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/SorkhTimes/134139" target="_blank">📅 15:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134138">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">⚠️
پوفیوزا
بزارید طرف بیاد بعد بگید لیست داده
🤣
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/SorkhTimes/134138" target="_blank">📅 14:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134137">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UpBmV0lDgzWQzmEyZuEA_sf3SLdSiCLDBE8T5xl6qS_dzIp52C89nM2QyeY7L5CBrvYh42HT3gBruYHGUBHlK-A23JDUdUnJ0BpjpGjkMmIFpadXxS6E34wEkOcdQItTQ4L2aeVvrSALYLnveQZwQGk1DDo9lhnqDc5w3fNx_7iSklL2dX56L7N9uU0cNvVcMi3jqak-Bvc0xY-ABqW0VW0YnEozYHz6IuS0eXkhHI9e874lONk67PTr81L82thpkV6GVXrYYrYk-GSB3q0hxrMg8_FNct5CNlYhq6kUPJ6HRJr8ydENZcJr1MvbuyLpdb7YM6yPLXNwe-QPCuf3Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚽️
اوج
هیجان مسابقات جام‌جهانی ۲۰۲۶ فقط با
اسپورت نود
⚽️
گروه K جام‌جهانی ۲۰۲۶
[
پرتغال
🇵🇹
🆚
🇺🇿
ازبکستان
]
⏰
سه‌شنبه ساعت ۲۰:۳۰
🏟
استادیوم
ان‌آرجی
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
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SorkhTimes/134137" target="_blank">📅 14:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134136">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❌
❌
اختلال هر ۴ بانک که مورد حمله سایبری قرار گرفته بودند، رفع شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SorkhTimes/134136" target="_blank">📅 14:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134135">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
علیرضا بابایی مدیرعامل چادرملو اردکان:
🔴
با وجود مخالفت سعید اخباری سرمربی تیم و اعضای کادرفنی به خاطر آنکه احتمال مصدومیت بازیکنان ما وجود دارد، در احترام به تصمیم هیات رئیسه فدراسیون فوتبال، کادرفنی درخواست مدیریت باشگاه را تمکین کرد و برابر پرسپولیس بازی…</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SorkhTimes/134135" target="_blank">📅 14:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134134">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❌
چادرملو هنوز تمرینات خود را شروع نکرده و تمایلی به حضور در مسابقه مقابل پرسپولیس ندارد.   احتمال انصراف این تیم از بازی مقابل پرسپولیس دور از ذهن نیست. / فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/134134" target="_blank">📅 13:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134133">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gOWQe3WGYJLW5XigkT_WNR5mce_kvzPX8h6gwR-LUF2NpoQoRNzzovY5mT025jC2pIRdiTyJi8Lu_HFROxG0S7YrUYQp6NPjnS01DpfKYzysBLiX7KSKNOwjghYuFEuQeIPzYaHTdoLcH33qdgm81tRpg4eweiOCP_BwO-xm3d22wku5rpborT0RgpXDcaNmmKebgnhBAOn3dUrVZt0R5WgzHw-z4-Ionm2NxGpEKTgK-L7bRWNkxuk9LeIwo4ol7oFv-Iiu6PdyDz_m9fMF8R7L05SpzLPVEF5GS3t4HIpwt3UKEMQ9Xps0ugzx4j-5-Mrm4sklS3BYdk0ex-rPEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ورزش‌سه:
🔴
اوسمار ویرا از پرسپولیس جدا شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SorkhTimes/134133" target="_blank">📅 13:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134132">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✅
🚨
اوسمار گفته اگه قراره فصل آینده سرمربی نباشم تورنمنت سه جانبه رو هم نیستم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SorkhTimes/134132" target="_blank">📅 11:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134131">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❗️
طی ۲۴ ساعت آینده جدایی اوسمار ویرا از پرسپولیس به صورت رسمی اعلام خواهد شد.
🔴
بدین ترتیب و در صورت برگزاری مسابقات پلی‌آف احتمالا کریم باقری به صورت موقت هدایت پرسپولیس را بر عهده خواهد داشت. البته هنوز احتمال حضور اوسمار در پرسپولیس در این تورنمنت وجود…</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SorkhTimes/134131" target="_blank">📅 11:19 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134130">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❌
سازمان لیگ : بازی پرسپولیس و چادرملو ۵ تیر ماه در ورزشگاه پاس قوامین یا شهر قدس برگزار خواهد شد
👀
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SorkhTimes/134130" target="_blank">📅 11:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134129">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
انتظار می‌رود تا ساعاتی دیگر، خبر رسمی جدایی اوسمار ویرا از پرسپولیس و انتخاب دراگان اسکوچیچ به عنوان جانشین او منتشر شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SorkhTimes/134129" target="_blank">📅 11:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134128">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
انتظار می‌رود تا ساعاتی دیگر، خبر رسمی جدایی اوسمار ویرا از پرسپولیس و انتخاب دراگان اسکوچیچ به عنوان جانشین او منتشر شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SorkhTimes/134128" target="_blank">📅 11:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134127">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❌
یه مشکل از دو تا اختلاف پرسپولیس با اسکوچیچ حل شد
🔴
مدت قرارداد که اسکوچیچ می‌خواست دوساله باشه ولی پرسپولیس می‌گفت یه ساله، حل شد و رسیدن به یه توافق وسط: یک+یک ساله
🔴
اما هنوز یه گره باز مونده: بند فورس ماژور. اسکوچیچ می‌گه اگه این بند فعال بشه، باید کل…</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SorkhTimes/134127" target="_blank">📅 11:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134126">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">✅
فارس: چادرملو در بازی پلی آف شرکت نمیکنه و پرسپولیس مستقیم راهی فینال میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SorkhTimes/134126" target="_blank">📅 11:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134125">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❗️
اعلام زمان و محل برگزاری دیدار چادرملو و پرسپولیس
✅
طبق مصوبه هیات رئیسه فدراسیون فوتبال مقرر شد برای تعیین نماینده سوم کشورمان در لیگ قهرمانان سطح دو آسیا دو مسابقه پلی آف برگزار شود.
❌
بر این اساس در دیدار اول روز جمعه ۵ تیر ۱۴۰۵ ساعت ۱۸:۴۵ در ورزشگاه…</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SorkhTimes/134125" target="_blank">📅 11:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134124">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">✅
✅
تایید شد
🚨
میثاقی: پرسپولیس 5 تیر به مصاف چادرملو خواهد رفت و برنده این بازی 9 تیر با گل گهر مسابقه خواهد داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SorkhTimes/134124" target="_blank">📅 11:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134123">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
مذاکرات پرسپولیس با اسکوچیچ مثبت شد
🔴
مذاکرات پرسپولیس با اسکوچیچ داره بهتر می‌شه. اسکوچیچ که سر بند فورس ماژور جنگ و مدت قرارداد بحث داشت، ظاهراً با باشگاه به تفاهم رسیده و فرداست که همه چیز نهایی بشه.
🔴
اوسمار هم که قبلاً می‌گفت می‌تونه برای بند تمدید…</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SorkhTimes/134123" target="_blank">📅 09:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134122">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">#تکمیلی
🚨
🇮🇷
صبح روز دوشنبه اسکوچیچ به باشگاه از طریق ایجنتش پیغام داده که روی پیشنهاد آخر باشگاه فکر میکنه و ظرف ۲۴ الی ۴۸ ساعت آینده خبر میده!
🔴
مدیران باشگاه و بانک شهر درخصوص خاسته اسکوچیچ درباره نقل و انتقالات موافقت کردن و همچنین درباره مدت قرارداد امروز…</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SorkhTimes/134122" target="_blank">📅 09:47 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134121">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✅
استوری معنی‌دار اوسمار: خدا همیشه خوب است. متعهد بودن، حرفه‌ای بودن، با دیگران مهربان بودن و قابل اعتماد بودن یک انتخاب نیست، اصول شخصیت انسان است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SorkhTimes/134121" target="_blank">📅 09:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134120">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🚩سرخ تایمز🚩</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AA25rVNwOAKG29DKCALqBuJT-e5km_uTnKMcox-w7ZzILmoYlG0Dtn46OIsd3IlGO_03u4JOM4xNc76ghKoAtaq5IYAXPfVl9Ag8Q5NP5cofInPIlfC5iGo7M7IXuTcw13COo2ExXu8aEcP90dQCb0p0nwBX8FO8hj2JTKWAj-gVh_TyrM3DBhdTA50uKg8ObVw62-7ObOVdvZEnbnSDZVEc646IyNyoVcepUY0ehCk1uYuQIZQ45jqP4l3mGOlXIAErGXEMAq8FnnqnAI1f_otZNfjBuNzrysToYGWgi92b1xwo72t6yffHxWaI-eHx01_MbMfkuEdzEIoWOEzrfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚽️
اوج
هیجان مسابقات جام‌جهانی ۲۰۲۶ فقط با
اسپورت نود
⚽️
گروه I جام‌جهانی ۲۰۲۶
[
سنگال
🇸🇳
🆚
🇳🇴
نروژ
]
⏰
بامداد سه‌شنبه ساعت ۰۳:۳۰
🏟
استادیوم
مت‌لایف
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
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/SorkhTimes/134120" target="_blank">📅 05:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134119">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #تکمیلی
🤫
🏅
حدادی و اسکوچیچ سر عدد ۱.۳ میلیون دلار برای ۱ فصل به توافق رسیده بودند؛اما اسکوچیچ خواهان قراردادی دو ساله بود و میخاست بندی داخل قراردادش قرار بگیره که در صورت جنگ کل مبلغ دو فصلش رو دریافت بکنه،از اون طرف مدیران باشگاه میگفتن…</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SorkhTimes/134119" target="_blank">📅 02:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134116">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
منزل بیفوما و دنیل گرا پس گرفته شد  مذاکره برای فسخ دو خارجی پرسپولیس
🔴
فرهیختگان: باشگاه پرسپولیس به دو بازیکن خارجی تیمش اعلام کرده که اجازه ورود به آپارتمان خود را ندارند چرا که دوران حضورشان در این تیم به پایان رسیده است.
🔴
تیوی بیفوما و دنیل گرا هر…</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/134116" target="_blank">📅 02:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134115">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rdWgUSomRblrbiHQu5OpqIMyBP6HjTd3xHmcIJvWFFw61daikTyH4N63e65hU8bHQ-SDYBcrlz0CYSQSVSCur7fv3EpuMySh0vPRp9utq542gVBz9Jn7Qe4rZlsLhV_o6PfKRgkWtHYisaWFGJNfHHfwsxEy-0xGBB0Bhx2yuuJxk5DDa8lNSx4JsLbO4_vblR35WlvjVVlfaVVNdulyKRtcF03fJOXim3YEyM4SBPC4Ra27-eQsriHeE7RfY7Upru0NRBJ_me4sbmwqIBxJMyP-VOtXJ3HgMArnPIlGw2DmVEW3-YMWT-S3d-gJxbEJz6OA8NPc73xUJ_FEEDci7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚽️
اوج
هیجان مسابقات جام‌جهانی ۲۰۲۶ فقط با
اسپورت نود
⚽️
گروه I جام‌جهانی ۲۰۲۶
[
سنگال
🇸🇳
🆚
🇳🇴
نروژ
]
⏰
بامداد سه‌شنبه ساعت ۰۳:۳۰
🏟
استادیوم
مت‌لایف
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
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/134115" target="_blank">📅 01:14 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134114">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPulseGate</strong></div>
<div class="tg-text">🔰
سرویس اقتصادی
🔰
یک ماهه
25 گیگ 220T کاربر نامحدود
30 گیگ 280T کاربر نامحدود
35 گیگ 320T کاربر نامحدود
55 گیگ 420T کاربر نامحدود
100 گیگ 600T کاربر نامحدود
دوماهه
50 گیگ
380T تومن کاربر نامحدود
70 گیگ 450T تومن کاربر نامحدود
150 گیگ 700T تومن کاربر نامحدود
200 گیگ 750T تومن کاربر نامحدود
سه ماهه:
120 گیگ 680T تومن کاربر نامحدود
160 گیگ 730T تومن کاربر نامحدود
230 گیگ 800T تومن کاربر نامحدود
320 گیگ 950T تومن کاربر نامحدود
400 گیگ 1.1T تومن کاربر نامحدود
🛜
مناسب برای تمام سایت ها و اپ ها ،ظرفیت اتصال نامحدود
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/SorkhTimes/134114" target="_blank">📅 00:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134113">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dee5f09984.mp4?token=ePVxXXXyR_CQyaYEpKvYlQuITrJjY_ukcdrWKucVox9SrIQHn22KVKp4M2AohoibcEo9BxtZAMaYBw9SaZLpewfBGQfP1bhnN-kk2dsMKjA25zw-UAposckAjAPs9_eqbM4qjgSG4dAO7-rakIDdCyYWd0U3sb2aSi8MWQWAC4OQqeQUQ8Oqb1HLBsJVyWG51o3RIPBkp1BJKnIlESR3xkGl7HDSk8vDts1VsECJEWxt9nCobKibVG1RJog7JvVLK36s0JUrCk36VYc5ZdX9HpydZBZXVXIS-S8gxIl8-TfvyZNABuuTsam6PGHjgHItNPVYAiwwETbdFFv0DbUmCTOyaGoWMxN4OZVtniASZu82PSZpUroFhDhs9YFnz7__F_0c2FTdlfQGtszHOQcESUrZ0ugQb26A-pO82FzGoFiosEe4KdH6OdMMpAImPxzobwtiuO30HXKp4xaBVB-ci-JJOAS1RKS9vBL_6ZZKcIGPWikYVXQwUk2yeCETcbHv_EI-kBliHzyf3ofHUalKc1_qHILMnJrcYXUmiXQKSehejP3FDNUZlo-mAaeu1jTvHG8okxiPWXAZd2Q5vFL1mLTXicbzLDc91ML3WIGdUHCjRWwV97ca3bNeH9HBm_3gMkZjKFVwDoHQ2Zo2WfT7c-YYSgnNWLgHAFEjFk1bTHk" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dee5f09984.mp4?token=ePVxXXXyR_CQyaYEpKvYlQuITrJjY_ukcdrWKucVox9SrIQHn22KVKp4M2AohoibcEo9BxtZAMaYBw9SaZLpewfBGQfP1bhnN-kk2dsMKjA25zw-UAposckAjAPs9_eqbM4qjgSG4dAO7-rakIDdCyYWd0U3sb2aSi8MWQWAC4OQqeQUQ8Oqb1HLBsJVyWG51o3RIPBkp1BJKnIlESR3xkGl7HDSk8vDts1VsECJEWxt9nCobKibVG1RJog7JvVLK36s0JUrCk36VYc5ZdX9HpydZBZXVXIS-S8gxIl8-TfvyZNABuuTsam6PGHjgHItNPVYAiwwETbdFFv0DbUmCTOyaGoWMxN4OZVtniASZu82PSZpUroFhDhs9YFnz7__F_0c2FTdlfQGtszHOQcESUrZ0ugQb26A-pO82FzGoFiosEe4KdH6OdMMpAImPxzobwtiuO30HXKp4xaBVB-ci-JJOAS1RKS9vBL_6ZZKcIGPWikYVXQwUk2yeCETcbHv_EI-kBliHzyf3ofHUalKc1_qHILMnJrcYXUmiXQKSehejP3FDNUZlo-mAaeu1jTvHG8okxiPWXAZd2Q5vFL1mLTXicbzLDc91ML3WIGdUHCjRWwV97ca3bNeH9HBm_3gMkZjKFVwDoHQ2Zo2WfT7c-YYSgnNWLgHAFEjFk1bTHk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
بیرانوند: مهدی طارمی قبل از بازی یک سخنرانی حماسی کرد و به بازیکنان گفت اگر سر خود را در مقابل بازیکنان بلژیک پایین بندازید، بلژیکی‌ها ما را له می‌کنند و آبروی ما را می‌برند و باید در تمام لحظات سر خود را بالا بگیرید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/134113" target="_blank">📅 00:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134112">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d02fae5a3c.mp4?token=q64IR8SZwfjDUz6uyRMzN0XhZyAWLjmUKJrQGVF9QIRccsUh2O2S_I345ksgmjDx8JsiOhUx2dJOeAJpstmqGeFvWMK0ARdbLCUJD3QcnrTBZvoGZWPg436-veTG28ZuVhGC_YoR8R60eEibE43u_8WEYaa1o6mDYTiDEvhgMlgeY7l4X2j5YmCqlQzkrJR917WauULzhqCIMXT0P_v5Dy279adh8d-cfrOFNP5jSwPorNH2K6h0ut0Va59jB547ZFlX0BHOh9saq-umzcpuTHlnco8Ho1md6Wf8cq7YAm8Bpd-aHUM857NIRvmqm-BI0i0RcBQfFlw3naPw1Ey4-g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d02fae5a3c.mp4?token=q64IR8SZwfjDUz6uyRMzN0XhZyAWLjmUKJrQGVF9QIRccsUh2O2S_I345ksgmjDx8JsiOhUx2dJOeAJpstmqGeFvWMK0ARdbLCUJD3QcnrTBZvoGZWPg436-veTG28ZuVhGC_YoR8R60eEibE43u_8WEYaa1o6mDYTiDEvhgMlgeY7l4X2j5YmCqlQzkrJR917WauULzhqCIMXT0P_v5Dy279adh8d-cfrOFNP5jSwPorNH2K6h0ut0Va59jB547ZFlX0BHOh9saq-umzcpuTHlnco8Ho1md6Wf8cq7YAm8Bpd-aHUM857NIRvmqm-BI0i0RcBQfFlw3naPw1Ey4-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
علیرضا بیرانوند: مردم ما ۴ ماه سخت را سپری کردند و همه تلاش خود را کردیم تا دل آن‌ها را شاد کنیم و شرمنده آن‌ها نشویم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/134112" target="_blank">📅 00:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134111">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">✅
باشگاه گل گهر سیرجان به صورت رسمی از شرکت در تورنمنت آسیایی انصراف داد
❗️
بیانیه جدید باشگاه گل گهر سیرجان: ما در هیچ تورنمنتی که خارج از چارچوب مصوبات رسمی فوتبال کشور تعریف شده باشد شرکت نمی‌کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/134111" target="_blank">📅 00:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134110">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ay4dT25um9pLhxgs_dYXKm09wwjyDpzk5gP2sBVh6iEGbHuvH_EE4a-R1kFxHRgeWYWeTGpR_J0b9vw6L6bIv-ZZSMmWRfpWOEjWgfm8UXRyhADEo15nuXRXD7C0AIfyCTyRxR-Fx5CPjzYWEJ0Rpaw9bDvR4-GSObCQnZu6e28YpsP4tjMT4gJZUhOKsCOI2GXA2n8AeSjpm5sZzefzwAv42uVEay0r_HXzET1X1ixEzsmuV2PmVjUagQBUpUObistPsIIKPdFmzfgv8VqmuZHz9DwK1TeOMww2OXM3yJRnYZXUnmIGxWbIahM1-ZjHqDyBfw1rVi8ocN9FEqambA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تیمهای صعود کننده به دور حذفی جام‌جهانی تا این لحظه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/134110" target="_blank">📅 22:43 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134109">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">✅
امین حزباوی، مهدی تیکدری، آریا یوسفی، کسری طاهری و مهدی لیموچی بازیکنانی هستند که پرسولیس با چراغ سبز اسکوچیچ به سراغشون رفته////فوتبال 360
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/134109" target="_blank">📅 22:36 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134108">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dDmombcyt9K8TAL0P6R9LCp9JTeKpGisTxsJa8JUiW-6Cqr6JKdzlntXXEkrjlCaCyMKMvqVFJ5X-eXqAYLhz8EQ3tNmDBMOi3BCmlddtJe0oPQfxqP3B0WqEDIAA-5EaI0h36Kwic5FodgzWciEA99XzE0bzj6K02dMLxbWTehKEBk6H4SPUEn21od78XbJ_hEy7Btm9mHqvnhCkxWTzs_GR-tnYDVtnK5dXktO6jy42nUvbP-SUp1y5kGhCLNKP5r0sOxcQMRjZX9zt3LKloPKyKvCvYqHr55g1bf3nGKN9y7Ywg7zing8HSdAUWCDdCzxUPDq5Q5dgeUi-FwBzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مثل اینکه یکی از بندای توافق ایران و آمریکا نشون دادن لب گرفتن تماشاگرا وسط بازی بوده،
🔴
امشب برای دومین بار شبکه سه لب گرفتن تماشاچیارو نشون داد:
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/134108" target="_blank">📅 22:27 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134107">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🇮🇷
بیانیه باشگاه پرسپولیس در خصوص تصمیم عادلانه فدراسیون فوتبال و سازمان لیگ
🔴
باشگاه پرسپولیس در بیانیه‌ای ضمن تقدیر از فدراسیون فوتبال و سازمان لیگ، تصمیم برای برگزاری دو مسابقه به منظور تعیین نماینده سوم ایران در رقابت‌های آسیایی را اقدامی عادلانه و در…</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/134107" target="_blank">📅 22:10 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134106">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🇮🇷
بیانیه باشگاه پرسپولیس در خصوص تصمیم عادلانه فدراسیون فوتبال و سازمان لیگ
🔴
باشگاه پرسپولیس در بیانیه‌ای ضمن تقدیر از فدراسیون فوتبال و سازمان لیگ، تصمیم برای برگزاری دو مسابقه به منظور تعیین نماینده سوم ایران در رقابت‌های آسیایی را اقدامی عادلانه و در راستای تحقق عدالت فوتبالی دانست و تأکید کرد که «حق باشگاه‌ها باید در زمین مسابقه مشخص شود.»
🔴
در بخشی از این بیانیه آمده است: «بسیار خرسندیم که تصمیمی درست، ورزشی و منطبق با عدالت اتخاذ شد تا سرنوشت سهمیه آسیایی در مستطیل سبز رقم بخورد. امیدواریم تیم‌های حاضر در این دو دیدار با ارائه مسابقاتی جذاب و جوانمردانه، نمایندگان شایسته‌ای برای فوتبال ایران در آسیا باشند.»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/134106" target="_blank">📅 22:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134105">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❌
مدیران باشگاه پرسپولیس برای توافق با بیفوما برای جدایی کار بسیار سختی دارند! / فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/134105" target="_blank">📅 20:54 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134104">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❗️
پایان کار میلاد محمدی در پرسپولیس؟
✅
طبق شنیده‌ها، قرارداد میلاد محمدی با پرسپولیس به پایان رسیده و باشگاه هم فعلاً برنامه‌ای برای تمدید ندارد. از طرفی، خود این بازیکن هم احتمالاً قصد دارد دوباره لژیونر شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و…</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/134104" target="_blank">📅 20:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134103">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❗️
باشگاه شاید قرارداد میلاد محمدی رو تمدید نکنه.چون قیمتش بالاست ...سر همین داستان دنبال جذب ابوالفضل رزاق پوره///قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/134103" target="_blank">📅 20:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134102">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_6214Tgn5g18Ff1q6JGrP9dF1iVaIMrEGpGxOl6-O2lMwCaH_SjsjfJjidkiwfLmws8mVAOSPGPhEGntGAbGKeYC6723x2X2FAOdOvx8HNfDec8vxxUCvX7tDGmCQSFit-vTjgIu55vsmSRF-V5ucbQ-Q39O6gFV-eUsqDHBZlFS0PTDOMKSpBhw2A3vRl-g4q6q7ss3XEWGw7xff83LLLsyQM8rdNs6MjzSKqkH1l6jlO4NEM2tJnhqHTyqAeLS2bfudDoC0QxDkDoHZjkoXxo7vfrbDwQZJjhwTz23d-96pfNEUWKTg8GuGm5_yN9KGAimY6R2zH3VShNvsZpOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
بازی‌های جذاب و هیجان‌انگیز امشب جام‌جهانی رو با بونوس ویژه وینکوبت پیش‌بینی کن.
🎁
تنها چندساعت تا بونوس ویژه جام‌جهانی
6⃣
2⃣
0⃣
2⃣
همراه با وینکوبت باقی مانده!
🎁
🔣
5⃣
1⃣
بونوس ویژه روی تمامی واریزها فقط با یک گردش روی حداقل ضریب ۱.۸ به موجودی خودت اضافه کن.
⏰
این بونوس ویژه وینکوبت فقط تا امشب ساعت ۲۱:۳۰ فعال است.
📌
همین حالا وارد ربات وینکوبت شو و ازین بونوس ویژه استفاده کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/134102" target="_blank">📅 20:48 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134101">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">⭕️
🇮🇷
اگر سازمان لیگ با تأیید و مصوبه هیئت‌رئیسه، سازوکار تعیین نماینده سوم ایران در آسیا را از طریق تورنمنت سه‌جانبه تصویب کرده، سؤال ساده است؛ چرا هنوز نامه رسمی این تصمیم به AFC ارسال نشده است؟
❌
وظیفه دبیرکل فدراسیون، اجرای مصوبات و پیگیری امور اداری است،…</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SorkhTimes/134101" target="_blank">📅 20:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134100">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/brVGrs7cKapy31KhrcpyGttqSTYaU0WcMvpJMZN6pgv4tNkQnKb8OOiYd37LryYf6PBCHNOxdn8kMqSffVfnJkXsnzUNIRrirCc8J_hlQnRj7DwF4xMLSa5K8w5gMtXUYH4XlviitXgEhvHsvUGKHNbWIBQOEonjSBuZwRNAPfaWouEe1eZ70-YEjyyJB_D1110XeazYwaK4a575y1_UL1NKXCYDCwkgLLazekNHUvRpMx-3BRtobnNKImCj3qiRL9U6qLbN14yXIVBV1VsXyKsitcfCYCBhpku2NTJ0VcxOSO1r-vFH5Gw96eyM8jkHpDjA44n-ecTSd4qsf09gHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
🇮🇷
اگر سازمان لیگ با تأیید و مصوبه هیئت‌رئیسه، سازوکار تعیین نماینده سوم ایران در آسیا را از طریق تورنمنت سه‌جانبه تصویب کرده، سؤال ساده است؛ چرا هنوز نامه رسمی این تصمیم به AFC ارسال نشده است؟
❌
وظیفه دبیرکل فدراسیون
، اجرای مصوبات و پیگیری امور اداری است، نه معطل گذاشتن آنها. هر ساعت تأخیر در ارسال این نامه،
ابهام بیشتری درباره سرنوشت سهمیه ایران ایجاد می‌کند
و حق سه باشگاهی را که باید در این رقابت شرکت کنند، تحت‌الشعاع قرار می‌دهد.
❌
آقای هدایت ممبینی
، اگر مانع قانونی یا اداری وجود دارد، آن را شفاف اعلام کنید. اگر مانعی نیست،
چرا مصوبه هیئت‌رئیسه هنوز روی میز مانده و به AFC ابلاغ نشده است؟
فوتبال ایران بیش از هر زمان دیگری به شفافیت، پاسخگویی و اجرای دقیق مصوبات نیاز دارد، نه سکوت و تعلل.
❓
هواداران و افکار عمومی منتظر پاسخ روشن هستند؛ اجرای مصوبه نباید قربانی ابهام یا تأخیر شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/134100" target="_blank">📅 20:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134098">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❗️
با تصویب هیات رئیسه فدراسیون فوتبال بیست و پنجمین دوره لیگ برتر ( فصل ۱۴۰۵-۱۴۰۴ ) به دلیل حمله وحشیانه دشمن به کشورمان به صورت نیمه تمام باقی می ماند و جدول لیگ نیز با شرایط فعلی متوقف می گردد.
🔴
ضمن اینکه براساس این جدول ۳ نماینده فوتبال کشورمان برای حضور…</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SorkhTimes/134098" target="_blank">📅 19:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134097">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">✅
اعلام ساز و کار لیگ برتر در فصل آینده/آغاز مسابقات از ١۶ مرداد؛ تورنمنت سه جانبه برگزار می‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/134097" target="_blank">📅 19:48 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134096">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">✅
شروع مسابقات لیگ برتر فوتبال ایران سال آینده از ۱۵ تا ۱۹ مرداد خواهد بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SorkhTimes/134096" target="_blank">📅 19:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134095">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eb150d050.mp4?token=IKuAfX1pwkDIrumr3mWyiXsx5GtV3eSD_qc4ZcFPINJxvN5FQs5oCi61VH8s9FFOJFxUAmQqC6UsB3nJIJmvLadxkKV4KEvLP4jkBDx_PB0y16wOFj6uiP3PyrQRMh3m8l3rkMSklNOX5lJd1dcijUgIgWejunYq0ozYuXIWofi_Z0CWyQntcz0fN1NfpGf2bqOZdbD5KReS62NCrmY96MmD3fy-ykeIyW4XgJo8DbM7NkCpCmQvs1bkr34z7O45Pq1DDOceJk1l3CIGYhQm502nVll6f-RIDgeE1pzEloXmYih7p9OlUBk2qqoXo53_OUKcUb6M7DpNNKkzq-rJzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eb150d050.mp4?token=IKuAfX1pwkDIrumr3mWyiXsx5GtV3eSD_qc4ZcFPINJxvN5FQs5oCi61VH8s9FFOJFxUAmQqC6UsB3nJIJmvLadxkKV4KEvLP4jkBDx_PB0y16wOFj6uiP3PyrQRMh3m8l3rkMSklNOX5lJd1dcijUgIgWejunYq0ozYuXIWofi_Z0CWyQntcz0fN1NfpGf2bqOZdbD5KReS62NCrmY96MmD3fy-ykeIyW4XgJo8DbM7NkCpCmQvs1bkr34z7O45Pq1DDOceJk1l3CIGYhQm502nVll6f-RIDgeE1pzEloXmYih7p9OlUBk2qqoXo53_OUKcUb6M7DpNNKkzq-rJzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
تتوهای خانوادگی مارکو باکیچ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/134095" target="_blank">📅 18:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134093">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETFxa6PLC3zF81awT0pWDLxVIRsI7MTQ1-W3WpHjf5V4z051WZondiyavIxzThVNNqlWcNalfK-59Zxm48YsRHtaU4eU-ryAFxjAox2pO-ABTCStIO8z4ThYy6Nv5sbJvQAGwU8X1n0r2vWlym78H2ShYbaTwxCIF-e2rioBc8fzs6DSKb85W85sIBWSPgX4XSuGvOWEorQ6C4ZdcP0Q1wV1XI_mrca4PeHLtffdjz9oshdi0ZAT6rXw8Zaj3YAms8BOFQyN14vf0--V9C_ikbazwc8YpZHIzkn5lNDANHjvhvs4le5hrcprME7zNmnp5DvkzwDeoc8Stesm1tIUwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
ملی‌پوش پرسپولیس چشم کورتوا رو گرفت
🔴
تیبو کورتوا پس از دیدار بلژیک و ایران در اینستاگرام حسین کنعانی‌زادگان را فالو کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/134093" target="_blank">📅 17:26 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134092">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🔴
پیمان حدادی: تا پس‌فردا بین اوسمار ویرا و دراگان اسکوچیچ یکی رو بعنوان سرمربی فصل جدید انتخاب خواهیم کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SorkhTimes/134092" target="_blank">📅 17:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134091">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❌
هادی حبیبی نژاد در آستانه عقد قرارداد با پرسپولیس/ ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/134091" target="_blank">📅 17:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134090">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
🚨
محمودی رسما در لیست رزو تیم ملی قرار گرفت عازم امریکا شد  امید نورافکن و کسری طاهری که قرار بود با تیم ملی به آمریکا بروند، به ایران برگشتند و امیرحسین محمودی ، خلیفه، حبیبی نژاد مسافر آمریکا شدند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SorkhTimes/134090" target="_blank">📅 17:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134089">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❌
سخنگوی باشگاه:
✅
« اوسمار به کار خود ادامه میده و تمرینات تیم زیر نظرش برگزار میشه. هر اتفاقی رخ بده، از طریق رسانه رسمی باشگاه به اطلاع هواداران عزیز میرسه. »
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SorkhTimes/134089" target="_blank">📅 17:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134088">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
بازیکنانی که به صورت قرضی یا حتی دائمی احتمالا از پرسپولیس جدا خواهند شد:
❤️
امیررضا رفیعی
❤️
محمدحسین صادقی
❤️
سهیل صحرایی
❤️
مجتبی فخریان
❤️
ابوالفضل بابایی
❤️
علیرضا عنایت‌زاده
✍️
خبر ورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/134088" target="_blank">📅 17:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134087">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HfaiOLf_I5bAfqbJDb0SuOTLBJphPtvHIuVpr9HDJVJaCn4c7MJTdvJutQ3HlcRv_2zEiM047qns-358uYOPMrKafYRwQ4_U62dZ2MPG6Sa281Z0_N5QQTLSINF8JAmVZa97v35qO_ORLNJiHDT94RgFZXxKq_X7XI4T0hbt0jktTiiG0qgQCBJHMtU0Kywz81coW8OkOQZ9RrNCfvyOviB6_qcwIpQeBxCbZw3ROVaedSkRB0vA8hVsyFazice0vRgPfgjjAOtcgR37tA4AFtUT7smSevKrcz7RrMu3c0BtiG6ud8n8bu_8OlcqrQJ447BMc4Ewt7O9iKE__UtTNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
فقط کمتر از
2⃣
1⃣
ساعت تا بونوس ویژه جام‌جهانی وینکوبت باقی مانده!
🎁
🔣
5⃣
1⃣
بونوس ویژه روی تمامی واریزها فقط با یک گردش روی حداقل ضریب ۱.۸ به موجودی خودت اضافه کن.
📌
همین حالا وارد ربات وینکوبت شو و ازین بونوس ویژه استفاده کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/134087" target="_blank">📅 16:43 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134086">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🎥
گل‌های روز گذشته جام جهانی ۲۰۲۶
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/134086" target="_blank">📅 14:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134085">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❌
#شایعات
🔴
اوسمار به دلیل اینکه مهدی لیموچی درگیر مصدومیت بوده و کمتر به میدان رفته با جذب این بازیکن مخالفت کرده  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/134085" target="_blank">📅 13:48 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134084">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
فرزین معامله گری، علیرضا همایی فر، علیرضا عنایت زاده، سهیل صحرایی، محمدحسین صادقی و محمد گندمی به اردوی تیم ملی امید دعوت شدند   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/134084" target="_blank">📅 12:10 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134083">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
ثابت‌قدم، مدیرعامل شرکت توسعه: تا هفته آینده نصب صندلی‌های استادیوم آزادی به پایان می‌رسد/ عملیات چمن هیبریدی هم آغاز شده و تلاش می‌کنیم به اوایل لیگ برسد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/134083" target="_blank">📅 12:09 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134082">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">✅
نساجی مازندران به لیگ برتر بازگشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/134082" target="_blank">📅 12:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134081">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X2iBgVvQCas_VDkzW-1l9kyvh_Zuwq7RxNAWK7NgLaUCAsasp_zL-IoJJsQ9OJESU-PeRsHLoMcw2GdEkEGO_6mXVHqUf84axqyqnGHR4vaFSoGI6ONWA2ZWvRuwWO-VO0l0FTI-6sGJaVx-20ZyL2hQQBzK5dClOhoXctwzVRhU5G9vWyAgEpoIZ14MwRsY7SzIfk1Y2v5uGVnRjFxPS1XIWPB0O4l8zy6KmUcEU6jTW8rY9xXNFrotROUtDXjKcf06_8tEEtGj6w58rHN_yKKrMUDg-1saiuLTk3phddHfIQXO78w9i-XtPMFiPo9CF-AnhTlLROCklkhNDXsaKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بر اساس تصمیم اتخاذ شده، فقط فصل آینده 18 تیم برگزار خواهد شد و در پایان فصل آینده چهار تیم راهی لیگ دسته اول خواهند شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/134081" target="_blank">📅 12:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134080">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/652cdc4d67.mp4?token=G6GbywM7AlbIqRZt7ClENLdFmmg9vOYAOn15968OCazHAUayMLAcQVqSr5zCjRB1rYBdlr6c0TcbfSaLwtcCuleGiLh-b7i66HGEgeTeKqYKF_ZBYR_622l26IHBQ8KHZUdLdLjys45ihmAUMtZRdg-jgscwkeqzM1v5KTi9-N29vrxvwm50VBZrRNggk25ouzj4sdTvZWzM6KYEV9yW0Uts6mR12ZPE_AjXeYqSNNea3f351wx7vxDu-hPRuDtLmWISu_9Wv6mkI1JXZi_jw5kR8cJDUNymhdtjL7daDVQwHJbN8l2cGihyFK2Z624aTWhnxXkU1jBnJ6G7bILTXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/652cdc4d67.mp4?token=G6GbywM7AlbIqRZt7ClENLdFmmg9vOYAOn15968OCazHAUayMLAcQVqSr5zCjRB1rYBdlr6c0TcbfSaLwtcCuleGiLh-b7i66HGEgeTeKqYKF_ZBYR_622l26IHBQ8KHZUdLdLjys45ihmAUMtZRdg-jgscwkeqzM1v5KTi9-N29vrxvwm50VBZrRNggk25ouzj4sdTvZWzM6KYEV9yW0Uts6mR12ZPE_AjXeYqSNNea3f351wx7vxDu-hPRuDtLmWISu_9Wv6mkI1JXZi_jw5kR8cJDUNymhdtjL7daDVQwHJbN8l2cGihyFK2Z624aTWhnxXkU1jBnJ6G7bILTXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
پدر کسری طاهری: کسری فصل بعد پرسپولیسی ست و قرارداد داخلی امضا شده
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/134080" target="_blank">📅 11:59 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134079">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cfc110b2c.mp4?token=moCgIEjUIQUt4kYyQh62A8-Zx8U3aEeLQUlMgybpcIuLAwsDXOwrYl9yoQxX8-OlmlYL9z-UaVdCpzZTmelRiw6wW2NQ7XzUZYnSFb5C2YMAoIzGecn1TJ8ILq8t6T8XpDOCxsquTnBkTQ9M3-b9rd4i9tZYRZqGxL0EMgYOUZsaspKt-OMWTzge9i_zd1RVglAOeHXWNloXEAK8MeS-EE0e6DgY5YqPl-CuSUszJcsmVJ_W_IuPN6Tx5EMbl7nk-TN28Kq6PCelNK1RF48v7cvVAjSszo-6nOABcVbHFzMGv9W_vkgFnvicf2D4P6spzbXcYHRPrHWP1MZ812N3tF7IJN21mt7QRjSsvPXb9nF91RX5WSfOTTxKibsOh9EjUAMSl6hVXZ_UDw86ha6hhEjfenhir7Nn_itMwWWRVzkDBgLfROXou6d0ovMh2QnmFJFiRoXkNthK-WGQ8xe_MqtqR8sTYhNm4LTO4a3-6yJSbiOibqCghwRLCwEurf-mZ6yGknPl1pP3GGKJgyEzu0YX0fygEqSha4Fn0urjztLvzjVfNRAV6-p823aGM_tBF6VJd_cO_7Hrv4aTBN-jbqhiiLbglv4kSXX3OmOON0nuQfjFNAhMxhrf4SaZ4jM0l8F3U2vmdI2-VtVYiCUDsloYbJOSDOf7eLowIppmSlM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cfc110b2c.mp4?token=moCgIEjUIQUt4kYyQh62A8-Zx8U3aEeLQUlMgybpcIuLAwsDXOwrYl9yoQxX8-OlmlYL9z-UaVdCpzZTmelRiw6wW2NQ7XzUZYnSFb5C2YMAoIzGecn1TJ8ILq8t6T8XpDOCxsquTnBkTQ9M3-b9rd4i9tZYRZqGxL0EMgYOUZsaspKt-OMWTzge9i_zd1RVglAOeHXWNloXEAK8MeS-EE0e6DgY5YqPl-CuSUszJcsmVJ_W_IuPN6Tx5EMbl7nk-TN28Kq6PCelNK1RF48v7cvVAjSszo-6nOABcVbHFzMGv9W_vkgFnvicf2D4P6spzbXcYHRPrHWP1MZ812N3tF7IJN21mt7QRjSsvPXb9nF91RX5WSfOTTxKibsOh9EjUAMSl6hVXZ_UDw86ha6hhEjfenhir7Nn_itMwWWRVzkDBgLfROXou6d0ovMh2QnmFJFiRoXkNthK-WGQ8xe_MqtqR8sTYhNm4LTO4a3-6yJSbiOibqCghwRLCwEurf-mZ6yGknPl1pP3GGKJgyEzu0YX0fygEqSha4Fn0urjztLvzjVfNRAV6-p823aGM_tBF6VJd_cO_7Hrv4aTBN-jbqhiiLbglv4kSXX3OmOON0nuQfjFNAhMxhrf4SaZ4jM0l8F3U2vmdI2-VtVYiCUDsloYbJOSDOf7eLowIppmSlM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ثابت‌قدم، مدیرعامل شرکت توسعه: تا هفته آینده نصب صندلی‌های استادیوم آزادی به پایان می‌رسد/ عملیات چمن هیبریدی هم آغاز شده و تلاش می‌کنیم به اوایل
لیگ برسد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/134079" target="_blank">📅 09:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134078">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5172bbee52.mp4?token=llcDX5Yp4Fj83dsNxq-huzRjQ66T1J2tp6g8rQNITKDPniF7NCMGsrZMS7a4h5_jCejorXgxQ5t7UYLw6_3zco5kiXCfO4sDu_yIvCjctYhgAQAeqRr7-1gFpthHNpt9Vxn2KplXieIWguGtROpmOSU7QIdX6aQ4TuWjIpbMASV4htRNtYd51zsa7owqBEggXWrrmzpCkHKqWUi5jk0HJLtacotffJm6JfJ1ctJm4gQ6RzygyfMRH-VSXDrdvsUEKktS78zGsO7AkR-k4VYl6JH6DotUIOYPJcW9Qp4JNFzoHg-r1bYa3NonD0pT41b9YvYGg-mcJKlzNoxu1XqQwxpyWfIWlr0yMRxqOnoydyi3f2Kyx68gCqJoBYuB7RKg4k4SgyOpHaKbO4rtGOJ43KUln6ejB-9eYT3Sfn3fbRwHeKSbD2m06SoyzgvdSsRSwKxpzh_yRhD8G5ranxPiIvL3XW5ttkNmgvKwgSD3079RbHfb0e7QSltbxN9JbHT4r5bPMeY7AfhblsoLr_FSGkMs9wrzJ_4Ps5eq9VVMGCGS2HGfME_KRdp4L59VKvDuzvOgKDre_bxWCwffaBzUAx8qAOHbhUoOwHqdPU2NgqU9cCVxfFhY__JH8nXOImNPSBXC3Gv5JH94SQunpXXOx_6kOQup1JgLp4C7ctiqUK8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5172bbee52.mp4?token=llcDX5Yp4Fj83dsNxq-huzRjQ66T1J2tp6g8rQNITKDPniF7NCMGsrZMS7a4h5_jCejorXgxQ5t7UYLw6_3zco5kiXCfO4sDu_yIvCjctYhgAQAeqRr7-1gFpthHNpt9Vxn2KplXieIWguGtROpmOSU7QIdX6aQ4TuWjIpbMASV4htRNtYd51zsa7owqBEggXWrrmzpCkHKqWUi5jk0HJLtacotffJm6JfJ1ctJm4gQ6RzygyfMRH-VSXDrdvsUEKktS78zGsO7AkR-k4VYl6JH6DotUIOYPJcW9Qp4JNFzoHg-r1bYa3NonD0pT41b9YvYGg-mcJKlzNoxu1XqQwxpyWfIWlr0yMRxqOnoydyi3f2Kyx68gCqJoBYuB7RKg4k4SgyOpHaKbO4rtGOJ43KUln6ejB-9eYT3Sfn3fbRwHeKSbD2m06SoyzgvdSsRSwKxpzh_yRhD8G5ranxPiIvL3XW5ttkNmgvKwgSD3079RbHfb0e7QSltbxN9JbHT4r5bPMeY7AfhblsoLr_FSGkMs9wrzJ_4Ps5eq9VVMGCGS2HGfME_KRdp4L59VKvDuzvOgKDre_bxWCwffaBzUAx8qAOHbhUoOwHqdPU2NgqU9cCVxfFhY__JH8nXOImNPSBXC3Gv5JH94SQunpXXOx_6kOQup1JgLp4C7ctiqUK8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
فیلم خلاصه بازی نیوزیلند 1 _ 3 مصر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/134078" target="_blank">📅 09:27 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134077">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">✅
جدول گروه G جام جهانی در پایان هفته دوم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/134077" target="_blank">📅 09:10 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134076">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❗️
قلعه‌نویی: معادلات گروه را بهم زده ایم و به دنبال صعود به عنوان صدرنشین هستیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/134076" target="_blank">📅 09:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134075">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">✅
جدول گروه G جام جهانی در پایان هفته دوم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/134075" target="_blank">📅 08:59 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134074">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">✅
جدول گروه G جام جهانی در پایان هفته دوم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/134074" target="_blank">📅 08:58 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134073">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uPEX8CasvXLyzf69pzEvTqqmA_DtU8QNq1CMMaEnb--TmpIHa6xWNqSVoAqPbvrJRz8tLi-aDa02O9LJ6jiGlcwdoMRsR2Td_MJbdYLN06nBuejvQ2WbCV8ADkm8E3yaTHOkQtAN4nUCDdEUmoCHWcU4480rhWyCjT7tme2bebnHCz6-TLjlU0Lfagm9Pid6TH1ev0LZfZsaDLvxv1PdpWk-hTsJMpMmRtNR9y8k2_j80CD8tU_onIUJCvPsPtvcqk087XpfsVqG5r28mXNcy9iYnU3qpDwvcMKyR-ksGPGvmzEuAvYm2y7aAAcdHU2vs3h-CTtV-QAGoLdwjE3SMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جدول گروه G جام جهانی در پایان هفته دوم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/134073" target="_blank">📅 08:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134072">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k9YiA6qxB9713mJxV_XjXcfYYCtnINtZXvWFiF1CEcHkyY9qAz6XABm1noehSiWAK5AUwX1284Tal-OK69odxFJG3GHgDI0EcfAEjA4LyxfxkHV9n6lKMeIr8ALGeaI7cIgXiHTGTRNdLy7dMbSpVZd-0pCo1J6P7-n36btRFIX75enEm2EA7PaZ8D6L_FfzrR0YcbhhRafWgTcb04WYvNjseJaUcLHxfk4jZHj4ExJ7bTBourARRN4zngcdQ5NcRcybZDtNe3opzeSuYzqYMrLw2z1yUcCLgObkuigd6HRlQMD75sQcMONSGK0lkTcPe0ps6PN2uqSgf3LPN9mDmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
نتیجه بازی های دیروز جام جهانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/134072" target="_blank">📅 08:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134071">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RFQ7PSLOPNv7Gu2IfnG4Up6Ki8DLsIEziAVPdnnf6xgVpc4aZmcHe6byAh33oKwlw8q8uR7ATLpuQyBKABc5_-mS3BrtgwS-vD_TyPi3zCMOPalj1-f0HR4TesOyXAjOSLnS28f3SFMw_brjN-k9Wu4W7fp7VbrgzJYX8hadcRIGswMi55u-feIXsgzYjSESsFgwpF0cfU7U027wGvF3eDeH8hTGnQHqiwPETsmsoDxgCgBM5HTBsDAw_GJQ1AoTxLmrE80AC9HjlsxD-u9Ae18bJSw5iGTu8rUcyxdKZjz1EI-d-_MlvRuqtnn7caV4LQl4PkNDNLv6zOFmE3wU1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
ژوزه مورینیو:
بیرانوند هر توپی میومد سمتش رو می‌گرفت، بعد از همراهانم پرسیدم این پسر کدوم تیم بازی می‌کنه؟ و گفتن تیم ایرانی انتظار داشتم بگن یک تیم بزرگ اروپا و فقط محکم زدم تو سر خودم چون حق بیرانوند این نیست
❌
اگر یک دروازه‌بان بتواند آن واکنش و مهار توپ‌ها را مقابل بلژیک انجام دهد، یا باید برای یکی از بزرگترین باشگاه‌های اروپایی بازی کند یا اینکه استعدادیاب‌های فوتبال آدرس او را فراموش کرده‌اند. بعد از بازی امشب اما فکر نمی‌کنم آنها دیگر آن را فراموش کنند و به سراغ او خواهند رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/134071" target="_blank">📅 08:25 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134070">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqpL5SybQDSqIlGAeux1PjPRu3OqwlgT4iyRXQPhA7UdZe6Xx8B2i4cXnhai5HZbX-Ihw0aCTb83fZArV-Xavu0ByeaTORbqi_H3h9-b80xJA2hcuedAWtfzOnqFiTLv0aG-qagCSgX-y2cN96JVD0kWGPbzXOl8zIw1xFuuGRLOT-TUZ-kSCd44HMV60EybH1GWgbGn5C5UT2I3DbnoDCmHhm8PDsXuNYZ7EXdiSZVqHCFLufdypUC2e4CfVLl77lauX32bfmsPduie_cTscpbNiyuFldKvJyT1YzoG2LEM9SEBo7UGx5LKClR5mjvgPf-YqY_qGyLUtc5JMd_ugQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚽️
اوج
هیجان مسابقات جام‌جهانی ۲۰۲۶ فقط با
اسپورت نود
⚽️
گروه G جام‌جهانی ۲۰۲۶
[
مصر
🇪🇬
🆚
🇳🇿
نیوزیلند
]
⏰
بامداد دوشنبه ساعت ۰۴:۳۰
🏟
استادیوم
بی‌سی پلیس
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
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/134070" target="_blank">📅 01:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134069">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">✅
جدول گروه در پایان بازی ایران و بلژیک
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/134069" target="_blank">📅 01:14 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134068">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GnRVpY0s5SRisBe6AJ6C7BKctVs06EiYPu-N2zNpVSyd5jW6wEHmcyavGraxOUqwoYPaKRdaUzwO0nJRehzZ5REdXs6dT3j62iGItIzhldX9g3j-VS3yE2YXUWERnvndz-oQP8KkSqNx6u9wL-yw4YJ_ICzfogTmUTmu8_6enQ_1HKOOmmW5TjWbR9QYJsGdd93P1q_vr5ObgXrMkpnzyBvmomEb5STLsr4QwLdmeup1FCLWRPkDVceXIksDWSSfwk9F7-6HND-W04NcEWmn6wwlX37uxTTaXnJzX8s5RARSy4_tztulAnYNdMiiEddnFTed3URAXLznBLJ3xF8KvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جدول گروه در پایان بازی ایران و بلژیک
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/134068" target="_blank">📅 01:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134067">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p97bRCGzBq8UVRNBMI0A8ccgeS_fbyTH6UjbJrrIVBI2lAKulU0dc2X4dTkx_qUP7noVcXDqh3rgCL4MFViGhvoAPJS5u7zn1KC9QxayhpQR8TT0VSI49VnAriSGTtUPMUMC5GjfnxE4bduOzhVW9kzULdvtOBZJU0nrdmcKrxMdF6OrClksfSBtKbW_B3ucdG3VO3uhl8Zo_JTKnkaSD3T3ole-ADUR_BCYjV1UeN55RxrCkIr0IMKldmYXJHXz_RWrORD-02pZDqgQIjmBLcKzRlRq5AQQSBuSz158Era981j5-9-s-DGYW0k7gveiGQC_2mg0HPGELcltKQkWoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نظرت در مورد بازی ایران و بلژیک ؟
🔴
ابراهیموویچ : نزدیک بود نیمه اول خوابم ببره و نیمه دوم واقعاً خوابم برد
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/134067" target="_blank">📅 01:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134066">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EokywUQDk1I7oIUie_JJ22RbDl8M90ezoHBET6G-k4Jpy0jSOll0yzNlt_ojGCaixaSVr_7wotM7LT8uv0uNB-5spzSDNMVtT5b8J6qemvI9Q3qFJTSvg6AhdMbR3rN3O4CRJfBMY3qCoBIcMOHiwYUnFtaabGBoS3y58TPKc7SWRyokaOqtmv9N_04wz29_id8h6PyA6eBI_gzGs_mqEwPN11WoucOMrv5EYGd0LMUxXcsbznm56T_krKTGP9xWmCjczW11uYmajXKfQk0Pm9k5zAQssmub8OkhLaYzRgccE3Bj3Rj5-SSu1jzuTyX7gCrP2ExOJoIl8OjGq5oLyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
بیرانوند و جایزه بهترین بازیکن زمین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/134066" target="_blank">📅 00:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134065">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UdXF8K7ZpYEltZ2WmyLpukrXi4pqpnXZz36trIa1IsEgr8wUR2l0E7tf3t7p14JBBtI82e0UAzWlkpAoo1E7l0fMtelDanR0x8oU9C4_9689q-_igAIkCFH94Si9jEaMM5DGTACSzcD_rjmCl8KJ2Mf-t3cC9hs8VM8HaZNdWFLKR_nKqZVzN4N66ZEo0vqdRi28gu-551LRUur8mYxXyDNrw7Ci_hceO2yy2h8amM2DRHQ8nFaJk_HNB8PaZZtTA1rtaEtrQY48UtVYo42j2fFal7OXVM7oAdABLzJYjGYhbSTewat3sBtxCLwsScbQ_lO3maZGP5Vm5tZhRGFK_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سرطان اخرشب بیرانوند در کنار مسی، تونسته نمره 10 بگیره(:
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/134065" target="_blank">📅 00:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134064">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/135ac7b305.mp4?token=qDxENQVXhdbDneACwBG-HWe3v9CD6d7RMFJRRb93j7D5FpOlv-MtuezZ9xwEdJYf7sPlzeM9ies0LpqQkC03EaqntcT74pAyjWpkcHoRkLb-Nx-mO86rXi0aywsBNlcjrNHrMLqLvsoHPYtHbWflUM5Xbf-ubcF3usX6hN6grZjE-CApb4qEnc6ApVfMVUlaiMK1HHLiawIO7aJsTsN_qG20aaL4LxGhKKKpIiBX0KAFBcaoe-h84AWY0XdG3pXq_5UdGrABwEqDIxuM4LYcpKlSvtm6o_lEZQMP8D774uVgVFz-PJL7Po2m7Zw39eX2mPN-vWEIpHDyPRdetYEZWyO_b1gG5xT69PB10nFLTlZkp7BDAEHOMuGg5R7xgFDIJgUOHRxfqs1IXp9370EEihztkNFDNEatV_JtRQklloJyS5yep0d9d7v7sgL59E55EKg2kQ7wgB9taK94wsx9eC3qVLfzV2-xOXZo087vwOYCSu6m5FsgAdXjPeYHoCPvmx4Qg9Q1yzRkbeW2RgRUHlJ6ZGl6eJ3g7ixYQZmm7GFTAAQGd4il58_NyDy4xnod2dX3aBuTESm_UpnXnSN1EBUF8FEqEBUAh-tHS3xp5MvCzOlyeWBmDH1ssfSstv4JmInbMYOfhgJz5MO1xEWSdz3d_9GHfldZzHbF1T0MUcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/135ac7b305.mp4?token=qDxENQVXhdbDneACwBG-HWe3v9CD6d7RMFJRRb93j7D5FpOlv-MtuezZ9xwEdJYf7sPlzeM9ies0LpqQkC03EaqntcT74pAyjWpkcHoRkLb-Nx-mO86rXi0aywsBNlcjrNHrMLqLvsoHPYtHbWflUM5Xbf-ubcF3usX6hN6grZjE-CApb4qEnc6ApVfMVUlaiMK1HHLiawIO7aJsTsN_qG20aaL4LxGhKKKpIiBX0KAFBcaoe-h84AWY0XdG3pXq_5UdGrABwEqDIxuM4LYcpKlSvtm6o_lEZQMP8D774uVgVFz-PJL7Po2m7Zw39eX2mPN-vWEIpHDyPRdetYEZWyO_b1gG5xT69PB10nFLTlZkp7BDAEHOMuGg5R7xgFDIJgUOHRxfqs1IXp9370EEihztkNFDNEatV_JtRQklloJyS5yep0d9d7v7sgL59E55EKg2kQ7wgB9taK94wsx9eC3qVLfzV2-xOXZo087vwOYCSu6m5FsgAdXjPeYHoCPvmx4Qg9Q1yzRkbeW2RgRUHlJ6ZGl6eJ3g7ixYQZmm7GFTAAQGd4il58_NyDy4xnod2dX3aBuTESm_UpnXnSN1EBUF8FEqEBUAh-tHS3xp5MvCzOlyeWBmDH1ssfSstv4JmInbMYOfhgJz5MO1xEWSdz3d_9GHfldZzHbF1T0MUcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
❤️
علیرضا بیرانوند: هنوز هیچ چیزی تمام نشده است؛ از همه مردم تشکر می کنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/134064" target="_blank">📅 00:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134063">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❗️
بلژیک رو هم الکی گنده کرده بودن چون واقعا تیمی نبود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/134063" target="_blank">📅 00:36 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134062">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❌
ایران با ی بازی سرد و بی روح و دفاعی و بکش زیرش  ...بازی و صفر صفر تمام کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/134062" target="_blank">📅 00:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134061">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❌
بریم برای نیمه دوم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/134061" target="_blank">📅 00:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134060">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🔴
پیمان حدادی: تا پس‌فردا بین اوسمار ویرا و دراگان اسکوچیچ یکی رو بعنوان سرمربی فصل جدید انتخاب خواهیم کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/134060" target="_blank">📅 00:14 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134059">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❗️
ایران با هشت دفاع و بکش زیرش و خوابیدن روی زمین .تونست نیمه اول و صفر صفر تمام کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/134059" target="_blank">📅 23:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134058">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">✅
بله آفساید اعلام شد ولی گل قشنگی بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/134058" target="_blank">📅 23:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134057">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">✅
بله آفساید اعلام شد ولی گل قشنگی بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/134057" target="_blank">📅 23:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134056">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❗️
❗️
جونم ایران ‌‌..گل اول و زدیم ولی فکر کنم آفساید باشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/134056" target="_blank">📅 22:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134055">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇮🇷
🇮🇷
کم کم برای دیدن بازی ایران و بلژیک .امیدوارم خوب بازی کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/134055" target="_blank">📅 22:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134054">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇮🇷
🏟️
🇧🇪
ورزشگاه سوفای لس آنجلس دقایقی پیش از آغاز دیدار ایران برابر بلژیک
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/134054" target="_blank">📅 22:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134053">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇮🇷
🏟️
🇧🇪
ورزشگاه سوفای لس آنجلس دقایقی پیش از آغاز دیدار ایران برابر بلژیک
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/134053" target="_blank">📅 22:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134052">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tvdRmgeTvTwhYGPB2XePL8E7sjAuR7v063HAda7vUVZAGEI0OSEzhOQrKaurHmN9O9oXkcfAoAR5aDrqV0VQQDImuegbxCKj0fva63rYI9ThiR2nbwQlGGcwvrYg-PxDvAt29ps_8WG0rDA_crANIGA_66XdeM-CIINj7WLFBq5-gSzk4d3RKBFROphwPD6fymCEQZWKViCw6YqmvcnoPUiRCX0EpHlQ3Eywmd2mdxbm-Dv4ZJ549aqvGs9gUJ-BRjWypLvEZRzgVuZXgeW6iJ5gMgC1dVYWq3L9BcHBPW2eaEXtYKJkfjc9nRoPSrT_bW1l9DW5AmBIWN3dy060mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
رودی گارسیا سرمربی تیم ملی بلژیک: برنامه ویژه ای برای مهار رامین رضاییان داریم!
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SorkhTimes/134052" target="_blank">📅 22:14 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134051">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RDXK4epn256DcJuwGX7SLUPjuzvjJvG7KFU1lNeFRPfi7Rb0jVf7PHsAbnFQTJoed1Gwj3rJgm7oVCdNcMG2YYgDbVrxXbu6tu6li0Wa-dmOYINNlAWjikDMWvhlo5X6kLXkSBIPGdfj3RFw9t1tjfksRV2YRKX8B7gKpxdTI_byL6gpSVyY8UWHpAoT9l2FwMRoma-FLiVhIHMjSgd7GD8CGYtjv4kY3vS_7mYee2URPJ2e4rfoaripMYbnUkQ6VM_QyH6f9tpyjWsma5UTEdGEfnD1IKjhDLy48EdTxQqA3F5jYGUwWcJ7lCkeLTmegDiV3POQdT3TYGMel7CNfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
به نظر میاد ترکیب 5 4 1 هست و با پنج دفاع بازی می‌کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SorkhTimes/134051" target="_blank">📅 22:13 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134050">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">✅
با توجه به قانون جدید که فقط هر تیمی میتونه 4 بازیکن خارجی داشته باشه، اسکوچیچ از پرسپولیس دورتر شده چون باشگاه بهش گفته بازیکن خارجی نمیتونی بیاری/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SorkhTimes/134050" target="_blank">📅 22:10 · 31 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
