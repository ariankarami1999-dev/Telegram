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
<img src="https://cdn4.telesco.pe/file/P51VLA4qgQyjtRxaVuHC1fmxf2ysBx0m8tIDEcC9uGD0Q_-4blU9TISMfK7KT54DfBTshgea86UDJlh0RNEdZw8WAz0KS7ibSc7MJwiWhpjnm8mQQp7whHO5AGRvX7MlrV_UEi76NoxO7P-DGFF3PjGSu2i3-C-j5gWCyybGBkYZU2YBP_VpZzrvgDYSkwSbfkSK27OU03COijcI-9asCbFtF26Jp64N5uakODyptAwBzX52wHm5iVDfkaLdzWuu230H6IOeIdxh5CqlrLVETzjYcIhR4szb3WRSrQBlPDmssYL8GH_Bw3FfJP1L1EmxZ2ZLWwSOYtDGnOa5pgQSkQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 959K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-27 16:01:22</div>
<hr>

<div class="tg-post" id="msg-148029">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p3k2fXxIXizEG7trasyEF5Qt5zr6WRIS4aWVBOeX58cviu7ExjBddEoZoTduFJdUruHPxgExbdJGfO2EbZ7KQrQCD6zLpurlAd-jIJYAK8ru2Q2K3GBmsAgShuHKiXzPNWqSthDlEp1Nrr8FBZjykHT96fIWfA76uZbO-z5dcn98DPXivEQsszWCqsr2PGgYmET2am5SFIMriEJ1CjdOXcd7oKBCIW0YVEO0GbRqzM50YCIn0YPjjuwgw9NrXSWfn0KSy4lSulWQhifvuHlF9Xy102R52sKZ-wVgh5w8PxA8dfTvL62ZNiwBjf8wLetfbdb3R_E1Z1Qe6GP4vqVXgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oZt2S9Eu_T3WuH5Ul0yOpRA3YXeEBeNAVk3uanJRlimd-bt3_yzK7JR9qONj5Zgqzuk9MM16HRIAmiIieYe2E8xC7LvLRSIeLxY6_D6_xfmvAxqf9DuKhZ3LSinYaDv3rLDlUtvvk0Gx35NjhXophfwRVb8hC4kA6zHnb6Al53j1kPolNVXEYcA54s6ehFkieoAuyqzlcgq3x0wUWM5gXx8sTdaV8hfagzEkcVocqpAX144cLjMqv85DSvWZc5HGNMKNLJIzDISmnyDaauEs6HY4VVLZDAcqDgOJP8VtrCxl9CVtiBC8f9kaT2qvARwvwJAPwRVi3879u_CEeMREKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cA8iq5ysXo2l9PtQQ9GPBdIehy3Eh61VxoYayNFBd38fzPmO00TC9_fdmwXWqe3xtS2NPhWG76CmFOwBOtNr7VJnRETLvrw22tzO3XDO1vOHpR8whHbKAE2GvGHMq0E9jmUPnrizxuU8pzKuc49UdGM6U8Bpbfp6tfNae3vKHfJ9YUsmAXRYUluzNQPprgbElisO3ItJZoeYlCtyDy3rhBX5bsEN9SkezJQ4Kd47YQk3aFLIdGxTsVGhYKIVytMtita1vQv3_VFOeUMweROvZKWsou98Dremg9QGIzoXnCbkEolYjfkDk7GS_5O5l0JjLRjbVkSblBmbukfw0fHQag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
انفجارهای متوالی در نزدیکی یکی از انبارهای مهمات در حومه شهر دیرالزور در سوریه رخ داد و آمبولانس‌ها به محل اعزام شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 11 · <a href="https://t.me/alonews/148029" target="_blank">📅 16:00 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148028">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
مکرون: فرانسه در چند هفته گذشته، هدف حملات ترکیبی روسیه قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/alonews/148028" target="_blank">📅 15:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148027">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGUMlq54iyZouXtf9N4e2ZKQH3CakMNvz1_HENCNR27IdsDqCejz2HSettOmT_QFo04IieHm91PfbAZhAtumBa9LyyzinY70UWwTHCRnR7lzFQnStrt7VVByUp4WnkCRf-QA3Jl4-FqUvXob5U_RPSEN3x0_Ry74T9QGFHE99eVsvXomQgV-qcgWu43TW5Ymfol9lWICLZRrvLs3OtSqjNSxSgGK75RQFVE47ZusuaqW992AktGb7WT44bmMrzECALhIv7KUF57dBwgm_wogm_rAH4fEIZ-rLJvXHVHPui6VuU1y0PepnBVUPbaGMBSM737PFMvp4K8s2mBoyqYIyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
بلومبرگ: شرکت آرامکوی عربستان سعودی به پالایشگاه‌های نفت اروپا اطلاع داد ماه آینده نیز نفت دریافت نخواهند کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/148027" target="_blank">📅 15:43 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148026">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
خبرگزاری فرانسه به نقل از یک منبع اگاه: پزشکیان، رئیس جمهور ایران به نیویورک سفر خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/148026" target="_blank">📅 15:37 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148025">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
مرتس، صدراعظم آلمان: دوران دوستی بی‌قیدوشرط اروپا و آمریکا به پایان رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/148025" target="_blank">📅 15:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148024">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
وزیر آموزش و پرورش: مدارس امسال حضوری است
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/148024" target="_blank">📅 15:20 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148023">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dn8PdlJ2TWiJFRWWAJCoMn-ipQlG028UKCwD6_vpb4H9kfcU6io_AVfoiSQk-XDH6IsxJqa3ni7LoU2QdyvtQNeXHmk2uQ_W8QJTaKiH3XeRBDzu4LBqz9GFpZ7z6UliLRbsFhFWjPrAKIOk8ogWJn-3uMBlieOPWAmojq9CtOCE8-VwnahW1gLC6ojYUGLD9CBqY4sK1Q4IOAc6V0Zk-Ic4xYIgkvf3odH8qdk89qMwJnJZPhDvPdnta3WCP7IoL3dhsHedIM51qvp9ShWwgulFFtCfQEsg6HJ3rjyJLH4ahZcufupNiJHpN5gaYXnwISii7i6xc9jLeO9N_y9opg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک هواپیمای باری مدل "بوئینگ 767" که از جیبوتی می‌آید، در فرودگاه بین‌المللی صنعا فرود آمد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/148023" target="_blank">📅 15:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148022">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
دراپ سایت: تحریم‌های جدید هوایی ترامپ زنجیره تأمین پزشکی ایران را تهدید می‌کند
🔴
اثرات تحریم‌ها بار دیگر به آسیب‌پذیرترین افراد در ایران لطمه خواهد زد
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/148022" target="_blank">📅 14:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148021">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2706380824.mp4?token=Y7xrwOSXXa1rvvUAEgZre1w3Qct_Jc2y-y5WK7fBP5a6hOviUrj7myEddsu9ummBtXbdfZreiQiNS0sWHl0neycrHwpyQBYKLvJlo8zLZ2JskT_XSyxBkqcZVuajDsbgIgtJd1QxveQ5LqsP8GhiI6Ql2IiI5aIjJLRrz-cgj12jUc5AleT-v3-KnX3rDeLZeoWVEM5iMexmLFYfx0oJDyr0dp97-Mn2vkQLysukAQQIicWkf_GfxfDrwZOO6BgBnrxfDvvuPDcLczp_ZsvlobvVDJC08e1UkzrcanzoytivovQS2q_HGDWAcZpZ2yktJaqDJIf8f7268b9vwJdS2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2706380824.mp4?token=Y7xrwOSXXa1rvvUAEgZre1w3Qct_Jc2y-y5WK7fBP5a6hOviUrj7myEddsu9ummBtXbdfZreiQiNS0sWHl0neycrHwpyQBYKLvJlo8zLZ2JskT_XSyxBkqcZVuajDsbgIgtJd1QxveQ5LqsP8GhiI6Ql2IiI5aIjJLRrz-cgj12jUc5AleT-v3-KnX3rDeLZeoWVEM5iMexmLFYfx0oJDyr0dp97-Mn2vkQLysukAQQIicWkf_GfxfDrwZOO6BgBnrxfDvvuPDcLczp_ZsvlobvVDJC08e1UkzrcanzoytivovQS2q_HGDWAcZpZ2yktJaqDJIf8f7268b9vwJdS2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رژه عروس و داماد های جانفدا تو رزمایش امروز
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/148021" target="_blank">📅 14:51 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148020">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
بلومبرگ:دو محموله گاز طبیعی مایع قطر از تنگه هرمز در هفته گذشته عبور کردند و یک کشتی دیگر نیز در حال انتقال بار از یک کشتی به کشتی دیگر در نزدیکی سواحل عمان بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/148020" target="_blank">📅 14:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148019">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
پزشکیان: با صرفه‌جویی جانفدایان در مصرف بنزین، گاز و برق، می‌توان از توقف چرخ‌های کارخانه‌ها جلوگیری و مصرف انرژی را کنترل کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/148019" target="_blank">📅 14:27 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148018">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
فایننشال تایمز: پاکستان بر اساس توافق امنیتی مجبور به دفاع از عربستان خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/148018" target="_blank">📅 14:23 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148017">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUcHo7EHjpibhKfZbjY4qrSlhFSinNN97woKueG0Tp_ppI0uy8OkeMBr4VmPcbBCWfFjBnOdkcxReCSbDKXXQ4sXHb4hhgsE6c3kzZVpjX_gz8UjZORUX-DySajFbphellRh6wF_wWcml-RZBKFhXL9oO9k_sAEfP3BYmAGn9U0ly4-KWiUfgpBB3keZrbXO-X0KOI4p86_AomctEe2i0YNmvnUDFE8qWsiNB1jNXKPcvCJVpIb9Ezl1AQAQh8p-tlIoTt2PXw6JrRcRXPzDzK2QkI7OtGyu0HZhnZrmEccXbyQbsEAV3_oI_3tynEzMrGT88ZBfkzvq059IiYOpxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خطیب جمعۀ تهران: تجمعات شبانه به دستور خدا انجام شده و تا هروقت خدا بخواد ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/148017" target="_blank">📅 14:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148016">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
این تاریخ بیت کوین میاد رو 200هزار دلار
از این تاریخ پرواز میکنه تا 200هزارتا
👇
https://t.me/+4jOgodAq96dmYzY0
https://t.me/+4jOgodAq96dmYzY0</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/148016" target="_blank">📅 14:13 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148015">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی: با وتو شدن قطعنامه ضدایرانی توسط چین و روسیه، آمریکا بازم شکست دیگه ای خورد
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/148015" target="_blank">📅 14:11 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148014">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mFUhikIqHA4CQz1obZPZIm2XokzfVWrSLdMylp-YRDUXDiwbXuEC5h5Ebil9SSALCBosWTjku1BH3_uf28H3CcUP2AHbCE6q-wm-0Xa9SawcVX-J3_DQDq4pacTJgfxtYdTrzGnjqs9DUoBYjd0ET-ObWnWwLoKPnAjVqZTePI6womf5dU_FHkHqPxCASPXm_X5x8uec4JUSMikq64w2RnWpJ5P4ZmktVEoAL4RsTsegTCd0LxfmGmfemeTTgdycdaPaurJmFxWCBEBlV7UpZO9_MvdojRQADkGibWao-6b_rXJcDSm9blA_SPUsHlXiCGU4-hW9uR9-R1uUnwVBrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفت برنت امروز با قیمت بیش از ۱۰۳ دلار در حال معامله است
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/148014" target="_blank">📅 14:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148011">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/387a49d38d.mp4?token=fENXpjx9eEeq28GPW_2iiSJesH5eE_nOBkgeNYPUyxswv2P1MC5WWDIB8PlnZjuSYBYwn1g2BJkD_EVZNaHeILnwPjUu8bWtbJMJUhLPVjRomByKW9zLF_k7Vj5J7_LUg_tD6onWWxv34qMY-KCG80b1R1GVczGjZIEwAKegQaRrFPL3g5ZzcSJXa6xdUGJ5jXfmszZ7zgG0b6mj6FSgPoQF8MItkPCFdG8ZJLoTuXnFq_oz3X4_WzXqikHfKImt_u1vtjR_S06b-2pc6pUC1WvJ8F47de14pR2KrI0cvq459WXZjk-cpLJz3Z4Aa3Wu_SLGNTxDGz7zJ9jX4sFd6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/387a49d38d.mp4?token=fENXpjx9eEeq28GPW_2iiSJesH5eE_nOBkgeNYPUyxswv2P1MC5WWDIB8PlnZjuSYBYwn1g2BJkD_EVZNaHeILnwPjUu8bWtbJMJUhLPVjRomByKW9zLF_k7Vj5J7_LUg_tD6onWWxv34qMY-KCG80b1R1GVczGjZIEwAKegQaRrFPL3g5ZzcSJXa6xdUGJ5jXfmszZ7zgG0b6mj6FSgPoQF8MItkPCFdG8ZJLoTuXnFq_oz3X4_WzXqikHfKImt_u1vtjR_S06b-2pc6pUC1WvJ8F47de14pR2KrI0cvq459WXZjk-cpLJz3Z4Aa3Wu_SLGNTxDGz7zJ9jX4sFd6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یاشار سلطانی فروشندگان نفت را لو داد!
🔴
از داماد سخنگوی پایداری‌ها بگیر تا خانواده فاسد شمخانی
.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/148011" target="_blank">📅 13:59 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148010">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
منابع داخلی: در صورت جنگ زمینی تمام جان فداها به خط مقدم ارسال میشن
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/148010" target="_blank">📅 13:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148009">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
تصویری از انفجار در یک مسجد پاکستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/148009" target="_blank">📅 13:46 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148008">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXMnhGI13vLBmmAauXPZJYNsy-MoY6HKQHUGMcDU_IXkEQBYr46jAG7vwRnfHAEtupA4Im6r7jYkjAgSE11yApOQzF2JVyQg0_Z8V825ssUHrpef73XQnMn0eL3lVld62dULyowHuCXsJuaAbn64pji-oV3jnFh7eOPlfQN8ZZZ_2q_Zxl2BbsW9w6DR1-Cu9-9UQmJ9po57-KlmpFdWTcr59h_tNs_3zx0TRj9i8rO_q4qlN5-f2NMI_50zbKkaa-JGLhgnhNhBY9_iP_noyK_gAAN1zGxoY4bZNCYwW3tE6zKiNqHgz5S0j6ygunBSEYFmlWQUmyJajnZ606tJKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش اتاق جنگ اسرائیل در مورد تصمیم مهم ترامپ در مورد ایران:
⏳
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/148008" target="_blank">📅 13:42 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148007">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ciOKOj9l5W6XgA11a-zxJUVJB1sjFFJoPSjcWNyqPr8h9Hv8AGmN76snBYkzUUCbFRlpsMH74LbPG3WRcaFfVxdB3z6m3eD37vH1BEBEoklD9j9ZsaSKOxuSvcbqyfu79a0T3Ut5yWoCb2bOIO_Ri7UY-pu0nnMClJzSCp9qLS4EtOluGQFuBuowJNnq9AcjJsV-lSMnftS5ad6-vSdGV5iekx6s6kVlRp8yjnpPzo5AHj_mLbJxEfxJNHviK7Z2PnaDgR0Xqk_KeeKb60fqJwLrhAY7KFjiC3uo7C_wG6_IIXfTQgjE-jINCVYkIMd-ZwUCZS_8wg_1VsL1fnPIjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش لبنان از یک موضع تازه‌تأسیس در دیر میماس عقب‌نشینی کرد؛ این اقدام همزمان با پیشروی نیروهای اسرائیلی به سمت این منطقه و سپس تفتیش خانه‌های اطراف انجام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/148007" target="_blank">📅 13:41 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148006">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
فایننشال تایمز: ونزوئلا ۴ میلیارد دلار ذخایر طلای خود را به آمریکا منتقل می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/148006" target="_blank">📅 13:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148005">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1xpm2_qske70rvGChwXONi7k85lK9YI7F5f4ALfgV3H-O2kFSPWbSEGF_aYLucXAknvXK3f8tFEmBuZmfZBN-jljKXTICkbbsDrzQ1xoLIyt1dcUaoaZEv_GpqGf6c1CrSCJW9-LKU19uR9W0NpvG_WiMhLetxyCFKSc43zcIWwLuJu13R1Zls0o54j45SflkWk3HKknJ2uWnjing-bKLp1u4tqz6LCpTNonhlF8BGjTH33uRipx2IZbDPjbV8aShLDfUT9FkEjAKwH7Pf8cn15P-99a9P_Ta4zY5GezU8fl-QYHccKGgaGTnpkBrsOt1bi0xSShnYiNmj-fS-10A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
غریب‌آبادی: آمریکا نمی‌تواند با خروج از شورای حقوق بشر از زیر بار مسئولیت خود شانه خالی کند
‏
🔴
معاون وزیر خارجه: تاریخ فراموش نخواهد کرد؛ در میناب، مدرسه‌ای به خون ۱۶۸ کودک آغشته شد و در لامرد، زمین ورزشی به کشتارگاه غیرنظامیان بدل گردید.
‏
🔴
اکنون همگان اذعان دارند که وقایع میناب و لامرد، نه یک خطای عملیاتی، بلکه جنایت جنگی آشکاری بود
‏
🔴
آمریکا نمی‌تواند با خروج از شورای حقوق بشر، از زیر بار مسئولیت خود شانه خالی کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/148005" target="_blank">📅 13:27 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148004">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
بانک مرکزی ژاپن روز جمعه نرخ بهره معیار را از ۱.۰ درصد به ۱.۲۵ درصد افزایش داد که بالاترین سطح در ۳۱ سال گذشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/148004" target="_blank">📅 13:22 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148003">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33da215b97.mp4?token=HHUoMj14-PVSaaypF4tlVzA6IbKAz-gwdGwRbktIDy2MhqQctEPu2YsGOmHsOj2hEqU-sfl98BegdLCTQ2U4wS9SC62Yp0tyUTKwta96JrFfG7PGuFt7A0kLs79a7c1xePtgnj9ZtJaIp6EiRW8bMnGyOhym5adoinRWcTA4J434m6NgMcJQRLY7CBii_78TBdOFyeExQan0CcKJERYRxYiNweNg8bPr92-7HTWI8n3hGe4aEVPpDrb3CTYhDfeDJP3zSrH6s9PMsqwJhub7Q7iF-M8ZGFCkvShRSPoOUR_0YW5y6ybuRZOFBhlhzcpxBJQY3bnqQS-lpbyyNRWdKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33da215b97.mp4?token=HHUoMj14-PVSaaypF4tlVzA6IbKAz-gwdGwRbktIDy2MhqQctEPu2YsGOmHsOj2hEqU-sfl98BegdLCTQ2U4wS9SC62Yp0tyUTKwta96JrFfG7PGuFt7A0kLs79a7c1xePtgnj9ZtJaIp6EiRW8bMnGyOhym5adoinRWcTA4J434m6NgMcJQRLY7CBii_78TBdOFyeExQan0CcKJERYRxYiNweNg8bPr92-7HTWI8n3hGe4aEVPpDrb3CTYhDfeDJP3zSrH6s9PMsqwJhub7Q7iF-M8ZGFCkvShRSPoOUR_0YW5y6ybuRZOFBhlhzcpxBJQY3bnqQS-lpbyyNRWdKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصویری از انفجار در یک مسجد پاکستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/148003" target="_blank">📅 13:08 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148002">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
انفجار در مسجدی در پاکستان/ اعلام وضعیت اضطراری و احتمال تلفات
🔴
شبکه‌های خبری پاکستان در گزارشی فوری از وقوع یک انفجار قوی در مسجدی واقع در ایالت خیبرپختونخوا خبر دادند که تعداد زیادی از نمازگزاران زخمی شده و برخی گزارش‌ها از احتمال تلفات انسانی حکایت دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/148002" target="_blank">📅 12:54 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148001">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSyrpVupzrKfRdISVNQNz4xXwG-gPwFFFIdoeuQnGX76T_P5HGAwhb4nKrLk8WTyggr8uUTsk6s76bnWmFvut5RiHR6RWXLQXFyxphRUzKplYcDVg87MUaGG7-cpMdAAUSi0q4fzvRbTu-wNb2JEAgGd9lhvbIJZFSB0Ofoo55vgI-78Z6Xw8KPQQxst8qnBM2LnnxB26b_BWa9gfV1Z54sP5Y4vPohPOEA73YrviemO3WSvCJnnTrEBRCl6zFtad0oblL3PYmmY3bKXuHkMCXjzcWn66EhYbFhV6dgOjmm9NVJe-WMyGBGI0M1xQETt-TPinfi9cew0Ub2b76Ry4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شرکت ورتکسا (Vortexa) متخصص در تحلیل داده های انرژی و ردیابی حمل و نقل دریایی اعلام کرد که از ۱۱ سپتامبر 2026 (۲۰ شهریور 1405) هیچ محموله نفتی از بندر ینبع عربستان سعودی خارج نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/148001" target="_blank">📅 12:36 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148000">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
وزیر دفاع ایتالیا:یک هواپیمای جنگنده ایتالیایی مدل یوروفایتر F-2000 در جریان حمله به یک پایگاه هوایی در شهر طائف عربستان سعودی، شام پنجشنبه، آسیب دید
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/148000" target="_blank">📅 12:31 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147999">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lkxhql6-FJs9TAn1udPEMKPtOtCt2SDkUbM1dsRshN7c9sV_U05NqrpFXZO7EtHou-mpwfX_NPLKM1cOig1MAk1UCi06VpyFNAgkJ45qvu5bYE7V8zu-20WSy5I_udevMYXWcPG5ayNWqH7gkcpRo_YClZRkAzdFtSmNfsDrcXUErK5xrA4koF35In7CqJDrJCJilm8x5Xl0SLra-XCdQ8hGZl2FBAvFrOmOg_HDSVsxmEtytfg9IMkiWvbs1hzKB-fYKhOLD6t1G0BuiSPgYzQEkVaOwKMKN_wqzkIzlRmr0Dl9PD9E4dlzUUiByXTdhfPpu5gJ0BBhpyBq27N0FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در شبکه تروث سوشال به یادداشتی در واشنگتن پست اشاره کرده و نوشته است: بسیار جالب است. حتماً بخوانید! به افشاگری ادامه دهید ای سگ‌های کثیف! وقتی پیدایتان کنیم، بهای سنگینی خواهید پرداخت!
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/147999" target="_blank">📅 12:27 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147998">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
جی‌پی مورگان: بیت‌کوین احتمالا از طلا جلو خواهد زد
‏
🔴
تحلیلگران جی‌پی مورگان در تازه‌ترین گزارش خود اعلام کردند که اگر سرمایه‌گذاران از لاک دفاعی خود در صندوق‌های قابل‌معامله (ETF) رمزارزها خارج شوند، بیت‌کوین فضای بسیار مناسبی برای رشد و پیشی گرفتن از طلا خواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/147998" target="_blank">📅 12:12 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147997">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
روزنامه فایننشال تایمز به نقل از دو منبع آگاه از مذاکرات اخیر منیر با عراقچی:  فرمانده ارتش پاکستان بارها از رهبران ایران برای توقف حملات انصارالله به عربستان و زیرساخت‌های انرژی آن درخواست کمک کرده و تعهدات کشورش به ریاض را بدون تهدید خاصی به آنها یادآوری کرده است.
🔴
ایران می‌گوید این درگیری بین عربستان و یمن است، اما به نظر می‌رسد که تشدید تنش، اوضاع را به نفع ایران تغییر دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/147997" target="_blank">📅 12:07 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147996">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
رئیس ستاد مشترک ارتش ایالات متحده:
نیروهای آمریکایی باید برای جنگ‌های آینده‌ای که فراتر از زمین و شامل اطراف ماه نیز گسترش می‌یابد، آماده شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/147996" target="_blank">📅 11:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147995">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
قیمت طلا در معاملات روز جمعه بازار جهانی تحت تاثیر کاهش قیمت نفت و تضعیف ارزش دلار اندکی افزایش یافت.
🔴
قیمت هر اونس طلا برای تحویل فوری با ۰.۲ درصد افزایش، به ۴۳۴۶ دلار و ۶۵ سنت رسید. قیمت هر اونس طلا در بازار معاملات آتی آمریکا برای تحویل در ماه دسامبر با حدود ۰.۳ درصد کاهش، به  ۴۳۸۵ دلار و ۷۰ سنت رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/147995" target="_blank">📅 11:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147994">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWnzDCXToEzsxn7S3ZdBfqwX-2yVLbpP5MCbqPE678wd8vdV8LhfpDMAIuXCiaJhv3hFqp760WaD41j2-cmdHMjBJlOyRLPrffEMez44ejs0RIeYh1KUmaJwmzXgNQOtTA35n93aROzMzE0bwSczyfYepCcBH75f-z77iC63_c6GSuTkbzQMplpfBojKgIf4UxER5HUWHd7909JJvaF_wM-6avsZaFx1VuHAjPgnH7aM_rY_DVsXy1diSH5WunyAR-lgw6-183pC7Z896TifTNdIH37TP582Q2QP-kGAer_JREFnqoqLvFBv8atRYtAxdne9UO6VbMd6zOHqNaucPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایران از جدول سرعت اینترنت اسپیدتست ناپدید شد
🔴
ثبت نشدن اطلاعات ایران در نسخه اوت ۲۰۲۶ لزوماً به معنای حذف رسمی کشور از این شاخص نیست
🔴
در حال حاضر توضیح رسمی درباره علت نمایش‌ندادن اطلاعات ایران منتشر نشده و بنابراین نمی‌توان دلیل مشخصی برای این وضعیت اعلام کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/147994" target="_blank">📅 11:49 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147993">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
رویترز: جنگ ایران تقاضا برای ابرنفتکش‌ها را افزایش داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/147993" target="_blank">📅 11:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147992">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
رسانه اسرائیلی از آغاز گفت‌وگوهای محرمانه میان کویت و اسرائیل درباره ایران پس از حملات منتسب به تهران به کشورهای منطقه خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/147992" target="_blank">📅 11:37 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147991">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
هند: از منافع اقتصادی‌مان در برابر تحریم‌های آمریکا علیه روسیه و ایران محافظت می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/147991" target="_blank">📅 11:31 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147990">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
فدراسیون جهانی بدنسازی و پرورش اندام شب گذشته در فدراسیون بدنسازی ایران را تا اطلاع ثانوی تعلیق کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/147990" target="_blank">📅 11:26 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147989">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
تسنیم: در جریان تبادل آتش میان نیروهای امنیتی و چند فرد مسلح در زاهدان، استان سیستان و بلوچستان، چند فرد مسلح کشته و نفر سوم بازداشت شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/147989" target="_blank">📅 11:19 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147988">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
اصابت پرتابه به یک نفتکش در تنگه هرمز
🔴
سازمان عملیات دریایی انگلیس: امروز یک شناور دیگر در آب‌های تنگه هرمز، مورد اصابت یک پرتابه نامشخص قرار گرفته که در آتش می‌سوزد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/147988" target="_blank">📅 11:14 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147987">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
فوری / ایتالیا به تنگه باب‌المندب ناو جنگی اعزام می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/147987" target="_blank">📅 11:09 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147986">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
ترامپ درباره ایران: اقتصادشان در حال حاضر در سطحی است که هرگز پیش از این ندیده‌اند، بدترین اقتصاد تاریخشان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/147986" target="_blank">📅 11:07 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147984">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a8836c88e.mp4?token=pyfA9g0vGci1QFYPrS77VC4Wgxq641DfjL2Dbb2dwanGUSs31nyvm-NCg-H9t-RKIn_WKZn_ikqgt5WZNv9A57XxBdUC7vX88NkyEI27eFqFH3Q0IUolt9bd8_XqUmJ1TzAV7g18VFzwEgihAq45N7X7X-Vfhg7QVTuffeY5eedMsy57xzaxbAcSTYdrvb2o7fdZ0dx40s1yF4JZ0kjjNidsmrTTNTjlc6iIQhmEKtPQU6-hdIY6Y0wt3wLboMQf62Pnb5fLNfYgWMIVxERJOB77z-JAKxCgA7T3tfFhJ2IH-Mg9UJ_9smpp2kkiYTz9DDmN-scTQy6KkVtIITJVSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a8836c88e.mp4?token=pyfA9g0vGci1QFYPrS77VC4Wgxq641DfjL2Dbb2dwanGUSs31nyvm-NCg-H9t-RKIn_WKZn_ikqgt5WZNv9A57XxBdUC7vX88NkyEI27eFqFH3Q0IUolt9bd8_XqUmJ1TzAV7g18VFzwEgihAq45N7X7X-Vfhg7QVTuffeY5eedMsy57xzaxbAcSTYdrvb2o7fdZ0dx40s1yF4JZ0kjjNidsmrTTNTjlc6iIQhmEKtPQU6-hdIY6Y0wt3wLboMQf62Pnb5fLNfYgWMIVxERJOB77z-JAKxCgA7T3tfFhJ2IH-Mg9UJ_9smpp2kkiYTz9DDmN-scTQy6KkVtIITJVSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک پهپاد جاسوسی متعلق به عربستان سعودی بر فراز پایتخت یمن، صنعا، منهدم شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/147984" target="_blank">📅 11:01 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147983">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gCUofUUG4n7Nnp71Fl2__RfFROzUwP0L5-0t-4pnfVOT7y3oR29K9BIfOiNF16leR-8FnmdWVNNF--JPL8nP3aO2kK_gJ45Jw2O7zFQAexj4rMx6mcWaX8LlT8Jrz_lDxsea6RnISzWhVtXliS5iV2IXBzTS9hLvwMqkl0-KRTcHEceMhqnPtvEtKDipao-RPzaL9B7JjhKlwrfcGrhcSRvzO-f0cHYo6XZkG6ImNACTWjWoYGhFV2Ylb7OTmIzMq3xSIDNd8WUB0ZjfXKKZtCM8cOrh9bXbLpkpfr14Zj0OPqA4vnsMciVY2stw5Rq9b6mNZD90f4wUkL5WayRJBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد خوش‌چشم: مطلع میگم، آقا مجتبی تجمعات شبانه رو میبینه
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/alonews/147983" target="_blank">📅 10:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147982">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
الشرق‌الأوسط: لبنان در حال بررسی گسترش «منطقه آزمایشی» برای دربرگرفتن تپه‌های علی طاهر و شهرک‌های اطراف آن است
🔴
همزمان، قرار است با حمایت آمریکا یک پست دیده‌بانی بین‌المللی ایجاد شود و استقرار ارتش لبنان نیز در این مناطق انجام گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/147982" target="_blank">📅 10:49 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147981">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
ترامپ و صدراعظم آلمان درباره تنگه هرمز و دریای سرخ گفت‌و‌گو کردند / برلین:
🔴
این توافق وجود دارد که این دو آبراه باید سریعا بازگشایی شوند
🔴
فریدریش مرتس صدراعظم آلمان و دونالد ترامپ رئیس جمهور آمریکا در تماسی تلفنی درباره جنگ در اوکراین و تحولات تنگه هرمز و دریای سرخ گفت‌وگو کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/147981" target="_blank">📅 10:44 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147980">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
تا ماه بعد وضعیت طلا چجوریه؟</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/147980" target="_blank">📅 10:41 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147979">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZgtWUYrgB27Vtf8RvHbUOBG4K5CK_-lXikOkGfmNjpXF2laEbZY-diY-pMnSimQ7yddoDecOsWe4Z9GoSX96vJ9NUwRxQb0vsbxQlboXBs5906C2k4cFNSqeXzNQIp7b1nP65PqoQg--g7boDY7CN5wbsAV3Y_8IAWg6cJ6c7R1N4jC4R2Jlu3ArbNGqXHpDHNoVX5cUNgvfxLH4NUWwozZCKAkrvhAjfFh33_d2QGUIe2wO-buLoNs51ByvX5bNxrOFfph_t_8XEFoJP13juZJ1USPnvsyoI9LyfrKjiGfxZDxIzbwFLRpc8LoDjHd-qnmDrSMcz6VnNMdwLhBcqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروهای یمنی(حوثی ها)، سلسلة کوه‌های "الأغبرة" را که از نظر استراتژیک اهمیت دارد، در منطقه "المضاربة" واقع در استان "لحج" تصرف کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/147979" target="_blank">📅 10:39 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147978">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
آمریکا رسماً از شورای حقوق بشر سازمان ملل خارج شد!
🔴
وزارت خارجه آمریکا این شورا را متهم کرده که به ترویج آنچه «ادبیات ضد آمریکایی» خوانده می‌شود، می‌پردازد و در برابر رژیم‌هایی که به سرکوب مردم متهم هستند، رویکردی مماشات‌گرانه دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/147978" target="_blank">📅 10:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147977">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
ان‌بی‌سی نیوز به نقل از مقامات رسمی:
پنتاگون در حال بررسی طرحی برای خروج حدود یک سوم نیروهای آمریکایی از اروپا، شامل ۲۵ هزار نیرو، هواپیماها، کشتی‌ها و تسلیحات است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/147977" target="_blank">📅 10:31 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147976">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B2xAo7rRU8XVyCXhqbI4QMTbrIMBFnH1eQPsxyrDPRVjRzfbc3n0dm7K5WjN8a9vLGn1Kp1Q-UHxKWwE6hbSi8rmISdNcTlNbxgFWJWGkJnxhzDefnBo4EhXkI6eESog1567PKf6gq9FpKnVW4VNBj2T99oH11C2cNcdcf7LhQH9VgKzZH8Dps3RWBJQkppLTmId1G95_YVBMuH9-PtxG5QyP2KmrkgWTxDoy1b2S5PjBxKq-ULFOvMYEUGjF2xfgS1UnQQ2vO5E7iZ8EusIo8KTv2uG9SiDnOJmViyEZIlJU-UBTNsHzID94FN2u4owwYT_7cxUodtqJcj6bqA-7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز ۱۸ سپتامبر، روز جهانی خایمالاس
این روز رو به دوست خایمالت تبریک بگو
[تصویر تزئینی هست]
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/147976" target="_blank">📅 10:11 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147973">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E9h-ibu4bO3Q1bTLMGDzA942HbOJdRveZiI7ZYMOUiMMwwl7_dToEzAUjJhlS3v7NzLppfHVkALSsPjEIirp0ALkA9ax0cZxM8JXMLMlNZXXM7WD-oKPocuzjhjuxj04v1ji69zkPpGXZVlmVSeTqujVghJ4qPDMZsUwtEgsdkInU_f6_x8NnoaL44a0ikTzKN_MEm0zIGQQPzst6q5n0UWchMeXplBwI7ShN4UobvYUKze6yvIYJN7q2fJ8Anobhiv-YgQjMUKIIpoRfWHbI1kkQoicFnVQPSwqIWEwwGdVJ4YL89cV-O3MmFGUTB63iZlHa0d7tpWGkA5FwQKTYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I8sJxwn9hJlQudyItEqQ5qV1Fcb9sVh6gyvcU7hk0kWJjWd9uwmVtLAC94n9r3TPrydkeX3RID1RhytHF2HCv1wulHGk54cDnZvT6O1qykTwQ21WmgDUEmgdg7m0CoH12ZFBiZ0VWHyuLNV2ffMQR0O7urxKrq-d0kjXSg_TAcBoAZt2MUFTHewmIN7wkKjRbh7CCNn27N9HUl0IBnnUAvkrxwGMvwmgXXcLAo4Ye0sT9OlXoKCbsCya6AFa-zE598c8S2MoYzbqua0QQjIJEpe_Os0p_RynipAYER_3wWR0DrzQRnOe_moF94chFZ_74fYC2BikWIj6jGzOrPJlYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZdCMt1YGH1-y0QIA4PZYVAy6YTeVXIainXZwxdAG_iIDsSbfLi1LmtXEeOJ2JSqNJGhDB7cb_pIjsrA97Mh-ObP1d6JZs0Bffty_hIuttutFbWc_OdcT_91rFrhNrN8KoHzEog712FAWCSjE9KiUhHTiqVzAFj8C3Jv50uAb7jY8KUkl938lEqLnGlX988Di7AuZg3PNOjfN3S0wv44sTaFZGP3NW7sVe-Hbvk2v7NcFicxvyoRpi2tzgHR-EUDoxCIqJLUq8Lxwe9xYEwSfhRlOuiIGuGhgTlydJvhYvr9FdzDeZ5DruQAYpNa6wLL8iChNaFN5-IHi-Rudac06tg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
انتقال تجهیزات نظامی آمریکا از عراق به اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/147973" target="_blank">📅 10:10 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147972">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
مقام سازمان ملل:جنگ آمریکا و ایران در ماه اول، ۱۵۰ میلیارد دلار به اقتصادهای عربی خسارت زد
🔴
این خسارات معادل حدود ۴ درصد از تولید ناخالص داخلی منطقه است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/147972" target="_blank">📅 10:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147971">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00fa97a9a0.mp4?token=XtdN2LZuASuyjBBBCh9AvAlySQPvdpIPEF1_GjemZKYvfsVHi-iAzyxTyXCW1nHW4Czf2Mhl8kxKLusIp6glxtp1utCV9ed6fsovvkDRsR9NZ0bBaVBSqkiYCsOzkDlqtfFcRY7lp6d2mUbUd8M5k7AJ-S6DDFgpEPNUlBlQrw89DGhiA44QD4nZ3-YwAbtYOhCAU5cAiWGREB6wd0blgS4tiMhmj5EaPD9c0JImWybgSbRn4jsXcKFCSpCV-TK2bLIdCXy3WnvgIXxUAFR-fqSJO5vn01PRCuk2ppoKoJ5qCAgXS2U17M_UXFw9fHrNO2JA8ai4WLxu4ld1gMZVTYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00fa97a9a0.mp4?token=XtdN2LZuASuyjBBBCh9AvAlySQPvdpIPEF1_GjemZKYvfsVHi-iAzyxTyXCW1nHW4Czf2Mhl8kxKLusIp6glxtp1utCV9ed6fsovvkDRsR9NZ0bBaVBSqkiYCsOzkDlqtfFcRY7lp6d2mUbUd8M5k7AJ-S6DDFgpEPNUlBlQrw89DGhiA44QD4nZ3-YwAbtYOhCAU5cAiWGREB6wd0blgS4tiMhmj5EaPD9c0JImWybgSbRn4jsXcKFCSpCV-TK2bLIdCXy3WnvgIXxUAFR-fqSJO5vn01PRCuk2ppoKoJ5qCAgXS2U17M_UXFw9fHrNO2JA8ai4WLxu4ld1gMZVTYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی ارتش پاکستان: تا هر سطحی از عربستان دفاع می‌کنیم
🔴
ژنرال احمد شریف چودری، سخنگوی ارتش پاکستان، گفت اسلام‌آباد در برابر حملات موشکی و پهپادی حوثی‌ها به عربستان سعودی، از این کشور «تا هر سطحی» دفاع خواهد کرد.
🔴
«پاکستان کاملا در کنار پادشاهی عربستان سعودی ایستاده است؛ هم از نظر دیپلماتیک و هم از نظر عملی. ما تا هر سطحی پیش خواهیم رفت.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/147971" target="_blank">📅 09:54 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147970">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
رئیس‌جمهور کره جنوبی، لی جائه میونگ، گفته است که سئول تجهیزات نظامی را به خاورمیانه یا تنگه هرمز اعزام نخواهد کرد، مگر اینکه این اقدام خطر وارد شدن کره جنوبی به جنگ با جمهوری اسلامی را به همراه داشته باشد.
🔴
با این حال، دولت او در حال بررسی امکان گسترش نقش کره جنوبی در حفاظت از کشتیرانی در تنگه هرمز است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/147970" target="_blank">📅 09:48 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147969">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
صداوسیما: هر شب بالای ۶۵ میلیون بیننده داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/147969" target="_blank">📅 09:43 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147968">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
مشاور ارشد ترامپ درباره تلاش برای پایان دادن به جنگ با ایران
🔴
مسعد بولس مشاور ارشد رئیس جمهور آمریکا در امور کشورهای عربی و خاور میانه مدعی شد که دونالد ترامپ برای پایان دادن به جنگ با ایران تلاش می‌کند.
🔴
برآورد رئیس جمهور آمریکا این است که جنگ شعله ور شده در سراسر خاورمیانه به زودی پایان یابد و وی برای تحقق این موضوع تلاش می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/147968" target="_blank">📅 09:38 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147967">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
ادامه روند نزولی قیمت نفت برای سومین روز متوالی
🔴
قیمت طلای سیاه همچنان بالای سطح ۱۰۰ دلار باقی ماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/147967" target="_blank">📅 09:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147966">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
الجزیره: داده‌های اولیه نشان می‌دهد که تنها ۴ کشتی باری در روز پنجشنبه از تنگه هرمز عبور کرده‌اند که نسبت به ۶ کشتی در روز قبل از آن، کاهش یافته و بسیار کمتر از میانگین ثبت‌شده در ده روز گذشته (حدود ۱۶ کشتی) است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/147966" target="_blank">📅 09:16 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147965">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
یک مقام سعودی در قبال تحولات یمن در گفت‌وگو با شبکه ۱۲ تلویزیون اسرائیل: ترکیه و پاکستان هیچ کمکی نکردند، آن‌ها فقط می‌خواهند سلاح بفروشند
🔴
«از سوی پاکستان یا ترکیه چیزی جز اظهارات نرسیده و هیچ همکاری‌ای صورت نگرفته است. آنها فقط می‌خواهند سلاح بفروشند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/147965" target="_blank">📅 09:12 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147964">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
رادیو اروپای آزاد/رادیو آزادی (RFE/RL) گزارش داد دونالد ترامپ ممکن است از فردا قانون «تحریم روسیه و ایران لیندسی گراهام» را امضا کند.
🔴
این لایحه پیش‌تر برای امضای رئیس‌ جمهور به کاخ سفید ارسال شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/alonews/147964" target="_blank">📅 09:08 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147963">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWblYq7-nXV5Fdiwq4HPxdZb11qeqZaLTSlzZXNsNnocwddfpaORiR5BnCuiuQgj77OaUmb8TF0rfnhy5U6PmpDGhmRJnAE4u6iJjXMnHpwEsOzB_TKpceh3HD1fE6FOOsUvwpx35BC9bTFFNR0NUjOuWMx9HQnk0hCltvWLFzbadIscJPl2SDPWKdIsjKyEAOlv19ZT26VfLFtgnMnImFtfK5ZDR4lrX7HC2evadcHX0ocULMgxg2MAKtArwb4r3tzUNCyDx4CWLwbnc3wWl5o6Uh--GunUEvYt43BN2q2T8a-363xCP0GTgkSlFS8fnuNvuVP5W7pafyL2h1r5Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نوسان قیمت نفت برنت در ساعات اخیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/alonews/147963" target="_blank">📅 09:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147962">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
نظرسنجی شبکه فاکس‌نیوز:
اکثریت رای‌دهندگان آمریکایی معتقدند ترامپ استراتژی برای پایان دادن به جنگ با ایران ندارد
🔴
۶۰ درصد نیز اقدام نظامی آمریکا علیه ایران را تصمیمی اشتباه می‌دانند ‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/147962" target="_blank">📅 08:59 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147961">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bff9339b7.mp4?token=u_fIZoOjZq5J646TvSAEb89dOqTSGcgP7RENTSxauqxnpMXVp-xuEwduPyc9LrCgOHwQFtismY6x74BE5dvX0Jb8iZtGtrdSR0ySHhXqis-TJwhSPMeg_LKQjFUz2XJwtZYylq7JApAPp77UAnGzw6ZkIv9J6mbY-c5aFopJMTBITEmPqqECaSbMUUXYq6X31VR8FxZ-EPFzF4B6j_OqEEfMyMkv2S7xWK7vDESdppe_ufgzUCdwepDK5zKeQGIEHVIc3amWNP97cxG8gBF3gvujVcF12TJ_oIfCJ6GSFqJsSZyYycPpaFug6QgSLGLx3yo0jFiKHyn4iHnRKnAQBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bff9339b7.mp4?token=u_fIZoOjZq5J646TvSAEb89dOqTSGcgP7RENTSxauqxnpMXVp-xuEwduPyc9LrCgOHwQFtismY6x74BE5dvX0Jb8iZtGtrdSR0ySHhXqis-TJwhSPMeg_LKQjFUz2XJwtZYylq7JApAPp77UAnGzw6ZkIv9J6mbY-c5aFopJMTBITEmPqqECaSbMUUXYq6X31VR8FxZ-EPFzF4B6j_OqEEfMyMkv2S7xWK7vDESdppe_ufgzUCdwepDK5zKeQGIEHVIc3amWNP97cxG8gBF3gvujVcF12TJ_oIfCJ6GSFqJsSZyYycPpaFug6QgSLGLx3yo0jFiKHyn4iHnRKnAQBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرزیدنت ترامپ درباره جمهوري اسلامي ایران:
هر جا را در جهان نگاه کنید، ایران به عنوان بدترین کشور جهان شناخته می‌شود و مدت طولانی است که این‌گونه بوده است.
ما کار را انجام خواهیم داد. آن‌ها در وضعیت بسیار ضعیفی قرار دارند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/147961" target="_blank">📅 08:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147960">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
دونالد ترامپ، رئیس‌جمهور آمریکا:
«
اگر ایران بخواهد به توافق برسد، از نظر من هنوز آماده نیست. ما یا به توافقی می‌رسیم که توافق خوبی باشد، یا اصلاً توافقی نخواهیم داشت
.
🔴
ما پیشاپیش توانایی آنها برای دستیابی به یک موشک هسته‌ای را از بین برده‌ایم. اگر ما از بمب‌افکن‌های B-2 خود استفاده نکرده بودیم، الان ایرانی داشتیم که سلاح هسته‌ای در اختیار داشت و آنها خیلی راحت از آن استفاده می‌کردند.
🔴
ما به کارمان رسیدگی خواهیم کرد، ما... آنها در وضعیت بسیار ضعیفی قرار دارند.
🔴
ما کنترل تنگه هرمز را در دست داریم؛ به‌طور کامل و قدرتمندانه آن را کنترل می‌کنیم. ما هر شب، معمولاً در طول شب، تعداد زیادی کشتی را هدف قرار می‌دهیم، چون آنها در شب نمی‌توانند چیزی ببینند.
🔴
آنها می‌دانند که ما آنجا هستیم، اما نمی‌توانند چیزی ببینند، چون ما رادارهایشان را نابود کرده‌ایم. آنها هیچ نوع... دیدی در شب ندارند.
🔴
اما ما عملکرد بسیار خوبی داریم و فکر می‌کنم آنها در وضعیت فروپاشی قرار دارند.
🔴
می‌دانید، اقتصاد آنها در حال حاضر در سطحی قرار دارد که هرگز پیش از این ندیده‌اند؛ بدترین وضعیت اقتصادی‌ای است که تا به حال داشته‌اند.
🔴
آنها تورمی بیش از ۳۰۰ درصد دارند. آنها کاملاً به‌هم‌ریخته‌اند. ببینیم چه اتفاقی می‌افتد.
🔴
فکر می‌کنم در نهایت پیروز خواهیم شد. نمی‌دانم از طریق توافق خواهد بود یا نه، اما ما همین حالا هم در حال پیروز شدن هستیم و فکر می‌کنم در نهایت پیروز خواهیم شد.»
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/147960" target="_blank">📅 03:21 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147959">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/411c3a472b.mp4?token=vNzdMidmyt51kdbpqFxTldgkVvJxPBeYi9gtnKpMLYLGfFQJ4y66rMkkP4zP5NyQVhPte3b7nFfSMZA65D5nbwXtQVVdHPUGf_u4s5bRyej4ma08WXBeBi4pqrQIoMdrJ-rzDa-tPOqgmKl0kgBkE9K_sEqlfbNl6QesoFf9sQeWqqGtNe32KN6tFgYbc6sBhTygiU6tWzdbKmwOUa7ro9OPqVMWJqT6nKVcnKAor5zSpzhutObtQQiv5j_ZndUZS9eWKEBwq8z0fznQY5K7_2Lrx2qtbdx3tx_MzXzfXs-b5PAJ4YOZ6EY_0mUJOmAYlsxbM1l7MQvAevFPYVFJ1y38mUV_bXNXT-l4q_76nTKhbmFWk8AYgKwMVmLkqLl6ZRI-2q4AX_j2zSx_fbssk7wNaELAceN687Cp8hQ20S24Z0KDCTEB17iIAs0n_f80WzwOVWvSAR1NUdQQFuc77RQ-gjrp9-yxmUtzoDJWTVSfxULNcKuhhRTu9pzhHkQ_0lu_I3Js-Z5VjohC_tkQJJI-yjOlb1YeP-V6nlwW73HJMCH8cA2ptHe2izDmB4lluHpy33Hux3vhD4iKN_OaveNR-VsBiIb3JX4BaDo7vuWOhXEFxGUfmb3RmV2CcsZ5zSLayXrCbT5mZlu1-wbAJQHcB5K8S8nbaaoV07g7jyM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/411c3a472b.mp4?token=vNzdMidmyt51kdbpqFxTldgkVvJxPBeYi9gtnKpMLYLGfFQJ4y66rMkkP4zP5NyQVhPte3b7nFfSMZA65D5nbwXtQVVdHPUGf_u4s5bRyej4ma08WXBeBi4pqrQIoMdrJ-rzDa-tPOqgmKl0kgBkE9K_sEqlfbNl6QesoFf9sQeWqqGtNe32KN6tFgYbc6sBhTygiU6tWzdbKmwOUa7ro9OPqVMWJqT6nKVcnKAor5zSpzhutObtQQiv5j_ZndUZS9eWKEBwq8z0fznQY5K7_2Lrx2qtbdx3tx_MzXzfXs-b5PAJ4YOZ6EY_0mUJOmAYlsxbM1l7MQvAevFPYVFJ1y38mUV_bXNXT-l4q_76nTKhbmFWk8AYgKwMVmLkqLl6ZRI-2q4AX_j2zSx_fbssk7wNaELAceN687Cp8hQ20S24Z0KDCTEB17iIAs0n_f80WzwOVWvSAR1NUdQQFuc77RQ-gjrp9-yxmUtzoDJWTVSfxULNcKuhhRTu9pzhHkQ_0lu_I3Js-Z5VjohC_tkQJJI-yjOlb1YeP-V6nlwW73HJMCH8cA2ptHe2izDmB4lluHpy33Hux3vhD4iKN_OaveNR-VsBiIb3JX4BaDo7vuWOhXEFxGUfmb3RmV2CcsZ5zSLayXrCbT5mZlu1-wbAJQHcB5K8S8nbaaoV07g7jyM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امشب تو شب نشینی شهر بابلِ استان مازندران، وسط تجمعات شبانه‌شون دور هم جمع شده بودن و داشتن «
کلاغ‌پر
» بازی می‌کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.4K · <a href="https://t.me/alonews/147959" target="_blank">📅 01:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147958">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WYJuBgMirdy-Y5cZRTjs4hxgQNHCozmKNgOXqobGJVRivaO3Hdn4BuSn8eqvvE3GJVr3_GpliaSll4EJ3BZ0Bs_xCPlf__9kNwEqLQE1_jkwUCApe_dXGQCOs1F5WE0046KbT01-JLiTcDQGespEoXXdxcUo3jgMMnpvAK9Rc4AexkSLEu63UQh-7lSOsqWMwOCYYSrbdgxSEPi0NrbS5hBYYQ1_vesKJ-G1FdAEzDsejYlr-IrPDOKb4lzfmpCYbzp7sCil3WtE-HBadTcH8FontmWcpWWN5bH8YONs31CgvfTG2bf-9_ssWXg8H21Tlvc9N9N8Lbw_Jibcuve-lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عجیب اما واقعی
‼️
🔴
ایران ایر که یک زمان بزرگترین ایرلاین آسیا بود اکنون فقط ۹فروند هواپیما دارد که اکثرا فرسوده هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.1K · <a href="https://t.me/alonews/147958" target="_blank">📅 01:01 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147957">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MqXDDJHAKfJ3MDAgF1DE0vJJVAA2pD6MXb5SU76U2Pr2p19ko11r_9Vs8Ajxrxov4bBIsx12nz3r0M_YoQ4RSZt9euqtcTIK1v8dQzuIgkxlQ4JAev0zdCJZPj33riCsMxdYh4sDHVKR82lnBMy_f5S_BuCsmf-ViJy79Bl4wnwhtvWj9HBaiKuhA5BuLPMc2BPUTeYk37gLNOzYPTKZplkAalshCpc2ai06sSbmwMLUW0ICYfg2ppzc5GVrDaPF1I6E7noKoJw9tchZod6aXy_mn6odskn5q-mqRG99iy4cSUAadiqYIEda4OmeYIA856GjVod7F_hXxYs4XY-JmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بمباران شدید جنوب لبنان توسط اسراییل
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.5K · <a href="https://t.me/alonews/147957" target="_blank">📅 00:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147955">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MQZvLPFXcA3LKc0AaJyUscLNAd7j0l6UyLrnyDBTACQj4AfvKYgzixUlKeMxI_GyfbqStkY7WXtg2d2Q-cj2pi5aqLuszKONkvH3XXJbEQPPaRGr-M4ulWz86HJ3vZzXTic6mWNNFJ42GoHdlh_xj_-SQCnxVtFdIkGO7bSEQ9C72V7xkp1z3mwtD2H07DnlTrSGVYXxSTtGdbPjpH4LAuo0m0sjodWNYPXsq18Yco8vycEKOAsld_5ju81oe_a54LAWrEvUGUOp7v5Z07iXtBWjCoPKYEd0xxENN6yadoKOa3Vw1W5XJLESoGYwEkOee549PSnsc4xcLrD63Wkkxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bidmfQ7NdrUS8cGuMr9AWJiFo20zt5MOBLZ7TrV2L-qSsLLb2gFPSSy1D2-1oHU48CTKsAsZ1h-r44se8q8Ygee8Zcm5d4TRFVw88Pd4Ggn1fmYRa5ximu3PcFvZlo2Qep2QNj_XeAKPq2qKWaLBcA0f5lRjZsfGISnfenU4LB4rCKLijau1rpoUsyLFeQzIC46vJ0PoH4SJ-b_Q2Ha9ixokOimJYin7A2zgwAxKy8OkOWAmK148YD84DEzuo_bhG93if6YJQhQUDTbH8C72BNZL6Na2CBo9g2j8v78_3IOyQZeJtXFFExGUB-0LCOvEmxa6dtg_q_ONYsr9m09yqg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
گسترش سریع فعالیت‌های ساختمانی در سایت طالقان-۲ تهران
🔴
تصاویر ماهواره‌ای نشان می‌دهند که فعالیت‌های ساختمانی در تأسیسات «طالقان-۲» در تهران به‌سرعت در حال گسترش است.
🔴
طالقان-۲ از تأسیسات مرتبط با برنامه هسته‌ای ایران در چارچوب پروژه «آماد» معرفی شده و گفته می‌شود این مجموعه در اوایل دهه ۲۰۰۰ برای آزمایش مواد منفجره مورد استفاده قرار می‌گرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/alonews/147955" target="_blank">📅 00:27 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147954">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
قوه‌قضاییه: واسه ۱۵۹ آمریکایی اسرائیلی پرونده تشکیل دادیم دادگاهی شن
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/alonews/147954" target="_blank">📅 00:17 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147953">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
میدل ایست آی: ترامپ «وسلی هانت»، جمهوری‌ خواه ضد اسلام و حامی اسرائیل را به عنوان سفیر بعدی آمریکا در عربستان نامزد کرده
🔴
این انتخاب در لحظه‌ای حساس برای روابط آمریکا و کشورهای خلیج فارس صورت می‌گیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.6K · <a href="https://t.me/alonews/147953" target="_blank">📅 00:08 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147952">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
نتانیاهو: من نه مسیح هستم و نه پادشاه.
یک پادشاه نیازی به انتخاب شدن نداره؛ اما من باید انتخاب بشم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.5K · <a href="https://t.me/alonews/147952" target="_blank">📅 23:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147951">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
نتانیاهو درباره ایران: اگر به‌موقع برای حمله به ایران اقدام نکرده بودیم، امروز اینجا دور هم جمع نشده بودیم؛ چون ممکن بود اصلاً کشوری به نام اسرائیل وجود نداشته باشه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.6K · <a href="https://t.me/alonews/147951" target="_blank">📅 23:39 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147950">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
مکرون خواهان اتش بس فوری در لبنان شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.5K · <a href="https://t.me/alonews/147950" target="_blank">📅 23:22 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147949">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه آمریکا به الجزیره: هیئت ایران طبق تعهدات کشور میزبان در مجمع عمومی سازمان ملل حضور خواهد یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.1K · <a href="https://t.me/alonews/147949" target="_blank">📅 23:17 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147948">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
فوری / عملیات تجارت دریایی انگلیس (UKMTO) اعلام کرد گزارشی از یک حادثه امنیتی در تنگه هرمز، در ۱۶ مایل دریایی شمال‌شرقی خصب عمان دریافت کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.2K · <a href="https://t.me/alonews/147948" target="_blank">📅 23:13 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147947">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gTx6-LKhVO-rzI9tAir1D9FuWQqv0RepgYFHC-iqp_-awMa2CqIsZaHEGNC3lf-lAbC5xuBdCcsdoHhZxM-zpRhK4t789KsC_j7EmstOzfGTMZ2SuWZGBjTAsRLj60sjLwO3FC3O5RCn3dSFaapzThLru4mVNt55D-LWjCa9OVE1VXNsqsw-TBmbB7MYdWvNF9IuCBRfvPGlSTds3z9YOx1SortZABuNlmwslcpyCZCL5S6ErcCrjH7e77MofGXHfRDn6uNgy58XBoQS8m9h7n0RHmWGdh_-cjI-JuHxAppXuTYKnA1_qSGf6Id10Tz98mat60zPc3n7CW3N_6AMYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف: نظم تک‌قطبی که در آن یک طرف با زور و اجبار امتیازگیری می‌کرد، به پایان رسیده است.
🔴
وتوی چین و روسیه سوءاستفاده سیاسی از شورای امنیت را رد کرد و حاکمیت قانون را مجدداً تثبیت نمود.
🔴
ما باید از چندجانبه‌گرایی دفاع کنیم؛ زیرا یک‌جانبه‌گرایی در خدمت منافع هیچ‌کس نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.3K · <a href="https://t.me/alonews/147947" target="_blank">📅 22:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147946">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">دلار و طلا تا کجا بالا میره
⁉️
🚫
پاسخ عجیب هوش مصنوعی
👇
https://t.me/+cs85WnZxgpM1NjRk
https://t.me/+cs85WnZxgpM1NjRk</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/147946" target="_blank">📅 22:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147945">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
خزانه‌داری آمریک«بیت‌بانک» (BitBank)، یک شرکت ایرانی فعال در حوزه دارایی‌های دیجیتال، را تحریم کرد
🔴
گویا صاحب بیت‌ بانک بابک زنجانی هستش
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.9K · <a href="https://t.me/alonews/147945" target="_blank">📅 22:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147944">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
آخرین جزئیات قتل‌عام خانوادگی به خاطر ارثیه از زبان خود قاتل
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/alonews/147944" target="_blank">📅 22:39 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147941">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OkG6qRcqrwNEAKwLYLT-1kyQmHN7K12r0-xO5TmtDDy_aM8Vs2WDMZB5Vuk_MvPaAHoeEH_sJBVD-kXpYKzjJqPzu0g-n6yZfbneLHBb4bFLM2H3q08IRCvhlrX2V1imyu_IGK7Zm0KB5Z56X29V5A2yUkmfkmG2uFSw-lVSdtgKjARHzaq9XPUNrqEB4RN49w0Pfkfchope1l9Bwl6C3jKabN3ANzp4Ozli6XdbAiRlW73LjKV-3L1eUBPSDlgbGbOSH222K3yJtxwxgudcG91J5TLJEnAq6EKw4l3ApcAnePJYBW47s8gAKHpWdTj_IO7eaxjQ3vFKcDCnfYQeaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jzMPT5ZIbgNfEMBU-Sonhp-yg_E-8sx4fCFpJeObLvIR82xSsgIznrivEyRGNNA2GmWDbsF055F2we1Qf7GXmM0Pj4DMmg9e9QM0yE9Jg_9iHXbClLTDb8DkAh_BIPow1-N_DLLKmt4dzSnfRDrBu3FOYFtV4wHLZTGt4w4YIM1HbJE0AlSGC8E8uHny_HsFqerSVt-8YiN4C15g_4URBt_64uXPnXQeUgDVG06-5gEgdSbP4JzHUa7X9O0HhO36ytRI1HbhxYRTEnYjpOrPIR_KiKQ7EqSVwuLZ4slAfttQUrDIZ7VfA9Zhsn-gZsO0st6TTRct4CZQloF6tBewJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FwhhIX1KCubevpG2M_pSUsC8ps8hqiIE7rH6pRucqAcLBS7XdzgQRoEHleuIqqQuhv3DRFry3v2VZsRV0-MLhTi1_-3I5SbH-FGiOrSlmg4s1tfHSpstKuvVrnNcU1bvQcnDlM8fetcEvq-ftSq0jhz0ZI4iZOmj-PDJkuMNx0U492ekVqVNh7Dv7thssyNZpXxguQJ00xtTLWvwk8sw24NZ0u1XXUMSsu0EQWyO49qnwQMbPnREOjAE3truWHel0KanSJ-16RFcEPRzZ7GThunc2trWtEb5-UMaBfkmOkSMBFdDM37Sf_UIGANKlO9SD2zsGKDSDGX-OmzIjfrKAw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویری از محل سقوط هواپیمای F-16 در شهرستان بلر، ایالت میشیگان، در شرق ایالات متحده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/147941" target="_blank">📅 22:26 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147940">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
آسوشیتدپرس: واشنگتن با صدور روادید برای مقامات ارشد ایرانی جهت شرکت در مجمع عمومی سازمان ملل موافقت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/alonews/147940" target="_blank">📅 22:19 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147939">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9263a32ce5.mp4?token=k0JIxr4LJTua5LNxTeeXbzlzg-9H15FPac9D0m_dkucsovaCtHkPCZx2am_961YMNEd1QT7hC74mY_iNarRRWJ-ytTJdVbFlg5y5Lv3yEzchzgrVej8FDms_qdjesdO7nke-9mlYiPnd5qlLQZ_1kcGbv_MWdqVJjh3JlGOQQtrpbOUgvshYPxP0RAgW9Ckn0Lr7-T_vfJnxpSlwx9spt_bFyKMhs7kOZhaZhOMg_WWTRqnLvXA_PN9r_l92mWI-bgv3f-6q-i_rU9_GHDvIz3QPtTWjQ3G_Vip1Ghx1XOy8VbnkUs9Qq4kkEZhNpGBdKn3p5qmP2jp5JmShMR86ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9263a32ce5.mp4?token=k0JIxr4LJTua5LNxTeeXbzlzg-9H15FPac9D0m_dkucsovaCtHkPCZx2am_961YMNEd1QT7hC74mY_iNarRRWJ-ytTJdVbFlg5y5Lv3yEzchzgrVej8FDms_qdjesdO7nke-9mlYiPnd5qlLQZ_1kcGbv_MWdqVJjh3JlGOQQtrpbOUgvshYPxP0RAgW9Ckn0Lr7-T_vfJnxpSlwx9spt_bFyKMhs7kOZhaZhOMg_WWTRqnLvXA_PN9r_l92mWI-bgv3f-6q-i_rU9_GHDvIz3QPtTWjQ3G_Vip1Ghx1XOy8VbnkUs9Qq4kkEZhNpGBdKn3p5qmP2jp5JmShMR86ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عروسی یک زوج ایرانی ارمنی با حضور اسنوپ داگ خواننده معروف آمریکایی
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/alonews/147939" target="_blank">📅 22:13 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147938">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
وزارت خزانه‌داری آمریکا: ما به دلیل حمایت از دولت ایران، پلتفرم معاملاتی ارزهای دیجیتال بیت‌بانک را تحریم کرده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/alonews/147938" target="_blank">📅 21:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147937">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
بر اساس گزارش شبکه خبری ای‌بی‌سی، سام آلتمن، مدیرعامل اوپن ‌اِی آی، و جنسن هوانگ، مدیرعامل انویدیا، قصد دارند هفته آینده در یک شام رسمی با اهمیت بالا در کاخ سفید در کنار شی جین‌پینگ، رئیس‌جمهور چین، حضور یابند
✅
@AloNews</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/alonews/147937" target="_blank">📅 21:46 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147936">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
وزارت خزانه‌داری آمریکا: ما به دلیل حمایت از دولت ایران، پلتفرم معاملاتی ارزهای دیجیتال بیت‌بانک را تحریم کرده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/147936" target="_blank">📅 21:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147935">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
وزارت امور خارجه ایالات متحده فروش احتمالی ۴۸ فروند جنگنده F-35 لایتنینگ ۲ به ارزش ۲۴.۳ میلیارد دلار به عربستان سعودی را تأیید کرده است که نخستین خرید این هواپیمای پیشرفته توسط این پادشاهی محسوب می‌شود.
🔴
این بسته شامل ۴۸ فروند F-35، ۴۹ موتور پرات اند ویتنی، تجهیزات ارتباطات، قطعات یدکی و حمایت‌های اضافی است.
🔴
وزارت امور خارجه به صورت رسمی کنگره را از پیشنهاد این فروش مطلع کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/147935" target="_blank">📅 21:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147934">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
نورالدین الدغیر خبرنگار الجزیره در تهران: «صحبت‌های ترامپ درباره حمله به ایران، به اعتقاد من تلاشی برای زمینه‌سازی جهت مذاکره با ایران است؛ چرا که این موضع‌گیری‌ها بلافاصله پس از سفر عراقچی به پکن مطرح شد. همچنین تماس تلفنی میان وزرای خارجه چین و آمریکا نشان می‌دهد که چین در حال سنجش تمایل ایران و واشینگتن نسبت به هرگونه اقدام چین برای حل‌وفصل اختلافات میان آن‌هاست، و ایران نیز در جستجوی کسی است که تضمین‌های لازم را ارائه دهد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/alonews/147934" target="_blank">📅 21:31 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147933">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gu9CGm4pkMMeYxF3yM683lwppGJms69-ZJELLYrfi7V9GuCxSzF1TB4R-YA64NacAjXYKph5520SQXmtPKo8BxjOBR-luT9Sba7Ze2GyD9PY3A8IPzQV1IH61HzLX6kgXX9fBsF8pp0GdYh7L4s-hTM8KC2KwijvzZ-GwM-q9rUNdpA9_fTacJzEKXlKHsaHhQu1AedvmW-tl987ztiDAyQ-sim-QI_djRmNrJM6aiupmJ5kYZnApkqqsSj_cbh5ix8-zP1kGLjH50myjKplyDhzZby_ZpRJihxr94tLIgENbKkFKDhnBJHAAH2OUeorfzeJo_9HM58pBcl6ZmW_fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ درباره لهستان: اخبار عالی! به لیدرهایی جسورانه از سوی دوست من، کارول ناوورکی، رئیس‌جمهور لهستان، پیشرفت‌های چشمگیری در جهت ایجاد پایگاه ارتش ایالات متحده در لهستان حاصل شده است.
🔴
اگر این اتفاق بیفتد، مکان آن به‌زودی اعلام خواهد شد. این یک گام تاریخی برای اتحاد بزرگ ایالات متحده/لهستان ما خواهد بود. از توجه شما به این موضوع سپاسگزارم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/alonews/147933" target="_blank">📅 21:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147932">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=m9d1dZFYiYhwj5lACuJBzoJxbMVC1u6m7pJU7zrfgqgdFLWf9MjGe8O9QXYW1ECf32pIJTufaisxazbS_dGnGHSh5LzZJctICCOMNRg5co9khm4XGDgXWSfZUwA0beWhs3djsVl6fK-av95cN6AyuULCPo7a_m8G9rThz0Y2FXNZUXgsYgaCtadbqzxm-OGXLfkceUdZE2ptAi1aujsZzaaiwP7xtgjnHACJFUJwq6bVyra36UNoNCGh88DzeK7XjbBgwIerxduGkqu5-QvRbwL-Ku63y_zuR9NOOvrmp4a4ovTceibpJEufdIPRbZGtFt-nT9Oc4FsHAmEAM2Wyeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=m9d1dZFYiYhwj5lACuJBzoJxbMVC1u6m7pJU7zrfgqgdFLWf9MjGe8O9QXYW1ECf32pIJTufaisxazbS_dGnGHSh5LzZJctICCOMNRg5co9khm4XGDgXWSfZUwA0beWhs3djsVl6fK-av95cN6AyuULCPo7a_m8G9rThz0Y2FXNZUXgsYgaCtadbqzxm-OGXLfkceUdZE2ptAi1aujsZzaaiwP7xtgjnHACJFUJwq6bVyra36UNoNCGh88DzeK7XjbBgwIerxduGkqu5-QvRbwL-Ku63y_zuR9NOOvrmp4a4ovTceibpJEufdIPRbZGtFt-nT9Oc4FsHAmEAM2Wyeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فارس: کالابرگ ۳۰۰هزار زیاد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/alonews/147932" target="_blank">📅 21:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147930">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGAslpkG2f9CEIiEUA-YxJ3IVprOhXcF5aGElDkAjQpcjbCgfSA4OavaEU4qSIpzED4KH1y-UEc1CV3CG7l78WU-lHksRRZN-E0O118i8Rq9wHpi-3uLnhT5ZQ9RFfeNKl3ruj_G6CfDeYBaxaNoJhXp00SpvKMnjmsI7IsN0Kj7aKOub-Zghzf5B9ERFOmwwLOO817a3jVj7MDA41rvmPEUl18UquFWBlBFCkq2jgZuAyPi-Y0yzZDIegj4KHLHdFhneaJd1PSJxdSBVAIeafSba6BWZ8VCcr63XsBoG-AVSlBYbsebq24x47Yhkvvm7Hpt0ruHo-cp7cLH3Uf24g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef55f0b0ff.mp4?token=oIKYWGKU0KI8CRObScRAMs5IZVb72X1tqAbsM4u14U73WVh8LJ53IHHTkcBXRZHq8NvvvZwKWorqMj81VYZ5H79cC6wJOL1PyXC3IdUatZjASo4XsIISJxSGmotKlC9qifpJGielu3AFgdZvYgWO9GOxgsCjRxKU4TFsy6yMWMXV6RtTNHRXW6prf8i76dphkAWiMokV9rExjhfc4_YFgBe-Be2VRWlB5hEYpOhGN6MXP7i59Y7qmhLSkRYr4esL2B5HmEGEzb6lK-GjUgG02loazHZZV96eQy6Ons6p3F9iDmdhtUJpZhzS2Tav1C_fBR5x8Ru46eDq6RJsvDPb9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef55f0b0ff.mp4?token=oIKYWGKU0KI8CRObScRAMs5IZVb72X1tqAbsM4u14U73WVh8LJ53IHHTkcBXRZHq8NvvvZwKWorqMj81VYZ5H79cC6wJOL1PyXC3IdUatZjASo4XsIISJxSGmotKlC9qifpJGielu3AFgdZvYgWO9GOxgsCjRxKU4TFsy6yMWMXV6RtTNHRXW6prf8i76dphkAWiMokV9rExjhfc4_YFgBe-Be2VRWlB5hEYpOhGN6MXP7i59Y7qmhLSkRYr4esL2B5HmEGEzb6lK-GjUgG02loazHZZV96eQy6Ons6p3F9iDmdhtUJpZhzS2Tav1C_fBR5x8Ru46eDq6RJsvDPb9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات سنگین اسرائیل به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/147930" target="_blank">📅 21:13 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147929">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
تا ماه بعد وضعیت طلا چجوریه؟</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/alonews/147929" target="_blank">📅 21:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147928">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
آکسیوس: ترامپ دستور داد سطح نیروهای فعلی در خاورمیانه تا پایان سال برای احتمال از سرگیری درگیری‌ها حفظ شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/147928" target="_blank">📅 21:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147927">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
وزیر دفاع پاکستان، خواجه آصف:
حتی اگر هیچ توافق‌نامه‌ای وجود نداشته باشد، اگر عربستان حمله شود — به‌ویژه مکان‌های مقدس ما — ما به موجب یک توافق ابدی موظف به محافظت از آن‌ها هستیم.
🔴
خانه خدا و مدینه منوره — محافظت از آن‌ها وظیفه دینی ماست
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/alonews/147927" target="_blank">📅 20:54 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147926">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb984ea71a.mp4?token=GVjfBpoA5csdHpbsY7GBOK_LClyf8uS0qljddhJyU1f-_A6EVab3FAq5mcXsNCD1JrMFNeZKGeZ1s0YHy6L4ZvcgKOFBoh9bUL4pqfWedlVv3ft-VtcyTO-RwjJPjUSCL-Zal8V-nqKxI1YMxZdaU0U06tWhc3NY7BY6g1dRsRIIQIOYa_kTOUKY_zMNMkRN1NVx6EDeoIwjNe9Y7u8yDwiyroOpNrLwZWfVA9taD-7bD-9QedJ7-_F1lj22t53M0zFOz2I2gSq3FPHU24NXX7qMQf9jxqa7FfIgC6uZR3aygsnk1B3LSKGHANf_IhHdavfV0WQfP3oPUair6mOgOQ1JyQS_Iw2r5X-U8FWCVTxiWOR3sLp98qaQJV6QwPFBhufBxvHXHG2ZK1UtzGFjg0HaCbdFTNHOyjMd723oKHj2NgTPPiwfeAWRnDvdW868PEX3ZlWxWqCa0MOrMSy9WHSBPxtqOkQ1g6bKhNuODpnylG57jO9W6afuumh6bdebDd-tdNqoEEL_CcqZ3YLoZ6SISe31RPjr2sQs8ev5Dn9lCPTqGdWB6g_IAv-XduYdxQ5wTloPg8SbqekH4H9aKMrCrB5ZJPJcdd2S3m5J1SG_SNp6J13H3q3QeaW0PKxB4jI0el6SeKgpd1OVvLBzVsU6aj87UzvNvL8lmU7X_Ms" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb984ea71a.mp4?token=GVjfBpoA5csdHpbsY7GBOK_LClyf8uS0qljddhJyU1f-_A6EVab3FAq5mcXsNCD1JrMFNeZKGeZ1s0YHy6L4ZvcgKOFBoh9bUL4pqfWedlVv3ft-VtcyTO-RwjJPjUSCL-Zal8V-nqKxI1YMxZdaU0U06tWhc3NY7BY6g1dRsRIIQIOYa_kTOUKY_zMNMkRN1NVx6EDeoIwjNe9Y7u8yDwiyroOpNrLwZWfVA9taD-7bD-9QedJ7-_F1lj22t53M0zFOz2I2gSq3FPHU24NXX7qMQf9jxqa7FfIgC6uZR3aygsnk1B3LSKGHANf_IhHdavfV0WQfP3oPUair6mOgOQ1JyQS_Iw2r5X-U8FWCVTxiWOR3sLp98qaQJV6QwPFBhufBxvHXHG2ZK1UtzGFjg0HaCbdFTNHOyjMd723oKHj2NgTPPiwfeAWRnDvdW868PEX3ZlWxWqCa0MOrMSy9WHSBPxtqOkQ1g6bKhNuODpnylG57jO9W6afuumh6bdebDd-tdNqoEEL_CcqZ3YLoZ6SISe31RPjr2sQs8ev5Dn9lCPTqGdWB6g_IAv-XduYdxQ5wTloPg8SbqekH4H9aKMrCrB5ZJPJcdd2S3m5J1SG_SNp6J13H3q3QeaW0PKxB4jI0el6SeKgpd1OVvLBzVsU6aj87UzvNvL8lmU7X_Ms" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس ستاد مشترک ارتش آمریکا:دشمنان ما در حال یادگیری از جنگ‌های ما و به چالش کشیدن برتری‌های ما هستند
🔴
دشمنان ما ممکن است از نظر جغرافیایی پراکنده و دور از هم باشند، اما به شکلی فزاینده با یکدیگر در ارتباط هستند.
🔴
آن‌ها فناوری، اطلاعات، تسلیحات و حمایت‌ های اقتصادی را با هم به اشتراک می‌گذارند.
🔴
آن‌ها میدان‌های نبرد گذشته و کنونی ما را مطالعه می‌کنند، به سرعت خود را با شرایط تطبیق می‌دهند و در پی یافتن راه‌های جدیدی برای به چالش کشیدن برتری‌های ما هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/alonews/147926" target="_blank">📅 20:49 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147925">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
ترامپ: ایرانی‌ها در تماس مستقیم با ما هستن و همچنان خواهان دستیابی به توافقن
🔴
می‌خواهم از جلسه عمومی سازمان ملل (هفته بعد) استفاده کنم تا مستقیماً از متحدان منطقه‌ای درباره گام‌های بعدی جنگ بشنوم
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/alonews/147925" target="_blank">📅 20:44 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147924">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
فوری/ ترامپ: به جایی که باید درباره ازسرگیری حملات گسترده به ایران تصمیم بگیرم، نزدیک هستم
🔴
هر اتفاقی ممکن است بیفتد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/alonews/147924" target="_blank">📅 20:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147923">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
فوری/ ترامپ: به جایی که باید درباره ازسرگیری حملات گسترده به ایران تصمیم بگیرم، نزدیک هستم
🔴
هر اتفاقی ممکن است بیفتد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/alonews/147923" target="_blank">📅 20:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147922">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
فوری / دونالد ترامپ: قرار است تصمیم مهمی در مورد ایران بگیرم
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/alonews/147922" target="_blank">📅 20:31 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147921">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed64f0a840.mp4?token=R9lHpnPNO-Uxeq1k2qhQTmnBvouYXXBkCOJHvSWLBZsIz7fNvlBV7EbKk01K-RSrNRui7ezyM4kbznRiPAmOUhrX7r7nq-VpWF3OPA5pvWsd54qgvSnMTWWgTRQeYOFlas4X1Y0P2WQMqPXpekrAAoNu_3Ad4QnCCYlTupVTlJvnAu6wRaBN8h3cPrvyjmvP6pR1aB_4kwU8FeRBVmeqrGAsJ1nF8QojDTX1tUn77wHUWwrrl4vIOU3k5sWQiXZRwXKeYcfbkHTALvWJFkHdHkDt4cAbn6jI1sba8y03ZWqS2gS3_dBkL6hEHVmJcxzg9Ok7Ymd-bcVO6fHtlGIShQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed64f0a840.mp4?token=R9lHpnPNO-Uxeq1k2qhQTmnBvouYXXBkCOJHvSWLBZsIz7fNvlBV7EbKk01K-RSrNRui7ezyM4kbznRiPAmOUhrX7r7nq-VpWF3OPA5pvWsd54qgvSnMTWWgTRQeYOFlas4X1Y0P2WQMqPXpekrAAoNu_3Ad4QnCCYlTupVTlJvnAu6wRaBN8h3cPrvyjmvP6pR1aB_4kwU8FeRBVmeqrGAsJ1nF8QojDTX1tUn77wHUWwrrl4vIOU3k5sWQiXZRwXKeYcfbkHTALvWJFkHdHkDt4cAbn6jI1sba8y03ZWqS2gS3_dBkL6hEHVmJcxzg9Ok7Ymd-bcVO6fHtlGIShQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نمایش بمب‌های سنگرشکن برای تهدید ایران در گزارش خبرنگار فاکس‌نیوز
🔴
خبرنگار فاکس نیوز: آنچه الان می‌بینید، یک بمب سنگرشکن GBU-31 ویکتور ۴ است. ما در یکی از انبارهای مهمات ناو هواپیمابر جورج واشنگتن هستیم و همان‌طور که می‌بینید، انواع مختلفی از تسلیحات در اینجا وجود دارد؛ از جمله موشک‌ها و بمب‌های گوناگون
🔴
در انتهای این بخش هم انواع دیگری از بمب‌ها را می‌بینید. این‌ها بمب‌های ۲٬۰۰۰ پوندی هستند. باز هم تأکید می‌کنم، تمام این تسلیحات در صورتی مورد استفاده قرار خواهند گرفت که رئیس‌جمهور دستور حملات بیشتری علیه حکومت ایران صادر کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/alonews/147921" target="_blank">📅 20:25 · 26 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
