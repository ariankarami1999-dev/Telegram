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
<img src="https://cdn4.telesco.pe/file/qLhLmHA8OLXraenVcJUmytpExJKMH8newebthXSX8tIjEnzP6QW2pU2pOHXKeYM_l8-IbnaqMArVnH779FbVc-358vSHVVto8dXiOJpE9FiHoUiHC8mLwHnct6KT1x9GnwGogZBTHXIBjGi0qHDQtdcKq0-VKRjbgMJgs7u6Oj-SYmp-nSvQT6Pn11h2Dfx_QS8y-Er9pPr_Oi2-cIDz9vQAgH2iPa0byVHs9H0xgTAv8TCNybYDNNhQhMagss1hK810mOOzMJr09dChbMSpVcBmGJc51nzAPTlN8lTg5ol9IijeO9rP-exxzT6c_Hs3vk-2KJ7555Xl7Mwb-DgWng.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 972K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-28 21:48:15</div>
<hr>

<div class="tg-post" id="msg-148255">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
ترامپ: نیروی هوش مصنوعی [در ارتش آمریکا] تشکیل می‌دهم
🔴
رئیس‌جمهور آمریکا: درحال تشکیل نیروی هوش مصنوعی هستم؛ درست مانند «نیروی فضایی» که در دوره اول ریاست‌جمهوری‌ام تشکیل دادم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/alonews/148255" target="_blank">📅 21:40 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148254">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
کانال ۱۴ اسرائیل : ترکیه به طور رسمی مجوز فعالیت بانک ملی ایران را در استانبول لغو کرده است. این تصمیم، عملاً تمام فعالیت‌های این بانک را در کشور به حالت تعلیق درآورده است، از جمله تمام شعب آن در شهرهای استانبول، آنکارا و ازمیر.
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/alonews/148254" target="_blank">📅 21:40 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148253">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
به گزارش شبکه i24NEWS، بنیامین نتانیاهو، نخست‌وزیر اسرائیل، قبل از سخنرانی خود در مجمع عمومی سازمان ملل، در شهر نیویورک فرود نخواهد آمد.
🔴
به جای آن، او در یک پایگاه نظامی خارج از شهر به زمین خواهد نشست و سپس به منهتن و مقر سازمان ملل سفر خواهد کرد، جایی که قرار است روز پنجشنبه ساعت 14:00 به وقت محلی سخنرانی کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/148253" target="_blank">📅 21:35 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148252">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/025ae7d2df.mp4?token=jJAP2aX3ALaxunkW1Vkz39NQGlbhaknGHsBcGOdyKVE9-n7riax362PyNOjXibETtBXNy-KoLknyT9qaS_-ZwZtZCl1yyfWVnXIzmaUYTYFNZ0M7GaR_b2BOLVSLpnSqC_ExFck6e-QzVxHS_HGxgTKXoW7DdvJ6dr15CFlDaRA0BOWa6m6_2YecVfixe3DEZ2Aji8Kt3N3MaMLn2wVxO4X2QdUQGgkPIyYSue1wbwi6T3n25PNo20cq4XQIMIUpirtE2zqmRw23XXCmbh96MqzOQFno3e8S_t99aIebx71nC5mVCiycWBgS9KlePMnOEkWcMkTDq7zZYSPSbyE3pIzwaTGWCogcV5bccFSUNLyjMR3W0IsCWoyYwFrluavDcuIgqfdfmvOXKJ76GWLEs_bFVF7CDk9GzOfhB8WIlzwiNjlWziilTQDwV05bNcDSV6kHwbUq-PBANwR0hi0ipyN9W21igkdbb6DTvxA4AkQEB1OO2AEVxvQAXyZFzMup7JufoZFxgNmRlMTFkFg6bhdQDEbUaq7Htkipa4mcHD0Bw8K8AjXF5WXneUBCCavBtrzUxNUPn5TE2QvcbGuBpqb96gMi0bsQpKMzmIlCAQPjwI3LZ9vtW2_-283q_q47tT7z6-Vn-wdTRDrnmxSPD7-vX_EFc_fO6vKJ9SgyEZs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/025ae7d2df.mp4?token=jJAP2aX3ALaxunkW1Vkz39NQGlbhaknGHsBcGOdyKVE9-n7riax362PyNOjXibETtBXNy-KoLknyT9qaS_-ZwZtZCl1yyfWVnXIzmaUYTYFNZ0M7GaR_b2BOLVSLpnSqC_ExFck6e-QzVxHS_HGxgTKXoW7DdvJ6dr15CFlDaRA0BOWa6m6_2YecVfixe3DEZ2Aji8Kt3N3MaMLn2wVxO4X2QdUQGgkPIyYSue1wbwi6T3n25PNo20cq4XQIMIUpirtE2zqmRw23XXCmbh96MqzOQFno3e8S_t99aIebx71nC5mVCiycWBgS9KlePMnOEkWcMkTDq7zZYSPSbyE3pIzwaTGWCogcV5bccFSUNLyjMR3W0IsCWoyYwFrluavDcuIgqfdfmvOXKJ76GWLEs_bFVF7CDk9GzOfhB8WIlzwiNjlWziilTQDwV05bNcDSV6kHwbUq-PBANwR0hi0ipyN9W21igkdbb6DTvxA4AkQEB1OO2AEVxvQAXyZFzMup7JufoZFxgNmRlMTFkFg6bhdQDEbUaq7Htkipa4mcHD0Bw8K8AjXF5WXneUBCCavBtrzUxNUPn5TE2QvcbGuBpqb96gMi0bsQpKMzmIlCAQPjwI3LZ9vtW2_-283q_q47tT7z6-Vn-wdTRDrnmxSPD7-vX_EFc_fO6vKJ9SgyEZs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل (IDF) در ادامه تحرکات نظامی خود در جنوب لبنان، اقدام به تخریب منازل  و زمین‌های واقع در شهرک «منصوری» با بلدوزر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/148252" target="_blank">📅 21:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148251">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/plQqZv4Edh2bho4RjQdONrYWLHBEamkEv-LZCMF0YC-MoOf6W0HT7b_ir4T3jFNGgj47LfeaIOLmL9hFeE0_LTeWGTC8wChQayLfEv4x8XEQlzPQJgh7OIhWpjUrCncOJiPGC8-CqkGb9r0i_grpakw697ez0QqJzUrMOg89mxPKZwKJt5ViAUF-jhhzRb0ugpW9-r2LUTv8VyaS_NGHz3pnxhl8mTQDmAjwT0Mb-LYUucuzHY6icueVzgUr-JPA8nFTTMElxQD8gbKPlb6fFR7xAgQuWzo8p4EB4WkzyLGaMuB0AsRokyhJNWh7CjEraKV9D_y3mTzjCe5QmmBR_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث سوشال: متأسفانه، دادگاه عالی ایالات متحده از شجاعت برای بزرگ کردن دوباره آمریکا محروم بوده است.
🔴
در طول ۶ ماه گذشته، با تصمیمات معیوب، سیاسی و احمقانه خود در مورد تعرفه‌ها و شهروندی حق‌الولادت، آن‌ها هزاران میلیارد دلار به ایالات متحده آمریکا خسارت وارد کرده‌اند و برای همیشه روشی که مردم از طریق آن شهروند کشور بزرگ ما می‌شوند را تخریب کرده‌اند.
🔴
این فصلی غم‌انگیز در زندگی و دوران آمریکا بوده است، اما ما پیروز خواهیم شد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/148251" target="_blank">📅 21:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148250">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daafee079a.mp4?token=VV4nx9QQvwMGD-W2HzL05DW7BubQMUgWiktN4tbjY6JCXqOhoBnnEHSGaVxIoGH1R5XXmh_WG1FOErjpntFvYo7VtOQUD2v-vcxCNX7DHPAITxivuLBmzXb_KArbKvo6LQ5xuyLC5A4S9BlVFveSgTEe6shlhv5gTZwy917zsWSDaJE8pcPfDUHZzEXO0cEfRG4m5RGx3LokblnXKLDIDF-67mvw6TzzxfWz2IpsWvqewlb9NVmN6GDjIcXkuPM-dp-oUZM3i0rpdB9eACL21zM_AzEum8JhDlqEu-Ksboy7ALcR4pFYUBWwQG66mpl2xnj813N_OJjoiWrW1_yotiyJceruwbesd6FW7xK0RK7kNoLqOUEKYucveXEmLRODhEjjKFG6nZojvVSVoL65CoCrkeApqKIhcfTqrXREknnf3S3rqq6fpH46JJSV93hOnJH0G-5ZtZZyLe3S_-k3WeBC5KOimAGWorDLRRiWaK9_5AbMRlUBdKGhKi4jgITYdpJqHyxrP5Hxo5Q84dHBDVfvutuz5ibn1SKZGOdl7YHWmhSlB7rzL_5HlhEpgKWGn1dgf85kEf-BELM-tZicwoKHWfgkm-Xlmn0hdlQ2etg_7HoBK2YDol6RK-mW8rulR7628aoo25WvTMfzk6JG9CJCOOiUc7Teasz6RlRD8GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daafee079a.mp4?token=VV4nx9QQvwMGD-W2HzL05DW7BubQMUgWiktN4tbjY6JCXqOhoBnnEHSGaVxIoGH1R5XXmh_WG1FOErjpntFvYo7VtOQUD2v-vcxCNX7DHPAITxivuLBmzXb_KArbKvo6LQ5xuyLC5A4S9BlVFveSgTEe6shlhv5gTZwy917zsWSDaJE8pcPfDUHZzEXO0cEfRG4m5RGx3LokblnXKLDIDF-67mvw6TzzxfWz2IpsWvqewlb9NVmN6GDjIcXkuPM-dp-oUZM3i0rpdB9eACL21zM_AzEum8JhDlqEu-Ksboy7ALcR4pFYUBWwQG66mpl2xnj813N_OJjoiWrW1_yotiyJceruwbesd6FW7xK0RK7kNoLqOUEKYucveXEmLRODhEjjKFG6nZojvVSVoL65CoCrkeApqKIhcfTqrXREknnf3S3rqq6fpH46JJSV93hOnJH0G-5ZtZZyLe3S_-k3WeBC5KOimAGWorDLRRiWaK9_5AbMRlUBdKGhKi4jgITYdpJqHyxrP5Hxo5Q84dHBDVfvutuz5ibn1SKZGOdl7YHWmhSlB7rzL_5HlhEpgKWGn1dgf85kEf-BELM-tZicwoKHWfgkm-Xlmn0hdlQ2etg_7HoBK2YDol6RK-mW8rulR7628aoo25WvTMfzk6JG9CJCOOiUc7Teasz6RlRD8GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش سوزی در یک فروشگاه درپی حمله موشکی روسیه به شهر دنیپرو اوکراین
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/148250" target="_blank">📅 21:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148249">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
فوری/ساعاتی پیش عربستان سعودی رسماً از پاکستان و ترکیه خواسته است تا پس از حمله به فرودگاه بین‌المللی ریاض،
پیمان دفاعی مکه را فعال کنند و اقدام نظامی علیه حوثی‌های یمن را فوراً آغاز کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/148249" target="_blank">📅 21:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148248">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
وزیر کشور پاکستان فردا به ایران سفر می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/148248" target="_blank">📅 20:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148247">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1367899db.mp4?token=vL_zWd21t6kFGcZM5Lp3jRmbvrTEACdu7c8f5PGh5lusJ1FXJB2zTCfmWWHus1pDd--clkdBqCTBHoFfU8eRi46MHeFzn-9Q58jeqUR1afQ6GsHNld9vY2agb7Q5-XDTj97mzaExgdossCVgj7k90E21_RzmICiQhtiSQur7iMOzdD3b4AWpn9gO6UK1nHPC5mc09InRdiVx_R-QGAeJOtZK4NZz6M-U-1iKCZ-EuRNXLqJRL61_j_ezq5ROxeiVdWIY9aBglyWjI9OzkQJ7XvYCkXe7mUbn3qM64J6mUblYBlKBI7wwKGcCXk32zJ23zHFKdFqF5CfgPjziXY3RUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1367899db.mp4?token=vL_zWd21t6kFGcZM5Lp3jRmbvrTEACdu7c8f5PGh5lusJ1FXJB2zTCfmWWHus1pDd--clkdBqCTBHoFfU8eRi46MHeFzn-9Q58jeqUR1afQ6GsHNld9vY2agb7Q5-XDTj97mzaExgdossCVgj7k90E21_RzmICiQhtiSQur7iMOzdD3b4AWpn9gO6UK1nHPC5mc09InRdiVx_R-QGAeJOtZK4NZz6M-U-1iKCZ-EuRNXLqJRL61_j_ezq5ROxeiVdWIY9aBglyWjI9OzkQJ7XvYCkXe7mUbn3qM64J6mUblYBlKBI7wwKGcCXk32zJ23zHFKdFqF5CfgPjziXY3RUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ساجده سلیمانی، مجری شبکه یک:
آقای جبلی میگن ۷۰ درصد مردم صداوسیما رو دنبال میکنن
والا من ۵ سال تو شبکه یک مجری بودم وقتی میرفتم بیرون جز یه مشت پیرمرد و پیرزن که صبح برای نماز بلند میشدن و تلویزیون میدیدن دیگه کسی منو نمیشناخت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/148247" target="_blank">📅 20:35 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148245">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‌
👈
سخنگوی وزارت خارجه: سفر وزیر کشور پاکستان به تهران دربارۀ روابط دوجانبۀ ایران و پاکستان خواهد بود و قرار بر تبادل پیام خاصی دربارۀ میانجی‌گری نیست.
🔴
شروط ما مبنای مذاکرات بود و آمریکا آنها را نقض کرد با این شرایط نمی‌شود از پایان جنگ صحبت کرد
🔴
ایران و عمان درخصوص تعیین مسیر امن تردد در تنگه هرمز به تفاهم رسیدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/148245" target="_blank">📅 20:28 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148244">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YnDOetuTimbIw4agZhvSxgG-WeS1Fr8c3A_p56VnHWxprsdhk40a7H3pgZ3gcBBZNI60rvjeDUvXgUAPW-7hxDFqXIDutOyd_Ty6y9RuW3vC0Kd-rATMMUEINjam5WP_pkiFYNK8aFjl_vLDkSpXt8XGgsKRnktvBrilvCv8moJFFYwqPzalxQEp8xTqwCL1Ut1zIqioZo67WSQssKaLTFrrd_aOiDu4AC0jcDRABgahMpqbkVNWafKI-FeEA27Q8H3H6Zonsq2N9hFRljsdoMqe6BEUktkBwwrWYRLTYCfyabmcuOnr0WlXxFbHb-sZChuqQMdn5PU2_JJtMvnhkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر وایرال شده یه خانم تو دورهمی دیروز
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/148244" target="_blank">📅 20:21 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148243">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
کانال ۱۳ اسرائیل:
قطر شروط تهران برای پایان جنگ را به آمریکا منتقل کرده و ایران اکنون منتظر واکنش دونالد ترامپ است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/148243" target="_blank">📅 20:17 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148242">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">دلار و طلا تا کجا بالا میره
⁉️
🚫
پاسخ عجیب هوش مصنوعی
👇
https://t.me/+cs85WnZxgpM1NjRk
https://t.me/+cs85WnZxgpM1NjRk</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/148242" target="_blank">📅 20:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148240">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
هشدار سفارت چین به شهروندان خود در عربستان
🔴
سفارت چین در عربستان سعودی اطلاعیه اضطراری صادر کرد و از شهروندان چینی و شرکت‌های تحت حمایت چین در این کشور خواست تا اقدامات ایمنی را تقویت کنند و بلافاصله پس از دریافت هشدارهای امنیتی از سوی  مقامات محلی، به پناهگاه بروند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/148240" target="_blank">📅 20:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148238">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YZDDVgQRC-KZbKmxEFvqB7PM3nAegaImD-4M0IhYXx8AOQriZIyFblN9JhtppFuesNIk-FO-o9BZcsVrb0EOFXZWOOwJ2jrDHliJeAJZVISCfxBiYJDfLBa6kULxU5ZXnjvRA4w8scW7pmmpic_40BZyG2Ux965xPn51Uu8Dz1ax3-oMT_oEHCbxhpNiqYrgjTnQLd-7P-YgCr9lz2VTSq_ydpwlcmJkI5064BsGL5IJr1WvFS1uz4eSegu61MeGZBCuI46FYx0q0ph7Yn3QIYNpVrew3tNwJ5coACIigOivewlp75h5fUWy1VBzuCscFoxN1H4VowYci7mDGsOyzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mzPqDRU47SNic257HB1_alTUmwZDvUaEz0i3VsXGlM4ySjcdwU5FMrQQYCz4el60ncWBzhm6fDVwC_QHvv9QJN8jv8iQQPZCecbvk7PKsB16fPaZG4nzt8uNN1fDpXYX9bEPODtW5IWhgtzYtBzqdi0t1AeQcjpQg7c3qPjhTBpie7LqdgxP-L7GhddXOI_kyD0ePHaU3V6Jh41PVhkwq5YuM9jTibUssMJkFczjeEdG7bIYKxAic4m_wdyPKjl0Q0z-lfWz0w3TFhVrOsbc9E8g_zT0s3rdBw8IqA02UQkRcV6i52i__7uHJqJ87U5VffC5HB6XN8cKoXnZxx3TmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
قیمت امروز انواع محصولات سایپا و ایران‌خودرو تو بازار آزاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/148238" target="_blank">📅 19:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148237">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
نایب‌رئیس کمیسیون امنیت ملی: عبور کابل‌ها از تنگه هرمز هم منوط به مجوز ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/alonews/148237" target="_blank">📅 19:48 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148236">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
نتانیاهو: دو سال پیش، نصرالله هنوز در پناهگاه خود بود. حالا اون‌کجاست؟
🔴
سنوار کجاست؟ ضیف کجاست؟ هنیه کجاست؟
🔴
و ما چه کاری با خامنه‌ای کردیم؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/148236" target="_blank">📅 19:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148235">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
ساعت کاری جدید ادارات از اول مهر: از ۸ تا ۱۳
‏
🔴
رئیس سازمان اداری و استخدامی کشور در بخشنامه‌ای ساعت کاری دستگاه‌های اجرایی را از ابتدای مهر تا پایان سال جاری، از ساعت ۸ تا ۱۳ تعیین کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/148235" target="_blank">📅 19:41 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148234">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">‏
👈
محسن رضایی: ما خواهان پایان جنگ بین عربستان سعودی و یمن هستیم و من معتقدم یمنی‌ها نیز خواهان توافق با عربستان سعودی هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/148234" target="_blank">📅 19:35 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148233">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی، دبیر شورای عالی امنیت ملی: ما با میانجی قطری که شرایط ما را با هدف توقف جنگ به واشنگتن منتقل کرد، در تماس هستیم و منتظر پاسخ رئیس‌جمهور آمریکا هستیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/148233" target="_blank">📅 19:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148232">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALn9dpzSFY59LxqSJ1mjAtiUbPrH9t5gM6TaPsfu-piiR758aBBAejmxssYyB5nuNef0J_lT8k_k80e4J0s-yRlHmShEth3Y2ZjdjPtHbbyoF5fnhiKr1Cksz52In0ygKSYFMS_cuSXO3CrA4b1Xe-hHDEJrSGyj-v1yMcEfyz3WhKqW9Y4Nbn6zlMA-kHd4POEGUFO13tcr3CEffdXTT2EYAg4NOtyrhSd6W4PQOSaxouXRTTLF2aZDPgRXZ-7QyyZCr09-XbApumLwFvXDLX-NlWAe-y5UHY43OVzSIuLIECxGCDSP1GcP8cX8QuMEmu8gPTwKxtG-iGYHR4A4iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ماشین تارا 3.5 میلیارد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/148232" target="_blank">📅 19:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148231">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qogMSTC8iOLM01v7AuJPaB6gGLI5qTXfzZlc8eGeqSNrFj3uq416B6YBx2esrU-9brlPZGk7jkCxK2nUSBVmJVyVQrUHXRyyF7p8vbLyQ3koLutkUJn5_xdMJ4XITk14QvWxTEZPoj9HueuwAy3DFh2NPBM3aXhrIrj5QngxTEzhEma_gD4cFH0MAsAlxt2sFCy96iyLUZVCv_hfNqpOHrnkwijeDAfWBYAfpGlJbQftvM206IrwiqGoPcE7WuskOQWEa90zYIFMwqQGA17JzV-msNVHDC8gIu9o4nuRHLA2UKGFtBAF8aheTu2MRxOM37huatNpE_3A9D0ipWKJlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کوبا در خاموشی سراسری فرو رفت
🔴
شبکه برق کوبا به‌دلیل نقص در خطوط انتقال فشارقوی از کار افتاد و میلیون‌ها نفر بدون برق ماندند؛ تلاش‌ها برای احیای تدریجی شبکه آغاز شده و برق برخی مناطق و بیمارستان‌های هاوانا وصل شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/148231" target="_blank">📅 19:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148230">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V3De9_wJe7SF2VMMqG2ad4Ii_kUmgxjVO-zhkGYoyzN1w7nbDEJRg4zAcPPga05G2h4k5LdNccbi9fuFx47KVvRBJLwFiS6s0JRHRtKus7bigWwmfiPQ2Wd5Xv7gd7pHqlMtO8GWpu93AbZvFRM-mjZ4gAoosGdwlRNrnRYV9RQTWDKF27MGZ0B3Ldewf8j3jxL2EsijIcdKN0mkbzEmqLVjKIwSwL5VHbtho6z02uRiCL6w7STC0Us2eSHvTGXLYTMRyc8sk9AWoOyVQgM_mnnXiIOi_5Moq3KZAPM7aqkDePayRBZ3WxMdtcXLNYYoqyTrfYuOe91b-vzsHwRp4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ نظرسنجی‌ای در تروث سوشال برای تغییر نام هوش مصنوعی به «هوش برتر (SI)، هوش افراطی (EI) یا هوش معظم (SI)» منتشر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/148230" target="_blank">📅 19:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148229">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
گاردین: بحران سوخت در فرانسه در حال وخیم‌تر شدن است، زیرا جنگ در ایران باعث اختلال در عرضه انرژی شده است. در حال حاضر، ۱۱ درصد از پمپ بنزین‌ها کمبود بنزین یا گازوئیل را گزارش می‌دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/148229" target="_blank">📅 19:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148228">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
فیلد مارشال رضایی: برآوردها و محاسبات رئیس جمهور آمریکا در مورد ایران اشتباه بوده و جنگ توسط نتانیاهو آغاز شده است.‌‌
🔴
به نفع واشنگتن است که شرایط ما برای خروج از جنگ را بپذیرد و تهدیدهای ترامپ نتیجه ای نخواهد داشت و ما آماده یک جنگ سرنوشت ساز هستیم.‌‌ …</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/alonews/148228" target="_blank">📅 19:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148227">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
پولیتیکو نیز اعلام کرد که خبرنگارانش در روز شنبه از ورود به محوطه کاخ سفید منع شدند، پس از آنکه ترامپ تصمیم گرفت این رسانه را همراه با سی‌ان‌ان و ام‌اس‌ان‌او از ورود به مجموعه کاخ سفید منع کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/148227" target="_blank">📅 19:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148226">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">ویدیو وایرال شده از ارزش پول ایران
ادم نمیدونه بخنده یا گریه کنه..
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/148226" target="_blank">📅 19:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148225">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
فیلد مارشال رضایی: برآوردها و محاسبات رئیس جمهور آمریکا در مورد ایران اشتباه بوده و جنگ توسط نتانیاهو آغاز شده است.‌‌
🔴
به نفع واشنگتن است که شرایط ما برای خروج از جنگ را بپذیرد و تهدیدهای ترامپ نتیجه ای نخواهد داشت و ما آماده یک جنگ سرنوشت ساز هستیم.‌‌
🔴
ما نقاط ضعف ارتش آمریکا را می دانیم و بیش از گذشته برای مقابله با حملات هوایی آن آمادگی داریم.‌‌
🔴
به این باور رسیده ایم که استراتژی خود را در قبال واشنگتن پس از خروج از یادداشت تفاهم تغییر دهیم.‌‌
🔴
اخیراً یک موشک ضد کشتی را در نزدیکی یک ناو هواپیمابر آمریکایی آزمایش کردیم.‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/alonews/148225" target="_blank">📅 18:52 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148224">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
حمله هوایی نیروی هوایی پادشاهی عربستان به مواضع انصارالله/حوثی در جبهه شرقی تعز، یمن غربی.
🔴
این جنگنده‌های نیروی هوایی عربستان از پایگاه هوایی ملک فهد در طائف، عربستان غربی، به پرواز درآمدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/148224" target="_blank">📅 18:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148223">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
پیت هگستث، وزیر جنگ: برای پیروزی، به رهبران کشنده‌ای نیاز داریم که بدانند چگونه پیروز شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/148223" target="_blank">📅 18:37 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148222">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed6cbcc478.mp4?token=XEc0Hx66khmALQc1lKH0E227CSAgJao6me2tuxlbZMjUfa6wdIFnaoWId6Fs3oH-KdtERPxx_xS0bb64ykbQMQWH4chS5cZEkdDRDJ-gVeFGxd1PpMukwmThc4LXrCj_FwCTucnW_gy3fJl46x_KzJ5uAAGsMXQBsYrs91G5xTtHTcAmUlanZdSasnuLUEXl4q_8jDOuopTl-OSY9BpVle_Yfjgn_yxAC758w-AxxglAjUirD-JZjjp0WVMoRWAsIY6oytkXTt4krTkb1KK7V3FckmQEOBbhrNT65PO1FE8lLJ8-r51AeT8TJvfxE9l4Jyvsa45uHV9yP_z65Mdgrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6cbcc478.mp4?token=XEc0Hx66khmALQc1lKH0E227CSAgJao6me2tuxlbZMjUfa6wdIFnaoWId6Fs3oH-KdtERPxx_xS0bb64ykbQMQWH4chS5cZEkdDRDJ-gVeFGxd1PpMukwmThc4LXrCj_FwCTucnW_gy3fJl46x_KzJ5uAAGsMXQBsYrs91G5xTtHTcAmUlanZdSasnuLUEXl4q_8jDOuopTl-OSY9BpVle_Yfjgn_yxAC758w-AxxglAjUirD-JZjjp0WVMoRWAsIY6oytkXTt4krTkb1KK7V3FckmQEOBbhrNT65PO1FE8lLJ8-r51AeT8TJvfxE9l4Jyvsa45uHV9yP_z65Mdgrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیت
هگستث، وزیر جنگ:
برای پیروزی، به رهبران کشنده‌ای نیاز داریم که بدانند چگونه پیروز شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/148222" target="_blank">📅 18:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148220">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62dbc95860.mp4?token=NOJF5fhmNA4rJ5VnD0zfS1UhedwBTJyeEIQD7e2-jmaK0ej6EgPbK7GL4gPCzIcsJfGpePe49rbpCzc_64e_ZsmoSuEEPV1y4JVJCh_aZOQ7i7I8lSlEjw3KcAXeTL_I3cEGqBrwHZrCGIM121C7Mm1q6DlQv_SxJyA1aIkf0keEJSBGOUc5SFUSnShUMwQyHVY1dWtb4BB4EUqM9kRehnaIzwFRcxM6zoYSLRKD4aBgxSDbj98rDi8l1N-Iy0h7Y8ppOZ8PvWTFv-zQeU58fddzvItYOVGeX_DuOYhvusTSlcQEUOH06Z2UkGhguGnC6Xxm_h2C8CrjhvxYyQ3Hlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62dbc95860.mp4?token=NOJF5fhmNA4rJ5VnD0zfS1UhedwBTJyeEIQD7e2-jmaK0ej6EgPbK7GL4gPCzIcsJfGpePe49rbpCzc_64e_ZsmoSuEEPV1y4JVJCh_aZOQ7i7I8lSlEjw3KcAXeTL_I3cEGqBrwHZrCGIM121C7Mm1q6DlQv_SxJyA1aIkf0keEJSBGOUc5SFUSnShUMwQyHVY1dWtb4BB4EUqM9kRehnaIzwFRcxM6zoYSLRKD4aBgxSDbj98rDi8l1N-Iy0h7Y8ppOZ8PvWTFv-zQeU58fddzvItYOVGeX_DuOYhvusTSlcQEUOH06Z2UkGhguGnC6Xxm_h2C8CrjhvxYyQ3Hlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیت هگستث وزیر جنگ:
اگر ارتش ایالات متحده آمریکا رو به چالش بکشید، شکست پایان شما خواهد بود.
🔴
در دوران ترامپ، جهان آموخته است که ما فقط برای پیروزی می‌جنگیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/148220" target="_blank">📅 18:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148219">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54da84d255.mp4?token=CLY3OfZ0fjGiBcPbPkebuLn9_fm8rWrRn4qPB_s9JwMwi9j-GtuJcy9SWz-67RtU-86X4L0IOIcdRQTgF29ch_JnT5PjatRokm4rGns9DI5LBGbl5Y-HiG-rioMDKuIqWPgA2mmCjgTcyFNK2zJ1A0i2wFdbBjnk2Iwcc77IKsgsMmZR9Xo-GWydSZaIXEbk8OGvMbn1jmZRXadzoppnU0I8f25E2Ows_aVderXfYXNULJOQI3o2Dmn3iV1t3QyH-x2qu_HCci0_07Dw9UJpNi7JoMciMQir1GqUbyVHE-xw7frPxCkzZM2uNRJIDvwDYjVUdurIIXAA3UuwXuoZnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54da84d255.mp4?token=CLY3OfZ0fjGiBcPbPkebuLn9_fm8rWrRn4qPB_s9JwMwi9j-GtuJcy9SWz-67RtU-86X4L0IOIcdRQTgF29ch_JnT5PjatRokm4rGns9DI5LBGbl5Y-HiG-rioMDKuIqWPgA2mmCjgTcyFNK2zJ1A0i2wFdbBjnk2Iwcc77IKsgsMmZR9Xo-GWydSZaIXEbk8OGvMbn1jmZRXadzoppnU0I8f25E2Ows_aVderXfYXNULJOQI3o2Dmn3iV1t3QyH-x2qu_HCci0_07Dw9UJpNi7JoMciMQir1GqUbyVHE-xw7frPxCkzZM2uNRJIDvwDYjVUdurIIXAA3UuwXuoZnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمزه صفوی: من جای ایران باشم، دنبال ارتباط مستمر با ونس می‌روم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/148219" target="_blank">📅 18:17 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148218">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5phdGSj23PJrjOPCq-D24XozCv70VQLv81W17uDMJUnSRlVGJxmwXYDXovSWs4vfo48VwSZcr5yxZDyS5sS-H0aUMn7iLOqAs1SFJfORlSYSrQxyh2gDxP7GUn9OclH93dJOnf3ekq4Gf7x7FIUXW8c76M2mK0hwvq_OrJJVZf_XKir27jdSBCNKDD-6cmABp1ZPYMhcqLH2zMdLFbK33EEuHQ-v29a4ZpR-la9piu-iXwO8VC_sBTxSkwI5vBQSk4onue_3tLcnjhmu2QaRE4QDPTC9sIOmBcL2puEBZqpYbyJmBXL9XfQFuvdbFKSspTCtrGnZi67Q5Z--98LwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برخی تراستی‌ها برای افزایش سهم محموله‌هایشان، کشتی‌های رقبا را لو میدادند تا توقیف بشوند…
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/148218" target="_blank">📅 17:58 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148217">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75801e50d0.mp4?token=T6dGIwHWmt_vaA9DzmFWXcrTvEP0cD-WYD_VeF0n8be2N1WHPJnLJkgXHxCw6xH1esXzJxEHx0dURiSQUDQta4XOvs9q78hszZF-2XQUgINBcNAqq3v-vnNLO4C1FLsuAC4mFNAP-1EvFBApcinbDovmsFbVSuyavEh1odPKJujjYI51w5sBehYwyNnlOm8QNW-LlbIzGD63GIIeOP38cimjbSwmwEpcYlSjFwxVu_G8wnlsGbjSjJpxBZqJvwvXVMYLprayijpgGmq8oxaAFvftUKK-WocgJek8Fj31djZMNMgqOyngUF4wbaSSxazzNXFOEOwZDYX6_q-tQSoKlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75801e50d0.mp4?token=T6dGIwHWmt_vaA9DzmFWXcrTvEP0cD-WYD_VeF0n8be2N1WHPJnLJkgXHxCw6xH1esXzJxEHx0dURiSQUDQta4XOvs9q78hszZF-2XQUgINBcNAqq3v-vnNLO4C1FLsuAC4mFNAP-1EvFBApcinbDovmsFbVSuyavEh1odPKJujjYI51w5sBehYwyNnlOm8QNW-LlbIzGD63GIIeOP38cimjbSwmwEpcYlSjFwxVu_G8wnlsGbjSjJpxBZqJvwvXVMYLprayijpgGmq8oxaAFvftUKK-WocgJek8Fj31djZMNMgqOyngUF4wbaSSxazzNXFOEOwZDYX6_q-tQSoKlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای اسرائیلی به تخریب در مناطق مایس الجبل و المنصوری در جنوب لبنان ادامه می‌دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/148217" target="_blank">📅 17:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148216">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
حسین پوراکبریان، عکاس و طبیعت‌گرد، تصاویری از پرواز صدها فلامینگو بر فراز دریاچه مهارلو در استان فارس منتشر کرد و در توضیح این تصاویر، با اشاره به گسترش نمک و فاضلاب، نسبت به وضعیت زیستگاه فلامینگوها ابراز نگرانی کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/148216" target="_blank">📅 17:14 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148215">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
رئیس‌جمهور لهستان: پوتین در حال برنامه‌ریزی برای حمله به کشورهایی حامی اوکراین است تا اراده ناتو را فلج کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/148215" target="_blank">📅 17:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148214">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
این تاریخ بیت کوین میاد رو 200هزار دلار
از این تاریخ پرواز میکنه تا 200هزارتا
👇
https://t.me/+4jOgodAq96dmYzY0
https://t.me/+4jOgodAq96dmYzY0</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/148214" target="_blank">📅 16:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148213">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7d70147ef.mp4?token=mOj61g0KHkRZH8TJRK5fISL4S19x-ZbOIC4VPGgmEOSrNAowLxjq1Sz2hjD9IFLrnhbwb1dgOIsghV8ifVJaEkHznzErrKeL3q1tqq4w4L4880rKpVc3j7wU536rTlgAmqIvPN1G75KNBxGcgtkGFk9mppGFawel9aEsWVkKfOo8VWGGTyYviKDmZ0f3pSFgowzDPRqVUXvBtfNX36Dy7-TJkjbewu0XUYwHUwnyY5hBeTc0Jn8_W0G1B48AfPAOwUCmFwEBh7UutG0FWTqbk0HmPM8pY3KffSm1TJ6KXXs61e3WHxiyzyNaJycWwkAr1yYRjU9EC0Q9cRY8oT3fxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7d70147ef.mp4?token=mOj61g0KHkRZH8TJRK5fISL4S19x-ZbOIC4VPGgmEOSrNAowLxjq1Sz2hjD9IFLrnhbwb1dgOIsghV8ifVJaEkHznzErrKeL3q1tqq4w4L4880rKpVc3j7wU536rTlgAmqIvPN1G75KNBxGcgtkGFk9mppGFawel9aEsWVkKfOo8VWGGTyYviKDmZ0f3pSFgowzDPRqVUXvBtfNX36Dy7-TJkjbewu0XUYwHUwnyY5hBeTc0Jn8_W0G1B48AfPAOwUCmFwEBh7UutG0FWTqbk0HmPM8pY3KffSm1TJ6KXXs61e3WHxiyzyNaJycWwkAr1yYRjU9EC0Q9cRY8oT3fxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جوزپه کاوو دراگونه، رئیس ستاد نظامی ناتو: در مورد فعالیت‌های ترکیبی، درخواست خودکار ماده ۵ (معاهده ناتو) مطرح نمی‌شود، زیرا معمولاً این فعالیت‌ها از آستانه بحرانی پایین‌تر هستند.
🔴
منظورم این است که یک حمله مستقیم در دستور کار نیست. اما یک حمله مستقیم، به طور کلی، فوراً منجر به درخواست ماده ۵ خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/148213" target="_blank">📅 16:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148212">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
فوری / گزارش انفجار در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/148212" target="_blank">📅 16:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148211">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
کمیسیون امنیت‌ملی: کاری کردیم که آمریکاییا دخل و خرجشون دیگه نمیخونه
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/alonews/148211" target="_blank">📅 16:49 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148210">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
برد کوپر، فرمانده ستاد فرماندهی مرکزی ایالات متحده: ما با دیدی روشن و تمرکز کامل در کنار همکاران خود در سازمان‌های مختلف دولتی ایالات متحده، همچنین با تمامی شرکای عضو شورای همکاری خلیج فارس، و همچنین شرکت‌های بیمه و حمل‌ونقل، برای افزایش حجم تردد از تنگه…</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/148210" target="_blank">📅 16:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148209">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
برد کوپر، فرمانده ستاد فرماندهی مرکزی ایالات متحده: ما با دیدی روشن و تمرکز کامل در کنار همکاران خود در سازمان‌های مختلف دولتی ایالات متحده، همچنین با تمامی شرکای عضو شورای همکاری خلیج فارس، و همچنین شرکت‌های بیمه و حمل‌ونقل، برای افزایش حجم تردد از تنگه هرمز همکاری می‌کنیم.
🔴
این تلاش‌ها نتیجه‌بخش بوده است. حجم نفت خام، بار و گاز طبیعی مایع در دو هفته گذشته، بیشتر از هر زمان دیگری در شش ماه گذشته بوده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/148209" target="_blank">📅 16:38 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148208">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
ژنرال برد کوپر، فرمانده ستاد فرماندهی مرکزی ایالات متحده (CENTCOM):
نیروهای CENTCOM در ماه‌های اخیر، انتقال بیش از یک میلیارد بشکه نفت خام از خلیج فارس از طریق تنگه هرمز را پشتیبانی کرده‌اند
🔴
ما به این دستاورد مهم دست یافته‌ایم، در حالی که با ارائه حفاظت هماهنگ، به عبور بیش از 2000 کشتی تجاری از این تنگه کمک کرده‌ایم.
🔴
مسیرهای اصلی عبور در این تنگه از مین‌ها پاکسازی شده‌اند. هزاران کشتی از این تنگه عبور کرده‌اند.
🔴
بیش از یک میلیارد بشکه نفت خام از طریق تنگه هرمز از سوی کشورهای هم‌پیمان خلیج فارس صادر شده است، و ایران به دلیل محاصره قاطع ما، هیچ بشکه‌ای صادر نکرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/148208" target="_blank">📅 16:38 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148207">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a12d9906e4.mp4?token=Rvt51IR2mflpXuZyhZ2MM74BjCTPCyPtL0sUF32aBp9r_fQHIgxyyHXycTcJkHGKV-ssIb7qTDfg_LCEJqM4VFkSQmq__FNJRtGN5R--v_eyQOY8eEikQL7URDYuMX8BbLIYBWwA4uUI9AMzo4ro_p-7OQ80JzkCvk5XIwaelXK7Tcd2K2R7QMfHxtpwacz9XK3sDZjKADLe4nqt_WrGN3EhXgmU7QS72YZ022IadSpIGhEgAmi2LzCxDnAVVutkl-sChBuADp0C5LzGaEc2Xr-mWDQqRFD8nmm7eQpZXNWQl-j30PfBYhPmX_MRRMchufw9UlbS636ieVZoOeupXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a12d9906e4.mp4?token=Rvt51IR2mflpXuZyhZ2MM74BjCTPCyPtL0sUF32aBp9r_fQHIgxyyHXycTcJkHGKV-ssIb7qTDfg_LCEJqM4VFkSQmq__FNJRtGN5R--v_eyQOY8eEikQL7URDYuMX8BbLIYBWwA4uUI9AMzo4ro_p-7OQ80JzkCvk5XIwaelXK7Tcd2K2R7QMfHxtpwacz9XK3sDZjKADLe4nqt_WrGN3EhXgmU7QS72YZ022IadSpIGhEgAmi2LzCxDnAVVutkl-sChBuADp0C5LzGaEc2Xr-mWDQqRFD8nmm7eQpZXNWQl-j30PfBYhPmX_MRRMchufw9UlbS636ieVZoOeupXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
محل وقوع آتش‌سوزی در فرودگاه ریاض
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/148207" target="_blank">📅 16:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148206">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
هیمتی: چرخ اقتصاد کشور فعال شده و اوضاع درحال تثبیت شدنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/148206" target="_blank">📅 16:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148205">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IgxHSwA9IX0jEjxpQcCIlswjN-ZpfkqZcSAwxu1uQj3JAb57-1prXBBUpSQJAeGFWXeZ2bps7td3gyji2Y_RW7lM5SRp-mXvjJfk2gV4ln9pRI4ePqLW7mQKIgpkbGvChpZsvyyhdnhd3Qv8i_73Wx4PZ7KnWY4sSd6YEtwCnAk8WHUY-znenIeGv-8Eb1cbV8CxFvggeYj0Ot2G84oDiv1jjZWjLRz6x0JWrXx3gS7L4T7IxZjB31hH6lXXtN9NAfDcqiJevCO3M6Txx0St5L_PfWnD8bFZ2_e5cVQRmQiF6oiaydJ8aZfaYEcVS5egxWpzCuBxDdeOY0xsgJ485g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاسبی جدید با نوبت گیری دکتر: ۲۳۰ هزار تومان بده وقت بگیریم!
🔴
نوبت‌گیری پزشک و دندان‌پزشک حالا برای برخی افراد به یک منبع درآمد تبدیل شده است. برخی بابت این خدمات بین ۵۰ تا ۲۳۰ هزار تومان دریافت می‌کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/148205" target="_blank">📅 16:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148204">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7383ac988.mp4?token=OLk1-GF1NfG5rFLjGucjhuw2EZSLId5KB7F-eWSw1tvsQ2AAMMqgp13ceFcPEQH4bjtEQxcdPmtW332DcXWh6ZCyvhrB_Yn7iJH4cv1YvSpi7TEp92Qz8vh_G-K80IvWzubwH6LVtxxgSEGgGTUQR9nRRc9avZcvbTQdEnXBfWnWKeftF_AwU4z3He-cKb_C00VeqWgAz5U2GmuKCc3JqZWxFdKAI1mJBm7BGdv_7ySa-bKhP8jvQkz9hUCutr5gsc5HXT4XJawoUtd2yhSKfFHQzRsVdxDcuT2OQmpTQHFsDqaX3Ua-as6xcyJqZAHGAaCVyfnhUdvKiqBNlUIPoILjEeVoVjpx7L8jfy7UxjClC7K4oFYvvE_vRzeujMPN5VddEj_ERDLEKfDm7qzZ8ngTUHWhxVd833qHtW5MJDLGpC1WJfs1ZFV81Jm20gw9v-yUJtkw2ut2mCMtvxoyCF6eZz0dhOLPU641HHztZKA-rlB_WQC0mfb79aNpAoUb1aegpI78GfA9D6BGLNtaBsIiaH3S9rdV-9CfmEjxFfmLcaDPsLIQ0QoO3eHQNd0WHqwKngHl2ZdgeimpaBCPg0TYy_zOBTIvYM6xiZS4ZLG1aHgJsw0yzYLoFRJQcVwiTMOhhuusFyUfR0MgZdUJ_AKEUk4I8JDEpVfLEQ4s5Ic" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7383ac988.mp4?token=OLk1-GF1NfG5rFLjGucjhuw2EZSLId5KB7F-eWSw1tvsQ2AAMMqgp13ceFcPEQH4bjtEQxcdPmtW332DcXWh6ZCyvhrB_Yn7iJH4cv1YvSpi7TEp92Qz8vh_G-K80IvWzubwH6LVtxxgSEGgGTUQR9nRRc9avZcvbTQdEnXBfWnWKeftF_AwU4z3He-cKb_C00VeqWgAz5U2GmuKCc3JqZWxFdKAI1mJBm7BGdv_7ySa-bKhP8jvQkz9hUCutr5gsc5HXT4XJawoUtd2yhSKfFHQzRsVdxDcuT2OQmpTQHFsDqaX3Ua-as6xcyJqZAHGAaCVyfnhUdvKiqBNlUIPoILjEeVoVjpx7L8jfy7UxjClC7K4oFYvvE_vRzeujMPN5VddEj_ERDLEKfDm7qzZ8ngTUHWhxVd833qHtW5MJDLGpC1WJfs1ZFV81Jm20gw9v-yUJtkw2ut2mCMtvxoyCF6eZz0dhOLPU641HHztZKA-rlB_WQC0mfb79aNpAoUb1aegpI78GfA9D6BGLNtaBsIiaH3S9rdV-9CfmEjxFfmLcaDPsLIQ0QoO3eHQNd0WHqwKngHl2ZdgeimpaBCPg0TYy_zOBTIvYM6xiZS4ZLG1aHgJsw0yzYLoFRJQcVwiTMOhhuusFyUfR0MgZdUJ_AKEUk4I8JDEpVfLEQ4s5Ic" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بوریس جانسون: به نظرم این استدلال که روسیه به‌نوعی به‌خاطر استقلال اوکراین چیزی را از دست داده، کاملاً اشتباه است. داشتن یک همسایه آزاد و مرفه چه ضرری برای روسیه دارد؟
🔴
اما درباره اینکه چرا این موضوع مشخصاً برای پوتین اهمیت دارد، پاسخی وجود دارد. پوتین می‌خواهد یک الگوی سیاسی خاص را حفظ کند. او دموکراسی نمی‌خواهد و اوکراین آینده‌ای جایگزین را برای روسیه به نمایش می‌گذارد: کشوری آزاد، مطبوعات آزاد، جامعه‌ای کثرت‌گرا و رسانه‌های آزاد.
🔴
او از این متنفر است. مشکل همین است. تهدید علیه ایدئولوژی او، خودِ اوکراین نیست؛ بلکه اوکراینِ آزاد است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/148204" target="_blank">📅 16:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148203">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
سوئیس کشوری که ۲۰۰سال توهیچ جنگی نبوده و نماد بی طرفیه وضعیت جنگی اعلام میکنه !
🔴
با این اعلام آمادگی برای شرایط اضطراری که اکثر دولت های اروپایی دارن اعلام میکنن به احتمال بالا روسیه قراره علیه ناتو اقدامی انجام بده ‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/148203" target="_blank">📅 16:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148202">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/byVGAQOnF57Glx5iFCzo3u1hZi72Lu-G4KFrFhn7x6B1DdCpdu8dli4A-subu5ST0qe7YQ2fyXmNjcI5AgNsHzuNkvgAOo18pB9B1wvy9CgFOrINvwfneiW-C5yx7X0QhFuw1TH9uIeINxwsbu6O2aVY2zEzCrnuQRE81XkiE6NfX0D4nKbWHf37OaiD9eqY9qOtCCsL8d6F2SOcSzZSKKkuBhXnVkSx4n1YMpL9g_v37GKTtyIVx0Ed_XW2M3WrEW5OPFGw7-JdEZfX4OSZooCeUBm8yXr8uPS1V_vC_EDAGvEZg9Xag5SpN9ywamZfbwmI5LukxEpolub0Bw60hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سوئیس کشوری که ۲۰۰سال توهیچ جنگی نبوده و نماد بی طرفیه وضعیت جنگی اعلام میکنه !
🔴
با این اعلام آمادگی برای شرایط اضطراری که اکثر دولت های اروپایی دارن اعلام میکنن به احتمال بالا روسیه قراره علیه ناتو اقدامی انجام بده
‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/148202" target="_blank">📅 16:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148201">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7509fa857.mp4?token=uLWTYXmn62iPaHX-LHpEZKJHKTZnFsRfhIja1oMckNg94B-gtlY1OPCxBVfBAojcxOQR2MPNo83lt-PRYaoT8hA5YhmwFlQ5qinp71EEn96DuZEpNswcTJYBqiB4nJtvE4GDGu_sUDm1HOI3xO-jWvdACOOmEmY5h6u4HAN3BEAvE0m57KKgtCo4t0tgQZ8zBvumqmF_itpA2l8JYv3K7JmMwOZcypgOSOX27vUB7X2e7mUmwv8sAPM07nNoZU279YvbdAnTMOY_j2phP0-Lsxp4u6tiu1ADFlHW2dA69_wvO6D9gsbC8pEy0ErOl3niySZWRZSuJHPBRHoEJIzmjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7509fa857.mp4?token=uLWTYXmn62iPaHX-LHpEZKJHKTZnFsRfhIja1oMckNg94B-gtlY1OPCxBVfBAojcxOQR2MPNo83lt-PRYaoT8hA5YhmwFlQ5qinp71EEn96DuZEpNswcTJYBqiB4nJtvE4GDGu_sUDm1HOI3xO-jWvdACOOmEmY5h6u4HAN3BEAvE0m57KKgtCo4t0tgQZ8zBvumqmF_itpA2l8JYv3K7JmMwOZcypgOSOX27vUB7X2e7mUmwv8sAPM07nNoZU279YvbdAnTMOY_j2phP0-Lsxp4u6tiu1ADFlHW2dA69_wvO6D9gsbC8pEy0ErOl3niySZWRZSuJHPBRHoEJIzmjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه‌ای از فعال شدن سامان‌های پدافند هوایی در ریاض
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/148201" target="_blank">📅 16:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148200">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IdydG2JEtShHlvqksmCSRokkOcVklqXoXE-p9zAzcj3qchnGCS1H8vPjC0aeu1bg1-O6QGEUhDJ0OqLUgyIHAo345RV2N4fo83NgSeZHG_Mc0Pq6LeypgjqdrccBn8I7E9q0U848Kx_IPFatmDSzgCk0f1rJPVgdf4LmDlcQlkuUJec7wwpVbibYxBG6-2kUPbieFcsVnW2KmcHyJgMAh88ppJO9ROAMFEAo3p84tzgq5pPHEkXgLp3vzwIpeXE7CYg9SQKCSoXbwCutBy36CcECNpCPkmga-B3K6_5nireEU_3vXnpQDmAfqfCNHmNgExJyae6zsMLpWh1fymoLfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواشناسی: شدت بارش باران و برف در مهر و آبان ماه به حدی شدید خواهد بود که در اکثر استانهای کشور احتمال سیل و کولاک وجود داره.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/148200" target="_blank">📅 15:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148196">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kfg02F2bEafQsyZjTgUyfruNwZX0OXy0CmXBSD4hYxNmZbYuf5x8lmnNJDmQriwwytInRRYcyBN8WlHjbM604q8UrBtbZ-3hel7_T0Uzzvbz3twpN3Noum0dgfxwwmNSK5bkieiVUaaLiwQTBO53QjdbAYL_fC5xPWPtP2lgV_9FWVad_IIa-KfVnAKjACBiBZblzYNgt49Z2XL6MQJsH4rzxxg7-4VF5xxq2cyWy1wtTGtkMkrI3vCJVkk6Y2yiO5P_uKIt6NDMItCG4OhtkvQPM0etBHD4Ny6xBuCGG1SmeQlzuViOKozYTppUUCUe1SZ-EeAbKpv5TVqQQ96rsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/t6GyKghOvZUV0QZNQI3LnsvYK6lk2VkOxeU8Hy3HCK51wHe7UfR6CN1-a5YuZocZ8E7OCPQ-28OJ6GxD5RTC7OVr1LRl4r97amnAMNfnfB4VZUHRdz0sBn2xfFKbsj_3v_SGolHei2qyo4u0CYaL-xfYkLxhfW2jHMJX480RCOSvgYiqGrZWMoyuBMj4HtcM_Q9oqECyJTX2QyWy7ddW0bKbuarMajj5fmJBc8jhKRzscOQn_PXHBXMrxXfjp1ueKYesOCpEbetQlI8KxkffV1hO6GBr6MjS2FlLUr-_ByBnxbs_KUrY3E8hzSVSUxBbjuNZLWzC05EgReyyVIl_9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FCY6mCBEwLDjQMKnOry_FAphwlhow5keTZ6mZeiyMlkPETcBzM9jC643ucOs3YA5wH03HS1phn6W2cogxNvklPdMWBHtpCzicsMNA4rV4l8jLoOVFiQsnEiQApjlKT6RVKchVwtUolKP6jey89-STllc0XyRIvwUs8LKQGSEJb1uoDZU85I2p7TwTNAZsM1wwkkGqtwo4BV09nNARb8m1Xe70_7N3A9mRuWauZm9PMO68NSuwx9XhkhUN5UF3iSzN-_sF1ZoDay0sMSLCoXt5kvyPt6LcKI8FdJApwkrbP5g4m6lri5a5FcmRB26Oufc3OMQEKV9tiAMBse931kYqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RHpe0XHRbSIY-wMVDwM1U9l5IU8cPJUibLkJkkz1k68R9VqMv64vJ5gqHCHdJKXvj0d_HJP1aMrbCSZEB2O_7QrEwzFz2cVJBV0a2cLEv3IvufBj6g9JouH1PPQEfq9aZo-NpG8NkJOMkN9uMlHyVgU7cq71tlMEev-8N4M8Ar3i0T90BQVO_yF2rgaJsqkEpMrrNBQOrw8QoDBqVM_Mqqb1Jo4DqeKQI_T55LSrG4HmDaKmjQG4AzFuGCJpVq_1xHJMaExlEkWcOOLOCxb3u-WnCgAhl3mAV5DaMx0-KtFBwlJXdj7WwVxx9w8fmaYzRaGyjBya9y4fvEgKALszmg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جزیره فارو اعلام کرده که مهاجر می‌پذیره.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/148196" target="_blank">📅 15:52 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148194">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/243abf4097.mp4?token=ag2JU_pJaqiL8cyjCX4ua_ogufhatT3OxHQOWCFAkA58qjsUiBpaRWGLI9jC-6VsfASnmHUoq7_qhVG_Xv0CXalg2Vv1PZfYMAg5yvdS-ZN-rSmXWxgLYsKmRtOC0Jc3LU1QE_fic10WxoagsrTwtg7r_pupN3DIcuUVCpQmSZ_6SE8nk9wTPiHX6DeCR2Mc3bfOncXWDbQrjpYkKDsdbqpsAkn_f3gKk7VJnBsHKMDL0hkWvfi9Mr_quT0Y0Y6o43cPCokxDECktuAEGZkuJUisTTn3bIKxzDeIucLh5Iz4ajJgBzy8wXzrLwLpZXFe294uxkMypVK9LUrqk8r1YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/243abf4097.mp4?token=ag2JU_pJaqiL8cyjCX4ua_ogufhatT3OxHQOWCFAkA58qjsUiBpaRWGLI9jC-6VsfASnmHUoq7_qhVG_Xv0CXalg2Vv1PZfYMAg5yvdS-ZN-rSmXWxgLYsKmRtOC0Jc3LU1QE_fic10WxoagsrTwtg7r_pupN3DIcuUVCpQmSZ_6SE8nk9wTPiHX6DeCR2Mc3bfOncXWDbQrjpYkKDsdbqpsAkn_f3gKk7VJnBsHKMDL0hkWvfi9Mr_quT0Y0Y6o43cPCokxDECktuAEGZkuJUisTTn3bIKxzDeIucLh5Iz4ajJgBzy8wXzrLwLpZXFe294uxkMypVK9LUrqk8r1YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قار قار کردن و توهین عده‌ای به پزشکیان در دورهمی دیروز
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/148194" target="_blank">📅 15:36 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148193">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
پوتین: رهبران اروپایی در روز های گذشته به صورت آشکار اعلام کردند در حال آماده‌سازی برای جنگ قریب‌الوقوع با روسیه هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/148193" target="_blank">📅 15:35 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148192">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
یاشار سلطانی: کشور صاحاب نداره! رئیس جمهور و رئیس مجلس یه توافق رو انجام دادن اما عده ای خودسر موشک شلیک کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/148192" target="_blank">📅 15:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148191">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
یاشار سلطانی: کشور صاحاب نداره! رئیس جمهور و رئیس مجلس یه توافق رو انجام دادن اما عده ای خودسر موشک شلیک کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/148191" target="_blank">📅 15:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148190">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
مکرون: خواهان بازگشایی تنگه هرمز از طریق دیپلماسی هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/148190" target="_blank">📅 15:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148189">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
واردات خودرو مدل ۲۰۲۳ آزاد شد
🔴
تا پیش از این، تنها خودروهای مدل ۲۰۲۱ و ۲۰۲۲ در این رویه امکان ثبت سفارش داشتند، اما مدل‌های ۲۰۲۳ نیز اکنون به این فهرست اضافه شده‌اند. جزئیات شرایط جدید و الزامات قانونی، همچنان اهمیت زیادی برای متقاضیان دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/148189" target="_blank">📅 15:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148186">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Na3IE3hV-dioG2DJDj1d2Yn1aNCq8xtEiN4cgTSxf0MSQvuDE_gyKsyTa33VcKDHprGT40149XhWRxnkAMN46jWTFAa1PSfMTESrdbSVhaz8u3Sf6MFSMTSPAakB6ZsVmhgTavf4w65lQ7cGluRenRDzcq0AHHoxl_pnbU3fBGieRM6yR-sAA0m5Ams0wvIzVBR0rwTOnW2Ufqh_Q92JbysOfShErvTWq8xyWnk6QCpBDNllzzMUhPoRFL8RxELNX2WlHaPaGM8MtBI0ZSsRMKW84ll-dStmBjW-zIU4IUOKQt0cC4d2sxs9FphcweyLzk9iMmYb7aHPZ5DLUM8hDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23a4c429f9.mp4?token=aD03XEajy-a6-9u_uEu0n9aUQmwh4VRAIjWzzN-3wHLvO8lB4rskYYMgxFk6sHVqiA2vg2pChY4v2sBnBII_72Aap53E0itzZH4OaW9395ncKepPLtqZ0WwowWl3MS5-NTmJLAJcsl62odnPnLnYdJYeZv4I86Vj-fyDoPj9S787skHEvCYLgM3hohRx81RdQ6JWIMi6ic0lcWBBliSUJmtlkuYSzY1cntRp7irrha-hZ5PelxhUipVM7tYpzilr2q_nmO4WjYJYfXZ2fP9NFZl_PhSJJgf4XxIwbJZQ7COAZ_YGWp_MXnJUIpyuwCcFh8IOk9jkRtzfkQf4BoPTvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23a4c429f9.mp4?token=aD03XEajy-a6-9u_uEu0n9aUQmwh4VRAIjWzzN-3wHLvO8lB4rskYYMgxFk6sHVqiA2vg2pChY4v2sBnBII_72Aap53E0itzZH4OaW9395ncKepPLtqZ0WwowWl3MS5-NTmJLAJcsl62odnPnLnYdJYeZv4I86Vj-fyDoPj9S787skHEvCYLgM3hohRx81RdQ6JWIMi6ic0lcWBBliSUJmtlkuYSzY1cntRp7irrha-hZ5PelxhUipVM7tYpzilr2q_nmO4WjYJYfXZ2fP9NFZl_PhSJJgf4XxIwbJZQ7COAZ_YGWp_MXnJUIpyuwCcFh8IOk9jkRtzfkQf4BoPTvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر دیگر از انبار ذخیره سوخت در فرودگاه بین‌المللی شاه خالد در ریاض، عربستان سعودی که در حال سوختن است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/148186" target="_blank">📅 15:17 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148185">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bd3300290.mp4?token=t-ejjACXnsSyyHKDCyEncZAqgYUe2ycHUL4cygvXQ7p2S6LvvFQsT-sOfvE2Ea78-B8yaxXP2yCrJsb8eRrjAVtYu6iIodxCLWW2y5Qoi5Z6buknOOuRUnzWD18iKspLoDF6lz2RH7gZWa5t6VuoufavU2xRjgZ3XaRfChf2Ajzg9XE10kP6oqtwgjPx7Sn2Bfbo1urtexxhDJnW0bPLLFA1ASPSPRSrvnq8n24_K9wqyOiitZ5x2VnATIWPCtOUs506W05u7_z-H6lyZcctDzEJxOflW9IY79bExB4jkuCrSUBL7bAerB7lUEpI3ahWm1jlES7bd6n9ydyrG1X5rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bd3300290.mp4?token=t-ejjACXnsSyyHKDCyEncZAqgYUe2ycHUL4cygvXQ7p2S6LvvFQsT-sOfvE2Ea78-B8yaxXP2yCrJsb8eRrjAVtYu6iIodxCLWW2y5Qoi5Z6buknOOuRUnzWD18iKspLoDF6lz2RH7gZWa5t6VuoufavU2xRjgZ3XaRfChf2Ajzg9XE10kP6oqtwgjPx7Sn2Bfbo1urtexxhDJnW0bPLLFA1ASPSPRSrvnq8n24_K9wqyOiitZ5x2VnATIWPCtOUs506W05u7_z-H6lyZcctDzEJxOflW9IY79bExB4jkuCrSUBL7bAerB7lUEpI3ahWm1jlES7bd6n9ydyrG1X5rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زین واکر بازیگر ایرانی هالیوود با انتشار این ویدیو از جمهوری اسلامی حمایت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/148185" target="_blank">📅 15:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148184">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
امام جمعه دزفول: دختری که تا پاسی از شب در کافی‌شاپ‌ها و فروشگاه‌ها حضور دارد، نه فرزند خوب نه مادر مناسب و نه همسر موفقی خواهد بود.
🔴
پ.ن: این یکیو راست میگن
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/148184" target="_blank">📅 15:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148183">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
معاون پزشکیان: شرایط اقتصادی خوب نیست؛ مجبوریم پول چاپ کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/148183" target="_blank">📅 15:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148182">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
دود از شهر ریاض در عربستان سعودی به هوا برده می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/148182" target="_blank">📅 14:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148181">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48d0c461c6.mp4?token=iraH8pzUNjjDH385cJbQ_w_e3QUJt6lJSIcIiY71RzSHhMA_NVkCE0nQ1KPD1l6a1V_g8LgO04OqummAek93gvujASEVcsH58riIjswOnNMggtefT1PiW6tPkUXu93o93yYt-Z2lIDCkxDw-Sc3y5vsNvforHOt0OrnjRVUQi_Dec7L37Ko6cNN5yoVm3rD4OMT2cax_FdcA5cRGWThHWQNfHjg-CFWxU2Awl9fGFP3bQd3y4H1LZtNbEVdoq0bVdqrwfQxOQ0esaJw05dvHPZ75U5MHJ-Pb903SFpDmRukIzoA3PprlcJKt8HfiiBTis1RRg767a3bYCdTeAzFBeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48d0c461c6.mp4?token=iraH8pzUNjjDH385cJbQ_w_e3QUJt6lJSIcIiY71RzSHhMA_NVkCE0nQ1KPD1l6a1V_g8LgO04OqummAek93gvujASEVcsH58riIjswOnNMggtefT1PiW6tPkUXu93o93yYt-Z2lIDCkxDw-Sc3y5vsNvforHOt0OrnjRVUQi_Dec7L37Ko6cNN5yoVm3rD4OMT2cax_FdcA5cRGWThHWQNfHjg-CFWxU2Awl9fGFP3bQd3y4H1LZtNbEVdoq0bVdqrwfQxOQ0esaJw05dvHPZ75U5MHJ-Pb903SFpDmRukIzoA3PprlcJKt8HfiiBTis1RRg767a3bYCdTeAzFBeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دود از شهر ریاض در عربستان سعودی به هوا برده می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/148181" target="_blank">📅 14:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148180">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
مکرون دیروز  صبح تمام سران سیاسی فرانسه (حتی احزاب مخالف) را به جلسه‌ای محرمانه دعوت کرده بود. موضوع جلسه امنیت اروپا، احتمال گسترش جنگ در اروپا و خاورمیانه بوده است. جلساتی مشابه در آلمان و لهستان هم برگزار شده بود. گویا احتمال وقوع جنگ بین کشورهای اروپای…</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/148180" target="_blank">📅 14:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148179">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
رسانه‌های عربی: پروازهای فرودگاه ملک خالد ریاض پس‌از اصابت پهپاد یمنی متوقف شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/148179" target="_blank">📅 14:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148178">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b27b34a2bb.mp4?token=FxHZWz0IMYXp_ynObBkLBoDF2j8w0jyOgpWlq37Oj14GXzJVknH06vNEJtjR9EdTv4_H8H7RlF5W5qALaYz4AIxop3cDvh6qNI8YQG0TQZ_OAj9rzT_eev1nfukfQn77_jlrFjVfoJXllO8XWMhEW0_eM0RpfQoODC6GGy7o6b5nrHZjqRD2VN_5ESEf3uEZfgu22p3nilNPu5aPD1aeiZAkFdWb9quGBHnMxyr2WwacQeZYT1hNLAnom1kaqVKSW6YZhQbbU1ZbtLGy_uDflMqWa5Czmpl5CF6JoXK9kPHK3U1nR3DArNaGLRTKx7jgQw0a8Vqf1qn0O9LSYJZpgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b27b34a2bb.mp4?token=FxHZWz0IMYXp_ynObBkLBoDF2j8w0jyOgpWlq37Oj14GXzJVknH06vNEJtjR9EdTv4_H8H7RlF5W5qALaYz4AIxop3cDvh6qNI8YQG0TQZ_OAj9rzT_eev1nfukfQn77_jlrFjVfoJXllO8XWMhEW0_eM0RpfQoODC6GGy7o6b5nrHZjqRD2VN_5ESEf3uEZfgu22p3nilNPu5aPD1aeiZAkFdWb9quGBHnMxyr2WwacQeZYT1hNLAnom1kaqVKSW6YZhQbbU1ZbtLGy_uDflMqWa5Czmpl5CF6JoXK9kPHK3U1nR3DArNaGLRTKx7jgQw0a8Vqf1qn0O9LSYJZpgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امام جمعه دزفول: دختری که تا پاسی از شب در کافه‌ها وقت می‌گذراند نه می‌تواند مادر خوبی باشد و نه همسر خوبی
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/148178" target="_blank">📅 14:36 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148177">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNnka_yHVO6RDaqene_0G0Uy-2fCOBYufXHtQWfJqJJvvU_yuIPygBUNWGUQnCz-ybpPjIgcrB4b6l6yiz_YHCWe2BtyXGyNU4bjbtnJb0kt4FKbkrWG2X2F4yCQMAXo6s1WNoXG7IxiDFcT9XqEyxD2-0oK5XeCpD5ORJLWkU_gcVMK45HNcPC4Ye8Cu_R8l1Gzh5-1B1C4oQm0hKtYpyFDvoy61SnycDZWJ_1zx2aqZCUMqhwAfspvpfD-OST4ytd97wP7gXURAYq2gepQGD6rCTfTE8574-0A3wXKFThmwNchRvRJfnmJhQC1EY1qEuxoNvdw-KW4ejYk6s7eGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرودگاه‌های عربستان سعودی با مشکلاتی روبرو هستند...
🔴
تقریباً ۹ فروند هواپیمای مسافربری قادر به فرود در فرودگاه ملک خالد در پایتخت عربستان، ریاض، نیستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/148177" target="_blank">📅 14:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148176">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
رویترز: شعله‌های آتش و ستون بزرگی از دود سیاه در نزدیکی فرودگاه بین‌المللی ملک خالد در ریاض مشاهده شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/148176" target="_blank">📅 14:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148175">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
وزیر امور خارجه پاکستان به همتای ایرانی خود:ما بر لزوم تضمین عبور ایمن کشتی‌ها تأکید می‌کنیم، زیرا این امر به نفع زنجیره‌های تأمین انرژی جهانی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/148175" target="_blank">📅 14:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148174">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bcf4947eb.mp4?token=W5zkx_t91gBK_ndSrfbt_kvV5NWBNi8vCXDexFw-z6cdsT3Q9G2MDr3IU3POREQNkwxJbeCqSXFYR1UlaRq_UYeFPF2WzDvEwl1hvzvAmhcsrNQbjk_yLbUO5slBsp3T70OPiw4J-P3z5NmrdWMrH_CP4XvdChTXyIC0mV_bbxfaS7MZUu-mQQJ7o3r0ywzFydDUTHMNqoasMooSR5cAmJ7oOguDPPq86M3ZzD0F1FwVOHs3I8POyj-bssd6HKRkJPfUR2p3qs51A9Owm6DqZ-6rZuDXawhXhR6MxdDkGjXLEj4exxlXRsjUkz4cwZWNC4orEmqVMOZY--rX4ypIow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bcf4947eb.mp4?token=W5zkx_t91gBK_ndSrfbt_kvV5NWBNi8vCXDexFw-z6cdsT3Q9G2MDr3IU3POREQNkwxJbeCqSXFYR1UlaRq_UYeFPF2WzDvEwl1hvzvAmhcsrNQbjk_yLbUO5slBsp3T70OPiw4J-P3z5NmrdWMrH_CP4XvdChTXyIC0mV_bbxfaS7MZUu-mQQJ7o3r0ywzFydDUTHMNqoasMooSR5cAmJ7oOguDPPq86M3ZzD0F1FwVOHs3I8POyj-bssd6HKRkJPfUR2p3qs51A9Owm6DqZ-6rZuDXawhXhR6MxdDkGjXLEj4exxlXRsjUkz4cwZWNC4orEmqVMOZY--rX4ypIow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تو صدا و سیما مجریا‌ با تراکتور اومدن وسط برنامه میگن با همین میخواییم اسرائیل رو شخم بزنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/148174" target="_blank">📅 13:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148173">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
وزارت دفاع روسیه:«ما یک نفتکش در بندر اودسا و یک کشتی باری در دریای سیاه را که برای پشتیبانی از نیروهای مسلح اوکراین مورد استفاده قرار می‌گرفتند، هدف قرار دادیم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/148173" target="_blank">📅 13:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148172">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
مذاکرات پکن و آمریکا در حوزه انرژی /  بازگشت چین به بازار LNG در بسته ۳۰ میلیارد دلاری
🔴
آمریکا و چین برای کاهش یا حذف تعرفه ۱۵ درصدی پکن بر گاز طبیعی مایع آمریکا مذاکره می‌کنند؛ توافقی که می‌تواند هم‌زمان با سفر رئیس‌جمهور چین به واشنگتن و در قالب بسته گسترده‌تری از قرارداد‌های انرژی و کشاورزی اعلام شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/148172" target="_blank">📅 13:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148171">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6WeQ0bS8zqthSwBq54tdG69cL0-AUv9H400EoC-OC4dFKPY1mJiD1el8Z9kIrPfU6Ux0OzUvm-bPo-yd_z6FGlxrJggjWXwzehCzd31M4pwsKEzG_1nATMTfNkk_6nPtsSPUltuVSCQzdSdsMJYN-X0mLN6bcOA1-4tkBwVNLday4XkjGQk6MH6xR5rpedHViVRLakb5Nb8a7SQLo_xOM8j3q2ZJurCzj1TAG5ZLkF1D3H30v9c4LsEsqfBT67KJDLymXk2hmIa1lcAwX9bh5j7vpEx3hbj-c4Ilpl1XoXyHIdNL1byBUzXimRujD2LJ6i5uE_Vy6Kc-vWhrpPoPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پاسخ ایران به پیشنهاد جدید آمریکا احتمالا منفی است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/148171" target="_blank">📅 13:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148170">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
سخنگوی ناتو: از اعلام توافق بین ایالات متحده، گرینلند و دانمارک استقبال می‌کنیم. این توافق، امنیت و ثبات در اقیانوس اطلس شمالی را تقویت می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/148170" target="_blank">📅 13:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148169">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
ان بی‌سی: روبیو، وزیر خارجه آمریکا برخلاف ونس، از قرار گرفتن در کانون توجهات درباره جنگ نامحبوب ایران اجتناب کرده؛ این فاصله ممکن است از نظر سیاسی به سود او باشد
🔴
روبیو در تمام مدت این جنگ، یک «دست پنهان» بوده؛ او به تدوین راهبرد دولت ترامپ کمک کرده
🔴
به گفته افراد نزدیک به وی، نامزدی احتمالی او برای ریاست‌جمهوری می‌تواند روی میز باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/148169" target="_blank">📅 13:19 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148168">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
سفیر آمریکا در سازمان ملل: محور سخنرانی ترامپ در نشست سالانه مجمع عمومی سازمان ملل در هفته آینده، ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/148168" target="_blank">📅 13:14 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148167">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16b3ec86ff.mp4?token=PLnSBIMWOttxV-9MUVPG0UuT-mnVb-D_2teyLpqXOKEJkbl7GKamlqUB4qg8m6DaHXL3EP0Ew3T0axUTYtiiRYqVU__RkdXy4kWO0Gaerh6pxMyWKRmb4IgDU1OJ1NudEr5Zy3ym22voiVhb6hcHnAJZpraDA2JcoDGyn70TyUN73HbDTx6SHwqbSUvys0TNdjgCCZ3g8-9gfBl7PtSKTCFqYGs_YjYhUIBNP5M9XhEIuNmSs9qyxhRREaOHZu2KzBl-tiVAeqFAopwksnyg03xKBjnUFPMMmtjWNLgQ8RSDjcuFBbz8K5IDELLHKGOe-fO3j2BOH_fGnlzSWcg7fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16b3ec86ff.mp4?token=PLnSBIMWOttxV-9MUVPG0UuT-mnVb-D_2teyLpqXOKEJkbl7GKamlqUB4qg8m6DaHXL3EP0Ew3T0axUTYtiiRYqVU__RkdXy4kWO0Gaerh6pxMyWKRmb4IgDU1OJ1NudEr5Zy3ym22voiVhb6hcHnAJZpraDA2JcoDGyn70TyUN73HbDTx6SHwqbSUvys0TNdjgCCZ3g8-9gfBl7PtSKTCFqYGs_YjYhUIBNP5M9XhEIuNmSs9qyxhRREaOHZu2KzBl-tiVAeqFAopwksnyg03xKBjnUFPMMmtjWNLgQ8RSDjcuFBbz8K5IDELLHKGOe-fO3j2BOH_fGnlzSWcg7fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دختر پزشکیان: من هم جان‌فدای ایران هستم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/148167" target="_blank">📅 13:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148166">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rwc6cLlw_Tb6HS7u8NoDAUS7t5dI1-Ne3tT3hVgc4YQnfDLehFyNm1vFtGHM5ZEEPlYyDK2lb10qlSBEkVhDNuQM8kiduo4M4fhsNHaj1tSlV63jGbyNtMBoIokLfvUAuS8hOgGq9cdThasImw0EMDXnlBRyBSHf1dU5Rhw350B1kMBW74ZqgwL4nxc6bbJ_xfArjrQQ0nJYuIUkIK7wPQi4_y_Ns9ogN4I1UtYWQ5isE0Nz6cwriKjBEpU-AHmGT0xvfDUzRqsz0nqv_R6eGsTJ25UYj9ScJVPMXjw2mokpBUbuLfEQtvyct2KrNFPnM075cPWC_d75lIPgXqGaIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرودگاه‌های عربستان سعودی با مشکلاتی روبرو هستند...
🔴
تقریباً ۹ فروند هواپیمای مسافربری قادر به فرود در فرودگاه ملک خالد در پایتخت عربستان، ریاض، نیستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/148166" target="_blank">📅 12:56 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148165">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
النشره: حزب‌الله برای سناریوی شکست مذاکرات ایران و آمریکا آماده می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/148165" target="_blank">📅 12:47 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148164">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CPqKRjaeKikmEQF8Peykco2rssQ7jVLGudWs7e-1vwtHHkhL3Tbq9XkK1T0P159Sg_ku8xrdXu6ldTsTcPkRoTiCU2pK1TPwBHydfyAoOqrO1btQsSV696LrrpVVZsOxBHk5qRuOOpa4q1r8hQR0x4jkjCPYbkG2vMw-FNk46YSwyvVQ1ZNcYHfQaocbd-wa6qhc2Zfq5_tIorUHVIlpl-5ZG20rnScP2Tgx-nDDodU5yCaLsJAo3zHEDwIM5kA-Jg9TpgTgJswxbsUj249DOcdHm-yp946c3oIZeea5Yg-ZXMMirxnHYnyj3YTIpVSFzxvIzHdgj42sd-qKhdabQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری پر بازدید از یک جانفدا
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/alonews/148164" target="_blank">📅 12:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148163">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
تا ماه بعد وضعیت طلا چجوریه؟</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/148163" target="_blank">📅 12:40 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148162">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
هواشناسی: بارش پاییزی هم خشکسالی تهران را جبران نمی‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/148162" target="_blank">📅 12:39 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148161">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fnw3wrqNf9_vUgyCNy3i_CaewUZuqp4B4Lq2HABsc6AHtJ3MElZlvienTB2qzeSv0QP3SRjQgcbnmDfEE5s7eLy8Wk3DZ_XwRQ356dAwry6x3RM9YGabNKWxlTslrW_hZC1IYprfoA1aUriB2aUJhi5siZGRbwL-dAHCzHczJppSTrH61T2nmZJP1ITQEZ8jogKVKARg0HPuXdGN1Ehfi73gXIO9SCgNM-hF23e8A3vYk6GePn-CkwunRnZGQQJqKXIIoMVmPYyhbHljs4ion6sP5Btd8gvYh_erHo0Ne3KHwPX9e6QTS50Q0YTJwWD2v1CkeHx6xjEiPw14s0_KGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مکرون دیروز  صبح تمام سران سیاسی فرانسه (حتی احزاب مخالف) را به جلسه‌ای محرمانه دعوت کرده بود. موضوع جلسه امنیت اروپا، احتمال گسترش جنگ در اروپا و خاورمیانه بوده است. جلساتی مشابه در آلمان و لهستان هم برگزار شده بود. گویا احتمال وقوع جنگ بین کشورهای اروپای غربی و روسیه بالاست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/148161" target="_blank">📅 12:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148160">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
جبهه اصلاحات: رأی مردم باید بر سیاست‌ها و جهت‌گیری کشور اثر بگذارد
🔴
جواد امام، سخنگوی جبهه اصلاحات ایران، با تأکید بر شایسته‌سالاری و اصلاح شیوه حکمرانی گفت انتخابات زمانی معنای واقعی دارد که رأی مردم بر سیاست‌ها، اولویت‌ها و جهت‌گیری عمومی کشور اثرگذار باشد و تنها به جابه‌جایی افراد در مناصب محدود نشود.
🔴
او با انتقاد از آنچه «بازار مشترک قدرت» خواند، گفت حضور مدیران در دولت‌های مختلف به‌خودی‌خود ایرادی ندارد و تجربه، تخصص و کارآمدی می‌تواند ادامه مسئولیت آنها را توجیه کند؛ اما روابط سیاسی، قومی، خانوادگی یا حلقه‌های قدرت نباید جایگزین شایستگی شود.
🔴
امام همچنین بر تفکیک مناصب سیاسی از بدنه کارشناسی تأکید کرد و کنار گذاشتن نیروهای متخصص با تغییر دولت‌ها را آسیب‌زا دانست.
🔴
به گفته او، حکمرانی سالم باید بر رأی مردم، شایستگی مدیران، حفظ تخصص در نظام اداری و تعیین مرز روشن میان سیاست و اداره کشور استوار باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/148160" target="_blank">📅 12:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148159">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d462dd9ba9.mp4?token=RYlxI4a-D0IgH52HUvjAp9YCjlXfW8-miq1-c1mu1Grf1keZXPNw4Bx_62Fh6TW-gYgiU2IdhdOpGPLjCvnfj3eS4L2JnRUHw-Y95odk0hwX26gCPf3LLewYQDbsy8EEtIx6rpKqp_fMS82fJT_YDHhIHwaTRQlN5od5G0uxZ2lC4NcXKO_ejCgDoPtq-uA8AEp0jcxZMCnhX1edqdvvJstCCLt33nunP8GyrFkjBxbPHcQ8iiQgB7XS6JGeyUVh4IfHp6NfSD25LBStfO3ha7pmPcS5o-AL4_HPn5_DNtykMYXGN9mPq_WQcWVkL0WuzAZfjG6esdkgFI_jr5uJdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d462dd9ba9.mp4?token=RYlxI4a-D0IgH52HUvjAp9YCjlXfW8-miq1-c1mu1Grf1keZXPNw4Bx_62Fh6TW-gYgiU2IdhdOpGPLjCvnfj3eS4L2JnRUHw-Y95odk0hwX26gCPf3LLewYQDbsy8EEtIx6rpKqp_fMS82fJT_YDHhIHwaTRQlN5od5G0uxZ2lC4NcXKO_ejCgDoPtq-uA8AEp0jcxZMCnhX1edqdvvJstCCLt33nunP8GyrFkjBxbPHcQ8iiQgB7XS6JGeyUVh4IfHp6NfSD25LBStfO3ha7pmPcS5o-AL4_HPn5_DNtykMYXGN9mPq_WQcWVkL0WuzAZfjG6esdkgFI_jr5uJdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک پهپاد بدون سرنشین سعودی در حال پرواز بر فراز استان صعده در یمن است و شهروندان محلی تلاش می‌کنند با سلاح‌های سبک آن را سرنگون کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/148159" target="_blank">📅 12:18 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148158">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
گفتگوی تلفنی عراقچی و وزیر خارجه پاکستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/148158" target="_blank">📅 12:14 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148157">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7aa0bfc25e.mp4?token=F9eg4Pgox5URyVPywy4sfmN8ILt6SB1NqOaucUaaYCq6Tp_iNlxtRZGoMcPA4uPKu06T4GpTdb0PKwpmprVFe8vCaincRxqzKz7W_x1ZaWGRsajS99KA3KK3-5-0fucbWT1r3EmSKa_eu0pwgflngl00yQDRDqnwuvCc4-1SiRl7uxKk4t60RPCMBIkR4wMUXkAUpfbeDpRjIdj2jSpONu4Ka9555sTqNJSXaNHYn3Ulj-D86-msUi4qcviQjTeGL0yko2wtZhY_SCOi4eHAfrrVSauOYMsVXfHdP_YkmgLV8GJFrjyFu0K50Kq9RcbIEmGtk6d-KhEf16mT1OlM1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7aa0bfc25e.mp4?token=F9eg4Pgox5URyVPywy4sfmN8ILt6SB1NqOaucUaaYCq6Tp_iNlxtRZGoMcPA4uPKu06T4GpTdb0PKwpmprVFe8vCaincRxqzKz7W_x1ZaWGRsajS99KA3KK3-5-0fucbWT1r3EmSKa_eu0pwgflngl00yQDRDqnwuvCc4-1SiRl7uxKk4t60RPCMBIkR4wMUXkAUpfbeDpRjIdj2jSpONu4Ka9555sTqNJSXaNHYn3Ulj-D86-msUi4qcviQjTeGL0yko2wtZhY_SCOi4eHAfrrVSauOYMsVXfHdP_YkmgLV8GJFrjyFu0K50Kq9RcbIEmGtk6d-KhEf16mT1OlM1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: هرکس پلیس بکُشد باید اعـدام شود
🔴
ترامپ: "مدت کوتاهی پس از آغاز به کارم، یک فرمان اجرایی تاریخی امضا کردم که بر اساس آن، هر کسی که به جرم کشتن یک افسر پلیس محکوم شود باید با مجازات اعدام روبه‌رو شود؛ و سال گذشته، کشته های پلیس حین خدمت به پایین‌ترین سطح در ۸٠ سال گذشته رسید."
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/148157" target="_blank">📅 12:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148156">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7AFUohYBBGZRo6v4LjevkDnijIroJTnJj6-3_wiUOMnZGeZwAaUdpUGPrH27nDiNgIJQt2y3v2tIjx-IYBJmtfG72OgYVNJ6ZLpUI0TtTDv1XH50FuDG7ydCUO4lGlftOOlMQS3GoUC9gKMeSNLHRkNebNZ8zfHNhDjxZBToTLUS823HJqFRfIJe-TDUm50qhMcMI3pbP17aNU8HzTmwo0ImLos6AgvEW9yGxI_angiVuck55JeAgB6RoywvHtDK-FYVVt_QiyueXfuHtRG9Nw0yOeqJ5mmnx0lBa2w1XVb4IJPrycNgG-e4x3hZID11zSk3Yp0v0N7UAXjtL42-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تعدادی از هواپیماهای مسافربری که قصد فرود در فرودگاه جده در عربستان سعودی را داشتند، به دلیل احتمال وقوع حمله، قادر به فرود در این فرودگاه نبودند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/148156" target="_blank">📅 12:06 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148155">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
دادستانی تهران علیه عوامل برگزاری «دو مارتن تهران» اعلام جرم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/148155" target="_blank">📅 11:52 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148154">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
وزیر خارجه کره‌جنوبی در دیدار با وزیر خارجه آمریکا، از آمادگی کشورش برای ارائه سهم قابل‌ توجه در تلاش‌ها برای بازگرداندن آزادی کشتیرانی در تنگه هرمز خبر داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/148154" target="_blank">📅 11:49 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148153">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
پیمان اکبری مجری صدا سیما : به تجمعات عادت کنید، دیگه هم شب میاییم هم صبح
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/148153" target="_blank">📅 11:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148152">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
شورای امنیت سازمان ملل حملات حوثی‌ها به عربستان سعودی، از جمله حملات علیه زیرساخت‌های غیرنظامی و انرژی را به‌شدت محکوم کرد و خواستار توقف فوری تشدید تنش‌های نظامی شد.
🔴
شورای امنیت همچنین تهدیدها علیه کشتیرانی در دریای سرخ و باب‌المندب را محکوم کرد، حق عربستان برای دفاع از خود بر اساس قوانین بین‌المللی را به رسمیت شناخت و بر تعهد خود به حاکمیت و تمامیت ارضی یمن تأکید کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/148152" target="_blank">📅 11:38 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148151">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
نیروی هوایی اوکراین اعلام کرد که در جریان حملات شبانه، ۱۴۱ پهپاد روسی را در مناطق مختلف این کشور سرنگون کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/148151" target="_blank">📅 11:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148150">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
الجزیره: قانون جدید تحریم‌های ترامپ، اختیارات کلیدی تحریمی علیه ایران را تا سال ۲۰۳۱ حفظ می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/148150" target="_blank">📅 11:28 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148149">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fafde8acd9.mp4?token=dKFbwvc-dD06AD-wOzAeZwRL5XbjDzioBf9jXBVMnWk6yzv3HLfFFdB098GLTa1S13lA8aGmnjcRLYwRJd7wtlc_tRDkCRYgcqOOT_TOAFBrTkbiKtTgT5ksQtcrcMIuD0eoYEecMqxvOCKTNXKjQgBWl0wVpJ45dnChSW27kOUH1efNYMhQSkK6DH76rSeYrhsqkdCoTcLk10R1Sl7e-2nTx7L_vNMDN-ySnkz2j3ks82Qsbx9GfjkFZ1yYbSZ_lvF-OpdmSYKQGeWtvkxEJn2VwAitMFe_esMFtU2lx3lHputuI1nw9VoyBaPpPyYMu-ZkjB36xTEvMbr3fml1fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fafde8acd9.mp4?token=dKFbwvc-dD06AD-wOzAeZwRL5XbjDzioBf9jXBVMnWk6yzv3HLfFFdB098GLTa1S13lA8aGmnjcRLYwRJd7wtlc_tRDkCRYgcqOOT_TOAFBrTkbiKtTgT5ksQtcrcMIuD0eoYEecMqxvOCKTNXKjQgBWl0wVpJ45dnChSW27kOUH1efNYMhQSkK6DH76rSeYrhsqkdCoTcLk10R1Sl7e-2nTx7L_vNMDN-ySnkz2j3ks82Qsbx9GfjkFZ1yYbSZ_lvF-OpdmSYKQGeWtvkxEJn2VwAitMFe_esMFtU2lx3lHputuI1nw9VoyBaPpPyYMu-ZkjB36xTEvMbr3fml1fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
هم اکنون ، ویدئویی از آتش سوزی یک رستوران در خیابان دولت
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/148149" target="_blank">📅 11:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148148">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
قیمت بیت کوین پس از افزایش نرخ بهره در ژاپن به بالای ۸۱ هزار دلار جهش کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/148148" target="_blank">📅 11:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148147">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
شبکه خبری سی‌ان‌ان: یک گزارش اطلاعاتی نادرست که با کمک هوش مصنوعی تهیه شده بود، در جریان جنگ آمریکا علیه ایران، ارتش این کشور را تا آستانه یک عملیات علیه یک کشتی چینی در خاورمیانه پیش برد و خطر درگیری نظامی میان واشنگتن و پکن را افزایش داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/148147" target="_blank">📅 10:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148146">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
نماینده آمریکا در سازمان ملل: ترامپ در سخنرانی خود در سازمان ملل، به موضوع جلوگیری از دستیابی ایران به سلاح هسته‌ای می‌پردازد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/148146" target="_blank">📅 10:35 · 28 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
