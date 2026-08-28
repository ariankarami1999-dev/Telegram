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
<img src="https://cdn5.telesco.pe/file/pBv0syoDFFqmfMJotoNNyI356DIdMan_OvcVcOMlDTk2cDZcpx2lHRNfEFKQNP0yXk9S27xfAr9pOHonPBHpsWw2yYDMkL17-ZAXqSjAw0MpaZ6n9FsOm4RwzBSF0iUZJ0LtJtkNGjoFmTJHNxz3Mz20g1BEj3znowUGVArvrmWI66uEE7vrEQ0-Z5q2hWwSKKLqPgvIeU3YB0Xlcey5WgPaoM7G1URrbvqtpNrmqpzcbDLuwM3Yi11-N_jITl4J3wLBQhE8xubZFTROVvic-vWUwNCyU2uEMe1fOS6c0HQNBV8_aca7a5Xn_IFIGDA1ykIvqC46JTKhetiaUdf9yA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 440K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-06 05:04:32</div>
<hr>

<div class="tg-post" id="msg-104879">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V3wkDngZ54Db5aFmBo6FVN0jQtNoIic7rEtx1th3ExaXNQVH0HqxPX8QCztldGTI1HHa4INo0hKpZg2XoisFpZfTuh9NBTohT5n-TBU6wQZ24_vcfxEcD1lnBBbLU2B-eWriV6RFg1IMw8qSTFXwTiqWdFAKk-xQOhaISMnQ2rZ-jNZIvO-CS8kIWMW7I-IYQjUtS6jwxMN9JDE9ry-SpwqFEQQ3w80iqgaoOBElOTI2F-g8LhbVYrNP4qb-d32ILRE172lXMHXLxQlsqgb-qjQg0RPqbkYPCRtwDnnxgRwRkg-SLSyivaPcdFJS1MiGYaMfE4N4kvoWkMWSOf9k1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دی‌مارزیو: منچسترسیتی تماس‌های اولیه خودشو با لیورپول برای جذب مک‌آلیستر آغاز کرده! سیتی قصد داره به صورت همزمان طی روزهای آینده با مک‌آلیستر، انزو فرناندز و کودی‌گاکپو قرارداد ببنده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/Futball180TV/104879" target="_blank">📅 02:17 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104878">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‼️
🇮🇷
دختر استقلالی: کوشکی امروز ۴ گل میزنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/Futball180TV/104878" target="_blank">📅 02:03 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104876">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c3OW8al1NG87JO1gVknOorTteQLmqiKal-b8fdVHwmJDlvdhWcXvXLUgtzx2LxRZPqT3ob2B2lAVZyqG_HFnhV7FlF0msu1imhRLl8c-Jpv5otmmMF3vfhmdXgGeZYTIr_2OaOqCdi8VHe5f9ejyr7MJyw2ie2_Mk4HOEyTUQQXGc7Q8SnFplTaCI2iZLcQvsHSnWy8tbRRCmzIeMWbSsK0uO6nUy3eRtVFE7rUwcop5gXxEwbUIaN9Ua-oiJCLPhZDsO58WwuNgqPfbepkC-XabG0YRqWyefgnKjZuwOHzVE1R5CyqYLM__X8kf2VUVgNIXyZz8quzUDBV_Jldxlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pP3l1p4TN0hnqjdmP-ltgK8BuS0aEyIw9ZJU80WDTGaFXFdReEHtVtsifXxEVPodNe4uLyM8KDBq9KbuQPByxvzebnw-kQhKVpXMq_eaP35gqOeXA53yNNW1ROrHEtKcS6syGkyZ9xBmC7aNUxtcyM8j5_15bRb3AayKHANzC3RC-y9axU05X-37hBlWynzXkoOUKBYJ933tMLtuIKpzFqPM7q5YFdz7XMQYurrr8EQque95cHbZNF_XB1ui4mNzjbISAFnqZW7qEIpkL-CFm9L2qZXtU342I1ZCxhSwEyFpSk3NYtuM9AF8xD0uZAol_3g5DljQBJhkIl5k0QZ6ig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✔️
🇪🇺
🇪🇺
مشخص شدن تمام 36 تیم در هر دو رقابت لیگ اروپا و لیگ کنفرانس
؛ قرعه‌کشی ساعت ۱۴:۳۰ امروز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/Futball180TV/104876" target="_blank">📅 01:38 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104875">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63ad7bc72b.mp4?token=Yl8fDAd9xOZh2FY1G6f3-uS9-y2nsLNcppn9dgfScCBhAZ3RRJPPXB9DyHumIJr7U9rdzgR_JHHUCfkZL8J_s2CVV2r9CNltv5s_v2kOW9gKCXkuCdXF-kz0hZdRvrRLFFr4LDvfRNi_sUNRpIIn3GVDTgiWF0G-WUoVpGp6856u48ifQEm8LOEHPcPFKJEfctThchgm0921eZWXUyhGDTR5_DpUBqzeBZFr3qsemM0RDHWWBp3UMtD3FS2pQ04UYQ0DYKYmSZ2n-s8ggt_kg2KK0OH8218rRpgu07zMUubbkRVFCTThaIlFKeOv1Ajbzl89Rrq8-po7GbCeGqpDqQ3an47LjKljHboeNEmj6NqJssPhXMDgc6A3WoP7oHccxWH4O7AzfjVQx-0MQhx4gl4pcp1CKrTH43ry3jHcm1gVXxRHmiCWP2f0-lBQK0xPfX4HZIA7p9f3nFIt2cVVGVhVph_-dYKmXRnjddLC2vdWN_Nuqp0faKBhjuwglSxxzIfgzuhLjrRcTwwyVUedcINK1Dt_oZAlhMWCC70ntK_ki1I4mU27j8QDXZxJqz24vuegS_m147CBUwO5LTSrMx5D3YjL1Hr9VwOdXcBHzhBieNb0RnUkwH-q7Tq448cc0XierINvR_UuehR3SNifD68LExPc5BclVWvLqlZWmUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63ad7bc72b.mp4?token=Yl8fDAd9xOZh2FY1G6f3-uS9-y2nsLNcppn9dgfScCBhAZ3RRJPPXB9DyHumIJr7U9rdzgR_JHHUCfkZL8J_s2CVV2r9CNltv5s_v2kOW9gKCXkuCdXF-kz0hZdRvrRLFFr4LDvfRNi_sUNRpIIn3GVDTgiWF0G-WUoVpGp6856u48ifQEm8LOEHPcPFKJEfctThchgm0921eZWXUyhGDTR5_DpUBqzeBZFr3qsemM0RDHWWBp3UMtD3FS2pQ04UYQ0DYKYmSZ2n-s8ggt_kg2KK0OH8218rRpgu07zMUubbkRVFCTThaIlFKeOv1Ajbzl89Rrq8-po7GbCeGqpDqQ3an47LjKljHboeNEmj6NqJssPhXMDgc6A3WoP7oHccxWH4O7AzfjVQx-0MQhx4gl4pcp1CKrTH43ry3jHcm1gVXxRHmiCWP2f0-lBQK0xPfX4HZIA7p9f3nFIt2cVVGVhVph_-dYKmXRnjddLC2vdWN_Nuqp0faKBhjuwglSxxzIfgzuhLjrRcTwwyVUedcINK1Dt_oZAlhMWCC70ntK_ki1I4mU27j8QDXZxJqz24vuegS_m147CBUwO5LTSrMx5D3YjL1Hr9VwOdXcBHzhBieNb0RnUkwH-q7Tq448cc0XierINvR_UuehR3SNifD68LExPc5BclVWvLqlZWmUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇳🇵
‼️
⚠️
جان جدت دلشو نداری اصلا نبین؛ وضعیت فاجعه‌بار نپال پس از سیل دیروز!!
🦾
🦾
🦾
🦾
🦾
🦾
🦾
🦾
🦾
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/Futball180TV/104875" target="_blank">📅 01:26 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104874">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ri2ctB6fTjoFbSe3fa5wcW70DZX4471A0YVB0qX3bXfo0hPLjKP1i2qdYydpvE-6zLYWSg-5W6u_tfuyE7EfPS3uewq3HDW3cP4-P7r9d-_lPF_nuvgsmLieSMbjW14UuWjZfd5ai6IzSrfknomrpoO08zwwUAWb0CiLgCxkt7EeAy_TqKKTZXeWZzmvCweD1HEp08M8SMTltpcfqUyeC-GIm5m3v8VglgFocRnycY_y6m0q5M0YI-bQO3UDD5dLLNUyvEh5ExlVxgR-Nm3g5Hu-uEVqfdHBVRNHTMCxIYc_EB7PzqfPS6pZR_vm83-sUp2QcKxm0dCMVwuLBg5MBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منبع خبری indykaila، مربوط به لیورپول که اعتبارش زیاد نیست البته:
آرنولد به لیورپول باز خواهد گشت، اما فقط در صورتی که لیورپول بتواند طی روزهای آینده با رئال مادرید به توافق قرضی برسد
🤍
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/Futball180TV/104874" target="_blank">📅 01:18 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104872">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K-mGfbpDlZ77_qQjm2IsCzIY7I5-CCsquKyKHw_SNDxqhO-O_C7zDYxOEKAyJ3blr0SGGThePaBeToFKzqAQBYE1KlHgXoe6B_piYTNfHpxqcP1yao7AKVcK7_a-Yn7OkDdctUky5CkHtgwe2KNk2wXJk9dctg8TjSM2-9UtPQaShN8dgInLZxChASuZ1z2HdAIYtO-43UtaOFhUObaaZDNOXm_XN0PviDY9cL2cBIhUNxdrpqW9wzD_n_akDz7ysbYV1NfWvk4I-eBf_roYurgK0ZZ1hFEFN2rqI4E7-Rvl5TWyB8ULsU-dKrbyBeZWO1z9XJMo7WpNnD_NcuMSQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lBL1Jh4fYL_t5gZ6mI2C1sE_FI6Na0i0ZTW0CRyCEPC0aAfDCv8-H1RmhJttA1ZqjZslkaSKHkM1P95QKO-G1c8ubU4HdZt4EW9hNxjDSYVauUeGw9_-GNkY99ndQRmc1Y3tmN9QNZYszGVYNfSTQGHxUvlccLy6wz5LFd9b2D31cIzHXFmbKUyGees2hADNi8y8bHZb6rUo5JOSbuiDT9biFW6kh67ixcrp6oATIKgbfwWq7whRDAbPZShEJ0cUy_q48EnZx0dikj-djll_bObkYMAAx1kM-IJK1Ub4FYXjIeyaJaO_CYL9vqKC4mYxKxbDU_zzOZdTCfIHv_6dOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🤩
💔
🇪🇸
آرشیو‌وار: ژاوی‌اسپارت در بازی امشب باید دو کارت زرد می‌گرفت و از بازی اخراج میشد اما داور باهاش مماشات کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/Futball180TV/104872" target="_blank">📅 01:12 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104871">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tN8metXRMh5NCRgxwKY0O-__KoRjBnUfMT_9BDBJnJvBW9euWj6Jv4UltSpxIodLiLUdCKuRJtxwARL90_ZRzwXqfYC6XdmhlYChB-Hh5vj4w_51DWJg_JKJOP0QDQoFi6dyeQasroVnHib6OJ85znCX6AG06c3htSsU2FGLBEFVjzkqeh0x_i_oY_l1PaBMIN9xO3wWkCWxHzjkD0S6Vf78BtAt_aGtlux1M4HzpgwPJcIOtIzcsT8TSrVzCH1oYaiIVpIbvwcO9nZGEbgQptXVokd7SI4gdAiHze8PouC7FiIJjF0j0RgaeHt7P3r4S4IDeLeEw9ovhX2UqBETAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
محسن نامجو از نوازندگان و‌ خوانندگان ایرانی پس از دو دهه دوری با استقبال مقامات امنیتی به ایران برگشت. نامجو اخیرا به سلطنت‌طلبان انتقاد کرده بود
📲
پ‌ن: توییت چهار سال قبل این بزرگوار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/104871" target="_blank">📅 01:07 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104870">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
⭕️
🇮🇷
#اختصاصی_فوتبال‌180؛
❌
باشگاه استقلال با ارسال نامه‌ای به فدراسیون فوتبال اعلام کرد که تا پیش از بازی السد هیچ‌یک از سه بازیکن خود یعنی سحرخیزان، قلی‌زاده و رزاقی‌نیا را به تیم‌ملی امید نخواهد داد!
‼️
این درحالیست که بازیکنان دعوت‌شده باید تا فرداشب…</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/104870" target="_blank">📅 00:53 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104869">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sj6vDxrT0a51Tufsz41-Ljnvrz0OFeAT9lfK2n1qSUSZtVJyQkZjF4tysfSJariYHxTI_Ih2HOfXuFyVVklR4gnCKfI1mJuv9LL38PeN0fctPjSuDYZEOZhr2RypAREW11bJuelqMI2M8bWUnOCRfwpRiddYAtzJT6mkfvrg3iQ8SSfeYnxHTlUuNc21dgFZsMVJb_A-w5IFj7Va8ATtiZycETDJ8WDJkkxmFT4UWRXHshR01a90yKX08wHbfGiWod-3g-lfN-l95QbtQ1rEaofJ9yqdKgN1-4GTmMUt9rjJER8NBfBhRrvzXGHKJbmVLF08b0p4bx5tPjxUmYKxNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇮🇷
#اختصاصی_فوتبال‌180
؛
❌
باشگاه استقلال با ارسال نامه‌ای به فدراسیون فوتبال اعلام کرد که تا پیش از بازی السد هیچ‌یک از سه بازیکن خود یعنی سحرخیزان، قلی‌زاده و رزاقی‌نیا را به تیم‌ملی امید نخواهد داد!
‼️
این درحالیست که بازیکنان دعوت‌شده باید تا فرداشب خود را به کادرفنی تیم‌امید معرفی کنند. از طرفی فدراسیون فوتبال به استقلال هشدار داده که هرگونه عدم همکاری باعث محرومیت هر سه بازیکن از مسابقات لیگ‌برتر شده و هیچگونه بخششی در کار نیست
🔵
آبی‌ها در نامه‌ارسالی به فدراسیون دلیل عدم همکاری را کمبود بازیکن در هفته‌های پیش رو عنوان کرده‌اند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/104869" target="_blank">📅 00:50 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104868">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adShBSt3rd1fMxdailSl8wbElAPqWcvTSNvbIh_DkhSMJejiVI_W6XqRo7ySDqZeQEuNU0EGlNcUoCQa1-KnRHErce-LsgoCFkVqhbZor1AMku3k2tTkpnm7mQbaDYLBqYB0oMMMhSOb34UzcNwOQzDax3O0x9UVuj5njdsRjdDcTf-WEYeQ6pTMYoRKeS7D10EfwgsLip0pzRsBHQNoye-ndmio3zPzGbA6-YfSHTa92HueoLF_vq_kZcpFTK-CZBG6kJrS8ZJjkkDqsSfzoSqnuIsZ0Y-z-15CPG7fYBrjFbQywO60tgVCD7YSQmP6owMiFX4b1SPLuH7apTakeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
بازی‌معوقه لالیگا؛ اولین برد خانگی بارسلونا در فصل‌جدید؛ بیلبائو در کمال شایستگی مقابل کاتالان‌ها بازنده شد
🇪🇸
بارسلونا
😀
-
😏
اتلتیک‌‌بیلبائو
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/104868" target="_blank">📅 00:41 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104867">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6-rv_OtFTt5m91_COKMHPUJyxYOS9ktng523BWbPZMMmhGXHlm66wxAZwTYFoRFPAEhJV3hhGltPDnSd6xvE3XacGVgkcsb_zWr3cJ41BlvfYEytQ7nXzqjrTOoKW-zira4NtAtKvQ4mDczPIcsAUhLmSDioYZn5v7soJfxvhqdGmtFr4nKzxzPX1btTwfOLQCbGi-BTYKsUsJVsByZK-TE3wAzcwkyvj8eVMkMxvdPZuCRX1oP5RL02qBMIq9tgCPZRjjcbEXBvT-MAcE3wE8bdv9vGiCRLIicUWOJz_GDwj8GPl2Ragc0KmmQavKHAQertX3wlCM8aRFDDDL5rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
بازی‌معوقه لالیگا؛ اولین برد خانگی بارسلونا در فصل‌جدید؛ بیلبائو در کمال شایستگی مقابل کاتالان‌ها بازنده شد
🇪🇸
بارسلونا
😀
-
😏
اتلتیک‌‌بیلبائو
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/104867" target="_blank">📅 00:31 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104866">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">فرمین لوپز گل دوم بارسا رو زدددد</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/104866" target="_blank">📅 00:19 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104865">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">گلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/104865" target="_blank">📅 00:19 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104864">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">یامال یجوری ریده این دو بازی که وقتشه زیدشو عوض کنه</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/104864" target="_blank">📅 00:06 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104863">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
🚨
رودری وارد زمین شدددددددد</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/104863" target="_blank">📅 23:58 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104862">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇮🇷
⏸
باشگاه استقلال با انتشار این ویدیو نوشت:
❗️
خوزستان همیشه آبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/104862" target="_blank">📅 23:48 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104861">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fd2b46d0c9.mp4?token=Ewv5cveeaQYZ8pNQX-3O3LIAEYR1K9EU_YIUqt9AxWwqsXQxQlOyfaqkXUhjueRnpDWKA5KIwUD4at4tpMVp23gYT4BIzuyiweXoicE8j49AmbEKDoxJF6-r9iRnWfgVtXMSjk4BMG1L1BXCpw0PpvmyipNx7bAtXDPX1OyQy1PLz8ulaluue_A-7DSBjnNclG2XAwRjOdiuketlT9pRc1Ls95urP-AbMHq2rei2OIzPQX38MhulfhjJmRUDFynAUsC5BCrEWkTOeFSqFhfpIAgWu8RKCOra5A5XYt9dYFVr1Sgwj_lil2eYjrBmuCo4E9s-y5Ztt9i3rcJkbBUHDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fd2b46d0c9.mp4?token=Ewv5cveeaQYZ8pNQX-3O3LIAEYR1K9EU_YIUqt9AxWwqsXQxQlOyfaqkXUhjueRnpDWKA5KIwUD4at4tpMVp23gYT4BIzuyiweXoicE8j49AmbEKDoxJF6-r9iRnWfgVtXMSjk4BMG1L1BXCpw0PpvmyipNx7bAtXDPX1OyQy1PLz8ulaluue_A-7DSBjnNclG2XAwRjOdiuketlT9pRc1Ls95urP-AbMHq2rei2OIzPQX38MhulfhjJmRUDFynAUsC5BCrEWkTOeFSqFhfpIAgWu8RKCOra5A5XYt9dYFVr1Sgwj_lil2eYjrBmuCo4E9s-y5Ztt9i3rcJkbBUHDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
😃
دنی‌ولبک بنده‌خدا امشب برا چلسی گل‌زده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/104861" target="_blank">📅 23:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104860">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f04612395d.mp4?token=Ghxl_ZcXk60zR7pr35JX1-GDDCGxTE7pG-ygMDTY8yE28HCcDHsKQhLIXDsV9SexAoCgcgTNFjLCFYyMZ9lxVl-TzgGjApfIDD7YqPXWskqHWsI91cQZ5ohPd30u_FVvp8B8KH6xN2B3GKt38DHYkwdoklgMAURf1XoskOw7SwyibxuNL415PbgI1FfAbcms-AfGWZcnd54_hSCPafKMIvpLvho5aWYbjSxi21hMm6r8nmpoeesUjyyxlMrDLTVHt7v-Q2-n4Zq4Md_ox-RDuU8vKrHqU-Gdg9Ya8WXMpzPZOB6nEMqZ-d0qS3Kz6u-DVxz8Ws-yYR5nMERYRZY8Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f04612395d.mp4?token=Ghxl_ZcXk60zR7pr35JX1-GDDCGxTE7pG-ygMDTY8yE28HCcDHsKQhLIXDsV9SexAoCgcgTNFjLCFYyMZ9lxVl-TzgGjApfIDD7YqPXWskqHWsI91cQZ5ohPd30u_FVvp8B8KH6xN2B3GKt38DHYkwdoklgMAURf1XoskOw7SwyibxuNL415PbgI1FfAbcms-AfGWZcnd54_hSCPafKMIvpLvho5aWYbjSxi21hMm6r8nmpoeesUjyyxlMrDLTVHt7v-Q2-n4Zq4Md_ox-RDuU8vKrHqU-Gdg9Ya8WXMpzPZOB6nEMqZ-d0qS3Kz6u-DVxz8Ws-yYR5nMERYRZY8Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🔥
گل‌اول بارسلونا به بیلبائو با سوپرپاس پدری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/104860" target="_blank">📅 23:18 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104859">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">اونای سیمون چی گرفتتتتت
😐
😐
😐
😳
😳</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/104859" target="_blank">📅 23:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104858">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">پشماممممم</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/104858" target="_blank">📅 23:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104857">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">سوپرپاس گل پدری رو فقط
😐
😐
😐
🔥</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/104857" target="_blank">📅 23:13 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104856">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">بارسلونا یکی زددددد رافینیاااا</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/104856" target="_blank">📅 23:13 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104855">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">گگللگگلل</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/104855" target="_blank">📅 23:13 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104854">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d569393418.mp4?token=DfRJBHg2yKg6AUAUCJy_Ce4PqjAapu8ppvIKqrHol9QJSlg7R6yNWMDE9bTchVmhY6hTquubpzCxVw_TS-buGIp6OrypmLOI-1__Q_gzzpbs7pYtyROUuNyqJIBHwsWouDsCUhXk4LYvUdb8_jJbfP6JU78LjX8ISSMU0evEaiNeAyK-Qoef0UfuMK9lrZ87ICiZJPzgyaMH7Mbo3Pfq5sPrX8vBgZMuDatGceSzPC8su7ECiW_xemTreZXBbBXx58_iEeXhNiU-mq-Jb5-YKvp8SFU3NvQMuzbFLd2tmabIIzdW78BNNeyqGTy74quCdegfjSBJzbshH7MYDtFmqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d569393418.mp4?token=DfRJBHg2yKg6AUAUCJy_Ce4PqjAapu8ppvIKqrHol9QJSlg7R6yNWMDE9bTchVmhY6hTquubpzCxVw_TS-buGIp6OrypmLOI-1__Q_gzzpbs7pYtyROUuNyqJIBHwsWouDsCUhXk4LYvUdb8_jJbfP6JU78LjX8ISSMU0evEaiNeAyK-Qoef0UfuMK9lrZ87ICiZJPzgyaMH7Mbo3Pfq5sPrX8vBgZMuDatGceSzPC8su7ECiW_xemTreZXBbBXx58_iEeXhNiU-mq-Jb5-YKvp8SFU3NvQMuzbFLd2tmabIIzdW78BNNeyqGTy74quCdegfjSBJzbshH7MYDtFmqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
اولین تریلر و گیم پلی رسمی GTA 6 منتشر شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/104854" target="_blank">📅 23:03 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104853">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZBZoIiBvy-X_YfCFdDV387P7e_vr98Cxepw-4nKjiFN8H26TU2ZQ1CXlo_gzw79KGjcOfSW_jTkYqMEx3I_--S93_j4fHwqQZ5f40RF_QB4eqA4VE8OQVZ5pOFppPVjQZ3vCPmBY7OnGahuA3PiF0NS_CgSAGe5Mxk2E3z70IAo6vQP8eUL8nHHRF5IndhpZFseEYfLPieMoohEsGRY65OmoeIbKSi-rWf7EZE_CulLSp9kDZAvneFO3gDXiu6F2wdwcZJdKv5Fl3DkYWl3AUxKxmxGQc9CZrRrd1fOZyVZwCIEx-x2NJLpwsjkKcAqvW8hXo8Uvu6vQ2tz0zFD0ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
❌
ایالات متحده آمریکا ویزای علیرضا دبیر رییس‌ فدراسیون کشتی برای حضور در مسابقات جهانی لاس‌وگاس رو صادر نکرد و دبیر در حرکتی پیش‌دستانه گفته که قصدی برای رفتن نداشته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/104853" target="_blank">📅 22:36 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104852">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WoEl3dPhvNr_JucZsY8MatRrNC6KBYCAR6IMiCNVv6CCLJMxIo2yJV1oiR2nLXrLdDHcY79Bipd6KNqAAY-zt_8CgS5zbufz3sVzSc7MnlfVx9UKGMHxe46dj5pHo4l1qjKimaGLjiR-hHda4x4cdFjwu-Mu-7mCoNxSgu9-8YKAT7E7WMuqbIlHud5aKBpnVabrhtJb5JPQzvpQfPBRDR-urdWnxFVdvXbGUfEUhAFLusbGRWvZNDkN2HRTWyS0AEv2NsUPjqYaTRHTmK9zv-pVnrjpJv-d8of-4dxi7JhLrpccL1eAgO7MJNgTeBpA7CqqTeXDCa4a7Jarr97YOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
📺
نظرسنجی
رسانه DAZN؛ سرنوشت خولیان آلوارز در نهایت چه خواهد شد؟
🇪🇸
‏به احتمال 34% در اتلتیکو مادرید باقی خواهد ماند.
🇪🇸
‏به احتمال 33% به بارسلونا خواهد رفت.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
‏به احتمال 33% به تیم دیگری خواهد رفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/104852" target="_blank">📅 22:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104851">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZkT0RXeyKm99ydvgd3JmjOUrjM7JXQPAUKl4vBkKNv9CujUZKxFfi4r3Stc4XtBsP6B1qUs0--ssD1m-YPtm1Afz_fvfxmA9KCDlipRc7GQ_OuzFwx4oSNoazJErGZycLkktofvjl9sA8P23SNhncDw9mwEyt8zEjoxFtlV7jkdeZMPSGvC0ROS0FY63LucBz9kgGKKyFZ80PLFHrh2gvYgZxDVnL9tAJpEwautTy7IWedWxkx1f05Rz4zBSqwc1dSWyqh4aVsZuHhDR9BE4gHHtz-YShEFh3u8yirpBmwUEngOJuYoDPRv17TtrOk3FZRWdEOg0Q-TAhUN9y-i7iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
برنامه‌های فولاد برای بازی با استقلال؛ از مردم میخوان که سریع بیان ورزشگاه که تا ظرفیت ۱۰ درصد استقلال بیشتر نشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/104851" target="_blank">📅 21:59 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104850">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdfb514bfe.mp4?token=rtU9_rOWxYu47EISgoXhntrrWCJX6vSwRnY_RXjAe2wg5wZUGfyx17GPjIrQ7t_e1CqgwdDxOHPzZaeRkmtxoASn1PegiDrnsEgO2ud8KNM9axAX-e2qRXDiUIPWbE00S2RYfVj1AWgnMwgA04CPZ4W5OhZmgDgOBLEJbD28SDLQ2QoF-XeMvgXkj7bpCPk16oYtERInDi9um4RJWiBmFICmcahbvCkpmjOPwzc79JYunweQLTGG7q6YJbh3E2KN4A2piG1QLzb_NaQJXCsFz9QsUS7GR0oQ60TSnc4gkHcEJII8uzx_Bq5ghNYYM-nsSBP4ve5P2li6tew4CfyXySAreyl3nC0-vxfKV1KGGxCrpht1NBcfh-88LbqFrXXSCXOx0U-bvzPr71YMwYgbV-HZdbRRoXGRHAgbWdXY63DRjPPuumZFBJ101D9IBQepDdaAHrirzvQ1G3JNAnoP8snsZrFhZ38ejOzywPF8KDkW7R6zUCXmF5ehMDgTv199QKV0DAdkDoa1G2JbJlCy8W1ERki_azUsF8QMmzU8WsiqDGE0hsdmWDDfa10BG1XNy9fxm4v7nqfItHU6rwDw0rMBRGQWMnYx0xY1qci2DnPF9AM6sZCAy-hV_C9Dsn7P8HNf1gDOsjoiX_s-3TLdQGE9gzO5mU4VggfZN6S64EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdfb514bfe.mp4?token=rtU9_rOWxYu47EISgoXhntrrWCJX6vSwRnY_RXjAe2wg5wZUGfyx17GPjIrQ7t_e1CqgwdDxOHPzZaeRkmtxoASn1PegiDrnsEgO2ud8KNM9axAX-e2qRXDiUIPWbE00S2RYfVj1AWgnMwgA04CPZ4W5OhZmgDgOBLEJbD28SDLQ2QoF-XeMvgXkj7bpCPk16oYtERInDi9um4RJWiBmFICmcahbvCkpmjOPwzc79JYunweQLTGG7q6YJbh3E2KN4A2piG1QLzb_NaQJXCsFz9QsUS7GR0oQ60TSnc4gkHcEJII8uzx_Bq5ghNYYM-nsSBP4ve5P2li6tew4CfyXySAreyl3nC0-vxfKV1KGGxCrpht1NBcfh-88LbqFrXXSCXOx0U-bvzPr71YMwYgbV-HZdbRRoXGRHAgbWdXY63DRjPPuumZFBJ101D9IBQepDdaAHrirzvQ1G3JNAnoP8snsZrFhZ38ejOzywPF8KDkW7R6zUCXmF5ehMDgTv199QKV0DAdkDoa1G2JbJlCy8W1ERki_azUsF8QMmzU8WsiqDGE0hsdmWDDfa10BG1XNy9fxm4v7nqfItHU6rwDw0rMBRGQWMnYx0xY1qci2DnPF9AM6sZCAy-hV_C9Dsn7P8HNf1gDOsjoiX_s-3TLdQGE9gzO5mU4VggfZN6S64EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
برنامه‌های فولاد برای بازی با استقلال؛ از مردم میخوان که سریع بیان ورزشگاه که تا ظرفیت ۱۰ درصد استقلال بیشتر نشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/104850" target="_blank">📅 21:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104849">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TosV1xT2SdCQ074tay2H3O_jDpc6PXRUcooffwvY31QsDHV3DR67bsv-nb63ngy0ND-bgrHB2QJXcEYwZD-3XN_kDi9zRdR5cR1chUTZLu2amNVz5tDjLp8j93Yhbktx_D2lyQAtS505Y182m-4czyvOf5PVZVZwV_u2k_RXKkBeHiCFBZGXkRHJ1fjCRJ9iUbkhRAzwitFDQyNVq6j_S4DAn12ozme5zT8mnUmaQWgwX0XJQBqG9iFlRxbx3ST-zKsS6fipueZ3YOS3aq0awkEYIXABzkYBJx3MIJAKChjoz6a9B0na65m789X_NO5kmNtAEtmCpd6U11XAH4qHRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
• امیلیانو مارتینز از استون ویلا به چلسی
؛ HERE WE GO
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/104849" target="_blank">📅 21:37 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104848">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
خیل‌مارین: رویای من اینه که آلوارز بمونه اما اگر بخواد جدا بشه مانعش نمیشم ولی به بارسلونا هرگز نمی‌ذارم بره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/104848" target="_blank">📅 21:30 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104847">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MH_lFjDzGZ_aJKwRebwTG0VcJ3ytE2gf08Arp4FfpAmMDtABJwcITkq_fw4srMrPyV1tJ8Q7aEyBcASF0Ta7X471BNGplxjY051wVHVbyO7yrQXnmV8pmsaHk2IPaGykKnr8j_WcXysCtiNh07RC-DvxRlmZKQfahiLB63zqbc415YJxbVadmKuF-sy-VwUKQnxfE_y2r4xmI-UengNAafMtXIcMN0g5XouUxdFFRmh6_4UphG6jDgGf9E7RS9zzWOGfuzNv_wfymUD6Q2gjiOrGpsFSCZZFRX9dcf8q7s6UM_On3pC4W1OAKhoual2-0eEZcbcp6LduwF7ksfKEkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
معوقه هفته‌اول لالیگا؛ ترکیب بارسلونا مقابل بیلبائو؛ ساعت ۲۲:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/104847" target="_blank">📅 21:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104846">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
🇪🇸
خیل‌مارین:
🔻
بارسلونا روح و روان آلوارز رو گاییده. تحت هیچ شرایطی نمیخوام با این باشگاه بابت آلوارز مذاکره کنم و قیدش رو باید بزنن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/104846" target="_blank">📅 21:03 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104845">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
🇪🇸
خیل‌مارین:
🔻
بارسلونا روح و روان آلوارز رو گاییده. تحت هیچ شرایطی نمیخوام با این باشگاه بابت آلوارز مذاکره کنم و قیدش رو باید بزنن
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/104845" target="_blank">📅 21:02 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104844">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3a58dbdc1.mp4?token=e1mlzIfKI3ABSJvIjVUct8mXptyYCVE9pyx3DwCCuPGZ90-yfBr9_njkheOWQe9_DDq1uU8ixJESSV3s2ZdLdGDWzUgf-m0WMP0j6h-89aMwf2JoCe-GJOMu-cjeUjN0c8aLpPvNgZYys2_qGRjqZH8sGvA5nKSz0d2Bi0aAyDsvf4PhsyLaxIw-bPhFkhQq5iq_vbvmSZnzdJAG-8rN_vgw02oafBPlyTGK1cpwuFctZKVLNvjU-HWAfegA9f0jav9zdE3MPpO-Ui9f3kEtJShpcJ1LXUsMJyQ5Vh5hnMGl5OKD9UodnGwV4z_csDAOkvjJ3RYhBRmr25Aeql9X3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3a58dbdc1.mp4?token=e1mlzIfKI3ABSJvIjVUct8mXptyYCVE9pyx3DwCCuPGZ90-yfBr9_njkheOWQe9_DDq1uU8ixJESSV3s2ZdLdGDWzUgf-m0WMP0j6h-89aMwf2JoCe-GJOMu-cjeUjN0c8aLpPvNgZYys2_qGRjqZH8sGvA5nKSz0d2Bi0aAyDsvf4PhsyLaxIw-bPhFkhQq5iq_vbvmSZnzdJAG-8rN_vgw02oafBPlyTGK1cpwuFctZKVLNvjU-HWAfegA9f0jav9zdE3MPpO-Ui9f3kEtJShpcJ1LXUsMJyQ5Vh5hnMGl5OKD9UodnGwV4z_csDAOkvjJ3RYhBRmr25Aeql9X3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😢
🇪🇸
کارگرافیکی اتلتیکو دلقک برای معرفی رقباش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/104844" target="_blank">📅 20:47 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104835">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b6HbXjYNXe4GVJwe0tjRfj-DvKoYSO9VmUKX0CMMi5GSg3o01O_vhvNrxE55cloV1x_lq3K3RuLEPPJvWrtbdrfggSzNPJp_Awle1F9lPjrJ1afPxjNUin6Yb89J3oC5RQZJCzcC9NMRpqdnUBm1F2-91SjiKPOddG5X0Ux0WHvRCaVGaxjVp3Wb5AxDwlpgUZwdalEkVUdC0RABhZCXBE-MlkU_XoT0u0_k9HwDbIssnL5VpDCwRh2QKJWr0sMoV9eEhr-TX7BTAfom-Q7M_ATgg_TZXPhcumRd420b_90ubrLxyKEMmUEUzMx-CjoKXpGeOZ3YmKzP5gzZF4e9bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b9zOeqSPy5L4TxzlHbF8t6SOrvgzbPzz3Zyh44ZAOXlwAZW0l-SfjZuMaTH11JohiBZE6bRiRLbO6sY0UUAgGqZYLcxheQzkQXWSF6v8c2Vh6VAk1EdxmW55hggcKMMYcYBuagkBm1sEF-P_mRFhlCuqFuGoxLX-UeX9Fmi6vDrmnc2EWl7KW4E4gNVJcCIclb1qeBB8RgsCwLMQ3M8ua-A0AZ-blfRHEc-CP_GTBbfjk43uxQpuGxOsnmxVr7NI8kXs4eeCrOBswHX21EG6VpM6tZ0kZAZgXyAd_zQij22p39IKFITSADnLm1nlIGHH5l8wO4CZxbNlcOJJs6O2yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UddZEciMh34DGTzR3D3vbWpHTwWow7qTsim1mDiEXPfJmF3inGSypTJm0A5eJ_UUwsrl0Cia8wTvpvynesd90kFGXbXNDo7QyzBf41ePeRF7UwBLC448y8fG_phBrxmUyjaaBEmRSvGL1-3LhJDczqlfTFnxDIhwo-yo5R5_IQch_JEHhr_KGptRRTpoJryXjMxjQDRbw_pEl3lh9gzPWdcf7X3NoaVxbyAwFeKSECbeG1j9KZEhJCMjCTdDMoVMPaJgUR9AElpzr3y4QeCSpK3u2mkDFs6sV2ABphTeCwb91bhgArfPQoTzVowUMNCMLz7E7C4_t_jXSRKZJrbV3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JUdtwFrFDchY1B_gWvlbg1bmYdC_PQtz9o4_auXfABN9Opfa93J0hJQ6NPjryCNeUqeIyg7Txy0R7FE6KT__irkYJn_j9hrTeOQhZ63sKuw79KY8O5OIHAJEdztpPVicU8nSr6_hlkCQeIhaWPedY54nHgBT61LDrM17C_g9ncldtFH1-IDRhnFxO6dF40dlSJGftgAjc3Q_PIcbdf4KHKwMNLIJlznEYgSszoLfaUagyYOENs0VOdfC8HE_jKdGk4RjqGWONRIk4MHWZZt751GJ2g0WDd493vx-g-7Q4cn0WHgZr7g82L5AV9Ww5mCFRBUJgU6J9MJyKynmrOW94A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gEITWyTk_etaLlCJjOxMDK-Dvf-Uvk2PAtOETFRUcZsAu0S4MU7SnBju6wbQ62e5do9Hy-kVih_KiMWUWhNEyFPzT2hfYQL9EYvQPLFyNacGzXWZEYYOS6gSpc0Hu58pRNR61T-GoiM0OZzigWv6xoHSqyzMk5jLBEqTgDOL2qEJmYJJEkZY5-X9BtFSynQ9PfJxpSzECZibjvLUUPkyy-acQD2dP4uQ4pj1MJIop3zmwye3RQVMKLom7Fx0p6OqzwZjl-qFFy_EHZgtU2l7waDTED3mA0LcpKkddBkEyXXJ_ijFgeashYocsu3Tu4kbeLde1ihpHwVPr1lhhV7k6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GZzeD-xgTg_9sN5HNVmSSakme3NHXTToSqVgz6-2bZwq2QEsTpkELk8kq-sLJCWPOmfVB_GY-H4iL0Y0WhjNk5pj2l1_V2nlVltkmsImBl5bHketlhilBuJ_a7OvkxjWeY0e1C_jejA4w64s6NlGLOIOKGQVgDCPevaPUo3k0o3qdxMPK3e77RPr1oEZxmPYXnW32-Y6EcX6MwmDKG2WGvzC5KMBAoEboR5-holRwvgL6ygaanT2oVw7ReTd49TSu3yDMtUxcct9Env8GdXFdwAj3Z6pId3oZdpoDv9ro_4kxRCkCOaarjK10zjXglQnzlSR_zN2GPQl50MljAWXrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k7U72L7uG7D3oLzoMYg5la5m1bvZSlOSBN4koNPPOfT8CL3xGAfBhLTHTrWIIyW_EXooZOryuuhTxCpKFEWbiHKvRzxcT2eDJraECYxQQByNFsKTbKK0meBUQ8u35p3pmEL5s_ZHR-VVFyinqaNfNebhuweCRRmBNQ7KOliPDG0mtxlBDWqd9zytBuyidP4vlZsEDlg1hbLsWbCIib9fl9jBeO7hD-H1yEet8Ko9Gh7dxsPLoSGTscb1QJM4o-UFC0_SUHB9fCZtTX7snMaAWlqnjqru0a_T0qftTOGQkFACG2yAOvqFtqt54RV7-GB2wqNNmqqnKSmklQGE9o3vtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CSUXx4OY2mtDE7bKQ1dOmsnpCO4GDwqXk4cb1A5VNWjki_hoK6OB8AXfRwLSheEnZER3Jr7RU2mC7bc1uoXe7GBu1ejD2gr2KjoMp69kftEMbqlqzYRTPh6HcJfLtPHhCljAUhWyPmyZNdcxlIIOZwpqLaHXp9j-tzjUVD6SV03scG3URvcokVoWkr8hUrQu-7PPw7KPOBRvamDwYd5fazNn0CW0-nKsSPDDdTNaxnnYeVe2c1tt7yXe2WFRgETx6CtnzszxzETRX30yOiFYzEy8gmrTXEcOA8xlhzxX254s0twjoVXk3xNzJHe54K7pCPx10P1Q9L-KJMFFPrtNrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CioWENemK6LXcB0aZGYrh32-YwTgnRMYvE0vxkL7JDuSYrM-o76RajE8JuwuMHgxsvuzo-G_qrG5oQgrM0h6S8QEiVmnVEtwk2MNCr5KDXh1EOD-6jink2Msw84HR3q8uGxdoRL_bMXEng3VyJvKMtoUUkAEuXTgEzxlOQvCwF7iDE3udvg242Tn8_hBw7MrSNQJ-fcFAYUTwXWRXFWo4PPGaSZrtOUPztt6nWqiL8312fFXe5X7j2COcBuXzVcx-aF8jZ33GqwFRiGEaAKZbIKQ0fdaMKLqV_3tyiea43sjUpXGLc2lxPC43tSKNHhlf1FmU95XoKAnwXKMqjOWPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
🏆
📊
#فوووووری #رسمیییییی برنامه مسابقات تیم‌های سید یک در اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/104835" target="_blank">📅 20:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104834">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ikb8X7BdP4NHB3SbOhLU4IuwssjtUBcyozE67uMoEId_OuPcp3sZqEjNzjKeYvwFm4pTzQDrGoQYnKOc_PrkZiV81nvs9O2l4wMrPxP06KyhiMEwf1CFFCJNWUIbcf_8fY1w0rKLFvu-o6PANOZSngSYkeyOApI6hlG2Jb44DC9zrAKHlGnvsYEb9rwrf1RruWATjrhQgkb1NIl1bdBsD29Apm0-mYQW-dRd0qcjRFZiGTUcjupsrKvVfVq9dK3fs4WBELTZ9J9XysK5evP2MAw4CnY5_rnWcKbF4pd3-5RfIG4yw4grTvtXGPpI7mVlzGBHPESpzeVdQDa90sVwaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
📊
#فوووووری #رسمیییییی برنامه مسابقات تیم‌های سید دو در اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/104834" target="_blank">📅 20:35 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104833">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WP3Izc-VUJ-VXydNQ2HU0HwC5PRSOZ_weiHYmznm0tv4Df-2NkMVVDd8Z4D0qJPVFfkXd4XuU4lrPtjdklv54pGeZbvyOVFI_OWy1BE3ylyd48jXbvxgPpahUKMgeUXjuchlEPAjlWQBFBAFuqY32WWXoNikikSWfE9Et6JpW9lFL2NjXsvEOPfdttMZdcjAY9ZMiLpG2zYf0mAj-uO-iSrRvDfXcdWEPcDPZlJp63nURU9ODCT5veH1xZgmRiCBZIwwkVjNTVjnCJCr1Or-kBHhHHqdU8UFfDXZ5WOkT19ugA78WczkIROIR3izRzRx7OKffTSyjcIyR3c9zdEbqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🇪🇸
دیدار یوستی مدیر بارسلونا با رئیس اتلتیکو مادرید در حاشیه مراسم امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/104833" target="_blank">📅 20:32 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104832">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CnQ8EAhXfEYNl_nzB3EqAaeioT_IHUtp2l0m5swGpGKIYgr964I3gEnB0w4yq8_LHzTtxzaBn2IuOFbPu3HDczfNPJDAuZWq6MxfBSG8NuVH8I9tp3RgMnHeIuj19rsdC0nLREXap2Rojyct0x10EY9PM3HVOjQ3Q6eFJw1PlzO-JOWNnQyOgikQS8_yVrD_eGtzYOrQt3ROX8h3304g_VwUhIjhugRlvMxN1SJXajMiyEUjJAwlyO2vkPoalHIu9WK0238yB2sE1g_Klgavr9u9-EGwvs5VY3EaUmPVhqCrcOWCEgpAaUt-hCGBvguT664OqvQbPSgtkOpc2mGAkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
📊
#فوووووری #رسمیییییی برنامه مسابقات تیم‌های سید یک در اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/104832" target="_blank">📅 20:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104830">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gOZ2lP5c_AGB8NpbB-MI1xTpG_BPqN5bp21zIehj6wUua0hsaFbMdPjavZjvb9FYdhwavq8Har7nvcemcQCynr_qXlDwg0E1N2sOcKtsNRS2EqLygR-BeooZfPEvV1gQBQfZ-kTSn21_XIW13VoGgZ681VTQPJBFmEaERKTltZLjGfPLCPH7yXC_Rg9P19cavbfzkvDBYcA2Ph8_bV-cTP-zOLBwjHxT1hzTL8XIysiygheu06QgYZxBiVCuSmYa0x-izyvHVsg_Oku5Hi48Lab_FXFL_Mg5Qv5f5yDF69o1YmHYs_lgND2Rhd8xPoimKvvITW9jy_cevpFCon-PVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
📊
#فوووووری
#رسمیییییی
برنامه مسابقات تیم‌های سید یک در اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/104830" target="_blank">📅 20:13 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104829">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/liA23FDLqz1KYuj2UagVSAF_9-Ho3j51_gHsvqOxyiGo--poQC8knkHOMXgH92zXpZ3W167Z8P8TEs_ykUagQDHd_-plG-l8_j85oWad-MX5ttIMgoSXANcDS-9KztsnuiMtQ-gkazd7YHhx_G0F_3YnGFKoJERgQY52WKcJizxJiz_VsJbnot61kNKWDozsFzNttkqMH0gpvg3ITMpJOrD5VCgDjTajv50QNyB7MQIdQo5jNd8F4XM22f-oGd50gq7INX9nSdgEoJb7Wq377iEXf0iR67NzCQgsErgSdG-KUSvTW51DjP6n5pmT5y4OmY63rrrzI68nl4ruTLgF2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🏆
🇩🇪
بازی‌های بایرن‌مونیخ
اتلتیکومادرید و آرسنال رقبای سید یک باواریایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/104829" target="_blank">📅 20:12 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104828">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rMzf9sxZcv_IMQZsX5sGUCn752nih-YYz_YP691wEBHvNcAPafoPlEwPN-QmtIK34G8q2XBXIuye1JY54qdhahZsGDJjfsd0iUX51tpGkdw7HEE1FBO6m0EiZTpCqY2kl7AT0pIO-eYhBzcDN8cXyvEtNBqXy-K1U6vWKVfokut1n8jRIGbYRmaKLKZCcjDrTFM4tHoUkaGHu0j7egbfQVF9MaRjOtUPHGyJLb5wPTPphfq56T2pjGyQuiM4J8VJcSzGSCZfiA18EM9EiExAQJXPQ7KIUgOO_KhmHDjQcCPeYtgZiuG9wMrOXdJasDuTn-90BMUqMeaSRM9Rf2ZMzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
برنامه مسابقات آرسنال
تقابل با رئال‌مادرید و بایرن‌مونیخ از سید یک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/104828" target="_blank">📅 20:10 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104827">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YrbTXXu0DlL_ZMNmjrnSzERVl7RGx9P3_pDryI83uWmVTQn2Z15unuQ1DJfPbJkM79wa-HPmn2FYJ8_BdhQdt_MC66BPUW00lArx1u3lAijdHyEWdb82YeyjSbD44TciCH8cfvr3PreFT0XA0GPFQymm5BDSgMCSjAAniI98qKx4aGiGNmgRF1wMWOF64fsZTc3Vh0ViqUvmiYmI53PjiKhrpaH7JBGT6kyMUZisNrgaFU81Uj-AqM-Ex5scS4UrmY9U1cB5TyeRwUjPOWmU04jzNd8Xh19mnbRosZP82w9DX4aMSAxh9CGNwyw0w2yDaGvKpFExnVQRAX5LKn4eTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مسابقات لیورپول
تقابل با اینتر و اتلتیکومادرید از سید یک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/104827" target="_blank">📅 20:09 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104826">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jffh9BprqRpBnNyN04wSHrG06TzYblcznm38JHKVf9mzbEk_6cQrD2HH_cPbhmBgQQIxbCsBg96mQdDawzpSZBFqXp_7NtDP8PKm0HPb-Rw3w4gWEIebWGd4WqEsWs7hHwpVUQrQwYa5wg10GuzirC7Efm-FWlxWedKk6BAdCHzDiv-kb_d-jGlY43eQsxKT13SZagQheGa8j9AYOunOelvoqciMZmgufM4sisft4G3FmMw8weJU2oYaG1zLTfP7-wtDPIilkm_F3yrKs06IJHByuIBSeW0paVkmuKlwexlEPZzKXESrJIPofgOr4NVdC2PNsX20_O2tPeFL8kB5Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🏆
🇫🇷
برنامه مسابقات پاری‌سن‌ژرمن
🇪🇸
بارسلونا
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچسترسیتی
🇮🇹
رم
🏴󠁧󠁢󠁥󠁮󠁧󠁿
استون ویلا
🇹🇷
گالاتاسرای
🇪🇸
ویارئال
🇮🇹
کومو
بیلاسترفیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/104826" target="_blank">📅 20:08 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104825">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qU0Oawwf8gde1Ic6j-7LJQXoI3QCgcdK9N24f9BdaCG9o-oU46YAsXSPUVNtIjgR6Pc8YRjuEN05phssiLzTIgieOx-pCCyOWgxGLQjr-s0b2ChALnv4lyETQssgXYwHj-tCEiq1ALJxtwxW9wI9Y1RbjAd_T2wIzdz9yL-GfbVgKWx8w2AmCIGeUVSNOYgupqrcmNLmY16d4J3rCtjRifJo7rbr3GCtfQ5BOzi4FPUesfg7ZE73UDGqaVk42N5417tqQK_qTaDDaIv22SlhbEnlM5epwvilmWnnE7r96Y_ofV0iJUfcCx_XLuGcrllKervW-HnuJjRJKjr0sSMETw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🏆
برنامه مسابقات اتلتیکومادرید
🇩🇪
بایرن مونیخ
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیورپول
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچستریونایتد
🇳🇱
ایندوهوفن
🇹🇷
فنرباخچه
🇳🇴
بودو
🇳🇴
وایکینگ
🇩🇪
اشتوتگارت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/104825" target="_blank">📅 20:06 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104824">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇪🇸
🏆
بازی‌های بارسلونا
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچستر سیتی
🇫🇷
پاری‌سن‌ژرمن
🏴󠁧󠁢󠁥󠁮󠁧󠁿
استون ویلا
🇵🇹
لیسبون
🇳🇱
فاینورد
🇹🇷
گالاتاسرای
🇮🇹
کومو
🇦🇿
صباح
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/104824" target="_blank">📅 20:06 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104823">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ileBGbQ5-5EHXuPzn2NVozik4WK8g3iRMyVeV54XSZJcM6sYw713T7dZxzhOMcHlsCGb7GPF4-aeeyFz8io1Q3Uor48hQOvsMJh1gk5O4c8zws-bSVhb2Taq25kdpBJCZk41gJ6icYJCwQVxW6KxdzA8OIVr6OCvF8JFbweirHq0KhEWug6kMWNMjXwvBS__xxJrHkGcLZ1TlwV3evDPJGkkRTk_GDy0PcjTDiGKhjHvuYvvHLlH_GgkGh3gBWusMThoeipQeYMoocTPANU-JS0gUdp6MEdM5hvdfNuo-AecPBg8mhRds52Xjj9RBjWaMLQSn3pEcLCVpU2xovuslg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🇪🇸
🏆
بازی‌های بارسلونا
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچستر سیتی
🇫🇷
پاری‌سن‌ژرمن
🏴󠁧󠁢󠁥󠁮󠁧󠁿
استون ویلا
🇵🇹
لیسبون
🇳🇱
فاینورد
🇹🇷
گالاتاسرای
🇮🇹
کومو
🇦🇿
صباح
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/104823" target="_blank">📅 20:05 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104822">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jpNDatCGVp29qdHXfdYv9dk0PKnnENebnnFQ6kNFS9F1HVT1s5Suoj4_5Ljv-LwSiypjQuQwutKHqsR5inwl35z7Ikyz0kqCV-KsRR_cjMhdfk2sA1fSJ-1_KHszxTY0eBgou_wBjZcIaPhT0i6GV1cqfYpgOcyReJBKdxAxlLUhcbk3d7Q7UTKZjg3qMjrK8d_F05XNK-fVC1J3GoWi_MWCp9ntj2lOo06NuqY2V8YcLUJ-j0N-81YlNjUOnGp0CQUGcv4MBhJo78MzJLB54CuGycqRgrpCvq6dD-07zrgq6f5Uh-jkRqYQZbFj5IsZYbWb8YYafXEkRMROLm-6jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
🇮🇹
برنامه مسابقات اینتر
🇪🇸
رئال مادرید
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیورپول
🇧🇪
کلوب بروخه
🇩🇪
دورتموند
🇺🇦
شاختار
🇳🇱
فاینورد
🇩🇪
اشتوتگارت
بیلاسترفیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/104822" target="_blank">📅 20:04 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104821">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
🚨
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مسابقات منچسترسیتی
🇫🇷
پاریس
🇪🇸
بارسلونا
🇵🇹
لیسبون
🇵🇹
پورتو
🇮🇹
ناپولی
🇩🇪
لایپزیگ
🇬🇷
آتن لانس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/104821" target="_blank">📅 20:04 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104820">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFo1E28_1C8lsURnnVqElIe3ZaZOsJEiJdQFZzAauMTCzOwtJ4ETc0JkZEvUM9Tnn0vbMKORqw-YgbWfw2SGgZFConn236z1zjhh918jtXcapXhhpAIDZHe_2rcSohru9tyxpxqUgBEY7YtvN3h7PNbm9dORV6zOiQtGLttClMDUacnx5hZiBJqY2cr8RXnF6nP6L5nE5aTvR4G24Sm-uIfaBwFRRPf8_BcxBFaO5SIFAQPDKYOyZpjGiyOX2YSdlpFn8ZRVSs9WC7VlP5D2kdxMHep8HkwnN66OAMUMyG4BJKXkntUX_vkNdqKopQARSbg-WnpdzcXrPlA-icLxyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مسابقات منچسترسیتی
🇫🇷
پاریس
🇪🇸
بارسلونا
🇵🇹
لیسبون
🇵🇹
پورتو
🇮🇹
ناپولی
🇩🇪
لایپزیگ
🇬🇷
آتن
لانس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/104820" target="_blank">📅 20:03 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104819">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sXmhmD_IVeJh-ByK56Q_LdFrL_et9WNC8o8vDgVh-G8ECkYzm83vbB799Ic8Rqu6ju8-4JUI2NaooneRjNUHpZ8sgdsoHmJFqXBguHCSk1CMbxpKrMxbcUc4X4-Duy-4rlSE_s9Zw0aMXJJprbTa1i6Wfea39QiAnX6dR9wdeD-jUd2EPAlL_qKSfKQ8yRp4WYbtfaY1s4BVfo8vphjHJRvas_NJfoDCyE5soYSq0cAhKiykL7FQ1136m3QkpwUJxBIbyENrvdRsn1PUMvO2liX1TNO7-EYEetMMYyTBw5wp2mtbrUarwNzpiWp64P3sZoOEh1-HK2qp7Y3q5fwk5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🏆
برنامه مسابقات رئال‌مادرید
🇮🇹
اینتر
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال
🇳🇱
آیندهوون
🇮🇹
رم
🇩🇪
لایپزیگ
🇺🇦
شاختار
🇦🇹
لاسک
🇬🇷
آتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/104819" target="_blank">📅 20:02 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104818">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
رئال‌مادرید</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/104818" target="_blank">📅 20:01 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104817">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
🏆
معرفی تیم‌ها شرررروع شددددددد</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/104817" target="_blank">📅 19:59 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104816">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
🏆
#فوووووری و #رسمیییییی
✔️
سیدبندی فصل‌آینده لیگ‌قهرمانان اروپا تکمیل شد. قرعه‌کشی امشب ساعت ۲۱ برگزار میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/104816" target="_blank">📅 19:59 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104815">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIumOR0O5zZ_vOa6-vBAKcZjYTALeHPbt0EKDslOb69ZHZAqHOssCc4AekPHJ_Gmr8RloD_eetTMvg6PovHuvsvcIkGY5JWDtXGVBqT0ruTEKZwhD7fm1-4kaWRHXgrenE-DK8QPq60VH_BKWbdy1e-1hpFOsnRKhm5xFvSoIj77UMBGGVScm03Eo-5vOJ-Dp4a6HCtidOWGVcCGiyIJ0yrDvUSVR6p9W6jqv0h-QDu33WUYslzatkbd-wg3t3bFR8q1n2g_W-INwDq5TQJ2PFQVjCakFBfJrw7QmL4dr1Mn0lvepBBR8YjBYF6Rf4BxOtxSGhMo4ixvfIGPQkOBbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
شررررروووووع شدددددد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/104815" target="_blank">📅 19:54 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104814">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">⁉️
🇪🇺
سؤال مجری از دیوید ویا: احساس شما در لحظه‌ای که در سال 2011 با بارسلونا قهرمان لیگ قهرمانان اروپا شدید، چه بود؟ چه چیزی باعث درخشش بارسلونا در آن زمان شد؟
🗣️
🇪🇸
دیوید‌ ویا: در یک‌کلمه بخواهم بگویم لیونل‌مسی بود. همین برای یک‌تیم کافی‌ست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/104814" target="_blank">📅 19:53 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104813">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/seI7DVkFoE02R_HCoZbZ11SKY6LAq-ZOBucALGADL9QAclZ90wZ--isj79qz-YtUs61-S_uqcovp6MK4GLDim7PHZ9qMqpIPgDHABtyzn8rrgf99kpuU0rSd8hOM7XNcalUuUVRVS8FcFRnZ1pufQYr6RZGUbn-MOYNrH9oCHH3De5C2gcOW7jIzeMwPIZAT5nT5wAsTkVkjxgEJCMGGMcsSxsmbbBJ6gtzjC8mlp91ZrgIkCJg8ldUYkvbserTFMF0owqbbteW-rPADVM0EnBwY11jHc_NMoLPSc4oLMWjf8QzIjDKadlCyUhc2ryMtALy9sufn74TbBE2o9_faIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇺
‼️
یوفا اعلام کرد که از این به بعد، صحنه‌های مشابه خطای هند مارک پوبیل در بازی مقابل بارسلونا در فصل‌گذشته، به‌صورت دائمی از این فصل پنالتی اعلام خواهند شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/104813" target="_blank">📅 19:46 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104812">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ll_gHZRYfkiBQQ1xycTj41kBl2S-KStLDZm9vUz5hVgpufzvVRevbiLEh_Bnc3omUMYeS-4Aaq4sQusZXYlC-YTO2UnSO0IU8eyuQ_mVoGQyGrcAMvgtcwz92AJHb3H5cjbLx0-3SZk_-P6CJhpQcmWpn0TQ8l8yY-TEnTCUqLjZYL9naTxAnfY85zayxFIiy8TJqpAhwijkQt8FxQgy43L_BTk7nArmGlqU38830GVMQcxaZJq1N7oGQfFzCVgFAg70ogV46BcbjaGigC0qh-IdWZzKFReiw8a8sJlNmLeN5ZjRD4R_vrqxxQqaEZ6j01gAgkx7DAQa_UZ8ed9Bdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
تیری‌آنری هم این وسط یه جایزه گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/104812" target="_blank">📅 19:42 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104811">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SYJ62_ZvxQh0oW0OaLu03OXpVU7as52bafJl-c-lI_efVfP6XTIAh73s1BPREy8OHVF8dY8wAhKUsz5dhbZMTPGxDDMIEaS3UpS8qtMApYLZufdreUBRBwz09QW9deUy8KboPrTCMNsr70Nak12eZGFVAOjdt7Yl4gqrSlFR68AjuMmoQ0KxvuPlveeWe3XMv1z4hPzlDe3r2UkJODCsceahKhHVqBKrGCxPgAjQU8eazeJn3aOcB01B06o6cXHcowDQokPcUtnfyHPD2Knkpckpwtsu-L3BAspm_eA_RrLd6HWpg4z32cv1-a29zMunlwdBh70j8Tcwwo_DWf1iYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇫🇷
مارکینیوش کاپیتان پاری‌سن‌ژرمن برنده جایزه سال از سوی رئیس یوفا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/104811" target="_blank">📅 19:39 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104810">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EWxgB6EUjChSkq8p_bwWwMNpHJF2FTZ5NaIR6pEUDoCyr1FfGy62EHHaDDS6qzbhqzRzkUK97AeOJzgzuP3RgQ5WdgUKmvzoNwBjYFy6CarpoNt3ku-36dlP7SWEjmG7rcNGfytNRWrFE1zoQiuuFjp0icrO2g97gLHwN7xbvZylbUlruQWjtTzb0rs-SUr6Kez_9Z9zWQPuB5chj4Up7ozy_1yp328Y-x9FOj-zdBJtYbCoirCxtuDeZR3lT1NJLuPGe8xXN0DnenMVPattxlSTgR7gyHmLn7iDvUW9fkCOZKQ8aPwnJMArUTm1U_pZZ_NfFr-UNwbKujl1pY-UDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرعه‌کشی آغاز شد. با ما همراه باشید
❤️
🔥</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/104810" target="_blank">📅 19:35 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104809">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
🏆
#فوووووری و #رسمیییییی
✔️
سیدبندی فصل‌آینده لیگ‌قهرمانان اروپا تکمیل شد. قرعه‌کشی امشب ساعت ۲۱ برگزار میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/104809" target="_blank">📅 19:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104808">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ffeeffdde.mp4?token=RZMYH7CchiANlwaTZd9cF6ejOXlMZECoDKd_yOYnsUZ8AC6i5fcmQ1twYzjyiC4JwauKnxLwZbMfOa28LBzkcLysChBM6kmKbB6U_tVU1J-egJ30-EkLe5vrF0Qk7fHNmbBPF6O0UX_1wPo1qzuZ8-CHjoX6cByAlfBNAJHkz-Mt8T3FArIpyT2C4VkB8PmXXnYVAfqGYAUHW7Jr6XW4j8ITQ5llxoHYcXmakEoaN3DSbSoQMUMd1B1BNydP6vhU7rFTJYgDbDbkllrkfl5P-MtzHvZuGwPyxPp-bjHcSRlifb_G5GKrJ4HSX-X4kKz0_Oqf1Nwre6-sk2GFTMJEuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ffeeffdde.mp4?token=RZMYH7CchiANlwaTZd9cF6ejOXlMZECoDKd_yOYnsUZ8AC6i5fcmQ1twYzjyiC4JwauKnxLwZbMfOa28LBzkcLysChBM6kmKbB6U_tVU1J-egJ30-EkLe5vrF0Qk7fHNmbBPF6O0UX_1wPo1qzuZ8-CHjoX6cByAlfBNAJHkz-Mt8T3FArIpyT2C4VkB8PmXXnYVAfqGYAUHW7Jr6XW4j8ITQ5llxoHYcXmakEoaN3DSbSoQMUMd1B1BNydP6vhU7rFTJYgDbDbkllrkfl5P-MtzHvZuGwPyxPp-bjHcSRlifb_G5GKrJ4HSX-X4kKz0_Oqf1Nwre6-sk2GFTMJEuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
تنها ۲۰ دقیقه تا شروع قرعه‌کشی UCL
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/104808" target="_blank">📅 19:10 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104804">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SkANIfTdqMW-OWSxnyXkChQQdaC2k4y3ZatRYjNPB1Eum4LVTBZ7dLqTqlzFG53ebBkSyODO0C9eWtz6dh_AcyAkrFQgpcDWT8NMC99Adi9B9O_mwr5iyNipIW7TIfEVq1GA-I2QdsRwco54pDtrHOZLUJBJBFbsiPkgZa7S4IKXoGDAJk5y78tKYiLQGeCT3TboEOyuYC9Xlhz69XHDtM7zzbo3WRLObQ35gYxeRYPJLiy7d5_Ton4zdxO1bh0MBFyqIBWiESeLljfi0V6xazXJFTKSlj8MxYDoqp7Zhsg47IWVhM8wtd6Adhn8GX9Ti0Q9fIDCkzA2tiCyYZosTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DUeU-azJMfitEi6LiJREsCyoTjlpwmvaJBHgNJCYEmT7d1fOLcWoh6rTSzBGp_eME5YnjlSqw-dqsl5FvoOOIl_Hn62ru9_Pneb52Xw0MzlacFophEZoWrB7lqPF8EBMTQgWDYKhxN30Ku4hil85V38kh2r592WgelMRj2sc0mYlRJsct08olclEFmLxZ2_N-BNBokdXq_VD5j-i72TUb5dD1p1PohtDnwiav36LY1jRYnrlz5egGfDFRZpD8a-ihigvYfHHq17H0yACqzc15bON-4USsCOndHZlxAiGlEUIsOh975oTqQRo06t5d0VDOSOvRgy7vu0aqtMN7gwO4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jy9Gk_E1zr6A6CS3RBm0gtrFa2GnuWui02ci6dUJ67caF7AQRMvFKWfnK2B9IGjLxOJ0WidzyecqukpdPxFX4JkfUmPlt1mMew5zGIXeWmS3jl6bV1yycpbJ4aqdF7srcXIVyH4y0Ern-1WEDmrk7B6xQkzyMuYfiSCpeWIYTn0RvqddTBGh85tXWZ74Eh6t533rbp4hTh4eGP_u9Sugo9uR1K9jLa7hRnxIqXB8uJnz58f72u5KmvW7LMU6KXjpf--hrZEkoSbCPn4SFvZOyVvMEH9_y8fCcLzNMicR8SRs7EQmn2AIQ5LpEIJreF-6rbmuvrXUIQWKYO5s9aLGVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XYvU-f3eixBqH_c3zNBMX-KxlTQx3BojO3CrbOI4lwvFlfEoXw45n_NWmRoQ4zsRQcD1UsFfc4Nsq3dwSwd2pRFNGNIGQmzSzmTrqPjs_iyEyZEWpUb_3tpBhbeAHCvJNNzL8gOqb73XqkZr5LSxvFEAIDMWperHv7YyELLA7WiZiXmmYbSknglzXhO61nOR7h70uqsq9tGKQnEmcJPrWfXhRhHoSYqsmwH5yfBH3nGUsQhYe5feBfQzI6rWCdOOYYbe44XFjoQIJvpyR60TI-tj9NuBEC-2oKcXir70JO3hxVJV7hbGeUqAyRJdQ8UB8EjICzoWoAnOqxaCf_LXrg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇺
بهترین افتخارات تیم‌های حاضر در لیگ‌قهرمانان اروپا در آستانه قرعه‌کشی مسابقات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/104804" target="_blank">📅 19:08 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104803">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KeFRhgciZ9HgS9tPHzRuQJ8k_31mAZoDHduDUFXzUudyoxUuCvhd-ZnOaguU-_OFgFKBlplrTVYAGhvXD8G28bKAriDO2mG6bA6s4sN3ZDnd6yPRaYExRnJsO8Ab3yMZl8mxAztvd9_Us2gPPfQiR0J4bXQKg2uWyBaw3VRDIQ8yMGbfEZmF5eWzvBTzPe0OPWqbnVkFEB3XgVadp0YiXMSxdWUx92em0jr6VCVS2smMOhzRgdiy74CoJvBzofsWD_imHLxifhh0ZcZQgJpgXlxeMoR7maxMfe23FgDgsviN3mJp6gWOxoSYwV8JUrAiZlxMXEGzGsPr51A_R9zJWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
بهترین افتخارات تیم‌های حاضر در لیگ‌قهرمانان اروپا در آستانه قرعه‌کشی مسابقات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/104803" target="_blank">📅 19:05 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104802">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ac7aaf7e8.mp4?token=P30vInlfZh6rdBsbgGXxvmkHJQssYoDluSaOYkToCyFdqqguJ9IThIdv-tanEZ2z2EBvgizDJc5IScYf7qrI7W_l7JT0pZAdUlUqgJt6rehu_hlT9eRM1_gIl_qfWuRflAP2BTf1a65vcE_Exq3R24XjZsLUstuCrPbMlJUbiArl8k0cnoX5YcxLfTZhTxPqLnuwx5A6RiVEBupcmc1Qhf9TvfdFIyEQaZ4cfoQtfP6mqA2ggsjMTPfjnrYEz0d_q87CmrbywIIjvL2XxQBp8l1GYa02cm38Dnve9TEj9Imxb9uVyCkT1zWGIJTvYK7651Lm_TPd_9NjHDlJxKnFDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ac7aaf7e8.mp4?token=P30vInlfZh6rdBsbgGXxvmkHJQssYoDluSaOYkToCyFdqqguJ9IThIdv-tanEZ2z2EBvgizDJc5IScYf7qrI7W_l7JT0pZAdUlUqgJt6rehu_hlT9eRM1_gIl_qfWuRflAP2BTf1a65vcE_Exq3R24XjZsLUstuCrPbMlJUbiArl8k0cnoX5YcxLfTZhTxPqLnuwx5A6RiVEBupcmc1Qhf9TvfdFIyEQaZ4cfoQtfP6mqA2ggsjMTPfjnrYEz0d_q87CmrbywIIjvL2XxQBp8l1GYa02cm38Dnve9TEj9Imxb9uVyCkT1zWGIJTvYK7651Lm_TPd_9NjHDlJxKnFDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
🇮🇷
آغاز جنجال در اهواز؛ به گفته هواداران استقلال، لیدرهای فولاد شدیدا آبی‌ها رو‌ برای حضور احتمالی در استادیوم در بازی فرداشب تهدید کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/104802" target="_blank">📅 18:57 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104801">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🚨
✍️
سامی‌مقبل روزنامه‌نگار انگلیسی:
🇪🇸
اتلتیکومادرید سه روز پیش به آلوارز گفته که بارسا سرش گِرده و از خیالش بیا بیرون
🇪🇸
آلوارز هم از طرفی گفته یا بارسا یا هیچکس به همین دلیل سه روزه خودشو به مریضی زده و تمرین نمیکنه
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال و اتلتیکو توافق خوبی…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/104801" target="_blank">📅 18:52 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104800">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06afe0fc50.mp4?token=FOh2xDM54R8fYCSEQ6BRCvIIJng7-3_1wJLjp4U5qXKqTd1ylGPYDxTomPv6jJcmH6wZkwYNoCAuAMRqE1H7ZbVWpDvNJS3aBGCRVkHzVRZFdcoIUJodDctcAmuhAKP_2pqa9z0OrMaApgJXfIWpAVtThsg_9Ldq9HuYuXMj8ue3b3PA0M7dm39FNe1pc9WTda_TWWd49ZFWkcdRHDYUk1Ku6ipImF-UYA68RrCzIU0rb1szC--Je_BHEFm_3Z2uXV42dGktwR4PP6Jw5Be3fY3ZzqZyaRV9kifC3DvBMdWnWnZMTLtOUdx_M1YlUwdYQAekRFPEskDgOmEBpcJFwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06afe0fc50.mp4?token=FOh2xDM54R8fYCSEQ6BRCvIIJng7-3_1wJLjp4U5qXKqTd1ylGPYDxTomPv6jJcmH6wZkwYNoCAuAMRqE1H7ZbVWpDvNJS3aBGCRVkHzVRZFdcoIUJodDctcAmuhAKP_2pqa9z0OrMaApgJXfIWpAVtThsg_9Ldq9HuYuXMj8ue3b3PA0M7dm39FNe1pc9WTda_TWWd49ZFWkcdRHDYUk1Ku6ipImF-UYA68RrCzIU0rb1szC--Je_BHEFm_3Z2uXV42dGktwR4PP6Jw5Be3fY3ZzqZyaRV9kifC3DvBMdWnWnZMTLtOUdx_M1YlUwdYQAekRFPEskDgOmEBpcJFwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اختراع زبان جدید توسط علی‌منصور در الطلبه
😁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/104800" target="_blank">📅 18:50 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104799">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bdsKnw-K1fCgGJ6No21-Lz-7VtqXXOBI0lG8MEcEP8BAQgsdCQtz4aiGlgKfpJBPrGltJraJlgSOXrHJaouBd3IXk3OdZqznCk60ii8mv_w8r9gDU0otKUuOW_z7HAzVamh64Xz2g_lu4zAHhH1WHNVfMucTv-8RES07PftCnUyUZ5dVRs4Uj76cG_6zY0f5b0eAICt8fzaeIACjCewwBeX80De3sfz_WMtsN_cw9t2Rch4n3EQoIM1SorSjuVGohiHAP1I1Kli5V3tgUG5nTEE6oD6wHqIYFcTwVP604TLzwUiOHtMahXN08ot_5gDHSH77aDb-zGmqbl3SkSdECQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
روزنامه رکورد پرتغال: رافائل لیائو با رد پیشنهاد گالاتاسرای به استون‌ویلا پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/104799" target="_blank">📅 18:45 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104798">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‼️
از عجایبی که فقط در خاورمیانه میشه دید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/104798" target="_blank">📅 18:35 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104797">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PBXdL5HwNwnPSSyA5-UWXpcdkSBmPOj79PSWRYZKJXcM86e6fWa7OarE8900iIePUJao6eLRl0IXwgFn0nXlmUHljuxxod3jHrSDdwiajfvBpHV5_6qbUoIjBy_nROvxtoQnYlaPgGkE0SFfobQOVledNRneRVC9iVxFx2-6XlhTXacwE-EhN2Fw-DDBqTmxWtoWoADFC70JPypH9flJuLR_2swDbEg6L50Lo82504iPrMqRfz1nmnfvY0kU7auL_1fe5EnmP8vFEq0Oaeo7k3zsCnnVf_dfEiwU2mFm6wRn1OvuF8_oTrgWMjoMVM0qZWlSk42bAyEtVqNjjAGVfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
✍️
سامی‌مقبل روزنامه‌نگار انگلیسی
:
🇪🇸
اتلتیکومادرید سه روز پیش به آلوارز گفته که بارسا سرش گِرده و از خیالش بیا بیرون
🇪🇸
آلوارز هم از طرفی گفته یا بارسا یا هیچکس به همین دلیل سه روزه خودشو به مریضی زده و تمرین نمیکنه
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال و اتلتیکو توافق خوبی دارن و به محض دریافت چراغ سبز از بازیکن خیلی زود شاهد توافق‌نهایی دو باشگاه بر سر آلوارز هستیم اما بازیکن تا این لحظه شدیدا مقاومت میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/104797" target="_blank">📅 18:18 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104796">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80bc2fd38e.mp4?token=ZK1TiJS5RAyxKf0DsHnp0GOMHSxNSkNSQcnENqaA4DXc9jNirxHigt8a1CpIkjHig3p0w-nqk7m3ITenFHRk_i8g3jLgAUE3cFOcHNFqf2bWZIqw8s1J7E4bQYFSeGsR2ijMgH11fvt805jkWgyZmglQ3CIIGAXYHqxanN9uvnOkEKm0N-yIc9wD5yPJ0A5HwQkvG-X9ifmBsFrOdsL0C50FQigHuszn3HdoEb0rZDnGQMII-i1reychV2Ps8jGfXRB_hG-gMGetekXSvqweE0JghMDUXCRXq5xehEA6o3gyJzsKubR1TOL-8yXDebVNAGoetVX6LH_buPcuWuQHTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80bc2fd38e.mp4?token=ZK1TiJS5RAyxKf0DsHnp0GOMHSxNSkNSQcnENqaA4DXc9jNirxHigt8a1CpIkjHig3p0w-nqk7m3ITenFHRk_i8g3jLgAUE3cFOcHNFqf2bWZIqw8s1J7E4bQYFSeGsR2ijMgH11fvt805jkWgyZmglQ3CIIGAXYHqxanN9uvnOkEKm0N-yIc9wD5yPJ0A5HwQkvG-X9ifmBsFrOdsL0C50FQigHuszn3HdoEb0rZDnGQMII-i1reychV2Ps8jGfXRB_hG-gMGetekXSvqweE0JghMDUXCRXq5xehEA6o3gyJzsKubR1TOL-8yXDebVNAGoetVX6LH_buPcuWuQHTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
سخنگوی دولت:‌ مردم منتظر بهتر شدن وضع اقتصاد در سال آینده نباشند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/104796" target="_blank">📅 18:10 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104795">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPDOqdYA1-2che1WmXMx4_IWiHHJ16IC_4MNeZ9zH0h4Ad30FQlinKlx-yw_N4WKkotCkq6BnHtVZziwaEjnsldwKeVrmPsygKRI3CODjHl8IZZZET9_AEpgmnKl2Tw9yY39x20QRBx5c0LYcLoSFjHDlhUV8_Su0K15oEeVIrWrjtT8ItesONqOxmyGkavVNY7fFTBMrLc0ahtULSK-hO8r-VpD1c_PWZPrOUCAR9RrvisX538LB5YuwsDF7XeDaPNyxgY2uERj5eP0s-JZt-gu72RKpCakwkvXJg02WvftxlCk71plMO9KhsE7dOw9UWtmnfQuwgQ2rorFJVaUWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمیییییی؛ عمر‌‌مرموش با عقد قراردادی قرضی با بند خرید اجباری به تاتنهام پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/104795" target="_blank">📅 17:52 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104794">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jI5KhlMxAeI8FC2CVIePWMu6LeoCv_AFN8mxiuLp-LbRwDbdkuFodGV7SBzH8SDuMDHsd199bsrYUcaGg5K_9v4qaiUqRaVsRw8I-MmVVsuIcIjxLhwhNhtUTGe58S0_nNR2qHgid6k3SlUqC1uQPk7AyZMhPfHZNok4G36ZEQFYh_AR1yyZsuwtZptIfCpLR2vgpoL3xQ2N2CX3y7RH3cvLOESNZO7HPjvrT50SrVzywU3AsF4kFg_SrObKb6bCV5sRW2TBJD_DySePhGnwPOTRJGILliC4pwn6_Kbyo2PgkgLyRFc5KsZ_ufiMQ3u8L3PupNy-w9QhaderxVeYEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🟠
پوستر فولاد خوزستان با تصویر رامین‌ رضاییان برای دیدار‌ فرداشب مقابل استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/104794" target="_blank">📅 17:39 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104793">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JgtTlxFpsVX4difjjk7rjfd2HdD9qxZCppvBIH1v-4673OgDs6mdqnzfArDLQWGVjVHLNaAotXd44TlCkrzciiLRp9CvJ0c-mHe-A_54SmTDTuSV4FNagBPMmYaycLsX0VD1f4wg8MzQ1FAUjRhrpPAW4_P3TTyE7LmvaNX9BbWzN6ZYJIqKzq23u9V0sB7IGWuGRvUDyuXg_FVrcSPaWhjpyw73Z3MRPVqd6654BfHqjxiykxxebJuYXslcAUO-LCq-1NFJp82ZTbEEoCqMvMmuhePDEJSB52afkhI8Ta29eOpeDa9UaLeNVbJRHCWQBydvzbWqIdxP9C7GGSnGPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمیییییی
؛ عمر‌‌مرموش با عقد قراردادی قرضی با بند خرید اجباری به تاتنهام پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/104793" target="_blank">📅 17:36 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104792">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/auuuE1PMpqngXt7s5uT1q8uFZowob5V5MMlloTFbMwpKcgcpwPL6wUP2u4TdSQqvnYUZ86wnnCQ7P2X62VG36vku-lt0kWB9E4yeA1Bhm_PmMzQDzZuX_SNHw5R6x7W8X97HrzbVxcQXhJYILmauLIBWaK6Y31gQbRx9ZOPjOiKVxRJ1gYBZ92-2-NUyQwzY__qjfrcKv2MPTQyumO7UnooAc2r91LLeijsca7zsFEzJ27QF9ugZ9GZepXf_b2CKJlQZUJvFQDaQpymzW8PXPGx1eFx_dKnenzPvAZNjjASOt9jb__mB2BeoRxW-f47PEDkTZnybT4_N-4txsHHaAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
✅
🇪🇺
سالن محل‌برگزاری قرعه‌کشی لیگ‌قهرمانان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/104792" target="_blank">📅 17:09 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104791">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3180f2f4cb.mp4?token=d2GhEsfmHk25tpAjO_ik9h46yrwgsX5TPUDq5yBmmaHRQg-vEG6jkPdfr72ZSPFYXRZXAHz87FbICLuR9r06e6eBitCt8A-N3Cpl81OUPEK3xvCSzi2PEr4XfdJ3cHL-_0QCBTX0ZD8ej4KQkxfFcpdPtd60mWAQJVkedM0CWrz6h83GD6BTOff0dU8-Izs2cA_tdukPSz94WuKAhj_x3TY2h8PyL34UAz5N-mq6jscSzdni7L0jpCX7tpzgYsZEqfswsB4T8-Krp16S6C4uhnPdOPpn_SeHUqpB9hd_riPiRKhG2aOlQDbc63023J7FSvunmeUEnd33UVXHu624Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3180f2f4cb.mp4?token=d2GhEsfmHk25tpAjO_ik9h46yrwgsX5TPUDq5yBmmaHRQg-vEG6jkPdfr72ZSPFYXRZXAHz87FbICLuR9r06e6eBitCt8A-N3Cpl81OUPEK3xvCSzi2PEr4XfdJ3cHL-_0QCBTX0ZD8ej4KQkxfFcpdPtd60mWAQJVkedM0CWrz6h83GD6BTOff0dU8-Izs2cA_tdukPSz94WuKAhj_x3TY2h8PyL34UAz5N-mq6jscSzdni7L0jpCX7tpzgYsZEqfswsB4T8-Krp16S6C4uhnPdOPpn_SeHUqpB9hd_riPiRKhG2aOlQDbc63023J7FSvunmeUEnd33UVXHu624Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشکلات خاص در‌ ورزشگاه‌های ایران؛ ورود آقایان با شلوارک ممنوع!!
🚫
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/104791" target="_blank">📅 17:07 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104790">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frommydiplom.ir</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m4GDlpk5RHN0JmxxsX6kuAzffh2X86szab5kd0SmMWgZgBJhXrz9CI5NvPyvCdgoG8_aJ1OGRT1atTbToIoUFU2MN-srTHIyFP70p7fzW4FUIEwPm8ADwuHgjpav33PPssXnk8FmDtglpanQQBq4roziPqhCvwJ8sxuZl8Yuw2qMnyKbS6XTjZPSA25gH7j_TdRGY4yOtvjTH6O9ieeyQvkbeCoCvOrl9NxnSiXpW44KbfMUuve_ysV0JmR6PVSfiX_B7cSmKQGFxZg4K6LsVLvbGyzG2YUlTMu9zMO0KDqs44qwPqkK77PIIOCPh_OXFl9bKCWbL3qzGH2382uPqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👮‍♂️
مد
ا
رک رسمی تحصیلی «مقاطع متوسطه و عالی»!
✔️
از دیپلم تا دکتری | کاملاً غیرحضوری
✔️
قابل استعلام قانونی
+
قابل ترجمه رسمی
✔️
مناسب برای
:
مهاجرت
|
استخدام
|
ادامه‌ی تحصیل
ارتباط با مشاور
:
https://t.me/mydiplom_support
ورود به کانال :
https://t.me/+lHweVa-y92IyZDA0</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/104790" target="_blank">📅 17:07 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104789">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fd2815717.mp4?token=Nm_S44PTD0IdEW6WWAOlR-wxm8nq8wMU6AD7lpNY7xdiLFB0V-FFYILSv1rkdahdDPO2iYqZk_R8-Gr81J32u-XaL93m_vtMT1iijLJrdWFSvQxTp-bZn7b1a9BX_9shCtq57axf3VqmEIOStWjWUZ0iNKJD9ygrXLSI4f9v2mWG-RkM5BnfU8wYLcD4vwQylPydMaiRY3L14q77eIiquRSBoiv9J8w6oMZFq3OgVsKi2B55l6RF68I1ERnHKOgnTXO66o3F3XQ3ZqB-a25ZTVgLk-YzO6FY2zkAZImP5TbdgoVubiTRQJFNHUU5QJZ2HAgRg_mByDwePGO9Re5TNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fd2815717.mp4?token=Nm_S44PTD0IdEW6WWAOlR-wxm8nq8wMU6AD7lpNY7xdiLFB0V-FFYILSv1rkdahdDPO2iYqZk_R8-Gr81J32u-XaL93m_vtMT1iijLJrdWFSvQxTp-bZn7b1a9BX_9shCtq57axf3VqmEIOStWjWUZ0iNKJD9ygrXLSI4f9v2mWG-RkM5BnfU8wYLcD4vwQylPydMaiRY3L14q77eIiquRSBoiv9J8w6oMZFq3OgVsKi2B55l6RF68I1ERnHKOgnTXO66o3F3XQ3ZqB-a25ZTVgLk-YzO6FY2zkAZImP5TbdgoVubiTRQJFNHUU5QJZ2HAgRg_mByDwePGO9Re5TNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚠️
طنز تلخ از وضعیت اقتصاد مملکت
🙂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/104789" target="_blank">📅 16:55 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104788">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc2ffd8aad.mp4?token=AvmpfVYTu0b5rPuMNmPyhSeIuPrWVp9WxsMNMuKgx4WYtbTBwWSGfjnx-6dtu-tU4x4LD4y8arSg_DTyBVh4dbyIf1LCsCF9iGiwRRtPSUbD-LanNyButPEOuWRLOq6WpKZ7LpS7SOZa_qk3-NyjRgWt-Q1LY2ojW03jABB6f-nQps8tvb2N7378B7pRzW-3gDEMVHrXCx0feBvxcXoCDZuEDOsx85Gzu0ebRfnDbxasE7Y_1EHBccw6YDR76lFX8ttjYa-K7WjB7ODivZ3dx0WoeSiAJDdV5j2tq0ZZ1mrX98Dv_6JLwDr0e2RFHp24WjTwQMrzHwZp_kS4Plp15w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc2ffd8aad.mp4?token=AvmpfVYTu0b5rPuMNmPyhSeIuPrWVp9WxsMNMuKgx4WYtbTBwWSGfjnx-6dtu-tU4x4LD4y8arSg_DTyBVh4dbyIf1LCsCF9iGiwRRtPSUbD-LanNyButPEOuWRLOq6WpKZ7LpS7SOZa_qk3-NyjRgWt-Q1LY2ojW03jABB6f-nQps8tvb2N7378B7pRzW-3gDEMVHrXCx0feBvxcXoCDZuEDOsx85Gzu0ebRfnDbxasE7Y_1EHBccw6YDR76lFX8ttjYa-K7WjB7ODivZ3dx0WoeSiAJDdV5j2tq0ZZ1mrX98Dv_6JLwDr0e2RFHp24WjTwQMrzHwZp_kS4Plp15w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ماستانتانو در اولین بازی بعد جدایی از رئال:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/104788" target="_blank">📅 16:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104787">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2544620852.mp4?token=rcKlY_cRdPbheKJbFGx1hQMSbx6WWa4dLLO3_jeRXLIJ8zV2qg7KMd11hmkPyXF4pLM0mzN8V7H0OtYp840-mvf9mZzPiIQhYfMR8it-GdTz1FfxoRTgGu_fWcnaXOPKmwQWDdZ4g_QZkI9hekUGLIPL8MU6e5Bc2CUvfivegP4P6nH3YNrVzdf4OII5gHiwbtfiyKRRQft_yXLRZnDznYP9ab_bNnfywXaeeXnJPRZahtZcObTgdwLTuudxwWqqCTj4Ht8z1pHlDjeeRM1sQC2Tk-az-fDO916PvWfm1kwwbTI6J_9If7J5Z9KeVisJ4VfFY2j3OW6hJfPZ36lNNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2544620852.mp4?token=rcKlY_cRdPbheKJbFGx1hQMSbx6WWa4dLLO3_jeRXLIJ8zV2qg7KMd11hmkPyXF4pLM0mzN8V7H0OtYp840-mvf9mZzPiIQhYfMR8it-GdTz1FfxoRTgGu_fWcnaXOPKmwQWDdZ4g_QZkI9hekUGLIPL8MU6e5Bc2CUvfivegP4P6nH3YNrVzdf4OII5gHiwbtfiyKRRQft_yXLRZnDznYP9ab_bNnfywXaeeXnJPRZahtZcObTgdwLTuudxwWqqCTj4Ht8z1pHlDjeeRM1sQC2Tk-az-fDO916PvWfm1kwwbTI6J_9If7J5Z9KeVisJ4VfFY2j3OW6hJfPZ36lNNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیلی که دیروز توی نپال اومده
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/104787" target="_blank">📅 16:05 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104786">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12ccdfab76.mp4?token=NfEv3rEjRsDc9xbZj2dnYqKyjU5MqlP2zMAt1qmmRuelmosif-HUZ_UVDLdbo6BIgXVDd2W_nh1csJyEe84J_YsIwyqHIAke-WgCSdujQvw2OfeVYuU-pxJlJ7Gxh9lgd_cDM__yfG3LFwrZE_msZS6esos6aOhl8ulpZ732hyJQzpz-_5tOqpnJATBawyPiK2h378aFtqt6ii10d7Bhe8eCFmi32Z9ON3ieQ4lRL-empC4yAQmM52HRwJXbbQ9fSXnGs1HnksEu84pr-UzscGI_cPwG4B4af7jX9BaUupKhsfm51sweXWXASjJyGq0GxEPRVdJ59bZ1MEW3kSFNuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12ccdfab76.mp4?token=NfEv3rEjRsDc9xbZj2dnYqKyjU5MqlP2zMAt1qmmRuelmosif-HUZ_UVDLdbo6BIgXVDd2W_nh1csJyEe84J_YsIwyqHIAke-WgCSdujQvw2OfeVYuU-pxJlJ7Gxh9lgd_cDM__yfG3LFwrZE_msZS6esos6aOhl8ulpZ732hyJQzpz-_5tOqpnJATBawyPiK2h378aFtqt6ii10d7Bhe8eCFmi32Z9ON3ieQ4lRL-empC4yAQmM52HRwJXbbQ9fSXnGs1HnksEu84pr-UzscGI_cPwG4B4af7jX9BaUupKhsfm51sweXWXASjJyGq0GxEPRVdJ59bZ1MEW3kSFNuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🇪🇸
خولیان‌آلوارز در قفس آهنین خیل‌مارین!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/104786" target="_blank">📅 15:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104785">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SC__iwt_JHP58-EZ_4QUBC4R1belFinzr2jmg4lHrWgzKj9rgpfjo_w7XJxYx57D0EPFf1J6Q7Kd2TSta173MLHmctj5LmMYc6yysSjHzqHvVrbvYho8Uwe_rk5t-l4ZRAePAl6jHb3XHSq9Lmymqk4ucOoo7xRVGnzrUr3G8STVQgVdCPbEaTBoyQaorWnPOZkXZFOCK5V99ailHU9MQ05FvEWHibA10Kd8OsvfGQ95NZVt8LrTWhG3o3Bhp4j1UihxRW4MSNER3qqiL1KaP14b4AMYj8l-5alFSD01a9_96pBiy_uK6H5S948U-sstfmbGS2gKI8r1nzxv59Wr0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
شماره بازیکنای بارسا تو فصل جدید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/104785" target="_blank">📅 15:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104784">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GX6Ych6_Uz6zzy7BS9HS8fmGoc61Z1fn8GqCA_A1K0sCs2s_I4KncOpmhjH4j8IMX4fpA_DJpv9RLhlAFCOlbeG5c_K0yvfzMmkMQKfUN1GeB4XyorWhojZK6HY6NveZQZtLW0n0dXl8qLDHq3mC2vWSAKrEJkn2_T6Knyt9YTmGCAaxluqkn30GkinQvDnMPC0tK1oDGm9AK4jeszQWOBCXx1GCJS8XoywaZz_9WkDlu5Zg4sZDEn6mL25lvj7n2bRy1ivO34bXFWIeBS88yiHI2lawkfxITGehWZOEAb-Jtp9_YRIhbYQw8Pg0uWpv3m4IX0l_GNQMdfIQ9F8Zjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🇮🇷
سهراب بختیاری‌زاده بهترین شروع استقلال در تاریخ لیگ‌برتر رو به ثبت رسوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/104784" target="_blank">📅 15:15 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104783">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJpDdOz2Z-qYdSpP5t_GVyp3eoStC2VjMOZj38-CMN2ZTg5xrxuw9E1mBHi9ySq5wfZkfruN3flg0MjHoL3OdJYqgLyRxQ3U2hUduyfC-EW2GAQLAYDjPyIk6712SXlsd6THDAtvjCRE8zpT-YReL19mJ28Tif1sIx3KEVyoXob5oFDRFWdH4408xtLcwFHWgWcjtKKvqvQ0nrzvPZM0RNIltXAp5RiQENSXJC4VaWN1eOkvgJrZ9zK_6DFIda4Rkrc5wDt-sMxXhsU3rrrs-2pTnKUYRdi8rQFxNn-coaSoFi9Bt0Q-IZUo5AjZ-1wPtA9XjbWEzXlXk2YnqknFAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🇪🇸
لیست بارسلونا برای بازی امشب مقابل بیلبائو با حضور رودری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/104783" target="_blank">📅 14:59 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104782">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ced5cf8b4.mp4?token=l3rMikejtjudwk0GRoqAFyE_D64ydseJdxnG51srSW1R_L2OgRZd-9Dzl-vQHOREyUGpmlDdotR8P3gyC8S2l1ALV8bQbZzhJIaR7x0ouNqcIh_bxLmYnicuaCoBMPcoGtNtka03Gr4WwZmaWfj4-RWZi9GyIjLvUqVPEX1hTsOHOT3KXKc6JGzLKrTcQQSe8FLq6k6G5QSEy9wK3hDGth9sHfMSHvxhPe3boyi8NQXc1b47VkBHvL6ec8wQD4KvxAsey80Fad-Kz53sv0flMM63C9e7J3faFobkwYLkc2NWjD8mgqZyPnpLM2HBvau4-zssBbTfLTeUJCzk6-8O7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ced5cf8b4.mp4?token=l3rMikejtjudwk0GRoqAFyE_D64ydseJdxnG51srSW1R_L2OgRZd-9Dzl-vQHOREyUGpmlDdotR8P3gyC8S2l1ALV8bQbZzhJIaR7x0ouNqcIh_bxLmYnicuaCoBMPcoGtNtka03Gr4WwZmaWfj4-RWZi9GyIjLvUqVPEX1hTsOHOT3KXKc6JGzLKrTcQQSe8FLq6k6G5QSEy9wK3hDGth9sHfMSHvxhPe3boyi8NQXc1b47VkBHvL6ec8wQD4KvxAsey80Fad-Kz53sv0flMM63C9e7J3faFobkwYLkc2NWjD8mgqZyPnpLM2HBvau4-zssBbTfLTeUJCzk6-8O7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇹🇷
انگولو‌ کانته دوست‌داشتنی دیشب اینقدر بکیرش بود که وسط زد و خورد بازیکنای فنرباغچه و‌ لیون حاضر نشد و راهشو کشید رفت سمت رختکن
😂
😂
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/104782" target="_blank">📅 14:50 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104781">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0ZAkpdfQ05GwVin_o3Y7zSUW7KLH9kEKnGIXq7Rv2XzNJ4A6jGJfZC91GPDUblaa8Gp9hK_cFGVAs8pMZ_iDhyamfdgpfXIOnOhVQJXpsnLt7x_4JdLPiEiw67dqmiuocQWSIKNJIho0X7seaU_YUwjghcBZ1G_Px0NNMTKtQtKCc_WStwaz-4JMHeQ8kE7QP574TNeLjwOM2fCeEB4gcxwQwAbSB9OL5Xc5ZU7dXD8xDeHiBZsl3KsV-LZCE_cviBr16q6RVFWEYbbMrqe9F2pfzrjfZekfr5MOsjzyEr0Ar6pkFo_jyxZYbzXjjRZP6-QJE-3CIZZMUmUcRXKYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇺
🔻
ورزشگاه اسپاتیفای‌نیوکمپ‌گزینه اصلی یوفا‌ برای میزبانی فینال لیگ‌قهرمانان ۲۰۲۹ هست و حدود دو هفته دیگه به‌صورت رسمی اعلام میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/104781" target="_blank">📅 14:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104780">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b12f4aaba6.mp4?token=HvxAJBcR_chmSP9xcWHWuLuLLnC2hMFhtAQhovGGcWbdWnao6p5mbsaNIUMwFDe6P6ZiBjTAtEgUGDbbfEgfJGiiwIOcKsL_DGAWI_a_i9X0yo1O8LEmeFD27UcOLtFVtW8cIcps2xgup7xD8AX62W_-qu0SHY6pM86XbouTRF0OoYdQgofnfcCLk2XomC4uiKV9O6HBYi1FlFGWffS2Rrpl-jGqUD5gaCKWY44FrAVJlhFuXRDIBf7uGDaZboVqBCOWKftz6DWMsWyWpTuawgjGLqSW_oeVLMLF6XLIEvOA3JmBchuFGl35BOzdAvHky2aurdgKHg0oM8rJPQRTkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b12f4aaba6.mp4?token=HvxAJBcR_chmSP9xcWHWuLuLLnC2hMFhtAQhovGGcWbdWnao6p5mbsaNIUMwFDe6P6ZiBjTAtEgUGDbbfEgfJGiiwIOcKsL_DGAWI_a_i9X0yo1O8LEmeFD27UcOLtFVtW8cIcps2xgup7xD8AX62W_-qu0SHY6pM86XbouTRF0OoYdQgofnfcCLk2XomC4uiKV9O6HBYi1FlFGWffS2Rrpl-jGqUD5gaCKWY44FrAVJlhFuXRDIBf7uGDaZboVqBCOWKftz6DWMsWyWpTuawgjGLqSW_oeVLMLF6XLIEvOA3JmBchuFGl35BOzdAvHky2aurdgKHg0oM8rJPQRTkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🤡
تحلیل‌ عالی و‌ شنیدنی یکی از حامیان حکومت: ارزش دلار هر روز داره بالاتر میره و پول ما بی ارزش میشه، اما این به نفع ماست! اون فرد خارجی بیشتر محصولات مارو میخره، در نتیجه تولید بیشتر، بیکاری کمتر و تورم مهار میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/104780" target="_blank">📅 14:02 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104779">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a6a68d1e3.mp4?token=nVRc8-miM-MuJ0w_14cOwtBnt-Xy0UIEhWZg3loLJBC5vd9IvyOSn5ysYTWF3qfSGNp5d-dgwoVqfDC2nJ7iSFwb31cJ3fSmcso6vFw2addZBZvaeG06MUfoQpgibH4OibZYaFP1WNvNotmwNZUTJ4fiXy6FwSRfbj6xt3jSkTO_TR5Ci5ATNKBZQ5mR4Y9NIlqBSGwtwo9gXmjRGQVnzLqA8fRGCFZwcCDTvkB0hIeW0eQyTwUNJ5c7EV6-F1jNsuTEFUQlCTbBbfqB0-b0RVrzaxli8DEmQUwLXuziNfF1BqAFspsaZD5uo3kuAJmiv0DzveoKmIe7BCCK2gH5WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a6a68d1e3.mp4?token=nVRc8-miM-MuJ0w_14cOwtBnt-Xy0UIEhWZg3loLJBC5vd9IvyOSn5ysYTWF3qfSGNp5d-dgwoVqfDC2nJ7iSFwb31cJ3fSmcso6vFw2addZBZvaeG06MUfoQpgibH4OibZYaFP1WNvNotmwNZUTJ4fiXy6FwSRfbj6xt3jSkTO_TR5Ci5ATNKBZQ5mR4Y9NIlqBSGwtwo9gXmjRGQVnzLqA8fRGCFZwcCDTvkB0hIeW0eQyTwUNJ5c7EV6-F1jNsuTEFUQlCTbBbfqB0-b0RVrzaxli8DEmQUwLXuziNfF1BqAFspsaZD5uo3kuAJmiv0DzveoKmIe7BCCK2gH5WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
👍
بازیکنان لیل‌فرانسه این‌شکلی و‌ خوشکل با ایوب‌ بوعدی بازیکن جدید منچسترسیتی خداحافظی کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/104779" target="_blank">📅 13:35 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104778">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJIw9Z1lBcsAnNEXaN6ZG_RndtS7tOUHMTQT9bmKSYubvuf_8IFlNLU5FZ8vwosEIm5Y-O4wfceAeJwm_NA-X4C_bEnxKWqWoFvFw8Mts7Xwg5MpahXgvm0BMFrvneKwvfvbgXg9ybfFYsQsYqgV4E7VOyYLWmmoR0CtC-JJI2uHA2yfgPKDtxZB-7eeQEpRf2JCAcpmBVLcLnTscE1OCg0AQVpoUpRRkov6ZFl3OzS9crP4ea-nvHXb0lyAIqdUO6wGRGGwUZtybaTuptXWSzGMtPyDvZMNjgVqp3_q2GGrdOF3KbNDwE0Eq9zWpLnhAb3eouzdwovSdx44AnZbjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
ورزشگاه بصره عراق به عنوان میزبان بازی‌های استقلال در آسیا انتخاب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/104778" target="_blank">📅 13:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104777">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ooA9n-FhxRD3DEw2pXCoxAaE1QuD7JV_Ln9DnrxpVLbhM1cV3Xoh8i7bvd7fw3G4ZAI2i8GnCdtWDa-Dm8N5VqteESe8mz0Lt_bhW2px-utujQJ64d2hEyPLGzNYEh5BKUpQ_ritorzgzziCFSo1G4vTA05rIRoFVz428nRVzdYs6MuEZ_BOJeoh1nF8H64ZtZK-eKLKxMibj4Aq9bljtX6p_jvs2G1OOvTzN46giAYdUBFfX1wiplUF7pK9AfKtA04Xis1p6pRwDks6OB6c2R4ouUsLj8IUiGVGv_9pHfTRYLXwPF7F8EBOythrTKSV2FdBGhlZJIJLFcex-9UGuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
#فوووووری
و
#رسمیییییی
؛
✅
لیواکوویچ سنگربان تیم‌ملی کرواسی با عقد قراردادی تا سال ۲۰۳۰ به بارسلونا پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/104777" target="_blank">📅 13:21 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104776">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mdYUIEa3OQdl_iHxRXA_4xudQMmd90dVOzlZOn9VK5K4WHRarw10sM5yoyIeyDiOAEpnvtLNkoX3dK9znDRV_oAA_YPgy-1u12vqBwROihS55fRlO7nxEIXhLTvT3Nsk7KOhDh2iBd42o9JlM1Qm1ozUYeSmThO-RIXgtzvX_Jko1a61qgoEhb8Zl76iTqn1IajCvxU8fAPJbdedCNyU7IUNtpVrT_ireEEEkn7dMNvFvXTbGjMcihFSoODU1-2368HD0lcSyMfeNVWR9kdrc6nqNWRlFEumJIUar2BOoG7dy5W5L9YHGC1_NDYydAZHm6sD2cRBpRTrICdCMPtMmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
خط‌حمله ۵۰۰ میلیون یورویی لیورپول
🇸🇪
الکساندر ایساک — 145 میلیون یورو
🇩🇪
فلوریان ویرتز— 136 میلیون یورو
🇫🇷
هوگو اکتیکه — 95 میلیون یورو
🇫🇷
بردلی‌بارکولا —  135میلیون یورو
🆕
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/104776" target="_blank">📅 13:19 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104775">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBkB_SL1Jtq_ovcvIeBUlYJaDMFuuO0RpmTV8PsNs2rlsrvbolezSSgVAz5f3c73enmc4zLhIX4Q6HQQi5GSde9IT46Jvu5mupikFwGeFarJ8tBMdE9u_ALfwJ5SUrn3_BNAfHz57MPZC3AaqTgUaFrqw9rYQY2YjjKROC5jjHUqYIRbhJL0B0sJduC0C_aY8DzJbzltvFclfc_h8-i2pXNxF8D54E9sx-lc1hLSSfxtGljb8KuEsAbK3XLoSHv4jnokwrG8HfXprshJ213EjMkpckqzbzCCJ7RtYMFQjMoNoEO2ppSQb_QWjl7G50b4XysihHREXwOfvYJN5DcIcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🇪🇸
اوسکار‌ناسی مدافع ۲۱ ساله گرانادا با عقد قراردادی به رئال‌مادرید پیوست. این بازیکن جوان قراره در تیم رئال کاستیا فعالیت کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/104775" target="_blank">📅 13:01 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104774">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZolLKnlQ8CpTGybb0qWC3T0BzIEVee-qDNKkWtr1lxRHYmhFxR3RDeUvUJbTsCx6icfTE1J24KJuoCYQfkFahzbXb9ukqAyRM0gSKjS_TkqmNJd7zmnDuuBd81pPYVryKVADkSnNhMRIZqZqt4H_ZpR8QzRcgjOQOyqImrfdT_WwgjNYKR4IgcXdtpNXxhLuguTMQiBoEYbtIfY2_abEciYP8EYoYZOPh3VQF_hASm_nf7N0j1QJj1rSpPfMx4En3HtoKUP9W5yIQM_m6XeMhTQb_9Nw2BTdz9sQWTxq8pXm3RZdP790iTtqa4e8l-mIlgVrDwsD8Bl2M6U93aMtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🏴󠁧󠁢󠁥󠁮󠁧󠁿
کیت‌سوم سکسی فصل‌جاری منچسترسیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/104774" target="_blank">📅 12:58 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104773">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ecd32f7a0.mp4?token=GHItSyOsZWxCrAc2tyU6Q93DVLtkucg2_yRSRE1tdSdU09kvUsPO_HoTPuUpIn1CAqtwQTEscq5Tu_AC6buGjDak9eI-RXRdpXYSVBK0yeoyjUljgAsNYFCLh_-IKf1COg9cIpmS2IK4OyOtRDrcxHot2s0aqoyufJVnmFOQhUVwWbnAMbWCAJuhLAC8UZKZMLKfFpWHh33x_7fVhnSZ5uyGLuN47_9JhNYeU7htIoZkPwOAXJD4Wctn_x8Apv-1rYpoVVuDxeh72USJmbA9TWNJRlUG3eGpAjL7jUCp6VFcAg0k4Aq5GRqChq8Su0_GcQNFYpmo430kLKvcUeAu_kUywMc0dq6Ybyxh3Q6HBvIIzpVGdGPhCcu356qe_m2Y-OL6gpdzWE-U5WWGGHDxpYX1rEIOg0pBu5v-fK6cJzfVtJlTiF2mr66o2s94m0rIHwHqTM-Lymepz-diHyBfFEjDcaxGzJDZGSmaZ95OX58oAVPFWGcj6TxRP3z5wByI2CHPM7i5bzRS9RhNY8OpnbFySy5MNLTJeEx59Udui2NDmeNHEnb3MryCSr-3LvCmn6wr2BZPdBiKqDb3QFY84HzchFvxGrJCNa0WJOCCh_EhLFftGhgDXlG5PrxTr8qYytnOKMXLtfh8yvxVBuADjmLiBg7XltZU1-EOcY2Oj_c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ecd32f7a0.mp4?token=GHItSyOsZWxCrAc2tyU6Q93DVLtkucg2_yRSRE1tdSdU09kvUsPO_HoTPuUpIn1CAqtwQTEscq5Tu_AC6buGjDak9eI-RXRdpXYSVBK0yeoyjUljgAsNYFCLh_-IKf1COg9cIpmS2IK4OyOtRDrcxHot2s0aqoyufJVnmFOQhUVwWbnAMbWCAJuhLAC8UZKZMLKfFpWHh33x_7fVhnSZ5uyGLuN47_9JhNYeU7htIoZkPwOAXJD4Wctn_x8Apv-1rYpoVVuDxeh72USJmbA9TWNJRlUG3eGpAjL7jUCp6VFcAg0k4Aq5GRqChq8Su0_GcQNFYpmo430kLKvcUeAu_kUywMc0dq6Ybyxh3Q6HBvIIzpVGdGPhCcu356qe_m2Y-OL6gpdzWE-U5WWGGHDxpYX1rEIOg0pBu5v-fK6cJzfVtJlTiF2mr66o2s94m0rIHwHqTM-Lymepz-diHyBfFEjDcaxGzJDZGSmaZ95OX58oAVPFWGcj6TxRP3z5wByI2CHPM7i5bzRS9RhNY8OpnbFySy5MNLTJeEx59Udui2NDmeNHEnb3MryCSr-3LvCmn6wr2BZPdBiKqDb3QFY84HzchFvxGrJCNa0WJOCCh_EhLFftGhgDXlG5PrxTr8qYytnOKMXLtfh8yvxVBuADjmLiBg7XltZU1-EOcY2Oj_c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
ریشه اختلافات وحید رضایی و پیروز قربانی که باعث درگیری خشن در بازی اخیر آلومینیوم مقابل شمس‌آذر قزوین شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/104773" target="_blank">📅 12:45 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104772">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8ec217fba.mp4?token=oAtArYcRSoEysm1sYVyKmeqgjeuF0PoaWwepvm2hQnjyh6EsfQYSUnhsGcTBBr88kQqAfmssDgqlkX74bbu_g-5lmd7RtC0_F9fiCc-2k2ttU_vwbFc7MWrpuQgwhu8vOc6Yt5Ouc1HQN6K9EyLDQImHbdVrlnZAJWyEiDaFXiMwn6bOzaa2xIZ1A9LjLyDp0cG1FXBJrhNTb88T5nXb2NKW2hXUpbwxVHrhsUBOPyJ-BZdK3ppCwGPFSbcKT09PEjn7a3ca3ANzjwuSthg4EZbql_XiRF-GEomFmTqnpmoo5CsQOX1Rs-9ljCd0VLc7ZrqQ4hXa4EzIT3CZghIvzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8ec217fba.mp4?token=oAtArYcRSoEysm1sYVyKmeqgjeuF0PoaWwepvm2hQnjyh6EsfQYSUnhsGcTBBr88kQqAfmssDgqlkX74bbu_g-5lmd7RtC0_F9fiCc-2k2ttU_vwbFc7MWrpuQgwhu8vOc6Yt5Ouc1HQN6K9EyLDQImHbdVrlnZAJWyEiDaFXiMwn6bOzaa2xIZ1A9LjLyDp0cG1FXBJrhNTb88T5nXb2NKW2hXUpbwxVHrhsUBOPyJ-BZdK3ppCwGPFSbcKT09PEjn7a3ca3ANzjwuSthg4EZbql_XiRF-GEomFmTqnpmoo5CsQOX1Rs-9ljCd0VLc7ZrqQ4hXa4EzIT3CZghIvzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❓
خبرنگار: امباپه میتونه به رکورد ۶۰ گل رونالدو در رئال مادرید تحت هدایت تو برسه؟⁣
🎙
ژوزه مورینیو: من ۴۰ گل با جام قهرمانی رو به ۶۰ تا گل بدون جام ترجیح میدم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/104772" target="_blank">📅 12:20 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104771">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WOM9iLUYuovlEX5IYHeSbJdfF7fb6_K-6E9XBkRppDVJBEDCguf1E3eORCbw6bgpCyxMe3Aw6OhW5UC9i4e-UdaofPwzYOcflEvbJWFCupyzDxBOeVT9qDoxbt_mM5J55qeVEZhJKMqSBz0MgF0phyZ3EjK8mFBxQ1OqM8Oyj6lmnwIihEiTZAl9YJbBrhLYAjxG3eN9B1nsJohnzXhvODFP6YgyTenE7Sq2V7jvWPpcKhCQc0MMZ9hehIz7n_a1fJ5CddJ7-oVbTAkJ9zjxLYuvS_l6dNriZwhTulooK4mkiox7LBC-R5O5qZiKg7YHLXX8wBAIJAm2d1Gs0fsIzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
✅
متئو‌ مورتو و دیوید اورنشتین: انتقال بارکولا به لیورپول با رقم ۱۰۰ میلیون پوند خالص به علاوه ۲۰ میلیون پوند پاداش نهایی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/104771" target="_blank">📅 12:02 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104770">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jVhm3TbtdNxeZuUVOt7244jkjP197lDQ2kg-cye1Z0jt049gZ9DIbOV0Jq65UkBoaw_mPvh5Cx0Vcaw7nOWyZGiKZUws4and37YOJzQR86Zl08J6UmgkO-Oj7wWfR3aXbGc9XXTNo82HhM4whbBIVjl5Jws0q6RyiBKpx4agO3bSvH8sEgGswjvPlN8oELX8eaSYavsi2tYTR2J0fGD0jrYwa9zyN2cHhZArD07C1FS8ka9sbQfM7DXfAWBeD8cNUHDwP1UE2843nU5P5J4HB9XGfek7l78iStkDploRAF4ItxIVYzi-255y5y08FYj0Klibb6iRKfPpSSuIdOfRuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
📱
توییت جدید علی کریمی: دیگه از هیچ شخصی یا حزب سیاسی حمایت نمی‌کنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/104770" target="_blank">📅 11:58 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104769">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F_FtD0aY7C4jY_b2nQ03eFLUbiPFTdeAFnaSMZFBChor8pf726qYRRqNiCtDAqREw21W1nE2Dw8kwFriYlKAN9qpBmmri4H2h20qJH6hP1bPKfztFb7uV-Ka0WuzXCjN_Q7LSeQhX3PQ9j5bMNk9dBng3TeNmPdHuk982IcoepCAQS-5jNLWCQ_Q5C-GbOu2ExU0Mk0PzAbetebZcqzLAT4ZILjwRjtQbgpXxXnnGrmQ1fpV5biLhNNbIT665WtSkr8RFFbXu3ppjNPdWclQed90zR2YROFfuMFHgbo1twpdIfVIipgoszmL5HrlIWglUfshaSvK7KDVvHXKWQIrpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
#فوووووری از رومانو: مذاکرات لیورپول با پاریس برای جذب بارکولا در مراحل نهایی قرار داره و بزودی شاهد توافق نهایی خواهیم بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/104769" target="_blank">📅 11:57 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104768">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4d0d739a4.mp4?token=lZIHO2HOJKC6biiPqEz7tpwUUshPD_C_Fkl1i4t_yMNTcE1LM8clLBwdOJtPzqtaHHOq_hTEKKQyuqVecfx9qhIDB1dvFUcKLLggdSTc8i9ODBfgTVgiqWMv6Co-TH84-ddscLiKHPPqMUhF6_5kVxeqfpkF3XZLnIxvr8AoLmq4xJLwDvm3GnWTquIXlOzF2QGCS2W94D8slQ9hBGzpsJqcT8YAR8bT8CU4BURQhWfe2dld3snxAzwniOsYWWH098z1V47w3-5phKRcPP6Lj39OD2LbHtvds7hVcoXGNlu9PkZ_XgXOq7ouyw65AX8HZ0FkrzVyPmxhPX6D-B0UOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4d0d739a4.mp4?token=lZIHO2HOJKC6biiPqEz7tpwUUshPD_C_Fkl1i4t_yMNTcE1LM8clLBwdOJtPzqtaHHOq_hTEKKQyuqVecfx9qhIDB1dvFUcKLLggdSTc8i9ODBfgTVgiqWMv6Co-TH84-ddscLiKHPPqMUhF6_5kVxeqfpkF3XZLnIxvr8AoLmq4xJLwDvm3GnWTquIXlOzF2QGCS2W94D8slQ9hBGzpsJqcT8YAR8bT8CU4BURQhWfe2dld3snxAzwniOsYWWH098z1V47w3-5phKRcPP6Lj39OD2LbHtvds7hVcoXGNlu9PkZ_XgXOq7ouyw65AX8HZ0FkrzVyPmxhPX6D-B0UOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
احمد الشرع، رئیس جمهور سوریه، نخستین تراکنش پرداخت با VisaCard را پس از حذف رسمی نام سوریه از فهرست کشورهای حامی تروریسم انجام داد.
❌
ایالات متحده آمریکا، سوریه را از فهرست کشورهای حامی تروریسم خارج کرد؛ ایران، کوبا و کره شمالی همچنان در این فهرست قرار دارند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/104768" target="_blank">📅 11:52 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104767">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0PyJCXX64ALOW-RVAM3YMRXdqHq_5uTE8rb84NjSeREp2Qsnebj72dSL0PT8MNXZ_lEJ22JB5yzuqaM3zOu5STjlXpAPl841e5V-ISjBrxuCfvEGMQPp0DgH9sd9GcijFGNLcZNZo03_Tl7sw3vUH2v9baHiJ6b1rCzSkULltdo9Wnq3iZ7JrVZ2gVL4w8RbYcmgPK5PzAQhx2gpGmY76DOq7nAWL6JK2d5Bk1e1J5V3Irbp3EIaTVj8SYRB5wT4krIbQH5ZyQsuQv27xD6pWMEzrHjWyyRcuuQhm-2veRfBHr4XpnVNwv3ZokURDvfKGwVnyU0U1aubugVONgOdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇪🇸
خولیان آلوارز برای دومین روز متوالی در تمرینات اتلتیکو مادرید شرکت نکرده
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/104767" target="_blank">📅 11:47 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104766">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b6RxOfXoY_RPD8aNG7_WB9BUzpUS5OctDoMUzRLoPNvud52_3ONVigMxT9GccEAreoNilZkjMOlevBogPf1CnDNi5tfErxz8L_siXMUSSCfpBwsrEZou2piurhm5V7C3KYk55AXxQtwqZ0TLRov5KpycbJ8ObDNdn5iMVFOsSJY9YgQZDB5JNAClV2KH_Hm9qrQQxd7dy8mCwNTD0CTLqIKQFgN4Hl9kLAT99Q1oIFgt408UyVcLWQF1nFD3BV8Z-wk18PpqnhYLjdjiuQUaiMJq1FdeRpWP6lDdVxm2R3m7osavp1-skAope5NVFXd_qjls_OjXI8Pwlw2xBX4DBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
کیت‌سوم این‌فصل لیورپول رونمایی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/104766" target="_blank">📅 11:46 · 05 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
