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
<img src="https://cdn4.telesco.pe/file/qBBaAtJ09tqvVINbISTTwahx4ofkV1RKngVrJ9Eeste1H3iMP4chdLAZpmp60wnbsh_cAzFXkqo1vmsTBLRfqzSV2R0AEDvEiUln6FZDIixY5vqyDUSKjOUD7rFO0yetAuybAkzsPNsBwHp3KjDzzqG7YaOhUVqqX25Q94bFwvvbLt4ydZnFi-h8q403kyHPdENwSH54eQxKyfmaVE06bYz2Znw5ml0z75fIbF5QveBIVvv8pfxsALAMaClIArhJDQhGaP_x5EL0G29SVnd_fol_y03EB2dKd-ConnDkgY6CDthm389Ayv1LZai59yyvDtsR721VZKG_pwKn-DaFJg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.38M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-08 12:13:41</div>
<hr>

<div class="tg-post" id="msg-685518">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
شبکه کان: آمریکا درخواست بن‌سلمان برای رهبری عملیات علیه حوثی‌ها را رد کرد
🔹
به گفته این شبکه، واشنگتن اعلام کرده از عملیات احتمالی عربستان حمایت می‌کند، اما رهبری آن را برعهده نخواهد گرفت؛ چراکه در حال حاضر حملات حوثی‌ها عمدتاً کشتی‌های مرتبط با عربستان را هدف گرفته‌اند، نه آمریکا.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/akhbarefori/685518" target="_blank">📅 12:11 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685517">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/920d463811.mp4?token=VQ780u9SrtxvaQA1AnTEh2RVUyJn7NvnWlt5Equwbg5KawwFnIeHFkh9eE5mEp1_HDgeRs4Pv1XRbvgEBX7aRhjzoKCbSmkelk-VdJzHIqcxucLcsn6aoZJKVNziqSgKD7Y-69KthG9s6CWX5ZYUexZVpbq36kgMyAh7_zwi_YawgPn4eCczzcFwqY7gCPYxSWnSfJkoqyfOR0aWKTtakP95pJJBBAN8ZqVjIWZ0WecQFkDuNUNsq_ImZrw_IMbsJc28yAM8Jz3VkUL9jIAPuCp8rPtVcHPIvoXxOurP3nrD3ahlVbYJaRtgBcumBoGXVGMySFT7eJVDF6pRcJM4bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/920d463811.mp4?token=VQ780u9SrtxvaQA1AnTEh2RVUyJn7NvnWlt5Equwbg5KawwFnIeHFkh9eE5mEp1_HDgeRs4Pv1XRbvgEBX7aRhjzoKCbSmkelk-VdJzHIqcxucLcsn6aoZJKVNziqSgKD7Y-69KthG9s6CWX5ZYUexZVpbq36kgMyAh7_zwi_YawgPn4eCczzcFwqY7gCPYxSWnSfJkoqyfOR0aWKTtakP95pJJBBAN8ZqVjIWZ0WecQFkDuNUNsq_ImZrw_IMbsJc28yAM8Jz3VkUL9jIAPuCp8rPtVcHPIvoXxOurP3nrD3ahlVbYJaRtgBcumBoGXVGMySFT7eJVDF6pRcJM4bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر پاهایتان حالت پرانتزی دارند یا زانوها به داخل یا خارج متمایل شده‌اند، این تمرین‌های خانگی می‌توانند به بهبود وضعیت پا و کاهش درد زانو کمک کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/akhbarefori/685517" target="_blank">📅 12:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685516">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
رییس پلیس راه البرز از ممنوعیت تردد وسایل نقلیه از کرج و آزادراه تهران -شمال به سمت مازندران خبرداد.
🔹
رئیس قوه قضاییه: پیام رهبر معظم انقلاب نقشه راه همه کارگزاران نظام است.
🔹
دیلی بیست: ترامپ امید خود برای حل‌ درگیری با ایران را به جای وزیر جنگ، به وزیر خزانه‌داری سپرده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/akhbarefori/685516" target="_blank">📅 11:56 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685514">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f83e55167.mp4?token=dOw5csm8KQvv4rvNBxscau0Tb26VhdSu8GfJoU45OlHwTUmvpD9WTT0W2ymU0i6d5t814TTuAveOSUhQXzAOwGj_yVePZGrsPQ8_wBd22mo1H8ajBJEpCLq3fF_7NpFgCywuPWFlMHusbRtASBibd8kaxv3Wn2U5UHiHc76PBfI2A-c7Y2hWYOPL-1H2onzifbavHtFAPlNg_EWRBtMCSFaVY4qvJtrqp8odumWjnXAl1oUUewBOBkMQwR0934HcxXaoN6NHvuayIJvYubrZTgA8oWMUKd7VkgW35A9sFz4xlvnxgaR7hXj57FD4m5Yt9SzQSQqRJiShn7tgXFzDtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f83e55167.mp4?token=dOw5csm8KQvv4rvNBxscau0Tb26VhdSu8GfJoU45OlHwTUmvpD9WTT0W2ymU0i6d5t814TTuAveOSUhQXzAOwGj_yVePZGrsPQ8_wBd22mo1H8ajBJEpCLq3fF_7NpFgCywuPWFlMHusbRtASBibd8kaxv3Wn2U5UHiHc76PBfI2A-c7Y2hWYOPL-1H2onzifbavHtFAPlNg_EWRBtMCSFaVY4qvJtrqp8odumWjnXAl1oUUewBOBkMQwR0934HcxXaoN6NHvuayIJvYubrZTgA8oWMUKd7VkgW35A9sFz4xlvnxgaR7hXj57FD4m5Yt9SzQSQqRJiShn7tgXFzDtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سوخت چگونه از مخازن زیرزمینی به داخل خودروی شما منتقل می‌شود؟
#موشکافی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/akhbarefori/685514" target="_blank">📅 11:47 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685512">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aIBJOL0elxvvu6PphSHWrdHdfpV9JEEYGmw6TAWJff5VJR-SLqqjqyx9Zaz9mHGkLNnLe4pGXOXAmqew8R1DK56cjXNa8NEkij9W1xTykpYEmK2TCW-uUuKA-DOVoL4xHkIgIkxsqrMIrGAaD0a0g6YCEu8yA_Nqbx56DogvAZRYDH0QC6U-hD_iVn2vjJfIP9xubLZ3B1PDy3TCW59KxEryYyCMBJ9ziC4R0GIC2vUtdFjKaPEBKyysITNo5SE8N37zCwx0RxEPszuZwAoOsOwYFieMCFK04DJDQR10KqpPP4JZyaUCY5oZPZWcGAib1gIIKV0p4oGrTH2bOl9K0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OiUxh1vIK461JGAMMXgQleEoPHO_KLVb0Kj2stp3w8Ql25xloEiGNBQF93SWjD_aaZkLJwzXs38nH5CN5fWcDOmhG7W322TC_CKo-PoF7_E3zRbQSRvCl47JjVwYMvI4DQZ_hV0WEcN_bP8m9pYD_lYvMaYz_i3VOWXhphzuwsgXp1vL67_YkAV9kB7hPtJxou7ZB-AErJru_8FXjwAbBGHZysQzKe3PFLvO7gcLMTssyZtAFcZYnWSA9KUpspm5xPTGkeBl8ug93dQA5otlzj-kDjc0TKG8SrLubPIK93XUlWPl2hmrbg72LAKacKIadaEvx5NGB4EmkDnKDEYj1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
آزمون تافل در ابهام، آزمون دولینگو با محدودیت روبرو شده است
🔹
دولینگو اعلام کرده افرادی که از مدرک هویتی ایرانی استفاده می‌کنند، امکان شرکت در آزمون این مجموعه را نخواهند داشت و همزمان، گزارش‌هایی درباره نبود امکان ثبت‌نام و انتخاب تاریخ آزمون تافل در تهران منتشر شده است.
🔹
این تحولات، ابهام‌ها درباره دسترسی داوطلبان ایرانی به آزمون‌های بین‌المللی زبان را افزایش داده و لغو یا توقف برگزاری تافل برای ایرانیان هنوز به‌صورت رسمی تأیید نشده است./ فرهیختگان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/akhbarefori/685512" target="_blank">📅 11:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685511">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
سود سهام عدالت در روزهای آینده واریز می‌شود
؟
🔹
رئیس هیئت مدیره اتحادیه تعاونی سهام عدالت کشور از احتمال واریز مرحله نخست سود سهام عدالت در روزهای آینده خبر داد؛ با این حال، زمان دقیق و مبلغ نهایی سود سهام عدالت ۱۴۰۵ هنوز به‌صورت رسمی و قطعی اعلام نشده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/akhbarefori/685511" target="_blank">📅 11:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685510">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a2c950187.mp4?token=M4x4ppLMqZ6nEICfmK10g4g2mEcWLtchmTBFMVK9cbWvJ6_P_EE9egYqy6bkk_HtkzJ_L9zA_vspkJ2H2XaZAxlTAMvRfaihJmRO4WLiTmlx7sapGQYYC1N4fCWXNRlHA4XQZjDzo-lIdvPAsyC1aAp-JZULb_zaQBRzzLyhC80ibWZCORpXvSLVFiUGbv3-Br_123Qp_qbjgW9GHSzAv2GaiTR5GA26kD7om7A2NH3Y9b-rxWBlKc5wHJCpW6yo9cTr5Zlh-KYrY8NccGf_2HIJyX3qv2l6DwnPJCGpcuBM1gaX2mUU5PsglCdgvXlCxK1oV9VcgKrmWAhC2gQ_RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a2c950187.mp4?token=M4x4ppLMqZ6nEICfmK10g4g2mEcWLtchmTBFMVK9cbWvJ6_P_EE9egYqy6bkk_HtkzJ_L9zA_vspkJ2H2XaZAxlTAMvRfaihJmRO4WLiTmlx7sapGQYYC1N4fCWXNRlHA4XQZjDzo-lIdvPAsyC1aAp-JZULb_zaQBRzzLyhC80ibWZCORpXvSLVFiUGbv3-Br_123Qp_qbjgW9GHSzAv2GaiTR5GA26kD7om7A2NH3Y9b-rxWBlKc5wHJCpW6yo9cTr5Zlh-KYrY8NccGf_2HIJyX3qv2l6DwnPJCGpcuBM1gaX2mUU5PsglCdgvXlCxK1oV9VcgKrmWAhC2gQ_RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فوت ناگهانی هنگام سخنرانی شبانه
🔹
نعمت‌ الهامی از چهره‌های شناخته شده منطقه مغان و کاندیدای دوازدهمین دوره انتخابات مجلس شورای اسلامی از حوزه انتخابیه پارس‌آباد، بیله‌سوار و اصلاندوز، به‌طور ناگهانی دار فانی را وداع گفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/685510" target="_blank">📅 11:33 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685509">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQjSfM2T2q5Ryylb_4slTUGcO4d8SyXyDV3FZ1shzNV4Rr4SeBWRwOo4DfFJNUzgKD4t47GS2MXo83ajX3z97PKm4-V89TWF1wzaATVsiNPuK5fk03COestziCcbK1dr_9ZfCLPKYtd7n2GWUzyVI9eIXMU4_33m2gsX_6c86TXKq8EAgbbcU0F-qHSo1jJFJa-S0qWVJ23hvgiLQAZ2Gg6ZxbNhC3sC5_Zo1p9ZSKWfdvwmvgv9RhnXxSKBN-5UhVsEe7Am4-5v6BQUgNnuPzX9PfQ8E5MBrf_8qvaMg1WBeRUHsqdQpbS1dFt50GfJq6HZCxRA2qu0Cco3L1jPXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آماده‌باش سرویس مخفی آمریکا برای حفاظت از پسر ترامپ  ادعای سی‌ان‌ان:
🔹
پس از پخش ویدئویی از تلویزیون ایران با عنوان «بارون ترامپ را کجا خواهیم کشت؟»، سرویس مخفی در حالت آماده‌باش کامل قرار گرفت.
🔹
این ویدئو حاوی ادعاهایی درباره نظارت بر دانشگاه بارون ترامپ،…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/685509" target="_blank">📅 11:29 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685508">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81ff99cf26.mp4?token=ODo1rvsNYj5bpx0uw1qhsHVPMRcTEF_aaBgqVY-fHDSkbqIfhHCVz_fGZjPuQwZCjussl3jcqkjIxuj5rxZltVFeMTZ3Wwb_S45oFleAlJ3fDvfbX4KKMx2PyvC0FcdSBmyGVLw3NyL2q1NxZBz4wHGO80psrRn_LAN7Mfj9AvQf7vBTxmuyiQFmJ1d0BuYqMQ0anppCiy9aPJiyxyu3HpVvMy3vCozf-5Ugd2P86N2XK6mFIt2H5h3qUiYCdCVmossfJCaSdEWy0fIGHwfvE9FOoreJW1a0MVHmHwzLf4qNLCxLxv3RoXyRJW0kVbbYVrR1K0hqS5ODXD9xvaKbIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81ff99cf26.mp4?token=ODo1rvsNYj5bpx0uw1qhsHVPMRcTEF_aaBgqVY-fHDSkbqIfhHCVz_fGZjPuQwZCjussl3jcqkjIxuj5rxZltVFeMTZ3Wwb_S45oFleAlJ3fDvfbX4KKMx2PyvC0FcdSBmyGVLw3NyL2q1NxZBz4wHGO80psrRn_LAN7Mfj9AvQf7vBTxmuyiQFmJ1d0BuYqMQ0anppCiy9aPJiyxyu3HpVvMy3vCozf-5Ugd2P86N2XK6mFIt2H5h3qUiYCdCVmossfJCaSdEWy0fIGHwfvE9FOoreJW1a0MVHmHwzLf4qNLCxLxv3RoXyRJW0kVbbYVrR1K0hqS5ODXD9xvaKbIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کف پا مرتبط‌ترین اندام بدن با ارگان‌های داخلی است
🔹
باید با انتخاب کفش مناسب و استاندارد، سلامتی پاها را مدنظر قرار دهیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/685508" target="_blank">📅 11:10 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685500">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sP3i7HgTj8EXQo02O6-ChX2OQBnb8ydKIe_vAlMbIztVWueFj3Sa2nTA8NdwOD-BpDq3D3HEOOO_nC0wcRkDDY3B8n28qjrhNr2SwK-hSlr4tdHGkBI1pem3zqQDvf-ubHcNKunZ8vcraT1Lj8IiBIVIqbGATDSb4kzSg6ECnQJF-RLDTaGYKbpQPJt4AZt1SAMXoWL5bp6V3f-_8z8w2XComUK83chKtuBtijX_NeNLABVzlabNGtMFYMvEuDkpq3lHdvpOA6v87MjKn0kZ3vBeoh3txuf_8W5_O0cLpKUqJqiZYY3NWr87DwQUWd32XQiEK8J2I3-RkH7oCTkEpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VqoxqKBCasOEoXaUpGyrxdKnUXwhyNkn-d54t_M8JOS99a1053LidXA0Exr-UJQecxrTnBx_-_3-4tsgZkn7ELdxZ4vJpc8bBg5BKgHJM1bc9fZXmVhRL7dL6sLAnkNGGQq2dy2gCLTvKrN-KoYjAHsl1cbBeHSnaLXxFkqdlk-lDpCCex9WmmnMzPysAvMAwn8LTZKF7hWDoU7X4yPHlSGij8kghLO-vkGRI7KOn0tcJihZefHPK4AfuBiLJ0Sh-7RCQXyAp7hwbSVuiF05bYkLhWgZIhlcyd40mDvu5QnSCWj--WNArd7IHUT-hR_CdbvKQJIyfdGOY4RqnoaZjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KK7lKLva7n-4YOHV_PWSoH3-YVXURBn-M_aUqt5rkW05cTMC-Q1ntIpGmnBf_Z63Wqv3_UyjQ648-IFEagToOCE_dsOe10Yheom0VPBeGYIUNUDp6Y8jA5QDFI7Ux3g-BL5w9KJSX7Q3OyKDzcRbk2ZqebPqO_3ECitP0mMZj8Dx97x-3tYct91WTudhpLfHBdc-TJp-ZfZrEhIgQYtwMTM64KVoKHkZNipelMMgcIU2FaoqLokNMVGL0yih7p4SsMczQ6RlBNy1GWMsf5QkNDarjPw23Qq-FBiigYN0OaaxFnbZGV1drQsUvThMPCAKqoBK8x0TNYesJGX7htjX9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YRao_-wlH6ni4P2doIFw2Pk_NPy9p0_mUVtDu7XXjeOfxNRkvwJWF6K-_i8Nj3VK0yndFyF7oflsyuw9A0-Gmxx7vwzKcb-VrWlTSfX-Eee9ePyDHErThmCOeBLBxowXKiifEwdDiBepLVZSUcGbnSkiGW5lr1q2d-tHyhXnBImLli8hdiYJHFh3PPkDdZZZCmfL6kSmK6rsE-qqDqFp78nV54Bdhflu2_cGr2rC6DaMn85ZFao0NK42flO_LhqN8cy5GdCDxmLTlnhzAr_CYGCFFYX2pgLD59tERDGf2AsMYnMO9dPjw4Zce40a7UUBpAx1rd9hLwZ-5qMbhn-Dcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rCIx_h0R-w0moo7c1gbzV_Beu26yTcklhnsydUCYZvsv0L0o8-UANccyeGoQ69dUlIIJL2UvWPwInBsLHW9-UvLNH9I0KYaD2MKww7R8SJhCB3omPVo3WDQWKShVhaf4ZDGa34YZCB_hoBlPUu44fcb2GOmsez4MP-0sa01UXxW5XcaAu1GWzWoHEADqKKgc7yf9oqL3_VOYYwmiB8zzjszz5JZSHVFZzwg5sIkVaChbklHlwq4igiPR7g76oryDsjMIhJCRY336LLOzQcVorn-M_bIg-jsBrKaLh-PXEIFyekRNoYmeV4AJ8uFUJAHFxlg-558Y9Lim_S9IN6vHtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GNAfCQLuiYb4DN535LOJQIpl5_kv0GMSmZ8Nh6rtzMieiEx23C6OvDyO_5gHRdQQVu-5_wDcRNJCcg9YNHdppWl5C0yeDx0I8rqVpEMEY7Dtak0mBFejWhdKLB4DYFVyd55ufO-NWaGR7UMWQ4E5kSj3CyOSuHEWY71wfrBS-Z8cUqVPKzSnOqhMxl1A-lLaA2kmpPtDbOKqLfH5mYjaBw5nWUWHAXecfJwfLXGP4e_THJ_KAFEzgFevxcY9nwtFLuY1-B5yGnoc_VXpY-u8rn7k_6kxLQmKlnMBk-CI1uMxAZPtGU-4Zi_EvdN_ZHfjpXNvoqBwPzqOV-7612QBIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YYsx0V_8yjgICpTv9FpijhxH9Nqt2ehHkCLZ_7tyyUeLhjz6yj5WvEY4xTAOM7O_U7HpSUylUDWWTS2i6ia6Kyo2Eg72xWsVJOfSGsm7YfhV4lAM4YKcywP3PkLiEzgNT92a7pDo-V1-3stFQ4EkdcrGcH9XzxWFyfl7oCJHc2jLNdLt5yKUG2UFqVKcuUN4rxEDOXbqeqqWGO5kqLve4KbalHWLZX1Y25xc2_tRNPBaSRRtXvjEa6Xvqns-aoKIlMjvkNREPJhpwVV34LdM6-SL8FDP9fJTWpi5xVTSr_wKhghSFxsY-Yg5mUqJSncqKf0b17hoNXz_lY14u2aLmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ETWWDUBdAQ9pRR3DISkUo_7AHGFqQ5gYpA0Av5B8EnjXIGCjEIT5BxvceCrlJ-yHnXT_s0xNeiuqyXCL7MQNkbymM05LOnbFCXD69Jm9rm3OrKIEjWpKMDPLRSXIiOkHU-bFo9cGdCCoyEPNtY2jze6stohid0Id2ByZVc3EV4YDuNlblTYOm9Yv371Cv-hzoWHOxCeiGkcuc9Bit7mXNesQaRUUxkbd0xVN6sx152mXJzTPLJQciqQ17RZcUWXBV7jpomhiQs-FhKj1R7VdgMTiXYCGxDI2p4tBTQ_tMhmmbrLX8WKSkURtFeOFjklCahJQYjlDSeqCHzMRnDw1FA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری متفاوت و تماشایی از ماه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/685500" target="_blank">📅 11:04 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685498">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lNbvoGdYc8IMgDoCtyWq9O1NwzjgA_IgxQFaC95qD5qxaRV2CWjl0o4SQxV8awcfS3HRfVruL2D3Za-EuCmiv2FDLw2yRIYrdrtAwJsv4B7Bz6UzkmVbdXkeNqzpuaRoVBYdJSYtXGG-3sNPWlUu6tQdJcASLFpdTzKJRPA-X8VP44QmHZO2p2zhUKbN4tNJCLf_XyBzOMrBeVgpZpC4SSSWW1PanuD0eTCConl8mZ0EcAjz8xMK6EZCVY86l19_rte7amAef-WSaML2HwLcnJ-ZCxNJDAnIROBU56FyKc71nOKh7Gz97y1KKysjesP-w6ZzxoFTqa6xQ7X2SRyyrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
موج انتقادها علیه ترامپ دیوانه به‌دلیل توهین به خبرنگار زن
🔹
دونالد ترامپ پس از انتقاد از گزارش مگی هابرمن، خبرنگار نیویورک‌تایمز، او را با الفاظ توهین‌آمیز مانند «زشت» و «حقه‌باز» خطاب کرد.
🔹
این اظهارات با واکنش منفی چهره‌های رسانه‌ای و دفاع نیویورک‌تایمز از صحت گزارش همراه شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/685498" target="_blank">📅 10:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685493">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f00434ac85.mp4?token=EtYLpWjW-kfGqcb_ZTyrxOd0DQlv_3ENfGUOX2jKDk2PUNYv9_8u_kZkrYIm8xnUM-kLQV4168CEwLA-8n3sAL4d35oXUSu_auSMFF_cP0pjEE98N5pXWDZ_sqtWc9mGdDfMjkTGC_zLnyWtBCvd4eRU6BXQdVT_QuIlzkCA_GtdPFyyVlYhFD_ZGlbevM8442hTtxu7UU-z5LFjgJ-cHh8O1m18ZMJeXryW_eA2XSW7MusyV7ukfnru-YHTTSUkmZBk-uKlIkOUc5_jMAwfECYQ3ABwuN6zsWvyMgzVOvDPUCtpD0hZT9yIu3lqJxwM5ZMYvJeHWKn3uiflMMzOuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f00434ac85.mp4?token=EtYLpWjW-kfGqcb_ZTyrxOd0DQlv_3ENfGUOX2jKDk2PUNYv9_8u_kZkrYIm8xnUM-kLQV4168CEwLA-8n3sAL4d35oXUSu_auSMFF_cP0pjEE98N5pXWDZ_sqtWc9mGdDfMjkTGC_zLnyWtBCvd4eRU6BXQdVT_QuIlzkCA_GtdPFyyVlYhFD_ZGlbevM8442hTtxu7UU-z5LFjgJ-cHh8O1m18ZMJeXryW_eA2XSW7MusyV7ukfnru-YHTTSUkmZBk-uKlIkOUc5_jMAwfECYQ3ABwuN6zsWvyMgzVOvDPUCtpD0hZT9yIu3lqJxwM5ZMYvJeHWKn3uiflMMzOuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وحشت در ورزشگاه کیپ‌تاون با عبور خطرناک ۲ هواپیما از بالای سر تماشاگران
🔹
پرواز نمایشی دو هواپیمای «ایرلینک» پیش از مسابقه راگبی آفریقای جنوبی و نیوزیلند، تماشاگران ورزشگاه ۵۵ هزار نفری را ترساند.
🔹
یکی از هواپیماها در ارتفاع حدود ۵۰ متری نزدیک سقف ورزشگاه پرواز کرد، اما مسئولان اعلام کردند خطری برای برخورد وجود نداشته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/685493" target="_blank">📅 10:24 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685492">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCuJ5XFD-4wtphN7pwT9RLS0XFV1T2tXLkvcWh8BTXetTQu9t1CMkHJxxheAls4rznM9aEnLJgX9XuV-5AWStyDCYcwLVfo_KiHnj4Ja1btgalpJr9F4D_bnXXYRaQzxOwqq84FNZEz1WyXO_0eBfB-hvbgorvHSi4u40bZqOEdeMkQYy3T1R6VzsOTxq5nyUUCF6KZbYoRJdwfqKjjj4p0HshXXFRscMFiwWNwlLnqzYF2z-iuotpXT6utrpKeksygRfUI121NiD7-Jd1CHSvx_CQYlTpttoLL1q1qUsOuPeCzhCIeWkUV0fqpjmE_mgr9m4Ckn25mPNDutuiCZ5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راهنمای دریافت و اهدای خون
🔹
دانستن سازگاری گروه‌های خونی در شرایط اورژانسی حیاتی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/685492" target="_blank">📅 10:18 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685491">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OSXvavIZ_eTYxHXcYt6jsutmDjnICa2s9WFyGKEuo5KYqvTMDlKmBNOCF1GkJdsGjDVTOcoKJmpQW85kz_c5yVTsZE3oBgdOz0wfBLvJHxTBsLvBR7zknwHvyxkoGiaO-MYbm6644GqV_rPdEpAP_DMCk4y6c0KUT77Sv0__iZVoYVP9Ln-eFb5VPnvecXuR0vEY6CRMfSRRaqRIIZH0NvQadTnYjZwiHG9lBAWO0mg25_tet4GHNSblUqdWoYPo_v9-kDWqrOokZAAdm40D5vvjBclcOl634KdoTSE5u0nFosy9A3UXDYCPdO2MVWi9yAuNX8yGZPe_lgQTsoU-YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یوسف پزشکیان: اگر غنی‌سازی نکنیم نمی‌میریم!
🔹
حیات ما به غنی‌سازی وابسته نیست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/685491" target="_blank">📅 10:10 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685490">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd0ac0aa2a.mp4?token=DhHNx-cZ9TE8P5V8f5VhcUTfytjo89EoyFipHaKUEgTgGYMqMzMpQZq7IiJqosfLjJ_88h8x6GCpNKOX9uMn1hQ7r-uuRaIpWvSn65Dkav68OZKerdmNA6rKhcwY4e9uZLe2t9leAVueuaCnac4t9ojFnO3pu2o0bIpzrB8tUlBWCPjZUTXFMJ5T9dvADVzDvWtprPDQL4nCLDZalcHVDVsA_THuZaImw6LxOqZo8wVxa6Wg2Ct8frDVcm6sneW_1Rg2uHUlxy5kDNgd3G3gC2CTmpyxdWDFgVLVFdqJuKfi6FTVop_xkb1TpFiVupIKYyKyPY2U-nsdIfiwqmyihA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd0ac0aa2a.mp4?token=DhHNx-cZ9TE8P5V8f5VhcUTfytjo89EoyFipHaKUEgTgGYMqMzMpQZq7IiJqosfLjJ_88h8x6GCpNKOX9uMn1hQ7r-uuRaIpWvSn65Dkav68OZKerdmNA6rKhcwY4e9uZLe2t9leAVueuaCnac4t9ojFnO3pu2o0bIpzrB8tUlBWCPjZUTXFMJ5T9dvADVzDvWtprPDQL4nCLDZalcHVDVsA_THuZaImw6LxOqZo8wVxa6Wg2Ct8frDVcm6sneW_1Rg2uHUlxy5kDNgd3G3gC2CTmpyxdWDFgVLVFdqJuKfi6FTVop_xkb1TpFiVupIKYyKyPY2U-nsdIfiwqmyihA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویری هوایی از قله کلیمانجارو؛ بلندمرتبه ترین قله آفریقا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/685490" target="_blank">📅 10:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685489">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
دستگیری عامل ارتباطی شبکه‌های معاند در تهران
پلیس تهران:
🔹
فردی که با برخی رسانه‌های ضدایرانی در ارتباط بوده و اطلاعات و اخبار جهت‌دار در اختیار آنها قرار می‌داده، پس از تحقیقات فنی و اطلاعاتی شناسایی و دستگیر شد.
🔹
متهم در انتشار اخبار خلاف واقع و ایجاد فضای نگرانی در جامعه نقش داشته است.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/685489" target="_blank">📅 10:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685488">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
یونان از رژيم اسرائیل سامانه پدافند هوایی می‌خرد.
🔹
افزایش آمار قربانیان سیل در نپال به ۷۳۴ کشته و ۲۵۰۰ مفقود
🔹
وزیر جنگ پیشین رژیم صهیونیستی: اسرائیل باید زرادخانه موشک‌های بالستیک خود را گسترش دهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/685488" target="_blank">📅 09:49 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685487">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9394581bae.mp4?token=RG71K0rXz6c5FN6xVEBu4zNKhsc4A3AfrnvtZ4tepfaIrHe-TD1U08X3id7rkkhW0cNO50ZBWKzHIarJuowjbSJ18qOm5zd4wHEYQJdeWrivlM4K0CmVCirlD6fST0_E_QlvE9kwVdUpGlabBS5dIxGYoOYEN6uhYNfvpQ56cfEnuOjcMK7tMueefHfg08VM1KpAxolwfbvioNOUo1XSPnRUOgZWPFFprC_0nSeGYNqG8eax3gaGdSFeOOuaUC_IreMVvxt4l3DY9JOjVkOjXQNXJUoe40nEJwKYNHOWr0poUEPmoVLSDcWh_GaK-H3pg1VKlReFz0FwHjwc-uR8kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9394581bae.mp4?token=RG71K0rXz6c5FN6xVEBu4zNKhsc4A3AfrnvtZ4tepfaIrHe-TD1U08X3id7rkkhW0cNO50ZBWKzHIarJuowjbSJ18qOm5zd4wHEYQJdeWrivlM4K0CmVCirlD6fST0_E_QlvE9kwVdUpGlabBS5dIxGYoOYEN6uhYNfvpQ56cfEnuOjcMK7tMueefHfg08VM1KpAxolwfbvioNOUo1XSPnRUOgZWPFFprC_0nSeGYNqG8eax3gaGdSFeOOuaUC_IreMVvxt4l3DY9JOjVkOjXQNXJUoe40nEJwKYNHOWr0poUEPmoVLSDcWh_GaK-H3pg1VKlReFz0FwHjwc-uR8kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ورود سامانه بارشی به غرب و شمال غرب کشور و صدور هشدار نارنجی سازمان هواشناسی برای برخی نقاط
🔹
هوا در نیمه دوم هفته خنک می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/685487" target="_blank">📅 09:40 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685486">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50c84f5d91.mp4?token=XNcOkz_cNdSw3pFvLUYHpLtU7jIHnHjgLd_EBLXlHOwuEUNtmCo8d4nR7yOmMieJ1wVSB7TyW64EuXYktpvwXm0X8zPgR7cqU3Bfvj16WQ_EEI691s9NHbVxI7HY24_WdoZwaPGiMufRJcwf5QVN-w-hjdh8NzqI7kjzaVoilDSJXf141YvcykX989l_xvHgtdtZWT1ciyeRQHHDGTnH_SS95Ll6KqRs7wIh9S1umlWfTp6Mjagnu7c-D0sAg54D5f-G1prw30Ix8DgHLKf6W8td8_Wgp9O79LTGSuJm6jR1l0VZ1seL3Rk1qkzjllZUDuZLCJoes4A8JYni3YtZVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50c84f5d91.mp4?token=XNcOkz_cNdSw3pFvLUYHpLtU7jIHnHjgLd_EBLXlHOwuEUNtmCo8d4nR7yOmMieJ1wVSB7TyW64EuXYktpvwXm0X8zPgR7cqU3Bfvj16WQ_EEI691s9NHbVxI7HY24_WdoZwaPGiMufRJcwf5QVN-w-hjdh8NzqI7kjzaVoilDSJXf141YvcykX989l_xvHgtdtZWT1ciyeRQHHDGTnH_SS95Ll6KqRs7wIh9S1umlWfTp6Mjagnu7c-D0sAg54D5f-G1prw30Ix8DgHLKf6W8td8_Wgp9O79LTGSuJm6jR1l0VZ1seL3Rk1qkzjllZUDuZLCJoes4A8JYni3YtZVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای
کارلسن: گزینه استفاده از سلاح هسته‌ای تاکتیکی علیه ایران در پنتاگون مطرح شده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/685486" target="_blank">📅 09:33 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685485">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49cb916dca.mp4?token=YO2E2NVN-ACJe-5162wQ9VLXCgP_pwop5hFYjkMz_c8eBFqOcsLuIGyw50kjP3g80PpI1GRHo6W5wrTI2p5FV7Tz0VzCl4aRHuUXxbNjCluZK7C3Kybd-crAFBSiWHfBdYu8PNoMfT_hZ8NdZvEHzApgEvUKtvZPkbB4B42Mt_-ppxWijpSGxA0BjmNpUXQPjU59soAGIuTM0MHETvP-dq9pidG8yfZ3nibDnr-jvFUdR8MesTcm01Z9cg0YLkqA-uzgfZzTxb7xFAQu51o17i5BJ-4oEMzM0HsNnXC4GOObfI1pQIIqI-Y9-Q_nXe7Wvx1aEp6rX_1OUv5xFOfbxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49cb916dca.mp4?token=YO2E2NVN-ACJe-5162wQ9VLXCgP_pwop5hFYjkMz_c8eBFqOcsLuIGyw50kjP3g80PpI1GRHo6W5wrTI2p5FV7Tz0VzCl4aRHuUXxbNjCluZK7C3Kybd-crAFBSiWHfBdYu8PNoMfT_hZ8NdZvEHzApgEvUKtvZPkbB4B42Mt_-ppxWijpSGxA0BjmNpUXQPjU59soAGIuTM0MHETvP-dq9pidG8yfZ3nibDnr-jvFUdR8MesTcm01Z9cg0YLkqA-uzgfZzTxb7xFAQu51o17i5BJ-4oEMzM0HsNnXC4GOObfI1pQIIqI-Y9-Q_nXe7Wvx1aEp6rX_1OUv5xFOfbxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کدوم امگا ۳ برای تو بهتره؟
🔹
منع مصرف امگا ۳: اگر داروی ضدانعقاد خون مصرف می‌کنید یا مبتلا به هموفیلی هستید، این مکمل مناسب شما نیست و یا حتما با پزشک مشورت کنید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/685485" target="_blank">📅 09:23 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685484">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t_p9Eb8d-ebtBVEWflISiePe0WmzkSqltO-l_UibfbF2a3dvxCAB7xRlygGgkw5H5AfSxKoV9CMethMnYgo0_-YTIA7N5YHLAJmsUZmXIRhPadLAS4kj0Wf_QgCNIQDPgZPw_K0tyg5Ygryi4txomFyHNdnU1GEXmHCkbxUNpQbhdP1MjPL_Qv-zyLQgVYK6bq_aHoA9BXRfGVXSZwMz2ep1fQXXUOjiGr_O5DZana1acCs6EvjvCMxg6vq1kI0n-uzdvixGIBdZJAYi2DGFMuh4VBpIb9cVfqqJNnHOrB34AkuUjhcgzIRK6yRqqUAEa2GQZtpbO8cR2AW2qRTXKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رهبر انقلاب: حاکمان آمریکا و رژیم صهیونی، دشمن همۀ امت اسلامی و حتی حکام این کشورها هستند؛ بکار بردن تعابیر زشت آن‌ها نسبت به بعضی سران کشورهای منطقه در حافظه‌ها موجود است
🔹
حاکمان جنایتکار امریکا و نظام جعلی صهیونی دشمنان قسم خورده این اتّحاد و دوستی هستند.…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/685484" target="_blank">📅 09:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685483">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
اتّحاد، دفاع متقابل در مقابل کفر و همکاری مسلمانان؛ سه گام برای وصول به تمدّن نوین اسلامی
🔹
درس مهمّ اتّحاد و عدم تنازع، درس اوّل مکتب اسلام در مورد نوع مواجهه با دشمن و دوست است. امّا درس دوّم آن، دفاع از یکدیگر در مقابل کفر و درس سوّم، انواع همکاریها و…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/685483" target="_blank">📅 09:17 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685482">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
رهبر انقلاب: اگر مسلمانان متحد بودند، فلسطین این‌گونه بی‌پناه می‌ماند؟/ حکّام کشورهای منطقه دشمن واقعی را بشناسند و  با آن مقابله کنند/ اکنون وقت آن است که مسلمانان به فکر فرو روند و حوادث را دقیق‌تر بنگرند
🔹
آیا اگر مسلمین یدِ واحده‌ای می‌بودند که مشت خود…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/685482" target="_blank">📅 09:13 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685481">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
مقصود از وحدت، محور قرار گرفتن نقاط مشترک میان مسلمانان است/ مسلمین باید «اَشِّداءُ عَلی الکُفّار، رُحَماءُ بَینَهُم» را محور فکر و بیان و عمل خود قرار دهند
🔹
مقصود از وحدت آن است که در سطح عمومیِ جوامع اسلامی، نقاط مشترک بین همگان، محور و اصل قرار گیرد.…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/685481" target="_blank">📅 09:05 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685480">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
رهبر انقلاب: هر کاری که به تفرقه بین مسلمانان بینجامد مقصود دشمن را سامان داده
🔹
اختلافات عقیدتی و مذهبی گرچه یک وجه مهم از مقصود دشمن اسلام بشمار میرود و او به استفاده از آن بسیار دل بسته است، ولی به آن بسنده نخواهد کرد و تلاش دارد تا انواع تفاوتهای نژادی،…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/685480" target="_blank">📅 09:04 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685479">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
رهبر انقلاب: بدخواهان در کمین وحدت مسلمین هستند
🔹
زمان برگزاری اوّلین هفته‌ی وحدت به اسفند ۱۳۵۶ هجری شمسی و دوران مبارزه با دستگاه ستم پهلوی برمی‌گردد؛ آنگاه که رهبر عظیم‌الشّأن شهید اعلی‌‌الله مقامه‌الشّریف در دوران تبعید خود در ایرانشهر این فکر را مطرح…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/685479" target="_blank">📅 09:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685478">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
با میلاد پیامبر(ص)، چشم‌انداز سعادت بشر درخشش دیگری یافت
🔹
ایّام ولادت وجود مبارک نیّر اعظم، اشرف خلائق، سراج منیر، برگزیده‌ی خداوند، شهر علم، حضرت رحمةٌ‌للعالمین، رسول مکرّم اسلام صلّی‌‌الله علیه وآله وسلّم و فرزند پاک و پاک‌نهادش، حجّت بالغه‌ی الهیّه،…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/685478" target="_blank">📅 09:02 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685477">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R7j1PscO3NeyiS9P85YO3duBT80vhMWmKTLkWjrkHiH5sJEPJaP4LeWQ8gItsxyH_euna462M5CE_9AaPH9jik8uj0l18b-wMon53GdLaCWsiJCpe38VVZzwYKFa5FVCxONSOtqOxFSzKm7LoyDcSOJY2N0Nmc2PEWWI6kDmCMxay0B3Z3NI8tC4gbKaQ41Jki30CrA58BMJnb5HbIR7KfJ2tF0Cqk3_DsLGuWm4BBiKtVKtVVR_LfxfS_4S8OFoMnAtKHVzrYCjOvIDE471zqlfm3Cbatu-YLL1dVH3VPDQYakmW38tu0V4GeLAM3WeozGlsKL9tcUYLf4TZXfbPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با میلاد پیامبر(ص)، چشم‌انداز سعادت بشر درخشش دیگری یافت
🔹
ایّام ولادت وجود مبارک نیّر اعظم، اشرف خلائق، سراج منیر، برگزیده‌ی خداوند، شهر علم، حضرت رحمةٌ‌للعالمین، رسول مکرّم اسلام صلّی‌‌الله علیه وآله وسلّم و فرزند پاک و پاک‌نهادش، حجّت بالغه‌ی الهیّه، حضرت امام جعفر صادق صلوات‌الله وسلامه‌علیه را به ملّت شریف ایران و امّت بزرگ اسلام تبریک میگویم.
🔹
از آن وقتی‌که خورشید وجود حضرت ختمی‌مرتبت در مکّه‌ی مکرّمه طلوع نمود، چشم‌انداز سعادت بشر که رَهین کمال بندگی و اطاعت از حضرت حق جلّ و علا است، درخشش دیگری یافت؛ ارواح انبیاء و ملائکه‌ی الهی و قدسیان، غرق در سرور گشته و شیاطین انس و جن، انگشت خشم و حسرت و غم گَزیدند.
🔹
زیرا برترین خلق خداوند در همه‌ی‌ عوالم بی‌شمار خلقت، پا به عرصه‌ی خاکی می‌گذاشت و به‌زودی با خلعت نبوّت و خاتمیّت و با در دست داشتن قرآن عظیم و مأموریت هدایت همه‌جانبه‌ی انسان میرفت تا حرکت کاروان عظیم بشریّت را به‌سوی عبودیّت و تکامل الی‌ الله رقم زند.
🔹
بخشی از پیام رهبر انقلاب اسلامی به مناسبت هفته وحدت | ۸/شهریور/۱۴۰۵
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/685477" target="_blank">📅 09:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685476">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FEbtm2NLT5xRbCjVZiF5IVwnR7WRPd8WTcMEYhfYyqrhZeZSqq7GygjRVLWVPPZFFbcaZVCul3zdWI7fRbnMDYys8P6P3BWd4H_RyQHfU8r7MatnBduFdwegGMM1HA9JP5-Nvwm9vnlwb5eRyhQn6KLPxkD8-lNXtRAhx5PBPvbbzJre1ht3EQ7kXRmQrzqaQ15_BGbZXmuWNyqAwaaMcNnamefZcPV9se4H1NxoDoUiPUOG_v4kECvgQQkSOCCfnVjEnBdPJGFpN2EuH5aS-J-b3bGiIui9smHyW0q7xSal6PD-DUv8ZXIxZQBc-YyHewtRzFnmt1LoOSCDQJle5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تلسکوپ فضایی رومن ناسا امروز پرتاب می‌شود
ناسا:
🔹
تلسکوپ فضایی نانسی گریس رومن امروز، از فلوریدا به فضا پرتاب خواهد شد.
🔹
رومن قرار است میلیاردها جرم کیهانی را بررسی کند تا دانشمندان درباره شکل‌گیری سیارات، ستاره‌ها و کهکشان‌ها و همچنین انرژی تاریک و سیارات فراخورشیدی اطلاعات بیشتری به دست آورند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/685476" target="_blank">📅 08:56 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685475">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28f18eaa49.mp4?token=LvzMsdkA-k7qrk644Id158dsibtmnqQVB_XpLVcw_sLcO_x2kmzT_usbed-fdyW6sn4CKpDuGPjDtig6VLfTfDjdv39XJcr2f_VIYnqdnKeR0fd2aNEahunkRnGUA1XY9U93btVxFCQ7QGLxTlvgMXMZZD2LregAnMti06LTKglyqRiY9KyM4g_cKvAvd-gY3RiDi7pU3-KCUjOrPseXCAERgZUKUN9RBq8UhIp6PONb05snxjYJQOTFxVbrI8PQhrWLVjQr0cEQM8z6DPMo7YUFJ5is891iGBW7s5DhQPVlysPUpzEgeNPTOZqqi4czQLwyZC0IaKxxvydUK4ffPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28f18eaa49.mp4?token=LvzMsdkA-k7qrk644Id158dsibtmnqQVB_XpLVcw_sLcO_x2kmzT_usbed-fdyW6sn4CKpDuGPjDtig6VLfTfDjdv39XJcr2f_VIYnqdnKeR0fd2aNEahunkRnGUA1XY9U93btVxFCQ7QGLxTlvgMXMZZD2LregAnMti06LTKglyqRiY9KyM4g_cKvAvd-gY3RiDi7pU3-KCUjOrPseXCAERgZUKUN9RBq8UhIp6PONb05snxjYJQOTFxVbrI8PQhrWLVjQr0cEQM8z6DPMo7YUFJ5is891iGBW7s5DhQPVlysPUpzEgeNPTOZqqi4czQLwyZC0IaKxxvydUK4ffPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چاپلوسی عجیب نماینده آمریکا در سازمان ملل برای ترامپ
🔹
نماینده آمریکا در سازمان ملل، ترامپ رئیس دولت تروریستی ایالات متحده را «رئیس‌جمهور صلح» توصیف کرد؛ تعبیری که با توجه به رویکرد نظامی و غارتگرانه دولت او، یک چاپلوسی عجیب تعبیر شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/685475" target="_blank">📅 08:47 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685474">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c98edaa0b.mp4?token=PH1BrppnkhirKWjcVeSwkfNwwhD4AlWKEovKgMfefXn7OEI9CUL1tTj_v-McHCErCI0Us84bEvyRAIO3lrPqENP_ukrxtrfxbvx1a1zjtuOQjA9lcQ0M3uMGZJhEsV9Ks6oDRAW2c12UnSSGD3ku9s4qoY2t0EiU2Z5mex54c5Ux_tH7oCFQxlcNtMOLFy62Ee3898YH5GYXRzisOStjWjITypgLBU9M_mwSmkZGdjOvMkTp0L-REI4IsB9xUiGunXwXdGvWDUWi4VXCYYgX8JnANxcDRpcmgU_PjQsYyYu5IyGnhRo6nUzgxpd1V2nVTbOij4ExPhvWF38Cr2fBzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c98edaa0b.mp4?token=PH1BrppnkhirKWjcVeSwkfNwwhD4AlWKEovKgMfefXn7OEI9CUL1tTj_v-McHCErCI0Us84bEvyRAIO3lrPqENP_ukrxtrfxbvx1a1zjtuOQjA9lcQ0M3uMGZJhEsV9Ks6oDRAW2c12UnSSGD3ku9s4qoY2t0EiU2Z5mex54c5Ux_tH7oCFQxlcNtMOLFy62Ee3898YH5GYXRzisOStjWjITypgLBU9M_mwSmkZGdjOvMkTp0L-REI4IsB9xUiGunXwXdGvWDUWi4VXCYYgX8JnANxcDRpcmgU_PjQsYyYu5IyGnhRo6nUzgxpd1V2nVTbOij4ExPhvWF38Cr2fBzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدویی از روش جالب روشن کردن مشعل گاز با فلر
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/685474" target="_blank">📅 08:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685473">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_lHLDrBWW4ucpRXMdw4lWDLLq7VUeWBz8_jPapDCVhgWWmtacYxyKaMxbCovimm6hf9SUQIdcbfQBr7Ui9mekBHLfaZxUpvbcJwnDgqyxB5Zq0Iassyy3eSAYaICvCz9h21zye9u849E4cCtTtGtO69yZlO9nW0Y8-_HnLHbrnDV_yJg-pterXjQcktx9-sO_Xmu_yNEl4Fx_1JPdtqXdU6mcUKTPA_CBLpbsGIeVdDFHw9q_r4xOPmDtuiOGbUcB7z5SwriRbBUpmU126hRrGD3XCQ_q_F-2FFKDOosoHNPQhHtFCgba6d8w4ITiqLdKDhcMrVozTeJR88yUePRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دستِ رد واشنگتن به سعودی‌ها برای حمله به یمن
🔹
شبکه اسرائیلی «کان» مدعی شد که عربستان تلاش کرد آمریکا را به اقدام نظامی علیه یمن متقاعد کند، اما واشنگتن درخواست ریاض را رد کرد.
🔹
طبق این گزارش‌ها، عربستان اصرار زیادی به همراهی آمریکا داشت اما واشنگتن «لحظه آخر» پشیمان شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/685473" target="_blank">📅 08:18 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685472">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwYDtJGo5fwwpkUVwOdZA9k3MJkfqgSpCG8cv-3wWMEsOG4fQ1AA56Jxf9GKLy5Ri3p_RnQlk65wZoLPyVDFZdjBUWBIKtcmiRWlOIwzaAi0d_pF-x8z9SopVmsFECxBUbjwn0hu7TLSqS8pGCzxa4rlVZqaR6wDI_vLcXu_EXpr2j7UhZc05-M1nQRDo0G1NOB4rLuDmmb7hfDYEDTmiCdUP_yjTkT_FnaUHAltBcWcOU4xujksD2aFZcZ9yd6OuCTknj9v2aYPJUVu_xU6tJ55qmB4_tmVCmr-JPgjknC_olaLirDTl0h2KWSY-iW0DPFimHR5Hgi2mEe6YwvDlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
ماه در آسمان آلاباما سرخ شد؛ تصویری تماشایی از ماه‌گرفتگی
🔹
این پدیده که به «ماه خونین» معروف است، زمانی رخ می‌دهد که زمین بین خورشید و ماه قرار می‌گیرد و نور خورشید پس از عبور از جو زمین، با رنگی مایل به قرمز به سطح ماه می‌رسد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/685472" target="_blank">📅 08:16 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685471">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وال استریت ژورنال: آمریکا به دلیل کمبود کود با بحران غذایی مواجه خواهد شد.
🔹
اوکراین شب گذشته با یک حمله پهپادی، پالایشگاه نفت کریشی روسیه را به آتش کشید.
🔹
واکنش ترکیه به اسرائیل: اتهامات تل‌آویو تلاشی برای توجیه نسل‌کشی در غزه است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/685471" target="_blank">📅 08:10 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685470">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JQiHSRNK-n9PyyO2gJzSDOoGywdm4HrQKOz5dJLxtYS4KwhE6gqFyfcxb_jp-rN0tsPCHLSk74C4y3IPBmIEnLg2cZdX5py65tx7Wxknroed96cTbWfeZHXUjiYnxsm6UdL62KpdN4JOBoS8XMyTGPwE5XZVc0VA4-9iEgqwEZDjY2mOxCKdpG7Snb52JWoJFnyj97MHItUPera7o50g1EG-H6HX9IlxWeTRnVI3KlL5a50WeE3xZdJ9Ll8M9y4RKHQIvU1XjhPgxthRFmGZYvEI_eK5YFEA4z0pS4bu7tuKPuIy2cPGPUTvZGo6tzL3S4E6DHSuOHg7qlbMH6ZODg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وحشت پسر نتانیاهو از احتمال ترور  شبکه ۱۵ تلویزیون رژیم صهیونیستی:
🔹
یائیر نتانیاهو (پسر بنیامین نتانیاهو) در طول دو سال اقامت خود در میامی آمریکا، از ترس جانش، احتیاط شدیدی به خرج داد و در چندین نوبت از بیرون رفتن به بالکن آپارتمان خود خودداری کرده است،…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/685470" target="_blank">📅 08:05 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685469">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sIEG0dTGfxVYglSV_aNix3s2HVRfQVO6iCKCSjuqxbdL8p2aIahU4Q96CQprquB-vQSlyZBlUdS62O7dbP82aqWuqjWWCvsvgbSpliaD7d7qDUpVtlQiWqGqqquC8K3tbjpdKleAYx6t3C78DcTrF9Mkxs-m7jEYV7MHxf0-X4uBIR2g1s9OVaGg5LPcvVfqcNnHmGZE1qqp2c8jkpYToU1f39Y-BSIMERmi7eOJ9jAaiN3fVkdP0L33ymhRsIcvThjHd728x0f1Mmepr5iE2UbVSo-5rqPOqaN6T9GccYEqyIvJfErqnSzZx8C7n9Gt_FmLMLU7u_ZClWquO1yOmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز یک‌شنبه
۸ شهریور ماه
۱۷ ربیع‌الأول ۱۴۴۸
۳۰ آگوست ۲۰۲۶
یکشنبه‌ها
#حدیث_کسا
بخوانیم
⬅️
متن و صوت حدیث کسا
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/685469" target="_blank">📅 08:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685468">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AMGzT5W-q96zFW6mGFKGPXn3QqFKHFiahOkY6Nw0pVZCA-3DfWSWwRrwUSlNDzBRfh7Msv5nL4ylR--DHZK3dEEfs6Lt3sDvFP1jg6Oo3SFqxJE-O8NDTSkkS0t34Oad74v8SkY9RdBadvWjgV3se9yGBo1oh9LCbfeAXSr5pl6DjyWD32NsUxA4a90e4Gv1Qq8eNz5-VPdBYYWkaFavi8m4eWQxOAbXt_28U9CaEMsWY626zW3bZKCzGeBPtua2oMXWxIx7CwUv9r9lI4rQp3tvtRNRg5lDuXyFBol3NVFdvZ7Le2hbcnmcRabMmWeY41FVeoTuya8gX-PXHY3-mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
تخفیف ویژه چمدان خارجی و ایرانی
🔥
چمدون PP نشکن و عمری
😍
خرید مستقیم از واردکننده
✅
بدون واسطه | قیمت عمده حتی تکی
✔️
PP پلی‌پروپیلن (۱۰۰٪ نشکن)
✔️
قفل TSA
🔒
✔️
زیپ و چرخ دوبل 360° سایلنت
✔️
محفظه لباس کثیف
🧳
چمدان پارچه‌ای جنس خارجی هم موجوده
⏰
موجودی محدود | تخفیف کوتاه‌مدت
📞
09153835409
📱
تلگرام:
@Ali_aam06
🔗
https://t.me/maross_mashad
📣
تولیدی چمدان ماروسی</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/685468" target="_blank">📅 02:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685467">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sOmpLRsiBj23N9ilLUo1ffrmEIK7viPHlyKR-J_zP1qDdphAAq2QC5kzLSF5iglkAAFLGt3kXMRwjBexVKN4aWY9_fPiIyNvfS8Kk71SqonRVGoHkCg9cnBIutJ3wOeulkyQ_iipFSzCx7lbirYCwIitSAnOS5mpAUOuc1SgNCxvaLk3iKIQexllqOWESVIZanaWiLGE4y3Pi1SWs5cvaorvk2wz1Zmxtu7dEckhuTTZ4Qtxx2hIlZe8NvnTl9cWxKawC9WA5phm_0-nKMM0aoKj__rlFYpQyr4aulchNlUtFtSc8rau_eslsz8fnm3LMS-4HNioHjA-ZlYu5xIWPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
گوشی نوکیا 105 | دکمه‌ای، ساده و بادوام
اگر دنبال یه گوشی دوم، سبک و جمع‌وجور هستی، نوکیا 105 انتخاب خوبیه
👌
🔹
دو سیم‌کارت
🔹
منوی فارسی
🔹
باتری ۸۰۰ میلی‌آمپری قابل تعویض
🔹
چراغ‌قوه و رادیو FM
🔹
صفحه‌نمایش رنگی ۱.۷۷ اینچی
🔹
ریجستر شده و آماده استفاده
❌
قیمت قبل: ۲,۴۹۸,۰۰۰ تومان
🔴
قیمت ویژه: ۱,۹۹۸,۰۰۰ تومان
🚚
پرداخت درب منزل
✅
ضمانت تعویض ۳ روزه کالا
خرید از سایت
👇
https://memarket24.ir/product/brief/63518/180124/
✨
تخفیف آخر ماه؛ فرصت آخر برای خرید با قیمت بهتر!
https://l.memarket.me/lp/65/180124</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/685467" target="_blank">📅 02:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685466">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c48d8f745f.mp4?token=oT7fak-0fsmTarqx8gd7SLYlqgfRSrFYsoIOqw9lNqmb4CLe8KPrUZ4q1zV8CHDV-CxhbAe20YFQYKzG-6GdloXdZMNUZbBlWECNiMu-8lshws4jcjHzAjKn45VgoDQTyQCv4oNV3qkSCQtNa_Sq3tiYtm-hUNjYHp6Eh0CIGz259q5fX_TDAznsHLHEF-qV2tnInvxeHgciP2MNPu90sESEXD7PgiYLkCpJazg60jXmoRmVs1j9paimuBZkNAQzQ1ihiAh8vAGcQcdkBn5bF9aZx-mMzt2jVjjGF9iHG6XMghxlFJcHGvuJWeIr6Qo0l9EH8IYyHApA30v-UirMuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c48d8f745f.mp4?token=oT7fak-0fsmTarqx8gd7SLYlqgfRSrFYsoIOqw9lNqmb4CLe8KPrUZ4q1zV8CHDV-CxhbAe20YFQYKzG-6GdloXdZMNUZbBlWECNiMu-8lshws4jcjHzAjKn45VgoDQTyQCv4oNV3qkSCQtNa_Sq3tiYtm-hUNjYHp6Eh0CIGz259q5fX_TDAznsHLHEF-qV2tnInvxeHgciP2MNPu90sESEXD7PgiYLkCpJazg60jXmoRmVs1j9paimuBZkNAQzQ1ihiAh8vAGcQcdkBn5bF9aZx-mMzt2jVjjGF9iHG6XMghxlFJcHGvuJWeIr6Qo0l9EH8IYyHApA30v-UirMuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس‌جمهور فنلاند: روسیه قصد حمله به ناتو را ندارد
🔹
الکساندر استوب، رئیس‌جمهور فنلاند؛ در حال حاضر نشانه‌ای از وقوع جنگ نمی‌بیند و معتقد نیست روسیه قصد حمله به ناتو، قدرتمندترین ائتلاف نظامی جهان، را داشته باشد. او دلیل این ارزیابی را اطلاعات امنیتی و قدرت بازدارندگی ناتو، شامل نیروهای متعارف، موشک‌ها و تسلیحات هسته‌ای، عنوان کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/685466" target="_blank">📅 01:51 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685463">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
فنلاند به دور از توجه رسانه‌ها یک یادداشت تفاهم‌ ۱۰ ساله با اسرائیل امضا کرده که شامل تحقیق، توسعه تجهیزات نظامی می‌شود و روابط نظامی دو کشور را گسترش می‌دهد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/685463" target="_blank">📅 01:29 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685462">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b634dd076e.mp4?token=b6bgJoAEyqPlWekne7ZlqsQzHFCjjZLrufS1_eDYpP5DFgsyU8R89W9zbGMFPw3AEMJFbMSoRNVfyDIVwQOdjQ-Q54wIW5s7O5umX-2qlvIy5QDhoGXPSN55BVHWgwynpejpONt7CwU8THlPOItsNxM0tDgk8EA8E9ZkjqAgahuR_JShEsnNFZcUmK2GFcLxFtkbczllgdAUkU8gcREvXxhD7wKqIsubSHbt9lUzPuFwohS1tr-XlOMm-pEn84fY7k_51XPs67YoMhrYjTWkbS7j86Y8gIUsYgLu4AzDpZVeYfiHaTiGXFI9tczQJv1l5aN1yXfPngWdPa57l4g1Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b634dd076e.mp4?token=b6bgJoAEyqPlWekne7ZlqsQzHFCjjZLrufS1_eDYpP5DFgsyU8R89W9zbGMFPw3AEMJFbMSoRNVfyDIVwQOdjQ-Q54wIW5s7O5umX-2qlvIy5QDhoGXPSN55BVHWgwynpejpONt7CwU8THlPOItsNxM0tDgk8EA8E9ZkjqAgahuR_JShEsnNFZcUmK2GFcLxFtkbczllgdAUkU8gcREvXxhD7wKqIsubSHbt9lUzPuFwohS1tr-XlOMm-pEn84fY7k_51XPs67YoMhrYjTWkbS7j86Y8gIUsYgLu4AzDpZVeYfiHaTiGXFI9tczQJv1l5aN1yXfPngWdPa57l4g1Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نماینده سابق کنگره آمریکا: ترامپ باید از والدین دانش آموزان مدرسه میناب عذرخواهی کند
🔹
ترامپ باید از من عذر بخواهد.
🔹
باید از آن خبرنگاری عذر بخواهد که صدایش کرد «خوک».
🔹
باید از آمریکا عذر بخواهد که وعده‌های انتخاباتی‌اش را زیر پا گذاشت.
🔹
باید از پدر و مادرهایی عذر بخواهد که روی مدرسه‌شان در ایران بمب ریخت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/685462" target="_blank">📅 01:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685461">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
امارات گوش به حرف آمریکا؛ بازرسی از بانک مصری کلید خورد
🔹
بانک مرکزی امارات فقط ۹ ساعت پس از اقدام آمریکا در تحریم یک بانک مصری، از آغاز بازرسی از فعالیت شعبه بانک مصر در این کشور خبر داد.
🔹
وزارت خزانه‌داری آمریکا پیشتر مدعی شده شعبه امارات بانک مصر از ژانویه ۲۰۲۴ تا ژوئن ۲۰۲۶ حدود ۱.۸ میلیارد دلار تراکنش برای ۱۰۳ شرکت پردازش کرده که احتمال ارتباط آن‌ها با شبکه‌های مالی ایران وجود دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/685461" target="_blank">📅 01:15 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685456">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54cb7f1f24.mp4?token=pIo2M1dRtYtYKG6VLge_l9f1p4030CX6YyWeAdlA3uHHfv9oqYnuO3WMJEJ5BSN-ddlxlG7N2GmD3ufDy4eKHop5MqgS5YnGrjaeMgmzuPdYvD8xzphR48SWTxrq35gS2hmacf6hgKcNwseS2CW2WeeesAHhtccGSyNKP_yONQ7hNcn3Sgwy6bxnddVF2uIPx-E9Ozla0rHOYGS1NtxIo8SZoVyUply2uwD0AMrqsnYq0D_dExjrZNERltA9UAEDXZsaGtRy3hzbZhxvzzNXt6mhiUhK6CrYuk43IomBeZfdVvJ4TQxvf72AdQFQMI6ZabRgrs878KNfPudOwruuIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54cb7f1f24.mp4?token=pIo2M1dRtYtYKG6VLge_l9f1p4030CX6YyWeAdlA3uHHfv9oqYnuO3WMJEJ5BSN-ddlxlG7N2GmD3ufDy4eKHop5MqgS5YnGrjaeMgmzuPdYvD8xzphR48SWTxrq35gS2hmacf6hgKcNwseS2CW2WeeesAHhtccGSyNKP_yONQ7hNcn3Sgwy6bxnddVF2uIPx-E9Ozla0rHOYGS1NtxIo8SZoVyUply2uwD0AMrqsnYq0D_dExjrZNERltA9UAEDXZsaGtRy3hzbZhxvzzNXt6mhiUhK6CrYuk43IomBeZfdVvJ4TQxvf72AdQFQMI6ZabRgrs878KNfPudOwruuIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نحوه عملکرد برف‌پاک‌کن‌های خودرو: توضیحی ساده از مکانیزم آن
#موشکافی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/685456" target="_blank">📅 00:24 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685453">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromقرار مداحی</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ای نخ عبات رشته نجات</div>
  <div class="tg-doc-extra">حاج محمود کریمی</div>
</div>
<a href="https://t.me/akhbarefori/685453" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✨️
ای نخ عبات رشته نجات
ای یم نگاهت معنی حیات
ای دم و صدات صدای قلب کائنات
🎙
حاج
#محمود_کریمی
میلاد
#حضرت_محمد
(ع)
💚
مرجع رسمی مولودی و مداحی
👇🏻
👇🏻
@gharar_madahi</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/685453" target="_blank">📅 00:16 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685449">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da12c27796.mp4?token=hU1lPfudrwQc78WZ32ymBGDkWFMlMSFiHJIL40_2ec9m7G6o2P7N6csV3LHDth7H8551CdgWJKlB6fkpkxc5dybtyqsl-kOJPgo5I4wwO4edfRp7DKhmx5s5JDdrRrSUxqYitT1MDC5O1DYZ2v3KMyk3KMQbO8E19DI7tMSRvpLOQLNf6r8wov-C4UaUt7YB9pOU4uoxZOz8ui0EHlWEWYiwZntv-QNCv8ip1WOFtY1wpE7EwS2dxyltx_kRH_a6OtwEjcb3VnC2gpaRE74yEFpVkdgTe3P79rfATzpFpZ8HzjkWqJ0jC-8-UH6t3_EdrZnYdaGw9PcVxiFaygizGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da12c27796.mp4?token=hU1lPfudrwQc78WZ32ymBGDkWFMlMSFiHJIL40_2ec9m7G6o2P7N6csV3LHDth7H8551CdgWJKlB6fkpkxc5dybtyqsl-kOJPgo5I4wwO4edfRp7DKhmx5s5JDdrRrSUxqYitT1MDC5O1DYZ2v3KMyk3KMQbO8E19DI7tMSRvpLOQLNf6r8wov-C4UaUt7YB9pOU4uoxZOz8ui0EHlWEWYiwZntv-QNCv8ip1WOFtY1wpE7EwS2dxyltx_kRH_a6OtwEjcb3VnC2gpaRE74yEFpVkdgTe3P79rfATzpFpZ8HzjkWqJ0jC-8-UH6t3_EdrZnYdaGw9PcVxiFaygizGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیو‌هایی که در روزهای اخیر از مسابقات تنیس در باشگاه انقلاب در فضای مجازی پر بازدید شده
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/685449" target="_blank">📅 00:13 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685448">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fTtd5fpmscmqh8Qt2whaHjfi2DHRekrK2CmFFStEUvTw8Xvc6lUdNVR_BGGpauRa0n6SAhgDgIakN5fu5IGMruNVpZXsPDb8VczfU5KJ2nA73qn1NBgSy16zsjOmCrr6lZmp-YO8YAbZWmFtvatJ9W2II8IlFwYBM1J2OD31i6wcN6QAPVhwr5v0DWN_oulrvgCK6mkK7mIHK6EfFP5nNdFoTqW0qXwyBxmADkypBMQ3q2iE_OgDgIWk59hoBM3_dk-R8UNrzpFxWStclOJaERmmo2o_e-xySeG0AeudAE8jJQEviJi2MoMaXmOcHPG-nsTsDk8cXnTohbVP8Tnf6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش‌ها به پیام محسن نامجو به همسرش | آیا او به همسرش نگفته بود به ایران می‌رود؟ | نامجو یک هفته پیش از بازگشت ناپدید شده بود!
🔹
بازگشت ناگهانی محسن نامجو، خواننده و آهنگساز سرشناس به ایران پس از نزدیک به دو دهه مهاجرت، به یکی از داغ‌ترین سرخط‌های خبری و رسانه‌ای تبدیل شده است.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3241385</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/685448" target="_blank">📅 00:10 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685447">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
هشدار احتمال وقوع سیل در شش استان کشور
🔹
سخنگوی سازمان مدیریت بحران کشور نسبت به احتمال وقوع سیل و آبگرفتگی معابر در شش استان کشور هشدار داد.
🔹
احتمال وقوع سیلاب و آبگرفتگی در استان های آذربایجان شرقی، آذربایجان غربی، اردبیل، گیلان و ارتفاعات شمالی استان های کردستان و زنجان طی روزهای یکشنبه و دوشنبه وجود دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/685447" target="_blank">📅 00:07 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685445">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E9rM-aMf53MqavxpSFsZhvbh7JEBqVccOlUmsfw_QzmfQ9_bafVEwO4fEGbO7N0Reuqe-mk2upyLXUMhy8BWib6Fjjycn40Wegmu930Pxz_JO1rO_xsoZenc8x_89J7XOEABjx2W9VC6wnPrPMJ6S3uuQmJtepZlPpz3wD3QRpSUGkky-QUv-bncxn_O2WI0yAwmGeMj1UaSgrBhwgU13s0hYEZUIrq64b2eVsUi5LHlmsn-GWREKWWCysr9ois6kFM4fNRGqsUaRasHJdme1eaQPRDJC1_C6aqzw5HXMjB3rkhbmZjvFYUl1Fw-yu-OK30oMEfMEPxdRQrq87fwWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/akhbarefori/685445" target="_blank">📅 00:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685444">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromقرار مداحی</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نماهنگ هله یا ایها النبی</div>
  <div class="tg-doc-extra">حنیف طاهری</div>
</div>
<a href="https://t.me/akhbarefori/685444" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✨️
تو معجزه ات قرآنه ولی
معجزه کردی با برادرت علی
اومدی که به همه بگی
ناد علی ناد علی سینجلی
🎙
#حنیف_طاهری
میلاد
#حضرت_محمد
(ع)
مرجع رسمی مولودی و مداحی
👇🏻
👇🏻
@gharar_madahi</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/685444" target="_blank">📅 23:49 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685443">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
حدادعادل: نباید مردم صبح جمعه بیدار شوند و ببینند بنزین گران شده است
🔹
پیش از اجرای هر طرحی، دولت باید پیوست وحدت و انسجام ملی داشته باشد و واکنش اجتماعی و احتمال سوءاستفاده دشمن در نظر گرفته شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/685443" target="_blank">📅 23:48 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685442">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6fe597b54.mp4?token=hAuWf1boxmzoLKvwB8JWBSRz4iVoo6sZA3VocC7KaVxPio7tKjmyGm9uvtNBjNwrAJHsKp0ICfltLivdRtuupCY9dPiEhUqeqxEcgaRrrc4jddjnmUzVIZlQtD5Z8mrBDU97atCVNc-jbIehbzlATWb6xpjSS37VDJvwfvM9MicptO37hk1s4siTUK2Ftr37oaHeKAedWdXetiV-VfDApH0qeDQXh7E1q15FT8HmPT7-eUHhjSrRrqjxXOR50IQSp6b0SamoBTyJ8hGuDni3iADAkAOSH88Ybs3Dr7eQN3QLlUQdROqG7IkyjuSeGgoBGWEE6vKKwfW5qhwx_Bk8wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6fe597b54.mp4?token=hAuWf1boxmzoLKvwB8JWBSRz4iVoo6sZA3VocC7KaVxPio7tKjmyGm9uvtNBjNwrAJHsKp0ICfltLivdRtuupCY9dPiEhUqeqxEcgaRrrc4jddjnmUzVIZlQtD5Z8mrBDU97atCVNc-jbIehbzlATWb6xpjSS37VDJvwfvM9MicptO37hk1s4siTUK2Ftr37oaHeKAedWdXetiV-VfDApH0qeDQXh7E1q15FT8HmPT7-eUHhjSrRrqjxXOR50IQSp6b0SamoBTyJ8hGuDni3iADAkAOSH88Ybs3Dr7eQN3QLlUQdROqG7IkyjuSeGgoBGWEE6vKKwfW5qhwx_Bk8wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تفسیر حدادعادل از پیام رهبر انقلاب درباره مذاکرات و خطاب به افرادی که قصد دارند مذاکرات را غلط جلوه دهند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/685442" target="_blank">📅 23:45 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685440">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
اصلاح سهمیه‌های کنکور به امسال نمی‌رسد
وزیر علوم:
🔹
اصلاح سهمیه‌های پذیرش دانشجو که از مهر ۱۴۰۳ در دستور کار دولت قرار گرفته، در کنکور ۱۴۰۵ اجرا نخواهد شد.
🔹
در نظام پذیرش دانشجو بیش از ۳۰ نوع سهمیه وجود دارد و طبق اعلام مشاور عالی وزیر بهداشت، در برخی سال‌ها سهمیه‌ای‌ها بیش از ۶۰ درصد پذیرفته‌شدگان را تشکیل داده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/685440" target="_blank">📅 23:35 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685439">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1340f65a8.mp4?token=Rj52YmYdJPiA9bPMJF_Toe9h3RQr9i5HXi2xjoBmK0jyK68pHjFZiZHaz_1QTjVx5sIy7oUT15gXYJP20mWyJYvr35h-xLp5lDoDN24_UrFRn15NKT8B7E5F81V-WmILtTXjulGgmASkbRlVbqmwqKTRr5bZjLJQD0M8ecsUOsfADxMDHEz6KP1WI9jPJ2c6I5g3kuyRq2BDDULaJg4TywMnN37K1f6jqF1qjN3R5SJNubWfeytlFXe49bl4IzJU1D4bNcRLbSdVlkVkeLzsFfXpwlsNiGXxxFdXlVJnNDdc3vqCPR2W3pJJqg353lLK5fTQHA0Ex7tEzrEdK-kYzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1340f65a8.mp4?token=Rj52YmYdJPiA9bPMJF_Toe9h3RQr9i5HXi2xjoBmK0jyK68pHjFZiZHaz_1QTjVx5sIy7oUT15gXYJP20mWyJYvr35h-xLp5lDoDN24_UrFRn15NKT8B7E5F81V-WmILtTXjulGgmASkbRlVbqmwqKTRr5bZjLJQD0M8ecsUOsfADxMDHEz6KP1WI9jPJ2c6I5g3kuyRq2BDDULaJg4TywMnN37K1f6jqF1qjN3R5SJNubWfeytlFXe49bl4IzJU1D4bNcRLbSdVlkVkeLzsFfXpwlsNiGXxxFdXlVJnNDdc3vqCPR2W3pJJqg353lLK5fTQHA0Ex7tEzrEdK-kYzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تفسیر حدادعادل از پیام رهبر انقلاب درباره مذاکرات و خطاب به افرادی که قصد دارند مذاکرات را غلط جلوه دهند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/685439" target="_blank">📅 23:34 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685438">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f8a45ff7e.mp4?token=sFfORJGC7ga02deNBs1SRiUB7T1qYWHuVzoKZnSUaPSClCP-wg6gOWTP2pqBIcrMeyipRHJ2J5c-N1vOXKbPS9XtxShjBPRrN1Zi3_KTRxzqqgDx-08Fo7GkG-HfhfMnDquklpH22623bMyAFQtzEPzxIL-z-NYBEkaBEWWn6Uwpnyq04Hr4446qgE5627pYEYhtx6VhZHpA5VJwUFQ9meObY-N06CQ7q7nwuj31BhYqKZB-uLIZMD6puG91ti12i3sLtxUFnqPL1LzrteQ85ftFWMzQPpAa-dR_onAdnksCi7oZmxApTmpKFWSN50IA5gWk7ORweGxisMPiaq_ETQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f8a45ff7e.mp4?token=sFfORJGC7ga02deNBs1SRiUB7T1qYWHuVzoKZnSUaPSClCP-wg6gOWTP2pqBIcrMeyipRHJ2J5c-N1vOXKbPS9XtxShjBPRrN1Zi3_KTRxzqqgDx-08Fo7GkG-HfhfMnDquklpH22623bMyAFQtzEPzxIL-z-NYBEkaBEWWn6Uwpnyq04Hr4446qgE5627pYEYhtx6VhZHpA5VJwUFQ9meObY-N06CQ7q7nwuj31BhYqKZB-uLIZMD6puG91ti12i3sLtxUFnqPL1LzrteQ85ftFWMzQPpAa-dR_onAdnksCi7oZmxApTmpKFWSN50IA5gWk7ORweGxisMPiaq_ETQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نجاتگران چینی در مناطق سیل‌زده نپال، هنگام جست‌وجوی بازماندگان گرفتار زیر گل‌ولای ناشی از سیلاب ناگهانی، با فریاد زدن «کسی آنجا هست؟» تلاش می‌کنند نشانه‌ای از افراد مفقود پیدا کنند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/685438" target="_blank">📅 23:28 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685437">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b18c117eae.mp4?token=KcKGSbTj_xIrEY_x5tjZd5sYuainFaj6vt5CjEwuBmNLrtfwDbcTPnJYivTTs2fVRIYAtQRT0js-Z8nIln7aLPxoiIqvbBNdoNpkdTUThaPELNtOwRNZ4aFiog5w-XdswyH0Z0nNmJofNz6AKH98-C036XfMeZkanWV_eRwxd0fghOUrd30oGA3z04iIsxW9_mWaEtSrdNJcfO2DzNoYLtzovtfS-OEbpDPkOzAl2lezSgdWXu3qdmBRjWI66Bq0D75JXB2gqL6IHBinDz2Yobt8odTvwx57LF5GZVj_prUDllWlh17XJe8Zyfb-rTbfKQyAuwdAxLZBC_RKhYgDEIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b18c117eae.mp4?token=KcKGSbTj_xIrEY_x5tjZd5sYuainFaj6vt5CjEwuBmNLrtfwDbcTPnJYivTTs2fVRIYAtQRT0js-Z8nIln7aLPxoiIqvbBNdoNpkdTUThaPELNtOwRNZ4aFiog5w-XdswyH0Z0nNmJofNz6AKH98-C036XfMeZkanWV_eRwxd0fghOUrd30oGA3z04iIsxW9_mWaEtSrdNJcfO2DzNoYLtzovtfS-OEbpDPkOzAl2lezSgdWXu3qdmBRjWI66Bq0D75JXB2gqL6IHBinDz2Yobt8odTvwx57LF5GZVj_prUDllWlh17XJe8Zyfb-rTbfKQyAuwdAxLZBC_RKhYgDEIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازیگران فیلم جواهری در قصر در گذر زمان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/685437" target="_blank">📅 23:25 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685428">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TiEHooVdzaBSQd0fSCso0-I6nXwypKiVWDYrVAj8IzDmmvqZBXQv5FXimtsiP5AJxUAxJs1DQt26WupkavlzAx4lrYS4lUfzfuWh55a01r94zeIYuaetxO1M02bT7FM9qN-r5xJ6zcxcNQx358_9dF7HTLObfePCphBVe2CEZIH4hPvfTG1Bs_nIi6MC7jyyp2kngUEUGTaGr-OpLWE7ZutQFu7lT4DD8Sqx1AvqlZ26DY4gMl3ozxPsMGIXDB6GxNKY8UsY_2mX1BGxcevHPSfSEV4TzAGWrSbR-CRlkNQo6f5eY9bJU5dlnJ5UI43mjPsS6dVxbEOwS5o3dILfyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gb_ElnHAYrcs-2B-dSUl9is2tC_CbdUhbtP9U9nt9YCuPveM2nxisV4VrF0OFGxqEBlUNNV05wgKpSMURertFJ3nHyjDnK6qu3dz7SMfPEjAqYAbKXWqQKZ1LrXbVkpeAyDKwQ7u0R1IljZH2-QCZdoq7mU3De9Qv-f4gUaQT6p0XmxckwmnvcrOcFHchllzWwd8N3xBTsoDTGPZptmhv6CZo7WKnPSblkQZQtvL_lg-v5Lf6BYhrPFlMMgqOkA45MuqmiISAzWUmPt2l6ttt1FSwA3N3uE3t4nUNB0uBD3yOYTCnM2bNgbVpdm8362DJypOfwqA_w2-3qexHpPfVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/neWtAqlUxFFshHYgr2dJIJlbERccRdjQLUZrG_C3H56cY6DvkCLFo-sVr_B4bkWN2HShSpL0OXK9K23jRjgzWRl6zlr4BKz7z0XXBO5AhPx-36-cbWWwaLZF1JK8nTspHoIed4jhhvYLuffYtMupBTipc9OPVs1eqg5dwYwLq1exyqAFbKjvlrH8Xkp3bhDzXRHfQoZn8d5OIIVUkIVYyUB6S4ab9ucYyhgSZeQlcjWl2VFeCRL3DdUc2da-OHz-E-fiJJfcRUkNRVg1ykxz5fufriq2VCemCrgDBIP_w94wNMJcmdUc2r13rR5kbDF5vEZmYteYNqGBdqd8ry2CPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HvatyUvAty7bk_1l1GqnhiuYqnobcpA1smsBgeQzvwiO05pOy75qUl3oWQm9jBWDCIILJ03h161G9ja_YAMfuSs3GYVimiZAnLMCQkPRjn7FCZi1NuPnSW1YGILOxPQf5diczC_g4pNDVrUn08TH5jE9vcIalXxTbJIm6lUDiRZLgTe5RQpUVh8k13uLZHDCgwbrM6JpWWKOraBj7TD8QcA6AaU3uYds-PaggU-dZmS7ZE7CqieGPQO_IytECgQzifJjCNJdjb9HdMzC7V3G0uvoBdGHukB61Pjg3kxOtZQus4OkURbYhAPSirEp5Inz8HC2cZNmuJFj2HS552WPuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KNElhP2g2V_w9YYq9eImPG48Xo7fth_S28J_K2vbspxnlhIBbtRIBQRiy8tH-E_NPb4mUnRa_-qUZJJARWox7hwZDPg0bWHsDaq7tBagQr4LWzMSTnh4FKs2YwxdECYRs_VifTJjccLqwsrshggnCIucgq0EobrQYHLkFhoQa4UaB_VtyECd3XvLY83ZIHHC80TEwGVQqPijkXAjKzEAmBSHgfY8lyGU8O8J2gAWzIGkVB6BOiPDPTrjIynewYJWkp39RurUlZAfhfeMzfAzQEa5dwmQmAYVzghZttT3ZhCWTL_HmRY2ptpfY8avSabKk3dVNfdJVnbzL-0HtV4pTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LRBL1ivHtYHw6-pLCzpHJ-925nBG4lex3aQgcRf4gekIErUldRe3bvrdI-Y23ZKqGR1I2JMqBwh2ZAKxgG9TyaByHDLyJyeA5eXIxG1ucWQIv_4wYmiedKDHPS0qb-iZg60GMrnENRGO-QF4HZHnuqKqUvWa0FPR0HgQN2ScfvPp4jdtGIlNxcAz0kKvbeM26uRIXL4HW7qrGGsx7U85jlJbW8qZSLP1tiBxnzrE7nRtkw4D8mnnRYyklcm_lgoR2jk5TGJrza7v7jjlECzo2Ew0aacslboHTs3hY4d9d2WT-PApw-89TabFbnROoT_kys-7JpyvvbTH74roe3iYlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nwP36kFLX0HxYDqgEdGKYQVrwF_KoTJUf-EbfFh3IoTUDKNZjGl-eSD5APMzS-osp4nkhJs4jFfsHKiSa2fCxT7UZM4AgSbb-gKtZBBs0EMrkQGOtNvMHg2urQSaejtGPWmfQu8-LaH3wiUmYOcZsSwWVSFxKoQOD9_Mm6tHUW1fXVFadg2YebZ7NyZU2yiQqgPxWI3TI8B7h2Ri6sWnwAAFwjM0DIilA93dCX2w37GsMTaJc8vurxTGaaQ1Awu7XAzGNX1huyTonDelW4MltoH97PYjWZu-3okopreMHtB0GoJ1ywrKMEk1D338y7tolo-hM3wQtCG71PRBViCaGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cad3UB_TO-4C4ZOzhyEgLcJqT9mKOkPlbBIfDLh8Dc_JGk5w9LHQ1D0SpEVOiwybpIIEA72d_o1oo22sRA0QBAfI-7DGnHfn66P9kAAYqbNeDSJj6CW24sPWPRiQ0wt-xP-sq7gU2mtejEZ-h7eeBHma3Q4VQci_43KBg_viYHfimBZQVa-0gyk6jayz9tGg80Q0o7T5_EGzwc2Rzozyw9c4dTWIu0sDG6-AMkJ-YGinkJqd3w-gAom0JHihwe9YW6pDrdql3X9s7Ot2ymIbewnDHeFmr7CUP5n4aMgYChztuftypEzYht34RffRgH5168DQGPORLk59ndfkiXluNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FDVJ81Y3C1LUHCE2cMtX-X_e9uJ9ldsiVvuJCy2vkhmWRXzDqMO26SIcMNLmag7GZikpcfZBR1t8NHSR-nJpvKcL8EU7SGFEcRRihL6tVh25WjL5OQB8noGcZrS4zS3uCD9-oCuilgrJu90ZxFnnKeJ_Fsys14w_CpMofahxcgG8oXjacT0YGnrmymHwHWkjVKBTobwMyOvDCziIFgRKuGATx_4y7YifEMjI1ixnStUFVRNiZ3r7h0zbDq4nXV6Ikh71FYwnk5pjScWPjGBL0Ahllco5k3zpII2cw_F-aDicnz8rggEwpONcTNoy0qdHTEhV7Tsy9fy1KKa9OPuLzA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
درد دارو
🔹
روایت بیماران از بحران تهیه دارو؛ سرگردانی در شهر برای یافتن نسخه‌هایی که بی‌پاسخ مانده‌اند.
🔸
الوفوری را دنبال کنید
👇
#درد_دارو
@Alo_fori</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/685428" target="_blank">📅 23:25 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685426">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🌹
دسترسی آسان به فایل‌های تصویری برنامه "زندگی پس از زندگی"
داستان افرادی که از مرگ برگشتند
#فصل_پنجم
🔹
اول
🔹
دوم
🔹
سوم
🔹
چهارم
🔹
پنجم
🔹
ششم
🔹
هفتم
🔹
هشتم
🔹
نهم
🔹
دهم
🔹
یازدهم
🔹
دوازدهم
🔹
سیزدهم
🔹
چهاردهم
🔹
پانزدهم
🔹
شانزدهم
🔹
هفدهم
🔹
هجدهم
🔹
نوزدهم
🔹
بیستم
🔹
بیست‌و‌یکم
🔹
بیست‌و‌دوم
🔹
بیست‌وچهارم
🔹
بیست‌و‌پنجم
🔹
بیست‌وششم
🔹
بیست‌وهفتم
🔹
بیست‌وهشتم
🔹
بیست‌ونهم
🔹
سی‌ام
🔹
سی‌ویکم
🔹
سی‌ودوم
#زندگی_پس_از_زندگی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/685426" target="_blank">📅 23:22 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685425">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
پاسخ نیروهای مسلح به هر تهدیدی محکم‌تر از گذشته خواهد بود/ جزئیات عملکرد پدافند در جنگ ۴۰ روزه منتشر می‌شود
امیر زاهدی، فرمانده دانشگاه پدافند هوایی خاتم الانبیا:
🔹
نیروهای مسلح جمهوری اسلامی ایران در هر لحظه آماده هستند و پس از پایان موقت جنگ نیز آمادگی خود را حفظ کرده‌اند.
🔹
پاسخ نیروهای مسلح و ملت ایران به هرگونه تهدید، محکم‌تر از گذشته خواهد بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/685425" target="_blank">📅 23:20 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685424">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01cc087fc5.mp4?token=nlFPlEprMQB0MPBJCAPzzc95fklFAKco4o_skLhrq-t9U3Ra-eNEnWkSJ4eA8sQ_jSHNT9yg8itx3c0ziYBO5fGvSy9PtSmWpdrt_u2UrTr06qDAUhG1HIfPt-aTA6JivdhYH_4fzVbwm5m0TA-3DaCA3iLez2fxo1ucgH9pVvL_MMMAJApCqhKz3I8_aHOnJplCBTf1O3Gg0IBszBpTJe3AhAkgScwBjlHkkQ68snhIsnWzRG7MNzJBWSz2GO3i7z4REZ4BHiXr_M_w-mxnfFQbIvd0Mz2zfAEAk0vhG1CuBDVYVg-lqL3bk9MD8T8gdNg5-O3zsksoaXEbwbRgRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01cc087fc5.mp4?token=nlFPlEprMQB0MPBJCAPzzc95fklFAKco4o_skLhrq-t9U3Ra-eNEnWkSJ4eA8sQ_jSHNT9yg8itx3c0ziYBO5fGvSy9PtSmWpdrt_u2UrTr06qDAUhG1HIfPt-aTA6JivdhYH_4fzVbwm5m0TA-3DaCA3iLez2fxo1ucgH9pVvL_MMMAJApCqhKz3I8_aHOnJplCBTf1O3Gg0IBszBpTJe3AhAkgScwBjlHkkQ68snhIsnWzRG7MNzJBWSz2GO3i7z4REZ4BHiXr_M_w-mxnfFQbIvd0Mz2zfAEAk0vhG1CuBDVYVg-lqL3bk9MD8T8gdNg5-O3zsksoaXEbwbRgRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گوشی‌ای که براى خيلی‌ها، اولين تجربه استفاده از گوشی هوشمند بود
🔹
گوشى Samsung Galaxy Gio از مدل‌های اقتصادی سامسونگ در اوايل دهه ۲۰۱۰ بود.
🔹
اين مدل براى خيلی‌ها يكى از اولين تجربه‌هاى استفاده از گوشی هوشمند محسوب می‌شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/685424" target="_blank">📅 23:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685419">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/135e761d0d.mp4?token=u0Vn04oD_pkzj_NTi1n0ayQlVyGNtiHUnClTqdxrMBaaP80NVHjC18mYJm9nUODCRDv6bglixbaZ3mWYnxVfLaDn8aTH0z-JC_t6qTXUpcolYpFRppva97PfaZSDrVXqiuHopbrXvM-U0OWHWApddshQivsg3DUqIREmCbd7l_VGL_Db6N5fqsz0WNz7vVx4TSeTcXG_hiZGOC_PTMOkIOwRKKV9m6HGIJRlcWjeOKGEa8jxW-9wgRMBesskrl4QyCp8_a3nGkWS57cDg2FfuDzi9KB6IdKMBkv4ywK_9cHBHtQxw3W_p-OIgsDIHiJ4rbCYUbCsomowYx6U7gUWmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/135e761d0d.mp4?token=u0Vn04oD_pkzj_NTi1n0ayQlVyGNtiHUnClTqdxrMBaaP80NVHjC18mYJm9nUODCRDv6bglixbaZ3mWYnxVfLaDn8aTH0z-JC_t6qTXUpcolYpFRppva97PfaZSDrVXqiuHopbrXvM-U0OWHWApddshQivsg3DUqIREmCbd7l_VGL_Db6N5fqsz0WNz7vVx4TSeTcXG_hiZGOC_PTMOkIOwRKKV9m6HGIJRlcWjeOKGEa8jxW-9wgRMBesskrl4QyCp8_a3nGkWS57cDg2FfuDzi9KB6IdKMBkv4ywK_9cHBHtQxw3W_p-OIgsDIHiJ4rbCYUbCsomowYx6U7gUWmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨️
هزار طایفه آمد و هزار مکتب رفت
و ماند شیعه که قال الامام صادق(ع) داشت
#پک_استوری
ویژه ولادت امام صادق (ع)
💚
@Heyate_gharar</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/685419" target="_blank">📅 23:12 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685417">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
دلیل سفرهای اخیر قطری‌ها و پاکستانی‌ها به ایران چه بود؟
غریب آبادی:
🔹
تلاش قطر و پاکستان در سفر به ایران این بود که بررسی کنند آیا امکان بازگشت به اجرای تعهدات تفاهم اسلام‌آباد وجود دارد یا خیر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/685417" target="_blank">📅 23:02 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685414">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
الاعرجی: ایران خواستار اخراج گروه‌های تندرو از خاک عراق است
🔹
قاسم الاعرجی، مشاور امنیت ملی عراق شامگاه امروز شنبه تأکید کرد جمهوری اسلامی خواستار اخراج گروه‌های تروریستی تجزیه‌طلب از خاک این کشور است.
🔹
حضور نیروهای حزب کارگران کردستان (پ‌ک‌ک) در خاک عراق غیرقانونی است و «ما با طرف ترکیه‌ای برای حل این مشکل همکاری می‌کنیم
🔹
وی حضور نظامیان ترکیه در خاک عراق را برای مقابله با عناصر پ.ک.ک دانست و گفت: شرایطی که باعث حضور نیروهای ترکیه در خاک عراق شد، با پایان پرونده حزب کارگران کردستان به پایان خواهد رسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/685414" target="_blank">📅 22:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685410">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pyftUbFW6ZoCU3RFfXR6cV510Iy6gldotvdcvvipmmIjNgnMC0f78gI6wacyV06rihtBrsQPPqvfqQajB5waJqfotZvCHUdTPpDUkR2sEd3QNxyYFZIFz5nIOySu51YqwWNP54fAFd3Qks92rW9VF6k63v1ycsZ85xbUxD6KBooi3OCSBygIzws-QGFYbvAZ-arUF7J7BX3bkQs22QTXoNpGB5IMTVfxH_uj64GeP-fVDZKvW8Ti4jchnWYiYJzSAhDyzpIfg4jYAAUN94-bD_HOU0dSoM-3IZy6T-1NvexAaLQOnQP07jJeTLKlQ1fhqhcAebygJQvFrw5yjLiDEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jp7eIDQ7VY41GRTwkpMkhXwiyhctiIW79C_ZAEUvZHtQnjZckTQZL6QjSFyeErDJZdD4yr5sAq0B1SPKqZZ7QlJD5J-iSMU5eWmLVQ2nJScp4m9Nr18AUI76nWYF1sO2Xs0E-RDyPPWfZmDPAXOvBfE9slGlpSdy8y_obigBC7l0gLu6QSYTXX_MqU2eTAaQbCnPDAEkdZi6ZhacE6H62Zfe0W3W1EGwP0h-sYQGpca0TaqXjwqzE-y7-6HS7qD_yf4v-9kOG3tu-zNXawmuPF6fHgZNuxGFJBadtANOn7XvbGrMjAXklkaws6wWl1UlUYGgRMaRIAgo_BDAEW7a4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U5dTMTenLhSmVEbHuwxTLi4SVzKV4o8mhBx15lFlqWD_5UI09wpcRci_1QtjHsYvTPWTSYp3hbrxn79fuZG2HhEMBRog6ANo-YCqkEarWw3VvN8vIC6-adsVZaP4LZSQmKVFOcLxpX7ySOBOSL9tNnfK892PbbnROLmjLfqJuaLhwJjt1hppNWGXMSCJczi9OyKSPzfMEaeOsDhreQlbAoLPtv_6IQeE1sl07Nnx4XMVkDnqsYYKkpWG0Gof0GNOkGArOOoEA7X61RSAOEPFsLIU5Pw50CriMcEhfpGieYTg4kzLXfsxdEWdQMiwkpd6DTz_CVcA1b0kD6BHt-xVNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ep4T7v8qIbsOtc-yQCEo-LWF8-LpE9vdMufB9Ol_IpHc3oEu6qU9IRyeZuODty5S6QyLjvRII4fJiYIz1U870l23Bg3Cf4KYzdzjaOjg31Nouaif1Ti6SMfF-mRIKejPzh2zZVkustox5D7Xz-eHfj9klwpGH2IH7oLWsVhfWydT_ucn4nA_D9Qo7Qxu0QjIrfc52yn4g1gzQ4HjYVfgBbEA1thwpIKMhUetuK6GEHz6XNsZAKtonD-oFI9e5sUlFppUlUoCo4HNsLejSecnqbJ27wgAHk3nXsC4NnusbQiyLGXvHcSGyjb9MXTSO1bgzlcJKbsT4lTmqKZtW937Iw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✨️
دوای درد دین و درد دنیا ، درد بی دردی
حضورت دردهای مرگ را حتی طبابت کرد
▫️
#والپیپر
به مناسبت میلاد حضرت محمد (ص)
💚
دریافت فایل تصاویر
👇🏻
👇🏻
@Heyate_gharar</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/685410" target="_blank">📅 22:46 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685408">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55c81e867b.mp4?token=tLB6gWNIb6L8w5YjUVJlk_AHHfo56MxMl7MgDUFp7IWF4cyzcdChr5N7ccG_hQ1Yv8oyjcK1rBMdwVpJ8eKObFFyhTXutMY5lv6TP0pbLUioGkfKeoJ0a4s52PJWIcbSq171Vw7lxFIi2M5lQyciKXZhOGjaf1peDB3CmaAGe0_FR9QxEJkNro2lcodAmRwWJDamVIJOsFum_BDfifKlI8XTx4LaeEsiWD6Z8V1MSU7PzDWis_Pxj2X-5e21FeoJAj-ahGKIz4ICsFdstlMFxiUf_10AiVHEDHpHDKKDLQUnoafOQsgSE-FoJfuAQkA8o39bvAP0EBX7agX8t07R3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55c81e867b.mp4?token=tLB6gWNIb6L8w5YjUVJlk_AHHfo56MxMl7MgDUFp7IWF4cyzcdChr5N7ccG_hQ1Yv8oyjcK1rBMdwVpJ8eKObFFyhTXutMY5lv6TP0pbLUioGkfKeoJ0a4s52PJWIcbSq171Vw7lxFIi2M5lQyciKXZhOGjaf1peDB3CmaAGe0_FR9QxEJkNro2lcodAmRwWJDamVIJOsFum_BDfifKlI8XTx4LaeEsiWD6Z8V1MSU7PzDWis_Pxj2X-5e21FeoJAj-ahGKIz4ICsFdstlMFxiUf_10AiVHEDHpHDKKDLQUnoafOQsgSE-FoJfuAQkA8o39bvAP0EBX7agX8t07R3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی عجیب از درگیری چند دختر باهم؛ گفته شده این درگیری مربوط به دعوا برای یک پسر بوده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/685408" target="_blank">📅 22:42 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685407">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
پشت پرده گرانی‌ کالاها با وجود افزایش تولیدات در کشور، چیست؟
وزیر جهاد کشاورزی:
🔹
هیچ مرغ آلوده‌ای در کشور توزیع  نشده است
🔹
اقدامات ترامپ و جنگ با ایران سبب افزایش قیمت جهانی برخی کالاها شده است و در این میان برای ایران آنچه که بیشتر از سایر کشورها افزایش یافته است، قیمت حمل و نقل است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/685407" target="_blank">📅 22:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685405">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-poll">
<h4>📊 برای سلامتی همه شیعیان امیرالمؤمنین علی(ع)چند صلوات هدیه به محضر پیامبر اکرم(ص) و امام صادق(ع) می‌فرستید</h4>
<ul>
<li>✓ ۵ صلوات</li>
<li>✓ ۱۴ صلوات</li>
<li>✓ ۱۱۰ صلوات</li>
<li>✓ ۱۴ هزار صلوات</li>
</ul>
</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/685405" target="_blank">📅 22:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685404">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
ایران دلار را از کجا می‌آورد؟
الجزیره:
🔹
با وجود تحریم‌ها، ایران از مسیرهایی مثل فروش نفت به چین، دریافت یوان، صادرات غیرنفتی، صرافی‌ها و واسطه‌ها، تجارت با کشورهای همسایه، حواله، طلا، ارز دیجیتال و تهاتر به ارزش دلاری دسترسی پیدا می‌کند.
🔹
چین خریدار اصلی نفت ایران است و بخش زیادی از معاملات با یوان انجام می‌شود؛ سپس شبکه‌های واسطه‌ای این درآمد را به ارزهایی مثل دلار و درهم تبدیل می‌کنند.
🔹
عراق و افغانستان نیز از مسیرهای ورود دلار نقدی به منطقه هستند. در کنار آن، صادرات پتروشیمی، فولاد و محصولات کشاورزی میلیاردها دلار درآمد ارزی ایجاد می‌کند.
🔹
در نتیجه، تحریم‌ها ایران را از دلار جدا نکرده‌اند؛ بلکه مسیر دسترسی ایران به دلار و ارزش دلاری را پیچیده‌تر و غیرمستقیم‌تر کرده‌اند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/685404" target="_blank">📅 22:31 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685403">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
غریب آبادی: ایران برای بازگشایی تنگه هرمز تعجیل ندارد/ تفاهم تنگه هرمز با عمان وارد مرحله اجرا نمی‌شود مگر با انجام تعهدات آمریکا
🔹
جمهوری اسلامی ایران با عمان درباره ترتیبات عبور از تنگه هرمز به تفاهم رسیده است، اما این تفاهم به‌صورت خودکار وارد مرحله اجرایی نمی‌شود.
🔹
اجرای این تفاهم نیازمند انجام تعهداتی از سوی طرف مقابل، به‌ویژه آمریکا است و هر زمان این تعهدات اجرا شود، ایران نیز اقدامات خود را انجام خواهد داد.
🔹
ایران برای بازگشایی تنگه هرمز تعجیل ندارد و همچنان به اقدامات دفاعی و مقابله با تهدیدات ادامه خواهد داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/685403" target="_blank">📅 22:27 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685402">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
وزیر جهاد کشاورزی: ایران در شرایط سخت جنگی، برای اولین بار در تولید گوشت مرغ خودکفا شده است و به سمت صادرات آن در حرکت هستیم
🔹
تولید گوشت قرمز نیز افزایش یافته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/685402" target="_blank">📅 22:24 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685397">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromقرار مداحی</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">السلام علیک یا رسول الله</div>
  <div class="tg-doc-extra">ماهر زین</div>
</div>
<a href="https://t.me/akhbarefori/685397" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✨
به پایش ریختند از نور‌ها آن قدر از بالا
که سینه ریز خورشید این وسط ناچیز مثقال است
#پک_مولودی
ویژه ولادت حضرت محمد (ص)
مرجع رسمی مولودی و مداحی
👇🏻
👇🏻
@gharar_madahi</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/685397" target="_blank">📅 22:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685396">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d2d0487e0.mp4?token=Rmp5d2woqEcgAIa4P-ZN-A40QjZDD2hyYsbL7ioeTxrxwKry7HQoliLeh7QvYUBFzG9Y0sJCX-EOjbwgaFVdI4xhf5aer5PzDjvPEAOrp5npHIW31KoOj_iQMWbCRuRhKC4oHj4fz8b7O_mNEDSMNME7ypdX2yl8QEjjWB4HNVohgdoxv3il4J452C9z0tqoTvkLI7KzMXqJLp5zxWKnYXkvAhMTxMS9PLO9-EYzBm8PLjwXtDAvmJbTdJ0JRErBV21e60nGSdTceQwkhIwQF7Wvg5RtNlycoRq6--MvXeNiOHgYcYQud5iOQCo1xYymAcTLtA-eIUxzBoDiaS9Llw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d2d0487e0.mp4?token=Rmp5d2woqEcgAIa4P-ZN-A40QjZDD2hyYsbL7ioeTxrxwKry7HQoliLeh7QvYUBFzG9Y0sJCX-EOjbwgaFVdI4xhf5aer5PzDjvPEAOrp5npHIW31KoOj_iQMWbCRuRhKC4oHj4fz8b7O_mNEDSMNME7ypdX2yl8QEjjWB4HNVohgdoxv3il4J452C9z0tqoTvkLI7KzMXqJLp5zxWKnYXkvAhMTxMS9PLO9-EYzBm8PLjwXtDAvmJbTdJ0JRErBV21e60nGSdTceQwkhIwQF7Wvg5RtNlycoRq6--MvXeNiOHgYcYQud5iOQCo1xYymAcTLtA-eIUxzBoDiaS9Llw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پایان زندگی هرکس مرگ اوست، جز مرد حق که مرگ وی آغاز دفتر است
🔹
دست‌نوشتۀ سپهبد موسوی فرمانده شهید ستاد کل نیروهای مسلح
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/685396" target="_blank">📅 22:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685394">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HMo-f0I_HiYVvZ7UIS5z9YKiY5GQGNwWZH8bIDuVdLFW8FLx3179rc24hYYxFfgEyhm1oHeu7xv3L83Gcae9X___9kwD7klXqUQ8jv39gaYYCjI2Cd_EGX9F0koH_1SqskP2nPJ6mOAFJsts-C75TqrBwpgwYeGaejL9kKIUk_5aH5Aj8szEtw77JuHe-aQ2X5cn233o7CnGk862Yq0ncl_T4Zs4UAR_WWBcYdQk6QpzFzPxqEFPkVEfO6w4qC2suwTYfstYSCj0FzNSEGUS3KubKo74Yd6R-miGvQnQptpecIdflIl8KHp-6LthHs7JURKckuKq8fOAjbI6Yg2QFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نماینده مجلس: بدهی تراستی‌ها باید دلاری تسویه شود، نه ریالی
🔹
رحیم زارع، عضو کمیسیون برنامه و بودجه مجلس، گفته بدهی تراستی‌هایی که پول حاصل از فروش نفت را بازنگردانده‌اند باید به ارز و با نرخ روز تسویه شود و تبدیل آن به بدهی ریالی قابل قبول نیست.
🔹
وی یادآور شد: در سال ۱۳۹۶ نرخ دلار نزدیک به چهار هزار تومان بود؛ یعنی یک میلیارد دلار حدود چهار هزار میلیارد تومان می‌شد، اما این مبلغ تاکنون تسویه نشده و با احتساب نرخ ارز به رقمی بالغ بر ۲۰۰ هزار میلیارد تومان رسیده است. یعنی ارزش این ثروت حدود ۵۰ برابر افزایش پیدا کرده است.
🔹
این عضو کمیسیون برنامه و بودجه مجلس بیان کرد: دولت باید بدهی خود از تراستی‌ها را به نرخ روز ارز بگیرد، نه اینکه معادل ریالی آن را دریافت کند. اینکه دولت بگوید معادل ریالی ارز را از تراستی‌ها می‌گیرد، درست نیست و اقدامی اشتباه است./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/685394" target="_blank">📅 22:08 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685393">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVzSlGDWFYIyw6sL_60hHcl3DkW3tC75KOtO7LVNWtFi6mG9nTSMOxSwyb5NWzdP5oDzsP1DTpf0wdPrf6qxZudowaRTmjmmACGtHdceadzJz60URmIJdkng7w_VTn5FoUTxj8HbvqQT7tt486FxkR3tER84-bIx059nht71XuCl2vPJ33a7o6aSu9pIlbxKfGQdorbGq5aSyrOLz54oEHTVfJpX5872MdXZ7mst0tSUR9FJ7CFEP7NzUZL58eVK_DuslWxoHt1UFFamtknNqsLHGZuNXqwzpcICE1dpMYKB-GECMx2G6Wgwuj59GIe8h2dCv7d62IQBWvg5z7i5Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شیفت دفاعی ایران آغاز شد/ استراتژی جدید ایران در مقابله با آمریکا: درگیری مستقیم، حفظ سایه ترس و دیپلماسی با همسایگان
🔹
اکنون، ایران در سال‌های ۲۰۲۵ و ۲۰۲۶ در دو جنگ دیگر شرکت کرده است و درس‌های جدیدی را علاوه بر درس‌های قدیمی فرا می‌گیرد. واشنگتن باید به این درس‌ها توجه زیادی داشته باشد، زیرا آنها استراتژی ایران را برای سال‌های آینده شکل خواهند داد.
ترجمه گزارش پایگاه The Dispatch را در وبسایت خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3241350</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/685393" target="_blank">📅 22:06 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685392">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aef7f9f7d3.mp4?token=DOsnoMkBaLNEOjxqNe7zYsfp2j1Xg-FjEPmzjQqFcdFJSS4tM_chynt-NemYGqr1w3QpGBvMgyIHMY5D0YiYq8w2LY4Hzi_In8oPg5ZxVgP1nzlhRk5u1Fsv2AC4eD4HI7ZkIy95pkAbxJBdR1H4GYIJB8VtnMYQrTCwnxav9f1cDTgj4s1H44aVuFOA5PixXryovQirSlLjyga_ZbOg3EpTvvrS6Y2HppnnPDtjdQCsOpgci6ssVcrWs6XnPcoKdxHxoVrH2jk-srOPEHCP938Z51IiMDgOyrmdY8WLbPjlr3_tsO_ZWU0aRiQDBMYgpxo9VSJkUDZ8MCRFKHDm9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aef7f9f7d3.mp4?token=DOsnoMkBaLNEOjxqNe7zYsfp2j1Xg-FjEPmzjQqFcdFJSS4tM_chynt-NemYGqr1w3QpGBvMgyIHMY5D0YiYq8w2LY4Hzi_In8oPg5ZxVgP1nzlhRk5u1Fsv2AC4eD4HI7ZkIy95pkAbxJBdR1H4GYIJB8VtnMYQrTCwnxav9f1cDTgj4s1H44aVuFOA5PixXryovQirSlLjyga_ZbOg3EpTvvrS6Y2HppnnPDtjdQCsOpgci6ssVcrWs6XnPcoKdxHxoVrH2jk-srOPEHCP938Z51IiMDgOyrmdY8WLbPjlr3_tsO_ZWU0aRiQDBMYgpxo9VSJkUDZ8MCRFKHDm9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تلویزیون دولتی روسیه نحوه نابود کردن بریتانیا با بمب اتم را بررسی کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/685392" target="_blank">📅 22:04 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685391">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pkEEUC2RFvXoKqH3mum7TWKO1ghhbEWfpVzu80q_BgfcKnO-9wm4P4XBkM6Fn3mVxUAmBhS_hBlXTbnNyPOl-SDJHEytKYfQXew29dbEGcc75QiO46SEIIE5tlKQx79Pdnj44p0HdrAlRTv1ijHLuFIL91t4xhm33tXdntr6_L6vvWAAtVEb-rp7h5ppusuGdOISsomj-JBBQxixPc6Vi2e6jlLV73qlLtc8Ce86oxnIincjQkdSE7Xahc5zHNtVoug8pxi9mRpqZn4VvwiXW7ObkDOKo4g_WwtUU8Qr0S76khCwIr2FtoykRrs4PSdHjqr6a0uYb6i652DP-dDiuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صبر، فقط تحمل سختی‌ها نیست؛ انتخابی آگاهانه برای رسیدن به چیزی‌ست که ارزش انتظار کشیدن دارد
🔹
امام علی(ع) در نهج‌البلاغه می‌فرماید که صبر دو گونه است؛ صبر بر آنچه ناخوشایند است و صبر در برابر آنچه انسان دوست دارد. گاهی باید برای عبور از سختی‌ها صبور بود…</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/685391" target="_blank">📅 22:00 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685389">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a4eecac98.mp4?token=RWOBphbVAb--yM10jqmFXdkJ5CiJbsi1td_NGKBi6dWUlGoqBsETGRVH2HWCHTbTzLtdnG04QYVskAKxRDSIBPubvvj2qv3cCybVFjDSDHS3KRJxgqCn-tGFK8UJyivLSZ6HbIfHJpck8de2P6ybno5iQ-JePkppC030ly_PEP42RwrGs59ZbOtrwSG8vV7gl2SLrkABZxTjzIkUcAIkpit6Ge0ROaRvnvuvJzMzjytzWuApsUDSB3nvduZaToY7xI0MjScHNT0uf_ohHwwG_ZkaTuA61XW9drU4eF-gKru84UwWbZSTt1JZOkDu3Qo1bIzQ5AxXdKRF0y4nEBKJIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a4eecac98.mp4?token=RWOBphbVAb--yM10jqmFXdkJ5CiJbsi1td_NGKBi6dWUlGoqBsETGRVH2HWCHTbTzLtdnG04QYVskAKxRDSIBPubvvj2qv3cCybVFjDSDHS3KRJxgqCn-tGFK8UJyivLSZ6HbIfHJpck8de2P6ybno5iQ-JePkppC030ly_PEP42RwrGs59ZbOtrwSG8vV7gl2SLrkABZxTjzIkUcAIkpit6Ge0ROaRvnvuvJzMzjytzWuApsUDSB3nvduZaToY7xI0MjScHNT0uf_ohHwwG_ZkaTuA61XW9drU4eF-gKru84UwWbZSTt1JZOkDu3Qo1bIzQ5AxXdKRF0y4nEBKJIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
اگر عاشقی کنی و جوانی
عشق محمد بس است و آل محمد
اینستاگرام هیئت قرار را دنبال کنید
👇🏻
👇🏻
https://www.instagram.com/heyate_ghararr?igsi=YXZnNWZhaHRycTlm</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/685389" target="_blank">📅 21:53 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685388">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/992b33ce12.mp4?token=QQG27vifPhN8cVZ-lue3CMu_oh8xnq4t4zXJs1HuqM0pGXMwFeyvaKXBpsffQeyll1OD_Z7NHsFxGPNEjB1GJCCZmXoZD9HHtNmPUUQpCF43_TmsT1DghmhPuvjzDA1mSIJ0abbc5SjUkb6kOq7r0756NUiIBGYWN_VCR-iftbxfEL-no9zKW1hp2dF9klpQRVeLUURIe8bSnvi3Kygy68V1MZkOvcJaBI_k3DHSIDCnAVcYNoukq7H8UnrRfCGy628VjfF9uy2QFrcWbfQbvHaJaWjAIqBG6it0SKKO0nJQcmFyYImVaF3exmQrEb1WpWbVEAvnYPkCv0kzXaX2xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/992b33ce12.mp4?token=QQG27vifPhN8cVZ-lue3CMu_oh8xnq4t4zXJs1HuqM0pGXMwFeyvaKXBpsffQeyll1OD_Z7NHsFxGPNEjB1GJCCZmXoZD9HHtNmPUUQpCF43_TmsT1DghmhPuvjzDA1mSIJ0abbc5SjUkb6kOq7r0756NUiIBGYWN_VCR-iftbxfEL-no9zKW1hp2dF9klpQRVeLUURIe8bSnvi3Kygy68V1MZkOvcJaBI_k3DHSIDCnAVcYNoukq7H8UnrRfCGy628VjfF9uy2QFrcWbfQbvHaJaWjAIqBG6it0SKKO0nJQcmFyYImVaF3exmQrEb1WpWbVEAvnYPkCv0kzXaX2xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر کشور: تفاهم‌نامه اسلام‌آباد بهترین توافق تاریخ معاصر بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/685388" target="_blank">📅 21:49 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685385">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h4StMquAmCDj4ik6lzjiTNJmzq94T1LSGYjoLDXPuautC4h7m0EpKF1gTk4IwMgi8g3T4HTCVfGoQIfPZYW9BmIyp5Hofa-cQNy0yTrN2FMWQx4SLgImkhm_k4yCYWexxCeP0NfNFbGUIQ-ZWGR1AOolaFx5saFS9ulhfEx4O_w9uFbYlXElrD6QoDe1_RxVXSnH8DFApWYYsAmWGDuRT8SwchTIoOnks-ZIaJzX9lSMCGvRKhR4xAXS5IxeeYXI0vAWj_TWrev3_hIzm9S7WrgRxiHJyXJ4681siHcuvth7iTzq5Yi962HWnhs6XMOhhB3S5hUl7itU4xO13C57uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ریچارد ژئوپلیتیک و سیاسی: خودکشی یک هژمون
🔹
جنگ ایران به عنوان یکی از بزرگ‌ترین اشتباهات راهبردی آمریکا ثبت خواهد شد. آنچه به عنوان تلاشی برای نمایش قدرت ایالات متحده آغاز شد، در عوض محدودیت‌های آن را آشکار کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/685385" target="_blank">📅 21:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685384">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bx2Unt0f2zKnWA4TRPqszE3vptIFJvmEfnhzLQho3FiYQika0i0rN-YY_rJ6WFzJPxERvRtmd1xP8wztgXRujrdoE1u3dtOr0M01A0gkMdLGbEKhDO_Ow1PWxnKTAh58NZTq_dd6Q5xgfWgFuyjW94UEIND6JK9DX_3Cc_uQCV90YJhrLv6OlAeXCxDmaja3yTu-JV_cILEGELVh68SmAapPXooAAHcxo5Ves-mDiAo95ASWwr0PmXqcaswJC3eLGswPVhZIxA_gEsa97cknF8pkziL_KbsZ4Ek3jjZlL6jEAuuI97gw9bBjj2rSP47vdM1vuHX92xagOcmg9sW_NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای
باراک راوید: دو مقام اسرائیلی می‌گویند ابتکار بستن تنگه هرمز از سردار علیرضا تنگسیری، فرمانده وقت نیروی دریایی سپاه پاسداران بود
🔹
در ۷۲ ساعت نخست جنگ، ایران اعلام کرد که تنگه هرمز را می‌بندد و هشدار داد که نفتکش‌ها و کشتی‌هایی را که تلاش کنند از تنگه عبور کنند، هدف قرار خواهد داد.
🔹
اما به گفته مقام‌های اسرائیلی و آمریکایی، سردار تنگسیری در پشت صحنه دستور استقرار مین‌های دریایی در «طرح جداسازی ترافیک» (TSS)، یعنی مسیر اصلی بین‌المللی کشتیرانی در تنگه هرمز را صادر کرد که وضعیت را به‌شدت تشدید کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/685384" target="_blank">📅 21:36 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685383">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
دولینگو (معروفترین برنامه آموزش زبان) اعلام کرد آزمون‌های این برنامه از ۱ سپتامبر (۱۰ شهریور) برای تمام ایرانی‌ها متوقف خواهد شد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/685383" target="_blank">📅 21:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685381">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESw1tpLYlmNfRfvosPMSn-2p_D2g7il38U3XGx9liSrQPd3kp79JQtXoPHVFRTYdDjPset4VUn-6drJbVktITDRmwUo5roB4Itrde16qsKpV-32ySmVJBA6VTWXMPUfEkBfYS-qsTAVkOKIEAPno0Hxr8iCFMxVscPVFTE7SNGsiUpJ6hb3p0ohWwZFJcaggGPtFG3SQjVeyfrez88le9qoQa1k2rDr7NdXvLtFYzYn-L88ViH497SA1AFPmXecsKldIwzalakgHre8O4WjC37P37QrIhyix9e9bZ9VDuKj65kWyWXzLVYok-FnfTGyGgQunj-cxDw6-8oEFitUjvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گل سوم پرسپولیس به ملوان توسط علی علیپور ۵۶
🔹
پرسپولیس ۳_۰ ملوان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/685381" target="_blank">📅 21:27 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685376">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RZMl1xtxyL2xcv2bd_sFvDmzON7GJNwACNXKNVdbq37bGageln2plwJhYNn6soRgdLmwMvv9vyNym3kjlxDvjtnJN_qDHT9ocdB4KPFlpbtxrAIfG1gzRCJ5Eqm1EE_0zM4MfZS-e9bFpeYshuneiIODfY7j4XJR3gbmGoup5bO_n6WB_nIkMBe1KRZWkNfyxetD_D0ENwMf6cZSy3PrawAk5mkfKYVW1Ao5O1q6UYhBXNJcAOxjdXtBeUUUJuQY3zDsWmKeI_IykN-k7kuxEqc4D2NCvOh_CuOcH7KyaB3nNVfbUzZNqwRnXbLILhtyI_9dUBePgL7XPbKOUkMCDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CLtvjI4PllOQ596NKKcgCKyZFmHtWRGOC6QF9-kcfoMVxdnNwvhKxdUEsLAtcqjDe8-sn2CyOuE41TCZNcczasbGZoRXkOzsu6e1GIuR4QR88XnTB0RizaM4jHwyFNcHxHSewXXVuZSfIEz5JUlwwPlAnJKLaf5zyrdk2jH44arb5Wd5Wie54iZQUAKsO5d6aFBU78IvTcimyHI_EA7EeQjqESoC9tNu1C3UVQ3Yuc4etePSHYeOrrNCtnP9b1WNmzYDOZD_kfjFqSteHnAtwwSg631AJlL981VBMi7DfsPDnPwsPBursj2RZimVx2PDKdx7bYEjCV7T9RvfgC_k9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
دیگه با کپ کات یا اینشات ویدیوها رو ادیت نکن، چون هوش مصنوعی واست اینکارو انجام می‌ده #هوش_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/685376" target="_blank">📅 21:05 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685374">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cHQ6RWuemk9tUlDgcpGaruaRruPlvPnTk6-qtbznUfXxOJZ4Qx5STpsdTY--4vRXLEeIBIugfx7SgJDrwnPnEVYagBDxRlTYt0ENCsXrMx6vwuhShbDzEtAK1vylEZ3zsSIxohFowVf3JwBWrmoNjvY1CmoCRbUvB5WpLuXkyh_wm7SOKNlMR0Tn6tyru8k9PF2tEwD9meNwJGmOXKjO_M-dGTa2w5v5yZLZFPdoDAIFH3d-jZ9r9KmPW75lZTltQz3MdBcw1NaP5KbhF7wTHWlrNrA_H0-YrYZtjT8JSEQl2I_hOpwzx8sOGcmelo8ovGSvR_uIR3A5UIZRcXFg-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
ایران قوی، ایران علمی
💠
اعطای بورسیه تحصیلی و صنعتی دانشگاه بين‌المللی امام رضا علیه‌السلام به داوطلبان سال ۱۴۰۵
🔹
ویژه داوطلبان کارشناسی ارشد مهندسی برق
🔹
ثبت نام تا تاریخ ۱۵ شهریورماه ۱۴۰۵
🔰
جهت کسب اطلاعات بیشتر در مورد شرایط و نحوه دریافت بورسیه با شماره‌های زیر تماس بگیرید
👇
☎️
05138041 داخلی‌های 1421 و 3108
🌐
imamreza.ac.ir
🆔
@publiciriu</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/685374" target="_blank">📅 21:02 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685372">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBimebazar</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VG-dgo1jKl3xYwjG7l5DhU51jTXUi-qCiTWdvz_qz8VCmp6HJwE46OyR5T2t-wMv8o1CFYIZi9mPl2p3ycoODdZnImhjvg_z-70bUX8mtzjz8eNSULvmXFclAs01SmOuI_pPd4CdqZLB2piRzNB6LFHZDd9rk-DgwGkjdyNPWy6DcskiK-KKbQ2Gf82oo8jnl0hEARdKl7sjW9EdQDYWmJU_EjZkTR1ghm8FlGqhiRbJXbjvnmpH-pVOnF6nAhYqZGB7IlN6A06yTfp-oiL6nLtxs0aNVA2NNr5pYmzeJvxv5kIJSK20fY9uqRIXY8v6zlPqnBIa8THA73Z4xPyEBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
بخشودگی ۱۰۰٪ جریمه بیمه شخص ثالث!
📢
طبق اعلام بیمه مرکزی،
از ۲ تا ۱۳ شهریور ۱۴۰۵
✅
تمام جرایم دیرکرد وسایل نقلیه فاقد بیمه، به‌طور کامل بخشیده می‌شود!
فقط کافیه در این بازه زمانی، بیمه‌تون رو تمدید کنید.
✔️
تا 2میلیون تومان تخفیف با کد
pnsc
👈
تمدید بیمه شخص ثالث
#بیمه_بازار
🟡
@bimebazarco</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/685372" target="_blank">📅 21:00 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685370">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/276adae82c.mp4?token=j46kau0oT3EXbrft7Favh5r-679BC_ebzRqFcQYtuYIhEQ74_GAoHSZx9HZwlkoYEwbuA086Rq6oGw9wOuqJAvqMz3OoBgYVXoBIn_sxI7shnZ8od34lUBL6elJufh99YCPpZDUlO_GixITq1rjlYpwmnUPLoEMq8X5X7u2DBpdrcCk2zjby6dkiZYXbHncyjPx2jFb7Xm47qCpCSmFWcxUuZj3QPoNFaeRRGSgoRlrvCabVs0goxE7LE3r-Z_D4qZlfI3eEM9Mnb3M-PIhmBDmSiRIPPFBvimIQp0cuWWqZ4O4aPXSeqxqwR40xFzdITQeAFBArb2pObf30R9JKiahB9EdxQ5Npc1jMl-kQUt_dXqMt1TRB6sr9lvRhBXd8xaZjKabbU7xhRoDbmcEoYV2NaX4hxejx9l2WGee0973l-DatZQRajDIHesCWoxMuKjF9KNbQZDejl91KKM_2rXW-0DMwhZUBY_PAizF0pvE_Iuw6QLlySvhMreMf7zrH4SyADkgFocPdokvSbcsMffgsMP28tVeFPin6OBcDXysH-Gqj6p7XGDeGr_8eTtzH8ootVs9mlI10zykZ17R1eRRdU0mXvhoFoEFt2YjNg0MesuKlBUs_T1IyiLG1ArhspIxAwPy115PcJodDE2KDudHB5Z455Wa7DM_3zbg7sVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/276adae82c.mp4?token=j46kau0oT3EXbrft7Favh5r-679BC_ebzRqFcQYtuYIhEQ74_GAoHSZx9HZwlkoYEwbuA086Rq6oGw9wOuqJAvqMz3OoBgYVXoBIn_sxI7shnZ8od34lUBL6elJufh99YCPpZDUlO_GixITq1rjlYpwmnUPLoEMq8X5X7u2DBpdrcCk2zjby6dkiZYXbHncyjPx2jFb7Xm47qCpCSmFWcxUuZj3QPoNFaeRRGSgoRlrvCabVs0goxE7LE3r-Z_D4qZlfI3eEM9Mnb3M-PIhmBDmSiRIPPFBvimIQp0cuWWqZ4O4aPXSeqxqwR40xFzdITQeAFBArb2pObf30R9JKiahB9EdxQ5Npc1jMl-kQUt_dXqMt1TRB6sr9lvRhBXd8xaZjKabbU7xhRoDbmcEoYV2NaX4hxejx9l2WGee0973l-DatZQRajDIHesCWoxMuKjF9KNbQZDejl91KKM_2rXW-0DMwhZUBY_PAizF0pvE_Iuw6QLlySvhMreMf7zrH4SyADkgFocPdokvSbcsMffgsMP28tVeFPin6OBcDXysH-Gqj6p7XGDeGr_8eTtzH8ootVs9mlI10zykZ17R1eRRdU0mXvhoFoEFt2YjNg0MesuKlBUs_T1IyiLG1ArhspIxAwPy115PcJodDE2KDudHB5Z455Wa7DM_3zbg7sVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وحدت؛ توصیهٔ رهبر شهید که رنگ عمل گرفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/685370" target="_blank">📅 20:57 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685369">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVFb4Ik943PXeBYb-WpK0v7ZPbENwk1loVRWNFSae-Zl215fehymGOeCEmfPUmO_AvUVVwTBphP1FoDyY9J0UA-oNBkK7gyrjMjrKu_X3Zi-gO2ffqQnLMegYQ4EcxYQaC8VIE0zR4hLItEcd6yKDUAWwZ4VhC_CMdMUucA4XFSn3hON_-EBHw5fAPXdODV9-T3QvG7wpktd1rDXTNul4XNSUssdZAPsaeC91fktqesHNHeQuEw-2kyFf4V5FkDdW6Qbk9Ml4JcaqCRBBJGDfaXh99jisnWKBxWROe7jg4rTQYrdchPGeVz4LvSr-KzPKRmJaMHvvJn6JEncXnDtmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری این‌بار از نزدیک با شماست
✨
🔹
بیست‌ونهمین نمایشگاه بین‌المللی الکامپ، فرصتی برای دیدار، گفت‌وگو و همراهی با تازه‌ترین جریان‌های فناوری و تجارت الکترونیک.
🔹
در غرفه خبرفوری منتظر حضورتان هستیم...
سالن ۶، غرفه ۳۲
۹ تا ۱۲ شهریور
ساعت ۸ تا ۱۵
نمایشگاه بین‌المللی تهران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/685369" target="_blank">📅 20:55 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685368">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ef114bf55.mp4?token=qDiIOysZWtfM3TyNxLfCAMzmM7QeEpoukCypE2zhke3dPbLqjMc2PLAzHB5Lyvezt4DGds3hVQiahjK6F8CmxR8wDQAUlS07C9C8YzqYIB6QiHu1E6OtWdxU0S3in_J2SedkF-k5_8S5ms6BgoUHLfCdDgsgK0g1YwbgGGX_U3P__Roq8ZQC4nOex9Kl-6Z8JRUs9_nN8409LKDKwRy1m67cvbnoqj7SLzvKln6AaOokoyLUzTyWGH_TMF6Sy3MsTBWnAOkWGfaSo-PdwQVqriKsnfVMVhYgVVIm0IgivEO82o3IdtLH2TNc8d9mi6i5qmhgyUigHgfnFgi7PA5Vaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ef114bf55.mp4?token=qDiIOysZWtfM3TyNxLfCAMzmM7QeEpoukCypE2zhke3dPbLqjMc2PLAzHB5Lyvezt4DGds3hVQiahjK6F8CmxR8wDQAUlS07C9C8YzqYIB6QiHu1E6OtWdxU0S3in_J2SedkF-k5_8S5ms6BgoUHLfCdDgsgK0g1YwbgGGX_U3P__Roq8ZQC4nOex9Kl-6Z8JRUs9_nN8409LKDKwRy1m67cvbnoqj7SLzvKln6AaOokoyLUzTyWGH_TMF6Sy3MsTBWnAOkWGfaSo-PdwQVqriKsnfVMVhYgVVIm0IgivEO82o3IdtLH2TNc8d9mi6i5qmhgyUigHgfnFgi7PA5Vaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ متوهم: حالا فقط یک اقیانوس کم دارم!
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/685368" target="_blank">📅 20:53 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685367">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e809ca549.mp4?token=DH3ptzF5SO4WT7AVHh7kDNkgrXfv53bLnqFgypWRaJAYAsPNuwWWcHMSZCYzZwPtE_mpZVJkAwyWu4PNl3oVHPenNukZUwZcwM9o5i1nJm1wnYELdC54Hm7oioj8Q1XjuTJKo7-jMm_DbT4AvCGA71Wrm3jD0j8_Xnhz5Xk_Puv1HZdTFaClB8jkZ_mdH-iOHJFWorcKxW7856U4pkVJrj8jRDDD2w6LQYlbKuv6jCN-HS9XJdA7FcnHtiify4r_lmnNx09WjGXro6Ho93K9DsTH-LTqesg2HIDY3akEEXx-Wuak4Ug_5QWePc0JEzToY3ZZHl451QxvoKbmzrLuF41shyP3yq8OpM4BVnBT998-qfMdJg8B9jCSa5HfR6esPTkDshXKJYUE4oybe2gsIHBqACURun0jkEo3tlgZxF8f5CPCJeTva6aFrQrJkDc3sewKCmWWByJX1h_IeIVlzvX2gPGD7h9XvJEtOp-cKwUBGB_Ru7rodxVL6afeYVl0m_9cj_mtQBJffv2_dy77UzyTdgY4iTEInLZloKJmbXdbo4T3cf6s7K4YstaGXIkuN7UV34EVx3Au-cf2e3002UVpUnnqLb6cK-lorseilBTXohDnNasgyCM8Kgu9Toath0jKXmDNGDzRm24CtAMg_-3i7oUjKFi-0rEb8LEI2PM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e809ca549.mp4?token=DH3ptzF5SO4WT7AVHh7kDNkgrXfv53bLnqFgypWRaJAYAsPNuwWWcHMSZCYzZwPtE_mpZVJkAwyWu4PNl3oVHPenNukZUwZcwM9o5i1nJm1wnYELdC54Hm7oioj8Q1XjuTJKo7-jMm_DbT4AvCGA71Wrm3jD0j8_Xnhz5Xk_Puv1HZdTFaClB8jkZ_mdH-iOHJFWorcKxW7856U4pkVJrj8jRDDD2w6LQYlbKuv6jCN-HS9XJdA7FcnHtiify4r_lmnNx09WjGXro6Ho93K9DsTH-LTqesg2HIDY3akEEXx-Wuak4Ug_5QWePc0JEzToY3ZZHl451QxvoKbmzrLuF41shyP3yq8OpM4BVnBT998-qfMdJg8B9jCSa5HfR6esPTkDshXKJYUE4oybe2gsIHBqACURun0jkEo3tlgZxF8f5CPCJeTva6aFrQrJkDc3sewKCmWWByJX1h_IeIVlzvX2gPGD7h9XvJEtOp-cKwUBGB_Ru7rodxVL6afeYVl0m_9cj_mtQBJffv2_dy77UzyTdgY4iTEInLZloKJmbXdbo4T3cf6s7K4YstaGXIkuN7UV34EVx3Au-cf2e3002UVpUnnqLb6cK-lorseilBTXohDnNasgyCM8Kgu9Toath0jKXmDNGDzRm24CtAMg_-3i7oUjKFi-0rEb8LEI2PM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل سوم پرسپولیس به ملوان توسط علی علیپور ۵۶
🔹
پرسپولیس ۳_۰ ملوان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/685367" target="_blank">📅 20:51 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685363">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80057e224b.mp4?token=XcCN9L7n8onutt5ZcrRDQqBjOS_8njLU0YdPA15-BPFJUY_d6hJCpbrvpXUyRMNgMGL4LjoOgVP2NFlGTMHADIVFJxdwDRwzW8Z4DmWVYErf8M9gTNSJx7s3s78QOfPQKmzFmKb7GHKip5-bHaVoxaj2sHoWs9legssXZ00lEB51WULbFNF0NPQsVSy4CXZ6M_jDNh-ZScg7eaM5gVxv0utZHJ4araMdylk54MRnBReCcB0ZYBTP3NusLlAGdhLNLy0V4jyUD2Mosx-BNXwB3tWq174DCQqBWvTgGrpQBtpBCVB6DTYEXDMKiJbrw6_VipGLJpPVTWOPzF6ahUyuGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80057e224b.mp4?token=XcCN9L7n8onutt5ZcrRDQqBjOS_8njLU0YdPA15-BPFJUY_d6hJCpbrvpXUyRMNgMGL4LjoOgVP2NFlGTMHADIVFJxdwDRwzW8Z4DmWVYErf8M9gTNSJx7s3s78QOfPQKmzFmKb7GHKip5-bHaVoxaj2sHoWs9legssXZ00lEB51WULbFNF0NPQsVSy4CXZ6M_jDNh-ZScg7eaM5gVxv0utZHJ4araMdylk54MRnBReCcB0ZYBTP3NusLlAGdhLNLy0V4jyUD2Mosx-BNXwB3tWq174DCQqBWvTgGrpQBtpBCVB6DTYEXDMKiJbrw6_VipGLJpPVTWOPzF6ahUyuGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم پرسپولیس به ملوان توسط تیوی بیفوما
🔹
پرسپولیس ۲ _ ۰ ملوان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/685363" target="_blank">📅 20:36 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685361">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
سازندهٔ چت‌جی‌پی‌تی شمشیر را برای ماسک از رو بست
رویترز:
🔹
اپن‌ای‌آی قصد دارد ارائه مدل‌های هوش مصنوعی خود به «کرسیِر»، ابزار برنامه‌نویسی مبتنی بر هوش مصنوعی که اکنون تحت مالکیت اسپیس‌ایکس قرار دارد، متوقف کند.
🔹
تصمیمی که بار دیگر اختلاف طولانی‌مدت میان ایلان ماسک و مدیران اپن‌ای‌آی را به کانون توجهات بازگردانده است.
🔹
این شرکت دلیل تصمیم خود را نگرانی دربارهٔ نحوهٔ استفادهٔ اسپیس‌ایکس از فناوری‌های اپن‌ای‌آی و تجربهٔ قبلی از نقض مفاد قرارداد توسط برخی شرکت‌های متعلق به ماسک عنوان کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/685361" target="_blank">📅 20:36 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685360">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53e66bb35c.mp4?token=k0BHE4gTO-VFH8B5pwglo7NBXazUSUa3k6Fq39Y_7AS2yP44zdZpf-fjN3HA9r0LrJzGA5oIgMiG1dv643UZd4Iv3snxHi7ertulJjOXjMiKa5soM0ljtZpntIXbKxYjSyMw6vPuk8gpI0XgbWSSFdjxmO2SsisYdkfai2HSG8eTXhRHetp5Zw-M6ZxvBulDLVECM_1CLY_cNDHtY9RcOYkOVB_rVqL2xOyq52UL2J3SVUaslOu4TEf-RY-gVnWV_HsskqBBm_lAYErbS_3zjUltepxRXbYL4ssZkjuL0m13flAUxiSVBXSJ_2Px7LFaF4pClWbLc8RjLdUpWDtkfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53e66bb35c.mp4?token=k0BHE4gTO-VFH8B5pwglo7NBXazUSUa3k6Fq39Y_7AS2yP44zdZpf-fjN3HA9r0LrJzGA5oIgMiG1dv643UZd4Iv3snxHi7ertulJjOXjMiKa5soM0ljtZpntIXbKxYjSyMw6vPuk8gpI0XgbWSSFdjxmO2SsisYdkfai2HSG8eTXhRHetp5Zw-M6ZxvBulDLVECM_1CLY_cNDHtY9RcOYkOVB_rVqL2xOyq52UL2J3SVUaslOu4TEf-RY-gVnWV_HsskqBBm_lAYErbS_3zjUltepxRXbYL4ssZkjuL0m13flAUxiSVBXSJ_2Px7LFaF4pClWbLc8RjLdUpWDtkfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر بالگرد چینی از سرچشمه سیلاب مرگبار در مرز چین و نپال
🔹
یک بالگرد چینی خود را به نقطه‌ای رساند که در آن یک یخچال طبیعی فروپاشیده و حجم عظیمی از آب آزاد شده بود.
🔹
این پدیده که به آن GLOF (سیلاب ناشی از طغیان دریاچه یخچالی) گفته می‌شود، یکی از خطرناک‌ترین…</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/685360" target="_blank">📅 20:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685359">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DTLeGbHucf1R0a4hAoU2qRdP7f3FeTzZCtX27qA8UfViTiIRH2HvZHzAsmEebA5wgI_SC-dAPbb3yx6Mo294Q4iPTuwf7YN8dBkJfNRYlvWH7y1LHL3XzYPyZ_l8u9IZOTG3AugQ5Dm9tRs_6pfYqBO9nT-Q7FqWsXDILcv1EXg72ZL27T4eUapINH5syyJ1qsOn7s8dkrhPbTqOCP4DjIFIaCW8LbMFpnCxVVJvAKj9_vge3gAw5Qbk1nBd6wnOrI1rIP_tVY2iGPf4S5K3uporoRF0V0scbYnfXlX_dfHJcrtCPIVQbvAOZbWIUxYB6EEB48AE2GlsKL4KZMoo8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روغن، رکورددار تورم نقطه به نقطه مرداد ماه ۱۴۰۵
🔸
بررسی آمارهای تورم نقطه به نقطه کشور در مرداد ۱۴۰۵ نشان می‌دهد که اقلام خوراکی و پروتئینی بیشترین جهش قیمت را نسبت به سال قبل تجربه کرده‌اند.
🔸
در این میان، گروه «روغن‌ها و چربی‌ها» با ثبت تورم ۲۵۸.۲ درصدی در صدر رکوردداران گرانی قرار گرفته و بیشترین فشار قیمتی را به سفره خانوارها وارد کرده است.
🔸
پس از آن، گروه «شیر، پنیر و تخم‌مرغ» با ۱۶۳.۷ درصد و «دخانیات» با ۱۶۰.۹ درصد در رتبه‌های بعدی بیشترین افزایش قیمت جای دارند.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/685359" target="_blank">📅 20:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685357">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc5cd16df0.mp4?token=NtkN2OPhK0j2YhfPCQeCDkewAD5XKhrYE08IKuPlNhoh3dr6oJ71_i3uePEWG6B5xU_MQEcnqcolJEuuv_QOpSd6dnn6ttG62-vv5a25OGvaARCFZ-_YTQgm3A2no7JnLqlvHN2Yj59y7tisW4QFIlE-u-_IGJLpyyihoFIHRDqOgleOUuq2JjE0vwl0VVOuXanOSyn4yB6IXGP81BR8r1hjfGhrKUTqluof04XNseO_TMk2Jyb9eBQMOk-N6vsZtoE4pomrB0WmxG-kwm-7rvf3FJa4Ek1hbVItLEzgI8PJ4G3gr6UtfX9byK0Zrt0riWaFDN3xXKtkndcUYFaPwJUGmCSyLX5wnGeHYtIx2voVK0fxy_l9RTdkjWgKHCnneCGJc6wT192bzmLD6Roa5XJXepKtjn7sjdAC2ekbQU623nmhiSb6qXWwIZsXcITsNIHcLxrWjGmMiP-FIwKvLoYBxPVRd7SM8ahuw3nHTLcyWYrMgW0Wl_VGNaEoBVPKkXYNYr2PZm1-smAc6B_g5LNAOJzybV7Dsw5pU4UtYZoO0zsqNvfF3UsKXKTXtSXtSEK6mD55g8G8_rAhongC7fuZ9T2rotKidGLrrOoUckao7jJXQKWIvLbm526zGCf42o4SsgztlSvpEe-tjC5OsmfJ9uyyg2oa8S4FDHjxQdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc5cd16df0.mp4?token=NtkN2OPhK0j2YhfPCQeCDkewAD5XKhrYE08IKuPlNhoh3dr6oJ71_i3uePEWG6B5xU_MQEcnqcolJEuuv_QOpSd6dnn6ttG62-vv5a25OGvaARCFZ-_YTQgm3A2no7JnLqlvHN2Yj59y7tisW4QFIlE-u-_IGJLpyyihoFIHRDqOgleOUuq2JjE0vwl0VVOuXanOSyn4yB6IXGP81BR8r1hjfGhrKUTqluof04XNseO_TMk2Jyb9eBQMOk-N6vsZtoE4pomrB0WmxG-kwm-7rvf3FJa4Ek1hbVItLEzgI8PJ4G3gr6UtfX9byK0Zrt0riWaFDN3xXKtkndcUYFaPwJUGmCSyLX5wnGeHYtIx2voVK0fxy_l9RTdkjWgKHCnneCGJc6wT192bzmLD6Roa5XJXepKtjn7sjdAC2ekbQU623nmhiSb6qXWwIZsXcITsNIHcLxrWjGmMiP-FIwKvLoYBxPVRd7SM8ahuw3nHTLcyWYrMgW0Wl_VGNaEoBVPKkXYNYr2PZm1-smAc6B_g5LNAOJzybV7Dsw5pU4UtYZoO0zsqNvfF3UsKXKTXtSXtSEK6mD55g8G8_rAhongC7fuZ9T2rotKidGLrrOoUckao7jJXQKWIvLbm526zGCf42o4SsgztlSvpEe-tjC5OsmfJ9uyyg2oa8S4FDHjxQdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسن روحانی: رهبر شهید بارها نگذاشتند جنگ شود/ در سال‌های ۶۹، ۷۷، ۷۸، ۸۲، ۹۲ و ۹۸ تا مرز جنگ پیش رفتیم و عبور کردیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/685357" target="_blank">📅 20:24 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685356">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2LR9xCmgNVPUREZC2Ai0WaAoq2rEZNoEtPgMwDM-LLTR0iPXBIaOhyAn5LM5HzQ1Y1dYbfa5kbaXG9bUv_MoUDdeN8c7lEF1snRoFfGmoJDRS08m14QQ1On9pb_5LnbkRdDpq5nBA-BWh37OeDCXi3YlukO0ohmNT5uWQopcGfLOSSVd1gjPWtF1RNSdBYQBTY5Z9QdjmiI9G5ymByYipDx2EH0EtIe5RLbPnJjt-d_UOVdvt73txiluaYZVM-pAoNmuz8jaioHCWk02qpV2ador1Git5cKkvfhOjRThWT5KcaIUNTwCuxC16G4GQMrx-WQw3zCLgttgeqCqNNOnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ خواستار تغییر مدیریت و مجریان CNN شد؛ به‌جز مجری‌ای که از او تمجید کرد
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/685356" target="_blank">📅 20:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685354">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39cdccc011.mp4?token=TW5b7VmTUXgi6YJqvBn-P5J-v-0R-EpRBrFGAhUzNsfgZ2wuckvcteOJ9z9ii4zeYVJiszAvNliwfD2YOPta8MKnO11IgOwNLuHRjSFra96mF28oOa-PLBZkZePnCWaFOopcDnHY-3ZVFs5MCau3CxpOL7AqiFfupXgrPT_Yw9Mbsg0d7gUFjDuYGFQh9IE57V46WRE-ZBrOXeGDMX7ex5W4eFOFdCXPREDkX9WvuRkjLMzod-zW9PBK5hvFOLWvo4Q_mgJj6HQByYgMoEN02AHGr3cxRpCqUfRzWiJIODuHGDMCmZB6_D5nJpLiJzutQrTjAehQ2Rx81_IGoYy8Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39cdccc011.mp4?token=TW5b7VmTUXgi6YJqvBn-P5J-v-0R-EpRBrFGAhUzNsfgZ2wuckvcteOJ9z9ii4zeYVJiszAvNliwfD2YOPta8MKnO11IgOwNLuHRjSFra96mF28oOa-PLBZkZePnCWaFOopcDnHY-3ZVFs5MCau3CxpOL7AqiFfupXgrPT_Yw9Mbsg0d7gUFjDuYGFQh9IE57V46WRE-ZBrOXeGDMX7ex5W4eFOFdCXPREDkX9WvuRkjLMzod-zW9PBK5hvFOLWvo4Q_mgJj6HQByYgMoEN02AHGr3cxRpCqUfRzWiJIODuHGDMCmZB6_D5nJpLiJzutQrTjAehQ2Rx81_IGoYy8Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آپدیت جدید تلگرام ویرایشگر متن پیشرفته
🔹
کاربران پریمیوم حالا می‌توانند متن‌های طولانی را با ده‌ها ابزار قالب‌بندی و کمک هوش مصنوعی، حرفه‌ای‌تر ایجاد و ویرایش کنند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/685354" target="_blank">📅 20:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685353">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">07-2 Ane Manaee (1403-09-01) Marghade Sheikh Sadoogh</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/685353" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه هفتم؛ بخش دوم
حجت‌الاسلام امینی‌خواه:
🔹
زنگار دل، قصه‌ای از چرک اعمال [00:50]
🔹
وقتی قرآن هم بر دل اثر نمی‌کند [5:37]
🔹
از ترک عمل تا خروج از ایمان، فاصله‌ای کوتاه [6:38]
🔹
آنجا که زکات و انفاق، آزمون بندگی است [10:05]
🔹
حج‌گریز در شب اول قبر: انتخاب بین یهودی یا مسیحی [12:30]
🔹
بخیلان کافر؛ فراموشی فضل الهی و وظایف بندگی [15:17]
🔹
حسادت؛ زمزمه‌ای از کفر و جنگ با خدا [17:23]
🔹
رجب‌علی خیاط؛ مردی که با فرار از گناه، چشم دلش گشوده شد [19:55]
🔹
انفاق؛ آزمون سخاوت یا سقوط به کفر؟ [21:31]
🔹
عیب‌جویی و فضاحت‌طلبی؛ قدمی به سوی ظلمت کفر [23:50]
🔹
احوالات حضرت زهرا (سلام‌الله‌علیها)؛ تصویری از باور عمیق قیامت [27:34]
🔹
محشر حضرت زهرا (سلام‌الله‌علیها) در صحنه قیامت؛ هفتاد هزار ملک، عود، و پرچم‌های تسبیح [30:18]
🔹
قیامت در التهاب؛ روشن شدن آتش جهنم به خون‌خواهی فرزندان حضرت زهرا (سلام‌الله‌علیها) [37:27]
🔹
محشر در حسرت: ای کاش ما هم فاطمی بودیم! [41:44]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/685353" target="_blank">📅 20:08 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685352">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tURStc0mxS0RZ1aeG_3SeWdrlv1wWOISRBeRnseIYzUNI13xmu5Ltgbur7tmKfflkwjgrN0RWOoEUjUWt7UHbW7nsrlFaaiO2ZLqffsfJmEiA0UnRDvaY2F6yvXtrHuH70C4eVg-MT93oxU02NY_1_jqBH73sOLjX6110UEDJhsYJBHZvKLH38iBDsMvstL3BTBDBnF-meWb7XzmVpad-PLcddN6V5XHR9u1MO7n0d38XHyUj-Lsr6SNvbIuuJaooo7oTWdVspvWcAV2TkJmKlJHJ1M2cvtn875NVaE9UogrVPLKzWBF5lxjmEB8WdBi707G9cTosAQ5EBOFMsq3Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چند تا ترفند که روزی به کارت میاد #ترفند_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/685352" target="_blank">📅 20:00 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685351">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eob_HCvC0-la2h7tWWpEyo4_CZtSWPkKvHQKdvoIgkuUFq4sLlRtbKo3kYVTuPLr5lIobLQFipoln7ibdRYCvYo8pjpZLH6Zh6qxo8DxZ5Vi9bKj749oWtkDie_JTY9T0kWIT8ZrnjGHD19v7NjC5unEe0o_tGeac1b75BPNUaQmDInvPl6SjQYlSs8zLZIVf5a_7jvRSBedCz3RJw1ejrbBtUvMQwZudZBOSJIq3Re8MPrJPbfrZCd4K-6QHU9IXYF64DeaIgYu6AHDgSefh56NC-VsJO2hE2WVsKa4Amv63OgYiLr35DCq6fih0DgYdgHvmE73-3ECq-7RIXe7Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⬇️
به مناسبت هفتاد و پنجمین سال آغاز فعالیت بانک صادرات ایران
🔵
اهدای جوایز ارزنده به کاربران سپینوی بانک صادرات ایران با برگزاری کمپین «۷۵ ساعت تا ۷۵ سالگی»
🎁
بانک صادرات ایران همزمان با فرارسیدن هفتاد و پنجمین سال فعالیت خود، جشنواره «۷۵ ساعت تا ۷۵ سالگی» را در نئوبانک سپینو برگزار می‌کند. کاربران می‌توانند با شرکت در این رویداد ویژه، یکی از ۷۵ برنده جایزه نقدی ۷۵ میلیون تومانی باشند.
🌐
برای مطالعه متن کامل خبر، لطفا کلیک فرمایید
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331
#سپینو
#جشنواره
#جوایز_ارزنده
#اخبار_سایت
#بانک_صادرات
#بانک_صادرات_ایران</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/685351" target="_blank">📅 19:59 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685349">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8aac8cd06.mp4?token=TkiE5BEJ9gk334T0FowCaEIYKpEF0WSKtwWmAYlbXpHGM2lEIjDpcyh8c5xkxJowMIRzedcA6ZelHyV6zhhlXYRAnN-jp7rX6sDgMWVgISq8kNqX7-hN8lQnrrZt_HXds_YjEX2Xs8Uu5Cw_TO439ATURVwt7KUfgoDQyEjTJhkN0ObpZC573cybC2Ltu-4pSJKNvtBeBZkm6l9YG4maY8UyyhOheP1ElA9gcFwXk2jZszq8nYtj7O2-bFa0tNPTEgKCsOW97hZaS8_z_XSJx2VypAm677USBry1BL5c9ptwEJMQ0O0YhTgaFueWXGyQbAKwmb9-IjK_cEPBe_WIsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8aac8cd06.mp4?token=TkiE5BEJ9gk334T0FowCaEIYKpEF0WSKtwWmAYlbXpHGM2lEIjDpcyh8c5xkxJowMIRzedcA6ZelHyV6zhhlXYRAnN-jp7rX6sDgMWVgISq8kNqX7-hN8lQnrrZt_HXds_YjEX2Xs8Uu5Cw_TO439ATURVwt7KUfgoDQyEjTJhkN0ObpZC573cybC2Ltu-4pSJKNvtBeBZkm6l9YG4maY8UyyhOheP1ElA9gcFwXk2jZszq8nYtj7O2-bFa0tNPTEgKCsOW97hZaS8_z_XSJx2VypAm677USBry1BL5c9ptwEJMQ0O0YhTgaFueWXGyQbAKwmb9-IjK_cEPBe_WIsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوشحالی والیبالیست‌های نوجوان ایران بعد از قهرمانی در جهان
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/685349" target="_blank">📅 19:57 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685347">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d17b66253f.mp4?token=eBWuehNxN23GdhsMhNbDA8nuZUf0KjE1AnGzhMVIeUeeChq7iLDswx_POTgfeNkKybWmPkJhoB6kE3uaaEv0QaJG9Ni4vbWXhOYC3ehuvHD8xwRaveJ4dG8B_odmmWrpyqMV_nmuJq49TZqENks3dQOqPoEwaAR6JOR_E3J_Pc7pdBBMSffYAcnpAvwS5691Vs5e3duERqz1ri54kFck7hCUikLZ40SiboigSRJB6C8uRppgfBmrto3aewzCaWcDtLOBTYFcc_02IY4uzrY0jAntz9AfNAsJ3TbihAQD3TRT-q-ji9w8fknIOA_AAQxXerFci-MNcvAPdProbWaq7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d17b66253f.mp4?token=eBWuehNxN23GdhsMhNbDA8nuZUf0KjE1AnGzhMVIeUeeChq7iLDswx_POTgfeNkKybWmPkJhoB6kE3uaaEv0QaJG9Ni4vbWXhOYC3ehuvHD8xwRaveJ4dG8B_odmmWrpyqMV_nmuJq49TZqENks3dQOqPoEwaAR6JOR_E3J_Pc7pdBBMSffYAcnpAvwS5691Vs5e3duERqz1ri54kFck7hCUikLZ40SiboigSRJB6C8uRppgfBmrto3aewzCaWcDtLOBTYFcc_02IY4uzrY0jAntz9AfNAsJ3TbihAQD3TRT-q-ji9w8fknIOA_AAQxXerFci-MNcvAPdProbWaq7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول پرسپولیس به ملوان
🔹
پرسپولیس ۱ _ ۰ ملوان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/685347" target="_blank">📅 19:53 · 07 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
