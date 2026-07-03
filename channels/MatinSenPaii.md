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
<img src="https://cdn1.telesco.pe/file/lwIhpx_Qq84wqkLCAuCEwELylCjN1_wt05uzkK6Cq6MZrkdHYBfl1WOnn8FJKWNNicaB8kUCzKIjNZ_3Wp5siTwE0vcjjEb-GDOk9vFwEQv8V0D5msiUOnpFvrhPQj_FngaszSao-Yb5Gkt6QCY3PFXe_XLxTDvQHsO5VQ_srwA3K3kPJyZtJc2IwDFr7quz9ot89yCu85LCfEB5951DqmWgXM87ve77dPViUnjrmxAE8HCNTX2zxdarHnU02GWDB57tJoA_Q5OjZe_EJW5QbbxJNE-taFLP5r5rgMMyyqPdz9ZWk3iR_yvZVffDxwYuLS87gFzj8uhwzfJ-onwlWA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 159K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPaiایمیل کاری: matinsp.job@gmail.com</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-12 06:02:13</div>
<hr>

<div class="tg-post" id="msg-4194">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AAuvbUzKVoboKbndrSK0XuBv7NrLwlJY-UfyEPxpfkGKzBBENdDUtQgm4psoknhPRUwpB1qoQZ72bdIqRiDofTyQsrLCBMcR_I5rJTKn2iVQxOywTOHgsqqG5uUIyZFSxGOKz6F5duLMoIAOa4b_WZrcP6lfi-uf3TAmXvNwu9FrsqbNrjjnU6zW3hjSk73ZLbvykJpZqgYqz9yZK7GsaH1mqb2-WBjW6MEXdImcPbRztwssHYpU2cYUxc71XZv2YqydojBfe9hbPVoMe5GF4yCbQJ1FCIs9HQQs-8THJXRrDvHDI6Sd7GTU7JfOlHneiUw0VQIi5j4XZq0IMC6ZEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر ZCode رو نصب کنید(با Zed Code فرق میکنه) می‌تونید روزانه 3 میلیون توکن رایگان GLM-5.2 و دو میلیون توکن GLM-5 Turbo بگیرید با یه محیط کدنویسی تمیز شبیه به Codex با هر ایمیل هم می‌تونید یه اکانت بسازید و... بله خلاصه
🥰
اینم لینک نصبش: https://zcode.z.ai/en/docs/install</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/MatinSenPaii/4194" target="_blank">📅 00:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4193">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LU2EBOEZp_J5ecJQqHOgOPsZjO4U1dGKfSXy7HBqkBW9eBEdsE94BhPd1Jo_CdhsQnTFMA6ZaqkUp-fiAdqSbe5J-1O7PR3akxAkqn8wvoYVEViGgibbakcsOehUJlpt0RtT9j9el-JMg-9LZj304ij-fkEzTqFLhJoQn3NBZfaexkE37cpLFpG94jAQTcSML11n36gq-CO_J0MJge01QxuutbNCYBYRLNz7m5ObPFeEK9nGQomS_-RigLx-r--ikdUWHMQHQ1jmyKxbgbg5hpzCFprTsTzBO9Nl9z2zuvXAd7173JP64XLNNkirbGF3qRKEa0xlG5E1dwzH7spsQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر ZCode رو نصب کنید(با Zed Code فرق میکنه) می‌تونید روزانه 3 میلیون توکن رایگان GLM-5.2 و دو میلیون توکن GLM-5 Turbo بگیرید با یه محیط کدنویسی تمیز شبیه به Codex
با هر ایمیل هم می‌تونید یه اکانت بسازید و...
بله خلاصه
🥰
اینم لینک نصبش:
https://zcode.z.ai/en/docs/install</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/MatinSenPaii/4193" target="_blank">📅 23:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4192">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسمپا- آزاد سازی اینترنت</strong></div>
<div class="tg-text">‏DoH HTTP Proxy یک ابزار سبک و کاربردی برای ویندوز است که با ایجاد یک پروکسی محلی، درخواست‌های اینترنتی را از طریق DNS over HTTPS مدیریت می‌کند. این برنامه زمانی مفید است که DNS شبکه دچار اختلال، جعل، مسدودسازی یا ناپایداری شده باشد و تلاش می‌کند با استفاده…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/MatinSenPaii/4192" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4191">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسمپا- آزاد سازی اینترنت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gLGXet_wKHnVTkTOi3UegxLMeVPqEDJoBGAEhM6I1FqK6iQLFjwRypGcpBnmgI7odhFESSs1cpscu4SLDRmsm9jHYTsN9zBymSX1t-Q1Xox7zUuaZlssprzq0ER9uy4Gs84P5FhxX4dYJKpby2nyRq-QOv4vTF2mc_5_-QY4q18c9ipYGbgqaF6OQOWILxvyOWgVGbeL5mZay13dybtTy7uG703l9SwNp2EASsH0wzUePRvQITB_0GpW8QxiQi5NPPobSRZxc9-KOina92pUkrgim3GP8VEs072tL5ipqWY9H4rthBhonsyl2cacyXOclRWmqJeKuFYVWd95QwPelA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
DoH
HTTP Proxy یک ابزار سبک و کاربردی برای ویندوز است که با ایجاد یک پروکسی محلی، درخواست‌های اینترنتی را از طریق DNS over HTTPS مدیریت می‌کند. این برنامه زمانی مفید است که DNS شبکه دچار اختلال، جعل، مسدودسازی یا ناپایداری شده باشد و تلاش می‌کند با استفاده از endpointهای DoH، کش نتایج قبلی، fallback و حالت اضطراری، اتصال کاربر را پایدارتر و قابل‌اعتمادتر نگه دارد.
لینک دانلود برنامه:
https://github.com/SAMPA-ASA/DoH-HTTP-Proxy/releases/latest
لینک پروژه
👇
https://github.com/SAMPA-ASA/DoH-HTTP-Proxy</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/MatinSenPaii/4191" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4190">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SSHLBBJahB51SxqcP7pGx82beG5Y9auksXId2Xaep2BlqfvtXI241bn4gQRppPeel1WzWPxQNNaZGl0n9wVPcPdOYRYFR7eComVUO4IviDfNmdhtWTakyopl3uYx0U-2xIiZLfmrtL7TUOtNkCwTrTeXiQmCYnm4oK1DC4Wq-_YbFmODTbG4KoihRwakiyxlARM__94VyQliXaH7B29uA-rvSi6jxkqrFb0lluqBjIPlKnjmMz6-Xgt7cf8Qq4q3_EjDm-N_RO2fHGuIxE_2VmHW1BbgebmQHm35AEWQcYywYzGHRhaec3gzfB0jDJRgMvuTVNit6RnYy5EW4ZAugA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر از تلگرام برای ارتباط با ایجنت هرمس Hermes استفاده می‌کنید بهش بگید که تاپیک فعال کنه یا فرمان /topic بزنید. بعدش بهتون میگه که برو توی تنظیمات BotFather و گزینهThreaded Mode روشن کن بعد از اون برای هر موضوع میتونی یه تاپیک جدا باز کنی و ایجنت موضوعهای مختلف باهم قاطی نمیکنه
✍️
Hessamsh</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/MatinSenPaii/4190" target="_blank">📅 23:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4189">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">برای هرمس، 1 هسته سی پی یو و 1 گیگ رم به عنوان Minimum کافیه. اما پیشنهاد میکنم 2 هسته - 2 گیگ رم باشه</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/MatinSenPaii/4189" target="_blank">📅 22:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4188">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iqg6IUZt-FLlyO6x0ySj5l_6wW34ehwbYWpQyiCdAT3GVjcZoYRAzDTpIeaIYVBdeef5-zCyMrOXP1s4Mj7S-Elj-9v6QjEOWVb4pUGbpAmC5BdnnbAmlsbCK3PMvl8PI0UUN2Fhfm88f4Kbanvcdb8uqQBMdkwr_xz6cduGww9tPvUnRToCsEev-FojcsCX19TflElyL7b-NLUnewjwtKORpPVCdNol3R0-EUu5XK_6DkDDALyBk7fSnDkbzm-aW8keo48J1IEW2_hQ9FYWVjZ6P8e2nR5ECQ_LE5v_9NquWKbu0aPcBSE50-e2zWnX2nU7LXI8sF-ru_mlSb9cJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفقا اگر صحبت کاری‌ای داشتید با من، از اینجا می‌تونید ایمیل بدید و مطرح کنید:  matinsp.job@gmail.com  سؤالاتتون راجب متدها و... رو توی کامنت‌های یوتوب بپرسید. این ایمیل برای این منظور ساخته نشده
❤️
ممنونم از درکتون</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/MatinSenPaii/4188" target="_blank">📅 21:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4187">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">رفقا اگر صحبت کاری‌ای داشتید با من، از اینجا می‌تونید ایمیل بدید و مطرح کنید:  matinsp.job@gmail.com  سؤالاتتون راجب متدها و... رو توی کامنت‌های یوتوب بپرسید. این ایمیل برای این منظور ساخته نشده
❤️
ممنونم از درکتون</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/MatinSenPaii/4187" target="_blank">📅 21:50 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4186">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">رفقا اگر صحبت کاری‌ای داشتید با من، از اینجا می‌تونید ایمیل بدید و مطرح کنید:
matinsp.job@gmail.com
سؤالاتتون راجب متدها و... رو توی کامنت‌های یوتوب بپرسید. این ایمیل برای این منظور ساخته نشده
❤️
ممنونم از درکتون</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/MatinSenPaii/4186" target="_blank">📅 21:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4185">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X7xTmv-nPLyrv9XSppzmDQ8YuWqVZYK5IrZldDFj7qu0ZJGxnO8ZZ9BCI5WRJ-s0bEnYE03WZphiQysCoXQNP4vZ9NJf6nrcaG97keo2r0XhUH17GhXfg3TFir4V4Fs-tRHsRpwjYQnzALHwXzqOjMl8ZW6YOWSduBvmwc1ZweEhRjUg6W0JHKW33T_55XNBFlAYoAJtMEf8mSfY86yQCJFnXZ-_ufmrKd9a4VaHPtuEcT5kuvsbE4DT1ildOk-YaGlGEdKLJcCr0kb7vECK2npdsEc1bjRxdEjKm9SJu7W4yKbtOcEOkI8WeGTxyZYyZqdh7clFtQHz3wlPsdN5JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی هم تر و تمیز و عالی</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/MatinSenPaii/4185" target="_blank">📅 21:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4184">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">فیلم آموزشی Clash Party
https://youtu.be/gMFH88yRghg</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/MatinSenPaii/4184" target="_blank">📅 21:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4183">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">سلام خدمت همه دوستان
✍️
سرویس ساب WhiteDNS در گیتهاب راه‌اندازی شد.
✍️
اسکنر های ما هر ۳۰دقیقه بیشتر از ۲۵۰هزار کانفیگ را اسکن میکنند، از خروجی این اسکن تست سرعت، دسترسی و DNS Leak گرفته میشه تا بهترین کانفیگ ها جدا بشن.  نتیجه این تست، هر ۳۰دقیقه داخل…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/MatinSenPaii/4183" target="_blank">📅 21:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4182">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">سلام خدمت همه دوستان
✍️
سرویس ساب WhiteDNS در گیتهاب راه‌اندازی شد.
✍️
اسکنر های ما هر ۳۰دقیقه بیشتر از ۲۵۰هزار کانفیگ را اسکن میکنند، از خروجی این اسکن تست سرعت، دسترسی و DNS Leak گرفته میشه تا بهترین کانفیگ ها جدا بشن.
نتیجه این تست، هر ۳۰دقیقه داخل این مخزن گیتهاب برای سرویس های متفاوت قابل دسترسی خواهد بود.
🌎
ساب مناسب اپ های V2Ray, V2rayNG & ...
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/base64.txt
🌎
ساب مناسب Clash Mi, Clash Party
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml
🍏
IOS App
: Clash Mi, Karing
👾
Android App
: Clash Party, Karing
👍
Mac App
: Clash Party
📱
Windows App
: Clash Party
📱
Linux App
: Clash Party
@WhiteDNS</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/MatinSenPaii/4182" target="_blank">📅 21:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4181">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">بن شدن حساب‌های کلاد واقعا نگران کننده شده. هرکسی هم بن شده از ایرانیکارت خرید کرده یا سابقه خرید داشته</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/MatinSenPaii/4181" target="_blank">📅 20:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4180">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">بن شدن حساب‌های کلاد واقعا نگران کننده شده.
هرکسی هم بن شده از ایرانیکارت خرید کرده یا سابقه خرید داشته</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/4180" target="_blank">📅 19:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4179">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">☠️
نصب و استفاده از Hermes، آینده‌ی هوش مصنوعی
⚡️
فایل لینک‌های مورد نیاز: https://t.me/MatinSenPaii/4178
⭐️
توی این ویدئو: 00:00 چرا هرمس؟ چه استفاده‌هایی میتونیم ازش بکنیم؟ 04:17 نصب و راه اندازی روی دسکتاپ(ویندوز، مک، لینوکس) 13:47 نصب و راه‌ اندازی روی…</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/4179" target="_blank">📅 17:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4178">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Hermes-MatinSenPaii.txt</div>
  <div class="tg-doc-extra">886 B</div>
</div>
<a href="https://t.me/MatinSenPaii/4178" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دستورات نصب Hermes روی سیستم‌عامل‌های مختلف و سرور
سایت YottaSrc:
https://yottasrc.com/
سایت Netlen:
https://www.netlen.com.tr/
سایت Senko:
https://senko.digital/</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/4178" target="_blank">📅 14:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4177">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tudDCb-5ih9vIjFQ3Y0rO8KHtXYRbLpHzXe00Mk3ZzMxNbDvshwIYWsuynbLWmLb4jMqKLr-gq-IMTFmkvWecT9RXCMl55Lr8vxhneOo7XQ7iqSIzxlyeAMYMXXTOT5cJCiJ8NlhNJ3ei9YmMm0AiYH2UZ7sDoKrM3g-Y-pwj8dskx-dQvXsqswaIinSEc_nzcTrNzMekho5eLMI9zRqcF9WXvyKEEZSO5ZunWhu0F3jLEtQ31GUoTUPKWDK5g9GIlVwO8pWWa_E189GMFbl98076-ppsYFYddY9e8GAYK9rIF8NeCGFPtNdqUFpL8-5RQBq9T0AiYFyauJv_-9vqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
نصب و استفاده از Hermes، آینده‌ی هوش مصنوعی
⚡️
فایل لینک‌های مورد نیاز:
https://t.me/MatinSenPaii/4178
⭐️
توی این ویدئو:
00:00 چرا هرمس؟ چه استفاده‌هایی میتونیم ازش بکنیم؟
04:17 نصب و راه اندازی روی دسکتاپ(ویندوز، مک، لینوکس)
13:47 نصب و راه‌ اندازی روی سرور لینوکسی
16:46 نصب 9Router روی سرور لینوکسی
18:10 استفاده از API و مدلهای رایگان قدرتمند Nvidia
21:20 دور زدن محدودیت دسترسی به API ها با Worker کلودفلر
22:40 استفاده از Endpoint 9Router بر روی لینوکس و ساخت Combo
24:31 اتصال Hermes به اکانت تلگرام( و واتس اپ و دیسکورد و...)
26:35 نوشتن یه کرون جاب کوچولو که هر 5 دقیقه قیمت بیت کوین رو بفرسته و تحلیل کنه
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل ساده‌ست و نیاز به پیش‌نیاز خاصی نداره. دو تا ویدئوی قبل رو دیده باشید، عالیه
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/4177" target="_blank">📅 14:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4176">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ویدئو 2 ساعت و نیم ضبطش زمان برد، بعد از ادیت شد نیم ساعت
😭
دستم شکست انقد با موس اسکرول کردم</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/4176" target="_blank">📅 04:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4175">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LtmDxuMnUgIGLe0jkacqE2nsoiaj9jeIb7DgK2cWOJ1KpctyIsRXHhc3nSktw_ksJ2OjPzOhvWJzjgx7VboddZYQLj6Iq5Xqmnbiy5WVUBo2a_0oLDgU2CcdlxBR8pTJnJWvvet0xkmY_wt8doGc3yKwA2dBV9XciRG_sk2mkW9XEg_NlrxLAD6SM9VjOYc0pAA6Np8GWbbP_t_IBP5GO6CtjBjOCYOcYCe3xHqGM5gqKJHJ4wu_5f92rm8Z3nDXzpbDnCyANiu5dG15bCDNGcs86NuopWRUSvoh3GFpQcdzwDa1WCrsOU_weTK2ZZc0_dXfSG9FNpmIBVSHPAZ2bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این وسط دسترسی به Fable هم برگشت</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/4175" target="_blank">📅 01:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4174">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">وسط ضبط ویدئو به طرز ضایعی یه ۱۲-۱۳ بار به ارور خوردم
😂
(اون پشت حلشون کردم و شما قرار نیست ببینید. هاها)</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/4174" target="_blank">📅 01:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4168">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-Desktop-1.0.0-beta6-linux-amd64.deb</div>
  <div class="tg-doc-extra">19.1 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4168" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/MatinSenPaii/4168" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4167">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5LyPaOiNw_csD8sH4NuPJtu9a2AHA9kTmwpjhoDKGQvpIUCaKOAVhOpsB5vm6ZQnSHjLEX4bCDJfyBF07mHUgcU_P9jyW8_QpkUkZkZ4gVxNsXKLf7uQOSqIg4rPwHeDaOjPSiabsDAXTs9M7yi7viVG4BiecfVSxRFarX4iLJoCCbMApS99ooGwnb8X_JRyha0w-YDb0xwS9NymLvud1C5AD04R3DJ95GOgYQCsmjbdGIZIEdGZPftT-Hh9oUw6KTRS9mWgU7PxWlggIQcAXhktY55gNHp0qUI8Ocins6HTtL_XwjSYE60Cbk_GiUQFdIzrtCTouqMVP9DLMWnrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
نسخه جدید WhiteDNS Desktop 1.0.0-beta6 منتشر شد
در این نسخه، ماژول جدید WhiteDNS VPN به WhiteDNS Desktop اضافه
شده.
امکانات این نسخه:
• اضافه شدن WhiteDNS VPN به اپ دستکتاپ
•  انتخاب هوشمند بهترین سرور
•  نمایش کشور و وضعیت سرورها
•  اتصال بدون نیاز به تنظیمات پیچیده
•  تجربه کاربری ساده و روان</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/MatinSenPaii/4167" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4166">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RXDafVaShxCRUfvG-Jw6Yf4fD4jCs5AtHmFNHx5ptvSReRQINacJvy0OYoYUMuCx1TjG02iCgdJWy1ndQbUOkMKM2UlwJDkTLkO_GxBp8P9hgp9HF6_OWcQIRc60Cypp_6nucwi8GaKiM8gMMQMAMgaZPJlRRglrdBHroYkGoMBPKeXIocehMEIequ6sGCqEpLikAEMqPCmcXeRsxO8xKjTOe_vExoFtROGs9-tz8ApNHDDuv6RiEiOcI16JTCrPBL1xO0F_LKHd6q_raQEJM71g-3VXdoCzjPTfMd2M5m0LBS9KHbsMKjd3Tk4nMZXA3F1ILJOnkh5bVqmcv4Y4_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این api هایی که Nvidia میده واقعا سخاوتمندانه‌ست. 40 ریکوئست در دقیقه
با 9router انداختم پشت هرمس، چه میکنه این Qwen و MiniMax3
توی ویدئو آموزشش رو میدم که چطوری بتونید وریفای بکنید و ProxyPool هم بزنید که روی سرور مشکلی نداشته باشه(مثلا با آیپی سرور من مشکل داشت انویدیا که با یه رله کلودفلر حلش کردم)</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/MatinSenPaii/4166" target="_blank">📅 22:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4165">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">کلودفلر یه درگاه جدید معرفی کرده که اجازه می‌ده روی هر وب‌پیج، API، دیتاست یا ابزار MCP که پشت شبکه کلودفلر دارید، سیستم درآمدزایی پیاده کنید. تسویه‌حساب‌ها از طریق پروتکل باز x402 و با استیبل‌کوین انجام می‌شه؛ یعنی عملاً دیگه نیازی نیست درگیر ساخت و پیاده‌سازی…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/4165" target="_blank">📅 22:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4164">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cGPRiXxjjNp9ZTUVIpgV_pP4_MstyN7cTUp0Ds4oJ0W3WZLRPeAlv6pv0F7DR_9AFdj1lpgcVajNWrQo83-Mu2D3CgxZ8G17lweIMFOPz1Y1R-k2yf_NrCKJrx7BwdmgirFM5GZ1S75c-4ri-59lSI_QyUXBqXm5KExmKRTR8wMAZcQUTGysIwV4bn6DiHBFeSecqz2BP2G0m5rz2bUY61eQ49l_r1M7GVUYYUQ63ZyapT2seI4FkGbPLnuqyv9k-eMA7Ww-0l_mIQ34KpG7FNst0x5lJgCnXekgYbYMDrqA8w2NvhJnGw6PhdupETvTkrmcmM_y-dtPpaEDDQZRbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر یه درگاه جدید معرفی کرده که اجازه می‌ده روی هر وب‌پیج، API، دیتاست یا ابزار MCP که پشت شبکه کلودفلر دارید، سیستم درآمدزایی پیاده کنید. تسویه‌حساب‌ها از طریق پروتکل باز x402 و با استیبل‌کوین انجام می‌شه؛ یعنی عملاً دیگه نیازی نیست درگیر ساخت و پیاده‌سازی زیرساخت‌های پیچیده‌ی پرداخت هم بشید
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/4164" target="_blank">📅 22:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4163">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">از بین سایت‌هایی که تست کردم برای SMS، کاوه نگار که باید میرفتی از دفتر اسناد رسمی احراز هویتشو انجام میدادی، فراز اس ام اس هم که شیش ساعت گشتم اصلا بخش API پیدا نکردم انقدر UX اش درب و داغون بود. بیست دقیقه وقتمو تلف کردن این دوتا تا وقتی که رفتم
sms.ir
و همه چیش اوکی بود و 10 تا هم پیامک رایگان داد. خیلی هم سرراست api تنظیم شد از خارج به داخل هم دسترسی داد</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/4163" target="_blank">📅 21:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4162">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">تمام رادار جنگ الان فعاله و AI هر نیم ساعت یه بار، خبرگزاری‌ها و پنج-شیش تا کانال تلگرامی رو چک می‌کنه و اگر جنگ شده باشه و اسرائیل و آمریکا به ایران، یا برعکس حمله کرده باشن، پیامک میده</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/4162" target="_blank">📅 16:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4161">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hNDHM3BCg-JopextW9SRkz9vEe-suhgKSL2U0NLQS6ZDZQn44q1SawcriE7p1EMmFMWZ1xmfT0WuXlRFSo3J006AfXdMcyZvhwt-zl0xwBtlu0nF9vXVHnaHRJbh13sFO5zhrbjeN_9CIMeCnff6y1PfWLYETwtfNqXkrUht1fiOwO5kkmXYBT-7ZZINWkBAGWAZ48buDusT-EGJz2M19mLDwUnCW59bFjYxKUf9iR4WIIdRMe9eB0tw7CSxn1OENAPNqZvlUe8tIVdde1H1-gAuYih2sfkIR6oi9_zdMZfZD_ObNxbyzXYTURrXcWotmIce7V-_bXaAWJw_31dQ2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌خوام باهاش یه رادار جنگ بنویسم</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/4161" target="_blank">📅 16:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4159">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">می‌خوام باهاش یه رادار جنگ بنویسم</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/4159" target="_blank">📅 15:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4158">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ivPw8qGNJJ_44XDsdz77ZsAq2DCjC3ObXD3V5YqShO8FjXROr--ohCGFeD00CRv0hEjOEIFx6Mh2CKU9eA8rOnKmopTSkIOfwg2BW1pgvILIzhCMglVdp_OpTRyt1TFrSiRw9iUUEsVAwnrtN8E1-Rb0x-5yCO13YnbwMxm7_G390MS9am-KIrj1TKApD8Uy8jzwGsnbFLU-mrLbjH4dbLy7Kp_ovXgwp8g4JsjRZiiSSBwHBDKMf9h525fUh1Bu3wNlhu5QaqgCnT9XuOqT3VsFQdPuIIxbUgzN41NYFKu_Fs_lgFiA6TL2Sq5cLDPvt0VdEzUtpjVFED6xubzazA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمی برای خود یادگیری را شیرین کنیم
(دادم همه رو هرمس با gemini 3.5 نوشت چون هم یادم میره چی رو تا کجا دیدم و هم همه‌اش هی چک میکنم که چقدر ازش مونده و الان درصد دارم و اعصابم آرومه)</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/4158" target="_blank">📅 15:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4157">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">می‌خواستم ویدئوی هرمس رو ضبط کنم اما انقدر برق نوسان داره و هی سه راه قطع میشه کلا برقش، اعصابم داغون شد. می‌ذارم یه کم برق بهتر شد میگیرمش آموزش رو</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/4157" target="_blank">📅 14:55 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4156">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">همین الان ویدئوی یاشار عزیز رو دیدم، و باید بگم دیدگاه فوق‌العاده‌ای میده به شما از ai
اینکه دیدم یه سینیور چطوری بدون گارد و با آگاهی و مطالعه‌ی کامل از ai استفاده می‌کنه توی حوزه‌ی خودش، واقعا لذت‌بخش بود.
نکته همینجاست
با این ai عزیز دل، حتی باید بیشتر از قبل مطالعه کنید و دانشتون رو بیشتر کنید تا برتری داشته باشید نسبت به رقبا. و قوه‌ی حل مسئله‌تون رو تقویت کنید و کارهای تکراری یا سنگین رو، به راحتی بسپرید بهش. اگر به مبحث باگ بانتی هم علاقه ندارید، ۱۵ دقیقه‌ی اولش رو ببینید حتما
https://youtu.be/-Rt_Z0allhM</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/4156" target="_blank">📅 13:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4155">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">متا قراره برای استفاده از عینک‌های هوشمندش ریت‌لیمیت بذاره
😐
و یه مدل پرداخت (soft paywall) داشته باشه که باید ماهیانه اشتراک تهیه کنید  لینک خبر
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/4155" target="_blank">📅 13:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4154">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R7Z74pfsNSBBA7nmu2lKpsCQGlCi2LcZwjAGsvR-V2qJKWSQ0B0SgT4q_p7qmgSkYzpDqYyQdWM2JbZ4GuHOESEuvArJWPf9O8J4vINZiUzfjZcDEhQaLdio5PfMPdNTMmKb79oTJjeiBFbrZ75cqzl8Qg8BcjvBUmmARWhA9vM-k_ssJSOwL7sYkF1af4VsxEPgvCGSrtpsZvQgaXrjVjzid5TOsIJ2wUqRmpxxaqmrhQjoV7Ofa0LHvmZWj8rFhDx8he4IebTq4uTCSPTqJBIYsfsleMzjOybttZIRMCu0ufj1cmgq7oHrhJC9U5MxAeq_CU916jF0n63zw0HNVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متا قراره برای استفاده از عینک‌های هوشمندش ریت‌لیمیت بذاره
😐
و یه مدل پرداخت (soft paywall) داشته باشه که باید ماهیانه اشتراک تهیه کنید
لینک خبر
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/4154" target="_blank">📅 13:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4153">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FtLUE1Nq4QxdimBGXmbRyWwg9UM9hYbHL8XiO45T-qIEwBFV4wQIJY5nIC-DIMa9k8_EotHP77leP-Gy2BckUtqaBNiAPOyL8wvoy5Deu4to1LeOR0tmC5K5flAp9l93fXzpBzZvxIluT4Y30MFGUE2r1cY4RZ7iclzGI8G5QkG1M4vZeKGcTGlG4U6ZIpvsaG5w1LNcGyGCxSaXM7iEaWEFwDWZOhN_RqlajrO-KANNRm54FzMYo9EpPSLn3DxtY2afx5RauB6rZG07okV5DxjILPHHGbhMqnkWDhcpmlJXNzyfzKoTSFPyDL6bkZmGJj7YEMbYqt4r2QCG48bT0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غول چینی، GLM 5.2
همچنان ارزونتر از حتی Sonnet 5</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/4153" target="_blank">📅 10:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4152">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">خب گویا کلاد Fable 5 امروز برمیگرده
😁
آنتروپیک گفتش که با دولت آمریکا مذاکره کردیم و امروز مجددا مدل رو آنلاین می‌کنیم</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/4152" target="_blank">📅 10:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4151">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ulmxRfqkFhWV45FLLeVOfNfM4rWewQGlD8gZaJZdfqW0AQZqXbqVWNnWg1md6Bsa-NW9UWlYQPPesu-RsPW0ztaw8j-UAZ0LexhywrmaldY8wEVw_wKTKQvy7Fe2lA9IJ5lcCIN_lsrGosDAYhasgahvO5-CwtvujZRl-Cqve-0yMNZ-Sr88exMw1-S516SVodqnsglMyu488QmOwPm3cKvpf2Sn4CUdHQI-_NROnhesiqkzQ6sQHn1rGySCVSDRxaVoBtYElqQr70OUo_Rx1NK-yh8z2RLrpn0EazsFAuyd_qWDEH5kUYhS8Y6krPSNxrpVQcyNDYeo30r-F3xYUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انقدر هوش مصنوعی‌ها چند ساعت اخیر آپدیت دادن که نمیدونم کدوم رو برم تست کنم
😂
وضعیت عجیبی شده</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/4151" target="_blank">📅 01:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4150">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">انقدر هوش مصنوعی‌ها چند ساعت اخیر آپدیت دادن که نمیدونم کدوم رو برم تست کنم
😂
وضعیت عجیبی شده</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/4150" target="_blank">📅 01:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4149">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f2ffa3ab51.mp4?token=bgTIn6IPSNuTP7IaLGcdSgLap4akFz_t7eflMVKCRZFDr69rSMWCW8arftRxOm4nOAKdpc1EMan3slFPO5jrJ6UUBBj9Zunh_ZqYuc_WJ4cJC1uHfibUnVPrnv15g-gYn0UyeTr6tntjI_y6SclFGsKPs5tPXfjtuND1AK3pX1a5CuX-5ErxY5HSpc3f9Bu0gybQz1s4Z55MvEXLiAniUS4_uqFqEz08dGaHjRNBIeIg4-6JgEoTVQBwvZDKpnXt0_-NU5eNkEY82icxZ1FlkdQU6lH7P4yX_c2pT6LfT5p-uGWqkhq_iNu0Ey-XMYzcbLF9psQfH0_ympVQAIHjrA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f2ffa3ab51.mp4?token=bgTIn6IPSNuTP7IaLGcdSgLap4akFz_t7eflMVKCRZFDr69rSMWCW8arftRxOm4nOAKdpc1EMan3slFPO5jrJ6UUBBj9Zunh_ZqYuc_WJ4cJC1uHfibUnVPrnv15g-gYn0UyeTr6tntjI_y6SclFGsKPs5tPXfjtuND1AK3pX1a5CuX-5ErxY5HSpc3f9Bu0gybQz1s4Z55MvEXLiAniUS4_uqFqEz08dGaHjRNBIeIg4-6JgEoTVQBwvZDKpnXt0_-NU5eNkEY82icxZ1FlkdQU6lH7P4yX_c2pT6LfT5p-uGWqkhq_iNu0Ey-XMYzcbLF9psQfH0_ympVQAIHjrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شرکت Anthropic از Claude Science رونمایی کرده که به صورت اختصاصی برای مراحل مختلف کارهای پژوهشی و علمی طراحی شده.
توی این نسخه محقق‌ها می‌تونن کدهایی که مدل می‌نویسه (Artifacts) رو به طور دقیق ردیابی کنن، محیط‌های اجرای کد رو بر اساس نیازشون همون‌جا بسازن، و جالب‌تر از همه، بیشتر از ۶۰ تا دیتابیس معتبر علمی رو مستقیم به کلود متصل کنن تا تحلیل‌ها روی داده‌های واقعیِ علمی انجام بشه. این نسخه فعلا تو حالت بتا در دسترسه.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/4149" target="_blank">📅 01:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4148">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9603918fce.mp4?token=IzPSnddCfh34nxmSnqhMqBtLcIL1dgTmz_ea9aMH_dLd8RvFav3ABmk2I1c5-6wTf6POGR9w4b64WbTj1ZrAa1XaKAmoKd_2fntruokp7kKbAtAtU-jqN7rjyXuNVM1NvNFfp7pij7-UhoqGmRryjDgOjC46yAl4MFy0tpVz4y9Hh22hS6JnEGktqzKfggjt7ttS_hftZ4xsj93kt3KdP7R6JriJIQqL5vKZ-lM8LO91MsdKZU9x9sOsho9Fgt4JrXUCJefSKgR6QB_6tGJBsGgbg03uabVSLa76kHYcaibB_vm66ghDTwDlVtzqt3nXDOHqnPIhP5Z1Y3eSWMCRWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9603918fce.mp4?token=IzPSnddCfh34nxmSnqhMqBtLcIL1dgTmz_ea9aMH_dLd8RvFav3ABmk2I1c5-6wTf6POGR9w4b64WbTj1ZrAa1XaKAmoKd_2fntruokp7kKbAtAtU-jqN7rjyXuNVM1NvNFfp7pij7-UhoqGmRryjDgOjC46yAl4MFy0tpVz4y9Hh22hS6JnEGktqzKfggjt7ttS_hftZ4xsj93kt3KdP7R6JriJIQqL5vKZ-lM8LO91MsdKZU9x9sOsho9Fgt4JrXUCJefSKgR6QB_6tGJBsGgbg03uabVSLa76kHYcaibB_vm66ghDTwDlVtzqt3nXDOHqnPIhP5Z1Y3eSWMCRWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نسخه جدید Hermes Agent سرعت خوندن صفحات وب رو ۶۰ برابر بیشتر و هزینه مصرف توکن رو ۴۹ برابر کمتر کرده.
تیم توسعه‌دهنده‌اش، Nous Research،  با حذف پردازش‌های میانی کاری کردن که دیتای تمیز مستقیماً از بک‌اند به ایجنت برسه. همچنین برای صفحات طولانی و سنگین، داکیومنت‌ها اول روی سیستم کاربر ذخیره میشن و ایجنت به صورت صفحه‌بندی‌شده و فقط در صورت نیاز اطلاعات رو می‌خونه.
این تغییر یعنی کیفیت تحلیل و پردازش هیچ افتی نمی‌کنه، اما زمان و هزینه‌ای که بابتش صرف میشه به شکل چشم‌گیری کاهش پیدا کرده. و یکی از نقاط ضعفش یعنی مصرف زیاد توکن رو پوشش میده!
کم کم تیم Hermes داره یکی یکی مشکلات محصولش رو برطرف می‌کنه و امیدوارم همین شکلی جلو بره
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/4148" target="_blank">📅 01:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4147">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qfRp9iQBk4fd3xJC0nebpoy_9E0Q_Nba2mI27pG2AfudiiM1BlwudxiYvRhZSG5N_nt79jTzZdAS-pV1nuNzXIjCQYJ6W4HNetKgH0-6GeGC538CYUGW8_g5B5tyHHKj8XVEDHu2aCRy-ZDXzibY9z4U_DRyG6-W9ODF6D0qqqpFcLu53fmLLvRvLS3GQk08lIReoXGLfHcmGyaff7MfekipyFHtBY4IMLfY3A50b4v7mIhXD3eR9sXSjfgWdMQ3bYu24YaIbtUA69Ol33IVVS7GX6kUQIuwhYHJkktQnkVAv_p6ejlZl1pHBJFl_B4TnGxvFTVbHhR1xTJKEpqVcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم بنچمارک منتشر شده توسط خود کلاد</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/4147" target="_blank">📅 23:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4146">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k6aVAlAB0lWfqcWU1wAveR3C5NPARVqA0pcUQMZ6l5SsGg18wZbDfTrq-ES-_1fP7jgp0mNKCtayaRCGoNWW8HZuYw_BZFnefk_LbkI_CniTam1XqAj2IT7RuXlczsc3Av8M5f-GrpahsgUz5NMxZDckT5D9GC3zVIYgKevf2PVu6YEuHHlDZ91eun0eJLrAPuxgSDks-mw6DeMQR9ntg9wCxyfZvd9hqBWOStJY46klxAjdhRYwwzrWn6jzUG-7JCQqXVTGyX7iVlid7AwNa5TWIVWDUlDyDNyp0FFrQ_ZRTtNmSfJWG9gKpdh_sQFf5X8xgtJMjxvDchSMGGnFZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسم‌الله‌ آنتروپیک Claude Sonnet 5 رو معرفی کرد همین یک ساعت پیش</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/4146" target="_blank">📅 23:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4145">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EP0nuCdT9SEuG8Gsk77e3AMForYMcFp2zArxbWemG71-SlEHc-Ap_QLkyXtsAcJxjDwPj4idhvt0XJoi7JSsh1RtEgD1TCCHhY0-t4RPHBkPbz5jUjnLub7vPaw_wj6h57sHI_cbgaGY0VCOIV3e6d9ahRisqHnrn2W8h8EoMNd1o2gxlj-PsNQgK8A-Doh76VFd2CkS2Cr8SLcAZCKsb-KCgBzBJBdgW3yQseZQzyeicK4Jm-l23fFGIgfL-K9K04FGCuWohMihdNS_czsoo7IRs3sbCx0CNbrutoSnakTiUPJVeZ3xCR-pIbvTfa68hGnNxpaiMNO-o5Bc8Vzx3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسم‌الله‌
آنتروپیک Claude Sonnet 5 رو معرفی کرد همین یک ساعت پیش</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/4145" target="_blank">📅 23:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4144">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">پولسازی از طریق کانال‌های انیمیشن کودک با کمک هوش مصنوعی!
🚀
تا همین چند وقت پیش، ساخت انیمیشن برای کودکان نیاز به یک تیم بزرگ (نویسنده، صداپیشه، انیماتور و موزیسین) داشت، اما الان با ابزارهای AI، یک نفر به تنهایی می‌تونه یک امپراتوری محتوایی بسازه!  این ویدیو…</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/4144" target="_blank">📅 23:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4143">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAiSegaro👾</strong></div>
<div class="tg-text">پولسازی از طریق کانال‌های انیمیشن کودک با کمک هوش مصنوعی!
🚀
تا همین چند وقت پیش، ساخت انیمیشن برای کودکان نیاز به یک تیم بزرگ (نویسنده، صداپیشه، انیماتور و موزیسین) داشت، اما الان با ابزارهای AI، یک نفر به تنهایی می‌تونه یک امپراتوری محتوایی بسازه!
این ویدیو دقیقاً به شما یاد میده که:
✅
چطور کاراکترهای ثابت و باکیفیت طراحی کنید.
✅
چطور با استفاده از AI سناریو و موزیک مخصوص کودک بسازید.
✅
چطور انیمیشن‌ها رو با صدای کاراکترها لیپ‌سینک (همگام‌سازی لب) کنید.
اگر به دنبال یک بیزینس مدل جدید و پولساز در حوزه هوش مصنوعی هستید، این آموزش گام‌به‌گام رو از دست ندید.
ویدیو با حجم 300 مگابایت اپلود شده , از طریق نسخه دسکتاپ تلگرام میتونید با حجم کمتر دانلود کنید.
〰️
〰️
〰️
〰️
〰️
〰️
در صورتی که مایل بودید میتونید از لینک زیر دونیت کنیدتا قسمت های بعدی و موضوعات بیشتری پوشش داده شود.
🌎
donate.isega.ro
〰️
〰️
〰️
〰️
〰️
〰️
📽
زیرنویس فارسی
🌐
ترجمه این ویدیو با وب‌سایت
isega.ro
انجام شده — حتماً سر بزن!
📌
برای دیدن قسمت‌های بعدی کانال رو دنبال کن:
📺
🌐
@AiSegaro
🚀
هر روز یک قدم نزدیک‌تر به آینده‌ای هوشمند!
📤
بازنشر آزاد با</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/4143" target="_blank">📅 21:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4142">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sJCtm93oRm2L8_0ZMscuv686Vwu1Or0N-9hf1ihDbYSxhQxK7iyaS9mfTSHE0LtsIiUaSZZd2pn3naFTeu8AsDneD2ZoEpCSRq3hPgvSEtxKt7Ms7oETvh-P-qZdh1zlwUpkI-70KTvBBKcUmU56h7Gvyh8O92Lliqh42HhZcOPgXqNClpraLKDAt0lQSJa0JMYFZ90lwohll73GQSadympc3CBAl0nWdNGNLyydUI-wULD38uGbpMuIaghP2WwSTwXfh7_S2ffES2fYw5_ZSi1LA8ySGFp9opsn2bZXJCctgOad1vCJv8rW12AIHHaOLTEPvjnpB24KP_Q1b0oUDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوتوب یه قابلیتی آورده به اسم Ask پایین ویدئوها، که می‌تونید وسط ویدئو اگر جاییش رو متوجه نشدید از جمنای بپرسید
🎨
فعلا برای وب فعاله گویا</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/4142" target="_blank">📅 21:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4140">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">برای نصب کردن 9Router روی سرور اوبونتو اول sudo apt update && sudo apt upgrade -y curl -fsSL https://get.docker.com | sh sudo systemctl enable --now docker و بعدش این دستور رو بزنید docker run -d \\   --name 9router \\   -p 20128:20128 \\   -v "$HOME/.9router:/app/data"…</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/4140" target="_blank">📅 18:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4139">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">☠️
این شکلی از هر API ای استفاده کن برای هوش مصنوعی🫪
⚡️
لینک سایت 9router: https://9router.com/
⭐️
توی این ویدئو: 1- یاد میگیریم که چطوری از اینهمه API Key رایگان استفاده کنیم 2- ابزار 9Router رو نصب کنیم و این API ها رو اونجا جمع کنیم 3- کلی API رایگان…</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/4139" target="_blank">📅 17:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4138">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">انقدر برق رفت و اومد و نوسان داره روی محافظ میترسم لپ تاپ و همه چی بسوزه آخرش. آقا بیا قطع کن همون دو ساعتو، نخواستیم</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/4138" target="_blank">📅 15:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4137">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">بیشترین درخواست توی یوتوب و توییتر ازم این بود که آروم تر صحبت کنم
😁
من فقط نمی‌خوام حوصله‌تون سر بره یا وقتتونو الکی بگیرم
اما از ویدئو بعدی سعی می‌کنم شمرده شمرده تر صحبت کنم</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/4137" target="_blank">📅 14:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4136">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hvBvHeaWJJeUc90IFxTAS8-cPV0Uvz6A-90wka4InU7LwzQsX7GO3iPYevt3CJFi4ddvv4ANWSpK7z8_IGSK6Sab20DxcseMBeo5w-uWE7ELzpQJJMfHc6bnq0TmS7cN60X6_qU3U4SEd8wVnVqzXkLT3CyCmykJCjZ7kVQcFvD1p9954uAiPJD9cQim3re0-i9WI-fmD56CCIyUMkxg5fvHc6iI7lpCGbXZfV32Z3muM5GkbzClY-HgX9gx0A281kJg-ZCn8l8Nv0i6R2Q20Ph7VOLudxjRWPmkoLs2cfIIJ2Z3pEdOOdI4TZf7yl2PxW155CwBu2yBH1DRuk477Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مورد نسخه‌ی موبایل Hermes، من توی ساب‌ردیتش دیدم که یکی واسش نسخه اندروید ساخته و Pull Request زده روی گیتهاب(که کدش ادغام بشه) منتها هنوز، رسمی منتشر نشده</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/4136" target="_blank">📅 14:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4135">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4135" target="_blank">📅 14:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4132">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/adFhrmF4hOYfdkwdi6XcW7fQmw6tkXbnt06y3VBNm8vKMstsyQvL6t5JkP-CdKa9vtBt-v3jHvLZwYqcORStrs_b3cJKh6dE4amBkP--eSed6Kh5qrE3AZt58bGnw_trs4mjaHMO7MhLfw4z7dIey7RvDZ2UnMup3FHF-RNDT8pXK4_NfsONWqDEbJ1DpGAKhTn4XFRRczuQaZ9izzwWiz-Vxo6ELeSLGViVMgVMj4nvf2EgBfWY8hRDqRSuaPN9vKuXXpJiAv3J1o-urpM_4CsRaEdlcsRHvpTSQ9xhwib-vW6TvXBXS5UA2mhemErAhEfUiXDgH7zb3slut1ufwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gIITl_IRCqXW21zDGAzw0g2Rd4AFjEAL2ImOvIJmG4w-gEGEQswOYQjaNfs4WNb4HNk55AwTxR2E2tgxrICytkUegOpS9tmyRfxSHm1z_9finfMS5hip60KaIUXw3EyTSv9ffr-mAyWfV0ITIvSSSXpEzKtoq9T6Olj1ikcfWjpCNRVuLv0E_9G5mAeV01PWWIECqRq5qb7pKjZz7uIvGtVhjzOlDqgQ38rVawCnZ-yD9T3_lB0ijAQ-v7fCvRaC6_HuKIOkEEzyDDY407jL-lfxYdknhcsHBrM2UlQK-f0JcvXyeOSHCjfDTyyV1YeTvUx6zPO3joAVUmjmtojLWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/u6N0NWQFzQHUz2uVrhkcJGxknMEr04a9x0gLVGBUKy8r9mpmbbCFMkzPkzHa21XUsE_nS2rhnD-y8--SIXXMdj0gWCSbN9nBOnrM2Qqbo5YJaWnkB3pdDtq1pDirqbps6O_oFcUlpjh-exoJjMg_Y_6G1gA39IS3oPzdEY7n0iJENd6_hRbFABaxKbem9FsS82I7Xnfxua-PQlnhGaOv97-VBp0kWA2ZOZyLA0MeYZJ-yCxsKydbHmEiqlb3u6srxPjisQE2IuhFlPr3-oanMznBaPtP04mwzsmOmTEyqKGLjwlqooyTT2MSzCKuUJq19uDDULqOrD2ufMi03DJH6g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">واقعا Hermes و وصل کردنش روی تلگرام، یه چیز دیگه‌ست!
فقط کافیه ازش بخوای، و بوم
انجام شده. ویدئوی بعدی، هرمس هست
👀</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/4132" target="_blank">📅 13:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4131">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🚀
اسکنر WhiteDNS  اسکنر WhiteDNS ابزاری برای اسکن، تست و مدیریت آی‌پی‌هاست که در دو نسخه در دسترسه:
💻
نسخه دسکتاپ مناسب برای اسکن‌های سنگین، سریع و حرفه‌ای؛ مخصوص کسایی که می‌خوان تعداد زیادی آی‌پی رو بررسی و تست کنن. https://github.com/WhiteDNS/WhiteDNS…</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/4131" target="_blank">📅 08:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4130">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAZYSC72OQKJOhCK4EBcAdioUEvB9OI-Oyflh9pValOvCuwoL4s66CuHTJDrBcsu8Ifu9pAGHO9Sb4pQwxZ8dmCFUk7iV9IZa7ewHARbr1uzISXgzzxnB6jmgAJQ-32keALndrcWgM1Xe65RMBui3G7qFX0E271Sbgsfg20RwNFrmNnyD5dVk1UlTd9llZI8yWnmR4SCzkwk6D8sIBfO132HAxpKilDu4dU4fjNGPtu2ZAaVCGWyjQdOy3E-ZxpCfS5YVxHX_j-I1LzCCT6j0kn-Qnn7HmhELRMQAMpa4BS7VLttOItK-xzWVSKbR--lHuJUjamIAyFIPhbKStAxVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
اسکنر WhiteDNS
اسکنر WhiteDNS ابزاری برای اسکن، تست و مدیریت آی‌پی‌هاست که در دو نسخه در دسترسه:
💻
نسخه دسکتاپ
مناسب برای اسکن‌های سنگین، سریع و حرفه‌ای؛ مخصوص کسایی که می‌خوان تعداد زیادی آی‌پی رو بررسی و تست کنن.
https://github.com/WhiteDNS/WhiteDNS-cleanip-finder/releases/tag/v1.3desktop
📱
نسخه اندروید
سبک، بهینه‌شده برای موبایل و قابل استفاده روی گوشی، با امکانات کاربردی نسخه دسکتاپ.
https://github.com/WhiteDNS/WhiteDNS-cleanip-finder/releases/tag/v1.3
⛏
قابلیت‌ها:
• لیست آماده از ASNهای ایران و ASNهای معروف داخل اپ
• امکان وارد کردن لیست آی‌پی دلخواه
• Health Check برای توقف خودکار اسکن در زمان ناپایداری اینترنت و ادامه بعد از پایدار شدن اتصال
• ادیت یک کانفیگ و ساخت تعداد زیادی کانفیگ روی آی‌پی‌های تمیز با چند کلیک
• استخراج آی‌پی از داخل کانفیگ‌ها
• تست سرعت دانلود و آپلود آی‌پی‌های اسکن‌شده
• انتخاب پورت از لیست آماده یا وارد کردن پورت دلخواه
• لاگ پیشرفته برای بررسی لحظه‌ای روند اسکن
• خروجی کامل و دقیق از نتایج اسکن
متدهای اسکن:
⭐️
IP Scan
برای پیدا کردن آی‌پی‌های تمیز از دیتاسنترهای داخلی و خارجی و استفاده در کانفیگ‌ها.
⭐️
HTTP Scan
برای پیدا کردن آی‌پی‌هایی که امکان استفاده به عنوان پروکسی HTTP رو دارن.
⭐️
SOCKS5 Scan
برای شناسایی آی‌پی‌هایی که می‌تونن به عنوان پروکسی SOCKS5 استفاده بشن.
⭐️
SNI Scanner
برای اسکن دامنه‌های موردنظر روی لیست آی‌پی‌ها و پیدا کردن آی‌پی‌های مناسب برای SNI Spoofing.
⭐️
Speed Test
برای تست سرعت دانلود، آپلود و Packet Loss آی‌پی‌های اسکن‌شده، همراه با رتبه‌بندی خودکار.
این ابزار برای کاربرهایی ساخته شده که می‌خوان با دقت بیشتری آی‌پی‌ها رو بررسی کنن، خروجی تمیزتر بگیرن و زمان کمتری برای تست دستی تلف کنن.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/MatinSenPaii/4130" target="_blank">📅 08:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4129">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5950435463.webm?token=f4kIcIUIODU41ovUCME5OEZFEaB3_X8PkwNdhxq-PiFCGhZkuGbK6KoPI1UkFQoKhK33t3ykQSn0Ak3l3uyQHYVRfFb0viALPRC8noKFABP0MtFc1GKVXiYSldtq8S2Y_7Sccp5wBCq4HBQMv9xi5nvy0gK9NZwfKyfWRTfFw33FLyzo_yQeS4p3BBAi8KR9FovgNtM6V4vbebDR4QrWt6Oy4fdubNqsZYuBQbfbSV2_rRoiW_upIN34IAC9E2oaYiKcZDUe7lTM9XfMkz6SWoBrMYHQt-VQPrJly5ipm6LG-Et2wPdXysVrAt2b4HRPVglAONI6ml_NhMUek6-sSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5950435463.webm?token=f4kIcIUIODU41ovUCME5OEZFEaB3_X8PkwNdhxq-PiFCGhZkuGbK6KoPI1UkFQoKhK33t3ykQSn0Ak3l3uyQHYVRfFb0viALPRC8noKFABP0MtFc1GKVXiYSldtq8S2Y_7Sccp5wBCq4HBQMv9xi5nvy0gK9NZwfKyfWRTfFw33FLyzo_yQeS4p3BBAi8KR9FovgNtM6V4vbebDR4QrWt6Oy4fdubNqsZYuBQbfbSV2_rRoiW_upIN34IAC9E2oaYiKcZDUe7lTM9XfMkz6SWoBrMYHQt-VQPrJly5ipm6LG-Et2wPdXysVrAt2b4HRPVglAONI6ml_NhMUek6-sSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/4129" target="_blank">📅 04:39 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4128">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">☠️
این شکلی از هر API ای استفاده کن برای هوش مصنوعی🫪
⚡️
لینک سایت 9router: https://9router.com/
⭐️
توی این ویدئو: 1- یاد میگیریم که چطوری از اینهمه API Key رایگان استفاده کنیم 2- ابزار 9Router رو نصب کنیم و این API ها رو اونجا جمع کنیم 3- کلی API رایگان…</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/4128" target="_blank">📅 03:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4127">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N7UJafQKYIznGctpY9gv5XNFYsrTnfUGxG4DugiBLui8I-g9OWjI5iCiE1EGVVoLI5IPHIgcUI895yITMS1difEuW7C1D9IfjFBT7sJ7ssfHbIJf-NCO0yczM47DaPHK-EtTL4YIydDFvg3hvxzC8SZZJn8iZzscjuGTP5c50247RevnWLMDikWbJ2pPR0MsnLoXew4tIUyjLeD63mregecJ-Wcpz6yE9ZE_gAe7VlVsJdYdVd0CMOu1YQUHAyjnrq2OTDReIXzkS-aJXt5W_LFgHDvV9jIiEUdaEz66O8L5cjFpACl62rTnzIBgRIiXDLcNX-3q5G4lqzEDWDosqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
این شکلی از هر API ای استفاده کن برای هوش مصنوعی🫪
⚡️
لینک سایت 9router:
https://9router.com/
⭐️
توی این ویدئو:
1- یاد میگیریم که چطوری از اینهمه API Key رایگان استفاده کنیم
2- ابزار 9Router رو نصب کنیم و این API ها رو اونجا جمع کنیم
3- کلی API رایگان وصل می‌کنیم بهش
3.5- اگر تیک آبی توییتر داریم، به راحتی از گروک 4 و اگر جمنای پرو داریم، از AntiGravity استفاده می‌کنیم
4- از امکانات 9Router مثل Combo استفاده می‌کنیم و چندین هوش مصنوعی رو توی یه مدل فرضی کنار هم میاریم
5- به ChatBox و افزونه Cline وصلش می‌کنیم که هم بتونیم عادی چت کنیم، هم بتونیم کد بزنیم باهاش
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل رایگان و ساده‌ست و نیاز به پیش‌نیاز یا هزینه نداره
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/4127" target="_blank">📅 03:33 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4126">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">وسط ویدئو متوجه شدم اگر کانکشنتون با api ها خصوصا جمنای قطع میشه هی، می‌تونه مشکل از proxy-ip یا آیپی تمیزتون باشه
گفتم این نکته رو بهتون بگم</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/4126" target="_blank">📅 01:28 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4125">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">کمی ویدئو API بیشتر طول میکشه تا آماده بشه
صفر تا صد تمام API های هوش مصنوعی رو میگم بهتون
محتوا رو فدای سرعت نمی‌کنیـم
🥰</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/4125" target="_blank">📅 21:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4120">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitedns-v0.0.8-arm64-v8a.apk</div>
  <div class="tg-doc-extra">18.9 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4120" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⭐
نسخه جدید WhiteDNS VPN 0.0.8 منتشر شد
میدونم آپدیت کردن این سرعت یکم برای هم شما هم من سخته. اما تونستم دقیق مورد رو پیدا کنم و فیکسش کن
ی
م.
ممنون از تمام دوستانی که نسخه‌های قبلی رو تست کردند و مشکلات رو گزارش دادند.
⛏
در این نسخه، مشکل لود شدن بعضی سرویس‌ها مثل یوتیوب و اینستاگرام برطرف شده و اتصال‌ها پایدارتر شده‌اند.
✍️
از همه شما بابت اختلال‌ها و مشکلاتی که در اتصال داشتیم صمیمانه عذرخواهی می‌کنیم. ممنون که همراه ما هستید و با گزارش‌هاتون کمک می‌کنید WhiteDNS بهتر بشه.
تیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/4120" target="_blank">📅 18:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4119">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">اگر نمی‌خواید این بلا سرتون بیاد و کس دیگه‌ای بفهمه ای ایران هستید از وی‌پی‌ان‌تون، از نسخه‌ی جدید WhiteDNS استفاده کنید</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/4119" target="_blank">📅 18:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4118">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ولی GLM 5.2 واقعا عجیبه. قیمتش روی api تقریبا ۴-۵ برابر از Opus 4.8 کمتره
این چینیا چیکار کردن با آنتروپیک، خدا میدونه</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/4118" target="_blank">📅 18:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4117">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">☠️
آموزش استفاده از هوش مصنوعی MiMo Code + پروژه‌ی ساخت ربات تلگرام با AI
⚡️
لینک‌های استفاده شده توی ویدئو:  1-فقط گروک استفاده شد. ویدئو رو ببینید متوجه می‌شید: https://grok.com
⭐️
توی این ویدئو: 1- یاد میگیریم که چطوری از هوش مصنوعی استفاده کنیم تا ابزارهای…</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/4117" target="_blank">📅 11:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4116">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">تمام سعیم رو می‌کنم که سری ویدئوهای AI، برای همه‌ی مردم مناسب باشه. تنها خواهشی که ازتون دارم اینه که نترسید، وقت بذارید، و ویدئوها رو ببینید و کار با این ابزارهای جدید رو یاد بگیرید
🥳
خیلیا که کمی از این فضا دور بودن، فکر  ما داریم راجب چه چیز خفنی حرف می‌زنیم و ...
در صورتی که شاید تفاوت درک و دانش ما از این زمینه با شما، صرفا دو سه روز کلنجار رفتن با ابزارهای مختلف باشه! همین.
به محض اینکه کم‌خوابی ۳۰-۴۰ ساعته‌م جبران شد ویدئو رو واستون ضبط می‌کنم
🤲</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/4116" target="_blank">📅 11:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4115">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YA_vyIbP99dA9pDQCzeYtib5DKyADKnol9OsOrne2dDohpQq6V81Peuieqjkm4t_BtnFypAhchBZaslNIy8THCm9wGSESsvSprPkzCV8liO2g83poD9dVt92z8LyWdjTE4NAz36DxX6yoHuUS2_gdOQPl-wyxdRn5w1KOX19eP4o1BQKriASeonF5vXgIqaY5ZDrCBe6myBzdcDb3NsD6CeNAZTmOSFog1dM3vGucgujsCa306rGQRP54U2jOQ4IqDIRzgYZ1ytjWRY9FVwpuex6ZESh_aBL3pU0rmoYP801RkFhJc--_dZ5Po6igukCCLDSyWQIJABoporNhHOijg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت هم دقیقا شبیه همینه حتی قالب‌هاشون یکیه
😂
https://api.bluesminds.com/register?aff=drPB  ۱۰۰ دلار میده باز هم میگم مراقب باشید و توی پروژه‌ی حساس استفاده نکنید</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/4115" target="_blank">📅 11:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4112">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nayWjV2EWN0sToasYfH0MxHUGvZXdNzrZM6I-wJizFLwmo-oQC9wvKYHiLPOkXMYxczn3DoO9lRSMppmdbQa6mI07-Mbogz-1KNiRTuViWvtpmJMdhLrtRpZekxdznfwOHvOxh4TCMg6Q91RNLx5wAYAjqz6n4-MRNR5sqA54jlU3xiJvU7A5JsdZC42OBHpj-6F8VdkQxcmWkPA_qk4l755TImZAVWlxz7A8dHTDmplYXrYjXuUl0o4YaODcjuGtaHqyW8engCHjjN0E1PhZXDkgkURO3Kv81EC9TmncDC7DoUqvjw4SFQorem0BEZ1xbidQ3EOrfMY_7MZGiz2Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nGztyc-DqfBvWkAR74IJVAOAxbK59byV5UZfWPmGq9LHRz2MHX7XrpfwTkrSX7mAo8NozLvb4XLObSBVLH3OPB4EN_ee6haHQZNPtyluK_jAWhBHzJPN_yMbMH1gcbEDshPxAwZJFL-vD7Z8ztr1aGf2pTcBzR2-CiwaY60N3K1xExxHJmcN_dJKrSjPOHosy_wPbtGwT4cGIsKzc1SiBaTboLiLhuTyRAa3PIiNqocy_PYYjFntoeRbhat1Ax6lL1su_ba8sQ3G17O9mFq5LOkybtzn_aS5A26J4sZ1H-wprlHTElrGI8aM4T9h6VaPMJ__RtGUcu_4FOM0KPnFEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gC6dzVAcNwLaklUZsLG1WsnrvSbQqnHxyT75Z0nBX2TwegTsoqH433UaFOw8OgY4xE48Cma_PfHXHydyQt8Y2PESAh97E9LyCA9JksY8Uvrt7CXpMFjCq_wMF7okDou6a9UyshiZrTWfyl3u7Rr4vKxbuU8Kf6l89vSVo7uNo_uvckMUk6wq0oD3lr1g9uwp2H5fQVAZ7jmqmuZ4JVQAtFR74UdcKBys-CT-QaO1jeQtpNkMK44XBAtRxJV9gHvJCulhR2-ad9wr5MIzSB-0ebVusXKO2U9Bzqz3hWrhWlE05S9EzsYyVwE-gTIKB_5bHZ3xDhGIHZnk-QX7OdGF_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یکی واقعا داره پول میده به یوتوب که ایرانیا رو به دین مسیحیت دعوت کنه
این تیکه هم از یه فیلم بود. دوبله فارسی
😂
😂
وبسایتشون هم بامزه بود
https://daneh.online/four-spiritual-laws/</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/4112" target="_blank">📅 08:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4110">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/k_pYwZE3Q_OluVQMlljHIb8_7BlZeLZSAEup39d7b5g1-5fPZiSBawI1TUz6uT3oamoeAiRdnl1Eg4q5Yydp1ZC57td5JNtMg0WBH_EmOHqRNofKpIzmpRfmlrx9qsf9D4_KOBkkvFyy2MWOW-eUJ29QnaKD2ETyNSo8z1UIBnPdR52H9JsIOoYHnY9Ldd8PGsfLZGZMztThko34bCK5zBAs0-ex0Nxsn0XzhkXSkqwguGlzgpMnLEjuGmywBpKVvfrJsaabJXuUkU_GAGtt_3TFa4fukhShxtbGEJ02itXlic-vx2DkUzRLrVGsp_lSTbttbB9TfKO9nkS4gQk0hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/N-7N5wiDOEPJ0eUmCbZy35vQaqH0LddQX0xE_GFjZfXAN-kMUMRotHH5XBx4XgNRGF1fyj2PdbW9fuSUZ7wUCXjqe4d70BQQwY9d9Yve9W1ERr7zSlsMJWl9sW1oEtYmUx1hrdBf4b9i1HS6OE8Obw-xr580_Y11rLZlW73SpLnACXSzNK9vgxTl-hCQH0-0bmhuUNbVqEJf5fBqG5KsiizEhsVJiKzvSL_9lSPPgMWEkih8rMcTDyzknPA6lGNzZINGqls3-SAh7VkMK46auBRBFe-Sxt9JFHQhSNPRIezqVjYuE6sAdBNBde48T8F3-fv1RuEU2k5fxF8RvZBRNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگر حواستون به توکن‌های Hermes و ستاپ درستش نباشه، اتفاقای خوبی نمیفته:)) همه‌ی اینا برای یه تسک ساده. بهش گفتم برو نقدهای منفی راجب Berserk رو بخون و بهم بگو 10 دقیقه طول کشید و کلی توکن سوزوند با gemini-flash . اما در نهایت، نتیجه خلاصه و عالی و دقیق بود(حاوی…</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/4110" target="_blank">📅 04:07 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4108">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ddDd11XtiXgldRWJNOtkk9ga-yHarc5Kez2HHedhLiZZy9G-9gBgwXJvdQexwaXjZFLEOO2RfdVsIChudyccZIs_guy3KCh2aq_IEmPjHks9grlPha69PWEC3KKSTxYWcjDMtqvp4-sXQI4zjrtStpTxh0rnt1pmjE3_t0A_xe9YtV8kmrbvRuI45RtwEtZ2RRB_VOksNEDiXUqbNJ8opmdKAePdaCWRcXRyrffY7IwyNjCJOyh9W3qphtcwjeBdF_qKwZjLOAB3tsm9bg897wcd-b8ZQTDTYYtGg7WI6y-JzZgGwkifdJZFaKR8zdyRGsLJVI4PCQIM1dF7YtPfRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bcxHaZfmT04M_3zOF0ZSUHbPOtb0vAmj_mP8dPhFc-xXYaP57LrRxqevkzwe7n_DWIGAPd2dn3QR3Pg-Da4pi9BqCfh19IWDgXFTiewwtTd7456AmIrmzbYcVFn1Fdj1quhARowBbzIgLJDWVre_7_yKoJJ3J4ngbucalbbbD0IfDT8BfrfpeSbtLJAWoRI-Rr3i2jd567D7ua6T4ZsA8HQ3vimOGHqmWRlga6vNkBkV1iVJv9F3xUCeYIoHd6tgJbDYO53YKX2seUFyhGAbcAUGxD2CEPHKiDNsu7IDdV9de9vPj4MVut4KdPNphhAk3CCRZPegubplNJbe-Kdo8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگر حواستون به توکن‌های Hermes و ستاپ درستش نباشه، اتفاقای خوبی نمیفته:))
همه‌ی اینا برای یه تسک ساده.
بهش گفتم برو نقدهای منفی راجب Berserk رو بخون و بهم بگو
10 دقیقه طول کشید و کلی توکن سوزوند با gemini-flash . اما در نهایت، نتیجه خلاصه و عالی و دقیق بود(حاوی اسپویل طبیعتا)</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/4108" target="_blank">📅 04:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4107">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">یکی از خفن‌ترین و کم‌هزینه‌ترین مدل‌هایی که می‌تونید ازش استفاده کنید برای ترجمه‌ی بسیار روون از انگلیسی به فارسی، مدل جمنای gemini-3.1-flash-lite هستش. روزانه 500 تا ریکوئست می‌تونید بزنید و 250K توکن هم داره. از aistudio.google.com هم می‌تونید بگیرید که…</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/4107" target="_blank">📅 03:12 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4106">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">یکی از خفن‌ترین و کم‌هزینه‌ترین مدل‌هایی که می‌تونید ازش استفاده کنید برای ترجمه‌ی بسیار روون از انگلیسی به فارسی، مدل جمنای gemini-3.1-flash-lite هستش. روزانه 500 تا ریکوئست می‌تونید بزنید و 250K توکن هم داره. از
aistudio.google.com
هم می‌تونید بگیرید که بسیار راحته و توی ویدئو بهتون یاد میدم. در کنار یه سری api و چیز میز دیگه</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/4106" target="_blank">📅 03:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4105">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">رفقا اگر می‌خواید از نسخه‌ی دسکتاپ Hermes استفاده کنید، به نظرم یه دور Hermes رو با Keep Data حذف کنید و بعد، از اینستالر Desktop استفاده کنید. چون من دو بار روی دوتا سیستم مختلف تست کردم و اگر اول CLI نصب می‌شد، بعدا با Hermes Desktop میخواستم نسخه‌ی دسکتاپ رو بگیرم، به باگ‌های به شدت عجیب غریبی می‌خوردم و یه سری از بخش ها کلا به درستی نصب نشده بود. الان که دانلود کردم از
https://hermes-agent.nousresearch.com/
اینجا، اوکی شد</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/4105" target="_blank">📅 01:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4104">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">کار خفنی که پدرام امروز کرد این بودش که جلوی دی‌ان‌اس لیک رو گرفت کلا توی اپ WhiteDNS
اگر وصل نمیشید به اپ، حتما از Fronting IP استفاده کنید.
من که با سرعت بالا وصلم</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/4104" target="_blank">📅 22:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4103">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🌎
سلام به همراه عزیز WhiteDNS
تغییرات جدیدی روی سرویس WhiteDNS VPN اعمال شده که از همین حالا در دسترس هستند:
✅
تمام کانکشن‌ها با دقت بالا از نظر DNS Leak بررسی و اعتبارسنجی می‌شوند.
✅
قوانین جدید پراکسی اضافه شده تا سایت‌های داخلی ایران به صورت مستقیم باز شوند و دیگر نیازی نباشد برای دسترسی به آن‌ها VPN را قطع کنید.
✅
تبلیغات از بسیاری از وب‌سایت‌ها حذف می‌شوند تا تجربه بهتری داشته باشید.
برای استفاده از این قابلیت‌ها نیازی به آپدیت اپلیکیشن نیست. کافی است یکی از کارهای زیر را انجام دهید:
• یک‌بار دیتای اپ WhiteDNS VPN را پاک کنید.
• یا اپلیکیشن را مجدداً نصب کنید.
• یا حداکثر تا ۳ ساعت صبر کنید تا تنظیمات جدید به صورت خودکار از سرور دریافت شوند.
ممنون از همگی.
🙏
تیم
@WhiteDNS</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/4103" target="_blank">📅 22:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4102">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">این 9router واقعا ۱۰۰-هیچ freellmapi رو میزنه. شاید کلا با همین بهتون آموزش دادم</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/4102" target="_blank">📅 19:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4101">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">یه گزینه هم داره به اسم disable ai
هرچی فیچر ai هست رو غیرفعال می‌کنه توی کل برنامه
اینم برای عزیزان دل مخالف ai
😂</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/MatinSenPaii/4101" target="_blank">📅 16:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4096">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/W3Yhxgj72YRh1RmG0ShB11ryO_D7oZBP7ZwUEk4N6k8Z1eHUYflFphPuGCJ8SvNaqDAtHuuLxg_3tS_i4zK7pIhlPzfezF03kK6PMe9WVk8QfcsR7VhiAmn3-TNcmqC0IVozrVbhCLfUTuispmEIy0aljsOWPl-1n8vqGMHsKS1dB5vCnntCVhptmEalNKH2jAx22Uys7p_1GAiYeszeNAnF7Qac6n3EsoBW5BQSwvtqRPSrUT0CwOA82ZM0O-9s3rWRU5kh8KplJecyB1lPWX9YJfXBjtyxkwHXBSsG6oB0BCPbOJba4kz_3tlN-gnHSKDNK5aWLz9mKmwa9lZznA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CVhrMfYhSAW6tnZ88VKM9TzkWqkRkfYxbI3ein_1Pp4jQNHG3KEm-ujX5oQ4Rfrf6_THzo6jwoiofwduAPEtYHyUdvqZeDAyw7J5tVf0XK7d7lV8J2CucX3bpzmKhu5CaJysExhxzC1BjdV9JjuxY7XM_Gj8lJws5_mkd43t1TtLIWFBPU71hTF0WSzavchjalnWR3Xe2xx36FUbVTIpKEBdnM0T5pxQkXKuS9qr9ZKqBN3MDCvOF8BGJZuj5gT8KKXKbiYIxFVDykSN52PKvSHCUx-Gldhqh_Nz0VkgW5SxCU9u8wfEbzG5YTWBVxhX00t2zZmFt4UKD6UBZ9Lipw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AzhzQGWcXfDuSr9oeq7RxooEY3b44nDf3pCzacftI1yUda1kF6GGfuuxmgIqj-eIEA2Evkq-J7SmuPinI8CCwCLC5YstJZiSuHRjwhbXfX4BKrfc-plm-yAGvUt8TNZT1F2qfU3wTfyqkKQLG_2Okd5qx1m8d35gwo55_4eMfPnex0bdNvlUpMNPASiVSaZ334QyJ0i4NBHYRjCBb1aXNUOkscQlcGPGp7TeUdPXlWhWd-cEG019xoR4cJomj5mp362kPrhI5UoPFdPadxmEIQhua-qVlZX95Wf82HfdMzEvvlYDsbsw_-vwWL73TmV2Vi8hvLHzQ0gbUOBPRoHqrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Z6feD_buw011PjhoSet1knE6_jlVQZ7ktm5bygOvXh1_aI2JUnTOtvPpkTWzkpnbSLuOju5F-WZpvv0VByQeXWBtxXxW1XZEVB9g-c-PENeDHx38_kWAJu_5Kb7_fAFQ4NrVJ8eTDkyhBUmm_QDALy9hn4ovX90Pth1CEOaMNebMaLAEoaJ-VAmnst0anH2G1np1jAM5wZrBFPVqyjZAyA2K_kvzyBmta7ekBmuQnHyB-9uNw4z9H5BwmkNBxXq034rvKsYJuTZ97LPaNzUc1X9ECXl_7S0PqIU8_hSFI0zkefbrqVpdZOQlpWhsHci3Xj_WeUjwsOtPka6xu_62OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Yyt2X4vgUEEEnv9c6iJjWHreUV1mWykSrk9FU3RAMNBS8KO1uPfthLM4oCTwQbMVakzYWBKcIs7aEu9toMtUwFnQsxn17z8aFw-82E7umNulfGdLO_XG-RskaFwrdLNWt3Gz8Rj--7MebqKknlTYswfCwHZaZO8vdce9A1J3dR-UkeAX16JZ8xkOm09XZ504QT6XUtwINw6pumD4D8OBuN8GBhz0kbrCJ4P73kLF_e8DRfMqih_NlaI8_px1Mp5eRQVKvuNBjbqAz8e5wyWcMeYA6diuZ9grytwqmqJOLa7eUGmDFr9qwUGmlXr5BardsAk8szxilD3SSgiRKARUuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگر دانشجو هستید، با ایمیل‌های .ac.ir و .edu می‌تونید اشتراک 120 دلاری سالانه‌ی Zed رو با مدل‌های Calude Sonnet 4.6, GPT 5.5,5.4,5.3, Gemini 3.1 Pro بگیرید به رایگان. 10 دلار هم کردیت از API خودش می‌ده. به شدت هم IDE سبک و خوبیه از اینجا می‌تونید اقدام کنید:…</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/MatinSenPaii/4096" target="_blank">📅 16:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4095">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-poll">
<h4>📊 بچه‌ها آیا نیازه من یه ویدئوی کوچولو بگیرم واسه‌ی طرز استفاده از همه‌ی این ‌apiها؟</h4>
<ul>
<li>✓ آره. بلد نیستم👍</li>
<li>✓ نه نیازی نیست. بلدم👎</li>
<li>✓ رهگذرم. دیدن نتایج👋</li>
</ul>
</div>
<div class="tg-text">برای اینکه در عمل انجام شده قرار بگیرم یه وبسایت بالا آوردم، فعلا هدفم اینه که API های رایگانی که بچه ها میذارنو با اسم خودشون اینجا رفرنس بدم.   خودم اینقدر بوکمارک و هایلایت چک کردم که کچل شدم  در ادامه میخوام چیزایی که یاد میگیرمو همینجا داکیومنت کنم و…</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/4095" target="_blank">📅 15:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4093">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sRR_ncbqthMsJaKWIdq3ZjU9uF4N9_tyy8ju1V03tSZkaY7dyRvl9faq9P-h6jBlFky3aUfAmBOMSUg0OiEd8zS37xPdhseAowUkCPCOYfXfx4cr6n38A7Xuz-Y9tqpkfDYlPA40dwtksONhJGp7Kz4uBgDsXwVxSDn0-u6UkWvBpZET_I78XYqwh2pX2QcL0kz-SEmUYTslofHGnl1qLpvJ93Wo9r-HmWjijJkr2XAp9QBOpmXuAJ3Daeqak5oKKM2aHTyXKs8-nhw2as5fuOx163PXi4CyiXtXrpcu-Nufsg3bx9rnmnivq7dxU67S5kSOXS023l0zQ9xgUzCISw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QIeOZaJxW8jaFkS7EK9_GuGGE0tH3lX6oRILI10wRxtwM6udVPtFGlGwX8FNdxRAZistqQdzGPjkD1dR8VG6GMSIt7iZTfdVkjqnh1gQS1aepjdShXCa-vQdCUIAznMNO8RFctgUsHSoHw8iDVA5Pm1wg5jTHFVsU-ZB2tw5r80MJtIwZcK0nhl74bY_jXSynZr_EnpenvDpBMZtcQjO96IFGxef8dYFh5bKpj_Kdt_yz23X6DVrsw5gYhpalcRvsqR0n-j1SsIXMmzDaGVdXnArcY2jyf1_TS9plLtOnSTgEx94rjcd8zCmCmq_U13WND-owpDSgIck8ERjB5axmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اونوقت واسه بوفه خوابگاه ما تو یه روز 30 نفر کارت به کارت میکردن حسابش مسدود میشد به خاطر تعداد تراکنش</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/4093" target="_blank">📅 15:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4092">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CheYc_PHCSG2h2EwLd5RSmF0uS-OgkqD82A6ocE11WumXP412KBIowCu80gbPb6EkdFyU2b3_uBXwdB7IWUlttgTvVimhmS3ocIVeEUUjtoeONRsa_jmK4WO2_Iglzd8udlbIzC1D3CVCAbmY3pGWmrfH_ROaPqc-y5aVtqQAwDY0Sy5X1itilmNb0OMM5VOx0ILBHbHQSYl_SuALL1rDnPGlj_hhkcYRmPzmyvp85-PtNhBBKilDv0abU6opnhUIrBaxY6JrPr99PWs90exog24kQ-z9FUbWwKA6yGYsBScTrBXDPtjv-MmxdlZjjQtHHCHr4QT58stZR4yzQti5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای اینکه در عمل انجام شده قرار بگیرم یه وبسایت بالا آوردم، فعلا هدفم اینه که API های رایگانی که بچه ها میذارنو با اسم خودشون اینجا رفرنس بدم.
خودم اینقدر بوکمارک و هایلایت چک کردم که کچل شدم
در ادامه میخوام چیزایی که یاد میگیرمو همینجا داکیومنت کنم و یه رفرنس خوبی درست بشه
این لینکش، big pickle هم برام درستش کرد دستش درد نکنه:
https://ez-ai-access.yazdan.me/
✍️
Yazdan Fathali</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/MatinSenPaii/4092" target="_blank">📅 14:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4091">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">به قول یکی از بچه‌ها انقدر api رایگان پیدا کردیم که حالا نمیدونیم باهاش چیکار کنیم
😂
چندتا نکته:
1- اصلا از api های رایگان روی پروژه‌های خصوصی یا حساستون استفاده نکنید
2- هیچ اطلاعات حساسی بهش ندید
3- توی env پروژه‌تون، api key یا... نذارید مخصوصا api پولی کلاد یا gpt یا چیزی
4- حواستون باشه که به جز شرکت‌های معتبر(مثل خود شیائومی که mimo رو رایگان میده یه مدت)، به هیچکدوم از بقیه‌ی سایت‌هایی که api رایگان میدن اعتبار و اعتمادی نیست</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/MatinSenPaii/4091" target="_blank">📅 14:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4090">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/psDMUo708S8OrhyhpR_wbpEjspRt7s6JD9FRAtEcz0hjDrCMOgcSLpGUwqKNrSySahIdkE8IeKk3dmu2pZzuAeD0OuapEKWQscRsve4CGUbTv8iIxBRAbgyq5M4hcDOYkntGep2-ORC9UvytswwDz1MhTuazBw_bF8PsmyG_yekFsLN-Chx2RIkUu-HEHwGpuJnxPRrelBNYzTTeiKwf1D1lBdxTq8htQg8_--cdjATbiO1pt-0yDPn4z6L_jcI2FiGp2L63wMCTJfVfDoETxaU5rxpe3VG-nsMENfVaewbfQd4PVYexG6nh3jm2mLZlZz9ev7hAEs7aKIIPUGmXWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سایت بامزه پیدا کردم تمام اخبار جهان رو با ai رصد میکنه. اوپن سورس هم هستش
خبرای ایران و آمریکا رو هم می‌زنه درجا وقتی موشک میزنن و اینها
این پروژه‌اش:
https://github.com/koala73/worldmonitor
اینم سایتش:
https://worldmonitor.app/</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/MatinSenPaii/4090" target="_blank">📅 13:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4089">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">در مورد بن شدن اخیر اکانت‌های کلاد، باید بگم که من ساعت و همه چیم روی ایرانه(Asia/Tehran) و یه کله هم باهاش فارسی حرف میزنم و حتی از چت‌های قبلیمون که شرایط تحریم و اینها رو براش توضیح دادم، توی تصمیماتش قشنگ لحاظ میکنه "توی ایران بودن"ِ من رو. پس فکر می‌کنم…</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/MatinSenPaii/4089" target="_blank">📅 11:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4088">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d15zALB3td9aZKJaMnFTSybpg5wWNjmeq_adREmpnALPg6lqPCz2yo5byY2PLqhJHi_tnERMBP1UYUTYblUItybckDppe4sPB_Zn0WjYK84-NvxTarWngC-sIhHr3HcWMVRKMmC_ubz1QniVBqP8vmpHM_urEK2XKKO_xigtP5HunDjeCLaAXjIiJvjKGXAHFcKO9klgF9I0l7xE8GjKCudYWrY8rDQlSOZ1MJHIBNZKbsUeY962-92sULR11CIBYyXBzIGGYLsdHawKz8YYvKsmpX9cMw1DfU9VAvniT615bK53AHVpTvIWNiOrHMx5_yUz9-hPBvjV5Kb3FwrYxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مورد بن شدن اخیر اکانت‌های کلاد، باید بگم که من ساعت و همه چیم روی ایرانه(Asia/Tehran) و یه کله هم باهاش فارسی حرف میزنم و حتی از چت‌های قبلیمون که شرایط تحریم و اینها رو براش توضیح دادم، توی تصمیماتش قشنگ لحاظ میکنه "توی ایران بودن"ِ من رو. پس فکر می‌کنم علت بن شدن دسته‌ای اکانت‌ها، چیز دیگه‌ای باشه. نه فارسی حرف زدن یا ایران و... .
به نظرم مشکل یا کارتی که باهاش پرداخت شده هست(که شاید کارت‌هایی که batch payment داشتن رو تشخیص داده و اکانت‌ها رو بن کرده)
یا اینکه علت دیگه‌ای داره. چون خود خارجی‌ها هم باهاش درگیرن توی ساب‌ردیت‌ها</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/MatinSenPaii/4088" target="_blank">📅 10:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4087">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">پیشرفت ai واقعا گاهی اوقات ترسناک به نظر می‌رسه، اما من به شخصه باور دارم که نه جای متخصصینِ واقعی رو قراره بگیره، نه قراره اتفاق بدی برای زندگیمون بیفته(به جز افزایش قیمت رم
🤣
)
در کل، نباید نسبت بهش گارد گرفت. نباید هم نسبت بهش پذیرای 100 درصد بود که "آره ai خداست هرچی بگه درسته"
مخصوصا توی برنامه‌نویسی خیلی خیلی جنگ و دعوا هست و می‌بینم که کسایی که به خودشون میگن وایب کدر و کسایی که به خودشون نمی‌گن وایب کدر، هر روز توی سر و کله‌ی همدیگه می‌زنن. که خب صحبت طولانی‌ایه؛ اما
نه اونی که می‌گه نباید از ai زیاد استفاده بشه اشتباه می‌کنه
نه اونی که می‌گه کلا همه چیز رو باید سپرد دست ai
چون این دوتا دارن راجب دوتا شرایط و چیز کاملا متفاوت صحبت می‌کنن. و این وسط یه سری سؤتفاهم‌های بزرگی پیش اومده و هر دو دسته پیش همدیگه منفور شدن.
به نظرم با گذشت زمان، خودش درست میشه
بازار، خودشو پیش می‌بره و پیدا می‌کنه
و در نهایت، کار هر دو دسته هم مشخص میشه.
الان همگی توی قطار پیشرفت ai هستیم و صدای همدیگه رو نمی‌شنویم:) بهتره صبر کنیم ببینیم کجا می‌ایسته، یا لااقل سرعتش کمی کمتر می‌شه، اون زمان میشه بحث و استدلال کرد دقیق</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/MatinSenPaii/4087" target="_blank">📅 01:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4085">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">یادش به خیر یه زمانی مد شده بود می‌گفتن Prompt Engineering کنید قبل از اینکه با ai حرف بزنید و یه سریا دوره برگزار کردن کلی فروختن</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/MatinSenPaii/4085" target="_blank">📅 00:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4084">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C0V1Wiispr4pZR5_WM4dI0lfuDs6a1HZ1gcF5MpYVfdIGpywJrVYHQ9Is0Q0dWAdQK4yXRRSHbiXyCXQjJZmS5axkvsgKpPHvYIIbHyUAXRAFa7xV20SDM7tzvLiuRFfdkjb_VICW4OkWibDBwgQlyfGlO6-W3AN38WP8xQ8bAYE7Tx5-ZZEdrjYkccIPT_sk0zxBOZwOgeLAuRGJZ-zZYqEte_WMeuHnuxUQLjQ2vgRwMZFdMfac-u6l4PPq6FHkiumuRYYoF0BCutt5WEIn61Wr3I1uEM01dOLorlkuYz9j4TJLTWwqoIEWDt31n-j82nbG-Z_cjvf-D-8NqBI2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید اعتراف کنم وقتایی که حوصله‌ام نمیشه یه ویدئوی یوتوب رو ببینم یا وقت ندارم، میدم
جمنای
واسم خلاصه‌اش کنه
👌
attention span در حال غرق شدن</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/MatinSenPaii/4084" target="_blank">📅 23:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4083">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">الان Zed Code رو به جای Vs Code و Cursor نصب کردم، و اولین چیزی که چشممو گرفت حجم کمش بود. کلا 80 مگابایت بود:) ستاپ اولیه‌ی بسیار تمیز. می‌تونید اکثر ایجنت‌های معروف رو نصب کنید و تنظیمات رو هم از Cursor یا Vs Code ایمپورت کنید. تمام اسکتنشن‌هاشون رو هم می‌تونید…</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/MatinSenPaii/4083" target="_blank">📅 23:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4080">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MlGBivzUolpJOgOnNrjYHJ1V4wx2TTGOM1qJXKpl00bLo_99DigZ5GO5_YI0ujE9ot6a2JbReFemD5jtlWYH6SmPGf00wzKV-UHt1bVeUhJtsxwIuA0ZpRQqXQokk3QPNPDpoJf3FQrLQKVRosC9Meq67qFs4NGX8Y-orkK36K7TXG3jrJjiuSnljCmr0sbd5WmdM_7DcBIrmfa3YmdUuIXZymk7rgoANYFT1sqd2ppP2wSerwmQglLzDWE2ArqUH_bu-6jEKv4ssswy8qEwMdnGsK5d_m1CdOK7Zso24HByxl1ZZapwWDMg74PgZgrX6833g9sPuP289EWlm0-zGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BpcNJfDPmki6HZSo7ZGu33bZGVSDPEM8NwvIb4331WeqpMiAgaGN__z77ZH19qLuKXW7Lq3Tfx6gImBXJLry7PdVeHHjVdX3POL5EfmSp34b1diO11MXu6Z8c-lmr34a9_hxVrHHoFQG6D5M7SjxMam5sc8gq9jYkyB4bZxF-87B0g5ZQP3YDxgMwWOL76sB2ewxkUyRVWdnKJDVBe0LS3qTamvKGxDyO5D6FdtL8Mfo7z09YunGdQEoNa6c8xz18mLjpzNrgTkQgGJPwhorJueWNYGTx_6kmGuVdPhNXztC_KPtM3DTEmPAE8b0spR3oDmBewN6DBjXd7oacexR0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AEMs0ikZ4aZg0JCOzf-cEeZEur3PXYai2AYIz_MV_8FKiwWSBjKQxAv4po0GPJzSrq9yuhR1O7t-6YLJhRPsnJUg3g8NZvskxzT50Dpux-ZQMSlGJnjwzydOGxmbHhThgYDC7sNx5Wo0FDRwhgas1gUkpipvgMPR9xkqmpXutSttE8SE9lbRwB6Jj2yL-isptA6sNwz2g1aoWFoYbZxdF01Q_74n8lwRSoP10BmtcPyyulBw5u6vPcX3H-SJN7n97X3-sNjWaWzMnqRoeLqd9rBYA-zSsEf5qK4VfSSkOdAc2t8zbd9ruUQ3pj-iChnORW8gDTztb5AmmhYMIE6cZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">الان Zed Code رو به جای Vs Code و Cursor نصب کردم، و اولین چیزی که چشممو گرفت حجم کمش بود. کلا 80 مگابایت بود:)
ستاپ اولیه‌ی بسیار تمیز. می‌تونید اکثر ایجنت‌های معروف رو نصب کنید و تنظیمات رو هم از Cursor یا Vs Code ایمپورت کنید. تمام اسکتنشن‌هاشون رو هم می‌تونید نصب کنید طبیعتا
محیط داحلش هم عاری از هر گونه حواس‌پرتی و به شدت سبکه. به سرعت تب Git رو بالا میاره و تا اینجا عالی بوده</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/MatinSenPaii/4080" target="_blank">📅 22:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4079">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">اپل تقریبا ۱۷-۱۸ درصد قیمت محصولاتش رو افزایش داده، اونوقت فروشگاه‌های وطنم نه تنها قیمت رو ۳۵-۴۰ درصد کشیدن بالا، بلکه سفارش در جریان تمام مشتری‌ها رو هم لغو کردن تا مجبور بشن برای قیمت جدید پول بدن. بله ایران درست خواهد شد
✉️</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/MatinSenPaii/4079" target="_blank">📅 21:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4078">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RyO2-Ib0bE8cG5jyZMGrMyB3SwA-fCDfBdPCZwKnd8BFBOIvGqLw_EK4mLLDB8xVoqV_dRS9Z5mPNQcYeQeCWpgj9ggevo-5-qWY5RWkyTUb_nkP99YnUJHhSmDyaxwPU3O2QuOCdSD26uQv5l-ieNIdee8WRwwLBK1s_Rfuq7wezrWrZg3TwZBSvgXpDS1qVukllnndvIncTe_3ZQ9tKWnzEpXrx5T2JntGp0TWVe2WKpbGEKk4cNf7BXGHYRS3I0cz2S84dH0K0dkr6ccKj2iyRRmGJ67TS9vYOeSqlbV39Ca7Vsip0ZRcNULbbdkatfCjafwB3KWbG04eQLaoHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نفر توی ردیت، مدل GLM 5.2 رو روی سیستم خودش راه انداخته با ۴ تا RTX 3090 و 192 گیگ رم
😂
وزن Q2 مدل رو هم ران کرده که توضیح میدم چیه. همینطور با اینکه تقریبا از بیس‌ترینش استفاده کرده، گفته که GLM 5.2 داره کار کدنویسی و پلن و هرچی که نیاز دارم رو عالی انجام میده.
تأکید کرده که مدل توی کد زدن، پروسه‌نویسی و حتی کارهای طولانی و autonomous خیلی قوی عمل می‌کنه. و واقعا حس Frontier Model می‌ده.
حالا Q2 یعنی چی؟
حرف Q مخفف Quantization (کوانتایز) هست. یعنی وزن‌های مدل رو از دقت بالا (معمولاً ۱۶ بیت) به دقت خیلی پایین‌تر کاهش دادن تا:
حجم فایل خیلی کوچک‌تر بشه
حافظه (VRAM/RAM) خیلی کمتر مصرف کنه
سریع‌تر اجرا بشه
Q2 یعنی مدل به ۲ بیت کوانتایز شده.
این پایین‌ترین سطح کوانتایز رایج هست (از Q2 تا Q8 و حتی Q1 وجود داره).
همینطور طبق گفته‌ی خودش برقش هم خورشیدیه و هزینه‌ی برق نمیده
🔋
مشخصات سیستمش هم اینه:
۴ تا RTX 3090 (هر کدوم ۲۴ گیگ) که میشه ۹۶ گیگ VRAM
سی‌پی‌یو هم Ryzen 9 9900X
۱۹۲ گیگ رم DDR5 (Overclock شده روی ۵۶۰۰ مگاهرتز)
مادربرد MSI 840B (هرچند بهش گفتن برای این ستاپ ایدئال نیست، ولی خودش جواب داده که فعلا داره جواب می‌ده
😂
)
ایشالا قسمت ما هم بشه
پست اصلی:
https://www.reddit.com/r/ZaiGLM/s/Ew9JHC2XIA
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/MatinSenPaii/4078" target="_blank">📅 21:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4077">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OroOAicfGIs0sXYhVhZfo4fZ3nRwzvsHr3E1YtkyzuUp_dkWs08e13bMT9hyQm_WikwS5_Hd8kZGhJMesVCeidu3cAV0q03g5y6CGf0j_fHMeLLjjVTou_RQwOUlAJD012AGJP85cH_ZFuRdwcSv6TOkcxOW5ugCLRGyYH4yeMbot8efW9G0XedNPF4x0GO6J_e8Eh8S0dsuELY6vk1AF8G1-zbfmSbRg3Xgh18G4EG-uiY-0f7JOHBxib2_eXtrO42SxzI9m8XuMzA1mVnHt4Z23ICDW2v-kI8YZ1oM86i4fQU7R9zQoH-19ePgH4BD4xwqP4Bnnr-oLIzSDyxMHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر دانشجو هستید، با ایمیل‌های .ac.ir و .edu می‌تونید اشتراک 120 دلاری سالانه‌ی Zed رو با مدل‌های Calude Sonnet 4.6, GPT 5.5,5.4,5.3, Gemini 3.1 Pro بگیرید به رایگان. 10 دلار هم کردیت از API خودش می‌ده. به شدت هم IDE سبک و خوبیه از اینجا می‌تونید اقدام کنید:…</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/MatinSenPaii/4077" target="_blank">📅 18:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4076">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M58HMCnob4F4W1RF4R6Jh5PXBdwa0umbP2cAMq7JpdNe_CvY1tNxnvej5PazwRtZbmt83n3M8VmFlKyawexDMEJ-lujau0uYM0iHxd1fet1AMANLxt8NQ6gAmknqAjXZcTLXsT0Kkgy0y1hmLbvie8ZRCgcARuA9uUGeIfw5TjJn2MoaxYoFvIWFx7ZbPa8CBKT98DV0_tcJCkzooM5s6XjpAVpwK8cIYkQbRxqBhzmruWjhIqKisqLcUeKo5gW2m5gtPRCwsNtckhn4zR8ppqKSw7jlKnRM6sWD4z4vcRTkrs_lGJzA7LibM75fZBdhTeyqQHBblAQu871rpcFYRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر دانشجو هستید، با ایمیل‌های .ac.ir و .edu می‌تونید اشتراک 120 دلاری سالانه‌ی Zed رو با مدل‌های Calude Sonnet 4.6, GPT 5.5,5.4,5.3, Gemini 3.1 Pro بگیرید به رایگان. 10 دلار هم کردیت از API خودش می‌ده.
به شدت هم IDE سبک و خوبیه
از اینجا می‌تونید اقدام کنید:
https://zed.dev/education</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/MatinSenPaii/4076" target="_blank">📅 18:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4075">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/38b0a3b6de.webm?token=e3wz54x0Kd5JfM59SXACcQFOkhYy1fph2IBh2dOJrGG_FXsD-CfSo01YfxqWGbPLBH_DivfGwo3CsFlJiFPnmC2R03xy26ZAHq6yxuU22USJFf_dELMwCddW66V2VJ3qGadpArtc5DHVYeRefYOUrRmNiaazY22CdBmc6XRWRW9zrbiw1EuRdfmCGFllAer6TNq6N4ioXdWNBRhf_4cm_Y_xB6kmeeQ97f9lp6JSfa89vY2qtvcKDoA22is_Dpun4btcEPG1JiAbc6DPGjwH9jLVRibkzUfp000KcAxMvwIZgTZdYdNgYMx5pYxCSxmTjVlGx9Qat0BIYMNR1bL2Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/38b0a3b6de.webm?token=e3wz54x0Kd5JfM59SXACcQFOkhYy1fph2IBh2dOJrGG_FXsD-CfSo01YfxqWGbPLBH_DivfGwo3CsFlJiFPnmC2R03xy26ZAHq6yxuU22USJFf_dELMwCddW66V2VJ3qGadpArtc5DHVYeRefYOUrRmNiaazY22CdBmc6XRWRW9zrbiw1EuRdfmCGFllAer6TNq6N4ioXdWNBRhf_4cm_Y_xB6kmeeQ97f9lp6JSfa89vY2qtvcKDoA22is_Dpun4btcEPG1JiAbc6DPGjwH9jLVRibkzUfp000KcAxMvwIZgTZdYdNgYMx5pYxCSxmTjVlGx9Qat0BIYMNR1bL2Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/MatinSenPaii/4075" target="_blank">📅 16:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4074">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">دو ساعت برق رفت، گند خورد وسط کارام و تمرکزم و همه‌چی</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/MatinSenPaii/4074" target="_blank">📅 16:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4073">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">از سایت Nara Router که ریک معرفی کرد دارم استفاده می‌کنم برای ‌Hermes و چیز خیلی خوبیه! یه ربات خیلی کوچولو هم دارم می‌نویسم. دارم تمرکز می‌کنم روی این قضیه ببینم چطوری می‌تونم کارهای روزمره رو Automate کنم و چطوری میشه حداکثر بهره‌وری رو داشت از Hermes  خوبی…</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/MatinSenPaii/4073" target="_blank">📅 16:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4072">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SwPmWZX2BdsbULnTAPrUwYOv50oF4NqMGBuvucm-CHD5wPEeYBOrd52o0e_hijgKC3TI4cqA3DrOyKoLOiqa_xzK-EtLXupR3n0mzYbsH7I_SrNWhY0xEB0taqqRy8p-KynYYzVFxkhnH6mCxQ38mjF4oBWn2UKzhly15ChULiCFuwEXRfSx3TtPtUBdBgkidXFpc7jRxJhUHJrqaWDpeKg1JHApwmas0YXY54sYfBmg4kRyTvGlQkPIq-C-x50qqkUS0rZQHx7lfX6bACgaOQRD3OrNzxItgQFsgL2BgyR3Z3A_rR2pSTPraJ4BOGPeV58Z5s9AyAlf1PGIdrDLdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرمس دیگه منتظرت نمی‌مونه — خودش یاد می‌گیره!
📱
قابلیت جدیدی که Hermes Agent اخیرا اضافه کرده، دستور  /learn  هست. به‌جای اینکه بشینید دستی یه SKILL.md بنویسید، یا خودش صرفا کورکورانه بنویسه و شما ندونید چه خبره، حالا می‌تونید فقط منابع رو نشونش بدید و خودش…</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/MatinSenPaii/4072" target="_blank">📅 13:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4071">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q1CAT56TNf45Rko65VypGtwLrVDDAj9HQVD3KmjqUdWtiu_a08-yma1Xq-uAgnVL7rIyoxxC7R5sfO16HcfvYCDfYW3YWm9auPrUWfDqODaGRpe6_LeM8RRFYmiY3AlnEALaP9R3U7M8l1CHYPTkO7dQw1_a5NIC1DGI50E-nlLQBsamkLWfXAx_yYbtYCdcCt9akQ-k7SCtG9O-KXJOsi9yQRZTf0SaXEDW3V0iaq4iV2Jhq2jYLmZsP5AcKs42YsUEsGoYcod1CuQLmLnfBLy6hBubcZsipiGMDkj2O_-fgWQ8oLMJAStw-Gn-wF86A4WF4WpFhAUX2P0JqJmlmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرمس دیگه منتظرت نمی‌مونه — خودش یاد می‌گیره!
📱
قابلیت جدیدی که Hermes Agent اخیرا اضافه کرده، دستور
/learn
هست.
به‌جای اینکه بشینید دستی یه
SKILL.md
بنویسید، یا خودش صرفا کورکورانه بنویسه و شما ندونید چه خبره، حالا می‌تونید فقط منابع رو نشونش بدید و خودش بقیه‌ش رو انجام بده.
🗃️
وقتی دستور /learn رو می‌زنید، ایجنت با ابزارهای خودش (read_file، search_files، web_extract) منبع رو می‌خونه، یه skill استاندارد می‌سازه و ذخیره می‌کنه — و روی همه‌جا یکسان کار می‌کنه.
چند تا مثال که بهتر متوجه بشید:
۱- /learn the auth flow in ~/projects/backend
کل منطق احراز هویت پروژه‌تون رو یاد می‌گیره؛ دفعه‌ی بعد برای پروژه‌ی بعدی، فقط صداش می‌زنید.
📞
۲- /learn
https://docs.someapi.com
مستندات یه API رو می‌بلعه و تبدیلش می‌کنه به یه مهارتِ آماده. مثلا من خودم سر API تلگرام و اینکه هی آپدیت میده و ai ها رسما نادون میشن سرش، این قضیه خیلی به دردم خورد
💻
۳- /learn my writing style at
https://example.blog.com
استایل نوشتن خودتون رو بهش یاد می‌دید که من روی این می‌خوام یه کم مانور بدم و قشنگ تستش کنم و نتیجه رو بهتون می‌گم:)
📚
🌍
نکته‌های باحالش:
• مهارت‌ها توی ~/.hermes/skills/ ذخیره و persistent می‌شن
• بارگذاری سه‌سطحیه؛ محتوای کامل skill فقط وقتی نیاز باشه لود می‌شه — توکن الکی نمی‌سوزه
• و اما مهم‌ترینش از نظر من: نمی‌خوای کورکورانه بنویسه؟ با write_approval: true توی تنظیماتش، هر skill رو قبل از ذخیره خودت تأیید کن! کنترل کامل=)
🛡
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/MatinSenPaii/4071" target="_blank">📅 12:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4070">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">از اینجا ببینید آموزش WhiteDNS VPN رو به همراه آموزش اسکنر اندروید من که پدی زحمتش رو کشید:
https://t.me/MatinSenPaii/3999</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/4070" target="_blank">📅 10:32 · 06 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
