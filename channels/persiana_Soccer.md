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
<img src="https://cdn4.telesco.pe/file/vz7bcqj_oJXVCfvEPmgQELfxh4t-5QdLg4VcQ4emrlDbWIfuZX4Guzy3wnoZ2_qBKCdoJ_XkaEaiElq4d-lSZxiitRSNIJEZ1tNz9CCCyQy_MNbii1XfO9q4UbABREeYT0TbIijW_iEU8MZx75RiSFutgPju_glLE-2p-tFaDrdYg6q2eDk4bcCpsqcDdi63u_jnEabHngR_SWm3zLbgTJKoXHxT1WPSdglSu3O8Xt9cJRgcN78bGLCSfwKdrFc8ZSFHHs1tDviZB3M0EZ9gwbx3sGACeHw3SNJZ8WWic8CG1hX89q_7lKZO4oNihxEASCFf33Qq9koXB4y1C8xjpw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 473K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتارتباط با ما:@ads_Persianaaهماهنگی و رزرو تبلیغات:@adspersianaaa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-21 22:53:43</div>
<hr>

<div class="tg-post" id="msg-31523">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e058158de7.mp4?token=QsVYl_Xp_YjKjnyUEp8gAZRRge7Nu1wYySgkOtYWTv30868WTYBSAB9poc25_Q7Wu-eJC6jGjh2UXFgZrAFN7ZXWkkdplo9gOEFo6nRp_p_56zhmcvE2gSoItiNoDa9yX5ajhU--p7AKuyIqMhi1OqyCBNFE1GEdYYUv-1YEjV_shTeLK4Rdadq2R4XFxocjTOYm4-8eOll0oS0KWCJ6lNVQYWLatI7wyj6Dhhw7lB3BUhCCj9b0SJzkpITBbdAkVfXOs3h1wQCw0k48PcSYkfhQn7x0BNVfXbRYTLSAx8bOf6vYBQAyG50UybGFR0wee_kpcZbDfc9r-tQ3IA_oEmCdELcUXHw6a2tPUxX4n1XnlP1i1BxC5Ma0a30SRnyu2ExaFJ8cypMGbahvQwAB7OztG9i-As9rTYgIyeid_uLZOX88w5SQvYApR5x5Sn8CzP2qbhQtx3qtBntbGf8ldWUmCUVmFbl2XMWBM17NG5ayFKYUmV7L8Y4qlqpAprPAqz6stSWGGBYNwG0B3XWKjRahRODHiI0_KDKZ2hRQr2RQpAC8OAR0cq1i3iJXaYvhPgIlN4IQZcZctOsD9nNoTnCTpzWvkFR8fFVWzBhEslLTQKmx8plBQr_ZNYYBa8sdpF84EyvbvtMA3o2lVqxx2izJ5ipI7z5fWBsniIawSVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e058158de7.mp4?token=QsVYl_Xp_YjKjnyUEp8gAZRRge7Nu1wYySgkOtYWTv30868WTYBSAB9poc25_Q7Wu-eJC6jGjh2UXFgZrAFN7ZXWkkdplo9gOEFo6nRp_p_56zhmcvE2gSoItiNoDa9yX5ajhU--p7AKuyIqMhi1OqyCBNFE1GEdYYUv-1YEjV_shTeLK4Rdadq2R4XFxocjTOYm4-8eOll0oS0KWCJ6lNVQYWLatI7wyj6Dhhw7lB3BUhCCj9b0SJzkpITBbdAkVfXOs3h1wQCw0k48PcSYkfhQn7x0BNVfXbRYTLSAx8bOf6vYBQAyG50UybGFR0wee_kpcZbDfc9r-tQ3IA_oEmCdELcUXHw6a2tPUxX4n1XnlP1i1BxC5Ma0a30SRnyu2ExaFJ8cypMGbahvQwAB7OztG9i-As9rTYgIyeid_uLZOX88w5SQvYApR5x5Sn8CzP2qbhQtx3qtBntbGf8ldWUmCUVmFbl2XMWBM17NG5ayFKYUmV7L8Y4qlqpAprPAqz6stSWGGBYNwG0B3XWKjRahRODHiI0_KDKZ2hRQr2RQpAC8OAR0cq1i3iJXaYvhPgIlN4IQZcZctOsD9nNoTnCTpzWvkFR8fFVWzBhEslLTQKmx8plBQr_ZNYYBa8sdpF84EyvbvtMA3o2lVqxx2izJ5ipI7z5fWBsniIawSVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شباهت‌برگ‌ریزون‌گل‌تماشایی یاسر آسانی در بازی امشب استقلال‌به‌الغرافه به‌سوپرگل‌خاطره انگیز آرین روبن در دوران حضورش در باشگاه بایرن مونیخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/persiana_Soccer/31523" target="_blank">📅 22:42 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31522">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NUJGgzbtjfYcHYg5e9EtwuOoB_b9VaBMvI2wLPLcD8zmgHGv28hcVl2LBsWkq4GRznzJnkvIu-oPEm6NLuR7nle_mWND2qRhsebrKeTOvmvueQEPg2GkZM_6eVJqKKUgu67rG-C4TOXaAg4ggvR4LtkS37CNo3FmLJjREtXnCzsgp5sTkrp4WgEPtOHy6s186UnyXGZpaKFjx8xH1eKOjG4p_ZLHHQd_FytOp4AzCMLkvTkXo00OnIH09KbcRTFsjJkm9dPfL3H0t814EfBdWb6ASrpQItasdVU0M0CHe9JmDlGUlqlMyc_jTo-UXH8K0bqfW8mp10Izxc_t9b-YnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دانیال ایری مدافع جوان تیم پرسپولیس که چند هفته به دلیل مصدومیت دور از میادین بود در فاصله 24 ساعت تا دیدار باخیبرخرم‌آباد به تمرینات گروهی سرخپوشان بازگشت اما به احتمال بسیارزیاد در بازی فردا در ترکیب فیکس حضور نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/31522" target="_blank">📅 22:25 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31521">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d9d3f2c25.mp4?token=dTwiSrtqih0oyKdcTZ8GszxnuzPNXzJxsVKZp8FeVBGQJw4WimYNpAt-u9Sz0Xk5xoOYYcBU8RCsjuUZXZn28MZ45CIwxROyiewPdNmyMXp3NMnrUdjKyC6vDTlfUBbJmqBu3inWTFHov23trCFPJFtmHOTvM8_fP3YtF093IfAyjYrAOCX7wT-QnC6QiDnPjTtFUht8T0xQxE--dnq0C7q8t7BaES4dK_Ywxa_Q8LaasSkMuz1t-jeTpssUQ13ye0dAHeQlOhnHF-87mCFjJpA8vDSTa8uBhzgwdgMQ5YOcx3ye060GCkA_VQV0CtRU0VMCBepdoeZFZTSRUnj_hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d9d3f2c25.mp4?token=dTwiSrtqih0oyKdcTZ8GszxnuzPNXzJxsVKZp8FeVBGQJw4WimYNpAt-u9Sz0Xk5xoOYYcBU8RCsjuUZXZn28MZ45CIwxROyiewPdNmyMXp3NMnrUdjKyC6vDTlfUBbJmqBu3inWTFHov23trCFPJFtmHOTvM8_fP3YtF093IfAyjYrAOCX7wT-QnC6QiDnPjTtFUht8T0xQxE--dnq0C7q8t7BaES4dK_Ywxa_Q8LaasSkMuz1t-jeTpssUQ13ye0dAHeQlOhnHF-87mCFjJpA8vDSTa8uBhzgwdgMQ5YOcx3ye060GCkA_VQV0CtRU0VMCBepdoeZFZTSRUnj_hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
گلزنی‌سردارآزمون ستاره‌ایرانی شباب الاهلی دربازی امشب‌مقابل الاتحادعربستان در لیگ نخبگان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/persiana_Soccer/31521" target="_blank">📅 22:10 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31520">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/559d04596c.mp4?token=jMaAF6Pr2ugUpsdCU_0sD4UD91PbD0ywsYkUuQbz-_QHMjT0Kw69EA6qZpfyXaESBNeVIxEoyjLgjnNeWJk8PlT-zfonEHec7xJORoZyXnknK8iPjFHvuOWcwVlmicesH2C3eByp4RKu_vdyBOreyfX0FMfv82FD5-OymeaPTcxXdSvzhCOvB1PF7sFhcLCE5ddT3dwkyC-wongb7NGCf8qFHE1JO5r1DYZ_cvOdYThnkeiR6LiSHc29DXcR5VfVmooIShXy3fmA0gvhK8dn8Si8rOIh8AoVknjbnZGGrgg9usg74z299GVI6ic1wvcJdN4B6B7WIpH0cYDRFTgk-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/559d04596c.mp4?token=jMaAF6Pr2ugUpsdCU_0sD4UD91PbD0ywsYkUuQbz-_QHMjT0Kw69EA6qZpfyXaESBNeVIxEoyjLgjnNeWJk8PlT-zfonEHec7xJORoZyXnknK8iPjFHvuOWcwVlmicesH2C3eByp4RKu_vdyBOreyfX0FMfv82FD5-OymeaPTcxXdSvzhCOvB1PF7sFhcLCE5ddT3dwkyC-wongb7NGCf8qFHE1JO5r1DYZ_cvOdYThnkeiR6LiSHc29DXcR5VfVmooIShXy3fmA0gvhK8dn8Si8rOIh8AoVknjbnZGGrgg9usg74z299GVI6ic1wvcJdN4B6B7WIpH0cYDRFTgk-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
نتایج و جدول لیگ نخبگان آسیا در پایان دیدارهای امشب؛ دو بازی مونده که السد فردا به مصاف الهلال میره و الاتحاد نیز از شباب الاهلی و یاران سردار و سعیدعزت‌میزبانی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/persiana_Soccer/31520" target="_blank">📅 22:00 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31519">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LDM1uYwjBQVuQIIpCqg_a5o4uzZPhygBAW4wKd7WPnkcs_t2NFerAj8olyykYrkPbrI1s59NAynHUFn-5c6lK744-To2ucWqGg863GF03CILbbCOjt-JcV7B7DptlveqU2NM7YE6jerX3QST0T5jLxGOKnivbEr2QW1kvWMyKhtksfVEyDwCm1gv1Oj1ZLgdyFl0mewaqMSeeTVsCFTGS0F5Nl2IrMLEJ-s4uv2pCMupq9YjFiaqdR2Us9XnAD0F79rG7IHx-O7xAkdzbSJS8pcqqN9qWeRWPqFybuzwFFZ1knuOEKTRGHaOUPeLbaw3mPI6il0V9S-8tLGxFGk49Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
تایید شد؛ با اعلام کمیته انضباطی؛ خداداد عزیزی سرپرست‌تیم تراکتور به‌دلیل فحاشی به امید عالیشاه چهار ماه از همراهی پروشورها محروم شد. عالیشاه هم چهار مسابقه گل گهری‌ها محروم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/persiana_Soccer/31519" target="_blank">📅 21:55 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31516">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b6Q_Q9fkpaXF1JALrsKNsRKMSLGmjdbrrhCtK2AeufWEhA0uQdihHwxvCCU_Q8FviO2LpQ9i0rANLgOrONn4VKJh0rlTRrZbLrw8kaPsV743VF1kBvv-TGeKU3hcBKAOqHD75W_-jhOg6cPKjk_0Fq2t1maqky6I0l8djm58eUfx2NO21ljM9ZQRT9COazelNjsMRl6ncWHHUK4hFKYdEGTH3Oho27szLpUx1FXdaQAQ6QwolD9gQp7y9oNjgYn-rFgVxglzl4gsFZzHzLJcn4oyv2TFv5rV1cerPx2ui0GQeHMh9ORCmoVaYpNNVXxy5wWmDsGDcrJZmlxKHTthLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/syHdJoVZYba1KgfkA_GhVt_9cGHnYiR2VuAaBxgq4yp2crCUexGiMexaxrcg3fPUslzyvCqOFZ6QQqOLjlZQGC5zU906RcrmXx04RiDBJc6B3FigOlm82bGj3nE3NKJWW2cB7polifben17kji9ABy9L7tRE7XtZhU1eWwt_anxCL_5wd_wE3_2RAk8SZPAnpGFAMymtrQ_cJbqTEYC8Xee-PI4d7uCWspoRISl6Sx0GKHKKzFUXFjDsmPLg3e8ZpxalzB8gRp4Iw0QNLBvRV_xsw5kPSTDj2oxVUcuG2T424jTIVzaAv5jLaTKHjHaSrQJMc0Akl8MLXRB3adDMzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌دوم‌لیگ‌قهرمانان‌اروپا
؛ شماتیک ترکیب دو تیم گالاتاسرای
🆚
بارسلونا؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/persiana_Soccer/31516" target="_blank">📅 21:36 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31514">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t6YsgX5r5-A2PJnY43lXRFurMDuTVPA3tb13DfGJYtrOHsCTwt6eJAHRO3sd-IR7YgHK8myRrAm8l4xPwxSTihjuvlnPugWttkYTAtkv7oG-mvcPIiKKOL1z3RUmeQ4taEvmLWMurI-9eQFtMVmPE0-83yETRGWCZHoNbRxT-tktSn2xGA4mwnhQqyWM8psw5txiBkkgedQcBwsbM1BuIGEEq5uGUCVpfV_029Ano1buuYae5pzQF_huPY3SvcaUJ5j3VAFlvmJAAS6XPEFCNWUTmwK5GIGkWjq3TV97G7CG_DYvX6-WFJ-gZY5TtSIcJgylpV4PAUFsx3kE2L3zsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GZI0HGFaR9bsiOmE3KIgZtTl5mByM3QKzhgo6b_wDQE6QPxKlyGJQkl432MdO9s5jo6tl7KdlP_siJRhR5LJRfFX-KtrEgFLE8jbYRpHpnFfD5Qk3BZrbk5zZndCbh-yoSbDl6Hwp0iFqLSHlhCHGalOK_EwGK-R10yipvnAmnR6ZhbSAAeB3xXhau9j9R3Lwq7RRjZ9oD2hTR66wct1JVOtc9R7E7g8-Q_BLTJvCEsI-tt45NKeojX8TH1k10QdQnFyynLe5FTMRRbIbUYEpjktkQx6ezlAlZBGpMgulhFp9tgE2A3vLQTAH2XS6dBskxdSmjtI8gXwNaYvg0D0Ng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❌
کاکا اسطوره برزیلی باشگاه آث میلان: وقتی همسر سابقم گفت‌که‌میخواد از من جداشه و مجردی زندگی کنه من همه تلاشمو کردم که اون بمونه ولی دیگه لحظه ای فرا رسید که اون گفت: نمیخوام.
‼️
اون روز به درسی از زندگی رسیدم که میخوام به تمامی مردای‌جهان بگم: برای موندن…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/persiana_Soccer/31514" target="_blank">📅 21:22 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31513">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBKj4gP-LJUxJYO7Rnbr8hxWuJp1SP_ZQnn7X2bx5GPR0GNi2n5jkkDv04s8yn-8VPCsBJJJer5iMX__YZ8NGantjB1UqUxgURAN0EPk0yKIskYxPsyCBIdYROeS0HywTe-ELnISNdoaN2AK_M_uTSGo_EZAk1DgFyurL0H91Z_wJLCJOn7CUdFxDa6rAsp9Givnyp7JGht4xxKpUYZoPC9W5kqQDSd8l4SmrfKgxuvB11oWJEBjbtomNyS9Ml22VLsy_rnIOXynwpGRr_s9-SUS908ZL8Evfypl070pg1zmJSsHctDgnLOT8P__eTT_hsRoAk6wSVDtRM0LALVktw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🟢
مهدی رجب ‌زاده نیومده اولین شکست فصل پیروز قربانی رورقم‌زد؛ محمدخلیفه هرتوپی اومد رو خورد؛ درخشش فوق العاده یادگاری رستمی که پایه گذار هر دو گل فجرسپاسی به آلومینیوم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/persiana_Soccer/31513" target="_blank">📅 21:00 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31512">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00694d1532.mp4?token=Xd0zjmpmgAj4_1La0lr1iW2wu_h7ucd8GmeGmoggYElCHSIiUy0STJPzPL1PEvbXArDxtAvSzJIcQEUd5LiN87q71OGDxhfp4D5bKEVZa5mFMeyBGdJVJFd1yNqE4i0sLtAIfkF8--HFlO9pFGOuk4hy-gw2XqzDj-7ilzqTAY0atpyeC70GeMowSezLn4tNHoZ1uBSDyd3bNuCbcTQPQGKTr7T3O0c6Ae_gYqjeHsoRFBg1YtrbTVU5Q0P1x4JEz6IMJbMnJDE6qpMt3KpgU9ltEyvpnmnsmnAb8pQXVYmI9LtieynFL0Leeow4w7mdFo0xcgtYBJLuFfn1pTQiVDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00694d1532.mp4?token=Xd0zjmpmgAj4_1La0lr1iW2wu_h7ucd8GmeGmoggYElCHSIiUy0STJPzPL1PEvbXArDxtAvSzJIcQEUd5LiN87q71OGDxhfp4D5bKEVZa5mFMeyBGdJVJFd1yNqE4i0sLtAIfkF8--HFlO9pFGOuk4hy-gw2XqzDj-7ilzqTAY0atpyeC70GeMowSezLn4tNHoZ1uBSDyd3bNuCbcTQPQGKTr7T3O0c6Ae_gYqjeHsoRFBg1YtrbTVU5Q0P1x4JEz6IMJbMnJDE6qpMt3KpgU9ltEyvpnmnsmnAb8pQXVYmI9LtieynFL0Leeow4w7mdFo0xcgtYBJLuFfn1pTQiVDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های‌امیرقلعه‌نویی‌علیه عادل:
خودشون برنامه‌ دارند و مجوز گرفتن‌ از اسرائیل مجوز گرفتن یا جمهوری اسلامی؟ اسپانسراتونم که مال جمهوری اسلامیه. تا جایی که تونستی تیم ملی رو زدی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/persiana_Soccer/31512" target="_blank">📅 20:53 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31511">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/icfomzqlyiU_UUCCoX9lNtVZtkGGQ8srbs2oFpPD8yGX0xQVFCol4taJA3WRlHd98Pl1iJkTqI2Frf5lPYRVK72nce52xe7UydnhvkO8l5ulJO4UmhU0sMV6iPajX08sxxT3eQfUxNJ8qQGWXwo0yjo2CZ1Ct0UmBnsM5aESgtvS4dKPFoEvpvS36dzyhFn7G4OxxpoecBz8jOhxWAYsBgGRi9YpD-zcTqdmWx3gxfUb_VhTBStxio3yT6bCo2yOt6kGmSGayKddVj0KPHLr2UnEgomRmZtn_HsNpra4SNzdAV3f1GRTihtCovn3F4JMryrVDKnRhsAcwt-O9XOY5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ درصورتیکه سازمان نظام وظیفه پاسخ مثبت بدهد؛ علیرضا بیرانوند دروازه‌بان 34 ساله تیم ملی با عقد قراردادی تا پایان خدمت سربازی به تیم لیگ یکی نیرو زمینی تهران خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/persiana_Soccer/31511" target="_blank">📅 20:43 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31510">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c7f86dd8d.mp4?token=bAMPaiJT0HDQqkdeM6871djO3DIMvBcSVKPtkiaFoa0z8DWFOdPer18yWPEJ0xZhhsFn8dICKoqlVJ-YDUeJriCszp5GlBsoUlikbgIJGu5T85QTzq3z1N4yPaFAmU_HLZ--kEgBEVVKs12E7B7UDXqQZ508RKISCLhqLLd5FRKVETPbuCctAfatXrSmbh5D65wLNivupiKCkquMzyYcJ49aen-k1nHBR3boYfSqy1cTBHCZDBOq1h5haDU9r7KBCnvNlDqZ3vVO7ks2zU9NUvnQ82jr9A2FSff1It-96hiVzazAd6jfVRm7NmECELMI8IISofg96j0HrKNUqrhilw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c7f86dd8d.mp4?token=bAMPaiJT0HDQqkdeM6871djO3DIMvBcSVKPtkiaFoa0z8DWFOdPer18yWPEJ0xZhhsFn8dICKoqlVJ-YDUeJriCszp5GlBsoUlikbgIJGu5T85QTzq3z1N4yPaFAmU_HLZ--kEgBEVVKs12E7B7UDXqQZ508RKISCLhqLLd5FRKVETPbuCctAfatXrSmbh5D65wLNivupiKCkquMzyYcJ49aen-k1nHBR3boYfSqy1cTBHCZDBOq1h5haDU9r7KBCnvNlDqZ3vVO7ks2zU9NUvnQ82jr9A2FSff1It-96hiVzazAd6jfVRm7NmECELMI8IISofg96j0HrKNUqrhilw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مجری‌شبکه‌رسمی‌باشگاه گالاتاسرای ترکیه هستند که گفته‌امشب گالا نوارپیروزی‌های این فصل بارسلوناِ هانسی فلیک رو پاره خواهد کرد و پیروز خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/31510" target="_blank">📅 20:18 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31509">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n5tziIzlaMn-K0PZCM-Hg9Ek_708IpUve4hbJbestD7NbJQI0CsbKng-tSK38Cym-lKR9gCE1ztNl47HqyOCkYXp67fK9gAxG-vAKcVLmXgB5dANna_2O3PaqM4N4jw319XzxmnJ24dFolSHhdCWmvdGVETY176VmQ-cH0L39cRXAbjgYLzkw7X7dpAhP9feKVzw7mjrB21nJsZYIbEYqxQPbsywLoDpfLeEcVALTJcKxjjNMQOliBShWs0gTIsh2UsZrQRX3F9TBxt-qTQvZ9gi31zESrvUA7aSza3HhTfR9IibbmM4qKp43YyAE4ddvOGtvtdgwhcQlOt6iyLPVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
از نگاه بیشتر بنگاه‌های شرط‌بندی؛ لامین یامال فوق‌ستاره‌اسپانیایی بارسلونا بالاتر از هری کین و لئو مسی بیشترین شانس گرفتن توپ طلا رو داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/31509" target="_blank">📅 19:56 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31508">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🟡
🟢
مهدی رجب ‌زاده نیومده اولین شکست فصل پیروز قربانی رورقم‌زد؛ محمدخلیفه هرتوپی اومد رو خورد؛ درخشش فوق العاده یادگاری رستمی که پایه گذار هر دو گل فجرسپاسی به آلومینیوم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/31508" target="_blank">📅 19:21 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31507">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">📊
جدول‌ آنلاین‌لیگ‌برتر درپایان دیدار معوقه دوتیم سپاهان
🆚
ذوب؛ فردا در صورت پیروزی پرسپولیس مقابل خیبر خرم‌آباد؛ سرخ‌ها صدرنشین خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/31507" target="_blank">📅 19:02 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31506">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfxJSbDarNz_7XysuF-KHWInE38A-nrj5iXXsai9nA4u8_3dWjvZMvNiZq8LuDFtp6bn5ApDMGqsJmzHm57GzM9kvNgvIBuH-H1Mf1dagt0L2QgQczKcF1mjmwJrUh7d0ZThDhNF-la6mfbn_sfcGywJRWhs57eSykjy0kg5apl8ylMEiA8nWw7hmw7i0E3pv8Rq7sy2QdKlDXp6ArigZ4YiQFb_ZNvfeoGSamqv81cjXP5vMSAPCSM3MPphzc2RfthapWszqavROtQ6OJKjemZLHp67NG0KlMjGBGySMW3jtJK_Hl-ENsoK2korxi3xxT7MSxU5sdTe4H-Gr9uqQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ یاسر آسانی با گلزنی به الغرافه به آمار ۱۱ گل زده در ۱۲ بازی لیگ نخبگان رسید. او حالا بالاتر ازفیرمینو ۱۰ گله و به تنهایی دررده‌سوم بهترین گلزنان‌لیگ‌نخبگان‌قرار داره. ریاض‌محرز با ۱۳ و سالم الدوساری با ۱۲ گل زده بالاتر از آسانی قرار دارند.
⚪️
…</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/31506" target="_blank">📅 18:43 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31505">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nkHRd8NUicoq1nAs2NGVyWfl-matYHVuHze8V2bWhMSy38IPg7F85lk9ZmdonCwrXJ4Z7GPQTYCoaIuh6guK_jIZbQOUJmL4oaR8TQ78sDw-TNF2k9oWolxSJiBYVuNGRBX10dgQ6qzne9l_faEjKIjxNaXnX5NYsv2IrkV-k-WdjVt3XTeC23-BLJgQpcwKE7Y5LnCwTj6pcVN74B6IAR6NqSQz5C22HjLVnSJA-sWtM9E4OZe21WXY17S3CG_0Gp5OUeu1dAuBXHdTKO6F9KEBCaH_YtYR5dJaIL_YD1RO9rLzQ94cFOWvoDoDKYXlq15J1XIOD3MQsOnUBM0-_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
در شب برد دو بر یک سپاهان مقابل ذوب آهن در شهرآورد اصفهان؛ سیدحسین‌حسینی بازهم نتوانست برای طلایی‌پوشان‌ موفق به کلین‌شیت شود‌. سپاهانِ محرم نوید کیا شیرین با این پیروزی شانزده امتیازی شد و در رتبه چهارم جدول رده بندی قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/31505" target="_blank">📅 18:19 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31504">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🟢
🟡
گل‌اول‌ودوم سپاهان به ذوب آهن در نیمه اول دیدار امروز دوتیم‌توسط مهدی لطفی و کاوه رضایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/31504" target="_blank">📅 18:04 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31502">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NW0BissLdM47ehMJwo20YLFUD9VYx9I7g9w9s3Q7GPrd2O--qaFdLsPkUJsIkQPQ5nPtJnRbQNUNlyUeF_Axhm6QDOTjj4q-Si_xXWM7TC_vgU7B-4HGTqXPP6xBpn_LQAA_ysKjqlZSuXxwgNOi0fYaDqp5nVK8V2W0E3TmUD0cjlpd95sF79KbS0x2Xcw4nWSmnO-lxmGiAJ37y-i99vGppgnb3Xw2P150zVa0ebYRer8fEHTFxQhgJ2KcfYkOOOwueKhT0l9sbjjlq-30wEcqmI_rFY4Cb72YeYFFseam9aMoK_t5nKnGvLX1axhCYJXBCp851yabaepjFIoCDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مجری‌شبکه‌رسمی‌باشگاه گالاتاسرای ترکیه هستند که گفته‌امشب گالا نوارپیروزی‌های این فصل بارسلوناِ هانسی فلیک رو پاره خواهد کرد و پیروز خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/31502" target="_blank">📅 17:47 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31501">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5NBCQqBwU_txYpWY9y9-yq0zPQPgKfdyhzbCqDxibYpBGrv8jYxnkLkFgxZSMtr7YcxrpnflCsKRXBuV5PJ3BnqKiMap0G8fcmOg9qN9bNzN6qQo6vNRyHEOn_RDCvwV8MfdjWrJdtXLJilxQCZTjlR5hC_2U3NUiY5GZ3P8Dy8o1eMrC5-nppkLpXTF1tO4BSFZG5plpDHNCQnhq7m93hbbXZPRuxR9mfzYvjQVoufRvX4PwO094nTE1m6zVieBP4AKttuqaglyuX3XpnzwbcL3rpTaIWbH2i7oxNXSe4QwGN6Hlgxck2ClcyenMgwo6PUCupWvRbXV3XQu7Ei4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عملکرد استقلالِ سهراب بختیاری زاده مقابل سه‌تیم‌مطرح قطری: 3 مسابقه، 3 پیروزی، 7 گل زده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/31501" target="_blank">📅 17:27 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31500">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6451b4b3f5.mp4?token=mcbd9_I8bLwYhals3Uf5qCX1WkWU9uIsZmeeTz7htLhDKDGVfADVFE99f7KHc9HkjbiftJyamypeiOibpShca0BdkWznLCymx6MmCjBHOtsPwJvz2dEjDx6PAZdChCqk_J4DkXbFtuDV5L3x4RMxPlM8LNt6oYZRW4TgdrcgadHMF0H7JdncI-xADor-alr18KDU-P4RtWnBM_NFSOiMPIsCNljRmFl8OpLZbEBLUHzLJgRMEE602YkREJlsl6h9c1RbN8nvHClUzVMXd-b7uWuyVBYyNoHVEgka6VE7-sa6s39fMM5h9ywrwSA8_fYeRn9A0uRZ5TPS9lmuecXhPxYXVn41l0ynE559Yc8SLcLyGDP8Zo0G-ccyrC08btatGBrgmdyWW99dMud73ipRx3Z80o6FvqiENuUvXFyrZCF5A3ThVE6A4oufe6cGu7ge9Fi-ZCn73mG8ddxMnD1jcxh24VCYJt4q0pJutvK1976rfZYZsGXrQBOBmzOWiiZBlxFfe3yLsJM1HtYIM27vBJDADs_Dtwfpe4NapyYATF9jj8USA1Agbomazkg-WoQqCyhY7hbMazR4Ym2ogc97bqF6RsXEP7xck_asiHOWp-JU1vSV6poKWgfjG8X2irK1M5fC-xBExs-bImNeGs4Auvs32Ees1k4V0qWDQ3aah50" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6451b4b3f5.mp4?token=mcbd9_I8bLwYhals3Uf5qCX1WkWU9uIsZmeeTz7htLhDKDGVfADVFE99f7KHc9HkjbiftJyamypeiOibpShca0BdkWznLCymx6MmCjBHOtsPwJvz2dEjDx6PAZdChCqk_J4DkXbFtuDV5L3x4RMxPlM8LNt6oYZRW4TgdrcgadHMF0H7JdncI-xADor-alr18KDU-P4RtWnBM_NFSOiMPIsCNljRmFl8OpLZbEBLUHzLJgRMEE602YkREJlsl6h9c1RbN8nvHClUzVMXd-b7uWuyVBYyNoHVEgka6VE7-sa6s39fMM5h9ywrwSA8_fYeRn9A0uRZ5TPS9lmuecXhPxYXVn41l0ynE559Yc8SLcLyGDP8Zo0G-ccyrC08btatGBrgmdyWW99dMud73ipRx3Z80o6FvqiENuUvXFyrZCF5A3ThVE6A4oufe6cGu7ge9Fi-ZCn73mG8ddxMnD1jcxh24VCYJt4q0pJutvK1976rfZYZsGXrQBOBmzOWiiZBlxFfe3yLsJM1HtYIM27vBJDADs_Dtwfpe4NapyYATF9jj8USA1Agbomazkg-WoQqCyhY7hbMazR4Ym2ogc97bqF6RsXEP7xck_asiHOWp-JU1vSV6poKWgfjG8X2irK1M5fC-xBExs-bImNeGs4Auvs32Ees1k4V0qWDQ3aah50" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
عملکرد ستاره‌ایرانی جوهور دارالتعظیم؛ شهاب زاهدی از ابتدای فصل تاکنون در پنج بازی سوپر لیگ هفت گل و در دو حضور تعویضی در جام حذفی نیز سه گل زده تا با 10 گل بهترین گلزن این تیم باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/31500" target="_blank">📅 17:09 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31499">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WfgZTKuocH0WIqG2gGbyKIthXjiGlVi8wL8bR6FhH5hBQU78Q7oqgfTxU4q8Z_uF4lYLH8b9tdOMBt52N5HBGn1lXOAhPTr6znGV6SdKo2eHch1vsv5cLbO468ygZCLBfQpM86VSUFGQ4nj4d53NObWiwEgjRlreXh9cYS8-pO_SVdB45xZapFo0JZlQwN14uftEeDcT29S-z62Oj3WFeHnCxEkBiRZcDGbwE6-qEf67sjDk3-Ur75SR1gfE1Z9qn5z-ysFDgvHCunjli0pdcaxeur1x_33jjLBoleuSIJgm670QZTc8OqjnGh7TGUbS8DiHCxwgXNpe6_mkO7qLZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
شماتیک‌ترکیب‌بارسلونا دربازی سال 2022 با گالاتاسرای ترکیه در لیگ قهرمانان اروپا که آبی اناری ها موفق شدند اون مسابقه رو دو بر یک ببرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/31499" target="_blank">📅 17:09 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31498">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">بانک تحصیلات ،بانک  مشاوره اخذ مدارک دانشگاهی. واحدهای معتبر ایران. کارشناسی، کارشناسی ارشد، دکترا.‌ پزشکی عمومی،داروسازی،دندانپزشکی
پیراپزشکی. با استعلام.
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
Telegram :
👇
👇
👇
👇
@banketahsilat
⬇️
⬇️
⬇️
⬇️
⬇️
جهت ارتباط با ادمین
@tahsilat_azad
@tahsilat_azad</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/31498" target="_blank">📅 17:09 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31497">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ht_6AQGXtGbIBUzpbr3YlBA9aDid_8wcxNNELPBs7Aa8tgsJrNk-hCurf5zIcBmzRRkAgHo7T5Sk0QaVeb5Yai1zuIJlaDEBCw3V-Q5GJ4RPfH4wHLV13-Dxz48aIgEaU-_Algy_0e7Coxqh-Gf1eOqRTscTbn2dz-A_-_FWv3Oj_gTXISaH4ePjm8tn5CCOhBlIXaKGEHiTkLIoWSPKhr8l7P02xb-nav6eMJKyM7T5mBXmAuTMn1hzhfR0eZe9NvgDjQrCCHAf_sIeBN00f0AfhrdK8Nqrw4U_-VqWg1DrLxPDH5uVz664Pse5QE5BmxVAjWcqdxNlDf1ZcmVY0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیدارفرداپرسپولیس
🆚
خیبر؛
ششمین تقابل دو تیم‌است. در ۵ دیدار قبلی خیبر سه برد و پرسپولیس دو پیروزی کسب‌کرده.تقابل‌های پرسپولیس و خیبر ۱۳ گل داشته که سهم پرسپولیس شش گل و خیبر هفت گل بثمر رسانده. اسماعیل بابایی، ایگور سرگیف، علی علیپور،اورونوف و عیسی‌مرادی گلزنان تقابل‌های این دو تیم بودند که در دیدار فردا هم حضور دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/31497" target="_blank">📅 16:50 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31496">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0e5fab635.mp4?token=r9fLs98A_KgBL1vz8qPbtk-YCt9ac94fhb6-628v9JxcMBGMxfsvtGDqpzjwv2fQ3KDRIe9Ao_I5FdzFXhOcTREPaHuxYrDFJzj3P6YWFGoYye7Qni2jt0p1-t_hTpzLZptNskpDdpHEI5BCUwuA86gikO49Xz6A63yUyphE47320cFkWHysSMh1Mkyu8GhQOBF8gFPYNxggDmBUZUMn6VH9FWz9RH781R_Dh2eAiGAqjsD1CAfi-h1_SzN7fP_pi6my_1_vy-6ZFa9k_UNRS3oKLrFdZh37ctufl4yA_0_sdUMJy82o9ecFqbTXJlaqP25I3jZ4cnfsp7AA_SxGTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0e5fab635.mp4?token=r9fLs98A_KgBL1vz8qPbtk-YCt9ac94fhb6-628v9JxcMBGMxfsvtGDqpzjwv2fQ3KDRIe9Ao_I5FdzFXhOcTREPaHuxYrDFJzj3P6YWFGoYye7Qni2jt0p1-t_hTpzLZptNskpDdpHEI5BCUwuA86gikO49Xz6A63yUyphE47320cFkWHysSMh1Mkyu8GhQOBF8gFPYNxggDmBUZUMn6VH9FWz9RH781R_Dh2eAiGAqjsD1CAfi-h1_SzN7fP_pi6my_1_vy-6ZFa9k_UNRS3oKLrFdZh37ctufl4yA_0_sdUMJy82o9ecFqbTXJlaqP25I3jZ4cnfsp7AA_SxGTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
معوقه هفته هفتم لیگ برتر؛ ترکیب سپاهان برای دیدار مقابل ذوب اهن؛ ساعت 16 از شبکه ورزش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/31496" target="_blank">📅 16:44 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31495">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSeMs_Mawl9Mr5gey_IG4wivpFVvfuRu6MN26PaQsCP6R13gF9SBuD9CuVUH8wvp0ExbXxcEGE_OOK0D_uJgFL5Kfossadc9lcEEfMpcm4UBtqWUpdaFFVwuaCMGPRQRVoWIAns4tV6OOFuEeWJXWROlNKqVuA3Bn4cQeK4hU2KkQDoGqX0RKkhCfK0ALFsp1FXxnwLKKgWVf6CzYT76i5JDUaWkF4eaItUaW0Yede5dv5-3k2jz3LBGPuE5ZPMOkIhudFvPINn5mk1AP3C99kohn2dsLGTPYZufvFTshLmwdFtPHnAJhOVgIZiIk7AMYS-dtkBkpNvD1sTEQTCd1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدشد؛ یاسین جرجانی مدافع‌جوان فصل قبل آلومینیوم با قرار دادی سه ساله به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/31495" target="_blank">📅 15:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31494">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KP-00K8cnB2psuOSFbw_DRfGn6Ka69sCesmRVIKskyoFzVyC2V2Xs63AyJsG8BEc4KFBxxX7Ke-fcI-ox-GDR0ggHl9lHWzxW8GdoKQUCIsnZ2lOL8hIIYcSBgUOV54DA-cK5t2q5X2In6yJtr7lIcCnHL2QHBPhYcaM5kGH7svWwwwtJaMqJciHSa7xeiXVhheaycDDJC_F8zTBQ9bU1cAI-Fh-vj2VIdwgyEk9jFd0__0nMdKFlsPADfcU2QbyuSnCIv87w1iqJHESyG1nabt8rdiM-D8VhjO47b_zyAP9weoRJSszZLAv4q2GoQhB6jumUKnlwwl-e5iq1U2GzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
دانیال ایری و حسین کنعانی‌زادگان دو مدافع میانی پرسپولیس به دلیل مصدومیت دیدار روز چهار شنبه مقابل تیم خیبر خرم آباد رو نیز از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/31494" target="_blank">📅 15:30 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31493">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iRTiEJ35JEBcsj8MUqMrB7vQ3SThqZC9R7qPloEbZn3zcWVhXrXaIC1Y8-RLLWf8dYQ8_5QDq7M-X_gQiwbpEQiYl7e7hnPcwwc9ECvuyVeuFvo0LsDI0t9Ns94ICXR8sSKWAfcOr32e6_vqhfph9Qwb_yWlnkzfyTWLwL-SpiojzBLftX31b8sKr8BCDN7gnNbximKQMNTymlLPl9-FK3iAVO2Bh_js6PvCoQ_Tk5ufTV5YRmDSsCN1yBZboNg4Sw0KFCaAiDDfXE9BzapZ7QKoZWDfpc3SV1YxFPTr508U6uy9aec0penKyhvotW8JfgjOUVx41nGRAxl-tFeKLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ معوقه‌هفته‌هفتم رقابت‌های لیگ برتر که قراره امروز و فردا برگزار بشه. درصورت برد پرسپولیس در بازی فردا سرخ‌ها صدرنشین میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/31493" target="_blank">📅 15:16 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31492">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8XailJz17Kn1tcIoeZ1Lkgel1CXWodhdM7n_VJCxaVDt2nHpDc0NcfODwhCC_eWPQQVUSNi1bA7rIuJFEtp6HfrDEkLRuToQu_SZqkbhKq2pfcyHX7NZ_NOvrLr_7YeCXwxzqGK_VHs04jncDmB_6TOjopnB52JCbYCPgAX2JjVMCuUvne6HWxjUQ3ZQktU0Lg4TUY_hwa0ejI6PgAay64Nv-7SCepHUgjCmRG0evDPpHvPJtiyERfBJMZVFk87zRcIQWCscSCswmWOYM_EnJma7UqlMbCl_bH7BLi0qHGGjK6mffn_Vw8n1PzMIUuq57t1IW3wzUCP7AYV8uRvRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پیش بینی جالب بازی‌های امشب هفته دوم لیگ قهرمانان اروپا؛ ببینیم‌چندتاش‌درست‌از آب در میاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/31492" target="_blank">📅 14:50 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31491">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UmDA6G0DiNYIj7ODdPeeKwmOZs-pU1kPF1S5J-qyKYHmm72QaD3NNtZdYfzvKKroQR7ch4QzdZwo1DKFL4QKCaEYKty-h35m3Noi4IIFEcnZn7pursDG58l7puQADK8QUqGEHsJkwTkjONkGgF_wH4CwvakMEUOZESwMUB84s2N562_uxTZ1iZv2bjpMjsKE3Q1m8t1y5cJulr3VwBvK7TC_cnByeCSzZe72Cb8tMby15GyJGNHjOg1BkyZbAFRBBxR0nB9oTRaDA3MJIoVYbRFjPl3xoegtsij_eAQYtf73W8tSflJo6j_hPMPTp5PyBPeYLWuxWahdbGM0pQJDCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عادت بدش روترک‌نکرد! جواد نکونام سرمربی تراکتور: شرایط به‌گونه‌ای‌است که همه چیز به سود الشمال است. چالش امروز ما مقابل الشمال شرایط خیلی سختی است که برای ما به وجود آورده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/31491" target="_blank">📅 14:15 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31490">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fo3NW1zAU6SIAIrbJ3ZdQk7L0iNcy8rVV-5EkedDEOlptihPeGK_PwLSRPv0e9JJvn1FV4e4LxwyCWlKUMQLeVtZWVa1VwWW7I18YUkYoIz4uUrv1yAv1zd0rG60PNn5jmhaWeFYbcQg9SHX-KxOfoNsQH6uK884UuY8gcVta7XQmA9l1rd7MAI4ptyoydGhzQfUjDYlM_bjUcjfxDeWAnLSKKOJzmhImnwW4Rc_St7TSbZIhDeMEbwUCeWdaNS-6-Hg9b7hA_Fn1MIXdzJbIcnS6UVJqPhSLBCDXa5pV7KnzXQvmI2s4w9cqodL24p2PRq03uYx6NsAZDf84vD5pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تغییر زمان چند دیدار هفته نهم و دهم؛ استقلال و گل گهر بجای یکشنبه روز دوشنبه بازی خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/31490" target="_blank">📅 13:50 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31489">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GYkp8wy57oA_ON3oOEyTCExLKC4Un7teB-ZNrUv1Yph2QSmtaVJRTSjPft9veFD0pNbAtEdl3azNXmyv2G0JPC-Qui-moBFof4xIYFTkCv7cHtqC3PHvKM2L2qHWBUQYV4h9Oi1Hb2HAinF1rDMA2yDdqC0tKaXzYlTllhR6wLWsFa7dZ0MAsw7vdtDGRxtcdCKJ3AfhFYcdEn6xPUXjtxpF1gFgnlNMVBTM2Cs5Uu9TA-T3y_gZNimVQczAfnkZCj8WvlbceLbDS5P4OV5cYi6QUZEzTFzLTmlDWQ7dOxQcWIRssPXe1m_2kulwYuimql6wl3WJkTVL4Aw3ktNt4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛سخنگوی‌نظام‌وظیفه: باتوجه به کسری‌ هایی که علیرضابیرانوندبخاطرمتاهلی و داشتن‌فرزند خورده سربازی او تیرماه سال آینده به پایان میرسد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/31489" target="_blank">📅 13:29 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31488">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YNdfOjKYituLo6ClcVYJMY0n782my03A7lO3Cby8KPcizTp-B6dN90iuG_omJ4jjjonn0qhcjVF_5MhFhrdPiEOh_4O4zRKmmBhBzCAIacZ4n7UNwaXOZYQYwWpl7Hr5yk4hfImpf-ZZLzjT5iiZ6-RZDP9wY2dIe3sje6l3_hk6U4aELtRxDxzwg94iYdWZQvGwyXpxbL5kj6ov4oocXLn9o_u4H9uT_wxiFGPIirekdccFeFrTHuGTjditcZvVOduhjji6QJKnpLvICKkkP9Z9ldlJwcnm5bYddO8_eTSQU_0KYBSLeATLI-lV_nKZSl1Q8uwGWuV9mvMiRrwyxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
درهفته‌پنجم‌رقابت‌های‌بوندسلیگا؛ شاگردان نیکو کواچ در دورتموند درحالیکه تا دقیقه 85 دو بر صفر از وردربرمن جلو بود در عرض تنها هفت دقیقه دو گل دریافت کرد و 3 امتیاز شیرین پرید. زنبورها در چهار بازی اخیر خود به پیروزی رسیده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/31488" target="_blank">📅 12:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31487">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HnIJ7CMQYG5fWsk8wb1e8R3KIsvRsxW-GNbQBDRrd6rxLlN9jXfjtFeDEDNs8KsCjtBGf8bwrgarLZZQWFvLo0g0jwZg4df1YLxT6e1Sp5cKwLTznFUdslVZ1DyaXnVBOzaYMUJkhni8YaMf-tQUAp1XhxJ0XH0LF-yr7Y9ELxjPxJgASVL42qQH2xGmFf5HS9fE7OcRB2quCzxzMkV4vA--AxktxPzkiF4Uk-HHH-KVR3qDzUqLqknv_1feIgOY_LYBqQFGOhsOA7f7Tfh_AxV2M_sNr3EUNPaAYHz8CmeCYyfD5qwNR0EZPKTdFTmPPcwoyGrvzc9edAlsYGj9mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اکثر مسابقات لیگ برتر مصر رو ایشون گزارش میکنه و برای هرمسابقه 5 هزار دلار دریافت میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/31487" target="_blank">📅 12:45 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31486">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O7lUxaOXpMtT_Un95Io9xncQ4Rk_C5FAoZ0Xlm7P2SFcn3RdpkaAIzyVau-xFXDJC1iiGFAeqBv2iIAvlGNYNfy7gfYSlx8ZFTA-bMYOcdxrU9Kfp0khAVPE2rnQp5ZqJddfk2w-sdIyUAVDJjT9G72iMCRBdo9UMTz_LSwfRd7_lX5BzTNtOF_TOGn7iHfOCTGNFDw_u-1IFYEw5VPsrXXq0CCtZGKBI_12oKg9hWCR1qt3DyYSF4JxX25UkPIv5GZ9M1e9gYskny5cQPWSYwz2As0BhETOIQDY3QvHGpJjjWVN0KB-UVTBTN7AYiVgvLyJd6tCAiRSeBwZlSZRVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مسیرسفر گلگهر از سیرجان تا بحرین را مشاهده میکنید. پرواز از سیرجان به تهران، از تهران به نجف، از نجف به بغداد با اتوبوس، از بغداد به مسقط عمان، از عمان به منامه. به همین دلیل خواستار به تعویق افتادن دیدار با استقلال شدند که مخالفت شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/31486" target="_blank">📅 12:28 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31485">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71e001dfa4.mp4?token=nop_MHysKAOu8stozIMRpC87Dv8ZPj2EDO7CinPkLMdRAyG7TwzcDdhTFqtd9zhWFJNwigZC-44zjGQQKjhoMfdDzLq52YtkX3RzzmcelukbmVrqJ_57W2ya3_jeiIYlLyHXUoJOTRRUNsm_UIczWnvjKfSgah1BnawdVf16jdRKlKwFJLoaZps0GqGb-H4ylVetMwZyQk99k2ZSc-SyNpsh7RtKGejKpo8R2tTse_GnbsXCp5qHBRYTT7JiNWzp4_jlDT4Qx8SuacU05PAgMsvhJA33PNDas8kB3GQczli3mmkYlDBNuQpAkvRsEZTPfvKQsAVuxpvwynTfMXyXo3jHxrA8jMiQjLzxzTyxL13He7kmRLuMd4Kcg8tyT61UWRwm2eCEu63igj0q7-3s-CtvLLL9siuNjkjMbXbbJYS6NjmPsqo-N8RxqLHNf59lPLy7lg3V5bSQdN4sbGuzex1fuX3FHqpsOip9Zda7wQHALGYYd_mGm3BmgZczPzQPuNCwX-08qbj4UT6SW5Q8LcP9hTnEI77Q4ntIcGFVO3u0ws-JNnhP1PEY9J9ARCoI9cozsf5ZMWjpEZDahAxOyU9ouAaMdqdQJZi-EO0ztiVpgh0lSTu91A9-SsMJIsNVNIrfMjCpDLNNLx9Spx2cLFLuj_zzVDXmqI--s2NcPsM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71e001dfa4.mp4?token=nop_MHysKAOu8stozIMRpC87Dv8ZPj2EDO7CinPkLMdRAyG7TwzcDdhTFqtd9zhWFJNwigZC-44zjGQQKjhoMfdDzLq52YtkX3RzzmcelukbmVrqJ_57W2ya3_jeiIYlLyHXUoJOTRRUNsm_UIczWnvjKfSgah1BnawdVf16jdRKlKwFJLoaZps0GqGb-H4ylVetMwZyQk99k2ZSc-SyNpsh7RtKGejKpo8R2tTse_GnbsXCp5qHBRYTT7JiNWzp4_jlDT4Qx8SuacU05PAgMsvhJA33PNDas8kB3GQczli3mmkYlDBNuQpAkvRsEZTPfvKQsAVuxpvwynTfMXyXo3jHxrA8jMiQjLzxzTyxL13He7kmRLuMd4Kcg8tyT61UWRwm2eCEu63igj0q7-3s-CtvLLL9siuNjkjMbXbbJYS6NjmPsqo-N8RxqLHNf59lPLy7lg3V5bSQdN4sbGuzex1fuX3FHqpsOip9Zda7wQHALGYYd_mGm3BmgZczPzQPuNCwX-08qbj4UT6SW5Q8LcP9hTnEI77Q4ntIcGFVO3u0ws-JNnhP1PEY9J9ARCoI9cozsf5ZMWjpEZDahAxOyU9ouAaMdqdQJZi-EO0ztiVpgh0lSTu91A9-SsMJIsNVNIrfMjCpDLNNLx9Spx2cLFLuj_zzVDXmqI--s2NcPsM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیش بینی جالب بازی‌های امشب هفته دوم لیگ قهرمانان اروپا؛ ببینیم‌چندتاش‌درست‌از آب در میاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/31485" target="_blank">📅 12:26 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31484">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I3JuXZ6NgH_CK4f1-0Ja4q6uaHPlbKQt5BJO93comMqkvflDHUfTp5-s9XvyXBi7ERhdZpWwsPBWjQdwth8_IuknJsHX3ViZxDw92_ihhxzaNhHfiudnrTtnwSXAz4k3WCLlsTyk3vTKEBY16GV1FzJoWn9sNrPM1-987u-mBzNTU7EyGvgvqm4HZ4XKQdZs1oFSDa5z4QZq5rXVe753BnPueJVuv4zmWC1fQ6J9LwOO2cTDBIqOpkbPrI0y50h5R9qneIKYQFbgpMdcTbPjxgYU54z9VEVUGttEJKXR9EEhMX8audXQD6aiYfyoMucT_9l47iLq__hkKSWqFT2-aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
با اعلام رومانو؛ دنی کارواخال مدافع راست رئال مادرید با قراردادی یک ساله به ختافه پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/31484" target="_blank">📅 11:56 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31483">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RksepAnSDg5I64l1LT3m6OR-6PZl49mAjNQwQP75PrXUZ-NDk2Cy3U_Es9xexEqtaWj-GQUzkuhTTF1hEwtHpivtxcg-P2vNYnxF0Oqz1z7Z3B6m0ajU9X4KUZkS6D66UeovZsV_ArwsNAw9ZQkqRyUU2VBRvXP6PpU4q5MRKZCRNy_uOuk29NeLCnKwcxzmfkDN9oVkg_7E1RjfLy8EH66GdiSlHBpRbgLhKKcVPARBW8CIZJSf_lYKFv9zfSoX1YPIsO33rV0IbcHYc_P_LdaQzs2MMkwyklCBDrvYmS8ra9M20usFYekokuQqmBL3Lk4Haz6We-xhbVGJrx66zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حمایت‌تمام‌قد کریس‌رونالدو از کشور عربستان در جنگ با حوثی‌های یمن: جنگ هم شود از اینجا نمیرم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/31483" target="_blank">📅 11:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31482">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tCsImGHvmJvaXvh3mrNAyq7z7ou9vfrZztFWTRzVrjSboKdwABh04P7V1pS6sBxai0CDdEF0zxM1XEJ614sJYPWHGfqKIswEQcq0tgtEh3aC-hiHtPM7cs7iIzhIdkx5J7COlLGIaHDb3BnaScrv8PJKEE3GseIMQMo9LBvID_tTLF1xkMP5lq_Gxpyt3JYBBRAHprIQdaZz-k100JwIN8Ne52tpzoRdQi4ngyUTQ2nd3h3yTjBcPJ0_yvGHEDXjuVwJgovhCiOIJBL-lkEj08iw2yYJ4q-K8a3NdzoMfVV8i3YCde5wudOcMTl3kN1SYQ78io_q_fTitFmmCK9c-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بوسه کریس‌رونالدو روشمشیر و درخت نخل نماد عربستان سعودی و ناراحتیش از جنگ تو عربستان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/31482" target="_blank">📅 10:52 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31481">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/boR49ptuGpLStuJgLQxrV3-T4YkLdLnOEtm1OiCG9sjooMnfENY_H_mPplMsaQ1QI4Y36fP-BUB6HDgX9vkAkkvB04IZ5vfLUMTxoQuvvVFG3sn4uONbPm-ejbvM9TMEDQDbdaIqksZf8QlZvowc1bFbRZ6PCg9Ytu2gwXNn6ZESeMWgFKwwCIOMmpv-g9kOet1z54LAbZeL8tzyy_s-X4us3L3l-KIJojc3Otv4AYDhu_xlkWuGoFjIVuAMFJnhzxnPTdm-2dH7CW7otNsNeMs92b4PNc5KMhdOpvS6y8irDefX-L0kx3OrE3hLviTyerGEFAwV4KlmF-AssL1meQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
برنامه‌مسابقات‌این هفته رقابت‌های لیگ قهرمانان اروپا که قراره فرداشب و پس فرداشب برگزار بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/31481" target="_blank">📅 10:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31480">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-v5IZTxR7bKEXOE9w7phitqh2MUneXmU-Czlommj7XPqBYS6Z-LXoDbleYyaB0OCaQdt6Hkd1cGnUs9PuKm5lQB8Hy8d_G8OgICrlI3_J2Yi_z6plAH9TXjju5PmwzaOtRMtjVWXXTUnji9LIQ8Xl8S-s5fOpWvm4bPMgGXVn6RiR08uPW6A5XOmCvbiVGhP1D-sgXP35iCmU-_FfKCJuEtv-qXQpJI6ZWla2ka7a3zgpWGcNyjpRvsTwvNdz7fLFweZpS9Nhme9U3B6pyeI26rfBd2qyuy5ySnx65UkT4j_qEjP-6Z_cLWUZYM89DupQugIX8FJQubaKRBtW6vyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
👤
سعید الهویی دستیار و همه‌کاره کادر فنی امیرقلعه‌نویی رسما گفت که مهدی قایدی بخاطر اون مصاحبه‌اش باامیرحسین قیاسی خط‌خورده است!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/31480" target="_blank">📅 10:30 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31479">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NcTPSTiBEp_b6hvTNmS0L47skNQJvMXsVkD0DzM_hqW7dMqUXq1ECgEkhl1NNuux15sDdShhh0nm-ZNLW_a5YGmdmcwX28OW2jYCJuaOYYv7yPoPwdeTVS3FnTPmX98umVH4ur4cTlDFsZ0vcNcUekrvco8G0Ed-EWpEr4fIhdbIshEoEiQKd2vpmQJGGwJZuhcQe-iUYznkxIY9odWsRdbVxZFoHUl3evXZ32aqY4fNdXNdSdE2icEWRQwUm0TcryuK_fZOzoKn1ABb0F42rMH3kSCrFyYZgpNEeg4XggrTAcVcXj7w2nD8P9PAfYKdIl69zSzr_DPr7G75376EPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه دیدارهای هفته نهم و دهم رقابت های لیگ برتر که قراره از شنبه 25 مهرماه استارت بخوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/31479" target="_blank">📅 10:30 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31478">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrNcIHjNaNMIzxoZjRznDPfncBlHKmmAfXd8nYRpA9sLY9hg3cmOVojniTM6C8tlPLC5dbe8MoXnr3e-dCp2zZPw1DIVwg0UoNCk6qiCNIMK0clPAS_KAspOcN5gRHdf5BDRYAdysC-dvaJw4LyK4SEaUZYsH_67TTy5qWhdE0Meto7UnL5M0YIZMXLn2haWoSVDO9H1Zi82hD9f83Wa9ALbr_2Ia_M5bnlUyWEnR-SRZqA1Prpow_OkIysQYMqKpF9-PLokbJAvzfj3NLtNpcIJA4Ar2YGEJw8EAqTY2QUR5yfwCCPfAGebRtE7YIig9yktvt7Sz2mUKJT3WqkmxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
بری بت | BerryBet
🔥
مسابقات امروز
👍
⚽️
الغرافه  - استقلال
🌎
ساعت ۲۱:۴۵
⚽️
تراکتور  - الشمال
🌎
ساعت ۱۹:۳۰
﻿
💸
ضرایب ویژه و رقابتی
⚡
پیش‌بینی سریع، تسویه آسان و پخش زنده مسابقات
🎯
همین حالا شانس خودت رو امتحان کن و هیجان فوتبال رو چند برابر کن!
✅
۱۰٪ شارژ بیشتر برای روش‌های رمزارز
🤙
ورود سریع | شارژ آنی | پشتیبانی ۲۴ ساعت
کانال سایت:
✅
https://t.me/BerryBetOfficial
آدرس سایت:
🅰
r21
🔗
https://ikruyxysd.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/31478" target="_blank">📅 10:30 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31477">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b74c2dae8.mp4?token=Wg3boTd5_WvDbM44EOslSEKybhFFdULGY7YTsGTCVgGnGotHYQ_0CSkBycEi-8IxTZXIA8z2fclADkk1ifJtCtdqxzcb5pR5Y0NAq122JOED8RSGfVRE6pmVPGY4uXEADztP7ztGTa7VGOoWYVNCgirIRJG5xzTuFKR6VxUHbz1CMVWzUFDsT6JCaJFbbGWGkwiI2K6ye5PcDJQPoviDWwXr2JPRbZC8J9EG6NGdrz8alQSBbtdWjzmEMAkRyRdC8hbIQ3m7kUUQ4QLYNQgcZTJ6dJVwHZL1r8WSOJ3lsm5NxShdDsz1xfv01D7mCcRRapEbqe073jISwPwoiehHBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b74c2dae8.mp4?token=Wg3boTd5_WvDbM44EOslSEKybhFFdULGY7YTsGTCVgGnGotHYQ_0CSkBycEi-8IxTZXIA8z2fclADkk1ifJtCtdqxzcb5pR5Y0NAq122JOED8RSGfVRE6pmVPGY4uXEADztP7ztGTa7VGOoWYVNCgirIRJG5xzTuFKR6VxUHbz1CMVWzUFDsT6JCaJFbbGWGkwiI2K6ye5PcDJQPoviDWwXr2JPRbZC8J9EG6NGdrz8alQSBbtdWjzmEMAkRyRdC8hbIQ3m7kUUQ4QLYNQgcZTJ6dJVwHZL1r8WSOJ3lsm5NxShdDsz1xfv01D7mCcRRapEbqe073jISwPwoiehHBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دستور محمدرضا زنوزی مالک تراکتور به حجت کریمی: قرارداد علیرضا بیرانوند روفسخ کن. او دیگر به هیچ عنوان جایگاهی در تراکتور نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/31477" target="_blank">📅 09:53 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31476">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b7c8f6c96.mp4?token=bniY9BfVAzU0wXFOJ3HY39xydaAPLHPNwJQf78l83-yie7pTPmATymhQljhjBLx5lCda93AynVgq4WB-KeRB8HW3R_4ZAujrb1FRH9wcxB85ibfkxhpKFRl_x4dke1omBZqVjDr4HqcE-cWsTU-b6sJS0mrM0Id8sZzDPKFPEmh_FFGO0VLy8NcAzuBNC0vHGZg97vIdFZc3biHVeT4U1O9jHe1wS7yc1OxY3wOqovpdU6zkc24fM97Cxty4jN-SL30BTz6OMEpznX9FVM2LGQx6cdJpEaIOzl_n37iQQLB-nzJHiXv-8bE2F-WOOfm2NWK9_p71EXGcAloMDy4gsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7c8f6c96.mp4?token=bniY9BfVAzU0wXFOJ3HY39xydaAPLHPNwJQf78l83-yie7pTPmATymhQljhjBLx5lCda93AynVgq4WB-KeRB8HW3R_4ZAujrb1FRH9wcxB85ibfkxhpKFRl_x4dke1omBZqVjDr4HqcE-cWsTU-b6sJS0mrM0Id8sZzDPKFPEmh_FFGO0VLy8NcAzuBNC0vHGZg97vIdFZc3biHVeT4U1O9jHe1wS7yc1OxY3wOqovpdU6zkc24fM97Cxty4jN-SL30BTz6OMEpznX9FVM2LGQx6cdJpEaIOzl_n37iQQLB-nzJHiXv-8bE2F-WOOfm2NWK9_p71EXGcAloMDy4gsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
واکنش حامد لک به صحبت‌های بیرانوند علیه علی دایی: طوری می‌گوید در نوجوانی کارگری کرده که انگارهمه‌فوتبالیست‌های‌ایران در خانواده میلیاردر متولد شده‌اند. ببند دهنت رو بابا. حرف نزن تو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/31476" target="_blank">📅 09:40 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31475">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e5884a83c.mp4?token=ky9gOcL28ETwFgtFaSh_0vVpV87aUJc_HGv_TlWK7qUcxpF-pQtItZCQY02e8eqlFU0I0Q5UQnU7p0xhPVYCsoOFusEBnC2QWYxoZLEXpXwrdrgERFBby7I2RMkx_Oc0D8JQi-fRoSxdg9gmgvAS3KG895Qk1rYmneD8R9YLGBr_UKq-YA7DG14A87xyEmcH9mhDJ4sJKp3UEhkTHJxojsUonCvqi-8Tx9-L6G28Zw7_Q855TtbOrOVkVU77yTOHbLcKffeasf4s6fk7WSmuWDrHF_qzxKZS8L8pwAmRQ_yoEexyQvIOhCehDIGNxMGBcUXKJDAUio-mqQMSTKnlRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e5884a83c.mp4?token=ky9gOcL28ETwFgtFaSh_0vVpV87aUJc_HGv_TlWK7qUcxpF-pQtItZCQY02e8eqlFU0I0Q5UQnU7p0xhPVYCsoOFusEBnC2QWYxoZLEXpXwrdrgERFBby7I2RMkx_Oc0D8JQi-fRoSxdg9gmgvAS3KG895Qk1rYmneD8R9YLGBr_UKq-YA7DG14A87xyEmcH9mhDJ4sJKp3UEhkTHJxojsUonCvqi-8Tx9-L6G28Zw7_Q855TtbOrOVkVU77yTOHbLcKffeasf4s6fk7WSmuWDrHF_qzxKZS8L8pwAmRQ_yoEexyQvIOhCehDIGNxMGBcUXKJDAUio-mqQMSTKnlRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
گل‌دیدنی‌کریس‌رونالدو در بازی شب گذشته النصر مقابل نفتچی از زاویه‌ای متفاوت؛ CR7 بدون نگاه به دروازه حریف توپ رو وارد دروازه کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/31475" target="_blank">📅 09:27 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31474">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39e71f827d.mp4?token=Ib8UKInIw_Z_-RAkkKr7c2gn1_x44JeAeK4leF95m4XrQRzgHBjmpaFthMnTQJg698RM_IoVlCOhbEZivBOfma1D9Pw9J_cpKCqiDEdlZgcfxDDq7ryrugss8JuHtOxpBTbp7u5F6HR0rHDvSneV-GDXP3YdFDQTayB0aDwDIKczGspaSu4Tb4UhyIXsS4dUURAfO00T0_jtt2d0Ulw83IVasOuV_3hSyekAOyLGfoNds3VKTtOt27xeAgCLONwXF9l2gi0bbmQ_19U5-z_XZF46pJIT1JPr0rDahMHEywN-uBPQhiE-nClggY1prkYGL-_rwo9xxs8y-9Qzp6gFkja5E7aqwmugK1s7GyV6PqUulPcVqYEHjG75qWZNgHE9tPohG6YdqyoA9WBEQx1oEObITpYYptqRUibMyaXZeSpcAjTaBCW1d-ysdv7h7TukwIKEPi96T24x2SPCsN4aUaQ3KTyIL-_3X6bjOCnpzCGwQZndYvJkHNggPJamchwC1vA8JyfGwU30ArZoBbUonwTvx6RJY2OzGtvMbCdOCaNUWwN_w-W6u7fWY8eZWYuJhpxIZAaw5Kvvgj--opLVrEPdnmMQzJ0R_TPuoY566bvGvrxUVmK0QKl0OwZZE10svZ0fN2G_v9CEliLgo-gDkhx-cnN9cCC4jJjWGiyaep8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39e71f827d.mp4?token=Ib8UKInIw_Z_-RAkkKr7c2gn1_x44JeAeK4leF95m4XrQRzgHBjmpaFthMnTQJg698RM_IoVlCOhbEZivBOfma1D9Pw9J_cpKCqiDEdlZgcfxDDq7ryrugss8JuHtOxpBTbp7u5F6HR0rHDvSneV-GDXP3YdFDQTayB0aDwDIKczGspaSu4Tb4UhyIXsS4dUURAfO00T0_jtt2d0Ulw83IVasOuV_3hSyekAOyLGfoNds3VKTtOt27xeAgCLONwXF9l2gi0bbmQ_19U5-z_XZF46pJIT1JPr0rDahMHEywN-uBPQhiE-nClggY1prkYGL-_rwo9xxs8y-9Qzp6gFkja5E7aqwmugK1s7GyV6PqUulPcVqYEHjG75qWZNgHE9tPohG6YdqyoA9WBEQx1oEObITpYYptqRUibMyaXZeSpcAjTaBCW1d-ysdv7h7TukwIKEPi96T24x2SPCsN4aUaQ3KTyIL-_3X6bjOCnpzCGwQZndYvJkHNggPJamchwC1vA8JyfGwU30ArZoBbUonwTvx6RJY2OzGtvMbCdOCaNUWwN_w-W6u7fWY8eZWYuJhpxIZAaw5Kvvgj--opLVrEPdnmMQzJ0R_TPuoY566bvGvrxUVmK0QKl0OwZZE10svZ0fN2G_v9CEliLgo-gDkhx-cnN9cCC4jJjWGiyaep8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔵
👤
با اعلام مدیر رسانه‌ای باشگاه استقلال؛ مصدومیت یاسرآسانی‌جدی‌نیست و او به دیدار هفته آینده با گلگهر سیرجان در هفته نهم لیگ برتر میرسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/31474" target="_blank">📅 02:06 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31472">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KoidMkF4J5mUWij0uMyf_aU4gwB9I1qU3pOUXUS6bpHuYwgIu8dnzPra--k9k84wiwzi-sN9vq910CfaLU_Kg3TXhBC_PeCC0ZSos9fo1sjoC8ZIzu3RYb7EdpnU38WNPxLOEUsx_0tMQtehFnhYtuIpqD-I7JXdcySbuSrB8ewH8s41u-fJPyoOpeR1NZ65Q0_9AaHPJG21tcG_5czsWgvojmoMyrQ5tidDq7w89fG5XnJ-6XL33XHeYL_-TByxIGTAG71jfy2ZGQbbUUrKLCCz6ewCYwPpxF0BKFdCGT0oRJW5S5VaBb7SxKfA_M2MflfO-h0yJB9MgCzy53_c8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لیگ نخبگان آسیا؛ دومین پیروزی پیاپی شاگردان بختیای زاده در شب درخشش یاسر آسانی؛ آبی‌ها با پنجره بسته در صدر لیگ نخبگان.
🔸
الغرافه قطر
1️⃣
-
2️⃣
استقلال ایران
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/31472" target="_blank">📅 01:15 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31470">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MNQnf8pzbz7cvt8tMpbCiXfBpigYqJ77FWHmqM6Pndun5RrNNmhiklNpJ6jFpNBLYikwcKzuWxaoFygymMmPHXut9TsXjZZeeDVJFQBvK4_hKGntHD28YRW2TyI1t4kkauT8OaPXM-XyJ3j10DMvjNgQiSyJ-teie5qN9CABQLNBURDjoEfR5gmyMWCgJj1OsTHnxaO9oG86DzmSLQaBd7mRFb6cmt6gti1wVPAX-OWjkO82S6RSOlibBDiuvFO9-GH4OUcYT-w4PyWJ_xmzJcQcbmGgedviDbu5p51Z6YiSP3cdMhbDXU3JRsoYXaOsSufvktVYrHajbmOg3RAt5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌امروز
؛ از دوئل تماشایی شیاطین سرخ با شاگردان سیمئونه تا نبرد بارسا و گالاتاسرای‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/31470" target="_blank">📅 01:12 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31469">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_DAPqnsTkIQHZ8Nk5ynIOyOn7FaIagp9ysu20IPKzXUomdGrYNAi9eSNpBVXA-G8RNUVrFIucYEhwq-ZjPe8Lp1fxnUX5fDX5RpGzy58aJBMXL0BCIgpjQOrRHdGOIuuVIyOfchLHr4INBbxZJxb0-Dfp-esujRDXoR2oBOQyXHwPxVeXCbTGIXYQEzUIVtOzfRDOFi9zJm82rnC_ZXWCUgtpz65LprJJ4aIsQ1wmW2IvEDBnqBvktDXp1G6N-e5xnQGnnCYREPbFORQ1ed_v6InRxBVA4uqLG7wicyF4l1HlG0xG1C5w4DOmWRs64sEUMaAJLcn6KC49cEClGCWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌دیروز؛
دومین برد پیاپی استقلالی‌ ها درلیگ‌نخبگان آسیا 2027 با سهراب بختیاری‌زاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/31469" target="_blank">📅 01:12 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31466">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D24d8tIYPndRcmmzK5AD-D-j-Jce4NTpuDcBmLwaDuxTsUwerxfYhTxNogeixNjiQr2VOSRrf2GVK0d2Vdxjdns3p_sh4iWxBIR_NqwHGLmtexJV2wAqoruNQx4gUs4kSrWBlFTrRtppbiKrXBCdKqk2GgwqceGn98hj41n9NL8Zh86r55afAjRqDSMZggc-FWRA_XX_k3ztCRIPJSNSsQszLCjkXSWjAeDUbxOWWAqa8IjGMM0EIrrsJBkjseHYVcVWwVIn7fHy5K8kp7fOzIDN6Hjb5M9HC4AOYnAdvZUmkQkENYPd-_DOu-_mG4ny5G4cIGlZ6XYhYydaWpfOHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EdrsXkR8Mtdh8EX7a9kuHknmEcshjAk-WxSmaz31fmF-Khqw8kaPefs-llxbtSvO3qWdai1y0SbbbczaVCktPCHYV6eecj6G_tqVqBL6LneuOR-yEJQR3dPKJNG367NccI2TLnj_5R0nLWN-8JZ61_D012Bc86CrYNHMnBlHYxAW5yMGpRT5kvt3PCu0KQe_Urap2sKpadZ2BJBUyu15DzdAKqXRxIbLqcSzxixo-PZHlCQJt0E85DR67gi6hV6xIWd3I2R59LO1p4UaDz1G9l6sUpJAhTe9Xo8dOXBqHCeB0lHodLu43gAS4q6dKr-MMtGdudlEBCBS-7SF_l2HUw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌دوم‌لیگ نخبگان آسیا؛ دومین پیروزی پیاپی شاگردان بختیای زاده در شب درخشش یاسر آسانی؛ آبی‌ها با پنجره بسته در صدر لیگ نخبگان.
🔸
الغرافه قطر
1️⃣
-
2️⃣
استقلال ایران
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/31466" target="_blank">📅 00:57 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31465">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYtFJW3Bn1GG2Hpo7MPEE1q6_8lvUZcswq0KcoSGQ8NZ9-Mfxht4P-mhVimdzDZtJ-Ix2ODR7Xdv2pwVeAdP6es3ipJWCJtVxKwElSJjclc4_x5naICCOAkplUNa6YBFmRY1reKsnLXzMyUzBf-kmuY7fqt1--DlEWsheelu-kUISK9efr1NGLREMNGFxIJq8Ryz7RGwcH0utpDuERka2GQOY6W__y4-b5HideoqL6eeakTPVJGc_Rl159CVrSA5d7dv7OKjugVo4d-nXUbaqvQvJ6KpC8vXYzUZqQEB0TuwnewXPQiQRdQzaVmWJDwOHBKKlcOSIdheMQB1vFkshg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
👤
با اعلام مدیر رسانه‌ای باشگاه استقلال؛ مصدومیت یاسرآسانی‌جدی‌نیست و او به دیدار هفته آینده با گلگهر سیرجان در هفته نهم لیگ برتر میرسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/31465" target="_blank">📅 00:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31463">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J92aPRwaRsyXjy7NEIbED8QSHQV1Nqmi2vLCHhV770XadGiwOVerqY-Ye5gJwITmSUo0QBqbd3h_mDBNmuEmZ5fBYVNYi9xe-4vTeqF6m_nxwBSlEvIo56OQMox9GLNpMH9FWaMr8soW29Uc2Ip7pphRdzKD1DYPsL2H5ORovHunMvUl7H5iU1tlKW_53XhIIPg2QgZK_4FlhPxf41rinpzb2awIMQA7q4ZJvexPLZXSTP-_ovlc0xWx8EoNPDCN80i2ne5i0JglWNy6scvjN0cCkeP4WKyMp9c7qbu3wTDTNmd6IOfk4zNmUcFyOqIq0subofysD4b2uCB1mbtGrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
#تکمیلی؛ یحیی گلمحمدی سرمربی دهوک عراقی توافقی قراردادش رو با این تیم عراقی فسخ کرد و به احتمال فراوان با عقد قراردادی چهار ساله سرمربی تیم امید خواهد شد. فدراسیون با افشین قطبی برای هدایت تیم ملی امید به توافق نرسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/31463" target="_blank">📅 00:37 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31462">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hwPI854X0Dzk4Grdzota3njfpetja4HFMMG71exwlHv-1EROM6i-AGuW7jEu83gZh6P5HrdEqWbqSl8z1bhcUoRCfPRXuL-cIyN88wAUAOHnoFMzIT2SQCYjkcJGnPhFXM1_s3CUUFuthbhTjPeWHYXUPU9w-w8z2CMt3asaZ5qP96_vipoWGvBrKf9bP3vVl63AZxmQtYJix8EdZQ6LWSFdWwCSIwhxJGXoPr9gBktbX7wk_gcAOIuQ0NKlM2MKOHw3uBmchrFNZsuNfn_AvoeawhgsqqIauWVxseQzjlpwurniAGTYx8x3RFWB0TQDn6GvStifS9ZjZmef1fC0Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگام این چه خبری که منتشر شد؛ آرجی میته، بازیگر نقش پسر والتر وایت در سریال بریکینگ بد، به‌دلیل خودکشی در سن ‌34 سالگی درگذشت.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/31462" target="_blank">📅 00:29 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31461">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e66d7fe407.mp4?token=AwW1GLc5Ef2eJLmQo0ZUBWVlw0tN9aOf2nkySfbMUMRXCv-Ex6VU29fdwXQmGQwTamEFNTqtULrut9i_TEBO3K0PhsVe54wWuqzluHk8-JGMdwba1eslKjddY1BMKfHrMuH1gm9Ldr_5cYbk0okFeWEJcRt6BfMPXR2k3o_aGrllaK3hsPZRcxFVpJBBmfIKplD3ElSc7u0KPBhjDAwiJIHga81kTiUtlpZ4U7UuC7GTw_Ik_A8nIZY81qGcTDe96m3byCU88dh7Kvrzi48efuNuYtK6vswZsTIlNVsz7uljmNAEmupKpzRkFBpcAyCuhmNP-xW4icMqOViHx6_O2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e66d7fe407.mp4?token=AwW1GLc5Ef2eJLmQo0ZUBWVlw0tN9aOf2nkySfbMUMRXCv-Ex6VU29fdwXQmGQwTamEFNTqtULrut9i_TEBO3K0PhsVe54wWuqzluHk8-JGMdwba1eslKjddY1BMKfHrMuH1gm9Ldr_5cYbk0okFeWEJcRt6BfMPXR2k3o_aGrllaK3hsPZRcxFVpJBBmfIKplD3ElSc7u0KPBhjDAwiJIHga81kTiUtlpZ4U7UuC7GTw_Ik_A8nIZY81qGcTDe96m3byCU88dh7Kvrzi48efuNuYtK6vswZsTIlNVsz7uljmNAEmupKpzRkFBpcAyCuhmNP-xW4icMqOViHx6_O2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
پیش از بازی با گالاسرای در UCL
؛ یکی از خبرنگاران درباره‌وضعیت‌فعلی رئال از هانسی فلیک سوال پرسید که اون‌هم‌عصبی‌شد و گفت امیدوارم بالاخره یه روزی یاد بگیری از این سوالات نپرسی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/31461" target="_blank">📅 00:24 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31460">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4sWnyXXPhVxF206a6Ffip_oMkZ6adB6nvEWYrau2BLo2B9UjBL3VJxhH6mtx8SF6GU4vPY-oSEhjxpX3ANynDb1fliA40TD5kgmZacT4r7a0a7FDGguK35wSEs_-Hzeg9AnBWOPdwOLjMWvZvgRnnyxuve_GcyC6sM7hlFuu-jsM5CaF4p9wqFjw1vgRXO-DABZlnqVfJtO96yBJkKcUJk4wc_1cHpLhFvhREfDYcPBiiqJf5T0nkrpKOaRpBTatYWz4DlucuR63Tv6k1g4x0aZ2LE7k0VaP00udmuSqQ9-EhmohrTQ9KM4DdWykASenNol2w5uvOZeL-kA2wgmkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ یاسر آسانی لنگان لنگان از بازی خارج شد و بجای او محمد حسین اسلامی وارد زمین شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/31460" target="_blank">📅 00:08 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31459">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PYyFEp5mN4IO2qXOEEJriEARnra_dbYyEYyCjrYx8eDsOPJVUhWXecIYu0cB8fJmTyhCLcsaI7Jovq1fHE9Ey1BhBjuMtwDogeF5_l4zoygXNF1mDECyRP1-D0g9yQodyfMAW8Q1ypyi1Q5u7rgWuTf03PEOiVgVeUM21OEw6oJMQb1ZLc7dKEZktOgejTT7gsbZL0PqaCZGk6zK8UljgH516PAjYRPk3OMmCFf3ICDrLal-pMI0R00peHqIdPOJHoR1VUZL7RzvriCMPIBuxdBkrOsIMYh5CZ-H8spHqqgxDsDEyNLMuOS2OfYvBgMqJqPn2pV3TDUOlvz6_RnTKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لیگ نخبگان آسیا؛ دومین پیروزی پیاپی شاگردان بختیای زاده در شب درخشش یاسر آسانی؛ آبی‌ها با پنجره بسته در صدر لیگ نخبگان.
🔸
الغرافه قطر
1️⃣
-
2️⃣
استقلال ایران
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/31459" target="_blank">📅 23:51 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31458">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yml6Ya7gHHjvhzUZbflmiljA3TzgZaQelAXeM5A0Oh3VesDIHPyAZt0nkzCBBKlZ_q5mU0lchIolY1PuAIbzpEwrsx-_dShLm99CJq5NieCZ443l5pv7hfogHYQCkU2IODLTAZXbrGzhB4Z5__T_5_P9Bua0TdFWcxD9bD6PcaJ9mXFgydpUbRDGFQiuX77a-xfmQR5AmdHuruD5XBardV8hY98hP_01Ho9cLJF17UWa6DAma1LINNDvzsJaupoI93HXiaW6c2-g8xhFRBD1ZGbye_MVInahpe9MsUjyKuC-JpFq8SFclZv312VYLk-mMU5wBt3qUmatImIeheKwhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ یاسر آسانی لنگان لنگان از بازی خارج شد و بجای او محمد حسین اسلامی وارد زمین شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/31458" target="_blank">📅 23:48 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31457">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57855f950d.mp4?token=qchGtZI0VAia6avkTKsFkgxCJDkSO4GQGX78IOXZgBAoGlNfP17LZsqsmgX4Iy8KF_KLo_xyOyfMip-i944Gjqh81F9Cs7GSTRUUvXsIX3ZaetBUx5BaiTBRgNgJfiakzS7CLBlZySLbPAuTOIbCTXNOrZ9zLDRWpQUTjdkNNxqtk2IXQ3btkaH662UyUUeuoi8BFEcLdLFj5bnfMU-gZXoX4EhMp-QBZmXonpZAYkWz93vox3Dq7uoaU1rBhrISpj93rmz62Q_oCrufR6Q6SGGr3vtNE3_NgE5xpps1Mn7iZefT-YadQnonVt0Kev8dMgEK9m9Ol6LZP7-BvpIuEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57855f950d.mp4?token=qchGtZI0VAia6avkTKsFkgxCJDkSO4GQGX78IOXZgBAoGlNfP17LZsqsmgX4Iy8KF_KLo_xyOyfMip-i944Gjqh81F9Cs7GSTRUUvXsIX3ZaetBUx5BaiTBRgNgJfiakzS7CLBlZySLbPAuTOIbCTXNOrZ9zLDRWpQUTjdkNNxqtk2IXQ3btkaH662UyUUeuoi8BFEcLdLFj5bnfMU-gZXoX4EhMp-QBZmXonpZAYkWz93vox3Dq7uoaU1rBhrISpj93rmz62Q_oCrufR6Q6SGGr3vtNE3_NgE5xpps1Mn7iZefT-YadQnonVt0Kev8dMgEK9m9Ol6LZP7-BvpIuEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بوسه کریس‌رونالدو روشمشیر و درخت نخل نماد عربستان سعودی و ناراحتیش از جنگ تو عربستان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/31457" target="_blank">📅 23:33 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31456">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BSp1XJYV9y5o6Kf_5i2D8zZ48Ew_X0vApjAXPPTip0VAUajsbYzzqlK-sK5wrCYBLi5rmWk7V9Hdj8wUmrWEGurAkKso_ehzwIhNtA05D_yhjm4VQT6UN1C8XX3hgzNUsZXHPQtLQPrN5XQlVlhewAa35vZDPISsnaqG1gWZi9XNYuGxBIbBTd4QankOUYzmyjjAPvK_6ekRiVfJid16r_tMUDVaEYGGURsyCtsSg6SuOIRPPDhMRhKY8jgjZcQsz-Al-NaJpnnPd5UqWiLxs7qiHeR65amo2dfcXf9OJlkHJUqACLlBcv7eN-JqDZGbLVtH0FJLfdjhNDMWfIaDmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ حوثی های یمن: بزودی تمومه ستاره های فوتبال از عربستان خارج میشن. کار میکنیم که عربستان نتونه هیچ‌فوتبالی‌رو درخاکش برگزار کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/31456" target="_blank">📅 23:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31455">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad69f494fa.mp4?token=LeLFCNc6GfT9kRICZxgov6b_DInxUPa3GYxZfi-rFPyAERysiD9sAoCTzVAqiokAYuJf8BZQo3Z9qDUzBL5AuXeM1UqkotFkyfireupXN2Z7zZGcL-stpzRnlaaOPaMhp9-R5JxY6Tl_0nYneDWGdFMg2CGE0H8IUYJZgfmaGBFSKRjQeL7rBtCaxrwJNfOGYyisBcB1mJekIavxVWs8auqBakLdyAAgpa8vdcAbBm9XkypVtuAcz7f_va_JPPhCv-T-KsS-CBOBLyOmUt4rjN_WF3GRw_2PUGDBDn93Gl25kGvxXuw4tENssExONOe_C1rdAwWp1phG24ajdtxMyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad69f494fa.mp4?token=LeLFCNc6GfT9kRICZxgov6b_DInxUPa3GYxZfi-rFPyAERysiD9sAoCTzVAqiokAYuJf8BZQo3Z9qDUzBL5AuXeM1UqkotFkyfireupXN2Z7zZGcL-stpzRnlaaOPaMhp9-R5JxY6Tl_0nYneDWGdFMg2CGE0H8IUYJZgfmaGBFSKRjQeL7rBtCaxrwJNfOGYyisBcB1mJekIavxVWs8auqBakLdyAAgpa8vdcAbBm9XkypVtuAcz7f_va_JPPhCv-T-KsS-CBOBLyOmUt4rjN_WF3GRw_2PUGDBDn93Gl25kGvxXuw4tENssExONOe_C1rdAwWp1phG24ajdtxMyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
قطری‌ها خیلی زود دومیم خوردند؛ گل دوم استقلال به الغرافه توسط گودرزی در دقیقه 60
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/31455" target="_blank">📅 23:21 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31454">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c059d16e2.mp4?token=dld9ocRUOVWJ6gOo7Gb_nGJPA6EA3sTH1xlWv6YMxFzeNPUCBj_wimRsvOObIaN5cLN0FgQuwsvwimj7NHQyuYwPN7V4BrSJUxmpm1Vz7ZH74Qwkfh4My2cKPASCym6E1OP36jmfPeZRdW_YV4t-PRyicbsSJwDeuW44oy9W4svLsISfl06d3aLpDt45Q-_yYOUzd1mlqMJkdZVhVPk3murU1AFfmKOZwGzV4ZuISTYf8rlyMw69TYfFC7I9ZJkBD-5U0rFJzK7gmP_czGeZAKrkvcVraKQuVCkezmmN7Tnp-lpwon2Xki30gd7LwxebDhNapJ4vaQ00qhM4IN7vPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c059d16e2.mp4?token=dld9ocRUOVWJ6gOo7Gb_nGJPA6EA3sTH1xlWv6YMxFzeNPUCBj_wimRsvOObIaN5cLN0FgQuwsvwimj7NHQyuYwPN7V4BrSJUxmpm1Vz7ZH74Qwkfh4My2cKPASCym6E1OP36jmfPeZRdW_YV4t-PRyicbsSJwDeuW44oy9W4svLsISfl06d3aLpDt45Q-_yYOUzd1mlqMJkdZVhVPk3murU1AFfmKOZwGzV4ZuISTYf8rlyMw69TYfFC7I9ZJkBD-5U0rFJzK7gmP_czGeZAKrkvcVraKQuVCkezmmN7Tnp-lpwon2Xki30gd7LwxebDhNapJ4vaQ00qhM4IN7vPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آبی‌ها گل مساوی رو از قطری‌ها دریافت کردند؛ گل اول‌الغرافه به استقلال توسط فرجانی ساسی 48
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/31454" target="_blank">📅 23:14 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31453">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1448a1396.mp4?token=oL9BN_djB_Vmey6616zm7ZF3rPfydbOBNNuRDRtGhZb2GCs9X63bNqXuYBmRjWGfnikLuAPhmmkhtWk8c6ZG46u5SwVKVBl3WQk6F8BUiMdcuf2hymxRP6FvM2DYhESgTqnLw5unrhAa6N-FNq7G01xvfHFD1E_LTnwjRK8Vcm_MgJN15vV4Se5MzhU26q6aTLySC-jJvDDZsdpLds6e1BjAVMrsk01_pmHCXpRqbAj_AACIdomX5dMzn_fxbH7QSr5jNpfpPc3dO_kX-0uoOOCfC_2mLW1FbLipRIyjy1BbxmFvbWK8zsHSxtPb-B3bASoXcFMVAVPmNYjGVl5mcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1448a1396.mp4?token=oL9BN_djB_Vmey6616zm7ZF3rPfydbOBNNuRDRtGhZb2GCs9X63bNqXuYBmRjWGfnikLuAPhmmkhtWk8c6ZG46u5SwVKVBl3WQk6F8BUiMdcuf2hymxRP6FvM2DYhESgTqnLw5unrhAa6N-FNq7G01xvfHFD1E_LTnwjRK8Vcm_MgJN15vV4Se5MzhU26q6aTLySC-jJvDDZsdpLds6e1BjAVMrsk01_pmHCXpRqbAj_AACIdomX5dMzn_fxbH7QSr5jNpfpPc3dO_kX-0uoOOCfC_2mLW1FbLipRIyjy1BbxmFvbWK8zsHSxtPb-B3bASoXcFMVAVPmNYjGVl5mcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
زوایای دیدنی از سوپرگل یاسر آسانی به الغرافه قطر؛ نانزد بهترین گل این فصل لیگ نخبگان آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/31453" target="_blank">📅 23:04 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31452">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b33iL9o5JkjJmMRhLaLCNwGV2GD6oJcI4iECVKEoOgGU3bHIrY_tOnDMDHqg7qxZn7VF93tI008CNZbXNYQachVAhdF_YTH7KkmjvQS04D04DuDH17NLV-62kEPDWiS_hvMbRM3i7KFeZ7haqm0fLB0Nym3cliQSwJ9gBhboY2Jkm2JhWYzsyx8tW6CH1Oa8j3lkhxvzpCa1N2OfrWI_IfMFB6lEa2AdaIsz8wy4JScaWfD4J-s-4PxEpLzB6s_jHTy0As0foSkw526pWWJdk49sTpwaAqIjIfk6_Zpp0jmwp7RQXskk1UAJqt04L9aXolGObOmwDVC-ttrRnVQmgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
زوایای دیدنی از سوپرگل یاسر آسانی به الغرافه قطر؛ نانزد بهترین گل این فصل لیگ نخبگان آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/31452" target="_blank">📅 22:48 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31451">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Df6GKjYbw0U_RqIz4F0k0APg2FLu7uMNYm58ZoQ4N-DvSGMXiFVZwrn5w0yPI09zId20w9J5voXvQErwEayjbGOlL9SnWGQiR71d9YCCNvh4yAVARfAw2rzA2TM2w4jkWjptUQSkJ66s6rlBpUnqmV2hneA_tX04GjIM0XgeY-KEOV5BLLfRe-0hjRFGNiGrMSvBILy-3WZXkB3uqAEw4lYa8Ll5WX8tumau0il_oWZQ3EK9Ca6BiqaXZRIFID7gNmfasufaQLaZ9wEV3liM_Pdgf1Mt3WhMdTRJ8FhS12_buXmlIEE8R0hm3r5B-7zEk-zimd6LXeTpPGzWUZ9kqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی‌امشب النصر درلیگ‌نخبگان‌بخاطر هشدار امنیتی و احتمال حمله‌حوثی‌های‌یمن‌تاخیر خورد. عربستان با این‌وضع 3 ماه‌دیگه‌میخواد جام ملتها رومیزبانی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/31451" target="_blank">📅 22:39 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31450">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔵
👤
سوپرگل پشم ریزون فوق ستاره آلبانیایی تیم استقلال بلافاصله بعد از اومدن به زمین بازی؛ گل اول استقلال به الغرافه توسط یاسر آسانی در دقیقه 38
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/31450" target="_blank">📅 22:31 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31449">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8af2c2d01f.mp4?token=npPbfpzjQxoROZ5HHTC9isqbGq-SSdAVvnKqfUw0hYIoxp7zS5uPRkPmeaB5PyEX1M0r06Hs2-JhyOjlQuO-06WFi0lv7UOJyQyAAoBpIIINWwitdT3R1bMxoupEwfgLQE9p9RcVVj8EJ8rxIGua0c6tBhQnmt2rRpRysg6WXSL3g_wr_BvrFG1iCHIBbupjhDM1pNNPJN1NklHarJrr5h_DmMVWtFwfXSHExShTk5JrgM8xQz9HDuukmbUEYJQUHXtFea4FWAzdXVpNKkxuf3-AFky4vQs-0hbkQ73uxihpgAJ8GmLryBQk7lymYeq92AR1jSvry_TKlZVItGnwwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8af2c2d01f.mp4?token=npPbfpzjQxoROZ5HHTC9isqbGq-SSdAVvnKqfUw0hYIoxp7zS5uPRkPmeaB5PyEX1M0r06Hs2-JhyOjlQuO-06WFi0lv7UOJyQyAAoBpIIINWwitdT3R1bMxoupEwfgLQE9p9RcVVj8EJ8rxIGua0c6tBhQnmt2rRpRysg6WXSL3g_wr_BvrFG1iCHIBbupjhDM1pNNPJN1NklHarJrr5h_DmMVWtFwfXSHExShTk5JrgM8xQz9HDuukmbUEYJQUHXtFea4FWAzdXVpNKkxuf3-AFky4vQs-0hbkQ73uxihpgAJ8GmLryBQk7lymYeq92AR1jSvry_TKlZVItGnwwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
شماتیک ترکیب استقلال برای دیدار حساس امشب مقابل الغرافه قطر در هفته دوم لیگ نخبگان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/31449" target="_blank">📅 22:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31448">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7a4d637ce.mp4?token=KyHtyly1OJrr7MrI3rCl0rlzUsgsBT_oMdkmQkaiA5btT8di-FuQjHwetF0pu4UFC62b6xHe3SP7glfq6KlnJTPOH90bQdQhV7hL5y2bDGWmv-c5XmphdEUlt9Q5qvqG1VGB3ZjERqydDEL-BrdlmsVIjShvgAT4WL0RtshGElC0fe-_YOQMo6tH0uXaJ2G3dThkPMlmhMG7d9l7cXSslBxxV3DLHpFHYG-PyJWOJB9OH13y6A6RoNX9O8EYta1LY0bC68pJCz_NsuUiGlwUSYxZnYevl1j5USd38ZsCCnGXPWcBunSKIj6Pq-eldZfiShLlMbIDnwodQIxpHaVMLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7a4d637ce.mp4?token=KyHtyly1OJrr7MrI3rCl0rlzUsgsBT_oMdkmQkaiA5btT8di-FuQjHwetF0pu4UFC62b6xHe3SP7glfq6KlnJTPOH90bQdQhV7hL5y2bDGWmv-c5XmphdEUlt9Q5qvqG1VGB3ZjERqydDEL-BrdlmsVIjShvgAT4WL0RtshGElC0fe-_YOQMo6tH0uXaJ2G3dThkPMlmhMG7d9l7cXSslBxxV3DLHpFHYG-PyJWOJB9OH13y6A6RoNX9O8EYta1LY0bC68pJCz_NsuUiGlwUSYxZnYevl1j5USd38ZsCCnGXPWcBunSKIj6Pq-eldZfiShLlMbIDnwodQIxpHaVMLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
به دلیل جنگ اخیر دو کشور عربستان و یمن و شلیک و برخورد چندموشک به‌فرودگاه های عربستان احتمال‌گرفتن‌میزبانی جام ملت های آسیا از عربستان وبرگزاری این مسابقه در یک کشور دیگه وجود داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/31448" target="_blank">📅 22:17 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31447">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30cb6e2f17.mp4?token=eOOEwjqdSxz-mF4Syq8cJXiThhFeg8IfdLopBhLT5nWq9mcWvRzUubTpj3R1C0HYdHdq_7w7iTYeamKUs_3P4-DfVmQfe50EQ7QpippVtmchdrVjMufm1Z54TBtHQB_tlDMZQO9nLvUXPPgmJB2S8wmuZdF7vfplVr6ZndbIqimf73lbzEZEKuIncmn7JU6JOQjoA9VB49w4ldl4WjTQpBLxtOumxQk7-s4ueqmk9KFUlSKBJ7RGiz2N3E76m3SQz-x92MZxFqQRtlLlpkTQP-S34p2E0eHsHpQCfTL57xR-I4bXkfs6larpHEDs6niwJIgGmx41vK1ohB1n9nU7jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30cb6e2f17.mp4?token=eOOEwjqdSxz-mF4Syq8cJXiThhFeg8IfdLopBhLT5nWq9mcWvRzUubTpj3R1C0HYdHdq_7w7iTYeamKUs_3P4-DfVmQfe50EQ7QpippVtmchdrVjMufm1Z54TBtHQB_tlDMZQO9nLvUXPPgmJB2S8wmuZdF7vfplVr6ZndbIqimf73lbzEZEKuIncmn7JU6JOQjoA9VB49w4ldl4WjTQpBLxtOumxQk7-s4ueqmk9KFUlSKBJ7RGiz2N3E76m3SQz-x92MZxFqQRtlLlpkTQP-S34p2E0eHsHpQCfTL57xR-I4bXkfs6larpHEDs6niwJIgGmx41vK1ohB1n9nU7jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی جالب از فوق ستاره‌های حال حاضر فوتبال اگه خانوم میبودند؛ نیمار خیلی بهش میاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/31447" target="_blank">📅 21:40 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31446">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_k5Ydb5Or8bozRBy09ki3QqdGCcbbslg0LTBRTxeV2I2TjaTm-0UKOCsMA34CBEP_a4NaqLS2UuQzkqYxcF8nNjgN2PoeVmm6-1WdaNebh0CLEVCEEgOji7nYDbtIY5wW929HQOG5vKz2g8_ATZn8a21ShLNHSaF0fdPX84uEWipLsDydZDv1-D_DtZipSu25RUrywzGd2qk0_BUfFhZPN0wE1fC6lmQzbK8L67PW2-mq-Dch1jZ9AnNkpTGf5aRl2YguI1nmY7pTbsS0m5CV6tuck-zKcJi2M9ujlRCnI3E-3aHF4G18mHn3WGjJ4i1VACBj2uyxmSjwQLxqtvWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ باگذشت‌‌بیش‌از 15 دقیقه از مسابقه بازی تراکتور و الشمال؛ شبکه‌ورزش موفق به دزدیدن تصاویر شد و بازی تراکتور الان داره پخش میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/31446" target="_blank">📅 21:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31445">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VlEEvTxZ-eM4ykWIQTGlChN17e3-NUWL4TLoa2b-6yesYAb7fZWZ4a-qzq8AZ07WKPE3tBwQxkyGrhKXXk1IWowxZB_92Ts4WzcotT3ReJylH9CDuCq_KxDfooQiUz_sBRqIh_HLxFgo3BYOnTeFEOXGwREQDsL1FRakv7UlgbsY1bhHRNUEyP4i0poyzFNNmZNtITwTSXjaBG477hy7f7JO2GPL8AAbCaD5CMcCeljUgPOiMyanNZ_KLs-ftwff5bYunFFDU55IzVsgEN1DJRPsHrlmZkRs1j4LhhdNpMt29pc8_oqzIksjuruIHKFkjVECpiFwKJq4e-wVfrtkog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌امروز؛آغاز هفته‌دوم لیگ الیت با نبرد حساس شاگردان بختیاری‌زاده مقابل الغرافه   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/31445" target="_blank">📅 21:15 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31444">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/drvUZPPBBeUI8OdMWRPcin-DWATkZSuUYuLWDpCF_43MgkIIqMNHKsjj2z3AtxA49WDTrJq0rXUdybnlYDW2x3jsmQTuMsrjUimjBdVG0PylOlfy9yRzfIoU6fqG40c6mWQmziYLxeWcx0g13pVdNiG_kbMDgy_MEQb2MhoGIc1d9Vzte5SYEbz5F3nyTjbuixTmP9awWzT3Oe-STd5oIsINOPqOQtEMHozAqs30eLMOQLgmDbOQzoGzFhjx9UXIc2RNUkDcxuIUAsg1nZ9AQuMdS5c0l3Y5FVOlk1uGJDz7r5rZso6EGVuhQdSTdz-qmM4A4t4czhMo7shmWe2AlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرنگار باشگاه فنرباغچه و فن کریس رونالدو که در ورزشگاه بازی شب‌گذشته تیم ملی کشورش مقابل فرانسه درهفته‌اول لیگ ملت‌های اروپا حضور داشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/31444" target="_blank">📅 20:49 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31443">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MarKEj_c5mFQDRWDsl71t3BpwiWm3stMuMA4cDMOQJzGoWoDP-Uo5pwrvzs9Jz3Tee6hsHJMK-lLqmsEpR96zfo-qhUJR8TmA09eN8PM1f0-wwMe45ellSo9GP5QBmPldiUpFcYYtxMAh8VbxnCA-2gmR_7SKZwq02FUFxeMKLGwMpe-JIGSQ_Oib27WV65LQJWq6tr6Xz7Hi4qBCT1PqnDtssH-glxIeyxTbLKxPvxufaNMcM6bXvopIiWBHOjIam39w4rjUbP9WoVigEsCVj9PiCx8PruOBELVHgnFhV2njbkZOB67Bg86tYNGNfK5wRYp2SXC4UPjhsMyyycMcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ‌نخبگان‌آسیا؛ ترکیب استقلال برای دیدار مقابل الغرافه قطر؛ ساعت 21:45 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/31443" target="_blank">📅 20:34 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31442">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bSAEMuvHer5jBWeSuqtWJWPAY2-i-2Qlq6srOoLAK8SQbeFbC3yvVsjOuBsU6QWVlYqvCbyrHN10DIFi_04n2D0y1eVYcQ2AHZD64jFzCKwONEtY1YpsCfMBT5FkQjpgSjQvYwr6EhykGJPuChAI02SxqJl0XR2Y4PIg32Q9pNFfwePRPOWSxHYHV6OSma2zietpR1qQWBsYebWXMY9iNvlQW9kkHDGQSDXAVC731H1FeTVJcC1NmCBGjieDeCHcOONNWe65VF2AW38XetaGbUk69igO-eSDHJZW_9w1D8W2uNzTnl1SQ19xRsJ9rnJmi-kd5PW4G1x_mUx7ZdOrAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌پرشیانا؛ یاسر آسانی ستاره آلبانیایی‌استقلال دیدار روزدوشنبه مقابل تیم الغرافه قطر رو از دست داد. این بازیکن ممکن‌ست با کاروان این تیم به قطر برود اما قطعا بازی نخواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/31442" target="_blank">📅 20:18 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31441">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9509bbb5ca.mp4?token=oXqmhDkC9B8vdwZvCDmpFlZ37Nr7vO5pjNpQLPAhEykHz_kdFHNQE9s8embClMhNpWwYFD2Wx84i7rnc5-duRdbvM638sXMDbcv7LnOGiS_JEZCIeaPXY6vRJUG6RiezL-BrKNouvsKufT6woREu7wJIJWDvlMG9hX_q7NsmYkCcj20WxRY6wUo7w7hs7ETK9CGIY5zxFXQkqLfzOOMb1h1CEV84MkKYWP8TP6lHFMSyynJufqRPtSs_84t99dUhxHxhL5xbDfDxun9E6G0roFhhp5AoHJ3_v62tIuIqMTXaDY8aWTYJjRrwzcJFAYrhZQhrpHfxBbL7uf6CwGqIuI7nkvcjPZLPptW8vz-jLZ0As7bUcTbJChShkhxd2fz3gyiVEqxVR1Ug9OAX93K93dmyjplFcTK1h5XBb2dA9zDbJ0C1lKofWfJcP61HMVdSee2bATNBgjH67plT6wAD4ylXvhHh-xRnjidzlP245ePK7g-tTO7HVrySLUP1qzrwmHBsGUzxKqbUg_EWzwVx9HryCmnYa8gPHkCVTw0DJjy32ytw_4DGh_wGMiQPyTjHj_28Aiu8ZW71JWfaI7BexA9o6zBFemd5NqNI7pSZcagGuJHZrfOkRgtLScxCZxBUyuAEWV-pxMLThEUVC0-JxEx3JxeiiyDJbA7Lj_pdq0s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9509bbb5ca.mp4?token=oXqmhDkC9B8vdwZvCDmpFlZ37Nr7vO5pjNpQLPAhEykHz_kdFHNQE9s8embClMhNpWwYFD2Wx84i7rnc5-duRdbvM638sXMDbcv7LnOGiS_JEZCIeaPXY6vRJUG6RiezL-BrKNouvsKufT6woREu7wJIJWDvlMG9hX_q7NsmYkCcj20WxRY6wUo7w7hs7ETK9CGIY5zxFXQkqLfzOOMb1h1CEV84MkKYWP8TP6lHFMSyynJufqRPtSs_84t99dUhxHxhL5xbDfDxun9E6G0roFhhp5AoHJ3_v62tIuIqMTXaDY8aWTYJjRrwzcJFAYrhZQhrpHfxBbL7uf6CwGqIuI7nkvcjPZLPptW8vz-jLZ0As7bUcTbJChShkhxd2fz3gyiVEqxVR1Ug9OAX93K93dmyjplFcTK1h5XBb2dA9zDbJ0C1lKofWfJcP61HMVdSee2bATNBgjH67plT6wAD4ylXvhHh-xRnjidzlP245ePK7g-tTO7HVrySLUP1qzrwmHBsGUzxKqbUg_EWzwVx9HryCmnYa8gPHkCVTw0DJjy32ytw_4DGh_wGMiQPyTjHj_28Aiu8ZW71JWfaI7BexA9o6zBFemd5NqNI7pSZcagGuJHZrfOkRgtLScxCZxBUyuAEWV-pxMLThEUVC0-JxEx3JxeiiyDJbA7Lj_pdq0s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ریا بوز، استعداد ۱۹ ساله انگلیسی، پس از حضور درآکادمی‌ های چلسی و برایتون و تجربه اسپورتینگ، حالا بازیکن وستهمه و بصورت قرضی برای ساندرلند بازی میکنه. به‌ایشون‌لقب آلیشا لمن جدید داده شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/31441" target="_blank">📅 20:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31439">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HtMeBzbFMTpQ_uxih8W-Vq1WAxiQdHCV8zyoWCiWTaVQTN_ccRoiynKMXy2ng1nq4mvGIuCe0vLRavzX6VkCJo4b-k3ZnpnA53fXPkNrQX1Y5_ILeQFnlYox2Mm-OAUJDzld8nqU9soX7xjtFQuHXk2ExJNvZiol07oGzI-zE60ngy0pmhBy1XcGHi9Y3VXO2QJgERx0CaencYULeIXFE3iUz1Ls8Dr4gVNSGxVPRh93FWMOFJjwz7EqF_p20RrGIKYX69tIxc2ubkbI8oRRVfbk2X5hGvX9PaRGKRG5jWAbJ9hEnEGFn7kFWz5kJLejfpiFdXw9A4rP2dTE9HmAsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
هفته دوم لیگ نخبگان آسیا؛ شماتیک ترکیب تراکتور برای دیدار با الشمال؛ ساعت 19:30؛ حبیبی نژاد بدلیل مصدومیت این بازی رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/31439" target="_blank">📅 19:47 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31438">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eyCcFfGIWCpSkLfs2OaZAGGz7ncQiIWaBwY9Wooi52_1IlZwoovL1p97IOFAJkW5U1qxt4Q5NjkLGziV0xhqfcwQ2aE6wpf5S-sIarHwlwzQ8Xot1wUEcLrlmOOdMXUYUkIBSJPjxMkA_6JF9D949SEdJkMFiOd-14jBpPZmvjK0eLzxCYE4LeV7tNDPaNHs3ekM6PcBlvhfgrZPUx9jnvNaSSY1SsP1Uq3Ry7kOY0MxE4C9oBzLRdYrBRFL2P2evYVtZzcBZte-ZiuXN4THPUw3dRDHuu67vlSECoeTJTDEDsD_BO93PBZGACye9utTunjAbKou2v-EflnZE4OCjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مقایسه‌عملکرد مهدی‌تارتار
🆚
وحید هاشمیان دوسرمربی فعلی و سابق‌پرسپولیس بعد از هفت بازی ابتدایی‌سرخپوشان درلیگ برتر: مهدی تارتار: 5 برد، 1 مساوی،1 شکست، 16 امتیاز؛ وحید هاشمیان: 1 برد، پنج مساوی، 1 باخت و کسب تنها 8 امتیاز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/31438" target="_blank">📅 19:32 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31437">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oT5Mf_VJJztG9KlcLa_lELPBx61g5HA8yHYrfL2uoVgZKKroJfRd3nWzoLKiRPxWM230G_MpbkmHsCSBjBLN5nMJ2N2EoJt6JkD0QX8-8KV2ZlOXp-qMUyZ_oRWjvRoi7zqa1ZE9C1fGMalsGis_ALh9OxRWDriZrodUbND4HNkq-crkYTTTNvfgLa2yRV82g_hJpPQRu0YmCc893qjro3lcJQOjqL1cqwmNjqJJwLT1F3CJFRDyEeZkzHJoAH9lvVLfKbISG5cGww6BBMKEFfbksQTLpkD-v9aXMn8z_tSZG7SDT4cUDHjikESSzsI6slz9jka-K5zVVAlJORP_sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام فدراسیون فوتبال اسپانیا؛ وینیسسوس جونیور ستاره برزیلی تیم رئال مادرید مسابقه سوم آبان‌ماه با بارسا رو بدلیل محرومیت از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/31437" target="_blank">📅 19:15 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31436">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YC964DERHDAOlzx_pqi6_zvUnpO9yKmtE-2dgpIlKiZqlAxS2_ct4Lz_apoYz0ECjgNFMWvS4EImR6wTY0zWh00y0ARMMBmRUo_Lj6SrKKrA3w68ryErH5EYu8uAHXBI0yr5-qIY1EfRpLb8prLslUrtaMSs5ysWKYAP4XHwMN-nn2Kj6AZoL6hP15psvQlN73hD7EkFt8h88nCJcVtIdfQ_MoPKJCLSMK1T-_8IJjmay0vwVY-hHhMMOQKQSi8GPq9zzu7l76AgDFfSJgu8D0uQXC_ZWwUwobCBYGoB2uM5LXCMKclFiYgiId1ONzqYF3cBwBIy8lVjAApNo_TZJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
مقایسه از هزینه‌ای که باشگاه بارسلونا برای جذب پدری کرد بابقیه‌باشگاه‌هاکه برای جذب بازیکن هم پستی پدری هزینه‌کرده. پدری درحال‌حاضر یکی از بهترین و آماده ترین هافبک فوتبال جهانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/31436" target="_blank">📅 19:15 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31434">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDp5wpKN96oN2ZTltGJHlB5PtrEazPAlDjtZvnbOROpuW46SWF0LoeC3YG24Yhn4SY6Csl3xez4jJtACNIhRnJyAPG7-Sfmddvf0vJhuRphACKkbcqHU7ZYx6_J-cb6APwLUHnCpL0dDOZ-urOX7dNrkVCOt5rQN5mBTJUMBUrIF-yAhkqhvWTcsrugLi2mxLRIfFvPb5YKKBSwtpGJMV7CUNo1Ko0Zth2hRM0c-kArZ1fbuj8WY-Cv7eHxnZoR42qPxSpq1I-2mIqSv0KGe3OMCWk_Ae6bNRiWkHsp49ID84IxR4bjSd0P_I_4i1TJsC_S6QsXvF-g6jA3kagOpSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇧🇪
باشگاه رئال‌مادرید بزودی قرارداد تیبو کورتوا رو تاپایان‌فصل2028 تمدید خواهدکرد. تمام توافقات بین دوطرف برسر جزئیات قرارداد انجام شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/31434" target="_blank">📅 18:51 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31433">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d320f9626a.mp4?token=kgGVK8PQhHIEsRjoFUgICZSBEx-7ul6_d6c7zV7gUGfN97QkPSjXJYYUa1JtrFZ7342yJCDVmvYUGVpQIlKfE1qrcNfxghwi-hBMKcwpqM6Gk2kb48vI1rbWQHDb8X1ivDXEWXRcH5_kTlGA3IhCwGzLBg8cEhCD0gztQ4xnDvjVtUL4fZgGXb1fC1iu2pvGrxyrfHikcEvoCdAO7YBKhufv44nLX_i4Hgwuxopesqi2dbDlGCUhkdPaB-PapemvAIq_aLErd4CbXGgvBNViUW3Uf9tALlvz0hDeIr57PWU7nVKDImgMdLgcPKUis0vHFgO4TWzmkEUXJ9KkgpeThQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d320f9626a.mp4?token=kgGVK8PQhHIEsRjoFUgICZSBEx-7ul6_d6c7zV7gUGfN97QkPSjXJYYUa1JtrFZ7342yJCDVmvYUGVpQIlKfE1qrcNfxghwi-hBMKcwpqM6Gk2kb48vI1rbWQHDb8X1ivDXEWXRcH5_kTlGA3IhCwGzLBg8cEhCD0gztQ4xnDvjVtUL4fZgGXb1fC1iu2pvGrxyrfHikcEvoCdAO7YBKhufv44nLX_i4Hgwuxopesqi2dbDlGCUhkdPaB-PapemvAIq_aLErd4CbXGgvBNViUW3Uf9tALlvz0hDeIr57PWU7nVKDImgMdLgcPKUis0vHFgO4TWzmkEUXJ9KkgpeThQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عادت بدش روترک‌نکرد!
جواد نکونام سرمربی تراکتور:
شرایط به‌گونه‌ای‌است که همه چیز به سود الشمال است. چالش امروز ما مقابل الشمال شرایط خیلی سختی است که برای ما به وجود آورده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/31433" target="_blank">📅 18:36 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31432">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ywa9POgU78VvJsuJWtQz2c5Li0hkC657DO9Zf6hI0jR-o5R2jL0vri9VWjPRcH-7PFH0-VbUEwrGejw7nSt-WGuLPVd-Dg3iyMSIbPFlCtdb6nWJj_QftPjIGDvc6y7TzwDt823hjVerlAv9f7CHN7EG3uuPEfUwD5f_84VLiloXUGCcEcFqqEShMLZk8inIXj5e9e7nvzSJmOvvtOxL99iCvdSxadWQEsEdCXNPjl8-gjTJw5r0kU8jhWU-5mr_CUePKSU_3EiLJHltRhXcGNpPa2LCJZm4UXr9oWHuzTiFN4eVwHZ5_c-0fXYCjY9Y-08Yf6T-9HJw8QADFL4QNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
هفته دوم لیگ نخبگان آسیا؛ شماتیک ترکیب تراکتور برای دیدار با الشمال؛ ساعت 19:30؛ حبیبی نژاد بدلیل مصدومیت این بازی رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/31432" target="_blank">📅 18:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31431">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k70YcDYK5Dh-KPvcliaX90t6m1tbinu8fat9-j1NQFaV1ypEwNmHTMvVizA64RZQisrFvTHTwSCWghc90s0RaztxqeR_hWPHena18Fb_PEZpuhxSwpV5DLQTzix2kWrp0bMQuLE0OMdU9nq4T21GeHDg0v0f2VFRNjkM1nNCazI-sN5b43qJc02R1jGnT1NvlFt9qJrIkdfQcEa-8YKPaFdASErWmx8a-Ti0qlDOKTk0p3bt0llGSSBw7Db462pYfDZhXd2vquGGBjPcUMAMjWDLnC-UAaQm56ocOavhTTmqQoPrJnsr5KjbKEXbegrpmY_xPrAg_0xglvlyKNOjuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افزایش قد عجیب پسر رونالدو!
کریس جونیور درحالی‌که فقط ۱۶ سالشه، قدش به حدود ۱۹۰ سانتی‌ متر رسیده و حالا ازپدرش کریس‌رونالدو باقد حدود ۱۸۷ سانتی‌مترم بلندتره! جالب اینجاست که با توجه به‌سنش، هنوز صفحه رشد قدیش بسته نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/31431" target="_blank">📅 18:09 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31430">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zv6mfYvNgAEePRtIVYSUjm7wufzApdL7AnvnbsIrVlsaBdvCOLwGUGvWoebLKv8N4R2SCpwSZN1UZcChw1pU66UPa6rCMEWPVytWu0_W-lXc4VQzOBeGfl4IIJgn0KH6h_1Jabd86lrOy49c8loEhVbQ8Wo8xOWbDlYzKxgKhn3bOb4pZnikzPhcAQYPGxKMk8gGh5ZLhdnhjskpAEa5EAcmpsOX_IRV6nNGrA2OaacquZMSWl5hmTsszUhBNPNTUJAtPlzVrCXY26ERZxKZ8rTQPai7gqx_7zt-RWpV85AeE5QjjL4asv4i9Q_gzdIrXbqBM8uH1WBSkrL989LsbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
کریس‌رونالدو: اگه‌کسی‌مسی، پله یا مارادونا رو ترجیح می‌ده، این سلیقه شخصیشه. بهش احترام میذارم. اما این که بگید کریستیانو یک بازیکن کامل نیست، یک دروغه. من کامل‌ترین بازیکن تاریخم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/31430" target="_blank">📅 17:42 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31429">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nm83QUvHcgTSYi1Vp9jFH2nhOH315-fGAEiwUIL8cf5uoyrwLUQC2O3G1NobVch8aNz-E0vDIUdPENWnczwDzGnzhfOFoEc6k4af_C3SRERLjtX_x6Z7wGqvwNrbHTvHWMeo5JmtRAKlKUF94evzg7D2pS9DNssCyz14JJ3hIxNecqJO5lTA_pSbkV3ZVPtaN5-7xIKrdP_nsvzhXm3F4iKn18fZxRm3Oh4f3FrN81DydpEKxqCPjyADzFuyFCiP0g9SOYwstMhX21rlAVjawdMX5xA4WXeMqyzyC18rBT7qpPAkUSx7b20EmBQM_Y1tJ_HPsb7yab0g60kDnS_4bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درخواست‌پزشکی‌علیرضابیرانونددروازه‌بان سابق پرسپولیس و تراکتور ازسوی‌سازمان نظام وظیفه رد شد و از اول آبان ماه اعزام پادگان خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/31429" target="_blank">📅 17:32 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31428">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cs3A0YmgRheUuxysHVMqi2oSiC92unn24pPg_NCAa-danJJT1T_wjjD5S5ao9ItCa5jdsxyk9qedfQ86c_-SWxcEnKZJo9sgDH5zH6GK0s2ZnHKfOgQ2ArbXWzLhQEK60WdtIRvYaVZ9uwvg4QhESlWxGmVGb_Jtvz2i49w96PFB3pF6zj1co-Ohvk05mMzuoyjfaIXYg5XV8za4sW-XprU8cAVIPW1PrpNiN334X7sg4pJguOvFU1cMk_VEWT4pYW1KBZSFPdqKVwjWEo1uZX-V4f0lKGJjC6dr6wh7Ode71Pzy3X26Rw34Fka9ihDS-gCZnZL4TgXznW7ojFRo7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ سهراب بختیاری زاده سرمربی تیم استقلال در تماس بامدیریت باشگاه درخواست جذب همزمان یوسف مزرعه و یادگار رستمی دو ستاره 21 ساله فولاد خوزستان و فجرسپاسی رو داشته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/31428" target="_blank">📅 16:22 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31427">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PwA-pPByVq0rUgKG8Nt8NZJJnaaAluPamsJydgPIauVBI4gbm4hkYCQSuJesfHcAbxZ9YGfFcLe5qkDQK2e9MjXIlKxYyJVgOFrHRL26AFyuLy5EGWPNZLGIgm-bMbD257zUrZtRsI_tr8CwLFwt1OOfQqen4_GSh0v8mpm8FOpcPq7fe8qSFG2hP3oI5Atla-wl3SUCnzL7PPULMY2YnK91OQcyqEHovkwEC6viQHxqnBsFHKqnrR4WeJjNaBA5Z2pkLcPVB1u0daqSw1YOl7Si0IpThz8wGqDLsAxi_XKSsXK2HzxTL9neKFrreP6F2KZ2DxqLwteETE8ncV-Vkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇯🇵
#تکمیلی؛ کازویوشی میورا ۵۹ ساله قراردادش را با باشگاه فوکوشیما تمدید کرد‌. میورا فوتبال حرفه ای خودش را ۴۱ سال قبل و از سال ۱۹۸۶ شروع کرده و در فوریه ۲۰۲۷ میورا ۶۰ ساله خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/31427" target="_blank">📅 15:12 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31426">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">‼️
ویدیو کامل قسمت سوم فان 360 با امیر مهدی ژوله با بالاترین کیفیت؛ عالی بود حتما ببینید تا آخر.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/31426" target="_blank">📅 14:31 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31425">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MUsUr6yOHMKF9Nlji11DtYdh_BIR4vz-Ygo-huOztypTJF0IgQXF2JED22OYrJ1uz_vqR0i_T_J6OMmh4k5g3xfvyCNdFaJE2Y0zUM-lJ5Iwhnr8ArhYIOniayHy0MLMh3_NYnzor4bno-tHuoCtFGbpbgIV7LQZBz_eIxiZ7FgkvDbf8C3cwCcKS9fFgU5B1Nwif7DmCOmcHCLbb8TiTT52zA3eO3F84x9LB0_yJVloBq75-dnePoF34GzAJgrmtlWq4NiGeiIdbbtN3gwU4sXAH2n4r3QlIVx4IkTpxn6M9PgeBBsGH4h9ClsnZUsgTanC5wVUQ3yRuzS0ZA0aqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به دلیل جنگ اخیر دو کشور عربستان و یمن و شلیک و برخورد چندموشک به‌فرودگاه های عربستان احتمال‌گرفتن‌میزبانی جام ملت های آسیا از عربستان وبرگزاری این مسابقه در یک کشور دیگه وجود داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/31425" target="_blank">📅 14:14 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31424">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aUdOIHn66LSEvv-jhX8MoZf7aQcPyTUPn-w1df6Q40_N8RVu9cOEa_KNt1NJw804Nz_3pUzs6XVSQBFgrBbjkoK6XAl4qvFJKDtO4kFlwY0i7S8biJO9SqPWZNinVTei_i4hPr3ntxAW-mF8--XtPMKI919QNSa91uFl-l-n5yyTaKPyeZWcAHhgo9glgS_VV_JBf5Bh5TfDCCPMyyk2CNXfr5m-jw_NQrwUjQFceNuTdsGSmOjwx0z1H6LQRrOhgaek0nQlpOG79D-Zkg3fQrTs5IR5UKWwN2LYy2BQnSzOW2fZfDp_eq4H3jVP1wvA2KVGAphtrQei6ML1ojRWFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
مهدی طارمی مهاجم 34 ساله تیم الوصل در اقدامی خیر خواهانه 8 زندانی در تهران رو آزاد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/31424" target="_blank">📅 13:57 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31423">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bb0f80f69.mp4?token=RZ5RqSJe1oqHXMVEwq-_tMa3KuBNuTt93ucUpuCYXGLKon3FWqCgheHuFCWhaf05s7pvnSoXQbrSGWV97gxaEuHxKI2JUKYYe4NvWFmTOud7wWzM7U_n573bBahNE4lwrxUnqIOZVjHamnO5_rBiBgF0YpiIf8gkPlF8lbHV57X85fhVYAbFnfaO8P4a21jY1TpXdIGONHVrI2pR2xPtXFm5g4Zdvb4dC7ZSkydTjhFlpGdRJjGxCSk8HV0tyUlSbal75V0Gm2HqytUePHzFnltYu3o604vTfu6mc1rpB_KzSrE1F1NqxJR1cKfvktdjLbOhoBs4GdoyghD5mDp_IYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bb0f80f69.mp4?token=RZ5RqSJe1oqHXMVEwq-_tMa3KuBNuTt93ucUpuCYXGLKon3FWqCgheHuFCWhaf05s7pvnSoXQbrSGWV97gxaEuHxKI2JUKYYe4NvWFmTOud7wWzM7U_n573bBahNE4lwrxUnqIOZVjHamnO5_rBiBgF0YpiIf8gkPlF8lbHV57X85fhVYAbFnfaO8P4a21jY1TpXdIGONHVrI2pR2xPtXFm5g4Zdvb4dC7ZSkydTjhFlpGdRJjGxCSk8HV0tyUlSbal75V0Gm2HqytUePHzFnltYu3o604vTfu6mc1rpB_KzSrE1F1NqxJR1cKfvktdjLbOhoBs4GdoyghD5mDp_IYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تعدادی از گل بخودی‌های تاریخ لیگ برتر؛ از گل بخودی‌های عجیب و غریب محسن ایران نژاد تا گل بخودی مدافع ذوبی‌ها در فصل جدید رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/31423" target="_blank">📅 13:43 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31422">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqVBrYBsHl6xrj7UV4nC-LvcXEm1rISPSZPeLwX1kbzms4bD55_96gcyFlbiKmKMLvfH61OYieMxLHOd1covTGuUJfpEd0EyL07MOnX75AsYS-mxGHLTiLEZcW6PxrzBbl5-rPhDc0UxIjEJLMedfcxqqYQZbeYt2AzaFKybeEQF9OJGmGIGVpO6Ru4cBeuctxtBaZRtRx9W4hyxonvggCibIAChRb66E_vEfE4SAvspW-zXo1LKURpxGfGZf6CMZ7zq6K09S1vOAgJEY1sSWbw5VXbR14nXWsqEFNGhRfzaFMOUuhIQpui7vgWF281i3qSpCoWOiBWfcobU2VLGTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
#تکمیلی؛ عملکرد درخشان کریس رونالدو و لیونل مسی در بازی‌های این هفته تیم‌هاشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/31422" target="_blank">📅 13:32 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31421">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/diFhJPTQ6Jp0EacLOw3CVO6qSjBPPnfjGzNnQWiY7mi9R8onERnMWXtMYZrwRGl3zfhkawczMvA0goPoygsPmBqLfY4VkxT1IYhm2kz9WbBjKZJh9Rk0ajfs_zNlpQSInmlJufMTj48m6g7t2xlHPRzKL4OIuP8mbEH7Cd6cIn_t3wJIv_VEH_VIk7trlMIlOwe2eVhnU38eFkn1MZ4T9XNIAUIB5dwmZDGMennmTNtNY9Ex4agtVx9FqKUWQ-tR4Z94Cx2v0tavTLpE8wJxfXFm3homDQEJlmm_oi_sfS5YrH8nF8dPT3os3XfaO6yhKbIRGbY-QjlyU_CvO2aRvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
کریس‌رونالدو: اگه‌کسی‌مسی، پله یا مارادونا رو ترجیح می‌ده، این سلیقه شخصیشه. بهش احترام میذارم. اما این که بگید کریستیانو یک بازیکن کامل نیست، یک دروغه. من کامل‌ترین بازیکن تاریخم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/31421" target="_blank">📅 13:11 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31420">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ekj5OY6BrRnx1vtEJo8T0e-NCV3r7qvZwoFtPFiMyfBK4VcwhMUCBxooL5sv-Fj97z06g9FzCHSPWoa5ihVI-OO4iBIC95Qke9gZo2HKosF4a8ky-fmbEg3MdyVu0blgNpFWJbp-HJJT4La_ew7YKf9gnTTow07ofSNZ5g1UBC7IZPbJfC6SR38Yz4r6gbPzvb0qi9l4015kJrOge01ojxypL31C5SVqdas8uwi5nIaIuDzZgGLUQOpCa1b2CciIw4omTytoYz0zx7egoCXmDLCKICGswD-Be_1Kr-D7ZGEYbfk2AQ66Di1ZIyFkgdkfZ7OxJ8o4mdjMnJ342dAsmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
چهار افتخار بزرگ لیونل‌مسی که از سال 2021 استارت خورد. مسی حتی‌قبل‌ترشم از بازی‌های ملی خدافظی کرده بود اما به یک باره ورق برگشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/31420" target="_blank">📅 12:39 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31419">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BXdNbg7sQybl6BKss0fYKnKT-W-9ww_nRGgIOotqiJ4-1rDd0S5ksvXJPRU4PF0Jhw5SxvSgk7RysmMLVp5-J-GuUy2rN8PuEOFjer5yJFecCgY37yCPqmDxJvVQFLzZ3ssdiVePouPhYXOHEKIygVD4zyl8e5fPsnmE7jcgF8S3x5VAOLKZ3JBTCFvmLaGly6LJvetD0ramstIsUZIRZJdyFjT85KV9iXLgSZ-hmxxOzSN6Mj7dV48HM13xutypxksTkLXhQskymt02a2Jo3RH1tQyoJJ2SlKtERxO1Hu2Jb0qBdKfDADQ2-2zWl8GBHNXCmHfBPRnRn7M_MfUo5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛طبق‌شنیده‌های‌رسانه‌های پرشیانا؛ علیرضا بیرانوند ساعتی‌دیگر باحضور درسازمان لیگ قراردادش رو با باشگاه تراکتور فسخ خواهد کرد و راهی سربازی خواهد شد. او از اول آبان سربازه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/31419" target="_blank">📅 12:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31418">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q1exESHNqgvfaW84HcEXfCnqT7P0MRpnqgIz0YfZ-kkxnhRIG5j29mIy6sgTCnyjO3mr-M5hYkgm5ifhdYkVBfoyz5jbsRnyxdeqx4SKeJHtdxe6hi1_cfsmLZylpQ0XiNnuRybarhmE6ul9JeWSoUCv_IOAhBaxJRVIBaCja1zgB_NJvcxhpPPFVCmJtRGUeIcr4Ia41-AC-eWyp1wEvuDqbd_uYMrF6r5_X1zhZAA6_EdVxewUPX7vk1ZO4zORfVT5Cn700EvKcmPswNIPC9naBIrqUh6elUx-5uxJVD91VYDj62ixLIFE8-ngHQ5O1ctNc0zlcL0yMSyECnjJpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ تا به‌امروز اوستون اورونوف، سید پیام نیازمند و محمد حسین کنعانی زادگان بازیکنانی هستند که موافقت‌خود را برای تمدید قرارداد خود با باشگاه پرسپولیس به مدت دو فصل اعلام کرده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/31418" target="_blank">📅 11:17 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31417">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p7e1BGqkQPMNd4MEU8EdMy6Hdk0Bq3IG45--T_yA0nYUgEOi78PZOWDDes4NcXiVdU7ypOIc38ChrS7f-J0lHdJnevR9FAnof2Yc2Y2texOOEPW3uFdYjaICoXvELPcbpNh90uV_jNV1FL4IyhqvEeuPp4EDKIm8Zp9u7VIYO6NGqVMYOpd2LCqrJJZqJGWtJkfkm-FdwRI39UHDI-uyQsPfYlCia4u0CJjv060W-7ToGdLZ-V9Eudplcr4f6mSFRLF6pCeo92JKfwiqF8J7YE4WbOYaLHToC4-mYRWfqgUyeAjgbjZh3M1uPTvP2BvT_vncoZ0EFr7eu0uYqpaL1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
علیرضابیرانوند خطاب به‌شجاع خلیل زاده: هیچ نیازی به فالوکردن بازیکنان‌تراکتور ندارم. من به تراکتور نمیومدم این‌تیم‌عمرا قهرمان لیگ برتر میشد. بعداز خدمت‌سربازی به تیمی خواهم‌رفت که قهرمان خواهد شد. ثابت میکنم هرجاباشم جام خواهم آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/31417" target="_blank">📅 10:42 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31416">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJ-jY01bNH5EAajahq_LfR8cO6T2G2ZdENFqMmgqzkJ70w1XGdLyq0oxKyfacdQKI4ZbrOYK19hXlXXQ_1WMWaO2TPODPbKsM9wWXZDqH2Xx3qbZnvmV52CO4aY6BqL-vkLwdI8Csshlt9iD1nxeGECBYNkCbgQvNPuDLC_-fY6F-fKYI9leUmbqwrBd4kbULcDmF-xyCHpNxmBYNFkg3JL3L9YmtMCprblFHHgiP0HZuZbBVUPCBghEFe64Refv-5mQFRN_I-UfZxXKRcbWdbwQVWBt50DVumvLlE51fnk7VzJbxjMf4ZoC0ApQFAEwVS6SFf2YmgjG1RkEiUgDCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌پرشیانا؛وکیل‌علیرضا بیرانوند که رابطه نزدیکی با علی‌تاجرنیا داره در تلاشه که قبل ازرفتن علیرضابیرانوند بخدمت سربازی تمام توافقات لازم رو برای پیوستن بیرو به جمع آبی‌ها انجام بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/31416" target="_blank">📅 10:29 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31415">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pgts6e7onI36RTuFc2_i9pb-yb0mW758RQTxMlXkqh2QvCX7qqr_YRe518VdpEilBfaQstgVbSSUWd9TQz_Za2G6tGP169eFDsnEqiW4LeF4ocWmDW-nr49IN4DEsQnOI450cAtgFJvsbDBL3CjZqBsU_i-zZOZIEjgZQiiqhwRLUrNt2IB9RP3_CPJSsMXKhFPO2cRGmKDAwnHw97VZhH2p51oq-ahG9VVLb2z97xaBk6CzomvZuCrAIhPiMIqvzywIxUMSNHdrjLzkSUjNMmWP6jrobC-XFdwmK-CRGcu19S73rb_0Tk2XE16ygo0X3rcOLkQjtwRVllw3R3he4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد فوق العاده جی‌جی گابریل ستاره 15 منچستریونایتد درفصل‌گذشته:23 مسابقه، 23 گل زده، 5 پاس گل، میانگین نمره 8.6 از فوتموب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/31415" target="_blank">📅 10:29 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31413">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8f6d230ef.mp4?token=FQ5uXe_127EffSaaWq5PS-3_U2Hu1cDUrHMTh5QVndVjBaUuh70gaSE6rgVYzazHKFv8_eJaBSeTq3X94xYY-Hs4LM6y173nsK_Hnt3d64Stzkut3a5LdC3qds-vN5PyEei758-TkgbfgwErGXhL1zUaDWCWf_X2gtB2b8r-GiVLUIVmXZFUCt-cUvxU3xmhYfu9zDMYSkWOp8ReWtPDZnlJkdqSFUhWCVb3eFeBVriOGi_LA_ORP2rsvKGl0c4gVrex724uF8YQbESKYWY_kaz1piAKQVzmhhU1V--hVaBXYkOExiNi_F-QbMa3JZeXVcVHb-MWejoob90Dw4OcOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8f6d230ef.mp4?token=FQ5uXe_127EffSaaWq5PS-3_U2Hu1cDUrHMTh5QVndVjBaUuh70gaSE6rgVYzazHKFv8_eJaBSeTq3X94xYY-Hs4LM6y173nsK_Hnt3d64Stzkut3a5LdC3qds-vN5PyEei758-TkgbfgwErGXhL1zUaDWCWf_X2gtB2b8r-GiVLUIVmXZFUCt-cUvxU3xmhYfu9zDMYSkWOp8ReWtPDZnlJkdqSFUhWCVb3eFeBVriOGi_LA_ORP2rsvKGl0c4gVrex724uF8YQbESKYWY_kaz1piAKQVzmhhU1V--hVaBXYkOExiNi_F-QbMa3JZeXVcVHb-MWejoob90Dw4OcOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
مجری‌جنجالی تلویزیون خودش از ایران رفت! زینب‌ابوطالبی‌مجری‌جنجالی«مملکت مال حزب‌اللهی‌ هاست هرکس نمیخواهد جمع کند از ایران برود»، از کشوررفت. ازفردامنتظر عکس‌های نودی ازاو باشید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/31413" target="_blank">📅 10:03 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31412">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f5075dda3.mp4?token=gXiuQatxWHOLLypmdJhwuxHm6YSMM7mQTktyz-bOORC1SJi50C54Fi6Z7I-mF_R8-r9cKjxtQGVj68NnacoChWeL9u8INkljNL8ZFfO1pQruZP5VMUxpfmDZAhgbx0vMb9ClY-he7LfYLdcb4HWWhdAIbOZTfpUUWIgVZUXj2FBSgPs9GjXd9iHCtd_tIMXnyypG6HEEpt6S6eP5oZQ7YaN1GZztQii7ZJg4Hg1RtrBXsPnMJzvhND6GWXjWn-2CuwYGJmxWjclGKh-LHQLwjNPRypbA8U_vr-DOu_UlsfDtPAcwyCFW6024hqFE6q6ZgUzM5l5EqQF9UUV6IU9sFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f5075dda3.mp4?token=gXiuQatxWHOLLypmdJhwuxHm6YSMM7mQTktyz-bOORC1SJi50C54Fi6Z7I-mF_R8-r9cKjxtQGVj68NnacoChWeL9u8INkljNL8ZFfO1pQruZP5VMUxpfmDZAhgbx0vMb9ClY-he7LfYLdcb4HWWhdAIbOZTfpUUWIgVZUXj2FBSgPs9GjXd9iHCtd_tIMXnyypG6HEEpt6S6eP5oZQ7YaN1GZztQii7ZJg4Hg1RtrBXsPnMJzvhND6GWXjWn-2CuwYGJmxWjclGKh-LHQLwjNPRypbA8U_vr-DOu_UlsfDtPAcwyCFW6024hqFE6q6ZgUzM5l5EqQF9UUV6IU9sFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نادر قاضی‌پور نماینده سابق مجلس:
تراکتور پر طرفدارترین‌تیم‌جهانه.بالاتراز رئال مادرید و بارسلونا. درترکیه، ترکمنستان و آلمان همه طرفدار تراکتورند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/31412" target="_blank">📅 09:39 · 20 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
