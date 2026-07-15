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
<img src="https://cdn1.telesco.pe/file/nugzGVn_IQcWHuGKuf7S3dz2L8tSsrkLM_8Q1dExVo8pzTNhgPrBEl7TWKINUZO3NQ1Qh1bKgl7xB28qX7LrLSLZ3BbG8a-2cCM9XLzfIvQB2GpNvRR0XqLscvgkCtLNOQ_rIuX3tH-87XVgleZNTHx6FTbahU2_1KtWMmvlonu8i-g1mmq0umIWb4ThkeB1RwZkCytABNbhf4PCOyiEACMNBDo3_s0HmU0mx2hsf2-osrBtD0RtylEiDEewcenEFYGY2EBjIhk1EIXStSZw5iRYRzR0ku4U_iBy1jA-ZiemkAwJbyQxysqLgZbHAUIbdxIEPhrE_6gmVQMiH25FEQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.38M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 14:36:21</div>
<hr>

<div class="tg-post" id="msg-77098">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cd0e6fce01.mp4?token=M7vcfkGAl3o3GfkUR0IjG97DNqJF-kaAi35L0gBT64jO8m3X62i-aYe0L19g0XNVQR1xw89xkXReGEBNCZXrqNirUGy-_TbINjCiLFN8AXSs_3scyxlisUi4tWPdhs8ioxxJeFOEznJPz0gr8BtZxTaZLtujgXAZUNaGv0LEGOGL34UG8MBmwYsY5FpfBIoS7iHth8Tag915Jf2sKYytGQr3gtDQDcR7DGqrOCe5ToDH7Tdo5lPz_fWbh_yPLtMATNYTBqDR_8LG62ptq9X_8eu-7WN0a9HRhVgCCODcspNhWZKa_UIFjoKr36jkj8vGB4gTFox-qT4uBVcEjyFURQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cd0e6fce01.mp4?token=M7vcfkGAl3o3GfkUR0IjG97DNqJF-kaAi35L0gBT64jO8m3X62i-aYe0L19g0XNVQR1xw89xkXReGEBNCZXrqNirUGy-_TbINjCiLFN8AXSs_3scyxlisUi4tWPdhs8ioxxJeFOEznJPz0gr8BtZxTaZLtujgXAZUNaGv0LEGOGL34UG8MBmwYsY5FpfBIoS7iHth8Tag915Jf2sKYytGQr3gtDQDcR7DGqrOCe5ToDH7Tdo5lPz_fWbh_yPLtMATNYTBqDR_8LG62ptq9X_8eu-7WN0a9HRhVgCCODcspNhWZKa_UIFjoKr36jkj8vGB4gTFox-qT4uBVcEjyFURQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی: '
#چابهار
، چهارشنبه ۲۴ تیر، ساعت ۵:۳۰'
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/77098" target="_blank">📅 08:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77097">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/67211d7671.mp4?token=ILGnpyHAxIFQA9hlGvQmR5yGzwkEfqormqJzZGz0K-REjrTDBW_V9ssfCyWCcSPhK52gGHKCiWi83wkAWildL3gVkFgCFT0AJ14J2MYQVoJa4Je1jUaZIVEF5CCkaMxQoTaJgr3xOCyk8vB9GA98Felflwn8R7NvjWyUnceMACbsBhUz7SCh_GgN7-a_c5VGAhS7X2H9opawUuLCzfYIRTW9L6qbUbhw4puCpjJKaJGaSm7cQiucFS7dZJrUQ406RfN6CXvCELLksaoRhbXw37w-soLd7aFnPj_FHfjB3s-3s9MdTyUhLRmVchwH-y0kQQ8hNbEAN6h4xA6zbjaFRA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/67211d7671.mp4?token=ILGnpyHAxIFQA9hlGvQmR5yGzwkEfqormqJzZGz0K-REjrTDBW_V9ssfCyWCcSPhK52gGHKCiWi83wkAWildL3gVkFgCFT0AJ14J2MYQVoJa4Je1jUaZIVEF5CCkaMxQoTaJgr3xOCyk8vB9GA98Felflwn8R7NvjWyUnceMACbsBhUz7SCh_GgN7-a_c5VGAhS7X2H9opawUuLCzfYIRTW9L6qbUbhw4puCpjJKaJGaSm7cQiucFS7dZJrUQ406RfN6CXvCELLksaoRhbXw37w-soLd7aFnPj_FHfjB3s-3s9MdTyUhLRmVchwH-y0kQQ8hNbEAN6h4xA6zbjaFRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام: ده‌ها موضع نظامی را در نزدیکی تنگه هرمز و مناطق ساحلی ایران هدف قرار دادیم
ترجمه ماشین:
تامپا، فلوریدا — فرماندهی مرکزی ایالات متحده (سنتکام) در ساعت ۱۰ شب به وقت شرق آمریکا در ۱۴ ژوئیه، دور دیگری از حملات علیه ایران را به پایان رساند و ده‌ها موضع نظامی را در نزدیکی تنگه هرمز و مناطق ساحلی ایران هدف قرار داد.
جنگنده‌ها، پهپادها و شناورهای نیروی دریایی آمریکا در جریان این موج حملات هفت‌ساعته، مهمات هدایت‌شونده دقیق را علیه سایت‌های موشکی و پهپادی ایران، توانمندی‌های دریایی و سامانه‌های دفاع ساحلی به‌کار گرفتند تا توانایی ایران برای تهدید کشتی‌رانی تجاری و خدمه غیرنظامی را بیش از پیش تضعیف کنند.
این حملات در همان روزی انجام شد که نیروهای آمریکایی محاصره دریایی علیه شناورهای در حال تردد به مقصد یا از مبدأ بنادر و مناطق ساحلی ایران را از سر گرفتند. این محاصره امروز از ساعت ۴ بعدازظهر به وقت شرق آمریکا به اجرا درآمد.
نیروهای آمریکایی همچنان هوشیار، مرگبار و آماده اجرای عملیات‌هایی هستند که فرمانده کل قوا دستور دهد.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/77097" target="_blank">📅 06:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77092">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JKTqmP8p1QVNMSfgcq0qxY283PcqUfMfclHK2Lk2KpyBaJJRzCi0tRVzyGQdU7YkPjAjoAUHVgtJr5IxGWBlUcDNuDxoQoh2Au3XR6eu2rcn6e_wxNy3j6-dZCo8d4ATX7pxPiI4ZVrAUCPAtEi-K179Ub61EXR_D2kDuXgHata9wWtQSHGtcazpIEwp23QHQVfhJ6DXoLj8dRaVLaqRLDqgCnozqJjufar8pJXL_gTCtwqm4-Bnv69s93PHNKtOyYhV4l5r-rSDl_d5z1T8FmmYq9sasilplXBmmcjSC7XDGP8RVjQ8OmXjqaS_cxVk-U3HgbF380SsSro62QMjyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RFibI6R9ZuD39JmfXdyoLN68cz5duDy7-jZXNsqpIoEL3mO3gLa5U0WtETrkCS79OAgqU9Lx_6DBybTL_jT10-p5rbPxrp7R9qHWOfEJ3asfeKi70WvHBWI-fzCiJaFmu5h-8vAUHFIPSIIfyCDJqmRGIdxCrYIXypaOyTjR7YuX6u6Q5WIfBR0oOvZYkyGqVfvzWXSVatriwgpAY-jGc9EfmeIVjqd06HEfTvjfs4NR_CBXidksdLbze29RRyWD3iLFoc_SgemWGsSg6pRU47uLQV5kk4leA70rPDzr5AacClAUtv1n53aFfLQ2skZD8GUmZWTyZgiZ2uUzZlcRWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d4e711947a.mp4?token=uBYU5h56JMLAfWZ00gO_hxVtm6S6Wko5N-5AxL0OvHbnd0u7W34vltZ6iVMRPja5z1lYHNfJ0cZ46c4zPSMeM2An1Rr9S-CVk5NiftfXwL6RQGc9z1W8XS3EdyiwD-3V-29Bwh6ackjQLLfRx2gW90V1UF1klPXRNprsjjAiz395jnn2dF1IMOIgxoqFHQO9fw_kGCu34lGfj1-0JRZUNPlwqgMdbD2qByTzb_UdfHBARG-KHUWRenreE5PHeFhCuaTxLAPm8l8jFP6XwzC1IQgOo4HP0Sxrb4PnT_n8bDfl9WJ3yn0Gq34_xTg9Zg-_7BAK21cZwsKJwxJkaD75Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d4e711947a.mp4?token=uBYU5h56JMLAfWZ00gO_hxVtm6S6Wko5N-5AxL0OvHbnd0u7W34vltZ6iVMRPja5z1lYHNfJ0cZ46c4zPSMeM2An1Rr9S-CVk5NiftfXwL6RQGc9z1W8XS3EdyiwD-3V-29Bwh6ackjQLLfRx2gW90V1UF1klPXRNprsjjAiz395jnn2dF1IMOIgxoqFHQO9fw_kGCu34lGfj1-0JRZUNPlwqgMdbD2qByTzb_UdfHBARG-KHUWRenreE5PHeFhCuaTxLAPm8l8jFP6XwzC1IQgOo4HP0Sxrb4PnT_n8bDfl9WJ3yn0Gq34_xTg9Zg-_7BAK21cZwsKJwxJkaD75Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر دریافتی با شرح:  انفجار حمله به چابهار حدود ساعت ۵:۳۰
چهارشنبه ۲۴ تیر
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/77092" target="_blank">📅 06:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77091">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G17H0vdf5TRtRAgfLakCOmVvkDqM8oMzw_EqZjTcUm569h-wEk44K6Rr7ST5k3UGPvVSgARBudTnPnQrCiRJsRvVGsgs1Ufgp3slTiUAi5b0ueGo2RjgIix0FnpolpkxwwFELMdPH4Fu8JKZ4ByjLprVUYTPy4QcuglDM2pKAEfNAbW-9IoxD4oMV-ZxTRQ05JuNp5koO525H9cloUXSaSthEsfzlYAMS417yyPn4uiBy4qo-x4kHpD0hAo9Oax3XjzH1NWcYl1OOkdScseSPqToKp6Orve_h4t20DahwdG1QvcvpKHaS1eMxDrOnsK_mvSW64UvcZC2fxTEuxWQUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی از سیستان و بلوچستان:
چابهار پایگاه مستقل امام علی همین الان دوتا زد
سلام کنارک الان دو تا زد
سلام همین الان صدای چهار انفجار در کنارک
۵:۳۰ دقیقه چابهار سمت دریا کوچیک فکر کنم زدن. صدای جنگنده ها میومد.
ساعت ۵:۲۰ صبح جنگنده وارد حریم چابهار شد پایگاه امام علی و کنارک زد
کنارک دوباره یکی زدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/77091" target="_blank">📅 05:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77090">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">پیام‌های دریافتی دوباره هم‌زمان از سربندر و ماهشهر:
همین الان بندر امام خمینی‌ رو زدن سه بار
یا خدا سه تا انفجار وحشتناک سربندر
بعدی
وحید جان سلام ماهشهر صدای چندین انفجار متوالی
سلام ماهشهر الان زد نسبت به قبلیا موجش بیشتر بود
همین الان صدای شدید ماهشهر، نمیدونم کجا رو زدن
سلام اقا وحید سربندرو همین‌الان‌چهار بار زدن
ماهشهر الان ۴تا زدن
۵تا شد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/77090" target="_blank">📅 05:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77089">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q7caCK4aB7f9fb8gRkqFG2L-2-3Xefb0KzJB57BcjmD4H2ARXb5tVxWrJQA2UXceJO389voJvxOl3xcyV40ZV_J5rX1l_hsEqTTLWx3axeLSAGpdMD91eQHOwSi-ndv4G0so-9AEzbJ0qfnXXmEDhQCq13a3HzSubTzolH6mG-oOklNI5oyH9nfbFIGm19hdo8O2w2oJNuGZ7HNmlNQb-cBNLltD8fwrId0ASvQoeH-DxejVrz6hcSg-UkKruz0auatYhVrH3POgu4P1B0-GAqgCCkuJchNrq6FRj7mJb6aKdBQLLP91tG4jMPGRZy19JgZ7xLuQEYkQpcTIe2JvxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیش از پیام‌های مربوط به شهر بوشهر، پیام‌هایی از شهر جم در استان بوشهر داشتم درباره شنیده شدن صدای انفجار:
۴/۲۵ همین الان ۳موشک به فرودگاه جم برخورد کرد قبلن از اونجا موشک میفرستادن
جم بوشهر
فرودگاه جم
الان صدای چند انفجار در شهرستان جم استان بوشهر شنیده شد.
دیشب هم همین موقع صدای چند انفجار شنیده شد.
همین الان فرودگاه جم رو زدن
درود وحید همین الان جم سمت پایگاه چمران نه سمت فرودگاه توحید دوتا صدای خیلی آروم اومد بعد دود سفیدی بلند شد و نورانی، معلومه موشک خواستن بفرستن نرفته
جای همیشگی نبود
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/77089" target="_blank">📅 04:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77088">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">پیام‌های دریافتی:
بوشهر صدای انفجار همین الان
انفجار ساعت ۴:۳۸ خورموج بوشهر
سایت موشکی را زدن
بوشهر ششم شکاری هوایی [رو] زدن
ساعت ۴:۴۰
سلام وحید جان شبتون بخیر ساعت 4:41 بهمنی رو دو بار تا الان زدن و همینجوری دارن میزنن پشت سر هم پایگاه هوایی
انفجار خیلی وحشتناک بوشهر ساعت ۰۴:۴۱
وحید بوشهر ۴:۴۱ پایگاه هوایی یا دو طفلان مسلم
😂
بوشهر الان زدن ۴:۴۱
درود وقت بخیر
بوشهر همین الان یک صدای انفجار بشدت بلند اومد
سلام ساعت 4:40 صدا بزرگ انفجار از بوشهر اومد
۴:۴۰ بوشهر یه انفجار بزرگ
وحید ۲.۳ انفجار سنگین در بوشهر ۴:۴۰
وحید بوشهر ناحیه‌ی بهمنی صدای شدید انفجار
😭
😭
😭
😭
😭
😭
بوشهر زدن الان ۴:۴۰
شهر بوشهر ۰۴۴۰ زدن
سلام وحید الان بوشهر رو خیلی بد زدن مراقب خودتون باشید خیلی میزنن مراقب باشید ساعت ۴.۴۰ بوشهر بیسیم
وحید ما سنگی بوشهر هستیم صدا خیلی شدید بود درحدی که انگار صدمتر کلا فاصله داشت
بوشهر دو تا صدای بلند اطراف تنگک اومد
آقا وحید پایگاه هوایی بوشهر و زدن 4:40 صدای انفجار خیلی بلند بود
داداش بوشهر شش دقیقه پیش یچیز سنگین زدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 272K · <a href="https://t.me/VahidOnline/77088" target="_blank">📅 04:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77087">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/34c6ee4fb2.mp4?token=VwCyp9t_5rQKG-NoF9y-9Ro4LJ2jt0FNo8kH2lziaOf0w331G-GHsY2_GqsZb981lWbT5YaLmmZN_WLgpZAtv1bZOdzqv8yqHGTbFyABZA1_bicbI0fiVw2DL9rhFhviMK8vZAdmBlplj0bJX8GQErfL-vJwt4DgAi85MlY0HIO4JhEXuejGfD_6FBtTWS2rBV_16ewyUbPzNvXUnUjd1iSGTuzDLY6PI2YP0Bx1BeP2TkQyvTntCWoIFBDkWil2VVvscDcSLNMe7xBUomtHgFUdCCOs2130I_rYFtAG0fzXH2gPif2awrt8z1YTAgGbqkcxkvOmh4rIen-ImSsODA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/34c6ee4fb2.mp4?token=VwCyp9t_5rQKG-NoF9y-9Ro4LJ2jt0FNo8kH2lziaOf0w331G-GHsY2_GqsZb981lWbT5YaLmmZN_WLgpZAtv1bZOdzqv8yqHGTbFyABZA1_bicbI0fiVw2DL9rhFhviMK8vZAdmBlplj0bJX8GQErfL-vJwt4DgAi85MlY0HIO4JhEXuejGfD_6FBtTWS2rBV_16ewyUbPzNvXUnUjd1iSGTuzDLY6PI2YP0Bx1BeP2TkQyvTntCWoIFBDkWil2VVvscDcSLNMe7xBUomtHgFUdCCOs2130I_rYFtAG0fzXH2gPif2awrt8z1YTAgGbqkcxkvOmh4rIen-ImSsODA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترجمه ماشین:
تصاویری که بنا بر گزارش‌ها پیش‌تر در جریان حملات پهپادی و موشکی ایران به کویت ضبط شده‌اند، لحظه اصابت یک پهپاد شاهد-۱۳۶ را نشان می‌دهند. آمریکا همچنان با ایران به تبادل حملات ادامه می‌دهد و اکنون اهدافی در بحرین و کویت زیر سنگین‌ترین آتش ایران قرار گرفته‌اند.
sentdefender
,
MenchOsint
ستاد کل ارتش کویت، بامداد چهارشنبه، با انتشار بیانیه‌ای اعلام کرد که پدافند هوایی این کشور در حال مقابله با حملات پهپادهای «متخاصم» است.
این ستاد با تاکید بر اینکه صدای انفجارهای احتمالی ناشی از رهگیری این پرتابه‌ها توسط سامانه‌های دفاع جوی است، از مردم خواست تا دستورالعمل‌های امنیتی صادره از سوی مراجع مربوطه را رعایت کنند.
@
VahidOOnLine
وزارت کشور بحرین، با انتشار هشداری فوری در حساب رسمی خود در اکس، اعلام کرد آژیر خطر به صدا درآمده است و از شهروندان و ساکنان خواست آرامش خود را حفظ کنند و به نزدیک‌ترین مکان امن بروند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 258K · <a href="https://t.me/VahidOnline/77087" target="_blank">📅 04:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77086">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">خبرگزاری جمهوی اسلامی ساعت ۲:۵۶
حمله به یک واحد تولید آب معدنی در موسیان
🔹
دقایقی قبل، یک واحد تولید آب معدنی در اطراف روستایی در بخش موسیان (استان ایلام) هدف سه پرتابه دشمن قرار گرفت.
🔹
مراد یگانه فرماندار دهلران بامداد چهارشنبه به خبرنگار ایرنا گفت که این حمله هیچ تلفاتی نداشته است.
🔹
وی اظهار کرد که در این تجاوز به تجهیزات کارخانه خساراتی وارد آمد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 272K · <a href="https://t.me/VahidOnline/77086" target="_blank">📅 03:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77085">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8c0dd68356.mp4?token=V7Y3bBx22gvIEQmDaphJtBik4O6lxD144F-LbgthUUYsv7D8AlUbBSLrQkV0Uxrd0--tqVa52-Zv7M5MuDGMTXKVoFI9c5QiuFTAq3oiuEdH1lZkJFbAHZ99gzOVh9uV8n359l_DaxOFs0LS0O9CzxMy8uXXf3s4xzVbIb-iMKTbMHZlLDa7qv77eSgxa9VkrlKcsWMccgwvznZkQTytE9a--Xw7ojeAtZDa2MHcZrbcEiz_d8vmw0kJhhoRcCNFTAuils_MQZhZ3vALqUEILfOnkuClAyy20IYPGHoTWeJ1B9UaoHyeJg1sGQgrzdH_g0MtzlIIV12JJ-Z0UqJN-A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8c0dd68356.mp4?token=V7Y3bBx22gvIEQmDaphJtBik4O6lxD144F-LbgthUUYsv7D8AlUbBSLrQkV0Uxrd0--tqVa52-Zv7M5MuDGMTXKVoFI9c5QiuFTAq3oiuEdH1lZkJFbAHZ99gzOVh9uV8n359l_DaxOFs0LS0O9CzxMy8uXXf3s4xzVbIb-iMKTbMHZlLDa7qv77eSgxa9VkrlKcsWMccgwvznZkQTytE9a--Xw7ojeAtZDa2MHcZrbcEiz_d8vmw0kJhhoRcCNFTAuils_MQZhZ3vALqUEILfOnkuClAyy20IYPGHoTWeJ1B9UaoHyeJg1sGQgrzdH_g0MtzlIIV12JJ-Z0UqJN-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حال وش:
منابع محلی از افزایش آمار مجروحان حمله به تیپ ۳۸۸ ارتش در
#بمپور
خبر دادند؛ دست‌کم ۵۰ مجروح، دست‌کم دو فوتی در بیمارستان و گزارش‌هایی از تلفات گسترده در داخل پادگان
بر اساس تازه‌ترین اطلاعات دریافتی،
تاکنون دست‌کم ۵۰ مجروح به مراکز درمانی، به‌ویژه بیمارستان خاتم‌الانبیا ایرانشهر، منتقل شده‌اند و حال هفت نفر از آنان وخیم گزارش شده است.
به گفته منابع حال‌ وش: «از میان مجروحان منتقل‌شده به بیمارستان، تاکنون دست‌کم دو نفر بر اثر شدت جراحات جان خود را از دست داده‌اند و وضعیت هفت نفر دیگر نیز بحرانی است. روند انتقال مجروحان همچنان ادامه دارد.»
منابع افزوده‌اند: «همزمان گزارش‌های متعددی از داخل تیپ ۳۸۸ حاکی از آن است که
شمار کشته‌شدگان در محل حمله بسیار بیشتر از آمار منتقل‌شدگان به بیمارستان است و ده‌ها نفر در داخل پادگان جان خود را از دست داده‌اند.
با این حال، به دلیل محدودیت‌های امنیتی و جلوگیری از دسترسی به محل، امکان راستی‌آزمایی مستقل این آمار تاکنون فراهم نشده است.»
به گفته منابع محلی، بخش‌هایی از آسایشگاه سربازان و سایر تأسیسات داخل پادگان در زمان وقوع حملات هدف قرار گرفته و همین موضوع موجب افزایش شمار تلفات و مجروحان شده است. همچنین تدابیر امنیتی در اطراف تیپ همچنان ادامه دارد و از نزدیک شدن شهروندان و خانواده‌های نظامیان به محل جلوگیری می‌شود.
حال‌ وش
پیش‌تر
از وقوع چندین موج حمله، شنیده شدن دست‌کم ۱۱ انفجار، ورود آمبولانس‌ها به داخل تیپ، خاموش شدن کامل چراغ‌های پادگان و انتقال مجروحان به بیمارستان خاتم‌الانبیا ایرانشهر خبر داده بود.
تا لحظه تنظیم این گزارش، هیچ‌یک از مقام‌های جمهوری اسلامی درباره آمار کشته‌ها، مجروحان، میزان خسارات و جزئیات این حمله اطلاع‌رسانی رسمی نکرده‌اند. اطلاعات منتشرشده در این گزارش بر پایه اظهارات منابع محلی و شاهدان عینی است و حال‌ وش همچنان در حال پیگیری و راستی‌آزمایی ابعاد این رویداد است.
haalvsh
همزمان با انتقال شمار زیادی از مجروحان حمله به تیپ ۳۸۸ پیاده مکانیزه نیروی زمینی ارتش در شهرستان بمپور به بیمارستان خاتم‌الانبیا ایرانشهر،
مرکز انتقال خون ایرانشهر با انتشار اطلاعیه‌ای از شهروندان واجد شرایط خواست برای اهدای خون به این مرکز مراجعه کنند.
haalvsh
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 284K · <a href="https://t.me/VahidOnline/77085" target="_blank">📅 03:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77084">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jQ3PL5BJjSs-iqo65vS6p-327XxUvPo1bwZ-4mjWaNI3wuuC2YlaDnzNsla7Fqm_hIaQg4naPbRniuHOkCCjE28EymnBEBNpxyQZIEXkiBB0DIkHaXWtPlLMSmMMr47OeYUihT0NYaFlirsHQZMp2-L7kGQzUXclbWyOSYnDRU8RR0HFvAeSu6SReBWZShxKZ-Y6MmDzDh6cnjEP5C7Ypp3s2CsOiWgktN7RJHnbWxldElcawEWUBRSxMS1v7tVPwMGr_BwkMiWAm9D2TVh2Unfiy3tQs2HMyzr5qULxbVB-QPFBFahIT7gR2I8YrtNsaWtEB9LzhGtrldYyayOTpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریاسالار برد کوپر، فرمانده سنتکام، با انتشار بیانیه‌ای اعلام کرد جمهوری اسلامی طی هفت روز گذشته با حمله‌های عمدی به غیرنظامیان در سراسر منطقه، هفت کشتی تجاری را هدف قرار داده است. به گفته او، در نتیجه این حمله‌ها نزدیک به ۱۲ نفر از خدمه غیرنظامی کشته، مفقود یا زخمی شده‌اند.
@
VahidOOnLine
تصویر انگلیسی رو سنتکام منتشر کرده متن فارسی رو بالاش اضافه کردم. ترجمه ماشین:
بیانیه فرمانده ستاد فرماندهی مرکزی ایالات متحده
«ایران طی هفت روز گذشته با حمله به هفت کشتی تجاری، عمداً غیرنظامیان را در سراسر منطقه هدف قرار داده است؛ حملاتی که در نتیجه آن نزدیک به دوازده تن از اعضای غیرنظامی خدمه کشته، مفقود یا زخمی شده‌اند.
نیروهای ایرانی همچنین ده‌ها موشک و پهپاد به‌سوی کشورهای همسایه در حاشیه خلیج فارس پرتاب کرده‌اند. نیروهای ایالات متحده، ایران را به‌دلیل این تجاوز بی‌دلیل که همچنان جان افراد بی‌گناه را به خطر می‌اندازد، پاسخگو می‌کنند.»
دریاسالار برد کوپر، فرمانده سنتکام
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 272K · <a href="https://t.me/VahidOnline/77084" target="_blank">📅 03:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77083">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6d1f952110.mp4?token=T9_mWU4jNN3fMVNyOCvGjw6Lk9cA7D1_rKKuqmJO3suOFtc0nomxqPhklF3inP4EQvu2JakVGWjOnP1YZRAXjIU0MYgkXfMIhHMc-8DxmMuuWsEVx1GU7TAL6DMR81CasFGk2CGeGgeeJCuLVwpY_odQK5vOky_S4CrNBrsiLkxD69f8ASPIbVGk3_ZFyLLh-9JijkPcMhXu17ZqdFZMD83aHmMMpDlrvRh9ord2PbigbBVVGEEgV69V7Ga2p2KCvCA0StavW-JfAx_0kUFsV0tK9-UtTVbbaVpbXeSMO_gUdaadynyDpRlSoSAwUaN5B41wgUDkMJZP_711yu3Wpg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6d1f952110.mp4?token=T9_mWU4jNN3fMVNyOCvGjw6Lk9cA7D1_rKKuqmJO3suOFtc0nomxqPhklF3inP4EQvu2JakVGWjOnP1YZRAXjIU0MYgkXfMIhHMc-8DxmMuuWsEVx1GU7TAL6DMR81CasFGk2CGeGgeeJCuLVwpY_odQK5vOky_S4CrNBrsiLkxD69f8ASPIbVGk3_ZFyLLh-9JijkPcMhXu17ZqdFZMD83aHmMMpDlrvRh9ord2PbigbBVVGEEgV69V7Ga2p2KCvCA0StavW-JfAx_0kUFsV0tK9-UtTVbbaVpbXeSMO_gUdaadynyDpRlSoSAwUaN5B41wgUDkMJZP_711yu3Wpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Vahid
پیام‌‌های دریافتی:
وحید جان همین الان تبریز موشک زدن باز
سلام وحید از تبریز موشک فرستادن ۲:۱۰
سلام آقا وحید ساعت ۲:۱۲ دیقه از تبریز تا الان که ساعت ۲:۱۴ هستش دوتا صدای موشک اومد
سلام وحید جان همین الان ساعت ۲:۱۴ صدای های انفجار میاد از ارومیه
مشخص نیست پرتابه موشکه یا چی
پرتاب موشک از حوالی تبریز به جای نامشخص، صدای غرش خیلی شدید و بی سابقه
سلام وحید دو سه دقیقه پیش از سایت موشکی [...] دو موشک  پرتاب کردن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/77083" target="_blank">📅 02:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77082">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c39cdf8b03.mp4?token=TaioeJAoyr4Y3R4f5Yf8KPK0TvvSLmkXcBtgalTgZbjfxu8OuaqFgK1S6Kxb3gr9ricD-AlsINYC1wk9ZOF6-HulCH-7hgEpqr_XY85IDCt2JGc4nucVen2YfU8sHO9w6-clAw6dGKqZapmz20mIr_y6YQ1J0JHWU8imOwiEk9B6rscehc6-fYh6bv2aTWcxEkIAywoGBGXvKDtBY9RJ79cWoS3vusIRksAShT3angX_3cV9C3GyA6vy9jTJlqvII1e4kRT6ay3tvs5eVmfc65aakkWfPJYw5NR7_FuJvoOvoQfmArINo_cuY-60xSF9tVHYhi8pI5LiPi38EYyaog" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c39cdf8b03.mp4?token=TaioeJAoyr4Y3R4f5Yf8KPK0TvvSLmkXcBtgalTgZbjfxu8OuaqFgK1S6Kxb3gr9ricD-AlsINYC1wk9ZOF6-HulCH-7hgEpqr_XY85IDCt2JGc4nucVen2YfU8sHO9w6-clAw6dGKqZapmz20mIr_y6YQ1J0JHWU8imOwiEk9B6rscehc6-fYh6bv2aTWcxEkIAywoGBGXvKDtBY9RJ79cWoS3vusIRksAShT3angX_3cV9C3GyA6vy9jTJlqvII1e4kRT6ay3tvs5eVmfc65aakkWfPJYw5NR7_FuJvoOvoQfmArINo_cuY-60xSF9tVHYhi8pI5LiPi38EYyaog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، روز سه‌شنبه، در گفتگو با «فاکس‌نیوز» در پاسخ به مجری که از او پرسید حمله‌ها تا چه زمانی ادامه خواهد داشت، گفت: «تا زمانی که من بگویم کافی است.»
او گفت آنها (حکومت ایران) هنوز تا حدودی توانایی جنگیدن دارد اما چیز زیادی برای آنها باقی نمانده است.
ترامپ در پاسخ به مجری که از او پرسید، اکنون وضعیت را چگونه توصیف می‌کند، آیا جنگ از سرگرفته شده، گفت: می‌توانید هر نامی روی آن بگذارید اما ما ضربه بسیار سختی به آنها زده‌ایم. ترامپ بار دیگر بر اهمیت باز ماندن تنگه هرمز تاکید کرد.
ترامپ در پاسخ به مجری که از او پرسید آیا جنگ از این فراتر می‌رود و اهداف مرتبط با انرژی ایران نیز در فهرست قرار دارند گفت: انرژی را برای بعد نگه‌داشته‌ام.
ترامپ افزود: امشب و فرداشب و پس‌فردا‌شب، ضربات سنگینی به آنها می‌زنیم و هفته آینده برای آنها خیلی بد خواهد شد. هفته آینده نوبت نیروگاه‌ها و پل‌ها است.
رئیس‌جمهوری آمریکا گفت: هفته آینده همه پل‌ها و نیروگاه‌های آنها را از بین می‌بریم مگر اینکه پای میز مذاکره بیایند.
رئیس‌جمهوری آمریکا پیش‌تر نیز این تهدید را مطرح کرده بود اما پس از آن اعلام شد که مذاکرات از سرگرفته می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/77082" target="_blank">📅 01:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77080">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/203d452dd4.mp4?token=EioGNZ-MDTMMVsFeZI9Kzg5WhYeM0E9Fqstw9HOUj3uk9g-0LYtD4HTc01PXCljG797rSug_Df_ratL1eWC3IaTRtXLAC_LVQ8qxHyK_36IHBaDxkhNyoaIpo3ui79ZL6f27UpAu-_xETB8UvGFJEwsVBeQVtTTgb00CkWPPANsZOoIcLyUJrkMck5hG53o_irhERcACsoAZCJNs6KFWucpB48CXrT90AetV4s9sbE8B7VVe6HH3u3Zv0fGaK9mkDYNK3d6-GubooyA9HUw8GhrnbIOLtPRLepbIz-KJP-aW66drF3atEC6Iv9sKXD29311aQRigiukQDL1QBRCEqg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/203d452dd4.mp4?token=EioGNZ-MDTMMVsFeZI9Kzg5WhYeM0E9Fqstw9HOUj3uk9g-0LYtD4HTc01PXCljG797rSug_Df_ratL1eWC3IaTRtXLAC_LVQ8qxHyK_36IHBaDxkhNyoaIpo3ui79ZL6f27UpAu-_xETB8UvGFJEwsVBeQVtTTgb00CkWPPANsZOoIcLyUJrkMck5hG53o_irhERcACsoAZCJNs6KFWucpB48CXrT90AetV4s9sbE8B7VVe6HH3u3Zv0fGaK9mkDYNK3d6-GubooyA9HUw8GhrnbIOLtPRLepbIz-KJP-aW66drF3atEC6Iv9sKXD29311aQRigiukQDL1QBRCEqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حال وش:
ویدئوهای جدید از حملات و انفجارهای شدید در محدوده تیپ ۳۸۸ ارتش در شهرستان بمپور
بامداد امروز چهارشنبه ۲۴ تیرماه ۱۴۰۵، ویدئوهای جدیدی از حملات و وقوع چندین انفجار شدید در محدوده تیپ ۳۸۸ پیاده مکانیزه نیروی زمینی ارتش، واقع در نزدیکی روستاهای ریکپوت و کلاهدوز از توابع شهرستان بمپور ، به دست حال‌ وش رسیده است.
به گفته منابع حال‌ وش: «در این ویدئوها، صدای انفجارهای پی‌درپی و نور ناشی از اصابت‌ها در محدوده این مرکز نظامی مشاهده و شنیده می‌شود. شدت انفجارها به اندازه‌ای بوده که صدای آنها در روستاها و مناطق اطراف نیز شنیده شده است.»
منابع افزوده‌اند: «حملات در چند نوبت انجام شده و ویدئوهای تازه، بخش‌هایی از لحظات اصابت و انفجار در محدوده تیپ ۳۸۸ ارتش را نشان می‌دهد.»
حال‌ وش پیش‌تر گزارش داده بود که حوالی ساعت ۰۰:۰۵ بامداد، دست‌کم هشت انفجار شدید در محدوده روستاهای ریکپوت و کلاهدوز شنیده شده و منابع محلی از هدف قرار گرفتن تیپ ۳۸۸ پیاده مکانیزه شهید حیدر شهرکی خبر داده بودند.
تا لحظه تنظیم این گزارش، اطلاعات دقیقی درباره میزان خسارات و تلفات احتمالی منتشر نشده و مقام‌های جمهوری اسلامی نیز درباره جزئیات این حملات اطلاع‌رسانی رسمی نکرده‌اند.
haalvsh
لوکیشن دریافتی تایید نشده:
GoogleMaps
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/77080" target="_blank">📅 01:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77079">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">در میان رگبار پیام‌های اهواز سه پیام متفاوت درباره جاده تهران-قم حوالی فرودگاه داشتم که نمی‌دونم چقدر درست هستند. هرچه صبر کردم پیام دیگری نیومد ولی اون اطرف کلی نقطه نظامی در بیابون هست که لابد کسی بهشون نزدیک نیست:
پیام ساعت ۲۳:۲۰
هم اکنون انفجار فرودگاه امام خمینی
صدای انفجار دور بود ولی لرزشش احساس شد
در پی مکالمه اضافه کرد: من اطراف فرودگاه هستم. چون اینجا بیابونه و نزدیک ترین لوکیشن بهمون همون فرودگاه هست اون  رو گفتم
پیام ساعت ۲۳:۲۳
سلام وحید جان جاده قدیم قم نزدیک اتوبان غدیر هستم صدای انفجار و لرزش اومد
زدیم ماشین رو بغل
پیام ساعت ۲۳:۲۶
سلام حسن اباد فشافویه نزدیک فرودگاه امام میشه صدای انفجار شنیدیم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/77079" target="_blank">📅 00:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77078">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NmFjaEn-4GpzAHgfCFFmGS56paLMw5AtR4QYkfIfjdyftXuGajtxZ0k91G-1TGVmgNCNcxiDkte7CqBhI1YWMk-59ztNQQqsp8MpcazbhdHDK0moABXKTIFT-dUJM6BaonRk8nTTQ58wUdHbXPqpwC2kDtOyMbfGdIJbpOxR70T9YlpIdQa_ZL9YHwVTtbibVH6Y6Fi1Ru8GqChX1LKBWRILrF1r-_V0tosti7vGf667FEuzeui-hfIKZgrQ1jZwDO83_vOdBbqgPwoTo_TTCcCZnoiqei8ZAftXH7UfJkz4CfVoNjExyYfXRTUDVjPa6pJfAezkqLd8L-Z73ld6RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستاد فرماندهی مرکزی آمریکا، سنتکام، [
در پستی تازه
] اعلام کرد نیروهای آمریکایی از ساعت ۴ بعدازظهر به وقت شرق آمریکا [یعنی دقایقی پیش]، محاصره دریایی کشتی‌های در حال تردد به بنادر و مناطق ساحلی ایران را از سر گرفته‌اند.
سنتکام در پیامی در شبکه اجتماعی ایکس، این اقدام را پاسخی به آنچه «حملات اخیر و غیرموجه ایران به کشتی‌های تجاری و خدمه غیرنظامی» خواند، توصیف کرد و افزود آمریکا جمهوری اسلامی را مسئول این حملات می‌داند.
بر اساس این بیانیه، در حال حاضر بیش از ۲۰ ناو جنگی نیروی دریایی آمریکا و صدها هواپیمای نظامی در سراسر خاورمیانه مستقر هستند و نیروهای آمریکایی «هوشیار، آماده و دارای توان رزمی» باقی خواهند ماند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/77078" target="_blank">📅 23:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77077">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">پیام‌های دریافتی:
اهواز ساعت ۲۳:۱۸ یه انفجار دیگه
ساعت 11.19 اهوازو زدن
۲۳:۱۹ ، اهواز صدای انفجار اومد
وحید جان سلام
دوباره اهواز روزدندساعت ۲۳:۱۸
ساعت ۲۳:۱۹ اهواز صدای انفجار
سلام وحید جان 11:19 اهواز، زدن
اهواز الان زد سه راه باهنر موجش اومد ۲۳:۱۹
همین الان ۲۳:۱۹ اهواز دوتا پشت سرهم
ما کمپلوییم! خیلی نزدیک بود فکر کنم لشگر ۹۲ زرهی بود!
سلام اهواز صدای انفجار نمیدونم کجا ساعت 11:19
اهواز  الان  ۲۳:۱۹
سلام ما باهنر اهواز هستیم با اینکه کولر روشنه و فوتبال میبینیم ولی صدای دو انفجار حدود ساعت ۱۱.۲۰ شنیده شد
و کلی پیام مشابه دیگر که بعضی‌هاشون فقط نوشتند: همین الان یا دوباره
که چون ساعت و دقیقه نمی‌نویسند نمی‌دونم کدوم باره.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/77077" target="_blank">📅 23:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77076">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">پیام‌های دریافتی:
صدای انفجار در بهبهان
بهبهان رو چند دقیقه پیش زدن خوابگاهمون کامل لرزید
سلام
چند دقیقه پیش شیشه های خونه وحشتناک لرزید
نمیدونم انگار تو شهر رو زدن
بهبهان زندگی میکنم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/77076" target="_blank">📅 23:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77075">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aKs65qAAb0FA3KST4gOBOW8pglIAOHiERouWLRAIdpbcNR7xe0YnQ48Nmg3JqdgipgbbfOlq1pqrRPpXJEBb4kmiqZTBeGVcipttSpRH3h3HQWQnUYh2h0xrTJIMq7oB9s6vWhm3J0JmLV2tJmDqxuQ5Us-d1ykLrWHw8Aclqtho-ft2zLngSGMj13EUJa9I3XPqlFBGpEMAqGTE0JI6dgA3A_Y7-RY6bIzKdHtphh_Y1Yk2LkeLNW0gM-dY5QpetHyh-L1-OUhzWkijWTj_BK8CAzUzOJs5ufCmeyeBL6vSD1A_zqSpXMgQQp_NRgKTyvt30uJR-kuqqldOhrONfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
امروز ساعت ۳ بعدازظهر به وقت شرق آمریکا [۲۲:۳۰ تهران]، نیروهای فرماندهی مرکزی ایالات متحده دور دیگری از حملات علیه ایران را آغاز کردند تا به تضعیف توانمندی‌های ایران که برای حمله به کشتی‌های تجاری در تنگه هرمز استفاده می‌شود، ادامه دهند.
این حملات در حالی انجام می‌شود که نیروهای آمریکایی خود را برای ازسرگیری محاصره دریایی بنادر و مناطق ساحلی ایران آماده می‌کنند. این محاصره از ساعت ۴ بعدازظهر به وقت شرق آمریکا [۰۰:۳۰ بامداد چهارشنبه] به اجرا درمی‌آید.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/77075" target="_blank">📅 23:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77074">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده:
بندرعباس ۲۲:۴۴ صدای چند انفجار
بندرعباس ساعت 10:45 چهارتا صدای انفجار اومد
چند انفجار ممتد ساعت ۲۲:۴۵ بندرعباس موجش زیاد بود
ساعت ۱۰.۴۶ صدای انفجار خیلی بددد تو بندرعباس
درود وحید جان بندرعباس سمت باهنر چهارتا انفجار شدید بود
🔄
سلام بندرعباس انفجارهای پشت سر هم سمت منطقه۴  ۲۳:۰۸
بندرعباس ساعت 11:08 دوتا صدای انفجار دیگه اومد
ساعت ۲۳:۰۸ بندرعباس ۳ انفجار
باز بندر رو زدن 23:08
دو سه تا انفجار مهیب ، لرزوند ساختمان رو
۲۳:۰۸ صدای دو انفجار شرق بندرعباس
سلام آقا وحید بندرعباس دوتا صدا پشت سر هم اومد ساعت 23:08 دقیقه
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/77074" target="_blank">📅 22:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77073">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">پیام‌های دریافتی:
اهواز ساعت ۲۲:۳۰ صدای ۲ انفجار
سلام اهواز رو الان زدددد
سلام وحید جان اهواز ساعت ۱۰:۳۰ صدای ۳ انفجار مهیب
همین الان اهواز صدای دوتا انفجار اومد
اهوازو زدن
درود وحید جان همین الان  صدای دوتا انفجار اهواز شنیدم. ساعت 22:31
اهواز ساعت ۲۲:۳۰
۳ تا انفجار
سلام وحید الان اهواز [رو] زد ۳ تاشو من شنیدم۲۲:۳۲
سلام اهواز [رو] همین دو دقیقه پیش دوبار زدن
سلام وحید جان اهواز همین الان دوتا صدا انفجار اومد. زمین لرزید.
ساعت ۲۲:۳۱ دوتا انفجار اهواز
سلام اهواز [رو] زدن خونه لرزید
سلام وحید اهوازو زدن ساعت ۱۰ نیم دو تا
سلام اهواز دو انفجار شنیده شد
وحید جون 2 انفجار اهواز 22:31
انفجار مهیب همین الان در اهواز صداا از سمت غرب اهواز بود. اونقدر شدید بود که زمین لرزید
سلام الان اهواز سه تا انفجار شنیدیم
سلام آقا وحید اهواز الان زدن صدای 2 انفجار نزدیک خونمون صدا مهیب بود
سلام وقت بخیر اهواز سمت کیانشهر صدا اومد ۲تا صدای زیاد
ب[ذ]ار فوتبال نگاه کنیم جون مادرت ۱ ساعت
🔄
۱۰:۳۵ دوتا انفجار دیگه اهواز
سلام اهواز [رو] زدن خونه لرزید
یکی دیگه زدن
۱۰:۳۵ دوتا انفجار دیگه اهواز
اهواز رو الان دوباره زد
هنوز اهوازو دارن میزنن ۲۲:۳۵
همين الان ١٠:٣٥ مجددا دو بار صداى مهيب توى اهواز
ساعت ۲۲:۳۴
۲ تا دیگه انفجار شدید اهواز
اهواز  . از ساعت ۱۰:۳۰ تا الان ۴ تا صدای انفجار
ما کوی نیرو هستیم اهواز
صدای دو انفجار اومد
حدود دو دقه پیش
وحید اهواز رو دوباره زد ساعت ۲۲:۳۵
سلام ساعت ۲۲:۳۴ سه انفجار در اهواز
همین الان اهواز برای بار چهارم انفجار مهیییب
با اینکه کولر روشنه ولی صداش خیلی بلند میاد
اهواز ساعت 20:37 چند انفجار پشت هم
۳ یا ۴ انفجار ، صدا از سمت ارتش 92 زرهی بود
صدا سمت  زرگان  کوروش کوی عابدی کم تر و بیشتر سمت کمپولو هست احتمالا لشکر باشه
سلام وحید جان.
تا ۲۲:۴۵ صدای ۵ انفجار شنیده شد که یکی از باقی بسیار صدای بلندتری داشت برای مایی که در نزدیکی پایگاه گلف و الحدید هستیم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/77073" target="_blank">📅 22:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77072">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EuZIkiz-br0czFeXQWqjIsZWwdteL7FIKvC0VIl74Q3WYKMplnXmVmFKU8rEgpZyYAXFaakaDrOkwMDl-0dkUCfiwP392eLotRG3qj5F12vHv0-Y5jm9LXtp5yhzvz3bx6iJmf_r8t3ISLwsQA7vl-MGoasLvveZpPcsPVl1nep0j3xVt5_U2sRYMNycTq1FoplBjVN7H6o76xnAT_zGwCLtLJ_sHCfaEN2sEkUJzBJW_74kuKPsR5lEAgS7N95En5HyDvrSrLeCpS4E-YJyIvBjInPGL3IXesQ3cQ7p5o-lgbMqF0zpekZZxKFM-kPbzeGjqDaOtOgpc_CSrxQgFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وبسایت اکسیوس به نقل از مقام‌های آمریکایی و اسرائیلی گزارش داد که رئیس‌جمهور آمریکا روز پنج‌شنبه در یک تماس تلفنی، به نخست‌وزیر اسرائیل گفت که این کشور باید خروج تدریجی نیروهایش از سوریه را آغاز کند و او را ترغیب کرد که اقدام مشابهی را در لبنان نیز انجام دهد.
بر اساس گزارش روز سه‌شنبه ۲۳ تیرماه این وبسایت، یک مقام آمریکایی گفت دونالد ترامپ به بنیامین نتانیاهو تأکید کرده که حضور نظامی اسرائیل در خاک سوریه تنش‌زا است و می‌تواند به تشدید درگیری‌ها منجر شود.
به گفته این مقام، ترامپ به نتانیاهو گفت: «آن‌ها شما را آن‌جا نمی‌خواهند. باید نیروهایتان را خارج کنید» و افزود که همین موضوع درباره لبنان نیز صادق است.
در مقابل، دفتر نخست‌وزیر اسرائیل اعلام کرد: «نخست‌وزیر بر ضرورت ایجاد مناطق حائل امنیتی در امتداد مرزهای اسرائیل تأکید کرده است».
این تماس، یک روز پس از دیدار رئیس‌جمهور آمریکا با همتای سوری خود، احمد الشرع، در حاشیه نشست ناتو در ترکیه انجام شد.
به نوشته اکسیوس، سه ماه مانده به انتخابات پارلمانی اسرائیل که برای بقای سیاسی نتانیاهو حیاتی است، بعید به نظر می‌رسد او گام‌های مهمی برای عقب‌نشینی نیروهای اسرائیلی از مناطق تحت کنترل در سوریه بردارد یا فراتر از آنچه پیش‌تر در لبنان پذیرفته، با خروج بیشتر موافقت کند.
ارتش اسرائیل در حال حاضر بخش‌های وسیعی از جنوب لبنان و جنوب سوریه را در اختیار دارد.
اعضای ارشد دولت اسرائیل خواهان کنترل نامحدود بر این مناطق هستند و برخی حتی از ایجاد شهرک‌های یهودی در آن‌جا حمایت می‌کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/77072" target="_blank">📅 21:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77071">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sRREsk1xNRNvsO8-iZVUfimELM-4nqxfE2T5jFFzMvi_kq3R4d_fAYFYFIJfxOeAbysXg9FeTRneODB8b4GnJ4Deh7HgxhSNKt5JZsQfcwXrx8TZelY2ZsRYuWBjtPGC4vsFQz6EUBkw8CBiJn5YIghZ6K_J0PWjNyL2oLZomkESRsNfPn1vuU10-rWMPpgokZRsTt39PhQm4OzX0YcCcNGNYoPd6dNm5TOVbEX-kwV6ugKz7va3tlhYbZWNSfUkB7hd2F8kC3CykO6dnc59A_oPf84kFk1g7O1zJGPNj1dGeavqXwkGZdjRRGPQ15TlKf3cKAiad6BcvSm00vSunw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه عربستان سعودی روز سه‌شنبه ۲۳ تیرماه با «محکومیت و انزجار شدید» از حملات ایران به چند کشور عربی، تهران را «مسئول عواقب ادامه این حملات ظالمانه» خواند.
در بیانیه این وزارتخانه، از هدف قرار گرفتن تعدادی از پاسگاه‌های مرزی کویت، یک سکوی حفاری دریایی متعلق به شرکت نفت کویت و حملات به سرکنسولگری کویت در شهر بصره عراق خبر داده و با اشاره به حمله ایران به اردن، بحرین، قطر و دو نفتکش اماراتی هنگام عبور از تنگهٔ هرمز، از «تداوم تهدید امنیت و ثبات منطقه توسط ایران» انتقاد شده است.
وزارت خارجه عربستان در این بیانیه «مخالفت کامل» خود را با آنچه «نقض حاکمیت کشورهای برادر توسط ایران، ادامه رفتار بی‌ثبات‌کننده آن در امنیت منطقه، و نقض اصول قوانین بین‌المللی، منشور ملل متحد، منشور سازمان همکاری اسلامی و اصول حسن همجواری» خوانده، اعلام کرده است.
عربستان ضمن درخواست برای توقف حملات ایران، بر همبستگی کامل ریاض با کشورهای هدف قرار گرفته، تاکید کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/77071" target="_blank">📅 21:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77070">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VObAj39eKiiIfFyZ8fhbO4oqMH_onX329QVF47HpM6MbxL7TM55fK4X1MuxdM3eV2Ge2CgPAiaTOblY-w2QH69ukX8vyh79rv55VRqIRSQTgkRh7mt3ZsdatkJ6SQbfvkSlEQZf46LpzTXeH2g5lWS9t3xB1BC41BVUfyfL14oPTNCX9dDI2LOs68jb4U4JozYVz4AeCzrTlVvqyV3Zqj2r1-WjhuHdj7iC_tGjZ1Su0-mox-Jc4Xc-X4oA6-aHYQkF_90Ud-_HRXZbKaBfQns4tP3rCj9z30-Qn1mQ8E0vYaPqLAYjMBwR5krg2yWhyw7hMMag3KowAcu-YZWpb0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور آمریکا عصر سه‌شنبه ۲۳ تیرماه و ساعاتی قبل از آغاز رسمی بازگشت محاصرهٔ دریایی بر بنادر و کشتیرانی ایران گفت هیچ‌کس نباید برای عبور از تنگهٔ هرمز عوارض یا هزینه‌ای دریافت کند.
دونالد ترامپ در یک نشست خبری همراه علی الزیدی، نخست‌وزیر عراق، در کاخ سفید گفت که پس از اعلام قبلی‌اش مبنی بر دریافت ۲۰ درصد عوارض بر کشتی‌های عبوری از تنگهٔ هرمز، کشورهای مختلفی با او تماس گرفتند و گفتند به‌جای دریافت عوارض برای عبور از تنگه، مایل‌اند در آمریکا سرمایه‌گذاری کنند.
او با اشاره به کشورهای حاشیه خلیج فارس گفت این کشورها قرار است در آمریکا سرمایه‌گذاری کنند و فکر می‌کند این موضوع راه‌حل بهتری در مقایسه با دریافت عوارض است.
رئیس‌جمهور آمریکا با تمجید از علی الزیدی گفت اگر عراق به حفاظت نیاز داشته باشد، ما در کنار آن خواهیم بود.
او گفت ما در بخش نفت با عراق همکاری قوی خواهیم داشت و به زودی آن را اعلام خواهیم کرد. نیروهای آمریکایی عراق را ترک می‌کنند و شرکت‌های آمریکایی وارد می‌شوند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/77070" target="_blank">📅 20:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77069">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f1ccf9a2d5.mp4?token=HJv7IhQNh6GkCZTyZZ8sabBmQCZUHcWatRo6B-U20TNXOzmuUhlM7h2U2nhBTq53lMmBeT5E3QU7ma26rF-6dfVDdVP95DjPFEFDdw-GH7jmaaXRlTZ6xqxmJme5c_6bDwaHpqBG5x53U9rrc7HlOvmdO3buDsWvb8jomUCp-P6NMuX8vqWZLa8f8Vt-PdZ1eB-qtO2nhA-H-r9EhS8BslqW1KEgKq-cfbJ6BaFpf1TC32jcGQSuQvqNJ2y3ldPt7YIei58IB4d8KA9ExGJMBfoYo7cpsNPFi01e3QVY2pKUQwEfNVUUdX0DQBqI7QbnIWfQ3w23WSJEONwOdWOpgA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f1ccf9a2d5.mp4?token=HJv7IhQNh6GkCZTyZZ8sabBmQCZUHcWatRo6B-U20TNXOzmuUhlM7h2U2nhBTq53lMmBeT5E3QU7ma26rF-6dfVDdVP95DjPFEFDdw-GH7jmaaXRlTZ6xqxmJme5c_6bDwaHpqBG5x53U9rrc7HlOvmdO3buDsWvb8jomUCp-P6NMuX8vqWZLa8f8Vt-PdZ1eB-qtO2nhA-H-r9EhS8BslqW1KEgKq-cfbJ6BaFpf1TC32jcGQSuQvqNJ2y3ldPt7YIei58IB4d8KA9ExGJMBfoYo7cpsNPFi01e3QVY2pKUQwEfNVUUdX0DQBqI7QbnIWfQ3w23WSJEONwOdWOpgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، روز سه‌شنبه ۲۳ تیر، در نشست خبری مشترک با نخست‌وزیر عراق در کاخ سفید، اعلام کرد که خاورمیانه در حال تجربه وحدتی بی‌سابقه است و دیگر خبری از ترس و وحشت ناشی از «قلدری» ایران در منطقه نیست.
ترامپ با بیان اینکه ایران پیش‌تر با رویکردی سلطه‌جویانه، کشورهای منطقه از جمله عراق را تحت فشار قرار می‌داد، تاکید کرد که اکنون توان نظامی این کشور درهم‌کوبیده شده و آن فضای رعب و وحشت از میان رفته است. او در بخشی از سخنان خود به سرکوب معترضان در ایران اشاره کرد و یادآوری کرد که آن‌ها ۵۲ هزار نفر از معترضان را به قتل رسانده‌اند.
رئیس‌جمهوری آمریکا در پایان ضمن اشاره به نزدیکی کشورهای منطقه به یکدیگر، نخست‌وزیر عراق را به عنوان یکی از رهبران بزرگ آینده در خاورمیانه توصیف کرد و افزود که این اتحاد منطقه‌ای، در سایه پایان یافتن دوران سلطه‌گری ایران، اکنون به واقعیتی دست‌یافتنی تبدیل شده است.
@
VahidOOnLine
دونالد ترامپ در نشست خبری با علی الزیدی، نخست‌وزیر عراق، در کاخ سفید گفت: «نخست‌وزیر عراق در انتخاباتی پیروز شد که بسیاری تصور می‌کردند فرد دیگری برنده آن خواهد شد. من هم در این موضوع نقش داشتم و برایم مهم بود کسی روی کار بیاید که بتواند این مسئولیت را به‌خوبی انجام دهد. اکنون یک قهرمان جدید و فوق‌العاده داریم و حضور او در کنار ما مایه افتخار است.»
ترامپ افزود: «شرکت‌های نفتی آمریکا با حجمی بی‌سابقه وارد عراق می‌شوند، با این کشور شراکت می‌کنند و همکاری گسترده‌ای خواهند داشت. روابط ما اکنون به سطحی رسیده که دیگر نیازی به حضور نظامی آمریکا در عراق نیست. ما برای کمک به عراق حضور داریم و اگر لازم باشد از آن حمایت خواهیم کرد، اما فکر نمی‌کنیم چنین نیازی پیش بیاید.»
او درباره جمهوری اسلامی گفت: «ایران رقیب اصلی عراق بود و بار سنگینی بر دوش این کشور گذاشته بود، زیرا قلدر خاورمیانه محسوب می‌شد. اما اکنون ایران تا حد زیادی تضعیف شده و توان نظامی آن تنها بخش کوچکی از چیزی است که چهار ماه پیش بود. این وضعیت به عراق آزادی عمل بیشتری داده و یکی از دلایل ورود گسترده شرکت‌های نفتی آمریکا به عراق نیز همین موضوع است.»
@
VahidOOnLine
ترامپ با یادآوری دوران فعالیت خود به عنوان یک چهره غیرنظامی، گفت: «من همیشه می‌گفتم به عراق نروید و به آن حمله نکنید».
او با انتقاد از این مداخله نظامی و با اشاره غیر مستقیم به ایران، افزود: «صادقانه بگویم، آن‌ها به کشور اشتباهی حمله کردند و آسیب بسیاری به بار آوردند».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/77069" target="_blank">📅 20:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77068">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dl7TlEpQ6arbGQ0wDSA_cBwwqsjqCO8KbJfiwZTc4_Ap6Pq9vy1EqPO6dDLWtHBaA4vvYQBtDBghS3QcIEmeKi_kLOs_C5tyPeLsnyePaYkZ1xdYMO2kVtm-bb_BNhN5bVNDMVs8HlASK3zTFwtpOFXEETunPXjCfwqzKahNgTpqMcET6EL4pfzPQgraaXJEA8nsWZ2JOPn_-Ot4lus9KmWf7MPnGXbdbdU8U6ut7vWwvSp8pHNr90AIPCxSGQMoGcwLCF2OrWlw5hL0Pkzm43eTYLAxjedo5oUX1OS4TwNS4c1SnW7CSSEf_b9mtvrjOERvoc3STsskDiuQ9JrY_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر دریافتی: صدور هشدار خطر در کویت، همین الان
رسانه‌های ایران عصر سه‌شنبه بدون بیان جزئیات بیشتر از شنیده شدن صدای انفجار در اندیمشک و جزیره قشم خبر دادند.
صداوسیمای جمهوری اسلامی به نقل از استانداری هرمزگان گفته که ساعت ۱۹ به وقت محلی، «نقطه‌ای» در جزیره قشم هدف حمله آمریکا قرار گرفت. صدا و سیما همچنین از شنیده شدن صدای انفجار در اندیمشک خبر داد.
هم‌زمان، ستاد کل ارتش کویت با صدور پیام هشداری از رهگیری «اهداف هوایی متخاصم» در این کشور خبر داد.
در بیانیهٔ ارتش کویت با درخواست از شهروندان برای رعایت دستورالعمل‌های امنیتی گفته شده که صداهای انفجار احتمالی ناشی از فعالیت پدافند هوایی در رهگیری حملات متخاصم است.
خبرگزاری فرانسه هم از شنیده شدن صدای انفجارهایی در کویت خبر داده است.
@
VahidHeadline
سپاه پاسداران در بیانیه‌ای حملات شامگاه سه‌شنبه به «مواضع دشمن» در خاک بحرین و کویت را تایید کرد و گفت عملیات «نصر۲»، پاسخ به حملات عصر سه‌شنبه آمریکا به تعدادی از ایستگاه‌های ساحلی نیروهای مسلح جمهوری اسلامی بوده است.
در این بیانیه آمده است، در صورت تکرار حملات، مقابله به مثل جمهوری اسلامی ادامه خواهد داشت و این «تجاوزها» نتیجه‌ای جز تاخیر در بازگشایی تنگه هرمز ندارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/77068" target="_blank">📅 19:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77067">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sb_4E3daVp9ApfhYD9aRq9WShLsMOOsUnepi34EwlfvHVbp4Gz9kIlKnLxNI9Kj29eRDS5M-fRL2cVJt5sqYNa-OelyRgFQjeBU0pFVn_zCeU0CgyvoILmgtLuAIBMMwvkBtkirW8gwAKHckZZRhdcaO4ZPDCrGknh8C9hireI9YTiUIcvoo8dUMTL7gP2lRhfibj--grkorh3FWoM1dMA9FRwLozdqczmh634N1IpyK1Z1ZitBMvFnynxFuxGxlcGXPcBmpbBFFI6tizlTB6xGxuruZ25E-SvGQCMC2gb3-OyfE317sA8LAZkRkKJM4jPQo9Nb0c5V8gvuTikN1dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: تنگه هرمز به روی تردد همه کشتی‌ها، به‌جز کشتی‌ها و محموله‌های مرتبط با ایران، باز است
ترجمه ماشین:
نفت به لطف قدرت شگفت‌انگیز ارتش ایالات متحده، بیش از هر زمان دیگری در جریان است. درود ویژه به وزیر جنگ، پیت هگست، رئیس ستاد مشترک نیروهای مسلح، دن کین، و فرمانده ستاد فرماندهی مرکزی ایالات متحده، دریاسالار برد کوپر. به لطف آن‌ها و همه اعضای قدرتمندترین ارتش جهان ــ با اختلاف بسیار زیاد ــ تنگه هرمز به روی تردد همه کشتی‌ها، به‌جز کشتی‌های ایران، باز است؛ و این به‌دلیل رهبری دروغگو، خشونت‌طلب و بدخواه ایران است که این کشور را به مسیر نابودی کامل می‌کشاند.
بنابراین، ما یک محاصره کامل خواهیم داشت، اما فقط علیه کشتی‌هایی که به بنادر ایران رفت‌وآمد می‌کنند یا هر چیزی مرتبط با محموله‌های ایرانی حمل می‌کنند.
بر اساس گفت‌وگوهای بسیار سازنده با رهبران خاورمیانه،
تصمیم گرفته‌ام «هزینه بازپرداخت ۲۰ درصدی به ایالات متحده» را با توافق‌های تجاری و سرمایه‌گذاری جایگزین کنم که کشورهای مختلف حاشیه خلیج فارس در ایالات متحده انجام خواهند داد.
این سرمایه‌گذاری‌ها عظیم خواهند بود، اما در عین حال برای خود آن کشورها و آینده‌شان نیز فوق‌العاده سودمند خواهند بود.
همان‌طور که همه می‌دانند، ما بیشترین میزان سرمایه‌گذاری دلاری در ایالات متحده از سوی هر کشوری در تاریخ را داریم، اما این سرمایه‌گذاری‌های جدید آن رقم را حتی بزرگ‌تر خواهند کرد و شاهد سرازیر شدن کارخانه‌ها، تأسیسات و تجهیزات به ایالات متحده در سطوحی تاریخی خواهیم بود؛ امری که میلیون‌ها شغل پردرآمد دیگر برای آمریکایی‌ها ایجاد خواهد کرد!
آمریکا دوباره در حال پیروزی است؛ پیروزی‌ای بی‌سابقه. دوران کشته شدن صدها هزار نفر، از جمله ۵۲ هزار معترض، به دست ایران به پایان رسیده است و مهم‌تر از همه، ایران هرگز به سلاح هسته‌ای دست نخواهد یافت!
از توجه شما به این موضوع سپاسگزارم.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/77067" target="_blank">📅 18:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77066">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4730c53847.mp4?token=B7-Y19v4pJFdo7tDkXYOIfGtJhqTQZBHq_EIlYxdaRJ0PfcGOg7m7YVUE-09_yxdFZNr3QJaPbW63Omali7T365rUTIRVgCXmbNnyNkV3Rzn1T-Bh6M4bqsJK5QCilFhT9PwFEr55QApsr__Y4211-JcHTHo-BA2ch_TrM2lDhwL24wxEiNltkUN3zhvXfmGANB9cLJfO6iM0N6nwZGu8cnhrHw9jcqVqgvxZs54BweVbyN-psHWaOrE5Ru_5OM4WjtAkGl8W0y9klfZtqqX1yHkEPElqNJZiR5cb4-3FRnmm-JvuOeE8SyPxSaeCv4KZ8LZ4lnCmEmHLhkpG3mYaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4730c53847.mp4?token=B7-Y19v4pJFdo7tDkXYOIfGtJhqTQZBHq_EIlYxdaRJ0PfcGOg7m7YVUE-09_yxdFZNr3QJaPbW63Omali7T365rUTIRVgCXmbNnyNkV3Rzn1T-Bh6M4bqsJK5QCilFhT9PwFEr55QApsr__Y4211-JcHTHo-BA2ch_TrM2lDhwL24wxEiNltkUN3zhvXfmGANB9cLJfO6iM0N6nwZGu8cnhrHw9jcqVqgvxZs54BweVbyN-psHWaOrE5Ru_5OM4WjtAkGl8W0y9klfZtqqX1yHkEPElqNJZiR5cb4-3FRnmm-JvuOeE8SyPxSaeCv4KZ8LZ4lnCmEmHLhkpG3mYaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر اسرائیل روز سه‌شنبه ۲۳ تیرماه هشدار داد که اگر تهران حملهٔ جدیدی به کشورش انجام دهد، اسرائیل با تمام قدرت به ایران ضربه خواهد زد.
@
VahidOOnLine
ویدیویی که دفتر نتانیاهو منتشر کرده، ترجمه ماشین:
ما برای هر سناریویی آماده‌ایم. فقط یک چیز می‌توانم به شما بگویم... نه، این را به رهبران ایران می‌گویم:
اگر به ما حمله کنید، روی آرامش حساب نکنید. تصور نکنید آنچه در گذشته رخ داد، دوباره به همان شکل تکرار خواهد شد؛ زیرا این بار، تکرار گذشته نخواهد بود.
حمله قبلی به‌اندازه کافی قدرتمند بود؛ حمله بعدی بسیار قدرتمندتر خواهد بود.
دورانی که کسی به ما ضربه بزند و ما با ضربه‌ای چند برابر پاسخ ندهیم، به پایان رسیده است. این کار را در برابر محور شرارتِ ایران انجام دادیم و در برابر هر کسی که به ما ضربه بزند نیز به همین مسیر ادامه خواهیم داد.
روش ما همین است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/77066" target="_blank">📅 17:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77065">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWY7cCTMRyszN-bOuSvGwtI3jCIPu3rhmq1Qu-x0MCcsHBQzcEUFQWu3BNRvDaA4ic3JWn5W_vO7thBWBjf8k6zXrgAJ-9M1SNE02UM86nv6omlxQgig7sqR3RQbVe0ki8gMeYlgHysJMOtLffSKiXtMU_hCZoLOlXiebiBJX8RjYC_I5DfhNExmqGj0lAh_L8GbDHKGXXZuK4AIWtByjlJu2S5B7_i5vkq4hm4zbLu4LS8AmSkewzCDKswLvYAsvLNl5ZGHK1d538QgjWgN0JwWt_jj7ndmJ4apPsAzQ3ljmKhrKG324B0ZuDvdpTuj0cX002NFtfQoR_ZNJX0pdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان به نقل از یک منبع ارشد در تهران گزارش داد که اگر دونالد ترامپ تهدید خود برای حمله به تأسیسات زیرزمینی موسوم به «کوه کلنگ» را عملی کند، جمهوری اسلامی «پاسخی ویرانگر» خواهد داد. این تهدید در حالی مطرح شده که کوه کلنگ طی سال‌های اخیر به یکی از مهم‌ترین و امن‌ترین مراکز هسته‌ای ایران تبدیل شده است.
دونالد ترامپ، رییس‌ جمهوری آمریکا، روز گذشته در گفت‌وگویی رسانه‌ای اعلام کرد که واشینگتن یک مجموعه زیرزمینی عمیق در ایران را به‌دقت زیر نظر دارد. او مدعی شد هرچند در حال حاضر نشانه‌ای از فعالیت آشکار در این مجموعه دیده نمی‌شود، اما آمریکا ممکن است به‌زودی «ضربه‌ای سخت» به دهانه ورودی این مجتمع وارد کند.
کوه کلنگ گزلا که در رسانه‌های غربی با نام Pickaxe Mountain شناخته می‌شود، در استان اصفهان و در فاصله حدود یک‌ونیم کیلومتری از تاسیسات غنی‌سازی نطنز قرار دارد. به گفته کارشناسان، این مجموعه به دلیل عمق زیاد و استقرار در دل سنگ‌های سخت گرانیتی، یکی از مقاوم‌ترین تاسیسات زیرزمینی ایران به شمار می‌رود.
برآوردهای فنی نشان می‌دهد سالن‌های زیرزمینی این مجتمع در عمقی بین ۸۰ تا ۱۰۰ متر و در برخی نقاط تا حدود ۶۰۰ متر حفر شده‌اند؛ ویژگی‌ای که آن را حتی از سایت غنی‌سازی فردو نیز عمیق‌تر می‌کند. به همین دلیل، برخی تحلیلگران غربی از این مجموعه به‌عنوان «دژ هسته‌ای» ایران یاد می‌کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/77065" target="_blank">📅 16:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77063">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OZI3d-YuF_33csnXziO6TL-NKFLNrCZz-vvDsVG_3oIYI7fo51_3Mj9amB9E5ZtBgbxKBRgKETSSP27PUkx9y-cr4dyhqEgENUdfsg4cyEW3wK7kcmGriKEX_X9NynGgcqmSl5cH8fTb9WS7Y1-pDYvQDqhH_uj7ZSu0Py6d7EzF9pmAYH2yPoNDr4qV3yJURmvUvrwk1s7pcjuiYj3hzTo2Bff2lAgjURRYeEaP7L8wlS4EjOCmIYFQYAwlhX35ffFSHwRFAmbNFzpC4wEzKRDMQf07_G6EvZjg2QMNrMKmbUq_URxxXejEXNLQkSLvTqycVJel_2UpdfOd9iBguA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MgBUW27JUEXSneZ-j4hAtrlywuRcDIoJS-I7lWpBf4KkyweZLdGzhOymBc4WfRvlowQMDZER-5G8TMSrFQYJPNN-5Hp43X7nUXFPWdUi3oXdwn_mM6C-A4bDsF57WtqLrVSqRcYv4kS904PwuTwgYAuC9zG-ox-YuWAtdae8aqe5mWuRKCJqQFUsmadTPd0JkEsk3PZo7DMu4LrTY0gC7i4GHC1Y5v_RJieuEnbUiPNzZFxGuky5qLYSq29tXwGcGt6cjYi4JGTJfRJzxUrm7rFRvqM3AJNarAXGop05dOOn-DfGiXjTgNjCO7RzBCB0sMA35fJOCLNsfZyjCeo_YA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قیمت نفت در بازارهای جهانی روز سه‌شنبه ۲۳ تیرماه و همزمان با تشدید درگیری‌ها میان جمهوری اسلامی ایران و ایالات متحده آمریکا در تنگه هرمز از ۸۵ دلار گذشت.
@
VahidOOnLine
قیمت ارزهای خارجی در ایران در روز سه‌شنبه ۲۳ تیرماه افزایش قابل توجهی پیدا کرد و نرخ برابری دلار آمریکا به ۱۸۴ هزار تومان رسید.
قیمت سایر ارزهای خارجی هم افزایش یافتند و قیمت یورو به حدود ۲۱۰ هزار تومان رسید.
در کنار ارزهای خارجی، قیمت سکه طلا هم به ۱۸۰ میلیون تومان رسید.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/77063" target="_blank">📅 16:28 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77061">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/j71vt8d4FHFJzslQVuc82j22ad72SCp3SNJTwOf7JYscQLG8hWycw7DpNJcpSTK5M8rQRBX4Z1sUBc4qdrnkrpgg5AyLnL7xdk3UhSUKQtTwpzTy8-dGPXFcE40I8NVv3jzoThn_YO3W-funi5ev5vexcV7mx-eVSGyJblZS8sOtHMX8lAuDj2Z1YuDDac6m4ftZXCt7jZzDX73m1kmHXsW1mFojZekepN4N_RqgfuWjVWkLoBFp8MYT3bQPqBwykdruvwol52HZ7fxp0OjhOww_GpkI---z2ow08LjVnlUAfaRLTbzXFpsBfdaD5cbnNA3yK8_k0hY7C9mrMJM01A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/thw08b_yuwLwetbQJOFRp7n-3Fy_6YUwK5rGwekYvGefK_AJL-DtxLP9VBK2_cQl4q8z_IFAimkiavvEDvzaMwVoTWFroNLsWW_mEgrfCVPxQOOq09T_DS5nj9OUfgOlm_B9rYlux_b9f_eM5OP_uski-ulilgVGFPRE8ynhRQUP2QbiLf0hfAuz_iQKFz67bSAlinb40-JhDBwnsl7OFPPIqia3KsYJSlta_TaVQPA-sd4yVEt0u1NvIUg13AYdl6-cTDl3BIt7TLEhYjN41UCBEtffehdmyJajbVI1tkuU3ViYgwI3K8i-aLAr6ho9My2zfJVWUhnp0jynWoo-xQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روزنامه آمریکایی نیویورک‌تایمز در گزارشی اختصاصی که روز ۲۲ تیر ۱۴۰۵ منتشر کرد، از تلاش چندساله سرویس اطلاعاتی اسراییل برای جذب محمود احمدی‌نژاد، رییس‌جمهور پیشین ایران، به‌عنوان یک عامل اطلاعاتی خبر داد؛ طرحی که هدف نهایی آن، به گفته این روزنامه، نصب او در…</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/77061" target="_blank">📅 16:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77060">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mtB9NHMNOUa8LVsAzF3crPXRL0XoMw9y3e9GBPNHLOA5JAJPdfkHT-LAIoIl4G7tzIi0sNgV35HVOV94uQdZj8qKecujDs4asqBI0N6cWtS4cbZWdlr1kkYcG0mA8OT1Lyb7OeojlBe74I9L43AdnQ7fgSL-grrQ7SdrftOIOS_r0AlI89u82YVTkPYHplkjjy5RrVeDr7DfjVjgPvUYUbNEiFgBLjp59BTQhoDV3c9qJw9s4TxanidcnwJPB_aVt0NdOjIsYzeYr3Ju0os-ntvlaEgyCc4JVQoWv6NeI5mK_Q-HndpMygbPRZFZT3EWvo2Njmv3sZmqE30YaDVyNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستگاه قضایی جمهوری اسلامی صبح سه‌شنبه ۲۳ تیر از اعدام دو نفر به اتهام «بغی و قیام مسلحانه علیه نظام جمهوری اسلامی»، خبر داد و و آن‌ها را که آن‌ها را از اعضای گروه داعش معرفی کرد.
قوه قضاییه نام این دو را محی‌الدین عبداللهی و حسین پالانی اعلام کرده و می‌گوید آن‌ها اعضای یک «هستهٔ وابسته به داعش» بوده‌اند که در ارتفاعات بمو در نوار مرزی ایران و عراق و پس از یک درگیری که به کشته شدن سه عضو سپاه نیز انجامید، بازداشت و محاکمه شدند.
جزئیاتی از روند این محاکمه منتشر نشده و شرایط برگزاری دادگاه و دسترسی آن‌ها به وکیل و دادرسی عادلانه نیز مشخص نیست.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/77060" target="_blank">📅 16:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77059">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ddf664d6f9.mp4?token=ar7yHKcn7jHn07nmGb1ZD_2QsLG0FegK5occFcFHstr3faAW7Ugq6Q7MkYAi4bVgdXvNtVm0OXSAnGNy-T3aw8d-UYJlrYS4l_M8SJKNXl0vPTS14WYHSxXoIirxleiRWlzfFft1gGeSFbrBYGV85NSxI2pNItQkprCwblHGyTdRyRHJYbdibovRN3fQxuNea_K3KPvjzDnP_qk0kWHALEqh6NqWyjNBRm-GN3dYjVMyRly9Fk5jl5AZFM6WNZX1L-WtOUNogmQCa4eyhVDH54QViP9xwUQ2GbVXDngx-KUKaEdXfST-WEuMng7rcmKR60GskfAqXbL7lmAUYvM5UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ddf664d6f9.mp4?token=ar7yHKcn7jHn07nmGb1ZD_2QsLG0FegK5occFcFHstr3faAW7Ugq6Q7MkYAi4bVgdXvNtVm0OXSAnGNy-T3aw8d-UYJlrYS4l_M8SJKNXl0vPTS14WYHSxXoIirxleiRWlzfFft1gGeSFbrBYGV85NSxI2pNItQkprCwblHGyTdRyRHJYbdibovRN3fQxuNea_K3KPvjzDnP_qk0kWHALEqh6NqWyjNBRm-GN3dYjVMyRly9Fk5jl5AZFM6WNZX1L-WtOUNogmQCa4eyhVDH54QViP9xwUQ2GbVXDngx-KUKaEdXfST-WEuMng7rcmKR60GskfAqXbL7lmAUYvM5UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منتشر شده در منابع حکومتی:
'حمله هوایی آمریکا به ساختمان سازمان تنظیم مقررات و ارتباطات رادیویی در بندرعباس'
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/77059" target="_blank">📅 16:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77058">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bMLq8AoXD9xxRj5-DlJwmhuVPvfN86WsR22taWcUaFtS7oSQM48-MJ6XLvdM2splLyLD7cn4Kl8670zi8GY19tg2rPtlQnIhdMR5qfaW7WQKeYDtvSBP9-D1S26ih-07TeXhwu2ZkJ66kMdbAoLvsB67ndO6wcsPHU1Y48BnnD444B00DAMfcthIHfO79jxF9maDG6VWfj_KgReJJElUWX1Bec3EFfv49aCGccVtXC-o6ieHzcPEIZ5OUKRtNy1O1ow5lGbqNkMXGSiVt5dXXbObSspZN6C7xo5pMgDesrxfOMV0ad69cVsnYRreel8n2LLFAZEYNEYLuqPzbS-qUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس دریافتی با شرح: 'مرکز آماد و پشتیبانی دریابانی نیروی انتظامی بوشهر محله بهمنی، سه‌شنبه ۲۳ تیر'
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/77058" target="_blank">📅 15:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77054">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sLjxFJv_y6YCD-ekL9Sn4W-xGWB5xH0Wi8Tpm4FMqi6IC-cjZbueHk4c_M2qLvtPPWgtCDqjqD8fZDwXEKKcwS9AL1p5BAVgAhjh87TvyQd5Q1EKN2UJVwjpkY7wYFYe2min8BjTj9Ws1x3RR6CEUOhL_kJYeLq5KvCr15QlNFdHkj2HdV7M3x-_KmeAFv_Ov-5kaSO-uR9mT6BX2SBDI2Xzgihkd19UJ2w9640mbqnybfguW_B0nLj1sDSPikQz4-48yzdxJ4hPXiPOgb4zmqHCEQYcVouvicMqESGEEIwWE-Wyw0X0NGXlbDqtedF9OFTbSnAzBolNoOv0SCw3Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/31d98f9c91.mp4?token=pJuTPeemBsoyoMvtZxu5ucwkqVXKKGmqrLF29rzjUjjG1n3WR4VKI2Hr7VPXQGjUoaywDtP0pNsL8fT6oOw832nIvjsr_V3hJlzrhqJKoQcSWBZutNSLq3ygiiypzHCCxhKzRWv_9nUCSb1tWo6nT7l1QQmRxBvGNI5TeVKfmwfURiSJoY-2wliNaNXN-00rbJROADa1yV0EIBXEATSoCSFN0qOhCvSaYaLEXJFuOGmqBHPBIiAgQJ6XUMbDPhb4YW1ip7bVlSg1DIEjQVAZk-xcppI7UY9pEiE_lv-Q66mwbLjDsUPB7ISuohrKypzZIgMag3L6CoKsruehNgQaEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/31d98f9c91.mp4?token=pJuTPeemBsoyoMvtZxu5ucwkqVXKKGmqrLF29rzjUjjG1n3WR4VKI2Hr7VPXQGjUoaywDtP0pNsL8fT6oOw832nIvjsr_V3hJlzrhqJKoQcSWBZutNSLq3ygiiypzHCCxhKzRWv_9nUCSb1tWo6nT7l1QQmRxBvGNI5TeVKfmwfURiSJoY-2wliNaNXN-00rbJROADa1yV0EIBXEATSoCSFN0qOhCvSaYaLEXJFuOGmqBHPBIiAgQJ6XUMbDPhb4YW1ip7bVlSg1DIEjQVAZk-xcppI7UY9pEiE_lv-Q66mwbLjDsUPB7ISuohrKypzZIgMag3L6CoKsruehNgQaEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنا برگزارش شهروندان از حدود ساعت ۱۲:۴۵ بار دیگر به نقاطی در
#بوشهر
حمله شده و بیش از ۱۰ انفجار رخ داده.
تصاویر دریافتی، سه‌شنبه ۲۳ تیر
#Iran
Vahid
از بوشهر پیام میدم
ساعت ۱۲ و ۴۴ دقیقه صدای انفجار امد اما کم بود
سلام وحید جان
ساعت 12:45 دوباره بوشهر رو زدن
بوشهر ساعت ۱۲:۴۵ ظهر منطقه بهمنی صدای انفجار خیلی نزدیک بود. خونه لرزید
همین الان ساعت ۱۲.۴۲ بوشهر منطقه بهمنی رو زدند(احتمالا پایگاه هوایی ارتش یا پایگاه دریایی سپاه ریشهر) زدند. صدای دو بمب شنیده شد.
سلام بوشهر ۱۲:۴۷ شدیددد صدای انفجار میاد.
درود وحید جان ،بوشهر الان دوتا محکم زدن
الان بوشهر و زد ۱۲:۴۴
به نسبت اخیر صداش نزدیک بود پس میشه حدس زد فرودگاه بوده دوباره زد ۱۲:۴۷
الان زد باز ۶/۷ تا انفجار بزرگگگ کارخانه جاته چون خیلی نزدیکه ۱۲:۵۴
۱۲:۴۷ بوشهر حدود ۴، ۵ صدای انفجار اومد. نسبتا شدید بود.
۱۲:۵۳ دوباره دارن میزنن.  حدود ۷، ۸ تایی زدن الان.
سلام   بازم بوشهر داره صدا میاد از ۱۲و ۵۲ دقیقه چندین صدای انفجار اومده
ساعت ۱۲:۵۳ دقیقه حداقل ۱۰ تا موشک به بوشهر زدن
از ۱۲:۴۰ دقیقه نزدیک به هفت هشت بار دارن میزنن بوشهر رو. خونه می‌لرزه!
وحید جان بوشهر رو ده دقیقه یک ربعه دارن همینجوری رگباری میزنن…
خیلی میزدن انفجارا همش دنباله دار بود مشخص نیست چنتا بود
حدود ۱۰-۲۰ ثانیه یه کوب صدا انفجار قطع نمیشد
وحید جان  رگباری باز بوشهر منطقه ریشهر رو زدن وحشتناک بود
ساعت ۱۲۵۸ دقیقه اسکله والفجر بوشهر را با ۸،بمب زدن، انفجار شدید
سلام ساعت ۱ ظهر صدای انفجار مداوم بوشهر
از ساعت 12:30 تا 13:15
بیش از 15 بار صدای انفجار مهیب توی بوشهر شنیده شده و موج خیلی زیادی داشته
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/77054" target="_blank">📅 15:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77053">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">پیام‌های دریافتی:
باز بوشهر رو زد
سلام دوباره بوشهر رو زدن
دوبار بوشهر زدن ۶و ۷دقیقه
حدود ۶:۰۷ باز بوشهر رو زدن.
بازم زدن ولی صداش به مراتب ضعیف تر بود.
🔄
سلام وحید الان ساعت ۶.۱۳ دقیقه باز کنارک زد خیلی بد زد
چابهار ۶:۱۴ زدن
بازم چابهار همین الان ۴ تا شدید زد گفتن تموم شده
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 436K · <a href="https://t.me/VahidOnline/77053" target="_blank">📅 06:09 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77052">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cd0e2facea.mp4?token=HewXI5AJFJIHNfOsDGyzCyi09nVqBODJAuPwn-ZTbSft1tNKazdwueLP2Oh_XmUCk1YYgFLpHhAAYn7z328IjXT9MOpwVc0HuCS879jSYTzBgFuFVK8bjcGmWstR0lpKzoOHP7IA3AbCupd5_z19EA5sOLrjmsbstc5pBFrhtSanayIPFGyXUU0ExV6Ng5iIG9Yw3yoS_iAAS27Vh5JLWgB9MbahpmU_bauYtl4UtfXC-chM2BLV-81GgsRFZu4UMMxX0pBP122dXl4olWH9dD5PWy9kREiKj8X1HNM1VFem3YL8ozeni9Zpqpy4Mwn-AZahwKxAVqCDyCaIij3m3jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cd0e2facea.mp4?token=HewXI5AJFJIHNfOsDGyzCyi09nVqBODJAuPwn-ZTbSft1tNKazdwueLP2Oh_XmUCk1YYgFLpHhAAYn7z328IjXT9MOpwVc0HuCS879jSYTzBgFuFVK8bjcGmWstR0lpKzoOHP7IA3AbCupd5_z19EA5sOLrjmsbstc5pBFrhtSanayIPFGyXUU0ExV6Ng5iIG9Yw3yoS_iAAS27Vh5JLWgB9MbahpmU_bauYtl4UtfXC-chM2BLV-81GgsRFZu4UMMxX0pBP122dXl4olWH9dD5PWy9kREiKj8X1HNM1VFem3YL8ozeni9Zpqpy4Mwn-AZahwKxAVqCDyCaIij3m3jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اکانت سنتکام با انتشار ویدیوی بالا نوشت: نیروهای ایالات متحده حملات جدید علیه اهداف نظامی ایران را به پایان رساندند
ترجمه ماشین:
تامپا، فلوریدا — فرماندهی مرکزی ایالات متحده (سنتکام) تازه‌ترین موج حملات علیه ایران را در ساعت ۱۰:۱۵ شب به وقت شرق آمریکا در ۱۳ ژوئیه به پایان رساند.
در جریان این مأموریت پنج‌ساعته، نیروهای ایالات متحده با موفقیت اهداف نظامی در نقاط مختلف ایران،
از جمله بوشهر، چابهار، جاسک، کنارک،  ابوموسی و بندرعباس
را هدف قرار دادند تا توانایی ایران برای حمله به کشتی‌های تجاری را بیش از پیش تضعیف کنند. نیروهای سنتکام با استفاده از مهمات هدایت‌شونده دقیق، سامانه‌های دفاع ساحلی، سایت‌های موشکی و پهپادی و توانمندی‌های دریایی ایران را هدف قرار دادند.
در حال حاضر بیش از ۵۰ هزار نیروی نظامی ایالات متحده در سراسر خاورمیانه مستقر هستند. نیروهای آمریکایی همچنان هوشیار، مرگبار و آماده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 422K · <a href="https://t.me/VahidOnline/77052" target="_blank">📅 06:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77051">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/aff0de23f3.mp4?token=bSRFMneXf3kXepdMLYnNtw-xNZAzfwArz1PxMxVJ1EDL1fAhsyKI34A6JcGXgSeUGFyXtE8Rp9psxCnzXuCOTgxVhBuhK7Dw4MFrqzvrTWXUa1cUcCD1cGRbFVcaDR8gcNru1hs_xlUEp_Qw2nj2vg5XpGiAB9JFQoSb8z_VHMEuKwl-h4avtaRsB3RCOnmCtTrWbxWrkAyL6kmuTSFsPniI0p0FyTUkWhzcfmJ9JrSrCfz2_YZxTnNF9fli062KE-42aUZKA57P4iD4odXDCrQw6CyBqwtsQGpg1QCyYbUsWvk2kLdsCEJqa9_lRicGL769Qa3omW1iv9qbJxkd_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/aff0de23f3.mp4?token=bSRFMneXf3kXepdMLYnNtw-xNZAzfwArz1PxMxVJ1EDL1fAhsyKI34A6JcGXgSeUGFyXtE8Rp9psxCnzXuCOTgxVhBuhK7Dw4MFrqzvrTWXUa1cUcCD1cGRbFVcaDR8gcNru1hs_xlUEp_Qw2nj2vg5XpGiAB9JFQoSb8z_VHMEuKwl-h4avtaRsB3RCOnmCtTrWbxWrkAyL6kmuTSFsPniI0p0FyTUkWhzcfmJ9JrSrCfz2_YZxTnNF9fli062KE-42aUZKA57P4iD4odXDCrQw6CyBqwtsQGpg1QCyYbUsWvk2kLdsCEJqa9_lRicGL769Qa3omW1iv9qbJxkd_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حال وش: حملات به مقر سپاه پاسداران در سراوان
haalvsh
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/77051" target="_blank">📅 05:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77050">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده:
همین الان ساعت ۵:۳۹ صدای انفجار اومد چابهار و خونه لرزید
الان چابهار رو رو زد خیلی سنگین بود هنوز نمی دونم کجا بوده
سلام ساعت ۵.۳۹ دقیقه دو انفجار شدید چابهار
همین الان دوتا دیگه هم زدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 363K · <a href="https://t.me/VahidOnline/77050" target="_blank">📅 05:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77049">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">پیام‌های دریافتی:
الان بوشهر [رو] زدن
دو بار
باز بوشهر رو زد
پایگاه هوایی بوشهر [رو] زدن سنگین الان ۵.۱۲
باز بوشهر رو زد
وحید سلام  بوشهر [رو] باز زدن 5,11
سلام بوشهررر رو زدننن
ولی الان باید بریم امتحان بدیم توی این شرایط
😐
😐
🔄
ساعت ۵:۳۷ موج دیگری از پیام‌ها رو دریافت کردم که از شنیده شدن صدای حدود ۱۰ انفجار پیاپی در بوشهر خبر دادند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/77049" target="_blank">📅 05:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77043">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ve2sd_AmXsclYDfpcDZwo8yivC-iPZTqlic0RU0CwFtIiSSgd_F-JUc_jVYg2uHbHAOqq7nffSSF1DtoBLpRluMwTonBnDI6eBGlgm4chqiqMaBbxWsurfJZVqH61rzKrp6pqEE3I_kf1RQ1ddXGIRbn0xACIDKxHtwJ0yOU4J9IxOpg6boUY3QTcN5pp2eqnxyx8-PCo-_-6Tq_KyuMNK4yi___1s1GnBDviezHBEpmsy-8PStRR9pK0z8qd-Bj3whuAZ6vW0qNuivPersnGEKuCOiVuAZw-mcfeO9-aECO4lAlmJaqXCY2mle_bxca5ViyDLG-vbjyhJMfXhGcgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DWVvtTW9KX_eyQhbkVu5gbkrmLebqesUcYwa8cxw4OSI8-6mrHeeIP6UleQ0vxuirUjhbjXUNPuPDQZcRC8Ea_DhXGYV8HpYl-IqHPegDL4CD-4huctUMkVFZ3XVi-vuMpv8_bqbZHifVzSL_Xa7wLQhQDGevYpLd4YnPXIp0zWCsB_YKjEIKsEHY0q16t9S6VtbdglLD7cIC70H-YAAPzHiH5KNLAlUddbWxTnl6w3QtTl2vY64uC_-5GzlbouXIDBt821DO39j57vTymnetJVGGmNY033ilZZRsvFeemTY7XhAjHUmmecHVVCa8Nj3na_ylTY8c6yL93HoTaemzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ow5JzBzX7YT3Td07SXza9AlCi9zraR1DGY_KKu6huTOs_V2Ex_Gl2Vl_nlV48g0v_iMjC9aYmsD7NMtDvuofmWk_m0fPvkwZMwToWdJF_-ub7Qiv540m6iCQZJRz2JXfl1u2mEj9u7YBQjnjP21ceBkVYVbsU1i2IJ72qZPN6Vz4iipHMllNFiBXe5MsiRtJTF6b1R9-JKrfNwgtVmevl76Rt4EYCJ8BnrIkZoowkGHEEZZepe3Scz0opNunhXp0k5YICRStx4hSPUrR9FakRNuA_Wk8W5_l7RxEwZpVYQPFkS4QNB0umG6H5S5W0mxcDtnfr0bviln8W2QeTyOjTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jKyuofHcVtAtHAQ_VVp9DRR2Fh9cqbnr-D4GDzIeh-3wxxaV-tgZ0FZcsrisNfEqhRjPsRkipmSm54UKfAh_5iLORC1ImejjXWciJrZIJy1Uouc8zTycNUzR7yX8rRuAJcp050olsBXbxBA2kB44tTaTa0tY3jSpIafDs0Y6bfddX-BLMdapXhdoh_IhWc4Rx6ukyihyYbWhJQYudK-9M40avk5VpYofEXGkImvulYCwjvGScI61V_1VrRPgCrFpaIgOa0QLzlKWw2UoibEJ4cBaNxA7-Q5SB1_u89aon7oi-Lb6kmrIKK7uWiOd6BpZ_Ez9PLRJi-OnKKP2i-SgcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tdem8ii26z_kPgVDbrLfQ7V6Z2kbE-HTwCmcym-eQ0L3sygP_c7DUdhqM6JAP_U0pMlhcFXi6AQvE3NcmvwMGSbw52LCpKw06Bgu_O3X0SLlW-r2wWGPcdo8ihbRyhIWrWOR8m2wxZezZ6Il0wmNh_SAXRdWU3oS_7e0UaNh2M5Z2YQKk75OYUmZnmiwz2i4DlSiGLFV3NY4TcUmZO9ZI8TjAvzL_PBK2AZcHlStrS9Zjwy-cbzAvo4llYKM513SMTwNqn1HiVCSBo8H0RRTFqG30iAY3HJpOxJz1iiTSMtp14vz3185ySgEbPbUI1I_Im6EfiCOiPDUqHFh3DUQKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DeT4ou0E2bFECxt9MSILGsPBhTcfZSWjfrjmZbSoOOHLFnAedxeAYK-5U5MkyACRn7BWB11h0cFKGyu0EdVlZScpUXW65mhK00qwr4L9BnNqBwklcBZE3dhhk8Yipl7s7Gu5gC6asSq3FimnegRTHJXMabi7-5WQAQ5Lmr-ncrzdrlZoIMACnV5Lcqk6EiQmMyHJR9b10IUWKcRHcqzrCNnxzb19d0v2jf39E5MsKKzpVkpaHLInIA91NM8YQKxFxRulR_RicQxs7z7Lmf78hCDR3houNHstNevorIxLPsu4wEv9DT-RW6DfpEPs_-3az_l-6891YOk8IYM_or5c8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مجلس [شورای اسلامی] پس از ماه‌ها تعطیلی، شب ۲۲ تیر اولین جلسه علنی خود را برگزار کرد.
به گزارش خبرگزاری خانه ملت (خبرگزاری مجلس [شورای اسلامی])، بیش از ۲۵۰ نماینده مجلس با حضور در ساختمان بهارستان جلسه خود را به ریاست حمیدرضا حاجی بابایی، نایب‌ رئیس مجلس، آغاز کردند.
نمایندگان مجلس با شعار دادن خواستار «انتقام از قاتلان» علی خامنه‌ای، رهبر پیشین جمهوری اسلامی ایران، و فرماندهان و شخصیت‌های سیاسی کشته‌شده در جنگ شدند.
در این جلسه مقرر شد که در مواقع اضطرار و شرایط خاص ایران، جلسات مجلس می‌تواند «در فضای مجازی یا خارج از بهارستان» تشکیل شود.
از نکات جالب توجه در جلسه امروز مجلس، نصب عکس مجتبی خامنه‌ای، رهبر جدید جمهوری اسلامی و همچنین غیبت محمدباقر قالیباف، رئیس مجلس در صحن علنی مجلس بود.
تشکیل جلسه علنی مجلس پس از ماه‌ها تعطیلی، آن هم در ساعات غیراداری واکنش‌های زیادی را در پی داشت و توجه رسانه‌ها را به خود جلب کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/77043" target="_blank">📅 04:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77042">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cRjfien44yS7xI3p8_ofvBHEff2ewpCxpyMdx0OZWibySaLiF6VJzaSM_O-imaelB1aBiFMtQXf9MoKI2pu474LEnPbanuXV9VpNpozS2VojnUbRSfqJtMy97dYnDnnX1rW6t9cVjNEruo7lzWS8bVzlBqL1PWEnYRYehkMqFa0AqMgN3emgH2ra0Vcx09YvEGUAJl7sqlNaja0TLgTMZWPoNAnodHya4kidlCa0K7ujVry1LHOT384OERqT2Co5BdP03sc3ifFIxNbFTOyVQ14FzKBFvJ1e0pbcHOWT07EcYyziWMpfKmMEQnCXdzK5TT_5CRttOYpQyrv1rxu5wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون امنیتی و انتظامی استانداری خوزستان گفت: در ساعت ۲:۱۰ بامداد سه‌شنبه، نقاطی از شهرستان امیدیه مورد اصابت پرتابه‌ها قرار گرفت.
به گزارش مهر، ولی‌الله حیاتی گفت: بر اساس ارزیابی‌های اولیه از وضعیت مناطق هدف قرار گرفته، تاکنون چهار نفر در این حادثه دچار مجروحیت شده‌اند که اقدامات امدادی در حال انجام است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/77042" target="_blank">📅 04:30 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77041">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Tskj7IqJHJp27uLt9vz6UbJ9ficzvHuePc9hFVjewOLLkzJvBIZL62yLWVZ1cSjGSfjC2yCnpvJQHB1iT9tbJh78p7kGizRy_D0Ab7EWV8O1WFA1BK6TBssvcAtLn9iWkgQt6UHlMrxT_ueq8FuLgeUKI9X3CpbXpkHW-YNh6ABznIcKsL_2CTTemJ6R-8nwdzHs2Dia05ri5uPac-8Mz1rAa-VLO8pwQFGoSnXF2BUIW2VPcQoqkRT9S-Mvv1pohCbDbEj-XyVY_-IB7Wf-VuAUessHg7AO9PSAldo0B0aJ-OFYz-XcTLqRGPqzGiphjtA9JA-k5_07XV89QaYKWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت دفاع امارات متحده عربی اعلام کرد که جمهوری اسلامی ایران به دو نفتکش در نزدیکی سواحل عمان حمله کرده است. به گزارش آسوشیتدپرس، در این حمله یک نفر کشته و هشت نفر دیگر زخمی شده‌اند.
@
VahidHeadline
" اطلاعیه روابط عمومی سپاه پاسداران انقلاب اسلامی"، ایرنا:
بسم الله قاصم الجبارین
قَاتِلُوهُمْ یُعَذِّبْهُمُ اللَّهُ بِأَیْدِیکُمْ وَیُخْزِهِمْ وَیَنْصُرْکُمْ عَلَیْهِمْ وَیَشْفِ صُدُورَ قَوْمٍ مُؤْمِنِینَ
ملت قهرمان و مومن ایران عزیز؛فرزندان شما در نیروی دریایی سپاه بر عهد خود در حفظ حقوق ملت ایران در تنگه هرمز تمام قد ایستاده‌اند.
ساعاتی پیش ارتش کودککش آمریکا که از شکست های مکرر عبرت نگرفته است، با تحریک شناورها تلاش کرد تعدادی از آنها را از مسیر غیر قانونی عبور دهد. دو فروند سوپر نفت کش متخلف که فریب آمریکا را خوردند و با خاموش کردن سامانه های ناوبری و بی توجهی به اخطارهای مکرر مرکز کنترل امنیت تنگه هرمز کشتی رانی در این مسیر را به مخاطره افکنده و عبور از مسیر مین‌گذاری شده را ترجیح دادند، مورد اصابت واقع شده و از کار افتادند.
نیروی دریایی سپاه به همگان اعلام می کند همکاری با دشمن متجاوز که از هزاران کیلومتر دورتر آمده تا حقوق مردم منطقه را تضییع کند و عبور از مسیر مین‌گذاری شده جز پشیمانی، خسارت و تاخیر در بازگشایی تنگه هرمز و ایجاد بحران انرژی در جهان نتیجه ای ندارد.
و ما النصر اِلا من عندالله العزیز الحکیم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 295K · <a href="https://t.me/VahidOnline/77041" target="_blank">📅 04:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77039">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nEexBXhAemrN7FWiByHY-BX6mehg3nNZBJfZhUd-vogHMd_LFTnArF28CmTU1JTHIUUQ6sW3mlBS_qe5ekX71FRYCqZXo1Fmb4RMqLUWg9IwnLTEjbej2ZIxw5izIQpRlsMubQG-y3pKITC2MxRZoZ1IaveUraVwSa2sA-LDjcLu8sm-T6u3HxCIRhqpRzNiGRmKy_DkjsYhXROG9tZcw-kV2hBjzfG1nIRVbJaH2ITjnP1gukfzNftHjzFVnd0jl77DBYGjnk2qSiY5TgbG0MpxvWCM0mPeCkRv-V4WU1Bwb27jmoC7xsk7b_EqBeptbx3kFnCCJZWaluIUjQ-eKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JSqCkDrLt9ICMxhHZtguyc-GDKQA_pNrLYiNTP00SVEPW7SThvhRmuahaO1jHAD6aNNZJZo4afniz4x7w2j9oF6nzUyx6IsHR4PxjzPGy_M15_yWSSMsbZdBYYP88_o0a8fIo0a9X6W0mx57BtDJ8fDmFIdwmOIrYhn89x1C10j-fgVdcm2JYqP6BZ7m8KP-MXb-oNfg3AIssq0xwUkwsI6w0ZKFoIhCRS2MLWN2hGWI_-bRLAd9T4ovq1J6CGJ9fvhwkbMcquh0XL30SUqkp_oPUZ2zXQahsFqjsRL18G1gi7QT6T0TZiL5vNJ_kBh43G-pMaj8vKvZaGEU0zyCpA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر دریافتی با شرح: کرمانشاه ۲ تا موشک شلیک کردن ساعت ۴
آپدیت: ممکنه تصاویر مربوط به پرتاب از تبریز باشند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/77039" target="_blank">📅 04:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77038">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">پیام‌های دریافتی:
همین الان تبریز
از سمت شمال شهر  دوتا پرتابه با نور شدید قرمز به سمت جنوب غربی دیده شد
سلام وحید جان، تبریز صدای جنگتده میاد [احتمالا صدای شلیک موشکه]
سلام اقا وخید همین الان صدای دوتا انفجار کرمانشاه
سلام
صدای دو انفجار در کرمانشاه
ساعت ۴ و دو دقیقه
ساعت ۴:۲ نردیکی هرسین تو استان کرمانشاه صدای ۲ انفجار سنگین اومد
سلام ساعت ۴:۰۳ کرمانشاه دوبار صدا اومد احتمالا شلیک موشک.
سلام وحید کرمانشاه شهرستان هرسین دوتا صدای وحشتناک مهیب
سلام کرمانشاه ساعت ۴:۰۲ دقیقه صدای انفجار از سمت تنگه کنشت
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/77038" target="_blank">📅 04:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77037">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9e3d542753.mp4?token=ZsjzbI88e3MYawaDpzgMh3YFUEIcEpoyVpOO6axu8GHRnfSA-SGsapjPZHrraL4HUMDSc5hqBOhhj87DRH13tgCRxJC4Kt3GZ6pXmnHJqnh9poebzh4uosVU5WuQGnihYsihkWSD4S0Fk_jeMIdav-BQRZpaYvoT3cBKVTL3DpLfDmxyfZXGtSbWqBGmUoZHY6XlHF2BW7DTLkN-CsddTKOjF0wFJ5YHz69-BXS1jcM2RijuptqOX3gH_QdYgsPwmmLFGPJsVyfLFbiU-gRkPshLOXQBUY3jUrNYuo4LAgwc03yAwU4yVhESpII4gC3IAmyLDXYlJf7LL2x0RsaDjw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9e3d542753.mp4?token=ZsjzbI88e3MYawaDpzgMh3YFUEIcEpoyVpOO6axu8GHRnfSA-SGsapjPZHrraL4HUMDSc5hqBOhhj87DRH13tgCRxJC4Kt3GZ6pXmnHJqnh9poebzh4uosVU5WuQGnihYsihkWSD4S0Fk_jeMIdav-BQRZpaYvoT3cBKVTL3DpLfDmxyfZXGtSbWqBGmUoZHY6XlHF2BW7DTLkN-CsddTKOjF0wFJ5YHz69-BXS1jcM2RijuptqOX3gH_QdYgsPwmmLFGPJsVyfLFbiU-gRkPshLOXQBUY3jUrNYuo4LAgwc03yAwU4yVhESpII4gC3IAmyLDXYlJf7LL2x0RsaDjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی منتشرشده با شرح: سراوان سه‌شنبه ۲۳ تیر
پیام دریافتی: اینجاست
GoogleMaps
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/77037" target="_blank">📅 03:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77036">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pYXL1JsHBXkeMKPJjrzipMCDVvCuFTOvONMrhXF4utj20B2FycK2Nu-eFIZGgTZI7XPn2rgjhz1hn-g7SeiTYzGPz3pBlHXvTgGxvATIMOb1P4h4BASxCVi_t5gkE-BMaoJ_qAcbhv_UtZEDLs6JeBFcdMNz_WhJYMcrAHPKz3U2e28611HOuarjucJ_N6hB1ZBzDe0K4r-HeNNzTNyKinfoxyGy9Wo-4v56RI5Di0UgV8vMFRqajpl0qjSQjJKX8hetQjbz-sJ4oZCvZwp4GTY3UjdlkSysKdZWqvy-hODsWvY7MaYHq_D4SsE4znf93bcHu_CaPBsbgCAW_DYo0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی:
ساعت ۳:۳۰ بوشهر دوتا انفجار خیلی شدید صدا توی بهمنی اومد
بوشهر 3:28 مجدد صدای انفجار
بهمنی زدن 2 بار سنگین بود ساعت 3 نیم دوباره زدن
وحید جان دوباره صدای انفجار اومد بوشهر ۳:۲۹
سلام همین الان بوشهر رو دو تا پشت سر هم زدن فکرکنم انبار مهمات یا همچین چیزی بود
دوتا انفجار مهیب پشت سر هم شهر بوشهر ساعت ۰۳:۲۹
سلام دوباره زدن با صدای انفجار بدتر
بوشهر تا الان ۴بار زدن
چهار تا صدای ترکیدن دیگه ۳:۲۹
پایگاه هوایی بوشهر ۳.۲۸ سه انفجار
سلام وحید بوشهر همین الان سه تا انفجار خیلی شدید پشت سر هم
بوشهر رو زدن ۳:۲۸ نزدیک به اسکله جلالی گمونم، پایگاه هوایی
سه تا تا حالا
الان بوشهر صدای بلند انفجار ۳:۳۰
3 تا انفجار سنگین
بوشهر ساعت ۰۳:۲۹ صدای انفجارهای خیلی شدید و نزدیک میاد
بوشهر ۳:۲۸ ۳:۳۰ هردو انفجار بلند خونه ها داره میلرزه سمت بهمنی
بوشهر صدای ۳ انفجار همین الان بهمنی
بوشهر همین الان ۳:۲۸ تا ۳:۳۰ ۵تا انفجار شدید ! خونه میلرزه
سه تا دیگه زدن
تو پایگاه هوایی
سلام دوباره زدن با صدای انفجار بدتر
بوشهر همین الان باز زدن
دو سه دقیقه پیش هم زده بودن
بازم زدن سه تای دیگه
بوشهر رو دارن میزنن
انبار مهمات اینا نیست فرودگاه دارن میزنن
و پایگاه هوایی ششم شکاری
و موشک های تام هاواک هستش ک صداش بلنده
یعنی جنگنده نیست مثل سری های قبل
بوشهر خیلی بد دارن میزنن تو این چند وقته اینجوری نبوده باز خونه هامون لرزید چهارتا پشت سرهم زدن
بوشهر - اولین انفجار پایگاه هوایی بود ۳:۱۳
انفجار های بعدی شامل دو انفجار در همون حوالی
دو انفجار مهیب دیگر در اطراف شهر بوشهر بود. احتمالا چغادک. حوالی ۳:۳۰ تا ۳:۳۲.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/77036" target="_blank">📅 03:30 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77035">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">پیام‌های دریافتی:
سربندر همین الان دوتا پشت سر هم
یکی دیگه
همین الان بندر امام خمینی‌ رو زدن سه بار
ماهشهر ساعت ۳:۲۳ صدای ۲ تا انفجار پشت هم
[احتمالا همون انفجارهای پیام‌های بالایی]
سلام ماهشهر تا الان سه بار صدا اومد
وحید جان ماهشهر ۳ تا پتروشیمی سر کارم لرزیدیم
سه انفجار پیاپی در ماهشهر داشتیم
😔
بچه ها صبح امتحان نهایی دارن
😭
سلام ماهشهر زدن 3:24 دقیقه
شیشه اتاقم لرزید
همین الان ساعت ۳:۳۰دقیقه
بندر امام خمینی سایت موشکی رو زدن چهار بار
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 267K · <a href="https://t.me/VahidOnline/77035" target="_blank">📅 03:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77034">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">پیام‌های دریافتی:
بوشهر 3:06 صدای انفجار
سلام ساعت ۳:۰۵ بوشهر صدای انفجار
ناحیه بهمنی
سلام وحید جان ساعت ۳:۰۶ بوشهر صدای انفجار اومد
الان بوشهر و زدن ما پایگاه هوایی هستیم خیلی بد بود
ساعت ۰۳:۰۶ دقیقا انفجار مهیب شهر بوشهر
سلام . همین الان بوشهر رو زدن . صدا خیلی مهیب بود
سلام وحید جان ساعت 3:05 دقیقه بوشهر رو زدن پایگاه هوایی بود فکر کنم
بوشهر زد ساعت ۳:۰۵دیق شب
همین الان وحید جان زدن بوشهر رو ، لرزش و صدا خیلی خیلی بیشتر از روزای قبل
ترس و لرز وجودم فرا گرفت برعکس شبای قبل
واقعا ترسناک بود این یکی
سلام
پایگاه هوایی رو زدن الان
صداش وحشتناک بود
تمام بدنم داره میلدزهه
همین الان بوشهر نزدیک فرودگاه صدای انفجار بسیار مهیب
سلام بوشهر بهمنی زدن ساعت 3:06
سید جان ۳:۰۶ بوشهر صدای انفجار (فکر کنم پایگاه نیرو دریایی بود)
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 269K · <a href="https://t.me/VahidOnline/77034" target="_blank">📅 03:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77033">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1b221ac38b.mp4?token=aWt-eR8pNOgJ0Qs95MAwoZ5njrBVFpbmC0olFIJrTusowDH35xU-4CtZn2hlItxz6PT9wB2WJqwkx-DzLS56VeGwPfrbEdTnyEW075q7rOBrfcmwGyRtdZ3mkc95lIWMIIGTcX021B9Mocx1rLIiAUJz47KKgfxH1q3wbdy3gQI2kxuKjlXn006TfiJCAURcjrbS3oV3GyGkuK0_t-V6ECif2COREV1x_ycou4xUZDcm6nwsmC6CM6GpWEKLVudqFfsNyk9cTPr2oHNIKTCOGN2vyrC9vfTmDqDG4_zXNdlbW1LYDQHsHiwh4ARD9LxvlMfTD-sSGU_yFDhn45kuLA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1b221ac38b.mp4?token=aWt-eR8pNOgJ0Qs95MAwoZ5njrBVFpbmC0olFIJrTusowDH35xU-4CtZn2hlItxz6PT9wB2WJqwkx-DzLS56VeGwPfrbEdTnyEW075q7rOBrfcmwGyRtdZ3mkc95lIWMIIGTcX021B9Mocx1rLIiAUJz47KKgfxH1q3wbdy3gQI2kxuKjlXn006TfiJCAURcjrbS3oV3GyGkuK0_t-V6ECif2COREV1x_ycou4xUZDcm6nwsmC6CM6GpWEKLVudqFfsNyk9cTPr2oHNIKTCOGN2vyrC9vfTmDqDG4_zXNdlbW1LYDQHsHiwh4ARD9LxvlMfTD-sSGU_yFDhn45kuLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی با شرح:
#سراوان
ساعت ۲:۳۰ دقیقه [سمت] فرودگاه رو زدند.
سه‌شنبه ۲۳ تیر
Vahid
پیام‌های دریافتی دیگر:
پیام ساعت ۲:۳۵: سراوان رو ۴ بار زدند
سلام سراوان سیستان بلوچستان ۵ تا انفجار پشت سرهم
پیام ساعت ۲:۴۱: سلام، سراوان بلوچستان رو زدن، ۳ تا صدای انفجار اومد خونه‌ها بد لرزید، حدود ۲۰ دقیقه پیش.
همین الان سراوان سیستان و بلوچستان رو زدن
سلام ساعت 2:20 سپاه شهرستان سراوان سیستان و بلوچستان رو زدن
4 تا انفجار بود با صدای خیلی وحشتناک
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 260K · <a href="https://t.me/VahidOnline/77033" target="_blank">📅 02:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77032">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/30da9372f8.mp4?token=Xy1RfdIrMMBvUxYy-7mHgnv9jXX4XHGdx1Emd-d0mdg2gkE2R80FOsQS0Py9VPNG9b1UdOv1EKEf9N01fMiyZWNM0_-o38Yvx_Csc7EdJOARVgDy_KcaTq3zRGB8gsYjOw2k4YP69YgtkzHBPBo4VOyRhFn2oJYgMqlrUVgpRZ20bUvum_WUmHcZKQCUz7Jp8D49SlC2EDEBMB_oo4-8ketKK_3piHAuosClWKj1whivqRLWngJqh5xIpTT1sx5FGPyTNg7x4EF7tGi09cc5m3VaXLY8mtm7BQDSB785YlsPn6sGjeilbnG6QW9uvUXl6WZi0sGXc0xZKs2zjRtM6yPywTiho5Ok-zFc-V9djo2wxjy3imNY9fS145dZldrgQtxcZfMajictv2n9aim1L-jg34OmnwkgdL-256ZE6s5y0ES4_7dn9d0RP6CH4FmU2Vhd_MsGMnMZATclFBUlRKhfdean7BiCWqZG5BBXVxRF0aMvHGKkfGVwYL31JtEEMsHEYz1lApSf5JVMCNKFR5wz6CMeFAuWZ3vQQ8JNgAIbrP_z4O9cd-jY7F4R1j_tOPhS3TXzOHiHMdgq_sXQQUWVLQqz-qGJcWQ-BtnHWXNsnCvlbsKd20sqJUj8zkgHAjz7Ml8oDtJTz3GfkJDr-COkEdi2HPIBOFHNP6XCscI" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/30da9372f8.mp4?token=Xy1RfdIrMMBvUxYy-7mHgnv9jXX4XHGdx1Emd-d0mdg2gkE2R80FOsQS0Py9VPNG9b1UdOv1EKEf9N01fMiyZWNM0_-o38Yvx_Csc7EdJOARVgDy_KcaTq3zRGB8gsYjOw2k4YP69YgtkzHBPBo4VOyRhFn2oJYgMqlrUVgpRZ20bUvum_WUmHcZKQCUz7Jp8D49SlC2EDEBMB_oo4-8ketKK_3piHAuosClWKj1whivqRLWngJqh5xIpTT1sx5FGPyTNg7x4EF7tGi09cc5m3VaXLY8mtm7BQDSB785YlsPn6sGjeilbnG6QW9uvUXl6WZi0sGXc0xZKs2zjRtM6yPywTiho5Ok-zFc-V9djo2wxjy3imNY9fS145dZldrgQtxcZfMajictv2n9aim1L-jg34OmnwkgdL-256ZE6s5y0ES4_7dn9d0RP6CH4FmU2Vhd_MsGMnMZATclFBUlRKhfdean7BiCWqZG5BBXVxRF0aMvHGKkfGVwYL31JtEEMsHEYz1lApSf5JVMCNKFR5wz6CMeFAuWZ3vQQ8JNgAIbrP_z4O9cd-jY7F4R1j_tOPhS3TXzOHiHMdgq_sXQQUWVLQqz-qGJcWQ-BtnHWXNsnCvlbsKd20sqJUj8zkgHAjz7Ml8oDtJTz3GfkJDr-COkEdi2HPIBOFHNP6XCscI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنان تامی بروس، معاون سفیر ایالات متحده در سازمان ملل در جلسه اضطراری شورای امنیت، ترجمه ماشین:
بار دیگر، این شورا برای برگزاری نشستی اضطراری فراخوانده شده است تا درباره تلاش‌های حکومت ایران برای تهدید همسایگانش در خلیج [فارس] و تضعیف تلاش‌ها برای برقراری صلح در منطقه گفت‌وگو کند.
در ۳ ژوئیه، یک پرواز ایرانی از تهران وارد صنعا، در قلمرو تحت کنترل حوثی‌ها، شد. هدف این پرواز، انتقال نیروهای سپاه پاسداران، از جمله کارشناسان پهپادی و موشکی، برای حمایت از تروریسم حوثی‌ها بود؛ آن هم با پوشش انتقال مقام‌های حوثی به مراسم خاک‌سپاری رهبر جمهوری اسلامی.
این نوع حمایت، حوثی‌ها را قادر می‌سازد مردم یمن را به وحشت بیندازند و آزادی کشتیرانی را در دریای سرخ و آبراه‌های پیرامون آن تهدید کنند. از زمانی که پروازهای ماهان‌ایر به صنعا در سال ۲۰۱۵ متوقف شد، شاهد تلاش ایران برای ارائه چنین حمایت آشکار و گستاخانه‌ای از حوثی‌ها نبوده‌ایم. در واقع، رهبران حوثی آشکارا از این پرواز اخیر به‌عنوان دورزدن موفقیت‌آمیز تلاش‌های بین‌المللی برای منزوی‌کردن این گروه تروریستی تجلیل کردند.
این اقدامات نقض قطعنامه ۲۲۱۶ شورای امنیت به‌شمار می‌رود. ...
افزون بر این، صبح امروز دومین پرواز ایرانی با وجود دستور صریح و علنی دولت جمهوری یمن مبنی بر خودداری از این اقدام، وارد یمن شد. بی‌اعتنایی عامدانه جمهوری اسلامی ایران به حاکمیت یمن و تصمیم‌های جمعی این شورا، به‌سادگی غیرقابل‌قبول است.
به همین ترتیب، بی‌اعتنایی آشکار ایران به قطعنامه ۲۸۱۷ شورای امنیت را نیز دیده‌ایم. ....
هفته گذشته، ایران پهپادها و موشک‌هایی را به سوی سه کشتی تجاری غیرنظامی که در حال عبور از آب‌های سرزمینی عمان بودند، شلیک کرد؛ اقدامی مغایر با حقوق بین‌الملل. این حملات می‌توانستند دریانوردان را زخمی یا کشته و خسارات زیست‌محیطی قابل‌توجهی ایجاد کنند. یکی از کشتی‌ها، یک نفتکش قطری حامل گاز طبیعی مایع، در حال سوختن رها شد و تردد دیگر کشتی‌ها در تنگه را نیز بیشتر به خطر انداخت.
سپس عصر شنبه، ایران یک کشتی کانتینری در مسیر امارات متحده عربی را هدف قرار داد. یک تبعه هند همچنان مفقود است. این حملات از هیچ اصل مشروعی سرچشمه نمی‌گیرند. بلکه همان‌گونه که یکی از مشاوران رهبر جمهوری اسلامی روز یکشنبه گفت، این اقدامات از تمایل ایران برای تصاحب غیرقانونی یک آبراه حیاتی و استفاده از آن به‌عنوان ابزار بازدارندگی راهبردی ناشی می‌شود.
فراتر از عرصه دریایی، ایران در هفته گذشته پهپادها و موشک‌هایی را به سوی بحرین، اردن، کویت، عمان، قطر و امارات متحده عربی پرتاب کرده است. وزارت کشور قطر گزارش داد که سه نفر، از جمله یک کودک، بر اثر سقوط بقایای عملیات رهگیری پس از حملات روز یکشنبه ایران زخمی شدند.
...
در چند هفته‌ای که از امضای این تفاهم‌نامه گذشته، ایران بارها این توافق را نقض کرده است. تا زمانی که ایران به تهدید عبور امنی که این تفاهم‌نامه از آن حفاظت می‌کند ادامه دهد، ایالات متحده آن را به‌طور یک‌جانبه اجرا نخواهد کرد.
به زبان ساده، اگر ایران به سوی کشتی‌ها شلیک کند، ما فوراً با نیروی نظامی پاسخ خواهیم داد. عملیات نظامی ایالات متحده پاسخی به این تهدیدها در چارچوب دفاع از خود و دفاع از دیگران است.
...
ایالات متحده در کنار شرکای خود در خلیج [فارس] ایستاده و همراه دولت جمهوری یمن، در برابر تهدید تروریستی حوثی‌های مورد حمایت ایران خواهد ایستاد. ما همچنان متعهدیم با اعضای شورا همکاری کنیم و از همه ابزارهای موجود، از جمله تحریم‌ها، برای حمایت از راه‌حلی مسالمت‌آمیز برای درگیری یمن و حفاظت از صلح و امنیت بین‌المللی استفاده کنیم.
و در پایان، بار دیگر از شورا می‌خواهیم با صراحت و بدون هیچ ابهامی به ایران اعلام کند که این اقدامات آشکار، مغایر با حقوق بین‌الملل و غیرقابل‌قبول‌اند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 266K · <a href="https://t.me/VahidOnline/77032" target="_blank">📅 02:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77031">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c6082c82eb.mp4?token=KtuRacNfvUNZ6AqVcif5DCk5c_DzIPhTPdikIlN00qI5A9WMrZ0NOdRr4MYkmftJx-JCdpeRradkwXzPz1JJiDV7FaVlBZRNQ7OeFXxNG5YDaWZ8UHLR0PoVPdYsOVL2QwDOc4S4almYseJrObhomOTi6tXtasTmzK-D6cXL5Dyb59J8Zjrrczc7dDIAdRkNiO2O3wk065V1E_FhmEkg8iXtu7eDxL_hh82H-D03sCbx5yUbRITiJxggvGMTjxeqQR1fcfdjv3fzjlH3lxrFK4dt7T1EOwRQf3OMLY3BJEl9opwePATDYa5GVfzovLuqYKLlOJ3dTfmRL64lis7Zmw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c6082c82eb.mp4?token=KtuRacNfvUNZ6AqVcif5DCk5c_DzIPhTPdikIlN00qI5A9WMrZ0NOdRr4MYkmftJx-JCdpeRradkwXzPz1JJiDV7FaVlBZRNQ7OeFXxNG5YDaWZ8UHLR0PoVPdYsOVL2QwDOc4S4almYseJrObhomOTi6tXtasTmzK-D6cXL5Dyb59J8Zjrrczc7dDIAdRkNiO2O3wk065V1E_FhmEkg8iXtu7eDxL_hh82H-D03sCbx5yUbRITiJxggvGMTjxeqQR1fcfdjv3fzjlH3lxrFK4dt7T1EOwRQf3OMLY3BJEl9opwePATDYa5GVfzovLuqYKLlOJ3dTfmRL64lis7Zmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی: '
#کیش
، سه‌شنبه ۲۳ تیر'
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/77031" target="_blank">📅 02:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77030">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده از حدود نیم‌ساعت پیش:
سلام وحید جان
امیدیه رو ساعت ۲:۹ دقیقه زدن
سلام همین الان امیدیه خوزستان زدن
شهرستان امیدیه خوزستان
صدای شلیک دوتا موشک شنیدیم
بعد هم دو تا انفجار قوی خیلی نزدیک بود فاصلش
تونل موشکی که در روستای نمره یک امیدیه ازش استفاده میکنن همین الان بمب بارون شد و تخریب شد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/77030" target="_blank">📅 02:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77029">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">پیام‌های دریافتی:
حدود ساعت ۱:۳۰ چابهار یه صدای انفجار اومد
سلام وحید جان همین الان ساعت یک و نیم صدای پنح انفجار در چابهار شنیده شد
سلام وحيد جان ، چابهار صدای انفجار اومد 1:34 بامداد
#چابهار
: فقط باید تهرانی باشیم کسی به فکر ما باشه؟
[آپدیت: در واکنش کلی پیام حمایتی از تهران دارند می‌فرستند. زحمت نکشید و ننویسید لطفا.]
صدای انفجار ضعیف کنارک
انگار فاصله زیاد بود
وحید الان چابهار رگباری زدن نزدیک 10.15تا
سلام ساعت ۱:۳۳ چابهارو دارن بد میزنن
کنارک همین الان نزدیک ۱۰ تا زد 1 : 34
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/77029" target="_blank">📅 01:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77027">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VfWpMKg0aoQdZvv6nJQlX-FewICXMiv7BIfp7CN5pV209264DT48oyjm95PQon4pAE0Y31l-tX4JtC-J71TDj4H-iOc5gj_MZFWzPsXBX4VA5wcioG3h2bFRL8B3PQoF3Ny_4rgTIHui3VaPa2hmwqqBJ2h9myXWlCpuUm6jSVDK6WFacox432h24JFfnYsfko3prvtpe6nUfc4h2zsUGlXKIglmSjRimzL5HYCEkHEJ9CkFAtm9vnsgRYlY6lKdxgQQxkT6VseW2yVu_HFXHpLLzF07yCXd0j5e4ZrdBRRgTJBWy5bMjaA3Xqbph9XW2MjZuP3r7tjPZ0wV8a-scA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oo9Ize3mJE7um1Sx9usfI8hc5wWD5jl3RWK2qvei_XW5Awxk-arGdiCfcrAOSVgwlWMwmN9aygh2g0ag7RrCGjgYNX_6truo1hEbbnfio4gpJYvpe_AsMqLG-ASsyJHNOxmfwimkXsYPXjaobzmj8YpMG2Esj_o7GW2FOzcQ1yzxYD63Xi2uyfUNAbkaz9qcNq12vw8iuu99sol_FPXiHws1UsPWe16c9DMknbXjKsNLOqazERQ8XtdRVCA2Fuc1oK_u3JySt0XE4SbkwsEdYesRPDk7f0laurLduKttQJ0juVRKKuAOGWeVCeKFL8pqCxikOrtWd7Ljrss1g4wHIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر دریافتی با شرح: '
#کیش
، سه‌شنبه ۲۳ تیر ساعت ۰۰:۳۸'
Vahid
بعدش هم حملات و انفجارهای دیگری بوده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/77027" target="_blank">📅 01:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77026">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">پیام‌های دریافتی:
کیش ساعت ۱:۰۲
۲ انفجار دیگه
صدای انفجار داره میاد تو کیش
کیش دوتا صدای انفجار دیگه
دوباره کیش رو زدن وحید
الان دوباره دوبار کیش زد
کیش رو دوباره زدن
البته صدا دورتر بود ۰۱:۰۳
دوباره زد کیشو
وحید جان این دفه دوتا زد
بندرگاهو داره میزنه
مجددا کیش را زد صداش از قبلی ها خیلی بلندتر بود و شیشه ها لرزید.
🔄
سلام همین الان کیشو دوباره زد این بار هم دوتا بود ساعت ۱:۹
الان سه بار دیگه زد کیش رو
وحید جان دوباره یکی دیگه زد کیشو
و مجدد صدای انفجار در کیش
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/77026" target="_blank">📅 01:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77025">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4f01979093.mp4?token=LAjaimuITlHiNR6mfgxKyFKBZCg2j0r-jXa6JI0sOcJx2yiCgnJKrHitk6DVInGehilvasRDPVNlq3DsGU3aSUaVpSLOZ7Tdm-sf-FNyQhqyHfJ6S5Sdvm31ffE_dW-cCWiNT6blSSQUGohvmqE6tQTnUaaddfuMUTuE9Eu9O_30MlV8FalAJ5jkZTAHPjLSkJGhBpOuRfFp023fRen0cft5Xla4pnmAWe6modWtnl4UcLX2Fr4vukF7Fri5BwM75S0cTwkljfEXN96DM4ksNKCScdUUUElCP0a2viQktfkrn0pX5XGMsbooyXhBjmbcZv61IXnsXG6_UVyXxoyRlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4f01979093.mp4?token=LAjaimuITlHiNR6mfgxKyFKBZCg2j0r-jXa6JI0sOcJx2yiCgnJKrHitk6DVInGehilvasRDPVNlq3DsGU3aSUaVpSLOZ7Tdm-sf-FNyQhqyHfJ6S5Sdvm31ffE_dW-cCWiNT6blSSQUGohvmqE6tQTnUaaddfuMUTuE9Eu9O_30MlV8FalAJ5jkZTAHPjLSkJGhBpOuRfFp023fRen0cft5Xla4pnmAWe6modWtnl4UcLX2Fr4vukF7Fri5BwM75S0cTwkljfEXN96DM4ksNKCScdUUUElCP0a2viQktfkrn0pX5XGMsbooyXhBjmbcZv61IXnsXG6_UVyXxoyRlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی با شرح: انفجارهای
#کنارک
الان، سه‌شنبه ۲۳ تیر'
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/77025" target="_blank">📅 00:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77024">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BXYwodPjwt_0NV-BsBFllf04-O-I2DeC8rZRJY_bONNm1yzCx2Kg1u7HNesKV8A38e3SRckHkTYEJosfyU9FfyWHvg5I5U2pYyEzE07ByvIyzwE15-qovqPY0FqULj6yeQApr1zIeYlJ_U6etGxzKIG-jcWcGBBEP51nfKThh_f9R3QDsUx9Yp4x3WG0SIVukzfjvA75Yb4oNdkDAAKIvhI3klWPToobSun47aW0TZxCpoJm2tr58EwNoIdu0b0ryuxbmooCanFXMC8A261c2J2UZlnCCCVkxYM2pFCKF6BtRBQg2TV8sTxrhylo_fGLgZCjxufXN7AUH_QJOljRQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام:
امروز ساعت ۴:۴۵ بعدازظهر به وقت شرق آمریکا [۰۰:۱۵ بامداد سه‌شنبه ایران]، فرماندهی مرکزی ایالات متحده به دستور فرمانده کل قوا، سومین شب پیاپی حملات علیه ایران را آغاز کرد.
این حملات همچنان هزینه سنگینی بر نیروهای ایرانی تحمیل خواهد کرد و توانایی آن‌ها برای حمله به غیرنظامیان بی‌گناه و کشتیرانی تجاری در تنگه هرمز را کاهش خواهد داد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 340K · <a href="https://t.me/VahidOnline/77024" target="_blank">📅 00:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77023">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">پیام‌های دریافتی:
سلام همین الان توی جم صدای ۴تا انفجار اومد
شهرستان جم استان بوشهر
چهارتا تا الان زدن
همین الان جم رو  زدن سه تا انفجار12:40
درود شهرستان جم استان بوشهرو همین الان دوبار زدن
درود وحید جان، جم بوشهر ۴ انفجار پشت سر هم، خیلی شدید بود.
حاجی جم همین الان ۴ تا انفجار شدید ۱۲:۴۰
وحید جان جم بوشهر ۳ ۴ تا صدا اومد
همین الان ۴ تا صدای انفجار مهیب سپاه چمران شهرستان جم
خیلی مهیب
سلام وحید جان همین الان ۴تا صدای انفجار در کنگان شنیده شد ۰۰:۴۰
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 382K · <a href="https://t.me/VahidOnline/77023" target="_blank">📅 00:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77022">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">پیام‌های دریافتی:
وحید جان زدن کیشو پنج‌تا پشت هم
کیش رو زد
سلام وحید جان
همین الان کیش صدای دو انفجار اومد
دور بود صداها
سلام وحید جان کیش صدا انفجار پنج تا
همین الان ساعت ۰۰:۳۹ کیش رو زدن
نمی‌دونم بندرگاه بود یا فرودگاه، اما مطمئن که شدم، بهت میگم
سلام آقا وحید کیش رو زد ما نزدیک فرودگاهیم پنجره ها لرزید
جزیره کیش ۴ بار پشت هم زد و صدای جنگنده میاد.
کیش ساعت ۰۰:۳۸
۳ انفجار متوالی
درود
کیش، ۵ صدای انفجار، ۱۲:۴۰
۴.۵بار کیش صدا زیاااد پنجره ها لرزید همه تو بالکن خونه هان .. نمدونیم کجا بود
شاااااید رو آب بود ولی خیلی نزدیک ... هنوز کسی خبر نداده کجا بود..
انفجار در بندرگاه کیش بوده شناور سپاه یا نیروی انتظامی بوده…
بچه‌ها میگن حوضچه بندرگاه کیش رو زدن
شمال جزیره
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/77022" target="_blank">📅 00:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77021">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">پیام‌های دریافتی:
وحید جان مشهد زلزله اومد
مشهد لرزید
یا زلزله بود ، یا زدن یه جایی را
سلام
مشهد نمیدونم زمین لرزه بود یا چی؛
زمین لرزید!
همین الان ساعت ۰۰:۳۵
زلزله بود گویا مشهد.
وحید جان مشهد لرزید
مشهد زلرله اومد
مشهد لرزید ۰۰:۳۵
دو بار با فاصله ۴۰ ۵۰ ثانیه ای
سلام مشهد ساعت00.35 زلزله یا یه موج لرزه‌ای شدید اومد با فاصله سه ثانیه رفت برگشتی بود
مشهد یک لرزش خفیف حس شد ولی صدایی همراه نداشت.
مشهد چند دقیقه پیش دوبار لرزید
سلام وحید آقا
مشهد یه چند لحظه ای لرزید
فکر کنم زلزله بود
سلام فریمان هم از زلزله مشهد لرزید
من تربت جامم اینجام همون تایم در حد دو سه ثانیه یکم لرزید
فریمانم لرزید(شهرستان60کیلومتری مشهد)
حتی یکی از اعضای خونه از خواب بیدار شد
چند ثانیه طول کشید
سلام وحید جان. ما طرقبه نزدیک مشهد هستیم اینجا هم لرزش رو حس کردیم.
🔄
سلام آقا وحید زمین‌لرزه‌ای با بزرگی ۳.۶ حوالی سفید سنگ در مشهد را لرزاند.
بزرگی زمین‌لرزه ۳ و ۶ دهم بود. مرکز زلزله سفیدسنگ خراسان رضوی بود. بیشتر نزدیک فریمانه تا مشهد
[دو تا پیام هم درباره احساس زمین‌لرزه در یاسوج داشتم.]
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/77021" target="_blank">📅 00:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77020">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">پیام‌های دریافتی:
سلام وحید جان انفجار بندرعباس ۰۰:۳۴ ۳ انفجار
١٢:٣٣ سه انفجار پشت سرهم بندرعباس با صداي بلند
همین الان
بندرعباس انفجار شدید وحشتناک
چند انفجار وحشتناک پشت سر هم
بندرعباس ۳۳: بامداد صدای چند انفجار
بندرعباس ۱۲ و ۳۴ چهار صدای انفجار
وحید بندرعباس ۳ـ۴ تا صدای انفجار شدید
بندرعباس ۴ تا انفجار فوق العاده شدید سمت نیرو دریایی ارتش و سپاه
همین الان ۰۰:۳۴ دقیقه ۵ بار صدای انفجار اومد
سلام بندر عباس همین الان صدای چند انفجار شدید پشت سر هم فاصله ای نزدیک بودد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/77020" target="_blank">📅 00:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77019">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/33fa32f341.mp4?token=V_-LBTWki78vunCGq8nntRQiOMzBO7vE3z_aNeN1OUBaK7f-3TZLlKkPOIcQgfZGcgpckO8W7gNYfsHFNUhqlruagF4fQA9y84MWLXZ_IVg7LTy_rbqofLEf_5Pp45640EEpMSbu8sQYKDV3YglCh9CGGjpf9K0boFLST26ttBKRWAnTrEUgIRcw4Aos6O1SSonnscIbvZGI8Bz609CQ3aWnxGasKjzKRtpFYUE5xmOpIMFyKrlK4NHdQpCpJQjSgTd5O6S2toKng7W-ubra-lKLh9a1qNRAE6OmAeUvKrVF8uObH1ZPXnj1P_8FMxlsdWoQcAROzir9nA-N-Gm__Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/33fa32f341.mp4?token=V_-LBTWki78vunCGq8nntRQiOMzBO7vE3z_aNeN1OUBaK7f-3TZLlKkPOIcQgfZGcgpckO8W7gNYfsHFNUhqlruagF4fQA9y84MWLXZ_IVg7LTy_rbqofLEf_5Pp45640EEpMSbu8sQYKDV3YglCh9CGGjpf9K0boFLST26ttBKRWAnTrEUgIRcw4Aos6O1SSonnscIbvZGI8Bz609CQ3aWnxGasKjzKRtpFYUE5xmOpIMFyKrlK4NHdQpCpJQjSgTd5O6S2toKng7W-ubra-lKLh9a1qNRAE6OmAeUvKrVF8uObH1ZPXnj1P_8FMxlsdWoQcAROzir9nA-N-Gm__Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخش‌هایی از مصاحبه ترامپ، ترجمه ماشین:
🔴
ترامپ:
این را می‌گویم: به نظرم مردم اشتباه می‌کردند. هرگز فکر نمی‌کردم [نامفهوم] بتوانند کاملاً مسلح شوند. هرگز تصور نمی‌کردم چنین قیامی رخ بدهد، چون این‌ها آدم‌های خشنی هستند.
رهبران به‌اصطلاح‌شان بسیار خشن‌اند. آن‌ها قاتل‌اند. ۵۲ هزار نفر را کشته‌اند. آن کشتی‌گیر را یادتان هست؟ آن کشتی‌گیر یکی از بهترین کشتی‌گیران جهان بود. او و دو دوستش را کشتند، فقط چون حرفی زد که حتی آن‌قدرها هم علیه حکومت نبود.
آن‌ها دیوانه‌اند. به کشتنشان ادامه می‌دهند، چون تا وقتی شما کاری نکنید، مردم خودشان را خواهند کشت.
🌳
Hugh Hewitt:
آیا شما، ارتش آمریکا یا ارتش اسرائیل می‌توانید به آنچه از رده سوم، رده چهارم و رده پنجمشان باقی مانده دست پیدا کنید؟ می‌دانید کجا هستند؟ می‌توانید آن‌ها را بکشید؟
🔴
ترامپ:
بله، می‌دانم؛ اما نمی‌خواهیم درباره‌اش حرف بزنیم. ولی قطعاً زیر نظرشان داریم.
بله، من درباره این موضوع خیلی چیزها می‌دانم. خیلی چیزها می‌دانم، اما فکر نمی‌کنم الان مناسب باشد درباره‌اش صحبت کنم. ولی خواهیم دید.
برای نمونه، امشب آن‌ها را بسیار سخت هدف قرار خواهیم داد و فردا هم سخت به آن‌ها ضربه خواهیم زد. هیچ کاری هم از دستشان برنمی‌آید. هیچ چیزی ندارند. هیچ کاری نمی‌کنند، جز اینکه فقط لاف می‌زنند.
خب، فکر می‌کنم کمی خل‌وچل‌اند؛ همه‌شان همین‌طورند. رده اولشان را از بین بردیم. بعد رده دومشان را از بین بردیم. سپس حدود ۲۵ درصد از این حکومت را از میان برداشتیم.
ذهنشان کمی متفاوت کار می‌کند. دیروز توافقی داشتیم و قرار بود صددرصد نهایی شود؛ اما ناگهان تماسی دریافت کردند و همه‌شان از اتاق فرار کردند.
این آدم‌ها... این آدم‌ها دیوانه‌اند. توافقی داشتیم که در آن به همه خواسته‌هایمان می‌رسیدیم. اما آن‌ها اساساً توافق‌ها را زیر پا می‌گذارند، می‌دانید؟ توافق می‌کنند و از نظر آن‌ها، توافق‌ها برای شکسته‌شدن بسته می‌شوند.
این‌ها آدم‌هایی به‌شدت غیرقابل‌اعتمادند. صادقانه بگویم، اگر روزی سلاح هسته‌ای داشتند، ظرف یک روز از آن استفاده می‌کردند.
🌳
Hugh Hewitt:
آیا شما، ارتش آمریکا یا ارتش اسرائیل می‌توانید به آنچه از رده سوم، رده چهارم و رده پنجمشان باقی مانده دست پیدا کنید؟ می‌دانید کجا هستند؟ می‌توانید آن‌ها را بکشید؟
🔴
ترامپ:
بله، می‌دانم؛ اما نمی‌خواهیم درباره‌اش حرف بزنیم. ولی قطعاً زیر نظرشان داریم.
بله. من درباره این موضوع خیلی چیزها می‌دانم. خیلی چیزها می‌دانم، اما فکر نمی‌کنم الان مناسب باشد درباره‌اش صحبت کنم. خواهیم دید.
برای نمونه، امشب آن‌ها را بسیار سخت هدف قرار خواهیم داد و فردا هم سخت به آن‌ها ضربه خواهیم زد. هیچ کاری هم از دستشان برنمی‌آید. هیچ چیزی ندارند. هیچ کاری نمی‌کنند، جز اینکه فقط لاف می‌زنند.
🌳
Hugh Hewitt:
ادامه بدهید، آقای رئیس‌جمهور.
🔴
ترامپ:
متأسفانه این کار را کردم، چون آن‌ها را شناختم. [نامفهوم درباره تفاهم‌نامه] خیلی بهتر است. می‌دانید، مردم می‌گویند دست‌کم آدم معقولی بودم، اما آن‌ها را شناختم و فهمیدم کاملاً سنگدل‌اند...
🌳
Hugh Hewitt:
تفاهم‌نامه‌ای که مذاکره‌کنندگان شما آوردند چه بود؟ آیا آن یک تفاهم‌نامه [نامفهوم] بود؟ آیا طوری تنظیم شده بود که از هم بپاشد؟
🔴
ترامپ:
برای آزمودنشان تنظیم شده بود. یک آزمون بود. نمی‌دانستیم.
ببینید، وقتی با آدم‌های پست سروکار دارید، تفاهم‌نامه معنای چندانی ندارد. حتی وقتی با آدم‌های شرافتمند سروکار دارید هم معنای زیادی ندارد، چون فقط یک تفاهم‌نامه است. معنای زیادی ندارد.
من گفتم: اصلاً چرا این کار را می‌کنیم؟ این یک روش استاندارد در آمریکاست که ابتدا به یک تفاهم‌نامه می‌رسید و بعد سراغ توافق نهایی می‌روید. من گفتم مستقیم سراغ توافق نهایی بروید.
ولی می‌دانید چیست؟ آن به‌نوعی یک آزمون بود و آن‌ها پای آن نایستادند؛ به آزمون پایبند نماندند.
🔄
بعدش جملات دیگری هم گفت که در ویدیوی بالا نیست:
دونالد ترامپ، رئیس‌جمهوری ایالات متحده، روز دوشنبه در گفتگو با هیو هیویت، مجری و تحلیل‌گر سیاسی، اعلام کرد که ارتش ایالات متحده «کوه کلنگ» را در ایران هدف قرار داده و آن را نابود خواهد کرد. پیش از این، خبرگزاری «وای‌نت» با انتشار تصاویر ماهواره‌ای جدید فاش کرده بود که این سایت زیرزمینی محرمانه در رشته‌کوه‌های زاگرس که آژانس بین‌المللی انرژی اتمی اجازه بازرسی از آن را ندارد، همچنان فعال است. موضوعی که پایبندی تهران به یادداشت تفاهم اخیر مبنی بر عدم توسعه سلاح‌های هسته‌ای را زیر سوال می‌برد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/77019" target="_blank">📅 00:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77016">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XezjQavqSWz7wQMWBKb_WKAOkDbKV3wMRB9-zOIPifslQY4KJX2Otozqde5q-7fpX1D-_3zIo8T-jzhmpgMUYCBfjWewwFoR6DsG7eploK0r624KAR2BbLLVAkSPzrkpPSuZ1sUtDYiyWiOqBVQmgDHLX5DX52bhmRv-gKQzfPMLXaCbkWx924OQizVr4C-AImRlOjYEA2Plqxgfxgsj-wKI5i2dUi9uTerrExMQqKkDJk8Mi5jtNHmOOVkikMv1F3RUFQ58JmDxQGmQmwc-6r0aMRwglyyNVoDp5p-XeCvsyhVTFEe0uNMYKXJ4mP3vZYQqkAZoKDdjUtFUPr950g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سفارت آمریکا در امارات متحده عربی با انتشار پستی در شبکه ایکس اعلام کرد تمامی وقت‌های کنسولی سفارت آمریکا در ابوظبی و کنسولگری این کشور در دبی از ۲۳ تا ۲۵ تیر به دلیل وضعیت امنیتی منطقه لغو شده است.
در این اعلامیه آمده است سفارت و سرکنسولگری آمریکا همچنان در وضعیت «تخلیه اجباری» قرار دارند؛ به این معنا که کارکنان غیراضطراری دولت آمریکا از امارات منتقل شده‌اند. در نتیجه، فقط خدمات کنسولی محدود به شهروندان آمریکایی ارائه می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/77016" target="_blank">📅 23:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77015">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">جنگنده‌ای که صدای پروازش در مناطق مختلف تهران شنیده میشه خارجی نیست.
هر شب هم‌زمان با وقایع جنوب کشور صدای پرواز جنگنده در بعضی از شهرهای دیگر شنیده میشه. گشت می‌زنند احتمالا.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/77015" target="_blank">📅 23:19 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77014">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VF4T_LYFLvwipxCF2Ds3HnY_uvls_KuqadlzfKJMyu0a9IvW13hhipdAEeq9bwGiN9Buqp4IGjfLfYeb2pDKlzyB1-NThga_10d0UOaqZq8atI8eewFJnbdagGROFXXax6vuAfjpnOu8pt3o_ofIwamAt31jFwwOVLkdLe_wW0OgHMKzEUVlxGcYufoVGBIZQtGsOiRVWxiirUM6PX_nLfTl8YZsJ0QzbwcSJqYxh1mA2qc4LhfKRJyNhJqkiL_H12rc7AuB7VUAven6JGdPwSlt9gRJ0qROj_-S3hPVfc6CyR-lhaTppyo5mJQCsmEdtwmwVCLogXBRYwdoBlw24Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ:
رئیس‌جمهور ترامپ پنج‌شنبه شب، ساعت ۹ به وقت شرق آمریکا، برای ملت سخنرانی خواهد کرد.
از توجه شما به این موضوع سپاسگزارم!
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/77014" target="_blank">📅 22:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77013">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ایرنا:
خبرنگار ایرنا در چابهار:
هم اکنون اصابت چهارموشک دراطراف کنارک و هواپیما امریکا در فضای اسمان شهرکنارک
صدای وحشتناک و کمافی السابق درب و پنجره ها شدیدا لرزیده و با غرش و لرزش همراه بود
صدای خیلی وحشتناکی داشته و تا چابهار و دشتیاری صدای انفجار شنیده شده است.
همان انفجارها
فارس:
دقایقی پیش صدای چند انفجار از سمت شرق بندرعباس به گوش رسید؛ هنوز محل دقیق این انفجارها مشخص نیست.
دقایقی پیش مردم در چابهار و کنارک صدای چند انفجار شنیدند‌
برخی منابع محلی محل وقوع انفجار را مرتبط با کنارک می‌دانند و معتقدند مردم در چابهار صدای انفجار کنارک را شنیده‌اند.
🔄
آپدیت: صدا و سیما
برخلاف خبرهای منتشر شده در فضای مجازی و فضاسازی برخی رسانه‌ها؛ در بندرعباس، جزایر هنگام، لارک، قشم، جاسک و سیریک تا این لحظه انفجاری رخ نداده است
من هم فقط از کنارک در سیستان و بلوچستان پیام داشتم و از هرمزگان الان پیام‌هایی درباره شنیده شدن صدای پدافند در بندرعباس دارم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 381K · <a href="https://t.me/VahidOnline/77013" target="_blank">📅 22:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77012">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d63f96615c.mp4?token=PsxUQkK-bdSaD5j75DMzNscgWcP0CZAOvL1-KLb-FdgTzSLyqQ3EwEwDYra-scm-0odfA7NbpZQ7UcPIVB7bVaHaHkSvhkS3HdSjbgzrfswwiFgYqhgGYlz3HyOrTTYRCO59LOdmSKkBOSM00B80aKUvUfbiYBcva2Ls2oKkYsjJFl-_nQVyAe-IJkBBYU2XSYO8VFp9XUyIYfNbWOCZtvrc6ebhkF4p9QneBChcfcfFX4tqoExmB-AwFOU0ZpdjVjpwzOnXR2Q9d7JZP3tWgGQvftSJ9ykjW-K3kNdjzp60v81yZ2zQhf8qsUnEEEJxVzeGODUt50C5C50r62fiEw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d63f96615c.mp4?token=PsxUQkK-bdSaD5j75DMzNscgWcP0CZAOvL1-KLb-FdgTzSLyqQ3EwEwDYra-scm-0odfA7NbpZQ7UcPIVB7bVaHaHkSvhkS3HdSjbgzrfswwiFgYqhgGYlz3HyOrTTYRCO59LOdmSKkBOSM00B80aKUvUfbiYBcva2Ls2oKkYsjJFl-_nQVyAe-IJkBBYU2XSYO8VFp9XUyIYfNbWOCZtvrc6ebhkF4p9QneBChcfcfFX4tqoExmB-AwFOU0ZpdjVjpwzOnXR2Q9d7JZP3tWgGQvftSJ9ykjW-K3kNdjzp60v81yZ2zQhf8qsUnEEEJxVzeGODUt50C5C50r62fiEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، روز دوشنبه ۲۳ تیرماه در گفتگو با شبکه خبری فاکس با اشاره به ایران از لغو توافق اسلام‌آباد خبر داد و اعلام کرد واشنگتن از این پس رویکردی به‌شدت سخت‌گیرانه اتخاذ خواهد کرد.
ترامپ با بیان اینکه «توافق نهایی شده بود، اما بعد آن‌ها آن را زیر پا گذاشتند»، تاکید کرد: «آن‌ها همیشه توافق‌ها را زیر پا می‌گذارند. ما با این افراد ۱۰ توافق داشته‌ایم، بنابراین، ما به‌شدت آن‌ها را هدف قرار خواهیم داد.»
او اعلام کرد آمریکا کنترل مستقیم تنگه هرمز را بر عهده خواهد گرفت، چرا که دیگر حاضر نیست به صورت رایگان از امنیت این آبراهه کلیدی محافظت کند و کشورهای ثروتمند هم‌پیمان باید تمام هزینه‌ها را بازپرداخت کنند.
رئیس‌جمهوری آمریکا همچنین با اشاره به سرکوب شدید معترضان در ایران گفت آن‌ها تاکنون ۵۲ هزار نفر را کشته‌اند و با ایجاد فضای ارعاب، جرات اعتراض را از مردم گرفته‌اند.
او در پایان با تاکید بر اینکه «آن‌ها گروه بدی هستند و مدت‌هاست که همین‌طور بوده‌اند»، خاطرنشان کرد که این گروه اکنون در حال متحمل شدن سنگین‌ترین ضربات ممکن هستند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/77012" target="_blank">📅 22:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77011">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Cjy9KvVGH6-ESMA497KsByL5YSwgNTcS9MUHv12UIaADR2J0WKn7xWSo7Yv5I2sQ1win-lDSQfaK82OiZOYZG_Q9vqvdPyy9S9t1auQHIkAjy1oaflF7PtcBFMpWlUX63MgSnxL0SRh0zcTtSrmT7oKoy-HgJJMrU-pBJLrchx-d4COEl1kvcwV6lHx6CsW3RcTU6sE9x2uvSPjVzKaLzCO4Db8R-DTFXdOKkLYZkVUMbxQB-I644a4cumlkHVLbA0Ckj72stY9iV4sx7MQDGZBY1Fpb__tOoE1yTo4G7l24_Vgs8SnxhdXi_Tqvet2orupK1O3GsZ0fPvYL0ahD1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک‌تایمز گزارش داد دونالد ترامپ، رییس‌جمهوری آمریکا، به‌طور رسمی کنگره را در جریان ازسرگیری درگیری‌ها با ایران قرار داده است.
بر اساس نامه‌ای که جمعه برای رهبران کنگره ارسال شده و نیویورک‌تایمز به آن دست یافته، ترامپ نوشته است نیروهای آمریکایی ۱۶ تیر «حملات دفاعی علیه اهدافی در داخل ایران» انجام داده‌اند.
به نوشته نیویورک‌تایمز، این نامه بار دیگر اختلاف میان کاخ سفید و کنگره بر سر اختیار رییس‌جمهوری برای ادامه جنگ با جمهوری اسلامی بدون مجوز کنگره را تشدید کرده است.
هر دو مجلس پیش‌تر به طرحی رای داده بودند که ترامپ را ملزم می‌کرد جنگ را پایان دهد یا برای ادامه آن از کنگره مجوز بگیرد، اما کاخ سفید همچنان تاکید دارد که ترامپ در چارچوب اختیارات قانون اساسی خود به‌عنوان فرمانده کل قوا عمل می‌کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/77011" target="_blank">📅 22:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77010">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">پیام‌های دریافتی:
ساعت 10:09 دقیقه حدودا سه انفجار در کنارک
سلام کنارک دارن میزنن
سه تا پشت سر هم زدن
۴ تا زد همین الان کنارک 12: 10
کنارک بد میزنه حاجی
چهار انفجار همزمان
خونه ها لرزیدن
6 تا انفجار وحشتناک اطراف کنارک شنیده شد
ایرنا:
🔹
خبرنگار ایرنا در استان هرمزگان از شنیده شدن صدای چهار انفجار در شرق بندرعباس خبر داد.
تسنیم:
منابع محلی از شنیده شدن صدای چند انفجار از بندرعباس خبر می‌دهند. این در حالی است که به گفته منابع محلی حملات موشکی و هوایی به مناطقی از لارک و کنارک هدف حمله دشمن بوده است به طوری که گزارش از ۴ انفجار سنگین در کنارک حکایت دارد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/77010" target="_blank">📅 22:11 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77009">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4930898fcb.mp4?token=tHnY1Oq7YnLPh-CSX3rg3Z1-wLXhtGcukGHwShH2DGpRV10vQYOPvQe0oPy8aK4mvJzACnqLav4OfPQwpghT6lgyNCVn9ycOG8YD8D_CbfxVoqely-aHpYA3zmQFQxzvksZdobrOFgfxZY-rMpCSZsQ1yX2B83SOcxY4--u7WaGYHuUcCo9e6rZCXpe4kY5363jtQpO1v_m0vwPlUWLvs1w74jYA5qb1zjvNGUOty9MZB-Fmw6E_o7BTNuMG7C_zBCWREs-hSONHAaUpoYZW1J-qEw-I-jz5qlUScaan4Dz53p0FNvcctziVKTWKi1TnJEgyz4-lg5L79cxD3iIdLw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4930898fcb.mp4?token=tHnY1Oq7YnLPh-CSX3rg3Z1-wLXhtGcukGHwShH2DGpRV10vQYOPvQe0oPy8aK4mvJzACnqLav4OfPQwpghT6lgyNCVn9ycOG8YD8D_CbfxVoqely-aHpYA3zmQFQxzvksZdobrOFgfxZY-rMpCSZsQ1yX2B83SOcxY4--u7WaGYHuUcCo9e6rZCXpe4kY5363jtQpO1v_m0vwPlUWLvs1w74jYA5qb1zjvNGUOty9MZB-Fmw6E_o7BTNuMG7C_zBCWREs-hSONHAaUpoYZW1J-qEw-I-jz5qlUScaan4Dz53p0FNvcctziVKTWKi1TnJEgyz4-lg5L79cxD3iIdLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام: نیروهای آمریکایی محاصره دریایی ایران را از سر می‌گیرند
ترجمه ماشین:
تامپا، فلوریدا — بنا به دستور فرمانده کل قوا، نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) از ساعت ۴ بعدازظهر روز ۱۴ ژوئیه به وقت شرق آمریکا [ساعت ۲۳:۳۰ فردا سه‌شنبه به وقت تهران]، محاصره تردد دریایی ورودی به بنادر ایران و خروجی از آن‌ها را از سر خواهند گرفت.
نیروهای سنتکام این محاصره را علیه شناورهایی که به مقصد بنادر و مناطق ساحلی ایران یا از مبدأ آن‌ها در حرکت‌اند، اعمال خواهند کرد. ارتش ایالات متحده همچنان از جریان تردد در آب‌های منطقه برای تمام شناورهایی که محاصره را نقض نمی‌کنند، پشتیبانی خواهد کرد.
ازسرگیری محاصره ایران از سوی آمریکا پس از اجرای اولیه آن از ۱۳ آوریل تا ۱۸ ژوئن صورت می‌گیرد. نیروهای سنتکام در این دوره دوماهه، مسیر بیش از ۱۴۰ شناورِ تابع مقررات را تغییر دادند، ۹ کشتیِ متخلف را از کار انداختند و به بیش از ۵۰ کشتی تجاری حامل کمک‌های بشردوستانه اجازه دادند از محدوده محاصره عبور کنند.
به همه دریانوردان توصیه می‌شود هنگام فعالیت در دریای عمان و مسیرهای ورودی تنگه هرمز، پیام‌های «اطلاعیه به دریانوردان» را دنبال کنند و از طریق کانال ۱۶ ارتباط پل‌به‌پل با نیروهای دریایی ایالات متحده تماس بگیرند.
اطلاعات تکمیلی از طریق یک اطلاعیه رسمی در اختیار دریانوردان تجاری قرار خواهد گرفت.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/77009" target="_blank">📅 21:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77008">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZXAhYS7Ve4Jfh6LcZbRU9BewCXrAdUUjaFRPVqma523bZ-DJy1NhzvUAUYKhvtC4FPaPML1PuEhfaUnLyKJ9abXybMOGBTAGEFwhrl404vIffV2_kZTJCuIOgqc8VLFIm3XulVHgN5BJrGcTxqaAIB3kQmUBMJf6Ruh4gp2lxk0UU1UgyvbckkFbEtsGNxQIHTq6TKUsOz8QJL0X60kOk88S6IcqOUcCzSCBeXDDMo9AFse03iqFnn5RJ01mtOYYg1FBW6ewmudEQInNQdhNYr6TXr3_Eyc53CIZLmo6gg5MY46oBYrPEO-U7QRsyQUKrLsoKTOcy17TUtNgBHSfgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روز دوشنبه ۲۲ تیرماه و دقایقی پس از اعلام تعطیلی سراسری دو روزه در هرمزگان، استاندارای‌های خوزستان و بوشهر نیز از تعطیلی و محدودیت ساعات کاری این دو استان جنوبی در روزهای سه‌شنبه و چهارشنبه ۲۳ و ۲۴ تیرماه خبر دادند.
خبرگزاری‌های دولتی ایران، دلیل این تعطیلی را «افزایش بی‌سابقه دمای هوا و به منظور حفظ پایداری شبکه برق کشور» اعلام کرده‌اند.
بر اساس اطلاعیه استانداری بوشهر، تمامی ادارات و دستگاه‌های اجرایی این استان در روز چهارشنبه به طور کامل تعطیل خواهند بود و ساعت کاری آن‌ها در روز سه‌شنبه نیز تا ساعت ۱۱ کاهش یافته است.
هم‌زمان، استانداری خوزستان نیز اعلام کرد با توجه به شدت گرما، ادارات این استان در روز چهارشنبه به صورت دورکار فعالیت خواهند کرد و روز سه‌شنبه نیز همانند استان همسایه، تا ساعت ۱۱ دایر خواهند بود.
تعطیلی در استان‌های جنوبی در حالی اعلام می‌شود که در پی افزایش تنش‌ها در تنگه هرمز، ارتش آمریکا در پنج روز گذشته حملات گسترده‌ای را به شهرهای مختلف به این استان‌ها انجام داده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/77008" target="_blank">📅 21:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77006">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AJaN5mfF910RKTC-d9Wnow1vYA0C-mOmO2vX0KoOU-0_MgxkHTybE0U7NopMXB_dfrnHLpo9Wrdx0gaF56plC9rs8MZR_EgP_NydF0Fih7VVw-FdFF5NjTUQ0UrsV3e68zSQHNx0hcltPm54SAlr2pKCax78c8elOS82F72OH_GjwC4FZqGpqCmhFt9KhzsPgDC8-2JonsofR8ow4dP8oclhkSKfoDY9Y6TW9y2qewyIDRUDblajZQzoS1YdBorALZ5wSGyI_DVP6HkRHCok1ZAvN0CHumCIdxm_ATNbbSiCefs8JEkRy9NW1DixQGVvtmjh3cYLO5DKQH3t5Qqtrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس عراقچی، ترجمه ماشین:
رئیس‌جمهور آمریکا کاملاً درست می‌گوید. هر کسی که عبور امن و بی‌خطر کشتی‌های تجاری از تنگه هرمز را تأمین می‌کند، باید بابت این خدمت غرامت دریافت کند.
ایران همیشه «نگهبان» تنگه بوده و تا ابد نیز خواهد ماند.
البته ۲۰ درصد بیش از حد زیاد است. ما منصف خواهیم بود.
araghchi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/77006" target="_blank">📅 21:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77005">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MwqTWA2JTB3lvpDbV-pUIbOV1EI0tnmymANPRNifjXSduA3SWslghmRN9uukf6KJ9X-xBwzAic4eCMSzxPugz7YlPzsORviKpC2nk-JG9gc2xsU2fLC5Ixa4pUjy-5agJAdocJwI-7-yY-DCzvZthB1XrGIFtsOUhj1JqD1dFDQ8Fbcfh9B12ztuuzy9V3-kOke7ebUdB1ABaYZ48ZlSnyLJckr1pqDZ4hIomQ7g0oEyw2mE1vQmWX_V6UtkhPH0Z-OUwM7aLyc3jWZowYUjxT4B5W7r9IQzGyWyyLiya0HSnN0f5IPTYln113DiHuxXwiooS3C2U8bsEP4LvzlQ2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدرضا پاکروان، معاون استاندار هرمزگان، روز دوشنبه ۲۲ تیرماه، از تعطیلی تمامی دستگاه‌های اجرایی، ادارات، بانک‌ها، مراکز آموزشی و دانشگاه‌های این استان در روزهای سه‌شنبه ۲۳ و چهارشنبه ۲۴ تیرماه خبر داد.
این مقام استانداری هرمزگان در گفتگو با خبرگزاری مهر اعلام کرد: «این تصمیم با توجه به بررسی‌های کارشناسی، موافقت استاندار و مصوبه کارگروه انرژی استان به دلیل افزایش شدید دمای هوا اتخاذ شده است.»
به گزارش مهر، مراکز خدمات‌رسان، درمانی، امدادی، امنیتی و انتظامی برای ارائه خدمات دایر خواهند بود و
امتحانات نهایی دانش‌آموزان و دانشجویان طبق برنامه قبلی برگزار می‌شود.
این خبر در حالی منتشر می‌شود که در پی اقزایش تنش‌ها در تنگه هرمز، ارتش آمریکا از بامداد ۱۷ تیرماه حملات گسترده‌ای را به شهرهای مختلف این استان ساحلی انجام داده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/77005" target="_blank">📅 21:11 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77004">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kd9XFDekEkhQo7QlEfSElcahJykTPcVfc4rTxh_qS3p5l3h8K4wqBrntv7uL8DH61Zon86B1oFlPvrwUN4FzOi_q8ea_jjDLIIsR4zaDHtOz4y4J_vXsKLedimmNMheQ3h0oIBgjyIobHmFqbvGN1p5SQ34SDdhJfm4TbLZi3eZnCidZHLHm5FYlzxmkJi1ptoRnFLmm_NptSe29rxcO9NR-K_HFy_OKCn9o0lcSoAJ2W5QosRwWiGGkEhLzV1PMrpCe1VL-c8xcXMnpN6ywz2V4UcU9jafAyKeuq-iHQESBdcuR45fTrp2niEOJzeYgni3AcnC7DdWMS3Dhort-sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تام کاتن، سناتور، ترجمه ماشین:
رئیس‌جمهور ترامپ حق دارد که به‌دلیل زیر پا گذاشتن قول از سوی رژیم ایران، هزینه‌های سنگینی بر آن تحمیل کند.
در برابر حملات تروریستی ایران علیه همسایگانش و در تنگه هرمز نباید هیچ‌گونه مماشاتی صورت گیرد.
برقراری دوباره محاصره، رژیم را بیش از پیش فلج خواهد کرد و اجازه خواهد داد نفت برای متحدان و دوستان ما از طریق تنگه جریان یابد.
SenTomCotton
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/77004" target="_blank">📅 21:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77003">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDBySNlwhmg5CcTHjJ-jkeN-fePPwjZkwDIYXPfUdtYtxASQevYDEJDFFVpwEwYrkd7Fg8HrMdV5NTYRoYCNHgkSwut1oCUBEEAp6kqSKEE0LgwiYELFwWtY-Y29KI3Tzow71yhf5SvCBP9EaLdHXHLsaJp0zA-P7zKgaUDDqjGa1sTWs_ToGSTyu4zWyVyKFdQFuiRZcCZTX92YFPC5CwGit700Xv8-3tyDYeCiXUMH3iOP_QtEVXmlpWKRRylYbJ8Q_TSjXqVaT_gNOlx1wvxAVP0DpIx6FQ0MxL4LnTDNbBgauV8r2umA_LCicD0j6bkNrRGV63iZPopx6_mDXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وبسایت اکسیوس روز دوشنبه گزارش داد که اعمال دوباره محاصرهٔ دریایی ایران هنوز اجرایی نشده است، زیرا طبق الزامات قانونی باید ۲۴ ساعت پیش از آن به مالکان کشتی‌ها اطلاع داده شود.
یک مقام آمریکایی به این وبسایت گفته که فرماندهی مرکزی آمریکا، سنتکام، زمان دقیق اجرا را اواخر روز دوشنبه اعلام خواهد کرد.
یک منبع ارشد در خلیج فارس به آکسیوس گفت ایالات متحده موضوع دریافت عوارض احتمالی برای تأمین امنیت تنگه هرمز را با متحدان خود در منطقه مطرح نکرده است.
دونالد ترامپ رئیس‌جمهوری ایالات متحده روز دوشنبه اعلام کرد که محاصره دریایی ایران بار دیگر برقرار می‌شود.
او همچنین تصریح کرد که آمریکا به‌عنوان «نگهبان تنگهٔ هرمز» شناخته خواهد شد، اما ۲۰ درصد از ارزش همهٔ محموله‌های عبوری را به‌عنوان هزینه دریافت می‌کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/77003" target="_blank">📅 20:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77002">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QxQgMW9kunfFe_kA6c4ASZygBcfl1-crd57FfZKt8qkOqtZWzj23WA4axWEd97cz-_9d2hisEU8c5ZeK9N66K51SY48Vilc5Qy6KEYYgUGjpUKxHU8_HJcbDuczRIxe4qrUZQ2qPep_7a7KuWN4QLET9CeMAGVtdd0yXRHb40KNpDp1gLuq6iUiSjyWpm4Lf6tvs-xWNT9OEQQN6yCfDSUZiaTJHMjD5JxGq29ZzYdrVH1rzBIpPXJdJ3N4MmTXQiOHb53ejRJefNIs0YaOyTepMVOu84SfquQwiX5Mk4RuFiG0KL2kzF-vDgtw7xRNuRJ25Ss6N9YY3FQnkKhtZCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه آمریکایی نیویورک‌تایمز در گزارشی اختصاصی که روز ۲۲ تیر ۱۴۰۵ منتشر کرد، از تلاش چندساله سرویس اطلاعاتی اسراییل برای جذب محمود احمدی‌نژاد، رییس‌جمهور پیشین ایران، به‌عنوان یک عامل اطلاعاتی خبر داد؛ طرحی که هدف نهایی آن، به گفته این روزنامه، نصب او در راس نظام سیاسی ایران پس از سرنگونی حکومت فعلی بود.
بر اساس این گزارش که به نقل از منابع آگاه آمریکایی و ایرانی تهیه شده، ماموران موساد طی چند سال گذشته در سفرهای خارجی احمدی‌نژاد با او دیدار کرده و حتی هزینه‌های مسکن و رفت‌وآمد او را تامین کرده‌اند. «دیوید بارنیا»، رییس پیشین موساد که پنج سال این نهاد را اداره می‌کرد، شخصا برای دیدار با احمدی‌نژاد به بوداپست سفر کرده و به گفته مقام‌های سابق آمریکایی، موساد، موضوع تماس با احمدی‌نژاد را به‌طور رسمی به سازمان سیا اطلاع داده بود.
...
بر اساس این گزارش، در ۹ اسفند یک حمله هوایی اسراییل به محل اقامت احمدی‌نژاد صورت گرفت که ساختمان محافظان و خودروی زرهی او را هدف قرار داد.
به گفته چهار مقام ارشد ایرانی، پس از این حمله یک خودروی پژو مشکی‌رنگ در صحنه حاضر شده و احمدی‌نژاد را با سرعت از محل خارج کرده بود.
منابع آمریکایی و ایرانی آگاه از این عملیات گفته‌اند راننده این خودرو از ماموران موساد بوده و احمدی‌نژاد را به یک خانه امن در داخل ایران منتقل کرده است.
اما طبق این گزارش، این طرح در نهایت ناکام ماند. احمدی‌نژاد از شیوه اجرای این عملیات نجات ناراضی بوده و به گفته افراد آگاه از جریان ماجرا، نسبت به برنامه اسراییل برای بازگرداندن او به قدرت دچار دلسردی شده بود. او سرانجام خانه امن را ترک کرد، هرچند شرایط دقیق این خروج همچنان نامعلوم است.
احمدی‌نژاد از آن زمان تا دوشنبه هفته گذشته، که برای لحظاتی کوتاه در مراسم تشییع پیکر آیت‌الله علی خامنه‌ای، رهبر فقید ایران، ظاهر شد، در هیچ رویداد عمومی دیده نشده بود. در تصاویر منتشرشده از این مراسم، او با وجود گرمای هوا ژاکتی ضخیم بر تن داشت و ماسک جراحی را تا زیر چانه پایین کشیده بود؛ در حالی که سرش به زیر افتاده و از هر سو افرادی که به‌نظر محافظ می‌رسیدند او را احاطه کرده بودند. حسن روحانی و محمد خاتمی، دو رییس‌جمهور پیشین دیگر ایران، به این مراسم دعوت نشده و در هیچ‌یک از تشریفات مربوط به تشییع حضور نداشتند.
به گفته چهار مقام ارشد ایرانی، احمدی‌نژاد اکنون در بازداشت واحد اطلاعات سپاه پاسداران به‌سر می‌برد، پس از آنکه نهادهای اطلاعاتی ایران بخش عمده‌ای از ارتباطات او با اسراییل را کشف کردند.
...
متن کامل:
telegra.ph/ahmadinejad-07-13-2
هم‌زمان گزارش مشابه دیگری از هاآرتص: @
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 363K · <a href="https://t.me/VahidOnline/77002" target="_blank">📅 18:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77001">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/246c412fdb.mp4?token=qS0Cn9dsZIoq8Wz9O7N58j-wMR1fnhsW5kQWd5w6UsZiwBsl6d33RuFXphTpRGM4ZvkE6MYAvlg7IJ2_a2_EUORwA_6zG3-bmh_888h0ZKD_cXV3YBwn6-DhbN7RfR6HyhwwvRLUe59i8yiXkFLSSkRovvmBacZrJPI4hUthNJzxiVSM8A1ZPWNwoEpyRrtf4bgA_rwbmkRzzW2aMGOUoauzvUTGpUGRvSV03WR76inKDAwdUTuyd6BqXzBvJMlkPg1XSWZ2tHmcpsWgtBv3pR95Rwt3zybZ-aeyTD6GsdHhotX0k_Ss2KYjfeL9jCudCYArrETWtAvS9j4hgjgRVw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/246c412fdb.mp4?token=qS0Cn9dsZIoq8Wz9O7N58j-wMR1fnhsW5kQWd5w6UsZiwBsl6d33RuFXphTpRGM4ZvkE6MYAvlg7IJ2_a2_EUORwA_6zG3-bmh_888h0ZKD_cXV3YBwn6-DhbN7RfR6HyhwwvRLUe59i8yiXkFLSSkRovvmBacZrJPI4hUthNJzxiVSM8A1ZPWNwoEpyRrtf4bgA_rwbmkRzzW2aMGOUoauzvUTGpUGRvSV03WR76inKDAwdUTuyd6BqXzBvJMlkPg1XSWZ2tHmcpsWgtBv3pR95Rwt3zybZ-aeyTD6GsdHhotX0k_Ss2KYjfeL9jCudCYArrETWtAvS9j4hgjgRVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرماندهی مرکزی ایالات متحده (سنتکام): یک تأسیسات نگهداری زیردریایی و کشتی در ایران برای نخستین‌بار با استفاده از شهپاد هدف قرار گرفتند
ترجمه ماشین:
دیروز، نیروهای سنتکام با استفاده از چندین شناور سطحی تهاجمی یک‌طرفه، با موفقیت یک زیردریایی و یک تأسیسات تعمیر و نگهداری کشتی در ایران را هدف قرار دادند. سه شناور سطحی بدون سرنشین «کورسِر» به بندر پایگاه دریایی بندرعباس اصابت کردند؛ رویدادی که نخستین استفاده نیروهای آمریکایی از پهپادهای دریایی در عملیات رزمی را رقم زد. حملات شب گذشته توانایی ایران برای ادامه حمله به کشتیرانی تجاری را کاهش داد.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/77001" target="_blank">📅 18:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77000">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Bs3iOfLanvrLV1tElpURXoBg96OhW72OXy2XFthVprTH_8ScxXtyU_sSXudv4cwmQ2Hq25noV2lIhTEQIXYyZxh9PkLwKcn-U0N3lbsY6lVuId-UMxaP-slJwQt_JESsn6KmFgETnc5F5QlcIaRpjd7D2rErbGHXYraNUI0BxL6GFcEruXOIeP3GsUyIWOA4SYL8-CulHr5iGHON_GCt4rTrNakmKo4YDYKjjLy3I_EeWUJevhxSAqK0G8YXLaULGFyPKJsNTOzcz2rF0qpqsqHNZAyb4gjVlqUNt4XzkG9ZWEAtRRXOTflzwYscNfoufbB40Dryezr4lN2DU4RkDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: محاصره دریایی ایران را دوباره برقرار  می‌کنیم
ترجمه ماشین:
تنگه هرمز باز است و با ایران یا بدون ایران، باز خواهد ماند.
ما «محاصره ایران» را دوباره برقرار می‌کنیم؛ این نام به این دلیل انتخاب شده که این محاصره فقط مانع ورود یا خروج کشتی‌ها یا مشتریان ایران می‌شود. همه کشورهای دیگر امکان استفاده آزادانه و منصفانه از تنگه را خواهند داشت.
از این پس، ایالات متحده آمریکا با عنوان «نگهبان تنگه هرمز» شناخته خواهد شد؛ اما در مقام چنین نقشی و از سر انصاف، بابت تمامی هزینه‌های لازم برای تأمین ایمنی و امنیت این بخش بسیار پرتنش جهان، معادل ۲۰ درصد ارزش تمام محموله‌های حمل‌شده را دریافت خواهد کرد.
روند اجرا و تشکیل این سازوکار بلافاصله آغاز خواهد شد. از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/77000" target="_blank">📅 17:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76999">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c1f13be57b.mp4?token=lsOReTygYG-4-VKkabRnrB72fU4p64ApTJgfNAcLsSDvVZlk3Fe5da6yf8ssv-8s4BW33HtW5hOPmaCZg_SWfLyXcrUEdfCfqKkIbY4NmK0gnXV5MLMjCoG6O21wjeA4PfOrGCzkbneHQwwHc4t3yD5Xy_arzuO8Jc-h4DXo2VrXRfa8YkhCwFn0c6snzGrd8_7R2GCgdHFP8zODz30yaaBa6kLzuPtvbjqV7RQna6xeF3429nvy-NTSYEpaz6fdnqOH3UcGp7Y-qG4i2B6voVnxJt2ViC-5fiOWqd7xKFhKd0mq8pSIyehmxmx-WDHu0Ahl0xKvZfzIBsKD93Pagg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c1f13be57b.mp4?token=lsOReTygYG-4-VKkabRnrB72fU4p64ApTJgfNAcLsSDvVZlk3Fe5da6yf8ssv-8s4BW33HtW5hOPmaCZg_SWfLyXcrUEdfCfqKkIbY4NmK0gnXV5MLMjCoG6O21wjeA4PfOrGCzkbneHQwwHc4t3yD5Xy_arzuO8Jc-h4DXo2VrXRfa8YkhCwFn0c6snzGrd8_7R2GCgdHFP8zODz30yaaBa6kLzuPtvbjqV7RQna6xeF3429nvy-NTSYEpaz6fdnqOH3UcGp7Y-qG4i2B6voVnxJt2ViC-5fiOWqd7xKFhKd0mq8pSIyehmxmx-WDHu0Ahl0xKvZfzIBsKD93Pagg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ به شبکه فاکس‌نیوز گفت: خامنه‌ای مرده، پسرش ۹۰ درصد مرده است.
از زمان جنگ از مجتبی خامنه‌ای عکس، صدا یا تصویری منتشر نشده است و در انظار دیده نشده است.
دو روز پیش عکسی جدید در وبسایت رهبر جمهوری اسلامی منتشر شد اما نشانه‌ای از اخیر بودن در آن دیده نمی‌شد.
رئیس‌جمهور آمریکا بار دیگر تاکید کرد که نیروی دریایی، نیروی هوایی و پدافند ایران از بین رفته و رهبرانشان هم کشته شده‌اند.
او در این مصاحبه همچنین گفت دیروز پس از یک «جلسه ۱۱ ساعته» بر سر «همه چیز توافق شد» که اشاره‌اش به ایران بود.
او به جزئیات این جلسه اشاره نکرد.
او افزود: «کار اینها همیشه ۱۱ ساعت طول می‌کشد درحالی‌که باید یک دقیقه باشد... اما از اتاق که بیرون رفتند، دوباره تماس گرفتند و گفتند باید چند تغییر اعمال شود.»
دونالد ترامپ سپس افزود: «همیشه تغییراتی در کار است. می‌دانید، آنها مذاکره‌کنندگان حرفه‌ای هستند، کارشان همین است. البته من حتی نمی‌گویم در این کار مهارت دارند... آنها هیچ چیزی از من به دست نیاوردند.»
آقای ترامپ چند روز پیش هم گفته بود با ایران بر سر همه چیز توافق شده بود اما ساعاتی بعد آنها به یک کشتی تجاری در تنگه هرکز حمله کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/76999" target="_blank">📅 16:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76998">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uc-jFt7Ra29ZJJBFiD8JU6y7TIUwxj4nAnTZrDXlgvVXfOhQgB-QdyEMMo8wR_tonez3yYjYAMqu-n86kCc2FKN5EMLSjCxAdk2nwFFoR3XFQHIi4gJZuc6o_FSFjxN3-ePkX0DP9A7bNPVdOAycPyZxr9piO4R52qr-Vw8ckRmwUEbUHA0VRtw33xEu7kV-1azbdsoiX5yx7iFDCEScX4fXh24I3sTZPHEdUp0L6OVU5v2sqV1Swtm8APeWoBwCGSX2d26uJaQMQImPfi0GcEB76N9sB_arQMQQQLdSyhiKa1d0l9vWAOyKyXBXAoACXoYJUjZ4rA4jp2UqewoFEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، در گفت‌وگو با شبکه فاکس‌نیوز با اشاره به تحولات مربوط به ایران و تنگه هرمز گفت: «کنترل تنگه هرمز را به دست خواهیم گرفت.»
او افزود: «ما به یک توافق رسیده بودیم، اما آن‌ها آن را نقض کردند.»
ترامپ گفت ایالات متحده مسئولیت حفاظت از تنگه هرمز را بر عهده خواهد گرفت و افزود: «باید هزینه این کار به ما پرداخت شود. ما بابت حفاظت از این تنگه، پول دریافت خواهیم کرد.»
رییس‌جمهوری آمریکا همچنین درباره مقام‌های جمهوری اسلامی گفت: «آن‌ها گروهی بد هستند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/76998" target="_blank">📅 16:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76997">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGYv6TDprNyFkq_0vbLNGTiU0PsqxxE0Tlo-RI2dIqQNyi3lNs0LHIfkVjGOsYazcubR2cRbSiw-fcBbh5DegM-LJ3z4V4RFaxBrU5U5Lmc94zFfgyv01fmTO6mkbzZKmfZdkSe8azTOD_hHoA7i-s7_Oj0kT9p-TDc7JDHRmxoiYfZ6VAhVj2_VYDDfcBvlV3x3xZQb9JfbzCoFBlrNnOqxKbhUI_zcY_rylrnGvu_mFtofeY6GNwqhCvbF6_Ly5F-ek-z3U-TVXXSXYi0YcFgxonUMJ3csp5e2rZxqPUXrjSHkmSJi8nrOacqslNJEpNvZY11E9VQkWkpiKhjMog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت بریتانیا سپاه پاسداران انقلاب اسلامی را در فهرست سازمان‌های تروریستی قرار داد که بر اساس آن، عضویت در این نهاد، شرکت در نشست‌های آن و حمل نماد آن در انظار عمومی جرم کیفری خواهد بود.
سپاه پاسداران پیش‌تر به‌طور کامل مشمول تحریم‌های بریتانیا بود، اما دولت‌های مختلف در بریتانیا از اعلام آن به‌عنوان سازمان تروریستی خودداری کرده بودند.
لندن سال‌ها زیر فشار پارلمان و نهادهای امنیتی برای این اقدام بود. سازمان اطلاعات داخلی بریتانیا، ام‌آی‌فایو، اعلام کرده بود بیش از ۲۰ توطئه بالقوه مرگبار مرتبط با جمهوری اسلامی را خنثی کرده است.
دولت در ژانویه گفته بود سازوکار موجود برای ممنوع‌کردن نهاد وابسته به یک دولت خارجی مناسب نیست و در حال تدوین اختیارات قانونی تازه‌ای برای این کار بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/76997" target="_blank">📅 15:38 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76996">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c8171dfe95.mp4?token=e05RdbutLHZhSZqnkdx7UykZHbOH1wbauz1bItGgLcaCmF9xp3jTcWRb-DA5_loFz0QPVmPo-KT6G7mgMuvISisJipX2rvVWFBNbcQZkLcCBooH5KRhjM5lQyBoYcy4zS9Uf2YEZfmFfSYcB7vQ7RkkZl98Gte4CK33vTehjQ1v_u2zYirjTF_vQGy7eCrPul-i3Z_69WT8EbPRaZHlDln-IGG5UnFi67lr7scv4GKnwqpOAKNb5FstgspyJLIsOAhpRP5h9oRBdPLAZDCUiaFyH4nFt7VnyvAXLd9hg_3_GSDUK-CHSRNUA3QJQgRAh6UajnELcaH5f5VhnRrWC_w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c8171dfe95.mp4?token=e05RdbutLHZhSZqnkdx7UykZHbOH1wbauz1bItGgLcaCmF9xp3jTcWRb-DA5_loFz0QPVmPo-KT6G7mgMuvISisJipX2rvVWFBNbcQZkLcCBooH5KRhjM5lQyBoYcy4zS9Uf2YEZfmFfSYcB7vQ7RkkZl98Gte4CK33vTehjQ1v_u2zYirjTF_vQGy7eCrPul-i3Z_69WT8EbPRaZHlDln-IGG5UnFi67lr7scv4GKnwqpOAKNb5FstgspyJLIsOAhpRP5h9oRBdPLAZDCUiaFyH4nFt7VnyvAXLd9hg_3_GSDUK-CHSRNUA3QJQgRAh6UajnELcaH5f5VhnRrWC_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از حملات متعدد به باند فرودگاه صنعا امروز ۲۲ تیر منتشر شده است.
وزارت دفاع دولت یمن، که از حمایت عربستان برخوردار است، اعلام کرد که باند فرودگاه بین‌المللی صنعا را هدف قرار داده‌اند تا از فرود یک هواپیمای ایرانی جلوگیری کنند.
حوثی‌ها، که متحد [حکومت] ایران هستند و کنترل فرودگاه بین‌المللی صنعا را در دست دارند، عربستان را متهم کردند و گفتند به ان پاسخ خواهند داد.
بعد از حمله به فرودگاه صنعا گزارش شد که یک هواپیمای ماهان ایر در فرودگاه حدیده به زمین نشسته است. ویدیوهای منتشر شده نشان می‌دهد مسافران این هواپیما پیاده شده‌اند. خبرگزاری فارس اعلام کرد هیئت رسمی یمن به سلامت در حدیده از هواپیما پیاده شدند.
پبش از این هم یک پرواز شرکت هوایی ماهان ۱۳ تیر به صنعا رفته و ساعاتی بعد به تهران بازگشت. این پرواز ساعاتی پس از آن انجام شد که گفته شد «توافقنامه حمل و نقل هوایی میان اداره کل حمل و نقل هوایی یمن و شرکت هواپیمایی ماهان ایر» ایران امضا شده است که بر اساس آن «۱۴ سفر هوایی در هفته از سوی ایران و یمن می‌تواند انجام شود.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/76996" target="_blank">📅 15:09 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76995">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">پیام‌های دریافتی یک ساعت و نیم پیش:
‌
درود بندرعباس ساعت ۱۲:۳۱ دقیقه انفجار شد
بندرعباس انفجار ۱۲:۳۱
بندرعباس دو انفجار شدید
پایگاه هوایی 12:31
سلام بندرعباس ۱۲:۳۰ صدا انفجار اومد پایگاه هوایی فکر کنم زدن
سلام دارن بندرعباسو میزنن خداحافظ
آبادان بریم صدا اومد 13:19
صداش هم با لرزش بود ینی احتمالا درست شنیدم
صدای انفجار اومد تو ابادان
کجا بود و نمیدونم
هرچی بود اطراف پالایشگاه بود احتمالا باز پدافند الفی یا جزیره مینو
سلام وحید جان، صدای انفجار در آبادان
سه بار شنیدیم
ساعت ۱۳:۲۷
بندرعباس
ساعت ۱۲:۳۰ ظهر امروز دو تا انفجار بزرگ تو پایگاه هوایی رخ داد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/76995" target="_blank">📅 15:06 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76994">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/aad6931866.mp4?token=DTvT-mKITaTTcnoUnRH_sUIWnUEs2BQDnxIIMeY8R54oIUXOn-Dt2LGW_TkwBCSow6qYOYr7nlAWm8aY35t-gIQohfSHOwLo3px3u7zGPyIbqr8DmBXczyDkDDYAAv_VO56bIrg7hbNZxNn4drBqQCceF4y6457GpTmxDkRrdHUkK9vvy6aWuRpzCXVuOVmhAugUK2gcNgvF11WsLLb96oCzgagN-SRbhBlScohdwPVEjkkDft7i8J2wz8ejqlLv9XFzltL-kPkvqMWS_zqyYarXOwvCNHdWM2Isef4O0XxUxQ9K6TCPyNA_GBo6WZ7WFjfyVdbxKwanEcKseAWEcA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/aad6931866.mp4?token=DTvT-mKITaTTcnoUnRH_sUIWnUEs2BQDnxIIMeY8R54oIUXOn-Dt2LGW_TkwBCSow6qYOYr7nlAWm8aY35t-gIQohfSHOwLo3px3u7zGPyIbqr8DmBXczyDkDDYAAv_VO56bIrg7hbNZxNn4drBqQCceF4y6457GpTmxDkRrdHUkK9vvy6aWuRpzCXVuOVmhAugUK2gcNgvF11WsLLb96oCzgagN-SRbhBlScohdwPVEjkkDft7i8J2wz8ejqlLv9XFzltL-kPkvqMWS_zqyYarXOwvCNHdWM2Isef4O0XxUxQ9K6TCPyNA_GBo6WZ7WFjfyVdbxKwanEcKseAWEcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام: سنتکام موج دیگری از حملات علیه ایران را به پایان رساند
ترجمه ماشین:
تامپا، فلوریدا — نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) در ۱۲ ژوئیه موج جدیدی از حملات تهاجمی علیه ایران را به پایان رساندند و با مهمات هدایت‌شونده دقیق، ده‌ها هدف را در چندین نقطه مورد اصابت قرار دادند تا توانایی ایران برای ادامه حمله به کشتیرانی بین‌المللی در حال عبور از تنگه هرمز را تضعیف کنند.
نیروهای سنتکام با استفاده از جنگنده‌های آمریکایی، شناورهای نیروی دریایی، پهپادهای تهاجمی یک‌طرفه و برای نخستین بار، شناورهای بدون سرنشین تهاجمی یک‌طرفه، سامانه‌های پدافند هوایی ارتش ایران، سایت‌های راداری ساحلی، توانمندی‌های موشکی و پهپادی و قایق‌های کوچک را هدف قرار دادند.
تنگه هرمز یک کریدور دریایی حیاتی برای تجارت جهانی است. ایران کنترل آن را در اختیار ندارد.
نیروهای ایالات متحده در وضعیت استقرار و آمادگی قرار دارند تا تضمین کنند که با وجود ادامه تجاوزهای بی‌دلیل، مزاحمت‌ها، تهدیدها و اعلامیه‌های خودسرانه ایران، آزادی کشتیرانی همچنان برای کشتی‌های تجاری برقرار بماند.
CENTCOM
سپاه: پایگاه آمریکا در بحرین را نابود کردیم
اطلاعیه روابط عمومی سپاه پاسداران انقلاب اسلامی به نقل از منابع حکومتی:
بسم الله قاصم الجبارین
وَقَاتِلُوهُمْ حَتَّىٰ لَا تَكُونَ فِتْنَةٌ وَيَكُونَ الدِّينُ كُلُّهُ لِلَّهِ
🔺
رژیم شرور و جنگ زیست آمریکا که از آغاز تاسیس تاکنون زمان‌های اندکی را بدون جنگ و شرارت نظامی سپری کرده و از شکست‌های اخیر در مواجهه با رزمندگان اسلام هم درس عبرت نگرفته و به تجاوزات خود ادامه می‌دهد.
🔺
در پاسخ به این شرارت‌ها، رزمندگان هوافضای سپاه در مرحله دوم عملیات مقابله به مثل خود مراکز مهم تعمیرات و نگهداری بالگردی، آشیانه هواپیمای جنگ الکترونیک پی ۸ و مرکز فرماندهی و کنترل پهپادی ارتش کودککش آمریکا در پایگاه آمریکا در شیخ عیسی بحرین را در هم کوبیدند.
🔺
عملیات مقابله به مثل ادامه دارد.
إِنْ تَنْصُرُوا اللَّهَ يَنْصُرْكُمْ وَيُثَبِّتْ أَقْدَامَكُمْ
سپاه: آمریکا را در کویت منهدم کردیم
بسم الله قاصم الجبارین
وَقَاتِلُوهُمْ حَتَّىٰ لَا تَكُونَ فِتْنَةٌ وَيَكُونَ الدِّينُ كُلُّهُ لِلَّهِ
🔹
به استحضار مردم شریف ایران می‌رسانیم، رزمندگان پرافتخار نیروی هوافضای سپاه، در سومین مرحله از عملیات مقابله به مثل و پاسخ به تجاوزات رژیم مستکبر و متجاوز آمریکا، مخازن سوخت و سامانه پدافند هوایی پاتریوت در پایگاه آمریکایی در علی سالم کویت و همچنین یک سامانه راداری راهبردی FPS در پایگاه احمد الجابر را به طور کامل منهدم کردند.
🔹
عملیات مقابله به مثل فرزندان غیور شما ادامه دارد.
🔹
تنگه هرمز سرزمین ماست و اجازه نخواهیم داد یک ارتش یاغی و کودک‌کش از آن سوی دنیا به دخالت‌های غیرقانونی خود در آن ادامه دهد.
إِنْ تَنْصُرُوا اللَّهَ يَنْصُرْكُمْ وَيُثَبِّتْ أَقْدَامَكُمْ
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 433K · <a href="https://t.me/VahidOnline/76994" target="_blank">📅 06:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76992">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">پیام‌های دریافتی:
درود همین الان صدای انفجار بندرعباس
ساعت 5:47 یک انفجار بندرعباس
سلام وحید
صدای انفجار  الان توی بندرعباس
خیلی شدید بود
سلام بندرعباس الان صدای انفجار اومد ۵:۴۸
سلام وحید 5:47 دقیقه بندرعباس صدای انفجار اومد
۵:۴۸ بندرعباس صدای بلند
05:48 بندرعباس صدای انفجار، خیلی زیاد بود صداش
5:48 انفجار مهیب در شرق بندرعباس
فاصله یک ساعت و نیمی ازمون نهایی صدای انفجار مهیب بندرعباس
سلام ۵:۴۹ بندرعباس یه صدای انفجار شدید اومد
سلام همین الان صدای موشک در بندر عباس شنیده شد
همین الان بندر عباس صدای انفجار ساعت ۵:۵۰
بندرعباس
ما ۱۲ فروردین هستیم
کامل شیشه لرزیدددد
درود آقا وحید همین الان
بندرعباس انفجار خیلی شدید
بندرعباس الان صدای انفجار همرا با لرزش شدید
5:47تک انفجار بندرعباس
صدای انفجار نسبتا شدید بندرعباس
بندرعباس همین الان انفجار خیلی شدید از توی خواب پریدیم
وحید ۵:۴۸ یه انفجار خیلی بزرگ بندرعباس صداش ب شدت زیاد بود
صدا اومد  موجش خونه رو لرزوند همین الان بندرعباس خونمون نزدیک جاییه که موشک میزنن
سلام بندر امام از ساعت چند همینطور دارن میزنن
🔄
صدای یک انفجار دیگر ساعت ۵:۵۱
05:51 یکی دیگم زد
صدایی بلند تر همین الان
دوباره انفجارر
دوباره زدن ۲ تا انفجاز بندرعباس همین لحظه ۵:۵۱
دوبارهههههه
سلام همین الان دوباره صدا انفجار اومد بندر
بندرعباس دوباره صدای انفجار اومد ساعت 5:51
ساعت 5:51 یک انفجار دیگه بندرعباس
سلام ۵:۵۰ بندرعباس دوباره صدا انفجار اومد خیلی شدید بود
این دفعه چیزی تکون نمیخوره فقط صداش بلندههه
واییی دوباره زدنن
دومین انفجار شدید تر
نزدیکی پایگاه هوایی
سلام
صدای وحشتناک انفجار از سمت دریا، همبن الان بندرعباس 05:52
سلام میشه خواهش کنم بذارید تو کانال؟
الان دارن حمله میکنن
بعد ما باید یه ساعت دیگه آزمون نهایی بدیم اگه خدایی نکرده کسی خون از دماغش بیاد کی پاسخگوعه؟ جدی باید یه فکری به حال ما دانش آموزا بکنن
همین الان ۵:۵۳ بازم یه انفجار شدید بندرعباس
خونمون داره میلرزه
😳
بندرعباس
بندرعباس پشت سر هم داره میزنه بعد بچه های یازدهم یه ساعت دیگه باید مدرسه باشن آزمون دارن
نهایت نامردیه در حق بچه های جنوب شب تا صبح چشم رو هم نذاشتن از صدای انفجار
بندرعباس احتمالا مناطق نظامی داخل شهر (نیروی دریایی سمت صداوسیما) رو داره میزنه که صدا اینهمه واضح و شدیده
چون انفجارهای قبلی رو ما با اینکه تقریبا وسط شهر ساکن هستیم متوجه نشده بودیم.
🔄
صدای یک انفجار دیگر شدید ساعت ۵:۵۵
بندرعباس باز زدن ۵:۵۵
۳ انفجار دوباره ۵:۵۵ بندرعباس
05:55 از بقیشون شدیدتر بود
آقا دوباره انفجار
وحید بندرعباس همچنان داره میزنه
صدای سوم انفجار در بندر عباس 5:55
۵:۵۵ دوباره صدای انفجار
5و55 دوباره زدن بندرعباس
بازم زدن هر بار شدیدترر
بندرعباس انفجار ۵:۵۵ درگیری از سمت ساحله
۵:۵۵ سلام برای بار سوم صدای انفجار بندرعباس اومد خیلی شدیده
آقا وحید سومی هم خیلی شدید بود
۵:۵۵ یکی دیگه زد خیلی بد بود
دوبارهههه همونقدر صدای بلندد و لرزیدن شیشه ها
برای بار سوم
این بلند تر از دوتای قبلی
۵:۵۵ انفجار سوم بندر عباس
۵:۵۵ صدای انفجار ب شدت بلند و مهیبه خونه رو کامل می‌لرزونه
بندرعباس ساعت ۵:۵۵ سومین تک انفجار قوی
وحید جان قشم هم صدای انفجار حس میشه خیلی شدید نمی‌دونم کجا اینجا یا بندر
بندرعباس صدای انفجار سوم
خیلی شدید بود
هر بار شدتش بیشتر میشه
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 405K · <a href="https://t.me/VahidOnline/76992" target="_blank">📅 05:49 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76988">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/t8ruLyH1chSSmpcXhb1ii6-KNkOSNN3dZacqwpSkQQoHg918nfor_omqZlk_iOortRGgoeyHcp6lFAmiv7Kkd4fuqejXd4Ss0ZH6NEocJdrXIW6vR3m_lLpbP68e1wP8SL0yBb4YwsGuRis1v2I1sSHIv4sHgk-W7zIl2a9FdprWM0kOpIMOUtVgYORUs2EzEO96HBBnI9LfaqKofgTHTxX4sR5HAkdHuldIQ9Ky7vQkI6wZOll7DmfQFN1WkaQLLFnyCgIoClVQdqSArpIcN8Ju7RGKlHCImcU7RfASYx51vf3VEVIyDjh4A72YNyxZbAFCZLy8_g9UuglkirrGHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JMqnA-EXQM6FZxlDp17i4DlwwN0qS0AZB3vLFuBI1cgHn3XlRL_OcSSejP6kvwFCViD2gVA9cfsmvUBmAQIcETcY-nKHOlFD2W-IakdgS6q6ZB8ZOPZBWp00gq2vQBknh24eEiAegDiIt11j3I4LiRCFXqxweTQb2-gRlFwwHII_GBTSH2cx2VHVctfav6XxhGsfj-kgAPgqtEdlaqFcqusCEnWpuND6P1JQWWnp_SZuIknOTY8IHZT0BOG5JQKClH43er6EHJyX-Ak5fIz_j_t4jlogZta-00lKIzuBuSpdkKsmCJZkm0d9b9hjDHBy5uGP7u6IA3et7qnyO5zivQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/79d39aa187.mp4?token=KPx_kteC6qqN-ah7yLO2RlfU8zo6fgGCdCSrQJUg6SJXltcHRBpRopLh9WA9qgSsRgvR8RcFuN8X6PjWBIVdVHh6Xkor3-T_AFYHeMR10HK8HtZBM9Egvg8yCXzmiOTPUuFfMu_I86Vd2P-KCSL9cUJnL9y8ePqLisvkv0g-wgdQsFa8R-dPri8A4_r682ojt0O3PR0mghR1-ko1C-lQpD8CpHFsMnrwW2_vxOmL8V5oig_MTy9aDWDKTfXxvNoGKV8H1bryWum0I1Iqefl3HMit1yx__WiJ3sIb5KAiSuNMhR6SX4MP3c67JAPCeR6BtPm0_jFfqqQ5l-AD1QSs7g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/79d39aa187.mp4?token=KPx_kteC6qqN-ah7yLO2RlfU8zo6fgGCdCSrQJUg6SJXltcHRBpRopLh9WA9qgSsRgvR8RcFuN8X6PjWBIVdVHh6Xkor3-T_AFYHeMR10HK8HtZBM9Egvg8yCXzmiOTPUuFfMu_I86Vd2P-KCSL9cUJnL9y8ePqLisvkv0g-wgdQsFa8R-dPri8A4_r682ojt0O3PR0mghR1-ko1C-lQpD8CpHFsMnrwW2_vxOmL8V5oig_MTy9aDWDKTfXxvNoGKV8H1bryWum0I1Iqefl3HMit1yx__WiJ3sIb5KAiSuNMhR6SX4MP3c67JAPCeR6BtPm0_jFfqqQ5l-AD1QSs7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی درباره شلیک موشک از بوشهر
Vahid
سلام ساعت٥:٢١ دقيقه صبح از شهرستان جم موشك بلند شد
همین الان جم چهارتا موشک بلند کرد
سلام وحید
شلیک موشک از جم-بوشهر ساعت 5:21
سلام ساعت ۵:۲۰ از جم صدای پرتاب موشک اومد
همین الان جم چهار تا موشک پرتاب شد
ساعت ۵:۲۰ بامداد چهار موشک‌از شهرستان جم بلند شد
وحید جان سلام . همین الان از جم ۴ تا موشک زدن
پیام دریافتی:
direct impact in bahrain, smoke visible from far away
[اصابت مستقیم در بحرین؛ دود از فاصله‌ای دور قابل مشاهده است.]
🔄
وزارت کشور بحرین با انتشار هشدار فوری در اکس اعلام کرد که آژیرهای خطر در این کشور، صبح دوشنبه، به صدا درآمده‌اند. این نهاد امنیتی با صدور این بیانیه، از تمامی مردم و ساکنان این کشور خواست تا ضمن حفظ آرامش کامل، به سرعت به نزدیک‌ترین مکان امن و پناهگاه‌ها بروند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/76988" target="_blank">📅 05:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76987">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TJ8IMjMRL7mPTyl0UD_eewEBxNtCv7T0pTyKQRj01mCU4NEIPgWNRRXw1fUdODVMlFR-zba1u3j5vIcyLW7KZWpCVSy4NPRfqOaHhNmgHCpHT15Plnsy5WPjDHBfBZiitDJhFHk6QptMs5_qfafeWBkIDTwigGqix1HOd6YR-EqDiVZzjCInrp7Qw2fAiTVrGUsCw68XqJlAb4hMChKhcqus0UcNQ_KCnGrmtIbmMgPKzP5TOm17ZuMqFSgh1xWb6WYXOQbA2O2TvkfMea2VVamViBOfRLeXSJKDL21DgZO0mcytKSdb9s7HY6g2mDwhca59viaiWv4kE3UGy1QNrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ در
تروث سوشال
عکسی از لیندزی گراهام منتشر کرده است با کلاه
Make Iran Great Again
سناتوری گراهام در این تصویر کلاهی بر سر دارد که روی آن نوشته شده است «ایران را دوباره با عظمت کن» و عکسی بزرگ از صفحه دونالد ترامپ در دانشنامه ویکی‌پدیا را بدست گرفته است.
دونالد ترامپ در این پیام غمگینی عمیق خود را از درگذشت سناتور لیندزی گراهام ابراز کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/76987" target="_blank">📅 05:09 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76985">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EoCt_s7lQCHfAKPov4RsbOsBN-GUPdtusIDbtCWUWysfGiCaKVNkeaEHf5Ag69Uy3_LnFNabDgYqPn0yUYB0UV_ypT5dsRF66prfH4vJtidlD0g8uITxqNUkPOe_4iLSYRAF0Bw03m42nGWA46b8gfN9k12RUGOFWmzx8386bYDOauCn9ur3hVXVgKIWz72iSUM0qVQM-5PCNmc54CTmFF5Lpt2ZAoN4icgYiLN_NQ6dnOPZ0I_i-SbgtjGMLhJW8PuEjUAbdkS9WJ04_OTjGemjdSj7RDg4iIHJSN8C2Fwyf24C_o2P9iY66ItNQiBKQRJEIobC7yPOOF7ecIS13Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FQAO9PaGFfbgLP3UMdQnjxq7OdtldcBK75h088UuLSpQm84IN_4QKQc2Xubgqis81Tu1TZloz8MENd6rWzM5jCdGzl7k1ifuO5FYslJTzSwA2j6U621KBL8QT8geumzeGiDHiWAiF53Am8lApDOIwxC2j-c9K0kpQd0NaNGLuFBESh-N-MU8prLdiyM7oSfw_2diKPo9vBrv9JRbu4levEUYwHTp3vGgUjf1sXC6X6iW6uFhJzknkQ7eluF4uAkNsovrFy2-BGbSJUj8GYR4mSJ89eE0izvUN5vqSla1W5sficcWQSMMzYVfCjxw47i83V3MACYpogANl8eLC5N_KQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیام‌های دریافتی:
سلام وحید جان دوباره ساعت۴:۲۸ دوتا موشک از خمین زدن
شلیک دو موشک از خمین
درود ساعت 29 4  الیگودرز دو شلیک موشک
خمین الان دوتا موشک
وحید از سمت خمین و الیگودرز دوتا شلیک کردن ۴:۳۰
همین الان صدای انفجارزیادامد
من حوالی شهراراکم سمت خمین بود
خمین ساعت ۴و۲۷ دقیقه موشک پرتاب شد
+
از زنجان و ازنا هم پیام‌هایی دریافت کردم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/76985" target="_blank">📅 04:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76980">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UbxrM45_GahLOTHC0hUoCFxa_iyVxQg0cdLNE9dnuWwu4fRae0IolXHAl5HByDpuSTDRNvJf6JgBy__0pKGWXWyt05m8zZU7YE7KWNflJh5IXazmLdOMe6Ii8t8GzCKBvpEoBZ7oKS42Md-pmuQnINOb4SNIk_imutvgeE5CE46CfZh0Ih3lWPW7BZJ-UBXDfdK_89YRxAmhk0CtCD2mcttuySD4fp3H7C14XxMlW9-lbmEnZdwjshlscPJMH1Rd3TkSjtkCFOEXc1WrXvkDR3GHT-WM0hmla2s7YKIStEQulxCcm8klsT6hduVrIfuGm-5yyaKpmagjn3PTufDulg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ctvOosx9obdz3qu001-BOdbjS4Pgvy3H0_bDlONWGPrFVpQLSPZo92nzt54dtjjWzQMx1CtoVD64Osh-XxiFXfDgxqabTHCR_70_ybaOk2TwpoXR0rznfsUkahMiMYnHT8KKEhOsqwC_m8Npsh6jDIpDdCFLd4oCS4PPZJd7_k6TpbQCZAxsg9ayNIaMR3Q641rf8XRufjz03q3BdKl27f46EuaVwWeJiAQlEkVg0hd9mGdSFW-rYe8MVN-fxhXrUf9nZIlJxjGZtn7yLY7Q-tkQTX_1KkDyMSHs-BZKOsA4QVzeaEs2Zv3qZ1w3qcJtzu50pSG41PyOwEvU1W1aWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Nzcuw0FjA5H_vMhI5OpHMgNAvCzKQuxWnKA6DIlsN4rNxxqlGmfAzjWlcBrnBH-pZzQz0BD3Ig6NtMo8GKPL2ZQb1A1v5opCA-59p5ykfypJqSEtry8Ytb5EJ2cA9_AlFebl7GX2vq4yMWfpfk5bLoozVbmEGHCjm3lP6jc41AsMZWMbxezEl2s0jj11c6A6LD_mSYPmN96Zivyw3GAoNG8UwK96YSCLRqzDr8d5HW-Si5Sd24HzxXi-Rigie0bzjANzS4RNfiAigUGIdtI3N2Ybn9IeMS5_SL_TWHphkU9o_i0UV_ZLwHl3F59jGzbuxdE8lqg7VRjsdjnbeMPYXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/892957aa92.mp4?token=GMKd2L_LXHiuUTjmGfZlaF_FC6kjIDrsrGoaQTD1bfKtBNekinn93XIGbEydpUFm8BSRs-1hftG_5r-Vw049SVVWqbCmJY8Rj1qC4hNYRJY8vFrD9cV4VzPYYBXOQwQCVHHmJMm32iLrWcK8xllKl4DIeUTThXxSbgFezCD4f3cQW2zIXUb65xph-IYh1cTi2EY6CG1qADZpxrijrgM1jxulKoJ-hSL6U0fxeIawqmsAhmDaif3rhbBIdwJVR7bov6w-tFcIiFBfoEJinRC81XEV6k0XDGUYeMiDPuFAMOJZZAggmjOTJ6T2hO5oCN_1XLK16RquH6yaqWCUwyVFog" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/892957aa92.mp4?token=GMKd2L_LXHiuUTjmGfZlaF_FC6kjIDrsrGoaQTD1bfKtBNekinn93XIGbEydpUFm8BSRs-1hftG_5r-Vw049SVVWqbCmJY8Rj1qC4hNYRJY8vFrD9cV4VzPYYBXOQwQCVHHmJMm32iLrWcK8xllKl4DIeUTThXxSbgFezCD4f3cQW2zIXUb65xph-IYh1cTi2EY6CG1qADZpxrijrgM1jxulKoJ-hSL6U0fxeIawqmsAhmDaif3rhbBIdwJVR7bov6w-tFcIiFBfoEJinRC81XEV6k0XDGUYeMiDPuFAMOJZZAggmjOTJ6T2hO5oCN_1XLK16RquH6yaqWCUwyVFog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر دریافتی با شرح: 'انفجار و آتش‌سوزی [سمت] فرودگاه
#امیدیه
در خوزستان
دوشنبه ۲۲ تیر حدود ساعت ۳ بامداد'
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/76980" target="_blank">📅 03:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76979">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">پیام‌های دریافتی:
‌
اهواز صدای خیلی شدید اومد
همین الان انفجار شدید اهواز
درود وحید جان ، همین الان اهواز صدای انفجار شدید اومد ساعت 1:31
اهواز ساعت 1:31 بامداد صدای انفجار
اهواز ساعت ۱:۳۰ صدای ۳ تا انفجار
هواز همین الان زدن ۰۱:۳۲
سه تا موج انفجار پشت‌سر هم ، شدید تر از دوران جنگ  بود ، من مرکز شهر ساکن هستم
سلام دارن اهواز و میزنن ساعت 1/28دقیقه
سلام وحید ساعت ۱:۳۰ سمت فرودگاه و گلف رو زدن خیلی وحشتناک بود
😭
😭
😭
سلام  آقا وحید. اهواز ساعت ۱:۳۰ دو تا انفجار پشت هم
وحید همین الان ساعت ۱:۳۰ اهواز رو زدن، کیانپارس خیلی شدید حس کردیم
اهواز دو تا محکم زد
ساعت ۱:۲۹
اهواز و‌همین الان زدن صدای سه انفجار اومد نزدیک سیصددستگاه/سپیدار
اهواز صدای انفجار
سلام الان ساعت ۱:۳۲اهواز سه صدا انفجار اومد
اهواز همین الان دو صدا همراه با لرزش ساعت ۱:۳۰
وحید جان همین الان ساعت  ۱:۳۰ اهواز صدای انفجار اومد.
وحید جان اهواز صدای انفجار شدید
وحید انفجار به شدت قوی تو اهواز خونه لرزید ۱:۳۰
سلام وحید جان ساعت ۱:۳۰ اهواز صدا دوتا انفجار اومد منطقه کیانپارس یک مقدار ضعیف بود صداش
سلام وحید
ساعت ۰۱:۳۱ اهواز صدای انفجار اومد
فکر کردم خیالاتی شدم، اومدم بیرون دیدم همسایه ها هم ریختن بیرون
وحید جان
اهواز ساعت 01:31  دو تا یا سه تا صدای شدید اومد
اهواز لرزش شدید و صدای انفجار
دقیقا نمیدونم کجا، اما زاویه‌‌ی صدا از سمت چهارشیر بود به نظرم فکر کنم سپاه چهارشیر
صدا انفجار ماهشهر
ماهشهر همین الان
ما اهوازیم کوی باهنر
صدای انفجار شدید
بندر ماهشهر صدا اومد.
اهواز ما سمت کیان آبادیم و واقعا صدای انفجار زیاد بود
🔄
همچنان خوزستان:
انفجار شدید ماهشهر"همین الان"
دوباره الان ماهشهرو زد،1:51
شش انفجار 1/52 قشم-طولا شنیده شد
سلام ماهشهر هم صدای انفجار اومد
دوتا تا این لحظه 1:52
سلام وحید جان اطراف بهبهان تا الان صدای ۶ انفجار اومد
همینطور دارن میزنن
سلام قشم همین الان صدای چند انفجار
صدای از دور از سمت غرب جزیره
همین الان صدای انفجار زیاد بالای ۵ تا داخل قشم شنیده شد
بهبهان ساعت 1:52 بامداد صدای چهار انفجار شدید
سلام وحید ما نزدیک فرودگاه ساکنیم حدود ساعت حدود یک و نیم دوتاصدای انفجار اومد همه همسایه ها ریختن بیرون معلوم نیست کجارو زدن
قشم ساعت ۱:۵۰ زدن ، چندین انفجار شدید
بهبهان‌رو الان چند بار زدن
روشمهر پایگاه موشکی ساجد
بهبهان خوزستان/ ۱:۳۲ ... صدای ۲ انفجار.
مجددا ۱/۴۵ تا ۱/۵۰ بهبهان خوزستان صدای ۴ انفجار
سلام وحید جان
امیدیه صدای بسیار خفیف انفجار
مشخصاً درون شهر مورد هدف قرار نگرفته
احتمالا دقایقی بوده
همین الان خوزستان بهبهان ۴ بار پشت سر هم زدن
نمی‌دونم کجا بود
🔄
ساعت ۲:۱۵ دقیقه دزفول رو زدن
در و پنجره ها لرزید
دزفول خوزستان
همین الان زدن
سلام وحید
دزفول رو دارن میزنن
۰۲:۱۵ دقیقه
سلام دزفول رو دوبار پشت هم زدن
🔄
موج بعدی پیام‌ها از دزفول درباره شنیدن شدن صدای انفجار در ساعت ۲:۱۹ و ۲:۲۵
🔄
امیدیه ساعت ۳:۰۲
درود امیدیه خوزستان همین الان صدای چندتا انفجار پست سر هم اومد
امیدیه خوزستان چند دقیقه پیش ۴ تا پشت هم زدن کل شهر لرزید
ساعت 3:02 دقیقه
صدای بشدت وحشتناک توی امیدیه اونقد که شیشه ها لرزید
پازنون هم زدن
صدای چند انفجار  در امیدیه شنیده شد
حدود ساعت 3 بامداد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 398K · <a href="https://t.me/VahidOnline/76979" target="_blank">📅 01:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76977">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/APyBhc3q1CZu7FcSQFoIIDeM2Xtt-uiWHjMXWen7fx2IrPlwIA2KzZbFInQE98pQmXpjdYHWJPx7Rx-3gP_us25wvEpYnO-2KnoBbxiDt5C6c_Ab2RKQW5cC_xWirnbyqikyvJUp4IxpZuT6yFwz_UTv0LO6w59_PfTZekYVrvWL8WjB7ZpOcN8XBBIBpywjGwXulHrb_LZHfyr_7-36c3LEb7NfsaYdc9XOU-Qq7bA-Tc92Gdb-_ZriYqxiR0FYky6xaoetRecVEtOFKvBZr2KeSvNwAugzGknqkGMtUChf1AHZRNuLWeEqbVkizgwAX7VSES0XIfmieKCCV_uiYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cfc3526ac6.mp4?token=IEPcHAjjVxGWOuV6rJly2_3wKKYDzc3OtjlMBb9ef4jU3OYn69sE2NTPLtCTUu0ugtzIkQsv2cZ-8x1_I0dv81t9_C_DV2tMcsGiL3cQrir1cqzw0hvDuuGNCj0V7ETzuki7eLmV-Zo29t7JdzdnHWI9BVLZtuGdfUY4qF4lrGteiSsjYnnkaIfbS4THF2XjfdOCQj0gh_O5oTiMiNOs8RbYlsOujYL3QB91GzS5j-uv2AR67SIRRTH2GoMSEzrFVusamIXH9nT_57X-yId8VXtjvrE2a2IV4uWaKIo9vpeSdeiQqoNklEwn7bIztWVSwjst1w-xac1kgCg1dvItTg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cfc3526ac6.mp4?token=IEPcHAjjVxGWOuV6rJly2_3wKKYDzc3OtjlMBb9ef4jU3OYn69sE2NTPLtCTUu0ugtzIkQsv2cZ-8x1_I0dv81t9_C_DV2tMcsGiL3cQrir1cqzw0hvDuuGNCj0V7ETzuki7eLmV-Zo29t7JdzdnHWI9BVLZtuGdfUY4qF4lrGteiSsjYnnkaIfbS4THF2XjfdOCQj0gh_O5oTiMiNOs8RbYlsOujYL3QB91GzS5j-uv2AR67SIRRTH2GoMSEzrFVusamIXH9nT_57X-yId8VXtjvrE2a2IV4uWaKIo9vpeSdeiQqoNklEwn7bIztWVSwjst1w-xac1kgCg1dvItTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر دریافتی: 'بندرعباس، ساعت ۰۰:۴۳ بامداد دوشنبه ۲۲ تیر'
Vahid
صدا و سیما:
بر اساس گزارش‌های اولیه، حمله امشب به دکل مخابراتی اطراف روستای طاهرویی سیریک بوده، همون جایی که در حملات قبلی هم مورد اصابت قرار گرفته بود
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/76977" target="_blank">📅 01:19 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76976">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T3Lg50Qtpy3Rx45yTgSzOO1LOHw8EdGIQcKI5tRcbDUiN_KKuUfyTorFZlgu639UPa7U_CCOgP4wt3ZRYvUvVn95Lyz67TILI20R-dapd5yp_NBPOK4EY-gE7-Mpt2Qe3Zi_3RjKXW3oOebmxJfUqeF9cC72K4Z4ImXqvks4zFfym5OGA4MiLZrpkJ9sKO-3QMx_cqbphtWhhs6WscXNbtN2RZdrmafyNHlTbuQ3yNtAJZuUr4I2uU3oeeFzza_PVRn-6ZMPZo7QlZ3qilpyg5Xmwh2UROgFdZNCjxQNq4HXuyhVksMmwQC6Syk7gfJIa9SRhvLwGvOfBuiIaoBmow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست اکانت سنتکام:
ساعت ۵ عصر امروز به وقت شرق آمریکا، نیروهای فرماندهی مرکزی ایالات متحده حملات بیشتری را علیه ایران آغاز کردند تا به تضعیف توانایی این کشور برای حمله به دریانوردان غیرنظامی و کشتی‌های تجاری که آزادانه از تنگه هرمز عبور می‌کنند، ادامه دهند.
فرمانده کل قوا دستور این حملات را برای پاسخگو کردن نیروهای ایرانی صادر کرده است.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/76976" target="_blank">📅 00:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76975">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">پیام‌های دریافتی:
00:38 صدای چندین انفجار در بندرعباس
همین الان انفجار پیاپی بندرعباس ۰۰:۳۹
بندرعباس ساعت ۱۲:۳۸ صدای انفجار چنتا اومد
باز هم داره صدا میاد
بندرعباس همین الان چهار پنج صدای انفجار پشت سر هم اومد
😭
صدای سه انفجار بندرعباس ساعت ٣٨ دقیقه بامداد
00:39 بندرعباس سه چهارتا صدا اومد
قشم الان صدای انفجار اومد
ولی از خود جزیره نبود، بندرعباس سیریک یا روی دریا بود
سلام وحید از بند عباس خبر میدم صدا ۳ تا انفجار شنیدم شدید بود شیشه ها لرزید
🔄
جنگنده الان بالای شهر جاسک
۴ تا صدا انفجار اومد
دوباره جاسک داره میزنه
همین الان
سه انفجار درجاسک
همین الان دوتا انفجار جاسک
صدای جنگنده هم خیلی زیاده
صدا و سیما:
🔺
دقایقی پیش؛ شنیده شدن صدای چندین انفجار در اطراف روسنای طاهرویی سیریک
🔺
صدای سه انفجار در جاسک شنیده شد
🔺
صدای چند انفجار در قشم شنیده شد
🔄
خنداب در استان مرکزی:
سلام وحید جان. همین الان سمت ساعت  یک بامداد صدای جنگنده شنیده شد.
خنداب.
همین الان صدای انفجاررر
سلام ۳ دیقه پیش خنداب رو زدن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 395K · <a href="https://t.me/VahidOnline/76975" target="_blank">📅 00:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76974">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_Rqp-2J8bglIfBxH0l08D33vmz1_twz0TUWQYOM8qUgqHaHetxeBwxqiHYdWrheUb7Rs2M5gRiwV-FWOsOpPa1aYb9G6UDyuuzbx-odNniGMqKeH4lDs5i5ZUfLH8uhcOFmiuKLpY8_HwkABZE-sLa_uaCnou_xlUoth1gwKWp494PSvut_RfAV0aiX-cNFmppznk7TE94Fx912IMHtnwxCOeiOyfMPpJF4DG27Et4IK8CxHuOiV6nF3BY9BgshtbsJ6K9IZJBWK6KtJ53AGiXFZ4xLTpVYSKLFqrkzCVZGRHUw78w3L2P5hMVLgq5Tb6BqGlTLuMwLaUMZmiAWjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرماندهی مرکزی آمریکا (سنتکام) شامگاه یکشنبه ۲۱ تیر، ادعای رسانه‌های وابسته به جمهوری اسلامی درباره کشته شدن نظامیان آمریکایی در کویت را رد کرد.
سنتکام
نوشت
:
🚫
ادعا: تبلیغات ایران امروز مدعی شد که سه نظامی آمریکایی در کویت بر اثر حملات ایران کشته شده‌اند. نادرست.
✅
حقیقت: هیچ گزارشی از کشته یا زخمی شدن نیروهای نظامی آمریکا در منطقه وجود ندارد. وضعیت همه نیروها مشخص و تأیید شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 409K · <a href="https://t.me/VahidOnline/76974" target="_blank">📅 00:19 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76973">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">خبرگزاری مهر:
گزارش‌هایی از شنیده شدن انفجار در جزیره بوموسی؛ وضعیت جزیره لارک عادی است
ساعتی پیش منابع محلی از اصابت ۲ پرتابه به جزیره بوموسی در جنوبی‌ترین نقطه کشور خبر دادند.
در حوالی ساعت ۲۰:۳۰ امشب، صدای چند انفجار دیگر در بندرعباس شنیده شده است که به نظر می‌رسد مربوط به شلیک یا اصابت‌هایی در محدوده دریایی بوده است.
پیگیری خبرنگار مهر از جزیره لارک نیز حاکی از آن است که وضعیت در این جزیره واقع در تنگه هرمز کاملاً امن بوده و هیچگونه گزارشی از حمله یا حادثه‌ای در این منطقه وجود ندارد.
اخبار تکمیلی متعاقباً ارسال خواهد شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 425K · <a href="https://t.me/VahidOnline/76973" target="_blank">📅 21:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76970">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFactNameh | فکت‌نامه</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hbWyEYAy56VkHjuGLRkAqoKmM9ZOPNDPMFEvF8W4Y4lHSUx5YRBDnaxHRZsjFD2WyBNQN3Y7HhzYAC7qZjWFQPlwXET9LvaE-h-_VXdvBBbXqLpEC7RW8un0CK5c9Q8FJ_RHYrT4PrTTqw7rUksVOGIPlhIyjPODjLbO0no1y4iTpOHyEEjuBpFmnPjJ9aPWnYlfa-9Ja4UcWMWhzkWch6Pu6W4M1qqdX8oymEGDR9C-exgoAdwujnmd8r8LcUI9yMreSCB42n7rSUDQh_fpz1IQjSQI84jvhcFmeq2YDG3tiZawXE7Pbjmbmc4pseA5G8b1a2yMp-rr_pMsuQ_qUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NsbTu2TUI5ZYJR6I3pMF7ad3vcuUoc0QcjRhJhsgx9sGeU0mBor2qnt3xwMnENq0gKwIKZfoFRVKQ8jte7FrytE2exvPT5J6dZDYx1lKOulqtpBjDP0qi58Xzp_p-gncbcTJ_8M8fpQfcKpJetOIPuk6apf9-9YzrwCHf28gRreT2boHP2r5MWTkv5QaV2fsdJgDuTqBc2AhVtYBKFG-DPZfsqboMbfLreLXlxk3WP22-EmTgc9SgdzhfC85l5KkJM5SZ_8OrNDaDxlxnEIVRi69eOPmDBc2wZxTusPG1c9ptcUYyP7YVuD4CaIfNuWdqQs2AYevW9ILRYPs7gyc2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/83e7b96a5e.mp4?token=XT7OMIDyOBKxqmwRA7Y0lPjkWrZzM8paapnWvLlZAIWhoY-u78OOYltFWCbhuyFM8gcA5ObbYfkjam9iBqVZBOUUzFZkMjzXTS6O62h4GlP4Q6L85tMplUp8B-5Qg4ceDOIMCnvYrUOea7-suG05fpK06CWQCgnzMrtcukVEfepezqXmRmMubPrXfN9MKrHsPj1blJ4LrV0Kq-tlgWU3vjx2-KCMrjzKNFnATdbovMlLiES6Sr6WS5ti9joTIaIdFtx05dAC2hPXj2Yee2CTZ1qM131d2BhDjZfp-2clkJmYOPhzGxjoAfgjmAG3v3vvKUoM3tzrw5esElXAZRo_-A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/83e7b96a5e.mp4?token=XT7OMIDyOBKxqmwRA7Y0lPjkWrZzM8paapnWvLlZAIWhoY-u78OOYltFWCbhuyFM8gcA5ObbYfkjam9iBqVZBOUUzFZkMjzXTS6O62h4GlP4Q6L85tMplUp8B-5Qg4ceDOIMCnvYrUOea7-suG05fpK06CWQCgnzMrtcukVEfepezqXmRmMubPrXfN9MKrHsPj1blJ4LrV0Kq-tlgWU3vjx2-KCMrjzKNFnATdbovMlLiES6Sr6WS5ti9joTIaIdFtx05dAC2hPXj2Yee2CTZ1qM131d2BhDjZfp-2clkJmYOPhzGxjoAfgjmAG3v3vvKUoM3tzrw5esElXAZRo_-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ادعای شاخ‌دار دکتر کلانتر معتمدی درباره رابطه واکسن فایزر با نازایی و عقیم شدن زنان
🔹
محمدرضا کلانتر معتمدی، دبیر فرهنگستان علوم پزشکی، در یک برنامه تلویزیونی گفته است: «بعد از ۸ ماه مشخص شد واکسن فایزر حاوی همان ماده‌ای است که در واکسن ابولا بود و دختران را عقیم می‌کرد.»
🔹
این ادعا صرفاً تئوری توطئه بی‌پایه و اساسی است که از سوی پزشکی مطرح شده که در جریان تحولات علمی روز قرار ندارد.
🔹
واکسن کرونای فایزر چه در ساختار و چه در عملکرد، شباهتی به واکسن‌های تأییدشده ابولا ندارد.
🔹
سازمان بهداشت جهانی تأکید می‌کند: «هیچ شواهدی مبنی بر تداخل واکسن‌های کووید-۱۹ با باروری وجود ندارد و هیچ مدرک بیولوژیکی وجود ندارد که نشان دهد آنتی‌بادی‌های ناشی از واکسن یا ترکیبات آن آسیبی به اندام‌های تولیدمثل وارد کنند.»
🔹
محمدرضا کلانتر معتمدی، پزشک و جراح است و به عنوان عضو، دبیر یا حتی رئیس گروه‌های علمی فعالیت می‌کند، اما اغلب اظهارنظرهای او در فضای عمومی جنبه اجتماعی و سیاسی دارد.
🔹
ما در منابع عمومی چند مقاله از او پیدا کردیم که عنوان موضوعات آن «اقتصاد مقاومتی در نظام سلامت»، «فقر و هزینه‌های جراحی»، «تجربه‌های دفاع مقدس» و «مولفه‌های فرهنگ ایثار و شهادت در جامعه سلامت کشور» است.
🔹
او یکی از امضاکنندگان نامه منتسب به «۲۵۰۰ پزشک» است که چند روز بعد از ممنوعیت واردات واکسن از سوی خامنه‌ای اعلام شد.
🔹
بررسی‌های فکت‌نامه
همان زمان توضیح داد که هم محتوای نامه بی‌پایه و اساس و تئوری توطئه است و هم نامه‌ای که به «۲۵۰۰ پزشک» منتسب شده کمتر از ۱۸۰ امضا با نام‌های تکراری و مخدوش دارد.
🔹
با این توضیحات فکت‌نامه به این ادعا نشان
«شاخ‌دار»
می‌دهد.
👈
در فکت‌نامه بخوانید
🌐
@Factnameh</div>
<div class="tg-footer">👁️ 425K · <a href="https://t.me/VahidOnline/76970" target="_blank">📅 20:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76969">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8bbd214211.mp4?token=s97Nw_brMsWt5TLnO3suLEOXXbrijrgtA3WanLM_k4lt3tnxDKEJRUC7PJeSEwdJqJxmU5am6u8sDXNnW2zcEs0RKhZCKCochi3Hth7Xr2amVdFc9zK_04EY7r_cjYnKZRJ_AOA_ZyEDN7OmcucD3ZofT6aV0_rGNhQjFL5fqkWtDNOJ2T_hdJQ1M3A96MxyBKIfDzaoXfDPPxYisiwj6TSneAX7jMeZ86Rr5BWS3JfRQFNJd5H5JdwiH21GqXAINjQZAGeyjXtb-wAu58HuunvL-2J8U65RjjBlrCABNCXhDUqPgpU0MAFzOTVWvfYVX5zd5_tLyuppvSnCCjCxKw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8bbd214211.mp4?token=s97Nw_brMsWt5TLnO3suLEOXXbrijrgtA3WanLM_k4lt3tnxDKEJRUC7PJeSEwdJqJxmU5am6u8sDXNnW2zcEs0RKhZCKCochi3Hth7Xr2amVdFc9zK_04EY7r_cjYnKZRJ_AOA_ZyEDN7OmcucD3ZofT6aV0_rGNhQjFL5fqkWtDNOJ2T_hdJQ1M3A96MxyBKIfDzaoXfDPPxYisiwj6TSneAX7jMeZ86Rr5BWS3JfRQFNJd5H5JdwiH21GqXAINjQZAGeyjXtb-wAu58HuunvL-2J8U65RjjBlrCABNCXhDUqPgpU0MAFzOTVWvfYVX5zd5_tLyuppvSnCCjCxKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی وزارت دفاع کویت شامگاه یک‌شنبه در بیانیه‌ای اعلام کرد که سه پاسگاه مرزی زمینی در شمال این کشور هدف یک حمله «خصمانه و جنایتکارانه» قرار گرفتند که در پی آن خساراتی به تاسیسات وارد شد.
وزارت دفاع کویت افزود همچنین یکی از سکوهای حفاری دریایی شرکت نفت کویت در آب‌های سرزمینی این کشور هدف یک پهپاد مهاجم قرار گرفت. این حمله خساراتی به بار آورد و یکی از کارکنان زخمی شد. این فرد در حال دریافت خدمات درمانی است.
ستاد کل ارتش کویت نیز تاکید کرد نیروهای مسلح این کشور همچنان در آمادگی کامل قرار دارند و همه تدابیر و اقدامات لازم را برای حفظ امنیت کشور و تمامیت ارضی آن اتخاذ کرده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 399K · <a href="https://t.me/VahidOnline/76969" target="_blank">📅 20:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76968">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjmwuQp1V__2EKyA-qN9KH6idyyk0hcUFi3dldS805vYyRhzxEXrgpKx_Mj9pK781xdz1eljKlUsbvhzh98cKyG093qBqR_NxCuxSYafLGZNdDG0aGKpMh90Wx137DKw4SinqPaNhzZ3PLXqm2okCOGgWNVUJtLPlE4SdTnPWKFi1Ou-D2ziMDw-3CWntfuR0GChPov1ow_p-FHYFZqBu5nLQ9JPMLxT8TXjZI7DzTlFmzr_pG-RjOBonzGCOmglG_V5K_mPWDBefpxrMcD3nHE5CgSXsn9gpn2_ZdhmkZWRIDY8SCa8LPXvfdSNe5iQirYrE2QNgaFYi7KNwe_Jjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام ارشد آمریکایی، یکشنبه‌شب ۲۱ تیرماه، به خبرنگار آکسیوس گفت ارتش ایالات متحده چند حمله را به سامانه‌های موشکی و پدافند هوایی ایران و همچنین قایق‌های تندرو سپاه پاسداران در چند مکان در اطراف تنگه هرمز انجام داده است.
حسین امیرتیموری، فرماندار قشم، تایید کرد یکشنبه شب حدود ۱۰ پرتابه به اهداف نظامی در این جزیره اصابت کرده است
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 385K · <a href="https://t.me/VahidOnline/76968" target="_blank">📅 20:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76967">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b1e454bd90.mp4?token=Be5VF_QBxBAkMbKbEye4PRAoZFApHwjo2dvpiX56LRhHhK6AhkoEWe1Ei9W3EZIl12v-_cjAtMKf-MATN8oJSdNtGTVl-ZxIhvOSfs2Rcf1uqCT3z4d4ci1276EGDeuOgT1e4855uTF2OBdM-bjAdhuGOzFXbQL1tFqZzkDLcPIyjtlDStFd9I4nvY_GsH5JrE26s9tIOU0vgOet9rurswFBuVzLItEO8wI_BgHPacmdUz5hbhzWYmQoMEixI3j4Md7Az_Br8-j9SGK0l5Id2oYoaghAqItQFlwZQORBTPqRniChpJyxukVjkokFMy6TnFjQjKhTdpWbvAjfPE0isQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b1e454bd90.mp4?token=Be5VF_QBxBAkMbKbEye4PRAoZFApHwjo2dvpiX56LRhHhK6AhkoEWe1Ei9W3EZIl12v-_cjAtMKf-MATN8oJSdNtGTVl-ZxIhvOSfs2Rcf1uqCT3z4d4ci1276EGDeuOgT1e4855uTF2OBdM-bjAdhuGOzFXbQL1tFqZzkDLcPIyjtlDStFd9I4nvY_GsH5JrE26s9tIOU0vgOet9rurswFBuVzLItEO8wI_BgHPacmdUz5hbhzWYmQoMEixI3j4Md7Az_Br8-j9SGK0l5Id2oYoaghAqItQFlwZQORBTPqRniChpJyxukVjkokFMy6TnFjQjKhTdpWbvAjfPE0isQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری فارس:
شنیده‌شدن صدای چند انفجار در بندرعباس و قشم
دقایقی پیش صدای چند انفجار از سمت شرق بندرعباس و محدودهٔ دریایی قشم شنیده شد.
همچنین اهالی منطقهٔ مسن در جنوب جزیرهٔ قشم نیز صدای چند انفجار را شنیده‌اند.
ماهیت انفجارها هنوز مشخص نیست و اخبار تکمیلی متعاقبا اعلام می‌شود.
پیش‌تر نیز برخی رسانه‌ها از وقوع انفجارهایی در کویت خبر داده بودند.
@
VahidOOnLine
🔄
ایرنا:
اصابت پرتابه در جزیزه قشم
🔹
فرماندار قشم از اصابت 10 تا 11 پرتابه دشمن از عصر امروز یکشنبه در جزیره قشم خبر داد.
🔹
حسین امیر تیموری در گفت و گو با ایرنا افزود: تمامی اهداف نظامی بوده است. خوشبختانه این حملات هیچ تلفاتی نداشته است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 391K · <a href="https://t.me/VahidOnline/76967" target="_blank">📅 19:31 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
