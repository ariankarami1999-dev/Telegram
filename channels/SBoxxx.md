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
<img src="https://cdn4.telesco.pe/file/du6gIwcWbp3FYkPm2DLHZUxHKEEH7LOJfG1PgsUtVC7_DxQ4qDZkbe4HCJqzIoOdG8jcEGI_eBxhO-FkYAXpUl15YxAEZr6rErw5K7Xu_FXn6Q849ao9rrjdvr7XQPIYX1dpucucioUAMv7rpKTiYjZxcMgDU2qE8WKgXObvRPB0MbpBH-GzeVLHG5VjjrSRy5jzN6Vu3GESAlMHnU8SCRVtw1b1hsHn_LugKQLe8ZgjU51S1Cd0WjdJwZpB_u-7QQyAesS83P5GyFvWyMnlWmGsHOB8m0bqbp_5cGbYcu6G5hX0rhmjJsKwcuVlQRVBbwQLXpyKGpNBsLJW_lcpJA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.8K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-25 18:42:55</div>
<hr>

<div class="tg-post" id="msg-20931">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6727faabd4.mp4?token=l2v-gJPrMw9cQ9pYHMwq2fsTGpEQ0PHBnGxkdkkeQ86vCbBTox5TchO7s8hEERbK1cwj5fqm8gwvGwDjBfYUl0KVXWLxmBMJmIh4E0ahmQvlBa86WEgw5Oaq9T3pdk6ySj2lyFbTcoVtZ5d_-mE2KZ8WVxN_AuIrsQ4gIsqPJtvk2-snHNcSLILrSFAZehZZZ4hWUTDaxpoZ0JfXlpsXj7d6EvCNEBxbh6CXPmQ-mfmV3_o4Tochor0o3Gbt7-cvhouKJyLqfgbQt9HR4v7X8lImXbjQ6Uahv9U-xRVF63nk4b-n2JI5zINRNZVOWYrHshILrafIqTodIu5JZdtxEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6727faabd4.mp4?token=l2v-gJPrMw9cQ9pYHMwq2fsTGpEQ0PHBnGxkdkkeQ86vCbBTox5TchO7s8hEERbK1cwj5fqm8gwvGwDjBfYUl0KVXWLxmBMJmIh4E0ahmQvlBa86WEgw5Oaq9T3pdk6ySj2lyFbTcoVtZ5d_-mE2KZ8WVxN_AuIrsQ4gIsqPJtvk2-snHNcSLILrSFAZehZZZ4hWUTDaxpoZ0JfXlpsXj7d6EvCNEBxbh6CXPmQ-mfmV3_o4Tochor0o3Gbt7-cvhouKJyLqfgbQt9HR4v7X8lImXbjQ6Uahv9U-xRVF63nk4b-n2JI5zINRNZVOWYrHshILrafIqTodIu5JZdtxEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تایید شد</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/SBoxxx/20931" target="_blank">📅 18:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20930">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZyzU7hzl6CvUfdFjXEeDnWrsHXXKbXlDiezHU2wNGXDtZYnPezxK8ij2xbwqBeItXYAQc32VgOUM0P930ysUcESCX2PPs8asrrz7bF0l0TW1j-Xw0RoGkpuU5xAmhPPRn03sojC5du-Xsnkql-jUEwdqwgWar1IW-H-0is114PELgUP_aGORCr0YWBxCpQM6PURGhs5VavaFTvoPXFq52fin_UtkYWriuQUZYB5QhKvAEiEVOieWXGbXyfa1u04bRnFnhfNOaD0rOHoyZwS9P-fVg0SK_cOsihHTiahTJR3YQIpSfOwbfGDrAF1X3n3raG-nYNgs6mhRlXkFSi8sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یحیی سریع سخن‌گوی نیروهای مسلح یمن در بیانیه‌ای از انهدام یک‌فروند جنگنده F-15SA متعلق به عربستان سعودی در حین انجام عملیات بر فراز آسمان استان مارب خبر داد.</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/SBoxxx/20930" target="_blank">📅 17:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20929">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VevfXrQs0WNygxejkG-kOKdRTt6fyY6GHkWQV0e1DmVhu_21zTJzceW2mpWwkBD8CTHDTnvfVuWy4ycrx739DJX9gpEp0SHY-nl6SSPdXRHAKF6UJ3SMYtlEFz05zhAhjRShqcQuLJ63miesfNbzFaxMmKmNCt7DEyRu6ORLk4SJ7M1f2lH8bow6Yi3x7Hqt5a-jejl14JUIBovF7i1k7hBYqe5jiBhS7BpaX4LaiJiCwN9mRNKhixIHM1CD9DWZP7FoolQqZtjQJTc5zZEpv1YE5_bzckYdoIfaZe0CSGrR_pldxX3cgmjpSLv597vtTKp_Gy_9IL3jdpMm2uJW9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی در سطح بالایی قرار دارد و نظر به رشد طلا از این محدوده (4340) انتظار افت داریم دستکم تا 4300</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SBoxxx/20929" target="_blank">📅 11:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20928">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQKuuc-KCzcnrOT75v4mvgKN0t2QraSHIYL3hPDA-Q5TVADvV1TBKTb2qKk2hrRfPRnUoSJDzdPO-QY0ECHzSjQ-DTKQNCtKIgipCYNavJLUsdk5guWv-P2yJB7LID911tGReq9mkM8RyK2CS46NO3OQLpWvcPagPJhGnYQGbmyDYb42SX9SCOS7KnCCF7ONAnmgxtlmp5FkIRvxydVq1Vf_6b41mlfEmcwR4a3D4tksMYJvcWZBZdZdplQ88jIl9CSZarJkveMUT-e3-Rq5T7izD51bcphFGAk8Lp1_kbzMK7DoN92jhYLHYnmOTZVmZcNohGZoaw64hc3h664FyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
جنگ هرمز و باب‌المندب؛ آیا ایران در حال فرسایش مالی دولت‌های غربی است؟  اختلال در تنگه هرمز و افزایش فشار بر باب‌المندب می‌تواند با بالا نگه داشتن قیمت انرژی، تورم و نرخ بهره را تشدید کرده و هزینه تأمین مالی دولت‌های غربی را افزایش دهد؛ در نتیجه، جنگ از…</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SBoxxx/20928" target="_blank">📅 10:07 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20927">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c861857ae0.mp4?token=ii3gLb6kqaV1-t1TP3U0d5tuIn6dSml_VGGRHaR7t3_ftTO3_4bjTTIkCuQhBXobE-H-785HDehdbCaPqJuDpkTMtg50JjUy56Fv1ShV3LcSbRBCkukuujzdKL1hXjQNjS43K_kUupvsNNWgJ3ZOhEuIxESWorEC1P0QmZEAwced8ZlW2aYYJnt4Dx0T-QSX1HYgyfgM07OzHMqEh1Und3GzjKgq7HKcmLJtCi-4pwzzpGXYGXB7ERncXsw25A0XokNyPf0DAYli-joRFdN747G1z9x_JjnoeJLiXRq49_iy81TeT-EANa3u6AonJWTuOAAEf7H3XDwZ1lxKCD6yfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c861857ae0.mp4?token=ii3gLb6kqaV1-t1TP3U0d5tuIn6dSml_VGGRHaR7t3_ftTO3_4bjTTIkCuQhBXobE-H-785HDehdbCaPqJuDpkTMtg50JjUy56Fv1ShV3LcSbRBCkukuujzdKL1hXjQNjS43K_kUupvsNNWgJ3ZOhEuIxESWorEC1P0QmZEAwced8ZlW2aYYJnt4Dx0T-QSX1HYgyfgM07OzHMqEh1Und3GzjKgq7HKcmLJtCi-4pwzzpGXYGXB7ERncXsw25A0XokNyPf0DAYli-joRFdN747G1z9x_JjnoeJLiXRq49_iy81TeT-EANa3u6AonJWTuOAAEf7H3XDwZ1lxKCD6yfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حوثی ها دیدند هر کار می‌کنند این عثمانی و فاکستان برای دفاع از عربستان در قالب پیمان دفاع مشترک مکه تحریک نمیشوند این بار خود مکه را زدند!</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SBoxxx/20927" target="_blank">📅 09:22 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20926">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">یحیی سریع سخن‌گوی نیروهای مسلح یمن در بیانیه‌ای از انهدام یک‌فروند جنگنده F-15SA متعلق به عربستان سعودی در حین انجام عملیات بر فراز آسمان استان مارب خبر داد.</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SBoxxx/20926" target="_blank">📅 09:19 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20925">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SBoxxx/20925" target="_blank">📅 09:19 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20924">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vMvtSu8uuA7cuwGxvDSKbLsZM7LxiEDLkmbpXsau37mEurrKtt9LPqpFD9oDd6mszIji3E5kQIIOF-0fDOvq8iOzcEaNmP9-cPpgfIzU1yoex5m8RkAPTiX0q8b-RbbVsyah_laq_QWzcobPq0yucZQ0Kw-UnXjK20nGbJ83nqM2ChpjWaHwZubsDzt1f2QMyCSRvgtzA81z8GevaEqAtlDQCHPDnRD9F30gMAfgPBIxbiN5pU9n1ocEjK9qMNJE9yQbEc7SEmzh4_GlqPobokzmNENJjVGojwTQIOluUaJW53H040Gz3Vqm0o02btadmglHNVhhP23QIEHikOj8Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشتر گفته بودم در عصر اقتصاد دانش بنیان و هوش مصنوعی، تنگه بندی و راهزنی شاید در کوتاه مدت نتیجه بدهد اما در درازمدت نتیجه عکس خواهدداشت.  (به پست ریپلای شده که حدود ۲ سال پیش منتشر شده نگاه کنید)  اکنون این ویدیو را ببینید و دریابید که چطور بسته شدن باب…</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SBoxxx/20924" target="_blank">📅 01:38 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20923">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oqMHN51fYgxKmLB06ZA6T9JG7iaktaVJC4tzOZCNJxNCcB41YDr--4RoQpM5WoeCjO9evfH0SyDWZq4QhT0Bk0G9sLP9bctWaGpMQprrgKjNPxTPhcG_VBrXq1iswbOG65qf6Nr8hL7PX7cf5BwQrAoytmqq53cfhwGKru82FHD1F9rnswkZLA-WQhtuqPpZFk9cvf3Cg_9fYIUODRJ8h2NgNKpOsq563V1XlgmWZ1c9XZLZ9OX7AiuFFVYf9UxZWVNlZz6rjyQ_eSKYgNlQYBErJnRbfUE2f3WVx5jPVQqkEAtavsltxxA_MThrT3vhp2fMHLkfnpiVL9zkkglUrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve  نمایه ارزش منصفانه طلا نزدیک به سطح مناسب خرید عالی است و لذا پیشنهاد می شود برای امروز خریدها رو به پایین باشد.  بهترین محدوده خرید از 4280 تا 4250 می باشد.  نکته: معمولاً وقتی به سطح خرید منصفانه نزدیک می شود بعداً رشدهای خیلی خوبی داریم…</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SBoxxx/20923" target="_blank">📅 00:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20922">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RsG2Bv0VpQovMiBazeo6-_fvnZH6hPgh9cGz0UJgOGfD9dDS2ys9PGFBpU-2hJjkF9TXE_XlyYH03mpqdTykAMHy-mcPGEwoSAyBbsLVmQfzOHr3SJMn46Jl9Z4G8bK-n0y0PQaXANggpLSlHSN9-J6bkaY3Sfd6wfGmMEG0XgWbN1GupEbhxI1J_7h7mvDMs2V4IkxhdhhThjo04Nc6EKSujpTW94uym9OLCvOxlJ4C9BXgX4fUwrrssFV-Tw_6LecvKbFuZxE94hKyUq5juoipjRX4U9T07TkknDFLJRdSKwd3ydW2sssCyZnJ9Wr4ZSPzDLns-PEMRhx0j3J6iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - Podcast 27</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/20922" target="_blank">📅 00:18 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20921">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f__S7kJaQRyxxp09rkmMhg1wKgYbH2cwEiGY2NcTcaCU_Hpi18PBG_tBhp4baA5uhwwDrqEDQa9-MHoMWCPh1MDrNj9qJGM51h3Hnju8jX-GBsSmaY2kMhISWAI64NuhoIOTRBSpYQUcNEugfuffr6jtAOwk9x5riXqgiVq9w4okKanNRTix__B9IeYwfoVw4LjAknIA5jyDudkgsoMIqPshvwwPyXEjJ49d1luWFnImaJFyJY8avdidYSuoGii5E0IQVCYo_isX-niZuMmXOsBAOllJspJ4oV0sWQu9cQt5Qu2oxq1M94xNpgoaikcGMKWo4TSlm9jPguVXL8NfUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا امروز برای ادارات و نهادهای دولتی ابتدا کد 100 (تخلیه فوری) صادر شده و باعث ایجاد اخلال در کار ادارات شده و بعد از چند دقیقه وضعیت سفید اعلام شده و با اعلام کد 69 همه به سر کار همیشگی خود برگشته اند.</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/20921" target="_blank">📅 00:13 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20920">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">به گفته مقامات آمریکایی، دولت ترامپ در حال تدارک فروش بمب‌های ۲۰۰۰ پوندی به ارزش میلیاردها دلار به اسرائیل است؛ اقدامی که بزرگ‌ترین فروش یکجای این نوع مهمات بحث‌برانگیز در سال‌های اخیر محسوب می‌شود.</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/20920" target="_blank">📅 22:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20919">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">به گفته مقامات آمریکایی، دولت ترامپ در حال تدارک فروش بمب‌های ۲۰۰۰ پوندی به ارزش میلیاردها دلار به اسرائیل است؛ اقدامی که بزرگ‌ترین فروش یکجای این نوع مهمات بحث‌برانگیز در سال‌های اخیر محسوب می‌شود.</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/20919" target="_blank">📅 21:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20918">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">عراقچی فردا به چین سفر می‌کند</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/20918" target="_blank">📅 19:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20917">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">آکسیوس:
یک پهپاد آمریکایی پس از تلاش سپاه پاسداران برای توقیف یک پهپاد نیروی دریایی آمریکا، دو قایق کوچک ایرانی را در تنگه هرمز منهدم کرد و اکثر سرنشینان آن را کشت</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/20917" target="_blank">📅 18:46 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20916">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">بارگیری نفت در ینبع، مهم‌ترین بندر عربستان سعودی در دریای سرخ، به دلیل حمله قبلی به خط لوله شرقی-غربی، متوقف شده است. (به نقل از خبرگزاری رویترز)</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/20916" target="_blank">📅 18:33 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20915">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">بارگیری نفت در ینبع، مهم‌ترین بندر عربستان سعودی در دریای سرخ، به دلیل حمله قبلی به خط لوله شرقی-غربی، متوقف شده است. (به نقل از خبرگزاری رویترز)</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/20915" target="_blank">📅 18:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20914">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">#FairValueCurve  نمایه ارزش منصفانه طلا نزدیک به سطح مناسب خرید عالی است و لذا پیشنهاد می شود برای امروز خریدها رو به پایین باشد.  بهترین محدوده خرید از 4280 تا 4250 می باشد.  نکته: معمولاً وقتی به سطح خرید منصفانه نزدیک می شود بعداً رشدهای خیلی خوبی داریم…</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/20914" target="_blank">📅 16:32 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20913">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">وزارت خارجه چین: «ما با هرگونه رقابت تسلیحاتی در فضا و همچنین هرگونه تلاش برای تسلیحاتی‌کردن فضا یا تبدیل آن به منطقه جنگی مخالفیم.   از آمریکا می‌خواهیم گسترش حضور و توان نظامی خود در فضا را متوقف کند و با اقدامات عملی، از ثبات راهبردی جهانی محافظت کند.»</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/20913" target="_blank">📅 16:14 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20912">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T9qeESBDpeSUdJt5xliGAQxjijUQ7qnZW_gSg9p4XDrnziWQZnc-aq3ariZBx1eg3K-1Rg_7S37Ctmag1z0DQALZE-oM7-dXuWsANUM4e-urpejflU25WgX1c3ugriWgFIdOQQKxsWeROsk_VJc5HhUOTka0v5BnbUHPpCviaMuwauvRFMsCyO9LBKF2P3GYKAJWoXRrZrJulZ5tJ_P6MY3Bfpyw3Sj_LutzlKFKcD_2vVzmJ2hoFqwskbtkvUMkNDLJZOfIFDvKT_AVXRCEHFAnNcpVz6R7HcgK5Id4mhHKfeBmHn478WsX-hei6KyTdfzlDB-1fH39m_uREWb2aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سخنگوی پویش جانفدا :  جان فدایان غیور صرفا برای اهداف نظامی به کارگیری نخواهند شد ، به زودی پیام های جدیدی را به این عزیزان تقدیم خواهیم کرد</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/20912" target="_blank">📅 16:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20911">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">وزارت خارجه چین: «ما با هرگونه رقابت تسلیحاتی در فضا و همچنین هرگونه تلاش برای تسلیحاتی‌کردن فضا یا تبدیل آن به منطقه جنگی مخالفیم.   از آمریکا می‌خواهیم گسترش حضور و توان نظامی خود در فضا را متوقف کند و با اقدامات عملی، از ثبات راهبردی جهانی محافظت کند.»</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/20911" target="_blank">📅 16:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20910">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">گمانه زنی هایی دال بر انهدام ماهواره چینی فعال در کمک اطلاعاتی به ایران از سوی نیروی فضایی آمریکا منتشر شده است.</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/20910" target="_blank">📅 16:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20909">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">به نظرم بین اسراییل و ترکیه و پاکستان یک تورنمنت سه جانبه بگذارند ببینند کی می‌تواند برنده شده و بیشتر گاو شیرده حجاز و نجد را بدوشد!</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/20909" target="_blank">📅 16:02 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20908">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">رسانه عبری والا به نقل از منابع:   تماس‌هایی میان عربستان و اسرائیل با میانجی‌گری فرمانده سنتکام انجام شده تا از طریق ارائه اطلاعات، به سعودی‌ها در دفاع از خود در برابر انصارالله کمک کنند</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/20908" target="_blank">📅 16:01 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20907">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">این هم پاسخ ترامپ به چموشی سعودی های مفلوک در نپیوستن به پیمان ابراهیم و در عوض دست نیاز پیش فاکستان ورشکسته و عثمانی مقروض دراز کردن!</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/20907" target="_blank">📅 16:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20906">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">در سوریه با گران شدن سوخت، اعتراضات مردمی آغاز شده و آشوب ایجاد شده</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/20906" target="_blank">📅 15:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20905">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - Podcast 27</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/20905" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 27
سه شنبه 15 سپتامبر  2026</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/20905" target="_blank">📅 13:05 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20904">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">گویا امروز برای ادارات و نهادهای دولتی ابتدا کد 100 (تخلیه فوری) صادر شده و باعث ایجاد اخلال در کار ادارات شده و بعد از چند دقیقه وضعیت سفید اعلام شده و با اعلام کد 69 همه به سر کار همیشگی خود برگشته اند.</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/20904" target="_blank">📅 12:25 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20903">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">گمانه زنی هایی دال بر انهدام ماهواره چینی فعال در کمک اطلاعاتی به ایران از سوی نیروی فضایی آمریکا منتشر شده است.</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/20903" target="_blank">📅 12:22 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20902">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPfyoM7244Wi7dv_YlPkC0xkVPGuf9oVFDPVU6PpoOgqbjIJ6287mDz-NA4qhCT1BDVlqikI_RPGimPjH5fmK1daQlnLIdC57rfmuIOv717gDgwVgFIgPyU4xDGebIzc9DZ-y7siHlePqJPJYQJ5YvrV4VgatqRQ7AIT4cmqV_chdSrodxwRxIGnKAl7CLQMpGhLG5SxKw4X-Wab4IA_l6ea5yTPgUpOkTnUtPpxkv6fL-ZqdweL7lSWDmhcDZqtpP4QytFsoCnRdc4GTn9aXK-yFeCgeL_4HkIgcnU3O6g6X9oTDfzm1knXej2CUA4KHdztYXKp_ldvH2NkxXU5dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گمانه زنی هایی دال بر انهدام ماهواره چینی فعال در کمک اطلاعاتی به ایران از سوی نیروی فضایی آمریکا منتشر شده است.</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/20902" target="_blank">📅 12:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20901">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ocjvC1RIH8FGxUOIiipOZp_XHu9HoQvYJQsmvFj7-K_FkQePOJ4a-RH_r928kuapCDAjSfBwCHbwnHGdooK65tKtFwKhos8hiTVLp64d-QKBzLs0PDGrl3kXWYKmNxxSmVs50DayWHZa60yAbB3cVBhkBG3ldj9ZLnMTrCtX8ySxymQN-UQSyZ5lqcwHQBdSZ9cnRpmDI7NHRL4WXen5dtOK4i5PmWqOG79omDpQvP9_Xt7NHoZxorX__xqd5y46s9Y9L3Bsslz9tRfp6nkWntoVm2EMDHN4gCU2E08m30Iyi2mnIcz_up2ZmaOrkvCvmIxpVFxYj4GGtwUGVZjejw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وال‌استریت ژورنال: کمک ماهواره‌ای چین به ایران  به گزارش «وال‌استریت ژورنال»، مقام‌های آمریکایی می‌گویند ایران پیش و پس از حمله موشکی ۱۷ ژوئیه به پایگاه «موافق‌السلطی» در اردن، از تصاویر ماهواره‌ای با وضوح بالا از منابع چینی استفاده کرده است.  در این حمله…</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SBoxxx/20901" target="_blank">📅 11:56 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20900">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PgAIdLFumkOd8yYYBfBT8GuqGD68RdU-lNla7aId3SWPlGLSHp6gGxTr2qmjE_HsotANTu-K75jd4Do1qIkcL0Va9pfkUG3GBTweetrVTi-UUZIgCTyUkAzhfLlUr3CMG20kGc6nZ0KsSQuKc89gd_apKL018-xSlxRpbuC5ADoO-ha5AE7AdqE6m-U1dvUL5WNMa1Qyal3nlSw9s5O6beCfWdO_rjOTMrAaBmLSFcfemENYZZJEDvlifNXxVNEG5-0WrYRiRUtB7CPzWN6X4IULHLuZ-jjNEBjUgOBJRZf-KqOSARV0l6ZXkA7z_Jb6ZGFln3IY-jyNYYvexBRDdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve  نمایه ارزش منصفانه طلا برای امروز در حال نزدیک شدن به محدوده تخفیف ویژه (پایین تر از ارزش ذاتی) است و هر چه به سطح 4290 نزدیک تر بشویم برای خرید مناسب تر است و تا زیر 4300 نرویم خرید منطقی نیست.</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/20900" target="_blank">📅 11:36 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20899">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PRDL6PoTxvr5kFFILjgIm1LJ5_l4WtRBEvWt4Nl-R8QeJBlNWpWM2kl-WrnZc9ZphjkHZRsWx491urVHJPA07azGWrQb7x401K-FTvlt9_wO3ZRD26bjnu1ujH94VBvqm7F8SNHd1Yn7MVjm9nGerpK2AdPZv2ckLTbGz6IzlkrfDfsk_1US8kHc4WfZyEWxH4OX3XSt5qs6wbZS48KJEZfEftsfTIE_Bto01WdiEE9ayEUwRqX6CHIXgwJDT_p4AUIrfCPM5XgFWii3yMa8KTbh47S4SJFIKyiSv_XI9AFoSJBJ82t_sbfQBckk-jJNQbhAMkSWCLOwhRR_Smu6GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه ارزش منصفانه طلا نزدیک به سطح مناسب خرید عالی است و لذا پیشنهاد می شود برای امروز خریدها رو به پایین باشد.
بهترین محدوده خرید از 4280 تا 4250 می باشد.
نکته: معمولاً وقتی به سطح خرید منصفانه نزدیک می شود بعداً رشدهای خیلی خوبی داریم و پیش بینی میکنم این هفته طلا سطح 4400 دلار را پس بگیرد.</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/20899" target="_blank">📅 11:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20898">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UtOjr6NkBqdBY8jxpYXqFNtRh7wsEc8GtIGYLa0pL1A-U5GPX78atjg4qFVnTegCyaMhtubf7BftJlEWvf1yk8V8nyrehlxPlCtxzv7rqBP0FVXE-MzNd0t4jjgTfQc9wcsGA6w4vtTkcgRjCvsa-dBQzA01nnnPQiqXB5L78UeldvZ7YHprU84qWQ0vcLpDGkHimVDQMhbXiHxogM4qJyVrt73oe2uwyobLpYoOl5aCzp3obYTjOlsF-4wpkqOtFDkX44BUfs-yv0IYHuKnzrjXNSnLoGNkZh8_leT8XnsqaONJ5o9fXh06fY4NDPgSddGtUDjQ7loZcGzY1KxDQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح نسبتاً بالایی است و احتمال فراوان هر بالایی فراتر از 4300 فروخته خواهدشد.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/20898" target="_blank">📅 11:21 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20897">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDtGhL6YCJzqct76pBDMJUc-HfF1bMH73SBKOCw9NjPmxChb2EciLaUnKhlRCtvrvT7aWG5IWcZndQLKTH3E4mQ_ZUZD5eC8h1x-r7fweWUN_-MgqOoQHhWck8TzVkl7Fnhy8Sv7yx-ubJdF17BnULhN9NTHg1hP_CMf3Hzr9kfmp7KOUcBU7OKr41gE7s9_2R0tTqPdzjdypJxzaO_V4fJHomQvOAPGguf3GxWPK7mTtmc_D2XdlHq9pK3eKuAf2quU761bgdsx96CGsi-cLzsJjeBJPmb9uh-pcobdciqAIt0NfGTVXIl8KLTyfpds6tggt_wuV0oY01v0E4f5FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله حوثی ها به عمق خاک عربستان در ۱۱۸۰ کیلومتری مرزهای یمن!
و کماکان از متحدین پیمان مکه (عثمانی و فاکستان) خبری نیست!</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/20897" target="_blank">📅 09:57 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20896">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">جمعی از نمایندگان مجلس در بیانیه‌ای خواستار تجدید نظر عضویت ایران در NPT شدند</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/20896" target="_blank">📅 09:55 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20895">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">درخواست کمک عربستان از انگلیس برای حمله به یمن
بعد از مخالفت آمریکا با حملۀ به یمن،‌ عربستان سعودی این‌بار از انگلیس خواست که در این کشور مداخله نظامی انجام دهد.</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/20895" target="_blank">📅 09:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20894">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">یک بار از یکی پرسیدند تا حالا اتوبوس هل داده ای؟
گفت نه ولی یک بار تو اتوبوس هل شدیم دادیم!</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SBoxxx/20894" target="_blank">📅 01:11 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20892">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">آن‌قدر به ما گفتند ترامپ تاجر است که قبل از جنگ به آمریکا پیشنهاد همکاری ۵۰۰ میلیارد دلاری دادیم!
- حسن قشقاوی، سخنگوی کمیسیون امنیت ملی مجلس</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/20892" target="_blank">📅 01:09 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20891">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TBasmSsocKLLJ6o847BesV2LvGhe2j9KUEIpoCe-gVRrCrq4d0SvJTPw6FM5PU1KVsxgJMdoXRgq3AAyFiok5ChjeLApGpxgvRVJX7wU6HcK-O8bAJyDiJfGjG2kjc_cFMfSwAxfNftIhVgSX8ah1X62nLyGL_80YXDg8ZvEgw_w4M7ud0D-idGf3ylEynA-RT0Py_LR1TD_NBWbrTcM48pV0Lnong3W_lJs0wkaPnkfPXVzr38BqeBImGCSZgMnpFBzyWvhO1tSJmJOSchrf-Ctt-eGDswWnVAPiBvS7me63RopcwIDRdFpjVg3Ofm6ekRc9aUtf2XWo6iTqDbX_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😀
💙
😀
💙
😀</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/20891" target="_blank">📅 00:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20890">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">برنامه ریزی آمریکا و عربستان برای حمله به مواضع تازه تصرف شده ارتش یمن در ساحل غربی
یک منبع یمنی وابسته به مزدوران سعودی اعلام کرد آمریکایی‌ها به عربستان سعودی در مورد مناطقی که مزدوران عربستان آن‌ها را از دست دادند و مشرف به باب‌المندب هستند، فشار می‌آورد تا این مناطق را پس بگیرند
در پی این فشارها عربستان سعودی با کمک نظامیان آمریکایی در حال طرح ریزی حمله ای به مناطق تازه آزاد شده ساحل غربی با نیروهای سلفی و سایر مزدوران است
این منبع اشاره کرد طبق دستور آمریکایی ها به بن سلمان این حمله بزودی آغاز می‌شود.</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/20890" target="_blank">📅 23:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20889">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">پزشکیان:
برخی کشورها در خفا به ما می‌گویند ما با شما هستیم اما در عمل از آمریکا حساب می‌برند و جرئت همراهی با ما را ندارند</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/20889" target="_blank">📅 22:49 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20888">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">پزشکیان:
آمریکا چون نمی‌تواند رهبر ما را پیدا کند درباره سلامتی ایشان شایعه می‌سازد</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/20888" target="_blank">📅 22:42 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20887">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران ایران اعلام کرد که نفتکش غول‌پیکر «ال‌گایا» (EL GAIA) هنگام تلاش برای عبور از یک «منطقه ممنوعه» در بخش جنوبی تنگه هرمز، با یک مین دریایی برخورد کرده است.  سپاه پاسداران می‌گوید تلاش‌ها برای مهار آتش‌سوزی ناشی از این حادثه بی‌نتیجه…</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/20887" target="_blank">📅 22:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20886">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران ایران اعلام کرد که نفتکش غول‌پیکر «ال‌گایا» (EL GAIA) هنگام تلاش برای عبور از یک «منطقه ممنوعه» در بخش جنوبی تنگه هرمز، با یک مین دریایی برخورد کرده است.
سپاه پاسداران می‌گوید تلاش‌ها برای مهار آتش‌سوزی ناشی از این حادثه بی‌نتیجه مانده و این نفتکش اکنون کاملاً در آتش می‌سوزد.
آن‌ها تأکید کردند که تنگه هرمز همچنان بسته و «تحت کنترل هوشمند» آن‌ها قرار دارد.</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/20886" target="_blank">📅 22:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20885">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">گاردین: طبق گزارش ها نخست وزیر بریتانیا در حال بررسی اعزام ناو های جنگی برای حمله به حوثی ها در کمک به عربستان سعودی می‌باشد</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/20885" target="_blank">📅 22:12 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20884">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">روسیه و اوکراین دارند با پیشنهاد ترامپ برای تعهد به نزدن تاسیسات انرژی یکدیگر موافقت می‌کنند</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/20884" target="_blank">📅 19:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20883">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">#FairValueCurve  نمایه ارزش منصفانه طلا برای امروز در حال نزدیک شدن به محدوده تخفیف ویژه (پایین تر از ارزش ذاتی) است و هر چه به سطح 4290 نزدیک تر بشویم برای خرید مناسب تر است و تا زیر 4300 نرویم خرید منطقی نیست.</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/20883" target="_blank">📅 19:56 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20882">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ادعای ترامپ:   ایران به شدت می‌خواهد در سریع‌ترین زمان ممکن توافق کند.  من تعیین خواهیم کرد که آیا وارد مذاکره خواهیم شد یا خیر، و این گزینه‌ای است که نسبت به آن پذیرا هستیم.</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/20882" target="_blank">📅 19:55 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20881">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ادعای ترامپ:
ایران به شدت می‌خواهد در سریع‌ترین زمان ممکن توافق کند.
من تعیین خواهیم کرد که آیا وارد مذاکره خواهیم شد یا خیر، و این گزینه‌ای است که نسبت به آن پذیرا هستیم.</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SBoxxx/20881" target="_blank">📅 19:08 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20880">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">محاصره اقتصادی | فعال شدن گروه های جدایی خواه</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/20880" target="_blank">📅 19:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20879">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اینها تغییرات بسیار بزرگی هستند اگر خوب دقت کنید.</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/20879" target="_blank">📅 17:47 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20878">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ادعای یک‌فعال رسانه‌ای: قالیباف کنار رفت!  محمد مخبر به عنوان نماینده‌ی ویژه ایران و چین منصوب شد.</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SBoxxx/20878" target="_blank">📅 17:46 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20877">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c6zCEsZ6ImrO1N4IlCGgMtwnOAj7Ov86lBMRUE1SibmVtEFfjy5wHAbo442lqpip5fhYR3wcluSLW5YgEkGrFP6iZbs1LitJce1lwQ4SyyEsZ1aDHKxeDWlP2H_1D8BHZjfUaejmL28CQAc4tm3u4c1U5bvKLrLt1wZ43TwPP3TVJgB63RQLW-5NSDVUImc8jFJ4YiGhCL3xcw1cOCRCEMhZRFHQvBhB2bSsNzpDe-FozRkX_29LO6oqqzbqkdnPnJevc1H9VqX2M_06KcPi4gC1B_G3YhBEHM3G5rDFCjfumsZZ2ODDWo_b5ECUD1GDkwD27W-FFBzuE46oMHMGfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیروزی احتمالی دموکرات ها در انتخابات میان دوره ای نوامبر عملا مبتنی بر یک سنت تاریخی است که در دهه های گذشته بارها و بارها تکرار شده است</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SBoxxx/20877" target="_blank">📅 17:03 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20876">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A9pHpLyxDkNINC3wdTtIAcN7njbGZiVjltDA4c5iXCRAuZ8rI7rFS49i1h2JWEz0FUkYxW2x_3JIxhp3JNRgcAfH5Vigg9wHwCEDASWJvxcHbAYV3WP3qQJqgu5rosrXl0TnsgJ1HvuyO5RXtZQOb3g2utNVeqYoBeIp_QUmSS_jj_gwu8LuHLO8948K85Np5B2U289W1Ic1mRK78FthzV-bzBIfJxgHm33pte8b3HtV03vVEvoq93WctZj7A0Q6qNBdc2y2AlRUKCFXAtt7FdxQGrhyXaAM4RtXrswI9zJQdQHyv_9JdV4YdmbmC4nGSHVfDgd85WJWppTOXg2YPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای ارواح عمه ات پاوول دوروف !</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/20876" target="_blank">📅 13:40 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20875">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ای ارواح عمه ات پاوول دوروف !</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/20875" target="_blank">📅 13:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20874">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l98m2HR_lhAHvOJdHFNStTgdnc4Ercusbt4dsRXFn1roERL4p15aYMejR8nQGt-5qVQtlYN3wqSzNCPWZxcPlG0_Ar6Vk-baXcZSe7BXHqdkM3qq3YQ6ruBBaP7SwUh6JMGHR3gy0j97TcdmP4AuCAE4BEBavlTGVFHmyMZBCWU1bQwq62kSjY2tdfM49pdvrrqb9B02huZ3sIewk5zeJOH-0Lj0fU2n30F3FC3NQ3qMjDvCuCS6hyDx8Wf0aCnYeb2lLLl4QS-Iq_WgYWo_FRPus_TABImjCpKNR_exg_SV3boAx7XwLWxG4RYp7mUK4N8v24EwQ0W4vHGappU2Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای ارواح عمه ات پاوول دوروف !</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/20874" target="_blank">📅 13:03 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20873">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">یک آوانس برای براکصه در آستانه سفر رهبر چین به آمریکا</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/20873" target="_blank">📅 11:55 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20872">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VAy5_jNlbHI3Xu-CqsYNQvFEDwrsijIA85ELmSFajAmNhdg50-fqAfeCC3XCDBvlBfLoHNTDhtjXIsPe6SuNvphIdzk7H1O5VMf8lsEXe_i4awQgxfI8qviLNi3T3mVMvV6c7j6m7yxYiLufYDRv7FKJwX2p3jWZQm0_AXIl4S0Dhd28LsIBLu503xNOSREnQxEI_4Mor4Qg8iNk3HK0daUVcX8VRDf97DU-4ERxUIBoGNNBqcLfRKRR2wWk5KOBgDHc2aSGeWOKjgT79FutYC3SnmEe4KeK-U_G30S_Yf9cK-Yf85ie-Dx_kG_MZfRl4I-vTWn2BhUuSRDmvwi71A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه ارزش منصفانه طلا برای امروز در حال نزدیک شدن به محدوده تخفیف ویژه (پایین تر از ارزش ذاتی) است و هر چه به سطح 4290 نزدیک تر بشویم برای خرید مناسب تر است و تا زیر 4300 نرویم خرید منطقی نیست.</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/20872" target="_blank">📅 11:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20871">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7051TInJY_QtmK0VAGi-7Q5rYV_gd1Xs1MRIkcdDOp5mjFQIzg1rU8RTetc4CMBNMHqZy6qqtaMrangXeEHyaeXXGBmpicnRCPFVc_Y4LDZFvZOrPB8VBgZEwm05sFPocOpczNkj9EJFzPvF5nHd6hvvJ4ogAHNTms0d2izjABiLvXYethlJP_bLNQiRD4vigNAsNz755tffmYVzXiRPstqO9bIuPhxFFWbuWlg3vkBeL55lS9U79v6cM655HiaKvFlxTrSTvlh7Iwa5_oLwe-pSpYa65EnB8w_oSB1cvYn5y3Bknf07THyulBdnp9_bUvbLb_9y3yoMXYH8HUipQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح میانه ای است و نظر به ریزش طلا تا الان، انتظار یک اصلاح صعودی می رود.
دقت کنید که رشد طلا «اصلاحی» قید شده.</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/20871" target="_blank">📅 11:49 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20870">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">📌
جنگ هرمز و باب‌المندب؛ آیا ایران در حال فرسایش مالی دولت‌های غربی است؟  اختلال در تنگه هرمز و افزایش فشار بر باب‌المندب می‌تواند با بالا نگه داشتن قیمت انرژی، تورم و نرخ بهره را تشدید کرده و هزینه تأمین مالی دولت‌های غربی را افزایش دهد؛ در نتیجه، جنگ از…</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/20870" target="_blank">📅 11:47 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20869">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ادعای یک‌فعال رسانه‌ای: قالیباف کنار رفت!  محمد مخبر به عنوان نماینده‌ی ویژه ایران و چین منصوب شد.</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/20869" target="_blank">📅 11:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20868">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ادعای یک‌فعال رسانه‌ای: قالیباف کنار رفت!
محمد مخبر به عنوان نماینده‌ی ویژه ایران و چین منصوب شد.</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/20868" target="_blank">📅 11:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20867">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eAucDI7mb9-POyufC_8qWmwsMRFMj4uPNUTIyAKUbYnMmnub7sCQeE30HVsBqiA8RbxcsjT9pV6VecLBGrRF8Y2Sxwj3QhF6fiG_XdKxcnQChGVRJL0Z0T_-2STShINAL33EEH2paSLkMQKL5ZmG0L9HYhNK82drlthtAm_PoN7i8Ujgy76EZVyHBW01Cn46zTdYeyZUODoi2J0HWMbLFF8rt5cAmSzoVMQZeagwMbgGM2qlOWMJNfLwO0j-Yns3Otr8ZE5fx0OsKgkejZ1skbwZ6AduARrYgSSDrvBDaYSllZ8Ab8f-6CzdYC-a4r3__Jb6DAnbAJMR6TSWcskLNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادداشت تحلیلی | سناریوی اختلال کامل در مسیرهای صادرات نفت عربستان
یک سناریوی حداکثری برای بازار نفت، تخریب خط لوله شرق–غرب عربستان، بسته‌شدن تنگه هرمز و هم‌زمان بسته‌شدن باب‌المندب را در نظر می‌گیرد. اگر هر سه اتفاق به‌طور هم‌زمان و برای مدت معناداری رخ دهد، بازار جهانی نفت با یکی از شدیدترین شوک‌های عرضه در دهه‌های اخیر مواجه خواهد شد.
اهمیت خط لوله شرق–غرب در این است که به عربستان اجازه می‌دهد بخشی از نفت تولیدشده در شرق کشور را بدون عبور از هرمز به بندر ینبع در دریای سرخ منتقل کند. ظرفیت این خط حدود ۷ میلیون بشکه در روز است. در شرایط عادی، صادرات نفت عربستان حدود ۶ تا ۷ میلیون بشکه در روز است؛ بنابراین از کار افتادن این مسیر، وابستگی عربستان به مسیرهای دریایی خلیج فارس را به‌شدت افزایش می‌دهد.
اما اگر هرمز نیز بسته شود و خروجی دریای سرخ از طریق باب‌المندب هم امکان‌پذیر نباشد، تقریباً تمام مسیرهای اصلی صادرات نفت عربستان مسدود خواهند شد. در چنین شرایطی، ظرفیت قابل استفاده برای صادرات نفت خام جدید می‌تواند به حدود صفر تا ۱۰ درصد ظرفیت عادی سقوط کند. البته این رقم یک برآورد سناریویی است، نه پیش‌بینی قطعی.
اثر اولیه چنین اتفاقی احتمالاً در بازار نفت بسیار شدید خواهد بود. بازار نه‌تنها کاهش فیزیکی عرضه را قیمت‌گذاری می‌کند، بلکه «ریسک عرضه» و احتمال تداوم اختلال را نیز در قیمت لحاظ خواهد کرد. بنابراین افزایش قیمت می‌تواند بسیار سریع‌تر از کاهش واقعی تولید رخ دهد. ساختار بازار نیز احتمالاً به سمت backwardation شدید حرکت می‌کند و پریمیوم نفت فیزیکی افزایش می‌یابد.
برندگان مستقیم این سناریو، تولیدکنندگان خارج از منطقه خلیج فارس هستند؛ به‌خصوص تولیدکنندگان آمریکای شمالی، کانادا و برخی تولیدکنندگان آمریکای لاتین. شرکت‌هایی مانند ExxonMobil، Chevron، ConocoPhillips، Canadian Natural Resources، Suncor، Cenovus، Petrobras و Occidental می‌توانند از افزایش قیمت جهانی نفت و کاهش وابستگی بازار به نفت خلیج فارس منتفع شوند.
در طرف مقابل، خود عربستان با یک تناقض استراتژیک مواجه می‌شود. افزایش شدید قیمت نفت از یک سو ارزش هر بشکه صادراتی را بالا می‌برد، اما اگر نفت فیزیکی امکان خروج از کشور نداشته باشد، افزایش قیمت نمی‌تواند به‌طور کامل زیان ناشی از کاهش حجم صادرات را جبران کند. فشار بر درآمدهای دولت، پروژه‌های Vision 2030، پیمانکاران و بانک‌های داخلی نیز در چنین شرایطی افزایش خواهد یافت.
اهمیت ناوگان نفتکش‌ها و مسیر SUMED نیز در چنین وضعیتی افزایش می‌یابد. در صورت بسته‌شدن مسیرهای سنتی، دسترسی به مسیرهای جایگزین و ظرفیت حمل‌ونقل دریایی می‌تواند به یک عامل استراتژیک تبدیل شود و نرخ حمل نفتکش‌های بزرگ، به‌ویژه VLCC و Suezmax، را به‌شدت تحت تأثیر قرار دهد.</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/20867" target="_blank">📅 10:40 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20866">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">رقابت عظیمی میان ترکیه با اسرائیل برای ایجاد هژمونی در غرب آسیا شکل گرفته که بجز جنگ با ابزار دیگری حل نخواهدشد.  بزودی در قفقاز هم شاهد تحولاتی خواهیم بود که نقش و جایگاه کشورها را عوض خواهدکرد.   اسرائیل به شکل هوشمندانه ای از دهه ها سرکوب اقلیت های قومی…</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/20866" target="_blank">📅 10:14 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20865">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LvzIdh9-w6oHqk27dgrkiGSdbb1Y8klGzT7Bl-qncklbgHiHEt3Znt2b0bCNuPE57_a2GkHPPs6xFjiOel4HXJDcVo8UeRCh5Zx2s1Ffb1VCbyfaf9xhjedMJspKlsaA8qgQYIWrlNz0Znwr7SpDpoxMPzg77MPbhZM0g9N0xUEKMWLvkLKwjOWLIscgkTfqop7y4eoxvqJbT8pp1_GK8Dd44rDSm5u7imKciQudbV8UTXln7rIPUUnciE0ktb66nj4YEx4GMmJaisnt_02XOwlC6ZWLkEbayXE5EaViTEvTo5cMreC7Eep5kxdGa0pEfxTLyxJwwLtojHO0Jem2Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ نفتکش‌های VLCC به شدت افزایش یافته و در تمام مسیرهای اصلی به بالاترین حد خود رسیده است، زیرا جنگ ایران ترافیک تنگه هرمز را مسدود کرده و جریان جهانی نفت خام را مختل کرده است.
هزینه انتقال از خاورمیانه و خلیج فارس به چین به حدود ۱ میلیون دلار در روز رسیده است، در حالی که نرخ خلیج عمان و چین در یک ماه ۳۰۰ درصد افزایش یافته و به ۵۷۱۰۰۰ دلار در روز رسیده است.
این محدودیت فراتر از خلیج فارس در حال گسترش است. نرخ نفتکش‌های غرب آفریقا به ۴۱۱۰۰۰ دلار در روز رسیده است که در یک ماه ۲۸۰ درصد افزایش یافته است، زیرا سفرهای طولانی‌تر اقیانوس اطلس به آسیا کشتی‌ها را متوقف می‌کند.
موسسه لویدز می‌گوید که خرید مجدد نفت خام چین، ترانزیت‌های خطرناک تنگه هرمز و راهکارهای ناکارآمد فزاینده - که اکنون با تعطیلی خط لوله شرق-غرب عربستان سعودی بدتر شده است - عرضه نفتکش‌های موجود را بیشتر محدود می‌کند.
با توجه به اینکه حاشیه سود پالایش هنوز به طور غیرمعمولی بالاست، اجاره‌کنندگان تاکنون می‌توانند شوک حمل و نقل را تحمل کنند. دلالان می‌گویند هنوز "سقف مشخصی" وجود ندارد.</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/20865" target="_blank">📅 09:57 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20864">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7e-EbzYlWLDjofC-kHOg3RXNenTP28kADwxwZyZShusWR72WgQ7AeMs8N_aHAPDhpV3ym_J1m6VLF7aAetMsbKdKaMRXZW9r_Ob9SBriaR8EAuLtAmpdqQln1C5cA3FrXTjUwgQZNaYPXZzVDo-Rl6GGV-rmcGILHk4cfLhnezY44eyL1pp6B-GvjG7YTn8Nk3S0Wt7iEEiFvtaCHrePrhxi5nLy6rRllylzGTtakePD9vUodRsXBqXW71ZZWMGXa-6Z813AcWQrcaxoSFmHZunKR9Uf76vktdpxBTQYaRXV6q7zBt6MtGm6fFGeHjEfWtR1HE20rgEV1zdGUkW6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان سعودی ممکن است تا ۴ درصد از عرضه جهانی نفت را از دست بدهد اگر خط لوله شرق-غرب آن به سمت دریای سرخ در عرض چند روز
راه اندازی نشود
این خط لوله پیش از حمله پهپادها که منجر به توقف آن شد، حدود ۴ میلیون بشکه در روز به ینبع منتقل می‌کرد.
منابع صنعتی می‌گویند ینبع در حال حاضر فقط مقدار کافی نفت در انبار برای حفظ صادرات به مدت پنج تا هفت روز دارد.
این منبع زمان مورد نیاز برای تعمیرات را فاش نکرده است؛ برآوردهایی که رویترز به آن‌ها استناد کرده، از راه‌اندازی مجدد جزئی در زمان زودتر تا ۵ یا ۶ هفته طول می‌کشد.</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SBoxxx/20864" target="_blank">📅 09:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20863">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hysGJeHkunSdA4UrO5TayAM5UvDIvOq7Gmk4aJZVkiMlZUuqyY4kAg7xvdY4nZ4PalAVi6BeBlZ1sY3qrDxgNcvhyhMbzAfE8PyiIb9MQdbLYDBLJU0_Pfevmy7oD1oNXe9HTbzCx-HR1ZCLlPqivV3QgO3YTjezVKk5-JEryWacgkGK41rQEqaS3jB3ayLvwzFJJ4AdkEl2NqD-3m3yymne7ri0wfbMRS-xf9ek0hYWX902LUVJNx7vgjK9x9Tx2i7XAzkZnAKiLUe93gRAInC_ajrSTRLcUN-3lyrBRlHHL7DHJf1gtnZrgyp-u97F0GqO4auUzWBke5IfdkShMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر امور خارجه عمان پرچم  شیر خورشید ایران رو گذاشت
😁
@Piknikanalyst</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/20863" target="_blank">📅 00:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20862">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">نشست فردای ایران، عمان و کشورهای عربی سر تنگه هرمز فعلا لغو شد</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SBoxxx/20862" target="_blank">📅 23:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20861">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">شلیک موشک از ایران به سمت تنگه هرمز</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SBoxxx/20861" target="_blank">📅 23:28 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20860">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FEWiEspCDN9oThgr0usRVAmEdSYRcgc5t2isSa12chszeui6sDSSiEmF-SzELcfsUWJA8UdSA1Cck4fj51gHdyROGIiis6JunJZDR5RrjShugr75wnmr7g6V3fZ8aNmZ4qbRy1Z6cmS4hZpkZlIWze_pL2WhVeZWOfXFCk4MiVllmurzO_IMV6XGRQ4aWB4PeemR04O7uQ8qh-oNKoxYtZLahGYVsGo5F-k1ZtYj6fuvCszNlL-P-uQX9-hwT5RYpk_m5Nf2igmVFgOYrLLFwICa4vlJYz44Mg-y9alkuZmMPJKiJ6s4N2ln7MTY8Y8NSBjgsZzuc6e_ZaIqd8PStw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر امور خارجه عمان
پرچم  شیر خورشید ایران رو گذاشت
😁
@Piknikanalyst</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/20860" target="_blank">📅 23:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20859">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">توافق ایران و عمان برای تنگه هرمز به معنای باز شدن خودکار تنگه نخواهد بود   منبعی نزدیک به تیم مذاکره‌کننده ایرانی به تسنیم گفت: درک چارچوبی در مورد مسیرهای کشتیرانی «به زودی اعلام خواهد شد»، اما «فقط» بین این دو کشور است و مسیر جنوبی هرمز را بسته نگه می‌دارد.…</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SBoxxx/20859" target="_blank">📅 22:51 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20858">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xl19E2J-UWo6Rori-LZADviqe4LkAlFMgrW0LRrD6dK5DjgAl8DOdXdtA_UNDoo8oegIsW4Xm9nYR6NAi8BxtcAj2-1WM7PAqJMFIYTVtMR2s7HbBiIpeNcV2KIuvhala4xPmjv8fbxNaoeNezU5gOB3nzsGqQcSUwFMaM9cQIr1tObQriSVSqQT-VPGkjuvHCl9TTa_57pwovzNiKX3d6zs43jnFj18PSzRVMirNmma677IQM2cBpVcOYFLj_-vseJCPUlK4FG2Ge9kBweeuLqy5VOEx9aLL1n2jqVe7a89gITHrkxxC_f0Eruxg6sPTNTywXi9wnU2ttjHuZ5GxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگنده J-10C چین: نیرویی جدید در آسمان جنوب آسیا  جنگنده J-10C چین اولین پرواز رزمی خود را انجام داده و نقطه عطفی بزرگ برای صنعت هوافضای چین محسوب می‌شود. پروژه J-10 که در ابتدا در اوایل دهه ۱۹۸۰ تحت رهبری دنگ شیائوپینگ آغاز شد، با هدف توسعه یک جنگنده بومی…</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SBoxxx/20858" target="_blank">📅 22:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20857">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">فیدان: سوریه می‌تواند جایگزین مسیر هرمز شود
وزیر خارجه ترکیه گفت:
سوریه می‌تواند با اتصال به اردن، عربستان، عراق و ترکیه، نقش مهمی در ایجاد مسیرهای جایگزین تنگه هرمز ایفا کند؛ مسیری که قرار است از طریق راه‌آهن، بزرگراه و خطوط لوله عملیاتی شود.</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/20857" target="_blank">📅 20:27 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20856">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dlx6VMOSzzINnfxSq_kk5CceijC3TS3YeuQKwwTF9V3K3y_zd0DR7Mr6tRjX_quODBOGnwS_vZIo4HQocVjDUOAWMDfZIElKM7yhxaziUiDgogJjG0xTAURQztrQG1UEqcsHy4BBYWBfWFCl7FLwDcZ3iasFdI-NUKjU5d0xuKNG4WEizwvwYlNtE9C3hejwlqu2QxpMzpqAhPvQcbCspfAFyVDWiuDfbFvenih0EreXu1VV-oEvEUKJQ_w7OptivwW5hFoyMkvD5-nK4z0m_V8IeZwn6Qv3DyU44-4Q_O_ZZIqwflZeJFEHIyZV-Zl_EWRO0vN0UB7UTYxFviBHwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فایننشیال تایمز:
ایران از روسیه درخواست پهپادهای اصلاح‌شده «گران» را کرده است
بر اساس گزارش FT با استناد به منابع امنیتی غربی و یک فرد نزدیک به کرملین، تهران به مسکو برای پهپادهای مدرن‌شده خانواده «گران» روی آورده است.
باور بر این است که ایران قصد دارد از آن‌ها در درگیری جاری با اسرائیل و ایالات متحده استفاده کند.
این نشریه علاقه تهران را به توسعه سریع اصلاحات جت‌ساز روسی و افزایش قابلیت‌های این پهپادها از نظر برد، سرعت و هدایت مرتبط می‌داند.</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SBoxxx/20856" target="_blank">📅 20:07 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20855">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ub8KYXRB7eQi5gp2kgUVwkSrDqbsgy46Wv0hu9lvI6-FVy2uTlx4dEpBVJN6xtSc8nocTLn6BIv6eC_8w1g_wiP6qYdJgBdvuXnNUkxSMZnAFSWpZVk24y1zxQ4ERaadtgzZ0zEEDWc1QT5axxmX3u3INho5kZur2xEOmQpFHF768Zmt0dyAai1lmvcTfKxPaXTktF5yAI5K5cIlVOtNZUtjZ4ZHzhqz9y_i0QcBhXAcmM7op_k7aTdbSuVcnYsS3rF00ojmHVMHHbs5VRPpiedPUdv28vUKAloOOpJ2MtX4bqhBuFwaUEqs7fy9lxmUHERl4112-MBLHsS2uefOIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
نشریه شماره چهاردهم منتشر شد
📌
در این شماره می‌خوانیم:
✔️
طلا؛ دارایی‌ با بازدهی پایدار بالاتر از تورم
✔️
واگرایی میان فدرال رزرو با خزانه داری
✔️
وضعیت رشد تورمی در اقتصاد آمریکا
✔️
چرا طلا یک دارایی راهبردی محسوب می‌شود؟
✔️
و...
🔗
نسخه PDF ویژه دسکتاپ
🔗
نسخه PDF ویژه موبایل</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/20855" target="_blank">📅 18:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20854">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">انفجار در بندر ینبع عربستان</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/20854" target="_blank">📅 14:17 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20853">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">هم میهن:  ترکیه به جای دلار گاز، غذا و دارو می‌دهد همتی به استانبول رفت  منصور بیطرف/ روزنامه‌نگار و تحلیلگر اقتصاد  دو روز پس از آنکه مهمت شیمشک ، وزیر دارایی ترکیه اعلام کرد که آن کشور - منظور ترکیه - پول گاز وارداتی از ایران را مستقیم پرداخت نکرده و بر…</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/20853" target="_blank">📅 14:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20852">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">هم میهن:
ترکیه به جای دلار گاز، غذا و دارو می‌دهد
همتی به استانبول رفت
منصور بیطرف/ روزنامه‌نگار و تحلیلگر اقتصاد
دو روز پس از آنکه مهمت شیمشک ، وزیر دارایی ترکیه اعلام کرد که آن کشور - منظور ترکیه - پول گاز وارداتی از ایران را مستقیم پرداخت نکرده و بر اساس سازوکار توافق‌شده با آمریکا عمل می‌کند ، عبدالناصر همتی ، رییس کل بانک مرکزی ایران وارد استانبول شد
به گفته شیمشک، مبالغ مربوط به خرید گاز ایران در یک حساب به‌شدت تحت نظارت و تنظیم‌شده نگهداری می‌شود و ایران فقط می‌تواند از این منابع برای خرید اقلام مجاز در چارچوب رژیم تحریم‌ها، از جمله مواد غذایی، دارو و کالاهای مشابه استفاده کند.
سخنان شیمشک فقط درباره پول گاز نیست. این اظهارات نشان می‌دهد که ترکیه در دوره فشار حداکثری جدید آمریکا فعلا حاضر نیست برای حفظ تجارت با ایران، ریسک قرار گرفتن نظام بانکی خود در معرض تحریم‌های ثانویه را بپذیرد</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SBoxxx/20852" target="_blank">📅 14:12 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20851">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FtmeadCSuaX816Nyz0C5rCwMY4PYeBkOEtOv9TyzI900ybWgN_t1zt8Xl3GJDYnweAYokwnxAgWCVPrGiKimFmRp-eceXV7liNiHdArv9_UClXUYTFtsLPQUI-V6P4fumao7tCAd0QsX2aQy-NJ1dFgqy_1i3FBT5Cdtkw1esrxdqkIYOrtG6V34fZjeWUvEXVut7kg1cd-NSTW6vyLBsyfshyYEXgKnncK3twOMUBRm9L3A120IWnrp3C30fl-j7bBXBGwKFvug9XQhLw7dmHLU-qTY90tL7Q-CMfp3uMgevnUExRdCGssqNLOcQs6yCq3YMpt_D7VeaokeJasfxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فایننشیال تایمز:
حوثی ها با هوش مصنوعی آنتروپیک موشک بالستیک ساخته اند!</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SBoxxx/20851" target="_blank">📅 14:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20850">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">پزشکیان:   نمی‌دانم مشکل آنچه در پاکستان نوشتیم چیست که آمریکا می‌خواهد از نو گفت‌و‌گو کنیم</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SBoxxx/20850" target="_blank">📅 12:14 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20849">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">پزشکیان:
نمی‌دانم مشکل آنچه در پاکستان نوشتیم چیست که آمریکا می‌خواهد از نو گفت‌و‌گو کنیم</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SBoxxx/20849" target="_blank">📅 12:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20848">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">خب امروز و بعد از ۹ ماه تارگت ۲۴۰ هزار تومانی دلار محقق شد.  بعید نیست مدتی رنج بشود.</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SBoxxx/20848" target="_blank">📅 11:47 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20847">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">— یک کشتی تجاری ایرانی در نزدیکی جزایر هنگام و قشم مورد حمله قرار گرفت که در نتیجه یک نفر کشته و سه نفر دیگر زخمی شدند.</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SBoxxx/20847" target="_blank">📅 10:33 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20846">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">احمد اروزان کارشناس ترک:
خلبانان اسراییل برای حمله به ایران در قونیه ترکیه تمرین میکردند!</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SBoxxx/20846" target="_blank">📅 02:20 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20845">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">معاون وزیر خارجه یونان:
ترکیه و همه در منطقه می‌دانند که یونان کشوری بسیار قوی است که جایگاه بسیار بزرگی ژئوپلیتیکی، دیپلماتیک و نظامی کسب کرده است.
و من مطمئنم که هیچ‌کس هرگز این قدرت‌های یونان را آزمایش نخواهد کرد.</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SBoxxx/20845" target="_blank">📅 00:39 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20844">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i1L8IVmIFCvUqADLhslSfEhm5fkaf6Hxz52jpJro2wI3W3tnWGcILJXtLomk9DwszIAlY8I9zvYytU5HnE-Qyc5SskLW0eG1w_VSgHtSiQWY1MtxFNnmQVkaJQiHef8ke0hm0eGqtCzSDVxKIhm2bpli5rUiY4Y0Hvnxi6X9G310bWhq9YzfP0anCQ0UFP1EGMOH6ehvbn1CKRSIlTfn9-Y1Qb8SRuqmFL89o_tOTlvREiWSEHksrAqDokX2WjpeC_YWUwu65p8i4-Ymo-C-Mrcnm068sKBmE9mNfmLjVLpVcw358bnZSIVBk4IJIbgpMNfOTZCoT7TCqC-IpgcG6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت پیمان مکه!</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SBoxxx/20844" target="_blank">📅 00:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20843">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">پرتاب موشک از ایران به سمت هرمز</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SBoxxx/20843" target="_blank">📅 00:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20842">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">کانال ۱۴ اسرائیل:
ایران در حال آماده سازی برای تست سلاح هسته‌ای است</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SBoxxx/20842" target="_blank">📅 23:53 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20841">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vzq_ILz07k-292oR9L8VSlBQhiuCbCJSGOSb4xSGQJuL17mW-O69gllGjF4xxvY-R8rjAF2EP9s1jR06HZEqR8Lhe-0ViAg8Ypohk7DHSr96wQX0mRUXXfEljZ9BTSUBFPEcD6Y9RD5NmHMb2L1jq5erisha-0g-KBVC6vUWn4wRl2CgVhJU6yUdcaE4lGbw4ZyE-9ziMTmGZo3LNjXFsRzhbKvBl0LM1kuY_LWTxzguw4MUsiOdns2zz8IHmlRDlGN4tKC9G06KR3iOU4o-_HGBH4snbahqmnwJjQWgzVWuCfnXH89Fus7QRKZyPDFnWoyFghlIyBJYjAOvDANkVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SBoxxx/20841" target="_blank">📅 23:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20840">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">توافق ایران و عمان برای تنگه هرمز به معنای باز شدن خودکار تنگه نخواهد بود   منبعی نزدیک به تیم مذاکره‌کننده ایرانی به تسنیم گفت: درک چارچوبی در مورد مسیرهای کشتیرانی «به زودی اعلام خواهد شد»، اما «فقط» بین این دو کشور است و مسیر جنوبی هرمز را بسته نگه می‌دارد.…</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SBoxxx/20840" target="_blank">📅 23:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20839">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">پزشکیان مدعی امضای توافق هرمز با عمان در حضور کشورهای عربی شد  رئیس جمهوری مدعی شد مقام‌های ایران و کشورهای عربی خلیج فارس روز دوشنبه در مسقط توافقی برای ایجاد مسیر کشتیرانی مشترک میان ایران و عمان در تنگه هرمز امضا می‌کنند.  مسعود پزشکیان گفت: «کشورهایی که…</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SBoxxx/20839" target="_blank">📅 23:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20838">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ترور یکی از بسیجیان عشایر منگور
سپاه پاسداران انقلاب اسلامی شهرستان پیرانشهر با انتشار بیانیه‌ای، شهادت حاج اسلام کاک درویشی را تسلیت گفت.  پاسدار پیشکسوت و دلاور عشایر منگور، حاج اسلام کاک درویشی توسط عوامل پلید ضدانقلاب در مقابل منزل خود در روستای کوپر به شهادت رسید.
شهید اسلام کاک‌درویشی از جانبازان سرآمد و از نیروهای مخلص و وفادار به ارزش‌های انقلاب اسلامی بود که سال‌ها در مناطق کردستان و آذربایجان‌غربی مجاهدت کرد.</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/20838" target="_blank">📅 23:14 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20837">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">معاون رسانه‌ای انصارالله یمن: با هدف‌گیری خطوط‌لوله و پالایشگاه‌های عربستان کار به نفتکش‌های سعودی نمی‌رسد
درصورت تشدید تنش میتوانیم زیرساخت‌های نفتی را هدف قرار دهیم تا اندک صادرات نفت عربستان از کانال سوئز هم قطع شود.
همه چیز ممکن است؛ مگر این‌که محاصره علیه یمن برداشته شود؛ عربستان فعلا درحال لجبازی است.</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/20837" target="_blank">📅 23:07 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20836">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">تهدید فاکستان به حمله موشکی در صورت دخالت نظامی در یمن</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SBoxxx/20836" target="_blank">📅 20:39 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20835">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">پزشکیان مدعی امضای توافق هرمز با عمان در حضور کشورهای عربی شد
رئیس جمهوری مدعی شد مقام‌های ایران و کشورهای عربی خلیج فارس روز دوشنبه در مسقط توافقی برای ایجاد مسیر کشتیرانی مشترک میان ایران و عمان در تنگه هرمز امضا می‌کنند.
مسعود پزشکیان گفت: «کشورهایی که خاکشان از سوی آمریکا برای حمله به ما استفاده شد نیز در این نشست حاضر خواهند بود.»</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SBoxxx/20835" target="_blank">📅 20:22 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20834">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F160A2taRFhcAr9WC0fU492a-g4PHXnkzT87hFaG1gvrMWtS4Ho_e5IAtMFA59PSpKFatHRjtTjUfgSNvsHJR4rxqhwa6DUjXcOXh31vI4pzZTyBdjJvQ_rvNW-_dLgihloqnTDsmbLTXYMciK_atGEfKV63aO2j6fbq0mr-5oL4ooOUuQrQRNmnE6V8QIRKI9nHYWFu1noUDbn8Oa2mSGdUPcCHUBvBzDyrTkkhSW_GgiqiM9pAJFL7XsQ-shY2JyhUXgiCGAwCPky9dwhidY433elGqGGrb6aQiqBoxxKP3s4cLyErU6h-sVM3sreST7yo7e653HoRTRFAx7U5XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی ان ان:
اوکراین در نبرد با روسیه، فراتر از اروپا، تیم‌های کوچک متخصص پهپاد را به آفریقا و خاورمیانه اعزام می‌کند تا نیروهای محلی را آموزش دهند، از گروه‌های ضد روس حمایت کنند و به منافع روسیه حمله کنند
حدود ۱۵ متخصص اوکراینی در شمال مالی در کنار جبهه آزادی‌بخش آزاواد (FLA) که توسط توآرگ‌ها رهبری می‌شود، فعالیت می‌کنند و به جای درگیری مستقیم در خط مقدم، آموزش پهپاد، اطلاعات و پشتیبانی عملیاتی از راه دور ارائه می‌دهند.
نیروهای اوکراینی همچنین نیروهای چاد، نیجر و بورکینافاسو را آموزش داده‌اند، در حالی که چندین متخصص در سودان نیز عملیات کرده‌اند.
سازمان اطلاعات اوکراین می‌گوید این اعزام‌ها با هدف فشار آوردن به روسیه در خارج از کشور و تبدیل تخصص اوکراین در پهپادها به یک «ابزار سیاست خارجی» انجام شده است.
نیروهای اوکراینی در سال جاری میلادی، هنگام تصرف کیدال توسط شورشیان توآرگ، به آن‌ها کمک کردند؛ جایی که نیروهای شورشی و وابسته به القاعده، نیروهای سپاه آفریقای روسیه را به عقب‌نشینی واداشتند.
نیروهای اوکراینی همکاری خود با توآرگ‌ها را عملیاتی و نه ایدئولوژیک توصیف کردند و یک منبع اطلاعاتی گفت: «وقتی توسط همان احمق‌ها مورد حمله قرار می‌گیرید، تفاوت‌های ایدئولوژیک در پس‌زمینه محو می‌شوند.»
اوکراین همچنین از اواخر سال ۲۰۲۵، اپراتورهای پهپادهای دریایی را در شمال غربی لیبی مستقر نگه داشته است. یک اپراتور گفت که یگان او از پایگاه نظامی بین‌المللی در مصراته برای انجام حملات علیه «ناوگان سایه» روسیه که از تحریم‌ها فرار می‌کند استفاده می‌کند و در عین حال نیروهای محلی را آموزش می‌دهد. یک پهپاد دریایی انفجاری اوکراینی از دست اپراتورهایش خارج شد و در سال جاری میلادی به سمت یونان هدایت شد که باعث اعتراض آتن و عذرخواهی کییف شد.
اوکراین همچنین تیم‌هایی را به حداقل ۵ کشور خاورمیانه اعزام کرد تا در طول جنگ، آموزش سرنگون کردن پهپادهای شاهد ایرانی را ارائه دهند.
مسئولان اوکراین مأموریت‌های خارجی را هم به عنوان راهی برای تضعیف روسیه در هر جایی که فعالیت می‌کند و هم به عنوان فرصتی برای آزمایش فناوری پهپاد اوکراین در شرایط میدان نبرد مختلف، از گرمای شدید و گرد و غبار ساحل در آفریقا تا عملیات دریایی در مدیترانه، معرفی می‌کنند.</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/20834" target="_blank">📅 20:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20833">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ut1ztymxdWyhCzFSi6p-53WjUO2fE0addgT9lgHvCkdWuD_-e9_gzaDrepNDDIEY6AV8SB0k0MxtJkLwlpUzkVrFSJD8ZrNT7ZbYSslitx2B4WMIR5_GUt8dMwJIt_DrIQ0i8YAa2X8JO38c2gv4FhIzYz8HRcP7ZNUm60EwGdjXxjJoG811HJMQjYkueRL0c4IccHp1boNeF6B8QXX6DKKdO31FliHhazYsm99DuuvF4n5pV7JYwV9u4tX8_EZVpXbmoT74VwwaTTbTs1wo8XwkAgkZuQ-9_vDRDrrNFKG0NRMxxcjRF4_utF6IJBTOiDqmPK8rgDzSRZ-tsA2MHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید فاکستان به حمله موشکی در صورت دخالت نظامی در یمن</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/20833" target="_blank">📅 19:49 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20832">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">احتمال اینکه کل داستان جنگ یمن در روزهای اخیر یک تله برای حوثی ها باشد وجود دارد…  توضیح خواهم داد.</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SBoxxx/20832" target="_blank">📅 17:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20831">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">مدتی است به صورت آشکار و بی پرده، صحبت از لزوم ساخت سلاح هسته ای ایران از سوی مقامات کلان جمهوری اسلامی مطرح می‌شود</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SBoxxx/20831" target="_blank">📅 15:36 · 21 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
