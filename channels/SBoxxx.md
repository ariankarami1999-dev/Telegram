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
<img src="https://cdn4.telesco.pe/file/rmx4GoyjeyIPANEXiOM8RG-fzUkdWHrF2z_r9lJ1u3iHMmIc0PEABf-fU0FnKwUl5UK_UMdKeDhA75leLsiJjvvyZUkrwiP24KVCDa_f4DwL23hqj1gw4EcaYy4VabghMu68RQXTgbraZQiwR4aSFAB4GxXwQSrQMj4-JRVgz5tGXrqn1oHjZptaLY3xBPkQ1xC96EXn-2m7ZwcYjKVbHSzudQ97iUiJs01YBh7vZRXq-Ro-qIHYag07rFzUVigERVX9T_Zb5IM6G6cjmDgERfKg5Gv90XW6thUkXLd4Io5BMVkGYfvd_OXmL1tQzHKv399P31CMhYD7afb4ZEVruQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.9K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-31 18:34:28</div>
<hr>

<div class="tg-post" id="msg-21103">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ترامپ:
در ۱۲ ماه گذشته ۱.۵ تریلیون دلار در ارتش ایالات متحده سرمایه‌گذاری شد.</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/SBoxxx/21103" target="_blank">📅 18:05 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21102">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">یک مقام عراقی به الجزیره:
«به فرودگاه‌های عراقی اکنون دستور داده شده‌ است از فرود هواپیماهای ایرانی، از نیمه‌شب امشب، جلوگیری کنند.
اقدامات انجام‌شده علیه هواپیماهای ایرانی مطابق با تحریم‌های ایالات متحده است».</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/SBoxxx/21102" target="_blank">📅 17:30 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21101">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ولی من هر چه میشمرم، رفع محاصره یک شرط است نه ۷ شرط !</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/SBoxxx/21101" target="_blank">📅 15:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21100">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">— مارکو روبیو، وزیر امور خارجه ایالات متحده:
«ترامپ آمادگی دیدار با پزشکیان را دارد، اما باید بدانیم که تصمیم‌گیرنده نهایی در ایران رهبر معظم است و او یک روحانی شیعه افراطی است».</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/SBoxxx/21100" target="_blank">📅 15:56 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21099">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">به نظر من نوعی کرنش در برابر چین از سمت ایران است که نشان بدهد برای حرف چینی ها تره خورد می کند. چین روابط مستحکمی با سعودی دارد و همین چند روز پیش هم مشخص شد موشک های بالستیک DF-21 در اختیار سعودی قرار داده که با آنها یمن را می زند.  در آستانه دیدار رهبر…</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SBoxxx/21099" target="_blank">📅 14:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21098">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">سخنگوی سپاه:   اگر مصلحت ملی ما ایجاب کند که در کنار جنگ، مذاکراتی انجام دهیم، باید مذاکره کنیم</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/SBoxxx/21098" target="_blank">📅 14:51 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21097">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - Podcast 28</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SBoxxx/21097" target="_blank">📅 14:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21096">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - Podcast 28</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/21096" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 28
سه شنبه 22 سپتامبر  2026</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SBoxxx/21096" target="_blank">📅 13:56 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21095">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">— شرکت هواپیمایی ترکیش ایرلاینز، به همراه پگاسوس و ای‌جت، از ۲۱ سپتامبر تمام پروازهای خود به ایران را لغو کرده و حداقل تا مارس ۲۰۲۷ هیچ رزرو بلیطی در دسترس نیست.
تحریم‌های «عملیات سرد اقتصادی» ایالات متحده آنقدر گسترده است که حتی هواپیماهای ایرباس حاوی قطعات ساخت آمریکا را نیز شامل می‌شود و برای شرکت‌های هواپیمایی ترکیه چاره‌ای باقی نمی‌گذارد.
شرکت هواپیمایی ایرانی ماهان ایر نیز پروازهای خود به استانبول و آنکارا را به حالت تعلیق درآورده است.
اسکات بسنت، وزیر خزانه‌داری ایالات متحده، گفت که خطوط هوایی ایران از ۲۳ سپتامبر با تعطیلی جهانی مواجه خواهند شد و هشدار داد که شرکت‌هایی که به آنها خدمات ارائه می‌دهند، ممکن است در معرض خطر از دست دادن دسترسی به سیستم دلار آمریکا قرار گیرند.
ترکیه یکی از آخرین مسیرهای هوایی بین‌المللی مهم موجود برای ایرانیان بود.</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SBoxxx/21095" target="_blank">📅 13:41 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21094">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ولی من هر چه میشمرم، رفع محاصره یک شرط است نه ۷ شرط !</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SBoxxx/21094" target="_blank">📅 12:54 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21093">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4lLWAk5pN7nwm794q6FbtOJMnbzmLJZXsVuO9lnEmkIvE3u3bLIq09yVRqY2gFF5TBn2aKk6WQSZruPgSGCO6xeo6Wx0SUnLByBjNPU6aYgkjlYIq34stdF_5pgosSkHCRjuNk3F3PXP4e_ph_ybFSTCyGUEEuMAaj6N0CWpTuTsYsegvEscEdwoK5NuleNpPclH2mIpj5lIYfWA8LGQ9d1jsXRGYf1F8sT_GBUSEpOF7uTcbTZcyRmHB1RaA6TMIXmQJTRTSMlYUCFpnAvSZ_lB34KM0SYF6QtmZ9eRKvioX3uXwGGWlv4PLUk7rzhd1eCUOjDKPpXCDMsPTpc8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران می‌گوید تنگه هرمز را مشروط به رفع محاصره ظرف ۷ روز بازگشایی می کند.</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SBoxxx/21093" target="_blank">📅 12:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21092">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l77-EeM--tMkLtUYHFV9XzibwQ1rqmP7WcidYBbBoZMqYXJVG9AN6eEILJZsFTGTR3UIVL7ga2ljK7CO-6Y9yfKwxql42ePcheVX57xoF4hKj0Q34IcNsxFHfaqxT4xwfpk1G4yRgkPCyjjOMOELyYZM8GgbmTY0UTlGuRSRSDbgz_zV2gAJrKsht1MdMZEmLkZBpGG1_1LOLqGaSat2IPdlrK-YI81t6qI6wSf69TymZRv5frJUPAE6ZOONhmXVtn1-9TDqL4iiHTgWzNqGmd5hm4fYeaPxuXdaJL6B7qeWcvcjfP5XU90-koxiTJzaymf6i-Yhqa2fcaqWZ_ZfeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سه کله پوک پیمان مکه کم بودند، حالا وزیرخارجه مصر فقیر (خر دوم از راست) را هم با آن ریخت و ترکیب ش add to group  کردند!
فقط سیس هاکون فیدان !</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SBoxxx/21092" target="_blank">📅 12:41 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21091">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJ-AD6B_jssTLoNaqNBVX_MCvK3N-zJza9lIATpvQLXpj8L8zYLl0LpaJrD3XYISvEVxkczLj1hlaAA6t-2jui9r0xJPG7a7qX4jAQGn_HE8IHU3i1uwctXacQADlCH4V1Pd9GWADtskOTJGGRjbizrjwzmEHl6R9oYkrMTGGp3uqcH6_dZi5x-cVwMwbq0imU3WPhntf-TJIKY2oFTqJGya6-GGk_mPf-jHaE-s3reBw6hZ4j0tQoaxcL8ShZFHp6GA8j8RHo8QoC-QPmij9CRX7L9-xsklkrhlBAAii_HKWS1d612K0_EqxkIp1rl3GgLJnk4ceJqBhU80M469jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve  نمایه FVC کماکان زیر محدوده منصفانه است و هر چه افت طلا بیشتر بشود برای خرید ارزنده تر خواهدشد.</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/SBoxxx/21091" target="_blank">📅 12:36 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21090">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">به نظر من نوعی کرنش در برابر چین از سمت ایران است که نشان بدهد برای حرف چینی ها تره خورد می کند. چین روابط مستحکمی با سعودی دارد و همین چند روز پیش هم مشخص شد موشک های بالستیک DF-21 در اختیار سعودی قرار داده که با آنها یمن را می زند.  در آستانه دیدار رهبر…</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SBoxxx/21090" target="_blank">📅 12:33 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21089">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">چارت نفت جوری است که به نظر یک کاهش تنش داشته باشیم و دیدار شی-ترامپ مثبت باشد.</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SBoxxx/21089" target="_blank">📅 12:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21088">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ایران می‌گوید تنگه هرمز را مشروط به رفع محاصره ظرف ۷ روز بازگشایی می کند.</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/21088" target="_blank">📅 12:32 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21087">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ترامپ می‌گوید توافق با دانمارک، «کنترل دائمی» ایالات متحده را بر امنیت گرینلند تضمین می‌کند  ترامپ می‌گوید توافق گرینلند، رقیبان ایالات متحده را از ایجاد پایگاه‌های نظامی در آنجا منع می‌کند</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SBoxxx/21087" target="_blank">📅 12:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21086">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SYinTfyKuDi_9aPn7wKa0PEBR3cV2jEu-wyGXnnYbjklI_0jzgxyPLL5loHRZuEasBo-rZKCVUfmjk1AlRsoBOcwPY8XKbUBhvGjPmxOC6v6dF19z0xXE7wl7PDXwEPFs24C42_xUQCeoYSXiS_x0LbcRDynnn-Gjpmk3mKcNp5ldR755vGdeOiVKOtZj7bLUTpjs-6AEQ6Zbx56q9Ymfefjxw9GaeUPqgE90LVTjIQ-rwOgxN6zdIWtEFlDER9lWboaXQBvBwphU3XzZkklqm2rx0HuKyr3mfj5-hTlecES0bpH5izjpgD38qiO3jXOVIZxenkZQ19qGHlW2gO47A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC کماکان زیر محدوده منصفانه است و هر چه افت طلا بیشتر بشود برای خرید ارزنده تر خواهدشد.</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SBoxxx/21086" target="_blank">📅 11:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21085">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFrw8p7HQVRpA6HgxOl0WXlTJ1o_DCsy4vOcm6BMDDzGRqRuW2pOahXl6Znk9pdV0GonEMhp8jF6Wpcc5FpclHu6putrWHYrS-KBQJR2QC0BsBWKngXGx2iM-PXzctq2uKEWB0y7teq785mTBxDtCL9L3S0m4wBsqOTKYAY9Cr3COmCLW-szJtPkauRRnbD9hQTYEQu8KujuWBYlj4ulq8-hPU6rkWJsauMVhmRXjqkCh2QrD2gM4dLZo33UB3kpGuizOK1KnYwdMRy2co8LzzuC2A-QeHQ1i1qg6SvyvNs1vCbP23xJRoVwvVT-r83LiNxGoyHbXb7qisHxVPCIVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح بسیار بالایی است. اما نظر به ریزش سنگین طلا، اثرگذاری اش را گذاشته است.</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SBoxxx/21085" target="_blank">📅 11:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21084">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxb1Ed9I7_YmHeT9Jtnf3ATRX0tTCttvdEkUC0FGkoj6Y6lgIPXlgg1wIYWJh21E_9EFQXPoaHEBmky4P5EAglrY9YEuyvkbwgPBn-49rt4k8R61o9yJKYEHMH80dYnZuyQ7y6gwV6TLGMeHJ2X-gqrnx4uLOSAHz8trz9rG33-U5AUSAhCu90HcG3L03Wd0E55Y98gJjR0Bjqp1wkCw4tLPjlOh4bmic33PzyCqRQDkN2xpVKW9xXbn13rIYffyWJ0LxtZzPsAV0f0yHCF2hDbILdyT0ikdpCWbLFCqB0S_w29n5x1AaHKjBPrdDUeSSdisaXMbxKus4q_CZCDkdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک پله خرید طلا توصیه می شود.</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SBoxxx/21084" target="_blank">📅 11:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21083">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">کاخ سفید، پخش ۲۴ ساعته‌ی «کانال تلویزیونی ترامپ» را آغاز کرد
!
کاخ سفید، پخش مستمر
«کانال تلویزیونی ترامپ»
را از طریق یوتیوب و پلتفرم X (توییتر سابق) آغاز کرده است و وعده داده که سخنرانی‌ها، اطلاعیه‌ها و مهم‌ترین بخش‌های فعالیت‌های دولت را به صورت "به‌روزرسانی لحظه‌ای" ارائه خواهد داد.
کاخ سفید در پلتفرم X (توییتر سابق) اعلام کرد: "شاید همه لحظات مهم در تلویزیون شما پخش نشده باشد، اما اکنون این امکان وجود دارد."
کانال یوتیوب، این پخش را به عنوان
«پایگاه اصلی»
معرفی می‌کند و وعده می‌دهد که مهم‌ترین لحظات و بخش‌های برجسته دولت ترامپ را به صورت ۲۴ ساعته ارائه دهد.</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SBoxxx/21083" target="_blank">📅 11:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21082">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sp_Em6Iv1JfECJAMUVSuhdgxdJQvKlzz2ugl3du_2La1W7Y73w0csBirII1rNG5ajEZgU3CzMmmXobEOlDm9IrTuAP4-he5LER1D-QJy9fcV-V_uVMl_w8t9Ub5xU5JKijopTwJhqNruvfe4u8gjxaJQPV_E2bOJ5UGrwd5Jx7VrX94fMm6z4JZ8DLeJLuumAv7LnrpSoMu9QWsHkmJ0XLoghYjUYRPSFgdSdznlxHXrMqH_IlNKlSNJbK38kqM0PVz37mEpSGtmW81oNkjYWYbX7O82uBF8Uu1-_traBzo-MnQLgaSbA-CafWDkwU2oBbIeVqmM2wsKgzWpoHQ5BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح میانه ای قرار دارد و با توجه به افت بهای طلا، به احتمال زیاد دوباره حمله به سقف جمعه و حتی فراتر رفتن از آن را خواهیم داشت (یعنی بالای 4400)</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SBoxxx/21082" target="_blank">📅 10:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21081">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JS14if3DG4DOauBQ2IztQm7tOyfuPydwuSqqjKqFdQqlA0ECkP4jHwcAp7ZFD045x2NsrIKgRazDaktePncqR1KGjlbn3GQsCrwp9zw3PwjQIrftArLNl16I8bKUHzUG9EXh8SStLCdYpB9a-c5ot9EBQ95XzZHzu9CfZLvT8Pmsbv1hWxIF__xN-DYfxakhODyQW3KIn7VnEMsuXXCFBhZ_Io6Sw-KubMsVvxxOa-ES8llpRREyFuar-L3kGd_LoHgzbO-GRa9lAE9F-XhkNnywiLLKI3TnEEmCfqJS4JalRj6NSvCxoVLpn1ZDWOhhni4fjHrbqhctv5x7ob0wRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمونه ای از جامعه ای سرشار از زور و ریا!
حجاب اجباری بر سر دختر می کنیم تا در بلوغ و بزرگی محجبه باشد اما همین الان مادرش بدون حجاب است!</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/21081" target="_blank">📅 09:50 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21080">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">رئیس‌جمهور ترکیه، اردوغان:
ما آماده‌ایم همکاری‌هایی را که با ایالات متحده در حوزه‌هایی از جمله انرژی هسته‌ای و LNG، حمل‌ونقل هوایی مدنی و فناوری‌های پیشرفته برقرار کرده‌ایم، گسترش دهیم.
توسعه بیشتر صنعت دفاعی — که به‌طور سنتی یکی از قوی‌ترین حوزه‌های مشارکت ما بوده است — هم به‌صورت دوجانبه و هم در چارچوب ناتو ضروری است.
ما می‌خواهیم موانعی را که هرگز نباید بین دو متحد وجود داشته باشد، پشت سر بگذاریم و شتاب تازه‌ای ایجاد کنیم.</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/21080" target="_blank">📅 07:51 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21079">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YnDJ-8FIQJwTBVsH3YJLn-NHvisw5CCW5B8pVDY1ZjC5g8F6ropCbyVfQGzeM6t_ncTKpT5td7gjO6tsF0C4pIPt6h84eNcKxZnYJFKTfTPrHfQ1zqEW0XsOFjgQqPZrp0kQm-ETBOIfy5okWcXRSqaQGwM-CP41Ls4U4rAqQYh6pXn9C2b94IXmK-qcq9tpUAbnBIhMa4sRMfzy8FnOAJ-QmUucZwY6m4OcWh1y0GJytrAKsfiM4-thE1G6-bXCrz7NPKAX5zjgy3S-UK_CvZ7HJvDwbun6kDwmbK53V8rURpTZJr0jhPT8Mi2RZoDzIlM4bb7nO3krF40P333FBw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/21079" target="_blank">📅 00:58 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21078">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">— ضرب الاجل دولت عراق برای خلع سلاح حشدالشعبی</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/21078" target="_blank">📅 00:55 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21077">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">هند نیز‌ به محاصره هوایی آمریکا علیه ایران پیوست؛ گزارش ها از توقف پرواز ها میان ایران و هند!</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/21077" target="_blank">📅 00:26 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21076">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">هند نیز‌ به محاصره هوایی آمریکا علیه ایران پیوست؛ گزارش ها از توقف پرواز ها میان ایران و هند!</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/21076" target="_blank">📅 22:07 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21075">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DiAuG4mbYCcaPQ9G483xqemqc-D6nL2G_spPDfrc77eOZm-kd6F6AU0U2lTQJPhX86SDJc1_IU54WugyV5Cjz7E7Ob9bOkvofdlESqjYFynyLxC0JRCLgNZUZ5dDiZOr13K7JhpF1cNnaoZd70XL9LMgVIsoIl9Bbm3DocZK-8mLCUSVa3cCehOAjRTkyv3JGEL4yQuDJB2V_v4UMi11R2r9Forj6TWkmH50e-NnFqaoJBDXdFnW9bfz5u-Dd4APH_w_OLmIbAfC5VERDumi-_kfHPC7U0t16JAigZ3gaNcI4INqmkYTySihC6EYsUtCUsEe6AOO9_ofgwy9lHUXgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام وضعیت !  فکر کنید پزشکیان بتواند آن ماموت ۱۵۰ کیلویی را با دستانش خفه کند!  اینها شده اند نخبگان ما!</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/21075" target="_blank">📅 20:08 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21074">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">رئیس خزانه‌داری ایالات متحده می‌گوید تمام خطوط هوایی ایران در ۲۳ سپتامبر «بسته» خواهند شد</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/21074" target="_blank">📅 19:52 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21073">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LpCNMAHcVHPtjIWuii3ytbfwOB1AXb19D0wKTXKi7RFIu8YKj0GcivTNvnTAy07QJ6MD29rHGRLST3Ma2JrjuuZQXEkMLgERQwaCJdsCuY_mCN-InUd36w0SCkVp-_eL9dM5XX6OK9sKZhYXYGW1Ik3MUUhgunKXdbIq4XAtP_CB5kAAM8p-ZBGmZbDSd6-dv84jbx3qsTLIB_Hu6GWksArl56DhKI2oXY2zJCu1VEX-to3WtHF1aIx5gtKYe5dSpsvPtwgzWlmCicAtMxh_l1U7FTIJH_AsffOR00LvY4aqLx-bxNmbyaqdmd374eZvSiX3Bs_ZsMQ164MZOv3-_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام وضعیت !
فکر کنید پزشکیان بتواند آن ماموت ۱۵۰ کیلویی را با دستانش خفه کند!
اینها شده اند نخبگان ما!</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SBoxxx/21073" target="_blank">📅 19:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21072">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">اظهارات جِی. دی. ونس درباره قیمت بالای بنزین:
به نظر من، همه ما باید این واقعیت را بپذیریم که تا زمانی که ایران در تلاش برای ایجاد وحشت در حمل و نقل بین‌المللی است، ما طبیعتاً تلاش خواهیم کرد تا در برابر این اقدام مقاومت کنیم. اما به همین دلیل است که قیمت بنزین اینقدر بالاست.</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/21072" target="_blank">📅 18:26 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21071">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zkep2UE4JOokns4Jc5i7z2OFmpm5yF1iVGUimn5UaJLcPKbncmzHce1FqpLCId2ehP_-AiNCtd8_4ggC5b9ibe1PFZMbW30xzQGD-w9i_ZfXZOSG9HgBaThD9UNoGiBJDwq6KsAbT2CK8efxFyyWjYVb7WTZepW9wjSNzAW73qbuCFrXwJSh4Y_l4EkFxQrh8UcxCootzxcOWwuy0E8tRaobbJXklLRwktnVt8t0Lx1qE1KnxY5-jGW-E-n3Vx8WRPSC7P4a32tbw8Fv8VmiBuYhcnSW7LDMp3eMyxxVdKCX28i-UiZGgjamP70lonBdZyi_Bchx8bRU8UZxjSc9Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/21071" target="_blank">📅 17:51 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21070">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">درگیری های سنگین میان نیروی انتظامی با جیش العدل در سراوان</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/21070" target="_blank">📅 17:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21069">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">رئیس خزانه‌داری ایالات متحده می‌گوید تمام خطوط هوایی ایران در ۲۳ سپتامبر «بسته» خواهند شد</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/21069" target="_blank">📅 17:08 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21068">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">جان کیریاکو، تحلیلگر سابق سیا:
اسرائیل هزاران افغان را در ایران با ۱۰۰ دلار برای جاسوسی به خدمت گرفت.
کار اسراییلی ها اینطوری بود:
«در این گوشه بایستید و هر بار که این ژنرال را در حال رانندگی دیدید، یادداشت کنید و برای ما بفرستید.» بفرمایید صد دلار.
اسرائیل هزاران نفر از این افراد را استخدام کرد.</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SBoxxx/21068" target="_blank">📅 13:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21067">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n9rTebxBcYVyvWrS6YMll3hxp9ptrTpkbAHJScdhEZA8q7aZ9wexz1oD7PC1ffHyiwtqqI85F3qVQegqMARbjokECgRkK43SdzCUnbdfWaEmpwlz0KXogDC9gqMYLPt1CNn85MSt1cg9so3uKRVaT5dcaJc8asYedsNxXUG4rDAyZuuw_xC50pj13v4TGGiC8VkZ7p_VmwazXuA5qWi579WKlbT9-ii0hc3iMCZm3WsHXuCGpQr3Du9VuLEs_zQfk91skXk0VtROwv9QvPVcQ071oI9tBWTFgX0oRaGCnSXShRMREQJZ7ConoHoCp2S_7bmvpsJD7ZRAxgOy9eQV5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC در محدوده زیر قیمت منصفانه قرار دارد و لذا فضا برای یک رشد در طلا هموار است.</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/21067" target="_blank">📅 11:52 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21066">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XqYPF38FncmC1YtHtml5ENozSYALtuPBo6V-pRBxMaI6JGl7TBoCqN8mnG2zCN6NSE1I6Cc84ziiOlpSlNqU8yVMf1sCNZWQtKpmnXpPgIczp8q1dKIv6cJiJ6hMU0BkCCFKeUlRS-4icJOyBewOHQbMl7f_rELP4Ic5-uht2Hd_h0C0O3-kF2XQ_jpZ_YB_JrE0m6mYuMFxKAEU7GjQvbi2LYk8UrPfztio66PVMFtt7UqIdUP3B7oCpP27IY_kBjrzEXqahnBwEmAt2wBgx_p4n-6E0cyaGBE753EdUeAUmn8ge1npJmYP0AyVZlSoK2j4gPcPyOnri4nmjIIFhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح میانه ای قرار دارد و با توجه به افت بهای طلا، به احتمال زیاد دوباره حمله به سقف جمعه و حتی فراتر رفتن از آن را خواهیم داشت (یعنی بالای 4400)</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/21066" target="_blank">📅 11:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21065">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">قیمت متوسط گازوییل در آمریکا برای اولین بار از
۶.۵۰ دلار به ازای هر گالن
گذشت. از ژانویه ۲۰۲۶، سطح عمومی قیمت‌ها (موزون با شاخص بهای مصرف‌کننده)
۴.۸ درصد
افزایش یافته، در حالی که قیمت سوخت خودروها
۱۷ درصد
رشد کرده است؛ این امر احساس بحران توان مالی را تقویت می‌کند. دونالد ترامپ، رئیس‌جمهور آمریکا، تمایل خود را برای دیدار با سید پیش‌وا (پزشکیان)، رئیس‌جمهور ایران، اعلام کرد. با این حال، گفتمان طرفین همچنان منفی است. توافق آمریکا با دانمارک درباره گرینلند می‌تواند گامی مثبت باشد (بازبینی یک توافق موجود می‌تواند یک سابقة مفید باشد)، اما عدم اعتماد بین آمریکا و ایران اوضاع را پیچیده‌تر می‌کند.
مِرتس، صدراعظم آلمان، پس از باخت در انتخابات منطقه‌ای هفته گذشته به چپ رادیکال و راست افراطی، سوگند یاد کرد که در سمت خود بماند. به صورت ساده‌انگارانه، نگرانی‌های اقتصادی به نفع چپ رادیکال و نگرانی‌های اجتماعی به نفع راست افراطی است، و روند جهانی به سوی قطب‌بندی سیاسی پیش می‌رود.</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/21065" target="_blank">📅 11:48 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21064">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OjIR6RHtqLeTvxJnJj9qvnkVZUylIARBxmtfVnJ-YKagUDuprtGmgVJSNBmtU-BqOEQudthkhU95rD_hAwB43nVaFSuGgpJFx1LiyHZUikpE_bqPfoIp1wZMi_tJO2clmwAO365Sx0rt2tTERQOKrFj6LK2zAvM1-YM3n8y9PRWibGpDCs-UyWlVsnimv_ykbrM4QIpQDPwJOvRha1iTSERAakxqnGEU6wzLr_r_Nk4JKAP2XnyQjPViLdOSwLPBpI-QUQUu2icyNmcRLNDNGF4TLSZNLM097xpkhtFFILBAnYlI0O90DcQFoPZsUU4s2ROs4rBi_C_vYInCLK3kyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چین میزان اوراق خزانه‌داری آمریکا را به پایین‌ترین سطح در 18 سال اخیر کاهش داد.
چین بیش از یک دهه است که میزان دارایی‌های خود را کاهش می‌دهد. این میزان از حدود 1.3 تریلیون دلار در اوایل دهه 2010 به 618 میلیارد دلار در حال حاضر کاهش یافته است.
این کاهش پس از سال 2022 تسریع شد، زیرا چین نگران وابستگی بیش از حد به دارایی‌های آمریکایی شد.
دولت‌های خارجی، خرید اوراق خزانه‌داری آمریکا را کاهش داده‌اند، در حالی که صندوق‌های تامینی و سایر سرمایه‌گذاران، خرید این اوراق را افزایش داده‌اند.
کاهش تقاضای خارجی، به افزایش نرخ بهره اوراق خزانه‌داری کمک می‌کند. نرخ بهره اوراق 30 ساله اخیراً به بالاترین سطح در حدود 20 سال گذشته رسیده است. افزایش نرخ بهره به این معناست که دولت ایالات متحده برای استقراض پول، باید مبلغ بیشتری پرداخت کند.</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/21064" target="_blank">📅 10:37 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21063">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ملونی ممنوعیت پوشیدن بورقا و نقاب را در مدارس ایتالیا اعلام کرد
«هیچ‌کس در ایتالیا نمی‌تواند تصمیم بگیرد که یک زن جوان باید خود را پنهان کند. برابری بین مردان و زنان نه در خیابان‌های ما و نه در مدارس ما قابل مذاکره نیست»</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/21063" target="_blank">📅 10:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21062">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اقدام بی‌سابقه دولت الزیدی:
یک “عراقیِ ارمنی‌تبار” سفیر عراق در آمریکا شد.</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/21062" target="_blank">📅 10:01 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21061">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rM_2zORTaG2jZ18Mo8MUtxCNAipsv_wA2uIxtVZpfHp8FJGCtAs7-xMZBAmHlgbl0n-J0I72XxNYR-NqmwU2OszNyqt9npJq3X2sEiyD5vgG4B1YI7J4l2oQrGn63ji5CWvrorv9RCPuTtkBvF6z2BahL60jUdh22CRxijwTSZCEo66oBJoBeGPpcHmBLge1aXQ3lRIBfQA1pqpFfyvnyJbwRVYbpNa7zfrKssdTdDlrkpQlAHwkFXS3yiGZdDUobqy5b9z4AE-zgFONmQwLpKC0LgUwy_ozuuPNL3Pt57dp_zMxvXVgBBI3deLP9HPlBj7xsySTJbipLxrL8ypGKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیده شدن یک هواگرد ناشناش در آسمان تهران امشب</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SBoxxx/21061" target="_blank">📅 01:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21060">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">یعنی همه چیز دیدیم جز قهرمانی....
هعیییی</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/21060" target="_blank">📅 01:35 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21059">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">دیده شدن یک هواگرد ناشناش در آسمان تهران امشب</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/21059" target="_blank">📅 01:34 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21058">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9e029fb89.mp4?token=uDB5_25uWgExOcFfEjkI8f5sHPWZfjwm4k7S5Pxa20MeMvb0oBD97_ogKLdAfpAxOdSikQemPuBFY3vGf1s4E6K6faFeq-cG9KE06RFU-7RO-PpBeeIq0tDYhoL45Ch2EdCF_LqkMoi2-8AyWdR6Ulz5A0jCAujHNd2dpbUT4hfNlwYpJ5J-b-HplM4g-V0DK53vNZmOi_YHUZIwH4MQoIy2ZFFrNUJHy_Nzq8tn57AJfJ5rSWFZ1MNHUCr7poZDHwTgzcksfrmrMYEwfccsqZapqTV1aOnYqQLWjwUG_10H3WHHrlfakzsMmGMGGipbAOIjEYG0ZhIagPZ33SOzaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9e029fb89.mp4?token=uDB5_25uWgExOcFfEjkI8f5sHPWZfjwm4k7S5Pxa20MeMvb0oBD97_ogKLdAfpAxOdSikQemPuBFY3vGf1s4E6K6faFeq-cG9KE06RFU-7RO-PpBeeIq0tDYhoL45Ch2EdCF_LqkMoi2-8AyWdR6Ulz5A0jCAujHNd2dpbUT4hfNlwYpJ5J-b-HplM4g-V0DK53vNZmOi_YHUZIwH4MQoIy2ZFFrNUJHy_Nzq8tn57AJfJ5rSWFZ1MNHUCr7poZDHwTgzcksfrmrMYEwfccsqZapqTV1aOnYqQLWjwUG_10H3WHHrlfakzsMmGMGGipbAOIjEYG0ZhIagPZ33SOzaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیده شدن یک هواگرد ناشناش در آسمان تهران امشب</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SBoxxx/21058" target="_blank">📅 01:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21057">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/304c99ed1e.mp4?token=DHYXM48xUgJj26vYy-oOAH3A5wCtd0ipt0X0gNzOqrygwT5YWvt4TpALky2bT53_pbokVAkcTps6JXLm5FEJPNbcIQhOPt1guv8pAyXEqqZXwuUvwIVu1KQiX108a9YjvIR9axq5C2GyCmUOqkPEDlOgCTIIsnhPa-Q7ctxHoYrlP8tT9L6TxPMPSKEVBvbIWGGthunYv19L93x7D3KUn_XR9jkhnYR9eI94w2nmp2nQ8pvhXdwfPxXlHhLrUHa0JTH34cuN1sJExKgE5xrPHMhsu14C_Nxy06VlzpEmEJ3IUnK3WuUt5eb9ul1cAIKTQWM4-DFzqTfc3m5l8tPYow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/304c99ed1e.mp4?token=DHYXM48xUgJj26vYy-oOAH3A5wCtd0ipt0X0gNzOqrygwT5YWvt4TpALky2bT53_pbokVAkcTps6JXLm5FEJPNbcIQhOPt1guv8pAyXEqqZXwuUvwIVu1KQiX108a9YjvIR9axq5C2GyCmUOqkPEDlOgCTIIsnhPa-Q7ctxHoYrlP8tT9L6TxPMPSKEVBvbIWGGthunYv19L93x7D3KUn_XR9jkhnYR9eI94w2nmp2nQ8pvhXdwfPxXlHhLrUHa0JTH34cuN1sJExKgE5xrPHMhsu14C_Nxy06VlzpEmEJ3IUnK3WuUt5eb9ul1cAIKTQWM4-DFzqTfc3m5l8tPYow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مستندی جالب از روند ساخت و امکانات شهر موشکی یزد!
بخش عمده اش به نظرم با واقعیت همخوانی دارد اما در بخش هایی از تخیل استفاده شده مثلاً بخش مربوط به نمایش طبعیت و روز و شب برای کارکنانی که 500 متر زیر زمین حضور دارند.</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SBoxxx/21057" target="_blank">📅 01:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21056">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v3lU1R0popaL7T1aMRU5p_HCK23aCbj5nKa6p2EsxvBYcYKhZUPwupXJLmh7yQixDXMXCf-3ki8QHRi7uMuscx1jY_0zpIE6OZejii3mi0wZBi--IcWrZcDzSLMbVmoZhaHpFJM-NqDJJftQvtbNbznygvmWSw9t3zQqAuJhU6EcOi4QfmJv3anhiqGosr7CV2jSFkWgR6FlCsJ2ilIHoeslAoy5VtMVYLoJe9rYw1zg4bbe-MUX6zbTYI51MA1KD04S5EqwLDKI_nM5WzSkbFFHsl7CF94iWFp32YaRB1wqQ4QVqLbYWwa4pHK9ptYwflCRfOM47o9d41ogD5AByw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ می‌گوید توافق با دانمارک، «کنترل دائمی» ایالات متحده را بر امنیت گرینلند تضمین می‌کند  ترامپ می‌گوید توافق گرینلند، رقیبان ایالات متحده را از ایجاد پایگاه‌های نظامی در آنجا منع می‌کند</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/21056" target="_blank">📅 01:16 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21055">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">واقعا تا حالا کسی رو ندیدم  که با این جدیت کصشر بگه
😂
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/21055" target="_blank">📅 00:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21054">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7235f04196.mp4?token=qeMwgu3sM7Jkw53StGoQF7u_rJIEfLjUxcemlOh3adn7dQGImHWzlGeyTFN6i4MbmkarqqTR6RREoq6ED4Ni9vPdQ_hZZOPDLc1tjha8GLYgetxFWXpleT1UoimwbnJGHrC39GAdLEiI9smKWRr7FMU1D8bmUQ91g9FRlfYdiT7vcEEE1gR0zhQtBmf_5MJw0YdWw4vdFqTfRzJZyEk8BnVPO4QmbY_MMT21Qlo6rRH3KP-i6E1vLErSqd1ggd0v52jJm0RIpLBGct03GioDI5TzEDHoKYytmwIoK6FmCVIMbC9Pg7x2Ne_VGtMWBQFu-jjii3-DHatXi_aKTJYn2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7235f04196.mp4?token=qeMwgu3sM7Jkw53StGoQF7u_rJIEfLjUxcemlOh3adn7dQGImHWzlGeyTFN6i4MbmkarqqTR6RREoq6ED4Ni9vPdQ_hZZOPDLc1tjha8GLYgetxFWXpleT1UoimwbnJGHrC39GAdLEiI9smKWRr7FMU1D8bmUQ91g9FRlfYdiT7vcEEE1gR0zhQtBmf_5MJw0YdWw4vdFqTfRzJZyEk8BnVPO4QmbY_MMT21Qlo6rRH3KP-i6E1vLErSqd1ggd0v52jJm0RIpLBGct03GioDI5TzEDHoKYytmwIoK6FmCVIMbC9Pg7x2Ne_VGtMWBQFu-jjii3-DHatXi_aKTJYn2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واقعا تا حالا کسی رو ندیدم
که با این جدیت کصشر بگه
😂
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/21054" target="_blank">📅 00:14 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21053">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dtYpR-hTrkfx9nF1ECRoq4SGgMPvnfT2_NfNzQTAevyanuanLVz5FwRiw48J4OkTYCAVEwAemfQUduK7KVsDDdGvPF8thpAkb4-owz-89uTzZeQfVwBv_B8MuvI6si_l8sP9Fxg1id1yKpKumTBZz39IVzeVHlKuo5IFMPJIKJctbhuYuaVZOrF2rbm4AHt7vQXoUMKTOSqBViT6JZxz0zUTN4fenHDcljruyYlTRp9FRaSo34KfrPCmTHy40--RbYuwmjMs7hbVkCCSJbTeuB8_0f0Y5ORCUWO8ABCGCTixa4r5cuQMAipd6GNmSnlu9bGr2yQZylWhDlL9tW1qlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SBoxxx/21053" target="_blank">📅 23:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21052">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">چارت نفت جوری است که به نظر یک کاهش تنش داشته باشیم و دیدار شی-ترامپ مثبت باشد.</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SBoxxx/21052" target="_blank">📅 23:34 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21051">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BdiHXVh621twfnYxvEPC6ezlZS8s9d2sfUaAg5tpPXKtVveD0IX_Rmk-autzVO_xEfYEu-_qtmNRCSFNpOGkb9RTuWy-fbsBvZi_pPrAMARcKNyjvm3RadJ4xDqtNCVIKfnhboyFrScWa4PGp4290AtD2JqgpHbwQcnezJZOxu67vscn9XuHjvtPVBx40zJWNqV6uuz0tkJSGoeiPwQhVnGf-2myrBzctxJHWTsSAPqdZgdAh3zbtG7a_YudCM9Hru6cLkBAeaCmKnlIHXo-bkvU4w93-vl8UjT17utRi1u7__1Owbk3yHYGnc1YNdJBP10Oi_bVtrL4NRqPojBh_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چارت نفت جوری است که به نظر یک کاهش تنش داشته باشیم و دیدار شی-ترامپ مثبت باشد.</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SBoxxx/21051" target="_blank">📅 23:33 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21050">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">حریم هوایی اسراییل هم بسته شد.</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SBoxxx/21050" target="_blank">📅 21:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21049">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSc0AgeH25vi8iSUW5qg16i0HYBTStnnLZJRV2nybldGQ5gm6KAAmJWTixSvyQrXuvFMBkP97zuEx-_HCmapChg-DX0lrzXAhj2_9y7hWDYABsm4CDpZr4L4Ke7b8VbVqFK3EXiWnkfwF8H9RcLcbyie78ggYRjkOfgrTPFwlCkrks8GWa29XqZ4RGtpFl2EV_-2UVOHjcHSWz1htxSqLItrRWLK_Xf9HSg11XBXPShR72q8yWVkclulW6_rwCxub3UtsdObUNA573RvDpvYAOLMneJ6G9Q0Btp3sCy7r5IO_6hX-YuhTJuPchuQCDHEdQUy5KvpG8hXgUMYn-Qftw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان:   صلحی که دشمن تو را به آن دعوت می‌کند، نباید دفع کرد</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SBoxxx/21049" target="_blank">📅 19:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21048">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">قالیباف:   هم میجنگیم هم مذاکره میکنیم</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SBoxxx/21048" target="_blank">📅 19:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21047">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">📌
تخریب تقاضا در بازار نفت و انرژی های جایگزین  شوک عرضه نفت در کوتاه‌مدت قیمت‌ها را بالا می‌برد، اما تداوم قیمت‌های بالا با کاهش مصرف، افت فعالیت اقتصادی و تغییر رفتار مصرف‌کنندگان باعث «تخریب تقاضا» و کاهش فشار بر بازار می‌شود.  در بلندمدت، اختلال پایدار…</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SBoxxx/21047" target="_blank">📅 18:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21046">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IKcEA-sBQXeFe_1rFhTuS_ZKFy8ODI7b5v_A2Ly1LoSTFzUrWZpgooss3pjRVsxCSmy1_eg50Y0_h1cScsnNvJCbuPufEQn3FUY-DqmFVv0sIBDsybHiElCfZsJ5IGzo60BhJB17n4SVJ7I7OLROXxzZJF0QITD1J5KyetwF5HyAfZVTVypw9oLgIHCMjr4W0QNkTeYK2ZlG1qumA7e7WYibeTUfk6i6zZfBD1kBfdHfA2-vZbDy2-hK4c_Yr5umCx0GwbvwJuJCz-Ux7I5Nms4wPRw8BjlBde3qpiXLVjzzaKkHqDV-6XtW9XCEDGDQLh6ccxeREcIBuMT0iACS_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ترامپ به فاکس نیوز:  برخی از مقامات ایرانی مانند موش‌ پنهان شده‌اند.</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/21045" target="_blank">📅 17:38 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21044">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ترامپ به فاکس نیوز:
برخی از مقامات ایرانی مانند موش‌ پنهان شده‌اند.</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SBoxxx/21044" target="_blank">📅 17:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21043">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">این هم پاسخ ترامپ به چموشی سعودی های مفلوک در نپیوستن به پیمان ابراهیم و در عوض دست نیاز پیش فاکستان ورشکسته و عثمانی مقروض دراز کردن!</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/21043" target="_blank">📅 17:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21042">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ترامپ به فاکس نیوز گفت:   گزینه‌های فعلی که در حال بررسی هستند، عبارتند از: نابودی #إيران، یا اجازه دادن به فروپاشی اقتصادی آن، یا رسیدن به یک توافق.</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/21042" target="_blank">📅 17:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21041">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ترامپ به فاکس نیوز گفت:   گزینه‌های فعلی که در حال بررسی هستند، عبارتند از: نابودی #إيران، یا اجازه دادن به فروپاشی اقتصادی آن، یا رسیدن به یک توافق.</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/21041" target="_blank">📅 17:12 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21040">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ترامپ به فاکس نیوز گفت:
گزینه‌های فعلی که در حال بررسی هستند، عبارتند از: نابودی
#إيران
، یا اجازه دادن به فروپاشی اقتصادی آن، یا رسیدن به یک توافق.</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/21040" target="_blank">📅 17:12 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21039">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">رویترز:  در این ماه، ایران فرماندهان سپاه پاسداران انقلاب اسلامی، مشاوران نظامی و تجهیزات مربوط به موشک‌ها و پهپادها را به یمن تحت کنترل حوثی‌ها منتقل کرد.  یک پرواز شرکت ماهان ایر در تاریخ ۱۳ جولای از تهران به سمت یمن پرواز کرد و بین ۱۰ تا ۲۱ نفر از پرسنل…</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/21039" target="_blank">📅 17:05 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21038">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">پوتین:   رهبران اروپایی در روز های گذشته به صورت آشکار اعلام کردند در حال آماده‌سازی برای جنگ قریب‌الوقوع با روسیه هستند.</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/21038" target="_blank">📅 17:00 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21037">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">قرارگاه مرکزی حضرت خاتم‌الانبیا:
براساس اطلاعات دریافتی، آمریکای جنایتکار .... بار دیگر تصمیم گرفته است با چراغ سبز برخی کشورهای منطقه، در نشست مشترکی در یکی از کشورهای اروپایی، اقداماتی علیه ایران اسلامی را از سر بگیرد.
هشدار می‌دهیم چنانچه آمریکا علیه ایران اسلامی خطایی مرتکب شود، تمامی مراکز استقراری و منافع آن کشور در منطقه، بدون هیچ‌گونه محدودیت و ملاحظه‌ای، هدف حملات مستمر، موثر و دردناک قرار خواهد گرفت.
اخطار می‌دهیم چنانچه کشورهای منطقه با تداوم سیاست دوگانه در قبال جمهوری اسلامی ایران، با تجاوز شیطان بزرگ به ایرانِ اسلامی و مقتدر همسو شوند، همگی در این شرارت شریک تلقی شده و دیگر نمی‌توانند از نیروهای مسلح قدرتمند ایران انتظار خویشتنداری یا نجابت را داشته باشند.</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/21037" target="_blank">📅 14:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21036">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">فایننشال تایمز:   عربستان از برنامه تحت رهبری چین که بخشی از تلاش‌های پکن برای ایجاد یک نظام پرداخت فرامرزی جایگزین دلار است، خارج شد</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/21036" target="_blank">📅 14:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21035">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">این هم پاسخ ترامپ به چموشی سعودی های مفلوک در نپیوستن به پیمان ابراهیم و در عوض دست نیاز پیش فاکستان ورشکسته و عثمانی مقروض دراز کردن!</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/21035" target="_blank">📅 14:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21034">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">قالیباف:  جنگ بعدی ناوهای آمریکایی را در هر نقطه اقیانوس هند باشند هدف قرار می‌دهیم!</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/21034" target="_blank">📅 13:07 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21033">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">این تناقض را نمی‌فهمم:   از یک‌سو ناامنی در کشور تا حدی است که رهبر حتی نمی‌تواند یک پیام ویدیویی منتشر کند،   و از سوی دیگر امنیت در نیویورک آنقدر تأمین است که رئیس‌جمهور و مقامات وزارت امور خارجه بی‌دغدغه در خیابان‌های منهتن قدم بزنند.   آمریکا دشمن خونی…</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/21033" target="_blank">📅 12:56 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21032">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRaefipourFans</strong></div>
<div class="tg-text">این تناقض را نمی‌فهمم:
از یک‌سو ناامنی در کشور تا حدی است که رهبر حتی نمی‌تواند یک پیام ویدیویی منتشر کند،
و از سوی دیگر امنیت در نیویورک آنقدر تأمین است که رئیس‌جمهور و مقامات وزارت امور خارجه بی‌دغدغه در خیابان‌های منهتن قدم بزنند.
آمریکا دشمن خونی است، اما با بعضی‌ها‌ کم‌تر؟
✍️
پسر سوم‌ خانواده تیبو
@raefipourfans</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/21032" target="_blank">📅 12:56 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21031">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">قالیباف
:
جنگ بعدی ناوهای آمریکایی را در هر نقطه اقیانوس هند باشند هدف قرار می‌دهیم!</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/21031" target="_blank">📅 12:47 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21030">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKVhCkjjuBd3itivWyWiWgpO4dZYr8rNitZ72RxJ23DG3whuSFUIRb3TjF7ULLJHmSTM9me2PAOaSSofm98EVUXW_f5NIZSE9-FWLT-tQpEcTpalrGTrnf0CjNQDR-KgMHjnQGlgeDQ5xh1srAPGdfQbWMvDtBTB0dZY0QR4UXn2XvoT4Qjr8PWaPkAclSpWvahuLeJibca0BPIJwd63XqlyHhxORGKqo1glkLI-HLS8HFTuIUhsiQxgAXah-LLtw0GJPuKhqw5Tc8L-3X3Xc3sj5Mjp5kP3Bz1yuwdaT2YGYIo2c3tFfKIofAeO1JRO7snAmCYOnbM6CYAg9UXRDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve  نمایه FVC نشانگر نزدیک شدن طلا به محدوده قیمت منصفانه است و لذا از حالت حباب منفی ارزشگذاری فاصله گرفته است (به دلیل رشد سنگین از پریشب) هر چند هنوز تا تشکیل حباب مثبت و بیش خرید بودن فاصله زیادی دارد.  پس بهترین استراتژی برای امروز:  خرید…</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/21030" target="_blank">📅 11:07 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21029">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">کانال 14 اسرائیل:
آمریکا گزینه‌های حمله احتمالی به یمن را بررسی می‌کند</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/21029" target="_blank">📅 11:03 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21028">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZiyEQI7lCsuZwH4yMLZKA93ZsT6Nf89YbcElgtnvxksTkpD6kkGzGG6v4njlgsBmGMW8wELrdsSzLC39Jqu1U74N2mgdBtFUq7wB6lP7a4ztz-3kKFmKmGO1nA9EYcrexuczItND6VpK3R_6wP7Kt-xL6JPTfFOxFP6DPTtNhO_LbeHKdq8OCYX_OUYFWce3yiWNIGCYWFq7JPmYIJMlUrDrv0IyP-UjYIBfhwn0RVs_fhbYmc3r7N7rhYk6CvBGdTpG1HyaKOauN9CIN5qxkbgE4iFIbgo9-i9477cz9XHM-xnk-DfFjtyiwtOGL1oQb-BtGoEkC6l4dAVLgFhlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک حمله پهپادی گسترده در طول شب به مسکو و منطقه مسکو، در روز پایانی انتخابات پارلمانی روسیه، انجام شد.  یکی از برجسته‌ترین اهداف، پالایشگاه نفت مسکو در کاپوتنیا بود که صبح امروز آتش سوزی بزرگی در آن مشاهده می‌شود.  ظرفیت پردازش این پالایشگاه حدود ۱۲ میلیون…</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/21028" target="_blank">📅 10:26 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21027">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">یک حمله پهپادی گسترده در طول شب به مسکو و منطقه مسکو، در روز پایانی انتخابات پارلمانی روسیه، انجام شد.
یکی از برجسته‌ترین اهداف، پالایشگاه نفت مسکو در کاپوتنیا بود که صبح امروز آتش سوزی بزرگی در آن مشاهده می‌شود.
ظرفیت پردازش این پالایشگاه حدود ۱۲ میلیون تن نفت در سال است.
آخرین بار در ۱۶ و ۱۸ ژوئن به شدت مورد حمله قرار گرفت، زمانی که هر دو واحد اصلی پردازش نفت خام آن آسیب دیدند و پالایشگاه مجبور به تعطیلی شد.
تا ماه اوت، گزارش شده بود که توانسته بود تنها با حدود یک‌سوم ظرفیت خود مجدداً راه‌اندازی شود.
اکنون دوباره مورد حمله قرار گرفته است.</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/21027" target="_blank">📅 09:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21026">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4607a666c6.mp4?token=lTAoDikxlc-ebbTrsWMAq0OzVvPLBCyuyDpkSoYQx6vMe-J7YB_C8RpLy8o_SYNcv8N5vjIZ5FIUWuqC-lDhmgUklb8-ZkQw8GGOux5z63XzDpKl00Wu0DW9tNNfzZOwi02aHxDhJeOA8atuSfg3RsAFRuuydwkS68cVhkbTsjwK1gtbJ5HQuqZSb2sYJeiyasJysds8mkr7KZ7FQVD3NA1hCdWjlbIqXuKLt5KXVwqi31Pj_9emMuXrjP-7dsL4vLP3krE3jzSV_0UHgmtTSyKgUpRXTYgIP0yLdpwMlAV9nJhEuQJHIO9AUYPoZS7UEO1BXk180zomwtqAZWOAIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4607a666c6.mp4?token=lTAoDikxlc-ebbTrsWMAq0OzVvPLBCyuyDpkSoYQx6vMe-J7YB_C8RpLy8o_SYNcv8N5vjIZ5FIUWuqC-lDhmgUklb8-ZkQw8GGOux5z63XzDpKl00Wu0DW9tNNfzZOwi02aHxDhJeOA8atuSfg3RsAFRuuydwkS68cVhkbTsjwK1gtbJ5HQuqZSb2sYJeiyasJysds8mkr7KZ7FQVD3NA1hCdWjlbIqXuKLt5KXVwqi31Pj_9emMuXrjP-7dsL4vLP3krE3jzSV_0UHgmtTSyKgUpRXTYgIP0yLdpwMlAV9nJhEuQJHIO9AUYPoZS7UEO1BXk180zomwtqAZWOAIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت امروز من در بازارهای مالی
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/21026" target="_blank">📅 09:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21025">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d8265c9ad.mp4?token=HdwGfNgQinghl594a3PIZTceFfnXRwbtC0v5rtWn6LULb3d3CERBorh5FrfT8CIofsjCKSkau9Qigoxb4bMKxPvJLhv91A-PHXLVcQXjtuqTkyJL_t_u73NEphrcvC7CbPZigOlL1vv8Eq1cenPSieC2rWrIvwzrUZ_Z-EkZOn1nDe7F7NhLcsYgFhLcXNSkAk1pDA9mgfHLIX05eD_LWG5LuIBjgtovc1gyKWImHEtIOL0vQqliBhQLTCujClsZFyY_xkLwH2TzjjWX3c_NbhjWulvjB3S-8Gy7ujarA4Q-0W84-HtNbfmGdwe_WERVa8qTXJ3sqIE8y_TKH5ts5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d8265c9ad.mp4?token=HdwGfNgQinghl594a3PIZTceFfnXRwbtC0v5rtWn6LULb3d3CERBorh5FrfT8CIofsjCKSkau9Qigoxb4bMKxPvJLhv91A-PHXLVcQXjtuqTkyJL_t_u73NEphrcvC7CbPZigOlL1vv8Eq1cenPSieC2rWrIvwzrUZ_Z-EkZOn1nDe7F7NhLcsYgFhLcXNSkAk1pDA9mgfHLIX05eD_LWG5LuIBjgtovc1gyKWImHEtIOL0vQqliBhQLTCujClsZFyY_xkLwH2TzjjWX3c_NbhjWulvjB3S-8Gy7ujarA4Q-0W84-HtNbfmGdwe_WERVa8qTXJ3sqIE8y_TKH5ts5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از حمله موشکی دیروز حوثی ها به فرودگاه ریاض</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/21025" target="_blank">📅 09:05 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21024">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ecd762d60c.mp4?token=bMnlajeeD1EGhCk6de1636Z1IMQ9j0naCtQ0bglMHP_eUax8akDN5inWDXMoi-jkbSQn4GNSrrwqtTVsfIP64cNLNWAeY_rEgzO4oj4WOgJ8iBXVae28iXASliD3-u1n10yHSIuG6zJO4L5-t4mOxzlNALxgTF1C7bf2cxbA9yq3EAzzrqt1oXTx5OLX6YOSMu_sHUV6Y8YJLxinKOetgiuM12r27FNl3KarP8dpFRGmobmsLxBNUF3709BknRlxhTG06u-Bt25XIX3q1R7sxjv4vPp0IPu_KFLquEekaO_362e2j4PupzzuPI4ZDhcNgbb-EtL5B0InVmMQ2AgHdw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ecd762d60c.mp4?token=bMnlajeeD1EGhCk6de1636Z1IMQ9j0naCtQ0bglMHP_eUax8akDN5inWDXMoi-jkbSQn4GNSrrwqtTVsfIP64cNLNWAeY_rEgzO4oj4WOgJ8iBXVae28iXASliD3-u1n10yHSIuG6zJO4L5-t4mOxzlNALxgTF1C7bf2cxbA9yq3EAzzrqt1oXTx5OLX6YOSMu_sHUV6Y8YJLxinKOetgiuM12r27FNl3KarP8dpFRGmobmsLxBNUF3709BknRlxhTG06u-Bt25XIX3q1R7sxjv4vPp0IPu_KFLquEekaO_362e2j4PupzzuPI4ZDhcNgbb-EtL5B0InVmMQ2AgHdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/21024" target="_blank">📅 08:33 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21022">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ترامپ می‌گوید باسن ملانیا باعث «نجات» هر دوی آن‌ها در پله‌برقی مقر سازمان ملل شد.</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/21022" target="_blank">📅 08:32 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21020">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">وزارت خارجه آمریکا به تمام شهروندان آمریکایی اعلام کرد که سفر هایشان به خاورمیانه را فوراً لغو کنند.</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/21020" target="_blank">📅 02:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21019">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">محسن رضایی:   محل تپه علی طاهر پیش از حمله تخلیه شده بود و عملیات دشمن شکست خورد</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/21019" target="_blank">📅 00:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21018">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">محسن رضایی، دبیر شورای عالی امنیت ملی ایران، از آزمایش یک موشک ضدکشتی که به 80 گلوله تقسیم می‌شود، خبر داد.   به گفته ایشان، این آزمایش بر روی یک ناو هواپیمابر آمریکایی انجام شد و با توفیق الهی به نتیجه رسید.</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/21018" target="_blank">📅 00:57 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21017">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">محسن رضایی، دبیر شورای عالی امنیت ملی ایران، از آزمایش یک موشک ضدکشتی که به 80 گلوله تقسیم می‌شود، خبر داد.
به گفته ایشان، این آزمایش بر روی یک ناو هواپیمابر آمریکایی انجام شد و با توفیق الهی به نتیجه رسید.</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/21017" target="_blank">📅 00:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21016">
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c95cb0fd.mp4?token=OWdBuM-YV3gvKWGaT4-j6v2GmHQpZmJ_tKfhGCGJaBVH8szH_Re6esf99ReJ-kTrXHnwrsGIZH0SRXWaNGzbkdZs1jv8koxbGmXlukCUhLKPNFRDkAHbrVFu3zxIBU0Bk_08LhZ8kHS2PznF6p5gW6g9gWLW1e3jz7MQ6pZWl8a6FCeiGOXwkdJK7G-Aw35iJ_xNzknM16bXkCX2DiHbBnV_rMjoGCiCOz9bY5unjARC7tySigYX6NG6Ibs6n9JH-tR-4xfCOQGMUbI62x_rwmLgpCnnZHNK7bp1oDxO9hh1R5yxgfIcigekridNqVxtoOjpprGI4Qq-sP_IDgXrqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c95cb0fd.mp4?token=OWdBuM-YV3gvKWGaT4-j6v2GmHQpZmJ_tKfhGCGJaBVH8szH_Re6esf99ReJ-kTrXHnwrsGIZH0SRXWaNGzbkdZs1jv8koxbGmXlukCUhLKPNFRDkAHbrVFu3zxIBU0Bk_08LhZ8kHS2PznF6p5gW6g9gWLW1e3jz7MQ6pZWl8a6FCeiGOXwkdJK7G-Aw35iJ_xNzknM16bXkCX2DiHbBnV_rMjoGCiCOz9bY5unjARC7tySigYX6NG6Ibs6n9JH-tR-4xfCOQGMUbI62x_rwmLgpCnnZHNK7bp1oDxO9hh1R5yxgfIcigekridNqVxtoOjpprGI4Qq-sP_IDgXrqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر خارجه ترکیه گفته که ترکیه می تواند نیازهای نظامی سعودی را برطرف کند!  یعنی در این شرایط که عربستان بشدت به نیروی نظامی نیاز دارد هم ترکیه دست از بازاریابی برای سلاح های ساخت خودش دست برنمیدارد!</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/21015" target="_blank">📅 00:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21014">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bI-IxUKhp6xuJIsZvfCcmmlAXTqO-j-qrcZd8c2hNDzMAzOe7l9gFbLPp-1j9z5qPp-SEfb3nXUi2MUcCbuUaJbn7Zz7chxX8bUQ25hjENAA46o9n22S57MiNjk-Xx3PX2xnuIRuz-Nmzdl_h9tBc35jb9TeYHRaau1ZnAk7yaHt03T1JGj9OCbW4zyovRPVW1hgUbIMiV6WCQbwEU9fymZP-kIh3ECF1yO-5ycDWHYXPvvkFlUgrxIidMW8Mlz7-jFfBs8VkndNgVNHhVXJaaliLMXk0r8oJ7P6x-KW4EMoQWpx83uvpW1lpkyMs1tlJnIHDrLSOIY75dATLEwU-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضو دفتر سیاسی انصارالله:   این پیام به ترکیه و پاکستان ارسال شد که به خودتان احترام بگذارید؛ اگر از عربستان سعودی حمایت کنید، ما به شما حمله خواهیم کرد و شما را تنبیه خواهیم کرد، و دست‌های ما از فولاد خواهد بود</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/21014" target="_blank">📅 00:23 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21013">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpwdt3SPoJOR1ACWnUCR_PKIxGJtgXD7TXasIfx267uUQ97lFnZ0kwKZxqYDRDTFq4RXQ7m1VJRJSGiPrRR1iqd0TRyTTGTvS6YkM6X3uk0JnrnbNIHm_dWd-GJg0n9hl_6xDn0AOtJMpara-zDhLDOkvQG9VKFdnqc0TeN87lc69E8mmeavA074f3vDO5VhNd9KhY3-7kqWdACs5Cm0rq7NX92NyXF2fqDR8EGQQsmrNR6S6vXHyhT6eveP79HESyAOALW_Z3zr2EkDbaRbD7r1r5BlbQharO-PR4lm8oy6UYE4MCvEc2Hqr9awxHnoteAafXqGCx7gmNUym9qo6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی:   خواهان پایان جنگ میان عربستان سعودی و یمن هستیم و معتقدم یمنی‌ها نیز خواهان دستیابی به توافقی با عربستان هستند</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/21013" target="_blank">📅 00:17 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21012">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">عضو دفتر سیاسی انصارالله:
این پیام به ترکیه و پاکستان ارسال شد که به خودتان احترام بگذارید؛ اگر از عربستان سعودی حمایت کنید، ما به شما حمله خواهیم کرد و شما را تنبیه خواهیم کرد، و دست‌های ما از فولاد خواهد بود</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/21012" target="_blank">📅 00:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21011">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">صداى انفجار در تنگه هرمز شنيده شد
گزارش‌ها حاکی از شلیک موشک‌های کروز ضد کشتی به سمت شناورهای متخلف در تنگه هرمز هستند.</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/21011" target="_blank">📅 22:08 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21010">
<div class="tg-post-header">📌 پیام #9</div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ممکن است برویم یک نایت کلاب اما آنجا شربت بیدمشک سفارش بدهیم !</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/21009" target="_blank">📅 21:48 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21008">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">محسن رضایی :
دکترین هسته‌ای ایران تغییر نکرده، اما خروج از NPT ممکن است</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/21008" target="_blank">📅 21:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21007">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cdfeosxiLE5llyh921bGaKAzOSiqO_MA8nc_mEbg5APlhBnpo0w70QcduqOuVGXakCIRR8q3Ci_SGegJtuE5Zb1yBiwnpiNiNlmtydZoqdAPniaD_mO9Ss_YIfFV4B1cyMDDLs8rn6AY_C_CNbsx3R1lu5F3F8eC5TFBmHkpJefbyrdYDpEtIHmB3jPNEFk0ghVfhKJKATWrXoBuY3L01UoOCAGg2IF34TTuV-YmeGz7pHdTmNkFv5KVq1NFchBv-AFOE94hFEhXQF-eiAGzIK4E1LWxDHHHZyii2EqKeuF5QhD1PIyKWstWMwUe-KsLju_VrOLvlsHqFJKl1S_20w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب امروز و بعد از ۹ ماه تارگت ۲۴۰ هزار تومانی دلار محقق شد.  بعید نیست مدتی رنج بشود.</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SBoxxx/21007" target="_blank">📅 20:29 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21006">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ترامپ می‌گوید توافق با دانمارک، «کنترل دائمی» ایالات متحده را بر امنیت گرینلند تضمین می‌کند  ترامپ می‌گوید توافق گرینلند، رقیبان ایالات متحده را از ایجاد پایگاه‌های نظامی در آنجا منع می‌کند</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/21006" target="_blank">📅 20:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21005">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">محسن رضایی:   خواهان پایان جنگ میان عربستان سعودی و یمن هستیم و معتقدم یمنی‌ها نیز خواهان دستیابی به توافقی با عربستان هستند</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/21005" target="_blank">📅 19:38 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21004">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">📌
جنگ ایران؛ رشد و توزیع ثروت و درآمد مصرف‌کننده آمریکایی و چالش فدرال رزرو  با وجود فشار تورمی ناشی از انرژی، درآمد واقعی و ثروت خانوارهای آمریکایی نسبت به سال گذشته افزایش یافته، اما بخش بزرگی از رشد ثروت از افزایش ارزش سهام و املاک ناشی شده است.  این نابرابری،…</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/21004" target="_blank">📅 19:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21003">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DRcnzozkUAjb0odh_5TL5GFurSqqZ1zoq3AWqW4JySycb-LsZeVKo_I-7KEqid8m1-a44s47LczVRd-L0u3ax2qybp3E-NDJXRAgMj8XleTNDbEQG3nNC4o9svqx0VqJhsRdWKVekP2zYZv_7qhqD_D6QAN20oUczvSp2d1GnJfC46cCtiyrVVCUJOJohkt55g7TsZFqaWCBj0YjYMj0VyOAiVQC6DQX9e9GvO43rpAjuSDDEiWeRba_aDMuirJ8cuXIY4eUNXy942EKYTd0NiDRYF7VXTZrt9Zvm62VeBg2oDA0e5TyshDXJFdKPgeqo9SYpEbAlcqtHet-EdxTHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/21003" target="_blank">📅 19:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21002">
<div class="tg-post-header">📌 پیام #1</div>
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
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SBoxxx/21002" target="_blank">📅 19:12 · 28 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
