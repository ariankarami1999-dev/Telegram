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
<img src="https://cdn1.telesco.pe/file/d7VYk6nUa8TQ0QVBUK1mF0ASq0PxFwKO0GX8z-gax6Q2P-Hb7GHISTOKpZJ7YGsSmfY96EhH3rHqWQWKiPuhxRI5wFOgMYDBzpYXvHlY_PzqFRRT3OoSA7uOiFOYOmZ2Uf9AJnYWVbYMJt0akaPxYmGw3hTOjWkjIYEROoWlEe-trDR7zXVu5phztcB8gZHbXt7qIdXRlVb57Mcrl8iit9IJIpsMjpz8z5Lun_OHyXNvaKd1OIiDR0SAQqd-z-SPOaTeQt5eX7nMvxcy5VfPZTak9MsrQY0Slhxz15FIGCm5VTeRzICj6UTlLDddzGwFpfnHRzRtNu4NaHX_uWyKFQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 163K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 درود! متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی می‌کنم به شما هم یاد بدم اگر به دردتون بخوره =)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 21:14:30</div>
<hr>

<div class="tg-post" id="msg-3761">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">Valid-08-June-MatinSenPaii.txt</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/3761" target="_blank">📅 16:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3760">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/67cf13d855.webm?token=Vr_p4UrPQZisqpKios913LmuunJnNb86zfFyDkI-sycnoc8ciaMGeNQHnsiom9-JD8ji8vZ3iKO8f67uebaj6SuRGDLXrdU9_rRMLGvqzmfF71bZl_aTMtAdg5GNqDd6Nj_ZkZ4MrW-9krODDNvXSxBgPvrk8FwYXNtEfeuXimTkBu_9DapFmOpNst-Ble_KEyV_csiWnFkoH1MBv5DwvaOrPzD0iFmL-hOb38mPRZ6NkjppQhlTqkaFIH1gNLvnZKxsLxf8biLoC30UgMlez530PtPbwTjMPKVU7GSjkZkS6EAEVs045WZNEgM_SMfz68WjxmtrqKzRoaOMwcjk8w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/67cf13d855.webm?token=Vr_p4UrPQZisqpKios913LmuunJnNb86zfFyDkI-sycnoc8ciaMGeNQHnsiom9-JD8ji8vZ3iKO8f67uebaj6SuRGDLXrdU9_rRMLGvqzmfF71bZl_aTMtAdg5GNqDd6Nj_ZkZ4MrW-9krODDNvXSxBgPvrk8FwYXNtEfeuXimTkBu_9DapFmOpNst-Ble_KEyV_csiWnFkoH1MBv5DwvaOrPzD0iFmL-hOb38mPRZ6NkjppQhlTqkaFIH1gNLvnZKxsLxf8biLoC30UgMlez530PtPbwTjMPKVU7GSjkZkS6EAEVs045WZNEgM_SMfz68WjxmtrqKzRoaOMwcjk8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/3760" target="_blank">📅 15:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3759">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Valid-08-June-MatinSenPaii.txt</div>
  <div class="tg-doc-extra">9.3 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3759" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اینها 688 تا ریزالوری هستن که Valid بودن توی دوره‌ی قطعی برای من، از اون 5800 تا ریزالور ویدئوی WhiteDNS</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/3759" target="_blank">📅 15:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3758">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-poll">
<h4>📊 دوستانی که سرور دارید، دیتاسنترای ایرانتون...</h4>
<ul>
<li>✓ اصلا وصل نشده بود هنوز اینترنتش</li>
<li>✓ وصل شده بود، الان قطع شد</li>
<li>✓ وصل شده بود و هنوز وصله</li>
<li>✓ سرور ندارم، دیدن نتایج</li>
</ul>
</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/MatinSenPaii/3758" target="_blank">📅 13:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3757">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ترجیحا هیچ VPNای نخرید دوستان. هیچ تضمینی نیست که اگر اینترنت قطع بشه هم اونا وصل بمونن یا نه. مثل اوایل جنگ که خیلیا اسکم شدن
همون هزینه رو بذارید whitedns راه بندازید</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/MatinSenPaii/3757" target="_blank">📅 12:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3756">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">هر پنج دقیقه میرم یه پینگ میگیرم ببینم وضعیت چیه
روانیمون کردن</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/MatinSenPaii/3756" target="_blank">📅 12:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3755">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اینکه هنوز اینترنت قطع نشده جای تعجب داره به خدا</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/MatinSenPaii/3755" target="_blank">📅 12:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3754">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">مجددا تأکید می‌کنم که سرورهای عمومی سرعت به شدت پایینی دارن مخصوصا توی محدودیت‌های شدید و بسته شدن ریزالورها. تمام تلاش رو بذارید روی راه‌اندازی
سرور+دامنه شخصی</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/MatinSenPaii/3754" target="_blank">📅 11:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3753">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">سرورهای عمومی MasterDns(با کلاینت WhiteDNS):
1-
https://t.me/Masir_Sefid/612</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/MatinSenPaii/3753" target="_blank">📅 09:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3752">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PyHBOVssHPV_kxZypCmhes70amG_2BmW98Eo6MKx45nhrZZZD8e_7YYdDTfZK89Tlaouarrtu1jANHXDLq2bm9Chd6J2pr3Vb-l_JGrIi-r241MYHpolpOFE6W4w8yke_sMigknsca7baVnP0nv0a_j4u4fvEkANqmsIwCmiqln5EyC4tQfwujJv4RiUaNq2XeVonJIcIbFGWKpgrF1oBApvAKKOHFs_0oFQPS6JBuwHfcM9cc8pRnix2n2FC64ICM7u58_QWtro4PPlX8EsnXgT7sh7w-2xk0ALLpVyMZM7p1vk4REUWgSprIZiYQ4lVtAyNUKYD-bYvKE7AIZsyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب همونی شد که فکر می‌کردیم. جنگی در کار نیست انگار تا بعد از جام جهانی. فعلا اینترنت داریم</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/MatinSenPaii/3752" target="_blank">📅 08:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3751">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">خب همونی شد که فکر می‌کردیم. جنگی در کار نیست انگار تا بعد از جام جهانی. فعلا اینترنت داریم</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/MatinSenPaii/3751" target="_blank">📅 08:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3750">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">دوستان دامین سالم این شکلیه. نه اینکه از ۵۸۰۰ تا بهتون ۴ تا valid بده</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/MatinSenPaii/3750" target="_blank">📅 00:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3749">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fsbWqPe3amM1qhWXqz1OWYcXg8qyoVPC3Qf2e9xWlUpA3kT2kr-fllWR5hLhQgHmUfIvJXOUQZEMAg7DHEcxx5miW005vnRbVtY4K-VFcFzouDqPhu1l0LOt63cwRqHfsb3tjqLpZDZqrLk9T27Mfe4P1EjG4aH5Q894zaLmufcjRXL2IfEAxZoI2PxXj2zOtBcUBofNY0auYt49Q__AGAl1cA11u9YFUY77lE1IqFK0SyPuirmm6r5D8Z1LxqeAyZ2iOwVkqqiZFK7qOT-ifKLJ6CNNLGoNQ90N835cq7MBucoILHqHv494ch3gsmjtFj8W355veyfJPr7CqkqLSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان دامین سالم این شکلیه. نه اینکه از ۵۸۰۰ تا بهتون ۴ تا valid بده</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/MatinSenPaii/3749" target="_blank">📅 00:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3748">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-poll">
<h4>📊 سرعت اینترنتتون؟</h4>
<ul>
<li>✓ تفاوتی نکرده</li>
<li>✓ یه کم کندی حس میکنم</li>
<li>✓ تمام کانفیگا از کار افتاده و نمیتونم به هیچی وصل بشم</li>
</ul>
</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/MatinSenPaii/3748" target="_blank">📅 23:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3746">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">Matin SenPai
pinned «
دوستان با این اوصاف حمله‌ی پیش‌دستانه WhiteDNS+Master راه بندازید که هر لحظه ممکنه اینترنت رو قطع کنن متأسفانه. توی ویدئو آموزش خرید سرور و دامنه و راه‌اندازی و تانل کردن کل سیستم و راه‌اندازی روی گوشی و سیستم هست کامل: https://youtu.be/6Pm7kNQb3mo سر هر تحرک…
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3746" target="_blank">📅 23:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3745">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/MatinSenPaii/3745" target="_blank">📅 23:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3744">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">تا حالا حمله‌ی پیش‌دستانه تجربه نکردیم. اگر منطقی باشه، اینترنت به جای قطع شدن باید قوی‌تر بشه</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/MatinSenPaii/3744" target="_blank">📅 23:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3743">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دوستان با این اوصاف حمله‌ی پیش‌دستانه WhiteDNS+Master راه بندازید که هر لحظه ممکنه اینترنت رو قطع کنن متأسفانه.
توی ویدئو آموزش خرید سرور و دامنه و راه‌اندازی و تانل کردن کل سیستم و راه‌اندازی روی گوشی و سیستم هست کامل:
https://youtu.be/6Pm7kNQb3mo
سر هر تحرک نظامی و موشک مجبورم این حرفو بزنم چون احتمالش هست واقعا هر لحظه</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/MatinSenPaii/3743" target="_blank">📅 23:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3742">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">تغییرات WhiteDNS Wizard v1.1.0
- خطای ACME و DNS بهتر تشخیص داده می‌شود.
- قبل از ساخت SSL، برنامه چک می‌کند دامنه واقعا روی Cloudflare فعال و درست تنظیم شده باشد.
- پیام‌های خطا واضح‌تر شده‌اند و کاربر بهتر می‌فهمد مشکل از توکن، دامنه یا DNS است.
- آموزش دسترسی‌های Cloudflare در README کامل‌تر شده.
- Reality XHTTP با Reality TCP Vision جایگزین شد.
- Reality حالا از
xtls-rprx-vision
استفاده می‌کند.
- انتخاب SNI برای Reality امن‌تر و پایدارتر شده.
- مسیر نصب روی سرور از
/opt
به
/var/lib/whitedns
منتقل شد تا روی VPSهای بیشتری بدون مشکل کار کند.
- مشکل ساخت فایل Docker Compose روی بعضی سرورها رفع شد.
- نصب Docker Compose Plugin روی سیستم‌عامل‌های مختلف بهتر شده.
- بیلدهای GitHub Release سریع‌تر شده‌اند و به صورت موازی ساخته می‌شوند.
- چند مشکل مربوط به مسیر فایل‌ها، ریستور، تست‌ها و آپلود فایل‌ها رفع شد.
https://github.com/iampedii/WhiteDNS-Wizard/releases/tag/v1.1.0</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/MatinSenPaii/3742" target="_blank">📅 21:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3741">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">یه جمله‌ی مشترک که از افرادی که پایتون اولین زبان برنامه‌نویسیشون بوده و بعد از اون رفتن سراغ یه زبان دیگه(علی‌الحصوص
زبان‌های کامپایلری
) زیاد شنیدم، این بوده که تازه با یاد گرفتن یه زبان جدید فهمیدن برنامه‌نویسی چیه. و درک و قدرت حل مسئله‌شون اونجا بوده که رشد کرده. علتش برام جالبه</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/MatinSenPaii/3741" target="_blank">📅 20:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3740">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">این پنل هم دیدم بچه‌ها زیاد باهاش ساخته بودن vpn روی کلودفلر. یه تست بکنید https://github.com/IRNova/Nova-Proxy</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/MatinSenPaii/3740" target="_blank">📅 17:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3739">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">این پنل هم دیدم بچه‌ها زیاد باهاش ساخته بودن vpn روی کلودفلر. یه تست بکنید
https://github.com/IRNova/Nova-Proxy</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/MatinSenPaii/3739" target="_blank">📅 15:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3738">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمسیر سفید🕊</strong></div>
<div class="tg-text">ساب لینک
مخصوص تمامی اپراتور ها نامحدود
❤️
✔️
اپدیت کنین ساب رو اگه نتونستین اضافه کنین ساب رو کافیه لینکو توی مرورگر بزنید بالا میاد و کانفیگا رو کپی کنید
⚡️
لینک ساب دائمی کانفیگ ها
:
https://raw.githubusercontent.com/masir-sefid/Sub/main/@Masir_Sefid.txt
⚡️
توی تمامی کلاینت ها به جز npv میتونین استفاده کنین پینگ نگیرین وصله
🟢
نحوه ی اضافه کردن ساب لینک با اپدیت خودکار
⭐️
پروکسی 1
|
پروکسی 2
|
پروکسی 3
⭐️
دونیت برای کمک به ادامه دادن این مسیر
❤️
🪐
Channel |
@Masir_Sefid
| کانال
🪐</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/MatinSenPaii/3738" target="_blank">📅 11:19 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3737">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromیـ بـ خـ(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZiWAhknzRmr0uRYCZRxi6kvrkdA4-13wo4XNE4A-nhK8jWysno3Sn2tYSNsXvFto6hB-E30pnlVxDlgn2MkxqdWFrk-Gk_jHLG4Ksxdy1LJ9uGSozfLXXIbH--vssFr1GTlVmHdlCvlWeACfzIIna5GnBzrVTvEyLHBXgU1B-xgPYHbKY3bqoHmwyu-D9mG_LCvS_-Kc4Y3UtkXjBztfNIVqt1yzo5qkzKt5eQAzO_utCMAQeIe6fHuXR2oJjSy5ynpvm_tGFUxeJqqTsnyhoUuWYaODolpCQSTLfwTjmcY79noF8CtXnkV3SHVKjAMDxby8Zzed8bIHMd1BK_PMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه نهان
🍷
پنلی بر بستر
#کلودفلر
با کلی قابلیت به صورت رایگان و تنها با دادن ip واسه خودتون یا خانواده فیلترشکن بسازید...
ویژگی های این پنل:
✅
⭐
محدودیت حجم گذاشت
🗓
تاریخ انقضا تعیین کرد
🚫
دسترسی رو قطع کرد
✅
دوباره فعالش کرد
❗️
مصرفش رو دید
و همه اینا بدون دست زدن به مستقیم به Worker یا KV.
‏یه سری امکانات مدیریتی هم داره که بعد از مدتی استفاده واقعاً به درد می‌خورن:
⚡️
داشبورد مصرف
☁️
Cloudflare Analytics
🔔
نوتیف با بات تلگرام
💾
Backup / Restore
و چندتا ابزار دیگه که کم‌کم بیشتر میشن.
لینک خود پروژه:
https://github.com/itsyebekhe/nahan
@yebekhe
👑</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/MatinSenPaii/3737" target="_blank">📅 08:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3736">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🍷
یه سری نکات رو بگم در مورد bpb:  کانفیگ ممکنه پینگ نده واستون ولی کار کنه الویت رو پینگ نزارید  داخل تنظیمات اگر مشکلی بود به جای chrome از firefox استفاده کنید  اگر اینترنت شما 8.8.8.8 کار نمیکنه یا اختلال داره سعی کنید از dns زیر استفاده کنید:(کمترین اختلال…</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/MatinSenPaii/3736" target="_blank">📅 01:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3735">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet(امیرپارسا گودمن)</strong></div>
<div class="tg-text">☠️
آموزش ساده آپدیت پنل BPB به آخرین نسخه  نکته: همونطور که توی ویدئو گفتم این صرفا آموزش آپدیته و هنوز نسخه‌ی استیبل نیومده اما می‌تونید استفاده کنید از ورژن‌های Pre-release
⚡️
لینک سایت کلودفلر: https://dash.cloudflare.com/ لینک پروژه‌ی  BPB برای دانلود فایل…</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/MatinSenPaii/3735" target="_blank">📅 01:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3734">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‏نسخه‌ 4.2.2 پنل BPB منتشر شد
🕶️
طبق گفته‌ی
برنامه‌نویس پروژه
، این نسخه مشکلاتی که از سمت کلادفلر بودن رو برطرف کرده
🔁
اگر دارید پنل جدید باهاش می‌سازید هیچ کار اضافه‌تری نیاز نیست، ولی اگر آپدیت می‌کنید باید همه‌ی ساب‌ها رو آپدیت کنید و اگر دستی توی داشبورد مقدار compatibility date رو تغییر داده بودید، بذارید روی جدیدترین تاریخ
طبق ویدئویی که برای آپدیت دادم
📆
تغییرات این نسخه:
1- بخش جدید External Raw configs:
میتونید ساب و کانفیگای شخصیتون رو اضافه کنید که همه‌شون به ساب Raw اضافه می‌شن
💪
2- بخش UpStream اضافه شده که می‌تونید به طور مثال
127.0.0.1:40443
رو به عنوان آیپی و پورت دیفالت بذارید(برای اسپوف) که به ساب Normal و Raw اضافه میشه و دیگه نیازی نیست دستی ویرایش کنید
💪
3- تغییرات جدید هسته‌ی Xray اعمال شده که حتما باید کلاینتاتون(V2rayNG یا هر کلاینتی استفاده می‌کنید) آخرین نسخه رو داشته باشه
😎
جزئیات کامل تغییرات رو اینجا بخونید:
https://github.com/bia-pain-bache/BPB-Worker-Panel/releases/tag/v4.2.2
آموزش ویدئویی آپدیت از نسخه قدیمی به جدید:
https://t.me/MatinSenPaii/3732
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/MatinSenPaii/3734" target="_blank">📅 00:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3733">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ub278NEc3_jkVp76FeAeHoHjnH1Sssw-YExaPt0Tm-TVGFrjXBgUkwSJp3v5L0fW_tStVdQ_WtfA6tyHfqsYJWc_RxhQB8DpLQnrf3xNe-AnhAZkQMFFYhSHgFH1z6qfUxy4cQ1WfVpDnq2JeO2K7vpxjlVJuMWOQhVg6_XvKVDO9zEo3Y4heWZshFaCxCWDccHrE1iVfhAG4PCGsFpPQFnBvGJiSGWdbcIdrepWn9hO1ffKd7mI_EUAasM6zd_y90rNsLBT_bkQISqc3YUxDcJnVsreAe8VeECtrXBAas1cbllV35jmc2tQjTfQffgOmQxXbd9ocDpbY3eISqpYJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انگار دیسلایک اضافه کردن به توییتر</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/MatinSenPaii/3733" target="_blank">📅 20:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3732">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">☠️
آموزش ساده آپدیت پنل BPB به آخرین نسخه
نکته: همونطور که توی ویدئو گفتم این صرفا آموزش آپدیته و هنوز نسخه‌ی استیبل نیومده اما می‌تونید استفاده کنید از ورژن‌های Pre-release
⚡️
لینک سایت کلودفلر:
https://dash.cloudflare.com/
لینک پروژه‌ی  BPB برای دانلود فایل ورکر:
https://github.com/bia-pain-bache/BPB-Worker-Panel/releases
⭐️
توی این ویدئو بهتون یاد میدم که چه شکلی می‌تونید پنل BPB رو آپدیت کنید
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
قبلش باید این شکلی یکی ساخته باشین:
https://youtu.be/_aXy8wwyRG8
✉️
تماشا در تلگرام
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/MatinSenPaii/3732" target="_blank">📅 16:43 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3731">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🔥
1500 کانفیگ جدید به ساب WhiteDNS اضافه شد
.
همون ساب های قبلی رو رفرش کنید.
⬅️
آموزش استفاده از FlClash
⬅️
آموزش استفاده از Clash Party
ممنون از همراهی شما
🤍</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/MatinSenPaii/3731" target="_blank">📅 15:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3730">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">⚠️
Confirmed: Metrics show a major disruption to internet connectivity in Pakistan-administered Azad Jammu and Kashmir.</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/MatinSenPaii/3730" target="_blank">📅 13:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3729">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHaoodi Senpai</strong></div>
<div class="tg-text">یک سری بحث و احتمال هست که یوتیوب فیلترش برداشته بشه، همون‌طور که گویا برای یک سری شده الان هم (البته مشخص نیست اختلاله یا واقعا داره رفع فیلتر میشه).
اینکه حقی که ازمون گرفتن رو بدن هنر نیست، ولی خب واقعا خوب میشه اگه این اتفاق بیفته و مردم همه بتونن دسترسی داشته باشن
♥️
همون‌طور که
قبلاً هم بارها گفتم
، ما یوتیوبر بی خانمان هم بشیم مهم نیست، مهم دسترسی درست هست و آزاد برای همه هستش.
اون یوتوبر بی‌شرفی که ناراحت میشه از آزاد شدن دسترسی هم بنظرم هرچه سریعتر آرک تمرینی نفس نکشیدن رو شروع بکنه
🫵🏻</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/MatinSenPaii/3729" target="_blank">📅 12:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3728">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">مراقب باشید سرور ۱۲۸ مگابایت رم و بدون ipv4 و اینا نخرید دوستان
😂
اونا رو هیچ کاریشون نمی‌تونید بکنید</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/MatinSenPaii/3728" target="_blank">📅 12:13 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3727">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">یکی از دوستان توییتر(ixAbolfazl)، دیشب یه سایت معرفی کردش برای پیدا کردن ارزون‌ترین سرورهای مجازی یه سریاش قیمت سالیانه‌شون کلا 2-3 دلاره. در این حد و کریپتو هم قبول میکنن مجدد یه سریا  آدرس: serverhunter.com</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/MatinSenPaii/3727" target="_blank">📅 11:58 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3726">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rUUKOQU9PDf_hc63zlwSRw309ssNZvGpplLKutusIHrbXrR7ryWYWhkzmui_Dx39r4qlYpIRbhHQAmI-yM-fgV36aDzqVaQvP5AfyQIA4dHqLf53_er63gbQ5RdHWBHmXq3WxNk39yGEToeRkrYql4Hvq7W5MoHDpK0eG0BjeqI8aFwB1SNw27-vwGVy0sCXxkDsPY98_PCzZZfJ4qNIyYX966u2g31MVr3vOXiDo0k1-uB-5khWy5Rx4dcUnBOuDYNWibig6Vkw0-c0FKfwTD_mPs4a3URSvx9ne60GqFbYbp7xznP47oyhnXl5RcoZWxQY4egf2On5mDyJ56qsMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از دوستان توییتر(
ixAbolfazl
)، دیشب یه سایت معرفی کردش برای پیدا کردن ارزون‌ترین سرورهای مجازی
یه سریاش قیمت سالیانه‌شون کلا 2-3 دلاره. در این حد
و کریپتو هم قبول میکنن مجدد یه سریا
آدرس:
serverhunter.com</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/MatinSenPaii/3726" target="_blank">📅 08:07 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3724">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qORIVZk8tx3z4V78fY2m6ytxVHtEGYjwDuixF5oSQ4keplx3zDnDLxsSCIU4cJAIUYUsx1G0huF9cFDuFLvUghL0ApQFoOn0sEN3GGQs5HKV_Biy4V6yo94vQWH_IXrclVFlb0TXqSuTreyFHwXfOs96qAb40IpECVJdKkrKfXQ28K_p7vbaARfqSec8uKWsDoy1ry3NpX15pWskyDPqSmM743Tbjh_qX8DZmz3Y9sNpKyGxwNMJZWLUv3WM3TRKlgeUU-5rEVnDTO8HptCJKNStIpY88QTZRGcQb_HEPKSJvwtSKsJbFUZAU3TWHMl3J-sQiX79PpqV1ByKncM2zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qax7ISTyj_vbHGyn6JE_KS25BYD0yKwyjFvwiPOdJ132o3-NdTzxqrFW_VYf6eKhlfLbL2DQ24Q2t4Q3xT4q_y_c7PsskSI8faxZ4C8ZuczvIh7FsLjw3NubsI93CkdenYNBlaTwAKB6eZU_ePgBbPJ7-qAupsNkkUYNuBB_CWjek5SJ3xry1fzZ6RKEbfb6ZtPK2M7vwB1kT_GEwdnGicIFdiVLyBcLu7Jpm4TavU5xEIeY0gbRGC1AfffiBH9YlHGasUvGiMAAzx-Zeq7eogVSasvDnxWpx4kDZL18fTgJ1Xtv2dxjqp9N2ZwQF077VJqz1EIVAb2zUxlwYom6AQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">والا برای من هیچکدوم روی ایرانسل و همراه اول نمیان
یه سری شایعه شده بود که میخوان یوتوب رو رفع فیلتر کنن
اما خب بازیشونه دیگه. سرگرم کردن ملت</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/MatinSenPaii/3724" target="_blank">📅 02:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3723">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lrVpK5mItahJV7TyK65pmEdM_frcPxEULFW831xi461-WMqXN05qtCd11hrD4vy_JE3E10pVwBOMour9fsK1ZxFJH_yTMnxDP_Vm-za33MBf2wmniKydbF89jg6fBL5W16qyTM9Fxye5FjEaCPg4e17ueOiC1F2lVxlh5XduafVaOUGZZoi_KhXj_Raz4JQfjONDiSz1zEImKLycONpmwKX3kdvs66euFsGNcCuBucyRBMbBhKp1vRE4ne3duat8pwg59isMgrqveAMjN5eb7Q5Ab3xhtV2D52FbRoSh1SAHFBNPB2QkFiCzoaNQHLugTOqqemU_cOuasXgxe_0UKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای شما هم این شکلی شده بچه‌ها؟ با لایک و دیسلایک بگید
شنیدم این رو چند بار از سر شب</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/MatinSenPaii/3723" target="_blank">📅 02:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3716">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">senpaiscanner-darwin-amd64</div>
  <div class="tg-doc-extra">31.9 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/3716" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بفرمایید تست کنید. ورژن 0.6.0</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/MatinSenPaii/3716" target="_blank">📅 02:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3715">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WZX8o_pbhJ4d-VFJh9yhOfcJPTbm10YCgEeYkxomYr5wKiWVWay8dXcuTLLXmkRO2QLbhSLKzEMZGFhSJ-1_Lsm8Jb1o504nhusOg5j_uPqeaNv4j9OVVB3z8f1JjrKsdDz3B2z-_bADpcWR4xGkSz0ZYYBOm2-66-RD-mcJq4UN7yxKEMbMrq-Bfw8BrXMxcwbwG_k8dwjosyfInWIQH1OoM-3g8cOIe7w5ilmiReZe1RNvPo4uGIIO0UcT0EdhgrK2etXJD7gzTRXHAm-ejB77TwK-BMQhpFWVi5QqIpWbrolTDfxbL-pGWGfsnSWD7GrulWZghsUvIfalX5YAMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشکل بزرگ اسکن روی اینترنت سیمکارت هم حل شد</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/MatinSenPaii/3715" target="_blank">📅 01:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3714">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">مشکل بزرگ اسکن روی اینترنت سیمکارت هم حل شد</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/MatinSenPaii/3714" target="_blank">📅 00:54 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3713">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c5Z35R4fM3wZPlX4CeJsdAtt9WK4ovcvHvt_oBCiqaxP2gPYtiRkuhbt6syT9RORFz-hDuamczBmQUJB6GbrBcWpHSJV6S20wG9II98dH0khs5zB3F3B0EZ1uUAybPc3NQWn4_y6pJF3GbImIYLA8r0Mi6XYyuhsCVYVDLbT9WJm_uumNCMY7un9F4CvWrVqLaDPIkmSEoy6X_hfqlfcGolbrQvQDcY6PfYerD7mp4Y1vxvkriXvsMRfOsHsUc4QgNoXA_ywBbw4-VmF6lEq_def2OR_BV5pdpG6COyU3EvuPF9LsroYa58DjFTmrm2C4QN-bg1SQj9tdKQZN61Itg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان این رو بگم توی ورژن جدید هسته‌ی ایکس ری، حتما باید Allow Insecure رو False بذارید توی کانفیگ وگرنه ارور میده</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/MatinSenPaii/3713" target="_blank">📅 00:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3712">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">یه کار جالبی یکی از بچه‌ها سر SenPaiScanner در آورده که واستون قرار میدم به زودی. PR های بقیه‌ی دوستان هم بررسی کردم و همه عالی بود و تأیید شد و رفت روی کد اصلی</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/MatinSenPaii/3712" target="_blank">📅 00:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3711">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">یه کار جالبی یکی از بچه‌ها سر SenPaiScanner در آورده که واستون قرار میدم به زودی. PR های بقیه‌ی دوستان هم بررسی کردم و همه عالی بود و تأیید شد و رفت روی کد اصلی</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/MatinSenPaii/3711" target="_blank">📅 00:02 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3710">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kwDLEMrbKF15gM4Jcf2qt9ruaX2F0j4hmOGC7iZN7L5N0B7dqZBtDd5XH0BxTvR_v659tuXcigileqrmC_yomOtBGONuFIw_sZJgwI95s8FGDFOp9RvEuE7zZ5xpoxf_axZDfrH--YbAI-HywFv1b1E6AmkFoG8JMHjaQKwrShnF5Zi3BFIO3dW-lJLRyTeijvWzBRGy62y_kEmDUdK_-FEQXfbaWWR2DWX90Oq_3dq0KN1e6xe5k2p09-2GHzb_-Wu4-1cvXbU4IBhhciTyO6xlVblLKIXea8g5GnwXntkh36x5Pu8U7rdt04cVhrvS82BmTkcKKp9hk8o99dlNBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرویس WhiteDNS-Wizard برای کسایی طراحی شده که سرور و دامنه خریدن، و حالا نمی‌دونن که با اینا چیکار بکنن
👍
این نرم‌افزار مولتی‌کراس پلتفرم تحت CLI اوپن سورس، از شما اطلاعات سرور و دامنه میگیره، به علاوه API-TOKEN کلودفلر، و برای شما صفر تا صد کار نصب پنل، گرفتن سرتیفیکیت و ssl و ... رو انجام میده. و این خروجی‌ها رو میده:
1- کانفیگ VLESS WS شخصی
2- کانفیگ REALITY-XHTTP شخصی
3- کانفیگ Hysteria2 شخصی
4- کانفیگ Shadowsocks شخصی
5- کانفیگ Tor vless ws
6- کانفیگ Tor Hysteria2
7- کانفیگ Tor direct
8- به زودی مستر و ... هم اضافه میشه
آموزشش رو هم داریم با آپدیت بعدی
گیتهاب:
https://github.com/iampedii/WhiteDNS-Wizard
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/MatinSenPaii/3710" target="_blank">📅 22:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3709">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QTDpXU4k9-ownRCg8ZJiMqNUaAd4TAyB8CvPRzweIs6IAYOrwkiTuEXvq_Dp58rwaufO7oS1jY0vQqQKAQuoNmHJnLX-fZgeg83iHULdOquq0X42Z4egswiT9pvYEy8pNZ9TT4azvhwxBm-8kMDItK_pHyQQwcjb3zKkaVVnbDottWM8higkfYCKar8J2Hci9DddBv064t89iDkf_Nd__KL-BNbXxlSTVk9OhderOegxbM-eGc7EoRYlEiNrpGxJ20S83coyCngQzU1WdP2MrYr7Glhfts1zWZIo7UCyyAFaUuT0kbQXPNVPkvWvUjQKvDv2IBs8qiW7iK8cdtS8Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">AzadiTunnel نسخه آیفون شیر و خورشید
👑
یک اپ iOS برای اتصال امن و پایدارتر، با تمرکز روی تجربه ساده، CDN Fronting، DNS هوشمند و تست اتصال.
📱
لینک مستقیم اپ استور:
https://apps.apple.com/ca/app/azaditunnel/id6776486891
منبع توییتر
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/MatinSenPaii/3709" target="_blank">📅 20:27 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3708">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ورژن جدید 4.2.0 BPB رو تست کنید بچه‌ها. سازنده‌ی عزیز روی مشکل Undefined کار کرد و درستش کرد. همینطور بخش Compatibility date رو نیازی نیست دست بزنید دیگه https://github.com/bia-pain-bache/BPB-Worker-Panel/releases/tag/v4.2.0</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/MatinSenPaii/3708" target="_blank">📅 18:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3707">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/twDiQSMg-_F8OHlyjlNKfYSujg-vTa3malCsX2CAZ9g4T5VIxheScov-fkdDES9KQwJm2-u41GiU-mSQpiUt-QKVh4Q1y7tLrhw_NYBpYHi_0EPKURS8ZvEiC7H6u76ZR3cQi_U39oO2I2Zn1GdVBC1tHre3KMAr5B985WwIWsjvP7NFmN4mWdjcYE4lFpxbaUOYGDBGzzGIcokKrGP_psoGPkVdgJjfg2itOteofJPcH1li-xb4HCxKnFZaT4J3kPUb070t0fsYoCShSN_G_aogRJx0_9s-VSj1nqoq18TFShGfiO8v3iEw5hHLnwHpVWESAldknHpFKARGA0VaJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏شرکت OpenAI ویژگی Dreaming رو برای حافظه ChatGPT معرفی کرد!
بالاخره بعد از مدت‌ها انتظار، OpenAI ویژگی خیلی مهمی به اسم Dreaming رو برای ChatGPT معرفی کرد. این آپدیت حافظه رو از حالت «یادآوری ساده» به یه سیستم هوشمند و پویا تبدیل کرده.
قبلاً چی بود؟
قبلاً ChatGPT چند تا نکته رو یادش می‌موند، ولی بعد از مدتی قدیمی و بی‌ربط می‌شد. مثلاً اگه بهش گفته بودی رژیم غذایی خاصی داری یا پروژه‌ای داری، بعد از چند هفته دیگه درست به یادش نمی‌اومد.
حالا با Dreaming چی شده؟
با این قابلیت ChatGPT تو پس‌زمینه (حتی وقتی باهاش حرف نمی‌زنی) همه چت‌هات رو بررسی می‌کنه، خلاصه می‌کنه، الگوها رو پیدا می‌کنه و حافظه‌ش رو همیشه تازه و به‌روز نگه می‌داره. انگار داره «رویا می‌بینه» و اطلاعات رو مرتب و هوشمندانه سازماندهی می‌کنه.
فایده‌های واقعی‌ش چیه؟
شخصی‌سازی خیلی بهتر: ترجیحاتت، علایقت، محدودیت‌هات و جزئیات زندگی‌ت رو خیلی دقیق‌تر به خاطر می‌سپاره. مثلاً اگه قبلاً گفتی عاشق عکاسی طبیعت هستی، دیگه پیشنهادهای generic نمی‌ده؛ مستقیم بهت ایده‌های مرتبط با سبک مورد علاقه‌ت می‌ده.
پروژه‌های طولانی: اگه روی یه پروژه چند ماهه کار می‌کنی (مثل نوشتن کتاب، راه‌اندازی بیزینس یا یادگیری زبان)، لازم نیست هر بار از اول توضیح بدی. ChatGPT زمینه کامل رو حفظ می‌کنه.
آپدیت خودکار: مثلاً اگه گفتی قراره به سفر بری، بعد از سفر خودش متوجه می‌شه و اطلاعات قدیمی رو پاک یا آپدیت می‌کنه.
کنترل کامل داری: می‌تونی حافظه رو ببینی، ویرایش کنی، بگی چی رو فراموش کنه یا چی رو حتماً یادش بمونه.
در کل، ChatGPT دیگه مثل یه دوست معمولی عمل می‌کنه که فقط حرفاتو گوش می‌ده (حتی این هم با ما دوست معمولیه!) حالا مثل یه دستیار واقعاً باهوش شده که تو جزئیات زندگی و کارتو درگیره و همیشه به‌روزه.
این ویژگی از امروز برای کاربران Plus و Pro در آمریکا فعال شده و به زودی برای بقیه کشورها و حتی کاربران معمولی هم می‌رسه.
لینک کامل توضیحات OpenAI:
https://openai.com/index/chatgpt-memory-dreaming/
✍️
Diego JR</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/MatinSenPaii/3707" target="_blank">📅 15:37 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3706">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ورژن جدید 4.2.0 BPB رو تست کنید بچه‌ها. سازنده‌ی عزیز روی مشکل Undefined کار کرد و درستش کرد. همینطور بخش Compatibility date رو نیازی نیست دست بزنید دیگه
https://github.com/bia-pain-bache/BPB-Worker-Panel/releases/tag/v4.2.0</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/MatinSenPaii/3706" target="_blank">📅 14:16 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3705">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fxaIM_PEuCT9YculmMitwsox1ZxPBt8b2NX429BRy-c9HU5Genp0_QG7x4wRvKPWQCYrd4pMllQTGwfC43lObGvfGvAid6D8DLdBixRwjhPSFnsMKnyAyWp31FVi-u67OyR17aTpAmZ0qd8UOdO51gSa1035c_f9cFSc0TewWM4y37B_WzFaXTfvZdgtRqDLb1vhAETtrWHtPBF0YDEmR77Nixz5P-T5Mz4yzF4L2q5QOUap59IAU_YknpTbNnVQpYyAAGipf7rbFlkQaWxBYLcobg8wtqz-qaPwz5LhIGEWxH4DARqT8_w3WL-qvE3cR8T6T9GMggho0iB5mGGgfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها اگر کانفیگ worker پینگ می‌ده اما درست وصل نمیشه تنظیمات مثل عکس قرار بدید fingerprint روی Firefox و Alpn روی http/1.1
یا اگر توی mahsang هستید Psiphon انتهای اتصال قرار بدید
✍️
🏴
Amin
🏴</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/MatinSenPaii/3705" target="_blank">📅 11:54 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3704">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">دوستان این رو بگم توی ورژن جدید هسته‌ی ایکس ری، حتما باید Allow Insecure رو False بذارید توی کانفیگ وگرنه ارور میده</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/MatinSenPaii/3704" target="_blank">📅 06:09 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3703">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bNstfohXfkwb_sh5wzse4eWwuqTm3Mb_mHXiQ0b0PgmSZOdY49WOqE9bvXS-OkbBeOdLvEzty8Xtq2mRMflPZo5jRQPo2oC5sN5qe9I1Ofo-BDRA5KF5ta6ceUgeTxJeCT3ramyx3eq2ihqnTUr8LghZEMEIdErHCPGhACO14cq5I3YaF0feNOJXoHy1NgZ_yhiZd_JpwTx9Owm9utPeFLo2bqctK9UhR54UBRVjA7Hhw2uEhNpIPT7s7_E9ttQ6GeJrQZvGgOCjAQBvJFF6Pv5zK3daRKEgO7yF7okKbCQqzQ1Hyqszu7bVaF2H9OmvCQ7CmfssU4eafoJax2pBbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به چند سرویس تحریمی مثل اسپاتیفای، گراک، کلاد و ... ربطی به آتش‌بس، توافق و رفع تحریم‌ها نداره و مربوط میشه به دستکاری شبکه توسط فیلترچی و عبور ترافیک از شبکه آذربایجان!</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/MatinSenPaii/3703" target="_blank">📅 23:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3702">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M6ympGIGWyXBBVnv3Cg41qAsdBwcZFiQcTQ6lmEkrS094JblNcQ3S_YWAy3P7eey5ACq9U5PffdoXdKS4QB9GzfLUDfdFARzsjou5QKRrR9_il7-yRcX5lSfWMt0z2oxvOC4DVaJ_hdR7bNzl7icbi3bmRLIUjqHW0MmqQspUD4U4w1DmxpYnjSsRxFv8tXjBG-V6YGrtCF-7RmBUOEf01HhFFhCA355XNIeJPrSgrOP_Kt-1RW-oHc2hL80GnSBPdqushyWa4Z6Lli66Ka_lAaxldevOLPbuTlMQGip2xZ9HAsPoxe8PNHpvcac-zNuyrxLK8QcwQhQGH2VPiVcuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محدودیت کلودفلر(روزانه تقریبا ۶ گیگ) روی اکانت کلودفلر شماست. نه خود Worker
پس اگر می‌خواید این محدودیت بشه 12 گیگ، یه اتمیک میل جدید می‌سازید، یه اکانت کلودفلر جدید می‌سازید، و یه بار دیگه مراحل ساخت رو پیش میرید روی اکانت جدید</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/MatinSenPaii/3702" target="_blank">📅 23:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3701">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">📌
چند نکته کاربردی برای بهتر وصل شدن با FlClash در اندروید
یکی از کاربران WhiteDNS تجربه‌ی شخصی خودش را از کار با FlClash فرستاده که برای اتصال بهتر مؤثر بوده.
اگر با FlClash مشکل اتصال، آپدیت نشدن ساب، پینگ‌های عجیب یا ناپایداری دارید، این موارد را امتحان کنید.
━━━━━━━━━━━━━━
1️⃣
بعد از نصب، قبل از اضافه کردن ساب، Resourceها را آپدیت کنید
بعد از نصب FlClash، قبل از اینکه لینک سابسکریپشن را اضافه کنید، وارد این بخش شوید:
Tools → Resource
و تمام Resourceها را آپدیت کنید.
⚠️
نکته مهم:
طبق تجربه‌ی بعضی کاربران، اگر اول لینک ساب را اضافه کنید، ممکن است بعداً Resourceها درست آپدیت نشوند یا اپ رفتار عجیب نشان بدهد.
━━━━━━━━━━━━━━
2️⃣
تنظیمات Network
از بخش Network این موارد را بررسی کنید:
✅
گزینه‌ی DNS Hijack را فعال کنید.
❌
گزینه‌ی
Allow applications to bypass VPN
را غیرفعال کنید.
این کار کمک می‌کند برنامه‌ها ترافیک یا DNS را از بیرون VPN رد نکنند.
━━━━━━━━━━━━━━
3️⃣
تنظیمات دسترسی و اجرای پس‌زمینه
بعد از نصب وارد این مسیر شوید:
Tools → Advanced Configuration → On Demand
در این بخش، گزینه‌های مربوط به دسترسی‌ها را روی Authorized قرار دهید.
همچنین در تنظیمات باتری گوشی، برای FlClash حالت Battery Optimization را غیرفعال کنید تا اندروید برنامه را در پس‌زمینه نبندد.
━━━━━━━━━━━━━━
4️⃣
گوشی روی Power Saving نباشد
اگر گوشی روی حالت
Power Saving / Battery
Saver باشد، ممکن است اتصال ناپایدار شود یا برنامه در پس‌زمینه قطع شود.
برای استفاده بهتر از FlClash، هنگام اتصال، حالت Power Saving را خاموش کنید.
━━━━━━━━━━━━━━
5️⃣
تنظیمات DNS
از بخش DNS:
✅
گزینه‌ی Override DNS را فعال کنید.
🌍
گزینه‌ی GeoIP Code را روی IR قرار دهید.
بعد از این تغییرات، لینک ساب را اضافه کنید و تست پینگ بگیرید.
━━━━━━━━━━━━━━
6️⃣
اگر ساب آپدیت نمی‌شود، حذف و دوباره اضافه کنید
طبق تجربه‌ی بعضی کاربران، FlClash گاهی نشان می‌دهد که ساب آپدیت شده، اما در عمل لیست کانفیگ‌ها تغییر نکرده است.
اگر حس کردید ساب درست آپدیت نشده:
1. لینک ساب را حذف کنید.
2. دوباره همان لینک را اضافه کنید.
3. مجدد پینگ بگیرید و تست اتصال انجام دهید.
━━━━━━━━━━━━━━
7️⃣
در تب Auto کمی صبر کنید
طبق تجربه‌ی کاربر، بعد از حذف و اضافه کردن دوباره‌ی ساب و گرفتن پینگ در تب Auto، ممکن است اول فقط چند سرور پینگ بدهند و بقیه Timeout شوند.
اما بعد از اولین اتصال، FlClash ممکن است خودش شروع کند سرورها را دوباره بررسی کند و از بالای لیست Auto دونه‌دونه سرورها را تست کند تا به گزینه‌ی بهتر برسد.
یعنی ممکن است اول یک سرور اصلاً پینگ ندهد یا در لیست بالا نباشد، اما بعد از اولین اتصال، همان سرور یا سرورهای دیگر دوباره تست شوند و وصل شوند.
⏳
گاهی این روند کمی زمان می‌برد، پس اگر همان لحظه همه‌چیز Timeout بود، چند دقیقه صبر کنید و دوباره وضعیت را بررسی کنید.
━━━━━━━━━━━━━━
8️⃣
مرتب‌سازی سرورها بر اساس پینگ
برای اینکه سرورهایی که پینگ گرفته‌اند بالای لیست بیایند، روی سه‌نقطه بزنید و وارد این مسیر شوید:
⋮ → Settings → Sort → Delay
با این کار، سرورهایی که پینگ بهتری دارند بالاتر نمایش داده می‌شوند و انتخاب سرور راحت‌تر می‌شود.
━━━━━━━━━━━━━━
✅
ترتیب پیشنهادی بعد از نصب FlClash
1. نصب FlClash
2. آپدیت Resourceها از بخش Tools → Resource
3. فعال کردن DNS Hijack
4. غیرفعال کردن Allow applications to bypass VPN
5. فعال کردن Override DNS
6. تنظیم GeoIP Code روی IR
7. غیرفعال کردن Battery Optimization برای FlClash
8. خاموش بودن Power Saving گوشی
9. اضافه کردن لینک ساب
10. رفتن به تب Auto و گرفتن پینگ
11. تنظیم Sort روی Delay
12. اتصال و چند دقیقه صبر برای تست خودکار سرورها
━━━━━━━━━━━━━━
⚠️
این تنظیمات تضمینی نیست، چون شرایط اینترنت، اپراتور و گوشی‌ها متفاوت است؛ اما برای بعضی کاربران باعث اتصال بهتر و پایدارتر شده است.
🔗
لینک ساب WhiteDNS برای FlClash:
https://sub.whitedns.one/sub/mihomo.yaml
لینک ساب برای اپ های V2Ray
https://sub.whitedns.one/sub/base64.txt
📱
یا دسترسی ساب از گیتهاب
لینک ساب برای  Clash Party & Mi Clash & FLClash
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml
لینک ساب برای اپ های V2Ray
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/base64.txt</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/MatinSenPaii/3701" target="_blank">📅 20:31 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3700">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">😊
آموزش استفاده از Clash Party نسخه ویندوز در کانال یوتیوب WhiteDNS
🔥
کانال مارو Subscribe داشته باشید.
https://youtu.be/gMFH88yRghg</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/MatinSenPaii/3700" target="_blank">📅 20:31 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3699">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">این هم آموزش‌های مربوطه. از لینک ساب گیتهاب استفاده کنید</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/MatinSenPaii/3699" target="_blank">📅 20:31 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3698">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-poll">
<h4>📊 چرا نتونستید وصل بشید؟</h4>
<ul>
<li>✓ بلد نشدم وارد کنم</li>
<li>✓ لینک ساب رو زدم آپدیت نشد</li>
<li>✓ لینک ساب رو ژدم آپدیت هم شد، وصل نشد</li>
<li>✓ الکی دیسلایک زدم اصلا وارد نکردم</li>
</ul>
</div>
<div class="tg-text">تونستید به ساب جدید WhiteDNS وصل بشید؟</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/MatinSenPaii/3698" target="_blank">📅 20:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3696">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔥
لینک ساب جدید
https://sub.iampedi2.live/sub/mihomo.yaml
📱
یا دسترسی ساب از گیتهاب
لینک ساب برای  Clash Party & Mi Clash & FLClash
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/MatinSenPaii/3696" target="_blank">📅 19:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3695">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet(امیرپارسا گودمن)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">به یاد محمد جواد حضوری.npvt</div>
  <div class="tg-doc-extra">3.4 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/3695" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">💔
این کانفیگ رو به یاد محمدجواد حضوری عزیز که هم محلی من بود و دیگه پیش ما نیست میزارم تا یادش تا ابد در ذهن من و شما خواهد ماند...
به یادتیم پسر
💔
💔
💔
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/MatinSenPaii/3695" target="_blank">📅 13:38 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3694">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">😭
الان که همه‌چی فیلتر و بسته‌ست و فیلترنت داریم، یه مشکل کلاسیک ویندوز همه‌مونو کلافه کرده!</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/MatinSenPaii/3694" target="_blank">📅 12:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3693">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o5T_iw8n_NYvW3qbg-xqtN9RBAB-Emv7g2498bwMOEE-iEKs-AFYLeh4vXoeQz2hGtX5asBCqfnZVU3GfFQkn1JQSGWrNTPe_55aIrKyQyxJmqssHT4aUv1vQErC-jkbnEtqckEsYwczfy96pwCi1grogn_qQVjv0h_cXjGYaOoD2TqkjgwegQbB0v5NUFbRXiMeuPyhqFN3h0fIeEdcXoWXf64vtrpSz3Qc4ohUBLV0Snzji5z4hn8UtluSfI06EAtVE8kEv7jYBnsdi96qSzQvKH0wQMVkEV49KLP-bd2A-1HwzXHbkw2DHXYINr5YFKAqyqdWS4Vg3Gfm_FaPww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمیدونم چی باعث میشه یه سری دوستان ادب و نزاکت یادشون بره، ولی خب برای بقیه میگم. فکر کنم دو سه باری هم گفتم قبلا که برای مشکل سرعت آپلود متدهای پشت سی دی ان چه شخصی چه BPB و Edge:
1- فعالسازی Fragment (اون F بالای صفحه توی اپ MahsaNG با تنظیمات auto)
2- بردن کانفیگ پشت SNI-SPOOF</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/MatinSenPaii/3693" target="_blank">📅 09:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3692">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b2725e3a8.mp4?token=Uo20upVJ36ktV8S8gUgj6JsmOLEBw8BmrQj0hOupsGziSHBj7URRzOPAvTrxRwQDVMXq47wgQaHQ9NKyNI5jlzJ1cQmFGHotCW9xjIP-1YuUG98yowiSqeSLkupS2pV8Uc3sNh17yxp3BFvoKHbJMIC9E8rrX4X9n6Jxx9_8EMYLMfNYIVotshoBcgNqg7CmcCOktNfKYYlYufZzHJ-pOTsrDmGKOnKUS8wwblfeI1UBaRrewA_u9H429nT8kTnanvI1EdNOzNuSyMLYknfTMqB6LGsQizz2bE-8JclUQLqaeiegPpB6qe9MHXrBFfqDw4TRLKr2M_I9jjmCBxepeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b2725e3a8.mp4?token=Uo20upVJ36ktV8S8gUgj6JsmOLEBw8BmrQj0hOupsGziSHBj7URRzOPAvTrxRwQDVMXq47wgQaHQ9NKyNI5jlzJ1cQmFGHotCW9xjIP-1YuUG98yowiSqeSLkupS2pV8Uc3sNh17yxp3BFvoKHbJMIC9E8rrX4X9n6Jxx9_8EMYLMfNYIVotshoBcgNqg7CmcCOktNfKYYlYufZzHJ-pOTsrDmGKOnKUS8wwblfeI1UBaRrewA_u9H429nT8kTnanvI1EdNOzNuSyMLYknfTMqB6LGsQizz2bE-8JclUQLqaeiegPpB6qe9MHXrBFfqDw4TRLKr2M_I9jjmCBxepeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کمتر از یکساعت پیش مدل جدید تصویر ساز Reve 2.0 معرفی شد , این مدل با پیشی گرفتن از نانو بنانای دو، رتبه دوم رو در جدول مدل های تصویر ساز بعد از GPT بدست آورده
از سایت
Reve.com
‎ می‌تونید به صورت محدود و رایگان تستش کنید.
یادداشت تیم: «ما روشی نوین برای تولید و ویرایش هر نوع تصویر با استفاده از چیدمان‌های دقیق ابداع کرده‌ایم. برای نخستین بار، خلق تصاویری که گویی می‌توان آن‌ها را لمس کرد، امکان‌پذیر شده است.»
✍️
سگارو</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/MatinSenPaii/3692" target="_blank">📅 05:24 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3691">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">واقعا متوجه نمیشدم چرا مردم پول vpn میدن</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/MatinSenPaii/3691" target="_blank">📅 05:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3690">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">توی 12 دقیقه، با گوشی یا کامپیوترت بدون هیچ دانش فنی‌ای برای خودت سرور VLESS اختصاصی بساز!
🔥
توی این ویدئو، بهتون یاد دادم که چطوری از طریق وبسایت کلودفلر، پروژه BPB و پروژه BPB-ReCoder محدودیت‌های قبلی کلودفلر رو به راحتی دور بزنین و برای خودتون سابسکریپشن…</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/MatinSenPaii/3690" target="_blank">📅 05:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3689">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">از کامپیوتر فقط دکمه خاموش روشن کردنش رو بلدی؟ نگران نباش! من بهتون یاد میدم که چطور با دانش فنی بسیار پایین، بتونید برای خودتون و خانوادتون، بدون یک ریال هزینه، VPN بسازید!
🔥
هم برای IOS، هم برای اندروید، و هم برای دسکتاپ و مک  ربع ساعت وقت بذارید این ویدئو…</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/MatinSenPaii/3689" target="_blank">📅 05:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3688">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">یکی از دوستان این روش رو رفته بود برای مشکل اسکنر و برطرف شده بود این اشکال واسش:
متین جان برای مشکل
https://t.me/MatinSenPaii/3652
از این کد استفاده کنن دوستان
pkg install wget -y && pkg install unzip -y && wget https://uploadkon.ir/uploads/c86602_26senpaiscanner.zip && unzip c86602_26senpaiscanner.zip && cp senpaiscanner /data/data/com.termux/files/usr/bin/ && chmod +x /data/data/com.termux/files/usr/bin/senpaiscanner
بعد از اتمام کار
کافیه برای اجرا
senpaiscanner
رو بنویسن و اینتر بزنن
(توی نسخه ۵ اسکنرت)</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/MatinSenPaii/3688" target="_blank">📅 23:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3687">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">به مناسبت ۲۰ هزارتایی شدن، یوتوب هم ۱۲۰۰ دلار از کل درآمد این چند ماهم(که موفق نشده بودم بگیرمش سر مشکل ادسنس) رو خورد و با ادسنس چینج، کلا پروند همه‌اش رو
😂
عاشق این آمریکاییام</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/MatinSenPaii/3687" target="_blank">📅 22:52 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3686">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">به مناسبت ۲۰ هزارتایی شدن، یوتوب هم ۱۲۰۰ دلار از کل درآمد این چند ماهم(که موفق نشده بودم بگیرمش سر مشکل ادسنس) رو خورد و با ادسنس چینج، کلا پروند همه‌اش رو
😂
عاشق این آمریکاییام</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/MatinSenPaii/3686" target="_blank">📅 22:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3685">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OPVgeDjJ9tXj9_QT57Qz1quzmZ8P98dbEmgt5QeJtlzsKm-HPh_jotX25FqWkxknIfyrEzaZr7lDlwh_E2lSqVLddnxsL1Dyt2OEsnOl10ziZcZaQL011ZbOVNnefWwANfzZMj9ejiwJmgg1VnNCt72Js0MeEGeAlJveHmn1PjtKvDOoYBhXYpMO6TjnAYtsriocSXIVpatSuf3tgfp1mSGGL1B-UvUVA3FkGa6ESRwhsptiuoYsWLZ_lRcdf-_Q1SI6dEwS0VK8wAGvbltXJoSYz0HCqGY4EB_NXhTsMQzBd68WXnNrOakyQqLBTukoCtxwE_Vt7X56z50dv-SjhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عدده هیچوقت مهم نبوده و نیست. اما مناسبتیه که به خودم یادآوری کنم اهدافم رو. از 2021 که با یه گوشی و ذوق مسیرم رو عوض کردم و اومدم سراغ یوتوب، هدف والا و بلندمدت من، گذاشتن یه تأثیر مثبت روی جوونا و نوجوونای خوب وطنم بوده. کسایی که ارزشش رو دارن، عقاید و شخصیت درستی دارن، انسانیت سرمشق‌ـشونه و شرافتمندانه زندگی می‌کنن.
شاید یه جرقه‌ی امید توی این تاریکی.
شاید جلوگیری از خودکشی چندتا از برادرا و خواهرام.
شاید ایجاد شغل و ایده دادن و کمک بهشون.
توی این خراب شده، ما فقط همدیگه رو داریم.
ممنونم از تینا، پارتنر عزیزم. کسی بود که من رو از تاریکی بیرون کشید، و بهم امید زندگی داد.
پنج سال گذشت، و از مسیری که رفتم پشیمون نیستم.</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/MatinSenPaii/3685" target="_blank">📅 22:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3684">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">شما یه اپلیکیشن می‌بینید، یه لینک ساب می‌بینید، من ساعت‌ها و روزها زحمت و هزاران دلار هزینه از جیب شخصی بدون چشم‌داشت و تلاش شبانه‌روزی می‌بینم. هم از بچه‌های وایت‌دی‌ان‌اس، هم از بقیه‌ی دوستامون که برای اینترنت آزاد تلاش می‌کنن
✌️</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/MatinSenPaii/3684" target="_blank">📅 21:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3683">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">لینک ساب ها درست شدند
😃
🔗
لینک ساب WhiteDNS برای FlClash:
https://sub.whitedns.one/sub/mihomo.yaml
لینک ساب برای اپ های V2Ray
https://sub.whitedns.one/sub/base64.txt
📱
یا دسترسی ساب از گیتهاب
لینک ساب برای  Clash Party & Mi Clash & FLClash
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml
لینک ساب برای اپ های V2Ray
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/base64.txt</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/MatinSenPaii/3683" target="_blank">📅 20:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3682">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/3682" target="_blank">📅 19:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3681">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">الان که بهش نگاه می‌کنم، از دی‌ماه تا الان نزدیک ده سال گذشت...</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/MatinSenPaii/3681" target="_blank">📅 15:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3680">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l02U-qIZpuvE3JBB_22VKfAmf5TFnrBdwQFpOEjrBn1-A6em-HHB_s0Ip6eA3zIgZWOuJZ6mL5J1lLJ57UYOvPK6AWlc0lmRcJNJqFwDWE3s94w2Vw00icrWKuSWzXg3mBVQnXRZBAAIf8GHTAubTEndjOZtZhJzjeSIyCNJUzHy46G985TBq_LEW2IkUQN6Hij9rfUca0H-EM5G8LmX-R4bfeeTDNyK8A9t4E_m1wzS4faRvtFupOV5J5K9Aam3k9GPb3BzOPOIWeDZD-6ZYukHsVgimDGIgOK259wnDydWLHDhZVjvPy2y0IjgdngIp5zWnmCSaqBOqQ-RjlvzUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمام آموزش‌های مبنی بر اینترنت آزاد که من توی کانال یوتوبم منتشر کردم به علاوه‌ی توضیحات و اینکه توی چه شرایطی به چه دردی می‌خورن. از بالا به پایین، برای شرایط سخت‌تر معرفی می‌شن تا شرایط خاموشی کامل:
1- متد Paqet، ویژه‌ی شرایط الآن(کلودفلر و اینترنت بین‌الملل باز شده) واسه‌ی هر نتی(تبدیل سرعت اینترنت داغون به سرعت خدا)
مزایا: سرعت بالا و راه‌اندازی یک باره(هم مستقیم هم تانل)
معایب: نیاز به سرور داره، روش مستقیمش فقط روی سیستم میتونه ران بشه یا گوشی Root شده و تانلش مصرف داده‌اش ۴-۵ برابره
ویدئوی اول آموزش Paqet مستقیم:
https://youtu.be/q4BbgdhPm-w
ویدئوی دوم آموزش Paqet تانل:
https://youtu.be/nwpLOANv7VY
ویدئوی سوم آموزش Paqet با نصب آسان(اسکریپت سم):
https://youtu.be/QkGI8WoOtPc
2- متدهای بر پایه کلودفلر Workers، ویژه‌ی شرایط الآن(کلودفلر و اینترنت بین‌الملل باز شده) واسه‌ی اکثر اینترنتا به علاوه‌ی آیپی تمیز
مزایا: سرعت بالا و راه‌اندازی یک باره، نامحدود بودن(هر اکانت روزانه 6 گیگابایت حدودا(هر شب ریست میشه) و می‌تونید اکانت‌های زیادی بسازید. من خودم نزدیک به ۱۰۰ تا ساختم)
معایب: فقط وب سوکت میشه ساخت و ممکنه برای گیم و... مناسب نباشه اما برای اینستاگرام و یوتوب و اینها خارق‌العادست.
سری اول کلودفلر، پنل BPB:
آموزش اول: ساخت فیلترشکن بر پایه پروژه BPB و اسکن آیپی تمیز با سیستم:
https://youtu.be/_aXy8wwyRG8
آموزش دوم: تنظیمات پنل BPB از سیر تا پیاز:
https://youtu.be/7G9Fjhe_NxM
سری دوم کلودفلر، آموزش پنل Edge:
آموزش اول، ساخت پنل Edge با سیستم به علاوه تمام تنظیماتش و ثابت کردن لوکیشن:
https://youtu.be/svYBcv4bSzo
آموزش دوم، ساخت پنل Edge فقط با یک گوشی موبایل و نصب ترموکس و اسکنر برای پیدا کردن آیپی تمیز:
https://youtu.be/2otJfXgNWCM
3- آموزش کامل خرید سرور و دامنه و نصب کاندوئیت بر روی سرور ویژه ایرانی‌های خارج از کشور که می‌خوان کمک کنن به اتصال از طریق سایفون:
https://youtu.be/DtZyWXWV4BA
4- متد SNI-SPOOFING که در صورتی که یه روزنه‌ی کوچیک باز بمونه، می‌تونید باهاش با نهایت سرعت حتی توی بدترین قطعی‌ها هم وصل بمونید.
مزایا: بدون محدودیت سرعت، می‌تونید کاملا رایگان وصل بشید(با کانفیگ‌های کلودفلر متد شماره 2)
معایب: نیاز به باز بودن اون روزنه داره، و فقط روی سیستم قابل اجراست مثل Paqet. اما قابل اشتراک‌گذاری به دیگر دستگاه‌هاست.
آموزش اول: راه‌اندازی SNI-SPOOFING و استفاده ازش روی ویندوز:
https://youtu.be/dujMBt4sCpw
آموزش دوم: رفع مشکلات و ترکیب لوکیشن متد هر کانفیگی از SNI-SPOOFING روی آمریکا:
https://youtu.be/PuYwXH4D4tU
5- متدهای بر پایه‌ی گوگل. این متدها مادامی که گوگل وصل باشن، کار می‌کنن و طیف وسیعی از متدها رو هم در بر می‌گیرن:
الف- متد MHR و زیرمجموعه‌هاش: این متد محدودیت ۲۰ هزار ریکوئست روزانه روی هر جیمیل داره و سرعت آنچنان بالایی نداره اما با تعداد ایمیل‌های بالا، میشه بهترش کرد.
آموزش اول، متد MHR خام(توصیه میشه بعدیا رو راه بندازید نه این. چون با آیپی خودتون باید برید و هوش مصنوعیا رو نمیاره واستون):
https://youtu.be/jzaqdKl40Ww
آموزش MHR-CFW(ترکیب همین، با کلودفلر برای داشتن آیپی خارج):
https://youtu.be/L3lJZrAqqUQ
آموزش راه‌اندازی MHRv-RUST با گوشی موبایل:
https://youtu.be/7YdJIJloIxY
ب- متد MITM برای دسترسی به سرویس‌های بسته شده‌ی گوگل(چون از روش یک حمله‌ی سایبری استفاده میشه روی تلگرام آپلود شده فقط):
آموزش اول دسترسی به سرویس‌های گوگل و گیتهاب:
https://t.me/MatinSenPaii/3151
آموزش دوم دانلود نامحدود از یوتوب با نت ملی بر پایه‌ی آموزش اول:
https://t.me/MatinSenPaii/3230
ج- متد Skirk بر پایه‌ی گوگل درایو که مزایاش، سرعت دانلود بالا و معایبش، Latency بالا هست؛ از کانال عزیزی:
https://youtu.be/vCr4E6Y1k4c
6- متدهای بر پایه‌ی DNS، که از روز اول جنگ وصل بودن تا آخر قطعی. اما ما اواخر قطعی بود که به بهترین ترکیبش رسیدیم. پروژه‌ی MasterDNS و کلاینت WhiteDNS. مزایا: وصل توی هر شرایطی، قابلیت اجرا روی هر پلتفرم و سیستم عاملی، حتی روی سرور، و اضطراری‌ترین راه چاره‌ی ما
معایب: مصرف حدود دو برابری اینترنت(که به نظر خودم می‌ارزه توی اون شرایط) به علت کوئری‌های DNS فراوان. همینطور نیاز به سرور داره اما از سرورهای رایگان هم می‌تونید استفاده کنید(طبیعتا سرعت خیلی پایینتر)
آموزش کامل راه‌اندازی روی گوشی و سیستم:
https://youtu.be/6Pm7kNQb3mo</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/MatinSenPaii/3680" target="_blank">📅 14:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3679">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">امروز واستون دسته بندی می‌کنم یه کم راهکارهایی که تا الان دادمو</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/MatinSenPaii/3679" target="_blank">📅 08:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3677">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fx3E2f-EiXoxcKE7lvimSMVdDOdiOApXB2CSnnWl71cI4u91RIE_biCI_GXtyeG9hO2dqx_sYuiDdYqbOE1qzHj-abWU85xk9rthUe3o0O_r2zRtC4CV-Tj9AMRE6Uym0XqA3G3_llUDvghCyt_jJUxldBotCbiV_ZokGJ8HQW0W1SI-vFt6YHPW2YYY0RmnWTWRO8fJfi3-MYFpWy7bx-oXWD0YXeUVWwjQj1HSyfEh7g85CYhdCEjcwgcI3laRrhRMrXc2nYXyWr6Nz9KwVgwGKuUbAqV6431RCxYY5wgZmDgvxFEs2Bed8LYzlpWmODSRUh5xo4JcWhjKt23JyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/215e27ea42.mp4?token=WE6xBshCNxCPEFh960eEjoM_CLiEfU6cIDg9gr4Mf05zkbqgJ3bf8T_X5eEQpzcZshBhK7gzA3GD_efiwaoMf1c5zoUXiJwMAF7IBa4jJeT00M-TlLgbwbDy9suuI3qav5ed7RMhP4as5D8jcP8U4lmWVHCRFxsxaQ9-oYi7N_P2WQUB8ux23mzErzVvKPNae1Z-w_Fu0tFhBt1EcweLoNyu8-mFnrsnUkqVa7IxiWvnoPseAZai7GZaKbyZcTCUpJjpsRrEoD6gAB5dUPfy4rrNfjBIL6T-ZtP9Z92LarMRf1-pbasU5dIGkC-6A9sv82Wnw2K2waQshPz1HTObZw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/215e27ea42.mp4?token=WE6xBshCNxCPEFh960eEjoM_CLiEfU6cIDg9gr4Mf05zkbqgJ3bf8T_X5eEQpzcZshBhK7gzA3GD_efiwaoMf1c5zoUXiJwMAF7IBa4jJeT00M-TlLgbwbDy9suuI3qav5ed7RMhP4as5D8jcP8U4lmWVHCRFxsxaQ9-oYi7N_P2WQUB8ux23mzErzVvKPNae1Z-w_Fu0tFhBt1EcweLoNyu8-mFnrsnUkqVa7IxiWvnoPseAZai7GZaKbyZcTCUpJjpsRrEoD6gAB5dUPfy4rrNfjBIL6T-ZtP9Z92LarMRf1-pbasU5dIGkC-6A9sv82Wnw2K2waQshPz1HTObZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Operator: Asiatech/Datacenter Time: 2026-06-02 22:22:04  The status of this service has changed to:
❌
DNS google.com via 8.8.8.8 : timeout</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/MatinSenPaii/3677" target="_blank">📅 04:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3676">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">هیچی.
موشک زده شد؛
اونا هم گفتن دفع کردیم.
ما مردم بدبخت هم چیزای عادی‌تر دیگه‌ای از سبد خریدمون حذف میشه فردا و پس‌فردا و روز بعدش</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/MatinSenPaii/3676" target="_blank">📅 03:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3675">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarto | سارتو</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5a4f5e103.mp4?token=UI0y9hS07T7Y9xZ3ZACAcRVKgtPMz4b98Z7LWPLzgaPwma8FNlw65H8aKqPjvaUxTXQj2XYpjJ3uT4124o4MgOQkJVSIa2zaPQThs5BxIX8cVBvIC-ia3aSwvaLwhd0oEVwE8OpLusTX9GenXZl9b2MnSE_DG9COfp1JixNFBPJ5Uuo11VEWvTHXkX26Pb9yzGEGT2kzoLUhymTghDjKYuVEsypSrw_oBSDgKJ9362h07qWsevvD6VebJk7Jg1nUNeVjK2uTYfJPS0yDf-IjTcZhx7D3kriiRkZeHAEIXNiHRRZ_H6LuBgH0ICJYuV3OUDlOXrFaIFDpzzqbxqPWaBAeBYiCse4vHht4TUjucWCcErMdOn-wblFcjYzsokPZgsAhqqTw336thtsLVNWfpXpT9ZApBQI2GaG-2CSVSKLsRzVMM9XA53ewQpmoiUkT3Qn8_C5gAbunzUl5tr9DSFIx4Ar770V6-HHSxXRlYQgPjPuGoK0n2ZPSuZWtUk1aydw7cWK12bcgCO1b9qCJduie5pU168ShNAPtK587hI2uY2hk-UzlpVuLswWoT6CFhT8Uj1XWPKAhQkeTbejpTboDKKfQKygJ8QDQcinNRysmAjt6d2u-3jFB4JxRF912Nm2cgSXp0S_0lz1xqSAnHdDDcaBBjDHAsrKZgPuNkGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5a4f5e103.mp4?token=UI0y9hS07T7Y9xZ3ZACAcRVKgtPMz4b98Z7LWPLzgaPwma8FNlw65H8aKqPjvaUxTXQj2XYpjJ3uT4124o4MgOQkJVSIa2zaPQThs5BxIX8cVBvIC-ia3aSwvaLwhd0oEVwE8OpLusTX9GenXZl9b2MnSE_DG9COfp1JixNFBPJ5Uuo11VEWvTHXkX26Pb9yzGEGT2kzoLUhymTghDjKYuVEsypSrw_oBSDgKJ9362h07qWsevvD6VebJk7Jg1nUNeVjK2uTYfJPS0yDf-IjTcZhx7D3kriiRkZeHAEIXNiHRRZ_H6LuBgH0ICJYuV3OUDlOXrFaIFDpzzqbxqPWaBAeBYiCse4vHht4TUjucWCcErMdOn-wblFcjYzsokPZgsAhqqTw336thtsLVNWfpXpT9ZApBQI2GaG-2CSVSKLsRzVMM9XA53ewQpmoiUkT3Qn8_C5gAbunzUl5tr9DSFIx4Ar770V6-HHSxXRlYQgPjPuGoK0n2ZPSuZWtUk1aydw7cWK12bcgCO1b9qCJduie5pU168ShNAPtK587hI2uY2hk-UzlpVuLswWoT6CFhT8Uj1XWPKAhQkeTbejpTboDKKfQKygJ8QDQcinNRysmAjt6d2u-3jFB4JxRF912Nm2cgSXp0S_0lz1xqSAnHdDDcaBBjDHAsrKZgPuNkGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
آموزش کامل TheFeed از صفر تا صد
اگر تازه با TheFeed آشنا شدید و نمی‌دانید از کجا باید شروع کنید، این ویدیو دقیقاً برای شماست.
👇
در این آموزش یاد می‌گیرید:
✅
اضافه کردن کانفیگ
✅
آشنایی با ریزالورها (DNS)
✅
پیدا کردن ریزالورهای سالم
✅
مشاهده کانال‌ها و دریافت محتوا
✅
آشنایی با بخش TeleMirror
✅
رفع مشکلات رایج کاربران
✅
نکات مهم برای استفاده بهتر از برنامه
دفید یک سیستم مبتنی بر DNS است که امکان دسترسی به محتوای کانال‌های تلگرام را حتی در شرایط محدودیت اینترنت فراهم می‌کند.
📢
کانال اصلی پروژه:
@networkti
📦
فایل‌های نصب:
@thefeedfile
⚙️
کانفیگ‌های عمومی:
@thefeedconfig
توضیحات متنی
👇
سلام. توی این ویدیو می‌خوام خیلی ساده و سریع نحوه کار با برنامه The Feed رو توضیح بدم.
بعد از نصب و باز کردن برنامه، اولین کاری که باید انجام بدید اضافه کردن یک کانفیگه. برای این کار از بالا روی علامت جمع بزنید و کانفیگ مورد نظرتون رو وارد کنید. کانفیگ‌های عمومی داخل کانال
@thefeedconfig
منتشر میشن و می‌تونید از اونجا دریافتشون کنید.
هر کانفیگ دارای تعدادی ریزالور پیش فرض هست که توسط سازنده کانفیگ داخل کانفیگ قرار میگیرن. بعد از اینکه کانفیگ رو اضافه کردید، برنامه شروع می‌کنه به بررسی ریزالورها. ریزالورها همون DNS هایی هستن که The Feed از طریق اون‌ها اطلاعات رو دریافت می‌کنه. این مرحله ممکنه چند دقیقه طول بکشه، پس اگر بلافاصله کانال‌ها نمایش داده نشدن نگران نباشید. بعد از پیدا شدن ریزالورهای سالم، لیست کانال‌ها دریافت میشه و می‌تونید وارد هر کانال بشید، پست‌ها رو ببینید و در صورت وجود، عکس‌ها، فایل‌ها، ویس‌ها و ویدیوها رو دانلود کنید.
اگر یه زمانی دیدید برنامه کند شده یا اطلاعات جدید دریافت نمی‌کنه، معمولاً مشکل از ریزالورهاست. برای همین داخل برنامه بخشی به اسم «پیدا کردن ریزالور» وجود داره. وارد این قسمت بشید و روی «بارگذاری لیست پیش‌فرض» بزنید. با این کار حدود ۵۸ هزار ریزالور برای اسکن آماده میشن.
اگه خودتون ریزالور خاصی دارید، می‌تونید به صورت دستی هم واردش کنید. علاوه بر این، ربات
@dns_resolvers_bot
هم می‌تونه برای پیدا کردن ریزالورهای جدید بهتون کمک کنه.
بعد دکمه «شروع اسکن» رو بزنید تا برنامه ریزالورهای سالمی که روی اینترنت شما کار می‌کنن رو پیدا کنه. وقتی چند تا ریزالور پیدا شد، می‌تونید اون‌ها رو به لیست فعال اضافه کنید. فقط یادتون باشه موقع اسکن بهتره VPN خاموش باشه تا نتیجه دقیق‌تری بگیرید.
داخل برنامه یه بخش دیگه هم به اسم Tele Mirror وجود داره. این قسمت با سیستم اصلی TheFeed فرق داره و برای نمایش کانال‌های عمومی تلگرام از سرویس‌های گوگل استفاده می‌کنه. با TeleMirror می‌تونید خیلی از کانال‌های عمومی دلخواهتون رو دنبال کنید، ولی محدودیت‌هایی هم داره؛ مثلاً امکان دانلود فایل یا پخش ویدیو توی این بخش وجود نداره. همچنین اگر سرویس‌های گوگل در دسترس نباشن، ممکنه Tele Mirror کار نکنه. البته این موضوع روی بخش اصلی TheFeed تأثیری نداره و سیستم اصلی برنامه همچنان از طریق DNS به کار خودش ادامه میده.
در نهایت اگر جایی به مشکل خوردید، اولین چیزی که باید بررسی کنید ریزالورها هستن. در اکثر مواقع با پیدا کردن چند ریزالور سالم، مشکل برنامه برطرف میشه. برای دریافت آخرین اخبار پروژه هم می‌تونید کانال
@networkti
رو دنبال کنید، فایل‌های نصب رو از
@thefeedfile
بگیرید و کانفیگ‌های عمومی رو از
@thefeedconfig
دریافت کنید.
ممنون که این ویدیو رو دیدید و امیدوارم از The Feed لذت ببرید.</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/MatinSenPaii/3675" target="_blank">📅 02:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3674">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">من الان خودم با WhiteDNS آنلاینم(داشتم تست میکردم دامین اینها نپریده باشه)
خواهش میکنم ستاپ کنید هر چه سریعتر. هرچی نیاز دارید توی ویدیو هست
https://youtu.be/6Pm7kNQb3mo?is=Hh_zNDNmPQGHgzLb</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/MatinSenPaii/3674" target="_blank">📅 01:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3673">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/966f6f971b.mp4?token=LpHaTbaYVbVmrydrZWppcIJoFw4JdecxirA6TA22ywRBf9RN3PtIiqN3WPspkhfOtkRoxqb0mCCH1B9Fx15okxckrMShbrq41eORas4CNmRUImAJKCm0TOJD6IuxJeMXqbOUcyjqVMfe_CXch8dS6YZLxKWYn4EpVK-VrCQ-fA883FfiB3LadmKzaWIXU2DsaxQuqicg5n_0K6XQWEwQGffor07nhElb9YaApYiXbps0iZApuGUc9PcMe_PYZ0NPo5ukN-Wh-Kr2pTSJOR8NEwYunPSyTefJ-s0SFnz3aTmWoDHxml_s47FflzXfSsTH_PYtTumqi8IU2TvFRhU6NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/966f6f971b.mp4?token=LpHaTbaYVbVmrydrZWppcIJoFw4JdecxirA6TA22ywRBf9RN3PtIiqN3WPspkhfOtkRoxqb0mCCH1B9Fx15okxckrMShbrq41eORas4CNmRUImAJKCm0TOJD6IuxJeMXqbOUcyjqVMfe_CXch8dS6YZLxKWYn4EpVK-VrCQ-fA883FfiB3LadmKzaWIXU2DsaxQuqicg5n_0K6XQWEwQGffor07nhElb9YaApYiXbps0iZApuGUc9PcMe_PYZ0NPo5ukN-Wh-Kr2pTSJOR8NEwYunPSyTefJ-s0SFnz3aTmWoDHxml_s47FflzXfSsTH_PYtTumqi8IU2TvFRhU6NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/MatinSenPaii/3673" target="_blank">📅 01:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3672">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">به نظر که جنگه
چون بالستیک زدن
اگه آمریکا نگه اینا نقض آتش‌بس نیست</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/MatinSenPaii/3672" target="_blank">📅 01:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3671">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">لطفا WhiteDNS رو ستاپ کنید هر چه سریعتر تا قطع نکردن:
https://youtu.be/6Pm7kNQb3mo?is=Hh_zNDNmPQGHgzLb</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/MatinSenPaii/3671" target="_blank">📅 01:28 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3666">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">استفاده از فرگمنت هم جوابه</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/MatinSenPaii/3666" target="_blank">📅 00:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3665">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/F4y1J5zd9ZTSqflCqyZBwju6y0SRiJSWuJGY_q9l4skX9WtLZ6Ri6OkMSGK-oei7NnHtj7xy7PbodUPmH_mKA6ae4j4C3xymCWoAr7gTvpUz0vneCKEtwEfdENtvSHjsFAuz6cjPuJ0s9-WrGO-WqVKePHlPyhqkzbpqPsrrQ5hJ95nwFaHZXZMn5asVYZDliS9X94vjJ3dy_4fDwwje8h7IRCiireGOIYO8RHrfS0yyfIMlQtk1yNIVWIelvITrFYarX-5LUbA_Adu3fCvgEoJh161qfkZtJNfMtLBaUCTXwN0_Gr7AEzKL5kzhtRJ4sVPsjTjYezDQP2ZPpa2bqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای مشکل آپلود روی کانفیگ مستقیم پشت CDN، تنها راه استفاده از اسپوفه. sni spoof</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/MatinSenPaii/3665" target="_blank">📅 00:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3664">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">دیدین گفتم
😂</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/MatinSenPaii/3664" target="_blank">📅 22:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3663">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromiran internet monitor</strong></div>
<div class="tg-text">Operator: Asiatech/Datacenter
Time: 2026-06-02 22:22:04
The status of this service has changed to:
❌
DNS
google.com
via
8.8.8.8
: timeout</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/MatinSenPaii/3663" target="_blank">📅 22:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3662">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">Operator: Asiatech/Datacenter Time: 2026-06-02 21:01:30  The status of this service has changed to:
✅
DNS google.com via 1.1.1.1 : 142.251.14.138</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/MatinSenPaii/3662" target="_blank">📅 21:02 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3661">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromiran internet monitor</strong></div>
<div class="tg-text">Operator: Asiatech/Datacenter
Time: 2026-06-02 21:01:30
The status of this service has changed to:
✅
DNS
google.com
via
1.1.1.1
:
142.251.14.138</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/MatinSenPaii/3661" target="_blank">📅 21:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3660">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M-7XmihBZiel_wPVhy6bFU-6kNU-hl_FSyZrFMjxcCBlhi1xcPXC_ykkTRNDXuaKvjNk6BeIv3aU6qQk_OZ1lP9vSsfrJ2WYaj2PCWYhjiZUnKmy_q9MHqgvUU6cmWwd45DV_CFO4BIODKZY0HUyr0uz7e2LrGktZ6O7Ktr4px7bHQm7hqQ-U-thzwIy9e-zodeVjIPC6AFErdp4RVEc-H1kV1GI9h0QwwwJscwU9UVLBtW_a-n_x7BmX76p77qGlWQz56s0CqG-juZw1b3wQ3upVRs9JVyE55jrAMBVHrrSDGve9JNdH-wBrjInW-aj9ZWybfjMndG778fqOz5E6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچند یک سری دیتاسنترهای خاص یه سری تانل‌ها روشون جواب میده به راحتی. از جمله Paqet و بک‌هال و  reverse</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/MatinSenPaii/3660" target="_blank">📅 19:04 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3659">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fmMP-w6dQv56K4PJajObrkfslVQbAqGKsPM4kLCYswwiP37Aw_u_tOFFQV6KHoegw_n6vLQyFCA9_p1W5UfgHvCvI1zx4yA-pOoVn5iCemyWLiUxAwOoiK4r78u583UhfhRa1-XS202A8l9cmakQ_I4mjgl9Wytzm5t9Q1AKch4NigXeYsmUeTC655FYkg6iPujQGhXKylDTMs8cbgpNOPbRVEMtKeyX2phQgXZFb6WS7Fuzw5IN5QNBFG6nL3hz3LGHlTewQO1QhqHUfpfNEZ4ngwcyQpT1An4IsQ9tUJV_lDgyJq3myDuq3qiWpN1UuYKPLIg2NXKSyZ_xKc_t4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
ساخت نامحدود تصویر با هوش مصنوعی Nano Banana 2 گوگل + طراحی رابط کاربری(UI) و ساخت ویدئو و موسیقی
⭐️
توی این ویدئو:
1- بهتون نشون میدم که خودم Thumbnailهام رو چطوری میسازم و چه شکلی می‌تونید به صورت نامحدود از Nano Banana 2 و Pro گوگل استفاده کنید
🎤
2- یه UI باحال با هوش مصنوعی به همراه پروتوتایپ طراحی می‌کنیم
❄️
3- و با همدیگه یه موزیک در مورد 90 روز قطعی اینترنت می‌سازیم
🎧
🤎
اسپانسر ویدئو:
کانال تلگرامی ذغال سیستم؛ فروش لپ تاپ و لوازم جانبی استوک وارداتی دبی:
https://t.me/ZoghalSystem
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل رایگانه و نیاز به پیش‌نیاز یا هزینه نداره
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/MatinSenPaii/3659" target="_blank">📅 17:49 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3657">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ببینید MHR و mhrv-rust و skirk و flow drive و تمامی متدهای بر پایه‌ی گوگل، با اولین بادی که از سمت سرزمین‌های دشمن بِوَزه قطع می‌شن
تنها چیزی که برای ما می‌مونه، DNS هست که همون هم ممکنه سرعتش خیلی خیلی کم باشه و می‌تونید از اینجا
https://youtu.be/6Pm7kNQb3mo
آموزشش رو ببینید.
متدهای بر پایه کلودفلر مثل BPB و Edge و... هم که یه پله بالاتر از MHR و اینها هستن و طبیعتا همیشه بعد از وصل شدن گوگل، وصل می‌شن.
هرچند به WhiteDns هم نمیشه ۱۰۰ اعتماد داشت که برامون بمونه چون توی هر سری فیلترینگ ما غافلگیر شدیم. مثلا ما به هیچ وجه فکر نمی‌کردیم بتونن جلوی Paqet رو بگیرن اما تونستن. هرچند امثال پترنیها هم با SNI Spoof، اونا رو غافلگیر کردن!
برای همین شما ترجیحا متد مستر دی ان اس رو توی Whitedns به عنوان اضطراری‌ترین راه، داشته باشید علی‌الحساب</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/MatinSenPaii/3657" target="_blank">📅 12:13 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3656">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/MatinSenPaii/3656" target="_blank">📅 11:54 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3655">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRCF | اینترنت آزاد برای همه</strong></div>
<div class="tg-text">گروه Void Verge در تازه‌ترین
#گزارش
خود اعلام کرده: از زمانی که اینترنت ایران دوباره توسط دولت بازگشایی شده، تغییرات گسترده‌ای در شبکه داخلی کشور درحال انجام است. پس از هفته‌ها قطعی و محدودیت، تقریباً تمام روش‌هایی که در آن دوره مورد استفاده قرار می‌گرفتند مستندسازی شده و به دست نهادهای مسئول رسیده‌اند. سیستم فیلترینگ خود را برای مرحله بعدی اختلال‌ها و قطعی‌ها آماده می‌کند و روش‌هایی مانند DNS Tunneling، MITM و Domain Fronting به احتمال زیاد در قطعی‌های آینده دیگر کارایی گذشته را نخواهند داشت.
علاوه بر این، نهادهای مسئول فیلترینگ اقدامات گسترده‌ای برای ایجاد ارائه‌دهندگان واسط انجام داده‌اند؛ سرویس‌هایی که خدمات خارجی را با محدودیت‌های شدید در اختیار کاربران ایرانی قرار می‌دهند یا وب‌سایت‌های ضروری را که امکان استفاده از روش‌های قبلی را ندارند، از طریق NAT در دسترس قرار می‌دهند. در چنین شرایطی، انتشار عمومی و علنی روش‌ها نتیجه‌ای جز آسان‌تر کردن کار نهادهای فیلترینگ ندارد. این سازوکارها باید دور از توجه، به‌صورت کلوزسورس و کم‌سروصدا فعالیت کنند.
در همین حال، مافیای اینترنت در ایران بیش از گذشته قدرت گرفته است؛ مافیایی متشکل از افرادی با دسترسی به «اینترنت سفید»، برخی ISPها و مراکز داده که از طریق سازوکارهایی مانند سرویس‌های پروکسی و سرورهای اختصاصی مجهز به NAT، اینترنت نامحدود را با قیمت‌هایی در حد صدها میلیون تومان به فروشندگان VPN عرضه می‌کنند. این مافیا آن‌قدر قدرتمند شده که توانسته بر سیاست‌گذاری‌ها نیز اثر بگذارد و حتی در شرایط بحرانی و دوران جنگی هفته‌های گذشته، به حفظ هرچه بیشتر محدودیت‌های اینترنتی کمک کند تا منافع اقتصادی خود را حفظ و افزایش دهد.
برخی شرکت‌های ساده میزبانی وب در ایران تنها طی دو ماه قطعی اینترنت، به فروشندگان بزرگ VPN با درآمدهای بسیار بالا تبدیل شده‌اند. ما در هفته‌های آینده به جمع‌آوری و انتشار اطلاعات و داده‌های لازم ادامه خواهیم داد. اگر این روند ادامه پیدا کند، هدف بعدی باید مقابله با مافیای اینترنت در ایران باشد. امیدواریم این روزهای سخت برای همه ایرانیان به پایان برسد. آسیبی که از سوی دشمنان داخلی و افرادی که زیر سایه جنگ از مردم سوءاستفاده می‌کنند به جامعه وارد می‌شود، گاهی از خود جنگ نیز دردناک‌تر است.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/MatinSenPaii/3655" target="_blank">📅 11:38 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3654">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">دوستان برای هیستریا، سرورهای AWS آمازون با این سرعت جوابگو هستن چیزی که من دیدم و دوستان گفتن و متأسفانه دیتاسنتر دیگه‌ای ندیدم که به این خوبی باشه. آمازون هم گرونه به شدت
پس از آموزشش فعلا منصرف شدم</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/MatinSenPaii/3654" target="_blank">📅 00:55 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3653">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">شمع Iced latte</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/MatinSenPaii/3653" target="_blank">📅 23:34 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3652">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uWmdEzEihXdlB1AHrx4nMf8Y1F-jtm2jiMrAuU5F7PgJAR-SnsIbsujSCGAcAqt_H80GMVXjY2Jf_F8vEIM4cgbe9wMmCpas6L19f_Zz4m3Wh4GBcxH_ZxdBvwA19IfPaAyukMgTrMSG2l4dbDy-_atCYrd8o0JoQK_OenBhi9skr_RmLVT3vVBqAG_VIL3gA2DmVUAiIGNqVQ83Ram499ykjn-x4M_M7Q4Ja6hrv6KtsdOrbYPQgrJDoprURNBBWh-12o0bDfbdT2hVzLkL21SOF3ngb-VvGeUyTZCqQdOTgyo_EIDGD_YCa6K3OshawLZVAr3d6msA-2SQWn7yHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر ارور EOF و 403 گرفتید یعنی گیتهاب هنوز روی اپراتورتون مشکل داره و این یعنی اسکنر نصب نمیشه(باید با وی‌پی‌ان بزنید). طبیعتا وقتی دستور senpaiscanner رو میزنید not found میده چون اصلا چیزی نصب نشده</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/MatinSenPaii/3652" target="_blank">📅 22:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3651">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">☠️
آموزش ساخت VPN شخصی با گوشی موبایل(کاملا رایگان) + اسکن آیپی تمیز با Termux  دوستان این متد  تا مرحله‌ی 4 اش انجام دادنش منطقیه. ما متوجه شدیم که در واقع SNI Spoofingای در کار نیست و کانفیگ داره فرگمنت میشه فقط. تا مرحله‌ی 4 پیش برید و پرسرعت به کانفیگ خودتون…</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/MatinSenPaii/3651" target="_blank">📅 20:32 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3650">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lZBjkBApEv0kugOGjN4ntE6nupkeFWOQhWxSsUmnjswmtji7_FRHhrygLQBbiYKRRx6ohS1eghE34R4c4LtQRZTk9bj62bw0L95PS8XhBrJZqEfa0ab9M0m7Vb-WrKyae3iw79mcMlLtyM6kefrwNNUzSSTx_9fEuxoNWLRIsNSsbfvnEL6o9YNLqbTlJ-P_gR3XKw1KMvkv-1mnaYa4W4mYW60_zxmCJnQ_77ZmPM5ViXuaARArRnrXEJcBBHkojJxEfQBVA3goFADmXyTumsd1j5G0N7RrG9_9Zg1Hw2BkoW8On-caLUTvnlXnni9gATwHNFUwT4sjx69EnFG3ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر به این ارور خوردید، پروژه‌ی جدید بسازید. اگر باز هم نشد، با یه اکانت دیگه وارد بشید و مجدد تست کنید. توی این ویدئو
https://youtu.be/_aXy8wwyRG8
به همین ارور خوردم و این شکلی حل شد</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/MatinSenPaii/3650" target="_blank">📅 19:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3649">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">☠️
آموزش ساخت VPN شخصی با گوشی موبایل(کاملا رایگان) + اسکن آیپی تمیز با Termux  دوستان این متد  تا مرحله‌ی 4 اش انجام دادنش منطقیه. ما متوجه شدیم که در واقع SNI Spoofingای در کار نیست و کانفیگ داره فرگمنت میشه فقط. تا مرحله‌ی 4 پیش برید و پرسرعت به کانفیگ خودتون…</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/MatinSenPaii/3649" target="_blank">📅 19:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3648">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">دوستان این متد  تا مرحله‌ی 4 اش انجام دادنش منطقیه. ما متوجه شدیم که در واقع SNI Spoofingای در کار نیست و کانفیگ داره فرگمنت میشه فقط. تا مرحله‌ی 4 پیش برید و پرسرعت به کانفیگ خودتون متصل بشید</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/MatinSenPaii/3648" target="_blank">📅 18:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-3646">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DMjQQFPRvFrDHV2Uz--IyiJDwPLJiKQGA3Htf4OtYKlJXtnqgolQTNDhee-u14bL3RbEm0pUCmomXwyS_Yto-QtR3MdTDN9IScsL0NtqLI6PdcmxqbHyp9c3jZni_3ySMbD9bB28cd3G_0ntzwDaB4-TViZIudEYav3OOgK4Uw_w4CMPWbO3b_ZCb3x0LIcsNfYBFPXM-N-DrTXtJfyroRmUW300bzF0paUxPzLD9xx5oaWV7DqoXKv10VDPlsYp5StHMIWbwiAxMzuUDZx029ZIXqysatJia9TwakMUkAU80QpjV8cBLsRewnVssCg8nUOc7Uo8WCtCfLZ5YNJS9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MJVSqwTJZe5dYC2tqqwgjtd8_yNGbgw_oa21mD0nEogXsvCLpTB8cEZ-qjqcCnsl7kecJImZMsbSX6jY31uvZdo2ML0M34meTvHaek1SVHOwx844MKJF8rGpyRR5ZBYRyxIiTYX-YZ5k6HtC-bHi2m4A1c2KyF8o2975JunoXasmkYFgpyyiZ3DHN28BfjuLtzsLceVFqaMriVGRCcECCJXAqRtkg11u9-tF40SMl-yYhLltKWRhohbqGGF9rhKMMC3m1FPyX5_VnbE3HUjunVIdOCHiWrEMKwPvvtZxFG113tiAffVLd2ZO39TaTbhas0G55xrzaHfGPuote1bX8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">☠️
آموزش ساخت VPN شخصی با گوشی موبایل(کاملا رایگان) + اسکن آیپی تمیز با Termux  دوستان این متد  تا مرحله‌ی 4 اش انجام دادنش منطقیه. ما متوجه شدیم که در واقع SNI Spoofingای در کار نیست و کانفیگ داره فرگمنت میشه فقط. تا مرحله‌ی 4 پیش برید و پرسرعت به کانفیگ خودتون…</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/MatinSenPaii/3646" target="_blank">📅 17:47 · 11 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
