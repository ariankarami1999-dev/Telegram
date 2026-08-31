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
<img src="https://cdn4.telesco.pe/file/qmqweqrD3xzr51d2Wkt-_AY7Gu-mbTvaG14CxCf1xXfiDjdUnlgovFKeo2s8rjNBgsmdo22S8t2lOa6A3brQ8TlNDgfUnJ29Z0jULPx_BKbss9TzTiJnOcfzdLGuC1TbON-s-Cwh83Ih6cR1OksNaloFOTN6fW8j2esAFchyCFc_FqXQ7TdXkltXbiue8ohn1srdhEZRfI8ZkyRA3RmkGKFRWvn7B5-4tdJ6F0YWmrgAjSFMwpHA-R2MLnTAJqd2HcqjF0ICeXNvpu84UzrythWP-_RTwDsjZgpu0GNDhWtsj5mVf_mSN9mn-DuFRtEyOl7VJ-SMbAJqIJGz7uLvcw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 960K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-09 20:38:04</div>
<hr>

<div class="tg-post" id="msg-144785">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZWoPCs1m03LYvFI--3dg98KFmfy1DIiVWKQX-k0KuOQjLBQfpj1TltpJMXqpKoSwfh8i-onC8_TOc_ovbYJqtSQ0wHOm5GxsoYpKbaCGXVMEp_iDdfiR1iRuEfv1C4UjcyaXPxwGqZfrag0mka3KoV6ZA7TsOeR0AXKYVDTQbfjWDLvsK4iwXE2PP2R6ebaJqNh5kDk7Svg080EEOcS-gcOrTS_HnfiiOWA_m3dpKPfffdcdBwgFlwV-Cq1v19zSv36MznWfQSt9uY3AaO8faZa53h4j7RBfuEl38nzyna4KLj2dZgKXuKtaE0FXBNVr_0yxfdWKhZxhODO3y-BkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جنوب لبنان،دقایقی قبل
✅
@AloNews</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/alonews/144785" target="_blank">📅 20:37 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144784">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
فوری / زلزله‌ای به قدرت حدود ۵ ریشتر هم‌اکنون یاسوج را لرزاند
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/144784" target="_blank">📅 20:28 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144783">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
ترامپ از کنگره می‌خواهد لایحه رمزارز را تصویب کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/144783" target="_blank">📅 20:26 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144782">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
پوتین: در مسیر پایان دادن به مناقشه اوکراین هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/144782" target="_blank">📅 20:23 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144781">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3666243261.mp4?token=L2hQRWcndoor7DWWnLA4q-pDrpzYl6kk6SlJELyelsU66Mek2-K9Zs3JiijyRh-PObPJ5fw5U4y_GwhOwcbE99ZZFQHIixGkhJaDAlBR26ws2SMu9c7kZG-zndLjphaudwu2zfmVU3qdzEuocyw-KctH2n2rpaFxbcOSm3T-FN25gFwYEugMfZ-Ax9hMA7nYjoKzGRI5cg_72fkOPhnqESyTPWkJ1PKCu7T1e8AA9FeGM7gOAaODiZN-Ic64AqNHRn0B_2TR3M0-uLrcLkMGeuHbmqYufeIhFgtfp3y9114SJayJlNOPETvQLdgtgQz0iaXdo_rwGJiBI30GiHCJdQauWwNO7TgOePSgBh7W4viQIZbKRlJ3igTf-adB2ybo4iy_74EMuXEpr7JCgeQ5cqjm9dvp3M4Kt1LdvF-pf1m89YRxCYXhotDPXZnaGrlTbKWQLLefCnH8PRArveYMiVjVj5EOcjHJ45M6Fg5VaeMZX21sH8uCvdxha3hvaN8Rh3MB9-dtP_QxKGqk7nuSQi8kgx5kN1EuszIJBJ9Ron9LFZaRWI6srKsiAkNzMEBsRwliF8nvpjDw5T990ceDjZQZVdIoSoXeYpbJHHf4UjLoeqZGqpAHgh7kXNCTf6AB6atshS8dgqDbcBNVDMSpvxhXlvmdb1nnYl1bbXAzdrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3666243261.mp4?token=L2hQRWcndoor7DWWnLA4q-pDrpzYl6kk6SlJELyelsU66Mek2-K9Zs3JiijyRh-PObPJ5fw5U4y_GwhOwcbE99ZZFQHIixGkhJaDAlBR26ws2SMu9c7kZG-zndLjphaudwu2zfmVU3qdzEuocyw-KctH2n2rpaFxbcOSm3T-FN25gFwYEugMfZ-Ax9hMA7nYjoKzGRI5cg_72fkOPhnqESyTPWkJ1PKCu7T1e8AA9FeGM7gOAaODiZN-Ic64AqNHRn0B_2TR3M0-uLrcLkMGeuHbmqYufeIhFgtfp3y9114SJayJlNOPETvQLdgtgQz0iaXdo_rwGJiBI30GiHCJdQauWwNO7TgOePSgBh7W4viQIZbKRlJ3igTf-adB2ybo4iy_74EMuXEpr7JCgeQ5cqjm9dvp3M4Kt1LdvF-pf1m89YRxCYXhotDPXZnaGrlTbKWQLLefCnH8PRArveYMiVjVj5EOcjHJ45M6Fg5VaeMZX21sH8uCvdxha3hvaN8Rh3MB9-dtP_QxKGqk7nuSQi8kgx5kN1EuszIJBJ9Ron9LFZaRWI6srKsiAkNzMEBsRwliF8nvpjDw5T990ceDjZQZVdIoSoXeYpbJHHf4UjLoeqZGqpAHgh7kXNCTf6AB6atshS8dgqDbcBNVDMSpvxhXlvmdb1nnYl1bbXAzdrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست‌وزیر پاکستان، شهباز شریف: پاکستان و ایران کشورهای برادر و همسایه هستند.
🔴
هر زمان که با یکدیگر دیدار می‌کنیم، این موضوع باعث شادی و رضایت بسیار می‌شود، زیرا احساس می‌شود که دو برادر با هم گرد هم آمده‌اند تا دیدگاه‌های خود را درباره مسائل مهم تبادل نظر کنند.
🔴
امیدواریم که با هم کار کنیم تا صلح را در منطقه ترویج دهیم و به کاهش تنش‌ها کمک کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/144781" target="_blank">📅 20:18 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144780">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
فارس: پهپاد فوق پیشرفته MQ9 آمریکایی رو تو تنگه هرمز زدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/144780" target="_blank">📅 20:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144779">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50156c76a1.mp4?token=NrPMk1XCurenrK_nAkW5Ea-Wrvj2lvWA53IqjLXSpx54oVUYaAzGD-vIOXAUjgQr1JaE0-D1pgeFtlEndQxiL2R4dcsAMuV_ve_Yi0kYqJODKmJ8blOZyzfKTZ9MdRFMi_xPOFFHrPPrk_cnce_f0uq-N1MKouoZ0ZQmYW90fmt82pqcv_qheESXX-ck6yx0-girAUfbuSjl5fEiKxPiWgpGo9Ca0e2kOpOi71A03kazARYFmD-LzCpb5iTIs3R0SOxpFoOlrh1vCrTnFH1F7dh4zkPWrH9015fX4qG4PGPP3rC7p3tqxymYwpeeJhwWgTVs3yyAWeqBY4dfHFiMng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50156c76a1.mp4?token=NrPMk1XCurenrK_nAkW5Ea-Wrvj2lvWA53IqjLXSpx54oVUYaAzGD-vIOXAUjgQr1JaE0-D1pgeFtlEndQxiL2R4dcsAMuV_ve_Yi0kYqJODKmJ8blOZyzfKTZ9MdRFMi_xPOFFHrPPrk_cnce_f0uq-N1MKouoZ0ZQmYW90fmt82pqcv_qheESXX-ck6yx0-girAUfbuSjl5fEiKxPiWgpGo9Ca0e2kOpOi71A03kazARYFmD-LzCpb5iTIs3R0SOxpFoOlrh1vCrTnFH1F7dh4zkPWrH9015fX4qG4PGPP3rC7p3tqxymYwpeeJhwWgTVs3yyAWeqBY4dfHFiMng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بسنت، وزیر خزانه‌داری آمریکا:
تنها چیزی که برای رهبرانِ ایران مهمه اینه که سرشون به گردنشون چسبیده بمونه [ زنده بمونن ].
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/144779" target="_blank">📅 20:09 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144778">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/arEkKWS5KeCgtV9DwAiu6EQaVZyf5FtaZXE-ouzkxhUMNgD0NCClmhVza-3lX8Kx9TCp89AhQgHwhwww32XRWzW5yEaZ86GHCNuVkyx5e8rgGaB7AWNO_x16ocK2c8NcJ9w6hmnBxdlNyvbkYMUHnOY2_pNWgFug1mLJGKjFzMb8JuZvVfe3mid_rtejUI3-gm93XY4pnQq2CPS3ImzyuSppkDWOzkWC_pHPjE-C23rWd8m4IkFeZRx1Pci_C6kzFScYnVdbe72YkG-BtbMQuRprPRyIVBkFrMQyATNwmmfnWOqGQ62vFg9Mx8W8NusZg5tX6zmgOSzxXF0hx0rT-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت خارجه عربستان سعودی در مورد اتحادیه دفاعی مکه
:
یک دبیرخانه با ریاست یک دبیرکل در پادشاهی عربستان سعودی برای حمایت از فعالیت‌های سه کشور در چارچوب توافق مکه ایجاد خواهد شد.
🔴
دبیرخانه در ابتدا توسط یک دبیرکل از جمهوری اسلامی پاکستان برای یک دوره سه‌ساله رهبری خواهد شد.
🔴
سه کشور از طریق فعالیت‌های مشترک برای تقویت توانایی‌های دفاعی و انسجام نیروهای مسلح خود از طریق همکاری قوی در حوزه صنایع دفاعی و توسعه تولیدات و فناوری‌های مشترک تلاش خواهند کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/144778" target="_blank">📅 19:53 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144777">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
الجزیره: پوتین اعلام کرد روسیه در مسیر پایان دادن به مناقشه اوکراین است
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/144777" target="_blank">📅 19:41 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144776">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
سردار نقدی: ساکنان اسرائیل به کشورهایشان برگردند و به سرعت فرار کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/144776" target="_blank">📅 19:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144775">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
نیویورک پست: قیمت نفت پس از نخستین تبادل حملات آمریکا و ایران در یک ماه گذشته، ۳ درصد جهش کرد و به بالای ۹۰ دلار در هر بشکه رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/144775" target="_blank">📅 19:28 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144774">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4FHuuNCOO8JDDXwN1khKrq1TvhtD_8riv9PzYDGyiWnlvrjvS2D9L63iyevHWzextqxTEaK_e5bCxYd8AeyRFQU_8FzOvVh3NzocF3QYDBDhg8I0mYlQdt7Tzo9AmXFyhC4owATK7EuI9rLwU8HK30H8QoWsOrV3mX4-7SRb4fBPOkEOIZdGfFOUT0zsgvdPgeuceoD-rp3jA5eB950rKoYXylFb_A2g7AP2sM9c3ki-QsyZcUMLtcWAwW8uCXkPYu0sjpBxrEW31Bxkerj4qGRyeQKnv3mRcneA8D-7ya63EXv5XnJe9pxZ7cNzzkY7FgPpBHPA3CxV0OeBHzRaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین وضعیت قیمت نفت/ برنت در کانال ۹۰ دلار
🔴
نفت آمریکا (WTI): ۸۵.۲۷ دلار
🔴
نفت برنت (معیار قیمت جهانی): ۹۰.۳۶ دلار
🔴
نفت امارات: ۹۵.۷۵ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/144774" target="_blank">📅 19:18 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144773">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krckoPMQqX5pboptJ4n8nSCh7zEed-cnPyDqJgNeBX58qhSi_KhEvU2zJEUKTFdLfDx0noESbQmoXxpCFH01pnKkuKnIYIQ5lCKZaYfk6-gV4_vCu6H7dR0ngum6FQUxhyCZ9RFQSnRCde75RgoMYkI5IA9pUNp5YK2PrKs5l-YbdqrnCHdECeVid9V9hbmBoL9CAhsUsVWOKUvoMG0Nu98WFq1hIa73VlMmECL4-tFHu2tpq96ShrKRADNQrE89zs_nIu3yVt0gjk_6K5GycEvc-OwIWq7DiBwWHhWFwqbHX3ci7iLUP-GVwyynSWDqPKLAi5mhi3KlzS4zQPDZXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: ایران با خطر از دست دادن یک شریان اقتصادی اصلی روبرو است پس از اینکه امارات تجارت خود را با این کشور متوقف کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/144773" target="_blank">📅 19:12 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144772">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
دی‌ ونس، معاون رئیس‌جمهور آمریکا: همچنان ابزارهای زیادی برای جلوگیری از شلیک ایران به سوی کشتی‌های تجاری در اختیار داریم
🔴
معتقدم که ترامپ با انتشار پیامی درباره جزیره خارک به دنبال فرستادن پیامی به ایران بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/144772" target="_blank">📅 19:07 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144771">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
سردار نقدی: ناو هواپیمابر و جنگنده‌های آمریکایی آنچنان اهمیت و کارایی ندارن
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/144771" target="_blank">📅 19:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144770">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea9b88dc97.mp4?token=tCPfrE0TgK8ZvUc-zIj_-ZWHXf5n0qTWlmcbItbHVN4cSEZlohR15ypQ-qVnkBNkE_qlmnLRvjYZXqsLc0ps1xz5GSBS4y1cNe10h15RJ6sAg5tB_aeA5rLqWjhvd_H0MvmRXuLUrZ4DXmr154sKhokhWl4Q66Povcemx-ElwUX_26wZ5CDdH17J7e1CvsdQ7scxndMdKD8pvbPxtXka4FB8Q6HU_6jdcdnnu9XbK-uy-gHgLzkXt-3FCBl8BPnmG0XRNJ_MYAs_09C9rqj0P1OwUgSXrGiRAeIKXWmtOBjPqU8QDINWBMbDKHDFpgsaOoyffZemvYqQXxOZGeHRDSvIl5-_b3LCT_uSMqXJL9zFT14TSauOXrBs8Es1FOTN009rutmZ9BbNd1CcGcFUeLbn9eR7MIzPomOQDHYBYN_KqmDsgPPMeftrhON5HMkc5_QsAGsAw0rKTjY6QXT8wEAQ9vawXfE3jqMNijHjjPCplRri6bkoE8E-rAXwU4EBpkFVf_L9mRTmCD_yuO42W100g1Whj0STgM0LU7GEzSxwaq8fQiIyj6wxBdnBG--5tAwPnz146rZDRyNheorTARVy3PqrXm9NOVZw7nGQL4d2Tc-MM76E0yG-6R91TX9P05QZB3VXsPIF-WpfKY4jNBtTGmmUkZZq5JeKayzm5Ps" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea9b88dc97.mp4?token=tCPfrE0TgK8ZvUc-zIj_-ZWHXf5n0qTWlmcbItbHVN4cSEZlohR15ypQ-qVnkBNkE_qlmnLRvjYZXqsLc0ps1xz5GSBS4y1cNe10h15RJ6sAg5tB_aeA5rLqWjhvd_H0MvmRXuLUrZ4DXmr154sKhokhWl4Q66Povcemx-ElwUX_26wZ5CDdH17J7e1CvsdQ7scxndMdKD8pvbPxtXka4FB8Q6HU_6jdcdnnu9XbK-uy-gHgLzkXt-3FCBl8BPnmG0XRNJ_MYAs_09C9rqj0P1OwUgSXrGiRAeIKXWmtOBjPqU8QDINWBMbDKHDFpgsaOoyffZemvYqQXxOZGeHRDSvIl5-_b3LCT_uSMqXJL9zFT14TSauOXrBs8Es1FOTN009rutmZ9BbNd1CcGcFUeLbn9eR7MIzPomOQDHYBYN_KqmDsgPPMeftrhON5HMkc5_QsAGsAw0rKTjY6QXT8wEAQ9vawXfE3jqMNijHjjPCplRri6bkoE8E-rAXwU4EBpkFVf_L9mRTmCD_yuO42W100g1Whj0STgM0LU7GEzSxwaq8fQiIyj6wxBdnBG--5tAwPnz146rZDRyNheorTARVy3PqrXm9NOVZw7nGQL4d2Tc-MM76E0yG-6R91TX9P05QZB3VXsPIF-WpfKY4jNBtTGmmUkZZq5JeKayzm5Ps" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سوئد سفارشی به ارزش ۴.۳ میلیارد یورو برای چهار فریگت از گروه دریایی فرانسه امضا کرده است و انتظار می‌رود اولین کشتی در سال ۲۰۳۰ تحویل داده شود.
🔴
این فریگت‌های جدید بزرگ‌ترین کشتی‌های نیروی دریایی سوئد خواهند بود. این کشور قصد دارد در میان نگرانی‌های امنیتی فزاینده در منطقه بالتیک، توانایی‌های دفاع هوایی استکهلم را تقویت کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/144770" target="_blank">📅 18:53 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144769">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBKhXathyTqFbLiUEEsFv2mtX36S6mKcoP0hIRXo97Vm8N4tPHRfPqE96S8mg3V0QHhftKpNdMPMrUod30PxPRJYhDr_m6VJX5dzEFScEjlKVP4nR3ZvvIi4jOQNgNyxOrOj3t4YvPTpR63pNamAiMeUHgh4JRzF9I0jdUhTs2EMnfE-C_snt6Lousdm3C8ibmwVlRUvApup1dbp0rO1rZbgZ32iIZO7B6OJ72DIF4FbWj2oYlohMypGawOIrGkOW9cgK5Dy3iQ1M7FUnrsKz0ZqAbM49sPzwJqyT0Dm0X1g4-XtCPrN4U1wRyjxpPD6roE33UVgrACzcdT9H6guZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست اینستاگرامی اسطوره لیونل‌مسی و اعلام خداحافظی از مسابقات‌ملی: دوست دارم، و دوست خواهم داشت، و همیشه عاشق این هستم که بخشی از تیم ملی باشم. تمام تلاشم را کردم و دیگر چیزی برای ارائه ندارم.
🔴
همچنین، بازیکنان جوان فوق‌العاده‌ای هستند که در حال ظهور هستند و شایسته حضور در این تیم هستند.
🔴
از شما به خاطر تمام این عشق در طول 20 سال گذشته سپاسگزارم. دلم برای شنیدن صدای شما از نزدیک تنگ خواهد شد. اکنون من هم یکی از شما خواهم بود و همیشه از تیم ملی از بیرون، در زمان‌های خوب و به ویژه در زمان‌های سخت، حمایت خواهم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/144769" target="_blank">📅 18:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144768">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
آمار قربانیان سیلاب در نپال به ٩٣٠ جان‌باخته و نزدیک به ۴ هزار مفقود افزایش یافت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/144768" target="_blank">📅 18:41 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144767">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3MPRGXXLue0upyMG8_z8spEX5pYfuZHGithViaDFr1NXaVieBT8TiOlo62e1LDb3RgjfQU0KSnTAmMvYSwFj-co70jxFu20tk7JlydcJ9YfS-OhaREPUIiZcAiZHGPX4PCnOOQagTd3Zg00u2CZfh2Sd2Bsvn7R2ZhmFIL46WtIaG20Y1oK6RnFu1VFO_DKQe9DteONmXiAUUAbpor4SJZA39BpafaF906wPWp37AgtLx89dSTWg4g5szlQUhh4PJCuvni3xQHruY9zi_GBW4zB8XYbhiZHOLHopp1Yc5tH_sYGFur4BckbPIW_GJWT2XKKE3xaRnzQn0DFB4eZMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نوید محمدزاده به خاطر حواشی زیاد از تئاتر جدیدش اخراج شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/144767" target="_blank">📅 18:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144766">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
پزشکیان به نخست وزیر هند: منافع جریان‌هایی در آمریکا بر تداوم جنگ است
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/144766" target="_blank">📅 18:29 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144765">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
دفتر نخست‌وزیری پاکستان با انتشار بیانیه‌ای، از دعوت رسمی شهباز شریف از مسعود پزشکیان برای سفر به اسلام‌آباد خبر داد.
🔴
این دعوت در راستای رایزنی‌های منطقه‌ای و تلاش‌های دیپلماتیک اسلام‌آباد انجام شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/144765" target="_blank">📅 18:29 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144764">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
پزشکیان در دیدار با نخست‌وزیر پاکستان: ایران همچنان آمادگی دارد توافقی را که با تلاش دولت پاکستان حاصل شده است، اجرا کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/144764" target="_blank">📅 18:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144763">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/offDzjbwwXiVgzBLjgqKUv8hw9QYmOUFRMsLF-Va2Qya86_-JJopQixLPkIB1fSzLRPRL_PaDmQh5HcKMaIGfPg48c9Vgl4JyB450yEoKty0RpB3wbU00NrUSHeaGsz2EWWvtcF2W3gp3K4yqo17ZUcQQ2wCG4I6SMEdnLzLTucrPwmsCSHUrGdS2HnxzzpJk_ZSQZFe73o9qJvSkvWnjiByv94Acey9PoWTws6wn-RvbN2s_TmUOjIVBjVOEChGbvvL60ynQ__KMzsi4ZpIgnCgyy0UxgbCMAmhKIJQ7He319NXvfkGUyi3RM79tBGrV-jiXWoCs7GdFnk7s_a5eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمید رسایی: من شبیه یوسف پیامبر هستم
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/144763" target="_blank">📅 18:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144762">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJfb9Bl9xPvfTa943A8zS8Vb9VdSw9K-ez-uwy03odw8UMS4hooz1glPXTQ8DFU5GNkujoLVCc_kcQsIN8AvM57wnkGCkjCDotGM1yT171uaJFkQOsNcDm4jW0qIxxYe-IA-tOUf-FEG0fIt4055rQPjt1TOqoQu-x64MonjKY0WyBYUAuyl-oaKFg5CfrvJ6LWVYVBz935lie5pYVSr-MU5Z7mNvahD0LTMkFjJ5huyNlPl3ymIifDxRwxrbCmqkaGdMfM0z2NB9mEdcILqzhj5vsn75BhE8FAPhYeUJyeIXzqfaEtJT0_buyA7mFzE_qJJA16t9WYeK-O69Pn3Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سردار نقدی:
بیش از ۹۰ درصد ذخایر موشکی ایران دست‌نخورده باقی مانده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/144762" target="_blank">📅 17:57 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144761">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/my53La9YDNNGfSvYai9bdD0dT1hBXyuGdFXePYYqNQ_LXVnZUenw65Ebbmkb0JStygAAFZYRW8Zzn14sgueEhygEx-6u2h7pFLhmCxep8gOUI-pWhKmzOFBhJXl-pKthGXEKG3vJrGVsWCtqWG_6cxtThRTTOR5o5R97cimK5c08QDKdOr1I67pWsMPXdoI53TUEFGfKC0r9HfiCPihaXrGbAf1GBmt5P4bQmdqt9RO6EOjpCBJpmkAGCjm47-mlovsykEdMinLY1BSpiRZYbTQAQlv33bZVVw81hOlgSBpA3ls3p5kcLrSfvCmfnd0TTCnxf2bPBk-DQlSX4HQNiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حاج علی دبیر:
دشمنان به ما پهلوان‌ها توهین‌ میکنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/144761" target="_blank">📅 17:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144760">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
طبق گزارش کانال ۱۳، یکی از طرح‌های موساد برای سرنگونی رژیم‌ جمهوری اسلامی، عملیاتی مخفی شامل نیروهای کردی بود.
🔴
هزاران سرباز کرد به اسرائیل آورده شدند تا آموزش ببینند. این طرح، یک عملیات هوایی گسترده اسرائیلی در مناطق کردنشین ایران را در نظر داشت تا یک راه‌گذر برای ورود نیروهای کردی به کشور پاکسازی شود؛ طراحان امیدوار بودند که یک شکست نظامی اولیه، اعتراضاتی را شامل میلیون‌ها ایرانی برانگیزد.
🔴
با این حال، این طرح به‌زودی پس از آغاز جنگ کنار گذاشته شد. یک مقام اسرائیلی به کانال ۱۳ گفت: «سه روز پس از آغاز عملیات، دستور رسید: انجام ندهید.»
🔴
این دستور از سوی کاخ سفید صادر شد، پس از مخالفت رجب طیب اردوغان، رئیس‌جمهور ترکیه، و فشارهای جی‌دی ونس، معاون رئیس‌جمهور ایالات متحده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/144760" target="_blank">📅 17:30 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144759">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
اژه ای، رئیس قوه قضائیه : اغتشاشگرا بدونن بازم بخوان تو کشور آشوب و اغتشاش به راه بندازن، برخورد نیروهای امنیتی و دستگاه قضایی بعدا موقع محاکمه، قاطع تر از دفعات قبل‌ خواهد بود، پس فکر این کارو از سرشون بیرون کنن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/144759" target="_blank">📅 17:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144758">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">‏
👈
مقام ایرانی به رویترز:
به ازای هر حمله آمریکا به ایران، تهران پاسخی ده برابر بزرگتر خواهد داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/144758" target="_blank">📅 17:19 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144757">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48f793f615.mp4?token=G6fS2tuvyi3Yr2RuR7pEesWgEwJnaPVW_Ve1s7IEOj65gtaklBil3Z6WfRLyTFUpDGJv7oIWCJkUxxJZehaPzda3NftkiUr7p-DBtrw6Moagnt9TVsv3FhQqwPF6RMJQDpTM66JZjm76kgDXgBKaW18gqQ2kNr2KzIpjiJOfQgIUtUFrszkd1-N21S2QtoGVOeSPR-lGVZueOO97qtAGIh5esevwlg1WeW9bKE6aQ8YtnipbC8B0mC-tJdIphmIvZssTHzPfJhgh9Qce2FpufIgsCQBHrQb5olg0JhsYyCW802GyK6mW2j_5NKYdYDiFA0f4z-mqLT0JAjTIo_xqLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48f793f615.mp4?token=G6fS2tuvyi3Yr2RuR7pEesWgEwJnaPVW_Ve1s7IEOj65gtaklBil3Z6WfRLyTFUpDGJv7oIWCJkUxxJZehaPzda3NftkiUr7p-DBtrw6Moagnt9TVsv3FhQqwPF6RMJQDpTM66JZjm76kgDXgBKaW18gqQ2kNr2KzIpjiJOfQgIUtUFrszkd1-N21S2QtoGVOeSPR-lGVZueOO97qtAGIh5esevwlg1WeW9bKE6aQ8YtnipbC8B0mC-tJdIphmIvZssTHzPfJhgh9Qce2FpufIgsCQBHrQb5olg0JhsYyCW802GyK6mW2j_5NKYdYDiFA0f4z-mqLT0JAjTIo_xqLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بسنت:
می‌خواهم از اتحادیه اروپا و بانک مرکزی اروپا بابت بیانیه قوی حمایت از عملیات‌های اقتصادی ما علیه رژیم ایران تشکر کنم.
با هم، این گروه حکومت وحشتناک ۴۷ ساله آن‌ها را به پایان خواهد رساند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/144757" target="_blank">📅 17:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144756">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aecc7a99d5.mp4?token=O4oMC9kUyHJWkyDd2WVcaLCN2W9BCWDkbcPmzhazhtWODIAZBD1WQe4iaWl9n16m6UpeD3aKFqMwCJxCXJIIGeY1ikqKsja9oyTtbflSv5_ALOJ0f77-80H4miyzmWX4ZAw4I_ax8t4y1D2sEhxeHYjoibXyeL1mECi4Ku12s_15K_L045vtii6odtTrAp20DFr8YLF-Us8oO0lpkebPfmtbwtvGqEumpX_t4okUlVt0cw_z7MtTLXxEs_bArxaXyTFkRHgHbt2z_iRkzO2kqM-zCbXSumirlguyl08KT7VhK61zKJGOOZeRJ7UGU-FJY0H1VhA6k69LcjpMERmVKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aecc7a99d5.mp4?token=O4oMC9kUyHJWkyDd2WVcaLCN2W9BCWDkbcPmzhazhtWODIAZBD1WQe4iaWl9n16m6UpeD3aKFqMwCJxCXJIIGeY1ikqKsja9oyTtbflSv5_ALOJ0f77-80H4miyzmWX4ZAw4I_ax8t4y1D2sEhxeHYjoibXyeL1mECi4Ku12s_15K_L045vtii6odtTrAp20DFr8YLF-Us8oO0lpkebPfmtbwtvGqEumpX_t4okUlVt0cw_z7MtTLXxEs_bArxaXyTFkRHgHbt2z_iRkzO2kqM-zCbXSumirlguyl08KT7VhK61zKJGOOZeRJ7UGU-FJY0H1VhA6k69LcjpMERmVKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: آیا بازه زمانی مشخصی برای فروپاشی اقتصاد ایران وجود دارد؟
🔴
بسننت: اقتصاد آن‌ها نیازی به فروپاشی ندارد. ما فقط باید منتظر بمانیم تا رژیم به خود بیاید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/144756" target="_blank">📅 17:08 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144755">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436d225a06.mp4?token=VcYqSApR5-1qnoXD7T144oEQpiuOYkuOVbqflr-WEK-iSEzJQsxpcFJxjoAWd7mCOF63qDMZ9zKF8eIJqkeRdDExdmLKNlI2iO00KvDD1vao8edaxujTDHoHsGCy8_O7ys8oFHl3F3BYS0asAFUlB5wdO-yxy4vZX0RN8dNBejA57OmrTPOQmHqodvyaVYL5jo-DbKqnzAgodgNwwvwadjkjJUf5AaRAnoJ-uxmuVJhvpSumMocWnLWlilXkPoJmH3BOy9rJO_CtzF0sYb_kEG02jYfzShR6GC-hfb-oNkay6kyHPuLb_WDAlMSX2Xn-8redmhNrD4wp59FpA2kk4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436d225a06.mp4?token=VcYqSApR5-1qnoXD7T144oEQpiuOYkuOVbqflr-WEK-iSEzJQsxpcFJxjoAWd7mCOF63qDMZ9zKF8eIJqkeRdDExdmLKNlI2iO00KvDD1vao8edaxujTDHoHsGCy8_O7ys8oFHl3F3BYS0asAFUlB5wdO-yxy4vZX0RN8dNBejA57OmrTPOQmHqodvyaVYL5jo-DbKqnzAgodgNwwvwadjkjJUf5AaRAnoJ-uxmuVJhvpSumMocWnLWlilXkPoJmH3BOy9rJO_CtzF0sYb_kEG02jYfzShR6GC-hfb-oNkay6kyHPuLb_WDAlMSX2Xn-8redmhNrD4wp59FpA2kk4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بسننت درباره ایران:
ایران به‌خاطر اینکه در اقتصاد در حال شکست است، با خشونت فیزیکی واکنش نشان می‌دهد.
🔴
می‌خواهم از اتحادیه اروپا به‌خاطر حمایت آن‌ها از عملیات طرد اقتصادی تشکر کنم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/144755" target="_blank">📅 16:56 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144754">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b95b794a2.mp4?token=PtE_Rr9T0kH2fmZseD08DKGj4nz690Vp7KN-nSg2Wc5P40rpK2SnBQQtmZBz1S890pKOzZk1nyaamafMorSKI5OiFnlSmVwWeNZsnGkm3a2lIGpXiyl8qezjPfi1-HgCn_dMudFLcAWDED8qERUhUt9PfRx1gPLS038FqHkD1SSdBpVDTQLwuBY5ipHH5GV27jOiIB-tvLzijLYuhHcLxGrnJLh38tBy6i0W7s4FmCltf-Y6SHvwW5QUiN6zG4tOLtCSOLp59HCLujqOMSU7E3aWEVjHWRsv3HR0vhoxGTsi0ldCP2gq7XBIkTEOO6v-nnIK6skbzbXCIlHVvRMsHDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b95b794a2.mp4?token=PtE_Rr9T0kH2fmZseD08DKGj4nz690Vp7KN-nSg2Wc5P40rpK2SnBQQtmZBz1S890pKOzZk1nyaamafMorSKI5OiFnlSmVwWeNZsnGkm3a2lIGpXiyl8qezjPfi1-HgCn_dMudFLcAWDED8qERUhUt9PfRx1gPLS038FqHkD1SSdBpVDTQLwuBY5ipHH5GV27jOiIB-tvLzijLYuhHcLxGrnJLh38tBy6i0W7s4FmCltf-Y6SHvwW5QUiN6zG4tOLtCSOLp59HCLujqOMSU7E3aWEVjHWRsv3HR0vhoxGTsi0ldCP2gq7XBIkTEOO6v-nnIK6skbzbXCIlHVvRMsHDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بسننت درباره ایران:ایران تحریم‌ها را بسیار جدی می‌گیرد. رهبران ایرانی از وضعیت اقتصاد خود شوکه شده‌اند.ما در ایران صف‌های ۳ تا ۴ ساعته برای گاز را شاهد هستیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/144754" target="_blank">📅 16:54 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144753">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jByYFEYSKREUs2TP7mHNRF2p_AP0b8O_jQQ78mxJaUipJnsQNBsIoGxkJt6-ODgiddBLiKfMAwfbarylTNQ84JK0KnnbknAcDiDu8dBcJj2brEpMfV1ZpCu_Wc9WOBRfbhcYdgNJCeyqtdxIVouAjjHHTHJLWjI2POZhfJ3vmRhgbAsgsPEMPajCN7AhpPiYGXeJVMzwCXciFW7mjrPYrIPdO7RHrqxz7MmshVgDg45bRvSOwiuPTrR__kH8mQKzlpAwWAWTEP2jjBMrYPzsqHKB78DBQredPq6FD-y8MKVdMMp8yFtEmg88oKoWI9xdsR-trL-khFMSns_2OnnueQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مسعود با الهام دیدار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/144753" target="_blank">📅 16:52 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144752">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-poll">
<h4>📊 مهمترین دلیل گرونی دلار از دید شما چیه؟</h4>
<ul>
<li>✓ سیاست‌های حاکمیت</li>
<li>✓ دولت</li>
</ul>
</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/144752" target="_blank">📅 16:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144751">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
ترامپ:تمام موشک‌های ایرانی که به سمت پایگاه ما در اردن شلیک شدند، مورد رهگیری قرار گرفتند، به جز یک موشک.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/144751" target="_blank">📅 16:37 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144750">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
آکسیوس: احتمالا امشب ایالات متحده حملاتی به ایران انجام دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/144750" target="_blank">📅 16:29 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144749">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d3f3815fb.mp4?token=cNWATutys8f18gbaGXZNLOg4Kx6y8SUBAOUTkAtIRCgQuZ8cbO4wPAGmGKuDgJJFwZVE7ehadSA_v0VKUbFYjD1SzSBNrcskFLO4hI66CmrIS5-W03g30zKGAaHu5w_uNnC4dPuqjWXj1-KThm210VAUHX4dxL8mJP9VTSSv6H5tX76ORodg1qlqJ0SvOE8vAkj9YB4YyKgTklJMdgNOcx5T0124UB9xdv07Zu6AXLu5SEM-wABglsAEthrxLj06ryqRsdZUVlhtovBDJyfKWgnvCorZnZhSfXAbl799GCvfzrawhlorcf7wIwezvcH8FySHwL9wongY38R5H-4wyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d3f3815fb.mp4?token=cNWATutys8f18gbaGXZNLOg4Kx6y8SUBAOUTkAtIRCgQuZ8cbO4wPAGmGKuDgJJFwZVE7ehadSA_v0VKUbFYjD1SzSBNrcskFLO4hI66CmrIS5-W03g30zKGAaHu5w_uNnC4dPuqjWXj1-KThm210VAUHX4dxL8mJP9VTSSv6H5tX76ORodg1qlqJ0SvOE8vAkj9YB4YyKgTklJMdgNOcx5T0124UB9xdv07Zu6AXLu5SEM-wABglsAEthrxLj06ryqRsdZUVlhtovBDJyfKWgnvCorZnZhSfXAbl799GCvfzrawhlorcf7wIwezvcH8FySHwL9wongY38R5H-4wyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیدار پوتین و شی‌جین‌پینگ
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/144749" target="_blank">📅 16:20 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144748">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kALwBErJnUj-KQpbe04ftvJTxaJz0bmoFTr2ot8dSN9FEQh8bedwD0tmE1ZjUmVSdNGPPrpkh-rGRct1Yr3tQ1nwLFJshF07zJBZ6eS8jsZbmRLbdncC03eGNfhoq_lqlnlhldSP20BS2EqzQYCpYaK_YlHuvd6qdg5zmInEfOM48ZSYpBhM1hcWyN-_lQOSojWzV3cpi6gKzDnV2YbtbZx8Df_FPjaCHDmeub1_5zoXXJq4kuk4EI_mz1oV4TopdYYzpfTkJ-PTv6OAamcmbHW6lVHAY4keVjg-FEmHJOiud8uTYfEKHPrB9DcRl9OGFtnSvzJPvurm_HekkgjWsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نریمان پناهی، مداح: بعد امام علی، امام مجتبی اومد، بعد امام سیدعلی هم امام مجتبی اومد، آیا ایمان نمیارید؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/144748" target="_blank">📅 16:17 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144746">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0baed51151.mp4?token=cg8tS7xVXI8cGTFbW_xgoBfK7ccShzdGdKum7svZfJZWrNswoaLeuM0kWDq4tBZTPHrjBYTsa2kIxFx-WsAkV8XansoqTGexnEfOgsfgdNjQYXeFXJtXhW6_0Q4y5uKkieTIsZ04V4PVJj-QkLfYbqbtqJV5o0IIKu33zXeku4yegjMihzOAb00sh5kr7KMEskKexHo4IlTIdkzLKiE-_iP5UUWPsXS6VXPplRbP6Rs0TvOl5fvuNY1CISP-b4JE5j_oSqs5vrKU9y8JZjrWwS0uR3ScCnAZ49zIBklQpu55lA3jOGeuf7I56D17xfRGTZCIhgCPG5CcpOC43Elb1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0baed51151.mp4?token=cg8tS7xVXI8cGTFbW_xgoBfK7ccShzdGdKum7svZfJZWrNswoaLeuM0kWDq4tBZTPHrjBYTsa2kIxFx-WsAkV8XansoqTGexnEfOgsfgdNjQYXeFXJtXhW6_0Q4y5uKkieTIsZ04V4PVJj-QkLfYbqbtqJV5o0IIKu33zXeku4yegjMihzOAb00sh5kr7KMEskKexHo4IlTIdkzLKiE-_iP5UUWPsXS6VXPplRbP6Rs0TvOl5fvuNY1CISP-b4JE5j_oSqs5vrKU9y8JZjrWwS0uR3ScCnAZ49zIBklQpu55lA3jOGeuf7I56D17xfRGTZCIhgCPG5CcpOC43Elb1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران در گفتگو با فاکس نیوز: ما به حمله ایران به نیروهای آمریکایی در اردن پاسخ خواهیم داد.
🔴
ما به شدت به آنها ضربه خواهیم زد. پاسخی در کار خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/alonews/144746" target="_blank">📅 16:08 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144745">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ATX-maJwVf7LxZWhZWZfYO6S63uYLVSvp36nV0jJ71qlEAzrZ6l3qo2INw1m9TuLjBVlnriN2IpmCz6IWOrdkh-EBkzd_qQqmjkd9K11muvS9bxSHTKox7ND5F4dEQ9Twx-yNww2ShWD-d6yNyzHTE78gZRWfVJCKQOfBnAI4tbOYzDmonfF8T_8vZUbv6WxAruWOMLsSxhPcFD0fMoSVNvQmRGWjqamj9NQKzwARNCFqeh-5kMBDbFwg0EsIO4Lq9HEeUzo6d9LivMKJ_uElm5BdO5Nspi4nKSzp5giggitIf7cHykcUEqNaBP900Psx5wYbPawYf_5R8qfoGsmdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سود BMW از خودروی 740 حدود ۴۰۰۰ دلار؛
سود دولت ایران از عوارض و گمرک آن ۲۴۰ هزار دلار؛
یعنی ۶۰ برابر سازنده!
سود اپل از هر آیفون 17 پرومکس حدود ۵۰۰ دلار؛
سود دولت فقط از رجیستری آن ۵۵۰ دلار!
اسکار بهترین بازیگر هم حق مسئولانی‌ست که
جلوی دوربین از تورم و فشار بر مردم ناراحتند!
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/144745" target="_blank">📅 16:04 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144744">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
فوووووری/ همین الان با شروع مجدد جنگ دلار منفجر شد
😳
‼️
همین حالا چک کنید
👇
https://t.me/+8ARFoPm-00g4YjU0 https://t.me/+8ARFoPm-00g4YjU0   فوری برید ببینید
☝️
☝️
☝️</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/144744" target="_blank">📅 16:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144743">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
وزیر نیرو: اگر این هفته را ‌بدون حادثه پشت سر بگذاریم، با اطمینان می‌توان گفت که از هفته آینده‌ دیگر در بخش خانگی و صنعتی ناترازی برق نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/144743" target="_blank">📅 15:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144742">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
وزیر امور خارجه ترکیه: نتانیاهو اکنون به تهدیدی برای جامعه بین‌المللی تبدیل شده است و باید متوقف شود.
🔴
با نزدیک شدن به انتخابات اسرائیل، لحن ضدترکیه‌ای در حال افزایش است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/144742" target="_blank">📅 15:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144741">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tu84FLXodkGRilRHad5YLVTuxYXrwU42Ay7lE6-eUKCunComz4Mkk77epF0ssZmne_t2SjFkvDbbY9xy2P3Ss0Lucp5T8l4J0jlzZk842APGrsKNcXGb3QCgg7MKXEjMHeXZOmvqyJzI-1C2REPtLknrrow5Vgaj9pbHjkIJrf6EJ-Ei5Jhp7PcsVoIo7tOyKqUK1-ihl66TmVK__DR1SI1hPqA8cP_OYd3p-jbwq4jhKjNmhXnA_lvFt44_ukwj61XkNiPjEmhuSiJ8XzdsCAJv_7rzwA_ADZStd2HJcxlBeLounnscEtm7ZvpFvUm2g6SXrghMPqyZXsuBRSC7tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ: ایران به طور رسمی یک کشور شکست‌خورده است. این کشور مرده است! آنها نیروی دریایی ندارند، نیروی هوایی ندارند، ارز ندارند، به سربازان و پلیس خود حقوق نمی‌دهند، نرخ تورم به 300 درصد رسیده است و رهبری آنها کاملاً در هرج و مرج قرار دارد و قادر به نمایندگی مناسب از کشور نیستند.
🔴
تنها چیزی که آنها دارند، اخبار دروغ از ایالات متحده، تمایل به کشتن معترضان خود (که اکنون بیش از ۱۰۰۰۰۰ نفر کشته شده‌اند. آنها باید به اتهام جنایات جنگی علیه بشریت محاکمه شوند)، و مجموعه‌ای از "دروغ‌های آشکار" است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/alonews/144741" target="_blank">📅 15:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144740">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gAre_g6srWBn9UO9GZPArI4RWWEwL28Y8lpWxQqIwAVmMrGez6loJY8zSz9Qlzxwf58QBim0ATZZz0CWI1ilez_k-b9NcrcMUF3ArgDLvqUqxj9XZJYsX3WShjT63L4oqaAWR3ert8NH4CFKqe7rnWF7aot8btLt4fUTTue47CekSMA33via8IdmRpZWZlBGdtEiB7AXKKQVZ-xKIyVLj5L81uE6MaCHf9LcJ-CEWZ0GftpnmvbOAqu2gMT6eNTJslrYro5Pg0cVOEmtQxdDduUzwe9CZPU2tdng9VuOF2Vb-x51iFaJ4-AjC5Y_zOKSKOGV0-cLsvqaq8xiwXVx6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر ماهواره‌ای نشان می‌دهند یک نفتکش از نوع افرامکس، لکه نفتی به طول حدود ۱۰ کیلومتر در مسیر کشتیرانی جنوبی مورد حمایت آمریکا در تنگه هرمز بر جای گذاشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/144740" target="_blank">📅 15:40 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144739">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
فوری / یک مقام آمریکایی به خبرگزاری رویترز گفت که نیروهای این کشور در جریان حملات شبانه خود، جزیره خارک ایران را هدف قرار نداده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/144739" target="_blank">📅 15:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144738">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63933221fb.mov?token=WydMQCi7V7wt39tgmwfzU7i8KJ_PlbNR37-_fYGFGWuMDoTMOY4Cng3qwHStZA8XVWqCPijCNggPN4fjdnbCJVVc--GF7zgjrCnFHnMj5cuFENVJ-83ju3bQKQs7Lk3gutNKBO67SMKi5Bu5MkwIEpuWcvJdNg5-gDCGIny-9ylqJ8wsprUzeKxYUvoGwgc4HkycJvG61CdOHFpWBv-y3OPZJALoQIwFmDQ3lpvAu3AMq4uBQMRAG_0GVt9p1vOC8UjZLXduQdVtbJ9vKRIaW8L0YqhH_kqb9kD_10kwzjT8u4E3cg-g8ISjqESfv3vJwzah27E819Cp0IgTqi8TBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63933221fb.mov?token=WydMQCi7V7wt39tgmwfzU7i8KJ_PlbNR37-_fYGFGWuMDoTMOY4Cng3qwHStZA8XVWqCPijCNggPN4fjdnbCJVVc--GF7zgjrCnFHnMj5cuFENVJ-83ju3bQKQs7Lk3gutNKBO67SMKi5Bu5MkwIEpuWcvJdNg5-gDCGIny-9ylqJ8wsprUzeKxYUvoGwgc4HkycJvG61CdOHFpWBv-y3OPZJALoQIwFmDQ3lpvAu3AMq4uBQMRAG_0GVt9p1vOC8UjZLXduQdVtbJ9vKRIaW8L0YqhH_kqb9kD_10kwzjT8u4E3cg-g8ISjqESfv3vJwzah27E819Cp0IgTqi8TBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیدار نخست وزیر پاکستان و پزشکیان در حاشیه اجلاس سران سازمان همکاری شانگهای
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/144738" target="_blank">📅 15:18 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144737">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
فوری / بسنت، وزیر خزانه‌داری آمریکا:
واشینگتن احتمالا هر هفته تحریم های ثانویه جدیدی علیه جمهوری اسلامی اعمال میکند و اولویت بانک ها خواهند بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/144737" target="_blank">📅 15:17 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144736">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
طالبان برای کاهش تحریم‌ها و آزادسازی دارایی‌های مسدودشده اش، به شرکت‌های آمریکایی پیشنهاد دسترسی به معادن افغانستان را داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/144736" target="_blank">📅 15:13 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144735">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qf-o3KbT9HAXMUkqHfRR49sbgjuYiPkALfFeq8wni1LWra5eAyPpk1OduiWEnNjJ6JMzPXNPDPbd2pu_fegxbcfLb9xlT4TN0CGXbRFLQnGxpnfZMEg66t5PbrLDioOoEMCu8zvhEHh_e59PfG1TfwuZJkd5OSdHVSoFNhkLDJIGCrHxnZSRbDQOw4GSxuSVUwhjVDF6Bn830FsJXXF8ta0HNBCOO0uJ16ZmGIg8w1xM3SK2G98SgjO1TAUi1tGTco9AS7RylI-KDYBKqa8LOGnBZOSqs8sotxT5Udgd3j8ev0Od2d8fehmp82eNmIBMBxi4sENwt6kc4uO_Fa5lkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دانشگاه تهران اعلام کرده به رتبه‌های برتر بابت انتخاب این دانشگاه بورسیه ماهانه می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/144735" target="_blank">📅 14:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144734">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KuNvN9JrBIkE6RW08sKy29m-eTTBLsBElF5Nu-Ho7hhv0PGuqdiluMqgG-pBuhJsBWI91dH2MBHzKzKVnM1DO1rMpnfdSz7DFSOU49tqQYAhvFraCtZ4AIZfcKAQzSvIgzGVj_XIGZ2r4Y95TSqhDDh8jcbNEGpX_Eu7SQ8uETU6dS7HJxMY5peTX-qy_D-IbRRNWNtpwaksuycMrwX1yaUtGpUcStTadAoBqfmA1d3r8EXP7m9b35ncdZ3zduffTfvCUUr3YlUgNyvzuq1hesfdkUpmW0BtCFhbD9ijwlFWSf9IXmgNY4rB_Dk5GIcrlfABkKgjxB8xA8iKqSpFOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک پزشک جنین رو از رحم مادر خارج کرد و دوباره برگردوند!
🔴
گروهی از پزشکان با یه مورد فوق‌العاده نادر و وحشتناک روبه‌رو شدن یه جنین تو ۲۳ هفتگی(حدود ۶ ماهگی) به توموری خطرناک مبتلا شده بود که نزدیک بود قلبش از کار بیفته.
🔴
دکتر اولویینکا اولوتویه، جراح نیجری‌الاصل، و تیمش اومدن یه کار پشم ریزون کردن: جنین رو به‌طور موقت از رحم خارج کردن، تومور رو برداشتن و دوباره به رحم برگردوندن!
🔴
بارداری ادامه پیدا کرد و این نوزاد در حدود ۳۶ هفتگی(۹ ماهگی) کاملا سالم به دنیا اومد.
﻿
🔴
این نوزاد، تنها کودک تاریخه که دو بار متولد شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/144734" target="_blank">📅 14:42 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144733">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eTSO_0ZmhToa8PJ9q2tRI0RyPeMEuziJM1N4Lck5E6tRohEjPnL61Guyxd1yr3ivKWvD4qEyfdqw3hevK0zF8rOd3Wim0x47RxgjerieLyogiyM3g_YLkprF8TVqtDVWWdMP7bVFXATK3d9EjU9b-DpTJzbpFSMusaak_2kw9ZJOf3kewCEu5qgjiW0sEdBuExTF_jTaO186K3XOSTCWd2bJS26suTl8zRuYddEugjirJIk7OUrTwdwrlYFXleINecFj2bzS09841cNw317bXN8mXMiopGSZGYMmGF3mSkb0eU4JmTax-dqvHZf1JHcF4RJ6gDCjYUhIcl3Iaii13g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بلومبرگ: عربستان سعودی، در بحبوحه فشارهای ناشی از جنگ بر منابع مالی خود، به دنبال دریافت وام‌هایی به ارزش حدود ۸ میلیارد دلار است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/144733" target="_blank">📅 14:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144732">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kmgQ-7c8g4IxLSD1Zv-73EfxVvTSccrPMP81kWzbjMyuSHeMe21z9UfGFKx2QRjrZe452Snh_49QjONtU338a_aw2q93WcJDf63AwitjQS8glzZCACPpIjJgJY2mDLEYcteQ7-YDJIA5gsCu5-jJeIpWm8pqPoTa25eSytNaUvPiwn9SIIBlBs4JJFSdi8RM99LBeds2w86-0ZH2G_av_53MTiJMYt5HCG6dtW8fc42I2ZkFLdCc7o8KB-2l999aB397gTiu522jHDFZt-0hI694Y39pdfifS1wic1D7TF2Edma-efejgCR2bpkUZjpqINJZXsjhpBm9ftcDjbKu_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسرائیل و یونان یک قرارداد دفاعی به ارزش ۳ میلیارد یورو امضا کردند که بر اساس آن، اسرائیل شبکه پدافند هوایی چندلایه یونان موسوم به «سپر آشیل» (Achilles Shield) را احداث خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/144732" target="_blank">📅 14:30 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144731">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
قیمت دلار سقف جدید زد و به ۲۱۰ هزارتومان رسید...
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/144731" target="_blank">📅 14:23 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144730">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
اداره کل هواشناسی تهران: از سه شنبه تا جمعه (۱۰ تا ۱۳ شهریور) کاهش دمای هوا به‌طور میانگین ۳ تا ۵ درجه سلسیوس در گستره استان پیش‌بینی می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/144730" target="_blank">📅 14:18 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144729">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e01d2ddd6.mov?token=R4W2EcTR6rzbm6jZwLeU4twF7dRk-T7reUcY47cEBYwBGI8LW3cDZXJ2OzxmR0LmC1IaZUPs_SFum7vbOUd1kKHBf_tbFSgg1k041fd9TLQ1PNHFCIVrVEzkF5PIrvXScJ8La_OHt1Zh3NOzwv0VU7pvllU2FUuOsKdhKX_g_qZnWbo8lrmY9epA7V975SUXHgJaHFteElHVGAehX70sqnNwUV4sy4r4vLDAwlhkPW116CQmUfJQpHyP6MYGyCPGbMw_9SozVM-Hodz3ciUUh6lWQ09veILNMG1p3RkCQSdcce3HvZ7mvBxAm6EB2YZSdQkQwVUBtQCDoo01CZDU-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e01d2ddd6.mov?token=R4W2EcTR6rzbm6jZwLeU4twF7dRk-T7reUcY47cEBYwBGI8LW3cDZXJ2OzxmR0LmC1IaZUPs_SFum7vbOUd1kKHBf_tbFSgg1k041fd9TLQ1PNHFCIVrVEzkF5PIrvXScJ8La_OHt1Zh3NOzwv0VU7pvllU2FUuOsKdhKX_g_qZnWbo8lrmY9epA7V975SUXHgJaHFteElHVGAehX70sqnNwUV4sy4r4vLDAwlhkPW116CQmUfJQpHyP6MYGyCPGbMw_9SozVM-Hodz3ciUUh6lWQ09veILNMG1p3RkCQSdcce3HvZ7mvBxAm6EB2YZSdQkQwVUBtQCDoo01CZDU-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان به دیدار رئیس جمهور قرقیزستان رفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/144729" target="_blank">📅 14:13 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144728">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RR7fVDAk_Gu1PqXDKemrJQcRk7wXPoreGXQ_RBBFzg7lCjmNYKqHWgkjQYsf_PkOmBeWMFwXxg6u5xaOei6f8VgPlkAHZH4pkiAnQX6d2_JpWQPnIV13B6Z-66-OhaOIZoLiGznSZVz1brfidx-TzzubRgbmLEoPn58KKxhk13Z3VDrKtAQ9X0r6buLrVChT8m0BARwm_8vMO6zi5dicaf9rCHofDSAllvVfJkqYMQAgHZVKOhixew79lUTY91iKsdbD5Au2HRPd2R2dx7CWAtXoaZZ-mQaIK2EcqaMnxeeHje9t_jQwDFkEqVu-7buqG0O0hVlZwgpvF01RrpL_8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پیشنهاد حذف تعرفه‌های پلکانی و اعمال تعرفه یکسان ۱۰۰ درصدی خودروهای وارداتی، با واکنش انجمن واردکنندگان خودرو مواجه شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/144728" target="_blank">📅 14:08 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144727">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
بلومبرگ: پاکستان اعلام کرد که شش یا هفت کشور با اکثریت مسلمان به عضویت پیمان دفاعی مکه علاقه‌مند هستند؛ پیمانی که در ۷ اوت توسط پاکستان، عربستان سعودی و ترکیه امضا شد.
🔴
بنگلادش به‌طور عمومی علاقه‌مندی خود را اعلام کرده است، در حالی که ترکیه پیشنهاد داده است که مصر نیز می‌تواند به این پیمان بپیوندد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/144727" target="_blank">📅 14:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144726">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
الجزیره: میزبانی از پایگاه‌های آمریکا برای اردن هم «مزیت» است و هم «مسئولیت»
🔴
امان همچنان متحد نزدیک واشنگتن است و از نظر مالی از میزبانی این پایگاه‌ها سود می‌برد، اما در حال درک هزینه‌ها نیز هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/144726" target="_blank">📅 14:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144725">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
فوری / اتحادیه اروپا: ما به همکاری با آمریکا و دیگر شرکای گروه ۷ برای حفظ فشار بر ایران ادامه خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/144725" target="_blank">📅 13:53 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144724">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
خبر رسیده بانک های ایران تحت تحریم سنگین و شدیدی میرن!
🔴
سپه، ملی، صادرات، ملت و تجارت تو لیستن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/144724" target="_blank">📅 13:51 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144723">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G5ybCbRQ3q841LxT69jY3XGpW16OihwczDlbZIGr0Gl6hsZc4tA_gvsVhkGdjYDWXPUEy6qz1yWHMOSZ6cyvcGa7INF_by9hkkatNyitUkUi73aKYEqFPlGXw14jp-yCTTnayHrWoy19qhDuy4R-P12B3a7SdVzRZ6FDRvov-TUEyQ5zEylQ8-cjSL4S9G3iuUBE-A4pFC4Gg5zc4q5Om5_ep4Opggl11B22NRxDpC1eN1TUI9fhrXfTqlnIm4XJ0P8y1APFArXnSTNFtKkpC0VyBsIRtoRcGP2bb0l4lw--u4fUT_MH8xW3CVUdv1-uJOUQ-lvd5gCCJh_6JBpWPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزرای دفاع ترکیه و پاکستان در شهر استانبول با یکدیگر دیدار و گفتگو کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/144723" target="_blank">📅 13:40 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144722">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
حمید رسایی: داستان من و اسرائیل مانند داستان یوسف و زلیخاست، زلیخا برای گناه می‌دوید، یوسف برای دوری از گناه
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/144722" target="_blank">📅 13:36 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144721">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jAqjWJemPCQq_fxPev5CEFMr7KIqCKOScfaC-Us6o-MfKQWcSxYNmvq4M4iAATE3rwMJ6ayuiZaOSYGCn5kV7J1TqCtmxNZ0hnuLaHy1Hj1d5b0vKow_ZIVUsD0oagKfVvB5uM33t5jrnFA45lhNLGhx95BlTrCxSjHsopE3cTiKrxVbaee0n3Vk9qHzW-MoVfHwGrzqh9daNYwuiMEEIiFS_RB0nVTNqLXA165htHu8eS1RFPSPrQ7CDLdrhlA5PpLYx9eEfVdK01N0QqhCayrrIb0otxv3q0wBvxtzwyQg3XURZL_00a7g0MbOii2cm3CgWYSw207iQC3Wfr-4Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تانکر ترکرز: تنها کسانی که انتقال محموله‌های STS (انتقال از یک شناور به شناور دیگر در دریا) را در تنگه هرمز انجام می‌دهند، خود ایرانی‌ها هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/144721" target="_blank">📅 13:29 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144720">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
ان‌بی‌سی: قیمت هر اونس طلا با ۰.۷ درصد کاهش، به ۴ هزار و ۴۲۳ دلار و ۸۴ سنت رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/144720" target="_blank">📅 13:26 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144719">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
تلفات سیل‌های نپال از ۹۰۰ نفر فراتر رفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/144719" target="_blank">📅 13:21 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144718">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
تسنیم به نقل از یک منبع نظامی: ادعای آمریکا درباره حمله برای جلوگیری از مین‌ریزی ایران خیالبافی  و داستان‌پردازی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/144718" target="_blank">📅 13:14 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144717">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
روزنامه عبری معاریو: سطح آماده‌باش دفاعی و تهاجمی نیروی هوایی و دیگر یگان‌ها و سامانه‌ های ارتش اسرائیل از ساعات شب در سطح بالایی قرار داشته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/144717" target="_blank">📅 13:12 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144716">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
رسانه‌های یمنی گزارش دادند که نیروهای مسلح این کشور (حوثی ها )کشتی‌های متعلق به عربستان سعودی را در دریای سرخ هدف قرار داده‌اند.
🔴
این منابع به جزئیات بیشتر این حمله و میزان خسارات و یا تلفات احتمالی آن اشاره‌ای نکرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/144716" target="_blank">📅 13:07 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144715">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCZeMEHrQqB2FYZxt9JBamzj1knQnUwEj3tyGvuimg-MiIrR9VG7VVWNprLo2hHkvl3WLpi0SHYpJ4wTlyo6taAEdo1tdveJVwbsAfcAgwLtD2ZdakeclnXbXNNuJ5YZh6CEusDTCuMX6zLwujsj_btw-u5tpnxG06NMmpidqgprPliULdjvHdh0tEpO-8KV4T9UQ_Q4qqhQPgqdiRZb02a9-g4wxplV6ujv2Q9vZuUw991WnEeIcNdhgRDULskv9vFN7ooMmlsP3Cv5qUwZbeqzYkHSZ09XOLMegV5CRUdukSnaYNe-CJ6ybLPSaOPRzFQvpH7fgBd1Dp9MrrkybQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وال‌استریت ژورنال در گزارشی با تیتر «شی جین‌پینگ چگونه نفت را از یک نقطه‌ضعف به یک سلاح ژئوپلیتیکی تبدیل کرد» نوشت: بحران ایران نشان داده است راهبرد چندساله پکن برای انباشت عظیم نفت، یکی از مهم‌ترین نقاط آسیب‌پذیر چین را کاهش داده و یک «دفاع حیاتی در برابر غرب» در اختیار این کشور قرار داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/144715" target="_blank">📅 13:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144714">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
جوزف عون، رئیس جمهور لبنان:
توافقنامه چارچوب نمی‌تواند به صورت یکجانبه اجرا شود؛ باید به طور کامل توسط هر دو طرف و بدون گزینش اجرا شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/144714" target="_blank">📅 12:57 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144713">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
الیوم: سران کشورهای عربی به واشنگتن پیام داده‌اند که اعلام جنگ اقتصادی علیه ایران به دلیل شرایط جغرافیایی، همسایگی و نزدیکی، قابل تحمل نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/144713" target="_blank">📅 12:54 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144712">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
وزارت خارجه امارات: امارات حمله تهاجمی ایران با استفاده از پهپاد به این کشور را به شدت محکوم می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/144712" target="_blank">📅 12:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144711">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
ادعای جان مرشایمر، کارشناس بین‌الملل: ترامپ به دنبال استفاده از سلاح هسته‌ای علیه ایران است
🔴
مشاوران او به شدت مخالف هستند به ویژه ژنرال دن کین، رئیس ستاد مشترک ارتش.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/144711" target="_blank">📅 12:42 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144710">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
مدیرعامل شرکت ملی پخش فراورده های نفتی مدعی شد: جمع آوری کارت های جایگاه در سیستان و بلوچستان و کرمان با هدف مدیریت سوخت و جلوگیری از صف های طولانی بنزین انجام شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/144710" target="_blank">📅 12:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144709">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BCi-z199_zUddqWnepSwpVH8_2R39G0C76srQ_gZpqYQeEWPLptJhkPJcLgSTYOTh4Whgs0gIg2d2AgB_GwwFWK1jIne05oyp8gm13_G22SuaklmmV-QknVefwaViM1tmy3i93S5bpUkFntkG71tSrd9reAd_KJd13VBwr5QGlbNvvnn1TxUSFDPEY6HnJGySdlgvWVv58RrY2sZZDxl1O3Lti_Lo_GDgdH76Nd32vQUqwDOCjw8CwTeI-tJCB6IONyQWXFyW2i7sJNpMpCZaWBoZLjfOpJvAlistkk-ViLa7awDJK_VNa9DMpDihmE4oOryiAHsilEcVzr_-QH3Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیدار پزشکیان با نخست‌وزیر هند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/144709" target="_blank">📅 12:30 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144708">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
انور قرقاش، مشاور رئیس‌جمهور امارات:
وضعیت «نه جنگ و نه صلح» پایدار نیست. ما به راه‌حل‌های سیاسی واقع‌بینانه نیاز داریم که از کاهش تنش و بازگشت ناوبری طبیعی در تنگه هرمز تا رویکردی فراتر از یادداشت تفاهم ناکارآمد (که نقشه راه عملی ارائه نداد) را پوشش دهد..
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/144708" target="_blank">📅 12:26 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144707">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
سپاه  ویدیویی از حملات موشکی علیه پایگاهی در اردن در پاسخ حملات آمریکا به جزیره لارک را منتشر کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/144707" target="_blank">📅 12:14 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144706">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WNH-AeJV2Zroda__CdZrUA-ncQp9PorfxSV7_QDNlPJBQECDuasuSI9PkK_cuesSRCgCBtHH09D31RecKWoqd722_0jbSJoGTCwD7WlSMqNxIe7htyNpuXxegSzd2XQb3KWLMyVwf2Tbk0KJ6TjRKJvorybFI-5tlIa0OshVk6T2eKpRGoVvTf6qt9wPZnVCBjSotzTkTKdBCSYOxxkacJZk1KuPKS3sJcubCLvxh4a9-iDmzGxk8lxcAT_2h-bSaaC2TF8Lnp5epW8m2sGfsu9zzdV6mgklzUz8nD6jTwprz4tDQN7YjelLT30yDLFA1yEmBvTaRfMDAMAjmSmetw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی: نتانیاهو با افتخار می‌گوید که موفق شده است دولت آمریکا را متقاعد کند تا به جای اسرائیل، علیه ایران جنگی را آغاز کند. او در حالی که می‌خندد، درباره "تاثیر" خود بر ایالات متحده صحبت می‌کند، تاثیر ناشی از بیش از 1000 ساعت حضور در شبکه‌های تلویزیونی آن کشور. در عین حال، او با زبان انگلیسی، از رهبری ترامپ تمجید می‌کند.
🔴
او یک مار است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/144706" target="_blank">📅 12:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144705">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
قانون مهریه چه تغییری می‌کند؟
🔴
عضو کمیسیون قضایی مجلس: سقفی برای خودِ مهریه تعیین نشده است
🔴
ضمانت اجرای حبس یا نظارت الکترونیکی تا ۱۴ سکه خواهد بود
🔴
تمکین عام همچنان الزامی است؛ اما زن می‌تواند تمکین خاص را به دریافت مهریه مشروط کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/144705" target="_blank">📅 11:51 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144704">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0bV5PbbY-tViiATBYPUXBzcvnlJi4Mk61gaUcSppsi9ky51IPbVgJQQuyhYkef0IUvAKf-n-M_WNehMiO8nbSxjSYbAeWybkTtT8XMLQH9L27cQAKuaA4Rvg2TWBRG7Qp_lnc7Pw-2X9nq2d922rVrXoms2AjpMkl7y0qpnbOFIb60gJGKwGcSOjf1VEFxuLXyRk5QbWJm2lILHtd5QdIvw0_c3Ll9-8hUBXVG4uvYD-MT348-Awr9R7oZw2JorlCmkFH3V_QBTFBqhNMbuKpTOXzrNvKdwOSCUE7TaundNMSmPTyMrqC2g8Meyi-VNEFwRicXUAzf5evh87gA6Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ :به محض اینکه در جنگ با ایران پیروز شویم، قیمت نفت مثل موشک سقوط خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/144704" target="_blank">📅 11:37 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144703">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
واشنگتن‌پست: چند مقام ارشد نظامی آمریکا در گزارشی محرمانه نسبت به ادامه عملیات گسترده علیه ایران هشدار داده‌اند و گفته‌اند این وضعیت فشار زیادی بر نیروهای آمریکایی در سراسر جهان وارد کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/144703" target="_blank">📅 11:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144702">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
الجزیره: پزشکیان احتمالاً در حاشیه اجلاس شانگهای با پوتین دیدار می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/144702" target="_blank">📅 11:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144701">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5dadc26d4.mp4?token=EqkPlILlf2Rq0QDJHMtSowisoeFVR3qmNyH0zaOLkIO3ymUMNKx1hmlR2VESruSgQzccs6y34u_NiFJgBe-yPDS6ke3co50jnpLNteJVzZaH-9eqQ0FWjeCdp-afVVNmdSu9CAMaRjU8t8GDPdpQq1qLlAl0Ii_C_n6hKGivvGkWwX_qEex2BDngmsA-KEXDKloPFqm6oJuLUhBG4bOlaPAXfDWnCJBhfF2v_C171fISkfHrKSaKEPYTDEoMoERSEN3cLDECFo1-6ohsQN9_7jo2rxgybHvtPO9r8iWsvGhw_BwtytqiNqjCbK52X1h5Qrq5CfzjnYoOkNIN8V-EsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5dadc26d4.mp4?token=EqkPlILlf2Rq0QDJHMtSowisoeFVR3qmNyH0zaOLkIO3ymUMNKx1hmlR2VESruSgQzccs6y34u_NiFJgBe-yPDS6ke3co50jnpLNteJVzZaH-9eqQ0FWjeCdp-afVVNmdSu9CAMaRjU8t8GDPdpQq1qLlAl0Ii_C_n6hKGivvGkWwX_qEex2BDngmsA-KEXDKloPFqm6oJuLUhBG4bOlaPAXfDWnCJBhfF2v_C171fISkfHrKSaKEPYTDEoMoERSEN3cLDECFo1-6ohsQN9_7jo2rxgybHvtPO9r8iWsvGhw_BwtytqiNqjCbK52X1h5Qrq5CfzjnYoOkNIN8V-EsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
واکنش معاون وزیر امورخارجه به حمله شب گذشته آمریکا به جزیره لارک
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/144701" target="_blank">📅 11:13 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144700">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
مقامات آمریکایی به نیویورک‌تایمز: نیروهای ما آماده حمله به نیروهای ایرانی تهدیدکننده کشتیرانی در تنگه هرمز هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/144700" target="_blank">📅 11:07 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144699">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/365909d20e.mp4?token=p3EuaEIDJO8fNInc69iu8mZbVWN9QlnL4NitE11z7_BDgbsWwv2iMoKLXM9fGuwkS_hjy5Iik3kNKhhLPPG3gd44XB7KeDmGUoto1BRe6RT6JzA82EROSXJE2bgjB3wcmsEJIyjxS9ezOy6qITcFGoIqax97PxUOquJKnM4M67IJKtwh-PuAXSATgcB8qOa79xrYjfHDgmuK8xm5qvHJ5O5c12I-E591WihLbznhGWZM7_hMJcgjNy8Yl9ZntVePn8Sv5c1zQFjmCkVHy2jY6g0ijEt2l9SUnQO55M9c9piv3MKwcWky7t-T7WwV-OeFgQQTt0pv6VmLIN9uMC4nrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/365909d20e.mp4?token=p3EuaEIDJO8fNInc69iu8mZbVWN9QlnL4NitE11z7_BDgbsWwv2iMoKLXM9fGuwkS_hjy5Iik3kNKhhLPPG3gd44XB7KeDmGUoto1BRe6RT6JzA82EROSXJE2bgjB3wcmsEJIyjxS9ezOy6qITcFGoIqax97PxUOquJKnM4M67IJKtwh-PuAXSATgcB8qOa79xrYjfHDgmuK8xm5qvHJ5O5c12I-E591WihLbznhGWZM7_hMJcgjNy8Yl9ZntVePn8Sv5c1zQFjmCkVHy2jY6g0ijEt2l9SUnQO55M9c9piv3MKwcWky7t-T7WwV-OeFgQQTt0pv6VmLIN9uMC4nrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روسیه انبارهای نیروهای مسلح اوکراین را هدف قرار داد
🔴
ارتش روسیه اعلام کرد که مجتمع‌های انبار در بوریسپیل که توسط نیروهای مسلح اوکراین مورد استفاده قرار می‌گرفتند، مورد حمله قرار گرفتند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/144699" target="_blank">📅 11:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144698">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
وزیر کار: امشب معوقات بازنشستگان واریز می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/144698" target="_blank">📅 11:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144697">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
کرملین: فعلاً زمینه‌ای برای از سرگیری مذاکرات اوکراین وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/144697" target="_blank">📅 10:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144696">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EIyQy8pwzB3YEDmgPvyLNZe7nAqKXoWe8l2RcssxfnpM70XmDq77SSmsnsqgfTP31LUaMegt4zmmc6oE451FtEX-2uIbp4qbl8QnQLmhHG_FqEId1bHdeI-YrBs_dcPw9KO_Mi5GtI_GGOdGfDn9rhUGNpn4dn4ibdGnCotVma7njs-_63eDVIGId3NRNWCwFL6af9wcI2T3iBGAqPKecdjWUEAgl8HE-aPs6TmfgireHOkQ8SXElDVcg4lt3SOUZsWqsRBvu18ZJfYYIm-9M2EbruRFeXLEuXjbLqdrnDe0GgF9FW7eUOyJIPO10qF4HQMeUukCjAmMj6rQaJQIRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی، فعال سیاسی نزدیک به حکومت: حمله آمریکا به لارک هم از نظر تعداد شهدا هم از نظر جسارت آمریکا ایران را بر آن داشت که تلافی کند
🔴
آمریکا پس از مدت‌ها عدم تبادل آتش دست به حمله جسورانه‌ای زد. امیدها به احیای تفاهم‌نامه ناامید شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/144696" target="_blank">📅 10:41 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144695">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae84ddea7c.mp4?token=ds2HpfzW6gAAoeQV0WXmvVT9f2FBDrzapW5bkzuF03eMT5pRLGmylKFhNpuNErcHvKN4l1pklddWiKs_3TQyAx3qKgzdPtYztxT3o3-aTqqOnEaeClI8-wk4W_z0WfAdK-Vm0VS-i37PmDGiwWiERqbiouo03hvJuvUPVyJg59kjbg0VB_CLCQ5kpXuF8j372sMZsjbfUK-x8bNjQO4yZIb5nT9L632XWB47K3Jqm5EvqQN3icreQvNKEv1o5jxUAcO9CEenTn0DM2Zg1IFLWMY0njqeqPvAO0khok1NNHOiKI_fQWiBTnR7EE4FbvwxXbUzwk8j1EYoQoZJrcJfKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae84ddea7c.mp4?token=ds2HpfzW6gAAoeQV0WXmvVT9f2FBDrzapW5bkzuF03eMT5pRLGmylKFhNpuNErcHvKN4l1pklddWiKs_3TQyAx3qKgzdPtYztxT3o3-aTqqOnEaeClI8-wk4W_z0WfAdK-Vm0VS-i37PmDGiwWiERqbiouo03hvJuvUPVyJg59kjbg0VB_CLCQ5kpXuF8j372sMZsjbfUK-x8bNjQO4yZIb5nT9L632XWB47K3Jqm5EvqQN3icreQvNKEv1o5jxUAcO9CEenTn0DM2Zg1IFLWMY0njqeqPvAO0khok1NNHOiKI_fQWiBTnR7EE4FbvwxXbUzwk8j1EYoQoZJrcJfKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران :
اونا 52000 نفر از معترضا رو کشتن و تا همین 3 ماه پیش، حتی به خیلی‌هایی که اصلاً اعتراض نمی‌کردن، توی خونه‌هاشون شلیک می‌کردن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/144695" target="_blank">📅 10:37 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144694">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
وزارت دفاع امارات: گزارش‌های رسانه‌ها درباره هدف قرار گرفتن پایگاه هوایی المنهاد با موشک را تکذیب می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/144694" target="_blank">📅 10:36 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144693">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8OD9g_YdnzUlmbIYasdKj9oWFvr_UxTGSzrC7jmK28CafjmoKYNYCaCGdNGqZ8i0oojnS0sssEUxeOwV8z7XCzc96VV83kLOeWz3dIcuxODVxNSowkmgI6tGU57YR5Z_l-vojLEFLcUNloENXuGrUoF37EUc1lmwWTKkntb2GFUqFVqJvQH40-tmrpgUtb7oUKtX3C1NnzbH3zkBCFMjtqbvUIE5v8d2tUgYr01kxSLRmYh3-wOrBjZiHC4JtR7QbLOlOIprKmhaS2At0O2t6dgW2OEFaD4vebkiT5SjegBhDFQxVklWVkIBZTGbd5_w16Lfd9p3Bne7b7etAJdWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فلاحت‌پیشه: آمریکا می خواهد تنگه هرمز را به مسئله اصلی نشست بزرگترین قدرت های اقتصادی دنیا تبدیل کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/144693" target="_blank">📅 10:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144692">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/794d812382.mp4?token=EZyh2HlEuX3izFDHrRKya5im_zTKVYI1izmsYhOGEEHtY2atj2bUCdB7x4pEl-lA75uPY1IKv4MKbzA8_P1DXPu1JSWCGseuQAxtYVqFll8czeSE350QpsBeWo7uURQvznzI3dh_jT6jjQmsL8vFvDZdu_jxOh1PR6W29Inh-nbR3fRhXGzf0uT9uiJXDjeoHfSSw80bN1d8e-wUVdVW2YuANEjRD6I_8kyqxDAsB-i3J-recLT-1MvWxzJux1Bp3z52dFhTx0TkZ55A7xNwsYU9ojxY_ubbK5ikYRoE4H9-x8G3dbaH6P4tY570O7EBd-jaCdZVpjyfeai1u7ouIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/794d812382.mp4?token=EZyh2HlEuX3izFDHrRKya5im_zTKVYI1izmsYhOGEEHtY2atj2bUCdB7x4pEl-lA75uPY1IKv4MKbzA8_P1DXPu1JSWCGseuQAxtYVqFll8czeSE350QpsBeWo7uURQvznzI3dh_jT6jjQmsL8vFvDZdu_jxOh1PR6W29Inh-nbR3fRhXGzf0uT9uiJXDjeoHfSSw80bN1d8e-wUVdVW2YuANEjRD6I_8kyqxDAsB-i3J-recLT-1MvWxzJux1Bp3z52dFhTx0TkZ55A7xNwsYU9ojxY_ubbK5ikYRoE4H9-x8G3dbaH6P4tY570O7EBd-jaCdZVpjyfeai1u7ouIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: عملاً الان فقط دو متحد برای ما باقی مانده‌اند: کره شمالی و ایران. خیلی‌ها می‌پرسند چطور به این نقطه رسیدیم؟ چطور شد که در چنین جمعی قرار گرفتیم؟
🔴
‏لاوروف: مگر این جمع چه ایرادی دارد؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/144692" target="_blank">📅 10:23 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144691">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
آتش‌بار توپخانه‌ای اسرائیل، شهر المنصوری در جنوب لبنان را هدف قرار داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/144691" target="_blank">📅 10:17 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144690">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t7nhC317DY1ikVGXQ79R6ii0eNvSUbaya1Ac75L_EMjnrkdWgBkODY2OOaTDUFqdxztydelbLCN87KADGH9pUi_UpZVl3qDlI2thRff-Jq7tCiafO72gl7lAVYUb9lEB1R8ZSKARjgQRhrSCsyr8UOo9YXLj4zI57wU-L9DxXSNnh6A-9MyzVgrZAqW70WcrKefkG6AnizKkS0JqFtfVGQiQ-hyXzzTwMQXc9ZU4o_MtDIgohAaojWneTfCGjkMCBfHkK4v7b7FIbayA6K3S-U8Wuvu2HfqZkf-xpo_WCuBX1hTI8C9GbAeFZY550LBMyNbOg0gVn2R_CWcaLnKh-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان در بیشکک
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/144690" target="_blank">📅 10:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144689">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
رویترز : تعداد کشتی‌های حامل کالا که قابل رصد بودند و در ابتدای هفته از تنگه هرمز عبور کردند، به ۵ کشتی در روز کاهش یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/144689" target="_blank">📅 10:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144688">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
ترامپ مجددا اعلام کرد: ما میلیاردها دلار به ناتو و کره جنوبی کمک می‌کنیم. وقتی از کره جنوبی خواستم در جنگ علیه ایران مشارکت کند، رد کرد. این موضوع را به خاطر خواهم سپرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/144688" target="_blank">📅 10:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144687">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
امارات مدعی رهگیری یک پهپادِ آمده از ایران شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/144687" target="_blank">📅 09:58 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144686">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc01c3c573.mp4?token=Pq8VR9PbBb_7H12gZkxOWL2W18SAFZ4z7xFE95oQvKdeqjA4PqUxyX-l7_lawWVsrabJONkAcZ98A32bB6aterl2xUQEeOvZqR4S7LKQB-FSDCYW9JbqueVvoq2YDSo75X9Z-GCUqb8ebpxzhMUtXQmxaYPsOmbaL7XZCrW3M_BTDg7CD-EaC0CRB0D0uxPaiaecxKuMpgIRSh3XUw1pe_xZQaLEWOFi9wsdgQjehngQa6U2-VZ7F7V9ahSOWMKZHhhsI0bpf5DbmgL3abqEJZoZi-hfrh2sYzgLKb5MNrNoZZCxTKyMORm96ipNLbex5T3J-YH5cwmjA01kmU3j6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc01c3c573.mp4?token=Pq8VR9PbBb_7H12gZkxOWL2W18SAFZ4z7xFE95oQvKdeqjA4PqUxyX-l7_lawWVsrabJONkAcZ98A32bB6aterl2xUQEeOvZqR4S7LKQB-FSDCYW9JbqueVvoq2YDSo75X9Z-GCUqb8ebpxzhMUtXQmxaYPsOmbaL7XZCrW3M_BTDg7CD-EaC0CRB0D0uxPaiaecxKuMpgIRSh3XUw1pe_xZQaLEWOFi9wsdgQjehngQa6U2-VZ7F7V9ahSOWMKZHhhsI0bpf5DbmgL3abqEJZoZi-hfrh2sYzgLKb5MNrNoZZCxTKyMORm96ipNLbex5T3J-YH5cwmjA01kmU3j6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اداره شهر اودِسا، حمله به یک مرکز پستی "Nova Poshta" را تأیید کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/144686" target="_blank">📅 09:56 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144685">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
پزشکیان دقایقی پیش وارد بیشکک شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/144685" target="_blank">📅 09:52 · 09 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
