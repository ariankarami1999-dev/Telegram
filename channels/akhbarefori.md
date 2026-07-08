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
<img src="https://cdn4.telesco.pe/file/M1FT8c7QyAppcfNGFAocN76S4whyyv0zNJNkUqbnCB8EDfv_lTkjnybNV7U87FsLeEHzMLqev9P7gd3mUxL-NXox7mHQNvZbv6_4uKcSv5BWeRYoRmeB-ZdUmqgBBS50bOfj1Nldj_RMu-dn61AgwFqGXJVIKnjiLXjXfoYvZQtkHVsBIMuH8PX8Uko8slLtqa-kvhrhcvZ9o9OYBwY6gV2j1W9zDQdIKQ_a3e_MmB_kZmCPnMdZS-qZZssxXIavVBHUM5RgCQJfLUgS0pYOMIYtmZZ7F6OY578STl-l_-o-M7prEerRbXq5bL7xTkd_UXZuMWYW-WUD7QLUzVDVBA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.48M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 11:13:54</div>
<hr>

<div class="tg-post" id="msg-668343">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6669419bce.mp4?token=VqFBIY5K891oHrd4Zb0Uc_0UFlxjWiMBj3E8-ndXkiufR9SJwRRRqshOXA9fUSfoNcwhFdd_h848SNJJnQ-KI3ENKpU5_7aODVsRGrfq-UZC-Dwnj_tqtSmLkO93SMIIxyNd7ufTT4JwYcTcXaNVTZb71tdmL1uVYaStcmc_UCcI_tyYpGZSdZmZy4GPnf50DHzIun4Yc0LxAz7i0E1QOa5-NQkrvC_vxN-EYd-DK3Dkjv05o9_ONpw1hDoDvDE7cB6q80UJ84yJTpj1R1uSgEwubF7lDY-d2qAQtMfuhPwS6pNNlMU5lQj6QOtGa-fDrAm8Y3E8qTFF-uQlVwWKUWOO1nf3x3YsU-h6tigFRnYJxgVhWfTL0WGA4tTswc7ECf4Q9TX6FkwrXMzeq3jv1mLNwlinFyPl7CJmnKRxGQ7e4AlnPqEsNlla1mwyuB2qckiCU3AVHKr455gE5m6yy2jI0gWr52GLd5zphpMchgL8zLoAGHRw-llsOkMha5D8Qua8xyMl06wmziI6P4vGJJIImHIbQwPE0IsdUWJ6jxVkS2QxmVtdgcsam-DOSFFjdm8TB-5RN3V-Y5deNaWYvwteONGi3Gyyl7orWnKmJaQhwf7TosBAEHtork54j3nWjyyQO5bdGjGgsq8hrSw0mYsqchy0WOavVGaMWj8ioQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6669419bce.mp4?token=VqFBIY5K891oHrd4Zb0Uc_0UFlxjWiMBj3E8-ndXkiufR9SJwRRRqshOXA9fUSfoNcwhFdd_h848SNJJnQ-KI3ENKpU5_7aODVsRGrfq-UZC-Dwnj_tqtSmLkO93SMIIxyNd7ufTT4JwYcTcXaNVTZb71tdmL1uVYaStcmc_UCcI_tyYpGZSdZmZy4GPnf50DHzIun4Yc0LxAz7i0E1QOa5-NQkrvC_vxN-EYd-DK3Dkjv05o9_ONpw1hDoDvDE7cB6q80UJ84yJTpj1R1uSgEwubF7lDY-d2qAQtMfuhPwS6pNNlMU5lQj6QOtGa-fDrAm8Y3E8qTFF-uQlVwWKUWOO1nf3x3YsU-h6tigFRnYJxgVhWfTL0WGA4tTswc7ECf4Q9TX6FkwrXMzeq3jv1mLNwlinFyPl7CJmnKRxGQ7e4AlnPqEsNlla1mwyuB2qckiCU3AVHKr455gE5m6yy2jI0gWr52GLd5zphpMchgL8zLoAGHRw-llsOkMha5D8Qua8xyMl06wmziI6P4vGJJIImHIbQwPE0IsdUWJ6jxVkS2QxmVtdgcsam-DOSFFjdm8TB-5RN3V-Y5deNaWYvwteONGi3Gyyl7orWnKmJaQhwf7TosBAEHtork54j3nWjyyQO5bdGjGgsq8hrSw0mYsqchy0WOavVGaMWj8ioQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تشییع باشکوه رهبر مسلمانان جهان، حضرت آیت الله العظمی امام خامنه‌ای، در نجف اشرف
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18 · <a href="https://t.me/akhbarefori/668343" target="_blank">📅 11:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668341">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
لحظه رسیدن پیکرهای مطهر شهدای خانواده رهبر شهید انقلاب به کنار ضریح امام حسین علیه‌السلام
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/akhbarefori/668341" target="_blank">📅 11:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668340">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ee3060ce4.mp4?token=FaujJAykEovnCFTRNcIFEdTPZfvWnxxwanLIL6QgklLKJbDJEEl5fv29dmFX2RMPGJkJKFjsEBNZ9XzMSSFjBrWXmnTdGiWEXZlwLl_hYXmDZRLzTLXIvhYKiuOwznF1vVmkF5tFpfEgvwVL3VW2mz8UeBaz8Q_mc9KgXhGRo82WcfZVcW3u_4_mj9_a2J34m8IzPZFd8VVu2un_mAknPHTMvv1Wz1pav15sH4CoBwHombvbvQKo4v_Fl-GRsPKQwfEEHas2A44ily5iE_lZIoh5K2653rt-0eQrYCkEwOep_FNItZZfulrLEXAcXqdZAzVcTzx2eaQDRQkO7DPEOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ee3060ce4.mp4?token=FaujJAykEovnCFTRNcIFEdTPZfvWnxxwanLIL6QgklLKJbDJEEl5fv29dmFX2RMPGJkJKFjsEBNZ9XzMSSFjBrWXmnTdGiWEXZlwLl_hYXmDZRLzTLXIvhYKiuOwznF1vVmkF5tFpfEgvwVL3VW2mz8UeBaz8Q_mc9KgXhGRo82WcfZVcW3u_4_mj9_a2J34m8IzPZFd8VVu2un_mAknPHTMvv1Wz1pav15sH4CoBwHombvbvQKo4v_Fl-GRsPKQwfEEHas2A44ily5iE_lZIoh5K2653rt-0eQrYCkEwOep_FNItZZfulrLEXAcXqdZAzVcTzx2eaQDRQkO7DPEOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه ورود آیت‌الله سیدمصطفی خامنه‌ای، فرزند ارشد رهبر شهید بدون عمامه به منظور احترام و تعزیت به حرم سیدالشهدا (علیه‌السلام)
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/akhbarefori/668340" target="_blank">📅 11:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668337">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f8c11fc5b.mp4?token=s-wbyq8ZU1SSu1MtChHTxVIKouYFPK5Kpz2YZI5StsQUeOlSyPxru-nxDEvBnlgl3vY-Nffk7yrE9laWBDrOUC8RuA71tIZkSKtmRKKUuzy0cv147di7WxNeeU5X927bIRekXegeoYBNtUoIjBWmme0fHO-2Lv_JYPgRHepCxIhtKLPjT7pwUMA0dQvAdSyaV3mlo3zFzdQlIAuFxieuyGRhvMovfaAkF8P-SIQ5Xc7IkBGUvTXrkFDrN93RdDiVi1QB6RGa8mM0hNtEQf6nLcvKB_Vfq5p8bSgNpovijMgR1bmFSTmPAYY-Pc_tcHLVnse7pr1YN8epgdU7fYM-bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f8c11fc5b.mp4?token=s-wbyq8ZU1SSu1MtChHTxVIKouYFPK5Kpz2YZI5StsQUeOlSyPxru-nxDEvBnlgl3vY-Nffk7yrE9laWBDrOUC8RuA71tIZkSKtmRKKUuzy0cv147di7WxNeeU5X927bIRekXegeoYBNtUoIjBWmme0fHO-2Lv_JYPgRHepCxIhtKLPjT7pwUMA0dQvAdSyaV3mlo3zFzdQlIAuFxieuyGRhvMovfaAkF8P-SIQ5Xc7IkBGUvTXrkFDrN93RdDiVi1QB6RGa8mM0hNtEQf6nLcvKB_Vfq5p8bSgNpovijMgR1bmFSTmPAYY-Pc_tcHLVnse7pr1YN8epgdU7fYM-bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یزله و شعار مرگ بر آمریکا توسط عزاداران رهبر شهید در عراق/ خبرفوری
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/668337" target="_blank">📅 10:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668336">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10157c44e0.mp4?token=s0q-VX4wq_yphWTtHGKAolik3buOQtD_-TrQGbokt8GpH_zNyIcKqnjG3YCtmu0koVSnrCP7-_lSxAbOPoIYVs8TtgSFc-tFrEvlyulJkVJWygCBCYuSYwr5fYdy63H4mLhcaOeeXZaYD8937fGNwPh2PiGuscZvuc_dYWbunJkKDe7bXwBJ5A81qgWQ1qyjv6D72RRdH0IiYjmf8Ytcd515w2xGu-zpPltEE-XqrCmSOp8tCiYq8mz2tyr74PdvDUCJUZL2QqwA34CDjiDgtkpc8aMeDI9wmp1Jzp79oHxUAKPlZmcNruwcdH3qnqsNOyHjrsnJK6HRvD9pGdPflw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10157c44e0.mp4?token=s0q-VX4wq_yphWTtHGKAolik3buOQtD_-TrQGbokt8GpH_zNyIcKqnjG3YCtmu0koVSnrCP7-_lSxAbOPoIYVs8TtgSFc-tFrEvlyulJkVJWygCBCYuSYwr5fYdy63H4mLhcaOeeXZaYD8937fGNwPh2PiGuscZvuc_dYWbunJkKDe7bXwBJ5A81qgWQ1qyjv6D72RRdH0IiYjmf8Ytcd515w2xGu-zpPltEE-XqrCmSOp8tCiYq8mz2tyr74PdvDUCJUZL2QqwA34CDjiDgtkpc8aMeDI9wmp1Jzp79oHxUAKPlZmcNruwcdH3qnqsNOyHjrsnJK6HRvD9pGdPflw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از تراکم جمعیت حاضر در میدان ثورةالعشرین نجف اشرف در تشییع پیکر مطهر رهبر شهید انقلاب #بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/668336" target="_blank">📅 10:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668335">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
مرقد رهبر شهید با نظر رهبری معظم در مسیر زیارت زائران خواهد بود
تولیت آستان قدس رضوی:
🔹
رهبر معظم انقلاب فرمودند که مرقد شریف رهبر شهید انقلاب را در مسیر زیارت قرار دهید تا زائران در مسیر تشرف برای ایشان ذکر دعا و فاتحه داشته باشند.
🔹
ایشان با پیشنهاد فضایی مشابه مرقد مرحوم شیخ بهایی ایشان موافقت نفرمودند.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/668335" target="_blank">📅 10:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668334">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در بوشهر
🔹
صدای چند انفجار در شهر بوشهر و مناطق پیرامونی شهر شنیده شد.
🔹
اخباری مبنی بر حمله به جزیره خارگ نیز منتشر شده که منابع آگاه مستقر در جزیره، این اخبار را تکذیب می‌کند./ مهر
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/668334" target="_blank">📅 10:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668333">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
تردد کشتی‌های تجاری در تنگه هرمز بدون محدودیت ادامه دارد
دبیر انجمن کشتیرانی:
🔹
عبور کشتی‌های تجاری از تنگه هرمز برقرار است و ترددها طبق ضوابط اعلامی جمهوری اسلامی ایران انجام می‌شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/668333" target="_blank">📅 10:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668332">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
هگست با دستور کار ایران و اف-۳۵ ترکیه، راهی اسرائیل می‌شود
🔹
وزیر جنگ آمریکا پیت هگست که همراه رئیس‌جمهور این کشور در سفر به آنکارا به سر می‌برد، امروز در اولین سفر رسمی خود از زمان تصدی این سمت به اسرائیل می‌رود.
🔹
هگست قرار است در این سفر با نتانياهو و وزیر جنگ این رژیم، دیدار کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/668332" target="_blank">📅 10:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668329">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CobVvmmisJ6m--IaF9iHgAx-y3sTDgpbHujBDems4mBUhmNk1DPa25pw36SsxDnbueNt6You-CigoxsNyH7yPF-6hRxSVlNTi_kWpSh9l2ep7IzY1TrIxS-GGX0vFoJnZPPA2Cn9c_wrt5D7zFHFEA8_-DPFdwsWxVdd8cOZwdUQ00REThtBkTKYEJDitrm3thHPMhqXbbqwbEs20_aOK9t6m1iR6rjEf-ndgRP4y1D1im6Ra5M2GUKcGi2-Hbwluh8PkyZW7NhIz1qQ1MgwIksQMLFUA1ViU4f2T2evCzsyp3coeqhJDukVG5_K6ALb4tXMAfbpLKN0-vcZTF1knA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n2rqytgyBXapvOuZKA-fmcOaiEKx7ZxJIM6G3ziNMX4CDhLAv9UqcPMrWRlsPDDzcv5mHaT46zAzt9c5gplvdz9-9eePbk9ySqxPf2SfJhwNfbTBAdYIGiDRcMJ9T3URs6qGpn4RF-gzG1sfMPNb51Kg423Wzy2pS9xrVBdn0a4i6Q5wC34SAZ3VjKSvxmIZte6TT3H3bNnuC17BppBLqQh4Y1aOV-JGpOID9flh76AgGWKBkbOB0XSd0mBRmqnL9V2JRbydBnvFg1FY-grjGTGl_g6YQapUqxOwphin0WLwUKjFJet8h8s8zQfsQR0aPvLnLW4BOrl-PSZoMYlszQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cRF4ndwPbSQdYt5VKh1Mz1Z4JNsgccF7VPXzmhnTCLU4BqOx2KgIvG4_dKfbYr7GKb26Mvr9O9MzEAdW43dSeWePPB-M779MFFDEtmKrgVAP7Bo2fcCQPpfd_eJhQT0XSl4YtRQxpyzwjVI8-hszfDHq9GRqgKy4bpT2XsqKnoUL-0OO7M2GeoQr8XOUEH9-iViV2-zhy5F5mppJwPs7rP5ro-MHFzEZGfcPyNIwVVJgm1q3ZdQLaIY6zssTsvly-TZLCT8EdxrMoNLPARzlCF857_r746Mv_yKPWvOSBTX_vZ2ahd2R4FvUtFAtEUfsTeECMPw6aiCgmjm6R5eAjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از تراکم جمعیت حاضر در میدان ثورةالعشرین نجف اشرف در تشییع پیکر مطهر رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/668329" target="_blank">📅 10:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668328">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
پیام نوری المالکی از نجف در مراسم وداع با آقای شهید؛ ایران تنها نیست
نخست وزیر اسبق عراق و رهبر ائتلاف دولت قانون:
🔹
جمهوری اسلامی از حامیان فراوانی در منطقه و جهان برخوردار است و این همراهی، فراتر از مرزهای جغرافیایی، ریشه در باور ملت های آزاده دارد.
🔹
تمامی اقدامات امروز ما، در راستای پاسداشت یاد شهید آیت الله خامنه‌ای است؛ رهبری که در برابر قدرت‌هایی با توان نظامی عظیم ایستادگی کرد و پیروزی را رقم زد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/668328" target="_blank">📅 10:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668327">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DTB1uxtg8uxOm_r4x0BZnECJwa1q56fnBN0QVQMlgVsVbeEYxbNUZJSdE_A5QgaPGMRl5u6-u6ksh0QZUMbhdkmyiMVo5MDMSQARqRaNI_j1FGj8VWN5bEFZUyYVoDFC05u2Bb2RzxvNPpH0kmus_L-blEethnqk3PwB9ETG1ckD091CB7T7thpEJSZOJICVXr787sj9Aw7ZzfpRxYA2JZc91XLbJD5xi2wPzNEnkwYbaKdeKXPIdLQXxYl58kB5UDuWibYVu44yepibRJVgG25WyIKR4O-qofhiUeI_nZZCpIgLoZc02LiyWpwceFB4hxJUpvMjYmwrcbuCEMEc3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قاب متفاوتی از حضور گسترده مردم عزادار عراق در میدان ثورةالعشرین نجف اشرف
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/668327" target="_blank">📅 10:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668326">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
زمان آغاز مراسم تشییع رهبر شهید وابسته به زمان انتقال پیکر‌های مطهر از عراق به مشهد است
استاندار خراسان رضوی:
🔹
در صورت رسیدن پیکر‌ها در روز چهارشنبه، مراسم تشییع ساعت ۶ صبح در خیابان امام رضا (ع)ی مشهد آغاز خواهد شد.
🔹
پیش‌بینی ما این است که مراسم تشییع در مسیر خیابان امام رضا (ع) بین پنج تا شش ساعت ادامه داشته باشد و مراسم طواف و تدفین در غروب پنجشنبه انجام می‌شود.
🔹
تصمیم بر این است که درهای حرم بسته نشود البته طبیعی است که درهای رواق‌ها و بخش مرکزی حرم در هنگام تدفین بسته باشد و  ساعات بسیار کمی بخش مرکزی حرم و روضه منوره بسته خواهد بود.
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/668326" target="_blank">📅 10:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668325">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
جانشین پلیس‌راه: ترافیک سنگین در محور چالوس و آزادراه قزوین–کرج–تهران مشاهده می‌شود.
🔹
ترکیه و کانادا مذاکرات برای توافق تجارت آزاد را آغاز کردند
🔹
هزینه‌های سوخت ایرلاین‌های آمریکا ۳ میلیارد دلار افزایش یافت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/668325" target="_blank">📅 10:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668324">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
به صدا درآمدن آژیر خطر برای سومین بار در بحرین/ چندین پهپاد در حریم هوایی بحرین به سمت منافع آمریکا در حرکت هستند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/668324" target="_blank">📅 10:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668323">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
شهادت یکی از پاسداران منطقه سوم دریایی سپاه در پی تجاوز دشمن صهیونیستی به ماهشهر
روابط عمومی منطقه سوم دریایی سپاه پاسداران امام حسین (ع) بندرماهشهر:
🔹
صبح امروز چهارشنبه ۱۷ تیرماه، در پی تجاوز نیروهای تروریستی آمریکا به منطقه سوم دریایی ماهشهر، پاسدار «محمدرضا خزینی» در حین مقابله با پهپادهای دشمن و بر اثر اصابت ترکش پرتابه به شهادت رسید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/668323" target="_blank">📅 10:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668322">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fb5206ff4.mp4?token=BaNrtV6mVP0QGFbC82b0P2oUFp2vg1ZdHIEnmXscxNVSFHfBsCGSVp43FXP0YI8qbEzPOyndY5MnRqVu9grg9lCwsgOch4f11v-zNlc1pNv7_0koNk_TS3Ov5Iu4g27yizk6ufY-I7wHoKRsCUfsvH-IZUoMrdoVHVj_0PxW4TsSuBZV2JeYbktwYtEVEgRMcJbBbCOrxbi-jecUVGgGJ__wxR_Hm-_-XGPxwXQMilgg2DyFKg9vkJyDoSOApecexL4BKPLt2eqIxpgrnc5__eSsvUCVDnXoVmg5FgILH44_rS9bPjZ-zy23RR2FHeQo3FHej3w9ua7RZumxPV3D84XKBCQe_RciAhsH6DlTJ1_pCVrSIm-HDGsJbwPGOzu5N1REJg5Xg5A_vKhF9GEcb2RYGnBkdlXLXDPiETkxvS_CfGGiwOhXD2--9XgdpbXOk2rF1Cs1jZ7zXma7oQIX9JVPO3oY08dsmEYWCtdNFdCCe7gyDxoE-yZCKMkjSHKA-Qn4xnt87TtZzh9p6JsvVylhiLaR9MNSkblKv5y-Iw5v2_fgPMvrBnrAsMYg-ASxT8vs9kBKlE_r4DfiIDDiozDCnsFbCmdT70d4dR8paoVF_26g3sB9lVTWuXx624lH0XM-YxPWElys7dXqumnTh5gqK1mCdn6e6Se5nMISo_U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fb5206ff4.mp4?token=BaNrtV6mVP0QGFbC82b0P2oUFp2vg1ZdHIEnmXscxNVSFHfBsCGSVp43FXP0YI8qbEzPOyndY5MnRqVu9grg9lCwsgOch4f11v-zNlc1pNv7_0koNk_TS3Ov5Iu4g27yizk6ufY-I7wHoKRsCUfsvH-IZUoMrdoVHVj_0PxW4TsSuBZV2JeYbktwYtEVEgRMcJbBbCOrxbi-jecUVGgGJ__wxR_Hm-_-XGPxwXQMilgg2DyFKg9vkJyDoSOApecexL4BKPLt2eqIxpgrnc5__eSsvUCVDnXoVmg5FgILH44_rS9bPjZ-zy23RR2FHeQo3FHej3w9ua7RZumxPV3D84XKBCQe_RciAhsH6DlTJ1_pCVrSIm-HDGsJbwPGOzu5N1REJg5Xg5A_vKhF9GEcb2RYGnBkdlXLXDPiETkxvS_CfGGiwOhXD2--9XgdpbXOk2rF1Cs1jZ7zXma7oQIX9JVPO3oY08dsmEYWCtdNFdCCe7gyDxoE-yZCKMkjSHKA-Qn4xnt87TtZzh9p6JsvVylhiLaR9MNSkblKv5y-Iw5v2_fgPMvrBnrAsMYg-ASxT8vs9kBKlE_r4DfiIDDiozDCnsFbCmdT70d4dR8paoVF_26g3sB9lVTWuXx624lH0XM-YxPWElys7dXqumnTh5gqK1mCdn6e6Se5nMISo_U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خودروی حامل پیکر مطهر رهبر شهید انقلاب به میدان ثورةالعشرین نجف اشرف رسید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/668322" target="_blank">📅 10:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668321">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2417608f0b.mp4?token=s-dGQtkYpJwlaKkyoPvi60UCcBGVUutE5f1XHFamYPQ9ZYeQwQegmW5YY6TGE25V3QJjkUrerq4nYjVaKIEjzaEydvJ5sR_Ge9OPoVtm3JK2PZoVu1iukwjs_XD0YLASic77VRK-Sn-i5MKzAgCu1dtbSOrCjFi3Hn0QrORmIVSvazW6LDwoAKaUVv6NPoMJet9tNbK2cv9JxQdjgdFEWwlaRdiRik-wpPplZP5wB8WkQg4ap_-WPtSVnKE7PuYGVZdJT_rrHuhNRGAbZspKxnjFOinys4u9l7s-QU4Akw-DStJ-UvctD2yiUCnou4QhIK9lGE5wIvlK-E9OyFt7HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2417608f0b.mp4?token=s-dGQtkYpJwlaKkyoPvi60UCcBGVUutE5f1XHFamYPQ9ZYeQwQegmW5YY6TGE25V3QJjkUrerq4nYjVaKIEjzaEydvJ5sR_Ge9OPoVtm3JK2PZoVu1iukwjs_XD0YLASic77VRK-Sn-i5MKzAgCu1dtbSOrCjFi3Hn0QrORmIVSvazW6LDwoAKaUVv6NPoMJet9tNbK2cv9JxQdjgdFEWwlaRdiRik-wpPplZP5wB8WkQg4ap_-WPtSVnKE7PuYGVZdJT_rrHuhNRGAbZspKxnjFOinys4u9l7s-QU4Akw-DStJ-UvctD2yiUCnou4QhIK9lGE5wIvlK-E9OyFt7HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرچم مقدس گنبد امام حسین (ع) روی پیکر مطهر امام شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/668321" target="_blank">📅 10:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668319">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3295ff058d.mp4?token=sgcal03NTlOdBgwWYBXCyzkq-W0Hvcown0oe27MKAs7SilXbAXGfXm25DceWlyuZ3M4fKw-ioT2j0016L2XXsn1AdWZyqLQfFDZHf1WG-vLGINH6wZGktaVHDuefVI-cJzW9uUxvdkWwnINoRSlmfbimBvNyXMX84q1cdSfxLH7_d654AeY--8hA61b7gfDye0H3RvJA2QJKsM_D6iAHvM9mm56QeDRweclX3NI7tk90A-9pYSd5Xtuq2Kw2JT0jyRCl57Th3zYdNSJ6OZbI-nxDjDes8oRmyU0fxxoFZHVMXVZ1q6Lbrf7M6c6MjoB1ZQxQoAdCBDNsE5JYE3wZlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3295ff058d.mp4?token=sgcal03NTlOdBgwWYBXCyzkq-W0Hvcown0oe27MKAs7SilXbAXGfXm25DceWlyuZ3M4fKw-ioT2j0016L2XXsn1AdWZyqLQfFDZHf1WG-vLGINH6wZGktaVHDuefVI-cJzW9uUxvdkWwnINoRSlmfbimBvNyXMX84q1cdSfxLH7_d654AeY--8hA61b7gfDye0H3RvJA2QJKsM_D6iAHvM9mm56QeDRweclX3NI7tk90A-9pYSd5Xtuq2Kw2JT0jyRCl57Th3zYdNSJ6OZbI-nxDjDes8oRmyU0fxxoFZHVMXVZ1q6Lbrf7M6c6MjoB1ZQxQoAdCBDNsE5JYE3wZlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر خبرفوری از حضور پرشور عراقی‌ها برای استقبال از امام شهید/ ندای لبیک یا سیدعلی در حرم حضرت ابوالفضل(ع)
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/668319" target="_blank">📅 10:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668318">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bS3JdDvabxioK6BC1IU_Apo3qiHywNyFFuj6pdJ7o8Wm2apR0rQuMWESqCygyuPVNgPytOVBf4Zwv5cTjn6lAUzqAXYwpeom0oNJgFQ8PMkcDDSCvdBy2sOxtsSrTHwNa4lwLSmAdAOkgOarbdOjSRT2Qqzq5xDEeIqhX2XvrM5yBqHq8Xe35DsPUa1Mu5aRUIfBVwOlJi59GC2Ca9Z42GCVF0CgEpOZe-lQlHH4NDrsfOpQ62QzvxliphFDYlmCTyPiGn5uCXhQqB0yC0a4iT_RQeL2oZ4GyJfmi3Pzb5Lq6OmZqCioS5VM_El83a4IMslmdmju7Lq0EoZ8abbFeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴
۸ نانوایی منتخب اطراف حرم مطهر رضوی در ایام تشییع شهید رهبر به‌صورت ۲۴ ساعته فعال هستند و نان گرم را در تمام ساعات شبانه‌روز در اختیار زائران و سوگواران قرار می‌دهند.
📍
محدوده: اطراف حرم مطهر امام رضا (ع)
🕒
زمان فعالیت: شبانه‌روزی (۲۴ ساعته) در ایام تشییع
#سازمان_ساماندهی_مشاغل_شهری_و_فرآورده_های_کشاورزی
🌐
https://samesh.mashhad.ir
🔸
http://Instagram.com/mashhadsamesh
🔸
http://eitaa.com/mashhadsaman
🔶
https://rubika.ir/mashhadsamesh
🔸
https://ble.ir/mashhadsamesh
🔸
https://gap.im/mashhadsamesh
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/668318" target="_blank">📅 10:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668317">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fa6L1SfwlWb4cZ28IinscVr_p52m-8YjScYd5jaZSTGoS6jIqjLIxMmir4s41oy6RU0Q_ww0RDRAuj1Y-ocBMhTzWNJnAHu-n3fgxoGlP9F5RcrIpD1tcsjg8hiMY_jeGNd3J9qgBeoJDl-dpDbC7y-Qz2ktK_INvayymlQlcmMLXK_kSMS62NRA3tSbHu33Mahw9RdnLZCxqucR-NMMMYRQDfSDhjQpyS39eZeQW8fhBqO6w-pix7MLTdBzP974afax2EN4iZz0ClOp2P0s6peMlqcITWQ-h0TRn-LRmLlydJ7G-gNFXN7307Mi4-iYHgv9Lomxisxr6iXIxiIt0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیانیه وزارت امور خارجه درباره حملات تجاوزکارانه آمریکا و نقض فاحش يادداشت تفاهم خاتمه جنگ
🔹
آمریکا بامداد ۱۷ تیر با نقض منشور و تفاهم خاتمه جنگ، به تأسیسات جنوب ایران حمله کرد.
🔹
لغو مجوز نفت ایران و حملات اسرائیل، تفاهم را بی‌اثر کرد؛ مسئولیت با آمریکاست.
🔹
ایران به همسایگان در مورد همکاری با متجاوز هشدار داد.
🔹
ایران حمله را محکوم کرده و بر اساس حق دفاع مشروع، مبدأ تجاوز را هدف قرار خواهد داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/668317" target="_blank">📅 10:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668316">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l2nqaT-sF7p9U7gN7zrJ-3uxnWaSE6q56yF4qZFPVRdclC7EMwssrKbfDTsUsoGMQb-bSlHC_0rM606-dquztcGecTce37e9n5EsL7Q1Kh33GBjzkO7KkeB7gpNUl-S4QX68iO4_zB_NrHSIed_GMCBw_dhmkdiCt88qK5u176JWxfDN_ntiZElHUzQkE4cPR2P4i_zzyzs2VzEv0RmFoB3CQFgzk9o5zwHKQM_JgO5j1pKoc1oB6ieTGQiJvCJIwWNQqs4ozcMrsvxeH15cMz8xp1SoCiaf9ha1TG2GVm0rH_hDeCM4ob_Lobll5MLX2VSFDo0iPJejAKoRyhKlKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری به مناسبت مراسم تشییع رهبر شهید؛ پویش مچ‌بند سرخ
🔹
مخاطبان عزیز خبرفوری، برای شرکت در این فراخوان کافی است با یک مچ‌بند سرخ در مراسم تشییع حاضر شوید و تصویری از حضور خود با مچ بند سرخ را با ما به اشتراک بگذارید.
🔹
مچ‌بند سرخ، پارچه‌ای به رنگ خون و نمادی از عهد، وفاداری و خون‌خواهی امام‌ شهید است.
🔹
بیایید در مراسم تشییع با مچ‌بندهای سرخ حاضر شویم تا پیام ایستادگی، حق‌طلبی و عدالت‌خواهی را به نمایش بگذاریم؛ پیامی که نشان می‌دهد یاد شهیدان زنده است و جنایت و ترور از حافظه امت اسلامی پاک نخواهد شد و همواره خون شهیدان خود را مطالبه می‌کند.
🔸
تصاویر خود را برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/akhbarefori/668316" target="_blank">📅 10:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668315">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jmto0tV7bMMUIG5nOWAfTDJIodw9SP2ju0TsfTEarkfDs_LvioATIXGLiDMIlxIlfWkV83rHSRem3twZkQnPRyvFWH_dKnQXkhstP1oOWIksQplHONimqhPWYCSDO26X4GToOtzGC1hSUBnjLlnOsNzFLFlQRqTeiPOqNU3PU0_vgidIdVO9U6tjgZCBr_N4Hyy1gUmHF0onABaMmYQi7tulShiBDrOBM1Lw0VgZqjyqCaaUAoc9dj-Bp_Hj_FCkRWLh98c7cDLeWgj-ciBqgdkogIbZPrSnH6mBtsbGXNVYbrsafYtN0c8i8aA_rnJiGGCfHRVrhsPyyuz816WVKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا دیشب به کدام‌ نقاط در ایران حمله کرد؟
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3228708</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/668315" target="_blank">📅 10:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668314">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
وکیلی: انتقام واقعی و آرزوی رهبر شهید، ساختن یک ایران مقتدر، توسعه‌یافته و بی‌نیاز است
محمدعلی وکیلی، کارشناس و تحلیل‌گر مسائل سیاسی:
🔹
انتقام واقعی و آرزوی رهبر شهید، ساختن یک ایران مقتدر، توسعه‌یافته و بی‌نیاز است؛ ایرانی که در معیشت، علم و تمامی حوزه‌ها در قله قرار داشته و الگویی برتر برای جهان باشد.
🔹
اگر تمام دشمنان را از بین ببریم اما کشور را نسازیم، یعنی در تحقق آرزوهای آن شهید ناکام بوده‌ایم و انتقام واقعی را نگرفته‌ایم و حواسمان باشد که با سوءتدبیر، حلاوت دستاوردهای میدان را در صلح به شکست تبدیل نکنیم.
🔹
ایجاد دوقطبی و انکار این پیروزی‌ها به بهانه بر زمین ماندن انتقام، یک ساده‌انگاری تاریخی و کفران نعمت است.
🔹
تاکید بر کشتن ترامپ و نتانیاهو خبیث، تقلیل دادن خون رهبر شهید است این دو فرد در جایگاهی نیستند که ما خود را مصروف به قتلشان کنیم.
🔹
ترامپ و نتانیاهو همین الان هم مرده اند؛ سیاست مدار با مرگ آرزوهایش می‌میرد و این دو در شکست ایران ناکام ماندند و اکنون مرده به حساب می‌آیند و تا زمانی که آرمان امام خامنه‌ای زدنده‌است او در میان ماست.
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/668314" target="_blank">📅 10:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668313">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/560f9383fa.mp4?token=Lm341w2WIqQ8YV8W6ZoG7NCmjdRjAizlwrrUyvpI8NoNnnAnZ6CNdfAOKVCqEg7RFuk1xecG6-uAgBNoGdKOcKCYhgExrCqIuHjfU9Tkjsdf21294U3L4cjzdF8ECgagDUluHMUU2TZpmZmAJ11gJ0ybLQazgEXja5xCG9_u_4PMFV9_lisK_1KFPA-b4qXT6Sz4v6j-ItRdV1eUVcitGabqioEmQkEJTdoIBrZ0bMqxNTj1wn5L4zw-Q3qxJkkIBQrAZ4XXbYU2dl6fFoL1ct7myAq_BMqdX6Jrr7Eqw9BFtmbvu7DdCeXSjbKxwDub3MZB1hameHgBe1QQssyMQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/560f9383fa.mp4?token=Lm341w2WIqQ8YV8W6ZoG7NCmjdRjAizlwrrUyvpI8NoNnnAnZ6CNdfAOKVCqEg7RFuk1xecG6-uAgBNoGdKOcKCYhgExrCqIuHjfU9Tkjsdf21294U3L4cjzdF8ECgagDUluHMUU2TZpmZmAJ11gJ0ybLQazgEXja5xCG9_u_4PMFV9_lisK_1KFPA-b4qXT6Sz4v6j-ItRdV1eUVcitGabqioEmQkEJTdoIBrZ0bMqxNTj1wn5L4zw-Q3qxJkkIBQrAZ4XXbYU2dl6fFoL1ct7myAq_BMqdX6Jrr7Eqw9BFtmbvu7DdCeXSjbKxwDub3MZB1hameHgBe1QQssyMQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حال‌وهوای حرم حضرت عباس(ع) همزمان با حضور شهدای خانواده رهبر شهید انقلاب در این حرم مطهر
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/668313" target="_blank">📅 10:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668312">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
حمله موشکی و پهپادی به کویت
🔹
منابع خبری از حمله ترکیبی موشکی و پهپادی به اهداف نظامی آمریکا در کویت خبر دادند.
🔹
همزمان با فعال شدن آژیرهای هشدار در سراسر این کشور، گزارش‌ها حاکی از وقوع انفجارهای شدید در مناطق مختلف است.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/668312" target="_blank">📅 10:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668310">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YFZ_F2l9SNh8BJuwICsY4kmb167Xtu70Ht-mM9g2Pl-TwxUXRRbHWZUhoOnIhqmMZe6-5r47vQD779gRBnDGlukZVWAzuBnNjR3bZCA1EPlHxcxKOvv06b18mHQx8U4IhG3n1Ukb9spz9JG_-DYGVA6_LyJYMWmvNAryUTOK0jHFuH9zNKxnNFBzgm9P0CuQwx71NaZetZ2wawTytOvJWTEQTIqGKAiwAPOBScPEEwlNyWIbaMutnq438M2o4e-0bUXZ46HWJJymW-0T_OhvAXwcg8ksFCfjMpqcUIQCT9iy_XZGLmlBoS63qQC9kqv5tzh7bw8ZET9cUF9nagGw_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LURGe3ynfEcCz64bCHABLfVD-M_ccBYZMNQJM8Dq9nxSfMVyWnz9WdG3fFmN1kiK3e3Cg--iQPzM0SuCyKNRCSNjPU1-ehz8ywZYzsfC8kZoNabvm3LT9QcBZQnstXCXhOBmoD1DgaG1fh49pj95R5Yy91pQeaLSoeaxAcEqB_MyJcPEGbKI9cCybs5oc0_gNd6UKC4AHoxQH3qrFWimqWA-TeoTBjkJLzsehbj87HkQ3rS5XiDCzWx0a9MrmlBg3wRR-wgEmBH-QbWyWq7icKWADvP9LISgckUjrrfaQ2B3HQUOo2XarFrCSb4FzZST3oFjrbFvSKv0LZi_HJB4Kw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پدر و دختر به پابوسی علمدار رفتند
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/668310" target="_blank">📅 09:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668309">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LwmR8sZy4u_hqF1HM_KhumkjxhEICsBm1ZDHNKOuLE9Tzcmr2i4ioK_nKlfMwkWwaqcTLR7ya3g0R3G4jk6jiNja0ZdQELvf1JNa4KcfVWjyBKmgv-jBvW0PgTuGyMJOiovhlxQJ1wXh3o4M2J_jQBZmfDgWT45YcJ777gXERHUAy0hclkvJi8uQzqLXq1qLhQ-JM3qGQVyIWrthb2EeR8-XRbByEv1HHWKxajampaK-G-LaGYi0LAvOzWLH-Tieey8iqdXsL2dqiKAmxFLJWyS3C632L-eNyNJW4JTHkGrqHakXAMis_DMPmwD0jqmkfGz6bytG46fjlxwB5vBSuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اسمیت، خبرنگار ارشد نیویورک تایمز به نقل از یک منبع نظامی: حملات هوایی علیه ایران فعلاً ادامه دارد و قرار است تا مدتی ادامه پیدا کند، تمرکز حملات روی چندین هدف نظامی ایران خواهد بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/668309" target="_blank">📅 09:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668308">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
آژیرهای هشدار در بحرین برای بار چهارم به صدا درآمدند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/668308" target="_blank">📅 09:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668307">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
حمله پهپادی ارتش به پایگاه های ارتش تروریستی آمریکا در  بحرین  روابط عمومی ارتش:
🔹
به دنبال تهاجم خصمانه دشمن آمریکایی به مناطق نظامی و غیر نظامی در جنوب کشور و نقض مفاد ۱۴ بندی تفاهمنامه، پهپادهای هجومی ارتش جمهوری اسلامی ایران، از بامداد امروز، مراکز تجمع…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/668307" target="_blank">📅 09:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668306">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c502698c7.mp4?token=r_oT26fNuVJg1DFGpBm_eNXJK6m8Y8L5Fo9-TjrT52TzbIfVoGfv1wblrd8Fu5HPhdMKJCcdhz_rXOer5ENpfukrp-uvT1eikovURjYrF24RtTtwqe70PA0CkMO0mbHF0H2xz-AHK8Ljx0cQLPPFrU7XV0jnv84ODOshlxhK503HPTwLw4ayoEc4oI1Or1MxYzPw9dV1_FodWmMfsImKDP_jEeAqfNHO4awkcv5EmbuJADpdzTal1H2HXPJYrTP-j7fHLuNzOhCuzRMyxYeZKxEom1K_5PWbhxTtoh61g1x_t1F9L1gMNqvh-00dd-5tWcTykenIXbQhFwBP5xKMFyChLcmV711Osu_AzyXYlVfJQkC4oYzY9mt8zGV7SqRcb72x70mlyiWpbZX_nkQvZIPUHdFbB_Z56HIadduZ30Pfll_0ZyyXigAFUUNvHuN0nHaFt25tnn5Ez1-4NZ932ZH75LzKI6w6QCXoCnUSn-z3PQpVjQIDRctbnrJmjndemgTi6o2LNMQoPfqVrruE0NGsMNNBApFRjz_ZaJmJTLc6pxAzxPipi0tyTA-o-CaF-jOx7OHxRYvB3YyH2iTJsizI_M0cmdr6KSEv4dHlML3NRBK18Dzu02-eigv11AIIhvoT_ETEQVtXu8N1drAtSzjyE1-FBM3ukL1YCjn7J0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c502698c7.mp4?token=r_oT26fNuVJg1DFGpBm_eNXJK6m8Y8L5Fo9-TjrT52TzbIfVoGfv1wblrd8Fu5HPhdMKJCcdhz_rXOer5ENpfukrp-uvT1eikovURjYrF24RtTtwqe70PA0CkMO0mbHF0H2xz-AHK8Ljx0cQLPPFrU7XV0jnv84ODOshlxhK503HPTwLw4ayoEc4oI1Or1MxYzPw9dV1_FodWmMfsImKDP_jEeAqfNHO4awkcv5EmbuJADpdzTal1H2HXPJYrTP-j7fHLuNzOhCuzRMyxYeZKxEom1K_5PWbhxTtoh61g1x_t1F9L1gMNqvh-00dd-5tWcTykenIXbQhFwBP5xKMFyChLcmV711Osu_AzyXYlVfJQkC4oYzY9mt8zGV7SqRcb72x70mlyiWpbZX_nkQvZIPUHdFbB_Z56HIadduZ30Pfll_0ZyyXigAFUUNvHuN0nHaFt25tnn5Ez1-4NZ932ZH75LzKI6w6QCXoCnUSn-z3PQpVjQIDRctbnrJmjndemgTi6o2LNMQoPfqVrruE0NGsMNNBApFRjz_ZaJmJTLc6pxAzxPipi0tyTA-o-CaF-jOx7OHxRYvB3YyH2iTJsizI_M0cmdr6KSEv4dHlML3NRBK18Dzu02-eigv11AIIhvoT_ETEQVtXu8N1drAtSzjyE1-FBM3ukL1YCjn7J0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اشک‌های عزاداران عراقی حاضر در بین‌الحرمین، هنگام ورود پیکرهای مطهر شهدای خانواده رهبر شهید انقلاب به حرم حضرت عباس علیه‌السلام.
۱۴۰۵/۰۴/۱۷
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/668306" target="_blank">📅 09:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668305">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در بوشهر
🔹
صدای چند انفجار در شهر بوشهر و مناطق پیرامونی شهر شنیده شد.
🔹
اخباری مبنی بر حمله به جزیره خارگ نیز منتشر شده که منابع آگاه مستقر در جزیره، این اخبار را تکذیب می‌کند./ مهر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/668305" target="_blank">📅 09:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668304">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
قرارگاه مرکزی خاتم‌الانبیا: اجازه دخالت در امور تنگه هرمز را نخواهیم داد
🔹
یدیعوت آحارونوت: وزیر جنگ آمریکا سفر خود به اسرائیل را آغاز کرد
🔹
سم آلتمن: فردا نسخه GPT-5.6 ارائه می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/668304" target="_blank">📅 09:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668303">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41cd9469ad.mp4?token=WjJ_KTNxf6Gqwyvq9JxjgP_0Yz7nGf3V34qBHcjNzIWruPVj4lpAyDwqmBnIq9FhtNwemX2fAcBSdG6piuSPf5ZFq7MC_sRiDFqhUCOKSqhiYThpgZx2naTZAGTYdkHCfZAbYewNfRuvZw5viNyL0QPDAELggOFAeIwLdZRAWzVazTlNtsVghixG6KVDDIFyVTh1cjPDbYHvWJY83cI1ugm6r7pPZhmxTJGbWpCC2lNdOt4ZXufsZZvtKDJLyVHneAJ3Hrwu1fHWn8q_SHP8uppfoXnzxIGidKOaZRHBwhGbTqGQZkQCAke6ghKKwET8b3svMoB6KRDrnFg4_ils6zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41cd9469ad.mp4?token=WjJ_KTNxf6Gqwyvq9JxjgP_0Yz7nGf3V34qBHcjNzIWruPVj4lpAyDwqmBnIq9FhtNwemX2fAcBSdG6piuSPf5ZFq7MC_sRiDFqhUCOKSqhiYThpgZx2naTZAGTYdkHCfZAbYewNfRuvZw5viNyL0QPDAELggOFAeIwLdZRAWzVazTlNtsVghixG6KVDDIFyVTh1cjPDbYHvWJY83cI1ugm6r7pPZhmxTJGbWpCC2lNdOt4ZXufsZZvtKDJLyVHneAJ3Hrwu1fHWn8q_SHP8uppfoXnzxIGidKOaZRHBwhGbTqGQZkQCAke6ghKKwET8b3svMoB6KRDrnFg4_ils6zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌اکنون؛
پیکر مطهر رهبر شهید انقلاب در حال حرکت به سمت حرم حضرت امیرالمومنین علیه‌السلام
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/668303" target="_blank">📅 09:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668302">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
نه به اسراییل و بله به مقاومت؛ شعار عراقی ها حرم مطهر امام حسین (ع)
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/668302" target="_blank">📅 09:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668301">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H4GqNMu5GLL4X397jB5qctv97-8MhuHvylrDD7LDF-eNiC1wYZnxiK_1KYfbnoMvcC_3MSXZBejwlJ6LIrIsFEDNX1T7OljDYzbu5NitKL1McuvMk_cMFUj7hqQB5CzeWNewIgyMGCGJtvAG7ftKYBnGI_aAF8JSeHfEUmwu0i8snbC5dhqpZndrmPanqlcsyDGuAHgI_oOx_P_eMk2WyuFWS8bIJx3ellZ2hKXVRfXTDCnkniOmSE92PeoJdfLZV_IPsnkAbAHL3rb6-cBIvtppnnqT33cavsJ7G153hzawlByshXHX-cdEMaNx4fogmmxAx5WVMOtYmLuNXhMX-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هلاکت فرمانده اسکادران بالگردی نیروی دریایی آمریکا در سانحه دریای عرب
🔹
فرمانده اسکادران بالگردی نیروی دریایی آمریکا، «گابریل ادواردز»، در سانحهٔ سقوط بالگرد MH-60S در دریای عرب کشته شد.
🔹
بالگرد روز ۱۰ تیر هنگام مأموریت روی آب اضطراری فرود آمد؛ ۳ خدمه نجات یافتند اما ادواردز پس از ۱۰۲ ساعت جستوجوی بی‌نتیجه، مفقود اعلام و سپس به درجهٔ کاپیتانی ارتقا یافت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/668301" target="_blank">📅 09:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668300">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec8993836b.mp4?token=r4nVmlugefqeyQ9mPciLE2TCwFETmjDDsS3IJF00SdvNx7531hvjH65tvbM5UAZKrXVNlmvQbZ22PnG93O_vPN4Cwq-FANvDhP88VfcC7ZqJJAK5HO_hY86lmO7H9IQsZyFBlZbYVeKoLHrTQNQhrKt9lB8zmqOgWvCJVL8DRaHe0pr7B0VvV5yNF9IPObrNsewUoEJxO1CQdhPgzi6SeQvrFEBNTqMkMHc1yIyPZAi8swARZA8-YnFQU19MXboiUP38UmpLCi43RAAKB4ixDPU1A627L19jp5mNx2REvXnOaUT8Xf5iiVGhXGuFAYtMzV4u4VMUCHKUZbet73QPsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec8993836b.mp4?token=r4nVmlugefqeyQ9mPciLE2TCwFETmjDDsS3IJF00SdvNx7531hvjH65tvbM5UAZKrXVNlmvQbZ22PnG93O_vPN4Cwq-FANvDhP88VfcC7ZqJJAK5HO_hY86lmO7H9IQsZyFBlZbYVeKoLHrTQNQhrKt9lB8zmqOgWvCJVL8DRaHe0pr7B0VvV5yNF9IPObrNsewUoEJxO1CQdhPgzi6SeQvrFEBNTqMkMHc1yIyPZAi8swARZA8-YnFQU19MXboiUP38UmpLCi43RAAKB4ixDPU1A627L19jp5mNx2REvXnOaUT8Xf5iiVGhXGuFAYtMzV4u4VMUCHKUZbet73QPsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از تشییع خانواده رهبر‌شهید ایران در حرم حضرت اباالفضل (ع)
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/668300" target="_blank">📅 09:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668296">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D6qr3Vyeeb-IA0IA_vf7CCp2i9cJDkYXSkjjbnElr3l7vJPumd6pI_uHzX0JVMM-_drpQybYMpPR-48PgTxDr5iEWZSuMMle52tQc9qjMSiySXrysViirWyGdgWYrPDfZGgSFNs_D-ZbGn81rpYx2uI8xvmNM-rTKJpBbP4m17b4a2nmcOrL__zjIZmO116AuuMgUYfhSoBDoDhg-oVaSX8CUaWY0ZZGzhueDIYmt8uqxzenVwPh0DpKTpBD0venBy5Qrr3jOYsnl1my_1dRwXOs1O78POyER7ZAoJZ9U3PXie3mLnoZcMDDbuKpc9t7_HGf-Rf8FRj6xfjQA36Gig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LfWlGrx-W5vGsxBlTWPChSmWNg-3laEK-8c5pm8QXUG4babQ_lmxq0orA5c3IdXrRZiz74Q1u7UX28r1nHI6CnYay11kzWKceP_SeaDWoOJBucqKg-3OG1o1IkaRwfVedUBfT1w9dEBE0UvLoDiT4PKWaZBevczk4Tg8q4cVYgicR99_XSv2HrPJZ9p8rT0-0Qw-ykjGrTivfUk287wHZ_4JMrdvXuOQ7IL66sJv1NIQ0DSX8RQ-Bu8xKSTxmDIPMIOcuYhHcMJSD-5vrScMr45a-Uih8cDaIkro7uQogHE4xSOXGX1D9OMD5cMtBTl2XbdVmuCdRquDh9dcJ0c0jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EibX3X75QN00c5m1xj_uNK3OgBOZkTiyZ1ibfdPPmsWK8eOoVVTrjFm2-KMMhIj0aqI9n12QcyrzMcMlGK0RabwfP-65xaXTIaNi3X8XMYQYbLsLvPNKXdVSJrFThdKIDS6NqLwIHU9r1cp4kZKcDlZYFwXZvg1kuawJ246Oem5nKMygqnaihQ2UGFys9wVqoQR0ZWyLPveZzgV-9LsAaKyInGiVpuWFhpd-Z6RTDu__pFTwR6QIdP6CTWUUYIL2D9W0eL6QganIOO_6FeZ6v2Jqy8iDD7BR0QaZcbIWt8wQ3Rt0FVZm5EHS1OuPrXV8XFm-UDdYVjVAF8ecXquNgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CUQukriN05agX76yecumGHeIodyWScjlmbOHlxQySm2IjpeIrxjWde0J-XxuLYWgzKZ86LUWXY3jh4keAMC7HVpKC0tmRXvL0Jc_2xMoZhf7djqxxAy8xqZ4QO-w7FBXji510oX12eyxv2GCWQ_qxkYDzxfympW2dnjWQwt96bn-yVBjiVbHwUJPOv1S50eAJzZoeey4quBCnFqcWv_L99vWtbcC72S9dOCYq5au9CoHxxYv-4Qix1caVeMYf8uJHKlbxYGGNh2zB6AWIO3U7oiiL9KV2jSD9peG48AjwAz4ubcg-Li9slyh-Ihsh8pU5HHpmcTYNjS0-BCA1NZnrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر هوایی از جمعیت پرشمار مردم عراق در مراسم تشییع پیکر آقای شهید ایران در نجف اشرف
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/668296" target="_blank">📅 09:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668295">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94a9ecaceb.mp4?token=SDuLhDNXVDzbjEQkXikals_OXbaX0x8H77_fqdCy5bnZL8vFLNHrDOE0u29nxmMLlFKHomGsq7q_oseejRlVlWsd6zLGryMB9OFMqBhfw6VeOt188Z-S19kj27LSEAHmUSQ6XBOJhNB0I77tfxZ5uVq8qh_SMhE_7QUiM0Jd8n_UrmKBp_RCV_ye1ZRktcDi5om2_M8Gagc3H_ly6aUkVbAO_5FdaLtTU7jAzuN1B0WNznwXOjsw0p6eQ5yp-cgkr6baFW074H84_kXBmjIHDhaSgX67I1cE-W0qHRa7_4B4cPZaN_qExGU9rE2Ro9zdg9Ljqcgs5RNOU9Tb4kQJMglVU3kBH5by2wQGqoGijtfIqqzBZBESN2WyBEFuU8VoCd4xOXlVmcb7WsU1TQPG7RnJCpFeXzHPTuTSGhGZY9r69VIynfNPvuEBqlyKC25ynuPFdPenuE_Nz0IgwiK8nHH1UJukSzhmSfHXsUvB_t_MGUQWLTZHp64dOpcADtxLkxrFTBuOuc9E5XCnssc8_b8VBAxoi-68nIUB2Suvwd-H4Ag1K0uTykf7f5nOcT7Vz4vucxX_cristFYfLx9d4PuLgtHs9XIzr2BNeCXzxQthx6RmfxXpgiZ73E5TJUCnvP7mYOXri5vIKedDRt-XiXNkRSo6AAkFb_zdLDR9W1M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94a9ecaceb.mp4?token=SDuLhDNXVDzbjEQkXikals_OXbaX0x8H77_fqdCy5bnZL8vFLNHrDOE0u29nxmMLlFKHomGsq7q_oseejRlVlWsd6zLGryMB9OFMqBhfw6VeOt188Z-S19kj27LSEAHmUSQ6XBOJhNB0I77tfxZ5uVq8qh_SMhE_7QUiM0Jd8n_UrmKBp_RCV_ye1ZRktcDi5om2_M8Gagc3H_ly6aUkVbAO_5FdaLtTU7jAzuN1B0WNznwXOjsw0p6eQ5yp-cgkr6baFW074H84_kXBmjIHDhaSgX67I1cE-W0qHRa7_4B4cPZaN_qExGU9rE2Ro9zdg9Ljqcgs5RNOU9Tb4kQJMglVU3kBH5by2wQGqoGijtfIqqzBZBESN2WyBEFuU8VoCd4xOXlVmcb7WsU1TQPG7RnJCpFeXzHPTuTSGhGZY9r69VIynfNPvuEBqlyKC25ynuPFdPenuE_Nz0IgwiK8nHH1UJukSzhmSfHXsUvB_t_MGUQWLTZHp64dOpcADtxLkxrFTBuOuc9E5XCnssc8_b8VBAxoi-68nIUB2Suvwd-H4Ag1K0uTykf7f5nOcT7Vz4vucxX_cristFYfLx9d4PuLgtHs9XIzr2BNeCXzxQthx6RmfxXpgiZ73E5TJUCnvP7mYOXri5vIKedDRt-XiXNkRSo6AAkFb_zdLDR9W1M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کلا کلا آمریکا (آمریکا هرگز)؛ نعم نعم ایران (ایران بله)
🔹
شعارهای مردم عراق در انتظار رسیدن پیکر رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/668295" target="_blank">📅 09:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668294">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
لحظه خروج عراقچی و پزشکیان از حرم حضرت علی ع و استقبال گسترده مردم عراق از آنها
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/668294" target="_blank">📅 09:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668293">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
پخش زنده مراسم تشییع میلیونی امام خامنه‌ای در شبکه عراقی الفرات
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/668293" target="_blank">📅 09:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668292">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
داده‌های ردیابی کشتی‌ها: ۴ نفت‌کش و گازکش از تلاش برای عبور از تنگه هرمز منصرف شدند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/668292" target="_blank">📅 09:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668291">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c4c1d2d8a.mp4?token=KPf4PQ6hOhYzqMNC_YZ1OJFuFn6hXob3NaXoY-G4DStGqPUXxGESnRklw-6qQwT369E03YPBYyUstG-gnv8uctsioVyXIXdYaLqkOrHVC2kWkSKf6IFmXfKYNR8afztL2-nw2E2TP-SIxrQ4T8PluS96gA7XGGME968mm3m__Xn95v2sj4GLhyjUSgwMXyi5s2EDcrTCO-M9oCD6KiAzicgSoA7RonkMN_QLL974BpMCf_J_bgULRj_0wEPiCCZ7vKTB2K4izkcI6vyuuXRAIQqBf_wqXswtY5YPlJsL-a6n1EQdkObapXt4VTBLSPK9YNeW1C3kuLYtcYwbPUqxvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c4c1d2d8a.mp4?token=KPf4PQ6hOhYzqMNC_YZ1OJFuFn6hXob3NaXoY-G4DStGqPUXxGESnRklw-6qQwT369E03YPBYyUstG-gnv8uctsioVyXIXdYaLqkOrHVC2kWkSKf6IFmXfKYNR8afztL2-nw2E2TP-SIxrQ4T8PluS96gA7XGGME968mm3m__Xn95v2sj4GLhyjUSgwMXyi5s2EDcrTCO-M9oCD6KiAzicgSoA7RonkMN_QLL974BpMCf_J_bgULRj_0wEPiCCZ7vKTB2K4izkcI6vyuuXRAIQqBf_wqXswtY5YPlJsL-a6n1EQdkObapXt4VTBLSPK9YNeW1C3kuLYtcYwbPUqxvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری که سنتکام از حمله دیشب به ایران منتشر کرد
🔹
ارتش آمریکا مدعی شده در حملات دیشب ۸۰ هدف را که شامل اهداف ثابت و قایق‌های تندرو بودند از بین برده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/668291" target="_blank">📅 09:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668290">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
مدبر: حتی مسیحیان روسیه، حق ایران در خونخواهی را کاملاً مشروع می‌دانند
روح الله مدبر، کارشناس مسائل بین‌الملل:
🔹
پس از شهادت رهبر انقلاب موج قابل‌توجهی از محکومیت در روسیه شکل گرفت و نه تنها مقامات رسمی بلکه اقشار مختلف مردم و حتی مسیحیان ارتدوکس نیز این اقدام آمریکا را جنایت دانستند و حق ایران در خونخواهی را کاملاً مشروع می‌دانند.
🔹
کسانی که فکر می‌کنند از طریق حقوق بین‌الملل یا سازمان ملل می‌توانند امنیت به دست آورد جاهل‌اند و ترامپ جرئت کرد ارشدترین مقام ایران را که یک مرجعیت دینی بود به شهادت برساند و این نشان می‌دهد که این نهادها هیچ مشروعیت و کارایی ندارند.
🔹
اتکا به کلیدواژه حقوق بین‌الملل یک دور باطل و خطای راهبردی در دستگاه دیپلماسی ایران است که مغایر با منافع و امنیت ملی ایران عمل می‌کند و امید را به یک سراب می‌بندد.
🔹
در طول جنگ‌های جهانی حتی ارتش فاشیستی آلمان نازی نیز جرئت کشتن رهبران کلیساها را نداشت و کاری که ترامپ انجام داد حتی هیتلر هم نکرد و این جنایت بی‌سابقه است و باید به سمت مجازات برود.
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/668290" target="_blank">📅 09:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668289">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltiOn1LTywIpRJvHDRQyH4CS51gA7SnGjcfEASZR0Q96hw4z1ciAX7r-J2OFMMU5qgl55NEXBQgEeKhXO_ui3gcZ45KYMSnaaOptxejDrHZbddHpjz9iuwZDkXPgzUemN4PEnTDAmubkJhedxxVtFEulIhvbMSh-MD4BXyDV9GVrGy8xOZVmBS_e-Gj4B_YMISns9CXlEYGTRVt2IxhanN-Nv54mBtfVk4BFQrdQjIQm46R1copeTIG-VD8V03h369BU_qZnmxyMiFQuI9MtdB8CH6FmvG4NZY9uoRWraKYjPALrS3jr0Ve8c6BxxHMRkE3nI9xpggYzx-u5t2Xy-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هم‌اکنون؛ پیکرهای مطهر شهدای خانواده رهبر شهید انقلاب در جوار ضریح حضرت عباس علیه‌السلام؛ کربلا
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/668289" target="_blank">📅 09:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668288">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
قاب متفاوتی از لحظات ابتدایی تشییع پیکر رهبر شهید انقلاب در نجف اشرف.
۱۴۰۵/۰۴/۱۷
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/668288" target="_blank">📅 09:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668287">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e2c9bfc0f.mp4?token=wBgGSIz2oYcP1_BaKvj1p3btpphsnklp90i-qua_iFl1WlmNOVj25fU6qVYhnaejWfr_rvl8zTLEoTt062keRPIn51ytIA-t0haeTWt-Yr9c_IdAG8GugdsfVczfysKCUqrFg6QFz4hCx0TZO9u10cM7uZfF-gViiBNE658wrbegjvZ8IgVaTVXMSDQdFTZW3sQs5ej9bsURCYZPSZv6LA98SWfG-IYaNGMoFTxDFmc0-aAkpPuldm3XB8KatpQ5KUqbRsdtXNWhxgxURvSO6xqWxbqo3n2dvX_48bEsm1kJ6ePiVw1PeX_q-JihoWDUeW2Y4istgaXyZHFIUDuV0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e2c9bfc0f.mp4?token=wBgGSIz2oYcP1_BaKvj1p3btpphsnklp90i-qua_iFl1WlmNOVj25fU6qVYhnaejWfr_rvl8zTLEoTt062keRPIn51ytIA-t0haeTWt-Yr9c_IdAG8GugdsfVczfysKCUqrFg6QFz4hCx0TZO9u10cM7uZfF-gViiBNE658wrbegjvZ8IgVaTVXMSDQdFTZW3sQs5ej9bsURCYZPSZv6LA98SWfG-IYaNGMoFTxDFmc0-aAkpPuldm3XB8KatpQ5KUqbRsdtXNWhxgxURvSO6xqWxbqo3n2dvX_48bEsm1kJ6ePiVw1PeX_q-JihoWDUeW2Y4istgaXyZHFIUDuV0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بدرقه باشکوه رهبر شهید با حضور گسترده مردم عراق
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/668287" target="_blank">📅 09:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668286">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NbMoHvDPSwCK7LpnH4FeARig4Vg2JugiDRLxC4WKN7s8ljpPsrEFLSperASJRYt2ASdsPQz-o0sWfpyG0Tj574Z42t9eCpSAQ5zPXTOv-6jzi-EOpw-yr8yOYhmaDkFgD7fa749-XI2ZyH2RQHCth1rPOE9zRTjKxtNm-RSqDxGLJOIJEcbJ6ntb1wwd6CaVuMevpLcAeZ3qSuu5Up1icW3WarerqVe8RGtCnkbKNGuYakTbZrxgwqll7OchUgEVJPV79Ahm9JHTpi_v-7uX5yUGhtH5ULN9C9A-hMkxAYO_CuDhUkrSzQi8G5d5DSmdybj2tpsmX7N5XkEVJgJ7qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه بازی‌های مرحله یک‌چهارم نهایی جام جهانی ۲۰۲۶
🇫🇷
فرانسه - مراکش
🇲🇦
📆
پنجشنبه ۱۸ تیر - ۲۳:۳۰
🇪🇸
اسپانیا - بلژیک
🇧🇪
📆
جمعه ۱۹ تیر - ۲۲:۳۰
🇳🇴
نروژ - انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
󐁧󐁢󐁥󐁮󐁧󐁿
📆
یکشنبه ۲۱ تیر - ۰۰:۳۰
🇦🇷
آرژانتین - سوئیس
🇨🇭
📆
یکشنبه ۲۱ تیر - ۴:۳۰
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/668286" target="_blank">📅 09:08 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668285">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2615cddda.mp4?token=jEYFRC1-SW61DKWeWeriUC2pJtlJRo7geE7szHFKKUs7jUCUEIg-q6H-3ufFriCM3NhB1uZHwmoAQi8n2-O5u1iA0Ezg6A4aHUdt8YQ81bMPzQuZrNr-6yeLW3oC-LbRdxOPUoA4tEZva6naALKXDrUqOvF1-79CXPLPyAlXzpUoe5czfLzMl-e79Ta2OVmkQYNH4N2kkvSmNseEl9i8IpIz2_6HgXaV9vTELqesopIFvFEsdFwhPjAWQCowSWoLsCXKkRjE7qctRNtNFv3EM7fl0xFw4vJo_JitbDr-DrrIP_YXfOQqvnsGfXi70Yei-9OIagpIBDgn9RkNMgdJwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2615cddda.mp4?token=jEYFRC1-SW61DKWeWeriUC2pJtlJRo7geE7szHFKKUs7jUCUEIg-q6H-3ufFriCM3NhB1uZHwmoAQi8n2-O5u1iA0Ezg6A4aHUdt8YQ81bMPzQuZrNr-6yeLW3oC-LbRdxOPUoA4tEZva6naALKXDrUqOvF1-79CXPLPyAlXzpUoe5czfLzMl-e79Ta2OVmkQYNH4N2kkvSmNseEl9i8IpIz2_6HgXaV9vTELqesopIFvFEsdFwhPjAWQCowSWoLsCXKkRjE7qctRNtNFv3EM7fl0xFw4vJo_JitbDr-DrrIP_YXfOQqvnsGfXi70Yei-9OIagpIBDgn9RkNMgdJwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور آیت الله یعقوبی در تشییع میلیونی قائد شهید امت در نجف اشرف
🔹
آیت الله شیخ محمد یعقوبی، از مراجع عظام تقلید و شخصیت‌های برجسته حوزه علمیه نجف، امروز (چهارشنبه) با حضور در جمع میلیونی عزاداران، در مراسم تشییع پیکر مطهر امام امت، آیت الله العظمی سید علی خامنه‌ای در شهر مقدس نجف اشرف شرکت کرد.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/668285" target="_blank">📅 09:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668284">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bc54bca3f.mp4?token=cfub_XH9sVOp21fUCMe01BinMeJUwNwtqN8cJrNc4IXQuO7k848XwGyGcBRNmSlCfEzTSHOJWBu0NqMUYJjeOCBOcPo4Wlyh48deapxhc2V5-lzdR3YG-ZH_BVutglCl8rOjfgR6l1o8S-YVMpRwVkiWX6XW_VZuiVVs2rTTUuDw_GRqUmLr0uadc5YRyBKmfZjjsuhIWjcFNzjF5AsA2pSqguP9nZ77OcQ6QclWorOdIC7QnLxayjAM4zvjWU4GqzdWYzrAfj5I2f-HYOEPQIHMBRGBUpuWAe7xjhKpvm39ymTnYtJ4KdH_mID-wWPBxfaM99hZp7x_dXfbpELHmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bc54bca3f.mp4?token=cfub_XH9sVOp21fUCMe01BinMeJUwNwtqN8cJrNc4IXQuO7k848XwGyGcBRNmSlCfEzTSHOJWBu0NqMUYJjeOCBOcPo4Wlyh48deapxhc2V5-lzdR3YG-ZH_BVutglCl8rOjfgR6l1o8S-YVMpRwVkiWX6XW_VZuiVVs2rTTUuDw_GRqUmLr0uadc5YRyBKmfZjjsuhIWjcFNzjF5AsA2pSqguP9nZ77OcQ6QclWorOdIC7QnLxayjAM4zvjWU4GqzdWYzrAfj5I2f-HYOEPQIHMBRGBUpuWAe7xjhKpvm39ymTnYtJ4KdH_mID-wWPBxfaM99hZp7x_dXfbpELHmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پخش زنده تشییع پیکرهای شهدا از بیلبوردهای نجف
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/668284" target="_blank">📅 09:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668283">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
حمله موشکی و پهپادی به کویت
🔹
منابع خبری از حمله ترکیبی موشکی و پهپادی به اهداف نظامی آمریکا در کویت خبر دادند.
🔹
همزمان با فعال شدن آژیرهای هشدار در سراسر این کشور، گزارش‌ها حاکی از وقوع انفجارهای شدید در مناطق مختلف است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/668283" target="_blank">📅 08:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668282">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1241767cce.mp4?token=UvOqucTqEiz6RhzTh-BH3orRn7vZFEzPZ-MKf4jajAQKfvp6-sFp6569L7GqJI7oS78T8xywqR9ieA0vzwMzTxEroq3bUoeRZt3wHa34dU73YCA2ZxWzcLO-RVYh-PU47VA3cIcY2bvabM8mFkNOxMHEgnh3XUMHQ0bH8Gyr5BFAlSRTzL2gXeaYdetzTeac-z5KZ11vYvpaaRdK_wDjxV0TK3KcI2V-RZDfwTS4JorMry9NfuuGUKPTtuMed-BIsLnBVVs5txP9e2x5PuMpGgHKvz9uu0dCPhSsfreLfaoKXg3b5dA___GZ-mvaWDHjJSAdU05L9_5k-bltyHZKTVLKePL1lp-ExAyvZ-hIQgu-y0ZkTLHUpz7_-va-9lLrdQ5lQPJgvOkQNgohHZYiqaU4aI89m5ssMIvAd4bjNnA3uN6vTApovZAtffZmjbGsld8JGUkjWcZHhjxC8wwtOsGe_SctdNhDKVDs_L9dUOBghX4ZgqX77w3Ud2H8qyAbNyagmNKaNqd9cSlFXXyEE7r7KcXsFcwGxxlpJpLUUJ_BLboBRjV4eWt8GieVnXvVMnETooj67N0OJ8FCR23ZbX4TuoRGOw11jLHdoYX2g8ZolgSSgaIrYAFxpRSi01GI_YBMuwKKLHM-ChnB4De3WPqOD7jGTKv1dekLGwz910g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1241767cce.mp4?token=UvOqucTqEiz6RhzTh-BH3orRn7vZFEzPZ-MKf4jajAQKfvp6-sFp6569L7GqJI7oS78T8xywqR9ieA0vzwMzTxEroq3bUoeRZt3wHa34dU73YCA2ZxWzcLO-RVYh-PU47VA3cIcY2bvabM8mFkNOxMHEgnh3XUMHQ0bH8Gyr5BFAlSRTzL2gXeaYdetzTeac-z5KZ11vYvpaaRdK_wDjxV0TK3KcI2V-RZDfwTS4JorMry9NfuuGUKPTtuMed-BIsLnBVVs5txP9e2x5PuMpGgHKvz9uu0dCPhSsfreLfaoKXg3b5dA___GZ-mvaWDHjJSAdU05L9_5k-bltyHZKTVLKePL1lp-ExAyvZ-hIQgu-y0ZkTLHUpz7_-va-9lLrdQ5lQPJgvOkQNgohHZYiqaU4aI89m5ssMIvAd4bjNnA3uN6vTApovZAtffZmjbGsld8JGUkjWcZHhjxC8wwtOsGe_SctdNhDKVDs_L9dUOBghX4ZgqX77w3Ud2H8qyAbNyagmNKaNqd9cSlFXXyEE7r7KcXsFcwGxxlpJpLUUJ_BLboBRjV4eWt8GieVnXvVMnETooj67N0OJ8FCR23ZbX4TuoRGOw11jLHdoYX2g8ZolgSSgaIrYAFxpRSi01GI_YBMuwKKLHM-ChnB4De3WPqOD7jGTKv1dekLGwz910g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اهتزاز پرچم «قوموا لله» بايد برخاست در مراسم تشییع پیکر مطهر رهبر شهید ایران در نجف
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/668282" target="_blank">📅 08:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668281">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874542565b.mp4?token=HiwrC9RwExxi3_2DCIpzg4Ugo2N-tYW5tBvUnFOIVK2W_RDM2uYwvBCybLm_wJS1_-2YRapPsk8OCPTtOarj2QjYFLUea-6UAJj175IF2Q_AjowSGQZRH3vz3cwfpgFW0xOit05CQQhCbJI08-jXFavDKWvJOD_0Pp1Fa3fkAfmJKntLeS_jYPHJDzJ_6CEipWlELe8aPtdd5KlABSp8ywZKa9eSY7rmNygfc-lE907y1OMV7gIoLahhXzxsLYp7K8BLvpNZqOdBmo0gsXN1y8VTcDwxuD4sA95R29-nfWkqHHjP4k_eWsCUqp__93AD6YckLfkjMH_78-_JRw3qew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874542565b.mp4?token=HiwrC9RwExxi3_2DCIpzg4Ugo2N-tYW5tBvUnFOIVK2W_RDM2uYwvBCybLm_wJS1_-2YRapPsk8OCPTtOarj2QjYFLUea-6UAJj175IF2Q_AjowSGQZRH3vz3cwfpgFW0xOit05CQQhCbJI08-jXFavDKWvJOD_0Pp1Fa3fkAfmJKntLeS_jYPHJDzJ_6CEipWlELe8aPtdd5KlABSp8ywZKa9eSY7rmNygfc-lE907y1OMV7gIoLahhXzxsLYp7K8BLvpNZqOdBmo0gsXN1y8VTcDwxuD4sA95R29-nfWkqHHjP4k_eWsCUqp__93AD6YckLfkjMH_78-_JRw3qew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمایت ناتو از حملات آمریکا؛
گزارشگر: واکنش شما به حملات اخیر آمریکا به ایران چیست؟
روت، نماینده ناتو:
🔹
به نظر من، این اقدام کاملاً ضروری بود. ایران، آتش‌بس را نقض می‌کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/668281" target="_blank">📅 08:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668280">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
تداوم انفجارهای شدید در بحرین
🔹
منابع خبری از شنیده شدن مجدد صداهای انفجارهای شدید در بحرین خبر دادند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/668280" target="_blank">📅 08:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668279">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
المیادین: استانداری کربلا حضور ۷ میلیون شرکت‌کننده در مراسم تشییع پیکر رهبر شهید انقلاب را ثبت کرد #بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/668279" target="_blank">📅 08:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668278">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ae4eb2dfe.mp4?token=gQa8el3GqocQDKGMRyBGTJ3pkVYmw2_HkMClvuUDOaMy8nwBz41eOi6I9cAJDro0oZPfTGQ1gLVvqpfZfrfA6ePngjLT-RN4lOD9e_28qnq4DFQV9mUjsqxhnH0zE9WTljoreYHNIPI1GmEcvgQYiORJsaA3Ykeu_hNUvkOQIWS5basYmdzfT3pFN0OtGPOc2gLt6Fzxy_kkN7PkGven7nz7u18CxRuPwRhvzqfqKgMsYXkEmJWBKiufwaRraa2o-A3WqPStXY8hGQRJHBVwOqV4FeHJfPpjDD-bhj4mboxik3zUfCEFB8hkj25lDmRHUGXBMcLbcAvDbJaMyUI3N57VBjCAI1yubMs73m3epImiWRE670ZQaywzXFbeeO2FKIv2C4r2AFPCQyx1vy3HLbZWXeyc-HN4J0K0FuwizvSBPSDwM35GElzVEL-DxAY1hKdZi4wSD7UB88UJdd6sUmA4Z_Z6Mb7iMcrj8vAL9F9lP1aO35Q9xLuhaFWE0FuFkrwLJVGKALz3MvyKT2xOkwJShIXKHnLs11yFGsmGAEUUwzB1JHGff1WTzN-3-CqPjcBBikTfm786d_F6jBtL3l10qj2YQ1FbbyiBgjLhfjSJ3oP3MIla7zZuSZoTMNAB-B6OHCq4WCEFW8KSA2hnkgzQp4IEArgo66hVkD9r8kE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ae4eb2dfe.mp4?token=gQa8el3GqocQDKGMRyBGTJ3pkVYmw2_HkMClvuUDOaMy8nwBz41eOi6I9cAJDro0oZPfTGQ1gLVvqpfZfrfA6ePngjLT-RN4lOD9e_28qnq4DFQV9mUjsqxhnH0zE9WTljoreYHNIPI1GmEcvgQYiORJsaA3Ykeu_hNUvkOQIWS5basYmdzfT3pFN0OtGPOc2gLt6Fzxy_kkN7PkGven7nz7u18CxRuPwRhvzqfqKgMsYXkEmJWBKiufwaRraa2o-A3WqPStXY8hGQRJHBVwOqV4FeHJfPpjDD-bhj4mboxik3zUfCEFB8hkj25lDmRHUGXBMcLbcAvDbJaMyUI3N57VBjCAI1yubMs73m3epImiWRE670ZQaywzXFbeeO2FKIv2C4r2AFPCQyx1vy3HLbZWXeyc-HN4J0K0FuwizvSBPSDwM35GElzVEL-DxAY1hKdZi4wSD7UB88UJdd6sUmA4Z_Z6Mb7iMcrj8vAL9F9lP1aO35Q9xLuhaFWE0FuFkrwLJVGKALz3MvyKT2xOkwJShIXKHnLs11yFGsmGAEUUwzB1JHGff1WTzN-3-CqPjcBBikTfm786d_F6jBtL3l10qj2YQ1FbbyiBgjLhfjSJ3oP3MIla7zZuSZoTMNAB-B6OHCq4WCEFW8KSA2hnkgzQp4IEArgo66hVkD9r8kE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم اکنون؛ خیابان‌های نجف اشرف مملو از تشییع‌کنندگان است
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/668278" target="_blank">📅 08:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668277">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
سقوط یک هواپیمای باری با ۵ سرنشین در دریای عمان  ادارۀ فرودگاه‌های پاکستان:
🔹
این هواپیما ساعت ۲۱:۱۸ به وقت اقیانوس آرام از شارجه به کراچی در حرکت بود، که مشکل سیستم ناوبری را گزارش کرد و بلافاصله توسط مرکز کنترل ترافیک هوایی کراچی راهنمایی شد.
🔹
در ساعت…</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/668277" target="_blank">📅 08:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668276">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
رئیس‌جمهور لبنان برای پیشبرد توافق با اسرائیل به واشنگتن می‌رود
🔹
خبرگزاری رویترز به نقل از یک مقام ناشناس کاخ سفید گزارش داد که جوزف عون، رئیس‌جمهور لبنان، برای ۲۱ جولای(۳۰ تیرماه) به کاخ سفید دعوت شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/668276" target="_blank">📅 08:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668275">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
الحدث: آژیرهای هشدار مجدداً در بحرین به صدا درآمدند
🔹
منابع خبری از شنیده‌شدن صدای چند انفجار در بحرین گزارش می‌دهند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/668275" target="_blank">📅 08:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668274">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfcdfebc55.mp4?token=Uk8qbqwfn-K2kZAH7sAZYUZsEQDMVhV6W9wZtqIyWEI_s8k9cAs1ItIdqu3s9DaqYOABVhE6OF10GgOmatmSRPqyLk8i3nkJUgclN-830kXWI8uGvhjXhvCO7DB17QfXlONHeF4n_0PK1g-FXDFrw7rF0wkDOu7LibQOVy2bxOiow-YAVn5D2QYq0HJtrcDSjEkrLbWseWORfGIpfPkPHDs3-Bw3QyIthj9fhcSZ2hWe9OQplh21YCRevQnXV45upVrGNy5dRp-CdAjR70EKLtp2l9Wt8Nb_pHfHeCN3NgVKXzmDUweqtqZDlE54JiGpoEPBftvAn0Q4-M1vvc5INA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfcdfebc55.mp4?token=Uk8qbqwfn-K2kZAH7sAZYUZsEQDMVhV6W9wZtqIyWEI_s8k9cAs1ItIdqu3s9DaqYOABVhE6OF10GgOmatmSRPqyLk8i3nkJUgclN-830kXWI8uGvhjXhvCO7DB17QfXlONHeF4n_0PK1g-FXDFrw7rF0wkDOu7LibQOVy2bxOiow-YAVn5D2QYq0HJtrcDSjEkrLbWseWORfGIpfPkPHDs3-Bw3QyIthj9fhcSZ2hWe9OQplh21YCRevQnXV45upVrGNy5dRp-CdAjR70EKLtp2l9Wt8Nb_pHfHeCN3NgVKXzmDUweqtqZDlE54JiGpoEPBftvAn0Q4-M1vvc5INA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌اکنون؛
انتظار جمعیت عظیم مردم عراق برای استقبال از پیکر مطهر رهبر شهید انقلاب؛ مسیر تشییع، نجف اشرف
. ۱۴۰۵/۰۴/۱۷
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/668274" target="_blank">📅 08:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668273">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
سپاه: حمله به ۸۵ هدف نظامی آمریکا در پاسخ به نقض آتش‌بس  سپاه:
🔹
در پی «نقض آتش‌بس» از سوی آمریکا، نیروهای دریایی و هوافضای سپاه در عملیاتی مشترک، ۸۵ هدف نظامی آمریکا در بندر سلمان، بحرین و کویت را هدف قرار دادند.
🔹
همچنین یک پهپاد MQ-9 آمریکا نیز سرنگون…</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/668273" target="_blank">📅 08:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668272">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a11aafb0f2.mp4?token=d7N99i6b_D9R16s3PsR4d2JcUTAZSoShWH2oiA1k9na6Lm172LSYhLPDUd7K-4MRLZ3BgByppOMLER9Vk2RO9fkY6-4lfDE7JtWIgVMJJ_AwmmHsRBHW40djYWmwRwOW3zZuosbE6dAFqFX7EruOeIaseu6rSFaJqY0MZjAUAWOlV34OWlP88Lo5aqntBf15oE_HhUtzupNdLXxMuM3oNpzuZ3sPQFaRKB566JBx8a6ETcBu2A8gwZuu889VI2mYwsrqO9KaXaoLz1Eh6Kj25G2hZ_un6IbyJhJNq9uCjszog9FJG66G1F8RCQYZlqkHkFRjgEK3jIPeIYZfFhJYww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a11aafb0f2.mp4?token=d7N99i6b_D9R16s3PsR4d2JcUTAZSoShWH2oiA1k9na6Lm172LSYhLPDUd7K-4MRLZ3BgByppOMLER9Vk2RO9fkY6-4lfDE7JtWIgVMJJ_AwmmHsRBHW40djYWmwRwOW3zZuosbE6dAFqFX7EruOeIaseu6rSFaJqY0MZjAUAWOlV34OWlP88Lo5aqntBf15oE_HhUtzupNdLXxMuM3oNpzuZ3sPQFaRKB566JBx8a6ETcBu2A8gwZuu889VI2mYwsrqO9KaXaoLz1Eh6Kj25G2hZ_un6IbyJhJNq9uCjszog9FJG66G1F8RCQYZlqkHkFRjgEK3jIPeIYZfFhJYww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فریاد «لبیک یا سید مجتبی» در مراسم تشییع پیکر رهبر شهید انقلاب در نجف
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/668272" target="_blank">📅 08:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668271">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
المیادین: استانداری کربلا حضور ۷ میلیون شرکت‌کننده در مراسم تشییع پیکر رهبر شهید انقلاب را ثبت کرد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/668271" target="_blank">📅 08:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668266">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y7h31jJyVcLteO6-GA8DCszM2w4OW9I8__oiqBVzi0hqwMJjg7M50EboDC5m1tlTNRGw9fyV81MmB6aEVWL4ukOqkQuB0rH4EVYiZdHtU7CSxrJXhlDQwfawBkwC0WbaflDf7hU02sMuDlpWzbBx8-9-ibI6KmAn8iiCcbzOP2VhNUHB--oABtn1HVWkU78a7kfQxezt_AMEqzD5vCWoZbK_gKP7C6aPlUPzLAYmHvFWW5kJn3SrgP9jx-wnRJlBxMfDHeABQ72RC8hDX48dMmnYVo2wLi-x9ccq9jHQ0oFu7y9bK2q42uOcpWnHYoGBEB_Q-HYp4kBpuyruZ2ouYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GbfmjM9SB-6Sli3GplF-y8LfV0_1Rd6PWV_kooa1BTwtSSA5c-irchxW-kbJJSt1DnMV5RDqcTAJRFHV2ZN_8VIhhn9B_tAKrhTAS5bItzJbvJJUT3JGJ5-6jhWpRV7YNppte-HlB-SfpSHSnW8GdQ3A1BZofwD-BV1TcyXk70s3jlPpW0vTe_-gd4d8xtU-Fsxc6edV34oFQW_ntZ2xgmGBD3TvRin79iFBugb2nZoFv11xUfprcQChURIAtskOD36MT1lpiIGLXADG4VMMbjZd-rGG_dO264OuwYE85rtEBe91abjBZm4mqY-T0qBZ0mIGIH5mUWbZqqLb_gqS0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mQx9uleLrVPNCQ8dc0bNCMmIy5fshCAVCTHDX37t2PZ8VdoZUZLgcMQmpHlvH9cZuGIXUIrljh0Rp8GotU_-IE9p8tRhaASX6HCs95qJ4Tts1vokCDHkWuhh_ueV2EfQApO5wZKkLGNl8Wiu-lD9p2u4D2O2bClVIZiSl9Lk0on0N1frJO-TcORhzYp2GhQnPXW0iTHym-TEKXEflUJ907MNVxptM4GNbp-R5RK-TUMSFALUaVXVUDsix_Gz67gxQ27wDmb5d7OFb_5icUP4k7mJYLHZ9sNm2GRJ19XPNldpwTcRxyf1-vWOvzeEaEDyEiKkXnCCvzMAkyApVV7NuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yj__doB1IpOFOWd6ABQZT80rZtfwyQx9sbmK7OW76UvWx2EUlEqhXIDnhUuPblle_qPooudxBJQ_ndztd3qU1opAh7y7Ojav5Jt2x0Lc5lfum4qZI7RdTTEcnDQyTIrNoXuQZ4X_tkm_aWjW87FywQPaZomqwjEx4_71imGgkb1mf46HXwRTmSaQyhf5eY5m9aTbXFhmAa8AySIhqLUqrUfhGnmZH2hWPrwKiRDU0zSyzYQhhFVC-fqv_1oVKg6g9ZCYb5AxzGbAKOwc9u0x0MLPi_1cDYZBeZLGrLRS3UjHypruQC-bivM0CzTEyBksLcjkuZ175FNvnD8ejGAIGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hIDtTg71gSgl0KqB3n42JZ9ytM51BeQbQgIJbm2BKykU0OciZJhPgizsuiCAy7DPlf_fQbUCX77K2fJQLzljBNa5T-TnOfnSrsrIi9wT_LFDXtZCvBjbW1sxP2piLd34aDNocxMcYeqZXJyFkBFlrNPXNhGGpCznj-ef1ixb7UcqMy8fZdmuiHVYIFLHZ1n2pYXb-BRodZ6fKUVFj3UA3NiFxgt8VkekzMW2DbaWENGHxPixl83r6pKuUi5OSspU0Ri7bDvPXM79BDopaIObiiemBpCNZvxc8ye4BLkjsQfbBSpkZps5-oX6NFv9NG9OfElahhpGSMi_nkGaOnylyg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
سیل جمعیت عراقی‌ها در تشییع پیکر رهبر شهید امت اسلام، در نجف اشرف
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/668266" target="_blank">📅 08:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668264">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DhukctfzmuHUDuBZBnXCri1KvUsnweKXg8UiGxz8KIHGNmIoXjXlzZNpYGzUb6EMyZZtZZyvUcZyZl9t-ZT-PXY55DIPqWzQCKDTvjFyzAru9Q3ASooGjw28te7_AqjYsdDTo9ZwnpWcMwymb9dSkFDu3EkHb76V2OANihVe_MDaqwm96los6dvte1mrt65S0SOkwgfzMIYKzkos3hHaGVsL8S0xHLOasZJBZcyHeCR3_iajH9aAtktcGaTKrAYLmrZU95C4LWQpLfI1TmXsBMlfz2Y9NA7hV6ApyBcNbdpgI2JxD2duaKZH5_FF038bIH65Wvo6GsgK4FvvF2-Rrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ow5Oc9IoMYulEBl32Sa2WZtt-p36WNBLgvBo35AuG8X40E5oeqOIE9BMzReydvnitWlxlgWeEZ4uos8B4cjEuDqKZHV8_I-gs7b8Js1wJallggZr9068Eb5Z_DscXyD3hP-jxqJsEwqt0rlSTox06z5LfWHUImRISYxbBy1bP2HyhEByBTFH2BE15MNLR9rtRxp_fDUHSCMN5YmCB0jMVSr0HELGy5A5AoHph7ddk4nXsgdczBjxpQBBPgxxHdAz1hADwSTQ6n-4PsL29oiNeUUtFWOYhddEwgPLnSQT2QnpLNLKvPdWuDxF_W0LQtvFn16mWeqfbBaWlLijfe6Ekg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حضور سید عمار حکیم، رهبر جریان حکمت ملی عراق در مراسم تشییع آقای شهید ایران در نجف
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/668264" target="_blank">📅 08:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668263">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21ff16f06b.mp4?token=acCaLaFHfc5mKkVByt2BTFIe4Wtf0HCDi5KyESIJteHHDVw5YGfAU8e5NZmAlC7w_JQoE-TQW3eW22M5lhz2ybd21wk_QXXNmkpd73whRwsGX3gBnS_08N3nIHfwkjYQPzI2tySrS2wydy6vI8fR5dccgiwz45bMSGZHuFiI8gYhZVrAU-FdnldtjQmcKoprhBJhHrlWVVWPrJag7t_cKjEA9yuXEBmrkOZuGGGgo4zI7asQo_XeiZmDc11t2xsnRsMbfTm96_63HJiwQ_QaS7mbOa1KP5HVfLs6vNCDrorTSv5HQUbPRNfMUpNKJDd-68iZqp_Z8d6VxeNx3pKOVCXZ4uWkDPWeMDQz2h5ppy3pIg5DpbUvKtZAN4ixNw3YxrCLvEnQFizVWeNdfGOIjm5VW_wcqhACdXpun5NWAe1VRxV3l2kqTCjY3FEGBL3Ywg0-SLyNDt9k6whfCsybRye6e-oTJyh6iWbfvUXQ4t1NeYoA6QAnYhuCKQb6rSep2vx_CAvcTQtpCSE7H6ZR_EWtGzUfMlpLeTelNScj-f_yvhdeRUaKaT2L87g07_fhIfMxXURUCnkHz30MB-lre2Kv3Cvt9d9ifaz3TweRPKBtjO1_TJgKgUc06K_3ZRMvQ8eMeeMZjkhC1DOjiU3PZWzdhh_1fkIDkP0LijjhdGk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21ff16f06b.mp4?token=acCaLaFHfc5mKkVByt2BTFIe4Wtf0HCDi5KyESIJteHHDVw5YGfAU8e5NZmAlC7w_JQoE-TQW3eW22M5lhz2ybd21wk_QXXNmkpd73whRwsGX3gBnS_08N3nIHfwkjYQPzI2tySrS2wydy6vI8fR5dccgiwz45bMSGZHuFiI8gYhZVrAU-FdnldtjQmcKoprhBJhHrlWVVWPrJag7t_cKjEA9yuXEBmrkOZuGGGgo4zI7asQo_XeiZmDc11t2xsnRsMbfTm96_63HJiwQ_QaS7mbOa1KP5HVfLs6vNCDrorTSv5HQUbPRNfMUpNKJDd-68iZqp_Z8d6VxeNx3pKOVCXZ4uWkDPWeMDQz2h5ppy3pIg5DpbUvKtZAN4ixNw3YxrCLvEnQFizVWeNdfGOIjm5VW_wcqhACdXpun5NWAe1VRxV3l2kqTCjY3FEGBL3Ywg0-SLyNDt9k6whfCsybRye6e-oTJyh6iWbfvUXQ4t1NeYoA6QAnYhuCKQb6rSep2vx_CAvcTQtpCSE7H6ZR_EWtGzUfMlpLeTelNScj-f_yvhdeRUaKaT2L87g07_fhIfMxXURUCnkHz30MB-lre2Kv3Cvt9d9ifaz3TweRPKBtjO1_TJgKgUc06K_3ZRMvQ8eMeeMZjkhC1DOjiU3PZWzdhh_1fkIDkP0LijjhdGk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شب گذشته؛
تصویر هوایی از پیکر مطهر «آقای شهید ایران» در آغوش مردم عزادار عراق در فرودگاه نجف اشرف
. ۱۴۰۵/۰۴/۱۶
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/668263" target="_blank">📅 07:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668262">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec2b9692df.mp4?token=R9qiZsoeX2Zosq-vvqqtUZtJWfw3Lg6ClPjfLWHwlVJ--glX_9s0mEMEk9zvVybesQ191FZnSIW8LkjKdYbhcuGynuZMqXkw0K55l0-9jcd0RgOfHWGcGMaNi8Vp3wnhdbNUw6aJ4KjVVXBR6ePVrVyFN-AfsB-G5up7MHqksRM7zsO8uEZw5aKfzPbvnepzUPvwR94gfzVj59bAZrS6wJHDe0uxiZNvwmMjHvsnBK-DRg7uVv6fi1eN_a1gteqjsvgYgIr5orDx4dflvWkPAIaZ0WbeejKSvrNLtX50WeJrYWUzrmGbyoFf9M6czCrelly_jDQ6kW0wmP8rkjfAmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec2b9692df.mp4?token=R9qiZsoeX2Zosq-vvqqtUZtJWfw3Lg6ClPjfLWHwlVJ--glX_9s0mEMEk9zvVybesQ191FZnSIW8LkjKdYbhcuGynuZMqXkw0K55l0-9jcd0RgOfHWGcGMaNi8Vp3wnhdbNUw6aJ4KjVVXBR6ePVrVyFN-AfsB-G5up7MHqksRM7zsO8uEZw5aKfzPbvnepzUPvwR94gfzVj59bAZrS6wJHDe0uxiZNvwmMjHvsnBK-DRg7uVv6fi1eN_a1gteqjsvgYgIr5orDx4dflvWkPAIaZ0WbeejKSvrNLtX50WeJrYWUzrmGbyoFf9M6czCrelly_jDQ6kW0wmP8rkjfAmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراق، میزبان وداعی که تاریخ فراموش نخواهد کرد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/668262" target="_blank">📅 07:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668261">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/801ccce70b.mp4?token=AeYXVwMj5QGcTHaNTGxTKah3lr6ScVR8A_-bidtmB4aNPwyiO0YCx3DfWhDEZdtD8277AQWfNRXAI3lcosckj9Y3_knzF3QAA41_Ya4AFuuuVrrMuLnIzsuiZqU-iFjmVWo1XRI-l4mONOcqpDsth_vRg_608H560FjjNaUDgOV9FPToKAFNKyKz0FAz_8thG7be2CBm8yujjT2mMqeMBSWWFr8szHtgNlYazbhfqYBq2RzXz7KPl9kVjgfJxfKHsg2TFrA04L4fBGkwdfag8hy6y_c2QnJQWUpDqaQU9x1bak8vbSfDvltSekrKnnToVgJn-oUSfGwhOgjtpKijpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/801ccce70b.mp4?token=AeYXVwMj5QGcTHaNTGxTKah3lr6ScVR8A_-bidtmB4aNPwyiO0YCx3DfWhDEZdtD8277AQWfNRXAI3lcosckj9Y3_knzF3QAA41_Ya4AFuuuVrrMuLnIzsuiZqU-iFjmVWo1XRI-l4mONOcqpDsth_vRg_608H560FjjNaUDgOV9FPToKAFNKyKz0FAz_8thG7be2CBm8yujjT2mMqeMBSWWFr8szHtgNlYazbhfqYBq2RzXz7KPl9kVjgfJxfKHsg2TFrA04L4fBGkwdfag8hy6y_c2QnJQWUpDqaQU9x1bak8vbSfDvltSekrKnnToVgJn-oUSfGwhOgjtpKijpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور مقتدی صدر در بین عزاداران رهبر شهید انقلاب در نجف
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/668261" target="_blank">📅 07:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668260">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a6ecd8e54.mp4?token=ndmY-e9t9jUijg2mzWxtPFNnZDmn3KhPfX_37y9GYWJMTiJaftogOKgRTXSKKSDnpT2z7UmSsyJstZcBAAkvonsA2e_UzxTk9cF8MvWdde1wZvLfudCoZjUJONXFoELuXP1URMmEkyeVOpzzJggc4KYMzHuEpMOSa9lextn7y8tHaup_qEfFIRwgn4E7K76ScESTozI8hWenzu7S0lkF0IQDQHTf_dH-MNdvi3jvueoz1kA6fGho4b2qqFQ2sMOZnVBHOyf7IyLbNcrrNWQpH7n5yJ4Lxy0jQR1uFDWgDB21vfjNho2y4xnkJhkuscIinDDdFkKV7qFvpGBtR9SDwZupepMSxseltQO_W7OHXGFU7HzYYEz9LEAaYDS_LZOimtayUNpiUgrbbmblIKRLZjUZa1qm9cOb0bLfLvL95DNWuMUNnqFbG_-jYyzuVEFpWDLRulr56kCeGjKDD7FnBqEGySUZlwusEsfQlPTOdC1A9viQDqairUQbaqz4K7BXzn-_mGLJ9szckJR6kX5jOfdUbOj8D9iQ0KYyd-9gbeWmaHe74m6dnMS_9KJoqTrxw3R-4GClWsOnm1vohqWzW3lodJGfMaWc7fjIGdMWZ-cCvCubFEms0A83d_UEgC51Blt5G90kSj5G3CqC1Xi7v3v7q0LC0T83SYnpRRpQkVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a6ecd8e54.mp4?token=ndmY-e9t9jUijg2mzWxtPFNnZDmn3KhPfX_37y9GYWJMTiJaftogOKgRTXSKKSDnpT2z7UmSsyJstZcBAAkvonsA2e_UzxTk9cF8MvWdde1wZvLfudCoZjUJONXFoELuXP1URMmEkyeVOpzzJggc4KYMzHuEpMOSa9lextn7y8tHaup_qEfFIRwgn4E7K76ScESTozI8hWenzu7S0lkF0IQDQHTf_dH-MNdvi3jvueoz1kA6fGho4b2qqFQ2sMOZnVBHOyf7IyLbNcrrNWQpH7n5yJ4Lxy0jQR1uFDWgDB21vfjNho2y4xnkJhkuscIinDDdFkKV7qFvpGBtR9SDwZupepMSxseltQO_W7OHXGFU7HzYYEz9LEAaYDS_LZOimtayUNpiUgrbbmblIKRLZjUZa1qm9cOb0bLfLvL95DNWuMUNnqFbG_-jYyzuVEFpWDLRulr56kCeGjKDD7FnBqEGySUZlwusEsfQlPTOdC1A9viQDqairUQbaqz4K7BXzn-_mGLJ9szckJR6kX5jOfdUbOj8D9iQ0KYyd-9gbeWmaHe74m6dnMS_9KJoqTrxw3R-4GClWsOnm1vohqWzW3lodJGfMaWc7fjIGdMWZ-cCvCubFEms0A83d_UEgC51Blt5G90kSj5G3CqC1Xi7v3v7q0LC0T83SYnpRRpQkVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نزدیکترین تصوير از ماشين حامل پيكر آقای شهید ایران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/668260" target="_blank">📅 07:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668259">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kxrYEJUfoRV0osf3UKkq5wD9lutrFsAwsLGNpkyOsngx-tibAsWFEYPMv5oTsovJikpHnkY5FFaja_-e9kNnjU36dUM6Rwwyr5o5_iH2sk37LPqtHqvtTExsg4GafRmPFayZhQ2sMw2bWX8EUdFoqnnN0wzvmHsJdKEA0CvIkQM6vez_OTx0DHDnkBgAb9OLHPyvyzslUqPkEJ4udzTsTzYZ1dESDP_i8wb6s4YRHKB98SeNw9wDzRdmOOXQvBvkm0rifwWfzRip7DKmKFXP5I5W-dwY8JNlLtmAxiJQvF-1DBwcBv7UET3auso7IrwSFLrLdcCkNXws_Apch0zyOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای سی‌ان‌ان: افسران ارتش آمریکا هشدارهای اطلاعاتی را پیش از حمله به میناب نادیده گرفتند
رسانه آمریکایی مدعی شد:
🔹
افسران ارشد ارتش ایالات متحده هشدارهای درج‌شده در پایگاه‌های داده حیاتی را مبنی بر سال‌ها به‌روزرسانی نشدن اطلاعات مربوط به اهداف نظامی در ایران را نادیده گرفته و حمله‌هایی را تایید کرده‌اند که یکی از آنها حمله جنایتکارانه به مدرسه شجره طیبه در شهر میناب بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/668259" target="_blank">📅 07:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668258">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nggxUlrGjgi8yV6KK9E_ZSyI7Gw_LvMAhY8CPxyE4KXgzKIRqFSmiRCeN27GuCWRi9Te71bGDXUleb_2ury3Bw2o3TuTyAYN1MY2k3kONcpvNN4_EWM1jvPIAfjPkVLJd6dXUyVcLaNi6oSAc_h6Wmu08OeEHvFvcDj56__fovnxPKaL1sNLGDB0l4LkDqxkvLweNf8wA0dLPFnNhWm-3XUdwnDnxhQexr-6ivRRGitacvQySPs_gfVITQTH5lQR-j-e23Ng16r3SCoimsXIGsP39mas1o-zlOP5MX1NS4a6rZQ_A6N2nPS7lM5j8XPvrxqs2Oj2oX7bXoBR5N8Mqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از خودروی حامل پیکر مطهر رهبر شهید انقلاب اسلامی در میان جمعیت مردم عزادار عراق در نجف اشرف
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/668258" target="_blank">📅 07:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668257">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47f4c3f506.mp4?token=EiofF6_9XSeL9EUXT2hwE6ocWU_sFKq2az7-9vNl9ZD4EBss5Q1BmxXWjxfWeIsoUdZvNAFtl6czaPaeKP1HdAHGZLUZlZM8kOGJcRqZRtlMWH7oENrVNr1CEFXwBaYmmOH5QQppqMx5qNRQoZkTFsOZ5FmHIWoY-cGiOXYMnlYmZQPWSv3jnB13PoOKvJvShhRRariZ5u36GBeaZMR9MTXO67NXDEfv0PIHx56S4-nO3bnImIBygeGovrCgAaYgM9bZjCUlF5KI-Z__doXTV2W4EbHL5Ng2PbCsEqKvfsBeWd1VGwLhPJWKEyKju59mrsno_ZamlDZgL2JXM43WTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47f4c3f506.mp4?token=EiofF6_9XSeL9EUXT2hwE6ocWU_sFKq2az7-9vNl9ZD4EBss5Q1BmxXWjxfWeIsoUdZvNAFtl6czaPaeKP1HdAHGZLUZlZM8kOGJcRqZRtlMWH7oENrVNr1CEFXwBaYmmOH5QQppqMx5qNRQoZkTFsOZ5FmHIWoY-cGiOXYMnlYmZQPWSv3jnB13PoOKvJvShhRRariZ5u36GBeaZMR9MTXO67NXDEfv0PIHx56S4-nO3bnImIBygeGovrCgAaYgM9bZjCUlF5KI-Z__doXTV2W4EbHL5Ng2PbCsEqKvfsBeWd1VGwLhPJWKEyKju59mrsno_ZamlDZgL2JXM43WTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شعار هیهات من الذلة عراقی‌ها هنگام تشییع پیکر رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/668257" target="_blank">📅 07:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668256">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
سنتکام مدعی پایان حملات به ایران شد  سنتکام:
🔹
ما دور دیگری از حملات تلافی‌جویانه علیه ایران را تکمیل کرده‌ایم.
🔹
ما بیش از ۶۰ قایق کوچک و بیش از ۸۰ سایت را با مهمات دقیق هدف قرار دادیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/668256" target="_blank">📅 07:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668255">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ff90c9a8d.mp4?token=gyZkL-ny-nDt0WCLDaUxzstyhDWrmHQMu9dt2QN-C1HaX0VTuDK7oL0o4SJm9i_qKywHvg5qWblDF4As7cWLXSoKts_jbrfLaQ5Wdj0kI1h5WGXGzM5YciQg4q8x0grJwR_UdsVG_iPhqs8SoeQsFiLvgjygM0T2Dpf7I_H65-b9pJRXSYu2h6nX_LXEXoFau4h34D_2ygwYg-k7ISxyamz4ziL0s0C9jyI9D488bo1eGWAxIpLewVwmsIY63FjuGbCDKfLJFI0U7LX14ys6WdGRCrsnlpOtF-8-qUA7VrCKM5JvDHPTJNzQo4e_8QFGrNBCw0RpCiy5fKrRRs1uiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ff90c9a8d.mp4?token=gyZkL-ny-nDt0WCLDaUxzstyhDWrmHQMu9dt2QN-C1HaX0VTuDK7oL0o4SJm9i_qKywHvg5qWblDF4As7cWLXSoKts_jbrfLaQ5Wdj0kI1h5WGXGzM5YciQg4q8x0grJwR_UdsVG_iPhqs8SoeQsFiLvgjygM0T2Dpf7I_H65-b9pJRXSYu2h6nX_LXEXoFau4h34D_2ygwYg-k7ISxyamz4ziL0s0C9jyI9D488bo1eGWAxIpLewVwmsIY63FjuGbCDKfLJFI0U7LX14ys6WdGRCrsnlpOtF-8-qUA7VrCKM5JvDHPTJNzQo4e_8QFGrNBCw0RpCiy5fKrRRs1uiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیکرهای مطهر شهدای خانوادۀ رهبر شهید انقلاب، در جوار ضریح امام حسین(ع)
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/668255" target="_blank">📅 07:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668254">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
پیکرهای شهدای خانواده رهبر ایران در حرم امام حسین(ع)
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/668254" target="_blank">📅 07:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668253">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJ-pevN0Md-KgxCiwNLa5uQGeETG2Ub3WmsMloKmoO_8MYhjuZZW0tSzCKsByMka8InxxoxwT96jaqlM9Y9feItQacqQjGZs8wYcC0tFxYTT5LRbTQ2jGAdG1Mqr4oIIj_-llvDLqImv_dFJESaOe1pjc4OFopaDWBBDZ06Vj-8Uo07eJkGXqPIhYQ8pR11wSaZTn62rKqtbGqz4nY81lNlhda-7Rr9L23TKPWwflxNUVZX-ZmhXgZLvuNd1J0tu1Qwzo3kABYvWXrxyxMCwCyl4z006_5GlK7PANplmnOdlfSWLFdoy-qEbMZaB11chkHAuxBuCWsL7hzhqtB5K8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
حضور شیخ ابراهیم زکزاکی رهبر شیعیان نیجریه در بین عزاداران رهبر شهید انقلاب در نجف اشرف
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/668253" target="_blank">📅 07:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668252">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
سپاه: حمله به ۸۵ هدف نظامی آمریکا در پاسخ به نقض آتش‌بس
سپاه:
🔹
در پی «نقض آتش‌بس» از سوی آمریکا، نیروهای دریایی و هوافضای سپاه در عملیاتی مشترک، ۸۵ هدف نظامی آمریکا در بندر سلمان، بحرین و کویت را هدف قرار دادند.
🔹
همچنین یک پهپاد MQ-9 آمریکا نیز سرنگون کرده‌ایم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/668252" target="_blank">📅 07:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668251">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d10a07000e.mp4?token=gHzB6RcWgY083baCtOzV7iETKEIthXG9_-rqyY1_9ev4QG4PaqyDDsidJhHiTth50vQ0qoqLpV0zq1YwI7EbobI-7nm8lF1fG98VgabFNJRboENLJxfOgem40TTU7l6WZF_3m5t8JbhtGhqTlBtOUFpCdymvUEXCgYaH7F5lP0Y4zqPzBcyDF8QywrelNGlVBX-2DB_8rFh_zSIP4vnYrktki8QzzMFoGQthC4TQ82E-yRldbXjfuMn4iZw42_RaDSNUAFE2FJq9mpYPagSgLavbuU9A2Fkml7EN4hzDS5R7ICEWx9xWJ7DPTPqSCE_HW-KFJ1v4MdO18rEK9kwQMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d10a07000e.mp4?token=gHzB6RcWgY083baCtOzV7iETKEIthXG9_-rqyY1_9ev4QG4PaqyDDsidJhHiTth50vQ0qoqLpV0zq1YwI7EbobI-7nm8lF1fG98VgabFNJRboENLJxfOgem40TTU7l6WZF_3m5t8JbhtGhqTlBtOUFpCdymvUEXCgYaH7F5lP0Y4zqPzBcyDF8QywrelNGlVBX-2DB_8rFh_zSIP4vnYrktki8QzzMFoGQthC4TQ82E-yRldbXjfuMn4iZw42_RaDSNUAFE2FJq9mpYPagSgLavbuU9A2Fkml7EN4hzDS5R7ICEWx9xWJ7DPTPqSCE_HW-KFJ1v4MdO18rEK9kwQMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عکس نوه خردسال آقای شهید ایران در دست دختران عراقی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/668251" target="_blank">📅 07:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668250">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16ed0bdd1e.mp4?token=ocLQ-T7alBoDJwsAUO-xShp0BaWfqc2_w9lNes2R80LstWI2zzlmBpXsAiPsup6uhciZ7zLeP20TvRVZRu9HLY-jM4yKjn7fSTzdFiDFb5KbeWQsgKkYWWNFftm1r7IgWO8rc3zvDsWgWgYijlsVevZfJ1yWr5VttMB61XODwJSIVX5yMmPyVydVrDwy4O95tMDz6avT9CVQUSc9PvDPjNzelj00gNsabQEnSvr5YLtM4C3wutVIKJ1OA56DtDwGGDC0qHwBUZ22Y69oZAz2DWC6EbthXkc8vyF7Gz7vaNSSruh2giCTtUJgAGqEhgin_6ECh66QudleSRERx94Xjp_5qJy7r15PBKh0soPCk_SnmjxaAeqyPnGQrJPoT30XzG58KVEz7XrUtJwjDAqe4T3orBSoWMC4aSRdZF6zAwIpwsosmP1BMydCZb0aLD92TrnkHrR8vd0QfCdOuJSOHyJ6NcvRP_BysTleaUqwcEIFrDD8IIC9wLTABk2WI4LVXCnjddb5YKuB1H-2x7VNNzA4ZcpTzv8Ngwd0Rx3h-_EgFd-vEYR6DXtYdl2LICV3GeHfSQn29BK2hljQFbIsaGqE4iYJnAzS1cm5ivnYArV3SX7WUMeGT3ANYg1vDAhivOR3x6FG_P2357xlH9nZF5ihO6NzdwEl2QjATMK6NXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16ed0bdd1e.mp4?token=ocLQ-T7alBoDJwsAUO-xShp0BaWfqc2_w9lNes2R80LstWI2zzlmBpXsAiPsup6uhciZ7zLeP20TvRVZRu9HLY-jM4yKjn7fSTzdFiDFb5KbeWQsgKkYWWNFftm1r7IgWO8rc3zvDsWgWgYijlsVevZfJ1yWr5VttMB61XODwJSIVX5yMmPyVydVrDwy4O95tMDz6avT9CVQUSc9PvDPjNzelj00gNsabQEnSvr5YLtM4C3wutVIKJ1OA56DtDwGGDC0qHwBUZ22Y69oZAz2DWC6EbthXkc8vyF7Gz7vaNSSruh2giCTtUJgAGqEhgin_6ECh66QudleSRERx94Xjp_5qJy7r15PBKh0soPCk_SnmjxaAeqyPnGQrJPoT30XzG58KVEz7XrUtJwjDAqe4T3orBSoWMC4aSRdZF6zAwIpwsosmP1BMydCZb0aLD92TrnkHrR8vd0QfCdOuJSOHyJ6NcvRP_BysTleaUqwcEIFrDD8IIC9wLTABk2WI4LVXCnjddb5YKuB1H-2x7VNNzA4ZcpTzv8Ngwd0Rx3h-_EgFd-vEYR6DXtYdl2LICV3GeHfSQn29BK2hljQFbIsaGqE4iYJnAzS1cm5ivnYArV3SX7WUMeGT3ANYg1vDAhivOR3x6FG_P2357xlH9nZF5ihO6NzdwEl2QjATMK6NXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌اکنون؛ پیکر مطهر رهبر شهید انقلاب اسلامی در جمع خیل عظیم عزاداران عراقی در مسیر تشییع نجف اشرف.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/668250" target="_blank">📅 07:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668249">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ipropej7eW7pX8vkDwDhNPksbusK6doCQhQD02ajWtHaqCnfKwnQiIzVzLNmr4BFPV4m0uTJkiiSwW0LO9ky5uMOZFwS7Qk4lN-rXR5vDNE2vixw1W6kxuDwybgeNEVeNMESTuRKA7t80fKRylBPH1q7Z607VrLYILWrFNVOMomdbAYCD7B5vxHoEYbM7V43A_U6GxVzfSfxD-onLZr4WYOX3nvc7SsqK7gN2o4A-S5VfnhGoEUL2BIdQ2raTa7t7jNPTXf5Tp3Gx2Qe_Q8rpzQtftmGxCIr4OVvViO8a5ggx0m3N3H-R1iWNEUWizx8j3farmyclb5S0nt5E04ENA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز چهارشنبه
۱۷ تیر ماه
۲۳ محرم ۱۴۴۸
۸ جولای ۲۰۲۶
چهارشنبه‌ها
#زیارت_نامه_ائمه_اطهار
بخوانیم
⬅️
متن و صوت زیارت‌نامه ائمه اطهار
@AkhbareFori</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/668249" target="_blank">📅 07:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668247">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d75a445d83.mp4?token=HJkCsDP-WYuRaZVynbI-6YxcYYE_Ndcn2XIvn-sjFUBskPgUsgt6yOgV-TjVUMxXn0ATSCPs73jCrXKalpTM0kGlEO1iZbzP_w7BVKbhLUkyPpUTJnIMC8YNnx5ei26fLpcsy_uDArjwd9dImxhTCZfTBL-AcYUS_Q_Y58Hmg6IXRkgI_gO7i_ZoNrDSSXiV1px8vT92vJU0Cxm5S7PeeFLA3xf6M1EqimybFVhjZuEYZCOV6cm3mnJ4p9-LYNaLDfANBG-BxDLxNUl4BfUHSej2gybmRhIhC1NgRnguRzROC_alSC9-s_JY_7iJlquumCrl8vQDetv_STWmrDdB0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d75a445d83.mp4?token=HJkCsDP-WYuRaZVynbI-6YxcYYE_Ndcn2XIvn-sjFUBskPgUsgt6yOgV-TjVUMxXn0ATSCPs73jCrXKalpTM0kGlEO1iZbzP_w7BVKbhLUkyPpUTJnIMC8YNnx5ei26fLpcsy_uDArjwd9dImxhTCZfTBL-AcYUS_Q_Y58Hmg6IXRkgI_gO7i_ZoNrDSSXiV1px8vT92vJU0Cxm5S7PeeFLA3xf6M1EqimybFVhjZuEYZCOV6cm3mnJ4p9-LYNaLDfANBG-BxDLxNUl4BfUHSej2gybmRhIhC1NgRnguRzROC_alSC9-s_JY_7iJlquumCrl8vQDetv_STWmrDdB0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
السلام علی قائد المقاومه الاسلامیه
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/668247" target="_blank">📅 06:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668245">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/USkJH4LYCafjxivXgzhd8PUjxfOYGgrYLa2Q62a9Nj0E2iCT1Bkw5AN7lSbsSPilSV5E2Wbx7XB9vlipI7R444L9pxiXlHWzR1FsQcUz4OM5hPgd2vEBUKuw7xNItq_DISNjXEGvZaeehR0-aL1drn9ZKyjpseN8bG03echTMo9xLxhAZa-KgnqxVI32AnlvJI5VEMlNid6GMqI4c7BecM3WvbFYiGn04NZpsNf5xtLGMyVchvO1wNl9dupHk6-1eebKxx4ZrxIBC3z9PW4B5WmKrD5u58UY-vMI5MyLwpmZptBzPboAu_xHtN1_MB_Tx4A4Vnykftspu6obP7T32g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xxcm5dtLzQLSfwhDWX2K2ESmjC6rQTPcdKlw77MJ6tlb3-GF5iYx9C9qPOq-QxZLFXNplKURLufan07xuu-lz7ngtuiyilX3KyShFEMl3s_SGApfPsWDqui0f9n0RNZW8yPgxw_p53tovB-0a2b8ff2tqxzb9A_ME_-YFZC6IyUvSra8bfnXMw6vrYaqNRUgyclsEtPl5XTHYzun-R9i_zce7DHy1jG2zihP4PG8q3RdjrU3piuprEJ3rreQgZtJ92TKXWR7Af_iPxMHu2ToOCW781TKit-TGwnKNC9WK4n_K6ZehhuM7_yvOjjK6VcGyuJYMHzptxSNauj9aSNcbg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری از پیکرهای خانواده رهبر شهید امت در حرم امیرالمؤمنین(ع)
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/668245" target="_blank">📅 06:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668244">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2c3a8b7ce.mp4?token=RCES7q2PidPHGP-5hmJSP16GtvL3yVx7nJ5UrOC1ZqMXX2RRGHmod3nWM0lby-vMPxygVgDjmPWmJUW6plbhEyJ15PPkd7aftjR6-xHrUTZOS4pCmtjFvpdsnigX-OPmCX5SFW4xbSEqn04LHzc8-9TjTuaZCe4YF6Fhiv3lcoANXBidv2ey9c7FDeweUs-YQjkPEelz5sBcwqsElgalT5dBzMAf4CE8Ht1V2DAfmwvICi278ORPdFRoShkT8QlSi-QumD6FGid5cKrDZUkBqzEx9-y8niW4zuF6gsqdRA9OtWnEgvMV8pbphm7_ZVMHYZzsNpho8CzBAkpSieDtNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2c3a8b7ce.mp4?token=RCES7q2PidPHGP-5hmJSP16GtvL3yVx7nJ5UrOC1ZqMXX2RRGHmod3nWM0lby-vMPxygVgDjmPWmJUW6plbhEyJ15PPkd7aftjR6-xHrUTZOS4pCmtjFvpdsnigX-OPmCX5SFW4xbSEqn04LHzc8-9TjTuaZCe4YF6Fhiv3lcoANXBidv2ey9c7FDeweUs-YQjkPEelz5sBcwqsElgalT5dBzMAf4CE8Ht1V2DAfmwvICi278ORPdFRoShkT8QlSi-QumD6FGid5cKrDZUkBqzEx9-y8niW4zuF6gsqdRA9OtWnEgvMV8pbphm7_ZVMHYZzsNpho8CzBAkpSieDtNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور حماسی و پرشور مردم در مراسم تشییع رهبر شهید ایران در نجف
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/668244" target="_blank">📅 06:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668243">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0085a62f98.mp4?token=hExML-oA1BxOj3oGb-U8yY2ljSa400VVZWCfzuXkRmH7cLPdKBrbmFYGX20_86n-ri7B6j29WDWMIykzsdfDThMbxrUdUi2Rxc6ezvGiUUg-4JCHVgXpxLh4JipRYPXqx2JZjt8IiWPvXC1FeQu06GKJvoXx6cYs_bvDnRzRQ5O-IMXfHs8tH_wgnnZHgRDtNJjoFw1klQRiwBB0wiNnN1SQwFE4oYyjMhjJZgRygY-OGYyVnKg_SldaLekuPKq0HvReSewhcKu8Rj6qEPx0M3tdnBOq53uyuW0zd0I46y3MX0QuJKOQreGk1LvHdFKkK4wonPr9hB33zmHOk6A2wx5PZyJnkY32MWxuDCcnqJeWYDILRemxjJIagMX8bldq6akYVgBTV80eKCmPn57vlOWUxls-e2nGnBWyXHdLDSv63m9rjfblkNPbFbF9NqogGS5J99HiDuLPPPkRdp75zz5D1-lYFWc7d0PpYFDST84AW3hFJfaD0P-CPXk-UA7NUZm3c42UrZGWir84KY0VKQaQA-SdStk3kyJrLfxvIrBRSf2zdrE2zgQtfoigDk_-NOFc-dcM36y_k0tFFUb468JTC5cL-i3ty77KQcm7kDxXAKcFZmPDql5dkGnqW-o7RoPjvbOGlgyS3yhEw0eqUVZRGEQdpcO3x_a9wK3NV5s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0085a62f98.mp4?token=hExML-oA1BxOj3oGb-U8yY2ljSa400VVZWCfzuXkRmH7cLPdKBrbmFYGX20_86n-ri7B6j29WDWMIykzsdfDThMbxrUdUi2Rxc6ezvGiUUg-4JCHVgXpxLh4JipRYPXqx2JZjt8IiWPvXC1FeQu06GKJvoXx6cYs_bvDnRzRQ5O-IMXfHs8tH_wgnnZHgRDtNJjoFw1klQRiwBB0wiNnN1SQwFE4oYyjMhjJZgRygY-OGYyVnKg_SldaLekuPKq0HvReSewhcKu8Rj6qEPx0M3tdnBOq53uyuW0zd0I46y3MX0QuJKOQreGk1LvHdFKkK4wonPr9hB33zmHOk6A2wx5PZyJnkY32MWxuDCcnqJeWYDILRemxjJIagMX8bldq6akYVgBTV80eKCmPn57vlOWUxls-e2nGnBWyXHdLDSv63m9rjfblkNPbFbF9NqogGS5J99HiDuLPPPkRdp75zz5D1-lYFWc7d0PpYFDST84AW3hFJfaD0P-CPXk-UA7NUZm3c42UrZGWir84KY0VKQaQA-SdStk3kyJrLfxvIrBRSf2zdrE2zgQtfoigDk_-NOFc-dcM36y_k0tFFUb468JTC5cL-i3ty77KQcm7kDxXAKcFZmPDql5dkGnqW-o7RoPjvbOGlgyS3yhEw0eqUVZRGEQdpcO3x_a9wK3NV5s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سحرگاه امروز؛ لحظه ورود پیکرهای مطهر شهدای خانواده رهبر شهید انقلاب به مضجع مطهر امیرالمومنین علیه‌السلام در میان شعار «لبیک یا علی علیه‌السلام» عزاداران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/668243" target="_blank">📅 06:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668242">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
منابع عربی: انفجارهای شدیدی پایگاه هوایی السالم در کشور کویت را لرزاند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/668242" target="_blank">📅 06:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668241">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
خبرگزاری کویت از فعال شدن آژير خطر در این کشور خبر داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/668241" target="_blank">📅 06:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668239">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
خبرگزاری کویت از فعال شدن آژير خطر در این کشور خبر داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/668239" target="_blank">📅 06:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668238">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
سردار محبی: یک فروند پهپاد MQ9 در آسمان خورموج ساقط شد
سخنگوی سپاه پاسداران انقلاب اسلامی:
🔹
در پی تجاوز هوایی ارتش تروریستی آمریکا در سحرگاه امروز، یک فروند پهپاد MQ9 توسط آتش سامانه پدافند هوایی سپاه پاسداران انقلاب اسلامی در آسمان خورموج استان بوشهر، مورد اصابت قرار گرفته و ساقط شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/668238" target="_blank">📅 06:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668237">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/36ad33cf7a.mp4?token=enXs3L-gTagLdQSHbFywsnmsPlEUCSSA8rPMYQhiNIJXaaK4Xw9sMvAK7w3VDsl2UZ5UWJs45Z1h0uIRD8kWHgK2anNz970Uq2t96_-BNCh4401xBe_HXIV_pxM61rNYHXsBQytTHjYDWitF22eH0g80b8oyhFgbqNqLtBeiWqhvHtEvbJyyNN7gyxDWVJp2TcOeZ-seB5LDu7xCJLL-pboN5OcSXepPezGXKXVEkci7YFf1QTwDpv60weWDLna8JamjBAxNObvzVm9l31Wa3XZX86QWdLibjEw5iH5qfPYBlk4J36MAG4Z9TCsHt3GOD_giEyvlj8AeYUqar5R7rA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/36ad33cf7a.mp4?token=enXs3L-gTagLdQSHbFywsnmsPlEUCSSA8rPMYQhiNIJXaaK4Xw9sMvAK7w3VDsl2UZ5UWJs45Z1h0uIRD8kWHgK2anNz970Uq2t96_-BNCh4401xBe_HXIV_pxM61rNYHXsBQytTHjYDWitF22eH0g80b8oyhFgbqNqLtBeiWqhvHtEvbJyyNN7gyxDWVJp2TcOeZ-seB5LDu7xCJLL-pboN5OcSXepPezGXKXVEkci7YFf1QTwDpv60weWDLna8JamjBAxNObvzVm9l31Wa3XZX86QWdLibjEw5iH5qfPYBlk4J36MAG4Z9TCsHt3GOD_giEyvlj8AeYUqar5R7rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیل خروشان جمعیت در مسیر تشییع/ عبور میلیونی سوگواران از پل کوفه
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/668237" target="_blank">📅 06:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668236">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
ادعای وال استریت ژورنال درباره تمایل آمریکا به ادامه مذاکرات با ایران به رغم نقض آتش‌بس
🔹
ساعاتی پس از حملات متجاوزانه نظامی جدید آمریکا علیه مواضعی در خاک ایران، روزنامه آمریکایی مدعی شد منابعی در واشنگتن از تمایل این کشور برای ادامه مذاکرات با تهران به منظور دستیابی به توافق نهایی خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/668236" target="_blank">📅 06:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668228">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pJCPdOLa7qrOmgt3ISHeVvtPN4x5uYIx5ydWbZyO-ZPc0mXEccJsXnZ9o8XuJzWU9tvfSjnXWYdCDVjuVyikWHV2o3MtOdbpX7ktbbbXIUpkwV6gLEkfOjm4BlLDM8cCPamJirLpDxs3yUCW_kNHvUykxWQRbauXZlqub6yOgOJUCPD_tP0O7fcdH3_QjbC8oi7lekWKWfqK9-W1mu_nRze9Ctgqy7wf1DH7igqm4AQ3s8hREuQIrTMfpfOiLHihqNUqDt73K6ldovBgha2GK1tv5HcsRMmyT2eHYNJ-rMGSK8G24gx5AWGmkNUbFI92PO2kydjl3XNIay5wCKZZ2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O57kxoggj17CoqqQb-Tvlx_9DZHwNS4HfHCrUbHPkNyhSDcnzUCCwVGqyKt686wur0tUPvn91GTLQX4E7uVU6yPtfkWFQw3hOxxIhritrEj3dwwmZ4RPu8O4IDoPXlJNAAl6J4TvZwHRQbmhEajyw43Lr81mBRyzwEoczNMg61LCV6o6JNSoSltZy-Q74J_PWnJSlCrLJ9EL5GL7aYOlfwZ68Xt-TLmTs0AWx72r-eo6uZi6bvZ5CAKugZJgo3rIUdtCz0NHiTVu0p8I_asC6WmeyzkfbXo93xBX9zR9Bk4zOyNBy37Lc2ZJO7mYKtKIVxJbNT5d1kuDP27YnXnnoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H-hB_Iy_cl_Z8eTXZXzpUMocTopCmbcUJns19kcSdl0iTwMWSnhEqNnpC0jMAD3vFogA9bjER2uvAYizXiSWL_FaXrXXQu3MA6g7xhfmmNMWObnihj7_liNXh723uJ40AzdMpWew3HqLKBOr0HgFw0Ubt7MY1tDSn-4506hD1LjggrMf1Nq_Y_M3wyslZtjAnkpSQ-5RaBZ-ye4sRjsaVSVViqoSOt8hP7f7Cm4j9CHgBVAm9vcveu2Ydsgkt449Oy9wKd-WNubNNtehqgpy9PgRiFZ_SnYU5Wrh3lsp8OfrsfkUVV9lvuR7OP1SgL2wRLeThOmVs7wMjWCSpXDgaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sdBUiyzyslwzwtjMh1Tpx8VKa-qstbf9ESfp33H-CnmW55moIrGQ-wS_b0HMhoek1H5MLdgBXiKsYWmM5TzBFZNAzAYDoS1DiD9gtVqtuFA4EhDFT7_rExuMURvE2fFW4PT4z8QfOvGnY5u1WE1CeADdnkPJAvb09tDbT5bq8d2NGEt0k----JBYSdDRBhMxMNx3f3E5LMYczbNrmLg2HnSnB-dM_ywG7ja0pZJmK_EyitTK5aRHZ8Y1n2CsGEVFxa2G8f12LytElAeNDq-22OoOcV5JyIywD2ForoLO522kFuKMh1uL2M-Hcp-WzrMwTFh5unqDqtohIzOWEp2I9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QObkLqJ5t2DYdQvGXA2Mrns2_C0RgrIHJ8h5tIttla_3G0Z67qqGnXY6prqBzissY0lzloYudXBVaeZXEMrmd8rNL7FPRkHfBjMB_rtISdYpKFGUGUhuX89UEtLE2BRpEiDi0vLl_1weC-CLwTnMsu1QpThaeQib3NvUCgsNwsF0xzRafEvzIFwwkmBGAxVDIFGac9lCoIZcVYBe21A1DKESiZtcTgwD9NlCDzRbM0BPjW6Sfic1ruqDoV9Gq0KXZMzRTZ1cE7aYgTkRiHluEUYEUyTCAlpMUgsECLe5InrzhybAuHCtxkmhstHu_HITT5xTe5FOznklblviUJt_7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/blzkrYXdwMEYvyUehMOEZ-MOWz_AbmhfKLVTuNcmR_Wh4ofAtwY8Jdh1fSOIlveLxkn1rr2dp6y8JYHoRJWyUZ68hjgYlRj3F-nOefY3JRmCx1VrYuvL8WVKnAt1RjMocL5Nojmj6rI9wBUspgU24sVS7KfQ9qVIzrtDyYzd_DWyb-kDNBjAliQFvI70YfcSSm_90VbK9M38l1ymPKNlnyXuYuWO9E6AFk0Q4ny2O2nl6_HKsCW7dggtpe3eijw-2VttZKMw3AkK70nAeY-850aGQz1GauPge4UnYz7o-BV3TYN-Ce53RU1d8uqRKeT99scDdXlL1JtHuRCIr5cZIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JiNIsHKfhDUNF98DwZluP_043z6W3HOewJIVXc2-rDemtiFuNbaWLZTELSJrHcSxQaCdqURg-z5LYmL4dMeAp_Ph7xnW-xVzggzhqW6dEqC3BwtqaISbXb8X3pdhOXi5qfLulCZbhK_oxjLerNPBRXgwOmvAG5a079L-f6cg1G-qKAVx8FWQZ8q6chuE_8Dzc-7WcdohWwtAad50Q9823quSpLfrda6cd2mKeXFIe0NCweXloF5cIH0i0wPig-Yp7sp74mKnfCwB3m2nrC9B5qcvAM2ffPI40ARQdFdUnE9EIiuoJorZwAaFx60ej6B8CfZupWp1Cw_6v56_2N6qzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DiHHXPapwq1JMJpvWewmvreG8xioBiQeB60Zko6GyNCx2q_lCOQUpddLEZpgqIMvTPzvEhZSjM5oVabK2sXQNrOa0RgDLzb-664dcEcEr0qoIrnfh-LtmGM0gdXjjIziffMEiHtv4QTMuylmCFroS_YptVrPD0yLk830KU8TE_Qhmso4igMyoz8nTK_U55AFJvfdARc4F8x9jCxgPzw5TsnTvTVqvPJ8-bUnDCMfNTtpj1LoTO9qV77fNhNDAWzex82Cke-Jp8vlhlSQkGxVVj71HwKDQaTQBydRir4A1ytBHm4hlXTWnXnNi7wANnbyEsHW3731vup4wGMeNDFJoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
غوغای عراقی‌ها، دقایقی پیش از آغاز مراسم تشییع پیکر رهبر شهید انقلاب در نجف
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/668228" target="_blank">📅 06:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668227">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
صدای آژیر در بحرین دوباره فعال شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/668227" target="_blank">📅 06:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668226">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58742557ec.mp4?token=vJjLhDLIPW1l9o7M56m-O5fbLYNfyyaahElaAPcAf_NYUqV_1eSDM9L_lZfPIrconPYAjAFnY5FwFlAVzR5B5r70rzK6kug6YuziviWPkH7Je47q8ngefw4GlXwE7hegcautOpsYIIjVGOM9jwfXe1KcyqTY3guyIjlBscwhy7HkKG669nTpb5YtzNVBIxOuzAHsgMJCtds45ZChmdd8ZqXht5xXsHvNB1RQdKKDOhidL8iwUOFhxOcHx7a8CAIS9wzbuMcLycE4fQdDEv-Os0aJ4EulmrGhL5PVWguWoVbOqLvW6INJHAQ3Bj4keYrEbGa9-2NRHh133LamrG9Wmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58742557ec.mp4?token=vJjLhDLIPW1l9o7M56m-O5fbLYNfyyaahElaAPcAf_NYUqV_1eSDM9L_lZfPIrconPYAjAFnY5FwFlAVzR5B5r70rzK6kug6YuziviWPkH7Je47q8ngefw4GlXwE7hegcautOpsYIIjVGOM9jwfXe1KcyqTY3guyIjlBscwhy7HkKG669nTpb5YtzNVBIxOuzAHsgMJCtds45ZChmdd8ZqXht5xXsHvNB1RQdKKDOhidL8iwUOFhxOcHx7a8CAIS9wzbuMcLycE4fQdDEv-Os0aJ4EulmrGhL5PVWguWoVbOqLvW6INJHAQ3Bj4keYrEbGa9-2NRHh133LamrG9Wmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خودروی تشییع پیکر رهبر شهید انقلاب و خانوادۀ شهیدشان در شهر نجف عراق
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/668226" target="_blank">📅 06:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668225">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68ddcf397b.mp4?token=QFDUgzV2Lm_gEfvaYB_wDMq1RT5V3WgyEZjjVoVIhGzUm2GweWlJm8WJAUtd4w8AIkF90Ofz7EQhH7Jyd86Y7u07hzkHlVD-SN-FgryUr7U_IHsWjHiq3N_wbSs6s0So5j7yB_x5NYtbdLFajYO-KiQeSvAismhsTEbQkc1Ylr8lGfSwZpaloM5t1pBwjvpzTLefsEXubFPvgNVUNDdgsOc_wUxVue3BZWiirpmkVhMPWXm2Ek2j_WcTf6VWhfw6Iy2TH4lmpDniAFSllL1vjUt_Af_KAch_pIK1LmKy6p66MCCtcd7Tz2n-qM4wVepdjQwjF3X0cAPVoceRBctm9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68ddcf397b.mp4?token=QFDUgzV2Lm_gEfvaYB_wDMq1RT5V3WgyEZjjVoVIhGzUm2GweWlJm8WJAUtd4w8AIkF90Ofz7EQhH7Jyd86Y7u07hzkHlVD-SN-FgryUr7U_IHsWjHiq3N_wbSs6s0So5j7yB_x5NYtbdLFajYO-KiQeSvAismhsTEbQkc1Ylr8lGfSwZpaloM5t1pBwjvpzTLefsEXubFPvgNVUNDdgsOc_wUxVue3BZWiirpmkVhMPWXm2Ek2j_WcTf6VWhfw6Iy2TH4lmpDniAFSllL1vjUt_Af_KAch_pIK1LmKy6p66MCCtcd7Tz2n-qM4wVepdjQwjF3X0cAPVoceRBctm9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادای احترام نخست‌وزیر عراق و رئیس‌جمهور ایران به پیکر مطهر رهبر شهید انقلاب اسلامی در فرودگاه نجف اشرف
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/668225" target="_blank">📅 06:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668223">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
صدای آژیر در بحرین دوباره فعال شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/668223" target="_blank">📅 06:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668222">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mp2s1B2GcRnYiyWsm-68brtFz7emZbDu6g1fS0b2nhWSryR8HHw9-NbN0Qs46kVAiUnrDaqVFb26Gm3iia1XbQXdxfItZT7NrFY0C3E7mFImgnkm78BrEuj4BLvSq6QR0HcXE4-49sRos001jkwfQp2MvyoGYRI_zyOrfZ5j7rHshIQWqOOyQSAXw2W2AuYrEiyrERtGe-A9Qu79NTbCDKdPLHxs8X7Zs_Fe4gSfkzFjYhcckF4PW4beI2VermXdeX7K9hAB_Y5Nh4mqRbX8mnG8jfJtu2N4d7FEISTOGNoXu7By92v3R7niwA5OclITL7j2Px4dfveCzyDjqn-teA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف با برشمردن موارد نقض تفاهم‌نامه توسط آمریکا نوشت: دوره قلدری و باج‌گیری تمام شده است، راه به جایی نمی‌برید | ما اهل کوتاه آمدن و عقب کشیدن نیستیم
رئیس مجلس:
🔹
کلیدی‌ترین موارد نقض تفاهم‌نامهٔ ۱۴ بندی توسط آمریکا:
۱ - نقض ترتیبات ایرانی در تنگهٔ هرمز
۲- تهدیدهای مداوم به حملات نظامی بیشتر
۳- حمله به مناطق جنوبی ایران
۴- بازگرداندن تحریم‌های نفتی
۵- استمرار تجاوزات رژیم صهیونیستی به لبنان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/668222" target="_blank">📅 05:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668220">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf867b1801.mp4?token=Ml3lUDaeOONkpmPRWrSSKXk3A4sATqD9DRvXxVT7YRa2Wj6See8MXM84HOc6wq_0taWOfB_Vz-Bupub229BGqCmfyp6JOCMjLfeptSVuraPQmrjKF2CZfWj2K3ztZxFrCOFLb07U3sQKgFZk2czrfgD6p_cwNr-u9MskWwrKr2EA5btga0wIUCSoWSYWkyOiyytFaY72x7mD-0E0whjEYd9VfuVrRwZAcsURSnPcMnmzJzUKDzjvaRPnyj_OenEHxRiVdjTAhFmnJeNUn0e6-aRmudSCzKvaV7cLiTQjkTskaPQtXa7UqGZsstTUsH1uqbubSQWZm9lexdMvCMfVhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf867b1801.mp4?token=Ml3lUDaeOONkpmPRWrSSKXk3A4sATqD9DRvXxVT7YRa2Wj6See8MXM84HOc6wq_0taWOfB_Vz-Bupub229BGqCmfyp6JOCMjLfeptSVuraPQmrjKF2CZfWj2K3ztZxFrCOFLb07U3sQKgFZk2czrfgD6p_cwNr-u9MskWwrKr2EA5btga0wIUCSoWSYWkyOiyytFaY72x7mD-0E0whjEYd9VfuVrRwZAcsURSnPcMnmzJzUKDzjvaRPnyj_OenEHxRiVdjTAhFmnJeNUn0e6-aRmudSCzKvaV7cLiTQjkTskaPQtXa7UqGZsstTUsH1uqbubSQWZm9lexdMvCMfVhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خیل عظیم مردم عراق، دقایقی پیش از آغاز مراسم تشییع پیکر رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/668220" target="_blank">📅 05:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668219">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
شرکت شهر فرودگاهی امام خمینی: عملیات پروازی شهر فرودگاهی امام خمینی از ساعت ۰۵:۰۰ صبح روز چهارشنبه(۱۷ تیرماه ۱۴۰۵) به روال عادی بازگشته و همه پروازها طبق زمان‌بندی تعیین‌شده انجام خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/668219" target="_blank">📅 05:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668218">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93dd221766.mp4?token=Awgldq1IeM34JT1utbGM2WD0VEb_8V62ZlMhQgLWGV7AJ2udiZkdmJ7ynxxacZyo4tYRWSpPLI33l2fY1F3g1lFoxZD2eFdN84wC-uMqswe7jnOpI9gN3R7Agkdry3SEhVNusXYvhUprrhnNNaskM6wr-cKd1fL04p_TT_CY1oqlr_Ep2sLB_1WH1-aCcFljEdq5PpSDrp2pwq9QoDPDPgruLAQyeRJ_2WnmrdmzmN0b7LVDUYYmlMehjDDZtx_nm4qUrIr7m0R9Xagpl4WOt1ju2MSCLoG4JY_t4ITtwcmypo631kAKNqygLNk5WKzAmwmhDTI0fTZH_q34z79Y14i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93dd221766.mp4?token=Awgldq1IeM34JT1utbGM2WD0VEb_8V62ZlMhQgLWGV7AJ2udiZkdmJ7ynxxacZyo4tYRWSpPLI33l2fY1F3g1lFoxZD2eFdN84wC-uMqswe7jnOpI9gN3R7Agkdry3SEhVNusXYvhUprrhnNNaskM6wr-cKd1fL04p_TT_CY1oqlr_Ep2sLB_1WH1-aCcFljEdq5PpSDrp2pwq9QoDPDPgruLAQyeRJ_2WnmrdmzmN0b7LVDUYYmlMehjDDZtx_nm4qUrIr7m0R9Xagpl4WOt1ju2MSCLoG4JY_t4ITtwcmypo631kAKNqygLNk5WKzAmwmhDTI0fTZH_q34z79Y14i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زائر خوزستانی که از مراسم تشییع تهران جا ماند و خود را برای تشییع به نجف رساند
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/668218" target="_blank">📅 05:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668217">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q0HGiKGvlRkNMI1XyEenVkvVVeif9uxxjQaLCDcnAEw1UmTJQ5bpNKWpR-SJB2Q76XkR5_GhbWVqwjy52cn0xoFRpxe1OMu363rJbORS2tjOzaWMW2jrMxAPhvBAJEuz9sJrjn4btcDaTonCt2OcA8tY-bbq-7dZv0S8X9t25Iwu6KkBAvraJwcIeEtk5x6Cq3xLba1vjntvu4gxHQcRu5dZx5IoNB6cKySeDQNAWTYsEHhpZ2u7I-euFtpE92EPq6gLjDaoev7jRsX9NJ_E4RbKY-SFRgipe2tAN8yZEg9w6qLWj38XSdiuieONL81KhlleTuDlyGDnhR-Shns57g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
خیل عظیم مردم عراق، ساعتی پیش از آغاز مراسم تشییع پیکر رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/668217" target="_blank">📅 05:40 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
