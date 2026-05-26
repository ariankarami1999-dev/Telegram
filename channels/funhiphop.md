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
<img src="https://cdn4.telesco.pe/file/dGbWWUys1Khmfup6aajzwLX9dKHscLRBPiQvKWPlrp6fhYfAoqViQxqfS-bnyHfaJsaKA99jr8FJZ4yKxqsGTmIf6fLiZUxyvIhQF7o9VoHy738xQWPWhUWFDjQRf6sfI7Zr7zZnPBwXI_0Yq1maGLfJAC-DhZ30YmR5E_1-yR3ua4xffIVa0IDAgilK_L1gVsU1BSdTZhnqiHEem31yJDG2RAIIt5pic0XfgJlXSa36rErqPPu20uYnGu_kVgy3Ivd0Us_6r4jgSafZSiIXe-uJRB6IN8-Ty3AdBWpGv2f7cHjhjEgxbYwwUm-_DMlk_Zd3Xc4bvwApT4hle3y6QA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 183K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-05 17:41:59</div>
<hr>

<div class="tg-post" id="msg-75984">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">وی پی ان فروشای عزیز چرب کنید که قراره از این به بعد ساعتی ۵ تومن پول تبلیغ بگیرم ازتون</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/funhiphop/75984" target="_blank">📅 17:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75983">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nI-xsQ-nPh7u-DjqX0BwiAxmcs_TxVJoPisE9MvEATpz2PkRriKFlT1g0C7XOFpsSnFhLdi0Q4t6BbCx9Ig7HHbYsI-ljsc9P_egr1nUqItAihoRbnKKlpOjWjlfxxsVw2uGSKPgpaqD9H9rJ4hCWkTLYzUtjuY7nP0EvITgVi6ugHEadsu1V_V3YQu09NSdgKRzJF3It0ZEqpz2-J5LVsyi6A4L8iQJJSMZ0R2Dyvv6ZvlKs9it6onYeo_QdMUo2CX8CHmhCCbDC_YzSjL7uK4-IHZaZvBLbtXTpMNr331ovcyCEw16Q0JbeMnnBj5Pux6OoD5NYjjm6y0YxrxAGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطعش کنید، قطعش کنید خار این اینترنتو گاییدم قطعش کنید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/funhiphop/75983" target="_blank">📅 17:06 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75981">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">دلقک بازی میکنیم ولی حقیقتا من یکی نمیتونم بابت برگشتن نصف حقم خوشحال باشم و از کسی تشکر کنم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/funhiphop/75981" target="_blank">📅 17:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75979">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ای شیر زخم خورده، به خانه خوش آمدی
📱
ای پیر درمانده، به خانه خوش آمدی
📱
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/funhiphop/75979" target="_blank">📅 16:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75978">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">وزیر امنیت ملی اسرائیل، بن‌گویر:  من قول می‌دهم که دولت اسرائیل اجازه نخواهد داد دولت ترامپ توافق «بدی» با ایران امضا کند. می‌دانم که نخست‌وزیر نتانیاهو و کل کابینه وزرای اسرائیل اجازه نخواهند داد این اتفاق بیفتد. توافق بد توافقی است که می‌تواند به دولت اسرائیل…</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/funhiphop/75978" target="_blank">📅 16:47 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75977">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">وزیر امنیت ملی اسرائیل، بن‌گویر:
من قول می‌دهم که دولت اسرائیل اجازه نخواهد داد دولت ترامپ توافق «بدی» با ایران امضا کند.
می‌دانم که نخست‌وزیر نتانیاهو و کل کابینه وزرای اسرائیل اجازه نخواهند داد این اتفاق بیفتد.
توافق بد توافقی است که می‌تواند به دولت اسرائیل آسیب برساند، و ما اجازه نخواهیم داد این اتفاق بیفتد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/funhiphop/75977" target="_blank">📅 16:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75975">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">وای اگر پزشکیان حکم جهادم دهد</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/funhiphop/75975" target="_blank">📅 16:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75973">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">آقا خوش برگشتید
به یادتون بودم، همش میگفتم ممبرای فقیرم بامزه تر بودن</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/funhiphop/75973" target="_blank">📅 16:37 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75972">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">تا 1411 با پزشکیان
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/funhiphop/75972" target="_blank">📅 16:36 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75971">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ore7p80IHfdZfctPSmOmkfN862fTfKaUVEngC_WGg4ZULsyOtQiI35Jesj7rMeJhdyIm784ypXPaVxdI7CMVpIxvypTOK4JVWoXXL7KZvgYXHEHR4va253qqrY11AuZiOubfD8VmKtgnWRXmCzTTpLVcgfaIY0vfAdcSUpEVSR3v_5728x0u6VYe-pfhnPYSy6DKqABkk-s3XlY1jUv8JJdyD8wP2wf1qopwj6uDhuLwLqJlFk8ZYxywoTdiEqwTCOVEvGN4g6sFpwAv0VWWuRVkywOvGZ2AgpT1jAaFJjuXAKICzu1mPTeF7jIrUJrR5POvD1ug2RN2mwhhRcL7ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت مخابرات وصل شد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/funhiphop/75971" target="_blank">📅 16:29 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75969">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">حاجی من تو اورژانس بیمارستانم
کلی ادم رو دارن میارن از رنج سنی ۱۵ تا ۵۰
بطور عجیبی گروه شغلی همشون تو رسته وی پی ان و کانفیگ و ایناست
@FunHipHop</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/funhiphop/75969" target="_blank">📅 16:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75967">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">آسیاتک و مخابرات انگار دارن منطقه ای باز میشن</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/funhiphop/75967" target="_blank">📅 16:11 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75966">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ستار هاشمی، وزیر قطع ارتباطات : فرایند اتصال به اینترنت بین الملل شروع شده و تا 24 ساعت اینده همه قراره وصل شن  @FunHipHop | Mehrdad</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/funhiphop/75966" target="_blank">📅 16:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75965">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ستار هاشمی، وزیر قطع ارتباطات :
فرایند اتصال به اینترنت بین الملل شروع شده و تا 24 ساعت اینده همه قراره وصل شن
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/funhiphop/75965" target="_blank">📅 16:06 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75964">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">یه یارو از ۳ ماه قطعی نت ۲.۵ ماهشو قطع بود، الان تو چنلش زده تو شرایط سخت کنارتون بودیم از این به بعدم هستیم</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/funhiphop/75964" target="_blank">📅 15:52 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75963">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">یه آپدیتی رو فیلترینگ پیاده کردن که یسری از کانفیگ پولیا هم قطع شدن
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/funhiphop/75963" target="_blank">📅 15:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75961">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">عجب ماجرایی گذاشتم
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/funhiphop/75961" target="_blank">📅 15:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75959">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">کونیا من روبیکامو پاک کردم تو اون ۵ دقیقه
نمیزاره اکانت جدید بسازم الان</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/funhiphop/75959" target="_blank">📅 15:38 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75958">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">علی گوه خوردم بلاکت کردم بیا کانفیگمو تمدید کن داداش  @FunHipHop | Menot</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/funhiphop/75958" target="_blank">📅 15:37 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75957">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">علی گوه خوردم بلاکت کردم بیا کانفیگمو تمدید کن داداش
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/funhiphop/75957" target="_blank">📅 15:35 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75956">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">یسری ای پی کلود فلر باز شده که دارن روش کانفیگ رایگان میزنن، ممکنه اختلال باشه و یکم بعد ببندنش.  @FunHipHop | Menot</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/funhiphop/75956" target="_blank">📅 15:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75955">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">خر کونتون بزاره ولی الان جای اونی که تازه پنل گرفته نباشید</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/funhiphop/75955" target="_blank">📅 15:31 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75953">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">یسری ای پی کلود فلر باز شده که دارن روش کانفیگ رایگان میزنن، ممکنه اختلال باشه و یکم بعد ببندنش.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/funhiphop/75953" target="_blank">📅 15:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75952">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cd-XQ577wibpc5IkDewj2DN8oag8yNhRpCuJ0XZFc9vF2hP6QLF8ykfx69xJteeBsQ6YODQy6VayzyVjuIj0owWP9013LczmAZDPzjHCMxf5tDtCZI2cCzpntfDX5Xk__zSUagFCyF3MepkdRPsDZt-mjfBMw6p7HCZIOYqH5qAvPOK1OR8FW3Gv3A2lQ01IsI9a6JQ_yQ5WB9DJBUEXorg_lQgpnR7UfkSFg0UNWgfv0n3ZRBqePp3UPxFLcEB1KHGR-wbgy51tE5Njd6ECpNGttui2sM7N4kjp-Tm1In_q-wKtuCap4V3zI8I9_PAWe2_eBnU7IdkwEPc6oHGdRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه:
آمریکا دیروز به طرز فاحشی آتش‌بس رو نقض کرد و ما هم این اقدامشون رو بی‌پاسخ نمی‌ذاریم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/funhiphop/75952" target="_blank">📅 15:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75951">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">این مادرجنده باز شروع به کانفیگ رایگان گذاشتن کرد، فک کنم داره وصل میشه</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/funhiphop/75951" target="_blank">📅 15:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75949">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">بیایید به زبان ساده کیری که خوردیمو تعریف کنم براتون
اینترنت رو کی قطع کرد؟ شعام
کی میتونست وصل کنه؟ شعام
رئیس شعام کیه؟ پزشکیان
حالا راه وصلیش چی بود؟ پزشکیان از طریق شعام نتو وصل کنه
اما پزشکیان چیکار کرد؟ یه ستاد غیرقانونی برا وصلی اینترنت ساخت
نتیجه؟ از اون ستاد شکایت شد و رسیدگی به شکایت‌ ۶ ماه طول میکشه
و اینطوری شد که بطور
کاملا
قانونی وصلی نتو ۶ ماه انداختن عقب
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/funhiphop/75949" target="_blank">📅 14:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75947">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">پزشکیان: ۱۶ میلیون رای در انتخابات ریاست جمهوری
رسایی: ۲۴۰ هزار رای در انتخابات مجلس
قدرت اجرایی کدوم بیشتره؟ رسایی
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/funhiphop/75947" target="_blank">📅 14:38 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75945">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">وضعیت آیندتونو کامنت کنید
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/funhiphop/75945" target="_blank">📅 14:28 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75944">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">منابع آگاه به فارس درمورد پیشرفت مذاکرات دکتر قالیباف:
گفته شده آخرین اختلاف جدی میان ایران و آمریکا بر سر آغاز مذاکرات که مربوط به نحوهٔ دسترسی به منابع مسدودشدهٔ ایران بود که با میانجی‌گری و ابتکار قطر
در حال برطرف‌شدن است.
براساس این گزارش، پیش‌تر آمریکا نسبت به اجرای تعهدات خود در این زمینه عقب‌نشینی کرده بود، اما ایران با پافشاری اعلام کرد «تا زمانی که پول‌های مورد توافق واریز نشده باشد، هیچ توافقی ممکن نیست». نهایتاً با رایزنی‌ها در قطر، پیشرفت‌هایی برای حل این مشکل حاصل شده است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/funhiphop/75944" target="_blank">📅 14:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75943">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">مسعود چقد دیگه باید کیرت کنن استعفا بده برو دنبال زندگیت
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/funhiphop/75943" target="_blank">📅 14:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75942">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">دیروز پزشکیان تو ستاد ویژه ساماندهی و راهبری فضای مجازی کشور، وصل شدن اینترنت رو تصویب کرد.
الان فارس خبر داده که یه سری افراد ناشناس شکایت کردن که این ستاد کلا وجودش غیر قانونیه و رئیس جمهور اصلا اختیارات لازم برای ایجاد این ستاد رو نداشته، پس تا زمانی که به این شکایت رسیدگی بشه مصوبات این ستاد قابل اجرا نیست اصلا.
😊
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/funhiphop/75942" target="_blank">📅 13:56 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75940">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fPhMucoKRU2wiF6ydwyiInIuTBttG0AVqV-d5wF0wlP27Du-UfzGJxW61FBrx25jLoJDFwcrq6RixYuxEqYtZMLsX5IZzRVnfzlY30Jk2TJEYKllpBCEXgQf-vOizS6p3PVYaH3eO2ooZMzX8HuiSORuc9-wK8DM5vqU1MLeSCdRM5q1YY3Qw4xxhaAxC2L20GRmw18JHtu_sp_5DTWjbh8ueZ8vH7hRljhOURFXK-lf6d-n7UZ49V0DCvteg0xS0kXVw-Fi0uYr3UkGKz_vUhW_rq4e3ZPdITGE2CjWvKav2yh68NfsLEYFFeSO97j0BmRf48b_KssgrAZMII9mwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بوی بمب اتم میاد</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/funhiphop/75940" target="_blank">📅 13:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75939">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">بوی بمب اتم میاد</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/funhiphop/75939" target="_blank">📅 13:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75936">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">اقا مجتبی:
همانطور که پدرم سال ۱۳۹۴ گفت اسرائیل ۲۵ سال آینده را نخواهد دید.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/funhiphop/75936" target="_blank">📅 12:55 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75935">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">حس میکنم پزشکیان تستی ی چیز گفته ببینه تو نظام حرفش برو داره یا نه
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/funhiphop/75935" target="_blank">📅 12:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75931">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">خداروشکر جزٔ تنها چنلایی بودیم که اصلا تبلیغ کانفیگ نکردیم و مهدی هم بیخیال پول شد تو این سه ماه.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/funhiphop/75931" target="_blank">📅 11:58 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75929">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ERKOVDxDACorFJbB8dy7R3zHRjSjiVoI1bBvZNnn2fNAu7NrcnC-CS8ut57CSR6yUuHLU11iWxPfaAmqCRCtJ8r8wVdpxQ8I-n5oG7d_Y203P3iJ1jB8wyg2t-4DQL1YiwKf-JWyipTyWjyoJzjXz37821P1vY8ReHFugYwVmQOCRjzldfGEhslsrmpLQd6pYMgIbEyPk2agY4CbkG2u5VyT1baJfbexm5TKP9V_5ScorB1vEffrpHYzH6cDB7FhC6v55qifT0fcpJRHPaduKlhxaPGO6EEfB9-hd7tYuTWI36wsLvcKTvbW_VY5xXdXCBiSG4FNKSJqf2XIIIDoxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمودار نت بلاکس که آمار بالا رفتن وصلی هارو نشون میده</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/funhiphop/75929" target="_blank">📅 11:47 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75928">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">خوشم نیومد
از اشتراک معمولی ChatGpt استفاده شده، زیاد جمله بندیاش دقیق نیست
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/funhiphop/75928" target="_blank">📅 11:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75927">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">کصکشا گوگل پلی تو حالت عادی هم فیلتر بود، یعنی چی که میگید باز شده
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/funhiphop/75927" target="_blank">📅 11:31 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75926">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">پی دی اف بزارم براتون؟</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/funhiphop/75926" target="_blank">📅 11:29 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75925">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">یادش بخیر
ماه پیش همین وقتا یکی از ممبرا رفته بود کانفیگ گرفته بود برا پورن هاب، ۲۵۰۰ هم هزینه کرده بود
بعد لوکیشن کانفیگه فرانسه بود
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/funhiphop/75925" target="_blank">📅 11:19 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75924">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">یعنی بالاخره پزشکیان تونست یه گوهی تو این کشور بخوره؟</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/funhiphop/75924" target="_blank">📅 11:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75923">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">شهوانی رو یه سری از دیتا سنتر ها بالا میاد
باید ببینیم اختلال بوده یا جدی جدی دارن نت بین الملل رو وصل میکنن
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/funhiphop/75923" target="_blank">📅 10:59 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75922">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اونایی که اینترنت پرو خریدن دارن کیر میخورن
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/funhiphop/75922" target="_blank">📅 10:58 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75921">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ظاهرا جیمیل رفع فیلتر شده باید ببینیم اختلال بوده یا جدی جدی دارن نت بین الملل رو وصل میکنن
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/funhiphop/75921" target="_blank">📅 10:54 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75920">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">کصخلا بزارید کامل اینترنت بیاد بعد برید پیوی وپن فروشتون گنده گوزی کنید
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/funhiphop/75920" target="_blank">📅 10:38 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75919">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/laNlbAFCU7K5b_Is_79Q9eYJYy2YR3ZGZhZ-79fP_FuqxkZwK-awASyu6DihIUuZJ5aEPNzLQ8yAfZvRcEybAJ1yeNrWUOcvueBUMwE4wGLwSjkZEr7Vv27lSjF0QAUjXsb7QBnwzt4KDYTQY-S_44kKeYkgmZK8bL-qa01jAAb2VY8VSWOM0moKVcIno-7EiVYVGfDF4jPEgSofdQpu8KB5Hf0aQWMc3yW_EuzlZENGceZqkLEblXWvtJhcIS8iRrBNGQikYfNnECoWvztT8d73rYpLnznP5KXe_-38im3fmMzF5nxsA2x3qPf9pnKosfdQ264add36SBVpwTGTWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاپورتا مادرجنده آلوارز چه گوهیه ژائو پدرو بیار  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/funhiphop/75919" target="_blank">📅 10:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75918">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">لاپورتا مادرجنده آلوارز چه گوهیه ژائو پدرو بیار
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/funhiphop/75918" target="_blank">📅 09:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75917">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtA7HPfC6iAQ7vDREhcTRt6_XoyMGRhQMYlA4_loEQrDF5FDp5xgyNLGS7SQkLbDXm7TxLp4MyJR2veUHOwIsjI5IUEhpITWJ8-T-91uLlk2mSpn_7oBaUlil2mnlVZVdVFt6PwAqVVtA5oJG2syQTmj-oqvXVgmDwCOFmQbAU0cUoPVOAvXScKjNoiXMHqD13Ub70rMryIWkXcfNUaKCIN8j9lJrJq2MgnbyfUJNZu_zVFVj6cTYvnYr4OV6ksnfwnToYf-KMAxlijni-UjgN6eoq_jvPgWbVNtTIRFNkpqMvxR1BveugjazZFngs5EDgkz-X_JwUIQMj-083WPQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توپ 2014 یچیز دیگه بود.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/funhiphop/75917" target="_blank">📅 09:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75916">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/75916" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن اندروید سایت جهانی دربی بت
💰
اولین سایت جهانی با امکان شارژ و برداشت ریالی(کارت به کارت)
🔗
برای ورود فیلترشکن روی کشور مناسب قرار دهید مانند فنلاند و المان و....
😀
Telegram Channel
👇
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/funhiphop/75916" target="_blank">📅 09:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75915">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GrDp9GRLWp1zsJsjjjgd-vBxHxzskLwaUagxlsLamhosEn1d1NeYSormx6GBJPQgDOX5O_lwTdsZYBlqNVrjoDB3UiqmUQ4GOUPwQxhK9PbAiU70XVv0mQGLQX8YGHIxI7u6FJ6UrX9JxXrddqIEkIEi0bz8ZfYydQvQApcZ8IQjK80BQkGKRrwSZ9FRtO44gZcHHvOmZnN8KE2wNeRgjhvgnWoZOpq6GULasZHEiUNRTJFyZL4ZNuvzK6SKdHUEFLMIt72Nb7pS-oO0104Zc7NzydarWuR_WF0hMmeUTj92gtetpNv-6mgJO1bzP-DQmHbjtuQR5gKzzCAYX_PuMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
دنبال یه سایت شرط بندی بین المللی بودی که به ایرانیا خدمات بده؟!
⛔
👍
دربی بت همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
🚨
کد هدیه ثبت نام:
GG007
⚠️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت :r5
🅰
🪙
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/funhiphop/75915" target="_blank">📅 09:04 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75914">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RUHzE7K6UqAxFV8PWdlLr8DZD1ZpqNL8d9fUBn3B3ojz5gxb4kbJscouSVcWXwApxY2rMcD95YpklQq1QGzOix50rdPFtipU37EBXIc9v6-bkyhU9isKMwXk1OUa_xgznBlRNnBcbTYGJltMgryxgDUdeoMbrEPN9ngkj5nCnGZNPyaHApS9E2Lo2VLhRiAVK5jfWdlek4wwbqvecYIdj5RNfGwmB47lmRvlIyI8PbEdWASAi9ZjTVUjifWbYUni85JvrT-yzGzDiCrkSQ_9cfU8dFPah-8e6hv4NBxBDa60z6SdFwOs7bOGcqGTkdR9qVY1NZG_kccn5J8sDnmS5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@funhiphop
| reza</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/funhiphop/75914" target="_blank">📅 05:06 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75913">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAli .</strong></div>
<div class="tg-text">داداش من خودم قایق مین گذاریم ولی بحث بحثه وطنه</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/funhiphop/75913" target="_blank">📅 03:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75912">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">خلاصه اتفاقات به زبان ساده:
تو ۲۴ ساعت گذشته سپاه در جهت اطمینان از روند مثبت مذاکرات، سعی کرده با چند تا قایق تو تنگه مین بیشتری بکاره و با موشک‌های زمین به هوا هم جنگده‌های آمریکا رو بزنه.
آمریکا هم برا نشون دادن حسن نیتش و امتیاز دهی، اون چند تا قایق مین گذار و اون پایگاه موشکی‌ای که ازش موشک‌های زمین به هوا لانچ شده بودن رو نابود کرده.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/funhiphop/75912" target="_blank">📅 02:58 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75911">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">یک مقام آمریکایی درمورد روند کاملا طبیعی آتش‌بس به الجزیره:
ایران در ۲۴ ساعت گذشته تلاش کرده است به نیروهای آمریکایی حمله کند که یکی از این حوادث شامل شلیک موشک به جنگنده‌های آمریکایی بود، ولی هیچ نیروی آمریکایی در نتیجه این حملات آسیب ندیده‌اند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/funhiphop/75911" target="_blank">📅 02:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75910">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">سخنگوی سنتکام درمورد زد و خوردهای امشب به فاکس نیوز: نیروهای آمریکایی امروز در جنوب ایران حملات دفاعی انجام دادند تا از نیروهای خود در برابر تهدیدات نیروهای ایرانی محافظت کنند. اهداف شامل سایت‌های پرتاب موشک و قایق‌های ایرانی بودند که در تلاش برای کاشت مین…</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/funhiphop/75910" target="_blank">📅 02:49 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75909">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">سخنگوی سنتکام درمورد زد و خوردهای امشب به فاکس نیوز:
نیروهای آمریکایی امروز در جنوب ایران حملات دفاعی انجام دادند تا از نیروهای خود در برابر تهدیدات نیروهای ایرانی محافظت کنند.
اهداف شامل سایت‌های پرتاب موشک و قایق‌های ایرانی بودند که در تلاش برای کاشت مین بودند.
فرماندهی مرکزی آمریکا همچنان از نیروهای خود دفاع می‌کند و در عین حال در طول آتش‌بس جاری از خود خویشتن‌داری نشان می‌دهد
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/funhiphop/75909" target="_blank">📅 02:28 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75908">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">سخنگوی وزارت خارجه قطر: گزارش‌هایی که مدعی می‌شوند قطر مبلغ ۱۲ میلیارد دلار به ایران «پیشنهاد» کرده تا تضمین‌کننده حصول توافق باشد، کاملاً بی‌اساس است و توسط طرف‌هایی منتشر می‌شود که به دنبال به شکست کشاندن توافق و تضعیف تلاش‌های دیپلماتیک با هدف کاهش تنش…</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/funhiphop/75908" target="_blank">📅 02:17 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75907">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">الجزیره به نقل از یک منبع خیلی خفن: میانجی‌گری قطری‌ها منجر به تفاهمی با آمریکا درباره دارایی‌های مالی مسدود شده ایران شده است. با حل شدن این مسئله کلیدی، منبع اشاره کرد که احتمال قوی وجود دارد که فردا توافق آمریکا و ایران اعلام شود.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/funhiphop/75907" target="_blank">📅 02:17 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75906">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">نکنه پستای ترامپ دلقک بازی نیستن و همشون واقعیت دارن؟
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/funhiphop/75906" target="_blank">📅 01:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75905">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">رسانه جبهه مقاومتی میدل ایست اسپکتور: قضیه حمله به قایق‌ها از صداهای امشب جداست و مال ۴۸ ساعته پیشه و برای روی گل دکتر عراقچی که مذاکرات به خطر نیوفته رسانه‌ها صبر کردن الان خبرشو کار کردن.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/funhiphop/75905" target="_blank">📅 01:38 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75904">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">رسانه جبهه مقاومتی میدل ایست اسپکتور:
قضیه حمله به قایق‌ها از صداهای امشب جداست و مال ۴۸ ساعته پیشه و برای روی گل دکتر عراقچی که مذاکرات به خطر نیوفته رسانه‌ها صبر کردن الان خبرشو کار کردن.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/funhiphop/75904" target="_blank">📅 01:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75900">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">سید مجید نقطه زن, کاخ سفید رو شخم بزن
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/funhiphop/75900" target="_blank">📅 01:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75898">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">دیگه حتی نیاز نیست اسمشو بنویسم:
اورانیوم غنی‌شده (گرد هسته‌ای!) یا فوراً به ایالات متحده تحویل داده خواهد شد تا به کشور بازگردانده شده و نابود شود یا ترجیحاً، با همکاری و هماهنگی جمهوری اسلامی ایران، در همان محل یا در مکان قابل قبول دیگری، با حضور کمیسیون انرژی اتمی یا معادل آن، این فرآیند و رویداد نابود شود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/funhiphop/75898" target="_blank">📅 01:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75895">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">خبرنگار الجزیره:
یک منبع ایرانی به من گفت که صدای تیراندازی شدید نزدیک بندرعباس پس از هدف قرار گرفتن یک شناور توسط سپاه پاسداران در دریا شنیده شد، و پس از آن جنگنده‌های آمریکایی قایق‌های نیروی دریایی سپاه را در خلیج فارس هدف قرار دادند.
طبق گفته منبع، چندین نفر از پرسنل نیروی دریایی سپاه در این حمله کشته شدند.
این رویداد هنوز در حال ادامه است، منبع گفت.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/funhiphop/75895" target="_blank">📅 01:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75893">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">میدل ایست:  دو قایق تندروی سپاه هدف جنگنده‌های آمریکایی قرار گرفتن و ۴ نیروی سپاه پاسداران کشته شدن.  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/funhiphop/75893" target="_blank">📅 01:02 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75892">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d92631652.mp4?token=Iciy_UlNJNgFlwl62ZZiDSB1B02vxfjoxFgJIgnRLPw9L8p1i2zfvxWt6C7INUrxdPTM0kOrfNJyLNiHvWblEsoXF1D_x4xloOcUCDSIvLTAaWqJtW8WWbpmryr4PbJJQ2jo74QnWo6K1K-dJ6GW7mjtiGE5IiSAeX94tOS68GkNvPFS0ATBExhBcnCgf2fQycS9C3gbucehk8iCKuajgMRbF-DRLc9gUFJgekunwHaT33Dvf61_VO1Y-le4nEpK8lsiKWtJ_yM7Ao3_vEoZD_meWEZh11u6HD5BKZw-JSr7_G5ApECc2TLij58d2iaxfxgvbdR8w1kBr0sonnKqDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d92631652.mp4?token=Iciy_UlNJNgFlwl62ZZiDSB1B02vxfjoxFgJIgnRLPw9L8p1i2zfvxWt6C7INUrxdPTM0kOrfNJyLNiHvWblEsoXF1D_x4xloOcUCDSIvLTAaWqJtW8WWbpmryr4PbJJQ2jo74QnWo6K1K-dJ6GW7mjtiGE5IiSAeX94tOS68GkNvPFS0ATBExhBcnCgf2fQycS9C3gbucehk8iCKuajgMRbF-DRLc9gUFJgekunwHaT33Dvf61_VO1Y-le4nEpK8lsiKWtJ_yM7Ao3_vEoZD_meWEZh11u6HD5BKZw-JSr7_G5ApECc2TLij58d2iaxfxgvbdR8w1kBr0sonnKqDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/funhiphop/75892" target="_blank">📅 00:44 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75891">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">در نظر بگیرید که این چیزا در خاورمیانه کاملا عادیه و دلیلی بر شروع جنگ نیست
باید بگذره ببینیم اوضاع از چه قراره
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/funhiphop/75891" target="_blank">📅 00:43 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75890">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">میدل ایست:
دو قایق تندروی سپاه هدف جنگنده‌های آمریکایی قرار گرفتن و ۴ نیروی سپاه پاسداران کشته شدن.
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/funhiphop/75890" target="_blank">📅 00:41 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75885">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">فک کنم وی پی ان فروشا کودتا کردن نت وصل نشه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/funhiphop/75885" target="_blank">📅 00:22 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75883">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">اگه اینا هم صدای مهمات عمل نکرده باشن فکر کنم همه موشکای آمریکا سالم فرود اومدن تو ایران، هیچکدوم منفجر نشدن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/funhiphop/75883" target="_blank">📅 00:11 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75882">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">تو جزایر سیریک و جاسک هم صدای انفجار گزارش شده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/funhiphop/75882" target="_blank">📅 00:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75881">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAbtin</strong></div>
<div class="tg-text">آتش بسی که نشکسته رو میشه شکست
اما آتش بسی که خودشو زده به خواب نمیشه شکست</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/funhiphop/75881" target="_blank">📅 00:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75880">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">کشور از جنگ جهانی سوم هم در میومد انقدر مهمات عمل نکرده توش پیدا نمیشد، فقط خوشبحالتون که طرفداراتون عقبموندن، هیچوقت هیچی براشون سوال نمیشه</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/funhiphop/75880" target="_blank">📅 00:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75878">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">وحید آنلاین: گزارش هایی از صداهای انفجار در جنوب کشور  @funhiphop | reza</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/funhiphop/75878" target="_blank">📅 23:52 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75877">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">صدای طبل مذاکره است چیزی نیست</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/funhiphop/75877" target="_blank">📅 23:52 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75876">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">وحید آنلاین: گزارش هایی از صداهای انفجار در جنوب کشور
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/funhiphop/75876" target="_blank">📅 23:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75875">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">یک منبع بی‌نهایت آگاه و مطلع نظامی به تسنیم:
طبق بررسی‌های کارشناسی و تفکرات دقیقی که ما انجام دادیم، فهمیدیم حملاتی که طی این چند هفته به امارات صورت گرفته کار اسرائیل بوده می‌خواستن بندازن گردن ما ولی خب فکر اینجاشو نکرده بودن که ما زرنگ‌تر از این حرفاییم و خیلی راحت می‌فهمیم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/funhiphop/75875" target="_blank">📅 23:36 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75874">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">رئیس کمیته امنیت ملی در مجلس:
تا زمانی که ایالات متحده پنج اقدام برای ایجاد اعتماد انجام ندهد، هیچ فایده‌ای در تفاهم و مذاکره با آن نیست.
این اقدامات شامل موارد زیر است:
پایان دادن به جنگ در همه جبهه‌ها، به ویژه لبنان
رفع محاصره آمریکایی و مقابله با دزدی دریایی
اجازه عبور کشتی‌های غیرنظامی از تنگه هرمز با هماهنگی ایرانی
تعلیق تحریم‌های نفتی به مدت ۳۰ یا ۶۰ روز
آزادسازی پول‌های ایرانی مسدود شده
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/funhiphop/75874" target="_blank">📅 23:17 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75873">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">الجزیره به نقل از یک منبع خیلی خفن:
میانجی‌گری قطری‌ها منجر به تفاهمی با آمریکا درباره دارایی‌های مالی مسدود شده ایران شده است.
با حل شدن این مسئله کلیدی، منبع اشاره کرد که
احتمال قوی وجود دارد که فردا توافق آمریکا و ایران اعلام شود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/funhiphop/75873" target="_blank">📅 23:12 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75872">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">روسیه از دیشب سنگین ترین حملات موشکیش در طول جنگ رو به اوکراین کرده، توی حملاتش به پایتخت اوکراین از ۳۰تا موشک معروفش به نام اسکندر هم استفاده کرده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/funhiphop/75872" target="_blank">📅 22:57 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75870">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RxwEzTCMuMHBen24ONHODAFm-D_wforZqL3cSLLHwwz_H-_dlO7jxgtwODhy3ur8Z3wzsLu9IYCoezPpC_lENETG2ik91ANjqHmjwByQ7qaYtDmUusHzyBtPQwhYDLthvJSHAwei88-yqQJ8yEnxfVJgIA2sBgApeMNT8SzLFgjRrx_oGfiMRafRsgLxWkQmUdq9XD55GydlwFwZ9O7ypevB5iu2FM6PljeazE3m-EldDAiVyysFakAn6Ikn4WckE3Icu4OIkAiwsd_A5slpM4BeVR2uX_xop7Qq3uDhME021Hnf1l6FvTUS9MJ-VZldV1Ax0VRtQtTwQjYJ5rx07g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o6dHCwL6PiDuCBYnGuLe5TJHkv2wNon6yBK-4vBEdvBfQDBYsZZ4C2SNEpvMl3mU1PrzXXfx5yQn41ybPGIw8C82Qt2RWkUVWYSFmwwB7X7XDde2g9KFrLDG2wcZB8DVJhxOGnwJuv0Jin7kumfj0vDlbRPyd2p0GuqA6yLtSAjlL2MPWzsxIYbFg9NPhpF8_6MMZzTAdVN0oppiWN6WaNAfoAaLlwN4uhiuwxbNbECSyjevq3AEiU4FXXthDzLcbxwrdovINwUS-iKvnB8wU8tE-yoT5Wnz1KAX5UcjVkEX_frzH29XgC3ccRCwJhXNgLT2jy-G5Bw_OWQ4ZhootA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آردا از دختره سفید تره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/funhiphop/75870" target="_blank">📅 22:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75869">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">نتانیاهو: دستور دادم حزب‌الله نابود شود.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/funhiphop/75869" target="_blank">📅 22:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75868">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">فعلا تا وصل میشه بیایید برید از بات منجی کانفیگ رایگان ۵۰۰ مگی بگیرید پولشو بگایید:
https://t.me/TheMonjiBot?start=cFP8AVPe</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/funhiphop/75868" target="_blank">📅 22:08 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75867">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">تو زندگیم همیشه مثل پزشکیان بودم
هیچوقت کسی جدیم نمیگرفت
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/funhiphop/75867" target="_blank">📅 22:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75866">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">نت برگرده روز اول ۲۰۰ گیگ دانلود میزنم ۲۰۰ هزار تومن میندازم جلو ساقی وی پی انم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/funhiphop/75866" target="_blank">📅 21:53 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75865">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">پشمام معین میخواد واسه باز شدن اینترنت آهنگ بخونه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/funhiphop/75865" target="_blank">📅 21:50 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75863">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">فارس هم تو یه خبر گفته نت دست شعامه و باز نمیشه، تو یه خبر دیگه گفته رئیس جمهور دستور باز شدن نتو به وزیر ارتباطات داده  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/funhiphop/75863" target="_blank">📅 21:43 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75862">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">فارس هم تو یه خبر گفته نت دست شعامه و باز نمیشه، تو یه خبر دیگه گفته رئیس جمهور دستور باز شدن نتو به وزیر ارتباطات داده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/funhiphop/75862" target="_blank">📅 21:40 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75861">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BhkzLzJhfunS2-RA1bzY4oVt_korGh1vH9bLAClc_oDe0kW9MFosgY68Co1VjNVJ7F8Q8Hq0T506EAP3plYnBHZIJFu_h7kTBZucviZiUVWPXcB0g0CT7YSRyVGP4KlyyJIdMPRn-K58GzbPP_9A12rrSlLv4Cla392PywZVHqxUbajOWteXiK5Ns2XjoQ6dn08Puyhp1VJhWZBicp8zsjIdBFc6LFJ5b4Jvvlqglger550N8sye-17-HykJrfIfXfVFVKPhPxDRI-2kj9wHmgHfGa2odewuW2kqyrcBOhYPFW3P6RV77dlLDtpP6H25xEql16cGePFU0kmNxSCOPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسایی: پزشکیان و کابینه اش گوهی نیستن که بتونن راجب وصلی اینترنت نظر بدن یا عملی انجام بدن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/funhiphop/75861" target="_blank">📅 21:25 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75860">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚀
اینترنتی که قرار نیست وسط کار جا بزنه!  اگه از قطعی، کندی و وصل‌نشدن‌های اعصاب‌خردکن خسته شدی، وقتشه یه اتصال پایدار رو امتحان کنی
👇
🛰️
IRAN ORBIT
✔️
اجرای روان روی V2Ray / V2Box
✔️
پایداری بالا روی اپراتورهای مختلف
✔️
مناسب استفاده روزمره، AI، شبکه‌های…</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/funhiphop/75860" target="_blank">📅 21:21 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75859">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CwHIHc8nYjFjbk6vwHNR8Nl-TznLd4_SwFpq8cpNP0r9E5fubaUMQ1pIwtukNgm0WRH01K03t0ROYw62IgAdyj3FqHJi5h26zLO3dmSCyTi9xgigWpQcQXtrHZm7h3V07N5egb_d8WE4h4eVmTgCVDJklhVys90-waLiVbFas5XaAR4aaNsIQgY-CEkVxI8XL-eiaSTlKE2D_LJF7NIrZlDY_cjjFNuIvoWFtXvX9kOHY-ggpXtwUiIBACJ9T23x22LPW9LCwvC3P1jFQSiE1ZuN_mXeJhr6mGgyh-gNniBvxdXRxH6XQO9DBpUfOZafJKLI439DMRVx2770Nyt6Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
اینترنتی که قرار نیست وسط کار جا بزنه!
اگه از قطعی، کندی و وصل‌نشدن‌های اعصاب‌خردکن خسته شدی، وقتشه یه اتصال پایدار رو امتحان کنی
👇
🛰️
IRAN ORBIT
✔️
اجرای روان روی V2Ray / V2Box
✔️
پایداری بالا روی اپراتورهای مختلف
✔️
مناسب استفاده روزمره، AI، شبکه‌های اجتماعی و سایت‌های محدود
✔️
بدون محدودیت تعداد کاربر
✔️
سرعت خوب + اتصال پایدار بدون افت شدید
⚪
1GB = 150
⚪
2GB = 290
⚪
5GB = 700
⚪
10GB = 1300
⚪
20GB = 2500
📎
سفارش:
🛒
@IranOrbitBot
📎
پشتیبانی:
🙎‍♂️
@iranorbitowner
🟠
@IranOrbit</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/funhiphop/75859" target="_blank">📅 21:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75857">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">فارس:
یک منبع در وزارت ارتباطات: مصوبه بازگشت اینترنت به وضعیت قبل از دی‌ماه ۱۴۰۴، دقایقی پیش از سوی رئیس‌جمهور به وزارت ارتباطات ابلاغ شد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/funhiphop/75857" target="_blank">📅 21:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75856">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترامپ:
ما در عملیات خشم حماسی ۱۳ سرباز از دست دادیم تا اطمینان حاصل کنیم که پیشروترین حامی دولتی تروریسم در جهان به سلاح هسته‌ای دست نیابد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/funhiphop/75856" target="_blank">📅 20:49 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75855">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">رئیس شورای هماهنگی تبلیغات اسلامی در تهران:
هنوز هیچ زمان مشخصی برای تشییع سید شهدای انقلاب اسلامی، حضرت آیت‌الله سید علی خامنه‌ای تعیین نشده است و مردم به هیچ وجه نباید به شایعات دشمنان توجه کنند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/funhiphop/75855" target="_blank">📅 20:43 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75854">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‏الحدث به نقل از منابع آگاه :  ‏ جمهوری اسلامی شرط انتقال اورانیوم با غنای بالا ‏به چین را مطرح کرده است.   ‏همچنین احتمال دارد فرمانده ارتش پاکستان به ‏دوحه سفر کند.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/funhiphop/75854" target="_blank">📅 20:28 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75853">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‏رئیس بانک مرکزی جمهوری اسلامی پس از سفر هیئت قطری به تهران برای رسیدگی ‏به پرونده پول‌های مسدود شده، به قطر سفر کرده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/funhiphop/75853" target="_blank">📅 20:24 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75852">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NaGULaLV32k2ihuLMN62C6JptIS9i6HXrIPLjQdY6TJzY0gC_rgExof3fNTFmKKigD4Ekk72eAprvYtFZWaLMjjektRA1b1C2ETs3YRyZa8bzwtXss4siHDY86uyZnUkoUPACu3waS7m1QA3DNF9bgHuBqeqCNUsYSHgcF6TuQeRg2Giq1ix3Rg9hxcNWeBEiZGfRo0bdt9OzvN65OQlB-f6PmDQsgbNRIhMzM49z0v5P9doxZUMbfttdJU3k7ef1mZe1LQArk0Jr8GZi0Xw9-xMnG2IA9DZsLxkQG2JkH8ofwA0HPuE_RKCngYUJr4NNENpqWaCO44lROPODcKHdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای عباس پرتوان برس به داد ما ملت ناتوان
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/funhiphop/75852" target="_blank">📅 20:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75850">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">سینه مرغ ۶۵۰ تومنیو کجای دلم بزارم</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/funhiphop/75850" target="_blank">📅 20:12 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75849">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">منابع به شدت معتبر فان هیپ هاپ:
مقامات
در اسرائیل پیامی از ترامپ دریافت کردند که مذاکرات به جایی نمی‌رسد.
او بین حمله در آینده نزدیک و حمله در حوالی ماه اوت (۶۰ روز دیگر) مردد است.
زمان ترجیحی او در این مرحله، زمان دیرتر (نزدیک به ماه اوت) است.
در اسرائیل مقامات از این موضوع به شدت ناراضی هستند و با توجه به وضعیت در لبنان تلاش می‌کنند او را تحت فشار بگذارند تا زودتر حمله کند، اما فعلاً موفق نشده‌اند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/funhiphop/75849" target="_blank">📅 20:10 · 04 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
