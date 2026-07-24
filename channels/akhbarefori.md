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
<img src="https://cdn4.telesco.pe/file/MbvM7cM1rmECSaBB0EowY7vpY4CuPhuFC-lezoGZxKtirFMQe8qLj1fxQjwHj2677fJjq-x7HTZLnCpm3lx_BK_JgSFkRI1Y_B2tDvhywha_m4wY_TSjZqnAqyOBo3qgehJ8y_M3-zb_8s0kuskBU5hB_lH-LMN3LfgJcMNOCZhNRzv-W49QmpWBt0JkATmI5_ni-s63h7VjT36ryyJqDv3dD8En_jrMXCk9VMCkpuhRwD8qkyeDdkEgpo5DSbfW1SYdgySygg5-UFh0Ovz6UBZmfUgAgkInzi_mCL7OCKXaCdQlg8K8TSCt0Bc_2eU51MsZh7ojeFzCQPI3R1cdXg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.35M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 15:28:59</div>
<hr>

<div class="tg-post" id="msg-674823">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
ثبت تصویر پرتاب استارشیپ از خاک مکزیک
🔹
پرتاب دوم استارشیپ، بزرگ‌ترین موشک شرکت اسپیس‌ایکس (۱۲۱ متری) متعلق به ایلان ماسک، از زاویه دید ناظران در خاک مکزیک به ثبت رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/674823" target="_blank">📅 15:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674822">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQE7WSNVu_gG189vF4M7Xz4YggmI7um1y-VrOluVjPC4EXc8R-BFBtz7X20ylCvRCDqHzUSqWxET43zGpQkXnlUNCkIKsXeMeEkoDzlXtz93msGSub_FV-25gFz8l8K4GNadew8tHDEjqZ3EixtscWavXXhkqJBimN_gO-IZ41gflijHnNXqy-VhHpreAxM6E_y7NGXbS7J8WkQtwDzZ6UV8u7ysVdiOHrye389fuS3vACm86BbWQexN-MexvHUfkXnfZYeBCK0xCVXjXC0zPubeDA52dsY5vB6M8W2oDmjhoZNShvaxBoGk4MzQQHKPOWQZ7ymGt48poghCYyjOUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سرگیجه آمریکا از دقت حملات ایران | ماجرای کمک روسیه به ایران در انهدام پایگاه‌های سیا چیست؟
🔹
به دنبال حملات پهپادی ایران به چند مرکز وابسته به سازمان سیا‌در منطقه، نهادهای اطلاعاتی ایالات متحده در حال بررسی این احتمال هستند که روسیه در این عملیات به تهران کمک کرده باشد؛ چه از طریق ارائه اطلاعات هدف‌گیری و چه با انتقال فناوری پیشرفته پهپادی.
جزئیات بیشتر را در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3232561</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/akhbarefori/674822" target="_blank">📅 15:18 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674821">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIPq4hS7Yj1hKWgZgBCU5HrzwOmekYUboc8mrgyNthF2Tt6K5jMegatb50YGmETa5vZ-WJnmQkoijtxra6gqGE-IbDLL7_UNM7Cx-4ZmxEkQMNXVG3Y1tDICwxnsvKd-iVkHcgEJ8qZQVbtRLAP70P7qO8khIcio5dw3-NNtfr5qn-COtu2dtOIGHL-BvrjD9XKjBKenjJzu5zJ_ysosSA8uuKKB3iqZYuQjb0efx-VXh4dMStSKYhO5igCJp0X6xfE7kcDWhCoRIn38KUrr8bL2VW-dxw1f9Atn6tNpCJ_yGJtEBEqqBOatDjytiglTU0qQgp9snCBnFCGPp5Dz3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ونگر: مسی بهترین بازیکن تاریخ فوتبال است
🔹
آرسن ونگر، مدیر توسعه فوتبال فیفا، لیونل مسی را بهترین بازیکن تاریخ فوتبال دانست و گفت این موضوع «یک حقیقت» است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/akhbarefori/674821" target="_blank">📅 15:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674820">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca7f6657a5.mp4?token=fEIqkbYcMb0g63DJ3AmQt6dtA3jUWhxDr6bBwRkE7AJelGxafWTfLdo9pCxUhNfZJvbHM7L8794GF1zsP6H190hZXCDBQ83jlIy39qfkGQFV-umx6Wb2jq96Rs_XhETLgQxgIlsT7nw8Ma7b3ofIFgvPjuVExSqmu-d0ewuDlXtwL20Jh-DHgRyV9ccVde56K89S31INEOTLcuaqipr5MK_7vC4GIbIuFuvSEJQZK2KIaHM8vmCSVxyRMf8pfh3VTBiUZxqkucCX7WnNL6XH_P_Ct-6ClzKlKp9qrvN6vQwztgM-p8XF0_c7RNB_ETt1DIcXQEmlwUq0c2Q6Z7qyFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca7f6657a5.mp4?token=fEIqkbYcMb0g63DJ3AmQt6dtA3jUWhxDr6bBwRkE7AJelGxafWTfLdo9pCxUhNfZJvbHM7L8794GF1zsP6H190hZXCDBQ83jlIy39qfkGQFV-umx6Wb2jq96Rs_XhETLgQxgIlsT7nw8Ma7b3ofIFgvPjuVExSqmu-d0ewuDlXtwL20Jh-DHgRyV9ccVde56K89S31INEOTLcuaqipr5MK_7vC4GIbIuFuvSEJQZK2KIaHM8vmCSVxyRMf8pfh3VTBiUZxqkucCX7WnNL6XH_P_Ct-6ClzKlKp9qrvN6vQwztgM-p8XF0_c7RNB_ETt1DIcXQEmlwUq0c2Q6Z7qyFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آخرین تصویر از ماکان نصیری و هم‌کلاسی‌هایش در دبستان شجره طیبه میناب
💔
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/674820" target="_blank">📅 15:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674819">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d007100491.mp4?token=O73s9ZhO5apm4pGFU6tGA84gb1zX_Q0DcanIxuScAB7q_YV8UP-aKp7230ITcfvGpgqKpukmAR8qygPUknAdQ7JiFHA84A0bfNBYHz14JNCsSZm5gsSfIj_sNxDPRM8x0Cph2QVkSEC80t6xhsMnjPdjs7ZEEqNnoeEb8HpIuGA8QLjWM7Cy-wnfsQigZNQIDzFX1Xqukg4czLtYOEjI0Jf3n9YvxUwwle2qbNLvLtgAl_iaewdKzouOglzGm6PTID13uzBqqj_Rm2GAdHDRd-hN5-gMvJmEiZMyssQPnNSYKACx3pXYbVOu6ybGPpDPUly0ARE9_0VOTFL2iGkOng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d007100491.mp4?token=O73s9ZhO5apm4pGFU6tGA84gb1zX_Q0DcanIxuScAB7q_YV8UP-aKp7230ITcfvGpgqKpukmAR8qygPUknAdQ7JiFHA84A0bfNBYHz14JNCsSZm5gsSfIj_sNxDPRM8x0Cph2QVkSEC80t6xhsMnjPdjs7ZEEqNnoeEb8HpIuGA8QLjWM7Cy-wnfsQigZNQIDzFX1Xqukg4czLtYOEjI0Jf3n9YvxUwwle2qbNLvLtgAl_iaewdKzouOglzGm6PTID13uzBqqj_Rm2GAdHDRd-hN5-gMvJmEiZMyssQPnNSYKACx3pXYbVOu6ybGPpDPUly0ARE9_0VOTFL2iGkOng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«تقدیر سهامداران از تایید وصول مطالبات ۵۲ میلیون دلاری شرکت نفت سپاهان»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/674819" target="_blank">📅 15:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674818">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
اطلاعیه شماره ۵۰: سه سوله نگهداری مهمات و تجهیزات در پایگاه آمریکایی العدیری و برج مراقبت ناوگان پنجم دریایی آمریکا به آتش کشیده شد  روابط عمومی سپاه پاسداران انقلاب اسلامی:
🔹
ملت شجاع و وفادار ایران اسلامی، عظمت شما رعب و وحشت را بر پایگاه دشمنان مستولی…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/674818" target="_blank">📅 14:53 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674817">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N3kBw7dhGlHnaCUn040T4rONG9S5zrMtnUzpJOVjYU6CVByxjNTGr63nT1bJYFqhfyNkoLU7ZCgY6S1deJIZQwHKFM-gtN1t3OKx5pq46XDdLexD8LrJidRVwXJBkadFFUR_f_yC1S2bRwB5lEFGgR4u1NPYMcea35M53RmzAv6pZEJOwUWpG9KZ9EnxPojUciHARpBi-P1S6Yr9RwqRk8Wf_nlliTldOuEpgKy0fhm8h_TlNTPgjwcWwDpDTvg3FrKjtpBeFMoDTyrwhwxXk7BFg2_CbPFBb2Emfg_BcK9lMaQbIR_qwKtzQKDI1-GiQggNNEQL77kYbZjMPF9qhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نمودار نوسان قیمت نفت برنت در ساعات اخیر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/674817" target="_blank">📅 14:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674816">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
رویترز: داده‌ها نشان می‌دهد که طی سه روز گذشته، تعداد کشتی‌های عبوری از تنگه هرمز به‌طور ثابت روزانه ۳ فروند بوده است
🔹
دفتر نخست‌وزیر عراق گزارش‌های رسانه‌ای درباره میانجی‌گری میان آمریکا و ایران را تکذیب کرد
🔹
تردد خودروهای سنگین در جاده ایلام–مهران از ۱۱ تا ۱۶ مرداد برای مدیریت ترافیک اربعین ممنوع است.
🔹
بیش از ۸٠ هزار نفر در ۲۴ ساعت گذشته از مرز مهران عبور کردند.
🔹
عراقچی و همتای پاکستانی در قرقیزستان دیدار کردند.
🔹
سازمان ملل خواستار تخلیه فوری ۶ هزار ملوان گرفتار در تنگه هرمز شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/674816" target="_blank">📅 14:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674814">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/va7EMysbLkQ2kcuRh1WV3oZHrQ3lwwXhtk9UjDbc-eLY3aYtJAC6jQ6wNyyD8rDZFCA-gFP4ynfyx9LWgYUV-zPrZ2W48wKz4CytzuyssUcYqm8PLMq45sqLbeWPJnbUAxUtNlc9xSwZKwViXgJS0iOhtgFPvUq1ZvyzUa8tJ7XBtrO-OUwwsDtQ5SSkrG_nJQD49YSiIaKvqh_2BjSjj8oeBNdeih4Sc5QuvyF-64AjuLScnojxVlXtR3ItTSI_uzco_bbu_EezNCsP9ULd3MA77TMi7Mby-JxE2A09pK-qU1gcAp1xxXeYnLEWqRqwi8LfEuA6s1kbbf-zpa-Vmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برنامه امتحانات نهایی پایه یازدهم برای استانهای جنوبی اعلام شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/674814" target="_blank">📅 14:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674813">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4b9301063.mp4?token=iTnOFIqkjPIvDtEvqTGSSynGqiiutY21mhiHYSG20Bq-V9CZhmw-ogWY-U2wyCX8z58i3-Tr9adQ_TkZOVT5lqAyzhiVymymNPuSlObiOGkoQ7JfRLjP6cXJe2Olpp42jfbVcXyASCIxNj6deZCVZxliy0RMRcm8_Ze_mG7p6sj2PMzd6DZ5Nz1d3evl6Dous7Iq8w5P0aifZveJkPU_v-jenFmjHzA59teCF2uBW62CS-R1bjFvwSLZRCJHZ-zV7rOKfWm813me6hF8qVwDzaismAyt0TKMwmBkLN03_Ya3SEVr9u3dEdR1lH1xXJLLaPm_qzeaNA-JrBG2aQQNlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4b9301063.mp4?token=iTnOFIqkjPIvDtEvqTGSSynGqiiutY21mhiHYSG20Bq-V9CZhmw-ogWY-U2wyCX8z58i3-Tr9adQ_TkZOVT5lqAyzhiVymymNPuSlObiOGkoQ7JfRLjP6cXJe2Olpp42jfbVcXyASCIxNj6deZCVZxliy0RMRcm8_Ze_mG7p6sj2PMzd6DZ5Nz1d3evl6Dous7Iq8w5P0aifZveJkPU_v-jenFmjHzA59teCF2uBW62CS-R1bjFvwSLZRCJHZ-zV7rOKfWm813me6hF8qVwDzaismAyt0TKMwmBkLN03_Ya3SEVr9u3dEdR1lH1xXJLLaPm_qzeaNA-JrBG2aQQNlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رجزخوانی کودک ایرانی برای سگ زرد در مسیر پیاده روی اربعین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/674813" target="_blank">📅 14:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674812">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجواد موگویی|حرف بی‌حساب</strong></div>
<div class="tg-text">ماجرای جنگ۲
به‌روایت جواد موگویی
روایت بیستم:
گفت‌وگو با سیدعباس عراقچی (بخش دوم)
فیلم کامل
🌐
@majaraa_media</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/674812" target="_blank">📅 14:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674810">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41f39ca15b.mp4?token=i_uSjGSIi6QKWJ0o5skdMjU-JAkt1FBEO51tuXaW_yZLjojMBg7GuLhOzpxHyNcjly8rknhPBYV9OFHHvxPbmftgkTlaFxgwFBfMV69FTo_eKIULOWg-DBUQfhYjhz3IsbVMPvLT2Or8XHpEJrqH0dQuHhX85-AUW_XspRPMfco20OfZkEa_8fVZqgBEfyopfwiB6LjVjdQcrs8n-4kKLZIeAGqw4eBGKalo1q-yjgkdLxpPSRtMXHT6muHHVK6BLm1823WH7vxnxZu876DMQBMkBDpHgCmX3Qb-esfnK14RkRA0-Q-ZyYMqrr7NH3NJKWKMh6bSmFkztJKHXYIaqkosKezwpxyAGQ4eGAwBK-n11ATcZVKw1nt4Qjk0sR2mnbVFVibbjL7LKfimOb4buo4JDNP6Fp8NKtUDC9zO98BKdFSxDbfW-t3Dgffs8B5SpENN0GTQcup6knSfWa3LnfglFQYWSDqFT2_UOPcb2T6GrC7sQwtm4b5hCoNaXrc6nFeNnsGYFDBviPZHsJI3Iy6v5hthm767rH7JPWTQS-LSH1Ix7Z71D9t3YcUGsgA31TI4anYkgpBN0OX6fJaVYvtaVXg62DrINCiONCpkRHNENO6Wj8sVjfaQSJHQrZizC6UC-4as8kImZyc3S1Gsj7x3RsLU9TXn02oIjSFNjN0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41f39ca15b.mp4?token=i_uSjGSIi6QKWJ0o5skdMjU-JAkt1FBEO51tuXaW_yZLjojMBg7GuLhOzpxHyNcjly8rknhPBYV9OFHHvxPbmftgkTlaFxgwFBfMV69FTo_eKIULOWg-DBUQfhYjhz3IsbVMPvLT2Or8XHpEJrqH0dQuHhX85-AUW_XspRPMfco20OfZkEa_8fVZqgBEfyopfwiB6LjVjdQcrs8n-4kKLZIeAGqw4eBGKalo1q-yjgkdLxpPSRtMXHT6muHHVK6BLm1823WH7vxnxZu876DMQBMkBDpHgCmX3Qb-esfnK14RkRA0-Q-ZyYMqrr7NH3NJKWKMh6bSmFkztJKHXYIaqkosKezwpxyAGQ4eGAwBK-n11ATcZVKw1nt4Qjk0sR2mnbVFVibbjL7LKfimOb4buo4JDNP6Fp8NKtUDC9zO98BKdFSxDbfW-t3Dgffs8B5SpENN0GTQcup6knSfWa3LnfglFQYWSDqFT2_UOPcb2T6GrC7sQwtm4b5hCoNaXrc6nFeNnsGYFDBviPZHsJI3Iy6v5hthm767rH7JPWTQS-LSH1Ix7Z71D9t3YcUGsgA31TI4anYkgpBN0OX6fJaVYvtaVXg62DrINCiONCpkRHNENO6Wj8sVjfaQSJHQrZizC6UC-4as8kImZyc3S1Gsj7x3RsLU9TXn02oIjSFNjN0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مشاور پنتاگون: اگر ایران بر تنگه هرمز مسلط شود به عنوان چهارمین قدرت جهانی ظهور خواهد کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/674810" target="_blank">📅 14:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674808">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/377c3869f9.mp4?token=rkC2L32irVW_OE8oeym169Ird8aYj5yK9snOXe4AhCz4RWk2EE4wb4l8U46-nQ7-m71GciHjp-i_WWC3xNsuezEowRC_w31m60JiAzQ9TI9o-Czd86X0k8s1Yv64v6wv3eKlPonklyLB4eQ58Yle7GJYjnV9dRdWJO8vVm-SzTJ00V_fyZaDb9zjFMJDsMKfVZor98bS0u9N2iYreN8euRkSA2rzhrLZR3dXiLY7mNwrPL7a8LoihihDmb2Ha2tdyzEifutsknTjQ2MP8iI0HGN9MgUQEtDwl_nnDivdkyjf2ozvdj0toSrKLdfTmDa08UZ_OaghgME57ZNudVo6FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/377c3869f9.mp4?token=rkC2L32irVW_OE8oeym169Ird8aYj5yK9snOXe4AhCz4RWk2EE4wb4l8U46-nQ7-m71GciHjp-i_WWC3xNsuezEowRC_w31m60JiAzQ9TI9o-Czd86X0k8s1Yv64v6wv3eKlPonklyLB4eQ58Yle7GJYjnV9dRdWJO8vVm-SzTJ00V_fyZaDb9zjFMJDsMKfVZor98bS0u9N2iYreN8euRkSA2rzhrLZR3dXiLY7mNwrPL7a8LoihihDmb2Ha2tdyzEifutsknTjQ2MP8iI0HGN9MgUQEtDwl_nnDivdkyjf2ozvdj0toSrKLdfTmDa08UZ_OaghgME57ZNudVo6FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر شهید سلیمانی و شخصیت‌های سیاسی ایران روی دیوار هتلی در تانزانیا</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/674808" target="_blank">📅 14:19 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674807">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a58e93fb93.mp4?token=nU9W9q_M7RJN8vo8iHs6yzYHDZJSlpcNW79HfFk2lOqQa0qPRCZN1MgXlvVVOci1UA-oPVOKg9ndIlncpQK0QikO3WFty_oBzeMqGvwwXK784KHvrPg-xTPXywTrl0FxSJXqR42k1A998yRbaxJ9oEbnN6AhZSGvIb8cTchhE-1ZJi52bP2l-n-ucOOGd9jzHa_GMlFY8u1YlBMH0CqxNT1Dg81V0gKQI6-OqJF6xsnyg11AOFQetS9K-UrmwnKEC1KIB3cG-zheuo3IfSHzMsUIR_KKc3oiP1h7u1HIfpYHn0x5XJTQ7crhnjn4FqHY8GkfcuH3KGMR0USTfVkQDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a58e93fb93.mp4?token=nU9W9q_M7RJN8vo8iHs6yzYHDZJSlpcNW79HfFk2lOqQa0qPRCZN1MgXlvVVOci1UA-oPVOKg9ndIlncpQK0QikO3WFty_oBzeMqGvwwXK784KHvrPg-xTPXywTrl0FxSJXqR42k1A998yRbaxJ9oEbnN6AhZSGvIb8cTchhE-1ZJi52bP2l-n-ucOOGd9jzHa_GMlFY8u1YlBMH0CqxNT1Dg81V0gKQI6-OqJF6xsnyg11AOFQetS9K-UrmwnKEC1KIB3cG-zheuo3IfSHzMsUIR_KKc3oiP1h7u1HIfpYHn0x5XJTQ7crhnjn4FqHY8GkfcuH3KGMR0USTfVkQDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بلینکن، وزیرخارجه سابق آمریکا: ترامپ نمی‌تواند از گرداب ایران خارج شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/674807" target="_blank">📅 14:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674806">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e8365e938.mp4?token=p1Tgu4eurLv-YMF6pPP10xlcNqUzor7-nIHQd2uLiGfHm-25trXnVdlZxsuXetMyHoxr5JNIk8Kg4ff5b8foiUL5Y5KWovRrHaTT6i6GMYyPHBmq9UHOLhTLgWctvXOFHZVA9H2wl0SoV9_ZtDJjl9m4KhmesAJ6gUqtjO2xmlWCEYTYQo1fzbcRemmUtOlfgdOR_jYLfCFxqmLbEiLvjRJ1pNVw8F8ljZkDOwug2op0Ea7cDsnnT-mQx81rf8gdJxl2GOy5lSahIyXZ07Z28koZDuVEoUW7K0YR8YzA6xYxcf-JJFWPOZnKg5lB9GcEsTjRqaAPDeb7qBT1NjRI8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e8365e938.mp4?token=p1Tgu4eurLv-YMF6pPP10xlcNqUzor7-nIHQd2uLiGfHm-25trXnVdlZxsuXetMyHoxr5JNIk8Kg4ff5b8foiUL5Y5KWovRrHaTT6i6GMYyPHBmq9UHOLhTLgWctvXOFHZVA9H2wl0SoV9_ZtDJjl9m4KhmesAJ6gUqtjO2xmlWCEYTYQo1fzbcRemmUtOlfgdOR_jYLfCFxqmLbEiLvjRJ1pNVw8F8ljZkDOwug2op0Ea7cDsnnT-mQx81rf8gdJxl2GOy5lSahIyXZ07Z28koZDuVEoUW7K0YR8YzA6xYxcf-JJFWPOZnKg5lB9GcEsTjRqaAPDeb7qBT1NjRI8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جان میدهیم اما سر تسلیم پایین نمی‌آوریم
🇮🇷
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/674806" target="_blank">📅 14:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674805">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
اطلاعیه شماره ۵۰: سه سوله نگهداری مهمات و تجهیزات در پایگاه آمریکایی العدیری و برج مراقبت ناوگان پنجم دریایی آمریکا به آتش کشیده شد
روابط عمومی سپاه پاسداران انقلاب اسلامی:
🔹
ملت شجاع و وفادار ایران اسلامی، عظمت شما رعب و وحشت را بر پایگاه دشمنان مستولی کرده است و اخلاص شما شوق جهاد را در رزمندگان مضاعف نموده و فرزندان شما در سپاه و بسیج ذوالفقار برنده خود را پی در پی بر دشمنان فرود می‌آورند و آنها را در هم می‌کوبند.
🔹
در موج ۲۷ عملیات نصر ۲ با رمز مبارک «یا اباصالح المهدی ادرکنی» رزمندگان با هدف قرار دادن سه سوله نگهداری مهمات و تجهیزات در پایگاه آمریکایی واقع در العدیری کویت، این سوله‌ها را به آتش کشیده و از بین بردند.
🔹
رزمندگان همچنین به طور همزمان برج مراقبت ناوگان پنجم دریایی آمریکا را در بحرین هدف قرار داده و خسارات زیادی به آن وارد نمودند.
🔹
عملیات تنبیهی ادامه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/674805" target="_blank">📅 13:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674804">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQN61hsxA7jopjQuz-O7PePuDu4oaS14OE1BBG9olfy1qF1IkZmwvUp6LKjor4TJwgl39UYC5zwjvUSc78diHWfo1M8C8l4B0W7Aiu-xUzdgq8w7cIOpEdDlOvHyq_mumzIq5L3yNAaTi-NRNVZzZixFpbLMTBVFJm999HCRvaXOVvegEu_Ps7Xayhuw2-J8RzTVEwowjVPz5njrNXIsDk-SBpHPJTnndtLdHVqrxwl9QK1MP4Q-FJpAe7FjJ4WX4TTCNXyglVOGBnaREnmADs-9jMEADcVgnAMgB3Q3TErDQtTTDCIn-7tO9mdDmFB2RzxYK1L1FpaPVuZxfqPrOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زهران ممدانی شهردار نیویورک: در صورت حضور نتانیاهو در نیویورک، بازداشت خواهد شد
🔹
در صورت حضور نتانیاهو در نیویورک (برای شرکت در نشست سالانه مجمع عمومی ملل متحد) صد در صد او را بازداشت و برای محاکمه تحویل دیوان کیفری بین المللی خواهم داد.
🔹
او به اتهام ارتکاب…</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/674804" target="_blank">📅 13:52 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674802">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمداحی نور</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">{webahang.ir} Emam Reza Jan</div>
  <div class="tg-doc-extra">[WebAhang.ir] Amir Kermanshahi</div>
</div>
<a href="https://t.me/akhbarefori/674802" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/674802" target="_blank">📅 13:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674801">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf03fc9e60.mp4?token=CG3CNiUr69eb_vjWO-KkopztkSHyaCAAlcfAt5FBc7p2bz0mgAH2YxxJNYFU-0mecWA7qAK60SqS6Az3dmUm1jtSHSSyI5irtSv63hPbIUQJmENdXtcVdb9ucht9ATDRMxIpMFLkeN2AHv0m8j1PC79HOM_1Kuofah_xcmSUMYM4kFvIBQn9FiaouXTCZ-nW0-q_u2qY1xdXIagSwPTh2OeuUp_dfGcO_Zb9kbsqQUBTGE1hZXK5Quh0WsI_30LgfaWsku95GUVK4Xjp16RUv6mO3fysx3qMwoNGQMyGhlz8uBuv6l3GsDIi561wSwOByUEAzpeJsK8h52lP3bXQgFb9DSQ_sxgED8bOw4dZyASOkSGSm1H0AcqZDvfZSZvYkzal4-Bpc7E8ws5fF19_Ox0lYamSuU0lJD-2NllBHM-3lT0XvnMwuUjvV-1EcdeLRNQqw4nQ74HopSaj061WDF3tWcysXKSX_0DQeRa6VNTm8CFJ15sJGQ-Lx23FZ_SDSrptTQHTwDW9Ysh9rpkKa5opwm5e-rPF1BVS8jWMJYvLSUJFPSGhBIfgZz606e3Pvt9LiTMlf8c21VKj6WZtWuzr5ps8PJ-zep_P3c4OEMv_70K_FOgaxT0YNqdQ_zb46mVXdwoXJJRr6NeFx_zQ4xmEATnDXFOC3Ln7EM6kkfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf03fc9e60.mp4?token=CG3CNiUr69eb_vjWO-KkopztkSHyaCAAlcfAt5FBc7p2bz0mgAH2YxxJNYFU-0mecWA7qAK60SqS6Az3dmUm1jtSHSSyI5irtSv63hPbIUQJmENdXtcVdb9ucht9ATDRMxIpMFLkeN2AHv0m8j1PC79HOM_1Kuofah_xcmSUMYM4kFvIBQn9FiaouXTCZ-nW0-q_u2qY1xdXIagSwPTh2OeuUp_dfGcO_Zb9kbsqQUBTGE1hZXK5Quh0WsI_30LgfaWsku95GUVK4Xjp16RUv6mO3fysx3qMwoNGQMyGhlz8uBuv6l3GsDIi561wSwOByUEAzpeJsK8h52lP3bXQgFb9DSQ_sxgED8bOw4dZyASOkSGSm1H0AcqZDvfZSZvYkzal4-Bpc7E8ws5fF19_Ox0lYamSuU0lJD-2NllBHM-3lT0XvnMwuUjvV-1EcdeLRNQqw4nQ74HopSaj061WDF3tWcysXKSX_0DQeRa6VNTm8CFJ15sJGQ-Lx23FZ_SDSrptTQHTwDW9Ysh9rpkKa5opwm5e-rPF1BVS8jWMJYvLSUJFPSGhBIfgZz606e3Pvt9LiTMlf8c21VKj6WZtWuzr5ps8PJ-zep_P3c4OEMv_70K_FOgaxT0YNqdQ_zb46mVXdwoXJJRr6NeFx_zQ4xmEATnDXFOC3Ln7EM6kkfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بعد و قبل؛ تصاویر پربازدید از تغییر عجیب چهره‌هایی که دیگر قابل تشخیص نیست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/674801" target="_blank">📅 13:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674800">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFaXK_zIL16XXnjyUQtKOThhklUIbTJQtI3G-krsVnF2hpXTjXwcGZjj-Aj59ovYBdbnJZtUos4-yI4L5kFGjzJ5gJ7J4mTYRiBF01FrDexXOXHdy0F8lbU9IWXZeD6XQ-DpKxPp3MDp8_J9q5W-yUECNnVVu5-AMWe0-W9NP6kwVw9BV7W3qZkM8WQi8HPUZhNLJIEsFDIkeBuQRT43kHK_B0_6AJ3hpKbWT6BhWU3Y7cA86XHXYsDzrff-jVbXDHMfnxNpT2JgDlwvnlE8k9fAasGQIQhAL2mKBQFRiIjAZnQoU2yFTiuVQs1ELz3G8DHLxrG-I3zD4XDeu4Nb-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تناقض در گفتار؛ آماری از ادعاهای مکرر سگ‌زرد علیه ایران
ترامپ تاکنون :
۱۰۶ بار: «ما ایران را شکست داده‌ایم.»
۹۵ بار: «ما ایران را نابود کرده‌ایم.»
۸۸ بار: «توافق با ایران قریب‌الوقوع است.»
۷۵ بار: «تنگه هرمز باز است.»
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/674800" target="_blank">📅 13:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674799">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b07f492a7.mp4?token=MmshLRM39QDv99KFkGOWl_IOuPqdCOH6KXwu7A-mk5iBxHivPFcKl-7C-OBO0EWJm5RPzNyjj9W5VK5e6Wjz_nPxaSt0R9ciHlN7_z6lK2ffBPYYgaYeKTCRsG3d0WmP4y0x3jTfNG00g4tze7VMBZ4oUnmTMwcFjKLDK7IA9eWgYG0xwZM3cpyUHNM1OIbOudsBKvCjLeje85qyFmCKoaGtMDxt0NixGMkPnzg-o2DboOIC8TvFu5tbxY0r1CgbTAqIuRLACaIOCISpmmKnOFdLrR4bb7cgpXlCTAZyKB6WhfP50bLa0N-rBwyh5XvAQiipRS6VRJXhuFZ2Hxp6tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b07f492a7.mp4?token=MmshLRM39QDv99KFkGOWl_IOuPqdCOH6KXwu7A-mk5iBxHivPFcKl-7C-OBO0EWJm5RPzNyjj9W5VK5e6Wjz_nPxaSt0R9ciHlN7_z6lK2ffBPYYgaYeKTCRsG3d0WmP4y0x3jTfNG00g4tze7VMBZ4oUnmTMwcFjKLDK7IA9eWgYG0xwZM3cpyUHNM1OIbOudsBKvCjLeje85qyFmCKoaGtMDxt0NixGMkPnzg-o2DboOIC8TvFu5tbxY0r1CgbTAqIuRLACaIOCISpmmKnOFdLrR4bb7cgpXlCTAZyKB6WhfP50bLa0N-rBwyh5XvAQiipRS6VRJXhuFZ2Hxp6tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظهٔ عملیات استشهادی یک فلسطینی علیه صهیونیست‌ها که منجر به هلاکت یک صهیونیست و زخمی‌شدن ۳ صهیونیست شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/674799" target="_blank">📅 13:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674797">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B3OOXHTcWUx3zeguQrMtv62VHP8uI2CeJJuAJZHfSa39HH3aT-oMV3ufJOP2QtEBSTeyKyTEfwctB1b2njdFs8uewl9VA9Hc8PHnCXXbsxSwWsG1tqF1txLjnaKjJyOYymU1d8cyem_u5NYZHBxIzb6NUFEZ6WQ41L7aj2gtmm3iHf3oUjpwTJ8JoQKoPZpEHoXuUdOqaorKuzJodtbp7MibTOj9mA2VeXmSj_-AnvUyywMlZU3dg1YOqQg3kETydQfTRzVUVUQfTdPQmLjjtIqmmpryghdO2-VK9oMUWz7iSvB9Lc9x0lA-kcWS3WLqO-rpWOAou1Wf3VpZdGtJ_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JIUhDDYiV1zAMtReniaoobb7eEMt2SjhLy5pOd5HG3hAu5sYDlfG9LDMz4qPw7vq6DFdSQFJTSAqDs_FCwziV_g4iaw2XF2WTGuKAau0dqnvHUEM-nGd0dO5fBnXHdaGK9gM1VoCGQ9IbImIyRP7Z3eSJXSeYEhKjaAqbIzTyWLzha8vmHL78wYqcR7mK5TEsM60pOcinGckhx4iLmkDOT8PjMtDBlvAyN0cenWf1u50vJwVBUlPNOGe09GeZXck6p3X6bAOfuiuS8MWdzhKicHH_b2AbLsDXrdCRWgfXQG58v-ZrzcXQsf-x23JqI-1Xgj11-E-xK4TNvmo9R5TiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
استایل جدید صابر ابر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/674797" target="_blank">📅 13:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674796">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gEELKZCPdg45mhaBSsIiiCQSJ4kYKp-uK0E3bCkWWNt8Uxczj2-ZtcnsVjOJohfH2VyZpcFlauDJXrV8LNG0pbJm8P7oRBRpbyTbrZgkJMKduJdN34CuVOzCcr9hCFbjD10BLD96xFtxYcSVrFQADT8aRTmvBXyNoX-durX_yMf9OsFNMfQs6hCryP848CTRXJhYsltubc721mV3MyyfH7fY3tuD5x-PvH27rRFVotfl0sSXMvu8ym1QQ__rP9KJpYDzBpU6HtsODr27IqDwOM46U1ny2CHvnp1V7cd2-Bnvh3eoiFPNVIhV88-Qe3mJ4Z0FWJgUbjF-Yfnwp-lBWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک کاربر عرب زبان: ایرانی‌ها خوب بلدند پیام‌های سیاسی و نمادین را هوشمندانه منتقل کنند
🔹
وقتی ترامپ شهید سلیمانی و شهید ابومهدی را «دو مرد شرور» توصیف کرد و گفت: «من آنها را از بین بردم»، انتظار می‌رفت نخست‌وزیر عراق از حاکمیت کشورش و عزت یکی از رهبران نظامی آن که در خاک عراق ترور شد، دفاع کند. اما پاسخ او این بود: من درگیر سیاست نبودم و از گذشته به اندازه کافی رنج برده‌ایم.
🔹
در مقابل، پیام ایران به شکل دیگری رسید. آنها او را به یادبودی بردند که در آن تصویری از رهبر شهید به نمایش گذاشته شده بود و کنار آن تصویری از شهید سلیمانی در سمت راست و ابومهدی در سمت چپ او قرار داشت؛ صحنه‌ای که به وضوح نمادی از جایگاه این دو مرد در حافظه جمعی ایرانیان است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/674796" target="_blank">📅 13:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674795">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
سپاه: با فوریت تا شعاع ۵۰۰ متر از اماکن محل‌های اقامت پوششی و مخفی نظامیان آمریکایی فاصله بگیرید
روابط عمومی سپاه:
🔹
مردم شریف کشورهای محل استقرار پایگاه‌های آمریکایی در منطقه؛ رژیم کودک‌کش آمریکا پنج ماه پیش بدون دلیل منطقی و توجیه قانونی با به شهادت رساندن برجسته‌ترین دانشمند دینی و رهبر سیاسی جهان و همزمان به شهادت رساندن ۱۶۸ کودک دانش آموز معصوم، جنگ تجاوزکارانه‌ای را علیه ما آغاز کرد.
🔹
ایران بعد از ۴۰ روز جنگ پیروزمندانه در حالی که می‌توانست جنگ را با قدرت ادامه دهد، برای بازگشت آرامش به منطقه حاضر شد با نهایت گذشت با چنین جنایتکارانی پشت میز مذاکره بنشیند و تفاهم‌نامه پایان جنگ را امضا کند.
🔹
اما ذات جنایتکار و درنده خویی ایالات متحده موجب شد از همان روزهای اول تفاهم، آمریکا درگیری‌ها را از سر گیرد و تعهدات را زیر پا بگذارد و نهایتاً از ۲۱ تیر ماه رسماً تفاهم را ملغی و جنگ را از سر گیرد.
🔹
با گذشت ۱۳ روز از ازسرگیری جنگ، آثار شکست مجدد آمریکا ظاهر شد و دشمن فهمید با عملیات جنگی نمی‌تواند بر نیروی مسلح ما غلبه کند. اما برای خروج از بن‌بست به جای عقب نشینی به ارتکاب جنایت جنگی متوسل شد و پل‌ها، اسکله‌های صیادی، قایق‌ها و لنج‌های مردم، خودروهای عبوری و راه آهن را هدف قرارداد و غیرنظامیان را به شهادت رساند تا جایی که در روز گذشته با کشته و مجروح کردن زائران اربعین حسینی در مرز عراق جنایت را به اوج رساند و ماهیت یزیدی خود را آشکارتر کرد.
🔹
از آنجا که در صورت استمرار چنین جنایاتی دستور کار ما قصاص جنایتکاران خواهد بود، بسیاری از افسران و نظامیان ارتش متجاوز آمریکا از ترس آتش رزمندگان اسلام پایگاه‌های خود را ترک کرده و ساختمان‌هایی در شهرها را محل هدایت جنایات خود قرار دادند، به عموم مردم کشورهایی که محل استقرار نظامیان آمریکایی هستند، هشدار می‌دهیم با فوریت تا شعاع ۵۰۰ متر از اماکن محل‌های اقامت پوششی و مخفی نظامیان آمریکایی فاصله بگیرند تا در امان باشند.
🔹
مردم همچنین می‌توانند محل‌های جدید جابجایی نظامیان اشغالگر آمریکایی را به حساب رسمی روابط عمومی سپاه پاسداران انقلاب اسلامی در تلگرام به نشانی
@sepahnewsiradmin
و یا بخش "تماس با ما" در پایگاه اطلاع رسانی
sepahnews.ir
اطلاع دهند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/674795" target="_blank">📅 13:13 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674794">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
حمله انتحاری به نیروهای پلیس پاکستان با ۱۴ کشته و ۲۴ زخمی
🔹
یک مقام امنیتی پاکستان اعلام کرد در پی یک حمله انتحاری در ایالت خیبر در شمال‌غرب این کشور، ۱۴ نفر از نیروهای پلیس کشته و ۲۴ نفر دیگر زخمی شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/674794" target="_blank">📅 13:09 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674793">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
پایگاه داده‌های دریانوردی کپلر: تعداد کشتی‌های عبوری از تنگه باب‌المندب در ۲۴ ساعت گذشته به ۱۲ فروند کاهش یافته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/674793" target="_blank">📅 13:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674788">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lJOtOBTP83Jn5Dn-oHfovF4EPmaaJMqmf35HBIMPgVSJPDFKrtWJ_-imF9PHxUEYXIHcB2UsobRt3c3-Y1bUtbQiWv6tHV-xPQLrJu3SM0gjA-UuP6YOUZmRR6h4_9IoYwKYtut70dNp0W6N0AD9YOAb7cdDBYydLsBfhzhD0gysWljTDqNgmmY4gWqXjT02L4VTPNiRtl1TfuufojHima0425NN1F5_KCZl3IyZl7RN6Pi84AM4Wi6jxjRkm8TxnwqoePMoBnp6Y_D-bv3ch39TDipG7aNy2naV4aAtLQBcnPwow7GKYwZ5bvojMJFPT4dDVGDQhZCRg15h-lNGeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iXp7limxTeX2nKEqv9Wcvj1VaDmIlGaVjVrqktBMbeaLl62f5kJlp75xW6N7W3oPlr5zj5g0U0VJQBZuBSD-Yyu68I95XkoqW5Qx--Kz7_RW3b86Egz53J_mNPhEQFyw1MBCs5pkH4YxoWqoWeRnz1eUj3cW3wUhejejTZ6v5LO8dHA-8nx0fv1WfSuPbjjRBxi1uqu4NC2j2RXmfIVxYEEf9S1hkMZ2rFQnvLmmBuBDRX0m3IfAUplVm03RqMVnfnTgb-bfTnQh5LB-45P1W9tjW-kYtR5RKDvITxIqZZWZMSGKFx51a_8blno7Ic7DC02fFP0e3pwUnpRWy1f7kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qM0uFYmjoYqwG_5H75uVn-j0kI0wW2TKJ_-wiHmJGWNv8veEcjMSrd0qjCADTkwoZOC2PMzTcsXqmq9NG1AJegPZfBS0JHcpAEIL_7GUApajHBEl0mZepfYZ7SeYQqPY7S7mSnoaO7T-NfWwZkVPWeGw0uD5msSrerL9xyWepX5XhzJykTTOzj-Ctg0vRBtfQGum5hNHTyna9kvQWALzcwBe0-ie10m3ZaWIGkibnkNP6_CEdG9IWgApW5rQ74pEq1e0eF8RFm-tum5yFgrah7PfMeli1deDlswEz6bUvx7pSrIeMl2eSgsSgWM904vCLQYsDARuNJnst7uxcLnttw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vKm07WcMGgAwX01yGuLu80aKylAgag9Ck5bZhQr2HUMzBrxQM4NLo0r1fMq-0l5h3z4Jc_JdHb71LQbIz0drMpvyPZyNb9jw7ICOkNSdSLVgqQMsL2J5_zvgtfjlDRws3DeG0PR6Rgpuox68LVkE_tUitYaUO9_rc7hwLI_ELz4vjoG4rx9x83w3Gbgtl1VYu9wSrzY_mJhXT8bRsWMKdhEAIhzaJzjEbV_KQzROaemdIo0pnIOP0VU_holWLX77v-1PuY9RUfG8MaFaRniK0j8YoOSvOdkrNMQtnqhuiYeuu7c1FCSpthQe2UnkjmnJ6xxbOrGgQuwhh67B_VqHVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fh8Ik7N528J1zlEE_c5Rdn_7X4lAWTOd5LOOlr0c8ipilS7ncdqJR1qhLYtmaB9EwVLQntSCs3EUli4oLAIrDGD2Jg_fw99nl0eHJFHaUQOzYddT6h8HejRqcF_YUNxt4hCE8mm2mFo9RhDZeaNfSeDyU_gqPSARN3E3jA6jNwPNBqzlL3gZJg-4TRLq88s3rdVmpNF6WpHuf0aWECQsDxPkn_T7vFMBG8VCB8qeicAHlckRXeuscm4pwuKYZaaTHQgPIVInFEbRhtPD9VWmHdqsvvbGjSthBswCQSKwJVIHRiKAr1_2CQWtbukkfS9zHlUHEfUMEDsne6ayC_N5jQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اگر عاشق کیک خونگی هستی، این ۵ ایده خوشمزه رو از دست نده
🍰
🧁
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/674788" target="_blank">📅 13:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674787">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcb1e594d7.mp4?token=a6PTzFxwxi6ncxO2jzeL9Z6CZV7bCjfmpXCC_sm-bB2KVOgrqKK0DYRFTitPwrXRTUi5oKo4S3nCzjS9IVBRyp7j84hPiXC40dnR185dW8kEB4k85bxeHNfO-nIyzATAiS2kmYsKHg-wcHl-hmZTtcQGDs-LIUCA6Esah_6MjWnBjuIaWDE-dJyrWlglaJ8_3xM9ej7vsydv2BgGClf4k4J0hfSPS3ydNHVXJdG-HGFfexrhXvlfh5WaUpXPkeGz0-UmV57is-c0HeHOWG1RjwfJxj8ee3619R1TIzBNJOtsw5tiYspS4WtQZqLlCD4b2hwL-WgjxDmHz1lnPtytZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcb1e594d7.mp4?token=a6PTzFxwxi6ncxO2jzeL9Z6CZV7bCjfmpXCC_sm-bB2KVOgrqKK0DYRFTitPwrXRTUi5oKo4S3nCzjS9IVBRyp7j84hPiXC40dnR185dW8kEB4k85bxeHNfO-nIyzATAiS2kmYsKHg-wcHl-hmZTtcQGDs-LIUCA6Esah_6MjWnBjuIaWDE-dJyrWlglaJ8_3xM9ej7vsydv2BgGClf4k4J0hfSPS3ydNHVXJdG-HGFfexrhXvlfh5WaUpXPkeGz0-UmV57is-c0HeHOWG1RjwfJxj8ee3619R1TIzBNJOtsw5tiYspS4WtQZqLlCD4b2hwL-WgjxDmHz1lnPtytZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«تقدیر سهامداران از تقسیم ۲۰۰ تومان سود نقدی در مجمع شرکت نفت سپاهان »
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/674787" target="_blank">📅 13:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674786">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
انفجارهای جدید در اربیل عراق
🔹
منابع خبری از وقوع انفجارهای جدید در اربیل در شمال عراق خبر می دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/674786" target="_blank">📅 12:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674785">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
انفجارهای جدید در اربیل عراق
🔹
منابع خبری از وقوع انفجارهای جدید در اربیل در شمال عراق خبر می دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/674785" target="_blank">📅 12:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674784">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jvXkSEjgmni6CSRrao0XF2_V3HMRISByIjobnH3AtKV006J19E6K-i1i8q0OwKZJEfyY6piSTzwV2H8Ed687w4alCaJB9idNBcruWtZxI6YP0PdF5fR5fYYm1sTclOudmlHTTLtZEQ4AgO4vvq6gg1GiTZ1X3FUYk5XWl7PkvT0O1uoKRDKZecuBUz7HDGVvqRpMdw1JEgKx28Dvfl-eVGhUyBkTY8czzol9j22iZlwit-x67XkpDs-KqmMj705rkbHnBSN_aNldD9qZMuUxbQgpTD6lHcyEb1dF4Sha8zfqWSclIdlh1RbbI0dcu5DpH0LparYrnNDhWKhvA6hjKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رویترز: در ۱ مرداد، تنها یک نفتکش از تنگه هرمز عبور کرده و این کمترین میزان از ۱۷ اردیبهشت تاکنون است و هیچ نفتکشی نیز وارد این تنگه نشده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/674784" target="_blank">📅 12:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674783">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
درآمد دلاری نفت ایران ۱.۵ برابر شد
🔹
اطلاعات رسیده از وزارت نفت مشخص کرد، درآمد نفتی ایران از فروردین تا تیرماه امسال نسبت به مدت مشابه سال قبل ۱.۵ برابر شد؛ این درآمد علی‌رغم شرایط جنگی حاکم بر کشور به دست آمده است./ فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/674783" target="_blank">📅 12:44 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674782">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
چین صادرات به ۱۴ شرکت اروپایی را ممنوع کرد
وزارت بازرگانی چین:
🔹
علت اعمال محدودیت بر صادرات کالاهای دو منظوره نظامی و غیرنظامی به ۱۴ شرکت اتحادیه اروپا به دلایل امنیت ملی است. این ممنوعیت از امروز اجرایی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/674782" target="_blank">📅 12:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674781">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
سفر یکسره زائران اربعین تا نجف امکان‌پذیر شد
🔹
برای نخستین‌بار زائران اربعین از تهران، قم و اصفهان می‌توانند با اتوبوس یکسره و بدون تعویض وسیله نقلیه، از مرز خسروی تا نجف اشرف سفر کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/674781" target="_blank">📅 12:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674780">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
دیدار وزرای خارجه ایران و روسیه
🔹
عراقچی و سرگئی لاوروف، وزرای امور خارجه ایران و روسیه در حاشیه نشست شورای وزیران سازمان همکاری شانگهای در قرقیزستان با یکدیگر دیدار کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/674780" target="_blank">📅 12:33 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674779">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hIHJopQ1kFb39_BdOCHrR0zo-_QCIIwSbaCv_shPnp7d9fsYruwa-ZLiLw-Zmlb_gjdZLhO4SBH364ItlVIUYTjExB9essD16q25h69JY_y2AdmLqrSYprp0dqAxmKdu-CISJYNdg3Q8qlo-ytkltFQLFDr_CaFDW4IFj3bRoEzPZlAN5LTO8oTcCMSNkAsmn5vDgnyVKwl9rrOs2UQmYWGvqwfpm_qmuQZyfMgT-iiGwDMI2cS1ToirgZB0dMpLD19JiyhUEZ0t7xDK3g3DJaTlN8QFSnwhSMWQULttrFWSYrTqsHeBK5KmEbil4TJNtv_k1saSBcMNVHk_p3z2QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر روز چه دعایی بخوانیم؟
🔹
شنبه،
#دعای_عهد
🔹
یکشنبه،
#حدیث_کسا
🔹
دوشنبه،
#زیارت_عاشورا
🔹
سه‌شنبه،
#دعای_توسل
🔹
چهارشنبه،
#زیارت_نامه_ائمه_اطهار
🔹
پنجشنبه،
#دعای_کمیل
🔹
جمعه،
#دعای_ندبه
🔹
دعای باران،
#رحمت_الهی
🔹
برای پیروزی جبهه مقاومت
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/674779" target="_blank">📅 12:28 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674778">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
جزئیات جدید از جلسه شمخانی در بیت رهبری که ۹ اسفند بمباران شد
🔹
در روز جمعه ۸ اسفند ۱۴۰۴، برای شمخانی و شماری از فرماندهان ارشد نظامی تقریباً قطعی شده بود که آمریکا و رژیم صهیونیستی در روزهای آینده به ایران حمله خواهند کرد.
🔹
شمخانی همان شب، حوالی ساعت ۲۱، متنی را برای انتشار در اختیار واحد اطلاع‌رسانی دبیرخانه شورای دفاع قرار داد که در آن به احتمال حمله مشترک آمریکا و اسرائیل و واکنش ایران به این سناریو اشاره شده بود.
صبح روز بعد، کمیته فرعی شورای دفاع با مسئولیت دبیر شورا تشکیل جلسه داد.جلسه دو دستور کار داشت:
🔹
نخست، پیگیری اجرای طرح جامع مدیریت اغتشاشات؛ طرحی که ریشه در دغدغه چندین‌ساله رهبر انقلاب و شمخانی و پس از حوادث دی‌ماه ۱۴۰۴ به یک اولویت فوری تبدیل شده بود.
🔹
دوم، بررسی موضوع قریب‌الوقوع بودن حمله آمریکا و رژیم صهیونیستی به ایران.
🔹
این دو دستور کار، در ظاهر از دو جنس متفاوت بودند؛ اما در واقع به یک واقعیت مشترک مربوط می‌شدند: کشور در برابر تهدیدی چندلایه قرار داشت و باید هم برای جنگ خارجی و هم برای مدیریت بحران‌های امنیتی و اجتماعی آماده می‌ شد جلسه در حال برگزاری بود که حمله آغاز شد.
🔹
در جریان این حمله، دریاسالار شهید علی شمخانی و تعدادی از فرماندهان عالی به شهادت رسیدند.
🔹
به این ترتیب، جلسه‌ای که قرار بود هم اجرای طرح کاهش تلفات در اغتشاشات را پیگیری کند و هم درباره قریب‌الوقوع بودن حمله دشمن تصمیم‌سازی کند، خود به یکی از آخرین جلسات پیش از آغاز جنگ تبدیل شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/674778" target="_blank">📅 12:13 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674777">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2aa9f28389.mp4?token=GLGj5mKJ-3edJl2ya7evvFYUKL7kpFOJZ2H6LQuc0pnZhjjVoNZl8EKOfrekwJRe6HigO_dqhyXmZeC28hryU-xluociXT8JwEIEKZcpHX-Z8uJIb31IQAyZ78cWpGHEmHQ1Uu-zTaIXq78L6LKQchtmRq9FPd4BlgOmnUtTOC-ew6G1fQ0yOfFVxb5wnnu09xIgQFQmxraG7eIAUEikysiNlZL5hRH8LLxKEPB7olkeGtcLXYYiUmtZKhjjfdCE35jUndOL0kLuS1fewb7GMxT_pLUzNGvI4LCDzx5LxMzUtjEDwi90ifxD_nXO42tniE2uCowEn2UJ_q-qegvLOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2aa9f28389.mp4?token=GLGj5mKJ-3edJl2ya7evvFYUKL7kpFOJZ2H6LQuc0pnZhjjVoNZl8EKOfrekwJRe6HigO_dqhyXmZeC28hryU-xluociXT8JwEIEKZcpHX-Z8uJIb31IQAyZ78cWpGHEmHQ1Uu-zTaIXq78L6LKQchtmRq9FPd4BlgOmnUtTOC-ew6G1fQ0yOfFVxb5wnnu09xIgQFQmxraG7eIAUEikysiNlZL5hRH8LLxKEPB7olkeGtcLXYYiUmtZKhjjfdCE35jUndOL0kLuS1fewb7GMxT_pLUzNGvI4LCDzx5LxMzUtjEDwi90ifxD_nXO42tniE2uCowEn2UJ_q-qegvLOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چند ترفند ساده که لباس‌ها رو تمیزتر و سالم‌تر نگه می‌داره
🤩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/674777" target="_blank">📅 12:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674775">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
چشم دیجیتال سنتکام در بحرین کور شد
🔹
منطقه ابری آمازون در بحرین که با شناسه انحصاری me-south-۱ شناخته می‌شود، نخستین پایگاه متمرکز پردازش داده شرکت آمازون در خاورمیانه است که در سال ۲۰۱۹ راه‌اندازی شد. تاسیسات آمازون در بحرین شریان اصلی و مغز متفکر پردازش…</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/674775" target="_blank">📅 11:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674774">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
بن‌گویر: کرانه باختری را مانند «بیت حانون» غزه ویران می‌کنیم
وزیر تندرو امنیت داخلی رژیم صهیونیستی:
🔹
باید با شهرها و روستاهای قاتلان (مقاومت فلسطین) در کرانه باختری همان‌گونه رفتار شود که با بیت حانون در غزه رفتار شد.
🔹
خواستار صدور دستوراتی به ارتش برای تخریب منازل تروریست‌ها و حامیانشان خواهم شد. در برابر هر صهیونیستی که کشته می‌شود، دشمن باید تاوان از دست دادن زمین‌ها و منازل را بپردازد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/674774" target="_blank">📅 11:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674772">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d59a059df.mp4?token=IPIv4HdLeXnXOcErbL8Kvi3SxRiVU-cZN7c-CKRXtCKB6bkqT9ToVASL-5fspm5siiH9RbUuNvwE5G1LcOwLZ5oNuiDijoSpSGZ7oWHQ6lxzROS-uF6NhL-bJ2ouJGbUVhYioQ9yvKQBpwW5ifZpfZ6Zd297ksXDyKb2xbXOfSlxii0VLz3vewVwRo8QY88D0bkSzte0Us5GQrmYhnm1Mb8ntq8BBbdkhBOTyxKRgrHFQ03vKzhduN5bs1JllvRzpM56cNiU9AMEzFGDBEIPkXoS4PIw4CaA8jzpMQpSL1sg-jPAThdZnYUtYai3QEsCn69rkLjj1WX_fXEf8vEVrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d59a059df.mp4?token=IPIv4HdLeXnXOcErbL8Kvi3SxRiVU-cZN7c-CKRXtCKB6bkqT9ToVASL-5fspm5siiH9RbUuNvwE5G1LcOwLZ5oNuiDijoSpSGZ7oWHQ6lxzROS-uF6NhL-bJ2ouJGbUVhYioQ9yvKQBpwW5ifZpfZ6Zd297ksXDyKb2xbXOfSlxii0VLz3vewVwRo8QY88D0bkSzte0Us5GQrmYhnm1Mb8ntq8BBbdkhBOTyxKRgrHFQ03vKzhduN5bs1JllvRzpM56cNiU9AMEzFGDBEIPkXoS4PIw4CaA8jzpMQpSL1sg-jPAThdZnYUtYai3QEsCn69rkLjj1WX_fXEf8vEVrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعلام وضعیت اضطراری در اسپانیا در پی گسترش آتش‌سوزی‌های جهنمی
🔹
دولت اسپانیا ساعاتی پیش در پی گسترش چندین آتش‌سوزی گسترده در نزدیکی پایتخت این کشور مادرید و استان همجوار آویلا، وضعیت اضطراری ملی اعلام کرد. این آتش‌سوزی‌ها تاکنون بیش از ۱۰ هزار نفر را ناچار به ترک خانه‌هایشان کرده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/674772" target="_blank">📅 11:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674771">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d27e007073.mp4?token=mzW0QWbrPcta1ZVX6pWUYGOubZHBdBjZnyhVZ2pqkNtyMI1tmlb18GVzoL4_ncg-s1eFOGLkz_zKd9cErwjup2yAVwsfMGGatR5wmytZn7qz3bTKNbj2oObSl2VaJ_vxI3cRUf9bGmwd-pKbOGk-7ha3PnNl43Tre7Vk2qZx2PRROM1CjEgUV4R0M_Jsbj7UXgdR7hGuPDmjtrHBgwgkH5jahS8-XfEOkB7dGTlZ-5E341Ta93m5dcQHtSbJotqJpzEdt0M3S3-jFeyFD2_fab1uELo6y3JyoeU_13W-lQxTHeU8mfY7MJPfR_ig2U-hkAfnyKgiAvyRAG9Js2rtNTAOWHaDq--LOQu2TbqcvgF-r26JnWOohiRwl5l82jyEvqy69j-iGPmiKE4FqwDrQYxb3UxJnn8GJU8wymxuFGIL5oVhWAyYmadVNKSDedP31rgBOe8TGTHMWf1Ikl6Kk4Ayv_ldcPfKQfj4-ZfW99workMe3qDBDqIO48RRYNpa26NP_O-bIeRm-b7xCEsEG4_S-h3b7k-SbkKks9d02Krp6ky5-n_L8TcIXWBCapQMY9zbMiEYcqT-82ZBi4XUBEbCwiip0QEeFXu_vBHKa3OJsz1PqZRK61G1gCvUQBscEOGIOxBMSe8GCahErzrtv8AnFv-jNxDGESPIWh30aKM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d27e007073.mp4?token=mzW0QWbrPcta1ZVX6pWUYGOubZHBdBjZnyhVZ2pqkNtyMI1tmlb18GVzoL4_ncg-s1eFOGLkz_zKd9cErwjup2yAVwsfMGGatR5wmytZn7qz3bTKNbj2oObSl2VaJ_vxI3cRUf9bGmwd-pKbOGk-7ha3PnNl43Tre7Vk2qZx2PRROM1CjEgUV4R0M_Jsbj7UXgdR7hGuPDmjtrHBgwgkH5jahS8-XfEOkB7dGTlZ-5E341Ta93m5dcQHtSbJotqJpzEdt0M3S3-jFeyFD2_fab1uELo6y3JyoeU_13W-lQxTHeU8mfY7MJPfR_ig2U-hkAfnyKgiAvyRAG9Js2rtNTAOWHaDq--LOQu2TbqcvgF-r26JnWOohiRwl5l82jyEvqy69j-iGPmiKE4FqwDrQYxb3UxJnn8GJU8wymxuFGIL5oVhWAyYmadVNKSDedP31rgBOe8TGTHMWf1Ikl6Kk4Ayv_ldcPfKQfj4-ZfW99workMe3qDBDqIO48RRYNpa26NP_O-bIeRm-b7xCEsEG4_S-h3b7k-SbkKks9d02Krp6ky5-n_L8TcIXWBCapQMY9zbMiEYcqT-82ZBi4XUBEbCwiip0QEeFXu_vBHKa3OJsz1PqZRK61G1gCvUQBscEOGIOxBMSe8GCahErzrtv8AnFv-jNxDGESPIWh30aKM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر شلیک پهپادهای پیشرفته و فوق سنگین در موج ۲۷ عملیات نصر۲ علیه زاغه مهمات و سوله‌های نفرات آمریکایی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/674771" target="_blank">📅 11:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674770">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
اطلاعیه شماره ۴۷
یک زاغه مهمات بسیار بزرگ و سوله‌های محل اسکان نفرات در پایگاه علی السالم، به طورکامل متلاشی شدند
روابط عمومی سپاه:
بسم الله قاصم الجبارین
قاتلوهم حتی لاتکون فتنه
🔹
رزمندگان اسلام در ادامه عملیات تنبیهی علیه ارتش کودک‌کش آمریکا و در پاسخ به جنایات شیطان بزرگ، ساعتی پیش در موج ۲۷ عملیات نصر ۲ با رمز مبارک "یا اباصالح المهدی ادرکنی" با پرتاب پهپادهای انهدامی فوق سنگین و پیشرفته، یک زاغه مهمات بسیار بزرگ را در پایگاه آمریکایی علی السالم هدف قرار داده و آن را با انفجارهای پی در پی به طور کامل متلاشی کردند.
🔹
همزمان سوله‌های محل اسکان نفرات این پایگاه مورد حمله قرار گرفت که ۶ سوله بزرگ به طور کامل نابود شد و به سه سوله دیگر خسارات اساسی وارد آمد و تعداد زیادی از عناصر دشمن کشته و زخمی شدند.
🔹
دشمن آمریکایی که در جنگ تحمیلی ۵ ماهه اخیر صدها کشته و بسیار بیشتر از این مجروح داده است و تخلیه روزانه انبوه زخمی‌های آن با هواپیمای آمبولانسی به بیمارستان آمریکایی در آلمان سند روشنی بر این تلفات بالا است، با دروغگویی به مردم خود مدعی است کمتر از ۲۰ کشته داده است.
🔹
این بر عهده رسانه‌های آمریکایی است که در مورد واقعیت‌های این جنگ و تلفات بالای ارتش آمریکا و خسارات سنگین آن و ارقام هزینه‌ها که همه از دید مردم پنهان نگاه داشته می‌شود، تحقیق کنند و آمار واقعی و شیوه‌های سانسور حکمرانان دروغگو را افشا کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/akhbarefori/674770" target="_blank">📅 11:33 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674769">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0438202017.mp4?token=YNblR5i-AL31dhaL0hHcZClNaIwEirsT1Vge8kf2-1NlVEHUFCIXaL_G4HhRAXSiLQ4j_jgy6v0QAdxQ5p_0VC7Rnk9eCoSWTNixSqWnQfBfEIvf7ZNYWSYv0WPyvGSicyrGCfeEjKrb-bHGIjf7zYs7MJZROnVoXOjlrkktoHHAj6D8vC1NfKFnsWrT3xYxKteeK1ac1bgvc4kcvZyc0J4dx9YOynzVMQQTzSYihVqv8tu1V0zNGG6kYffubo1NTJJRpECDIIBtBUuknUaNcWnrXSSuWSEadfL8_EaUEEHAHvW4LA1XBXrpxD-pZqPohITLXn3ASzfBaqyxWg-2lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0438202017.mp4?token=YNblR5i-AL31dhaL0hHcZClNaIwEirsT1Vge8kf2-1NlVEHUFCIXaL_G4HhRAXSiLQ4j_jgy6v0QAdxQ5p_0VC7Rnk9eCoSWTNixSqWnQfBfEIvf7ZNYWSYv0WPyvGSicyrGCfeEjKrb-bHGIjf7zYs7MJZROnVoXOjlrkktoHHAj6D8vC1NfKFnsWrT3xYxKteeK1ac1bgvc4kcvZyc0J4dx9YOynzVMQQTzSYihVqv8tu1V0zNGG6kYffubo1NTJJRpECDIIBtBUuknUaNcWnrXSSuWSEadfL8_EaUEEHAHvW4LA1XBXrpxD-pZqPohITLXn3ASzfBaqyxWg-2lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هدف قرار گرفتن انبارهای کنسولگری آمریکا در اربیل
🔹
برخی منابع اعلام کردند هدف از حمله به اربیل، انبارهای کنسولگری ایالات متحده در اربیل واقع در شمال عراق بوده است.
🔹
در عین حال گزارش‌هایی از تعلیق پروازهای فرودگاه بین‌المللی اربیل خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/674769" target="_blank">📅 11:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674768">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
خشونت پلیس آمریکا و کشتن یک سیاه‌پوست بی‌خانمان
🔹
کوری دورل روئیز، ۳۸ ساله، در یکی از خیابان‌های شهر هدف گلوله پلیس قرار گرفت و جان باخت. لحظات تیراندازی توسط شاهدان عینی فیلم‌برداری و ویدئوهای آن در شبکه‌های اجتماعی منتشر شد. پلیس تاکنون هویت و نژاد مأموری که شلیک کرده را اعلام نکرده است. در سوابق قضایی ایالت ویسکانسین، روئیز به عنوان فردی سیاه‌پوست یا لاتین‌تبار معرفی شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/674768" target="_blank">📅 11:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674767">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1434f8b7b.mp4?token=YNIO-_lrGejOsCg418e7xnZqvPY1koIBrN8ScFh04rYJEdUszVdanSt2xadMZaaGCPr4wNi_GmVwA7r_u7gd_XMfEBZOmDDpl1l6SJaXZnvr3vbwPSEMMP_q5CokdNhgY87cEpX18MBlRb4izaMgupqWCmPJr8eeZw-i-YIglX08ny202mQTUNHDEsmr83RLQDUxJG57V1yf2XirLuMaOEUNHp4dJP1ipFZa3BHdWPW5SrJvaYu4fT6cOssqi8_fMFSfVa7re8kyfXUPRIZhmFoUXG_F9KOwE2JTkB-P9yojGKR3hTi_vvpAj-ZApPKCWZ1Et49_pW71Tq2mmQHOvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1434f8b7b.mp4?token=YNIO-_lrGejOsCg418e7xnZqvPY1koIBrN8ScFh04rYJEdUszVdanSt2xadMZaaGCPr4wNi_GmVwA7r_u7gd_XMfEBZOmDDpl1l6SJaXZnvr3vbwPSEMMP_q5CokdNhgY87cEpX18MBlRb4izaMgupqWCmPJr8eeZw-i-YIglX08ny202mQTUNHDEsmr83RLQDUxJG57V1yf2XirLuMaOEUNHp4dJP1ipFZa3BHdWPW5SrJvaYu4fT6cOssqi8_fMFSfVa7re8kyfXUPRIZhmFoUXG_F9KOwE2JTkB-P9yojGKR3hTi_vvpAj-ZApPKCWZ1Et49_pW71Tq2mmQHOvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی از یک نوزاد تازه‌ متولد شده که به نظر می‌رسد هنگام معاینه، قدرت بدنی قابل‌توجهی از خود نشان می‌دهد، در شبکه‌های اجتماعی پربازدید شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/674767" target="_blank">📅 11:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674765">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SUEtVnebcY0bCtz4dwF_asN2sUFavU9d30Y9G1ww-ESx4ugZRxko_0ZVTsNVuWJ7FXSzcm4ib8sQngZNQ9z93oKHxlh9iDCkQEhT23xbdQgi1UbQkRegdYAD9iO1R8tNItjjH73boUDtx-Qx8nli3XXLh8bArqOQJo4jnF9OglC3mWcvbgokZFK2fOfouyRCPBUvUVgv0EAeXKrwp55AlKQ9mjgemHqXtTvPVtStquNmJTY03BLkvj46Z2mHRH-GCS-Rz4sPfOZAXOUqiAvDKjGZ_chK9Bx1-BC4WbCmIB0P-Nfc2uxzQ9GL64VGUTePpxcAb-xwSxCafM7VK8IFAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با پول یک موتور یاماها، سال‌های گذشته چی می‌توان خرید؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/akhbarefori/674765" target="_blank">📅 11:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674762">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81a7d74649.mp4?token=m0RytvI23DwNIeKlMobn1jjEt5cK-BY3RxzcexvvmnKzGkKLNM8g7iOUEtw5bgrNP_gS1Ea907rBfWancwusHb1UjrZ3W852O6t4QjJk6zxJJp1DzGvSSbwjXEoPpEd9jQfMI8C8j7uRK3VWDbhyqNXqUMt5NQsk1tkb7tkunaY5GarzDRl_FAC2j-n5b6Df5kM6KuKW0Hxfuj35Ll_Uxdjs7G_KO6YiqFd_BG0Vx6_FyRZSDXvCCSa-h_i83hMLG3fa-WuFVzFP0QB6EJFUcw2RFKIeHUwpqqUkPFQtwDjZDN_m0tCxHTiHL6rb4f_q0AiYOKnrbufGf34OJJOXog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81a7d74649.mp4?token=m0RytvI23DwNIeKlMobn1jjEt5cK-BY3RxzcexvvmnKzGkKLNM8g7iOUEtw5bgrNP_gS1Ea907rBfWancwusHb1UjrZ3W852O6t4QjJk6zxJJp1DzGvSSbwjXEoPpEd9jQfMI8C8j7uRK3VWDbhyqNXqUMt5NQsk1tkb7tkunaY5GarzDRl_FAC2j-n5b6Df5kM6KuKW0Hxfuj35Ll_Uxdjs7G_KO6YiqFd_BG0Vx6_FyRZSDXvCCSa-h_i83hMLG3fa-WuFVzFP0QB6EJFUcw2RFKIeHUwpqqUkPFQtwDjZDN_m0tCxHTiHL6rb4f_q0AiYOKnrbufGf34OJJOXog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موج دیگری از حملات پهپادی ارتش به پایگاه‌های آمریکا در کویت
روابط عمومی ارتش:
🔹
در مرحله بیست و پنجم عملیات صاعقه؛ ارتش جمهوری اسلامی ایران در پاسخ به تجاوزات دشمن سلطه جو، ساعاتی پیش، «انبار‌های تجهیزاتی ارتش تروریست آمریکا در اردوگاه العدیری، و  «محل استقرار نظامیان آمریکایی» در پادگان الدوحه و «محل استقرار نیروهای دشمن مستکبر» در اردوگاه عریفجان کویت را هدف پهپادهای انهدامی آرش قرار داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/akhbarefori/674762" target="_blank">📅 11:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674761">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1df94d94be.mp4?token=VP0zYQtYxDc2rcxXQKz9VPij0l4NVWtvSH8cKF7T-C0new4BJdIWh4oNvakH3DS1peWxbtA7X-LTohd8Ngt4bIzPvgljctw3z8V809T_4klGHabN6kOAvj1oxiQ79kdOIVCh530DZH-7XWf81joDpFnIK0lC6l4DLBvk-fQS0_FbRMBFmxo-H_iVH5n2dpq_K3VM2aQ7WRtlMsoMKfbMt9W7XSFf1PK_tnJUdF_BTEbg0DNqb0S-Jh2nzKQjoAW99m0__YuJemZ51TboiWdKQ2mmWyaGdBUK4frlQHjRaelNv29YIgjfrobgofQxQ9_Iju__JIHgs20DfenHJT6nKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1df94d94be.mp4?token=VP0zYQtYxDc2rcxXQKz9VPij0l4NVWtvSH8cKF7T-C0new4BJdIWh4oNvakH3DS1peWxbtA7X-LTohd8Ngt4bIzPvgljctw3z8V809T_4klGHabN6kOAvj1oxiQ79kdOIVCh530DZH-7XWf81joDpFnIK0lC6l4DLBvk-fQS0_FbRMBFmxo-H_iVH5n2dpq_K3VM2aQ7WRtlMsoMKfbMt9W7XSFf1PK_tnJUdF_BTEbg0DNqb0S-Jh2nzKQjoAW99m0__YuJemZ51TboiWdKQ2mmWyaGdBUK4frlQHjRaelNv29YIgjfrobgofQxQ9_Iju__JIHgs20DfenHJT6nKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هدف قرار گرفتن انبارهای کنسولگری آمریکا در اربیل
🔹
برخی منابع اعلام کردند هدف از حمله به اربیل، انبارهای کنسولگری ایالات متحده در اربیل واقع در شمال عراق بوده است.
🔹
در عین حال گزارش‌هایی از تعلیق پروازهای فرودگاه بین‌المللی اربیل خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/674761" target="_blank">📅 10:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674758">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f14b5c80fa.mp4?token=VWlGYsBFD7qD-et6W_jvFWl2ZG3rzGTSpmQDtfVuJN_FS-8UTbnjLGC4LxyH5gsQrmf1RSFeA6WRudT3jDxfOSTtPmIBD6c4yhW-fYybXQzqq-uWDviQR9dNXZgePUa3v_y6KfcCzDRJ0XAA8_eNuDeH_EZFiQOhRrZCRJy-2K9LxhMHXGA04DxDLPZKfhp5_crgXijNjVzEY9HYOYbXCDR99ptTRXr9HP4YyXgsL88iU7BRlcQan_9_1xL8uiGWtv14IsIlwDTCHm_qTyoQigN5iYC_s4RLXpgA_yPuZSUDCCWmwZuncD04o8jC38Lp3O-VQGmYVWFGeeS_BjKaKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f14b5c80fa.mp4?token=VWlGYsBFD7qD-et6W_jvFWl2ZG3rzGTSpmQDtfVuJN_FS-8UTbnjLGC4LxyH5gsQrmf1RSFeA6WRudT3jDxfOSTtPmIBD6c4yhW-fYybXQzqq-uWDviQR9dNXZgePUa3v_y6KfcCzDRJ0XAA8_eNuDeH_EZFiQOhRrZCRJy-2K9LxhMHXGA04DxDLPZKfhp5_crgXijNjVzEY9HYOYbXCDR99ptTRXr9HP4YyXgsL88iU7BRlcQan_9_1xL8uiGWtv14IsIlwDTCHm_qTyoQigN5iYC_s4RLXpgA_yPuZSUDCCWmwZuncD04o8jC38Lp3O-VQGmYVWFGeeS_BjKaKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
باستر کیتون؛ نبوغی که قرن‌ها جلوتر بود
🔹
باستر کیتون، خدایگان بدلکاری بود زیرا او این کارها را در بیش از ۱۰۰ سال پیش انجام داده است.
🔹
از اسکار ۲۰۲۷، قرار است شاخه بهترین بدلکاری هم به جوایز اضافه شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/674758" target="_blank">📅 10:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674757">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pgZHC-TUIudN-Pb7a6fYsUetre_dD91yEBdOvKkjTYpFmVB-L9y4HQ2_TIyz3BaOaIAYzjbaivkuu0RYyz6H18sviIBtvAcDnR-WA52sGRJCsmToLrIGyt9Zef4ntb3R8W2UCR12OV-qkl8jOH2M3eV1cmzsEX6VzC3KfJ1A_o7q5Z_7RTjgp_j0tw7_SuLvgu3EQmBLXnW-A19j6yDIVtiyTySTQtAxOi7k8FImC-SXbfwguY7Tw_0rwJBJmesNZaIJHaF6rYheSnzcBwL9nIh13Ii58ll5MQlfbCp6jEGyMln1K5KAsvEBpUaV3CGvWyXlU-EhWZX_7ycxqP_fCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
همه باهم برای ایران
🔹
ایران، خانه مشترک همه ماست؛ سرزمینی با فرهنگ‌ها، شهرها و لهجه‌های گوناگون که هرکدام بخشی از هویت آن را شکل داده‌اند. هر اقدام کوچک ما، از حفظ محیط زیست و مصرف بهینه انرژی تا همراهی و همدلی با هموطنان جنوبی‌مان، می‌تواند نشانه‌ای از مسئولیت و عشق به ایران باشد. شما برای ایران چه کاری انجام می‌دهید؟
🔹
همراهان گرامی خبرفوری؛ برای پیوستن به این پویش، یک پیام صوتی حداکثر ۱۵ ثانیه‌ای ارسال کنید و با نام و لهجه شهر خودتان بگویید:
«من ... هستم از ... و ایران را دوست دارم، چون ... و به خاطر ایران میخواهم...»
🔸
پیام صوتی خود را با دلیلی که باعث می‌شود ایران را دوست داشته باشید، به آیدی‌های زیر ارسال کنید
👇
#همه_باهم_برای_ایران
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/674757" target="_blank">📅 10:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674755">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf31b84ef9.mp4?token=gb1DXGCPZYnIBDwF99SU_SFS5fTyOnIFermC3o08zzOlb0r8s8wRefLOTa-51B3CllLL7JNNROL_xWdw7_ANID4vQX_SlVkQ2L92Y65en8inujjD8jE_xepY71HglAE6FvNC_llz5VZRIl-G86aaYPpqCGLuER08-8aqGpeGDXFNwAi7zMDoacA1F-oQyi7kTsK13j0nLFSXvMEzOQeC_JXud0nGwE0i-guAdpeWkcsYr0ZgAgEp5u5Z9RMm166d5HKSgOGbmGiObD9WCvg59lLcN2KYOUvSiLV7ux_v7jDEtAzP5pFnI4XTA6BD5a6qnthoVkMuxOu_FKXtuMYjkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf31b84ef9.mp4?token=gb1DXGCPZYnIBDwF99SU_SFS5fTyOnIFermC3o08zzOlb0r8s8wRefLOTa-51B3CllLL7JNNROL_xWdw7_ANID4vQX_SlVkQ2L92Y65en8inujjD8jE_xepY71HglAE6FvNC_llz5VZRIl-G86aaYPpqCGLuER08-8aqGpeGDXFNwAi7zMDoacA1F-oQyi7kTsK13j0nLFSXvMEzOQeC_JXud0nGwE0i-guAdpeWkcsYr0ZgAgEp5u5Z9RMm166d5HKSgOGbmGiObD9WCvg59lLcN2KYOUvSiLV7ux_v7jDEtAzP5pFnI4XTA6BD5a6qnthoVkMuxOu_FKXtuMYjkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بلند شدن ستون‌های دود از فرودگاه بین‌المللی اربیل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/akhbarefori/674755" target="_blank">📅 10:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674754">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abf97b1a3c.mp4?token=OOK7AkF8uEK_3OH0yJatGa9coqX6w1xnZ7xegap_hffd-jyCUEj3NWczaWc5G_RMErltfSjeSekV_dYblchUsF_pxE-2TOJ93bWUxDamB7ADrecv8uddaGlL6bnRyKWhQrcWyk04a45Q_CAemmPjlgaeV41kWgJVa-M5hLseH2hcNa5GXUhBVvFXXSoR0ceOS7IETr2nyYFzpx70oibOIQ4Ke46AUr01Gq-cmwUgHjUif_BrYXlXAYX2mzeoXM0aDk1b2Pv3xBh9ddbq4AFErG2ip23mvEd_q6mPqktaaONO03WNL7lGu0fMycx-BdbeZ_DivGFZfxBx5nAmvXxViw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abf97b1a3c.mp4?token=OOK7AkF8uEK_3OH0yJatGa9coqX6w1xnZ7xegap_hffd-jyCUEj3NWczaWc5G_RMErltfSjeSekV_dYblchUsF_pxE-2TOJ93bWUxDamB7ADrecv8uddaGlL6bnRyKWhQrcWyk04a45Q_CAemmPjlgaeV41kWgJVa-M5hLseH2hcNa5GXUhBVvFXXSoR0ceOS7IETr2nyYFzpx70oibOIQ4Ke46AUr01Gq-cmwUgHjUif_BrYXlXAYX2mzeoXM0aDk1b2Pv3xBh9ddbq4AFErG2ip23mvEd_q6mPqktaaONO03WNL7lGu0fMycx-BdbeZ_DivGFZfxBx5nAmvXxViw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماسال؛ روستایی که همسایه‌ ابرهاست
#ایران_زیبا
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/akhbarefori/674754" target="_blank">📅 10:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674751">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
حمله موشکی دشمن آمریکایی به مقر نیروی دریایی سپاه در زیباکنار
معاون سیاسی استانداری گیلان:
🔹
صبح امروز مقر نیروی دریایی سپاه در زیباکنار، هدف پرتابه های دشمن آمریکایی قرار گرفت که بر اثر آن بخشی از تجهیزات مستقر در این مجموعه آسیب دید.
🔹
تاکنون هیچ‌گونه گزارشی از تلفات انسانی دریافت نشده است
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/akhbarefori/674751" target="_blank">📅 09:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674747">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74f3118cae.mp4?token=p1Ux1bcUZ1JeUjV1lzvh8SZ2-WXT8Z1wccjBeL3ugS2qDp2mSo2sMGAnUCbL24589TNzVMgTWOlDsI-Q5297dpn5POZB0RY_ATfgBTiM41how4pmaJI3MC6aWIW0CY74BRZqGwEI_ZAh5YfFEfBrr3A8P1wAhDlRxCGl7Lq3G4FTHdzynNvwr0AyrZyIDxau-hfGCT190Y8k-OSmovHzmpWvL8DWBWNqCy8OAuxfWk5wn1vM8kNDz4de1WyXKTOXC6mV0bK-fj6_kDwRT4h7cbzhCYfSrKIdkGWvHeuXKDcGiq0UiJULtW7HIGhzTfqjpmK4coRxX29IGBS7B946QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74f3118cae.mp4?token=p1Ux1bcUZ1JeUjV1lzvh8SZ2-WXT8Z1wccjBeL3ugS2qDp2mSo2sMGAnUCbL24589TNzVMgTWOlDsI-Q5297dpn5POZB0RY_ATfgBTiM41how4pmaJI3MC6aWIW0CY74BRZqGwEI_ZAh5YfFEfBrr3A8P1wAhDlRxCGl7Lq3G4FTHdzynNvwr0AyrZyIDxau-hfGCT190Y8k-OSmovHzmpWvL8DWBWNqCy8OAuxfWk5wn1vM8kNDz4de1WyXKTOXC6mV0bK-fj6_kDwRT4h7cbzhCYfSrKIdkGWvHeuXKDcGiq0UiJULtW7HIGhzTfqjpmK4coRxX29IGBS7B946QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله پهپادی اوکراین به انبارهای لجستیک روسیه در سن‌پترزبورگ
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/akhbarefori/674747" target="_blank">📅 09:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674738">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
عراقچی: هرگونه مشارکت در تجاوز به ایران مسئولیت بین‌المللی ایجاد می‌کند/ امنیت خلیج فارس با همکاری کشورهای منطقه تأمین می‌شود، نه مداخله خارجی
🔹
آمریکا به تعهدات خود پایبند نیست و موجب اخلال در جریان عادی کشتیرانی تجاری بین‌المللی شد.
🇮🇷
✊
@AkhbareFori |…</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/akhbarefori/674738" target="_blank">📅 09:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674736">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
عراقچی: هرگونه مشارکت در تجاوز به ایران مسئولیت بین‌المللی ایجاد می‌کند/ امنیت خلیج فارس با همکاری کشورهای منطقه تأمین می‌شود، نه مداخله خارجی
🔹
آمریکا به تعهدات خود پایبند نیست و موجب اخلال در جریان عادی کشتیرانی تجاری بین‌المللی شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/akhbarefori/674736" target="_blank">📅 09:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674734">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D4n-Xn_y3jQIVl3OvxTAw0djCMcx4dDMgfIj-P05FfZd_gcDT4NuwUbV_VcAjpQSgPzaYUnAkjHNSwMdyAVX2COYoRk5H8QYxncD_ZDGZbe7EvR7dHhiG3gJvcYvtZdkoGkP1yhMX8qD8A4rCteSC4po0xXtfFfOGl-imsqSXxxKLUKPqjunoQMvSDzfYu9YoEP8SfjFY2XWQ_ibldRwsQwcniRp58LQ22FEZbVYP1WpHrAauRstJNfEp342fJeC3Br8ZIVKXxCqfBE7pwVsuTjuxM8AWLRvU_XGekua3yO3R1FHsAyJ3Gw0SE64P8IajprRrw0uH2sJ3gc8yyrlcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
علائم پنهان مسمومیت با آفتاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/akhbarefori/674734" target="_blank">📅 08:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674732">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/967e2e2884.mp4?token=HeM7H3Yq74aV-V2bZCAB5_ENYJZPppa8yM-FoBgg-A8HbHczae6DI4WrgAmaTS1rFkmA8EFxddObN3_oYuak7bPlGyRQf-EbjxL4HgZInvJlI667Hs-bmzfd1HmFnPfLeHKP0OZ3UgcF4fnisvWIgUrgGPfrZcRY8r2PDB49wYqYHpQrBnTISEZ_Xr-6XtjLqkhllhHNzIGjHMKA3Ovz_cQ4_hvGLqHC0d92GyxVZt1n73WaIssSrS8QVTT_-wg5Sbd68Sx2LD63boGN_vHkh_TAuOy4awI6FrjFwe3so7oOtyu6bopJKBJqI4ba6VhmxcTkz_wJyjQJsbwoJ5AdoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/967e2e2884.mp4?token=HeM7H3Yq74aV-V2bZCAB5_ENYJZPppa8yM-FoBgg-A8HbHczae6DI4WrgAmaTS1rFkmA8EFxddObN3_oYuak7bPlGyRQf-EbjxL4HgZInvJlI667Hs-bmzfd1HmFnPfLeHKP0OZ3UgcF4fnisvWIgUrgGPfrZcRY8r2PDB49wYqYHpQrBnTISEZ_Xr-6XtjLqkhllhHNzIGjHMKA3Ovz_cQ4_hvGLqHC0d92GyxVZt1n73WaIssSrS8QVTT_-wg5Sbd68Sx2LD63boGN_vHkh_TAuOy4awI6FrjFwe3so7oOtyu6bopJKBJqI4ba6VhmxcTkz_wJyjQJsbwoJ5AdoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرحله بیست و چهارم عملیات صاعقه ارتش؛  پایگاه‌های آمریکا در اردن و بحرین هدف حملات پهپادی ارتش
روابط عمومی ارتش:
🔹
در ادامه حملات پهپادی ارتش جمهوری اسلامی ایران و در بیست و چهارمین مرحله عملیات صاعقه، بامداد امروز، «مخازن سوخت»، «انبار و سوله‌های بزرگ تجهیزاتی» و «محل اسکان» نیروهای ارتش تروریستی آمریکا در پایگاه شیخ عیسی بحرین هدف پهپادهای انهدامی آرش قرار گرفت.
🔹
در ادامه این مرحله از عملیات صاعقه، «آشیانه هواپیماها»، «آشیانه تعمیر و نگهداری هواپیما» و «محل اسکان» مزدوران ارتش متجاوز آمریکا در پایگاه الازرق اردن نیز، هدف حملات پهپادی ارتش  قرار گرفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/akhbarefori/674732" target="_blank">📅 08:23 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674728">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
‌
رسانه‌های عربی: ناوگان پنجم نیروی دریایی آمریکا در بحرین، مورد حملۀ هوایی قرار گرفته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/akhbarefori/674728" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674723">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZOnUuMYoPNFQmmw0C7iMkX4Iet52gxpYeUgWn-AQGvOuOmpCC9zeEShs77MyFrqPOZQJ5euUXbjc7JxUjGWOtoxgku-iXdYMDeAdDaZJ14W-1pwlGxBMKcylVh82jHR9u_mWfwzunQxw8ArBsmuAkSvbqT5JriMreApM76McMaH03ID5fiEmlbtd3pCnDxOn4iMhI1AbZAzHWOM6rR2dOHi2_ZHkvGuhnnJ_DN_bYzs1tPm67dNY48J4rdsQnkr_LGXbR4KYnClvI5A6MPUxdn7w7pDqb4f9YRCWWSn2M1Pv4Rml43ayFlEoY1YPEXpiPTsEwZ8RLyYd_jkW3oTcYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این ۴ اپلیکیشن، عادت‌های دیجیتالت را متحول می‌کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/akhbarefori/674723" target="_blank">📅 07:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674721">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TYfpkt7CTTCxdtY4bOqkP5wEa5TI2UEQkBnGW9FdD_N6YYhtk0XixuYS_PXvfFioxsQEwm5foXtjpPh76i62BX2gEnvfCa_kviETE_ROma-TapNeTUX2LKZni6l1wyOKeMo86J0wyk5flsXglaqMQEbdSSakM8IynK1j2OaV8zG1f1B8JPvH9Taw3WtLtlYEaUwrr1mtYqPZoK2E-lsyovsUqD5xFSicWD5WNnCdqITWEfFhyVdIY43mWubOOdhR-sbG0UgkLoI_2pKT7mc57WmaATLJY4-1O5y7GynQO9zviRBEaWiI94DuC6B6IF_4ZGhKvrxqtDTXzdXbbg9x1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عکس یادگاری وزرای خارجه سازمان همکاری شانگهای
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/akhbarefori/674721" target="_blank">📅 07:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674720">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/njecuXOTENRUqIMaDhenqW20g6aNlclWUzyMVSkDvn5H-x1omf74AcycL83wV8U5VOsMYCM56c6vubGEeAQpMzdV2N-BaI2hgodOuQ_ckk3csh0LXFTkZxfTkEsX-YG1vqFzUH-3Zb7-L8xOg4d7sIL9_CB_akJ45UCzxW3JMxxiKxh8izAfTs45F66rN04Mw-8lRY1wpvEMReQZS4uTn0ybOSukBJL8Fl06vdjgfPwZYhVyAgsUUCyUtoOUq8iEDEt_UdCc3t80nopULxPwqeJ_dNNQqsqCYlDnFTeBRrLLEC7lY1ilIPFUJq_TJowYZrbel_gAVgOeAgGkaAl0Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز جمعه
۲ مرداد ماه
۹ صفر ۱۴۴۸
۲۴ جولای ۲۰۲۶
جمعه‌ها
#دعای_ندبه
بخوانیم
⬅️
متن و صوت دعای ندبه
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/akhbarefori/674720" target="_blank">📅 07:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674717">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qyAifeHsiUsbM4tVZbSOwAddJi6di0LkLwhi01_bg52NJydmQv4P3k9INq1yqQimfqPEF3qPUW_hawyPRjEAYdGq4BAUJyMFX2EBCSammuxVDDMOhz7xlF2AP-q57KOrJr5oW0wlCFNqWu9Z2ZeUwnDL8HsUjZkqmfBagGxAX6PqWLLEKCFqmAywNBRjkkMNRqmvqaGdUOs0abSwurDlCGmrZmSoFBYtgVwN75EfgOJWV6ebKjDtERyzqQCkbDxGl_G9gCc6C48tjz0lO47I6INXtzMSK5roEsI5kHWKX37mfMXmdwUDSXdLdr4qUM0JNwEpiJPADXKNoXDBJ2fBlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پاسخ عراقچی به تهدید جدید ترامپ: به محض اینکه دولت‌ها مصادره اموال دیگران را عادی‌سازی کنند، آنگاه دارایی‌های هیچ‌کس در امان نخواهد بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/akhbarefori/674717" target="_blank">📅 06:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674715">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a60685601.mp4?token=Gq8Km0uudhCnLyXDwcGcfNgqq5nl3gQVHKVjkANAFytTRbFcvj8s5PlO4EY1CT5h1kMQGaD7DJDoEjs2zFlTvINzdowpUY_sIlX-elJJDeHnaFPns6u6QsnLBlxuIXMzHV3yuS56lV06xE-iwQYmXvaUl6p1mbjhoz7pk9FCahFGXxKF27Tdm3pHggjI6srA4QlCsZScM23tl9wHJ2csLDS-LeJemfrCE20fX-3h-qd9Mq-YLpSf05VBmA1YBeSTGZQQ_q2gO1pwTgXqR_5fibJ6Be2N_mW0EB_5mD6rSPuSrNGYorjob_lhfcsr8Iar-S7pZTBQpwKdBPQClQtb3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a60685601.mp4?token=Gq8Km0uudhCnLyXDwcGcfNgqq5nl3gQVHKVjkANAFytTRbFcvj8s5PlO4EY1CT5h1kMQGaD7DJDoEjs2zFlTvINzdowpUY_sIlX-elJJDeHnaFPns6u6QsnLBlxuIXMzHV3yuS56lV06xE-iwQYmXvaUl6p1mbjhoz7pk9FCahFGXxKF27Tdm3pHggjI6srA4QlCsZScM23tl9wHJ2csLDS-LeJemfrCE20fX-3h-qd9Mq-YLpSf05VBmA1YBeSTGZQQ_q2gO1pwTgXqR_5fibJ6Be2N_mW0EB_5mD6rSPuSrNGYorjob_lhfcsr8Iar-S7pZTBQpwKdBPQClQtb3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی از آسمان اردن در پی حمله موشکی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/akhbarefori/674715" target="_blank">📅 06:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674713">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPvZa66GS8C65smRWFhg-zFzECkBRe89rBQ5ECR7ExEiNah3kB9m89BOZC4EwA18z0GIPFhZ_-7E7ltuDTyNlRj86qyS_R6mVZZ9VeyH48WM3EkW9I9uKbpvnSgT3MWklS5-qeqC1lVBiCRc3j67leO9ypyF57lthY4gGaDHsbY-bxj6VNsvapFSNkDeZDLdYId3rH_gR6MXvEgyrxOlw8ExAce3zpfS2eAA8Qa8mY_gfYTPtM7hm7RaEJ-ScoV9425Z5ttMjcApPISC-5r4PqYKwSjXeHcJJhveora6ywEXfj_wDW9UePGmN1qL_bKX7PMrxlh_gJ6JMfe5yS7UNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش صفحه سفارت ایران در کوبا به تهدیدهای ترامپ با انتشار تصویر توئیت‌های او برروی دستمال توالت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/akhbarefori/674713" target="_blank">📅 06:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674709">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
۴ شهید و ۵ مجروح در حمله موشکی ‌آمریکا به اطراف شهر اهواز
استانداری خوزستان:
🔹
پس از حمله موشکی دشمن تروریستی آمریکا به نقاطی در اطراف شهر اهواز ۴ نفر از هموطنانمان شهید و ۵ نفر دیگر مجروح‌ شدند.
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/akhbarefori/674709" target="_blank">📅 06:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674703">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97864911be.mp4?token=UiPrMQWYU32R6y1nKh41S2mLEZIvq21hpZfNCB6UOwD5ftfipGbZXlbBQY_ktFrKIkiEPqKQYz7DeDqzUGxUE4k3QnkMyPU8UiA2HOTZubfynTyn-C0NvoeaYq8SoFOvjUXEGIZa-lfrzUgYNL_BC9bsFGDIhaZc_PUb45Z3ZtwXFwsCQTIChyFMkOUe8Qql75sxX_LkxcwFDlPrK7Z3upcZVZkH8MTZVjcYuKTGyrQVLV1rn4CycVrR0piUkuXZwv9ZdtKCLrVz2DVTIBCQdoZNiqmfzVwZbXU4zvprGwG5D-Fmp-nrioVVAnYqgfQxAy2s8ZHWL_iwueSq1pDqaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97864911be.mp4?token=UiPrMQWYU32R6y1nKh41S2mLEZIvq21hpZfNCB6UOwD5ftfipGbZXlbBQY_ktFrKIkiEPqKQYz7DeDqzUGxUE4k3QnkMyPU8UiA2HOTZubfynTyn-C0NvoeaYq8SoFOvjUXEGIZa-lfrzUgYNL_BC9bsFGDIhaZc_PUb45Z3ZtwXFwsCQTIChyFMkOUe8Qql75sxX_LkxcwFDlPrK7Z3upcZVZkH8MTZVjcYuKTGyrQVLV1rn4CycVrR0piUkuXZwv9ZdtKCLrVz2DVTIBCQdoZNiqmfzVwZbXU4zvprGwG5D-Fmp-nrioVVAnYqgfQxAy2s8ZHWL_iwueSq1pDqaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیوی منتشر شده در رسانه های اجتماعی، لحظه برخاستن هواپیمای آب نشین غول پیکر روسی Be-۲۰۰ با وزن ۴۰ تن پس از پیمودن مسافتی بر سطح آب را نشان می دهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/akhbarefori/674703" target="_blank">📅 05:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674702">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bB_PnBtp13A-uuCEJHAvYBRISiBCgOVBYVj435345fh3TclgPJf6oTnanL76Uqj_g-tqhgNSYU0jdPSPcLUfEiUrEQ38yO8BEkYNt-4jS4ZwOxQEsn4jnYVjuOYxdWNdLzDPZGidbCXGyA5-DXd6ZRP7HQBvz_iM9SyN2SD37uEByZ1K6WtkIl6Ak6Xv7pP7RE4XcGJEJSEI-b93FF1PD4VqsQ20hod7FQkQcTdgWSSJ3T5Tzukrf6_bQWEbGDN8wLYKgeGx3Lqs9IeM2_hCuLVqtCaBNfTqszv_Tx56UvSk7B82ACu6sqVriyCTUI_cdus_0MLUtyureaGePIs6_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرماندهی مرکزی ارتش تروریستی آمریکا (سنتکام) ادعا کرد که راس ساعت ۹ شب به وقت شرق آمریکا (۴:۳۰ بامداد به وقت ایران) به سیزدهمین شب حملات تجاوزکارانه خود به ایران خاتمه داده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/akhbarefori/674702" target="_blank">📅 05:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674699">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
آخرین گزارش ها از شنیده شدن صدای انفجار در برخی مناطق کشور
‌
🔹
بر‌اساس گزارش‌های اولیه و تأییدنشده دریافتی از برخی استان‌های کشور، بینف ساعت ۳:۱۵ تا ۳:۴۰ بامداد صدای انفجار در چند نقطه از کشور شنیده شده است.
🔹
بر اساس این گزارش‌ها، شنیده شدن صدای انفجار در مناطقی از خنداب، ‌‌تفت و شیرکوه در استان یزد، انارک شهرستان نایین، بروجرد، جاسک و کنارک گزارش شده است./تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/akhbarefori/674699" target="_blank">📅 04:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674696">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
فعالیت پدافند هوایی در شرق تهران برای مقابله با اهداف متخاصم/مهر
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/akhbarefori/674696" target="_blank">📅 04:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674694">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
فعالیت پدافند هوایی در شرق تهران برای مقابله با اهداف متخاصم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/akhbarefori/674694" target="_blank">📅 03:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674689">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
روزن روزنامه‌نگار آمریکایی: درباره اینکه شیطان زرد ظاهراً در حال افزودن شروط جدیدی به توافق هسته‌ای آمریکا و عربستان، از جمله عادی‌سازی روابط عربستان و اسرائیل است، یک منبع سعودی گفت: این توافق امضا شده است. بنابراین چیزی برای مذاکره دوباره وجود ندارد
🔹
او افزود؛ توییت‌ها توافق‌های امضاشده را لغو نمی‌کنند
🔹
از او پرسیدم: آیا عربستان در متن توافق یا پیوست‌های آن پذیرفته است که در مقطعی در آینده روابط خود را با اسرائیل عادی کند؟
🔹
منبع سعودی پاسخ داد: «نه.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/akhbarefori/674689" target="_blank">📅 03:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674687">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
ادعای نیویورک تایمز: ایران روز پنج‌شنبه پیشنهاد آتش‌بس رئیس‌جمهور ترامپ را که توسط نخست‌وزیر عراق به تهران منتقل شده بود، رد کرد؛ این موضوع به گفته مقام‌های ایرانی و عراقی مطرح شده است
🔹
این مقام‌ها که به دلیل صحبت درباره مسائل حساس امنیت ملی نخواستند نامشان فاش شود، گفتند سفر علی الزیدی، نخست‌وزیر عراق به ایران پس از دیدار اخیر او با ترامپ در کاخ سفید انجام شده بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/akhbarefori/674687" target="_blank">📅 03:19 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674685">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
حمله ارتش متجاوز آمریکا به تپه‌الله‌اکبر بندرعباس/ تاکنون دو نفر مجروح شدند
معاون سیاسی، امنیتی و اجتماعی استاندار هرمزگان از حمله دقایقی پیش ارتش آمریکا به تپه‌الله‌اکبر بندرعباس خبر داد:
🔹
تاکنون دو نفر در این حمله مجروح شده‌اند و دستگاه‌های امدادی و خدمات‌رسان در محل حادثه حضور دارند.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/akhbarefori/674685" target="_blank">📅 03:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674678">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P8_gX7IlCbySBPh8e5pTjmqgtvPWoM_O8rsZSHUVuqXD8D1gL6m6sBgvudlZxggBgWhBmEbrhfv8TZJpZ1x9SROAiptQJ-9VNlEZsK2AHVCfvmWZbNPe1fG6cIEyCXpe2NnzTRVLjn6nRx8WAwsN-kz9E-VR2CziYGgAw3UOgy4fbo4cgs07rH6Q6mgDZEK9Ejex524oRPyIo-exps7PPbuzgYByOF59Jvqc-ImbPH9QMkWZQ5FQL4U2yY6Cr8bdBIU4OKjWQU9jypCOzUMPR3jz6NpNKRqUxCZzEUbaMH7fS93Ce3o_wqgbdPwmL8STR69pBgP3hG_PF-_VkS7mNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یوسف پزشکیان: ‏چه کسی در صدا وسیما تشخیص می‌دهد که چه بخشی از سخنان رؤسای قوا نباید پخش شود؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/akhbarefori/674678" target="_blank">📅 02:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674677">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
عراقچی: اروپایی‌ها را به دلیل مواضعشان برای مراسم تشییع دعوت نکردیم
🔹
کشورهای منطقه در حال تنظیم خودشان با قدرت ایران هستند؛ قالیباف از وقتی نماینده ویژه چین شده به این کشور سفر نکرده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/akhbarefori/674677" target="_blank">📅 02:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674676">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
عراقچی: عراقی‌ها استقبال عجیب غریبی از من کردند
🔹
عراقی‌ها من را قهرمان خطاب کردند صداوسیما سانسور کرد و پخش نکرد؛ برخی به ما شعار مرگ بر سازشگر می‌دهند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/akhbarefori/674676" target="_blank">📅 02:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674673">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
عراقچی: توافق بر رهبری تحمیل نشد
🔹
هرجا رهبری اصرار داشتند؛ ما پذیرفتیم و هرجا رهبری بعد از توضیحات ما، متن را اصلاح کردند، ما مسیر جدید را جایگزین کردیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/akhbarefori/674673" target="_blank">📅 02:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674672">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
المیادین از حمله مقاومت عراق به مقر نیروی زمینی کویت خبر داد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/akhbarefori/674672" target="_blank">📅 02:19 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674671">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
عراقچی: توافق با آمریکا بهترین توافق ممکن بود
🔹
اما وفاق ملی درباره آن شکل نگرفت
🔹
مردم کف میدان را با دروغ ناامید کردند و گاهی فکر می‌کنم اسرائیل در چنین روندی نفوذ دارد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/akhbarefori/674671" target="_blank">📅 02:18 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674668">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
رسانه‌های عربی: در تصاویر به‌نظر می‌رسد یک پرندۀ ناشناس پس از اصابت در آسمان جزیرۀ قشم، درحال سقوط است @AkhbareFori</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/akhbarefori/674668" target="_blank">📅 02:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674667">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
المیادین از حمله مقاومت عراق به مقر نیروی زمینی کویت خبر داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/akhbarefori/674667" target="_blank">📅 02:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674666">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8d8c129d3.mp4?token=P7_rrIg6Lkp9V4c2K3SLom-UdVaZILctkugW3ix_aVZOQMPUQNsItThkJFOiOi6ySAcv9WeoUbc26vGvUXoGTqvMV2QAmwSngUEf3-B7Uw5jBPZG0IzjWcybLdLLSLvVaXc2LWkq3fp9sugBFz6GvsqhPdIST-Ud8GJZuA_62hDJjuS35jgjI_tKECi92nGGqsi8sElEpFD4pdhdAg0pvyqa7g_rrye4FY3EhNw1y9Nx1bJXpVBxa9GB4K3Nvba-VCGxJIqSTeGFyK46xWsiaS0bxZniAG5fUgGOUgisbjEPHMApNQbAxawACTZJ_fvapdRHqZhqbB3KentH8iuEwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8d8c129d3.mp4?token=P7_rrIg6Lkp9V4c2K3SLom-UdVaZILctkugW3ix_aVZOQMPUQNsItThkJFOiOi6ySAcv9WeoUbc26vGvUXoGTqvMV2QAmwSngUEf3-B7Uw5jBPZG0IzjWcybLdLLSLvVaXc2LWkq3fp9sugBFz6GvsqhPdIST-Ud8GJZuA_62hDJjuS35jgjI_tKECi92nGGqsi8sElEpFD4pdhdAg0pvyqa7g_rrye4FY3EhNw1y9Nx1bJXpVBxa9GB4K3Nvba-VCGxJIqSTeGFyK46xWsiaS0bxZniAG5fUgGOUgisbjEPHMApNQbAxawACTZJ_fvapdRHqZhqbB3KentH8iuEwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رسانه‌های عربی: در تصاویر به‌نظر می‌رسد یک پرندۀ ناشناس پس از اصابت در آسمان جزیرۀ قشم، درحال سقوط است
@AkhbareFori</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/akhbarefori/674666" target="_blank">📅 02:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674665">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XkYquZy4w38TIjfZywm5VWJnOWEl5NtE3SKRS9gy_cwB_6qhU0yuIdBjSO0d8P2ly_x3pNeJz5mIPIuLH5dEDdKtgOWMpadZybvmGSAKdquUEKXDiGO5Pu9Ph0F58HwiiyqnwKoRFzU__yknuI-fk3AdHiH-xkRRE_yUd1Lrr5PabhY0060m_QNH6TSeha8WI2srY8cST1twH_dFkunYH0Jdrl17y3sK2hUfBdt6zCqScrqye0aYuiMGG79VPW53MKSUXAx0AgqBfxhnCSg2bdYambTO0mwwjBx8JNyx7x1FAOVtvAll0yPKpyEnoYFO7KPkBmW89wHU6S7GezIRxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای خوک زرد:  تا اطلاع ثانوی، از این پس، هر گونه خسارت وارده به کشتی‌ها، محموله‌ها، یا هر آنچه که مرتبط با آنهاست، از پول‌های ایران که در اختیار و تحت کنترل ایالات متحده است، پرداخت خواهد شد/ این خسارات ممکن است بسیار قابل‌توجه باشند، اما با این حال، این کار منصفانه و عادلانه است
@AkhbareFori</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/akhbarefori/674665" target="_blank">📅 01:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674664">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
نگرانی اسرائیل از سرعت ایران در بازسازی زیرساخت‌های آسیب‌دیده
وال‌استریت‌ژورنال:
🔹
سرعت چشمگیر ایران در ترمیم سریع پایگاه‌های موشکی، پل‌ها و مراکز تولیدی آسیب‌دیده از حملات آمریکا و اسرائیل، مقامات صهیونیست را غافلگیر کرده است.
🔹
این بازسازی‌های سریع که در تصاویر ماهواره‌ای مشهود است، ادعای سران آمریکا و اسرائیل درباره «وارد کردن ضربات ویرانگر» به توان زیرساختی ایران را به چالش کشیده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/akhbarefori/674664" target="_blank">📅 01:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674663">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75012b9b40.mp4?token=TyMF66aeMZYBq2C3SPGK6jE62QtfyEERvnEI62mN4x5fxoScihW4629HIOB8ERqpO3xXsvGyBxetPAYL56hPA4MjlLSMf2yJFZHu9Rf9AUjqVR2C85DNE2VIMDSH34a70Yped1FCIVTJi9IqYv-FTPvsuXzudBU_rsvdbo9lV8r_pqhI6nO5znwaQ_MkO90UDN4B9VELvbS-WCwKAgYjU1wmHFGXC1Q6hjbmGVoxrjivWpOPc7nTA6pkWUJYgXe8BGW3nQRDx5d2n3ggMQtX5uvGet-xxRfS2eeI-BlXYq3x8P9gLdQgfAb7WntCP7dQvMNC0YAwFZ9sCjRFMFur6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75012b9b40.mp4?token=TyMF66aeMZYBq2C3SPGK6jE62QtfyEERvnEI62mN4x5fxoScihW4629HIOB8ERqpO3xXsvGyBxetPAYL56hPA4MjlLSMf2yJFZHu9Rf9AUjqVR2C85DNE2VIMDSH34a70Yped1FCIVTJi9IqYv-FTPvsuXzudBU_rsvdbo9lV8r_pqhI6nO5znwaQ_MkO90UDN4B9VELvbS-WCwKAgYjU1wmHFGXC1Q6hjbmGVoxrjivWpOPc7nTA6pkWUJYgXe8BGW3nQRDx5d2n3ggMQtX5uvGet-xxRfS2eeI-BlXYq3x8P9gLdQgfAb7WntCP7dQvMNC0YAwFZ9sCjRFMFur6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«اى كسانى كه ايمان آورده‏ايد، اگر خدا را يارى كنيد، شما را يارى مى‏كند و پاهايتان را استوار مى‏كند».</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/akhbarefori/674663" target="_blank">📅 01:33 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674662">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
حمله به مقر فرماندهی نیروی زمینی کویت
المیادین:
🔹
گروه‌های مقاومت در واکنش به حمله به گذرگاه شلمچه، به ساختمان فرماندهی نیروی زمینی کویت حمله کردند که منجر به خسارات سنگین شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/akhbarefori/674662" target="_blank">📅 01:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674661">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
تحریم‌های ایران به لایحه تحریم‌های روسیه افزوده می‌شود
جان تون، رهبر اکثریت سنا:
🔹
در پی درخواست دونالد ترامپ، توافق بر سر افزودن بندهای تحریمی ایران به لایحه دوجانبه تحریم‌های روسیه در سنا نزدیک است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/akhbarefori/674661" target="_blank">📅 01:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674660">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c423ce9cbd.mp4?token=QzGKMXbiSvrXIJum_OWsA7loNJXUmGNIHS9A73Iutc3aFIHqEy26i3OCKAdgyzmopIjGuRlH89ES7QTe9DODGWVoVD-Wf_sFtpkODiAE3QmcRxbFsMNqoVF4lMvvH6kvjk7c9Iwir_FoX_sKPJIYlJIqDrXzDtug4l0ghNHyu3V2dmogm_QJ3hszqDxLInJact8h_7JIXTW1FNM2XjsyNGfgKAw90H6NgUfi0h9px6lLqPJRYcadHCQ0wjcPnci9yMjF0OWRULOou0C7mlKDxdYTdB2HJ7yYgEZeNxQIjkC39tkSnSZDgzIjdHmmVWMCryrIo0k-vgw9oM5chtvk0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c423ce9cbd.mp4?token=QzGKMXbiSvrXIJum_OWsA7loNJXUmGNIHS9A73Iutc3aFIHqEy26i3OCKAdgyzmopIjGuRlH89ES7QTe9DODGWVoVD-Wf_sFtpkODiAE3QmcRxbFsMNqoVF4lMvvH6kvjk7c9Iwir_FoX_sKPJIYlJIqDrXzDtug4l0ghNHyu3V2dmogm_QJ3hszqDxLInJact8h_7JIXTW1FNM2XjsyNGfgKAw90H6NgUfi0h9px6lLqPJRYcadHCQ0wjcPnci9yMjF0OWRULOou0C7mlKDxdYTdB2HJ7yYgEZeNxQIjkC39tkSnSZDgzIjdHmmVWMCryrIo0k-vgw9oM5chtvk0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سگ‌زرد: نفت ونزوئلا حق مسلم ماست
🔹
ما به لطف ونزوئلا پول زیادی به‌دست می‌آوریم. حق مسلم ماست که این را داشته باشیم.
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/akhbarefori/674660" target="_blank">📅 01:19 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674658">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">عبور موشک‌های ایرانی از پدافند آمریکا در اردن
نیویورک‌پست:
🔹
در حمله‌ای که در روز چهارشنبه اتفاق افتاده موشک‌های ایرانی با عبور از پدافند آمریکا، به انبار تسلیحاتی در نزدیکی همان پایگاهی که سه نظامی آمریکایی در آن کشته شده بودند اصابت کرد.
🔹
این حمله پس از ایجاد انفجار، باعث شکل‌گیری یک «ابر قارچی‌شکل» شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/akhbarefori/674658" target="_blank">📅 01:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674657">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQF0ckhRDWLJ4mEIJbyG0JwddLI4-arw3SRSIzRn6sL_B3KqqAbLjjK0VoNbermbaXAgjPwjJMqxlfJ-UtP_HaqrUcyqzSBX0_lGpWJsLstj8zO-qzwpJ60pCdgfoGtVo8IhWqYfW9YNnm61-xLBKQjM4N4c7FaMYziW6xqvW1ttlh7ZGFUdLmMnl_Z2V0gBPR_09ZOD96IgoUTnbDlkbxB6H3yieYAX-IU2eFIp5pNanGdlmYoihZrIGJJB9RSb4Dkux1OV2fBzwGxEE8CQ4ztFeZAECEp9JmGoWycrZJtgk2APRu7o5p9FjCxVlWLmGe1YASVMREYe-l8pVdjDDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انهدام موشک آمریکایی در آسمان کهنوج کرمان
فرماندۀ سپاه کهنوج:
🔹
یک فروند موشک کروز آمریکایی در آسمان این شهرستان رهگیری و منهدم شد.
#اخبار_کرمان
در فضای مجازی
👇
@kerman_news</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/akhbarefori/674657" target="_blank">📅 00:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674654">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
اقدام معنادار قالیباف در ديدار با الزیدی
🔹
ادای احترام نخست وزیر عراق به رهبر شهیدانقلاب و شهیدان سلیمانی و ابومهدی مهندس
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/akhbarefori/674654" target="_blank">📅 00:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674653">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
عضو انصارالله: عربستان برای رهایی از تبعات محاصره یمن باید غرامت بدهد.
🔹
۱۰ سرباز آمریکایی مجروح از حملات ایران به آلمان منتقل شدند/ پنتاگون جراحات را خفیف گفته بود.
🔹
دادگستری اصفهان شایعه اجرای حکم اعدام ۲ متهم را تکذیب کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/akhbarefori/674653" target="_blank">📅 00:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674652">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
منوچهر متکی، نماینده مجلس: نامه‌های احضاریه ترامپ و نتانیاهو به کاخ سفید رفته است
🔹
آنجا امضا گرفته و از طریق کانال بین‌المللی به قوه قضاییه برگشته است.
🔹
اگر در دادگاه حاضر نشوند؛ حکم غیابی قصاص برای ترامپ صادر خواهد شد؛ صدور حکم، تنظیمات آنها را به هم خواهد زد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/akhbarefori/674652" target="_blank">📅 00:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674647">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qIpd2FRPgG6FdAbbf8NPy5DhxxNX8oqwwSyj1vQdLKh87AOqkA_6Y0q040pSbe6WPCNU7YemyCXmiEiKZFNve7MSFkHDujWqnDoIWLrNWqvUfhbfz9DysEQpNeJVJcEgT81OTBzMTXMsizeTAGF6ekYzoWmiDE27USh_KTbb8jjwDTqHtVMSXSNtfqiZI-Uf84SS10V60MuQ40AiK8uysnZLCFI6gByqfseIluYAHwnIBAK6EfqbN2z1eV_20ueO6dyxXhUsgTg-31x4B7cpG0aE05rgClvXjVauUh8eys6Zo1dhTwdkOcsHjb-Q1RfDqhjF4OpHrW7yUf_yyBNhUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/674647" target="_blank">📅 00:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674646">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
خوک هار: درصورت ادامه محاصره دریایی توسط انصارالله، ایران و یمن مجازات نظامی سختی در پیش دارند  ترامپ:
🔹
یک سال پیش، ایالات متحده آمریکا به شدت به حوثی‌ها به دلیل دخالتشان در تجارت و بازرگانی از طریق هدف قرار دادن کشتی‌ها، حمله کرد. از آن زمان و در طول درگیری…</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/akhbarefori/674646" target="_blank">📅 23:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674645">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ewdOsZyF3R2DFSLHAYfWFc0Vn94F2Jat7PtSDlTlCWcq3gtIxG08rnWIYHQeF5gZeZouZDj3BDfRrg7zzpJyoksVf02gSKcV6aKhoZKXMjm4gfzsFZ8H2jR_PSgQ6YjpE_FUdYCwjyTSFA2SdtJo8FzqAMejo5hVpZf5I558IakizkzktrTLtxhkHPdXzc3Oj7CZq8fPVndiMeiBpU-wAEec1KOr2mFTmn-TlNyZAYNOyDAw8HPl9-MVyLpq89iL283WA7ScxcZ6TUtFIWcghG8Od0Uj4VSBNMPn_y07Tou05fwnrHIOgJ_CcT4mmQYP0ixvqWlVhH8ZulkSqRWQ7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پایگاه آمریکایی علی‌السالم در کویت یکی از اصلی‌ترین پایگاه‌های ارتش تروریستی آمریکا هدف حملات موشکی و پهپادی ایران قرار گرفت
🔹
ارتش کویت ادعای مقابله پدافند هوایی (آمریکایی) با این حملات را مطرح کرده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/akhbarefori/674645" target="_blank">📅 23:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674644">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArydlgHu2-6Bc0JRdVWee2YCwirc5u9YNZ--9Ude5B411NMl4GpnK_cZ1PU42TLzf6FATutm9OWqcliChiFVqd1_JuuoRNePWXIaz8R96Vm7oTP2320TgX68NZkvrOFERhSFDoRzPPQ_XCURaDkLbqpKp-hVPekmWn6skd9Rx_F4gZz_k3XcL3c0HKhGr8RMFve80Aj8bp49cR9V55LxqJxsVRBs-b0zEjHIrJU_fXu64qHy1sZERjASGjvTvzoWeAzNLbWpT64FHZBsUJzJLqwkFeLzRS2j4VxHLe_ryy5f9vtq6Hb_TLkpFn14kU0Hm3SPhwqyzPQks35ktMbVPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ارتش آمریکا موشک‌های پاتریوت قدیمی می‌خرد
🔹
ارتش آمریکا برای اولین بار پس از چند دهه، موشک‌های پاتریوت PAC-2 را خریداری کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/akhbarefori/674644" target="_blank">📅 23:32 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-674643">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-text">🎦
سفر از آگاهی شروع میشه
🔹
قبل از آغاز سفر اربعین، از آخرین وضعیت جاده‌ها باخبر شو. ترافیک، انسداد مسیرها، محدودیت‌های تردد و حوادث جاده‌ای را در
سامانه ۱۴۱
به‌صورت لحظه‌ای دنبال کن تا با آگاهی بیشتر، بهترین تصمیم را برای سفرت بگیری.
🔹
کافیه وارد
سایت یا برنامه کاربردی ۱۴۱
بشی و از بخش
«اخبار»
، آخرین اطلاعات جاده‌ها را به‌صورت متنی و صوتی مشاهده کنی.
🔹
برای اینکه از وضعیت لحظه‌ای جاده باخبر بشی، بیا ۱۴۱
#اربعین
#سامانه_۱۴۱
#بیا_۱۴۱
#وضعیت_جاده
#سفر_ایمن
#چشم_به_راهیم
#اربعین_حسینی
#سازمان_راهداری_و_حمل_و_نقل_جاده_ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/akhbarefori/674643" target="_blank">📅 23:30 · 01 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
