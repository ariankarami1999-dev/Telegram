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
<img src="https://cdn4.telesco.pe/file/VWEoZD662VwS5MFA_hdjxbyFzA64jvPeUQxmYjezodCWXIgnK3yNoMpnXAIXsS-USRWlql7-8xSr_EO5TOX9UDLMv8KznbrryFCSHsP_8RBAN3x_KU43GhVufbvbmD6UkSZa6VvTWEYlEZ4QrCZe5NJsVhaoAN7XEvcHsbDpwPZPKXkdMFuUGu0vSxc7pZRtj11SvZiMP-KjfXM7Dm6viNc60YJ3IQAnfwDd_ecO3YdaANLFgvGQ7Ih_3RY3WGsLIdFvWvG5VjdJuywk48_6TJy8rLRKqePBmYJUl9dWa-CWWeFMajSg8COlY1NaGuRlG1Gk21Ef9lUgVzgvqz51rA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 112K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-15 00:05:49</div>
<hr>

<div class="tg-post" id="msg-71161">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a02f1d06a.mp4?token=Iq7Fq64UmkQ0kMHXXmByWltp5XaNcbfx7ZG9uSliOkmTwR_ijztkXQkE24oVOREZQkAGkeCfVmcC0fStT0C3f6I6N8CvZwScJ5FbyF3mjQB-ANpffvcbzIoWbfmNzv083tUq8MxF0oriy3fd7e4qQxtaNEps4YvkhCsMEojmIj8xYv6Q_4Jy-uXZfCF--9I6PGpO7VnPB1Dou0FsG70iEtIGUTbyxozdejfzSbD6Nt0YbPkh-DmFwA9QJw0948MhWgS5w3-LHv0i8A-O_qKma4Ov9YhVQ91SWPC4sBwm-igkoBtlABVKDiqLBsE0OZUzyDYAXjOK13fRSMTY2wGghg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a02f1d06a.mp4?token=Iq7Fq64UmkQ0kMHXXmByWltp5XaNcbfx7ZG9uSliOkmTwR_ijztkXQkE24oVOREZQkAGkeCfVmcC0fStT0C3f6I6N8CvZwScJ5FbyF3mjQB-ANpffvcbzIoWbfmNzv083tUq8MxF0oriy3fd7e4qQxtaNEps4YvkhCsMEojmIj8xYv6Q_4Jy-uXZfCF--9I6PGpO7VnPB1Dou0FsG70iEtIGUTbyxozdejfzSbD6Nt0YbPkh-DmFwA9QJw0948MhWgS5w3-LHv0i8A-O_qKma4Ov9YhVQ91SWPC4sBwm-igkoBtlABVKDiqLBsE0OZUzyDYAXjOK13fRSMTY2wGghg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
یه خانم درباره اقتصاد:
چرا مردم هر چی گرون میشه از زاویه ی آدمای متوسط بهش نگاه می‌کنن؟
خونه از ۵ میلیارد شده ۵۰ میلیارد.
گوشت از ۵۰۰ تومن شده ۴ میلیون.
سود شما چند برابر شده.
مردم از گرونیا دارن سود میکنن، مردم باید دیدگاهشون از آدمای متوسط جامعه تغییر بدن و بگن هر چی گرون میشه خب ما هم سودمونو داریم میبریم
@News_Hut</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/news_hut/71161" target="_blank">📅 23:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71160">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2d7d2ec60.mp4?token=D69wJ-q8Fw3VSn7Un9kYrHjKeKcKIFfqtO8r01PuheA--ICQi9Z1dlMpmdEGaYzJ-aPNJCMEUH0bVy9RHMlf_VVbsrkQVKs0JF9bWdhbyZF9sVqnqiNwFcvOilHiUUpLCYVK09dKQbVvIzzdLurc81lP8ZSNYTcsRnNKj56EPnRWb0iQW8UjUH4JPhj-IKfX_4fqA7MPa78N_Dp_bWB_6xRX75OUaHL-SgVm-g4vjvlCDUot3Dw2G7PWORseXb3fOjqJggf-L2NZq_a_-IVx4_g45vJ4y10Pd0d0dfN9f6Iz_eMkQnqWrqA5SH3C8v5ulNpVODUVtFHCLUrmdS7AMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2d7d2ec60.mp4?token=D69wJ-q8Fw3VSn7Un9kYrHjKeKcKIFfqtO8r01PuheA--ICQi9Z1dlMpmdEGaYzJ-aPNJCMEUH0bVy9RHMlf_VVbsrkQVKs0JF9bWdhbyZF9sVqnqiNwFcvOilHiUUpLCYVK09dKQbVvIzzdLurc81lP8ZSNYTcsRnNKj56EPnRWb0iQW8UjUH4JPhj-IKfX_4fqA7MPa78N_Dp_bWB_6xRX75OUaHL-SgVm-g4vjvlCDUot3Dw2G7PWORseXb3fOjqJggf-L2NZq_a_-IVx4_g45vJ4y10Pd0d0dfN9f6Iz_eMkQnqWrqA5SH3C8v5ulNpVODUVtFHCLUrmdS7AMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه جانفدای رندوم و حرکات جالبش
😃
@News_Hut</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/news_hut/71160" target="_blank">📅 22:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71159">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66b1ca1096.mp4?token=oTRxhW8TjL_5urHyaUGgfJ11fFqkJYVADUc9w1AaFD1gIKa65gqM294tYe27lnhfGh1v0FNzYDX25wJUgur1jwfys0zGmXJsVszfpk3ft8gEre8pKG6RDLbKkIZ-5lhLCMAj_nsFUSbj76YBuXFrIkKsTwMh07cE3mU5DFhg9ExuVysZIBYpuMeABNxupRpcpiTLYoxo8XHQCNvNzT-PDdJGcO_mfTNZNdz1Jwd-vOip256wkdRbSWD7pOXCHextqtvZaAy7jEhxgjtyL-Kqx1v1BQiyF7W-d-ueHHkZ3L50RA4sBqVy-WGNFWxGqPfUKOXd9Vtq4XIh427-WdXFVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66b1ca1096.mp4?token=oTRxhW8TjL_5urHyaUGgfJ11fFqkJYVADUc9w1AaFD1gIKa65gqM294tYe27lnhfGh1v0FNzYDX25wJUgur1jwfys0zGmXJsVszfpk3ft8gEre8pKG6RDLbKkIZ-5lhLCMAj_nsFUSbj76YBuXFrIkKsTwMh07cE3mU5DFhg9ExuVysZIBYpuMeABNxupRpcpiTLYoxo8XHQCNvNzT-PDdJGcO_mfTNZNdz1Jwd-vOip256wkdRbSWD7pOXCHextqtvZaAy7jEhxgjtyL-Kqx1v1BQiyF7W-d-ueHHkZ3L50RA4sBqVy-WGNFWxGqPfUKOXd9Vtq4XIh427-WdXFVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعاتی پیش تو مسیر پلیس‌راه همدان ـ سنندج، یه ماشین سنگین گویا ترمز می‌بره و مستقیم با یه دستگاه تانکر حامل سوخت برخورد می‌کنه و یه انفجار وحشتناک رخ میده!
متاسفانه تا الان 7  جونشون رو از دست دادن...
@News_Hut</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/71159" target="_blank">📅 22:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71158">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3aea156fe3.mp4?token=lk5E_IDwb9GAwUbVVtUaSzd45E8t7xReF-39ErZiezV9jS1rK8lu-cPApxS4aedU2UlXYzMGiP_9e0yiYCHW5_fyd4Kpg3oc6N_-SSr8TGe9HGUA_c40P3Mcvu5H75BcebMtWzHPJoaHxFDPHp6jQ3lAWMk3UZD0qBEtDgce2EGcRJmQP4bzta0DgsZ0sVPdpuHfwgc0LJ4KUgLOb9t5PnUmMp8PxPs4zgfQh_nXnY6FtW_P3mkYbG7M28f8TjCEPCFPwD9B3BV7oFQo5FQmcGAWlPSniDFpypuWOkQCjmwWknIl7e9Up4X6745fRdNV3sCSnBGIrqhtVzCSOLYrJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3aea156fe3.mp4?token=lk5E_IDwb9GAwUbVVtUaSzd45E8t7xReF-39ErZiezV9jS1rK8lu-cPApxS4aedU2UlXYzMGiP_9e0yiYCHW5_fyd4Kpg3oc6N_-SSr8TGe9HGUA_c40P3Mcvu5H75BcebMtWzHPJoaHxFDPHp6jQ3lAWMk3UZD0qBEtDgce2EGcRJmQP4bzta0DgsZ0sVPdpuHfwgc0LJ4KUgLOb9t5PnUmMp8PxPs4zgfQh_nXnY6FtW_P3mkYbG7M28f8TjCEPCFPwD9B3BV7oFQo5FQmcGAWlPSniDFpypuWOkQCjmwWknIl7e9Up4X6745fRdNV3sCSnBGIrqhtVzCSOLYrJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
وزیر نیرو:
دیگر قطعی برق برنامه‌ریزی‌شده نداریم
اگر مردم جایی دیدند به سامانهٔ ۱۲۱ اطلاع دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/71158" target="_blank">📅 21:42 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71157">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31160c5df1.mp4?token=tWPfe6rbBjGHosUP_fK94Sf0cMj6mOhmzVGjRqNKIenGiHx8Jcfo_R1Pm21p9HGdFnnvvEL7SwNSOerexpKPlt7-YaF8y7MgWgroeNNWVNwzh6w1u1ccFHYCp_V-Nqs8O1Lz0pa6qmwW39BSv1qfiYxSzUI0RCx5h_WWGOltHXZYRlXsqHniXdRfREfDFd7kLpySxczF0tkIHHGatr3POAY_NqS6xKhm8sqxCZrz-4ufrh9BAdL3IR5YJ0foWaKOVgXEEaQifIR0tR0HNGUGDeJnKV6j9gaBn8_6siSdpLqQqvHVY2I9Ywc1pzS8FLa_m74tWxcY6lnUhOj4-oluh4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31160c5df1.mp4?token=tWPfe6rbBjGHosUP_fK94Sf0cMj6mOhmzVGjRqNKIenGiHx8Jcfo_R1Pm21p9HGdFnnvvEL7SwNSOerexpKPlt7-YaF8y7MgWgroeNNWVNwzh6w1u1ccFHYCp_V-Nqs8O1Lz0pa6qmwW39BSv1qfiYxSzUI0RCx5h_WWGOltHXZYRlXsqHniXdRfREfDFd7kLpySxczF0tkIHHGatr3POAY_NqS6xKhm8sqxCZrz-4ufrh9BAdL3IR5YJ0foWaKOVgXEEaQifIR0tR0HNGUGDeJnKV6j9gaBn8_6siSdpLqQqvHVY2I9Ywc1pzS8FLa_m74tWxcY6lnUhOj4-oluh4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
جان بولتون دیپلمات آمریکایی درباره ایران:
من معتقدم — و دهه‌هاست که چنین نظری دارم — که تنها راه دستیابی به صلح و امنیت واقعی و پایدار در خاورمیانه، خلاص شدن از شر رژیم تهران است.
به گمانم حملات آمریکا و اسرائیل آسیب قابل‌توجهی به این رژیم وارد کرد.
بی‌شک ما اشتباهات زیادی مرتکب شدیم.
اما اگر اراده کنیم که درباره چگونگی انجام آن به‌درستی بیندیشیم، این هدف همچنان قابل‌تحقق است.
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/71157" target="_blank">📅 21:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71156">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
صداوسیما:
صدای انفجار هایی که در جزیره قشم شنیده شده مربوط به شلیک موشک ها به سمت شناور های متخلف در تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/71156" target="_blank">📅 21:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71155">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed43299c5.mp4?token=oBr358PUQFuOQXfstTrQVLnKAoyd8yod_acL8oc7GEFx7cXfrif0icxVCc8CsiDo8zzpQE8fN62PBGPwVl892_U9j0xVLdW5WaBzRCg_9GjxvYuUXJ50OvAAByEGLI_-tqN_9YumPg4XUAocS_kghG_Qobvgcch9eb2qdbugqYtzrRlZqDM98gTt6453zSJsmT6vt4fFZn1uypPD7liieRW_7SWh5oOtr2CJ0q5IBk2tbkPEMB21pxrGVxUMM_YIsDHRQHxyz85lRtlkQPS3wqOqXUJh5Wni36FQ4uXcIXx8TZScEilcm_vp2RMYYAA5g4IiICZN34dUQW_arcdpnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed43299c5.mp4?token=oBr358PUQFuOQXfstTrQVLnKAoyd8yod_acL8oc7GEFx7cXfrif0icxVCc8CsiDo8zzpQE8fN62PBGPwVl892_U9j0xVLdW5WaBzRCg_9GjxvYuUXJ50OvAAByEGLI_-tqN_9YumPg4XUAocS_kghG_Qobvgcch9eb2qdbugqYtzrRlZqDM98gTt6453zSJsmT6vt4fFZn1uypPD7liieRW_7SWh5oOtr2CJ0q5IBk2tbkPEMB21pxrGVxUMM_YIsDHRQHxyz85lRtlkQPS3wqOqXUJh5Wni36FQ4uXcIXx8TZScEilcm_vp2RMYYAA5g4IiICZN34dUQW_arcdpnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
تصاویر منتشرشده نشان می‌دهد یک کشتی کانتینربر در اسکله بوشهر تقریبا به‌طور کامل نابود شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/71155" target="_blank">📅 20:33 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71154">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
سازمان تجارت دریایی بریتانیا UKMTO:
گزارش‌ هایی مبنی بر وقوع حوادث برای چندین کشتی تجاری در شمال خلیج فارس و دریای عمان دریافت کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/71154" target="_blank">📅 19:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71153">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5717843ac.mp4?token=JdW_NiouVEv1HbWPXn4Yjw3yTJBUiqX_nbfUKWb-aNuNQD2wkfcbXN_fnS-n6Ao9j7fK6h3bs6y6c3gtBhimSpktaroPchrH2wfarYi32JcZOR7Fw8W6fljm0ughkm3n-PBwiffnigU4LdOHgECX7tgeRl3wvVStnPfI5eZxGW8M4Xw5WXotErbhLLUe9UppDzVRtTzZrj8neEaVeOGvl3dgr8r8zm1zoejc-c-PLs1vSxWCt6kBOUh9r_-qFAe9gpNexq8GvWRNx5iNt754zNbZFDucpW8hSQhwQBPGMov_87Va1uyb9GLJSB7Aa9QV0boI5ZzihT2i16fAJ90k5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5717843ac.mp4?token=JdW_NiouVEv1HbWPXn4Yjw3yTJBUiqX_nbfUKWb-aNuNQD2wkfcbXN_fnS-n6Ao9j7fK6h3bs6y6c3gtBhimSpktaroPchrH2wfarYi32JcZOR7Fw8W6fljm0ughkm3n-PBwiffnigU4LdOHgECX7tgeRl3wvVStnPfI5eZxGW8M4Xw5WXotErbhLLUe9UppDzVRtTzZrj8neEaVeOGvl3dgr8r8zm1zoejc-c-PLs1vSxWCt6kBOUh9r_-qFAe9gpNexq8GvWRNx5iNt754zNbZFDucpW8hSQhwQBPGMov_87Va1uyb9GLJSB7Aa9QV0boI5ZzihT2i16fAJ90k5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
✈️
ویدیویی تایید نشده از پرواز تانکر سوخت‌رسان آمریکایی به همراه دو جنگنده در آسمان جزیره کیش استان هرمزگان
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/71153" target="_blank">📅 19:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71152">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71152" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/71152" target="_blank">📅 19:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71151">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvB66GpBm_0KGBOP_TTTh810aGyYCK7MwcqvdzdxSUFc0yolqg78pP5QLmSFNMkvb757ZZglTmoPr6CVdaHnCNgkXAw7jQd7HcGobANFJ2oqg6idKnXNJ0lqKQkxZJqsXxICla4TROUftMIwLOONIZB9VgqyQEtofNQSW9o_pQusVsSNM1vAvP1baG8oJIe-IheqPC-m97_ctV1-4ayfCFg0AYo4t33x8fImDx_m65m_GBV0hUslokSDDDHC6epKE80jFpUcsgFYfWiUqvnRG_BjgV842qoCGKVLAKjFjxsdCYqJZ3BELoBYqwQmDBj9pswzobuwuEUOqUgH1p8N0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب اینتر
🆚
ناپولی را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید.
📊
نگاهی به آمار دو تیم:
اینتر: ۲ بازی ۲ برد و کسب و ۵ گل زده
ناپولی: ۲ بازی ۱ برد و ۱ شکست و ۳ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/71151" target="_blank">📅 19:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71150">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf5e996b2c.mp4?token=XHWz1HKb5EMG_fuM8ITquJb7UvtezAZ4hOodH6C7Wh2W9FIC3DWfp1soXXL1SBb5eElOsegi_91rWpRVGQb2_4M06dNRTn8alqsD2Mj6RV68f7r9hkqJVb9HFFwPeWTrcJfzE-BvKHWMsy2Sg7jBEI8h428utxZ-VY0QOGX-5rPlhhl09uyPh7sr_J1ZdJ3d-KjQm43phjO2LKFMrWy__ocp20r8HIDsPb9AcERJ4EW-n-dIlaM9basA4BShKbVHlbTvAkZKHiYeHh9YkBiZieAFVtd4vt8w3Wyj1_ItXBEDMoOhNvVuZ2vQOw3XA9qpv1rfNRG_Wy82hsFjsD5DIabtEMzXjJ7g9CkljDDu7XZTfRiWttQfevWnl7OWAcV3irAcIA93fcJYeuVZtD27IPpIahvmGwFoxz0wFdu3HO3VMYtOiEAqzmRvWvq-Lo-9rE03JuhEJP9erWwiLGpb36obQVQ4O5LBu_pAe3-m9660gAFL1nsj-t4wIbIbn3z3fpDKiEruJ4boNVcLm0ZJ4BTtaLx2PoXHO9QBBlEBDGTePZLSOc_vc5wqmComddgGyHQvKWRVfJfgted5DQ5wq1t9g5AQl2M10txyLRmdfC2hqcbF7W5moZhcjlXsQvc6uJW-Rmq4qEJ9LDrIoSCJFFQiUP7dhjb6buY1lUVJ3-s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf5e996b2c.mp4?token=XHWz1HKb5EMG_fuM8ITquJb7UvtezAZ4hOodH6C7Wh2W9FIC3DWfp1soXXL1SBb5eElOsegi_91rWpRVGQb2_4M06dNRTn8alqsD2Mj6RV68f7r9hkqJVb9HFFwPeWTrcJfzE-BvKHWMsy2Sg7jBEI8h428utxZ-VY0QOGX-5rPlhhl09uyPh7sr_J1ZdJ3d-KjQm43phjO2LKFMrWy__ocp20r8HIDsPb9AcERJ4EW-n-dIlaM9basA4BShKbVHlbTvAkZKHiYeHh9YkBiZieAFVtd4vt8w3Wyj1_ItXBEDMoOhNvVuZ2vQOw3XA9qpv1rfNRG_Wy82hsFjsD5DIabtEMzXjJ7g9CkljDDu7XZTfRiWttQfevWnl7OWAcV3irAcIA93fcJYeuVZtD27IPpIahvmGwFoxz0wFdu3HO3VMYtOiEAqzmRvWvq-Lo-9rE03JuhEJP9erWwiLGpb36obQVQ4O5LBu_pAe3-m9660gAFL1nsj-t4wIbIbn3z3fpDKiEruJ4boNVcLm0ZJ4BTtaLx2PoXHO9QBBlEBDGTePZLSOc_vc5wqmComddgGyHQvKWRVfJfgted5DQ5wq1t9g5AQl2M10txyLRmdfC2hqcbF7W5moZhcjlXsQvc6uJW-Rmq4qEJ9LDrIoSCJFFQiUP7dhjb6buY1lUVJ3-s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
لحظه تهدید تخلیه خدمه نفتکش های جمهوری اسلامی توسط خلبان جنگنده ارتش آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/71150" target="_blank">📅 18:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71149">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
〰️
⭕️
سنتکام مسئولیت حمله به نفتکش های ایرانی را گردن گرفت؛  پس از شلیک موشک‌های بالستیک سپاه به سمت دو ناو جنگی آمریکا، نیروهای آمریکایی ۳ نفتکش حامل نفت خام ایران را هدف قرار داده و از کار انداختند. دو نفتکش نزدیک خارک و جاسک هدف قرار گرفتند و یک نفتکش دیگر…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/71149" target="_blank">📅 18:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71148">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xbr2CZ5Ddlf02ZDHva5FKd9thSeJi7bIFDtVM_Lvec4FSE6q7ybNSKfAXXda9nemcxNkltUnyMWbfW-szw97U9iQ9XC5Ew0gwkeyNw_jimKqYVe0icuXino_4SrWVj0NlpygSGAR8mgEAWwIqfN0IS4MHXJa7mwFY2tLFP_Y1VFU6gJabMP2sA6C-LOo0vIo4KgZQHiEYvuLi6oVhekAv1lNl7asVCcEpNwVe0w42j0twabcES1uiK9MKhNeVof8PkxHNApHvCZS4lc3KOPZ7KXKmVNiBHDHC8N8A7WHgXpVo4JBQ_vs7jTvTM6FknGDsVfMGPDUhL48N7NQnLV10A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
🇧🇭
سفارت ایالات متحده در بحرین:
با توجه به تنش‌ها در خاورمیانه، وضعیت امنیتی همچنان پیچیده است و احتمال تشدید غیرمنتظره اوضاع وجود دارد.
سفارت ایالات متحده به شهروندان آمریکایی یادآوری می‌کند که ایران پیش‌تر زیرساخت‌های غیرنظامی در بحرین، از جمله هتل‌های منامه، را هدف قرار داده است.
آمریکایی‌هایی که در حال حاضر در خاورمیانه حضور دارند، باید هوشیاری خود را افزایش دهند و نسبت به احتمال لغو پروازها، بسته شدن حریم هوایی و اختلال در سفرها آگاه باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/71148" target="_blank">📅 18:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71147">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1d8dfb05eb.mp4?token=eb1CqUcYxditAcuj-p3wEinA9myZoMYd6x86sqwcZSHWnGqpJXDqSlRU_89XduvIXoxRphhhaYcV8GtLxqjlD8jxVuJGm_AFgCgv95FzH1Bj5lX7_TGfLSrFVPQlhss_c6NHILDdRJd3WdURuJuzXbjksKAWrTH4UHVd5-6pma62gGiaWQpin5xjwiIhrtvouMaxqTyM6mCNFZAIpKtEW1GDjOwBWTFbS4YBeE06dpxAeWIpQum7dnCuyl80XH7-ZgyF9iC38UoQAYsAg4eeRE-_G_KMflTTjfBG0HPBPGDZkrOM5HfKGJzXo2_k7QZvY3NZKGGEsafBVBCvH7o33g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1d8dfb05eb.mp4?token=eb1CqUcYxditAcuj-p3wEinA9myZoMYd6x86sqwcZSHWnGqpJXDqSlRU_89XduvIXoxRphhhaYcV8GtLxqjlD8jxVuJGm_AFgCgv95FzH1Bj5lX7_TGfLSrFVPQlhss_c6NHILDdRJd3WdURuJuzXbjksKAWrTH4UHVd5-6pma62gGiaWQpin5xjwiIhrtvouMaxqTyM6mCNFZAIpKtEW1GDjOwBWTFbS4YBeE06dpxAeWIpQum7dnCuyl80XH7-ZgyF9iC38UoQAYsAg4eeRE-_G_KMflTTjfBG0HPBPGDZkrOM5HfKGJzXo2_k7QZvY3NZKGGEsafBVBCvH7o33g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
〰️
⭕️
سنتکام مسئولیت حمله به نفتکش های ایرانی را گردن گرفت؛
پس از شلیک موشک‌های بالستیک سپاه به سمت دو ناو جنگی آمریکا، نیروهای آمریکایی ۳ نفتکش حامل نفت خام ایران را هدف قرار داده و از کار انداختند.
دو نفتکش نزدیک خارک و جاسک هدف قرار گرفتند و یک نفتکش دیگر در دریای عمان منهدم شد.
سنتکام اعلام کرد این نفتکش‌ها بخشی از شبکه تأمین مالی سپاه و نیروهای نیابتی آن بوده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/71147" target="_blank">📅 17:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71146">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c865776e9.mp4?token=QpXFm4UPfh-a1VgO4pG6BnZG-8O0wovr9JM9OzG_FK7p_xz6t_gcOsOTGTV6Q2lzxBSWSv1PsZNtiDQkkXjYlkuHgYhc_twImHH9-ZhHPS3PygMvhc4-ZPgmDmiLe3Cyypsc_Sx_7054i1WdavF_Pm4EnG49--YeagPy2yJIqQ2HvhVCxD1jnUYDoftlPaX8Cehx1SOt7Ktw7ghXsDmBtDbZpInI8P2-Hw8S2NJo8f-Ki5kQqdfq6VjBU6MlHOIJPCqGUooakmSeDFsN05ks-W5Im2bvq43En7_bccE7reb-bnnSlip8Po0KzHiLK22XFt4YMmf_fZw62Rj2tAZCgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c865776e9.mp4?token=QpXFm4UPfh-a1VgO4pG6BnZG-8O0wovr9JM9OzG_FK7p_xz6t_gcOsOTGTV6Q2lzxBSWSv1PsZNtiDQkkXjYlkuHgYhc_twImHH9-ZhHPS3PygMvhc4-ZPgmDmiLe3Cyypsc_Sx_7054i1WdavF_Pm4EnG49--YeagPy2yJIqQ2HvhVCxD1jnUYDoftlPaX8Cehx1SOt7Ktw7ghXsDmBtDbZpInI8P2-Hw8S2NJo8f-Ki5kQqdfq6VjBU6MlHOIJPCqGUooakmSeDFsN05ks-W5Im2bvq43En7_bccE7reb-bnnSlip8Po0KzHiLK22XFt4YMmf_fZw62Rj2tAZCgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
حسن روحانی:
به مردم بگیم قرار ما اینه که با قدرت‌های بزرگ تا بیست سال دیگه بجنگیم.
اگه مردم قبول کردن عالیه بریم ادامه بدیم.
ولی اگه مردم نپذیرفتن و راه دیگه‌ای نشون دادن حق نداریم نادیده‌شون بگیریم.
حتی پیغمبر هم با مردم خودش مشورت می‌کرد.
تو این کشور هیچکی از جانب خدا حاکم نیست‌؛ همه به لطف رای مردم اومدن.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/71146" target="_blank">📅 17:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71145">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/100451e13a.mp4?token=D-gVyVuEIAa5F6hxO109KZUXmali5OiwemjuyJ458y0vUa9wU9us8h9F00pLiX-u5yKuDjkqIZUMhYDrUlN_LTlStsaufXf0wkxlXyn-emzD6WbYaAHBPlBh1UrMPlI6jBCKnXsj63L_iGUd1D9y_F_Ed-ZdLoDq2a0q78s5N3KH-ER8xYP5Q-9DyE-OTYK8c4jnJ5exEaPGygS2S-CFldnWwWD-dM3c8HjIZei06S2Mihw-CjmIWwPJCqXg_lSKQzD-6AMkSjjeVLEZG5rVUIVthcHHO3U0zJd3lKljWsisHQ7dH482CnXm7cbPC1-GOUwpFsOYO8iZXHLeOOaRgTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/100451e13a.mp4?token=D-gVyVuEIAa5F6hxO109KZUXmali5OiwemjuyJ458y0vUa9wU9us8h9F00pLiX-u5yKuDjkqIZUMhYDrUlN_LTlStsaufXf0wkxlXyn-emzD6WbYaAHBPlBh1UrMPlI6jBCKnXsj63L_iGUd1D9y_F_Ed-ZdLoDq2a0q78s5N3KH-ER8xYP5Q-9DyE-OTYK8c4jnJ5exEaPGygS2S-CFldnWwWD-dM3c8HjIZei06S2Mihw-CjmIWwPJCqXg_lSKQzD-6AMkSjjeVLEZG5rVUIVthcHHO3U0zJd3lKljWsisHQ7dH482CnXm7cbPC1-GOUwpFsOYO8iZXHLeOOaRgTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بابک زنجانی: سایپا را ۱ میلیارد دلار می‌فروختند، ۲ میلیارد پیشنهاد دادم، نفروختند
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/71145" target="_blank">📅 17:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71144">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b09e3df411.mp4?token=W7gmX_WraWsi_7lWnFHAuKJQXKXyT8ZudjnwFj_Xrtd_GgyBTu9e2PBwWgAf9JfH_FZRXW2K023fxUYrbFmIvB208hnzvIlfV6R_PtAvySpi2yyF5qT9_SoX167L_-_-SPCAFLz4qwxfe2gmme6LrztpAnDdFV-IQAxvauaWWlEyXmFF9AuDKTQGGf9U0uWZpHkSWvL0Flmovpmo7_bdEC_Jbgn76Y8uZUlTbq_xEN6m7QWtBOmNv6emD3IWIfA8OEIhUGKszQV0FptxZaWAEZIjYuZT6dKemyxvd8oj6vGwN1nCE_9ZHmwt7KY4OROhlzm92LWmov7WcEa8869fZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b09e3df411.mp4?token=W7gmX_WraWsi_7lWnFHAuKJQXKXyT8ZudjnwFj_Xrtd_GgyBTu9e2PBwWgAf9JfH_FZRXW2K023fxUYrbFmIvB208hnzvIlfV6R_PtAvySpi2yyF5qT9_SoX167L_-_-SPCAFLz4qwxfe2gmme6LrztpAnDdFV-IQAxvauaWWlEyXmFF9AuDKTQGGf9U0uWZpHkSWvL0Flmovpmo7_bdEC_Jbgn76Y8uZUlTbq_xEN6m7QWtBOmNv6emD3IWIfA8OEIhUGKszQV0FptxZaWAEZIjYuZT6dKemyxvd8oj6vGwN1nCE_9ZHmwt7KY4OROhlzm92LWmov7WcEa8869fZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه سری ایرانیا هم انگار توی یه ایران دیگن و رفتن توی جنگلای شمال پستونک پارتی گرفتن
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71144" target="_blank">📅 16:31 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71143">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc463ce6f9.mp4?token=FOvcrYKZLJafR_q_9EqLD9_CIzZ0t_XDupnS363Py5RiZ3yotW4arP0t0VDEn9ogo45wmQqT_amcb8oJEx3odwEU6duf25IbLp5OB4zNGsiXb06JlbolQU1rOhuYxBch5-an8wQXe9QiRvoYuh_-mtZlzX05Bd0pmxya-ShRey7uvbLPgsT_C2ddrDZzeowP8py7nNeyuue24Hled5ynEZ8-B71ARjiuWHX0bxyeIGWs1JENeBLjRXhYtxbqeOOjuByaOHqtrFge6WGrC8bUCiAFvJeulV6XaJqpQvG8rrVG0oiruJqkYWXE6wVB7NzvQhyPPYEzzJEnVcyX-4teiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc463ce6f9.mp4?token=FOvcrYKZLJafR_q_9EqLD9_CIzZ0t_XDupnS363Py5RiZ3yotW4arP0t0VDEn9ogo45wmQqT_amcb8oJEx3odwEU6duf25IbLp5OB4zNGsiXb06JlbolQU1rOhuYxBch5-an8wQXe9QiRvoYuh_-mtZlzX05Bd0pmxya-ShRey7uvbLPgsT_C2ddrDZzeowP8py7nNeyuue24Hled5ynEZ8-B71ARjiuWHX0bxyeIGWs1JENeBLjRXhYtxbqeOOjuByaOHqtrFge6WGrC8bUCiAFvJeulV6XaJqpQvG8rrVG0oiruJqkYWXE6wVB7NzvQhyPPYEzzJEnVcyX-4teiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇳
تو چین یه نفر بعد ورود به مغازه‌ش که به علت نشتی پر از گاز بوده، کلید برق رو میزنه و کل مغازه میترکه ولی خوشبختانه زنده میمونه و بعد از اینکه به بیرون پرت میشه کون لختی فرار میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71143" target="_blank">📅 16:03 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71142">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9c6b59588.mp4?token=JK044tiChGbwtEGNNjEnUb3jysMwUjP9xXyGkb4gsJUDcfNVCASn1XhklqQO6DuMFAtCtiJP4Uc7UKQSOxNBUqnXrKDCmadTerxrePHPfDySeVQcawjjH5klB6BAs-IXrX_RXEVf_gOsA3PCkYwpSE7ODzuwT_g7-x5Smygf2_ja9pvn58YzW2PGpVFo55i2ltPKefPMoRWDOXq5Yv3-lWFgH3Tfh67ZBxKvSnntgHjEHcSpkN1xr_2P_ydlRypuRBYsK_3zqZrQihLk5G68IeWufCt46mlnFb3RTS5OcPff5uei5DWYN6Eh9kWi4OR_g4RUz-4FtiJnP6_Ob_14QoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9c6b59588.mp4?token=JK044tiChGbwtEGNNjEnUb3jysMwUjP9xXyGkb4gsJUDcfNVCASn1XhklqQO6DuMFAtCtiJP4Uc7UKQSOxNBUqnXrKDCmadTerxrePHPfDySeVQcawjjH5klB6BAs-IXrX_RXEVf_gOsA3PCkYwpSE7ODzuwT_g7-x5Smygf2_ja9pvn58YzW2PGpVFo55i2ltPKefPMoRWDOXq5Yv3-lWFgH3Tfh67ZBxKvSnntgHjEHcSpkN1xr_2P_ydlRypuRBYsK_3zqZrQihLk5G68IeWufCt46mlnFb3RTS5OcPff5uei5DWYN6Eh9kWi4OR_g4RUz-4FtiJnP6_Ob_14QoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🇺🇦
🇷🇺
یک مزدور برزیلی که در درگیری‌های روسیه و اوکراین می‌جنگید، لحظه حیرت‌انگیز عبور یک تانک از روی خود را — در حالی که میان علف‌ها پنهان شده بود — ضبط و در حساب اینستاگرامش منتشر کرد
😟
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71142" target="_blank">📅 15:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71141">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f07a24e005.mp4?token=gVBTmx78HCaZevvjWaDjUAHU_Y_pPLFWbBTtclkGHRHgOIX0WYFcvEg0kUt4C08GhvwtLyGTc0PqS0iEvFPkJ1rpzSKXTYoPIJTOK4kbDoQb1a7sryDfapt_oOIDn481b2PnBAeVDurNQASWVSn6fgLtDR9Mc92d6-O-zrI_uVv1qQeIZsZ9KTgwDUUe0SyWsWNp3XckdAxJszGSYXj6zTLM6G2gR-xzNwExzHfSu3wW5kw_J-uT2hZw4A-Xd_YmvhZAHcK4fk440ztBdwTVf6lWLxyVIimblSLxWMK6YjC9aFbN2cv4-L8JmMsG8u0VV1u7k-Z5-uXMopOTrB_Pqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f07a24e005.mp4?token=gVBTmx78HCaZevvjWaDjUAHU_Y_pPLFWbBTtclkGHRHgOIX0WYFcvEg0kUt4C08GhvwtLyGTc0PqS0iEvFPkJ1rpzSKXTYoPIJTOK4kbDoQb1a7sryDfapt_oOIDn481b2PnBAeVDurNQASWVSn6fgLtDR9Mc92d6-O-zrI_uVv1qQeIZsZ9KTgwDUUe0SyWsWNp3XckdAxJszGSYXj6zTLM6G2gR-xzNwExzHfSu3wW5kw_J-uT2hZw4A-Xd_YmvhZAHcK4fk440ztBdwTVf6lWLxyVIimblSLxWMK6YjC9aFbN2cv4-L8JmMsG8u0VV1u7k-Z5-uXMopOTrB_Pqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
یه آخوند درباره شعار«تا آخوند کفن نشود این وطن وطن نشود»
؛
همونطور که رهبرمون رو شهید کردن یه آخوند دیگه جاشو گرفت
به ترامپ و نتانیاهو و منافقین داخلی میگم این حرفمو
تا آخوند شماهارو کفن نکنه ول نخواهیم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71141" target="_blank">📅 15:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71140">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">⛔️
این قبیله ای که میبینید اسمشون موکو موکو هست
؛
این قبلیه در افریقا که مثل سرخپوست ها هستن برای اینکه زنان قبیله خودشون دعوت کنن به سبک رقص های به خصوص خودشون انجام میدن
هر زنی در قبیله شون مجذوب رقص مردی بشه میره بهش میده و اصلا اینطوری نیست که کسی حتما باید زن شخص خاصی بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71140" target="_blank">📅 14:33 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71137">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca83f4e683.mp4?token=gh_vgEleK9PDhlIPePwuNVg1sFNEx60K0zP75WKMGW9BU7CCOIs-WQFmlsoLYWGRKaYmnAfc6dppjZmK2H_md_Bth9B3xMH-LaTfL2tsl-ViWGglpXL-Fhgn8JtNJhVX33ZSKSBQX8n-niSgjgbwRxx6mgM_Qz2A-u8fGOftxpgLu-abtqLo4a1CgRtJMRvu0n8IzjPRqZMmaV-b-fcKVEmV6cBM-zF1MTYp40fuX6ipaxl5uwp_KS3EpwkFyc2-t6CsBrutVqR0pHLh0QYYYmZvHQxdKtYtMyM1bk86DQkj_PANS3or8wdax8dBCdiOqnuW2ykHgHMX93gdcB3yXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca83f4e683.mp4?token=gh_vgEleK9PDhlIPePwuNVg1sFNEx60K0zP75WKMGW9BU7CCOIs-WQFmlsoLYWGRKaYmnAfc6dppjZmK2H_md_Bth9B3xMH-LaTfL2tsl-ViWGglpXL-Fhgn8JtNJhVX33ZSKSBQX8n-niSgjgbwRxx6mgM_Qz2A-u8fGOftxpgLu-abtqLo4a1CgRtJMRvu0n8IzjPRqZMmaV-b-fcKVEmV6cBM-zF1MTYp40fuX6ipaxl5uwp_KS3EpwkFyc2-t6CsBrutVqR0pHLh0QYYYmZvHQxdKtYtMyM1bk86DQkj_PANS3or8wdax8dBCdiOqnuW2ykHgHMX93gdcB3yXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇦
تصاویری از تورنتو کانادا بعد از بارش باران و طوفان
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71137" target="_blank">📅 13:51 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71136">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fec01afbd.mp4?token=IxeGcJTwyLE3h_5tlr91t26CA78q9okw4T4k9YNM5XBF8Wqnc-EsHqDDnr3DR9k4pdWy5Mpu3na5VXZ5yW0nWfR-9MHthBW3oIJMGUOY_qz4rcT6MV0pnFRI3eFdKd_zV5ywqMDdEo6mgk4NTnz4GCuWOLeN_p5xGRNa7VSm1DwlkevO9bcwK8pO_XUJ1D6oKh3u34K_J3RZMkfOFEwjCGUe_q3AtQFJ5cVQCb7z1sxsHdWPHJW3euOzl-0kCPupYBWXohygE8yY6dHxAob7LFK5L5LNanCc80kABd3qChpO_teJLBXyFNZIum4Ncd5Q8YP7-obfwC006h2rDxeHig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fec01afbd.mp4?token=IxeGcJTwyLE3h_5tlr91t26CA78q9okw4T4k9YNM5XBF8Wqnc-EsHqDDnr3DR9k4pdWy5Mpu3na5VXZ5yW0nWfR-9MHthBW3oIJMGUOY_qz4rcT6MV0pnFRI3eFdKd_zV5ywqMDdEo6mgk4NTnz4GCuWOLeN_p5xGRNa7VSm1DwlkevO9bcwK8pO_XUJ1D6oKh3u34K_J3RZMkfOFEwjCGUe_q3AtQFJ5cVQCb7z1sxsHdWPHJW3euOzl-0kCPupYBWXohygE8yY6dHxAob7LFK5L5LNanCc80kABd3qChpO_teJLBXyFNZIum4Ncd5Q8YP7-obfwC006h2rDxeHig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پیرزن طرفدار حکومت که میگه:
نه پول میخایم نه چیزی دیگه گرونی هم تحمل میکنیم مسئله حجاب رو حل بکنید خیلی مسئله مهم تر و واجبی هستش
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71136" target="_blank">📅 13:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71135">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5af49e9554.mp4?token=FoCh1zPsQvHDErfkYdkoIdlR_Xg8WAq_a4vPbHpPGk-1KCtuQjGXf2iqdCRd6h5l1Se3aT-7UkIseqpryC8-fcfg4nGsf4ktGyT-lSP85L5nxNLVCd4strlbEuUrgIVQ4_EGUvdW0-flShC1tHu0Fhyljb6gTnqORQZWcaMv5S6aa7EwAYii0qVnvH7ZAoy7Oo2olbnuTZaeM2psrUjSz5sm3MN4i28AkGoMQy85Q-xfaJAVuclC8Y2sNIle4hE7H1vbtmPUh6QdF2Sbo09N1_07fk7C-968f3-jy6lHVLMYcpBaAvV4fjc2Vc3CfoCteerf2tueDbHs5sK61xiIDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5af49e9554.mp4?token=FoCh1zPsQvHDErfkYdkoIdlR_Xg8WAq_a4vPbHpPGk-1KCtuQjGXf2iqdCRd6h5l1Se3aT-7UkIseqpryC8-fcfg4nGsf4ktGyT-lSP85L5nxNLVCd4strlbEuUrgIVQ4_EGUvdW0-flShC1tHu0Fhyljb6gTnqORQZWcaMv5S6aa7EwAYii0qVnvH7ZAoy7Oo2olbnuTZaeM2psrUjSz5sm3MN4i28AkGoMQy85Q-xfaJAVuclC8Y2sNIle4hE7H1vbtmPUh6QdF2Sbo09N1_07fk7C-968f3-jy6lHVLMYcpBaAvV4fjc2Vc3CfoCteerf2tueDbHs5sK61xiIDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
تصاویری از نفتکش ایرانی که چند ساعت قبل هدف حمله آمریکا قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71135" target="_blank">📅 12:41 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71131">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bb2e861ad.mp4?token=MHTpc_U_tTvgwpXUmJCyaFS87dt31A8AAbPvneZqC6gkikmuPZ7vXYUj4ImC0BYm1mdWEhKvfy1xbd25JVv3FUvplJmFUTT8lNHElhUKWR5kJVorTAB2UA7NCiPrnZXU3iUYbSOFwJbCUBJKw9_sirpONrckx1xodMjP2oM9HfUWaj7WhddvSqHgjugELI52QJrE9KcVG3dOJAqBuyk7tGvSpHjIf5MeKVnOhEXH8l_VbTJ879-WKWXVxTrIuEbN2MZTHSZXHZ8qO-eggp0dXb7rqwQzYY7b-WybSO9Li5F6XleD6xYrIc9k0qZ1voDiCtbHJCJIufG6pj-cQyePNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bb2e861ad.mp4?token=MHTpc_U_tTvgwpXUmJCyaFS87dt31A8AAbPvneZqC6gkikmuPZ7vXYUj4ImC0BYm1mdWEhKvfy1xbd25JVv3FUvplJmFUTT8lNHElhUKWR5kJVorTAB2UA7NCiPrnZXU3iUYbSOFwJbCUBJKw9_sirpONrckx1xodMjP2oM9HfUWaj7WhddvSqHgjugELI52QJrE9KcVG3dOJAqBuyk7tGvSpHjIf5MeKVnOhEXH8l_VbTJ879-WKWXVxTrIuEbN2MZTHSZXHZ8qO-eggp0dXb7rqwQzYY7b-WybSO9Li5F6XleD6xYrIc9k0qZ1voDiCtbHJCJIufG6pj-cQyePNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇱🇧
خبرنگار اعزامی صداوسیما به لبنان سقوط تپه علی الطاهر در جنوب لبنان رو تایید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71131" target="_blank">📅 12:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71130">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
خبرگزاری فارس:ساعتی پیش، صدای چند انفجار از خلیج فارس در محدوده جزیره خارگ شنیده شد  خبرنگار فارس در جزیره خارگ می‌گوید صدای انفجار از محدودهٔ خلیج فارس به گوش رسیده است اما نشانه‌ای از دود و آتش در خلیج فارس مشاهده نمی‌شود. تاکنون اطلاعات رسمی و دقیقی درباره…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71130" target="_blank">📅 11:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71128">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AnMt81IANOKHyKeKIjPTZRpvANy9WN9hfs1Iaw6q52Wh589O7oQ8El6sQJqSvP4Apt4pxgQKnahp15FS-N3rRhmuoM-7DhAs9Pnk0vAGZuftb7l2YuAe_r26KDbYuQKnI5F_kOkbLyjqaVj7A_H0eFILv1PHMNMxilH-0i3KSPiRCeS_ul5ybYQ86HFGOgXEKNWqZmgLgYBl3glE5X-JzVRD49rs4B4mqmKeP4vrYxVsKWpvsTIU4sJXcqc3yjui0gazK2lwCJENN2PacClI-bf4eJ7n0TOvehp-wxZFfE4CaughOX_BSBEPBy9A4bBMfId6DZEU8wgDYwbQFLmBTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/924e97ac3c.mp4?token=iiBpzuFc5u88hVvbNcFEotyMfemY5DiZzS5fYV-NIoKnRHu_Q0LjNdy3s1jkhRKSpoEBdN95qvftNA6QU9kCM5UD5V7W8W3gCgIWgjMFic4a86arATx_lj9E_PKmX1zpQTI6Oodfhi64S9w2Ggr2vpexA9alfj_gPZuGZPBFUTbVOqbSv9sNpEPR-EY4CKMDh_xJ1Rjy2gGLOeNjYeBkUd2LbKPkgCx30IjDdfPWB1KidWyxOwTmBhwBhHkiOpPagWZfKv3jYbypbfMtir0-zjVvRdVF-d_G4dNcKOIOCGT-kbZSD-wn9hv33yFVldrKtumzcEqezZ7t8ddCMzv_0A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/924e97ac3c.mp4?token=iiBpzuFc5u88hVvbNcFEotyMfemY5DiZzS5fYV-NIoKnRHu_Q0LjNdy3s1jkhRKSpoEBdN95qvftNA6QU9kCM5UD5V7W8W3gCgIWgjMFic4a86arATx_lj9E_PKmX1zpQTI6Oodfhi64S9w2Ggr2vpexA9alfj_gPZuGZPBFUTbVOqbSv9sNpEPR-EY4CKMDh_xJ1Rjy2gGLOeNjYeBkUd2LbKPkgCx30IjDdfPWB1KidWyxOwTmBhwBhHkiOpPagWZfKv3jYbypbfMtir0-zjVvRdVF-d_G4dNcKOIOCGT-kbZSD-wn9hv33yFVldrKtumzcEqezZ7t8ddCMzv_0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یه پسر بدبخت پست گذاشته که اگه این پست ۵ هزار تا لایک بخوره، صاحبکارم منو میکنه! تورو خدا لایکش نکنین.
و حالا واکنش مردم دلسوز ایران:
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71128" target="_blank">📅 11:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71127">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
خبرگزاری فارس:ساعتی پیش، صدای چند انفجار از خلیج فارس در محدوده جزیره خارگ شنیده شد
خبرنگار فارس در جزیره خارگ می‌گوید صدای انفجار از محدودهٔ خلیج فارس به گوش رسیده است اما نشانه‌ای از دود و آتش در خلیج فارس مشاهده نمی‌شود.
تاکنون اطلاعات رسمی و دقیقی درباره علت و منشأ این صداها منتشر نشده و جزئیات تکمیلی متعاقباً اعلام خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71127" target="_blank">📅 11:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71126">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71126" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71126" target="_blank">📅 11:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71125">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMy3bGXOQNAwVS0M4Sjg1o44SeR17hsSO7Dac63Nb02m3t1E63kOkIdmgw64KMTipyEqDD0qCt2uw0RDqHr8eznrt-GMMjYAWMMtTH2L5skpcw925vXHjjt_kfV4i2gdIR3YhhlTjLhsApkzSVANbXKRr3uglPLXnNIY2u8NQwYp6PPLvaPtbqay_xFEjINkd2dmOjG5LVZeePTfMshP2Vx65QgI9GMfp6TLwnynLtxfdscqhK1IaEZhNIWiH9a--_CI80QAXQ8tcJ5NzCn5DxpaOoF634Ca4R334rXUdN0FZduylxhnbhIRa8Qvhy3JlSMQ9HR9RCWQz2t_VdRodw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
پیش‌بینی کنید.
بورنموث
🆚
نیوکاسل
کاونتری
🆚
منچستر سیتی
تاتنهام
🆚
ناتینگهام فارست
اتلتیکو مادرید
🆚
اتلتیکو بیلبائو
ناپولی
🆚
اینتر
آتالانتا
🆚
رم
دورتموند
🆚
هوفنهایم
بایرن مونیخ
🆚
شالکه
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71125" target="_blank">📅 11:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71124">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0380bdceab.mp4?token=TueNIh73b3zsgXg5zqCQILNljJFXds_oKfrzGgSXWubMYyHXKFlTHOe5KzVj4CatZf-YY2Cwld8vlPRi5I8AXoYREHTp7K60m6jlhl_IgqoNG_LKMz9Q0omj4MWQDot1oUZ0OQa2mQaMceCidcz8VD8-DYKI8mCcnrb25GSB3K1AY2niulByXTpjUWf9st-_mpB04FvOaZYZ46FO_V4TPOYgZY1H7moxx3nEeS7EEt_XjOoRYcUi_OkfyIN6rg_pGuJO_S7ThAneDZJvxyDDjxCYPDjVBaQOLz9oy7m15FBrcYyjUl1wvDgz56USSW59hTLgbBdoj06IBRmQJPzjAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0380bdceab.mp4?token=TueNIh73b3zsgXg5zqCQILNljJFXds_oKfrzGgSXWubMYyHXKFlTHOe5KzVj4CatZf-YY2Cwld8vlPRi5I8AXoYREHTp7K60m6jlhl_IgqoNG_LKMz9Q0omj4MWQDot1oUZ0OQa2mQaMceCidcz8VD8-DYKI8mCcnrb25GSB3K1AY2niulByXTpjUWf9st-_mpB04FvOaZYZ46FO_V4TPOYgZY1H7moxx3nEeS7EEt_XjOoRYcUi_OkfyIN6rg_pGuJO_S7ThAneDZJvxyDDjxCYPDjVBaQOLz9oy7m15FBrcYyjUl1wvDgz56USSW59hTLgbBdoj06IBRmQJPzjAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📚
معرفی لاکچری‌ترین مدارس ایران !
برای اینکه به علم برسی هم باید اول ثروت داشته باشی!
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71124" target="_blank">📅 11:03 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71123">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a478b3c9a9.mp4?token=O_0x5fqpbTmwC28imlEKbicFNHxcaJMFYikh-KEUK08jsGXy2FLdlMOrJV-DPnXhlh0Ky_Dj0ed_Enn2hlXR_HhlDbm8WKxakxQkeK-hOvRwnRHWwI6_8o5dvcMbxadZ2VbQZ_W4OECxd9mThmLQxYsg4lsMq-wsvFWXhLl2De0xKxsOCOiDaejXPMRGX0_iMJFmOAHH3Bkz6ZYVgTPR_dKCNQjmuwEV6ROrE8gEQzohWL4iJSLyOAabJhUExLPHCXKAAu7D_4BDD5GYV8JJyZWTifNH0BzMjCQsqSO44JYyZ3D0Vjbf-_v0p1-xPoNNsvAWU-fprwRYFWr34PveYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a478b3c9a9.mp4?token=O_0x5fqpbTmwC28imlEKbicFNHxcaJMFYikh-KEUK08jsGXy2FLdlMOrJV-DPnXhlh0Ky_Dj0ed_Enn2hlXR_HhlDbm8WKxakxQkeK-hOvRwnRHWwI6_8o5dvcMbxadZ2VbQZ_W4OECxd9mThmLQxYsg4lsMq-wsvFWXhLl2De0xKxsOCOiDaejXPMRGX0_iMJFmOAHH3Bkz6ZYVgTPR_dKCNQjmuwEV6ROrE8gEQzohWL4iJSLyOAabJhUExLPHCXKAAu7D_4BDD5GYV8JJyZWTifNH0BzMjCQsqSO44JYyZ3D0Vjbf-_v0p1-xPoNNsvAWU-fprwRYFWr34PveYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تسلا، سفر با تاکسی‌های خودران Cybercab رو تو تگزاس آغاز کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/71123" target="_blank">📅 10:34 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71122">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a09a3f19ee.mp4?token=aMwwZBJKzYQjbiqfSRRhx4duHTjWlLTsTnoNXozo1kZWgx4ydnbh774WbSSXvIAkrdzKjs1dyx_XstzdIDUIJ_nbCzqzFIjxgDePQXoxYmm99C_XzcvPZfB09ecaCF2Xnz9zyLbjPpd3QKseo26gGTEn-cODgdgHqyQ3ji0ud1JOkJlvJqMvbWT5vSCf3vUo522o-E0wLt5XaMlyyQ0kVZEBZlS1RsIU68B1QGjLgrxyLtKIoubCo5MhpjJK18j0Vu2sQKbEQRluGiX-jgEq_DhT-EJWim1DoaWtVuFKqIjNFv2EBuE6DYfv35wS8oUBecrH84ndX2B0nt-RkzlGvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a09a3f19ee.mp4?token=aMwwZBJKzYQjbiqfSRRhx4duHTjWlLTsTnoNXozo1kZWgx4ydnbh774WbSSXvIAkrdzKjs1dyx_XstzdIDUIJ_nbCzqzFIjxgDePQXoxYmm99C_XzcvPZfB09ecaCF2Xnz9zyLbjPpd3QKseo26gGTEn-cODgdgHqyQ3ji0ud1JOkJlvJqMvbWT5vSCf3vUo522o-E0wLt5XaMlyyQ0kVZEBZlS1RsIU68B1QGjLgrxyLtKIoubCo5MhpjJK18j0Vu2sQKbEQRluGiX-jgEq_DhT-EJWim1DoaWtVuFKqIjNFv2EBuE6DYfv35wS8oUBecrH84ndX2B0nt-RkzlGvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
〰️
🇹🇭
کامیون‌های سوخت‌رسان مشغول انتقال سوخت هواپیما به ناو هواپیمابری «یو‌اس‌اس آبراهام لینکلن» (CVN-72) در بندر «لائم چابانگ» تایلند هستند؛ به‌طوری که از زمان پهلو گرفتن این ناو، روزانه ورود و خروج ۲۰ تا ۳۰ دستگاه کامیون مشاهده شده است.
این سوخت برای تأمین نیازهای «بال هوایی نهم ناو» (CVW-9) در داخل ناو ذخیره می‌شود؛
یگانی شامل جنگنده‌های رادارگریز F-35C Lightning II، جنگنده‌های تهاجمی F/A-18E/F Super Hornet، جت‌های جنگ الکترونیک EA-18G Growler، هواپیماهای هشدار زودهنگام E-2D Advanced Hawkeye و بالگردهای MH-60 Seahawk.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71122" target="_blank">📅 10:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71121">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/deba41468f.mp4?token=XG-3OnWOpt9kc0R6Ax2ayWPU3hKJlBLRep6r7kAHewa4kFico3wWiA1QqeIw-VHpL468OrDehVSbxp57rLPjDrJxcR3ClZgdpqoLoOJE2bIrAvBUIUBG2tewiE4LafoUncIdNiqS-ixJ-XZGwKOsfRT7xGbrpTf1I_9kx-s00IGzmwdNbvVwjc4tKVSqnEjZ8QzgkY7ZDvlLJiv1wrd6nW3Az_b9J76plUzA-Me11KpbBqpNnaEBr-8D1KcwJqQG0et4BV4maMuQ7-0hcdoeVaMo-uSjvkLyqdq2zL8H6OBxdJxdwIPUb0WaXkOoPrr2l1ywWuu8QQpODnQDXxZGFrlUn9NhDhkIZx681qJqBiIp8G2DO9kHLAHJIIyiDZnhLbMV5p8Ku64fYEQ2B1mrHui3wUjg3JmginW1PV0cXFtLFV-r8-oZcS8CLx4XEBN-TCWrymUTscVrCeDiPV0cAR-PiVzEbPFW2SYnRJ94Mw4gHv_6h_h5T7441Jtk4hjgV6a4vvK9VE7vLdez8ORQWuSSU_jx8pZKctUNuKL4ZnX88YTdQWkXqmajy_GgrKGyYF8YBnWDvw6-ZmMDBQS0qapjQYE0NwRGwQqpyC2gbOuDQyxDUpmLIngosAxD_NpFDXD55IhYPdGmaAfpsqgZFCCCu9HlseuFHMi32batOhk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/deba41468f.mp4?token=XG-3OnWOpt9kc0R6Ax2ayWPU3hKJlBLRep6r7kAHewa4kFico3wWiA1QqeIw-VHpL468OrDehVSbxp57rLPjDrJxcR3ClZgdpqoLoOJE2bIrAvBUIUBG2tewiE4LafoUncIdNiqS-ixJ-XZGwKOsfRT7xGbrpTf1I_9kx-s00IGzmwdNbvVwjc4tKVSqnEjZ8QzgkY7ZDvlLJiv1wrd6nW3Az_b9J76plUzA-Me11KpbBqpNnaEBr-8D1KcwJqQG0et4BV4maMuQ7-0hcdoeVaMo-uSjvkLyqdq2zL8H6OBxdJxdwIPUb0WaXkOoPrr2l1ywWuu8QQpODnQDXxZGFrlUn9NhDhkIZx681qJqBiIp8G2DO9kHLAHJIIyiDZnhLbMV5p8Ku64fYEQ2B1mrHui3wUjg3JmginW1PV0cXFtLFV-r8-oZcS8CLx4XEBN-TCWrymUTscVrCeDiPV0cAR-PiVzEbPFW2SYnRJ94Mw4gHv_6h_h5T7441Jtk4hjgV6a4vvK9VE7vLdez8ORQWuSSU_jx8pZKctUNuKL4ZnX88YTdQWkXqmajy_GgrKGyYF8YBnWDvw6-ZmMDBQS0qapjQYE0NwRGwQqpyC2gbOuDQyxDUpmLIngosAxD_NpFDXD55IhYPdGmaAfpsqgZFCCCu9HlseuFHMi32batOhk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بابک زنجانی:
الان کافه‌های مردم را می‌بندید بعد شب آدم می‌فرستید که بیاید تعامل کند.
می‌خواهم فیلم و مستند درباره این موضوع تهیه کنم... آن شخص هم فکر می‌کند که با ۱۰، ۲۰ سکه زندگی‌اش را گذرانده
بیکار کردن ۸۰ نفر در منِ بابک زنجانی چه اثری دارد؟! اصلاً فردا بیایید آتشَش بزنید.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71121" target="_blank">📅 09:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71120">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XcpsmmsKZIAfpvryQ_c7uSUYjwao0YFx3HM2sk0dtyXdiOMHbiG0Rj7VGvMtthAzADAFyXKdxSm-iMb4c865GbY7maQpS7ZMf-gLks-3dQyIkjKKeNlm-dHHx-erO_cULoIMX0ZWwNoukqLEz2fDy__S-tYEz9NNq6Sr6WTNezZapvHFDlrolzNcSJxp2WsPyUI0XUSzRnZ7Ie_FdOHmh9lo32BAgm5_49rk0Ud5-mvw_aFMuC1UE7iKqbRceO0Y7l588PFnuBhtjV8y0yGe3CH3lSQ_JCy_k4S-X5Q4lplssELCk2Thx3gaITg1p_s2kgYkjkxyK5UMzDxCwG8JlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
🇴🇲
نیویورک پست:عمان بی‌سروصدا پیشنهاد ایران برای دریافت مشترک عوارض از کشتی‌های عبوری از تنگه هرمز — حتی به‌صورت داوطلبانه — را رد کرده است.
این اقدام، ادعای هفته گذشته سپاه پاسداران مبنی بر توافق دو کشور بر سر تقسیم درآمدهای این آبراه را تضعیف می‌کند.
عمان معتقد است که دریافت عوارض از کشتی‌های عبوری ناقض قوانین بین‌المللی است و تحت فشار آمریکا و کشورهای حوزه خلیج فارس، از این طرح عقب‌نشینی کرده است.
ترامپ دو بار تهدید کرده است که در صورت موافقت عمان با دریافت عوارض، این کشور را بمباران خواهد کرد.
ایران در دوران جنگ، نهادی برای مدیریت تنگه ایجاد کرده بود و از هر نفتکش مبلغی بین ۱ تا ۲ میلیون دلار عوارض می‌گرفت؛ اما بدون همکاری عمان، هرگونه سازوکار دریافت عوارض در دوران پس از جنگ، فاقد وجاهت قانونی خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71120" target="_blank">📅 09:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71119">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71119" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71119" target="_blank">📅 01:13 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71118">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjABErUNJyT3usUu8s_OxbPzjvVKrAnfbauMfpWsdbyPI3qtX1r1R8k95s2iR8Aq8fdQAQVZO5UEax0TxTNzzeeHki5KwrcAjAkNQD4MJ1hvK6HkQrqkjDjoflky2w_dm7FcEwyzVBND2NG-saN53cfBxS2PPSCHDMEQ789xE4muK_CNS6aOpS58qfCgreFaYXuO0OcjIhHWc3ElcDbbFuuuER0QVIE_5xW_wCxg-9C6IJwj-t_hmKvYN9fIhMHtDRmIInAgi5z9pnK5q3GlzyyLR06GqzWnHcIRO_2W-TdvoY_X-hCSj9L5Q5Hlw8Vut6NJHgjEHvv9VBNJ8wYyGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71118" target="_blank">📅 01:13 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71117">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59487b6d80.mp4?token=ZH-eWDhOoYBnrTa6vKr_Es06CihAy9Y6ZVW7sM9i_WAfPap5MO7KEbKYw8hePLStInb4ZHfN-z1NUu2FwJNPCDRsixZHtzvI2Y6IrlyU0Ot3IqGUXU27S7ezesbt1W1RVy7NV02ftgN7dIQ6AJUbn-PrBIMOVVvia8_tCylJiEsx023zGAFjS8pcA37_SRN0ro2y3K5sR7xXgmg1hLYPE2i8RiMgWvEwD5a65ArZeXQor3xUvuRQPhGVihfUaYeri_1ihwuksdbljRuZg-4lW60hLPBCiv4GEvwH6vZj2zE0s_QRoOaYZueRJAnJ-o229CfT2cqIraqWtlos7Jt2dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59487b6d80.mp4?token=ZH-eWDhOoYBnrTa6vKr_Es06CihAy9Y6ZVW7sM9i_WAfPap5MO7KEbKYw8hePLStInb4ZHfN-z1NUu2FwJNPCDRsixZHtzvI2Y6IrlyU0Ot3IqGUXU27S7ezesbt1W1RVy7NV02ftgN7dIQ6AJUbn-PrBIMOVVvia8_tCylJiEsx023zGAFjS8pcA37_SRN0ro2y3K5sR7xXgmg1hLYPE2i8RiMgWvEwD5a65ArZeXQor3xUvuRQPhGVihfUaYeri_1ihwuksdbljRuZg-4lW60hLPBCiv4GEvwH6vZj2zE0s_QRoOaYZueRJAnJ-o229CfT2cqIraqWtlos7Jt2dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
مردم آمریکا چه زمانی باید انتظار تعیین تکلیف (resolution) در مورد ایران را داشته باشند؟
🇺🇸
ترامپ:
انقلاب(Revolution)؟
🎙
خبرنگار:
تعیین تکلیف(Resolution).
🇺🇸
ترامپ:
تفاوت بزرگی است. فکر کردم انقلاب(Revolution) جالب‌تر بود.
⭕️
🗒️
به دلیل تلفظ نزدیک دو کلمه راه حل/تعیین‌وتکلیف(Resolution) و انقلاب(Revolution) ممکنه ترامپ اینجا به عمد کلمه انقلاب رو انتخاب کرده باشه!
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71117" target="_blank">📅 01:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71116">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76ef0c44cf.mp4?token=QN01LlCuv_QDHL3L58IJ3XdabC4yTVn3DphG385dk6FkW_ivFJN11oq5g8DnMmOUoOEAZFFi3wjAmhFuptI_5aM_1aA-Rkc-EyGf513SPXweslnDMv8YlLL86v5uW_LLuhPLQp8DvY3hupiG0IkCi3b7MtMx-4dYQ4288Ko71mYLTwSiUBoo73Zu-rP5p5neLbK4vtHFrEFcJCFzHDLir9bRDrhaFo8YicSsJlygFBXFzhpa8nU3fk22QwD_hXFDx2mO4swt_wq9blDn_xJk1vmtKUe--0SnCyhqJNyM042A5ln04ptvmx3mUj-Mz18VGnHwdhABG9aXtSeH5-gRNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76ef0c44cf.mp4?token=QN01LlCuv_QDHL3L58IJ3XdabC4yTVn3DphG385dk6FkW_ivFJN11oq5g8DnMmOUoOEAZFFi3wjAmhFuptI_5aM_1aA-Rkc-EyGf513SPXweslnDMv8YlLL86v5uW_LLuhPLQp8DvY3hupiG0IkCi3b7MtMx-4dYQ4288Ko71mYLTwSiUBoo73Zu-rP5p5neLbK4vtHFrEFcJCFzHDLir9bRDrhaFo8YicSsJlygFBXFzhpa8nU3fk22QwD_hXFDx2mO4swt_wq9blDn_xJk1vmtKUe--0SnCyhqJNyM042A5ln04ptvmx3mUj-Mz18VGnHwdhABG9aXtSeH5-gRNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو ایتا و روبیکا از یچیزی رونمایی کردن که حتی خودشون هم نمیدونن چیه
😳
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/71116" target="_blank">📅 23:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71115">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c1e4d7b78.mp4?token=hKQT35rOMJ6zTVi6_Aq8JFFlVcTOHusU8yZzLitkx66CfFdLwpclDQLQ9EL0BFFrU3jl2-WgYVV11FiVWs_1VAWjlEVmQTsOerpDORHHTs8PcEokiuy385gsx8xWb_rkDg9WV9RNhwC8mQwPQ4f5ILlFvLzSNIOqulQeXdXC11OoMn-ZL-LEXZg1FAe2yEgPL4xL0l863k-f8_nH7Ycxq_UHhFcAPH-9XkwaO9ASZb4EcotLZsnmOU39ParEsQNcHyCS7TLxD3vmuyV3lXDumZflNeU86oGorS_WPcfTQY-NGtYB6-PH2ND1skIt81nhvKx0T_1ohKOQ_FdBVpnpwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c1e4d7b78.mp4?token=hKQT35rOMJ6zTVi6_Aq8JFFlVcTOHusU8yZzLitkx66CfFdLwpclDQLQ9EL0BFFrU3jl2-WgYVV11FiVWs_1VAWjlEVmQTsOerpDORHHTs8PcEokiuy385gsx8xWb_rkDg9WV9RNhwC8mQwPQ4f5ILlFvLzSNIOqulQeXdXC11OoMn-ZL-LEXZg1FAe2yEgPL4xL0l863k-f8_nH7Ycxq_UHhFcAPH-9XkwaO9ASZb4EcotLZsnmOU39ParEsQNcHyCS7TLxD3vmuyV3lXDumZflNeU86oGorS_WPcfTQY-NGtYB6-PH2ND1skIt81nhvKx0T_1ohKOQ_FdBVpnpwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
طرف اندازه یه گاری پول جمع کرده و الان آورده تبدیل به دلارش کنه، کل این همه پول نقد شد فقط ۳۰۰ دلار
!
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/71115" target="_blank">📅 22:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71114">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/05f93dafa7.mp4?token=lQqY24jyqjXILPajnF03mXQj_kwxTadIvrzsZ_091Orq58Dw_YwU_6hzLuEMYCDi-J3QviVfn0Ls6wdDpjO2YS5J4k9uVLopI_EAW1b3b4nTqiqusZfhytxHIc3Ofl8HAg9-EyToYQWenD8FkLfVL7D8qH6LM94L787bBtpoODha6OHfmTlXzt4OXhFLHCyeMfXxMqdprCshvdBXD9pd5EQ60xU2MeTmzNdf2-PzlWVO4SiKVItH_onQ-dPKV16eOGBrl1SEW2LoOZdTVfppvmn-XvjP9ROtJShl6I0UV9eEpt54G5EApLxMwmpm6bdNDLA3eU_-hJJnXBZvfO1vkqrzuKRnrP7l4DNvU04B4p8HEc1wVr-aTLMigcRA5gfuw38s6Vv1H14RgKFnRzqnau4tz4DRp2_aUj4s-wtApervrDP8Dlie-JL_9mm6kMVM0QmZ9OtBW-huP3mDVB9ngFriSaEpbsVYoesFcJLBsKxw4DV2nrQlwhLMtuYAYvX8e7lq_DpRo5KSNk7gXzQtLbjh0q9vVKwLCxfU14MSFN8uEFh0nGjvty8ccpRCQ--t5cqx8W2VE8NK1nvpzf0F99rt-uCx_-1JLCOOYklXhXmMLSHE-naRxwE69eDiD-Vc11Tcd6WkKJ5649izgy3ooHhypPu3qgtf_Gl8KvohKTY" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/05f93dafa7.mp4?token=lQqY24jyqjXILPajnF03mXQj_kwxTadIvrzsZ_091Orq58Dw_YwU_6hzLuEMYCDi-J3QviVfn0Ls6wdDpjO2YS5J4k9uVLopI_EAW1b3b4nTqiqusZfhytxHIc3Ofl8HAg9-EyToYQWenD8FkLfVL7D8qH6LM94L787bBtpoODha6OHfmTlXzt4OXhFLHCyeMfXxMqdprCshvdBXD9pd5EQ60xU2MeTmzNdf2-PzlWVO4SiKVItH_onQ-dPKV16eOGBrl1SEW2LoOZdTVfppvmn-XvjP9ROtJShl6I0UV9eEpt54G5EApLxMwmpm6bdNDLA3eU_-hJJnXBZvfO1vkqrzuKRnrP7l4DNvU04B4p8HEc1wVr-aTLMigcRA5gfuw38s6Vv1H14RgKFnRzqnau4tz4DRp2_aUj4s-wtApervrDP8Dlie-JL_9mm6kMVM0QmZ9OtBW-huP3mDVB9ngFriSaEpbsVYoesFcJLBsKxw4DV2nrQlwhLMtuYAYvX8e7lq_DpRo5KSNk7gXzQtLbjh0q9vVKwLCxfU14MSFN8uEFh0nGjvty8ccpRCQ--t5cqx8W2VE8NK1nvpzf0F99rt-uCx_-1JLCOOYklXhXmMLSHE-naRxwE69eDiD-Vc11Tcd6WkKJ5649izgy3ooHhypPu3qgtf_Gl8KvohKTY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇳
یه بلاگر ایرانی رفته چین و ربات انسان نمای چینی رو به مبارزه طلبیده؛
حرکات ربات به قدری تمیزه که انسان واقعا از آینده جهان خایه میکنه!
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/71114" target="_blank">📅 22:16 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71113">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a66a864cef.mp4?token=hrBhv6-JCx8msKnrHO5xcXTHfqXGfwFQ61ZyJTzA7X9biMOgdj7CZswlJj4ycGyPfo5MCFFd75XCm1Dh8s_evU85KrP5qciGran5Vk6Mh4CFTAObNs_D1PaaAj3eBeSITe_050ZQADbluYtSwdF0pQtGFxER8lQdqkmfXI5lNDyHvbXviF3tveqVjy22kvSBsb24IRQlFidwu4gGPP8Yr4hwDz6PgsMcBipXlV_epNV3HSHMzcBGlLgrBkM6fjN7MaAda7i5kAwQCfQ7jftJ5ycNTBBMnl7rj1MG1XpPBogkpNQg7Jdg6ACyxdggQ6NSngQuNY_ZqU8jtjctCRNd3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a66a864cef.mp4?token=hrBhv6-JCx8msKnrHO5xcXTHfqXGfwFQ61ZyJTzA7X9biMOgdj7CZswlJj4ycGyPfo5MCFFd75XCm1Dh8s_evU85KrP5qciGran5Vk6Mh4CFTAObNs_D1PaaAj3eBeSITe_050ZQADbluYtSwdF0pQtGFxER8lQdqkmfXI5lNDyHvbXviF3tveqVjy22kvSBsb24IRQlFidwu4gGPP8Yr4hwDz6PgsMcBipXlV_epNV3HSHMzcBGlLgrBkM6fjN7MaAda7i5kAwQCfQ7jftJ5ycNTBBMnl7rj1MG1XpPBogkpNQg7Jdg6ACyxdggQ6NSngQuNY_ZqU8jtjctCRNd3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اخیرا بعضی دخترا طی یه حرکت فوق‌العاده و زیبا، دارن هرچی ژل و بوتاکس تو صورتشون بوده رو خارج میکنن تا نچرال به نظر بیان
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/71113" target="_blank">📅 21:29 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71112">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PhQ3wIREpiQUNC_aqjsGE50sV1DYpW376zPyxP9lBSPj5q7ZgZojIEvWO3osKpzqsdOgZuEnlif8cgQJXYFC6sE2mBq7Ow9R6nyTO7yVupo4Cm-Nb8k516B2o8hDEE7tRM-2EQ_NKFcdIfXOJyAiAngXVb4jl87CZYMUVoofinLIBqSehLLBgV2uAEME1lMXogGN84juTVEPeatUjS2JezZStZbCmOiGEu3aAI0788gvPOzfhXVPYclRPznJdwGRznnH2qdy05dDPLyIrSstlcOj8xMAMjAjvdNsterlhk808c8BpXV_79LLPHbU97uP8oykrTJz-T_jfWIxz_SmSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👎
قرارگاه خاتم الانبیا: حملات پیش دستانه علیه پایگاه آمریکا در اردن که در حال آماده سازی برای حملاتی علیه کشور بودند را انجام دادیم!
❌
خبر بالا که بطور گسترده در حال انتشار در رسانه هاست فیک و نادرسته، همونطور که می‌بینید سپاه پاسداران و قرارگاه خاتم‌الانبیا هیچ اطلاعیه‌ای مبنی بر حملات پیش‌دستانه منتشر نکرده
@HutNewsPlus</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71112" target="_blank">📅 21:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71111">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/phusccbV_L4bRyV0G0CQkdcu9EdFiwCg0nAIccaWHrPX65cDYzDDV4diHevNWWMqdtNK2ATRYrSuL3R0yejeXv6CBGMnghdJ9bzXvOAYK05dsaILUN8SNTo97nfWMVzIg4ItYmAbhzx-hhKxDfieO8dQFzzrEJ1zDJ3n8BoVbyiV3085ZdOuFxtPTczTxUx4f0oDd0ALO7rSMbBBRyPLkRmAne5F2SDqMnG3suWOqCbLbf43pFBZhjAfU7ajC6OjVRtnKEPcpdM9IrxHyNnTKpAVlncnzjKA3fS12yXooeDn7PQwVzSYzbUUh6pJx4iwUjycJ8CdThNEsbL-bkUWpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقام ارشد آمریکایی به کانال 12: در حال حاضر هیچ اطلاعی از وقوع آتش‌سوزی در پایگاه‌های آمریکا در اردن وجود ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71111" target="_blank">📅 21:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71110">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c74f1d2d4f.mp4?token=egdPHh5w6_0Y15zznc6qPZ6VOhx9vrCVIfNV4Ee_N0zwAyuF7cf29UipIN2IwtGn-e0LBsgCvxAHr4X7hzyEGwVCzQsC7cq9h9MnCmBSgBCKef6U9gxzv6GjFaGKL8PlPg8Hy1PT8QsWoVouefcJ86RrBV508vqxL30UE3aop8IiphBNv9-6usdiOhlyms3TmwZ1YZFiJ1A_dGMWxcUYBFmLHMM5QJITowGv-xyZdAZ7wKrYaDA7PpRTfoSdPOJ0-s24S_2JCksiv17SR0NWvTXmOA1wvYfkMn54qqnJjDEE6w3jEVCia4XE3vTcfnPtD007Jo82tsB_n_1MQ2WeZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c74f1d2d4f.mp4?token=egdPHh5w6_0Y15zznc6qPZ6VOhx9vrCVIfNV4Ee_N0zwAyuF7cf29UipIN2IwtGn-e0LBsgCvxAHr4X7hzyEGwVCzQsC7cq9h9MnCmBSgBCKef6U9gxzv6GjFaGKL8PlPg8Hy1PT8QsWoVouefcJ86RrBV508vqxL30UE3aop8IiphBNv9-6usdiOhlyms3TmwZ1YZFiJ1A_dGMWxcUYBFmLHMM5QJITowGv-xyZdAZ7wKrYaDA7PpRTfoSdPOJ0-s24S_2JCksiv17SR0NWvTXmOA1wvYfkMn54qqnJjDEE6w3jEVCia4XE3vTcfnPtD007Jo82tsB_n_1MQ2WeZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
شلیک موشک ها از ایران به سمت اردن
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/71110" target="_blank">📅 20:29 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71109">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
منابع عربی:چندین انفجار در اردن رخ داد
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71109" target="_blank">📅 20:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71108">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbf8f1e1a9.mp4?token=VucblGlJFk2Kw3-qtym2oWkaxWsnnby5Mj_F7fBcP_dkXMAhXBKbxqo2O7n0Si9M-yTN_cHUHmn-TfMFf0dvP8cPqeTNP2RmN-8sGQYyyM_B1y2osdD8sus_UHOnJuC7R-Slznu-IVz8H7noUueoYBKlXXbZnn5AwNClGX1QJZs2W9JI7pLTbZ84_pXxSLixoRhRpXRGkTs7zI8ftR5fBt8IHc5c_z_uy-XFUNmb8theQHnfdD3TTAGvXECKjCRYoxUj87_9tOKP1Lfnkj7EYEcVtoUolJ0H08lkmUn0oS4n5wYklXgNQe6JlJFxGF0auxzZpD4hDJPIo1KcdlZvzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbf8f1e1a9.mp4?token=VucblGlJFk2Kw3-qtym2oWkaxWsnnby5Mj_F7fBcP_dkXMAhXBKbxqo2O7n0Si9M-yTN_cHUHmn-TfMFf0dvP8cPqeTNP2RmN-8sGQYyyM_B1y2osdD8sus_UHOnJuC7R-Slznu-IVz8H7noUueoYBKlXXbZnn5AwNClGX1QJZs2W9JI7pLTbZ84_pXxSLixoRhRpXRGkTs7zI8ftR5fBt8IHc5c_z_uy-XFUNmb8theQHnfdD3TTAGvXECKjCRYoxUj87_9tOKP1Lfnkj7EYEcVtoUolJ0H08lkmUn0oS4n5wYklXgNQe6JlJFxGF0auxzZpD4hDJPIo1KcdlZvzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇮🇷
🇨🇳
بِسِنت درباره ایران:
آن‌ها محموله‌های نفت را به سمت چین روانه کردند. منتظر اقدامات مربوط به این موضوع در روز سه‌شنبه باشید.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/71108" target="_blank">📅 20:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71105">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64aa07a7bb.mp4?token=lv2x5XDiPFDruyyleUCPr0d1LSoafX4XyNq6DtMFWJcPGFctpk7NGstIu9IfKHR5N0rdFFLy68ZNf3mppbAoR9PEHIhsbHnW4-ruargved9u6a_2pItNEzucmBjLtgmB4sD0MqGnqthqm4I9cObYjnTTdIrCxO2vCt7VBvyKYqhTfMdOeIUQYNg5UMUJjrXAjJe9BbW-MicUSPa9l3ttVcrCs_IaWCTL-6WUNClDVHBdZuP8OsKQRghd4JaLqYzmI8AwKr9xynVQpCUS3xHIOKxQjJ-yscxBkRxGBG0BhxPpmY-ckzn88HqQNIOW46D8HBCQUuE_WnwMj_JBX2EpjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64aa07a7bb.mp4?token=lv2x5XDiPFDruyyleUCPr0d1LSoafX4XyNq6DtMFWJcPGFctpk7NGstIu9IfKHR5N0rdFFLy68ZNf3mppbAoR9PEHIhsbHnW4-ruargved9u6a_2pItNEzucmBjLtgmB4sD0MqGnqthqm4I9cObYjnTTdIrCxO2vCt7VBvyKYqhTfMdOeIUQYNg5UMUJjrXAjJe9BbW-MicUSPa9l3ttVcrCs_IaWCTL-6WUNClDVHBdZuP8OsKQRghd4JaLqYzmI8AwKr9xynVQpCUS3xHIOKxQjJ-yscxBkRxGBG0BhxPpmY-ckzn88HqQNIOW46D8HBCQUuE_WnwMj_JBX2EpjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
بابک زنجانی: دلار رو بدید دست من تا یک سال رو همین قیمت نگهش میدارم وگرنه با همین فرمون کشور تا یک سال دیگه نابود میشه.
من رو ۷ سال بدون بدهی انداختن زندان و همشم تو انفرادی بودم. همه اموالمم ازم گرفتن. وقتی آزاد شدم حتی ۱ دلار نداشتم.
با چند تا تلفن ۱ میلیارد دلار پول جور کردم و چندتا شرکت تاسیس کردم.
من میخواستم سایپا رو به قیمت ۲ میلیارد دلار بخرم که نشد ولی خودم میخوام کارخونه تولید خودرو تاسیس کنم
من توی خارج کشور بانک داشتم پولای وزارت نفت تو اون حساب بود. اونا تحریم شدن پولاشون اونجا گیر کرد گفتن تقصیر توعه و حکم اعـدام بهم دادن
تمام بانکای ایران بیان جلوی من بشینن ببینیم من بیشتر میتونم سرمایه جذب کنم یا اونا. فقط با چندتا تلفن. تا معلوم بشه کی اعتبار داره
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71105" target="_blank">📅 19:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71104">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf31ca2a30.mp4?token=D0Z2iX-zqX6EHNgQzUUM-l0sFO6hbiaUkgaLKD-yDXQIGUfDizknrnYIA8SsdwGo_RFT5UShwkLGyVQ8A7zPvhbGRw--mwThlM0WSVZS5WEd3sLNZDNCt4VSCj8QJ8RTqxKwfspasqy4RwhmBFw5RRRWUzp4djzpOAV-5NF-RLdUbwN9bksG3eyRMUczhBClm3wr7jOvkZLUWN4PsLo9UyUauuc1dX78NWX1wg2BJBrDoitakASrK_Vrs-LnfkorWedKCH8ZcTn3OY3ndvTIV_BpTi_1pMqmdbGPHr687DfLB9D-NBeUjb4JxSZy9SZ_3Gt-A-3N42X9OJZGruf7fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf31ca2a30.mp4?token=D0Z2iX-zqX6EHNgQzUUM-l0sFO6hbiaUkgaLKD-yDXQIGUfDizknrnYIA8SsdwGo_RFT5UShwkLGyVQ8A7zPvhbGRw--mwThlM0WSVZS5WEd3sLNZDNCt4VSCj8QJ8RTqxKwfspasqy4RwhmBFw5RRRWUzp4djzpOAV-5NF-RLdUbwN9bksG3eyRMUczhBClm3wr7jOvkZLUWN4PsLo9UyUauuc1dX78NWX1wg2BJBrDoitakASrK_Vrs-LnfkorWedKCH8ZcTn3OY3ndvTIV_BpTi_1pMqmdbGPHr687DfLB9D-NBeUjb4JxSZy9SZ_3Gt-A-3N42X9OJZGruf7fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
بسنت درباره ایران:
متحدان ما در امارات متحده عربی در خصوص این بانک مستقر در دبی همکاری بسیار مؤثری داشتند. اکنون ما برای متوقف کردن تمامی این جریان‌های مالی غیرقانونی، با آن‌ها وارد همکاری شده‌ایم.
ما برای رفع این مشکل با آن‌ها همکاری خواهیم کرد، چرا که بانک‌های متعددی در سیستم مالی آن‌ها فعالیت می‌کنند.
ما نمی‌خواهیم این بانک‌ها را نابود کنیم — هرچند اگر لازم باشد چنین خواهیم کرد — اما اکنون همه کشورها در این مسیر با ما همراه شده‌اند.
این پایان کار برای این رژیم است؛ آن‌ها یا باید [رفتار خود را] عادی‌سازی کنند و یا با عواقب آن روبرو شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71104" target="_blank">📅 18:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71103">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38e7eb93ff.mp4?token=kRYAXEYlZYEFbfMJKjOPj0DvuWOccmBUcUnOsDhvjRXBPjUg2vxYQAym1JMeR0ggqg5GWgbrEF_MHiq_VhuezS1eFdEyokfnjJ94Qvlf97tL1WZZmTgjumtel4QMId8asBpnrKCZkfHcqKBPt0aL53fmepH_x1NLkfw7efnEfnPoOa9ajew11pjCpi83SPDVzEp2eRco-Pa_h-RZPGFXX-1XK-HrcGIkvoueVAToyrrjL4M1XFhRF14gmaA-XEdEpx_yb5sIPu_HDauJWStmOUB5Yw6U_040BqiiKqAodmEU6mItRWKTyg3JvoWqMwyherF5peEN4dNz_zAwkEDrNFZ3xJpQoQ772wU_Ns_6kKoqk5IGeKn_SnxwtT1lC9PyXhLL8clSiMXa2wEAXWKC4YQeZ_YS3LJsRaN_nym3eEAY93re980xV-wq56IdYFLthEXWOXPc8rHMCrWengQzkn-rnNWQfArKXB1O8M-5I-tfZoD4lOs3bfovzmYK9fH65Jy9xnkGBAwrca-4c8O8wWFwTwBV0A74ZlKSTlyYlQAG-VyJFefcBZwe1WQD38OvBCw655ODW4q5Ye7qxmqmcGJHgPvw53vbEmLB8uLpbigKttuL5ZUWnl2ZTDRCFfi8BdUP6sJKvsI9Qv-YHGFvmfc6Bv6KoyprOKeRDuW3yTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38e7eb93ff.mp4?token=kRYAXEYlZYEFbfMJKjOPj0DvuWOccmBUcUnOsDhvjRXBPjUg2vxYQAym1JMeR0ggqg5GWgbrEF_MHiq_VhuezS1eFdEyokfnjJ94Qvlf97tL1WZZmTgjumtel4QMId8asBpnrKCZkfHcqKBPt0aL53fmepH_x1NLkfw7efnEfnPoOa9ajew11pjCpi83SPDVzEp2eRco-Pa_h-RZPGFXX-1XK-HrcGIkvoueVAToyrrjL4M1XFhRF14gmaA-XEdEpx_yb5sIPu_HDauJWStmOUB5Yw6U_040BqiiKqAodmEU6mItRWKTyg3JvoWqMwyherF5peEN4dNz_zAwkEDrNFZ3xJpQoQ772wU_Ns_6kKoqk5IGeKn_SnxwtT1lC9PyXhLL8clSiMXa2wEAXWKC4YQeZ_YS3LJsRaN_nym3eEAY93re980xV-wq56IdYFLthEXWOXPc8rHMCrWengQzkn-rnNWQfArKXB1O8M-5I-tfZoD4lOs3bfovzmYK9fH65Jy9xnkGBAwrca-4c8O8wWFwTwBV0A74ZlKSTlyYlQAG-VyJFefcBZwe1WQD38OvBCw655ODW4q5Ye7qxmqmcGJHgPvw53vbEmLB8uLpbigKttuL5ZUWnl2ZTDRCFfi8BdUP6sJKvsI9Qv-YHGFvmfc6Bv6KoyprOKeRDuW3yTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇺🇸
بسنت، وزیر خزانه‌داری آمریکا، درباره ایران:
همه خواهان پایان یافتن این وضعیت هستند. ۴۷ سال از عمر این رژیم شرور می‌گذرد و دنیا دیگر از دست آن‌ها به ستوه آمده است.
مردم ایران مردمی عالی هستند؛ اما رژیمی سرکوبگر بر آن‌ها حاکم است.
یا رژیم از درون تغییر خواهد کرد، یا مردم قیام خواهند کرد، و یا باید دید چه پیش می‌آید.
ما آن‌ها را از نظر اقتصادی خفه خواهیم کرد. آن‌ها در وضعیتی قرار دارند که من آن را «آرواره‌های مرگ اقتصادی» می‌نامم.
ارزش پول ملی‌شان در حال فروپاشی است و صادرات نفت آن‌ها به صفر رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71103" target="_blank">📅 18:30 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71102">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13cf8fb01d.mp4?token=QKS2H9LcN_QIPkdGmCvranc6U1EBxIzesWlDdmbM0ZFZAr6NTJwSzuHgGTQCxKA8v5q2wAzSpm2H0irHjTUInDpW0qYCpQ17mdHblN1Li4uK62tThtGN18RFTuizHa-4hivgIcqz8mQQ3f2UHOtqflYZLYrR5v_mEs9MrGbNEjuxJ2lT82SNiScKb77-wUkYEMKCcmET4l1HCHE-fmdT0gzmfGEC-0lkU4dwWxZA3dmhCCgDrm9wRgMVWLL62sMrXs-diB_SAqzs-z2Pxs8qJxzrmS-ulUqgjm2oyeUhR_Rx2hDX2RMyVa92rvKzPlh02mwaOxiWzFQQyJaUC0GUG4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13cf8fb01d.mp4?token=QKS2H9LcN_QIPkdGmCvranc6U1EBxIzesWlDdmbM0ZFZAr6NTJwSzuHgGTQCxKA8v5q2wAzSpm2H0irHjTUInDpW0qYCpQ17mdHblN1Li4uK62tThtGN18RFTuizHa-4hivgIcqz8mQQ3f2UHOtqflYZLYrR5v_mEs9MrGbNEjuxJ2lT82SNiScKb77-wUkYEMKCcmET4l1HCHE-fmdT0gzmfGEC-0lkU4dwWxZA3dmhCCgDrm9wRgMVWLL62sMrXs-diB_SAqzs-z2Pxs8qJxzrmS-ulUqgjm2oyeUhR_Rx2hDX2RMyVa92rvKzPlh02mwaOxiWzFQQyJaUC0GUG4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
بسنت، وزیر خزانه‌داری آمریکا، درباره ایران:
ما بانک دیگری را که با ایران مرتبط است، تحریم کردیم. هفته گذشته، یک بانک مصری را که پنج شعبه در دبی داشت و ۱.۸ میلیارد دلار در اختیار این رژیم قرار داده بود، تحریم کردیم.
امروز بانک دیگری را تحریم خواهیم کرد و احتمالاً هفته آینده نیز بانک دیگری را تحریم می‌کنیم.
ما به سیستم مالی می‌گوییم:
ای عوامل مخرب، ما می‌دانیم شما چه کسانی هستید. خودتان هم می‌دانید چه کسانی هستید. کارتان تمام است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71102" target="_blank">📅 18:27 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71101">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
⭕️
🇹🇷
🇮🇷
وزارت خزانه‌داری آمریکا سه نهاد مستقر در ترکیه را به‌دلیل ارتباطات مالی و فعالیت‌های مرتبط با ایران تحریم کرده است:  Golden Global Portföy Yönetimi Golden Global Varlık Kiralama Golden Global Yatırım Bankası
⏺
هم‌زمان یک مجوز عمومی برای دوره جمع‌کردن…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/71101" target="_blank">📅 18:23 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71100">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
⭕️
🇹🇷
🇮🇷
وزارت خزانه‌داری آمریکا سه نهاد مستقر در ترکیه را به‌دلیل ارتباطات مالی و فعالیت‌های مرتبط با ایران تحریم کرده است:
Golden Global Portföy Yönetimi
Golden Global Varlık Kiralama
Golden Global Yatırım Bankası
⏺
هم‌زمان یک مجوز عمومی برای دوره جمع‌کردن معاملات (wind-down) با این نهادها صادر شده است
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/71100" target="_blank">📅 18:14 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71099">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/372294672d.mp4?token=q8iHCu-d_vu-gvVakUAfSBqIwpZPdIauKN0EXozp9gCFr5IcSNiDS8hgoFOvV9K6OHNVZpD1Sa356P282dEUw4uekkQjih_ocPVNggsyQcH831jlh4ISc38zlUkm10Q3u_-gZ94dog-5e-9MjPeZAABeKLUtaehR_L5mfOSpdCKB-X1FDaVHeecT2cEjQTM-n7kF_cT5UAo-NPI_gO5lo_yTKZIEauA6Kj5DOrJ6wmJuIzToidq8e_vEOmLQK9z_B5qX3XPOW2nKHZmVj5MpaGMdiul6lBQLNx58nQRmoDlroP1ki0glhWiEJnuxb6nYZCdpicMsQMQIIqp7OaXSuE8bUU_FM0JqEcVxEEOgicAqq7BInWxvlxk5cBXcW1FwbPljkIU7SvUKpBAm86G8Xg71RitR_UdWmrI9mycvOKsS1mn0AoZHR5iOt3Hw0gFRayC5EgAxKBUbHFYnemuU7Y-h23Pv1-ZwS38l2NGLvMVbs7MlZgQZ3kFbGxaJ5jthYYBrv9zh56iKwS1BKW6hD3znHDhVek-DAwQa2VHRxsCs8X1AGaeFenDlrRsRERPZTiBwB2GfJpy-fYfqWtFjd-yT7ShaPIs-n-_s_C3h2_SCc65uuXp1HE_cPxayItScHtQRq2SW7ex5bT0-zsymXz1O7_Gr6-syOFfA25R--cI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/372294672d.mp4?token=q8iHCu-d_vu-gvVakUAfSBqIwpZPdIauKN0EXozp9gCFr5IcSNiDS8hgoFOvV9K6OHNVZpD1Sa356P282dEUw4uekkQjih_ocPVNggsyQcH831jlh4ISc38zlUkm10Q3u_-gZ94dog-5e-9MjPeZAABeKLUtaehR_L5mfOSpdCKB-X1FDaVHeecT2cEjQTM-n7kF_cT5UAo-NPI_gO5lo_yTKZIEauA6Kj5DOrJ6wmJuIzToidq8e_vEOmLQK9z_B5qX3XPOW2nKHZmVj5MpaGMdiul6lBQLNx58nQRmoDlroP1ki0glhWiEJnuxb6nYZCdpicMsQMQIIqp7OaXSuE8bUU_FM0JqEcVxEEOgicAqq7BInWxvlxk5cBXcW1FwbPljkIU7SvUKpBAm86G8Xg71RitR_UdWmrI9mycvOKsS1mn0AoZHR5iOt3Hw0gFRayC5EgAxKBUbHFYnemuU7Y-h23Pv1-ZwS38l2NGLvMVbs7MlZgQZ3kFbGxaJ5jthYYBrv9zh56iKwS1BKW6hD3znHDhVek-DAwQa2VHRxsCs8X1AGaeFenDlrRsRERPZTiBwB2GfJpy-fYfqWtFjd-yT7ShaPIs-n-_s_C3h2_SCc65uuXp1HE_cPxayItScHtQRq2SW7ex5bT0-zsymXz1O7_Gr6-syOFfA25R--cI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
تیزر دوم فصل اول سریال هری پاتر که از کریسمس 2027 قراره پخش بشه
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71099" target="_blank">📅 18:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71098">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71098" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/71098" target="_blank">📅 18:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71097">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bnp9TY0pUoLwQUe7ATuY_ZluL2HAb_4P1Tp3fhEyzI5yQbWw7wZUksASiAvnL80qsFEQcPNwZz95gcHT_cZ4AJt0RMs_9usFyFGUIpJb5ptIrfMIjQR6JbeKfaDHKROmJxP3Jf32af6J41fr7v2TKsVA_qlJmSZJCVUCMjRDFhaL3m5bx82mxRYPIszOmlC1gMN2apPF4fRvkTylLTmiBSAcHF4mLSh5BZ9Zq2LcEbFtrobtZO-6aJMp3qQZ4YgFJ0Dounk-9nJFMl_z3cYzFatI9ga5HFuSevrxgPu7WwHr0tl7EuZWyehzIfamjl6V6BdXrKmuPrMPsXiHcGeK1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب
⚽️
پاری‌سن‌ژرمن
🆚
موناکو
⚽️
را در سایت بین‌المللی
TrexBet
پیش بینی کنید.
📊
مونامو ۲ برد | ۱ تساوی | ۲ شکست | ۹ گل زده
پاریس ۲ برد | ۱ تساوی | ۲ شکست | ۱۰ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71097" target="_blank">📅 18:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71096">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">〰️
سنت‌کام:
بیش از ۲۶۰۰ تفنگدار دریایی و سرباز نیروی دریایی آمریکا، بر روی ناو جنگی USS Boxer (LHD 4) مستقر هستند و این ناو جنگی در حال حاضر در خاورمیانه در حال انجام ماموریت است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/71096" target="_blank">📅 17:32 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71095">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fcc841fe5.mp4?token=Q5zy1b8tE6kr5UTcc6oe_xTqJjNNrTRuvdynbkmzqNq0CRru8SFO8A8nNsBAI2jw88x01ADbjlW_BZfQxp5NN16cPLuEnu0FxBZZd7FlxZ-k3LY0N5G_zy7mZyRug7qjOXBiaZ94Nu5rJnFGldW_XVWQ-oNBgR5Fq7qLemUU8137E5cNy20VVbxGmMlkn_hjJu2wUXXWBRU1VEwcrsuXnNdtkJxGqnr1FPn_mocTUfv6C7kYVrSgVA3ISo28AuWQ3aHw61enJjYBaPWGskpdVdF5a5LqrTKTWOF3iq04GuC_JjYHvdXjbK5_DYL7CyrpP3-MbV1EsNJ_8oLnuK7bdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fcc841fe5.mp4?token=Q5zy1b8tE6kr5UTcc6oe_xTqJjNNrTRuvdynbkmzqNq0CRru8SFO8A8nNsBAI2jw88x01ADbjlW_BZfQxp5NN16cPLuEnu0FxBZZd7FlxZ-k3LY0N5G_zy7mZyRug7qjOXBiaZ94Nu5rJnFGldW_XVWQ-oNBgR5Fq7qLemUU8137E5cNy20VVbxGmMlkn_hjJu2wUXXWBRU1VEwcrsuXnNdtkJxGqnr1FPn_mocTUfv6C7kYVrSgVA3ISo28AuWQ3aHw61enJjYBaPWGskpdVdF5a5LqrTKTWOF3iq04GuC_JjYHvdXjbK5_DYL7CyrpP3-MbV1EsNJ_8oLnuK7bdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ببینید از خانمی که داره از تجربیات رفتن خودش به تور کویر میگه...
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71095" target="_blank">📅 17:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71094">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf229661bf.mp4?token=aJ4kZuIjolgVxYUGCxTZ9SX3ZWYOi2S4AFGjV0BKi5xUtDs3VmJnKm9FxWSX0piLKQvEaNSUM4tZdX4eYwtbSE4r51IBhItQG5CwJYJREW4zZAG2C4d5mBWAj7aEHHA5XuZ5wybyYhZmDlwQeEAzvlMnmuEn-Th7CkaEJGHrSwX1ThDfZN_-U6uPBB8WbO-Yenwi5AHunhxbWZtG_44BbXsPb_Cw5G_rJtKOMglW5CDcWlgX-jG5xdmjHztIQMdFefBbBrAk6eUrDTz7HzkKLDqT_HplziFIIJPGd6CGkRrmlF5ksXWdSLBqA8hQTY3711rjA64T83XhO1YvQW77FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf229661bf.mp4?token=aJ4kZuIjolgVxYUGCxTZ9SX3ZWYOi2S4AFGjV0BKi5xUtDs3VmJnKm9FxWSX0piLKQvEaNSUM4tZdX4eYwtbSE4r51IBhItQG5CwJYJREW4zZAG2C4d5mBWAj7aEHHA5XuZ5wybyYhZmDlwQeEAzvlMnmuEn-Th7CkaEJGHrSwX1ThDfZN_-U6uPBB8WbO-Yenwi5AHunhxbWZtG_44BbXsPb_Cw5G_rJtKOMglW5CDcWlgX-jG5xdmjHztIQMdFefBbBrAk6eUrDTz7HzkKLDqT_HplziFIIJPGd6CGkRrmlF5ksXWdSLBqA8hQTY3711rjA64T83XhO1YvQW77FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
سامسونگ A17 که یکی از ضعیف‌ترین و تخمی‌ترین‌ گوشی‌های بازار به حساب میاد، قیمتش به 100 میلیون تومن رسیده.
البته این قیمت واسه دیروزه و امروز احتمالا گرونتر شده.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71094" target="_blank">📅 16:30 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71093">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc7b61838f.mp4?token=rGzos_7xVNXQHoaX2Obpyq1qvOSm059ojHPy18xlu-qs0XitAqOas_68G_ZkGP5JzV9LgCJezYV5tMV5WF7ljtnYud93TrLcI_mK221FScOqm6-yjNLpTOxEf95rtSdptsGNMSE_RcPFyYIH65CjhxPu4ulKO85oFFqjSYnqGNCirZ5mm6HRQGwb1EsAZ_XQUP0_9m8rEhqTqrTW4UDHrFpMS4QaMNg0k_jN4bUl_kqIx1bxQjhly0B25-yE5q8hwaW89eFSEZOr61IbmTLOQu_w5YLGlaKLhFJjBHZKt0iqVwPh_UZntOvxw3V7DJYwxhAHSZnsy6xdbAFCUYrsLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc7b61838f.mp4?token=rGzos_7xVNXQHoaX2Obpyq1qvOSm059ojHPy18xlu-qs0XitAqOas_68G_ZkGP5JzV9LgCJezYV5tMV5WF7ljtnYud93TrLcI_mK221FScOqm6-yjNLpTOxEf95rtSdptsGNMSE_RcPFyYIH65CjhxPu4ulKO85oFFqjSYnqGNCirZ5mm6HRQGwb1EsAZ_XQUP0_9m8rEhqTqrTW4UDHrFpMS4QaMNg0k_jN4bUl_kqIx1bxQjhly0B25-yE5q8hwaW89eFSEZOr61IbmTLOQu_w5YLGlaKLhFJjBHZKt0iqVwPh_UZntOvxw3V7DJYwxhAHSZnsy6xdbAFCUYrsLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
یک راننده کامیون:
الان کنار مرز پاکستان هستیم میخوایم رد بشیم اجازه نمیدن.
رفتیم پیش رئیس گمرک میگه طرف پاکستانی اجازه ورود نمیده.
پاکستان گفته به ازای هر ماشین باید دو میلیارد تعرفه بدین.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71093" target="_blank">📅 16:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71092">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45bdb5a184.mp4?token=emTUTX-mZD-lKzRRcPu94y52W_-HvBN9SBFqaRgnfQhufz6wUGfmbgjhRmxiB0oZvSkJvznjSIrrN4ysDJO67A_RrtTocxSFq53maU-AGb3YO_z4TpSHeML-5c0cAH1_enpeQaEV7DMeg266DrszsQGstVUuIaqWWnScp8CNzkHEcWm0dUcGEXe_cYsdnRBtxbJ0jf0vmvDVKflFe_M6sY2Mkf0DfHJYAW6DnPtJHWCy3HE1utCDqame9gBCs0pxKqjMRGQUIRm5UIMxeiB6NAyXBh87efLtnOHwy2bisNKhahc72HM1Vlu4bqShNfAVrrtbk-n4PkfxNs271WBHWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45bdb5a184.mp4?token=emTUTX-mZD-lKzRRcPu94y52W_-HvBN9SBFqaRgnfQhufz6wUGfmbgjhRmxiB0oZvSkJvznjSIrrN4ysDJO67A_RrtTocxSFq53maU-AGb3YO_z4TpSHeML-5c0cAH1_enpeQaEV7DMeg266DrszsQGstVUuIaqWWnScp8CNzkHEcWm0dUcGEXe_cYsdnRBtxbJ0jf0vmvDVKflFe_M6sY2Mkf0DfHJYAW6DnPtJHWCy3HE1utCDqame9gBCs0pxKqjMRGQUIRm5UIMxeiB6NAyXBh87efLtnOHwy2bisNKhahc72HM1Vlu4bqShNfAVrrtbk-n4PkfxNs271WBHWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
یه دختر حامی حکومت:
فک کردین اومدم از قیمت دلار آه و ناله کنم؟ نه اومدم پاره‌اش کنم!
رزق و روزی دست خداست نه آمریکا، دلار قیمتش عوض شده، خدای ما که عوض نشده.
قیمت دلار هر چقدرم بشه، باز روزی مارو خدا می‌رسونه، منم اعتراض دارم ولی ناامیدی تزریق نمی کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71092" target="_blank">📅 15:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71091">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2be4c50b6.mp4?token=OeX6HZcY033XSD04aIcOmiY3T-nLNGgarptNDAEOPtQOlm1IKxQBloC7QY23RNGFHrYfMjATZGJ-q_PgfL1TmCLoY_8-syVg318IOZ-7SJ88wUYGvReAfcX9IhL3t5NfX6YCPqNtmj8mwI8Ka6YvZJalDzOArSATo2_yWtdMRs9Q379MUuAb4j_SJlNhw9yx5-z--CfcZaFdhItu71qmx-hb2ohL0i8U7ojGtuevZA31DZSOs4SiK_QrQZd3Nqjwzt9cmPv_dNOZQF1WRgZd14bDlBOIRcrin8P221KI6pYcy_e4UciuwgBJsC_XntNyNI3vzN_goYxyNcUpuOit0jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2be4c50b6.mp4?token=OeX6HZcY033XSD04aIcOmiY3T-nLNGgarptNDAEOPtQOlm1IKxQBloC7QY23RNGFHrYfMjATZGJ-q_PgfL1TmCLoY_8-syVg318IOZ-7SJ88wUYGvReAfcX9IhL3t5NfX6YCPqNtmj8mwI8Ka6YvZJalDzOArSATo2_yWtdMRs9Q379MUuAb4j_SJlNhw9yx5-z--CfcZaFdhItu71qmx-hb2ohL0i8U7ojGtuevZA31DZSOs4SiK_QrQZd3Nqjwzt9cmPv_dNOZQF1WRgZd14bDlBOIRcrin8P221KI6pYcy_e4UciuwgBJsC_XntNyNI3vzN_goYxyNcUpuOit0jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🚀
🇰🇼
روز گذشته، یک پهپاد انتحاری که توسط ارتش جمهوری اسلامی پرتاب شده بود، یکی از واحدهای برج مسکونی الدیره در شهر کویت را هدف قرار داد. این اصابت باعث آتش‌ سوزی و تخریب کامل آن واحد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71091" target="_blank">📅 14:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71090">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a0b6b730d.mp4?token=LAUVMmtPhfF8rG78u0w7X5rQwBKizjFawU-mIBc3lsWDlw5IL-XwAZtLonHpKzT1CYEk-wJ2ZD-5Pdn7sHBgAutItXkEw3HUs_IuUjX6SrJR0ENEkOUiIJvUHeo5T6QEpr544LhyiwangaBqvPdik0LqRzaGCzU4BuIGmTfU5BEFuksbR9I0SNtKQP3uCd7hT1klTuSxlzu5V-AtMxwRJwSfEnvgEypmj6T1HIwsfIwgiT6cJ0B4ZBjcb9QZ8ki8Zfp3uXvC9MTXpd2iKsVp75kFyf6vR95M-bHYIFBcOQxpQ7eT4FhF6yPTXx7UaVcBiJ6BwW-G2LSpA5pYBjNp_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a0b6b730d.mp4?token=LAUVMmtPhfF8rG78u0w7X5rQwBKizjFawU-mIBc3lsWDlw5IL-XwAZtLonHpKzT1CYEk-wJ2ZD-5Pdn7sHBgAutItXkEw3HUs_IuUjX6SrJR0ENEkOUiIJvUHeo5T6QEpr544LhyiwangaBqvPdik0LqRzaGCzU4BuIGmTfU5BEFuksbR9I0SNtKQP3uCd7hT1klTuSxlzu5V-AtMxwRJwSfEnvgEypmj6T1HIwsfIwgiT6cJ0B4ZBjcb9QZ8ki8Zfp3uXvC9MTXpd2iKsVp75kFyf6vR95M-bHYIFBcOQxpQ7eT4FhF6yPTXx7UaVcBiJ6BwW-G2LSpA5pYBjNp_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
❌
🇦🇪
با افزایش تحریم‌های آمریکا تجار و بازرگانان می‌گویند امارات از بارگیری لنج‌های ایرانی خودداری می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71090" target="_blank">📅 14:31 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71089">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28ac9cc9fe.mp4?token=SMU-T-CK68QGSVxlMfFRLwq8c_NG6CtJLGP1u7tYm3dXNyrmMZqJFEchHt3B7bvpoQPZiui0A2oc2dPO0dgLaf1Qp2HEoEU_6nNP8iebVEmdQAy7KnX5Jb9i6XSqjOK2lYF8YBEWn0sT1dGL9eBYd0wcCO0AEvJmfxnOkUoJCqWF9IELp9IaD-wQIoBJ6FiPeh0qnsbVSweM3GrL5OWTtdAkCsZ8zZlzPvA8XBX_io5NSI51H_rBSfFqrzt2Ccf7ok_jjoe2-F6kmKeiL3LCVBvzn-1s1hCf8NUtwS6jj0NaWG45acfUKNFtG1T1C-nrj75ZDOVNbo2WQzbUv84Eqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28ac9cc9fe.mp4?token=SMU-T-CK68QGSVxlMfFRLwq8c_NG6CtJLGP1u7tYm3dXNyrmMZqJFEchHt3B7bvpoQPZiui0A2oc2dPO0dgLaf1Qp2HEoEU_6nNP8iebVEmdQAy7KnX5Jb9i6XSqjOK2lYF8YBEWn0sT1dGL9eBYd0wcCO0AEvJmfxnOkUoJCqWF9IELp9IaD-wQIoBJ6FiPeh0qnsbVSweM3GrL5OWTtdAkCsZ8zZlzPvA8XBX_io5NSI51H_rBSfFqrzt2Ccf7ok_jjoe2-F6kmKeiL3LCVBvzn-1s1hCf8NUtwS6jj0NaWG45acfUKNFtG1T1C-nrj75ZDOVNbo2WQzbUv84Eqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇵🇱
🚂
برخورد قطار با یک کامیون در گذرگاه راه‌آهن در گدانسک لهستان.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71089" target="_blank">📅 13:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71088">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b60a6b68b8.mp4?token=l6_2cS8vfGLsrgZW5_1DZptxVthvPhOU0yYimgdgoLn-KoDnF27x-QwdRqx1vh1dAOmn4jytwzoZGyWtobzRIumbWz3tDGKJK0jnh--zTSbxeucRWlQOF0m5YL_Gokjs35tZqHfj0STUSn9Qi2e79rdDQaJm1QZiyz934wd8kZ6HZNp_3frfk5Dk2KKTCiL27VSR1SrvWl52E_tX0876dbv9jKammW6uuR7UH6TUfyCtaXZQ3ia_GTv-sZHNrVXe3Wgpsj29J_FUW1JSw00dSAgB1HT4pAno2ON8u7ejKxmZlRgk7wfo-rUlm4pRLsnUbDc-n4hjaQnuAsVI985hSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b60a6b68b8.mp4?token=l6_2cS8vfGLsrgZW5_1DZptxVthvPhOU0yYimgdgoLn-KoDnF27x-QwdRqx1vh1dAOmn4jytwzoZGyWtobzRIumbWz3tDGKJK0jnh--zTSbxeucRWlQOF0m5YL_Gokjs35tZqHfj0STUSn9Qi2e79rdDQaJm1QZiyz934wd8kZ6HZNp_3frfk5Dk2KKTCiL27VSR1SrvWl52E_tX0876dbv9jKammW6uuR7UH6TUfyCtaXZQ3ia_GTv-sZHNrVXe3Wgpsj29J_FUW1JSw00dSAgB1HT4pAno2ON8u7ejKxmZlRgk7wfo-rUlm4pRLsnUbDc-n4hjaQnuAsVI985hSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرف با رفیقش رفته دور دور الهیه و به یه دختره شماره دادن،
و حالا اولین پیامی که دختره براشون فرستاده
😟
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71088" target="_blank">📅 13:49 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71087">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71087" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71087" target="_blank">📅 13:49 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71086">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lTXrZA1-XeT0qN__m9Nn6GqXTurY5L_wU3tnPjIoSclRQSoezT8Ewswg1q4zuEeFwmA7F5541pI0KjjOoNn0Lz8Y_RFW-I25LZca5IuFmIt815f_t8kGpaiCm_21r7wv9k-2KNVl7iIGncO_m6S1dCbNU1o5FkLXPVjFEYSjXpAw17T2HzpcvHmuumYVEc9NZsvnc0CkNeurfkqnX9oU83haIqxJf4ey3GbpVjt6jQmgo0PqEJJrBMXC7OU1vtA7ymisugVGqcid8H_yKnqTNIfRshO0J4DeyXyvquh3esmcKB-I_qwUN9lMhOFlqwVaaCrJaEmXf9-IcMI-M5C83g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب رئال بتیس
🆚
رئال مادرید را در سایت بین المللی
TrexBet
پیش بینی کنید
📊
نگاهی به آمار دو تیم در ۵ بازی اخیر
رئال بتیس: ۲ برد، ۱ تساوی، ۲ شکست در ۵ بازی
رئال مادرید: ۵ برد در ۵ بازی اخیر
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71086" target="_blank">📅 13:49 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71085">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4843999275.mp4?token=d3OXAQF3r1Me2TdgnB8pnavd7-2iFHMGI5qshNxnYwhVzlU-iaspSG9NQz2x59x_OxKAFKgcMcTm7rhBsd92_S99dKLs6HAa9FNDPeuKe6N46nS3wQul6c3_BXzp7mIPgXZfkr2EOBofOZ3YBCOwcnzZxWU9HM8zM73biD6xAkchmSRByDxxxmbFf7a-1VwWEr2zw96jyFCF55-RKhT97f7m4SOR5oIeQTalc-Up5ongswh-Bd0oeiLExQ9t1nnBw8hEb3l_hUNvXGpMHDUqvaopbZQFzMNn_C6t54agPHprBehn7S1sBHP3qbI6uEEUSunVrMy_xw1ktASJA9G_XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4843999275.mp4?token=d3OXAQF3r1Me2TdgnB8pnavd7-2iFHMGI5qshNxnYwhVzlU-iaspSG9NQz2x59x_OxKAFKgcMcTm7rhBsd92_S99dKLs6HAa9FNDPeuKe6N46nS3wQul6c3_BXzp7mIPgXZfkr2EOBofOZ3YBCOwcnzZxWU9HM8zM73biD6xAkchmSRByDxxxmbFf7a-1VwWEr2zw96jyFCF55-RKhT97f7m4SOR5oIeQTalc-Up5ongswh-Bd0oeiLExQ9t1nnBw8hEb3l_hUNvXGpMHDUqvaopbZQFzMNn_C6t54agPHprBehn7S1sBHP3qbI6uEEUSunVrMy_xw1ktASJA9G_XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
پرزیدنت ترامپ در رسانه‌های اجتماعی پرسید: «مردم ایران کی قیام می‌کنند و می‌جنگند؟» آیا دولت در حال بررسی مسلح کردن یا ارائه، سایر حمایت‌های مستقیم از مخالفان ایرانی است؟
🇺🇸
ونس:
ها ها ها... مگر پیتر دوسی امروز صبح این سوال را در فاکس نیوز نپرسید؟
سوال خیلی خوبی است.
و چیزی که رئیس جمهور گفت(درجواب به این سوال) دقیقاً همان چیزی است که من می‌خواهم بگویم.
قرار نیست درمورد این سوال صحبت کنم!
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71085" target="_blank">📅 13:10 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71084">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gKv9zqEsyNzIfNORbEIEoMspkj4o4My1Au7RVfnBg9RF1N7_O8JIPHOarG92lfefDzb_Rx20_T0H_tj5X-VtbUHXeGi5BKIjwwLZw2MMUl50ZzX4OMbhS8VRusgw1UTdUCEr89KJYh_9RCLKwb4KGAyHZ7re0CPuo3i-6e7ntRbN4n5lbk1dmDjvLpc81iWEXJM6PmTaty0fJovosMKXV7cFOZy72pFt_Fz2ADrKjWMceJqzwaA1NDzyQh28U6G2DA-icSzHO90oSZym1vnrXw6lab3JLfHSoukJxFutElGbVrAi2M0CzKHlZXMPHIrNLJM2A7QeJmmME6VhzAb_fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عرزشی با این پست به شدت میسوزه
😃
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71084" target="_blank">📅 12:12 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71083">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0edd50344.mp4?token=sSywWnFI1YhjEhZh9tdl0Ht-CMuyRQcvyHZFAC7VZvU5pwDDxSg5m6b_caS233oQa-l48CoNWJJSuO23CuXe6g7H7Yh_OM1sBnbZDHd8ZlopXyl0RjuHJ1HZ3FTriDuatTWaqWdsrBvie1oIi2sadhlnPJ1yh9DmawcWSqe1G9vPVIIY2UdOS3mmzEETtQo1mnbIPzs0ZTFiVrrXVC-Wbw4iVFbrHYPnNNXp5C9hUtIfyrdUuGTuJyoXC0h0hL0sWM7ZB703Vuj-R5v3SXtDKL2gGEggbAh9rVtVikBtWuLjEdKJiUQezvr5WywaSO-3CGgmKNE9bz0MzgFCM7PkAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0edd50344.mp4?token=sSywWnFI1YhjEhZh9tdl0Ht-CMuyRQcvyHZFAC7VZvU5pwDDxSg5m6b_caS233oQa-l48CoNWJJSuO23CuXe6g7H7Yh_OM1sBnbZDHd8ZlopXyl0RjuHJ1HZ3FTriDuatTWaqWdsrBvie1oIi2sadhlnPJ1yh9DmawcWSqe1G9vPVIIY2UdOS3mmzEETtQo1mnbIPzs0ZTFiVrrXVC-Wbw4iVFbrHYPnNNXp5C9hUtIfyrdUuGTuJyoXC0h0hL0sWM7ZB703Vuj-R5v3SXtDKL2gGEggbAh9rVtVikBtWuLjEdKJiUQezvr5WywaSO-3CGgmKNE9bz0MzgFCM7PkAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ویدیو وایرال شده از طرفدار حکومت
🎙
خبرنگار:
از قیمت دلار خبر داری ؟
🇮🇷
طرفدار حکومت:
بله شده 200 و خورده ای
🎙
خبرنگار:
با این قیمت پس چرا اومدی اجتماعات ؟
🇮🇷
طرفدار حکومت:
دیگه باید قدرت تفکیک داشته باشید تو ذهنتون و قیمت دلار یه چیزه و بیرون اومدن یه چیز
اصلا اگه امنیت ما نباشه شما میتونید راجب قیمت دلار فکر بکنید؟ نه نمیتونید!
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71083" target="_blank">📅 12:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71082">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">⏺
ویدیو وایرال شده از اعتراض یه زن کارتون خواب:
به عنوان یک کارتون خواب که 20 ساله دارم این زندگی تجربه میکنم!
شما مسئولین که مردان خدا هستید شما دیگه چرا؟
تو دانشگاه رشته حقوق خوندم
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71082" target="_blank">📅 11:34 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71081">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d18ffbfe89.mp4?token=ELtcVK7shPa5wLSnzuS7efpJLDz6TQmWLWRUy0O3t-jfsjNreb2q0indKLhbqPkQXCYn9jOSRftaGMfNd6ii7ZPvuWy7NZRa20f6dcyFdfFth0pyfDvyR7md_q1KUZfzn5NH6HINdIirjp1SbqtQqJ1YMH6TfO-xESDfRRSclMRo_JBwJB3uIfW-i6Gc34wOb5WWGxy0zbnyVfouERsJXL6_Tcg7odJnMPAhgfc91XCXDLg5XrAHufyyRXLMbKpjUTU95p02QBOW7pG80MUAZXTfqPRTrXQaugVKwUafS-6tgIKvJaOP-aQWWQm0U8y1RcApdCxQjhtQ1t8A3oSd4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d18ffbfe89.mp4?token=ELtcVK7shPa5wLSnzuS7efpJLDz6TQmWLWRUy0O3t-jfsjNreb2q0indKLhbqPkQXCYn9jOSRftaGMfNd6ii7ZPvuWy7NZRa20f6dcyFdfFth0pyfDvyR7md_q1KUZfzn5NH6HINdIirjp1SbqtQqJ1YMH6TfO-xESDfRRSclMRo_JBwJB3uIfW-i6Gc34wOb5WWGxy0zbnyVfouERsJXL6_Tcg7odJnMPAhgfc91XCXDLg5XrAHufyyRXLMbKpjUTU95p02QBOW7pG80MUAZXTfqPRTrXQaugVKwUafS-6tgIKvJaOP-aQWWQm0U8y1RcApdCxQjhtQ1t8A3oSd4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پسره دوست دخترشو برده تو کوچه پس کوچه ها بهش رانندگی یاد بده
آخرش هردو غافلگیر شدن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71081" target="_blank">📅 11:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71078">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bc34fe3de.mp4?token=tJC-dfVQgv2r13I9126mJMecaSCyma1TaJiVItDDhcqb-gCTWB2tknhah3WDYeCvlFOWLQLZ6CVQ0_7KLKaeK8rK2xIWLjwA2-tFMFJnElYmk0LEkboBPthX7cWXELsv0wll1mX-dJi1O_VN9ZAhWIYq26uF-0R4dbiPw0lR21TkVc7OfvV7kWKiUZ_DKFuNOQU1hMyIH8BvQb0rc9QNezaZFsUBTNBjq5xFc0Thq6LBpq7BvLK7iPMUlcTd4trOG3-dR22aS7pCgskESYorziBkxJffsPJGiHNRumY7bJ8ipPPy4tc5GD3DZwrujEIjeh8MzSQJBZvM8KbIGx9v1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bc34fe3de.mp4?token=tJC-dfVQgv2r13I9126mJMecaSCyma1TaJiVItDDhcqb-gCTWB2tknhah3WDYeCvlFOWLQLZ6CVQ0_7KLKaeK8rK2xIWLjwA2-tFMFJnElYmk0LEkboBPthX7cWXELsv0wll1mX-dJi1O_VN9ZAhWIYq26uF-0R4dbiPw0lR21TkVc7OfvV7kWKiUZ_DKFuNOQU1hMyIH8BvQb0rc9QNezaZFsUBTNBjq5xFc0Thq6LBpq7BvLK7iPMUlcTd4trOG3-dR22aS7pCgskESYorziBkxJffsPJGiHNRumY7bJ8ipPPy4tc5GD3DZwrujEIjeh8MzSQJBZvM8KbIGx9v1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
توی دزفول چند تا دزد میرن توی یه خونه مجهز به وسایل ضد سرقت و 3 کیلو طلایی که توی اون خونه بوده و قاحب‌خونه قصد داشته باهاش طلا فروشی بزنه رو میدزدن!
صاحب خونه شب قبلش توی اینستاگرام گفته بوده که میخواد طلا فروشی راه بندازه که این حرفا رسیده به گوش دزدا ؛
فردای همون روزی که این حرف رو زده وقتی صاحب خونه خانومش که باردار بوده رو وقتی میبره بیرون یه هوایی بخوره دزدا میریزن تو خونه و طلا ها رو میبرن.
حالا صاحب خونه گفته که هرکسی هر سرنخی از این دزدا داشته باشه و بهم بده ، 10 میلیارد تومن بهش پاداش میدم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/71078" target="_blank">📅 10:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71077">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0def551e36.mp4?token=OMX4CR3punJg4DMdtKdZ-uVd4UwnaNpvb95pODilWqtQjAIXSW7wly-44qsYjenTF9kusgE-BVWOd4v_TmXjuLOtPcqOBKuu9L_HHy2ndwUvArHwYWBomHOlEnpTbtbrXKnUhF9BssslAOS6wGb6K61-NCiktrQscrb0S3xwfAvbN499UPw_dX0xRXi-gIAujxzt-oaUmBa5i7VvkL-Va-rUPGkR_OnTxkbzfrcSNIXakrxC594JDOnU357rmCVIBAf7W3JQC22qA53dvEl0kNBEeWrhJQHzC2yAhh19vVHLJN6jYGHZVOgo4nyE-d5ga08f9SVWtiJoYq8oj_jQIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0def551e36.mp4?token=OMX4CR3punJg4DMdtKdZ-uVd4UwnaNpvb95pODilWqtQjAIXSW7wly-44qsYjenTF9kusgE-BVWOd4v_TmXjuLOtPcqOBKuu9L_HHy2ndwUvArHwYWBomHOlEnpTbtbrXKnUhF9BssslAOS6wGb6K61-NCiktrQscrb0S3xwfAvbN499UPw_dX0xRXi-gIAujxzt-oaUmBa5i7VvkL-Va-rUPGkR_OnTxkbzfrcSNIXakrxC594JDOnU357rmCVIBAf7W3JQC22qA53dvEl0kNBEeWrhJQHzC2yAhh19vVHLJN6jYGHZVOgo4nyE-d5ga08f9SVWtiJoYq8oj_jQIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز یه دختره داشت تو قزوين واسه خودش قدم میزد؛
که یهو یه پیرمرده خواست مزاحمش بشه ولی بعد که فهمید طرف پسر نیست، عذرخواهی کرد و رفت
😳
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/71077" target="_blank">📅 10:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71076">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4ba13b0e17.mp4?token=UekEd9BxvjeorY8jx0d-DRsSK-_3jSbsyWaKPcOjPflMfREgS9CgnD0rc9iuosLGuUwJZ_-B_dqiqGMfbMD0PgEgr3EUPngJ2byRvyRq0Fb7A7UPF7DGpNN7_YgtzvVtx0Su_xI3cglYMu79b3pTqQgY407LVJLG7gPwEK5WdPUjlLdzKehPiE1SrgHNddtRRhFz7bYN7-YudvRUmJa9rghD1l8CBiLiTbChrhe8_072AQZMIGUt-Ix6QuX-Lu5eVACHBCvh8Rkdie4seXWlov8P2kACJw_4EDdxaxJKbI9hvAnqskCSGLc_guYizKEYAGMyzX2WJSf87P1eS5i56Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4ba13b0e17.mp4?token=UekEd9BxvjeorY8jx0d-DRsSK-_3jSbsyWaKPcOjPflMfREgS9CgnD0rc9iuosLGuUwJZ_-B_dqiqGMfbMD0PgEgr3EUPngJ2byRvyRq0Fb7A7UPF7DGpNN7_YgtzvVtx0Su_xI3cglYMu79b3pTqQgY407LVJLG7gPwEK5WdPUjlLdzKehPiE1SrgHNddtRRhFz7bYN7-YudvRUmJa9rghD1l8CBiLiTbChrhe8_072AQZMIGUt-Ix6QuX-Lu5eVACHBCvh8Rkdie4seXWlov8P2kACJw_4EDdxaxJKbI9hvAnqskCSGLc_guYizKEYAGMyzX2WJSf87P1eS5i56Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه دستگیری یه قاتل فراری در ایرانه
:
قاتل با چاقو مامورا رو میزنه و داشت فرار میکرد که یکی از مامورا عین راموس تکل زد و طرف افتاد.
بعدش یکی دیگه از مامورا ویلچر برداشت و میکوبید تو سر و بدن قاتل تا بیفته زمین، هر لحظه این فیلم عجیب‌تر میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71076" target="_blank">📅 09:32 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71075">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQJGDnkR9mXMC_XeYJGJWzsjoGJGveH8lbb32Nd0h-DVAOMLLUtHKOLAFxq7QCer-X_d5djWcoJxt7Rh9ME_ICPCzIfaLeIsIomCcn1iTWrWnzdOQksL3BcLbfGTy1tYTzoomN1piHbqRw9v0OqVB3g7snVeBNLKqrHQhYngDTSNBT6F_r1qewy5MUC0Y_Vy7-JYdMHNAZdZBY9h78VuwqaUqCZnlBGZh38oVdinsr6LzWiS4QmkuaDEPVFgFFAvwDviTlbEypfhSH9R28oh0PIt37XwHRRpzzZ7H5LLasl26CijFZfK0hZPd6YHnuAcWqdsoVcc6XjJMLR-syVc-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇺🇸
⭕️
#فوری
؛اسکات بسنت وزیر خزانه‌داری آمریکا:
اتحادیه اروپا رسماً به «عملیات طرد اقتصادی» (Operation Economic Outcast) پیوسته است و ما از موضع قاطع و زودهنگام آن‌ها قدردانی می‌کنیم.
ایالات متحده در کنار متحدان خود قاطعانه ایستاده است تا اطمینان حاصل کند که رژیم جنایتکار ایران نمی‌تواند از سیستم مالی جهانی برای تأمین مالی جاه‌طلبی‌های هسته‌ای، برنامه‌های تسلیحاتی و نیروهای نیابتی تروریستی خود بهره‌برداری کند.
جهان پیام روشنی به رژیم ایران می‌فرستد: ما تا زمانی که آخرین شریان حیاتی مالی باقی‌مانده قطع نشود، از تلاش دست نخواهیم کشید.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71075" target="_blank">📅 09:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71074">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71074" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/71074" target="_blank">📅 01:26 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71073">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0uBjoyU_yH88afBsots2syoxPMQtCVsKVjnqgiQWlks9xnZHcGB9lS6pfnlr6-m7GKnGZcmR74HC3kBG2HgTaJlL6QuOFlz2VBbzlK_CcPgEdyRh2ndDka95QEgi4lYaYZugPP72KJ3oKJFpHQZQzRQkote_o-PLW5NJ5lOvO5V1kLa6jteOZmHJpZnlJUchGjr5GiSpCs4-gjdKH4nSj05B-TlJ7VfM7GecT90dkP44W3yga_VQwO5VrtEFy5Xn4lHdb64rwDcu2MFTDD2uFYJNei_EixVg8SF1__g8XYweNqyM_F2aPt4-vUJgIzAxMoyEvYEeXiMuLGUJYVtVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/71073" target="_blank">📅 01:26 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71072">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🇮🇷
نایا:ایران چندین موشک به سمت کشتی ها در تنگه هرمز شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/71072" target="_blank">📅 01:14 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71071">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c46c090035.mp4?token=fKHVImRXIVbxLQllNoCmCnYxlUchwM5VuBpCFh144ytpC6QBl0HbzlFb8ZivvubIzDIOIEkwGqe_UynB-ryUPMXm7l3TFbhhVQeKdo7nyMLgEma9kFvRhxIFvoaRkYvKNFG9BvRlwtnIkJEOCcJJjkYodA1qXXKNQUpzPTwiiZUWqLofjIMdIT-kt6ESGnBJhmdRnmF3gUO_W9sCj6_BNuaVqmHYSgFJYgz9V8nzUKGV1cOSp9t-L5AV7SVzZfJ-YnmX5Ix-3zLV9DMpCtP1-ljN_OaQcZoTFxHnSXHemB6Zrs__lePel_tWihj0XIZpfUwyaQjJUlEEl1ZPZFc6tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c46c090035.mp4?token=fKHVImRXIVbxLQllNoCmCnYxlUchwM5VuBpCFh144ytpC6QBl0HbzlFb8ZivvubIzDIOIEkwGqe_UynB-ryUPMXm7l3TFbhhVQeKdo7nyMLgEma9kFvRhxIFvoaRkYvKNFG9BvRlwtnIkJEOCcJJjkYodA1qXXKNQUpzPTwiiZUWqLofjIMdIT-kt6ESGnBJhmdRnmF3gUO_W9sCj6_BNuaVqmHYSgFJYgz9V8nzUKGV1cOSp9t-L5AV7SVzZfJ-YnmX5Ix-3zLV9DMpCtP1-ljN_OaQcZoTFxHnSXHemB6Zrs__lePel_tWihj0XIZpfUwyaQjJUlEEl1ZPZFc6tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پورمحمدی:
انسداد تنگه هرمز، برنامه‌ریزی شهید پاکپور بود.
شهید پاکپور پیش‌بینی کرده بود که جنگ با ترور او شروع می‌شود.
شهید پاکپور برنامه‌ریزی کرده بود که اگر جنگ آغاز شد و او دستوری صادر نکرد، فرماندهان ۲۰ دقیقه بعد شلیک کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/71071" target="_blank">📅 00:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71070">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46300e7107.mp4?token=BtN5H3tPX3mwYi2VIWI071Bxwj4b4rLA5XYRAuvm2d7TYSJtnPxGYSuhIZXtL9qt8eXm6bvS3laHEYl_Xi1t6P32PPZqZgZlQTgMv8gbdR6caprKbMoeQPLkCt7YiNE_y5QamLBBj5pD1XJmTNeB5ADOYPcf0wwlt4Q0U1Nkgfg45n__C40jfx1c04cFUJZLA0GfBm1y2C2XmJksiBVT7INQgrEc7WL-3o7iBJ_iotjY16CZrUUBAeKy_MHOsYV5zdn1dWqddU0tq1MDCcEHB2e9mvNK7shUaoA9VNhWOaN7UDsDy2BHJJSbAIqky9rUluQimQaXmpnD1YGr-tBgXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46300e7107.mp4?token=BtN5H3tPX3mwYi2VIWI071Bxwj4b4rLA5XYRAuvm2d7TYSJtnPxGYSuhIZXtL9qt8eXm6bvS3laHEYl_Xi1t6P32PPZqZgZlQTgMv8gbdR6caprKbMoeQPLkCt7YiNE_y5QamLBBj5pD1XJmTNeB5ADOYPcf0wwlt4Q0U1Nkgfg45n__C40jfx1c04cFUJZLA0GfBm1y2C2XmJksiBVT7INQgrEc7WL-3o7iBJ_iotjY16CZrUUBAeKy_MHOsYV5zdn1dWqddU0tq1MDCcEHB2e9mvNK7shUaoA9VNhWOaN7UDsDy2BHJJSbAIqky9rUluQimQaXmpnD1YGr-tBgXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
چندشب پیش تو شیراز یه دعوای عجیب رخ داد؛
دوتا دختر با ماشین میزنن به ماشینِ دوتا پسر؛ بعد گفتن ما مقصر نيستيم و داشتن فرار میکردن!
پسرها هم گفتن چون بی‌ادبی کردی، باید بمونی خسارت بدی، بخاطر همین پریدن رو کاپوت ماشینِ دختره که فرار نکنه!
این وسط یه پیرمرده هم خیلی بی‌دلیل از دختره کتک خورد...
تهشم دختره گفت دیگه این موضوع واسم مهم نیست چون زنگ زدم شوهرم سروان شهریزی، الان میاد کون همه‌تون رو پاره میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/71070" target="_blank">📅 23:31 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71069">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/876466a913.mp4?token=OkGAQ6wMEyhxp17sKMjiGdL2mpVJjZ_seKJBLCa2rsncAKeISAdkM2ZA0ckN9JHy2kUMlRDEcSWG35SlkjbROgMDgQYtVkb8l8UBnZHZjQkbbrNBO6OXvz9UpdS2E9dNaMYB6ViA_XFmjijL5RXHHMjNKx4uWpZ5UVF__Lp__BGT-EWoSq1ipUQ7MgTtJNNbcgw-LDrgWaPEfdIwpbMhxfv7kG7whFOL5prtZQNgo03JYoM1qtSeS9jRAdG9sAO-WeYpOl5eYmtgX2-Tn9abwdx9kUA9vH21MsgTU8AawS5fH0SLXgpAzFrw7qRIP4eOfKhbSNxwQdT2C5YO7sq-6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/876466a913.mp4?token=OkGAQ6wMEyhxp17sKMjiGdL2mpVJjZ_seKJBLCa2rsncAKeISAdkM2ZA0ckN9JHy2kUMlRDEcSWG35SlkjbROgMDgQYtVkb8l8UBnZHZjQkbbrNBO6OXvz9UpdS2E9dNaMYB6ViA_XFmjijL5RXHHMjNKx4uWpZ5UVF__Lp__BGT-EWoSq1ipUQ7MgTtJNNbcgw-LDrgWaPEfdIwpbMhxfv7kG7whFOL5prtZQNgo03JYoM1qtSeS9jRAdG9sAO-WeYpOl5eYmtgX2-Tn9abwdx9kUA9vH21MsgTU8AawS5fH0SLXgpAzFrw7qRIP4eOfKhbSNxwQdT2C5YO7sq-6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طبق گفته خانم دکتر؛ دیگه خوردن واژن خانم‌ها نه تنها دیگه نباید باعث خجالت شما بشه بلکه پر ازخاصیت و فواید زیادیه که تاحالا درجریان نبودیم!
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/71069" target="_blank">📅 23:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71068">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aWqCffQ8Er8wuFyRBK-YlE5HXtBsA4Jck1gV9GJOO7VtCaWG0DID7RvCTWzlZBBmTB1cvTQRPh4fKO4t3mLskz6_xEkLKttzWf5Pb5VvQvnXM5qnKx-ymZhSBI2fYbTajIlgM9l2cC0r2kw46HI95op-5rEezjl-DM5HRsP8JbKE-Cs4ruymdv72cLZ0DrfO9mIzWvsJZDQxECxc0Eomq_8GLPVOtMCfeT3fcDrNpSW0crUjntuNbS30ImWdMPXZ9u_Xk8vfk9i_qX7f2qf7Pr6-XaJE-Lk0Y1ctJ69sjIc6yJiIBfPvgC11tUmTqlW1pJGbejFFMrpSlSDI73M-TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالیبافِ:
قهرمان، محکم‌تر «شورت» (Short) کن؛ طوری که انگار آینده‌ی شغلی‌ات به آن بستگی دارد (چون واقعاً هم همین‌طور است).
یا اینکه سطح ذخایر را به زیر «منطقه خطر» برسان و فرو ریختنِ آن حفره‌های عظیم (و البته نابودیِ شغل خودت) را تماشا کن.
یا هم به درگاه خدایانِ نمکِ «برایان ماوند» (Bryan Mound) دعا کن.
دنیا که از همین حالا بساط پاپ‌کورنش را آماده کرده است :)
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/71068" target="_blank">📅 22:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71067">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f701b5944.mp4?token=Zi9x-9vcyeXgU8LaxNvgnYIU_PEWDiEwLqN22QZvH2Zh8dLdibIJqZZ4VkpVnPi40-aVPsyWWbHx_pEUiWyCrsk10EqZDi3Faox44SdpKqgHcZKJVK9a7Xr7Qf6QqNpug-Alg2aOfF7KBsYK0c1LKMwU5hyjY0AFI1DEsYkMpWLK7uRpr0NMq-o8xlvMupXqz7lXr2oLkWMzyg-J0O_S9wtTrx50yayRm95xh-GVFWKixImrnYkMiyvZrUNgOhNPGIeSRml3y0m1LAkwqUfIkeDbg8FLFyj0685bRPHD4Tl52cqqjVFaYiqsbXrSyRBwEYvsmJaoOaxw9v9jVn11Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f701b5944.mp4?token=Zi9x-9vcyeXgU8LaxNvgnYIU_PEWDiEwLqN22QZvH2Zh8dLdibIJqZZ4VkpVnPi40-aVPsyWWbHx_pEUiWyCrsk10EqZDi3Faox44SdpKqgHcZKJVK9a7Xr7Qf6QqNpug-Alg2aOfF7KBsYK0c1LKMwU5hyjY0AFI1DEsYkMpWLK7uRpr0NMq-o8xlvMupXqz7lXr2oLkWMzyg-J0O_S9wtTrx50yayRm95xh-GVFWKixImrnYkMiyvZrUNgOhNPGIeSRml3y0m1LAkwqUfIkeDbg8FLFyj0685bRPHD4Tl52cqqjVFaYiqsbXrSyRBwEYvsmJaoOaxw9v9jVn11Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
ارتش اسرائیل تپه علی طاهر در جنوب لبنان را فتح کرد و کنترل آن را در دست گرفت.
ارتش اسرائیل پاکسازی دو مسیر تونل زیرزمینی حزب‌الله در رشته‌کوه علی طاهر در جنوب لبنان را به پایان رسانده و در تلاش برای خنثی‌سازی آنهاست.
لشکر ۳۶ کنترل عملیاتی رشته‌کوه را در بالا و پایین زمین به دست گرفت و آن را از وجود شبه‌نظامیان پاکسازی کرد. برخی کشته و برخی دیگر فرار کردند. خنثی‌سازی زیرساخت‌های پاکسازی‌شده در حال انجام است.
در داخل، نیروها مراکز فرماندهی، اتاق‌های تسلیحات، اتاق‌های ژنراتور، محل‌های زندگی، دوش‌ها و یک آشپزخانه را یافتند -- که به شبه‌نظامیان اجازه می‌داد عملیات جنگی را انجام دهند و برای مدت طولانی در زیر زمین بمانند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71067" target="_blank">📅 22:13 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71066">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rc5HAZTctLsgH0B7L_2YFHZVx6VL-FCSc09gOP_m2yUMS_Vwi9Ek-GQK2SF6OOLpiDU5wjyksWdNQFQYPnUCGn_r-IjDgMTfW7JJqHX1eoQxsMdVBOco4RiS9suRoWU2e1eyBGcdt19UF43kYB2uLPrWTwoq8dMr7oqvq1hQCkMBRMce9bkdu4TeLl1JBp1qD01cF6GyUVzaR3NRxcxp8tt0w7GLL5f2eERaISXWO13bQGikIuBfnEQgOKYn5DtPx1IxvFBF3BumK-4KBgM44Sj27uPv1S5ZRoq2dB_dbBDmBp3K1CkBuYi73-DMqG-p0Ub6cPVPSNZu3xYf2BVUcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خرید حضوری با اسنپ‌پی، یه خرید معمولی نیست؛ شانس بردن BMW داره!
😎
🚗
با اسنپ‌پی می‌تونی از بیش از ۲۰ هزار فروشگاه حضوری خرید کنی و هزینه‌اش رو ۴ قسطه و بدون سود و کارمزد پرداخت کنی.
🎉
🥳
همه‌اش همین نیست؛
۵ هفته، ۵ برنده، ۵ جایزه در هر هفته هم در انتظارته:
🏆
۵ گرم طلا
📱
گوشی Galaxy S25FE
📱
گوشی iPhone 17
💻
لپ‌تاپ MacBook Air M4
🎮
کنسول PS5
این شهریور، حضوری خرید کن و شانس بردنت رو بیشتر کن:
👇
👇
👇
https://l.snpy.ir/iozfb
https://l.snpy.ir/iozfb
https://l.snpy.ir/iozfb</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71066" target="_blank">📅 22:13 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71065">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af33ae7319.mp4?token=thHqyNxX_uioUg1bhj7SVTmKdWpO59zuHeiqf0_ecM2nAyYf5EdHCi-cjbB_6brs90Ax9l1utU83tObUUVpKTBMuFv2NvKwDpOp1A_A1xOE4xZ8PZT_efct4Ed3BRyBTyWnci1EQSrEtk9d2bKuwE19l7DmNINYQZw5X9kz8_4CHY7Y2zlS7mVdkkHw6RJjLwGAyqX5wuk_diyziQcqxM9eCEJt-DP7J7iYUWnQBBRP6M3utcMdIchtbWSdyVBDrPAI2GidLoPrAlbdHUdpjBpS3NXyrDFoKJ2Ui5fKxD8fEiWy4q56soT6znSCDS61NcAi32-r0NUVrnagYxme4LAJDtgqOH4RdRRwbxDw8CVz9xbMJn6TManXf2dsuVIv8JnlJef7CaUQwNR8M-skDQJ6Adjo4udU2svIJyITisjbEbBM-0aNQJwp_ByzE4RhZgMNKu_r0E7GKHf5sKQJ0Ei2JJ5-_2g81UbV12DeEGiE1HkdzlAXupVQpY7lwPhkCSBHv4fzLhb19fsdq-1phb1jMdBuZPUPS0Fk4UXgo0iv-OzRk4A9Ng8E8Mt5Wyk5tCj3WEe1_9XoY-HAkDjb03PrODSC6l4Ps8wUlJgnAmD2j2weEv-VOQhTvNGXdhnQ23dB7yr56KYAtyBfUWWNEh6sSlsSUatKrYDysa3Q-n3E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af33ae7319.mp4?token=thHqyNxX_uioUg1bhj7SVTmKdWpO59zuHeiqf0_ecM2nAyYf5EdHCi-cjbB_6brs90Ax9l1utU83tObUUVpKTBMuFv2NvKwDpOp1A_A1xOE4xZ8PZT_efct4Ed3BRyBTyWnci1EQSrEtk9d2bKuwE19l7DmNINYQZw5X9kz8_4CHY7Y2zlS7mVdkkHw6RJjLwGAyqX5wuk_diyziQcqxM9eCEJt-DP7J7iYUWnQBBRP6M3utcMdIchtbWSdyVBDrPAI2GidLoPrAlbdHUdpjBpS3NXyrDFoKJ2Ui5fKxD8fEiWy4q56soT6znSCDS61NcAi32-r0NUVrnagYxme4LAJDtgqOH4RdRRwbxDw8CVz9xbMJn6TManXf2dsuVIv8JnlJef7CaUQwNR8M-skDQJ6Adjo4udU2svIJyITisjbEbBM-0aNQJwp_ByzE4RhZgMNKu_r0E7GKHf5sKQJ0Ei2JJ5-_2g81UbV12DeEGiE1HkdzlAXupVQpY7lwPhkCSBHv4fzLhb19fsdq-1phb1jMdBuZPUPS0Fk4UXgo0iv-OzRk4A9Ng8E8Mt5Wyk5tCj3WEe1_9XoY-HAkDjb03PrODSC6l4Ps8wUlJgnAmD2j2weEv-VOQhTvNGXdhnQ23dB7yr56KYAtyBfUWWNEh6sSlsSUatKrYDysa3Q-n3E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شیر ترامپ هم اومد به بازار
😳
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/71065" target="_blank">📅 21:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71064">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40c15e0881.mp4?token=SBiMiqr-dbGE3H2xnb3llFCYdG5CG-pK8Y8pcco7HF8j_eYBzoZgraOYsVmz9A9lI1eJq5c6iFP87Xg_wdAZ1DAC_9c9n8AI240PELiRx9_ctpH3lXwmzoynxJ01XMlB3bLe0-tdUByLAIlSpoDfZyqiwEpA-a6myy2Y1X1xIIM5fpeBwq0x9Rnq6ZwJFwD1dKpiV0Z2H3Osae9C-ZqG5iEdi2UA90r1WKKQ02K6nKtjVS9HuzcH2SXwPFAYH6YJcMDXeZRpYmnUK6ZRi1_SG3gkT0d7Ca1AdjaUrppzKgRqEEuiskt-SBUwsYkYeJrC7N9XOi1xzV1V3IK8HKqj3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40c15e0881.mp4?token=SBiMiqr-dbGE3H2xnb3llFCYdG5CG-pK8Y8pcco7HF8j_eYBzoZgraOYsVmz9A9lI1eJq5c6iFP87Xg_wdAZ1DAC_9c9n8AI240PELiRx9_ctpH3lXwmzoynxJ01XMlB3bLe0-tdUByLAIlSpoDfZyqiwEpA-a6myy2Y1X1xIIM5fpeBwq0x9Rnq6ZwJFwD1dKpiV0Z2H3Osae9C-ZqG5iEdi2UA90r1WKKQ02K6nKtjVS9HuzcH2SXwPFAYH6YJcMDXeZRpYmnUK6ZRi1_SG3gkT0d7Ca1AdjaUrppzKgRqEEuiskt-SBUwsYkYeJrC7N9XOi1xzV1V3IK8HKqj3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
رقص عجیب «حسن حسین خانی» مداح نزدیک به حکومت  در حالی عجیب  و  با شلوارک! تو یک  ویلا با آهنگ شماعی زاده
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/71064" target="_blank">📅 20:46 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71063">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0392122fc9.mp4?token=l2elL4U62i_IR2u9quADusLrQt-t5ObQYeQigX9cJ6T7iNMF0SQbzbdHQmUJRMlcosJ3iW_fgTHoSsZmPoCOI1uamZm2Sgqssx2wEho_SWtIwrII3BBIIhVhUnuMD4jDPkKebUAbI6Xk8vk5SIM1UPpm2vBpuoLEr9d_ODYmHp8Yoq9gZGEH6956pW1oPMo0-08UvrL0dKp_yLdieKwhGu9tL5C6W_0bsacHq9WthozQHmdyrd0cdhyDdr3JCzVbHhfNURinzG4cZnOamqO4fk-Cug0WvWTxSDwBmuaZPp-n4EWGnfItyRtAqqwhQ-8RWLqIiCl70k3N9nNUxbwyAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0392122fc9.mp4?token=l2elL4U62i_IR2u9quADusLrQt-t5ObQYeQigX9cJ6T7iNMF0SQbzbdHQmUJRMlcosJ3iW_fgTHoSsZmPoCOI1uamZm2Sgqssx2wEho_SWtIwrII3BBIIhVhUnuMD4jDPkKebUAbI6Xk8vk5SIM1UPpm2vBpuoLEr9d_ODYmHp8Yoq9gZGEH6956pW1oPMo0-08UvrL0dKp_yLdieKwhGu9tL5C6W_0bsacHq9WthozQHmdyrd0cdhyDdr3JCzVbHhfNURinzG4cZnOamqO4fk-Cug0WvWTxSDwBmuaZPp-n4EWGnfItyRtAqqwhQ-8RWLqIiCl70k3N9nNUxbwyAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
#فوری
؛نخست‌وزیر نتانیاهو درباره ایران:
من به توانایی‌مان برای از میان برداشتنِ یک‌بار برای همیشهٔ این تهدید ــ یعنی سرنگونی این رژیم ــ اطمینان کامل دارم.
این همان مأموریت اصلی است که همچنان پیشِ رو داریم، اما به تحقق آن نزدیک شده‌ایم. این کار غیرممکن نیست؛ بلکه کاملاً دست‌یافتنی است.
آن‌ها بی‌دلیل از حمله به ما پرهیز نمی‌کنند؛ آن‌ها به همه حمله می‌کنند، جز ما. آن‌ها از قدرت ما، توان بازوی ما و عزم راسخ ما آگاهند.
من خطاب به دشمنانمان به‌طور کلی می‌گویم: با ما درنیفتید. اگر درسی گرفته‌اید، بدانید که نباید با ما دربیفتید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/71063" target="_blank">📅 19:55 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71062">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
شلیک موشک/پهباد از سیریک به سمت کشتی ها در تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71062" target="_blank">📅 19:31 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71061">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/veV9sDt2yUwv79728uZFt_i-gSfXw-8UP-pvglmjeaUjZJqThEBZwZM_ijorsq2nR8-DdpRhqTXrUOEI2tRYx-2u-tn15QMbRiJ6OdDxi8wK07-U2Au5X6jPPEQgnctJrlU6OacYX0IiJe_eeA4M9rw4MKa_CwWdbd240KHV96FS9LB0VAYBLZ2SoUAwabE736kgAm0qnFNwmaP_RptFUZAZkWviVvrH5n7Hq3e8TBD0SA22vKnp2pFV6jJpwz2vvz0E-vkKgamzwHQZ7xwJ-5zwxjAEq3SLzUq67H_EYRcbrCBfzGip-A3TMZ4mcInSre1w2DSFRUCWHapHMqsRRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
ترامپ در تروث:
برای آن مشتی خائنِ پست‌فطرت که از گزارش دقیق عملیات نظامی ما در ایران خودداری می‌کنند، باید بگویم که ما ذخایر تقریباً نامحدودی از مهمات با کیفیت متوسط تا عالی در اختیار داریم؛ بسیار فراتر از آنچه ممکن است برای این عملیات یا هر جنگ احتمالی دیگری (که وقوع آن بسیار بعید است!) نیاز داشته باشیم.
علاوه بر این، ما در حال تولید مهمات با حجمی بی‌سابقه هستیم. ما در حال انباشت و آماده‌سازی برای مقابله با هرگونه وضعیت پیش‌بینی‌نشده‌ای هستیم که ممکن است رخ دهد.
ما این مهمات را برای خودمان — یعنی ایالات متحده — نگه می‌داریم و فعلاً به دیگران نمی‌فروشیم، هرچند فروش به متحدان به‌زودی از سر گرفته خواهد شد.
همچنین، لازم است بدانید که دولت بایدن حجم بسیار بیشتری از مهمات را — بدون دریافت هیچ‌گونه هزینه‌ای — به اوکراین واگذار کرد، که این مقدار بسیار فراتر از مهماتی است که ما در ایران به کار گرفته‌ایم.
صدها میلیارد دلار کمک رایگان به اوکراین و ناتو اعطا شد؛ هزینه‌هایی که اگر از اروپایی‌ها خواسته می‌شد، خودشان آن را می‌پرداختند.
با این حال، ما آن پول را مطالبه خواهیم کرد، هرچند با کمی تأخیر!
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/71061" target="_blank">📅 18:52 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71060">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d21cce2e5e.mp4?token=knDV3Etp_Yq8nzl9Q-ztLPN8atzpXoWJV262sB73AokKOmZ4LwDDKOWKTW4nmV_R2bvsPrvFmzrRVfacjmGYIx4-71pbxv3JvCmolvL632kKGWIGK7Vkq3KYBhbJPVty77ryplO_7oDw_Su4oHy6r1gSv6d1old9mfF9h9M6KQdSNqSgF0e61gsC6OAGfw-EevoSPqmUHVKkItxAxvfadu63-CDUpOy8BobhT1De6WqZYpforL0KbMdI6_pfDpLHMog2f3NvP67_zYQtyGWEaHYYwBTB-w9vlvsOqRBln59D3MoaNfEp78eY4J78sSL0-qItJ6_rJNcbYe-RxDSE9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d21cce2e5e.mp4?token=knDV3Etp_Yq8nzl9Q-ztLPN8atzpXoWJV262sB73AokKOmZ4LwDDKOWKTW4nmV_R2bvsPrvFmzrRVfacjmGYIx4-71pbxv3JvCmolvL632kKGWIGK7Vkq3KYBhbJPVty77ryplO_7oDw_Su4oHy6r1gSv6d1old9mfF9h9M6KQdSNqSgF0e61gsC6OAGfw-EevoSPqmUHVKkItxAxvfadu63-CDUpOy8BobhT1De6WqZYpforL0KbMdI6_pfDpLHMog2f3NvP67_zYQtyGWEaHYYwBTB-w9vlvsOqRBln59D3MoaNfEp78eY4J78sSL0-qItJ6_rJNcbYe-RxDSE9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
کسانی که دوستتان دارند، شما را فردی خوش‌برخورد، شوخ‌طبع، سخاوتمند و بذله‌گو می‌دانند؛ اما دیگران می‌گویند که شما سخت‌گیر، متکبر، مغرور و حتی بی‌رحم هستید. به نظر شما، کدام‌یک از این توصیفات درست است و کدام نادرست؟
❤️
شاهنشاه آریامهر:
بی‌رحم؟ گمان نمی‌کنم.
متکبر؟ قطعاً نه.
مغرور؟ شاید کمی. اما در مورد کشورم—و آنچه به دست آمده است
نمی‌توانم شخصاً دچار غرور شوم، چرا که انسانی مؤمن هستم. من عمیقاً به خدا ایمان دارم و اهل عرفانم؛ پس چگونه ممکن است مغرور باشم؟
انسان در پیشگاه ذات ازلی، هیچ است؛ مطلقاً هیچ؛ گویی اصلاً وجود ندارد.
البته با نگاهی به دستاوردهای این کشور، قطعاً دلیلی برای احساس غرور و سربلندی وجود دارد.
اما بی‌رحمی؟ این ویژگی من نیست؛ این نهادهای حکومتی هستند که باید عمل کنند.
وظیفه آن‌هاست که کسانی را که قصد آسیب رساندن به این کشور را دارند شناسایی و خنثی کنند. اگر نام این کار بی‌رحمی است... خب، در آن صورت باید بپذیریم که در این مورد با هم اختلاف‌نظر داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71060" target="_blank">📅 18:26 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71059">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/259e330a05.mp4?token=rDwMLiwbaMgoDLAvTOX4JRCgrdDbtW5xwPndpQIzw3EOGrGfTNQLiJeYndqNn4ivuSG6XVlwQyeCDLHtXRUfhmtGBlfGGpPAfhwuwpPWD4pEGfRzhDK-9zptAPh7riCf2_75xz0wtPHSbwUE0xWs42iRp_jMAKlg-eJ9i6FzwVw_LYJfpBWkUlnsTkHVKXrgLdnE-4RiTZsxAUCuyAfPYy-mr957HjWCci6iAjj5cOwJgPvQVKaofB3qNfqtndPxfmk_V0aBC_vB_LTlGP3BOE0NsvGNF3021hEp7kGqicpeILetygS8H3_LnO7vK5AoamYDCPRn0Q-foklFqR-7aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/259e330a05.mp4?token=rDwMLiwbaMgoDLAvTOX4JRCgrdDbtW5xwPndpQIzw3EOGrGfTNQLiJeYndqNn4ivuSG6XVlwQyeCDLHtXRUfhmtGBlfGGpPAfhwuwpPWD4pEGfRzhDK-9zptAPh7riCf2_75xz0wtPHSbwUE0xWs42iRp_jMAKlg-eJ9i6FzwVw_LYJfpBWkUlnsTkHVKXrgLdnE-4RiTZsxAUCuyAfPYy-mr957HjWCci6iAjj5cOwJgPvQVKaofB3qNfqtndPxfmk_V0aBC_vB_LTlGP3BOE0NsvGNF3021hEp7kGqicpeILetygS8H3_LnO7vK5AoamYDCPRn0Q-foklFqR-7aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
صحبت‌های این پسر درباره‌ی اونایی که میگن کسایی که ریش ندارن کونی هستن رو با هم ببینیم:
کدوم مادرجنده‌ای اینو باب کرده که هر کی که ریش‌وسیبیل نمیذاره، کونه؟
شما برو فیلم سوپرا رو نگاه کن، عمو جانی کونش هم یدونه مو نداره، چه برسه به صورتش.
ریشو کسایی میذارن که ترس از کون‌شون دارن، اونایی که عقده دارن و بچگی کون‌شون گذاشن، ریش میذارن.
خیلیا ریش دارن ولی صد مرتبه از کونیا بدتر هستن
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71059" target="_blank">📅 18:16 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71058">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71058" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71058" target="_blank">📅 18:16 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71057">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehEe6Tqqv5QWakTNhOwATGkYoYO1aqccgXAls3WVw9_hz1zjFxjBjicWXZGioo8AeLlCxohZ8SqCsk6mEA_59lQdg24uqTd0JAsrgGZg69MNJQRAzH0gmIgto5IAY6ushnCerCGi7AxiMllrDuos8RPPDjsyF_-Gx3qp-UZF8vAGGxhLqux1HCw76rRwtCNrFaqSKa5oZZCEWH7dPn__PujaLOO4GVhMpJ9iNwQsM4VZV4bDrY3SOmm-9SIWF66hUBo6B3jNpEHklvdKjSgt3IuL9t7Kkve551Jny8ZKQnbJp0M0xHXSlkjRrgmNjo5_BWQDfNXeV25E87Ph8eyBhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیرکس‌ بت می‌بردت وسط هیجان
US Open!
🎾
🔥
🦖
رقابت‌های نفس‌گیر، امتیازهای سرنوشت‌ساز و هیجانی که تا آخرین ضربه ادامه داره!
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71057" target="_blank">📅 18:16 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71055">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uQ3SPsaCZPmTrvYQBmg0XiYVF58QVZOn6i8DNZjNqsaDKEERno1SJ1dn6Py9_f2t9qfCOJUqcyP1ms3SOxKzKhbGFDg9WzMbjMS6WBNfnKSSXL26fvxwzeAZTFNSqFWREada7fC4Yy6yYJ5ZfxiCTQ1WDYvoTngdciMTf4YQJPwIwWCmSI0Um5lFy135yfejysbcThaVcDwwSQuzxCtMy9A5u8dVG_iseptnSXgkhvYKO9zHezsoYijW9SiBs9OjaGyZSoYggoRbRWryHeCrkkCE9i5MgMfFTdqrXs2SLNv4dDrUCSXvqCX4MCFv43GdfSdVXBrRtPE-0P60IT4XLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
💬
🙂
پست جدید تلگرام در پلتفرم ایکس:
حس و حال بامزه‌ای دارم، شاید بعداً عکس‌های نودم رو منتشر کنم!
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71055" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71054">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_1ooZmXihuImHOJFFqOUCzotaZ3l5nw01LqA51Ux_vpjBwa-PguLPtr0nnyMQqbCQuII-7hcJxSIM4Hsbk6Zgg2U658oMQmCM7CkwumWKnYwTIyqg-A8ogv8I9WqsiZPiQhR3rl_5xmPxu4cvIi4BURfLDDO9JnTqu6qh7YEwJg9K5rP2wmRnPuHZY0efIiemi0T3FcYv79Pa-sorvAR07AimAfLZjU7YhsIjXfssLfIqwikA6Y_RR9wq5OOXweCLQvoaUNf5DHzNm_Mu2ZTWEUgSnmsNpA0SqHx-ZyNO1FmCrBpDO70Q_OpatmvxrNY27YW9ZQXzCCn-xloTOQ9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
جمهوری اسلامی کشته شدن سه خلبان نظامی در حملات آمریکا در دو شب گذشته را تأیید کرد.
اسامی: مجتبی باقری و حامد اوکاتی (خلبانان هوانیروز/هواپیمایی نیروی دریایی) و حسین مهدویان (خلبان نیروی هوایی).
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71054" target="_blank">📅 16:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71053">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03924aeb44.mp4?token=AFtuNV-11RyA9Mm3HxOGPg4-ROC8ZedLyWwTJ6QmbuLd9USA60KoGt57gbsZwlK2a3_iqQ_5sB2ywP1yGj3qRhpTtzUavIn_L7bPFO5j8Ib2hMrJkEOLtHm0sq8dUV6ORZcZ-ovDkR0XSEy-esDR7-HI-eLXSQf_D9LmK0dnNY7J4HTin3rbp20SDQ2g-90S1yXWmuQdI38KVYeGOsjYBTkJUQmtmi7Znrp1j0RPVFV53fVklAhZuhj2RSOvtoyRqhSJgTXCJVMRitRZG90El_6KDDABBTFUzr0sG-vnqmaeZ4pf2lvP_aDp9z70vWnWdkt6nfQJA-_6nCmDizviaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03924aeb44.mp4?token=AFtuNV-11RyA9Mm3HxOGPg4-ROC8ZedLyWwTJ6QmbuLd9USA60KoGt57gbsZwlK2a3_iqQ_5sB2ywP1yGj3qRhpTtzUavIn_L7bPFO5j8Ib2hMrJkEOLtHm0sq8dUV6ORZcZ-ovDkR0XSEy-esDR7-HI-eLXSQf_D9LmK0dnNY7J4HTin3rbp20SDQ2g-90S1yXWmuQdI38KVYeGOsjYBTkJUQmtmi7Znrp1j0RPVFV53fVklAhZuhj2RSOvtoyRqhSJgTXCJVMRitRZG90El_6KDDABBTFUzr0sG-vnqmaeZ4pf2lvP_aDp9z70vWnWdkt6nfQJA-_6nCmDizviaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تو ایتا و روبیکا با انتشار این فیلم نوشتن سامانه پدافند لیزری جدید اومده و همه موشکا و پهپادای آمریکا رو با لیزر زده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71053" target="_blank">📅 16:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71051">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94edb900f7.mp4?token=D1EmR-0AMSicGSjKxa_va37xQoXK99wvVuPRr081IPh0JdMJZX1pUGp4vuyZVasj2XjGHGnE3cWZydVGR6whVUoVQmQQuU_pyAGjfM5dKkU1oPzbdOH94LqfHjTV51Tatn0Vg9NlqtpuYj-gNqqwe9tLgxc46DQSKaSVeMP3mG6GXQW2f87OKAO95UU7YNoriEuR6Px3Z2M3cTBD-9QsayTNs30lerrhje5cToxU5UHY1o9_VL3qmuhHwpsdkTynJjKi-O2gfUfVw6JxjXTLfFITVvFmtyHsS7edO_OLmlJ5Ubtxk3R0_jFYePWdlyXR0iIplcXv90h3AkRLwv3LQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94edb900f7.mp4?token=D1EmR-0AMSicGSjKxa_va37xQoXK99wvVuPRr081IPh0JdMJZX1pUGp4vuyZVasj2XjGHGnE3cWZydVGR6whVUoVQmQQuU_pyAGjfM5dKkU1oPzbdOH94LqfHjTV51Tatn0Vg9NlqtpuYj-gNqqwe9tLgxc46DQSKaSVeMP3mG6GXQW2f87OKAO95UU7YNoriEuR6Px3Z2M3cTBD-9QsayTNs30lerrhje5cToxU5UHY1o9_VL3qmuhHwpsdkTynJjKi-O2gfUfVw6JxjXTLfFITVvFmtyHsS7edO_OLmlJ5Ubtxk3R0_jFYePWdlyXR0iIplcXv90h3AkRLwv3LQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این کلیپ از یه دختره که سر سفره عقد، آقای داماد رو سورپرایز کرد و گفت من مهریه نمی‌خوام و فقط 14 شاخه گل بنویسید
؛
هیچی دیگه پسره دیروز طلاقش داد و اونم با 14 شاخه گل رز طبیعی قرمز  یک جلد قرآن برگشت خونه باباش...
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71051" target="_blank">📅 16:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71049">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/01429c982d.mp4?token=UnGzirDx9rnjuxPW4c7tdNK1M2suiO2ktp4nX--Xm-xjUDxoV7wydSTaK261zHinVEDqgOAIJGIM-VftgTq5sp0fvCqycCSc2QAKC6mjaEECu9qacK8hmVvt1eavPeLj7plwvLLFwhCY5k_yNtkq9rAJ0qjLKcIGonDjeUXJS2WPYZvixZnQ5lKUmHq0Hm8IOkeG6Ebde6xnQW4b-Nd8oHR5UmyX1QBgiOGLVIO1gRWFT4dyVt23M0c5_7zuDSW5DgIcsiynKobsXJZk193Q2SwfzCVrZHU2m7-pjLj6Q7WG3IwhXGUDE_1WD406VVq2637HfNbWR7_iEOzJbyvokA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/01429c982d.mp4?token=UnGzirDx9rnjuxPW4c7tdNK1M2suiO2ktp4nX--Xm-xjUDxoV7wydSTaK261zHinVEDqgOAIJGIM-VftgTq5sp0fvCqycCSc2QAKC6mjaEECu9qacK8hmVvt1eavPeLj7plwvLLFwhCY5k_yNtkq9rAJ0qjLKcIGonDjeUXJS2WPYZvixZnQ5lKUmHq0Hm8IOkeG6Ebde6xnQW4b-Nd8oHR5UmyX1QBgiOGLVIO1gRWFT4dyVt23M0c5_7zuDSW5DgIcsiynKobsXJZk193Q2SwfzCVrZHU2m7-pjLj6Q7WG3IwhXGUDE_1WD406VVq2637HfNbWR7_iEOzJbyvokA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیروز، اولین ایونت مد و فشن توی تبریز برگزار شد و حسابی غوغا کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71049" target="_blank">📅 15:34 · 12 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
