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
<img src="https://cdn4.telesco.pe/file/iZsXwPdPZ052qUWAgpQndPbZKpmRboQsNroInN6az79fTNcIErNv3xGA-NW-N5ILa52Cv3B6I8hlnQDQIWJkX_6-3-yipmukXmguPF_4BjDLQPqwhE-L2t-bFo_i1r0vu4ZfAeYNfkbM2BHxiQrDLeGxLovVEndaNI_4XbpN2iMP87p-VOEF59p47tcWvZZf1peejuzab0rIbM9gEw4vAOc2NfgdcyhrYXUd8SmaTwDIBQCUR0ZGmoiWwg8W1AiLnhqDNR2iSD8wGQfkiVZ6rdIfGUC1Lbtef8_EcHUIyowv8DrqF9_UswhrIC-Ogw_Tt6aDIvF9x6-2b5VUGFy53Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.32M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-07 12:18:18</div>
<hr>

<div class="tg-post" id="msg-693913">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک اقتصادنوین</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RvNnI4hM2CNVwXs4eDYJK-gISabvm2OY8KL7DFL9xEdqHSxWTl4aDNo-oB7ocAQfjfobf9ac62CJyp5IaehmXha373zc-XaO0Xutg9eq6LZ7y5WmdROFeP3KPu7Erj0H6gcJevJnuQZNM2OAhYLUEB-2j0dQ2zJIuzsOCgHDg5TtMMzfw9tnrjmNEr-3w19siPhxTDxzNnvQFXXgho3uF7FNC4OG3eDo1aRzbhpMnznoUHjhYhOU9sPAMYQzr70pShKeT725tZspVx6grW06IsXn7i76f2uC6G_QZWqfkEDn2t8dxn8URwJ5Y_CH7Cz_nlzmwnXP1giai3Q4E6AItw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
«مهسا بهشتی» ورزشکار مورد حمایت بانک اقتصادنوین، در «ناگویا» تاریخ‌ساز شد
🔹
«مهسا بهشتی» ورزشکار مورد حمایت بانک اقتصادنوین و نماینده وزنه‌برداری ایران در بازی‌های آسیایی، صاحب مدال برنز شد.
🔻
اطلاعات بیشتر:
▫️
https://enbank.ir/s/mfaba86
☎️
02162740
🌐
www.enbank.ir</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/693913" target="_blank">📅 12:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693912">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97f7e668b9.mp4?token=rzHmHjt2IleazQ6JiPJ8Le6asO3AlKKavnf-KqHMJDOlBiRhpJ-Kc9itrpsHVefoJHMSaEI7pvMIsCLIhDjA0e00VzVrraz8f5npoZMgLn_07YjG0uHO1hXhkuoy0vt5ahAUQd_NAXTnq_5UQbM8ZxDOdzfKabvw1E0TWSkfeOkce_V6yLY35yxvuoj4gneB3N5VKURe27LqjVNmYMzW5gTy02IizH6ZhhOuQhUanC-BepHDa9JA_i1pcWXegVO8J-D0MNGuGLDgwvhoEUYe7N8rBtAuhpwn0sS42D7eMi8ij60OGcM8cMLe-n9pEy1i4nbMAG8G4ev5G3WCEY7BR5Ks9V-YvENeldVUL9FNl_3Ie-Rn1vcN3KtgFy4JxhH5WUcB766TPAJeIMVKN0IwnnpAoe-t4EueC01-amFzoAMN0mvr0z9LPc3Rt0lCDuu3v7XSiN86mELVm5s4fpvAbFhvUeObvinevCjrAOh0ry8auVeWQG1mDsFXG7gKZRTn8dTXQLuzGSIkTGeozfvfzBu16FqYMzEj6lnKyHQw2li4GZcXVK-MwsP5g5XePHw8LRqCL__avFub0hvZkEK-1pj_sljDa-3cEwQtHfdFKKnawHm3bDwgiq7EjQhRGFc6KaE27MoWpbpEOjJanpa0PbouLaGRy9hgwgThJeLHs_k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97f7e668b9.mp4?token=rzHmHjt2IleazQ6JiPJ8Le6asO3AlKKavnf-KqHMJDOlBiRhpJ-Kc9itrpsHVefoJHMSaEI7pvMIsCLIhDjA0e00VzVrraz8f5npoZMgLn_07YjG0uHO1hXhkuoy0vt5ahAUQd_NAXTnq_5UQbM8ZxDOdzfKabvw1E0TWSkfeOkce_V6yLY35yxvuoj4gneB3N5VKURe27LqjVNmYMzW5gTy02IizH6ZhhOuQhUanC-BepHDa9JA_i1pcWXegVO8J-D0MNGuGLDgwvhoEUYe7N8rBtAuhpwn0sS42D7eMi8ij60OGcM8cMLe-n9pEy1i4nbMAG8G4ev5G3WCEY7BR5Ks9V-YvENeldVUL9FNl_3Ie-Rn1vcN3KtgFy4JxhH5WUcB766TPAJeIMVKN0IwnnpAoe-t4EueC01-amFzoAMN0mvr0z9LPc3Rt0lCDuu3v7XSiN86mELVm5s4fpvAbFhvUeObvinevCjrAOh0ry8auVeWQG1mDsFXG7gKZRTn8dTXQLuzGSIkTGeozfvfzBu16FqYMzEj6lnKyHQw2li4GZcXVK-MwsP5g5XePHw8LRqCL__avFub0hvZkEK-1pj_sljDa-3cEwQtHfdFKKnawHm3bDwgiq7EjQhRGFc6KaE27MoWpbpEOjJanpa0PbouLaGRy9hgwgThJeLHs_k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئو وایرال شده از موتورسواری روی پل عابر پیاده در مشهد
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/akhbarefori/693912" target="_blank">📅 12:11 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693910">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/250aabb1fd.mp4?token=m__1G4Zwq9ZWwacMdeOcy-j45r92xUzo2itEeOFcZYo-xv0aRjXHh77Yq-1GTio1TMDTSKxiyiuBasOsV5xxznqH-SUVxrAfWDOhjZH6BkBh4g3hXztFIB_mKxLc4QRYgG6ylY6_2mbd6kre7EaR-dkwVTkKFc9hZXfDYoomht9382JuXnBAPHgZIrCMqN0brRH-uis3HgNHoerjAA5zDGEzJWazZzl-4LD0DRtpsfbcREQodMDICEL8EsDTKx8RhaMbmpsDvC_XRuiurYHf9HZU42m74DiDJR_MrceMyu_0Yt5ulU2dQ_Z1sL79ecYoHJqey3bsZGox9pWOyqdnTGy_I6vcvpben-LtC2kCbJJNnDLd8of9Cgl9-GgixO7MTSC6XjiFu47W94BEOaAfvLruLU_mvgqJfFz6FPicJqaRejN60xQNb4JfeQsBCixrrZEdfq1j5uK4BTfTgUfgJEivLkmgZSiss7BQOEMbeJm_jaxDpArtaUnNnvlzPki7pT8KDoqeGMaRelXq4iyhX4hKCmFws7URcEqYU3aJ3X5lgzKp94IeLF_WptP6Sh5aPpuvDm-IdCzCdC4Dmw_syx7FqeFuePm-WHoaE-LdO2Oqe9KPEEbPusrnT0Ao4jWLu2JCj2AmAiAaOvfvu-g8xpmO9Xh7kwGdcegH_6uc0vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/250aabb1fd.mp4?token=m__1G4Zwq9ZWwacMdeOcy-j45r92xUzo2itEeOFcZYo-xv0aRjXHh77Yq-1GTio1TMDTSKxiyiuBasOsV5xxznqH-SUVxrAfWDOhjZH6BkBh4g3hXztFIB_mKxLc4QRYgG6ylY6_2mbd6kre7EaR-dkwVTkKFc9hZXfDYoomht9382JuXnBAPHgZIrCMqN0brRH-uis3HgNHoerjAA5zDGEzJWazZzl-4LD0DRtpsfbcREQodMDICEL8EsDTKx8RhaMbmpsDvC_XRuiurYHf9HZU42m74DiDJR_MrceMyu_0Yt5ulU2dQ_Z1sL79ecYoHJqey3bsZGox9pWOyqdnTGy_I6vcvpben-LtC2kCbJJNnDLd8of9Cgl9-GgixO7MTSC6XjiFu47W94BEOaAfvLruLU_mvgqJfFz6FPicJqaRejN60xQNb4JfeQsBCixrrZEdfq1j5uK4BTfTgUfgJEivLkmgZSiss7BQOEMbeJm_jaxDpArtaUnNnvlzPki7pT8KDoqeGMaRelXq4iyhX4hKCmFws7URcEqYU3aJ3X5lgzKp94IeLF_WptP6Sh5aPpuvDm-IdCzCdC4Dmw_syx7FqeFuePm-WHoaE-LdO2Oqe9KPEEbPusrnT0Ao4jWLu2JCj2AmAiAaOvfvu-g8xpmO9Xh7kwGdcegH_6uc0vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر یک رابطه سالم با شریک عاطفی‌ات می‌خوای، این ۳ قانون رو حتما در مشاجره‌هاتون رعایت کن! #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/akhbarefori/693910" target="_blank">📅 12:02 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693909">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ca3fae826.mp4?token=WdFAfbfVd2OSilY0YqUDBF6UzONq1htHqo-0-mRUpKaGofO5Q5_nOMQuSvKV71s1Z_x_a3EZ_k0EBIILsq_7rNibMdK97nJ_CN9uiRuiPF0UxZPRRHCKdh9mcIQuLF9WtWhbv6Qdlo3cbhDK6xw7eKFd-Mf7Qf0epMTiltFsIhrZYiOK8XBpoznKTSzx5QyEnSCDrGhTUQpzUXjBxLGaYoF4oEMVe5l91vuOBmCgZu_lEHuc05BB6nRHOnNh4NNX4ZvY6N9yt3zEHJI7zWLU58y9Fg9RIenZ3cGhHA1QfHXyebjCIO495qcGDj12NeRG4ecL3DcvSJa3OJfwCXPaKIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ca3fae826.mp4?token=WdFAfbfVd2OSilY0YqUDBF6UzONq1htHqo-0-mRUpKaGofO5Q5_nOMQuSvKV71s1Z_x_a3EZ_k0EBIILsq_7rNibMdK97nJ_CN9uiRuiPF0UxZPRRHCKdh9mcIQuLF9WtWhbv6Qdlo3cbhDK6xw7eKFd-Mf7Qf0epMTiltFsIhrZYiOK8XBpoznKTSzx5QyEnSCDrGhTUQpzUXjBxLGaYoF4oEMVe5l91vuOBmCgZu_lEHuc05BB6nRHOnNh4NNX4ZvY6N9yt3zEHJI7zWLU58y9Fg9RIenZ3cGhHA1QfHXyebjCIO495qcGDj12NeRG4ecL3DcvSJa3OJfwCXPaKIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رونمایی AFC از توپ جام ملت‌های آسیا ۲۰۲۷ عربستان
🔹
جام ملت‌های آسیا ۲۰۲۷ از ۱۷ دی تا ۱۶ بهمن به میزبانی عربستان برگزار می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/akhbarefori/693909" target="_blank">📅 11:53 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693908">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
حذف ۴ صفر پول ملی به کجا رسید؟   سخنگوی دولت:
🔹
زمان‌بندی و نحوه اجرای حذف چهار صفر توسط بانک مرکزی در حال تدوين است‌ ولی این‌گونه اقدامات نياز به ثبات اجتماعی و اقتصادی دارد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/akhbarefori/693908" target="_blank">📅 11:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693905">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
جایزه ویژه یک عمر دستاورد هنری، جشنواره ترکیه‌ای آدانا به اصغر فرهادی
رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/693905" target="_blank">📅 11:42 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693903">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eRexU8hBTXZ8QebGU3lLDhrnXEs3hvdcL58ddphGeZS4jBjK7li-fnvuehSBblUFWlrDdxK27wjOvEGl-rATYZ6b4Tsn0ZghruVssM6W7AFbcxKGkugzYYQ-W9t8CNWwA0X35jBNXertllHFmTAPILeBTj7EN3Z5m9zlZlR9OZ9afN6p02jW2CKR9ZBCdRo_uoZZgWA8wNRullQh1ScLZHnH-x9q9F7kJeLPQfH-LeMECXQvJfz4J_o7nKQWLtZ2j9q5kvfUWj5gWBu77-4lWQhUUugvcA4YJYB9_ZQCo5qMkWLQQ0JTTXOKERoVgN7-8IkJr2RXeXor9CPVjFqXZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رویترز با انتشار تصویر دیوارنگاره میدان انقلاب: در ایران زندگی روزمره جریان دارد و ایران با صدای بلند دشمنی‌اش را با آمریکا به تصویر میکشد!
🔹
رویترز با انتشار تصویر دیوارنگاره جدید میدان انقلاب به یک بیلبورد عظیم ضدآمریکایی اشاره کرده است. گزارش رویتر تاکید میکند که در این تصویر با عبارت فارسیِ «لشکر شیطان در خلیج فارس غرق خواهد شد»، در بحبوحه افزایش تنش‌ها میان ایران و ایالات متحده، در میدان انقلاب رونمایی شد؛ در حالی که زندگی روزمره در تهران همچنان جریان دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/693903" target="_blank">📅 11:41 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693901">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e36f7b9ceb.mp4?token=MpGpneZyrZAsrlZ3sB94F5NR6MEgthQ1su7IAHhEdagRNJ2As1HFFO0-KmA9Eo95GL-kl-hfDaGJckM6t5XIDthEk4OrHMeKhXHDidbnr8wRUri56NHHOgKnXLk3nvagxUQe0y-3tW29_fUp_TTwSQzHPGkrUYIrs_dbobl3cqw0q6ZzaX7FPOcKsXY7kCklxoW_wPHpBMwfK1C4aaCyQj1AX8G3vAFd1SnLG_-bZV_3EnJXo_AXon9LJAiGKpzeGhcuQXsyuUFENRmiW8gVXB1LYVVn79R01plhagqdiXVzYQR4EkqPRNp-4F09a_tNoTUs7OqKN8UNNjgVHnvBoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e36f7b9ceb.mp4?token=MpGpneZyrZAsrlZ3sB94F5NR6MEgthQ1su7IAHhEdagRNJ2As1HFFO0-KmA9Eo95GL-kl-hfDaGJckM6t5XIDthEk4OrHMeKhXHDidbnr8wRUri56NHHOgKnXLk3nvagxUQe0y-3tW29_fUp_TTwSQzHPGkrUYIrs_dbobl3cqw0q6ZzaX7FPOcKsXY7kCklxoW_wPHpBMwfK1C4aaCyQj1AX8G3vAFd1SnLG_-bZV_3EnJXo_AXon9LJAiGKpzeGhcuQXsyuUFENRmiW8gVXB1LYVVn79R01plhagqdiXVzYQR4EkqPRNp-4F09a_tNoTUs7OqKN8UNNjgVHnvBoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دود مشاهده شده در مناطقی از تهران مربوط به آتش سوزی در ساختمان در حال ساخت در محله نیلوفر تهران است
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/693901" target="_blank">📅 11:28 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693900">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFnYOnZ3ZDixK-a9v9DxmUZ1-AERkUjqNamoluSMAIGj9QlqU_LKz0TEMrfzwiK91kK5xDVjy8YTUlHZNY8kEOiWSoz4o1DGlW9xXawxOZaK-GcdpUzb5u-7OScizevFvK_Fn-v8EL3ORdFzd9Vg5vmMS_f-s6cjLvHXo0F6YbgXCifKiN7ioS4yV5Zzd4rU8rYrFNPirV0_6J4f7HuQ-QSdj5X0L5kMK6aStOozfOGITAxYB4joMqpC3QMJsatBle_x6GfpKn-PaprN8SlKTe3gLd030-X-fTvGuoH1ML_zTWP7EpkEjyd0iUKLDGu27Tdkp1wuJlG0Yoc7hrF-SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کدام کشورها بیشترین استفاده را از ابزارهای هوش مصنوعی دارند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/693900" target="_blank">📅 11:12 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693898">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
سخنگوی سپاه: ادعای تلاش ایران برای ساخت سلاح هسته‌ای «دروغ قرن» است
سردار محبی:
🔹
آمریکا سال‌هاست مدعی است ایران در آستانه دستیابی به سلاح هسته‌ای است، در حالی که برجام نیز با هدف جلوگیری از دستیابی ایران به چنین سلاحی شکل گرفته بود.
🔹
دشمن خود می‌داند ایران به دنبال سلاح هسته‌ای نیست و مسئله اصلی هسته‌ای نیست بلکه «نابودی کشور پهناور ایران» است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/693898" target="_blank">📅 10:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693897">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZJUHZ9Jmxq5d7QWwLw4YIC-gINlDtMpPPEeS5U5v37otX6hRENa7PVhSG8nxiSeCi1IQkKPr3pUfoIWjW7-bU-AyEeGUt6yt2Kvh001Orbfx5mlg0ENoXzMssjyIhW4B6rAulGaOrtKuiOb3zw3jiUFnP4kyLmhDp1YFbnh7IaB0Jd2Mpb8e_hoNWsTsV_5BblYqaRZmQfBBLI2pUjbSBchGHrS7xbUe6Nz3wJMf7aiYWieBA2ZNOMLHbXnmw9b_FMx3iBZMihNXTlxrHAT0UhUyPAIUJ7rpl4RLuE6TUanRDPu3bnU7_r-M0jpEt4ePBm5TML3Kgku2C602omHPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مفت‌خورین عقب افتاده؛ چه چیزی باعث شد آمریکا از جانفدا تقلید کند؟
🔹
فراگیری جانفدا و عمومی شدن موضوع جنگ به نحوی موثر بوده که حالا آمریکایی ها درحال تقلید از این پویش هستند. اندیشکده های آمریکایی قدرت نمایی جانفدا را به عنوان عنصر تاب‌آوری ملی ایران و علت اصلی پیروزی ایران در نبردهای پیش رو می‌دانند.
🔹
خود وزیر جنایتکار آمریکا پای کار پویش «مرا بفرست» آمده و آمریکایی ها را ترغیب می‌کند تا توانمندی بدنی خود را برای حضور در جنگ با ایران بالا ببرند.
🔹
ایده درخشان جانفدا موجب حیرت رئیس جمهور روسیه هم شده بود و حالا عملیاتی شدن جانفدایان ایران در گروه های مردمی موجب ترس بیشتر جنایتکاران آمریکا شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/693897" target="_blank">📅 10:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693896">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
حذف ۴ صفر پول وارد فاز اجرا شد
🔹
بانک مرکزی پیش‌نویس آیین‌نامه حذف چهار صفر از پول ملی را تصویب کرد و اجرای طرح پس از تأیید دولت آغاز می‌شود.
🔹
زمان آغاز دوره گذار حداقل چهار ماه قبل از شروع به صورت عمومی اطلاع رسانی می شود و در دوره گذار هر دو واحد پولی…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/693896" target="_blank">📅 10:44 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693895">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9404ae77d3.mp4?token=NQMuCOrkAediu75ZMn6sqxe_Y_DrRPKwxfloBZDX3k_IqgVUSbz7HwMBnoKpoqdJqLct7hx46tyftOqaHnYJaQDKRbzcioqQztEmuxHe9P4vSm0SBfV0fKqXp8iCuAPw9xO6BIZzkDsk1CxI1THN7i6SKNAnRA3n-uHYMoPSic8uCxHrlZq00q0DGClvAJcXIl-SSsp-Cvr5ZqsVuW8phCfVbkLAu0QbXio7SjvgEZ8oIImQF03zeNmmAcYB3zA3wFazRFeDzGNJlSSPmdpnneDHmIUftVXEcGV91OKVChapnNjYVcHqgrteEH0qt-yDtJn76SbpfB3FOi3aw2kn8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9404ae77d3.mp4?token=NQMuCOrkAediu75ZMn6sqxe_Y_DrRPKwxfloBZDX3k_IqgVUSbz7HwMBnoKpoqdJqLct7hx46tyftOqaHnYJaQDKRbzcioqQztEmuxHe9P4vSm0SBfV0fKqXp8iCuAPw9xO6BIZzkDsk1CxI1THN7i6SKNAnRA3n-uHYMoPSic8uCxHrlZq00q0DGClvAJcXIl-SSsp-Cvr5ZqsVuW8phCfVbkLAu0QbXio7SjvgEZ8oIImQF03zeNmmAcYB3zA3wFazRFeDzGNJlSSPmdpnneDHmIUftVXEcGV91OKVChapnNjYVcHqgrteEH0qt-yDtJn76SbpfB3FOi3aw2kn8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس سازمان برنامه و بودجه: افراد تحت پوشش کمیته امداد، بهزیستی و افرادی که استحقاق دریافت کالابرگ با مبلغ بیشتر را داشته باشند، بدون اقدام خاصی کالابرگشان افزایش می‌یابد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/693895" target="_blank">📅 10:35 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693894">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
سخنگوی دولت: از جنگ نمی‌ترسيم و از مذاکره نمی‌گریزیم
🔹
۸۵ درصد از مواد غذایی ما وابسته‌ به داخل است؛داروهایی که به دلیل تحريم در کشور نبود، از ۶۴ قلم به ۳۲ قلم رسيده است.،
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/693894" target="_blank">📅 10:31 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693893">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zv36829b5zTFVFi79ZyPI-P9wwkWXaYxxrpjfTkcHi86dEAE96JdUc2D7h9UE7f7sV_8zz39AaP7pDpB0QaGUI2uoPRr07vTBUBkt6ru9bmBgDyHEDRsA2BTyz_kIncA7zfrCI6ZBFSJsW-3aDdUMhYSOwFkhpPJLV-L9Qx2TkpBhpEBiZUsbV-YtPRG-E6YaAeASVqWiMLYSChIK6NEphpKSwI5QUgCpEv-QmhbyXJgCtKcd5rSD9peTxbmfC-Oo7CwTXE4KslsXk5VYy51SdOJysOr0gsgsU-gdLO_96V1DqcQ0w9H8N6XQbOjerZVrc37G0rYXdsul8PXSje_3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترور فرمانده تیپ شمال غزه در گردان‌های قسام
🔹
نخست‌وزیر و وزیر جنگ رژیم صهیونیستی در بیانیه‌ای مشترک مدعی ترور فرمانده تیپ شمال غزه در گردان‌های قسام شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/693893" target="_blank">📅 10:27 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693892">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
سخنگوی دولت: از جنگ نمی‌ترسيم و از مذاکره نمی‌گریزیم
🔹
۸۵ درصد از مواد غذایی ما وابسته‌ به داخل است؛داروهایی که به دلیل تحريم در کشور نبود، از ۶۴ قلم به ۳۲ قلم رسيده است.،
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/693892" target="_blank">📅 10:21 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693891">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
ادعای تتر: از ابتدای ۲۰۲۶ حدود ۵۵۰ میلیون دلار USDT در کیف‌پول‌های مرتبط با ایران و شبکه‌های تحریمی را مسدود کرده است
🔹
به گفته این شرکت، این اقدام با اطلاعات وزارت خزانه‌داری آمریکا و برای مقابله با دور زدن تحریم‌ها انجام شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/693891" target="_blank">📅 10:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693890">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9abd452db3.mp4?token=oxbfNF6a8Mkk09FscazCD7KXbX52wNEndAVM15wHcS6J3GsiKOHp33SN51sthAt33vgfRYAu3mP8WPpNnR4h2IsnV0EEYBW3eoxuyqP-eHagNfwJprd9MXKDgSkmRyQXL5587CN5SZuT-XG-8IFKyO50xWg_cnJtI06P76ZoSRsU-Chs6THM9AGtvWE5uK_kSkUAW2L0egTJErow1ztW0Ac6eCzhVwLkCQwVke3WOcZt1dk5iVSNXBWA95x92vb0h4_DNFI5rMznNsK0PI23CISLgXWwtuXEhWVQ9_SIbkfbHLw27BK5qyTG8y6kfrL0mKY6vjWy93dBDjaL8sV43F5jVQOFo78PcBP1QZqi8FR8f-7hQq94GFAExz5imkdojt_aioeeIkYs7K6qOpkv0NOhxTKx8zI_ZPgwxjOHIzfYXsaJb0A4ssjO_JnCJXyc027K-JfoUEB8fr7vW5mYA4765G6MBdlWZUEvzrVusuWcP5g9q6p41Ik9HeCYObnJB3lZeHMpOZwGerjk3RfT6mHP1WZefHHInVQAt-UsWuhF_HI3ejmOpNKOQYlf_S-zoZNkv6hpx3RZMdMlZhQZZzE3WY8AlGV2H8ur2c4awLO_PccpHiyCnZnEGBGGIeFBDJrWpNzHtG-KoAVIYlTabokmTW_7RNhOB6MwQrnlK2M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9abd452db3.mp4?token=oxbfNF6a8Mkk09FscazCD7KXbX52wNEndAVM15wHcS6J3GsiKOHp33SN51sthAt33vgfRYAu3mP8WPpNnR4h2IsnV0EEYBW3eoxuyqP-eHagNfwJprd9MXKDgSkmRyQXL5587CN5SZuT-XG-8IFKyO50xWg_cnJtI06P76ZoSRsU-Chs6THM9AGtvWE5uK_kSkUAW2L0egTJErow1ztW0Ac6eCzhVwLkCQwVke3WOcZt1dk5iVSNXBWA95x92vb0h4_DNFI5rMznNsK0PI23CISLgXWwtuXEhWVQ9_SIbkfbHLw27BK5qyTG8y6kfrL0mKY6vjWy93dBDjaL8sV43F5jVQOFo78PcBP1QZqi8FR8f-7hQq94GFAExz5imkdojt_aioeeIkYs7K6qOpkv0NOhxTKx8zI_ZPgwxjOHIzfYXsaJb0A4ssjO_JnCJXyc027K-JfoUEB8fr7vW5mYA4765G6MBdlWZUEvzrVusuWcP5g9q6p41Ik9HeCYObnJB3lZeHMpOZwGerjk3RfT6mHP1WZefHHInVQAt-UsWuhF_HI3ejmOpNKOQYlf_S-zoZNkv6hpx3RZMdMlZhQZZzE3WY8AlGV2H8ur2c4awLO_PccpHiyCnZnEGBGGIeFBDJrWpNzHtG-KoAVIYlTabokmTW_7RNhOB6MwQrnlK2M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئو پربازدید از دزدی خانوادگی در یکی از خیابان‌های اصفهان
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/693890" target="_blank">📅 10:19 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693889">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
کارت زرد مجلس به خانم وزیر
🔹
نمایندگان در جلسۀ امروز مجلس از پاسخ‌های وزیر راه و شهرسازی قانع شدند و به فرزانه صادق کارت زرد دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/693889" target="_blank">📅 10:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693888">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aac48b4cd7.mp4?token=XWkqfL6A_ET45k04xS9qne0U01FHUnuNUPW-oevigeCjjd6SWjEXnlh6V0Q4hNmUp3OotMpNZqk9FG-oiFJuagks36Am966D7VNKpaE7pUkhFzWbhBNss3UyXozOMNMc9VRx1MRC-xGVacg5tdHT-pikK8GeXd-lB0aKcLlH9lPxCWTARyDb_LK5WSvFTv1boDCpo2HlqJNN2AU5L7r6g6IU8pPmgRbZ6DbuvyvwUPbwqdfCTxwWHckrau8tp2cio-3G1jwkIJ06CT-oz9WGEX-gYO2h_NVumrXKdgkqpAT99wUQMqwRVK5sEXcdLSwMACnHl4FNowvrr8SsQaP7Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aac48b4cd7.mp4?token=XWkqfL6A_ET45k04xS9qne0U01FHUnuNUPW-oevigeCjjd6SWjEXnlh6V0Q4hNmUp3OotMpNZqk9FG-oiFJuagks36Am966D7VNKpaE7pUkhFzWbhBNss3UyXozOMNMc9VRx1MRC-xGVacg5tdHT-pikK8GeXd-lB0aKcLlH9lPxCWTARyDb_LK5WSvFTv1boDCpo2HlqJNN2AU5L7r6g6IU8pPmgRbZ6DbuvyvwUPbwqdfCTxwWHckrau8tp2cio-3G1jwkIJ06CT-oz9WGEX-gYO2h_NVumrXKdgkqpAT99wUQMqwRVK5sEXcdLSwMACnHl4FNowvrr8SsQaP7Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگه عاشق سیب‌زمینی و پنیر هستی، این هش‌براون‌های طلایی و فوق‌العاده ترد رو حتماً امتحان کن!  مواد لازم:
🔹
۸ تا ۹ عدد سیب‌زمینی متوسط زِست
🔹
۵ قاشق غذاخوری نشاسته ذرت
🔹
۱۱۵ گرم پنیر چدار رنده‌شده
🔹
نمک به مقدار لازم
🔹
۱ قاشق چای‌خوری فلفل سیاه
🔹
۱ و نیم قاشق چای‌خوری…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/693888" target="_blank">📅 10:05 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693887">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tPrEBxCT733MspGTI7gCjslmbUTsqfd9swUPkDNYC0c25MttX94yJsQyCj5l4cPPdedbfkFMz-ydVN6lFeQ1bHLTd1tyqoT46sDHa02U4tA7ogJdOCgXbu9cgYRlCbRF-AWmsHTzue7LxP2fLe4F6DHDB3wrDExylHHQ5QnG3PWfA-82usd7CQ8JeWFBSyzG2uXw61fF-xMVb3SZ4W6TAtIynGwd29NPs5gomHqRQXm2zMm_5ZFQbDdhfik0HfefkTTiKfK07E-FpYMuJPUSaF0KGu7z3HRuQr3wXb-ZfjcE21o0Vu34TwdHgh1MAiXTw4zZq-M19L7aPbeHsQ3_DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت تتر از ۲۵۰ هزار تومان عبور کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/693887" target="_blank">📅 10:00 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693886">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
آغاز دومین مرحله پرداخت وام فوری ۱۵۰ میلیونی بازنشستگان کشور
🔹
دومین مرحله پرداخت وام فوری ۱۵۰ میلیون تومانی ویژه بازنشستگان و مستمری‌بگیران تأمین اجتماعی آغاز شد.
🔹
بر اساس دستورالعمل اعلامی، این تسهیلات بدون نیاز به ارائه چک یا ضامن ،بازپرداخت یک‌ساله و اعتبار آن در کمتر از یک‌روز کاری پرداخت می‌شود.
🔹
فرآیند ثبت درخواست و ارائه مدارک به‌صورت غیرحضوری انجام شده و متقاضیان برای ثبت درخواست نیازی به مراجعه به بانک ندارند.
🔹
جهت اطلاع از شرایط و ثبت درخواست، با کارشناسان از طریق شماره 02191551808 در ارتباط باشید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/693886" target="_blank">📅 09:58 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693885">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
قالیباف خطاب به ترامپ: «بچرخ تا بچرخیم!»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/693885" target="_blank">📅 09:56 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693884">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
ادعای فاکس‌نیوز: اسرائیل برای حمله دوباره به ایران در آماده‌باش است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/693884" target="_blank">📅 09:55 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693882">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
قالیباف خطاب به ترامپ: «بچرخ تا بچرخیم!»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/693882" target="_blank">📅 09:45 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693881">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
هشدار؛ مراقب کلاهبرداری با «عکس یادگاری» باشید
🔹
«این عکس قدیمی‌مونه، ببین»؛ پیامی ساده که ممکن است پشت آن یک لینک یا فایل آلوده پنهان شده باشد. کلاهبرداران با سوءاستفاده از اعتماد کاربران، لینک را در پیام‌رسان‌ها منتشر می‌کنند و با آلوده‌کردن گوشی یا گرفتن دسترسی‌های حساس، مسیر سرقت اطلاعات و پول را باز می‌کنند.
🔹
ماجرا اما به یک حساب ختم نمی‌شود؛ وجوه سرقتی ممکن است در چند حساب جابه‌جا شود و حتی پای فروشندگان و صاحبان حساب‌های بانکی را به پرونده باز کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/693881" target="_blank">📅 09:43 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693880">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
عراقچی نیویورک را پس از رایزنی‌های فشرده دیپلماتیک ترک کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/693880" target="_blank">📅 09:37 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693879">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XAbGcSVlCmMJ1hoxZrz2u_EyFgvrQ-9qsVDnCQVW3MKZNaoPsTS_LjxjUFdZdh84TvPiS_UdIuUVAKzhNJBJUkUSdn1tKFp2cIP088SXEDRgL8JjOdSc_kV4FqX6lvlmMkuU25D2MCNC5bd4cuxJnNCUHGm4rllTdwBx0rj_bSK8LHmbeRZgxI5RjT1lbCFlZ45Om9-2Kr0hSNX8hbb8H8YHJhf36XDjrXFN_13zQ3TXdWrHn_5BOf3EouaJxq2EARXcNMHc19c7FOWXZTy6hatXKrnTeK4oeILw2CYA4EDfpdOY-93Vex1WBVKxS6LZHL_Tk0uM9suJGJMSr2SmvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار پلیس فتا درباره «دعوت‌نامه عروسی» جعلی
⁣
معاون فرهنگی و اجتماعی پلیس فتا فراجا:
🔹
کلاهبرداران بوسیله شگرد جدیدی با ارسال فایل‌های APK تحت عنوان «کارت دعوت عروسی» کاربران را به نصب بدافزارهای جاسوسی ترغیب می‌کنند. کاربران عزیز باید بدانند که نصب این فایل‌ها، تلفن‌های همراه آنان را آلوده به بدافزارهای جاسوسی می کند./ مهر
⁣
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/693879" target="_blank">📅 09:35 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693878">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5HwqvH7s9Nv_c0MtlERPt4dN914oDrsTYmyjdtFd2zOgF_cwVr7psVOwzTff-tZ9fQjDkmF-jYQvJRpJ-LDzPiLUZ3LkVTPJn54_5zlBJT9yttYiw5lyxcmMsp3LnIzFdr7mWKe8xo_e1pmhNHABOurbQJA1dNtKRpc6xwhXKNag46LLKW8NvI0pQ-sP1mYstvVn-Pp_guY9NKXVTaRFU3ZDYP8qhr7mE1tH5fGr4uHgp0w7e4aEKDs1_0ttXpIHhDrCERmjHQd9W8stRP3Ais8i-7kJ737WoJM-jNdiSsxTY2JTUS-wcPsIosPYNXo-W00I8dYAvGljioRP3kY7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گزافه‌گویی وزیر دولت امارات: امارات خواستار پیگیری اشغال جزایر سه‌گانه تنب بزرگ، تنب کوچک و ابوموسی توسط ایران است!
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/693878" target="_blank">📅 09:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693877">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
انفجار کشتی در تنگه هرمز
🔹
شرکت امنیت دریایی «امبری» اعلام کرد یک کشتی تجاری هنگام عبور از مسیر جنوبی تنگهٔ هرمز، در شمال «خصب» عمان هدف اصابت قرار گرفته و دچار آتش‌سوزی شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/693877" target="_blank">📅 09:29 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693876">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
بیش از یک میلیون دوز دیگر واکسن آنفلوانزا توزیع می‌شود
علیرضا چیذری، رئیس انجمن صنفی تولید، تأمین، توزیع و صادرکنندگان تجهیزات پزشکی و دارویی در
#گفتگو
با خبرفوری:
🔹
سال گذشته تولید داخلی واکسن آنفلوانزا داشتیم اما نمی‌دانیم چه دلیلی باعث شد تولید داخلی ادامه پیدا نکند.
🔹
در دو روز گذشته توزیع حدود ۲۵۰ هزار دوز واکسن آنفلوانزا آغاز شده و همچنین بیش از یک میلیون دوز دیگر توزیع می‌شود.
🔹
در روزهای اول تلاش می‌شود توزیع با توجه به افراد دارای معلولیت جسمی و حرکتی، سالمندان، کادر درمان و افراد دارای بیماری‌های خاص انجام شود و در روزهای آینده و با توجه به حجم واردات، دسترسی مردم به واکسن بیشتر خواهد شد.
🔹
همان‌گونه که مردم از واکسن کووید سینوفارم استفاده کردند، درباره واکسن آنفلوانزای این شرکت نیز نگرانی خاصی وجود ندارد و واکسن‌هایی که از مسیر قانونی وارد کشور می‌شوند، تحت استانداردهای دارویی و پزشکی قرار دارند.
@TV_Fori</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/693876" target="_blank">📅 09:23 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693875">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
اخبار منتشر شده در مورد صدور مجوز پرواز برای شرکت‌های هواپیمایی ایرانی به فرودگاه‌های عراق صحت ندارد
🔹
تا این لحظه مراجع ذیربط در عراق تنها با از سرگیری پروازهای شرکت هواپیمایی العراقیه عراق به ایران موافقت کرده‌اند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/693875" target="_blank">📅 09:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693874">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
ستاد دیه: پول‌ مفسدان اقتصادی برای آزادی زندانیان را نمی‌پذیریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/693874" target="_blank">📅 09:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693870">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DxwStS0ONotiRYCjf9ryZBvM91cIKKuHe5QJKG51xsj5jCEUMnQvArek9EEj0WfQLgNsl1tFCiEdInTx55cDbksNMy6Qi0CkHpG6dcAYG27aYFU8jHdqXmb5J8pNm5teNpLUCJ4rvNqhW2HixUyPOCmGtwFP4FoLlbm9wkUERKHL3q79W0VIJEMM9RPYlB8uj4oF7pS55_oMmZjVKmJBn2ecjCBjuf_NbrmOwxFGvRwVYGY-qBQMTyHmgLAEn2OcnkiOSmC6v-uJMUJhV-BKDEaxeLYPQXGjA9K-ZCd7E2SSz99-G8Z9LOlzOhAT0GOES4v56Pt3jkA5y11BggotOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pT7kbcLttPj4bJzNpoEq_k2-BDaFdydAlVL31JptlGqcnOb7MB1vRx9xv4foCT5qfwoHeRAH7dNb5aC6AIb_f2PoQ9fP4obuGiO0I5jj-vh_ltrjtOKCyugeQxNyk-rO5Bile_YXFm5Znyv0w4dsP4gEmCfbpozQukKSps0l3ZppI1WN2yhs8zP7GNcrQY6FB_5NgC0dCx84DQgRO-_2AKzespMh-NPR0grtSpfjy9C-BFCoeK6pK16BkrvO4EQ25i33OGH1zIt6JQZE6-orIAL3ikz3yRh1sncBFRwVaqMekkAT0F4Dh_qLGOiy4mxRCzHz4LaEZEtEP0HXOIt7aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dHURRu7yM_8CrG2K3OT_MaCMpFgyXGYZnOtRPfQJMUie6SEzPsQqbm2SVyVtTB6Y3UZ6BzPYdz8vCJkFX1YApslbi0BoJCIbbmQmb4nIMOm29RThVgsP7e4fbMZLJcwyvtQMZsUQljKPufv0-VH2gLHeBH5mSbAbS4fFcNAX2rQf-HeY2OSVk9ZdG7Wpkw3kE38EgWlqyRYu6PNt7Vlb_PWAtLDwwpl7Ctpb5N_Jk54e7oNE-CbUZzEAnZBa00bnxlKR2nkZwQ4yE7IocWDQkFrLhJbwm3vvS__45Yjehx0Hr0DHtcCqQUiKkGDOJ_YpgmhJdgxG_apKMSP6jBDfVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Npnb4klQVw4jVq4Zoqtjxw1yHr2Gb7hPM7gHkR8l9aaHyPoI-qXGxNmO50RRGAhwBwadzeaGELB5fNjAWKtia06KDwgVYM2F9_E7Hvuxw6EZph0phkpgbAPRmOI9YOB6qNU8IoQ9ji0IpEiScsn7a-wf9wQlnTSsn2r9AzVTDVMukwtMLDqgqqGuFyBX42_odlZUurUXw0wdtkwm6Zc2uGsorHvwTQja83DaM8TN-c5yctEIoscIYfCPEyL9KtslKAUY4GhGGdN0jRWuIJGyMNpLIGTmzHUisSG367ZaBukkB966n66Wg7oxGRR3v3voQAjI7n8L0das54JHj0W2jw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
قبل از خرید با انواع پنیرها و کاربردشون آشنا شو؛ کدوم پنیر برای چه غذایی بهتره
🧀
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/693870" target="_blank">📅 09:11 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693869">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
اخبار منتشر شده در مورد صدور مجوز پرواز برای شرکت‌های هواپیمایی ایرانی به فرودگاه‌های عراق صحت ندارد
🔹
تا این لحظه مراجع ذیربط در عراق تنها با از سرگیری پروازهای شرکت هواپیمایی العراقیه عراق به ایران موافقت کرده‌اند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/693869" target="_blank">📅 09:05 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693868">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">جله علم النور 4_ جلسه نهم</div>
  <div class="tg-doc-extra">علی مقدم</div>
</div>
<a href="https://t.me/akhbarefori/693868" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
جلسه نهم؛ حکمت اعداد
🔹
در نظام خلقت، اعداد دارای «جهت» و «کیفیت» بوده و محاسبات الهی بر پایه‌ «نگاشت‌های نوری» استوار است.
🔹
اگر زندگی انسان از محاسبات مادی خارج شده و وارد ساحت
«احصاء»
شود، برکت در آن جاری می‌شود.
🔹
رهایی از ماتریکس زمان و دستیابی به عمری پربرکت، در گرو زیستن در نام
«الْمُحْصِي»
و تبدیل شدن به وجودی نوری است.
🔹
برای ورود به نام مبارک «الْمُحْصِي»، انسان باید از پیچیدگی‌های ذهنی‌ و نقشه‌کشی‌های مداوم دوری کند و در پیشگاه پروردگار با سادگی و خلوص نیت حضور یابد.
🔹
صداقت و راستی، فرکانس انسان را از اعداد زمینی به «احصاء الهی» منتقل می‌کند.
🔹
«الْمُحْصِي» دروازه‌ای است که انسان را از بن‌بست‌ محاسبات مادی خارج کرده و به رزق «من حیث لا یحتسب» می‌رساند.
🔹
خداوند با نام مبارک «الْمُحْصِي»، نه تنها اعمال بلکه کیفیت اندیشه‌ها و نیت‌های انسان را اندازه‌گیری و ثبت می‌کند.
#مدیتیشن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/693868" target="_blank">📅 09:02 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693867">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/343029349a.mp4?token=GdThV7yxR5npZaiJSpxbYXZqLAgktTOvNw1Dht0NwHoiZLNdVU88saht0OrWWhHTimJTBUtJu4HTgA6SDEy8DsRXdioPooSOGa9eNaCwIjJzx88XzeH4qXWcYvjcYF0mLy4Z8P7cWMGYhYL8Nhqc6UrV6MOSepQfD80nxelHt5OAf2v7mnrtPK1Xe-LTWCZ9CQUaxOLUOQ9gSug86qE8xbYyoLpxDPlubDTjKW4IlaobvM4X3ImrFtYHPb6KhcEDsuRp0KO5a0y9NLDwd8Uh5Pv47U2EzWupl6gfG4g2ZBCTHvdtDWFngzcavUD0e4My00Y9NWJ-R-GbRADr5B6ONw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/343029349a.mp4?token=GdThV7yxR5npZaiJSpxbYXZqLAgktTOvNw1Dht0NwHoiZLNdVU88saht0OrWWhHTimJTBUtJu4HTgA6SDEy8DsRXdioPooSOGa9eNaCwIjJzx88XzeH4qXWcYvjcYF0mLy4Z8P7cWMGYhYL8Nhqc6UrV6MOSepQfD80nxelHt5OAf2v7mnrtPK1Xe-LTWCZ9CQUaxOLUOQ9gSug86qE8xbYyoLpxDPlubDTjKW4IlaobvM4X3ImrFtYHPb6KhcEDsuRp0KO5a0y9NLDwd8Uh5Pv47U2EzWupl6gfG4g2ZBCTHvdtDWFngzcavUD0e4My00Y9NWJ-R-GbRADr5B6ONw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عینک بزنیم یا نه؟ آیا با نزدن عینک، شماره چشم بالا می‌رود؟!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/693867" target="_blank">📅 08:53 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693866">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
فدراسیون فوتبال: تراکتورسازی، سپاهان و پرسپولیس پیشنهاد داده‌اند که جام قهرمانی لیگ برتر نیمه تمام سال گذشته به جای استقلال، به شهدای میناب اهدا شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/693866" target="_blank">📅 08:46 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693863">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/660e23be90.mp4?token=sMcJyE8xFh4XNxhVvK2CW1GxVnKUoGwIXIWfu8ajlqO41ka-bU_kfGGUrZH3o0_TPn7QxjySNOAfI60boX6YN7I9BRfd1YVFpdE2ILOxHYBpi1KrNfDtGHgi3oTP-jcoPhO0h0ufy4nOlMruZQUB2gF8m86aTPT-Hf7IW2CbJjimzdxxE7W_hOWwzPlnh2bWklsVliCaWLHiauqTIctaFx-Pf1r319k5__zaQ1ptUMnYRpcjXvpL9CvUrkCWweoMX7z-ox_2MQkB_xwwCiRKzdCjK0zU7ZwB2o3liLqxrMftXtw_ucl_oWcPB-NwYqKb48NzUAOU50CTeWqogC8RAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/660e23be90.mp4?token=sMcJyE8xFh4XNxhVvK2CW1GxVnKUoGwIXIWfu8ajlqO41ka-bU_kfGGUrZH3o0_TPn7QxjySNOAfI60boX6YN7I9BRfd1YVFpdE2ILOxHYBpi1KrNfDtGHgi3oTP-jcoPhO0h0ufy4nOlMruZQUB2gF8m86aTPT-Hf7IW2CbJjimzdxxE7W_hOWwzPlnh2bWklsVliCaWLHiauqTIctaFx-Pf1r319k5__zaQ1ptUMnYRpcjXvpL9CvUrkCWweoMX7z-ox_2MQkB_xwwCiRKzdCjK0zU7ZwB2o3liLqxrMftXtw_ucl_oWcPB-NwYqKb48NzUAOU50CTeWqogC8RAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای روبیو: تهدید ایران را جدی می‌گیریم  وزیر خارجه آمریکا:
🔹
ما این تهدیدها را بسیار جدی می‌گیریم. اگر به منافع آمریکا حمله شود، عواقبی در پی خواهد داشت.
🔹
آنچه آخر هفته در بریتانیا اتفاق افتاد، یک تهدید بسیار جدی بود. ایران به دنبال دستیابی به تعداد زیادی…</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/693863" target="_blank">📅 08:42 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693862">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72020c2878.mp4?token=MHKhUwxYVDMwjjI5zv9hE5VrZ5qh9VBB0NSpTDlP_LvRYn8N3nOnVz7wMmcpJM_q1Goq3vat56klp_Aw0mHdfSVJJmTHMzM6JgFVEYB8MS-oDjbBsfKaN9PRjqfcBuRqmuU98LQBUvjZWQHVrWl7eXLtOq43_tqVj1bhbyE7Rd9LLQ953w2LMTeynIYKZoXRumL81Cw6AiZOHaW3B6DL5CIA8EpfQ-RfooTr5Urfm9bGlnFPXcYgRIxG54f_UweHkhA6U0iCfG_R6KonywEn_jKlEM4hYn4ym1HoPkjY3dmtKaWC6Uwdtluy2XzjTRYJIEiEfUuGiW7YTSZ5str1rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72020c2878.mp4?token=MHKhUwxYVDMwjjI5zv9hE5VrZ5qh9VBB0NSpTDlP_LvRYn8N3nOnVz7wMmcpJM_q1Goq3vat56klp_Aw0mHdfSVJJmTHMzM6JgFVEYB8MS-oDjbBsfKaN9PRjqfcBuRqmuU98LQBUvjZWQHVrWl7eXLtOq43_tqVj1bhbyE7Rd9LLQ953w2LMTeynIYKZoXRumL81Cw6AiZOHaW3B6DL5CIA8EpfQ-RfooTr5Urfm9bGlnFPXcYgRIxG54f_UweHkhA6U0iCfG_R6KonywEn_jKlEM4hYn4ym1HoPkjY3dmtKaWC6Uwdtluy2XzjTRYJIEiEfUuGiW7YTSZ5str1rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک دریاچه، هزار رنگ، بی‌نهایت آرامش
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/693862" target="_blank">📅 08:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693861">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZPbk00ZlrfjA4w8DuzMKnFy6FJr9LpPe4LWxaKiD3REgLUdXzw8Gw6SEAcnbhJPl78Yn5jTI8KvaSfy-lP45wok_xDSGRTjvpjTSDa88NI72fwa66uo2s9q3pDZDe8OqPttuxtS5WYnam3IzjmXmGLNK9S5AH2fMQHMBJyrfEGH-pIp9Ihwsd6B96LYhZuiAThPkJlN70T3O40tuy_s-pcoSkJl0XsRKqvQte_8sPu-eC6XWK0ngAM4yVSnQerh165VzLQwFyL9tpntDHdx6A2Dyj5-uYHBJ9faFAJqvG1DpYahGJUGDyQbJmoBysNux0Acz7Hio6PPGowSy1RO7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لباس‌های جدید بالنسیاگا با الهام از کارتن مقوایی با قیمت ۸۹۰۰ دلار معرفی شد
🔹
قیمت این لباس معادل ۲ میلیارد تومان میشه!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/693861" target="_blank">📅 08:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693860">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8049cf8551.mp4?token=VBfkYKYLIGxnSN8Eo5PqCa4hEEFJtAxO86zGWFk2iIr3Gwpy5BhBkqNKikoYEzoqX7JnV_nY-Sw0_yBlx-mn6FFKQgAy2F4-kaKDziUXxSK739hUBFtDydUU7xcvs5TpYdNmtcg9bh1WnV9LU9kjs8oDNywd_UWVmoDnBy3kEPYPAlEGjwq1NXPi06Rs12H4Q_m_RePq6fEkql9ER0nwNe5QYVnbivZbOHZVD6Rp7qPOHLkTvI2ZiHxtkQ4IAjPynAG_liGBGy3vYlh0zwm_OgvkVMdl418aPuNeL1awIGTpqXpaqPQOazgWh0pfTFgsgIW2d1JpfcFUaqjDbremkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8049cf8551.mp4?token=VBfkYKYLIGxnSN8Eo5PqCa4hEEFJtAxO86zGWFk2iIr3Gwpy5BhBkqNKikoYEzoqX7JnV_nY-Sw0_yBlx-mn6FFKQgAy2F4-kaKDziUXxSK739hUBFtDydUU7xcvs5TpYdNmtcg9bh1WnV9LU9kjs8oDNywd_UWVmoDnBy3kEPYPAlEGjwq1NXPi06Rs12H4Q_m_RePq6fEkql9ER0nwNe5QYVnbivZbOHZVD6Rp7qPOHLkTvI2ZiHxtkQ4IAjPynAG_liGBGy3vYlh0zwm_OgvkVMdl418aPuNeL1awIGTpqXpaqPQOazgWh0pfTFgsgIW2d1JpfcFUaqjDbremkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک ورزش عالی برای کسانی که سنگ کلیه و پوکی استخوان دارند #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/693860" target="_blank">📅 08:27 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693859">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
مدیرعامل تراکتور: با پیگیری ما معافیت بیرانوند یک ماه تمدید شد
🔹
بدون اینکه بیرانوند خودش به نظام وظیفه برود برای او دفترچه صادر کرده بودند که این غیر قانونی است. همه به بیرانوند گیر داده‌اند، مشکلات دیگر ورزش را پیگیری کنید.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/693859" target="_blank">📅 08:24 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693857">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
بلومبرگ: قطر تعلیق برخی از تعهدات خود درباره محموله‌های گاز طبیعی مایع به آسیا و اروپا را برای یک ماه دیگر تمدید کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/693857" target="_blank">📅 08:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693855">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/705c52bb94.mp4?token=Zv8n_jCuCmnUP3AnebTksLdbyADlvRDTIqxTxKb-4eTaOlejHKQDizWYAcGZ8QDVSITnRsSYopxYitCljspXPg7dQAKrj7oxrDMcZzU-uEm-zauHJItmL2pyLidwWia8gQvHJnqiyQVCDCOMdYHxnWCO6A5eX1xsuRUQTE9O3pxzt2Tm1CU52J2eNrccO_-yj2wDo4qxxLKc7ZO8_WjpmMvyoGCjo509alcX1zO4aNGaMN9ef_WG7e6CtX-Ie1SKI5ikqDeLLssPSKTzZMGDRTN_lptgPlY7gLtpDdjxGw0uR-VlaRlIOOCzsCKgs_iJ4YZb0E8z81b5dV2MUKsGAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/705c52bb94.mp4?token=Zv8n_jCuCmnUP3AnebTksLdbyADlvRDTIqxTxKb-4eTaOlejHKQDizWYAcGZ8QDVSITnRsSYopxYitCljspXPg7dQAKrj7oxrDMcZzU-uEm-zauHJItmL2pyLidwWia8gQvHJnqiyQVCDCOMdYHxnWCO6A5eX1xsuRUQTE9O3pxzt2Tm1CU52J2eNrccO_-yj2wDo4qxxLKc7ZO8_WjpmMvyoGCjo509alcX1zO4aNGaMN9ef_WG7e6CtX-Ie1SKI5ikqDeLLssPSKTzZMGDRTN_lptgPlY7gLtpDdjxGw0uR-VlaRlIOOCzsCKgs_iJ4YZb0E8z81b5dV2MUKsGAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی در پایان سفر به نیویورک: تعداد بسیار زیادی از ملاقات‌های این سفر به درخواست طرف مقابل صورت گرفت/ قرار است پاسخ نهایی طرف آمریکایی توسط میانجی قطری به ما منتقل شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/693855" target="_blank">📅 08:12 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693854">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
ادعای
روبیو: تهدید ایران را جدی می‌گیریم
وزیر خارجه آمریکا:
🔹
ما این تهدیدها را بسیار جدی می‌گیریم. اگر به منافع آمریکا حمله شود، عواقبی در پی خواهد داشت.
🔹
آنچه آخر هفته در بریتانیا اتفاق افتاد، یک تهدید بسیار جدی بود. ایران به دنبال دستیابی به تعداد زیادی پهپاد، موشک و سلاح‌های متعارف بود.
🔹
ایران می‌خواست از زرادخانه خود برای تهدید منطقه و نیروهای ما استفاده کند و سپس به سمت دستیابی به سلاح هسته‌ای حرکت کند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/693854" target="_blank">📅 08:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693853">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
هشدار نارنجی هواشناسی برای ۶ استان
سازمان هواشناسی:
🔹
با تشدید فعالیت سامانه بارشی از عصر امروز تا پایان روز چهارشنبه برای مناطقی در استان‌های آذربایجان غربی، آذربایجان شرقی، اردبیل، گیلان، مازندران و گلستان هشدار نارنجی صادر شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/693853" target="_blank">📅 08:08 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693852">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
ای‌بی‌سی به نقل از یک مقام آمریکایی: یک پایگاه داده بزرگ و جامع متعلق به کارکنان پنتاگون که حاوی اطلاعات حساسی است، هک شد
🔹
هک پایگاه داده کارکنان پنتاگون، ۲.۷۶ میلیون نفر از افراد را هدف قرار داد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/693852" target="_blank">📅 08:07 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693851">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
عراقچی: شروط ایران برای بازگشایی تنگه هرمز مطابق با تأکیدات مقام معظم رهبری به طرف آمریکایی ابلاغ شد  وزیر امور خارجه:
🔹
با میانجی‌گران قطری پیرامون ایده‌هایی برای انتقال به طرف آمریکایی گفتگو کردیم و اکنون منتظر دریافت پاسخ نهایی واشنگتن هستیم.
🔹
ایران همان‌گونه…</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/693851" target="_blank">📅 08:06 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693850">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
عراقچی: شروط ایران برای بازگشایی تنگه هرمز مطابق با تأکیدات مقام معظم رهبری به طرف آمریکایی ابلاغ شد
وزیر امور خارجه:
🔹
با میانجی‌گران قطری پیرامون ایده‌هایی برای انتقال به طرف آمریکایی گفتگو کردیم و اکنون منتظر دریافت پاسخ نهایی واشنگتن هستیم.
🔹
ایران همان‌گونه که برای دفاع نظامی آماده است، برای دیپلماسی نیز طرح دارد؛ این رویکرد، نگاه جهانیان را تغییر داده و ثابت کرده که ایران به دنبال جنگ‌طلبی نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/693850" target="_blank">📅 08:03 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693849">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
وزیر خزانه‌داری آمریکا در گفتگو با نخست‌وزیر و وزیر دارایی لبنان، از آن‌ها خواست اقداماتی را برای مختل کردن شبکه‌های مالی وابسته به ایران و حزب‌الله انجام دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/693849" target="_blank">📅 08:02 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693848">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
خبرنگار آکسیوس: یک مقام آمریکایی به من گفت ترامپ مایل است در ازای پیشرفت ملموس در پرونده هسته‌ای، تحریم‌های ایران را لغو و دارایی‌های مسدود شده این کشور را آزاد کند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/693848" target="_blank">📅 08:01 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693847">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0zjjNhALmgWsEZ8e7UqwkEZqTMfLQJBRevfyajfsgiUnzBrS0L_4WH_mO0n8tVvp_r6KERP2N0fXfO8TqLaswr3u1WMkFOdN1Pki0t17cZORvHq3zXyW43slSMHqsuLUOM6Fg5ekRfMYA9qx0dRvdkGAg45v_xZhpVsv5F2eusF8RgWYji3C3rIGt0jeQF9FGdhovqIKMYL5ulRqoljv4LGgYQkw1P16HyjPwcjdaD8cwlxnMSf_wHa6-k7UBX7rrkb1_Mweap5FuM3xvPVrj92VkuedA0lWXMb6ueu0foKcl7tPO3s6Cd71rqJYQQJ2xN38GlE7wNiyF9y9GHm1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز سه‌شنبه
۷ مهر ماه
۱۷ ربیع‌الثانی ‌۱۴۴۸
۲۹ سپتامبر۲۰۲۶
سه‌شنبه‌ها
#دعای_توسل
بخوانیم
⬅️
متن و صوت دعای توسل
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/693847" target="_blank">📅 08:00 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693846">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14b1c7cc7f.mp4?token=NJxfJW6ualI3AmFM20Tilxz3AywYji156NBT9cnSxGn986yrTjjRBhIJiEnoCwbDv8F49cyo-tXSospGtHcgQUUE-V8OGZ2pmOqM6cyx_GH2eKo4O40LvwWWqqtaeyjGslG4Q695VevNuUq07vPDWrcAcEgZEKaVioVkNAzBVADqUkQqAwo-9LPin857DZyNyQ_C4w8HKmT28XC_og2lZvflFYyXrh0weJwsMPne4GkSjiCR4hBJiHxDYhZKBtv__onALVCyav9sQN92HdvLBrik2XSW9KnVXc7-GAnSFAQ2lehCTkd6hLshX3Wu8EVM1cmz3b1P2ba8JJNeUUHxIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14b1c7cc7f.mp4?token=NJxfJW6ualI3AmFM20Tilxz3AywYji156NBT9cnSxGn986yrTjjRBhIJiEnoCwbDv8F49cyo-tXSospGtHcgQUUE-V8OGZ2pmOqM6cyx_GH2eKo4O40LvwWWqqtaeyjGslG4Q695VevNuUq07vPDWrcAcEgZEKaVioVkNAzBVADqUkQqAwo-9LPin857DZyNyQ_C4w8HKmT28XC_og2lZvflFYyXrh0weJwsMPne4GkSjiCR4hBJiHxDYhZKBtv__onALVCyav9sQN92HdvLBrik2XSW9KnVXc7-GAnSFAQ2lehCTkd6hLshX3Wu8EVM1cmz3b1P2ba8JJNeUUHxIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🎥
#_این_کلیپ_را_حتما_ببینید
سلام و عرض ادب و احترام
💔
یک بچه نیازمند 2 ماهه ساکن روستا داریم که مبتلا به بیماری هیدروسفالی شده و نیاز به عمل جراحی داره،هزینه عمل جراحی160میلیون میشه ولی هزینه شو ندارن و بچه داره عذاب میکشه‌ و روز به روز سرش بزرگتر میشه و باید هر چه زودتر عمل بشه
😔
😔
🔹️
این بنده های خدا هیچ کس و کاری ندارن،امید شون اول به خدا و بعد به شماست تا کمک کنید،فکر کنید بچه خودتون هست هر چقدر که توانایی شو دارید کمک کنید و بفرستید به دوستان و آشنایان تا کمک کنن،خدا به مال و زندگی شما برکت بده
💳
شماره کارت
#رسمی
بنام قرارگاه شهدای گمنام(کلیک کنید کپی میشه)
5892107050067480
📌
جهت اطلاع و ارتباط با مدیر قرارگاه
@Hoseinfahmide313</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/akhbarefori/693846" target="_blank">📅 00:31 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693845">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/knpQVj3Y0l8Yj23n5Skvwdwc5rBJbd0g9tUifIUc16XKMWTgwXUfJ6Tk2WdER2erbC97smmMt8xO0j_dbWuJG8mM_hQ3AYhqND1NpuA1bKepwD75togFCml6Jw15HBwHumBbtH9TFD6VNmJ_BnRtoIV_UQ7DibP9On0lE5qCOd-hjJwez5i_R5TUbMi_XA8mJOLo1IKhlJIluCDgeXouRD21XEtEwtwm4bG7-GLOzWGfv81yubad0kteEOKfrrV_hlhxUMfSvZrxwMLIwtof3qe7HUiSGnVAYK5uadhs8YmBQgyf_QxyqbNi5uKnjXycEVecP_dWZSK_7m6MqXj2zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
تخفیف ویژه در فروشگاه لوازم خانگی گناوه
🔥
🔥
😍
اگه قصد خرید لوازم خانگی داری، این فرصت رو از دست نده!
🛍️
انواع:
❄️
یخچال و سایدبای‌ساید
🧺
لباسشویی
🍽️
ظرفشویی
❄️
کولر گازی
🏠
انواع لوازم خانگی کوچک و بزرگ
💥
قیمت‌های استثنایی و تخفیف‌های ویژه
💳
امکان خرید چکی و شرایط ویژه
🚚
ارسال به سراسر کشور تسویه درب منزل
✅
تضمین اصالت کالا
🎁
همراه با اشانتیون و خدمات ویژه
📞
برای استعلام قیمت و ثبت سفارش:
09175959374
@genaveh21
📲
فروشگاه لوازم خانگی گناوه
🔥
خرید مطمئن، قیمت واقعی، ارسال سریع
🔥
لینک کانال
👇
https://t.me/+UwTOb3oQ3sRE8GDP</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/693845" target="_blank">📅 00:31 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693844">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDigikala | دیجی‌کالا</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPy2Rfr33RZKWGHzJzxBVyD64vcZEhkCGFhVjb2l6-JAIWdiB_aOII7Zjh18WTBxKxZjhNMBW8w_rmnNQ566UVNvTBqVG8zBw5Ybvf2CTcYmMuTvIFZdDGurB3gDAhNc-LyS7JDPkmC2HwuazUWdVyt206Yc_sHSxdY5Y4PCu7MbtA0CFkuLMRUWwdf72TFlvYjIw5YeHLGscMvDXnxFu-dLiDvioy3TDg4StIIySs35pW_0kDjXJrE38LjjknmaO4xV-ooqwHyxiqgTKffp_HT-D9PXkHmrVSCkm5caWpQjCF5L7JtNI1mTdHCqw_4VpcJtLzu1Ho0aY3DpaNocBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای پاییز آماده شدی؟!
🍂
🛍
هرچیزی که برای
فصل جدید
لازم داری، از استایل پاییزه تا لوازم منزل رو، تو
حراج سر ماه
دیجی‌کالا
با تخفیف
بگیر!!
✨
با امکان
پرداخت
اقساطی
و شانس برنده شدن
آیفون ۱۸!
از لینک پایین با
ارسال رایگان
خرید کن تا هر خریدت، ۲ تا شانس حساب بشه!
👇🏻
👇🏻
خرید از حراج سر ماه دیجی‌کالا
🛍
✨</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/693844" target="_blank">📅 00:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693843">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4f129a9c7.mp4?token=dnjXOnoMpbR2Wr1t6PcFVCpbNO5_HufLdSPDaxGrVtnHC9ssgRUHOoV3TcQANmnxjIuBeHhAVrTAm09TXkedaYSQzA9uosepgykMhfr9SQZR_0YnPrzaihm039AdJu6KYUlz0mNoxgsEbNNt_9OI43o4D8wchOtBH9kvczFMcHwcWArtQJLb5ssESgywCUgMtQ5MMX4gCxYnvCodgpafcA-4tIzQLYQcY3w7WIdZ5C9TfDQZc7rrdESFdgA-4CxZOWbFei-nD2khHE8rl7NpiAkbqbgndviM_HgBNJ4Pgo0Aa5A66qTXWroLnbNep2dH6k0Tw2RqL0Z0Y6AUmq8ppg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4f129a9c7.mp4?token=dnjXOnoMpbR2Wr1t6PcFVCpbNO5_HufLdSPDaxGrVtnHC9ssgRUHOoV3TcQANmnxjIuBeHhAVrTAm09TXkedaYSQzA9uosepgykMhfr9SQZR_0YnPrzaihm039AdJu6KYUlz0mNoxgsEbNNt_9OI43o4D8wchOtBH9kvczFMcHwcWArtQJLb5ssESgywCUgMtQ5MMX4gCxYnvCodgpafcA-4tIzQLYQcY3w7WIdZ5C9TfDQZc7rrdESFdgA-4CxZOWbFei-nD2khHE8rl7NpiAkbqbgndviM_HgBNJ4Pgo0Aa5A66qTXWroLnbNep2dH6k0Tw2RqL0Z0Y6AUmq8ppg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
چراغ‌قوه اضطراری چندکاره؛ فقط چراغ‌قوه نیست!
✅
نور LED پرقدرت |
🔋
شارژ USB + پاوربانک |
🧲
مگنت قوی
🔨
چکش شیشه‌شکن |
🔪
تیغ برش کمربند |
🚨
چراغ هشدار
🔥
قیمت ویژه: فقط 1,198,000 تومان!
👇
برای خرید کلیک کنید:
https://memarket24.ir/product/fast/30291/180124/
✨
تخفیف آخر ماه؛ فرصت آخر برای خرید با قیمت بهتر!
https://l.memarket.me/lp/65/180124</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/693843" target="_blank">📅 00:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693842">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
منابع خبری از حمله نیروهای مسلح یمن به نجران در جنوب عربستان و اضطراب در فرودگاه جده در پی حملات نیروهای یمنی خبر دادند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/693842" target="_blank">📅 00:24 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693838">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AmZz6krk-nomwg2c34LxlvZtCEpHK3vnFi9EcbO3-MexepxSeXxLeX-fcinxARS_sVj4xZl9V7wsJUOQRbQ7P0hr108mKZVdVqmdmwOzGk8-TD50Ix9SrZ3uWbVniBUsWTO9P4VtNK0w82bUNmodBN5ypOEAIg65lUMpNOH6gf51wO1y2-RKR3-IB0R7yQunGZIGS6KBXofluLQrd1jG119HgA4tCejbOcpShTfAeixQXMJqhx942H23JqWbrdrTGBNx7mas4ffRL779vFfIRIATu82ZhJfbX7QY0wa84q1MdHbSE6DhS28Xs9sAIs-si-CUS0EY93m4MrJWqggFsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lB1laMyWDfAxJ8x4aQbh1oTPcu9lUd5AQ6DkoMoIEBcQQPDEtcwvhfV9ff_ZBuelAGgBmklz4PGRG_6K8rmOGop_azbMNEAMu9A9N7tth_wIhyJ9NVlHLbu0EBJzmk4GrpCi6vFELF5K0OXkzRuTWtyYtbrMVH3FqIuwjgtcoTfvuBKE3AGQV9NaIdvFdOxfL0GvrQluVg-8poedILaXUa_h-YxX3Wmsg3qVP4qMvH9mG6lxwKhkUEeuR46OOALkYxryHj2XdikgYZ9gVzOQbnkHoQaH9iTY4Keu49kSPAhAI5r4DJeDaB6KnEmPn7LjjSfA6mF-QTXrG128oIcDOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xamfv3_4eyqGdRcoiuzVdlbsMEDZstY6lu6kNVX8EywRdX_Zvo9eAgxz0Mwrm_WCusjIkNrU-N80mKakwwZvzIN_RklPGJHlVeFUx8BhHZGD_xeZHHUggGK2mwz44gggnAg_zb_veaJzU-SRd-BIxRunvE3W4b3yBA0zvnHN2aI2w2zejKqhyvi50LV6diRBd3cgtkPhBdPVXpstoNBxSlU-FqQGNsQXahWUQq2Qci5bDyhgl0ujZVrsdSUeDB33aNkmhFdYWVj-29NA6vQmuKFEj5OjN7EymFooByVb1SFrj0IPGevGTZ7Qz-8J6Mh_WaiRJVc98w-YGPs01It3fw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۳ گروه خوراکی که می‌توانند به کاهش سردرد، آرامش اعصاب و حفظ سلامت مغز کمک کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/akhbarefori/693838" target="_blank">📅 00:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693837">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
واشنگتن‌پست: پایگاه پشتیبانی دریایی آمریکا در بحرین در نخستین روز جنگ از فعالیت خارج شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/akhbarefori/693837" target="_blank">📅 00:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693836">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
اختلاف قیمت حدودا ۳ برابری سیب در بازار!
رضا نورانی، رئیس هیئت‌مدیره اتحادیه ملی محصولات کشاورزی ایران در
#گفتگو
با خبرفوری:
🔹
قیمت سیب در میادین عمده‌فروشی حدود ۱۶۰ تا ۱۷۰ هزار تومان است اما در سطح شهر تا ۴۵۰ هزار تومان هم فروخته می‌شود.
🔹
اختلاف قابل‌توجه قیمت عمده‌فروشی و خرده‌فروشی ناشی از ضعف نظارت بر بازار است و هر میوه‌فروشی قیمت متفاوتی برای محصولات تعیین می‌کند.
🔹
صادرات محصولات کشاورزی به عراق فعلاً به‌طور موقت متوقف شده و اثر آن بر قیمت سیب‌زمینی و پیاز در بازار عمده‌فروشی مشهود است اما کاهش قیمت در خرده‌فروشی‌ها به همان میزان دیده نمی‌شود.
@TV_Fori</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/akhbarefori/693836" target="_blank">📅 00:07 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693835">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
واشنگتن‌پست: پایگاه پشتیبانی دریایی آمریکا در بحرین در نخستین روز جنگ از فعالیت خارج شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/akhbarefori/693835" target="_blank">📅 00:01 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693834">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CLLUy0ULPuyqutcRI4zD93vG4gB-sNbdyGEVnnBBHwH0NFCIE4ZtBze_miXDI1Uf973-4tHmYg4AQPcrUBQ2ng_f4SyCi5ILHw-ANXOv-ZvmYe7vvsefTkWsukOR_QajNGranq9n1LSbZ-cFCjSd2N8JmUg3JSs55tQAw8SvXiwaWu2qjfGFoQkN-_QB2kvqOOf1JE04bL6JkjM_y3oA7vR2M6G91AYhRuOij1SGWoHEZ5k5CI3jtuZg8ubQy7HkrqDw8M6O-TFz2hJVDkqzhMETweQHqBlhaOhvYYBj2nzZR92jZge7ENbeLTwGEE45pl65iOGVIhdZfwEXskIxjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/693834" target="_blank">📅 00:00 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693833">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16b6cf54c5.mp4?token=YnWRE8le3u722JGJUm0fAolp-K6LPM5CsHnQMAM19Z4q0MGp0AQSO3Zg6HoRYJ4nYuWIzzUnFY9iQ9GQAfZftxT_yYSKu2ydBbdjvNBW4t9jK64Y1GIuLy_BetVom1u8AI_UHcFZ8qAxwaBWKmaDt6ooant08K-OamPjxqdBC-xP-QxxdVqwiMvjejRI1Q1hVPlD4Bm0xkqpL2kz4Nh7X8WxW4NOLmJYurFEVoH6Fqsi1GqhRSkwIuVY3Tec-D9WC1k15tgcWiOkkaA8lOn4D0aFdxndmfAhJBKyo6c-FXXEglcCtGh3y7PgV9bGUFKIHD_63La2LNAKtayXv7oqUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16b6cf54c5.mp4?token=YnWRE8le3u722JGJUm0fAolp-K6LPM5CsHnQMAM19Z4q0MGp0AQSO3Zg6HoRYJ4nYuWIzzUnFY9iQ9GQAfZftxT_yYSKu2ydBbdjvNBW4t9jK64Y1GIuLy_BetVom1u8AI_UHcFZ8qAxwaBWKmaDt6ooant08K-OamPjxqdBC-xP-QxxdVqwiMvjejRI1Q1hVPlD4Bm0xkqpL2kz4Nh7X8WxW4NOLmJYurFEVoH6Fqsi1GqhRSkwIuVY3Tec-D9WC1k15tgcWiOkkaA8lOn4D0aFdxndmfAhJBKyo6c-FXXEglcCtGh3y7PgV9bGUFKIHD_63La2LNAKtayXv7oqUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزافه‌گویی وزیر دولت امارات: امارات خواستار پیگیری اشغال جزایر سه‌گانه تنب بزرگ، تنب کوچک و ابوموسی توسط ایران است!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/akhbarefori/693833" target="_blank">📅 23:55 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693832">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
رضایی، عضو کمیسیون امنیت ملی مجلس: دیپلمات‌های ایرانی در شرایط فعلی هیچ مجوزی برای انجام مذاکرات دوجانبه یا سه‌جانبه ندارند/ تا اجرای تعهدات آمریکا در تفاهم اسلام‌آباد، مذاکره‌ای آغاز نمی‌‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/akhbarefori/693832" target="_blank">📅 23:52 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693831">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
دقایقی پیش صدای انفجار در جزیره قشم به گوش رسید
🔹
این صدا از سمت دریا بوده و به نظر می‌رسد اصابتی داخل جزیره رخ نداده است. منابع محلی تاکنون در این زمینه اظهار نظر نکرده‌اند  #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/akhbarefori/693831" target="_blank">📅 23:51 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693830">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
نایب‌رئیس مجلس: مجلس طرح سه فوریتی خروج از NPT را بررسی می‌کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/akhbarefori/693830" target="_blank">📅 23:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693829">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f868d2f383.mp4?token=GHTrHEP76fKRZDxD2UKiqCY_9Bgfy0dw8LVCfpGgIHg_Rn0EnqZEcDO3c8WTuODPgqlhofSNMNQuYu0Z12z70T__5BiC8auMwQCpa4Q8FieRFiHiT-zz2gg-g2BGJej79A9WlTIL4-OaeW6iCx2fqGew55tjm1k4kylIIXIp4BlvdfGx6ZvMlZ-F-XH1Pr6vVP0Ur5QAJddBfibPhlRLHh6qH_eYsQ6GNUvKtcGkjSxFGXrsezpzSDNqaz5KMRBlo9X4C07B2LwPHYEWa_lHAZ_ocn8LXESKFoJXsZXpbVTCRzJMP2VtLsvUZ5PhBZeUHAuAlc6DCLhJTyY25xk4g4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f868d2f383.mp4?token=GHTrHEP76fKRZDxD2UKiqCY_9Bgfy0dw8LVCfpGgIHg_Rn0EnqZEcDO3c8WTuODPgqlhofSNMNQuYu0Z12z70T__5BiC8auMwQCpa4Q8FieRFiHiT-zz2gg-g2BGJej79A9WlTIL4-OaeW6iCx2fqGew55tjm1k4kylIIXIp4BlvdfGx6ZvMlZ-F-XH1Pr6vVP0Ur5QAJddBfibPhlRLHh6qH_eYsQ6GNUvKtcGkjSxFGXrsezpzSDNqaz5KMRBlo9X4C07B2LwPHYEWa_lHAZ_ocn8LXESKFoJXsZXpbVTCRzJMP2VtLsvUZ5PhBZeUHAuAlc6DCLhJTyY25xk4g4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ساعت هوشمندی که بندش برای اندازه‌گیری فشار خون باد می‌شود
🔹
هواوی در ساعت هوشمند Watch D3 از روشی متفاوت برای اندازه‌گیری فشار خون استفاده کرده است؛ داخل بند ساعت یک کیسه هوای کوچک قرار دارد که هنگام اندازه‌گیری باد می‌شود و با ایجاد فشار روی مچ، عملکردی مشابه کاف دستگاه فشارسنج دارد.
🔹
این ساعت علاوه بر پایش فشار خون، امکاناتی مانند اندازه‌گیری قلب، سطح اکسیژن خون، ثبت نوار قلب، پایش خواب و بررسی برخی شاخص‌های سلامت را نیز ارائه می‌دهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/akhbarefori/693829" target="_blank">📅 23:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693828">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
آلودگی هوا در آذر و دی امسال نسبت به سال گذشته کمتر خواهد بود
محمد اصغری، کارشناس هواشناسی در
#گفتگو
با خبرفوری:
🔹
بیشترین آلودگی هوا معمولاً در ماه‌های آذر و دی و همزمان با تشدید وارونگی دما رخ می‌دهد، اما احتمالاً امسال میزان آلودگی هوای شهری در این دو ماه نسبت به مدت مشابه در سال گذشته کمتر خواهد بود.
🔹
امسال عبور موج‌های جوی بیشتر خواهد بود و این موج‌ها با ایجاد تهویه طبیعی، می‌توانند از ماندگاری آلودگی در شهرها جلوگیری کنند.
🔹
با توجه به پیش‌بینی بارندگی مناسب‌تر در خاورمیانه و مناطق اطراف ایران و تهران، وضعیت گردوخاک نیز امسال می‌تواند بهتر از سال گذشته باشد.
@TV_Fori</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/akhbarefori/693828" target="_blank">📅 23:36 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693827">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
مسئول امنیتی کتائب حزب‌الله عراق؛ ضرب‌الاجلی تا ۱۰ مهر برای لغو محاصره هوایی ایران، اعلام کرد
بیانیه کتائب حزب الله:
🔹
در صورت تداوم محاصره هوایی جمهوری اسلامی ایران پس از یکم اکتبر (۱۰ مهر)، موضع ملت عراق قاطع خواهد بود و کار به بستن مرزها و گذرگاه‌ها با کشورهای شریک در تحریم ملت مؤمن ایران خواهد کشید.
🔹
مقاومت اسلامی بر آسمان کشور نظارت خواهد داشت و ابتدا هشدار داده و سپس پرنده‌های متخاصم را ساقط خواهد کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/akhbarefori/693827" target="_blank">📅 23:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693826">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
نایب‌رئیس کمیسیون امنیت ملی: پیش از هر مذاکره‌ای، آمریکا باید شروط ایران را بپذیرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/akhbarefori/693826" target="_blank">📅 23:33 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693824">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
برخی منابع یمنی از حمله موشکی یمنی‌ها به اهدافی در عربستان گزارش می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/akhbarefori/693824" target="_blank">📅 23:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693823">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
دقایقی پیش صدای انفجار در جزیره قشم به گوش رسید
🔹
این صدا از سمت دریا بوده و به نظر می‌رسد اصابتی داخل جزیره رخ نداده است. منابع محلی تاکنون در این زمینه اظهار نظر نکرده‌اند
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/akhbarefori/693823" target="_blank">📅 23:26 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693821">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CVYLeeV6gCd7V8MGvq7GNwStk-7oXMGwekkjuU_amifGQcFJVBKEQ109X6vdKIw73HeJFWmuhFPzk5kKmxmecjge-EeSeaYyOD9yR5fVQd8hJ4rtw1FhgeOa90GjwtnjhYuAAwOmm4jlIL6R3FQK7ybzDDo0oftEVpU-uFoqYhj96oXjfYZzUJs1vkVEdy_VbGZqt8Gum4ig492IeCzbSbDJVLgzGnjofTZdmu0aBD7DMEH4OkVRUY32_I66ELLG61wy7VzxJZuJ29oQcu0jpsVHDYwKKCxzaCXskzLpOmvKWcGn-Jp_RUi7bmFLGBG-PJE8m41lsSFtWM4z8JkMDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G63u3xVdJK8bkIzRZqz55eQhyY9oDer5QktXZ0Vbllqkc1VzcTIruj9s4O-E52-KuQKa3dZY4uW7BQUoGhRpUeKRWcQqinFAK6ZkmB4XBVUQASrkv2HkLHuKNW33uYpwP6av-uzWTa8pDIIqs9mBzQ8xO0YY53CKvLveT9mFjCHdz_Z2Vkf29qUVBT1IlpVZ62hE3-hwMayW56uGOefBqAdFQUDHCE4fBJyUZN7VCYbAf1YfTraFPnIXfl9DGc_WThHvQEO6JO9Lhus7ULkQz9PLNiWYANlihFcV4n6gVN7geBWvLhdNW5F9PgmfH8FbF7Wab3LbNklU_hmOE-eguw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
قهرمانان تغذیه برای رشد قد کودکان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/akhbarefori/693821" target="_blank">📅 23:25 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693820">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
نماینده آمریکا در شورای امنیت: واشنگتن با الحاق کرانه باختری توسط اسرائیل مخالف است
/ الجزیره
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/akhbarefori/693820" target="_blank">📅 23:21 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693819">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONz2nkSsWBuEo9AColo9lzXWg7QxDUEQwgXm0nEQwQnZ7vfQPPOUfRRDXsCDvbZBNnqmBx-wjxWuw_WMNh_xnPYt6X5JNVujsjJZYRLdsp2wHTLZIp9991kLoraq_VAmdXabnx8OBTsM50F17sty8SI3Mg2paSz5YejX5Ffl57D8eqEJan7z8vpfYSBjQ6klVS7DCQhCqwXXtaw7mGfL57KW8Hoh4QT9UpYspFny3seUsIJvvk1hk3j8U-lqzkVnBPIIUAfuZ-lUK7QW6_1MtNBeAS_d0ItuDdhCE68BEqwNIxozApGgwae8lhIDPX_r2z02kwGzqaABwSZX1ikafg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میلی اسناد تحویل طلا به خزانه‌های بانکی را منتشر کرد؛ روایت از کارشکنی در تسویه کاربران
🔹
میلی با انتشار اسناد به روز تحویل طلا اعلام کرد بیش از ۸۵۰ کیلوگرم طلا در خزانه‌های بانکی دارد، اما به‌دلیل آنچه «کارشکنی برخی افراد در پلیس امنیت اقتصادی، دادستانی و بانک کارگشایی» عنوان کرده، دسترسی به این ذخایر برای تسویه کاربران با محدودیت مواجه شده است.
🔹
به گفته میلی، طی یک ماه و نیم گذشته حدود ۳۵۰ کیلوگرم از ذخایر خارج از خزانه‌های بانکی برای تسویه کاربران مصرف شده است.
🔹
این پلتفرم تأکید کرده دارایی کاربران محفوظ است و موضوع محدودیت‌ها را از نهادهای امنیتی پیگیری می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/akhbarefori/693819" target="_blank">📅 23:19 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693818">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/510e502a72.mp4?token=lsh29WSWH34B5yynrx7GZV0ZsrJWR-Gf7ETuGdvT0JaLp1igxhwdllftsTlEOXzLYu2_j3cSgfrBa5oYYH0KCdP6Air3dtl4ADVYk9Nvkq4WwWbFEUw2o6QuM30R9tuGwUNaNzkPIAwj8LvFTdiq-WqgH5yBeOv-ocF0bYqvLSjQ6ldB1uRoIzIuZ961yfqO9ypMtNGA8YFbUFqodNN_9BkA6gbcXwuH1dpDq6vbldOA3vK9sRG5GLWuUWflsT7rmlv03iDAXp_DqLevyza0qwdsyR6HZ7td-lkfdqxKzhn6Yxi6ROCErZYYvKQV_ecwFZka73QcTqvvTyZ_UTdQKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/510e502a72.mp4?token=lsh29WSWH34B5yynrx7GZV0ZsrJWR-Gf7ETuGdvT0JaLp1igxhwdllftsTlEOXzLYu2_j3cSgfrBa5oYYH0KCdP6Air3dtl4ADVYk9Nvkq4WwWbFEUw2o6QuM30R9tuGwUNaNzkPIAwj8LvFTdiq-WqgH5yBeOv-ocF0bYqvLSjQ6ldB1uRoIzIuZ961yfqO9ypMtNGA8YFbUFqodNN_9BkA6gbcXwuH1dpDq6vbldOA3vK9sRG5GLWuUWflsT7rmlv03iDAXp_DqLevyza0qwdsyR6HZ7td-lkfdqxKzhn6Yxi6ROCErZYYvKQV_ecwFZka73QcTqvvTyZ_UTdQKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بزرگ‌ترین دارایی ما در این سال‌ها چی بوده؟!
@TV_Fori</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/akhbarefori/693818" target="_blank">📅 23:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693817">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/693817" target="_blank">📅 23:10 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693816">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmRw1VYtSObeg0AE04Fi0AgVwLlXW6tBapRTbA98bJA3PkmN9rrfJ7tzHctqZfpFtaa57-8s5VdnxFf_1EJzDdGY-orzJ9hV2YUm2BpadWOqhIH658ND7zZd2zDkjTDrnV6A92_l4Qm8zGccu5xMxW6d2pVo8yVEO7grvKe49H0YyOgQxjIEPo99Eny0lJd3Kz7mgL8HrNhfU_MO479tBcHuw4ikM0MYgyW9jKUeGChkNdskMmNpTckOpqxr7u6_oZeEgBsM-dTHdlIl_EO236KUokSS9fmNdlrSFObA-Rj6o2qnRuEPSLkyOXWczxPXRuTCJ1LEf9mn6BwGeEqbTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تیروئید فقط خستگی نیست؛ این نشانه‌ها را هم به همراه دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/akhbarefori/693816" target="_blank">📅 23:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693815">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">گذر از دجال-جلسه هفتم</div>
  <div class="tg-doc-extra">علی مقدم</div>
</div>
<a href="https://t.me/akhbarefori/693815" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
دوره‌ گذر از دجال
جلسه‌ هفتم: تفسیر دعای تقویت حافظه
🔹
تکنولوژی با فراهم کردنِ پاسخ‌های آماده، در حال تضعیفِ بخشی از مغز و توانمندی‌های ذهنی انسان است.
🔹
هدف نهایی دجال، «کم‌عقل کردن» و «منفعل کردن» انسان‌هاست تا در نهایت انسان‌ها قدرت مقاومت یا تشخیصِ حقیقت را نداشته باشند و به سادگی کنترل شوند.
🔹
دعای تقویت حافظه، دعایِ کلیدیِ افزایش فهم و بصیرت است که برای تقویت مرکز ادراک قلب و مقابله با زوال عقل توصیه شده است.
🔹
چهار درخواست کلیدی در دعای تقویت حافظه وجود دارد: «طلب نور» برای تشخیصِ خیر از شر، «طلب بصر» برای دیدنِ حقیقتِ مسائل، «طلب فهم» برای قدرتِ تجزیه و تحلیل اطلاعات، «طلب علم»دانشی که ناشی از اتصال به نام «علیم» پروردگار است.
🔹
آدم جاهل و سطحی‌نگر، هرگز به درکِ امام زمان (عج) نمی‌رسد، شرطِ رسیدن به شناختِ ولیّ، داشتنِ «کمالِ عقل و فهم» است.
🔹
برای ترک اعتیاد به «غم‌خواری و نشخوار فکری»، باید ذهن را با موارد متعالی مانند ذکر مداوم و حفظ ادبیات حکمت بنیان و اشعار پر مغز تمرین داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/akhbarefori/693815" target="_blank">📅 23:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693814">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
مقام ایرانی به پرس‌تی‌وی:
انعطاف‌پذیری ایران در موضع هسته‌ای نادرست است/ موضع ایران در مورد مسئله هسته‌ای تغییر نکرده
است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/akhbarefori/693814" target="_blank">📅 22:58 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693813">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
کانال ۱۳ اسرائیل ادعا کرد:دیدار نتانیاهو با رئیس‌جمهور امارات حدود شش ساعت به طول انجامید و تمرکز اصلی آن بر روی جنگ آتی با ایران بود
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/akhbarefori/693813" target="_blank">📅 22:51 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693812">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
ترامپ در حالیکه باز هم در جلسه کاخ سفید چرت زد گفت قیمت سوخت کاهش خواهد یافت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/akhbarefori/693812" target="_blank">📅 22:49 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693811">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
کمبود ۱۰۰ هزار معلم در آموزش و پرورش
بیت‌اله عبداللهی، عضو کمیسیون برنامه و بودجه مجلس در
#گفتگو
با خبرفوری:
🔹
حداقل حکم کارگزینی معلمان جوان و تازه‌ فارغ‌التحصیلان فرهنگیان، حقوقی بین ۱۸ تا ۲۰ میلیون تومان است و با احتساب هزینه ایاب‌وذهاب در مناطق دورافتاده و روستایی، دریافتی آنان به ۱۴ تا ۱۵ میلیون تومان کاهش می‌یابد، این وضعیت با هیچ منطقی جور نیست.
🔹
این وضعیت محدود به معلمان نیست و کارکنان سازمان‌هایی مانند جهاد کشاورزی، صنعت و معدن وزارت کشور و حتی بازنشستگانی مانند فرمانداران سابق نیز با حقوق‌های ۲۰ تا ۲۸ میلیون تومانی مواجه‌اند.
🔹
آموزش‌وپرورش برخلاف بسیاری از دستگاه‌های عریض و طویل که با تراکم نیرو و خروجی ضعیف مواجه‌اند، با کمبود حدود ۱۰۰ هزار معلم روبرو است و به ناچار از بازنشستگان برای پر کردن کلاس‌ها استفاده می‌کند، بنابراین راهکار اصلی کوچک‌سازی سایر دستگاه‌ها و تخصیص منابع آزاد شده به آموزش‌وپرورش است.
@TV_Fori</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/akhbarefori/693811" target="_blank">📅 22:45 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693808">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c36539f53e.mp4?token=Qb6oXicwrUcHFD1_Hz3oSuNhz42foltTlJK6JnCldzU4uW50VGlF0dmtO4PK_zUIvOEhK85GqYBttbZM1ahMCEo95di0lov0uwecVNj1EWs-r2vPUQ-n5YCn5x2yUZSYHRnSdaeyxJDI4e6-HyMRSBurRFTIqLDwoTIxoplSgVmO3wOCAT-eSWnWeu-tK5yZ79aMmRAjNDLGUs-KoBMO5keAy05_VtRw3QO9yJQo5b40xnsWM3gIe4PEUkxe-eL-obpWyqw-T-jaQH4TWSlwJtjH_eTC8dLJBEoJ1BMu5-QdJRuWwlbkMc460OQV1AOxfVvrIkGmlDYlgz70A03-vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c36539f53e.mp4?token=Qb6oXicwrUcHFD1_Hz3oSuNhz42foltTlJK6JnCldzU4uW50VGlF0dmtO4PK_zUIvOEhK85GqYBttbZM1ahMCEo95di0lov0uwecVNj1EWs-r2vPUQ-n5YCn5x2yUZSYHRnSdaeyxJDI4e6-HyMRSBurRFTIqLDwoTIxoplSgVmO3wOCAT-eSWnWeu-tK5yZ79aMmRAjNDLGUs-KoBMO5keAy05_VtRw3QO9yJQo5b40xnsWM3gIe4PEUkxe-eL-obpWyqw-T-jaQH4TWSlwJtjH_eTC8dLJBEoJ1BMu5-QdJRuWwlbkMc460OQV1AOxfVvrIkGmlDYlgz70A03-vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ در حالیکه باز هم در جلسه کاخ سفید چرت زد گفت قیمت سوخت کاهش خواهد یافت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/akhbarefori/693808" target="_blank">📅 22:38 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693807">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
ادعای تکراری ترامپ: ما خیلی زود در جنگ با ایران پیروز خواهیم شد و آن جنگ تمام خواهد شد #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/akhbarefori/693807" target="_blank">📅 22:36 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693806">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
دریادار سیاری: از خلیج فارس تا شمال اقیانوس هند مال ایران است
🔹
تمامیت سرزمینی و ناموس ایرانی خط قرمز نیروهای مسلح است و وقتی پای ناموس ایرانی وسط باشد از هیچ چیز و هیچکس باک نداریم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/akhbarefori/693806" target="_blank">📅 22:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693804">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5922f04ef0.mp4?token=YkdjuKn_4ltW9ux7RB199_ZPXxGjLOGdoCcKOwwzYsZ0rbolvu_QOqeyCSNNt-hN_0NsIQ5us7xLgilwnbBQvtCEyj9GbmgPDSH__joBM0EGWQiJR2__IieAMcnRUpJlpq2z1qaoOrHbign65pV7ydQjnKziOf718uBoCmzUAAiBtJo7AE_HtvtGkEMgCh3CAL3czSr5SecyTMfu8uNzKxC2kfmn_oOTZ9DKORzb0qDo7DcDLG-N8g4nrUUdpGXJ7BZi3hjA40bjd9ZSKRUuZN3Q6s6K2_pRLSb5jxAfFMrfy6d2__Tnvid4ajOmPxqdHQ2h2dY7T3J7jY3W0otVPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5922f04ef0.mp4?token=YkdjuKn_4ltW9ux7RB199_ZPXxGjLOGdoCcKOwwzYsZ0rbolvu_QOqeyCSNNt-hN_0NsIQ5us7xLgilwnbBQvtCEyj9GbmgPDSH__joBM0EGWQiJR2__IieAMcnRUpJlpq2z1qaoOrHbign65pV7ydQjnKziOf718uBoCmzUAAiBtJo7AE_HtvtGkEMgCh3CAL3czSr5SecyTMfu8uNzKxC2kfmn_oOTZ9DKORzb0qDo7DcDLG-N8g4nrUUdpGXJ7BZi3hjA40bjd9ZSKRUuZN3Q6s6K2_pRLSb5jxAfFMrfy6d2__Tnvid4ajOmPxqdHQ2h2dY7T3J7jY3W0otVPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای تکراری ترامپ: ما خیلی زود در جنگ با ایران پیروز خواهیم شد و آن جنگ تمام خواهد شد
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/akhbarefori/693804" target="_blank">📅 22:33 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693803">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2799f390bd.mp4?token=Nmzixjo4PTZKL8MbIAIx9jeNuT0t1SWPrxmuT8bMdrZ_SMykZPCs5LSCzgIx8GhsevteI7kHVQOsNhF2HiZRkGwrovKjaIkquwIQ9CadS5rX_GpqP-TygqkDwGZb0Lx90-diU5g-NIIu--PO1ZIGOzvDplb5JKT6ZRsQvB5yfHkG3Q2D-1a72ahiZgwcrtj9LHMMIfaW22r2ywAlXzjzr49BIxH9V0R6itmVd1zrhh_0tA6Hp87kwO8FrWTZxYQEfnrUVJZbbiqs_V380dlycopC91jvYkYj9OIF5v6ZpdW9SE5RyVt4eumpF6ZB6_g4Ssd9Hql_dfdJ7qsXRosygQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2799f390bd.mp4?token=Nmzixjo4PTZKL8MbIAIx9jeNuT0t1SWPrxmuT8bMdrZ_SMykZPCs5LSCzgIx8GhsevteI7kHVQOsNhF2HiZRkGwrovKjaIkquwIQ9CadS5rX_GpqP-TygqkDwGZb0Lx90-diU5g-NIIu--PO1ZIGOzvDplb5JKT6ZRsQvB5yfHkG3Q2D-1a72ahiZgwcrtj9LHMMIfaW22r2ywAlXzjzr49BIxH9V0R6itmVd1zrhh_0tA6Hp87kwO8FrWTZxYQEfnrUVJZbbiqs_V380dlycopC91jvYkYj9OIF5v6ZpdW9SE5RyVt4eumpF6ZB6_g4Ssd9Hql_dfdJ7qsXRosygQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پول زور در مدارس ممنوع؛ ثبت‌نام را به مالیات گره نزنید!
🔹
هیچ مدرسه‌ای حق ندارد به اسم «کمک اختیاری»، خانواده‌ها را در تنگنا قرار دهد یا اسم دانش‌آموزی را به دلیل عدم تمکن مالی والدینش در مدرسه مطرح کند./ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/akhbarefori/693803" target="_blank">📅 22:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693802">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E57geqG75A-p9PMnWcFwsxRRG_RL6IQrEEy1CpJu4Q8959PO5L9QtCrrAUG62WonaDmw5sWLM4_HEouQwme74yIPbXbAczDRV3rN8nDo4VG3aPSh8Rs43D8PVGUgaOhVC4xs0j8oi9r3K_69LYQgbS8NAXNoW7YW9icXpp49xLETeUXF3_dth1Du3f_2e8zjvaJOyse_xXiGx5Xa7gVUdWmNOSqYRzxL7kwdl0D1kFflgVAYoPVafau9TxdJHcsZHJhzEk0KxV6ctr56Lp5mYLXbWAnIItgqfYLZP57pZ6FzaoJfWCJ0kk5-4uVcrQ8_X1MvFbpJV9LWaIH10wv7xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تببین قدرت ایران
🔹
رهبر معظم انقلاب در بخشی از پیامشان به ‌مناسبت هفته دفاع مقدس و سالگرد شهادت شهید سیدحسن نصرالله فرمودند که این روزهایی که در آن هستیم پُر است از پیشرفت، عزّت، استقلال، و قدرِ اَعلای اعتبار در جهان اسلام و بلکه کلّ جهان. امروز کسانی ما را ابرقدرت چهارم دنیا می‌دانند. البته آنان بر اساس محاسبات دنیایی چنین می‌گویند؛ ولی محاسبات الهی، کشوری که خود را متعلّق به عترت طاهره صلوات‌الله‌ و سلامه‌‌علیهم‌اجمعین می‌داند و عمده مردمانش دلبسته آن والامقامانند و برای اقامه حق هراسی ندارند را قدرت اوّل جهان می‌داند. ایشان اظهارداشتند که روزهایی بود که دشمن سعی کرده بود عقبه اجتماعی نظام را دائماً ضعیف‌تر سازد ولی در این روزها انواع اقشار جامعه با تفاوت‌های آشکار، بر حفظ مواضع بحقّ خود و از جمله حفظ تنگه پر خیر و برکت هرمز پای می‌فشارند.
🔹
هشتصدوهفتادودومین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/693802" target="_blank">📅 22:24 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693801">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e55493978e.mp4?token=D52ym5Ene0SypTzA_ParlElpbD3do9ffX7KDfuOnPqRDJFDkkHTtc2FfGdEQsY_kKwUNiUJhHC8f1gJ3AehocjmcezlgUpQCtQyhZ3kRdlrw2tAkipHNk1Dszwsqj_oL87p4ZjlVhUxv4_eLt1j2aA5Php_wA4ftOK-ZnH5K5b2lbBqH_bO7Iu-rS0CjpCCf7JD6W04CD2KDK8yR9KLF1Cahbil9dYgM2J0Dzp3T3fevU0yLHkylpD0RZfE7GH9V1dxXim3unlwaweNiTPRwmLdpPLwT9XT9Det1n21E44ztVB40uAj_g9CuHHGgoQOpnOOGCEPAn2Ch19NDOvgIgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e55493978e.mp4?token=D52ym5Ene0SypTzA_ParlElpbD3do9ffX7KDfuOnPqRDJFDkkHTtc2FfGdEQsY_kKwUNiUJhHC8f1gJ3AehocjmcezlgUpQCtQyhZ3kRdlrw2tAkipHNk1Dszwsqj_oL87p4ZjlVhUxv4_eLt1j2aA5Php_wA4ftOK-ZnH5K5b2lbBqH_bO7Iu-rS0CjpCCf7JD6W04CD2KDK8yR9KLF1Cahbil9dYgM2J0Dzp3T3fevU0yLHkylpD0RZfE7GH9V1dxXim3unlwaweNiTPRwmLdpPLwT9XT9Det1n21E44ztVB40uAj_g9CuHHGgoQOpnOOGCEPAn2Ch19NDOvgIgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ درحالی که مدعی بود پیروزی در انتخابات کنگره برایش اهمیت ندارد بار دیگر وعده ۵ هزار دلار به ازای هر رای را تکرار کرد
ترامپ:
🔹
اگر جمهوری‌خواهان در انتخابات مجلس نمایندگان و سنا پیروز شوند، به هر فرد بزرگسال پنج هزار دلار پرداخت خواهد شد؛ و ما می‌توانیم این کار را انجام دهیم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/693801" target="_blank">📅 22:23 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693800">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
دریادار سیاری: مهاجمی که به اهداف خود نرسد یعنی شکست خورده
🔹
کشورهای حوزۀ خلیج‌فارس در جنگ ۸ ساله به صدام امکانات دادند و در این جنگ هم پایگاه‌ها را برای حمله به ما دراختیار دشمن گذاشتند
🔹
صدام فکر می‌کرد زمانی که به مرزهای ایران برسد از او استقبال می‌شود؛…</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/693800" target="_blank">📅 22:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693799">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/435c672b32.mp4?token=mDcNJ3eiT1wLJWe2TtIf7svsa9LeIckA6Yr49Z3AIAqhwkZDRvTnEVeBprN2N1S7wcbqH5SFq47xCfAWert3urrVVLnUjpX8eu1Siw45r2LVza3pUhCH2jz6T5kxlMpQKO07SFmCwrtIATJQSEAmSC3ihjm-jEGb3XQq-O4NxZOdHsYaubW4OsEEjZ9pNYG6O0hDKPFb-DyneIKlDlIBNgwT2ioM2O7d3yXsAdq2DZOhwJtqxo3NDWqyDN9O4nsTjyYmVKYjGYoLKioSUDZMYCG2vPnVuCcWHqoPCCDFnrnEn2vN47sbcWS3jYFvrQ4QNVAEhfqjWGoBfpkQnteosE4QMlavJRUXgyMcnZ9o7NphRpxyu9yU7DLH180obulLnCxYJ1ZJEu9RwPC_YH8HaQhFQ0CIAAq6fapYzDYDyi2AYOuA0UTuCvLsy8MzXePlo7ukAlzTDt0WGC8e73pkKgkNyDQyHw7wIkRmh-e22J3ato9fA2WheZcSO6rZDGj8808mf7Y0mSU1ZIy6X4zA58Sj6_n2q9YmFdYD7VYpYqQOi548txLXd1FANIHQG5r6RWXh53_qIA7myce9FnF5ol8WrNn5B_s1NFtYzWt2Kxg6FpN1wp73AG5l-OTDV5A5U03y_-eUmvOoQVOiKkghDe5ys9-ifVtOqmP4MhI8MqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/435c672b32.mp4?token=mDcNJ3eiT1wLJWe2TtIf7svsa9LeIckA6Yr49Z3AIAqhwkZDRvTnEVeBprN2N1S7wcbqH5SFq47xCfAWert3urrVVLnUjpX8eu1Siw45r2LVza3pUhCH2jz6T5kxlMpQKO07SFmCwrtIATJQSEAmSC3ihjm-jEGb3XQq-O4NxZOdHsYaubW4OsEEjZ9pNYG6O0hDKPFb-DyneIKlDlIBNgwT2ioM2O7d3yXsAdq2DZOhwJtqxo3NDWqyDN9O4nsTjyYmVKYjGYoLKioSUDZMYCG2vPnVuCcWHqoPCCDFnrnEn2vN47sbcWS3jYFvrQ4QNVAEhfqjWGoBfpkQnteosE4QMlavJRUXgyMcnZ9o7NphRpxyu9yU7DLH180obulLnCxYJ1ZJEu9RwPC_YH8HaQhFQ0CIAAq6fapYzDYDyi2AYOuA0UTuCvLsy8MzXePlo7ukAlzTDt0WGC8e73pkKgkNyDQyHw7wIkRmh-e22J3ato9fA2WheZcSO6rZDGj8808mf7Y0mSU1ZIy6X4zA58Sj6_n2q9YmFdYD7VYpYqQOi548txLXd1FANIHQG5r6RWXh53_qIA7myce9FnF5ol8WrNn5B_s1NFtYzWt2Kxg6FpN1wp73AG5l-OTDV5A5U03y_-eUmvOoQVOiKkghDe5ys9-ifVtOqmP4MhI8MqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعلام موجودیت جنبش مسلحانه حرکت یحیی با وعده انتقام از آمریکایی‌ها و اسرائیلی‌ها با استقبال گسترده در شبکه‌های اجتماعی مواجه شده است
🔹
به تازگی یک جنبش مسلحانه تحت‌ عنوان حرکت یحیی که برگرفته از نام یحیی سنوار، فرمانده شهید جنبش حماس می‌باشد با صدور بیانیه‌ای و با وعده انتقام از جنایات آمریکا و اسرائیل، اعلام موجودیت کرده و با محکوم کردن سکوت جامعه بین‌الملل، دعوت و درخواست مشارکت از عموم مردم در سراسر دنیا را برای همراهی با این جنبش داشته است.
🔹
در کانال اطلاع‌رسانی این جنبش آمده است: ای جنایتکاران، ما نه در سرزمین خودمان بلکه در سرزمین خودتان و درب خانه‌هایتان به سراغ شما خواهیم آمد.
🔹
این جنبش اعلام کرد، لیستی از صدر تا ذیل این جنایتکاران تهیه و افشا خواهد کرد و آمادگی این را دارد تا با بکارگیری کمک‌های ناشناس مردمی، از اقدامات عملی هر فردی که قصد عملیات یا ارسال اطلاعات در مورد عوامل جنايات را دارد، حمایت کند.
🔹
در صفحات این گروه در شبکه‌های اجتماعی، هیچ نشانه‌ای از هویت و وابستگی به جریان یا کشوری موجود نیست هر چند در شبکه‌های اجتماعی، گمانه‌زنی‌هایی از نزدیک بودن این گروه به جنبش‌های مقاومت فلسطین وجود دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/akhbarefori/693799" target="_blank">📅 22:19 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693798">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
دریادار سیاری: مهاجمی که به اهداف خود نرسد یعنی شکست خورده
🔹
کشورهای حوزۀ خلیج‌فارس در جنگ ۸ ساله به صدام امکانات دادند و در این جنگ هم پایگاه‌ها را برای حمله به ما دراختیار دشمن گذاشتند
🔹
صدام فکر می‌کرد زمانی که به مرزهای ایران برسد از او استقبال می‌شود؛ ترامپ هم فکر کرد مردم ایران اگر بگوید کمک در راه است و ایران را بمباران کنند مردم از او حمایت می‌کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/693798" target="_blank">📅 22:17 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693797">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2zqkk8YSTFD418W7mj7r-aYTHtfW4FAhb48OCOXJiGZMCZB8MNaw6ln2t00Dnkb6HVmUaRVQNfKtIWr1yyW55AMvc2l_U5QSvRG7DXtfFWJn1wFhFK11K2rRlQOatdmjegc4y2rd69EtUQk02E1awh8J8GmJReLivbvvxxKvAbf1BuV2nwsAzyNkiiLlKFV_YEIHAWmxEvIMnzf-yb4I-X6kbLxrVU-xaJLcRMd1uPzuzVLTIZdrbiGdy2o2af9wztYdlN_OuoJiWcH2xCLEADwoNV95ua3MBMTy3WUACFrxPGpDXHRGHKbFBSJzqRGkCmX4YK8xdIi4AJrtESzgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نامه رهبر انقلاب به برادرشان آیت‌الله سیّدمصطفی خامنه‌ای در دوران نوجوانی و در هنگام حضور وی در
جبهه
بسمه ‌تعالی
🔹
خدمت برادر عزیزم، رزمندۀ گرامی سیّدمصطفی، بالاخره پس از مدّتها که قصد نامه نوشتن را کرده بودم موفّق به چنین امری شدم.
🔹
جای شما خالی، ما در مشهد پس از زیارت و دید و بازدید از سبزوار بازدید کردیم. استقبال مردم خیلی خوب و دلگرم کننده بود. امّا خوب، جای ما هم در آن محیط صفا و خلوص و عشق به خدا خالی. ای‌کاش باز هم توفیق پیدا کنیم و در آن مکان الهی حضور پیدا کنیم.
🔹
بعد از اینکه به تهران آمدیم من دائماً در صدد تهیّۀ کتاب درسی و اسم‌نویسی در مجتمع رزمندگان بوده‌ام تا اینکه دیروز موفق به اسم نوشتن شدم.
🔹
قرار است همگی چند سطری در ادامۀ این دو نامه بنویسند و من از طرف بشری و هدی هم سلام میرسانم. امیدوارم در پناه توفیقات حضرت حقّ انجام وظیفه (بطور احسن) را بنمائی. زیاد وقتت را نمی‌گیرم و تو را به خدا میسپارم./والسلام. سیّدمجتبی
چهارشنبه ۹ مرداد ۶۵
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/693797" target="_blank">📅 22:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693796">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9JD2Muo_ZipcQ9Fk-eYbCCppBzNvC1J64UsWE0ixqQJtdkzCEWNTdplmek7dSvKN_9FbJj9YYBsh01N1keXMYcdO75ETqot4QiQmGRDCD1-Dh3q5T2BC9yOgPAyHzPxLUeNCORsohSrxubzh2WNuFdPClRXLP_ciWyqjONHdC4jdc4s4ii9hnQscZfcG2dr5iTdpvDaMZGoNulvOKmYNfjufxHxjXBMAeofqogYHRW7pqnMY5hXRvj3C3gVM9KdSpbszwAnaPmdqo5r91sycqHL_Wsa8a25Gob7KjDDe7AojQXWKJEUWbp53KtREpwacrhDvO8nm5UWVj1Ow8xUOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رونمایی رسمی از سامانه پیامکی هلدینگ رسانه‌ای خبرفوری
🔹
همزمان با یازدهمین سالگرد تاسیس هلدینگ خبرفوری، از "سامانه هوشمند پیامک خبری" به عنوان گامی نوین در مسیر اطلاع‌رسانی فراگیر رونمایی شد.
🔹
این خدمت راهبردی با هدف دسترسی بی‌وقفه مخاطبان به اخبار مهم…</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/akhbarefori/693796" target="_blank">📅 22:08 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693795">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
وال‌استریت ژورنال: میانجی‌ها برای امتیاز هسته‌ای، به ایران فشار می‌آورند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/693795" target="_blank">📅 22:08 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693794">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4952d610ef.mp4?token=OAhiAZ-QO6qb6dIlGeqx6hsMm8ubLc0h9m5gvKK-QfI9bR-ZWnXFosLM4Aw_JWKXn2hT94sTyH3l9CYSsqXYqXIzZQrDO6FM3M3Ou09xx52CB6kypjWkLzKcszRUrhoVEkW3ZknIPgeZkD84pa32T1bt86D2DN_Ggy5JPpk3VNsvcQAKPF8gdC3sGhqtDh5lW6VGzrZF8han-lkhytlmfwSrBjweK2rexi4rCAK40CCMpE-UfQOpIMbZhkCNuwndIN6uv0s7vNIAEDHGxA6BIkC1VqYrOCaaJ3EkgNyxKHogU12Xek2iXToHi0RzYVk_PHWK6KoPhU2-5YG9OHiUbKTxxuo03nhIZa5n6xwJskhSGrhr0M0jedbm_HnTPOlKn6EANIuhG0SDLcrurtdFdd0Z6eI6tOM155s6_lCXvwByqYYXps7KH46V8I5hyq04mFZcvjzauvaHqy25fBGpW1V8bdRENls9MTh5jZIuyRphnshb7qqT0vhKcGswugTAyOJ2W0T9rVxeKzLyH5dLptfsRpKH5MXZSMkwhbaUhXWNVIlLrLtcd4LO7y0hF_9dgLchm-T1euETwO6NSPdIQ_57fHhP6p9H3QOQcj6qhr9ao5Bhw9DcGUb9QpjvFBDeueCusNziglIny1UkozFcmwMF6zX0WYMIDc6-dNmKBcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4952d610ef.mp4?token=OAhiAZ-QO6qb6dIlGeqx6hsMm8ubLc0h9m5gvKK-QfI9bR-ZWnXFosLM4Aw_JWKXn2hT94sTyH3l9CYSsqXYqXIzZQrDO6FM3M3Ou09xx52CB6kypjWkLzKcszRUrhoVEkW3ZknIPgeZkD84pa32T1bt86D2DN_Ggy5JPpk3VNsvcQAKPF8gdC3sGhqtDh5lW6VGzrZF8han-lkhytlmfwSrBjweK2rexi4rCAK40CCMpE-UfQOpIMbZhkCNuwndIN6uv0s7vNIAEDHGxA6BIkC1VqYrOCaaJ3EkgNyxKHogU12Xek2iXToHi0RzYVk_PHWK6KoPhU2-5YG9OHiUbKTxxuo03nhIZa5n6xwJskhSGrhr0M0jedbm_HnTPOlKn6EANIuhG0SDLcrurtdFdd0Z6eI6tOM155s6_lCXvwByqYYXps7KH46V8I5hyq04mFZcvjzauvaHqy25fBGpW1V8bdRENls9MTh5jZIuyRphnshb7qqT0vhKcGswugTAyOJ2W0T9rVxeKzLyH5dLptfsRpKH5MXZSMkwhbaUhXWNVIlLrLtcd4LO7y0hF_9dgLchm-T1euETwO6NSPdIQ_57fHhP6p9H3QOQcj6qhr9ao5Bhw9DcGUb9QpjvFBDeueCusNziglIny1UkozFcmwMF6zX0WYMIDc6-dNmKBcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئوی وایرال شده از عروس مسلح که در مراسم عروسی اقدام به تیراندازی هوایی کرد
!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/akhbarefori/693794" target="_blank">📅 22:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693793">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gszrx8DQIDktviCfP3m6RBFZNs6nKcLY1FhDV6iysOMcHBV6c0MYpyM8i3HnM3OMdCl5l-u5pEeajdoIJPftV6f0VBZ-Lv2tQfLfzct_bUOzgBLVJKB9YtUvWKekjr6dfvesOuJ0LvRh2xyYdujbCotPcS26IW6vvr0lq58r12_lnqCiHw4DUn073nLBloWPTf3skXANRQKaEDE2r3JyGps75M3eJZ2I10oeXgULdvBp2Vy3XI0u7u5YjmXUGuCyj3IDJK72KtQc4AuxnAjiUN7gfMS_OJakNfjVOg25pQ7lBqWZXq0EiFaxbeHT9ISCI5iYlb89J58G3Qm7CU5e4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌱
یه وام جدید منتظرته!
💰
✨
💼
مالی پلاس | خدمات تخصصی امتیاز وام
🔹
تأمین و واگذاری امتیاز وام
#رسالت
و
#مهر
🔹
مشاوره و راهنمایی تخصصی رایگان
🔹
همراهی و پیگیری تا مرحله دریافت وام
🔹
انجام امور با سرعت، دقت و انصاف
📌
مالی پلاس؛ همراه مطمئن شما در مسیر دریافت تسهیلات
🔗
عضویت در کانال مالی پلاس:
🌐
https://t.me/MaliPlus1</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/akhbarefori/693793" target="_blank">📅 22:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693791">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mLYggKHW2ByKdiErf3YWyU5Gx7GL8nTgoq1TGRm9TCjA1_pTOuuf8ChaPINndt6zve1xEPcklsrsd01nN-_U3cAy4cu5Joz2J_QWgaddXJ2_JKQFDUWp6jwWxysQho4sVCIOR4qa9CCbbN1qKxq1Nb9L9zchE-KIMH-FwaJk81NpmJzrHnb7uBeRd6jRX2ZrwPyaxdsHQzOhhiqymx0zpjzUSSEYC7nEQEuCCUMEnYXc1wBv7SwMls-DY6wo1uffXb-HdXhi-ni9GYIw0nbL8PuId-zOtczFuN6tzDfb3Huy02MNWuas5K_tEP0e7n7ptzHJQIRFRnl-CgKv4G3JVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام_رهبر_معظّم_انقلاب_به_مناسبت_هفته_دفاع_مقدس_و_سالگرد_شهادت_شهید.pdf</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/akhbarefori/693791" target="_blank">📅 21:54 · 06 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
