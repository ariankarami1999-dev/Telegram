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
<img src="https://cdn4.telesco.pe/file/GE3yq8bkQ16p5KfNgI1Kp4BiaWvo7k82pOjoAtIfgr7CN_3e-D_u626RTinhoyhxxvIOD37Xu5BTiOoHmluS7jeCeiZScrC_OIWsiB2LHY6f3UKXcLef9kLtd-TJiE3VbtxzSmat7FKUqHvjkh_SS706tejLDHlzq6WVutfTtiLr1_5g-5V2_PeDSER3hsoW5zVw1CGif_BMggM3R24N5QGKJoNHJvFiJDmQzjS2RFOcBTlIAaHrUbpIW7YBmEtddo1HbPqGmqv6om9zPC1otoRkCS_IKZtBgLmxg1Xl8kybYdnXEaPoCOMMZC2sVA585RyybcvPRUf0hPI9dG2gZA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 548K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-18 22:26:57</div>
<hr>

<div class="tg-post" id="msg-29395">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RHLyr7MHJbJ1qIQAujBe48Vjqbh--URTzYTL0xZUnvgPcvDNUf5ufP9xOMdvIX__7ORJvDC36knzndnP8e3vgnSPrZm-bCkcmtq_-FVhh-ZWB1BTBWkCX2cZCjIghEHOPiqyITmClNocEJeJiBwlueWdygwCpdPgJBWQkAeINLrp8-UO5Siaw8vs1EvnftqdV5wDgDpjaO31MaYWGasJwzfl1yGq9jITpBAU_HPgj-nz7dKpRYd7LnYSUgHAPw904hpxaRlEZWy_DD2hwkWO4onmVZ01cpeyGcbEatlJNExtPY00UqFxOZtE0dTg8fUw7wUHUi-i-nyuSFXPQGmnLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
کاشته تماشایی لامین یامال ستاره 19 ساله بارسا در بازی امشب آبی اناری‌ها مقابل فاینورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/persiana_Soccer/29395" target="_blank">📅 22:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29394">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adadb2bd3e.mp4?token=T7l72szkelI0BW_lmgAcvnGIl2K8hC3llM4Xnfyi97v1GelpWbM9c0ETlKeOBUX3biuhqraWAKTLSOekLN-DxveXoUpulqiA1CLzVyYNaABdaXplh8EpmqAxYwt68HEh2zI4xZDUzsphz19-Gec1V47vLaqHnI-Ks46ECYOlXtOVH7Dq0t1MJDk-pLs_9Zp3sCPkJ-R3irYR2BcXO2rvPYZga7-aof9dkK0P7bS0Bd9R4dotvrne_pg9gw0w-bQSxdXB7lQCIhc5jMr8khwymMMnW222CO5Q4t86bDph6uSuL-6qddgbOIs46a2Mb_8iYo4cXB68KmqXgwWLfOd50w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adadb2bd3e.mp4?token=T7l72szkelI0BW_lmgAcvnGIl2K8hC3llM4Xnfyi97v1GelpWbM9c0ETlKeOBUX3biuhqraWAKTLSOekLN-DxveXoUpulqiA1CLzVyYNaABdaXplh8EpmqAxYwt68HEh2zI4xZDUzsphz19-Gec1V47vLaqHnI-Ks46ECYOlXtOVH7Dq0t1MJDk-pLs_9Zp3sCPkJ-R3irYR2BcXO2rvPYZga7-aof9dkK0P7bS0Bd9R4dotvrne_pg9gw0w-bQSxdXB7lQCIhc5jMr8khwymMMnW222CO5Q4t86bDph6uSuL-6qddgbOIs46a2Mb_8iYo4cXB68KmqXgwWLfOd50w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
مقایسه‌عملکردکریس‌رونالدو
🆚
لیونل مسی به مناسبت قرارگرفتن لیونل مسی در لیست 30 نفر کاندیدای توپ طلا و غیبت عجیب کریس رونالدو!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/29394" target="_blank">📅 21:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29393">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/135ac654e4.mp4?token=fkDZ3p17jmBSMPE6-EKJ8PkQtVCl8dYNKK87XCIiXnEfUoOyRspnDuLv9IuFC3kiLDFQDfzLYb-aw-v5bfg-s1QaWhO1CrM8UJsIQN8NGbQQBKq56vsTXn40j8qLJ-DyvnpmKePOuq2tHF-JYVfLxLLUaMxvHb965Y-HCjja4lNCDlDMnsc-PlaNh7qQOfHF1NLyfl27_v-OdXIthGOKV_vxGkTSolVJqEVqrlFQhTX0frDnhCNUfsg6422xxGwafS1Bo4-Z0Vygbo3TBcpvhl9lTLTDUCbJpiF2VA8_ox_LToUMa1JrNa1oG_7hz3Lk6xtcF-BFcqflcmDvGqEKXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/135ac654e4.mp4?token=fkDZ3p17jmBSMPE6-EKJ8PkQtVCl8dYNKK87XCIiXnEfUoOyRspnDuLv9IuFC3kiLDFQDfzLYb-aw-v5bfg-s1QaWhO1CrM8UJsIQN8NGbQQBKq56vsTXn40j8qLJ-DyvnpmKePOuq2tHF-JYVfLxLLUaMxvHb965Y-HCjja4lNCDlDMnsc-PlaNh7qQOfHF1NLyfl27_v-OdXIthGOKV_vxGkTSolVJqEVqrlFQhTX0frDnhCNUfsg6422xxGwafS1Bo4-Z0Vygbo3TBcpvhl9lTLTDUCbJpiF2VA8_ox_LToUMa1JrNa1oG_7hz3Lk6xtcF-BFcqflcmDvGqEKXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
سوپرگل‌استثنایی کریم‌آدیمی ستاره 23 ساله تازه وارد بارسلونا در بازی امشب این تیم مقابل فاینورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/29393" target="_blank">📅 21:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29392">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8GS55aZG-GnbfZbOHr_Ch7LvkkEs0c3gfs9rjrqv7srkdEuQu3-Zkj5rJa-XOcnSw8HkwJI5YzGrCmtLQhZRZmbsyvOLrubTFfAqfcwypH3EhtAgUi2Hpo3Mr5_7thaDQycAAXIaV7WmYX8Y9MgXBo_bDuG4hxi8xBhzRgBcVCjKsJXf1ADRGc5Sw18O5rSO_bpvRdWpHNMtlVB091JOi-mNNlKqoxjGfHg25tCiAZgfrwQHO6hldGK4hEKKWg9J75In7ZfnguidCUp3YAnvwyN_fqZPFfvQr9pIvRjA6cI1W1LHaMSZT5oBhJyeJpDzSpsBGVnYSWfkSSdE9Tnbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته اول لیگ قهرمانان اروپا؛
شماتیک ترکیب آرسنال و ناپولی و شماتیک‌ترکیب اتلتیکو و لیورپول؛ خولیان الوارز بالاخره در ترکیب اتلتیکو فیکس شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/persiana_Soccer/29392" target="_blank">📅 21:39 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29391">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a9709bebc.mp4?token=BF3J8Tnw0hdHjDapINdzpT1va7Xis9NEiMJ04V_VcLMGDlZ03iB_S9JFlocSGHd50DDg_7N_d8bUCReNlflVPzt3doinSrJXbCK5c-D88IcOwG9Uhz2UDKWd57VEZVQQa6Q9uSfj5ItVjmvsTonipI_wETPj1TjoKz6Mc7a3dI5FJWMbjRKKeTCKjBx0VK-M0KjOS9PqlDjoV7fUMr4uodwsubThPlonZRuK8EH-P3BXQGt5by8qu2nGMf6mtQ4lGGfjBTfbRl4vigEkV5CjvcJPmENOJNvB0tQVxMcYcQn3DhDMRqF1N_dORqzUyUNWgcB96vlrPkZT0wC5bkTbrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a9709bebc.mp4?token=BF3J8Tnw0hdHjDapINdzpT1va7Xis9NEiMJ04V_VcLMGDlZ03iB_S9JFlocSGHd50DDg_7N_d8bUCReNlflVPzt3doinSrJXbCK5c-D88IcOwG9Uhz2UDKWd57VEZVQQa6Q9uSfj5ItVjmvsTonipI_wETPj1TjoKz6Mc7a3dI5FJWMbjRKKeTCKjBx0VK-M0KjOS9PqlDjoV7fUMr4uodwsubThPlonZRuK8EH-P3BXQGt5by8qu2nGMf6mtQ4lGGfjBTfbRl4vigEkV5CjvcJPmENOJNvB0tQVxMcYcQn3DhDMRqF1N_dORqzUyUNWgcB96vlrPkZT0wC5bkTbrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آرش فرزین دامادسابق علی‌پروین:
بعد از شش سال جدایی هنوزم لادن پروین رو دوست دارم! بت زدن ‌هام رو بازی‌های فوتبال باعث طلاقم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/persiana_Soccer/29391" target="_blank">📅 21:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29390">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KymZFUbrAriaByXA6HRbB2yxl2fCCynpuMWCtp_CrHjaFwQ0glCANs3CsFxPdyfsiYm79X7voPa8l4O13jLvFqyvtCV3V-vsfC1FQWGEW2P0Rp6optd4RukkhfhPn6M_VsHeOPzmV2R4-KNShdrtoTNTkR3A5HovO2NRLnm4pMDfrpGeYBSzbnJuBkzDdCJNiPNvxpZzpeJF3Mf_F55a6gpv75EvlRN4daETf6jPmijkeMLhbNldqFCVHWWwi3hvRPI8w5GLVgJCNWy0FhpjVApuUeCP0_j_qwZo7Lnz_HfS6gAfmOReDP54iunSN8U7NBh7Hn5LHDzSq4tjkX-7Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇳🇴
پدر ارلینگ‌هالند ستاره‌نروژی منچسترسیتی: شاید روزی در آینده نچندان دور هالند رو در تیم رئال ببینیم. ممکن است اتفاقات هیجان انگیزی رخ بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/persiana_Soccer/29390" target="_blank">📅 20:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29389">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/448238a183.mp4?token=cmrVQMn97WoqAFzpyjRXYA38feZ2SgcfiKuk51dXhq1nB2PATlvht8xeAWeGXKwOZUOoEBjfRmXHf5cOOIf9aPmMwfEGHvRYQqYcoUsNQ7SpNCJmtMcqJFwFMKB0XtwVhu1YpSbGQW1TPkqZv-dnf3LSuFrhAEWsQv4sxz35Y_2lwkNGBl4O5DNW1lN01xfgLH9kZOnMsDQCVfkXu3fNBrYrwx84mHQJybT7on2ZCHIsuQnq0m33m7b3KpNy4Nb1mLz0Kd3nba6qPCZ5skOiSRUTym-sAERkBiom-iCTJBgpXxgPS2Gnh8O1dSbquiUvr7ZYjKG_99nPsXO4tns1sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/448238a183.mp4?token=cmrVQMn97WoqAFzpyjRXYA38feZ2SgcfiKuk51dXhq1nB2PATlvht8xeAWeGXKwOZUOoEBjfRmXHf5cOOIf9aPmMwfEGHvRYQqYcoUsNQ7SpNCJmtMcqJFwFMKB0XtwVhu1YpSbGQW1TPkqZv-dnf3LSuFrhAEWsQv4sxz35Y_2lwkNGBl4O5DNW1lN01xfgLH9kZOnMsDQCVfkXu3fNBrYrwx84mHQJybT7on2ZCHIsuQnq0m33m7b3KpNy4Nb1mLz0Kd3nba6qPCZ5skOiSRUTym-sAERkBiom-iCTJBgpXxgPS2Gnh8O1dSbquiUvr7ZYjKG_99nPsXO4tns1sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇺
هفته اول لیگ قهرمانان اروپا؛ شماتیک ترکیب بارسلونا برای دیدار مقابل فاینورد؛ ساعت 20:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/persiana_Soccer/29389" target="_blank">📅 20:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29388">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
#تکمیلی؛ پیج معروف 433 سه پاس گل دیدنی نادر محمدی باپرتاب‌اوت دراین‌فصل رو پست‌کرده و میکل آرتتا روهم تگ خورده که این بازیکن رو بخر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/persiana_Soccer/29388" target="_blank">📅 20:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29387">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_iCbwshzwJqlJ3VUwMQa1d9AzjoFvCWn9dqioXwrNLj0mGt-hLy-4zSIGnven-3_YIpEwcQlMxhNNLstYHjRV5li8ygnJYza-s05qomKm1Mz5pFxXjn2DPhWgC8Xi947C2Q7zyFdjLUROC9qFkAgdm48Hzri6Xykua_jdDFYgsmKcFBgY6v1o28jyi33lCEYsl5klq_cJfXf3GrRIhhjI9FfBStOVTCJAWzGCXNN152IWTdSLxv5QXqiLq2WiSB-Z2tVqeCK75dhBUpmfzDHXBSXJeirIIpjCPAf-e39MmpFmubsqlbUuuzpcCLC2AxIbKbhocFdch028MYbvj5Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
طبق شنیده‌های رسانه پرشیانا؛ سردار آزمون فوق‌ستاره‌خط‌حمله شباب الاهلی برای جام ملت های آسیا 2027 به تیم ملی ایران باز خواهد گشت. بازی های جام ملت های آسیا دی ماه برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/persiana_Soccer/29387" target="_blank">📅 20:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29386">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RYQ7kXPNXRzxO8bXoSjE84sn1pacXfq2OCrUeOny2A-JT-QtDJ9TTgahFoo7Os-XIUPfcFWggpVPnp00LL0lq-GN90mj56sAQHL5Gsw-z9v472TTUcN3kUN4Rhd9nXhxxGl1covbOfDpxWuR54HsxU7WQCBK1R7_4xlSoRXHRU0sjvS4aCTA9Lsik0ocn5f3D8qDRoRvWxP_pnJc3RHyERueqsYEhnqfgc3nttsosUw2YdmYDp6K4y_XeFUq80laDXwRsC1xzV7_2WoJr6E8i87b1VdZG3blZzRbnp8PDsyO59pf-rKf4bM0ARpg9_oD6N-wG8jPNEGFVDw1akC8BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
اسماعیل کارتال سرمربی فنرباغچه در نشست خبری قبل از دیدار فردا با آاس رم: «آاس رم فعلی قدرتمند ترین و با کیفیت ترین ترکیب تاریخ این باشگاه است.»
حالا
ترکیب فصل ۲۰۱۵/۱۶
:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/persiana_Soccer/29386" target="_blank">📅 19:52 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29385">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YlQqoohh6whSrs5JtYcR3d7c-BuvSblfdoPGuMl4QkPqL1xyY08HqVopLX8ZbHtTE8dh9XSQ6A3q-Rj6iWV6dHPmMugf_bvja3e_HYxgR5naovi8Yd37xpbVzyo7_5RTDq-x5RkkmS4d7_DdZhP4QvPyc3D5mhDZGwlSK23i4oYAlmkGh8NzfQ6CED9aMBQEqKaqDkAZLCOTYTgn1pM9gvEnMlKSx5SaNpWkSijYQlYmgrP1TyD2DW2-WaH3L0rMHm4dNXB8DMjKxb90ZDiCp8GgavQQBc2CHfVT_Qg6nk4xLi-j8bwBsCaXKqwEF2Jsg3-_botE6bXF4ARkfPCsaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین‌بازیکنان لیگ برتر تاپایان هفته ششم از نگاه سایت متریکا؛ مدافع مغضوب کادر فنی آبی‌ها در رتبه سوم! علی علیپور بهترین بازیکن لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/29385" target="_blank">📅 19:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29384">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rM8e0Be2-z8LOx4_Y3KNjqhaI5sU-X3NHSKau5wa0D2e_-zdDBdIbuknhN3XgXsVdelmGaePbpbtqm1HN_JnST609OnsgxaHeM9L8EI2QDVf0pu41Mmd2wTY46NbURlxWFXSSTVL5q1GTn39A-uWkWysDq1EaJMc4hQB55Nsfuf_i6bAx9k22kRgFBzxNP6swvtp5xkrXDH-kRnsZqPgKK-QJ98I_rudF_RjN431D_NYKFJ2mdpsdx_CiwDAuAlphkVgvQzrTLVTW3i4hB5shUw8lphET4ydSLofP08Vrdqk1WtHzm2MZyzH54VfcyY3hlGvaOq931HrV5o-dqr8Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته اول لیگ قهرمانان اروپا؛
شماتیک ترکیب بارسلونا برای دیدار مقابل فاینورد؛ ساعت 20:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/29384" target="_blank">📅 19:03 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29383">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s3hv0ywSTFqRLo99mNobN8dk9BXD1ztau3aFZz_tx_F312MZ8Xvhyb2gtpulKqCWF5oUYo3UBDG8e2zgUZhpFNOkU84ii8so5u2ecBiGiGh90tXBKta9xBm1Kf051-ZqDGL3ictaXf_lQUQ1U_82NBzlQR1zKuIszq78FHmbcJDmSfmUvBSOwegdz78jgCbtnXJOGZ27GzMcsXXXE7XGVJNcAcG1obwi5lmhKYYGMj8pDADhAM5XS2Vnr-hoHq8Rlp-DET9_5c7QXTAC9zYccRpYUGzhq-Gal571Xw5WYrgCbD2GR0mCyLw4cVglgIGI-QmZ_NNchq23tipjvDOoiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
فرصت‌های‌برگ‌ریزونی‌که‌بازیکنان رئال مادرید در بازی امشب و بازی مقابل بتیس از دست دادند تا اولین شکست کهکشانی‌ها در لالیگا رقم بخوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/29383" target="_blank">📅 18:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29382">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mtUYFPErhWm_buH4AOvM3zYJ-XL6AO_JZAm8BV8bjkVqvHXM3It8ZjAnvGuZc9CBMd7R97YRNMyDoyRI3djsiVLCXW0X68HSUIzi6IoNyLfCF2zBg6FSCSDuRApi28fz2BEUWo7OdIglfu9rd8vsMyTWnJGRq2hRRjqgssvOm9mLEQhnxrTFQN45_WBD-96Qbxm9NSmhXRfhCspncwP691yhOSOkOZKKm-KIDoS3e78T3sq-juC-iLju5qcFxE6RNOWLmXe7816wjDzdjTrZ24L9oyhInJdE0l29DyxetcFq8RfRFQFej4KelySnJJNpysrfhwBFG0ZehHpV8xKQ8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
با حضور لیونل مسی آرژانتینی؛ لیست 30 نفره نامزدهای توپ طلا مشخص شد، مراسم اهدای توپ طلای 2026 روز 4 آبان درلندن برگزار خواهد شد.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/29382" target="_blank">📅 18:26 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29381">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gnwlu6dqFI2QsWQB_hwdSsiOcUrKzx_8poFjv_zH36tl-aPqD6LPU79to6fCswh1j55-s6LPfomvbWAQ0kenjxectfnVK8zCzRb48y9v3b2DmQI0Abx-RlrIJF7LY3N9DZ5euwxKenNpVRAX9Qbt623TuovsArgjJe9PNh1V04Cp0OVVJ6HeSa7KXiC2JKLXgPMm1fQIwcT6WNck8b9CWwb3-XZsp0CRWAzG1jY5OPd0ahG9dxvtjNH-RHGcM9baG2oQbU0OKcLfSQQcADeB0ffHAXohUH0rA-rjNDk5N_LXH6PP7PsIjOgAYBWHwT6HC6DvQArzp4E4grn8XReo4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
لیونل مسی و کریس رونالدو آمادگی خود را برای حضور در مسابقه خدافظی کارلوس توز در تیم بوکاجونیورز اعلام‌کرده‌اند و بالاخره بعدِ سال‌ها این دو فوق ستاره در یک تیم همتیمی خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/29381" target="_blank">📅 18:26 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29380">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-4YbP9ZnEDj1iw4EfHWY4yGRmLNp51pt6Kbdy0s1kJQK5ALlIpMReKhSHZ8_GM0kr1teVYKeKr0kH4GC7w-Inu1wZi8oJLQXBuJFvHFpxneShMspDzjU5t0DHRZ4_2Ez-nJTkJCDEs5H977jJtCqjNt9pNScKYufSDclm_RffeiUvehSIY65XAOKAN3tX84FOKKepUoUq1k_-zFbkQaIWDydj4Df1zVqECsZWgkiFqI6QX_blQ1UPRXIbQyjrTBwkr9PTKi8awDriDowLnSjxfQmcRuVTH3nE1Ascl294YdXgGfUh2gFZQaMgwCVMD5u_TZu8BlhBxF9rrYIQyfsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته اول لیگ قهرمانان اروپا
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیورپول
🆚
اتلتیکو مادرید
🇪🇸
⏰
ساعت ۲۲:۳۰
🔴
بیش از ۵۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/29380" target="_blank">📅 18:26 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29379">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYQIM1eO7SdjJV1ZyICbXxxIBdxncsSDIQtZ2rINk2lpI6Cd9t1tMUR5amUldexCuWlWhlTUP4RLJTuV2U58tG0dFBpByN8i5JiSMBnhJebFXdgVTvuvhkXVYLKRUiu8S5ntz-olcqhebk3i01iGHWTkBHfQUz-v69RUf8wwjNCFSSGM3Fv0oYgjdsuWoIC0IgDW8rI0z2JEKg9Is4L2F2jfcfxp9c4OMixHcMUfK-7Ui3guGPITHwmDHASr5hAlH7LS3isjAVlT_yuqnKXSCy106d8Ka_8ssmNUbvCRuqB9zpMc_OSqZqBW_s9PjRVjhNR0UT8GeXgMhJ-yKZf8EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین‌بازیکنان لیگ برتر تاپایان هفته ششم از نگاه سایت متریکا؛
مدافع مغضوب کادر فنی آبی‌ها در رتبه سوم! علی علیپور بهترین بازیکن لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/29379" target="_blank">📅 17:47 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29378">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZbDLfDpqlCN94zk4rOL6THLo2liDQaQ4Kbt5hIJZY7O3KEZYwzltb6vzJH3mKkhy5Z2VZ4E-NAsF9D9k3EOowbHtArzvWtKQTjuHda_fysTcyiV3DI-E9EFcYPcAKk_OwZcaZL8uFocOF7hHwkbWqQ53UNLnlFxDhi7DiyT_RK_zt6bkgzxBH62SUprSJYGxNKqxs7INf-zr7awA0DFeBh1OUxxCjK5a6AutYm0TdD2wYc69ZlKepF1dQ-CNC_W8qYQm2MNn2YtPCsjeZfmT-y8Nycd7YWeGH7m7eUkh-Obq1VzJKQ65_DhExUcJAylMhPuwXI-ukBrhQHTgHWB_XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍏
💵
قیمت‌های‌احتمالی‌آیفون 18 که قراره امشب حوالی ساعت20:30 بوقت‌ایران ازش رونمایی بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/29378" target="_blank">📅 17:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29377">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EaCCu9F7l1kicBoy-qmvcZ1hjXUjjpN0TcWlqFxVDG1U5mkbqEi2-2LW_QARR8A1g_hXNleb8aJPtAaOI5bF5y-_mW9KiKzezlInDlrmZWATt3MxPmvEFtj1b6LM575u2Zil6dXEU8AgEo7RRh6Vvp2lzeUccagjkQaX_tP1m73q56fLL9sfDVBCwjZtoH9zHuSuSWLqeESJDvIxaGUjES3916aEkJZzySf6TRYoVbMdo2RZUc3fx55N050wtGpdDOFCBIP7GleLRuipvAVGmRSgxK0htnvcmTDSuoHFxs4ZOsOdJd3laSOkc7hPOOWMHGDfSVMn0ir-N0euFW32HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رکوردشکنی جالب پاریسی‌ها در تاریخ توپ طلا؛ نامزدهای نهایی کسب‌توپ‌طلای فصل گذشته فوتبال اعلام شدند و در اتفاقی جالب، پاری سن‌ ژرمن، فاتح لیگ قهرمانان با ده نامزد رکوردار شد. تا کنون هییچ باشگاهی در یک سال ده نامزد دراین‌مراسم نداشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/29377" target="_blank">📅 17:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29376">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHg3cQjnbwa9t8qWQEXAAv5S6uuuChatlWO-1YpFMmV0gEVqDRkpHQsEBE9J484WDwF8sn959G0K_nFXx-GlsdWj1zF7VC5YHWe6xDjOF8UPiyYIxihjXHFYR8lUx42ZVbPTkbG0zZMXt3Rpia78Dl5yJHMMX3fVz5eqxuTx6GnM2RqIzJH1SRZv9bxzxF8ZBvMfPp_6ZnfhYuDfSSTbfsDRMkfPyLYupbL7dMb8KmJ6iuqYvdNpxPNv1ejRXu81hyF_VYkoUWITlMyw6-rhruCJiKl-RaAQX9ETbiVxNL5UbfhzPH8uwmXz70_HK02XJrwCATN_wYMwGQEeUSUNNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
فرصت‌های‌برگ‌ریزونی‌که‌بازیکنان رئال مادرید در بازی امشب و بازی مقابل بتیس از دست دادند تا اولین شکست کهکشانی‌ها در لالیگا رقم بخوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/29376" target="_blank">📅 17:01 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29375">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jH9G88Q6QFQx62by5HAlzbzZ6f-V7nnW2X83jrPV0IC9Gy5IkKg1iwT3Jgj_hUq2ehx46YaVLJLM_Axmff6QHwfWp8RP6KXls9XFuCfpVoyjVM-ODjpWFoOQKUCvSgPyQKrYVDx2q72JOUlRFKEm7Q-Iylvjqgad4dUa8NYgq9A-IaK3nAWmeGcbtt3B-NayAxrWaI_qSj3ueSeup3Ap0mcD2Esam5kO26k6Aj5ythENkfUQLspZnZmuo1SKgtXZ-yUaXQyaJvz6ofIvZJxriK-rX8eORZF7TkVRa4xK0DIwvV43kvK2QMg3c0Y1qvLXw1cBL2TigS1OxD4K1qqkPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛همانطورکه‌پیش‌تر هم گفتیم؛ بانک شهر بزودی تغییرات‌مدیریتی‌درباشگاه پرسپولیس رو انجام خواهدداد. باگزینه‌های مدنظرخودبرای مدیریت باشگاه پرسپولیس درحال‌انجام‌مذاکرات‌هستند و بعد از به جمع بندی نهایی تغییرات رو انجام خواهند داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/29375" target="_blank">📅 16:36 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29374">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SotgEW-pUm-wf93PlyD5xb4Wn4RYDgkp8eqXNbTdu6A1_oKQVcc1iz9veb0KO4PywkmOawHKL57GEXjEmHCoW-tlG-BJjUiQ5GgLKo4zyLVV0czg8AI_UEAmD3crP3DFomydtAlwFBbClT-Zft8QFmfA8OHpL8tmNjeaLtN3NcSiEP8bo16GSnTnJ1KI5mppyKXeJA56BjN2it592HEzzrK0rQK5-4TgXD8BgCO-N8uefXkOovzTZ2FUyJdRrbhdzwDy8vfXEOXGXIMqbD2LEbjlkifCvjZPYn8xbVeEx0kOzXbCW_O0bFTeUleBQRe7rQmfrv74w2IFM4XS5MJ4og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ برخلاف صحبت‌های امشب پیروز قربانی سرمربی تیم آلومینیوم؛ باشگاه استقلال مبلغ رضایت نامه محمد خلیفه و بهرام گودرزی دو بازیکن جوان‌آلومینیوم روبه‌حساب این باشگاه واریز کرده و بااین‌دوبازیکن قرارداد پنج ساله امضا کرده‌اند و نیم فصل به جمع آبی پوشان…</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/29374" target="_blank">📅 16:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29373">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B1N-WbMqJloSquF5SiUO4flBZSpOgCN5jg6V18610qJRNc4nka_bIVm8lienD2RO6a6gWIiVN_nwRahHtyEBD6H3qR6sv28bqan5Z3rLpbSCxWzUANDlu2-FcanWl0ksFMTfxaMOB0XdRuCQwlDHxlCWYiR6OO2WXQ6bD-KSNcCbKFneGjmOXGC1KTI9dnf7ozsd_ZD0Yz8yE0Zb8OTwQFimvmDT9e5KD3Q-VphIekTvZO_wJkDU1bvQ0ZAI075I8MwN1Z7LUFg0-zpFKrryeXMVDATtjo7IYUenVuaX2WjfqANN3KljEoxOG7lcqzhPYGzXUnuK0EekoxhC3FVKjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
خبرنگار معروف و محبوب شبکه DAZN ایتالیا که مسابقات جذاب سری‌آ پوشش میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/29373" target="_blank">📅 15:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29372">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALJQZybElMpwd5QFOEg_psp8e9MvnwAbyPTw2rWoAnvuAjwJPg_3Fc_UXuQ90O8PyjVdTsxJBD7dOQOV_Y0hQ7yjdfmG0fx3JTebdW02Oe2FLg6Qn6JWBdbQ--ksvHrg0r71ehcv-12ukD7Jz4jxYi_noivbE39M32XXx6hpr8xD0vKIko_Msb9G7gN4mn391YeAbzC1rwI5jnCxLlV9Vy8ZqMj_99_dTSgBhV-NpuVvQUBqbVRthlD7D_Y3tPicRocj3jsDSx2lRY1ZhFHrcyCKJDnRsZSoVhb8Vw9AG1L7hfJCInHL3V_ckkV0Tlgwy-sDDYLwy7nbR9Sx9m0-pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
داورهای هفته هفتم لیگ برتر مشخص شدند؛
وحید کاطمی مسابقه استقلال
🆚
پیکان رو قضاوت خواهد کرد و بیژن‌حیدری‌ مسابقه روزیکشنبه دوتیم پرسپولیس
🆚
خیبر در خرم آباد سوت خواهد زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/29372" target="_blank">📅 15:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29371">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tjWACcOCBoy6tneiI_Vi9vP9SkUumwAD97OA3eZiitZ9EYGDNH7OkFNHbjF08UYtUdPfYdmhhwxbky8W2soER_iC-V3vtihGH7oFyKAqlcoGCWM_W9oWu_gXAm6wr-Aza2bJFhqFsRoCCNTXbHa6EhcCsP63w62p3QQerA8HtIe59nhbI3DIlO8R3_2GNdNihyP1vgYH6COs6iODLMA2fN2hmObjSa7dmHByF8TaoSeIOqqDHLQs9yAssQRKxWKKymAl92rLgnAr5Y8scDUiQWCgV39_6Wkh7Ju_YcZCkVQcFD8Ycs9IRsEuSxPo28LrdAUaKpMnvnxpe1JH5Pb_Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
خوزه‌فلیکس‌دیاز:فلورنتینو پرز رئیس باشگاه رئال مادرید بعداز فروش نیکو پاز به کومو با رقم 60 میلیون یورو به‌اوقول‌داده در تابستان‌سال‌بعداو رو به رئال مادرید برگردونه تا برای کهکشانی ها بازی کنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/29371" target="_blank">📅 15:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29370">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T0vNJi7DZ0d8GgAN4uDrUKV_znoOgKUu0DrJI-am5ObVwJvV4pnhyc0CLIYrTIneSllTlw8sMuaWNZHkKpGOkXhvezIJZRNgXkLGLiZTmss2_SBj2AkbbwkW_sYTSzguKPgc-fiNT5AHK8Ucs_HcNttBzPQHJyNQPTffAlOROm-JiElHlxdpxnUN4_xS1bi_1M6RpCtUBAELQuIyoH3g-nOJnPJTstEqI2gskvtq9HtO22G0sWXe48fw9dIrLuOcvSvf1SznBQH8y5UTC24P6GbHymodDCMfC-KKi91acmL22yub3FLUpyamJfQP-0iPcgi1mxLBvcMLwcHdEXqdFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
با حضور لیونل مسی آرژانتینی؛ لیست 30 نفره نامزدهای توپ طلا مشخص شد، مراسم اهدای توپ طلای 2026 روز 4 آبان درلندن برگزار خواهد شد.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/29370" target="_blank">📅 15:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29369">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gTLWtUK_Z53O0bzBxv3b6WWudHO4Qs3BG1YBn4yhtCUo-1F-12IiM36KTS05j-b7YoddX_xALlnqr6yPz-obL621xNZ8EaYsIwnwB4BZn-ffbBfH-eQFiPiSa9ODhmQxf_yrlPii0S65ovlOAgbBCzme9mooljMq58m8wD52qGQmoGU9MwwYVhe84rpjTKJlZC_0Xq0p2i9Ejvf1qyKYFY6JUN5V-E44z7lH81ZFPOWHKevOs70cHuIweK8vMyzhEUuOm8goZdWOIFYzrTd9QYHzlDWGQKgC781yRqGZZaGUXuZ2SLKgPsQGl4RdG9PpTvMqwR8_a4brmXQup9lLdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛صحبتهای‌پزشک.پرسپولیس درباره مصدومیت عجیب مهدی زارع درپایان تمرین امروز!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/29369" target="_blank">📅 14:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29368">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMAJwSgzyiQmvjFQ_cn2PnSLCnHYSm1E6xuRYCKFG-CeLzyxW8Etc8iXTPq2RSUWxAwzGr9l3Chgm_V2eEDkIL8NQhAk6kYkTZgta9peQ6HkAHSzCMNTIS-Ng20HyaI8vMLQxI3HpRdWpsZOJJPB-CzoGM6iSndphiEi76lQmiSshokwnbFqY-uYimAYOgWFVFQ9bsgkV8bgPkL5G2uMtZhrKv5KQBuyg1M_e7CUUWQ8dPMzgBBaoX_ggw5J5S7umkL1vqfgYIY-BdJ9oc-70_d_s5FDcrqytyLhYHuBhfijezk4ur7ef2QaTcPSooiy1AKYgEeTHN_ZzAuVpKcu9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
لیونل مسی آرژانتینی ساعاتی قبل با خرید 100% سهام‌باشگاه‌الدنسه‌مالک این باشگاه اسپانیایی تو دسته‌دوم لالیگا شد. چقد لوگوشون‌شبیه بارسائه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/29368" target="_blank">📅 14:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29367">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vk_q0tU0I0Zl6J11qzMA5GjRBIfF_pRrUJa7uJDqBhBvOcyDqbaiUbrVCw1IxB0dYj_I1CyJZH_KAxNrLWKuX52Bb7L22wImX_g2C3cdQuxzyJcAFoE2uE8ilM5FvgLrOl2Ac-C1OkCz0B2ZPLnYhD6aMLAgjUnESn2LYRvXT3EHXAfMxcO3vTMn9wl0mIECB_rSYU-JnQEaNMJcjOhAQY0P92n7dbuW2ktyK9lVvBXEDywVi6ouqBL_LApDfPZteITubUW14Ju9GQ42Q7daHsQOLCgPZVdDrIkV2BLXgPabSZSd7mhEn428T_1ZmNIx4BfaCMFYormLx7ALZgW4xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویس فحاشی برگ ریزون و باور نکردنی خداداد عزیزی به امید عالیشاه در پایان دیدار امشب؛ میگه منتظرم بیاد بیرون کارش دارم!
⚪️
@Persiana_Soccer – ویس فحاشی خداداد</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/29367" target="_blank">📅 14:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29366">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aXxWcxnPv3YdyShoGve4G7dUo5KdCReZ3on9a4d2AiO84VAM6kcJh3gZnmj2oZcjL2J_Km2rQlw160gGQYgwEVZ7tyCXnRHyluArcfJ9OHiiK9Hlggvqu3BJaqz7NLKkXX4nM15XY-UVxqbPHuzmGtPzklVe1ozxAxpWn9TwnGlprc8Hu4ett7V_dlNhQEuGmQZIO0iBexKAgPUBXZlCNYty0vdQyNN2X5U-VlZq0hSkEKw4Vwd4asGZ95vjp6prNKXVcp-5cbfNzOX1wOzMXSzWhn044CzPZivnxNZphYgyZCbpdMQw-9HW8ENS12Qut_r6Akg7fCwdZX3_ASBxew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جام‌‌ملت‌‌های‌والیبال‌آسیا؛
تیم ملی والیبال ایران درسومین‌مسابقه خود درقهرمانی مردان آسیا 2026 بانتیجه‌سه‌بریک موفق به شکست چین شد. شاگردان پیاتزا بااین‌ پیروزی درجدول کلی‌مسابقات در جایگاه دوم قرار گرفتند و در مرحله یک چهارم نهایی رقابت ها به مصاف تیم ملی چین تایپه خواهند رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/29366" target="_blank">📅 13:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29365">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/765da8fbb9.mp4?token=mofjB3P5iJVz10L4Tc6a2snuVa_BdTXpvJCOKrS0l-FcX0WQ1N6L2IozHTRDvzZMVA2xC8CxAcMCidjmUscBRLZO1ed_VFAiIJczzjGsm6Uhz7bWS_-eBsM5bBiVEq4OTJDF_6UOWbN-iXm6G0GSHLCuK46Mlg9vauw8AyTXJ2CrlNkK9P-ahUSh1t2fk9mUDABqGyjJSvsqLi1hPVn1y9qbVIg10WdyUOxcbMvXfz-t5wmkVr_2-vi0ZjiKnRLAHr9Qc4we5j9i2Vx7oKrzw5gpg_OXokccSWs9KSH9w1wyE0XBkoChp_58sXpuFwxZLDGGpwPWdgBX9h3r6od0dLq2ibqPBS_MiF3AXnm7jYUmnS947s_6NNDXoIVNnB-y9xncVnzmYHqWDWfrYHh1aJDhKHi--71S5wCUL0HTeTs8h8jOcSWWbeVXNHZVVqZnn0LKhSVf9G40AcFURhww9diEx5abvNSDcBDQso08SgzCGnB5XJrImxQEsnoRqb-2vwX_zbNIfybgjOL7cKm3UySTRUcOpNxsyX7fkOktMGUq8rVzf3NKUYzR33EOB9iX68LYZXu1ZofP9awpO9QeVtMRuptGDHg_vBnYl8bsUxEvWcceFmQJ_uwUQgPIzpu3rv9J-RUhzYaPJOdZJCIrv5ypKz1iS9UAQZzgjBfu-1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/765da8fbb9.mp4?token=mofjB3P5iJVz10L4Tc6a2snuVa_BdTXpvJCOKrS0l-FcX0WQ1N6L2IozHTRDvzZMVA2xC8CxAcMCidjmUscBRLZO1ed_VFAiIJczzjGsm6Uhz7bWS_-eBsM5bBiVEq4OTJDF_6UOWbN-iXm6G0GSHLCuK46Mlg9vauw8AyTXJ2CrlNkK9P-ahUSh1t2fk9mUDABqGyjJSvsqLi1hPVn1y9qbVIg10WdyUOxcbMvXfz-t5wmkVr_2-vi0ZjiKnRLAHr9Qc4we5j9i2Vx7oKrzw5gpg_OXokccSWs9KSH9w1wyE0XBkoChp_58sXpuFwxZLDGGpwPWdgBX9h3r6od0dLq2ibqPBS_MiF3AXnm7jYUmnS947s_6NNDXoIVNnB-y9xncVnzmYHqWDWfrYHh1aJDhKHi--71S5wCUL0HTeTs8h8jOcSWWbeVXNHZVVqZnn0LKhSVf9G40AcFURhww9diEx5abvNSDcBDQso08SgzCGnB5XJrImxQEsnoRqb-2vwX_zbNIfybgjOL7cKm3UySTRUcOpNxsyX7fkOktMGUq8rVzf3NKUYzR33EOB9iX68LYZXu1ZofP9awpO9QeVtMRuptGDHg_vBnYl8bsUxEvWcceFmQJ_uwUQgPIzpu3rv9J-RUhzYaPJOdZJCIrv5ypKz1iS9UAQZzgjBfu-1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
آنالیز جذاب و دیدنی دیدار هفته اخیر آرسنال و چلسی؛ میکل آرتتا به‌این شکل تونست ژابی رو ببره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/29365" target="_blank">📅 13:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29364">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea3eaf66e2.mp4?token=iYvquS9p4WDE5chQK3gwSh13bmNNXq9t8_jLRcZ7FYm7elAtPt1N2hbfX3GGnAPYyQCKRMj4mbhxc5rLnyyrJSO7zI_GcrOnvEmEIIW9grxF0RigiZeY0BxervN7AyaF-UC80RoxXCC9Zx-9K_Fxob3jl2wpymf9SRfX75D0Xwy5EHtOFnO9meq1XFqHhJFOxWlrrBKm74cV6p_Wx89mVnYa-X56YDHFzfR9211IzkjOk6GYHdD7jjIEFwVWATcAjWh3SpYpKIo3o0u_H_dJQxOmFXWjw4PRXpmWsQKZQDVppJj7JEyU2SjABI8resOvJfHmPHPl46y3etlDfyQcZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea3eaf66e2.mp4?token=iYvquS9p4WDE5chQK3gwSh13bmNNXq9t8_jLRcZ7FYm7elAtPt1N2hbfX3GGnAPYyQCKRMj4mbhxc5rLnyyrJSO7zI_GcrOnvEmEIIW9grxF0RigiZeY0BxervN7AyaF-UC80RoxXCC9Zx-9K_Fxob3jl2wpymf9SRfX75D0Xwy5EHtOFnO9meq1XFqHhJFOxWlrrBKm74cV6p_Wx89mVnYa-X56YDHFzfR9211IzkjOk6GYHdD7jjIEFwVWATcAjWh3SpYpKIo3o0u_H_dJQxOmFXWjw4PRXpmWsQKZQDVppJj7JEyU2SjABI8resOvJfHmPHPl46y3etlDfyQcZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔴
فاصله‌امتیازات دوتیم استقلال و پرسپولیس در تمام ادوار لیگ‌برتر به‌کمترین حالت خود در تاریخ 25 ساله برگزاری این مسابقات رسیده است؛ تا پایان هفته‌ششم لیگ بیست‌‌ششم استقلال تنهابایک امتیاز پیشه. نکته مهم این که در محاسبه امتیازات، کسر امتیازهای انضباطی اعمال نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/29364" target="_blank">📅 13:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29363">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eIPJKSv93f3kl9ngxy02FV0cRaVacZvOCEAw64Ct9b3Rbk1hrz66z3BmWveWgftqcchVVAJR43hDLoNTRMXjBNC7TyWh7gqLzMNiGn4-Fn8LY13SfAbQjyjVMaQJL59ygdABy_oas-3VKkYwGOkw4YWTBRs5bp0Yv4qPw1NyEzVCq87D4wBZWGomOGsvrvosmT6GkMrJfkg3_e3Fh5DeQGbI-J8YU4hZV26OOnQy1pj9clNzjp2Gd-DioebmzKiICq9fxnYBX8j6gHwWoFNZmA7fRCWfq6wm2U9Z-sNZow76zNKpAt4KQUOQS-wxdp5iMILVea3dtWrPN2xndAQn5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته اول لیگ قهرمانان اروپا
🇪🇸
بارسلونا
🆚
فاینورد
🇳🇱
⏰
ساعت ۲۰:۱۵
🔴
بیش از ۵۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/29363" target="_blank">📅 13:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29362">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1617cce66f.mp4?token=f4q4c4E1fRuYYFiX0ibs0cMi5JZa2zV9LQg4kY0xroZf1wnc_C8yro8ICNZHJVGguQ6iaTbJaoGpN56eV-1N_bWb6qiKnMS_L-seLO5EmuZb2f6Obo5xJInkJ_uqNZsPJyA6F4YVSMQ0e2CvmeowDimHIvMX8RjJ8lUU9pLL7U-DoVKMHMQ6L9Zo5jZy-MKQP_CWyX5aROF1kej2586XtPzGgS4FDkTcba484YAfCbGmP92IYtl2cqN9zl12DVxU4v-WqF8Ec83mUn3LDcEMsbe_MnxAdlZcN3LCh6wpVEoY9GtJ-YG6W4nQi9Xg1YnSVqUELml9lzugyb_qJMH8E45TW3jGUvLtZ1FNyHVjmYa6hGr3xiix_rX7wamE22JdwOajXe0mFViBW1w8wrE0RM9YNrG_jLvDgFUWbkAxjCWHwK2-Y6dh6M1k461Djn5o7PM2Igdy4eQwJol78rNY8CHlk7g_88-kJNTjSsvP9FZkI1KS92rFMpXti51Y3JPq54AAThhirpwlNElope64MsZCWXVw1vvXtazPGbceTc3a85cuUVNWxC7CyvsEr4GBvkMNO6eDhvD807pHjyDG363LXvSlkrkgeRUPq5x5Yem2pWDzOXFuYSblZNJLssEmmkZT2Fldf3seozCDnqRTJMlVt81l1pVrRsRLP7IVI54" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1617cce66f.mp4?token=f4q4c4E1fRuYYFiX0ibs0cMi5JZa2zV9LQg4kY0xroZf1wnc_C8yro8ICNZHJVGguQ6iaTbJaoGpN56eV-1N_bWb6qiKnMS_L-seLO5EmuZb2f6Obo5xJInkJ_uqNZsPJyA6F4YVSMQ0e2CvmeowDimHIvMX8RjJ8lUU9pLL7U-DoVKMHMQ6L9Zo5jZy-MKQP_CWyX5aROF1kej2586XtPzGgS4FDkTcba484YAfCbGmP92IYtl2cqN9zl12DVxU4v-WqF8Ec83mUn3LDcEMsbe_MnxAdlZcN3LCh6wpVEoY9GtJ-YG6W4nQi9Xg1YnSVqUELml9lzugyb_qJMH8E45TW3jGUvLtZ1FNyHVjmYa6hGr3xiix_rX7wamE22JdwOajXe0mFViBW1w8wrE0RM9YNrG_jLvDgFUWbkAxjCWHwK2-Y6dh6M1k461Djn5o7PM2Igdy4eQwJol78rNY8CHlk7g_88-kJNTjSsvP9FZkI1KS92rFMpXti51Y3JPq54AAThhirpwlNElope64MsZCWXVw1vvXtazPGbceTc3a85cuUVNWxC7CyvsEr4GBvkMNO6eDhvD807pHjyDG363LXvSlkrkgeRUPq5x5Yem2pWDzOXFuYSblZNJLssEmmkZT2Fldf3seozCDnqRTJMlVt81l1pVrRsRLP7IVI54" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
عملکرد 9 فوق ستاره‌ درفصل‌گذشته رقابت‌ها که در لیست 30 نفره کاندیدای توپ طلا قرار گرفته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/29362" target="_blank">📅 13:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29361">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/732028b756.mp4?token=C0Lo1T7GLjlpwF-NyiZQhM7tQrQmgGPTm62hUGARSz6rL3Kcva_yje_ykDq_AyqEv-gi2WVpDgHe2v0UlgMhDOCS_alVaMKcZR-FQhoLKfUs6Et0EGQB-02DNE-6DEFAFhaXnzBcFbP--EI4u8pdubg9dVOENLo_Lq0dndkYl0rk3KuwMYtfrTimywbzdv3qsKRM2UGpWUQVBtwt3cHjRI2RtSN_yMW5hRRTMg79Ha8UBZYFGqmdNeACzqzmv8wtwBmUKPGCFw9QOZ-O7-lVA48sIznnXxz77iI7-jhjzLfndHnD2OcrAFMIm2pqIMz36aDnaiwkKqoITVfPYLo4iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/732028b756.mp4?token=C0Lo1T7GLjlpwF-NyiZQhM7tQrQmgGPTm62hUGARSz6rL3Kcva_yje_ykDq_AyqEv-gi2WVpDgHe2v0UlgMhDOCS_alVaMKcZR-FQhoLKfUs6Et0EGQB-02DNE-6DEFAFhaXnzBcFbP--EI4u8pdubg9dVOENLo_Lq0dndkYl0rk3KuwMYtfrTimywbzdv3qsKRM2UGpWUQVBtwt3cHjRI2RtSN_yMW5hRRTMg79Ha8UBZYFGqmdNeACzqzmv8wtwBmUKPGCFw9QOZ-O7-lVA48sIznnXxz77iI7-jhjzLfndHnD2OcrAFMIm2pqIMz36aDnaiwkKqoITVfPYLo4iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
از پس‌فردا دیدارهای هفته هفتم لیگ‌برتر شروع میشه. تراکتور دراهواز به مصاف استقلال خوزستان خواهد رفت و آبی‌های پایتخت با پیکان بازی دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/29361" target="_blank">📅 12:45 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29360">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kvVbIw8kJvBWITnX7L6wG-AQZaYl03_rk5UfAvYLWZ9HB6S5bfvl4rDGZ0rnBYkKKNoNN3tagx5bfSLNRZVGWg_6N1A1m6nJMVPkqMiqtP0_NbgJZiE7_Ff7-68Hk2dCKnq5FBbMP28i-hB4nHawvO7U2oDa81z2crAhHN4pytkjZH5GNb7uvsujfnqRKxrBVsYSedURd89KPLtVbCJG9yGnw2WfZSh9KSc3fOkx2TEhA757fViOwg18X9CdUgi4GCge3iNoMDeq8WRB-qfwSAx1MQ6FTdfKoNov19nDKiA24_BLGss50748n6o7MwuYipg8ETTXOenQ_r-nBT5a4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
برسی عملکرد خیره کننده رافینیا دیاز ستاره برزیلی بارسا درفصل‌گذشته‌رقابت‌ها که یکی از بزرگ ترین غایبان لیست نهایی 30 نفره کاندید های جایزه توپ طلا در سال 2026 به شمار می‌آید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/29360" target="_blank">📅 12:26 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29359">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dcDRypBo1-t7GQL5gkDWbr8RwZKpQmmzgi9mJb53l90EBfTYfEo4_b4IaQmWNsWsRW4p1YxMQVqOrmjnO71lTFXH7tOSG1E68r6bc0cprJkutAsSwLf4HciAGnHivka0UoJYFNYuWshKvcuYbn9kGrsAOe9ehURp2LQLji_ereRtughtNiUDhCxopLpgAwehqzGzQDerZv_RldvdHgso0pl3ap_LFgMTYZUjD4Abn0emrQuTKcXQPZ6Y99ocDw1ioajOnmUqKTRBO2quZBEcOuvpq4d35VXR5tie-fQ_P9SuHw5Ob3jdlLTT7T6llXXNSoRWtzxKkIwUUiqG9nIEmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
با حضور لیونل مسی آرژانتینی؛ لیست 30 نفره نامزدهای توپ طلا مشخص شد، مراسم اهدای توپ طلای 2026 روز 4 آبان درلندن برگزار خواهد شد.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/29359" target="_blank">📅 12:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29358">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vWoTfodHNhnbjm_4q5ob42UOvXMQL6DobqmI9qTBcbhDC0dr_JXp5q790M5EcxDa5b9hXOJ6kRTChQ7u1Z7XL08LKQ6IfhFCQ9NAyZwkQeb4M_G8I3L07BwZHEkaLbyUkfMf3_Lq7QgnMUj0HshM2osBEuSPN-Qhu0REPUfMYyFBC7has_X-YKUYCVv05cIxDkWJDqoLKoXraoBgCjpM4JAFDujiRXiQB0qDPsiiWmlKUWiN1f6OVnisw3ODiLwt8mTrxGcdTLQ-cR0jASud6UMwgIZxDa9B9gcDB5L-x0DsJ1rC5z2_8VRrltsqJWXVN7yOep1Z8YAZ1HQNM1ZeSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دو سوپر گل دیدنی شهاب زاهدی در بازی امروز جوهر دارالتعظیم در حذفی؛ ضربه سرش رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/29358" target="_blank">📅 11:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29357">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L9lGTPngVfdEg2419ZdNyrwGH8ryZSViwFgaiNYYuaHjdANTgSNXtBJogNa83v5ngd-S3D5BTEZ4zL9haMuqNiKC4pXFvRf22KBhRNxuwvLdfCP3iuzOCs949ZY06ZGmbYk-wBqk_WULzLfVn1g8PnK7S27LXQ3acS0L-9k-lp62-ufA2Qe9796snFvsinsr0NicCR4Am6bXnOIeK6MDah2VvwnL5RGGMHA4ebfsjHH9fLmTeixu4Rq8o0uMGyvCwpebc3kgFV8Ez1Cvpt7d5jPg3lRHwpyP0BVc9mZdwmxPKud06VQcy28TiWXWNd6GW1B8ycNt2dLXdleeAc2Q8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
رکورد خاص‌امباپه باگلزنی به اینتر؛ کیلیان امباپه در اولین بازی چمپیونزلیگ در دقایق ابتدایی به اینتر گل زد تا با رسیدن به آمار رائول افسانه‌ای، پنجمین گلزن برتر تاریخ لیگ قهرمانان اروپا شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/29357" target="_blank">📅 11:22 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29356">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k86kzhfm03Dc1RKOgQhic1Syv27LJWs71tqldftT_SAiCsoIoVPLyQk4mBILxbSexZMIOogYv_Kd5LCoyWj90fBjCnyMPDYCUyQG-wc2Ow67A2Alq7gVBe8F3vKGZ4gbkpEg0yI009Y_AZGNq6ySQwDpAZayAPirCk3yhicm_kfgyrvfpJuAJgEzfdwpcqJ1Z5CxvfNPyyXwQxC8F8s4DP6OndNWCLWU7etPLpc3nRN1M_yKfse1PdnnxUZWgWXQNsBoj_YzmCvE76JBpzofdtaOSJ67_zyvqgeTekksZfeZdo00swPN8l0erxdjc-3GjBgxZ4wmwS2SDdiZvxtnvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇨🇴
با اعلام‌ رومانو؛
خامس‌ رودریگز فوق ستاره 34 ساله تیم ملی کلمبیا در آستانه عقد قرار دادی یک ساله به ارزش 650 هزار دلار با باشگاه آولینو در لیگ یک ایتالیا قرارگرفته است. شرایط‌جنگی کشور باعث شد که خامس از حضور در لیگ ایران پیشمون شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/29356" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29355">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qeLOW1XoNCIFBDAzhbAs8jNtU91VDqkbXBGpwod0v2dJbrHQP5iVDV0z-VQXSVyNba5t0bBBIWnxqJIxLd55n7VYZWR9oLWe6zkFkNhX7y3tpVPVJAbsW_P6VG8pFPZTkFlkcJ7oGrWQQ395GQ1GtNwe77UF-hHqx7MkC1FnqwdYeHc0WcpdSe0oPdvWoM9EBHVZT044dXyOB7jEfqm5yJyqXjkV0UGZ-cMdyurzMd_26BMbzQiCtb6tlc4MyKVlZvRvNFbZrkP6k0I69R-K5RROyrIl3gbk7V88ROPwso1PDRnTJlZK2TREW8HIy3Vzcpg3_rMZMAinpsAJbPI_Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پوریا شهرآبادی مهاجم ۲۰ ساله پرسپولیس با دو گلی که این فصل به ثمر رساند به دومین گلزن جوان تاریخ این باشگاه با حداقل دو گل تبدیل شد. مهرداد اولادی با ۱۹ سال و ۶ ماه و یک روز، تنها بازیکنیه که پیش از ۲۰ سالگی به ۲ گل برای پرسپولیس رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/29355" target="_blank">📅 10:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29354">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b6f5a93d8.mp4?token=RWCwm8Oupe_SR3tFPBy4g_OOKXRJUGSE9gs0VXfmQiU4uNPKK9VOF5x04UMwippMqvs-JARlcJthmC9KhNuCw-HZPYcgp6RzrkMN2uh4pXC4OsbJWrse-JACT5rrMkc5iBEvSAx5W-oucye1nI0T4I8uApIb_klOulWf0Wn6HMlRa9xlgCLpOPRcIKwG6mdqakTARGmjdzdj1tVQt6iqtceg1nh84GTZZBWIBFEnkeIiktDGpshdHjz6e0Xms-IVorHxPnmCQHTeAy-LqUdpPLdQIA4GJrnDqVoi907FRPM6rgML4JcLJUAzucviDj76FGKHufAFpT5rZzqpujzhIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b6f5a93d8.mp4?token=RWCwm8Oupe_SR3tFPBy4g_OOKXRJUGSE9gs0VXfmQiU4uNPKK9VOF5x04UMwippMqvs-JARlcJthmC9KhNuCw-HZPYcgp6RzrkMN2uh4pXC4OsbJWrse-JACT5rrMkc5iBEvSAx5W-oucye1nI0T4I8uApIb_klOulWf0Wn6HMlRa9xlgCLpOPRcIKwG6mdqakTARGmjdzdj1tVQt6iqtceg1nh84GTZZBWIBFEnkeIiktDGpshdHjz6e0Xms-IVorHxPnmCQHTeAy-LqUdpPLdQIA4GJrnDqVoi907FRPM6rgML4JcLJUAzucviDj76FGKHufAFpT5rZzqpujzhIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمایت تمام قد خوزه مورینیو از فده والورده؛
جایزه‌بهترین‌بازیکن زمین باید به‌کورتوا میرسید فک کنم اهداکننده‌جایزه گل والورده رو دید و بقیه بازی رو خوابید با این حال فده هم خوب بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/29354" target="_blank">📅 10:31 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29353">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YHfYm6ntHuYuxjJF4pJf8zY4hKdbZ6mEu0BLjE1YPpVSMfyjvKO-xBS-rxvtes2IJ8VfrsVv9MkLXAB9vHg25ChsNWo7leTcRl2CkE2T8viXcq0ootCdkS6ADzO0EFFLjKRic0aVOTKkAAeRu7uS5I_cbsTwdm3f4wU-K104-gcPAqDBWnex9rAmlnoUW2Cb-_Z0r0zEG-gd6tZAtOU7xhs5jBGZ-G4PLzxSaYAkWHBY5gKgrLXP4YfujVy2qX0mYT31ch8A5rvzewcoXR17Lf4Bvmy113YmGQCN1Lb2_PlCN9k4SJ6dna8E37gQ5qzccNk4PqBH0Yyfryxaiw5YGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛بعداز درخشش ادامه‌دار نادر محمدی در لیگ‌یک‌روسیه و لینک‌کردن او به آرسنال توسط رسانه 433؛ این‌بار نشریه سان گفته میکل آرتتا اگه قهرمانی UCL رو میخواد باید نادر محمدی رو در ژانویه جذب کنه! قطعا درهر بازی 3 4 پاس گل ثبت خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/29353" target="_blank">📅 09:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29352">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnum_vnrBMhRk27j3h9Hkf3QekzbSqu6zVMc1IE2LABSj1k_OtP7-0kULwrbf3nv59rmm2XOlQeEWdZt1k3H0WO7AQsvxoUePO1pP8W9w77SrpwJ6reANZo-Gn4mXRibTV5xTxBvVW7zkfyazOGhbS2naa9qrFNQUQkyXwobHS-iMnGtSntG_u2yhvFLBG4RpD0evjFalxFKqSt2P60IHBpNbZe-Zew0xPVeqLZywnZdT3v-7QCGbJTczpJvWQmq3frXxBh0jtCMS_slJptyRTKdRRhv03C217EB1ZiQQl0tPmey4ccefaFr4a0E9xn7HO51_CfTTPXblshJauT4sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
فرصت‌های‌برگ‌ریزونی‌که‌بازیکنان رئال مادرید در بازی امشب و بازی مقابل بتیس از دست دادند تا اولین شکست کهکشانی‌ها در لالیگا رقم بخوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/29352" target="_blank">📅 09:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29351">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qL9nhpDGb0YIouHLnN4AUelTQDGA0v8uQmOrjRJtwiFHL9Cg0BiuewON9RH6-ALhMwxVaHO_N7PAOwFaPPaTireO_oo7e1pDxW6hPvfPTwGo5mwqgGA6b1ktLQuBL0uKDOe-AIl286mWzxpAJ6lneXhaY4L9ta3Y8OWt0W6eSKa9sPRGLCLdx3WHW7HMUriwukTxXBqKPmQ0PCUomc0D8KCOQuKw0jxQxOGp3hlgNaAf_G_Wf7lQCTewIGVkous99_TWxefAUukNzmZnHxJFjUi_HKWaqlT8Ri9bThWcc6FJZfW7R8WkfNNJ7YYchK7wxm6vSX-Lu2yYa_XG64mNeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تاکتیک‌ این‌روزهای کادر فنی اسپارتاک کوستروما درلیگ‌یک روسیه: نادر اوت پرتاب میکنه یکیتون بزنه توگل؛ نادر محمدی چهارمین پاس‌گل خود را با پرتاب اوت به ثبت رساند. چقدرم خوب میزنن تو گل!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/29351" target="_blank">📅 02:03 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29349">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cHNzGNcittgksNOG2v4S8UawcMquwhHzD-IYgRKitoh53UIUOQlEO490YpS1MUQ4QMQRqZ40DnkhRQ0DR54zlX-1LswBNqkqKkTkBR4zdEZm8kBpkS92VYlRTJoBk_96dlQqPJmylG-sCU5zpevxv8MmDGtyDTquKBfCMEG7lNiYjoprrVf93qBmOfywtTwdtaIlnqGwrl27u84fRwdffXLQnLamj5u194MlrARLhWNkgrkAjXTy28jV3ihb_XteLAhN2vWnG4HV8wcQDVKFO1Mu-M5fnqJZPVouPh_MKeO57g1p3QNpcjXfTc2VkeW4Gc-lkTfMWIy0H5gDu8FJsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌ دیدارها‌ی‌‌‌‌ امروز
؛ ازجدال شاگردان فلیک با فاینورد تا تقابل لیورپول و اتلتیکو در چمپیونزلیگ!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/29349" target="_blank">📅 01:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29348">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kO4bFwf8XbVPPyPubkcnYBScewmgULezo4VHcpkabdq4dspQdX6Lm5eXeUvaShj5JOBjbpUKOFau4N8m0rDz2UHHQKZ4daSuJOgqWLr8H_ZzXncFWLXI5TOeDQS4uhCDl3h7r9LJxaxC1VYHnBznMrk62EXnnm08Zq3wpnD6Uf3vbbRsd92vhQ7PxPedlNt9v4PerO8fUHeXu2dy23PLLCq8KDBhIPsuJuAhaJOBVK-jMauvBl3DZwQly_EM_yRN49Gbm7NUye0XC7FPAaiYH7sjtHqus9aBM51jDEMinXY6xYtsCdxVaVh_kqjYriyvSrZFswXnsvBrFrJo3wiEUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
شروع سه امتیازی رئالی‌ها در UCL و برد آبی‌های منچستر در شب دبل هالند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/29348" target="_blank">📅 01:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29347">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqgQ91h8I_JgFDe7TqbxEKkDpH1gJb78DCjlxYiVyaxm19QUKn_FC9_u2yl1lhAt0Pd4Pv9faPcDq4BQC5wQfCp4cWzYaCPDv3KlC71lfB8Nt52byjiEiWXFxnERzjed9s64Uc6_EpAZSmyJHP2uq-8aJVpt7lYZrKS1mqKcNyA2IZm29yVOwUU7LufuzrdUoAkjXmNXwDxpfEbCbwM5mEtkiIGEEJ0B2mqZAdWfSKAXCeDD3_ycsp9HlJ2OVleLViCB4rtbcy8d0D3UdRHqAjt_fLKma8jCyEKGSBuNUDKU2uXdlnaFJSlNS3GRlR6BCPbDb0t-rr0XGe4KZ6Rn7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
در هفته اول لیگ قهرمانان اروپا؛ رئال مادرید با درخشش کیلیان امباپه دو بر یک از سد اینترمیلان گذشت. جالبه بدونید مجری شبکه اینتر که در تصویر میبینید گفته بود امشب‌چهاربرصفر رئال رو میبریم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/29347" target="_blank">📅 01:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29345">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bGzeL5f-TJEEMJzKtltmaD9SkyVkUt9FDDy0D5wkWu7L3rsWtOsYJohKW0arSgRRprxBBB7LIZPycpkxbThwQ_NOzCtqhjf3BWkQxHmjxTu_Kxg5ezsUchv02bvq9cQ_B9mt44HUh5npK9U7EUankeMFBJyXNeBf5Jb5HshR8xtLS29clarOsyQM4Jhy93ATMSh-FXPrFE38jH6OneHrGhSusjn0_oJoGZ404qDYgi4OkjIJ5MwlA6mEzeHksAuoU4o9aken8rlVKf__tY8wrkFw7LnQlmrWI_ec2B-y-f-Gt74dND5ru3CRY_Ir36Tb3_vF3leS55-zQT3iR6qx3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dTsW2UtFtUgSTtL2a77Zh_qu94A7a4PnFNciBFKlk9b7FZj4_h9TaRLLlRKQk3tg3jpH9TxusGOrdqZG9zR9zvpFVfwNdCvPA_RpssHHocg7RQuGqWlSsZiIc0FriTl4GuCzsAhXVn24Aa5gysRazEgJ7YZUdiKZ8xbEFaJ0PYQSxN6VN9XOyVsbhDC2jMS-Q5fzXQW4iVNaey-6jdX311B0qMvWIdgOZ2bsQXSNsVn7PQbYKccN7EkW1vCwghSG7WgT3ATBxSwcwHuRogeJi4rV3kTIDmPLk6o7I900nNBtLsoWe20rSpHAUG6qvvPOR6K6d2wkCIy0pPQn7wfrOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جک‌‌گریلیش‌ ستاره‌ سابق منچسترسیتی و فعلی اورتون در کنار پارتنرش؛ اون اوایلی که تازه اومده بود سیتی بیس چاری مست میکرد فوتبالش رو به چوخ داد الان باز بهتر شده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/29345" target="_blank">📅 01:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29344">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RnJVx3sof3o9IbAY3YISfcPlVM-MllT1nnPKTZ3fTJIdZMG3M-P-ti-rIf81E420pyjoEmQC4PFrSWB7zvQJfx1z4paO4bwrRezRKDA99S4llmMIEWOFRuBi__cYeypqwZSsURWlv3p5kQSPSwSIHI01LqpV-oe8dCJ-Nnywa-1Hajb7PDkE4mAGcGfcdl_ympIqORRk9v-9BMsBgsBnaU9dazjcSEEAOBdtaUg5LgM4GWU5SmMskAiT8Obkr03ZvQku0mrwJWSqj0MJ6F5dmL2UKmhEmoV0D_FSjVT1XgnxLZoAYx9mGyP-qLurA_YcnzsKpZPN9uu_yIMPY5Ybeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
در هفته اول لیگ قهرمانان اروپا؛ رئال مادرید با درخشش کیلیان امباپه دو بر یک از سد اینترمیلان گذشت. جالبه بدونید مجری شبکه اینتر که در تصویر میبینید گفته بود امشب‌چهاربرصفر رئال رو میبریم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/29344" target="_blank">📅 00:37 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29343">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_cWTmOTJ6ahs_SW1ZfIHUvCo7UjRpIvpi9llqB0KmbPtJsXzfzM7eUgqkNgUibsX6gzIFgCaAi86KXxzxi4lNzqLM_jMDVALac0aNtANVWjn0fsVZ78Mk93nbzPLw6ieHWU45DE7BT7yv3mbGR5Uar3a5_e_YRmcnbOyPaaguamLJiuDIHKO3iSfZtpQ370PgYY5MUjfLjuzio5k89fLCDAcDH8AbJAxInOAbrle8drE6CZneM24nTpMvx5jvuBBnEMieQdQYbZ55juj8aNLLIdmrxDBsEWrNX4XG3bMzH2ss816XjpXcYw8sHoeNan5eISxJjMDZMBLe1dN-iwfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
رکورد خاص‌امباپه باگلزنی به اینتر؛ کیلیان امباپه در اولین بازی چمپیونزلیگ در دقایق ابتدایی به اینتر گل زد تا با رسیدن به آمار رائول افسانه‌ای، پنجمین گلزن برتر تاریخ لیگ قهرمانان اروپا شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/29343" target="_blank">📅 00:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29342">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-mKqzEd8CzwN2o02t2dJg5EWMTeQb9PMhOcTdyqr832Ak-i_-AZzZzDZa3YLt_hruyIE-du6G_1F3CZ53eqcPoTkwdOUa-Hr7CDE07D_ij2EMTdfVSWhpg-bidwuig-BOb3IYuDdx_xBsufiTYvPFuWZ7Pxv0Rbc7dPdpwmOGYuaLuupYVyaCWxLufwvtE4bT2NcAvnPq9NuAsfS6ZXos5n8ecv51vf6J1JioWlDE2rZ2CKWIuLaoMeIJBiJ5HZBIyM1LVmhlqnAOkxBVVV8gf7O8WqFiPpfRewMnX9fF-a88g3Xdz86u1OitOpObxBk22WeZqNg0SJ81Ki5vHe-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌چمپیونزلیگ؛شماتیک‌ترکیب رئال‌مادرید برای دیدار امشب مقابل اینترمیلان؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/29342" target="_blank">📅 00:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29341">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51b900e940.mp4?token=Vnf20d_doamjt6252wwrAZrloTqnbo0SEK2ibCnpd22Z0vJporfgS-nKsxDqktI8ZTEtCyzCr-OnrfxVJG2Gw4uTo8AmmzFiEUNwQ7wSmk1bxcZeHVjJNWN6n07KR58ZpinBRdFn6_i2oKmZ3OaLUG2SzXRp5muBNx7l2S-OOfA8H_FbNVf30PdJBUDf-qavhMhNsS7t33y65ncNoJWVZ7AI0CTa_hOKmD9Ub9O4slXkASDtfQ4XtUMbSgv5VxtdtETIB8eCYG0E5GDjaQdezRwPvsrHY5nGl5XJHOioU5Sq0MZnv2hsk_xD0aWSkWxThFjAaQV_IxEbxQmd8yVHpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51b900e940.mp4?token=Vnf20d_doamjt6252wwrAZrloTqnbo0SEK2ibCnpd22Z0vJporfgS-nKsxDqktI8ZTEtCyzCr-OnrfxVJG2Gw4uTo8AmmzFiEUNwQ7wSmk1bxcZeHVjJNWN6n07KR58ZpinBRdFn6_i2oKmZ3OaLUG2SzXRp5muBNx7l2S-OOfA8H_FbNVf30PdJBUDf-qavhMhNsS7t33y65ncNoJWVZ7AI0CTa_hOKmD9Ub9O4slXkASDtfQ4XtUMbSgv5VxtdtETIB8eCYG0E5GDjaQdezRwPvsrHY5nGl5XJHOioU5Sq0MZnv2hsk_xD0aWSkWxThFjAaQV_IxEbxQmd8yVHpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دو سوپر گل دیدنی شهاب زاهدی در بازی امروز جوهر دارالتعظیم در حذفی؛ ضربه سرش رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/29341" target="_blank">📅 23:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29340">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7ok0-gF_7oYuaHvlKEa1YO4B8wFkLPFo6tO6bOMsOozjqgGjnjRog0r7hj753KIo1QFIukBxiq7i2Sy9T8iKtbZ5EqPlkS_2zENO6zRc-4eFip_cZmFxiSGBFVwMbfEiACZ-iBrslDrx2JOxxO6S56Fdk8xdH6mTgXaIm9tlfs3rx2EnQhraB8DmyKka8shNJUXB8GWzxgrUU4R3PnpNv7s3Nxw5_vR2VCzYXPaRJUtFd7qFlvzeh2gtpuR4B23XW8xJ7R694VNNlnpOZCwW2LI5izd-SPltk-70Rn9hjm4sNqH-Uzon1MiipYrJJN9hfuGg-bDlCMzYQT7e2y1qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وضعیت برگ ریزون بازیکنان السد و الجزیره در آستانه دیدار با استقلال و گل‌گهر؛ السد امشب چهار بر یک الغرافه رو شکست داد و الجزیره نیز سه بر یک تیم پر مهرهه و پرستاره شباب الاهلی رو برد. تمومی بازیکناشون آمادند. العین امارات هم حریف هفته اول تیم تراکتور در…</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/29340" target="_blank">📅 23:36 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29338">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🔵
#فوری #تکمیلی #اختصاصی‌پرشیانا؛ مهدی تاج رئیس فدراسیون‌ فوتبال عصر امروز به مدیرعامل هلدینگ‌خلیج‌فارس قول‌ داده که روزچهارشنبه باشگاه استقلال روقهرمان فصل گذشته لیگ‌برتر معرفی کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/29338" target="_blank">📅 23:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29337">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
👤
#تکمیلی؛صحبتهای‌پزشک.پرسپولیس درباره مصدومیت عجیب مهدی زارع درپایان تمرین امروز!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/29337" target="_blank">📅 22:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29335">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f6SnYzDStCSSamflbaDQ4OVCU6JYeAYchhCcv5JuRTAmCU20uCKw4gIiqFwhxlBiOYnvmAQCZLDmnriLGH2icmMDvrTJVVJB4DUmt-SarF6KRAhS_WhUjFOfChVxe2v_CIRjBRHhqDCBFTUpA3jXLlcHiqLkqeWE4FX96dEnU1g2IJkesABwQ9BzcJmDJ1GSMd0dn3xWNw40bQ6Tjb6XLLdyCfS5JwUrETgJZpvoCFhQVaa33e8NZgreRdzI-b57pZOj4K6ja0Zefw_-m-i7gMFwb_boIUtVqTcfpj4-diEemKRrlLXOpUENy6KopCFyDbMWBpWAnlhwhX_SLP87LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DuyXtbu1q6sYGmTJ2CH3UYj1SXKCE3j8ibCHTSlMJHZTZfDL4ctowDZ7cEjThhqN8SOW7V_Tsr7G_8w94mAEcfKjpwPvbJwmgTc657UyOC9JDHfVYOjoBcHIAfXtiPg7iYeV4cgSOX0UnNagxqFlJJlIjCbaLO3YdcGu4U_gCcJsHmj3Dd09LlDUBd5ggZ7mfAB2DcPPUWfSAnPTgO5DG5zDTYbxi5PvaHaYZzZKoGWLKkb_86XD-FarqfMBDWwC1AEXnBcOMm-DYayuIjrXQZykg0YdM_QyO-Vg9LcOapMY7XRiFDKsSSDwj5g4jwbLpVgQexkwHQ3hrXj1Ubp_2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
زهرا گونیش ستاره تیم ملی والیبال ترکیه که بخاطر علاقه‌اش‌به‌کشورش پیشنهاد لژیونر شدن و حضور در رقابت‌های‌لیگ‌برترایتالیا رو رد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/29335" target="_blank">📅 22:40 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29334">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e83f3f081.mp4?token=khzMcMOUxrHfr0_Bp1oIO5fJW_l_JWvG9GX89naEqwFrODPnE4glbskBkPATgQ27C5oay0SOq43PVSbN3iva-MFBYve7cgdDSXDFygpYfYRgN8tJcZjeKYkYxFm52HtNz2ZYv3NC5j1S2cw4veA1jbInhK6DJDNADa-ZpkReWyyeUhWVIoKVDqc6GNo03JyqNvxvVX8coJ7n5WcJmwPgCVi9ZRxxOH-ov-eAtQYbkvDh6pLJz-7a-rAbXW5Yr75dt4_5NzG0-pMfzgJ27QCFrShmPa9qRuLKDm8qxUT4--KT_yGo2BoxSoZAtKZGg2L-6Jm0A0Qs5IFYZd82A05O5Q-ooUihtDyOh6d5TSZb0dLQexKsNxrov4596oB9F_GuuVk-cLFjdrrKukgNe76NJ8JG2a6d-hytXTPgo7RHqhMgyyeGmAZQj8j6lg-btL2G6Xu12BqWwsuyqgevEhZjspzFrVz8RwvNGfA7bQv2eaU4O76UzPtOU_7PRYUzpKWSitxnzLFhsfkZJuAu7sbxn4HOjFvjj0xedmqkjNe4q8fmCSB4XbH5JfLrqBNJ_Rj_Ta6JpQCID6qMo_XeBDfBjvowIm-v88fnvyvjLO0yCBRXJT23EUEnst1e8tHgDgkpHq-N_gxtnITGL6jAYDid5mlZDa9gZvbDtdTd36cO-p4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e83f3f081.mp4?token=khzMcMOUxrHfr0_Bp1oIO5fJW_l_JWvG9GX89naEqwFrODPnE4glbskBkPATgQ27C5oay0SOq43PVSbN3iva-MFBYve7cgdDSXDFygpYfYRgN8tJcZjeKYkYxFm52HtNz2ZYv3NC5j1S2cw4veA1jbInhK6DJDNADa-ZpkReWyyeUhWVIoKVDqc6GNo03JyqNvxvVX8coJ7n5WcJmwPgCVi9ZRxxOH-ov-eAtQYbkvDh6pLJz-7a-rAbXW5Yr75dt4_5NzG0-pMfzgJ27QCFrShmPa9qRuLKDm8qxUT4--KT_yGo2BoxSoZAtKZGg2L-6Jm0A0Qs5IFYZd82A05O5Q-ooUihtDyOh6d5TSZb0dLQexKsNxrov4596oB9F_GuuVk-cLFjdrrKukgNe76NJ8JG2a6d-hytXTPgo7RHqhMgyyeGmAZQj8j6lg-btL2G6Xu12BqWwsuyqgevEhZjspzFrVz8RwvNGfA7bQv2eaU4O76UzPtOU_7PRYUzpKWSitxnzLFhsfkZJuAu7sbxn4HOjFvjj0xedmqkjNe4q8fmCSB4XbH5JfLrqBNJ_Rj_Ta6JpQCID6qMo_XeBDfBjvowIm-v88fnvyvjLO0yCBRXJT23EUEnst1e8tHgDgkpHq-N_gxtnITGL6jAYDid5mlZDa9gZvbDtdTd36cO-p4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔴
#تکمیلی؛ مهدی زارع به دلیل مصدومیتی که امروز براش رخ داد2الی4هفته دور از میادین خواهد بود و دیدار با خیبر خرم آباد رو رسما از دست داد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/29334" target="_blank">📅 22:25 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29333">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gecKd8yzVIBtv1_wvDJVgmiWFAOcW3MDDqmWRBLYXu9-Q7cBGwwy3BPRcnielfVPBAIQMI5SJYsZP0rGAY1qupOwLTwi6OwHbquXq6yv7TugsROxiMqZh53g9HrOz-UoVEJv09DaDHBxoDS_8o--Wmp-4cRdiXG12JyX6VgiTHChZsx42nCrU2tsppNh0fClO5HIWHpTufQr8TQ9qiMtR3ynRLvJZ9ukCc7cGcQ-IU_db0ARC1hSRCEQEPv2VwEW8v28l1JpKwfi4IGKTvvFubc-K6ieBcc_IZI211EWJjDKlJVN1FvV57Yz3nbT9IyIbVJZ3LVRsr2ifC6BRyALyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ایننرمیلان هم امشب بااین ترکیب تهاجمی 352 به مصاف‌رئال‌مادریدمیره. مورینیو هم برای چندمین هفته پیاپی یان‌دیومانده خرید 140 میلیون یورویی کهکشانی هارو نیمکت نشین کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/29333" target="_blank">📅 22:18 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29332">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMlgGfIrcKiX6kE202HUWOjXACgvkgWaJyEnsVxGbw8AvqrlPMK4_zNSr5By8RGaiSJVoB0LjyBxRsXkcbbZzy7f09IO2pAkfX2JugLZHAqmbeBHihl0kaB_mTMAI-XLWvetVAqqks_6IoDG0rlQts2fzufOq7lvNf7IhfFadIu4_eg1HsJyREig7pue4WRCWH9ZV6CMvC8B5lSGQNMzxvOedzAKIHTtZuvupYkvLXGh1GNxBnD-mD945BWG4DtRcFkSW33RyNZOL5nxOSaIZ7NIWjoomXgy4arHDCGmsEiPozNkQU7Kl5wXGyuqugK7pNpoFXzBlymKalajobs2DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
با حضور لیونل مسی آرژانتینی؛ لیست 30 نفره نامزدهای توپ طلا مشخص شد، مراسم اهدای توپ طلای 2026 روز 4 آبان درلندن برگزار خواهد شد.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/29332" target="_blank">📅 22:12 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29331">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dkd2qhNWPmKEjKUp_kzg_geGakPm7w49gz9-3Ytt3-410q27Yr5tndeufM6PGl6uxh705MwKxmLUqlPSv6h999skz1wku1FCmXeLc3noB8I3hOVrXgKLiACH5-QNdX331zuWfTNM0Id1JSIFgTPAGL0VlEC2YtWKAQoUgKZWSMiQuvUOXKUvqtIzMc7Xi2NXXFWi63VdDdEFdhDsU8rEJAyjOXC6xbMEEf6oWYir9sBqgK-qkFt9ot1AHsEq4kkSWktaty_ZLitfDcsi9F7sblUY0nueEC4N0naVm0tO1Iyfmz2xF-4dMiMv8nwnHR4JESSPZXpMawcbR0T95pO2Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
👤
عملکرد تیم دهوک عراق تحت هدایت یحیی گلمحمدی درفصل‌جدید لیگ برتر عراق: 6 مسابقه، 5 تساوی، 1 پیروزی، قرار گرفتن در رتبه هشتم جدول!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/29331" target="_blank">📅 21:57 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29330">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3QOi_Riq1Ur44u9JtRM23019XX6o3jdobOjGYiyvKyQyfUCxKXThM1t5SthJ9ROJshY_c8hFB00wAzAlSkDnBJjWg1_WnJDcpMeqbfQCH8MppifHFxFEs6qtzUQeuCPpRRSNTc2RA_LgrU5Eaqtvoe948ojeLWx117saFuafRWEgxT2up1KDExA3Ky7NHg8qUd85GPqdfq2uW26NC8SCc1FlO_pEvvkz-_zVeEvMrIR-il_Gk67SZTElZvOgZuPEOLECHzZvZSuGdmsxElV-6wYzgsHKhdVFNsT1DHmfyv_BTf6_5dKiYo103_aPOkRihcwOdpeuSeApaLKwuo98g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌چمپیونزلیگ؛شماتیک‌ترکیب رئال‌مادرید برای دیدار امشب مقابل اینترمیلان؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/29330" target="_blank">📅 21:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29329">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gzMrulgH42qUvrm7x8rkjrE34DTgQB5gzw6TIvZpgSDZ6NAEW2iA0CX8HvZwK_odeIT-Y6gsJB-TmHh1PpopKgdC3o4-pND5PvR9Yneop7bkF4M3EgvfuXYmw2q80tnD-tnD3rQDygcYbuFQaj9WlqRZm7HVNU2J_dSNj0u0O0M6ubmCKBJSRQhE__ibf0jyge8o7kLzG-aEaWUyqjetpzHJNtU8E42CEe7c2GhzeCmvaGqvlyBhQa3nwtH711MqyYxmg7B_Zg526djj8tXc3QCgT9-4e_lAkYyczTqMjY2JgtIeeUD-uC2xLK-6zxCewzmdRgM3NKRm1ANkONs4iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌چمپیونزلیگ
؛شماتیک‌ترکیب رئال‌مادرید برای دیدار امشب مقابل اینترمیلان؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/29329" target="_blank">📅 21:18 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29328">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/939eacf7b5.mp4?token=g1SpBUNvYCigy3LxgAyLUzK7P1TaXfYmCCN5TZ1YxIBmLlKbfTvn5YhJEqctMJMimZdTrjOACk26gACGrFH1Xd7G2QFbZreYqQlppwuQWkaZYs6TV8-f-wZkwDh4Cqhf7G93w62ef2eTB5YwdPi3Kpb357A3E1lci3drjRvbDrhlNbQl6e-BkRzNUmyz_iZkQgEkU2TI4KL2AtJskwaCaUAmdKpjvYGe-pf9Aolcv9JPvynMu_AJ7hHaiHWPNgD8MIfXyV9EVck8NmHJjlZ8ADMFBC3AGLCGbQvMkbgdm1GshvITMA_4Zgh88bF2Z9EdG3ld7FF4eue_OqBCPuqGsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/939eacf7b5.mp4?token=g1SpBUNvYCigy3LxgAyLUzK7P1TaXfYmCCN5TZ1YxIBmLlKbfTvn5YhJEqctMJMimZdTrjOACk26gACGrFH1Xd7G2QFbZreYqQlppwuQWkaZYs6TV8-f-wZkwDh4Cqhf7G93w62ef2eTB5YwdPi3Kpb357A3E1lci3drjRvbDrhlNbQl6e-BkRzNUmyz_iZkQgEkU2TI4KL2AtJskwaCaUAmdKpjvYGe-pf9Aolcv9JPvynMu_AJ7hHaiHWPNgD8MIfXyV9EVck8NmHJjlZ8ADMFBC3AGLCGbQvMkbgdm1GshvITMA_4Zgh88bF2Z9EdG3ld7FF4eue_OqBCPuqGsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
به بهانه شروع فصل جدید چمپیونزلیگ؛ نگاهی بیندازیم به تموم قهرمانان این رقابت‌ها از گذشته تا کنون؛ رئال مادرید با اختلاف زیاد درصد جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/29328" target="_blank">📅 21:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29327">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d64e7feb91.mp4?token=CQNwFk2oOiaA4N2k7hi95rFGvWeUm87G9mVwLO5xrLA61Uk0n6snrY3sqM8-8AakDD8Cdj4XWJouf7IttlgxchyiQyUBSSgVn8X-NhnXloD8PQK4F0HSzUXS2kUMig8pnoyHv0y2SSYJoF7BNxll35a9fyzIY8SCYakPOQ-DUwOekmeSJJChxoaiK5mJ3n3zcF-9YxvYIDrqg8F5Xm1NJ4f8OZbWRPgisALDVtgXYbj7zwQtOCXCHNEvoMjAlfsJkG87Mpfe-IdGC6i_bQNSGsWGC0LXIZyH1H-O4IZ1-zgNxnZ0VwUCcBjprfD7ZUKQ_nxU0EHDFXr3sYFfDMf_WHRLCn56is5D-yw6oI0WIdrkFpmSEATRfP8joa4mRDNgWdW5hspAe9zs-3asDfCarbXHKy02Z4VX4DMxA9fy0rrf-0_bhcjkV0mVON33ryf-gB6wx1T9sChQhhhDN5doT4fOMG46k_hGBrt5kufxyvWhJ5xfdsw0ihap3jmP8P4PQ1pbrwXhOobyyc9PGUobeBqkbaUmbKZxQ4rK-eQhvUMsA8Jv-LC8Vos0XSD4uCQiQ6XBouoF-d3dfUS8GwgnmD7fbe3uoSbZM5hVkAzAzpQn9eH_ZlDGw50uSEkHm0MoNy0aHGI7cuewVz72zxV-Ph3fnnH7hdX5MrWuGblWU2c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d64e7feb91.mp4?token=CQNwFk2oOiaA4N2k7hi95rFGvWeUm87G9mVwLO5xrLA61Uk0n6snrY3sqM8-8AakDD8Cdj4XWJouf7IttlgxchyiQyUBSSgVn8X-NhnXloD8PQK4F0HSzUXS2kUMig8pnoyHv0y2SSYJoF7BNxll35a9fyzIY8SCYakPOQ-DUwOekmeSJJChxoaiK5mJ3n3zcF-9YxvYIDrqg8F5Xm1NJ4f8OZbWRPgisALDVtgXYbj7zwQtOCXCHNEvoMjAlfsJkG87Mpfe-IdGC6i_bQNSGsWGC0LXIZyH1H-O4IZ1-zgNxnZ0VwUCcBjprfD7ZUKQ_nxU0EHDFXr3sYFfDMf_WHRLCn56is5D-yw6oI0WIdrkFpmSEATRfP8joa4mRDNgWdW5hspAe9zs-3asDfCarbXHKy02Z4VX4DMxA9fy0rrf-0_bhcjkV0mVON33ryf-gB6wx1T9sChQhhhDN5doT4fOMG46k_hGBrt5kufxyvWhJ5xfdsw0ihap3jmP8P4PQ1pbrwXhOobyyc9PGUobeBqkbaUmbKZxQ4rK-eQhvUMsA8Jv-LC8Vos0XSD4uCQiQ6XBouoF-d3dfUS8GwgnmD7fbe3uoSbZM5hVkAzAzpQn9eH_ZlDGw50uSEkHm0MoNy0aHGI7cuewVz72zxV-Ph3fnnH7hdX5MrWuGblWU2c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇧🇷
ویدیویی فوق العاده از دوران درخشان نیمار جونیور فوق‌ستاره سابق تیم ملی برزیل در بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/29327" target="_blank">📅 20:52 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29326">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aybhEawlWjMEnckb2UiwI8Ffrcz2zuw0mq4JWzc7rCAhy-N5hYc6xqiLBLAHzisWbVZYebhaanpaDYXo-vW5eKTWoj6rL8eWiGtpVdmXtppxhWlJvV0Hb7iAN_wRKQkFDfyw0MkgfebisoprUx8oj2XwxUlLnoOYy4Fokf-3haFaKZwHDXPQ9BaKoBXdSG6i02WkOwM4UlYjJ2UbF2Dt-BtGNkje3cLTFhmwYA8yoEWtuMKThtQD2wo2o4pqXspgPSMl7-WlcEMQ77HA6xtyCdxN8dQTCV3KCSUTCQieE_G3sE-8dZCdUmEK3TgmQtP8M2zeMviHxMabC0ZhUaLs0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
سامان تورانیان مدافع راست استقلال که در اواخر بازی با آلومینیوم مصدوم و تعویض شد امروز درتمرینات گروهی آبی‌ها شرکت کرد و مشکلی برای دیدار پس فردا مقابل پیکان نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/29326" target="_blank">📅 20:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29325">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K912X05JB_0Fe1b79SpQVkXL6UVKo67DwAlnRieFmxeyjv5X6Hz1KQTRZ3YHQnsBLHixkUYk7Pp4MyW8RhcQMr9WfN22AhdM3bYtMHRIke1iS9ccQEjdyI4BtrDOxUeGV3DBE0Sz7m4guKI8h_onzQLCul-2bmxI-Nnoa0FNCMY6Lv0ZiIxtuz4H7PG9sPQQdamNPb6GtCoPszw6_lSqkGBzD7C_HE_izSsuveha8wTPxMbE-ZEu0ArMjBmBsQyTQYsKvXJh8qSaF1LyV4bIDKAnOZD4JxeiIJiCWi0RT8wTjAslsYNNWPyeZP_SOXHSXqItUeaLCwHjR0CSj3-T5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
در فاصله چهار روز تا دیدار با خیبر؛ محمد مهدی زارع مدافع‌میانی‌جوان‌تیم پرسپولیس در پایان تمرین امروز سرخ‌ها هنگام دوش گرفتن پاش به طرز عجیبی دچار بریدگی شد و حدود هشت بخیه خورد. احتمالا خواسته که موهاش رو بزنه پاش رو بریده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/29325" target="_blank">📅 20:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29324">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PmEbkW8DfX015qQMmsuOK-qlvhGXP6qVmSXnvgGMpgZ0uKHSHyN9qA7L4uyHv4U8TRMi25emQDhiKwejUQ2b_s0MGcdEq6Zxsx6cffqo7lLQGc9iGQggl2Zkqgp012b0SG-ACIbeBqPqKNQibtDOij_hcz57VtYfC4qDjLfVpMS1Gi-QPfvevD9PpJsehGx_u9bt4wZrz7LdR1TkTBLrQcU8aFG0ep-VyclS4X6_mvZIQC9jDVkv5NoRg0d014Oklp6k595c--GmO_jmr0QMfatG936M1C7JzhigBk68iZuaXvS7Uih_yEI-seTElPkLg8mmX8IAWZslKCN4j1CcDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاپایان‌هفته‌ششم‌لیگ‌برتر؛
جواد نکونام، پیروز قربانی و سهراب بختیاری زاده سه سرمربی هستند که تیم‌ هاشون هنوز متحمل شکست نشده است.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/29324" target="_blank">📅 20:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29323">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPG4TQdrRCfR5O8XGiL_L0rD33_iXr9aWYRR4Nd5TBpg-s03oQXQjZcGgBel8AYTAjjgtLhLfkgImClho-dEqwmR5Oag4mAU8iiFjkRdqly3Hqcj8mI99rjacYRYNsKtEKmVjBbilnvXEASjd03UcxzR5RZ9r2kfmN7LpUlsvxFBUD5O9BRe6gHe7y1BrQmUI8O8BmVaNoz38hQxiH_UNM9Z_x7Lu8vGug0H0Oev45ZOhVmnD_oQDIq7SJOyAON4vWb0EvMI-jzZ5wtid7mVaTgFzoT386HPRGwAoJGPksR0pnUurp2R5cb9pIFHGIAJUZc35BwC18i3OqxhGWma2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
از پس‌فردا دیدارهای هفته هفتم لیگ‌برتر شروع میشه. تراکتور دراهواز به مصاف استقلال خوزستان خواهد رفت و آبی‌های پایتخت با پیکان بازی دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/29323" target="_blank">📅 19:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29322">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3830a1509c.mp4?token=hJgr6QWcoHVT8Z0jM9NgoD8LlqqhemCALuRwi8LIGKamrOhlqENMuZEWL9Z_R4ckCTw0u-HVpaYWZNoYSAj9jBltoskCKqrMaG5G2qsFJ567jyAb02nW5bAoasaplP52s00ms7vIwwHHIp8AF9LWkngAv15m2-9pVDP0ITh6qRg6lo0b8269LM3V7--Qwe6oaBG6FzglJ8FfpCnqLU4pWc1FN4zbpDXxy_ie1YDgz5sjV6_Kwzy2Fee3m812YCzdwO6KaK75Q0-fUXt0nFa7KpEmeuOGRvLJZrdMhChEYA4KSX8DJNEOVQz0O9X7OX9SBeus1pZxOJ31P_qPpmLm9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3830a1509c.mp4?token=hJgr6QWcoHVT8Z0jM9NgoD8LlqqhemCALuRwi8LIGKamrOhlqENMuZEWL9Z_R4ckCTw0u-HVpaYWZNoYSAj9jBltoskCKqrMaG5G2qsFJ567jyAb02nW5bAoasaplP52s00ms7vIwwHHIp8AF9LWkngAv15m2-9pVDP0ITh6qRg6lo0b8269LM3V7--Qwe6oaBG6FzglJ8FfpCnqLU4pWc1FN4zbpDXxy_ie1YDgz5sjV6_Kwzy2Fee3m812YCzdwO6KaK75Q0-fUXt0nFa7KpEmeuOGRvLJZrdMhChEYA4KSX8DJNEOVQz0O9X7OX9SBeus1pZxOJ31P_qPpmLm9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
به سه پاس گلی که نادر محمدی روی پرتاب‌های اوت خودثبت‌کرده‌حالارسانه‌های خارجی معتبر جدی جدی‌ دارند او روبه‌آرسنال و میکل‌آرتتاپیشنهاد میدند که‌در ژانویه این بازیکن رو برای توپچی‌ها جذب کنه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/29322" target="_blank">📅 19:29 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29321">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MS4cyR5xsqZnjX3Kpa2qJkENlXDa1txk3f3VGJKSqcI_NY4mL2utMtShteMeRlOkWwWFxNK_kfDcn6rCEW4EaToMiOoAmcl_6CAId-gw3AH7NzjQxDQpnOmL9StqZS7fo5sM68H5oLXI2zCfj9JfEKBS-SrRw0sOG4vRwSHU4oMdO-TR-ILkzOnmU-O324rwgHTlKsdoa0X3-G4mBnIRwXiCyEzpRzRZHXxnKy_NcBLE0QnFdKYgr5NB4bmdWapgbgvz5S4u0pExzMUEjGj1WhqrmcJ9JIqPs2DoxrBBg-mdBI2cTvhS7CpSkzpadenXmgGEdFn-lWBU4IdBrDxrkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
با حضور لیونل مسی آرژانتینی؛ لیست 30 نفره نامزدهای توپ طلا مشخص شد، مراسم اهدای توپ طلای 2026 روز 4 آبان درلندن برگزار خواهد شد.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/29321" target="_blank">📅 19:29 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29319">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/197500367e.mp4?token=GA63JsFfhZXRMRm89ILGQqNRyG2HTYjh4YxH54985oLAYsRZbiaFXmooUqn5GTb2mc-TsBknAJK0jNFndteLd3wbvfaUxPcmVag9eLVEsKVG_HsUGRCybc8mfKMXu7Ztc56WHxsVIsZlLqYkJ1UvGTkv5gVnoVHBgdLPA7mBNsl0hd4_vog38IgFYwzStSqR_ZdNcrIbP9X8S3v3P5SV6-vt4paFq4yB6B0cUd2QCdtZFrsXb9DhdH41H-gBpFwYEAZ-xBaUVjoqsG53P0tRVY_B1JEpfOM8i_sH_KoIQdJBz_K-CRDax9SPKy0yVZzpJbWNgXutMgIJmHOyllfzdqjfIVdkGoxR6tB7ezUww5RjuEgMvliDjsNxDNQR9FpetDLQtHPqUtxPVWmBEAkDg8TCJKt1Zp5oky9sAAzUmYRAKe084shZBmbBBbYZDX8nyEK5f7YeNsHfv1zYgSQq86n7rYg8dpYePMg4W3msUzmaeICZ6zF-pmZKuJ8TmV6m1-ucgfY9venvYWyUsBwImeRLnK2rpRs2b35HC-KTVu49hwazNIdWUKc25wridzXGI3uePVwzlFx2YBe9tueU0OX2lvp025dLbBwOU0wEDD_PqqaBOOpPJz_jW0AkIIrCNJUYRVUQGZ08vAEuMtsV5EdjC4xk-ulzG5FRkZMWVgY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/197500367e.mp4?token=GA63JsFfhZXRMRm89ILGQqNRyG2HTYjh4YxH54985oLAYsRZbiaFXmooUqn5GTb2mc-TsBknAJK0jNFndteLd3wbvfaUxPcmVag9eLVEsKVG_HsUGRCybc8mfKMXu7Ztc56WHxsVIsZlLqYkJ1UvGTkv5gVnoVHBgdLPA7mBNsl0hd4_vog38IgFYwzStSqR_ZdNcrIbP9X8S3v3P5SV6-vt4paFq4yB6B0cUd2QCdtZFrsXb9DhdH41H-gBpFwYEAZ-xBaUVjoqsG53P0tRVY_B1JEpfOM8i_sH_KoIQdJBz_K-CRDax9SPKy0yVZzpJbWNgXutMgIJmHOyllfzdqjfIVdkGoxR6tB7ezUww5RjuEgMvliDjsNxDNQR9FpetDLQtHPqUtxPVWmBEAkDg8TCJKt1Zp5oky9sAAzUmYRAKe084shZBmbBBbYZDX8nyEK5f7YeNsHfv1zYgSQq86n7rYg8dpYePMg4W3msUzmaeICZ6zF-pmZKuJ8TmV6m1-ucgfY9venvYWyUsBwImeRLnK2rpRs2b35HC-KTVu49hwazNIdWUKc25wridzXGI3uePVwzlFx2YBe9tueU0OX2lvp025dLbBwOU0wEDD_PqqaBOOpPJz_jW0AkIIrCNJUYRVUQGZ08vAEuMtsV5EdjC4xk-ulzG5FRkZMWVgY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دبل‌دیدنی شهاب‌زاهدی برای جوهور دارالتعظیم در بازق امروز این تیم؛ زاهدی در یک ماه اخیر بعد از پیوستن به جوهور دارالتعظیم موفق به زدن پنج گل شده. شهاب زاهدی این فصل فوق العاده آمادس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/29319" target="_blank">📅 19:14 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29318">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_TcICbLDdfBbCuDiaiZxzmPRi26RkFEqI1m9oNDbFfWuMGI6dW-zlcoGKLJL5OesoB_0nv969xSPgEYk-GfJzWjHGFLJunKdHgaqLxHaP7YlhWe1WtzxjP9LUNZKQrKLFXAAH9rD5Ctjaoa8KLg1adG7j6PS7JJBQrrbHiLeBjAlNi03yiCAXZ1JLSLuV1mHGJiKiR6dVDP4b4AeiS5Km9iTJv9Upob59CT1QSYOqzD4YqxFFbc-8ZbVIJQgdWD0zQ8oOKbC28LPGApQhNL4znjV6TfaRdt6LEblAS_YQIU2mYWMVIi3iM59XY92zVViEx9rpIu8i_SJNU4bRMDdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
به بهانه شروع فصل جدید چمپیونزلیگ؛ نگاهی بیندازیم به تموم قهرمانان این رقابت‌ها از گذشته تا کنون؛ رئال مادرید با اختلاف زیاد درصد جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/29318" target="_blank">📅 18:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29317">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QqWT2coxo8byWJnrNSmsdfoTWAvL-SLNIe1tQLkeidjojrqo6SVD5VF_ltKzKC71ITgBG1Pm9n32J0wu0ihE5hZ4Kf6zisJrOuT3xnGg7KrvqY_kwkjJDN9FUmXDSiWdp4F2njSLxrB9AG8E5r-1vVlN6GEVuLOpUswjExPCpoWNB95UwqK5FXzaWa8gMqp8KdPBcXYiw1L2FReB4HGPClYmkgLjBBHCX5YeMf8oeVE7bolvqD__SeUWkWvC85T6BHTr72U1gyj8Ylu2_gWAv28q9rhHUdziYy5we9ZAlCfqlQViSd7uTXy9ypCDhkIJzjRxQLQNFmUVCdGy1fRXig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رکوردداران بیشترین نامزد کسب جایزه توپ طلا در تاریخ؛ کریس رونالدو در صدر جدول قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/29317" target="_blank">📅 18:26 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29316">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ba4575c98.mp4?token=bCwr2V9YzvCUqexugv_QRJwxgD3pyxdYbGajCRSxs0ws8HjJpbEeZuZPQnAOrbt7CdrXrdKnRenhwNEQFZZ0oDhah_kS1fL-mhdfijSg6oNMov4eVi6CVC9WKhzk9xuYc7zUqqQzaZRVg7bsbZ9fi11gXXu4Ekez7TRUjzywrveZwCvBRbMpdXDGti5htCYncJ5DwL1Kzcy1B6aMD6pAEq49urJg2uyGPhqED8boKdZsYbg0etBawi3Fs5vxNNhCCmiYBUAZEqXNDim23YqhzZMCYeX5tsOdevGS_7ZgDhQLzjBDOTD7qrJXzbb2GgNHAxa6U4OUCRyr9_rG5DJ1GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ba4575c98.mp4?token=bCwr2V9YzvCUqexugv_QRJwxgD3pyxdYbGajCRSxs0ws8HjJpbEeZuZPQnAOrbt7CdrXrdKnRenhwNEQFZZ0oDhah_kS1fL-mhdfijSg6oNMov4eVi6CVC9WKhzk9xuYc7zUqqQzaZRVg7bsbZ9fi11gXXu4Ekez7TRUjzywrveZwCvBRbMpdXDGti5htCYncJ5DwL1Kzcy1B6aMD6pAEq49urJg2uyGPhqED8boKdZsYbg0etBawi3Fs5vxNNhCCmiYBUAZEqXNDim23YqhzZMCYeX5tsOdevGS_7ZgDhQLzjBDOTD7qrJXzbb2GgNHAxa6U4OUCRyr9_rG5DJ1GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی بعداز مدت‌ها پارتنرت رو راضی میکنی که باهات یه مسابقه فوتبال ببینه؛ هیجانش عالی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/29316" target="_blank">📅 18:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29314">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaa9ce7068.mp4?token=RB0RiYie0KlADuhsEixnZ7PO2F0-iomBO95VuqWIeiktPSJmpMAgwDmZwCil_CbDeRZ3oLxXQSroM316ESc3J2gVuotVmnvjJcQKS4Yhe4aX2Np6RTzqBA9YyTsjhTlSqA96DbSoliTVu1mfRNCOy_voKdM5AvG1eTExngwDJWPWQ2NcfYUAaOqR1ilf_gY75HZssqh0cg2ZFkdm6yIHwQUF5YSgcWMj8S7w0JbsG9j2KvyrT27yuP-cxEzK26-La_q88aSok78hJb9dx1yETXXlx6IUaBFF7y7CC3L6A4M-T1hQOruhOIk2hrfB7lxJFejCVjJ7bW8jjtC8mCIt6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaa9ce7068.mp4?token=RB0RiYie0KlADuhsEixnZ7PO2F0-iomBO95VuqWIeiktPSJmpMAgwDmZwCil_CbDeRZ3oLxXQSroM316ESc3J2gVuotVmnvjJcQKS4Yhe4aX2Np6RTzqBA9YyTsjhTlSqA96DbSoliTVu1mfRNCOy_voKdM5AvG1eTExngwDJWPWQ2NcfYUAaOqR1ilf_gY75HZssqh0cg2ZFkdm6yIHwQUF5YSgcWMj8S7w0JbsG9j2KvyrT27yuP-cxEzK26-La_q88aSok78hJb9dx1yETXXlx6IUaBFF7y7CC3L6A4M-T1hQOruhOIk2hrfB7lxJFejCVjJ7bW8jjtC8mCIt6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
لامین یامال ستاره بارسا:
"فقط کافیه تیم‌هایی که این اواخر جام بردن رو ببینید؛ تو پاری سن ژرمن همه پرس می‌کنن، اینجا تو بارسا هم سعی می‌کنیم همه‌مون پرس کنیم. در نهایت تو فوتبال امروز اگه ندوی، هر کسی هم که باشی، همه تیم‌ها میبرنت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/29314" target="_blank">📅 17:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29313">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iwm5LYw9sFQYDVls4ERlu-yjq-X5ly6_NDLvi9Tdf_h_QoqI5Wkqs0mdLH6O1Pd9bearTpTorkMckYXmBvqVYx0fwEfXiGcUF74y6-pGhKbE6O2cVb5IqwzYeQJAcDtQAfksC8yfdsnt9iGl0eWlC0S9wT-Mv_ukdOYy68Uv7ggv-J2ci2-RZtncTCLutaW3NgI9-tcWGyY0aZUYPgpVrusgFE-4JwQjL-2Yrps4hc4Rnoz-PBl1myb5vL5xvAzSE4ONEMyvimaiYM3ZnW8b_RK2ai3F9e8ZewfyTbEsPbmnwZHcHycjGBvr0yPhY4FcsOwgNFXLThwzPOM131XGEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
🇧🇷
پارتنر گابریل مارتینلی ستاره تیم ملی برزیل هستند که پزشک هستند و گفته دوست داره از بین برزیل و پرتغال یکیشون قهرمان جام جهانی بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/29313" target="_blank">📅 17:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29312">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X3yR30dYZuM8sKKYXI58Mpx6u8tJkk1BOPILSeZhlQIdtbWp3UaKGJvJcWxWPYRJ4k_mNNOXpQMWbcIfyYvwAlase9mz1rYtpfg2TE-P01RTmU_HaEXy2vCo7VQZ2mzvf-IkiedJzGqgLSt7aYtP-Ojb4Jl1-3gOvOL5MKrLefaIhyx-8mpJZbJTFG8NugjZ6Uwe9cieN5NEc3eTs8obXDBSRwJRHxxoZDlcNfRnVxdeB7alFVwsm_W3ag-kXG3aY0fak9iPe1RrFc-WF7m_65Q9BJvcDmPlE_vtRnn3lVp7w_keCNHXZefPMh7QdLbwv0cd727vE2i5r3RRcpgiaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
ترکیب‌احتمالی و پر ستاره اینترمیلان برای دیدار حساس فرداشب مقابل رئال‌مادرید در هفته اول لیگ قهرمانان اروپا؛ ساعت 22:30 از شبکه پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/29312" target="_blank">📅 17:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29311">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YPUDen_aPnJhBDITYH2439mz5RLMFxxj_FzLlrrcPAoFEcq4R3rBl4aJfvDsaRFDQHPHaV20YNlmrLyJwl2ZpAZ0ghq0i-NpfAIATTIwEk5HGPaD9TAwQ4O2cVEWDP6qo0S4NrhsgtuUQU1ZyAg4oaTTLQnLHzP6j5b1EBKthJjtz9ddwah7NDmJxInHU_Ld2YzntagKIZt4dTZEOqlO7XmPnElB077HrZnG1Z_lpimYrE5f0DjhymCCfyEut_JE4q4ZIF-y8zXBr-cYZ4IPfLNk8yMCDmWOXvb-oQb_md0S8H6TCgnF9sGavvBYwmPCzozkTNiiy52DcKU1Mh9_7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ اولویت بندی هلدینگ خلیج فارس برای مدیرعاملی تیم‌استقلال مشخص شد: ابتدا علی تاجرنیا، دوم شهاب الدین عزیزی خادم و سوم محمد رجائیان. از بین این 3 تا یکی قطعا بعنوان مدیرعامل جدید آبی پوشان انتخاب و معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/29311" target="_blank">📅 16:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29309">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Curr7RLRWBJMEJIv94DXN5UBSxPYFfqDeqzbIoCmqspUNPqcwVL5mGd9OissUIcv0V0LRDhgWk1IjwlBTGzcbcy0mUyM4Dld381Mc0DrlpM5swddnw-e3vm1nvRBi-w16gq8NNnh_-iBJkNRDEh2Etlcgoz-BGXs4GIICpUZe8W5aTipOTWMRywvTcdp8JktQvv8Me9iC83YHKkUFFfKBRfyxLWmvF6nXnvfq7AuyzqDlkAQYEQgkYGlDizWcZVvXoz8EhqWgzqKXtF5r3xzJ5qMQtIrIYxweTjgIROGGqpw8omr4LZQtcbZ5KzPUAoCn1_R0awLMd4FH6b9Bm-Qkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
مادر کوبارسی‌مدافع‌بارسلونا:
اینو حتی خودشم نمیدونه ولی اون هرشب تو خواب حرف میزنه. یه بار رفتم تا ببینم چی‌میگه دیدم داره تو خواب به مارتین میگه خط آفسایدو نگه دار بازیکن تو افساید باسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/29309" target="_blank">📅 16:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29308">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">‼️
هایلایتی‌ازعملکرد موسی‌چنپو وینگر مالیایی سابق استقلال در تیم جدیدش پانایتولیکوس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/29308" target="_blank">📅 16:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29307">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZWVpUJzugUytmw1nnepCp7hnDnAV3fNch-WM7fPUen0WDvt8u3yDkRQmGlfEz5fgBnNHuPztHjNLaVmua6ZKzvyBDJe4JYxP0wFyvYAKpJOxLVnOJZJBPWgNSSasUrwyVsOa83_ewVPsePx3zEXX3MyFyERpXxhv5lU_zf9mJmjrd74TRX_enuI4-3GfT61Ll1MPSZxz9IQd3FI_ouLwfE05ixXOx9wxgFZTtKcs6muz2FkzJHVNpmOt2NC4jlB0675NNMcOw0B1A2rsRyBWaP45Yct_dAwnFx3YdI7eprC4oER_rFDlRkvXkm2_M76Sxik0qSVvpmgWlIeTn-PDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین‌گلزنان‌تاریخ‌رقابت‌های لیگ قهرمانان اروپا به‌مناسبت‌شروع‌فصل جدید این مسابقات از امشب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/29307" target="_blank">📅 15:42 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29306">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZrhhXDhIgM3pIPUd1MXF-PTmrwGEQLUwLAFwcbbPTCVD4G_VfmnsnDh4h3UQdCvuNAHJTajx4-mcHmZI-hm0OUd-blARNH0vvmsC96clDcC81pa9Hmt5ubtwiAoLivwDF8kAxz69UtVSm5BBPF3IyI1DMOzVfrIcLoW1nhT1VnM5pTRELvEhe1grIy2vhgx8AVepMqfjvXqZuwbiJewlza8SyhXyrnDjnyYlxe0jj0XaFb47XSnDslr7xcy8adZYk-ZOVRzVdbUEqlVmdfHZKhF0VhRUMkYb5yg1E5ybkfj_6cYLjgdDAKqcG7AUs82rRxcYKIU5Sw18nxt7dBskQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
👤
به مناسبت شروع فصل جدید چمپیونزلیگ؛ نگاهی بندازیم به‌عملکرد کریس رونالدو بهترین گلزن تاریخ این‌رقابت‌ها با وجود دوری چند ساله از UCL.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/29306" target="_blank">📅 15:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29305">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfa4b6c3a4.mp4?token=kbjjmVMkm6ONJXNrlx1TcZ8ZEIO1qxgmJVLlV4ZtaX3aD7PQSIvMP5TiUmk4nnxyA1TonIE-eax1Dqf4qzMWDsVBfLzPN2p595b9Dn8DJ4XIk8v8nHwK0d2X7nIjqRePxlcTPjFv19NcZPxk4yYYjyAcair50sysD4WTEQ9OeMMyEIn_x7ReFSQBij2b7U_yxmdY1iCmmck2X2qR6I6NzoR8EOpMURKP8qEW6QA7wN0sedxYwy_WwRieXrn9ROJhOUH_bjc5q-PtmrCNWtu4dr8Mk4SJbGxhNqDEhGpEaQ6LOUp1tl89mkPY54mrlO34PGUUsaP9asUV6m7r6NKHgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfa4b6c3a4.mp4?token=kbjjmVMkm6ONJXNrlx1TcZ8ZEIO1qxgmJVLlV4ZtaX3aD7PQSIvMP5TiUmk4nnxyA1TonIE-eax1Dqf4qzMWDsVBfLzPN2p595b9Dn8DJ4XIk8v8nHwK0d2X7nIjqRePxlcTPjFv19NcZPxk4yYYjyAcair50sysD4WTEQ9OeMMyEIn_x7ReFSQBij2b7U_yxmdY1iCmmck2X2qR6I6NzoR8EOpMURKP8qEW6QA7wN0sedxYwy_WwRieXrn9ROJhOUH_bjc5q-PtmrCNWtu4dr8Mk4SJbGxhNqDEhGpEaQ6LOUp1tl89mkPY54mrlO34PGUUsaP9asUV6m7r6NKHgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی‌از لیگ جزیره به لالیگا میای؛ برگای رودری ستاره تازه وارد بارسلونا از سطح بازیکنان والنسیا ریخته؛ پنجاه بار گفت داداش اینا خیلی ضعیفن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/29305" target="_blank">📅 15:14 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29304">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/er37BMTgdNXJ8e1OVAUyXFVTDZfkDdZbfMLMm6AXczLLlD9Tz32QxEiTlT0roEVvQNs1DhzP6sxX2s90Of_8-E7o8xQSyuGIKTAvJEYYxQDyDPV0Qb7rBcwn-Oo2reL4WDARqEb5M9xdmvwPaA9RXBilDnxjaAC7G_MPpdARpkSLNEiHDpRZQktM4XBxjDrepzf8qBeQSHMLa2Z2Hdzx134OnHVhaIPYiJrFBt-9T-ISqhB0qhvTUMUFVzjW5XL9h7MdoMmRIQk_sOY-1VHvYkoCW8b4TPQnqNWC8LEw8xHekeSsWKExB7D5VLPemVNl_45gFM6bP7pcz_DXpqCdOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محمدرضا شایع به این شکل جواب میثاقی رو داد؛ تو خودت مفت‌بری. دیگه‌از مفت بری حرف نزن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/29304" target="_blank">📅 15:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29303">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7pRiCYal8tkgJo35OXDYNjzMcZDST42mZ1FcS8sSBZDKOYXgJEg1xB6rn19wXrAe8Ug_CDNAxG8zr02bEy3DErmy-SmiFGAEHpOnBIVm8_dlUbLuQ6ReraeCCGAl-dcKuEuy5ifCAGC_d0We3LPX7tDXnGxbB8W_DZcBMO85KHaP2SzSTuXTiWP4GLAO7lMsxsyV-C7NKvk8B9BIGIWr3tEcyRy2ZnveDlAiwXPAzx2Gs5LoqjaR42IH_MzPgTOFyuTSq8UTW6p2pzLemN8EijwdX_CEHgi_IgP-1OgvLng3VHSGyizOpZkxN9IbPCFnMdXTSSUPj2X-1x1s3AniA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
دوتیم بارسلونا
🆚
رئال مادرید روز یکشنبه سوم آبان ماه ساعت 23:30 در ورزشگاه نیوکمپ اولین الکلاسیکو این فصل رو برگزار میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/29303" target="_blank">📅 14:27 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29302">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D2v_euib9HsmMf5DjL04YWbds9wZKo_hNAnMawpi5Dr9rJaaQkfionfX4u15fh3kcopBS3wEzeUYMF1flb1pM2LjagGJGWW5JzU9DNjL9VMku-EqjMVot5P-oxAk7u3-s3RiGW1zowpRD4TprqyfoCNSNg8RNsgF-kDLkog8OVMQ3cgOtKpreqvJDKjhJJN3QPVwWuhW2ped3cMLLP_dDiIr2CBzrNmuG-Wut1fA6bCluxhQFEpLQMXKJwXM32QD-067Q_0wzhj1ZvG6TSpOsrybbyVFjbk-jes-eFlqek23O87e9jPlbVmfZCRMtd47YcJQ1wIpu8M3bqtD5FILAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هواداران باشگاه فنرباغچه بعد از شکست این تیم مقابل تیم بشیکتاش خواستار برکناری اسماعیل کارتال از هدایت این باشگاه شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/29302" target="_blank">📅 14:08 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29301">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d011bda7dc.mp4?token=MBfjm0c0dYmi9dh5WGBFdZJNx6w_nGJhfYfMTS_YHm_H4TDOEIXw2jgNWOAzINXwz8V2nYN8ui9NX4Xqa8J1NbpXjDBs3flMN0MsKbL5lekleDJxoEcINcvnGpQuZNVLVFcnuX_TZ7ubRWCguzWLObITZAh8OjLvtv2rH-4nEEG_w59RK8roOverD1UsJKIOB-vuMW_zCAG8yqM4mAlroG-L-ddefDTFK3Xuj11Tv-EsUvBurTxrUXcIUjXSFastUHjAISqjchU8z4IcAa4ZLAdphTgYCKsszQH0hETwE5Ngecr-t8xdheZ-u538Moy-gr7EYjZrkMU2kJQFhTDG3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d011bda7dc.mp4?token=MBfjm0c0dYmi9dh5WGBFdZJNx6w_nGJhfYfMTS_YHm_H4TDOEIXw2jgNWOAzINXwz8V2nYN8ui9NX4Xqa8J1NbpXjDBs3flMN0MsKbL5lekleDJxoEcINcvnGpQuZNVLVFcnuX_TZ7ubRWCguzWLObITZAh8OjLvtv2rH-4nEEG_w59RK8roOverD1UsJKIOB-vuMW_zCAG8yqM4mAlroG-L-ddefDTFK3Xuj11Tv-EsUvBurTxrUXcIUjXSFastUHjAISqjchU8z4IcAa4ZLAdphTgYCKsszQH0hETwE5Ngecr-t8xdheZ-u538Moy-gr7EYjZrkMU2kJQFhTDG3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🤩
خولیان‌آلوارز
🆚
بارسا؛انتقالی‌که‌بالاخره‌اتفاق خواهد افتاد؛ رسانه‌های اسپانیایی خبر از تلاش آلوارز برای راضی‌کردن مدیران‌تیم‌‌اتلتیکو برای پیوستن او به بارسا در پنجره نقل و انتقالات نیم فصل خبر میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/29301" target="_blank">📅 13:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29300">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnuUnAnyUihpivItYGi5L9gdLWZy0Q7nHmOLBUKcbjdM1Cc7hlExUEZZt5evS27lNoiu1o3aoyV9YSLCC1_Ek6WzgMWXx7ERB7mkzqtfvOGKMD-YrFm1sRk-JH3GrWA459rGqXhe52HBHsKv23_64Mm6ght6Z97olXMOD6tof4bpGbmQWhiaFckHhXEuMNWnn8WP6s5uem1L5pl2NMPl6QHHNnfAOd6Peh9lL3_RiyJJGZa0vvoAM6r5Cru22Zne4la1mvAYV2AyKjNXIVs3U3PLjiWtYPiAHBCb-ZIG7kwals-v0Rvv9QnKkdOIK6Pu3JwQLanYZoAxgbHo80prfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#فوری؛‌ کارلوس‌ توز ستاره‌ سابق یووه: کریس رونالدو و لیونل مسی قبول‌کردن برای بازی خدافظی‌ در دسامبر 2026 درتیم بوکا جونیورز هم‌تیمی بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/29300" target="_blank">📅 13:09 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29298">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rz5W02pxr6rZh7kDLsdk1Op_8UjmG8bBZU-JCy6CZwHU6G0MSvtgnRc9HDv7EUC2s0AedAJJ_CTXno1labwBljSf9Px4UwNOZh3JBDxPqWLBONyPsHJJncpSVsKZHu1giWPiY5JZEXpVOxNTUf2cPMBfxM96WMTZHfjIciIx_EI76AAL5MGh4zUwvNlfz_EiZyvKuOAtiYf12ZT89OF66bKLFI0DiE-cYgAwtiha_-FFZLohsoz7SmRbONmu8zTSGNOd59tmvifDqn9Ga4QjdTm4oelVZC9YDykT5ab0sl3kKeGGoVxBoLmyKY-cZ1taYkti2i4-_k9W3Ygj5m1tzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d_YrID2AYQGDgNk7__CQ4bmE6Q8roygdYwPJ8f9olT-RsrS5J-jUxhSNIoBr6gNkvrh04O8Je4UwZQa5lmlORIdoWvCtCWYFhVCiUpkToM-8BQ-lstWrq5KzXElT6NoUdoSvGC3jiOHH26DcjQduDQASGdE2swy9AZg95vW_b7X2uJ3_0_wx7WOzYhimwm_c4m_mWpzMjYvw33AORcgN3f9u0u8uuVWkxHNumsDD7mScIl-2NvBaBWjEDw7snT1E7G1I_nrSfMe-ZWQ4sNZ27j9RVvVaf5F-t2kfbexkf72M1pnU1kc20qNqKGfwObJoT2_rVuD_ZTvRUfvr-XYrUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
اسماعیل کارتال امشب در دیداری حیثیتی و با ستاره‌هاش دو بر یک به بشیکتاس باخت. ولاهوویچ که درجریان‌بازی بااشکرینیار مدافع فنر باغچه بارها درگیری داشت دقیقه 73 گل برتری تیمش رو زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/29298" target="_blank">📅 12:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29297">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fR39Db6Wa6-fXfsTtGBiNgko-oB61kHlklNAlesJLZE-E8_NaBSxoLDg3OzYUrgaziRriMyMx3V78f_V887ssYJ9SVOM9aHCze8jhouvOg5Ek87M5yA_ueMTAZ-spNvFb23iXgn5jH-RdAuHOH2AZ75R3hjy_q7JNguad8lAWRUBVPJxseR9YIAq4GTr25uinXmlCeLw9qcQ0NsvZW7iCa4ZPzBYzLY6BF8zIFjFScjNXDWOCXTDoLwleOPaySoDXIw-_gMHjCEoWPEg8L84EelxnbYX-uE3I63Vtps0V7tYjux1u8_DWRm3gEIa8iuv1zVLEPMpIxVP7hcy2aivOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ خولیان آلوارز تمرین امروز اتلتیکو رو پیچونده و گفته دل درد دارم نمیتونم بیام تمرین اما یه‌کمپ‌دیگه‌رزرو کرده و انفرادی میخواد تمرین کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/29297" target="_blank">📅 12:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29295">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CLLJzxiqPJX99Nu1Hf2a4o2BKibKpXI-kwBnm95L9IRLLHXAJ6aH7l2rlV4s1xqGqEOcDwvpaKa0CCIWhGkTO_bNVjEJ1W97pvIQULtKGBmi3vmJAIOnHxUW5DGZORsm2c2cebcla-ge6hc33EclYCDyd_K7Mx_1aI12gqUumL1W-cv8EaXVRtz0TfW8VjZWRAVR3njohjXclvYz6xcMtV0Nn7vach7lpEcBN_RVtgZIxaXeuqi4pFX0hplkqE0fuG_AfaXMNo2SXp4Cx_LCxIs6CLEI91mZRkP6WB5nxmjzL49SsfZkGm4MSL358ciC6afJrR7kShhpDANf2xPOqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد نیکو ویلیامز، کول پالمر، لامین یامال دزیره دوئه در کل دوران حرفه‌ایشون؛ یامال هر همشون کوچیک‌‌تره از لحاظ سنی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/29295" target="_blank">📅 11:40 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29294">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WwhneqcYNrOEX-jgMt59kM1n7tgoW-viT7anfuiIiiOZdAm94JD8NBL_OM4cMkeAGlbf6J3R00K9-5aQFB-1gxXMxmxYjPznc-CT2x_iYEHQS3i2w11Y0a_OzHlPTzMamp61TWnsBQD899GTOwqCCiwOcMjtIYKdEe9wpheSXulrEJW1QuM7yKUpWEty1zVvwU7P9kDgzk7QnQxef1JT5VXhJdBS5lEml8Vdo8bUJBd_6mIgHRa6WP93lO4KSxapZ4aKBTlm0IIDXE6EC9s0nPt-Bw9c-nxom8mKjZ-BEYImj3wVFg4aEMTs46ztgSt7AbG8vbI84dwL9_3e-7g-Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
امباپه در پاسخ به اینکه آیا باید در کار های دفاعی و پرس بهتر عمل کنه یا نه و مقایسه اش با عملکرد عثمان دمبله و رافینیا در PSG و بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/29294" target="_blank">📅 10:56 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29293">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eC-ckA4nUkh3ez_VqLXDVFMYUbv6H5Mk-u5A4YN-B5TL0FgY9huhAouSgqsbASySi-juflx1HB_CwLQrn67C5l2OG86CT5Bv2hKcWb5c2Nl0sFzGHUGnfCT0VJ-nvW9FoNHVW9R0Geq2zzs3nZCbA1SVsMOEMyhZlNwoG6qRkOH6_JpsX3bNeSH72lVhLOQksmsvqn37O8NzbWk8Nab-utVgjgWH8NZT58AswWF3eK7x8ISSSmUAJ0CtGM-NpBPYGa9-_loqAesbDv24c0-ClE5al_nzGoidyk0LUpf9p0PnZ-XGBh4Dx4pMiMSEm_ipwWvo9Wi6Lg_qap3bTS0Ugg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
منظورعادل‌ازاینیکه‌گفت خداداد یه کارایی کرده که فکر میکنه هرکاری کنه کاریش ندارند یعنی این.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/29293" target="_blank">📅 10:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29292">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RxkigT86YNgJvxjf3yo5qYzcxW9CNFJMz9oMKEuGx11UH9gqlMUsyUfVQjUvJU_8TaT0j95CTW3SLatZVG6_VTb-VejcgBeqxI8XROQsVKhO8u-4j9gJEZtzkLVasKC2mJmVSZjtQ2DgcBPEemThoGyyIgibMYB0reS3p7s8wRQoKR3mBVkPoMOdQEewqvFURZiUCnCG220tauvjc9u_Zk8e4dV8Q35Rqv7jwTqakVV09Zpf0dGAoWziSGGELp8rh7HbBa7KOU79kdwwIYDcPnwYmNTsffR7OW_V7Ts_J-Ct8ylQ0KEljzh4M0qqqG_3K8w3D7wl9VJ1wV5_aseSiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛دنیل گرا مدافع‌مجارستانی پرسپولیس به مدیریت این تیم اعلام کرده با دریافت 400 هزار دلار حاضره قراردادش رو با سرخ‌ها فسخ کنه. به احتمال فراوان بزودی گرا فسخ خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/29292" target="_blank">📅 10:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29291">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FQwvPCFXWFm9cd-zAf2nDWhRkZt_DfQxju6XUTfjQgUJ6JQOxFPp6KAIyw8ISfnt-U-ZkSk_kA1MaY7vn7b8Dc0bXORehD6UOWwn1XiqYucRVLlBaKxYCNenWEQx2YLeltBphwnKslWKyJSlQqfsjuZly_fp4hv99y6wtsApy-JIBSdYS0XaGPeqUYp0A7CTjaNdiZ6iXdmP2WrP1yG5x55-d0PXp8AD7Y5XrVwwfhnDcwqH_8LckFsY0SFeQFoONmOoSvJc1E2ghpbxU5eWulJoPEGtjQ4h_mfbSUbLw3trKIAz1H9InL4u964aNUXuSV3q-CHWEaLNGWS4Oja_rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
ترکیب‌احتمالی و پر ستاره اینترمیلان برای دیدار حساس فرداشب مقابل رئال‌مادرید در هفته اول لیگ قهرمانان اروپا؛ ساعت 22:30 از شبکه پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/29291" target="_blank">📅 09:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29290">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/roUbm8NYJ6fqjIwzUgcEPv_3Let_k4d9opuQC_fJCul9Fzhs9MnFgfXf6FQ0aa4t_HLj8U6-Jtl5wd9JEIxjJ33jkjFRiDgRkJcFtlU7YMGkNcgxnDfxDAlJW_KKv7Z15JcZY_Lb-RwaE-WucbrOY1PDJqVXtMZ8QV9R5K35Mu42ZA7c57FapO-bTqEZADQVCTqmhd7LACyO938uK5b0rrdSiVnt-f_ATqW9WlVHuPKNKl3jKSxbyQbu6RU9_0l2M0dc10t0ljAHdQZNuh_q8Zl_wEuMDRlTmJKuYkXts2DwSPZDojIjW8WIR0Q2KgKTeRW45PDBUAnJd1ORiB-9kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
ترکیب‌احتمالی و پر ستاره اینترمیلان برای دیدار حساس فرداشب مقابل رئال‌مادرید در هفته اول لیگ قهرمانان اروپا؛ ساعت 22:30 از شبکه پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/29290" target="_blank">📅 09:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29289">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔹
👤
ویدیو کامل ویژه برنامه جذاب امشب عادل فردوسی پور با برسی کامل اتفاقات این هفته فوتبال ایران با حضور دو ستاره جوان فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/29289" target="_blank">📅 01:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29287">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8uN0-aDxFuf8uB5VMtbe50q7pgCg_bnxsnZzTIa_DHSjyGzs_nBLvdr5zzCYTG2dk36NvXJSfvVLDF1LpTAimmTmF6woGdfJCUZGaKTDdtIvZxL6vPU9E9hqym80snIYSyYjjG3KZa2XZc1YOuZ099GHzJF-RlmRNXlB1GZB456zhfbklK6Yr5oXuzVaeQZrrzQ1_zsZ3JPXTmgZGBsdJb5L8BKOQJTfvtB_XR9drqF-UyMZ85YRmOuvrvCm0izKmzohS_MAlh42RT35pQwPG0HJ_-DU8rJ_ah9I45zDoerDuDL8Ksd7lKcj41ffrVNHstehWboY3kg-4OkQrw00A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌ دیدارها‌ی‌‌‌‌ امروز
؛ آغاز فصل جدید UCL با میزبانی کهکشانی‌های‌مادرید از تیم سابق آقای خاص!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/29287" target="_blank">📅 01:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29286">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6vFHudmpEqE-G0cUFcttNzeu_ARMAau4fI-2ZdQm3zmIL9-phaZ6NagXAh9EjmO9WkuXa-FJtxIqQCi0v-xbHvTYHXQEoSRAbHHrVrLMY6-YUSl0ml_d--bayQcxhJ1Rm4YNKgww5HVyXWbSyD_naoHuhM3DVt-0oE9mL6VrD_xMbUf9WI9uYjBN3pe23sK0n6UCRkGZDVVmLctP0qLn8IudfPXFCUT6d7A2lyA58MRNDOY08_WFu9PIlRbEc7tShGvPo91IP1w7QSA2Wj3aqziUYDMEjH0dpvP_VrFU_LuZPKPaAqpUT6OqzCIj0F4R19zlm1VkmMQDeA57cBn2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
برتری‌ارزشمند پرسپولیسی‌ ها مقابل ذوب‌آهن در پایان هفته ششم لیگ ایران
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/29286" target="_blank">📅 01:35 · 17 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
