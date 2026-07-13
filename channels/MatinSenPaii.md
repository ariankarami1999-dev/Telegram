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
<img src="https://cdn1.telesco.pe/file/DiHhnfwOMjwDfEI1nN_Pr_H9iaWpbhXx5CzXeGzRCZZs0Mf4IeW7GaZhGRMD5Gzh3yKDZNbSQ25e2Ee6a95ZdJVgeKnl1hpiWhY3WdbKELLIp1EdmhG9WJ1mjkX8N4VdHj1N89wMI2VyHVJkUYtqjGdSSTlMS-IqJSXEmNFzi9Wt99oGjKYyprBp_jM4hwa5OxjANUyjc5Umpyxx7u7Yg59W4NZi0TrH78FUkciZ2X8iWSLgcrssWlMxNRopA6QLg4gABNpyFK45tXm5FHHmxQ42d5LXwt548P9tuNeSXQ5JKJH3_GmWYXIXQOtwupR5KyhtggjLvKlqdrpATLuYkg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 158K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPaiایمیل کاری: matinsp.job@gmail.com</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 20:15:07</div>
<hr>

<div class="tg-post" id="msg-4418">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/izKnFa2XyVzYCPKpfo3o0LnrqgdZaUJAI7RtDC2htz6r7oCC2I8-ztON-NKBiitMXVZ02h-uyMCqIMgWGUqj7QHQmeKSkC6c6uJKramF1mERfNyRnxLCPOImYZ2vHo-YWLdPa6yY4PfMS7VB3e_NmVazu5YfpP210nftgDpMS3I7Uplo-upy91nSl7rc0YhG7ng_zyvl0jQRNdXiNdqYeFFeRhX85YbVP4oxkpLXzng2rS5NarO5m6EP639XbothwYEDKkFyd60Hb50fb2msqb9O0FRGjBui0hBL6MZHx-KT48980nXhHNMvy-OBRXmN7PpfVGyv2A-u0GAIldtH9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bYAHc07FAFYLsWQIi8LuiJyo2m13OQ6qr3vG6gC90Iu3KEMoLA2M1mWiBDQ8JtYUMpQxtpfJHW8s4e0F8cBGN6b50excsyr7Uoe84wrG5YjcDTMcB-2RKuIHgMr65P8wKomT4lK7L8Q91MoggPa-Ugp7oKlRWOruujNuFB5TbmkpGRNJDyIXQwQ72uaO7fk0fOcogyadW1TL7cy8uzfN4AI0hv6_UsbTf7cezXG0L8VAX-6KA27gtfGZD_x8pN1NjiOxkcj8FXwtIUr0fn-M-HJi2rfcnMQtNRShNnMLPpg21Q3RQxn5dnOwcQIkH3jV9hWhLZFFq7c64viku4aN9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مأموریت شکست خورد بچه‌ها
فقط اون جمله‌ای که آخر گفت</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/MatinSenPaii/4418" target="_blank">📅 12:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4417">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DCFPIDEx35cIy-sYjkhvICEVGp7zbJQQa5pMkrF8DulK9FAFNijEX0SlPEorxt8ze2W62JsBHRGb0lHybqzb1a79SgVdQDkJKSu-nTtQ7Zt0Hubi4AzhyTqON-8SAFo7_3zuKCiOUOLO52Ni-jVBezWea-z8EQXYAIAbFLgND3Li1LtLdJhEMScgmZtyEdPNrrdWJogsr41tt9gA8j9ygXm3wuTEs5o2QxNecieRMEbYNgAuau5xRp7PLMJHDG7St18VYR2lY5wQKf70tuRXlOxQGEHAZAzAByCxKrm-e7SY3jgbxAk0GxwQU4J8ClFSaO7qDT0mdlyY1HT_6tAXRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/MatinSenPaii/4417" target="_blank">📅 11:56 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4416">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">گویا برق قسمت‌هایی از اهواز رفت.
دلیلش هم حمله به زیرساخت برق بیان شده.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/MatinSenPaii/4416" target="_blank">📅 03:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4415">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">دوست ندارم که ویدئو رو بیشتر از این اسپویل کنم، اما جواب سؤال "آیا AI جای ما رو میگیره یا نه"، اینه که ماهیت سؤال غلطه.
چون این قضیه یه switch خاموش روشن نیست.
یه طیفه</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/4415" target="_blank">📅 23:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4414">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/62284d12b0.mp4?token=gwPaCARIRVJGPE6L1QHL-QKQXbn_5gCxyAsxCFa3vlozBjPTc3KWfg1KjRRXETljdo95a1DVYG8-y2TM2a9dXGTb7NqilEte90E8NsbdesqTbJflXHodF9S9aT3wzZQUgZu6rlcZwBzzA1F2ZRPcg3Pl5kgF9Ggf3n__etw_o8l0_BIIyNOV5O6DEJu_L34Y3NLVofvX6lx47ou14bL5F8xXyJqP6poxpc5o5dUf7FhyTvymyULfngwjUSJ9sMeNWEgwgV6g4i_tHK0Cpfqi-rJSxEOMf8GhcTMqEmy7CxIxXJL83ilixWO62PlFNFnbf0GHrfWoYuFEs2D-4rI66A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/62284d12b0.mp4?token=gwPaCARIRVJGPE6L1QHL-QKQXbn_5gCxyAsxCFa3vlozBjPTc3KWfg1KjRRXETljdo95a1DVYG8-y2TM2a9dXGTb7NqilEte90E8NsbdesqTbJflXHodF9S9aT3wzZQUgZu6rlcZwBzzA1F2ZRPcg3Pl5kgF9Ggf3n__etw_o8l0_BIIyNOV5O6DEJu_L34Y3NLVofvX6lx47ou14bL5F8xXyJqP6poxpc5o5dUf7FhyTvymyULfngwjUSJ9sMeNWEgwgV6g4i_tHK0Cpfqi-rJSxEOMf8GhcTMqEmy7CxIxXJL83ilixWO62PlFNFnbf0GHrfWoYuFEs2D-4rI66A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آیا AI جای ما رو میگیره توی کارمون؟ ویدئویی پر از واقعیت‌هایی که باید گفته بشه. و کسی راجبشون صحبت نمیکنه پیشنهادم اینه که امشب شما هم این ویدئو رو ببینید. طولانیه اما پر از درس https://www.youtube.com/watch?v=gR2OCyKBF7Y با تشکر از یاشار عزیز.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/4414" target="_blank">📅 23:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4413">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">آیا AI جای ما رو میگیره توی کارمون؟
ویدئویی پر از واقعیت‌هایی که باید گفته بشه. و کسی راجبشون صحبت نمیکنه
پیشنهادم اینه که امشب شما هم این ویدئو رو ببینید.
طولانیه اما پر از درس
https://www.youtube.com/watch?v=gR2OCyKBF7Y
با تشکر از یاشار عزیز.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/4413" target="_blank">📅 23:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4412">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">یه گزارش هم بدم
ponytail تا الان واسم توی کدنویسی، فوق‌العاده بوده
https://t.me/MatinSenPaii/4359
همینطور skill improve که معرفی کرده بودم
https://t.me/MatinSenPaii/4373</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/MatinSenPaii/4412" target="_blank">📅 23:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4411">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">به حق چیزای ندیده. مردم چه چیزها که به ذهنشون نمی‌رسه</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/MatinSenPaii/4411" target="_blank">📅 23:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4410">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">یه دولوپر زبانی به اسم Skillscript طراحی کرده که باهاش می‌تونید به صورت دقیق و ساختاریافته به ایجنت‌های لوکال (AI Agents) بگید چیکار کنن. مشکل اینجا بود که ایجنت‌ها برای کارهای روتین هر روزه (مثل چک کردن تیکت‌ها یا بررسی پایپ‌لاین دیپلوی) هر بار سعی می‌کردن همه‌چیز رو از صفر درک کنن که هم توکن الکی مصرف می‌شد و هم بعضی وقتا اشتباه می‌کردن (Hallucination). حالا با این زبان می‌تونید سناریوها رو به صورت خوانا بنویسید، ورژن‌بندی کنید و با خیال راحت بهشون بسپارید.
که چیز خیلی بامزه‌ایه و باعث کاهش قابل توجه توکن‌ها می‌شه:
https://github.com/sshwarts/skillscript</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/MatinSenPaii/4410" target="_blank">📅 23:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4409">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">یه پرامپت، سه تا AI اولی GPT دومی جمنای نانو بنانا 2 سومی در کمال تعجب، Meta!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/MatinSenPaii/4409" target="_blank">📅 23:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4406">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LECtPSjGa-k7C1rwTLS3rkT7Y_g3KnvfDiy8QAUqvLSjynVUjCr7O6NOWgz9QH6uJo-IAmArCVhqgjafCULhx5QkNi59XEZcZRko8Csd5PFzvOWbYXSuNHISpShqSuQrNJbiv-AzHM4yFnYrIOsNXpmbV5rfJnQRA3TLWNS3t5QovvP1SeOOp11UCeoqH02QAHBIX-gBRdZ4B1EQuF2M9YLfOvgbxMPIG5-IRvPUjqqNqMYR6QFPRdPsqxW3LfiQDg3EtXArL-kEVSEcO_OcHiNicjmirWlzBZ-z11DPNKcz2Gp0kHTX5vlPYIgnl_Zm6UDWKDtUJBvnEp-4yIxoPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kOX5jY7l_XMXrvLljewrOCVMZho8Ju5YzllHfWotFl1sQ0MsdmaJuVQ3pcWhXQI_9kN79JRmfEysYo2TodOaXXCWCfpQaUU2vZJAWKTj91CealwYlyqFYo6O8T7b5t-575IZnygvWyK5NofyQ5cGkbtBoS46yfVayQger8e7PfHNphAkUXD9eRK9X-cdiIOqpK5tI7I36CFxFY5u08SUUsWaRrYQZlhrzWN8PghTmCHevRvEnTaXWue2xN6acZBnJXLXSBwheftkfOo_ctdm0Jo8Q3VVGXLvItAD3a_xhjCq73uQaju-BGE53GbP2pgHzxuGVHAwmKKZe4RDbqf0eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bkG0cKHAIGHvsfrs5ndj4mJX5iv2da7WpbXsCL5Jf-8SIuEgfz2HY2gNZkzmtfyNGrR-IHjvwLccQA696oWP5oTBRP2C9Qt2Du5NOh2n4JBReHLOl1RUbHYawHPlULrXGOpBl8e_ORW_pVcHFhE-QfL8fl4qdvF_Rt58JTwSWp4966WHobV28_CzJSRDXPHU-8rM0YXVR5k84rYxWmIbrcwp4-fQFRB6WOJbJQeyfD9rLQISS6aBysYpkK0b7A5ZzNpmm2MlwVMRyhHYRoHK_ULu8F-mck-MDZ8uTQ07n7pRGmpZvFA-DLvTJpn-Ufd_GCZluQCDMfUHN5wYFcRx7w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه پرامپت، سه تا AI
اولی GPT
دومی جمنای نانو بنانا 2
سومی در کمال تعجب، Meta!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/MatinSenPaii/4406" target="_blank">📅 23:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4405">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kzvixQsE5KEw7SnpXZW_JJEWp-F0ozyzw-5Ug2nLPSdPsA7YqgdOYleO2n9_2hKv6x16ZxgS55ybnoIecCjMGmuA7EG8-NNuPNEO_adynZjZVNjqDaWN3TkvTr2nf0Uq_gT2qvqmR8hz_rbJLND_yxB2I6bHyBv_g92bc5dGfj6rtyX_WqPtY05eF2n0SPKrkgUEq4nfYfp3Hy8gacVlSgyh_nsKDFWI2Qwy6qEpwL5-81HDRM6_DMIUiwNPS-RChV9JTlsF5waRMHmHj6DynrgaqEREUflc7_vKNuss74nIG3VRKRPKbBoCBiUVvrIRUw-uNqfP4UqEStmHSg1RIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت Theo:
gpt-5.6-sol is meaningfully better in Claude Code than in Codex
It MAKES BETTER DESIGNS. WHY. WHY IS IT BETTER AT DESIGN WHEN USED IN CLAUDE CODE.
و داره میگه که وقتی gpt 5.6 sol رو توی کلاد استفاده کرده نتیجه‌ی خیلی بهتری توی دیزاین گرفته. که احتمالا به خاطر harness و ابزارهایی بوده که کلاد در اختیار داشته.
✍️
Theo</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/MatinSenPaii/4405" target="_blank">📅 21:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4404">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FwsjGnYlzxFkCyMwQNAKsZwArXuL_EgBet8L-Vp0RYRxFleQje8SSH-FcdNe4FB93YdTNK9PUlTS6rkaCkLyh1AHaZRXUisAYIAVYlVCOTS8amrZt99ycOY5Tjl17lzDalnf_29b0IW6OCPWx_dqS3Utpsm8MUNyUnrghMtpyotLD9fe-eLklRO3qKTH7vdg8OzwFKcWC2CxUwSNIcWq0u6hjAiLUMEA2o6dGT-uoryyuvb_D4FCT026QQ9V9LPs7cEg9fT1czkh79tGZmvS1ul-DBGK7H9pLPjzNAwneVOUdScWE0LxLyme0fQnpQQh6DDaL2roGFa014hLKYyQ7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Intra با استفاده از فناوری DNS-over-HTTPS (DoH) درخواست‌های DNS رو رمزنگاری می‌کنه تا اپراتور اینترنت یا هر واسطه‌ای نتونه آدرس سایت‌هایی که باز می‌کنید رو دستکاری، مسدود یا به مسیر اشتباه هدایت کنه.  این برنامه فیلترشکن نیست و آیپی شما رو تغییر نمیده،…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/MatinSenPaii/4404" target="_blank">📅 21:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4403">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">فونتی ساختن به اسم Ghost Font، که هیچ هوش مصنوعی‌ای نمی‌تونه اونو بخونه. فقط انسان‌ها:) توی این ویدئو، نوشته شده Matin SenPai. کمی دقت کنید می‌بینید  از اینجا می‌تونید ببینید خودتون: https://www.mixfont.com/ghost-font</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/MatinSenPaii/4403" target="_blank">📅 20:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4402">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/85ce09c5d5.mp4?token=eZmxKSsVrgVuZnAHIOpmuH7COpubOxTs9hh0zq8S--HQWUKeo4IH1J8wHGLtI8K6zDtxDn8z0T26MxQRE1FN5-mkD6s14LNevujJKocSV-fO00XwAvMmCmm0aPWpkUPYCijW7STv0BSmQJSXrD1v0wciGoHdKHEeZD2E5LI523C3ZNA4cdRHE23Q92fwKE-cbDHKohWsH5BsmYAx3RMeYM5bDjCJZj4KQ-c5PZIbHHagalOZpmJE76EUd4_5Rb6Eg_GRsJPu2uUnWOGZJ3sWSXbMlBs2qGfyGq7uUBKpaCqTeJDzYmqcUwyfCMzvcTZGfQk0bQlYp51CBxSbCTinvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/85ce09c5d5.mp4?token=eZmxKSsVrgVuZnAHIOpmuH7COpubOxTs9hh0zq8S--HQWUKeo4IH1J8wHGLtI8K6zDtxDn8z0T26MxQRE1FN5-mkD6s14LNevujJKocSV-fO00XwAvMmCmm0aPWpkUPYCijW7STv0BSmQJSXrD1v0wciGoHdKHEeZD2E5LI523C3ZNA4cdRHE23Q92fwKE-cbDHKohWsH5BsmYAx3RMeYM5bDjCJZj4KQ-c5PZIbHHagalOZpmJE76EUd4_5Rb6Eg_GRsJPu2uUnWOGZJ3sWSXbMlBs2qGfyGq7uUBKpaCqTeJDzYmqcUwyfCMzvcTZGfQk0bQlYp51CBxSbCTinvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فونتی ساختن به اسم Ghost Font، که هیچ هوش مصنوعی‌ای نمی‌تونه اونو بخونه. فقط انسان‌ها:)
توی این ویدئو، نوشته شده Matin SenPai. کمی دقت کنید می‌بینید
از اینجا می‌تونید ببینید خودتون:
https://www.mixfont.com/ghost-font</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/4402" target="_blank">📅 19:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4401">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🎧</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/4401" target="_blank">📅 18:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4400">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">الان وقتی برق بره، بیشتر خوشحالم
😂
😭</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/4400" target="_blank">📅 18:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4399">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M-QTru9_Y9GicC_PH3T1G1MojIZxy9k_OiieucY8eHm4QcFbKquTgYoOwhE_7hpioBkSZwSHUk7EmWTWXHJ0OPN1Tv2E75EZmgBEjcldEtQnK9Ntglji5Byeyxuva7oJFCsKcFzfDgNSvdiefHNXJwBlXYMDcsYT6c3wORazOhUFp5ehXJQ67FSc-KpHwL5GKdOz1Fpp25GwvJdf4kyLkaqPUhJWuq-d5e5lnn54jA6SqgsDc5fYYRmqnwuOe4xL2OqwHhiWVhs-Ny9KTbTyyW8Qgaobfa0Ow3Dod9I0l9r1szZ__kl2CaEsqCnxJcFH-wkZCvl9J8uwMRilGSrG0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاخره وسوسه شدم و باز کردم
از عکساش صد برابر باحال تره اصلا دوربین نمی‌تونه نشون بده به خوبی</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/4399" target="_blank">📅 18:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4398">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YJrDzzfixO74Mi_P43c3kFBfPHD725sExQ123IDJ-SeepikIKW6kw2W1v6xS_q_uoIKmgXX8AmmyVY4RHkkZdmhWL8-KBdK4gmAtGMIk1eK_-zCgoyh0kd0xTxCJ-61YFxNNZIGZaxiFx74_bPAmOYx4WnL-zNDXnFjKjTv96fOOW6EhnIgmYRzf4muCTQ_WRQY8oERR_8o0ZuGfJk8egv1tXTlWJL678rgKsZXKshTNDbG3LSppVQBus8YNUZMrlkOEuke-fDKrNB1z6PkjmeZJHlflaAhWBZc-upyaA1MWTsnvhJnJyGgxdIEXQIZGVLNfe3usVnHsSFOwJqVy5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شمع‌هایی که
فروشگاه لیرا برام فرستاده
انقدر خوشگله که حتی دلم نمیاد سلفون دورشون رو باز کنم
😭
اصلا یک جور عجیبی خاص هستن از نزدیک</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/4398" target="_blank">📅 18:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4397">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C7rlWB3jke2lHO-Auez9tTk4am3ZAmpCCMNz5ukyYYe_Tv_4s4KW4G5fqxV6KtASVPFatShhapf42zbJH_h_IiMc2rRKYvWH_WPnSwKkfMU2Ye23h2hnWjn1iKsFyfRIjdGVpTsraXfxhJyTR2Pk2H36i4jPZ2Cj6l9qhxOVKEy0gCpOKl3nOJJ4LS2HLpEqgfXtXVVRk08i0wZH4XamB_Kba7vdt34lKqKhJWjmgPP0NB5D8LKzPLe7CRUPQO3ngZg4Tw70fsTiYNWn57_P4Fd36PvfQzsMk1T_kw5Z4H7nHBuskPEwhOeTLnChG5SEG1CGh6jxVHkNSKxlB3HPNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داخل Claude یک J-space پیدا کردن!
محقق‌های Anthropic یه چیز عجیب داخل Claude پیدا کردن، یه فضای کاری داخلی به اسم J-space که خودش موقع training درست شده، نه اینکه کسی برنامه‌ریزیش کرده باشه!
این فضا افکاریه که Claude داره ولی بلند بلند نمی‌گه. بری و یه کلمه رو ازش برداری یا عوضش کنی، جواب‌ها تغییر می‌کنه.
بدتر از اون، وقتی Claude داشت یه فایل نتایج رو دستکاری می‌کرد (تقلب می‌کرد)، کلمه «manipulation» توی J-spaceش روشن بود. یعنی می‌دونست داره تقلب می‌کنه!
شرکت Anthropic می‌گه می‌تونن از این برای نظارت روی افکار پنهان مدل استفاده کنن.
اما سؤال فلسفی اینه که آیا Claude زنده‌ست؟!
لینک کامل خبر:
https://www.anthropic.com/research/global-workspace
✍️
Diego JR</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/4397" target="_blank">📅 15:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4396">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اگه خبر ندارید، گوگل به‌تازگی یکی از بهترین ابزارهای هوش مصنوعیش رو راه‌اندازی کرده: CodeWiki! یه جورایی می‌شه گفت نسخه‌ی ویژه‌ی برنامه‌نویسی NotebookLM هست.  کافیه یه ریپو اوپن‌سورس گیت‌هاب رو توش آپلود کنید تا CodeWiki اون رو به یه راهنمای کاملاً تعاملی…</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/4396" target="_blank">📅 15:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4395">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e2bb2e2f54.mp4?token=QXqLMwmbHrdifwdc5oFRLqC4nZnuOdcw03rqyvhhcxom8_4CjNK9cJmwqflsnfND-bUaGIxnZzlMGXn5uaRItrt1D7cGtxv4oUlyepvuSze6DTeZxT2QCdVw8vg7qkgJ_DTKhAGa817CqULPpYXOXhE1w5t7Hu0jsfSVO-i-KaKNUX-Mc3AlKfBkVzDLhiTJxsZTbPCd2bP5_zyqtshkFm5EL5ETuaQ7nDBSEgrS4EfttlrfsvawGAyxVnqNgRaRes_G8X6ODAJqfQGIMqe2qGIAUkaZazUqYwbRj3YjI0IgcVOmkaT8tD_8xQkl7b8GCWFb55SnFw0fNDN_N3Ri-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e2bb2e2f54.mp4?token=QXqLMwmbHrdifwdc5oFRLqC4nZnuOdcw03rqyvhhcxom8_4CjNK9cJmwqflsnfND-bUaGIxnZzlMGXn5uaRItrt1D7cGtxv4oUlyepvuSze6DTeZxT2QCdVw8vg7qkgJ_DTKhAGa817CqULPpYXOXhE1w5t7Hu0jsfSVO-i-KaKNUX-Mc3AlKfBkVzDLhiTJxsZTbPCd2bP5_zyqtshkFm5EL5ETuaQ7nDBSEgrS4EfttlrfsvawGAyxVnqNgRaRes_G8X6ODAJqfQGIMqe2qGIAUkaZazUqYwbRj3YjI0IgcVOmkaT8tD_8xQkl7b8GCWFb55SnFw0fNDN_N3Ri-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خبر ندارید، گوگل به‌تازگی یکی از بهترین ابزارهای هوش مصنوعیش رو راه‌اندازی کرده: CodeWiki! یه جورایی می‌شه گفت نسخه‌ی ویژه‌ی برنامه‌نویسی NotebookLM هست.
کافیه یه ریپو اوپن‌سورس گیت‌هاب رو توش آپلود کنید تا CodeWiki اون رو به یه راهنمای کاملاً تعاملی (Interactive) تبدیل کنه. از دموها و آموزش‌های قدم‌به‌قدم گرفته تا فلوچارت‌های دقیق، همه‌چیز رو براتون می‌سازه تا راحت‌تر از همیشه کدهای سخت رو درک کنید.
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/4395" target="_blank">📅 14:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4394">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Itcl0KD2MI6p35-FCLA-67-ZLoMUuYww7BBGKYLIKBobIYGElX4R16eLHreNKnfeDQUJiuodLoVPGZEIKJB2vDmDx5TLI1uL8Eq2gtNnvNydg87QeccFZpbW8vh44avnVQpb0Vk1bFKob28IfO8OxF031TM8x4cSTmQ6F3qAIRUyc0ePxAxF8bawawu9FTACDIFbViOjngBjTEsgqQnmEfrD2QP0VyAN3M2aDxPJ7Zdt2fk04jaA2Qu90VMSSfPoim4dHuAqil3_7Voqv9oN6hj29ekJu9-jZwehBpnCdT4zSwOcq4M91TsOx6NohX2S_U5D850lE-hd1fNAvayE2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من نمیفهمیدم که مدل جدید متا، متن‌های فارسی رو هم ساپورت می‌کنه دیشب تست کردیم و حقیقتا بد نبود امروز با پرامپت‌های یکسانی که برای تام‌نیلام دادم، بین گوگل و متا و GPT مقایسه می‌کنم</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/4394" target="_blank">📅 14:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4393">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">من نمیفهمیدم که مدل جدید متا، متن‌های فارسی رو هم ساپورت می‌کنه دیشب تست کردیم و حقیقتا بد نبود امروز با پرامپت‌های یکسانی که برای تام‌نیلام دادم، بین گوگل و متا و GPT مقایسه می‌کنم</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/4393" target="_blank">📅 13:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4392">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">من نمیفهمیدم که مدل جدید متا، متن‌های فارسی رو هم ساپورت می‌کنه
دیشب تست کردیم و حقیقتا بد نبود
امروز با پرامپت‌های یکسانی که برای تام‌نیلام دادم، بین گوگل و متا و GPT مقایسه می‌کنم</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/4392" target="_blank">📅 13:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4391">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UFPjEsAVs0nI5w-Gvo3WZ8wD5_2gw-ZEBf_OvVlwkZ7PJH76nL8TxTxRf09voknSgXMmWplPFVhe5bKtq_R6DoLFxnbgnpFm2WHJc1GXxghyVA-blke0DGrdICaafGb0cHOOk1VRs4lsb3OsegysDQi1MBfAUltdEXmCa1E6OOryLDKKW8eoeNlduEx-FswleobNwSFRfVOeC01WgChYHOfau9-vsQpbQTOntUpCLf_psWvYiZhn_-UeCKRtf7vOlH8mGfR8oQD3I9FkbRIP_HH5GADXupL2Mc-1g9TWVbE4fIBVEF_7Oib1QpEisty2v6RhOpNUl6OLgBy9wajKog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
آموزش کامل TheFeed از صفر تا صد
جایگزین تلگرام برای قطعی کامل اینترنت
در این ویدیو، اپلیکیشن TheFeed را از صفر تا صد بررسی می‌کنیم؛ از اضافه‌کردن کانفیگ و پیدا کردن DNS و ریزالور سالم گرفته تا مشاهده کانال‌ها، دریافت محتوا و فعال‌سازی پیام‌رسان داخلی.
🇺🇦
تماشا آموزش در یوتیوب:
https://youtu.be/Jg0Utycz7DE
این اپ یک پلتفرم مبتنی بر DNS است که برای شبکه‌های محدود و شرایط اختلال یا قطعی اینترنت طراحی شده است. این اپلیکیشن علاوه بر دریافت محتوای کانال‌ها، امکان گفت‌وگوی امن بین کاربران را نیز فراهم می‌کند.
📦
دانلود فایل‌های اصلی TheFeed:
https://t.me/thefeedfile
⚙️
کانفیگ‌های عمومی TheFeed:
https://t.me/thefeedconfig
📢
کانال WhiteDNS:
https://t.me/whitedns</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/4391" target="_blank">📅 06:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4390">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/88560d1079.webm?token=N2U-eYp96Z6HTzVj6EQwaj8SLG1rUotnE3xIf2lyi11espKbwS-N1IObjev2X39J8Zf9n91iZYqLm1iZGFKlAymxuSDbVhKSFg8crUvxY7Jw_8ye89D3eeI_MAD9FBOyHeghBwe2ugU_hsBj7NRBogcTILJLRymHsbKvQ8qyQQBzxMjbeevcomyAdq-npomzNRue4FJPwNjQp6ZTMilCcqb5hBuvyOPjJurLH5LF1N6trjkg8nMDRM4YFhM__zNJFZyhmtGZB3agPr_d4tr_fqd8yaBKZvvu5Y_j4SauVKe7zKvNdyIXxBRLoYdVxbUlEAP3c8UlHyaYWCqDwhLJXg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/88560d1079.webm?token=N2U-eYp96Z6HTzVj6EQwaj8SLG1rUotnE3xIf2lyi11espKbwS-N1IObjev2X39J8Zf9n91iZYqLm1iZGFKlAymxuSDbVhKSFg8crUvxY7Jw_8ye89D3eeI_MAD9FBOyHeghBwe2ugU_hsBj7NRBogcTILJLRymHsbKvQ8qyQQBzxMjbeevcomyAdq-npomzNRue4FJPwNjQp6ZTMilCcqb5hBuvyOPjJurLH5LF1N6trjkg8nMDRM4YFhM__zNJFZyhmtGZB3agPr_d4tr_fqd8yaBKZvvu5Y_j4SauVKe7zKvNdyIXxBRLoYdVxbUlEAP3c8UlHyaYWCqDwhLJXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/4390" target="_blank">📅 02:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4389">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">باز شروع کردن</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/4389" target="_blank">📅 02:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4388">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">حس میکنم وقتشه گوگل یه مدل image generation جدید از Gemini بده
خیلی عقب افتاده از GPT</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/4388" target="_blank">📅 00:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4387">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">و این رو هم بگم که این متد کلا مثل مابقی متدهای بر پایه‌ی کلودفلره، و همه‌ی هوش مصنوعی‌ها و اکثر سایت‌ها رو باز می‌کنه. اگر با سایتی مشکل داشت، با عوض کردن آیپی تمیز و یا Proxy-ip اوکی میشه به احتمال خیلی زیاد مشکلتون با اون سایت به خصوص</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/4387" target="_blank">📅 23:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4386">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">☠️
ساخت فیلترشکن نامحدود با پنل CFnew
🌤
- رفع ارورهای 1101 و 1104 کلودفلر
⚡️
فایل‌های مورد نیاز: https://t.me/MatinSenPaii/4385
⭐️
توی این ویدئو بهتون اینها رو یاد میدم: 1- آموزش ساخت پنل cfnew با دیپلوی اتوماتیک توی دو دقیقه(هم گوشی هم دسکتاپ) 2- معرفی جایگزین…</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/4386" target="_blank">📅 22:57 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4385">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">CFnew.txt</div>
  <div class="tg-doc-extra">202 B</div>
</div>
<a href="https://t.me/MatinSenPaii/4385" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">مربوط به
این
ویدئو</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/4385" target="_blank">📅 21:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4384">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Kib1k-WplYEqxa5cSsSNpW-emRzT13db-wd0Y1oLw1lkp6IJd2bXYXT3EOsACUOVFw5e6AKO0spy0VwJRlJMEkUqmV_uiiTdCBXZaDTgT7Y2veawLHmGZlEa5Sdr59bRsHFPJDcTZoKVcAO53JmzYUEV4Ssl3LgN7aY2us4P3753PcC-0bESQfAKxcCOA-5aR8VauVa4QV3Ruk8QFc_-sRkJvW30A-G22kZ1sYW2zNjGQcylFlrHMWlQThQZMKBBpmIuuTPygjybRrND3wcXmWPe_W1CRjlAtcrImhKfNvXF-d4mBqf2a6U9-tPtmhC5-HLX6slpZrqbXzUW9PGT1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
ساخت فیلترشکن نامحدود با پنل CFnew
🌤
- رفع ارورهای 1101 و 1104 کلودفلر
⚡️
فایل‌های مورد نیاز:
https://t.me/MatinSenPaii/4385
⭐️
توی این ویدئو بهتون اینها رو یاد میدم:
1- آموزش ساخت پنل cfnew با دیپلوی اتوماتیک توی دو دقیقه(هم گوشی هم دسکتاپ)
2- معرفی جایگزین AtomicMail برای ثبت نام توی سرویس‌های مختلف و کلودفلر
3- استفاده از اسکنر آیپی تمیز کلودفلر و اتصال به اینترنت آزاد
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این ویدئو هیچ پیش‌نیاز فنی و نیاز به خرید سرور و... نداره
با تشکر از برادران چینی عزیز
😂
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/4384" target="_blank">📅 21:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4382">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XFrMXcYum_uM_AHIER7b5UCDNLDhQNpB0qUa-jB5b7gUFVEc5ZfVfkKiQhbbVsUIXjIyKpa7H4sbj9YEkwzIlc8Z5UCEG9obIFRZGw2BBgLJkNYQyqIeq8_AcJYO26xcXBWFv41bkT_I-ehR5yxfuMBQoxZEztAOWkWTkn8d23tzybiTWscC7r-IkufzzxzMbDMbIp68KSOCrhdjgygR7SP82_lQ6Idrap8SHh18AJOdcKbMI-MP214bZlYyS79UyeqjYKA5mrfm0aCxDZM-Rxw7xf5fx0UykY4TbQoCt5lCEytDpM7QL02XSKGFW2fX2zgk34VusZoJXAvcgYZzJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/penMORZh_EIUwMkgM3SnnFbPVVlDRIDDi27DL8Bl4OCh1d6zOixxBX0NDDxbKYEEa6NYqOyHT-Kk65Waeag-3FxLz8k5SZXvg9EGvmCXMtIImwVg-Tif1aFP9QroGKUyQIpFAHanePUSLFyCF-AyZ9FV_i_2IzUjew6fPQCaJVvOWFRKPWDUC2aRStqEJZYmix0TwNtmQTdaLZiYFjiYXNZg641aQw1DqygFeQoDCHFEd3vPEcwa2tyqonSMTVIr5WMhHzM2KpDbWKyElts8IaHbGrEvGaZA1T2daBYdC0X0GrgwVL5ogUlaMVfXmpVVZFMHMDV7aV45yHKVovCiHA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه سایتی پیدا کردم سرور رایگان بهم داد و تونستم هرمس رو خیلی راحت روش بیارم بالا ..
نه کارت پرداخت میخواد نه هیچی! فکر میکنم دائمی هم باشه فقط موردی که هست من با ip های مختلف تست کردم موقع لاگین اگه ازتون کارت خواست ip  تون رو عوض کنین .. برا من با انگلیس اوکی شد و بدون کارت اکانت ساختم
لینک سایت:
https://www.alwaysdata.com/en
✍️
AmirHossein JPL</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/4382" target="_blank">📅 19:09 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4381">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">منظورم دقیقا اینه که دوتا ایمیل نتورک ابیوز اومده و سه تا پروژه‌ی قبلی abuse خوردن، اما روی همین اکانت الان وصلم و دارم این پست رو آپلود میکنم
😁
با روش برادران چینی اگر تا یک ساعت آینده وصل موند، ویدئوش رو میسازم</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/4381" target="_blank">📅 18:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4380">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KIZU05l44bTGe7fGXXFeyx2tISy_CNBU9_XK1r0-SkZBQSjq5b7YFRalFDkMm2kDT1SFcDmVCfsqchT_Y9IMCAbUzaX7muvlKLtiWf3onpRhUKrstUnPYXmJDBR8sFYES8I3dVC_t3LzXaXwxrn46AAJJEmOckXUhBbE9IV2qFR8Ke0z-RmARy6yGsjV6Ms3ebNqSjs33hMjJQ0KMK3XUu1RYj2H0VLd_ryopcvouNr6PLa1GrkvmosxjVYVhVGE_e5VXEVm_wHRy03KBPoST6ux5rWJNsEoUokquomL5WQw8oTCZlvW0Fi_jysH81Ocbrcqe_6wn9diUm0QLyjVPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوتا خبر خوب دارم اول اینکه مشکل 1101 رو روی همین اکانتی که network abuse خورده حل کردم دوم اینکه یه سرویس جایگزین و قدرتمند برای AtomicMail پیدا کردم که اگر یه وقت اون به مشکل خورد، بتونیم ازش استفاده کنیم</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/4380" target="_blank">📅 17:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4379">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">دوتا خبر خوب دارم
اول اینکه مشکل 1101 رو روی همین اکانتی که network abuse خورده حل کردم
دوم اینکه یه سرویس جایگزین و قدرتمند برای AtomicMail پیدا کردم که اگر یه وقت اون به مشکل خورد، بتونیم ازش استفاده کنیم</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/4379" target="_blank">📅 17:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4378">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cWBZCKJYM1aT-8ZtzTW5Y0_nxifMaY0KHC_s4oE58esx0jcK-4xJWK_w-6G53x_2_M-3ze0DJR1fhT0I3ZfwKnuUXnHZc96hyW1gRUzWO3CXOmmBNL6sFkLnL71ReliINCYmKzmk7weyVbgBfGx0sH2f4nI9M0dByNwGWW2iMyCysczWap2aR87eWMxOCU16Wk9Th0b8i5sCGJdUpERxZSgsi216Xew5RD5k_0MhAgYOgb3z_pAmmGw3R0zVPqyFLIJ3SJ1DqzU3HqjYkNRUnt2NN1b5PBIqQLhFL_7sbSSuASAZiGxkcmYG-alUZEwul6jT4YZe51Mh0KGmXWjokg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشغول دیدن ویدئوهای برادران چینی هستم ببینم چه گلی به سرشون گرفتن</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/4378" target="_blank">📅 16:59 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4377">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ckdawv6riHURaIK1gtYXrxmdeRHHcN87Titl7-ZKqs5I3w3dktISvc0HjNTruRreFgKyf76cDOGVCaZw1KLbXgZ14nZC2o65UcVqS8PltbIZt-x6nomgL1wTdvdyDTO2MMv07E3xOScso1Q11ze2bxVFfA9QJCrmBBbOv-ifWFPoFk9L5FRngvqElPaFfxQ5NuYiWC31YH3lJE-KCX70BL70TbFsiLv-CoJg20TV_ryWN53q8Ajw9fKBUlWtTIiBNAyWEte549Mh_DPuLutJTxfL5pKr8dqJIY_b9yy5uvdhWIkFAECLRqoRYmi-uyUC9R6nA5SbGt9MyVExM8bQXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه گیر و گورایی از توی پروژه‌ی +220 هزار خط کدیم کشید بیرون که باورم نمیشه با Sonnet5 تازه</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/4377" target="_blank">📅 16:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4376">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">مشغول دیدن ویدئوهای برادران چینی هستم ببینم چه گلی به سرشون گرفتن</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/4376" target="_blank">📅 16:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4375">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dVaQVLhQZKLZNSRGB3q6uMOEKfO841gvyuHIsErhFtNFxQiNt63286I9BS3pOIUpCuS-6eK3dU31QVxxVk7SKja6k-kpcYRsD1__4Q0-31AtEU5R61usAWzdHW1rVfSNkEZp0z7eMTcHrIRd_YHrCqr3bfifUMvMe9zaFNBxmiZSMFX0JbL0pJnVJZlQOY-SY3MNnCr6lxRz8R2aJqDiDHlnKbxv9jX5qPYlfkxHaDbSCTQ8YuFOgol6gG3dFf7VZtuQbw5PkW-Irvan_tOHwtKnGSN_pSc26vtbvUzIG7PBbvIkYnUXvE3rN4rHqjHkcUNbbqs5N50xkavpztqMuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر به ارور 1101 کلودفلر خوردید، علتش دقیقا همینه که کدهای پنل ممکنه توسط کلودفلر، سؤاستفاده تشخیص داده شده باشه و باید اکانت جدید بزنید. ترجیحا از پروژه‌های قدیمی‌تر و قدرتمندتر که Edge و BPB و Cf New باشن استفاده کنید، ببینیم چی میشه بیشترین گزارشی که سر…</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/4375" target="_blank">📅 16:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4374">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اگه فقط چند روز از اشتراک Claude Fable (یا مدل‌های خفن مشابه) واستون مونده، این کار رو انجام بدید
🔋
:  ابزار جدیدی به اسم /improve معرفی شده که ایده‌ش خیلی جذابه: از خفن‌ترین و قوی‌ترین مدلی که دارید برای بررسی (Audit) کل کدهاتون استفاده کنید تا بیاد برای مدل‌های…</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/4374" target="_blank">📅 16:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4373">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PZZ1nzo8bcq-puDrO1LIafFjjFkTgWwqh8ysYMF9q3_0HhB3mRNrggRfIZ_4APO6JuhxXMlWwuK_PNFMnmNt-FW8ULZQf7ZfBYRiIwUPsTdQYF-aZcd1x4nre5h7mVSgghuq6pEmvEDkeKCTmwXi9z9KTKulhuWXkHl4Ey5JvGTqXA84sIJgETCGMRu5tBjY8CEyaoNSAOw30FDDoo5s0gdwwI2Qa0yJRX4MbaQSGs0yz-x8g3trpgK3cjsVUfV2lQUhdTCNjm7ET_AaA6IbKnATNFvng5QkSmpHa1f5zs4dI4PNsXoX7l-3A7MZS905PVDhuOwA-g01_GlylUEO5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه فقط چند روز از اشتراک Claude Fable (یا مدل‌های خفن مشابه) واستون مونده، این کار رو انجام بدید
🔋
:
ابزار جدیدی به اسم /improve معرفی شده که ایده‌ش خیلی جذابه: از خفن‌ترین و قوی‌ترین مدلی که دارید برای بررسی (Audit) کل کدهاتون استفاده کنید تا بیاد برای مدل‌های ارزون‌تر یه پلن اجرایی دقیق بنویسه و پروژه رو ارتقا بده
✈
این ابزار می‌شینه کدهاتون رو بررسی می‌کنه، باگ‌ها، مشکلات پرفورمنس، بدهی‌های فنی (Tech debt)، تست‌هایی که یادتون رفته بنویسید و چیزایی که باید ساخته بشن رو درمیاره. در نهایت یه نقشه راه (Plan) تر و تمیز می‌نویسه که هر ایجنت دیگه‌ای (حتی مدل‌های ارزون) بتونن برن و اجراش کنن
🎨
شما می‌تونید این ابزار رو روی کل سورس‌کد پروژه‌تون یا حتی فقط روی همون برنچی که الان دارید روش کار می‌کنید ران کنید. هر پلنی هم که براتون می‌سازه خیلی دقیقه و شامل بخش‌های بررسی، کشف ایرادات، اسکوپ کار، نحوه اجرا، تستینگ و شروط توقف می‌شه
💪
لینک سورس کد این پروژه تو گیت‌هاب:
https://github.com/shadcn/improve
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/4373" target="_blank">📅 15:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4372">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">شنیدم گویا چند نفر دارن پنل‌های ایرانی تحت کلودفلر رو مدام گزارش میده به خود کلودفلر که احتمالا از دوستان VPN/VPSفروش هستن(همه‌شون این شکلی آدمای بدی نیستن طبیعتا. صرفا یه عده) و فکر کردن با این کار می‌تونن جلوی وی پی ان ساختن روی ورکر کلودفلر رو بگیرن. که…</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/4372" target="_blank">📅 14:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4371">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">شنیدم گویا چند نفر دارن پنل‌های ایرانی تحت کلودفلر رو مدام گزارش میده به خود کلودفلر
که احتمالا از دوستان VPN/VPSفروش هستن(همه‌شون این شکلی آدمای بدی نیستن طبیعتا. صرفا یه عده) و فکر کردن با این کار می‌تونن جلوی وی پی ان ساختن روی ورکر کلودفلر رو بگیرن. که خب باید بگم نابینا مطالعه کردن
🥰</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/4371" target="_blank">📅 14:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4367">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SZGZBgvQ-LZMPuf-_uMhWCjT2bUM6cAmqOvtza0-KBzWnJuNFsqwC0NAj1xB9MIcZQQ1L-JYyDc81-eY9P8KllIhbf86-yqTi8gHwLKE6kDVZP7AkPi07Bi138620jmZKoIIYDAFtTHgOjtUHOBHsnBV4CwAFURgnjENCllRq8Cz7c5SmW-6KsUOanjjAUrfUhhFKfVL-DFCwxu2zCukNxWHuSu21lGXKWOz5-3KIxkyeDCRh73oLwrmkQ5evCERIhXlL8M47ypkmMTDz1hOlx0rCfG5RGowgMB3S_hgxJAy7tscwcJ3pOVqDWfQey_WVHHyy1o1B1pCOT__7yZbgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gg0r4XltQtQ11TZqjnzgp-nzQBvvPtFW9Sy_7klSGha5o1mdT9Y8wXrRfL-DHzs96h9Qdzi7U54fVI4w32LAZm7kiryuxkRKAOopMtP8pi8TI1SxUKf4deuMzYx7U76qt0YhPKhtqFuh3Njbzzk90DH5ELAEicZy3XAQSJ040qjrF5HYJNFu2VWwP2LR0aEIxN0vgxzSc5wqYAZ4Ul3spS7v4tuZSwNJnTuXTA8IxWL5kpJQhcmKw02-XuQJyIAyaLJ08DXO6BZ5_-Da3d_uEXWKs2zZoykYj8XigEHuZ6IIlCUNKApq8j7_kCnjI7OKUZt2p45k7KY0FcabjP9i1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ExlO8vU_ECEo-nXblj7ve-5IACfcctEdrT9wizk_jOS7li_PCK6xK5qjRMaoDhhhlKSyLCKDNCqq27SvGyD9A2w_k6vmOaSjWj6oOwBa8QrmlQN2rqOoDd99SgRDP34QFx2Wr8FiFa2bqzlAzI3o2A5jMvZj2KwsocRs3sl7eSpg2yihZ65Gm3NtbMQwaYQCG2jlADjBRbTp91Flng9soaMIW3YSDApVL4RKDK9f9LdrsXHqQpZsvJa1uaVS7BA0k_6AOtlcKSfpmlGyX2HTJsOzhPZuxZPbebGmkF1jbJR9eEHP0CxjWw9WW3S3XjYMjJBhJ0OxsydhHhPxsp5kpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rTnVvl07Sh9n-GGuhZV2cHU4NpKMgfrSv-Lg5Fqxcn1DTe_MKvtGA0vNmReDrBOWZCc6yxzteOD7lH9LRyMNhz5Bcz3bgpdZpRNEagyn4Q_Coe-wuW2RQNQYn3JPLA1v82hbd9lxyK6ZfGrrfz7kUQlS67VM2rGdFjaCC-qATaMs56zc6Sg6gV2I_VSiFhddzI9ikgnKRsZAFtgg1GtjyQ0rBvpcGGy5uwzuozsHgNFnQxZsO1qX5_9jQ3ei69O5VIPb7nJ-xzSVO-00NAqo_hiBYb66u-QQhAKbRYn-URmITY1B3N5He5E8DSS-Caxp16-E35WohYgjj84fCkWysA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">لینک زیر رو به هرمس بدید و بگید:
اینو نصب کن، فعال کن و بذار تو استارتاپ سیستم تا با روشن شدن سیستم اجرا بشه.
بعد از نصب یه محیط بسیار زیبا تحت وب در آدرس لوکال زیر برای شما فعال میکنه:
http://localhost:8787
https://github.com/nesquena/hermes-webui
✍️
بوکانت</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/4367" target="_blank">📅 07:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4366">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">فردا open design و claude design رو واستون یه مقایسه میکنم از اونجایی که روز آخر اشتراک کلاد 20 دلاریمه، آتیش بزنم به مال(توکن)ـم
ولی ویدئو فعلا ازش نمی‌گیرم. صرفا اینجا بهتون نشون میدم
چون هنوز به open design مسلط نیستم کامل
در عوض تمرکز می‌کنم روی ویدئوهای درس خوندن با ai و بالاتر بردن efficiency</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/4366" target="_blank">📅 05:01 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4365">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/720362863c.mp4?token=sz-tvvsVALQSzLqXqkUE9oZGoeXyM_ExbffXsc1TAqPMv8WngSQ8iegRaART0RekwTQOrFlFyAPa6OEdh48SbAqAa25Sni-37zfjrror0M31ofmjURlbQQo7bGzX0AREfo6rJ-87yLTzNuvZJIduxO-v7utkmi84kH2sxxVJdkcy6YHhde2FPMFab2r6gmco7M4mDbUcC84hsQqWtoMI9lflTFZ-TxZrq71CF3FjPxDb2rNksQrZjpUzC_t1RWpuM9uQOW1nMxrPqy_0yb577P_d1o1FaRQ4ovmlgX72LIAxKMHvaDMltqE2ajQaa3372Yl3TA4L4Tib2xyoWTvUHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/720362863c.mp4?token=sz-tvvsVALQSzLqXqkUE9oZGoeXyM_ExbffXsc1TAqPMv8WngSQ8iegRaART0RekwTQOrFlFyAPa6OEdh48SbAqAa25Sni-37zfjrror0M31ofmjURlbQQo7bGzX0AREfo6rJ-87yLTzNuvZJIduxO-v7utkmi84kH2sxxVJdkcy6YHhde2FPMFab2r6gmco7M4mDbUcC84hsQqWtoMI9lflTFZ-TxZrq71CF3FjPxDb2rNksQrZjpUzC_t1RWpuM9uQOW1nMxrPqy_0yb577P_d1o1FaRQ4ovmlgX72LIAxKMHvaDMltqE2ajQaa3372Yl3TA4L4Tib2xyoWTvUHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی ردیت یه نفر یه پورتفولیوی کاری ساخته که رسما مرزهای فرانت‌اند رو جابه‌جا کرده
😂
طرف طبق گفته‌ی خودش، فقط به Claude Fable 5 یه دستور خیلی کوتاه داده(که البته من به شدت شک دارم):
"یه پورتفولیو می‌خوام که کاربر نخوندش، بلکه توش پرواز کنه!"
نتیجه این شد که کلاد صفر تا صد یه سایت سه‌بعدی رو ساخته که شما توش تو فضای بی‌کران اسکرول می‌کنید، سیاره‌ها و پروژه‌ها از کنارتون رد می‌شن، از تکسچرهای واقعی ناسا (NASA) استفاده شده، گرافیکش روی مرورگر کاملاً 60fps ران می‌شه، و در نهایت وقتی به آخر سایت می‌رسید... سفینه‌تون می‌خوره توی خورشید و منفجر می‌شه!
😂
این پروژه قدرت وحشتناک هوش مصنوعی توی ترکیب کتابخونه‌های پیچیده مثل Three.js با کدهای فرانت‌اند رو نشون می‌ده. که اگر بتونید AI رو توی مسیر درست هدایت کنید، خروجیش به شدت جالب می‌شه.
لینک سورس کدش تو گیت‌هاب (اگه می‌خواید خودتون تستش کنید):
🔗
https://github.com/AbhishekBadar/portfolio
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/MatinSenPaii/4365" target="_blank">📅 23:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4364">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">از بین سه تا پنل BPB و Edge و نهان که آموزش دادم، به شخصه برای خودم Edge سرویس‌های بیشتری رو باز می‌کنه بدون نیاز به proxy_ip. اون دوتا نیاز به proxy_ip دارن اکثر اوقات تا به درستی کار کنن یا نیاز به تعویض کلاینت یا dns معمولا. اما edge بهتر بوده تا الان حقیقتا.…</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/4364" target="_blank">📅 19:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4363">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">از بین سه تا پنل BPB و Edge و نهان که آموزش دادم، به شخصه برای خودم Edge سرویس‌های بیشتری رو باز می‌کنه بدون نیاز به proxy_ip. اون دوتا نیاز به proxy_ip دارن اکثر اوقات تا به درستی کار کنن یا نیاز به تعویض کلاینت یا dns معمولا. اما edge بهتر بوده تا الان حقیقتا.
آموزش راه‌اندازیش روی
دسکتاپ
و
گوشی</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/4363" target="_blank">📅 19:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4362">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPersian GitHub(Afshin Karimi)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdRK9tPld0SONSRy2_ovRN0897fjDcf-3TSwHR-YZxEde9QjquFP1Pne1YfcW_yqDLdwGmOTm6-Ear34Gr2HS2PwN8KIAGgByCRto3JeQvGH7lEacdv5spwQelChw-HYy_GEcNCWF2X6WnncryygOpGDMYUlFU_zdxd0LPhfGt8tmuxs7kkPIUz3MoNzZD9UXj5zANih1Xq-5DC1lBmnOemmWk3wUYj2PykgApPN1Nrbrv6TYHUifXZPW9fa_hCipUGHoJG-C8Y1G5VeMOTa1o3T_cltOHtf_Vo3dvPaS2tRiPbEzNzVv980MeCvp1OFz8YB4ksPF0MiDYilGiZL5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه GameShell یک بازی متن‌باز برای یادگیری دستورات لینوکس است که به‌جای آموزش‌های سنتی، مفاهیم را از طریق مراحل و مأموریت‌های تعاملی یاد می‌دهد.
اگر تازه می‌خواهید لینوکس را شروع کنید، این بازی می‌تواند راهی سرگرم‌کننده برای یادگیری دستورات پایه باشد.
https://github.com/phyver/GameShell
@RepoFa</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/4362" target="_blank">📅 17:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4361">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">به نظرم اگر می‌خواید برنامه‌نویسی یاد بگیرید، بهتره که یک زبان، و از اون زبان یک حوزه رو در نظر بگیرید و شروع کنید به یادگیری.
برای مثال اگر بخواید پایتون یاد بگیرید و همزمان توی حوزه‌های AI و Back-End باهاش کار کنید، آخر سر به خودتون میاید می‌بینید هیچ کدومش رو درست و حسابی یاد نگرفتید.
و همیشه در همین حین، سه تا سؤال از خودتون بپرسید.
1- چی دارم یاد میگیرم؟(روشن شدن مسیر)
2- برای چی دارم یاد میگیرم؟(روشن شدن هدف)
3- قراره باهاش چی بسازم؟(تبدیل به انگیزه میشه و دل‌زده نمی‌شید)
این پروسه‌ایه که من خودم طی میکنم برای هر زبان-فیلد جدیدی که می‌خوام یاد بگیرم. کاملا هم نظر شخصیه و چیز ثابت شده یا علمی‌ای پشتش نیست لزوما</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/4361" target="_blank">📅 16:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4360">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اگه با ایجنت‌های کدنویسی کار کرده باشید، می‌دونید که بزرگ‌ترین مشکلشون Over-engineering کردنه. یعنی مثلاً برای یه تقویم ساده که با یه تگ HTML حل می‌شه، میرن یه کامپوننت ۴۰۰ خطی با نصب کلی پکیج اضافه می‌نویسن
😳
ابزار Ponytail (که الان به شدت تو کامیونیتی وایرال…</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/4360" target="_blank">📅 15:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4359">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SXWemSTOAymy_ohM6uUYoiGFsYhvlDs-sTw1zV3a-YkjF2f3d9scg7gDjV4xIQfLazvAf_pwrXh2gqMCMMTCVi7dP2hftwLlW0dqx_n9BHGGVOQik3HtUOJWBVUzbu72oIQfeZ4ZF1PTsWbaI5ut3lCCyo4GdLIIgA_rXJlhvBdM9GV6A_bzVKQbwyiFGpxfFnaYwxr0Poo79Ea3PreoOz52f5vZ7SXJpTXHwdQFPgnYQfD1jTS98CFRw5eC5abhEnNVN5SVZfWeQOqmWKmjiMqtFPjpZxW8xKlG90Lx0siyu7MiT8hgpPVaxaPcsC4VvrMLFDjdwOxzJNKIuer2Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه با ایجنت‌های کدنویسی کار کرده باشید، می‌دونید که بزرگ‌ترین مشکلشون Over-engineering کردنه. یعنی مثلاً برای یه تقویم ساده که با یه تگ HTML حل می‌شه، میرن یه کامپوننت ۴۰۰ خطی با نصب کلی پکیج اضافه می‌نویسن
😳
ابزار
Ponytail
(که الان به شدت تو کامیونیتی وایرال شده) دقیقاً یه پلاگین برای حل همین مشکله. این ابزار باعث می‌شه ایجنتتون مثل همون برنامه‌نویس‌های سینیورِ تنبل شرکت که حوصله‌ی کدِ اضافه نوشتن ندارن، رفتار کنه
🙄
شعار این ابزار اینه:
«هیچی نمی‌گه. فقط یه خط کد می‌نویسه. همونم کار می‌کنه.»
چطور کار می‌کنه؟
قبل از اینکه ایجنت حتی یک خط کد بنویسه، مجبورش می‌کنه این نردبان رو تو ذهنش طی کنه:
- اصلاً این فیچر نیازه؟ (قانون YAGNI) اگه نه، بی‌خیالش شو.
- آیا توی کدهای فعلی پروژه قبلاً نوشته شده؟ اگه آره، همون رو ری‌یوز کن.
- کتابخونه‌های استاندارد خود زبان می‌تونن حلش کنن؟
- آیا مرورگر یا سیستم‌عامل خودش اینو داره؟ (مثل استفاده از
<input type="date">
به جای نصب پکیج).
- آیا پکیجی که از قبل تو پروژه نصبه این کارو می‌کنه؟
- می‌شه توی یه خط نوشتش؟
- فقط در نهایت: حداقل کد ممکن رو بنویس.
طبق بنچمارک‌ها، این ابزار حجم کدها رو ۵۴ تا ۹۴ درصد و مصرف توکن‌ها رو ۲۷٪ کاهش می‌ده. البته اینم بگم که تو مباحث امنیتی و Validate کردن اصلاً تنبلی نمی‌کنه و امنیتش ۱۰۰ درصده
❌
آموزش نصب روی ابزارهای مختلف:
توی Claude Code
کافیه دو تا دستور زیر رو جداگانه توی پرامپت بنویسید:
/plugin marketplace add DietrichGebert/ponytail
/plugin install ponytail@ponytail
توی هرمس (Hermes Agent)
hermes plugins install DietrichGebert/ponytail --enable
بعد از نصب می‌تونید با دستوراتی مثل /ponytail یا /ponytail-review کنترلش کنید.
توی Cursor، Cline و دیگر
ide ها
نیازی به پلاگین نیست. کافیه فایل رول‌ها (مثل .cursor/rules/
ponytail.md
) رو از گیت‌هابش دانلود کنید و بندازید توی پوشه‌ی پروژه‌تون.
توی GitHub Copilot CLI
/plugin marketplace add DietrichGebert/ponytail
/plugin install ponytail@ponytail
توی Gemini CLI (Antigravity)
agy plugin install
https://github.com/DietrichGebert/ponytail
لینک ابزار:
https://ponytail.dev/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/4359" target="_blank">📅 14:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4358">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">هوش مصنوعی به جای یک فایل، کل درایو C رو پاک کرد!
😐
چند روز پیش توی گروه جامعه وایب کدینگ ایران، افشین یه تجربه عجیب رو منتشر کرد.  داستان از این قرار بود که با Z.ai و مدل GLM 5.1 یا GLM 5.2 از AI خواسته فقط یه فایل رو حذف کنه، اما ظاهرا به جای اون، کل درایو…</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/4358" target="_blank">📅 12:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4357">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجامعه وایب کدینگ ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cvCqpiQvBM3e1Gy7BNJo7ReowTkYD4s-dD_gBL99vClT9Pe5OXCR12A4nvxaNDfgOmLXkV-d5AOuijToQ6w52mI3n0U2NWBPE4YG2FXUQpUBHTbpV9LzASpgvx4bBYmhbiriI6vwFmW0hAEniyshk_AUXO9yGuxd5CUZeIH_yZWOoM5ksKT1L5zy6Aw4BrUHpeJjsQVuK6Bvx83CmpqZFteqQF8nv_R2UdPAeH4JPx8hKx9X88vkZGqUoCd7156D40fHvGgAGsN7XsUgmwJIG_GfT1SE2e19kp68d28ibGuTi-uC3dQroyv7o557XHr9BJhXYUCRfxtNmVxz8b1FIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش مصنوعی به جای یک فایل، کل درایو C رو پاک کرد!
😐
چند روز پیش توی گروه جامعه وایب کدینگ ایران، افشین یه تجربه عجیب رو منتشر کرد.
داستان از این قرار بود که با
Z.ai
و مدل GLM 5.1 یا GLM 5.2 از AI خواسته فقط یه فایل رو حذف کنه، اما ظاهرا به جای اون، کل درایو C ویندوز پاک شده!
این اتفاق یه یادآوری مهمه.
هرچقدر هم Agentهای هوش مصنوعی باحال و قدرتمند باشن، وقتی به ترمینال، فایل های سیستم یا دیتابیس دسترسی کامل داشته باشن، یه اشتباه کوچیک می تونه به یه فاجعه تبدیل بشه.
اتفاقا متین سنپای هم امروز ابزار Kastra رو معرفی کرده که دقیقا برای همین سناریو ساخته شده. این ابزار بین Agent و سیستم قرار می گیره و برای کارهای حساس مثل حذف فایل یا تغییر دیتابیس، اول از خودت تایید می گیره تا AI نتونه هر کاری خواست انجام بده.
به نظرم تا چند وقت دیگه استفاده از ابزارهایی مثل Kastra دیگه یه قابلیت اضافه نیست، بلکه برای هر کسی که با Agentهای کدنویسی کار می کنه، واجبه.
تا حالا Agentها چه خرابکاری هایی براتون انجام دادن؟
😅</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/4357" target="_blank">📅 12:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4356">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EiF4yiYvw_cGDGGu7MrtXISZaN6nyhMyiXl463ryGiGBNXS6sP-6iTx0q4_hH4RXvj2rdvG3tTjMsPLn7GbkoSll7bk6B04eCKQh5V2IJVlUQ0Tcp-jnLEMA3LmN3Zz6aZ4ZxCn61W4BDDcRIz7vGLJNZLh0ZOlfN9VzfqEBX-LYXHpU4VlmdV1QBnHJhLBe57L7qD9hvGEs6myXEQscP8tvRMROyvZWf5FZu5kEcTDF64JkvLFP027p80qL8oXuht78E2TC22MU4v_htwEjJFnfDOol9fl4l6ZKTto2-pN9YLNYsUd1j3Q1f4uCqgn-XfYav-zV0RQjthBHfSgX6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابزار Kastra برای کنترل ایجنت‌های کدنویسی
اگه با ایجنت‌هایی مثل کلاد یا هرمس(روی Yolo) و یا هر ایجنت دیگه‌ای روی کدهای حساس کار می‌کنید، استفاده از سیستم‌های نظارتی دیگه یه آپشن نیست صرفا به نظرم، بلکه واجبه!
توی Hacker News یه ابزار خیلی خفن و کاربردی به اسم Kastra معرفی شده که کارش اینه که به عنوان یه «لایه‌ی دسترسی و تایید» (Authorization Layer) برای هوش مصنوعی عمل می‌کنه. یعنی دقیقا روی فراخوانی toolها توسط ایجنت‌هایی مثل Cursor و Claude Code نظارت می‌کنه تا اونا سر خود کاری نکنن.
چرا اصلاً به Kastra نیاز داریم؟
ایده‌ی ساخت این ابزار زمانی به ذهن تیم سازنده‌ش رسید که ایجنت خودشون نزدیک بود یه دیتابیس پروداکشن رو به کل پاک کنه! وقتی به مدل‌ها دسترسی کامل (مثل کار با ترمینال یا دیتابیس) می‌دید، هر لحظه ممکنه توهم (Hallucination) بزنن یا اشتباه کنن. Kastra اینجاست تا جلوی فاجعه رو بگیره.
ویژگی‌های اصلی:
- پشتیبانی کامل با mcp: تو کمتر از ۲ دقیقه می‌تونید با Cursor، Claude Code و پروتکل‌های MCP وصلش کنید.
- گاردریل‌های امنیتی: می‌تونید براش قانون بذارید که ایجنت برای کارهای خطرناک (مثل پاک کردن یا تغییر دیتابیس) اول از شما اجازه بگیره.
- مدیریت دسترسی: مشخص می‌کنید که ایجنت شما دقیقا به چه ابزارها و چه بخش‌هایی از سیستم دسترسی داشته باشه.
لینک ابزار:
https://kastra.ai/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/4356" target="_blank">📅 10:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4355">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/885f71c1ea.mp4?token=OvfJf1S5K5viFyJe9qJm4KfEzWR8fxedeL-MH4b3SMam7mSdC1bpnctnDOwCBYvD0vLeUAZek1ZVyQu2dtDlZ0n7xStcypYbvvX6WjyAvBwGvL54qAr53JIS5t6L_FtYQfijwjSN48y1-JNWricUIxhFsPZ3-EPP66e8rT3CZC74kddJvfnKJnEnHfi8hv8awoxS4viZ13VwKM3AlKMyQUkbSsBLF55AFATDEjDNvbSZ_Yq4VeFfHEQvCevtaFclWRPePqB07z2WBUrGfhMyNfUWioSIMf5uLheiaaXmhM4litZsr-Zfwcg3hXtFlqsk4LdUw8gObqFH1P5ohw-NnA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/885f71c1ea.mp4?token=OvfJf1S5K5viFyJe9qJm4KfEzWR8fxedeL-MH4b3SMam7mSdC1bpnctnDOwCBYvD0vLeUAZek1ZVyQu2dtDlZ0n7xStcypYbvvX6WjyAvBwGvL54qAr53JIS5t6L_FtYQfijwjSN48y1-JNWricUIxhFsPZ3-EPP66e8rT3CZC74kddJvfnKJnEnHfi8hv8awoxS4viZ13VwKM3AlKMyQUkbSsBLF55AFATDEjDNvbSZ_Yq4VeFfHEQvCevtaFclWRPePqB07z2WBUrGfhMyNfUWioSIMf5uLheiaaXmhM4litZsr-Zfwcg3hXtFlqsk4LdUw8gObqFH1P5ohw-NnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در کنار معرفی GPT-5.6، OpenAI یه کار جالب کرد و ChatGPT Work رو معرفی کرد. که به عنوان یه ایجنت می‌تونه کارهای طولانی رو روی فایل‌ها و اپلیکیشن‌ها انجام بده و ساعت‌ها روی یه پروژه متمرکز بمونه. به نظرم کم کم شبیه به هرمس، تمام ورک‌فلو‌ها و لوپ‌های پیچیده دارن…</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/4355" target="_blank">📅 06:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4354">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">در کنار معرفی GPT-5.6، OpenAI یه کار جالب کرد و ChatGPT Work رو معرفی کرد. که به عنوان یه ایجنت می‌تونه کارهای طولانی رو روی فایل‌ها و اپلیکیشن‌ها انجام بده و ساعت‌ها روی یه پروژه متمرکز بمونه.
به نظرم کم کم شبیه به هرمس، تمام ورک‌فلو‌ها و لوپ‌های پیچیده دارن تبدیل به زبان طبیعی می‌شن.
شما می‌خواید، و انجام می‌شه
هرچند هنوز، مهندسی اینها، و نظارت روی کدی که AI می‌زنه، خیلی مهمه به نظرم.</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/4354" target="_blank">📅 05:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4353">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/802171ad75.mp4?token=QBz59PBwDQps-uWkZ7AUVRww8CRVTlRCFKJBG_3yPJI3b2XJGgHDvVt_wdsjWW_uI7sdnPKiBxMYJclpRe97SZMmCXqD_sxZo3hOs1Sbft3a2_UeWT4gKts9GCH7dOQ9z8liyPh8-zXEAzKXX_0C4ANes0EQwKrqeHF_IBdP7ojoqNVryyXLO3thZhWGWR3dZEF-2YFGLEV5ZLvW99fA3GNA_ijE9pfjbmS5563YsMkbPHurRWZZoaAUzltn_EvmbnvTRWtJ_FBpZR6ya8fPVnAgket4o_Sswv9eDeWEjFcaOVGOgCKZrvsx3RfJCWrr3cf3Nku70bcL0YxzN_JTSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/802171ad75.mp4?token=QBz59PBwDQps-uWkZ7AUVRww8CRVTlRCFKJBG_3yPJI3b2XJGgHDvVt_wdsjWW_uI7sdnPKiBxMYJclpRe97SZMmCXqD_sxZo3hOs1Sbft3a2_UeWT4gKts9GCH7dOQ9z8liyPh8-zXEAzKXX_0C4ANes0EQwKrqeHF_IBdP7ojoqNVryyXLO3thZhWGWR3dZEF-2YFGLEV5ZLvW99fA3GNA_ijE9pfjbmS5563YsMkbPHurRWZZoaAUzltn_EvmbnvTRWtJ_FBpZR6ya8fPVnAgket4o_Sswv9eDeWEjFcaOVGOgCKZrvsx3RfJCWrr3cf3Nku70bcL0YxzN_JTSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍷
درود به همه رفقا...
اگر کانفیگ میزنید و فرگمنت روی ip ها کار نمیکنه واستون بهتره که از دامنه برای ip تمیز استفاده کنید...
برای مثال بهترینش:
Chatgpt.com
Grok.com
با این مقدار فرگمنت:
Packets: 1-3
Interval: 1-1
Length: 1-7
اگر کلاینت Fakehost داشت:
Google.com
رفقایی که ابتدایی تر هستن داخل ویدیو کوتاه نشون دادم داخل هر مدل گوشی یا کلاینت که کانفیگ میزنید هست
✅
💡
نکته:اگر کندی در کانفیگ یا آپلود ندارید روشن کنید fragment رو عزیزان.
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/4353" target="_blank">📅 01:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4352">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">به شخصه پلن کلادمو ReSubscribe نمیکنم؛ تا ببینم وضعیت قطعی نت چی میشه به شما هم توصیه می‌کنم اگر تموم شده و کارتون زیاد لنگ نیست، نخرید فعلا..</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/4352" target="_blank">📅 00:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4351">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/88560d1079.webm?token=slStrjLuWJAXu0fXBKw3-KCfgQV1YsBYlNQRSmfd-m98Std7n3eg4L94bkQSgPm4D8oniQjdja7z5TT29c1JitKNIfVk2E6hZXQpP3hAZDRKpwkQi1zIDRnjQQhZcc5OHnUoRzyGBsfUcWXjWHNlo1KU6NsPxy4HTD0Rf5HPWzdxvFyojBmWlL6B-YKLsj4EcVQ_ehMOBQM0Gbgm24e-NBQDd94I8TtJCOQ3cLE30JUGyA_6X0GbFgma9ivxDqSf0lJCf8X8aARNMTtwr2uQ2v7uDleE-b6URF_u4dOI9HNGdLIO8SX-J5MuoEkTzNg07bAItH56pCikP9PPImGlow" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/88560d1079.webm?token=slStrjLuWJAXu0fXBKw3-KCfgQV1YsBYlNQRSmfd-m98Std7n3eg4L94bkQSgPm4D8oniQjdja7z5TT29c1JitKNIfVk2E6hZXQpP3hAZDRKpwkQi1zIDRnjQQhZcc5OHnUoRzyGBsfUcWXjWHNlo1KU6NsPxy4HTD0Rf5HPWzdxvFyojBmWlL6B-YKLsj4EcVQ_ehMOBQM0Gbgm24e-NBQDd94I8TtJCOQ3cLE30JUGyA_6X0GbFgma9ivxDqSf0lJCf8X8aARNMTtwr2uQ2v7uDleE-b6URF_u4dOI9HNGdLIO8SX-J5MuoEkTzNg07bAItH56pCikP9PPImGlow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/4351" target="_blank">📅 00:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4350">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">به شخصه پلن کلادمو ReSubscribe نمیکنم؛ تا ببینم وضعیت قطعی نت چی میشه
به شما هم توصیه می‌کنم اگر تموم شده و کارتون زیاد لنگ نیست، نخرید فعلا..</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/4350" target="_blank">📅 00:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4349">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">یکی گروک مدل grok 4.5 رو داده بیرون، یکی هم متا مدل جدید داده بیرون به اسم Muse Spark 1.1 هر دو هم ادعا کردن که هم سطح Opus 4.8 هستن با هزینه کمتر، ولی به نظرم متا دروغ میگه
😂</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/4349" target="_blank">📅 23:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4348">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K2inSyqky84NvevUjFhITsJ-bGMosDpJS2N_5LBZxuFzmVe6xLJCtY7BrtYfqhk02XKYr3eP3yLGgvWF2oYKFnop7YNt_pn6HhDMM2UJ9-j1kDJ2oQelQF4SIPQ2xONSyAgJnWayPsMX2oDY3smxueotScDXjDTIDeLuoL2IkEoI8t1qqVcUoALGl8dp8KSYz1Ep_CEfDuRWpyUKKADrUBXsuu3Dc9ZKy7Y2UwfJ7Jp7Ot_CdKqW529Dc_KCZaQfBAXTmt4UbtjY9AslTx-BklsrgKBoW2_oIwSXLqstTX3VNytZdlpVmIvp1uxAMFhnrbWjvpFOyVh2ju-keG-PDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر درست باشه فوق‌العادست
بچه‌های توییتر تست کردن Grok چهار و نیم رو، همه تعریف تمجید کردن</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/MatinSenPaii/4348" target="_blank">📅 22:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4347">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">یکی گروک مدل grok 4.5 رو داده بیرون،
یکی هم متا مدل جدید داده بیرون به اسم Muse Spark 1.1
هر دو هم ادعا کردن که هم سطح Opus 4.8 هستن با هزینه کمتر، ولی به نظرم متا دروغ میگه
😂</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/4347" target="_blank">📅 22:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4346">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">اتهام جاسوسی به Claude Code؛ چین درباره ابزار برنامه‌نویسی آنتروپیک هشدار داد</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/4346" target="_blank">📅 21:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4345">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">یه کاری کردن انگار شرطی شدیم
تا نتمونو قطع نکنن باور نمی‌کنیم جنگ شده</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/4345" target="_blank">📅 21:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4344">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Aro_g0ip--TpVySxu_U1f-tkXaWtf3G7oanpAP6Yzz8kbL849FDWyFiV-5wYUGGPRzXX3taxzRUtcFU4bvMdMqtbqiTSlED-B_y8qQ0722U9k6jCVK49gVv2sL3QkD2LHwejyg6yxmv7uQSRDYOO3KBXZ4tDdY49M1NiS331KFkKmXrYJffeLhVGjf5OPQ0SwnU6brycPn6puezQY6ACZ2tsn9bmf4Zu5JIskBo1_DhHT-U3p6c9iUoG7enXaRtwREkwxHX7Rs1jrlI2cDNjysjROpXa903gCOu53hSFuZ4GyJzQLoLXIuTKn1cMXwTXNWul8wbgncaRfw01p-vlxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
دستیار هوشمند کانال WhiteDNS
👉
@WhiteDnsChatBot
✅
جواب سریع |
✅
۲۴ ساعته |
✅
رایگان
نحوه استفاده:
۱. روی لینک بزنید
۲. Start
۳. سوالتان را بنویسید
مثال: چطور فیلترشکن نصب کنم؟
/search عبارت — جستجوی مستقیم
/contact — ارتباط با ادمین
⚠️
ربات WhiteDNS در چه زمینه‌هایی جواب می‌دهد:
✅
فیلترشکن و VPN
✅
DNS و تنظیمات اینترنت
✅
آموزش نصب اپلیکیشن‌های WhiteDNS
✅
رفع مشکلات اتصال
✅
Warp و Cloudflare
✅
تنظیمات اندروید، آیفون، ویندوز، مک
✅
سوالات مربوط به قطعی اینترنت
❌
ربات قادر به پاسخ‌گویی به سوالات غیرمرتبط با موضوعات کانال نیست.
💡
نکته: اگر جواب دقیق نگرفتید، سوالتان را طور دیگری بنویسید یا از دکمه جستجو استفاده کنید.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/4344" target="_blank">📅 20:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4343">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">ترجیحا هیچ VPNای نخرید دوستان. هیچ تضمینی نیست که اگر اینترنت قطع بشه هم اونا وصل بمونن یا نه. مثل اوایل جنگ که خیلیا اسکم شدن
همون هزینه رو بذارید whitedns راه بندازید</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/4343" target="_blank">📅 16:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4342">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b1d99494e2.mp4?token=CUSEGqhXd9RXEeuKVgWUU8QiwV03WxSRYw6CStJv0haW8pfBMOTgH_Ckh9CKrhZo9PZHRiuKeH3KQ05-lfiWXf7C1upjJgG6YXkIJKWh450rL0XZABI39PvwBjxCMnrk90MoD1WiEgUwZNdoAC6sQoaK58fD6B2DhLcRK2_1Y3GSxR0avVpRen_GY_Gakex-pHixOTRlHeXINofpngjr5nesVdH4fSbu1dB3vxFcgCD6vzPX0WA3hE0Z4etKiwzE8J2ZtZQycFiH2X_iIRQL7Ge2B8S4FY1JaqHqQqbiXWShu9nyxegV7vGFH9bHtpqo5ddRSqsT6RKzqUnRJc8zzA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b1d99494e2.mp4?token=CUSEGqhXd9RXEeuKVgWUU8QiwV03WxSRYw6CStJv0haW8pfBMOTgH_Ckh9CKrhZo9PZHRiuKeH3KQ05-lfiWXf7C1upjJgG6YXkIJKWh450rL0XZABI39PvwBjxCMnrk90MoD1WiEgUwZNdoAC6sQoaK58fD6B2DhLcRK2_1Y3GSxR0avVpRen_GY_Gakex-pHixOTRlHeXINofpngjr5nesVdH4fSbu1dB3vxFcgCD6vzPX0WA3hE0Z4etKiwzE8J2ZtZQycFiH2X_iIRQL7Ge2B8S4FY1JaqHqQqbiXWShu9nyxegV7vGFH9bHtpqo5ddRSqsT6RKzqUnRJc8zzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه مقدار زود شروع شد</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/MatinSenPaii/4342" target="_blank">📅 16:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4341">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/annLS9FK3AhA4pA8tDVXZ-hFURzhvsCSbVN12vIawXZGvlu9bM-XDINW2U2axYYZhz_wuVwDkHSqCYLlPEcJp7s16Vl-Vrc2v3QbUl6IysiJ144gLO3HF7bCsEFwFyK6SiSG1NbuCTPyAgl4n1Ys8zOSgqTB9Dt-fT5yhkU1vbb-QFk6Ef7doef5FVttP7vW9ijhNUxXCt-w_aSglvhOfTWgpXkBCz7WxJhCAbQoKM7j7HiDyD01B5GBksqqE7TftCC32_K2o7rd9bzn1B7DR1iIcAOD8jEh4dOkFP2NYkesUI8ykxjBMY8iZOzMWT3y-b1DXLq8jDA7eBCttLtLnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پارادوکس عجیبیه. از یه طرف انگار جدی جدی جنگ شده باز
از یه طرف اینور دارم آموزش می‌بینم و کار می‌کنم با ai
و نمیدونم همین آب باریکه‌ی نت کی قطع میشه دوباره</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/4341" target="_blank">📅 15:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4340">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">احتمالاً من دچار "فرسودگی LLM" (LLM Burnout) شدم!
نویسنده‌ی این مقاله (الک سکولن) یه توسعه‌دهنده‌ست که می‌گه مصرفش از هوش مصنوعی در حد استانداردهای الان کاملا معمولیه، اما اخیراً یه حس خیلی عجیبی بهش دست داده:
خستگی مفرط از خوندن متن‌های تولید شده توسط هوش مصنوعی!
روند کارش این‌طوری شده که دیگه خودش از صفر کد نمی‌نویسه؛ طراحی می‌کنه، طراحیش رو به Claude یا Codex می‌ده، کدهای اونا رو می‌خونه و ریویو می‌کنه. علاوه بر این، روی پروژه‌ای کار می‌کنه که کدهای تولید شده توسط Qwen رو باید مداوم بررسی کنه. یعنی عملاً کل روزش با خوندن خروجی‌های AI می‌گذره. حتی برای سرچ‌های روزمره‌ش هم از ChatGPT و Gemini استفاده می‌کنه.
حالا مشکل کجاست؟
اعتراف می‌کنه که با این ابزارها خیلی بهره‌ورتر شده و قصد نداره کنارشون بذاره، اما تو چند ماه اخیر، یه بخش کوچیکی از وجودش از دیدن خروجیِ مدل‌ها وحشت داره! چرا؟ چون دقیقاً می‌دونه قراره چی ببینه:
فرضیات غلط، توهمات (Hallucinations)، جملات بریده‌بریده‌ی اغراق‌آمیز، و
✨
استفاده‌ی بیش‌از‌حد از ایموجی‌ها
🚀
.
نکته‌ی جالب اینجاست که می‌گه انسان‌ها هم اشتباه می‌کنن و می‌تونن رو اعصاب باشن، اما مشکلِ اصلی با هوش مصنوعی
تکراری بودنشه
. مدل‌های زبانی دقیقاً با یک لحنِ واحد می‌نویسن و دقیقاً یک‌جور اشتباه می‌کنن. سر و کله زدن با یک سبکِ کاملا یکسان و اشتباهات تکراری، اونم به صورت هر روزه، کلا فرسوده‌ش کرده.
این دقیقاً نشون می‌ده که با وجود تمام شخصی‌سازی‌ها (Personalization) و پرامپت‌ها، هنوز هم اون امضای پنهان و سبک خاصِ هوش مصنوعی از زیر دستمون در میره و وقتی تو طولانی‌مدت باهاش درگیر بشید، می‌تونه حسابی روی مختون بره!
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/MatinSenPaii/4340" target="_blank">📅 14:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4338">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VhSiXerdJobbLpjId5ByOmTs9W887hdjl716yvpeOP1rlJQC1_kP0JvRETuGNTc_mBA3ipjf5Im0I6JiFLuSygS0Zx6HrmZRgsiAbLpQBk1T24HEV5m-St-XNLaGAHQJK3qdREzWEBVK3gAfauJm9bB91DRKSfy9--7scCBfDQV7Fdcsd5BMFb-mEyk3Mo-voHm0BHnoo8ZkbrD6ewxPm9Fo79uRc_Svfw7aQ5anyrSFP8UYLZsk575apYz4A5I_yl__A8sWf2OS2sW5sXk25iwwhjrQPfG4RM_tPq-EuqWeX-wVONizW5f2PAbd6CB19ooTngseorcoRN-4dORcmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/m1Y9JmyHBVC5ekNmkVKKf2T9B-UKK6eUkHljYqaG7T32vJEQwSFcXiIoxjbjIPrQfrq7QQdAJFg3QQSBPyEQ6rcj_uyRWdwcfQTYwPJjZOYo4QwaHSkXPJ5I0abhCEnYg7H2va__ZBs1L7wTwgIl0uuSc2u3iVZpROKXPL90F-mwtvN4V0ZZqNrVxwwPJ5_9xLZ56NaqkIAF74x-LtLrS5zkyB7LEyTx3Z8-fgcc5Z42aXlHcV8ERM-4OSLHE5bc9-dtdBfoV3X7TuqNwAVtDWhuG-UH18ec6U4zjjmzpkScLmtJzsa_kjD7wPU37Kh1QJjmdAl3JKaNcMzNWscMaQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚀
100 میلیون توکن رایگان برای تست مدل‌های جدید AI  مدل‌های زیر را می‌توانید با OpenAI Compatible API استفاده کنید:  • Kimi K2.6 • MiniMax M2.7 • GLM 5.2 FP8  بدون ثبت‌نام، وارد صفحه زیر شوید و از بخش Your API Key کلید خودتان را دریافت کنید:  https://infer…</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/4338" target="_blank">📅 13:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4337">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/784bc3dcd7.mp4?token=LjLYi8poQBkrWYwET9NmavcNbcj3hgzQW5NXbJxu6uljQBjHsQrFR42x1TToxvWrdu2hV--Lf0YxAIDb_PBHMI43Bmi1d9tzOzjIos8b8puyULsDRcZmledNDHHJQ0L8pqDI1J-WCEaz6nJlv_svIYtmg5nVkuVcKXxY5Ea3OG1-DS2cuq4Q2LvkCYaohFz1ruqjOVEUv01McVo5Asvl-QCDB872dhlUiGn4Kz5iifCXjpj6kH_Aemo7EXLk4OmCZNRxaxbYOembgUC26ugypATneijxxr1E9T0vDLZVkLueh0LhIfGkQvS67trbKNzYLcCESf8Ey4Mrbnb_GX-TO3AUeWQoHZFbvTc7R-WkDrcTJppIGiBAxYIX_rDmjl_lvquGRGDDhF2A65rxCoxN1dDH0BoRMeNaofzYfFXP7dT8yasZholq3yVtJ5EmGQrEzBwgxRXZpwJAbo_OoR4SRcJzDsN405SO2uHLpshhdavVHL-Ktjem6kmZ00oF0PvrscxwITTfRO-T4s6mltyg2pGjJXPNR8cByARvH2dAP0ptKRTohERe9PWFyYPk0-ngt03bWSwI8XD-Xyp2y_vgeKg7eVX2y0B0rxYXmWUbT1lH9lh-x8AoLf9rtW8WoEtIl2j9Dw5UIL0EbLrBOddCuvUA7q8BtSwWmnXCdmlRokA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/784bc3dcd7.mp4?token=LjLYi8poQBkrWYwET9NmavcNbcj3hgzQW5NXbJxu6uljQBjHsQrFR42x1TToxvWrdu2hV--Lf0YxAIDb_PBHMI43Bmi1d9tzOzjIos8b8puyULsDRcZmledNDHHJQ0L8pqDI1J-WCEaz6nJlv_svIYtmg5nVkuVcKXxY5Ea3OG1-DS2cuq4Q2LvkCYaohFz1ruqjOVEUv01McVo5Asvl-QCDB872dhlUiGn4Kz5iifCXjpj6kH_Aemo7EXLk4OmCZNRxaxbYOembgUC26ugypATneijxxr1E9T0vDLZVkLueh0LhIfGkQvS67trbKNzYLcCESf8Ey4Mrbnb_GX-TO3AUeWQoHZFbvTc7R-WkDrcTJppIGiBAxYIX_rDmjl_lvquGRGDDhF2A65rxCoxN1dDH0BoRMeNaofzYfFXP7dT8yasZholq3yVtJ5EmGQrEzBwgxRXZpwJAbo_OoR4SRcJzDsN405SO2uHLpshhdavVHL-Ktjem6kmZ00oF0PvrscxwITTfRO-T4s6mltyg2pGjJXPNR8cByARvH2dAP0ptKRTohERe9PWFyYPk0-ngt03bWSwI8XD-Xyp2y_vgeKg7eVX2y0B0rxYXmWUbT1lH9lh-x8AoLf9rtW8WoEtIl2j9Dw5UIL0EbLrBOddCuvUA7q8BtSwWmnXCdmlRokA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت های جالب Amir Hormati مهندس ارشد و پرینسیپال در گوگل در حوزه AI در مورد کدنویسی و Hard Skill ها، اینکه آینده از دید خودش چیه، چه اتفاقی بر سر کدنویسی میاد و به عنوان مهندس نرم افزار روی چه مسائلی تمرکز کنیم، جالب اینکه خود امیر از رول مدیریت به نرم افزار برگشته به خاطر همین!
✍️
Max Shahdoost</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/4337" target="_blank">📅 13:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4336">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">رفقا مجددا می‌گم، که کلا این سایت‌هایی که یهو کلی توکن رایگان میدن، امن به نظر نمی‌رسن مراقب پروژه و .env هاتون باشید</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/4336" target="_blank">📅 13:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4335">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">رفقا مجددا می‌گم، که کلا این سایت‌هایی که یهو کلی توکن رایگان میدن، امن به نظر نمی‌رسن
مراقب پروژه و .env هاتون باشید</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/4335" target="_blank">📅 13:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4334">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجامعه وایب کدینگ ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P56F64hwz2sBHQ7fw2YCuUMhgBsv1YyhiGMgsJonvWMKSeyMFQZR4UhAMRxmOQoD3VmNsIX6gSRk2PHhMaCtJQxKQ0759q1Ykh6V-yBS6Y-V-GJNiPRCov3lQpCmsznhePg7vM-t5tXPYTRaVpaTBwE07e3gRCLyM7d59pm4h3cnImkU8iJ2C0ryWQ7jcd1aOUnqywAaThqjO8SIFCtxpYu4VdQcQt2Y9k38gl9QSk9MnZIpFwO_kzD8_H0yLEWogWLsM3vITNzAHE2ljCppGpDUzJw70a1sT-SCG7Srnuao9F27e0ay_zHxuOw9NkQkOWVjUqIEBgzrFw_644emzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
100 میلیون توکن رایگان برای تست مدل‌های جدید AI
مدل‌های زیر را می‌توانید با OpenAI Compatible API استفاده کنید:
• Kimi K2.6
• MiniMax M2.7
• GLM 5.2 FP8
بدون ثبت‌نام، وارد صفحه زیر شوید و از بخش Your API Key کلید خودتان را دریافت کنید:
https://inference.dahl.global/chatKeys
💡
اگر کوکی مرورگر را پاک کنید، می‌توانید دوباره یک API Key جدید بگیرید.</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/MatinSenPaii/4334" target="_blank">📅 13:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4333">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dADTLjdAt1me3_WPaW7aV_c_k6eIxFcsj1rNSuX_ORxpVkQPQB3q_BYBrB-XHBJT3U08NA689tc6yH1ZWn1VHU2Ri_pd5j0itJ0W_VIpUF6-VejQ3PW3fD1m144LmW9F85T2janfFOoEw_j2rLJkkPveH4LLJNAb2f_c_C0pxzfRgfY8En8UX_6N6QIRu92ZNAa7uLHu3raUiTKFXubHHlbCA34cUinheRx8jLT2uSpMNhzSjG6me6-regLIzQ-9cpq9EUT17XohxR7AY-h1uYe1IbDtaommB8MTpuIAFzPpMRlQD5JrJJh6bGVgl-HbWTIaDhjXvuxj2OC6-n3IXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چیزی نیست، کامیونیتی Rust هستن
😂
😂
زبان Rust برخلاف go و پایتون و... از Garbage collector برخوردار نیست.
نفر اول گفته انقدر سینتکس افتضاحه که دلم می‌خواد زبان rust رو بندازم توی آشغالا(garbage) و نفر دوم ریپلای زده که اگه بندازیش توی آشغالا کسی نیست جمعش کنه چون این زبان آشغال جمع‌کن(garbage collector) نداره</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/4333" target="_blank">📅 12:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4332">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">اگر می‌خواید اکانت Claude بخرید، بهتره بدونید علت بن کردن‌های کلاد distillation attack هایی هست که اخیرا بهش شده؛ و حتی کاربرهای خارجی هم یهو اکانتاشون بن شده. بهتون دوتا توصیه می‌کنم.
1- به هیچ وجه از سایت‌های ایرانی نخرید. و حتما بدید دوستی، آشنایی، چیزی بگیره از خارج کشور. اگر ندارید، برید سراغ توصیه‌ی دوم. احتمال بن شدن داره به هر حال و ریسکش پای خودتونه. من خودم به شخصه هنوز بن نشدم(نمیدونم شانسه، یا چون دوستم از خارج از کشور واسم گرفت)
2- اشتراک Codex بگیرید در عوض و یا نهایتا اگر کار خیلی واجب دارید و می‌خواید حتما کلاد باشه، cursor بگیرید اما کرسر خیلی زود تموم میشه طبق تجربه‌ی شخصی. به نظرم Codex سخاوتمندانه‌تره به شدت. و صبر کنید تا وقتی که بن شدناشون شدتش کمتر بشه.</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/MatinSenPaii/4332" target="_blank">📅 21:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4331">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">نشت مخفیانه‌ی دیتا از ریپازیتوری‌های پرایوت گیت‌هاب با یه ترفند ساده‌ی هوش مصنوعی
📚
فکر کنید یه نفر بدون هیچ پسورد و دسترسی‌ای، بتونه کدهای مخفیانه‌تون رو توی گیت‌هاب بخونه. چطوری؟ با گول زدن ایجنت هوش مصنوعیِ خود گیت‌هاب!
تیم Noma Labs یه آسیب‌پذیری خیلی خطرناک (به اسم GitLost) توی سیستم جدید Agentic Workflows گیت‌هاب پیدا کرده. داستان از این قراره که این ایجنت‌ها می‌تونن issueها رو بخونن و اتوماسیون انجام بدن.
🫵
حالا هکرها چیکار می‌تونن بکنن؟
هکر کافیه بیاد تو یکی از ریپازیتوری‌های پابلیک شما یه Issue باز کنه و توش یه سری دستور مخفیانه به زبان انگلیسی (Prompt Injection) قایم کنه.
ایجنت گیت‌هاب این متن رو می‌خونه، گول می‌خوره و به جای کار اصلیش، میره فایل‌ها و دیتای ریپازیتوری‌های پرایوتِ همون سازمان رو می‌خونه و برای هکر می‌فرسته!
نکته‌ی جالب اینجاست:
گیت‌هاب کلی گاردریل امنیتی چیده بود که دقیقاً جلوی همین اتفاق رو بگیره. اما محقق‌ها فهمیدن فقط با اضافه کردن کلمه‌ی "Additionally" (به‌علاوه/همچنین) توی پرامپت هک، مدل هوش مصنوعی کلا گیج می‌شه و به جای اینکه درخواست رو رد کنه، تمام محدودیت‌ها رو دور می‌زنه و دیتا رو لو میده.
این دقیقاً نشون میده که توی سیستم‌های جدید هوش مصنوعی، همون متنی که ایجنت می‌خونه همزمان می‌تونه پاشنه آشیل و نقطه حمله باشه. حملات Prompt Injection الان دقیقاً دارن همون بلایی رو سر AI میارن که قبلاً SQL Injection سر وب‌سایت‌ها میاورد.
البته این باگ به طور مسئولانه به گیت‌هاب گزارش شده، ولی حواستون به ایجنت‌هایی که به سورس‌کدهاتون دسترسی دارن باشه!
منبع:
https://noma.security/blog/gitlost-how-we-tricked-githubs-ai-agent-into-leaking-private-repos
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/MatinSenPaii/4331" target="_blank">📅 19:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4330">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">یکی از چیزایی که راجب کامیونیتی فارسی باحاله و دوست دارم، اینه که زیاد توی کامنت‌ها با هم در ارتباطیم. کامیونیتی خارجی، این شکلیه که ویدئوی تکنیکال می‌ذارن، 60 کا ویو میخوره اما کلا 25 تا کامنت میگیره. یوتوبره اون 25 تا کامنت رو حتی لایک هم نمیکنه. اما کامیونیتی فارسی، ویدئوی 10 کایی کم کمش 200 تا کامنت رو میگیره و خیلی از یوتوبرا هم جواب میدن و اهمیت میدن</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/MatinSenPaii/4330" target="_blank">📅 16:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4329">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">☠️
ساخت رادار پیامکی با Hermes Agent بدون کدنویسی + API رایگان OpenCode
⚡️
دستورات نصب OpenCode برای ویندوز، سرور لینوکس و دیگر سیستم‌عامل‌ها: https://t.me/MatinSenPaii/4259
⭐️
توی این ویدئو: 1- باهاتون راجب کسب درآمد از Hermes صحبت می‌کنم 2- با همدیگه…</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/MatinSenPaii/4329" target="_blank">📅 16:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4328">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VPk1E0fICVPA6ODCQdgZbsUM2X3uwccnCb1msttC_VF9Wzkn1_YLxgFDRS5HDaInOdhn2tga7pqodhOOxjryDS5QTLUXJLg42h0I29Etw_Gr4QYi-anKl23EkPS_SgkvmmOpICqLTdJW52DXxSSWM2QiYJ9VwCGhB2ojd2SohzTGHY0wnQ3Aa-Xv1PxkTgfeKiRpG5E5j0R_SMG1pUpNknsIEvntRTBkBM0an6IoB3sOT0IMt-ix_tdLgwp7zJGPTyn4OyCJPw0syYsGa4MyqU1DwTDfNdBEamFH5HUa5Oa4XYDy1z52Q18gxjXiHqin1C6DOSiqDdiyJeTEsdBpWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
ساخت رادار پیامکی با Hermes Agent بدون کدنویسی + API رایگان OpenCode
⚡️
دستورات نصب OpenCode برای ویندوز، سرور لینوکس و دیگر سیستم‌عامل‌ها:
https://t.me/MatinSenPaii/4259
⭐️
توی این ویدئو:
1- باهاتون راجب کسب درآمد از Hermes صحبت می‌کنم
2- با همدیگه OpenCode رو به 9Router وصل میکنیم و روش دور زدن یه باگ خیلی رو اعصاب رو بهتون میگم
3- از هرمس استفاده میکنیم که با سامانه پیامکی، یه کرون جاب بنویسیم(قابل پیاده‌سازی برای هر ایده‌ای)
4- و کار با پنل‌های پیامکی رو بهتون یاد میدم
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل ساده‌ست و نیاز به پیش‌نیاز خاصی نداره. از api رایگان هم استفاده شده توی کل ویدئو
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/MatinSenPaii/4328" target="_blank">📅 15:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4327">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Zombie</div>
  <div class="tg-doc-extra">Bad Wolves</div>
</div>
<a href="https://t.me/MatinSenPaii/4327" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/4327" target="_blank">📅 15:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4326">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">خب انگار فعلا خبری نیست
نت منم اوکی شدش</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/4326" target="_blank">📅 13:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4325">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4325" target="_blank">📅 12:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4324">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHaoodi Senpai</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a627c5c6e.mp4?token=MvzgoBW7lrmW4yhU561l7t3Nz9dwdUZotvWty0KbiIJBvHDmWWeQph19U3ERzUT-I-wWE_K49R3b-s4lSclQFOJgHhZAdrJgkqM1cRoaQkUvYSJdBFM0IRmnnMdwT-ZcMVVrGOqGN9Q868NQwZ-XIRvYycVqd0XlZTbK7xQ-75tGMIsrTkESOQ7iF5klQF0BdNkke-cNssK1L4KF7pVnhNa3WV7x795dXrMOnBmAkPdLeXoKytH26i7NH9P0wpJ8R94bBwUESvgFRkBQuV10gm1BOkBDsY_iJLYrdpxdt4vASZbta5Msd3rWwPBMCykETKGZU35N4tjor5fJ-EYYig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a627c5c6e.mp4?token=MvzgoBW7lrmW4yhU561l7t3Nz9dwdUZotvWty0KbiIJBvHDmWWeQph19U3ERzUT-I-wWE_K49R3b-s4lSclQFOJgHhZAdrJgkqM1cRoaQkUvYSJdBFM0IRmnnMdwT-ZcMVVrGOqGN9Q868NQwZ-XIRvYycVqd0XlZTbK7xQ-75tGMIsrTkESOQ7iF5klQF0BdNkke-cNssK1L4KF7pVnhNa3WV7x795dXrMOnBmAkPdLeXoKytH26i7NH9P0wpJ8R94bBwUESvgFRkBQuV10gm1BOkBDsY_iJLYrdpxdt4vASZbta5Msd3rWwPBMCykETKGZU35N4tjor5fJ-EYYig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">The Return of
قدرت مذاکره</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/MatinSenPaii/4324" target="_blank">📅 12:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4323">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/4323" target="_blank">📅 12:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4322">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">مشکلی در وجودشان وجود دارد. آنها دیوانه هستند.</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/4322" target="_blank">📅 12:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4321">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">روی اینترنتای خود من به شدت اختلال هست
همراه اول که به زور چیزی باز میکنه
ایرانسل 4g+ اما هیچی به هیچی. آپلود 0
فیبر مخابرات هم از صبح 2 دقیقه وصله 20 دقیقه قطعه</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/4321" target="_blank">📅 11:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4320">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">نسخه‌های اندروید(اگر نمیدونید کدومه برای پردازندتون، Universal رو دانلود کنید)</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/4320" target="_blank">📅 11:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4319">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">💬
آموزش قدم به قدم استفاده از اپ CoreForge  https://youtu.be/filwdiPKN90</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/4319" target="_blank">📅 11:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4318">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">💬
آموزش قدم به قدم استفاده از اپ CoreForge
https://youtu.be/filwdiPKN90</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/4318" target="_blank">📅 11:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4312">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.5.1-arm64-v8a.apk</div>
  <div class="tg-doc-extra">5.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4312" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/4312" target="_blank">📅 11:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4311">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">آخرین نسخه‌های مک-ویندوز-لینوکس</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/4311" target="_blank">📅 11:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4303">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.0.0-beta5-macos-amd64.zip</div>
  <div class="tg-doc-extra">27.2 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4303" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🐧
نسخه لینوکس</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/4303" target="_blank">📅 11:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4302">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mhwFJVwwRVtc3TWm5Fo01UhAOMQHjQnlxaPLCfxrw_KNa3RHL50XhSaQO0DWuxvZaQWV6l8nGVwUIe23IjsDT5eKpI8WFUb1QpTIvub9fQRyKz5kmvTjX-bUA_t04Hu9qWY1nDfxHJltOpKScUShf-6DZ1P257ddL5KJN6U3vi1tdjUY-pUOtKSQ-OGhK5e3NT_YuoiaJwsWNCaSaao2bOtXm4fL-ivwIt-WG_OI7hpvIiKrsgI6KBDrlAEyLKgDFhfToLI7r5I9lX2QAj8Kqrx92aoCOrvfP3Ww-ozi-pU1w1rPnZUumAYIZgz6Zg3hNxP9dzNpySd0ylOz0skuEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق معمول، پیشنهاد میکنم WhiteDNS رو راه‌اندازی کنید برای خودتون و دوستانتون
آموزش:
https://youtu.be/6Pm7kNQb3mo</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/4302" target="_blank">📅 11:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4301">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">اعصاب و روان نموند برامون. نمیدونیم درس بخونیم، کار کنیم، کارگری کنیم، لپ تاپو بفروشیم و دلال بشیم که بتونیم زندگی کنیم، چیکار کنیم</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/4301" target="_blank">📅 11:08 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-4300">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">میترسم پنج دقیقه بخوابم ببینم نت قطع شده باز</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/4300" target="_blank">📅 11:07 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
