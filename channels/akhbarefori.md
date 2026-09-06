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
<img src="https://cdn4.telesco.pe/file/pXIkCSCivbrlut1VqJMNmvewP4iqpZNi3Fs0jd8Tn6N6e6LYD9J0ZnMkjOZ8O1mSGB1-wxx3z078K1oWKuo25hfW1cDoKmBdO8zJ172NmaukyW1ONz8eorqTK_oiZ94xQ5UPhctizKzlvG4FSldWlbsrrUoz2iUrHjjgFS5Ad7oXl9uo2jUaoTRKf9TAQ7SZFpMf4C-9TNJE6WmFvTSLe5sYHv4jZGQg3QkgZeZgIq0zxndNRYett4NRFONJqoceov0Y4UWVK-j3oiTGtHJE__aW3_VR7AylaJq07j4hI3qw8xmKwqntQZm5QvlPQ6Jd6diJiAEHjD4Vy0cxuLXR_g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.41M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-15 12:33:46</div>
<hr>

<div class="tg-post" id="msg-687617">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
قالیباف: آمریکایی‌ها حتماً فهمیده‌اند که دوران «پاسخ‌های متناسب» به پایان رسیده است؛ هرگونه تجاوز به منافع و امنیت ایران، پاسخی «سریع‌تر،سنگین‌تر و دردناک‌تر» دریافت خواهد کرد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/687617" target="_blank">📅 12:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687616">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
قالیباف:
آمریکایی‌ها حتماً فهمیده‌اند که دوران «پاسخ‌های متناسب» به پایان رسیده است؛ هرگونه تجاوز به منافع و امنیت ایران، پاسخی «سریع‌تر،سنگین‌تر و دردناک‌تر» دریافت خواهد کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9 · <a href="https://t.me/akhbarefori/687616" target="_blank">📅 12:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687615">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWj0ysw9lcoSTgHrdiQtJldfBkbth-yHr_niO19JpEcRYkIZpm3PTBhpINwU2Jdwvf5j68GgeBl1WP_xTaEtQNJrDXkcxKESDwRJ9U15wEjUkBRtcgn4xjgoSn1fnPdF5j0eAokQsKjVHSdEOG8oFXmQebwYfjbfElqiJrgWaPwHelWM06m_v-jprj5olQpS0CINaYHG9TN7TthqXoTMs9zLAvYk9ceDCtUtYjSQQvkhcFD5iXN5LKhf9ky535gR55EX2I5uJX7I0KwWNfG7TAEQUDUyyvk2jXD4eTiA60m2ZihsS2Ty1CPPeP2ef7KzZV0tAdXK0DaleMbXrYyRuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رشد بیش از ۱۲۱ هزار واحدی شاخص کل بورس
🔹
در جریان معاملات امروز ۱۴ شهریور شاخص کل بورس با رشد ۱۲۱ هزار و ۷۱۱ واحد در سطح ۶ میلیون و ۷۲۳ هزار واحدی ایستاد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/akhbarefori/687615" target="_blank">📅 12:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687613">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PyDQanKOFBKJRBTZK-SRvhFkc5Sk8Q_8R33caNITDm6OqiPeFWl7oZAdaNavDixQHgVTJbSf4GNASC6eazHkjWztwM_vGKLjZb2efwCR2TRAWQCgPDWClx4G7nH-8rOd44O84BOI6IUDjjx4cCXJ-6Gs-J_47f5wYRclLmSWdF6opPnjFK_VcSHIASF97sQMIF7GKQQafRLvzt0QfW3UDeG8dcB_CM0F-uRuducU9BaguCuZjR2SDnBzGU-cisg-p_68hnxLwPeyy3l_Wfi9HF5Bu_lx5_t9b0oPcwG8aQ1mqfTXSdZaXxX8aNfo806SGJ1yruv3rGuSS7_WEPQo9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q02U99VTxsq9XVNbK7totlPv7mnxes0yin4FP9NUgaH1Vtww_J2eMLBJtOqz_Xih3pF7rXai1s9ZYisk_77wYmimYAjmMENwQpO4Mphgp4NRcl-plQgDGUyeTHkcXZdzncLPoxMGzy5hfJTkxqlo5G4XFz8AIcNTbPFJZI3Qv5V9l3jQDI_vNFvyUmBvuOSDLqay4uncHqD8kb5yOIbq6eJ9IJFHBRLHdxXEKBFzCVMSsn-JqeVBc2PvLQ68STGSicT_4fqvSGp05BeIEVrRKWCMbYNHONUwTUY1LvhnI0Vkq49SHG-jAX8j1NTqgp_a19gwkjZub34_7VtTjBbCGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
سرعت عمل در بازسازی پل‌های بمباران شده در جنگ
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/akhbarefori/687613" target="_blank">📅 12:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687612">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
وضعیت سربازان آمریکا در تایلند
🔹
پس از توقف ناو آبراهام لینکلن در تایلند، تصاویر متعددی از وضعیت نامناسب سربازان آمریکایی در تایلند منتشر شده‌است.
🔹
سربازان آمریکایی که ماه‌ها در‌ ناو لینکلن در وضعیت نامناسبی بودند حالا در خیابان‌های بدنام تایلند باعث رسوایی…</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/akhbarefori/687612" target="_blank">📅 12:24 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687611">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cTj3sciWmSRn2rJgBaz91Pf-veBjPRomh-reQCTldTi6i8XjNPAd_VLTPfr8QF4cdmm6_dyekkNLngDiHkR2m5UOGmqA_BXLCoePsAitpj-_PoxBysXm1Gw2lVhR102gt5VKjDhvI1fq55jjg66en-JOagaW450dWK9QnhL-XeelpI2HBg3VAeV2bcNyekYmAhiy6Zkx-jzRLRFQw6gIxz9TSWLHEzwWOtz1sXB_82s6KEs88xL64OHje7i0RYd6JcoN1Rd6gi7QHkbcO5cFRo_F-FwLioO_MkKL8q2SR4O0vHYO5ryzgtVMsJfD-J15pH2dlyqeWJrhbCwXUTm8uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر نیرو: تلاش می‌کنیم قطعی برق متوقف شود
🔹
این درحالیست که وزیر نیرو روزهای اخیر مدعی شد قطعی برق متوقف شده اما همچنان خاموشی‌ برنامه ریزی شده پابرجاست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/akhbarefori/687611" target="_blank">📅 12:22 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687610">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d334b1bd6.mp4?token=D5ftqbYZhUIwbPCdJSmtGrDtBSO4IX2DSAFwlRqNJ0Lp_NJlgQM0akcsQC1wH-GL2jK8GcE82yKKvphMFYSeBkadPA9VqTqga-DVdFHPYVGmKLqP-1U7jXWNMTvhokUbRXWsk_EqHUMEiBhf46zXd5M2YqY9syXOd0ONqbUC7SATPBYYa9oLFbcHPUdQEGqWXmQglLrifkKBo5g3IBhwKPFF-JT8n4cOoZ4WBsNZEkzmbZAboRBRTtd5QHkfUNoLwkmrcHWJ0L0GDd-7Q91QtQdtelq9h1KKeWR9fBY9j7FZQgayUu7XBVtcmJaz7maDPv43xZhqY35lH_o9F7BcZk4QBggoLWd6Gh6_3vaaCyo6ROVI5OEVw4yQ57MhsHLguXAdaZMgH7kL8Mzma-w-7usmZwT8w3QLogB3BRcVLevw9n09TU2FjyqHdVElhqjDXslTe8ZSPow7GqS1PzYsafOGnajjKHK3sVmAoSf1uI4EUImLNpzL1KD1UFUxSLiChzgEachfD0RtQW_DC-zek8XW7xDrK0pZ7lLtrit7-K8YvbZTG1YdR6jyfCNhv4blTAbtBzfBcnf11DArhhbm2YWNYcoDn3Kywda5rxR0A3-4JLAHjO7B1iBWNp35j4pHxRelWwjuSTDeQmgbBjMA_seiymNPhjq9dpWV3zJSVgE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d334b1bd6.mp4?token=D5ftqbYZhUIwbPCdJSmtGrDtBSO4IX2DSAFwlRqNJ0Lp_NJlgQM0akcsQC1wH-GL2jK8GcE82yKKvphMFYSeBkadPA9VqTqga-DVdFHPYVGmKLqP-1U7jXWNMTvhokUbRXWsk_EqHUMEiBhf46zXd5M2YqY9syXOd0ONqbUC7SATPBYYa9oLFbcHPUdQEGqWXmQglLrifkKBo5g3IBhwKPFF-JT8n4cOoZ4WBsNZEkzmbZAboRBRTtd5QHkfUNoLwkmrcHWJ0L0GDd-7Q91QtQdtelq9h1KKeWR9fBY9j7FZQgayUu7XBVtcmJaz7maDPv43xZhqY35lH_o9F7BcZk4QBggoLWd6Gh6_3vaaCyo6ROVI5OEVw4yQ57MhsHLguXAdaZMgH7kL8Mzma-w-7usmZwT8w3QLogB3BRcVLevw9n09TU2FjyqHdVElhqjDXslTe8ZSPow7GqS1PzYsafOGnajjKHK3sVmAoSf1uI4EUImLNpzL1KD1UFUxSLiChzgEachfD0RtQW_DC-zek8XW7xDrK0pZ7lLtrit7-K8YvbZTG1YdR6jyfCNhv4blTAbtBzfBcnf11DArhhbm2YWNYcoDn3Kywda5rxR0A3-4JLAHjO7B1iBWNp35j4pHxRelWwjuSTDeQmgbBjMA_seiymNPhjq9dpWV3zJSVgE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شعله‌ور شدن موتور هواپیمای مسافربری کوآنتاس در نیوزیلند
🔹
هواپیمای بوئینگ ۷۳۷-۸۰۰ کوآنتاس هنگام پرواز به سمت کوئینزتاون، پس از مشاهده شعله از موتور، مسیر خود را به نزدیک‌ترین فرودگاه تغییر داد؛ حدود ۱۵۸ سرنشین داشتند و گزارشی از تلفات منتشر نشده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/akhbarefori/687610" target="_blank">📅 12:14 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687608">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a159a5bee3.mp4?token=PFP9RBMoaYLfFZQ4cWGn4AZyXg3sn-WsF1WgVsgE-YSYspQcYEONlnCYqtdSfzN9Nt8PUTAxbf2263TokVU5oIU-kjPRc4WqxDXv70OE82MIPKAMGK5KX1zBSLUalH5MGoelyo6lDlvnE7scJtg-YTEjVbz_hgKV-5uRi0k6fRnxdKcxiN9zoNx4fnGAUlBqL-QxJ3rr-I8tQV55tMMFh3ZFa3rvftOcnbTgBSH6tGalTOHe07L7qYRn2eSdHANvMOUCxWSF42XB8RqInvVqNdUJNAqHmlKfnxAIqXFAvAKjYg2g-kZ0Y5AjaTuLnByzmTQjBQUc_iRvVT3VG_ztdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a159a5bee3.mp4?token=PFP9RBMoaYLfFZQ4cWGn4AZyXg3sn-WsF1WgVsgE-YSYspQcYEONlnCYqtdSfzN9Nt8PUTAxbf2263TokVU5oIU-kjPRc4WqxDXv70OE82MIPKAMGK5KX1zBSLUalH5MGoelyo6lDlvnE7scJtg-YTEjVbz_hgKV-5uRi0k6fRnxdKcxiN9zoNx4fnGAUlBqL-QxJ3rr-I8tQV55tMMFh3ZFa3rvftOcnbTgBSH6tGalTOHe07L7qYRn2eSdHANvMOUCxWSF42XB8RqInvVqNdUJNAqHmlKfnxAIqXFAvAKjYg2g-kZ0Y5AjaTuLnByzmTQjBQUc_iRvVT3VG_ztdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگه میخواین رابطه‌تون طولانی‌ بشه و ده سالگی خودش رو ببینه، قول بدید این پنج نکته رو‌ر عایت کنید #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/687608" target="_blank">📅 12:03 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687607">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدمـاتجهيــــز | Damatajhiz</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d57d3af292.mp4?token=tu4kPl2QbjWJAkm-Mh5wCIrK1BO7_XqPJ0AsJtWU2NlY6P0I04Y6Xk2abSiKVTy7vKuRiP52lwoDw1AOf2t8Op-Y27YB8jVFUGt_6JTsz5d_95Dn4XpCvfbpd64f91d2bFvw8O0o__m3I4s3WJ6UB_2VJMUlz5pV0ajU4lE-kGEqfs0XIzJIBJvN6yfcY8U1KWMGk2rmXF6M_GGy5mKxgHwT0PBYulwMBhGLzOc7CQ5wiEDiINJtZehXbhtBnPMO3p9_6TMONwHm7T6EBEyGPi3vs-cgIt3UKuLE2RvhHsUnEH7uhkDEQrpQmes1fPxQHepxojrhA1Kkp-0_zrZldA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d57d3af292.mp4?token=tu4kPl2QbjWJAkm-Mh5wCIrK1BO7_XqPJ0AsJtWU2NlY6P0I04Y6Xk2abSiKVTy7vKuRiP52lwoDw1AOf2t8Op-Y27YB8jVFUGt_6JTsz5d_95Dn4XpCvfbpd64f91d2bFvw8O0o__m3I4s3WJ6UB_2VJMUlz5pV0ajU4lE-kGEqfs0XIzJIBJvN6yfcY8U1KWMGk2rmXF6M_GGy5mKxgHwT0PBYulwMBhGLzOc7CQ5wiEDiINJtZehXbhtBnPMO3p9_6TMONwHm7T6EBEyGPi3vs-cgIt3UKuLE2RvhHsUnEH7uhkDEQrpQmes1fPxQHepxojrhA1Kkp-0_zrZldA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥇
دمـاتجهيــز؛
انتخـاب ،قیمت ،تامین و تولیـد
تجهیـزات تهویـه و تاسیسـات با
اصالت
گارانتی
(از سـال ۱۳۸۳)
داكت اسپليت
+
ارسال رایگان تهران
كولرگـازي واسپليت
+
نصب رایگان
👌
فن كويل و تجهيزات كنترل
🏊‍♀️
استخــر، سونـا و جكـوزي
🔥
دیگ و تجهيزات موتورخانـه
☕️
تخفيف ويژه
دمـاتجهيـز تا
15%
- انــواع ايـرواشـر
- بـرج خنـك كننـده
- چيلـر و ميني چيـلـر
- زنت آپارتماني و صنعتي
- هواسـاز آپارتماني وصنعتي
🌎
www.DamaTajhiz.com
☕️
☕️
🙏
☕️
☕️
021-88822550 خط ويـژه
Join
🆔
@dama_tajhiz</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/akhbarefori/687607" target="_blank">📅 12:01 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687606">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMBxxuJnEzLksBSMCu7W-fnZ9fk-2_PWPbMFdRKNSUcfC5koELlAmRxZQB5UV7npGZq1ShEmGgBf5m7G5Kuep4h2bXljqAfNyOqk3tR93BavNlemvsgQSHrsr0bbi5tQZWBplLsyA83D1--GluuIchLteqF-qn_gyQmMNToBxJiSek6bYqV4LahCu7GZRjD6RayIOLgFznarhKU3Jr4RZop0gswjzAIGbI5rdpOoQcEBH0jEEH-5j2LczRiHKGe7mHXmI-wdfBFwrWyIhejXrRDQ_NpO9In4PyxmhbwNwoFbdVkdn4MqPYeSqo0F5Y3nPYslZ40KMxKeiMC5At6CAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فوربس: هزینه‌های جنگ برای آمریکا بعد از جنگ هم ادامه خواهد یافت
فوربس:
🔹
هزینه‌های جنگ‌ها به ندرت به طور کامل محاسبه می‌شوند و جنگ فعلی آمریکا با ایران نیز از این قاعده مستثنی نیست.
🔹
حتی اگر این درگیری فردا پایان یابد، هزینه‌های پس از جنگ متعددی وجود خواهد داشت که برخی از آنها طی سال‌ها و حتی دهه‌ها ادامه خواهند یافت.
🔹
حتی اگر توافق تنگه هرمز حاصل شود، بازسازی ظرفیت تولید نفت آسیب دیده در طول جنگ، تأثیر ماندگاری بر قیمت‌ها پس از پایان جنگ خواهد داشت./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/687606" target="_blank">📅 11:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687605">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
وزیر جنگ رژیم‌صهیونیستی: تا خلع سلاح حزب‌الله از منطقه امنیتی لبنان خارج نمی‌شویم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/akhbarefori/687605" target="_blank">📅 11:46 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687604">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
چند تخلف تا توقیف گواهینامه؟
رئیس پلیس راهور تهران بزرگ:
🔹
سرعت غیرمجاز بیش از ۵۰ کیلومتر، ۱۰ نمره منفی و سبقت غیرمجاز در راه‌های دوطرفه، ۵ نمره منفی دارد؛ تکرار تخلفات و پر شدن نمره منفی، به ضبط گواهینامه و ممنوعیت رانندگی منجر می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/687604" target="_blank">📅 11:43 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687603">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xhp5KYORTFO2wRfhEldRxLT8QUT007FRkhdkRi6e7iQ4vgC5zyrSOFxAM9f_C-qX35cc24dA3va3mbzbiDzRlq3coVZWI6Xt5eeiQ8Yg1NACT09saMsgk7fkwOXPPSVR-lQzHBWH2J1zFCl3-XSOYwBDJqGUVpaPHDq-dwBM_sJN25Pke-L9YBGe6t7bkWOT6RuPcadHlO_WGprQbNpY26Hsg33Rbwywwc1T3jS1_VkNOqAxBzx_5Zq8WZX0snbpupZVpnwO_ic9VVJUiOWQoQPS-lXWkulUtuGKzzYBISIY47_ix5aBeiVNtSHfcDCF0QwC3rlw8vEU-9eQ7rloWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صاحب این طوطی که توانایی پرواز نداره، براش یه کوادکوپتر گرفته تا هر روز چند ساعتی باهاش پرواز کنه
🦜
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/687603" target="_blank">📅 11:26 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687602">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
صادرات طلا و جواهر ایران تقریبا به صفر رسید
حجت شفائی، رئیس اتحادیه تولید کنندگان و صادرکنندگان طلا، جواهر، نقره و سنگ‌های قیمتی ایران در
#گفتگو
با خبرفوری:
🔹
به دلیل تحریم‌های فلزات گران‌بها از دوره اول ریاست‌جمهوری ترامپ، عملاً صادرات طلا و جواهر ایران تقریبا به صفر رسیده است و در سال‌های اخیر، صادرات بسیار محدودی از اصفهان و تهران انجام می‌شود که در مقایسه با کشورهایی مانند ترکیه، ناچیز است.
🔹
جواهرات و سنگ‌های قیمتی نیز عملا صادرات قابل‌توجهی ندارند و مشکلات داخلی مانند ناهماهنگی بین استاندارد، گمرک و بانک مرکزی نیز به عنوان تحریم داخلی بر این مشکل افزوده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/687602" target="_blank">📅 11:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687601">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
فهرست شناورهای متخلف در سایت «نهاد مدیریت آبراه خلیج فارس» به‌روز‌رسانی شده است  متن کامل پیام پی‌جی‌اس‌ای:
🔹
فهرست شناورهای متخلف در سایت به روز‌رسانی شده است. برخی از این موارد با اطلاعات داوطلبانه مردم به دست آمده است که پی‌جی‌اس‌ای مراتب قدردانی خود را…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/687601" target="_blank">📅 11:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687600">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oAcMgBuKPYkBl3cH0t00nw-fronYJSbTsEHuI6Wx-1xq4WO7uV7KbNcbQnmtYUlH1Xpm90cBAGeUrekKQKfAZkklzaYUwM8PJS07bclgE7W2JV8AM2_pVKCcMCt6XNIFq27ZduEcK1geiYjC6Kycskoxr1Ms_GMRXqmeGX8ee6OwUbgt-4c2Y7Ty2zbBDcv2ll5IbkgujpgB1pj5xeEeCz4x1vaLkgFriQSPn6o6Mkcyr75xjMOZAS-Ypsre2ItDhP9FbbqUU7gRGlfA_vWRwk4_F0bDIdD1CWfKUMDNFodJ8hhiXqN0cJ0kuKIDAckzF4JVB2PwX2I6Hs_PGPGBow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استاندار کردستان در پی انفجار تانکر سوخت ۲ روز عزای عمومی اعلام کرد
🔹
در پی حادثه دلخراش انفجار تانکر حامل سوخت در محدوده پلیس‌راه سنندج ـ همدان که تاکنون منجر به جان‌ باختن ۱۱ نفر و مصدومیت هفت نفر شده است، استاندار کردستان، ۲ روز عزای عمومی در استان اعلام…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/687600" target="_blank">📅 10:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687599">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QpUWp-L_UAladNOXMYvL2ORYNz8mlKKAMTtSSycsTxxqwUqMoTNzghHGGC1usEjDtorK1lEgXz0EyTg5RoFkFF4tSSSfJVf6LTXKuP4kztZRujDUPG7Fxof0FVhjcYf01Jc_KCvvLafzg4iRWk3S2BD-w0wKapAoaQ5UZbSYY9g9qgRFG6ZPSHzdgv2Sm0vFcNih1g5KFE9IMn-_Ac8-x9nTbaBVqFgbQAdWA-qJ-6QHnwFaq9sa2c1KcmB6JM-2_RXqRU39zgdon8U48RInltl9gTwA5Et3r9Ug9Fc5jVAcGpd7o-2XHqGOF7UaIpjSO4dQCQ7xE8qlYB7JaWxioQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تحلیلگر آمریکایی: فشار اقتصادی ایران، در نهایت به تسلیم آمریکا می‌انجامد
‏برت اریکسون:
🔹
درد اقتصادی فقط وقتی مؤثر است که به تسلیم یا تغییر رژیم بیانجامد.
محتمل‌ترین سناریو: رنج کوتاه‌مدت برای مردم ایران،
سپس تسلیم آمریکا و دادن امتیازات اقتصادی کلان به تهران.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/687599" target="_blank">📅 10:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687598">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29a7f5d352.mp4?token=LQZwUKYQY7A-g48ieyODCbsNVtwY5Zm1EVL_8h_ZLoBMkat3S-bzqfW5wv4ibOlR6nU96W-O2WphluK1Qr4n2o_rwY-XXmYvm3LXzDPvCJ0uPMoLXSzwEhSK7gp5AfXOnO1aR1LAnDF8isjtSAQ8WO8N0E8pNz-WyMTjDnhexDaq_GMuNWk646363fOKW6UpXp8jV7vjx7hD21yVL2TLWJH5CXG_D_SjgRvlKYkc-XkB6k9OnUhxJEM_xAmBuBrBE5Z_Z-ARsaBYW8mIaFU620J-IPTdWaqkwrP9NdfaZLR7l1Pp3Bx3assZwXnPSYTL6OiXXF7ZTObNG79qfbD7hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29a7f5d352.mp4?token=LQZwUKYQY7A-g48ieyODCbsNVtwY5Zm1EVL_8h_ZLoBMkat3S-bzqfW5wv4ibOlR6nU96W-O2WphluK1Qr4n2o_rwY-XXmYvm3LXzDPvCJ0uPMoLXSzwEhSK7gp5AfXOnO1aR1LAnDF8isjtSAQ8WO8N0E8pNz-WyMTjDnhexDaq_GMuNWk646363fOKW6UpXp8jV7vjx7hD21yVL2TLWJH5CXG_D_SjgRvlKYkc-XkB6k9OnUhxJEM_xAmBuBrBE5Z_Z-ARsaBYW8mIaFU620J-IPTdWaqkwrP9NdfaZLR7l1Pp3Bx3assZwXnPSYTL6OiXXF7ZTObNG79qfbD7hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درخواست دوباره دختر موشک صورتی از سردار سید مجید موسوی در برنامه محفل ستاره‌ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/687598" target="_blank">📅 10:50 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687597">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fpHHTEw_AZQKVLHqHbiUTm7DEJPYmEcGuWcf9n7myOBEMdUAndAfqx1MuRwh2YjYMJCnYQSmDuRMGooXWEmRanZBsrJ1He2vNP8aEi4zCudpXWjaLAJvnbszyPpTLMDxGVeoT8nCK4b8ssoe71lmprlz7ZIBuX1rnjhy8BaFlwb3kzpSVlrDMiNH0lhFF3Wxb3wd-KwSFA9THtIoAnnbneO8WaVge_BVCSx6sCBt6gxHLy5pUf_vyx9Y3oZkL70ZxYJrzARKoYnyRxb3TGR3lI0B5-81obT9LpbhCFwFjR67eM7bgrxI_fQ_3V3qdp8D59ntEr6M_FzolzupnQEsvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای آژانس اطلاعاتی آمریکا: ایران مصمم به ادامه جنگ است
الشرق الاوسط:
🔹
بر اساس گزارش‌های اطلاعاتی آمریکا در هفته‌های اخیر، ایران نسبت به توانایی خود برای حمله به اهدافی در خاورمیانه اعتمادبه‌نفس بیشتری پیدا کرده است.
🔹
به نظر می‌رسد ایران مصمم است این درگیری را برای ماه‌ها ادامه دهد تا ایالات متحده را با چالش و فشار مواجه کند.
🔹
حتی در صورت نبود اختلالات جدی، حملات سایبری احتمالاً همچنان برای ایران روشی جذاب خواهد بود تا از طریق آن حمایت افکار عمومی آمریکا از جنگی را که از ابتدا نیز محبوبیت چندانی نداشته است، تضعیف کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/687597" target="_blank">📅 10:47 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687596">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09f0ea32c5.mp4?token=K37zu_EQu87p8NhFzCcKnFTckArEvir5ChBnSNpJWd_Jigh48hSfhYca3HYhMR0hgFrF82QM-s7-DH6opNk7psNQT5aR98sfvjOzkZdVl6hB5j4kAbKNMadOPat8GOaAHgdhzjuRH-PuEkWxh1tHXsxRyQDuyqlHU9kRTIqHKuMre9Syxi4JHB17tZamQM8tiIXF2Y5CsxHQvqjE7KybpzjGnbT3ojdlp1Ht8MHZYNY5whREtdDfoWQsgjEoXstU7hh_jQptp9nW0JVkofeRhDQfhv_Obsi6yNcB0SJcQwAYnnh_ngNrYfacLaGIJSqQ38s64Vht1BzLpmCgZ4DsWSj46DnFoEAZjyZocb8LKsY4KXB58exiUZatHBhk00ddMIxnjaQd8aW7g-A2oVctx-IQ2WiiSMRer95C4bhzhS2QB59ctbVhWYEfyQkMgMgJA4tjsw9hqT7g1V7PMCbv4iv2uJfQESlhEJcD4HCwu1Do7i8J3E6k6sdpVkyEWwQPFa6paqoEBQpnAE-HPKSZOFID1N0h7cwMjlxFNN9nHaWY1KZIy-bSP6rxAGOP6UQ1teUC6fJVUyGNxjHKH8eoMEZljR22bBbNjIFBQi5yIcRU1EPO1P3OixliS27ANTv_YHh2CQn9pkqDtLZSiMOGBRevQParH1we01RdPl5ZKLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09f0ea32c5.mp4?token=K37zu_EQu87p8NhFzCcKnFTckArEvir5ChBnSNpJWd_Jigh48hSfhYca3HYhMR0hgFrF82QM-s7-DH6opNk7psNQT5aR98sfvjOzkZdVl6hB5j4kAbKNMadOPat8GOaAHgdhzjuRH-PuEkWxh1tHXsxRyQDuyqlHU9kRTIqHKuMre9Syxi4JHB17tZamQM8tiIXF2Y5CsxHQvqjE7KybpzjGnbT3ojdlp1Ht8MHZYNY5whREtdDfoWQsgjEoXstU7hh_jQptp9nW0JVkofeRhDQfhv_Obsi6yNcB0SJcQwAYnnh_ngNrYfacLaGIJSqQ38s64Vht1BzLpmCgZ4DsWSj46DnFoEAZjyZocb8LKsY4KXB58exiUZatHBhk00ddMIxnjaQd8aW7g-A2oVctx-IQ2WiiSMRer95C4bhzhS2QB59ctbVhWYEfyQkMgMgJA4tjsw9hqT7g1V7PMCbv4iv2uJfQESlhEJcD4HCwu1Do7i8J3E6k6sdpVkyEWwQPFa6paqoEBQpnAE-HPKSZOFID1N0h7cwMjlxFNN9nHaWY1KZIy-bSP6rxAGOP6UQ1teUC6fJVUyGNxjHKH8eoMEZljR22bBbNjIFBQi5yIcRU1EPO1P3OixliS27ANTv_YHh2CQn9pkqDtLZSiMOGBRevQParH1we01RdPl5ZKLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تودهنی فرمانده سابق سنتکام به مجری صدای آمریکا!
ژنرال دیوید پترائوس:
🔹
شکافی میان نیروهای ایران وجود ندارد؛ رویای فروپاشی حکومت شکست خورد و استقرار پایگاه‌های آمریکا در منطقه جواب نداد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/687596" target="_blank">📅 10:35 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687595">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
پرداخت معوقات رتبه‌بندی بازنشستگان ۱۴۰۰ تا ۱۴۰۲
سخنگوی وزارت آموزش و پرورش:
🔹
پرداختی‌های بازنشستگان سال‌های ۱۴۰۰، ۱۴۰۱ و ۱۴۰۲ پرداخت شده؛ مطالبات تعدادی از بازنشستگان سال‌های ۱۴۰۲ به دلیل کامل نبودن فایل‌هایشان پرداخت نشده که طی یکی دو روز آینده پرداخت خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/687595" target="_blank">📅 10:22 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687594">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/puBmhRjXaUzmTJhGBhHi0HgGsG-2XjklBiZxTW0r7MvOXD6w_0OcefXEhnV94MQi5r3xwbKBVBcoshZ9_kLbHxEsyOw4KQdJ4OakDpglcD7xshyE_QPoyqWd7qad9Z912cUEpfwQ8BCOSXVzfL7WcT9_LnGHY3xTcfZoN2kUrtwRUYlwbbYwwc5_P11YL0SWgbRUH5BQsHrSFXnSP8LhKd_MLkQ5Jhyslzrh4cOA7WXLNWaN9-JWmXfuiEEbsav91rKEXWHLgjY3xiVSYThkA_6ocjJiqM6pb5AfgpsOVD_C9FpbAI_Oom-LScInq-RnaekVFPTJTlCRdv-bPX1Dew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راهنمای پلاک شهرهای ایران و نماد هر شهر
🚗
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/687594" target="_blank">📅 10:19 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687593">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
ثبت‌نام ایران خودرو برای ۱۳ محصول برای متقاضیان خودروهای فرسوده
🔹
منتخبان پس از دریافت پیامک، ۷ روز برای تکمیل وجه فرصت دارند و خودروها نیز حداکثر ظرف ۹۰ روز تحویل می‌شوند.
🔹
نکته مهم اینکه این فراخوان ثبت‌نام عمومی جدید برای همه متقاضیان نیست و فقط شامل افراد منتخب دوره قبلی می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/687593" target="_blank">📅 10:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687592">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
خوراک لوبیا رو‌ به سبک آشپزهای حرفه‌ای درست کن  مواد لازم برای سه نفر:
🔹
لوبیا چیتی ۲/۵ پیمانه
🔹
سیب زمینی درشت یک‌عدد
🔹
پیاز یک‌عدد
🔹
رب دو قاشق غذاخوری
🔹
نمک، فلفل، زرد‌چوبه، پودرسیر، گلپر
🔹
عصاره گوشت
🔹
قارچ ۲۵۰ گرم #آشپزی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/687592" target="_blank">📅 10:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687590">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54e0b143cc.mp4?token=MAVYm9wbFkZLMm_UkU2lN47f0kGx_y-GPUcgO-1L8IETqAkWhfl7wWg2fIx7YPqLilmd3cGZouIO3vFki-JSUuJZ8PWShw-1_MLLqTD6F1U19FzJ6Dzq38zNYiZrNA6_0KCQnViAPipuGu1oQO0tQJfo2O1Zs-Muv7IXGiHZrbwhqF0Ufw5JXGdoLxXFADgnTa5c8fFm7esYsVnaGic8_EEXBDhfpgsDbGl4wlXD4On_S8R7kbsh_Wt2o5s37A_VVIC9htPRre8YFLkEPaBlzIn9HeX-LpF--0otEUhNo-Pmwg1rb8wqWfAXuFFqB1yBlP-HG1GyyiLmb6SENko2zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54e0b143cc.mp4?token=MAVYm9wbFkZLMm_UkU2lN47f0kGx_y-GPUcgO-1L8IETqAkWhfl7wWg2fIx7YPqLilmd3cGZouIO3vFki-JSUuJZ8PWShw-1_MLLqTD6F1U19FzJ6Dzq38zNYiZrNA6_0KCQnViAPipuGu1oQO0tQJfo2O1Zs-Muv7IXGiHZrbwhqF0Ufw5JXGdoLxXFADgnTa5c8fFm7esYsVnaGic8_EEXBDhfpgsDbGl4wlXD4On_S8R7kbsh_Wt2o5s37A_VVIC9htPRre8YFLkEPaBlzIn9HeX-LpF--0otEUhNo-Pmwg1rb8wqWfAXuFFqB1yBlP-HG1GyyiLmb6SENko2zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مدل GPT-6 Astra معرفی شد؛ قدرتمندترین مدل OpenAI تا امروز!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/687590" target="_blank">📅 09:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687587">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kTP_5owZzH0UGYKdjSmqWclcxEbqOCAKtbvbzBSN4iPPmdCpoAyVAGz9EGvn7Y3bTOaWSwIPIvktGWvVmRngCqPqQbj3iGIAwZ7kQ_by_WJIzRBQiwkh8_oKO6cIpkEovy6Oat5vlcO3eZJYlyfTFeF1CAon3ZpH11cGZcl5uD6mjZKdCVqwR8j1mPpYZmauMvRl4nsc7dWORt5Cu7NAyHS8cDHct2VbCD43y8xphH-wfrzy8tWzksGDzEiUCjoL3TJLO2MvF02CWZl6vsOX7OarGF1JfVAFQ9XHObyNK40JtK-ogZdJRSL7oeJOMXO_23GiZrCTyJmwYwomTY1GCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رویترز: آمریکایی‌ها در تعطیلات آخر هفته با افزایش بی‌سابقه قیمت بنزین مواجه شدند
🔹
در آمریکا در تعطیلات بنزین به رکورد ۴٫۰۳ دلار رسیده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/687587" target="_blank">📅 09:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687586">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24a5b67fae.mp4?token=M9NHYSQc_maNw0RfW0kpZPMWnM6wcTO75Gwpam2sUmbro8H5wXNhuP58NmbCSq8NGAmDejfyGD8KGNum75Ko3hTSbYvWudapGLeNYE-E7fZ8fhFtSpU2M3HrD_UH4l2k_el4tb1M-OZ4xeCVsLR_1-uaer99336eqeA2i7VwMWoemxu4YmYY-09dJvRFTe035cVglnePrICvxd4Cp99kkQaWCkgSX1hnR50-G8iaUwpcmYiG801z1fvBLnh7C3dikOICd3nSgXDkvoGJ0EhNDzeSTOQKnlPy3EsWLWKp0tRzxbfj038MEjWKY60QLr31bJj0HPxyq96RYMUl34sKrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24a5b67fae.mp4?token=M9NHYSQc_maNw0RfW0kpZPMWnM6wcTO75Gwpam2sUmbro8H5wXNhuP58NmbCSq8NGAmDejfyGD8KGNum75Ko3hTSbYvWudapGLeNYE-E7fZ8fhFtSpU2M3HrD_UH4l2k_el4tb1M-OZ4xeCVsLR_1-uaer99336eqeA2i7VwMWoemxu4YmYY-09dJvRFTe035cVglnePrICvxd4Cp99kkQaWCkgSX1hnR50-G8iaUwpcmYiG801z1fvBLnh7C3dikOICd3nSgXDkvoGJ0EhNDzeSTOQKnlPy3EsWLWKp0tRzxbfj038MEjWKY60QLr31bJj0HPxyq96RYMUl34sKrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ارتش تروریستی آمریکا ویدیویی از غرق شدن نفتکش ایرانی در دریای عمان منتشر کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/687586" target="_blank">📅 09:26 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687585">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ef115f097.mp4?token=Y52ydwx24Elb8HAHkMyzZFMIjIRwSOkUNVyQcEgwhIpAHDROrCBy5NEJfswdDVcNKF0KVERRZOXWZD0YlWmVnGAwuIeiHDEyHuwvxEEs7D9j2oaanNrsr0obOB0jf6ovXR1MiXHurcdO_Fe50bVa7QU6-dZGUxebirnSLw2jyKDpykRRiw82HRFetSkfXX8upuCVzXyVbFo6dnwkeEBobjc0GufK0bpGrC9aMwKqClSCbdqNjPQ1EW39D94Pc3T94FMwPIt-qUezc9PYKPpNX9ur1D5VzAZknHCPLREIFeyOfu0IM8Jp86biAnWqMIznANtm3RrHFddbYyFQ6lOdHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ef115f097.mp4?token=Y52ydwx24Elb8HAHkMyzZFMIjIRwSOkUNVyQcEgwhIpAHDROrCBy5NEJfswdDVcNKF0KVERRZOXWZD0YlWmVnGAwuIeiHDEyHuwvxEEs7D9j2oaanNrsr0obOB0jf6ovXR1MiXHurcdO_Fe50bVa7QU6-dZGUxebirnSLw2jyKDpykRRiw82HRFetSkfXX8upuCVzXyVbFo6dnwkeEBobjc0GufK0bpGrC9aMwKqClSCbdqNjPQ1EW39D94Pc3T94FMwPIt-qUezc9PYKPpNX9ur1D5VzAZknHCPLREIFeyOfu0IM8Jp86biAnWqMIznANtm3RrHFddbYyFQ6lOdHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا تاکنون وصیتنامه‌ای از رهبر شهید منتشر نشده است؟
زاکانی، شهردار تهران در جمع دانشجویان:
🔹
متاسفانه، تمامی کتاب‌های کتابخانه رهبر شهید در اصابت نهم اسفند ماه از بین رفته است.
🔹
حالا اینکه وصیتنامه در کتابخانه بوده یا نه فعلا از وصیتنامه خبری نیست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/687585" target="_blank">📅 09:21 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687584">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19fbb61dc4.mp4?token=ag8VQGtMs1OxaM1yLk3l1GmeyMDX43vT4IsWY-fDXCzM4RvETiO_n-u-E6FltMznU1cCrHYR7L4ArIb_sjEX1WuQTrigdUXOtw8h-6CQhHo5ghPAiB1Zuk-ihruwIsOg523DrVlqkZ6tSgfqyxVCMwVLoOc58b8Bd8eJHJh9wNCl409WPFbORjM5mUqzfDyaM1uBvadANAFmYNhPaCc2q3JSuRTIbiPyb7lZv5AnNq9VLkauRmcn1SuhydBb88DGJxpib_pI47rH0glJk7v-gsISBX1FXQtVcY2DHS8_j08iOcZymUqkt_x0EFzKCq6e34eckA3Iz5eaemmQSqAMeIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19fbb61dc4.mp4?token=ag8VQGtMs1OxaM1yLk3l1GmeyMDX43vT4IsWY-fDXCzM4RvETiO_n-u-E6FltMznU1cCrHYR7L4ArIb_sjEX1WuQTrigdUXOtw8h-6CQhHo5ghPAiB1Zuk-ihruwIsOg523DrVlqkZ6tSgfqyxVCMwVLoOc58b8Bd8eJHJh9wNCl409WPFbORjM5mUqzfDyaM1uBvadANAFmYNhPaCc2q3JSuRTIbiPyb7lZv5AnNq9VLkauRmcn1SuhydBb88DGJxpib_pI47rH0glJk7v-gsISBX1FXQtVcY2DHS8_j08iOcZymUqkt_x0EFzKCq6e34eckA3Iz5eaemmQSqAMeIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یووال نوح هراری، تاریخ‌نگار و نویسنده‌: پول از میان می‌رود و نظام مالی مبتنی بر هوش مصنوعی جهان را اداره خواهد کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/687584" target="_blank">📅 09:19 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687582">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5d70bd09e.mp4?token=dQR9jnaOs3dvKc1CGCVyv82tTb8ZNXSXT58gINlaK4MD1YJK6Q0SFN2Ww8AljkFlQ8ivvwqfh1LKapKtKaA436RQKdwUf562MKXlOBCFHVHQyuy_q_dXIJq-SUpLNJOMAK1IM8c5Guyqd0AvkT8yPbGWqJI4EQi_T_nTwK9rMStkdSPvJLMgydEsbJfzlaCz5PNomF0IgWhgjsnP7bC3CEqMHCFTKKhGy5JUCP7LJl-F5_IylB6Q7ve3rS2N3dlVS4CHCWpmIGniLCfzUL0JityP6V1rhM3FSFOp4ZzlFu0Pmnn0KxbMLOjVqQ6AjCeh6Wtfl14ZwKmLkUd2QxF5iEBF2lDApNm4m2Mvn_Zf7V4I7AWw52oD3SuA9FTdozqkTX4fP32JMNyly9GyUY6cYkhRBmwtI_LlOP1_Bq5cVTOSgqoaXdmVwoUnZwDAlcVVwwilbmVG-qmtbWcT3c4n_SsJ8IITH_0lLeUtZ5YvuM9IM2IY74eqLSAEJXjulmrc_Vpb7myq-Ysd3cL-hkoTVREIj5GYVYWnatX7N_CBP_prLQwr9o2YuVp6l5natKxwdUFy9516t1bYqbe8vvACyTphPTOvg91vdvNDeNuFpLXsJh4GvFBX5EQ8xsGpfXLV_UjZl3T0884KOUGYD4EA_1cud3_pc3WChE9247XQu6Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5d70bd09e.mp4?token=dQR9jnaOs3dvKc1CGCVyv82tTb8ZNXSXT58gINlaK4MD1YJK6Q0SFN2Ww8AljkFlQ8ivvwqfh1LKapKtKaA436RQKdwUf562MKXlOBCFHVHQyuy_q_dXIJq-SUpLNJOMAK1IM8c5Guyqd0AvkT8yPbGWqJI4EQi_T_nTwK9rMStkdSPvJLMgydEsbJfzlaCz5PNomF0IgWhgjsnP7bC3CEqMHCFTKKhGy5JUCP7LJl-F5_IylB6Q7ve3rS2N3dlVS4CHCWpmIGniLCfzUL0JityP6V1rhM3FSFOp4ZzlFu0Pmnn0KxbMLOjVqQ6AjCeh6Wtfl14ZwKmLkUd2QxF5iEBF2lDApNm4m2Mvn_Zf7V4I7AWw52oD3SuA9FTdozqkTX4fP32JMNyly9GyUY6cYkhRBmwtI_LlOP1_Bq5cVTOSgqoaXdmVwoUnZwDAlcVVwwilbmVG-qmtbWcT3c4n_SsJ8IITH_0lLeUtZ5YvuM9IM2IY74eqLSAEJXjulmrc_Vpb7myq-Ysd3cL-hkoTVREIj5GYVYWnatX7N_CBP_prLQwr9o2YuVp6l5natKxwdUFy9516t1bYqbe8vvACyTphPTOvg91vdvNDeNuFpLXsJh4GvFBX5EQ8xsGpfXLV_UjZl3T0884KOUGYD4EA_1cud3_pc3WChE9247XQu6Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
داگلاس مک‌گرگور، مشاور پیشین پنتاگون و سرهنگ بازنشسته ارتش آمریکا: ایران مثل عراق یا افغانستان نیست که با تهدید و فشار از هم بپاشد اما آمریکا مانند کشتی تایتانیک، زیر آب رفته و درحال غرق شدن است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/687582" target="_blank">📅 09:12 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687580">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
سپاه پاسداران: ناو هواپیمابر و ناوشکن ارتش متجاوز آمریکا مورد حمله قرار گرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/687580" target="_blank">📅 09:09 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687573">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oXmkDk4xLw8CxCKx_rFgVkYUlHktzOdsPaJKuHR3o8jYPPbSqT_WQJqxJOmhJBvNfZTB_SAWNU6TpbZmJcQCxMBMrjuAvLaCF5d2blP-WDyuxr9sLzyP9F8P-oJXHZxCZ-9iIpQSTJDbmKsyvCaKlK1ikKBTw7lN9kBldqV99079OA9C13Y2BT1TEjchdVRM9q-0p3-ajZWYTfBSHWQP0_m4aBwXCsYjGB1ENA51mbuvzeKpCxB79erZicImRacr2Cxbct7pOyPBDAuG2CKGIGdRbeLqbvf6PTrlFyiNbafMZKi_KC8UO7yGsG_jP12E6krqTQSktG0Jdm9STsapaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b7bqKyV2tZGvOoMXSyOUwPmqr2QY5v74sfJykLL2OXElU2ZwZXsNfN_hRbKGuoq-F25v3pXa7rT3cjJnrMuNUMs6IVu08Eqat2Pkq7JsTdeuo9SJsuNOoSxxsXZMlyIVPxq9uwwB484e4TeOg0AfVfa1RjkY8LVWNeHYBcC0ILdSEof-KRfzxvaSNidrelqZxbukXsMTRU_h_JJ4M2a2L5EYQ0wLeFQXzsGntlsMnKkA3szPBctha5aZSGBhbKuP0tCw9EMkWXejnITH_NSCWcB0BS3qWalP9YSqFBmSI6sFWCwBG0NNyfkkkJ8_gwj6CVxO9MUsJJpHcy25weP__w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NCaZYVIffT5ihLlEYjsGwgLLzmUXoDl1LzorqrMdP19Vh-P6Q1UUFe0VAaVw8q1wbLgKjxH38tEVlezmVJ9cLaEx80iPHHQIboiZ4f9QoHsPgG4Of0mKQjKm-s-hRBCVe0zKDD5vQdMRujTgsTW12kKM3_wOjhDb0kobmyh23ZmmuFF4RSMlJCVvilkFcRmkFqaA0UwFnxoXDo7kyd3rnbmpmPk740VxTgqx8mQFCcsX2It6uK0cDD4RBiLvAI7waoj_O1dV9o9ODNgfQUFzgXmImVZ4RijVGcUkW5gll-mCAu_nzkmY2ryi_0PgdYxz0_mE0kxf239eVvyV0v72WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/roVNQyeQ4xyzaliiyR4sNKntI_936kmTmOCh9twaEIMwtDINnalkbfz3bRY8KrE3YowUiAsJrm9-k1Bs5g_Br8P4PiCcm9hpYe2a9Bg5pnVp6fO_iEigK5ywybKilo7QA7DxT21eruvnXdlvg-QlT86EJAUtCQHgBTMdflRCKkwfjjqt36-7bSrMQxqTbHPfP5hV-SMWwWPNGcYj86vp4UWFk6kNYNrckYoitPUYMte8h4RPfjMxLJ7oKmM5dKv3fBcPxSjrlnM_wIo7-jXRhvKPdvEdGNvqVdNvLhMyxatoZ0vQERqoYzePOfhRT8GoF60LVVof6SzlwjMPrDYw5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l3BWrwO0FcNSiL3MJ8mKVG7DjVlHVQYQ7UcsPnAnXIj17pKPu6axd6CjfCznq2DQIA8qzlzWl1ZP_-on_oJvuKKYnN1rEFwEyHmwwn31vSMnUscbUt_E0XL2r8o0SyRrv1FPBCjAWzJhO2VqGIxZg9tqXA_R53_CEv3ilVif7XSDJtFcurysniD8-un6UaPZyEaWtFW2nRMMyfYBZj62ZKYp2Ynzy4lRSiK7ls2qGJe2YQMfircPgeZ-VkpyS286FQbRDbuOx3dyBqpdPA9LvbobKWpYGAyMuIPbtndxvqOOlEi2nR1-z--2hVSCwyzn3w2v05JRXrOzX_2Po0AJ-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چند خمیر کاربردی که خیلی به کارتون میاد
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/687573" target="_blank">📅 08:42 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687572">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4309078e57.mp4?token=CNGMQaYYCCDcMwYf1aCl7nSgBqyVX1e7FW9B89N18W5yaupNQYtueibftoiBJRpkeoQJK-R1-85J_OCetL5E-UT6Y00GjN41iINc1pVfjIEHcE6Ezs6b2fDjbDsT9Zbwj8uoR7bibsGj4kq8s5mIE5LMuHQyiIkecO8oFuUmg2Ed-beF8qbJZm5SrK2lZMJaMxSaf9hN30f5aABX3dNeE7VhLTIwUK-5vHcEJoIA1CALrGRFDEkQqkrGSyKNWz6cGYFOGWfj76ATEM4qum-7rVxp6xS-TLbayD0v9yH0edMfi2kqubDg-unTga_EDt0idJ37M12KoHEHhBd4k3WEaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4309078e57.mp4?token=CNGMQaYYCCDcMwYf1aCl7nSgBqyVX1e7FW9B89N18W5yaupNQYtueibftoiBJRpkeoQJK-R1-85J_OCetL5E-UT6Y00GjN41iINc1pVfjIEHcE6Ezs6b2fDjbDsT9Zbwj8uoR7bibsGj4kq8s5mIE5LMuHQyiIkecO8oFuUmg2Ed-beF8qbJZm5SrK2lZMJaMxSaf9hN30f5aABX3dNeE7VhLTIwUK-5vHcEJoIA1CALrGRFDEkQqkrGSyKNWz6cGYFOGWfj76ATEM4qum-7rVxp6xS-TLbayD0v9yH0edMfi2kqubDg-unTga_EDt0idJ37M12KoHEHhBd4k3WEaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از فردا در نیمه شمالی کشور هوا سردتر می‌شود
هواشناسی:
🔹
بعدازظهر امروز و اوایل شب سامانۀ بارش‌زایی از شمال‌غرب وارد خواهد شد و در نیمۀ شمالی بارش‌ها آغاز می‌شود. دوشنبه و سه‌شنبه دما در نیمۀ شمالی کشور کاهش می‌‌یابد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/687572" target="_blank">📅 08:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687571">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Idmemnj0a5HHA0SjZPcJFY10A_YPwJVTNDip-owlnpSV5kyGEKM_ju_FT5X9npoFPr9vra2YbgbqciPShPkSh6V0KwgBGu90jbnl2SepAkZYMze5jL5r780dtyIV5T66p31TOOuiOzoKeKzcQXaudcgkecmY54CG65Xbz4MAFw6p-amowXZocYVXO7vQxvZgOBtPAb8FY-jfgL4bBxwhykRdLBK3u0Uu8JuUCbS_2MUMo14W-YScnUrpZLMTshwM3o-nUhPEoAAinyeDqGQj0sNi_9jvKd-cjzz79I50Z43lJ7_HauKXBpYuft36iWhRKVmle9OjCLrKj2_aLk5MWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پروفسور جیانگ: اگر ایران کشورهای خلیج فارس را مجبور به ترک پترودلار کند، اقتصاد ایالات متحده با فروپاشی و انقلاب خیابانی روبرو خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/687571" target="_blank">📅 08:21 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687569">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e0190e555.mp4?token=RCpZuFkuShVhQUwHjA0ZXJwPaUgp5ZiYFJFSWagH9m90i57PSZc91cXvqC9gH0doZ4Q-hrpXYdwXz92JZ-pdWNoevGJlt6_h-SgA8JE2_mPeGqqMvYxPPonRPlLfvg0SE7WlElvH9P8Dr9FzllS65ovTzaVgeINE1oae82Bz19kH73QXqLAoR9V65hXNxL3tNKVXM6EmCz0at8fTY4BX7FqWUiG2iYkDMzFpF-DMpGbNNheAFn1fIEOFdgAn11n3R0m8OrpYalqq6ngo6XvzHsaT-1DjOO3cHJIcBBIm3NpZlwxvyeDNKQ5lnRovsxIK984xtzZFbYOqpGGZHcxyRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e0190e555.mp4?token=RCpZuFkuShVhQUwHjA0ZXJwPaUgp5ZiYFJFSWagH9m90i57PSZc91cXvqC9gH0doZ4Q-hrpXYdwXz92JZ-pdWNoevGJlt6_h-SgA8JE2_mPeGqqMvYxPPonRPlLfvg0SE7WlElvH9P8Dr9FzllS65ovTzaVgeINE1oae82Bz19kH73QXqLAoR9V65hXNxL3tNKVXM6EmCz0at8fTY4BX7FqWUiG2iYkDMzFpF-DMpGbNNheAFn1fIEOFdgAn11n3R0m8OrpYalqq6ngo6XvzHsaT-1DjOO3cHJIcBBIm3NpZlwxvyeDNKQ5lnRovsxIK984xtzZFbYOqpGGZHcxyRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مچ پات خشکه؟ این ۴ حرکت رو امتحان کن  #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/687569" target="_blank">📅 08:04 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687568">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‌
♦️
سپاه: شمپاد آمریکایی مورد حمله قرار گرفت
روابط‌عمومی سپاه:
🔹
نیروی دریایی قهرمان سپاه پاسداران انقلاب اسلامی یک فروند شمپاد (شناور مدیریت پذیر از راه دور) ارتش تروریستی آمریکا که قصد ورود به منطقۀ حفاظت شده تنگۀ هرمز را داشت مورد حمله قرار داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/687568" target="_blank">📅 07:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687567">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
حملۀ اشتباهی جنگندۀ سعودی به مواضع خودی در یمن
🔹
وبگاه خبری «الخبر الیمنی» گزارش داد که یک جنگنده سعودی روز گذشته مواضع نیروهای «العمالقه» را در استان تعز بمباران کرده است.
🔹
طبق این گزارش، ده‌ها تن از مزدوران وابسته به ریاض در این حمله کشته و زخمی شده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/687567" target="_blank">📅 07:49 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687565">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c9528ee97.mp4?token=DV3tdbyr6Z-jRn3QtC6lZT4ln-AaRHSaVWA2-Z_4SgdgHv7uCp5KgV8ZyIsKilz9RtejXThwMBxTaoduQ48xvyoHsPMRA88NSDGy5KSHxfge4nxsLlNTpkwbzMjGqhlMy47x0TMBPqyeBGU7PSH3_1dPHq4AJ4THG9FkQw51IwZW9axWNQdWRZehzAZtNQJML_S2f_H3auNNkGBWJCCS6pZhAMcK9fNq6aNebnfYHhA5aJYz4LnEC14awXvLfWn8yEjk-hjfPDKHNNBCA-2N7HGfNbc-KnYMiHW5ScSP45xfjgzmEPuvsVMVTdUMAHtFdqrsj0Q6HRK7Oj7c7T9HFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c9528ee97.mp4?token=DV3tdbyr6Z-jRn3QtC6lZT4ln-AaRHSaVWA2-Z_4SgdgHv7uCp5KgV8ZyIsKilz9RtejXThwMBxTaoduQ48xvyoHsPMRA88NSDGy5KSHxfge4nxsLlNTpkwbzMjGqhlMy47x0TMBPqyeBGU7PSH3_1dPHq4AJ4THG9FkQw51IwZW9axWNQdWRZehzAZtNQJML_S2f_H3auNNkGBWJCCS6pZhAMcK9fNq6aNebnfYHhA5aJYz4LnEC14awXvLfWn8yEjk-hjfPDKHNNBCA-2N7HGfNbc-KnYMiHW5ScSP45xfjgzmEPuvsVMVTdUMAHtFdqrsj0Q6HRK7Oj7c7T9HFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فوران آتشفشان در اندونزی
🔹
آتشفشان «آناک کراکاتوا» در اندونزی بامداد امروز فوران کرد که موجب لغو پروازهای جاکارتا شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/687565" target="_blank">📅 07:42 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687564">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d869f2116f.mp4?token=GK7DK1Wb4sEjd-Du3DnqFcJ69_BNjYzQhwehWt7zeuQHgwzheb4x1hmuODFmcs1N2OdHE5-skMrFWTuDzm58EVaz_OhJA7VH70BtB73gRH5y4IOC9wW67aDOmNIsAJzIiLYLK_iLsVfVudkCMD0oj2-mObNctQIPnTNcmFT4WVp9UNtOTmrNPeXBrcaiozlT-U9c1VcJLq56FrvfFeG7hcRyySArXWE1QdFwLVikWrNjsu7Jkj1GVxVDLnFWvRzf6uUxMtg2BxnM8RHWwYH2TbVruWDq6wcuMEGEO7T5QzBGLMYYriL0ULh0CEKkbcwh3VWf4n4LE_QIGa4ICUnGWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d869f2116f.mp4?token=GK7DK1Wb4sEjd-Du3DnqFcJ69_BNjYzQhwehWt7zeuQHgwzheb4x1hmuODFmcs1N2OdHE5-skMrFWTuDzm58EVaz_OhJA7VH70BtB73gRH5y4IOC9wW67aDOmNIsAJzIiLYLK_iLsVfVudkCMD0oj2-mObNctQIPnTNcmFT4WVp9UNtOTmrNPeXBrcaiozlT-U9c1VcJLq56FrvfFeG7hcRyySArXWE1QdFwLVikWrNjsu7Jkj1GVxVDLnFWvRzf6uUxMtg2BxnM8RHWwYH2TbVruWDq6wcuMEGEO7T5QzBGLMYYriL0ULh0CEKkbcwh3VWf4n4LE_QIGa4ICUnGWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فروریختن مناره و تخریب کامل کلیسای تاریخی اوهایو
🔹
آتش‌سوزی در کلیسای سابق سنت اگنس در تولدو، اوهایو، باعث فروریختن مناره این کلیسا شد. علت آتش‌سوزی هنوز مشخص نیست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/687564" target="_blank">📅 07:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687563">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
بانک مرکزی از نظارت بر پلتفرم‌های آنلاین طلا کنار کشید
🔹
پیگیری‌ها از بانک مرکزی نشان می‌دهد بانک مرکزی قصد دارد «سامانۀ ناظر» را که بر موجودی طلای پلتفرم‌های فروش آنلاین طلا نظارت می‌کند، کاملا در اختیار ستاد مرکزی مبارزه با قاچاق کالا و ارز قرار دهد.
🔹
این یعنی بانک مرکزی مستقیم بر فعالیت پلتفرم‌های فروش آنلاین طلا نظارت نمی‌کند.
🔹
با اتصال پلتفرم‌ها به سامانۀ، موجودی طلا و دارایی هر کاربر به صورت آنلاین قابل رصد است، اما مسئولیت آن با بانک مرکزی نخواهد بود./ فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/687563" target="_blank">📅 07:35 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687562">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
لغو ممنوعیت استفاده از پیام‌رسان‌های غیربومی برای اطلاع‌رسانی رسمی دستگاه‌ها
معاون ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور:
🔹
ممنوعیت استفاده از پیام‌رسان‌های غیربومی برای اطلاع‌رسانی رسمی دستگاه‌ها، با اجماع کامل همه اعضای ستاد ویژه ساماندهی و راهبری فضای مجازی برداشته شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/687562" target="_blank">📅 07:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687561">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
کارت شرکت در آزمون کاردانی به کارشناسی ناپیوسته ۱۴۰۵ از امروز منتشر می‌شود
🔹
آزمون کاردانی به کارشناسی ناپیوسته ۱۴۰۵, جمعه ۲۰ شهریور برگزار می شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/687561" target="_blank">📅 07:26 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687560">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
کالابرگ سرپرستان خانوار با رقم پایانی کد ملی ۰، ۱ و ۲ شارژ شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/687560" target="_blank">📅 07:11 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687559">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_kUamt0BPwupmrkKhpaZVb8A1FOTNiwAZbetYvAPxI1Sxn9i2Zp3zla5VmEZJSDS5FSID-t7Pqh5A-5KrfjPegH01NDE0Au4xZLFwePeEwLBit6wanf-HmdNJWCmRrfhrMLhML-QDGSfi1xtHpdYPA3F9ewCePaPndVGeuMfPsFmrMiYwNlxnBA-fPA2uSZDRDIPmvWLORHiaHu2e8tx2xtVbHbYN_Y7ULLiROvXwTM8Aw7yR4gtMiw5qFEHgVDEVc2bUtXW6F94jNv4Rhdks1i6tMItXV6QTCXuAaeWBKX2-CjWgqWClWd-FbWLE1esulvlsr8L4tAgB0kbL_PwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز یک‌شنبه
۱۵ شهریور ماه
۲۴ ربیع‌الأول ۱۴۴۸
۶ سپتامبر ۲۰۲۶
یکشنبه‌ها
#حدیث_کسا
بخوانیم
⬅️
متن و صوت حدیث کسا
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/687559" target="_blank">📅 07:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687558">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromGoldiran | گلدیران</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80aba6e820.mp4?token=Wd7qEnBLRzt9RsJ0PlKvVMgxLiCqBajCFou4AlR0Wsk_mpsW5F9s6LtsBhonyem_y_dXnlf0Yp8UM3b3NFesQjCv9Qp-1AErT2_WenxN00SJYqJgvpEGI7FKq3JyUR7RxBKA28PyvlbQfPc1VVjiF6LsljIcD3zP8CvIkNzqk48RkqYfCLwtTfHIHYON65N2m5hZLLMr9W1NCIZAFl1RXj6X4mhPjx0NHHGPInz-odOrB5flsXt6TZ44TMk7jtuZ1_5m3Fq4aWF8ZRuXoIsFIZUfAsRg1Y0ixHGu_CRMUy5kiUZDSpCN0WNqT_bS4hJTWTh3rq8RDNBp8fE1cB-FrJHbgsSXAYtHly72GfIP23_vc8dxOIlz6pY41RFT7MhsmGIgMDGz9LvnRHhaQ-KmgeB__qnYLnpaA5IH99L8H1kV-0S41z1y3TzRv0JS3M-8YnLDtD6Vx7e7gl_c4YVHULQYnr5PQzZxaQOQPpRwG1eXZ2OGDDCjx47DoEYqTuuHsqK7CPpvRH2jS3_3HjAC6kD_ujoNv5_cYgRkNtTobpH8qfakHPwNJDlaOqlXiwh4Owhi54w8sqEb-wR4L1eYYyD0ipPUvv9d-Ar_C4LCR3TqCkgagrYEq5WGN3IUstv5pVNYevArJ0sm9ljXQeWJZIPEHAEFhMSBs-_a4lD6FwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80aba6e820.mp4?token=Wd7qEnBLRzt9RsJ0PlKvVMgxLiCqBajCFou4AlR0Wsk_mpsW5F9s6LtsBhonyem_y_dXnlf0Yp8UM3b3NFesQjCv9Qp-1AErT2_WenxN00SJYqJgvpEGI7FKq3JyUR7RxBKA28PyvlbQfPc1VVjiF6LsljIcD3zP8CvIkNzqk48RkqYfCLwtTfHIHYON65N2m5hZLLMr9W1NCIZAFl1RXj6X4mhPjx0NHHGPInz-odOrB5flsXt6TZ44TMk7jtuZ1_5m3Fq4aWF8ZRuXoIsFIZUfAsRg1Y0ixHGu_CRMUy5kiUZDSpCN0WNqT_bS4hJTWTh3rq8RDNBp8fE1cB-FrJHbgsSXAYtHly72GfIP23_vc8dxOIlz6pY41RFT7MhsmGIgMDGz9LvnRHhaQ-KmgeB__qnYLnpaA5IH99L8H1kV-0S41z1y3TzRv0JS3M-8YnLDtD6Vx7e7gl_c4YVHULQYnr5PQzZxaQOQPpRwG1eXZ2OGDDCjx47DoEYqTuuHsqK7CPpvRH2jS3_3HjAC6kD_ujoNv5_cYgRkNtTobpH8qfakHPwNJDlaOqlXiwh4Owhi54w8sqEb-wR4L1eYYyD0ipPUvv9d-Ar_C4LCR3TqCkgagrYEq5WGN3IUstv5pVNYevArJ0sm9ljXQeWJZIPEHAEFhMSBs-_a4lD6FwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">☀️
این تابستان، خرید راسل با هدیه نقدی همراه است.
در جشنواره تابستانی جی‌پلاس، با خرید و نصب ساید بای ساید چهار درب Russell، هدیه‌ای ویژه در انتظار شماست.
تمام خریداران این محصول پس از نصب، حداقل ۱۰ میلیون تومان هدیه نقدی دریافت می‌کنند و بر اساس قرعه‌کشی، این مبلغ می‌تواند تا ۲۰ میلیون تومان افزایش پیدا کند.
برای مشاهده جزئیات محصول و خرید، به فروشگاه اینترنتی گلدیران پلاس مراجعه فرمایید:
goldiranplus.ir
مشاهده آدرس فروشگاه‌ها
@goldirangroup
گلدیران | روی خوش زندگی</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/akhbarefori/687558" target="_blank">📅 01:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687557">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5072b66a5.mp4?token=lctbIftGvMFZ2jGrtyp3_HfzNsE0zhLogkirzFQ3eZ3R6Ho3BYKzBdxjvyx-ZjDpfF4gvmAZo8jbCwsiAriqWD0em_UI2s9OlakY0D91KnSYp828_z7jCA5Lo3AKDFDjB0GtT7lZi5HwoVd9ndzh18BgkCMw6OLNkh6cb0dzYIbSR-P-kM4N7GG0yDde8iWvjuHb1vHWdpLrfY218slq93S7ZABN_T0abhsuh0zfITxP766dOfS0gzWZqtStqZlORhx7ga2MAH0grGOU8JruN_p59_go9ZsFb1niz6dtuC8CchI0Utyzxd3WZ2fHIAHjdNTlXh7ZCNcASACMFVORtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5072b66a5.mp4?token=lctbIftGvMFZ2jGrtyp3_HfzNsE0zhLogkirzFQ3eZ3R6Ho3BYKzBdxjvyx-ZjDpfF4gvmAZo8jbCwsiAriqWD0em_UI2s9OlakY0D91KnSYp828_z7jCA5Lo3AKDFDjB0GtT7lZi5HwoVd9ndzh18BgkCMw6OLNkh6cb0dzYIbSR-P-kM4N7GG0yDde8iWvjuHb1vHWdpLrfY218slq93S7ZABN_T0abhsuh0zfITxP766dOfS0gzWZqtStqZlORhx7ga2MAH0grGOU8JruN_p59_go9ZsFb1niz6dtuC8CchI0Utyzxd3WZ2fHIAHjdNTlXh7ZCNcASACMFVORtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بعد از ۴۰ سالگی، چه ویتامین‌‌هایی برای بدنت ضروریه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/akhbarefori/687557" target="_blank">📅 00:43 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687556">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
منابع یمنی از کشته شدن حداقل ۳۳ نفر از شبه‌نظامیان «العمالقه» (همسو با امارات) در حملات نیروهای ارتش و انصارلله یمن خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/akhbarefori/687556" target="_blank">📅 00:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687555">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K9FQp0q1FyzU1zSVtgngiBOgKgdqofhj_9NayuZ5EVO5zKDtv9f9hLZivCck9DCZFMsnz6d9_JaHVP-uab_hq6g6W5CBdlHWd28Bvpa8qsmuTUo1VkTMUTjnMF78yhmesdWKNfL4u2noSjBYcKZonMXwzgJuhmivgpAo5EJADNQ8UNRI5kuPUV8ERmYVslIzYryHdjMUNYcm6qo037Z7IPUmxvB9zGEj6RZOHQGRfoqdx4i-TDi8PG9Vd4zhP21bjIP2tfyJl4v3z2zmatye0WHKFefQDoKLrpSzWvqOJS5iwYG-HkcaUoX-mjaZKhf8Wnyo0oR07QFwbPPAmImJTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رقیب نتانیاهو برای ایران چه برنامه‌ای دارد؟ | از «منطقه کشتار» هسته‌ای تا بازگشت عملیات موساد | توهمات ناتمام صهیونیست‌ها
🔹
با نزدیک شدن به انتخابات پارلمانی اسرائیل، رقابت برای نخست‌وزیری وارد مرحله حساس‌تری شده است.
بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3242959</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/akhbarefori/687555" target="_blank">📅 00:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687554">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5558d5321a.mp4?token=AyfzVdxWw_oAMM3Y4PvN1d-0TVGezkSfG_JZdFn3IiNnutFIZ7HPnfTtbQ3cYiWJB4-bYl8QBQXKrhCsblkNmWjJ3sRb4XNN-Xusxx7I7qMJ7MFxrRrUqANMGBQi2H1Vwk4JbygnvUWS62SE9yrauzP_6gRyWZBd9KLw__4kFveFEFo4JOSeZnaRBGbdJAI9nCUIo1wkWbmQ3cQhG8QnO6AgQI87ZbrvTz8EAjSx-6qJX-oMrV0Kb44qbZTegGxlF0YFK4BbeRt1WhgtdEro3x1O9olrpvqwea9fe_3x_O4KfSkeiy_qrkAwSKHLcAqvEu_2uJVqFhzGoyNEelzHGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5558d5321a.mp4?token=AyfzVdxWw_oAMM3Y4PvN1d-0TVGezkSfG_JZdFn3IiNnutFIZ7HPnfTtbQ3cYiWJB4-bYl8QBQXKrhCsblkNmWjJ3sRb4XNN-Xusxx7I7qMJ7MFxrRrUqANMGBQi2H1Vwk4JbygnvUWS62SE9yrauzP_6gRyWZBd9KLw__4kFveFEFo4JOSeZnaRBGbdJAI9nCUIo1wkWbmQ3cQhG8QnO6AgQI87ZbrvTz8EAjSx-6qJX-oMrV0Kb44qbZTegGxlF0YFK4BbeRt1WhgtdEro3x1O9olrpvqwea9fe_3x_O4KfSkeiy_qrkAwSKHLcAqvEu_2uJVqFhzGoyNEelzHGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صحبتهای تامل‌برانگیز آزیتا لاچینی درباره زندگی...
🔹
اگر درست زندگی نکنیم، چی میشه؟ به کی ضرر می‌زنیم؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/akhbarefori/687554" target="_blank">📅 00:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687553">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
انتشار برای اولین بار، تصاویر منتشر نشده از رصد و اقدام علیه شناورهای متخلف
🔹
اقدام و مدیریت قاطع نیروی دریایی سپاه در تنگه هرمز؛ هر گونه اقدام مشکوک مورد هدف قرار می‌گیرد.
🔹
ایالات متحده بزرگترین تهدید برای امنیت کشورهای منطقه و تجارت دریایی است؛ پشتیبانی و اسکورت ایالات متحده دروغی بزرگ است!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/akhbarefori/687553" target="_blank">📅 00:24 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687552">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
اولیانوف نماینده روسیه: در جلسه شورای حکام روز دوشنبه درباره ایران بحث خواهد شد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/akhbarefori/687552" target="_blank">📅 00:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687550">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔹
خبرهای جذاب امروز را به انتخاب مخاطبان خبرفوری بخوانید و ببینید و نظر بدهید
🔹
🔹
فاز جدید جنگ ایران و آمریکا | حمله به نفتکش ایرانی در جزيره خارک
👇
khabarfoori.com/fa/tiny/news-3242835
🔹
پشت‌پرده شایعه حمله اتمی آمریکا به تهران چیست؟
👇
khabarfoori.com/fa/tiny/news-3242751
🔹
ماجرای اعزام ناو از کره به خلیج فارس | ایران با کره جنوبی وارد جنگ می شود؟
👇
khabarfoori.com/fa/tiny/news-3242872
🔹
جزئیات فعالیت شبکه فحشا در شهرداری | نقش یک مسئول شهرداری در سازماندهی شبکه فاش شد
👇
khabarfoori.com/fa/tiny/news-3242669
🔹
خبر تکان‌دهنده درباره سرنوشت غم‌انگیز خواننده زن قبل از انقلاب
👇
khabarfoori.com/fa/tiny/news-3242916
🔹
خبرهای لحظه‌ای جنگ را اینجا دنبال کنید
🔹
khabarfoori.com/fa/tiny/news-3242976</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/akhbarefori/687550" target="_blank">📅 00:06 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687549">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
بازداشت عوامل رژۀ موتوری منتسب به سازمان منافقین در حوالی کرج
🔹
روز گذشته ویدئویی در فضای مجازی منتشر شد که در آن ظاهرا تعدادی از هواداران سازمان منافقین در خیابان‌هایی که گفته شده در حوالی شهر کرج قرار دارد، اقدام به حرکت با موتورسیکلت و خودرو کرده‌اند.
🔹
تمامی افرادی که در این کلیپ حضور داشته‌اند، توسط نیروهای امنیتی شناسایی و دستگیر شده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/akhbarefori/687549" target="_blank">📅 00:06 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687548">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QR8pqSm5EUAeWNh8qI7doAyK2GMdUBnid8EW3tGsQtliCzkxHynATxabJqgCFgnL39ZDu1MDmCXtppE3a-Nz9c97TzGfVoLb4SIlIUWVV3s6pfTuhp893EyxC9OqiKX4kSwaa1NWZ00FDVZNc-39rtrtBJQAddMVOeq3RkJbQh0MFS8_3sJhn0IoJfojl5cSQ5OGgMMFndVwj0ZImUt9f4d8YUEC7fSDcPaE2ogN-egt4B5V_4btTuOOCRsv7WJdEdSt3xzqq8kj2vixBVQCc3Wii4C9hrXH43t_TQ9URSEkH23-f5GU1rrYZcOprQXxAJnjOheuvYZ1RL7bE9mFCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦋
خاص بپوشید، متفاوت دیده شوید
🦋
حوریا عبایا | HORIA ABAYA
مجموعه‌ای از عباهای لوکس، مجلسی و روزمره با طراحی اختصاصی
✨
با پارچه‌های خاص و وارداتی، همراه با گلدوزی و نگین‌کاری‌های ظریف و منحصربه‌فرد
از مدل‌های مینیمال و روزمره تا عباهای فاخر و خاص،
برای استایلی زنانه، شیک و متفاوت
🤍
📍
خرید حضوری از شوروم حوریا عبایا در فرمانیه تهران
📦
ارسال با تیپاکس به سراسر ایران
مشاهده مدل‌ها، قیمت و ثبت سفارش
👇🏻
📸
اینستاگرام:
https://www.instagram.com/horia_abaya
کانال بله:
https://ble.ir/horia_abaya
📲
سفارش و مشاوره:
09103156129</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/akhbarefori/687548" target="_blank">📅 00:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687547">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMUDRaOXfuKBUFERsX-SfQX_F6raVIW7CBDSgSMJ2PRBS1Q3o3-m8sIwSyw6tyTtEio7TlkVG5z3RFBo15Wk1THzsYFr9fuqX4uhxIlzinKaNHNh-vBCIAPFhLRiFnxvPFjHrltVrxdeiy-Dw02Y4JG-qwsMBOsHpoZr5IYmKHw5IreE02fs8kUumrxWAfspHGToAKjJvMyltDUdUtYPyn6T5lYhgBe5GG0YDW62nRxVh9GGW6CeFcWM2HGi4qHrz5I2xz6q7sReS_s2XswzzKMNSYzjAKDusHEmFL8_izaMBi6nn7rCd_fAm2-eZuEnYWuy3UdBVfn98fFLOvMThQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/687547" target="_blank">📅 00:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687546">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
صولت مرتضوی: حسن روحانی همه مسائل کشور را به برجام پیوند زده بود و حتی تلف شدن گاومیش‌ها در خوزستان از کم آبی را به برجام پیوند می‌زد/ رشد اقتصادی در دولت حسن روحانی کمتر از ۱ درصد بود و شهید رییسی رشد اقتصادی را به ۷ درصد رساند
صولت مرتضوی، وزیر کار دولت سیزدهم در
#گفتگو
با خبرفوری :
🔹
ترامپ برجام را پاره کرد و بسیاری از مفاد برجام را هم دولت اوباما اجرا نکرد و زیر میز زدند. دولت رییسی گفت اقتصاد بدون برجام هم قابل اجرا است؛ رشد اقتصادی را به ۷درصد، نرخ بیکاری را از ۱۰۰ درصد به ۷/۶ درصد، میزان نقدینگی را از ۵۰ درصد به ۲۹درصد، تورم را از ۵۰ درصد به ۳۲ درصد، صادرات نفتی را از ۳۰۰ تا ۴۰۰ هزار بشکه نفت در روز به یک میلیون و ۷۰۰ هزار بشکه رساند؛ اینها بدون برجام بود یا با برجام؟
🔹
در جلسه‌ای آقای روحانی اعلام کرده بود اگر کسی در مملکت ۳۰۰ تا ۴۰۰ هزار بشکه نفت در روز صادر کند، بگویید او را وزیر نفت بگذارم.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/akhbarefori/687546" target="_blank">📅 23:56 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687545">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bad4d13812.mp4?token=g9S3Ahrrj07nqZKmwpWXscnNH6SdEhuWxRyD7pdKnZPhpvWa8cAuXMT7UDMOsvxkDIx8KVjbFwTPtlgoYAwEmWiUGXCVCTEx2_bXytyhGr3nmlWpDGLIHgpPILLHY1pQ7TDwv-KE4o4e5Pwwk_8BbkWLVpw-bBeDajHwWSW-AvXca1j-MPLU4Gh9w-u1e1LYlC-e9q2Uq324q0Ifoj7Xx4QstejjHFkLfBxi5lCI_mSKe75ExAUxnMF_lo6utTt-rHLue-h5-mvmedFwJFp4n55AC2kcwJhx4UGJfnAwXUUT3YVlwnOYgriYwX9xxON9w0mRTasHbXHa-PCSyU4wCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bad4d13812.mp4?token=g9S3Ahrrj07nqZKmwpWXscnNH6SdEhuWxRyD7pdKnZPhpvWa8cAuXMT7UDMOsvxkDIx8KVjbFwTPtlgoYAwEmWiUGXCVCTEx2_bXytyhGr3nmlWpDGLIHgpPILLHY1pQ7TDwv-KE4o4e5Pwwk_8BbkWLVpw-bBeDajHwWSW-AvXca1j-MPLU4Gh9w-u1e1LYlC-e9q2Uq324q0Ifoj7Xx4QstejjHFkLfBxi5lCI_mSKe75ExAUxnMF_lo6utTt-rHLue-h5-mvmedFwJFp4n55AC2kcwJhx4UGJfnAwXUUT3YVlwnOYgriYwX9xxON9w0mRTasHbXHa-PCSyU4wCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی پزشکیان آسانسور را ممنوع کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/akhbarefori/687545" target="_blank">📅 23:50 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687544">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار آذربایجان شرقی(Admin)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a553f8c48.mp4?token=RIXYmApoOC1q_AeKwHvj_CjVVN5kzZTYRptepqzJL5TK2jeilDoUHgxS7kGM-yeNJYge1xNSbYznlo1T6aCmgBMw4L6qcPndm2s2OK6rekyDzJx5ejmi4aJ_9eakpaMyqy6zYRSxuIxuHw_nOsT4BQj8N_RQOzuMdeAiFBX4vwFABSLH52WkEXDikL31XGHWukI4wOgjE9VSEpiV_uwpjhbHyBLISXOus9ln2zEdpsQyJoP3BM6RPFG7Fmh0hWA-8u79l7ZKcsxTiOuAyFIEbddJrSRfLFvxPTbVeNgYlvYURKlogA7cr8GnUFqUWUqql47UBam4NN1c43zUDUmh_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a553f8c48.mp4?token=RIXYmApoOC1q_AeKwHvj_CjVVN5kzZTYRptepqzJL5TK2jeilDoUHgxS7kGM-yeNJYge1xNSbYznlo1T6aCmgBMw4L6qcPndm2s2OK6rekyDzJx5ejmi4aJ_9eakpaMyqy6zYRSxuIxuHw_nOsT4BQj8N_RQOzuMdeAiFBX4vwFABSLH52WkEXDikL31XGHWukI4wOgjE9VSEpiV_uwpjhbHyBLISXOus9ln2zEdpsQyJoP3BM6RPFG7Fmh0hWA-8u79l7ZKcsxTiOuAyFIEbddJrSRfLFvxPTbVeNgYlvYURKlogA7cr8GnUFqUWUqql47UBam4NN1c43zUDUmh_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصمیم جنجالی داور؛ از کرنر گلگهر تا گل تراکتور
🔹️
داور ابتدا به سود گل‌گهر کرنر گرفت اما لحظاتی بعد تصمیمش را تغییر داد و ضربه دروازه اعلام کرد؛ تراکتور هم بلافاصله بازی را شروع کرد و در ادامه مهاجم این تیم در موقعیت تک‌به‌تک گلزنی کرد.
@azarbaijan_Sharghi</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/akhbarefori/687544" target="_blank">📅 23:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687543">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sy56NaymjI-jmzjSnmS8FElzDTPyC4IbAVRLL0iQYaznkdCW72nXzhnHdDy6YeQpOIEhpmhSxr-FeGUdNjL9LmaAwIH-75Hl6Zvx8nL_dQCKI0sIgxcrGJSVcU8cXaccE5PZC83u9VVfQ-pLwze96DGO5wgh5sbVloh1T4AXHODGYRe_CEpBzsm_mB7bOSASd_lrhQ4hQwxANGegtLsxAaDaCFrhKUuR5suRFu7sGO3VGHYXVMI6_JnLA61P02AHwsCKb2zeQfWlg1Ooc8VNwmdrGDL_jrVzCs7h6QR7xowLt7ss_yOe8t-klehG0ZNMDmvX0ITUSN2dr8lqHLjyMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«فخوز» به تابلو بازگشت؛ اعتماد سهامداران به آينده فولاد خوزستان
🔹
فروردین‌ماه ۱۴۰۵، تنها یک ماه پس از آغاز جنگ، شرکت فولاد خوزستان هدف حمله دشمن قرار گرفت و در جریان این حادثه، بخش‌هایی از این مجموعه با آسیب جدی مواجه شد. با این حال، اتکا به توان فنی و دانش بومی و تلاش مستمر کارکنان و متخصصان شرکت موجب شد فولاد خوزستان در مدت‌زمان کوتاهی وارد مرحله بازسازی و ریکاوری شود.
🔹
حالا پس از گذشت حدود پنج ماه از آن حادثه، نماد «فخوز» بار دیگر به تابلو معاملات بازگشته و واکنش بازار به بازگشایی سهم، قابل توجه بوده است.
👇
👇
akharinkhabar.ir/local/10996072/
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/akhbarefori/687543" target="_blank">📅 23:44 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687542">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
هشدار هواشناسی برای شمال کشور؛ بارندگی شدید در راه است
یک کارشناس سازمان هواشناسی:
🔹
بارندگی شدید از روزهای دوشنبه و سه‌شنبه در سواحل شمالی آغاز می‌شود و با تشدید رگبارها، هشدار نارنجی برای مناطق صادر خواهد شد، مسافران و کوهنوردان احتیاط کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/akhbarefori/687542" target="_blank">📅 23:41 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687541">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
غرامت دهید تا از تنگه هرمز عبور کنید
عباس گلرو، عضو کمیسیون امنیت ملی و سیاست خارجی مجلس در
#گفتگو
با خبرفوری:
🔹
طرح امنیت پایدار تنگه هرمز در مرحله پایانی بررسی در کمیسیون است. این طرح می‌تواند تنگه هرمز را به یک منبع درآمدی بسیار ارزنده برای کشور تبدیل کند. نوع رفتار با شناورهای کشورهای مختلف طبیعتا متفاوت خواهد بود، هر یک از دولت‌ها وضعیت متفاوتی دارند و علیه کشورهای متخاصم نیز اقداماتی انجام خواهد شد.
🔹
یکی از بندهایی که جدیدا در کمیسیون امنیت ملی مطرح شده، پرداخت غرامت از سوی کشورها، سازمان‌ها و افراد حقیقی و حقوقی است که در جنگ تحمیلی گذشته خسارت‌هایی را به جمهوری اسلامی ایران وارد کردند. در غیر این صورت، شناورهای متعلق به این کشورها نیز با ممنوعیت عبور از تنگه مواجه خواهند شد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/akhbarefori/687541" target="_blank">📅 23:36 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687540">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
معاون سیاسی نیروی دریایی سپاه: روزانه ۲ تا ۵ شناور در تنگۀ هرمز هدف قرار گرفته شده‌اند
علی محمدی:
🔹
در ۱۰ روز منتهی به ۸ شهریور، نیروی دریایی سپاه هر شب بین ۲ تا ۵ شناور متخلف را تنبیه و مجازات کرده و پس از آن نیز هرگاه اراده کرده با کشتی‌های متخلف برخورد کرده است.
🔹
حملات آمریکا کوچک‌ترین خللی در اشراف و تحمیل ارادۀ نیروی دریایی سپاه بر این منطقه ایجاد نکرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/akhbarefori/687540" target="_blank">📅 23:31 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687539">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
چهارمین حمله رژیم صهیونیستی به سوریه طی ساعات اخیر
🔹
نظامیان رژیم صهیونیستی مستقر در پادگان الجزیره، منازل مردم روستای معریه در حومه یرموک سوریه را گلوله باران کردند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/akhbarefori/687539" target="_blank">📅 23:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687538">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
واکنش سفارت ایران در آنکارا به بیانیه سفیر آمریکا در ترکیه
🔹
سفارت ایران در آنکارا، اظهارات اخیر سفیر آمریکا را تلاشی برای پنهان‌سازی سیاست یکجانبه‌گرایانه واشنگتن در قبال ایران خواند و تأکید کرد: تغییر واژگان، ماهیت عملیات طرد اقتصادی را تغییر نمی‌دهد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/akhbarefori/687538" target="_blank">📅 23:21 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687537">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd94871eaa.mp4?token=Efsc5WyZjjTIhThGZKnSsthkeXvpgI4Aq8xRQpXtQQgY_fVg_uTI6iTaQa9_mFiOBvVN9PUmd54qNA0z6tlibKi9zFhLn8ziXoI2i_8ZiVPPWsS936VdYNHlk9ch-soYxiKMwQJ8ZOgkZoviFSb4ZFzxV1P9aigCac9wvjrtecTNGL6-mxQPFogctrw7XUGOYimu3utzqbFGsMjyX-y_czSDSovl0pAhYYoGWXE4JFVsCVLNCVkhlXrPoS8_H7m2IUHy_MjuycMVit1-HOXhRavPNQlZgQKr_KUDpAcNOb26m97mjMxjWunId-iBo46qO2DEna6S1xCppjxXIXAtwb6wDIrSfolDJwOuuTdfqVXgGZsVxsa0mYaJ9lLC2eWRzteFRYFIxFDkjcjzsNI-RmKoKx7xpZW1n5hO07xKWZ7uw3vY7QXP-SW5naRLa-eCcqCSglhx10swlzT0O0bqWn5R1AcbhkOosNiFWtvNKKy31G07MyA8vkqhDxooT6IR5STZUpfb4EiaFPUFXDeNj-0cujWNeS98y2gFrxgMzNvs4bBSeW5wna-P-E2YtiwvwTqNfTXnKIWbhZJj4Y90KFFcnenHoLW1-EbX-kMilh3dzziRa1KrHoHIK2yjwaU0rY9af7NLqETLB11bJY2vMdP9GHioHs9RUrWG8AoWxHo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd94871eaa.mp4?token=Efsc5WyZjjTIhThGZKnSsthkeXvpgI4Aq8xRQpXtQQgY_fVg_uTI6iTaQa9_mFiOBvVN9PUmd54qNA0z6tlibKi9zFhLn8ziXoI2i_8ZiVPPWsS936VdYNHlk9ch-soYxiKMwQJ8ZOgkZoviFSb4ZFzxV1P9aigCac9wvjrtecTNGL6-mxQPFogctrw7XUGOYimu3utzqbFGsMjyX-y_czSDSovl0pAhYYoGWXE4JFVsCVLNCVkhlXrPoS8_H7m2IUHy_MjuycMVit1-HOXhRavPNQlZgQKr_KUDpAcNOb26m97mjMxjWunId-iBo46qO2DEna6S1xCppjxXIXAtwb6wDIrSfolDJwOuuTdfqVXgGZsVxsa0mYaJ9lLC2eWRzteFRYFIxFDkjcjzsNI-RmKoKx7xpZW1n5hO07xKWZ7uw3vY7QXP-SW5naRLa-eCcqCSglhx10swlzT0O0bqWn5R1AcbhkOosNiFWtvNKKy31G07MyA8vkqhDxooT6IR5STZUpfb4EiaFPUFXDeNj-0cujWNeS98y2gFrxgMzNvs4bBSeW5wna-P-E2YtiwvwTqNfTXnKIWbhZJj4Y90KFFcnenHoLW1-EbX-kMilh3dzziRa1KrHoHIK2yjwaU0rY9af7NLqETLB11bJY2vMdP9GHioHs9RUrWG8AoWxHo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر کار دولت شهید رییسی: رشد اقتصادی کشور در دولت شهید رییسی به ۷ درصد رسیده بود و اگر دولت ایشان ادامه پیدا می‌کرد رکورد رشد اقتصادی ۸ درصد را می‌شکستیم/ کاهش ۸ میلیونی جمعیت فقرا از اقدامات دولت شهید رئیسی بود
صولت مرتضوی، وزیر کار دولت سیزدهم در
#گفتگو
با خبرفوری:
🔹
میانگین رشد هشت ساله آقای روحانی پایین تر از ۱ درصد بود. برنامه مصوب مجلس ۸ درصد بود و ما در بازه ۲ سال و ۹ ماه دولت شهید رییسی با کمی فراز و نشیب به رشد ۷ درصد رسیدیم و اگر دولت تداوم می‌یافت برنامه داشتیم رکورد رشد ۸ درصدی را بزنیم.
🔹
زمانی که شهید رییسی دولت را تحویل گرفت تعداد جمعیت فقیر ۲۷ میلیون بود اما این جمعیت در زمانی که دولت شهید رییسی تحویل داده شد به ۱۹ میلیون نفر رسید
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/akhbarefori/687537" target="_blank">📅 23:15 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687536">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Os7Sf195R3-dyNltpumYmhdAlcrsP_DLUYM8cmwV6bbsSahjQGDvm1qEyDS_hkx2pCB1ME38SFHtmhMgReCMlSTttvpk5wVABwETtx-czDJtxNSHGqTdExZLyLvf_KmrQzm0oQcT0IDTwWCvC1J8zJcBItm7NQ5Q1g2Y7WVJgbN3-LptXdJCtVtm0iWzjfZ08XvyH7ki8kw61gIyhM-kYjNPr4QxAa34Wx-gBCLoPwdLpkv5OZsX_rRQAOAygbVlf45W7NPhV19bpmf1kyHvjAnkb9zrw0luf8nWozMZIuZX5IwwsH-CJMRg3S7teJkncYfJtA2QrTFiKM8n0RGc9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقشه جهان قرار است واقعی‌تر دیده شود!
🔹
مجمع عمومی سازمان ملل با تصویب قطعنامه‌ای از تغییر نقشه جهان از مرکاتور به نقشه‌هایی دقیق‌تر برای نشان دادن اندازه کشورها حمایت کرد.
🔹
این قطعنامه با رأی ۱۶۴ کشور تصویب شد و آمریکا تنها مخالف آن بود.
🔹
نقشه مرکاتور شکل و جهت کشورها را حفظ می‌کند، اما مساحت مناطق نزدیک قطب‌ها را بزرگ‌تر از واقعیت نشان می‌دهد.
🔹
در واقعیت مساحت برخی کشورها از جمله  آمریکا کوچک‌تر از آن چیزی است که روی نقشه مرکاتور دیده می‌شود و کشورهای نزدیک خط استوا، مانند آفریقا و برزیل، بزرگ‌تر از تصور رایج‌اند.
@amarfact</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/akhbarefori/687536" target="_blank">📅 23:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687535">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xakr5X6DLPftok1a0-OycB26oLQRo46rh07acXmemnFRWfcQ6EFG7cbZSqEdRZDwMcwclbDLWWMXT5ET_M7aNmOwfPfqYw9pMZiDsBM8f6cdo6UYaW-1RY4YtEBtM9t_MQF37NBUM8fd2rNwYbzXNrmzxtMS9TKnMDguuTEdGxDfOtVOXkn_OPwHra4BZsz6wikZGOktBoVc5w0w1buyKCNJDKc7S1iVEM8Q5E0czvGierwx7nn6G5zCY8XYFqps60bfNLyhGU1roVpGIJZ_0i7CAKXS5oi6mKrmlaUHNkOO-vLFEf9T06sR1c__6YpqL9bCFHGg8BNOs2H55ieYAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار قاطع فرمانده نیروی دریایی سپاه: فریب آمریکا را نخورید؛ هر تحرک مشکوک هدف قرار می‌گیرد/ پاسخ به تجاوز ارتش تروریستی امریکا در حمله به سه فروند نفتکش متعلق به جمهوری اسلامی ایران
نیروی دریایی سپاه پاسداران انقلاب اسلامی:
🔹
بسم‌الله الرحمن الرحیم
والحمدلله قاصم الجبارین و مبیر الظالمین
🔹
ملت قهرمان و بپا خواسته ایران عزیز؛صبح امروز ارتش تروریست و متجاوز امریکایی طی یک اقدام وحشیانه و از سر استیصال در بستن بودن تنگه هرمز به سه فروند نفتکش متعلق به جمهوری اسلامی ایران حمله کرد که خساراتی را به بار آورد.
🔹
رزمندگان نیروی دریایی سپاه با استمداد از قدرت لایزال الهی و با حمایت و پشتوانه شما مردم دلیر و به مصداق آیه نورانی قرآن کریم که می فرماید :« فمن اعتدی علیکم فاعتدوا علیه بمثل ما اعتدی علیکم» سه فروند نفتکش در مسیر غیر مجاز تنگه هرمز و سه فروند شناور وابسته به امریکای کودک کش را در مناطق دیگر مورد هدف قرار دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/akhbarefori/687535" target="_blank">📅 23:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687533">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KLsxYGaDnqQzzVJd-WDL52lcSyTzJzr4Ef3C5I25t1tiwQU0Bf495WngHK2S_6sW4kmLAKcW83Anz5SMdG32OnjpnqK9eJK5zig-SGIjsQRCfbovgx3LGdCGTjlA0SXaTs2HCn7CyLoVhmbWo73pipruXB-zVMI5Y_Wr7qHu7rO9CS8oqwBmysbGcrUGXCV5aPHYXCS1I2-bdFVPKJ_Y6DiLVyELYXSsh4wWMMrhghAJ-gutSszvEvifvwKj3caYP1Qi0kz-b-lMuyirS2uiIBUMDkkOaGXHt7O34w1ldg7Q9AQYNaYt8_EY5lS0Ll6bVfROAXukbSY_j0ip3JsNhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/484016062d.mp4?token=XwK6m1hNvUuNz1N1qvsvmDpKxC3-OkGlD7NwXqm4TCm9U3Jt93DTslvQKHwS4oQN57n8wmkTOJMrAy_Q09n8g1HqQRJ3s8Lfph9B96WVqpsukWp7dCUE9DAHR4CcGWIWGzOyNf_LSZG54y8Z0raQ6jfdqnntH-ASKvUVYzegqQjennQxp9ptINxxDe74tXdzXv4ACsYEf9ro0M8mRpBFZIEudIyzk8MUP9brEH6xKA4izw7p8tcvCSa79yW8wbMmLmjyZBB49yBIpRyTjCS79zYX31qDt3z9O1itgoRet0MtjpJtyo6kXaqA7Rvsb8pVrvu2d6l_jYFWPieAcT6tNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/484016062d.mp4?token=XwK6m1hNvUuNz1N1qvsvmDpKxC3-OkGlD7NwXqm4TCm9U3Jt93DTslvQKHwS4oQN57n8wmkTOJMrAy_Q09n8g1HqQRJ3s8Lfph9B96WVqpsukWp7dCUE9DAHR4CcGWIWGzOyNf_LSZG54y8Z0raQ6jfdqnntH-ASKvUVYzegqQjennQxp9ptINxxDe74tXdzXv4ACsYEf9ro0M8mRpBFZIEudIyzk8MUP9brEH6xKA4izw7p8tcvCSa79yW8wbMmLmjyZBB49yBIpRyTjCS79zYX31qDt3z9O1itgoRet0MtjpJtyo6kXaqA7Rvsb8pVrvu2d6l_jYFWPieAcT6tNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای فاکس نیوز: نیروهای آمریکایی پس از آنکه ایران به دو کشتی جنگی آمریکا موشک شلیک کرد، سه نفتکش ایرانی را هدف قرار دادند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/akhbarefori/687533" target="_blank">📅 23:07 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687532">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f6a40b18d.mp4?token=FaCteOnp3qgRTDgV0DwDjq1lBgRbEpdbjh4ZBTkIgQPiP42uc5YuWikyFZb_NtypDWHvDN9GrFWqZ9GC_Za6XZC9MeaoW8eCeuIfvEKBv9KG5YxrXbLk6vOrAbR2erpuhC0x0tCZJ9ZMkRcTaPv7lOjW_PbKDqjSuUaOnRNOcedXG9Fhr3a1Pd4ZPplTBxhkj0XqRoli_lGji-sHwgLfLkBeJrben2gAPVj8yyiPu4kiCv0LE1fV50H5a1w3uCqWbUmFvQBTPEvm-mo8Xv2-xkfiPCRLK8iiyad2YhYHO3zkU4cEoBuO9I7QlqUJxZ_BisiQ2xI5Bsva6FnnCTgrf4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f6a40b18d.mp4?token=FaCteOnp3qgRTDgV0DwDjq1lBgRbEpdbjh4ZBTkIgQPiP42uc5YuWikyFZb_NtypDWHvDN9GrFWqZ9GC_Za6XZC9MeaoW8eCeuIfvEKBv9KG5YxrXbLk6vOrAbR2erpuhC0x0tCZJ9ZMkRcTaPv7lOjW_PbKDqjSuUaOnRNOcedXG9Fhr3a1Pd4ZPplTBxhkj0XqRoli_lGji-sHwgLfLkBeJrben2gAPVj8yyiPu4kiCv0LE1fV50H5a1w3uCqWbUmFvQBTPEvm-mo8Xv2-xkfiPCRLK8iiyad2YhYHO3zkU4cEoBuO9I7QlqUJxZ_BisiQ2xI5Bsva6FnnCTgrf4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس قوه قضاییه ایران در اجلاس روسای قوه قضاییه کشورهای عضو بریکس حضور پیدا کرد
🔹
حجت‌الاسلام‌والمسلمین محسنی اژه‌ای که به هند سفر کرده در روز سوم سفر خود در محل برگزار اجلاس روسای قوه قضاییه کشورهای عضو بریکس حاضر شد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/akhbarefori/687532" target="_blank">📅 23:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687529">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
سفید شویی حمله هسته‌ای به ایران
🔹
از برخی چهرها و رسانه‌ها، زمزمه‌هایی مبنی بر عادی سازی حمله هسته‌ای به گوش می‌رسد. آیا این اظهارات صرفاً مواضعی پراکنده هستند یا بخشی از روندی برای عادی‌سازی چیزی که تا دیروز غیرقابل تصور بود؟
🔹
در این ویدئو ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/akhbarefori/687529" target="_blank">📅 22:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687528">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
ارتش آمریکا: ایران به یک ناو هواپیمابر و یک ناوشکن موشک‌انداز هدایت‌ شونده آمریکایی حمله کرد
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/akhbarefori/687528" target="_blank">📅 22:44 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687527">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
وحشت نهادهای امنیتی آمریکا از گسترش جنگ با ایران
🔹
شبکه ۱۴ اسرائیل شامگاه امروز اذعان کرد نهادهای امنیتی آمریکا، به شدت نگران گسترش جنگ با ایران هستند.
🔹
این نهادهای امنیتی ابراز نگرانی کردند که احتمال دارد نیروهای مسلح ایران تصمیم به تشدید و گسترش حملات خود بگینگرند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/akhbarefori/687527" target="_blank">📅 22:43 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687526">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
استاندار کردستان در پی انفجار تانکر سوخت ۲ روز عزای عمومی اعلام کرد
🔹
در پی حادثه دلخراش انفجار تانکر حامل سوخت در محدوده پلیس‌راه سنندج ـ همدان که تاکنون منجر به جان‌ باختن ۱۱ نفر و مصدومیت هفت نفر شده است، استاندار کردستان، ۲ روز عزای عمومی در استان اعلام کرد.
#اخبار_کردستان
در فضای مجازی
👇
@akhbarkordestan</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/akhbarefori/687526" target="_blank">📅 22:38 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687525">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6EMwo5SPprbLAfQyuUOfWubA2MrxTAIN-JpgtL58h_bl-0SkaGCzF9GXbEEh9XdCGaow3vYeOCNzy12KhEo-eJgty--I6AJWg_SOJ0whLO_PMf0ZbQ5BVWbsEkLF01KfNOeFeBtWq1ykPTuO7gqQf5ABQq3RXHfnlzUDlCo1ZqJQmlrGmZAZghdlx1OrVgxJwuwv8iPci9Dt8Zd71QZQPQZop8JgomDNAqhZHVnrqceAgtM3W7g-Jssmn7zIoiZ_JyyAEy1PXTiaCi0zC03fTgdc4psRp8OZmpryCqpmmHKyImhkj5pjYsDOVpkqycZbEvD56Y7Y__VG-QuJeZIig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کشف گردنبند ۵۰۰۰ساله از جنس دندان
🔹
باستان‌شناسانی که در حال کاوش یک تپه‌ خاکسپاری ماقبل تاریخ در نزدیکی «وروتسواف» بودند، یک گردنبند خارق‌العاده ساخته‌شده از ۴۲ دندان را در کنار اسکلت یک مرد بالغ، سلاح‌های سنگی و بقایای جمجمه‌ انسان کشف کرده‌اند.
🔹
در بررسی‌های اولیه قدمت آن ۲۹۰۰ پیش از میلاد تاریخ‌گذاری شده است که به عبارتی دیگر می‌توان گفت تقریبا ۵۰۰۰ سال قدمت دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/akhbarefori/687525" target="_blank">📅 22:33 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687524">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k9dRQrm7HWwBklyKbd213d-405NtDS9tNAy5kVkhaTWMQSN-MTW4VevdSNwbFIfgmA3HjBwAw7CyXKEveRjd3lw9HcJ0vJdiBVs-v72CH44B5Ven3xRrZNmi7MmicM9FpDqVvdQ9sh70GsAgmE0Nu6RUL4Drd8Qhc_2E5Qs3jfYUonB4pOfyFPiI30zQpH0rGGNO602PhQBzim2nMLFFttegknR8M01MzWFdbInS-2ds4KEuEFF_8-B6ndPelrcuWDt2-eKLH_e-R4Z2BRYCq9gy1J3qV8aBDbq09npBrtzbPLYbNF4EY_FzsukEY2tyNSotDXNJvHWuqGENAQMO4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سر در برابر چشم
🔹
با شروع بازی خطرناک نفتکش در برابر نفتکش توسط آمریکایی‌ها، به نظر می‌رسد راهبرد سر در برابر چشم که پیش از این روبیو آن‌ را برای مواجهه آمریکا با ایران پیشنهاد کرده بود، اینک می‌تواند به یکی از راهبردهای ایران در برابر آمریکا بدل شود؛ حالا که نفتکش‌های ایران مورد هدف دشمن قرار می‌گیرد، چرا باید خط لوله‌ها و بندرهایی که تنگه هرمز را دور می‌زنند به راحتی به کار خود ادامه بدهند و سالم بمانند؟
🔹
هشتصدوپنجاه‌ودومین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/akhbarefori/687524" target="_blank">📅 22:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687523">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/akhbarefori/687523" target="_blank">📅 22:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687513">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d0Ne8o1PIwjnCQ69ZGD9Sc2wlUmCSaIW8DnskA8KIUKb83869jJ33t4w_k470foiky1xosb44mZUf81JQ-KbdcMjBbkZAtSGsuF60V2v7oa9XeFr-B0fRj_Bz9nReZSPrUjh5ZroJzV3_bjit7OS7EEPjZeS2V71zm7dIAvEGlP4RyvBajwQ3qYoFpSYaCr2tb53RJJbVQaYE9FC66XPY1MY84vi1lr_1VZ7kIPb64-R2UJ21vaGweYJpVZ5UGxtCeBKTB00IV4Mpsc2_Da8XVqXTDjPJLKmDElDbz7UQFm6tQl3wyRCQb-JgAobcSb_plqXTldEeNZo0wDChXMf6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gjm5wK1Ze3kN4P4oIzlJm8w3DplwK4zy8Qi9rEbq-39uGvHxGBb1LPRWw7koh26mXqHBTL7OrBDw5Y83oxSXkAZleRa5dKapwl_Snt_DpgsJxUxsssvdy8Juu6josnaIJdtTDMNOIKCJj93bmlxw3GjFuPuWckrVuoM_pzctgknWMQCHccB6bWwo6kq3LuqOr3xf2EiHnaBFUdnU00iEqPWHSgli92fdXwblaIfOJTdH-jsSDyYWDeJBNJgS9bqyNaz6FgKVZxEPnJNAQSYNQQLGy4pk3n4JQgK5L5Sjn9QdYuwKZtM_diNQ_b25sJjx8pRi2omQ9Af6cyK3z3JnQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y7CTRYCSQ89QsJESkC0lOJM7ILZjYJc28cINssq9g84sEGlZCwtFUBR2N9Xih43clbVM5YWHJVOfGYklr4kVZd_4aNRYA8asFn-75RxE-NaekVWCW4xhPZK9v9ojJkTDA416Ss6eL0fk7r_2cW9PhSMIWkEFQsU7koUPuAoE2oZvtqq8txO9ukOaHq2PiUBKt1QOPsk2d2gbIghOdz2GLPt5SyiqTQVnZ1GmBVZHkk5M3e9Dzq7oz7SqNVmhvVA8wbiEgYxO_cqP4zhnnuz4uGodpNF9RytVPTk2RR3y_kczrRki1ruj-sSwFoL6ERpYyiXaoIc0gAEZFDHVxBRMXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I1IGV6_Wh_YA1bp1mRVlGpWrCH-XkzQsvr-WYOdMlu7OKarpMiFzROYZ6lkMQ0A5r56HEVGT5Ag8g5bnR8clyw1C7CeC97H89G9FpVBAOTtIJE6I9JLgZ-N7a_2MR1roG9ixg9ReaS8S1PoRM9luEJMQqL_w9Wvmeke6nuQsnjrQX8xEzJ4ut6gM15IFUuJkOugsdEom6spicD82AdPcYkIv2kXAn1MQkscLjutKlrcwc0ujOl5_tZrv6Cg6PDvWP1UfpmDSgKxEiqjZzIHpYsOVOJ43-tcCBLMI5spabJghFCN9DYAP9w2PaqhRRVxAgqQuc4X3n2roZQ3DVEKqDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l_0JGQlERSZZPsK1Q72ZFLZ6Qnv0xAsXMtJ2aft6u8eBIGumpYIviv6-6FkwXUX79gq34Ah8UHabN0oPMRn-MdoiNP4RbVWVu8lUDT-i0lZDkNuBSoSLnj38nTtBqG6hWy5A95GNPBlAgrnGcKPPEZvNyXPDdjagZHsVZDczS2MTJ-fNXrxExABf8UZvt5L3oMHUrSezYerzqw5Zb8-hfejrT7Pujj7BWr00JRhHGVXe-R9VnjlTahwiWoDA1DbZqtL-N68mgbZmEy0ts8DiRIOUHBglQY--UqJUCLHbaUlAZtS5uPKzHQ7EUsbyqKANH8nOEjWYAEY2RBJ87GKF0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uTEzPoorykQ4TCP867kbKDDpnstepPBZgHGEe3XwZkjVTq1qzDGeshUNuTzwsakp5j6LBIqAToLN4aEnuBaqjM8c4vaKBJ7nnhb2msjfkf0PC70cHSxGDLlp-gGkMF2ujLB_kp9Yxrr5YR5remewK_I6j5xzfVXZi1bg176_f2WtfC5_zPEinUvNiqvd4KTKwpAcH3VNwws89gSPy9LRLlYga8pxP72R-BdPj-nGM6Uh7689eaT5i6O2KRSgBkbOOcVgZrMPoqeZgzd7ctl65OWRjq0WQ8rEceja4a-UcjGxz2aJVTS-vDs8wlN_vT-XTEUfm-Xmle1fuNSuAObBXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cI7yQCxX_XABWxpYnThHeRUq6pFvjJLIhh1ha_GAXsNYIVybut_CnxkJohdhszzNc_AJP0lvSDcVXty8PqQNJTFf4Ig5VYtEY7Xh990Qxfb3q5DBKMPRzcIdcnRDDYf-iT9pBHDLi3wvXlJbCTcqZXg9i6MxQ5zJFV3AeHTj_YB9wVNtz5hHmk-qBCCMxZj-UWFC-rDqohy02R_51GUvbGu0xgfKIbikFmub3VHyo6e-1bxRTAnJlUnOFOlNP-8qAKTtOPLBbwrTxU0mjpYX9WdSvOxpMcl3Z9unYY7BuhhCzP9dMcwT297rvDf_RyRrHP-0JPJX1nP0DpHGDs-xGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cb1BijU4m09iXYIMgguIKC3oweMCCsi_XAt2pxVuKh4K4Yn90MmiD6_mHu0lEMVC5pnuGrAwKmQZBHMhEIgEIEHS6JCq2bruL3dTdkw6azYDTJKP-tCgSqzcS0Xf1uaA3JVbvRzDHOll_c7HIlggCzK2yYQRTodwSQH4tkYAlvr1ZK3kHG1xX5pCUPWZs17eXe0CufncojQNvM2RIlt3BBoQ1bpZiuDHCoMBt6zRWCF_gZ-tMG-ha5VerGXBtvP7CfqwSfRAcn6gdI78BiFfTA_I9h4v9o_MjIw9G6ReTe4p5ALtEETVg_Y0ANBlEVWefGvEV7V5L4DTmvrz4CxAsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/twRVn_Nz1wFTByon9_NRBZaFRCmocTRqj8egPu0QqdBYQI3dwQBHmqcJ_PGJJXhn4fGgiWZh2vY-bkFsjyrRPjHSsNQx2LtLmgeELOWvGw0eEapJSnjMkcdREM4dG60rKkZcSylJQLGzN1f9cKBvC1wh2HwTKNNidP4Hk90XJ2mAyjmV-7SChdM-mmpgW3EDoVI-1-gT7cot9247x3X_5BrFBNEO4aO-29F4siHSYQpYsRSdmDuvQ0JxVailJEFBI4-b-iprVGCziLbPykHZfwJb-jQ4ptp-hQ7H0BV50m7DGpy_jsWQF8lauGt__MkbaUUCrNfvS6lOckGPFznTQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aPwVx4Ch3CCwXGmvxWJTxsUu2dmiLqhQgFYpF3tr10t3Kv8or15nTARW-Xn34tQIFnULm7nSHIbtfQq026Pgo53xAEhaw6R5yGs9NLkPzB0Eob-DamLIoyycS3o8OgCDkKq8vnkVx4KPWz1bjWAmsrn6tOHVkVxAZ90Hagn1yZ0YH3g56Kt1v2Sk0YWW4Aa89Ngf1zuyWcQ3aE3-NHkKoaVg11sHKr4cUjp1OHLmcniOmH3gC-t_d1AqTSE5VDuknnP3yhtO0dnpbVAkAFSkGuHDnFD5tVkiJubD5uFG3BjLzPCtRejwt9N_4Je13EhGCge9rvQ0j3xebvKmsGK95w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
درد دارو
🔹
انعکاسِ مشکلات مخاطبین الوفوری برای  تهیه اقلام دارویی ضروری .
🔸
ما پیگیر مسائل و بازتاب‌دهنده دغدغه‌های شما مخاطبین عزیز هستیم؛الوفوری را دنبال کنید
👇
#درد_دارو
@Alo_fori</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/akhbarefori/687513" target="_blank">📅 22:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687512">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
اولیانوف: انتظار می‎رود موضوع مربوط به ایران در نشست شورای حکام آژانس بررسی شود
🔹
نماینده دائم روسیه نزد سازمان‌های بین‌المللی در وین اعلام کرد، مسکو انتظار دارد مسائل مربوط به ایران، سوریه و اوکراین در نشست ماه سپتامبر شورای حکام آژانس بین‌المللی انرژی اتمی که روز دوشنبه آغاز می‌شود، به‌طور فعال مورد بحث و بررسی قرار گیرند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/akhbarefori/687512" target="_blank">📅 22:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687511">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZD0iTl-8bZkwvAfeYePNU693anqZBFAVy6mbIoq6wCY711mcswgmrVfiBJR48ChojM8WagYrw7eURlFrD7Y4jtkJDmfVZ1BRxCDtmyiShq0Q7hjnGR8bXXFSzbLIZk92IuflvzG3JRMUJXtTr71cP2IDiORrqLfaGsp64ALxZg0s9KLbrudt_zogi7h0L5vmCD6aXiKBaRDbrebLn2uUwP08DO449hCk-2RMD__3uPOvsorw97bRelJht4gNcuzRYT1EgyAG1VjN3U_QHfLj1SyTII8Fc3S_rPgTIdRyBjDgLz1ewE8OZiKggbj7n1nTcOxLwwEnRppX9cxh2-6LJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ماجرای اعزام ناو از کره به خلیج فارس/ ایران با کره‌جنوبی وارد جنگ می‌شود؟
🔹
به نظر می‌رسد در صورت اعزام ناو از سمت کره‌جنوبی به خلیج فارس، ایران عملیات تقابلی شدیدی را آغاز خواهد کرد، چرا که این مساله می‌تواند سبب به هم خوردن تعادل جبهه ها و باز شدن دروازه ورود کشورهای خارجی به خلیج فارس و کمک به آمریکا می‌شود و این اصلا برای ایران خوب نیست.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3242872</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/akhbarefori/687511" target="_blank">📅 22:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687510">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EI1q0636gc_sEDF53KpULULAAQr_Sb2Q1UN2EVLmNLg9wTD2LEPzlM4Lza7VuBny3ajMw-VIEEN_HZysP_BKWwYiVFrkFuY-MNO--iyEs61TLUktqISXlj0AC6_BOFJHhipi3Ern0kDn9-QAVvv2WL5ukK5RWUYBzk1Uiifclyy_RYAIntjflaKMAsAfAWtSrZwDysLbSfFsLa5YAGZHBVDhs8UtlpGKCM-qB56fjmyf7wWVjYtwQC_WLXmFUsXzBLk5YjUtJi2oJ2Qs1OXHz95hZyhKW3EhkKzBwk9jzMYqyJhR2nWqBQysDz2wEBdTKHUWCI0v-U9Et6IJ1nN_5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توانایی، وقتی ارزشمند است که با خویشتن‌داری همراه باشد؛ قدرت واقعی، در کنترل خواسته‌هاست
🔹
امام علی(ع) در نهج‌البلاغه می‌فرماید: «هرگاه توانایی افزون شود، شهوت کاهش می‌یابد.» انسان هرچه بر نفس و خواسته‌های خود مسلط‌تر باشد، از وابستگی و زیاده‌خواهی دورتر…</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/akhbarefori/687510" target="_blank">📅 22:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687509">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
ادعای رسانه صهیونیست: ایران در حال آماده شدن برای یک حمله شبیه ۷ اکتبر است
ادعای جروزالم‌پست:
🔹
ایران در حال آماده‌سازی برای یک حمله هماهنگ و گسترده علیه اسرائیل در چندین جبهه به‌طور همزمان است. این سناریو شبیه به حمله ۷ اکتبر طراحی شده، اما با این تفاوت که از ابتدا برای گرد هم آوردن تمامی مؤلفه‌های محور مقاومت برنامه‌ریزی می‌شود.
🔹
بر اساس این ارزیابی‌ها، ایران به دنبال ترکیب نیروهای خود با حزب‌الله لبنان، حماس، حوثی‌های یمن و شبه‌نظامیان طرفدار ایران در عراق در یک کارزار واحد است./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/akhbarefori/687509" target="_blank">📅 21:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687508">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VglW0WEzJXA4CuYZtLBOqBaMSanRRz9XTg6U5wO6L98g8LBpKO3xSBXaAZ5ZQG1nqHKVbOgDtybsjGMWTIqjYFZ7H12cDAiuc06FmacRZdK7JBDJ1v1ZljFvjCvL6pSepjkeDQ3cxt-aMRqceH-I7ypO2ps1YlCYF0uIOq0REF0cgoIanH8FB2MTHs6CB7CDfN4eiNt6J6qZ5lM1F4BiBFo1xDuEChkW-mEhWT0gVKMLU2iW8PwblMUh25OA4FqHxa4sS6zXd5hhBhEGm9L1XEazAn8HXIgac4faj5pQjhno1KWdiRMpHHaS2LFyH5n5wrv6Ye8hl8RJbA_57wkZBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کارمزد خرید طلا در زرپی برای همیشه نصف شد!
🔹
از این به بعد کارمزد خرید طلا در زرپی به‌جای ۱٪، فقط
۰.۵٪
است.
🔹
یعنی با هر خرید، هزینه کمتری پرداخت می‌کنی و بخش بیشتری از سرمایه‌ات صرف خرید خودِ طلا می‌شود.
🔹
این کاهش کارمزد موقتی و کمپینی نیست؛ تصمیمی دائمی برای کم‌هزینه‌تر و شفاف‌تر شدن خرید طلا در زرپی است.
🔹
اگر طلا می‌خری، چه به‌صورت دوره‌ای و چه با مبالغ مختلف، این تغییر می‌تواند در طول زمان تفاوت قابل‌توجهی ایجاد کند.
🔹
برای آشنایی بیشتر با زرپی و اطلاع از آخرین خبرها و قابلیت‌ها، عضو کانال تلگرام زرپی شو.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/akhbarefori/687508" target="_blank">📅 21:51 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687507">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
سنتکام: ناو جورج واشنگتن مجبور به فرار از دست موشک های بالستیک ایرانی شد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/akhbarefori/687507" target="_blank">📅 21:41 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687506">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f5a97038f.mp4?token=iP1Ax3CWiBVpXN2mdrGTfR_VORzvLlt8d8JIleGvppU5YlTUugaUP6NBlRHwkCH5R5iQTyYD_jLI4WCYpSesq_3HVTok-v23bV5ct4_DzZk1n7MAeT0Y3lprYP-HbMHxZo-vW4hmqbT5Dqmvk_9N1i25C4F72rC2PPil3399DX430iOdTcYLcATbpEo4R84KmYQ2ttAv9LxJ0ULHo36xzddt2WFD5tCFZ2jj6i3JLAnr62DlPw-rBhyK02xbeghSAqZEMQjI21u7g_9zg0vGyLO48jPl1j8nX8agrpuKmEidrRUhc7y8MhTn4HRE-pCKTumMaumrKgeq6NLNXCbU2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f5a97038f.mp4?token=iP1Ax3CWiBVpXN2mdrGTfR_VORzvLlt8d8JIleGvppU5YlTUugaUP6NBlRHwkCH5R5iQTyYD_jLI4WCYpSesq_3HVTok-v23bV5ct4_DzZk1n7MAeT0Y3lprYP-HbMHxZo-vW4hmqbT5Dqmvk_9N1i25C4F72rC2PPil3399DX430iOdTcYLcATbpEo4R84KmYQ2ttAv9LxJ0ULHo36xzddt2WFD5tCFZ2jj6i3JLAnr62DlPw-rBhyK02xbeghSAqZEMQjI21u7g_9zg0vGyLO48jPl1j8nX8agrpuKmEidrRUhc7y8MhTn4HRE-pCKTumMaumrKgeq6NLNXCbU2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جان بولتون: هگست صلاحیت تصدی وزارت جنگ‌ آمریکا را ندارد
🔹
طبق گزارش‌ها، هگزت برای پست «سخنگوی پنتاگون» به ترامپ درخواست داده بود؛ پستی که با توجه به سوابقش، گزینه بسیار مناسبی برای او محسوب می‌شد. اما کاری که الان به او سپرده شده بسیار فراتر از توان و حد توانایی‌های اوست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/akhbarefori/687506" target="_blank">📅 21:37 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687505">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
حملۀ هوایی صهیونیست‌ها به علی‌الطاهر با وجود ادعای تسلط بر آن
الجزیره:
🔹
جنگنده‌های رژیم صهیونیستی شهرک المنصوری و ارتفاعات منطقه علی‌الطاهر در جنوب لبنان را بمباران کردند. بمباران ارتفاعات علی الطاهر در حالی است که رژیم صهیونیستی روز پنجشنبه گذشته مدعی «کنترل عملیاتی» این ارتفاعات و ورود به دو مسیر زیرزمینی در آن شده بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/akhbarefori/687505" target="_blank">📅 21:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687504">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZ5TBiJF0mODV4yyjOxvwbpucoy2a1GA2afhN0hspZruGzK-b_bCRKg9PoxNNJiij1phQnFTmnHrmYAVNAt7qXxWi8BO0faGLhiWqWWmkhP5uKtnPVXL9hoquXBSVHWCJ0qa2aLsKA5ZoLo3utAZ0jqRO7g55GJL4nmoflUoruYbwVSK5hmOBi4Ykn5RiZQ9Q0gkpEYqGUqHkiVpqEZFSRrdA0yXocu3SfuMffpJ2cV0jHRipJSus5QHORxmTsGHm781oUX5umHdnpVpDktzSY04_6MUcUSQz5IHIF7txN0oot7UppptZjmh8lwMRaHBSdR8fT_NSLuqdef8opl5MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محمد مرندی: اکنون تمام کشتی‌های نیروی دریایی آمریکا هدف هستند. هرگونه حمله به کشتی‌های ایرانی با حملات متعدد به کشتی‌های مرتبط با کشورهای شرکت‌کننده در تجاوز ضد ایرانی مواجه خواهد شد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/akhbarefori/687504" target="_blank">📅 21:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687503">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5fEE6Xmid7XEz7mzA2IDIB9zEfVm6PomtJBnBJLlZgk7rdaMP_NP8-fqp0cpT-rlgfwPO-_xhu4nxM8ZBFiTPA-UE6heVIFaComen2hJuRnMyXsn5ec6h6Bi0Pvt5rsTRmctHZnj7L-Gj5PTtVY1i3Uiv8dwoRncpV6a0R92zjMyDeoPDgNKHuaEcAxTmuxAY4iLN4TY8o5jj1eH9TE936GDtkyHTGSHDuRmtUhcGHlwzVJFpgKx-dLKqXVafuShFnLQ9mqcBAwa3qB9A4Bug4XfXLO3VvE_WG6nRto9w55rKjSb3Xy2GlSVC8kQ27AAv8EP2v7AgQ1TGz8fy3ALA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیانیه وزارت امور خارجه در محکومیت شدید حملات غیرقانونی آمريکا علیه شناورهای ایرانی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/akhbarefori/687503" target="_blank">📅 21:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687501">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
تذکر قاضی‌زاده هاشمی به دولت: ادبیات سیاسیون و دولتمردان اصلاح شود
امیرحسین قاضی‌زاده‌هاشمی در
#گفتگو
با خبرفوری:
🔹
اگر امنیت جلوگیری از جنگ می‌خواهیم و اگر صلح‌طلب واقعی هستیم، باید یک روایت قدرت به خارج که ما در موضع قدرت هستیم از ایران انجام دهیم و به‌درستی روایت ناتوانی دشمن را بگوییم، به جای اینکه بیایم به سستی‌های خودمان اشاره بکنیم.
🔹
اینکه ما بیاییم یک روایت ضعف ارائه دهیم که هنر نیست و امیدواریم که ادبیات سیاسیون و دولتمردان اصلاح شود و بعد کم‌کم شاهد توسعه آن در ادبیات مردم باشیم. به نظرم ما هنوز به این بلوغ نرسیده‌ایم که فصل انتخابات با بعد از انتخابات متفاوت است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/akhbarefori/687501" target="_blank">📅 21:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687500">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22a6521f5d.mp4?token=GItTsLAKorWs5EQNgzyhTD_FNi2Mm8WorQ6FtX0JKim3Y1c9pQFxs5GcMaD5nMoyq7Dl-ptQy4aU6pDidozEN3qc5xauyt9T_1cRSL4lrvbxpjtNEz-VMoS70P18yBh5mxfEe9iVehxrMJr3H-VffiCLeDxavrbV0UcfjUaQRDLhZxVSlQZChWjYwWWzigfU1W2yjBm3SNf666O-OrBg7YvrGU9W-5AUZeQaU7FZO4FGwLpstJbyqY-xIEz5hBxs4k7Bd6ROKqEClqEov6QrRJBwyuohqeevZkg2axvq4mBQ8osJ1b4WV9jrMhcQWiNqX6z1T10JzaBNsJWakpKhkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22a6521f5d.mp4?token=GItTsLAKorWs5EQNgzyhTD_FNi2Mm8WorQ6FtX0JKim3Y1c9pQFxs5GcMaD5nMoyq7Dl-ptQy4aU6pDidozEN3qc5xauyt9T_1cRSL4lrvbxpjtNEz-VMoS70P18yBh5mxfEe9iVehxrMJr3H-VffiCLeDxavrbV0UcfjUaQRDLhZxVSlQZChWjYwWWzigfU1W2yjBm3SNf666O-OrBg7YvrGU9W-5AUZeQaU7FZO4FGwLpstJbyqY-xIEz5hBxs4k7Bd6ROKqEClqEov6QrRJBwyuohqeevZkg2axvq4mBQ8osJ1b4WV9jrMhcQWiNqX6z1T10JzaBNsJWakpKhkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ثبت حضور پلنگ ماده در منطقه شکار ممنوع کوه سفید/ پریزاد نام پلنگ جدید شناسایی شده در دماوند
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/akhbarefori/687500" target="_blank">📅 21:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687499">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4f970358b.mp4?token=GXq8qISXklNNxOKbawT4YxpBspGDyPtnN7Q9TqSp1uvn2uI16jds7_zf0-PnS6xsBETeSsG9-4I2_o12BBWpNb26foJMCnf9HaxlJeBZCG3zRfj-qR0cTAhstByr7hTPXXxxiPTjfpJX8ayo5GJbGpgszGIB7iJlWm7I0qGHbVyMIcw9rR9iXIHXjiEoP1OExKQs1a29iR3s_AyH36eiAAo469AcseZVN-pagEjFGxyCLnKae8qDNnM4hJ2K-FOiUMuLEahaRBTlJPn2t1VEhz6UuGJIMGZSNRtfKZlyv45lqY0fVY8guvSeFeaIhucTtMKaUN4O54rrDprPAxKeDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4f970358b.mp4?token=GXq8qISXklNNxOKbawT4YxpBspGDyPtnN7Q9TqSp1uvn2uI16jds7_zf0-PnS6xsBETeSsG9-4I2_o12BBWpNb26foJMCnf9HaxlJeBZCG3zRfj-qR0cTAhstByr7hTPXXxxiPTjfpJX8ayo5GJbGpgszGIB7iJlWm7I0qGHbVyMIcw9rR9iXIHXjiEoP1OExKQs1a29iR3s_AyH36eiAAo469AcseZVN-pagEjFGxyCLnKae8qDNnM4hJ2K-FOiUMuLEahaRBTlJPn2t1VEhz6UuGJIMGZSNRtfKZlyv45lqY0fVY8guvSeFeaIhucTtMKaUN4O54rrDprPAxKeDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با این کدهای مخفی خروجی‌های خاص و متفاوت از هوش‌مصنوعی بگیرید #هوش_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/akhbarefori/687499" target="_blank">📅 21:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687498">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
خبرنگار صداوسیما در جاسک و قشم: صداهای شنیده شده در این مناطق ناشی از تنبیه شناورهای متخلف در تنگه هرمز است و در این مناطق انفجاری رخ نداده است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/akhbarefori/687498" target="_blank">📅 21:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687497">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
سخنگوی قرارگاه مرکزی خاتم‌الانبیا: به ارتش تروریست آمریکا هشدار داده می‌شود در صورت تداوم شرارت، ناامنی و مزاحمت برای کشتی های ایرانی و محاصره دریایی ایران، ضربات نیروهای مسلح جمهوری اسلامی ایران علیه شناورهای نظامی آمریکا در منطقه شدیدتر از قبل خواهد بود و امکان گسترش آن نیز وجود دارد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/akhbarefori/687497" target="_blank">📅 21:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687495">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSNYNs4HN0pdFSMxW0BM9uUxpE-QJlypN8gHds6dvzIHsoyBDGK6CABpgGxcdIfQbDrJ2pt0znQ9PDz1WNMZ8AS-z8CFIHOJHDbWqi4WC_Yd82nbHK0V8l2USZ-8ShpN5_Enc4rVEqtFLDmwna4AshrtffHTXzi8gq4QtVnaEs9mVKIQwgdRJELP2ZV4Baw5Svrt959m4-ipOdI_0CjQOTv-oYZlvM6kaQmIBP2YnYO253paxYVWuvWcuhDGLqNJ_UHubz7PLF9Q0551MLY4xY_VAv-89D9HbEUBykeTe-u06aNrs26eQnyi5VzhcxCiWo4lb7-stg0GoQpMK1648g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رهبر معظم انقلاب: امروز روزی است که چشم‌انداز غلبه نهایی حق بر باطل، و اسلام بر کفر به‌مراتب بیش از همه‌ ادوار گذشته به عینیّت نزدیک شده است
🔹
بخشی از پیام رهبر انقلاب اسلامی به مناسبت هفته وحدت | ۸/شهریور/۱۴۰۵
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/akhbarefori/687495" target="_blank">📅 20:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687494">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
خبرنگار صداوسیما در جاسک و قشم: صداهای شنیده شده در این مناطق ناشی از تنبیه شناورهای متخلف در تنگه هرمز است و در این مناطق انفجاری رخ نداده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/akhbarefori/687494" target="_blank">📅 20:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687493">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-RR59dutna6g4zvtTrbgRH-HhecBZq4S1BuXTOAVtF5s2BD05oGJQydMA_1jPM8zpzPYVq7Xk-BXedOBRCWCWkPFbDcrhEwNWhz6Snv3Ux_RaYtWu_8garzz6Fe1o6J41K1R2cBGy0IAqDK5b-q4psP-AmTiLtXos4Visr3MSM_6tTIHjSi5YzpY0gDWtpKqHsr85wkO3zDDGGt2HtxrjxQSOlMK2wr6JPNbFB-d1wuucrr2HPbylsSExRX0CryTX_ueKliKuH-XiPwGJIZHu7k2gqsRUr90W7Q_zamoEpuvFbnlUJ_XcQpzH4gilC2FH5v5jg8Xu197QDP5txp2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
افتتاح متمرکز هزاران پروژه‌ خانواده ارتباطات در سراسر کشور
🔹
رویداد ملی «یک ایران متصل» به‌زودی با حضور جمعی از مسئولان دولتی و فعالان حوزه ارتباطات و اقتصاد دیجیتال برگزار می‌شود. در جریان این رویداد ۷۹۴۷ پروژه ارتباطی و فناوری اطلاعات در سراسر کشور با برقراری ارتباط مستقیم با ۳۱ استان به بهره‌برداری می‌رسد.
🔹
«یک ایران متصل» قرار است تصویری از دستاوردهای دوساله وزارت ارتباطات و تلاش خانواده ارتباطات کشور برای توسعه دسترسی عادلانه مردم به خدمات دیجیتال، افزایش پایداری شبکه و تقویت زیرساخت‌های اقتصاد دیجیتال ارائه دهد.
🔹
هدف نهایی این طرح‌ها، کاهش فاصله مناطق مختلف کشور در برخورداری از زیرساخت‌های نوین و نزدیک‌تر شدن به مفهوم عدالت ارتباطی است./ ایرنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/akhbarefori/687493" target="_blank">📅 20:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687492">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
مورخ برجسته اسرائیلی-بریتانیایی:
طراح و معمار این جنگ نتانیاهوست؛ او یک روان‌پریش نسل‌کش است و هدفش نابودی ایران بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/akhbarefori/687492" target="_blank">📅 20:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687491">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/051a0fae8d.mp4?token=phhf4toChYAj2IJf8bbeI0IeRl_cR4bW38glBHaFxEms_9HmVfZYkU5hdxVOneNbjSo1OWnZDhsT09UaVwZqtQqwCbHtYN6EDGnAP_bISyFVVEtRkfJuK1wKZE_da0Fp3jn0lDPDe0boyCFkW1ZH6vOjU2zpdUFo5TkTv4vXMMmXhsg4LKL6H96_v6qvkJ8p-dsbJwxmXKutBu0MlbcfQcbvTZTnFXe63oyybTvQVdgsmnwCRaaYlLV_t2xsyiD-lc3mS3TLzhNpsmKDeQNGAuBMLRPVsmbiQNRuQCRTkv2Yt0Iq5MgGzqRYKXNox_wshZBaMQNxpdGz97Ss9s80sJu3dgm3y_xFnGPbI7G7jKE0Zx2O_XQkDFJX2bvz0UwjQKjlrNRsRy45DJhp-cRjEDynFyM6Ro3wVhQqLsNjN4e3OdiIe82rgZa0oIHB-wY4lNETTqErfOMUYuylRGE7iAuMfsGWVHBNiX2AUs5jy0I6Vnyed8XsoT2yJA-UUHdqglpK4-BLLZAm-CMaV2m0FbHyR0bsoLKIYEb69v-EItReIdl-3Na259EeBFfBcY5X55fNZpdtCpmIfdU43AfRmYbPkBVKXfZM5ZJAqT3Nub6_8oDKTOx20FwrvDWA7R4XS-srlXY35uPr5n2jiKs4awUS7UfK_osEPMdwUZgSNWY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/051a0fae8d.mp4?token=phhf4toChYAj2IJf8bbeI0IeRl_cR4bW38glBHaFxEms_9HmVfZYkU5hdxVOneNbjSo1OWnZDhsT09UaVwZqtQqwCbHtYN6EDGnAP_bISyFVVEtRkfJuK1wKZE_da0Fp3jn0lDPDe0boyCFkW1ZH6vOjU2zpdUFo5TkTv4vXMMmXhsg4LKL6H96_v6qvkJ8p-dsbJwxmXKutBu0MlbcfQcbvTZTnFXe63oyybTvQVdgsmnwCRaaYlLV_t2xsyiD-lc3mS3TLzhNpsmKDeQNGAuBMLRPVsmbiQNRuQCRTkv2Yt0Iq5MgGzqRYKXNox_wshZBaMQNxpdGz97Ss9s80sJu3dgm3y_xFnGPbI7G7jKE0Zx2O_XQkDFJX2bvz0UwjQKjlrNRsRy45DJhp-cRjEDynFyM6Ro3wVhQqLsNjN4e3OdiIe82rgZa0oIHB-wY4lNETTqErfOMUYuylRGE7iAuMfsGWVHBNiX2AUs5jy0I6Vnyed8XsoT2yJA-UUHdqglpK4-BLLZAm-CMaV2m0FbHyR0bsoLKIYEb69v-EItReIdl-3Na259EeBFfBcY5X55fNZpdtCpmIfdU43AfRmYbPkBVKXfZM5ZJAqT3Nub6_8oDKTOx20FwrvDWA7R4XS-srlXY35uPr5n2jiKs4awUS7UfK_osEPMdwUZgSNWY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افشاگری وزیر کار دولت شهید رییسی: برخی کارکنان موسسات نفتی و پتروشیمی بیش از ۲۵۰ میلیون حقوق می‌گرفتند
صولت مرتضوی، وزیر کار دولت سیزدهم در
#گفتگو
با خبر‌فوری:
🔹
در طول تاریخ افزایش کالابرگ و یارانه در هیچ دولتی به اندازه دولت شهید رییسی افزایش نیافت.
🔹
در دولت شهید رییسی حقوق حداقل بگیران ۱۷۰ درصد افزایش یافت. در سال ۱۴۰۰  با تورم بالای ۵۰ درصد دولت را تحویل گرفتیم و با تورم ۳۳ درصد تحویل دادیم.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/akhbarefori/687491" target="_blank">📅 20:47 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687489">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ee0880e45.mp4?token=Mv7iimG4PtJDZoneD3x7rLrmWUiIS4UwVPaQyJ5-KbY56KGukXPO_lE1v7msxwH6unSPi68U99P71u1jcd0sE6usEV8P93DW7MsHNPV7IUabp9kh9hAFArUTPzkVTXLblLdyBJuHM9KunBsVpORg0FrB3vEO0zcgxChzMYIdyI00c71La15lHl6CM3x787CGaxXAdvnkelRHIVSvBlohCqc98QBmx7FaL04r_vRSoxVNaNYzty6CumlRTE0nQv1Q-PE5Ymx1-H2Um-Q6pVd7uDHCsAZw60FI5273T7TJL9mG6F1U4NLwWHOh193SSxf3QJ1JHiKMTMzcZ5FOAdoCug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ee0880e45.mp4?token=Mv7iimG4PtJDZoneD3x7rLrmWUiIS4UwVPaQyJ5-KbY56KGukXPO_lE1v7msxwH6unSPi68U99P71u1jcd0sE6usEV8P93DW7MsHNPV7IUabp9kh9hAFArUTPzkVTXLblLdyBJuHM9KunBsVpORg0FrB3vEO0zcgxChzMYIdyI00c71La15lHl6CM3x787CGaxXAdvnkelRHIVSvBlohCqc98QBmx7FaL04r_vRSoxVNaNYzty6CumlRTE0nQv1Q-PE5Ymx1-H2Um-Q6pVd7uDHCsAZw60FI5273T7TJL9mG6F1U4NLwWHOh193SSxf3QJ1JHiKMTMzcZ5FOAdoCug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فروریختن پل معلق در لحظه افتتاح اندونزی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/akhbarefori/687489" target="_blank">📅 20:41 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687488">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
آغاز مذاکرات پوتین با فرستادگان ترامپ در مسکو
🔹
کرملین از آغاز مذاکرات ولادیمیر پوتین رئیس جمهوری روسیه و فرستادگان ترامپ تروریست(کوشنر و ویتکاف) در مسکو خبر داد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/akhbarefori/687488" target="_blank">📅 20:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687487">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b76139f2e.mp4?token=LDPefTE7nNPu-gjkqtKdnVgyYYdYB95UEX81jL95ARqcoUu6VksC0Fde4U--SctDDIXg1UYrLQg9JpR18R-Ohl4V92FLK525FViZtkUZec3JTUgmfS5qUoznnUohdeesk54NSBqbS0mAR0QX3WXWMZWy8qE2Ggte9cDGRCtNMnZV08Qtqll5-SLOeaEWZwC82PuG0Zp00SNn8Wiit4qvYVc9nNjnsJsa76Cu9Sqq9DwTvF8SeI7V3Tp4M8dpeF25jrg4P9iP7eGjm-JiQ-eEneM4l84zDM7EvXwGTIRpYBCktUounzSOEO4xt62e1aSeP2nz1g-dCbwhvIv2FJBiiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b76139f2e.mp4?token=LDPefTE7nNPu-gjkqtKdnVgyYYdYB95UEX81jL95ARqcoUu6VksC0Fde4U--SctDDIXg1UYrLQg9JpR18R-Ohl4V92FLK525FViZtkUZec3JTUgmfS5qUoznnUohdeesk54NSBqbS0mAR0QX3WXWMZWy8qE2Ggte9cDGRCtNMnZV08Qtqll5-SLOeaEWZwC82PuG0Zp00SNn8Wiit4qvYVc9nNjnsJsa76Cu9Sqq9DwTvF8SeI7V3Tp4M8dpeF25jrg4P9iP7eGjm-JiQ-eEneM4l84zDM7EvXwGTIRpYBCktUounzSOEO4xt62e1aSeP2nz1g-dCbwhvIv2FJBiiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیوی نظم تردد ماشین‌ها به دلیل مسدود شدن مسیر راه که بیش‌ از ۹ میلیون بازدید خورد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/akhbarefori/687487" target="_blank">📅 20:30 · 14 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
