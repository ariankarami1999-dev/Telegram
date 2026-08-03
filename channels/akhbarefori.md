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
<img src="https://cdn4.telesco.pe/file/jG8lb3WrLKFdL9tZMulcP6Pi6-_bKDPMzqvTsBq4TLAj2tALaDJCEtYI27Fpln92udpfY-TVzldOw3twUQWFH6TEQyiMYGtGyvOvsalMrk9Schd5m8AF8o2BD2HjwViiRHoZlsfKIyTA5CymoHdTL6D8vPam_a4Yow9fffSYuyjoIuaW3BZT0wcld-mOOy14uSvCkyNQjWKGFGXK5q6ZctdloOFqwk77motg4-cqnvAzHDYswGtk3OtSOSPhTsxx-kxni0weC4ZCph3j_Ob8GEE-npklHVOeCzC2uYqrr8pFLtkgQDBBWwjfrIeggQq027KdTYCtQr6qI427q48nDQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.05M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-13 02:23:17</div>
<hr>

<div class="tg-post" id="msg-678237">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e81c4a381.mp4?token=KoTmwnEj7g-lVgEPIelqR50UMKcxKu_L3l7CusVfPB4zS8b9I5hNkpm_SFXmg2PNuWCzDKFhflUdOYDJ_lJl_Fo_tXosDIMocZQN5s785oubfT9Z_Dk7RPPt2eYQhGaljrCjNiFNEwwLXaejCv5HOZF2NIWMVgKXwj4pjW_0sGJGxA4CQ9_tkPkOsz-D7sCaX3BN3C8Xf0vg-TeZrk8OH1JHq18CVYRb8Dw69OfS43aNgGBFxXVVXweoKqOHC5XVAdsNzsemvWtgmyaRxyHNWoT5UJl_ZWKT7tdUhuMA7UpR-0dTDqBnESzgKT7KY6XE0Xj2kkCwdmxPUJPe1lKZHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e81c4a381.mp4?token=KoTmwnEj7g-lVgEPIelqR50UMKcxKu_L3l7CusVfPB4zS8b9I5hNkpm_SFXmg2PNuWCzDKFhflUdOYDJ_lJl_Fo_tXosDIMocZQN5s785oubfT9Z_Dk7RPPt2eYQhGaljrCjNiFNEwwLXaejCv5HOZF2NIWMVgKXwj4pjW_0sGJGxA4CQ9_tkPkOsz-D7sCaX3BN3C8Xf0vg-TeZrk8OH1JHq18CVYRb8Dw69OfS43aNgGBFxXVVXweoKqOHC5XVAdsNzsemvWtgmyaRxyHNWoT5UJl_ZWKT7tdUhuMA7UpR-0dTDqBnESzgKT7KY6XE0Xj2kkCwdmxPUJPe1lKZHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رسانه‌های عربی: صدای انفجار در کویت به گوش می‌رسد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/akhbarefori/678237" target="_blank">📅 02:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678236">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N3Hz4oBjrt53vtpCFX8460OrJ0vl3ROX67_RTJZPpnhWbaNN_JGUU48TFMFnkPqayd2q5oH0hJk_FjS9_ZYFhj9cUv50f18cgaOMXK-6RmSmjRnV3eDrNJAnoPoUoX6bSGHOOoqs7v3fIfJn1etViAzARntFMVKw21kvV5k1PmXUMcacntxzKhaRv_5LsGbXyECsfK5uHfpG0FwPGCrhWYRqQLnY-_e4XVuGrsgKuZ035YKzbr3saqmjB8G4vyhIUIxciobZjnTuwqBoZhrobqUjreszZyXJObWm4dba-t0N63Um49RLji_MLIh8AnlGIWk5MssIgRlFHiEL8Y70LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زمین‌لرزه‌ای به بزرگی ۴.۱ ریشتر، ساعت ۱:۴۵ بامداد حوالی فارغان در استان هرمزگان را لرزاند
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/akhbarefori/678236" target="_blank">📅 02:11 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678235">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
تشییع پیکر بیش از ۱۰۰ فلسطینی پس از سه سال
🔹
پیکر بیش از ۱۰۰ نفر از اعضای دو خانواده فلسطینی که سه سال زیر آوار مانده بود، در منطقه الصبره غزه تشییع شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/akhbarefori/678235" target="_blank">📅 01:44 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678234">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
زنده بیرون کشیدن یک مرد ۴۳ ساله از زیر آوار،  ۸ روز پس از زلزله ونزوئلا
🔹
تیم‌هایی از هفت کشور - ونزوئلا، شیلی، آمریکا، پرتغال، کاستاریکا، السالوادور و مکزیک - به مدت سه روز به صورت شبانه‌روزی برای رسیدن به این مرد تلاش کردند.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/akhbarefori/678234" target="_blank">📅 01:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678233">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a35651a1e7.mp4?token=BpWAqYpp9Fg-A3OnMPHCzRNdYtjzmIQC_t7-zPapDOTkPd6q8wRrM0vAOE1no8AI-Imjl0EbmlnrMwYj-COmkIAa4ND7KYrvGw2mrUUj2Qwth-dNpv9VEv6z9uw1i2fbkYH63vgNF24jylAjy0Xzmx_wKqDE3R9lkNB19Oh9yMY-7ExyamlELHUHn5NYCt8_DPByhH4_uDV07tKtcPF1KcGWnfn3M1giaCvqy_Oy2gQrcCXNgHBwNUnrr23BQqbXDQ5Ac951pGpif7sxzXvfJu3BzxjxLQUwENG0HKUPVyZRPW0zywSCKsnPnon6mho3rwVAa2YPUMbC49H5eZMAjYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a35651a1e7.mp4?token=BpWAqYpp9Fg-A3OnMPHCzRNdYtjzmIQC_t7-zPapDOTkPd6q8wRrM0vAOE1no8AI-Imjl0EbmlnrMwYj-COmkIAa4ND7KYrvGw2mrUUj2Qwth-dNpv9VEv6z9uw1i2fbkYH63vgNF24jylAjy0Xzmx_wKqDE3R9lkNB19Oh9yMY-7ExyamlELHUHn5NYCt8_DPByhH4_uDV07tKtcPF1KcGWnfn3M1giaCvqy_Oy2gQrcCXNgHBwNUnrr23BQqbXDQ5Ac951pGpif7sxzXvfJu3BzxjxLQUwENG0HKUPVyZRPW0zywSCKsnPnon6mho3rwVAa2YPUMbC49H5eZMAjYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درگیری لفظی بن‌گویر و وکیل آنروا در جلسه دیوان عالی اسرائیل
🔹
همزمان با برگزاری جلسه دیوان عالی رژیم اسرائیل برای بررسی دادخواست‌های ارائه‌شده علیه قانون ممنوعیت فعالیت آژانس امدادرسانی و کاریابی سازمان ملل برای آوارگان فلسطینی (آنروا)، میان ایتامار بن‌گویر، وزیر افراطی امنیت داخلی رژیم صهیونیستی و وکیل این نهاد سازمان ملل درگیری لفظی شدیدی رخ داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/678233" target="_blank">📅 01:04 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678232">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ixPeWd8uLTGIGkriOZGomrQ7SfvTAqg96HHOBOkRD74aVJY4GuLv32MdPLuUXkr8co62vHmUAXoynbmTwCCH-9P4GbctNd4YWrCQ8dIxomFi-iAi0Gvep3ryFT-K2jf4P5qIgkdQ2Yqomvr0trFK-r8eIZ619PDlke4EXwANJSYyuAXnoZoVgWgnsQAt6n_cq6emSk6sGSOX4QacUqGkWdVHS8_F6eBnEb2Ju-Ik5kQR8FcWnhLKOOO55MO-uI90OOc24H09TNK_PAO9JNO9MWk0kgHJwY5EiM-R7CAzg_uX6he_YC4ZFcrX960k49OgkFAqoAGX7-hvjf9o8Mo0lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ویل شرایور: ایران ترامپ را در گوشه رینگ قرار داده و تنها دو گزینه تلخ برایش باقی گذاشته است
🔹
وارد جنگی شود که ایران می‌خواهد.
🔹
شکست را بپذیرد و منطقه را ترک کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/678232" target="_blank">📅 00:48 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678231">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
سرلشکر رضایی: به‌هیچ‌وجه اجازۀ بازشدن کریدور دوم را در تنگۀ هرمز نمی‌دهیم
🔹
اگر ناو و نیروی نظامی هم به تنگۀ هرمز بیاورند آن‌ها را هدف قرار می‌دهیم.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/678231" target="_blank">📅 00:37 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678230">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
تمدید تعلیق پروازهای شرکت آمریکایی به اراضی اشغالی
🔹
شرکت هواپیمایی «امریکن ایرلاینز» آمریکا تصمیم گرفت تعلیق پروازهای خود به سرزمین‌های اشغالی را برای سه ماه دیگر تمدید کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/678230" target="_blank">📅 00:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678222">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I5G-NsNYzf0Qla9OngXNKfAQErBWTtR9_MRn4fIROaPrZp_b9TpbK-MBzD8PBexci96WwW0Oey305wg0Zvxd6iBPywGcAsVasUOnvgRJ5JRQbOK3R6wGGjYN8A1M92c6kVd8wTpw2qEBNJ4L_y93gDb8n0kCAzZkDtkULxiA9vkzQsLWKfoH7GGW7bgJJ_0yeYBrI14rIRXiabyyiHl__zHoh8F4-VYohh635sUC1E_g3G3UC7Z0xZiCXeEKl9ln4soWwJfBR8XLjJJxH9YKKa4rPLYwHP6Zf20aIjSKP3ac1H5ExPhsOxmPVHIAk35lU9PbR0RJWzCUkhWh0SAOOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FE-8qJAVENfhUOusg-Sc7yL4ZONEFGsx8rZeD8uqCTltfHaqS6q0woabSSlllRlgTPz0Czc3bdBS958_JXo5UAdgamKNCuTNwnCWCXwFbCpAeIdMxNxzJ-IWLKIVvuNdMI2H4uSVLVAyG0rBIcVqq16ky95OcPtRXIVaN6ReYGQ0KQaYcOClhYhHzCzC_16DE4B0lJX6rajvXSvd7Rjo914BQ6Y-_yVuyHGlCEAdnULhbGz20aZLZpyDr7xGx81Y6LJNI6DUAwAzE8YbSEM26rekhzkzECg_8PCFNnGoYDqR54yrXDwXCFiNiMHwOZdHtM9qeRRVPrH8F8BebyIvfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IANH7PBdnaYurEBPELhO7OkSG1BHrBADkYl3xqhEWCW4AHZRxZJWLGd7dgHXcLlz5WzqO9-yCAbU88Iaz173kJ8TYBsHs5vcyf9_aJrAQVBx64cDAtzHjQaMygZYeqs0peSfq8Z82QKa-JYR90feeLvdVqDePsBQZiveEPym-sRaNG8kKnGA8uRq3GXw1gqtQZ5luSV-ZAgaiBs8xNxaNvhJvD5BGzouft2UjebRHnWwB9N_JAErgRvyK3oNc0CccwAbBossQ5IntlUf8WbVO4gRhv1VqLvFqkPhln-nRkMS9Xu7dqrVITY-q7RWest7066U9uMccjVNAt0h2iwcJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BmLXMYoP0dNFUX4UhXk96eMaoN4qU81IBLrvGSwM25EEc1zljpQciaTuK9qlT24cU05I057eg5ST0EgNwTgGB9uc4Cq4ICR1vLTzTl-fqD1qRszv0s1uWZkPXkBwuTznB5-zUtJv5vB82Sg1BNd2zer454LWzPecSjzvvOdy5dEkGG0NKypw5jGChXIAM3nj2dnC0841zGQDk79dO7dRSFrJ2lz9tSgQMSBKF4gIizkRDijuQA7oUrPITpc4KF0NZM5_UlZCJYrsHIfYaQe_XhpePz7nnPwljCMCrfMJjec1JYjMs_wmhfTiKVfTmGQdiOBmg33Ume86HJ8JSFPHIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lhC2eU9yvq9jbenYm786An0-Q0pRzpMZHPgYnv-mxqmuggbD00OZ_THqmtaNWbMYQ2FGXpn_wOvMQCs7wG9zWgKoKmXgfhTNIKQeXB1RKHI0EBRuaqiqcxiLqUb3Sctlj2BqVGzFPrVS3YxJpfsSYOuaTNISHKhlytbz3riuLaKkha6WGcTpNzSwLKuVYFKbAdVm3sfqTz85PgA7zCMfA9SvyGGLBUySHsWd57XDfQmDLTvGTp1rnRhbry0rx3Ir0bmk8Qc7SR5VMor0Cyged34Zq1OA6NLR7R08CF_2lzPDp1L_IBXpONrcYKsck-6zOiSc9v6hcXMP_fBRZe6zKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eii4MjWcxVc1BovOJXKTdm3s9J-7UoTYKB38blTD3Oj_VK58Vk9uvXrxD5MJmZ7JEht6dU_j_-6VM115B9b73CsVlwBpxzIM45kyMSwfWsZ3PVRVxUxXeaeHLtUNKSx-rmQcAxMDmPSUwsgfWlyMhZbV8vsW4PA-CXIURVU2D-xJx6O9GHUyoqp1OEP6-e5Ke9OUKeGIxFNNMMsDXM0HJAyzwkLJggl4VJyTZcOOpj58huZgjIRIJFkQb3-rekd-asv20lnGvClwJBBITHVw2wWPGIwGlyy3bwZXQn4tzgXRUytmjMAXpwEjNfbOpWvu852l-_dV_8AnRW3ozfGcwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gh36pNXqAjaWcbMifKUOumFgElKhv6kmLQUCAzswjDLUH0b5D7B70vlIH-210l9sBsYxanrj3n_wS1v3UEGW004yii6k2JapLaddokfNt6GSS3cfL8WC_H-KDhXNoz9nT4GeNL_XmQGlFHgjw1UIQJTFXDx0JGhqT-p3D_AQfcxrKssmX2mbt43cXfYliT9nPCnUUYO1oFmZf_oW0T6xlWI2iyYmqP78FvzF5RsycbxQVQd8v4aizkViHLS91s3l2c5CPE3szXyVo53mV44BAd0mkIKXuw_IIyDN8-U37phdIxbNK0osvcyav1iEX1Yn9bsBIGHOXxnTQHl0Wlp_Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OOIZx9X6fu-ogyqklgCg6ZVvV5oO5CL6LbBK8vkemVyZjjiqWYQW0eH9WeFwyVv4Ww9KRdoee9Raew1-Rv9Huhep1HL204mc09E-7qajUhplG7c2hzT3QKKHCiiNQHwzTkeHPs3xZs7jIgdJkHI95lDOdM0C1kOhVF6v_npP6KZ0cGNGKueyIKDzy6qn_snqCNHK99fQEgHfdY1PZZp-SuLvIjme7EG68BMNjZpZjGC_KW1kequ1kulUdW5nZvyvB-7KJ2Xs6qbLZgqoDIkdtzzsaEk8dl-gYMS92iSb-GzhHGXdm3mHPZeLIcwE7-2aWqUJ-GD9MpuZKQC4eaTH2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💫
روایت یک فرهنگ ماندگار
💫
✨
آنچه از نهضت حسینی در دل‌ها ماندگار می‌شود، تنها یک خاطره نیست؛ فرهنگی‌ست که انسان را به مهربانی، ایثار و خدمت فرا می‌خواند.
🌱
#هیات_قرار
با همراهی شما مردم عزیز، هر روز با توزیع گوشت قربانی، این فرهنگ را در حمایت از خانواده‌های حائز صلاحیت به تصویر می‌کشد.
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇🏻
@Heyate_gharar
شما نیز میتوانید در این کار خیر سهیم باشید
👇🏻
5029087002135690</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/678222" target="_blank">📅 00:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678220">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYQFgktcsYsN0lmf8TvGxCFvW-tVeIDgK93jyyQ3fCL5CzL73uV6eFjKJX4DMe4JXrWXhqcyjiN7gK3VIofqPUeBKObOGiYQw_vfXpzMwUwMxbowykava7u15U-NXT1rpDLGPFpUMcC8eND805j23WLhuTN23XYRdyqgrisArjtgHu4WRi7_YeF0xFCajJFXIEQIl0dr2n_9x6WBp9kwI7KSNeI6-5Yggug3tHzrPAcsZmJQkOEgtGRbI0a5uIMKMCZc9QPYaWEsMAId4l_pNQGFztj-f_CzxkIBdi9yXhHrcWAOEeDzsRCOiBq6ejQLx3gSHReURV0L9Io0IWjXSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ جنایتکار بار دیگر از شرکت‌های نفتی خواست تا قیمت بنزین را برای مصرف‌کنندگان آمریکایی کاهش دهند
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/678220" target="_blank">📅 00:21 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678218">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RwYdSh-v9jKspQW1v68-wRePX9GW4LDyHSRrIN_NelK8FGhJffc5TxkFkukHnDeHE2nRzcxeX4_G02pYPUtJSKS_A8gaZ1xpb0KiZ94lV6fQKken1zcO0rtzZSTLW4U9oMfgM6Mrz-7l5Sco7BKCPb5VpKgETQ2IV4tMP_UEhZi5IvlZGC-JMqi6JgXQ2yzLUCrgxFW0anpPOzdacu8XLMv7BvNPWQbN52ycGoO8CgFVT2u35p_RAcWLfsDFtUtmJlj5JOHCUzIQZu2NaiqL2EjQXFNrdoIQZxp7mCRQU7i5MhDpZ_OYBfKJCZGRar_P_1JVLzwYE1-DfLevlnJNvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CZgsPI89TyGw1VsR2TKOm37dgAWu2EoUlP0YdN7LmbPg7IlKiN0OeBePn9698CW2XfQE9L8zSCehxlCaKgPkBc13vC2Nu7mF0NE-0Xpe3S4f-L8BjF7Z4yNBzwSZomudD3sYqINaFJ8TIf5qq6tszU0MRFTg9SZow4SQVPdRI8L1l2x9HDx8XlhH6GxbxR3UHWtbK3Ap7cC5uSs3jTYSZpNsjdWeIGULLI7pj8GwqXTPw59eH5p3vjTo5A4JVMTxhVZ653XGIEIRIUQyQkw_Y7VT62YRQa39OTzsemBWyaWfUQgRdi3L1TXbBtVW8_7wmsywO83OjNTfRZV7QieKlQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
فکت عجیب: اگر دو، سه و چهار انگلیسی را بنویسید، زیرشان یک خط افقی بکشید و صفحه را ۹۰ درجه بچرخانید، دو، سه و چهار فارسی می‌شوند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/678218" target="_blank">📅 00:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678217">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lP2rI9EAA4y3H8kkccDEtb4ZhzNhdQHbtR8VWfFE6J0lAN7870Mj4mOeNMHIb7fCyzPFMO5RbiWI6ZElZb5CJWfXBs2YkLeVt_k7pjB_lb6jFYzZTvYrSyObkEeZCDUDPUeeQI-XyznoreBPeiJi8oGk9TmC1-NEPwuIzbw1qX--KWokroN3P3tL1RKTkBP_Qhy1AKscu5gzWtwtYkFIbb4gfTP_EeuA-Pa2zeuLyhOO3JhrTcnGzkgpYw5ebskywml3yBo9md1dqRiSLDS6gGjZGlQU3V3nMaxGLQ2puCqq2xE8FUqplTyJUaQNGs4fUR_H_eJKVPR7KKxLLj9hqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران و العراق لایمکن الفراق
🔹
اربعین امسال، در سایه تهدیدها و حملات نظامی آمریکا، جلوه‌ای کم‌نظیر از همبستگی و وفاق ملت‌های ایران و عراق را به نمایش گذاشت. این راهپیمایی عظیم، بار دیگر ثابت کرد که پیوند دو ملت فراتر از معادلات سیاسی و فشارهای خارجی است. در آوردگاهی که روایتگر ایمان، ایثار و مجاهدت است، میلیون‌ها زائر ایرانی و عراقی، دوشادوش یکدیگر، مسیر عشق و معرفت حسینی را پیمودند و با حضوری پرشکوه، پیام وحدت، مقاومت و همدلی را به جهانیان مخابره کردند؛ پیامی که ریشه در فرهنگ عاشورا و مکتب سیدالشهدا(ع) دارد.
🔹
هشتصدوبیست‌وهفتمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/678217" target="_blank">📅 00:07 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678216">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
الجزیره: ایران تعیین می‌کند چه کشتی‌هایی وارد یا خارج از خلیج فارس شوند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/678216" target="_blank">📅 00:07 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678215">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLWxoZP8fv_whts633eZ3jVfH45N6duJomHODVkgrenyHUPqIbtQS3cjL9eyBPEU97nELEbIXXTAeiymcKMiD7tNB3h6_PqmvAOEt1d-vCX1WnNrBpAuyABWjrhWxriprH1CU--714UuKz-Jhkl1aCY-H9MDI5QwiMLzTHpG1w6gZJp5TJ2yXR5ZM0Y9ygAdois8lc0Vz72tX_O52lt21DaxN87PoUR9LA3y323GSXhmDbU9dbI6VefpBMeCjpZsaLmiIhIim7A51-aOKerdyNYbDQNyFg5c27NqXCXgty16kBr8MaNCWd8DBN9tEpsfv_ydIbvjy0K-2KgUjbvZZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استوری اینستاگرامی علیرضا بیرانوند در انتقاد از بدون تماشاگر بودن
دروازه‌بان تیم ملی و باشگاه تراکتور:
🔹
فوتبال بدون تماشاگر اصلا فوتبال نیست، آقایان تصمیم ساز حالا نوبت شماست که خودی نشان بدهید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/678215" target="_blank">📅 00:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678214">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQTGa8mb_x9-Emv9k_yQD0PBQ16S_22MecA9qiHwoFxJF0SePHYkrmN8615bc7U7w-4Usd4yJF6ost4XNE5a_dgOUyuMC9jNTJ4Ai05yaOW6q-vvqbn5I3qJW3BDRI8NiMCmygx0lqURba_S6frWGtBdBeJF1OGDiQzJo5TTgkPBxO95OShA5Frgj_ehaQU0ibA5RAoWNRUAH21b3uE82aXsLjB3y2kTUR6tjxI_AdthjD-free9JeX3PJaZKlpXOGCyno9YviIQ05AqbRQK4rStB-DoUfRh_YnthckUvr-GIP2WbBlY4sKHDrD7RtTH6TlXX3BkDrmH7Q0sKjDClA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معاون ارتباطات و اطلاع‌رسانی دفتر پزشکیان: ادعای استعفای رئیس‌جمهور واهی و کذب محض است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/678214" target="_blank">📅 00:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678213">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VuCbXT0UkMaEEf9J09OqShLquEraaoz04XSgqfc3un8as8QVDMHPsDRKxFGmp-AdcOA6kKLAi181F6hj7oUzPkZXlRWNdq9b2NgEBe-I5fmouf3CX6jz7XfJTGha-b5JTjw3Osk01NjNrBkGVo1KuNNSQ1ucvssFYGq9CAxjVuD_IJSdq-axHLetJkZCkdA0UC7z1x0dsKq-H0nRGB5U4Y2CL8c3Eb9vODS1EX_P8fQrRjHQS9RlyID_JgbKa-nX_Vv_kBbN4fwleGeiILIsunQtcV-SJKdWkGPF979siQkraTgQnk7SAbJqS7t8yt1KPL5pG_XVf2rI2N9TCfM0wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/akhbarefori/678213" target="_blank">📅 00:00 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678212">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LhZFJn3sZ8mBDMJyXav-jBVmTbLZz7J0XljSbsRFBcWaxmoP_dEADsfXGro2OzM339o8F_nxaSFLvhzfwA1BAljISMqxkkvdRCCHLSfhZ48a2-5zFEmJb03OuXjiFYEfdnZ5OMK2qQDanZ-vmACTu0cS9EU2PdC4unQC8mScMAJxnITpcGqoDD1g4mls_xoIyt7xWaJH8NDX92Y_M5TiLMHiXEpSGvNm5ZX3eTlMeGZfXoIYxBo0gRJYumMxMch9e-ewncA87XDDXItJ31hriZdIFWqZi3rbHfFepASxumj3s8vj3noOgLBL0kU4YLFnb-W07pQtLTOMa-ZcDOWTwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
الایجا مگنیر، تحلیلگر بلژیکی: به نظر من، سنتکام متوجه نیست که وقتی می‌نویسد «۵۰ هزار نیروی آمریکایی در خاورمیانه حضور دارند»، این ادعا تا چه اندازه مضحک به نظر می‌رسد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/678212" target="_blank">📅 23:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678211">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75331f2505.mp4?token=iARbxPeyiQUA7lVsaflvuYimh_cKVL-8J3y7yrCAtwVyNs7RU-ke6tvfpqz2zkmgw2ssnRtnAVYDABDkorNJqh6SGny44kCA9x_y09z6a-I-Kpvzf7rNj7Q0j2gNENJb6ILUhq09uH0ga8rgO8mBAgkGSyZxOD9NzRMKWprxo-ooqplUaa_yaPCD4DIsjV61LmBiYLBlF3pSvcv3SSkaxk4y3c4I0601wl5ik56WIHgBM4PiBwCrvG05h2uPb9eYVfuuIiJh-_r2JpTECdfCqSU78N2V-ZAkD0sZ6q75xhPSPqg0Pnp75SQg_eZE0SSctNjnDwRw9kVCXCrnYTsdWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75331f2505.mp4?token=iARbxPeyiQUA7lVsaflvuYimh_cKVL-8J3y7yrCAtwVyNs7RU-ke6tvfpqz2zkmgw2ssnRtnAVYDABDkorNJqh6SGny44kCA9x_y09z6a-I-Kpvzf7rNj7Q0j2gNENJb6ILUhq09uH0ga8rgO8mBAgkGSyZxOD9NzRMKWprxo-ooqplUaa_yaPCD4DIsjV61LmBiYLBlF3pSvcv3SSkaxk4y3c4I0601wl5ik56WIHgBM4PiBwCrvG05h2uPb9eYVfuuIiJh-_r2JpTECdfCqSU78N2V-ZAkD0sZ6q75xhPSPqg0Pnp75SQg_eZE0SSctNjnDwRw9kVCXCrnYTsdWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازداشت معترضان به جنگ علیه ایران در مقابل کنگره آمریکا
🔹
تعدادی از روحانیون مسیحی و فعالان حقوق بشر در جریان اعتراض نسبت به جنگ علیه ایران و ابراز نگرانی درباره حقوق رأی‌دهندگان بازداشت شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/678211" target="_blank">📅 23:56 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678210">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
محسن رضایی: شرایط کنونی ما شرایط گذر به قدرت چهارم جهانی است
🔹
وحدت‌مان را حفظ کنیم و اختلافات بین نیروهای انقلاب را پایان دهید؛ نباید نقد را به سمت تخریب و اهانت بکشیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/678210" target="_blank">📅 23:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678209">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d92958e1f.mp4?token=QHYQHoNxFtOIKCotlRuIMX-zOOBUSjB1-T2LP_IBVlhA-90NtnR-4_xTeLn4b2qOzZMaxf1MfDUlQxXIVdhTtKx10N5ruG8L4l6GpkkL_XqPaQCCdrZ-J5vgo8UN-r24yDJSTDzIxjN_AKH6SewGEf1GK3XUZPayHRoHb87Y2xlnZIX0rxFpMvLTC9uNuddtNqYbxv504NWGIwl81QMDMV24adsX6GbbJn6khbcQBALPRSugUIXW5F8MOKUX2wyb8kX2zBYAMHvxzgoq6mrQy11DNqrtMYjiLzADKe01Io1v4pVD0WDGdKYJ3mhfCw037Kzo9lL8bU5OECOAFmAcKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d92958e1f.mp4?token=QHYQHoNxFtOIKCotlRuIMX-zOOBUSjB1-T2LP_IBVlhA-90NtnR-4_xTeLn4b2qOzZMaxf1MfDUlQxXIVdhTtKx10N5ruG8L4l6GpkkL_XqPaQCCdrZ-J5vgo8UN-r24yDJSTDzIxjN_AKH6SewGEf1GK3XUZPayHRoHb87Y2xlnZIX0rxFpMvLTC9uNuddtNqYbxv504NWGIwl81QMDMV24adsX6GbbJn6khbcQBALPRSugUIXW5F8MOKUX2wyb8kX2zBYAMHvxzgoq6mrQy11DNqrtMYjiLzADKe01Io1v4pVD0WDGdKYJ3mhfCw037Kzo9lL8bU5OECOAFmAcKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور سید عباس عراقچی در حرم مطهر امام حسین
(ع)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/678209" target="_blank">📅 23:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678208">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8017aa4184.mp4?token=gWuTjZx8twpQOrtounSut6r0-mjBr2LtRRCRSSHQACUh4hOttrfoQo3N6unYQ4t-iSLSrIoFGWr_Mki1u2eUIofYQgl9fkbr_g-atSLgh1RJgAVzARC62dY7uMjPV6RbX6BJaviM0GJTSUE1N_-1c7XkfD7HR_TMzeCUjgHiKdDHfuHhRZIQoHszS49SR80REa9tIOBlsocjSR8RZ3zE4qjEU_8qjSlh_faD0Fe9z9wr-a9DjPlsHb_BKuUu8n7cbUEa8VbcxyNNpreoLCIeaCTlma3tyzuLNRgQwkceJlA2fc809rvZ-R6yk74e8JOJedXNWBrnJw0-KQv669hPcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8017aa4184.mp4?token=gWuTjZx8twpQOrtounSut6r0-mjBr2LtRRCRSSHQACUh4hOttrfoQo3N6unYQ4t-iSLSrIoFGWr_Mki1u2eUIofYQgl9fkbr_g-atSLgh1RJgAVzARC62dY7uMjPV6RbX6BJaviM0GJTSUE1N_-1c7XkfD7HR_TMzeCUjgHiKdDHfuHhRZIQoHszS49SR80REa9tIOBlsocjSR8RZ3zE4qjEU_8qjSlh_faD0Fe9z9wr-a9DjPlsHb_BKuUu8n7cbUEa8VbcxyNNpreoLCIeaCTlma3tyzuLNRgQwkceJlA2fc809rvZ-R6yk74e8JOJedXNWBrnJw0-KQv669hPcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر هوایی از حرم سیدالشهدا (ع) و حضور باشکوه زائران در شب اربعین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/678208" target="_blank">📅 23:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678207">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0f8294db6.mp4?token=JuwG81yY5bYAQeepzXflnCONUz-eheJY9dUggw_ua7cEqbZWZ37kRyjLClpx4xO99Vz6JE_UPjPkPM5yFzpQskB7vBVtKWmZ4atRYF2IDxIS6XVDz3_kunhOiPOXoVlxeigUr9Dc7CEKwT1NViZElN1-_FydiCNHOOHaCJmmqpvYvzB_eZ9M2bN1WlrYydHzPBMDtSKB0q9QzY1kfy0W2bH2-hDVx0serq25G6ybLLYbXEF9RCdp_40wOcavgF-yUezpYEOVH6i1xcoPmi6lia01ooZ6qWWDjpRr9RSElMfyYzDOfeYq-RxJI47OdumDj9njHQuUJpQuYLwwEJtxs1kfESmKa19OYvP8bPPrFzkKLktVKcjdjOuCh6uANdAky-Eat33AdUGgFq6gpMk1_sgDU28zDvQkNEl259Dt3X0Mnjbhrdz5bJqLdW4v_gYmgKQ5F2RWSCB8AZsdsIwRd2trCzIN5irwc-9ExwBqsewmpz8pJD-uPnPZ_F2gBy8LE1G7rX1pkeaRlK3V8dFFUr3PrSmsUBthTyiftyyKyXRZ1l3Vx3RRcJXnV2FQ0EV8b3EaFlyCgI-nGODOXijW82CSB3vHhrfBqrU-rFxyW2JqZRxd2Bm909KNGtLu01b1qls93yiT9uWfmLQG-78YTkLwiDgvM7VUTIT_oa_T6iY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0f8294db6.mp4?token=JuwG81yY5bYAQeepzXflnCONUz-eheJY9dUggw_ua7cEqbZWZ37kRyjLClpx4xO99Vz6JE_UPjPkPM5yFzpQskB7vBVtKWmZ4atRYF2IDxIS6XVDz3_kunhOiPOXoVlxeigUr9Dc7CEKwT1NViZElN1-_FydiCNHOOHaCJmmqpvYvzB_eZ9M2bN1WlrYydHzPBMDtSKB0q9QzY1kfy0W2bH2-hDVx0serq25G6ybLLYbXEF9RCdp_40wOcavgF-yUezpYEOVH6i1xcoPmi6lia01ooZ6qWWDjpRr9RSElMfyYzDOfeYq-RxJI47OdumDj9njHQuUJpQuYLwwEJtxs1kfESmKa19OYvP8bPPrFzkKLktVKcjdjOuCh6uANdAky-Eat33AdUGgFq6gpMk1_sgDU28zDvQkNEl259Dt3X0Mnjbhrdz5bJqLdW4v_gYmgKQ5F2RWSCB8AZsdsIwRd2trCzIN5irwc-9ExwBqsewmpz8pJD-uPnPZ_F2gBy8LE1G7rX1pkeaRlK3V8dFFUr3PrSmsUBthTyiftyyKyXRZ1l3Vx3RRcJXnV2FQ0EV8b3EaFlyCgI-nGODOXijW82CSB3vHhrfBqrU-rFxyW2JqZRxd2Bm909KNGtLu01b1qls93yiT9uWfmLQG-78YTkLwiDgvM7VUTIT_oa_T6iY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عزاداری ایرانیان با پرچم‌های سرخ خون‌خواهی در شب اربعین حسینی در کربلا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/678207" target="_blank">📅 23:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678205">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
حماس: منتظر پاسخ رسمی و روشن میانجی‌گران درباره توافق هستیم
🔹
یک منبع مسئول در جنبش حماس اعلام کرد این جنبش و گروه‌های فلسطینی همچنان به توافق‌های انجام‌شده درباره اجرای مرحله دوم آتش‌بس پایبند هستند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/678205" target="_blank">📅 23:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678204">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49f726e8cb.mp4?token=DQluHcuOiC_6leRffmWTpxFxskbuK9fCzX1Ue4AZjN2DtRwxLFoUvtC5cEsB2ov7lhCmCmQokz6e9Joj3jW_gR_d0RVU1UQHnSd20aPbrqq3AUaoiHInO1MyKGB0TaNXgPz0n7zf7RAnvR6ZaPjpTP1JwVZvtJE5qa06bFPxZh_5pQ5oVqRQAngJ05pyrdgrctfECveT4LdGaclgI1_cDCxczch53JWk_Ezo0Zsn3-MmnvwFyVfQUf9QAMZCKRlE6ZBtjMF9RgNEZNOk8lsp8XTcGPk1FV4RymsxN6tww0RlhkPTAZQ_2YSniVoBSvPSiFn1uhjA4DpkeaIv_IhNh0Lp7onWw-rMYSh7kstidkWxPD4wrfhdWz2TnENT8U6wDoKssDruBGNykQBS-bBPG48sdc_Q3ikL_0d6raphuU1TEu6uWJYDM3W893tIfaNHqguvoZUb0RQ1TpfmsFWXNRy_ZnDcNn_-rNqDWFcf-cb9JoI5-zAvudLeAPN_b9t7mctTEOFhAElSJS2-1JmJIrHBCe65Em1lm_w-K9NmqTJVf8THAcb718dnRVfezUiBjmb6wNBoZdXdzQcPAXJICTFL5bn4civxjI4wOdd1PYBcY1wAgffQqHEW7Dn4IbJHaIZrQ1CKXbdW19ZLsIPjSHSFcKSOx9_TLTpMeSt_qU4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49f726e8cb.mp4?token=DQluHcuOiC_6leRffmWTpxFxskbuK9fCzX1Ue4AZjN2DtRwxLFoUvtC5cEsB2ov7lhCmCmQokz6e9Joj3jW_gR_d0RVU1UQHnSd20aPbrqq3AUaoiHInO1MyKGB0TaNXgPz0n7zf7RAnvR6ZaPjpTP1JwVZvtJE5qa06bFPxZh_5pQ5oVqRQAngJ05pyrdgrctfECveT4LdGaclgI1_cDCxczch53JWk_Ezo0Zsn3-MmnvwFyVfQUf9QAMZCKRlE6ZBtjMF9RgNEZNOk8lsp8XTcGPk1FV4RymsxN6tww0RlhkPTAZQ_2YSniVoBSvPSiFn1uhjA4DpkeaIv_IhNh0Lp7onWw-rMYSh7kstidkWxPD4wrfhdWz2TnENT8U6wDoKssDruBGNykQBS-bBPG48sdc_Q3ikL_0d6raphuU1TEu6uWJYDM3W893tIfaNHqguvoZUb0RQ1TpfmsFWXNRy_ZnDcNn_-rNqDWFcf-cb9JoI5-zAvudLeAPN_b9t7mctTEOFhAElSJS2-1JmJIrHBCe65Em1lm_w-K9NmqTJVf8THAcb718dnRVfezUiBjmb6wNBoZdXdzQcPAXJICTFL5bn4civxjI4wOdd1PYBcY1wAgffQqHEW7Dn4IbJHaIZrQ1CKXbdW19ZLsIPjSHSFcKSOx9_TLTpMeSt_qU4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جان مرشایمر: ایران برندۀ جنگ شده اما ترامپ از پذیرش این واقعیت سر باز می‌زند و در وضعیت فاجعه‌باری گرفتار شده؛ او هیچ راهبرد نظامی معقولی ندارد و فاقد هرگونه دکترین پیروزی است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/678204" target="_blank">📅 23:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678203">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
وقوع انفجار مهیب در حماه سوریه
🔹
هنوز علت این انفجار مشخص نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/678203" target="_blank">📅 23:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678201">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vVup0fv5IYrQgx_n0SWUvSleToy8kX3t5QaRgZIT84--RdJKmcoQjKZUVxinssRkj3GAeK4ZpLViqwodvKsUsb0AJRTkmdw2Sgqq44kfoTBcd2YhEQh7TPxNFUIaxM6z4zfBox4aHrMyNoj9M58E3Sg7HGc_LYXGcwCuP94hJgNLtureBP58Cyd9sjyxtpF4nE5kcAacUyWNgm7KwWaUD1atHEZvLT0uQdDVz8xKJ5nq5PUW1GI9rOzmaMZQq0n8cJGxbOYz-246gGVRlOByxXvkzSrB8pdkPdnTuVKbkMOTX0Mg1apGoM_GQU4wiDJKgo-1Ih5clbzSWxqcGTcxpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راز یک برنج قدکشیده؛ این اشتباهات را تکرار نکنید
🍚
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/678201" target="_blank">📅 23:18 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678200">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">یک منبع ارشد سیاسی در تهران به خبرنگار المیادین گفت:
🔹
ایران مذاکره ای با آمریکا نداشته است و رییس جمهور دروغگوی این کشور به جای پذیرش مسئولیت خود در به هم زدن تفاهم نامه، همچنان در حال فرافکنی است.
🔹
مذاکرات ما با طرف عمانی است؛ عمان یک همسایه ابدی با ایران است و تنگه هرمز هم صرفا در محدوده آبهای سرزمینی این دو کشور قرار دارد و آمریکا که تاکنون بعنوان یک نیروی شر و ناامن‌ساز عمل کرده است نمی تواند خود را به عنوان منجی منطقه جا بزند.
🔹
باز یا بسته بودن تنگه هرمز تابعی از وضعیت کلان منطقه است و قطعا در وضعیتی که اقدامات تجاوزکارانه آمریکا و محاصره دریایی و دیگر اقدامات ایذایی آمریکا علیه ایران ادامه داشته باشد، این تنگه باز نخواهد شد
🔹
مشکل منطقه ما، حضور آمریکایی هاست وگرنه هیچ کدام از کشورهای منطقه طالب جنگ نیستند و همه می دانند که خسارات دیوانگی های نتانیاهو و ترامپ، برای شان بسیار پر هزینه شده است
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/678200" target="_blank">📅 23:17 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678199">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔹
در لابلای خبرها، داغ‌ترین‌ها را ازدست ندهید
🔹
🔹
آمار دقیق از میزان خسارت جنگ در تهران؛ کدام مناطق بیشترین آسیب را دیدند؟
👇
khabarfoori.com/fa/tiny/news-3235347
🔹
کالابرگ مرداد برای این افراد واریز نمی‌شود
👇
khabarfoori.com/fa/tiny/news-3235308
🔹
چه کسی در جلسه شورای دفاع در نهم اسفندماه ۱۴۰۴ به جای سردار رادان حاضر شد و به شهادت رسید؟
👇
khabarfoori.com/fa/tiny/news-3235132
🔹
تصویری از تغییر چهره ضرغامی؛ او دچار سکته مغزی شده بود؟
👇
khabarfoori.com/fa/tiny/news-3235351
🔹
تعطیلی ادارات در این استانها در روز چهارشنبه (14 مرداد 1405)
👇
khabarfoori.com/fa/tiny/news-3235258
🔹
با نصب اپلیکیشن خبرفوری، از خبرها جانمانید
🔹
https://B2n.ir/jb2310</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/678199" target="_blank">📅 23:17 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678198">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
سرلشکر رضایی: ما در تنگه هرمز مسئولانه عمل می‌کنیم و ضمن امنیت خودمان امنیت دنیا هم برایمان مهم است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/678198" target="_blank">📅 23:08 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678197">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecccd3a4fe.mp4?token=b1KZ-49fYBvCI2l67MxtiQGbS_a5ET1-4sB7Rno_jFmgvWAHVNQDc62YBMUFYNymX8i5XNkBwFVLLCkY8-hbxMvIhCzo8K9rj0Qq-GV7EHr1rxU13KXon5Il9l7QT3RtM-8K-AAXPrla3E5enh8P4OJEujTlvSsATPEocFGMFPKq7lzCCuk7tXxdCeUNx4OiBV7ZMD-f8RrO37wrJx98czCKYf_ZoVwAvk3KpgR61ByOZFO6BlfbldhzE3t0wThVYBaHA5kL8TnX4LcnbhsPzpFvIUxOmw3NXoX3WDxlcucE0URQaRWYwFBopUHc_mLW70SooErCZU3v1JiKgML4IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecccd3a4fe.mp4?token=b1KZ-49fYBvCI2l67MxtiQGbS_a5ET1-4sB7Rno_jFmgvWAHVNQDc62YBMUFYNymX8i5XNkBwFVLLCkY8-hbxMvIhCzo8K9rj0Qq-GV7EHr1rxU13KXon5Il9l7QT3RtM-8K-AAXPrla3E5enh8P4OJEujTlvSsATPEocFGMFPKq7lzCCuk7tXxdCeUNx4OiBV7ZMD-f8RrO37wrJx98czCKYf_ZoVwAvk3KpgR61ByOZFO6BlfbldhzE3t0wThVYBaHA5kL8TnX4LcnbhsPzpFvIUxOmw3NXoX3WDxlcucE0URQaRWYwFBopUHc_mLW70SooErCZU3v1JiKgML4IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور سید عباس عراقچی وزیر امور خارجه در راهپیمایی اربعین
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/678197" target="_blank">📅 23:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678196">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
سرلشکر رضایی: اگر محاصره ادامه پیدا کند برای ناوهای آمریکا خطرات جدی به‌وجود خواهد آمد
🔹
آمریکایی‌ها باید رفتار خود را تغییر دهند وگرنه ما این شرایط را تحمل نخواهیم کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/678196" target="_blank">📅 23:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678195">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
گاردین به نقل از یک مقام ارشد پاکستانی: عاصم منیر برای جلوگیری از تشدید بیشتر تنش در منطقه، با ونس و ویتکاف در تماس نزدیک بوده
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/678195" target="_blank">📅 23:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678194">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
سرلشکر رضایی: دست‌وپازدن ترامپ ممکن است جرقۀ آغاز جنگ جهانی سوم را بزند
🔹
خلیج فارس و تنگۀ هرمز چاشنی بسیار خطرناکی برای جنگ جهانی سوم است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/678194" target="_blank">📅 22:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678193">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
محسن رضایی: آمریکا باید رفتارش را عوض کند؛ اگر آمریکا به شروط تفاهم‌نامه عمل کند می‌تواند نشان از تغییر رفتار باشد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/678193" target="_blank">📅 22:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678192">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
یک منبع بلندپایه ایرانی به المیادین: رئیس‌جمهور آمریکا که به دروغگویی عادت دارد، همچنان دیگران را سرزنش می‌کند به جای آنکه مسئولیت ناکامی خود در به شکست کشاندن تفاهم را بپذیرد
🔹
مذاکرات ما با همسایه همیشگی‌مان، سلطنت عمان، در جریان است، به ویژه آنکه تنگه…</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/678192" target="_blank">📅 22:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678191">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
محسن رضایی: آقای ترامپ شما در خواب و رویا عملیات بزرگ‌تر از جنگ جهانی دوم داشتید، پس چرا پای نیروهای شما در خاک ایران نیامد؟
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/678191" target="_blank">📅 22:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678190">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
یک منبع بلندپایه ایرانی به المیادین: رئیس‌جمهور آمریکا که به دروغگویی عادت دارد، همچنان دیگران را سرزنش می‌کند به جای آنکه مسئولیت ناکامی خود در به شکست کشاندن تفاهم را بپذیرد
🔹
مذاکرات ما با همسایه همیشگی‌مان، سلطنت عمان، در جریان است، به ویژه آنکه تنگه هرمز منحصراً در آب‌های سرزمینی دو کشور قرار دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/678190" target="_blank">📅 22:47 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678189">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e83ea2b385.mp4?token=iHEYJwuxHM_1Mshg4DgnrZcv_3zjo_Zon1HQVO20QfSC9cG-J60jdXU3QWMWgbWFkTBiH0XGaJfDLAqCat0kpD6LMgti_LqvY-2wG7ofFpQipIx6s1XI5qgBqeN3gACIxKebXUWLif9nLLFVf27c0V0Umr4F-j7-9wGMefE6zNsZhAk6nhSp0wtpmL6cRvJipBZkm_-HY0J0gz67WnB0x9ojw0-MsdHm3CISx2-9T4YkvUEbKRT27OcCc3_UVq2HRkUIg8tC3Nyb18BNfA-xNHeSew0qZXe-bxT1JXsszbowhQEODw-JXDu2pV-GGM80cKJmYHzQechggmxnwOHhvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e83ea2b385.mp4?token=iHEYJwuxHM_1Mshg4DgnrZcv_3zjo_Zon1HQVO20QfSC9cG-J60jdXU3QWMWgbWFkTBiH0XGaJfDLAqCat0kpD6LMgti_LqvY-2wG7ofFpQipIx6s1XI5qgBqeN3gACIxKebXUWLif9nLLFVf27c0V0Umr4F-j7-9wGMefE6zNsZhAk6nhSp0wtpmL6cRvJipBZkm_-HY0J0gz67WnB0x9ojw0-MsdHm3CISx2-9T4YkvUEbKRT27OcCc3_UVq2HRkUIg8tC3Nyb18BNfA-xNHeSew0qZXe-bxT1JXsszbowhQEODw-JXDu2pV-GGM80cKJmYHzQechggmxnwOHhvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با این اپلیکیشن‌ها حرفه‌ای‌تر، سریع‌تر و هوشمندتر کار کنید
🤩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/678189" target="_blank">📅 22:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678188">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
چرا آمریکا در حملات اخیر اسرائیل را دخالت نداده است؟
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/678188" target="_blank">📅 22:40 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678187">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8f4a2d6b2.mp4?token=oAwnvG8kxoZHhvjaCukJNdP2N7-0l3ne0TwqyCt5a8LLnutTgeFgheB8V6-hzZfGqk76hAl4-nXFMSTCMOPLwArQ7ulKVwwFv8YLmwm_L1QV-Ud1YjX1OreJ1R2uRnj3P-nBDknvJCxNUd-I7-41XStFZlRXEOx2RpWNjE8CqmGfYtsLB3AZ6hRP5bxPHOro6MlxyPgHfio5dSpSvnBay-2EBr0bRxNIybm6aca1SKO_RXt-pCn59laV0ZdgMkRc6iNMlsuOh4DcZogcLBbB6AaDr9Bij877bQB3Q5ItSnrXN1gfKw9hao7IjwzGZF3y0T9IMUpCE7G_oBgsnZQhRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8f4a2d6b2.mp4?token=oAwnvG8kxoZHhvjaCukJNdP2N7-0l3ne0TwqyCt5a8LLnutTgeFgheB8V6-hzZfGqk76hAl4-nXFMSTCMOPLwArQ7ulKVwwFv8YLmwm_L1QV-Ud1YjX1OreJ1R2uRnj3P-nBDknvJCxNUd-I7-41XStFZlRXEOx2RpWNjE8CqmGfYtsLB3AZ6hRP5bxPHOro6MlxyPgHfio5dSpSvnBay-2EBr0bRxNIybm6aca1SKO_RXt-pCn59laV0ZdgMkRc6iNMlsuOh4DcZogcLBbB6AaDr9Bij877bQB3Q5ItSnrXN1gfKw9hao7IjwzGZF3y0T9IMUpCE7G_oBgsnZQhRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شیطان زرد: انگلیس کشور ورشکسته است
رئیس دولت تروریستی آمریکا که بوی نفت در دریای شمال به مشامش رسیده است در ادامه اراجیف خود:
🔹
انگلیس یک کشور ورشکسته است. اگر نفت دریای شمال را آزاد کند، به کشوری ثروتمند تبدیل خواهد شد.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/678187" target="_blank">📅 22:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678186">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffffb49aab.mp4?token=oEKWvh4iAI5eRo-n9mIFmQpm8tTfmcnFZXtekJCmxnTvIKVw7esEYzsmle9kCgXc4tNAPuTR9nX71kIP71OQigOMArs-pupC7W1IjcrSa0T-Ty1RQc1CtUOfviDB-dt4_6wklvuD7OcV_u_aC-lkxj1lwhffnvZ1MHygaAQP-Zq2J4G_9Un1jxfLOmWfk9pD-LuKVmRJZ9BNbhG9D6suvewrsX2UAyzkZ5FOHhpz0_24SZf2iWpG1SI7BIq_VSNzDcrpUROyJVTEYKEs5Ydt8PkW4V49ah1H9rGiVtaxv3SN5uldHgCXOKWRH_qUZbUFy7g0W0cNZS84ITTds1R2MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffffb49aab.mp4?token=oEKWvh4iAI5eRo-n9mIFmQpm8tTfmcnFZXtekJCmxnTvIKVw7esEYzsmle9kCgXc4tNAPuTR9nX71kIP71OQigOMArs-pupC7W1IjcrSa0T-Ty1RQc1CtUOfviDB-dt4_6wklvuD7OcV_u_aC-lkxj1lwhffnvZ1MHygaAQP-Zq2J4G_9Un1jxfLOmWfk9pD-LuKVmRJZ9BNbhG9D6suvewrsX2UAyzkZ5FOHhpz0_24SZf2iWpG1SI7BIq_VSNzDcrpUROyJVTEYKEs5Ydt8PkW4V49ah1H9rGiVtaxv3SN5uldHgCXOKWRH_qUZbUFy7g0W0cNZS84ITTds1R2MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا آمریکا در حملات اخیر اسرائیل را دخالت نداده است؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/678186" target="_blank">📅 22:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678185">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/003c87529a.mp4?token=eBaW3doIybFFdiBMgqZIWeS5VpBGQpiQy1VPyWAiHCXpdnhhjpWSB7b3_qqbCkZH2fClI_iHXB8spkxMP7m0ucj0Cm9bjz9zCvfUyGNuAXwN5a2mvEAe7SNXIyCv83bgXWwGttnbPbu4uPV1Av64ear2CZQDRdxhn38hPA3NeZxCLePYQ2dnNd2VGBk3KGUeuU52N4u0khARX_VRt_tUnm2Yws6JYXvC8PXZfL9LTNuoNPRI9QVaD-WvWPSjhVYuzKKabE9me5DXVcg3ATsfxLUHmnTNEDo-oP8Z97Y6tHQv9ZuEpDwvGBwc0VI8aupr5WeCGoDtZimGE2YZNFLyaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/003c87529a.mp4?token=eBaW3doIybFFdiBMgqZIWeS5VpBGQpiQy1VPyWAiHCXpdnhhjpWSB7b3_qqbCkZH2fClI_iHXB8spkxMP7m0ucj0Cm9bjz9zCvfUyGNuAXwN5a2mvEAe7SNXIyCv83bgXWwGttnbPbu4uPV1Av64ear2CZQDRdxhn38hPA3NeZxCLePYQ2dnNd2VGBk3KGUeuU52N4u0khARX_VRt_tUnm2Yws6JYXvC8PXZfL9LTNuoNPRI9QVaD-WvWPSjhVYuzKKabE9me5DXVcg3ATsfxLUHmnTNEDo-oP8Z97Y6tHQv9ZuEpDwvGBwc0VI8aupr5WeCGoDtZimGE2YZNFLyaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محسن رضایی: دشمن برای باز کردن تنگه هرمز میخواست یک کار زمینی انجام دهد/ میخواست ارتباط استان‌های جنوبی و شمالی را قطع کند و پل‌ها را زد
🔹
طرح ناپخته فرمانده‌های ارتش آمریکا باعث شد حمله زمینی و هوایی متوقف شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/678185" target="_blank">📅 22:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678184">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
محسن رضایی: مقام معظم رهبری اجازه امضای تفاهم‌نامه را دادند و رئیس‌جمهور محترم هم امضا کردند/ ترامپ در کنار آقای مکرون یک شوی جهانی درست کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/678184" target="_blank">📅 22:23 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678183">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
محسن رضایی: با پاسخ شدید موشکی - پهپادی ایران در آن ۱۷ روز آرزوی ترامپ برای فتح‌الفتوح به در بسته خورد
🔹
به آمریکا فهماندیم هم موشک داریم و هم توان دفاع.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/678183" target="_blank">📅 22:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678181">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
محسن رضایی: با پاسخ شدید موشکی - پهپادی ایران در آن ۱۷ روز آرزوی ترامپ برای فتح‌الفتوح به در بسته خورد
🔹
به آمریکا فهماندیم هم موشک داریم و هم توان دفاع.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/678181" target="_blank">📅 22:18 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678180">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b694f704fb.mp4?token=enwF_IHaFdki5U5h9xhqHiJ2gaGbzqjjXkM7OmKCShyzkXs4LWwGGedtXQKViRFQdzF7eSg1RVFjN26l8E_opQ_94wX-0dmavjV3dA9Ty5oieQ9X7EEx1Tq2cbBIjpWPpA-LK_J4Z8fj2DQWh6qtmjyRYnQSOxWoVJ8cGz9FG2A0wcEKUtzd2A_TH6quJRhJj_yf1NfWzqujdNHoiy5kunnlu7c8C_sZsu1RJe6FefQenHzsHJRfkc2ZpIo7gXVqRrUkN-d-mJqQJsD0NUI_mEdrvTLJut0sDpFcsvyw653xcUPkFkXT_68ia0Xe4IivQKN0jcUAMSfyxFAkOHs0JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b694f704fb.mp4?token=enwF_IHaFdki5U5h9xhqHiJ2gaGbzqjjXkM7OmKCShyzkXs4LWwGGedtXQKViRFQdzF7eSg1RVFjN26l8E_opQ_94wX-0dmavjV3dA9Ty5oieQ9X7EEx1Tq2cbBIjpWPpA-LK_J4Z8fj2DQWh6qtmjyRYnQSOxWoVJ8cGz9FG2A0wcEKUtzd2A_TH6quJRhJj_yf1NfWzqujdNHoiy5kunnlu7c8C_sZsu1RJe6FefQenHzsHJRfkc2ZpIo7gXVqRrUkN-d-mJqQJsD0NUI_mEdrvTLJut0sDpFcsvyw653xcUPkFkXT_68ia0Xe4IivQKN0jcUAMSfyxFAkOHs0JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای خصمانه و گستاخی خوک زرد درباره ایرانی‌ها: قبل از بین بردن و کشتن ایرانی‌ها فرصت بدهید؛ اجرای برنامه ریزی هایمان بسیار دشوار است
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/678180" target="_blank">📅 22:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678179">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OcFAoyOOri4xJkbJVYMcpx0OXz7zG3v3S6apAG0IWNsRykERLNGTC5BWYmmT5t7aEhpcD9hS7ShKRtuEeWrEfOf5olSlKw9jc0YsM1fj_nNOB_yKRCnhOOIR6KDNEheRwpjcVGwC-DIHbUO89k94qUhsgneoACIi3Nnapv_vYQt5MCftlyF4tbPL2n0aAZakf1tjqRbGM0_kKkGnUbmCZqbSz2pa6KCyQWLUotnvoLK5vOGB2om7gqzsUfBU-LF-0MPCSSaI92uD1VFUUIDXjPogMGStwBKv89C3_SHYfxG4HXuNfRteJnxkgf-mitUwmNCDk8xywXPd8V5WjIwKkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرصت‌ها مثل ابر می‌گذرند؛ آرام، سریع و بی‌خبر
🔹
در حکمت ۲۱ نهج‌البلاغه، امام علی(ع) یادآوری می‌کند که فرصت‌ها ماندگار نیستند. بعضی لحظه‌ها فقط یک‌بار از راه می‌رسند و اگر قدرشان را ندانیم، شاید دیگر تکرار نشوند.گاهی یک تصمیم به‌موقع، می‌تواند مسیر زندگی…</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/678179" target="_blank">📅 22:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678178">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeef354708.mp4?token=V2Pt6GySOmACanIRJUTzCPaUqBFUSG48eSr8Drl2j0nAz66QhS4lpY0KM8vwgZOXwpk7ICdEVcj4lB8V81yqHjNSAKje5xDnt-oalCK7_UW0roS8OZuis0z0YwNLjX7qHSLh3eKm_PqSWeAw0H_wPwlWoU4WB49s9SgTjSecn_FTSGuc8cB0QDjg1SqAjqmOt-439XQ8qmcxGLOKS8WJ5KTOAeAS6S3NopmEU9UZNMAVqGh9DcI2BYklDmWyE7cji4R2JYA1KtbkboH75ROp4qbH3HjQyE1a8EhmVWFVHYCNhhhXdzQvR0s60K_EBFT3P4S63Bp10jPvGiIRLCVoMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeef354708.mp4?token=V2Pt6GySOmACanIRJUTzCPaUqBFUSG48eSr8Drl2j0nAz66QhS4lpY0KM8vwgZOXwpk7ICdEVcj4lB8V81yqHjNSAKje5xDnt-oalCK7_UW0roS8OZuis0z0YwNLjX7qHSLh3eKm_PqSWeAw0H_wPwlWoU4WB49s9SgTjSecn_FTSGuc8cB0QDjg1SqAjqmOt-439XQ8qmcxGLOKS8WJ5KTOAeAS6S3NopmEU9UZNMAVqGh9DcI2BYklDmWyE7cji4R2JYA1KtbkboH75ROp4qbH3HjQyE1a8EhmVWFVHYCNhhhXdzQvR0s60K_EBFT3P4S63Bp10jPvGiIRLCVoMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک کثیف درباره ایران: به من زنگ می زنند و می گویند: لطفا حمله نکنید، معامله می کنیم
🔹
این حقیقت مطلق است و همه آن را می دانند.
🔹
چه کسی تماس نمی گیرد؟
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/678178" target="_blank">📅 22:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678177">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65010e1c6b.mp4?token=J9TjtN6Q4Yv57OH0NQ3cb0wxe-bKkdo12937rfeW9YrLVGaY3sJnWbQRI4DteOSxieBdS84eyPsA6E8oeRykjXUKkA0wq2TylPBxKh6c38PQViLKk0hXq6avgN9WsQyzfkRfqIJiq4aOC4FB8ErumV65CyqNs--JGSjGAHERSx4xS5iy8gY9pRtZUVCq53bo0WsmEkOfjQwS0o_G0ZV3JBFkR4Htzkdavsd6bgp0Q_3RF-IUL1_np7h-sJqNf_XiBd65nnzgxM2GtIHHFOrnQn4XmrfRAF_rfwiexmqb9eFCdfSrCyQ33I2DDqdnSCYO4aakBGVxAQfJGNM6GCTjuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65010e1c6b.mp4?token=J9TjtN6Q4Yv57OH0NQ3cb0wxe-bKkdo12937rfeW9YrLVGaY3sJnWbQRI4DteOSxieBdS84eyPsA6E8oeRykjXUKkA0wq2TylPBxKh6c38PQViLKk0hXq6avgN9WsQyzfkRfqIJiq4aOC4FB8ErumV65CyqNs--JGSjGAHERSx4xS5iy8gY9pRtZUVCq53bo0WsmEkOfjQwS0o_G0ZV3JBFkR4Htzkdavsd6bgp0Q_3RF-IUL1_np7h-sJqNf_XiBd65nnzgxM2GtIHHFOrnQn4XmrfRAF_rfwiexmqb9eFCdfSrCyQ33I2DDqdnSCYO4aakBGVxAQfJGNM6GCTjuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک زرد: من می خواهم قبل از اتخاذ اقدامات شدید، هر فرصتی را که می توانم به ایران بدهم
🔹
امیدوارم به خود بیایند.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/678177" target="_blank">📅 22:01 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678176">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBimebazar</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/isAqfNhZEddtR09UML9mY3nwhlx1cLY7KODtg3jNMCXwNW6wIWYyapstboQY_uDEzK2kwfwnaX5RCVmnrY6tXA2slKpEh4vGbmWJTCvz6X7xqUwTw2Dn_rNlTpoQ23zpEvLhBRjOJqXNeHNFhfguQAUy6bb2D1apeTEDLszbcwqBkABclyVuo1Xy9D-CfmuqBKIN1GSe--CVBkG7FX12ne-hBejLLDyYVU4FtDyEtIhFJXMqJL0UP6dNsIPJIdIDKPuwb6bRH7L7sRJsJwjaZ3BZeHSBfAcLIitSmF3kwYbyQEb0B67rJrVYYUMGdbieAOwTo64WV0dPDEp17_ZwUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
نوبت به بیمه ثالث موتور رسید!
یک موتورسوار حرفه‌ای همیشه برای مسیرش برنامه‌ریزی می‌کنه. خرید بیمه شخص ثالث هم بخشی از این برنامه‌ ریزیه که امنیت خاطر شما رو در هر تردد تضمین می‌کنه.
✅
برای اینکه با خیال راحت تردد کنید،
بیمه‌بازار
خرید بیمه ثالث موتور رو براتون ساده کرده:
•
مقایسه سریع
قیمت شرکت‌های مختلف
•
خرید اقساطی
•
صدور فوری و آنلاین
👈
خرید قسطی بیمه
#بیمه_بازار
🟡
@bimebazarco</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/678176" target="_blank">📅 22:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678173">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a224327602.mp4?token=pKZz-yjhE-1_-HckiqFpcD24__1uWYbGzq5Hex9u5aktwGAGRWtUBOrC08AoowPEFyc_1aw2hyR-6muAy3L5q_HflCrBKQ42RoFn13ZDrctrYd4yL2T1KjAMWLt85c4jgOPA7OEw1O_cbcRJWCMiWnjCcNvSwnkDgNFEoNsL0-4WrdwjeCKEBmyBNKvWMYVgxEpk7IkLtfeojb1a-BEZrbpA3W6mzz8vQR-WXbUTDQSNXlSd6ZJjGu8WZpqZPIbCgnNrZzCmRbYQrZMQO5ztdroBUSe3Ci7nh_RvkKmsNT8NXhzQObMusEbONP_0uXj6ugLe7Ii9FcNzR_v32j-lsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a224327602.mp4?token=pKZz-yjhE-1_-HckiqFpcD24__1uWYbGzq5Hex9u5aktwGAGRWtUBOrC08AoowPEFyc_1aw2hyR-6muAy3L5q_HflCrBKQ42RoFn13ZDrctrYd4yL2T1KjAMWLt85c4jgOPA7OEw1O_cbcRJWCMiWnjCcNvSwnkDgNFEoNsL0-4WrdwjeCKEBmyBNKvWMYVgxEpk7IkLtfeojb1a-BEZrbpA3W6mzz8vQR-WXbUTDQSNXlSd6ZJjGu8WZpqZPIbCgnNrZzCmRbYQrZMQO5ztdroBUSe3Ci7nh_RvkKmsNT8NXhzQObMusEbONP_0uXj6ugLe7Ii9FcNzR_v32j-lsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای از آسیب‌دیدگی برخی ایستگاه‌ها و پالایشگاه‌های شهر ینبع عربستان پس از حملات اخیر انصارالله یمن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/678173" target="_blank">📅 21:57 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678172">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/moL1Sk-T4bRRZdfsfdMAXpE3Hc_1QezkgqQpVMqtscNICaWXmQ0A-T08de4z3Sf-UTp9AU1K-ThrWJV8Lphhm7pgPCb0s4s33yhXrnDo9DQVtsXXLNkWZg3rcatfwwPpwXHJ6DiQiKz2MtagcPo9ZVLi7P-SqzOiQNAitxt3Xrer_xigLYTGRqBF5c3euHgfyS1ngwK5yy1lxo4y2zg8TIu1wGK3rr7-4JQRikbZ0c9854hGFskGzv0qhRPuu8SVG6w_jSx9S2O9IeiAaJeQdtzdy8h5Yin9v4m0ysfY31F99Bn2WMyeAdvKfhd1CpwkH1KSpYyILVNkt3alXJH5VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زهرا، نوه خردسال آقای شهید ما هم اربعین امسال این‌گونه زائر حرم سیدالشهدا شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/678172" target="_blank">📅 21:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678170">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75a71f2f93.mp4?token=XYukc3qgeil8ByitIM6fuGnyZiLAkRF7HAdHMyGfuTbpj2u3ipCJ2TZ9-_t01iw9_Kd_qCmzzD6hHf6yWql9J5U_CmNUk_V8GBukw2XLjprpd_KOtbCWLNms_bPAY-LBquQe1SlvQElz5jOnNVEVCev0n5DzcCKAUExxBNk8Umy3lbxLijGeculZpGAst2JpTcr_3AI9KZv5CUXryNJb3mGY3xIlYXbyaon81y5Yoqlt2xRgWDz5ehFT39JIubjXnUfLGJUa1T3VARYmP9S0AP2w4tDFBSVhhL5r1DCZB-TRdIsEFpSvMKPxIU9CazRLOCBlCsBNvcjyqxtx7PcykA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75a71f2f93.mp4?token=XYukc3qgeil8ByitIM6fuGnyZiLAkRF7HAdHMyGfuTbpj2u3ipCJ2TZ9-_t01iw9_Kd_qCmzzD6hHf6yWql9J5U_CmNUk_V8GBukw2XLjprpd_KOtbCWLNms_bPAY-LBquQe1SlvQElz5jOnNVEVCev0n5DzcCKAUExxBNk8Umy3lbxLijGeculZpGAst2JpTcr_3AI9KZv5CUXryNJb3mGY3xIlYXbyaon81y5Yoqlt2xRgWDz5ehFT39JIubjXnUfLGJUa1T3VARYmP9S0AP2w4tDFBSVhhL5r1DCZB-TRdIsEFpSvMKPxIU9CazRLOCBlCsBNvcjyqxtx7PcykA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک کودک کش: من به ایران اجازه نمی‌دهم هزینه‌ای دریافت کند
🔹
اگر قرار است کسی شارژ کند، این ما هستیم.
🔹
ما کنترل کامل داریم
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/678170" target="_blank">📅 21:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678169">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e21c4ec7f1.mp4?token=VdgpN52-IzIxOSOznOnuFiaxAbA9poDNrn-ILtU-x1WVs043RQ-u79IiUZGTcnYN6bpBxZuvTjONgwbpAAYuQw3-ojg6kql0oisugKg3lmRVA9Z5e9FUheXMC5xpZDNRl7vicvdg5dFio9pmRbQbcTuW2AuKXEmvnRZRGQRHT7LqQ2x7Jb2gAcwrpYMC-REfOS6ic3e6LDSLeL6CV9jN5vmg3rGRKGEFUzs_GEu4KzfAM_jmYA6TOUGo9dd4Iah5C4r24voANAlENiUuKTHZOQsjB0VD5-3KM95-0t0-T87H3O19JQWeT7w5HW-ENABTMib3X6AExATnqjHKLQ1wyZDc7S_LZbxKOb_OsANSR3LAa5iIWATdnKADWJK2ZMexRJ5xoSofK1CXKR9U_ul7zxiSA3PHORTLh9snUIxTDpNcOK-CVJqoanSRe6Xm-BezyD7erhtPUmLAgZ9DAYXW6moJh6byMKCtaqw0PyCIMZVhKzEhusetxJRnAv5nGxDDlFHxI_8ILEs2YxQbMznLT-Ej8Pexxis3CsdzXP95ELcpBw1rn57OPLkxjScSUbYQ8KkSPLCCZebIh3eNXOTHLnmzaWZgoeAmDwdja3Arlaxw1iqp7hZZvTlv5ocD-PU8RxVaNfzddKaNEHaI5iqFBdjKlWu6Aji5YogW42M48TY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e21c4ec7f1.mp4?token=VdgpN52-IzIxOSOznOnuFiaxAbA9poDNrn-ILtU-x1WVs043RQ-u79IiUZGTcnYN6bpBxZuvTjONgwbpAAYuQw3-ojg6kql0oisugKg3lmRVA9Z5e9FUheXMC5xpZDNRl7vicvdg5dFio9pmRbQbcTuW2AuKXEmvnRZRGQRHT7LqQ2x7Jb2gAcwrpYMC-REfOS6ic3e6LDSLeL6CV9jN5vmg3rGRKGEFUzs_GEu4KzfAM_jmYA6TOUGo9dd4Iah5C4r24voANAlENiUuKTHZOQsjB0VD5-3KM95-0t0-T87H3O19JQWeT7w5HW-ENABTMib3X6AExATnqjHKLQ1wyZDc7S_LZbxKOb_OsANSR3LAa5iIWATdnKADWJK2ZMexRJ5xoSofK1CXKR9U_ul7zxiSA3PHORTLh9snUIxTDpNcOK-CVJqoanSRe6Xm-BezyD7erhtPUmLAgZ9DAYXW6moJh6byMKCtaqw0PyCIMZVhKzEhusetxJRnAv5nGxDDlFHxI_8ILEs2YxQbMznLT-Ej8Pexxis3CsdzXP95ELcpBw1rn57OPLkxjScSUbYQ8KkSPLCCZebIh3eNXOTHLnmzaWZgoeAmDwdja3Arlaxw1iqp7hZZvTlv5ocD-PU8RxVaNfzddKaNEHaI5iqFBdjKlWu6Aji5YogW42M48TY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شیطان زرد: فردا آخرین فرصت ایران است
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/678169" target="_blank">📅 21:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678168">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e9041bec7.mp4?token=BY79VNZtkbqSV0OV99yfDSaG7t1R_MaIb5QcNdCa-xBsiLYv82X3YScHE_j503EUnGe7wkO9Z71IIuWF_pWomVgDP5-MvISPIZ-ZZjVlCALWMDuFCO9l8O4ducPG5n8Uk50EOvYyrexWbDdYmtUDwr2fk1Luc20hMvAgu0XxLqe24HqEbuEcvlVUH4UL0gMpPfowAU4MQW-EJ_o1q7Q5uu86bvyPMpLsaQ2b_f-D-GLL3XsZVBnV3MYL4n36ZkvFjQhHTB8tUs1QU0fgbmmLQA_EF03sV4wF9QhAvSmCeSKniOKgKcFMK9UM4nN6XOHel8XwR2XdKLc_Tdp3d4KIyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e9041bec7.mp4?token=BY79VNZtkbqSV0OV99yfDSaG7t1R_MaIb5QcNdCa-xBsiLYv82X3YScHE_j503EUnGe7wkO9Z71IIuWF_pWomVgDP5-MvISPIZ-ZZjVlCALWMDuFCO9l8O4ducPG5n8Uk50EOvYyrexWbDdYmtUDwr2fk1Luc20hMvAgu0XxLqe24HqEbuEcvlVUH4UL0gMpPfowAU4MQW-EJ_o1q7Q5uu86bvyPMpLsaQ2b_f-D-GLL3XsZVBnV3MYL4n36ZkvFjQhHTB8tUs1QU0fgbmmLQA_EF03sV4wF9QhAvSmCeSKniOKgKcFMK9UM4nN6XOHel8XwR2XdKLc_Tdp3d4KIyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک پلید: مذاکرات به سرعت پیش خواهد رفت، این یا آن صورت. خیلی هم پیچیده نیست
🔹
ما در مورد باز کردن کامل تنگه هرمز فردا صحبت می کنیم.
🔹
سپس در مورد توانمندی های هسته ای ایران صحبت خواهیم کرد.
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/678168" target="_blank">📅 21:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678167">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c6a2a1f36.mp4?token=V_pOxFL4IX4VednRZDkZyD1Agxw8E8N2EFu8sRFrEuwWjgF-xhOfc0Ij7plRkB-SJfcyBuGBiTDjN2FmyTfr5V6udmU39dWMU5Vrqkq_ljVhvvVZNOy38nfq8ffzuCxjKyA4aNLCUW7XP-Y4SAsIUGsWvy45kPKF4_FA04Jf5dXlxjxVMZWXaTURWdN8GJvvVu2vo9DrOKipiIHfrA03PSWktesYwAmIeG4betNHMXnoKbaHfd7wvMXMI2lidETau_N_h41UL7dNbyRFMUxraKr-ve_OGTT3WCfjD0AeywIupwbWxYUuRfo3I_g5-is9QPV7ySXDEmqAPnwTKXO3pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c6a2a1f36.mp4?token=V_pOxFL4IX4VednRZDkZyD1Agxw8E8N2EFu8sRFrEuwWjgF-xhOfc0Ij7plRkB-SJfcyBuGBiTDjN2FmyTfr5V6udmU39dWMU5Vrqkq_ljVhvvVZNOy38nfq8ffzuCxjKyA4aNLCUW7XP-Y4SAsIUGsWvy45kPKF4_FA04Jf5dXlxjxVMZWXaTURWdN8GJvvVu2vo9DrOKipiIHfrA03PSWktesYwAmIeG4betNHMXnoKbaHfd7wvMXMI2lidETau_N_h41UL7dNbyRFMUxraKr-ve_OGTT3WCfjD0AeywIupwbWxYUuRfo3I_g5-is9QPV7ySXDEmqAPnwTKXO3pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شیطان پلید درباره ایران: این آخرین فرصت آنها برای امضای یک توافق خوب است
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/678167" target="_blank">📅 21:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678166">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7424851c8f.mp4?token=SD_90XmD_5CZddQdYPoOcaKTz6NOruvZPpyNONEXKcxukPezoPrkUm9v4eshBMxdk-A3XnXS9BIy7gSaSRQfM64iQxJRv1NsqkeHNzjqRTMtUE5HBrBs-d6CPt3hn_paJJN-JIkTJNF_4XF61Sb6YFvNJtB1oD0dDfGjFlAE5GyfRhdCaWGFvLE62LQeoN5cSpvMIcPtyVizwlkz-Ya51hnuWf2n0qB9hoH0cbHI3oj5s66uNMdtB3uUWYa-bprjLahuCF2tGVU2kF-9IoCGNQJrY8WpqXRrm-fhd9xY8t0uulKWlr8Nu_ZPLtwwCnp2WmByoGF0rxV2tLL4dkjiGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7424851c8f.mp4?token=SD_90XmD_5CZddQdYPoOcaKTz6NOruvZPpyNONEXKcxukPezoPrkUm9v4eshBMxdk-A3XnXS9BIy7gSaSRQfM64iQxJRv1NsqkeHNzjqRTMtUE5HBrBs-d6CPt3hn_paJJN-JIkTJNF_4XF61Sb6YFvNJtB1oD0dDfGjFlAE5GyfRhdCaWGFvLE62LQeoN5cSpvMIcPtyVizwlkz-Ya51hnuWf2n0qB9hoH0cbHI3oj5s66uNMdtB3uUWYa-bprjLahuCF2tGVU2kF-9IoCGNQJrY8WpqXRrm-fhd9xY8t0uulKWlr8Nu_ZPLtwwCnp2WmByoGF0rxV2tLL4dkjiGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شیطان زرد: ما اکنون به درخواست ایران و با حمایت عربستان سعودی، امارات، قطر و دیگران صحبت می کنیم
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/678166" target="_blank">📅 21:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678165">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e13546124.mp4?token=o_Jh6afnLUgeS8LUwso2pioiBmEaWtirjBgmkylWDxeUalx1N6JgBvVbPKXNOA8jV3uZytsndh1rq78NIJ2Z9rApwEE3nA-6H28m3z0gs_qKQ_73XLLuioXk8DN7Prnbqv3bj214tePqGv6GUaHM7w3AzJcun77NudeFyfMCoK3KQjthiwT_XWE9_JCCizUxv3zRR8OODxpKHwgoUCGfu_6lgmgjvhRMk4Hb36kTngnfYRlT-W43cHkbaUjrz4wxdTfvGZidmZn9ETWZu_TfbLOtqj1XNO5oe2zjGeY3FcvDaPm66E_ND4dgZ2_Fu1O2Eotg1vO0JWSxeXOZDPDqXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e13546124.mp4?token=o_Jh6afnLUgeS8LUwso2pioiBmEaWtirjBgmkylWDxeUalx1N6JgBvVbPKXNOA8jV3uZytsndh1rq78NIJ2Z9rApwEE3nA-6H28m3z0gs_qKQ_73XLLuioXk8DN7Prnbqv3bj214tePqGv6GUaHM7w3AzJcun77NudeFyfMCoK3KQjthiwT_XWE9_JCCizUxv3zRR8OODxpKHwgoUCGfu_6lgmgjvhRMk4Hb36kTngnfYRlT-W43cHkbaUjrz4wxdTfvGZidmZn9ETWZu_TfbLOtqj1XNO5oe2zjGeY3FcvDaPm66E_ND4dgZ2_Fu1O2Eotg1vO0JWSxeXOZDPDqXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک کثیف: دیروز قرار بود ضربه محکمی به آنها بزنیم. خیلی قوی قدرتمندتر از هر حمله ای از زمان جنگ جهانی دوم
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/678165" target="_blank">📅 21:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678164">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/735f9b35d6.mp4?token=C202C4xQvSHZEXEexic_ltDRKHqMcXut0kF9-iiVOLDivWPWDAxiz0wlyTSvxXHvgcUAEP0mBmbSJYR7kCLS6XdDOtbu5OH9YXvXx9In0YG5vcmY4YZCcEcMf5d4Tw5Ul60xT12UAundDy9RUIi3IuJApC7be66-PXeKh93fiFaYGsOtVbIgq5P_E8MfsOH6MLjjMsysVlJtibkwaB7o2kT2xOJuErZVpeKsXJtiL9y4sKl5cv1p0XcLvQwUZwiNSP1FC3jLYxVPUlySMbQNeput4IzdNjuzb19DbuUgMZw2CNqbVdhtfnX9PDYVaK5Xw5PeG3tp-1vG344r-QCnzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/735f9b35d6.mp4?token=C202C4xQvSHZEXEexic_ltDRKHqMcXut0kF9-iiVOLDivWPWDAxiz0wlyTSvxXHvgcUAEP0mBmbSJYR7kCLS6XdDOtbu5OH9YXvXx9In0YG5vcmY4YZCcEcMf5d4Tw5Ul60xT12UAundDy9RUIi3IuJApC7be66-PXeKh93fiFaYGsOtVbIgq5P_E8MfsOH6MLjjMsysVlJtibkwaB7o2kT2xOJuErZVpeKsXJtiL9y4sKl5cv1p0XcLvQwUZwiNSP1FC3jLYxVPUlySMbQNeput4IzdNjuzb19DbuUgMZw2CNqbVdhtfnX9PDYVaK5Xw5PeG3tp-1vG344r-QCnzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک زرد: ما با ونزوئلا اختلاف نظر داشتیم و خیلی خوب تمام شد
🔹
ما با ایران اختلاف نظر داریم و این اختلافات خیلی خیلی خوب پیش می رود.
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/678164" target="_blank">📅 21:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678163">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e26ecf0d2.mp4?token=MQeMT95AmKrH8LQBUtQKMN6rgpEPlzOGMK-AA6QeC6mmt_CGkPvyX-zR-uM4iStSuvJH-pP6c8ml9pPe2iT1c3EWKDE1gzsUsoThkWNWue1gFpxmneUK5vyCGslGDls_Zu13FcHIX0nXymYZN0z5ktAyNlbz5TmWIEjJq4BYQJ9DyrR0rOn6Z5CtiPzDmPzxwpYCUcMVEhTqix52iijbcxVvnak_6Pdo5YO0YZy4R-AQGgtU2lFlPiB-yl29yrJXIWPIqfqTDvNZkoiML3E8OON-zCnqrm_hbIVmLqSleU1Waj8sL30CAyLn1ca0UMVOEg06uYnsnB53a-S1Qy64Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e26ecf0d2.mp4?token=MQeMT95AmKrH8LQBUtQKMN6rgpEPlzOGMK-AA6QeC6mmt_CGkPvyX-zR-uM4iStSuvJH-pP6c8ml9pPe2iT1c3EWKDE1gzsUsoThkWNWue1gFpxmneUK5vyCGslGDls_Zu13FcHIX0nXymYZN0z5ktAyNlbz5TmWIEjJq4BYQJ9DyrR0rOn6Z5CtiPzDmPzxwpYCUcMVEhTqix52iijbcxVvnak_6Pdo5YO0YZy4R-AQGgtU2lFlPiB-yl29yrJXIWPIqfqTDvNZkoiML3E8OON-zCnqrm_hbIVmLqSleU1Waj8sL30CAyLn1ca0UMVOEg06uYnsnB53a-S1Qy64Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک کثیف خطاب به وزیر جنگ آمریکا: شما کار بزرگی انجام می‌دهید
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/678163" target="_blank">📅 21:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678162">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46daf284a1.mp4?token=K_hQSM3IYpBZkYOSaYDubHNFXjb_OFHyYdEJbbK0yKdhWAe-1lLT6w1j10K3YqqP9VEi7N4yMqzjNV33JwBVD3mt0FHO4M6bcwGpgRoQ7DR-IVLVwsIWnA4zfuZIqt-Rba3KeOOp7YA4-Tooas-YWGZR132cmKxo3XnBKu9M-W9pJyBy-z0ByKeQnfp_BMm11UfgkzIRMxhTi7GPJ9Xecd0qIej8yg9FoBsjb-gIOeO2uIwONaAi4b7kwcuSLG8bFqYgi5CP59-ExNlCODkGIju0z9YsaGcJ0lqKD3khx5a-Dd2UTSa_UIgT-pqfj9luy4S5ZpNVUC64T8Np6JfvAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46daf284a1.mp4?token=K_hQSM3IYpBZkYOSaYDubHNFXjb_OFHyYdEJbbK0yKdhWAe-1lLT6w1j10K3YqqP9VEi7N4yMqzjNV33JwBVD3mt0FHO4M6bcwGpgRoQ7DR-IVLVwsIWnA4zfuZIqt-Rba3KeOOp7YA4-Tooas-YWGZR132cmKxo3XnBKu9M-W9pJyBy-z0ByKeQnfp_BMm11UfgkzIRMxhTi7GPJ9Xecd0qIej8yg9FoBsjb-gIOeO2uIwONaAi4b7kwcuSLG8bFqYgi5CP59-ExNlCODkGIju0z9YsaGcJ0lqKD3khx5a-Dd2UTSa_UIgT-pqfj9luy4S5ZpNVUC64T8Np6JfvAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک زرد: مذاکرات با ایران در حال حاضر در جریان است
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/678162" target="_blank">📅 21:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678161">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/678161" target="_blank">📅 21:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678160">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2240c9d4af.mp4?token=lld6OTuqxD6L_A5rRb8gCQOWQMEgouLz4GHrw76fnkkNjyBTS0TDrdbMRXZziKv3TUbHZaaZc_Jn7pQ9Pu6Z5Q47jxotGIXrunFNjBC-OZVJ6lUpR80SlPJP2xBZfn6MPaeYGpyNkg7XyO7MDFBqW11ye4HtWaeQOviZaQwBN5iJQ5LwEpK4JHk-I_u5n6fJMkvlmqd4eGvqYA8z0G2aKcWMNg41iubMxpY2blg92WZCnByB-mYWz3qVw3eB1vYeRUEzMQIXLLSqYGJJLC13pdVaJkTN7iVdNpNJ1p08BtDcx2ZDI6-i_JA3ZsxKQXJ11bfst_lozhV1CiZZC06dgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2240c9d4af.mp4?token=lld6OTuqxD6L_A5rRb8gCQOWQMEgouLz4GHrw76fnkkNjyBTS0TDrdbMRXZziKv3TUbHZaaZc_Jn7pQ9Pu6Z5Q47jxotGIXrunFNjBC-OZVJ6lUpR80SlPJP2xBZfn6MPaeYGpyNkg7XyO7MDFBqW11ye4HtWaeQOviZaQwBN5iJQ5LwEpK4JHk-I_u5n6fJMkvlmqd4eGvqYA8z0G2aKcWMNg41iubMxpY2blg92WZCnByB-mYWz3qVw3eB1vYeRUEzMQIXLLSqYGJJLC13pdVaJkTN7iVdNpNJ1p08BtDcx2ZDI6-i_JA3ZsxKQXJ11bfst_lozhV1CiZZC06dgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راز
کارواشی که روزانه به ۱۲۰ خودرو سرویس می‌ده؛ فقط با یک کارمند
!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/678160" target="_blank">📅 21:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678159">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/678159" target="_blank">📅 21:22 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678156">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ryTrV467Jq30TH6x0lLD5TXm6UyZ8mH1-QMrmuNOgMMH_S64ynhpxqS65RwpaCNCAgtkHx8p3R5lUULwII6NzFTTYvCvpJveIyUHjDcFUlazt8g-AE6b29DCnKo_uz6pnVkgIZbKWaHibkCh0S813d09MKhCyhLfFPxJrnP4Ri_7ZIkchaCu2GoM0AfzclNsFp3DisoDa1zbwEbfNXdMcIpXShmezutWUpo2scYcbj3TlqafPhN8VmT7fb0BsYtPVt30IaXg_rRuwaUFK8x63gize4Ex3f5NSiVAbsuVAQBrva9j5M_ypWY9muk4vIudyBRGLWdTveDaCQcl26vVig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خورشید
🔹
کارگردان: مجید مجیدی
🔹
ژانر: درام، اجتماعی
🔹
بازیگران: علی نصیریان، جواد عزتی، طناز طباطبایی، روح‌الله زمانی، شمیلا شیرزاد و…
🔹
خلاصه داستان: علی، پسری ۱۲ ساله، همراه دوستانش برای تأمین مخارج خانواده کار می‌کند. روزی مردی از او می‌خواهد گنجی پنهان‌شده…</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/678156" target="_blank">📅 21:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678154">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b4a4714e5.mp4?token=Km4cEehB1awTOEwAjdJfPtxAGpzJ0G0g-7nwFQA9zNBQGDz5fBoCusvUH7kN8LJ93eWVZYPZkud8lOzan3JaaiAmSwQYmjnbABC4yFkO8lX_poY-RpoPPjiVEhIocRrP_KdVyqay33a1EO6iloby0wTL2fQyqDW8JHoF7h6x6E31HxsbA--r4lXrBnkGB-P6uAZl1naT1NXCaMTYzWyLbjfxltiK9-yTcwFxmimrfTW5Qmva0Xa6i1sjNW5pwCTkFutKc31_U9hEstrZc0EzekAs6cCdrWpP1qkLNg9fJPsvbss_gA19QtbjdX8X7Ri4a6MMwogOo9Ani8eLf6hIgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b4a4714e5.mp4?token=Km4cEehB1awTOEwAjdJfPtxAGpzJ0G0g-7nwFQA9zNBQGDz5fBoCusvUH7kN8LJ93eWVZYPZkud8lOzan3JaaiAmSwQYmjnbABC4yFkO8lX_poY-RpoPPjiVEhIocRrP_KdVyqay33a1EO6iloby0wTL2fQyqDW8JHoF7h6x6E31HxsbA--r4lXrBnkGB-P6uAZl1naT1NXCaMTYzWyLbjfxltiK9-yTcwFxmimrfTW5Qmva0Xa6i1sjNW5pwCTkFutKc31_U9hEstrZc0EzekAs6cCdrWpP1qkLNg9fJPsvbss_gA19QtbjdX8X7Ri4a6MMwogOo9Ani8eLf6hIgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این کلیپ از حضور قهرمان مسابقات مردان آهنین در اربعین و خدمت به زائرین، میلیون‌ها بار در رسانه‌های عربی دیده شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/678154" target="_blank">📅 20:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678153">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YRJ068uBOUsiYyIYB08-nWEfW27yYLqU0g1cUTNDVrR4QffeyaxVKFPjSOyMhI7nhXKZW0A0a6VlQrKJbGhp1TLZbnIT0l10zw4jeHO70tRvVylYfESSSux8sMRui-Z5zwjOaqBjvwKzf3SN3BYYEAjh9BNDHI_0EmurK4lN2vwG1QClzTzOnZfLq2Er6UHlcioWn4ghsSIJJftPg_cBMBAGB3ILh8emDHBiIyRpySFAvdVAglvdgSVNWIgP2N0QnTmnQ5FFUipsOxBJ31PvQvRH_9yPf47haq7mz7Anwbrv6hFpg2XF-_iXUuTuMT63yTno3XV5nOS6-ex3s9i3Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جالبه بدانید چه گیاهانی حشرات رو فراری میدن
!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/678153" target="_blank">📅 20:52 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678151">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GxhzzU3N_MrXs1SWwYoC30RMMRyAYuuu3bd0SczfKjmhexaqMKSlP6R81phDfQATygnDr53CIGd6RwC6K_2hECNO6Cm4AVWGo_XWXQdM0NbfCgN064S5IGECA9EaFeU2J-LCdgmDE0EewFoehtQZNJxLB5a8ioxmZ2w1dNgJhauaLek-UrOb2SvCRobLmwslxRwB8l8w7x7A5MULMemIlLk5uq3dV8mJQ1etORxuwkPCc8x50WLjiMYjbU_mbYKYqHk3eP4qy1-wZoqEtWfjESCA30tWs6pHq5LLXJk4DppSRye78cmxlMrTPtf3sQ2O89zX-qXmFdwikwLqeNQiOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NHLpk0qsd-1wuPxLUelyBEs60rlo6mLbp7pEBFkYGbD6l-0tI_p3Z8VNSKxF0fkPX9AvT7Y_nLK6KfIMDRslEcEJaW-gBWdkqA_DWKkY1J9x9NDhri7cN5Y2d0CdKQd2pM9PJI2ANSYpOOvSGcSar534uW5tuj-elfkM91TdCycMRKjiPUEHCffAuh6MwT7Bfc1twCbN3KeBGycuNzPBwad5mP84YPBwiFCcb-C0osv3uC2BAEdq6yPXrkFE5OScVLLdxLIc6AvUckhIDjiE4eetcWXxa3_UQp9VxQBWtWUGK8NflPMcpnRymFWDFKQ2Q2aBsiqgbyvUnO13-NorEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پست جدید خوک زرد درباره ونزوئلا: حق با ترامپ بود
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/678151" target="_blank">📅 20:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678148">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKD-cbSk20FLNSXWsF9Gjc2Mj-Via3sFy9deeNkHWRkewvktWjers8jNOWHvN1s46G5R_Oki_Nu6eJ_Gf8tETrk45N_Q268ib6NqtkL6DSJRAokbNmQDXnLyAdH4h2GDVVUA8RfkiPm8zclzWJ9VPHZ7emOIxRYLHqI7zzLrx3Zto7qMzQHGqHCmp1QFewJgdmNVA_-tHmpEKVMpviq_OIR_KvVjvbo9UXG-H1c2QNp3BKIoGsl6vmjfziOdSg7Axzo9hZRZs-N0d6Z9mXAHwMZPvce7TRHJYdLXKelVolN-7t-JgyPDIFZkKOpObs_MUMmQKl8x9_PcWjVB5kLk6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴
اعمال روز اربعین
▪️
فردا سه شنبه ۱۳ مرداد مصادف با ۲۰ صفر روز اربعین است.
#طریق_الحسین
#اربعین
@Heyate_gharar</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/678148" target="_blank">📅 20:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678147">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
از مسمومیت تا برزخ؛ روایت مردی که بازگشت تا حقیقت را بگوید
🔹
00:08:30 هیبتی مقتدر، با خشمی لبریز از مهر، مرا به اوج آسمان برد
🔹
00:28:15 مادر با قسم به اهل‌بیت، جان خودش را پیش‌مرگ من می‌کرد
🔹
00:36:05 چگونگی پاک شدن تن از پلیدی‌ها در آسمان
🔹
00:41:30 طواف معابد تمامی ادیان گرد کعبه و تأکید فرشته مرگ بر اهمیت آدمیت
🔹
00:51:30 ماجرای شنیدنی از مددرسانی امام رضا(ع) هنگام صدا زدنشان
🔹
01:00:30 آزمون الهی برای خانواده‌ای با مرگ فرزندانشان
🔹
01:15:30 علت تبدیل انسان‌های مسلمان و شیعه به حیوان در برزخ
🔹
قسمت بیستم (یک آزمون، سه برنده)، فصل پنجم
🔹
#تجربه‌گر
: علی لعل یوسف
🔹
قسمت قبلی
#زندگی_پس_از_زندگی
#فصل_پنجم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/678147" target="_blank">📅 20:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678146">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
دبیرکل کتائب سیدالشهدا: هر که آرزو داشته در مراسم تشییع امام حسین و علی ابن ابی‌طالب علیهماالسلام شرکت کند، امروز در مراسم تشییع امام خامنه‌ای شهید شرکت کند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/678146" target="_blank">📅 20:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678145">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73a59201c0.mp4?token=AtT5IFGEY7AgMLv5nDHtkacmonuZoBCawiCU6LQBtp8fZpeEdEk_r0Vyn3TF6BmL6w-l7cV6GImVvV5jG1Ii5kN2MyS70bphkr0mlIY9QubbEMx_lmdGpnx-wL0xuw2Lnuc7_y_XZ1-KIecKU9P7wh3NNfOuAcipcraYHVPc4GCi4Sx_PYEgNMEURMNJnGIdlC56pLFVBvZ6pbDuMMOaLrfKvkRgkyTqEUFESP9t0BK83xrJP-CjscEtYhkWHKMz_al0LvoG7ulytPaoq6a7Q8kanaCwyNoerEys9R_XSQIW76S7Kd-TLJIXWT3hEXOphHpI8Z6Rqzo1Amu4EWO_KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73a59201c0.mp4?token=AtT5IFGEY7AgMLv5nDHtkacmonuZoBCawiCU6LQBtp8fZpeEdEk_r0Vyn3TF6BmL6w-l7cV6GImVvV5jG1Ii5kN2MyS70bphkr0mlIY9QubbEMx_lmdGpnx-wL0xuw2Lnuc7_y_XZ1-KIecKU9P7wh3NNfOuAcipcraYHVPc4GCi4Sx_PYEgNMEURMNJnGIdlC56pLFVBvZ6pbDuMMOaLrfKvkRgkyTqEUFESP9t0BK83xrJP-CjscEtYhkWHKMz_al0LvoG7ulytPaoq6a7Q8kanaCwyNoerEys9R_XSQIW76S7Kd-TLJIXWT3hEXOphHpI8Z6Rqzo1Amu4EWO_KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در آینده ربات هایی با هوش مصنوعی جایگزین انسان ها می‌شوند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/678145" target="_blank">📅 20:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678141">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رهبر شهید انقلاب🇮🇷</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YARfU4rBGmfrlwHxVQd95pmq2xHZtUT7LW2deCejXJqwKcX9ZYsRhXkZHvh6EOfMuzT9QILmTIEXWBaLTd9YLeoPv4a00Nh8tq5LMubZtg0_-rlHaAx3UaA6flVQmwSbO5dWiZTC8aNYOBAo3t5YYNPkEiFIoUoJLkaL7sJZAftQrxvjIvG_-AFwK24ZZV55b5-PqzN1aIoieFDEcAfb3RQeaT2BOBF-HN3PsoWwG60nWs7aQ-jgApO28PN95iHw_SBMz5KXxXiwAbqi_sw2mob2y8qyOdvDubeSXsa3TjZimvpMg8ql5ajajQzUK5IDzglJjiXNPOcE-YJLM9dPQw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/678141" target="_blank">📅 20:08 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678140">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
امارات به اسرائیل سفارش فوری بمب دقیق و پهپاد داده است
روزنامه اسرائیلی هاآرتص:
🔹
امارات متحده عربی از شرکت البیت خواسته تا به سرعت شش پهپاد پیشرفته هرمس ۹۰۰، که در ارتش اسرائیل با نام کوکاف (ستاره) شناخته می‌شوند، را در اختیار این کشور قرار دهد.
🔹
امارات برنامه‌ای گسترده‌تر برای گسترش این گروه به ۴۵ فروند در قالب ۱۵ سامانه کامل دارد که ارزش کل آنها حدود ۱.۳ میلیارد دلار تخمین زده می‌شود. اسناد، یک پروژه تسلیحاتی دیگر به نام «یاسمین ۳» را فاش می‌کند که شامل تولید ۶۰۰۰ کیت بمب هدایت‌شونده تنها در سه ماه است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/678140" target="_blank">📅 20:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678139">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjHkmLjEMVMzMyZMXEpFH_-0eRN1ddODDHZ0eSm4xPEfBL61UHRr76NlXhRbGYU1ou7rp_qyjryyMVHFNUQPPv8S5Q08KKOX5l-RniPm4-SJwkUrlbA1N0YpeC9k2nEX7myd3atqLuaSXbK119cBsjztgqOKZ_59lxek6Mz1ctQ51rDmGGbv0_h7RC-gyHgw9CHozEfWG4xdm87baulqyHKNtW2OJgCj9nOLzTB94VlaycVsABmhRy6bPYu8nGDrV8hNJoQe7UJHJ1BwjIcr5dQly7Ls9X5k0e5Tb-mHm0BIgpzHKo7KzFw43i0zGSQe_3VAXpGRk9wJQ4Z5idmItw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
منابع غیر رسمی از جدا شدن امیر و رهام و منحل شدن ماکان باند خبر می‌دهند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/678139" target="_blank">📅 19:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678133">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rNis4YRMCqr23D4PPWtErjshrpkRZjejJyOf1o5Xju2Ca7z3Ww-WH6IDkbm_xz2Ai6TVUGfDsWCmSD0EEbjSw7IeGGS6Jgr_dCcqsuLb8HWuUgOkcCmJ9voDgr64749A5KcDSrclgwZAoG4f3nEhbp8E5JDffFHfIu0FESTWjk5F3odddIPX3SOVcon7JMQvAyZWCO98gOOs_6jDH1mWnRtdavFkJz9C2Qmd3hEYiuy9eq4d23S_a7F9lm7Ejsok7h0iw0BSBMLc_cCCarcvikRipzQEXYeWgtQkgTI1bqJsYhnulHuJQFhzCsO5efTCRfiyy90t-WLFWCFyQkkmfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zg45gV_EJa6fCU6LXpGkNCgotc2rBpCtu7orGFZZDfz8oB-Bv-vkVNRM8XAvvqr0fK8e67Tyu5ctBQgJe2G0GN6FKvSrh5Uc43xyIBM3d8AzUvP360xiyoNwh4U5Dd0eYqAd9IuOqtAp3KitZMRchWlwVLPtAeMHDP5Yk5xXL_MbvkaSmyXPEpQDSshe_9AmManBUb1Bw15YVmEuPbij99fTkYXNM0qR8EzMo-MNXXmEGqtMdtl2nQuYPVrU2Ep_E_VkmcXVnOpXKhKuIO2xtLBbcobbeuRL5YU2FFaNlGpybwVmgLVnTfLLC3-m4CvC3xQ6-LIK_1xg2h6mKIIdig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oxUwYkOGLFGNVTaWHwsu9Vf_fCoi7J__8-yWW6uZ7S7vOyNYoVjE-wM7iRi7UBzoGKapDCPgkeipPnSzvOyEBJZDaDMoe7bkZsNMeVhxUNmb7rAFDNOLwQy__57VX1VYG-sGXZm9XMX-2PndxmzsJKSBV0IMbXszxdTkF8cwaSbxiVZyFWVFNoMPNn2yXnMLdRTHnvpIhZlAUWInpjONV9IOOGdGYTkZBwHGc4M9cRj8QANfWU6pDZKC7kil4Snxp2s68yBtw_a6xKDw3b3Cxnl30xCYcH7yuH_4nJmc2FSGvj2WKgmyj_vyUS8_uRbAqHekQA9otNRVPhlefdIjGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R-x1yxOxDPS-hl7dnMoNeNDJ6VW0ovzYgoBPDeB_FOPyazlXNAnZ_kMh9_YTOp_DkDJchKqx2rgkDH7kFCb12bcQamTPylarbK8IAkKpH_RJ-XxadF5TiRK2EXn5fz-IwoVtY_1uqBPxZgzZd9xwv2hP9ZCj8wHCOE34SCG6B3fUWv5hMERtfBrDzkeSMEaYd_ATAziJSz1iSdn0YPxwbLMx4N7QjSFQh-JOeCkM1q6YbhXyFRv-nQTRmBV4eM3fEHZgnTJrWoaFBJH93896O-5Gdhp5kSn8KvNVbJrNvZXXJbM8VeiN38MEHQDfjg3ZLu3cohPYoWeW1fpYl91dtQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
میدونستی
نیازهای مهم بچه‌ها که ۹۸ درصد والدین
نمی‌دونن؛ چیه؟!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/678133" target="_blank">📅 19:31 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678131">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebee8d7d54.mp4?token=JB6MpWvT_uAtpxpQE4HFWVKG8beCFdtUat-3cqrFauStC2NmJNDkq23wPuanBzI3gL-aHryvHPajUMMclCFhgYVdNJRDe8P6ky9_BCR4NuOE1mqHM3eh4-NcepyH2uu7xAMzloTpB6BH13vCSAj_LrYAJgHksrO4f3oyYRMrGBHnvwQroS2mw4weft3GTf6PqHVeDJcYWN84H9bbs_SL2BoN3Fp5nWzcE2cAA0sPt7hqOGQd6WWj6rSXEtcmrWT96vgVtUSZDyOjoqdJOEDvZhel9txc45HrkagfUvZbNuNctdnt8UmuWfzHSJMIub8zhXNxSOQ1erZw5gaJvUgdYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebee8d7d54.mp4?token=JB6MpWvT_uAtpxpQE4HFWVKG8beCFdtUat-3cqrFauStC2NmJNDkq23wPuanBzI3gL-aHryvHPajUMMclCFhgYVdNJRDe8P6ky9_BCR4NuOE1mqHM3eh4-NcepyH2uu7xAMzloTpB6BH13vCSAj_LrYAJgHksrO4f3oyYRMrGBHnvwQroS2mw4weft3GTf6PqHVeDJcYWN84H9bbs_SL2BoN3Fp5nWzcE2cAA0sPt7hqOGQd6WWj6rSXEtcmrWT96vgVtUSZDyOjoqdJOEDvZhel9txc45HrkagfUvZbNuNctdnt8UmuWfzHSJMIub8zhXNxSOQ1erZw5gaJvUgdYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ساخت روزانه ۱۰ ویدیوی انیمیشنی با AI به صورت رایگان
🔹
سایت Digen AI روزانه ۳۰۰ اعتبار رایگان برای ساخت ویدیو ارائه می‌دهد که با آن می‌توان حدود ۱۰ ویدیوی انیمیشنی تولید کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/678131" target="_blank">📅 19:10 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678130">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b33d8fc781.mp4?token=DHUJFLqqarUZkf5K0KnCs5Oc5fdSZfB15G0fHQslU6qQ5ujTueGxcDoUmvVnza9UAWvlOAbA7DqteWtrA0qfVUizOIQUfc0E0svbpJszG0KnbPZukdL8Hxs5fkU1TJ9Dsal_w08OazTxMstgStzpNJBd35vCbRTq6gRUZPItc5oyBVM6YK0B4uOrdegXOzx1hKxzLu7gibmkG-NldPl_RAITpp1vdkkRFa7SXbBYkjY8-CndUzGf0QcBmJOvJHxiA7DplCCN-2vog748WHc6bAuj5QdD5gcuCoOW3c8rDk9wuSd0-owFdAr18dZ_Yl0ZhX58nT2BN1yW0DjngOQlYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b33d8fc781.mp4?token=DHUJFLqqarUZkf5K0KnCs5Oc5fdSZfB15G0fHQslU6qQ5ujTueGxcDoUmvVnza9UAWvlOAbA7DqteWtrA0qfVUizOIQUfc0E0svbpJszG0KnbPZukdL8Hxs5fkU1TJ9Dsal_w08OazTxMstgStzpNJBd35vCbRTq6gRUZPItc5oyBVM6YK0B4uOrdegXOzx1hKxzLu7gibmkG-NldPl_RAITpp1vdkkRFa7SXbBYkjY8-CndUzGf0QcBmJOvJHxiA7DplCCN-2vog748WHc6bAuj5QdD5gcuCoOW3c8rDk9wuSd0-owFdAr18dZ_Yl0ZhX58nT2BN1yW0DjngOQlYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسنوند مدیر مرکز توسعه پایدار انرژی: عمان خودش باید عوارض بدهد، نه اینکه شریک ایران در تنگه هرمز شود، عمان ۴ پایگاه تامین لجستیک امریکا را داشت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/678130" target="_blank">📅 19:08 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678129">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
‏
ادعای خوک زرد: رهبری ایران به شکلی باورنکردنی فریبکار است
🔹
آن‌ها درخواست برگزاری جلسه می‌کنند؛ حتی بعضی‌ها "التماس می‌کنند". گفت‌وگوها آغاز می‌شود و حتی برای آینده نزدیک نیز زمان جلسات بعدی تعیین می‌شود، اما سپس با افتخار اعلام می‌کنند که هیچ مذاکره‌ای در جریان نیست، هیچ موضوعی در حال بررسی نیست و فقط با "عمان" در ارتباط هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/678129" target="_blank">📅 19:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678128">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V-l7VXkezWazeonTwDMBK-WjfA5sXXkj_eaUWXlbYcdciy3CLnbyiyMJeqg-WRf0Ly-FsETLYso01GJxbW7HUaHN9H9jxug_0No-Of6SlOnD2mKbh206k-K5IH8P3fGNMWlINQw2NTJQSd0-e5gNmDILB0kxvxfWV5ykHyIMmsDux6aNW0_HWKcJPimieVHpM713bXBnJZkZ96FePvQVcyTBRIWFiVVxyTOO_ywe-WXcxrlQniumaM-n4_qn-73AcZlNVN0pqIW6TZIYgWIO3ZVv7M6H5r7dnyTUiMo3MHeecy2rlEryNZVm3NWF77cmrB9vpBJCW175PVutv5ImRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خوک نجس: هیچ چیز بدون خواست آمریکا به ایران نمی‌رسد
ادعای ترامپ در تروث سوشیال:
🔹
«در حالی که برخی حتی می‌گویند ایران برای برگزاری این دیدار "التماس" کرده، مذاکرات آغاز شده و قرار است در آینده نزدیک نشست‌های بیشتری برگزار شود، اما آن‌ها آشکارا و با افتخار مدعی هستند که هیچ گفت‌وگویی در جریان نیست، هیچ موضوعی مطرح نشده و فقط با عمان در ارتباط هستند.
🔹
سپس طبق معمول ادعا می‌کنند که تنگه هرمز را با قدرت اداره خواهند کرد؛ در حالی که این آبراه هم‌اکنون به‌طور کامل تحت کنترل نیروی دریایی ایالات متحده و آنچه ما "محاصره" و برخی "دیوار فولادی آمریکا" می‌نامند، قرار دارد.
🔹
هیچ چیز بدون خواست ما به ایران نمی‌رسد و تا زمانی که توافقی حاصل نشود یا ایران به‌طور کامل تسلیم نشود، هیچ چیز هم نخواهد رسید. ایران چه این واقعیت را بپذیرد و چه نپذیرد، ما در حال گفت‌وگو برای حل مشکلی هستیم که خود این کشور طی دهه‌ها ایجاد کرده است.
🔹
موضوع کاملاً روشن است؛
ایران هرگز به سلاح هسته‌ای دست نخواهد یافت.
»
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/678128" target="_blank">📅 19:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678123">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/078d1d0337.mp4?token=gZ-FWCP-qsPJQCu2czwdiGkHitHqqCbeWGOB_Y-E78nDcbsy9uI5BDzBnKFPseNhEkVn5cMEub13sly7fN0qtDV1Rm3RKf7pGkIKg5_aKoaO1hvv2IfbvL8vazgZrYIK5nRj2EDWcrPw9R2oyv7pSp5CNpQHq6Pc6YLhTXyeHz-jsiDUeLT5M58Wn7PvH6LiGn24MOMVHjGO4HPROk63ob3e69DR-uWlpdToFvhH4nTlDy0qaOud-RWRyS3uc5JVXxOeQkVMXJ_FdkMhfJb5rW9VE0VIjO_dm3W5L_xHQJN43p2kbWs3s9sg7PfWFMHJzbjblhYu2rGd04lIQGC3bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/078d1d0337.mp4?token=gZ-FWCP-qsPJQCu2czwdiGkHitHqqCbeWGOB_Y-E78nDcbsy9uI5BDzBnKFPseNhEkVn5cMEub13sly7fN0qtDV1Rm3RKf7pGkIKg5_aKoaO1hvv2IfbvL8vazgZrYIK5nRj2EDWcrPw9R2oyv7pSp5CNpQHq6Pc6YLhTXyeHz-jsiDUeLT5M58Wn7PvH6LiGn24MOMVHjGO4HPROk63ob3e69DR-uWlpdToFvhH4nTlDy0qaOud-RWRyS3uc5JVXxOeQkVMXJ_FdkMhfJb5rW9VE0VIjO_dm3W5L_xHQJN43p2kbWs3s9sg7PfWFMHJzbjblhYu2rGd04lIQGC3bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚿
ماشینت رو مثل روز اول برق بنداز!
با نازل کارواش سرشلنگی بدون نیاز به دستگاه کارواش، فقط با اتصال به شیلنگ آب، فشار آب رو بیشتر کن و به‌راحتی ماشین، موتور، حیاط، پارکینگ و حتی فرش و موزاییک رو تمیز کن.
✅
نصب آسان
✅
پرتاب آب قدرتمند
✅
بدنه مقاوم و بادوام
✅
مناسب شستشوی خودرو، حیاط، باغچه و سطوح مختلف
💰
فقط ۸۹۸ هزار تومان
🔥
قیمت قبل: 1,098,000  تومان
🛒
فرصت رو از دست نده، با کمترین هزینه یه شستشوی حرفه‌ای داشته باش!
خرید از سایت
👇
https://memarket24.ir/product/brief/58365/180124/</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/678123" target="_blank">📅 19:01 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678120">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORBKVVuYrbILwLlBJHJujcE0xl6e98IhoQ7FAPG6veLHSxYYA-2FFjNDTH-xp5cswaMKTraWT3QzRNOMwNnoguiVYDA3pefmHVC-w9IWxRanBqjbx7pQzHHx8zHdSUFCAtv6CATJLbIAJ27YcxCkLCLcUOW92ej02ko0DiycTVSFCCnzHz6MJbrvuB1ZWq8MW6bJGwPtqbl5FJ-es_tDH-npAuw3uaUULxQUJ4yRf6YuWIFE32J8-CEvJlevTjRD_US73kKEgRMOonPxa18IMlK3wrWPdUcNYwB8VFklUVvjGnAPeqATC9k4BgJcq_GGzo5QTNxPUUcyPJgCPX0O8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایده غیرمتعارف برای حمله به ایران | پنتاگون در جست‌وجوی گزینه‌های تازه برای فشار بر ایران
🔹
گزارش اختصاصی سی‌ان‌ان از درخواست فرماندهی مرکزی ارتش آمریکا، سنتکام، برای ارائه ایده‌های «خلاقانه و غیرمتعارف» به‌منظور افزایش فشار بر ایران خبر می‌دهد؛ درخواستی که به گفته منابع آگاه، بازتاب‌دهنده دشواری واشنگتن در یافتن راهی برای پیشبرد اهداف خود در رویارویی جاری با تهران است.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3235318</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/678120" target="_blank">📅 18:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678119">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b886a5807.mp4?token=aaI-Nx_QgZ84BmRJaKsBEkexD4lfpx4ViGeKKvY55iG2FRrhOZVBWyOMyfmzIYMenrDyOwwdxBvotQ9un3SXlHqwX3fJuV7FDqEEinnWeTotoKEfXfau0khgs8MAoHn5gbcXGwTkbayI7oCIjmy_UI5q4w2I2UfiX18QfXP63pbjSg8X-IYdk5NPKF1Eh-8O6go2bYvOc5Mu3C2VQ-LiVZmHbIncPIPrCUPv8AJSpfiMfsZ5jcNTW4W6f46_LYsp_1oPrOddQb8ncfvTsdYfONRXGZonG_QH1ZGd3183ocVN3YzW5fbUfFbrNffBLEP97sx6F9aUZi25yvQj__YD9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b886a5807.mp4?token=aaI-Nx_QgZ84BmRJaKsBEkexD4lfpx4ViGeKKvY55iG2FRrhOZVBWyOMyfmzIYMenrDyOwwdxBvotQ9un3SXlHqwX3fJuV7FDqEEinnWeTotoKEfXfau0khgs8MAoHn5gbcXGwTkbayI7oCIjmy_UI5q4w2I2UfiX18QfXP63pbjSg8X-IYdk5NPKF1Eh-8O6go2bYvOc5Mu3C2VQ-LiVZmHbIncPIPrCUPv8AJSpfiMfsZ5jcNTW4W6f46_LYsp_1oPrOddQb8ncfvTsdYfONRXGZonG_QH1ZGd3183ocVN3YzW5fbUfFbrNffBLEP97sx6F9aUZi25yvQj__YD9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فراخوان خبرفوری | به نیابت از رهبر در مسیر اربعین
🔹
صدای زائرانی که در مسیر پیاده‌روی اربعین، ارادت خود را به «رهبر شهید» با قدم‌هایشان نشان دادند.
🔸
پیام صوتی خود را ارسال کنید
👇
#زیارت_به_نیابت
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/678119" target="_blank">📅 18:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678118">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gbgb5NsG1H7hMTEEw93hA_edXoHlG-_SlIs5Dd6eOdfEeWQYTekfgJ7G0NmufRL9yG2Gzuouj6OnZtdkyruHlVNix45PCKRPzslgOmxbAzBkWXwqAsSm6q2ExiOUARf2DBviAujnyL3EnJCiZrycIMgVxGSa5q8DH_7F7goT8AB_H7zaMoIYTU4qKD53TSjYJG-mszY4_WOvajHj_DuvjlvpTbVGrQ1f7A-Ru75DGyFTxhZQcBmfQOzsAnszxnrvDTYOtbp4Tvnkck8j_zpKezYkKtTpef-jnIgBwdugNBhZX7mQ2j3HCW6CCnamEZQWayPN_kJjgzsbu5I4MbubzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر جای بدنت یه علامت داره؛ کمبود ویتامین‌هات رو لو می‌ده!
💊
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/678118" target="_blank">📅 18:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678117">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ageWgMSaHM8-EwtASLoc8YAjr0EkSfMwHAe7F-TkWJALZZP7heL35ezw1885ZdQ6QpgRnLaZmtfEiO97BxnhtLRYABKi-dvydmgPTAkWin7Yb0oc9cQD94B6JnIzvVzRfiYm52KkFp1DLx4aY4dbOWpQOU08tVlSfCFIZp5TYI-efqxORlt3Z6Zy9zF1c_DM8oVDmceZn4dftN4lWYPtbXoq3lzhibFpzJ5RTIPV8KLJXbYku63xYIyUFjVzntoGW7mfAhO_HYbrmotfLhIBBkwdT8BK02qcS5VCYIfrld5sCc1cPULZxMjubDdNvZVcRwJi23bwSKRk-SgkbEuzyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
صنایع خلاق؛ پیشران جدید رشد اقتصادی در عصر اقتصاد توجه
🔹
نشست تخصصی «بررسی ظرفیت‌های تأمین مالی و صادراتی وزارت ارتباطات و فناوری اطلاعات در حوزه صنایع فرهنگی و خلاق» با حضور سید صادق پژمان، مدیرعامل مؤسسه کمک به توسعه فرهنگ و هنر، حسن میثمی، مدیرکل توسعه و فناوری‌های نوین و تحول دیجیتال وزارت ارتباطات، حامد لدنی، مدیرکل دفتر راهبری طرح‌های کلان فناورانه وزارت ارتباطات و جمعی از فعالان و مدیران کسب‌وکارهای خلاق برگزار شد. در این نشست، توسعه زیرساخت‌های تأمین مالی، حمایت از صادرات، تقویت تولید محتوای دیجیتال و گسترش همکاری میان وزارت ارتباطات و زیست‌بوم صنایع فرهنگی و خلاق مورد بررسی قرار گرفت.
🔹
سید صادق پژمان در این نشست با تأکید بر اینکه اقتصاد آینده، «اقتصاد توجه» است، گفت: «در دنیایی که مهم‌ترین رقابت میان کشورها و کسب‌وکارها بر سر جلب و حفظ توجه مخاطبان شکل گرفته، صنایع فرهنگی و خلاق به یکی از مهم‌ترین ابزارهای خلق ارزش اقتصادی، توسعه نفوذ فرهنگی و افزایش صادرات غیرنفتی تبدیل شده‌اند. ایران با برخورداری از پیشینه تمدنی، سرمایه انسانی خلاق و ظرفیت‌های گسترده فرهنگی، از مزیت‌های قابل توجهی برای حضور در این اقتصاد برخوردار است؛ اما تحقق این ظرفیت، مستلزم تغییر نگاه سیاست‌گذاری، توسعه زیرساخت‌های تأمین مالی، تقویت نظام مالکیت فکری و حمایت هدفمند از کسب‌وکارهای خلاق است تا اقتصاد فرهنگ بتواند به یکی از پیشران‌های اصلی رشد اقتصادی کشور تبدیل شود و برای این هدف نیازمند همکاری و هم‌افزایی بین دستگاهی هستیم.
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/678117" target="_blank">📅 18:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678116">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔻
ماجرای سیا ساکتی و صندلی کودک!
🔹
صندلی کودک، فقط یک وسیله اضافه نیست؛ «کمربند امنیت» فرشته‌ کوچک زندگی شماست.
#سیا_ساکتی
#راهنمایی_و_رانندگی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/678116" target="_blank">📅 18:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678115">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95ec6b5082.mp4?token=H7fTFWcIUoo4N40UWLIzqIIjCXYyj9z_o6rqr3SrlXQ5CSuQoPTDRJktvoNUDdEG78SgdLr4BcH8-VzzYiNA5bk0Hrr7E5eBWU4d_ZuoOAUTozShKG6H3trsUSVKLiOZlt4_jIINgK6wW0zi2iWwCwWX5RJCE6KY2u00JNGgZ9UXTt_-dlXWzQb9EnXGhmuFLqsA7Itsbpvl5IrBu7ZAJc-WqmG4-3oJYbVgoQatPf-g6eqRaDxVqyjqW6JT2oYiuM6v0Dn_mdkKkXuukVMADcN-ohDYRQj6r9YN1QsTcmgdZHpu3CzDl8j4WDlIjT71BYs7CRTEc1yUHcafyqr0VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95ec6b5082.mp4?token=H7fTFWcIUoo4N40UWLIzqIIjCXYyj9z_o6rqr3SrlXQ5CSuQoPTDRJktvoNUDdEG78SgdLr4BcH8-VzzYiNA5bk0Hrr7E5eBWU4d_ZuoOAUTozShKG6H3trsUSVKLiOZlt4_jIINgK6wW0zi2iWwCwWX5RJCE6KY2u00JNGgZ9UXTt_-dlXWzQb9EnXGhmuFLqsA7Itsbpvl5IrBu7ZAJc-WqmG4-3oJYbVgoQatPf-g6eqRaDxVqyjqW6JT2oYiuM6v0Dn_mdkKkXuukVMADcN-ohDYRQj6r9YN1QsTcmgdZHpu3CzDl8j4WDlIjT71BYs7CRTEc1yUHcafyqr0VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای مضحک نتانیاهوی خیال‌باف: اکثریت  مردم ایران، اسرائیل را تحسین می‌کنند
#Demon
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/678115" target="_blank">📅 18:30 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678113">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5466c4816.mp4?token=HNiuoswXUJJlD90funrwe_xhsXeqDhpsWpqf4qdhgRaZsQHe3iT-sPozZ3TZy8jizvwvQtYQ3yOFXjWG7KKMIdcLhs2D7Le61sXwjA0f3TmbM58l2cZMdxnrpnZf7lf4_KjW4FHIwe1VFQuBepLgTHzINeuF6-k2UXMS_V9FgDT7q5TZnmajRZmSoKx2cFDpiTLuvoduiPnP-1fgLHC9-DF8cUF-O3bbp7VLtX6DensZxv_kWg0CaQa_Wnfun6bZQvitVUpWINbEL49A5X1kbX8kQULEOCJzwekHa_H3AiOsLlUvPh8OixJdUpWbZ-ozkBZpTXv8GaB4soQONy7Pdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5466c4816.mp4?token=HNiuoswXUJJlD90funrwe_xhsXeqDhpsWpqf4qdhgRaZsQHe3iT-sPozZ3TZy8jizvwvQtYQ3yOFXjWG7KKMIdcLhs2D7Le61sXwjA0f3TmbM58l2cZMdxnrpnZf7lf4_KjW4FHIwe1VFQuBepLgTHzINeuF6-k2UXMS_V9FgDT7q5TZnmajRZmSoKx2cFDpiTLuvoduiPnP-1fgLHC9-DF8cUF-O3bbp7VLtX6DensZxv_kWg0CaQa_Wnfun6bZQvitVUpWINbEL49A5X1kbX8kQULEOCJzwekHa_H3AiOsLlUvPh8OixJdUpWbZ-ozkBZpTXv8GaB4soQONy7Pdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
السلام ای شاه مظلوم و غریب
السلام ای آیه ی امن یجیب
السلام ای نور چشم مصطفی
السلام ای خامس آل عبا
فرا رسیدن اربعین حسینی تسلیت باد
🏴
🖤
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/678113" target="_blank">📅 18:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678109">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E7eWNDaLRqct5BlsA56U6mR7IrXXVX_uEg8D85bFfC4eEGEa3MnL-5VrI1a8ZP9q0Oy0tPI5lB_kl1I7S9wS4rdfObdbWJ7gwLyvvMB77NtI99OHOi-oF49RqJmBXiSdAWyPpOUXGfJEvdzrmf613HmeRt8diYkN0ooAcoybSK3Xq2nlkDfiuKM5fqYZpnhmtUL242Cfqsl-_-fNm73P-mkT-wf7ea3ZDYQLkEUiSwlnZyMYpv6VQqoieQu7gEn4yE6g_BGISN2G7TPtPs_X-aqYZzMSOCzQhXOCAvgmqY_QDVPk4NcvdX9dPxYATQQ0OqB77h_Hn-4Ov9T5a27G3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uzG18SaRd-XVh61lrGUL99xqUmJHuJ40mVec33zPJuWf8ncYJeLUmLq7mXd6-WJ5r-3Y3lQ_5edzmqAUUP7HSCNqv4dy6vMzWFTR9UOG111GTmDNycthuB72A_XTkawC5UnxbI2EBPtAw8PRk6wq-PNitJZA9QTcR-wXN88oYjXdjClgrBBnilBgI4E4jggDFzxoxuTrol-s3-aCUj_-rhnTbNa8IiT-FD6LbZJrXQjuOChkVYSvQkcAQkLLTmUPoU4ycw7B87_qOnmfX7TUSpe51lqc-_8P_tkA8btdGoeh-ZP3laYUCVqWzC3miP33hsLFkkw85hxCRp9Ez08f6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هر کشور چقدر برای توسعه هوش مصنوعی آماده است؟
بر اساس آمار، دولت آمریکا با امتیاز ۸۸.۳ از ۱۰۰ بیشترین آمادگی را برای توسعه هوش مصنوعی دارد و پس از آن، کشورهای فرانسه و بریتانیا در رتبه‌های بعدی قرار گرفته‌اند.
ایران با امتیاز ۴۸.۴ در رتبه ۷۶ جهان قرار دارد و کشورهای عربستان و امارات پیشتازان منطقه در این زمینه هستند.
نکته قابل توجه این است که ایران در مؤلفه «ظرفیت سیاست‌گذاری» با امتیاز ۸۴.۵ وضعیت مناسبی دارد، اما در بخش «توسعه عملی هوش مصنوعی» امتیاز ۳۷.۶ را به خود اختصاص داده است.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/678109" target="_blank">📅 18:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678107">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
اعتراف بی‌سابقه در پخش زنده: ما کشورهای حاشیه خلیج فارس آلت دستیم، اختیاری از خود نداریم!
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان عربی دنبال کنید
👇
@AkhbareFori_Ar</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/678107" target="_blank">📅 18:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678106">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BNnpTC9LfUH3RM60Et8itoRy1DZ62d_qYwyWiS9MrNSsUAaR8FsnnUhrHxjIK7MLr4ktyCFMOyuF7r4NZNIqeWGFyRFk5DktXSEYehkv8WwqQP-VkSaKmnm7zulScE6iZEaSBU9FDiLZhWERYa_EmGM-IrBo_fxo2R9yTuf_BWHHgK6O8iPVVT3RSpKwnEhavkj64pA97b2NpQ_to6ri38KL_O0t4tyoeWWu2oEdvQp9BBAwCAgEewQIcvkzjLvbC4pF-K3PEJqvmC6mbAYdcCn_ZchC8Bj8PAc4NdMP7qo5-DZNwEpbqeBHQWCMlJvkfFz_9jy1AT61kUbKSAUWag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طلا یا دلار؟ کدام یک پس انداز بهتری بوده است؟
برخلاف ارزهای خارجی هر سال به دلایل تورمی داخلی کشورها بخشی از ارزش خود را از دست میدهند، در سمت مقابل به دلیل تغییرات قیمت جهانی طلا میتواند رشد دلاری هم داشته باشد.
در سال های اخیر، صندوق های طلا ابزاری مطمئنی بودند که زیر نظر سازمان بورس فعالیت میکنند و امنیت بالاتری از حفظ دارایی های طلا در خانه دارند. یکی از گزینه های مطمئن، صندوق
#جام_طلا
هست که میتوان به آسانی تنها با چند کلیک آن را خرید و فروش کرد. برای تحقیق و بررسی های بیشتر میتوانید از این لینک استفاده کنید.
خرید آسان طلا</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/678106" target="_blank">📅 18:08 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678104">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_n5_SGJ2GrkP4QWQrYp7PhwI9Jh9vLDukYpy8rAZaIGRuRD9fhdkyXcHnQUrrblV2xTCr2q5IUYA5O_6NYSssmh_3kapDJzcgE9HdBWadEOLFlnAJIhvKXxSgUHJsHVIJxWKhlfbmdlRu_wmRJkKdV28y-YlJvwunhFi_0jXnuN1b6xIhjid5J26spcAqA-B2E8gDxzunDYjvnBAk7KwNmmaIyYUh8oQzkD6B71sFgU05yXAgfFFP5i0eHu7S4vABsEeqSVY_CUldTVzCDyRyUnP5z4AG1zzQixBnO1hJgK4EF5RAzJ5-0BZ4OhFfgie6VixnQeJkCVxUGvFJSGLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
♦️
بالاخره اسرائیل نابود می‌شود!
تصویری دیده نشده از رهبر آزادیخواهان جهان، حضرت آیت‌الله سیدمجتبی خامنه‌ای
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/678104" target="_blank">📅 18:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678102">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OPfaKJ3h6hlx6a83ZezhNOLEiRCZkM3rrJj8vbx36IRrD3XnjcNjC6eerw2qxTm2cGRSEWu3UGDTuQPgViEkxVUNxjdw-dUkB3MBEK9xLTNJTDQOJyEYD_5ZmcR0B7mgMx8cTZ9SnjwqUiULGvrFrtFCt03hYzSY2ZaULs4nNs4rArJs8S1G1yRW7B9XURF6nIS5gU_pMmt_dkm3N8Z7x_hhyplEfgG5xHubVpmKgSAFn34KcdY211xpA3xcHb9XnXUUKVMNm_I-MfXHb9bBYcg7x0MuF4q9tMCILMOzlBU1LyKyjV34EtcOsVz6puIyORoSSCkqGL9Z7nobPY1d3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرمانروایی که از دل آشوب برخاست؛ نادرشاه افشار
🔹
نادرشاه یکی از برجسته‌ترین فرماندهان تاریخ ایران بود؛ مردی که با قدرت نظامی، تدبیر و لشکرکشی‌های گسترده، بخش بزرگی از سرزمین‌های ازدست‌رفته ایران را بازپس گرفت و دودمان افشاریه را بنیان گذاشت.  رویدادهای…</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/678102" target="_blank">📅 18:01 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678101">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/678101" target="_blank">📅 18:01 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678099">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
برخی منابع عربی از شنیده شدن صدای انفجار در امارات متحده عربی خبر می‌دهند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/678099" target="_blank">📅 17:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678098">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f75305259.mp4?token=DQO8f6m02wxeTjc-dS63k-HN1_Z2sd3dzdvTa4YRwCDdW6jzFROM-brrFa_Obqwhn0lyvo8Yra8yms2QmLS4tBxPoKqEDehvsrElqveejCiRWrlozWQtXm2spAcKnTcvZPTHlBtq2YlnBZQsMwdnzkd45cHxqeGkMgKXTRYPp4KXiVQY8Y5gR67nBx5XDrAc9KE8CQkRLjWqyjkQUBXP3kr76aGs8zZAeD0eBfi4XIUQlMGJXssz6Gjq2BN225dCqlLs0ald3-VxkuhnHSfU25Oh-6Cm-i2QaeFpw90SNCHThDU9of72SfMhR6OmN1ZNTljZFe7cYPNJZyrOsTgcuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f75305259.mp4?token=DQO8f6m02wxeTjc-dS63k-HN1_Z2sd3dzdvTa4YRwCDdW6jzFROM-brrFa_Obqwhn0lyvo8Yra8yms2QmLS4tBxPoKqEDehvsrElqveejCiRWrlozWQtXm2spAcKnTcvZPTHlBtq2YlnBZQsMwdnzkd45cHxqeGkMgKXTRYPp4KXiVQY8Y5gR67nBx5XDrAc9KE8CQkRLjWqyjkQUBXP3kr76aGs8zZAeD0eBfi4XIUQlMGJXssz6Gjq2BN225dCqlLs0ald3-VxkuhnHSfU25Oh-6Cm-i2QaeFpw90SNCHThDU9of72SfMhR6OmN1ZNTljZFe7cYPNJZyrOsTgcuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚗
هر آقایی یکی از این جاروها توی ماشینش نیاز داره
👨‍🔧
🎥
برای دیدن کاراییش ویدیو رو حتما ببین
❗️
✅
سه روز ضمانت بازگشت
🏠
پرداخت درب منزل
تعداد محدود! همین الان کلیک کن روی لینک زیر،
تخفیف ویژه
رو دریافت کن
👇
khabarfouritel.affdn.com/lead/44273
➖
➖
➖
➖
➖
➖
➖
➖
➖
5000 محصول تخفیفی دیگر
👇
khabarfouritel.affdn.com</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/678098" target="_blank">📅 17:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678097">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0geMGIEh1G8ETTKnAArdBkzTjAuMMINHswIjg7QICS2chY1xdO4Cu2W2sfAk57R2F2a-8akUSj899HJnzr_BhnulF1PqhHAt8ZltNV1-KdMkXtUCKFIziVC6LuXqhDKZwB-9iUfO2477YN7ALrZnBJ0zjuPGgOv3LIKsnfe5T0bMKmu_UpfizmhZ88r70QqQmm_0wvB5CEUeLd_BiVNPtCdRHZwbTgVTFXzHstXvcdomO-g_w-mxB-s3y9hGViQ--FvITx27YDH_DVTysLuZlfbO6wyiaNaQljylUwMrlIWLLsEPgnJ1d3qh0gwjubStP8IeiwMCp_lvE_Yg_lzlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روایت مژده لواسانی از اولین زیارت اربعین مادران داغدیده میناب؛ روایتی از دل‌هایی که سوخت
🔹
مژده لواسانی از روایت مستندی با حضور خانواده‌های شهدای جنگ رمضان خبر داد که اولین زیارت و اربعین آنها پس از شهادت فرزندانشان محسوب می‌شد.
🔹
لواسانی درباره روایت این مستند عنوان کرد: من هر ساله در اربعین حضور دارم و معمولا برنامه‌ای برای اجرا به من پیشنهاد می‌شود که همیشه استقبال کرده ام. اما امسال به دلیل ماهیت گفتگومحور و متفاوت این مستند، اتفاق بسیار ویژه ای برایم بود. به نظرم الگوهای تکراری مانند حضور چهره‌ها و مهمانان معروف کلیشه‌ای شده است، اما این فضا همچنان بکر و تازه بود و خود من نیز از آن تأثیر عمیقی گرفتم.
🔹
مستند راویان پرچم سرخ به زودی از شبکه یک پخش می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/678097" target="_blank">📅 17:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678095">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/069f15d0bb.mp4?token=Ska2EqK5tWie-3eSgkGj6gXusKIgFg3zNdig7J4HaXS2tu10XG-IEBC-YSUDylrRaKbwnKTFXIR7fhc_dKcJKeXsANPDqqNZWEm8VNUO6f1tPGnqIJqsKO3EP3AZW61r5hkeSirHOnBkos712KXW-1-W3qiA6r8q2_BB_o-2odrqZHXvIcIE5DNtk7qpnSNzuv2BW4vB1tN5kEUKmb3EOC7B76xka87SpOV5b--5NOQlLaYGtfc5LnH6SXq2c-X0WtWbDDHHbkg4qv2ysNAqagDV1JvYN62i7VWQ_omOePXqU7uwXp4MX8EMZuU5t9K61AbBphj3J6wwgZ0VZQN8qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/069f15d0bb.mp4?token=Ska2EqK5tWie-3eSgkGj6gXusKIgFg3zNdig7J4HaXS2tu10XG-IEBC-YSUDylrRaKbwnKTFXIR7fhc_dKcJKeXsANPDqqNZWEm8VNUO6f1tPGnqIJqsKO3EP3AZW61r5hkeSirHOnBkos712KXW-1-W3qiA6r8q2_BB_o-2odrqZHXvIcIE5DNtk7qpnSNzuv2BW4vB1tN5kEUKmb3EOC7B76xka87SpOV5b--5NOQlLaYGtfc5LnH6SXq2c-X0WtWbDDHHbkg4qv2ysNAqagDV1JvYN62i7VWQ_omOePXqU7uwXp4MX8EMZuU5t9K61AbBphj3J6wwgZ0VZQN8qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عاشقانه‌ای از جنس فلز و سیلیکون؛ اولین ازدواج ربات‌ها در دبی!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/678095" target="_blank">📅 17:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678093">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7hecKzL5HZyJblfWMFNcjCKeqEuQvQCRgUXh2zb4lYClIvR0QPbPfdWCR1zbN2VBvOcp9xJnNXVgbfPE3HEyPndYktZhcAaSRicIgiPa65Nl6Pgj2zQNHrfQay3WSgUp5vNVRr6FgeFiweoDmNMqKUzw1_kS40MUeoLgXhnOc9kOia-TsFSBBnh_TECaGgA3sQGAif21vjR2IMfbch2bg2hv9XqRvr1zb5zeAUMXf8M1or7abBxlJ4LSmhcl_uKETGXS2W7SRo0iv21HPGhJbWTN1JqpXaMydiSxHA5yy_LwqrIJXi5tFpjgEIyeh1EqZHP3Jg5KXoPKR9YF855VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لیست هزینه‌های ساختمان که هر مالک و مستاجری باید بدانند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/678093" target="_blank">📅 17:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-678092">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
تیزر قسمت بیستم از فصل پنجم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ آقای علی لعل یوسف که با خوردن یک آبمیوه مسموم، روح از جسم ایشان جدا شده و توسط یک دست قدرتمند آمیخته با خشم و مهربانی به سمت بالا می‌رود و در آنجا آیه‌های قرآن را به تکرار شنیده و اینکه مهم‌ترین اصل آفرینش افراد در همه ادیان الهی، انسان بودن و زندگی انسانی قابل قبول درگاه خداوند است را درک کرده و بخاطر کارهای نیک و بد دنیوی‌اش پاسخگو میشود را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: علی لعل یوسف
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/678092" target="_blank">📅 17:24 · 12 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
