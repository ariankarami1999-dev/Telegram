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
<img src="https://cdn4.telesco.pe/file/Y_9jYxvmFl1znpbbK4uJLDO-WndKTwTstP8Bl8JSfUfFrClFjrnbuJ7zcHS-_wuX10r5E-YAaJVFpMRZIwx6N1N7xxiQtjqDs5LO_f8OEDpmQzAOQVTriLv9fIxRaG6pd0YAIlU_7XZGw2NmHzJyz5be7W4XLZpPK-qCp3MAIJUuho-j15cpyfKKtkqOfKzyV3o9sGd_a7vzkIueNvF5NsDmQ9wVW3Ki3bbBm2Vizu6RSap1VePe79ro03wIlEB5Vas0b1Ez35LBimoNguU40rQA_uaGd2syZg2Qzrr5kESi5WlFHYOdIm1kcoA_kTKvzZoSSnXQlJU2iJDgMqGrhQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 339K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 11:38:00</div>
<hr>

<div class="tg-post" id="msg-16433">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ان‌بی‌سی نیوز به نقل از چند منبع آگاه:
آیت الله سید مجتبی خامنه‌ای احتمالا در مراسم خاکسپاری آیت الله علی خامنه‌ای حضور نخواهد داشت، چون در حمله آغاز جنگ به‌شدت مجروح و چندین بار تحت عمل جراحی قرار گرفته!
@withyashar</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/withyashar/16433" target="_blank">📅 11:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16432">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">کانال ۱۴ اسرائیل : حسام حسن، سرمربی تیم ملی مصر که اولین پیروزی تاریخ این تیم را در مرحله حذفی کسب کرد و به مرحله یک‌هشتم نهایی جام جهانی 2026 صعود کرد (در مقابل آرژانتین)، از این فرصت برای ابراز اعتراض سیاسی استفاده کرد و پیروزی را به مردم نوار غزه تقدیم کرد: "امیدوارم خداوند پیروزی را به آنها عطا کند."
@withyashar</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/withyashar/16432" target="_blank">📅 11:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16431">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">نیکلاس لیساک فعال رسانه‌ای نوشت:
"یک منبع موثق می‌گوید مجتبی خامنه‌ای در اواخر ماه مارس، پس از آنکه بر اثر جراحات ناشی از حمله هوایی‌ای که پدرش را کشت به کما رفت، جان باخت.
او هرگز نفهمید که رهبر جمهوری اسلامی شده است.
قالیباف و سپاه اکنون در جست‌وجوی افرادی با شباهت ظاهری (بدل) هستند تا آن‌ها را در انظار عمومی به‌کار گیرند."
@withyashar</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/withyashar/16431" target="_blank">📅 10:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16430">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">منابع اسرائیلی به «کانال 15»اسرائیل اطلاع دادند بنیامین نتانیاهو، در انتظار چراغ سبز ترامپ، برای تصرف پایگاه «حزب‌الله» در ارتفاعات منطقه «علی الطاهر» در جنوب لبنان است.ترامپ از نتانیاهو خواسته تا زمانی که مذاکرات با ایران ادامه دارد، این عملیات را به تعویق بیندازد. برآورد ارتش اسرائیل، بین 30 تا 40 نفر از نیروهای یگان «بدر» وابسته به حزب‌الله، از جمله شماری از فرماندهان این گروه، در داخل این پایگاه گرفتار شده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/withyashar/16430" target="_blank">📅 10:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16429">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">سی‌ان‌ان‌ به نقل از مقام‌های آمریکایی:
مقامات دولت ترامپ از نزدیک شبکه جاسوسی اسرائیل که در ماه‌های اخیر، فعالیت‌های اطلاعاتی و جاسوسی خود علیه ایران و آمریکا را افزایش داده، زیر نظر داشته‌اند
مسئولان آمریکایی تلاش کردند به ایران درباره این نگرانی که اسرائیل ممکن است قالیباف و عراقچی را ترور کند، هشدار دهند
@withyashar</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/withyashar/16429" target="_blank">📅 10:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16428">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">حضور هادی خامنه ای (برادر کوچکتر سید علی) و وحیدی در‌ مراسم @withyashar</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/withyashar/16428" target="_blank">📅 10:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16427">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64375e3a46.mp4?token=rfcA-mJ5pvXvrvMq__i-EU5XYXx1T6RL686pzwoWdrU5AIYqzlmfRUQxEQD83iJfn5_e1xnx1QhTKljHNrbA21OPNVEbX0wpDf002e3DPxKsYDh5B6qTStWOCKG-5X832FyE3D-kXugGWHWBdd1JMHhE7SqyAcuXhNB8oJ69r0jI6El_SdidCwgTk0pQBSO65mUwCCBLvYLLWOVB9JiE0rJK332yOLRMsdt6zncIMWFHMgjC5d2GXX9Iziy7i1oVwo3hLWdvmqOahCjlRT6_3yj7XEwQ2RtEyTwqQh-XdHHTtpruVyLbAmcH-9-YL8jTpdDuj6zLemAvSzquU42GkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64375e3a46.mp4?token=rfcA-mJ5pvXvrvMq__i-EU5XYXx1T6RL686pzwoWdrU5AIYqzlmfRUQxEQD83iJfn5_e1xnx1QhTKljHNrbA21OPNVEbX0wpDf002e3DPxKsYDh5B6qTStWOCKG-5X832FyE3D-kXugGWHWBdd1JMHhE7SqyAcuXhNB8oJ69r0jI6El_SdidCwgTk0pQBSO65mUwCCBLvYLLWOVB9JiE0rJK332yOLRMsdt6zncIMWFHMgjC5d2GXX9Iziy7i1oVwo3hLWdvmqOahCjlRT6_3yj7XEwQ2RtEyTwqQh-XdHHTtpruVyLbAmcH-9-YL8jTpdDuj6zLemAvSzquU42GkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بارزانی، رئیس اقلیم کردستان عراق، با قالیباف دیدار کرد  @withyashar</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/withyashar/16427" target="_blank">📅 10:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16426">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">مکرون: ناو هواپیمابر شارل دوگل در پی امضای یادداشت تفاهم میان آمریکا و ایران به فرانسه بازخواهد گشت. @withyashar</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/withyashar/16426" target="_blank">📅 09:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16425">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">کانال ۱۲ اسرائیل : مقام‌های اسرائیل ارزیابی می‌کنند که طی ۲ تا ۳ ماه آینده، احتمالاً تا سپتامبر، «هیئت صلح» ممکن است حماس را ناقض توافق غزه اعلام کند.
چنین اقدامی می‌تواند به اسرائیل آزادی عمل بیشتری برای فعالیت در مناطق تحت کنترل حماس بدهد و به‌طور بالقوه به ازسرگیری درگیری‌ها منجر شود.
@withyashar</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/withyashar/16425" target="_blank">📅 09:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16424">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4efbcf8243.mp4?token=jQ9VHnisiFc8nUwk9F5rM4GL0vumGyi_urZLkICqqYgWEJFIBqiIKtlCCft_bMwnAHWBFnd6aw7j63Y4ZGQVUidEauGQqpzGXJuMg0tmYupjsvlAvpnq8ZvwIwNBS93SP5FGt84A16anjGwbNc5H9EK80vWJly6QfxgI_tO8Pds_Ima89D8UFVE8Ve7nQSNZ_edlx_DcU1US-N78et1pVn8OV4A179rOhJFNe8BP4Y2lLBWQLuPeF9kyA1BqfPBROWCMBeBXf1yeAiMF6gt4k424G_bUquziAVeN7cQlorYjeRq-GFHrPI-LtK7BqPXHJGJmD3AVwXSohM2m7LeBCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4efbcf8243.mp4?token=jQ9VHnisiFc8nUwk9F5rM4GL0vumGyi_urZLkICqqYgWEJFIBqiIKtlCCft_bMwnAHWBFnd6aw7j63Y4ZGQVUidEauGQqpzGXJuMg0tmYupjsvlAvpnq8ZvwIwNBS93SP5FGt84A16anjGwbNc5H9EK80vWJly6QfxgI_tO8Pds_Ima89D8UFVE8Ve7nQSNZ_edlx_DcU1US-N78et1pVn8OV4A179rOhJFNe8BP4Y2lLBWQLuPeF9kyA1BqfPBROWCMBeBXf1yeAiMF6gt4k424G_bUquziAVeN7cQlorYjeRq-GFHrPI-LtK7BqPXHJGJmD3AVwXSohM2m7LeBCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: ما ضربه مهلکی به ایران زدیم. آن‌ها مشتاق به حل و فصل [مشکلات] هستند. آن‌ها واقعاً می‌خواهند این موضوع را به پایان برسانند.
ما به آن‌ها یک هفته فرصت دادیم تا مراسم تدفین برگزار کنند، زیرا ما مهربان هستیم. این حقیقت دارد
@withyashar</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/withyashar/16424" target="_blank">📅 09:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16423">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/withyashar/16423" target="_blank">📅 03:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16422">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">https://t.me/boost/withyashar</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/withyashar/16422" target="_blank">📅 03:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16419">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">@withyashar
🪓</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/withyashar/16419" target="_blank">📅 01:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16418">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZjn24YUiTjkMH7dfvGTmQFNhECdaqheApTycOQWD-XMlSmmqlaEWVHx8Kymyl04unvXqTvLwZ7UPbUfg7h2piSiYAc9rR4pbQQJMCrCdTwtyM4Qa67gnT8bUoQ39ir_xrxguemGqJT7eHNRH1oLZNIC6S7oRwmbs-HNwPMNyRviiFulNfAXWQbL-IOL15oiyQjHAGiSXjQN2KJ6WvXQH2ldcWkORtxNo7dLaJpwkYqYwxqexHARIPp6J0LrQIaHYq9-jHgDN1p1u5VJO1LE-4AUaRUf0d6YPyKtP7ugHu5u5Zd06eFqDwHZJyTQhOnCi0i3oDa88Q_lOLSIhPJelg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همکنون عزاداری سنگین نیرو هوایی آمریکا کف تنگه هرمز ، قشنگ دارن سینه میزند
@withyashar</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/16418" target="_blank">📅 01:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16417">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MotgdfaW7aWnIto935imi19cTki2AteJvjwu8_Drg55WHtFSZVUtyO6EJnMn9YLEhSZk3q1kaAO0y2XDUmvCbiYgtTpWbUgwsyxszfbs0_q9JaNRqeLDKkpHyP5H8Wky-HD-jNFW0YhxpNyW2eyOUXAoaaW1YkECRQofS3XTVm0TkrVa3xJ1lSyW9rjc9YB-E-hRq0rcJ4gVW6DxFwNUG_Z2vb3G2plZTGNfnHmrEryk2VOKLFzFieb2NP1juEITiRBABBWR_Mrvr7rVNTRI9BSv43650-Zc2y0FIIwenoXfh5YSPRZB6shSvmnfguzy_kuoCe0ZbsTlBdQjz_s-gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامیونت یخچالداری که جنازه علی خامنه ای را حمل میکرد، گویا خیلی عجله داشته. ۲،۳۰۰ هم جریمه شده.
@withyashar</div>
<div class="tg-footer">👁️ 94.8K · <a href="https://t.me/withyashar/16417" target="_blank">📅 00:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16416">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">تعداد کشته‌های زلزله در ونزوئلا به ۲۶۴۵ نفر افزایش یافته است، به گفته وزارت اطلاع‌رسانی این کشور. همچنین اعلام شد که بیش از ۱۲۰۰۰ نفر مجروح شده و حدود ۱۵۰۰۰ نفر خانه‌های خود را در اثر این فاجعه از دست داده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 93.8K · <a href="https://t.me/withyashar/16416" target="_blank">📅 00:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16415">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ba3ecf0ff.mp4?token=qx_YnEbDCU6SD4gJpjqBRLrhnARE78BrtutBKfUbsLzVOsBepIQtz0CjgHcFJsPZ91Z8QalNGAiZKaPgIonTWsikMp6BT_Pz4OMy0XdpRmw39GjJcmWq5gtnV7Uw3E3c7KcL4LVZZjIBkObJ_Uvartbstd5yr9bSL4ebH5IEsqwNWed4w3WCXbN33Fa30-aGF5tdgJkIDuF-sDJ3MkOEV0hQhGkY68hJqIJ29L-8KJ4fXubEMt-cqgyZqOW_9-CEW-Gpx-ZNAvgbntJFfoujmuy45AEaMqHHX-l_hsKE5yrQuWi7tBa9smYassdjttR-5ELbwe_M8QMGS-OE059eZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ba3ecf0ff.mp4?token=qx_YnEbDCU6SD4gJpjqBRLrhnARE78BrtutBKfUbsLzVOsBepIQtz0CjgHcFJsPZ91Z8QalNGAiZKaPgIonTWsikMp6BT_Pz4OMy0XdpRmw39GjJcmWq5gtnV7Uw3E3c7KcL4LVZZjIBkObJ_Uvartbstd5yr9bSL4ebH5IEsqwNWed4w3WCXbN33Fa30-aGF5tdgJkIDuF-sDJ3MkOEV0hQhGkY68hJqIJ29L-8KJ4fXubEMt-cqgyZqOW_9-CEW-Gpx-ZNAvgbntJFfoujmuy45AEaMqHHX-l_hsKE5yrQuWi7tBa9smYassdjttR-5ELbwe_M8QMGS-OE059eZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی و قالیباف امروز
😁
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/16415" target="_blank">📅 23:51 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16414">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">مکرون: ناو هواپیمابر شارل دوگل در پی امضای یادداشت تفاهم میان آمریکا و ایران به فرانسه بازخواهد گشت.
@withyashar</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/withyashar/16414" target="_blank">📅 23:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16413">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">وای نت عبری : هزاران نفر در مراسم تشییع جنازه در تهران شرکت کردند، اما در اسرائیل این خبر خنده دار بود که "بسیاری نه برای عزاداری - بلکه برای اطمینان از اینکه او واقعاً مرده است، آمده بودند."
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/16413" target="_blank">📅 22:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16412">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">المانیتور:
مقام‌های اسرائیلی به‌طور غیرعلنی امیدوارند ایران مذاکرات شکننده را طولانی کند و آن‌قدر آمریکا را خسته کند که ترامپ دست‌کم محاصره دریایی کامل و تحریم‌ها را بازگرداند
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/16412" target="_blank">📅 21:38 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16411">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79266b9c5c.mp4?token=FTNCX6AreHnmv7UibkBIZTF9wMwiRPbiqsjzaDQWkaUlr2xu2ccb-yiHC74197S6_YtjPYh3rvc4ZkgCMnKYIK75Ce2w0Ped3-dNpzKrw534LoFcV8LQEbNOwCZuxDi9Llqex0pRERpRgMQzV76pFBARekkqQ2_PBAwJy5lgeb8X236Yz72emyX6_nJjwUvV-J_oZ_gYzvyiatQ4_YL9EJY3S9dQmoyY1xNLE65nrUOZ-aajmP2cBw0rv3tZhr4lKkMfWsOT1xmD8JpMy1BRarxWZPC_UPv69g-BiJZuGbZPAIy6HGyDexP6sA9NVxu1DU3LCQH4p-Phz01uPnRq8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79266b9c5c.mp4?token=FTNCX6AreHnmv7UibkBIZTF9wMwiRPbiqsjzaDQWkaUlr2xu2ccb-yiHC74197S6_YtjPYh3rvc4ZkgCMnKYIK75Ce2w0Ped3-dNpzKrw534LoFcV8LQEbNOwCZuxDi9Llqex0pRERpRgMQzV76pFBARekkqQ2_PBAwJy5lgeb8X236Yz72emyX6_nJjwUvV-J_oZ_gYzvyiatQ4_YL9EJY3S9dQmoyY1xNLE65nrUOZ-aajmP2cBw0rv3tZhr4lKkMfWsOT1xmD8JpMy1BRarxWZPC_UPv69g-BiJZuGbZPAIy6HGyDexP6sA9NVxu1DU3LCQH4p-Phz01uPnRq8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمل پیکر علی خامنه ای در کامیون یخچال دار
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/16411" target="_blank">📅 21:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16410">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">یورونیوز : در پی انتشار ویدیویی از زنی که با لباس زیر در پارکی در شهر یزد قدم می‌زد، مقامات قضایی جمهوری اسلامی از بازداشت عوامل انتشار فیلم و «برخورد قانونی قاطع و متناسب با رفتار آنان» خبر داده‌اند.
خبرگزاری دولتی ایرنا با متهم کردن این زن به «هنجارشکنی» مدعی شده که وی به «اختلالات شدید روانی» مبتلا بوده و بعد از بازداشت کوتاه اکنون وی به آغوش خانواده‌اش بازگشته است.
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/16410" target="_blank">📅 20:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16409">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">باراک راوید خبرنگار  آکسیوس:
ترامپ امروز با نتانیاهو تلفنی صحبت کرده.
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/16409" target="_blank">📅 20:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16408">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">آکسیوس: نتانیاهو به زودی در سفری ناگهانی و قریب الوقوع وارد آمریکا خواهد شد و با ترامپ درباره ایران دیدار خواهد کرد.
@withyashar
🚨
🚨</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/16408" target="_blank">📅 20:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16407">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">تکذیب خبر نیویورک‌تایمز درباره ترور مقامات ایرانی از سوی دفتر نتانیاهو
حساب رسمی نخست‌وزیر اسرائیل در شبکه ایکس نوشت:
«طبق معمول، آخرین گزارش نیویورک تایمز درباره اسرائیل و مذاکره‌کنندگان ایرانی، خبر جعلی است. یک جعل کامل واقعیت.»
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/16407" target="_blank">📅 19:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16406">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">صفحه‌ فارسی وزارت امور خارجه اسرائیل در X:
واقعا توی اون تابوت چی‌ گذاشتن؟
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/16406" target="_blank">📅 18:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16405">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">حوثی‌ها ادعا می‌کنند که با هواپیماهای سعودی در آسمان یمن درگیر شده‌اند، به منظور جلوگیری از فرود یک هواپیمای غیرنظامی ایرانی در پایتخت صنعا. حوثی‌ها اعلام کرده‌اند که هرگونه حمله سعودی دیگر، "با حملاتی به فرودگاه‌ها و منافع حیاتی در عربستان سعودی پاسخ داده خواهد شد."
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/16405" target="_blank">📅 18:52 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16404">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">آغاز مذاکرات ایران با شرکت‌های ژاپنی برای ازسرگیری صادرات نفت
به گزارش جروزالم‌پست، منابع آگاه می‌گویند ایران مذاکراتی را با شرکت‌های ژاپنی برای ازسرگیری صادرات نفت آغاز کرده است؛ مذاکراتی که در چارچوب معافیت موقت از تحریم‌های آمریکا دنبال می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/16404" target="_blank">📅 18:51 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16403">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tAJUgK_uq6HG57EEEUzFIVXFg-pvhCISko75PjTX6YWbzEfJb4OqmsAv3Wr0WOChx-WyxWQ1iSkQ1-uPANo3DIDm61xvTGgKeBI-gv0Qz3-fdz9j2nJ6-a6Ihgh4I9rebafV01yzKejQnnOln-4MJdfxP06hnesA0Qp5dd-EMpiqbhjgHAGeUyHOAdWf3bFX7qxZgY-b2HrxA_kjNHjKPFdqWHKRMSSY2ISnRATxIC-IK8E1et-Gi79GvpnWOw7shhMHLo7JJn0792EgGWvuSOY-WQn3yYXUdD-xwaDBTce2JKsrGbspbnnx9ffezQhaaprdrlW3b9s9m7zCUAGCew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: جان اف کندی بعد از من دومین رئیس جمهور خوشگل تاریخ آمریکاست
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/16403" target="_blank">📅 18:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16402">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">هفت خواننده سوپر عرزشی به نام های علیرضا افتخاری، محمد معتمدی، پرواز همای، مصطفی راغب، رضا صنعتگر، رضا شیری و حسین حقیقی ی آلبوم به اسم بدرقه برای رهبر ضبط کردن.
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/16402" target="_blank">📅 17:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16401">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">الجزیره: ۵۰۰ میلیون دلار برای ترامپ، دسترسی برای پاکستان؛ چگونه شرط‌بندیِ کریپتویی/ دیپلماتیک اسلام‌آباد جواب داد؟
وقتی این هفته جزئیات درآمدهای مالی دونالد ترامپ، رئیس‌جمهور آمریکا، در سال ۲۰۲۵ منتشر شد، یک رقم بیش از همه جلب توجه کرد: شرکت رمزارزی خانوادگی او، ورلد لیبرتی فایننشال (WLF)، فقط از محل فروش توکن‌ها در سال گذشته بیش از ۵۰۰ میلیون دلار برای او درآمد ایجاد کرده بود؛ بخشی از یک سود بادآوردۀ بسیار بزرگ‌تر از حوزهٔ رمزارز که در مجموع صدها میلیون دلار دیگر هم ارزش داشت
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/16401" target="_blank">📅 17:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16400">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a2a30f1a3.mp4?token=DH0DQATou74BslQMQKBIIq4of-S8g0gWmIzgGvywe549wOjtlXsWU0y4heoMQGJy1g5AdMBOzYDnR8rY4-vpch5zSLs3GHnqclwvwQfZ9f_x-FwcZDYGdce3-hmTR5LliERN7WRQmfkfKnapiKbHwjhN1yUsQDQjYGRysDH2L9My5F-Zj5DhEHMOvYUFUQUdQ8EFHpBciPEuQiY0vG2jxggw-vHfrMoCZCt5U5Y27T2G6f--whftygvRBeH9CyuGd8R9kVF_JTkGCe12ErA9Qf8LDfHJsmcuy8QGrprprYTgv556Fu0HqA0vVDwqX0pM-y7Jd3AoJaCPRau2KJIQEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a2a30f1a3.mp4?token=DH0DQATou74BslQMQKBIIq4of-S8g0gWmIzgGvywe549wOjtlXsWU0y4heoMQGJy1g5AdMBOzYDnR8rY4-vpch5zSLs3GHnqclwvwQfZ9f_x-FwcZDYGdce3-hmTR5LliERN7WRQmfkfKnapiKbHwjhN1yUsQDQjYGRysDH2L9My5F-Zj5DhEHMOvYUFUQUdQ8EFHpBciPEuQiY0vG2jxggw-vHfrMoCZCt5U5Y27T2G6f--whftygvRBeH9CyuGd8R9kVF_JTkGCe12ErA9Qf8LDfHJsmcuy8QGrprprYTgv556Fu0HqA0vVDwqX0pM-y7Jd3AoJaCPRau2KJIQEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
😂
😂
😂
😂
خطر حمله قلبی
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/16400" target="_blank">📅 16:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16399">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f09f9f705f.mp4?token=JqOyo9C4rVEvpZkxRWgS9Ny_cED4UUyHEzJjjzG-TrBEZKChjzRqaEF9mF4UCDCvaY4LEFN30e9pfcVv4xKAj-Yh6kzvSiGMPSQq0Yr0gldveBxVfls6gcLK4429bah5wOdMa0i1phN7p6l821o3tyyYLRn-U1zc7GehmyxmN2FvHSKAxsbC6K46y-zqbcTTMBGjHfl8jgkEABsXW-jJzcBOWBf9SMYNtF2OqqpzJtyaQunqiJA_8z4VJE5b3KgADT6FvTgLR5_1ieZ7QvigMh9sCVSA_iHummF1lPT1ahZLlGPr-pWT-NweMT-YRV2hymYWIpDq0mPQnYQj4XzyMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f09f9f705f.mp4?token=JqOyo9C4rVEvpZkxRWgS9Ny_cED4UUyHEzJjjzG-TrBEZKChjzRqaEF9mF4UCDCvaY4LEFN30e9pfcVv4xKAj-Yh6kzvSiGMPSQq0Yr0gldveBxVfls6gcLK4429bah5wOdMa0i1phN7p6l821o3tyyYLRn-U1zc7GehmyxmN2FvHSKAxsbC6K46y-zqbcTTMBGjHfl8jgkEABsXW-jJzcBOWBf9SMYNtF2OqqpzJtyaQunqiJA_8z4VJE5b3KgADT6FvTgLR5_1ieZ7QvigMh9sCVSA_iHummF1lPT1ahZLlGPr-pWT-NweMT-YRV2hymYWIpDq0mPQnYQj4XzyMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور هادی خامنه ای (برادر کوچکتر سید علی) و وحیدی در‌ مراسم
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/16399" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16398">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">محمد نعیم جُندیه، رئیس امنیت نظامی گردان شجاعیه حماس توسط ارتش اسرائیل کشته شد
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/16398" target="_blank">📅 15:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16397">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">واشنگتن پست : مقام های آمریکایی فاش کردند اختلاف اسرائیل و آمریکا با ترور لاریجانی آغاز شد
واشنگتن برخی طرح‌های اسرائیل برای ترور مقام‌های ارشد ایرانی مثل عراقچی و قالیباف را متوقف کرده است.
در این گزارش آمده اسرائیل به دنبال براندازی نظام ایران بوده، اما آمریکا به این نتیجه رسیده که چنین هدفی از طریق جنگ عملی نیست و به‌جای آن تمرکز را روی تضعیف توان نظامی و دریایی ایران گذاشته است.
همچنین ادعا شده «ترور لاریجانی» نقطه عطف این اختلافات بوده، چون آمریکا به دنبال فردی برای تعامل در داخل ایران بود و با حذف او این گزینه از بین رفت.
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/16397" target="_blank">📅 14:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16396">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">هواپیماهای مهاجم ، حریم هوایی یمن را نقض کردند، پدافند یمن درگیر شد @withyashar
🚨</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/16396" target="_blank">📅 14:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16395">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/16395" target="_blank">📅 14:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16394">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nhVWsEZ8-f4D5Q4W7YFU_Cs_pr_a6SdUjqxsFGYcg9Js4tvv5Si5nflGuSPqGmh9qCvxZmi_OZmi8hP8CwWWL3gGBZ2Fpf9-WdNarfUWZq3IX2h9owgLeQEBUo4pmiPGCD_BBXfE-9iBpsiQMkvDE3eGT7mp_ZinQYTToUJY41m8voxT8thAjsGDZk2S3cr76sFJmCrx9DA2hhhM5Jn9TYcywhtbpIhqB-e0RriQIZADQymB_7oBnueTGxYuPK6brqcZ-kMgvQgLqYRc_L8ISz7GBRSVdG_43jCNgdMQk3ng3J0pk-JbfnzUz5Akx08zSDkEUvcKhw68s8ZrW9CG9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فشار فروش آلت‌کوین‌ها به پایین‌ترین سطح در چند سال اخیر رسیده؛ به‌طوری که اختلاف بین خرید و فروش در آلت‌کوین‌ها (به‌جز BTC و ETH) به ضعیف‌ترین وضعیت چندساله خود رسیده است.
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/16394" target="_blank">📅 14:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16393">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TBQFExAEXAx-LlzywAYB1JDnDLFnLHF55rscWy6BBocnP4uA4UhTuPCPfT8_p7kJxL_CWZw5Fl6Q0-5wcYeQtnPbU4JugSPS14X-JpQA2-7zNhitE00J7iAR7T_HmUU_o-cxv5Gpa6AO53VSqmuEBYFC3-VnLmAW-z9fBSu3baKKcZpAKDWTQpkf1VyIEr7upnlzI62ffM6XB1CPaQ4sYMRZlgppYYR3KCRoLKJmISD83XIRKd3W3sSMz1Vo6Aii4U3Dc-lPdeIe-NGbxkW151ELUDr9l7dfTtKV4z-K-YOmag4RieIFVVGdyrMtDNaMhokGBzgTYgMCnMJNZmXCaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارزانی، رئیس اقلیم کردستان عراق، با قالیباف دیدار کرد
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/16393" target="_blank">📅 13:43 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16392">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">تکلیف امتحانات نهایی دانش‌آموزان مشخص شد
رییس مرکز ارزشیابی و تضمین کیفیت نظام آموزش و پرورش، با تأکید بر اینکه برنامه امتحانات نهایی و کنکور با هماهنگی کامل سازمان سنجش آموزش کشور تدوین شده است، گفت: امتحانات نهایی پایه دوازدهم از ۲۱ تیرماه آغاز شده و تا ۱۲ مردادماه ادامه خواهد داشت. همچنین امتحانات پایه یازدهم از ۲۲ تیرماه آغاز می‌شود و تا ۵ مردادماه ادامه دارد.
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/16392" target="_blank">📅 13:12 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16391">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">WarRoom with YASHAR
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/withyashar/16391" target="_blank">📅 13:06 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16390">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">1$ Tether 176,000 Toman
Brent oil = 71$
Gold = 4173$
BTC/USDT binance = 61,685$
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/16390" target="_blank">📅 13:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16389">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WSsUFdSPhgHot99Uap5COcpWYwerd5IaKMid-EZPKki3nHkr4j4o9l1aMRTIeBLEIImqGFD6R4W4EcZ4hEe8aKHu9N_jwZHhb-5e-GTJsQLwke3I4ZBbQyZe7ldlWUHzNxj6QJsoY2YEOVKuoC6dx8OqJCEGsMNsUJwX_zKDf8hmeLXWlHYMUBLd6RsmBsd5tP9QaBB3_MIUg5ge5g6b3fAYpz89MDlRua6-smPhc_SBbcceLXSozAdWmfpia1uifVo3UHbnLNl_sp0yKH9k2TMOKsBqP58Lprq6n438NsLrK_CYRyVRqOhBKMcbbm50GaaHS3DyZSSLXxjJBcuyHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این عکس از تفاوت تابوت محمدرضا شاه و علی‌ خامنه‌ای وایرال شده، تابوت شاه کاملا ایرانی و تابوت خامنه‌ای  انگار پرچم عربستانه
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/16389" target="_blank">📅 12:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16388">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">فیلم مستند «جاسوسی از تهران» هم اکنون با زیرنویس فارسی
🌐
@withyashar
🌐
instagram.com/yashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/16388" target="_blank">📅 12:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16387">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">۴ تن از نیروهای نیابتی جمهوری اسلامی عضو کتائب حزب‌الله توسط سرویس ضدتروریسم عراق (ICTS) در بغداد بازداشت شدند
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/16387" target="_blank">📅 12:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16386">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DDwE16fpBV2nxlLTUJmeINNnk0nS7rWIOdQgcUUEbUY_OwRmGMHtZNNiCbKCXPsYmHkur8fToRtNM7CHIg3J48KzgoxOsZsOtiqekhe4_rM0ci8WMAOl6mrenthXqTLvD1DDQvI4XweMK64M9XXKM0_iYuuZgOlcurfo-zUM4sewfQDA1ldoMAjJ3jpkEAms0sF1hYCieF5PUJi9LFiX89QYs6c3FPlqWmCQnOjHtw9-LQJPMJ9rWZ5CtcQo_Se534DExHoPk7WsYueVMRNMYor7g6lE2bwBvTAuTyuHbsTKrXI_lTqMvm5vs5qEMZB3vHkLz4IBzrs8P7jZTFrUdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رادان : یک بمب گذاری ناموفق در مصلی خمینی تهران شناسایی شد و خنثی کردیم
با برهم زنندگان امنیت تشییع جنازه بشدت برخورد خواهیم کرد
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/16386" target="_blank">📅 12:19 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16385">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">پشت گوشتون رو دیدین، بیرون رفتن ما از جنوب لبنان رو هم میبینید. @withyashar بنیامین نتانیاهو: تا وقتی تهدید برطرف نشه ما از جنوب لبنان بیرون نمیریم.</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/16385" target="_blank">📅 11:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16384">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XgiY-HETiabVSbsD-3ML6Rratqg3A6JxSFnuNExY-RAXKn6UdUmK8rpa3WTGUapnAYBzq6IINtUuekg9mnxzsxTiuQ1dMAkEotAlr6KSiRHYaBGCZ049-9p2ze1j1f5XMidf5Lvq-BAepqdhPlsesvDnHa-UR70uddz2t_86JRkQgk9VbSfpHJHoOVtPRUHqiDiKzYUNLrV0PZhFWx-O5E6bbnGpT_e5EshaLS009JiOmn9YJ1LVYXlFj2y0_xwaQByIGyTm1bDy8J7hCeuZ0U44piwpNB3FUDU4BG-ILGFudxs87H8tiK2--1ajJBmC4dZFZybuPrgHtgqQPt79Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">براساس تصاویر ماهواره‌ای به تاریخ 7 تیر 1405، آواربرداری و پاکسازی اغلب سازه‌های آسیب‌دیده در جنگ اخیر در حال اجرا است و برخی از آن‌ها کاملاً پاکسازی شده‌اند
هم‌چنین جزئیات موجود در تصاویر نشان می‌دهند که فعالیت‌های تولیدی در بخش‌های سالم این مرکز با شدت بالایی دنبال می‌شوند
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/16384" target="_blank">📅 11:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16383">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">کل تهران در زمان خاک‌سپاری رضا شاه (۱۷ اردیبهشت ۱۳۲۹) جمعیتی حدود ۵۵۰ تا ۵۸۰ هزار نفر داشت.
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/16383" target="_blank">📅 10:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16382">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/voWTmHfEE7rISwQJsCwmuf_oilWfIv1m2tXUZGS3tzZ1x6lp7Nn6sOeRv0YqceDrT60b3sjQjcAP9pgb8FGUIQIJzo4O02vE9XNma8y2cm7RTasMUC6qPFFtO1Z22jiz9mLsJjy4BHFVzZPUi-mBkAl42MYTR-EPf78eNdtN4gzRC4nI5-9yGwsEOkLZ_odY-fDCtoxCQo1gWlTtxbuCkif1ghxpED9rWP2SE2HhCVdMhsloNXMNRUSSYWfIqHqXSnDBxlVFiacm4ZpZNPpHFmBNojAFM3I4TGgmGs6jeeo_3JEE1u44rc00n7FU__m4fPFj5lgSki3Q2LG16ou0yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤡
@withyashar</div>
<div class="tg-footer">👁️ 99.6K · <a href="https://t.me/withyashar/16382" target="_blank">📅 10:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16381">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">سخنگوی کمیسیون امنیت ملی مجلس:
به دلیل تهدید مداوم وزیر دفاع اسرائیل به جنگ و ترور، ممکن است در دکترین هسته ای خود تجدید نظر کنیم.
@withyashar</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/withyashar/16381" target="_blank">📅 10:22 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16380">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4ERdHy2cCdAAGj5RKyR9g8XCI1EglwmtmILeREp5zmtO1-hah0y31tVcu3w447bb7i3Fei4GK4M0ARWK17I-5Ya7sPAiFtMOdMAvnuZcIiegV2YSRrTJPOmdmrNc3uI1UuO_anM48RNWFGe67LJznoU--2KSH-6K1fjtfoQv7ezaq5RC1Bojjb2veFTEDIqz_f0uskE11zcyHDrUyMzld5rlK4iqImQNqMpcUYrirp97HKZBRv9ajMP6oYDlYTdc09pafWS-MmbKxO4OhSbcV8dCEZ_GeTs12Oq-9me3-SIrxSuGyh9PrH5RliGg6JAhEfwpTFoiPkHYjHwcu-Aag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادای مفلسی احمد مسعود
(فرزند احمد شاه مسعود) و هیئتی از افغانستان به تابوت علی خامنه ای
@withyashar</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/withyashar/16380" target="_blank">📅 10:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16379">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">هواپیماهای مهاجم ، حریم هوایی یمن را نقض کردند، پدافند یمن درگیر شد
@withyashar
🚨</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/withyashar/16379" target="_blank">📅 09:53 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16377">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ورود هیاتی از حشد الشعبی عراق  @withyashar چند نفر از‌ موساد حظور دارند ؟
😁</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/16377" target="_blank">📅 09:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16376">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ورود هیاتی از حشد الشعبی عراق
@withyashar
چند نفر از‌ موساد حظور دارند ؟
😁</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/16376" target="_blank">📅 09:26 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16375">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ترامپ: من به دنبال تغییر رژیم ایران نیستم
@withyashar</div>
<div class="tg-footer">👁️ 99.6K · <a href="https://t.me/withyashar/16375" target="_blank">📅 09:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16374">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">اتاق جنگ با یاشار : با توجه به داده ها به نظر میرسد کشتیهایی که از مسیر امن آمریکا در نزدیکی عمان رفت و آمد می کنند، نسبت به مسیری که جمهوری اسلامی تعیین کرده بیشتر است. @withyashar</div>
<div class="tg-footer">👁️ 98.6K · <a href="https://t.me/withyashar/16374" target="_blank">📅 09:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16373">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2642f2a070.mp4?token=X-JbH7WKtAjv4zKy7sx5z1k8sHLRimx3fdu6ODTRbwQ3-R7kzlNXK4G4P1w-Nx4hqJ1McgiD_2wlpE73DyP1MBHnwRNPtnfT89pkf48QjjpWOOZPniImyKkSYnTbi9MEjnG2eZD_C9WPBJqNEJfr2mY4mMu4T8Rt2bcL6kPyv9bzOcss1yfcR_ve9fmQtMXzkm8OG0F-OOyHawAFvOAatI12GN6L_VbLgcVacf-hisk1ANAJWeRau5sTeoyyEoibtT2gv_Lezlaf6pk2zK9U7Mrqx4-BXPDTozVUlZH9bcQkKUsgfHY9BVR3HLiy4AIkNGB8QQOqoFQq461vSSGaBYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2642f2a070.mp4?token=X-JbH7WKtAjv4zKy7sx5z1k8sHLRimx3fdu6ODTRbwQ3-R7kzlNXK4G4P1w-Nx4hqJ1McgiD_2wlpE73DyP1MBHnwRNPtnfT89pkf48QjjpWOOZPniImyKkSYnTbi9MEjnG2eZD_C9WPBJqNEJfr2mY4mMu4T8Rt2bcL6kPyv9bzOcss1yfcR_ve9fmQtMXzkm8OG0F-OOyHawAFvOAatI12GN6L_VbLgcVacf-hisk1ANAJWeRau5sTeoyyEoibtT2gv_Lezlaf6pk2zK9U7Mrqx4-BXPDTozVUlZH9bcQkKUsgfHY9BVR3HLiy4AIkNGB8QQOqoFQq461vSSGaBYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون بمباران شدید جت های اسرائیلی در جنوب لبنان، چندین انفجار مهیب در عمق جنوب لبنان به وقوع پیوست. @withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/16373" target="_blank">📅 02:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16372">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XS73uBTMEtxpnqeNOf1x5IRBbAxTsX2hxGNeeySbLr0oyJRdTxsSYC2QvrTB3LdqIYJKuV3xxEMrBCtSbRQiGh7w0b_t0QQZqFyrfTTFHoCo27Dosxdo19kVn8OfrHNXGWyNcxrEbyTBdVACkZvxu9VGJRihNU37HZ7kk3yhokGV68hwJV_zd1OK4W6aoCWdKweEWfFP_jddcKSAz4sJPMOMxJNtgXZWiXP7u6Y04CM1FGCqa3ShpBIXbyK7s1Sb7nDyp6J06XefDHbH0TZDUHdSwZt98L3-1p9IkdoM_kfM_qHQ3mEjx2xRmBlN2ed4bQ_fq7heTFGe4ciXZ4t1Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان تجمع و عزاداری شدید نیروی هوایی آمریکا برای عظما
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/16372" target="_blank">📅 02:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16371">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">هم اکنون بمباران شدید جت های اسرائیلی در جنوب لبنان،
چندین انفجار مهیب در عمق جنوب لبنان به وقوع پیوست.
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/16371" target="_blank">📅 02:07 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16370">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eH-mhWi3jl6hSed4QHRyTjs_PNiYUJnNhTJESnkJqVPaePtwC55ieFD-_p64pus9dgw8pTclc6NI7UGXSL7o2KQLrXLoh5aYdB03CFgnrKlEDZ-Gv5IrC2j1UCQz0wMU9xVBylMYFORPiswhfi8eqrGt0CFpGEmqPYzS_s6Q4T1Gf479UqniFwA12YupqPAWP8XBqc5ixnz6wddKvAYt7hmjCuaomvYWp1n6_I0o8pixPUadm2WznI38Ilr-BTEbEX1SnaLdUoSutB0MocALE6Jxe0qJeuHfm0xOJP5IySZ6Lb-qFLWkBsUmov3icaCB6etHAROkaL0hM4fXKmzi5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ما رادار ایران را نابود کردیم. آن‌ها هیچ راداری نداشتند. و هنوز هم ندارند. ما هفته گذشته دوباره آن را نابود کردیم. آن‌ها یک رادار جدید و پیشرفته داشتند. آن‌ها آماده بهره‌برداری از آن بودند، اما ما آن را نابود کردیم. @withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/16370" target="_blank">📅 02:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16369">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3226c235ec.mp4?token=b5vqPnRmWTJCtkpAHrxXoybGcYeDMKTZ-c2sIkf8RbogMHUXO7eKqbDip-o6DCsG21gXnbzD0x5DjgVN459F-CxXWQQlSiXKOL_wP-0qSP6TpkII7Bdr3Ymwhv5rePDY44boGtBt2es_qAMC3497JcWAKTuKQin3KGFXCrURb0IiwhKkgPHWotKlWD5mAYXSMvR_HIqVljzly1gbfOdVWuLvUlW34wJWMHFKaPDZqHsL9QSe2Lwv0_mK2lbpnu18ZF14mXlB_WKlcZIPUT37Ro93yOHMJeRuL9bSjCHccSTWf6lpJjs7mocspMVjzfDH5-NTerwjmGtc8E3TaZoWrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3226c235ec.mp4?token=b5vqPnRmWTJCtkpAHrxXoybGcYeDMKTZ-c2sIkf8RbogMHUXO7eKqbDip-o6DCsG21gXnbzD0x5DjgVN459F-CxXWQQlSiXKOL_wP-0qSP6TpkII7Bdr3Ymwhv5rePDY44boGtBt2es_qAMC3497JcWAKTuKQin3KGFXCrURb0IiwhKkgPHWotKlWD5mAYXSMvR_HIqVljzly1gbfOdVWuLvUlW34wJWMHFKaPDZqHsL9QSe2Lwv0_mK2lbpnu18ZF14mXlB_WKlcZIPUT37Ro93yOHMJeRuL9bSjCHccSTWf6lpJjs7mocspMVjzfDH5-NTerwjmGtc8E3TaZoWrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما رادار ایران را نابود کردیم. آن‌ها هیچ راداری نداشتند. و هنوز هم ندارند.
ما هفته گذشته دوباره آن را نابود کردیم. آن‌ها یک رادار جدید و پیشرفته داشتند. آن‌ها آماده بهره‌برداری از آن بودند، اما ما آن را نابود کردیم.
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/16369" target="_blank">📅 01:53 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16368">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cdd54f95b.mp4?token=us-AY9jlFQZrzr9t-4OUCPgmvJf1-PSLNTfKZqvEJGGg8yl9RvfQtelm49Vv5gFdXMZ01uqMTQNcdXG6pom8Kk5Y0-bnV1TztPLSE0mUCl-l7UhhQTXMqdMeUuHKdQfEO2BGnQMGgbzJDne7eLjhJY52EW8f_wu2wlm1NsExQ84irvxvDZOmgADqLEKcMfnJbJKeCLqDbW6qrzGhHf8pIN4G0CYvDGNIRIZW7IOJULleFthUaHsgm8r0hObzTtzFSZ3wGKXV2Toax31QVKYV7oBLDJx8UokPQl20eSz-DEKzJN4nHbea-z5a_9_V57Yb-AdXPAuFeIFUxXL-nbUDqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cdd54f95b.mp4?token=us-AY9jlFQZrzr9t-4OUCPgmvJf1-PSLNTfKZqvEJGGg8yl9RvfQtelm49Vv5gFdXMZ01uqMTQNcdXG6pom8Kk5Y0-bnV1TztPLSE0mUCl-l7UhhQTXMqdMeUuHKdQfEO2BGnQMGgbzJDne7eLjhJY52EW8f_wu2wlm1NsExQ84irvxvDZOmgADqLEKcMfnJbJKeCLqDbW6qrzGhHf8pIN4G0CYvDGNIRIZW7IOJULleFthUaHsgm8r0hObzTtzFSZ3wGKXV2Toax31QVKYV7oBLDJx8UokPQl20eSz-DEKzJN4nHbea-z5a_9_V57Yb-AdXPAuFeIFUxXL-nbUDqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدیو رو قبل از خواب ببینید تا پستای قبلی جمهوری اسلامی رو بشوره ببره.
@withyashar
🌟</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/16368" target="_blank">📅 01:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16367">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">فیلم مستند "از چشمان جاسوسی درتهران" که حاوی تصاویر مستند از چشم موساد در قلب‌ تهران است و از شبکه ۱۴ اسرائیل پخش شده است.
@withyashar
نسخه اصلی با زیرنویس انگلیسی و حجم کم تا بعد با زیرفارسی شو بزارم</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/16367" target="_blank">📅 00:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16366">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdc81a4ce6.mp4?token=Mc0lZ_6fN7v0Kq5sCN9RgcyzmLO0Byx8q7dKxEmUgUCSMrgnaEFJ7FeJgI-nC4276_0N9Z8x_qV8qPIXtTEjl-2RQTq4aCeMV40KemrKhqY7xA88TkDKSo0iIPuABRFBzyYpeAeFXVKjW92q8wUcUH1uzNCTYAVQ3SuobXFlCkccEL0jVuECplF4QbQaMrQj_FHVZPTt_HM5-67Ww1UrjtckmF4NbqJL0fCHl8MI69doMQeN2dQFp8RF0bvNK-Mm9orV9uh1-bl7PI3NJ7i5EvtyIhXxkeLK4NfNa2jyCHm1XUWx45rmtJosTaMxwI-ca80TEqWJ9CwTVKY3UahhlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdc81a4ce6.mp4?token=Mc0lZ_6fN7v0Kq5sCN9RgcyzmLO0Byx8q7dKxEmUgUCSMrgnaEFJ7FeJgI-nC4276_0N9Z8x_qV8qPIXtTEjl-2RQTq4aCeMV40KemrKhqY7xA88TkDKSo0iIPuABRFBzyYpeAeFXVKjW92q8wUcUH1uzNCTYAVQ3SuobXFlCkccEL0jVuECplF4QbQaMrQj_FHVZPTt_HM5-67Ww1UrjtckmF4NbqJL0fCHl8MI69doMQeN2dQFp8RF0bvNK-Mm9orV9uh1-bl7PI3NJ7i5EvtyIhXxkeLK4NfNa2jyCHm1XUWx45rmtJosTaMxwI-ca80TEqWJ9CwTVKY3UahhlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌های یک مداح حکومتی:
ترامپ رو هلیکوپترش غیرت داشت، اونوقت رهبر رو زدن هنوز خاکش نکردیم.
چرا راستش رو نمیگید هسته‌ای رو دادید رفت؟ چرا نمیگید هر روز لبنان رو میزنن ولی بازم کاری نمیکنید.
۱۰۰ میلیارد دلار طلب داریم، بعد برای ۱۲ میلیارد دلار مارو کشوندن پای میز مذاکره، تازه نصفشم گفتن ذرت و سویا میدیم.
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/16366" target="_blank">📅 00:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16365">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd374ffde1.mp4?token=Ske18B43jdJttgcznUU1L_HGk21VtfqaphKdhoF7S_j5yxJ98WGdRxgUMEjwHBP0iI1n2nE05FipInkjN6OqT1LoOV4xXFLSZcByTno52BoGtsIctszkiZQWoKcDF3cHtO2OoYlbiKt7Fgn0gufSsPlSgl3wWDptPzsmUpA5Zfa6NWsYinog4LW-X_ws6tDpmd_1_aMwcdQ94fGxUXyuNxT-eLg8FUsQwhu0kAxAqGCv19fOIegxK-IFigxkKQewEyHwmFGMgSjRE7zlNoGx2cQiwmw-rhujjyOCCCmHEDQlnODvpKLknUBiNWtqW6vbvS2Yva2cWdAfcsGgxA1Ung" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd374ffde1.mp4?token=Ske18B43jdJttgcznUU1L_HGk21VtfqaphKdhoF7S_j5yxJ98WGdRxgUMEjwHBP0iI1n2nE05FipInkjN6OqT1LoOV4xXFLSZcByTno52BoGtsIctszkiZQWoKcDF3cHtO2OoYlbiKt7Fgn0gufSsPlSgl3wWDptPzsmUpA5Zfa6NWsYinog4LW-X_ws6tDpmd_1_aMwcdQ94fGxUXyuNxT-eLg8FUsQwhu0kAxAqGCv19fOIegxK-IFigxkKQewEyHwmFGMgSjRE7zlNoGx2cQiwmw-rhujjyOCCCmHEDQlnODvpKLknUBiNWtqW6vbvS2Yva2cWdAfcsGgxA1Ung" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاستگاری‌جنجالی نوک برج امپایر استیت
دو شهروند روس پس از بالا رفتن از نوک آسمان‌خراش «امپایر استیت» در نیویورک، در همان محل مراسم خواستگاری برگزار کردند، اما پس از پایین آمدن از ساختمان توسط پلیس دستگیر شدند
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/16365" target="_blank">📅 00:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16364">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">لحظه ورود تابوت علی خامنه ای به مراسم
،
امشب در حسینیه عمام خمینی
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/16364" target="_blank">📅 00:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16363">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">⁨ اتاق جنگ با یاشار : خشک خشک ، از دیدن بشقاب پرنده بگیر تا نرم باز‌ کردن تنگه هرمز
💥
کارای اداری یادتون نره ! برام بنویسین چند وقته منو دنبال میکنید ببینیم ترمیناتور شدید یا نه
😁
⁩
https://www.instagram.com/reel/DaTbNq0x1Pf/?igsh=cmx6bXhnYXB6aTN5</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/withyashar/16363" target="_blank">📅 23:50 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16362">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">بلومبرگ:  ۵۸ میلیون بشکه نفت و میعانات ایران روی آب انباشته شده و ۹۰٪ این محموله‌ها مشتری یا مقصد نهایی ندارند.
با وجود تعلیق ۶۰ روزه تحریم‌های آمریکا، خریداران بزرگ همچنان با احتیاط عمل می‌کنند و خریدها محدود مانده است
@withyashar</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/16362" target="_blank">📅 23:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16361">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fd6-WGJiGyL2sGX75_B6xes8blZ0wjJk-MPLezRf94TRiis0NHHRwk3Me7pNyy_7mdTCmpcknEs3iwJ3GDOY0PO6iND8KHHLJldbGhNiji7W-PVtQedhlFzpzKRRtrXHJcQ8P8N95ZbeywH1W4hqtbJDElN1_dWQjaIrDU-s0xMSPLoPqGwL8fsJZ_Am2iRRukyxL4kiW06GXjEKqHl7DMPH0j7CIy-Xs2_aWA5_I94hcWJwlMn5lcLuiVtp18W0sW-CiDO6msJCvk5EHUqKVTFzBIgXVj9eKFHD4bqVdFy1meob7KwXIRe32JDU6BLtpNIIdfdlVP1b4EjDDazGhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاور پست جدید اتاق جنگ
💥
@withyashar</div>
<div class="tg-footer">👁️ 99.2K · <a href="https://t.me/withyashar/16361" target="_blank">📅 23:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16360">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">مهران مدیری : با مرد ۳ هزار چهره که دارم میسازم باز به اوج برمیگردم
@withyashar
😐</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/withyashar/16360" target="_blank">📅 23:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16359">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vy1MbCIX1rhHliOEORBeOOXdOpHwJOPa3VclHFmsUcn3FrAFMvrwqmreqNfcYhpkjLeChDBxIo5xEF-PGXoMqXsP-9XXMEdg4FLtbLfWpzCED9hSuzPMfzqxe4CkcJNF4FEjrCjxHzTSSDAtxK7HhkmMen8oBQhl-GW8LG6jI6ShtavABZUtY0leu61N6m13jqRDGz153uZvs4NuieYTgo9qgR7eCrMqAI9GubO8dMmHaDM5DUWsys8nGBsyQILi8CuYM1i-k6B4nq1NfXCCZRb40LnAM6LCa8A1Yg1Qbu81blBSyVlRbbsi9py9pmHHX27QObG53vzKk37xHwShRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه های عبری در‌سالگرد ۱۰۰۰ روز پس از ۷ اکتبر : آنها بدون هیچ نشانه ای از حیات، در حالی که در آغوش یکدیگر در تخت خواب قرار داشتند، پیدا شدند. یک خانواده کامل که در تاریخ 7 اکتبر به قتل رسید.
ما آن را فراموش نخواهیم کرد و بخشش نخواهیم کرد.
💔
@withyashar
یاشار : اسرائیل درد مارو که ۱۸-۱۹ و کل این ۴۷ سال کشیدیم با تمام وجود درک میکنه و اینارو ول نمیکنه خواهید دید!</div>
<div class="tg-footer">👁️ 95.8K · <a href="https://t.me/withyashar/16359" target="_blank">📅 22:53 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16358">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">نیویورک تایمز گزارش می‌دهد که هواپیمای قالیباف پس از آنکه نیروهای امنیتی ایران در مورد اطلاعات مربوط به قصد حمله اسرائیل به آن هشدار دادند، در مشهد فرود اضطراری کرد و مدعی شد که دو جت جنگنده اسرائیلی وارد حریم هوایی ایران در نزدیکی مرز عراق شده‌اند. @withyashar…</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/withyashar/16358" target="_blank">📅 22:50 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16357">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-footer">👁️ 93.4K · <a href="https://t.me/withyashar/16357" target="_blank">📅 22:43 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16356">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">نیویورک تایمز گزارش می‌دهد که هواپیمای قالیباف پس از آنکه نیروهای امنیتی ایران در مورد اطلاعات مربوط به قصد حمله اسرائیل به آن هشدار دادند، در مشهد فرود اضطراری کرد و مدعی شد که دو جت جنگنده اسرائیلی وارد حریم هوایی ایران در نزدیکی مرز عراق شده‌اند.
@withyashar
🚨</div>
<div class="tg-footer">👁️ 97.4K · <a href="https://t.me/withyashar/16356" target="_blank">📅 22:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16355">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7W_VQKidkbJcYIbib14ix2QIW3Ldq7q9bjEw8a2_o22VgjWY10McfwaZhzJhFmwSXqvbo1Vh8ASsErV8p6myurK5g5iNjPBQSNpLNhdqhJVKNpcrPczNAjeYxcHp_7aOFV8gx7zBliGWA0WB-_9akCdEndx2p52Kxcm7o_Dovm3YYNxxEH7-fAK9WSF7utio5XciLpjxBNGjII2p3XbDbg6KT014cyT7SJOhjqF_OeVkWXar_Oq0dbGssqU_u8bTrKAZXqSVice174-ztzzgAqThxKpirS9ZkxZlWyJXFqgEPiu1ptK-F-AkDEp1b0Xk9nDW7ZoyhA1HIJ7m5e8zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشت گوشتون رو دیدین، بیرون رفتن ما از جنوب لبنان رو هم میبینید.
@withyashar
بنیامین نتانیاهو: تا وقتی تهدید برطرف نشه ما از جنوب لبنان بیرون نمیریم.</div>
<div class="tg-footer">👁️ 96.3K · <a href="https://t.me/withyashar/16355" target="_blank">📅 22:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16354">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ishuHrSbiS1d-Q_QfnsmNxARnJNJG8qLxOqz4ApT0u0CnNh1wOomBYhwQ31CwV0a1h12etTuJEz_7mXjcPskYbw-2RcCJDhSAZN6uqYHVptx2nehTgQt0NldK-ErE7yUA4MdWcQxRjLHZo2ZzoRrt4x8ZBNZLoY55o67jZ9KRgszcPIKR3o2valAmKxo5OXgSy7GdVKEeG1YTdSX5BJrFomGO8P8yB6BqAuHsFYExA13rVoOvoAvJzWPL3ZKhahAOMAISnL0Uy3B6p3_WWOunHHtkERaKc1LJ3-qv_spzzcDmKe2VlcVKVqA3KMvj6Rq7FftAyCrWp9_PogOInoZaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام صفحه مجتبی هم اکنون
من این توفیق را داشتم که پیکر ایشان را بعد از شهادت زیارت کنم؛ آنچه دیدم کوهی از صلابت بود.|  ۲۱/اسفند/۱۴۰۴
@withyashar
دروغ نمیگه تو اون دنیا بدش دیدن همو</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/withyashar/16354" target="_blank">📅 22:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16353">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">وزیر دفاع اسرائیل: ارتش اسرائیل باید برای انجام جنگ مستقل علیه ایران آماده شود
@withyashar
🚨</div>
<div class="tg-footer">👁️ 93.2K · <a href="https://t.me/withyashar/16353" target="_blank">📅 21:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16352">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b7b14f43a.mp4?token=nHFqOdhDmpulVCf7VV9OlJ0kcnvDUVJy4weF8ZC4p-3orVKu-Acj2qYmIy2N5_uLjBXKwiyFMDssZ4lnMYQp4BvvUg42a8Lfl-8_2wV6ST6oKxP3wP5_XrJ7KfNXO0opkcTHZoUr6YQWRwgiXVIWnnFsJ15HykUybVAxqlnPCQzfhm_x3LX-ZIE4Agnrr3ps_okhdtyA3L3VSNXma2dOeFqBhP-_pV-ikWN0MKjNckNDh9YdNDOf_WXig_M4G_ypbKlO0p9gc8F5akd-IyB5soodd1x7cGeZYOxm5gAAVFzb1-Lbk1Sv3Sw7vEw2lWID2NNUM8uGyAh2VzUeDM8uUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b7b14f43a.mp4?token=nHFqOdhDmpulVCf7VV9OlJ0kcnvDUVJy4weF8ZC4p-3orVKu-Acj2qYmIy2N5_uLjBXKwiyFMDssZ4lnMYQp4BvvUg42a8Lfl-8_2wV6ST6oKxP3wP5_XrJ7KfNXO0opkcTHZoUr6YQWRwgiXVIWnnFsJ15HykUybVAxqlnPCQzfhm_x3LX-ZIE4Agnrr3ps_okhdtyA3L3VSNXma2dOeFqBhP-_pV-ikWN0MKjNckNDh9YdNDOf_WXig_M4G_ypbKlO0p9gc8F5akd-IyB5soodd1x7cGeZYOxm5gAAVFzb1-Lbk1Sv3Sw7vEw2lWID2NNUM8uGyAh2VzUeDM8uUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبکه 14 اسرائیل قراره سه‌شنبه و چهارشنبه، 16 و 17 تیر مصاحبه ای که با جاسوس های موساد و شاباک تو سپاه کرده پخش کنه
@withyashar</div>
<div class="tg-footer">👁️ 98.9K · <a href="https://t.me/withyashar/16352" target="_blank">📅 20:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16351">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">کامنت جدیدم برای ترامپ. حتماً فقط همین کامنت را لایک و ریپلای کنید. میتوانید با اد استوری ( با نگهداشتن روی  کامنت)، انتشار بیشتری دهید.  https://www.instagram.com/reel/DaSrqH3NjVK/?comment_id=18333946015271080  ترجمه : آقای رئیس‌جمهور،  بسیاری از ایرانیان…</div>
<div class="tg-footer">👁️ 95.1K · <a href="https://t.me/withyashar/16351" target="_blank">📅 20:11 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16350">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">نماینده آمریکا در شورای امنیت: اجازه نخواهیم داد هیچ عوارضی بر تنگه هرمز تحمیل شود
@withyashar</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/withyashar/16350" target="_blank">📅 20:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16349">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H9ijn5Qs38yDvYZUbtmBCx_piJgSOnAe3A6d489VUULHN50Rna64JcBfF2QroQwLVGwg-4aDGlhIVD9584G6lNFnAuY8I8vtz3S7mzrl3KwVPlduae-4BNJfewZ0Ecg3riHeo19-2rXPmSi2FUolFbk-Ncs_LATI7TuVulbmlni1n3MU-qC4ohfjUAg004ggy_xRoggG3NswOsAPhN-I7AbnYsa-_mVShHx9itcgt44TegAWh2z7ZnEiVIVzsELuT9nWpbIAYIndbGzERzcfFj6PYH1yEkRGryxkNFgEZgSNql0oi5t9yM9rLiGatzL4uuK6Sp0IIh1WCipdoTdZUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وحیدی؛ فرمانده کل سپاه پاسداران برای اولین بار بعد از جنگ رویت شد. @withyashar</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/withyashar/16349" target="_blank">📅 19:46 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16348">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FFfVq6uXZWG_bap1A4oNpmfqb-kFS6sVXtlBG7AjS3Py8z-N75ARa1oMm3w4Nwx0XYLG2R1rK_pvUqqPfyGRzS4rorx9Hpu2mmbKAB3TZx38FAWlmJXqeIlwlREuvWXjaWNZrg6LfaOjVIyIbTzYA0DdJBzP-FW6fsyPTxLz0ZLWq343QyNAs-of6__t6E1H72ICoHNfExArF8gFwQCAQ6G7mXFn9-f9MEbf7RaLC-87dm1QC3T91lfeX_FW0LWgkAONdWj_j-vXZu3t5LQosV_VT7u72IJ1Da_un2mST5tk99dkBUmFTrLjainIvKNIEPHEUIi2OLVTTqWXrPXVcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وحیدی؛ فرمانده کل سپاه پاسداران برای اولین بار بعد از جنگ رویت شد.
@withyashar</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/withyashar/16348" target="_blank">📅 19:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16347">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">طبق گزارش ها برخی از مقامات ارشد سیاسی و نمایندگان پارلمان عراق از کشور به صورت پنهانی فرار کردند.
@withyashar</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/withyashar/16347" target="_blank">📅 19:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16346">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">وال استریت ژورنال: ایالات متحده به جمهوری اسلامی گفته است ما بخشی از وجوه مسدود شده را آزاد خواهیم کرد، اگر شما از دریافت عوارض در تنگه هرمز صرف نظر کنید. در حال حاضر، تهران این پیشنهاد را رد کرده است
﻿
@withyashar</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/withyashar/16346" target="_blank">📅 19:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16345">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">گزارش ها از استقرار گسترده نیروهای پیاده نظام و توپخانه ایران در مرز با اقلیم کردستان، عراق.
@withyashar</div>
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/withyashar/16345" target="_blank">📅 19:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16344">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">گزارش درگیری در مهاباد @withyashar
🚨</div>
<div class="tg-footer">👁️ 89.9K · <a href="https://t.me/withyashar/16344" target="_blank">📅 18:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16343">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">جان‌باختن شش عضو تشکیلات مخفی حزب دموکرات در کمین سپاه پاسداران در پیرانشهر
بر اساس بیانیه منتشرشده از سوی حدکا، این درگیری در ساعات پایانی شب چهارشنبه ۱۰ تیرماه ۱۴۰۵، در حوالی روستای قزقپان، در سه کیلومتری پیرانشهر رخ داده است. این نیروها هنگام انجام یک مأموریت تشکیلاتی و سیاسی، در کمین برنامه‌ریزی‌شده و سنگین نیروهای سپاه پاسداران قرار گرفتند.
@withyashar</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/withyashar/16343" target="_blank">📅 18:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16342">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">پزشکیان: کشته شدن علی خامنه ای آغاز فصلی نوین در جمهوری اسلامی است
@withyashar</div>
<div class="tg-footer">👁️ 91.5K · <a href="https://t.me/withyashar/16342" target="_blank">📅 18:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16341">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">گزارش درگیری در مهاباد
@withyashar
🚨</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/withyashar/16341" target="_blank">📅 18:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16340">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">این ادعا که «سرکرده حزب دموکرات کردستان به آمریکا گفته در صورت حمله به ایران، ارومیه و آذربایجان غربی به ما داده شود» کاملاً بی‌اساس و فاقد هرگونه منبع معتبر و فیک نیوز است
@withyashar</div>
<div class="tg-footer">👁️ 90.7K · <a href="https://t.me/withyashar/16340" target="_blank">📅 18:11 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16339">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">روزنامه بریتانیایی ایندیپندنت : لطف‌الله کاظم افراسیابی شهروند ایرانی-آمریکایی مقیم ماساچوست ، استاد سابق علوم سیاسی که در جریان تبادل زندانیان میان ایران و آمریکا مورد عفو قرار گرفته بود
به دلیل رد شدن گل ایران در جام جهانی شکایت ۱ میلیارد دلاری علیه فیفا طرح کرد
@withyashar</div>
<div class="tg-footer">👁️ 88.5K · <a href="https://t.me/withyashar/16339" target="_blank">📅 18:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16338">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">کارشناس شبکه افق، به قالیباف:
این مسیر به جایی نمی‌رسه، حالا دیگه خود دانید
@withyashar</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/withyashar/16338" target="_blank">📅 17:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16337">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/withyashar/16337" target="_blank">📅 17:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16336">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">آبدانان</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/withyashar/16336" target="_blank">📅 17:13 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16335">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">کامنت جدیدم برای ترامپ. حتماً فقط همین کامنت را لایک و ریپلای کنید. میتوانید با اد استوری ( با نگهداشتن روی  کامنت)، انتشار بیشتری دهید.
https://www.instagram.com/reel/DaSrqH3NjVK/?comment_id=18333946015271080
ترجمه :
آقای رئیس‌جمهور،
بسیاری از ایرانیان بر این باورند که صلح و ثبات پایدار تنها پس از پایان حکومت کنونی امکان‌پذیر خواهد بود. از شما با احترام درخواست می‌کنیم هنگام تصمیم‌گیری، این چند نکته را در نظر داشته باشید:
مردم ایران
گرسنه نیستند
(لطفاً به ویدئوی آبادان مراجعه کنید).
بسیاری از ایرانیان از شاهزاده رضا پهلوی به‌عنوان شخصیتی وحدت‌بخش برای یک دوران گذار مسالمت‌آمیز حمایت می‌کنند.
مهم‌ترین اولویت ملی ما، ایرانی آزاد، دموکراتیک و با تمامیت ارضی کامل است. حتی یک سانتی‌متر از خاک میهن ما نباید مورد خدشه قرار گیرد.
لطفاً با آزادسازی منابع مالی یا توافق‌هایی که موجب تقویت این رژیم شود، به آن کمک نکنید.
از توجه مستمر شما به مردم ایران سپاسگزاریم. ما به آینده‌ای بهتر امیدواریم و از تلاش‌ها و حمایت‌های شما قدردانی می‌کنیم
@withyashar</div>
<div class="tg-footer">👁️ 91.5K · <a href="https://t.me/withyashar/16335" target="_blank">📅 17:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16334">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">وال‌استریت ژورنال: در یک تغییر راهبردی مهم، فرماندهی مرکزی ایالات متحده (CENTCOM) در حال بررسی جدی انتقال بخشی از سامانه‌ها و زیرساخت‌های عملیاتی نظامی خود از برخی کشورهای حوزه خلیج فارس به اسرائیل است.
بر اساس این گزارش، منطقه صحرای نقب  به‌عنوان گزینه اصلی برای استقرار این سامانه‌ها در نظر گرفته شده است.
@withyashar</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/withyashar/16334" target="_blank">📅 16:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16333">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">استاندار تهران: تمام تلاش ما اینه که مراسم تشییع رهبر بدون تلفات به پایان برسه.
@withyashar
😐</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/withyashar/16333" target="_blank">📅 16:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16332">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترامپ در تروث : ایالات متحده بیشتر از هر کشور دیگری برای ناتو هزینه می‌کند، و این هزینه بسیار زیاد است، بدون اینکه هیچ سودی از آن ببرد:
آمریکا - ۹۹۹ میلیارد دلار، بریتانیا - ۹۰.۵ میلیارد دلار، فرانسه - ۶۶.۵ میلیارد دلار، ایتالیا - ۴۸.۸ میلیارد دلار، لهستان - ۴۴.۳ میلیارد دلار. سایر کشورها، از جمله آلمان، بسیار کمتر هستند. (۲۰۱۴–۲۰۲۵) مضحک است!
@withyashar</div>
<div class="tg-footer">👁️ 86.1K · <a href="https://t.me/withyashar/16332" target="_blank">📅 15:43 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16331">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">دریاسالار برد کوپر(فرمانده سنتکام): امروز، با افتخار از سربازان و ملوانان آمریکایی که به یک واحد مشترک ضد پهپاد (C-UAS) در بحرین منصوب شده بودند، به خاطر عملکرد استثنایی آنها در سرنگونی ۱۴ پهپاد تهاجمی یک طرفه جمهوری اسلامی در چند هفته گذشته، قدردانی کردم.
@withyashar</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/withyashar/16331" target="_blank">📅 15:41 · 11 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
