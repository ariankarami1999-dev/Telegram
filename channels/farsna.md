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
<img src="https://cdn4.telesco.pe/file/r5kromcne9Nj0cZiR-SZRkIKjSK-QyDxwMynKPhCn79eqt8lo0uTxd7vQlbPbkgjVZw9hfWzZHXd-mRXl63H4WQBinBEa1rEa63r7J9wtik4DMJq9kLlLgpeV6aXN_JDk65mBeIQTW41s9MF3hkJzgBO7HPNaT-3MPiCEesuHt-vm0GGDHOfzeOkyan-orJvTiblcR8_3r-i31kcBl_8lAGGAIFmhEsPQkGVg6K50AG75pNXqSkNWYN0jFfNGBOqpzsYyAHR29d4ASHaOlbTisb_uwk2ETqkpJXjWi7CZJ-Lu3RqEUPt003Vm-ZK3_ZR78ucdrcffkFpVoVaQaMyqA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-28 15:41:04</div>
<hr>

<div class="tg-post" id="msg-451103">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d2e116197.mp4?token=HvtS87KN-LmJD705mBlxKJnbnfGp5ME7hP_EtTABMfiGpJjqMMD9OgCXgMWIIaTR1H7B-ZwbS7_fK8ai7q_gjUCQWYTvE3m-g-NNQkxRfDUYileP1ad4vxWxDw79L4zBCId-jSKftBYMzR7gcJvKyLq1RHnzoHy9Uv_iCxmy0wR7bq9xuPO5E1Ohs6Foyk7uuhopai0rNNDB0haeJKNvhzAn2lCINUkjYbY9cCA1CRGXkz8BQyRz_EPd-AVPwne2qDbggAraGHICg60OqHQEWCcmzB3UppFRugUrFZnn1Z5fm5HZPejnNcs-mMj5_tNlPO3dUBEk9OUG-4MxEByNVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d2e116197.mp4?token=HvtS87KN-LmJD705mBlxKJnbnfGp5ME7hP_EtTABMfiGpJjqMMD9OgCXgMWIIaTR1H7B-ZwbS7_fK8ai7q_gjUCQWYTvE3m-g-NNQkxRfDUYileP1ad4vxWxDw79L4zBCId-jSKftBYMzR7gcJvKyLq1RHnzoHy9Uv_iCxmy0wR7bq9xuPO5E1Ohs6Foyk7uuhopai0rNNDB0haeJKNvhzAn2lCINUkjYbY9cCA1CRGXkz8BQyRz_EPd-AVPwne2qDbggAraGHICg60OqHQEWCcmzB3UppFRugUrFZnn1Z5fm5HZPejnNcs-mMj5_tNlPO3dUBEk9OUG-4MxEByNVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
آژیرهای خطر در پایتخت و مناطق مختلف اردن به صدا در آمد
.
@Farsna</div>
<div class="tg-footer">👁️ 5 · <a href="https://t.me/farsna/451103" target="_blank">📅 15:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451102">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24a0ea3252.mp4?token=tIS1U7g-mprjwh7o8yRPNUIDd-CuvqTKpu2J4t4uVfP6po1VFgvcILkg_3DRRd85cAIfoRsJfvJdhJbLPx9jw_7IBgAkqlU8JpUlWaFbhTQZOz1GQVSPPlrteSuOZY3NWwpWbqDZlgVaspMN9iISr1LjwzhC9mfX0DGMQXa4hfgn6ie_-PZEEpF5Hp1FBNcA1QqkGKZGkjOoJJr7OQRMojEU4Vz_NYsZU5ub3E_nehx_RFZ-zfToDV8euu_ELyRxmD40cMIEvg1ooWoNV0gSNWaF3kjsx8RLXoaVDr0D7t_N24epPFK_yeR_CvXJsK-c_fW9dhQNKO9V6cAxjuoZng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24a0ea3252.mp4?token=tIS1U7g-mprjwh7o8yRPNUIDd-CuvqTKpu2J4t4uVfP6po1VFgvcILkg_3DRRd85cAIfoRsJfvJdhJbLPx9jw_7IBgAkqlU8JpUlWaFbhTQZOz1GQVSPPlrteSuOZY3NWwpWbqDZlgVaspMN9iISr1LjwzhC9mfX0DGMQXa4hfgn6ie_-PZEEpF5Hp1FBNcA1QqkGKZGkjOoJJr7OQRMojEU4Vz_NYsZU5ub3E_nehx_RFZ-zfToDV8euu_ELyRxmD40cMIEvg1ooWoNV0gSNWaF3kjsx8RLXoaVDr0D7t_N24epPFK_yeR_CvXJsK-c_fW9dhQNKO9V6cAxjuoZng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امیر قلعه‌نویی: برخی افراد در دوران جنگ برنامه‌های خود را تعطیل کردند، به غار رفتند و حالا در جام جهانی دوباره پیدایشان شده
🔹
سؤال من از مسئولان این است که چرا به چنین افرادی تریبون داده شد تا علیه تیم ملی صحبت کنند؟
🔹
می‌گویند مردم تیم ملی را دوست نداشتند،…</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/farsna/451102" target="_blank">📅 15:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451101">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j0X9mCbqWXhvtVpONU-YbJv-7xUUPQjgDj43fio-FweV5jZ7rOnJi03KsOqn78Wz1i8tLX0_dqMaO4hCFkDpt2bKt2yTDw5wK-LNLGiOK4VogExuKZC_iYLTsPPwaRE022FhH-VRxPu51hvp7ptnsaqukjpREYdpb2dWeISu0C8ArX5IrpG-RYl-SR5uhih8jWiQh49pXK4GHMMThwqutI40HRzv_CeWK6LgGh-8AB2b7mSmSB7IJM2iEmN1lidYjPoLZ2ltkrrN65JXm4CnGRrgiEDjRivM2exVB4L5WgFihxQabvJ4C8Wu6pJVhHLwp65fxdfnjm4MUcucy1vdZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
منبع مطلع: تا زمان ادامهٔ شرارت‌های آمریکا تنگهٔ هرمز مسدود خواهد ماند
🔹
یک منبع مطلع در نیروی دریایی سپاه در گفت‌وگو با فارس: درحال‌حاضر هیچ ترددی از تنگهٔ هرمز انجام نمی‌شود؛ هرگونه تلاش برای عبور از تنگهٔ هرمز، به‌ویژه از سوی شناورهای متخلف، با برخورد نیروهای مسلح ایران مواجه خواهد شد.
🔹
تا زمان ادامهٔ اقدامات خصمانه و شرارت‌های آمریکا، تنگهٔ هرمز همچنان مسدود است و هیچ‌گونه مجوزی برای تردد شناورها صادر نخواهد شد.
🔹
در روزهای گذشته برخی شناورها که قصد داشتند با حمایت ارتش آمریکا از این مسیر عبور کنند، با واکنش نیروهای مسلح جمهوری اسلامی ایران روبه‌رو شده‌اند.
🔹
در شرایط کنونی، تردد در تنگهٔ هرمز به صفر رسیده و این مسیر تا زمان تداوم اقدامات خصمانهٔ آمریکا مسدود خواهد ماند و هیچ مجوزی برای عبور شناورها صادر نخواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/farsna/451101" target="_blank">📅 15:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451100">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c0f6f3e05.mp4?token=l0PNuoxjspHwn2-SNzAO6lwxqyBSk0Th9grC77PK1NWl_w5givEs1kGm0Dm5Ib39ytGd5cKzfDOSPvkhb0iQgxpCwq_MrxlSUXwIsKz2LIBrUdVYPYci6JPqgDmcIBmSN8cpPkuCBNWm_YayaNxMNmQEetpyPfPuDmxB4eU0WJ76BfpsYgQT-9b1G7IlTmZ5LAp5DNE9AdfVNk-3MlA8R3QRBnwGAabcKfHGPQHAQmRNlaq81OyYvYcjZVC-SuSDMXUD25M65BVQhXuKinGdyDX6g4eg08VBy6eIj76nAjCF4HVNJHxolaTS3cbyPLo3oSk6OKPWozsx8tTLEg_I4jGlmAqtJS-nfiCrisQKSpi3fD_ZJiDcTOj2CNbezGCaC-N2c4YBn9u15oO-DOujkhzXOSx9uUYSGyTy0nrtl3jouhyfF4XssXIxVdtCiD8N0SteBNJjPScKhFtqunl9ADGaHXDtwlPpe0dbP03fG_KlDc8iD0M89BzriKb7BOCrFonmjpfzD4e-Enh04J7PKxMgbbIIKsLbwb5T1ECSsYWc0z2gF816Z3vLiIHTBAQMSnDliF8i51vQr7kQR3PnoWp84g_Yie9nynMt4LsTza-NK3jQDdSDaMG859FFG-8R2PHLBXsbV_NHqagahLExOAwZ4EukCcxjXzDTswlAqsI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c0f6f3e05.mp4?token=l0PNuoxjspHwn2-SNzAO6lwxqyBSk0Th9grC77PK1NWl_w5givEs1kGm0Dm5Ib39ytGd5cKzfDOSPvkhb0iQgxpCwq_MrxlSUXwIsKz2LIBrUdVYPYci6JPqgDmcIBmSN8cpPkuCBNWm_YayaNxMNmQEetpyPfPuDmxB4eU0WJ76BfpsYgQT-9b1G7IlTmZ5LAp5DNE9AdfVNk-3MlA8R3QRBnwGAabcKfHGPQHAQmRNlaq81OyYvYcjZVC-SuSDMXUD25M65BVQhXuKinGdyDX6g4eg08VBy6eIj76nAjCF4HVNJHxolaTS3cbyPLo3oSk6OKPWozsx8tTLEg_I4jGlmAqtJS-nfiCrisQKSpi3fD_ZJiDcTOj2CNbezGCaC-N2c4YBn9u15oO-DOujkhzXOSx9uUYSGyTy0nrtl3jouhyfF4XssXIxVdtCiD8N0SteBNJjPScKhFtqunl9ADGaHXDtwlPpe0dbP03fG_KlDc8iD0M89BzriKb7BOCrFonmjpfzD4e-Enh04J7PKxMgbbIIKsLbwb5T1ECSsYWc0z2gF816Z3vLiIHTBAQMSnDliF8i51vQr7kQR3PnoWp84g_Yie9nynMt4LsTza-NK3jQDdSDaMG859FFG-8R2PHLBXsbV_NHqagahLExOAwZ4EukCcxjXzDTswlAqsI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امیر قلعه‌نویی: برخی افراد در دوران جنگ برنامه‌های خود را تعطیل کردند، به غار رفتند و حالا در جام جهانی دوباره پیدایشان شده
🔹
سؤال من از مسئولان این است که چرا به چنین افرادی تریبون داده شد تا علیه تیم ملی صحبت کنند؟
🔹
می‌گویند مردم تیم ملی را دوست نداشتند، اما سؤال من این است اگر دوست نداشتند، پس چگونه در زمان برگزاری بازی‌های ما رستوران‌ها و سینماها مملو از جمعیت می‌شد و دیدارهای تیم ملی جزو پربیننده‌ترین مسابقات بود؟
🔹
در سال ۲۰۰۶ در جام ملت‌های آسیا در ضربات پنالتی حذف شدیم ما را دادگاهی کردند بعد آدم‌های همین آقایان آمدند در پنالتی در همان مرحله حذف شدند و قهرمان ملی شدند.
@Farsna</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/farsna/451100" target="_blank">📅 15:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451099">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🎥
تصاویری که گفته می‌شود مربوط به شلیک موشک‌های بالستیک اتکمز توسط نیروهای آمریکایی از کویت به‌سمت ایران است.  @Farsna</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/farsna/451099" target="_blank">📅 15:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451098">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">قوه‌قضائیه: هیچ زندانی آمریکایی از زندان‌های ایران آزاد یا تبادل نشده است
🔹
بامداد امروز دونالد ترامپ در مطلبی از آزادی یک زندانی آمریکایی که به گفته او در زمان دولت بایدن و در سال ۲۰۲۴ بازداشت شده بود خبر داد.
🔹
ترامپ در حالی این ادعا را مطرح کرده است که…</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/farsna/451098" target="_blank">📅 15:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451096">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ABcccIQEMBCR0US8VkNrfFU8j3uyOUOYpGSaimRbMXar8qj_nSzLeZcvRSDilZDT-w8KZ-yiZLIeiO6doRR2eOHcAYnXmg9jhV4-3ppljQAFYk9W7JJbdeX-wAaxuD_yeXrX8-2CEBXYNJPaHeODoJuc1PQJ6kS2tE6Mph-Eia_wFsOvsk6O6DiXSELrpMiZjdxPXeaOYtSngZI3l0yTJlEMcBk_KkFUZarL5EVzz7BQ7T9H7m5cEXBY9oe2xQg8HjTd-QsYps4siLUkqOpGFLEdWJoTOIHFBYhIKQVpT-gCHwqnqdD8mgQOKgr67g8fTMYFLeCBepRChj3otWFRBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
حملات موشکی شدید روسیه به کی‌یف
🔹
مقامات اوکراینی اعلام کردند که روسیه بامداد امروز «یکی از بزرگترین حملات موشکی بالستیک خود را» به پایتخت اوکراین انجام داده است.
🔹
طبق این اعلام، پایتخت اوکراین با حدود ۴۰ موشک بالستیک «اسکندر» و هایپرسونیک «زیرکان» هدف…</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/farsna/451096" target="_blank">📅 14:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451095">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20d32dd0ca.mp4?token=JQld0p5HeqmsKkmPaDZh72MMbZFlb1lm7Ue9md-y9E6lbVweR-FUs_kI90BCpAoLBZFiihBotAGyRTUBSPPzr2c1cw-nK5yci6-GyNQPMcvpu6f5wTyViknftqifLlBGgh_zinHj1251tA1vQgFLxvgPkiONsCZa2k_XqQSZdo2BcboxJmg0RfZI2nV6luYgWxYksZUWEVdRXEQ6sP57a3KfEzH5mOQjgnbLJd3i4xkLRGysCcIXX7QwSzIAIy_su8MswJ0ofqiEicNM1hIJJ9zYajM81pV6BMLbYLbLFX2jKtCPWAwLc6edENyIo9qwW3vV5Np7qGNmhThYM84CFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20d32dd0ca.mp4?token=JQld0p5HeqmsKkmPaDZh72MMbZFlb1lm7Ue9md-y9E6lbVweR-FUs_kI90BCpAoLBZFiihBotAGyRTUBSPPzr2c1cw-nK5yci6-GyNQPMcvpu6f5wTyViknftqifLlBGgh_zinHj1251tA1vQgFLxvgPkiONsCZa2k_XqQSZdo2BcboxJmg0RfZI2nV6luYgWxYksZUWEVdRXEQ6sP57a3KfEzH5mOQjgnbLJd3i4xkLRGysCcIXX7QwSzIAIy_su8MswJ0ofqiEicNM1hIJJ9zYajM81pV6BMLbYLbLFX2jKtCPWAwLc6edENyIo9qwW3vV5Np7qGNmhThYM84CFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون اجرایی رئیس‌جمهور: به دستور آقای پزشکیان برای بررسی و ارزیابی آسیب‌های ناشی از جنگ به استان‌های جنوبی کشور آمده‌ایم.
@Farsna</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/farsna/451095" target="_blank">📅 14:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451094">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e729cb684d.mp4?token=ZJhGsEkZRoLvxBGzsbAw0BJyvSC0P5PqXM7OYIivpoUFPu372kvn65hIetgw7Au0p2d9_lAK-Uza3URqC0vpAQQ4BeYHCF2MfqPLAH2rD30ihp9jhjEfwcXbd4MRuU4iWq7jLo9He4baZSbQmncP9pCxPstiTau2urE8Wr99XMOURN-hjtlAKSUHJGhOu1Vp0QgzB6E4SC3nUI37dedHL59PdJ7UjdM7tJza6yrqU44uj0WNx1HEgpNq7yLUudwA1hfsyuzyl4hbiLG9VYWYt0R_LnqQpoPQ9bUTNGePkjsDgbolT-Hdwz0NYVzFO3CT9lI-TxSguZjx7GTbSD6lsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e729cb684d.mp4?token=ZJhGsEkZRoLvxBGzsbAw0BJyvSC0P5PqXM7OYIivpoUFPu372kvn65hIetgw7Au0p2d9_lAK-Uza3URqC0vpAQQ4BeYHCF2MfqPLAH2rD30ihp9jhjEfwcXbd4MRuU4iWq7jLo9He4baZSbQmncP9pCxPstiTau2urE8Wr99XMOURN-hjtlAKSUHJGhOu1Vp0QgzB6E4SC3nUI37dedHL59PdJ7UjdM7tJza6yrqU44uj0WNx1HEgpNq7yLUudwA1hfsyuzyl4hbiLG9VYWYt0R_LnqQpoPQ9bUTNGePkjsDgbolT-Hdwz0NYVzFO3CT9lI-TxSguZjx7GTbSD6lsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آب‌رسانی سیار به ۲۵ روستای شرق هرمزگان درحال انجام است
🔹
۱۰ هزار نفر از ساکنان روستاهای سیریک و جاسک از ۲ شب گذشته به‌خاطر حملۀ تروریستی ارتش آمریکا به ایستگاه پمپاژ آب از دسترسی به آب آشامیدنی محروم شده بودند.
@Farsna</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/farsna/451094" target="_blank">📅 14:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451093">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5ad108936.mp4?token=bC2rXzkzZvz3U5X8VFA5XmqoX7s7KwfL8WrUm1LQdiDDYMNlNxeCoKz-6jn-1_7HUBOhHUX1GFtSFhtsS2BTjo0N_9Xr_xF0zNcsG9Lxq4COXwYC0xOlLF59rWH_7JLJK06bE9GrmzwFGbnRi6sB4KqzzqfVFeT041YOeuwSpVH0pzusdqosmwVKm2Dtx0g5sExLtA97cKXxQszgz_1-woJkhYmAQpv-V5D8G1n7grTD9ou5s7RkXO-obimjs1G-GdmRzHdzne_iJcFvTZIo6GQeMb4sK_j2HHPb-mGX7ovlxS0qOqlnhQDxiWaafvwx3HjT8_kl_wey6TdmRZ3QVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5ad108936.mp4?token=bC2rXzkzZvz3U5X8VFA5XmqoX7s7KwfL8WrUm1LQdiDDYMNlNxeCoKz-6jn-1_7HUBOhHUX1GFtSFhtsS2BTjo0N_9Xr_xF0zNcsG9Lxq4COXwYC0xOlLF59rWH_7JLJK06bE9GrmzwFGbnRi6sB4KqzzqfVFeT041YOeuwSpVH0pzusdqosmwVKm2Dtx0g5sExLtA97cKXxQszgz_1-woJkhYmAQpv-V5D8G1n7grTD9ou5s7RkXO-obimjs1G-GdmRzHdzne_iJcFvTZIo6GQeMb4sK_j2HHPb-mGX7ovlxS0qOqlnhQDxiWaafvwx3HjT8_kl_wey6TdmRZ3QVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نیروهای آمریکایی در پایگاه‌های کویت درحال جابه‌جایی‌های گسترده هستند
@Farsna</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/farsna/451093" target="_blank">📅 14:37 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451092">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FQeOEIbYQCdJLqcuZnLOL3DLGwCrsmIo-3A3BpDJpdk2UgE7nTMmsxy4ts8HWFWlyPJRFN1sdaIaGYd-Mv6GdmZ5Ig1CiH9fap1y4NA4HYx96hGf6pRkvxH64QsSjBqrVnj9auQoNuTjmAIsl1O0CpaBUDrCb_Sa6bbrEa54GAJna67Qlvcl-UMiv6GRIOXAVbQmwk2k-KiuLt3Z1vOuVqqY4CT2lTT3HuGVTYB7naRS79sBxzpCsHWh1udxR9-IMtvRNCBIZGw8o5OuleQa6oloO41YBzYJ3imaLJmAIgcIFSV786K-EFZ1FbFQQq_rXG3ARklS23qgrcIEbQsyFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تامین‌اجتماعی: حقوق تیرماه بازنشستگان بدون تغییر از فردا واریز می‌شود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/451092" target="_blank">📅 14:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451091">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدرگاه فرهنگ</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d950307861.mp4?token=apVuQ4HEO3ejNI-s-XOByYJiJH8OB1ig1BK-xQzX0YUxMqBBEhIxBFnNclpx1dfXIR8npeaokQ3j9ewn-yHDBLgAf4f7gEBM7jkWxrqZ9n2T4h30GacUvmSkn3rg0w50GSw_lhWhThQgTusHF3DJOnNKi9_FlOoTvUbttvHXCMacwY8nhokgRd-5CHlVTZQNa0w4Bvp9Wj25_guQxuW47MOKvW8Mz08V266o502ls8VoQsDNWoTFFrdQIul9t65MUwRz6RxPf1B_VnNcOlAPZF_6tl9SJep3VVZoIiuBG_7KKDeWS-22ShNzmTokLUHQBx_UcEHdzPvWmVMpQ74IYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d950307861.mp4?token=apVuQ4HEO3ejNI-s-XOByYJiJH8OB1ig1BK-xQzX0YUxMqBBEhIxBFnNclpx1dfXIR8npeaokQ3j9ewn-yHDBLgAf4f7gEBM7jkWxrqZ9n2T4h30GacUvmSkn3rg0w50GSw_lhWhThQgTusHF3DJOnNKi9_FlOoTvUbttvHXCMacwY8nhokgRd-5CHlVTZQNa0w4Bvp9Wj25_guQxuW47MOKvW8Mz08V266o502ls8VoQsDNWoTFFrdQIul9t65MUwRz6RxPf1B_VnNcOlAPZF_6tl9SJep3VVZoIiuBG_7KKDeWS-22ShNzmTokLUHQBx_UcEHdzPvWmVMpQ74IYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
#پوشش_زنده
|مدیرکل فرهنگی شهرداری تهران:میدان آزادی در این شب ها میدان خونخواهی از مستکبرین خواهد بود
مصطفی زیبایی نژاد در چهارمین نشست خبری سوگواره آیینی «محرم‌شهر»:
🔸
محرم شهر در میدان آزادی یکی از میدان هایی است که 139 شب هست در مقابل جنایات دشمن اجتماع دارند
@dargah_farhang</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/451091" target="_blank">📅 14:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451090">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمس‌ پرس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6yfFCvf-qzxyJnve6t7aMah-KpUcZ6yI1IMzu8KQ5HqKGbmNg02wP9DYLuNG35x1F8KPEi2yXl03kqovR7d_aUlyFkbjLyuV5W5rIaGhZxxFpsxpcEeDgc3QuqzNyMzbLn51cGvDlxbhKlxfiWFNJxal7dvGIrk0_ZEvA5F1i8NEgUVcJnFJx6urI9HDavHZoSVNzSwTgJO4-czZZFRYlIcLAFdp-gHXe7ywYpCZOcDO6g-T743ZFYhfubrrf24-9sfARH0QusX0bOW-xtCSXRlGK_k42g-zIwSD2Tt8gjAm0lZ7avhz7sPRwszTYSniqaz12fVdVkHZzb3p_BWOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔰
پایش میدانی پروژه‌های راهبردی مس سونگون توسط مدیرعامل مس ایران/ تأکید بر شتاب‌بخشی به طرح‌های توسعه‌ای
🔻
مدیرعامل شرکت ملی صنایع مس ایران در سفر به مجتمع مس سونگون، با بازدید از پروژه‌های کلیدی توسعه‌ای و زیرساختی این مجتمع، آخرین وضعیت اجرای طرح‌ها را بررسی و بر رفع موانع اجرایی، تسریع در روند تکمیل پروژه‌ها و تحقق برنامه‌های توسعه‌ای شرکت تأکید کرد.
🔹
دکتر سیدمصطفی فیض در ادامه برنامه‌های پایش میدانی پروژه‌های راهبردی شرکت ملی صنایع مس ایران، از مهم‌ترین طرح‌های در حال اجرای مجتمع مس سونگون بازدید کرد و از نزدیک در جریان روند پیشرفت، چالش‌ها و اقدامات اجرایی این پروژه‌ها قرار گرفت.
🔹
مدیرعامل شرکت ملی صنایع مس ایران در این سفر، از پروژه تغلیظ فاز۳ سونگون، طرح‌های ذوب، پالایش، تولید اسید سولفوریک و اکسیژن، پروژه بازسازی واحد هیپ‌لیچینگ و تونل مکانیزه انحراف آب‌های سطحی سونگون بازدید و آخرین وضعیت اجرایی هر یک از این طرح‌ها را مورد بررسی قرار داد.
ادامه خبر در مس‌پرس:
https://mespress.ir/x6RL
@mespress_ir</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/451090" target="_blank">📅 14:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451089">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/farsna/451089" target="_blank">📅 14:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451088">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OLzDOjCK9EH9ebM3V4WlCRfsrfIQlbtW7Q3XVoPMnCqlcJ14uaAaB5IeX7DybDZRqRBCBRuhra2DXwnuEvgWgVG5PS27aQQGkVZPyuJttKY-GJiza1Q6o0ueLmIxClgeE7ele8QLJtzw8uxqca_7TzfAhANXniE8h_aINcyvDpvG_7EQLe1RmJ9JkwCtMtGwFsgjegZue5tIgTKKtCKeFnDpYtrd3AkkF8REj59X6hVs5YxAQQ02Cs8NgRNg_fBrgpq_09dmd63KwgsZ0BcEblfdIT6xOP33H8NAz7Fg_x7rOgqTEBcnFq6BEx2O0-8V8zeYJaDCYZNV7qGvb_rwYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانک مرکزی: فعلاً خبری از افزایش سود بانکی نیست
🔹
پیگیری خبرنگار فارس از بانک مرکزی نشان می‌دهد این بانک فعلاً قصدی برای افزایش نرخ سود سپرده و تسهیلات ندارد و هرگونه تصمیم در این زمینه به شرایط اقتصادی و نتایج بررسی‌های کارشناسی وابسته است.
🔸
بانک مرکزی پیش‌تر اعلام کرده بود همهٔ سناریوهای سیاستی دربارهٔ نرخ سود در کمیته‌های تخصصی درحال بررسی است.
🔹
این بانک گفت که زمان مشخصی برای پایان این بررسی‌ها تعیین نشده و این فرآیند ممکن است ۶ ماه یا حتی بیشتر طول بکشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/farsna/451088" target="_blank">📅 14:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451087">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">حملۀ آمریکا به سایت نیروگاه هسته‌ای دارخوین
خوزستان
🔹
سازمان انرژی اتمی: رژیم آمریکا بامداد امروز (یکشنبه ۲۸ تیر) حوالی ساعت ۳:۳۹، با شلیک چند پرتابه به سایت درحال ساخت نیروگاه دارخوین حمله کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/farsna/451087" target="_blank">📅 14:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451086">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v35f1SvMN-zZAPwix7MM6gal_thc0VXD0x3B848wajFGelu0DznsJBnxXaoQT2aTNox5aFcI6qKa5nKka5joj29_2qw6jtqU5XF8MN8FfFj8hdMKNsrmPyPIixzHSa7N8gAoqyNs5gW-dUhSDsm6Fx74ZZY-XlvQVLhWVrnd0Bo0za8__6lnGlvX3b2k8mwN9TW0TWK-JHU4IsRrThKzyvx6_bDHoLwWf5dgQ2n0uZBWp6Zvvy2-tztogUYMCqzwlqDB8RJUqlfjBu7tlqGddWgf5PsD6MporL2uQoeIF2NTNtHW672Zd0LPVUfd77j159vadGna4783W-5pVo30ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدال مسی و یامال سیاسی شد
🔹
دیدار فینال جام جهانی ۲۰۲۶ میان اسپانیا و آرژانتین، تنها یک رقابت فوتبالی نیست. رسانه‌های صهیونیستی این مسابقه به نمادی از شکاف سیاسی بر سر جنگ غزه و روابط با اسرائیل معرفی کردند؛ تا جایی که نشریه تایمز اسرائیل آن را «جنگ نیابتی سیاسی در زمین فوتبال» توصیف کرده‌اند.
🔹
در هفته‌های منتهی به فینال، دولت آرژانتین به رهبری خاویر میلی، صهیونیست که روابط بسیار نزدیکی با اسرائیل دارد و بنیامین نتانیاهو نیز رسماً اعلام کرد که در فینال از آرژانتین حمایت می‌کند.
🔹
در مقابل، دولت اسپانیا به رهبری پدرو سانچز طی ماه‌های اخیر از منتقدان اصلی سیاست‌های اسرائیل در جنگ غزه بوده و بارها خواستار افزایش فشارهای بین‌المللی بر تل‌آویو شده است. همین تقابل سیاسی باعث شد بسیاری از رسانه‌ها، فینال را فراتر از یک مسابقه ورزشی ارزیابی کنند.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/451086" target="_blank">📅 13:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451085">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🎥
دختر این افسر پلیس چند ساعت بعد از شهادتش به دنیا آمد
🔹
شهید محمد همتی چند ساعت پیش از تولد  تنها فرزندش، در شب ۱۸ دی‌ماه، در میدان علیخانی اصفهان به دست اغتشاشگران به شهادت رسید. @Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/451085" target="_blank">📅 13:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451084">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d813ddecf.mp4?token=U9ViRnkVv2IVhwr9sW6ek4bNIIwYYmJp2Cfo3Y-7Mokqr5BHhtH_a9wioyo40IfRlvvCjMvwHeCkuOQzmyeoEmAweUU51FqB66FCR7NQnQpc0WSD3PkufLv6jNHZ2ftVPyoVWdnekiAADBbJCPUHOcqdrasRm5Cvv6cKYz1OjnfUmvFD2eqnR14iBC5kyleAl6Dn1aCsghbksgcPf1b4CGHp4_vgIXg43Z7Tt3j_jbvUQfW3IncaO2IxLuERo3-vOB8LYnDTsKJANlICgoGL8czb2AhBSh2lIkyNf7hhgM_x2M73vtIuepGT6w3cO71BxifboICDZ5zKjiX_CkCC8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d813ddecf.mp4?token=U9ViRnkVv2IVhwr9sW6ek4bNIIwYYmJp2Cfo3Y-7Mokqr5BHhtH_a9wioyo40IfRlvvCjMvwHeCkuOQzmyeoEmAweUU51FqB66FCR7NQnQpc0WSD3PkufLv6jNHZ2ftVPyoVWdnekiAADBbJCPUHOcqdrasRm5Cvv6cKYz1OjnfUmvFD2eqnR14iBC5kyleAl6Dn1aCsghbksgcPf1b4CGHp4_vgIXg43Z7Tt3j_jbvUQfW3IncaO2IxLuERo3-vOB8LYnDTsKJANlICgoGL8czb2AhBSh2lIkyNf7hhgM_x2M73vtIuepGT6w3cO71BxifboICDZ5zKjiX_CkCC8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی: آتش‌بس اولیه با آمریکا در جلسات کوچک‌تر از شورای‌عالی امنیت ملی پذیرفته شد
🔹
وظیفهٔ تحلیل وضعیت برای جنگ یا آتش‌بس با شورای‌عالی امنیت ملی و وظیفهٔ تصمیم‌گیری دربارهٔ آن با رهبری است. هرکدام از اعضا وظیفهٔ ارائهٔ تحلیل دربارهٔ بخش خودش را داشت. …</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/451084" target="_blank">📅 13:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451083">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1c6f5985e.mp4?token=K3DInE2isE1pzcGJwHmDzOU8b-pdgxRjGL9sFyRdE4Edq5k7WHSIJvgcgYCrObTi94ooFI3cZV2Rzdf3MLKz7xPIWNlc9A3mQse84NPiS5ISWtglMpPvO_FO2lJd3mOogXYe8FsLkV2_-hQA1Uikn0vFjefgFgHnzAU1t62fS682FvHqhWEA2B3qoyvqdNYu6VNPumBO2vsfX0_n1P1vKDqUNGkCus5IVi1Llin68kYhbbcJNclCPts5b0UaEDslK5gjha9MTTtb7wTW-1IGnfUnnq2POoaToSXPGZNTZ8yfj3diXryPvufvu0ZNJESMWFa0prZFPJEILwXekftdOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1c6f5985e.mp4?token=K3DInE2isE1pzcGJwHmDzOU8b-pdgxRjGL9sFyRdE4Edq5k7WHSIJvgcgYCrObTi94ooFI3cZV2Rzdf3MLKz7xPIWNlc9A3mQse84NPiS5ISWtglMpPvO_FO2lJd3mOogXYe8FsLkV2_-hQA1Uikn0vFjefgFgHnzAU1t62fS682FvHqhWEA2B3qoyvqdNYu6VNPumBO2vsfX0_n1P1vKDqUNGkCus5IVi1Llin68kYhbbcJNclCPts5b0UaEDslK5gjha9MTTtb7wTW-1IGnfUnnq2POoaToSXPGZNTZ8yfj3diXryPvufvu0ZNJESMWFa0prZFPJEILwXekftdOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یک میدان نفتی در کویت دچار آتش‌سوزی گسترده شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/451083" target="_blank">📅 13:30 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451082">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Flo3Wdrx9CEKyW4Pz2fobBlGJd6FlJtK1D539gN79WqiDsEy_0WS65ahh7-oFDuasV4V8kFtMO5h2i8HIsgK7zdslkCfkgyv0SmLc9lhwbWucAEMvBhSsT9AyCz9KZeYLysr-0pfU5kJOsckt2dJcs-r1y_kx2gaDQRi3NOsNfEgRU_Tecy1TSzerOEEDNWSEctDRVXOHVUadAqd00hjaHjmyVxdXnVeu3pAV3Yhu67MBAT4V7Qvx1tkhq9g-y2LUXNnKRtEQax0StxxvwW7g0gjT7EKdlbOENueaYZxPbxKt_md6w7JSGKYOEKG8vW1k-SCquLXDc9gFV_nMjjtGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
رهبر معظم انقلاب: از اصولی‌ترین امور، اصرار بر اتحاد مقدّس در همه‌ی سطوح است؛ پرهیز از تفرقه و تنازع وظیفۀ همگانی است
🔹
لازم است به شما مردم باوفا و سرافراز ایران عرض شود که از جمله اصولی‌ترین امور در این برهه، اصرار بر وحدت کلمه و اتحاد مقدّس در همه‌ی…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/451082" target="_blank">📅 13:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451081">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aef42aff8c.mp4?token=mWd6NmHc_Pu4FafrmB-kGdhLPJRcFpKb8vy3wVnWsR_qSoa53xKWeysO1Wp34RoSXiGD8tJW0_oUypjFLjeozZ4v2n0Iy_5w-XQlr8JvU1hgzEirxxtIRcprVsrkMOOxrxz_0OuLsYjI6-rfjdWBFVI8fDYI9xxsyC6wzK-KhOklNlksfe729UT-Cs9QM4NqZiyRH_llrrACnAEXH8Qps0e5isOQmFssDTQOR1u1WJKdgXa_GHyb3LkVxYWK7thcLGlk6Xu8vUnbVSswOYYzDSRcc-A3LKhn8t2IYwyHLfkc7f-pbHfFqHH_3uEhyO3WxWkEneoc9zOdkCWU6ATTFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aef42aff8c.mp4?token=mWd6NmHc_Pu4FafrmB-kGdhLPJRcFpKb8vy3wVnWsR_qSoa53xKWeysO1Wp34RoSXiGD8tJW0_oUypjFLjeozZ4v2n0Iy_5w-XQlr8JvU1hgzEirxxtIRcprVsrkMOOxrxz_0OuLsYjI6-rfjdWBFVI8fDYI9xxsyC6wzK-KhOklNlksfe729UT-Cs9QM4NqZiyRH_llrrACnAEXH8Qps0e5isOQmFssDTQOR1u1WJKdgXa_GHyb3LkVxYWK7thcLGlk6Xu8vUnbVSswOYYzDSRcc-A3LKhn8t2IYwyHLfkc7f-pbHfFqHH_3uEhyO3WxWkEneoc9zOdkCWU6ATTFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی: آتش‌بس اولیه با آمریکا در جلسات کوچک‌تر از شورای‌عالی امنیت ملی پذیرفته شد
🔹
وظیفهٔ تحلیل وضعیت برای جنگ یا آتش‌بس با شورای‌عالی امنیت ملی و وظیفهٔ تصمیم‌گیری دربارهٔ آن با رهبری است. هرکدام از اعضا وظیفهٔ ارائهٔ تحلیل دربارهٔ بخش خودش را داشت.
🔹
جلسهٔ شورای‌عالی امنیت ملی برای تصویب یادداشت تفاهم با آمریکا از ساعت ۹ شب تا ۳ صبح طول کشید. آتش‌بس اولیه در شرایطی پذیرفته شد که امکان تشکیل جلسهٔ شورای‌عالی امنیت ملی وجود نداشت و شرط آتش‌بس این بود که مبنای مذاکرات، ۱۰ بند پیشنهادی ایران باشد.
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/451081" target="_blank">📅 13:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451080">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">۲ کشتی متخلف در مسیر ناایمن تنگه هرمز دچار حادثه و ۲ کشتی دیگر از ادامه مسیر ناایمن منصرف شدند
🔹
نیروی دریایی سپاه: ساعاتی پیش ۴ فروند کشتی متخلف با شیطنت و حمایت تروریست‌های امریکایی و با خاموش نمودن سامانه‌های ناوبری و بی‌توجهی به اخطارهای پایگاه کنترل تنگه هرمز نیروی دریایی سپاه، قصد اخلال و خروج از تنگه هرمز را از مسیر ناامین داشتند که ۲ فروند از آنها دچار حادثه شده، در جای خود متوقف گردیدند و ۲ فروند دیگر از ادامه مسیر منصرف شدند.
🔹
نیروی دریایی سپاه اعلام می‌دارد که کنترل تنگه هرمز در اختیار کامل این نیرو است و تنها مسیر عبوری ایمن مسیر مشخص شده و اعلام شده است و یک قطره نفت و گاز و کود شیمیایی همانگونه که قبلا گفته شده، بدون هماهنگی و اجازه از تنگه هرمز عبور نخواهد کرد.
🔹
شناورهایی که تحت تاثیر صحبت‌های دشمن آمریکایی قرار می‌گیرند و وارد مسیر ناایمن می‌شوند مطمئنا دچار حادثه خواهند شد.
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/451080" target="_blank">📅 13:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451079">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e24b3ea8cb.mp4?token=TmMIQV9mWVT4lUdvi9Ab1nv7GDusCL4iKQp8OZnak1bp3VPC3bnbfzNCH6RvZ02uwU3Tk1lxlyNy5n5y79pmMKjOgRNRy39qz1UUqfP8bFHMPMd4dGr8t_ufqp33hsIc5fOw0cvRawXweUfPIcV5pYPww9jRSTsMfQCPvjYFqnxjYvN60PMzB5WuoiPc6UKaQef2f4t31l7tg9eh0WsJd55WuRLx-59Y3mLnuPiSiXA9K5tCMlfhwQiXFmIVxUdNa-wGY9YHXqPhldOrLmhtIoaNKeIEB9lA6FM3HUcbchPnjwMNlGTg1OPusGxCkdYKy_Mff43IiuUJJ0QmYTfdtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e24b3ea8cb.mp4?token=TmMIQV9mWVT4lUdvi9Ab1nv7GDusCL4iKQp8OZnak1bp3VPC3bnbfzNCH6RvZ02uwU3Tk1lxlyNy5n5y79pmMKjOgRNRy39qz1UUqfP8bFHMPMd4dGr8t_ufqp33hsIc5fOw0cvRawXweUfPIcV5pYPww9jRSTsMfQCPvjYFqnxjYvN60PMzB5WuoiPc6UKaQef2f4t31l7tg9eh0WsJd55WuRLx-59Y3mLnuPiSiXA9K5tCMlfhwQiXFmIVxUdNa-wGY9YHXqPhldOrLmhtIoaNKeIEB9lA6FM3HUcbchPnjwMNlGTg1OPusGxCkdYKy_Mff43IiuUJJ0QmYTfdtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خضریان، عضو کمیسیون امنیت ملی: کویت بداند وضعیتش در پایان این جنگ عادی نخواهد بود
🔹
حملات از کویت را حملات مستقیم تلقی می‌کنیم و بدانند که به‌صورت ویژه ادبشان خواهیم کرد. @Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/451079" target="_blank">📅 12:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451078">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2f58528b3.mp4?token=j-Q_0c8W5Bkg-v7xfpatYyVfO7MMiM21RF_rdjUV-ZmriQozShP1Pb_SaEAFX4lEjZmzsAGckBGGTjzYuVS-M7qw68L_VLklu_4LVA3Pc_gWJk-5sKlzjCX2EyUfsiAyrH2ZF5mWYPGz9UUDBNOSv8gnqxwUNHbVHnZL_oecpw7oUzi086vMiYwd_JD2HU_lbeRLU552N9NXppxV4tnbSOkgjj7Rf3_lLFGQG-tOm-y31un5j44PimDd8No3jHaj-PH5jOYv35bQUzDMCNwe-dDd2R8kiPWswK1fpICZe_bFZthnHOAwfJoJgPwgXgJFSb8CjE8EbywcNF9LY29CYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2f58528b3.mp4?token=j-Q_0c8W5Bkg-v7xfpatYyVfO7MMiM21RF_rdjUV-ZmriQozShP1Pb_SaEAFX4lEjZmzsAGckBGGTjzYuVS-M7qw68L_VLklu_4LVA3Pc_gWJk-5sKlzjCX2EyUfsiAyrH2ZF5mWYPGz9UUDBNOSv8gnqxwUNHbVHnZL_oecpw7oUzi086vMiYwd_JD2HU_lbeRLU552N9NXppxV4tnbSOkgjj7Rf3_lLFGQG-tOm-y31un5j44PimDd8No3jHaj-PH5jOYv35bQUzDMCNwe-dDd2R8kiPWswK1fpICZe_bFZthnHOAwfJoJgPwgXgJFSb8CjE8EbywcNF9LY29CYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خضریان، عضو کمیسیون امنیت ملی: پاسخ ما به حمله به آسایشگاه ارتش در چابهار برابر نبود؛ بلکه حداقل ۳ برابر بود
🔹
تلفات آمریکا در سوریه بیش از تلفات سربازان مظلوم ما در چابهار بود. @Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/451078" target="_blank">📅 12:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451077">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3595950301.mp4?token=t-szDELbs81mJwHLuX_9dZtNsZZUxCbcwGgRZZbDCBJHA1IH_Z4mGwNaHJf7wdJxMsYrUK_WT5NToArLSCRhmRw8bpbcLW4PRRvaJayziTwmw_2gqeYGzatsJlOEchcFE_NOfcmrQyeoxPFFwWzHrJjl9opyNhjBnKxVkk_EuI7rwNOcivRtIZljUyNvSL5_jTjAz1wtSYq_KF2Q4kLQP5GEVQld8qm2vaKYME7oANSAk_SeO8c0Qlvyp09XqL2l8meYyn6PPsX522QO8lM6cHPm8rSmBW7qcm5tIdz2s_ASPOwjjg_12X_zhkV6GoXfy3e6C6Evwy6vXAyfsljQUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3595950301.mp4?token=t-szDELbs81mJwHLuX_9dZtNsZZUxCbcwGgRZZbDCBJHA1IH_Z4mGwNaHJf7wdJxMsYrUK_WT5NToArLSCRhmRw8bpbcLW4PRRvaJayziTwmw_2gqeYGzatsJlOEchcFE_NOfcmrQyeoxPFFwWzHrJjl9opyNhjBnKxVkk_EuI7rwNOcivRtIZljUyNvSL5_jTjAz1wtSYq_KF2Q4kLQP5GEVQld8qm2vaKYME7oANSAk_SeO8c0Qlvyp09XqL2l8meYyn6PPsX522QO8lM6cHPm8rSmBW7qcm5tIdz2s_ASPOwjjg_12X_zhkV6GoXfy3e6C6Evwy6vXAyfsljQUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خضریان، عضو کمیسیون امنیت ملی: فلسفهٔ حضور ما در جنوب این است که به آمریکا بگوییم «ما آمده‌ایم که پدر شما را دربیاوریم»
🔹
حضور ما فقط برای دفاع نیست. طرح «پاسخ پشیمان‌کننده» درپی حمله به زیرساخت‌ها درحال نهایی‌شدن است. @Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/451077" target="_blank">📅 12:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451076">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t7n1deLXgs-R9m_dTFq3mVFqo3BEJhO41DfTbRZxBZGgawYILHPFygWts60j3NWPkcFwnjoVrGSbvJQV97KNVlweXiATWAvGMUZe3EmNAdPZUn12ct_Voajp7zteCiluMVEMB27qT_XJMy0IXhvx4uYg4mun4vtqrtStguIeZaPRTYmSJSdbzue5qZGRN4_eencH3C9X4Hj8gLYGxcNj3L1iGItH39OQL1R7TVPE7mJvB9-ymzIa6QRDjl-l-0nsqWusFXv2znRjUf7pVLrBK5pnihk8-x2zKFGlo1afQ_y-t7R6qZ2QtEAuLidWd5vnfxDkKrdaskT5JtchcyEyGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاخص کل بورس در پایان معاملات امروز با کاهش ۲۲ هزار واحدی به ۴ میلیون و ۷۵۵ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/451076" target="_blank">📅 12:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451075">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11b7a1178d.mp4?token=eCkjRPWpNVeXdMZb0z2eC_d3iq_OQVdIMkm7Oay9rBd1MNfoeYMiUF4lMViH7zueKIwW242KZNWYW7VtXMGauaP-fTuYAL3LMXMLz0cCDSTFMhp9DI3fcBQ67ERtSfzyZPFiQVSe9lFUUCSSn7d4l9jzTbJZ5Ku3redfGkSucuPnx0u9JdjOvdyH2Xb4cIikIATSlY-AKHEOUrVa3BUL7jSeKsnTkOiMGTCch1GM3uUGItkESx5o48VxR6pvhP2Sq6oY8u3L6NSd8XYmp4m-L5jDsghG0UWHEbKpY5HNfuj-3RM4mVEy4qTF2GMVh0k-BIxUeGrG_Hv5SMOzboCxjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11b7a1178d.mp4?token=eCkjRPWpNVeXdMZb0z2eC_d3iq_OQVdIMkm7Oay9rBd1MNfoeYMiUF4lMViH7zueKIwW242KZNWYW7VtXMGauaP-fTuYAL3LMXMLz0cCDSTFMhp9DI3fcBQ67ERtSfzyZPFiQVSe9lFUUCSSn7d4l9jzTbJZ5Ku3redfGkSucuPnx0u9JdjOvdyH2Xb4cIikIATSlY-AKHEOUrVa3BUL7jSeKsnTkOiMGTCch1GM3uUGItkESx5o48VxR6pvhP2Sq6oY8u3L6NSd8XYmp4m-L5jDsghG0UWHEbKpY5HNfuj-3RM4mVEy4qTF2GMVh0k-BIxUeGrG_Hv5SMOzboCxjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شریعتی، نمایندهٔ مجلس در مناطق مرزی جنوب: آبادان نماد جوانمردی و حصرشکنی است
🔹
پالایشگاه آبادان نماد حصرشکنی نسبت به تحریم است. آمریکا نتوانسته و نخواهد توانست این کشور را محاصره کند. @Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/451075" target="_blank">📅 12:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451074">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
وزارت کشور بحرین: آژیرهای خطر فعال شده و از شهروندان و ساکنان می‌خواهیم که به نزدیکترین مکان امن بروند.  @Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/451074" target="_blank">📅 12:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451073">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9704386c34.mp4?token=tZJVR2N9UyPwH38zItcS_cTz-jaQZavFiv3tnR1HE3yWuMfYJU-cjYiWo3CKOEJTzfOouGIw3BooHDo8fP_eiNDLc8voAdLjQ2J3j-x5UCkeoxJ2bK8L-hm0XanpZTVHyUKB2bfX9mxAiASUeXCpo6oHflIlBl8W6PbSadmHwCm7dLXRAea4Rm5ZW3RuNAdwwl33h7VY7iHeGOr3cHXMprVL7IVpIsDldutNA3u16GXZ7aEmKumWuysVH1jTpbqSpOmHdIjqqLqpjTH1PnbsIkOAde94p1EQc1kMXMx7Ksci36d5LibjJn3LggyIDvIlL2Kq63K1e5trPUBrZHBLUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9704386c34.mp4?token=tZJVR2N9UyPwH38zItcS_cTz-jaQZavFiv3tnR1HE3yWuMfYJU-cjYiWo3CKOEJTzfOouGIw3BooHDo8fP_eiNDLc8voAdLjQ2J3j-x5UCkeoxJ2bK8L-hm0XanpZTVHyUKB2bfX9mxAiASUeXCpo6oHflIlBl8W6PbSadmHwCm7dLXRAea4Rm5ZW3RuNAdwwl33h7VY7iHeGOr3cHXMprVL7IVpIsDldutNA3u16GXZ7aEmKumWuysVH1jTpbqSpOmHdIjqqLqpjTH1PnbsIkOAde94p1EQc1kMXMx7Ksci36d5LibjJn3LggyIDvIlL2Kq63K1e5trPUBrZHBLUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پاک، کارشناس جبههٔ مقاومت: وظیفهٔ ما حفظ جبههٔ مقاومت و پاسداری از خون حاج‌قاسم و شهید نصرالله است.  @Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/451073" target="_blank">📅 12:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451072">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50a85689b0.mp4?token=ChGRRTw19gZJYDz5wHXaPcH4XVIosWNU_8s8A-gXlhLO_jZ5E1c8ajG49-eZviKkfmFAdWygdbxBlDSeToljBhbDPgAmSlKZkizEaQVSyNAdaL1-54bw--i3AUO8CdRZIiRsS_xi_OPF-NPTdYqvFvFutGBJ3-KBkeYSSoP7Zqmr6lcx9fvIfGmfIC057XR6Y3u9CE3icDOF2eQy9aDb6BYgooPIHtDIBku6iqzR3OfdtMXDtEjATy8FvzuwBpdSW86L21T6Qo-2UUXiU1uyTL3AoJQYzjgMD82SUdhM9666F8qwqF4LVx97RCz5mNZqBOOY0bOCurcn5cJixAWCCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50a85689b0.mp4?token=ChGRRTw19gZJYDz5wHXaPcH4XVIosWNU_8s8A-gXlhLO_jZ5E1c8ajG49-eZviKkfmFAdWygdbxBlDSeToljBhbDPgAmSlKZkizEaQVSyNAdaL1-54bw--i3AUO8CdRZIiRsS_xi_OPF-NPTdYqvFvFutGBJ3-KBkeYSSoP7Zqmr6lcx9fvIfGmfIC057XR6Y3u9CE3icDOF2eQy9aDb6BYgooPIHtDIBku6iqzR3OfdtMXDtEjATy8FvzuwBpdSW86L21T6Qo-2UUXiU1uyTL3AoJQYzjgMD82SUdhM9666F8qwqF4LVx97RCz5mNZqBOOY0bOCurcn5cJixAWCCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خانعلی‌زاده، کارشناس مسائل بین‌الملل در مناطق مرزی جنوب کشور: آمریکا که قرار بود امنیت کشورهای عربی را برقرار کنند، امروز توانایی دفاع از پایگاه‌های خودش را هم ندارد.  @Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/451072" target="_blank">📅 12:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451071">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59e2f40d35.mp4?token=g2T6R9B_1uEBM9x-DIh6vtkMJI-hWCMLxykpc9OkiPTVBQ_YvhzFN6L3EUf1O7mF-usdbJaVdLewRwO2uidPDV6HCsZzdGHgFqx1jgwHkPYsil1YOx5T9GoxPqdkgl81Yghzx-XMlWHLsqxLfPeWqrDYYCosT44E1vXgh3rT44CxUVPzz29wiGz7fedZWkrb_-AR097JaFogHztb8pIuAYdRfDJUHiPtYk0uw1oa92blTjh0XcdePOCuH5z7y3M5owjzv5FyN1gjJxpxU1R1qoKRilcvVVmyoQkx6RrYQLS66SemVe5Bgfcp6o53smwN4wvOHw6XRT914eYPWqUYMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59e2f40d35.mp4?token=g2T6R9B_1uEBM9x-DIh6vtkMJI-hWCMLxykpc9OkiPTVBQ_YvhzFN6L3EUf1O7mF-usdbJaVdLewRwO2uidPDV6HCsZzdGHgFqx1jgwHkPYsil1YOx5T9GoxPqdkgl81Yghzx-XMlWHLsqxLfPeWqrDYYCosT44E1vXgh3rT44CxUVPzz29wiGz7fedZWkrb_-AR097JaFogHztb8pIuAYdRfDJUHiPtYk0uw1oa92blTjh0XcdePOCuH5z7y3M5owjzv5FyN1gjJxpxU1R1qoKRilcvVVmyoQkx6RrYQLS66SemVe5Bgfcp6o53smwN4wvOHw6XRT914eYPWqUYMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حدادیان: رهبر امت به ما وعدهٔ پیروزی داده
🔹
مردم‌سالاری دینی در دورهٔ رهبر شهید به بالاترین حد خود رسید و کار را به ملت مبعوث شده سپردند. @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/451071" target="_blank">📅 12:29 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451070">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/767f04b69b.mp4?token=oH6hwtBuIiiGClSfEgrwJR9T9Sl3OstAYSlXX4BXjxafBbslyAP9f0yqyERmNSh2p9vlAeiX-1rHCKLicvYyUmMkXfcLa7mAhwfROEu7lJrsjHk9xQ6BjqR5MKjDCq7dB19hdu4bi318KaNrAbv4cNJPsVd9jnyRCPyvL5YCEf6Z6RpyMC25KxSQqqZNZePMxwsVYqW40Kr9T5ZNE9Vw_NbesLp7eVZVpmNrE7JIjdm_X5SjizwStvip-jbjaCNdaGecTl2UbJ3ZgQ1_O0EG1SQ0aGNBMKGc0s_wyjIW__bj7saX6a38f8L4UEh9rOmyimN0GTrPaiCAP1RZRZd8ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/767f04b69b.mp4?token=oH6hwtBuIiiGClSfEgrwJR9T9Sl3OstAYSlXX4BXjxafBbslyAP9f0yqyERmNSh2p9vlAeiX-1rHCKLicvYyUmMkXfcLa7mAhwfROEu7lJrsjHk9xQ6BjqR5MKjDCq7dB19hdu4bi318KaNrAbv4cNJPsVd9jnyRCPyvL5YCEf6Z6RpyMC25KxSQqqZNZePMxwsVYqW40Kr9T5ZNE9Vw_NbesLp7eVZVpmNrE7JIjdm_X5SjizwStvip-jbjaCNdaGecTl2UbJ3ZgQ1_O0EG1SQ0aGNBMKGc0s_wyjIW__bj7saX6a38f8L4UEh9rOmyimN0GTrPaiCAP1RZRZd8ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دعوت حدادیان از سربازان آمریکایی: پایتان را به کشور ما بگذارید ببینید چه بلایی سرتان می‌آید
🔹
آنهایی که می‌گفتند «نه غزه نه لبنان» خوب بیایند جنوب ایران!  @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/451070" target="_blank">📅 12:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451069">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DkZ7aBkaLt7fv4Bwgg9JGRqpCPlu-XCJFIfVsUdXBtjTpc3PNr2Sw8N-3O6Ah_YX5i_vpb1Mu2ck2YPghU7WXiSL3NAT9ZOcme18NkYsWJC9QHcDJOEkN-G_O-lSSbb5Tsk5I0Mh7CsIfWVR-XubFUKhTy7IR4q6M3x3ld07kw9eW8CD1y8MTyjxE8_EsjbzkH0h173vstiNSxLSB_fiLYX6hFBlHAiC4m7NpD0nCqkJxQdRkVXZ8M1K9IMgaD3FKPLkCsmX2GiRRzer0ikSX1g5evLeN0_CsRmrXXie3K6UTET9ev38MLVQtvFeZWVyOwiBai_8Jom1HLc17-l_yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدار فرمانده نیروی زمینی ارتش با خانوادۀ شهید موسوی
🔹
امیر جهانشاهی: اعتماد امام شهید امت در انتخاب شهید موسوی به ریاست ستاد کل نیروهای مسلح اعتماد به ارتش بود. امام شهید، شهید موسوی را یک فرمانده بزرگ می‌دانستند و در امور نظامی او را تحسین می‌کردند.
🔹
یکی از ویژگی‌های شهید موسوی استکبار‌ستیزی بود. در تمامی توصیه‌ها و سخنرانی‌های شهید موسوی نسبت به مقابله با استکبار تأکید شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/451069" target="_blank">📅 12:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451068">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZecLq3yddwsPMvCZkdB3Jmdb1yrp7DOYwdVzU365f_c3BlhKSOYjMBDBKWNqmzOw_icLF3Y9DeUuZypV1m1KP66uvXMa-auqF493XL_NNWntRJft43zIWcRdJhW15_NR8PPb6D6otcPSgu2GQruMTKDsXAp-IP2LeK6XpgeA5AoDtmxkwa-O2hPC3gUOmHw2e5SsTjRZa6M3kjb-8ptluhcF1JDeozMmKsSlDzvhGM9uIo5CcQHqfl-KmfJvhXNCjocRY2gYLPkF6XZiKDCmDBSFGs4xs_eW7wKmQT3dPIW7Sslizf5kz5U6tekmWV0Xb7XrSkADr3CKoqrvyFxXBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب آزادکاران ایران در بازی‌های آسیایی مشخص شد
🔹
۵۷ کیلوگرم: علی مومنی
🔹
۶۵ کیلوگرم: عباس ابراهیم‌زاده
🔹
۷۴ کیلوگرم: یونس امامی
🔹
۸۶ کیلوگرم: محمد نخودی
🔹
۹۷ کیلوگرم: امیرعلی آذرپیرا
🔹
۱۲۵ کیلوگرم: امیرحسین زارع
🔸
بازی‌های آسیایی ناگویا مهر امسال برگزار می‌شود.
عکس: رسول شجاعی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/451068" target="_blank">📅 12:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451067">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLkbY9SCGHilqFtACyS9U_RWcHQ_b95foj7tieRUtKH7kFgHenvJCKqX7Z-1Bqk7F79rtQuY893gqps6r-xeKhyZyZS64skZNH-vjVNEE2U9KP3h2qivIdJX1eEnHxDGkCD9DIKEONUK7B6spKZGmWclLBR0kSGMLl17nQQJkdmFfFoYjuXSYcNscy3Ao-aVTmRyX3TVJXRKutdclKORiOEN5ZksqFQosJ1TdIXImou1ISgmAYxuaMevFpK-iCVvq3oYo4YhN74v47xPw5Q0_EAkw0PoOE1SbU8yEphuxNuEhBS_SOd33LHNkBs9nGU4z4FcfuokPh1MesZQB0l5Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین برآوردها از میزان شرکت کنندگان در بزرگترین تشییع تاریخ جهان
🔹
مراسم وداع و تشییع پیکر رهبر شهید انقلاب، در یک بازه ۶ ‌روزه و در ۵ شهر تهران، قم، نجف، کربلا و مشهد برگزار شد که با حضور حماسی و کم‌نظیر مردم، به بزرگترین رویداد تشییعی در تاریخ جهان تبدیل…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/451067" target="_blank">📅 12:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451066">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e06a001e7d.mp4?token=uoIP5Gm2b6yqhlsXhkSToNtXcNNDnJ8HQAA3tzRwzNhynn_JbmRdPVjiQDSe2U9DwXG3_eUzLyNbmAuaqZ49ZhakHgZHrA9OjhVZml6avl5PMGi4z4oYZwAEKX9N-Q5-9RuL645kAaxjkAfnN_nh4Tngyzibg4FDrSh2zBr61MLl38kyR8Zaux5PWLtUPQ87VHUT4n9U-fjtzmrsom_MJ_7dsGlof3naOWl7ji1Gz-l0UfRqgQ3IDn24O5DZ1iBRwXf-ADMjsFDYz4ga5opfYXD8N0H_cBhzfp33FyJzyBj_OZBV8wHV49o-lo76GEX7ycADK4ujr8A53_gY1_NpdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e06a001e7d.mp4?token=uoIP5Gm2b6yqhlsXhkSToNtXcNNDnJ8HQAA3tzRwzNhynn_JbmRdPVjiQDSe2U9DwXG3_eUzLyNbmAuaqZ49ZhakHgZHrA9OjhVZml6avl5PMGi4z4oYZwAEKX9N-Q5-9RuL645kAaxjkAfnN_nh4Tngyzibg4FDrSh2zBr61MLl38kyR8Zaux5PWLtUPQ87VHUT4n9U-fjtzmrsom_MJ_7dsGlof3naOWl7ji1Gz-l0UfRqgQ3IDn24O5DZ1iBRwXf-ADMjsFDYz4ga5opfYXD8N0H_cBhzfp33FyJzyBj_OZBV8wHV49o-lo76GEX7ycADK4ujr8A53_gY1_NpdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
انهدام یک فروند پهپاد MQ9 در آسمان بوشهر
🔹
لحظاتی قبل یک فروند پهپاد MQ9 با آتش سامانۀ نوین پدافند پیشرفتۀ نیروی دریایی سپاه در آسمان بوشهر رهگیری و منهدم شد.  @Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/451066" target="_blank">📅 12:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451065">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HHS7FVrytWnDFDrakJsnj5ns_hCqWg1s9qiUU_zvE6Dn-XRq6XTDjT_zqLC5-XPD_2EvshN6mI1ZIafwmrOOwK-LaPjI51Ddk8fQ_BO6vEYr2fPJVgJjFiwp0BvvGf97owcIQ_F66QxyolW1BiS10UYejX8YtqwztQeBSG9-rTFlCWAASMDocgnT9Hu5iENb9UGrjUb7hQuY018pvpivSO_bFUOg8t8m7vZjzVG6Ippve8nWTilaGnXIzxzgC-L5u8bMpQjFpQQ9eM58vCNTpxGxK7KqzLWzNyfX0gNJFyXtTJXdA3sA-YON2X9ME1bE4p4F2_YaoODyiXuzfEyLrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا فرانسه ۶ تایی شد؟
🔹
شکست ۶ بر ۴ فرانسه برابر انگلیس تنها یک باخت نبود؛ این مسابقه به یکی از سنگین‌ترین فروپاشی‌های دفاعی تاریخ فوتبال فرانسه در جام جهانی تبدیل شد.
🔹
تیمی که تا قبل از این مسابقه در شش بازی تنها ۵ گل دریافت کرده بود، در یک شب ۶ بار دروازه‌اش را باز شده دید؛ یعنی بیشتر از کل گل‌های خورده‌اش در طول تورنمنت.
🔗
دلایل فروپاشی خروس‌ها را در
فارس
بخوانید
@Sportfars</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/451065" target="_blank">📅 11:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451064">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1f69b8faa.mp4?token=snLnGI3W08Ib94Tv7XMfY9sUyl3xdTE8vcAm7kAkrKQsfiIplQzd2TEZ4g66m6A5SOb6TmfQFgbmULm4TrPjoQqAscYJHD-DPPDc_VYEKBk4MMdcb2ZOxbo3M2aS_qLjqELEHdrT1t1SqBg9AEcVe3zUnOOzNbXQMvAYSUDSHjjpQEzq6zqaOG0wGz1EGfDaZbNgzSf4-P9SlsVAo6208f7I8YFNdv9u-wA8NOirH5YpEUP8_mAEES_quhPG-GxEh8765YOeSFBsQR6zXg-4P5egSfrKc-250SvKeaDz-CmDz3z1UcyWjVG4CeC6lLEpl6r2darDpWRV6G69B-u76g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1f69b8faa.mp4?token=snLnGI3W08Ib94Tv7XMfY9sUyl3xdTE8vcAm7kAkrKQsfiIplQzd2TEZ4g66m6A5SOb6TmfQFgbmULm4TrPjoQqAscYJHD-DPPDc_VYEKBk4MMdcb2ZOxbo3M2aS_qLjqELEHdrT1t1SqBg9AEcVe3zUnOOzNbXQMvAYSUDSHjjpQEzq6zqaOG0wGz1EGfDaZbNgzSf4-P9SlsVAo6208f7I8YFNdv9u-wA8NOirH5YpEUP8_mAEES_quhPG-GxEh8765YOeSFBsQR6zXg-4P5egSfrKc-250SvKeaDz-CmDz3z1UcyWjVG4CeC6lLEpl6r2darDpWRV6G69B-u76g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ثبت حضور یک قلاده پلنگ در گچساران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/451064" target="_blank">📅 11:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451063">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
وزارت کشور بحرین: آژیرهای خطر فعال شده و از شهروندان و ساکنان می‌خواهیم که به نزدیکترین مکان امن بروند.
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/451063" target="_blank">📅 11:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451062">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/167d0f36a1.mp4?token=Af_p7uTEj1ZDtSgB2ska_qzdvvCPZPZQFF8oqSB1V_-0oZxm_LTojRAXyqEA_SXoaXqdzpXKbNwO6g0s1I4ykZquMYv_RjV99KtrkC8UC-XFbzMxgw7F5c1a-s-VR3k_V8OjbPL4_Fzv4Kf_Z4tWL73A-XgSm_AxsMBCYnf2lLfh6njZUBufdwmoy9mnppNXE0EB01JJu8w_S6DkTwmcTnuHiTHu5vjhXUS7MN3YJdaO8fe7LtqDQzdrir4N8Djsxeh-yXrfn9YqBq65tr3WPlZnsKDuZeZV6cT_hTyDVAAWmMYeHyhLyCuY7aM0ACbP3cWnyxnmxQ1n2S6u7vBeYRFPBD23tTpfxlIToBYhwS7eF9c0NpkwDArvx_nbwNJkG_12uDJXVvzwSKVrGCVt3gH2ta_0kJeOTZRem2VnRFeS5Nip-EfQgInulFRnQXu9pyz8sp68LwI7DQM8ShpciuRme9L22Pojk6YNMHNzD4-inLcKuCTN6F7RXEcPtoNukWgncIdd_MDlJFQr84eIpvgqz4x_8WhVyvdQ7bkW57QizTR7eFB17a00blyyU5es81W4zBnNkBtoCBmSNqSBNeaepy29aZONf7R1shUaRKuo1OYVUYyzHEiPZbef3WmSkP9HIWELUyqIk4EBzwUrmrnhBgemxCf3q2mEQiLlOrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/167d0f36a1.mp4?token=Af_p7uTEj1ZDtSgB2ska_qzdvvCPZPZQFF8oqSB1V_-0oZxm_LTojRAXyqEA_SXoaXqdzpXKbNwO6g0s1I4ykZquMYv_RjV99KtrkC8UC-XFbzMxgw7F5c1a-s-VR3k_V8OjbPL4_Fzv4Kf_Z4tWL73A-XgSm_AxsMBCYnf2lLfh6njZUBufdwmoy9mnppNXE0EB01JJu8w_S6DkTwmcTnuHiTHu5vjhXUS7MN3YJdaO8fe7LtqDQzdrir4N8Djsxeh-yXrfn9YqBq65tr3WPlZnsKDuZeZV6cT_hTyDVAAWmMYeHyhLyCuY7aM0ACbP3cWnyxnmxQ1n2S6u7vBeYRFPBD23tTpfxlIToBYhwS7eF9c0NpkwDArvx_nbwNJkG_12uDJXVvzwSKVrGCVt3gH2ta_0kJeOTZRem2VnRFeS5Nip-EfQgInulFRnQXu9pyz8sp68LwI7DQM8ShpciuRme9L22Pojk6YNMHNzD4-inLcKuCTN6F7RXEcPtoNukWgncIdd_MDlJFQr84eIpvgqz4x_8WhVyvdQ7bkW57QizTR7eFB17a00blyyU5es81W4zBnNkBtoCBmSNqSBNeaepy29aZONf7R1shUaRKuo1OYVUYyzHEiPZbef3WmSkP9HIWELUyqIk4EBzwUrmrnhBgemxCf3q2mEQiLlOrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دعوت حدادیان از سربازان آمریکایی: پایتان را به کشور ما بگذارید ببینید چه بلایی سرتان می‌آید
🔹
آنهایی که می‌گفتند «نه غزه نه لبنان» خوب بیایند جنوب ایران!  @Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/451062" target="_blank">📅 11:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451061">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/976711c4e8.mp4?token=CLD4nXtQ0LbcezWFCKYE8XmHBHKa5np5L-AjfE-h6q3nEzJfqHHpGb2SiG6WCFrvS4VeUtidnsmaQt7SDI7-gnNbOZB-aK5993PGof5felOKlEvxZzgqbOPD-OkVwrwwnKofZnaR7bvLwD8PoaCK9Y2SZwuGmA3433V11S1zOm2maRAIsqnEf6skVQLxKW_HIkzi_b1abPkYbBcrrKk6r6y-tuotmckX-v5Fwde-zayjtWIP3f8UZGgAJf13-iVb9iBgAP1tjwTLGSmlfT-baYHqRMyuYx0A-RhAYTjzrpOF5OOuZhyhhUfSDHh2leiWvw7Me3LFS6VAj7_JyKMmyJi7WeXfmnkP9kFFpFE2MOTKA7XAJs8UIox-lxMj-Fto1dSaepWsJkePOTtdzl5FHuNJ9WksXkaygwV77yfG1dfni8oqJCtTUNSdJYqbd0EcrPy1TtngpLhOPz3wo0iVCbAJfQFFKdia5rbr2T4S9wSmoxmwYq-_O5MZG6qWgrAp5PIoB9tdhhXidbjYtAUWLFbkB1sf2dYSViDMuiv_HsuvQlb2WqZpdfxLWVo2g4M5BOe9UoOS2dcFh-bCNj6hnGQXs-HZSC5-v1l7qMK4_pUm8Oqux_aaH69rJzTnXe51HqS5StUhegyLE2SeYW22rVye2QyZLoWgaZJ5DIs-IMs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/976711c4e8.mp4?token=CLD4nXtQ0LbcezWFCKYE8XmHBHKa5np5L-AjfE-h6q3nEzJfqHHpGb2SiG6WCFrvS4VeUtidnsmaQt7SDI7-gnNbOZB-aK5993PGof5felOKlEvxZzgqbOPD-OkVwrwwnKofZnaR7bvLwD8PoaCK9Y2SZwuGmA3433V11S1zOm2maRAIsqnEf6skVQLxKW_HIkzi_b1abPkYbBcrrKk6r6y-tuotmckX-v5Fwde-zayjtWIP3f8UZGgAJf13-iVb9iBgAP1tjwTLGSmlfT-baYHqRMyuYx0A-RhAYTjzrpOF5OOuZhyhhUfSDHh2leiWvw7Me3LFS6VAj7_JyKMmyJi7WeXfmnkP9kFFpFE2MOTKA7XAJs8UIox-lxMj-Fto1dSaepWsJkePOTtdzl5FHuNJ9WksXkaygwV77yfG1dfni8oqJCtTUNSdJYqbd0EcrPy1TtngpLhOPz3wo0iVCbAJfQFFKdia5rbr2T4S9wSmoxmwYq-_O5MZG6qWgrAp5PIoB9tdhhXidbjYtAUWLFbkB1sf2dYSViDMuiv_HsuvQlb2WqZpdfxLWVo2g4M5BOe9UoOS2dcFh-bCNj6hnGQXs-HZSC5-v1l7qMK4_pUm8Oqux_aaH69rJzTnXe51HqS5StUhegyLE2SeYW22rVye2QyZLoWgaZJ5DIs-IMs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شرایط اعزام به جنوب را فراهم کنید!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/451061" target="_blank">📅 11:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451060">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7Zg6eh9Fymx3012fGxPAl8KwQNfAgsHQufje5AVSHgYW6Fe9aYkxFAPL2e-sHjvgA2e0GlQJYVgWJXSjlQ8LKkQykoGEYEf9QXQTb87SYCzLlh8Zsw8O38PmKOQgrJ5-wwC_63ZEx8N-kjfXJ7IGo_eL_1epWtv0aHmuD70w6imT8ONm0O1ODjwkD0cmHUJdoWrTXn2nwZD2hQGeJKkbtrPfNgWCx4iJ-7ewRUq6nhywISl-cU-zVqpizjOuzZZr16Wjv5U2opRZHmqMxZf9OdYgQwWRpDAwaYFX9dbei1tX5-tTyRW03gmolAYx14m4zZnXV57s3clncdjjIkCLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ انهدام چندین هواپیمای نظامی آمریکایی در حملات ایران به اردن
🔹
روزنامۀ وال‌استریت ژورنال به نقل از مقام‌های آمریکایی گزارش داد که در حملات موشکی و پهپادی ایران در روزهای گذشته به پایگاه موفق السلطی اردن که با تلفات گستردۀ نظامیان آمریکایی همراه بود، چندین…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/451060" target="_blank">📅 11:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451059">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d92f76bf7c.mp4?token=OkopyrOA37r9IH8QPh7jUSkcUFNdcfDEE3dBftd4DMyto4Dgd14sFA2fW9nlG9wDuHqbrCF5GeQh-MrwWH7OeHsLeW8GCA3TEvzZL_ZrPScFXzOLILWTr8myJgJKHJFJoMFw0gylSAtpcZOMCEE1rP2EB7rj1pPpLAOKFzlb9LxQqPgBAu5f8zMQGlIBcWXV3Qa-A_DM7FJGKdk0gELW7YvPALkWED-GJKwaxxm2brp-7-BKZhRpIfXWFikvxQc0HwW4IOQyxuU1OKa1Vb02RaYUGJGF1cQUa3iyqLvPTfAVW-Qmb2QqRuAMuaHrH_LrrUYxCIfHHlMjBaoO_XpQZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d92f76bf7c.mp4?token=OkopyrOA37r9IH8QPh7jUSkcUFNdcfDEE3dBftd4DMyto4Dgd14sFA2fW9nlG9wDuHqbrCF5GeQh-MrwWH7OeHsLeW8GCA3TEvzZL_ZrPScFXzOLILWTr8myJgJKHJFJoMFw0gylSAtpcZOMCEE1rP2EB7rj1pPpLAOKFzlb9LxQqPgBAu5f8zMQGlIBcWXV3Qa-A_DM7FJGKdk0gELW7YvPALkWED-GJKwaxxm2brp-7-BKZhRpIfXWFikvxQc0HwW4IOQyxuU1OKa1Vb02RaYUGJGF1cQUa3iyqLvPTfAVW-Qmb2QqRuAMuaHrH_LrrUYxCIfHHlMjBaoO_XpQZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
علیرضا دبیر: ما به جنوب کشور آمده‎ایم که بگوییم نوکرتان هستیم
🔹
من جزو کشتی‌گیرهای ایرانی هستم که به آمریکایی‌ها نباختم. آمریکایی بردن خیلی راحت است، شومن‌های خوبی هستند، ده‌شان را صد نشان می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/451059" target="_blank">📅 11:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451058">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZ_SztFPMsWjXHcIzcSIyrtU_NuaSWN6lSOWqhbwRPg7DaY8Bs-LggNGhx3JCmA2nQcVyF7mwcN3Ag9noeiouqRw79bSAmGD6HMCQe0ac5mXkEeIu159rCD6WzUycme0td5YdaWsfor2LREtPm_Z7hLUjMADoRcd33e0E4i2ePCHpHvTsyjDaNVjHtjJNQAHqPvy4hYhu0dhhz6wmH1bbTSOsSFHt0ElU3vDixEwiCoTZALPlYT2FHQv3H8FRq8Yp-r-uApYdNxlR6ZrJ5NDwUOtEYBHAAuYugQSnRSJAmOIN0iduQ8TRpiB8rpE2sBQn3x2luTItxQ9E3yTvvGjSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل به‌دنبال ممنوعیت پرواز پهپادهای شخصی از ترس ترور مقامات
🔹
کابینه سیاسی-امنیتی اسرائیل در حال بررسی طرحی است که بر اساس آن پرواز تمامی پهپادهای شخصی به مدت شش ماه در سراسر اراضی اشغالی ممنوع می‌شود؛ اقدامی که به گزارش رسانه صهیونیستی اسرائیل هیوم، پس از هشدار مقام‌های امنیتی و با استناد به خطر حمله به شخصیت‌های ارشد اسرائیلی مطرح شده است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/451058" target="_blank">📅 10:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451057">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38efd958d1.mp4?token=A3cgmdKUrYAkp3LcQfQ34Adbt59FT4D5pjxqEn1LPyBjWQYNE-i7s2yu6FsNWI1_uXOmp-VdAeW8h0WNzPYkTfzrVUehn6PZXLSGa94QJeQlT7WgJnPyeuwYT48LGv4EKGUdGlApqW7WaVN_n5NfXgXS3W8gwSWph6j0e6uK8Yg3KmIiQVMtQibWM-kF8bXzZlK16zns6C9y5SfPaXfpWjGsSkQ2MhwDyKEo8X6Ep2tvJN0UX_nIxc4CV_TiQ3in0-CX4v8pHo8oTiSLh3ySQVQqFwmA3KDd1FNRASms1Q2UhcZbQePRE4jfSKXPuQM5ZIt144lgIpCz8zseGwopbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38efd958d1.mp4?token=A3cgmdKUrYAkp3LcQfQ34Adbt59FT4D5pjxqEn1LPyBjWQYNE-i7s2yu6FsNWI1_uXOmp-VdAeW8h0WNzPYkTfzrVUehn6PZXLSGa94QJeQlT7WgJnPyeuwYT48LGv4EKGUdGlApqW7WaVN_n5NfXgXS3W8gwSWph6j0e6uK8Yg3KmIiQVMtQibWM-kF8bXzZlK16zns6C9y5SfPaXfpWjGsSkQ2MhwDyKEo8X6Ep2tvJN0UX_nIxc4CV_TiQ3in0-CX4v8pHo8oTiSLh3ySQVQqFwmA3KDd1FNRASms1Q2UhcZbQePRE4jfSKXPuQM5ZIt144lgIpCz8zseGwopbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
علیرضا دبیر: ما به جنوب کشور آمده‎ایم که بگوییم نوکرتان هستیم
🔹
من جزو کشتی‌گیرهای ایرانی هستم که به آمریکایی‌ها نباختم. آمریکایی بردن خیلی راحت است، شومن‌های خوبی هستند، ده‌شان را صد نشان می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farsna/451057" target="_blank">📅 10:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451056">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">تردد در جادهٔ هراز فردا و پس‌فردا ممنوع است
🔹
پلیس‌راه مازندران: جادهٔ هراز در روزهای ۲۹ و ۳۰ تیر از ساعت ۸ تا ۱۷ برای اجرای عملیات لق‌گیری و ریزش‌برداری سنگ‌های ناپایدار به‌طور کامل مسدود است؛ رانندگان در این مدت از مسیرهای کندوان و سوادکوه تردد کنند.
@Farsna</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/451056" target="_blank">📅 10:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451055">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e97d26e7e.mp4?token=QhSW7y4j4vw-YoIGmoovWRrePSExnAVxidOKvzJz9I2GjLlzBnrdslEsZkYhtNXM1IJy-P3PwkGGTtGHe-PAquJFFp6v1UwoLmiSYE6lOPViSX5zlEwZ4biMzI55pW27FtsZVg32gsZ5egrKh30fLOHGA_fJ071px5ij7lvvFvPe1PMsqHWN63BrLrx5zQoW390HVDFehnXs-j_iSyOXu_-bAOQpbb0egqxQTshg2JNN9CEMSiPtJUd7oMLCAt5712zxWmLuhUo4KrjXsWY66DccsU9-ZsWHQ0NE8oapNzRUss44sYtFJjlKzBATuQlG3X0ATajXjY0jbmH-l1Orxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e97d26e7e.mp4?token=QhSW7y4j4vw-YoIGmoovWRrePSExnAVxidOKvzJz9I2GjLlzBnrdslEsZkYhtNXM1IJy-P3PwkGGTtGHe-PAquJFFp6v1UwoLmiSYE6lOPViSX5zlEwZ4biMzI55pW27FtsZVg32gsZ5egrKh30fLOHGA_fJ071px5ij7lvvFvPe1PMsqHWN63BrLrx5zQoW390HVDFehnXs-j_iSyOXu_-bAOQpbb0egqxQTshg2JNN9CEMSiPtJUd7oMLCAt5712zxWmLuhUo4KrjXsWY66DccsU9-ZsWHQ0NE8oapNzRUss44sYtFJjlKzBATuQlG3X0ATajXjY0jbmH-l1Orxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی جبهۀ پایداری: مشکل ما اصل مذاکره نیست، طرف مذاکره است
🔹
متقی‌فر: این جبهه اصل مذاکره را ابزاری قابل استفاده می‌داند، اما مذاکره با رئیس‌جمهور فعلی آمریکا امری بیهوده است.
🔹
مذاکره با ترامپ نباید صورت بگیرد، زیرا او فردی قابل اعتماد نیست؛ انتظار مردم این است که مسئولان این موضوع را همواره مدنظر قرار دهند.
@Farsna</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/451055" target="_blank">📅 10:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451053">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">انهدام یک پهپاد MQ9 در اهواز
🔹
دقایقی قبل، یک پهپاد MQ9 با آتش سامانهٔ نوین پدافند پیشرفتهٔ نیروی هوافضای سپاه و تحت کنترل شبکهٔ یکپارچهٔ پدافند هوایی کشور، در آسمان اهواز ساقط شد.
@Farsna</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/451053" target="_blank">📅 10:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451052">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">سپاه چهارمحال‌وبختیاری: به‌دلیل اجرای پروژ‌های عمرانی، احتمال شنیدن صدای انفجار در امروز وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/451052" target="_blank">📅 10:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451051">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BvGLv_0U1JcNpgQRYIYcHJ9Trln_xANV0u_u-IlMoIWpjn7oa4EYIxXZTea54WuxgPZoHo14xO6H9YSX1FGt6J40g20l1S75HcOstpVsNDv-I0mW5eCWB9jNekbmYxdR2gw7t5ojmJcA8ZLxnKw1b9t1kbSGBPdinhi-KZjTBPhKLTuvHShWSkYaaFMUYwEQ08YAC0gzLw2wtOd1h3ERO6-hYoiS-jbLLlLCnEPrefqHj7wo3HH6d6imU1dYQ0tEWxJtuufca6EkOAvN9lEVrcdm-UDIcs0lG4vnr0x16C1ths6KnSFjtyb3aLKcQn5KZQZt_2uk_QQ5bPNv2Um51g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درس‌های فراموش‌نشدنی</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/451051" target="_blank">📅 10:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451050">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‌
🔴
ارتش کویت حملات موشکی و پهپادی به این کشور را تأیید کرد و مدعی شد که «پدافند هوایی با حملات مقابله می‌کند».  @Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/451050" target="_blank">📅 10:04 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451049">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
منابع خبری گزارش کردند که هشدارهای حملهٔ هوایی در کویت فعال شده است.  @Farsna</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/451049" target="_blank">📅 10:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451048">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
منابع خبری گزارش کردند که هشدارهای حملهٔ هوایی در کویت فعال شده است.
@Farsna</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/451048" target="_blank">📅 10:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451047">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mfa2v_hODkcrKbfJWQdlH434BH7mYwTLpdMZQQaK-i4wyj_A2hsvIhKNfFeltPHWg3y6jJFblSHfuJs6CH7SA1ki_-L97d_WrazppfE30314FxDKEyYEEVsiApLeBx-DD2CKn3Nu_PZvVTmYXnT929amwcZG8PCfInTSdP1qeP6j8YlvprunL0tqNyx6KdtSO5uc9uR-zjgHr1TPFI2AM2BYyESckRr_Lyr2-wLBiMIHeDttbV7HboqKwwVEOvmWrnW0Hp3cEt3Z9S9KwIOqsnRbIK0KciKE_amLKhh0jcuicF9Gls6R1ppXrUTai1OhPYw3sF628slYDXNEHHkz7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمین‌لرزه‌ای به بزرگی ۳.۹ ریشتر در عمق ۱۹ کیلومتری زمین، انبار الوم گلستان را لرزاند.
@Farsna</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/451047" target="_blank">📅 09:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451046">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c4d127f77.mp4?token=ZhhLdCthk21afIxnf4jBjI4IWZMd92uVZv6XDVzYrIUxVQgRdDhwsZL-AGF__Ynt9Kn9oZ6oLDchxdKXFkA1Cu0Ri7ztAZ8HCKIG-1ci8dFGcYVaSD_dQIRiPwm24iHbqv7k1_jN_SYgR5LIQAW8Rhv1rXIVsbCwk_UQ7hTSfi0ERl5iLhOFdmMwPiianv_J6m-UUeCo2hGSqxZ4NdGfIFHriIlhTKk-C6s6nMXuWhoI19YLymIshh7NXOnhUiyKo3zr5YM9cRc2ttsW50CWJ1oHQXLqddc_DEgZ17ObpzR7q0ZRIv21VHIoZ_QFoOPGunQuwCF8ne-JkJolWTzDOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c4d127f77.mp4?token=ZhhLdCthk21afIxnf4jBjI4IWZMd92uVZv6XDVzYrIUxVQgRdDhwsZL-AGF__Ynt9Kn9oZ6oLDchxdKXFkA1Cu0Ri7ztAZ8HCKIG-1ci8dFGcYVaSD_dQIRiPwm24iHbqv7k1_jN_SYgR5LIQAW8Rhv1rXIVsbCwk_UQ7hTSfi0ERl5iLhOFdmMwPiianv_J6m-UUeCo2hGSqxZ4NdGfIFHriIlhTKk-C6s6nMXuWhoI19YLymIshh7NXOnhUiyKo3zr5YM9cRc2ttsW50CWJ1oHQXLqddc_DEgZ17ObpzR7q0ZRIv21VHIoZ_QFoOPGunQuwCF8ne-JkJolWTzDOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملات موشکی شدید روسیه به کی‌یف
🔹
مقامات اوکراینی اعلام کردند که روسیه بامداد امروز «یکی از بزرگترین حملات موشکی بالستیک خود را» به پایتخت اوکراین انجام داده است.
🔹
طبق این اعلام، پایتخت اوکراین با حدود ۴۰ موشک بالستیک «اسکندر» و هایپرسونیک «زیرکان» هدف قرار گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/451046" target="_blank">📅 09:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451045">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vY_XSj7qJWaHiDwo4PYoZ3CzgRkVfSRtPPdTBNdp_xe4lHsvDKPf_gljo-43RpZMqK2mQFBqbmNYsOEjxHqQA-XplY_RuzZXLX-FvobSIlgcAvdV801KyZVkQrwJ5xiAh-lxD14blNFWh5JmFlkvocJ7xgR0R2CSEeJv3IBERVTJ9JKRmqzGIyVm-v4gtZE8ftB7yR9NWcJVT_0o5qRdWpGU6NVs7nm7rX0QQ87hsmlyePfXJd3kQJvBf_MNy_COJ1C59giXXxgY2wQqs2dTDbvPgnvHNwpm3qstxlXQdj-H5Z5NDdyVDuxsEYhlaou9Fc631-i_LSdHE-Lw-oS6og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جام جهانی بوی سوخت جت می‌دهد
🔹
جام جهانی ۲۰۲۶ قرار بود جشن جهانی فوتبال باشد؛ اما حالا آمارها نشان می‌دهد پشت ویترین پرزرق‌وبرق این تورنمنت، ردپای سفرهای بی‌وقفه، هزینه‌های سنگین و تناقض‌های بزرگ هم دیده می‌شود؛ تناقضی که شاید بیش از همه، رئیس فیفا نماد آن باشد.
🔹
جیانی اینفانتینو، رئیس فیفا، تنها در طول برگزاری جام جهانی بیش از ۱۱۵ ساعت پرواز داشته و نزدیک به ۶۰ هزار مایل (بیش از ۹۵ هزار کیلومتر) را با جت اختصاصی طی کرده است؛ مسافتی که تقریباً معادل دو و نیم دور گردش به دور کره زمین است.
🔹
این آمار فقط یک عدد نیست؛ نمادی است از جام جهانی‌ای که بیش از هر دوره دیگری به سفرهای هوایی وابسته شده است. از تیم‌ها و هواداران گرفته تا مسئولان فیفا، همه مجبور شدند هزاران کیلومتر میان آمریکا، کانادا و مکزیک جابه‌جا شوند.
🔹
نکته قابل‌تأمل اینجاست که فیفا در اسناد رسمی خود وعده داده انتشار گازهای گلخانه‌ای ناشی از جام جهانی و فعالیت‌های مرتبط را تا سال ۲۰۳۰ به نصف کاهش دهد و تا سال ۲۰۴۰ به انتشار خالص صفر برسد؛ وعده‌ای که با توجه به حجم گسترده سفرهای هوایی در جام جهانی ۲۰۲۶، از سوی منتقدان با تردید مواجه شده است.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/451045" target="_blank">📅 09:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451044">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">سپاه اصفهان: تا ساعت ۱۳ امروز احتمال شنیدن صدای انفجارهای کنترل‌شده در جنوب کاشان وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/451044" target="_blank">📅 09:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451043">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5895571f9.mp4?token=A_ZJyqj-ePAs_3zenUqk5crz_LuqAzLcTDNPYxi8BfOkMh753cDAF7xVDZ5OU5nG0XPdfLMIoRFopvF10IasJEc5ReMxGdsEecVdBJDXWHnqpnswRsnxtfNG4dwhIMJ4PXkuOxUxVQ4A6UYVXUyPgCs7mOTSMHQnnit2DNXl1j6OJ-uEoHw8-1oftU6ARAlc5bgKJhvZZ7oFbxRkUiCxjOi4EyRvzvEAb0SbRvORn8EIZn9Rm73ICkkIa9zTJUV1by-WNDDvVqJoJXNRGqEobewazB4nf_vr85TNdQ7tS5_Ta0fHiH1CHgjrjkQZ03VTKZ7TZxHkU7NiJdHjoW6NAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5895571f9.mp4?token=A_ZJyqj-ePAs_3zenUqk5crz_LuqAzLcTDNPYxi8BfOkMh753cDAF7xVDZ5OU5nG0XPdfLMIoRFopvF10IasJEc5ReMxGdsEecVdBJDXWHnqpnswRsnxtfNG4dwhIMJ4PXkuOxUxVQ4A6UYVXUyPgCs7mOTSMHQnnit2DNXl1j6OJ-uEoHw8-1oftU6ARAlc5bgKJhvZZ7oFbxRkUiCxjOi4EyRvzvEAb0SbRvORn8EIZn9Rm73ICkkIa9zTJUV1by-WNDDvVqJoJXNRGqEobewazB4nf_vr85TNdQ7tS5_Ta0fHiH1CHgjrjkQZ03VTKZ7TZxHkU7NiJdHjoW6NAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنان منتشرنشده از آخرین دیدار سرلشکر موسوی با فرماندهان ارتش
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farsna/451043" target="_blank">📅 09:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451038">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bCrmc83wIkBl7FqzX7usp2EB4_wtyvhPk8OqK4wfc6gmUjulT0_A34TAhE7Or6Yt1BE_r2_gmh-yNRPbUq6_mcudhrkdPomNFsANfpTk3DJIaRrPl9j8i6lp-yMz8kGmgt3Hsx1p79rE8lM5jFv6v2wvaamIWb5wxnVPilV-UOTIt9KLgiptsI2UsTxUsKVORDDp1ilgVCII_SK2x10TbhJJQBlb3R7AetGpSCpf0qqnEh45vPZjA-CxGAISF5-s8jvxOM5tSIJGUs6q1CW-uz5qhbN8gYwJCqdNC_pBYCZI1DSs_i2ctiyVLaZRJERWMWg9auk3376CEaNeISCVnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cTN1S6OGPGgjQgRknePRc-1RbCWSdc6-IZX3EWCNVFJvva0bIP-ja4NJTOQpxz7BOE7ZWFs8txUMQOgNtlX-V9oT3JvTbxm19j1qSB9dCBPawWfT9qg2F7G199rSN0Sj0Ha2WPbeWcHKOezPk7eEZII5_rA7JXou3_TUNlirEZRZDYMFZ1V9xlcF-yiVqjYdMstYPRO19-Gnk6mNd42yfXDkqinbSE1JfNlI2fgn_FO80CY55DmR1sZnLJDrPcltjF07HMgalPPvyTDGuqk54Ye42wWElXNG2X8Oy9xifAkveFiKkfjvlUr2XuizSqFWdAkMu6G44N5Qktk5B8Canw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xpz7EK1I301BRIEXjcAfp7-TknSJgEyBVP2TR9erVrDy6hAcqJ6hYKAiAyV3ZCi9LbjeVR6f0srrhNa5um2AN0sVCH6EdoJlsErAo0E-e4r5yxTUHWtgCuD_kEX7SMbDlAXa3zOMsPjxyZP_HrLa75WatFtGvfA4mszCSbv-AUzjgAy-geRPPK4KaHMhYagVyAD_iV6o1QRdFb38gW7fg31EGQXoiMlE_UXjDcmNLxZ2alz1tk6IHCt9nHDZMGZis7W2rgs4W_fVEUWGPTJNRnqxaWTCiOJoZwa-uQUpddy5wSM9zyfvaduhOZLArMnVjUx-VTzJdzMFzcrY0a5jKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/phvnruPvLd4TIeJFNUQY7zaJYAe1U1dcUTE9W8rZ5wk5fwfQHlYy_JbiEDpmcrlKASzfFTiMFsiLBCI0vQCna8cfQ1Rx0tVOphfvxDYdQJhZg5OPLbREQivDnQBmReSSBSYrcmirRxl4QSNhxGf9vwO-OlnwtESGus-A6YwQJiq_QTSMxpBKlmEtvO3GuJjlS9lRsk6MMRraRRnRteIiRiNkoFVUOOcZNmWuJB1bMkAjjUvrZc0iRPcZrzjKb60G3_l4ZV2UKx5aEuT8LxYc5deBUcf3yA2E5pnm1Q8E4s9EvKcIdPWJmdFsuWvvHZ7hRsaxYOKm6x5e6kuUtFlN8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GWE48xAPGazxMIdPMPhhbTjR8iBnPrLttnk74gyoWR0J4jejdR20u4F-fNKBCO8WEKC5hDWwdenMIn3_5E6SGyXTDHY6YAUEPDdpDS2zCVYS-4v3TTme3NZ9J87rTuzM3DuBC8jEqruqmitsxhZTRY5RSJin--Rn9pqPbsE7PH4iX3zcYkK0aPQBmm4i7Ta4tNQIajlHA-swP_fWI2CkGoQKW9DmhetTKsyxQns5lIgxSm30Nam0uJREth0OIJankhIDzOUL8VQEcMcRNNqCu6kOuGrm0zE3JWVbCD71tH47xCXshzjCqXmquDV7nrxFaNp37hQaRwwU1HIsrhTWYQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
فصل برداشت رُطب در خرمشهر
عکس:
فرید حمودی
@Farsna</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/451038" target="_blank">📅 09:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451037">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0cdc8e19c.mp4?token=MsPdwh0-Zq_34DBD3Wgh8qQfUArwBYI3UxBPk_BJh5PSheHJfqa2Xqe-VIEa3sBM7C7MHcHWOaLIvFN5H6NiVjeH0qoHzIKDL7nabwGdvreKD27yKcLTUL2pvPIlO4TFN1GpFqnzh1WEzo68Czeh_kH_TWRqzggHpncKoL3kARIHtVlUKolztGwUeovPFhHaQhaC4iWJQRokHN9-1jZAvJeDruvpBcwPPDqwGbZP01n69nubUaoIs0DZTJnPFT_uiHtGvyNWpin4iUntiIHGFzckMnTFsVTaH886ysZX9J5crYe30I10uGdFlqI28y56uZ25c6V1L2jxLcx2bJL6pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0cdc8e19c.mp4?token=MsPdwh0-Zq_34DBD3Wgh8qQfUArwBYI3UxBPk_BJh5PSheHJfqa2Xqe-VIEa3sBM7C7MHcHWOaLIvFN5H6NiVjeH0qoHzIKDL7nabwGdvreKD27yKcLTUL2pvPIlO4TFN1GpFqnzh1WEzo68Czeh_kH_TWRqzggHpncKoL3kARIHtVlUKolztGwUeovPFhHaQhaC4iWJQRokHN9-1jZAvJeDruvpBcwPPDqwGbZP01n69nubUaoIs0DZTJnPFT_uiHtGvyNWpin4iUntiIHGFzckMnTFsVTaH886ysZX9J5crYe30I10uGdFlqI28y56uZ25c6V1L2jxLcx2bJL6pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادامهٔ حملات پهپادهای ارتش به پایگاه‌های آمریکا در کویت
🔹
ارتش جمهوری اسلامی ایران: در پی نقض معاهدات بین‌المللی و جنایت‌های دشمن مستکبر در مناطق غیرنظامی، ارتش جمهوری اسلامی ایران در مرحلهٔ هفدهم عملیات صاعقه، از بامداد امروز انبار مهمات ارتش تروریستی آمریکا در اردوگاه العدیری و سوله‌های تجهیزات و نفرات این ارتش کودک‌کش در پایگاه ‌علی‌السالم کویت را مجدداً هدف حملات پهپادی قرار داد.
🔹
ارتش تأکید می‌کند که جنگ ما، دفاع از هویت اصیل و تاریخ چندهزارسالهٔ ایران و مردمانی است که در پرتو تعالیم اسلامی نه ظلم می‌کنند و نه ظلم می‌پذیرند؛ بر این اساس، رزمندگان ارتش با اعتقاد عمیق به این آموزهٔ الهی برای دفاع از مردم شریف در مصاف با دشمنان ایران و بشریت محکم و استوار ایستاده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/451037" target="_blank">📅 09:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451036">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">زلزلۀ ۵ ریشتری در سالند استان خوزستان
🔹
ساعت ۵:۵۵ دقیقۀ صبح یکشنبه، زمین‌لرزه‌ای به بزرگی ۵ ریشتر حوالی سالند در استان خوزستان را لرزاند.
🔹
این زلزله در شهرهای مختلف خوزستان از جمله اندیمشک، شوش و اهواز احساس شد.  @Farsna</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/451036" target="_blank">📅 08:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451035">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQtbiyxbxFsFGdqJ6hWzWnfzpSB03e0LcVe6XUXhpMgPHJ0-IuiMe47QkweWWuQ1K10oSF6b48ca9niP0R2D7pDYCWYchjMeSJ8rZsjASgsYyV7FQ8nR29moAZA34Qo7KgYhPXtcXYcZZq-DwOEFhRkx1GTg9m2rGjeZkaHWg6bGQ0VeI-mzb-jYmPmnHhLDZ8zd4XacAf8vaQeW3KoVxhlJfC2wElqW1G5G01ObyFg8ZySmbwVEIMvB-B8NS01e6SCOri3FBsSdB2yGhFI_CsYkrqg-xxZf-tNkXU0Xc3_bZXmrRMn-FHfTeXo3nKekQ1XRFNeGHWtlA_w4imwt1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایپا دوباره محصولات خود را گران می‌کند
🔹
مدیرعامل سایپا با اعلام قریب‌الوقوع‌بودن افزایش قیمت محصولات این شرکت، از مردم خواست منتظر اعلام نرخ‌های جدید باشند.
🔹
در این نامه آمده است که توقف نماد با هدف جلوگیری از ایجاد ابهام در معاملات و حفظ حقوق سهام‌داران…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farsna/451035" target="_blank">📅 08:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451034">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">حاجی‌دلیگانی: با مدیران دخیل در ماجرای دانشگاه علامه باید برخورد شود
🔹
نایب رئیس کمیسیون اصل ٩٠: برخورد با فردی که صرفاً در چارچوب وظیفه شرعی و قانونی خود اقدام به امر به معروف کرده، اقدامی غیرقابل قبول است.
🔹
وزیر علوم باید توضیح دهد که چگونه به جای تقدیر…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/451034" target="_blank">📅 08:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451033">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mqu6hBAw2VibuG7fvActj6ECsr13GpUybqJzHVAH-Zn9t8TNFtyw2_VtJafuT06Kvaz7xkJO8AIO2gU3lEaEhjZIiQHde6HkS024vBbf-WIF4V39Og8XQK4hddrCYo-s-Qmio9JwmugkqiJZJK6hSU_a170-URXLL6u8iwUTw3ek5kmhy78C1opiXsAX6fDRYIMalqyweTq6rqArg9ExmbNF8psXMUtvN4jGZ31jyYguDkxMaJRKRKypZOQWhzLgwUk9COf3TCPkHK_SZqGTC5mELYb6wqDTSTKjtg92AfNssJxc7zeAK-AokHqBkBqurb_Uw_gx8hRzVICAgL4eeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
با پیشنهاد شهرداری و تصویب شورای‌شهر تهران، مترو و بی‌آرتی ۲ ماه دیگر هم رایگان ماند.
🔹
در صورت ادامهٔ شرایط جنگی در کشور، ادامهٔ این طرح ۲ ماه دیگر در شورای‌شهر بررسی خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farsna/451033" target="_blank">📅 08:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451032">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">هرمزگان از برنامۀ خاموشی‌های برق خارج می‌شود
🔹
به‌دلیل شرایط خاص استان هرمزگان در وضعیت فعلی، وزیر نیرو دستورات لازم برای خروج این استان از برنامۀ خاموشی‌های برق را صادر کرد.
🔹
بررسی وضعیت سایر استان‌های جنوبی دارای شرایط مشابه نیز در دستور کار قرار دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/451032" target="_blank">📅 08:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451031">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9-6SywSLZtbkGrXH1Qs_2cOZ56e9BeMofV8JMxkThaeuyFXD6-JROo8FhDB-KY6zHt224C0329-fjsopqsN9Z7dh-M3m7g2YpvO58X8_9nYpUxAuqT6YoS_r6JBoTocccFTNmyabVrqyUOZ0UGbsPxX2uFjBrQRJ4gO8h1doBaMUroePUWvn2Y96HZfQj9AvesUceYfcafPy8iNqy040_F1p_M2RFebnxUM-VaPk1VYY1wDSzamMwUDBapv_IHpMcn7I-Q9d-7ry9Xn1f_KkGnASAErVXKvZw7zknZr0pQcrkF01b3NevLwUygHyJSH_eJ-_znzL5Q3_Ayy2pT7fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میزبانی فردوسی‌پور از کسی که آرزوی عصر حجر برای ایران دارد
🔹
«قرار ما با شما، نه دادگاه، نه بخشش، رقص و پایکوبی روی گور تک‌تک‌تان» این متنی است که علیرضا فغانی در دی‌ماه ۱۴۰۴ منتشر کرد؛ اما این تنها استوری‌ او در دی‌ماه و حوادث بعد آن نبود.
🔹
فغانی که پس از قضاوت در فینال جام‌جهانی باشگاه‌ها عکس ژستش با ترامپ را منتشر کرده بود، زمانی که ترامپ ایران را تهدید به برگرداندن به عصر حجر کرد، باز هم در استوری‌هایی هم صدا با رئیس‌جمهور‌ کودک‌کش آمریکا شد.
🔹
اما فغانی جمعه‌شب،‌ میهمان برنامۀ عادل فردوسی‌پور بود. برنامه‌‎‌ای که در ایران تولید و پخش می‌شود، میزبان کسی بود که طرفدار بازگشت یک مملکت و مردمانش به عصر حجر است.
🔹
البته پیش‌تر خود فردوسی‌پور گفته بود: «ما که با فغانی کیف می‌کنیم، هر کی خواست نکنه!» اما اگر این را بپذیریم که همه در یک جغرافیا زندگی می‌کنیم،‌ کسی که آرزوی نابودی‌اش را دارد،‌ منطقاً نباید این‌چنین مورد استقبال قرار بگیرد.
🔹
حالا اما ظاهراً قبح همه‌چیز آن‌قدر ریخته که فردا اگر علی کریمی را هم دیدیم نباید تعجب کنیم.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farsna/451031" target="_blank">📅 07:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451030">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8cda4d17d.mp4?token=uz4TmpikV9mSXG3yqQk4eoKrW-WxpKt28P6DxEsNqw23Wj0sRv35CXXKtDEq6QYP_n4OxeAAsUPrP7Oz-fRXdyYmTQdIZtXc1cpGiMMFcOUcCdZXBVOSIamUYobIxZev33aUKNYVgVA0RIUypmEwL9c7p6Zk4Z2B__GjRLqT5izXv5myqtkFg4UK8tzFtdzeg97MMjf5GVJaLUh4zlRVS7NTklUvQqFnI7LCdwsPQgqNYlTy_Kt1xX64uMHKuoMb_gJvZIG7MYflnjgHusEzkkfSkORduL1RRP4fU-clNWoH8Myjc7zaGgCnVybeOBdz4hxSJY0Kq3F16Q3kMY1npaZ14C51ytg5C4S6jNWarP0RCc20L9x8n9yoGmD2qQYWZJXVQyIugpRkaqeyxWi5MQyfKOd0s9zZNgn9t7PCRiB5fhktdbVw_QYKBcXAPaaBOhaov_dB_hA7jYZKtvEKMYD3VojuvS14SPCAQvCh3s0l0ssxUUBtrqTYN2kNHYHp470trUsNTzG1YqN1QfK8BkpWE3HdDs0KE5YK3o5PkMYYua_PQp7Up7ABCWTJm0S2B9igKpZOkPNGZEMn1SIR6myGSDE7wnDlhs5GJ6eplLlaJBpw0aGLF_Vmc6l3pNZsZ3k-kSQ4WjCSm68omKpsnc5Z1b9HMVaxeKxkmwgbE00" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8cda4d17d.mp4?token=uz4TmpikV9mSXG3yqQk4eoKrW-WxpKt28P6DxEsNqw23Wj0sRv35CXXKtDEq6QYP_n4OxeAAsUPrP7Oz-fRXdyYmTQdIZtXc1cpGiMMFcOUcCdZXBVOSIamUYobIxZev33aUKNYVgVA0RIUypmEwL9c7p6Zk4Z2B__GjRLqT5izXv5myqtkFg4UK8tzFtdzeg97MMjf5GVJaLUh4zlRVS7NTklUvQqFnI7LCdwsPQgqNYlTy_Kt1xX64uMHKuoMb_gJvZIG7MYflnjgHusEzkkfSkORduL1RRP4fU-clNWoH8Myjc7zaGgCnVybeOBdz4hxSJY0Kq3F16Q3kMY1npaZ14C51ytg5C4S6jNWarP0RCc20L9x8n9yoGmD2qQYWZJXVQyIugpRkaqeyxWi5MQyfKOd0s9zZNgn9t7PCRiB5fhktdbVw_QYKBcXAPaaBOhaov_dB_hA7jYZKtvEKMYD3VojuvS14SPCAQvCh3s0l0ssxUUBtrqTYN2kNHYHp470trUsNTzG1YqN1QfK8BkpWE3HdDs0KE5YK3o5PkMYYua_PQp7Up7ABCWTJm0S2B9igKpZOkPNGZEMn1SIR6myGSDE7wnDlhs5GJ6eplLlaJBpw0aGLF_Vmc6l3pNZsZ3k-kSQ4WjCSm68omKpsnc5Z1b9HMVaxeKxkmwgbE00" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شهید مریم حیدری‌پوری شهید حمله به تپه‌های الله‌اکبر بندرعباس</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farsna/451030" target="_blank">📅 06:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451029">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
حملۀ دشمن آمریکایی به شادگان
🔹
معاون استانداری خوزستان: در پی هجوم دشمن تروریستی آمریکا به خاک کشورمان، یک نقطه در اطراف شهر شادگان مورد اصابت موشک قرار گرفت.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farsna/451029" target="_blank">📅 06:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451028">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TrC6wp56c9dGwEiLwfiEXxJsXIyGrHCXg2kUG2p37AoMpDByKP31OlcKvxKMMglhDQeN26dbtBH--1ep205fher0gcQnhWfKPLw61pUmnDmtz0_S0Z22ORtxDdK7VAEuFhfXUpZA8AyiYTmkgAKUx4V_Oplsg30joz_i8h8CCf7yxDjnD_hOb_b0RNmiMdQY9ZULRg5V4lXhZU3kd4Bfh18pHGUQkUwPt3UZHlFqf_eKtKnhic7xJ-wFP49VFsyKAU_1pfSz86QIfq2EEfVUB07lhN6D7O-6D3vevDyrcFR8US0BPqoG9fhwqvu1TEGRckk0xN5OQBNvqobb8Q89sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلزلۀ ۵ ریشتری در سالند استان خوزستان
🔹
ساعت ۵:۵۵ دقیقۀ صبح یکشنبه، زمین‌لرزه‌ای به بزرگی ۵ ریشتر حوالی سالند در استان خوزستان را لرزاند.
🔹
این زلزله در شهرهای مختلف خوزستان از جمله اندیمشک، شوش و اهواز احساس شد.
@Farsna</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farsna/451028" target="_blank">📅 06:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451027">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db885829ed.mp4?token=V2JOKQQPLpa-zAAFptVI7LmgIAro28NU9eMPePQ_98HoLFPl2XRYAS2aBiOOYD0a3k9Jo2cUotdWPP_0EPa8zuD6DbeQ18kRa3uEt_T6ZkifEAZSy7WtkofiRavowD3I2b6lEgvfZRfLga-xvNqoKgo6vooBWcJ0GAIGRMoM8cqvPghX71GfQMNe2jBZ-tBF7EzpzSmRkdFATyHF6jgmIESpg78rgq2onvOp9CasKsmK167YKyzMsT2NrfryLpN4oR_S9ZX329pllcpLZwwl53hNGE0ceLjkbdvBt7SBh6ZUjFXAz6cYZkb1mlwdbCwHmF_GJ4DtNDsMzYYiY2Zntg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db885829ed.mp4?token=V2JOKQQPLpa-zAAFptVI7LmgIAro28NU9eMPePQ_98HoLFPl2XRYAS2aBiOOYD0a3k9Jo2cUotdWPP_0EPa8zuD6DbeQ18kRa3uEt_T6ZkifEAZSy7WtkofiRavowD3I2b6lEgvfZRfLga-xvNqoKgo6vooBWcJ0GAIGRMoM8cqvPghX71GfQMNe2jBZ-tBF7EzpzSmRkdFATyHF6jgmIESpg78rgq2onvOp9CasKsmK167YKyzMsT2NrfryLpN4oR_S9ZX329pllcpLZwwl53hNGE0ceLjkbdvBt7SBh6ZUjFXAz6cYZkb1mlwdbCwHmF_GJ4DtNDsMzYYiY2Zntg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ارتش: دو پایگاه مهم آمریکا در کویت، آماج حملات پهپاد‌های انهدامی قرار گرفت
🔹
در پاسخ به تجاوزات مکرر دشمن، شهادت هم‌وطنان عزیز و حمله به پل‌ها، زیرساخت‌ها و مناطق غیر نظامی، ساعاتی قبل و در مرحلۀ شانزدهم عملیات صاعقه، ارتش جمهوری اسلامی ایران، انبار مهمات ارتش تروریستی آمریکا در اردوگاه العدیری و رادار پاتریوت و رادار هوایی این ارتش متجاوز در پایگاه علی‌السالم کویت را، آماج حملات پرحجم پهپاد‌های انهدامی خود قرار داد.
🔹
اردوگاه العدیری یکی از پایگاه‌های مهم ارتش تروریستی آمریکا در منطقه و در فاصلۀ ۱۰۴ کیلومتری مرز‌های جمهوری اسلامی ایران و ازمراکز مهم پشتیبانی و تجدید سازمان نیرو‌های آمریکایی است که اخلال در عملکرد این پایگاه تاثیر قابل توجهی بر عملیات‌های پشتیبانی ارتش در منطقه می‌گذارد.
🔹
پایگاه هوایی علی‌السالم نیز از پایگاه‌های مهم، مرکز اصلی ترابری هوایی و دروازۀ ورود نیرو‌های نظامی به منطقه غرب آسیاست که نقش محوری در راهبرد نظامی و لجستیکی ارتش متجاوز آمریکا در منطقه ایفا می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farsna/451027" target="_blank">📅 06:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451026">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">هشدار قرارگاه خاتم‌الانبیا به دشمن: نیروهای مسلح به هرگونه وحشی‌گری پاسخی ویرانگر می‌دهند
🔹
سرلشکر عبداللهی: با تبعیت از فرامین و تدابیر رهبر معظم انقلاب، به شیطان بزرگ و دشمن جنایتکار، عهدشکن و حیله‌گر آمریکایی یادآور می‌شویم هرگونه طمع‌ورزی، زورگویی، تمامیت‌خواهی…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farsna/451026" target="_blank">📅 05:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451025">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">هشدار قرارگاه خاتم‌الانبیا به دشمن: نیروهای مسلح به هرگونه وحشی‌گری پاسخی ویرانگر می‌دهند
🔹
سرلشکر عبداللهی: با تبعیت از فرامین و تدابیر رهبر معظم انقلاب، به شیطان بزرگ و دشمن جنایتکار، عهدشکن و حیله‌گر آمریکایی یادآور می‌شویم هرگونه طمع‌ورزی، زورگویی، تمامیت‌خواهی و وحشی‌گری با پاسخ قاطع و ویرانگر رزمندگان مومن، شجاع و مقتدر در نیروهای مسلح مواجه می‌گردد و هزینه‌هایی سنگین‌تر از جنگ تحمیلی دوم و سوم بر آنان تحمیل می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farsna/451025" target="_blank">📅 05:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451024">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">‌
🔴
افشاگری نیویورک‌تایمز از حملات پی‌در‌پی ایران به پایگاه آمریکا در اردن
🔹
نیویورک‌تایمز: مقامات آمریکایی جزئیاتی از حملات ۵ روز گذشته ایران به اردن ارائه کرده‌اند که پنتاگون هنوز به‌طور علنی دربارهٔ آن‌ها صحبت نکرده است:
🔸
حملهٔ اول: موشک‌ به یک مجتمع مسکونی…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farsna/451024" target="_blank">📅 05:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451023">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66b78212fc.mp4?token=opz_jCmNOJBYYJHaYMx3RyzXPsSBk-5KpnGsZyOVgNW645jGmYR1mHsnvpUq1fcNNlRMnldsuVTVc7rFi7P3bwTWx0kD7fnFcPPupeNG_Y0NP9dD2jrhuYre82KI5zER7cbXoSfj03iX2UW5ddIgRR0PUStMDkXyEvMfWaO19FhKo1D80aHKzQIojHCuSMGJ3MPNREhuHscFF2YP_presNpxopzrwDmXm9NnHfYveStkF31jHruAnoH8CvuuIPMIYcvE5L3ecxu52fKTKNAFwG60wHNc8BWM-Z0P432DqZVvLygqXjpk65Tqw5FOijH4URYkN_QMf_fI9saEkNzxCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66b78212fc.mp4?token=opz_jCmNOJBYYJHaYMx3RyzXPsSBk-5KpnGsZyOVgNW645jGmYR1mHsnvpUq1fcNNlRMnldsuVTVc7rFi7P3bwTWx0kD7fnFcPPupeNG_Y0NP9dD2jrhuYre82KI5zER7cbXoSfj03iX2UW5ddIgRR0PUStMDkXyEvMfWaO19FhKo1D80aHKzQIojHCuSMGJ3MPNREhuHscFF2YP_presNpxopzrwDmXm9NnHfYveStkF31jHruAnoH8CvuuIPMIYcvE5L3ecxu52fKTKNAFwG60wHNc8BWM-Z0P432DqZVvLygqXjpk65Tqw5FOijH4URYkN_QMf_fI9saEkNzxCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شرط قبولی ذکر به نقل از آیت‌الله بهجت
🎙
استاد فاطمی‌نیا
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farsna/451023" target="_blank">📅 04:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451022">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
حملات نظامی دشمن آمریکایی به حوالی قشم
🔹
استانداری هرمزگان: در ساعت ۳:۴۰ نقطه‌ای در حوالی قشم هدف حملۀ نظامی دشمن آمریکایی قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farsna/451022" target="_blank">📅 04:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451021">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ufWrCrw6zT7Wckge4HvxLZ122CGZThN2ImN3BbQzcZesmucXAQnMCtkrk17Jm2ZVnYJNA7SORVT5DtTEf7E8Ug8f7pxBFHOwaaLfPw2DtHyfWHYQDwJgGzT3YBYPS013VJkm5Mj0Cgi3r-3KdnGpztvxuyerq7uliQLqjml-yyd0Qe8rXEa9b51_RWMZ98bkh5ZnAC95AJWQPPKwOFWrkh-N-k6u137px--tRUUTFSwqnQd403udFW5E4DWsrxdmop32srSlaQk4IGy13SoU4eGbvpIOuuBaoGlDiE6ip0nWR7ayZeIKnp0RJT0uPAUp7Cgebl_H-sPZeYP0avaIRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۴ ضربه تا خاموشی هاب امارات
🔹
هرگاه سخن از قدرت اقتصادی امارات به میان می‌آید، معمولاً نگاه‌ها سمت برج‌های بلند دبی، مراکز مالی بین‌المللی و درآمدهای نفتی ابوظبی معطوف می‌شود؛ اما پشت این تصویر، شبکه‌ای از زیرساخت‌های حیاتی قرار دارد که ستون اصلی نقش جهانی امارات را شکل داده است؛ بنادر عظیم، فرودگاه‌های بین‌المللی، مناطق آزاد تجاری و مراکز لجستیکی که این کشور را به یکی از مهم‌ترین گره‌های تجارت، انرژی و حمل‌ونقل جهان تبدیل کرده‌اند.
🔹
از همین رو، پس از هشدار یک مقام نیروهای مسلح دربارۀ ضرورت تخلیۀ فرودگاه‌های دبی و ابوظبی و بنادر فجیره و جبل‌علی در صورت گسترش درگیری، توجه‌ها به اهمیت راهبردی این چهار نقطه جلب شد.
🔹
اختلال گسترده در این مراکز می‌تواند نه‌تنها تجارت و اقتصاد داخلی امارات، بلکه شبکه‌های لجستیکی منطقه، مسیرهای حمل‌ونقل، بازار انرژی و بخشی از زنجیره تأمین جهانی را تحت تأثیر قرار دهد.
🔗
اما اهمیت دقیق این چهار زیرساخت در چیست، و اگر هم‌زمان از کار بیفتند چه رخ می‌دهد؟
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farsna/451021" target="_blank">📅 03:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451014">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CZKtGRzrQPpMhlOohbu5iEhd9AXsCByIb2A14kEVrr9fi30gDqy0AyI1lJncEYzds4uxAXCxZJFcSwpnMgmvQWMiOoqPYjEEudwnHR-vj-UjUj_hDxTzXcHIzsMt8enQQCH-UuUQaOPimPKfg0bnUsLbHdrN9PjhiyAsEcorfqO2CFQ05ADM7kreVTGquXYTnbdJHX94rh9Qy-40hQFwo7RigJzJaWz7GlRsNa1qQmowrZl8j2BsDZN6hTJYJURq0rSgUu7t2MSfFFo888VcKLAcRS5pMchi-eVXUZLzqf-3PSeCvZKqdaLMhwd8fb5ms0bdZD9IFYOWW4ZIzQdE4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lxbmzlPfDvlci7bmnVfC0ywT_d8rMqGYL0MzL0VWCBVat5y6ydbgPLB6_YBwtvY-ccVmlfUBV2gGvLw7vEDAAT0iFOlkmOE0B5NmNC1mhBqFYY3vwWMrQBFdgHiV3m06MnbLVUWmJEaa6b9BjqN0Dx1eQKjb14HtYHAOhQgRa-sO1qdAaNFoX240ZjrIn6LaLwT5mvDKbALi2A3Jpo-74rpa5W7nxDnDKn_9Ft902bfiNdHiw7tG7jYG2JWmuI6HjD01mxygY_As8cAnHIbk8PJBKFZXW7cH9bjCBtug6xeUH-0_HFQSPeiZC8NH_2gMAJ-kmnKKC0FR5TPOJI2AzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L5iXfTb1hFvZPrrAb9ZYuGBtdSY1OjT_K-jiqPPdIBkIdJe-TIYCCL4lYtRvh3tG1RHMFza4lud805-tHbhk3ndYY7_PONV3yennrfwzssMwb_mvir3n2F-nPjkj66nt2Rs0Edhso004dz-xZXohqNLufQp5AvucQM935x6jgjXuNHcBJayN0phDgwlb2FtMv6HCIFzMZ4uAVmpN5JbPIzregxMJAMiVgii6wH2ZJWzKZ_7GmQALdR_I4HP-bjGtLyXTwCKCFI1F0fvNaB7BJBZHi8fb78slCWa2NzNRadHDvfMU-54rxPBeUlsOIr9HUwOy6MEwyblXxuVDmwcyIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kYbwCzo4F9Lrxn-ySUi887du3ajyWW1cXv7bC2YGl_ZPaVZlSI-CL2yehEJeYf43vZQY4zXILLNyvXIup3tvfx2ZNzSIgkD7_hj8Epjgnalapv27xKHH36cn_ktLAtCtFpwvAhTzNuAWqVIrdRxHJVwAHymDNzV5keuvRoY8yxjET8mAQZwR0mlY6XeXwI5e4g32FKd0ZL1piJgPT9bVTRuZ0krEopnOEOKXy7mCkDVOrcdFf8HvmxxpjewAdopDGYWL-mbSPuBH-fiVpZ7JAhvUzlUIfvu_dk171tOufjcx1I3VaR5NvvM2_DXd4GeWgh1QcDkSlSFMmw8J9ySDcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FbtmWY7DmT0bb7FvKu8Sld4SZCTQEuNM2rQjKWVwC42Ep1rAC447hjDsGqa7IdthhsGlKzQwD6oIUJtrfjeh6rIIru_ac1byTs6GVg3cwx2DsnwowV3YsQGby9XDS12D4N6T0GQj10EgXKQ8-iEuNUs3aV5zpB5dtfFPnZVDfWOHDFMnC3hKGCIHgMNn2bhRRQHB_Cd93ZZpedYYF3z--Xe4QG8g68nmmpDiZIzHkAom7MkiLMn8BD-vnpZ8kov9v-iaC7iKrTyJReQO6BJ3Olz-XKkGk8iGJZrJ0Ri5IA_MesPQ3hKTcalyCnIC049oooShcMqbkyAgJ1pkJZRgAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SJRpxpxWXBhhEDyExhvStyOJaZ7Cx3DPX1Oqpk3NTuhMI-oGPZxvhNPQqUxGZjdjAJ4b49WXNgaPCu7v71XEGDORJAU5oVcBbcu8NlnDQT8KeskPktSYLzbHrnsyO9ZiHH7qvM1I7iZbaeK-Bj0Esg1jh6bAM_ZKRxMR1yPVPtJDWR6R4hINVHOFmK5HC8YNVp-5BVWb1SOESh2P0jBvWIJZHZrdpjoqR1aY-OSeQSm2qnX4HaHY8Ja-P3hOkKWWnnmSyCmw5NW3OW7LFWvK-SgHSN_1sAo-aVP68bo0yhgR7zRMeVtyWywPNhW0KL6JEqqv8hYahJdhID7VRrE3jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qSG0Qo5je13Vyk1g2G7Tckwa1i5SMRkl96dhOTh5hVAfp688FFegIEHQMX7Wbv0i9Seo4iYXhyvenF1DqN-oslnewf6lo-w0MNPg-H7G4TLyNg1Uk5pfEOuTTLSa2pxnGPnSYIQD45lY-Lk-BOO95AaMB2X-OspQ9zdskASODrsSY69JgxqBI_LTm7LgSDc0DP0HxUW4jcJrBxjY9Jn700UgRXuOgFUWqj1hQ2XmLaneY6XvyaGPyyIkosDyjG5-zdWvuBFsm9RN0b_3bRL7_N4DENwAZwsqoG7dSiy4yl8s_KT7uvgOo3kyrEtQDCGlxr3-AxtLSzC-SKZIWfbX3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تنگۀ هرمز میراث ایرانیان
عکس:
رهبر امامدادی
@Farsna</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farsna/451014" target="_blank">📅 03:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451013">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCaYEcXMgUCg_7qRSd-I5GVKfDNdSeqCJpY7O9a9rcP829cDxpVt5HOT2kW5sE9ppJ3UlaXlFBKipz7FVOA5lcRA1cV-QZY8qtGO6NjjCGt3T-j-YzO2eRKHd8zQn-KdP3U3b5G7j6Eqkq-DQRNIuHvf7c2ZPSko6aUQBwipjPd6CCtH5A3CiuxjRSJE-trseJ6Ik78hVtgx-AdkTW-VR53S-i7znJN53pH6dKeQmA4BhfT5UazxzNF_2Q-4j4P63N98-G3xSzQXaaP0P8diBOoK8bZ8siBF1-KAYxyIXYWN43S14pdeQoY7VkWLP_wA0zc3EBkhDhJF29kbVaQvbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
انگلیس با گل ششم بازی را تمام کرد
⚽️
فرانسه ۴ - ۶ انگلیس @Farsna</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farsna/451013" target="_blank">📅 03:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451012">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/275437ee88.mp4?token=ewqu3ABAl_sCltCYA52U2lN3G4D40TG3FIgYn28gsqlNo4ZFOpKBMLkAKIZfE8fGdXbI4OYJ3wmWUJu5tU1PEUNl4m3xDrsCx10rBNPtf2nWZiDm4LwiFFFdJyeO3TWyD0Fs6z17dLstitDMjnJDJpUWyJ5WDoTy4Caa8wZT0bGJVT4bDgaENW8onooPyDwPhYe2xI0LtTTZYr8h_N9lcprNtQVh0iFwK53BOVWrQT4QzMCEylVIdS6Pb3uiVz29gJeNxpEj_VObdfJR42aI9ZUDw3UC9angIlomoVt8CJ0nWfX5um2QNvRP1cv75vHN6xhTRnpIgGX6u8ynVy8LKwdVSc58dqNX70tXdO3eHafuqWLi-W4AKss1iAWtEMxL5psCy_aI3B-a-3diAD0_-5Qk95Rte31hSlZQjriJNXqHCNDg_VeIy9ecdh-Smqie951djrsy-FAK-8WCuMlWJ9nrPdRRh4Ib0ECXV2Uphvn7ODwS6b7u0GILaLs-PEqKnDPs_oulCjtH4xo2Ov7UjhrwYapSGFKGSDj0Iv30d3psCWfhiJVX2vH2EWTa8J9bl5HocdIGJMrbp7qArbxPhA8TVEN67BAklb2A1RRohNHl_LAENdf01vZ8ibKlqBrzD1ZQ3hwvzzqH9YmuQbdStuFQjmK0ZFW335GRtixX-28" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/275437ee88.mp4?token=ewqu3ABAl_sCltCYA52U2lN3G4D40TG3FIgYn28gsqlNo4ZFOpKBMLkAKIZfE8fGdXbI4OYJ3wmWUJu5tU1PEUNl4m3xDrsCx10rBNPtf2nWZiDm4LwiFFFdJyeO3TWyD0Fs6z17dLstitDMjnJDJpUWyJ5WDoTy4Caa8wZT0bGJVT4bDgaENW8onooPyDwPhYe2xI0LtTTZYr8h_N9lcprNtQVh0iFwK53BOVWrQT4QzMCEylVIdS6Pb3uiVz29gJeNxpEj_VObdfJR42aI9ZUDw3UC9angIlomoVt8CJ0nWfX5um2QNvRP1cv75vHN6xhTRnpIgGX6u8ynVy8LKwdVSc58dqNX70tXdO3eHafuqWLi-W4AKss1iAWtEMxL5psCy_aI3B-a-3diAD0_-5Qk95Rte31hSlZQjriJNXqHCNDg_VeIy9ecdh-Smqie951djrsy-FAK-8WCuMlWJ9nrPdRRh4Ib0ECXV2Uphvn7ODwS6b7u0GILaLs-PEqKnDPs_oulCjtH4xo2Ov7UjhrwYapSGFKGSDj0Iv30d3psCWfhiJVX2vH2EWTa8J9bl5HocdIGJMrbp7qArbxPhA8TVEN67BAklb2A1RRohNHl_LAENdf01vZ8ibKlqBrzD1ZQ3hwvzzqH9YmuQbdStuFQjmK0ZFW335GRtixX-28" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نوحه‌خوانی حسن شالبافان در مراسم یادبود مردم کهریزک برای رهبر شهید انقلاب در ایستگاه ۱۴۰ تجمعات مردمی
@Farsna</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farsna/451012" target="_blank">📅 03:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451011">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1efef3f4c7.mp4?token=CLRAMTpASqA8RCCOmNe4ElxJjsDolPW_fux-vAD770XcmvOK8bG-pp3-h36m5jrnK2r-YKyH9acKq9pQqeUjGu0oVJBqipJ53_loda77PuuDsbxBNdQFsAbeQD9dRhI3VMs96sYbsnB4m4v3GRKRkyhaXV-gtTK0DhnB9GQnlw-z1yj-k9UPRjvY-AbAPrtItOQ4dfuYuwGK3PGY0KAR7dj9eC7mxZbrCWZ_wEdVlG4V86N1pBUeVUsPjcayVEO_qQbG64WKD3AvOI49563mvcMbOBRa-NqNTx6ZCcgIx_aAD6I_A247JK9bOfelnV9z4VVxR2jtF1pmExtjc0bevQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1efef3f4c7.mp4?token=CLRAMTpASqA8RCCOmNe4ElxJjsDolPW_fux-vAD770XcmvOK8bG-pp3-h36m5jrnK2r-YKyH9acKq9pQqeUjGu0oVJBqipJ53_loda77PuuDsbxBNdQFsAbeQD9dRhI3VMs96sYbsnB4m4v3GRKRkyhaXV-gtTK0DhnB9GQnlw-z1yj-k9UPRjvY-AbAPrtItOQ4dfuYuwGK3PGY0KAR7dj9eC7mxZbrCWZ_wEdVlG4V86N1pBUeVUsPjcayVEO_qQbG64WKD3AvOI49563mvcMbOBRa-NqNTx6ZCcgIx_aAD6I_A247JK9bOfelnV9z4VVxR2jtF1pmExtjc0bevQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش‌سوزی گسترده در مقر گروهک‌های تجزیه‌طلب اربیل  @Farsna</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farsna/451011" target="_blank">📅 02:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451010">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">تکذیب انفجار در کیش و بندرلنگه
🔹
استانداری هرمزگان: تاکنون اصابتی در کیش و بندرلنگه گزارش نشده است.
@Farsna</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farsna/451010" target="_blank">📅 02:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451009">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
حملات نظامی دشمن آمریکایی به حوالی حاجی‌آباد
🔹
استانداری هرمزگان: در ساعت ۲:۱۰ نقطه‌ای در حوالی حاجی‌آباد هدف حملۀ نظامی دشمن آمریکایی قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farsna/451009" target="_blank">📅 02:39 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451008">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4714689b1f.mp4?token=Z-4jqI03bUSPw1JnN5wwlAEmEXlGKRRbvYgCpMsGM2ttB8m4qQDV5KRl9udcDANg_NDvVXbl7gu96Vn6N0kGCv6Ef22dVdSOICltiFdgubF6OCIWhfsK48QhTEyFMtXQ5q5zTQBAPlItRxbIQmxFg25PU5lBSe3Ycg7j_Rj6RdNtc_IsOQcy9_go9XF9-nKpUDSL5YhME_qe5OSni5HwsJFV3r4tm26TKuOWLRi7M6uc21nOcnFI4t2DQIJYOVLbs_SBeErNX-hvDAkyGk7S8QIWNglCFE-TQl6syIro8V5uAL44bBUgu0nwoKQzsBuV4gMGOTiLDwxN4QAk95gCCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4714689b1f.mp4?token=Z-4jqI03bUSPw1JnN5wwlAEmEXlGKRRbvYgCpMsGM2ttB8m4qQDV5KRl9udcDANg_NDvVXbl7gu96Vn6N0kGCv6Ef22dVdSOICltiFdgubF6OCIWhfsK48QhTEyFMtXQ5q5zTQBAPlItRxbIQmxFg25PU5lBSe3Ycg7j_Rj6RdNtc_IsOQcy9_go9XF9-nKpUDSL5YhME_qe5OSni5HwsJFV3r4tm26TKuOWLRi7M6uc21nOcnFI4t2DQIJYOVLbs_SBeErNX-hvDAkyGk7S8QIWNglCFE-TQl6syIro8V5uAL44bBUgu0nwoKQzsBuV4gMGOTiLDwxN4QAk95gCCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل چهارم فرانسه در وقت اضافه
⚽️
فرانسه ۴ - ۵ انگلیس @Farsna</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farsna/451008" target="_blank">📅 02:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451007">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd6bb19483.mp4?token=SdHxw9U4gokpkRSU-6CMaFMXSxQCX_fpV1jYKcQTBbbVfWEpcbJ7XZZYVHKVLrxBz8SwQljYKRtZIsIy7ld16eCpzfXtw7Qo1rPXyswvQqYUUQ3YqQDXZJtlNilRWOIS9r3fRaT8penTKqslSJO16ThAzXE5B1wxKJMfisv8vaE6Ct4OjQoeDoufuiTJ77Z6AHnBmPhFiq3iYTSIXorF4JZ5tS3RDTpMMdfabGpdN7gAUEFxE2bHslpy5u2ZGHSTxNbEA86gP21BveFgvA1fQLj7JlNAKacu3InmxHebwhEFXgj4_a63yi7uLaJpy_DnnqmAEjWRujvSBw6nfxT_TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd6bb19483.mp4?token=SdHxw9U4gokpkRSU-6CMaFMXSxQCX_fpV1jYKcQTBbbVfWEpcbJ7XZZYVHKVLrxBz8SwQljYKRtZIsIy7ld16eCpzfXtw7Qo1rPXyswvQqYUUQ3YqQDXZJtlNilRWOIS9r3fRaT8penTKqslSJO16ThAzXE5B1wxKJMfisv8vaE6Ct4OjQoeDoufuiTJ77Z6AHnBmPhFiq3iYTSIXorF4JZ5tS3RDTpMMdfabGpdN7gAUEFxE2bHslpy5u2ZGHSTxNbEA86gP21BveFgvA1fQLj7JlNAKacu3InmxHebwhEFXgj4_a63yi7uLaJpy_DnnqmAEjWRujvSBw6nfxT_TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هت‌تریک از روی نقطه پنالتی؛ گل پنجم انگلیس در دقایق پایانی
⚽️
انگلیس ۵ - ۳ فرانسه @Farsna</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farsna/451007" target="_blank">📅 02:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451005">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63191114b9.mp4?token=IgeQhisV3EUGZyGTEBEJRwOfGA4-DqULhiiYp2BaaK0wGG9r9SIAkdE4L7-0Gi3-7_7yZylR_yWUD7ltitO_KrN_Oxsh4AGP3wzKWubiMHQsKvX5L6Qaykl9qWjkgBBK74vK05TUVoiqOM5i1Fu7XnJFojlV2E7jGySkeS8rz5RdIUjCi4r9oAtNpVah2uYQneYOJF9nVJb200-Y_suNF5Q9JI0Z7WlsZ3awuEMPrMrzpwkNonDX6dbjkktsbD1kPgeXEjRbjqsQLR917fVlAr1UQgV8jnTArAizO3nxk1GcuJqvNu0-pkJQni_R-Uyt8OvHR1O60XAIxwiAFoHQ-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63191114b9.mp4?token=IgeQhisV3EUGZyGTEBEJRwOfGA4-DqULhiiYp2BaaK0wGG9r9SIAkdE4L7-0Gi3-7_7yZylR_yWUD7ltitO_KrN_Oxsh4AGP3wzKWubiMHQsKvX5L6Qaykl9qWjkgBBK74vK05TUVoiqOM5i1Fu7XnJFojlV2E7jGySkeS8rz5RdIUjCi4r9oAtNpVah2uYQneYOJF9nVJb200-Y_suNF5Q9JI0Z7WlsZ3awuEMPrMrzpwkNonDX6dbjkktsbD1kPgeXEjRbjqsQLR917fVlAr1UQgV8jnTArAizO3nxk1GcuJqvNu0-pkJQni_R-Uyt8OvHR1O60XAIxwiAFoHQ-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امباپه در دقیقۀ ۶۷ گل سوم فرانسه را هم زد
⚽️
فرانسه ۳ - ۴ انگلیس @Farsna</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farsna/451005" target="_blank">📅 02:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451004">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b93e8cca8.mp4?token=CdafwyezIIzp9tmteHSMYuy36lI489ocA3sEOeBk4UIuBsp55P6B7OosI_iDdRPbOPU8O_7TM9Nl6XR_SspIxbOGAw22ldr9GIRWimhdgOA-bRCgjiCZVmp7ocONZVOcZvY2C_nBnS1_FnTXYUWP7xYWR5MY2VKbD9RvsbxIQfZw_r6ULgbUmsOIp4eFcmYRzdacu8p2webM_KN8sDAO46loS5PuTlfbG1i_7pJ5RxMovp1KgjjukpfveuTBDQJOSLoVfBUcE2a1bvrysbFFFd4dwbrGQNffsRpvAqssCwtU1tXP48z3gW4Yy-f754tKUGHgGrk5cWm_kqj-8IKEBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b93e8cca8.mp4?token=CdafwyezIIzp9tmteHSMYuy36lI489ocA3sEOeBk4UIuBsp55P6B7OosI_iDdRPbOPU8O_7TM9Nl6XR_SspIxbOGAw22ldr9GIRWimhdgOA-bRCgjiCZVmp7ocONZVOcZvY2C_nBnS1_FnTXYUWP7xYWR5MY2VKbD9RvsbxIQfZw_r6ULgbUmsOIp4eFcmYRzdacu8p2webM_KN8sDAO46loS5PuTlfbG1i_7pJ5RxMovp1KgjjukpfveuTBDQJOSLoVfBUcE2a1bvrysbFFFd4dwbrGQNffsRpvAqssCwtU1tXP48z3gW4Yy-f754tKUGHgGrk5cWm_kqj-8IKEBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
منابع عراقی: همزمان با حمله به کنسولگری آمریکا، مقر گروهک‌های تجزیه‌طلب در اربیل نیز مورد حمله قرار گرفته است. @Farsna</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farsna/451004" target="_blank">📅 02:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451003">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YNFHaLCHA4bIi8z3JRn0VWhUGMrf10pHRnKjdP3WkJJwJM9vzlU7zGdil5S9okYQ10EZtnMn6DkFgxpqFjeEG1_UTmvZP4lC2rBUvpcOsJvDC5WpytBeVgEiGiu3UHxxFj7rq3hLbVbt7DLj5yeK_WpnZDWF7JLSU3Enh6LJ1fncxQYo8QassY4MnAEU624BnGvXw58sx-Wrep-_zySwL0rdnzoy7LkrDcR7A4DdBiynJiyMlIqDoqNI5Hkmp9gjkthh4UqauloOReBWXKeSPCPYdDGJ-D_3sr61e2TeyW4z38IUQx5uYTmz0GXOSUs7a1NPKWlQJhsc6wSrjB7bcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
امباپه با ۲۲ گل بهترین گلزن تاریخ جام‌جهانی شد
@Sportfars</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/451003" target="_blank">📅 02:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451002">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/131b049251.mp4?token=FmumSF7Ji8GGbFyM8wBq92JfLCifUjLvDRcuP0TGvO2ff8VJ1mk-jndZwMaDB8HCFli_-cwsw0aYRxxdjF0LQFXSeNsC3OatF0VDjtsBPzffERvhSQVYo4MIpwyVfZ_oXnKIhN-fvAWFHZsJveEBPafbXsOLrrPRiKl5yOQIPl8MNKusdZqCQMhsBzP7mwVoIrots36ANQVifYEkWlyLC8khFhHzeWy7oHi7T7iAZVsgG1HsibxT5kvnAih7C24eTd_SnjzoS4pR2djE6NuqBxI-PzCKvYC5fvkOw71AQqPTr00AKwWMbsWMqy219MC6fwmouixUS5BKMyj_Cjq2PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/131b049251.mp4?token=FmumSF7Ji8GGbFyM8wBq92JfLCifUjLvDRcuP0TGvO2ff8VJ1mk-jndZwMaDB8HCFli_-cwsw0aYRxxdjF0LQFXSeNsC3OatF0VDjtsBPzffERvhSQVYo4MIpwyVfZ_oXnKIhN-fvAWFHZsJveEBPafbXsOLrrPRiKl5yOQIPl8MNKusdZqCQMhsBzP7mwVoIrots36ANQVifYEkWlyLC8khFhHzeWy7oHi7T7iAZVsgG1HsibxT5kvnAih7C24eTd_SnjzoS4pR2djE6NuqBxI-PzCKvYC5fvkOw71AQqPTr00AKwWMbsWMqy219MC6fwmouixUS5BKMyj_Cjq2PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل دوم فرانسه در دقیقۀ ۵۳
⚽️
فرانسه ۲ - ۴ انگلیس @Farsna</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farsna/451002" target="_blank">📅 02:04 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451001">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
حملۀ دشمن آمریکایی به حوالی سیریک
🔹
استانداری هرمزگان: در ساعت ۱:۳۰ نقطه‌ای در حوالی سیریک هدف حملۀ نظامی دشمن آمریکایی قرار گرفت.
🔸
سنتکام دقایقی پیش از آغاز حملات آمریکا علیه خاک ایران خبر داده است.
@Farsna</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farsna/451001" target="_blank">📅 02:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-451000">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‌
🔴
منابع عراقی از حملات سایبری علیه شرکت‌های گازی اماراتی و آمریکایی در اربیل خبر دادند. @Farsna</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farsna/451000" target="_blank">📅 01:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450999">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‌
🔴
منابع عراقی: حملۀ پهپادی به کنسولگری آمریکا در اربیل ادامه دارد. کنسولگری آمریکا مورد حملۀ گستردۀ پهپادی قرار گرفت.  @Farsna</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farsna/450999" target="_blank">📅 01:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450998">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/933f021d4e.mp4?token=jsxQJpFlOPnsEIiWn9rZzxRkLqw7syJE0XX7b8GpAiUbfaBPpghNwwWWVazv84dlsFJGawz5DgdMjggmDOEqEb0IfoCOnJNaH5CVIGrCTqx5q0tDQjTLmAb3dD9ePkXit17HXJ6-mLWlTRTxVsqOvKHRrg6ZLFjIyrNYfiM_LujHF4mxAQCOz36VvTrJFH-ya99bIivBlyHzC8FBNm4J4R8obk_LCHx-06folo14hmvWMF2ps2YU78KhxlMghYZmzCAjbPO5Wj-ccBNo9hwaOb_i9AM9vCFj_J80RfIY8eOKRhQI8fVam8k9Y9EmQi4vefOp1wJABVPVsbpKoYH8bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/933f021d4e.mp4?token=jsxQJpFlOPnsEIiWn9rZzxRkLqw7syJE0XX7b8GpAiUbfaBPpghNwwWWVazv84dlsFJGawz5DgdMjggmDOEqEb0IfoCOnJNaH5CVIGrCTqx5q0tDQjTLmAb3dD9ePkXit17HXJ6-mLWlTRTxVsqOvKHRrg6ZLFjIyrNYfiM_LujHF4mxAQCOz36VvTrJFH-ya99bIivBlyHzC8FBNm4J4R8obk_LCHx-06folo14hmvWMF2ps2YU78KhxlMghYZmzCAjbPO5Wj-ccBNo9hwaOb_i9AM9vCFj_J80RfIY8eOKRhQI8fVam8k9Y9EmQi4vefOp1wJABVPVsbpKoYH8bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امباپه در دقیقۀ ۴۷ گل اول فرانسه را زد
⚽️
فرانسه ۱ - ۴ انگلیس @Farsna</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farsna/450998" target="_blank">📅 01:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450997">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73ab28dde3.mp4?token=A22qsxF3vKdn9DSW4M_jaRLIZSm6fjvre7x7EA55AR9xRZElMAv59hy7Ie7JRU3vuA97TVjhZbnoZ-IF_CnK5ikOIfJP6fgMs61Rek8nihyKAkkAGw1yKnJMexPVA5uqgpuXOARAYxKPRtT7mShmIbGziVpLtE_niVNkFM4OL3_bJG_G8jQcENKYyO8Vl6MPvyN0di3Lk8meDpwAIhP2A3THOarhEqsAwxFIcy-ZR47uUMa7TLPJSU2GhVkazcCnxF6GGzXovwpd9YJQ9hiI9BQYOPaGMqqZkAqsrOoSdUNaBvGQmihPTWQM-iLka3dSRwHVQSB4RZA0mhpg5Ud5bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73ab28dde3.mp4?token=A22qsxF3vKdn9DSW4M_jaRLIZSm6fjvre7x7EA55AR9xRZElMAv59hy7Ie7JRU3vuA97TVjhZbnoZ-IF_CnK5ikOIfJP6fgMs61Rek8nihyKAkkAGw1yKnJMexPVA5uqgpuXOARAYxKPRtT7mShmIbGziVpLtE_niVNkFM4OL3_bJG_G8jQcENKYyO8Vl6MPvyN0di3Lk8meDpwAIhP2A3THOarhEqsAwxFIcy-ZR47uUMa7TLPJSU2GhVkazcCnxF6GGzXovwpd9YJQ9hiI9BQYOPaGMqqZkAqsrOoSdUNaBvGQmihPTWQM-iLka3dSRwHVQSB4RZA0mhpg5Ud5bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
شرکت نفت کویت: صبح امروز یک مرکز نفتی مهم توسط ایران هدف حمله قرار گرفت و خسارت‌های زیادی به آن وارد شد. @Farsna</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farsna/450997" target="_blank">📅 01:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450996">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‌
🔴
منابع عراقی: همزمان با حمله به کنسولگری آمریکا، مقر گروهک‌های تجزیه‌طلب در اربیل نیز مورد حمله قرار گرفته است. @Farsna</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/450996" target="_blank">📅 01:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450995">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fded8ed20.mp4?token=twR3mB58iD3mgzWQdfVkk9Xt8NUBQrrCX5kkwaGalawUeW5MHw_lfyBwPv_plZWnA-dXfKXDu6FObF8_xVYakpx8hpItEdGPYCKzwXe6xOFFyMkZ33aW5SRg2tF4BMtHMp4CWDuTjWIGUql1kG5K6KlA1O5-0YZN-S3WuhtAL3P5_oiUG54TfMsNwCwTM830ctX1xz9kkmDSWI10ccdndNVlx-xJxGhYtZDAF92P87ot4WUkxIPuzNX9H3YoSEv0bff-jNEZtbvpaWH3LYUh3Evu_CPaQgMG00oRHgVrGf96yCovHEPX7UdrQEM1c4asrA3YS9HJWoY1jYmHpBm2RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fded8ed20.mp4?token=twR3mB58iD3mgzWQdfVkk9Xt8NUBQrrCX5kkwaGalawUeW5MHw_lfyBwPv_plZWnA-dXfKXDu6FObF8_xVYakpx8hpItEdGPYCKzwXe6xOFFyMkZ33aW5SRg2tF4BMtHMp4CWDuTjWIGUql1kG5K6KlA1O5-0YZN-S3WuhtAL3P5_oiUG54TfMsNwCwTM830ctX1xz9kkmDSWI10ccdndNVlx-xJxGhYtZDAF92P87ot4WUkxIPuzNX9H3YoSEv0bff-jNEZtbvpaWH3LYUh3Evu_CPaQgMG00oRHgVrGf96yCovHEPX7UdrQEM1c4asrA3YS9HJWoY1jYmHpBm2RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل چهارم انگلیس به فرانسه توسط ساکا در دقیقه ۱+۴۵
⚽️
انگلیس ۴ ـ ۰ فرانسه  @Farsna</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/450995" target="_blank">📅 01:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450994">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
رسانه‌های عراقی از وقوع چندین انفجار در کنسولگری آمریکا در اربیل خبر دادند.  @Farsna</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farsna/450994" target="_blank">📅 01:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450993">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
رسانه‌های عراقی از وقوع چندین انفجار در کنسولگری آمریکا در اربیل خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farsna/450993" target="_blank">📅 01:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450992">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OWcFYKF_-NVgceVIDhANR1wnNUuICRO0hg7Di6SkjhbSjdQgANS0kHIPlDSb029R0y9F1J7EWtou0F1Ut6WWH636MtP4FHjk9qXkVyRVKhVEN9-jQOCdoxuwKuS74C5JZib3WVYJuX1gN5b4crXDJyU3x9cQKwVdo_5bt56H-v8lypShQuvZybv_qJ9pHMVomonnPkExnTy0SQz7INkViVa_ri4phXUg07kKsC4Ie7CcfRIbRInTPtHpc9Ny0D_70NIMVHmAz8UukNWm-QLXC6eQArsGR60JvFNmKrisMLz3yNLF5hBzh1W88D5WL1549vkRWFuUiID0sl7ZKe04nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
آمار نیمۀ اول بازی انگلیس و فرانسه
@Farsna</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farsna/450992" target="_blank">📅 01:29 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-450991">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4302423563.mp4?token=OtIWlcIU3YufEXBIW7tZvwsQeKZNDk93of6xmFa3eAvkh4HYnhk9bL5OvlYN9shiq7CMQvr6qMvVCHUn6tHM3Ab7kdigWCpKabuwAS1eYgo5P6KUXDqM_kC9TLMtoUn0k6vP6BS1DwNTV4u2WwL2rfK_dlt0VbInd_HFtKSG1NU_4BFPaS7BB420US6fzkEqlHx-Y7WtDAOg33u_V6lGz6IShhvYlG5-_QBOQGmJLX4K6EXTy-MXR-jCznAjJMjceNHItQPiTg_z_8kDCz9XlQbXy-GWRY31nrediNgfNz8PY6sOgB-560-1dTBjq6qpwLJPYwcK2VAtgr-FQy0eaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4302423563.mp4?token=OtIWlcIU3YufEXBIW7tZvwsQeKZNDk93of6xmFa3eAvkh4HYnhk9bL5OvlYN9shiq7CMQvr6qMvVCHUn6tHM3Ab7kdigWCpKabuwAS1eYgo5P6KUXDqM_kC9TLMtoUn0k6vP6BS1DwNTV4u2WwL2rfK_dlt0VbInd_HFtKSG1NU_4BFPaS7BB420US6fzkEqlHx-Y7WtDAOg33u_V6lGz6IShhvYlG5-_QBOQGmJLX4K6EXTy-MXR-jCznAjJMjceNHItQPiTg_z_8kDCz9XlQbXy-GWRY31nrediNgfNz8PY6sOgB-560-1dTBjq6qpwLJPYwcK2VAtgr-FQy0eaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرانسه گل سوم را هم خورد
⚽️
انگلیس ۳ - ۰ فرانسه @Farsna</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farsna/450991" target="_blank">📅 01:21 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
