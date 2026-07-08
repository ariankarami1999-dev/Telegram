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
<img src="https://cdn4.telesco.pe/file/QR1ePsiGx-a3pmKpiBAZi5GXhn55iS2k6AzlIscQ0VJDiQb2HnzNbIy58kmgMKbhI1yLumAOisYkIUNJGGylo6lB-4lOC1V-YJ_8k3rDr5crH4q1ZSfaYJEtEtzILLeNGBHD9794uPZBZKE3_1YBaiVeU6PecCpmEuS4gYEbv0_XWbewkNx4WpjL1S9QQn8SgjI2V2xsjfRMWqqH6HbDMKrJvt-Ld17QT5VkrI0K3V1ep7OkTLrFC4w_GWu_Z74-k62-BsJZI_f8qTXhNcYfvvCF71cWG4mMN1IHVciTjhWYmKIqb8wV_1nYgsAZS2Wqsiyi_rO6_CsD3xrTHsfsKg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 193K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 01:29:01</div>
<hr>

<div class="tg-post" id="msg-67611">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lyvQOaESy4VINNR_v5j-kfxg57gfVLkLLnaNXUlW0ecrwMka7WoohEwRbqcwLyhkORb3oK_FxD1BATxmSUguJa_RG1ydLz0K2RbK8oDLolrfjv9JCM_Amf_JMw-JSiuAzl-YEnLcKaPw4RV5HfQ2qFO6gsD1gwz5be0O8wfVCZaAEDEOqywudqHKJIdFBho5osP91064m2JVrHeiAbiUX49Cat7ehul5ScTwnGupix7u0wLrDJ0VN2SLSpcvVGkc7YTWGWUr3L8h_mlhI8LFDmQAFj5qgwUTf7ClS7Sv0J1h9_tF0MIf6YmdclH_PHx3sdC89B2pfCddkECKKtnjlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ :
این یک انتقام برای بمباران دیروز کشتی ها توسط ایران است. اگر این اتفاق دوباره تکرار شود، اوضاع بسیار بدتر خواهد شد!
@News_Hut</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/news_hut/67611" target="_blank">📅 01:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67608">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NqoNhfh3XY2zxq1k2mjhlF0cvJbcCZa0trxhhRFJJCa8gY6TASv7NbdaH-fviopT-pFajoCNIVBZ6xlrOGKz6ivdmhUEokLzr5CVzaH_oQuu5T00ZLt593YWBc7pzhDIeSixz02wk0UbRGJaGcR-LfIEQwv8R3rkEbq5bllIInSXU8EWg8hC76DxOSzED4KrC6FeHG64sbCdgLMnLNKmgtYsOZUOTgroSqWH0V2BfhwTW582lYUb2a4l_l9J3dRk5mq5gyVOznzP6EMtq1ELMUdQEs73MEdvGCJHsABA6Zxzv80I3MZN4syLw9ryMTP3epHW1-YVKqTpuJjjmgUcyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NsKQIUIAqcD2DEZgAz9mURBqTol5Xz0h-fAY3UPXaxewfaYo5xT-wT5_LF4f-OKyWKWhskr2Yboq7qxObgoFC8uWus9wsWdK1g-eBuspIZNah_cK9JIjxiUHwbHq1yuAMmB40Gcw6khgrZ49VboXWN8u0Lga-RjJH5MUf906fB2RdgGT65vUGF8FBtLsgB4VO-EkOzfqfBA9rxjZJA2LloFc6MP79loN0arqMvLKhpjvfUQ1fH62Sj-8DTRI-mlQA_v8nXJp_YlAiGphmwOafyL6LsAQIU_MEgcxQJ0CnwonghLx1hcWO8A_vb5WmUV9HLYyj9HdKrGFYOZiZjXS6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a-xUowJeUfUhWUH05-Q99PPgmMMjlPv7dLm0YwYN4DdBPPct6h5Qb8Iqg5tiXpaP4MtNOTR_0kBKp6QEVlLhH8ftMr4XFrn_fjF2Ow5MNz9SdKv2IEhTmBmmdYnwGVXSTCy3xZl7ZC-8d3aEUbXnoOKEmpRHPQe5mwulYMJjuQ40kI74uU1nXUmddfT2WioW_PKIGHG40mWfM4qqx745K2dbvC-1NB9xY4ein38z8s9Thr5k1IViZQglR5aVrXZqmwQj6Fm1bOdjt_giJyf6WHErJO0v0EeihZfVSxvK-TVOAwaDVT9B4WbJM7n-9qbmdWsXqdnyo3NFuCgXtCjiZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ تصاویر حمله به جنوب ایران رو در تروث سوشال منتشر کرد
@News_Hut</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/news_hut/67608" target="_blank">📅 01:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67607">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">دلیلِ این چص‌حمله هارو متوجه نمی‌شم واقعا، آخه کسی که زدین رهبرشونو که از نظر اونا جانشین امام زمان بود رو کشتین، اتفاقی افتاد مگه که الان بخواین با زدن توالتای پادگانای سپاه اتفاقی بیفته؟
صرفا این حملات شرایط اقتصادی رو سخت‌تر می‌کنه همونطور که امروز دلار ۱۸۰ تومنی رو دیدیم، خود ترامپ هم می‌دونه تنها راه حمله زمینیه و اولین نقطه هم خارک ولی جرئتش...؟!
#hjAly‌</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/news_hut/67607" target="_blank">📅 01:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67605">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9864e05e49.mp4?token=arkpnGHhpmPcHY0MRKRvjKSr7JGg7jk3dlzhOmkss7g1czXq2Q24B9HnQC8VTEgnfnWZrG3qsZetfpAT2McR0K4GlvnG29ueeE4Q42FCtonJxR5S0MDB3sSZsxkJ72H2AZREyhIwCytpcCPCv7I4rSUtjaysED_H8tPfwrb6j-SE6_yxFEae1h_Pq8CwF_Vdz2oaxDqCWfkcYiRJh7TLacF1IdscFdOfyOhdeErHX6ARBTJuROLKHyxJZj5F9RegBYNKts6bgfLlzgNGPM389xnj1UknbNjO7mv14pEQS250aEfYUGUN0JNk4cIQAmTWrHWfccnQaU9e6ltxIH1CRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9864e05e49.mp4?token=arkpnGHhpmPcHY0MRKRvjKSr7JGg7jk3dlzhOmkss7g1czXq2Q24B9HnQC8VTEgnfnWZrG3qsZetfpAT2McR0K4GlvnG29ueeE4Q42FCtonJxR5S0MDB3sSZsxkJ72H2AZREyhIwCytpcCPCv7I4rSUtjaysED_H8tPfwrb6j-SE6_yxFEae1h_Pq8CwF_Vdz2oaxDqCWfkcYiRJh7TLacF1IdscFdOfyOhdeErHX6ARBTJuROLKHyxJZj5F9RegBYNKts6bgfLlzgNGPM389xnj1UknbNjO7mv14pEQS250aEfYUGUN0JNk4cIQAmTWrHWfccnQaU9e6ltxIH1CRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
ویدئوهایی از لحظه حمله آمریکا به برج کنترل دریایی اسکله شهید کلانتری چابهار :
@News_Hut</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/news_hut/67605" target="_blank">📅 01:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67604">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
انفجار های مجدد در جزیره بوموسی
@News_Hut</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/news_hut/67604" target="_blank">📅 01:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67603">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ماشالا ترامپِ شیردلِ مادرجنده‌ی املاکی
😊
#hjAly‌</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/news_hut/67603" target="_blank">📅 00:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67602">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندر کنگان
@News_Hut</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/news_hut/67602" target="_blank">📅 00:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67601">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EGsCi7EaTgb5c_O6iy90qEyzvpg1zRmiyqLQPcAFm6MufUCJx7oEnZpA8BZOVhajiFD639doyUykKY6BWXd8Raht3s_DZkShlO76v-zIjQuW_Lf6XuLy7NalMjyhqgJ3qu7lz5wrQmWWr6wFL2bdmq_8vpLQ2eDp6ClSev3nlDZ_F0AQ-eEjDDtsPBBKwYkAJ2AKPsFmwBuTUpNfZQYd6C5slDbYEL3g7EPGIjFTJ4n8W4ojYbxfKGXYjqJsDsZSxpaY2SfcJS6fBQYP9dWNA2DsnvQ9xaKuj97SuqyFtW0p3qmp0V26l49Rvwm7A2EdWMB34sQdDEJQcF-suY8cYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
یازده فروند سوخت رسان نیروی دریایی آمریکا بر فراز خاورمیانه
@News_Hut</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/news_hut/67601" target="_blank">📅 00:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67600">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gFp9mRFQE4lOq7DzYIJiiKWIPlS3To8afzvdTXBlzKdpvWLYyOTDWAbuSZMO2mO5pp5BghDeRGaAvICqT_930yonnbuNuBOneQv5ST4pCsLaQqCnHG6y0x45EuZUJzDKNz1t90XU7nfuuUXlkfVWyPB8PYXIrwxEPK3304JluL5pg-L2sHcOkjSZ01F8AMf9FySgHNkR-mdQDClgrtJSPotyMY3_Murub9KgYHbzapB6NhhSbNwdnZuv1fCkerkCxqyzqL9hbzIEBqtki-tDtegvTFxianwyZzK0Mh25txokjHC1qxyju4XnflB5xVp-ek5tTeDL-VeIMmSwxvni7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
وضعیت شهباز شریف بعد از حملات آمریکا:
@News_Hut</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/67600" target="_blank">📅 00:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67599">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
صداوسیما :
نیروی هوایی آمریکا در حملات به چابهار، اسکله‌های «شهید بهشتی» و «کلانتری» رو به همراه برج کنترل ترافیک دریایی این بندر هدف قرار داده.
@News_Hut</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/news_hut/67599" target="_blank">📅 00:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67597">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rP6t7Nzi4m9kh50THwLnM7D1EWiaflnRccuJnwCryb5QEllEd060cWfT_VsqW_I5bWSJqGl4HL4MyYrB9fzAiS_PBfmM3JQ_hlXeySS9iz8_r2-BfoQnEVlwr3sITU8XrFG7ZzWYKkIVZMENpeSJoQ18Y4ajjzAOTfjGxn_HwQun4Ns3Gnx6HTnN7uo76peV6lEepdgIXaNNQGa7qOIuTSUetKVTRP-YImOg366RZu8Mmuy_SWLqfh9v9YZUd0bpwGEmcB2t0eCzdRGWmYrLMo4DePoS9O4gbwyvfW1ldcMxdnLQEbzeQbaNzxPftKP3zjgu9vVnTRfLpO6FQrjaNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H2RYjTSBJFaF_uUfGKML9a4wcqfXUGLSNPOq4cZfLSXIaoolAxKcvytjU0UHM-f6Ey9_sIZGwYS3zWVDebIeZ1HR5mSDkr8VMA7EMjUY1VtSqA2M7hlhHtDHclo5DBVYW3OpOovEYlaRBPXv0dUQg8FqsZK25FWdwwvQvfT38TtPy7jYUfp11w2Fd-Lec1vomXyZRLR-e80FX9Hgel2enLLz4F1HLXEG_i8Ug42dBIWyhfp9IX1BomMKnSkngnUYOmIXqwCoqwInGeS459YIRzEZDwg1WKN8GBIUvOFGKWRa_fvsbF-buXFfZrXDUOTB3e67o7o0_UWnbG8EeR-eKA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
برج دریایی اسکله شهید بهشتی چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/news_hut/67597" target="_blank">📅 00:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67596">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🇮🇷
محسن رضایی مشاور رهبر:
دشمن متجاوز و همدستانش به شدت تنبیه خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/67596" target="_blank">📅 00:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67595">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
دقایقی پیش مردم در چغادک استان بوشهر ۳ انفجار نسبتا شدید را حس کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/67595" target="_blank">📅 00:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67594">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
چندین انفجاردر بندرلنگه
@News_Hut</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/67594" target="_blank">📅 00:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67593">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
فعلا تمرکز حملات مربوط به خط ساحلی جنوب کشور بوده
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/67593" target="_blank">📅 00:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67592">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df60497304.mp4?token=XciHaoh89T20vPfKsZdi8d1RP2jGNDCxdK1EmvlzW9BV5pXJZmH0EmwEat2f5OS0n553HrTQwCEILikvJRoe72rNY3yMIaEouht_WdujTDvld-dPa1lwXHANkjVO3WhRLcSQDoY-Czg7wVWcp2HeYDmxAo4M9IOy0jz4u0_2uCUOfwBb4o4nudcpYcDSEB8erTId7F9JUyo1BJeDay5RqzFQZUYrz35k8KaxkfAGDSCMRImvX2Xzma5SUR78HkHh_NENNqg0I81b0AxnACPakE1XLZ08ZNveKR3wKfZkhk4eR5KKUY92E-sFUmswKXDZHql7he0sLyy3aAP8CqsGdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df60497304.mp4?token=XciHaoh89T20vPfKsZdi8d1RP2jGNDCxdK1EmvlzW9BV5pXJZmH0EmwEat2f5OS0n553HrTQwCEILikvJRoe72rNY3yMIaEouht_WdujTDvld-dPa1lwXHANkjVO3WhRLcSQDoY-Czg7wVWcp2HeYDmxAo4M9IOy0jz4u0_2uCUOfwBb4o4nudcpYcDSEB8erTId7F9JUyo1BJeDay5RqzFQZUYrz35k8KaxkfAGDSCMRImvX2Xzma5SUR78HkHh_NENNqg0I81b0AxnACPakE1XLZ08ZNveKR3wKfZkhk4eR5KKUY92E-sFUmswKXDZHql7he0sLyy3aAP8CqsGdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/67592" target="_blank">📅 00:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67591">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
چندین انفجار شدید در جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/67591" target="_blank">📅 00:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67588">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M1WCH7qbFLjayqRhyRkFyxvXIJc9qmPOADPW-ocRevqQfHUSLLvvBsgs5F-WgWafqb2bKM9jv0tJeidWbnV40892pshp8RLMPDxwkCv2E5pOjmTNmwogfQhvUU9bKTKMJXHU1TexNkZZDHhTQ6Ep4OKcZLnBenKR3iuiVGl3Wko5JMz4-72JhiD5I_I1HXjHEt7nLmsKOYhbMqlQi2qwNuh00rBXsXEGJGWe7bVVX0e-M61EGgtj8q8YCPtc8wPUJ9r60yCSBsjsX0A1Nc5p91tEcuEwu3pOIhIhSr-px5gdjbaYAYqFlmePctQn2N3YC2Pm2ri6vmQQMU09fNcb-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6afb0f1898.mp4?token=vuBbmdfAYFmu-hMPRaR5-X6OoSn5UvtKqimJx4Cc1qrmAUAF5xAd0YU3PA8rzCLkMAL9dYyU3TdjvII6038mDJLPssBBP8B-QOwBzZ76qnKJhp8TkEDb3GGJSNgwxoh1WJnfeOz7d66gBu-agvyR3iKfAssj4hHzw35Ei-5ko9jcqMV-tBRY_zPyWrpNAXhW32sO4-ZW0mXejwfEDukM78DQeAhMCWQW7s-VnDPtUNdMCWrmw5GceJ_fmwCFIcYFeIlTUtm2cCxXGpCvLwvel7L1jkbdX-uvQy2msI9bzXKMysl9phBrPqDtuZH2Q-FjxET-Ery7DfE1USdjHJ0HXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6afb0f1898.mp4?token=vuBbmdfAYFmu-hMPRaR5-X6OoSn5UvtKqimJx4Cc1qrmAUAF5xAd0YU3PA8rzCLkMAL9dYyU3TdjvII6038mDJLPssBBP8B-QOwBzZ76qnKJhp8TkEDb3GGJSNgwxoh1WJnfeOz7d66gBu-agvyR3iKfAssj4hHzw35Ei-5ko9jcqMV-tBRY_zPyWrpNAXhW32sO4-ZW0mXejwfEDukM78DQeAhMCWQW7s-VnDPtUNdMCWrmw5GceJ_fmwCFIcYFeIlTUtm2cCxXGpCvLwvel7L1jkbdX-uvQy2msI9bzXKMysl9phBrPqDtuZH2Q-FjxET-Ery7DfE1USdjHJ0HXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ویدیو منتسب به بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/67588" target="_blank">📅 00:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67587">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac1596adc1.mp4?token=lMEuFHnfwKmkoP84k0ZaRzgqUsYnEKx18dCqgmlYRNv6KZsBbkbUB29af5nT5XbNalZjMMC7bQ3NnpBjYygvKuV1PXfp_zvnBrllsLYCSVtbsrLdaPsVWRs_5-AqtFR8RG-Rx_5F9ZyPGbAC_twmlIOCAMKzieFcmoAuKqHhaGMhC1UQe3FeO2BuBm0RasnSMDfO9grWKJsjwPkNTSF4iwXGLrxoEiPEXWN9ZL1UsRlH0qstolgm910t4y4miyVLLGyCHQ4Pw9Ou1jbbxhbBSvzBCmKcgY7ReEPOKxI2CvFHK0CcXqLwOudbS83euZh_SE2304K_z9ZsZzwJC8DraQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac1596adc1.mp4?token=lMEuFHnfwKmkoP84k0ZaRzgqUsYnEKx18dCqgmlYRNv6KZsBbkbUB29af5nT5XbNalZjMMC7bQ3NnpBjYygvKuV1PXfp_zvnBrllsLYCSVtbsrLdaPsVWRs_5-AqtFR8RG-Rx_5F9ZyPGbAC_twmlIOCAMKzieFcmoAuKqHhaGMhC1UQe3FeO2BuBm0RasnSMDfO9grWKJsjwPkNTSF4iwXGLrxoEiPEXWN9ZL1UsRlH0qstolgm910t4y4miyVLLGyCHQ4Pw9Ou1jbbxhbBSvzBCmKcgY7ReEPOKxI2CvFHK0CcXqLwOudbS83euZh_SE2304K_z9ZsZzwJC8DraQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
❌
لحظه انفجار در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/67587" target="_blank">📅 00:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67586">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
دو انفجار در جزیره ابوموسی
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/67586" target="_blank">📅 00:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67585">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9f9c6b6a4.mp4?token=ZBn8hb6KkmQahoWxVvaiMz40fqnM1-E_On0C7vU8IUYGhgqv9xSGkr8utLsOcwooJpRfcIsQv3hBT7QWOYEJTg-kpPnmzgS85vvsf1F-yGkolDIDI6-YtEYjuACvAJo1iCQSAYvaZaWEkCrnn4gbZvqa0z1ieIO2MJZaD4YHBipPvkRHBtGLt7TAStA35ZNMFJPapBw-dBNkO7g2GnFzvOgSm_QHfCQegzg5oMu5ISsFX89gKdNe-Xix9q4ccroAavgd1AAHR-XkdF9wgGt2QUwglZ8L1WVOicwpb5J26fQbquSA3sfzw3NQOb19DtC81LcjlEJAOknWjWHQ6ZO5VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9f9c6b6a4.mp4?token=ZBn8hb6KkmQahoWxVvaiMz40fqnM1-E_On0C7vU8IUYGhgqv9xSGkr8utLsOcwooJpRfcIsQv3hBT7QWOYEJTg-kpPnmzgS85vvsf1F-yGkolDIDI6-YtEYjuACvAJo1iCQSAYvaZaWEkCrnn4gbZvqa0z1ieIO2MJZaD4YHBipPvkRHBtGLt7TAStA35ZNMFJPapBw-dBNkO7g2GnFzvOgSm_QHfCQegzg5oMu5ISsFX89gKdNe-Xix9q4ccroAavgd1AAHR-XkdF9wgGt2QUwglZ8L1WVOicwpb5J26fQbquSA3sfzw3NQOb19DtC81LcjlEJAOknWjWHQ6ZO5VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
هم اکنون؛ آنتن زنده شبکه خبر
رئیس کمیسیون امنیت ملی مجلس: آمریکایی‌ها بدانند پاسخ کوبنده‌ای به آنها خواهیم داد و امنیت را در  هر جای دنیا باشند از آنها سلب خواهیم کرد
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/67585" target="_blank">📅 00:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67584">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36b350a9ac.mp4?token=PSuKPVaUxpwzcqzqzWZFEKgX4uC_LDAeIqgAaubSgu5bNxCEmCTW18NpHiuXVt84kSndug1LsvcFAoV7M_aiJOK1BXqX5qBK9d4qJqiomkzuycAC2wZe0LvlKYuIKlXwxLzHiVtjRQs5fVzzDlfNP2ZhUYiQZEWpBTS6nBd75t5nIAV6gQ6B50sX8PKcpWczs1I3Fo9yAjscDITHsP8a5yOckQsWy6OE6H3-qoeCzNmzcG5mnUGG0hlcY_XCoCZEAUV1eyteXfgyQ9c-PJfUv_8hohSb4kPFK_IVeaoaDDIT70aeeuPn5btVpPhO__jXEp19UnmILYkkDTgT-GeNxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36b350a9ac.mp4?token=PSuKPVaUxpwzcqzqzWZFEKgX4uC_LDAeIqgAaubSgu5bNxCEmCTW18NpHiuXVt84kSndug1LsvcFAoV7M_aiJOK1BXqX5qBK9d4qJqiomkzuycAC2wZe0LvlKYuIKlXwxLzHiVtjRQs5fVzzDlfNP2ZhUYiQZEWpBTS6nBd75t5nIAV6gQ6B50sX8PKcpWczs1I3Fo9yAjscDITHsP8a5yOckQsWy6OE6H3-qoeCzNmzcG5mnUGG0hlcY_XCoCZEAUV1eyteXfgyQ9c-PJfUv_8hohSb4kPFK_IVeaoaDDIT70aeeuPn5btVpPhO__jXEp19UnmILYkkDTgT-GeNxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
لحظه انفجار در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/67584" target="_blank">📅 00:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67583">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b02d221609.mp4?token=aMQ649KW2HD1xa5NUopTOYI69qeW88HTXakMhzYNMSKLaFzlvNA0fB4XJuxxacqrPUQsZBiRXUHuTV_c3iDVCKYH_IManCIwbZWcJ14XPBKvPvxUigYLQ7rz3QQMF1IHbjNX8u0JiDOhws7b66T8zVehFKp97OEes7OZaJ6atPxUXPPEdIArW22cr94Nz1TI3-DZax9bMuAun4zMlbvKzT6gHkR5v9lkm3Rikeh4KOUPKJuafHONrxKP-5kb4cnXPflNluqydT1uqlYay0iZ0WbHSjnTmaGJLQ0P2iVKFXx8A36FFZJwjMH6Ia-skxJrDFOo0Plys-Kd54woj3IRKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b02d221609.mp4?token=aMQ649KW2HD1xa5NUopTOYI69qeW88HTXakMhzYNMSKLaFzlvNA0fB4XJuxxacqrPUQsZBiRXUHuTV_c3iDVCKYH_IManCIwbZWcJ14XPBKvPvxUigYLQ7rz3QQMF1IHbjNX8u0JiDOhws7b66T8zVehFKp97OEes7OZaJ6atPxUXPPEdIArW22cr94Nz1TI3-DZax9bMuAun4zMlbvKzT6gHkR5v9lkm3Rikeh4KOUPKJuafHONrxKP-5kb4cnXPflNluqydT1uqlYay0iZ0WbHSjnTmaGJLQ0P2iVKFXx8A36FFZJwjMH6Ia-skxJrDFOo0Plys-Kd54woj3IRKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
منتسب به بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/67583" target="_blank">📅 00:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67582">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
نور نیوز  :
به زودی حملات ایران شروع میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/67582" target="_blank">📅 00:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67581">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c578ded4b.mp4?token=axECZAeBrnCDssdVQQXrKNh0wwIIKY80fnhBtgEovTM45RQ-grSHmLGi92E7hjuoOHoZWEqyLnh7gIoTZBm1uIlAl3Y8B6ZZe7Z9ASpHczMVZHhL72zYH2sgK2gENgjsB3X-rCYTYf-T5CBKXXwctJILP4iRF_uODBIlnVUKw1p7IL-jO5vbV00V9lkgfRTtc4ijzz6XkvEze984-2oU-W0as9TPRsw-EyMrD9lNHortyN014-n9tyNYSoMbrwgfkLbYap9ThMo-AFXCKihRhpP5vgLK8NSvwO6-FNCo_8m9MhJKX-Azj5gtesCqYsjaEtxteB-Jxsy0_FhdH06eFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c578ded4b.mp4?token=axECZAeBrnCDssdVQQXrKNh0wwIIKY80fnhBtgEovTM45RQ-grSHmLGi92E7hjuoOHoZWEqyLnh7gIoTZBm1uIlAl3Y8B6ZZe7Z9ASpHczMVZHhL72zYH2sgK2gENgjsB3X-rCYTYf-T5CBKXXwctJILP4iRF_uODBIlnVUKw1p7IL-jO5vbV00V9lkgfRTtc4ijzz6XkvEze984-2oU-W0as9TPRsw-EyMrD9lNHortyN014-n9tyNYSoMbrwgfkLbYap9ThMo-AFXCKihRhpP5vgLK8NSvwO6-FNCo_8m9MhJKX-Azj5gtesCqYsjaEtxteB-Jxsy0_FhdH06eFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ریشهر بوشهر دقایقی پیش
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67581" target="_blank">📅 00:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67580">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fce96b4303.mp4?token=rAx_w1xjHBP62denb173IntRbGLKW_uoiTMt5vc10_K1PikMbhvp5bN_bRtrTFPu0OalvDAmqwyL67ZAXQfPaPArS-ERN2zDS5lYpBDZEF9FvpBU2XU8adHmtRqPjmFUo1tFOlzZCzKv0GfB4X58QuNqMdSLDNp8x8a4btPWbom-8PPoIyzoI1xPm0gPAEAv3TDzDRNIw_c5EIuq2W-3bphTSA0AtlIyswCv8N_S9pnOxcd0zuBTdQ9KPWK9ABjd7xSnRcFZLdPf1DycGz06DWrJsTuwXHfDKc_HzZmszdAPlUn8xx6lFwUpUTXsDgfJQ5JxyGZJic-nyBh0tcuo5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fce96b4303.mp4?token=rAx_w1xjHBP62denb173IntRbGLKW_uoiTMt5vc10_K1PikMbhvp5bN_bRtrTFPu0OalvDAmqwyL67ZAXQfPaPArS-ERN2zDS5lYpBDZEF9FvpBU2XU8adHmtRqPjmFUo1tFOlzZCzKv0GfB4X58QuNqMdSLDNp8x8a4btPWbom-8PPoIyzoI1xPm0gPAEAv3TDzDRNIw_c5EIuq2W-3bphTSA0AtlIyswCv8N_S9pnOxcd0zuBTdQ9KPWK9ABjd7xSnRcFZLdPf1DycGz06DWrJsTuwXHfDKc_HzZmszdAPlUn8xx6lFwUpUTXsDgfJQ5JxyGZJic-nyBh0tcuo5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
لحظاتی از حملات آمریکایی به شهر چابهار، ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67580" target="_blank">📅 00:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67578">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F4rJ2RGctZ_1eGle03sihEkeUb7XUqkxXcogmU-GoeNBm2Gtl84jXjtnCASR2_XZT8aJGy8dTbkfJJOCpTY4kDcuTuNHpkFYzetnvjz60HHsbNIk6kXpe4coasiNVGJTHreZqFs1eEHhrCBDJgkqVF0zuTfqh3l3R2qO4Gd0LVDfT6UCav8lEH3dDvY7XWOUilO1it1q_189fUqn3f4MxONp2U-vTq0R39Ku6rQtgOWUv4HFFp5DMvbsvOyjRUpSMxNt5PLOUz7EgGqEOMJbYe-1FnrHFo3KpextDc40ua0WqudZ080Nfm8xve3UY4vNWIjmhV4_cQQBE5FtGBWWvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h2l39HsV7YTnA1wPipxIRoKsbjvQGqjPsWvv-WQojOWJz2NrojpMJTpVvmNy5toA6fMZw8K4s4x5aO-9_6LvIcYA0w2ArEK0m2qNFWCheeI2gCGuQIYESrN27QYW4XwdsAYu0fmwDg9WfrI0mxJy4pXiPAL1HjjEpRKUc4-yx5z2eBti5r_3g5f02gUNRGTbqoDi1Dfohl_tlZ3LSF3FldXjbFGULGXn2-sdDmV9G3WRfU5jXvA9Faf6y4c7IfQC4p7KpvLAD3S8mFZWCP2ya7oACsH2jyW8U6r6dqng1a9RenE7oc7-eGUb0l2aEj0IVC0Kb7SDt_EC-NRK-pqj_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
تصاویر منتسب به نیروگاه برق پایگاه نداسا در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67578" target="_blank">📅 00:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67577">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56e60a602e.mp4?token=Kl6pvaPhhJ46I20b8GPFoUAzxbJkaPq_4HRAQAWpdXlti5bs1VC8zSi8uH1wXccFTfbKxt49PpBehb1XPbvQD1gFi05Ak8kOvKTfquX5sQxgyxS2-GEL5hpyCrk4t24Hm1psOO6QgH43-n6Fondb7vU2LFIp8JB0FUDt7-xTVUaGTlMTvXK8Se4hxW1W6Fc0KWm6QA3ByJpLPZQjgMvCJBoyEtdNKFmf6kGjDKb7sveaEAARwC1U3m1GFYhF1s-AfxwNok_5oZoQLiSdJBmiao0-c2dRp_j-H_eFfCsDpcuMd9XB8duQCp6BatkDj_hEbI04iVXnaKq2p6HfbPiVBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56e60a602e.mp4?token=Kl6pvaPhhJ46I20b8GPFoUAzxbJkaPq_4HRAQAWpdXlti5bs1VC8zSi8uH1wXccFTfbKxt49PpBehb1XPbvQD1gFi05Ak8kOvKTfquX5sQxgyxS2-GEL5hpyCrk4t24Hm1psOO6QgH43-n6Fondb7vU2LFIp8JB0FUDt7-xTVUaGTlMTvXK8Se4hxW1W6Fc0KWm6QA3ByJpLPZQjgMvCJBoyEtdNKFmf6kGjDKb7sveaEAARwC1U3m1GFYhF1s-AfxwNok_5oZoQLiSdJBmiao0-c2dRp_j-H_eFfCsDpcuMd9XB8duQCp6BatkDj_hEbI04iVXnaKq2p6HfbPiVBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
آتش سوزی در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/67577" target="_blank">📅 00:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67576">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
گزارش‌های اولیه حاکی از آن است که هدف آن‌ها نیروگاه‌ها است. قطعی برق در چابهار گزارش شده است.
هنوز تایید رسمی نشده.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/67576" target="_blank">📅 00:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67575">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
انفجار های پی در پی در بوشهر و کیش.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/67575" target="_blank">📅 00:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67574">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
آکسیوس به نقل از یک مسئول آمریکایی:
حملات به ایران، رادارهای نظامی، پایگاه‌های موشک‌های ضدکشتی و سامانه‌های دفاع هوایی را هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/67574" target="_blank">📅 23:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67573">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
❌
گزارش‌های اولیه حاکی از آن است که یک پالایشگاه در جزیره لاوان مورد هدف قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/67573" target="_blank">📅 23:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67572">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dRN--RhfWexeGBXlj4X7GX1h9fJGiEeHQ9gktKEEeJBfwIKiBMJkrMFvqLGY5ztgVw22YFQ07c4NA1Ts9tgPfh0z0X8vEkYYPAXHG_mCAjH-CN2QlDN5lW7k7zVWnv4myAkr16xe66ejlw2wJmjlcS4fW3Yb4_G6eFW6b1bCZrKO2nbqjSUuiVAMaxwaC4QtaCWDQNrtEbg_Bc1GnFw-1uj_XFe1zZbeQgXLnATLh2OaKlGMfQJhtzuFtXh_PnNsHdFcc1seXgkyHuHIzswcOG-oSkMlBOPCplSbJrF7L9_uPcvvftCChtCGtDp7UENYSqeiuFWwDbf8nCeYwA2bLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
حملات آمریکا به چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/67572" target="_blank">📅 23:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67571">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🚨
انفجارها در بوشهر و جزیره خارک
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/67571" target="_blank">📅 23:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67570">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
🚨
چندین انفجار در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/67570" target="_blank">📅 23:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67569">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfrPEHiTZ6YcBpXukMpPWAa-hXRi5m-RIMiEJBX2J1q889bL_IM6E7hhg7_hcyIl5ZV9XYhofNDYQBO4RjeTcJsmi7WUYYLg1oFxiRMrYLbh6tUYvTZLjCGQ4HDjwktnAi7mT0MexGqgJDSPsTFvdrIPdElZJ1JY6JTrjW2UfshukXcY9JcF8KiIv3vNwoQDSmUiRphqyLJPMt6RbEcHUxPmsQFQ4FYuPGGUNoVuJf1Q0R2MtVsbT12KCEYECBykKRl9uDRK0RbREuOmiOJwftgjWmNcXzZw6udeiy-lNoH8D_-OCtoydCIbWsCpR3WQxbzfmcZu2AD6THTUQiKDxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده:
به دستور فرمانده کل نیروهای مسلح، نیروهای فرماندهی مرکزی ایالات متحده، عملیات‌های بیشتری را علیه ایران آغاز کرده‌اند تا توانایی این کشور در تهدید آزادی کشتیرانی در تنگه هرمز را بیشتر تضعیف کنند.
ایالات متحده، ایران را مسئول اقدامات تهاجمی اخیر و غیرموجه علیه کشتی‌های تجاری و خدمه غیرنظامی که به صورت آزادانه در یک آبراه بین‌المللی حیاتی تردد می‌کنند، می‌داند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/67569" target="_blank">📅 23:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67568">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
صدای چند انفجار شدید در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/67568" target="_blank">📅 23:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67567">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
آکسیوس به نقل از یک مقام آمریکایی:
ارتش آمریکا در حال انجام حملاتی علیه اهداف نظامی ایران در تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/67567" target="_blank">📅 23:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67566">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
پادگان ارتش در کنارک توسط آمریکا هدف قرار گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/67566" target="_blank">📅 23:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67565">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
دو انفجار در جزیره لاوان
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/67565" target="_blank">📅 23:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67564">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1d5e85683.mp4?token=KCa_TL_88otIxMCPb_iU-tz-68ITpi86m6Li-8RgC4DSFqESaRfjiXYAHzbUmu2IsN-SkvmK0ibBBFPu1ydTm3vHeB1-qxlNMKAmJxY13Iz-mobflqey6KubQeXPRioZuZG06SCNM5krkVDKhmPy7D3aFrx1MlezvLphQ7ph5HSM3ixrmcJFncnPrinasHTcURHhoZe5g-qlFZ70yv67wkjvJdftmprR5vVJTQ2mVjrlQZoFirXKihYJdELgtcdTeMXVX8lWeZHfJViqa90u9egp9blECmLyT2JiQjDARVdJPl4LrpU68p7XMwDt8MeyizcJFp48O9xLZwB2oa8jaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1d5e85683.mp4?token=KCa_TL_88otIxMCPb_iU-tz-68ITpi86m6Li-8RgC4DSFqESaRfjiXYAHzbUmu2IsN-SkvmK0ibBBFPu1ydTm3vHeB1-qxlNMKAmJxY13Iz-mobflqey6KubQeXPRioZuZG06SCNM5krkVDKhmPy7D3aFrx1MlezvLphQ7ph5HSM3ixrmcJFncnPrinasHTcURHhoZe5g-qlFZ70yv67wkjvJdftmprR5vVJTQ2mVjrlQZoFirXKihYJdELgtcdTeMXVX8lWeZHfJViqa90u9egp9blECmLyT2JiQjDARVdJPl4LrpU68p7XMwDt8MeyizcJFp48O9xLZwB2oa8jaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملات سنگین آمریکا به پایگاه سپاه در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/67564" target="_blank">📅 23:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67563">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
🚨
حملات آمریکا به بندر کنارک در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/67563" target="_blank">📅 23:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67562">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🚨
گزارش صدای چند انفجار سنگین در بندر چابهار
به پایگاه امام علی در چابهار حمله شد
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/67562" target="_blank">📅 23:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67561">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
خبرگزاری آکسیوس :
ارتش آمریکا امشب حملات بسیار سنگین تری رو به ایران انجام خواهد داد
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/67561" target="_blank">📅 23:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67559">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aXwz_YOLrFdV35LQJ1iqUOOYFCY1FrmTmM9shMhmZ2JPIwcz4K6x3aeQk_j7mRdJqiH6IHoEUgc-nXwz0zq37u-RNtx81wq8Jy1133QFjqpWvStibCFt_x4o3m9JMFwDWuwZvud0VVz_X2R9-hqjRDxUJ8nDX-M9vugxmKVmbogOIVOWzIuP-YJKi9uBhlCE17S88XYalIMZmQMNEwVwe9wTWmhxrF9aFgfl41KHLFvJqXMC4NaXgCKWYBc5ncNJHxBKpHxZcVyPDCUB-cbDG16Cm_kJhNKs5IoJFjF1AgPAhI-yhfjmTWH6f-WA7wlgmO-os7gpnlJBBsFMkJsk7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GRG-XdEA13NuXhlukA9xqF9ADYCiHA9FHuBkM_aQplLcJE_grND4T1SWJPdig8-DSVg3rs7tamsgLyypAC-e6DAcd3srAzlQNpRszYfACfe3jThx35499xVdr_AlXIUjZ5x_IYQzmnDSeTHa16SOo8qb-L7vscCiCcC2NaYO6shwcgNPZs16W2FDzDzLw0NlHMxo2oDl3vNV7FoTt6DF5GAi4M6QNTwhXPXrLAdMQqAWKTWvxm-_TEUS06mcp0i7axzIl_O9xIn9dZBX7DCMJ7k1xkESwZOkBOflKwualKLLdX7-4Bq6JHm2Yheg_srZ-6iAewWTS4PPuOjK_PphFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
بلند شدن سوخت رسان ها از تل آویو و امارات به سمت جنوب ایران
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/67559" target="_blank">📅 23:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67558">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
🚨
فعال شدن پدافند در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/67558" target="_blank">📅 23:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67557">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🚨
مجدد انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/67557" target="_blank">📅 23:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67556">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
🚨
حملات آمریکا به سیریک هرمزگان
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/67556" target="_blank">📅 23:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67555">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
❌
شنیده شدن صدای انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67555" target="_blank">📅 23:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67554">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c65cdf89e.mp4?token=Q3Wjqwf0mYHfhZixBpu0pUzlwMirRb3k7vM4dWURgZSoseh1NS1kaVkXdQfjhrD0JwsdtRr5Ak-C7F1MPlF2wg-9a_E1Lfp_6zoRdy1vL4XPiWkx_4_J1HXjHU-_e89Uu58f2JXN9pafuFe1IlxwkwLvKKCUaBsfWmrMOHYCBEDaOAk5MAe-DijelEkJiTl_KegE3415WZhyxQgWL5T580BQrur9_beMegGvfOD4yBbBqaV2JK3-BON2odp5PZNkOlAl4eHhqxyZ8mzxsgtEXVIH_1Q9RqbtbOX7Cm37-9WH4Er4pzL9MKjRS0cV_STJVysDcHq7L8923pzKltEV9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c65cdf89e.mp4?token=Q3Wjqwf0mYHfhZixBpu0pUzlwMirRb3k7vM4dWURgZSoseh1NS1kaVkXdQfjhrD0JwsdtRr5Ak-C7F1MPlF2wg-9a_E1Lfp_6zoRdy1vL4XPiWkx_4_J1HXjHU-_e89Uu58f2JXN9pafuFe1IlxwkwLvKKCUaBsfWmrMOHYCBEDaOAk5MAe-DijelEkJiTl_KegE3415WZhyxQgWL5T580BQrur9_beMegGvfOD4yBbBqaV2JK3-BON2odp5PZNkOlAl4eHhqxyZ8mzxsgtEXVIH_1Q9RqbtbOX7Cm37-9WH4Er4pzL9MKjRS0cV_STJVysDcHq7L8923pzKltEV9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇱
خبرنگار: شما امروز با هگست جلسه دارید.
نخست وزیر نتانیاهو: احتمالاً این اتفاق نخواهد افتاد.
خبرنگار: آیا این شما را ناراحت می‌کند؟
نخست وزیر نتانیاهو: چه کسی گفته ناراحت کننده است؟ شاید معنای دیگری داشته باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67554" target="_blank">📅 23:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67553">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/176e4f444a.mp4?token=SCqoHwPcV8yItPRHiF7Rp3e992YBog6QhI43H34r7aF5GTH_3J542HpBR-EF-pViflZIGM1-KTSrhC-zeJ15WBpTh5COllteUTnFk-pigjm0ztFB8uiZ6mxEl6sMrZxGoNAnCPAzDzTH44mBZZJNHHifLnbKtCiphRQxpKlpVgWLtnjeMjmigy8l7Xo2oPvCTzXV7pmNVF9o1HZjEJAcMrUGr6PjDJVM23UzNTJc2g3nLq1VRllwOC2BzB3GXoMN114Dc3o4D7kvnkaB8W69W4X6qRWW6NBHqw_Jx2xQx4EzzsynUytNcTSPcnt95PSaTdvVglFYNr1xlACd5cHBBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/176e4f444a.mp4?token=SCqoHwPcV8yItPRHiF7Rp3e992YBog6QhI43H34r7aF5GTH_3J542HpBR-EF-pViflZIGM1-KTSrhC-zeJ15WBpTh5COllteUTnFk-pigjm0ztFB8uiZ6mxEl6sMrZxGoNAnCPAzDzTH44mBZZJNHHifLnbKtCiphRQxpKlpVgWLtnjeMjmigy8l7Xo2oPvCTzXV7pmNVF9o1HZjEJAcMrUGr6PjDJVM23UzNTJc2g3nLq1VRllwOC2BzB3GXoMN114Dc3o4D7kvnkaB8W69W4X6qRWW6NBHqw_Jx2xQx4EzzsynUytNcTSPcnt95PSaTdvVglFYNr1xlACd5cHBBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سرنگونی پهپاد MQ-9 آمریکا توسط جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67553" target="_blank">📅 22:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67552">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/697775e593.mp4?token=FId8yRiQQPUrPG4uIuAFaFDqvShmnYrdiODv8HSvjC-vy2oudK3fT7sd_ph1KKfGPjVSlCx9LRAOp9wk0EQag1UPLLgAe2YQ0tqcgzMvhQZpdxX_wMw6DroiozFhTfdCbcIIpacxC_jBbyFA9DwPaz8qduN_Oo4GACxCpWJGqzpFK4j6r2-oNZm_YPzBOM3EPKtSBip-Ef4BfUOHlEgf_hhzfTP_J0dtfB_0q8aafHi5ibzO8_nh9k3g0dgaFPBuhAC_N-Gi5y0zGYukeoIvLEA8N89p2f8g0rAoHzxeDCK84f3LXqqgOTPOyBgfw4BB6XbAMGGSxJuSj4okqAgZiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/697775e593.mp4?token=FId8yRiQQPUrPG4uIuAFaFDqvShmnYrdiODv8HSvjC-vy2oudK3fT7sd_ph1KKfGPjVSlCx9LRAOp9wk0EQag1UPLLgAe2YQ0tqcgzMvhQZpdxX_wMw6DroiozFhTfdCbcIIpacxC_jBbyFA9DwPaz8qduN_Oo4GACxCpWJGqzpFK4j6r2-oNZm_YPzBOM3EPKtSBip-Ef4BfUOHlEgf_hhzfTP_J0dtfB_0q8aafHi5ibzO8_nh9k3g0dgaFPBuhAC_N-Gi5y0zGYukeoIvLEA8N89p2f8g0rAoHzxeDCK84f3LXqqgOTPOyBgfw4BB6XbAMGGSxJuSj4okqAgZiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ پس از پایان اجلاس ناتو، ترکیه را ترک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/67552" target="_blank">📅 22:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67551">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">حوصلم سر رفته بود این گردونه صراف رو زدم، 5 دلار داد
😐
😂
گفتم لینکشو بذارم شما هم بیکارید یه تستی بکنید ببینید چی میده بهتون
👇
https://r.saraf.app/s/agrd068</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67551" target="_blank">📅 22:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67550">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FN5yFpzoZJKm-kptOyTpcxSgxgeQF5M-4s_17G-NQgRVkQVEgVway1RFMvG_Sj6R8S85oCprAywv88bMYblnLMal6vhwcHx3GQKmRl6bxYq5fv5FQMK9K7eTsxwQ10ZW_V9nVE_VoXPqMCCScS_ubeIDP8JNU70aPwaWJzgHH4dElr2DYpzu8H7_TXYdBKTHYNXcP2M8VseH-l6B8PqbCGMW1GJYGCnOOMOp7zXogOTj4UYn9s8mht4bzldX0PZuQHdJw3fZUke6toWIzYCrpIzs-xsgiNXZ2wg9qzVK-1USVgyF_po6m5ISUo2hQOx_6Ox91ifS5I8_nRUlMsysZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
عراقچی:
صحبت کردن با لحنی تحقیرآمیز با ملت بزرگ و شجاع ایران، از عظمت آن نمی‌کاهد.
ایرانیان به خاطر متانت، فرهنگ و ارزش‌های اخلاقی قوی خود شناخته شده‌اند. ما به بی ادبی با بی ادبی پاسخ نمی‌دهیم، بلکه با عمل: با شجاعت و با از خودگذشتگی فراوان.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67550" target="_blank">📅 21:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67549">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
گزارشگر: ماه گذشته، شما گفتید که رهبران ایران بسیار عاقل هستند. حالا شما می‌گویید که آن‌ها افراد بیمار هستند. چه تغییری رخ داده است؟ ترامپ: من آن‌ها را بهتر شناختم. آن‌ها بسیار عاقل‌تر از سطح اول و دوم هستند.  @News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67549" target="_blank">📅 20:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67548">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/412c846bfe.mp4?token=tGFL9ixvGV6MXX60CWsR3WoytAlssudAj7S2wSEEw2R83iHDj6EAkvWo-kUVU41nr6yyqT_-57KbQ6DcAb0AGsXGz4ohUIrV9CC7cDEEBmzKw-TyniWJSfQ7Eqgu9aAoyZBlW0BuGS2mqrZvftGnZ3UeM317Fqnyy4spOtA9zIrcCgEZ8mPxBGxGXGzKSrU82rUqfQwqUf63QQppO8O-bNjP5OTydnBTIiBf4mmsLMzXijG0QqgaHupQYEhHDYD35z2a4pRZgqe6SqENSxtrqEblDWy1JnrBV4Lpwh9999ulScg-Xt1bEGYZ2oQurnUyag7LHRsj5SDCyIb4c5uT-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/412c846bfe.mp4?token=tGFL9ixvGV6MXX60CWsR3WoytAlssudAj7S2wSEEw2R83iHDj6EAkvWo-kUVU41nr6yyqT_-57KbQ6DcAb0AGsXGz4ohUIrV9CC7cDEEBmzKw-TyniWJSfQ7Eqgu9aAoyZBlW0BuGS2mqrZvftGnZ3UeM317Fqnyy4spOtA9zIrcCgEZ8mPxBGxGXGzKSrU82rUqfQwqUf63QQppO8O-bNjP5OTydnBTIiBf4mmsLMzXijG0QqgaHupQYEhHDYD35z2a4pRZgqe6SqENSxtrqEblDWy1JnrBV4Lpwh9999ulScg-Xt1bEGYZ2oQurnUyag7LHRsj5SDCyIb4c5uT-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ خطاب به ممدباقر درباره اورانیوم:
ما دوربین‌هایی داریم، که بخشی از نیروی فضایی ما هستند، که می‌توانند نشان شناسایی فردی که به یک سایت خاص می‌رود را بخوانند. محمد، چیزی آنجا وجود دارد که با بیل و کلنگ در حال کار هستند.
بیل و کلنگ به شما کمک نمی‌کنند. بزرگترین ماشین‌آلات دنیا هم به شما کمک نمی‌کنند. این موضوع بسیار، بسیار عمیق‌تر است.
اما ما این موضوع را زیر نظر داریم و اگر کسی به آنجا برود، منفجر خواهد شد. بنابراین، هیچ‌کس به آنجا نزدیک نخواهد شد. در نهایت، ما آن را تصاحب خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67548" target="_blank">📅 20:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67547">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd8dc7e8bc.mp4?token=XVwssvTXM4Rd2JeeHGhz4u1lDt3joDuoPqmMtvI7-GtC--L-zG0R6aohkfHenGczB_wedJLQZO6N8Vb17PFqXLox0ZiFx3NxPbxvlEO_Qn6NVwzNhMk2nQdPPhg8IOqyJWpZJV4nrS0suDuZ3T2S1blfiQROtpCNpmI5Vyfhx_8dkMHWTEaMdji7ZOrBDwyckOIqZTQXdvn2pc56MUiGSD1BjjiiV89N3XtY3NqlxhbzC8Ba3AGtvToTqtzT93z5ZxNqEUN3ys9rEYvYDvgFjNpuokj4ydMyM-quE2s3_5IkX0JDyUvxXH3M7JwX6-1gsWiq2te-JdSaOUJrvIWaWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd8dc7e8bc.mp4?token=XVwssvTXM4Rd2JeeHGhz4u1lDt3joDuoPqmMtvI7-GtC--L-zG0R6aohkfHenGczB_wedJLQZO6N8Vb17PFqXLox0ZiFx3NxPbxvlEO_Qn6NVwzNhMk2nQdPPhg8IOqyJWpZJV4nrS0suDuZ3T2S1blfiQROtpCNpmI5Vyfhx_8dkMHWTEaMdji7ZOrBDwyckOIqZTQXdvn2pc56MUiGSD1BjjiiV89N3XtY3NqlxhbzC8Ba3AGtvToTqtzT93z5ZxNqEUN3ys9rEYvYDvgFjNpuokj4ydMyM-quE2s3_5IkX0JDyUvxXH3M7JwX6-1gsWiq2te-JdSaOUJrvIWaWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
مطمئن نیستم که بخواهم با آنها به توافقی برسم.
ما می‌توانیم بازی‌ها را انجام دهیم، اما مطمئن نیستم که بخواهم به توافقی برسم.
فقط بیایید این کار را به پایان برسانیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67547" target="_blank">📅 20:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67546">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1d009a331.mp4?token=vxjcvb6W2PABM4EqQpqTQDBKxSXELA0prniydxl9fUEYdVlzeoghLJpqQ0JE6828AgEUbi6kbC-TC32lZcbA5khSmZlRGfugscD6NhHyEbpwZrp4sAuH6UVASant0sLZm6r5c2l4cgmGkajQFSdnXH3024sW1e00uja2vNoG8jN1bb6LlYws4dEwo7J2n5oJoPxn-XAvoB7OMYxP0Q-xrEKY77Z9JXcQakuCqN57rTX4L9wQCl2Bso4ckkDX1pEQtqk01Fe-QmWyAsXuv0tJ6Im7qxReSkjtkt6tJWEChmaUiCe5BDFfLa4MvoaGfUbk4fcwyM3y4ZHWnEixM7dszw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1d009a331.mp4?token=vxjcvb6W2PABM4EqQpqTQDBKxSXELA0prniydxl9fUEYdVlzeoghLJpqQ0JE6828AgEUbi6kbC-TC32lZcbA5khSmZlRGfugscD6NhHyEbpwZrp4sAuH6UVASant0sLZm6r5c2l4cgmGkajQFSdnXH3024sW1e00uja2vNoG8jN1bb6LlYws4dEwo7J2n5oJoPxn-XAvoB7OMYxP0Q-xrEKY77Z9JXcQakuCqN57rTX4L9wQCl2Bso4ckkDX1pEQtqk01Fe-QmWyAsXuv0tJ6Im7qxReSkjtkt6tJWEChmaUiCe5BDFfLa4MvoaGfUbk4fcwyM3y4ZHWnEixM7dszw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
املاکی درباره ایران:
به نظر من، جنگ با ایران دوباره آغاز نخواهد شد. وقتی آنها حمله می‌کنند، ما ۱۰ برابر قوی‌تر پاسخ می‌دهیم.
شاید امشب به آنها حمله کنیم.
هر اتفاقی که قرار است بیفتد، خیلی سریع رخ خواهد داد.
ما به دنبال یک راه حل بلندمدت نیستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67546" target="_blank">📅 20:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67545">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
من می‌خواهم این موضوع را در مورد ایران به پایان برسانم و با رهبران فعلی بازی نکنم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67545" target="_blank">📅 20:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67544">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/966c88b1c6.mp4?token=ZkOOci7GFdWKbbbIdTEc99KQVOOuHuVDF4dieWL2mgyfiKZoDV4SdEP_VwU74lg1a3b3HZJybf-pegLI-mC_0jwpfgKTufpJRfj73Si7gJu4Z4EI7088DSxSprXdAoNed5OJBnYYJUulqLXKzRPAf1WCCj8swA3OAFGoF7N1yFfL6DpPYMCMquIoEIdNfMqOtNTdl3g-ogd5YeZbsxQQo6KeeQ7ukC0e7ea1CFwe1HuvskIqnHJNNHqmf1H13-P_f4TjjO-mQaDulOKCCsLvhufpgnhJxgPePye6vs3VjZ6zRsY8EGyUgZuZORxXzw13bNuXAps04P7fefnA8TOCgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/966c88b1c6.mp4?token=ZkOOci7GFdWKbbbIdTEc99KQVOOuHuVDF4dieWL2mgyfiKZoDV4SdEP_VwU74lg1a3b3HZJybf-pegLI-mC_0jwpfgKTufpJRfj73Si7gJu4Z4EI7088DSxSprXdAoNed5OJBnYYJUulqLXKzRPAf1WCCj8swA3OAFGoF7N1yFfL6DpPYMCMquIoEIdNfMqOtNTdl3g-ogd5YeZbsxQQo6KeeQ7ukC0e7ea1CFwe1HuvskIqnHJNNHqmf1H13-P_f4TjjO-mQaDulOKCCsLvhufpgnhJxgPePye6vs3VjZ6zRsY8EGyUgZuZORxXzw13bNuXAps04P7fefnA8TOCgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
هر اتفاقی که قرار است بیفتد، به سرعت رخ خواهد داد.
ما به دنبال راهکارهای بلندمدت نیستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67544" target="_blank">📅 20:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67543">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ce02ad2ec.mp4?token=sqkdtPTufZacBFAriQNqLC420DBg9Nl17pcxZFSmKD9V8VEXLYHybbQVA8gYNGFHt-X5d5_vYhHZpIzv92sf44DX9WnbO2LlY5IC2eS3G5GhGDZETpsIdCYD1ysgOv3gJYlB1aAO-ZIxUlg2ZrsPdjB8_FxnLsVWZhCD5xSCfnSlGA8PU3hGZvlf2uHl65KEHv4lra_iaEqPnI62Of2-HfOfM0pn8IlIBtWJV-euNJhtb6OaH7ourrq6wYyylpljbwoi7uJOrYoe5OCFenpHBR4VZgrDbZ8QNFjJhqJOnIDpuRyEGVdsKUEmN-PVtTIEqAbZzwHqkW8tEM-U9Gfk-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ce02ad2ec.mp4?token=sqkdtPTufZacBFAriQNqLC420DBg9Nl17pcxZFSmKD9V8VEXLYHybbQVA8gYNGFHt-X5d5_vYhHZpIzv92sf44DX9WnbO2LlY5IC2eS3G5GhGDZETpsIdCYD1ysgOv3gJYlB1aAO-ZIxUlg2ZrsPdjB8_FxnLsVWZhCD5xSCfnSlGA8PU3hGZvlf2uHl65KEHv4lra_iaEqPnI62Of2-HfOfM0pn8IlIBtWJV-euNJhtb6OaH7ourrq6wYyylpljbwoi7uJOrYoe5OCFenpHBR4VZgrDbZ8QNFjJhqJOnIDpuRyEGVdsKUEmN-PVtTIEqAbZzwHqkW8tEM-U9Gfk-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
گزارشگر: ماه گذشته، شما گفتید که رهبران ایران بسیار عاقل هستند. حالا شما می‌گویید که آن‌ها افراد بیمار هستند. چه تغییری رخ داده است؟
ترامپ: من آن‌ها را بهتر شناختم. آن‌ها بسیار عاقل‌تر از سطح اول و دوم هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67543" target="_blank">📅 20:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67542">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac6daa8309.mp4?token=SVVfLlLznv2Y8z9vcW80VrwF3p0nBgQlmZ7YVXj9NlhnkJw5f22MWFNG2ne9sYCfIjKTSGmxUPJSPuAIkpjy7gRFHIH3R5vsz2rzmZ8m9Kp-199e34EtxqyCShq4D6S-3fWNvcFOGxPH4C9A9Cdx6ynK8whV-aKOH3aKmvAx6eJ22V2r1SqFcFEzp6ydPZlAPIhy1Kdm8MplnFg7ZqytkyZpxyHzTjkDGXe5lnnnHABMKtGgF7DpVJgbV0czVTcqBgqycHAN6vCVnxWkLmGwyqawHf8WEBEIsLP26hbXxZdB-xiOALfhsJ4IW8xAeKSDSLgXSlhp44LeDM2de4V5-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac6daa8309.mp4?token=SVVfLlLznv2Y8z9vcW80VrwF3p0nBgQlmZ7YVXj9NlhnkJw5f22MWFNG2ne9sYCfIjKTSGmxUPJSPuAIkpjy7gRFHIH3R5vsz2rzmZ8m9Kp-199e34EtxqyCShq4D6S-3fWNvcFOGxPH4C9A9Cdx6ynK8whV-aKOH3aKmvAx6eJ22V2r1SqFcFEzp6ydPZlAPIhy1Kdm8MplnFg7ZqytkyZpxyHzTjkDGXe5lnnnHABMKtGgF7DpVJgbV0czVTcqBgqycHAN6vCVnxWkLmGwyqawHf8WEBEIsLP26hbXxZdB-xiOALfhsJ4IW8xAeKSDSLgXSlhp44LeDM2de4V5-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
می‌دانید؟ ممکن است من هم دیگر نباشم.
من هدف شماره یک آن‌ها هستم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67542" target="_blank">📅 20:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67541">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0540439bf4.mp4?token=nTnQirPWx_uc_Ybewi7sbMXNuBLf4LJa4m_Mv9b6o9FeiejkTpndq_lpDvVVlNBdRmt7B--xznPc-Q68Jv1VR8odmykXvUAZUjb9eHl4bJXDSALDsmCV4IpC1QQMVINCRQL3Huyej1HBsyeWRE4Ez67OcJKNQQBqcIJzhSzhh348XpnkGzR5pulLRQA5EDXIsy2aF7RHueHbAqBdikIULhXbQyV6aYk9Y2aAjANbujB0D2p_vOBUha5eQpR61zHsEh239QNvnK7rYrAxy6X4D7BrtvTVeGrZV18iNc_CpAlmhpWbhqu5XftWPBrrw_rom8MWsXnlO9O7FFW45-C8iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0540439bf4.mp4?token=nTnQirPWx_uc_Ybewi7sbMXNuBLf4LJa4m_Mv9b6o9FeiejkTpndq_lpDvVVlNBdRmt7B--xznPc-Q68Jv1VR8odmykXvUAZUjb9eHl4bJXDSALDsmCV4IpC1QQMVINCRQL3Huyej1HBsyeWRE4Ez67OcJKNQQBqcIJzhSzhh348XpnkGzR5pulLRQA5EDXIsy2aF7RHueHbAqBdikIULhXbQyV6aYk9Y2aAjANbujB0D2p_vOBUha5eQpR61zHsEh239QNvnK7rYrAxy6X4D7BrtvTVeGrZV18iNc_CpAlmhpWbhqu5XftWPBrrw_rom8MWsXnlO9O7FFW45-C8iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
ایران می‌خواهد به توافقی برسد، اما نمی‌داند چگونه باید به توافق برسد.
و سپس، شب‌ها به کشتی‌ها حمله می‌کنند. من این کار را دوست ندارم.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67541" target="_blank">📅 20:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67540">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff03b3210e.mp4?token=hoLI3alymaUVZjVxfOZkk16UO0t8PkHtrHrUFqUStESrDCfunB5oDgaabABu82-6vTgbeNfKtVQ9B0igmJs1HEteamoLAZOuR1nvgD-bksqo7OxOnHD30xTMQ6_fhHAP5FEggkDM4VdGTzFf7TSU2cA4E4ZupwihFhv5MhqGUeFMQ8twVS5oAilYEthoID0q_t4C0veBuIyHzqNi-lpKYHKYO9Q-zAd2_o8CKrGol35FKGZMsbavF0pRxi-m0E89HKAGCOQgzeh2trEE2HqF2ehguMaZeU-8vAY03sxGcwk092k0ALaYwjRG2kpDtUHs-3LrAWmVfvOQtFGlQpO7TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff03b3210e.mp4?token=hoLI3alymaUVZjVxfOZkk16UO0t8PkHtrHrUFqUStESrDCfunB5oDgaabABu82-6vTgbeNfKtVQ9B0igmJs1HEteamoLAZOuR1nvgD-bksqo7OxOnHD30xTMQ6_fhHAP5FEggkDM4VdGTzFf7TSU2cA4E4ZupwihFhv5MhqGUeFMQ8twVS5oAilYEthoID0q_t4C0veBuIyHzqNi-lpKYHKYO9Q-zAd2_o8CKrGol35FKGZMsbavF0pRxi-m0E89HKAGCOQgzeh2trEE2HqF2ehguMaZeU-8vAY03sxGcwk092k0ALaYwjRG2kpDtUHs-3LrAWmVfvOQtFGlQpO7TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
فرماندهی مرکزی ایالات متحده:
امروز، بیش از 20 فروند از ناوهای جنگی نیروی دریایی ایالات متحده در حال گشت‌زنی در آب‌های سراسر خاورمیانه هستند، در حالی که نیروهای سنتکام به ترویج امنیت و ثبات منطقه‌ای ادامه می‌دهند. ماه گذشته، ناوها و هواپیماهای نیروی دریایی آمریکا به صورت منظم در دریای عرب حرکت کردند و قدرت نظامی و توان آتش بی‌نظیر آمریکا را به نمایش گذاشتند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67540" target="_blank">📅 20:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67538">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‼️
ویدیو ای که سپاه از حملات دیشبش به پایگاه های آمریکا در منطقه منتشر کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67538" target="_blank">📅 19:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67537">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/735f956d53.mp4?token=g-FeuWGZC5HEIyVkVx_9GAcQ6Iv8vrwtl2Pi5tz5yMVCMrMrZSIGcJ4mCVdegg-1MdedIWtELi37FTs4qyEVhweW5evIc-vg5A420NfH-NHd7X_qKoT8yIbKoBeFMSmvoMaPp587EhJY1hddAjjqivK65laS3YeuG8XTlL6jyCDFWTciZIClyOhFFkmaCLr8k8GDDvhF8pYFqRoa6vD8N2lrVkgGiJzKd9Bo-V2FQvQFM_mIxYprH7o7KyKd62MwWWrIkeoijQak2LWliifs03a48t55gGqbOS6faCjPYHXHnT_sB-lmBisYxPYOJyA0v7XtgJMuqdXVa-kxdYWYfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/735f956d53.mp4?token=g-FeuWGZC5HEIyVkVx_9GAcQ6Iv8vrwtl2Pi5tz5yMVCMrMrZSIGcJ4mCVdegg-1MdedIWtELi37FTs4qyEVhweW5evIc-vg5A420NfH-NHd7X_qKoT8yIbKoBeFMSmvoMaPp587EhJY1hddAjjqivK65laS3YeuG8XTlL6jyCDFWTciZIClyOhFFkmaCLr8k8GDDvhF8pYFqRoa6vD8N2lrVkgGiJzKd9Bo-V2FQvQFM_mIxYprH7o7KyKd62MwWWrIkeoijQak2LWliifs03a48t55gGqbOS6faCjPYHXHnT_sB-lmBisYxPYOJyA0v7XtgJMuqdXVa-kxdYWYfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
صدا و سیما و رسانه خامنه ای برای اولین بار فیلمی از حسینیه امام خمینی در بیت رهبری جایی که رهبر جمهوری اسلامی مورد هدف قرار گرفت را منتشر کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67537" target="_blank">📅 19:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67536">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
یدیوت احرونوت:
نخست‌وزیر اسرائیل، نتانیاهو، و وزیر دفاع، کاتز، حضور خود را در یک رویداد لغو کرده‌اند و در حال بحث و بررسی مسائل امنیتی مرتبط با تحولات مربوط به ایران هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67536" target="_blank">📅 18:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67535">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62a14b7982.mp4?token=RGl8Rmu7u2hp6gkmd68Zf3ChfIzVgOcLtx2TYO_1b0zkskze7tG-Pl6-leQ9B-yIYCmt2g08q4X1MIFMgm5Kad0r-iJ8Zn4UhHGyptyfqvT5mP1G8sE_T4vHA6s9IZnW_4eLo0jzeYVnsmYB_MSC5seLQaZH6tVw6ZN60H47kc0KQniICIXkq28Xjc9frMJwcR7EOLiKboVC_is7_AZzKyCFFxG2EsFB9Ca0bNzReliQzz4ieXeaI6JzxmL7HivS5IEkZNWNbOju7ORBUWkj8qyr3k3GTGsmGd11Br4RppQExKZJiyzrAy0ByKQC5a5cR41a-k6jDYb_k_ElpNegYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62a14b7982.mp4?token=RGl8Rmu7u2hp6gkmd68Zf3ChfIzVgOcLtx2TYO_1b0zkskze7tG-Pl6-leQ9B-yIYCmt2g08q4X1MIFMgm5Kad0r-iJ8Zn4UhHGyptyfqvT5mP1G8sE_T4vHA6s9IZnW_4eLo0jzeYVnsmYB_MSC5seLQaZH6tVw6ZN60H47kc0KQniICIXkq28Xjc9frMJwcR7EOLiKboVC_is7_AZzKyCFFxG2EsFB9Ca0bNzReliQzz4ieXeaI6JzxmL7HivS5IEkZNWNbOju7ORBUWkj8qyr3k3GTGsmGd11Br4RppQExKZJiyzrAy0ByKQC5a5cR41a-k6jDYb_k_ElpNegYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
خبرنگار: آیا برنامه‌ای برای اعزام نیروی زمینی به ایران ندارید؟
ترامپ: چرا باید الان وارد عمل شوم؟ من زمانی وارد عمل خواهم شد که آن‌ها کاملاً از بین بروند یا به یک توافق برسیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67535" target="_blank">📅 18:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67534">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2479db8c8d.mp4?token=b5NUGUFcwknfXWKcs04FgsSuep_LpSezJIU4y2xapqf4OuIfE5y9FI09cyLA0PkKIWuLmczxUS8nuQp_fsvEMM0fdbDpM6pU6RNFj2wdmRcQK-JZsxtMnDdSdNQv-U-Bmgrm8nm23zojB0BAHkfCh9FFyOvW1WvAaB4kXPr_q742RGJZKRk9K64r4jd-dNSWDkzVxMoKrNJwwWY-PZ4qr-2nHaXFtq-Y3TfSSy_Bqz6xWjoKKClZ2Z_SjIAHEGpx1ggHUDTd1nYFB4_8d6JWaMIhQ9OTHWc-lmyvIGp8Xf66632CzJRD4KKIpK6G6yL2_EfcjXYSDHa9zM10AdeTWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2479db8c8d.mp4?token=b5NUGUFcwknfXWKcs04FgsSuep_LpSezJIU4y2xapqf4OuIfE5y9FI09cyLA0PkKIWuLmczxUS8nuQp_fsvEMM0fdbDpM6pU6RNFj2wdmRcQK-JZsxtMnDdSdNQv-U-Bmgrm8nm23zojB0BAHkfCh9FFyOvW1WvAaB4kXPr_q742RGJZKRk9K64r4jd-dNSWDkzVxMoKrNJwwWY-PZ4qr-2nHaXFtq-Y3TfSSy_Bqz6xWjoKKClZ2Z_SjIAHEGpx1ggHUDTd1nYFB4_8d6JWaMIhQ9OTHWc-lmyvIGp8Xf66632CzJRD4KKIpK6G6yL2_EfcjXYSDHa9zM10AdeTWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:
هر زمان که ما به ایران حمله کنیم، قیمت نفت کمی افزایش می‌یابد.مشکلی نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67534" target="_blank">📅 18:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67533">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72f85ab468.mp4?token=Hp-e8uze6Hk2BHakwRlAgXVWCtFqRoxF9PdIMo1-qBEd6JFjb7yXrSFVDZF5jce1BcJnKYS1itU8OknuihjCvts_aC1OgpVtpw4v1IR8fvvUJwLpZb5gttuMQ_6-ZbOWr2gvteQxLfGMcalVQjADHWO6kqpUNMoYRiIfgU346aAAOboh9r1MdxDVNBMQgIO4oMM1uCrmBzWAic1DwOjruQ8Or88aGZSK79tl3eRmQ8d4zwprDIlbLixuUTyRCeVOoHnMsi39f4iKYIjNwlJrkLOn8cGgigIDK3inqj22F9ZeHtLNkz-VZkK8medf2raybGjoEpHFg-jMGnQrO9nK5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72f85ab468.mp4?token=Hp-e8uze6Hk2BHakwRlAgXVWCtFqRoxF9PdIMo1-qBEd6JFjb7yXrSFVDZF5jce1BcJnKYS1itU8OknuihjCvts_aC1OgpVtpw4v1IR8fvvUJwLpZb5gttuMQ_6-ZbOWr2gvteQxLfGMcalVQjADHWO6kqpUNMoYRiIfgU346aAAOboh9r1MdxDVNBMQgIO4oMM1uCrmBzWAic1DwOjruQ8Or88aGZSK79tl3eRmQ8d4zwprDIlbLixuUTyRCeVOoHnMsi39f4iKYIjNwlJrkLOn8cGgigIDK3inqj22F9ZeHtLNkz-VZkK8medf2raybGjoEpHFg-jMGnQrO9nK5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره اورانیوم های غنی شده:
این مواد تا این حد در زیر زمین قرار دارند که هیچ‌کس به جز ما نمی‌تواند به آن‌ها دسترسی پیدا کند، زیرا ما تجهیزات لازم را داریم.
این مواد در اعماق زیر یک کوه قرار دارند و اکنون مشخص شده است که برای دسترسی به آن‌ها، به ماشین‌آلات بسیار بزرگ نیاز است که ما در اختیار داریم و هیچ کشور دیگری این تجهیزات را ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67533" target="_blank">📅 18:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67532">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0911dd57d8.mp4?token=KdSBRMk7bTP-uXoR6dxGAC-fnNpVZ3mVgnLJRNuT1rF1R6SZT9d95wH7-WKJPUrfFCsH8tuxZq-qF1iPxNN_l-cpNM5qY7p7pG0pxD9OWbGWCkADjxAh12E8O6d0wMUHKOUL0YBNbUwV-AzwYwyt2si3dwRfaFukqcz_0qacl4XJaI17PTQXWTU3pA8xLRQA4IUYNj2MJJGsSJ9mSCg32Ve7TkpNn60IPcYXJ_2jAJpvpFwOLqws2gLEGdxx2VqRG7oCsK564xpf08lM-IK8OACPNbtPUi6um8RTZISU4FrfW4S5OahT3--anCvsjKq7bwr8BEgd7e2p7LlwvAnc_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0911dd57d8.mp4?token=KdSBRMk7bTP-uXoR6dxGAC-fnNpVZ3mVgnLJRNuT1rF1R6SZT9d95wH7-WKJPUrfFCsH8tuxZq-qF1iPxNN_l-cpNM5qY7p7pG0pxD9OWbGWCkADjxAh12E8O6d0wMUHKOUL0YBNbUwV-AzwYwyt2si3dwRfaFukqcz_0qacl4XJaI17PTQXWTU3pA8xLRQA4IUYNj2MJJGsSJ9mSCg32Ve7TkpNn60IPcYXJ_2jAJpvpFwOLqws2gLEGdxx2VqRG7oCsK564xpf08lM-IK8OACPNbtPUi6um8RTZISU4FrfW4S5OahT3--anCvsjKq7bwr8BEgd7e2p7LlwvAnc_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
وزیر جنگ هگست:   «امشب، اگر نیاز باشد، با دستور شما آقای رئیس‌جمهور، حتی بیشتر و عمیق‌تر حمله خواهیم کرد، زیرا این همان پیامد است.»  @News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67532" target="_blank">📅 17:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67531">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db8877d1b1.mp4?token=bYtFQfw4fovZQwz8DTt1JNtn4Q9YQvKQPeizWcIzNABCiN_vHxAejAojj-2zKF6jzv-XqJ9wAdxgjz9LBVYcADpK26XG8bhpl5BlbNESOqkRCxTZt4REDbu6r9vbuOIhSd7Jiv6PtxIxM4dHHM3_ovD2AkP9u3qW_UHrbiNr6KKW1NKj-WEQNFHcH_sglzLf95dXHZQuzzSJTLo-m3x4NtIgNiaIP0g65WbrDen_FcmCzS6yBBcUGA8LBRUkIV8pfiUd_Ekpl448RDXJO8iEmkSplUF25dcoC7QVLxNs3HAZIVt4unAqsQYexDAx89ZFDpwv8pzAEkiF3Iv60Bl9OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db8877d1b1.mp4?token=bYtFQfw4fovZQwz8DTt1JNtn4Q9YQvKQPeizWcIzNABCiN_vHxAejAojj-2zKF6jzv-XqJ9wAdxgjz9LBVYcADpK26XG8bhpl5BlbNESOqkRCxTZt4REDbu6r9vbuOIhSd7Jiv6PtxIxM4dHHM3_ovD2AkP9u3qW_UHrbiNr6KKW1NKj-WEQNFHcH_sglzLf95dXHZQuzzSJTLo-m3x4NtIgNiaIP0g65WbrDen_FcmCzS6yBBcUGA8LBRUkIV8pfiUd_Ekpl448RDXJO8iEmkSplUF25dcoC7QVLxNs3HAZIVt4unAqsQYexDAx89ZFDpwv8pzAEkiF3Iv60Bl9OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
وزیر جنگ هگست:
«امشب، اگر نیاز باشد، با دستور شما آقای رئیس‌جمهور، حتی بیشتر و عمیق‌تر حمله خواهیم کرد، زیرا این همان پیامد است.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67531" target="_blank">📅 17:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67530">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووری
؛ ترامپ:
به ایران هشدار میدم، دیشب ضربات سختی رو بهشون زدیم، اما امشب قراره براشون سخت‌تر باشه و حسابی بهشون حمله میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67530" target="_blank">📅 17:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67529">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f1152c373.mp4?token=lKW5l4jx1AeuKijz-6cj-VCMqmUHuAYscW6r6lqfwBtwef-os5NuY7sxX1H0V2R85mxVGAWyh5wvoK6lreu2pdkQiNPX8cTfvbsNJvIkVWcmZqW8QSAfI7pmdfZzVJxLhoMfwdxR3lXDekA6nhw-zcTnqqKeLZhzyrBr7cDCdw9y2gb2wBz1bmL2TsQEwmq1jb1ABY1b99m4vTlOpMIgURyOAPMkTFv9hW_LE6w5YmMI5wxxcdIkYHPo8NWuKSHFNAwSfHBYui0pRR9-xXHXdCu_USqby7lqaGXtaueoF3zW4chk5Pu8VR6QrewLrF6zHmjlmY6NbrKZM5Wn-g0lkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f1152c373.mp4?token=lKW5l4jx1AeuKijz-6cj-VCMqmUHuAYscW6r6lqfwBtwef-os5NuY7sxX1H0V2R85mxVGAWyh5wvoK6lreu2pdkQiNPX8cTfvbsNJvIkVWcmZqW8QSAfI7pmdfZzVJxLhoMfwdxR3lXDekA6nhw-zcTnqqKeLZhzyrBr7cDCdw9y2gb2wBz1bmL2TsQEwmq1jb1ABY1b99m4vTlOpMIgURyOAPMkTFv9hW_LE6w5YmMI5wxxcdIkYHPo8NWuKSHFNAwSfHBYui0pRR9-xXHXdCu_USqby7lqaGXtaueoF3zW4chk5Pu8VR6QrewLrF6zHmjlmY6NbrKZM5Wn-g0lkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
آنها توافق کردند که هرگز سلاح هسته‌ای نخواهند داشت.
و سپس، آنها به بیرون می‌روند و می‌گویند که ما هرگز درباره این موضوع بحث نکردیم.
چه کسی باور خواهد کرد؟
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/67529" target="_blank">📅 17:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67528">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff51c5e950.mp4?token=TcM2Ns-vPHDWzf59zyZQkg-k3RkKEOhqQgBJRw7rg6HC8O1bc4mpuzRxXfGySAQTPQCMWKppCJd59bRi0BxN3-RVlmw7pc9XAdyiycMH99_SRb2jgqcWjAgxLjREnbHoRrDnGC6EAdolizF4tHsnjUfWtkl1OtHF505MAuBX9hxulTn0H70vv_y39fuh-rnCKWeqUb_UDNSx0tgcfMv3SeVY8Lg17WIP9qJ3avR1Jb8SyGe3M3oigGaq7LlsI2IJiPY9yxdJbjfktLcmcED1ihDWfkKb0Ls9WZanTg88c26wxQsQJbiidOwITWFi_3CnVF-RQZg27VABjojVAjhbDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff51c5e950.mp4?token=TcM2Ns-vPHDWzf59zyZQkg-k3RkKEOhqQgBJRw7rg6HC8O1bc4mpuzRxXfGySAQTPQCMWKppCJd59bRi0BxN3-RVlmw7pc9XAdyiycMH99_SRb2jgqcWjAgxLjREnbHoRrDnGC6EAdolizF4tHsnjUfWtkl1OtHF505MAuBX9hxulTn0H70vv_y39fuh-rnCKWeqUb_UDNSx0tgcfMv3SeVY8Lg17WIP9qJ3avR1Jb8SyGe3M3oigGaq7LlsI2IJiPY9yxdJbjfktLcmcED1ihDWfkKb0Ls9WZanTg88c26wxQsQJbiidOwITWFi_3CnVF-RQZg27VABjojVAjhbDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:
جمهوری اسلامی ژاپن دیشب به ناو هواپیمابر ما حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67528" target="_blank">📅 17:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67527">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac18509fa8.mp4?token=o6ZCAoD9iMFqj-pdbQeXLZhd6r85JcaN_th3EP_hzovQ-9ikcmjQ4Hk0fCuy9PXbaGL88ZsTe3zknMrJHc91rq5u4HApr8i8HY_ZLLEgpNThPA45BEM0fPdT6LSTk7advpwh9j6IkXdigdkk3OXwpBmsj8MQrvk8Ri2Riar56-NFPmAzD5ogA9egii33S-wSEpX2jup-LbgeuWT9c9DxxLnseHWSld2VydxrbqUoC4a8cWIc6Hc6kviDAUgfHKE7n751vO0c1i7QZcV3jyqFHybzjuR42A1BwU3o3wCclyp7Ggh7TbJYStXwN6yLu9qPuxjQNG45HnSedC0O9pIq0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac18509fa8.mp4?token=o6ZCAoD9iMFqj-pdbQeXLZhd6r85JcaN_th3EP_hzovQ-9ikcmjQ4Hk0fCuy9PXbaGL88ZsTe3zknMrJHc91rq5u4HApr8i8HY_ZLLEgpNThPA45BEM0fPdT6LSTk7advpwh9j6IkXdigdkk3OXwpBmsj8MQrvk8Ri2Riar56-NFPmAzD5ogA9egii33S-wSEpX2jup-LbgeuWT9c9DxxLnseHWSld2VydxrbqUoC4a8cWIc6Hc6kviDAUgfHKE7n751vO0c1i7QZcV3jyqFHybzjuR42A1BwU3o3wCclyp7Ggh7TbJYStXwN6yLu9qPuxjQNG45HnSedC0O9pIq0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ممکن است محاصره را دوباره اعمال کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67527" target="_blank">📅 17:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67526">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e08b208584.mp4?token=UoUHmt2veR1nvA-31qKxo60y8HhAm9eq_Q5Q5crIa4XrqXKDuKrbqfv4HW3yvQQSWNrc_2stiOXwPuresdCij_oaVaI3cal3gwnkhTi4yXLjG9ioXsNFvX2CG1XAYMkcUlf2oL_vvUDvxZQcVDi-m6YnE091Sg8STRVwNUhJ-YhPLCrLQieXq6oxF-YkRgYQxjjDsAO6jU7doWeLXv-pgD-dbLohrYdHSgwZsAK6RpIIefqmRZyN27HThsgMdM5LtQYjuFpFyBqvACOOwkqQ0jVX3XzbWEDRgfEHx3zdFx1c5Sn4Rkk9k1nrey7ptE7t44C53kx39CKVqa2u2A1xYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e08b208584.mp4?token=UoUHmt2veR1nvA-31qKxo60y8HhAm9eq_Q5Q5crIa4XrqXKDuKrbqfv4HW3yvQQSWNrc_2stiOXwPuresdCij_oaVaI3cal3gwnkhTi4yXLjG9ioXsNFvX2CG1XAYMkcUlf2oL_vvUDvxZQcVDi-m6YnE091Sg8STRVwNUhJ-YhPLCrLQieXq6oxF-YkRgYQxjjDsAO6jU7doWeLXv-pgD-dbLohrYdHSgwZsAK6RpIIefqmRZyN27HThsgMdM5LtQYjuFpFyBqvACOOwkqQ0jVX3XzbWEDRgfEHx3zdFx1c5Sn4Rkk9k1nrey7ptE7t44C53kx39CKVqa2u2A1xYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
آنها به ما گفتند: لطفا در مراسم خاکسپاری ما را نکشید. من گفتم که این کار را نخواهم کرد، و ما هیچ اقدامی انجام ندادیم.
و سپس آنها به سه کشتی حمله کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67526" target="_blank">📅 17:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67525">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e9aa8bf24.mp4?token=RCPRJv3HFY1ZZOMorZrRhY87ZnDLhiiazF2VshZlZ0HTMt50igw5ImZV_s3Y6fE5GXj0076RpDBCpr6zxBBgIEsOPsrfCkcOatnzkq40tgRc9WAIzCUHBU3FMWKED6ZwfY3Gu74AgNnxH6Y3Lz5P9GoaZwyYBZv8qQKDt16oQwSzRCqkRoBXUwPwVPdV7gSDmjDAQiFkCnKcTbZXWKH1WX1Q0VnPXmDr_8v_L4KZ7kn61Ui9M-G88QuBmbQR22mV0VOR-HnSNeOB74LquhiCXpoOc5bjd64Kim8Mf38uFaKgnlPC-amVy6pcpGxyI0ZI0ph6vBdC88fQ0RMgTpfFgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e9aa8bf24.mp4?token=RCPRJv3HFY1ZZOMorZrRhY87ZnDLhiiazF2VshZlZ0HTMt50igw5ImZV_s3Y6fE5GXj0076RpDBCpr6zxBBgIEsOPsrfCkcOatnzkq40tgRc9WAIzCUHBU3FMWKED6ZwfY3Gu74AgNnxH6Y3Lz5P9GoaZwyYBZv8qQKDt16oQwSzRCqkRoBXUwPwVPdV7gSDmjDAQiFkCnKcTbZXWKH1WX1Q0VnPXmDr_8v_L4KZ7kn61Ui9M-G88QuBmbQR22mV0VOR-HnSNeOB74LquhiCXpoOc5bjd64Kim8Mf38uFaKgnlPC-amVy6pcpGxyI0ZI0ph6vBdC88fQ0RMgTpfFgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ما شب گذشته به جزیره خارک حمله کردیم.
ممکن است کنترل جزیره خارک را به دست بگیریم. هیچ کاری در این مورد نمی‌توانند انجام دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67525" target="_blank">📅 17:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67524">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/204bddd9b7.mp4?token=NJ8kUfJolKLI4brkmkFW7pFE_XcDBI5IWQxl3GXfUh_isnudGLRwu9fdohOhXEdeD2rTmpaG7x-7wzmtDk9mpcq8Kab5RTvDeXqI2vfIlIQwmb7gojA6RFBjxgOWzs7GY6Ufz22FqBpkG8G8EXzicd42m222gI29ZTdPXQAVK1dzdRdYJqvHQvXu_3admmSwlLqVapsHAz-vq3a583ES8lPjKUnS71V8nrI591TeWnXc4GzJIJHrK9rwSaeJmrasWNCpxF_jJuIMtKWNGH5rHoknrcNAVK6Hi-PjH7oHDj7T6EDcHCufvZAwQeyDAl5RmO4prj7V50MzihATDS1i5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/204bddd9b7.mp4?token=NJ8kUfJolKLI4brkmkFW7pFE_XcDBI5IWQxl3GXfUh_isnudGLRwu9fdohOhXEdeD2rTmpaG7x-7wzmtDk9mpcq8Kab5RTvDeXqI2vfIlIQwmb7gojA6RFBjxgOWzs7GY6Ufz22FqBpkG8G8EXzicd42m222gI29ZTdPXQAVK1dzdRdYJqvHQvXu_3admmSwlLqVapsHAz-vq3a583ES8lPjKUnS71V8nrI591TeWnXc4GzJIJHrK9rwSaeJmrasWNCpxF_jJuIMtKWNGH5rHoknrcNAVK6Hi-PjH7oHDj7T6EDcHCufvZAwQeyDAl5RmO4prj7V50MzihATDS1i5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
گزارشگر: آیا امشب قصد دارید قایق‌های بیشتری از ایران را هدف قرار بدید؟
🔴
ترامپ: معمولاً این موضوع را با شما در میان نمی‌گذارم، اما می‌دانید؟ آن‌ها هیچ کاری نمی‌توانند در این مورد انجام دهند، بنابراین احتمالاً بله.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67524" target="_blank">📅 17:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67523">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f96f01d100.mp4?token=RgoNrE7-ItWaw2_R5Ff83eIz0t3Hy1Pd2koq3lhmAecNsVNROpYIlsrZd0Zwq_XiZs4WTB5zSujYIaH2KnCnC38wtcmx4qA3qYfRlTPbr_7mbEDIkRbN_GWE-Lk67M5lFlHIv2iaoGZNi-CDV-fFj6SIIZaKZEOoIki5BOrt7EPMLwsHU506xHYh6gmHbhs1sTqucBwd62AA0FWoqfGUqrslPLvTtpRHGeCn2ZLRUZlL4h7SPJ49aHUJdF035fbBkJroh6Tb9dajjjY6mrA2xWEF6ocR6r_FlDNpaZI_tuSKSm8AA-swCG--Gr7rf-VttX4B_Z9ZrI-mEbBlcEHg_A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f96f01d100.mp4?token=RgoNrE7-ItWaw2_R5Ff83eIz0t3Hy1Pd2koq3lhmAecNsVNROpYIlsrZd0Zwq_XiZs4WTB5zSujYIaH2KnCnC38wtcmx4qA3qYfRlTPbr_7mbEDIkRbN_GWE-Lk67M5lFlHIv2iaoGZNi-CDV-fFj6SIIZaKZEOoIki5BOrt7EPMLwsHU506xHYh6gmHbhs1sTqucBwd62AA0FWoqfGUqrslPLvTtpRHGeCn2ZLRUZlL4h7SPJ49aHUJdF035fbBkJroh6Tb9dajjjY6mrA2xWEF6ocR6r_FlDNpaZI_tuSKSm8AA-swCG--Gr7rf-VttX4B_Z9ZrI-mEbBlcEHg_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انگار یه نسخه پرمیوم از ایران هم وجود داره که فقط مخصوص پولداراست.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67523" target="_blank">📅 17:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67519">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mfz15MgjzGb5ymlJSZl0cwqnxPCXdhzTRshfaJUvZiMplG_u0BS-ip-c_VXtSxKPk2hpZy0HDZnIUBfKuVHZtFKeHmR9EyjWpLoFRxK3XXD7jmmWS-3Hiep9sO2HhTUze6gxWBRzP2oppC1rszaCFrnT0axtBydHdmHio6_z_3Lo3xkTu3Lk7iUBu838Ohz3xUH9FwuyDlIgpL09SBsdtNB2gZ_b3Yi4ipocatgRi3AvuyOIxsCBsfslgyddGZ8ONT4ah1hnCMVWQfxfif3_LLXifWk_YyNs6cdUD6Q5oFhTKams89kIDU85dD1Y1lwst_hQCQMxMeyBLV7MtGiYzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41735c920b.mp4?token=dArQ-Q9ojJWOHDZtoDXGe__Z_Fd7XYEJwxpWp2II_v3CJTlXxNUdBWQiXvWs90kZxVIDyIfGeV8Zej3E5rap_SA2jX5d4fGYg8jHndCc6UHzWnkvvcgy8eOfaeJkL49fMwWB9OgAtm-8QSiCUmSQ0yQRKn7muNt3lEQ9Zif1yUYmddn6w1L0r4wUog1NRX5e6GcSCkPUjY85FrF1x0Ij7APtd_Ov-t7FkOtSl9K6AkPhearIBGmKwye6BRbUMS6HBMij4ERTF7Jh9cFyHEGJ44o_eDn4CkgFQ00ARPLH4eGphsoQKNxoe1tXXLiWcCmKezKyai_Klqc25B8_IDaAjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41735c920b.mp4?token=dArQ-Q9ojJWOHDZtoDXGe__Z_Fd7XYEJwxpWp2II_v3CJTlXxNUdBWQiXvWs90kZxVIDyIfGeV8Zej3E5rap_SA2jX5d4fGYg8jHndCc6UHzWnkvvcgy8eOfaeJkL49fMwWB9OgAtm-8QSiCUmSQ0yQRKn7muNt3lEQ9Zif1yUYmddn6w1L0r4wUog1NRX5e6GcSCkPUjY85FrF1x0Ij7APtd_Ov-t7FkOtSl9K6AkPhearIBGmKwye6BRbUMS6HBMij4ERTF7Jh9cFyHEGJ44o_eDn4CkgFQ00ARPLH4eGphsoQKNxoe1tXXLiWcCmKezKyai_Klqc25B8_IDaAjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حملات موشکی شبانه روسیه به اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/67519" target="_blank">📅 16:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67518">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c_fzl4NCcDIc0QpK0BxVSz93YUpE9ggkzMLVpDUM9ReIbXidx08jr_Dk0spD6sSkANRq7hG8wn1rVkA36nXddde47XWlIdJ1Ob68cUDRkhzRXKwC36b2Sh_cCyTAbhU4-jr0n1O3G0G1QmckNnsL0C_H1iY9PIIOqpu9RbfB_cG_U9gl9YKNG_H2-l2qMto0Is_M4vfUam5ZVHJeHR8cc8GR_hO4fZEta7qW9z7WN5mXU6rQm-hiErQhmw6ot-FFqTxfvHb_WFNr17GlSL050cGJt2uegew8uOK-CmMnjawJPVOMhL7W4y-fldAWZIxhnmon0HIEb2Z2N0j2hFKhKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری هادی چوپان
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67518" target="_blank">📅 15:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67515">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XwdlH35WnJimMAaHpydFO_EmIklIZj6zp0DQfPCGltpyQNzNzWmayKUrvUJ7c1bu23QJ_4XwtZ8g0b8woaX4rgusBkFgIVfiay9AdjH_3vKOV5I6EuEK0dU7LXO_2NEQLcXZmerbW3poe2l88lkcxgwroSiqVU05w7-12v5-3lJMlzt0DShtyIGYddLrq0BPGtvOrxixADMVy_jDU1ISX4SqLh04Wc_F3XBr0plbQMQnfgyggvGbSy465WCBxbAMzasOa0Xw2H9BUd8ZbyxEMdtY6sKjtinDOC5vCsJP7KJ3y2yDPb66cj53GIyslgdVriI4BTdffhOH6s4AgOzLDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WKuuigbqGpjOp9CF2zvdn19qBAun6gXMhQmpPjgoBQjisSiNNt8FIhkklIpqEoN1EAaKL5_XK4V8_jFNWvzPVcWnOurFnlqgnZ1ZnZ5U-jHrxLGBzi6TCtOkWGDnZsYZdXjsvQH33mmGjM9Yc9PXI1XQX-G8LcqAVAnPkO9gdydf-A608LGc1XW1823Xj-ccIfnhPxzoLHTBfdgK2jpTmdOap0OtBzQr_-26oazU7_kdNsEn__14yF6be0deoLwVKiwb7oUMM8o9WF8lIBQ7HlQC_pbG67QlCVroNAL8B1ukjb19F-4vYdrpha5A3mEyguhd9bLni7V9XJRR6uVaNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2e58f00c0.mp4?token=eaIftD7Q6gu-AoJj34a-TcZgRyxDIp34qw76JPdI9EhyFRssvcemixc7QdqMntsGRPL1RqdHq5hj42jJ7oWE1Im1W9DGyVthYyUpoCim8-Let5OvJcuH8oix0h7n4JpkSSOtoYjZzCCCRV6A5PbjzjHv0u30ZIY_LA-FshciZKkZCD5fnfuHO-pRaC1LEYq3AalvtVWpH9hmyXfrQbhRDucLvmxBkuJSUublU3Wx_-0PmwSXWY6Oa1vo0pJiG-rJLQnqz-XGDcatoxzePyiSaoE2hOGAulpFRZVtM1uYtn-Jrbjd2CmEoZisbAxM1bfwxAAzFGfb-RBsUZl1uOHPv4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2e58f00c0.mp4?token=eaIftD7Q6gu-AoJj34a-TcZgRyxDIp34qw76JPdI9EhyFRssvcemixc7QdqMntsGRPL1RqdHq5hj42jJ7oWE1Im1W9DGyVthYyUpoCim8-Let5OvJcuH8oix0h7n4JpkSSOtoYjZzCCCRV6A5PbjzjHv0u30ZIY_LA-FshciZKkZCD5fnfuHO-pRaC1LEYq3AalvtVWpH9hmyXfrQbhRDucLvmxBkuJSUublU3Wx_-0PmwSXWY6Oa1vo0pJiG-rJLQnqz-XGDcatoxzePyiSaoE2hOGAulpFRZVtM1uYtn-Jrbjd2CmEoZisbAxM1bfwxAAzFGfb-RBsUZl1uOHPv4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
با اینکه تو ایران با سنگ و چماق میفتن دنبال عباس و میگن مرگ بر سازشگر ولی تو عراق اینجور نیست!
مردم عراق انقدر عراقچی رو دوست دارن که اون رو تَبرک میدونن و خودشون رو بهش می‌مالن تا حاجت بگیرن!
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67515" target="_blank">📅 15:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67512">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZEoRnu0z-mjWbdv1M-2auWqRkyWqqBKSnl9OFjIOWKSiclWgKd0o-haaUtKnLcSWjdyS9FUq_XqfrqvIsXvR0xCpm_sNIK7cpSBOQMQmY3LwJloQgdsuVO3ggao5TPEESPOI0qb6v91CPGBv1j_xwz7h9LDV9pHLEdXBdRMP7o91Ndo39aPVJg5j4-ErYRxr7B5d5xagE5YDdYSiYTM76SJC-zSbLpPCgKbkV8UOEfh4tLOU7wPqWrQPpVZr1iBL7y-Jb3pPtASycFNqoTcENQwrgLSWwJhYAFFhTclsBJgHaDCha9S6lHTao_hjN2-kkmO7Mx3XkPLL9UOIPotkng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YuE8kcucSsobQbnZ4sdJsINlu5pp1J78ZjIgvbGpvrjc2QlMfbpnVbp5EvPTH2kHHYZvp8QR1Y23RlLjTWCOHTWfv8mWD2zeKZpjg8SFMuf2yaSZBvZgFfZrBQiRqQQQwqUV19DNN6WaJ1V9GJkWtZ_hwTzzA32XhTGeDnsDlmd3Bp9vYahrY-gNU1LVDxliOBCm7ncRaUrw9pytoQMWbOR61HHV5rxvO0Qt-wHfS82xBNbylL6-n-rbjrqteyVwXKX0CODAOCPdg-_m3D8i95is4XvsLmTBxiDE8cuHVRBaWGvOZRRRrwAkhjEqLkOGl2LbOzBLow0Zy7YsW3jBQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hi8Xeb7BGty50k5lNjrLM8je8E0rYaevmopVcUNilOsnwDbTvUPVnDSsBQ6mm7Y0ay6dJI17eFY2Bi-qBxJrSWhnyYOWGa3y32aShvGGym30PjbO58y9qFWxnECCTjvkeU2-QXnkoKfDmUXltmxjDY9Q6HMYIgJ9qY_7K9RLpUqEmU2mgWgT-UOZe-zeXMtxs6vGhSpyEfEb6PDSft8t05NzL0B9w1W0B_0LFfKpHRrmiXCRpMRPtFW2Q0-yUy0SriythFoXY_6bfwbNw3o4tYkvduw_jVGHEuF5_S-t5ktBDPeSkcHGhuc93xIqOrRnuGHQ3j_5OwaeltO_TW_IXw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
خبرگزاری تسنیم اعلام کرد یک پهپاد تهاجمی MQ-9 آمریکا در آسمان بوشهر سرنگون شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67512" target="_blank">📅 14:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67511">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/763cc26dcd.mp4?token=JN2RxP2POpSpo2bPzqGoczbiotzy8SvwEWXI6CsXYHmx2Uf83ldO9ADPCqwsawsT2s9pp88Zwj9ljTnLfxnd5A_aoUcjBbadOtWYGywOQ5O34IRRSklP7liB3QOcesev0it08B41cJAlcP90vZnUMCSCA5d12IcMME9e6-Blg02RKmSar9rMP8bpp10lOzHe_D_d_7f_WtADkweS8cWIaz0XG1qx4CfweH2_sccYnzCIQ2Q1yT2p1K-V_kmw6Tvu30avctAXrYRjkGp4gLFjVpz-hVKsqe-lqjTsjQw94ebEA2zhrCb7SrUjbmxiorZLFyldjLL9zW2kbpIPIgQLsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/763cc26dcd.mp4?token=JN2RxP2POpSpo2bPzqGoczbiotzy8SvwEWXI6CsXYHmx2Uf83ldO9ADPCqwsawsT2s9pp88Zwj9ljTnLfxnd5A_aoUcjBbadOtWYGywOQ5O34IRRSklP7liB3QOcesev0it08B41cJAlcP90vZnUMCSCA5d12IcMME9e6-Blg02RKmSar9rMP8bpp10lOzHe_D_d_7f_WtADkweS8cWIaz0XG1qx4CfweH2_sccYnzCIQ2Q1yT2p1K-V_kmw6Tvu30avctAXrYRjkGp4gLFjVpz-hVKsqe-lqjTsjQw94ebEA2zhrCb7SrUjbmxiorZLFyldjLL9zW2kbpIPIgQLsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
احمدی نژاد : بابا داره بهتون فحش میده،یه مرد بین شما پیدا نمیشه پاشه حداقل بگه خودتی؟!
+ترامپ امروز به مسئولین جمهوری اسلامی گفت آشغال،پست فطرت،کثیف،تومور سرطانی، شرور،بی‌ کفایت،بی ارزش،بیمار،روانی و حقه باز
😂
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/67511" target="_blank">📅 13:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67510">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
رسانه های عبری:
ارتش اسرائیل جلسه‌ای با فرماندهی مرکزی آمریکا برگزار کرد، به منظور آمادگی برای از سرگیری جنگ.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67510" target="_blank">📅 13:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67509">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbjxAb4K3NmzOwRAU_Ewp3e91G7Ku0GoUGcRDEe4ZZYn2im51xGmuAQ1J9OJFssNioTiF8HravSUawirf5K5mU_JdkcQ3NJEY4AY1skevQJvJY4CD_9q-xNoS4Zivp3kmdM9um0wohRuJok0mgyFmZUXf_iGZSOlWoQqtFFV3e8RBT2IjSltQ5UUxN5TXo1sNLzlv1h92yQe0gLmY1al1eVa9mdTXWeI3OHaylqPwjlyevS2mDjAMqE1axEMQGXGWz_a9TqmPht03dj1NhiefIc3J7s2TRA7tSweRbYrbBkDCqbbQpdjk0SmBIEn-GZUJRh4g66U-UqQ7hjQI_sHgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
پزشکیان:
رفتار دولت ایالات متحده به عنوان میزبان جام جهانی، همان سیاست خارجی همیشگی آن را نشان می‌دهد: زیر پا گذاشتن قوانین، زورگویی در برابر رقبا، ایجاد موانع و تقلب. این همان روشی است که آن‌ها دنبال می‌کنند. ایران چنین بازی‌هایی را رد می‌کند. ما به طور قاطع از حقوق خود دفاع می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67509" target="_blank">📅 12:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67508">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-sHzm-3uJ92ikJ_AuWLvpAbnGSmkdqP9aX7v0tLRdcgcr-P16HseEHARQyEQuDEt3JLqWCZwoS7kG5tXyMcyPOeRLt2xZvgH-eB-nhtukFPc-xNPVaAKVzl20dC4URBbw9EH5N9F-fEFXWUm7volwtHNGFm2Y5Z-3HB2XKDFVZIXwXAE8Z4bGpSMR3MsqfuUHI9wz17oC6UFyExmYmoFGKwg17gakrG8vDNND9hadD7x69sENkAXx2M00fAIN5mY00I451cGNiSp1Se31ZPYXnAXUajp7e3IBFNnCPEC3Jd0fzUoQMOQWjhBdhj4fXpPWyMjHZSikQ3iOHWwsGR6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آمیت سگال:
پیت هگست، سفر برنامه ریزی شده خود به اسرائیل را لغو کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67508" target="_blank">📅 12:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67507">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:
«ما دیشب به آن افراد بسیار خطرناکِ وابسته به ایران، با قدرتی بسیار زیاد حمله کردیم... یک مشکلی در آن‌ها هست. ما می‌گوییم: "بروید مراسم عزاداری‌تان را برگزار کنید"، اما آن‌ها به‌جای این کار، دیروز شروع کردند به شلیک موشک به سمت کشتی‌ها. بنابراین دیشب خیلی سخت به آن‌ها ضربه زدیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/67507" target="_blank">📅 12:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67506">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb70977fa5.mp4?token=J1Gb0Fpjv7U08n6ggwDZxMXkocf8wZKg-e70Y2p1QTGZhshFXj3TsvWSFEahWYEzzCJ6RbajPqRrX5dCIzZynZzFcXbzFVell_kWhn24ezTKqPFDibGJfSMtnA0RA9CQUa6qg82EWjeD1v6pckMLILv4rUudsCeRiWTFrXHiMJss9LLpMGhRL_DlLxfrgcXsJrvOteWKqHYttO9kc9U9aw1y_EAWvrHUG2Ie4xw4mO5PvyiRxqWDCOVYprZVPjbwZ27Mu9bytoDBKqliSpbvY5pEbUGLGu_ke5uAGWrWlTLJN9ZpxtWps00qVka80s0edUXD3WGOKXsKI5sw1YIvZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb70977fa5.mp4?token=J1Gb0Fpjv7U08n6ggwDZxMXkocf8wZKg-e70Y2p1QTGZhshFXj3TsvWSFEahWYEzzCJ6RbajPqRrX5dCIzZynZzFcXbzFVell_kWhn24ezTKqPFDibGJfSMtnA0RA9CQUa6qg82EWjeD1v6pckMLILv4rUudsCeRiWTFrXHiMJss9LLpMGhRL_DlLxfrgcXsJrvOteWKqHYttO9kc9U9aw1y_EAWvrHUG2Ie4xw4mO5PvyiRxqWDCOVYprZVPjbwZ27Mu9bytoDBKqliSpbvY5pEbUGLGu_ke5uAGWrWlTLJN9ZpxtWps00qVka80s0edUXD3WGOKXsKI5sw1YIvZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره مقامات جمهوری اسلامی:
آنها دروغگو هستند. ما یک توافق می‌ کنیم. همه موافق هستند. هیچ سلاح هسته‌ای. ما یک توافق می‌ کنیم.
آنها به بیرون می‌ روند، با رسانه‌ها صحبت می‌ کنند و می‌ گویند که ما حتی درباره این موضوع صحبت نکرده‌ایم.
مشکلی در وجودشان وجود دارد. آنها دیوانه هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/67506" target="_blank">📅 12:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67505">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5877eb817c.mp4?token=oF0Elcf366OotuuS5XynhV5qinE1eMNsCpbqAyzVIIVTQfgd_wOjkfT8TBJOEhMHWprr37C9JeM_SE8ewN_akvzd4b5o_t5dvdDVqbe7Uq82zYYb9FfexP0yhLAcTjul7JiJtBKnZ6x64gQ1-VJqdg6c_--2mO1cKemUcZ-5dpB8no2WAGf2YI0tGP878ItOuVh0SuK6AKEC8k-c-8-KXrgIDV6D_jMuAmP-r1lv_jrYmLJfr8ZWnUledA_35FadiZdtowYwkvYsqs1Psl-q780CTC8KzZD2Lv19coeespjB2bkRMdk4Byr0OTjvxQ4bBQK2fBOzMzwaM8n5_Y98hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5877eb817c.mp4?token=oF0Elcf366OotuuS5XynhV5qinE1eMNsCpbqAyzVIIVTQfgd_wOjkfT8TBJOEhMHWprr37C9JeM_SE8ewN_akvzd4b5o_t5dvdDVqbe7Uq82zYYb9FfexP0yhLAcTjul7JiJtBKnZ6x64gQ1-VJqdg6c_--2mO1cKemUcZ-5dpB8no2WAGf2YI0tGP878ItOuVh0SuK6AKEC8k-c-8-KXrgIDV6D_jMuAmP-r1lv_jrYmLJfr8ZWnUledA_35FadiZdtowYwkvYsqs1Psl-q780CTC8KzZD2Lv19coeespjB2bkRMdk4Byr0OTjvxQ4bBQK2fBOzMzwaM8n5_Y98hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:
به نظر من، ایرانی‌ها ناکارآمد هستند.
اگر کارآمد بودند، ۴۷ سال پیش یک توافق انجام می‌دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67505" target="_blank">📅 12:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67504">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48d7e6a047.mp4?token=o74X0KCT_7ZkIUPPNamdyEGccPKy472ySoGCEFvnL_ZaDWtW2xeNuomg7y5kmUrzZkxgRnFVSKK6IZeHgEJjmSxRpvqqKwKEf8lVvb6l0Mq_uw2m8V0pdFPZ2i1qItpas-4Ka_Wlwqj8u8Z_QS1c5lrdJaNVoKYSEiKWrWFvFx_lwppzk0mrKXGPbbciJTWIn_yR1psDfD4V-y8iLMucf3O0WhuP9VdOucl7iGyO6J8TQU_9c4rGworLXs_KDqZwHDyaNFZHn4oyhm6azMv3-5uuyt-SVt54nDAwW2N7On75mAFxgaDohfmFhUMyiT-JgJ37hW8Dr3UeVVv2ZcIsug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48d7e6a047.mp4?token=o74X0KCT_7ZkIUPPNamdyEGccPKy472ySoGCEFvnL_ZaDWtW2xeNuomg7y5kmUrzZkxgRnFVSKK6IZeHgEJjmSxRpvqqKwKEf8lVvb6l0Mq_uw2m8V0pdFPZ2i1qItpas-4Ka_Wlwqj8u8Z_QS1c5lrdJaNVoKYSEiKWrWFvFx_lwppzk0mrKXGPbbciJTWIn_yR1psDfD4V-y8iLMucf3O0WhuP9VdOucl7iGyO6J8TQU_9c4rGworLXs_KDqZwHDyaNFZHn4oyhm6azMv3-5uuyt-SVt54nDAwW2N7On75mAFxgaDohfmFhUMyiT-JgJ37hW8Dr3UeVVv2ZcIsug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ درباره ایران:
من در تمام لیست‌های آن‌ها قرار دارم. و تا به حال، فکر می‌کنم کمی خوش‌شانس بوده‌ام، اما شاید این خوش‌شانسی برای مدت زیادی ادامه نیابد.
چون این‌گونه است که مسائل پیش می‌روند، اما ما افراد بسیار خوبی داریم.
اما این‌ها افراد شرور و بیمار هستند، و ما باید از شر این "سرطان" خلاص شویم. این "سرطان". و شما می‌دانید چه باید کرد؟ باید "سرطان" را در مراحل اولیه از بین برد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67504" target="_blank">📅 12:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67503">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ در پاسخ به سوال یک خبرنگار پیرامون این موضوع که آیا آتش‌بس و توافهم موقت تمام شده یا نه، پاسخ داد:  فکر می‌کنم تمام شده، دیگر نمی‌خواهم با آنها سر و کار داشته باشم، آن‌ها پَست و بیمار هستند، رهبری‌شان دست آدم‌های بیمار است و اگر سلاح هسته‌ای داشته…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67503" target="_blank">📅 12:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67502">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/385c5453ef.mp4?token=Ki4ScAC-M58U-jYMZc6dUg0Mm3lTxNF0pfzEsAPy_DbGZdr5PNtFgzW0n22aL9bDODFNi3LerZCbRt7jI4EZC81pjS3BbSi6jmMggXlTiLp4MeTB8dhsPW01P5lovhr2dBvD3ioQXehmb35tBRSX9s9cOkLQ-3YHDhAAGQcj2p-9Vg9FtXWfd1LT4wLZMFftei7rGPLivI0hIVrWMnsaUl9rP7fQVZ_LoJkfh2rYH771WmFfDwta_ai40ORF-4X8nuINL0zHhrbvjSHbMR4OCnkBuE1rBqgBD3OoOybhdOkBQVxl2RX8BrA7mqerJ6LB6A83qr-YPyFerR9FZih7Coi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/385c5453ef.mp4?token=Ki4ScAC-M58U-jYMZc6dUg0Mm3lTxNF0pfzEsAPy_DbGZdr5PNtFgzW0n22aL9bDODFNi3LerZCbRt7jI4EZC81pjS3BbSi6jmMggXlTiLp4MeTB8dhsPW01P5lovhr2dBvD3ioQXehmb35tBRSX9s9cOkLQ-3YHDhAAGQcj2p-9Vg9FtXWfd1LT4wLZMFftei7rGPLivI0hIVrWMnsaUl9rP7fQVZ_LoJkfh2rYH771WmFfDwta_ai40ORF-4X8nuINL0zHhrbvjSHbMR4OCnkBuE1rBqgBD3OoOybhdOkBQVxl2RX8BrA7mqerJ6LB6A83qr-YPyFerR9FZih7Coi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ در پاسخ به سوال یک خبرنگار پیرامون این موضوع که آیا آتش‌بس و توافهم موقت تمام شده یا نه، پاسخ داد:
فکر می‌کنم تمام شده، دیگر نمی‌خواهم با آنها سر و کار داشته باشم، آن‌ها پَست و بیمار هستند، رهبری‌شان دست آدم‌های بیمار است و اگر سلاح هسته‌ای داشته باشند از آن استفاده خواهند کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67502" target="_blank">📅 12:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67501">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_SlYyeGVaXaltKOd4tDLDzlm0bEM-wIhuCYkyg5By2zdy-mgofelvkkeXuaLrcj9pc2xdpebLpM5BiE26fOHkaQ-4wjmcayoxQoRyOUJGOOcCfqYMMwY4FC802gjaZ763UNyQdahnO4DqNlM9UrTsDcmMZ5fiKnS8QjTqekPDf5vRlA74dSRrscUlGaoyVdbJz2rxWLfe4Yf_BZ8vtVHvO9v5bLCQaXiFX1n3YK44xCDef_U2CnO6898bqc9-ev6ZYfPA2qWQBHwIHYqQleNbJ2HfO5iWpJY6tZ07dD3am6m_2nrskw3pAuJU29dZKnyBMjwdMqAYJJOM_64oTAuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعد از حرف‌های ترامپ، قیمت نفت ۵ درصد افزایش پیدا کرد و به بشکه‌ای ۷۷.۴۰ دلار رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67501" target="_blank">📅 12:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67500">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b7bb2fcec.mp4?token=amfY3yAppy8iGpoqx8JuucZP34t5GUZxDDKQTG0DI58MbOyXaKAnkzHNDUyfaIVndo08QNyvqIzOdYDiUs-NNEH9CV9A7L59ObrFApSZuZqY6CZcYGb0KykJqZYvaFTbIyUdJDdSb4m3mK8XXcSsEfYTKZEfClBmxFTXMz43_mA4zxBB80NBhM8IJHii9PWNBl3RYZ_eaIjEuD0xUG_TSRxwkOVSee8jjvadiR4CJb8xIxxgrl0ImuyYriAtV9rF0meAm4ISfhaRYpTmt7TIu7-3qbJI3fOj71sqlQq73G94YjrHTcXs6uzLyNxPt3PwutrpTfl4ueuCHcRoJOZZRTP1jKdHMJLZvaZMJjzH4n-2_cUqnOeyG5Y449ap0JwE2fMBrLggcNLbSMvLTQj10-ammBAc9p9sw46uWWCCSGduV05mOAWaEAx6Y-LjD6FV9hvR3YSsghrX3rtQckDjQrcn4WKffbB5ES7qlNwO2KcKe-rknqRU-d-rLlt0BwbZ6L35bp5SGzasqJJAhecSK4e5oIp5LCpPvrXHcwJnuxN0NPK-vQ7e0LQzsMCSa4_gf98ePUyocQPz4YZU4iwmq73k-HC_4OT2QWK_MYZ5-JzCG-6SEqtrZSnp6_2Kd8BkKTeEL4q4WV99e3G_ACSQp_1rTbhP4KbzqR1HLDXlmEM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b7bb2fcec.mp4?token=amfY3yAppy8iGpoqx8JuucZP34t5GUZxDDKQTG0DI58MbOyXaKAnkzHNDUyfaIVndo08QNyvqIzOdYDiUs-NNEH9CV9A7L59ObrFApSZuZqY6CZcYGb0KykJqZYvaFTbIyUdJDdSb4m3mK8XXcSsEfYTKZEfClBmxFTXMz43_mA4zxBB80NBhM8IJHii9PWNBl3RYZ_eaIjEuD0xUG_TSRxwkOVSee8jjvadiR4CJb8xIxxgrl0ImuyYriAtV9rF0meAm4ISfhaRYpTmt7TIu7-3qbJI3fOj71sqlQq73G94YjrHTcXs6uzLyNxPt3PwutrpTfl4ueuCHcRoJOZZRTP1jKdHMJLZvaZMJjzH4n-2_cUqnOeyG5Y449ap0JwE2fMBrLggcNLbSMvLTQj10-ammBAc9p9sw46uWWCCSGduV05mOAWaEAx6Y-LjD6FV9hvR3YSsghrX3rtQckDjQrcn4WKffbB5ES7qlNwO2KcKe-rknqRU-d-rLlt0BwbZ6L35bp5SGzasqJJAhecSK4e5oIp5LCpPvrXHcwJnuxN0NPK-vQ7e0LQzsMCSa4_gf98ePUyocQPz4YZU4iwmq73k-HC_4OT2QWK_MYZ5-JzCG-6SEqtrZSnp6_2Kd8BkKTeEL4q4WV99e3G_ACSQp_1rTbhP4KbzqR1HLDXlmEM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره رهبران ایران :
«آن‌ها دروغ‌گو، متقلب و بیمار هستند. به مردم خودشان آسیب زده‌اند. تا امروز ۵۴ هزار نفر از معترضان را کشته‌اند.
می‌دانید بعضی‌ها می‌پرسند چرا مردم حکومت را سرنگون نمی‌کنند؟ چون دیگر زنده نیستند؛ آن‌ها را کشته‌اند.
مردم سلاحی ندارند، اما طرف مقابل مسلسل دارد و آن‌ها را به گلوله می‌بندد. رسانه‌ها هم این را پوشش نمی‌دهند.
اگر مذاکره‌کنندگان فوق‌العاده ما بخواهند، بگذارید به گفت‌وگو ادامه دهند؛ اما من امیدی به نتیجه نمی‌بینم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67500" target="_blank">📅 12:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67499">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ :
سران ایران یه مشت آدم کثیفن. اصلاً ازشون خوشم نمیاد. کلی وقتمون رو باهاشون هدر دادیم. بی‌عرضه و ناتوانن. بهتره فقط کار خودمون رو انجام بدیم.
اونا می‌خوان رهبر آمریکا، یعنی من رو ترور کنن. سال‌هاست که من نفر اول لیستشونم.
باید سرطان رو از همون اول ریشه‌کن کرد. من این‌طوری به قضیه نگاه می‌کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67499" target="_blank">📅 11:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67498">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ :
من دیگر نمی‌خواهم با ایران سروکار داشته باشم. افرادی بیمار بر آن حکومت می‌کنند و از نظر من، این پرونده دیگر تمام شده است.
«از نظر من، تفاهم‌نامه تمام شده است. دیگر نمی‌خواهم با آنها معامله کنم. و اگر سلاح هسته‌ای دارند... دروغگو هستند... به نظر من، ادامه مذاکره با آنها اتلاف وقت است.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67498" target="_blank">📅 11:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67497">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ایرانی‌ها رهبران آمریکایی، از جمله خود من را هدف قرار دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67497" target="_blank">📅 11:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67496">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
پرزیدنت ترامپ:
این‌ها گروهی از بدترین افراد هستند، من آن‌ها را دوست ندارم. ما وقت زیادی را با آن‌ها تلف کردیم. آن‌ها اصلاً نمی‌دانند چه می‌کنند.
آن‌ها مثل سرطان هستند و باید این تومور را هرچه از بین برد. این احساسی است که امروز دارم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67496" target="_blank">📅 11:54 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
