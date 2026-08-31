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
<img src="https://cdn4.telesco.pe/file/DSDJzEdDq7NjvIDWDNOAuDsPTeZKzsa57xijsaO6jKbsnylZXUjhp0VrgEHlz3I515TRpb-qDBNb6-wfPrXOIpM1GE-vixDvuLDAqgLb-hXk0dwPX_vORQ2NY_1w7IJsbPzF7PiBJvdf5qeJ5Hl-wfIP1IyTZTJpELFi2JyZQ3yCcJZXfW5KjycseiySCUPr8Y-ze_Ar-UCk42_kh8ClffAYplhDJmZysUH7rOj13Gz5UAKomzwcjahH-Zf1zJEFBalkKYcwJ5nXARyR3mYQc2STdV99tm1xnmyAimEbtgNhEZainSRJM-iqEyyketx3uHUhgJ8q1xBot3xi4LENeA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-09 12:35:56</div>
<hr>

<div class="tg-post" id="msg-459172">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qEzzShkEGta20qkBc5GCkHB0G6HOhVNU9KIqanrLiOB9MtUYIOYKJZG8Asp6wZDm-ZQEQYst8AfgfKxnGCjLvDs5W1H9HrcVIYlbTW1UWZoU0NyPjGfL1Nu1mLNZWOwlWz8_RRD45c0zZcGCI5Wf6uVRdHde9B8FRvwTXpwiaDSuqmQzlPBYF2qIwF4pFE1ocSmVpBJvjAnILhERPamXFCvsON5F3Hiaw-Ea4-9B-clbn_jpPc8kiPQeqZqf90eQBw54oXHOwADZpEMQOJ76lZgIwSFc71BosHGkc16ClcPLFCLyU5WQbsBAcFSfBhmx3Qqa16d8J8p8Nfp9RiiAvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اژه‌ای: قوه‌قضائیه برای مجازات عناصری که بخواهند امنیت کشور را مخدوش کنند، قاطع‌تر از همیشه است
🔹
تحکیم امنیت و مقابلهٔ قاطع با عناصر ضدامنیتی، جزو مقولاتی است که آحاد مردم و مسئولان ما، در باب آن اتفاق‌نظر دارند.
🔹
همهٔ مردم و مسئولان یکصدا و متحد هستند که باید از اقتصاد و سرمایه‌گذاری مولد حمایت کرد و موانع تولید و مشکلات معیشتی را برطرف کرد. در این زمینه‌ها هیچ اختلافی وجود ندارد.
@Farsna</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/farsna/459172" target="_blank">📅 12:30 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459171">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/slPknqvWH9msPAn4pNPo7LIXM4f06T-iBmoSAUeHGMbohFhF-XjxdaP8izS9V19nrhKw-KLp0fhN1xQvVvMY2Du5H9oCPr1F70AlHUXfU78aL6F0nlr9ISSERi29VG6DUFByIzFjWz4NCzIGlrXOE1p8fjyXA2hi01hH2AA9QJUZCuJLEyJd4s-fyRhSrBBtpQLiOO6Ev5WyCif2gmsULpjAfgwY25McDM9ZCvjHBIHHM1Md7mmOcx7RZGMG8BXWmO0-EzKhwwCKeNxtYx0IDaB-KdNWOS0SwkBksv155aV5xQwKg6_nKbDaMXNLHJJZnRVQ5qb7UHryfdM4Z_s54w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
قرقیزی‌ها با سوغاتی‌ محلی به استقبال پزشکیان رفتند  @Farsna</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/farsna/459171" target="_blank">📅 12:25 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459170">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac497cf83f.mov?token=HawaPvQyiyLC1rxGxws68YFXInjNbO_xRJx2OepWeGgLkqA9D_XBUwzU27yzy8N-wpE4dAfs5AQjd8J5eThxanYGlCGq4YH8LfHsi2ykwETsVmboNSfICPIEE6WBbzMnBcApmqQiBcJ_ZEQz2qfm-61DQ1TnwVq8F92Q7LIEfSVmO9mTpKwCLiMDLkginNUy1Up7gWDjeuDreYQgBBX8gnSPSWWZylqeT7ttd8D8htg1yPzJCOnU77mA3IOmjd16YwfiCYiwpGpG6ICSU1E4e_XR8dKeHonbtmSz2OLx80NRvseFeH6c52VZEUV7R642dPygxtB5aDr3Fzj0j1R68A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac497cf83f.mov?token=HawaPvQyiyLC1rxGxws68YFXInjNbO_xRJx2OepWeGgLkqA9D_XBUwzU27yzy8N-wpE4dAfs5AQjd8J5eThxanYGlCGq4YH8LfHsi2ykwETsVmboNSfICPIEE6WBbzMnBcApmqQiBcJ_ZEQz2qfm-61DQ1TnwVq8F92Q7LIEfSVmO9mTpKwCLiMDLkginNUy1Up7gWDjeuDreYQgBBX8gnSPSWWZylqeT7ttd8D8htg1yPzJCOnU77mA3IOmjd16YwfiCYiwpGpG6ICSU1E4e_XR8dKeHonbtmSz2OLx80NRvseFeH6c52VZEUV7R642dPygxtB5aDr3Fzj0j1R68A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قرقیزی‌ها با سوغاتی‌ محلی به استقبال پزشکیان رفتند  @Farsna</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/farsna/459170" target="_blank">📅 12:22 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459169">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1575014125.mp4?token=eA8ibvPc70b_kOl0xgg-Eb-1OG8d2uhRA07I0OwWkAP5eLbytFotkJce1vzcXk7m3cZhZAul7T8atl8lpc-Oh44cN63NBXWYDoU6uA5n96RrT_Oe8TfkEKSGz5L6cQ_UOQnDYqumMWovb1B5tC8zm3KL4BptPbblKWT9rbnRB6PlTubGoS0L5eDmTLUcZ0YQ49YdC6U5AUgzcyLjA4iAz7kxvHDwPCdR6LYerzt_cXOsRnCamhtGXdYUkZWjXaQmSreDh_MNOXJ76uL_LM7HXHj1X8iErTLGNDEsuoo8DqJbqVkWmeA9naREVKE3ysQvf1kt79khmONl46zm-uxE2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1575014125.mp4?token=eA8ibvPc70b_kOl0xgg-Eb-1OG8d2uhRA07I0OwWkAP5eLbytFotkJce1vzcXk7m3cZhZAul7T8atl8lpc-Oh44cN63NBXWYDoU6uA5n96RrT_Oe8TfkEKSGz5L6cQ_UOQnDYqumMWovb1B5tC8zm3KL4BptPbblKWT9rbnRB6PlTubGoS0L5eDmTLUcZ0YQ49YdC6U5AUgzcyLjA4iAz7kxvHDwPCdR6LYerzt_cXOsRnCamhtGXdYUkZWjXaQmSreDh_MNOXJ76uL_LM7HXHj1X8iErTLGNDEsuoo8DqJbqVkWmeA9naREVKE3ysQvf1kt79khmONl46zm-uxE2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وعدۀ سرخرمن ترامپ به آمریکایی‌ها دربارۀ ذخایر استراتژیک
🔹
ترامپ مدعی شده که ذخایر استراتژیک نفت آمریکا را با نفت ونزوئلا پر خواهیم کرد اما طبق گزارش وال‌استریت ژورنال، شرکت‌های نفتی آمریکا علاقه‌ای به ورود به ونزوئلا ندارند.
🔹
مؤسسه ریستاد انرژی پیشتر گزارش…</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/farsna/459169" target="_blank">📅 12:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459168">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hKPIR1WfjUAiw9Kn009ZoTWycIayLLoKlELw-NUrpNBtdON9aEvzpHoga81feytivi-zY5NhgX241p7ZvPx8Pt3MLlnPavYr2MT9lDmJa_ttuCU-xZ6l0dePZ7SHVCKRV4s8JrIDDLCNnLLFKZoFz43V4_h9OChBxGjlSsrl9zlO6C-oS19M5mrNbvP_VkrZ5Az4D4nokVeYr5wii_74T3Bx3iBpxFMkjMaOImkpFn0sBFmqi0TtTk4Clri8zxG5YLFKn8JiCvUpJwVTTvM3Vns61h6yNE0MmP3Zj25x2TbBlPVzLW8oAAJxFHW0Ewo-K5-9uNTekap0voxzGMvdwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عراقچی: نتانیاهو یک افعی فریب‌کار است
🔹
نتانیاهو با زبان عبری با افتخار می‌گوید که دولت آمریکا را فریب داده و آن را به‌نیابت از اسرائیل وارد جنگ با ایران کرده است.
🔹
او صراحتاً با خنده می‌گوید که چگونه از طریق هزار ساعت حضور رسانه‌ای در شبکه‌های تلویزیونی آمریکا، بر افکار و سیاست آنها تأثیر گذاشته است.
🔹
اما وقتی انگلیسی‌ صحبت می‌کند، او از توان رهبری رئیس‌جمهور آمریکا تمجید می‌کند. افعی!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/farsna/459168" target="_blank">📅 12:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459167">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">تبلیغ خریدوفروش وام ممنوع شد
🔹
بانک مرکزی با ابلاغ دستورالعمل جدید تبلیغات اشخاص تحت نظارت، تبلیغ خریدوفروش تسهیلات و امتیاز وام، سپرده‌های بانکی و اجارهٔ حساب را ممنوع کرد.
🔹
همچنین تبلیغ خدمات بانکی و فعالیت‌های مرتبط توسط افراد و مجموعه‌های فاقد مجوز بانک مرکزی نیز ممنوع اعلام شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/farsna/459167" target="_blank">📅 11:57 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459166">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KR152lG60beULRSLF8Cr-AOqtx9lZaocSt4chDu_zKQAYaQw-lcm5PHCLUGlzQF8h2_Bu97MKHqlFubo3Qd5vTx48YfMj7Jc1PR-5ekqqnBEH3HyTQbamxNtn2fron5iEISHjI6bHqYyGnKtRIn16lTV0htxNN0fQF0Pwzzp4qI8Cp2nR_pi4hF2l-OaWMmomh0oX9bVEqUqx2TQMfR8eLZjBw-3-G8msZhwNeg8a7tfv5c-3H9YhpprqCQF3wu7t9a8EmxaBznmcORYIhI4gtgLDw2UPCzlJa804-ixXr5R6CvxquK9NJELzJaGGztjitJX3o0HWNZG0TAbSD8r6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر کار: امشب معوقات بازنشستگان واریز می‌شود.  @Farsna - Link</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/farsna/459166" target="_blank">📅 11:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459165">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6bdea93d7.mp4?token=NAadopo26AJx2ADc-2eWcb-GqGzZfFWhLptC1kUM3z7sYCxxq9Gb3rl8QmujQtfAWVk8Hw1AKdx5Ey5GNgU2clY5kzRAzbMMblih0i4chXwBYU81i4gccUtFyhbRpzSSNCgmn88LrMBPw-3KOJSy1Y2Ki3Oqy5BWpI3flaspAGhgePehgv6rlfukhqao_k_u_ApdiKbfuSIvp-PLF1Ujyu9pczPD0lHPgIrzMSWwkyODhnkHvUS7IHjJKm2IDBxs4PFpZ3xqwO0px3RdDEIcIa_yYe4dOwn5hMK8qJvRJPsDaX-woM-H29ugVVHjT67tFCp9zRSJb5x0uGEVcGG72oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6bdea93d7.mp4?token=NAadopo26AJx2ADc-2eWcb-GqGzZfFWhLptC1kUM3z7sYCxxq9Gb3rl8QmujQtfAWVk8Hw1AKdx5Ey5GNgU2clY5kzRAzbMMblih0i4chXwBYU81i4gccUtFyhbRpzSSNCgmn88LrMBPw-3KOJSy1Y2Ki3Oqy5BWpI3flaspAGhgePehgv6rlfukhqao_k_u_ApdiKbfuSIvp-PLF1Ujyu9pczPD0lHPgIrzMSWwkyODhnkHvUS7IHjJKm2IDBxs4PFpZ3xqwO0px3RdDEIcIa_yYe4dOwn5hMK8qJvRJPsDaX-woM-H29ugVVHjT67tFCp9zRSJb5x0uGEVcGG72oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ادارهٔ بنادر هرمزگان: یک کشتی آلاینده در آب‌های هرمزگان توقیف شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/farsna/459165" target="_blank">📅 11:44 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459163">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aArVvxBnuYDwNP6tr2Hx6tTkG986xS1Wpb7KMwyCXOJJGJkA73hyqufE9ozAEE57vSjT8lH5J9Nw8yf3If0EJpzFktfrR9VOYAFh7Tz16APYcc1rVWrW6nVhoXGS2-lCsiHIVY0rvNSrEWWJXAFGQOQsSEPaxB77qLk6EB5rPFl65tDPDscKzfppRIMrmcp_KbvAsVf8BngswpWDbHB7fdy51Wqd6KuC8WLGzCWcO2MkDcl6qrPDzurbSvWeErON_t0vHWeGT9r1DUP98RnE7E6Tz7GQ0j40IqgJL5NAB6SmHjNfHB_WOLZ6MYafagTbiqgKJXrVLe7EYuZ45Rub5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dVH2w7bV_ogCCl0_vBY4w3qxw-Qui-1qOV7p5J7cPmkRRSMrJ4RNQ6Gd53GKf4sRBRY-tyLMyhPtgWK4GSs7Xk9e5rJlVet03r1kQo2g1G-MI5FKWsjX5xNBLJ5EspyCorBbb_ESrBHHudeq7HmMFo9EDQL-d6eX4EpwuN4gMhwG9rNSS7dx0e-7B7PoJJhmyWHBvY3dbu1v3Wxn9UzM9BC6ouneddq4SGC-z_C8YEQbdRcBzEyoy3KMSZ9hdaCBi7zEyRqy_PDcJ2CeCz14JRbswP_86NoUrZUwbyHiZQbP4ZrOgiEhHgcXkSuzKUKDgeDpdimR2cCdIIay1A4UYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ادعای ترامپ درباره نابودی توان نظامی ایران سوژه شد
🔹
صفحه‌ای با عنوان «پست‌های تروث سوشال ترامپ» در شبکه اجتماعی ایکس با انتشار مطلبی اذعان کرد ایران موج جدیدی از موشک‌های بالستیک را به سمت تأسیسات نظامی آمریکا در اردن شلیک کرده است و از کاربران خواست که برای نظامیان آمریکایی دعا کنند، موضوعی که به بهانه‌ای برای تمسخر و کنایه به رئیس‌جمهور آمریکا از سوی کاربران خارجی تبدیل شده است.
🔹
برخی کاربران با لحنی طعنه‌آمیز یادآوری کرده‌اند که ترامپ و مقام‌های دولت آمریکا پیش‌تر مدعی شده بودند توان موشکی و نظامی ایران به‌شدت تضعیف یا عملاً نابود شده است، اما گزارش‌های جدید درباره شلیک موشک‌های بالستیک به سمت مواضع آمریکا، با این ادعاها همخوانی ندارد.
🔗
اظهارات کاربران در این باره را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/farsna/459163" target="_blank">📅 11:42 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459162">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c76191ab23.mp4?token=a5u6T7jRCCwQtgmXic2scY1lTW4L3CxYuxmjD21JP2o9Y5rMBzQkLElXkZ5KW-V1H9ofUF6fTB5Ob8pt1p-YuePH3L2HD8qE2x_AFgt4U0w9eouo6h-YoMdGtM3_PR_jdI_dHOra44KGrrKbbuKnuZSIUU7bBNFuI4jsYuHkh2opIeH4yJsBUmeZSSjFZC7F_iCTjue63asUoMQKwp5wTF-KLjkXY0beX3QFoepetyq57LLFIDg6-81WbPxB7-hLd1m8Llb6DVoLOZeg0HiTeUbaMEMdBp623OMlmbbYGi6z7Tl1wjRjhpx02SNVia6TWA8uSoDq9dvFemHXaQjpeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c76191ab23.mp4?token=a5u6T7jRCCwQtgmXic2scY1lTW4L3CxYuxmjD21JP2o9Y5rMBzQkLElXkZ5KW-V1H9ofUF6fTB5Ob8pt1p-YuePH3L2HD8qE2x_AFgt4U0w9eouo6h-YoMdGtM3_PR_jdI_dHOra44KGrrKbbuKnuZSIUU7bBNFuI4jsYuHkh2opIeH4yJsBUmeZSSjFZC7F_iCTjue63asUoMQKwp5wTF-KLjkXY0beX3QFoepetyq57LLFIDg6-81WbPxB7-hLd1m8Llb6DVoLOZeg0HiTeUbaMEMdBp623OMlmbbYGi6z7Tl1wjRjhpx02SNVia6TWA8uSoDq9dvFemHXaQjpeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖼
بیانیۀ وزارت امور خارجه دربارۀ حملۀ شب گذشتۀ آمریکا به لارک و پاسخ دفاعی ایران
🔹
وزارت امور خارجه ضمن محکوم کردن تجاوز نظامی آمریکا به لارک که نقض آشکار بند ۴ مادۀ ۲ منشور سازمان ملل است، مسئولیت شورای امنیت سازمان ملل متحد و شخص دبیر کل را برای ایفای مسئولیت‌هایشان…</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/farsna/459162" target="_blank">📅 11:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459160">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cffc673694.mp4?token=JJW2ykYrZG0mWLR3OqsqwPb3wVORTyVpGOLChVfMs7dK19t0qQ2wm_bUZt5Si5ZnJ5e4Rbj21xO60k_5vd9LQ5wrSnP7mWyTdw8X3oJjyv0ZKSG9JGWy2jOPjb8iz-0T5Jwk7ajwdxWktjWmswukgYpvw7OrVv3tbAOh1NcGONl10KGqcm9YV1Q3eSFQ30_iTHuL6urAdUG8RccUCxkH5nkmSNj_WcgQNbuPreoKgtheMTMpvooQV1We8kYQF5cD9usdXooamGePbvjv0sJiCK9iCl8EVPziHNNNawy8imzMmUWDcmfL9NJd4FLIwVjfT8C2-5sfl7XY4Xcu6oKqbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cffc673694.mp4?token=JJW2ykYrZG0mWLR3OqsqwPb3wVORTyVpGOLChVfMs7dK19t0qQ2wm_bUZt5Si5ZnJ5e4Rbj21xO60k_5vd9LQ5wrSnP7mWyTdw8X3oJjyv0ZKSG9JGWy2jOPjb8iz-0T5Jwk7ajwdxWktjWmswukgYpvw7OrVv3tbAOh1NcGONl10KGqcm9YV1Q3eSFQ30_iTHuL6urAdUG8RccUCxkH5nkmSNj_WcgQNbuPreoKgtheMTMpvooQV1We8kYQF5cD9usdXooamGePbvjv0sJiCK9iCl8EVPziHNNNawy8imzMmUWDcmfL9NJd4FLIwVjfT8C2-5sfl7XY4Xcu6oKqbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام عابدینی در برنامهٔ سمت خدا: بعثت امت یک معجزه است و حقیقت آن مقابله با ظلم است.
@Farsna</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/farsna/459160" target="_blank">📅 11:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459159">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9edac3d8a5.mp4?token=CWTBNqulTE_I-fogCfhS_PN_W1gL32N8HMdWv1dZCxzLJmpNpwefD0TMvByT_ZNkZTuX2TOJkXkkiQmK0KmvhjX5OS-KDh6fvDK0vGbHfd3fn-rz4beovvGORI7HEXdSc262Upwjm8fqqeULV-fflAc2SNYdmWQTUzi-EP2n-H_YDILGPBTPIwd1aKDTL5ZqnhCdBOdJDKKdIlnpHzfX8nFUXt6KGIH4FUDT86OUlnWOCqAEDztQhSJobFvR1rDahn3NT4ecQykyILrHkC-fEzK8PFW8dkiXu05Fr09EK1IabEHWxWFwcg7PSrJ8zAyMe_IuOVzyNI-eiWUveR0mPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9edac3d8a5.mp4?token=CWTBNqulTE_I-fogCfhS_PN_W1gL32N8HMdWv1dZCxzLJmpNpwefD0TMvByT_ZNkZTuX2TOJkXkkiQmK0KmvhjX5OS-KDh6fvDK0vGbHfd3fn-rz4beovvGORI7HEXdSc262Upwjm8fqqeULV-fflAc2SNYdmWQTUzi-EP2n-H_YDILGPBTPIwd1aKDTL5ZqnhCdBOdJDKKdIlnpHzfX8nFUXt6KGIH4FUDT86OUlnWOCqAEDztQhSJobFvR1rDahn3NT4ecQykyILrHkC-fEzK8PFW8dkiXu05Fr09EK1IabEHWxWFwcg7PSrJ8zAyMe_IuOVzyNI-eiWUveR0mPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان وارد بیشکک شد
🔹
رئیس‌جمهور در سفر به قرقیزستان علاوه‌بر شرکت و سخنرانی در اجلاس سران کشورهای عضو سازمان همکاری شانگهای و شانگهای‌پلاس با تعدادی از سران شرکت‌کننده در این اجلاس از جمله نخست‌وزیر هند، نخست‌وزیر پاکستان و روسای جمهور قرقیزستان، روسیه…</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/farsna/459159" target="_blank">📅 11:09 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459158">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5261a5e1e2.mp4?token=B1VT1NJF1Mo5ejSyS-jegD1T4NHvHcHtNRHxBJvQ2rqmHQlfxdVKM4ERu3sRw5bJcGhRF6z62eGVBXQScBp3P3GmQyVcCRL9HZ-_TOXIfP1Kd1CGz-zQouW_AEf3x-aAkvUdgYhRumIVVmLWOtuijWudgXNwVb_oDVYktlbl-O6mCYKPo8gzpPlM1tzkd84Df1sVtNa5DGJ23aeUE20gCl9APah0b_oW0VcY3EDKeqC3bbpAhcec9l1R2Mk26lB_vyo4ggHY3SxBv1nGvXFB0h6MzqNI3DYoP77f3b93B3SorQYi6N6_PxxAhVeLiSMj4mczG7N4KV2LAp2bn3Psmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5261a5e1e2.mp4?token=B1VT1NJF1Mo5ejSyS-jegD1T4NHvHcHtNRHxBJvQ2rqmHQlfxdVKM4ERu3sRw5bJcGhRF6z62eGVBXQScBp3P3GmQyVcCRL9HZ-_TOXIfP1Kd1CGz-zQouW_AEf3x-aAkvUdgYhRumIVVmLWOtuijWudgXNwVb_oDVYktlbl-O6mCYKPo8gzpPlM1tzkd84Df1sVtNa5DGJ23aeUE20gCl9APah0b_oW0VcY3EDKeqC3bbpAhcec9l1R2Mk26lB_vyo4ggHY3SxBv1nGvXFB0h6MzqNI3DYoP77f3b93B3SorQYi6N6_PxxAhVeLiSMj4mczG7N4KV2LAp2bn3Psmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: کره‌جنوبی گفت که برای مقابله با ایران به آمریکا کمک نمی‌کند
🔹
وقتی با رئیس‌جمهور کره‌جنوبی تماس گرفتم به او گفتم: «آیا تمایل دارید در رابطه با ایران کمکی به ما بکنید؟» او گفت: «نه، متشکرم.»
🔹
من گفتم: «یک لحظه صبر کن. ما ۳۹ هزار سرباز در آنجا داریم…</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/459158" target="_blank">📅 10:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459157">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rnT7jg2Kw2cZ6Bj4jWZGIlOue81g7sTIguVcXlftnB54V9hCoT0sCfZFRQxqYlQpjF9JyztIDXb3VfGvQnzySs09pjfQB9QcSA7V1plUfNfGv7vY9eh7YsD9j_StWflyMptTI1IsKaFocsH-N16_i0bOP9Fsa3oEQI3768l_qw5-2WaZfYYqljbszbBk5Qea7ZHtKDRxWPJs6UsPAcsnPVGnFmfFTnzLnohTBQNUsv5D0TbWnNwS5Eobpg64rJRnbFh5V5K5EizbUDj_epiT-U6p1yA-pxZE5Q8cmMmfdNaYH0yJPgtszArvlFHcxEMN5pu2CADlvGmRLkCwnPRp4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاج دبیر جنجالی را برکنار کرد
🔹
با حکم رئیس فدراسیون فوتبال، هدایت ممبینی از دبیرکلی فدراسیون فوتبال برکنار و حامد مومنی سرپرست دبیرکل شد.
🔹
این تغییر در شرایطی رقم خورده که مدیریت ممبینی در ماه‌های گذشته با حواشی مختلفی همراه بود و یکی از مهم‌ترین آنها به ماجرای سهمیۀ آسیایی فوتبال ایران و پروندۀ چادرملو برمی‌گردد.
@Farsna</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/farsna/459157" target="_blank">📅 10:26 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459156">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/btENMZRr3Q_EGL1co9k-bmuNH4WcbjYrE3fm_ETu5rJvU_GXTycwg-RDCO_mAxdVB92OA3ejl5BPw5a8d2rnJE97mJAW916q6pWO_pSnSMD6PVcdwd4maJIiAZUi2qfJaVYTlwGZXjysEBwyS3YuOE2NNvroJrG5N3gNZy-seOgijAHTWOzM6oZ8Wgfcc3oEYgxH7Jn0CwYBiClNKTJ34yEiBmgZpI129cLJ7nZ-gAmJNWF081Yw3Lyi9Qdon104vJYZAh11kJa6Q4ou6P9Y-yfGGp6knH1pooei1hDkAvx4JIJH5Od4cXoaRbpYVLJZSdQ-OJuyYMFVf9uEPWJbyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
وزیر رفاه: معوقات بازنشستگان تا نهم شهریور پرداخت می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/farsna/459156" target="_blank">📅 10:21 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459155">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIKGwoBSTH_p4bhQPeDYvDIFQiiv-inNnYhj_BextNNQeNw0c2nKlXxrl9nSSLgC_ESTH-bvp-VpjEICJKP1UJkN-Gqs_r8O2Z8L5Hm7uCfWmAgwusab-vwiTP6-saNFfeTM3FapsE2cRK4zpsf_xEgrQMxQYhpuVZGeT2e354HR1EBOn7ADlbPY-rsCvuucPunjsEXgFE5zllot9l5R8YtRQJGMSvsEIE8chXWMSKfGkM3kLBjCceHFj7qc49OTd7zCeE7dJyvU5nGnPWrwww8Xk6tuOOK_jGJSmRN3ibFl18YT2TS6beZzpg8CrfLdzBKSP4AFLVj1VVg1wljX3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان وارد بیشکک شد
🔹
رئیس‌جمهور در سفر به قرقیزستان علاوه‌بر شرکت و سخنرانی در اجلاس سران کشورهای عضو سازمان همکاری شانگهای و شانگهای‌پلاس با تعدادی از سران شرکت‌کننده در این اجلاس از جمله نخست‌وزیر هند، نخست‌وزیر پاکستان و روسای جمهور قرقیزستان، روسیه…</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/459155" target="_blank">📅 10:17 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459154">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66874910f0.mp4?token=R_fCMOdAFxh4LslbZ_YjroLbwZK4hnRqMwnxkKk62tXOL9dR0sXK4GAW-CHDOZEP9H8QwJfjtK3QqvYetiGmhc9wxCyA2tQxjOGFUk3Z2InG4P5-fTrEgJqm7tvW3KHLTDUmF4NVZitFhWOxa-X2B3VetbXEKuAOmRGwKhyl8sAMidOhIZXkENADlsGA-6VoN-aEagAeA18XurY5b5m_6TZVWHc5E0ywn6Oeb6qtNshoCunDQmGV3M-9Pgek40Rm996zHsbtg4x8AnwyWEGySOW726vRuqjBDmwsefMnsNJCPambf7g9b_RWwUYwBDHCO8cFUs2GgHdjpl3SdIry3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66874910f0.mp4?token=R_fCMOdAFxh4LslbZ_YjroLbwZK4hnRqMwnxkKk62tXOL9dR0sXK4GAW-CHDOZEP9H8QwJfjtK3QqvYetiGmhc9wxCyA2tQxjOGFUk3Z2InG4P5-fTrEgJqm7tvW3KHLTDUmF4NVZitFhWOxa-X2B3VetbXEKuAOmRGwKhyl8sAMidOhIZXkENADlsGA-6VoN-aEagAeA18XurY5b5m_6TZVWHc5E0ywn6Oeb6qtNshoCunDQmGV3M-9Pgek40Rm996zHsbtg4x8AnwyWEGySOW726vRuqjBDmwsefMnsNJCPambf7g9b_RWwUYwBDHCO8cFUs2GgHdjpl3SdIry3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شیعه و سنی یک کلام، انتقام انتقام!
🔹
رونمایی از قطعه "منتقم" با حضور مجال در جمع چند هزار نفری مردم بندرعباس
#امت_احمد
@Farsna</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farsna/459154" target="_blank">📅 10:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459153">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rd__iKY3BJI799k96Gt5hYzMIO1DoWKNVSByhgAvlM0eOHAmbpxV_1ux6KXdtE3wQUFaZEi1JD3tih9QbGkIq5Pv3JrtfcYch2gorwLzVFXut5U7Z5r43MBfFk9BOrhzQiS4QAJccGdl97UrSZ_D2Y3M5qsO4Il1ThrTeArKdmL95M9CTyUdjSMUT8BYmlNOxhGERvqRaxmR96qAx7QI3GyXFwh0EXAw_D2XgOENTPvuQk1nBmN33lGAh3bCm3yuA45ITXmVhzb4GRj3pBkW9I2K2GqfBZWMzS7Vr7puVqu30Zv50uKh0LNi2NYpSIOzUyRPI9EqwV9NtePuoAarRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">*شرایط پیش ‌فروش BAC X3 PRO برای نیمه نخست شهریور ۱۴۰۵*
🔹
شرکت خودروسازان بم شرایط پیش فروش خودروی BAC X3 PRO را برای نیمه نخست شهریورماه ۱۴۰۵ اعلام کرد. این طرح با پیش پرداخت یک میلیارد و 500 میلیون تومان، از ۷ شهریور آغاز می‌شود.
🔹
در این طرح فروش نیمه اول شهریور، BAC X3 PRO در دو مدل ۱۴۰۵ و ۱۴۰۶ عرضه می‌شود. خودروهای مدل ۱۴۰۵ با موعد تحویل اسفند 1405 خواهد بود. سود مشارکت این بخش ۲۶ درصد و سود انصراف سالیانه نیز ۲۰ درصد تعیین شده است.</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/farsna/459153" target="_blank">📅 10:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459152">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/farsna/459152" target="_blank">📅 10:10 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459151">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HjRGmbmXFLbAH5pESv79N-9rbGkvfnVwV9QonCZmq_p6lyjcf9XZlpFMWq7NDWJHZi5p6j7E5AOwGP7-GyLhUgPuyaGwm3klyIPMMf72eF2J4qqAhnqE6MiDt_r3gNpmC-LSb_qF2AvCOWuWijx0F8g4YZ9DsM79xcF9kDhGv88obk4zUT59zzTFLz6r2GZPvikpEIbTH3lPcqQ1k2w2_4yy7ntv8Cl1dyl6hpCWwnrj6Arq0NkU7MMn2ZFmaczPwwIwPr8ljd-qdkR13QBnMhRW39xdAqQ9pt2Ko4g37zs_-OMAlhyZv4enwhH6quadN7Be2fPibtwK6Q3IaKAufg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: ما دنبال جنگ نیستیم اما پاسخ قاطعی به متجاوزان خواهیم داد
🔹
رئیس‌جمهور پیش از ترک تهران به مقصد قرقیزستان: ما دنبال جنگ نیستیم و این پیام روشنی است که تاکنون به دنیا اعلام کرده‌ایم.
🔹
اما در مقابل هرگونه تجاوز، هرگز آرام نخواهیم نشست و پاسخ قاطعی…</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/farsna/459151" target="_blank">📅 09:58 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459150">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8gEVCatQZMUpENl5Np503BAcIDTkWhQo5Ml2T2HnJqpwrN2Ns-IAiRyd5RsvfUVY3w4fQDW5zakjjyQrRB7EavXxTwV1HdMvD3a1u1F6mKiqQLnhvCqfBImcK-gX51GaXpQqa3fIuV4tvu2RH5vN6tRnX3DN_eXeKDrM4qdVSJkomqyNChtOEOQxPOx0x2EWVfflkUzQjZsODAfKSPCbP8DuKAlmHu_9qARFpyFkywyd9ag3T-YgWOm07O1NUvPQoThcgaO4_k0Z_sWGOSVkTxS2BU9wvJyoFCkI7hEy-ENv2fVbSklgYTWrvqoZAyEutBh061P6Xyz4NakJpEong.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انهدام باند جعل و کلاهبرداری با ۵.۵ همت محکومیت مالی
🔹
دادگستری مازندران: یک باند سازمان‌یافتهٔ جعل اسناد و کلاهبرداری در بابلسر که حدود ۵.۵ همت محکومیت مالی جعلی ایجاد کرده بود، متلاشی شد.
🔹
رئیس باند و ۲ عضو اصلی دستگیر شده‌اند و تحقیقات برای شناسایی سایر اعضا و ابعاد جرائم ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/farsna/459150" target="_blank">📅 09:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459149">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffcdb467fc.mp4?token=CkONHCs3NCpQpylX2AN6FbVxC7US4HEPfH_01jOud-RIqMyiyXoinQbmpZKT5JunnXCxinmvHRxzz9YwbDKu2M9oRCF0omjjwZA1cVstYXLSy88lXj-rTOrE1fDOBXUiNpdrVccmqzanLU_i7m0EteGkkmLNJ3oAGmfRJbrZc6FzfGNC-zLX7QQ4y2GVlq_-01HVoPC2AU7lfkvzi74Di98QpG_Di4IHU_TIovbhIvN0l6gESTYcWKn-N385YcLImRTmdWbp_IgPPSx3b2YyKxdCMonrz1nG3boaykG-_IaBEZb6U3Jf78Y_GLblIfxhL2wzrcuNkYelqk_-BamQLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffcdb467fc.mp4?token=CkONHCs3NCpQpylX2AN6FbVxC7US4HEPfH_01jOud-RIqMyiyXoinQbmpZKT5JunnXCxinmvHRxzz9YwbDKu2M9oRCF0omjjwZA1cVstYXLSy88lXj-rTOrE1fDOBXUiNpdrVccmqzanLU_i7m0EteGkkmLNJ3oAGmfRJbrZc6FzfGNC-zLX7QQ4y2GVlq_-01HVoPC2AU7lfkvzi74Di98QpG_Di4IHU_TIovbhIvN0l6gESTYcWKn-N385YcLImRTmdWbp_IgPPSx3b2YyKxdCMonrz1nG3boaykG-_IaBEZb6U3Jf78Y_GLblIfxhL2wzrcuNkYelqk_-BamQLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرچشمۀ سیل نپال اینجا بود  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/farsna/459149" target="_blank">📅 09:28 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459148">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">احتمال شنیدن صدای انفجار در جنوب اصفهان
🔹
سپاه اصفهان: احتمال شنیده‌شدن صدای انفجار کنترل‌شده در صفه، بهارستان و اطراف آن از ساعت ۹:۳۰ تا ۱۴ امروز وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/farsna/459148" target="_blank">📅 09:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459147">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">رهایی ۲ گروگان پس‌از ۲۵ روز اسارت در جیرفت
🔹
دادستان عمومی جیرفت: ۲ گروگان پس‌از حدود ۲۵ روز اسارت بدون پرداخت هیچ وجهی آزاد شدند؛ شناسایی عوامل این آدم‌ربایی همچنان در دستور کار قرار دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/farsna/459147" target="_blank">📅 09:23 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459146">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🎥
ترامپ با «حمله خیالی» به خارگ شاخ‌وشانه کشید
🔹
دونالد ترامپ در تازه‌ترین نمایش توهم‌آمیز خود علیه ایران، ویدئویی ساخته‌شده با هوش مصنوعی از انفجار و آتش‌سوزی در تأسیسات نفتی جزیره خارگ منتشر کرد و مدعی شد: «جزیره خارگ دارد با خاک یکسان می‌شود!!!»
🔸
لفاظی‌های…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/459146" target="_blank">📅 09:09 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459145">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c9ca828d4.mp4?token=vf2mp5HJR0LzftYUBJf1XYzKkcJGasx7j8d-WJj8rCV4nR8AjSL3Zp3F9X7ikaxzBtbzdpPOglS7FIC1WdSOXdXrmZDqpJCNfXCBXM3MimYXR-xXX8lLOQeo-r1UcO8HU8Q3vL84NgiGHpiN7tsTHU9Rf4J2uELMgIIw4mrESYA_hLHlQSTa3e-UaWxXgMYvOtZznbOCwYHtIYi5y_uY-0rhpHqfs0dvrjFbgpYWsQMzleugZeyW_3TQckEPRxGh3Sq0ioNSMRUZfaeGiB-M8_dt2KMFlNNamMS6n6tk7spo-v-3qKdegNANsBBHLcfVgHll9ry3trlBrosh4ZTDLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c9ca828d4.mp4?token=vf2mp5HJR0LzftYUBJf1XYzKkcJGasx7j8d-WJj8rCV4nR8AjSL3Zp3F9X7ikaxzBtbzdpPOglS7FIC1WdSOXdXrmZDqpJCNfXCBXM3MimYXR-xXX8lLOQeo-r1UcO8HU8Q3vL84NgiGHpiN7tsTHU9Rf4J2uELMgIIw4mrESYA_hLHlQSTa3e-UaWxXgMYvOtZznbOCwYHtIYi5y_uY-0rhpHqfs0dvrjFbgpYWsQMzleugZeyW_3TQckEPRxGh3Sq0ioNSMRUZfaeGiB-M8_dt2KMFlNNamMS6n6tk7spo-v-3qKdegNANsBBHLcfVgHll9ry3trlBrosh4ZTDLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کشور حال‌وهوای پاییزی به‌خود می‌گیرد
🔹
هواشناسی: این هفته در بیشتر مناطق کشور دما کاهش می‌یابد. به‌ویژه در نیمۀ شمالی، غربی و شرقی کشور حال‌هوای پاییزی به‌خود می‌گیرد.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/459145" target="_blank">📅 08:56 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459144">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">گردوخاک و باد شدید در تهران
🔹
مرکز فرماندهی و کنترل مدیریت بحران کشور از آغاز توده گردوخاک و وزش باد شدید با سرعت۵۶ کیلومتر بر ساعت در استان تهران طی دقایق آینده خبر داد.
🔹
این شرایط جوی تا حدود ظهر ادامه خواهد داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/459144" target="_blank">📅 08:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459143">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
دقایقی پیش زلزله‌ای با قدرت ۳.۸ ریشتر در عمق ۸ کیلومتری پردیس در شرق تهران را لرزاند.  @Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/459143" target="_blank">📅 08:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459142">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">فردا آخرین مهلت انتخاب رشتۀ ارشد ۱۴۰۵
🔹
داوطلبان مجاز به انتخاب رشته آزمون کارشناسی ارشد ۱۴۰۵ تا سه‌شنبه ۱۰ شهریور فرصت دارند انتخاب رشته خود را در سایت سازمان سنجش ثبت کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/459142" target="_blank">📅 08:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459141">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sT06J8DQ12GhjGOQYkcDI45wnoX9um9GKsULW6Dm8DQacwO0_VllbGUd1z17nz4sEGKe_dGNp17nEH5mHTYaT1E5d5OmHDyyzmj9AkR8KCRL-SJkz31oJM17BaaMnNyjMFUolLpBR0JB2JaWLgljGMM97NtAIQ3rHfHbRaxbLbFak1WKpW4D1leUyrqM3gK5CCRvj_inHEYf3L4GkeHW0EhxVQ7OTRDgdA8m1OVLBhMOwta3IgdMH-9im8QWsN6gjn2BrnNH_lnPc-uSPqaj9AsySv1EXhPVWZv1AX3my_9juNDkZtT9pl4Tr1_dyGVKoWvLfEmbUyenmmt1NlQAUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
دقایقی پیش زلزله‌ای با قدرت ۳.۸ ریشتر در عمق ۸ کیلومتری پردیس در شرق تهران را لرزاند.  @Farsna</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/459141" target="_blank">📅 08:04 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459139">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1e57e6988.mp4?token=M57MxG7HpJFvCQO5JmFWoB3i4V24ax6f3kw-g21iIz7z3kqgY9G6ILJE8YQonJk99mFCuIJjTuScf-7T9d4Nw4KqjduqjeM9iO5ESHISj-UQQnoRKloXJHJpTseu5OtlHdKnmUQMWaSlW297w5wVzn8jkWcjwbTGnRh5-hS5aMFBIe-4FVH5FJk7tbh8dTinA05uiJXygiP5NkQ0Q4BZd6_lFdFnF2xZV8AgaQChwyA9xyk44qiL4MH5SWzVlXh12kf5sk7MXze_KZtZGmvkGzkZMyMbPV4jnZ5rbj2d7G4W9CAU4dV-m2VOfO4IC4fxJXhKRzTuOcpoVHfPlW6msQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1e57e6988.mp4?token=M57MxG7HpJFvCQO5JmFWoB3i4V24ax6f3kw-g21iIz7z3kqgY9G6ILJE8YQonJk99mFCuIJjTuScf-7T9d4Nw4KqjduqjeM9iO5ESHISj-UQQnoRKloXJHJpTseu5OtlHdKnmUQMWaSlW297w5wVzn8jkWcjwbTGnRh5-hS5aMFBIe-4FVH5FJk7tbh8dTinA05uiJXygiP5NkQ0Q4BZd6_lFdFnF2xZV8AgaQChwyA9xyk44qiL4MH5SWzVlXh12kf5sk7MXze_KZtZGmvkGzkZMyMbPV4jnZ5rbj2d7G4W9CAU4dV-m2VOfO4IC4fxJXhKRzTuOcpoVHfPlW6msQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ با «حمله خیالی» به خارگ شاخ‌وشانه کشید
🔹
دونالد ترامپ در تازه‌ترین نمایش توهم‌آمیز خود علیه ایران، ویدئویی ساخته‌شده با هوش مصنوعی از انفجار و آتش‌سوزی در تأسیسات نفتی جزیره خارگ منتشر کرد و مدعی شد: «جزیره خارگ دارد با خاک یکسان می‌شود!!!»
🔸
لفاظی‌های جدید ترامپ در حالی مطرح شده است که ایالات متحده که از یک طرف برای توافق با ایران دست و پا می‌زند، شب گذشته اهدافی را علیه مواضع ایران در جزیره لارک هدف قرار داد که با پاسخ قاطع نیروهای مسلح جمهوری اسلامی مواجه شد و سپاه پاسداران نیز اعلام کرد در پاسخ، دو پایگاه آمریکایی در اردن را با موشک و پهپاد هدف قرار داده است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/459139" target="_blank">📅 07:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459138">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
نیروی دریایی سپاه: یک فروند سوپر نفتکش متخلف در اثر اصابت با ۲ مین دریایی دچار آتش‌سوزی مهیب و به‌طور کامل متوقف شد
🔹
ساعاتی پیش یک فروند سوپر نفتکش متخلف که قصد عبور از مسیر غیرقانونی جنوب تنگۀ هرمز را داشت در اثر اصابت با دو مین دریایی دچار آتش‌سوزی‌های مهیب شد و به‌طور کامل متوقف گردید.
🔹
نیروی دریایی سپاه مجددا اخطار می‌کند سرنوشت کشتی‌هایی که از مقررات امنیتی تنگۀ هرمز تخطی کنند جز این نخواهد بود.
🔸
رعایت مقررات ابلاغی نیروی دریایی سپاه برای عبورومرور الزامی است. شرکت‌های کشتیرانی فریب تحریکات ارتش کودک‌کش آمریکا را نخورند و اموال و جان خدمۀ کشتی‌های خود را بی‌جهت در معرض نابودی قرار ندهند.
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/459138" target="_blank">📅 07:53 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459137">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kfN66JCL4kn2nSlH86AHnGlMIepYtHv5KyKplZR5BIXgnl_4XFpmb4dseHs6zLPGW_3yzl0kuz8PkXpjTgjRXhPClXqCnExFjcc_Q6Gnnf2bLN-IFKSz0nfSEp8TjqZYtTsoOIgRWnQa_sHMIwlQjhfhaIKVY6YwD-DrGP6BYKV3lpA2gEFq3rzWXoUWV1UPIAb6QxnWokm4pxi0BU86TP0kcF7xX9zVvGHy5OvWaq2szRN7F05rOzLSk5_nQ--HtwbvWjlgmUzlabEpvf5EISarV3s4uKc_coBuRdTbERX77RPqFeaPFFBk8XClG_NWPGCfupWXb4geaBkbEZfT-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
بیانیۀ وزارت امور خارجه دربارۀ حملۀ شب گذشتۀ آمریکا به لارک و پاسخ دفاعی ایران
🔹
وزارت امور خارجه ضمن محکوم کردن تجاوز نظامی آمریکا به لارک که نقض آشکار بند ۴ مادۀ ۲ منشور سازمان ملل است، مسئولیت شورای امنیت سازمان ملل متحد و شخص دبیر کل را برای ایفای مسئولیت‌هایشان جهت پاسداشت صلح و امنیت بین‌المللی و پاسخگو کردن طرف متجاوز یادآور می شود.
🔹
وزارت امور خارجه تاکید می‌کند که نیروهای مسلح جمهوری اسلامی ایران در اعمال حق ذاتی دفاع مشروع تردید نخواهند کرد و به نحو مقتضی به هر تجاوز نظامی دشمن قاطعانه پاسخ خواهند داد.
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/459137" target="_blank">📅 07:50 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459136">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9371f8cfb0.mp4?token=oSBSs7VVO7DRZsb4SbbZrJ2VZtg17fz-hyhFgPamhO2jBD3bfuSreygDkiozlJfqhDg35Ubu1UojNAgC58FEx1vJzCxiBIa7FMRv4PFd0SnMmAuk98b6PCQMKmZpFEABXeL3ZOAGyHjUmyvt-WMPfkMnFWpygpj4G42VINbgvGeecom0dI-n8UYErPq8SWtQyZ6Utiqz__zxvscHETM-OjujVONY-xE1epAhU9Ion32EB0ha9Wi9kPwwT4WuCZ7aFW73yDthH-9cwQ2kI5iCkTohnBmFIb_YFAX773f28GKTO5Uwdo-gytUrGVMfRyCFKQhMC8LQt4Hc7xEUIfxQbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9371f8cfb0.mp4?token=oSBSs7VVO7DRZsb4SbbZrJ2VZtg17fz-hyhFgPamhO2jBD3bfuSreygDkiozlJfqhDg35Ubu1UojNAgC58FEx1vJzCxiBIa7FMRv4PFd0SnMmAuk98b6PCQMKmZpFEABXeL3ZOAGyHjUmyvt-WMPfkMnFWpygpj4G42VINbgvGeecom0dI-n8UYErPq8SWtQyZ6Utiqz__zxvscHETM-OjujVONY-xE1epAhU9Ion32EB0ha9Wi9kPwwT4WuCZ7aFW73yDthH-9cwQ2kI5iCkTohnBmFIb_YFAX773f28GKTO5Uwdo-gytUrGVMfRyCFKQhMC8LQt4Hc7xEUIfxQbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
سپاه: محل استقرار جنگنده‌های دشمن در دو پایگاه هوایی آمریکایی ملک حسین و الازرق درهم کوبیده شد
🔹
روابط عمومی سپاه: مردم شریف و بپاخاسته ایران اسلامی، ۱۸۳ شب حضور حماسی بی وقفه و تاریخ ساز شما در میدان، دشمن را در بُهت و حیرت فرو برده، امیدبخش مستضعفان…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/459136" target="_blank">📅 07:43 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459135">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
دقایقی پیش زلزله‌ای با قدرت ۳.۸ ریشتر در عمق ۸ کیلومتری پردیس در شرق تهران را لرزاند.
@Farsna</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/459135" target="_blank">📅 07:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459134">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">دست ایران در بازار نفت جهان پُر شد
🔹
طبق اطلاعات کسب شده از وزارت نفت، ایران خارج از محاصرۀ دریایی، برای بودجۀ سال ۱۴۰۵ به اندازۀ کافی نفت برای فروش دارد.
🔹
در ۴ ماهۀ ابتدایی امسال نیز درآمد نفتی پیش‌بینی‌شده در بودجه، تحقق ۹۹ درصدی داشته است.
🔸
پیش از این،…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/459134" target="_blank">📅 07:12 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459133">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc0ffcb3e.mp4?token=Om9L5bh2HZaTz1DDfbH6ThpCSRHJIVr0wDyCMkathpnndloi0JPEaWycv01zBlZEBnnGY9IbpYPuk3SdjVl3kE8UerhhP8prwAPOCSd0YrgVzXgYJvD_ej5pvdOz6W7yCxX6afsCVoEInmnHjBe5oqwB5TuUvCDeCJAEnAcQslIoXhWfdbso4He9ItXLKenN79BzdBwS3HSoLHbgRIP4tLOu3r8Y5nqyKlInv29Lr738P0zNRJvIV5m212SlnX8ONr3CAIl3UOJ60UbDgi6uwRC5kJ-n4GuJt15SLe5nc8oBEnTs2L4_kTEKwtvxZSFHZDarW1s_nLBPRhmw2TxgbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc0ffcb3e.mp4?token=Om9L5bh2HZaTz1DDfbH6ThpCSRHJIVr0wDyCMkathpnndloi0JPEaWycv01zBlZEBnnGY9IbpYPuk3SdjVl3kE8UerhhP8prwAPOCSd0YrgVzXgYJvD_ej5pvdOz6W7yCxX6afsCVoEInmnHjBe5oqwB5TuUvCDeCJAEnAcQslIoXhWfdbso4He9ItXLKenN79BzdBwS3HSoLHbgRIP4tLOu3r8Y5nqyKlInv29Lr738P0zNRJvIV5m212SlnX8ONr3CAIl3UOJ60UbDgi6uwRC5kJ-n4GuJt15SLe5nc8oBEnTs2L4_kTEKwtvxZSFHZDarW1s_nLBPRhmw2TxgbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرچشمۀ سیل نپال اینجا بود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/459133" target="_blank">📅 07:07 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459132">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
انهدام یک فروند پهپاد MQ9 آمریکایی بر فراز تنگۀ هرمز
🔹
روابط‌عمومی سپاه: دقایقی پیش با آتش موشکی رزمندگان پدافند هوایی سپاه پاسداران، یک فروند هواپیمای بدون سرنشین دوربرد MQ9 آمریکایی بر فراز تنگۀ هرمز مورد اصابت قرار گرفت و به داخل آب‌های نیلگون خلیج‌فارس سقوط کرد.
@Farsna</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/459132" target="_blank">📅 06:46 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459131">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bkhHmg_T7YlOkGV-ws69VOH__kky53V6qzodzDRlrC3wfR7x2gsUyv2v2sopxQ9QrFCqVOFWMkj5-9CZjENlTWTr2elqhZNs4lo36NosuTxv1h0TqnFBdw2NWOl6Xc047J18eKqDZjziLQjImRm0ZFyt-O4QcfZesR_KAboYf7bcLs1wQDR3sznGLNqeyqtEmV8b6Vw18waazGwDF4ot7N9CZSn47gu76wcA5u6PLQX8URLIKrNmgY6WzyprhTl17jRH0uzPB6tGlpK3GqDyz039CVTUD4k-aZ0Te1t0mAnkGBl_S2O31RbbSardZX5YJksqpSxiIC8w879QK_ocVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان عازم قرقیزستان شد
🔹
رئیس‌جمهور به منظور شرکت در اجلاس سازمان همکاری شانگهای، عازم بیشکک پایتخت قرقیزستان شد. @Farsna</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/459131" target="_blank">📅 06:29 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459130">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🎥
ترامپ: من از ناتو خیلی ناامید شده‌ام، ناتو [در رابطه با ایران] با ما رفتار خوبی نداشت
🔹
اگر نشست ناتو در ترکیه برگزار نمی‌شد احتمال داشت که اصلاً در آن شرکت نکنم.
🔹
قبل از اینکه اصلاً از ناتو درخواستی کنم، آن‌ها گفتند که برای مقابله با ایران پشت ما نخواهند…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/459130" target="_blank">📅 06:10 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459128">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6249a95134.mp4?token=j6OPQSul3B5ROv4bgIdNzJaT9C08sexRcQIW4gRd8FXhmhMukXt3HCLS51Q140ddyF5T8-hPHk9afue6tXwC9U9t-MAeRQ3w1SE7ydD0oBtAiKUP8O8fd70UeT-Ntv1x8Z-PNUC5sd8X9yOI--xVPUkH_ZWgoxSMrxUrG7QxjdN6QKWhq5ceynJvLoMAjgJvA25LDvTYw6IiplOZcqOtTa8a-BfHEdDDHVPuUzClCumNd7BUmOoax_RbknZNkDJCFLgNm94bv1Yaxd-bOOkSDgaOSicXn81HT09J-9ogBrrKtUD9LAPWQwJk1DrFLIXzNp6e9a3sWt5EfLNFApaZhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6249a95134.mp4?token=j6OPQSul3B5ROv4bgIdNzJaT9C08sexRcQIW4gRd8FXhmhMukXt3HCLS51Q140ddyF5T8-hPHk9afue6tXwC9U9t-MAeRQ3w1SE7ydD0oBtAiKUP8O8fd70UeT-Ntv1x8Z-PNUC5sd8X9yOI--xVPUkH_ZWgoxSMrxUrG7QxjdN6QKWhq5ceynJvLoMAjgJvA25LDvTYw6IiplOZcqOtTa8a-BfHEdDDHVPuUzClCumNd7BUmOoax_RbknZNkDJCFLgNm94bv1Yaxd-bOOkSDgaOSicXn81HT09J-9ogBrrKtUD9LAPWQwJk1DrFLIXzNp6e9a3sWt5EfLNFApaZhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منابع عراقی از وقوع انفجار و برخاستن ستون‌های دود از پالایشگاه الدوره در جنوب بغداد، پایتخت عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/459128" target="_blank">📅 06:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459127">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fTGxW8nWtFVWGd-Wt6HT-8lcNtFzFCXA-EG_WpbK6NOXZSz8CSNGLjIa-7Nn5LPIB54kGztB_9Obja8ouBq54hVltCFu3MEUUw5lFCVbl7Ao4Ji1sEfz_kR4d3pRrpadKojIRe3wRwL1uZteB6jvaj741wVWdzwB8S-IBTJLkOQvaE1Zliz2B4kKgrwXBQpDHmyjfxiRX4VlwTHZmDYqjIODjo3wWXz6FhmfaOWPhK3Ljs-3XJoDSrNk3iWYj1R973cZ3oyW6xTSn-HugFgfU-85f5Fhb6DyHy7Awo-cf54Wyv9Pm7iWCYjVsrmID0A5FNNqYn1Z2CP6aIy5HjlZ_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان برای شرکت در اجلاس شانگهای فردا به قرقیزستان می‌رود
🔹
روابط عمومی دفتر رئیس‌جمهور از سفر رئیس‌جمهور به بیشکک پایتخت قرقیزستان برای حضور در اجلاس سازمان همکاری شانگهای خبر داد.
🔸
بیست و ششمین اجلاس سران کشورهای سازمان همکاری شانگهای نهم و دهم شهریور…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/459127" target="_blank">📅 06:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459126">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">شنیده‌شدن صدای انفجار در جزیرۀ لارک
🔹
مردم محلی از شنیده‌شدن صدای انفجار در حوالی جزیره لارک خبر دادند.
🔹
هنوز محل دقیق و علت وقوع این انفجار مشخص نیست و پیگیری‌های خبرنگار فارس برای مشخص شدن جزئیات انفجار ادامه دارد.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود. @Farsna…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/459126" target="_blank">📅 05:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459120">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/osyKq5XqFNZhmYOuQSKTvXEM2TV7NA68u-vG5-zff87wQrABWfarplRlZ_sRhfoAH5kfsNS_CSIU_F7TEyfl0XFZHCttAHzSdSEOGuZQPcVErrCrOwDlXRDaxEHKDFjbnEbgYuSpcozXGCvrojhwRYefASZ-9jSMB9ole0oYzDr5nYvm39am5DzBABdSVBcGhokJquk5UpXxRWQLD7qrN7wERIMQsPIqjHntDmrzjvxu4Xs5lkE2JdhtQIUAnq5-STZ-xgtRUIpxZ6chWg3RX96Rago-phwgSVhYkatQDGnBrdqeS-wXhqu1-06osXRFI4V24FrkmrMK7j2VWanA1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BOUdCvTHUv5EIrBTK5rNnaRvyMcpmuZR-FoGca86qpTjazhBS19P8P5xc-ISCC_2UJc7mNDTar01qyv2EXcETTw-Z5qCE8XYKdCjiK3JI-TLJY9WKP9Q9D0x47XsvKahQpFAAtnbWDr0S1-2hN3pt8UhoYmbtkrl3wqPfoNMJz9moq6_z2yXofBrMJ3akGIUggT1xjv_ma55tTjNwKQbzvgphzYoHgNApPQ-x6pQb5OMXdAIEIFeUJdduieDQjcF2f0mvvwJ8SwsufalwqFvU7WJMHtV6OxKmYk6lCGK28xlcKBRYzvZPxKl_zGFDLHgs57xPiGcUQR_pT0MlWzMWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qENwqZtYs-rsHnUvAdp0tFuLKL3x7cFdO1oF85y8PmqdzucykgktVTKgcJdNrqK2S1lZj38jOvkyFchw1RZ5LBPhBx-zjch6-GRkCqngHN2Ydg8P9mILOysObYCkzq8jlXt_J4Vzsj2Zx9LpMXFifyV1ZkOh1DMspT-I7wysFUL2lynHHhPrTiKvaJo1aj1Eu2AJDwfHpPS_5dYj0Ct2E03b-3sh2FFPLiITdrnSzGX5SPobGylidvxwoHCd6H5_ZWuUwFLeb0Rje8tgx7lND3tbsA9THnQvzgAspiILYJ6JKu7m9mscd8NcefeD1XFQmk1Hy48uJbpv_GNdKYxi_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G4tOUjnsWWbd3y0wSnRZX7dihHsin_iumAUHvEN-52amtRkOeQBZWlZQNy1ZXbfr4QFVih8poV0rkevWOI0NRaAIUSKfzNZwi1JklA3jB_EscmZA53s2_YWm0xv3k2wh1kJc1OfRxiS7s1AL8W5hG50AQVdOLtk177v69sCbIoIPZ47iYu2JwCIFA3J0qkqbmwa_7iJllxS5DsClu-Mh2XK_4-Q6L5TeXB-XiGhQ1ZScg07XSEELCPVMHT3swdAz_DIHxjwt-yf2_w8Xjdd5KXhgoa6ZRZ-vvKvy7zgXliL9Cl5jOaqlWAxQeDL8EhiGXaXSnApF1d_v6HLm3tI5ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mSEDqvegEbEyvz4g_oFCaAaV3AUkCer-UVfTLDTY-E2eMlRDqUjJiderrTIIC8DVVSPNyUa8isZekpjyWMTHg6LZdcGzOgOphYkQPnBNfDk4kSGedg1FqyYOmD17SJydr4J28XttGq5pL3GDxWwEweYRh3QTO8ay8xzEI1MCSn6fLmJPis_892N6nRg_-wxIkw0qsA4lQPk8nYHWU9Gcz6jsK4eHWpnICUBdTuovK4NQ6S8A8zLd_iEHm8irMRC7D4XqJRpOVNRReTO-QXNRkvokpQTAk4h60JvDWyhVIk-ABxYlY8sdYSJmYXU3FPfzdh9RrpUSjqIVWWXD4viiHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BitLAI9pYYWOtjdaI3394LI4WwGuYrZFmAwjahAVXs7jTPYm4KM50JhuG9h2sF5lpLI7HCYVSfDUxltXvoa2_m1t-aDk4XBoGRMKFY1C9yxX30ueu2yx4s4hwrh3gqysSPCM0XiT6JbUPZFUB_CxfFRmwguWX6YaB4awPEukf3952hNrqPhHc_8DyAXjH1jkeegVZZ9I-FSbz92DqFMO4dlqNGUDj5hhU4AVaUzFaCwnYwjm8UHvNiXFrY9lPERkKA5Ta8k-QCbPYKN6WX9JSSHe_vPxdu3_Zm15zSj_okQzf0TwpCNvjP9o8ZJwcnVfvNyyfsiRlvOS-SQqy8XcPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جشن میلاد پیامبر مهربانی‌ها در قم
عکس:
حسین شاه‌بداغی
@Farsna</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farsna/459120" target="_blank">📅 03:53 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459119">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7489b53543.mp4?token=XmaUMU6jfZoJVzH5CkJNWOX4cpF8AU8JVsxuTMWGK0nsHQIR6H1AXDyOF6Wmcpj6dcGvrx-LbdV6q6sIrYqN3sSnJUgzyeo_fEbxeN7mPESjeMLMtAiAocEHq4_b2_WHv6tEv15M3HgnqPRsIkwReQcdn924X1xticlfeZHQEyG7M07RsW8Gwv3zIjSGpBooPhLS8ItWqI7rpfUIHDsPM2hDvjAzwIwlzjKj9-xd_rXXW_wXEIk40uQKrdc608N5nMDKIqWCXlq2ZPEvV0wUInkwpk656gr_1gZRzvbZH5N8OA2nQqZiUltOvzOk8GYcMQRpGXgynM-Z1CzRAOM4aUwolmY50IN_K2jjZPlDhJLqG-jR4u2hahuQmylTCaLT2_P7fHx6g-oFP4zmqT630mlX9v203KEhtG4hKggkoolbwIdeEMIsHNVutJf1FyDtro4BHZNSicMkUi5LrTGWKiYyZ9UuERUK925jPYidFxnvxRgGGHXoVJe4hGcmt4YkMJTm9urvaZYW8PPS3GY4IqERUrHH9bq-RM4Roc5J6rCJrwyMuyuXBMzvsxngz8BDsca3Dr1PHD9kZUa0CwLBQg0Vn-CRrtt6RutaoT1ir83F_WtcSXJKLpkHiXjX9PMC7qdseGbaXprfu3g9-grKG6x_IUicAB6n8_kS5zH4rfM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7489b53543.mp4?token=XmaUMU6jfZoJVzH5CkJNWOX4cpF8AU8JVsxuTMWGK0nsHQIR6H1AXDyOF6Wmcpj6dcGvrx-LbdV6q6sIrYqN3sSnJUgzyeo_fEbxeN7mPESjeMLMtAiAocEHq4_b2_WHv6tEv15M3HgnqPRsIkwReQcdn924X1xticlfeZHQEyG7M07RsW8Gwv3zIjSGpBooPhLS8ItWqI7rpfUIHDsPM2hDvjAzwIwlzjKj9-xd_rXXW_wXEIk40uQKrdc608N5nMDKIqWCXlq2ZPEvV0wUInkwpk656gr_1gZRzvbZH5N8OA2nQqZiUltOvzOk8GYcMQRpGXgynM-Z1CzRAOM4aUwolmY50IN_K2jjZPlDhJLqG-jR4u2hahuQmylTCaLT2_P7fHx6g-oFP4zmqT630mlX9v203KEhtG4hKggkoolbwIdeEMIsHNVutJf1FyDtro4BHZNSicMkUi5LrTGWKiYyZ9UuERUK925jPYidFxnvxRgGGHXoVJe4hGcmt4YkMJTm9urvaZYW8PPS3GY4IqERUrHH9bq-RM4Roc5J6rCJrwyMuyuXBMzvsxngz8BDsca3Dr1PHD9kZUa0CwLBQg0Vn-CRrtt6RutaoT1ir83F_WtcSXJKLpkHiXjX9PMC7qdseGbaXprfu3g9-grKG6x_IUicAB6n8_kS5zH4rfM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر لحظۀ شلیک پهپادها و موشک‌های بالستیک در عملیات تنبیه متجاوز با رمز یا محمدابن عبدالله(ص)
🔹
هدف این عملیات زیرساخت‌های فنی و تعمیراتی و محل استقرار جنگنده های دشمن در دو پایگاه هوایی آمریکایی ملک حسین و الازرق در اردن بود.  @Farsna</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farsna/459119" target="_blank">📅 03:36 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459118">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QFzRx0xLHj8L6oINeNf5TseOcmkW81VD909qwB9QJEcto1TSuZHt9NrlueniSSlrH-PycJxu_kGIcjegiYQ8lNuv43Ui3SVrW7Z8Yubd7Vxpl5QzhQfhUfQIQqIbMdXtbSEeuyGgFdDpuoMtY8O9f8iaJfSkYiSvkztsLhsG0cJ4cw7bZkJZ-yBVqZV6GXWxvy-eg8M7h92ynN5VHN40CVK8aVWJIY-iFHd52bjBXQK1Bpk_RdtZ72en5v9hUiS00Ib62ah5OdTJmyHLSHSbIjtUdK5bPinDQMqLGTuqWSGsx4BktmssAixUQXOoZH8w0O_9lZQhfgtbmahMLk0kQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اردن همچنان تکذیب می‌کند
🔹
اردن همسو با سیاست کتمان و سانسور ارتش آمریکا، ادعا کرد که ۸ موشک ایرانی را در آسمان این کشور ره‌گیری کرده است.
🔹
ارتش اردن همچون اطلاعیه‌های دوره جنگ رمضان ادعا کرد که این موشک‌ها به اهداف خود اصابت نکرده‌اند.
🔸
چنین ادعاهایی در حالی است که اردن بارها حتی حضور نظامیان آمریکایی در خاک خود را نیز تکذیب و همواره هرگونه اصابت موشک‌های ایرانی را رد کرده است.
🔸
مقامات اردن حتی زمانی که واشنگتن به تلفات نظامیان خود در این کشور اعتراف کرد نیز مدعی عدم حضور نظامیان آمریکایی در خاک خود بود.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farsna/459118" target="_blank">📅 03:30 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459113">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AhJ3ZTwsMPA_-OOBY4MZB7eAJ6qdp7gjJdX5ayBC8PPhBq7QNiF5OYaOjh9krmPDV5ntrX1IccxpTgTVFfIH4N7_dVyeDEIFJmIXP5KCI8Ewf7TuyHYa2Gsgk_5Sy78kq3SEaGmwqJgqHPZEEuflCTj-eETZIsBTTvUjJZTkTNQeR3LiYbEfjjsRgsc8FXRcKrLP9pi3WVoAHkGZAEALRphmBk0eIA6_Z3-lDPjNFNYlRPR5mEtcQ3BC6a43uYOE9AhT5xkqKiNu-bhTAZ4qOczdJBOITytwHqk55BYBy3gle0WT8lbYRL-1THo9lrVa6cvZRmVi0ppwLK0IMvUhBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/irOPp_W9r3Jy5yCnReFvTLHLSqTw-t7EolMijWZd1mFpER63GJU9JMgc110sft8rxyxY-dyXgLwWjXW-4Wep4da_nEbc7aQ_jqHA2uoVMZJKvz0C_-ZrNP-v0O23mUztpPVeO3QAUyccgAZh8E_-dS1SkHkg7AEI6JRKW7-t743V4E_72M_b0R5Q7wiz2-fjv5BLhC21jbHEHoG3WuxqdTXvMlwhUy2AK9xpJ2l7G-aldjOEY-miPsbLm-QDeoSxbav-L8vNJxqQdJXV3S6PpBYXIuX1Ad6kk7lKwGYZHSqCDijmN35NcoiE5uivj0cQZsWBQutV2RzBnCE-W1HJ8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nzwkD5SQ1LtF4v27_18WFaigW24Y115hQUSQBKmvNDSNJ6wI67ef1GJrJNvllrT8CAy1VneX2V9Y3iyh5Y0JAylYADOnpsj_dI9WSA3YDqQQq44QydwjJrQRm514TLq-vldyVSippew1YiMlmtmOPROe33_H5O3H6AXS4uGc7i2vcYPSZEwjSzSKURc76HsuA2_5TE-YfTtr7QBfgP2-GMLaO6Pr0sNBUfPF1eclJUgNgLK4PGbu__QlBv8zt30RJgBcDS1GrktBkgBbBuplYeMdBUVNBBaZVjzRQl-ZeT8fGJlJFg02DBLrMru7XTp-vl4322huU4349f-D0A1AzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p5l7l6CLxS7yHiSWTzNh9AJPsBV7HzQIjZR_16nglSJ2JKDXpgJ3FuqsfAkdhFUXyN61A7cLtiLy1DZ3u5RO93IMway1dhEmg1NN8vSCIWpTUSEb8WNDcF657EIQsoyvbFi20oHhidQ2TAfBGh0iN6oJBWSHP1UD8QsmskQreDVxalm1i30vJgZyK-VKKkjHIwuKIH0BWtxnYpbkmeIY01yGJCa2LVaKhnpemcLU8qdMCahusmW-Gblw-SJkuwktHwQc4r0PJ9JkMdQoQHjMVATf0uhYhv0pWsbkOE_qpPfRa_KSbJxt35Wbk77b_yTqjO5KbsdygkPr8puM4__k0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LE4edHtd7I-3ilYWjT1Jo5-Ug8bexGH2fRrstU0yKY2mzjl-VD3SazsxKQ7zMpPk5Aj3l7nYKxUjzYYfAV3RY-x_V9XWEmAj_7zJN-tHIZ0fKSKCBbZutbwGzII5QKhXtGiavJQWYyYUnE4FINN_UBgDKkywVwvtb-56LNGOwd-G0b5DVjlpOtKvewO3yBGarQQzVtk1Bgo1VIpxqEAF_xCso_eyZIkob25ed0F03vw0JTrGN7XSm2OHp6-tl3qklbl86tflYu3sDlibRmH1eXeyJDTm2Xp-6-muQkCFAQqzoLxSoBZYybAd4O-6iyDYVKMbkU7i_6ru_jZ0D_97FQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | دوشنبه ۹ شهریور ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/459113" target="_blank">📅 03:25 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459103">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AwPd_pZixpv_k_VJa-1HI78yoFXNZgJgxgnO8sbIOHEeHD11eEvBoDkjgGTeCnS1VBuFYGqIUlwebjwg9Ftxv23dgjI6qgGUvHuz0cNeTzfXwtAjjmRWqYuLTASpCDOlgegzPaB2wyTgJlzV0tHICXbr4TRj1p-Ly7oFRCu-4MZxYOVeFLP4E5mQc6PDstL3Dz_tBlEdkIb_glUezrCaUDHizOV61B69_Da1oXnqw-zRT3FYE_hWQtsEuzuzXS6uleMC_oXDXyv4V0daqaQsu_VLemv4Z3oW8Lh3sVilhvX9XFR4PfnGglXCc8L7GkIlbzSH3_ZG7sdgt0bLQePcsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J022L6JzqbiiRGd1Wo6RA-HGaOAezYNSXhMAOvq9eD5t-CibQCn5yrqde7E5sSzQxkA1JY3WGiC-dKc9u4YbTzG7EPTz_f2B9QuRxA1EEtD_8VsF7ZaAdgYqaK06ZEvFefPFIoBr-cNGcltcpvlw1UIdB_-RXtDrZJZYnM-bwnp3Pj-R49Mm8DtuQ2poo8vlOErHwsezVbXaRyjsxmsTSc1l0xi4lqD7FX2-UN-ib9KsPV-N0tngcxJbUzrL51GD1b3ci-I3kkNkuZI55__mzKcFVvBOyhw3d6IQbatWuXktsOH2Igwnq9Umf9b7q_l3GkCfYskH1i-ODU4IKeK1qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VqdS6KfqCM4G_V7MQWJU6QwrqHRDMXuWusGrYzeHIwhOuUuM0mujt_qfYrGFDfIqpuNmaSTcNUlc-jvmLIgnV9I7lXVaMg4f0BmhHwisMrT53OMyV2mUmvh-cUskcaRsbrVcrJvLFx3sfJlDiuD2ZzF5J4JbgfV-ExfKAx3MtlOdQBnT_8jcj4hY9x0sar0c0s4KB4a7DoJSMfRUsLl9BCYsr4PUcHu-fSby5Yu2YYk87-AcyHGdi8qn-O5QIv2Q-FwhpiuPamy0-Rlut-TlsKvFPFEKXKTU7aIg8dJdqn1v3TJsnZq1GVLVJqln3ZoJFjPfTGiaJqWMckSx3qcQcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jFK4lwc2HVqrBpDvHXbW1Toewqe3YjZOvzwuI3jn8OuvZuuccPj5WmJ72ji4EbYQAphqugwjPSx7hlY6rKrTCOxNgGU8WjjtRSKQ26VV32dKrpvQS1bJ4kyfqpQ-FtTnh83n9gqmsNfUMcVcA66YdukCUoHX0aY1A4vc4DKP8XbZ67L2LkLqvZ0SSgozCslTEYGCzhJ1neeU4QuGuQxhg1GTUAnD-wLkrqJnLI97Ez_cACI_L5bzayRni4SdN9jDxx5_dnOi0rB_UNyINGQw1x1ua8h15C1rR1ArjAP7UepU_jABcVR3ZKTIhdMlnL85dh-iDX7RR-IWYfqXy7s8Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aNnL05S0ePnIUa1AZXiKU7QRf2X8UT91rwvt3h2sodKsxS6XPGHTLKRVb79Eny6Ifu3J7a1hThBLh4rz9h0eTKEPh1bTqQxotSJDgYr335uQOKOlfjYdBbUBQxgRZfB2LBo7YKIDj7u_FZJQzrnrK456srlKHZ45SRpLeDqFOkdxyEpULpkfeEI0-EFcm8vdXwaZTCL6fbGbky3vQwc3D1KRuMpfouQ7UPRM2TeiKg_ckj0ZcT_1X7NYC_9mQ5W5GbawCAqtMhwaanxZ_QGru-1HCgbdB2o4XzO9tnRj8_oPvhsfi6f8v7gpX3hkSLbbxlbpSXKE9qkjbTEk24laaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WQ-WWZ8i4u9EzFSWOidbIRwwOCpZcOljw9Kd86XvIfjyiXcNcQA1pwEEdOVcsV7UB7vKOMFt9EO4e3tP_kCxcLWzJuRWa3Sp30fnyaU1LDUaSMtlPKOLrI9mJOXOrso6afUHpfxVFygP9BMQRjOBsL-hEnRG6OMx3XNuUgvawg7F0LlTACGXrIwHWwV53orPe6az2V7mXyF3IAMJ4RYa2eUz_Pleo-X2s1toG0_s4k2CQweyWhdedHUR7v49vuYA9yh3VopUp5l0XjSDfMERUjqq5FbMy-KLsWEIc57OZvIkx8wZ4JjITwzL1eUwEFNxveWTtQI0_zYtbtDWmWF94w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jOKAW6OeOCPU_2778RAKVbSa1UMPtL9-efT-pT1Ubp4dakAsD9O5DU8PNyUi45KDZzwaIDdZpQL9pRNHUWgcn_lQkakmzvOrRg4BCMJBxf8Z0HbDhxZbkR6pNIKaNJC_oA0bglQnArptnGYsuT53RSwGcT0QDy_0NizRwW20AgGkMZ1kxbKmh5k_NL40igL64SYPUvcjA2BK703eNL3KoDrGRKAGu_legE-RV5WGpmW4LYj7PEPyCOWZkKxEsYJvPYSqpbrE3R3kCWibQvajWwar3an22j8a1cj91tJzrJaLLq0KfGJC6yI8hR9ixuh3Mm-5U3XODDmints9-PJQAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dsMacjHZTpROQEuEy-VT4vXHLtohAaIPz0lJj9jNqOvjUfDPFTFEzYVUR7refVEs3Zjnay-e9REpMEGN2MiJ8so-YfKFYmK8VCZgG2UQ6D1oUD77JzLv8Rt7E-PqQFBy4VlzCM6tXteV7eYXU6XM2vxpP4TRAc4A6lcGJyVVje-bDAUg017D0clFUoH_x7sJK64zZR8DZZEL99mZ4PHe33rKKpilnu126gjM7WaLbmU_ULnxmxdahOEhhwUjrb_6gFN_eiu_Fm4mmkN_U7ft5kn8ceS98fCukva2WUwMNuRiDpVtXNc4zi63ZTlH1OyfZgU3tI4sexG9EvGuJOYRUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pN6pBdOO7pR8nOK99xhwgwXOmvXcws2UVhSeqwUkOnYbxlyQ41B0mMrCd7T8itxPSvf9V53r_HyU8JWzmocLj0x6r3xqEBNKmbZ9e4FZ_DN2CCU4yjRPMjZXGlOY5EbvA4tUZRhCna1OmnsQgoZ40Ta300V4J0yIJVvy1R7MgdAORxB-vwOtbSYrXKVPkI95oVuWM3LLJq7-4p5rn8jSRnzSVKogZbT7il5JpR_ejDotuxJLL1qVmj_6JcbXrjZ5mnw1l6mzGPwPx_Yw-kMXkS1IowBknPvOqL1G5L6SsSLPV7cbY14AuZy99wxiBXyIoyd9AQUpzeNlM_x6SpdohA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z7LpaUInGSiagftHzofCeB57T_OdB7eMr3Uhr2CshGlCMapApayG-0_b9zrPXBZTM5x8r-seCWPA1rOewZBw4E2W9xSxBelC5L4tT_pCGUDo8eBSGWsK2XZ1TKwgTA2Pv8zXcnShkttTBokS4nkJLXBxZSNm5bFD9Uid2MvuORBh7GFXGNn3_kpiJ5fwD_eT-sYISPq7o7YmeleAO5pRq7GemUJbSrdxooFUpSrjybcc4i6oc3ipn2aXhk6XGZIDc0pDES_gyG-IH2xhONi0K-PCit6jx9lzmu544tFth6FtZWjKvi3Qn_H8rxYwwh03H-ByJpFGBlp1Lzyqds7nLw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/459103" target="_blank">📅 03:25 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459102">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a738e19ca1.mp4?token=Y4iJnOcr77m3YhGqiYRpDFAwiV2kqLP-90gT5Mc1NXwLSi3Z7vd8QZd-AG9whSHXW6aFFCt3hu5_lU9hG_z3Hpx9t8siltoAZa0FilIkAiyFji1Fnf-RHdDC3577pz1vQqBRUmUJ8mj-MiTNL6HWhZC0IId3_2nHDcgdI1j8sDLNNCTgwQENFcRf-1kIyPs3l_dKQIW4DQAWcEFsuuDMWtqZHHzW51qswnZ437c6TgJLH_igrnp2ErYiNnuTjmRpbArZcXyNY-RctV8UIPs-_IiVtaopozq5obkz_bdIS3wBmJpoRn1QJSywNF6CAtJ54NomdZrdEwOOmNyDP84ScVoJjV5gq-l_gaAqUA73pTT7a2PR_ZHYDIUtLrw-w4THoaL4Fn-8LgXCS4Aex4_Kq3wIglVNUKwUt4dcWS-8oh7Wqx2GETYzvCN1QzsARRCTcoGzMsaJUbWcSME7VC1me-50lVDySbPmsBhnao70Mt6bXAliqcRZ-VMFP8a2jydaIXVGxe9wh7KbFL9hTnhVJlX3YCwtFZcuEUzincKQAZmYbZiRrStBZP09y5OeLBjLRIRe3zgwoq6e5mn-IW9fPnhqpQYhhf6sZKC1vZa9vLQ6bcitZUjuoveIkqPZAYPXhOw3fLNfQ5cgLRE9T59P4de1I7xHcG6A8RBCVWQmMWs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a738e19ca1.mp4?token=Y4iJnOcr77m3YhGqiYRpDFAwiV2kqLP-90gT5Mc1NXwLSi3Z7vd8QZd-AG9whSHXW6aFFCt3hu5_lU9hG_z3Hpx9t8siltoAZa0FilIkAiyFji1Fnf-RHdDC3577pz1vQqBRUmUJ8mj-MiTNL6HWhZC0IId3_2nHDcgdI1j8sDLNNCTgwQENFcRf-1kIyPs3l_dKQIW4DQAWcEFsuuDMWtqZHHzW51qswnZ437c6TgJLH_igrnp2ErYiNnuTjmRpbArZcXyNY-RctV8UIPs-_IiVtaopozq5obkz_bdIS3wBmJpoRn1QJSywNF6CAtJ54NomdZrdEwOOmNyDP84ScVoJjV5gq-l_gaAqUA73pTT7a2PR_ZHYDIUtLrw-w4THoaL4Fn-8LgXCS4Aex4_Kq3wIglVNUKwUt4dcWS-8oh7Wqx2GETYzvCN1QzsARRCTcoGzMsaJUbWcSME7VC1me-50lVDySbPmsBhnao70Mt6bXAliqcRZ-VMFP8a2jydaIXVGxe9wh7KbFL9hTnhVJlX3YCwtFZcuEUzincKQAZmYbZiRrStBZP09y5OeLBjLRIRe3zgwoq6e5mn-IW9fPnhqpQYhhf6sZKC1vZa9vLQ6bcitZUjuoveIkqPZAYPXhOw3fLNfQ5cgLRE9T59P4de1I7xHcG6A8RBCVWQmMWs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
سپاه: محل استقرار جنگنده‌های دشمن در دو پایگاه هوایی آمریکایی ملک حسین و الازرق درهم کوبیده شد
🔹
روابط عمومی سپاه: مردم شریف و بپاخاسته ایران اسلامی، ۱۸۳ شب حضور حماسی بی وقفه و تاریخ ساز شما در میدان، دشمن را در بُهت و حیرت فرو برده، امیدبخش مستضعفان…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farsna/459102" target="_blank">📅 02:36 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459101">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
سپاه: تجاوز دشمن تروریست در جزیرۀ لارک همراه با تنبیه متجاوز پاسخ داده خواهد شد
🔹
روابط عمومی سپاه: دشمن آمریکایی - صهیونی بار دیگر بر مبنای استیصال خود در حل مشکلات داخلی و کاهش اعتبارش در بین کشورهای منطقه به دنبال احیای نقش شوم خود و توجیه افکار عمومی،…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farsna/459101" target="_blank">📅 02:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459100">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">مبدا حملات آمریکا به لارک کجا بود؟
🔹
داده‌های ناوبری هوایی تایید کرد حملۀ پهپادی آمریکا به لارک، از مبدأ اردن و با پشتیبانی پایگاه‌های این کشور انجام شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farsna/459100" target="_blank">📅 02:13 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459099">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
اخبار غیررسمی حاکی از انفجار در پایگاه العدید قطر است.
@Farsna</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farsna/459099" target="_blank">📅 01:50 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459098">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jcRCu2Il9qw5Cit65XKHwWpfq2jYohaQvlq6LMRdLyVNVL3Xx4RzK8tx9arw_JiP3cB3OfRRd8OVUQzdRF7vBqNoRO7TEKeb6XLE7BeHHegmqut-z9lXhaW1h5GRHlCsBt7GA0G8rsXlMyBHJ7LeswdVHD6SdWOqgZY4X1lw7_N0zAPTu0bcyJpRCLbkQ01LeN035HWe2AjOcdeD1VMuJrk5e5CpfwmFPvyhFakVuu2bxyGw9w8I0LOJM0B45ZYoJYl7yWA_REo4O4jgM9mCfBrFr-gXHpqKnTmoyQRRnYt7u7LNjCly7i5dm4nc-nHsY6_zQLOOe2-0H0lbi9kxrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازگشایی بازار نفت حین حملات ایران و آمریکا
🔹
بازار نفت دقایقی پیش بازگشایی شد، و هر بشکه نفت برنت در مرز ۹۱ دلار قیمت خورد. هفتۀ گذشته بازار نفت برنت در نرخ ۸۸.۳ دلار بسته شده بود.
🔸
براساس ادعای پایگاه کوبیسی‌لتر، افزایش ۲ دلاری قیمت برنت فشارها بر آمریکا از مسیر اقتصاد و سیاست را افزایش می‌دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farsna/459098" target="_blank">📅 01:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459097">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
منابع عربی از انفجارهای متعدد در جنوب اردن خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farsna/459097" target="_blank">📅 01:36 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459096">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBgFuWYTsi-KNNWhstB-F-EfYqYu38g7tgxnGykGaQS1uMgu_Ju8dRM88_1BcUxjai5hsFU_BzJ8JFH56rawXpS8SzkYH3Qo5i3sNJw7isocjwp5ZfA9dErsXgl-OK_jp__Bm8DB5ESjyJz6CS7V31aQOHpO0CFvivLmFKwnm9pMYR1mcs3yVhWkPIfqNFDb_-ed1tR9RIWeQ3bX4uV9bWtHqTMe_TnTYZ5TK3sB20B6YXz6WNZfm7DyhF3TG0asEn0946EdwBzRXLL3RX9tY4MghrSknAz81_Hg_pvUvkjrE78W9o9qneIkHRgTmQNIlKklroxSvKpqbZKoOihSEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرار سوخت‌رسان‌های آمریکایی از ترس ایران
🔹
پس از اعلام ایران مبنی بر پاسخ به حملۀ آمریکا به لارک، سوخت‌رسان‌های پارک شده در پایگاه‌های آمریکایی کشورهای حاشیۀ خلیج‌فارس، در حال دورشدن رصد شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farsna/459096" target="_blank">📅 01:34 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459095">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3381114e02.mp4?token=CxB30otGXbbPNalt3We0aaO6i1M2T2eBgfy9JCuOk33dmJ4BWshsHlYq7JRZtBihMCbCZptn3aZJfIK57XGIO1pJJrETWhQN9WLawbM6rJYoUPZ3ukqg3i4DtHm9GR4LppA-nAD-ksf10QakRdNMBlAuvJ7Dpf9KVheGRsv7ChLdKAXrOpTSVgL7V_SYv8CIAkn4ExTp8Io0weUjWi2pytOe_PMiscgOyaMpK2CVuOlomlrrWb4AEPPd_jJ24j-8XjPYaCKo_NsQJX4_ZhqS7YIEN2a7VMTx7_E2RCGv35ccrYzg902mb3wTjAPovANZXl4yFXcedr7kjwpsJ9nIsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3381114e02.mp4?token=CxB30otGXbbPNalt3We0aaO6i1M2T2eBgfy9JCuOk33dmJ4BWshsHlYq7JRZtBihMCbCZptn3aZJfIK57XGIO1pJJrETWhQN9WLawbM6rJYoUPZ3ukqg3i4DtHm9GR4LppA-nAD-ksf10QakRdNMBlAuvJ7Dpf9KVheGRsv7ChLdKAXrOpTSVgL7V_SYv8CIAkn4ExTp8Io0weUjWi2pytOe_PMiscgOyaMpK2CVuOlomlrrWb4AEPPd_jJ24j-8XjPYaCKo_NsQJX4_ZhqS7YIEN2a7VMTx7_E2RCGv35ccrYzg902mb3wTjAPovANZXl4yFXcedr7kjwpsJ9nIsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خبرنگار صداوسیما: حمله به لارک در ۲ نوبت نزدیک به‌هم صورت گرفته است
🔹
صداهایی نیز در سیریک شنیده شده که مربوط به دفاع ما از مسیر ایرانی بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farsna/459095" target="_blank">📅 01:29 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459093">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
منابع عربی از انفجارهای متعدد در جنوب اردن خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farsna/459093" target="_blank">📅 01:12 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459092">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">تعطیلی فرودگاه مهرآباد تکذیب شد
🔹
سخنگوی سازمان هواپیمایی کشور با رد شایعات تعطیلی فرودگاه مهرآباد، از انجام پروازها طبق زمان‌بندی قبلی خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farsna/459092" target="_blank">📅 01:07 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459089">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W_ALOW8ElpDneANWIfSpmLiWuIFDphKya0cwzMt2YrxkzR_eKF2F1qDSWcEc_O8SynTi46N6viLvmTHpIf6XA0LxoELnGsyOLrEbRxYskUmj3s-zzf6skj4zGBUIP7gmjJ2tZ7CsbxXOoDzpBRo1y-hwwy4wPsqZxINRf3SddEaEBCZnY0SRTrA3N-w6M5YOSM55_5pMPNb1aF2sugNIle_E1g0BCx4cLUfYzwIONO4bxtzaWnU4CIN8qGrQjfevr8kKR868e77BTPU6Ht9Fu3TPYwbNeAzpz4O92fBNka-rD4FSBcLDycG2whLQVolmGAx6eMb2GWe_nbW8nuretQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IwUcMIsMjnkx1Dx48hgw-KX5WtT3QJSQggF_dDO4iM9IzUvtMEQ_qjbuM1YMZwavjF8exhuHAy6Io1RhvNBMswpCxCRCWrM2G-7zGMG_PJamI2d5gzFsoo42aS3nuz2lfNQC6XnyI8UnHNRIAPUVl2yoUeKUvLWlJ4yFfS_lByFncpcswNE9jOgt47aH-3yJNPa5P3Q-sxs5af3X4z_f_3Cgmxn-qFM3ENOT6iZEBX_DuUb-ppCBZpO_eRERl7eGvLRpbdPxEDsWUdILHtWDcg0Xh8v3Lq48xh5KM8Udvw6wJqXnmwt5L5BbhsU8fDJ6XGqdY7pf3jGh0XwXjJzuhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ocCQIAQkNHwkFgvtpf-dMVTtIEWuS2CDe2MWYm9qlNYD8e1DGzQti0MfKITocYzY_0SoADj3XW9uSGtYyw1DH2xQgEktxtzDwnakn5PK5N8x0-PFA9gmmSqyAYDegEx0YAAsZ5dxycoAPkgi-Rfd4IDu_l07nWcsrtqoQhFvru9WIVAKPjcdb_LRWZHtauQNERN6hRFH6S8lAMVirqXev5qlGB_zylDD6dZW_Ly-Kdqm4hwxUwpPDwNV4aYZzsdnM0mJTIzIlA6Sbvvh-_jpUltVTxThFbIsHI7c40pTaj1u5pWXBdD66UDToo2oG4cvmIqXgq72Ai6MBBQQhR2LBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
یاد دانش‌آموزان شهید مینابی در بین‌الحرمین زنده شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farsna/459089" target="_blank">📅 00:58 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459088">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FLoMmcoK1tHzvVTItKHtFoSS8s-AOZ-QPXi9c0xZCC14AB_aM4Qee6Esvy2Qs3InOCsq0s4fC_LoE__pi4vJVZA_lNnoc2h-Jz8gmYnptxzDUDPm6hquDS5M1KIljzLI27_Zocv0eqW4jjA5iA8gLp7z244BQto9-Fcy9Yyfo4WPAMalbLAPaJMLac0Yx5wML_uWJwq8L69Y0A9u-CP5MxXTlXMNDr6FjL2O23UB0pYXG0kqmxgn_aqFUAQmNm0oQctgbXXodzUq5KcomgjahYZGBEeZQjSBv7_VBqCgAFZZINmAK61jg2yd1fFJCel-qcwrGcWB38gRNL71hlzwpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
رئیس کمیسیون امنیت ملی: آزمودن مجدد ارادۀ ما، تنها هزینۀ شکست‌های خفت‌بارتان را سنگین‌تر می‌کند.
🔹
بی‌تردید هیچ جنایتی، در هیچ سطحی بی‌پاسخ نمی‌ماند؛ پاسخی ویرانگر، دردناک‌تر و عبرت‌آموز که سلسله شکست‌هایتان را کامل خواهد کرد.
🔹
با ترس و وحشت منتظر باشید!
@Farsna</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farsna/459088" target="_blank">📅 00:43 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459087">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">استارت عجیب تیم امید برای طلای بازی‌های آسیایی با ۲ بازیکن
🔹
اردوی تیم ملی فوتبال امید ایران برای حضور در بازی‌های آسیایی ۲۰۲۶ آیچی–ناگویا، امشب در هتل المپیک آغاز شد. پیش از شروع اردو، با توجه به مخالفت برخی باشگاه‌ها و تداخل برنامه‌های لیگ برتر و لیگ نخبگان،…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farsna/459087" target="_blank">📅 00:26 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459086">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VECng5FuqlUtOkCrCm76GajJvXduBOGc6h2hRyaAZI54SecQfXjcgUgMf6lRdJ-c8GeNHEZyCFlSvycc491a_3fSBM8kcZlM82c-owAWZIUOuamuFmWJyN1Fm9Ei949_HJyjdMClkFDaccSNTFt82FGfrOGWx7WF9tRbnQI_0aEUIntNg98S89TdOHEnXA2zUa_eicf_AEok3xtyY7oPjjDAgiVX8SFwoLV13oTstr9wEpLFcEs1rLsFDaQnsFMM-auXbukmskXg1Z7MVxytGHGcMHBnm_8iOf9EBnmajok1KvAHqPL96fvbRcxRVX8xnwpwQaPLmViZdhBwJ3a3SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
سخنگوی سپاه: اقدام تجاوزکارانه دشمن تروریستی در جزیره لارک، با پاسخ و مجازات مواجه خواهد شد.  @Farsna</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farsna/459086" target="_blank">📅 00:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459085">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCTx46UgXI4Tg5u8tfAM9cigKcoiM-VI8Ua1eXvK773sVq-RMgRVLhzt3ZwoWGZzePLzBfT3vmBkgbX7-40iQjGGqyQAIWgyAdhoH6YM-9PymO7bWAEG4645j0PI9y1Ri4fqeS7Ss7dmWyT2ZJqRUNQ7gqAUy8cH1I895CdR1pDnbrsDoHS5grQM60qCbeYh9dXEvleg6VaAKTA_T4mkxR4u2T6476ZSkcs1EbQNYWN-5xKiNa4QA_jyqHKqe8j4Tp6qy3x2ewRouiFEU5t4VhAdkd5j5d1McrFIyfqhl8aGNcVO_kzSduQ8HqFwkOGXge49q-ncuvFNlaoy0o5C7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
قاب ماندگار از حضور رهبر شهید انقلاب بر مزار شهیدان رجایی و باهنر
@Farsna</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farsna/459085" target="_blank">📅 23:56 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459084">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9e7aa5b3d.mp4?token=XpK0w06qkT6vVK3GcUa7GnG7TQYWjOIQ_ORmYWQ4oapAJFYOvB1lL08yNvqrVH0eBiWNxTSDB3QaAdI0j7RBjoEQ4AmGt69oPKlgVL8EMZqIKNbPm_5xe9rOTGBDkYXkcAWbKirwV4qmvbmqmEmruCsgQSnj7Z67Y3V68GPJXdAsFzwEaC6CuJ49A_S_nV00EwjpGT46kmsOKMHjC5suoJBYOAU7n89VDcq3kAXooggC1cEsqh6amgo9DVT6D8ZaUGWwqf2yED-pwR3SUZNpDC0vALwf8jgYe91tyxlPAbxR-B_2Y4sETYkPxEjfWV3nLu3-N9eC-waWTFUAC9xKQTnXN8rNtuxREch0z3k8QzLnPPPrq-o5DDnELiED8aCaPdi3zgZ02fSPxp2xpOI_ZKsbDJ8bkLR2sc0pPYcSCOyPXkjK7P0T_YOknlbvEx0dymCYpvMwSTa_scE1cyViRs4jbxv3UvpiWKibzSHcS7DWPA0AFjE1-Nyv1042D29mGWVkPEHYFCbOPm2YzxLHFSRYeo4p7z0YT4GADAdb_4-Df2Z2pTPrW0V06JB-VYSleNkBhakPvhqBkLAnvNBjEOomP5U01dvMCtPrxLAonT7qi8EJHE8XcSfhbiDwtxjPVUmBnlk87dcakiqqUDrxAU4_Pvrrnblha67mOrq77Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9e7aa5b3d.mp4?token=XpK0w06qkT6vVK3GcUa7GnG7TQYWjOIQ_ORmYWQ4oapAJFYOvB1lL08yNvqrVH0eBiWNxTSDB3QaAdI0j7RBjoEQ4AmGt69oPKlgVL8EMZqIKNbPm_5xe9rOTGBDkYXkcAWbKirwV4qmvbmqmEmruCsgQSnj7Z67Y3V68GPJXdAsFzwEaC6CuJ49A_S_nV00EwjpGT46kmsOKMHjC5suoJBYOAU7n89VDcq3kAXooggC1cEsqh6amgo9DVT6D8ZaUGWwqf2yED-pwR3SUZNpDC0vALwf8jgYe91tyxlPAbxR-B_2Y4sETYkPxEjfWV3nLu3-N9eC-waWTFUAC9xKQTnXN8rNtuxREch0z3k8QzLnPPPrq-o5DDnELiED8aCaPdi3zgZ02fSPxp2xpOI_ZKsbDJ8bkLR2sc0pPYcSCOyPXkjK7P0T_YOknlbvEx0dymCYpvMwSTa_scE1cyViRs4jbxv3UvpiWKibzSHcS7DWPA0AFjE1-Nyv1042D29mGWVkPEHYFCbOPm2YzxLHFSRYeo4p7z0YT4GADAdb_4-Df2Z2pTPrW0V06JB-VYSleNkBhakPvhqBkLAnvNBjEOomP5U01dvMCtPrxLAonT7qi8EJHE8XcSfhbiDwtxjPVUmBnlk87dcakiqqUDrxAU4_Pvrrnblha67mOrq77Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ماجرای کمپین تکراری علیه صداوسیما؛ مراقب دوقطبیِ تکراری باشیم
🔹
انتقاد اخیر رئیس‌جمهور از صداوسیما، اگرچه می‌توانست یک اظهارنظرِ معمولی باشد، اما تیم اطلاع‌رسانی دولت، با توزیع گسترده بخشهایی از آن، آن را به یک کمپینِ تبلیغاتی تبدیل کرد. گویی قرار است این‌بار هم همان الگویِ همیشگی تکرار شود؛ الگویی که در آن، هر ناکارآمدی به گردنِ «نگفتنِ رسانه» انداخته می‌شود.
🔹
رئیس‌جمهور مثل هر فرد دیگری حق دارد که از دستگاههای مختلف انتقاد کند؛ اما وقتی این انتقاد، توسط تیم رسانه‌ایِ دولت، به خوراکی برای دوقطبی‌سازی ِ «ما در برابرِ رسانه» تبدیل می‌شود، جای نگرانی دارد. تجربه نشان داده که این تکنیکِ فرسوده، نه تنها کمکی به حلِ مشکلات نمی‌کند، بلکه سرمایه‌ِ اجتماعیِ دولت را که مرهونِ وفاق و همراهیِ منتقدان است، به خطر می‌اندازد.
🔹
نکته تأمل‌برانگیز اینکه اعضایِ تیم اطلاع‌رسانه‌ای فعلی، تا دیروز خودشان در بیرون از دولت، تندترین نقدها را بر دولت وارد میکردند؛ از تمسخر تکیه کلامهای رئیس‌جمهور وقت تا کوچک‌نماییِ دستاوردها.
🔹
حالا اما انتظار دارند منتقدان، بدونِ هیچ نقدی، ویترینِ عملکردِ آنها باشد. این تناقض، اگرچه برایِ مردمِ امروز پنهان نیست، اما دولتِ وفاق نباید با این رفتار، اعتمادِ همراهانِ خود را از دست بدهد.
🔹
رسانه، آینه است؛ شکستنِ آن، تصویر را درست نمی‌کند. امروز که رسانه‌ها از جمله صداوسیما، با درک میزان توانایی دولت در شرایطِ جنگ و تحریم، بیشترین همراهی را با دولت دارند، جفاست که به‌جایِ قدرشناسی، با کمپین‌های ِتبلیغاتی، فضا را به سمتِ تقابل ببریم. دولتِ صداقت، به‌جایِ دوقطبی‌سازی، به نقدپذیری نیاز دارد.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farsna/459084" target="_blank">📅 23:49 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459083">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
سپاه: تجاوز دشمن تروریست در جزیرۀ لارک همراه با تنبیه متجاوز پاسخ داده خواهد شد
🔹
روابط عمومی سپاه: دشمن آمریکایی - صهیونی بار دیگر بر مبنای استیصال خود در حل مشکلات داخلی و کاهش اعتبارش در بین کشورهای منطقه به دنبال احیای نقش شوم خود و توجیه افکار عمومی،…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farsna/459083" target="_blank">📅 23:47 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459082">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/683a1d1a08.mp4?token=W4riXp_t0cwH6xZSx7ytYUzi552sML6z3ytEMKBY36LBi_Dd13uOBTVYGyZKbb3y9vBMfWm4VEQJ-7cSPzWVDg5BFeICmvqi79eEkrblterJg2oddcNesASw4d4CGcFaQ4LsR5pNwgdfvdgJ8kW3g3SF6ARJ6i3sYDzAQQoWcsEyAwULvKbXza3Mm5bTcXKXxDT5o0AcmpMm3geyn395PnZ0g-7xCtTgQ7KMbvvsLGpVMyGZbizE3yO6-DlLAtIxPcin_L8LDpG67NY3QHIazeKfHNX-hGKOKRo2wR7Kg3PdV0uN4Mxl6NgQ4wDhs0rFU317zp5tCfCLNCKHJnVWPEPHJK0F0PiXJxtTYawaBq_KuQZZkWWZldphdagTWFG8othAcfZ6yjwRESptOGjL1ARsGjJ8eOsYKiUEBQIj4dPXWmDomXF3Bzomhxp7A9LBS-NT338RIBnVxzNH3GjekBH1LHFkr8VlOZx-GVfCLnz2bCgLwt3WOpw02OM4_q8XpFzMJSDuwl9ACmKRzQkJGoRs5TY0KgmWxlBfMfx9F8YepxKXkp8t9pcYF4OGdX8BlHSxgGBzvXoj9KZgaudLYNq9T886q8Kwi2orK9iNBTMmGSn18qtKEBFSwuhvI_GmeKjvbSIxRBP4q9JKQzwCK_wEKKx2jvru7scpGt1FZH8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/683a1d1a08.mp4?token=W4riXp_t0cwH6xZSx7ytYUzi552sML6z3ytEMKBY36LBi_Dd13uOBTVYGyZKbb3y9vBMfWm4VEQJ-7cSPzWVDg5BFeICmvqi79eEkrblterJg2oddcNesASw4d4CGcFaQ4LsR5pNwgdfvdgJ8kW3g3SF6ARJ6i3sYDzAQQoWcsEyAwULvKbXza3Mm5bTcXKXxDT5o0AcmpMm3geyn395PnZ0g-7xCtTgQ7KMbvvsLGpVMyGZbizE3yO6-DlLAtIxPcin_L8LDpG67NY3QHIazeKfHNX-hGKOKRo2wR7Kg3PdV0uN4Mxl6NgQ4wDhs0rFU317zp5tCfCLNCKHJnVWPEPHJK0F0PiXJxtTYawaBq_KuQZZkWWZldphdagTWFG8othAcfZ6yjwRESptOGjL1ARsGjJ8eOsYKiUEBQIj4dPXWmDomXF3Bzomhxp7A9LBS-NT338RIBnVxzNH3GjekBH1LHFkr8VlOZx-GVfCLnz2bCgLwt3WOpw02OM4_q8XpFzMJSDuwl9ACmKRzQkJGoRs5TY0KgmWxlBfMfx9F8YepxKXkp8t9pcYF4OGdX8BlHSxgGBzvXoj9KZgaudLYNq9T886q8Kwi2orK9iNBTMmGSn18qtKEBFSwuhvI_GmeKjvbSIxRBP4q9JKQzwCK_wEKKx2jvru7scpGt1FZH8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعار همبستگی میدان و خیابان در مراغه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farsna/459082" target="_blank">📅 23:46 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459081">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CxxlKuoc3Las0Bs7QAF8qHAjcIRNIsb95MJNQBEc0wS_VZMDdToGpPXQr1U_NoxKxGfl78xc2_RE3VeduwvwWifPBXcctIjZvGgWejsBYa77P1698-qexPXIKmtlyorPaal3HI-2QK8vyi2cfsccuydhbRsan0Pvrs2zABu0o_jnjSfR-Q1-Eedw5tJhtak4IGFeDyJvD5Qa59qhKz91R7en63kod08T4z5UwGHS16SVbrpwqXLX-5zqeRq33SvrkmzDrbVTlmtDHRBFYnR23lRQjJPg66c45jsfqM9xFNpc0_nuuTZBQ59f9pnPcVG6YOJWFTf9IKrhkEkc8l2_LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شنیده‌شدن صدای انفجار در جزیرۀ لارک
🔹
مردم محلی از شنیده‌شدن صدای انفجار در حوالی جزیره لارک خبر دادند.
🔹
هنوز محل دقیق و علت وقوع این انفجار مشخص نیست و پیگیری‌های خبرنگار فارس برای مشخص شدن جزئیات انفجار ادامه دارد.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود. @Farsna…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farsna/459081" target="_blank">📅 23:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459080">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2933b57941.mp4?token=ol8h_K-f9E8LQIMuju4xBge5vn5GBik3SllQsT3FTA01U0licnppjs1VuIUddpj-HCLXsWobkrM0MnHrV928khAdTOmxjn7s0a5T3lLlMUymEzlqU09ArP14CgIeG2P3NPYkoFTdLUh516ghDaZJmh7PDOCNCSstuCYAccFdwolOTgMf-GaDeGFpL7cGnFL4HMFhBLu9W-wFw3aLf2XQSLGXbytjfccNdwGgKInlEbzuyPUvgmwpICMAu9EcU9AFHqGGfUQstZBmtzVl9LiK_rX1Smo-SCbOCEoiG_P1nPzKPEVDxi1QiNbTB63UkwGNeWcvPXH_qwIA6q2E32-UFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2933b57941.mp4?token=ol8h_K-f9E8LQIMuju4xBge5vn5GBik3SllQsT3FTA01U0licnppjs1VuIUddpj-HCLXsWobkrM0MnHrV928khAdTOmxjn7s0a5T3lLlMUymEzlqU09ArP14CgIeG2P3NPYkoFTdLUh516ghDaZJmh7PDOCNCSstuCYAccFdwolOTgMf-GaDeGFpL7cGnFL4HMFhBLu9W-wFw3aLf2XQSLGXbytjfccNdwGgKInlEbzuyPUvgmwpICMAu9EcU9AFHqGGfUQstZBmtzVl9LiK_rX1Smo-SCbOCEoiG_P1nPzKPEVDxi1QiNbTB63UkwGNeWcvPXH_qwIA6q2E32-UFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شب ۱۸۳ بعثت مردم و حضور پرشور تهرانی‌ها در میدان ولی‌عصر(عج)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farsna/459080" target="_blank">📅 23:26 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459079">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7627bc0740.mp4?token=mQ7CnSFq9zAKcBg6BJL4jpuZDjQTbpZKtwUnj1gPPhajXq7pZ-Of1gY1rp4MchnVcfzp8QWotM2SoKburDmfcXqNRTqT9PBBnyvVzHL_O3xwX9FWrUx1mElTmRK1UzWPecm2C1ziaZNj6WyKdcmjroukSlL_EXpws7xZzwxCZxf595Yp_0qEPT9NlRjsLft083qR5jPtAMLNs3Vc2dsq9YuCmmfeZPsNAjT6MQ1p2WEYk8afWsniypaHmEp_szuVZBc2eiH8KIZ1Ks_SnmEyhcq5yP9XzXZlvhGW1I4wybTW0W_94G6kcpxYgNlZlTQ6H1KiGZtHaCgUSR9q8yRAJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7627bc0740.mp4?token=mQ7CnSFq9zAKcBg6BJL4jpuZDjQTbpZKtwUnj1gPPhajXq7pZ-Of1gY1rp4MchnVcfzp8QWotM2SoKburDmfcXqNRTqT9PBBnyvVzHL_O3xwX9FWrUx1mElTmRK1UzWPecm2C1ziaZNj6WyKdcmjroukSlL_EXpws7xZzwxCZxf595Yp_0qEPT9NlRjsLft083qR5jPtAMLNs3Vc2dsq9YuCmmfeZPsNAjT6MQ1p2WEYk8afWsniypaHmEp_szuVZBc2eiH8KIZ1Ks_SnmEyhcq5yP9XzXZlvhGW1I4wybTW0W_94G6kcpxYgNlZlTQ6H1KiGZtHaCgUSR9q8yRAJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
افتتاح بیش از ۴ هزار طرح در آخرین روز هفته دولت
@Farsna</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farsna/459079" target="_blank">📅 23:17 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459078">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/395013da0d.mp4?token=IDGszFWXzdwHlKNKxIkuhITrKLJeBq4fB0U1YLOGOGb4gbWD65SwwMNL1ydCpcIL2Dqd1Tpx5QrPweawJKd5fLZN2zVgIkLufM3aEBj9GTW2LQmdfQyCV5T9gQX-vv9urSIhI0l4ulxm20_AV57uA3enrTWxrUhJ6Yhhh5-k8IWDkdq9FLvlWGzHX2ZA5HLPUFYvjjSJv8v9cAPCHlKTnwXG_S4e6n9Le6px9A8-DyxvE_xS6bN6oiqi3hjPAMXYhorDeGEBWbSfjzPHYc6qYSJclzTfn5vI8SWfCPVlrqlNVHhtmfQ5CkhReux1WI5iaWP-hy7VfVupe8EAHI1bRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/395013da0d.mp4?token=IDGszFWXzdwHlKNKxIkuhITrKLJeBq4fB0U1YLOGOGb4gbWD65SwwMNL1ydCpcIL2Dqd1Tpx5QrPweawJKd5fLZN2zVgIkLufM3aEBj9GTW2LQmdfQyCV5T9gQX-vv9urSIhI0l4ulxm20_AV57uA3enrTWxrUhJ6Yhhh5-k8IWDkdq9FLvlWGzHX2ZA5HLPUFYvjjSJv8v9cAPCHlKTnwXG_S4e6n9Le6px9A8-DyxvE_xS6bN6oiqi3hjPAMXYhorDeGEBWbSfjzPHYc6qYSJclzTfn5vI8SWfCPVlrqlNVHhtmfQ5CkhReux1WI5iaWP-hy7VfVupe8EAHI1bRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر راه: سعی می‌کنیم ۳۵۰ هزار مسکن دیگر بسازیم
🔹
قولی برای  ساخت ۸۵۰ هزار مسکن تا دو سال آینده نمی‌دهم. @Farsna</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farsna/459078" target="_blank">📅 23:12 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459077">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d22ac977b.mp4?token=F5djz2YkGIwOWl_bOXrAvJEMZQizCSYL-1LG70CIauaJ20YFW6qr1wmWCK9ddwAzhRPhg9NE_V7bm1vCiu4KOxkmBOXhXV-1LWnGNVjPJA0lyY6ii5439f3ZIAy5N7BxpYXLrfeCQo5k1nNWsqho_9ys2dj5fKlnHEsKkalb82YWH-89H96T6sf0bIEWhTmpm2GE9EVd0NQPWAyDs42e1fkEE52mg1ahI1Ct4hSZG4iZJbLuXiSsjwddNg6X4EuOVM_OuxmT7zEuOWgqwrqf07_voyLrQGXQoowkm2w4e5sOYGid9JNDMnqug5g6ctwxFkXzXGbckUe62KeKGeU3HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d22ac977b.mp4?token=F5djz2YkGIwOWl_bOXrAvJEMZQizCSYL-1LG70CIauaJ20YFW6qr1wmWCK9ddwAzhRPhg9NE_V7bm1vCiu4KOxkmBOXhXV-1LWnGNVjPJA0lyY6ii5439f3ZIAy5N7BxpYXLrfeCQo5k1nNWsqho_9ys2dj5fKlnHEsKkalb82YWH-89H96T6sf0bIEWhTmpm2GE9EVd0NQPWAyDs42e1fkEE52mg1ahI1Ct4hSZG4iZJbLuXiSsjwddNg6X4EuOVM_OuxmT7zEuOWgqwrqf07_voyLrQGXQoowkm2w4e5sOYGid9JNDMnqug5g6ctwxFkXzXGbckUe62KeKGeU3HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم‌داری گنابادی‌ها در شب ۱۸۳ به عشق ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farsna/459077" target="_blank">📅 23:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459076">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">شنیده‌شدن صدای انفجار در جزیرۀ لارک
🔹
مردم محلی از شنیده‌شدن صدای انفجار در حوالی جزیره لارک خبر دادند.
🔹
هنوز محل دقیق و علت وقوع این انفجار مشخص نیست و پیگیری‌های خبرنگار فارس برای مشخص شدن جزئیات انفجار ادامه دارد.
📝
اخبار تکمیلی متعاقبا اعلام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farsna/459076" target="_blank">📅 23:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459075">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8344de3119.mp4?token=OPAZk8CScjp6c0P_3F-hCTE6PChMtN8Gwfun23JOX16zMiAAI04UQLPdzRllc1toCRvNg9A4SmPRq-MIO5Pze3Rm_wiMzeTwS7DKpHN4H__dc879rq6iDVm78osUbmaAgn-PlUxrjWul0jEpDNsMzTtHf-tqhKuyruYKn-JfnAqKDutYDWeD9adWERlAvZV-emsq19i9cYc2rk4EFeAv0XH5ye8MxNOGjOipLd2H-m8YozIfU-GWIB_1j0udPh1S6bWL48oSDLd6G6KZhHiNvZA9yuinN-WFfzjYfcI_mQBTd-8lvSCa2lvqXdBqnaDMyzfsA1FhLm7wPddFkPgncg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8344de3119.mp4?token=OPAZk8CScjp6c0P_3F-hCTE6PChMtN8Gwfun23JOX16zMiAAI04UQLPdzRllc1toCRvNg9A4SmPRq-MIO5Pze3Rm_wiMzeTwS7DKpHN4H__dc879rq6iDVm78osUbmaAgn-PlUxrjWul0jEpDNsMzTtHf-tqhKuyruYKn-JfnAqKDutYDWeD9adWERlAvZV-emsq19i9cYc2rk4EFeAv0XH5ye8MxNOGjOipLd2H-m8YozIfU-GWIB_1j0udPh1S6bWL48oSDLd6G6KZhHiNvZA9yuinN-WFfzjYfcI_mQBTd-8lvSCa2lvqXdBqnaDMyzfsA1FhLm7wPddFkPgncg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر راه: سعی می‌کنیم ۳۵۰ هزار مسکن دیگر بسازیم
🔹
قولی برای  ساخت ۸۵۰ هزار مسکن تا دو سال آینده نمی‌دهم.
@Farsna</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farsna/459075" target="_blank">📅 22:57 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459074">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85a8b48ecf.mp4?token=SXnrvhGPC3ekMmB6tbCRsttAco8QjyrwYngXhYwtrkluoeJrPIKfd9PBolwkbKb0VtjDAW2d-moHtQvhXOoSqPEfn-BfWQ2M5dm9VGd2SiU6M-o6Gu195gtgko8F2uB2DqrV-DevrFM0C4Pccw8L0yRmwUzwhO95W49qbt_IuSSCtbkdlVwEOYEDvyP-OAg6y44MK88rOg9q53wBCyr2gp7BTxpS9XYzzTtcWGkwA6Hxom1ab7ZVSrb2tn3fsLQZH4IyfFqrGRy28MFIqRVKC-4_A82DlWbOOjeR_Jt2zAy3huwKsddBYeNvkWR0_dgo0I47-sSz-vXGoMRSevFHtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85a8b48ecf.mp4?token=SXnrvhGPC3ekMmB6tbCRsttAco8QjyrwYngXhYwtrkluoeJrPIKfd9PBolwkbKb0VtjDAW2d-moHtQvhXOoSqPEfn-BfWQ2M5dm9VGd2SiU6M-o6Gu195gtgko8F2uB2DqrV-DevrFM0C4Pccw8L0yRmwUzwhO95W49qbt_IuSSCtbkdlVwEOYEDvyP-OAg6y44MK88rOg9q53wBCyr2gp7BTxpS9XYzzTtcWGkwA6Hxom1ab7ZVSrb2tn3fsLQZH4IyfFqrGRy28MFIqRVKC-4_A82DlWbOOjeR_Jt2zAy3huwKsddBYeNvkWR0_dgo0I47-sSz-vXGoMRSevFHtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت صمت: بلوک ۴۲ درصدی سهام سایپا تا آخر امسال به بخش خصوصی واگذار می شود
@Farsna</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farsna/459074" target="_blank">📅 22:47 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459073">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25999cd90c.mp4?token=W-wenqM1RSPTfluAq8AbEIsDXi1Cq7qQpgunZTD3xCMKA_YHV9D4nnjIny8aORuA7Wb5WJdcx1pNkwa0LhfjvIkK9el13FEEBYEI4SiLgLuHAdtOiQbOkHn6jB1WIfhmBdERHcrcoDKrsjnAaOI9-02NypPjJHzc8yC6rCgSaPgHtdX6-2l_eejmRr5WSKIV2oFiEDgiwpXcAuwpCqHUrOV884IL6yW2CsfvkCVKwFhPWTVAPxgAlQ279faPYXReVCyLUQjwr14h2bFTvDeX2ouZXw0w4m7LtBwOMkAWQEDWdXonO8P0s5-5cxy9wI6mjYaRMKGz_7YZe3fkPl5GIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25999cd90c.mp4?token=W-wenqM1RSPTfluAq8AbEIsDXi1Cq7qQpgunZTD3xCMKA_YHV9D4nnjIny8aORuA7Wb5WJdcx1pNkwa0LhfjvIkK9el13FEEBYEI4SiLgLuHAdtOiQbOkHn6jB1WIfhmBdERHcrcoDKrsjnAaOI9-02NypPjJHzc8yC6rCgSaPgHtdX6-2l_eejmRr5WSKIV2oFiEDgiwpXcAuwpCqHUrOV884IL6yW2CsfvkCVKwFhPWTVAPxgAlQ279faPYXReVCyLUQjwr14h2bFTvDeX2ouZXw0w4m7LtBwOMkAWQEDWdXonO8P0s5-5cxy9wI6mjYaRMKGz_7YZe3fkPl5GIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طنین ایران ایران در میدان شهید سلیمانی رفسنجان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farsna/459073" target="_blank">📅 22:46 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459066">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CKci4wPa3RJ9ppV1P7qdhtpaCc1Lpfa7QeIKpn_tb5VqZZgy6N1BeU5o7RTWjRWQkCVfdqai_wF2iiY4J7pPA4qCvz6du-C2Wh5eMQpEhQzDmOpKixw8s5bKOpQ_AL6sWa54oOUS_LVZfKI19aFiPOrlrVGBCRmM9FGZncS3ylerT0SGdTK4rQy7797oiWny_hYmLIudTwwp_26dqv6FuB4xlKTbIwNWlhCcb95D19m0utYH42B0k5w4h6-S2l7_hLlfriWBBr4QgDUn3DB5Ws5jm38gopp8fkYY5RLSvqddR792az1Kur9geDbaPqsjTZjyMXGOpeeXKN4t50Oeow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aaeCfI4AcQ3cY0qguOnra5Ab3iILxkU-6OzFvQQs7dGMXr_tylKV0IbwAdSsuKtNCgvIz6ePzMnWUx2o2BX2ErYNR-OzPMNbnXMOzkjH0dNxJrDHXKt0oUUaWHrVyGG9RIK-ZaR7Oe5NSd1JjVqBI5TFJQPTA4Em1cT2RCAOJWLmTVDae8-d9m6plJrrzQlCiygywVIf6bHX6QxORcL7rYTWpjzCC55a5vpjpPu00PlctaTBq510-oisOXr3pdnhw7Seea_0L4IVfpq9P2L1EmhYiRxj7loPZ5ravYMz-mYK_RVFb7lnmtxF9PIkl6y4Ponma_FBShpsVpcKmhUASw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LRV_52GAVX3GS6E_ExMKr1Tkiumu_Mb0shmfBH629jkpavis5pAfal8TNYGESIKaMqCGX1xXWAwUMQELqMqdZQEi5GEA92ZQKmF42kK4ACWt1XqbqyfT1MAEbFnieZHEyUE6HlXreyEm2xrJ9HeNT0HOA4gV2v7Diu_V0LwF5KP7tt5TaNGtrcxjPXrXsUsQiltZmzuSSldt3uZa5ga44hixZfJuaSTvCZAVq_jNwWVZHOC1pJu5pQE6KPZHlOuNFij5CaaooBV4EUVGG167EuAyIeZJfHsp6zplG49hJBYjA_wK5Qs_Ac5-yf0znfV3aTcCe3JOS4HCNCXk6BrIXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rfaT7opTeXsGv0UvuIn8zdaaFxfJGKOZJKsrrizbp-Vn4CxXek1aDh8KCO_B8fPtSMofiuidTQBSxfq239Vd8rExNl0HIddXq9tVECVNWe7eKgUQIgnrdleQZ5IkQt7cSzbYjpWYsZMN34nkj6F1KCuvOFJLyvkR3GBsidl-MsEZhS5kTESliVxw3bVkbnWy4xpjEUkpTgKAKceCez_dl2cg6ZHB7RzV_vq4YEwIszm7zxg7tPaWeKTCvuD7rZX5TMhqFO508zPfsanO1SY0k1v7Oah6PMbVEVvN5ev-PZCOx0VD-ZjD6tTn6K_Zku40XKLKsevcgIDlATnMuQQAsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KjQkm0Sy_1f1oljGDaK9ZTn7m5lFtykfWONQIA_vzIOQ5V-aWQzbi4l32UKZUACbFLEKHBpAOGWI2b1UivdvdKyG8dXXTe_jhO76hkvWpPaFD602rQA9vsWUMgQu1kX6JxQN3KKFw9AJxEfLk2Y6mkLpjUIxmqjsCOp2rwQUWVNK1PQqEjdD-ZV9GP8DxGf09RFhjU8JcBqEV1UzkXbqeZmQnHgkRE0Yp4t9et6elqn0nHRlZIONS9ENXeUGJdEoRQnPeI9dGrA8QnHJyRmTzZMaFjutqJh_M_txEEkvDVLaK4UxDu6zELol05RtdqhryeymRuQJz6NZ71AHNvp71g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tYSe8ZlzuvrRBlQBy0ZYQ45mFI-YAajOKdu3_KCn4JQKkFQpFBhnWOkhCjy-xsg74HSUIXQk36J4h-nvHSBqAvxGF1x6a2SM-0v7sJlPSGIWPLNa_0Zfv3AZUQtPKck4sxtZmMr2rd9X5C9r0d7Tcwt36etKY6anew8NNCnv2_u1iSW2Or61BGak258ElYwYIvpNG27Iej95XPWhnPUuz70nWQDNpE4f8W52uRpVJAUKM9ZdsAQBWmmvjEM5qJ3U1w3iw1nKeNljZWmNEmG-5-sy57T5YOCrfb2pDaEqDc9tKn93oxysxLoPi7yPwgH8pB80BkIC27FTOGg6TIJnqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dYFp2XC1IHid6ubVxFvmByTYzBPoMCr0zo4eH_bDFccUehv6v_WA1XjkYV3tY-h_rmuG6WPwy6kIyJm9KKI4cGIDWsH5D55nx2aRReyZNTdZy38Oq1UBsbOFixRrPRGAexymt6tDs_fmQrQ4WDfMibhOOkONvc5CL5h00Arm5WvwI7QbjOMb5QbqsforCWV4LYsyc0nIGh8I8G0-xlpnM4BiJYFMLCuGrY2ESBsj8JKlVqmLXofkUkLGFtPKe89D0Y0tg2SF1q5Uedp7StutPVeEltBEUkydiUKseJ_FdQnOF7DcCGv1JYIUpwCwkuqVn2n2kufTqltLHOa2tUHIXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جشن بزرگ «امت احمد(ص)» در تهران
عکس:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farsna/459066" target="_blank">📅 22:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459065">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea4f22402b.mp4?token=iBFQngbnA5OEEN5GwiVwd69P6u_9jQenozRKpQKMs-RKIqCdyFlySO-Z3CfTx7F_KXRcrR8E4sm9zG9G3mDZBv7hkpCu4LobeCeZuoCNImeWBDMFL7e78U6rD5PB5W9ddxQ4vR_OHRQqSvu4-RrECxZ9aZa4XovhA1Kxm19Gps3CXXFVrqrMtZkWoLRDfTCYI7XURKKc0c_E-Ny0ACXwwdXi96tPh8SrIOOkns3hxKInntnefWHY0O7vDZu1au_Rj-pGBPFyHvfv8suF0tAEmGKxw3L8aVAMPgEjk4--w2IQkjgVPBvYUDFKW5oUYygipbl2KUTQNQl--SG6OdpwNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea4f22402b.mp4?token=iBFQngbnA5OEEN5GwiVwd69P6u_9jQenozRKpQKMs-RKIqCdyFlySO-Z3CfTx7F_KXRcrR8E4sm9zG9G3mDZBv7hkpCu4LobeCeZuoCNImeWBDMFL7e78U6rD5PB5W9ddxQ4vR_OHRQqSvu4-RrECxZ9aZa4XovhA1Kxm19Gps3CXXFVrqrMtZkWoLRDfTCYI7XURKKc0c_E-Ny0ACXwwdXi96tPh8SrIOOkns3hxKInntnefWHY0O7vDZu1au_Rj-pGBPFyHvfv8suF0tAEmGKxw3L8aVAMPgEjk4--w2IQkjgVPBvYUDFKW5oUYygipbl2KUTQNQl--SG6OdpwNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قائم مقام حزب اعتماد ملی: نباید به خاطر اخم غرب از تنگۀ هرمز عقب‌نشینی کنیم
🔹
به این زودی فراموش نکنیم چه کسانی حامی اسنپ‌بک شدند؟ همین اروپایی‌ها. مگر این کشورها حقوق بشر را می‌شناسند؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/459065" target="_blank">📅 22:33 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459064">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/defe8accac.mp4?token=RptTB-ncphBDDkvH-bULKNFUQMunMWYtR9g-l99mt4Ity5wsvvwNqQYazreC7iTDh_gTaJTM1P_sDAD818UcoM-sP9WCKd6P9psnG6f0HL_qGVzZi-ZPQh-RPk9YGoTXM72hJRKNAN2CvEnh0QD-NB_yFPtBKw-oJcbkmj-kj7ZiIKsqsUFV4d9l7DWBJp70VMbZ7nnFXp3A2DaGy3dN4igQsuYBvTTSJzLkOf6Yif4Co5ovvHN1Zo3k2TK2PHkuUTJaiW0K4vsket4SRlD5RpAAzS7Y50jEtTB3_mXBrHRlSMvuTxxqnrwmNrCQ-CHuSCgsC-Qa0q98gAiCfBoYdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/defe8accac.mp4?token=RptTB-ncphBDDkvH-bULKNFUQMunMWYtR9g-l99mt4Ity5wsvvwNqQYazreC7iTDh_gTaJTM1P_sDAD818UcoM-sP9WCKd6P9psnG6f0HL_qGVzZi-ZPQh-RPk9YGoTXM72hJRKNAN2CvEnh0QD-NB_yFPtBKw-oJcbkmj-kj7ZiIKsqsUFV4d9l7DWBJp70VMbZ7nnFXp3A2DaGy3dN4igQsuYBvTTSJzLkOf6Yif4Co5ovvHN1Zo3k2TK2PHkuUTJaiW0K4vsket4SRlD5RpAAzS7Y50jEtTB3_mXBrHRlSMvuTxxqnrwmNrCQ-CHuSCgsC-Qa0q98gAiCfBoYdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رجوم، پهپاد کوچک یمنی‌ها که مزدوران سعودی را تحت رصد و ضربه قرار می‌دهد
@Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/459064" target="_blank">📅 22:15 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459063">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45df4384b4.mp4?token=vawLB7bIRJFPvo7ckdZRvxx_g8UEcv0vRZmIvDHLDIG1Ffyb8mK-nY-h99xTAfIB2CcJk_7N5RN7prf9So9SIlHlqojAash3Cge0-KDoPdk3mHIeXaY6gZ-Tiw3KiTzNo75sv7cle7c3XFoVI8K-hPdjJHmZdIqc8NcD8BJz66kQAE8-GDltwCJZhIlwjI4B9P679kojIJtHh5gzjS7U6HxonMUss12DqLDuj8Y1Z2qkdHcmGGOVvNtylBPFVx0ruS80B2kQzJvLdq0e5XVEbwR4INSxZUiLf6_LnfvFJ8hZo1Jesv4mAtuDcO3Wgrfk2rXZr3QYdglEVKH7eFMX7oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45df4384b4.mp4?token=vawLB7bIRJFPvo7ckdZRvxx_g8UEcv0vRZmIvDHLDIG1Ffyb8mK-nY-h99xTAfIB2CcJk_7N5RN7prf9So9SIlHlqojAash3Cge0-KDoPdk3mHIeXaY6gZ-Tiw3KiTzNo75sv7cle7c3XFoVI8K-hPdjJHmZdIqc8NcD8BJz66kQAE8-GDltwCJZhIlwjI4B9P679kojIJtHh5gzjS7U6HxonMUss12DqLDuj8Y1Z2qkdHcmGGOVvNtylBPFVx0ruS80B2kQzJvLdq0e5XVEbwR4INSxZUiLf6_LnfvFJ8hZo1Jesv4mAtuDcO3Wgrfk2rXZr3QYdglEVKH7eFMX7oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گفت‌وگوی دخترانه دربارۀ پیامبر رحمت(ص)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/459063" target="_blank">📅 22:07 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459062">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🎥
رئیس سازمان اداری و استخدامی: بساط واسطه‌ها در موضوع نیروهای شرکتی برچیده می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/459062" target="_blank">📅 22:04 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459061">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔹
شبکه آب شرب روستای اسلام‌آباد علیا شهرستان صحنه استان کرمانشاه به دلیل مشکلات ناشی از فرسودگی و شکستگی خطوط انتقال آب در وضعیت بدی قرار دارد. چندین سال است مردم روستا با مشکلات شبکه آب مواجه‌اند و موضوع بارها از طریق دهیاری و شورای روستا پیگیری و گزارش شده، اما متأسفانه تاکنون نتیجه مطلوبی حاصل نشده است.
🔹
طرح تعویض خودروی فرسوده واقعا ظلم در حق قشر ضعیف هست. دولت اگر می‌خواهد کمک کند، ماشین فرسوده را تحویل بگیرد در عوض خودرو صفر با قیمت سال‌های قبل تحویل بدهد.
🔹
در صورت امکان در مورد معوقات فروردین و اردیبهشت ماه بازنشستگان تأمین اجتماعی که هنوز پرداخت نشده در کانال خبری خود مطلبی ارائه بفرمایید.
🔹
امسال خیلی از خانواده‌ها به‌خاطر افزایش زیاد شهریه مدارس پولی و احتمال غیرحضوری بودن کلاس‌ها، به سمت مدارس دولتی رفتند. از آن طرف تازه در مردادماه به مدارس دولتی گفتند کلاس‌هایتان را زیاد حذف کنید و ثبت‌نامی‌های جدید یا غیرمحدوده را نپذیرید. آن‌ها هم شروع کردند به بیرون کردن بچه‌هایی که خیالشان از ثبت‌نام راحت بود. حالا بچه‌های سرگردان و خانواده‌های بی‌پناه یا باید ۱۵۰ تا ۲۰۰ میلیون تومان پول بدهند (و این شهریه هر سال بیشتر می‌شود) یا بچه را به مدرسه نفرستند، چون هیچ‌جا ثبت‌نامش نکرده‌اند.
🔹
از تهران داریم می‌رویم زاهدان. در استان کرمان نه کارت‌های شخصی کار می‌کند و نه کارت جایگاه وجود دارد. چرا باید برای استان‌های جنوبی محدودیت قائل شوند در حالی که در استان‌های شمالی و تهران کارت‌های سوخت همه‌جا هست و مشکلی وجود ندارد؟ تو مسیر هم اصلاً کارت سوخت نیست. ما با مشکل بنزین مواجه شدیم و ماشین را همان‌جا با خانواده گذاشتیم و مجبور شدیم بنزین ۲ میلیون تومانی بزنیم. آمدیم زاهدان هم همین‌طور است؛ نه کارت‌های خودمان کار می‌کند و نه کارت جایگاه وجود دارد.
🔹
لطفا پیگیری کنید. بیمه تامین اجتماعی نیروهای قرارداد مدت معین و قرارداد مدت موقت مجتمع گاز پارس جنوبی قطع شده است و الان نزدیک یک ماه است که مشکلات ناشی از عدم بیمه بودن پیدا کرده‌اند خصوصا در زمینه پزشکی.
🔹
آب شرب روستای قلعه چنعان شهرستان کارون (استان خوزستان) در وضعیت خیلی بدی قرار دارد. لطفا پیگیری کنید.
🔹
ما از مال‌باختگان ۱۲ تعاونی مسکن در تبریز هستیم که در سال ۱۳۸۲ خریدار زمین‌های تعاونی شهید مدنی تبریز به تعداد ۱۵۰۰ نفر بودیم. متأسفانه با گذشت ۲۴ سال، علی‌رغم مراجعه به محاکم قضایی، استانداری و مسکن و شهرسازی، هنوز موفق به تحویل زمین‌های خود از تعاونی شهید مدنی تبریز نشده‌ایم. خواهشمند است صدای ما را به گوش مسئولین برسانید.
🔹
من یک شهروند اهل استان سیستان و بلوچستان هستم. متأسفانه هیچ جایگاهی به ما بنزین نمی‌دهد. به خدا کارت سوخت خودمان هم کفاف نمی‌دهد. هیچ مسئولی هم پیگیر نیست. جایگاه‌داران می‌گویند کارت پمپ بنزین داریم ولی نمی‌دهیم.
🔹
اینکه قرار است ماشین‌های زیر ۸۴ از تهران حذف شوند و سهمیه بنزین نگیرند یعنی چه؟ خیلی از مردم در این گرانی پول ندارند ماشین بخرند و با همان کار می‌کنند. مگر با ۴۰۰ میلیون وام می‌شود ماشین خرید؟ پولی نداریم بگذاریم روی آن ۴۰۰ میلیون که ماشین بخریم. لطفاً قانونش را با این وضعیت بد اقتصادی تصویب نکنید. از کجا بیاوریم قسط ۴۰۰ میلیون را بدهیم؟
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/459061" target="_blank">📅 22:02 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459060">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HVO-jgKRnb41-TkUAA44ttsKDx0YrI3E-CWWNVKFKmxYMYN1Ets5PxOeI2fbDOR8yi1ZoHBYuiqEnDRHj596b8ca3-1uJbork8p0GcE5q6QQG4nHo-6rqZdL6fJ5ClcV-YhABHg5dkwo8xIJ7MJoJ_OimoX44szdvy7nxzDG9tih1trKu7GE6MR9qDsaTJyTmjPMPMLiISs_rn723pq5aDIBnY838LdG3P1CD9Pfq2hKYKglRicCg9SOZTaVWeeSPhq-fyaqCTnE2MRumgOFJHGQK3TSOt6Sz7SdRwCh6jUsYExUvJBPD14bTMKih2nejHGlHlp7Uj2qna7i0qliZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هدف قرارگرفتن یک نفتکش در نزدیکی عمان
🔹
سازمان عملیات دریایی انگلیس: یک نفتکش روز گذشته هنگام عبور از تنگۀ هرمز در فاصله ۱۲ مایلی بندر الخصب عمان مورد اصابت شیئی نامشخص قرار گرفته است. @Farsna</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/farsna/459060" target="_blank">📅 21:59 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459059">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">رویارویی کشتی‌های جنگی ترکیه و اسرائیل در دریای مدیترانه
🔹
شبکه کان اسرائیل به نقل از منابع آگاه گزارش داد که کشتی‌های جنگی ترکیه در دریای مدیترانه به کشتی‌های نیروی دریایی اسرائیل نزدیک شده و برای آنها مسیرهای دریایی تعیین کرده‌اند.
🔹
به دنبال این حادثه، نیروی دریایی اسرائیل سطح آمادگی خود را در دریای مدیترانه افزایش داده تا برای هر گونه تحول احتمالی آماده باشد.
🔸
جزئیات بیشتری دربارهٔ محل دقیق این رویارویی و زمان وقوع آن منتشر نشده است.
@Farsan
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/459059" target="_blank">📅 21:45 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459058">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6fb79d721.mp4?token=ECsbDreZ03J4Hdn1pkm8DrBuvR301IuUeB9Umtp71NrV-IVBj7KwlHbiX7-tX1UkERM20XE5roAk3g3BSHuCoxDPCYqgKjMt9Z8_QNU2q4OA3krA-frYv3EDtbNf98bVoIpNhLZYTb2alJkvylM8WEXCIjMUFfihg4o8ZPdm231US46AkizgzNG7_wGydpsNUbjy765TaGfN5i8KpimUhSfi9ArYeiMSgXgYDKWCgCfd6OZX-LmQLtVgJ9CkSKcd16y2YnV4ZRFddAR0u03pLlREihKTA-qd_DLSHAwSrkSE-k7-pO9m5L3sDlmjUmiMsD_ZVxtcWCGZW9EwbuAAKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6fb79d721.mp4?token=ECsbDreZ03J4Hdn1pkm8DrBuvR301IuUeB9Umtp71NrV-IVBj7KwlHbiX7-tX1UkERM20XE5roAk3g3BSHuCoxDPCYqgKjMt9Z8_QNU2q4OA3krA-frYv3EDtbNf98bVoIpNhLZYTb2alJkvylM8WEXCIjMUFfihg4o8ZPdm231US46AkizgzNG7_wGydpsNUbjy765TaGfN5i8KpimUhSfi9ArYeiMSgXgYDKWCgCfd6OZX-LmQLtVgJ9CkSKcd16y2YnV4ZRFddAR0u03pLlREihKTA-qd_DLSHAwSrkSE-k7-pO9m5L3sDlmjUmiMsD_ZVxtcWCGZW9EwbuAAKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان اداری و استخدامی: بساط واسطه‌ها در موضوع نیروهای شرکتی برچیده می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/459058" target="_blank">📅 21:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459057">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/boc97_-bjawSrn_ReB_vwhf1rSJ5H7w9Xzxfe6S1K1IIsa690PMDWA_F8RE5sX0Aavm14py1_Op29WnCGFEtIOkWlCAyM4HOEaOpCTxV0oHXslNzTRD37pwo2g51dfOGrELbiqYfSMrjIZ82CoqpFp0DfqkU00AKixxH8SZdheBmWhcDvHsyUtXFQg_LevkSaSo8AC_gbQBYY6ZP25Lh3FTeC2SFRyU9FhnpyHGy3m1Y0lYfo7IbCHEymO5n5vqd-G3RDjjwaAlW2K5_FWD_Iq4eNVMipwh5ngYFFccE_ZB5UlGJ1w897kk29yalNZTUnfAx2B6eAJc3bWSsRNtaBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیۀ فعالان رسانه‌ای در لبیک به رهنمودهای رهبر معظم انقلاب
🔹
فعالان رسانه و فضای مجازی کشور در لبیک به رهنمودهای رهبر معظم انقلاب اسلامی بیانیه‌ای منتشر کردند.
🔹
پیام امیدبخش رهبر معظم انقلاب اسلامی به مناسبت هفته دولت، برای ما اهالی رسانه فراتر از یک پیام تقویمی و در حقیقت نقشه‌راهی روشن در میانه جنگ ترکیبی و وجودی با دشمنان این مرزوبوم است.
🔹
ما فعالان عرصه اندیشه و رسانه، با گرامی‌داشت مجاهدت‌های خادمان ملت و یاد شهیدان والامقام دولت به‌ویژه شهیدان رجایی، باهنر و رئیسی این رهنمودها را جان‌مایه حرکت خود قرار داده.
🔹
هم‌پیمان می‌شویم که در این برهه خطیر با بازآرایی صفوف فکری، بازوی توانمند جهاد تبیین و تقویت‌کننده پایه‌های انسجام ملی باشیم.
🔗
ادامه متن بیانیه و اسامی امضا کنندگان را
اینجا
بخوانید.
@farsnart</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/459057" target="_blank">📅 21:37 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459055">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0528b651c5.mp4?token=CwE9ezgb-DshB9zPdxoTjPb2nWfqSW2hfLvv9TXp_4AruDmfniwEZm7fqTuF0d7wn3s97SUnirruX3CnAS8glh_z2ifkwlPRFSDkSdxXV_Bmw0ziDPLxwtYS2VpO0rY3-IYXAWfUT-6XvM-15-8gEEHq0tepYtfx93z-erfZvpQwts1ksit8JiWBDlP6HrXHoeLfk0sTK6xo8WWozZaZb4U35xjMQMdA-Fhx0hBiehjIUmH2UNIdbHuGDqmjDIFLy0t1Sudt279flC42dSxXbzJFTwNzir8jgHy8jUQlozxm3x5fiQlqYdwvroktU9XsKvNHbj42mSVX47NPCmzUsDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0528b651c5.mp4?token=CwE9ezgb-DshB9zPdxoTjPb2nWfqSW2hfLvv9TXp_4AruDmfniwEZm7fqTuF0d7wn3s97SUnirruX3CnAS8glh_z2ifkwlPRFSDkSdxXV_Bmw0ziDPLxwtYS2VpO0rY3-IYXAWfUT-6XvM-15-8gEEHq0tepYtfx93z-erfZvpQwts1ksit8JiWBDlP6HrXHoeLfk0sTK6xo8WWozZaZb4U35xjMQMdA-Fhx0hBiehjIUmH2UNIdbHuGDqmjDIFLy0t1Sudt279flC42dSxXbzJFTwNzir8jgHy8jUQlozxm3x5fiQlqYdwvroktU9XsKvNHbj42mSVX47NPCmzUsDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج ۱۸۳ حضور مردم بسطام استان سمنان در میدان اقتدار
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/459055" target="_blank">📅 21:33 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459054">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KuySauF09PMFa_1e2WiSGk43AcrzVlgjVtENv4Rd-BE06ArC1VQDEjBdajuUvdiNzTCnllc4gveXtnFDX46Ex3nDQjDvILLxgbT_FzUhNDWWYxgz8e0jhBSD29uqKfXWfW-5f1usf6yio3VMyoRVGc9DFlYwTX58ffBX__LxajAM8qdCo4E7dZwlxB619FfPH3by6aMhiptsyudt7-5_2nL_iSRm0RfkrsN0Um-bCT_oFdNcVi8MVXLruSOFicmwopc_GpxxT_xzK6_HzeJXe8KngOdQfgNTS6nSR_2P-loy1XJcUMskczMMhIKWotmF3z2RI3GP19tFvgc3NPVKow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابوترابی‌فرد: فعالان سیاسی نقش جدی‌تری در حفظ انسجام ملی ایفا کنند
🔹
امام‌جمعه موقت تهران: رهبر معظم انقلاب طی چند ماه گذشته پیام‌های متعددی داشته‌اند که به نظر بنده فصل مشترک همه این پیام‌ها، تأکید و توصیه جدی بر ضرورت وحدت و انسجام بوده است.
🔹
احزاب و فعالان سیاسی وظیفه دارند در این حوزه نقش‌آفرینی جدی‌تری داشته باشند؛ نهادهای حوزوی و دانشگاهی نیز نقش محوری دارند و باید پیشگام وحدت و انسجام ملی و تحکیم رابطه دولت و ملت باشند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/459054" target="_blank">📅 21:27 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459053">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gRqjMVfoYom_TSR-SQXT1Ge1qLAro4Ohjh9sBrbj58mUI3f4z7Iws8hz3nxYNlpTBJUZWTFx888ww6C79xCr0HPjuEFEba2mURLw25bK-sYYCDgWHmDYIJXqdvDyFEAVh9fGAxVfW6iaio9nRQtZgSjoS2NHJNQb_7uSkCM8umhyd4JMyD_7uUGP3Nu9d_JAPaJ7v3HwCrvi7mnSzK9vOeeqecVKYDxeRVp_YMbL1-qEAOYVchVbdwVAhoQkpgNZP-hjmW5UrNCLxgzqIJH4y73fTaAVx5LT8C61-_LdS2DDCgm12JumFLn3Ca36r2SqcNKJBaf4y5Iwwx3DwOojTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سازمان اطلاعات سپاه: دشمنِ مستاصل از مقاومت ۲۰۰روزه ایرانیان، «فرسایش ثبات و تاب‌آوری ملی از مسیر جنگ روانی» را دنبال میکند.
🔹
پاسخ مردم ایران روشن و مبتنی بر اخلال در توان فرماندهی دشمن، ضربه به شبکه همکار تروریستها و مقابله با تخریبگران ثبات و وحدت است؛ اراده‌ای که دشمن پیش‌تر قدرت آن را دیده است.
@Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/459053" target="_blank">📅 21:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459052">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/27a0efc341.mp4?token=VZxZCYJNUC1NEsn2eUmQnvBzzp3kxUf-W-RKB-yYrTx4NcjNpHottIO11sWpPk4SxiQ8AwEkj7ezde5ZBIczlQpKYqJGogw_BFEIerNdeaZ2W9G9p_7a0QJPnAAMpfWenn-7a3K1TQ02P_YbnFSFvYFFfK98mKS5XguK2xH91EP0WIrfSsILDaYmbZimHxLm8sWQ3YcuQQWWW61TC_3RCnd8-kKbawqMb64cDjmrjwGqWSHtBgqHMvfLv8-MmJ6_BN_HoByzGlrR87HwBaSCz5BDF_zvyUVPW6ftKeKfCXsgGTO1v4ESTeSLczRD-CUM16aDVUsbCSVTRzDq6HCjN4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/27a0efc341.mp4?token=VZxZCYJNUC1NEsn2eUmQnvBzzp3kxUf-W-RKB-yYrTx4NcjNpHottIO11sWpPk4SxiQ8AwEkj7ezde5ZBIczlQpKYqJGogw_BFEIerNdeaZ2W9G9p_7a0QJPnAAMpfWenn-7a3K1TQ02P_YbnFSFvYFFfK98mKS5XguK2xH91EP0WIrfSsILDaYmbZimHxLm8sWQ3YcuQQWWW61TC_3RCnd8-kKbawqMb64cDjmrjwGqWSHtBgqHMvfLv8-MmJ6_BN_HoByzGlrR87HwBaSCz5BDF_zvyUVPW6ftKeKfCXsgGTO1v4ESTeSLczRD-CUM16aDVUsbCSVTRzDq6HCjN4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تیراندازی پشتِ تیراندازی؛ این بار در نیوجرسی آمریکا
🔹
در پی تیراندازی در یک گردهمایی در نیوجرسی ۱۰ نفر هدف گلوله قرار گرفته‌اند که ۲ نفر از آن‌ها کشته شده‌اند.
🔹
انگیزه مظنون‌ها از این تیراندازی تاکنون اعلام نشده است.
🔸
ساعاتی قبل هم در یک حادثه تیراندازی کور در نزدیکی «واشنگتن پارک» در شهر شیکاگو ایالت ایلینوی آمریکا، دست‌کم هشت نفر هدف گلوله قرار گرفتند و زخمی شدند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/farsna/459052" target="_blank">📅 20:57 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459051">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">توقیف ۲ میلیون لیتر گازوئیل قاچاق در آب‌های خلیج فارس
🔹
فرمانده مرزبانی فراجا: مرزبانان پایگاه دریابانی بندرعباس، بعد از اطلاع از انتقال سوخت قاچاق به یک کشتی خارجی، مانع انتقال ۲ میلیون لیتر گازوییل به این کشتی شدند.
🔹
۶ نفر از متهمان اصلی این شبکه قاچاق دستگیر و به مراجع قضایی تحویل داده شدند.
@Farsna</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/459051" target="_blank">📅 20:49 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459044">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n-VIY1_dZGXnHSsLnaIlwZFRGS2wi25mjkUx74JDdgvG_rOwsowXIqBCDeSpiLH5xnehDGrom_A00wHwCbvYizdsuuDVAMZ4rNJZRxq5rud3s6N8JvNIf6maOFjLrH3-ULCYWu9oiiwvyukDP8XrwEDP46tPvzvU7NEy6AD4P4iyx0JO5qQCkBAU9qww0qM2Ze-R98-IKVYaQWaagRdBRyokUS2-Yf2NUNju6JsyYaWmsB9qBnJdyo2bXOWTVTZnOPy6_fbG4phwIuv5B9YsqmNk7zsC9TVz81WY6o5ArYYTwdQ-s7Y7cfLtrGb0VB4j3Yo5-p0cMI0P8b-FJWpz7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KhkA3wfDV3Gu7Opnw4vYdNCmoAu5hcv66PV10ibZ63QTsln2HxSXpExLFswTFHsBjSvYlhC_UXpSSfAIPqxLzcKGvxX_pBxEY6X2FGFbud_ZWKerhgz5I5wG3o9s6jsTKqkTUdZA20v3KueMO5Ta_ptJC_cm7ZEf9H1GC5Q0VdF1-ELRTMZRjhEGCVlt6ppgPAgPOZTyCyqaR92H3viwpaGNzorRjB4dUhneC0RZYf20VUNOhYDfmKjxwBuu7CZJL-DGzRDYtwwzW3sc8lStbHENAroLasAjSzyY0UCYqMSLZc04aSkZfRsnc0I0NOzeHxqPTI5ib8pGn9Uk7SrMBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nhlUA-QHZJZa-EgjxawXANWPuI3E7Ru2TXQXB4ANJ8p4RXLccpEVBVxK9voRlmjn2oY-DObgorg49zMac82AQbgy-Is0SAzkvFQ8m3C8yPLpEgIC_V1cmEVP1y6pikcLNvDjGP7pKdeMrFm6EjB50U1G1uacJ16rnGA43HaZVX7jSDzTwf_rry9ZnYF5nL5tG2GRXfs0T4OKs1BpovjCU88H-kyWlf81w5j2o4pPvmTOhw_4eiZTIG1cOs4ryZE3U-yE1B-nPdLwWexookzKrihajTildqQ344VmsGa9y8V-5fyssNFXyHJWDfbjuElAOO5Ng_3L3X5WI4o3fYbtYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IfuW4EDIthkqH_R5qtJa2BjSPiHiBqlmctfHzVwsbJp76oQ4YTGMKFS5KWlGlbppxrTovqqaO7bTRkJBXGCNH55KQCR6JxlI3Ram6S7aw5q_XxKEL4Jg5CjHdfZh2f9AREzyj7isM2zuIvoP_AFDN_DP5gnrL3u3wmdeknYXJZpwlAeun_Z6aiHk7BX01-ZnARnVpA0W4UI2zueasiQlU9zQulp-VciRv-KyL4P7fdoqffS-mC2m0KRCE3-W7wrW_VrFdesJvTbFbjbRz91kOCRIkg_W-Z1wIav9ihW3Hww2aiJa5jN08RUhvViw0RXVye8EeSmkKg2EMYj8KVMv_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EGx23ZC2xjwu7g2bFdlrx9QWDkEVL4Wod-dP6zM-lgaC2ucqsyKIPL3jfOgK6uWxtUcFEVuOZ2rMr0EnRhRdJLda-WhcWKOLczxdWOVOtTcoQ5pLAEMsQXUN-e1y-pyAvP-95kD_Z383wC5FONyp_qnJFsfyOzWItz0HZwumhbFQFJcPzhD3R8TcmZGp_MBfaNyE-bu48BWFxMPn8bUSb3FQF0q9prfOZyia3uEobv_54oxCen9zENWilg_9RSUdv34pFve5m7yGLfCRLv9z9ZkHuO6n6cusHpdQwNbWAslryqDiFjbj5KxSiHWgCpKLDrZY98uH0pDBAJXp648ziA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YiGMJOo32Ibwgs1RzoMq2Ivn_R5wt3SWi1t5PPHEfJB8cf2ddCU0aaq3hVufjTVR-IZwHjZnVXX_cKP1dji03WNHqFED4KRqaxmUysntQlh3XqoIFBz_KItbS_4b8IWv_U-UvqW_m46kWlViXuewVy_cf_kEuo-us3jn7KHHzmTSO7oL6Bl4xB5zrJoJZqniGI1Ha7XOsxrOfpb7Q9jiukq6v49rAPKdO9Pycz8tvWU1tKyPJUeWSjhfcGK89xADECLbY61ha0ErsyzaZJNwu6usRV-vd1Z493Mb5rskr-myLh31URjyWoBqd_nkvhwGM4QdpbDShhH8eyQJlxMvnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qep7qANuwV22l-H_M68CiZRw4JT6fSHWhgqXae12HvCjCfn0T2cLEf9mgpvZgiLHc5aiF_b9Em8QrVEikzffkWnvM0G-eBu3lMWEF7siKGamKuIxs5gyyDAsJ0lqu8liYsnzHiJYd9xYJKdqfgDo-hiAcxLyPNk3lrktd9d7SUrt2OvvcLKDqn13XMotLgMJUT2WE1a2qePUdtaJ5YN7nuEoLNdhnfzqBz0Mb7zTqZqAhCTxpzOTKgMOLO_8c3kkut-asapYM34-LGYdmtWILhdk3bc4NDh_5I88xMf-aIhDHTLXHx-7QPzbcF8IUjaCi6wScrkqzoWCtZKTIXohPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جشن امت احمد(ص) در کرمانشاه
عکس:
بهروز احمدی
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/459044" target="_blank">📅 20:49 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459043">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b2524a388.mp4?token=UH6TO3kNVTsKy9wDCDZa3_jOG4lOHdYxZ3Jbl_v9BXDO0gekDXylLm4DCqaLt3khf419K1Esl-MXeE38Z7KyVRGRys3DGR-BVFZz7zd44f1Y5iz4P5iRQGWKKjMYgmnwIj3GGkAph2KQnCyMfzFxsa9MFJoX4Uj6ahrXskOJX0zOF8bBS0WWlV_ykc0sEvJrhCrIbfEAKeBi9kB3oQq6M7hZASbwlk62QSAZbM8u90IYvG0na3-rw8JvO6wBjj7OumkNFLXt_EvJWH-Avi5TrSgNSY_nPkfMZFscMVWe7i6Ydl2MQsQHSCZqXujZobj4sQRs7NIwJcW6uN5O7EXa2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b2524a388.mp4?token=UH6TO3kNVTsKy9wDCDZa3_jOG4lOHdYxZ3Jbl_v9BXDO0gekDXylLm4DCqaLt3khf419K1Esl-MXeE38Z7KyVRGRys3DGR-BVFZz7zd44f1Y5iz4P5iRQGWKKjMYgmnwIj3GGkAph2KQnCyMfzFxsa9MFJoX4Uj6ahrXskOJX0zOF8bBS0WWlV_ykc0sEvJrhCrIbfEAKeBi9kB3oQq6M7hZASbwlk62QSAZbM8u90IYvG0na3-rw8JvO6wBjj7OumkNFLXt_EvJWH-Avi5TrSgNSY_nPkfMZFscMVWe7i6Ydl2MQsQHSCZqXujZobj4sQRs7NIwJcW6uN5O7EXa2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیرعامل شرکت پخش فرآورده‌های نفتی: دوگانه‌سوز سازی خودروها در دو سال اخیر  ۴۶ درصد افزایش یافته است
.
@Farsna</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farsna/459043" target="_blank">📅 20:46 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459042">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13bfa5919a.mp4?token=tc_8wZyOysQOM76PXuNq_IJjp24xt4TXNXw48c-z2QEbpOsFekFSyxcTtuM478EOOFB7ami2_g4D332n8jSulz1iQsEDrZm_ovY0HymiMT738j65jddK8V2sZ0FfqZbhC6onorfBL8TQdYUWQBc--ZLCrbUzSG2ZmtqUNnjWL6QxxRhn87-PCw13wfGs3sNRqoUqFvwTN8FYfaCogjSnmn3PTnnxQ5tCgBMb2L7l7ARq5E7qNYpfNIuqYAyee_EEv51fLP9xYOiIY46XsIrj20L0-xhJDw_dZaNHh614JaAbu1TwPnop5_to8cYZOqwmDYpZ7rmRJB7yn8eKjWaN5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13bfa5919a.mp4?token=tc_8wZyOysQOM76PXuNq_IJjp24xt4TXNXw48c-z2QEbpOsFekFSyxcTtuM478EOOFB7ami2_g4D332n8jSulz1iQsEDrZm_ovY0HymiMT738j65jddK8V2sZ0FfqZbhC6onorfBL8TQdYUWQBc--ZLCrbUzSG2ZmtqUNnjWL6QxxRhn87-PCw13wfGs3sNRqoUqFvwTN8FYfaCogjSnmn3PTnnxQ5tCgBMb2L7l7ARq5E7qNYpfNIuqYAyee_EEv51fLP9xYOiIY46XsIrj20L0-xhJDw_dZaNHh614JaAbu1TwPnop5_to8cYZOqwmDYpZ7rmRJB7yn8eKjWaN5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون امور مجلس رئیس‌جمهور: کمترین میزان استیضاح و تغییرات کابینه در دو سال اول دولت را داشتیم  @Farsna</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/farsna/459042" target="_blank">📅 20:43 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459041">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NbXjhxWHOyluDxRc8OhyWakPwQkR-CcZcyUQmdalr1g8klL-0kCTpTo6Mkb7s7aeWVFIiUH5bizNF3ZTphfw07ob5xzqgwK2sz_izhvJHknUFcmfBbQmdX_ILvu2hv4cp0xtVN3ja7Yfe8l2fX5t3C3iAOh229NCZX1Ac4X_WPGj39Pq0T1M9DlHp0dcVQG9SofbNQS1N7PlpSgfvSVhZt2v3an8sKirWz79GwLCx1GYcjO_GLLSDbTKJ_xTO8NbxudYGD8JqAi3urbFu0bDH_bZk5F3uNKYZZ1aOaKUaK1yDOKL7k7tjjuGakX0uVq9JvjbsCdWNUACUfIWTKI_SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کنوانسیون خزر و زنگزور دو لبۀ قیچی علیه ایران
🔹
مدت‌هاست ترکیه و آذربایجان با چراغ سبز آمریکا، کریدور زنگزور و کریدور میانی را پیش می‌برند تا منافع ایران را از معادلات ترانزیت اوراسیا حذف کنند و با بازگشت کنوانسیون خزر به مجلس، میدان نبرد ژئوپلیتیک و تجاری امروز در دریای کاسپین است.
🔹
دولت چهاردهم در شرایطی پرونده رژیم حقوقی دریای خزر (کنوانسیون 2018 آکتائو) را به مجلس فرستاده که نقشه کریدوری منطقه دستخوش تحولاتی اساسی شده و رقابت هر روز شدت می‌گیرد.
🔹
پروژه‌هایی مانند کریدور میانی (ترانس‌خزر) و کریدور موسوم به زنگزور که با حمایت ترکیه و جمهوری آذربایجان و با چراغ سبز ایالات متحده  با عنوان کریدور TRIPP دنبال می‌شوند، در تلاش هستند شبکه‌ای از مسیرهای حمل‌ونقل را شکل دهند که از شمال و شمال‌غرب ایران عبور نمی‌کند و عملا ایران را دور می‌زنند.
🔹
نتیجه این تحولات، شکل‌گیری کریدورهایی است که ایران را از کریدورهای شرق-غرب حذف می‌کند. این مسئله فقط کاهش درآمدهای ترانزیتی نیست؛ بلکه تضعیف جایگاه ژئوپلیتیکی ایران به عنوان پل ارتباطی بین شرق و غرب است.
🔹
تصمیم‌گیری درباره کنوانسیون خزر، یک انتخاب صرفاً حقوقی نیست؛ بلکه یک تصمیم ژئوپلیتیک است که می‌تواند آینده ۱۰۰ساله ایران را در منطقه رقم بزند.
🔹
در چنین شرایطی، دریای کاسپین به کانون معادلات تبدیل شده است. سؤال اساسی این است که آیا صرف تعیین چارچوب حقوقی، بدون تضمین سهم ایران از اقتصاد و ترانزیت خزر، کافی است؟
🔗
پاسخ این سوال کلیدی را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/farsna/459041" target="_blank">📅 20:32 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459040">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4949575f84.mp4?token=fMFpYgcDlyMILV1e-XGs5J8uZPXeKI_cX3uFQ3oXerl57RCEOleCsJNNWRTNQHgaHPrNpFRi25LgrjHORHrr8OPrH0O_maCIISUxm57Nsj6KsOF9zTk1DPN1Z8KnOzcKKKacHnctW3HvsFB0W7PslQQITp23PtL0vwGIEGVp_OJAkRiSIwsmEjGlH41GB2A0Omai0kREruSKN-l0Jp1Mod_aEqa0KbyEDBPa_HWxoLNFD8De_VbMMjdD-QfdL2K35A4VP-WW-FSC2jUlcnBB0_3sSoYVdaVXJt9K1AkibKbL0G8642ZhThDv5v4_mL8Chvez1b54eA0VTPRtFR8m3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4949575f84.mp4?token=fMFpYgcDlyMILV1e-XGs5J8uZPXeKI_cX3uFQ3oXerl57RCEOleCsJNNWRTNQHgaHPrNpFRi25LgrjHORHrr8OPrH0O_maCIISUxm57Nsj6KsOF9zTk1DPN1Z8KnOzcKKKacHnctW3HvsFB0W7PslQQITp23PtL0vwGIEGVp_OJAkRiSIwsmEjGlH41GB2A0Omai0kREruSKN-l0Jp1Mod_aEqa0KbyEDBPa_HWxoLNFD8De_VbMMjdD-QfdL2K35A4VP-WW-FSC2jUlcnBB0_3sSoYVdaVXJt9K1AkibKbL0G8642ZhThDv5v4_mL8Chvez1b54eA0VTPRtFR8m3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امکان ضربۀ مستقیم به اقتصاد آمریکا و لزوم دریافت غرامت از کشورهایی که مبدأ حمله به ایران بودند از زبان کارشناس مسائل منطقه‌ای
@Farsna</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/farsna/459040" target="_blank">📅 20:28 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459039">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n511R92lz99A6f7W8kQ5_ABIZlbAQ0zvBI6d5eOyP-z-vp4FS7FiI_NNR7F8DIEVuORazTQPhDFQXfYWz8hQe9saa9SxRtNQqup4NW8PSevN-OdPaoXTWhquHln9UuHS88ZAUF3UTPDHD1Ptfn3uCpzv4YDKQ8YlZUMwSXg82u02wfzBM4FC7SdTp4jupS1YHGLPm08gX_WYUnqQP_ANn1bI0ovSBO6WyHFP9b8RRnjyxahmDdbGbLDHRbpHUcn3HrAzfLkdYuGRTmFiTwzUIshClD-N6wHpBSxDTdksoxRZ_v64fHXsl_eih_jGSdg_k5TQlOr18fi2huazVgslRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمایت دبیرکل سازمان بدر از بیانیۀ گروه‌های مقاومت عراق
🔹
هادی العامری: گروه‎های مقاومت به شرط تحقق حاکمیت کامل ملی به سازماندهی سلاح در دست دولت باور دارند.
🔸
کتائب سیدالشهداء عراق امروز در بیانیه‌ای شروط ۱۰ گانه‌ای برای انحصار سلاح در دست دولت این کشور اعلام…</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/farsna/459039" target="_blank">📅 20:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459034">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/abCnoj8xgcirqXjaldW-eNILMOuxZ7Wbk7PZf8CbpcTRwE0S5lScXnoKWtpkrx_ZC1_tpPEzkMa5pQg6BC7MZkbU_YSejHYe-5S3R6mk2IXeVYx53X1PQnqZ-aclTH3FkuaDY-8LZWVqPKm2FygYWo-kFbcakFK7trTwr2BtfmtJ4PIR3fgKFfIjbq_F_UvufJJm0h6BQ_Ca6ENM2KGFXSxqK9RCUOFknQypgCIcymT6crYBWZoWsEUAgViDiqwIxaKCom7NKsgk_QfkovwH6dZ8LFQ-IMI6TAx5DTCdy-eJ1BUe4147q5tt3PK8JI9D7lFLPtJYFUwnsLy0wy8fLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lzU0YoSwQc6CNGX1xjs0iJvj7UN6AUeRIzrIq9iC9E2NI3XSwf8X0HmHSbn70OettabWBoeZiV8XvMPAr6lEFYI_46JztPvx3yPA-zxZ-nnxLh01torfzOtYCaBembogdTjP7iNgZUEHBfHRFEYyHp731HKYc5cp_Dp9WL2QpT8Quaicx1I8irHjwnailgWl0UM1-uN8b_gHcshH72JYf8_l5qgy-HgH_bBGB_mh0jy0PwnM_BwvJNKeELYjBe7NxhcdSzCDHvace3FL15pqy-iIPEW0cXqgAPr-_rf1kz946YOjyjCCo_yw5Sm2SNiii5WxgwWJnMOhp7s5VPaQ_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NIhnJ0BGsLY_jSfDQGK8K4VxXpy-U6GbMkeoWmWcpPT2Z32BfH_t3fn1IAtiNlCMseCiwDWEwzhDwJ9lzSLm4HfPVeQ7gO7_Ucj7Wk3UIn-JRwGgkyCuRrcz62vn7pngXVyXaGX91KJlLbkQZ3U6YzC7lCNTcd2wRrycaPjCdHUssjKbVo_Zcch2VF6PNWFtbRGMAUvkk9Nhi2DdJMUZsW4EYqg56x6JKP4YE6J9NnFdeB6BhrpeBWO2sA_UJc25fEk5apDLgcmyeY-zoU9mVg73szgV0ljpH5N7ZcGwbt5e_UrbyduSpraENPuFqI0QmxgQ8S5z3dpnONOhsBwt_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kg8RR5A9U3_34P3X9Kf1JvtiRGJziVz0eDLJYWv8ehqhQwKe14LGI6L0vo_5GUKfEze87R5LAjXv2HoqZfSQPOItH0kE3Yj0ZdQan_aBsbfCM_vHczxlxN4dWYTQcLbw8vVap_PzZ4DFOEZ6SReudCRnA-aONP4Sj6QxqLYAaJGYfJdZr1rIFc1vaVKA4Gmz_K89bV7v-Do-tQvlAbFaQ7NDRNAKzXDv--qNj8cjb-MzJO_vgqIMsT4VX4y3AS4Ebc0vJo8AkXZEPshaJRPzuiiEaxeUmbpLQ5pg3fkb5yl_5r8Ph-07PgsJ78nt4CvtK7cRLhpiLEg06y6KvNM43A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nIlUDj0g5eEdbq0QO_eXCgXhP0oKECzIPdk51Ls1lp7oBZOydrLNN2aRNY5kxkpmLyn5tyS1eXHcS1qKkiSZ0ZobovZMIVsn9kAuA8awm6lZqGCxXGrHwOQ5zmEUnnoTYs8iQOhg2qkKlle03ub7QclK1BMNoqyumoUMznGLcE7mjvr6dt1XGBulELLPyhqBMWJjiV7gvzWWIZeSbZwMR5jTWBNh-GHeFMCx29Fmpq4PI7VVOpVF48sdxT93-hQnqpSVwJABsuKdGRGNplYmukpo6fFnvp3rIG_RfqeAaUACKIIze2Fxxjy11rZwgWoLeDxoZpn6IKgMkV75bghFFw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جشن امت احمد(ص) در بندرعباس
عکس :
عماد یگانه دوست
@Farsna</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/farsna/459034" target="_blank">📅 20:11 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459033">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VzYdhl2OCnUsy900F70SymzfAa2CrxEi5fYiNwUhdzTDwQh8DrM76f0DD_PqU9xn7JugfQnC84i8miH-57ytCSM1LZJvIs4pbVoKXIYLx7JHfCLX9tI6B6rgARGRaHQLHqoHLQHMKNNCoy_vZ98GqyX5YWc-Gm0Jr7zFWiqPqVdH61BfY7Ap6opvwB8Nigyqis3QLbyRPqQIs9t05-FteyFOhpySopGMNr1WDx4vi0rkK-3j0vbpeepZ74oAP3lqIxcuc3KQqP4TYA3tj2jW135uD3UM5tI3LQX4jeSeziPKnIvXAjUkJlCmYYHT8aKm6ejrhAkHT9nc-eRCiklq0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هدف قرارگرفتن یک نفتکش در نزدیکی عمان
🔹
سازمان عملیات دریایی انگلیس: یک نفتکش روز گذشته هنگام عبور از تنگۀ هرمز در فاصله ۱۲ مایلی بندر الخصب عمان مورد اصابت شیئی نامشخص قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farsna/459033" target="_blank">📅 20:05 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459032">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc097c7ed4.mp4?token=IAAFjKeucG8d8KEKZSdkQQ0QPnH5hLqkkM3ZNlMc1ZZwD_LQL_Ghbci_G97yvPbS2E2Qrf_MPmcODjwEpPsHsM1F3BjxSMiyd-4IGjM9UCD2l6BX4GYxbdkC5B_NxM6zo8IW0EWUfrL2Qpma_YzuXS6c3lN_1DhvQl7sPEnt3uE6VhnHPuqOxuaBx1pB9V9lfxFqSi3YlGY4ur8-dpHyeH2acl_AYMLXnb9wSqvHzKaMs48CKzNEvfa8XQFE_p5nBLSJhCsKGJ6EpotYiT6eBaq89UAMJuI93_V1abG7FhUBPnre2-aOSUwhCyTBBJTF0ar1xZ79a1d6ft0R9SQ_Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc097c7ed4.mp4?token=IAAFjKeucG8d8KEKZSdkQQ0QPnH5hLqkkM3ZNlMc1ZZwD_LQL_Ghbci_G97yvPbS2E2Qrf_MPmcODjwEpPsHsM1F3BjxSMiyd-4IGjM9UCD2l6BX4GYxbdkC5B_NxM6zo8IW0EWUfrL2Qpma_YzuXS6c3lN_1DhvQl7sPEnt3uE6VhnHPuqOxuaBx1pB9V9lfxFqSi3YlGY4ur8-dpHyeH2acl_AYMLXnb9wSqvHzKaMs48CKzNEvfa8XQFE_p5nBLSJhCsKGJ6EpotYiT6eBaq89UAMJuI93_V1abG7FhUBPnre2-aOSUwhCyTBBJTF0ar1xZ79a1d6ft0R9SQ_Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون امور مجلس رئیس‌جمهور: کمترین میزان استیضاح و تغییرات کابینه در دو سال اول دولت را داشتیم
@Farsna</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/farsna/459032" target="_blank">📅 19:57 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-459031">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68d4388b5a.mp4?token=sKlNuUjAYRnHEuDwqvxk4qZ0jvBhxqdatU0G-hZkjUU4QO6pKQPfoANHy0RJFsPtSC3oXZobGz2mK9XM1UH3zx2qv5skudsZJgZyNn6ybxztkmqRQ2I3Kz59tO6wPCoVIenktvjbHGb_C5IfIO5B-l6sIBp9JlsLiZgEee_bGA7mBrjypGogmGu6CRnO9J9Nlh7FcbYR2jFKpijQSKNgWT_BHQdlpSXXBnhTTChlENun3A_7Kyv7qZNxk42xOMtWwvHjIZc-hjskdnWhEp4wRhA9fP7z8bJN6ImQ1Sltt5mfYb6oauWupEzqROAc-REa9Dom1cchD_A-6aDLXgaBUhohGbQITg9p7EaRAux6PCla5E-wwZlEVnnl8oFIJxotzztiKXcYL0MyS3l-qSxHMjfYQzo6qihrh0Bm82t0dS4I1MVDGhLmDhXVaDkjl3YtpjsOyTZHiTdNrjCj58f2bZvWHPnG3G2cAlHmpnNSeUs1dw9Ee3AgZ7LmoqsDEPKIBQYYExrFpkoSJ-rWsHk61v4gWP4Va4jbo9vjmv7lWVmxNT6KbVZ4yhHne_6sBebSQFVG7hcPqvzL5Y3cxshDxQVjI7UQLd2f02Tr9NtxL8XJwcLSgvRjl_LLe5Kfavw3JjoK5OuZVPov0f-AJrnS_J53HO4B9u44bckHqc6yJoI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68d4388b5a.mp4?token=sKlNuUjAYRnHEuDwqvxk4qZ0jvBhxqdatU0G-hZkjUU4QO6pKQPfoANHy0RJFsPtSC3oXZobGz2mK9XM1UH3zx2qv5skudsZJgZyNn6ybxztkmqRQ2I3Kz59tO6wPCoVIenktvjbHGb_C5IfIO5B-l6sIBp9JlsLiZgEee_bGA7mBrjypGogmGu6CRnO9J9Nlh7FcbYR2jFKpijQSKNgWT_BHQdlpSXXBnhTTChlENun3A_7Kyv7qZNxk42xOMtWwvHjIZc-hjskdnWhEp4wRhA9fP7z8bJN6ImQ1Sltt5mfYb6oauWupEzqROAc-REa9Dom1cchD_A-6aDLXgaBUhohGbQITg9p7EaRAux6PCla5E-wwZlEVnnl8oFIJxotzztiKXcYL0MyS3l-qSxHMjfYQzo6qihrh0Bm82t0dS4I1MVDGhLmDhXVaDkjl3YtpjsOyTZHiTdNrjCj58f2bZvWHPnG3G2cAlHmpnNSeUs1dw9Ee3AgZ7LmoqsDEPKIBQYYExrFpkoSJ-rWsHk61v4gWP4Va4jbo9vjmv7lWVmxNT6KbVZ4yhHne_6sBebSQFVG7hcPqvzL5Y3cxshDxQVjI7UQLd2f02Tr9NtxL8XJwcLSgvRjl_LLe5Kfavw3JjoK5OuZVPov0f-AJrnS_J53HO4B9u44bckHqc6yJoI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از حضور پرشور مردم در جشن امت احمد در تهران  @Farsns - Link</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/farsna/459031" target="_blank">📅 19:47 · 08 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
