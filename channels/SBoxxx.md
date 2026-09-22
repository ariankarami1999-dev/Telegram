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
<img src="https://cdn4.telesco.pe/file/vwjiC215YbqQkyJUV1mMPSEWQV976Tmp5QPArP4xUnM0iFjEaEbsWGDUvsd2A4fmRIudEFhkAcHgxozmqWoNn_SJ9PU4oInEwxACsbPx8co0Yf7qtzOOxKTa9L3scnhbQ8D_F7s1z70IJ-RnwUaRznsjhOpoglfpcRAbg8MbInpDeTlcmIu589_UnNyr1xPvuzZsM7bMEkwjghi8BErWPsWZTngJNmhbG_He_LCc17WsVnwl6zGSqyVEi9cEW_KDYMFjQxbXHwyePVdm_OLW8mm86RMwqDmFpTqIkYFvF7iPUnc3YCg7hzjJL2z_XkwMmbja3V0H1BNWqAxg9imUUw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.9K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-31 13:38:24</div>
<hr>

<div class="tg-post" id="msg-21095">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">— شرکت هواپیمایی ترکیش ایرلاینز، به همراه پگاسوس و ای‌جت، از ۲۱ سپتامبر تمام پروازهای خود به ایران را لغو کرده و حداقل تا مارس ۲۰۲۷ هیچ رزرو بلیطی در دسترس نیست.
تحریم‌های «عملیات سرد اقتصادی» ایالات متحده آنقدر گسترده است که حتی هواپیماهای ایرباس حاوی قطعات ساخت آمریکا را نیز شامل می‌شود و برای شرکت‌های هواپیمایی ترکیه چاره‌ای باقی نمی‌گذارد.
شرکت هواپیمایی ایرانی ماهان ایر نیز پروازهای خود به استانبول و آنکارا را به حالت تعلیق درآورده است.
اسکات بسنت، وزیر خزانه‌داری ایالات متحده، گفت که خطوط هوایی ایران از ۲۳ سپتامبر با تعطیلی جهانی مواجه خواهند شد و هشدار داد که شرکت‌هایی که به آنها خدمات ارائه می‌دهند، ممکن است در معرض خطر از دست دادن دسترسی به سیستم دلار آمریکا قرار گیرند.
ترکیه یکی از آخرین مسیرهای هوایی بین‌المللی مهم موجود برای ایرانیان بود.</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/SBoxxx/21095" target="_blank">📅 13:41 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21094">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ولی من هر چه میشمرم، رفع محاصره یک شرط است نه ۷ شرط !</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/SBoxxx/21094" target="_blank">📅 12:54 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21093">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4lLWAk5pN7nwm794q6FbtOJMnbzmLJZXsVuO9lnEmkIvE3u3bLIq09yVRqY2gFF5TBn2aKk6WQSZruPgSGCO6xeo6Wx0SUnLByBjNPU6aYgkjlYIq34stdF_5pgosSkHCRjuNk3F3PXP4e_ph_ybFSTCyGUEEuMAaj6N0CWpTuTsYsegvEscEdwoK5NuleNpPclH2mIpj5lIYfWA8LGQ9d1jsXRGYf1F8sT_GBUSEpOF7uTcbTZcyRmHB1RaA6TMIXmQJTRTSMlYUCFpnAvSZ_lB34KM0SYF6QtmZ9eRKvioX3uXwGGWlv4PLUk7rzhd1eCUOjDKPpXCDMsPTpc8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران می‌گوید تنگه هرمز را مشروط به رفع محاصره ظرف ۷ روز بازگشایی می کند.</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/SBoxxx/21093" target="_blank">📅 12:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21092">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l77-EeM--tMkLtUYHFV9XzibwQ1rqmP7WcidYBbBoZMqYXJVG9AN6eEILJZsFTGTR3UIVL7ga2ljK7CO-6Y9yfKwxql42ePcheVX57xoF4hKj0Q34IcNsxFHfaqxT4xwfpk1G4yRgkPCyjjOMOELyYZM8GgbmTY0UTlGuRSRSDbgz_zV2gAJrKsht1MdMZEmLkZBpGG1_1LOLqGaSat2IPdlrK-YI81t6qI6wSf69TymZRv5frJUPAE6ZOONhmXVtn1-9TDqL4iiHTgWzNqGmd5hm4fYeaPxuXdaJL6B7qeWcvcjfP5XU90-koxiTJzaymf6i-Yhqa2fcaqWZ_ZfeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سه کله پوک پیمان مکه کم بودند، حالا وزیرخارجه مصر فقیر (خر دوم از راست) را هم با آن ریخت و ترکیب ش add to group  کردند!
فقط سیس هاکون فیدان !</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/SBoxxx/21092" target="_blank">📅 12:41 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21091">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJ-AD6B_jssTLoNaqNBVX_MCvK3N-zJza9lIATpvQLXpj8L8zYLl0LpaJrD3XYISvEVxkczLj1hlaAA6t-2jui9r0xJPG7a7qX4jAQGn_HE8IHU3i1uwctXacQADlCH4V1Pd9GWADtskOTJGGRjbizrjwzmEHl6R9oYkrMTGGp3uqcH6_dZi5x-cVwMwbq0imU3WPhntf-TJIKY2oFTqJGya6-GGk_mPf-jHaE-s3reBw6hZ4j0tQoaxcL8ShZFHp6GA8j8RHo8QoC-QPmij9CRX7L9-xsklkrhlBAAii_HKWS1d612K0_EqxkIp1rl3GgLJnk4ceJqBhU80M469jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve  نمایه FVC کماکان زیر محدوده منصفانه است و هر چه افت طلا بیشتر بشود برای خرید ارزنده تر خواهدشد.</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/SBoxxx/21091" target="_blank">📅 12:36 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21090">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">به نظر من نوعی کرنش در برابر چین از سمت ایران است که نشان بدهد برای حرف چینی ها تره خورد می کند. چین روابط مستحکمی با سعودی دارد و همین چند روز پیش هم مشخص شد موشک های بالستیک DF-21 در اختیار سعودی قرار داده که با آنها یمن را می زند.  در آستانه دیدار رهبر…</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/SBoxxx/21090" target="_blank">📅 12:33 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21089">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">چارت نفت جوری است که به نظر یک کاهش تنش داشته باشیم و دیدار شی-ترامپ مثبت باشد.</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/SBoxxx/21089" target="_blank">📅 12:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21088">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ایران می‌گوید تنگه هرمز را مشروط به رفع محاصره ظرف ۷ روز بازگشایی می کند.</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/SBoxxx/21088" target="_blank">📅 12:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21087">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ترامپ می‌گوید توافق با دانمارک، «کنترل دائمی» ایالات متحده را بر امنیت گرینلند تضمین می‌کند  ترامپ می‌گوید توافق گرینلند، رقیبان ایالات متحده را از ایجاد پایگاه‌های نظامی در آنجا منع می‌کند</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/SBoxxx/21087" target="_blank">📅 12:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21086">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SYinTfyKuDi_9aPn7wKa0PEBR3cV2jEu-wyGXnnYbjklI_0jzgxyPLL5loHRZuEasBo-rZKCVUfmjk1AlRsoBOcwPY8XKbUBhvGjPmxOC6v6dF19z0xXE7wl7PDXwEPFs24C42_xUQCeoYSXiS_x0LbcRDynnn-Gjpmk3mKcNp5ldR755vGdeOiVKOtZj7bLUTpjs-6AEQ6Zbx56q9Ymfefjxw9GaeUPqgE90LVTjIQ-rwOgxN6zdIWtEFlDER9lWboaXQBvBwphU3XzZkklqm2rx0HuKyr3mfj5-hTlecES0bpH5izjpgD38qiO3jXOVIZxenkZQ19qGHlW2gO47A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC کماکان زیر محدوده منصفانه است و هر چه افت طلا بیشتر بشود برای خرید ارزنده تر خواهدشد.</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/SBoxxx/21086" target="_blank">📅 11:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21085">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFrw8p7HQVRpA6HgxOl0WXlTJ1o_DCsy4vOcm6BMDDzGRqRuW2pOahXl6Znk9pdV0GonEMhp8jF6Wpcc5FpclHu6putrWHYrS-KBQJR2QC0BsBWKngXGx2iM-PXzctq2uKEWB0y7teq785mTBxDtCL9L3S0m4wBsqOTKYAY9Cr3COmCLW-szJtPkauRRnbD9hQTYEQu8KujuWBYlj4ulq8-hPU6rkWJsauMVhmRXjqkCh2QrD2gM4dLZo33UB3kpGuizOK1KnYwdMRy2co8LzzuC2A-QeHQ1i1qg6SvyvNs1vCbP23xJRoVwvVT-r83LiNxGoyHbXb7qisHxVPCIVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح بسیار بالایی است. اما نظر به ریزش سنگین طلا، اثرگذاری اش را گذاشته است.</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/SBoxxx/21085" target="_blank">📅 11:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21084">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxb1Ed9I7_YmHeT9Jtnf3ATRX0tTCttvdEkUC0FGkoj6Y6lgIPXlgg1wIYWJh21E_9EFQXPoaHEBmky4P5EAglrY9YEuyvkbwgPBn-49rt4k8R61o9yJKYEHMH80dYnZuyQ7y6gwV6TLGMeHJ2X-gqrnx4uLOSAHz8trz9rG33-U5AUSAhCu90HcG3L03Wd0E55Y98gJjR0Bjqp1wkCw4tLPjlOh4bmic33PzyCqRQDkN2xpVKW9xXbn13rIYffyWJ0LxtZzPsAV0f0yHCF2hDbILdyT0ikdpCWbLFCqB0S_w29n5x1AaHKjBPrdDUeSSdisaXMbxKus4q_CZCDkdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک پله خرید طلا توصیه می شود.</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/SBoxxx/21084" target="_blank">📅 11:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21083">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">کاخ سفید، پخش ۲۴ ساعته‌ی «کانال تلویزیونی ترامپ» را آغاز کرد
!
کاخ سفید، پخش مستمر
«کانال تلویزیونی ترامپ»
را از طریق یوتیوب و پلتفرم X (توییتر سابق) آغاز کرده است و وعده داده که سخنرانی‌ها، اطلاعیه‌ها و مهم‌ترین بخش‌های فعالیت‌های دولت را به صورت "به‌روزرسانی لحظه‌ای" ارائه خواهد داد.
کاخ سفید در پلتفرم X (توییتر سابق) اعلام کرد: "شاید همه لحظات مهم در تلویزیون شما پخش نشده باشد، اما اکنون این امکان وجود دارد."
کانال یوتیوب، این پخش را به عنوان
«پایگاه اصلی»
معرفی می‌کند و وعده می‌دهد که مهم‌ترین لحظات و بخش‌های برجسته دولت ترامپ را به صورت ۲۴ ساعته ارائه دهد.</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/SBoxxx/21083" target="_blank">📅 11:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21082">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sp_Em6Iv1JfECJAMUVSuhdgxdJQvKlzz2ugl3du_2La1W7Y73w0csBirII1rNG5ajEZgU3CzMmmXobEOlDm9IrTuAP4-he5LER1D-QJy9fcV-V_uVMl_w8t9Ub5xU5JKijopTwJhqNruvfe4u8gjxaJQPV_E2bOJ5UGrwd5Jx7VrX94fMm6z4JZ8DLeJLuumAv7LnrpSoMu9QWsHkmJ0XLoghYjUYRPSFgdSdznlxHXrMqH_IlNKlSNJbK38kqM0PVz37mEpSGtmW81oNkjYWYbX7O82uBF8Uu1-_traBzo-MnQLgaSbA-CafWDkwU2oBbIeVqmM2wsKgzWpoHQ5BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح میانه ای قرار دارد و با توجه به افت بهای طلا، به احتمال زیاد دوباره حمله به سقف جمعه و حتی فراتر رفتن از آن را خواهیم داشت (یعنی بالای 4400)</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/SBoxxx/21082" target="_blank">📅 10:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21081">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mdNfWVLtVLUpkRoqtVwXHFjiS2A_alHeT1ppO21bnyfp-QZ91xpe2hH2Hccz2K0RhE1fBoxpqN-TMgfKDpXtPGVacA-ouAK8njw0TRmBYJuhwzhORbk03oeNX7mpQyzB-wEw2CaJNyc1vKCZfePEwAHyOp7FnWatfAUG-AqqNa-WUMBf743_z4hlHDN4kfdtuQSR5NnIj0NidhJDwjO8joj2MsaJFzIcEm1DEZe_VeX5hHAebGGLqCX4S4Oir6C4lsQc_axlzlp6rN81C8IWdf1QCl83tyvui-rpN8uf400UXE65os1JhqAuESfDyWNEBOwD19n21OZpt5vt2JIRCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمونه ای از جامعه ای سرشار از زور و ریا!
حجاب اجباری بر سر دختر می کنیم تا در بلوغ و بزرگی محجبه باشد اما همین الان مادرش بدون حجاب است!</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/SBoxxx/21081" target="_blank">📅 09:50 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21080">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">رئیس‌جمهور ترکیه، اردوغان:
ما آماده‌ایم همکاری‌هایی را که با ایالات متحده در حوزه‌هایی از جمله انرژی هسته‌ای و LNG، حمل‌ونقل هوایی مدنی و فناوری‌های پیشرفته برقرار کرده‌ایم، گسترش دهیم.
توسعه بیشتر صنعت دفاعی — که به‌طور سنتی یکی از قوی‌ترین حوزه‌های مشارکت ما بوده است — هم به‌صورت دوجانبه و هم در چارچوب ناتو ضروری است.
ما می‌خواهیم موانعی را که هرگز نباید بین دو متحد وجود داشته باشد، پشت سر بگذاریم و شتاب تازه‌ای ایجاد کنیم.</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SBoxxx/21080" target="_blank">📅 07:51 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21079">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FcvgfXt05GRCsRCZZkJL5aoa42M7QVVT7O3JiFRVMtN4iDYAlzTtKW3NWQkBxYU1vZEZfzBGGGJqkItgjWWtrjQCttsykNwfoMT7GR30lJLFXIlApVpqbihcr2JOebWpAC5Wuy8tme08Yi_WnHZm8Od2Fks6GKRkojGhuWeYTwcF6X9t_R9jlqIaO3rqUE-q5DsLg4LmyztIe5QnwJnhlLi9aMFtg-OlHuNjtlVI62tRnSWylT5Gza04qGljNwWucEULnXovm4s-Mggr1CT2_atzdNr06oOX8vLCOt8MmVOpEGOuQ4IAByAvWuIWKWr50HtFhqG4c5rFF8QTQFCCyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
دلار، نفت و موقعیت های معاملاتی گرید از دید موسسه Danske
موسسه Danske با توجه به رشد اقتصاد آمریکا، سیاست انقباضی فدرال رزرو و اثر شوک نفتی، تداوم قدرت دلار و فشار بر یورو و پوند را پیش‌بینی می‌کند.
در بخش معاملات گرید،
GBP/JPY
به‌عنوان یکی از سناریوهای نزولی مطرح شده و ترکیب تحلیل بنیادی و تکنیکالی، افت قیمت تا محدوده 181 را مورد توجه قرار می‌دهد.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/21079" target="_blank">📅 00:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21078">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">— ضرب الاجل دولت عراق برای خلع سلاح حشدالشعبی</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/21078" target="_blank">📅 00:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21077">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">هند نیز‌ به محاصره هوایی آمریکا علیه ایران پیوست؛ گزارش ها از توقف پرواز ها میان ایران و هند!</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/21077" target="_blank">📅 00:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21076">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">هند نیز‌ به محاصره هوایی آمریکا علیه ایران پیوست؛ گزارش ها از توقف پرواز ها میان ایران و هند!</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/21076" target="_blank">📅 22:07 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21075">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/POUhsy3uJCgJV6hOshH1ojLyTCN5a3tAIKmgZeyrQLtLbV2hXVonE5xyqowI6nqT_3VdymvAxb72Nr0f3RXUpPSxROguxbD8o95rDmPhYJBq3ywM85PeyMi_Du_AyOIxq4poP8UN56Y_GEdb9QvqlEKyGWdA7FSty9lWJHVY65fGndg3rVFiRb1ryu3zvSeWC6vlCGWtqPXRA90MLl14RoZZ5SqcPlrnPu8ep4tDugVSCLYsVFXjV1Z7z5A8IEoOeTgqy8P2qJoA0TAkerS1gcEHWAelXvteUjDg-mzqrxxdxCCGGAl2gQCg1onYfPyZCeGN-2GbII1_q_80jz-0wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام وضعیت !  فکر کنید پزشکیان بتواند آن ماموت ۱۵۰ کیلویی را با دستانش خفه کند!  اینها شده اند نخبگان ما!</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/21075" target="_blank">📅 20:08 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21074">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">رئیس خزانه‌داری ایالات متحده می‌گوید تمام خطوط هوایی ایران در ۲۳ سپتامبر «بسته» خواهند شد</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/21074" target="_blank">📅 19:52 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21073">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZgSgmbJpRFGNNqXj2Qyi7MuYKpDNlcg_FpwhINYdN8BEz00Yh-i84lUbQ8c_HyMbCYGrR-cZRVGGaeP-p1Gq3dcxPXIk_ui_L9RTja4iXhdzBkkIH7EHrikIQac76iqixvMQuwiAAagkuwD8MmBFXBmuBEykkKXht45MooM4DPbzHkGtPOAtdRZsIwosKkKH17SHRyUimpM9kPX_g8W9bwRlmm5ZXIgYFaowkFGzEaXA9jrr8LemHPYQLntSEZG0xdNmBaW_ENb1YCVZ_k7Iri5JhREQZUUAkDG6PnaFd2POodQr2cFa-snyba2bV4ftjDYwjZelaF_dEbTRbSmIHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام وضعیت !
فکر کنید پزشکیان بتواند آن ماموت ۱۵۰ کیلویی را با دستانش خفه کند!
اینها شده اند نخبگان ما!</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/21073" target="_blank">📅 19:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21072">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اظهارات جِی. دی. ونس درباره قیمت بالای بنزین:
به نظر من، همه ما باید این واقعیت را بپذیریم که تا زمانی که ایران در تلاش برای ایجاد وحشت در حمل و نقل بین‌المللی است، ما طبیعتاً تلاش خواهیم کرد تا در برابر این اقدام مقاومت کنیم. اما به همین دلیل است که قیمت بنزین اینقدر بالاست.</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/21072" target="_blank">📅 18:26 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21071">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RG5WZ6NL3idTOViiJEXeUOjW4kIVmHg-pNGH4Qil9Yo4E1NE7Byq5T3PFjwL2ZE2uxdgW_Fhp8PV9oir8vbywpstkyjtxlQ2NDnpjM9lrgsZirLQAS8dVcBCvW5T9UtB9Y-9iELkS9Sw-eo3R5NNUAD23Qh2DePUzP1Wq4et3Ef3Ryvsix1hWrem8QJcfmEOm4BuoayQjZCoYM0t75XfWw4M94NdySdv0s_S2kAgKMjczFBI0_PCrmqN0y7teZA-1VJi581EoKXqLwMOC5VA31s0vOmrjE7HUPdzmfRNNJxUJxUw2Vm6xZwIjIhDewP0eqx0uWjYj3vntbRGuzeBAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/21071" target="_blank">📅 17:51 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21070">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">درگیری های سنگین میان نیروی انتظامی با جیش العدل در سراوان</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/21070" target="_blank">📅 17:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21069">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">رئیس خزانه‌داری ایالات متحده می‌گوید تمام خطوط هوایی ایران در ۲۳ سپتامبر «بسته» خواهند شد</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/21069" target="_blank">📅 17:08 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21068">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">جان کیریاکو، تحلیلگر سابق سیا:
اسرائیل هزاران افغان را در ایران با ۱۰۰ دلار برای جاسوسی به خدمت گرفت.
کار اسراییلی ها اینطوری بود:
«در این گوشه بایستید و هر بار که این ژنرال را در حال رانندگی دیدید، یادداشت کنید و برای ما بفرستید.» بفرمایید صد دلار.
اسرائیل هزاران نفر از این افراد را استخدام کرد.</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SBoxxx/21068" target="_blank">📅 13:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21067">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTjOapLyJBn0GDwjFya-jUbzSQGxQFWvYkhISt4lc9xWnUD4bF4ftM8WuQ0x0TOgG-zQ56-57tvn5H5D0TXVT5q8bmgd5zMao3tHlU08LkWslykOPnXtszipJJ2ErfgS-c_1ebxwxHHDUV7NDU_t39MCrDucNoobahN-7uw2JsVWbwxIK7xyYAyAJlb8GhFe_u0n53xJ3TGfY7LbKc_VGEe-0KtvF8v14CKEE_cuiit13VSXHkl1ox_V-m79v-xofIZd73ke4Z9qhVIpkYC-AycRfm-Jmwy716pRJ_n0sETeZ5Hnmd3rGBXk3m0qUxA2JncYBJJNYAlQ-UUmbYrTJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC در محدوده زیر قیمت منصفانه قرار دارد و لذا فضا برای یک رشد در طلا هموار است.</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/21067" target="_blank">📅 11:52 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21066">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tbg_XK2g4NTmvwJRpR0XOvCuX_all_pdsg2-ht8Ig6fnSYMKEmNyqjtV-PJaPnAzvLpx6rSaRYLHm2vFHGGtfqUre0cX9aGHbtDUvr1wNs5_hoMI9MhjY0l-JRqY9-9QQ0pTEPYiCwRi1otaQU8XPAYwsq47foFqtapf4RpNsanCXSRqcPOfWq0LYi_9CcUQSdrMxZUQmgA_Pl4UU1V_5IgoSb-oOhVzfe5VrMBeLW3v2Znbrq7LgvfH1OiKTXDP-UfmEA4FSyNvhHetVBiu1OEu-e-qDRFYynDDwebZbU_gfT7qCKoOQKN-2pw7a2KLHCaVKRQfGt9y5jxKnuRvXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح میانه ای قرار دارد و با توجه به افت بهای طلا، به احتمال زیاد دوباره حمله به سقف جمعه و حتی فراتر رفتن از آن را خواهیم داشت (یعنی بالای 4400)</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/21066" target="_blank">📅 11:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21065">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">قیمت متوسط گازوییل در آمریکا برای اولین بار از
۶.۵۰ دلار به ازای هر گالن
گذشت. از ژانویه ۲۰۲۶، سطح عمومی قیمت‌ها (موزون با شاخص بهای مصرف‌کننده)
۴.۸ درصد
افزایش یافته، در حالی که قیمت سوخت خودروها
۱۷ درصد
رشد کرده است؛ این امر احساس بحران توان مالی را تقویت می‌کند. دونالد ترامپ، رئیس‌جمهور آمریکا، تمایل خود را برای دیدار با سید پیش‌وا (پزشکیان)، رئیس‌جمهور ایران، اعلام کرد. با این حال، گفتمان طرفین همچنان منفی است. توافق آمریکا با دانمارک درباره گرینلند می‌تواند گامی مثبت باشد (بازبینی یک توافق موجود می‌تواند یک سابقة مفید باشد)، اما عدم اعتماد بین آمریکا و ایران اوضاع را پیچیده‌تر می‌کند.
مِرتس، صدراعظم آلمان، پس از باخت در انتخابات منطقه‌ای هفته گذشته به چپ رادیکال و راست افراطی، سوگند یاد کرد که در سمت خود بماند. به صورت ساده‌انگارانه، نگرانی‌های اقتصادی به نفع چپ رادیکال و نگرانی‌های اجتماعی به نفع راست افراطی است، و روند جهانی به سوی قطب‌بندی سیاسی پیش می‌رود.</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/21065" target="_blank">📅 11:48 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21064">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_uQ07O9d7wIFbMKICTdSx2rEiwgnldyzXD2xNnNCHfmIxlqKT_SeGtspp3Ua2bIlNCQj21q3XJjxaSxVGs3-SsSbuMQjyoPhbXoMZc7TKwVxKVjI3OkEBdj_1LjvfcA82UVkwdVfscTQEUE2Oq6wy1elaPMJt1yeh4jYq-dNDzEMlUnpBZS2UnA3R-LrpdFrcPeeCnZj4fGOlsEXfPUKbzz6FvoqUtRbBKn9WKhcxHxrCPXc-W9JsrkXhIG8ynEs9o77oOBRScRUOvKF42qsXZ8IVn935nMRBNk7wcDYcdJRkHq2wnk5zW6RVQh3qt9Xj_XnEnf1y9QHZa5sKTwqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چین میزان اوراق خزانه‌داری آمریکا را به پایین‌ترین سطح در 18 سال اخیر کاهش داد.
چین بیش از یک دهه است که میزان دارایی‌های خود را کاهش می‌دهد. این میزان از حدود 1.3 تریلیون دلار در اوایل دهه 2010 به 618 میلیارد دلار در حال حاضر کاهش یافته است.
این کاهش پس از سال 2022 تسریع شد، زیرا چین نگران وابستگی بیش از حد به دارایی‌های آمریکایی شد.
دولت‌های خارجی، خرید اوراق خزانه‌داری آمریکا را کاهش داده‌اند، در حالی که صندوق‌های تامینی و سایر سرمایه‌گذاران، خرید این اوراق را افزایش داده‌اند.
کاهش تقاضای خارجی، به افزایش نرخ بهره اوراق خزانه‌داری کمک می‌کند. نرخ بهره اوراق 30 ساله اخیراً به بالاترین سطح در حدود 20 سال گذشته رسیده است. افزایش نرخ بهره به این معناست که دولت ایالات متحده برای استقراض پول، باید مبلغ بیشتری پرداخت کند.</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/21064" target="_blank">📅 10:37 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21063">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ملونی ممنوعیت پوشیدن بورقا و نقاب را در مدارس ایتالیا اعلام کرد
«هیچ‌کس در ایتالیا نمی‌تواند تصمیم بگیرد که یک زن جوان باید خود را پنهان کند. برابری بین مردان و زنان نه در خیابان‌های ما و نه در مدارس ما قابل مذاکره نیست»</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/21063" target="_blank">📅 10:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21062">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">اقدام بی‌سابقه دولت الزیدی:
یک “عراقیِ ارمنی‌تبار” سفیر عراق در آمریکا شد.</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/21062" target="_blank">📅 10:01 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21061">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mp_LAEGePwawdTnNJ-3I--dBjycNdAkWnbcE3_Q1kFw6A1-mY1mT5njqcMN13dIswZseZdg3Tbj0J2YVbX1JnMRibfPUiZpk1Dgo_VPntMVMQhAfLVO6xv5M65-scmLoURwkBJIFKpJUvE3h2vyHbr_1SbsOY2vn_Wb9zeI-NSO0PxZU34XUDii1rXY8tZ06x51nBcCYSUfnp8swS0JMtmWbr1HxbAIS67untfFH6vYokSwYBY7LnuFhBi5_sTpsZXJFTyRla6r3TwhbPp6_8bJXkPm_uypvplhTlsWu6JbFCQzFYpTB6-aO2lG62IHf0uxUNBjUoyTONVyYlU1Jmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیده شدن یک هواگرد ناشناش در آسمان تهران امشب</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SBoxxx/21061" target="_blank">📅 01:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21060">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">یعنی همه چیز دیدیم جز قهرمانی....
هعیییی</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/21060" target="_blank">📅 01:35 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21059">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">دیده شدن یک هواگرد ناشناش در آسمان تهران امشب</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/21059" target="_blank">📅 01:34 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21058">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9e029fb89.mp4?token=PB4EDuaJmowBFj1sk0rb6UzGqbvxf6Yvdz_99I-UtxXrioS_xEGwBq6kS2OcF7h1U_CbjIbEO18sulPlRe9rpgPTv_XGDqawV1Bwy9zd40etIk0DIrArre54jmBxhjlKPglr7fqCLjcpsB72q6JDkXvNI-WqW0C3YAgNl49c0wXJsSZOY5GU6tXCTZWmrHeSf4w7_u1Cc0-cli8fwbi2UF9CBRfj_4jdlWLJoDFvKG7JYWWtHkkvVyw5EQoq7eztR4NrlMUUGdZw0WBZEzEAhALSTNSCuMYhxG2tlbI98iAdoOIluNB5Fso85QhR0IIPPI_K4S9VDfRtyfvcLDLHpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9e029fb89.mp4?token=PB4EDuaJmowBFj1sk0rb6UzGqbvxf6Yvdz_99I-UtxXrioS_xEGwBq6kS2OcF7h1U_CbjIbEO18sulPlRe9rpgPTv_XGDqawV1Bwy9zd40etIk0DIrArre54jmBxhjlKPglr7fqCLjcpsB72q6JDkXvNI-WqW0C3YAgNl49c0wXJsSZOY5GU6tXCTZWmrHeSf4w7_u1Cc0-cli8fwbi2UF9CBRfj_4jdlWLJoDFvKG7JYWWtHkkvVyw5EQoq7eztR4NrlMUUGdZw0WBZEzEAhALSTNSCuMYhxG2tlbI98iAdoOIluNB5Fso85QhR0IIPPI_K4S9VDfRtyfvcLDLHpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیده شدن یک هواگرد ناشناش در آسمان تهران امشب</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SBoxxx/21058" target="_blank">📅 01:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21057">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/304c99ed1e.mp4?token=fkL5L6qmavPE-ecckWCyaeWpMvOdcOy4bmIo5iP2muEvlPidC66t8ZLa5RqwHIl_wggUlDOVyTWa-W7vuriyNC1dYBh0yD-yurUmQLVwKu8BGJxXLQ3XlEvIxQ-dPovksEixM3G_GEWD5ho_nXITi72lEW3X7L9jOdFEtgagEhjCCZFf9uEf8-n4UPOCQHr6NSV4s4pOVx9fH1N6XKzy2Hoy6xiY2LhOFRbL2iAq2HDChrl-Jcn7sc-dkHrOHJtVXp2nqyAmrZgASR3wzmqnLo1-G25EsQVst_1rKjGkxSAZ0_Obas_1C3Nvk3fTacLD1wUlknhARAifkS29XcAwxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/304c99ed1e.mp4?token=fkL5L6qmavPE-ecckWCyaeWpMvOdcOy4bmIo5iP2muEvlPidC66t8ZLa5RqwHIl_wggUlDOVyTWa-W7vuriyNC1dYBh0yD-yurUmQLVwKu8BGJxXLQ3XlEvIxQ-dPovksEixM3G_GEWD5ho_nXITi72lEW3X7L9jOdFEtgagEhjCCZFf9uEf8-n4UPOCQHr6NSV4s4pOVx9fH1N6XKzy2Hoy6xiY2LhOFRbL2iAq2HDChrl-Jcn7sc-dkHrOHJtVXp2nqyAmrZgASR3wzmqnLo1-G25EsQVst_1rKjGkxSAZ0_Obas_1C3Nvk3fTacLD1wUlknhARAifkS29XcAwxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مستندی جالب از روند ساخت و امکانات شهر موشکی یزد!
بخش عمده اش به نظرم با واقعیت همخوانی دارد اما در بخش هایی از تخیل استفاده شده مثلاً بخش مربوط به نمایش طبعیت و روز و شب برای کارکنانی که 500 متر زیر زمین حضور دارند.</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/21057" target="_blank">📅 01:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21056">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K9JBCPCdKk3RC41NdkWpgDyiPcum1libS-ncWdI7jUgVxZbHtj-3iQVbc7iLDCxRR0pilUHxrC0zqiv2q1ZaEsVnlU78rRAgWihigNOFliQZS3b-6fGlteyxkNXnLXYXiBvVH0YEuS4u0uMXZ7Dqq92XtEc__5Pv86dYaTYYxL3ICDuxf-VWbd4pBCVdTPwao4byvoVzvFakwwDI6tfPYg4tZ9foPQ3JM4x6-747qiFfcDFHqeaMyz8TTNe_3Ejfo8Pa8pyqnZWRFaiXZzSOsRC6KH1_UFB9Ly05NWvYHRSUraPiXtnJ18esQHO9LUqQbGFqN2AmCNVxft9RQCRZIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ می‌گوید توافق با دانمارک، «کنترل دائمی» ایالات متحده را بر امنیت گرینلند تضمین می‌کند  ترامپ می‌گوید توافق گرینلند، رقیبان ایالات متحده را از ایجاد پایگاه‌های نظامی در آنجا منع می‌کند</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/21056" target="_blank">📅 01:16 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21055">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">واقعا تا حالا کسی رو ندیدم  که با این جدیت کصشر بگه
😂
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/21055" target="_blank">📅 00:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21054">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7235f04196.mp4?token=fBTwNXcCjHwttN4BkCxfuJuyakLlYqrlpZ240Dy9n8cNarImxjyvxhGgq5z-kPWhhKy9gvLuYz-Kk1dNr72UD0Dy8J-AsCfpmnRpIkHAExcML_FHVIYT4xyQzWOCfCOEgddUSMCRixP3gVyjQAraflulzwUR19EClk07nSbQksfAFjsZOCdjajExA2ytkFXtYTQ_V-UQf85a0oNfitJXAELGUKSgVwQ74p17DaIWQjewgI6cG1RfZyplJD5hGlaMaci25Mo5xGdqXQyoddTM0sgrort5h5KzCS_AXn8s0D7BcmTK9zmcmkRZVr9f76eAgcS0Mp1CVDnYjYiVEt1Cbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7235f04196.mp4?token=fBTwNXcCjHwttN4BkCxfuJuyakLlYqrlpZ240Dy9n8cNarImxjyvxhGgq5z-kPWhhKy9gvLuYz-Kk1dNr72UD0Dy8J-AsCfpmnRpIkHAExcML_FHVIYT4xyQzWOCfCOEgddUSMCRixP3gVyjQAraflulzwUR19EClk07nSbQksfAFjsZOCdjajExA2ytkFXtYTQ_V-UQf85a0oNfitJXAELGUKSgVwQ74p17DaIWQjewgI6cG1RfZyplJD5hGlaMaci25Mo5xGdqXQyoddTM0sgrort5h5KzCS_AXn8s0D7BcmTK9zmcmkRZVr9f76eAgcS0Mp1CVDnYjYiVEt1Cbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واقعا تا حالا کسی رو ندیدم
که با این جدیت کصشر بگه
😂
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/21054" target="_blank">📅 00:14 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21053">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XEjlHCwnvG2N8GdP_bpbrP02l6ohFYdoJwBCy7ynWe8VjYKu5H-udpQQGwdG_MpCW1lbyWnlQ5gq4_J1zTqMERwQ6LDkp3bn71gWFbe1gDf3pNA0GW3TM4ZwJwe4nHWY1lRIpwpa7MmsMqZR-P8lzXbMazjEFaSJzksP-F_sKHPJpWYAA4_j1PhnckEPbDpJ0hS8ceptxvIcjEdPyRGghbRFa8-Y7TGRpXNYiJW2J_-aqqeWN-sRP-s56uy0B1j8RgeGzTyy42CvO1cn7b3vPJZ4FvJ6mtm4hYVSyVDdtYt6M9clqKBUeFBRYyZKlDO23V8raGRFQA8vmFB2cZWwaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SBoxxx/21053" target="_blank">📅 23:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21052">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">چارت نفت جوری است که به نظر یک کاهش تنش داشته باشیم و دیدار شی-ترامپ مثبت باشد.</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SBoxxx/21052" target="_blank">📅 23:34 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21051">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ApOA43L2K_25rTOmKH_u3I6c7OS8XE2g0eSRkr-KsTrKQojWnaOpx4cDr0nwgwVA8lzf8X1AiEY5bS4c07XQCNSlm6jiiyt8MxRsUrddwzEcEiXjU0ohYpn6uyVrMCHL6VOlEHKgAJ6uBtIjnMORFUs1AabMhEnMvcsIuvyl8zsu2IS7FD5sh-rBMcBf62AhdfgY4SpppH1ITwPZQruYv0NvAKLOxHedYSj_SfLwh4Loz2QHJ_YGaqFcmu51p-tO3qH7VPKdMtU4LhOT1BLmy8nngnockmTxGFx2v9BJrMhMRYWs4rL2Dr2DnMqvv8zKxSfS0F9eKlNH6CYPXwdvTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چارت نفت جوری است که به نظر یک کاهش تنش داشته باشیم و دیدار شی-ترامپ مثبت باشد.</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SBoxxx/21051" target="_blank">📅 23:33 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21050">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">حریم هوایی اسراییل هم بسته شد.</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SBoxxx/21050" target="_blank">📅 21:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21049">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_Zq9aeRhxoQzfnOvcSMpdBRsSqCyajD5zfodqFtKJItv8fgIhk037xgDI32H40nT7mpP2nsYHI0WkgHLSLwNNsjO_ZUgHPnn2siikek2OWp1jjyUJ54ZZYBJ1cyrama3YlGXEGUB1uz13ByZF1NBGhNQEMpuKZDG3MTemr_X83X-5Vc3hkqwXrWO5OFqmVmieBz-ZYMLlO8RiratzV3jMnN08uAmZAjgY2ll1ozSjmJRGJy5p7V4ROm6ps7ltywnwHY9TBLZTwyrAGPuJB2lMhYYiSd5whpM3tvAXomqF0wyIsAoZP4kPt_GPJrm4p_phEs6brEbAfX1odfl3Thbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان:   صلحی که دشمن تو را به آن دعوت می‌کند، نباید دفع کرد</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SBoxxx/21049" target="_blank">📅 19:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21048">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">قالیباف:   هم میجنگیم هم مذاکره میکنیم</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SBoxxx/21048" target="_blank">📅 19:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21047">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">📌
تخریب تقاضا در بازار نفت و انرژی های جایگزین  شوک عرضه نفت در کوتاه‌مدت قیمت‌ها را بالا می‌برد، اما تداوم قیمت‌های بالا با کاهش مصرف، افت فعالیت اقتصادی و تغییر رفتار مصرف‌کنندگان باعث «تخریب تقاضا» و کاهش فشار بر بازار می‌شود.  در بلندمدت، اختلال پایدار…</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SBoxxx/21047" target="_blank">📅 18:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21046">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-zJHMbyO8DblvPAuIGIDQHvp4kub6KtYIbP859TOSUoBCEqe_QAuKsfYCfDW0QE7IEYBZUzrvL5_VjbJ5c0e1vDpOUtyvlcQ6voFn4DmleXq91pHR5jY2a6ZCpel8XbkHVj_hOLR3BNIGYrsJfEVRGYTdiFcpAIgGLWugh2m7ZS_vYJB9iqtPK9iFLGrUzbpTAyFIxAIahb7o9niifha5HgjptL0tYDHdSQcBW96H5T0uQbSH3H2njb4iATn56YhJaF_2VVqTX3Y2dZQQ8mYaUwyvSvnvJm6RVrkdsfcBxIffio5NdFJ8nNR9tYG_zx7zLBnWbWC7IaimF2aKmclA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
تخریب تقاضا در بازار نفت و انرژی های جایگزین
شوک عرضه نفت در کوتاه‌مدت قیمت‌ها را بالا می‌برد، اما تداوم قیمت‌های بالا با کاهش مصرف، افت فعالیت اقتصادی و تغییر رفتار مصرف‌کنندگان باعث «تخریب تقاضا» و کاهش فشار بر بازار می‌شود.
در بلندمدت، اختلال پایدار در عرضه می‌تواند سرمایه‌گذاری در خودروهای برقی و انرژی‌های جایگزین را سرعت دهد و وابستگی به نفت و اهمیت استراتژیک آن را کاهش دهد.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/21046" target="_blank">📅 18:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21045">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ترامپ به فاکس نیوز:  برخی از مقامات ایرانی مانند موش‌ پنهان شده‌اند.</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/21045" target="_blank">📅 17:38 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21044">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ترامپ به فاکس نیوز:
برخی از مقامات ایرانی مانند موش‌ پنهان شده‌اند.</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SBoxxx/21044" target="_blank">📅 17:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21043">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">این هم پاسخ ترامپ به چموشی سعودی های مفلوک در نپیوستن به پیمان ابراهیم و در عوض دست نیاز پیش فاکستان ورشکسته و عثمانی مقروض دراز کردن!</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/21043" target="_blank">📅 17:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21042">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ترامپ به فاکس نیوز گفت:   گزینه‌های فعلی که در حال بررسی هستند، عبارتند از: نابودی #إيران، یا اجازه دادن به فروپاشی اقتصادی آن، یا رسیدن به یک توافق.</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/21042" target="_blank">📅 17:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21041">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ترامپ به فاکس نیوز گفت:   گزینه‌های فعلی که در حال بررسی هستند، عبارتند از: نابودی #إيران، یا اجازه دادن به فروپاشی اقتصادی آن، یا رسیدن به یک توافق.</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/21041" target="_blank">📅 17:12 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21040">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ترامپ به فاکس نیوز گفت:
گزینه‌های فعلی که در حال بررسی هستند، عبارتند از: نابودی
#إيران
، یا اجازه دادن به فروپاشی اقتصادی آن، یا رسیدن به یک توافق.</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/21040" target="_blank">📅 17:12 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21039">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">رویترز:  در این ماه، ایران فرماندهان سپاه پاسداران انقلاب اسلامی، مشاوران نظامی و تجهیزات مربوط به موشک‌ها و پهپادها را به یمن تحت کنترل حوثی‌ها منتقل کرد.  یک پرواز شرکت ماهان ایر در تاریخ ۱۳ جولای از تهران به سمت یمن پرواز کرد و بین ۱۰ تا ۲۱ نفر از پرسنل…</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/21039" target="_blank">📅 17:05 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21038">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">پوتین:   رهبران اروپایی در روز های گذشته به صورت آشکار اعلام کردند در حال آماده‌سازی برای جنگ قریب‌الوقوع با روسیه هستند.</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/21038" target="_blank">📅 17:00 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21037">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">قرارگاه مرکزی حضرت خاتم‌الانبیا:
براساس اطلاعات دریافتی، آمریکای جنایتکار .... بار دیگر تصمیم گرفته است با چراغ سبز برخی کشورهای منطقه، در نشست مشترکی در یکی از کشورهای اروپایی، اقداماتی علیه ایران اسلامی را از سر بگیرد.
هشدار می‌دهیم چنانچه آمریکا علیه ایران اسلامی خطایی مرتکب شود، تمامی مراکز استقراری و منافع آن کشور در منطقه، بدون هیچ‌گونه محدودیت و ملاحظه‌ای، هدف حملات مستمر، موثر و دردناک قرار خواهد گرفت.
اخطار می‌دهیم چنانچه کشورهای منطقه با تداوم سیاست دوگانه در قبال جمهوری اسلامی ایران، با تجاوز شیطان بزرگ به ایرانِ اسلامی و مقتدر همسو شوند، همگی در این شرارت شریک تلقی شده و دیگر نمی‌توانند از نیروهای مسلح قدرتمند ایران انتظار خویشتنداری یا نجابت را داشته باشند.</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/21037" target="_blank">📅 14:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21036">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">فایننشال تایمز:   عربستان از برنامه تحت رهبری چین که بخشی از تلاش‌های پکن برای ایجاد یک نظام پرداخت فرامرزی جایگزین دلار است، خارج شد</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/21036" target="_blank">📅 14:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21035">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">این هم پاسخ ترامپ به چموشی سعودی های مفلوک در نپیوستن به پیمان ابراهیم و در عوض دست نیاز پیش فاکستان ورشکسته و عثمانی مقروض دراز کردن!</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/21035" target="_blank">📅 14:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21034">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">قالیباف:  جنگ بعدی ناوهای آمریکایی را در هر نقطه اقیانوس هند باشند هدف قرار می‌دهیم!</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/21034" target="_blank">📅 13:07 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21033">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">این تناقض را نمی‌فهمم:   از یک‌سو ناامنی در کشور تا حدی است که رهبر حتی نمی‌تواند یک پیام ویدیویی منتشر کند،   و از سوی دیگر امنیت در نیویورک آنقدر تأمین است که رئیس‌جمهور و مقامات وزارت امور خارجه بی‌دغدغه در خیابان‌های منهتن قدم بزنند.   آمریکا دشمن خونی…</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/21033" target="_blank">📅 12:56 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21032">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRaefipourFans</strong></div>
<div class="tg-text">این تناقض را نمی‌فهمم:
از یک‌سو ناامنی در کشور تا حدی است که رهبر حتی نمی‌تواند یک پیام ویدیویی منتشر کند،
و از سوی دیگر امنیت در نیویورک آنقدر تأمین است که رئیس‌جمهور و مقامات وزارت امور خارجه بی‌دغدغه در خیابان‌های منهتن قدم بزنند.
آمریکا دشمن خونی است، اما با بعضی‌ها‌ کم‌تر؟
✍️
پسر سوم‌ خانواده تیبو
@raefipourfans</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/21032" target="_blank">📅 12:56 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21031">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">قالیباف
:
جنگ بعدی ناوهای آمریکایی را در هر نقطه اقیانوس هند باشند هدف قرار می‌دهیم!</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/21031" target="_blank">📅 12:47 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21030">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikNMBtW4dMnqIWFyXRPwuMlLXoPYbsvpAwiLlsNFJBIIiNJdiYwUXfrBlKGZoCgEyg6z9I4bRa0uR5HF5v_1aLkykmmePVIMhetan6H_aL-AU0i6ay2ysNfq4aGwhfGILT-wj8W1zYPA5xh-6m89SszPYRuuwg3IcIXqWw3oxBGmfkq7D9WIdzfMx_FPlPcu7cQ3AKYpPEYtS6dDJLvh7gAa1Eh6280NKp0qENkeElkhRMStFeETnBJkDJu1KsV_Za5aEd24uhCnLFBDVsnzPYj3i5UUHjcCE5dN2L637eqoP2MYS-UmOgygQxgTVrfhBkacapRn_jxukq8nZV955w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve  نمایه FVC نشانگر نزدیک شدن طلا به محدوده قیمت منصفانه است و لذا از حالت حباب منفی ارزشگذاری فاصله گرفته است (به دلیل رشد سنگین از پریشب) هر چند هنوز تا تشکیل حباب مثبت و بیش خرید بودن فاصله زیادی دارد.  پس بهترین استراتژی برای امروز:  خرید…</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/21030" target="_blank">📅 11:07 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21029">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">کانال 14 اسرائیل:
آمریکا گزینه‌های حمله احتمالی به یمن را بررسی می‌کند</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/21029" target="_blank">📅 11:03 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21028">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mEPqvVWSftf9XAwHmM0tvuWKy89SmOBkw7llrwNUAaQQiVvLiKj-6TciNIYEx3Hq50JlbnrMSohYJssbtX3hVqDzz_eV3bSVHByZisYT-fZSVo9Mulx5h07M_k_ZtxcA54n5LwW8GJAnAjCReyCzApsSBOAguYEhZZsH6vuCXRNrW_yn5Mz2cISJGxl9NLeDjJ-O2IfdLqo-G5cTyBu8QwgdXlhdAzELDQDDKiCLhOPI8jJD9gpU11AWF5puCocERCa4F5h4wJSgrbk-QUdfNsRd9nQ8h3ZXm9jCe6jNL2ttZJSvLYfkJWa-ynKfJsBqHbwxHvFjFPktNQoV92zg0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک حمله پهپادی گسترده در طول شب به مسکو و منطقه مسکو، در روز پایانی انتخابات پارلمانی روسیه، انجام شد.  یکی از برجسته‌ترین اهداف، پالایشگاه نفت مسکو در کاپوتنیا بود که صبح امروز آتش سوزی بزرگی در آن مشاهده می‌شود.  ظرفیت پردازش این پالایشگاه حدود ۱۲ میلیون…</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/21028" target="_blank">📅 10:26 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21027">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">یک حمله پهپادی گسترده در طول شب به مسکو و منطقه مسکو، در روز پایانی انتخابات پارلمانی روسیه، انجام شد.
یکی از برجسته‌ترین اهداف، پالایشگاه نفت مسکو در کاپوتنیا بود که صبح امروز آتش سوزی بزرگی در آن مشاهده می‌شود.
ظرفیت پردازش این پالایشگاه حدود ۱۲ میلیون تن نفت در سال است.
آخرین بار در ۱۶ و ۱۸ ژوئن به شدت مورد حمله قرار گرفت، زمانی که هر دو واحد اصلی پردازش نفت خام آن آسیب دیدند و پالایشگاه مجبور به تعطیلی شد.
تا ماه اوت، گزارش شده بود که توانسته بود تنها با حدود یک‌سوم ظرفیت خود مجدداً راه‌اندازی شود.
اکنون دوباره مورد حمله قرار گرفته است.</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/21027" target="_blank">📅 09:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21026">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4607a666c6.mp4?token=nJO2_q2Ua2gwCdrsC3-AnrwXlG5OBCYDOx5FsYAcKlm5NsAUCNE-3zVvin8qRdrw7oAL7lMQ1R2-EWcWSw4UkAs9PNw64_Jv5pEcDWghXxKyGH2KmnP2Z27vap7g_btk4JXmoL07A-0g-xYdJPFekyJs3NVBUfJL5kfTUFMZvV-G1sViGMS6830Z-9kINeQsqm8kPG3C0PBI-ADwQ2XNjUXKF1r1tVnE8W6azQHWmUSDBbpgA-lPfUeK2yZH-YEZLSJ5zexYRvMCu0OMWZDrrk_Ig5UHUNgkLqmyR6Y2XP6wd3FeZVRB-yEi5uDUpMEl6Hhw6jPJHVZk9PB3_kXM6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4607a666c6.mp4?token=nJO2_q2Ua2gwCdrsC3-AnrwXlG5OBCYDOx5FsYAcKlm5NsAUCNE-3zVvin8qRdrw7oAL7lMQ1R2-EWcWSw4UkAs9PNw64_Jv5pEcDWghXxKyGH2KmnP2Z27vap7g_btk4JXmoL07A-0g-xYdJPFekyJs3NVBUfJL5kfTUFMZvV-G1sViGMS6830Z-9kINeQsqm8kPG3C0PBI-ADwQ2XNjUXKF1r1tVnE8W6azQHWmUSDBbpgA-lPfUeK2yZH-YEZLSJ5zexYRvMCu0OMWZDrrk_Ig5UHUNgkLqmyR6Y2XP6wd3FeZVRB-yEi5uDUpMEl6Hhw6jPJHVZk9PB3_kXM6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت امروز من در بازارهای مالی
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/21026" target="_blank">📅 09:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21025">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d8265c9ad.mp4?token=fQI4nWDg_XfrpUJqBkoZ6DU-t1_l-D38i5rshFS-Ib6g7uzaQXy6zK2rOdxTIj7hIkJLkM6evXAu4YAsEHhldE8d5sIBVZIT0wJjingQrPYyMMkkcsB1XDNxxNFjyEv1OWrwisrcnXWOm-a-6Ig5SUXF2VQhiA9deOtvoDMriNsgdsnx8cBENpED09JKHVM3KM2FeIKnZItQjG2ACpY6Nvl_w9hFIHTLzvDGVzZny0PhQ7iTsnhOEJktzpas-0p5blVGqb6xKFtDivIe8Zzzd85FonrJOzK-SAfIDx1Wuz9EbQBhMVwc4e_646ySG4dAL1Z8EX6EHdAJwQNRTivgyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d8265c9ad.mp4?token=fQI4nWDg_XfrpUJqBkoZ6DU-t1_l-D38i5rshFS-Ib6g7uzaQXy6zK2rOdxTIj7hIkJLkM6evXAu4YAsEHhldE8d5sIBVZIT0wJjingQrPYyMMkkcsB1XDNxxNFjyEv1OWrwisrcnXWOm-a-6Ig5SUXF2VQhiA9deOtvoDMriNsgdsnx8cBENpED09JKHVM3KM2FeIKnZItQjG2ACpY6Nvl_w9hFIHTLzvDGVzZny0PhQ7iTsnhOEJktzpas-0p5blVGqb6xKFtDivIe8Zzzd85FonrJOzK-SAfIDx1Wuz9EbQBhMVwc4e_646ySG4dAL1Z8EX6EHdAJwQNRTivgyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از حمله موشکی دیروز حوثی ها به فرودگاه ریاض</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/21025" target="_blank">📅 09:05 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21024">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ecd762d60c.mp4?token=bYLVC-gLoljUIdKUg0OQCA7UfbYydKT2lb8qw2MlcrjA8xJZRuGA7JE8qikpFwq7wjmx9j5R7mu7Tcd3YclYsBCuQlwy8VjoDTidjDsCEA8Ujg15DvriL-8qnuIOCVsEaGuEQXIwzbHOdMXmpd46NvSK4B2iANsehA35iAnLFB-PAcn5Gjul3Nql5epZaFtFI8WTRmxofdsPOUX5HVLJ5OK7iUreJ7pSaie5nQSHv4Lg8YhXHYxpjMEqToB9oAkFeczzE-kUPNv4k3gPXrdSr_sL-N4YvS_1Btv3YhYc4tWW6uiye4nDxDdPaZH5YrNrUOTjljVfQNCYH80h7gSsrw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ecd762d60c.mp4?token=bYLVC-gLoljUIdKUg0OQCA7UfbYydKT2lb8qw2MlcrjA8xJZRuGA7JE8qikpFwq7wjmx9j5R7mu7Tcd3YclYsBCuQlwy8VjoDTidjDsCEA8Ujg15DvriL-8qnuIOCVsEaGuEQXIwzbHOdMXmpd46NvSK4B2iANsehA35iAnLFB-PAcn5Gjul3Nql5epZaFtFI8WTRmxofdsPOUX5HVLJ5OK7iUreJ7pSaie5nQSHv4Lg8YhXHYxpjMEqToB9oAkFeczzE-kUPNv4k3gPXrdSr_sL-N4YvS_1Btv3YhYc4tWW6uiye4nDxDdPaZH5YrNrUOTjljVfQNCYH80h7gSsrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/21024" target="_blank">📅 08:33 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21022">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ترامپ می‌گوید باسن ملانیا باعث «نجات» هر دوی آن‌ها در پله‌برقی مقر سازمان ملل شد.</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/21022" target="_blank">📅 08:32 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21020">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">وزارت خارجه آمریکا به تمام شهروندان آمریکایی اعلام کرد که سفر هایشان به خاورمیانه را فوراً لغو کنند.</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SBoxxx/21020" target="_blank">📅 02:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21019">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">محسن رضایی:   محل تپه علی طاهر پیش از حمله تخلیه شده بود و عملیات دشمن شکست خورد</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/21019" target="_blank">📅 00:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21018">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">محسن رضایی، دبیر شورای عالی امنیت ملی ایران، از آزمایش یک موشک ضدکشتی که به 80 گلوله تقسیم می‌شود، خبر داد.   به گفته ایشان، این آزمایش بر روی یک ناو هواپیمابر آمریکایی انجام شد و با توفیق الهی به نتیجه رسید.</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/21018" target="_blank">📅 00:57 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21017">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">محسن رضایی، دبیر شورای عالی امنیت ملی ایران، از آزمایش یک موشک ضدکشتی که به 80 گلوله تقسیم می‌شود، خبر داد.
به گفته ایشان، این آزمایش بر روی یک ناو هواپیمابر آمریکایی انجام شد و با توفیق الهی به نتیجه رسید.</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/21017" target="_blank">📅 00:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21016">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">موسسه مطالعات جنگ:
طبق اظهارات مقام‌های آمریکایی به Axios در ۱۵ سپتامبر، تعداد عبور روزانه کشتی‌ها از مسیر جنوبی، با انجام موفقیت‌آمیز عملیات نظارت و مین‌روبی آمریکا، به حدود
۴۰ درصد سطح پیش از جنگ
بازگشته است و عبور کشتی‌ها هم در طول روز و هم شب انجام می‌شود.
عربستان سعودی نیز بنا بر گزارش‌ها صادرات نفت خود را بار دیگر از مسیر تنگه هرمز منتقل کرده است. بر اساس اطلاعات منابع تجاری که رویترز در ۱۸ سپتامبر به آنها استناد کرده، عربستان برای بارگیری‌های ماه‌های سپتامبر و اکتبر حدود
۶۰ میلیون بشکه نفت
را در بندر رأس تنوره در شرق عربستان بارگیری کرده که انتقال کشتی به کشتی آن از طریق تنگه هرمز انجام شده است.</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/21016" target="_blank">📅 00:43 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21015">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c95cb0fd.mp4?token=KICShnZceXg6a_UKTtyPO6SDd5Kp6lY6yo3_7Xv0nvyvNw4pLX_EpGw8DL6TYIE6bcd86vQ8YnKCN0j72rpa3wBL1qw-dm2QnjGZfwiLvm259Vbqo-peEsD46WCoXXT0Y-xhrcXdmfDQgOCNANqiIESGrel5bNcmG3CCXgCzShJw5QoEL2KbQqNRnwKVjkaue7Gr3-XIAJXb8EQgbl7u3IkLwvb4H5W5QZ78REry2E_AZHh5i1HZRRX21xrDa611jOWhbFuqC7U8d-SZ3llDgIcQ_byx5nKiDNFcZq4vmre4Es0v4XWimtjgFk_wXDyCZV1UBq0XoUmCF54Dc_skFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c95cb0fd.mp4?token=KICShnZceXg6a_UKTtyPO6SDd5Kp6lY6yo3_7Xv0nvyvNw4pLX_EpGw8DL6TYIE6bcd86vQ8YnKCN0j72rpa3wBL1qw-dm2QnjGZfwiLvm259Vbqo-peEsD46WCoXXT0Y-xhrcXdmfDQgOCNANqiIESGrel5bNcmG3CCXgCzShJw5QoEL2KbQqNRnwKVjkaue7Gr3-XIAJXb8EQgbl7u3IkLwvb4H5W5QZ78REry2E_AZHh5i1HZRRX21xrDa611jOWhbFuqC7U8d-SZ3llDgIcQ_byx5nKiDNFcZq4vmre4Es0v4XWimtjgFk_wXDyCZV1UBq0XoUmCF54Dc_skFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر خارجه ترکیه گفته که ترکیه می تواند نیازهای نظامی سعودی را برطرف کند!  یعنی در این شرایط که عربستان بشدت به نیروی نظامی نیاز دارد هم ترکیه دست از بازاریابی برای سلاح های ساخت خودش دست برنمیدارد!</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/21015" target="_blank">📅 00:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21014">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oHj27jGkAREk7E5KtaV7psZ0iMW3n1mEPHLrUYjaeoh4LS6iEEABgOeIz1mE3y9_DBRQjaFtp8xRXvfOTg_H4kF0HN9f9oWVpNPiIA0nUm4wvdckZ2pCftANg37cvbkExRNISfPC20YyQa-w5pT3NyOjtd1ymox3nP6AQPGnAu0Byhlmm1R3LDIXT5bY8nLpMx6HPqqBu5r5igvQ-4GNArC0vDlY-N_xV_Uo3im9ZyHXXYZo6d7-L5WTnIRdYgF2Fd2Ls2V9NyU7UwftXAQDAwwV_I8tyx03p8H9tN3MHcO1V1mqX1JeM5fPvSqbccM5JcoJ6JikFu9EXty5hty8FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضو دفتر سیاسی انصارالله:   این پیام به ترکیه و پاکستان ارسال شد که به خودتان احترام بگذارید؛ اگر از عربستان سعودی حمایت کنید، ما به شما حمله خواهیم کرد و شما را تنبیه خواهیم کرد، و دست‌های ما از فولاد خواهد بود</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/21014" target="_blank">📅 00:23 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21013">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NeIOyjKIbes7U0M9bLHjufaZLHwNS6JTF9UtSL3RK3wWj9kINJiZ-wTpNNS1fhWOtf0BjiqbugSMhov0somUNgMSDd_ommbh8bBpEh2VM0iiBHWXk1sBWOA0eyJPi37I-NlwdjPVqr3DSB4tkKAuoVPiP70YpJTyeF8yW7uhCZWRW685PLkmOWEorJlKzjNGmxOYz2Ij2TuNacIffae0H_yenTFarko-9amIoqH9gfjTsGJwbHUq1ast5cRzlaPBv4DlHnaIR0MHY9QohQAFIlnnvTv_FbXpsF9YLxNCzWbbV-7jSpKy79JeXEkxuw1ssi7Tc2uA6Z9JFQWcMlsnFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی:   خواهان پایان جنگ میان عربستان سعودی و یمن هستیم و معتقدم یمنی‌ها نیز خواهان دستیابی به توافقی با عربستان هستند</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/21013" target="_blank">📅 00:17 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21012">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">عضو دفتر سیاسی انصارالله:
این پیام به ترکیه و پاکستان ارسال شد که به خودتان احترام بگذارید؛ اگر از عربستان سعودی حمایت کنید، ما به شما حمله خواهیم کرد و شما را تنبیه خواهیم کرد، و دست‌های ما از فولاد خواهد بود</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/21012" target="_blank">📅 00:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21011">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">صداى انفجار در تنگه هرمز شنيده شد
گزارش‌ها حاکی از شلیک موشک‌های کروز ضد کشتی به سمت شناورهای متخلف در تنگه هرمز هستند.</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/21011" target="_blank">📅 22:08 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21010">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">درباره دیدار مهم رهبران چین و آمریکا
دیدار دونالد ترامپ و شی جین‌پینگ در ۲۴ سپتامبر در واشنگتن، در ظاهر یک نشست دوجانبه میان دو اقتصاد بزرگ جهان است، اما دامنه پیامدهای آن بسیار فراتر از روابط تجاری آمریکا و چین خواهد بود. در شرایطی که جنگ ایران، بازار انرژی و رقابت فناوری بر اقتصاد جهانی سایه انداخته، این دیدار می‌تواند یکی از مهم‌ترین رویدادهای ژئوپلیتیکی پاییز باشد.
مهم‌ترین موضوع برای بازارها، احتمال تمدید آتش‌بس تجاری آمریکا و چین است؛ توافقی که در ۱۰ نوامبر منقضی می‌شود. مذاکرات مقدماتی اسکات بسنت و هی لیفنگ در نیویورک نیز نشان می‌دهد که دو طرف پیش از دیدار رهبران در حال تلاش برای حل اختلافات مربوط به تعرفه‌ها، مواد معدنی حیاتی و دسترسی به فناوری هستند.
اگر ترامپ و شی بتوانند حداقل یک چارچوب برای ادامه این آتش‌بس ارائه کنند، نخستین واکنش بازار می‌تواند کاهش ریسک تجاری باشد: سهام و دارایی‌های پرریسک حمایت می‌شوند، فشار بر زنجیره تأمین کاهش می‌یابد و بخشی از تقاضا برای دلار به‌عنوان دارایی امن می‌تواند تخلیه شود. در مقابل، شکست مذاکرات یا تهدید به بازگشت تعرفه‌ها می‌تواند مجدداً سناریوی جنگ تجاری، تورم وارداتی و اختلال در تجارت جهانی را فعال کند.
اما مواد معدنی کمیاب شاید از تعرفه‌ها نیز مهم‌تر باشند. چین همچنان اهرم بزرگی در زنجیره تأمین عناصر کمیاب و مواد حیاتی مورد استفاده در خودرو، نیمه‌رساناها، هوافضا و صنایع دفاعی دارد. آمریکا نیز در مقابل، محدودیت دسترسی چین به فناوری پیشرفته را در اختیار دارد. بنابراین این دیدار در واقع مذاکره‌ای بر سر «اهرم‌های استراتژیک» است، نه صرفاً تراز تجاری.
برای بازار طلا، نتیجه اهمیت ویژه‌ای دارد. کاهش تنش تجاری می‌تواند بخشی از صرفه ریسک ژئوپلیتیکی را کاهش دهد؛ اما اگر نشست به بن‌بست برسد، هم ریسک تجاری و هم تقاضای پناهگاه امن می‌تواند افزایش یابد. هم‌زمان باید نرخ‌های آمریکا را در نظر گرفت: اگر توافق تجاری باعث تقویت چشم‌انداز رشد آمریکا شود و بازدهی اوراق بالا بماند، اثر آن بر طلا الزاماً مثبت نخواهد بود.
ایران؛ مهم‌ترین بخش پنهان نشست
ایران احتمالاً یکی از موضوعات حساس مذاکرات خواهد بود. واشنگتن از چین انتظار دارد در فشار اقتصادی علیه تهران همکاری بیشتری داشته باشد، در حالی که چین همچنان بزرگ‌ترین خریدار نفت ایران است و روابط اقتصادی نزدیکی با تهران دارد. گزارش‌ها همچنین از تلاش آمریکا برای اعمال فشار بر شبکه‌های مالی مرتبط با تجارت ایران حکایت دارد، هرچند واشنگتن تاکنون بانک‌های چینی را در موج اخیر فشارهای خود به شکل گسترده هدف قرار نداده است.
برای ایران، اهمیت نشست در این است که چین می‌تواند بخشی از اثربخشی تحریم‌های آمریکا را خنثی یا تشدید کند. اگر پکن حاضر شود در زمینه نفت، شبکه‌های مالی یا دور زدن تحریم‌ها همکاری بیشتری با واشنگتن داشته باشد، فشار اقتصادی بر تهران افزایش خواهد یافت. اگر چین در مقابل، بر ادامه تجارت انرژی با ایران تأکید کند، یکی از مهم‌ترین کانال‌های فشار آمریکا محدودتر می‌شود. همچنین شایعاتی درباره کمک اطلاعاتی چین به ایران در راستای دقیق تر کردن هدفگیری موشکهای ایرانی منتشر شده که احتمال بحث طرفین در خصوص آن می رود.
از منظر بازار انرژی نیز موضوع حساس است. هرگونه توافق آمریکا و چین که به کاهش تنش‌های ژئوپلیتیکی منجر شود، می‌تواند از صرفه ریسک نفت بکاهد. اما اگر ایران در مرکز اختلافات آمریکا و چین قرار گیرد و هم‌زمان اختلال در جریان انرژی منطقه ادامه پیدا کند، نفت می‌تواند دوباره تحت تأثیر ریسک ژئوپلیتیکی قرار گیرد.
در نهایت، اهمیت واقعی دیدار ترامپ و شی شاید در یک «توافق بزرگ» نباشد؛ بلکه در این باشد که آیا دو طرف می‌توانند رقابت استراتژیک خود را مدیریت کنند بدون آنکه وارد مرحله جدیدی از جنگ تجاری و فناوری شوند. برای بازارها، همین تفاوت میان «مدیریت تنش» و «تشدید تنش» می‌تواند مسیر دلار، طلا، نفت، سهام و ارزهای آسیایی را در هفته‌های بعد تغییر دهد. برای ایران نیز سؤال اصلی این است که آیا تهران از رقابت آمریکا و چین فضای بیشتری برای مانور پیدا می‌کند، یا اینکه واشنگتن و پکن در نهایت بر سر اعمال فشار هماهنگ‌تر بر اقتصاد ایران به تفاهم می‌رسند.</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/21010" target="_blank">📅 21:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21009">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ممکن است برویم یک نایت کلاب اما آنجا شربت بیدمشک سفارش بدهیم !</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/21009" target="_blank">📅 21:48 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21008">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">محسن رضایی :
دکترین هسته‌ای ایران تغییر نکرده، اما خروج از NPT ممکن است</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/21008" target="_blank">📅 21:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21007">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WsQ5mRJzlHS6m7bHPN8AdMLkH_ucMwkcAmmTB9NFkkq-n3U0fT6gW25dAKnufcDkHFqD5tvtQhuUewobWSyj7rRnL5xEyYukb2vBcVy-Y6CjEkmXsejM-lEse0qHDp7EQndum8QGnybtAD0a7Xi_-V7OIISVG6jk09qFpPwhFMElbAefe23aqYjmJbtdJROzPqzBvuES6mqkM_cIeEdR_05z78Ni63bC3fYuiJzN327JENPrsJq8STVayiXLZllWnrqt8kLUtsn1-d7sFmxeSJOSck9aSfOXTHzNUiL9TuZ-absIrladD3UuFEABmLmQ3BR5weWFhHy_tmKZarP9hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب امروز و بعد از ۹ ماه تارگت ۲۴۰ هزار تومانی دلار محقق شد.  بعید نیست مدتی رنج بشود.</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/21007" target="_blank">📅 20:29 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21006">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ترامپ می‌گوید توافق با دانمارک، «کنترل دائمی» ایالات متحده را بر امنیت گرینلند تضمین می‌کند  ترامپ می‌گوید توافق گرینلند، رقیبان ایالات متحده را از ایجاد پایگاه‌های نظامی در آنجا منع می‌کند</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/21006" target="_blank">📅 20:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21005">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">محسن رضایی:   خواهان پایان جنگ میان عربستان سعودی و یمن هستیم و معتقدم یمنی‌ها نیز خواهان دستیابی به توافقی با عربستان هستند</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/21005" target="_blank">📅 19:38 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21004">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">📌
جنگ ایران؛ رشد و توزیع ثروت و درآمد مصرف‌کننده آمریکایی و چالش فدرال رزرو  با وجود فشار تورمی ناشی از انرژی، درآمد واقعی و ثروت خانوارهای آمریکایی نسبت به سال گذشته افزایش یافته، اما بخش بزرگی از رشد ثروت از افزایش ارزش سهام و املاک ناشی شده است.  این نابرابری،…</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/21004" target="_blank">📅 19:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21003">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbjJa_AhDzUmXd8cK5FEDPG7Fbcpbwq_1ZK9swJAfP5AxH8UhvzUhBwu82Bcjp9fv-2nbhgDcYRJsxInqSjSNW8wkFtyhoB0JLze538lYhqLop1aeFLm5g7UbJwuCOW0BOUYLnmRuEz8RiKjS79mmORTCiEUvdgkikuyzbS89vGbjDOCEheL6-6DagXyLdYvHgYRd0oUo0yjH9mvDIrewUTspA3JY7fOE0_cJSaPXq31t36ebbfvned0qpxrh8Qp6_p0wLtEMX_wgdpCJng53r8b_VFpw8YvXuSmHWMgP9yA5SLnvnSR08zMBPKSr_k6_Ihu0jp3PF9miA-sv1c70A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
جنگ ایران؛ رشد و توزیع ثروت و درآمد مصرف‌کننده آمریکایی و چالش فدرال رزرو
با وجود فشار تورمی ناشی از انرژی، درآمد واقعی و ثروت خانوارهای آمریکایی نسبت به سال گذشته افزایش یافته، اما بخش بزرگی از رشد ثروت از افزایش ارزش سهام و املاک ناشی شده است.
این نابرابری، چالش مهمی برای فدرال رزرو ایجاد می‌کند؛ زیرا رشد دارایی‌ها می‌تواند مصرف را تقویت کند، در حالی که افت بازار سهام می‌تواند همین اثر را معکوس کرده و به کاهش تقاضا منجر شود.
🔗
ادامه یادداشت از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/21003" target="_blank">📅 19:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21002">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">محسن
رضایی
:
خواهان
پایان
جنگ
میان
عربستان
سعودی
و
یمن
هستیم
و
معتقدم
یمنی‌ها
نیز
خواهان
دستیابی
به
توافقی
با
عربستان
هستند</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SBoxxx/21002" target="_blank">📅 19:12 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21001">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRiQTGuy1bk-UKANGvibAyArjKA4YJjdNho3kIG8jkXSy9a29_hnDoJi2WVcu3Q077pf3BOcDXLzPcvTMjl5fhS5CW5GolhGKtWW83co3umKxAQhNZyI54x3yJZ4FtaVNoNexZYr248Wb1H_lewRWke9L7n2in1A9lOqVqFi47qLm-h_vFIfnAAGCdC5Du5G7u0LfMOq0xcJS56TthduQlSWNiirzuZczn79Jlg2dS2ZwhkR-6qQ-lrSs2djMOHeoCLCwzNh4sLSJ4KRcKNeuLtx0SL4Bt7PxzTqUiJfI8fcLEh25ZfExHV4ZfkEDw0gT2tlEcdfXwT04fOPWRvMog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین وضعیت نتایج احتمالی انتخابات میان دوره ای پیش رو در آمریکا</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/21001" target="_blank">📅 16:22 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21000">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">WW3 is loading....</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/21000" target="_blank">📅 16:06 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20999">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">خطر جنگ هسته ای؟!  ساعت نمادین روز رستاخیز بار دیگر به یک یادآور قدرتمند از خطرات رو به رشد برای جامعه بین‌المللی تبدیل شده است. در ارزیابی ابتدای سال ۲۰۲۶، مجله «بولتن دانشمندان اتمی» عقربه‌های این ساعت را به ۸۵ ثانیه قبل از نیمه‌شب (ساعت فاجعه) رساند که…</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/20999" target="_blank">📅 16:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20998">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">رئیس کمیسیون امنیت ملی:   دخل و خرج زندگی مردم آمریکا با هم نمی‌خواند</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/20998" target="_blank">📅 15:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20997">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">رئیس کمیسیون امنیت ملی:
دخل و خرج زندگی مردم آمریکا با هم نمی‌خواند</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SBoxxx/20997" target="_blank">📅 14:38 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20996">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YW8NHK3UmedbBbIL-Ks87l3SFJlqtQC8y1deKjWsirRUIKrrQTip2hEXIMZ4z0mlj6KTCtowLS7REiAiphHoTLUO5j7kKg4X7hXTBNwI1wjmkGbOOHw4mUrtWHK2cOkvRPu8Z3BS-HeCREQYzp3570jPPREzHvTXSmr48ENg6BJifNMRU-1ZBJ2HGWhS54WDQR_CgE3sqDQ1YIijgx9FbJT0dmZH-0jxz2ObYD9trM61qdzNoUXd7lUM1na-MBCzfloMxpg3HwYRCsDbwhTMunwR3aQTLflvcf0Bd5D3S1KP_Jq9XWnDVZkS_BEwgD6QbtVcbzgZ3CR9wZGkbwSmGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش های موثق، ترکیه چندین پهپاد رزمی و شناسایی برای کمک به سعودی ها در جنگ یمن ارسال کرده که دستکم یک پهپاد کارایل توسط حوثی ها سرنگون شده است.</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SBoxxx/20996" target="_blank">📅 12:41 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20995">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترکیه مجوز فعالیت بانک ملت ایران را لغو کرد</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SBoxxx/20995" target="_blank">📅 10:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20994">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">آمریکا بسته دفاع هوایی ۲.۶۸ میلیارد دلاری برای اوکراین را تأیید کرد
وزارت خارجه آمریکا
فروش تجهیزات و پشتیبانی دفاع هوایی به ارزش
۲.۶۸ میلیارد دلار
به اوکراین را تأیید کرده است.
این بسته شامل
سیستم‌های دفاع هوایی برد بلند، پرتابگرهای متحرک، رادارهای ضد پهپاد، قطعات یدکی، نرم‌افزار و پشتیبانی فنی
است.
اوکراین هزینه خرید را از طریق
کمک‌های مالی اروپا
و
کمک‌های نظامی خارجی آمریکا (FMF) که قبلاً تخصیص یافته بود، تأمین خواهد کرد.</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SBoxxx/20994" target="_blank">📅 08:20 · 28 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
