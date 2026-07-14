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
<img src="https://cdn4.telesco.pe/file/YN5dSGrgn0AFOgOhTqYhjotqu1Shrj9vDoyrF1FbTrIcMiygQk4FA9R-Gz5_oxmnXD_QJjvuKK9q3NjqcLTKw836_PETiz7awpsvsYv2jRjPBezkZFiuKcKcvycZzJt43y2wvwKSdm4V8tV84-PUpuu5FS9RwtNAMVYAppBd6Nsb6mUWXtXMT2c6ihzS4AAOlOYkB1pWW94gYOFhjz1y4yqpHsX7e6QNdEr6lmRfWkd8vZFZzq297_lxVkkwsy5rVpyarQ7gTTXHATa2KJ-7qebidp5hpYBLYfK6SdR7TlsEkJH9OwFlIDOieE1oLQdOffQ-qrH8a1mI5OlhhEYs3w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.4M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-23 22:34:32</div>
<hr>

<div class="tg-post" id="msg-671125">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CE53vqD120IH3ddzYitQnebNK3Rh0yFbi6iwSuhWjX5B4w7DNVB1XhcuYoPF0iMb2V47MsoC-tbKBNWEFNVsACYNr1_O3suOcwUfbfIqhy5jXfd88LrPKqNlbMlxz9xdylYuLZHMdbBIdEPDzGHDI2jUQhfnCJmQlQktXbgJtEB_HM2iBCD5w0FO6FBoiU_c3_VVFuUWcT4Q634HhB9WKy8-PWlIKdGFKFt9muoN29F5yVd6kiuZrZ0lRudb__9Ni-IFVZTpVopCkR2SUTxQYOnnQB9RBgM9t38wzqGToc1SuXaRPwAOZyC2BLmYj0QzVrYqxsNQLakTeBWETYfAsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AU6g29IFqToaEAv2AOWdC48H40G0FIe4VZBwypt-0behS-ZSFD4mgIBJUHH2UkyqgotV5G0hp9oa3XVGTUpVSZ_5SfBmwVivWKMUF8JGkbgr_9lyGxJC0HOvgZd7kb6EqsbWFpi8B3-k4L77968zBsWMVnq0OFTnz3DtR83beTd0d_fSqmYd23u-4gm5HrwyPwWESZvUDWmh-zDKaIEHq2x1peabRAVmyhh_20TCA3MpADNw6AsUZCrbu-I4gvwAtaXD-0czF5DU_3rJNSJXO2cn_zmF7QuFtE6Nfq1CEJwZWxsFWeXIas7r_hUbMM8rWDN3N9iIwwhAOkOHbHlyLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IYUUgu_gc7f2V_987QNTABuXWx2FQrQuZRl7nXQKbkoGr05yMXIHIyaZF4ryNf3R77JqNiwX7ydKIuDNO62GV_TQ-DqnwYs__ADwSZfb7mw0fUgEdgTO9u48h-VDIlZV-QEJgbM-Bv_isz0AWpDuBaazM4LQut0QQ1t6dQdQAyjIcpUyPdyhhwOvJ2Mo8JxtgW58KAkrfhLrQBKeHVM8F3zwm_q2AijRr_G1g7VwC0_71PNeyyHs7FT8DfrfCDkE3VQDYOLqDO-igMYkdjPNh4G1dfboSu06DnqpdyPyzVzL55mph4OxY8B_B3C84IECVAvHsnbmNLgIW43YQ_ZrIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gK2NQH3oueU0NTf0P3H3W4psYLdYCMol8sdvuzBe7VIEEYrPW0cM8avBrDpna6ePmsEC1CW0E_h2gQjckraykCZxsDE0flf6yDtJc6vfCN40blL-J9LObp1RJl_fX9jvzgScyWGXKdub7yewL8JQYiDzcumInyZfXzIpOqHuHvo1yUOcnDq6YivqeTGBginCfkTG5jZVdDnm4Qz06Al62bE6UyzRergfEL2FOkRX4rQIQjYH57isMtO60OpOSOlmy5tZvlXgk1p6ItMVpqGyWiKxZElSggcgIt8OKsb_KIZObnveyzJT7_eIJ0j2SuMyrPGbtk3OEVwG0Gwi40O0Zw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
منابع پروتئینی هم متنوع هستند با بهره‌گیری از تمام آنها میتوان از سایر مزایا نیز بهره‌مند شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/akhbarefori/671125" target="_blank">📅 22:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671124">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbaf1ccbd8.mp4?token=KhefnX--Kf81fmjXBJuorTMh49xgKIGO8bzxjNZzR8fQ5ERKoecKY96qzYkV-6qZGSBlva8Hcmzjch8uB9sCpfcdluRKM02fIptSm6U7xmF8m3ZYobJAtJKtRRRtuGdBLmgxRbNgKQZjgUypnOXkWCnYq-2gQk_boh8S5IImXeTIz1yewjwnl6v7pYrz57fovTEBj9phLsGkxh6HFlvRk3IERdL6x38Vkz_CMVLO2yod96nh1OR_usivloZCxLOOXYMfA4J5eSZXvcbCidYdWoVgbyNEx6u6l4YdUSPtC1CzjjAmhH7LmK0WFyjLYWyxzkQOi67Vg7h_I4K4p9DTV3LU1N34J9xFXO_c27BQ0vAdCRH01DAFgV04ouBFToETaUZeffvCXC7YHx8m0tjX7NCM_f864o1_tVv7qdsyzthmnupmnAXbJ2eZZuJB2VRYRsdfLmB70pNQQEDgrGKOEHYbf_U3oQ0643B2ZeEaoqtmQCwv38ZundwExu2YVYW2zlhGlk7D8UHQdDWmFjt6iMoJ_ZwQsmOQIDxg9UigSIrh4TPOylw077yb_1juBsRJRyRFfDW6lw8vNEoFcNRyo2etf4s5jZHpHfAqhHSNCxWZblufHbR_GPFMiuDHWS7KvnDsxC2NjL0c--EFk_vi-FJ7igkC_n9cabAztokIwAE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbaf1ccbd8.mp4?token=KhefnX--Kf81fmjXBJuorTMh49xgKIGO8bzxjNZzR8fQ5ERKoecKY96qzYkV-6qZGSBlva8Hcmzjch8uB9sCpfcdluRKM02fIptSm6U7xmF8m3ZYobJAtJKtRRRtuGdBLmgxRbNgKQZjgUypnOXkWCnYq-2gQk_boh8S5IImXeTIz1yewjwnl6v7pYrz57fovTEBj9phLsGkxh6HFlvRk3IERdL6x38Vkz_CMVLO2yod96nh1OR_usivloZCxLOOXYMfA4J5eSZXvcbCidYdWoVgbyNEx6u6l4YdUSPtC1CzjjAmhH7LmK0WFyjLYWyxzkQOi67Vg7h_I4K4p9DTV3LU1N34J9xFXO_c27BQ0vAdCRH01DAFgV04ouBFToETaUZeffvCXC7YHx8m0tjX7NCM_f864o1_tVv7qdsyzthmnupmnAXbJ2eZZuJB2VRYRsdfLmB70pNQQEDgrGKOEHYbf_U3oQ0643B2ZeEaoqtmQCwv38ZundwExu2YVYW2zlhGlk7D8UHQdDWmFjt6iMoJ_ZwQsmOQIDxg9UigSIrh4TPOylw077yb_1juBsRJRyRFfDW6lw8vNEoFcNRyo2etf4s5jZHpHfAqhHSNCxWZblufHbR_GPFMiuDHWS7KvnDsxC2NjL0c--EFk_vi-FJ7igkC_n9cabAztokIwAE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چطور با فرزندم که به وطن عِرق ندارد مواجه شوم؟
!
پاسخ مشاور را ببینید
/ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/akhbarefori/671124" target="_blank">📅 22:30 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671123">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
دبیر کل سندیکای صنعت برق: خاموشی‌ها فقط به تابستان ختم نمی‌شود و احتمالا به زمستان هم کشیده می‌شود
مهدی مسائلی، دبیر کل سندیکای صنعت برق در
#گفتگو
با خبرفوری:
🔹
با وجود ورود نیروگاه‌های خورشیدی و سیکل ترکیبی، کشور همچنان با دست‌کم ۱۰ هزار مگاوات کسری برق مواجه است.
🔹
دولت برای مدیریت ناترازی برق دو گزینه دارد: محدودیت برق صنایع مانند سال گذشته برای کاهش خاموشی خانگی، یا افزایش خاموشی بخش خانگی با هدف حفظ تولید و فعالیت کارخانه‌ها.
🔹
از ۱۰۰ هزار مگاوات ظرفیت نصب‌شده نیروگاهی، در بهترین شرایط تنها ۷۰ هزار مگاوات قابل تولید است؛ روز گذشته نیز با پیک مصرف ۷۱ هزار مگاواتی، فقط ۶۳ هزار مگاوات برق تأمین شد. به دلیل کمبود سوخت نیروگاه‌ها، احتمال تداوم خاموشی‌ها در زمستان نیز وجود دارد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/akhbarefori/671123" target="_blank">📅 22:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671121">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AC1Wq89Yjixq2ovsRbg9r6CTiyh-1B9XqoZYX0mfQNa-03xggnFxsrO0CWH8ncFuLXn0YAdutfMGia4SOrFaaI98QX8DCBF3LZgeUyy3wYKoHTODrRgwFivT8uCgxvdZ_DjOMHBRJHb6e_1xd2xylIuG9T88agDPe4orxtm7-ntNaGTHTD2YinF0dTsgIOZBld48g2nraGQ_JckXufCvxpnL_8mKa_cpEiUmqLUoKMjcH9Tpu1jouf6KQDDgCXmTeo4dWRVAZICSvxEMwbmoYSBvPmrtn2W6CFk0-o4wby8JRkiU_ZCalI_F1034z9TOfk25Y3YGARzvG7_pfNKloQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/voKbI-NYYPh-01JJT5ZbjlL7z0abcFO09eu_qtKEzf7ZqAwxj75ZH8iWvViLXwFUJVy59HyJIkq0BvA24AC3tIVfs4UoNU0M42dy8v9B9XkGGdnY1I6cw2Gqt4-lQMpW7SCCStBeOnzWqOfyhF0H5WObP072Gs6zft3ejFESaX3UkVh8D95XgjQjFs6dA1oeEkKxdgCZd3U4D2z-I1GKh2oz5QbxZTAQ1iTNTEj__2Xvkl9CJ07cD5g0ieeJdRxW1_eLsdTJ-THEoite_r3io9q7p6rCV4exXJYEI5BF01j5wEqI_Q2HTJu-cRJYmVh-Xs2ylTcqeo1Hr5Rj_r-b4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
معرفی انیمیشن: بچه زرنگ (۱۴۰۱)
🔹
ژانر: انیمیشن، ماجراجویی، خانوادگی
🔹
امتیاز: ۴.۱
🔹
خلاصه: محسن، پسربچه‌ای عاشق ابرقهرمان‌ها، پس از آشنایی با آخرین ببر ایرانی وارد ماجراجویی پرهیجانی می‌شود تا او را از دست شکارچیان نجات دهد. «بچه زرنگ» با ترکیب طنز، هیجان…</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/akhbarefori/671121" target="_blank">📅 22:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671120">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc203453c9.mp4?token=kPSqzfOOFOpWH-106DdSdRXYH5WbWrhQ0AMGdOT_COKUATGEWic_ncDypvirbigLu2GZ_vd6b-gNyQTaswlM2VRheEulRP2ti9FMcJoC4zG8FAbmfxpUT62SYDhFOi8Q85b0CyblACFaRqcGuhSFe0Biok5vLTR_M4pzQ0Bl0PNYCgcj56nTqC5nInkWA7msuJdgv2DBcBHOHIp72F_62xUzuqDHZXsT_PpU4fF2SA64c517ea1yMZdOpFMnSsbs6Z8h_hl_BN2zdbHBfynO4P0y8rS7Q6XifvbxO-_Qqv3XFfCPoYXfil4Uo-hRnlFDEKCUVIiYa4LNvrALWGtn7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc203453c9.mp4?token=kPSqzfOOFOpWH-106DdSdRXYH5WbWrhQ0AMGdOT_COKUATGEWic_ncDypvirbigLu2GZ_vd6b-gNyQTaswlM2VRheEulRP2ti9FMcJoC4zG8FAbmfxpUT62SYDhFOi8Q85b0CyblACFaRqcGuhSFe0Biok5vLTR_M4pzQ0Bl0PNYCgcj56nTqC5nInkWA7msuJdgv2DBcBHOHIp72F_62xUzuqDHZXsT_PpU4fF2SA64c517ea1yMZdOpFMnSsbs6Z8h_hl_BN2zdbHBfynO4P0y8rS7Q6XifvbxO-_Qqv3XFfCPoYXfil4Uo-hRnlFDEKCUVIiYa4LNvrALWGtn7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون حقوقی وزارت خارجه: آمریکا با بازگرداندن محاصره کاملا تفاهم‌نامه را متلاشی کرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/671120" target="_blank">📅 22:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671119">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
سپاه: چندین سوله نگهداری تسلیحات، قطعات شناورها و هواگردهای دشمن و رمپ استقرار پهپادهای MQ9  در بحرین هدف موج سوم قرار گرفتند
روابط عمومی سپاه پاسداران انقلاب اسلامی:
بسم الله قاصم الجبارین
الَّذِينَ آمَنُوا يُقَاتِلُونَ فِي سَبِيلِ اللَّهِ ۖ وَالَّذِينَ كَفَرُوا يُقَاتِلُونَ فِي سَبِيلِ الطَّاغُوتِ فَقَاتِلُوا أَوْلِيَاءَ الشَّيْطَانِ ۖ إِنَّ كَيْدَ الشَّيْطَانِ كَانَ ضَعِيفًا
🔹
ملت شجاع و بصیر ایران اسلامی؛
رزمندگان غیور نیروی دریایی و هوافضای سپاه در موج سوم عملیات نصر ۲ با رمز مبارک یا زین العابدین علیه السلام و تقدیم به ملت مبعوث شده، طی یک عملیات همزمان موشکی و پهبادی در ساعاتی قبل چندین سوله نگهداری تسلیحات و قطعات شناورها و هواگردهای دشمن در پایگاه شیخ عیسی بحرین را منهدم کردند و همچنین با حمله به رمپ استقرار پهپادهای MQ9 دشمن در پایگاه علی السالم کویت تعدادی پهپاد را منهدم و یا به آنها خسارت وارد کردند.
🔹
این حملات در پاسخ تجاوزات بعد از ظهر امروز ارتش کودک‌کش آمریکا در حمله به تعدادی از ایستگاه‌های ساحلی نیروهای مسلح ما بود.
🔹
مقابله به مثل و تنبیه متجاوز تا وقتی جنایت آمریکا ادامه دارد استمرار خواهد یافت و در صورت تکرار این تعرضات با پاسخ‌های غافلگیر کننده مواجه خواهند شد.
🔹
تا زمانی که شرارت های آمریکا در منطقه وجود دارد یک قطره نفت و گاز از منطقه صادر نخواهد شد و این تجاوزها جز تأخیر در بازگشایی تنگه هرمز نتیجه‌ای نخواهد داشت.
و ماالنصر الا من عندالله العزیز الحکیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/akhbarefori/671119" target="_blank">📅 22:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671118">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
سلطه شهرهای خوزستان بر لیست گرم‌ترین‌های جهان؛ ۶ شهر استان در میان ۱۰ نقطه داغ کره زمین
🔹
بستان: با ثبت دمای ۵۱.۶ درجه سانتی‌گراد (رتبه دوم جهان و گرم‌ترین شهر خوزستان)
🔹
اهواز: با ثبت دمای ۵۰.۸ درجه سانتی‌گراد (رتبه سوم جهان)
🔹
امیدیه: با ثبت دمای ۵۰.۵ درجه سانتی‌گراد (رتبه پنجم جهان)
🔹
صفی‌آباد دزفول: با ثبت دمای ۵۰.۵ درجه سانتی‌گراد (رتبه ششم جهان)
🔹
آبادان: با ثبت دمای ۵۰.۲ درجه سانتی‌گراد (رتبه هفتم جهان)
🔹
بندر ماهشهر: با ثبت دمای ۴۹.۴ درجه سانتی‌گراد (رتبه نهم جهان)
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_Khozestan</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/671118" target="_blank">📅 22:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671117">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YvHsrckHWV4d3w3-aFfzcoEKYYPqDE9y2nhHdT0omkcj26yCPgocwoNoZcWcU8VTOw_qtpE-wic8eduXcou38K5udAIZ3gPI2RWpur3wLDJZQTVPF9gGbOAZzwOPzZycRVa5VptGhrHaPZ0HdU9DfnkD0Z569j05wMAQYGf9YdpLvFqnBs_AvhIogPwJ4wqjIbSdU3f8lXHcBx5PP_89lZWx6ABaLB_-67Gi5-5YheHqv3mfUYl3n65ZEoXUFlWkdQnrC9LrU4moaBm7MbCsfBSvS7LBD09tt0UIXQww5zgTtX20Ts3Ou8bsrDh-ev8mDHAnXQNE-gaaD-l1UDGtrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سفارش کارت بانکی با طرح ماه تولد از طریق اپلیلکیشن دیما/ ۳۰ طرح جدید کارت برای مشتریان بانک ملت
‌‌
🔷
بانک ملت امکان انتخاب و سفارش کارت‌های ویژه ماه تولد را را از طریق اپلیکیشن «دیما» فراهم کرده است و مشتریان می‌توانند از بین ۳۰ طرح جدید، کارت ماه تولد خود را انتخاب و درخواست صدور آن را ثبت کنند.
‌
🔷
این مجموعه کارت‌ها شامل ۱۶ طرح عمومی، ۱۲ طرح مرتبط با ماه تولد و ۲ طرح ویژه مشتریان مهان است و بدون نیاز به مراجعه حضوری از طریق شعبه دیجیتال بانک ملت قابل سفارش خواهد بود.
‌
🔷
در بازه برگزاری جشنواره کارت‌های جدید بانک ملت تا پایان شهریورماه، صدور و ارسال کارت برای مشتریان رایگان است، به این صورت که مبلغ کارمزد کسر شده پس از ثبت درخواست، ظرف ۲۴ ساعت به حساب مشتری بازگردانده می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/671117" target="_blank">📅 22:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671116">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTBpnEonF_1VZbIJv48IFX2JTKNeVTe_SI6TW3ozrHNfI6ej_wvDCUhg7HKLIxr8gXbtERIvSk90j28nOISiL8ApGAz3M4nr6w9bHthYAz7vsTfTJR_PmiYsYg3PQn92Ho1nN_0V3XbqoppNTzJDFzMl54TVd3YBPegxvNhRCWgzJfORJguLo32NQjSz1_4rZHEwXYbVnuTj1YnkdsFzGvIK64oC10UbPnc5BrfdTNjAX34MvKzNYnQjoYzqM-FI9OwYAQE8LUoPAYrBOUWJcuOCLd66YmxG5megoUj0Rg7CyhPxUVNwWGioUNrMXhIzdqSzLsObQAYod6OAPRWD_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
خون در برابر خون؛ جدیدترین دیوارنگاره میدان فلسطین اکران شد
🔻
دیوارنگاره جدید میدان فلسطین تهران با تصویری از ترامپ، نتانیاهو و خانواده‌هایشان رونمایی شد. این اثر با تأکید بر خون‌خواهی امام شهید و شهدای مظلوم جنگ اخیر، پیامی صریح درباره پاسخ به آمران و عاملان این جنایت‌ها ارائه می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/671116" target="_blank">📅 22:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671115">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
وقوع انفجار مهیب در حومه دمشق
🔹
گزارش‌های اولیه از شنیده شدن صدای یک انفجار بسیار بزرگ در شهر «صدنایا» در حومه دمشق حکایت دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/671115" target="_blank">📅 22:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671114">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8de3410e77.mp4?token=cBRym-LMt2JTeHKK6wisaEmhjx9ZaRVJ6oxiHGfUgX1hcZRkhSX5eE3DvXjOs1VYGOi6mwNsPM-bdovWqyjj3u3uZrR7PsrMiLIOLBpGHIQB_SRhN_J-uOOKcvPFqJoZQnjlDyJouJYMbYKf46DKG_AFj8ROIxmhntFnMoK0wTqddaMORSiQQxXBL-LSCPM2aP5pJWw_oijtHG2sQKxuH0I2jIW0VOdUotseGoJVo0XR4np0gT8JywXA3Gl6S7N6pdPa-7HVC_V9S2cSHiiuH2Q8FIRjnJO87GSZq5cgo_J5bWvibLQrD2fS7c4eUk1u8VPINHAFhqbcXU52O4vZ-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8de3410e77.mp4?token=cBRym-LMt2JTeHKK6wisaEmhjx9ZaRVJ6oxiHGfUgX1hcZRkhSX5eE3DvXjOs1VYGOi6mwNsPM-bdovWqyjj3u3uZrR7PsrMiLIOLBpGHIQB_SRhN_J-uOOKcvPFqJoZQnjlDyJouJYMbYKf46DKG_AFj8ROIxmhntFnMoK0wTqddaMORSiQQxXBL-LSCPM2aP5pJWw_oijtHG2sQKxuH0I2jIW0VOdUotseGoJVo0XR4np0gT8JywXA3Gl6S7N6pdPa-7HVC_V9S2cSHiiuH2Q8FIRjnJO87GSZq5cgo_J5bWvibLQrD2fS7c4eUk1u8VPINHAFhqbcXU52O4vZ-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون حقوقی وزارت خارجه: آمریکا با بازگرداندن محاصره کاملا تفاهم‌نامه را متلاشی کرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/671114" target="_blank">📅 22:09 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671113">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58c15bb8d4.mp4?token=r1CTEt3en7X1yeEaFMfMH5kAvphgHSKx_99uCLCJgsxP99rCp-geOYK1wVO-8zeUSl033DkXLpv5MwnMzpXkcQsmkNv8xZFqa6fFKpR0EBx764tJ61j0WB_cWrjvcXJSmPmN6-j_vMIgh-k395QNp4EDobolPWXPmXRTeCs-gEpyXC5g7uFa9ZuVkTYK355QPPJtKnxZf03dbj6eUqfiQxWkrj3d45ERYDD1zQRve7FRdM3nE4xulnsewoOqOBxKv62EtqDhB5P95HQh6Tpho72st1aah_Ezu6ZUqNVRjrIpoONldg4P4dRipKk_KXodsZQuKPee-eqHzvsJ43md4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58c15bb8d4.mp4?token=r1CTEt3en7X1yeEaFMfMH5kAvphgHSKx_99uCLCJgsxP99rCp-geOYK1wVO-8zeUSl033DkXLpv5MwnMzpXkcQsmkNv8xZFqa6fFKpR0EBx764tJ61j0WB_cWrjvcXJSmPmN6-j_vMIgh-k395QNp4EDobolPWXPmXRTeCs-gEpyXC5g7uFa9ZuVkTYK355QPPJtKnxZf03dbj6eUqfiQxWkrj3d45ERYDD1zQRve7FRdM3nE4xulnsewoOqOBxKv62EtqDhB5P95HQh6Tpho72st1aah_Ezu6ZUqNVRjrIpoONldg4P4dRipKk_KXodsZQuKPee-eqHzvsJ43md4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جلیلی: انتقام باید به‌شکلی باشد که مردم از آن راضی باشند
#تقاص_خواهید_داد
#WillPayThePrice
#خونخواهی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/671113" target="_blank">📅 22:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671112">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdb1475316.mp4?token=CWq7MBxvvX9wVSG_n3kwsuNhwsAuTbBdFiS7i3QU3qmrPIWFFruhpwB1Qj2W61AFMjvWWO0h40C00sN8NmS5G68irwgKJmSABUhngB-7EDe4DyFWpDoYz8xeWr8VZkTAfEvKgmWFbMj4FHrdAj0XT1jnfw4HMX5FxXWJGWDZgt3lw3oGCqi5XX_V1bGowA1fuX8DourOnZp8zu4qkQkHcF7odvNxd65BNEHN-t0OodCGsW_IGcwAMB7yAmaKawVGoRVPfaj-dlk7waSFfkNxYvcrMo3hSWqhRrd3ODJpYrgCCi7Jw0z2P74nVv-tbxtOoA-0v2It_yI34Yh7SxYtfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdb1475316.mp4?token=CWq7MBxvvX9wVSG_n3kwsuNhwsAuTbBdFiS7i3QU3qmrPIWFFruhpwB1Qj2W61AFMjvWWO0h40C00sN8NmS5G68irwgKJmSABUhngB-7EDe4DyFWpDoYz8xeWr8VZkTAfEvKgmWFbMj4FHrdAj0XT1jnfw4HMX5FxXWJGWDZgt3lw3oGCqi5XX_V1bGowA1fuX8DourOnZp8zu4qkQkHcF7odvNxd65BNEHN-t0OodCGsW_IGcwAMB7yAmaKawVGoRVPfaj-dlk7waSFfkNxYvcrMo3hSWqhRrd3ODJpYrgCCi7Jw0z2P74nVv-tbxtOoA-0v2It_yI34Yh7SxYtfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جام جهانی ۲۰۰۶؛ عصر اسطوره‌های تکرارنشدنی
#ورزشی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/671112" target="_blank">📅 22:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671111">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
ایرنا: شلیک پرتابه دشمن آمریکایی به قشم
🔹
دقایقی قبل نقطه‌ای در جزیره قشم مورد اصابت پرتابه‌های دشمن آمریکایی قرار گرفت که گزارش تکمیلی پس از ارزیابی‌های اولیه اعلام خواهد شد.  #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/akhbarefori/671111" target="_blank">📅 22:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671110">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/287e492c12.mp4?token=rqseluHrN5yBMw5ylBaBUnjCupp84fM6ntqdL-Bg-SJfYjExh0Utm_xX6euvWpIHFzYWVEN7N9X7UGWqdQkPly0Jjn6DhQWVgswh5ln9Tq4ADRwRgTE_UPCFOliT4Z6tGpk5cQU6JmNO3tWq60H__wsN7S81vtHyijSom9pR3T9i-R52aXX3woNAqH0lT13HSLDw5TeUu9jaPYj-5HBiequJs2Fh-eH8s2jy9foM-lssvtokGanAy2wDro5LTgyfQ5OwgUWt5E7DrQYfKytpIEUnrVeS5Ni0FzZBgppHekWU_93-LiLjoVV2rRUOJ0A3HA88OXEpEH0mZAvILUG4egd4JoIqfmGY06NaEslFRI6ggPf29Z_p5YcNnOjk4y4xxUtsuxlJpeRg2BY-narfvm44-Dn7AaptXCA-Kn7SZ0O9TyaZy7-rwfHjxHsR-scBJzG2FlT4g6bBEawbqYzo60AAcixmdcC-t1Ue4703bokFGRR1sI1w3UhIosaM7XrzzLfTuaGHcjB5iJ3i2xSz_OqUjMNLr0kMMR96ltd9rAnz2vyYDrwHE1evhJALufo0JM-OuEgLZVFWTtAQ5XFxxttxX-2x6pZapnM0OXPolWoaZCxhuBPYkzQEgMjekOqxa5Fbz-QsBHanbIu4kANOarWeEtO52Vxbg54u7lm6Dhc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/287e492c12.mp4?token=rqseluHrN5yBMw5ylBaBUnjCupp84fM6ntqdL-Bg-SJfYjExh0Utm_xX6euvWpIHFzYWVEN7N9X7UGWqdQkPly0Jjn6DhQWVgswh5ln9Tq4ADRwRgTE_UPCFOliT4Z6tGpk5cQU6JmNO3tWq60H__wsN7S81vtHyijSom9pR3T9i-R52aXX3woNAqH0lT13HSLDw5TeUu9jaPYj-5HBiequJs2Fh-eH8s2jy9foM-lssvtokGanAy2wDro5LTgyfQ5OwgUWt5E7DrQYfKytpIEUnrVeS5Ni0FzZBgppHekWU_93-LiLjoVV2rRUOJ0A3HA88OXEpEH0mZAvILUG4egd4JoIqfmGY06NaEslFRI6ggPf29Z_p5YcNnOjk4y4xxUtsuxlJpeRg2BY-narfvm44-Dn7AaptXCA-Kn7SZ0O9TyaZy7-rwfHjxHsR-scBJzG2FlT4g6bBEawbqYzo60AAcixmdcC-t1Ue4703bokFGRR1sI1w3UhIosaM7XrzzLfTuaGHcjB5iJ3i2xSz_OqUjMNLr0kMMR96ltd9rAnz2vyYDrwHE1evhJALufo0JM-OuEgLZVFWTtAQ5XFxxttxX-2x6pZapnM0OXPolWoaZCxhuBPYkzQEgMjekOqxa5Fbz-QsBHanbIu4kANOarWeEtO52Vxbg54u7lm6Dhc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روزنامه‌نگار آمریکایی: از منظر عینی، هیچ تردیدی وجود ندارد که این آمریکا بوده که  توافق‌نامه تنگۀ هرمز را نقض کرده‌است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/671110" target="_blank">📅 21:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671109">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
ایرنا: شلیک پرتابه دشمن آمریکایی به قشم
🔹
دقایقی قبل نقطه‌ای در جزیره قشم مورد اصابت پرتابه‌های دشمن آمریکایی قرار گرفت که گزارش تکمیلی پس از ارزیابی‌های اولیه اعلام خواهد شد.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/671109" target="_blank">📅 21:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671108">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3ba926c24.mp4?token=tInRXF0me2wEhB_zVw7j0Vm1fLRyt1tfOnQcBPPOuexPveDfAMt0gLvH2KKW67tgQ8FMwwBqubwWxLj8pazn2k4Z6Ezh87Gr9AVgtRZ2QK4edD4udkS0GEmtfSqSL4QwfkOM7JneWo8UFZj-XpPvnv20ZimDF08ZFHxZd6CctrNY-x9sT59t24plwUGTOMVfeAeAueiYc3nU3KqlxJFZU55TEY4b4QqyxfTIYJ2RMi0B22tVjxgeorkTdzNOlnK_benvgsyqCYY_R9dYl1gBcJhGC16IO2gOQf34uzHArzHdSLYwhqfa3PhrRK7bYC-wOLjxhBJW2Zhh6h2COXs4VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3ba926c24.mp4?token=tInRXF0me2wEhB_zVw7j0Vm1fLRyt1tfOnQcBPPOuexPveDfAMt0gLvH2KKW67tgQ8FMwwBqubwWxLj8pazn2k4Z6Ezh87Gr9AVgtRZ2QK4edD4udkS0GEmtfSqSL4QwfkOM7JneWo8UFZj-XpPvnv20ZimDF08ZFHxZd6CctrNY-x9sT59t24plwUGTOMVfeAeAueiYc3nU3KqlxJFZU55TEY4b4QqyxfTIYJ2RMi0B22tVjxgeorkTdzNOlnK_benvgsyqCYY_R9dYl1gBcJhGC16IO2gOQf34uzHArzHdSLYwhqfa3PhrRK7bYC-wOLjxhBJW2Zhh6h2COXs4VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قسمت دهم مستند احیاء و حقیقت | یادمان می ماند
🔹
تقدیم به آنان که در میانه آتش ایستادند!
🔹
آن‌ها می‌دانستند کار در یک کارخانه فولادسازی، هنگام وقوع حمله، تنها به معناین شنیدن صدای انفجار نیست...
🔹
انفجارهای زنجیره‌ای، نشت گازهای خطرناک، ریزش سازه‌های عظیم…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/671108" target="_blank">📅 21:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671107">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d052002c2.mp4?token=P_QqDbksXnlG3tk7Gl_j4g4sKmhm_PNpU5hhRhp84hsqtKg9pDv9eJyfEVugdq49uRbxglX249x-70WRr2MI8GnAzutm21Isg1uAuVhsxBt0PZNEAgoaXtrsMb_tXowMnjx0TZp5qvemo5CZpUu29dvOnTM6R6tBl9x5pZ3cgGbyAgfXBBDqLegdEU84-dZ4G4ev-yBvuIrxrCd-t0loHAQzmrwI6B8ne_rIqhRYiVObd_sC3mhFtmm4Hkwlkm806F_XNl-8SGlJ1NesjnV_s9CESafetmFew6eu5WIuyG2bQEeuRnXLq51V1vJ5bf9VwyY1UzImfkmQhBVf6Ak4Si5NXl4p5Bg85sZyEcKNq-oQ5MQsBrh-ojGWpqTCE9JvZ2v4wcvPiXuMOQAFTNmfkzCc_Var7ZA2cHf1MVHWmBOCZGkh39x1RP9MYXRj9qYNYEywWGQ8sPo-IpIBWJQ6S0rSOTsPCTdKSuPk8Mi0iyH5PSIbW3j_jU4jlzszYnAAHLDNAwsePKqwflpgC250gZ2dNkGwWOFqoy96xyFI40FGXL4PcvG5dCmZUGLO_Qw1DSCQlmzPeeG-oW4sGkSnI5avj6ptxpVgXYk1hvSi6A6EDXFNIW8ZJ6DGO49OeT34uiYnGzbeQ6zHXmPhfdfDoCJlAvUqq3t9GkjTd8xEmJU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d052002c2.mp4?token=P_QqDbksXnlG3tk7Gl_j4g4sKmhm_PNpU5hhRhp84hsqtKg9pDv9eJyfEVugdq49uRbxglX249x-70WRr2MI8GnAzutm21Isg1uAuVhsxBt0PZNEAgoaXtrsMb_tXowMnjx0TZp5qvemo5CZpUu29dvOnTM6R6tBl9x5pZ3cgGbyAgfXBBDqLegdEU84-dZ4G4ev-yBvuIrxrCd-t0loHAQzmrwI6B8ne_rIqhRYiVObd_sC3mhFtmm4Hkwlkm806F_XNl-8SGlJ1NesjnV_s9CESafetmFew6eu5WIuyG2bQEeuRnXLq51V1vJ5bf9VwyY1UzImfkmQhBVf6Ak4Si5NXl4p5Bg85sZyEcKNq-oQ5MQsBrh-ojGWpqTCE9JvZ2v4wcvPiXuMOQAFTNmfkzCc_Var7ZA2cHf1MVHWmBOCZGkh39x1RP9MYXRj9qYNYEywWGQ8sPo-IpIBWJQ6S0rSOTsPCTdKSuPk8Mi0iyH5PSIbW3j_jU4jlzszYnAAHLDNAwsePKqwflpgC250gZ2dNkGwWOFqoy96xyFI40FGXL4PcvG5dCmZUGLO_Qw1DSCQlmzPeeG-oW4sGkSnI5avj6ptxpVgXYk1hvSi6A6EDXFNIW8ZJ6DGO49OeT34uiYnGzbeQ6zHXmPhfdfDoCJlAvUqq3t9GkjTd8xEmJU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بریم در خیابان‌های قشنگ ایتالیا یه دور بزنیم
🇮🇹
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/671107" target="_blank">📅 21:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671106">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edxbb62I_0AbrTLw_ScGHsOfp6dEcaoNz27HN8tOauBtAguD7xx9JF_5jAzOlPOalINaee7GgiChl0fJcqXdcvi3zT2NTLWKWKpQvyK7MSiU2PlupPeTSOxpLDi99PDJrZFMoNjhrk5bWZom-MqpkdpGyKzqsrNCst5Y04svTJVlUcP25pEPhClyWQoEJNl850XYtsly0trXegwn2nqppv4RU9wEScrNfyckmfS_07BITqXxLaMqOoLy9habRZvF64IChG_TEnFV_VIw3Npb15h_1DclsjbmvdAVVc2NWMaotf_RubP8qRTTsnfG0R7YVuexXVqXPf9iAmXLdtai7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آیا لیندسی گراهام با سم روسیه کشته شد؟/ سوالی که ترامپ مطرح کرد!
🔹
دونالد ترامپ، رئیس‌جمهور آمریکا، پس از مرگ لیندسی گراهام، سناتور جمهوری‌خواه، پرسش‌هایی درباره احتمال دخالت روسیه در مرگ او مطرح کرده است؛ موضوعی که بار دیگر گمانه‌زنی‌ها درباره روابط پرتنش واشنگتن و مسکو را افزایش داده است.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3230368</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/671106" target="_blank">📅 21:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671105">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c49773d4f2.mp4?token=vdEDS85Zfh9AQlFDxHvQmczJzzImddRXvErVBvLMTjEreUSoyzCYOGalKP9ryvmpDGPic5c1OwjlGQYnwG8OEjHPEG5l1Rfmcl1-yAGBMbA7RklPwMN_aHWJ7jd7fzYp86256nuSFjXBj2tC728xa7BHyHsSQR89i4AdCBBg8IE1Y3r8KkmqwlxhLO1tPFz2m06dqSaRBlf09toRvrgF8E2ogS-vJOKhc7PtbvJ8ZXnATHHoIAH5plckZPMSP5TEDEXJ-ABPcrRmMbS8VplGIBaD96OW_aMUUu157VD0cny-wASpE1IPKOLzQv3cvFVhihVssbgC3Z65McUGbAahCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c49773d4f2.mp4?token=vdEDS85Zfh9AQlFDxHvQmczJzzImddRXvErVBvLMTjEreUSoyzCYOGalKP9ryvmpDGPic5c1OwjlGQYnwG8OEjHPEG5l1Rfmcl1-yAGBMbA7RklPwMN_aHWJ7jd7fzYp86256nuSFjXBj2tC728xa7BHyHsSQR89i4AdCBBg8IE1Y3r8KkmqwlxhLO1tPFz2m06dqSaRBlf09toRvrgF8E2ogS-vJOKhc7PtbvJ8ZXnATHHoIAH5plckZPMSP5TEDEXJ-ABPcrRmMbS8VplGIBaD96OW_aMUUu157VD0cny-wASpE1IPKOLzQv3cvFVhihVssbgC3Z65McUGbAahCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برخی منابع اعلام کردند در حمله به مواضع نظامیان آمریکایی در بحرین از موشک‌های بارشی استفاده شده است/ فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/671105" target="_blank">📅 21:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671104">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
این منابع تأکید کردند پایگاه «شیخ عیسی» و ناوگان پنجم آمریکا، هدف شدیدترین حملات موشکی قرار گرفته است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/671104" target="_blank">📅 21:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671103">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
آخرین اخبار و حواشی جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/671103" target="_blank">📅 21:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671102">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
ادعای ‌سی‌‌ان‌ان به نقل از داده‌های ناوبری: ۲۲ کشتی تجاری از تنگه هرمز در شبانه‌روز گذشته عبور کرده‌اند/ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/671102" target="_blank">📅 21:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671101">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPtbpsvwsS8Tkp3yORDRcrdXBh4ftjDJelsk0hlvSv2HIxtEd66tNW53jumLysE1qhEVsJcOQIoBqCB9-AM6zKYAZOxEZ64t42qvktbX7IJ9MD4_RGsOzqoubfdd5hCY_UMts4Oj3srrcUgtmjiVZq1V0KPNudn7_O4pcRw7odKiO-Gj45wsnIXI-w6MQM0Nho3MrtIVp_RF-lfp2Vr9uwzVQLU6Dk4szIMaAjOtB9q9N8tXttVGj7rSTxgXS5wcCBTxEFkIzhIcnDP3GKvuTEg0pWeTOuQVwpeFeOseAHAG_dBHNGLxGPKWTByC0OPMj8eAfLhKYJyX5eXODRKHcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ملّی‌گلد در سال گذشته ۲۰۱۴۵ تحویل موفق فیزیکی در سراسر کشور ثبت کرد
پلتفرم خریدوفروش طلای آبشده آنلاین «ملّی‌گلد» گزارش سال ۱۴۰۴ خود را منتشر کرد؛ در سال گذشته تعداد کاربران این پلتفرم با ۲۹۸۷درصد رشد به بیش از ۱۷.۵ میلیون کاربر رسید.
ملّی‌گلد در این سال ۲۰۱۴۵ تحویل فیزیکی در سراسر ایران انجام داده و با ۲۳ شعبه در ۱۷ شهر امکان تحویل حضوری را برای کاربران خود فراهم کرده است.
همچنین در دل جنگ ۴۰ روزه نیز، سرویس تحویل درب منزل با پوشش ۳۰۰ نقطه در ایران را ارائه کرد.
رکورد سنگین‌ترین تحویل فیزیکی متعلق به کاربری است که در یک سفارش ۶۷۸ گرم طلا تحویل گرفته است.
دریافت گزارش سال ملّی‌گلد</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/671101" target="_blank">📅 21:30 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671100">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
واکنش نماینده مجلس به توهمات ترامپ: امنیت تنگه هرمز یا با ایران است و یا برای همیشه ناامن می‌ماند!
اسماعیل کوثری، عضو کمیسیون امنیت ملی مجلس در
#گفتگو
با خبرفوری:
🔹
از یک تفکر شیطانی (ترامپ) غیر از حرف‌های بی‌اساس چیزی در نمی‌آید. خب مردک تو از ۱۵ هزار کیلومتر آن طرف‌تر آمدی اینجا و می‌خواهی عوارض بگیری؟ چنین چیزی محال است و شدنی نیست.
🔹
امنیت اینجا (تنگه هرمز) یا با ایران است و یا همیشه ناامن می‌ماند. اگر لازم باشد یمنی‌ها حتما تنگه باب‌المندب را خواهند بست و باتوجه به اینکه عربستان با یمن نقض آتش‌بس کرده، باعث شد که اعلام شود جنگ شروع خواهد شد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/671100" target="_blank">📅 21:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671099">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m4KIAWF5oG9e0-2LEx4VJEv1bDQxHyGOc-McxyeJ4V0BjfvMVET5RUEMAeKX8uqueXzunk0cuUOK6CCJ-wW7goIbNx1n3Vbscqa_TPbwxTF6rtm7MZu3rmPol-ne9Lfo3Zz9R-9-EYhDrL9Q0ATLIQ5IuOWijax2BNytPFIXVCh0sT8ChGBm2Fd91AG2IeJar3F_E5gii-nf7wphvK4zX_NYul0usIEWzXW_DEi7zlcIzxjL8fEvoPqbjP2kZiN3Oky_Z54Ux-pWZE_YI6PdUSqdX1RxpPjuEpoTvpbRI44FNo6dNF7eQSX-E0dfq_yOwDH4Q1V1dWIF9U-fJLqKRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پلاکارد جالب زائران صربستانی در حرم رضوی: رهبر شهیدم، چون آهنربایی دل‌های همه را جذب می کنی طوری که از سه هزار کیلومتر دورتر به مراسم وداعتان کشانده شدیم و این دعوت را مشتاقانه لبیک گفتیم؛ سپاسگزار این روزی ویژه هستیم. عاشقانت از صربستان
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/671099" target="_blank">📅 21:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671098">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
برخی منابع خبری گزارش دادند یک پایگاه آمریکا در بحرین، هدف اصابت موشک‌ها قرار گرفته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/671098" target="_blank">📅 21:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671097">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fe7e9cf4f.mp4?token=HnQGLKfZapXSySS7_bDJR13BdR0hZTVApmFIuIGPkNvdNQ8gzCBZh8WS_-_ojZWGMXSuzeWLosJ-yN_i7j_vJHBU8DSpS_TcNwVtg11vRSP97F9TZC42c44o_n9cq1YfH8-nkOJAXOaDNzptYrwAHOlsYvotr8K5qrK7-29GCjlYmSC1Dd-GkBMYsnL5YLPNPPyHs5cIUxYDMMp6Tp9LFTFanKWBANGtIMCj4blVxhETyo0k1L0qI-QJ3XrxntuVp1viBrkd0gWuxYTjTmMEZR64rtL8oM05e9KsOCJ7ioSbMRoO_olHjXbp87451t5Fue-xr5zaKI17ZzMj7K4Fmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fe7e9cf4f.mp4?token=HnQGLKfZapXSySS7_bDJR13BdR0hZTVApmFIuIGPkNvdNQ8gzCBZh8WS_-_ojZWGMXSuzeWLosJ-yN_i7j_vJHBU8DSpS_TcNwVtg11vRSP97F9TZC42c44o_n9cq1YfH8-nkOJAXOaDNzptYrwAHOlsYvotr8K5qrK7-29GCjlYmSC1Dd-GkBMYsnL5YLPNPPyHs5cIUxYDMMp6Tp9LFTFanKWBANGtIMCj4blVxhETyo0k1L0qI-QJ3XrxntuVp1viBrkd0gWuxYTjTmMEZR64rtL8oM05e9KsOCJ7ioSbMRoO_olHjXbp87451t5Fue-xr5zaKI17ZzMj7K4Fmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
باقری‌کنی ،معاون دبیر شورای عالی امنیت ملی: برابر دشمن هیچ‌گونه انعطاف و نرمشی نه در کلام و نه در عمل نباید نشان دهیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/671097" target="_blank">📅 21:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671096">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rH2PN11wwUb14WGl73m6tF1dJbTt9nd_5I0hmqQRjKX3qsD3tJ4842DlCDBmDqVqUj13ZjA5G_c2MJgJzLnV-U6dCeX7jHwdUxy2CxaLhZ4dLyhrpH-PYB9SkyQ8xkZUUF7SGdFEGYuHjpDlcyJ-hatjovviasSioCj3vMntTuJ5n8DgNO7JPghN8wLnzyNyxIwO_5wSSofkMy0XjpB0LG0NFOTzF0flDZy75Ex2yLLdV79AUDs6lFyeraYu26pzp_IvFudnJCMdnqvIvp2Y6xxSpTWdgO_mu9D1UD49PAIQIyx1_LxkM1IeF-i9cafX57SCFNndlua7N67IFV0xzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رییس سازمان عقیدتی سیاسی فراجا: رهبر شهید انقلاب فرموده بودند رژیم صهیونی ۲۵ سال آینده را نخواهد دید؛ اکنون اگر دشمنان برای تحقق این سرنوشت عجله دارند، ما نیز آماده‌ایم و برای نابودی کفر جهانی آمادگی کامل داریم.
#تقاص_خواهید_داد
#WillPayThePrice
#خونخواهی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/671096" target="_blank">📅 21:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671095">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
برخی منابع اعلام کردند در حمله به مواضع نظامیان آمریکایی در بحرین از موشک‌های بارشی استفاده شده است/ فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/671095" target="_blank">📅 21:17 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671088">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YRHqc657Zeh8kcFX9V5UIXG3eR4IvxXyHC__0bc10NINriTgOWwPvESIIbIAQlzsNtcsqtYXC1o_ZT3fW897a2JWG1oQysX08tug4yAoqC7kmlLS1euJa-d7Z6Z6iUSCo20MRXSp-_BRjg2HpzJ75nWhL5_GjwQBJl-2l9maWM63LWoE8FTrQltSd4YYetEhPvnmdu6OG5PbrOnMOolvI8DCL4h6L2MLMd-tgSCKYLoUQw_TBWxvzX1Ykb64RZys5cY34sz498pfwlJNK6ORsg04a-S6hSS5J1nZO1-cy9f0gh_hJ1OEVwsBWc0Aox0430GfiXbbIb1hXuwe3bJJ1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aQw0qCjGkkUsT0G1OWxccwMsCpsGG6BvTqc4VR1cWGNCWnez1qtkhpOXJ9BUxXLfyps8bbJQWkKFcA8nJgfo9_aBm-CFLdt8kVM6gUvuY_cdW93qnvp0yev3lxaaG16TRsFNQZFAloTEx5Myy4ggecdb3scwz1rloCMiioW0YBLZ38UeIdHmxqoJmw91AvQIveaRSuCoe01rM9dGo77mcvvAGhWCzVomkSlcr9NV3XT7DIDLScpsT4EbjzV7zywsslhpOyEn1q6SsHcDLDWds_k1ECxBqFZNKLaUR96twLVq_gcVkh8GxgPnG_XMVIU56gnZwDA19whF24x1enuAsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZEmPLg-ikf4Z7NwunNFvYN08Pn-z6_TJVRLLfM475W3pLx4gq-93kpiDXGtNm2zelM2GlvgkUhrxuKDxEUiSphq2qWvmKQeBMjgGPJ4D6HkIGL_LcM1g5xa-xGrua-i_tpE1dWT7r1ZCykNI8_5gMucO5cNBAhvB5NP7-Fdq7b0a-VuZjUWP9ZQ_p4fFkNwEbHSt8bAM9xk_-JUMyIttt6HtyDdxNyptdqMXu922kLrfU-4y3jhUKVFd7kC7VakoSYqr6sNurDhrJ6_CZvQ5N6egNioahwOzAoBUpDM1Lpc_N9QTlea3TqdFmOkfDrtc6mWMl_JTBlnJ133Y-qwOKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iV7I0i3R_vYzlbwCxKBQhH4gK2uGtJIQhaEc2zIF-EHpQ3lXUvv3nBbwcNDeHCiYC-G_-tUxYdaCi-5jjC2DaH6_GPa8Qt6z5aqDs2y-8Mxc3QNIS7qHCawsI2nvEy87SoagG8V0Iobpf-0wu5Goj6x7uI9lgNM0XOFlQr8JGSTc9jqp7KVDqHS2wBstmmDS2L--mAiJ5dAnw8ZrwrDdVw2qcf3vdjNEIiauC4y3tMI9BKhOWf4-164zXpnpVAfu2StH8dqvAZkrNm9E57IZ1W0kLW_cO2jgqKCHq1cyexDtb1svweDkI2ytc7AwmK4UxooyVWsQVnaleyzcCPpkpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QoAGhaszA_H5C-cHNmrEubuKph9ZBq8j2dI_8Dpi0AzS_OHN82CbsErBTROiM4q69Hgwq5G4ytFI1iPEfLlFspAgONR71aN1jQB6bH6KMIfDKcH6dGZmRsXZknZWD-NozJJbDORMSiBy0fyBsAl4nE1nx0Wx0CJP1BBee1QYXOMqTOdkJar4_V3xtFQPzxeEAs6jL7kkGAjJUndoLAS9g08wVPtJRWJu4RDuvUCyFDVIV0xpA4cPIScg30OvZDwmHSIS8otIU3I3Px5GXYkCzc5S2OceeI9CcDHHxMBQilGMMd0kpAdwbzmgyHl-O2ZvE9YZDvC0RmSXs_Q16-H1Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SY3bwNW786Y0Pghf1pzKDBHE-d8FWOjcn-NvNNvLPZXnPeWa4tevVHj-rrrbPFIZZZSuLxqsT_D18GhHEuz2rlT9EgN4O2ogVh1c9bve8lB2w_SHTK76O5vNUFYvQuVA7Hu_wimKq658ExGqLXUCcci3RR9pWMyTmPWEnksz1WZCzEw-NsbX7uSvFp9NhWb90TOJmdsa2gygR1xYEinuEDnuoEx1YOb6tq7Itv3-IEUmXsucDflv9k_r4k8MZsrQ3bUBIVp2qCpuWSY9zgyjn8HRQoR7QePfMlFpsVySsiDfWTItYqEQg-8JiNRO0uK4CcgD19Fjo_yxdco2XA5aCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nAMdIJs-oBqnGG9rJmnLxEdMSe8uXDjcQ0vCNUdTQGxqxWXc92VBWCYwPqwbB-r4dFyFYOgKlXFY-soe7PHalQM5TuGoCsVGxMQqO9jYXr2mryf1S46xWWSDuIi_-Sc4QgnXdJzHKqfkwvTrVYLMhmOI-0dKCrCF7WPDNfKsQBorvzoX0sfEqr2WiQpycXDKiW7T9kjp-el_xDCfY9D_5ujBDyNvSQKxPc3W48P7gEIVpk2A0y_SB7guxmM0jZIwt4YEJ72gdXGKfUIDuYHfjQ-3Wdu8kWew9wzsMPZkuoP13EUmcsJ-OhRS4da-3xHbtgVvZhn9LKCkrvsaSJS8yQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
مراسم بزرگداشت رهبر شهید انقلاب در مصلای امام خمینی(ره)
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/671088" target="_blank">📅 21:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671087">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وزیر نفت: فروش نفت ایران در چارچوب‌های قبلی ادامه دارد
.
🔹
اکونومیست: ترامپ با بمباران نمی‌تواند تنگه هرمز را باز کند.
🔹
تعطیلی ادارات دهلران و کاهش ۲ ساعته ساعت کاری در باقی شهرستان‌های ایلام بدلیل گرما.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/671087" target="_blank">📅 21:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671086">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNad165tzvxwS-UhDp9HA_xHsIc785-EP0ezdOkunsLuKRqVk4hkTzw4yzFMVOJ5IQ2OKbJpRlW0wsogPDta3xYyOCh5mO4E7IfgqYFGQYKIX5Ghek7Req6fD7w_SEcm0l0rF76bmpB82oMZjfLLu6Nbsl-b_UiKbo3d6tJb8vXoDx1I9w558v1TMaGWECCrL95N66TilG_b43rEmP6UXaK_to6y6NCFi1haDqFPau8lhaFVnOF5_0ty2tUu7Q0UFQWC1kWV4Afo1CzOKGHlYWxGle7_uMCVryZAL6Y8ibZ_aBYv655vVBGVsEwBe_Bz-Fu2TKs4cjOKFFT3iq8rmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انفجار گسترده در جنوب لبنان
🔹
نظامیان ارتش رژیم صهیونیستی در ادامه تجاوزات خود به جنوب لبنان، عملیات انفجار و تخریب را در شهرک «کفرتبنیت» واقع در منطقه نبطیه اجرا کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/671086" target="_blank">📅 21:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671085">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
توانیر: از فردا قطعی برق برنامه‌ریزی شده در شهر تهران آغاز خواهد شد
🔹
با توجه به افزایش شدید دمای هوا و رشد قابل‌توجه بار مصرفی در پایتخت، محدودیت‌های برقی و خاموشی‌های پراکنده در تهران از تاریخ ۲۴ تیرماه ۱۴۰۵ آغاز می‌شود.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/671085" target="_blank">📅 21:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671084">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tmF_5C8TQs5M5fS3FFa8gyEfCTYmZhKwjK3YcxeVXgY1nhW-AwFTfwU0IQr6YxL-1Axyx1ICXDaFPZL-DJ86FavB8C9_DIV8I5kdmZgFGZph4WqJS5MOiegW7lmAJI3rasuTdYrWTyWgi9ayNpEjYIUf8c7g_K2_7jSVILOmfWeWRoYhoF-wXLMYKqhbIiNI6gbdBFZi8GIxB7bLLCrJaEFwSX8N_DnUZqcg7s4EiIkwN_ZDVHpJRp2v_WxLt-3s43nHccDHCeJfStiPlfYToa-IDfwG0HA-Wrz1gCLIP9atXkaflsYNw5h36kNRXl_3YaLT69zNZgG2YO6LjdZTNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سیت‌ دِلُم خینه
🔹
چند روزی است که جنوب ایران آماج حملات نظامی آمریکا قرار گرفته و مردم غیور این دیار با صلابت و استواری در برابر این تجاوز ایستاده اند. آنان با وجود همه سختی ها از سرزمین هویت و عزت خود دفاع کرده و بار دیگر نشان داده اند که روح مقاومت در این خاک ریشه ای عمیق دارد. مردم نجیب جنوب با شجاعت و همبستگی مثال زدنی، صفحه ای ماندگار از ایثار و استقامت را رقم زده اند. ملت ایران نیز قدردان این پایداری و فداکاری است و باور دارد که نام و ایستادگی مردم جنوب همواره در حافظه تاریخی این سرزمین باعزت افتخار و سربلندی جاودانه خواهد ماند
🔹
هشتصدونهمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/671084" target="_blank">📅 21:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671083">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adcbdf98be.mp4?token=pGN2sqhwgb25vOvtMektGa1XkyU3YKjxBJ2kY_c61PRcFRO_bxoWB96yHecXYN-9ypwr2EHwpntrJb2a5D2C9_73kASrDXTDrXWxguVMyr7oGK0OyvdtPfC6gcCj1Wyml8b5G16jfeYENRnG8_36SnTggunlp7WLKfXVrLpWRaswFtA78phCECUuYcIC0Yx9cIjg3oelBXV4JOh-NEtlcGP454TeQhaL6AhO1g3a3OKLGkMV7a0aIufiFcTml9VhuMIi_C0eJ0rHP_tJMaPRZGFAKYnE421JhIZ66XjmYAfaPz4EeCRSM_racWH6Dxj9AHoSjJrhfUOdyiBzUwtw1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adcbdf98be.mp4?token=pGN2sqhwgb25vOvtMektGa1XkyU3YKjxBJ2kY_c61PRcFRO_bxoWB96yHecXYN-9ypwr2EHwpntrJb2a5D2C9_73kASrDXTDrXWxguVMyr7oGK0OyvdtPfC6gcCj1Wyml8b5G16jfeYENRnG8_36SnTggunlp7WLKfXVrLpWRaswFtA78phCECUuYcIC0Yx9cIjg3oelBXV4JOh-NEtlcGP454TeQhaL6AhO1g3a3OKLGkMV7a0aIufiFcTml9VhuMIi_C0eJ0rHP_tJMaPRZGFAKYnE421JhIZ66XjmYAfaPz4EeCRSM_racWH6Dxj9AHoSjJrhfUOdyiBzUwtw1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منابع خبری از شنیده شدن صدای انفجار در بحرین گزارش می‌دهد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/671083" target="_blank">📅 20:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671082">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
منابع خبری از شنیده شدن صدای انفجار در بحرین گزارش می‌دهد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/671082" target="_blank">📅 20:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671081">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03d1312506.mp4?token=sYsOHn5f0kqXhDIHgGiX4Qxkjd8JXsn3iSr5e7ank7wcjElNj-rGyePj82vD8vEfX0LUpkdWWl-kI7HsyY9DMWgijqo5-QMRPx7spZxmsL-olIC6m8eb5n6Dj3RELhwbqvCrbqFddd1tne78S1yNy1iDLftdkjHXqXJteoqn4QQXqyh_MRu1oqpH8ZA1ANAAcNODsSFAfypcJcHHRCAZQSSpAoiGjw7rM-dxWBXMO7UGiK7EaDqoso5UI4rHJKt3ZcTmjMpfAT3kYuFrex2OeJLW0iLMPDUxL8ulezxOYEtYejbJtW-oOzeB_fCrXo9EwFl-Lyt7WUJJ1pWWojPIIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03d1312506.mp4?token=sYsOHn5f0kqXhDIHgGiX4Qxkjd8JXsn3iSr5e7ank7wcjElNj-rGyePj82vD8vEfX0LUpkdWWl-kI7HsyY9DMWgijqo5-QMRPx7spZxmsL-olIC6m8eb5n6Dj3RELhwbqvCrbqFddd1tne78S1yNy1iDLftdkjHXqXJteoqn4QQXqyh_MRu1oqpH8ZA1ANAAcNODsSFAfypcJcHHRCAZQSSpAoiGjw7rM-dxWBXMO7UGiK7EaDqoso5UI4rHJKt3ZcTmjMpfAT3kYuFrex2OeJLW0iLMPDUxL8ulezxOYEtYejbJtW-oOzeB_fCrXo9EwFl-Lyt7WUJJ1pWWojPIIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی ارتش: تنگۀ هرمز وقتی باز می‌شود که در آن ترتیبات ایرانی اعمال شود
🔹
مطمئن باشید دربارۀ تنگۀ هرمز حتی به اندازۀ سر سوزنی کوتاه نخواهیم آمد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/671081" target="_blank">📅 20:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671079">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nGmNsy33cyJx7NbTxmhjYaeCyoeSg9vx35Fk2mMuGYDtYaskhKjwmUd8MP_Lz61F2IIeSvmYFRr-oo04giYVoz_qwWMGM5MrxQbOv8ZY-gBcBznG1OiIFcEbGLO7Dc70NvaztIDbm7OG0wKEFY_Kmd5ZotJ7LZULmqr9dva9lO2o-wtPlEOOddghCLLcYpMLhD7nmyUKNzJzINMitBektwDlY5Jug-WcwSm_H8h-TrsirXqS7lh1OL00cy4c3uX8LaeI3iroqIaFzloRnkmvwIBj-xr9DpUSUv9bHOq8gYAU9xKgIRKKjwCVF2rYI9RcIMYozpER_LQXplw-ajUDlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WsK5InA-WnrqjODbqJz_6ZKwYyJsdMt0TXHVd-8mqA2NRaMDVWC1UXKBB7MTeAg3KQFxpb2xGIgLHSqKjUQPp2703A7tKEWBFKpxlaX4puUKjU32YYyoXcNkvIBajfasKLuEse9-VApOHp3hcsDrbXqdDYrLxBl_YbTpZr_raDyeNoGKScUsKIY581z3JLbwRegRJoG04LlsAqU3s_vgXOwRTwbhrIDZPEFpl6Gk9cm2eSJNh7IcbLvOnK1yGTZ6eaDGVv2fE3-MpyKTeE0A0R84ertIK-lFAu3_ygqCbb-mCy5NxVCegleObo9naMqhzBPlbJz2C8owfJ3XJ9aavg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
در سایه جنگ
🔹
گشت و گذار مردم در سواحل سورو واقع در غرب بندرعباس.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/671079" target="_blank">📅 20:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671078">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
رئیس‌جمهور جنگ‌طلب آمریکا خطاب به نخست‌وزیر عراق: ما [سردار] سلیمانی و یک فرد بد از عراق (ابومهدی مهندس) را کشتیم؛ نمی‌دونم بهتون لطف کردم یا نه؟
🔹
نخست‌وزیر عراق: در آن زمان در سیاست نبودم …. ترجیح می‌دهم دربارهٔ آینده صحبت کنم.
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/671078" target="_blank">📅 20:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671077">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a4lbNo1clkbBxhtdBlxsky9CcbwJzYAuIhmEVK4P28NB0rJX-l_oi91RbAld56x_z4-ktnXoJgjV9aHp_9B_IsLMg0yN1lQKkeOXj5iV_hUAI-eCRs-q4fDFUJcRpNXjsH3J2XJWBCSAI53LFCvh5SukoQ48IT4K14HpYS7PYfsNNnZQI007wsgYzPWVDKfnwIffhP1rOuCJpNNfX7cxkTiNtW7QYhPV1pBQ8i1D85NRwcUpZcZl7y8EwYGmpaCxgH34Rd6_B22RZ8rpZd6bUVyfRHG_U_mZtSeLoSdcZAhMTXyTUFTRFyvMSu_KuBpvwIjhe1erK3YAYztc-CCB-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اخطار مالیاتی به بانک‌های مالک مسکن؛ ۵ بانک ۵۰۳۵ واحد را در اختیار دارند
🔹
بانک‌ها در مجموع بیش از ۶۷۰۰ ملک مسکونی مازاد دارند که ۵ بانک سپه، تجارت، رفاه، ملی و اقتصادنوین بیشترین سهم (۵۰۳۵ واحد) را به خود اختصاص داده‌اند؛ سازمان امور مالیاتی این املاک را مشمول مالیات دانسته و برای واگذاری آن‌ها تا پایان سال ۱۴۰۵ مهلت تعیین کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/671077" target="_blank">📅 20:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671076">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15c1d559fb.mp4?token=PTjEQmRQOmOc0Yrzgj-B_z9lre7jEqon9f0_5Q5s0WmFTJ9xmlwIXfl6TqJn1FCBGL3sXoxIhiTtAlj7dsK7Sdhjy9R40fRIi0yDaJ0s8LSryKmYWdEXMVkvbKxn5FE1uK9ybZ0fS6UI-gvm8kaQzQ3k0IjEYsgYhheUvWzgBuGCGaqy5VwpxYUMPIA4lkt-_D_GeytTi_roaajd23o083GiiPuCO_0EMRD6vJouIbKJQZGZbJv3dKtSM7FD0S8fcs5uX0cEJe02_zONr6VdtPl0ZjGG_17Yk3uCit6JdgIDMA6UGQyS0grglylfM-Q-nlvosonhTpsLbSvTpOvhPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15c1d559fb.mp4?token=PTjEQmRQOmOc0Yrzgj-B_z9lre7jEqon9f0_5Q5s0WmFTJ9xmlwIXfl6TqJn1FCBGL3sXoxIhiTtAlj7dsK7Sdhjy9R40fRIi0yDaJ0s8LSryKmYWdEXMVkvbKxn5FE1uK9ybZ0fS6UI-gvm8kaQzQ3k0IjEYsgYhheUvWzgBuGCGaqy5VwpxYUMPIA4lkt-_D_GeytTi_roaajd23o083GiiPuCO_0EMRD6vJouIbKJQZGZbJv3dKtSM7FD0S8fcs5uX0cEJe02_zONr6VdtPl0ZjGG_17Yk3uCit6JdgIDMA6UGQyS0grglylfM-Q-nlvosonhTpsLbSvTpOvhPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: لفاظی‌های ترامپ را در عمل جواب می‌دهیم و از وجب‌به‌وجب خاکمان دفاع خواهیم کرد
🔹
بی‌ادبی‌های ترامپ شایستۀ خود آمریکایی‌هاست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/671076" target="_blank">📅 20:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671075">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
آموزش‌وپرورش: حوزه‌های امتحانی نزدیک مراکز حساس و نظامی جابه‌جا شدند.
🔹
فراجا: نیروی انتظامی در جنگ رمضان ۳۶۱ شهید تقدیم ایران کرده است.
🔹
قوه‌قضائیه: حکم اعدام ۲ تروریست وابسته به داعش اجرا شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/671075" target="_blank">📅 20:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671074">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88422be40e.mp4?token=lP-xzdkAlSuGkGJ_HgqaOCab_7suo22EaSVQXmd0WmQWbAwAaPny3RRQvPorc08h81DB7EIvC6vq-Px6HtUSKWjr9YZXdfG91wz7efYWTXIevD3coB7XeSr8aSpr69uIpqpxR6KLNARgl1js-BU0HRoTfr9c8buC6Np2Kex72FN3Kl38OlehNV6ahWXSnHKvJVqLWa8UboNJj5LWNlarfKefmbbjC2tdLx1UluydVaV5iJb5uWxviEhKyx8GVDdlEq1j-Y3MPrfhlJ6MQf625rVfDns2MhfMrU1tZ4WkQxvoUtlc8sqhRIDXnI3NoVO6tFlei0naafEg5d0Au1ifQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88422be40e.mp4?token=lP-xzdkAlSuGkGJ_HgqaOCab_7suo22EaSVQXmd0WmQWbAwAaPny3RRQvPorc08h81DB7EIvC6vq-Px6HtUSKWjr9YZXdfG91wz7efYWTXIevD3coB7XeSr8aSpr69uIpqpxR6KLNARgl1js-BU0HRoTfr9c8buC6Np2Kex72FN3Kl38OlehNV6ahWXSnHKvJVqLWa8UboNJj5LWNlarfKefmbbjC2tdLx1UluydVaV5iJb5uWxviEhKyx8GVDdlEq1j-Y3MPrfhlJ6MQf625rVfDns2MhfMrU1tZ4WkQxvoUtlc8sqhRIDXnI3NoVO6tFlei0naafEg5d0Au1ifQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی گسترده در پاریس
🔹
حریق گسترده در جنگل‌های فونتن‌بلو در جنوب پاریس، منجر به سوختن نزدیک به ۲ هزار هکتار از اراضی و تخلیه اضطراری ساکنان منطقه شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/671074" target="_blank">📅 20:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671073">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
اعلام آمادگی مقاومت عراق برای مشارکت فوری در حمایت از ایران
مسئول امنیتی حزب‌الله عراق:
🔹
در صورت آغاز جنگ علیه ایران، گروه‌های مقاومت به‌صورت فوری و قاطع در حمایت از ایران وارد میدان خواهند شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/671073" target="_blank">📅 20:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671072">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b95fb9dbc.mp4?token=GvrXfl7facNc2Pj0CMleLZVRCzvw7dgRhHPMKSUejLAU9JDiRs06n7VL6N7MO6d_3E6Pcc4lZIUAXlQrXAtnU2rFRReLrztQja-W0FdEblpnAaT9yk411J2TkVPBtOIofZtMG0rMn4dSqMHQJ0n2VHyBBVtv-C31WVWqwYnV46QuJocMx-2o_h1LlgFpcQiI3ZGlQze8mlEwU-dYJSuP7Fi6uMzTntDurn4a3S3FBiaNpRMhj0m-EunhXxaW7ZgllhlxILc9WWHomHsTIwutB_unU3hFjC5Qmv0x0wy63YF1NPuogNitcEgTSLF71sNtwU5XbNkgAH_Y4KuDlJ296Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b95fb9dbc.mp4?token=GvrXfl7facNc2Pj0CMleLZVRCzvw7dgRhHPMKSUejLAU9JDiRs06n7VL6N7MO6d_3E6Pcc4lZIUAXlQrXAtnU2rFRReLrztQja-W0FdEblpnAaT9yk411J2TkVPBtOIofZtMG0rMn4dSqMHQJ0n2VHyBBVtv-C31WVWqwYnV46QuJocMx-2o_h1LlgFpcQiI3ZGlQze8mlEwU-dYJSuP7Fi6uMzTntDurn4a3S3FBiaNpRMhj0m-EunhXxaW7ZgllhlxILc9WWHomHsTIwutB_unU3hFjC5Qmv0x0wy63YF1NPuogNitcEgTSLF71sNtwU5XbNkgAH_Y4KuDlJ296Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیام مهم سپاه به مردم اردن/ تاسیسات مهم و محل استقرار دشمن آمریکایی در یک پایگاه هوایی در اردن هدف موشک های بالستیک قرار گرفت  روابط عمومی سپاه:
🔹
ملت شریف و مسلمان اردن؛  سحرگاه امروز رزمندگان اسلام در مرحله سوم موج دوم عملیات نصر۲ بارمز یالثارات الحسین…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/671072" target="_blank">📅 20:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671071">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
از آزار یک پیرمرد در کودکی تا نجات یک جوان؛ روایت عجیب از عالم برزخ
🔹
00:06:00 تغییرِ ناگهانیِ بوی خوش به تعفن، با شنیدن وحشتناک‌ترین جیغ
🔹
00:12:00  آزار و عذاب توسط موجودات انسان‌نما در تاریکی مطلق
🔹
00:17:00 حضور منجی و دور شدن موجودات عذاب‌دهنده با صلوات
🔹
00:37:30  هیچ آتشی، مثل شرم از خطا، جان را نمی‌سوزاند
🔹
00:42:20 ماجرای شنیدنی از جوانمردی دکتر شیخ مشهد
🔹
00:55:30 کمکی که مسیر زندگی جوان را کاملاً تغییر داد
🔹
01:10:45 بازگشت به دنیا با خوردن یک دانه انگور
🔹
قسمت اول (رنج و گنج)، فصل پنجم
🔹
#تجربه‌گر
: سعید اعمی
🔹
قسمت قبلی
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/671071" target="_blank">📅 20:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671070">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
صدای انفجار در اندیمشک شنیده شد/ صداوسیما   #اخبار_خوزستان در فضای مجازی
👇
@akhbar_Khozestan</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/671070" target="_blank">📅 20:30 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671069">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/APtoIYg9n_79I5UJVkBJgt28r5uulFHlDi7hNsDP0nWA6GN1Lkf5nKnGxI586IWSUzdIYbD38RGy2kAtuvhtyhi6NqLIXDFJ8HqGklvp9x54wF-2Yi5hajRSzfC8Ia6_dUaPCxroZ2lSaKt4ggiL8K-nLE5fXNIhV7r6tYZvi5ihdrLIhtT8-s-5yq1LOq2LFwf-oTMuohLMoJjfcY9ISUXrmwrUkk6At4IXH067sinEQ7bBrUIYtLqENXS7joCIC2bvXCKQRpyY8DZq_E_LxUWucdEgpmcSqXyRL9bQWEcOg1YkkaRAIFAZKQORbJQ9BDTdE4WNGzd6_LyaGDgcyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیام جدید دونالدِ متوهم و اشاره مجدد به اشغال کانادا توسط آمریکا
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/671069" target="_blank">📅 20:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671068">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
کویت انتشار تصاویر مناطق آسیب‌دیده در شبکه‌های اجتماعی را ممنوع کرد
🔹
ارتش کویت در اطلاعیه‌ای رسمی، از تمامی شهروندان و ساکنان این کشور خواست تا از تصویربرداری و دست زدن به بقایای موشک‌ها و پهپادها اکیداً خودداری کنند و نزدیک آنها نشوند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/671068" target="_blank">📅 20:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671067">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
آژیرهای هشدار حمله بار دیگر در کویت فعال شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/671067" target="_blank">📅 20:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671066">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/502efd69ee.mp4?token=HSHqLTMZ6hEFiIcwkdiafQb3pAWzU-Rs8KU6rmTN257MKQRoUfry-7NVeoXgj9fBfJ_1TBxHYzvS4octscMDvIkzwESu-HqV7jST_Bm1ajIGnyuyY6zFrKasPyRMcasJFYRKP9Fk8ywpgTMQhNBdXSGUsQfddoTwW1DWb8myBv7WqHtJeb8gVydFOpepDJpVqAczep028KIQ5h2msLVNX_ZRN-6Vz5LaZm11zDn0BbD91-flr-sR9Fsfu1O51VkxrgTlcVFGuvqY4RDxx3VKWFTs7eYn5KwL85RJuteHBWt0kZJms2JhseVxR_BMg7QCW2Ace8-hqfMg3Ja1E-JjcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/502efd69ee.mp4?token=HSHqLTMZ6hEFiIcwkdiafQb3pAWzU-Rs8KU6rmTN257MKQRoUfry-7NVeoXgj9fBfJ_1TBxHYzvS4octscMDvIkzwESu-HqV7jST_Bm1ajIGnyuyY6zFrKasPyRMcasJFYRKP9Fk8ywpgTMQhNBdXSGUsQfddoTwW1DWb8myBv7WqHtJeb8gVydFOpepDJpVqAczep028KIQ5h2msLVNX_ZRN-6Vz5LaZm11zDn0BbD91-flr-sR9Fsfu1O51VkxrgTlcVFGuvqY4RDxx3VKWFTs7eYn5KwL85RJuteHBWt0kZJms2JhseVxR_BMg7QCW2Ace8-hqfMg3Ja1E-JjcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از غرق شدن کشتی حادثه دیده در خلیج‌فارس
🔹
بامداد امروز برخورد کشتی فله‌بر با یک شناور دیگر در شمال جزیره قشم، منجر به آب‌گرفتگی و تخلیهٔ اضطراری یکی از کشتی‌ها شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/671066" target="_blank">📅 20:17 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671065">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
غریب‌آبادی: باج‌گیری و ارعاب آشکار از سوی واشنگتن برای خفه‌کردن عدالت
معاون حقوقی و بین‌المللی وزارت امور خارجه:
🔹
واشنگتن برای حصارکشی دور مقامات و نظامیان رژیم آمریکا و اسرائیل، دولت‌های عضو دیوان کیفری بین‌المللی را به تحریم، لغو روادید و فشار سیاسی تهدید می‌کند تا همکاری با دیوان را متوقف کنند؛ باج‌گیری و ارعاب آشکار برای خفه‌کردن عدالت، پیش از رسیدن آن به متهمان آمریکایی-صهیونی.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/671065" target="_blank">📅 20:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671064">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
حمله دشمن به شهرستان دشتی خسارت جانی نداشت
فرماندار دشتی:
🔹
در پی نقض تعهد و تجاوز دشمن به کشور، حوالی ساعت ۱۳ امروز یک مقر نظامی در شهر خورموج مورد اصابت چندین پرتابه دشمن قرار گرفت؛ در این حملات خسارت جانی متوجه شهروندان نشده است.
#اخبار_بوشهر
در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/671064" target="_blank">📅 20:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671063">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
لیندزی گراهام، سناتور جمهوریخواه آمریکا به‌درک واصل شد| علت: بیماری کوتاه و ناگهانی! #خونخواهی #تقاص_خواهید_داد   #WillPayThePrice ⁩ #Trash
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/671063" target="_blank">📅 20:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671062">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رهبر شهید انقلاب🇮🇷</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cbQmOpJnYmJezkkEn6iax1J_7iQbAh4HUDIry2GultS_q53e6yYMp8Rn9n7TaLZMDDp9oNVputcxGYvSptslqW2HhHV8fMzLIFsv8xFPcelhQptatWCqLfsCmlqzlS8ctRa4UHmOGXdOhv5tr7h0FnVYEXxw8va3Xdrs7aqXhRwCSLjKYcbvKAWk3miyG6vRx01GYDaYesnCHTDel9bye7knyi8bKel8wC6B7eViScNCxALSH2rT6fR-0LPbV9EV9MJIZQ9RK0yq8Eh6t9D5Pdqchsi53NS9CLUqH-sWz5gMR0JmJ0xzSiBiRh1-VNUUGMQrph5tBwW_vTjJWPFqdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
توصیه‌ حضرت آیت‌الله العظمی خامنه‌ای رضوان‌الله‌علیه به قرائت قرآن و دعا برای پیروزی جبهه مقاومت
🔹️
رهبر شهید انقلاب اسلامی در پاسخ به سوالی، قرائت
سوره فتح
،
دعای ۱۴ صحیفه سجادیه
و
دعای توسل
را برای پیروزی جبهه مقاومت توصیه کرده بودند.
💻
Farsi.khamenei.ir</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/671062" target="_blank">📅 20:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671061">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
نیروگاه برق جزیرۀ کیش درپی حملات تروریستی آمریکا آسیب دید
شرکت مهندسی آب‌وبرق کیش:
🔹
در جریان حمله بامداد امروز سه‌شنبه آمریکا پرتابه‌ای در مجاورت سایت تولید آب و برق کیش منفجر شده و به‌دلیل نزدیکی محل انفجار به واحدهای تولید برق، برخی از پارامترهای فنی این واحدها دچار تغییر شده است.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/671061" target="_blank">📅 20:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671060">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
شعار علیه سازشگر و پزشکیان در مصلی تهران؛ صداوسیما صدای جمعیت را دو بار قطع کرد/ جماران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/671060" target="_blank">📅 20:02 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671059">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c285ace09d.mp4?token=D3AiiSoKAf2ve44zbtypvCFOG7q8o71VL3uNbnPZmY1EaNKZivoTuDCLxr23tHpg5OO01JqCbbhKjpSSG4SOn7n9_EG0W3sgfgW2bL5EkkWMybM6dE0SKvwuu36lwHGy9izEzmCEj0_Q-4HP-IB_MB5zP_0uaiwVvPcuNR4lO4is3euK5zNcIN2VwUzMN7xo8QwuKHKeESkzpiDNUH3RR9lU9WQ8sU6O5Juj7r9QNuUDMUag-aLkEeKmMPxCeMZ-f9JWZjNedOr-Smy5p3nOyqc_t7dSCDBvXc3eu7Pm5nS3uQx4p_snUGnuKRu361lTIYT_JkMjx926I9lxEirQcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c285ace09d.mp4?token=D3AiiSoKAf2ve44zbtypvCFOG7q8o71VL3uNbnPZmY1EaNKZivoTuDCLxr23tHpg5OO01JqCbbhKjpSSG4SOn7n9_EG0W3sgfgW2bL5EkkWMybM6dE0SKvwuu36lwHGy9izEzmCEj0_Q-4HP-IB_MB5zP_0uaiwVvPcuNR4lO4is3euK5zNcIN2VwUzMN7xo8QwuKHKeESkzpiDNUH3RR9lU9WQ8sU6O5Juj7r9QNuUDMUag-aLkEeKmMPxCeMZ-f9JWZjNedOr-Smy5p3nOyqc_t7dSCDBvXc3eu7Pm5nS3uQx4p_snUGnuKRu361lTIYT_JkMjx926I9lxEirQcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: حق ندارند در صداوسیما بین دولت و نیروهای مسلح
شکاف القاء کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/671059" target="_blank">📅 20:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671058">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7vfMcA67qKTMXYdUWkBQU1aTnLiFq4qg7fmEumFL4WzZwT7p9b0I4vb6k2rSgKi9d-nRqmNN9Yy610njNRo-ncSSUdnrcXQ2qNwpWlwVMyYKuSCR0Z81kqHv3_B3QGtNjfiN7jmLARlNQIOQYtI2h--c2o7EY2jBbeoOgxPJx_yD_K52Fa8Hnb3aY0oTfndQwoUOP0ZUYj5n4H_fTBzPfD8U2HyNR1zIvLPt200J0sshyEza6vu1Uutt7ypzziUTefAiV4JlInfuihsGFvDA2O64RvZ67Exs5ykltvI_szjX2oefox8YSHQ4fIXWpgSGhMAiHQUr22InGhlKTH5QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعضی تصمیم‌ها... فقط یک بار قیمت دارن
💎
طلای اقتصادی با اجرت از ۳٪
🏦
بانک طلا؛ خرید تدریجی، بدون سود و اجرت
🔄
تعویض طلای سالم با عیار ۷۵۰
👰
مرجع سرویس عروس با تنوع بالا
✨
بدون مالیات ارزش افزوده
📲
جدیدترین مدل‌ها
https://t.me/haghgo_gold
ادمین :
@haghgogold
_
__
آدرس شعبه ۱: ستارخان بین فلکه اول و دوم صادقیه پاساژ زرناب طبقه همکف پلاک ۳۲
شعبه ۲: فلکه اول صادقیه زیما مال طبقه B1 واحد۴
برای اطلاع از موجودی تماس بگیرید :
09924100036  ---  09924100039</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/671058" target="_blank">📅 20:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671057">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
استانداری هرمزگان: ساعت ۱۹ چند نقطه در جزیره قشم مورد اصابت پرتابه‌های آمریکا قرار گرفت.  #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/671057" target="_blank">📅 19:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671056">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
ادعای سگ‌زرد در دیدار با الزیدی: نیازی به حضور نظامی آمریکا در عراق نیست #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/671056" target="_blank">📅 19:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671055">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/epELrf4bBUZXhdwH06OoWq7HHBrolWAEpj8hxUo3nuMTCIcGjNPY_pCVtJAYRiAI-WBQiceUcvTH8zkL7yljXlGpElz8x00uzsBzcyMnaUt0upk-xkW6th4PQSxXOmdcTTg8OcMnWPRidXOTXwpbD7A_zMjO3PvL0J4J0DNl4KbKKI0ZIer0OFuB0EjRGdH_oDx_Ej_56ICiyNBS5VG2gwVNPV0mFoboipUQTepmJrxX_NmivNJcR46FGTeT0fKwL389sFkA7Sc1MG3MGjh0rbIFLKvp8b929Ve-osx9dXAqgcloDHbNqJ5sGz3GcTt-dX8TvZv94U-KJ-zspV5Hfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر ایرانی سالانه ۹۳ کیلوگرم ضایعات غذایی خانگی تولید می‌کند
🔹
مالدیو، عراق و پاکستان، بیشترین ضایعات غذایی خانگی به ازای هر نفر را در جهان دارند.
🔹
ایران با ۹۳ کیلوگرم در رتبه ۵۳ جهان قرار دارد و ضایعات غذایی آن از کشورهایی مانند چین، آمریکا، هند و روسیه بیشتر است.
🔹
کاهش ضایعات غذایی، علاوه بر صرفه‌جویی در هزینه خانوار، به حفظ منابع آب، انرژی و کاهش انتشار گازهای گلخانه‌ای کمک می‌کند.
@amarfact</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/671055" target="_blank">📅 19:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671054">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
سرنگونی پهپاد پیشرفته «وینگ‌لونگ ۲» سعودی در یمن
🔹
سخنگوی نیروهای مسلح یمن از هدف قرار گرفتن و سرنگونی یک فروند پهپاد جاسوسی متعلق به ائتلاف سعودی در آسمان استان «البیضاء» خبر داد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/671054" target="_blank">📅 19:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671053">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
صدای انفجار در اندیمشک شنیده شد/ صداوسیما
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_Khozestan</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/671053" target="_blank">📅 19:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671052">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
حملات جدید به کویت؛ صدای انفجارهای شدید و آژیر خطر به گوش می رسد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/671052" target="_blank">📅 19:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671051">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
ادعای سگ‌زرد در دیدار با الزیدی: نیازی به حضور نظامی آمریکا در عراق نیست #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/671051" target="_blank">📅 19:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671050">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
دود شرق تهران ناشی از آتش‌سوزی یک منزل قدیمی در خیابان دماوند است
سخنگوی آتش‌نشانی:
🔹
دودی که در بخش‌هایی از شرق پایتخت مشاهده شده، مربوط به آتش‌سوزی یک منزل قدیمی در محدوده خیابان دماوند است.
🔹
اطفای حریق در حال انجام است.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/671050" target="_blank">📅 19:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671049">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
دیدار نخست وزیر عراق با ترامپ
🔹
علی الزیدی، نخست وزیر عراق که به واشنگتن سفر کرده، در کاخ سفید مورد استقبال ترامپ قرار گرفت.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/671049" target="_blank">📅 19:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671048">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
صدای انفجار در قشم
🔹
صدای دست کم ۵ انفجار در جزیرهٔ قشم حوالی ساعت ۱۸:۴۵ شنیده شد. ماهیت انفجارها مشخص نیست.  #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/671048" target="_blank">📅 19:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671047">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i07g4P0Dy27NfslIgvpaAmLwaNqR95Dxpbsb_9GhrnSdy_7g_KbudiZOEul7Qkj-x5wU-qQazIql40LuqvM42NPupg7Xcnmv9Hztx1CChihrG7wyCdXeoMfIB9ftlxCIpcr5t0BkKj-xvgZ8yukYlaN53opDcFCdstG9f8rb9Jtjbd58YP1n2-lC7aK6tuTZiaprsUcHaMNnuBkd1EFWD4MXA7iEKkyTZN5TLSFuiVzYWDHEiDCRiMuJvGw8qjIq86dVjpXfgYRl-F79nqiSqMo9i2tQkj4UkpqdRmdQgR31-m-bjk5tPeKR6MUbw38G4p5rOutZf-w5LxN-lQocCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رامین رضاییان با کیف لوکس Hermès Birkin ۴٠ دیده شد
🔹
قیمت رسمی این کیف در بوتیک‌های هرمس حدود ۲۰,۵۰۰ دلار است و با نرخ فعلی ارز، ارزشی نزدیک به ۳ میلیارد و ۷۰۰ میلیون تومان دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/671047" target="_blank">📅 19:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671046">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c82c869464.mp4?token=DfCrcpkfketfUE1IQtMUttQ0O3A8iJz7Ul-FhntU0GKy8EPny4_92RD0dKlOIeVkAiTCeVI8Md0VwZd0JRDtLO14s8YnUcGOBZkch2mDeBZjaOyZVswoK0Hzb4RF9Kol4TA9NQr7yLHRvrOUnSpkRnDryCnctuGQ2_TNIJuEKzgmNyO5WRyK_S0N0UiuTOne-6xXzYtNzL06Dk_xNUsSW9ujuwI49wNOaQdFL2Zbft7px7XrTWR1a75p4pM9hY7GGncDEPGohU1-6n7m8v0PQvZePXNkaLjRBw_Ou3qMsfOsxQ-b5JQAItc2-FkOcbGvxbVHQdnQdMSKaAuqW8o_P7v-OPc6DzsuU8sbqXzWD5tzs7F6WQUNgfiWlZs4lpf6YA0m5oTtkBw_TksYfOQMzJIcjeyeaVwL-xcrKMPOYDosqGZ7Nf_ptU0YZeLnoSNX1ExHgU_tQSlyR8nXPxaZ7q8VorqNeMr1GbG-SOZStWI3wYlBrfkFcOrul0X4gtXb_TOtsrozGVvmvbzq_RButWR-hoB8vOIEw6ES3bdOS5cRzS1GlxErBu39SgQruN3wHq0ojdfS-mRSBRVyqqAUxbGBAmzS_sEBiXy6E8ETjjzzjY5jiTMIZ-NQtS7g7fp5SwddopV9ddmhTQPNnYwG9SyGvbLIrNAzzIE78wH6ffg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c82c869464.mp4?token=DfCrcpkfketfUE1IQtMUttQ0O3A8iJz7Ul-FhntU0GKy8EPny4_92RD0dKlOIeVkAiTCeVI8Md0VwZd0JRDtLO14s8YnUcGOBZkch2mDeBZjaOyZVswoK0Hzb4RF9Kol4TA9NQr7yLHRvrOUnSpkRnDryCnctuGQ2_TNIJuEKzgmNyO5WRyK_S0N0UiuTOne-6xXzYtNzL06Dk_xNUsSW9ujuwI49wNOaQdFL2Zbft7px7XrTWR1a75p4pM9hY7GGncDEPGohU1-6n7m8v0PQvZePXNkaLjRBw_Ou3qMsfOsxQ-b5JQAItc2-FkOcbGvxbVHQdnQdMSKaAuqW8o_P7v-OPc6DzsuU8sbqXzWD5tzs7F6WQUNgfiWlZs4lpf6YA0m5oTtkBw_TksYfOQMzJIcjeyeaVwL-xcrKMPOYDosqGZ7Nf_ptU0YZeLnoSNX1ExHgU_tQSlyR8nXPxaZ7q8VorqNeMr1GbG-SOZStWI3wYlBrfkFcOrul0X4gtXb_TOtsrozGVvmvbzq_RButWR-hoB8vOIEw6ES3bdOS5cRzS1GlxErBu39SgQruN3wHq0ojdfS-mRSBRVyqqAUxbGBAmzS_sEBiXy6E8ETjjzzjY5jiTMIZ-NQtS7g7fp5SwddopV9ddmhTQPNnYwG9SyGvbLIrNAzzIE78wH6ffg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیت‌الله سیدمصطفی خامنه‌ای: صبر در این مصیبت بزرگ هیچ منافاتی با انتقام و برخورد با اشرار عالم که در این جنایتهای بزرگ دست داشتند نخواهد داشت
#تقاص_خواهید_داد
#WillPayThePrice
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/671046" target="_blank">📅 19:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671045">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MHbRcXEGitrx7heEKdaPsK1Z1gAljSmSj3IFaYFAxo4gGA10UAxBFIt6EEv-YxAKG33h_XYE-QBRXK2Ih6ahRDXepOdAoMaskrwqrFs2n-DLEa0bFQg_N7o1VWTweg6K7tJOCvmj_XPEKAIFLAA8rBGCL6SaabajkwvUtQB12QJnPGN3GVOTtMuIS4nGboSIQTlP7Ot_o0sHEUYgRwGB-LF9S2KrrzcWqh3lIsCRMorV8-6f95JoTW1E4x-kRGcYztOP2ylZPlwflRPQOTSDicIRpqHAaRt8yIZ8raR6xFWZLOwlUXdFkzCidGv6U_AG1NCrAAYqpCeoqY9F2O4wtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
خريد و فروش طلا
صندوق بانك گردشگري
صندوق اندوخته آميتيس
صندوق درخشان آميتيس
‎روبیس با دریافت مجوزهای لازم بستری امن و قابل اعتماد برای سرمایه‌گذاری فراهم کرده است.‌
https://rubisinvest.ir</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/671045" target="_blank">📅 19:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671043">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/971cb6b758.mp4?token=iNEEOrTYgdW1c7jafq3m9RMq_-ASRCtA9CtCxtdlzxdkNppQwYetw8Zon0j3Ws-5aIKOxW4F2A3kV-HyOaV_TYK7vIB_cD_Jxt72FoRhI1n_GDPwJY7Sb9Zo0Ct9gWBwPXwVEhrx3nGKE4nUrGoTEqd1C3ukpkvw7hlg4xbG7_4p_fxJajOtcwXw9Wmit9JMci3_KgnrSwb5Aw-3eqNtQu08196lvc-vymfWFXgoZg0jBObI4IsjU4V4Is5v0xUBTf1xuYYcIyR7UsLmRe3Yw6JGqwnDC4Oqxzh9jPxn08QeBpEmc4r1Azph62aHhC0cSj7-sAvTGfpOxopbnrNDVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/971cb6b758.mp4?token=iNEEOrTYgdW1c7jafq3m9RMq_-ASRCtA9CtCxtdlzxdkNppQwYetw8Zon0j3Ws-5aIKOxW4F2A3kV-HyOaV_TYK7vIB_cD_Jxt72FoRhI1n_GDPwJY7Sb9Zo0Ct9gWBwPXwVEhrx3nGKE4nUrGoTEqd1C3ukpkvw7hlg4xbG7_4p_fxJajOtcwXw9Wmit9JMci3_KgnrSwb5Aw-3eqNtQu08196lvc-vymfWFXgoZg0jBObI4IsjU4V4Is5v0xUBTf1xuYYcIyR7UsLmRe3Yw6JGqwnDC4Oqxzh9jPxn08QeBpEmc4r1Azph62aHhC0cSj7-sAvTGfpOxopbnrNDVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور سردار قاآنی در مراسم بزرگداشت رهبر شهید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/671043" target="_blank">📅 19:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671042">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
آسیب به تأسیسات برق کیش در پی انفجار پرتابه‌ها؛ احتمال خاموشی موقت
شرکت آب و برق کیش:
🔹
در پی انفجار پرتابه‌ها در نزدیکی نیروگاه برق جزیره، برخی تجهیزات فنی آسیب دیده و در حال بررسی است.
🔹
ممکن است برای انجام تعمیرات، تعدادی از واحدهای تولید برق از مدار خارج شوند که در این صورت خاموشی‌های موقت و زمان‌بندی‌شده اعمال خواهد شد.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/671042" target="_blank">📅 19:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671041">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
اطلاعیه دولت: مراسم بزرگداشت امام شهید انقلاب که مقرر بود روز چهارشنبه از سوی دولت جمهوری اسلامی ایران برگزار شود، به روز یکشنبه ۲۸ تیرماه، ساعت ۱۰ صبح موکول شد
🔹
این مراسم به میزبانی قوای سه‌گانه کشور در مصلای بزرگ امام خمینی (ره) تهران برگزار خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/671041" target="_blank">📅 19:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671040">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
فعال شدن آژیرهای هشدار در کویت
🔹
منابع رسانه‌‌ای از حمله موشکی به اهداف آمریکایی در کویت و شنیده شدن صدای انفجارهای پی در پی خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/671040" target="_blank">📅 19:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671039">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
فعال شدن آژیرهای هشدار در کویت
🔹
منابع رسانه‌‌ای از حمله موشکی به اهداف آمریکایی در کویت و شنیده شدن صدای انفجارهای پی در پی خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/671039" target="_blank">📅 19:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671038">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
صدای انفجار در قشم
🔹
صدای دست کم ۵ انفجار در جزیرهٔ قشم حوالی ساعت ۱۸:۴۵ شنیده شد. ماهیت انفجارها مشخص نیست.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/671038" target="_blank">📅 19:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671037">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lYuM30mASMz2XDniZLrvk4waHekZUuRyFaCKF1Xztm16nYLjPI3jP3npQpwB1OsOpGljorVmalJk-SDmxqTMsKz-bpthh6aKik8ea6twRPF1el92LA2HfeAGK3HnqNt0RLwcVaoO8nMuKYnzv-SSh3mKmN2f_aXzh1XOf3ehd6BSitB2fApBkYfEPmC47kjPK5ICqgtm3AZWqBOvYkO8waN7SlgAI14o29ymazITsmB7cP99zaONJFpy6VuAe4bRlelqVIxYlL9o6qMVNv6x5xBUoFlGusM4p4ypw2RV61D3HvyswklMc6lKUHkLJAakEcKjh96JObCA3SRx6TIEWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/671037" target="_blank">📅 19:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671036">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
خبرهایی درباره حمله به نفتکش اماراتی در سواحل عمان
🔹
این منابع گفتند نفتکش «البهیه» امارات در ساحل عمان هدف قرار گرفت و نهاد امنیت دریایی این کشور خبر داد سه نفر از سرنشینان این نفتکش مفقود شده‌اند.
🔹
در حمله بعدی هم یک نفتکش مستقر در امارات متحده عربی با پرچم لیبریا هدف قرار گرفته است.
🔹
امنیت دریایی عمان خبر داد که ۲۱ نفر از سرنشینان این نفتکش هم موفق به خروج از آن شده‌ و نجات یافته‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/671036" target="_blank">📅 19:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671035">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4cv5DCJ-B0JoTXq0TQP42fFgkuMHCU7ccV2RIGVvomd04cUZxpBCgGNIC6q8CJDjQ50v_plVNovo_KO0G5b-DVSgKm6Gm8967ZMuucEW0DzktBJvRp84gidMdoRuvgsx64uUtIlOXzGBo0dukIJOjVZwIXdx4hB7OVul23Sj5Ml_Q_cmkIKwLEqg7_QzU5QSmIwEzR9LxeD7t6T5U4ZY-28Y5S_2RQiHKVIxc5uhz9fA-YNe7sQP2qauGLDVEzbdykPzO_EGuxw-NbKRybF0Oxz5lD3SfSNANI6Pr9HnjFo3_q4LFM2WoOfWbu9demuT4QR2uoLGjArdFdpjMaeGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: در تاریخ، جنوب ایران همواره نماد مقاومت در برابر استعمار و پاسداری از استقلال بوده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/671035" target="_blank">📅 18:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671034">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abecbc4c7d.mp4?token=OiB2Mxv2WUTAgy9n5C_g-muhsPZjREp0p4RrqePs8iAdsxUEzA_JAhg8X6_Och1guKC3mro4CUUF6QjKfCflY9Ok6LSvBkm49NLFcLaBzid_Upuy2gqs0zZNpbfAeUKwyGBf9JvmOXuXVtrWQ-mY5uyWuyuSLGGfrdZ2hCqIbTHQnr19EZeDnOu7Ta5DJ90VJez_5oGMST-TjKFtMWASwqMa_7J40cmQdjFeetGQ1yxdW7Sv8XkzakIDDWP-5QtJeK5qY7-NeAWfj8RY68nOdWNGoae-ShFNH2XMbmRlRIVCKaMm2Y9lGyYdwDQw66lhj1I2llg_raLjVeXWes88mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abecbc4c7d.mp4?token=OiB2Mxv2WUTAgy9n5C_g-muhsPZjREp0p4RrqePs8iAdsxUEzA_JAhg8X6_Och1guKC3mro4CUUF6QjKfCflY9Ok6LSvBkm49NLFcLaBzid_Upuy2gqs0zZNpbfAeUKwyGBf9JvmOXuXVtrWQ-mY5uyWuyuSLGGfrdZ2hCqIbTHQnr19EZeDnOu7Ta5DJ90VJez_5oGMST-TjKFtMWASwqMa_7J40cmQdjFeetGQ1yxdW7Sv8XkzakIDDWP-5QtJeK5qY7-NeAWfj8RY68nOdWNGoae-ShFNH2XMbmRlRIVCKaMm2Y9lGyYdwDQw66lhj1I2llg_raLjVeXWes88mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دیدار نخست وزیر عراق با ترامپ
🔹
علی الزیدی، نخست وزیر عراق که به واشنگتن سفر کرده، در کاخ سفید مورد استقبال ترامپ قرار گرفت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/671034" target="_blank">📅 18:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671033">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
پلیس فتا: احراز هویت خریداران در معاملات آنلاین الزامی است
پلیس فتا:
🔹
در هنگام ثبت آگهی در سایت‌های فروشگاهی و یا انجام هرگونه معاملات آنلاین، احراز هویت خریداران و واریز کنندگان وجوهات از سوی فروشندگان و یا ارائه دهنگان کالا و خدمات الزامی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/671033" target="_blank">📅 18:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671032">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45a05e1e5a.mp4?token=LjGBogCv-YbWUPOSVg-zfiPtWUP3yoIrundI3284BBpgrm6b6-63Rdr2gMzFh5RFoIy-M3peYrJk6ond28AHXfaio0w9DPJvDOU9fWCZzv-gRcspF1HfB8his6Gg8_XoTsGZKcu1UE6nd2m2PdhiEo7muh_nmzPiAOX208LiJdcs3Ir7S1_gOep5DOtoV7LLGtJIadoS0ABSG2UgvV-RADel_QDIKG2WSfasfqGpxnvblBw-vc9rGiDJ5WQeIBA5GunVsQp_c4W0Iqnw9fY9rnek-czRfVyRCWhF7q0hx1UKkrG3Y-qZxsAmSKJkybX_oWZ-la0smYoJgpvEJJc8yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45a05e1e5a.mp4?token=LjGBogCv-YbWUPOSVg-zfiPtWUP3yoIrundI3284BBpgrm6b6-63Rdr2gMzFh5RFoIy-M3peYrJk6ond28AHXfaio0w9DPJvDOU9fWCZzv-gRcspF1HfB8his6Gg8_XoTsGZKcu1UE6nd2m2PdhiEo7muh_nmzPiAOX208LiJdcs3Ir7S1_gOep5DOtoV7LLGtJIadoS0ABSG2UgvV-RADel_QDIKG2WSfasfqGpxnvblBw-vc9rGiDJ5WQeIBA5GunVsQp_c4W0Iqnw9fY9rnek-czRfVyRCWhF7q0hx1UKkrG3Y-qZxsAmSKJkybX_oWZ-la0smYoJgpvEJJc8yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«فکت‌چک» برنامه تلویزیون اینترنتی مدار برای کشف حقیقت از میان شایعات روز
🔹
تلویزیون اینترنتی مدار در روزهایی که اخبار و اطلاعات با سرعتی بی‌سابقه منتشر می‌شوند، با ساخت و پخش برنامه "فکت چک" راهی برای تشخیص واقعیت از شایعه باز کرده است.
🔹
«فکت‌چک» برنامه‌ای است برای بررسی و راستی‌آزمایی ادعاها، خبرها و روایت‌های مطرح شده در رسانه‌ها و فضای مجازی که در تلویزیون اینترنتی مدار تولید و پخش می‌شود.
🔹
در هر قسمت، با تکیه بر منابع معتبر، اسناد و شواهد، به دنبال کشف حقیقت و روشن شدن واقعیت‌های پشت پرده خواهیم بود.
اینجا مدار را تماشا کنید
👇
www.aparat.com/MADAAR_TV
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/671032" target="_blank">📅 18:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671031">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NceZuCnELZSvy6IFSDoLH0NzBrtdRr6ckqYQAGX8QU14idUhTEIy6v7mbx5TgFz3IDYOKnL81HUpktYaivCPqVY8hm2JCLw1ahlzSfAXLB3VBSQ_x-ZH7vUpDX89gH04qInc_xYxTCWrmYGf00tU80H8huV3cKNb-1w3DJv1MM3GS__OhPM8Df1DxCGf-xITpBblEIVsup76rilvcX1Ym1RWcb8jW-ORjXI0k9CQ7v-wSDxZjuZI7-p-oPDOi1sRsPdRP5uNmuXJRywQCjo5ymBdNdP44v6ocamtJOeUpLLJnX9-XUxTP21g9XRn5srz5fiqr2NIOgzWpRtnhEtTkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خوک هار از عوارض ۲۰% تنگه هرمز عقب نشینی کرد
🔹
«تصمیم گرفته‌ام که هزینهٔ ۲۰ درصدی بازپرداخت ایالات متحده را با قراردادهای تجاری و سرمایه‌گذاری جایگزین کنم که کشورهای مختلف حوزهٔ خلیج [فارس] در ایالات متحده انجام خواهند داد. آن سرمایه‌گذاری‌ها بسیار کلان (عظیم) خواهند بود.»
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/671031" target="_blank">📅 18:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671029">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Np0LMYcl7o1vrOTjtHiv-YJxQyrY9kms9SoDwqVTzWU426oIS0eWrVWUdLhJv4GK89VpG229k8DQrxx3ytaVpAxJHsbsC5VodWfrwsGMIdjn82pHrMpdHxVryLIvvQobt1Pqa0MJp0VD7kSk58WHoAqhO4Uo31hZrp0cAgcBT5LCjjT6ARnSSmuvFnpqWppYDpK0Uw1ji3bG8DUViZBLG0czR5Ff0SO6-Bnt79gNYX4rv5VdZcmiAozQqNTuSR4DKVKJLQd18tU_-LkMlM4EO7iTBw5foKilkesHwsxSY5RLmWdVCBNTHWe-fmXNwcq6hgKBSvs3SyGMHG_pIEO6iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاش خواهر زیدان، ایتالیا را ببخشد | نیمه‌نهایی؛ جایی که همه پیش‌بینی‌ها می‌میرند | فوتبال عادلانه نیست؛ راز جذابیتش هم همین است | فینال آرژانتین و فرانسه؛ تنها پایانی که جام را نجات می‌دهد | همه چیز درباره نیمه‌نهایی
🔹
حرف زدن از فوتبال آن هم در این‌ شب‌های داغ جام جهانی همصحبت خوب می‌خواهد. کسی که هم خاطره بصری بلندمدتی داشته باشد و هم پای ثابت فوتبال باشد و البته که فوتبال برایش فقط محدود به فوتبال نباشد!
در خبرفوری بخوانید و ببینید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3230294</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/671029" target="_blank">📅 18:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671028">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81e4352e2e.mp4?token=ifYine3JH5FMA2gOzAQLcUj708y7wF-OEqYYxqvKHBGMEOlbWFPIraNAldsr8OaSTxJo0h0ldm8Kg9TQl2XXDSHfZZ9-I-uzSD14BPXimjjSHFVFP5iMoEPI0Yhi3BxtEPJy9Q5ZwdZlqMX-77IFXRt_hO83qg040JWkIMp4KAoZgajT7E0MbF1MWMNhevG66-du3fkB5z9lCBLI1IDJc-kfIr7g__G1mDRewIf0qFBGIBcr8-pOG-10VZTg1Y-5Mkx5V4Kns5QCmu1NKe25vHdwwopWL7hfj01g8pp1pZGomyb6K4WkMtNOGAu0XNYjoZQS9krgp3fvQYtcCKUp5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81e4352e2e.mp4?token=ifYine3JH5FMA2gOzAQLcUj708y7wF-OEqYYxqvKHBGMEOlbWFPIraNAldsr8OaSTxJo0h0ldm8Kg9TQl2XXDSHfZZ9-I-uzSD14BPXimjjSHFVFP5iMoEPI0Yhi3BxtEPJy9Q5ZwdZlqMX-77IFXRt_hO83qg040JWkIMp4KAoZgajT7E0MbF1MWMNhevG66-du3fkB5z9lCBLI1IDJc-kfIr7g__G1mDRewIf0qFBGIBcr8-pOG-10VZTg1Y-5Mkx5V4Kns5QCmu1NKe25vHdwwopWL7hfj01g8pp1pZGomyb6K4WkMtNOGAu0XNYjoZQS9krgp3fvQYtcCKUp5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عارف قزوینی؛ شاعر وطن‌پرست دوره مشروطه
🔹
عارف قزوینی فقط یک شاعر یا خواننده نبود؛ صدای خشم، وطن‌پرستی و آزادی یک نسل بود. با تصنیف «از خون جوانان وطن» نامش در حافظه ایران ماندگار شد. هنرمندی سرکش و میهن‌دوست که با شعر و موسیقی علیه استبداد شاهنشاهی؛ از…</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/671028" target="_blank">📅 18:28 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671027">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dzx-UfkXroPRnd9DhxZyHp8gLwd4SJteQymfHMhPNtpmOWzVzyHNvmjzUEsQ98PgDNK8KNEr4LpCsdBBxW3XL48O-TsiinE5D0t4Y09i42KhGxHC2Wzq6PHeC-BIFvLs7Rd9BWOjqcMzBnmgMVIGSeDyKvvgTSCZkUL7KpdsYe4v0pjdCs4rpdWgjBZVQeL_xmD4EpP8K6xzXk_nK0R1m2TIZBFkR6-YSpKtcgP1QjCWsdVSS4CjGbH9oGsrOgwuDAqUfyDf2xmkGvFaiNWM7sG8Leg2pLBqpOL_o9VdGwiwBouVcxsU6k7iiztRHAWGpmgzJXfZPmbwsIUXTnXo3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اصطلاحاتی که بهتره وقتی میری کافه بدونی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/671027" target="_blank">📅 18:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671026">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
امکان تغییر محل آزمون پزشکی داوطلبان اهواز، بوشهر و بندرعباس
وزارت بهداشت:
🔹
داوطلبان حوزه‌های امتحانی اهواز، بوشهر و بندرعباس در صورت تمایل می‌توانند از ساعت ۱۴ روز سه‌شنبه ۲۳ تیرماه ۱۴۰۵ تا ساعت ۱۰ صبح روز چهارشنبه ۲۴ تیرماه، حوزه امتحانی خود را صرفا به شرحی که در ادامه آمده است تغییر دهند:
🔹
حوزه اهواز به لرستان
🔹
حوزه بوشهر به شیراز
🔹
حوزه بندرعباس به کرمان
🔹
آزمون فوق در حوزه‌های اهواز، بوشهر و بندرعباس همچنان برگزار خواهد شد و  این مهلت قابل تمدید نیست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/671026" target="_blank">📅 18:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671025">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
پاداش ورزشکاران مدال‌آور در بازی‌های آسیایی اعلام شد
کمیته ملی المپیک، پاداش پای سکوی ورزشکاران مدال‌آور در بیستمین دوره بازی‌های آسیایی را به این شرح اعلام کرد:
🔹
مدال طلا: ۳ میلیارد تومان
🔹
مدال نقره: یک میلیارد تومان
🔹
مدال برنز: ۴۰۰ میلیون تومان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/671025" target="_blank">📅 18:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671024">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10c0d02ae7.mp4?token=bunkqoLZlFwWRLHoc7lg2lkVfgSSnPScjVqS53ZJVpwMwo1YOhrLNSdJk1aJpT_wahUTn3S9e_evJWQIp00m-BAsmMWjhGhp2_tqCmJYIPhi3ZqVPAqGve9q3EeJ8WXSu3xRnr43l_6M6D_irtlkfxRnc2pelK47pHY-h-VIdI93EpEtjDQH0jlW4kRJxggZ_WDkdtXotmKRrkUVLjaQDQhdV77oE6qTX9YR3lYjMQLFten76pTQYgrI42euhzJnAEgg06x_FHOMZmDd4Lq6HmwqFDJuteVgT51GO1n2-9AlcLsuZQuURQ-gFxjnU7sKe52wbdB8_zNp8y1flGQULw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10c0d02ae7.mp4?token=bunkqoLZlFwWRLHoc7lg2lkVfgSSnPScjVqS53ZJVpwMwo1YOhrLNSdJk1aJpT_wahUTn3S9e_evJWQIp00m-BAsmMWjhGhp2_tqCmJYIPhi3ZqVPAqGve9q3EeJ8WXSu3xRnr43l_6M6D_irtlkfxRnc2pelK47pHY-h-VIdI93EpEtjDQH0jlW4kRJxggZ_WDkdtXotmKRrkUVLjaQDQhdV77oE6qTX9YR3lYjMQLFten76pTQYgrI42euhzJnAEgg06x_FHOMZmDd4Lq6HmwqFDJuteVgT51GO1n2-9AlcLsuZQuURQ-gFxjnU7sKe52wbdB8_zNp8y1flGQULw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور سفرای کشورهای خارجی در مراسم گرامیداشت رهبر شهید در مصلی امام خمینی(ره)
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/671024" target="_blank">📅 18:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671023">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MM-xJCq3T84lv9tOpIM8mkRZgsNT4yEeWoNzcrBbOwBf9CCJVMLInyseneC2-RDBMstog_So6M6NQayxYrT10SYWdptaXAwe1oA6IVM7_6-jvTPZdH4g8bqMh1FueEP9vPNg0ekj8hTYULqmPge6xBJeUDTiHzJH28lW8q9hw6QCE0VP69BNWJFC4gO9VLuFxD0wpoNLaXXitkYL1GbHHLAdQMf1Uxn4AEMz6V9_UkoRXy-QGSYdXu49BI0nJptqakepHTmSFEpwVdXyM4ufyD1NFWfTKYz7bDtl_H-N-sBY_VDPP_TKTatATQSzK5a8p5YbzX7YQRUt1P3TS63TfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا تنظیم‌گری بازار آنلاین طلا به سرانجام نمی‌رسد؟
🔹
خبرگزاری فارس نوشت: ماه‌هاست مقررات این بازار میان دولت و بانک مرکزی در رفت‌وآمد است. تازه‌ترین اختلاف نیز به تفاوت میان مصوبه هیئت وزیران و ضوابط اجرایی بانک مرکزی درباره نحوه نگهداری طلای کاربران بازمی‌گردد.
🔹
بازاری که میلیون‌ها ایرانی در آن سرمایه‌گذاری کرده‌اند، بیش از هر چیز به مقرراتی شفاف، پایدار و قابل پیش‌بینی نیاز دارد؛ نه ابهام و تغییرات مکرر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/671023" target="_blank">📅 18:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671022">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hl5yNTT7o9ZKJPwZCTLrTBmQg5t7rUJiGz8hcOyfs9t--xNhxpZfclvb_Ou_bJfc5AuuDR8FKBFq3EOtlFy4zzilT5DXRRvBVFITxl2ZNQfQ2K3nwo-lCQrutd74EcygLerABDNcxKhcyvwIS54_kgvYubuEsJOoyeP89vLBJFGlJ69TN8kmUG-YAzKE6MrS268blQV4EJY_D4zzmjYBn1AzRupWCRM3qJMSoeBf1-uaZLLzAWllGTnTex-AvqFjlm515Zi_LFWR-NmkWvoX0H3Osp2ZHQOKf967pe5f7Q-PUO3L5b-Hs871LSi9nGzTt-c0L0cMvIo7PIJAFyr5fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خوک زرد ری‌پست کرد: جزیره خارک رو تسخیر کنید!
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/671022" target="_blank">📅 18:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671021">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
بریتانیا طرح ترامپ برای دریافت عوارض از تنگه هرمز را رد کرد
🔹
دولت بریتانیا پس از ادعای ترامپ مبنی بر کنترل تنگه هرمز و دریافت عوارض از آن، امروز اعلام کرد موضع خود را مبنی بر اینکه تنگه هرمز باید «بدون عوارض یا هزینه» بازگشایی شود، تکرار کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/671021" target="_blank">📅 18:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671020">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b03e544f40.mp4?token=cjUxx2_DZaQYG8jzSwVWsGNkxuNR8YuPujaAWwBYIsPFyLjGRvsxH-e_h7M30Lh_M3lzND1sAZ7Tz7klemkV8W-31iMgTLRRvm3UDX6HQXDsmzFvsC3EJ1CedqEHQQptlY8xMY67o3rKSzsPzfXk7Y1evnudPmnaQ92-9ZqCxZgictisz2eunJw5pR3ntqB0UaUP0tvjSH4a0ZkYf6TINgk0CeM3YpRPy4psl3tFQFvoWfDGfiRZsVDmw_nnQHSjwwnsvsOv3cLH-kIJZnD8xCVI8vwuLp3xL5-Au13gNEWWkqUOIcTy6WVeOBaoaX5I3ZoQFLALRCRQfxqZ3N-qZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b03e544f40.mp4?token=cjUxx2_DZaQYG8jzSwVWsGNkxuNR8YuPujaAWwBYIsPFyLjGRvsxH-e_h7M30Lh_M3lzND1sAZ7Tz7klemkV8W-31iMgTLRRvm3UDX6HQXDsmzFvsC3EJ1CedqEHQQptlY8xMY67o3rKSzsPzfXk7Y1evnudPmnaQ92-9ZqCxZgictisz2eunJw5pR3ntqB0UaUP0tvjSH4a0ZkYf6TINgk0CeM3YpRPy4psl3tFQFvoWfDGfiRZsVDmw_nnQHSjwwnsvsOv3cLH-kIJZnD8xCVI8vwuLp3xL5-Au13gNEWWkqUOIcTy6WVeOBaoaX5I3ZoQFLALRCRQfxqZ3N-qZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شهادت سه عضو خانواده یک محیط‌بان هرمزگانی در حمله آمریکا به دکل محیط‌بانی حاجی‌آباد
🔹
صبح امروز در پی حمله آمریکا به دکل محیط‌بانی منطقه حاجی‌آباد در استان هرمزگان، سه عضو خانواده یکی از محیط‌بانان این منطقه به شهادت رسیدند.
🔹
بر اساس گزارش‌های منتشرشده، دو فرزند پسر این محیط‌بان به همراه عروس خانواده در جریان این حمله جان خود را از دست دادند.
@AkhbareFori</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/671020" target="_blank">📅 18:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671019">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
سازمان بازرسی آثار حمله سایبری به چهار بانک کشور را بررسی کرد
معاون نظارت و بازرسی امور اقتصادی سازمان بازرسی:
🔹
هدف اصلی سازمان در شرایط کنونی، کمک به بازگشت هرچه سریع‌تر ثبات به شبکه بانکی، رفع مشکلات ایجادشده برای مردم و پیشگیری از تکرار اختلالات ناشی از حمله سایبری است./ایسنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/671019" target="_blank">📅 18:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671018">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f592965c1.mp4?token=QteRQtzTLKZLlcH159ZZhanrwBUOGbDAeIdcDi_QBzqwjVzx1CV_RVNv8rlF4apRJo5EXDh_xmsBbL_lhJdvM22eR0qS_2mhdaR01DqH9ZY2xGedJglxVNGYK7qDCqYY8O75j3sbVRWpGdz9O8EuogeC23V1fjdG0fmhqiLozDxa8jRMtoLXrDU1y1ZDNc9-Y2MU872qtwHBH7N_fKi-9pnvM7vvd63p7EAkOL05Hh88jGC0YvaENRZyRUqcX1rM-XJIqDthEVAxId1Iw0lr3L1x4s7kCHorPCXKUAlS3TWWhSzfCI42zg1HHlsjzOUP8IbIysegp-4mQVBMtEHyvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f592965c1.mp4?token=QteRQtzTLKZLlcH159ZZhanrwBUOGbDAeIdcDi_QBzqwjVzx1CV_RVNv8rlF4apRJo5EXDh_xmsBbL_lhJdvM22eR0qS_2mhdaR01DqH9ZY2xGedJglxVNGYK7qDCqYY8O75j3sbVRWpGdz9O8EuogeC23V1fjdG0fmhqiLozDxa8jRMtoLXrDU1y1ZDNc9-Y2MU872qtwHBH7N_fKi-9pnvM7vvd63p7EAkOL05Hh88jGC0YvaENRZyRUqcX1rM-XJIqDthEVAxId1Iw0lr3L1x4s7kCHorPCXKUAlS3TWWhSzfCI42zg1HHlsjzOUP8IbIysegp-4mQVBMtEHyvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
قطعی برق؟ تاریکی دیگه دردسر نیست!
🔦
چراغ شارژی خورشیدی
تاشو با طراحی کاربردی، مناسب برای خانه، سفر، کمپینگ و مواقع اضطراری.
✨
ویژگی‌ها:
✅
شارژ با نور خورشید و USB
✅
طراحی تاشو و کم‌جا
✅
نوردهی قوی
✅
مناسب برای قطعی برق، خودرو، ویلا و طبیعت‌گردی
🔥
قیمت قبلی: 1,598,000 تومان
❌
💰
قیمت ویژه: 1,098,000 تومان
✅
⏳
این تخفیف برای مدت محدود فعال است.
🛒
برای مشاهده مشخصات و ثبت سفارش، روی لینک زیر کلیک کنید:
👇
👇
👇
https://memarket24.ir/product/brief/47540/180124/</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/671018" target="_blank">📅 18:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671017">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e44ec578b.mp4?token=LtxX-xfjnmhHNyrvHcQhubmsL9WsTjy_Zk_H2JsELfB9xRv0R1v3Yxlbcui2ak5ifkXECRwmNhN133C93zlbX1T7nMv7t119G_QX_J0yDcQRcb7pkzYh-Zvd5GH6KcE3IeMRyLaA70yqxQT_GYjJEOdpuVKkEpvGi2ETVkAJYmiBd64km3Q9NbhjwZaSqFF1a-r_r8xami7AXt1VuSG0x9r2UFkybJOPlhxCDu3OYvANTbVuBjgxl9ElQuYZ0BCcuD9AhIN2LhucIXDF0ryb3hKwdyAV_kxQty3ezq3eHx-y1Luoe86PGwZ9wQNEH-lujLfP-PY8xS59ZPLdnvbl9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e44ec578b.mp4?token=LtxX-xfjnmhHNyrvHcQhubmsL9WsTjy_Zk_H2JsELfB9xRv0R1v3Yxlbcui2ak5ifkXECRwmNhN133C93zlbX1T7nMv7t119G_QX_J0yDcQRcb7pkzYh-Zvd5GH6KcE3IeMRyLaA70yqxQT_GYjJEOdpuVKkEpvGi2ETVkAJYmiBd64km3Q9NbhjwZaSqFF1a-r_r8xami7AXt1VuSG0x9r2UFkybJOPlhxCDu3OYvANTbVuBjgxl9ElQuYZ0BCcuD9AhIN2LhucIXDF0ryb3hKwdyAV_kxQty3ezq3eHx-y1Luoe86PGwZ9wQNEH-lujLfP-PY8xS59ZPLdnvbl9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انهدام یک فروند پهپاد متخاصم با آتش پدافندی نداجا در بندرعباس
روابط عمومی ارتش:
🔹
بامداد امروز، یک فروند پهپاد متخاصم دشمن متجاوز آمریکایی، با رهگیری و شلیک موفق سامانه های پدافندی دلیرمردان نیروی دریایی ارتش، تحت شبکه یکپارچه پدافند هوایی کشور در بندرعباس، مورد اصابت قرار گرفت و منهدم شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/671017" target="_blank">📅 17:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671016">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a8ddd9019.mp4?token=VepxiCCcaNMefKjZfJXME8r3tbfKu1ed2W9j4Vht2IDm9_Egn_RiWV6Y6TK4EDHAD4NMp6ASgjwi4egkY0iwxph7_hbYYsqvtbGW31TnfosxwjfWq6qmC29wFDIYpzbWu6X-Krv4s8kv3R92tD9Y_0xDHWob9KNDeRIXnXziTdm2QHlIqgkgrYiOBDojq0FoWRibLnbUqyCcWtWcND2Kuf23QhHWlGT4KBZQBHwjT0wV0MKOrlbYnZYrznRTibYg87AR7RXscWGisb6OQ5jlF7RT_V0kaVLRpKKK_eyUbSuVggrEmZbVJI999Tn_26VLnbyCJWk4qxPl2uAeoj5hTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a8ddd9019.mp4?token=VepxiCCcaNMefKjZfJXME8r3tbfKu1ed2W9j4Vht2IDm9_Egn_RiWV6Y6TK4EDHAD4NMp6ASgjwi4egkY0iwxph7_hbYYsqvtbGW31TnfosxwjfWq6qmC29wFDIYpzbWu6X-Krv4s8kv3R92tD9Y_0xDHWob9KNDeRIXnXziTdm2QHlIqgkgrYiOBDojq0FoWRibLnbUqyCcWtWcND2Kuf23QhHWlGT4KBZQBHwjT0wV0MKOrlbYnZYrznRTibYg87AR7RXscWGisb6OQ5jlF7RT_V0kaVLRpKKK_eyUbSuVggrEmZbVJI999Tn_26VLnbyCJWk4qxPl2uAeoj5hTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک، تحلیلگر حوزۀ مقاومت: استراتژی چشم در برابر چشم دشمن را متوقف نخواهد کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/671016" target="_blank">📅 17:48 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
