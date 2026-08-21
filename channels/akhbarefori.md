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
<img src="https://cdn4.telesco.pe/file/ifTA3EiV27UZq8zQLvkvwN_B6JfnNmcpm9BqRhbCQk263Kg817kKbsaVE_zuGZxLTxPz5W9e9xQVG9xNn3_bYYk_kItSCjYsuYcMdEc0g2Q5n6jS78zjsLW0Fv7IXaaXCEXcrYre5qyWPrGcWxQkYJQ5Qjoi8xAJs_Ony4DE_CPiNtmq0pb6RR9j1ceQxG-5m5-CS1KHcUt-MDWIHQ7pOsfWgHyM7nEWl3UwmYV290nQuREmorGJTUxMT2sIGbDHIPzZKooqRvVw-s6XCOBnhUm5brmVZtc7ZoOXr7QSd3Wk8W4BOEJ8wQH6ZKPTjDj33hvEih3Q_DvRagMA_ll5fw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.02M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-30 16:55:57</div>
<hr>

<div class="tg-post" id="msg-683089">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سخنگوی دولت: درباره قیمت‌های جدید بنزین هنوز تصمیم نهایی اتخاذ نشده است.
🔹
وزارت دفاع چین: چین و امارات رزمایش مشترک هوایی برگزار می‌کنند.
🔹
دیپلمات عمانی: تهدیدات ترامپ علیه عمان کم‌کم برای ما تکراری شده.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/akhbarefori/683089" target="_blank">📅 16:51 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683088">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/169c3f70d5.mp4?token=STlXg9MRl8GY6F35kARJvYmVuiBv4LwZdL5nUcfZZqZ7xcWNuGD8E7Jq-ZV7ECIKP4riJAcV0PISM-Oa0u8fTFmPV-ylGG5W2XwVZpUPAiIZZQAUqN-jSRFWXaWsEltjVFeZ8D_nmYhkiueonnnpjZLP-CVQM8n8ocJXqIOjjQqL2QsCyg42PInBWUd_wqv1TIlUcOYzoyNTzqFRJrTFNRhPxywWaoXs27U2MJMXzKs9MAZPk2a3NqW2fUeUsApvS3DCi9WlhQnQyCidLcmxMaZbz59h8pj8QjoAYA8kVPANFCFJrLIKyRGLnEVLHVmogXa634ks5Jz1KJq3ZlpFYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/169c3f70d5.mp4?token=STlXg9MRl8GY6F35kARJvYmVuiBv4LwZdL5nUcfZZqZ7xcWNuGD8E7Jq-ZV7ECIKP4riJAcV0PISM-Oa0u8fTFmPV-ylGG5W2XwVZpUPAiIZZQAUqN-jSRFWXaWsEltjVFeZ8D_nmYhkiueonnnpjZLP-CVQM8n8ocJXqIOjjQqL2QsCyg42PInBWUd_wqv1TIlUcOYzoyNTzqFRJrTFNRhPxywWaoXs27U2MJMXzKs9MAZPk2a3NqW2fUeUsApvS3DCi9WlhQnQyCidLcmxMaZbz59h8pj8QjoAYA8kVPANFCFJrLIKyRGLnEVLHVmogXa634ks5Jz1KJq3ZlpFYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماجرای خالی فروشی پلتفرم طلا چه بود؟
خالقی معاون پلیس فتا:
🔹
صحبت‌های من در مورد پلتفرم‌های طلا ناقص در رسانه‌ها منعکس شد. پلتفرمی که ۲۰۰ هزارکاربر داشت به مردم خالی فروشی نکرده بود و به میزان طلاهای فروخته شده نزد بانک کارگشایی طلای ذخیره شده داشت.
🔹
مشکل تعهد این پلتفرم به شبکه همکارانش در بازار سنتی بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/akhbarefori/683088" target="_blank">📅 16:49 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683086">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
آمریکا یک پهپاد ریپر خود را منهدم کرد
🔹
واشنگتن یک پهپاد ۲۳ میلیون دلاری ریپر را پس از فرود سخت در منطقه عملیاتی سنتکام روی زمین منهدم کرد تا از افتادن تجهیزات حساس آن به دست دشمن جلوگیری کنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/akhbarefori/683086" target="_blank">📅 16:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683076">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AiYajdd_JNpPUJFnfkyBTXseKIqTbTRBDe65hrBAAsU-xzjSqq6402sTFt0vPXL5SXB35Pm5UjAPn37wFHMrsNQdvwD93ImqIb5eYx1XCwiQ406Ysujp2Hbl6ujv73BP3i4OVvCUIRPorOKTp5G4jO6JnnvyhUKIzQn2q99QaYlkq0BuEQJBD1D30l54aJ5Ouz6bTBF8ac5MZlFL3CKFxmtBI8E7PRrKQWavKhQqjV1syS9KyRO5R4IKRmeSeJ5p3CilHtIBbZ2g4sMSjBuP0xFOH7vqPvtxAR3is0hMqC8jyaYdtKnhdLjZbJCaNNu8rWfi0yPtICVxF9s2k_qqAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oC_DaWYIWEi6tj3xr_SREQAiTJAbpSVmJggeNHRHWtNOYW7MOLhE8X2yOcnzUIeEH2yb0SyrZ6DThlw4kL3-TG7uxf3LG5TRV_AG1qa2CajxKsVjtRG2hrITLcgTBP9tunpad4R38ez4LPTndxE3ZG8RIbZbvXUAdV9bYZJDC9d1HqIpw4yoDMwC0NxS9onlPy3I7zQquAXRYML_C5c3f8Q0qiiJ_u1RLLkC3BFH2La3Ino1LyEo6_yTTfdiWxfXsletCZfngBLwOSlz5AJYxnugVHxzPQ3FHDNvOMDgPTlBjWmt-rtlcHuUPdj_oR0GE1BrHTDm_3sY4owJK74IwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oBRK5Ow0VxuAowFE5HmSNpGQcUQVX04hfadeh039pPwqCR1yqpZuQDXUKMPJMA7P8RdI2OE3_BdGTXAn__QTM_FRuSyDGvlZEH_CI092AXVlOiE89FZEISulGK3EKjYa3t2ENLVUFwlerS8O86tf2tccocFQuWAeYuD3zDyZFzlNUgjadUXuhrh9ehQBD48AlkeqzLbI88n03jWPemkmmw45u8J6TTdsUGXYVcfTx-C_WOdX9I8LgqYSrKtzUxYjbT_08pIOrpYn3l61lqteNXKHuwre0pcsB3fdGSSESV5Y189WVbxQ3qwJuqtQbjGT2H4W-sKcPs7Spain8XF7Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nixVxYqkIL_07cXllQ-Y6pfePwWQAWHWSoJscu3DzE7ZZCrMbVdzphXWuj496rW2lVfvmQmCjYxjZLYeZYtUzdJJqDf40uBcIvjOOsrStOpoGrkmYtwINmmrRpEIkrHyeRj-8QgrgHOraKOHscRPymg7-T-1ul14-YirGXyB5Db9ycsGUrERkEwcoclnZT1XheDWD1se12K_mJDM5Z7uo6E6uQbmOF2ek0QXzQx3CjRAUh2jJTPi0T0YdTVEw3_5_pJoEn3u6acgd8KbdI9khLcPrrBHh5XEHLzo_M95MP-8VWKqkVcDnz1GgwI-yVKmo6UPN7PCEFfToBwlPiMnHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gV1rI3sgQ2eldB1XagNFdYLuWT1pusZwUoD3hbZgJbfnqDWjjiaUkTcQolIkRN34Ig0NmblTVHlgb-Jz_EpZHH9MWciV0-MowMdG1OmEpL-ic9Lcsi1fy24C1Gz-IfynjrK7S9EX_4vlcBftH2DkyMakQ6KUzY0aSnVyG-xmuvjCp-bVImFuILZuostJesecjiMSOvkNUZLKNS99kaWLx-1db3l7kvUQKmoooDa1lbzJUsyLTwNuYJJUnLWSieVe4gX_zhB1_GAO1HCdb0iZvCTzM4hhKLp7HtUSYD7tPfYEMIrIUiRxn051W4c7QdJeBt-FY9AqI5auFGQiUK0JvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bm6giIlIkXeVH2251isyrLJAAq4VrHnQozDx-NtGeQOXTAk2ET7z1YqaahhPT2gk6RXJN2f4aiCN3ItZFS8lfpv4BoQglGv7HRm03Phdie5BHHgjWGxaJnvmiC-paMa67kWSQLbA4P1SzLHkjHkFrSUHwL7oz8EWy1sbu8eSsShWYsNVgqoWHhLSTW0gkjU4tNjV1JirvET26Fo6RhHboPCralKFCTCZI2S5V2Owf5OPad6Mtrv_HIo5X9cCjkabEg8nK3EamkJiqRC5wRNVMIGQV1iUbn5wd0iMo9MKViyepzY7uI7TpF6JQDhIFl8N3aL76_vg08NIBPouCGwxzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/svSCqQp72NrKIi7j6ss8Ha9LzauLR2xe7aMM6O73bh_TalTzYgkcut28lmzppVUgBfuBjXq0WbJd8xreXhCKwcosU6C-y7Iz__fBLUrtSCAe3Y5DKRMd0SQ34KTBNsQq9Mo0-MLCy1c9STkeNcOmpzOb2g57xOxxiqVUQH8qeHZzLSuRxV1mT9gjmMisYTOF5ny0ZfmbONK75Oy59rxPyl5WENyIzZ7pMr5xhs7Slr0i7DD2Ciz1FytFNcWPcGixkYKm8QLRuI8dGh5_2zVcH2rnoaK0sfHZwjA_Y2clXnhpLDY32fsFEwSSHhdInC7Fu5nAVzHQ6S5XKk_JrqbS3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LBLy1NPjtKM62NTmS-E_N5X3QTOClts6Lnxs-fMIZJV8Y6wuvZJUnKhQh7sS-Sid_x7OgPYpRsI-1jXNNS9dTNLk9t8njZNso4ILARehIYbAOYKnPzvTLP48eV_FwSB_0SZ4X_c6tg-X-6NyYQHeMLkAJamjgwdhPkADeWLxCvLEF_SJBfH9ZsQRMkHRKafy-h5FsnBdvJMLrOgx_2tjUbHlmiM4fScHphpsXYpVVC5iwi26wTQGA8CPEcSacwaCBtZ6Po7mzONKNVxzXdM4qOVTEQF0ziH2-CHbYDIzAHDl8CmXBhDNTEWjP-0NzVyqShliN0tQtATEi6O7XhmLYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m0dLQd2tWdO9k4LNdugG5s2ANc7C7ZJ1_EQsjA-Rb3SM_JNrFpkbpM1M1TgoijI_95nnQPU2Y9hwqYuNzf56AYWdTBiQXzrteqe1pPtK7Sr2YzPeKeGFUAW2Ibi9kY7lnEnwMv23s8MPXwySCZH1qSRJy9Eju-3zlWWdT2s_MGtkOSKEZyVmijrA0kwbznXhsCujLUznm8snwYApG8oE1luWaWa44-SoifY0dUrBsPTZjbiRvftSTO2pWuY0YxMSsGujbIEFC7XfmrHJLVq5ZPdlm15AUt_y0GbWB68WLMPhAUW9tWBcjZxdBxiF2Prk7CER-7Cp8r9Vys5mxrjVoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Po_ZyPkytzQvC8qjn26BhuXDE-CwSLfh_LmGZHMPIz5BUYlzI8ZtxVrDnjcQLt-lKGPlxwdc6-We8vZbbX412LJY3xXeIxxuoIxn1tgvhfmQahNVEk5qxFqMYLTRWy7febmVdmzzyW7qi7lXZYevf3D-NjqyDCqaJ9xPHdGdjZ3b0DdbcATVpocj1ruKm2fXpbLoQ_cgMday6G18xR6Q2jhvWF9aL51Vffn2tiEGPozY2XdJ3OQRB9jXZvGyZWZybR3awqEr5Wdi1jmRJPR9x4yEju2gUpWKS3Agm_CHTz3RYhtKfKsNVRDkLNP2C3uK4BvLoupxGuj6znLgVqIyog.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نیروهای مسلح یمن بیانیه مهمی صادر می‌کند  «سرتیپ یحیی سریع» سخنگوی نیروهای مسلح یمن:
🔹
نیروهای مسلح این کشور ساعت ۱۶:۰۰ به وقت صنعا (۱۶:۳۰به وقت تهران) بیانیه مهمی درباره هدف قرار گرفتن مزدوران عربستان سعودی با پهپاد «رجوم» صادر می‌کند.
📲
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/akhbarefori/683076" target="_blank">📅 16:34 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683075">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
نیروهای مسلح یمن بیانیه مهمی صادر می‌کند
«سرتیپ یحیی سریع» سخنگوی نیروهای مسلح یمن:
🔹
نیروهای مسلح این کشور ساعت ۱۶:۰۰ به وقت صنعا (۱۶:۳۰به وقت تهران) بیانیه مهمی درباره هدف قرار گرفتن مزدوران عربستان سعودی با پهپاد «رجوم» صادر می‌کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/683075" target="_blank">📅 16:17 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683071">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/axA04BHLYexMTejd4dTGrJn4sPWnssnSWv4AVkxHpWInf1ckC8aDPNsitpPuezKEwiTzf76ys_TAo_LOlBRW4RyS1e2ZsGrB_BI-xhohrEv1mfpLCk5VuOJl4G2ExL3lS_tOnS0w6lHS5_VLVybK7_2HEcOumhp3wX2XLyFRQ7KLPEeZPptfj5YIT-ePiRqXyBbR6K4gUVbv9gZAvcQrNfhx5KbhSEfC4DE74t-nTyY1ER82QKgGC1_Bjz1Dlp02iDFcX-oXhPABSMuK2yuXbcJIzg5bsqQ4punKRZIqncHdmM7wDE7QNU3zbyebk6oR1odqk8siEcyoV3ZGfpcODQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GuuO1ftqxVIdHuEvio-R8aQlAV4yXiiMe6KFDzU4izIT-zs2zfvumIAScwfW54zk3fHqgWf_wH50VlyoBIovWKKmmjJsaz2Xbo8wc0YUGiUXCdq-TKQ6JO1TqzEJ48zgD3tQ2C4oJ558Ih-d5IGBV2UJz15ENAgK7J5Kv2yf2GXmems2W8UfbLOdftSQVIH-0Zb0VbLC43t_kg4YYivtmidVzafJFuBNTrWyy6sjpIlrVeGu6kAW49U2qkb8EoW9g7MPImdjpI-_UEQmKAKzDUOHr7-YAHtxsPfTvD1FaeX9CZHaKY0r8A4BaiCbIy3QOHOhX1osnsDeFspisdaTOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dJ_xlJuDtmWfr2AavIBMFEEzRBilROU14V8aesozlLUZjJhxdIFJVwIOdtH3AkL-wMiBm9ms0rOVexnlpe_ZjrU1a8yjDEqId3CWNBkFVhSF6jmWtzwOOsXkXlfg7hDyoXlhUGfNB3cPR2zLfRPsgA72QY5HyzoEdYbY7Ti4pdVyGCW7vQ_09LiZjbqR6ed_OK9xKrAOVcLekmLP4PkY21ykof13sN9qzVZYbsOhVbD86OXTe1VVItEIJd45jx9J5CxM_vh75JHJCesTEO63aMHd-XtSoW3RIiAvcr63Py39ayLA10NGpkIXz6QV0s7C-VRaMoeCPRBestfqu1Xj1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BI4pAjkOb9SBNHmy1lsb_qAwx0s-WzN06JUUZTlHGQb_7TMBL7k8Yf3x-9vFgAFp3sMOFiTd9WpWW95mi3ve9N2rGdZ62rJB8NSbid6zP9Og1y9iE7UwyAtCmlLDzkW3Bn5MUNzWtQ8lzaDzoZP_dSUMujIsBlRTFGoHBpB3vr8F8G4pOubyu9VO3Sd47XOromoMANa3nTA3a_T5UxSkij3cbhkFsA6365B5vHJiWjSPXHJQGqSpdtndTliwJT183W1BilkC90Q1OSRNlvbRzaSFUXypDjCFCPeliFK2FU5YOgq7jTBRoSwWFiqMKFk4xwNCNIS0UNj0EZpZApYdXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
صندل عجیب شنل در فرش قرمز جنجال‌ساز شد
🔹
مارگارت کوالی در مراسم فیلم «The Dog Stars» در لندن، لباس مشکی ساده‌ای را با صندل‌های «Barefoot Sandals» از شنل ترکیب کرد؛ کفش‌هایی با طراحی متفاوت که ظاهر پا را شبیه حالت پابرهنه نشان می‌دهند.
🔹
انتخاب غیرمعمول کوالی توجه‌ها را به خود جلب کرد و بار دیگر بحث درباره مرز میان جسارت و انتخاب‌های عجیب در دنیای مد را داغ کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/683071" target="_blank">📅 16:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683070">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7e5c725d4.mp4?token=TD3vNKByoGNl92cgyUA09ES5b5eJzfFXAy10u-T_F92m7UzZW_KJZxrL6FOEwvQhChAP3jUl1ZmLlv8bwWyFMNShL3OxlZV_6AXI941exCfM7zn8GrIQfBdoHZNoXKFxccdfzRV4xky83a1tswJ9yihr6A45F1BkayQP75wfMip59QcR37wFIGz5sD_SIWEbmIuv1fG3Zh2lthmlxZREqtCKmNVkQaoUKQ1AWmkedUyT3AY-9zjZOZTE_8-etOF29hB-8_JhLPwTcm4nT1XmbZIzIVLVtOHQON6n-g1D3qPQN7RjowTnKmLenJV9Ft_1mfpdtXlZCe8TZtu8FKMIOiZAZSfcQ5sU369Nqnn9uI_ZyRY2X4eKc4fPu_Jvtc1xI88h98Wt1iZbBgdTuWWKqZ4dwxoRd1MfJE5F61JZUPzRUOQLC2i4O5LRX-50E-vA_1m9NUAh5qP76A5yDS4nJkBiyP26XeMtXf1edcBizAupyGd60J1BIc1ZH0YPd7-puomX_1SA68hw4t3aqu1upFJzE_0C-6BwDU8wx4LS-J3bpIXXTjePxtgmLu4p2aM4NTjb6JmPnAW_k9SfxZC0fU0foDmD3m5ZFqb_bDxcWg2wjqqd4e2eowQAdetruKTVsp4vZ0dcLKXemY3wTn5MNk6XRcPwkUJkaoNOFKGt4LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7e5c725d4.mp4?token=TD3vNKByoGNl92cgyUA09ES5b5eJzfFXAy10u-T_F92m7UzZW_KJZxrL6FOEwvQhChAP3jUl1ZmLlv8bwWyFMNShL3OxlZV_6AXI941exCfM7zn8GrIQfBdoHZNoXKFxccdfzRV4xky83a1tswJ9yihr6A45F1BkayQP75wfMip59QcR37wFIGz5sD_SIWEbmIuv1fG3Zh2lthmlxZREqtCKmNVkQaoUKQ1AWmkedUyT3AY-9zjZOZTE_8-etOF29hB-8_JhLPwTcm4nT1XmbZIzIVLVtOHQON6n-g1D3qPQN7RjowTnKmLenJV9Ft_1mfpdtXlZCe8TZtu8FKMIOiZAZSfcQ5sU369Nqnn9uI_ZyRY2X4eKc4fPu_Jvtc1xI88h98Wt1iZbBgdTuWWKqZ4dwxoRd1MfJE5F61JZUPzRUOQLC2i4O5LRX-50E-vA_1m9NUAh5qP76A5yDS4nJkBiyP26XeMtXf1edcBizAupyGd60J1BIc1ZH0YPd7-puomX_1SA68hw4t3aqu1upFJzE_0C-6BwDU8wx4LS-J3bpIXXTjePxtgmLu4p2aM4NTjb6JmPnAW_k9SfxZC0fU0foDmD3m5ZFqb_bDxcWg2wjqqd4e2eowQAdetruKTVsp4vZ0dcLKXemY3wTn5MNk6XRcPwkUJkaoNOFKGt4LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«موج‌سازی مجازی» یا عملیات فریب؟
🔹
در روزهای اخیر، برخی جریان‌های ضدانقلاب با فراخوان‌های به‌اصطلاح اجتماعی و خاکستری، تلاش کرده‌اند موج‌هایی را در فضای مجازی ایجاد کنند؛ فراخوان‌هایی که در میدان، مابه‌ازای قابل‌توجهی نداشته‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/683070" target="_blank">📅 16:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683069">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وزارت خارجه آمریکا: خبر فروش ۴.۵ میلیارد دلاری تسلیحات به قطر را تأیید می‌کنیم.
🔹
پروازهای تبریز- ایروان؛ پس از دو سال وقفه از سر گرفته شد.
🔹
وزیر دادگستری ترکیه: برای نتانیاهو درخواست اعلان قرمز اینترپل صادر کرده‌ایم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/akhbarefori/683069" target="_blank">📅 15:56 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683068">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWkxbUuCZcl_H1tAciWVbOG0MFQLFQ5SOkRrMOwrcVa3IOtdY8D_UGO6GyJiUDzaAGCzeAtF7vqYBC8aKo0dteJ4kTxNFd4-V_2MZ_7p2Hl8BoWDBB5f_H1quaG5wy_aUyeLfWkaRaRLwplcpCHfw9UbCe5TQZXJR-FnFsMcZetx-hANa-TnyLD0N8-f0HYq9KWd3FLRN-b9IR643Rfr0dVEtl10oS4_Y9bhOsTb9dFtqG1NVCP9B1O9ng77x0r3Rvz7wcYtnyvfuD49DUdqTHvllv8GgnjdjG3u2fDzHttLU2wETPHamqaHGwyYphBzss-7bytlQ89UN7TO3aov6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت از ۹۴ دلار هم عبور کرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/683068" target="_blank">📅 15:50 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683067">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M8wvAdKiDSjMBdpf0FQD_d_GouWFWg21RbMD5w0h_uuMYZ5MyWsRwhqxUuZWuUXqomNK-oLDMdOvOAna59vyhAxVZgwS56_EVos429AHOVKjuNCLpkBOTlY4cAOP4jdndNAi6IyuXm7VUUFbu3T2RrJp1WQZJl0mIr4h_28yHdMVErDg7S0usQvw0KGwXDnaPnoiNDrjVYwXJtDANEQ_u-9vJ5-koWWLA32AhA2dSf1PH4If6MD2tjMtB_AdI8OX16r9YId3Xq5z2uxOBG_BzukUM434LAMvy252U-mc2rIFy5YeDxCxZhGtwZoxtU3EBKyHLiL4Kn-vngBWCnOmUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واشنگتن‌پست: احتمال «غافلگیری اکتبری» ایران
ادعای واشنگتن‌پست:
🔹
ایران ممکن است پیش از انتخابات میان‌دوره‌ای نوامبر آمریکا با گسترش جنگ، حمله به نیروهای آمریکایی، اهداف انرژی یا کشتی‌ها، فشار سیاسی بر ترامپ وارد کند.
🔹
این روزنامه همچنین احتمال اقدام پیشگیرانه آمریکا علیه رهبری، زیرساخت‌های انرژی و تأسیسات هسته‌ای ایران را برای جلوگیری از این «غافلگیری اکتبری» مطرح کرده است.
🔹
با وجود آسیب‌های آمریکا به توان نظامی ایران، تهران هنوز قابلیت حمله به اهداف انرژی، پایگاه‌های آمریکایی و کشتی‌ها را حفظ کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/683067" target="_blank">📅 15:49 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683066">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/elyrk9VlE8HrSEbIDlUkMPw3pM3Y9FDzBNgBkCXzHe048i6W6m8wqTpYTrnXu2wX3VqnrkrYYL4LlUKxOc1WK5RF_MW5LVwkHCOkD0aEpw6_9wE_iPD3H8hZTQZSSE20ysDwGgUp8jDyZQNhmUwgdO2TM1o5cBmIQ3ypDbbaDyA6Epq4IcH_ayRz_i5TVmsx3uphhU9y1HDzzvzgXubgj_TQ2uXA-9j3OPtONTmNwR-ZvYkMPR4UTSdoPT_Ag2q_rafWYn1kS3GjLI6mBBrRkpG1l4LwGKqV22QI0azcCen27x0Py6DogbYA6uUDBPXuf3zp4B76-Yps9Q2eZZuhsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ممنوعیت واردات لوازم خانگی؛ ممنوعیت قانونی واردات، مسیر قاچاق کالا را هموار کرد
🔹
هاشمی نخل‌ابراهیمی، نماینده مردم هرمزگان: پیگیر رفع ممنوعیت واردات لوازم خانگی از مسیر ته‌لنجی و کولبری هستیم
🔹
سید عبدالکریم هاشمی نخل‌ابراهیمی، نماینده مردم هرمزگان و عضو هیئت‌رئیسه کمیسیون برنامه و بودجه مجلس، با انتقاد از تداوم ممنوعیت واردات چهار قلم لوازم خانگی، این سیاست را عامل افزایش قیمت‌ها، تقویت قاچاق، کاهش درآمدهای گمرکی و فشار بیشتر بر معیشت مردم دانست و گفت:
🔹
ممنوعیت قانونی واردات، مسیر قاچاق کالا را هموار کرد و سود آن به جیب قاچاقچیان رفت. تداوم ممنوعیت واردات نه‌تنها به هدف حمایت از تولید داخلی نرسیده، بلکه موجب افزایش قیمت‌ها، تقویت قاچاق و کاهش درآمدهای گمرکی دولت شده است.
🔹
اگر بخشی از واردات لوازم خانگی از مسیر قانونی مجاز شود، مبادلات رسمی مرزی می‌تواند جایگزین قاچاق شود و دولت نیز از محل تعرفه‌ها و حقوق گمرکی به درآمدهای پایدار دست پیدا کند.
🔹
پیگیر هستیم بخشی از نیاز جامعه از طریق ملوانی، ته‌لنجی، کولبری و مبادلات رسمی مرزی تأمین شود؛ اقدامی که هم به معیشت مردم و اشتغال مناطق جنوبی و مرزی کمک می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/akhbarefori/683066" target="_blank">📅 15:49 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683065">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b0aa356f4.mp4?token=RBHMw7PtpvhFna1h-qjv4o4wCz_Td9k6CELQCWlNAvPY0okvn3IANw43p2u1hNlfQzHIqnGrbhEtpMIir5nU0txMaYWeV9-kJAW1ndemiyEXV6x1YVwM1cUq7mBY5YzM5IaDxsZJE7cNlPn67IdPO-O3WoS-I7i60lP71beNzKG-aeK5SLmMmiX2ohbHXYI5LLd33JthZvgvOtSi64XjKpvefX9431vGnsGb4yafgZT-uxBDnqdwG8o5fjG5Yi4KxKZn0Qnyd8wMpBXAUBLauc2UinTWIQACVFDpnG9Svu6Rcv5FwnHNu1HKwIOIsotqhMyueT_3lQo-TGMtLWV3zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b0aa356f4.mp4?token=RBHMw7PtpvhFna1h-qjv4o4wCz_Td9k6CELQCWlNAvPY0okvn3IANw43p2u1hNlfQzHIqnGrbhEtpMIir5nU0txMaYWeV9-kJAW1ndemiyEXV6x1YVwM1cUq7mBY5YzM5IaDxsZJE7cNlPn67IdPO-O3WoS-I7i60lP71beNzKG-aeK5SLmMmiX2ohbHXYI5LLd33JthZvgvOtSi64XjKpvefX9431vGnsGb4yafgZT-uxBDnqdwG8o5fjG5Yi4KxKZn0Qnyd8wMpBXAUBLauc2UinTWIQACVFDpnG9Svu6Rcv5FwnHNu1HKwIOIsotqhMyueT_3lQo-TGMtLWV3zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیل در تابستان؛ وقوع سیل در قوشخانه شیروان
بخشدار قوشخانه شیروان:
🔹
بارش شدید باران و جاری شدن سیلاب، راه دسترسی به ۹ روستای بخش قوشخانه از توابع شیروان در خراسان شمالی مسدود شده است.
#اخبار_خراسان_شمالی
در فضای مجازی
👇
@akhbarkhorasanshomali</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/683065" target="_blank">📅 15:40 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683064">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
مرکز عملیات تجارت دریایی انگلیس: تردد کشتی‌ها در تنګه هرمز به ۴ درصد سطح پیش از درگیری کاهش یافته است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/akhbarefori/683064" target="_blank">📅 15:37 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683063">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
استفاده از متانول در بنزین تولیدی ستاره خلیج فارس تایید شد؛ احتمال افزایش خوردگی در برخی قطعات خودروها
🔹
مدیرعامل شرکت نفت ستاره خلیج فارس استفاده از متانول در ترکیب بنزین این پالایشگاه را تایید کرد.
🔹
انجمن خودروسازان ایران پیش از این در نامه‌ای هشدار داده بود که استفاده از متانول در بنزین سیستم سوخت رسانی، باک، فیلتر و پمپ بنزین، لوله های فلزی، واشرها و قطعات پلاستیکی را دچار خوردگی شدید می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/683063" target="_blank">📅 15:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683062">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HPM-nya2Bmw6ocNcRGMGW4JNvkLYw680OcN4_gpbNvMGSWl8O0t2is3K8uQYHIE40G0dGZEDv4WC7tbXi1KBTTJFjhVxfEYC29GYsQL-a_Wt3fFY8bXBJ7S1xL9iG3X5mgCDKbies3LR3cDtQOIp6wf6MMqzy1vuA6dxlG2mbewV_2ojpprq6boQnJsJCIP-dmvi5O1WEDqNlC65LuEOCWq4r-i06g4zxfKqqHuf3TrVjeQnPfgMH6cHlklPqXB_9kgSauUqWBy8HAT_HF8pSMja2ekmYU1jMfVblcRh26XpXrV8ucdgDJvsPkFX18R5DYc8OpS3PVcWJEHwx8UwHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازگشت ملانیا پس از غیبت مرموز یکماهه | مقامات امنیتی: او ترسیده بود
🔹
ملانیا ترامپ، روز پنجشنبه پس از بیش از یک ماه دوری از صحنه‌های عمومی، با جمله‌ای شوخ‌طبعانه در باغ رز کاخ سفید ظاهر شد و به گمانه‌زنی‌ها درباره غیبتش واکنش نشان داد.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3239331</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/683062" target="_blank">📅 15:30 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683061">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae1568e3bc.mp4?token=hIYw1GpJrrQh6pzMSGiDzp44P9lusRkH36m1vgoH3naETQJmh2gAgUwmQmGBjnlU435pfxnm6yDIQ7E4t2SIL2OLAGLWn66JWFeWG8srDmyzKarIo-zx7OCLj0qjRSFBSRyWNN9SXFsYtOREuXutI16bH_OdD0v9Et6gEaqI9peN8aCcnE-DdWU0zsTZMn7fs5pBmYQ7rUqlifJXLG4uLl18SXFzKdp2W57m1LiJaaB0iWIrsfh9OX1Q4EpLr7k5EjOI6Q9gRr5VU_vB0C_B-3pDMW4cXD37bIqDvVRm1gLAGZQajkZIA46XA9oKntWymR7Wb6447Zv4NxK1OeeVUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae1568e3bc.mp4?token=hIYw1GpJrrQh6pzMSGiDzp44P9lusRkH36m1vgoH3naETQJmh2gAgUwmQmGBjnlU435pfxnm6yDIQ7E4t2SIL2OLAGLWn66JWFeWG8srDmyzKarIo-zx7OCLj0qjRSFBSRyWNN9SXFsYtOREuXutI16bH_OdD0v9Et6gEaqI9peN8aCcnE-DdWU0zsTZMn7fs5pBmYQ7rUqlifJXLG4uLl18SXFzKdp2W57m1LiJaaB0iWIrsfh9OX1Q4EpLr7k5EjOI6Q9gRr5VU_vB0C_B-3pDMW4cXD37bIqDvVRm1gLAGZQajkZIA46XA9oKntWymR7Wb6447Zv4NxK1OeeVUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ناکامی گروهک مسلح در ورود به مرزهای جنوب شرق کشور
سخنگوی پلیس:
♦️
مرزبانان هنگ مرزی سراوان مسیر نفوذ یک گروهک مسلح را مسدود کردند؛ در درگیری، یکی از عناصر گروهک به هلاکت رسید و سلاح و تجهیزات ارتباطی کشف شد.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/683061" target="_blank">📅 15:30 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683060">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
کف‌گیر پاتریوت‌های آمریکا به ته دیگ خورد
🔹
مرکز مطالعات استراتژیک و بین‌المللی (CSIS) تخمین می‌زند که آمریکا حدود ۸۰۰ موشک پاتریوت باقی‌مانده دارد و این امر تردیدهایی را در اروپا، آسیا و خلیج فارس در مورد اینکه آیا واشنگتن می‌تواند همزمان از چندین منطقه دفاع کند، تشدید می‌کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/683060" target="_blank">📅 15:23 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683053">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/swPJ-UsQ-exS5vDlWhspWrF_G_-X0YVjT-Q0dBs0N_dDPlx0CBcLr_XXRYSU349BwXWPMc-jObdZAwWo--NUGTtUOKNnCYvNviGHK_t9_Eum0ZDRYi63SaG1exZS7pcrYFqJI1_IrHkjLaKfjqyhTgQ6mXBe_jBDd2Y4c1AHnhuhthPHy6NBr3JZir3Ar2TgqU23UzEnusgEyr0aplzkBssMYeQRE_0jBe66o4IN-1-05Dejvo0akn5A13uQR86nBFdt3jDoqtbcFt_Rk_YfiDfM08uGSp0r6oQjLmck7phDh8BuqoH3rzUpbNA2aSdSwLvWlzyt0vmSQbG80RZLpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FcjGbOqoZNOIkLMULcLeF6k9S6BwMLnuHyamjTHoLzqKnihqayQl0u-ho0btBQXKXADnV9iQOE5x0XLgjHSwF2L4h5l94cTyoSAk5mS6lODnEaefuqaiMipL9Y8u7-Bxd6MpWiw-wgH_hHBcd5P1BJabOYeILnnCDcACHMWmWqsOGt59WQGUTY8kKuelUvgmBMVS2mryeJyiIE6FEqHMU55piFX9OtUfwYV_LPTtLKTRqW-7FNAsP4fVEXUz4-FpI0sg1aLYPm-of9meQikPEi0qO0ozhzvDDhiElyeAKswuBk_Tv1EOKGM1K0Zx-ZQYlGbeFnCZsrIz5dL6rcxkLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R79bOFI_3xbcVnWb9Ng4xZNkvi4U_EMogskvME-xnmybwX4GYr89bjnwYzW70ijnms8mcBzTfZiJfcIc1LJlP_JF_b6inqCHxQr03x3Ntda21vi_-4dZ-B3bUbHsTDllABwt4YY2K_rQ9dfO6_-n5bgNl6Lf3NFjJngf1TvIoKtYTJJGeaa_ACUERE_pkwSCUdCjzXn-4euLgOQgRj3_bZM-V7Ll85C67K1ara4tl8gbak6DNZAU5LwASTzRTlFxE93sTqgyRoZFZE5jsMyKXhKdxUxqZ2tViWTMnwhY2SO09YCe47Ur7JSdAwVj9zNf-10t-nEy2tnZ_Ms4rrVpJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s7Z6Mp86ROT4UW80LF7lJRN6ChwwUweKodI3NuT3q2bYSCcE9wOWyQKk-N2vKZnL8pj_C5q9PNjsIYIl7kQa1eFjye7YRkwrlSe3rJYv8myf5il3mlGNEydf-BfvplMd0wWVjEk35w-eyrY8OWAKNYeJ3hfwEBnqKlP9rBFOE4jLvskNr4z03-pPaEnlebQSBKvCLncwpO_ME5P4T6ORL3DixNxDmth7TqnnVww0oTsXqrW4U5_5IPwoQaQ4n_aJHSEHSINF6OzZg_IS0PXKxZjApr8UEXEn6kI02N-2cVYIfTDJ-ErYo95sciGmA7Qdd8kLAzA50oFtGQWh709t8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qrr6sHqN2ORjlcLg6Uy91HH5kItBqfAmMXl7Cl09MQKtxx5H87Rvcq0oGZXWD7xutYlitEsOBDXedfs1vQfnGdWeHthOxWbb347ecL0oLrZxEK4RWkAaEiaPS44VLDRkfYtEPbF9CVBwzsa27udK59_1auumG98zywLCfMKxyDVr5D2qtcGCgBEdXfTAeE-AXIhRRuCVFkD9YvibYDYXidz0DiWAlUg6yQT910470wh7DnkJPpq5eyYLWowyCX-n7XEGbURRrx56uQ-bX6jyjT4GMiQX3kV2_h1H7txMJNz98wJbm0Bevu-oHiWIVYs4mbsZ_h1nIUJecy9JXLD6Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F1yFEZjryosuZTUwEm34rp1RmD4hLjI5ELGz4P6dxdc6QqYXCSUalsSojkD2e4Nqa_Aq6NMMKWULx1fNPV6EaJlsQ6OL-hqJWZJLtDikRoM1Ox3Dvh0IYHpp0PokjxdOyGLsJAHhOFVqnwkd9RjUEz_sQbWfuQRqlpp0kwihwWWuQmAc-6h76Pf59jguvR-t28rCIfLlHA5wb0cPNYH-bOVehmCnurC8mHDXBJoYYhDcykdmlr_sEBy9calUMPawBENLT1loYQ0r3PYqwK7NIfagLNLOonyz4U4vZ2Qx8l88e_vpyhNa2-FGoDk0JkCp1dnLyVVfYi6kuf3ro719xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XAwByUXtduete0IvWnPyh285zdsJodayYZZKqf030Isd5hDzkhUidVdBX6NFG1LCPTNyyTDoC58Q_EktNkSYqTC9oiKMzsMs1tu4dwhM_cDjwUtuQL52w8Lj917G2k0g5jDLcLi5ECUrukk-TsNfs3MmYxiyzFyLPD8a3YTH09OrUel71etOsAsL21QBkLrGq4Q7QKHvcKkHw2AO2HWGxeMlhxObUEjIK06RWcJ0wnff7zFO7owBSdcHwv_DTXN2-Y_IQ0M4Uj2dmxh55y_6xHRN1oy4tzaUSlbUxZypSEPTZMAlRFgsilrQdDNHG4UiS-DdW31GGEN6ooiQakySLA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۷ مدل بستنی خانگی چوبی خوش‌رنگ و خوشمزه
😍
🍦
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/683053" target="_blank">📅 15:20 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683050">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OMkPhBO3Cv0nLrFsmndrqdyjhqUkxxGc33DkloiHlRwO0JK6fxJQzb9wIWyhXeQi1tx-Yi4vTZMAkSAeDsYPe4WCLCmDw6s_PUcqgP4o0zIcR7WTfFSn1ft24poCy5JNSCR46lDhj6mGIfPccnWhCGRu9po1m1DTBUuiKYdi-3_SzC9M7NHauzwgotGAWkaipF8JLdplms10W2DHlyB5Uj8YsbhSeoU0zYblG5vsIiUNgvytgg6SW0SUVo4li7GHpQMeeby8NcIh4Ey9O9pd53gP3yTV4FPNgpRMYhHVbq8JKwZipY9erLFUcQCtRutN4yDQmOKsLX_jM0fitzBpvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QL3BQz30qojh1Jb_W_FQVNKVQ_R_oF-z1DuglR_9LPyPI29tGtZVRmScE-2C4Kywz-lw9_kHlRvbFa9r0AnBROdbsMywSctAWdEfaamxpx_6HVEPj1wUNBOSRG15ai5ZTu3RS-vX1CEB5g6bOemXsjCmoT-FjJwT_gKGGrIMgsGSTNF90WUQCpOc-WY8zmkABkBofcRnLBFLhWEvmKca6anXPN33sP7K4cP0uSahcAj18sS_DG2V1aqA3wvU4u9txHlfEb3ui2jf9REmVXPuA_A1x0iBemhq-JNV5wIMFf7sGP48O_nL726STXc1TA8lr1tLaKn0PcPN4rCfSfeF0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dVbS5vKnpXn6XXVsapZID8_W8bNWYhZpg7BajvAJpNOxcYzt2sp5XHptrifVYw6xAqYvij_12LDElHBTypmY-sLfFX5fFAv1eeXrFLLJ-B2sPyk9TLzxoBYjSjb16nPmtWYbv-gdVTywLTJp9Z4bB6ey_dskEQ07lfIhHtaq2yX9D0ykAMKluZ2HHIB9ORPYt6rYOhknssIWqAU-L-aCX16nmfb-0MMjmtbtgFtHhN5Ic64-u63AI8CXtn2xhUzTLt7v-Dy7-so4DyV4_HuCC5vHFFiDQa31RdZVlawOr0vaYAUaBbU_AoEjvfHDsYPARpY9lvBQ-fAooQjD3UanNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
همه باهم برای ایران
🔹
بستن شیر آب در زمان‌های غیرضروری، گامی ساده اما مؤثر در حفظ منابع ملی و مسئولیت‌پذیری همگانی است.
🔸
الوفوری را دنبال کنید
👇
#همه_باهم_برای_ایران
@Alo_fori</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/683050" target="_blank">📅 15:18 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683049">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sjl4IJYJIf4FkIAmoE766X2yK4OIT_cnZRrE2KWqH85MpOIlCyhyN605MjFjvquO7sPWy8dMBigScSOm7f8w2nySGOXEktNfAwuK_SUj7mC6l8-Z9UJCWwloFNaHzPdS4fWOlJ_Iqqve4s6L4xa5q30gIgT3_XeBZmhZ7UvGnyb_D9AUvSdVYXwhNVEz08hssDSVoxSLS4ntc67fOqfdF-jTqnnOhRCooryqpwDI2JYqPNT2muCuGTcACqvwOzY-0I2oJKP0R9c6zqBEjD4pixKustmNeiFsVN5Bb8rF8h3FKo9LTqh8mNmpeMoXc8GgiXMhLgmCHAuWEBmuTyXbwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تداوم شکست نامزدهای مورد حمایت ترامپ در انتخابات
🔹
واشنگتن‌پست گزارش داد ترامپ که سال‌ها خود را «پادشاه‌ساز» حزب جمهوری‌خواه می‌دانست و از صدها نامزد حمایت کرده بود، اخیراً با شکست‌های انتخاباتی مواجه شده است.
🔹
سه نامزد مورد حمایت او در انتخابات مقدماتی جمهوری‌خواهان شکست خوردند و شمار شکست‌های نامزدهای مورد حمایت ترامپ در انتخابات‌های ۲۰۲۶ به ۱۰ نفر رسیده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/akhbarefori/683049" target="_blank">📅 15:16 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683048">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pTQhamPABbHlWHmsiw4XW2IWv5VvriDajj2mLTYvzD3fAq2uLR5A3j1XtAhRgQvpxCXnKMawZkLGJ_X20pJkDk8UwCqyqu9QSHlD9NEOK_8yckm6UI4WqLrtcC4NhNgPXTlq2cIC6yTm7g7Eo1Ljf3HdV9fzsEAwPIeOj9LxlQVOVu_NsadAf7UhDoxi4x6MVQMA3p6xzBRKufoX88SefReKWjECWof9crutSmR5r5NlNtiiliRFDcZsnQ6IjILGsYW65KmoekfeGGpoidQlWz-Ih2l_BtAnAk6s5pr0zbiF7M4PrDFZRtbaQMSlz1ya3jOD3V2MfRAkhXia_F65pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: انتقاد از مشکلات تورم و مسائل ناشی از جنگ با شعارهای برخی همخوانی ندارد/ وقتی شعار می‌دهیم، باید سختی آن را هم بپذیریم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/683048" target="_blank">📅 14:57 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683047">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
نرخ غذای دانشجویی در دانشگاه علوم پزشکی ایران اعلام شد
🔹
طبق اعلام امور دانشجویی، قیمت وعده‌های غذایی افزایش یافت؛ صبحانه ۶۰ هزار ریال، ناهار ۱۳۰ هزار ریال و شام ۹۰ هزار ریال شد.
🔹
برای دانشجویان بین‌الملل نیز هزینه وعده‌ها به‌مراتب بیشتر تعیین شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/683047" target="_blank">📅 14:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683046">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
پزشکیان: انتقاد از مشکلات تورم و مسائل ناشی از جنگ با شعارهای برخی همخوانی ندارد/ وقتی شعار می‌دهیم، باید سختی آن را هم بپذیریم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/683046" target="_blank">📅 14:44 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683044">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cegi8q5-oAf3X6eH54bvQlUg9UaeA2D6kIYNK-P27zqiYHoJp0nPVbZkTDQxq4wZ2nAEOIjb0p8b7BoJ2PKSnmkdbt77HI5lnsPdOvgtsqDNZnYsd1olv-oXSklBaSKztNeYAnpH4p0yikOGAGgB0HoqVMhYYuyHw_9S3ccobz2XOLfOfMwvxmh6v4yV-aCyzvKTywAkEedERg1TgI-77balT88mgdzEbuhCoG0idd1r9xzSHGetkV_PT1elnB4fKN_z1_AbK6vlGkaRNznQR1Y01xNv96dcMgBbYt_7OjQzGDAFI9nqwQ7z5gyi51hQ1mS4nMo3yLyVx3CWY0gSEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پشت‌پرده تمایل بیرانوند برای رفتن به بازی‌های آسیایی؛ یک مدال تا معافیت از سربازی!
🔹
احتمال حضور علیرضا بیرانوند در بازی‌های آسیایی ناگویا مطرح شده؛ حضوری که علاوه بر کمک به تیم امید، می‌تواند با قانون «سرباز قهرمان» راهی برای پایان خدمت سربازی او باشد.
🔹
در صورت کسب مدال، بیرانوند می‌تواند از معافیت این قانون استفاده کند./ میزان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/683044" target="_blank">📅 14:29 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683043">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fb760beea.mp4?token=QBe9i63-Ag2L9p8rmnQ5GNRKZxGM96pWHxbYFxdUvfFN2iRIblIeDhCQkjih0BX8CWDhmTccRTaVAuK6C1-FMpTg9Bi4V8ji0SjHkYq0249y27FZyTP3nUz_WRN8KP-VinUZs-__ztMPav0lUx_OY0g3edPZyu0BDte75Eje5_IKRwTId_PDKErt8UPW_ZmmmznKpg6KVcMEPrzfjc2Y_NN3kQ_UqzPIGN6AFKCR4a9sEJHOTWqNqvSpnVsr9Cd3YNM4IuQUBqT0zeLmoMwlTsYlLge5ECL96V4FZtZWsIfZhhnTlYXrLSic2dxg2YsXCSRSQJBJ7Ef5QR4briTOqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fb760beea.mp4?token=QBe9i63-Ag2L9p8rmnQ5GNRKZxGM96pWHxbYFxdUvfFN2iRIblIeDhCQkjih0BX8CWDhmTccRTaVAuK6C1-FMpTg9Bi4V8ji0SjHkYq0249y27FZyTP3nUz_WRN8KP-VinUZs-__ztMPav0lUx_OY0g3edPZyu0BDte75Eje5_IKRwTId_PDKErt8UPW_ZmmmznKpg6KVcMEPrzfjc2Y_NN3kQ_UqzPIGN6AFKCR4a9sEJHOTWqNqvSpnVsr9Cd3YNM4IuQUBqT0zeLmoMwlTsYlLge5ECL96V4FZtZWsIfZhhnTlYXrLSic2dxg2YsXCSRSQJBJ7Ef5QR4briTOqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شغل عجیب و ترسناک یک زن در فارس؛ کمک‌رسان چوپان‌ها در دل طبیعت
🔹
یکی از عجیب‌ترین، ترسناک‌ترین و هیجان انگیزترین مشاغل در ایران مربوط به این خانم است که در استان فارس زندگی می‌کند و به چوپان‌ها کمک می‌کند.
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/683043" target="_blank">📅 14:18 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683042">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_q-eZ3nepb8_Jx2azDasQAmupz8oLO0prDyUYbqPeO8t5C31OxhpH6_bUC4QE6xkENCENHKiUPJ34w-eZqwyfSQ4Bhifl8Fz0zl24TinotfLLodIYoZ5uHzI_7ufaoN4Y0Klb7MRu_mlUHpu2XLDQ0Ux05eiSs-JLzeoHJ7FznX9j1fGN_mSNTnSpN2X0BmKORokKbvRif8lbQxEztFS9t88bbE5JoMqn3goh5y4nC9lZA9_91INhxEyYZTJu-ZFafnBLuXk_9Ty6l2yz_hl6UegmGvPzKZscFaCEyEGAfrVovRc6hh8TpATjiCsjM0m0HFkBJLHfaYx2Xa_RYsow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تقدیر معاون اول رئیس‌جمهور از خدمات سازمان راهداری و حمل‌ونقل جاده‌ای در اربعین حسینی
🔹
معاون اول رئیس‌جمهور با انتشار پیامی، از تلاش‌های بی‌وقفه و مدیریت موفق سازمان راهداری و حمل‌ونقل جاده‌ای در ساماندهی مراسم اربعین حسینی سال جاری قدردانی کرد.
🔹
محمدرضا عارف از حماسه اربعین به عنوان عظیم‌ترین همایش وحدت‌آفرین امت اسلامی در پهنه گیتی یاد کرد و گفت: این راهپیمایی عظیم مقارن با رشادت‌های ملت ایران شد که در جنگ نابرابر ۴۰ روزه با الهام از حماسه عاشورا، حماسه دیگری را آفریدند.
🔹
وی یاد رهبر شهید انقلاب اسلامی که عمر بابرکت خویش را در مسیر عزت اسلام و مسلمین سپری کرده و همواره بر پاس‌داشت شعائر حسینی و عظمت‌بخشی به حماسه اربعین تاکید می‌ورزید را گرامی داشت.
🔹
عارف از تلاش‌های بی‌وقفه و رویکرد مسئولانه سازمان راهداری و حمل‌ونقل جاده‌ای در ساماندهی باشکوه‌تر مراسم اربعین حسینی سال جاری، مدیریت مدبرانه در مواجهه با چالش‌های اجرایی و ارائه راهکارهای اثربخش و ایفای نقش محوری و ماندگار در اعتلای سطح کیفی و کمی این رویداد عظیم قدردانی کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/683042" target="_blank">📅 14:16 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683041">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81ce609344.mp4?token=TdnYT7JBRr-pa4SShg_m69UvK9oEdGcCYnbaX5YtsjoCItwPvMfO7ggFxLYYo7gkOlDJybs33KwRHLzQqTCUBZ_9h_yDTO7nMMiaGbaP8UG13Q3Yf6diWAFsooxX6WVWydEVyIJwm9Qc1k6ka16EoiIQebvzVJVEZlqGLWyEK4hRmoom5OE7P6JM28uSecwEmQsBuB7vTW76zDARUU6DzX1yOqdWxn5EDmoPkzh0_kwcDtJr5aLvYtusff8AVu71CNQEWEMRrnfzevHMtQQVK2brMZSIDFaJg5nMpH0nMearHFez46oBaPVKlP6dRxJ5Q5VDbKjomnlOZOTCyG4j0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81ce609344.mp4?token=TdnYT7JBRr-pa4SShg_m69UvK9oEdGcCYnbaX5YtsjoCItwPvMfO7ggFxLYYo7gkOlDJybs33KwRHLzQqTCUBZ_9h_yDTO7nMMiaGbaP8UG13Q3Yf6diWAFsooxX6WVWydEVyIJwm9Qc1k6ka16EoiIQebvzVJVEZlqGLWyEK4hRmoom5OE7P6JM28uSecwEmQsBuB7vTW76zDARUU6DzX1yOqdWxn5EDmoPkzh0_kwcDtJr5aLvYtusff8AVu71CNQEWEMRrnfzevHMtQQVK2brMZSIDFaJg5nMpH0nMearHFez46oBaPVKlP6dRxJ5Q5VDbKjomnlOZOTCyG4j0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بحران سوئز؛ کانالی که آغاز پایان امپراتوری بریتانیا را رقم زد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/683041" target="_blank">📅 14:13 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683040">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PeMM0AB2UJxvGnLOyukSgZ6XvAiYcEMeUXzL3w1xMtuYhS68wh6AYyZ6u28GrEqaN4aClI-DHSQHd1QuRA4XXeBs8S-iVj0eGAjs0I9jEFqtfYyLfHkn0p-HuGCuBaFvRTuamnZuqgkxglBD5rN95f0mzP_Po4ynmsS3FlQZQGBQWM06rD4WWyKi597F9G5WVu6bomkmaIFGw-JRQOLKI5pdDm_3WWR7PvWfQaq6IBEWJPivwKhqjPD_ioxCxj_XrkKphZ9bgPZx22062_xI4MtaPJ7CggEBujfloHXA5riWwfdOuPcIJH9X48F7EGSqFLOH1zTNaoDVBjfs0ONxwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توصیه تاجگردون به پزشکیان درباره «بنزین»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/683040" target="_blank">📅 14:12 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683039">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
سخنگوی دولت: درباره قیمت‌های جدید بنزین هنوز تصمیم نهایی اتخاذ نشده است
فاطمه مهاجرانی:
🔹
در صورت نهایی‌شدن هرگونه تصمیم در حوزه مدیریت مصرف سوخت، دولت جزئیات آن را با شفافیت، از مسیرهای رسمی و به‌طور مستقیم با مردم در میان خواهد گذاشت./ ایرنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/683039" target="_blank">📅 14:09 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683038">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30d8e0ebb3.mp4?token=jw4If06s9O_s5dfNVF575sa0tBUUA2iLLJasNxpMRNemvuzHS45oB-Gxt4fjigoqLod6c5nfo8ky-0iU_WhbTeb_3OJJ0HBZGDqkQmX7-TVn3xWu7ZYkwcMbFlc3-I2WJZx3hRf0EZefhqDnpidNhQ3O4P_Nnw6ElzwCdaYHzYE3eL9g5U0o5ifu85tjUoMrKAEjewJRBUKDUwB3oj-lTmb11Ock0Jm7nVwot_rFXr5nBcRZalmtlT8EebHhdu-wsD5FkN3YL2cHM5RPbuOmiqrFbABzBvydpW_CWgB3eWwtSrPHb-RMi2vqfXMXXRIZUbuH3I-DteUQH4GXpKlxNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30d8e0ebb3.mp4?token=jw4If06s9O_s5dfNVF575sa0tBUUA2iLLJasNxpMRNemvuzHS45oB-Gxt4fjigoqLod6c5nfo8ky-0iU_WhbTeb_3OJJ0HBZGDqkQmX7-TVn3xWu7ZYkwcMbFlc3-I2WJZx3hRf0EZefhqDnpidNhQ3O4P_Nnw6ElzwCdaYHzYE3eL9g5U0o5ifu85tjUoMrKAEjewJRBUKDUwB3oj-lTmb11Ock0Jm7nVwot_rFXr5nBcRZalmtlT8EebHhdu-wsD5FkN3YL2cHM5RPbuOmiqrFbABzBvydpW_CWgB3eWwtSrPHb-RMi2vqfXMXXRIZUbuH3I-DteUQH4GXpKlxNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهاجران در دبی به خیابان آمدند؛ اعتراض به پایان اقامت‌ها و اخراج‌ها
🔹
نیروهای مهاجر در دبی در اعتراض به اخراج و عدم تمدید اقامت به خیابان‌ها آمدند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/683038" target="_blank">📅 14:08 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683037">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OxXu4Zi6HgEwkltFg8kaEIUatgV5cRVtfDttX0m8YyxnvDNxSbPVfMaQgIYXoQTBehJAMqvdtLMRMgp44sCBjw7zPNEFr6KfyaOCecUWf2vCulomiu8NXlxPlPBGa8StpNZ7p7KUboAHtT6-HTXlDip935yv2aOSofoAWiamjlIbVrdgWweDugFVJCiNbFjFzM3gA9TrTDXnXDt1YhW4BKrkWpZ6wznkE1VYTB0dmjoucQyvgV9zbQjJCKWXt_Ozf30hBD9jV2SXlQltkmX0qeA7Lz6yE7KG7mkbQnJibtktm5XsrL4uc3RAyKxIydQ6UdhWgljWztiZJ_zhTv3Gog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: جنگ باید در یک مقطع به پایان برسد، بهتر است امروز که در قدرت و عزت هستیم و تمام دنیا به پیروزی ما اذعان دارند جنگ را پایان دهیم
🔹
عده‌ای خارج از گود نشسته‌اند چون نمی‌دانند دولت در چه شرایطی است، بی‌محابا اظهارنظر و تحلیل می‌کنند، هیچ رنج و سختی هم به آنها نرسیده و بعد هم دم از گرانی می‌زنند
🔹
انتقاد از مشکلات تورم و مسائل ناشی از جنگ با شعار‌های برخی همخوانی ندارد./ انتخاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/683037" target="_blank">📅 13:58 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683036">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/835c394f11.mp4?token=lFSzgESBeACOfRd_79GlNupxnk2wQDTywmsSYzKoLXpnAJqlTlSnKBqZ9uXSkNlC2FNUmjam8uXkeOLwl7givhCxHqtvb2PN_sGhRRLXuQ7o8_YqQ1s7M1TenhTZDlc6Miarolc0NpjyKInOnrjMIsx6nuRXFOoX_EHNHJ2j9kPh8CyjqUPm0SW5N_vZPXhcB5ghTT4zFENli85bOGZoCGxd6MYqNuaWA629t5IBJcbDrdQ-s02-YbCYc3U-4Wqf7ywF6fSqgICPfuawSvCCQxkVhQPq9HJiKt6-z84Wb7EJs4W0GjUPorwvgAGtivF6DmTN60Ur10Jeg9INnBKXEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/835c394f11.mp4?token=lFSzgESBeACOfRd_79GlNupxnk2wQDTywmsSYzKoLXpnAJqlTlSnKBqZ9uXSkNlC2FNUmjam8uXkeOLwl7givhCxHqtvb2PN_sGhRRLXuQ7o8_YqQ1s7M1TenhTZDlc6Miarolc0NpjyKInOnrjMIsx6nuRXFOoX_EHNHJ2j9kPh8CyjqUPm0SW5N_vZPXhcB5ghTT4zFENli85bOGZoCGxd6MYqNuaWA629t5IBJcbDrdQ-s02-YbCYc3U-4Wqf7ywF6fSqgICPfuawSvCCQxkVhQPq9HJiKt6-z84Wb7EJs4W0GjUPorwvgAGtivF6DmTN60Ur10Jeg9INnBKXEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ابرهای خونی شهر گالراس کلمبیا را چند روز پس از زلزله مرگبار ۷.۴ ریشتری، به وحشت انداخت
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/683036" target="_blank">📅 13:46 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683035">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
سمافور، رسانه‌آمریکایی مدعی شد: مذاکرات ایران و عمان درباره تنگه هرمز به بن‌بست رسیده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/683035" target="_blank">📅 13:43 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683033">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53e1bd7446.mp4?token=oJPd26dJRRZPMDg0xcQ6GFgrtp3zJ6hq0m6ZaKYnSx54PKgvxK8WE0HWjw0QajF8L0J_H5M4HDWJYjh-mxmDbFBPxdbFfqgS4lL_uOPxn-2fKe9GOLbn-dTkAXsE5lJRWZ_BS2_mC-G7nHtmmrXnWl1eaGidSL5ea4dD_iFHIgdhxqrwn5GQaq6Lncl7aEqJzgJFp-nywrN03vtN2LTrVxBs1JBji1SJDHqmMT5H4LUa7x9xqAYigVph6qGpemZQT20VolDUr_1eZR5ONUXFvlozugLSlWqmfYN4HcWYbmBf6Vl_NGu-DT2ZRDwDEVBmUu2E74zfxh2p8Iohfs8buQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53e1bd7446.mp4?token=oJPd26dJRRZPMDg0xcQ6GFgrtp3zJ6hq0m6ZaKYnSx54PKgvxK8WE0HWjw0QajF8L0J_H5M4HDWJYjh-mxmDbFBPxdbFfqgS4lL_uOPxn-2fKe9GOLbn-dTkAXsE5lJRWZ_BS2_mC-G7nHtmmrXnWl1eaGidSL5ea4dD_iFHIgdhxqrwn5GQaq6Lncl7aEqJzgJFp-nywrN03vtN2LTrVxBs1JBji1SJDHqmMT5H4LUa7x9xqAYigVph6qGpemZQT20VolDUr_1eZR5ONUXFvlozugLSlWqmfYN4HcWYbmBf6Vl_NGu-DT2ZRDwDEVBmUu2E74zfxh2p8Iohfs8buQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ربات «سوپرمن» رکورد سریع‌ترین انسان جهان را هم شکست!
🔹
شرکت رباتیک Unitree از یک ربات انسان‌نما به نام سوپرمن رونمایی کرده که موفق شد رکورد سرعت دونده سرشناس اوسین بولت را بشکند. این ربات فقط یک مشکل کوچک دارد، اینکه هنوز نمیداند چگونه ترمز کنه!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/683033" target="_blank">📅 13:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683032">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71b778864c.mp4?token=pnsuQd43HFOjqsrCXbQfbG3SoRIQckopNLVsaDYpfxXxfcnfayWpynsPlU2gmfxbpbluZoLN-hXV1KjZzshrUXi9UmWig8mHXNz3oU0LSvJTkK1kHUt-w80oKhl2cnMazjYaickc0Y3vGbpb4eb2V6cbqMDp4OTrzlawnFSXDmV2UkHacUg_lTeMXIXFWB_341BdGdxKNs2-2gQPJQaZEKoVILSrtBCYCeYbSCn6AVTvVG7oFk3FGvHYA2nEu6phgIdDftGKy3mlDnEutB68qIddqu2b2x4TZHExwtQMwWm_dZGH1ItKZwrdY2IItjyUneui9gljGq7oWrVPh1jGag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71b778864c.mp4?token=pnsuQd43HFOjqsrCXbQfbG3SoRIQckopNLVsaDYpfxXxfcnfayWpynsPlU2gmfxbpbluZoLN-hXV1KjZzshrUXi9UmWig8mHXNz3oU0LSvJTkK1kHUt-w80oKhl2cnMazjYaickc0Y3vGbpb4eb2V6cbqMDp4OTrzlawnFSXDmV2UkHacUg_lTeMXIXFWB_341BdGdxKNs2-2gQPJQaZEKoVILSrtBCYCeYbSCn6AVTvVG7oFk3FGvHYA2nEu6phgIdDftGKy3mlDnEutB68qIddqu2b2x4TZHExwtQMwWm_dZGH1ItKZwrdY2IItjyUneui9gljGq7oWrVPh1jGag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ما ریشه در این خاکیم...
🇮🇷
❤️
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/683032" target="_blank">📅 13:34 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683031">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011d77ae40.mp4?token=dR_mTNXq_f8c5Y3MVAjc4gjVKfWCorwN2AVdvaYwB7ApCfpcEXVuS4xJ2f5spWsofiIEqL_gDXQXQra5GBhaAsUMMkzm1uKrKpr-dYk4W4EgQepZ6lQk1EvSIzkZ_mpOA3uTylal0Ih73M9bcx21YSbN2N_hD_34FtL2QfLLD_zANmDlLjX-FMuw4oW6lhXo0qdHgiZ_-SKdPEuufLxydVHFDh6UOuzNGkcGmovyJvEUhb-Nkl5AJzrDpAvoLNlbLLbj_rWim3iSYctnWgbHZ3Y29TZrkDGSrUJCCZB8rKHtMmWuCVRgsBgxuDGm02McsIRBwBivLd5QTMz0aqPoHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011d77ae40.mp4?token=dR_mTNXq_f8c5Y3MVAjc4gjVKfWCorwN2AVdvaYwB7ApCfpcEXVuS4xJ2f5spWsofiIEqL_gDXQXQra5GBhaAsUMMkzm1uKrKpr-dYk4W4EgQepZ6lQk1EvSIzkZ_mpOA3uTylal0Ih73M9bcx21YSbN2N_hD_34FtL2QfLLD_zANmDlLjX-FMuw4oW6lhXo0qdHgiZ_-SKdPEuufLxydVHFDh6UOuzNGkcGmovyJvEUhb-Nkl5AJzrDpAvoLNlbLLbj_rWim3iSYctnWgbHZ3Y29TZrkDGSrUJCCZB8rKHtMmWuCVRgsBgxuDGm02McsIRBwBivLd5QTMz0aqPoHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سقوط پهپاد ناشناس در سواحل استانبول
🔹
ماهیگیران در سواحل استانبول یک پهپاد ناشناس پیدا کردند؛ هنوز مشخص نیست این پهپاد متعلق به روسیه یا اوکراین بوده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/683031" target="_blank">📅 13:31 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683030">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mRsI9dmsMQDIxd5oJm4ZOfWfHszSK3VdB5XB-eQTDXcJKERVyBHEoNNJ4L0MrhUfxIoHrVXrhKiC1mKpG7gbrbS1kaKVcFHRjJuZIOiLA1stJCeYuJrU9wedEfyDOyIJ363_ZOCiDV8ZkF40Ol5QvppR2Xn8-kP5vgAaA28zjmI7Uh9owt29CfwHGKMvjox7UuRLsy_6fLuLcxUHOPSv1OwbpoXsiYtn41rx1cWt5eRsbOq1K-qhfHPU9bEcESi4SVdZPGTUN0jHffdHEe5_63Q2qcabQJFnkSpPgyqlleCtw1AoebWStHxSKgA_w0GomfvtC9WCNnnPnvQtL6UIzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اقدام گزینشی شهرداری اسلامشهر در تخریب باغات تهران!
🔹
در اقدامی عجیب و در سایه عدم وجود نظارت، شهرداری اسلامشهر اقدام به تخریب گزینشی برخی باغات جنوب غرب تهران کرده است.
🔹
این اقدام به تخریب، در پی ممانعت از پرداخت رشوه درخواستی از سوی برخی اکیپ‌های شهرداری اسلامشهر صورت گرفته و همین امر موجب شده تا به صورت شبانه، باغات برخی شهروندان تهرانی مورد تخریب قرار گیرد!
🔹
این در حالی است که شهرداری اسلامشهر   با ورود غیرمجاز، این اقدام را در حریم شهری شهرداری تهران در منطقه ۱۸ انجام داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/683030" target="_blank">📅 13:30 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683029">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxhoYhCOHUXz924PL3_rULPilWyjVLxQDb3GP7ZAyCNeE3Kxn9ypvXCTFmWvympuvuGprhyU5SlaH3QVhBWvyLvRqMAJ86GD-RDM1W0kluS3X0GTQsgrdxgeqmAIPCipgowExpC6rjimcE1WMm-vt62aj2-QEmo2f7ajk-TkL-z3tkqTN_6L3pCuxuYE-VhTH3Y1NZcRozrx2YUwWei8mOiMmA13QhOHCfqb3cgO0fwJI1qVEXWwN6G0iqfTmN9RUhXJC-9IYB-Llw19tpC8uisVYqS82EpqNRgr_NhdhOGIefqSR1KpZrSDtpemMJLVAJeZGckOxzEoJpUtWqSYzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قبض جنگ با ایران برای آمریکایی‌ها صادر شد؛ ۱۲۰۰ دلار!
مرکز آمریکایی پیشرفت CAP:
🔹
شش ماه اول جنگ ترامپ در ایران بیش از ۱۲۰۰ دلار برای خانواده‌های آمریکایی هزینه داشته است.
🔹
هزینه‌های گسترده‌تر جنگ از جمله هزینه‌های نظامی، نرخ‌های بهره بالاتر و افزایش قیمت بنزین، مواد غذایی و حمل‌ونقل برای هر خانوار بیش از ۱۲۰۰ دلار بوده است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/683029" target="_blank">📅 13:23 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683028">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OexPqmF3F1gyLiCySNifENxRLGYv1je0hVK2ZyzFaPbtktM7vTgcRo4mHdy_aOlvGTnAMDRRGGVT11h3SzFds6k1pIlycNRE38eDSja1i5uTQHt9kL18jo34LKvluhrNUZNP3jCmFySCEvNCVudLs7FNk3iW_suSrFlqt76evt-si3Hv_FrFnxjNQ2PCA_1qK9R2w5rmKQ_XAPEJzbTe53R36idwmVLX5DjWzjDv4TgsHh-ZEJgCAP0Mg755bHREsnvwgwfAm-ImXZ0-V2kyEjkgIUOZaUS1m9tPpf6mvK8pyrWV1zZoUgYrKCozECk8k9ogwM6OXhRrWLHOEGunlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جنگ فرضی ترکیه و اسرائیل چگونه خواهد بود/ مهم‌ترین سلاح‌های آنکارا و تل‌آویو/ خطرناک‌ترین سلاح هر کدام چیست؟
🔹
اگرچه جنگ ترکیه و اسرائیل هنوز به واقعیت بدل نشده و بعید هم است که به این زودی ها به واقعیت بدل شود، اما بد نیست به مقایسه قدرت نظامی این دو بپردازیم.
گزارش خبرفوری دراین‌باره را بخوانید
👇
khabarfoori.com/fa/tiny/news-3238628</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/683028" target="_blank">📅 13:07 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683027">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83339bd471.mp4?token=lZWE_Ic-lvDQppPy2ROf0pN04kK_4ZfciNzamqooOMn5zto6dWh3X_1ZooD9u3FgFh_2LXVqCrZuRDC-jtxdIWMUun6EvYY6KPa8n12OtXZUi5ff3bC5LG39EYrYTGKbhzrJgy7qO_moA56JPRRhH7RNDwQ0eOo4naQAcjiOzbpDp1sd9gK06Wk_Kr5KlFEzljm44eVkI9ZV9QsewBvLzgQ_HDFyLstMgGgGIJxLATueikVGlZIpR8v3snF_Hn1BFCqyY_3vlQoygYu-9ITs0EVRYhAQTaCbo4My4eRM2kzzeg1MmrWNbEaoSkbHNpkL5oowlCQnftKK3yDZL5mbGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83339bd471.mp4?token=lZWE_Ic-lvDQppPy2ROf0pN04kK_4ZfciNzamqooOMn5zto6dWh3X_1ZooD9u3FgFh_2LXVqCrZuRDC-jtxdIWMUun6EvYY6KPa8n12OtXZUi5ff3bC5LG39EYrYTGKbhzrJgy7qO_moA56JPRRhH7RNDwQ0eOo4naQAcjiOzbpDp1sd9gK06Wk_Kr5KlFEzljm44eVkI9ZV9QsewBvLzgQ_HDFyLstMgGgGIJxLATueikVGlZIpR8v3snF_Hn1BFCqyY_3vlQoygYu-9ITs0EVRYhAQTaCbo4My4eRM2kzzeg1MmrWNbEaoSkbHNpkL5oowlCQnftKK3yDZL5mbGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس حضرت کی قراره بیان؟</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/683027" target="_blank">📅 13:02 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683026">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/309bcedc5b.mp4?token=T-cGWtG7Q_rIlBr910P2W2kYQC25RvjiccJ3tPxs7p1DsbtHQtvKyf252MRATqWqX18gR9IW4WQS__x2HCVSMD9t3bpiFNAjrgzsCr_iAB4e_gbIa0j37EXkquEv_5zVK15NaOSzUoH-L5-iiyUAoBlzAXN7kTRXNG3LzjS9MdP3DT0BR6V8ayDbMHdv8jAneXWPHLZoPgbiT06I_v8B1IoOik9cXjQmIwv72pZMpqC9SqD4_qRE83JhYgrZrOBoY0wEW4rfXSKw74-l1U-K8xVPkf-kfKhkRcSgXzQrOzlZQ_bvJj5YbkVU4WOJ6nR8s8duCv8HSuHpy6IdmfOanENkECtVcvq_aEYW9pZ7bvxs4FfQFuZ7REIPmnEwCvtnDmNgObdRRZoZFb10LWJ_XUI1yj07hzcVi8Fj5--t0HgN7HRQrGPRajE3geCQZfiC2rzHGu2cWnR4YvAZQl5GfWxs4u3jbqWfxBCnCThLvsxMPchR7s6JrELYTn7oHpf7Z9rc2GViaiQx1m0UemnJMEVnWWnp5aqk9xKdkghce-YRksRl5RPHCzdp7Mq4_kzkp2y_gIJNMOLnwiHXGUPTCfDxSmTXQ5APkCvIMdFLleMQHeCPrVWdZH7Yh6ZsmpVu6zIjooRF1zQAegYj4dumHrghoRKrrVBC6RvSID0I6Xc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/309bcedc5b.mp4?token=T-cGWtG7Q_rIlBr910P2W2kYQC25RvjiccJ3tPxs7p1DsbtHQtvKyf252MRATqWqX18gR9IW4WQS__x2HCVSMD9t3bpiFNAjrgzsCr_iAB4e_gbIa0j37EXkquEv_5zVK15NaOSzUoH-L5-iiyUAoBlzAXN7kTRXNG3LzjS9MdP3DT0BR6V8ayDbMHdv8jAneXWPHLZoPgbiT06I_v8B1IoOik9cXjQmIwv72pZMpqC9SqD4_qRE83JhYgrZrOBoY0wEW4rfXSKw74-l1U-K8xVPkf-kfKhkRcSgXzQrOzlZQ_bvJj5YbkVU4WOJ6nR8s8duCv8HSuHpy6IdmfOanENkECtVcvq_aEYW9pZ7bvxs4FfQFuZ7REIPmnEwCvtnDmNgObdRRZoZFb10LWJ_XUI1yj07hzcVi8Fj5--t0HgN7HRQrGPRajE3geCQZfiC2rzHGu2cWnR4YvAZQl5GfWxs4u3jbqWfxBCnCThLvsxMPchR7s6JrELYTn7oHpf7Z9rc2GViaiQx1m0UemnJMEVnWWnp5aqk9xKdkghce-YRksRl5RPHCzdp7Mq4_kzkp2y_gIJNMOLnwiHXGUPTCfDxSmTXQ5APkCvIMdFLleMQHeCPrVWdZH7Yh6ZsmpVu6zIjooRF1zQAegYj4dumHrghoRKrrVBC6RvSID0I6Xc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۳۰ لغت کاربردی زبان انگلیسی در آشپزخانه
✨
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/683026" target="_blank">📅 12:58 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683025">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tYCUCWKzZmBw7Fd-55ZMot1-IRSP37_LOb9yb6f3TsyVW8ZGlWK-L1pdA4ibG_S--f4jh59Wc59Krrt6HIQ6O0c7DkrjHFya8qnBwKgq0zJ5d481_3EZ4_muZwj_ht8oCj-kAUzvUVmF_2gFU10YRDKWloYAZeuranUMWjI7VG1FOVBwnuK4TDTGqhoqa839Ft9utJtDvdHfmgiS8R4flIEWUG8FcPsMjGPcSQAxogePQpadrmbn-Jp9MHdwCaYc2EB673jgkEA4GfTVaIRi2mu8uMTaC9vsXy7sn0-LENOLSw4virHqBCA4CZke6AWhJ7T6lJl71bwYlf_aOVxurw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خسارت به ۱۰۰ هواپیمای غیرنظامی در جریان جنگ
🔹
حدود ۱۰۰ فروند هواپیمای غیرنظامی در جریان جنگ آسیب دیدند که تنها ۸ فروند از هواپیماهای عملیاتی به‌طور کامل منهدم شدند.
🔹
حدود ۱۴۰ فروند شناور خصوصی غیرنظامی شامل شناورهای باری و مسافری محلی نیز در جریان جنگ آسیب دیدند.
@amarfact</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/683025" target="_blank">📅 12:48 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683020">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SlEmdc_Kk2n8fmp7uLOfo-CPrbmQhkuo1x7X7HLWhWGlSNotS2cbSF6ZG5i0XXeQoyOjPN1Tw6ev66uHN3OWq8gPOnazjC7cOhzfc6zd24Y5JQU2wVNF6SVJWnEa6inLkdnM97WejvMjfr4m0cpn-AqEfzhpj8sVDXHS-_wrN4HJ4SIbTpdLSUAJskPD4Jl_-uoxqKaNy2CVCsuelozWbSu45Mp7SzY88ZksCccGLQedOBvYjcmqeRvk_aMJIRkPKTTWZY6jr9h5ZkMcXZOluYlXsvBMBQbvbQYHLPMRiTAFkKih9kpY7ICEvYhxUrhL7UX389cOlW2inA4JiY64gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K--CQOQX3yA3seY2YDe9FqvR9pTM9XDtNNVngW1ZLc7FEnZ2QccKdit4Ro5dFUAH7cZe2Ei65abtPK65Qfm3qc5NSAT-nj-oyt8FGYrbNYJO7MV_feSnRdaQfbX6zXujtfKVvczxB5MaghlxPKgWAwYOW_13wYNTsIcOXTHG1J4a6hONs1Dhx0x2UeG6gMpbiwJDQ4lUXV-BxyadUj8TFKe5kYiBy3QZtMQnwuIT-Zq6Qk5tgbegj8ByPCeV_3iv54fGQ7jjnmQ4nRRf6fG506yJ7LNVDcI7lzwNlXzCewJAdfcWL9YRc7Ob_N3Z9d0wB1D1gnpFTT_oeQ7aJr7BUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZfiJCSAPMolXsR4Dys-PIx474BMG6_rRwde6C8hnOIxhDI4OzQrXOD2yNjetAcZPbmsIxkEx_o3NogpWOs7pqi8PtTcit33QxbGcG_-rn_SN0r6LODyn6xlDH0K_POkd3-E0IyUtWPn8GawqTcFmy5cdjtkUTZ_bZlV-7vgGyedJ8I_pAOH6QvKCW70F_tPCTFsd_PYpxXCpzcMcvKvuy8oWyz7sp65BzXEAUcJ9ZCzlyf_VQq4Vj_vUqDdMQ2xh13urucQrWQZCXb2CTywGCSgxz-s1NQa2TxVbwiyWlERjCZenHvUlKzFnUnFvjcVwr8tfHcXel4VOyS0aPa-_1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CekE95DMKd2F-ua4QquQCtGQ4O2e8JGstQZhmHuF5kd21WFFIgvn1cj9Ki5Cz6WYIzUMVauFxrRamlBtDeKDV8DygJ92_0iQynfAUX5ypvVrLOKIL1SkOKrkGC1l_LUHpyc2Rn-Ih-Q9ybKWdCZUpu152sKqoj225cjaiLf6LYajyFsTSFidpo29K6Lv5CIznZI5Q7U-41eJ0Dn-k87fPuVVnt6B28n5JVsUprNdRCthOvyHgnx2A5MiadcM7onwhLJKc8o5r8wafhE3TSJZqSoVmylruWOx3G1Ni9Oa0hv2_LBt_YA7rmHTcIUNTvuMycBR0Qo9QMVe6aQAKNTgNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KfPWN544NpW0fD-NDcRKfrdPVa9Wpp5be38DQA-8qVHQ_eqv-s4fLKcGPdgkMd_6HUyrU5keRhHERVP7yLyUleaf7vHtrAILCbUx5FOZsKM7QA0DfXtcn2DSGcBF-rhlQ6FP6ODhzYMe7HGOiOZ53VrOpDRSHB3QutLKhRMy3saF6II2EaEYv4vh7NCmGqS1joVyHWN1QUHX7d_BMjvJR_3g4o-FwQfwAUjsPsJL2Sk0PgoLYTzE7O0jThkP7PaSvUjws6WryPpF99s3lLi4q9kGtmX2FUnPTrSogd2YlZ2od7zVfCVmRpLy732PbbwmXenfUU-PRp_lF08o5mttUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
قالی بافته شده در عراق - ۱۹۷۰ که نام خلیج فارس در آن حک شده است
🔹
۱۲ سال بعد از دوخت این قالی، رئیس مجلس عراق به دنیا آمد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/683020" target="_blank">📅 12:43 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683019">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سرپرست وزارت دفاع: اجازه تجاوز به سرزمین و امنیت کشورمان را نمی‌دهیم.
🔹
عدم پذیرش کالابرگ توسط میادین میوه و تره بار تهران همچنان ادامه دارد.
🔹
ادعای پنتاگون: ادعاها درباره کمبود مهمات آمریکایی نادرست است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/683019" target="_blank">📅 12:29 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683018">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54b492a859.mp4?token=SgxGgP3KZBUhI_XmbrB6LIqmY_Bii8c3NR8-3hkN46sXFVX1MKw1Wih7qu49ShJ19VnC37gD7_z53JmT78AhGwRD3GTb-n5dnRUEWhzmJPBw3iI79x8W5-xt0N9A0lG28eYGIfobMrSvB2mYhrD26zkpBUA1OvYiaPwRrY3drYyDblKG5Ss6tCwYZk4d6CkpvY-UIE07Ups-WToQeEz3OUPivf9NXNo4Z3--CdgfKoCSIzMjLbA_KB3_ID1Hajh6R6BSkt7X51jLy65b8IGT2eebM-S3ZAxi-163ZHi1LJNJAkXCu4xlbTcZMj3sG9lbalH0A4q4XoIAzdhDelf5yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54b492a859.mp4?token=SgxGgP3KZBUhI_XmbrB6LIqmY_Bii8c3NR8-3hkN46sXFVX1MKw1Wih7qu49ShJ19VnC37gD7_z53JmT78AhGwRD3GTb-n5dnRUEWhzmJPBw3iI79x8W5-xt0N9A0lG28eYGIfobMrSvB2mYhrD26zkpBUA1OvYiaPwRrY3drYyDblKG5Ss6tCwYZk4d6CkpvY-UIE07Ups-WToQeEz3OUPivf9NXNo4Z3--CdgfKoCSIzMjLbA_KB3_ID1Hajh6R6BSkt7X51jLy65b8IGT2eebM-S3ZAxi-163ZHi1LJNJAkXCu4xlbTcZMj3sG9lbalH0A4q4XoIAzdhDelf5yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عبور خطرناک جنگنده از فراز جمعیت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/683018" target="_blank">📅 12:21 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683017">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YuHpfpuQso4eU3jvf2ptoLw6ELcT-lZHcg9skV7NyW8pt6GLf9oNQX6gzn2CB-N0HPOZfS8ITqeSLgkaJak8Inx7CxmrwED-cNGCnUoWzIlhhOerHGdmPNVseDNAZRn_e0mwuGHBj97ckMsWiPluxC8Roy-aX-gTXTmyrWDd9uCnCK2pld1aeoGXB3ArLMP-acEhxoO14yjx5Elgo1PMD7yYcWvKg-Y0WzIHqZp1vSiS6wFGtDFi5AUiAa7icgaEU8WW1HNqNdaVIT-vfz667lFWlwB5FcVOcmCCidujOoV83CCh_KZxEsDaGpn46SzmBQSAk6Fdyq7qsbmwGL5ksg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ای‌بی‌سی‌نیوز: FBI از احتمال حمله پهپادی ایران به کالیفرنیا خبر داد
ادعای ای‌بی‌سی‌نیوز:
🔹
پلیس فدرال آمریکا (FBI) در روزهای اخیر به ادارات پلیس کالیفرنیا هشدار داده که ایران ممکن است در واکنش به حملات آمریکا، با پرتاب پهپاد از سواحل غربی آمریکا دست به اقدام تلافی‌جویانه بزند.
🔹
ایران ظاهراً در پی آن بوده است که در صورت انجام حملات آمریکا علیه ایران، یک حمله غافلگیرکننده با استفاده از وسایل نقلیه هوایی بدون سرنشین (UAV) را از یک شناور نامشخص در سواحل سرزمین اصلی آمریکا، به‌طور مشخص علیه اهداف نامشخصی در کالیفرنیا، انجام دهد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/683017" target="_blank">📅 12:12 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683016">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBr2NP3eMs4ubmf45VaaY4FLt9e-ZFoiGtaZJ5TAC8na0f2bmh_dTM81ofpp6wfEpsfwoL3uEgCs-8AY1LsWb7lNhacNrl06QDyQCf9yT4t8KyKKsyxYyyJ8Q_TyA89VoBCkZsyx4JM14esaqVVh2LihU-seYgolowLduZwDUMtUD817C8oOxFOnCQMULST8zH0dxqT4ObFRHcA86sPhR_hhfvlnGPjBweHKr16fNrXq84SXEw1NUcutpeex2oCzYqxaWpkPXelu6WWCqi7u4hcgH0glIsqVVvvUqnyacKdbQNdtKeG-wo7zTi8pBPN9tVt_nsLSf2ILzjg5f_qEcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نوسان قیمت نفت برنت در ساعات اخیر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/683016" target="_blank">📅 12:10 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683015">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f30a0037e1.mp4?token=Lz5sVQf8hZUGhDVTpthU611Kr9vw4Xt-N_u7YNiLprl6Kg9MR52IubnSBuYgUvh-HxUTtDIxeXvX7iby_Rs5IpWow0OZQagGIaS09167kUoO3Whfl6a9Dy2WuBWuvvXJ6htYcBsTn-Ih1Ygkm4x3CV6d-Lc1Of5wcL-g_Fz8-3DwgXbQGL2CiscURsir0X2ZezrSpLDAiY6jCxdZwo7Lm3ULv1kJ8ZGcQgPxsbi0PegC6C76vr6tj9ApzatRUVNQzS92s7rDAPoR-Z-C41l2-OVM0FJ9DfFeNqxkcIfOS-6NcFlfaqteR_D3RH6mhFkk5tXEa6slsdrfQ6Eh44MkoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f30a0037e1.mp4?token=Lz5sVQf8hZUGhDVTpthU611Kr9vw4Xt-N_u7YNiLprl6Kg9MR52IubnSBuYgUvh-HxUTtDIxeXvX7iby_Rs5IpWow0OZQagGIaS09167kUoO3Whfl6a9Dy2WuBWuvvXJ6htYcBsTn-Ih1Ygkm4x3CV6d-Lc1Of5wcL-g_Fz8-3DwgXbQGL2CiscURsir0X2ZezrSpLDAiY6jCxdZwo7Lm3ULv1kJ8ZGcQgPxsbi0PegC6C76vr6tj9ApzatRUVNQzS92s7rDAPoR-Z-C41l2-OVM0FJ9DfFeNqxkcIfOS-6NcFlfaqteR_D3RH6mhFkk5tXEa6slsdrfQ6Eh44MkoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آغاز «فرمول یک آسمان» در ایتالیا
🔹
مسابقات جهانی پاراگلایدر در ایتالیا با حضور ۱۵۰ خلبان از ۳۳ کشور آغاز شد؛ شرکت‌کنندگان باید مسیری حدود ۱۰۰ کیلومتری را بر اساس نقاط GPS طی کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/683015" target="_blank">📅 12:06 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683014">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hw33k0QmzKbLbYa5u_f4cWZ3-fI-5YyN0QcR8QpHbqmWAVQFGXHC_CwLnqOEyiqW5Ftz7aWAIm4Iw9ohfQhg9yCsAZ_lzbH97jRYnc9BiAXP5TqZajkihI2SKOwOndXMK6EKdGh2DAT6_AOVPqkGpnmVcgYmAwM4t5h_R_xQVMPTbGIj_lV8BcZ8F8VyvfiCnL6zb4y-fuc7Co-MBCXzHuaoiM6eGSR6iI1JCYazIKZOzYWYd_llqDQmOlSO8lpVJNZcT3JABWoL_nT9QbcZ_u1LN_quM6D42gvlu_DebMbs60voQ2YSW2xv8rqVQv7ekiwI7b2YDbC9l_ZTInTdsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رشد ۴ برابری قیمت موبایل در یک سال
🔹
افزایش قیمت تلفن همراه در یک سال گذشته، بازار موبایل را تحت تأثیر نوسانات نرخ ارز، افزایش هزینه‌های واردات و محدودیت‌های عرضه قرار داده است.
🔹
به‌طوری که قیمت برخی مدل‌های پرمخاطب طی یک سال دو تا چهار برابر شده و دسترسی مصرف‌کنندگان به گوشی‌های اقتصادی و میان‌رده را با مشکلاتی همراه کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/683014" target="_blank">📅 12:04 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683013">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ea40a0464.mp4?token=HF1dPgH_ztXqUjPO23DFmA19DML_ytkvGxgtT5JaP7NIvQ5p0VgsGaS6XLjHa55vDorca9hiSytX1IX0CgxK1uDPkoH_6b_kGdr8mDE07hIq9JMpc_7j40qFtwp6Yhf-Rj-4b6E2VaxyKZ49xoijFUlSRXYNpCAPdsI-eWc-rXs3JwdN75X9yzfZqNtJ-5FBntPBPSQy4Kc5bnHe68JlfKzqYb1YNLxCX6n1HG5BSEKzcW-SN46JVooVQk07dk5xeEStKCYgcO9no5CgalYKVBUFMxRO6iSPlmOTGDFHM3DrQHBms7UREPTpbprWK7smEGDK4TeUkFnJqaL91DRU9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ea40a0464.mp4?token=HF1dPgH_ztXqUjPO23DFmA19DML_ytkvGxgtT5JaP7NIvQ5p0VgsGaS6XLjHa55vDorca9hiSytX1IX0CgxK1uDPkoH_6b_kGdr8mDE07hIq9JMpc_7j40qFtwp6Yhf-Rj-4b6E2VaxyKZ49xoijFUlSRXYNpCAPdsI-eWc-rXs3JwdN75X9yzfZqNtJ-5FBntPBPSQy4Kc5bnHe68JlfKzqYb1YNLxCX6n1HG5BSEKzcW-SN46JVooVQk07dk5xeEStKCYgcO9no5CgalYKVBUFMxRO6iSPlmOTGDFHM3DrQHBms7UREPTpbprWK7smEGDK4TeUkFnJqaL91DRU9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ساعات پایانی...
جشنواره ۱۰ سالگی "چرم مَنطِـ"
✨
تا %𝟴𝟬 تخفیف
✨
«تمامی محصولات»
➕
𝟮,𝟬𝟬𝟬,𝟬𝟬𝟬 تومان هدیه اسنپ‌پی
با کد: PAYZ63R
حضوری و آنلاین
👇
🌐
manteofficial.com</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/683013" target="_blank">📅 12:01 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683012">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ouT7AelUuh1jkEG4t9qZxWyv7NHEPJ6E4Ei_qqliaQTkFVKBWG5KDK9v4POV4ESyBqlBU5J3PkSd9tQMIHPTmV_jF_idLp0djz6vlXnJOmnB8ZAQ-EXyKI_uhKxQzcks2NXBsrOvzlP0SFV8zIarvwq6rBfWh4vzsHELCTfLDJYzfbt_SYQsnxj44m4bqmdKsx1WJASPPtdzV_AnpwtUtzi8nkIpCUoNDmh0JMSLPa7yq4JtvVgoBQQwQGk381IsugTlcQLgYUZINrkHf2GnBNDBn9xICiUe-uhOA7IRTYviFee2M0SD6grgU_yGkoq6fFiFHg1G2fA9GNdhuEtklw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پلتفرم چینی Bilibili برای رقابت با یوتیوب وارد بازارهای جهانی می‌شود
🔹
سرویس Bilibili که رقیب چینی یوتیوب است با راه‌اندازی نسخه بین‌المللی اپلیکیشن خود در اندروید و iOS، به دنبال جذب کاربران و تولیدکنندگان محتوای غربی است.
🔹
این شرکت قصد دارد محتوای چینی و جهانی را در یک پلتفرم ترکیب کرده و با استخدام نیرو در چند شهر جهان، فعالیت‌های بین‌المللی خود را گسترش دهد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/683012" target="_blank">📅 11:57 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683010">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQe3W5oIxbV7MYp2XNlEIeWHSCCNk6fT1aB_ngGRJnd6ps_cMxwKR-PgO8uWeU6zmwwWplGBivypDfxrectd4x6hQwD_yKV0IuSM06BeZ_P2JzNXAPgRC5Yut-WB44c6ztFjhqClfDG9uBK5v4EcA2vmSRfm0ya6CCZZRVZbtrbhuxaUJ-r4NGvqHqU7XqkhH5O4Vbi2S8w7UFOG0iOBwja0Tp6e9_l8ZM4hS-DxYdxQ3i50V0eGCMTBPHYspDb_Ps_hnyP5j3B50Uh8zRs7i7h2gccV96-QqJorwolSk006t2t1xl0bciD6vTA_RslbwT6TALzfuor1HRsHavCtrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پلتفرم توئیتر در واکنش به توئیت رئیس‌ پارلمان عراق که در آن از عبارت جعلی خلیج عربی استفاده کرده بود، طی یادآوری‌ای تأکید کرد که نام تاریخی و صحیح آن، خلیج فارس است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/683010" target="_blank">📅 11:45 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683009">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/in_zX0PcppV-lQTjHV1GhfwvbKMHdie6GJME4T5uWLFjevj4IHPMg1gFy2zzX3rCRpglhXmdORXjEQ3ZsZJJGEUArSTf20bNb3QZdl9XUNAD4Fa29kwgcjmM_24cPxEGLKUu_FyomJbQiq2hn5_jCZODOBE8o1suzr6HFdUu4oqMA3YZaLLoCesx-Ko-fpksZ9HdLJmNaydHio-Xk_Zyp__uT-Jjzt2MZjpXFub1yVkNecIfjCAMjbr4h7DsHhPWZQatESbc5BB2KC29mjKCuUmq-aKjAPDW8OGpDK0-OEGkKzx4O1Yyvg2jBfCDkHDFJ-yG38ndtB82F_kyxi6pkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌼
بیعتی دوباره با صاحبِ زمان ( عج)
💚
به مناسبت سالروز آغاز امامت حضرت ولی‌عصر (عج)، در اجتماع بزرگ
«مراسم تجدید بیعت با امام زمان (عج) و رهبر معظم انقلاب اسلامی»
▫️
با کلام:
حجت‌الاسلام و المسلمین سید مجتبی کاشانی و علی‌اکبر رائفی‌پور
▫️
با شعر خوانی
: محمد رسولی
▫️
با حضور
:  سرکار خانم الهام چرخنده
و حسین حقیقی
▫️
با اجرای
: امیر مهدی باقری
📍
وعده ما:
شنبه ۳۱ مردادماه، ساعت ۲۰
میدان شهدا، مشهد مقدس
🤍
بیایید در این شب عهد و انتظار، دست در دست هم، بیعتی دوباره با امام زمان (عج) کنیم...
@Heyate_gharar</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/akhbarefori/683009" target="_blank">📅 11:43 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683008">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
واشنگتن‌پست: ترامپ ناکامی مقابل ایران را بر سر عمان خالی می‌کند
واشنگتن‌پست:
🔹
ترامپ به طور فزاینده‌ای متحدان را هدف حمله قرار می‌دهد، چرا که پیروزی در جنگ با ایران دست نیافتنی به نظر می‌رسد.
🔹
از آنجا که قادر به وادار کردن تهران به تسلیم نیست، به نظر می‌رسد دونالد ترامپ، ناامیدی خود را به میزان بیشتری بر سر عمان و دیگر شرکای آمریکا خالی می‌کند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/683008" target="_blank">📅 11:42 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683007">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
خودرو جدید محمدرضا گلزار در خیابان‌های تهران؛ رولز رویس!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/683007" target="_blank">📅 11:36 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683005">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fNJWrtBPT00UQr-Z3oO7VWvNTUoVbHfntap9lSRk9-xeRB9EQrhFm9tlwjteaqagCY6sXGF8upBUgamvFOBcGzn2ugNwEhHko4r1fiE6M39_KI0-MEWLdX5omTeSk7c_vAFcCOLZExH-1Vqg-OWxtolIxSPgk7I3nBRHfA1Mj5VaivXOLRDwW4G38FXvji0XCBjKl4ftUy635QkNqdAg5vsIzrSocjaPbLqOv4FtHyZAQnwKhava7oNOWM-rsQ-HIfwaN08OXHtzC6rw6xI08HM5oeE-opZN2NMXysrrL-JgL1gCrinnWgNbH6d7buOnjdJUg9hffAfA5Htc-ZRnFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مجید شاکری: پاسخ نظامی ایران به حمله اقتصادی آمریکا ضروری است
🔹
هم معقول است؛ هم به موقع.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/683005" target="_blank">📅 11:29 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683002">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQXOfzfA6LU0AtvdNGS6yy9sW02_rmU8ijdqtM2UyaqV-uzDwPOYwCPNjsWtcpkYvwdP6cKF-xnYJppfsidAhv9ZRXITEMMxAEO13R51VipFw0e-VI8O1Pfrs0uLhtJJD2ZXRqwJ34XnpKL7HGspm7gZMM5Raw4T7L7a6JIbutHoOTxWQlugG0t6NfLpmUGmoEuM2C3dFXSuptonjdYoeL2fw6lWwIB6AeiAZNmrGmOPgis7w59oEaIPbNVR9gBHKeaTvmvF4TzQ7PAtppXwCGoldOB_GhdciRzfqycdU5k7L5XTGO8hkaQR1dsowa-IJsvQIuTGKt1blZfuyNLWSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت بیت‌کوین از ۷۶۰۰۰ دلار عبور کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/683002" target="_blank">📅 11:25 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683001">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jtuLo6XkfsScl4PPogQUY7nNF8vJOtMzhmPyP3X82eV99sIcS153ceXS7QE-QF9hB18HWY9HEV6pbBoyQGpn_O8Y12XUGaQvMFpZoVYxjht60-n_UIfMJNfJOb-8oebIHrWEs6UflC1ubQ_css5963XVp0ymalU0X6e2PA4yLPObgYbK7r0s3XjrZ-yHiY3HMAEOOxDdwCxF1bq3nexO5EOvbiFC4CLaZhoRuoVXRnJVEQJdz6hCqjEi8ecyIKo7i0mhEyQuoQXwzwpF4aoUOoZiZJQbqBMqkwG9eu-ExANv2jz8ZR6NvQrzodiqtGD7dGQmjquxQSkxG6-RWsbCsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ شیاد مدعی آغاز جنگ اقتصادی علیه ایران شد  رئیس جمهور جنایتکار آمریکا:
🔹
هیچ‌کس به اندازه من فرصت بزرگ‌تری برای دستیابی به یک توافق در اختیار جمهوری اسلامی ایران نگذاشته است.
🔹
متأسفانه برای خودشان، نتوانستند از این فرصت استفاده کنند. بنابراین امروز…</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/683001" target="_blank">📅 11:06 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-683000">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d3fbbb826.mp4?token=C8xHwdMWcNQFMQAx5ML36h-HVN6b2i6JSb5AASZWXtQ5hK6hKrIE154_rdk5wrIhWdAtqkBsUIz98dqjeRC3YStFenykyB_-Eqlzn3epik49TdVfkWRgHFSzPiWQBI0FPWNFkaCPx6OhlpGaJThrauU266JyoYijI55SEWsV3mtEaQkWn3lI4WuKp0QeFeAJFgXKBIhfMgYwMWlfGcl1rKysiYjznHvhmRWWoE80t08YQw_zbW9Kdztz6bzSZGaJ2AXy69h-6JQYNGMdjsRlNkk9-VzNNE3GGeRgoBdd265hIFuV4Yq3KgoJGq9_uRx7STEpvT4V1d_qwRZgQfqzKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d3fbbb826.mp4?token=C8xHwdMWcNQFMQAx5ML36h-HVN6b2i6JSb5AASZWXtQ5hK6hKrIE154_rdk5wrIhWdAtqkBsUIz98dqjeRC3YStFenykyB_-Eqlzn3epik49TdVfkWRgHFSzPiWQBI0FPWNFkaCPx6OhlpGaJThrauU266JyoYijI55SEWsV3mtEaQkWn3lI4WuKp0QeFeAJFgXKBIhfMgYwMWlfGcl1rKysiYjznHvhmRWWoE80t08YQw_zbW9Kdztz6bzSZGaJ2AXy69h-6JQYNGMdjsRlNkk9-VzNNE3GGeRgoBdd265hIFuV4Yq3KgoJGq9_uRx7STEpvT4V1d_qwRZgQfqzKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایمان محمدی، کارشناس مسائل یمن: یحیی سریع از تثبیت ۳ معادله در برابر عربستان خبر داده است/ یکی از معادلات این است که نقض حریم هوایی یمن با پاسخ در عمق عربستان همراه خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/683000" target="_blank">📅 11:05 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682999">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bkyDTly7gfYqE_YmLXrKZo6jdoHC1w7rN_1cUkeuFSJLCbZXtBiPffkqnZ3rPGR43gENRZHj71msEZOABIv2Tl2_CMNpVJ8OcNcrVh9sBKkfylbf6rlT3W7Zo8Haaz58-fS8w5VrGk6aDl32ZikJA5XpW5VF4ugRbxVu1x2ewgCg_HJ0BgRtBBD-Qfsz_iFt7n7X3zQahVURaQlx3-kN9W8ma4Mzg-YiCN-W-6B878kEXgZaKtpN0lFvDziZWi7J2Zn6a6oCZApB_vZHt1DTxX_bq9XMtokDmsZSN1v84D1LfCL5G5kla62MTu_cHrSZist9-toDq_vljz2d1rXb6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌼
بیعتی دوباره با صاحبِ زمان ( عج)
💚
به مناسبت سالروز آغاز امامت حضرت ولی‌عصر (عج)، در اجتماع بزرگ
«مراسم تجدید بیعت با امام زمان (عج) و رهبر معظم انقلاب اسلامی»
▫️
با کلام:
حجت‌الاسلام و المسلمین سید مجتبی کاشانی و علی‌اکبر رائفی‌پور
▫️
با شعر خوانی
: محمد رسولی
▫️
با حضور
:  سرکار خانم الهام چرخنده
و حسین حقیقی
▫️
با اجرای
: امیر مهدی باقری
📍
وعده ما:
شنبه ۳۱ مردادماه، ساعت ۲۰
میدان شهدا، مشهد مقدس
🤍
بیایید در این شب عهد و انتظار، دست در دست هم، بیعتی دوباره با امام زمان (عج) کنیم...
@Heyate_gharar</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/682999" target="_blank">📅 10:59 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682998">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
رئیس ستادکل نیروهای مسلح: پاسخ ایران به تهدیدات نوین دشمن ویرانگر خواهد بود.
🔹
نتایج اولیه کنکور ۱۴۰۵ اواخر شهریور اعلام می‌شود
🔹
الجزیره:چین احتمالاً واردات نفت ایران را با وجود خطر تحریم‌های ترامپ به صفر نمی‌رساند.
🔹
معاون وزیر خارجه روسیه: حتی توافق ایران-عمان هم تنش‌ها در تنگه هرمز را از بین نمی‌برد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/682998" target="_blank">📅 10:56 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682996">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c13095e93.mp4?token=JB5wyj-wIsRCPrXZtD0ffE6sgQ9WkUILVwG-BEsjekBpitn0HB1gCt58xi5yp1K4t2Sx6--QXi3J04whOJaE2zVn8A_jDZj7duUh6LDRkRvcmZOs22VONtVt4M6nVmtMxdy2BDFpBROjlrLQrhqdA7QG0barHrNicP6JQNl-dS7QRoPnI0KM6YjU-6WatczT5irMk0wtV51xUOtskaTtrlckU_Lp3SCcehIUJ8-y-VN4NnPAWWBdgiPRtQohRoeYgVdAhy88FjquZlmGC8_6rtDhTEhPhfrrbYAmBl_Dnr5Rm2X21DMNTlG3ERK08lM9UqUHeJHZmH46eoiEa5oWkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c13095e93.mp4?token=JB5wyj-wIsRCPrXZtD0ffE6sgQ9WkUILVwG-BEsjekBpitn0HB1gCt58xi5yp1K4t2Sx6--QXi3J04whOJaE2zVn8A_jDZj7duUh6LDRkRvcmZOs22VONtVt4M6nVmtMxdy2BDFpBROjlrLQrhqdA7QG0barHrNicP6JQNl-dS7QRoPnI0KM6YjU-6WatczT5irMk0wtV51xUOtskaTtrlckU_Lp3SCcehIUJ8-y-VN4NnPAWWBdgiPRtQohRoeYgVdAhy88FjquZlmGC8_6rtDhTEhPhfrrbYAmBl_Dnr5Rm2X21DMNTlG3ERK08lM9UqUHeJHZmH46eoiEa5oWkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دوش رایگان برای پارک جلوی پارکینگ!
🔹
یک مرد استرالیایی برای جلوگیری از پارک خودروها مقابل پارکینگ خانه‌اش، آب‌پاش مجهز به سنسور حرکتی نصب کرد تا مزاحم‌ها را خیس کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/682996" target="_blank">📅 10:48 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682993">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66d822e31e.mp4?token=n9CAOLeI66I4MULNdQ-NyMj3Bhg5cptxHSS7R6zuVXHntgVN63rWseeoqTwu6N_t2LerHNcLxnOiFBfTJEhIlhrfzCAE9xHFc6sTur5Hk6zkGP0l0xz8RtPAvgXg_-omH9l0fyhNA1tn534pRNOGU4BidWx7enMwR-KifPrX-r--oyOjQou_m3VVrr6MjE-4bw7bLmRGWLV9So2KmIAE5FdQ1ZH-i4xygXpD2LUS2m131kEDDM8al_2RrcBhSkCMg0tAhchVBsVMolCKLDznDWC6TfTVKD3SWS42Ufoo58dWh7s0K_Jz8Zaagx2Cu8C_Ot4MauzMj05gOiHsVVdtow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66d822e31e.mp4?token=n9CAOLeI66I4MULNdQ-NyMj3Bhg5cptxHSS7R6zuVXHntgVN63rWseeoqTwu6N_t2LerHNcLxnOiFBfTJEhIlhrfzCAE9xHFc6sTur5Hk6zkGP0l0xz8RtPAvgXg_-omH9l0fyhNA1tn534pRNOGU4BidWx7enMwR-KifPrX-r--oyOjQou_m3VVrr6MjE-4bw7bLmRGWLV9So2KmIAE5FdQ1ZH-i4xygXpD2LUS2m131kEDDM8al_2RrcBhSkCMg0tAhchVBsVMolCKLDznDWC6TfTVKD3SWS42Ufoo58dWh7s0K_Jz8Zaagx2Cu8C_Ot4MauzMj05gOiHsVVdtow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روش خنک کردن کارگران در دمای ۶٠ درجه عسلویه
#اخبار_بوشهر
در فضای مجازی
👇
@Akhbarboushehr</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/682993" target="_blank">📅 10:18 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682992">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZC2rk10yGOr2PBg2I-P0sKpTodqfXbArphJB3m9JqyAJDFwb0NyNoqkiGYNo40yLyy-xl9gz6RdLMlgP_QVPzCjVh-1xajhghFC9kc56ZBd7dZywlIdJqb_V6DnUy4KBQDN0-uGgB-I2VlP1_1mSt06KQbyw6GjXqUwnHmQCEEcJlxMLtWCymxLHpducV1exaB4x0g1VuhG7IVZhOPm2RsfYHdpMK7XasyeC_pt9jpEvWgxwZFZRUdw5-1LQHd9aNfZTLGdh3xdRKYeKvUCMju1o4QdTQHLfo3Mx-j2HcmhFviMYnj9eX7rUtN1nX0zEpbkkkNzFCPbUo9ZkMgiEDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تکذیب شایعه بنزین ۸۰ هزار تومانی از سوی دفتر معاون اول رئیس‌جمهور
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/682992" target="_blank">📅 10:13 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682991">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JS3jVbc592u52QDi8071FdEqKTmpcDcNYLjSwcG1oYhnFEJaCOCTS7uo6w0vf9iYVdj3hPCnzfG0EvJYm8kzc5SsLY2UMpxTcyFtUd08-rMgIfPoxNypMXufdgs8tiaur4egpKOIKHaYajiK6UM7N4KTdmGCfmOxPh3Atb4qOtl7-F9HjOxJkhDzX5DMif_v3obzckNRmu2hSqnoYR_CrPhBo6UdpK5CRv_EIQ0XOIzn-fMkjNM4mM7cHTaVAdTtXuD4UJMu9mERcWib7TfDCyZqtZXnmBS1ZeeWyrY2cYZzduw_QbP2edYZowpz6VnTsuj0uoFlUKiFlMna0BIDLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
عکس جدید رونالدو در ۴۱ سالگی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/682991" target="_blank">📅 10:11 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682990">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02620d3034.mp4?token=YR0ZUZpLdQZRDkgy6Ov2771rECVia1L8rE6rMDZdE7AmomxxQyzYELnLNZWUijBhL1HoXYFyhlI5l-hNmSZ89p6SGiJ6m9WtYXocqjcv-NdtX67ZU2DHoKMNm7WyflhQPpFBlwkUYdmfs2pPZ8ZdZcwiBoxpXbjpD3sz8CrUlHtqeyQ9zJo2dSz1ATK7JRMz4ymLMEFVcg8k3gyMP1puKNEBqThdslnyrdSJhiPlr7tQR4VaNkWwsLEg8Cpy14ae-ZtiMmBROfZTj9V5V2ZVuwx1Xybu4mivlbTVfLXvIgRqMHTpdFCh1N16BMlYKXS7ONB5khN7lfEZMk_5SaotPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02620d3034.mp4?token=YR0ZUZpLdQZRDkgy6Ov2771rECVia1L8rE6rMDZdE7AmomxxQyzYELnLNZWUijBhL1HoXYFyhlI5l-hNmSZ89p6SGiJ6m9WtYXocqjcv-NdtX67ZU2DHoKMNm7WyflhQPpFBlwkUYdmfs2pPZ8ZdZcwiBoxpXbjpD3sz8CrUlHtqeyQ9zJo2dSz1ATK7JRMz4ymLMEFVcg8k3gyMP1puKNEBqThdslnyrdSJhiPlr7tQR4VaNkWwsLEg8Cpy14ae-ZtiMmBROfZTj9V5V2ZVuwx1Xybu4mivlbTVfLXvIgRqMHTpdFCh1N16BMlYKXS7ONB5khN7lfEZMk_5SaotPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک بشقاب غذا شاید جسم انسان را سیر کند؛ اما یک رفتار انسانی می‌تواند روح انسان را سیر کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/682990" target="_blank">📅 10:02 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682987">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cffd8d88c.mp4?token=t6kjf7sivjul_9HnURns4o-dUWv0KmvVFsfHCS4_TTGjCFFjavTRSOTd10KY9YqibUPLJQQHgu7kEdNPdnIdTVaAIYC8xCdmz3NWl3sbDvFmMcVVpuNLiNq-0j-ninhl5PFxZoCivQU-34MEkWseXCmmRIK0YYl4QkQan7z-X-rItOK6zPC2xabBu5HSB2EuQxZzBIBSdY6VpcNk4Cf64KbZ_c31goLwt-sh1llIpdTDNyJfdNVEX-7fgCKwtgD0lrTDG6WCw0stZQJ78pKaYiKDrzsX-Zz18RNt7V9yyIA7EH5HCECPZe1zIc1Ehv_8h14rmo88VxV43ovzgQ3L9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cffd8d88c.mp4?token=t6kjf7sivjul_9HnURns4o-dUWv0KmvVFsfHCS4_TTGjCFFjavTRSOTd10KY9YqibUPLJQQHgu7kEdNPdnIdTVaAIYC8xCdmz3NWl3sbDvFmMcVVpuNLiNq-0j-ninhl5PFxZoCivQU-34MEkWseXCmmRIK0YYl4QkQan7z-X-rItOK6zPC2xabBu5HSB2EuQxZzBIBSdY6VpcNk4Cf64KbZ_c31goLwt-sh1llIpdTDNyJfdNVEX-7fgCKwtgD0lrTDG6WCw0stZQJ78pKaYiKDrzsX-Zz18RNt7V9yyIA7EH5HCECPZe1zIc1Ehv_8h14rmo88VxV43ovzgQ3L9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حادثه عجیب در کجائلی ترکیه
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/682987" target="_blank">📅 09:48 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682986">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WeXREZt33eC0hB_4q_U1JTOKg0tWEpTUrUcmEMeWUmXAGXQfkmc3Uuo5c0uBlU_8-fZzrFPXeXSJbkjcvNjLB0PeocgUYBFk_BZgsDJ_2g5cwzQk2N04sYTjhjftqY4wSiHzYxW5X7DBieSJO_R_-tSYf10YriaaB4q4zfE3frKj4V0RL1XwNAeMnqCfuHxlO4WL2cDWo-lBCSOfK64ITxh9xp4WrzBMgVN5wIYt5B9VCL_DkCK9zVEmdFAstsvoB555WR77ckKufHe9kxVUfGXL21KHX-_YiWcqx49lpquCqHDmbaXfyvLLfNBWqP3MXHoeySEhHzqXClE3zy3_Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
دماوند ساعاتی پیش
🔹
چشم انداز رخ جنوبی دماوند بر فراز دریای ابر و نور چراغ کوهنوردان در حال تردد در مسیر جنوبی دماوند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/682986" target="_blank">📅 09:40 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682985">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcfb012d98.mp4?token=WwPZ_IMOLU5evsxGhw1dLQOT7rvTxaks5Cyuj79CS3-v2iCHLxjBggb1-5-cQlSp03Vf9HUwue9X07UQpKeupznY0Kuy8uVIq0Q2CYslZxemThwgCah5-izTNJiTG_gS9PeUl7aNkk0XIfosswVB-r0FAH_cBtywStjF6Ag1bCbOUTXofChoWPFnlSpytlS8bN8qYkR6yBhkoxoT4zFtrtmGIop9XwEWtpUcyV4MT-1bU7lcd7DCUevKpzhZdGXCmD83Xt4xadPJ_fuOKkmyypmbjJxGLJYup0_M4PcLkrNgyVyA74bMdVaMya8WzWfZjr6CjL6k_3A9OsPO85wnlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcfb012d98.mp4?token=WwPZ_IMOLU5evsxGhw1dLQOT7rvTxaks5Cyuj79CS3-v2iCHLxjBggb1-5-cQlSp03Vf9HUwue9X07UQpKeupznY0Kuy8uVIq0Q2CYslZxemThwgCah5-izTNJiTG_gS9PeUl7aNkk0XIfosswVB-r0FAH_cBtywStjF6Ag1bCbOUTXofChoWPFnlSpytlS8bN8qYkR6yBhkoxoT4zFtrtmGIop9XwEWtpUcyV4MT-1bU7lcd7DCUevKpzhZdGXCmD83Xt4xadPJ_fuOKkmyypmbjJxGLJYup0_M4PcLkrNgyVyA74bMdVaMya8WzWfZjr6CjL6k_3A9OsPO85wnlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پترائوس: پایگاه‌های آمریکا در خاورمیانه دیگر قابل استفاده نیستند
فرمانده پیشین سنتکام و رئیس اسبق سیا:
🔹
ایران اکنون توانایی‌هایی دارد که پیش از این نداشت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/682985" target="_blank">📅 09:38 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682984">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2abae3341c.mp4?token=RFAkOF3PA2IeT-cm0C2Nrz2BTJOkYMrTVMUYlcaQr9dx_78ZfTo9eK1C3DZyt3hh3en3K0-ILfLheKF7726m0tYRzzmMqdxFc2jSMH4wFlkRcdBQlpA53QIZteClTaF1V-WyFO0E_dvDnMBxIMT8CLINdVvR-OGJyzH-peeMTAP_atVNGszwGaAetdEkftrZzxYssub73vw6mZb5vLvS-55y5kR5dNrTPYUV5IP8EkRpDpPrCFHR-ntS5uw55MMTmglbx-jxuvR9ITi0vx5eQFWUHfJ1Of0IfQqpXvx5bk2at4pUxnSKI8IqTsi--bdq7YtEM4sUsBQsuW5NCn70OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2abae3341c.mp4?token=RFAkOF3PA2IeT-cm0C2Nrz2BTJOkYMrTVMUYlcaQr9dx_78ZfTo9eK1C3DZyt3hh3en3K0-ILfLheKF7726m0tYRzzmMqdxFc2jSMH4wFlkRcdBQlpA53QIZteClTaF1V-WyFO0E_dvDnMBxIMT8CLINdVvR-OGJyzH-peeMTAP_atVNGszwGaAetdEkftrZzxYssub73vw6mZb5vLvS-55y5kR5dNrTPYUV5IP8EkRpDpPrCFHR-ntS5uw55MMTmglbx-jxuvR9ITi0vx5eQFWUHfJ1Of0IfQqpXvx5bk2at4pUxnSKI8IqTsi--bdq7YtEM4sUsBQsuW5NCn70OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فوری و مقوی؛ معجونی که روزت رو می‌سازه!
🔹
شیر نصف لیوان
🔹
کره بادام‌ زمینی ۱ ق
🔹
پودر کاکائو ۱ ق
🔹
موز ۲ عدد
🔹
عسل (دلخواه)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/682984" target="_blank">📅 09:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682979">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4aec1aa13.mp4?token=DtRVkouxvXkN3xfF0NahGubKrxuzQNwNbA-j5eftXBsQcJLp34cMppFG4xD43j7z37ddYHNEDkyJ3zSUZpzko7fSiEL2f9AfnPMzTiNXTziNTt95t8cWRGo8iQJ4tqdTb5qIjcywmJ8AwTtiajoDg96Kw4VInLe2kqYdpGzZ9wGoQgwFDTLCuX3nhszjgSEDwtmFOCI05kzCikR3Ey9mvq3cUHDtRl0rkUvagmhui_QO7fKHBZ0iS_e0nO_Ij6MGk45lteruLXADeaA30l_cAtyZFZhN5o8-U0UES_6UlvDRXJTKb86SWVEZwKBu8je5bzE3vTnPnHEeru6pN9R8xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4aec1aa13.mp4?token=DtRVkouxvXkN3xfF0NahGubKrxuzQNwNbA-j5eftXBsQcJLp34cMppFG4xD43j7z37ddYHNEDkyJ3zSUZpzko7fSiEL2f9AfnPMzTiNXTziNTt95t8cWRGo8iQJ4tqdTb5qIjcywmJ8AwTtiajoDg96Kw4VInLe2kqYdpGzZ9wGoQgwFDTLCuX3nhszjgSEDwtmFOCI05kzCikR3Ey9mvq3cUHDtRl0rkUvagmhui_QO7fKHBZ0iS_e0nO_Ij6MGk45lteruLXADeaA30l_cAtyZFZhN5o8-U0UES_6UlvDRXJTKb86SWVEZwKBu8je5bzE3vTnPnHEeru6pN9R8xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر روزی ۱ دقیقه برای یک ماه walk sit بزنی برای بدنت چه اتفاقی می‌افته؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/682979" target="_blank">📅 09:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682978">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
قالیباف: ما هر چقدر قدرت نظامی داشته باشیم ولی اگر مردم گرسنه باشند و گردش مالی و رشد اقتصادی نداشته باشیم، دوام نمی‌آوریم
🔹
امنیت و اقتصاد لازم و ملزوم یکدیگر هستند؛ اگر امنیت را برقرار کنیم و تداومش را با اقتصاد پیش نبریم پایدار نخواهد بود
🔹
ما به عنوان یک رزمنده، بیش از آنهایی که حرف از صلح می‌زنند، قدر صلح را می‌دانیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/682978" target="_blank">📅 09:10 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682976">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jPzH9hArpvaa7DdhwOz_V6sIrSrxSInVxyQvwgIxSV7_G_8pL92u5XsYKtpY4qthtcFJdtJtmMdh340nYib7dRHk-pizvdz2B71uqIF5v3U5MTbDiR9ZUG4CeTyDKtHctNe9aU8XWYDnGABL6Aju93k7-l1ukqSlxIOEATVuLTqBg7FnIBan8XOoC7683bM_VuarNgcKDtYpnPwhoyQHn3ABiy3INhK_eCYHAh201k2sC0xg_73dsf9nBUayYoaNVjcX1djX8NoM278COOM2H0gBljgVmXrE5OgxAVmd9XQops_WuV5ntzibye2bBhvr1lSuq-jydEGmQtsCSLbx2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جانشین اینفانتینو از آسیا می‌آید؟
🔹
رویترز گزارش داده که یوفا، ای‌‌اف‌سی و کونکاکاف درحال بررسی استفاده از سازوکار  «رأی عدم اعتماد» برای برکناری جیانی اینفانتینو هستند.
🔹
زدوبند اینفانتینو با ترامپ و پرونده فساد اخلاقی‌اش باعث از دست دادن اعتماد بیش از ٧٠ درصد اعضای فیفا شده است.
🔹
اگر اینفانتینو برکنار شود، طبق اساسنامه باسابقه‌ترین معاون فیفا تا برگزاری انتخابات جدید سرپرست ریاست خواهد شد؛ این فرد درحال‌حاضر شیخ سلمان، رئیس AFC است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/682976" target="_blank">📅 08:58 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682974">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFJ8fL3RRJmZb0vX323JdJHcyK0f_X0WTG2GWYMRW4RpdEu29GME6P_U1XMi3H89wxqMsI6SLPvUX7x8FSYYv2fDiFjkJJg0JlMuLax5bL7MgHLMy8Z6a5GBjkJOb0W3iWcj1LUGuq4ba9uh6srcLx5JNRTVSa8wDlTYuzdXPZ8jqiF9AIpBsXRrj9gX94ycSzpxx4OH9GUD-nqx1o9gzv9FAl0Qc1T0L6VFbeDdjhMaY9uAS1TCN3Tc83ifXUiR_0hYXUFVb9UuZh_csmAAXoktOe0NIGvJpvezmMKlxW5Y0gL4iXV_ybMq4KCbh2430Knt65e5v8iOT3bPhEYLtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برد زنان والیبال ایران در قهرمانی آسیا با ثبت رکوردی تاریخی
🔹
تیم ملی والیبال زنان ایران مسابقات قهرمانی آسیا را با برد مقابل چین تایپه آغاز کرد و برای اولین بار در تاریخ به جمع تیم‌های ۱۰۰ امتیازی جهان وارد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/682974" target="_blank">📅 08:39 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682969">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">#چند_خبر_کوتاه
🔹
رویترز: تعداد کشتی‌هایی که روز پنجشنبه از تنگه هرمز عبور می‌کردند، کاهش بافت و تنها ۷ کشتی از این تنگه عبور کردند.
🔹
رسانه‌های اسرائیل: ترکیه قصد ارسال سلاح به سوریه دارد.
🔹
وزیر امنیت داخلی رژیم صعیونیستی: زندانیان زن فلسطینی باید رنج بکشند و اعدام شوند!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/682969" target="_blank">📅 08:26 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682968">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
آزمون سراسری سال ۱۴۰۵ تا دقایقی دیگر آغاز می‌شود
🔹
امروز داوطلبان گروه آزمایشی علوم تجربی در آزمون سراسری حاضر شدند در این آزمون ۴۵۱۵۲۲ داوطلب شرکت کردند که در این آزمون ۶۹ درصد خانم و ۳۱ درصد آقا هستند.
🔹
همچنین بعد از ظهر امروز آزمون سراسری زبان‌های خارجی…</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/682968" target="_blank">📅 07:58 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682967">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
واشنگتن‌پست: ترامپ گزینه‌های چندانی برای تشدید تحریم علیه ایران ندارد
🔹
روزنامۀ واشنگتن‌پست با اشاره به تهدیدهای شدید ترامپ برای افزایش تحریم‌های اقتصادی علیه ایران «در ابعادی بی‌سابقه» نوشت که او گزینۀ چندانی برای جامۀ عمل پوشاندن به این تهدیدها ندارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/682967" target="_blank">📅 07:53 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682964">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
وزارت امور خارجه چین اعلام کرده است که تحریم‌های ایالات متحده علیه ایران را به رسمیت نمی‌شناسد و چین با کمپین جنگ اقتصادی که این هفته توسط ترامپ آغاز شده، همکاری نخواهد کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/akhbarefori/682964" target="_blank">📅 07:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682961">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lU1FEusBxAT9fMtrs5rn5ol7qp1yQPVfo4eQL4AiQm-jDIH6mmcYOALxMwXUabUUqkZZCLQkv0aLFOeHu7Hi0LkGKtdZlreedZKsLTl_M9MG8jM9cAXf7ahvFvU9rwWmr25WB4D_HDFdujYtOLU3Ilk_wJvp8SCnkTBU6adlym0d5OPoU9IDi9XW-GrOvLHSV1Xfpl3ArE5-KKFlu8lHobAYxsq6rLphIZ_KtAIEJfB8s14BTUtqEtJamTPOYdf8SJpanuiuvts_6IBDqI3tH8YFfBNhjJs7rghZ3Rs7xbrHTDN5TejiaMnlbxkQK_9-5tHZsrdNWuk2LArYHBHRRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جاه‌طلبی بی‌سابقه ترامپ برای ثبتِ نام خود بر یک ناو هواپیمابر آمریکا
🔹
نیروی دریایی آمریکا در حال بررسی تغییر نام یک ناو هواپیمابر در دست ساخت است که قرار بود به افتخار «دوریس میلر»، ملوان سیاه‌پوستی که در جریان حمله ژاپن به پرل هاربر به قهرمانی مشهور شد، نام‌گذاری شود.
🔹
سه منبع مطلع گفته‌اند که در دولت ترامپ، بحث‌هایی داخلی درباره تغییر نام این ناو و احتمال نام‌گذاری آن به افتخار خود ترامپ مطرح شده است. چنین اقدامی بی‌سابقه خواهد بود، چرا که تاکنون ناو هواپیمابر آمریکایی به نام رئیس‌جمهوری که در قید حیات و در حال تصدی این سمت است، نام‌گذاری نشده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/682961" target="_blank">📅 07:36 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682960">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEVcff4_MguixeRsx0OuR0y4gx1uL8T_xbPtmGZQZ_A-r0gjgEfIbHSsPH4pD17r8ArgbjPvDeDtn7hE0fQIUG7rQGyVenpJ_qqPOW_cONpPIpx0wX2tb7NV16i70zpFRmWd2VvVSJBlXz6Nc-PLsJgl01GYzjtCX28_1LtDr5KW_6TM27LRNrAIpTez_5_dWJpt-Lpz9WsOplmyFRz9c1RKgdYSMLMpnenthuUj7Rfe61Amk1FI99HCtSaJFYQkF9v4dooUZeSsISWKEjtwA3O7nm8ZW7PkrO-H_SFkpBf-9IjlRJUxDm_Unqu4upI7X_r0avl6o5V01C8g7gDmxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز جمعه
۳۰ مرداد ماه
۸ ربیع‌الأول ۱۴۴۸
۲۱ آگوست ۲۰۲۶
جمعه‌ها
#دعای_ندبه
بخوانیم
⬅️
متن و صوت دعای ندبه
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/682960" target="_blank">📅 07:30 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682958">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b985c5d06.mp4?token=GTfGqoCYfSIRYkO471JS1XVNy6PCeWy2oxX0wKIetjCroZEUdBz9G0y6oJMW961h6G8B4BcZiDNCynGRv2zj85rZjmKgVmieOqAdRYuwPN8r6mmjTgDEhCs47VtTfayqpAiNifjzWLvoGrhSAY8y4ef6we065ADJfSl_L5LqGIx16FHQgRS8WwwFLXA9aLa2JsbmmFTpeescwoVrfGp3hBAyhXA6AGXvkwzr9cktVLDzMuaD3Px3sDVIyHK7KCedyxr07rjdoKOKjHEz99uBu6iBqYLJwfObMSELSQsCUhuQdiu8YxrHCa14oHjxae_IVnA8ju0D38oV7-9TxGrMz6OrPOSTBD4Z0a3YTt96V3WnlHOT6fyhMaFv433F7KjkDPxmiCm2ieQM5NX4mg6wARY3cOl0pkBbCwf2kJsG_V1gm2buzo8nZu1rSATnFu5ReSUAq0_3ofMoPhVnmuF6yUM_QiWLFshBTjaWnNzGjL8TBoUVQQXRQDGr3XzdHH1ag2WR7JBLL2rsbWEFDfNdGXkFu7ITdjhOTSpf8zOVrdbgNnbrR_yWw-v2NreN8UxUEnEgzq2yNhXFXwNMvpdYmO_QUx_j9EXR4N14IVw9YLJNwSP2ZlVauTxEGnxDFSZwbqTYpixD8QbFjpgW6bvp-8Qf9fl3CmA78OLUxQVj6N0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b985c5d06.mp4?token=GTfGqoCYfSIRYkO471JS1XVNy6PCeWy2oxX0wKIetjCroZEUdBz9G0y6oJMW961h6G8B4BcZiDNCynGRv2zj85rZjmKgVmieOqAdRYuwPN8r6mmjTgDEhCs47VtTfayqpAiNifjzWLvoGrhSAY8y4ef6we065ADJfSl_L5LqGIx16FHQgRS8WwwFLXA9aLa2JsbmmFTpeescwoVrfGp3hBAyhXA6AGXvkwzr9cktVLDzMuaD3Px3sDVIyHK7KCedyxr07rjdoKOKjHEz99uBu6iBqYLJwfObMSELSQsCUhuQdiu8YxrHCa14oHjxae_IVnA8ju0D38oV7-9TxGrMz6OrPOSTBD4Z0a3YTt96V3WnlHOT6fyhMaFv433F7KjkDPxmiCm2ieQM5NX4mg6wARY3cOl0pkBbCwf2kJsG_V1gm2buzo8nZu1rSATnFu5ReSUAq0_3ofMoPhVnmuF6yUM_QiWLFshBTjaWnNzGjL8TBoUVQQXRQDGr3XzdHH1ag2WR7JBLL2rsbWEFDfNdGXkFu7ITdjhOTSpf8zOVrdbgNnbrR_yWw-v2NreN8UxUEnEgzq2yNhXFXwNMvpdYmO_QUx_j9EXR4N14IVw9YLJNwSP2ZlVauTxEGnxDFSZwbqTYpixD8QbFjpgW6bvp-8Qf9fl3CmA78OLUxQVj6N0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظاتی منتشر نشده از دیدارهای صمیمانۀ خانواده‌های معظم شهدا با رهبر شهید انقلاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/682958" target="_blank">📅 06:45 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682957">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
دلیل‌تراشی‌های ترامپ برای توجیه شکست مقابل ایران ادامه دارد
🔹
دونالد ترامپ در میانه فشارها بر دولت او به دلیل آغاز یک جنگ ناکام علیه ایران تلاش کرد از اقدامش دفاع کند.
🔹
او بار دیگر مدعی شد که نیروی دریایی و هوایی ایران را نابود کرده است. ترامپ همچنین گفت…</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/682957" target="_blank">📅 06:29 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682950">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
دلیل‌تراشی‌های ترامپ برای توجیه شکست مقابل ایران ادامه دارد
🔹
دونالد ترامپ در میانه فشارها بر دولت او به دلیل آغاز یک جنگ ناکام علیه ایران تلاش کرد از اقدامش دفاع کند.
🔹
او بار دیگر مدعی شد که نیروی دریایی و هوایی ایران را نابود کرده است. ترامپ همچنین گفت که چاره دیگری جز جنگ نداشته است.
🔹
او در توجیه دلیل ناکام ماندنش برای توافق با ایران گفت: «انجام معامله آسان نیست زیرا سران ایران را از بین برده‌ایم.»
🔹
این در حالی است که او چندی پیش ادعا می‌کرد که به دلیل ترور رهبران ایران اکنون آدم‌های کاملاً متفاوتی روی کار آمده‌اند که با او تعامل می‌کنند و آماده توافق هستند.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/akhbarefori/682950" target="_blank">📅 02:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682948">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gYlQzmQok7sjyl3AlhWqkqWGdm5CkM8GiA4QtJeYvZKxuK-hOLzuD0_tbPAuVHKHdonNDoJvWEVDpjHvTjimFM5WRcIPRdAdH4ld6kUrIgnucWXrKDnxipXuBhutR7_aMUBgiQHFeM8sefvEPATjs88ZXAOQubEPD0_QMgCBgtotcJ3FlJ5rllwhIxpEUyzYMFwldJxgGDQrJrZT-ecATSdt0s1yWBhNldJC7fBZtYzNtYQ9OyHfAx19jV-MRf47qkZMSyihfpZqdU3f92OQF8TtBcIhDOZohTLvb-Zn9nNrWsfDInnpe-iP4V7XJfP43NUZPYOP3KQ4vH1vNagX4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
به یاد آن سحرگاه جمعه‌ای که پیکر آقای شهیدمان در جوار حضرت رضا علیه‌السلام به خاک سپرده شد
🔹
ای تازه بهشتِ این زمین دارالذکر
ای آینۀ اهل یقین دارالذکر
ما هستی خود را به امانت دادیم
پس باش مراقب «امین» دارالذکر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/akhbarefori/682948" target="_blank">📅 01:32 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682946">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0655d59c4.mp4?token=eGQxqONekQ9ib64Ny5ZPnl8BwgUBNmeVAyRLx6JM9009LJdEV_SEl1YoabrCMwKNTaFKtbwa9eJXugNgsi64K1v__3_TPCv-fZkMFlZ5WZg4D362vdB_yW0hQLRgtx583OISBiUUfxG9x-tCJHPSdcqyCtsUIGRosrUAGBeIZ7Pqr8UwdroxTtOk6BzWH5nKdYeueGc3m-ba3_Bw2IwGsWXC7xkq_gTlCwo-7mNGXSkEZMbE3ZnoPZyeWZEVFpmgZqgWGBux5QRSVpIIIumNQt7caIX1hYORv6-CoIq3s_VQ6l7-8lOF8O1Ocx6AzpeLH_Cuke2d2Se-TxO1VtQhxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0655d59c4.mp4?token=eGQxqONekQ9ib64Ny5ZPnl8BwgUBNmeVAyRLx6JM9009LJdEV_SEl1YoabrCMwKNTaFKtbwa9eJXugNgsi64K1v__3_TPCv-fZkMFlZ5WZg4D362vdB_yW0hQLRgtx583OISBiUUfxG9x-tCJHPSdcqyCtsUIGRosrUAGBeIZ7Pqr8UwdroxTtOk6BzWH5nKdYeueGc3m-ba3_Bw2IwGsWXC7xkq_gTlCwo-7mNGXSkEZMbE3ZnoPZyeWZEVFpmgZqgWGBux5QRSVpIIIumNQt7caIX1hYORv6-CoIq3s_VQ6l7-8lOF8O1Ocx6AzpeLH_Cuke2d2Se-TxO1VtQhxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترفندهای کشیدن نقاشی سه بعدی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/akhbarefori/682946" target="_blank">📅 01:08 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682945">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NIbLD1euGoHSVpT3LG0I-a391wiEPlV2gwX_albnNEcT4U5e0xEi-5pPD0OPjk9mPYd4DMzaDNtb6SGUnTGrOumtHj5YfdkwWVFEMNIj6NxEeuHSoNCv66F6B8uF22AZCWbVW46UaD1WomGzgU1rU5HCrw81HczWgIZoLkKkObXNLtIOMeM-c8FrP0E2u27T_7EGxMXb7Io7bfMUA86fBN2cI_F0uTgFQ_Ekig0CAMdz4Y9P08mRJN4rmuTAONtB6VWjGPc8_ZeoEoEoLJftjeO7Ih-3ll_speFCOOVmLIRhpN-m9I7l0sBvqltWeMIyXdxfuOemSLao9vhDRcGHbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محمد مرندی در واکنش به پست ترامپ: جمهوری اسلامی فرعون را به زانو در خواهد آورد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/akhbarefori/682945" target="_blank">📅 01:03 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682944">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e460f436ee.mp4?token=T5Crn-TSUZgvlr_lBgTBv6G8y9Ux3dAJGvbFQUVkqf6iOrf5i64i5jqsqAyhyc2s9BWObvL1U0fnpZ2PCEUk_V9eTa0ni_PFQ7OURMUaFnoJyx539BqJ2vIvdLyU8aE0NooF1Hl7bht3VyT4MkKWJVMGRlzPTsJRZgLkzHvhU9u7Kj5quauaMMMHvWLWsAnc35E9ojh1S_BWcRBb6H3jGX3hCR0C8kk-op-TE3pCCHGtArhsPRPySDzAQTUtz7zhLxKfcjlRUQ8rigq8jTOzP_0oM2FohyS0q6qxW4UzfkToYQ8WyvPe08Hewj2jBl2C7OQ6tloW0gnqxSuLPT9AaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e460f436ee.mp4?token=T5Crn-TSUZgvlr_lBgTBv6G8y9Ux3dAJGvbFQUVkqf6iOrf5i64i5jqsqAyhyc2s9BWObvL1U0fnpZ2PCEUk_V9eTa0ni_PFQ7OURMUaFnoJyx539BqJ2vIvdLyU8aE0NooF1Hl7bht3VyT4MkKWJVMGRlzPTsJRZgLkzHvhU9u7Kj5quauaMMMHvWLWsAnc35E9ojh1S_BWcRBb6H3jGX3hCR0C8kk-op-TE3pCCHGtArhsPRPySDzAQTUtz7zhLxKfcjlRUQ8rigq8jTOzP_0oM2FohyS0q6qxW4UzfkToYQ8WyvPe08Hewj2jBl2C7OQ6tloW0gnqxSuLPT9AaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ساخت کیف پول و کارت با چند تکه مقوا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/akhbarefori/682944" target="_blank">📅 01:00 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682941">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
سالی یک متر از آب دریاچه ارومیه تبخیر می‌شود
محمد کوهانی، دبیر ملی شبکه‌های محیط زیست کشور در
#گفتگو
با خبرفوری:
🔹
سالانه حداقل یک متر تبخیر از سطح حوضه آبریز دریاچه ارومیه را داریم که طبیعی است. اکنون تراز دریاچه به ۱۲۷۰.۹۳ متر رسیده که نسبت به سال گذشته، یک متر و ۱۳ سانتی‌متر افزایش داشته است.
🔹
همچنین وسعت دریاچه با ۲۸۵۰ کیلومتر مربع، نسبت به سال گذشته ۲۲۴۴ کیلومتر مربع افزایش یافته است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/akhbarefori/682941" target="_blank">📅 00:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682939">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZ0jTfUliz_EeDtDTJEN5n6yow7LdFokZW0-GB8qpbljLmIbdOU1FKxqX4arhEF_VY1ZyZC2sl-6uYkozxSLibpGF4lDoyuiqs5AvCrtr0yKR8SXftLoggjLSVJGUMEEOjnoXlVI8L6P8zmo_Az6S5CG3Sc3ndh74YRBFWjKqrckkXkmUlUM2v_Q-BSqh4ZKhss_KGm8qIaOmzTYMoEUs-EzgcHndBnR7eT9S1vaueNPIQoRbRDTrGPTCsTUM79KspZzMXZncXp33qj_qvYtSTlHoXoyJ6X-oabhZZ7xD9VlSEBIAv48hfN37xDGSK3aiV2Cql3ZIxwbcXXHdbDQ_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش فارسی آلن ایر، دیپلمات سابق ارشد آمریکایی، به تهدیدات اقتصادی ترامپ علیه ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/akhbarefori/682939" target="_blank">📅 00:29 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682936">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
افشاگر بحران در ناو لینلکن وادار به استعفا شد
🔹
مقامات آمریکایی به سی‌بی‌اس نیوز گفته‌اند که مسئولان پنتاگون در حال بحث و گفت‌وگو درباره برکناری ناشر قدیمی نشریه نظامی «استارز اند استرایپس» (Stars and Stripes) پیش از تاریخ بازنشستگی برنامه‌ریزی‌شده او هستند.
🔹
رسانه آمریکایی نوشته دولت آمریکا به ریاست دونالد ترامپ در حال برنامه‌ریزی برای بازساری کامل این رسانه نظامی است که بخشی از بودجه آن توسط مالیات‌دهندگان آمریکایی تامین می‌شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/akhbarefori/682936" target="_blank">📅 00:14 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682935">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aec764cbf3.mp4?token=Sb7zjjyH4nlaWTwIKMC_G62GB_7vlR-3_R6BCbmhmukhRDuzUvfugAJBnmT_tA7PJFWIrllSteNnAQ88EhpVijlQDufqyPTk4GMwxj9Oks6kjGZsMw07C86FeRj6WsXSxtPNqvsaF5BSDQpa7boFxavL-MX1SKk_WEXYBfH7DtooiNXOt3HhWFwV1iwxhePGaEf6hiGLO-1mkL6jIR9xV6kizJR4UYGxFYNI-UC-Oto-8eFtnaFRQQ5mFb0lc48ghY8ZUxkuQLbhoKhx9id5zsadpikSszPOZKOQSnWYL8BoeAeAjpP3KBnfeIdQgII3BQlQXy7XzVJC9uQTGAbCGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aec764cbf3.mp4?token=Sb7zjjyH4nlaWTwIKMC_G62GB_7vlR-3_R6BCbmhmukhRDuzUvfugAJBnmT_tA7PJFWIrllSteNnAQ88EhpVijlQDufqyPTk4GMwxj9Oks6kjGZsMw07C86FeRj6WsXSxtPNqvsaF5BSDQpa7boFxavL-MX1SKk_WEXYBfH7DtooiNXOt3HhWFwV1iwxhePGaEf6hiGLO-1mkL6jIR9xV6kizJR4UYGxFYNI-UC-Oto-8eFtnaFRQQ5mFb0lc48ghY8ZUxkuQLbhoKhx9id5zsadpikSszPOZKOQSnWYL8BoeAeAjpP3KBnfeIdQgII3BQlQXy7XzVJC9uQTGAbCGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غیبت ملانیا ترامپ از ترس ایران ۲۵ روزه شد!       وبسایت Wonderwall:
🔹
ملانیا ترامپ پس از انتشار ویدئویی که سرویس مخفی آمریکا آن را تهدیدآمیز و مرتبط با ایران اعلام کرده بود، ۲۵ روز است در انظار عمومی دیده نشده است.
🔹
مشاور او می‌گوید ملانیا آرام و قاطع است…</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/akhbarefori/682935" target="_blank">📅 00:10 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682934">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ایرانِ فردا را نسوزانیم!
🔹
بیشتر از یک ماه دیگر، زنگ آغاز سال تحصیلی به صدا درمی‌آید، اما حقیقت این است که سال‌های تحصیلی ما بعد از کرونا، دیگر هیچ‌وقت شبیه گذشته نشدند.
یک روز سرما، روزی آلودگی هوا، روزی تعطیلی و حالا جنگ...
🔹
هر بار بحرانی از راه رسید و چیزی را از مدرسه گرفت. گاهی یک روز، گاهی یک هفته، گاهی ماه‌ها از کیفیت و استمرار آموزش.
🔹
و هر بار، آموزش‌وپرورش آرام‌تر و بی‌صداتر، یک قدم دیگر به حاشیه رانده شد.
🔹
اما مگر می‌شود آینده یک کشور را به حاشیه برد؟
فناوری را می‌توان خرید. کارخانه را می‌توان ساخت. ماشین‌آلات را می‌توان وارد کرد. حتی عقب‌ماندگی‌های اقتصادی را می‌توان، با سال‌ها تلاش، جبران کرد اما انسان توسعه یافته را نمی‌توان وارد کرد.
انسان توسعه‌یافته، محصول سال‌ها تربیت است، محصول همان کلاس کوچک.
🔹
و کودکی که قرار است پشت نیمکت بنشیند، فردا پشت میز تصمیم‌گیری این کشور خواهد نشست.
آینده یک کشور، یک‌باره ساخته نمی‌شود،
🔹
آرام و بی‌صدا، هر روز در کلاس‌های درس ساخته می‌شود.
پس لطفاً آموزش‌وپرورش را فقط یک وزارتخانه، یک ردیف بودجه یا مجموعه‌ای از ساختمان‌ها و کلاس‌ها نبینیم.
آموزش‌وپرورش، کارخانه ساختن آینده ایران است.
🔹
آموزش‌وپرورش این چند سال با زخم‌ها و چالش‌های جدی روبه‌رو شده و هنوز به ثبات و قوامی که شایسته نسل آینده است، نرسیده است.
حالا یک سال تحصیلی تازه در راه است و این بار نباید اجازه بدهیم بحران‌های امروز، آینده کودکان را هم تعطیل کنند.
🔹
مسئولان، پیش از آنکه دوباره تقویم را ورق بزنند، سال تحصیلی جدید را جدی بگیرید.
برای مدرسه‌ها، برای معلم‌ها، برای دانش‌آموزان، برای تداوم آموزش، برای روزهایی که نباید از دست بروند، فکری کنید.
🔹
کودکان فقط آینده ایران نیستند، آنها ایرانِ فردا هستند.
و ایرانِ فردا، از همین امروز، در کلاس‌های درس آغاز می‌شود
.
#سرمقاله
@Tv_Fori</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/akhbarefori/682934" target="_blank">📅 00:01 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682933">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjw2-82zcPNqvbl8J51waMZcAo6I0k9Eu20JweO1bSFx9i6e5a82rJtfcg2au3h2XBoTC8NIRSEVob7MarlQAWcJoU491m9EY6JiqExpy0VxkBNbLTIhBVuoLvVfXPJ-wc9ytmQSZsipdv3-4CrT1Vp7HSJ9uA8UrJbSJOk21kuCDbNv00fJZxMJKckayMMbVuT7jfJa0t2LFI_zUsgEjoPeW7bN21XQzD0ia4-3HrbYYYg9kML1FLzw8z8Q_xtK8RHZ4SMw7JBsyqjYpOFcg1n0BfKj9bYeWjwVQa06vkhNiaMFEsybSNorfmtnmmCWpcjIcIc3UPn_NHugaCMXtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/akhbarefori/682933" target="_blank">📅 00:00 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682932">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a77329d195.mp4?token=biTo6jxz5IzC3kQn6_fMdeOF79T4NxVd9JFSGRxZqmxyI0Jf4bvsGMtt9TUO3nQb5OqvlBrvQqzd2aGNE7qPDWdW0vOmf0N-PBs3X9yaaFwGvS16t1vzcOFNqoYMelvT1yMNwylj5zvQfG4J7hZnDyEw9bOUoj2sgUUHOzE_n-b27LzSLcqVStKlXkVcOiAPXAn_PkECCu0wPi_cnLqg8Zk4gvu9th-Lqc3QVneYEIyjVPj1Po3G6F1kzlggoRnMHSN60b9r9Et6FLS3lB9kG_nzEW4AjHzy9OxBtq96_LefHV7cfGyTzrs_SgMCEIJnNR8WuWqximsO6MLUXFXiJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a77329d195.mp4?token=biTo6jxz5IzC3kQn6_fMdeOF79T4NxVd9JFSGRxZqmxyI0Jf4bvsGMtt9TUO3nQb5OqvlBrvQqzd2aGNE7qPDWdW0vOmf0N-PBs3X9yaaFwGvS16t1vzcOFNqoYMelvT1yMNwylj5zvQfG4J7hZnDyEw9bOUoj2sgUUHOzE_n-b27LzSLcqVStKlXkVcOiAPXAn_PkECCu0wPi_cnLqg8Zk4gvu9th-Lqc3QVneYEIyjVPj1Po3G6F1kzlggoRnMHSN60b9r9Et6FLS3lB9kG_nzEW4AjHzy9OxBtq96_LefHV7cfGyTzrs_SgMCEIJnNR8WuWqximsO6MLUXFXiJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش فاطمه مقصودی (نماینده مجلس) به خبر سو‌استفاده اینترنشنال از بیماران پروانه ای
🔹
کسانی که لوکیشن زیرساختهای ما را به دشمن می‌دادند، امروز شدند دایه دلسوز تر از مادر!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/akhbarefori/682932" target="_blank">📅 23:58 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682931">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
میانگین روزانه معاملات خورد بورس از ۳۷ همت عبور کرد
🔹
هفته پایانی مرداد برای بورس تهران با یک جهش قدرتمند به پایان رسید؛ شاخص کل ۳.۷۷ درصد و شاخص هم‌وزن ۵.۱۱ درصد رشد کردند و به‌ترتیب به ۵.۹۵۲ میلیون و ۱.۶۸۶ میلیون واحد رسیدند.
🔹
در این هفته میانگین روزانه معاملات خرد از ۳۷ همت عبور کرد؛ رقمی که با وجود کاهش نسبت به هفته قبل، همچنان بالاتر از میانگین ماهانه ۳۱ همت بود.
🔹
پول حقیقی هم در مجموع حدود ۴.۵ همت وارد بازار شد؛ دارویی‌ها و فلزات اساسی در صدر جذب نقدینگی قرار گرفتند، در حالی که فرآورده‌های نفتی و بانکی‌ها بیشترین خروج پول را تجربه کردند./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/akhbarefori/682931" target="_blank">📅 23:58 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682930">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcf377f0d6.mp4?token=J1LIMwia6Qkam481EJVJQK9q0rAvW_fG8ByAOyCviB8v53Jfw5Xrk4bNHN6uwLrS5e6ldfz_a9ok4bQs92NVXEXPxge9kqT1fdxIXHmgQkZxcHnG25Ozyr-RBSe9MQd3WTviNbf4QfR_VXwhxkPbQpD7Ct4-HhFQo0oFh2nAUsra8BrwjBS7CPFpvhuZkl9ofbancfWFFZ3p1gOOFzEhfJkPiusLevQEtTzAOmcHYX4DLS3JQ9CeCurfVPvU5-0P-Jh5GM9c_sgcxJi2tTPySJjOCN6dcIHiTIm_5oDHC8L2dW3g9Vc6IxcyDw5fYIOn0DOJMg8sL50m2YEoq-HsQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcf377f0d6.mp4?token=J1LIMwia6Qkam481EJVJQK9q0rAvW_fG8ByAOyCviB8v53Jfw5Xrk4bNHN6uwLrS5e6ldfz_a9ok4bQs92NVXEXPxge9kqT1fdxIXHmgQkZxcHnG25Ozyr-RBSe9MQd3WTviNbf4QfR_VXwhxkPbQpD7Ct4-HhFQo0oFh2nAUsra8BrwjBS7CPFpvhuZkl9ofbancfWFFZ3p1gOOFzEhfJkPiusLevQEtTzAOmcHYX4DLS3JQ9CeCurfVPvU5-0P-Jh5GM9c_sgcxJi2tTPySJjOCN6dcIHiTIm_5oDHC8L2dW3g9Vc6IxcyDw5fYIOn0DOJMg8sL50m2YEoq-HsQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک، کارشناس حوزه مقاومت: با توجه به فشار دشمن، احتمال سقوط بخشی از تأسیسات علی‌الطاهر لبنان در روزهای آینده بالاست/ همزمان دولت لبنان به‌جای تمرکز بر اشغال جنوب این کشور، فشار بر جمهوری اسلامی و نمایندگی ایران را افزایش داده است/ آمریکا، عربستان و رژیم صهیونیستی به‌دنبال حذف و تضعیف جمهوری اسلامی از معادلات لبنان هستند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/akhbarefori/682930" target="_blank">📅 23:58 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682928">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f158b8bc4.mp4?token=NUl8qCOGQU45ome9H-NJ8GV-KfwG32yi8B50W6sRsSt_a0scxO_Mypb1l7Cv3mmxjn-Ja7Xw7_QW8Mybr01m0skrJiazUt0SxvE287wQHa2-dxqATi8VAF9t1elWZWB9EjwwRae0MRTGGtWbJnnaoPKRtbYDr3mixB0bd14vp9LnjDU5qURGGVtwVt1NxyaI9CihpCIb3CX9tulD1IKZqJgh1ucLMTT4hI3uawT7KnDtYx3UJ04oKneEGa9vmc3h1SHPz3j01KieLKMHcwb5I5F4FXF-Fx3chBOvLq2dF0YpiI1Tp2Kcly49ON9SQL5GTV5ne_snf9GIjPFm0SgNDxxXLtflncxcQFNq6kVESpRCx-et9GO6rEGSB6IjjIHd1sWgNNZl-ar8it9zX-UZOWiWBnbBlFSuO8cF5lAZuFXu13xCx1ppUobxf_FVAgx_L6SNFhfv7QEhnwTcYbqd5c_f-XqrzZtDWRChfxiXYLkwjYt556UomghbBaDKdw0dtfwYe4x4uBsMahCEJfZ7c_sKlxO_lff1eL8jSNRaf7gner-sSqOF1O6PF5TComPMaiZ9qulfrozbZ6hcubsgK7IlP4w87fv9Eo6d5vaNDoh_DJYq6pL96sqUcnuluVKi57iXpbn5embIH_DjKlRiBlgwdT9wftOJuSRdmlYE8sE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f158b8bc4.mp4?token=NUl8qCOGQU45ome9H-NJ8GV-KfwG32yi8B50W6sRsSt_a0scxO_Mypb1l7Cv3mmxjn-Ja7Xw7_QW8Mybr01m0skrJiazUt0SxvE287wQHa2-dxqATi8VAF9t1elWZWB9EjwwRae0MRTGGtWbJnnaoPKRtbYDr3mixB0bd14vp9LnjDU5qURGGVtwVt1NxyaI9CihpCIb3CX9tulD1IKZqJgh1ucLMTT4hI3uawT7KnDtYx3UJ04oKneEGa9vmc3h1SHPz3j01KieLKMHcwb5I5F4FXF-Fx3chBOvLq2dF0YpiI1Tp2Kcly49ON9SQL5GTV5ne_snf9GIjPFm0SgNDxxXLtflncxcQFNq6kVESpRCx-et9GO6rEGSB6IjjIHd1sWgNNZl-ar8it9zX-UZOWiWBnbBlFSuO8cF5lAZuFXu13xCx1ppUobxf_FVAgx_L6SNFhfv7QEhnwTcYbqd5c_f-XqrzZtDWRChfxiXYLkwjYt556UomghbBaDKdw0dtfwYe4x4uBsMahCEJfZ7c_sKlxO_lff1eL8jSNRaf7gner-sSqOF1O6PF5TComPMaiZ9qulfrozbZ6hcubsgK7IlP4w87fv9Eo6d5vaNDoh_DJYq6pL96sqUcnuluVKi57iXpbn5embIH_DjKlRiBlgwdT9wftOJuSRdmlYE8sE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هیچ‌جای آیات و روایات نگفته صدای معین و مهستی و داریوش حرام است!
/ تلویزیون اینترنتی مدار
موضع عجیب یک روحانی درباره خواننده‌ها
👇
https://www.aparat.com/v/mkfc6hp
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/akhbarefori/682928" target="_blank">📅 23:54 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682927">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
تولید خودرو نسبت به سال قبل ۴۰ درصد کاهش یافت
محمدرضا نجفی‌منش، رئیس انجمن قطعه‌سازان خودرو در
#گفتگو
با خبرفوری:
🔹
تولید خودرو نسبت به یک سال گذشته ۴۰ درصد افت پیدا کرده که جنگ، نرسیدن به‌موقع مواد اولیه و کمبود نقدینگی از مهم‌ترین دلایل آن بوده است.
🔹
این کاهش تولید باعث شده حتی قطعی برق در تابستان هم فشار خیلی محسوسی به بیشتر واحدها وارد نکند، چراکه اگر برق هم می‌بود شاید کاری برای انجام دادن وجود نداشت.
@Tv_Fori</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/akhbarefori/682927" target="_blank">📅 23:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682926">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73d2f9f680.mp4?token=NYgOZity48dVpueft7ONkt2ZPXqtp6cGHytuaEl8DjJKGWQ-33lrL7WwdDH589T7ifvzYah8LOlH8PymB4CcyiyFf-9Qfg2lfrDzy4CAlGiSAiPWfBZ5WReab70l7Ll1hSm9ly7AxSbHgibQo1JgNASitJcbH8yG9qFmjh3pCkJ3QAIHyIzMEAVuZxKWHluSfyOQlkkjMgjJza3em1ShikPsqY3TmT7D7fBECklQY_eUJzcZVFhK2mcS3Rjjpm50niLIIN3nvpET1sB4FG6VG9vYoricUbwR_hcQHHa8aQq8dzGuIFKNqwCgoASnyVruO6YSO9cn6HVNe949QoqVbXdusokFBNZXcUycs-G2tjIhyIwhZLHEJdbigRk9XfPRsRHn5-ZE1tpOsNM-IJ-MxOC9VQVeCjUgSrarORiwsSJJ9sSmvFi7MgXSgHK6HdHAC0A_wsYCq8uy_oh8RFhw1tLgRZNegT7R-8j0Lz2nFnwury4nA7a6H0IIDFbTzXDWLLaxbxcXfQu8kdQPuKAUjISmWq80QEi5EE1rbvx32VSEHCNbKNIRrtgoT5O3ynq4tvadRGGC12hlFn-3md08Siy81Sqt0dnilym4N67wplWWIXB3IlWPiByq169ltgle8y1BNdSmacsaRs0yksK6af7ESdgADuKW-uFmz2E_euo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73d2f9f680.mp4?token=NYgOZity48dVpueft7ONkt2ZPXqtp6cGHytuaEl8DjJKGWQ-33lrL7WwdDH589T7ifvzYah8LOlH8PymB4CcyiyFf-9Qfg2lfrDzy4CAlGiSAiPWfBZ5WReab70l7Ll1hSm9ly7AxSbHgibQo1JgNASitJcbH8yG9qFmjh3pCkJ3QAIHyIzMEAVuZxKWHluSfyOQlkkjMgjJza3em1ShikPsqY3TmT7D7fBECklQY_eUJzcZVFhK2mcS3Rjjpm50niLIIN3nvpET1sB4FG6VG9vYoricUbwR_hcQHHa8aQq8dzGuIFKNqwCgoASnyVruO6YSO9cn6HVNe949QoqVbXdusokFBNZXcUycs-G2tjIhyIwhZLHEJdbigRk9XfPRsRHn5-ZE1tpOsNM-IJ-MxOC9VQVeCjUgSrarORiwsSJJ9sSmvFi7MgXSgHK6HdHAC0A_wsYCq8uy_oh8RFhw1tLgRZNegT7R-8j0Lz2nFnwury4nA7a6H0IIDFbTzXDWLLaxbxcXfQu8kdQPuKAUjISmWq80QEi5EE1rbvx32VSEHCNbKNIRrtgoT5O3ynq4tvadRGGC12hlFn-3md08Siy81Sqt0dnilym4N67wplWWIXB3IlWPiByq169ltgle8y1BNdSmacsaRs0yksK6af7ESdgADuKW-uFmz2E_euo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پدری که چشم انتظار فرزند کنکوری خودش بود، قبول بشود یا نشود زندگی ادامه دارد/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/akhbarefori/682926" target="_blank">📅 23:43 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682924">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6ce052442.mp4?token=Gc8-siZ2AYUgAQgBVERdxTQ1o4oMr9xJRbzq6gN-pvoKbhfcqGGFbVn8IQFbWSK5kb--6N38qbJUkzJ-3YjYT0wcLuJN1-Ri610V6iU3zAbAC-VfXeKnQGq2COSDUNdeaNC-m_ZPpLhEIvlr8W4EcwoEI2Thbo18G9_rLpO4qc6lHjaauJ8O1T9T7LHAWOIsKo-m4u4Ou-hlBWxeylkMbV__qXylLJjDFYRKOwrzKsbyhqBuVq1DXTw4-6bzdofh84K3oe5ZjYDFD7uNMvR75ViRCaJ8lwV-HOmF5KTyRtt3n6sd_HfAFIp30sCoSTgTFrBNkbYEYEJ8YEJA5uo6nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6ce052442.mp4?token=Gc8-siZ2AYUgAQgBVERdxTQ1o4oMr9xJRbzq6gN-pvoKbhfcqGGFbVn8IQFbWSK5kb--6N38qbJUkzJ-3YjYT0wcLuJN1-Ri610V6iU3zAbAC-VfXeKnQGq2COSDUNdeaNC-m_ZPpLhEIvlr8W4EcwoEI2Thbo18G9_rLpO4qc6lHjaauJ8O1T9T7LHAWOIsKo-m4u4Ou-hlBWxeylkMbV__qXylLJjDFYRKOwrzKsbyhqBuVq1DXTw4-6bzdofh84K3oe5ZjYDFD7uNMvR75ViRCaJ8lwV-HOmF5KTyRtt3n6sd_HfAFIp30sCoSTgTFrBNkbYEYEJ8YEJA5uo6nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صنایع دفاعی؛ نمونه‌ای از اقتصاد مقاومتی
امین طباطبایی، استاد دانشگاه و اقتصاددان:
🔹
ما در تولید صنایع دفاعی کاملاً تابع اقتصاد مقاومتی هستیم؛ این موضوع تا حد زیادی به چرخه تولید داخلی و ایجاد اشتغال نیز کمک کرده است./ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/akhbarefori/682924" target="_blank">📅 23:33 · 29 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
