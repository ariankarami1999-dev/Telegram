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
<img src="https://cdn4.telesco.pe/file/q9EIGojXLT9w_yuw8Z0tEd2Be5zZ-5HPVIRK3qw0QwN5E-3Gc2k_9SjktQQQa1ZaJGoHe5iHzMeyMuv_f9IcNCLdwaiRTH-7Mnk5gpQXIjsDvw9965zEqlv_VRKUyhp_YBwP-FfeFOi6xSo-TSMSl7W0vCpFPPGHHTq4A38jwL7q7w0zEGuNvKm9uN-jlbiK3dUtYhi-u9MN82zNJZ5T3xIYp6N-goh8Rd9YgCysC8z4PkpmfCF9rnmUUP9mEx1H1JKYdmoc7ySIUKhn9Z4rG1sgPSnDXN2yNytohB7jFFNivM0NGgZIKJhhEjh58T30pT3N6UWLTSkSOxk1q0rnKg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 475K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-29 23:31:04</div>
<hr>

<div class="tg-post" id="msg-30153">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dy72Z8jXsstZEgt90oZva5vQptdzOq7vaw7K-X0WdpyZ2o2-k0i-atDo1fF26b_nb0L4kZiuDyZyCLqeYvCh8lz41TBiN40Inx4lzO8EFJJNEv7TqRzNMcRHaddVgKGhEbPrWWI1WAQuhkMnYza1vgxIA3PkJ5fKf_stSgS1awPz18BY6acj56JPpPhJq3cgK9gysbXg4rAgyPilk-g_f3biQo-WObgIJVWgIFWvEvborVmObHVdMLorLdAU8_LQAIwWHP_J25vzz1WojROr6mUvS0Xan2_ISPAfk_vfo6wVcC0Hj4poCt0nEyc3LnvP4_enVcCFDNa32QNIuUpmlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
مصاحبه‌‌شدیدالحن خوزه مورینیو علیه داور بازی امروز مقابل اتلتیکو مادرید که از نگاه سرمربی پرتغالی رئال‌مادریدعامل‌اصلی شکست تیمش بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/persiana_Soccer/30153" target="_blank">📅 23:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30152">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDSerppMspNOY7WG-pzTicwqc33PpyLPeM7lpueKmgqcFe2wHs2BrmjOs7HYDhL-6iLy2ToCoAIzBeSHXFDD03WjHvpUAubPVbw3pr7sQKrGICWlQy21P1DqAMQlwjW1rVjAuVrY9weS7zzbZ8HGKlo7FcNlf2XtyRd2yC8EMjOsLkEFsbo0iz2xVTFuOMTMrRW7wAkDQpwXMdW2z-kfOr_fhegSsPdG2j720ei6DRCAo7dY93CEMAeqcFo1cBI0TKQailZYLLVWdrgD7PbGtcStowI3rzUn290AexHBIwmPw0PI2xMIoScpaoupuFwgUa0wEkfgOwiX5-15g3JEKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
به بهانه آغاز فصل جدید رقابتهای لیگ نخبگان آسیا
؛ نگاهی‌بندازیم‌به‌تموم‌قهرمانان و نایب قهرمانان باشگاه های ایرانی در رقابتهای لیگ قهرمانان آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/30152" target="_blank">📅 23:05 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30151">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇮🇷
👤
طبق‌شنیده‌های رسانه پرشیانا؛ کادر فنی تیم ملی با اللهیار صیادمنش برای حضور در جمع شاگردان امیرقلعه‌نویی برای مسابقات جام ملت‌های آسیا تماس گرفته و این ستاره 24 ساله که عملکرد درخشانی در اروپا داشته احتمالا به تیم ملی دعوت خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/persiana_Soccer/30151" target="_blank">📅 22:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30150">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rXsMMot-DGehqk3Brdn6aL4ZycrUwc3qDstxswVkfvS1HZ52WItGr_1H8MQkdKWDO3aW0Mgo6gm7g2_fuFyS6O_Z2ydTTv3oO6iL1Ihd2ezsLZESHFDBvj2kXGHk8pDDVI0NAEeY08i0pMNpjVKaH2Iis71D4SOXyt9dtjAsMI-ed4R8DjgwSVs2-OgnA7PMcHqxL7VrP9p9_3f9lBRzSswpXBqiTF93UKuD0kdhXXfdEpmDAHXx2GwI2_oL1wJB7lilKrUKPBQJQT_STaLYiG2ZBzS_efd6BXSXeBW4h-JeMjNq-GFgSCrnsI-OpB95HC2LtbcvzvIyFztVFH3IRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
خبرنگار رسمی باشگاه فنرباغچه: بزرگ‌ ترین آرزویم این‌است که کریس رونالدو قبل از خداحافظی از دنیای فوتبال یک فصل برای فنرباغچه بازی کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/persiana_Soccer/30150" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30149">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCxaZk4rwQsCqCLrF_ZseuHuschmXggGi50IEC2o8ZmtrhvRhrcOn9aakvmk61PpjOWaVgPme51vy0Wl6WrQYhsDfBlIDELu2jB4HTUBY-52Sr3Y7mH_aBL0sE5ksdskIUFr0CPQ-pFmr2b4goCL0qPUODxch1-ZyyFjVSONQUma8uPkBulfYENcprF-gJ__0AStRDOQ_0LPvWUDr9DUSmSqKWoXCBvhJbasGVbLZFlcEpZx93beY8VG94UDxmf5fW-DiZtTC1mFWNnFgYcxWaFir9uWBGhtYose7rTvrzwoxKGsvREVPHHAkhAqfXb75c6-FQvGLn6uiR3CC4mIOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فده وارده کاپیتان‌رئال‌مادرید به دلیل مصدومیت 3 هفته دور از میادین خواهدبود و احتمال داره دیدار الکلاسیکو که سه آبان برگزار میشه از دست بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/30149" target="_blank">📅 21:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30147">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">⚽️
⚪️
شبکه رسمی رئال مادرید به شدت از عملکرد داوری دیدار امشب با اتلتیکو مادرید شاکیه و گفته سران‌باشگاه دارن برسی میکنن که لیگ کنار بکشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/persiana_Soccer/30147" target="_blank">📅 21:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30146">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CgVSI9iV2ehoyJYrni7PTDjICY4Ghc7Rp0tElBhavYvGsO1sYXRBs1uMg0Ozs-IfCpK02T-l34oVe90twkDal8OGnpVr1gd9i2xZzJcFcwXacp2qR3Pagb2BvM_jWvq7jlUqjUVE1GIV3R5N2nO-4USMq9AJ2LI-xdiJBtxqbefvigPPCafZOyTjIdoWL-YANWUBUy0TytxenfxIpVTdOcezfaxO8cnJokez2P_DGWLh5Qlc3AL4E0_gTEZCNg7FUMj7htNeY0V5ItOELlWMaNUNK5E3hvVSkeN1zlfc5J7u2HPfNk2Rb8rYFiA5o3HgLG1xULtOKVDSG82iYqJn0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
آندریاس کریستنسن مدافع‌میانی‌بارسا به دلیل مصدومیت دربازی‌شب‌گذشته مقابل سویا، شش هفته دور از میادین‌خواهدبود و به احتمال فردا دیدار سوم آبان مقابل رئال مادرید رو از دست میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/30146" target="_blank">📅 21:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30145">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/584eeae99a.mp4?token=aaAn6iO77BmfaVKChCQW8anXQ7zSeeyeBBei995o4NqiDsf_LYIJ2rBGebefiVG0iSuTBxr1loZAoSGXmiewufFU0j0OPvI4yUUuR-sOlM3nVWEYTzdzUxqYgp_IA_sU_3sa9nxRwG3yDc8oBhZGzWBsMT2DSdMZ3dhXs0gvJBurNC4UpYfYDSXf_BSY-MAYXwr-nbB82sF9VEfWdiDbMYx1MwAFjEo41cJ3SGhFdPppoJK33l53pXkfE5nZxA8Ovlg2lhyYimBE0XVXxRk4F_n4nzHJquOdNcdbr-05xVTgbITRzECcSdrmITsxg0QPsIfSQoB24bJczHtb8vWnfHe2PZY7nj4cMsmhTSD7Gmcpq88Prf9MUGUC2aX_PvMLdxEVJG08EXcOeReWMYqAy6PCuBn4vXy3Vww6VqRy5SAGeho8VdG8meNbVsuENL5wfV9zQIxiGknKN5_4eAPGXrD9EdwQsPQ1aOC5C8P47SrO0szvl7Fh0_DkdSAtFoLisSeG6SIDJSyH2HnRvQobp8zIffyYvVSz8JPVlzC4GJ5vfOV2i-oUQ-pYEyhWvbWhXB3Jbos81zQ_9sxF3rDNYFPMkCLUFiyJtB4i6kivneP7XwPH0eBKoSI364rDZRI1cRGtHtoRY939bMvZAsVFZmNeYh9Yy8_8BOVrQN7nJAU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/584eeae99a.mp4?token=aaAn6iO77BmfaVKChCQW8anXQ7zSeeyeBBei995o4NqiDsf_LYIJ2rBGebefiVG0iSuTBxr1loZAoSGXmiewufFU0j0OPvI4yUUuR-sOlM3nVWEYTzdzUxqYgp_IA_sU_3sa9nxRwG3yDc8oBhZGzWBsMT2DSdMZ3dhXs0gvJBurNC4UpYfYDSXf_BSY-MAYXwr-nbB82sF9VEfWdiDbMYx1MwAFjEo41cJ3SGhFdPppoJK33l53pXkfE5nZxA8Ovlg2lhyYimBE0XVXxRk4F_n4nzHJquOdNcdbr-05xVTgbITRzECcSdrmITsxg0QPsIfSQoB24bJczHtb8vWnfHe2PZY7nj4cMsmhTSD7Gmcpq88Prf9MUGUC2aX_PvMLdxEVJG08EXcOeReWMYqAy6PCuBn4vXy3Vww6VqRy5SAGeho8VdG8meNbVsuENL5wfV9zQIxiGknKN5_4eAPGXrD9EdwQsPQ1aOC5C8P47SrO0szvl7Fh0_DkdSAtFoLisSeG6SIDJSyH2HnRvQobp8zIffyYvVSz8JPVlzC4GJ5vfOV2i-oUQ-pYEyhWvbWhXB3Jbos81zQ_9sxF3rDNYFPMkCLUFiyJtB4i6kivneP7XwPH0eBKoSI364rDZRI1cRGtHtoRY939bMvZAsVFZmNeYh9Yy8_8BOVrQN7nJAU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نامزدجایزه‌پوشکاش سال؛ ضربه قیچی برگردان فوق‌‌العاده و تماشایی‌از میگل بورخا، مهاجم تیم کلاب آمریکا مقابل تیم گوادالاخارا؛ چی زد!!!! حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/30145" target="_blank">📅 20:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30144">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b82b6c09bf.mp4?token=n5-dbit72MmO1skr41V33iIXJIxzPapCEZ_FECQryy-KL-EOKeNRjkorlvaouP3v-1G-orOWws4CqATLU46SNN259Z4-T8yq9YC9zHpMaEzaYEq8WX5qGj8_9-kcJj6ATn-vIgmfzLUechnjTElKRFmjKH6tExl3dj2PkYq5IhrfXxOD4_E9DCO_DJD1zq8SlfGZ7UGJrKgI3KAldh1LzeogQxv7PrxcawFGfzqK7fFyn7yWLMdjSl1IWYJhLYIXfhKWgoKv-RuUOaWnBkBdAcqdnWDKlZE481KBo4G11e5e4m0V7qnRAmUW9xTGvQtzNCbokr_HuyFem1n6MrkA_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b82b6c09bf.mp4?token=n5-dbit72MmO1skr41V33iIXJIxzPapCEZ_FECQryy-KL-EOKeNRjkorlvaouP3v-1G-orOWws4CqATLU46SNN259Z4-T8yq9YC9zHpMaEzaYEq8WX5qGj8_9-kcJj6ATn-vIgmfzLUechnjTElKRFmjKH6tExl3dj2PkYq5IhrfXxOD4_E9DCO_DJD1zq8SlfGZ7UGJrKgI3KAldh1LzeogQxv7PrxcawFGfzqK7fFyn7yWLMdjSl1IWYJhLYIXfhKWgoKv-RuUOaWnBkBdAcqdnWDKlZE481KBo4G11e5e4m0V7qnRAmUW9xTGvQtzNCbokr_HuyFem1n6MrkA_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نامزدجایزه‌پوشکاش سال؛
ضربه قیچی برگردان فوق‌‌العاده و تماشایی‌از میگل بورخا، مهاجم تیم کلاب آمریکا مقابل تیم گوادالاخارا؛ چی زد!!!! حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/30144" target="_blank">📅 20:13 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30143">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2be5ebfb1.mp4?token=dgREOh5aCVjdPbfsWkuL8Ag-0f1K401KVU7cD6gjZhjasBIxvzm_c9WFO_Y8enc36-v2w9DNdoIQLQQVK8DGKUfbpowjeGPFC1WRU7d-mQXkYQFpWqK75hABreyx_ZobJI6UgrwiK5V36KjAKhjlrzJ6MdVxJL6Mhb8vYLGPfSwKVVI9KTEu03IYeYkLEs8EogIE6JLf7cqdFBhiTpvLooCbjDZEz_maSvd8YKlkvPRt4vtpEmy-5A31uf7EnvKbWI3eZ9i-F-CLkgvNeJhEJ63zZJUvtqMpM-ccpcm4PbzrANXlpd31d2SZBwPD8iETpxwQA6MS8c6TOdL7v9WIpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2be5ebfb1.mp4?token=dgREOh5aCVjdPbfsWkuL8Ag-0f1K401KVU7cD6gjZhjasBIxvzm_c9WFO_Y8enc36-v2w9DNdoIQLQQVK8DGKUfbpowjeGPFC1WRU7d-mQXkYQFpWqK75hABreyx_ZobJI6UgrwiK5V36KjAKhjlrzJ6MdVxJL6Mhb8vYLGPfSwKVVI9KTEu03IYeYkLEs8EogIE6JLf7cqdFBhiTpvLooCbjDZEz_maSvd8YKlkvPRt4vtpEmy-5A31uf7EnvKbWI3eZ9i-F-CLkgvNeJhEJ63zZJUvtqMpM-ccpcm4PbzrANXlpd31d2SZBwPD8iETpxwQA6MS8c6TOdL7v9WIpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته هفتم لالیگا|دومین شکست فصل شاگردان آقای خاص این‌بارمقابل اتلتیکو مادرید؛ اختلاف رئال مادرید باصدرجدول به شش‌امتیاز رسید. بارسا مدل هانسی فلیک قهرمان زود هنگام این فصل؟!
🔴
اتلتیکو مادرید
2️⃣
-
1️⃣
رئال مادرید
⚪️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/30143" target="_blank">📅 20:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30142">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-S_H5Fv1CvXDfgfIk8neEVyx0XFq0JAcLYjU_eURVko4uxpi3ISxddS9fQ2RNpe3ZEcJm4hQm76PeOlGNf7YxEH5iyac1tcW6-w-1kw8RAD_kynJemqjIlgKIOh7acgr3eXM20pww5MU5u6r3O9K8_94B4_P0x9JxSzwm7NqPaUDGJrRutyqpHgIGJhKZCIMyWxnlLdxzX7Ra6RvdOQrX94_LT1p6HmQKn8VC7Vgqtdk_NbJrlhBNx5BgAAXjUgRCz3ea-rTG5f_TrXxQOYa6UHp8tSQnbU47nl4t9oly4aiS2m5MfIIriAbExgan7zLMDGMlCkqPOm1g4Vleiq1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته هفتم لالیگا|دومین شکست فصل شاگردان آقای خاص این‌بارمقابل اتلتیکو مادرید؛ اختلاف رئال مادرید باصدرجدول به شش‌امتیاز رسید. بارسا مدل هانسی فلیک قهرمان زود هنگام این فصل؟!
🔴
اتلتیکو مادرید
2️⃣
-
1️⃣
رئال مادرید
⚪️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/30142" target="_blank">📅 19:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30141">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zra0COy4NtdjDjemUCRDPOE-ppKOTYz3Wq7IpIWXubzasN-ZgET7AwGBeaJxTijDZTqGtT2L2LxpGeYqUE8pPePDMlPbxgSF3gaM4wRNS0kGuEy-NiuNx6dTscKj3akcKXalWgW4VPXco9fKkGCS8jcN21NSPrKm1VEIrWMyKnPOeOR_ZXwx_EGDn7fGimwbOahG1tRz7XrP_Wjr7NO2pF9uwuTrYOvxgj9G6TJrkFKxsOkz4gnBaBXN97Qec9N95MjpqPMnDvnM5TQi7Npit_ekc67dCiMb1nmF0kriewbrEmrZFhQa3nwE37-pN-X2CvhYdQC7Gi9VnBtPy0Y98g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هفتم‌لالیگا|شماتیک ترکیب دوتیم رئال مادرید
🆚
اتلتیکو؛ ساعت 17:45 از پرشیانا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/30141" target="_blank">📅 19:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30140">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iNy3v7K1ulfSnn6HguAylNX7AAg-Q_x8xr7ge0bWWI_t0VIab1OHmcCY29VNvSgSMqERi9spv4EaoSq8mtcOZzXmMSKrDZ3v_USBLpUk3VMykjhhxGleMzn0Ruiz2_qDwLsAFOldqeh2ArfvsJzQyrgHoBq_HfqWuclAz1JnnsLcMRVvO8kJD8fWhUtBL4-EN6a2mjfeAvKJk7i8NuErRZDoi0NcG_XKuWNOO9B92_Hluoe6w59NB40UKrJNAVLCx1_9A4MMk9tdjp9DHQTylB1jwrGLCyHZqZLyC5wMz9L_sYV4jLovga9tqe-gfuOE1vjdNLVW3tJVNbF8-jK6bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه کاشیوا ریسول درروزهای اخیر پیشنهادی دو ساله به ارزش 4.5 میلیون دلار به یاسر آسانی ستاره‌آلبانیایی‌استقلال داده بود که این بازیکن بعد از مشورت با مدیر برنامه‌ های خود این آفر رو رد کرده و آمادگی کامل خود را برای تمدید قراردادش با باشگاه استقلال…</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/30140" target="_blank">📅 19:45 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30139">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43f4a8d8c8.mp4?token=FdIBpmKpy349MaHsrinWv-xnWJ7su5ZKfhgT-oFHe9t0ZRDSoXvJvuiWqYLkRuk5eGur6Ge1yyV3wNyWFSM3opw625O0xtB3keK2jNfXm7kp1uyJCiPgZ_Bm-714acKUuza2VTxKVh0iU9G5Tf69b5F1exqsWXPfF2I8l4P6qRFpE0TCybilryqMx86ywszzQykvNstBtFoz1zWFnwJOMjkWmy-Qyv7J0RSgdqcMkwkFIGjJcnQYQzxpfpFkRlMlI420f5Xdj-RsN9XxV11i6dq0LromYzvap4yF_Boyv-qOfDuYArARDpQgwbdyIr57uf7hczqvP3r43eqjJfUd2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43f4a8d8c8.mp4?token=FdIBpmKpy349MaHsrinWv-xnWJ7su5ZKfhgT-oFHe9t0ZRDSoXvJvuiWqYLkRuk5eGur6Ge1yyV3wNyWFSM3opw625O0xtB3keK2jNfXm7kp1uyJCiPgZ_Bm-714acKUuza2VTxKVh0iU9G5Tf69b5F1exqsWXPfF2I8l4P6qRFpE0TCybilryqMx86ywszzQykvNstBtFoz1zWFnwJOMjkWmy-Qyv7J0RSgdqcMkwkFIGjJcnQYQzxpfpFkRlMlI420f5Xdj-RsN9XxV11i6dq0LromYzvap4yF_Boyv-qOfDuYArARDpQgwbdyIr57uf7hczqvP3r43eqjJfUd2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خاطرات سمی امیرحسین قیاسی از مصاحبه با علیرضابیرانوند و جواد خیابانی؛ بدترین مصاحبه کل عمرم رو با علیرضا بیرانوند گلر تیم ملی داشتم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/30139" target="_blank">📅 19:45 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30138">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g0ooSGJjLS3-T4OS58ugk92q6YxTo55YBVNb8vXy8PAsLREg5AYx57hhjHYzg1ZkPsgPwSN7xlkau1ngCA7EDxZY9tWI_XEnti4-QHQGOHxJ9z_-HaYBiHq91DPdXKJRa5tekVV7qyNfdLw7Q1JFtDJM66l78ETc59CpKdkWuuQlSHqU7oALBdgsasdoi5lRZT50s8QF4DcgHMOzew0V9UM2yFDlaNEr81gqs3vEzIlH9pSSz9pEZIbP26_SWMv0Bb_9gJvX8iU6p1o9ZkZRNun2YW6mPB-l7cByRr8dDCm4x2rVH77mkXCFqSffXoSMtWvKOugkQO6z1WNdmC7cPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی Yekbet
💎
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🔔
فرصت ویژه اولین واریز دلاری در یک بت
⭐️
یک واریز
🤩
دو جایزه
🎁
⚠️
یک انتخاب هوشمند، دو هدیه ویژه
تجربه متفاوت با اولین شارژ دلار
ی
🤩
🤩
🤩
فری‌بت ورزشی +
🤩
🤩
فری‌اسپین کازینو
👀
با اولین شارژ حساب از طریق ارز دیجیتال، یوتوپیا ووچر یا پرمیوم ووچر، هر دو جایزه رو دریافت کن
🗓
شرایط استفاده
🤩
⭐️
فری‌بت:شرط میکس حداقل ۲ مسابقه با ضریب حداقل ۱.۸۰ برای هر انتخاب
⭐️
فری‌اسپین:قابل استفاده در بازی Yummy از POPOK
﻿
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
g29
🔗
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/30138" target="_blank">📅 19:45 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30137">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZC4PPQ0295O54dfLKXe8QUya00uPgJRw3K69lXiw9Ohh6r5-29_EgLK2W2rLR7AFofj-RCgNk5qyzQg4_abZbYCrRFXXokZngyCWejKbuVHdcr3lploqDTWHbgEljnsSReIFYD4lPj0F2-qXnew9Q6XSAlVnyAvm6Ya4fIHCrYhiD-d4QXqtij9CrEEUg7k9jn0P2341hrWiXaoSsXAOEhkb6_3RWHTkdZ3dJPkksDp_3VRrOy3ifvN4NAiLfFbA_Yph_TeW5fIOiewELHSo1cHyk-FRey9DR19cxWh5GiqJNben-W5-FrD8DnvBfvnHacFJMioU_O61KMQD1dwag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هفتم‌لالیگا|پیروزی شیرین شاگردان هانسی فلیک درشب درخشش خیره‌کننده غایب بزرگ لیست توپ طلا؛ رافینیا دیاز یه تنه با هتریک‌اش سه امتیاز مهم بازی رو برای آبی اناری‌ها به ارمغان آورد؛ هفت مسابقه، 21 امتیاز، 31 گل زده در لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/30137" target="_blank">📅 19:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30136">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dpz0r5bcsyom9ZOMGCs3BSxIG1AmXmiA6SY5NhAXVDvxiyiKN6pBg-ZLR-9KR4-i8SnAZslxdGkmUHRHZ2lvVbucPZuMqbqhoXjcKNALX9jWqI-39aTg3BKJOMX0W0_lDQjKiCfqQpQyhWrz8z_Y-OSy1x0LGCCKr1_4ZUgDwfgg7YtA22--n5MIQ1xWz30NkFQDf-A1iPwmbHjhXj9BZCtDEigaSJkqggc-HuVQFBr-vPaw9gPxpf0ctGnul8q5chvfRscUqLMKm80VPdXvhuszB-n0i4V8GjHWVcOIMpZyPZzV7eNsHwAWJlcQwK1VhOO2wDZ4DJeKcKoC5JDvCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق پیگیری‌ های رسانه پرشیانا از نزدیکان اوستون اورونوف؛ برخلاف ادعای رسانه‌ های ازبکی باشگاه تراکتور تبریز هیچ گونه مذاکره‌ای با اوستون اورونوف ستاره‌ازبکستانی‌سرخپوشان نداشته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/30136" target="_blank">📅 19:21 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30134">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eb0177e91.mp4?token=KMr99YRnzIQNK3SEJufzPrO1g0doniPd-Az12xQjqa-f8ghDSAysqHq3l1jLnB_xNLmrbzOpdSIniEu-fnkQjctu-dBwYCjz2I8QI-wGdn4cwdZb9nKJX3J43hIyu0sePiRsAAUT6gL2Rjb9Q7G-wH6UUZkaNWl9q4HiD31FP6oQNfSvWbFeRHcC0Pb56CwSlGhvadD_OEiEMcOzuuy8P7xUNut1SZe6Ehvre6N1w0ePkhCzLKthvIf6pVe53387gO80Jko6AOkZ3Y17lB8RMcICf34hlehTMGam39K8QZw8wtei2c2ePtw-prpjlGDc-pn76uQ87NXlUQ3JR7krNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eb0177e91.mp4?token=KMr99YRnzIQNK3SEJufzPrO1g0doniPd-Az12xQjqa-f8ghDSAysqHq3l1jLnB_xNLmrbzOpdSIniEu-fnkQjctu-dBwYCjz2I8QI-wGdn4cwdZb9nKJX3J43hIyu0sePiRsAAUT6gL2Rjb9Q7G-wH6UUZkaNWl9q4HiD31FP6oQNfSvWbFeRHcC0Pb56CwSlGhvadD_OEiEMcOzuuy8P7xUNut1SZe6Ehvre6N1w0ePkhCzLKthvIf6pVe53387gO80Jko6AOkZ3Y17lB8RMcICf34hlehTMGam39K8QZw8wtei2c2ePtw-prpjlGDc-pn76uQ87NXlUQ3JR7krNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌پنجم‌لیگ‌جزیره؛
پیروزی خفیف لک لک‌ ها در دیداری خارج از خانه و آتش بازی تماشایی سیتیزن ها در اتحاد با درخشش انزو فرناندز. گل‌های این دو مسابقه رو حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/30134" target="_blank">📅 18:42 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30133">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PrzQfaRsTwnuhdBQdjRL1ERDb3CpznYv7OYg4fg1zGoVcg8Ba3xalqak81uXBJ-yIxGsMLVIOWGOjqm24T-TKfNpiEp3kT-b0c3UXLgDqQuXoGkvZwa2_RCQ_iDno72bIRMWSX1Ot9QEd96whnga5-20N3QSCZbzSIl-IekASS5bLJgjuQWTC4HF-cc5qjlZrb5z7alDWMNUrf5KdT9jHaYEA-37E9ayAHyCifPEfDBURy6PYntwFoBTB7wXCKxU3Xp4lNr-L-svFUl8nVZd-5j_rBfN1bvEWSL5tJGV-7ABk60-dpjK7MaH5IhPjoLWuv5tIDdy9X8Iub2LCKUwPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رفتاریکه‌مایکل‌اولیسه بااونیکی خبرنگاره داشت این بنده خدا هم ترسید اولیسه اومد تو میسکدزون ازش پرسید گفت اجازه میدی که بغلت کنم؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/30133" target="_blank">📅 18:10 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30132">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NYVjqW_y987KNRNe8QEweUXta6vM_Qr3svpAs4rs4HQrVGXcJ8UUEpjO31qYE7qn8_SSa7bI5m5up-eUxQBmCcpYCxbhihXnL7_1QSd72Labp0Jtfxj4L1SVxNDBtY1ZoQPc9mL9ybKD72mVoAkoZH-PLsNlyRpYBRnXwGg9vECR2I0JkchB9hA9HCz8U58lwWM-TX2o9VDmhAcCspCJmWmtAswGMXmqx0Zv6jDlegjLA6DVnpkJ8ElJuUq4y7PHxO3FYMbmv8tqlm9JETNp88oStXFosZ6j3Pzs3sqKNorcQZwmga4UspKWZplEVL-PKgxRky7egxRTba527w21jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
پارتنر لامین‌یامال:همه‌شواهدنشان میدهد که یامال شایسته‌ترین‌بازیکن‌برای گرفتن توپ طلا 2026 هست. اگه عدالت برقرار باشد یامال برنده توپ طلا خواهد شد او اسپانیا رو قهرمان جام جهانی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/30132" target="_blank">📅 17:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30130">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d3be7a360.mp4?token=sqVyndeAzHHrMV9woT2k4ixA_5jkOx-N0_VmBA2q-bQssqWPhdTMpEH0qCSEMfqHgzGelgRZFoGNdZMH7jMccTL7cfeh7hTogIpe33T-sjYYStIc-nC4iq_jCxkq_jJ8hWgo3N-6jh7ym61q7qyTxHG3Hgio0Yh0F_WCEFgxIy26NMbtvVnN3lPnIwd0O8pjuE7_L291o2N9F8BVXnkz1SSzfJfbYX_taaIMVYBnqJj3fW9ta7P4UijCjZQYw0OjYqDl_7U-lSsfbmiS55SoXRsH39ULPlxJzdl8P1_dRIfOyHS8IbNSn-9eb_v3j4-IWQo5fbx2FiVyVK7FRcvvrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d3be7a360.mp4?token=sqVyndeAzHHrMV9woT2k4ixA_5jkOx-N0_VmBA2q-bQssqWPhdTMpEH0qCSEMfqHgzGelgRZFoGNdZMH7jMccTL7cfeh7hTogIpe33T-sjYYStIc-nC4iq_jCxkq_jJ8hWgo3N-6jh7ym61q7qyTxHG3Hgio0Yh0F_WCEFgxIy26NMbtvVnN3lPnIwd0O8pjuE7_L291o2N9F8BVXnkz1SSzfJfbYX_taaIMVYBnqJj3fW9ta7P4UijCjZQYw0OjYqDl_7U-lSsfbmiS55SoXRsH39ULPlxJzdl8P1_dRIfOyHS8IbNSn-9eb_v3j4-IWQo5fbx2FiVyVK7FRcvvrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی‌کنیم‌ از مصاحبه‌ تاریخی‌وفوق‌العاده گزارش گر صداوسیما با یه‌کشاورز؛ خیلی خوبه حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/30130" target="_blank">📅 17:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30129">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37c2e1f8d1.mp4?token=YiQd4ABpkhZZpWbGWw3zgGCU5vzARSSI6mJA9IbDp-c2tVJHKyM_li8-qP5h9AMMjdGEqMgqrjBX1NhqvYvm_wlUveCmmKpZgs4O3nHUWb8HiZjqlGdmrz0s9USGrdxhJgEK1sMlpg9GJXNsrRt_qNU9afAfTojZSBORVNN541U7agWOcGujIs__3RFxBpAeL8IxCPec5nHJLVBpYiA9tbj57-ItXEH5YDPAWYsjnF3bL-ZQqhvE549Fd98I3q642T0Y8gNMMkOyOX8EdPXv8AuNQXEnBGtBLG3SiL6VyjCWDYSZ3OPqoWwPlx6bamRBgZFmgSUKnhSSNHzy-3-n_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37c2e1f8d1.mp4?token=YiQd4ABpkhZZpWbGWw3zgGCU5vzARSSI6mJA9IbDp-c2tVJHKyM_li8-qP5h9AMMjdGEqMgqrjBX1NhqvYvm_wlUveCmmKpZgs4O3nHUWb8HiZjqlGdmrz0s9USGrdxhJgEK1sMlpg9GJXNsrRt_qNU9afAfTojZSBORVNN541U7agWOcGujIs__3RFxBpAeL8IxCPec5nHJLVBpYiA9tbj57-ItXEH5YDPAWYsjnF3bL-ZQqhvE549Fd98I3q642T0Y8gNMMkOyOX8EdPXv8AuNQXEnBGtBLG3SiL6VyjCWDYSZ3OPqoWwPlx6bamRBgZFmgSUKnhSSNHzy-3-n_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توصیه مهم مهدوی‌کیا اسطوره فوتبال ایران به والدین درباره زبان‌انگلیسی؛ حسرتی که مسیم دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/30129" target="_blank">📅 16:53 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30127">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m8xV_2g2kV19NZOBk3Y9w-qXpajAx4o9W4dW4gb1i7qnb2gxO_KqKzOB4pTdAIvtCIlv6TJFpHGcOWnw714r8dEWU8JeoNqF8xXIPeG-Mp1WcVfKvDLlcXUkn9mA5IfHZq0r9zLBYwW7_2Ef2JSYSE6z1alo4zYGfxIGETMG8bL9ybR2JHNBjYg_whQe2w990gm43OFZdZmh80m7EwqwVpXX3fMcZM5Q2k472xNdw0eEwDlhF4AW51wIQjqAUH0Ops35NUpW6vR8NxxtRZnXZwF_h30jFDJKAQUEWeegSv4BDZTZjI4wrW2glAUS5pLGeo1zBBm_jPRo-RXAQjKRIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NsIBT9s6pfIZE17JGfyKMN8RpI8XkBDYiLT0yGEAZ2FlMnD2DMUslSQOQPfA2knMVw2eKp1dqm9KDaNvrIL3SIOk44NWySiD4GNMsy0xCwoDu2XTQxMdCrDmzSqfUMIBZEhu7ct5fv4p-N0ee9NYpFk8TAa9MBHf9gZQX_H4vW_b2wntcXw2QM2RIt0lOOe-4A5mZUya8ThodStPJe18LKflDcfaKp9lGXR3qt2csA1AD1R_GLxJ-1v2W7-uvh_Ui1BdK-MQXW3sCj7D0oydmpLjTHTlNnKGAAJ9kw_IdCaFUCXNC8c8H7dojdRdQ_hgcGp8R-SneaDFqeBou2srTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
آمار تقابل‌های لالیگایی اتلتیکو
🆚
رئال‌مادرید؛ کریستیانو رونالدو بهترین‌گلزن دربی؛ 22 گل؛ اتلتیکو در 10 دربی‌اخیر خانگی تنها 1 شکست داشته؛ 5 برد و 4 تساوی. مورینیو دربرابراتلتیکو:11 بازی و هشت پیروزی. سیمئونه در برابر رئال: 50 بازی و 14 برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/30127" target="_blank">📅 16:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30126">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6_FpapALdvVM4ghWOtmwK_gSLqZbnB59WWHcVQXly7Tbp8w9KflokRN29nKRHmNpchLw3-PXrGSiQ6OpExTMP-1GVUUC0IcIcm9QGjchdR5bB4us3zleI4ytoNIXYrrysphyMixpjd2g843g5OTDUsqxiPUlQ66DeKo-eyAFx9pvmHll1VGzgV4vXY4099vTrz_vQ9FOYM43Bp-R1j2tTXqo0nn6djFf7IjRagpHPf9JvYuKoSMnmomYJLy3KIqQgszaZj-oGxDSxsWnfXi6Jt5nh1gfL8J9MSBxy4kQ-U6lU3sBLiezCS8FSRBrF0Fp2mapPUWXEPLAvNfx0Vbkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار تقابل‌های لالیگایی اتلتیکو
🆚
رئال‌مادرید؛ کریستیانو رونالدو بهترین‌گلزن دربی؛ 22 گل؛ اتلتیکو در 10 دربی‌اخیر خانگی تنها 1 شکست داشته؛ 5 برد و 4 تساوی. مورینیو دربرابراتلتیکو:11 بازی و هشت پیروزی. سیمئونه در برابر رئال: 50 بازی و 14 برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/30126" target="_blank">📅 16:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30125">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTJ5sBfvalcmj9_safd0IEP8ugMRNhZ-dSYHGncmJPUDzahD58_wjBNkFGa0nZ7Ib4RCHb-iL5-1v-60EOuXLXbP1WoxdLuOvDqPf59BS-JABDooaDc0UhcFD3X702dDjG1cWAY7dfI0U-1ps_dTcbhMzYk22_rkOcRxReYrlIYCDtTwOaXPFPT4FCl-1l20Ziw1RX_f71hrjqqnIIvVumXUVdg523tCIUHOMbkXy_JbLW6jO5k3QRE8xzPuE0GaY6Ki6LF1BtcSN00-TFNqiZW33Fey_-IetFerWRwzdcjcpdy-O--lZTjMtvwCQe5Xl4Q1UQnvPfguA_Oe12LYnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار تقابل‌های لالیگایی اتلتیکو
🆚
رئال‌مادرید؛
کریستیانو رونالدو بهترین‌گلزن دربی؛ 22 گل؛ اتلتیکو در 10 دربی‌اخیر خانگی تنها 1 شکست داشته؛ 5 برد و 4 تساوی. مورینیو دربرابراتلتیکو:11 بازی و هشت پیروزی. سیمئونه در برابر رئال: 50 بازی و 14 برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/30125" target="_blank">📅 16:06 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30124">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJhv3DXz2gZlndqaJgHhgUn4q4aSwduyjJeVnSnt0OEdASgzULKSluOatgMhQcTMGG4R9if8OtXnbCtGw5u0Qc-sgWPGAu4n6eZyTng6yuzimQl3kotKmThms1cF7SyYrrIJe7KcgmHDueS_5kUj8MgUzsPe1-InINFnNQ-fRTzLAqfIoLwzGSFDP3VmW9S6AHtwll-fcmfEGgY2XWaQWGT7kQwT2fLQaJ-aylMveRShse9aqNURZ5MDB8BhDnfR37a20-8Cupx8jNI0u44fNvB1Z8dfV_GGOdBvivUxsUqFsJCs42Mxa_rTlsjt9GP6wneSLUtCRXOQ5OaiPI-ZPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ مدیریت استقلال و شخص‌علی‌تاجرنیا رئیس هیات مدیره آبی ها بعداز انتخاب‌مدیرعامل جدید آبی‌ها با مدیربرنامه‌ های یاسر آسانی برای تمدید قرار داد سه ساله ستاره آبی‌ها جلسه برگزارخواهدکرد. درباره مدیرعاملی هم چه فرشید سمیعی انتخاب…</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/30124" target="_blank">📅 15:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30123">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ujye6Y_nLJ9y2wOAbKEXOnU9Z6410YWVdsC7cEAuVs9Pi5inr8FmkdVv1YFWkdryTPqhxYaHJTie-pvmwT4x2-uejOIwMxLIHr2r_-ayenbpdV9aysqAt0JKs5OzN3BvosB3QrQpoW3bjAO0J8w6XCTye94jfVnvdOmwVPGRWaRS3jfAEIr83XHTr_bEsYqiyytFvWi0rdZlyKA60TNcoFipecUvbuOMWYbqbUp8ZnqVLYzRIkkSRHpOFSkWbEYNbrqPjRpU5aH1aKyEHOwvo8pCJebRy3Y8n3yt5Al-le2m5ogz3o6TmRozuLNy1gn88FUk0GAa58ljKdVlC2SJ-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مقایسه عملکرد رابرت لواندوفسکی و هری کین در 150 مسابقه اول با پیراهن باشگاه بایرن مونیخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/30123" target="_blank">📅 14:53 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30122">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e09969a195.mp4?token=MluwmVJV3UjINIPVm5EWFBbcLHP1nX-pN4VAgLOf-JupQ9hz-MRNgQIqRKQuSizelLat6wWm_BMZjDG5Hw-6ztKHv2agCg6X2bao_v064xgeS8Ve6odwbGce6_syU3okRRMaI0vatqxbwRIgNxL1kHgOrTMghN7_i4uEYDhUeJvJYQwWIA-PZlrxEqcWrOO96ru8tGy7ph9Ej_gmS0pCGhEkBufXI8EQZqR_UWVqCopLZVi0PL5HJgvtxSeBLxWmR4QsQQZhNF9ysMspL6q-fPKLrRbkePT69eAsEijgUE3qV5Yz_6m4DWa3oEwcOs3d87SKNYONKg_nVBLYZ5S6oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e09969a195.mp4?token=MluwmVJV3UjINIPVm5EWFBbcLHP1nX-pN4VAgLOf-JupQ9hz-MRNgQIqRKQuSizelLat6wWm_BMZjDG5Hw-6ztKHv2agCg6X2bao_v064xgeS8Ve6odwbGce6_syU3okRRMaI0vatqxbwRIgNxL1kHgOrTMghN7_i4uEYDhUeJvJYQwWIA-PZlrxEqcWrOO96ru8tGy7ph9Ej_gmS0pCGhEkBufXI8EQZqR_UWVqCopLZVi0PL5HJgvtxSeBLxWmR4QsQQZhNF9ysMspL6q-fPKLrRbkePT69eAsEijgUE3qV5Yz_6m4DWa3oEwcOs3d87SKNYONKg_nVBLYZ5S6oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های‌جالب‌ و شنیدنی این نابغه هفت ساله اهل شهر تبریز: در آینده میخوام پروفسور بشوم‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/30122" target="_blank">📅 14:33 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30121">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJD06fYXFgazvIGMUfZBqXfB_uETzl5biV5nsgHZjgGoQ4imZ90qb6n_Tp7yH3GEgBQ6JDbKhnq0scJcpJ7TBlzAQ_o6DSxiTATXmUn6NZpTcBl7WTTb3SJ4BtxwiyuHgDQ4p-J84JKn1KFkXGSAezOAzbXacKJB5WyLi-XYdWf3CM-pIVTLTIu09lffWDkFQgp13JV_z6QWI5MZr62iB03y-RCxXtPTPzui5jucbmOEmM4mUFADi_qAtaqfXeRc6RQtbV2LYEdwFgvBPrY3fl_3WzQCUUBMfdCd1MOa27lpyxEj_k4RpaPdELsA5JKFbZr_iqhbxUUFUIseRWze4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق اخبار پرشیانا؛ به احتمال زیاد سعید دقیقی سرمربی‌جدید نساجی میشه‌. فرهاد مجیدی که مجوز فعالیتش درلیگ صادرشده دیشب ضمن تشکر از مالک نساجی به آفر این باشگاه پاسخ منفی داده است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/30121" target="_blank">📅 13:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30120">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXvtCab2ZVyz2hzkkujE7ClS98CTdotEo4kcd-59jH9WRmGIgvJczPpGZltRlnDn5ROiNxZcqYGYqWSYbRLVhoxekTiLwGPIaG1An4S3fAR7k2_Q0_F0Z2pNzmcZMQGZOS5UtV1GofDoJAlFUYIA1CxHhexFP1rDV9hSVOYtlZ9IJ3VEXjyG5ZegCCGezEyrUS-bu3ksFV0GWiu4JL7tQlztxjtcZb6NVMahO5TZEvesr_2IJoP8ncMF-hdZLL8xq9qTFDEs5EeV38OBUd16V9kNRjggLqwT8VV0LkOmRnsu9n_cGef7gKOCyZTU8wICYD4aUbG0CEz1hfNFXPMzeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فرشیداسماعیلی‌بازیکن‌سابق‌ آبی‌ها:
رفته بودیم اردوی کیش با چندتا ازبچه‌ها عکس گرفتیم بعد از ۳۰ ثانیه همون عکس بین فن پیجا پخش شد. از اینکه به این سرعت عکس پخش شده بود تعجب کرده بودیم. بعداً فهمیدیم که خودِ سید حسین حسینی ادمین فن پیج خودش بوده و اون عکس رو گذاشته بود. تعداد فالور های اون فن پیجش هم خیلی زیاد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/30120" target="_blank">📅 13:45 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30119">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7061b4b2b5.mp4?token=GccpSAhP0b9KA8YkufcZ0W4RzCpiwGsZCKGb3LhWK_JeJ3odoh8OvzRNjAkTKEwht3pdknzwYGwMstVJJSd8BvdGwSj_vqpJoIl97bcbpnJ-p2vNG8Xt0US6Hrbgs2RJO9IwYOiaXegZoM7BgluH_4-u2VNonoKDu_NFThJOEEwz3WKAUVGBKNEgbwsRS1aJNGEQzk093qQEmNr71j8P09MJtsuU_ZYMcFBEjSJmaT46DfN6AaRbhlgL9aVVNKBqWVDoIODoPNWIXTXA29uS7OOZfsJ_DYg4l452jdlXKrplGcDPjCIM3PTFAOhgrKnN6TozgoENLi_h1hZ_ezsjrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7061b4b2b5.mp4?token=GccpSAhP0b9KA8YkufcZ0W4RzCpiwGsZCKGb3LhWK_JeJ3odoh8OvzRNjAkTKEwht3pdknzwYGwMstVJJSd8BvdGwSj_vqpJoIl97bcbpnJ-p2vNG8Xt0US6Hrbgs2RJO9IwYOiaXegZoM7BgluH_4-u2VNonoKDu_NFThJOEEwz3WKAUVGBKNEgbwsRS1aJNGEQzk093qQEmNr71j8P09MJtsuU_ZYMcFBEjSJmaT46DfN6AaRbhlgL9aVVNKBqWVDoIODoPNWIXTXA29uS7OOZfsJ_DYg4l452jdlXKrplGcDPjCIM3PTFAOhgrKnN6TozgoENLi_h1hZ_ezsjrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
👤
#تقویم
؛ 20 سال‌پیش درچنین روزی؛
ژابی آلونسو ستاره اسپانیایی لیورپول این سوپر گل فوق العاده تماشایی رو درلیگ‌برتر انگلیس به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/30119" target="_blank">📅 13:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30118">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lv4Pn1JBP_DtFOzkYICBj4miL8mLszgj0l7ZhXD_n_dknpES3B_z7PoKdUtVzLCEkvph0iexBIJwekGVMLuCTrO9BMh0CrkehsRspprEZGZlTAPytLEQpxwguVSHZJWGzeKOeiZBISBTVczoQS2epW_G_0auH1ex4dmqyUl41R3yU5E4m5xpQCWqMf0rN1dVVwil97NxMUj5JXRwpYjnElHJ2SkboWs2f-UZZuSDJ6HERsuj6HA4kOsf3fH289ZLRzZerKSbA41rdxqZPmWk-LqVsgk6hDr0i4Zmwj-91ZH9D6rIYxjG09CO_b6fltuHODqEKvhbrr4FJElpOlgzMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هفتم‌لالیگا|پیروزی شیرین شاگردان هانسی فلیک درشب درخشش خیره‌کننده غایب بزرگ لیست توپ طلا؛ رافینیا دیاز یه تنه با هتریک‌اش سه امتیاز مهم بازی رو برای آبی اناری‌ها به ارمغان آورد؛ هفت مسابقه، 21 امتیاز، 31 گل زده در لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/30118" target="_blank">📅 13:16 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30117">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fVU6ElnhcHCwOogQWFCa-xMwUgVDmtqDoUr6_NcFDW30AJ6ToxE2C3P96vOC6kF1-KpcBqGn37b59Q_wWNZeYT9LMvu5psiZNqHBCUFFr9lJY-kTzZmpQeJ32cmm2AcbZA0lgaV7wsvmdcC1QxlJ8oFTpwoN6CF86sLX4oJkn7cSoS871dGrmhovycMr_TUyoFFfR206K2fHqmEyu0OI7oBbLYxmy689QDXvIBV7BXzWy4JXDjQ8IpTd4_KEitfNmxjfyENLRdOsEn-J5TSDnYm1qHqpOAKPGCkG3OTqqD9i6CQDvaTLfiM8GEG0FRk0LAGw7Xjgnsz_86PKacq9Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخچه تقابل‌های دو تیم رئال مادرید و اتلتیکو در تمام رقابت‌ها به مناسبت بازی حساس امشب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/30117" target="_blank">📅 12:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30116">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VePK8Bwk6nci8rGCuAVW8xLemTqr_Q3mg0xtM_56lm5McLV6wniBX_dy1EuJUuppfeKMqZ1-qXR2wPNY3VedOTD-T4UJKxkF5tnHFJ2rjq6uE9vgxlYegBo-Goy1d1DXnnhsNjXlEoPlhVTDN6hawCfbcT7XoXfOoqi4uag1rDLenhdex-JuCUjtfxFAlOU8zaXMcO-6kMTmuSHsgI3ufEd71hJCTT0KVew86DEtxvWRA_Z3UXDYt_yZbAdvKc2eBGEHQw0tn0W17OZMmsG4_lLNwFSnI5SIhz5-PxLYQb6WVFSTPDOatomuNGoK6Kb_2zbgCdMKjnszdFrtHLBBBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ عباس کهریزی وینگر20ساله آلومینیوم یکی دیگر از ستاره‌های‌جوان لیگ برتره که مدیربرنامه هاش درتلاش که در نیم فصل او رو به یکی از دو تیم استقلال یا پرسپولیس ببره. شانس سرخ‌ها برای‌جذب این‌ستاره 20 ساله کرمانشاهی در حال حاضر بیشتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/30116" target="_blank">📅 12:27 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30115">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eWwZCh-ORmAflKjgt8Swt_P0Np_NYYa2WP_Wm4rPA91fDMWn4UcUehJHcSpXHlNfF2NhhNqApEAcOvHIFpova9wf4rv413RQ2WA9N7Z4qVif5009rAtaTs6T_SM6RZVenwz4vr_QnUTOCgRW37fskMwjwodhjJ4rhjwEcdOLhaXCJIIb9ev1h0BpLWcKYMc3h50eCYpp969t34tM6kencDDKQ-zqQ3utctNg_HObaFLSixKWjXu0yVrgnMrmhtGUR6LDC0xeIEP876AvkWJAhpSYG1kdCdvqYB_MYOPnFtRtuMqhCEXRPdEx9-IYPjAVZi6eqBIb4xT4XGtOQ4Ew6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇿
لیست‌تیم‌ملی‌ازبکستان برای بازی دوستانه با ایران بدون حضور ستارگان استقلال و پرسپولیس! این‌مسابقه‌دوستانه روز دوم مهر ماه برگزار میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/30115" target="_blank">📅 12:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30114">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز؛ از تقابل مارسی و PSG در لیگ فرانسه تا دوئل حساس مورینیو
🆚
سیمئونه پس از 12 سال؛ اختلاف با صدر زیاد میشود؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/30114" target="_blank">📅 12:10 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30113">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZCVsVrcjTpZIEgIV7Dw4SbeyeXIgynf8UFyWvcOyyD8groxXqgIpXPdwpY91Tk2LNjfhekFekbzFEeeJaO9NA4dVyK3Wh91yK1NOtsTJPQmbkj_mB3WmKbZAXu3rtgy8iM26oD3sY4VADjED2-LLTC_Ov7erbsInjcfkoRtGGNnG8tzvGZI6lPR7Z2zno-_85ctLBh9kPhX6sQjTUPmTZobIJgTyJsUGp1h7Jjfq_bn8gpgDaecEnUDx0Lumyvv9tq_DF8Zc3N-3LitatizeiHAR4Noj7SLgSpwgBQyXIwvHakXsGD8LETBMfwxPirChre_Utw8MDikdAVXih88MLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔵
#اختصاصی‌پرشیانا #فوری؛باشگاه استقلال اواسط هفته آینده بامدیریت‌تیم فجرسپاسی جلسه‌ای مهم برگزار خواهدکرد و با پرداخت 50 میلیارد تومان رضایت‌نامه یادگار رستمی وینگر 22 ساله این تیم رو خواهد گرفت و رستمی آذر به جمع آبی ها میپیونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/30113" target="_blank">📅 11:53 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30112">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QmWHL6oJH7poRkYgW6SS68JCy42ru2qzJVkwkhHPJMBS4LoclSKP5LNkmZdYvA7Z9lqbOXN8cp-Tfd1zYh8pKGCAHKoXalFjOVA9P4lIBHvFwez-nYGOaiU5ePVzYlkrlWXayyLxkxGiIknG1bvyUSUBsAHck5cYi_PtM6Fg_ubzwS4OjuOw3ENnqrPq3DJGOZ9HBN2pzUngY6UWpnAfltYY198047k3vO9_S6pYs2xAVbJA_TYzc455VN0Ec7EO_O8Sb-10TCBKJ71bLc28f4ojOjy6uD8KGLKwNzV1ZKkc78oZutQUHZbbhNr9i7-RT6AulGqbtBmqJsABTjQqGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
رافینیا دیاز تنها در یکقدمی رسیدن به رکورد رونالدینیو درجمع‌آبی‌اناری‌ها؛ از رونالدینیو تا رافینیا؛ ۲۰ سال بعد یک برزیلی دیگر در بارسلونا می‌درخشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/30112" target="_blank">📅 11:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30111">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KnMbVfUm5IaC_sb5je2UHA8VeYB-1TFVze3l0p8gzIDEs-gxlx9mHIfG0ibC1-wFiMqsIjKu75A2Mf8x85Jq2IKT9WTVkRWseSMp-p6JURc2C_sIxVpzsUkjRrlmWTVcwfT8cZgjpikJXgtT0YRIKcalzrXCnHoawobhzDR0gil41SOpW1srB_vUWwZP96w-s2N9_FJB3gWa_DMLUUNEJ-jXfomeSxEXrO3rJY7WBmRRHe-gV_38scXTRVbNg4WOKIVbqjEqVeJacpJgpdSkPMcRexBpXwDLlFMYWzfQmztrSyLzJY_I7YZKcZIRHMA_EhveAyXE-pdmi_CjitunHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست‌آپدیت‌شده‌سرمربیان‌لیگ؛ مجتبی حسینی اولین سرمربی جداشده درفصل جدید لیگ؛ سرمربی بعدی نساجی‌به‌احتمال‌زیاد سعید دقیقی خواهد بود. فرهاد مجیدی آفر مالک نساجی رو رد کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/30111" target="_blank">📅 11:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30110">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPgBOpaxFPSDi73cfgR3PiNR962bxugv7aEGToKmJW1LtvBavFSgWGiM3BIynZuf9KcPHamPNLngdGnaq3Uh_k6sawQSzvau1PL3wSH4MiL_vsFhO24zkbC9DrsKWuz7eOpaIyLrtTAdW697UJI0nbzWdMGKpK7c9SPy1FEK-9O5tymiDxmTvNzRMd1XHGKWCnBKgwU2nWEbEQpvpcbOuOG49ITGw_oSvSaTA9mAUR9pT4f5kwIA4oB-nfhK8Q6mKMzrsH3H57iraHz1p0DfnWCZWL6Vqbopyy3kBkPsCY9EOv55LYsftnvedHBvD98EyZxKKrwbxXxdj38olsqkEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
تیم منتخب هفته اول لیگ نخبگان آسیا در غیاب ایرانی‌ها با وجود درخشش ستاره‌های استقلال!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/30110" target="_blank">📅 11:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30109">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLK5QnupFyZSNVUqLdg9sEwsHHxiS-JwqoRw0DKpV6ib6uxu52s5NwUvELnSt8_cfuvy6TDekU9vKgcavMt5ZfX-jfNdKvxv11burmROUst_4-D2AEUnm8ukaMD_DumBoAowLemDvaHSsrzS22PMZbanum9I9uWwJj_rUVhapLqsEv5AdlT_G9wGUCIzRzAJipTAAe9ickfb1xUMM7-07-QihJRqaLlxumseivKjhy9Y6kWImyHGROxju6iXJ3kh76aXKb60auuHg9itD4VotWFMmljuczE-yjcKY2gAgxNBzluKw0dD-XOiECyBV5fssx9QlOojX1AeqCl7U8Jfew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
⚽️
لیگ فرانسه
⏰
شروع بازی ساعت22:15
⚽️
مارسی
⚽️
🆚
🗼
پارسن ژرمن
⚽️
💯
اولین واریز، اولین برد بزرگ
شروعی هیجان‌انگیز با
🤩
🤩
🤩
🤩
هدیه خوش‌ آمدگویی ورزشی تا سقف 250 میلیون ریال
🖥
امکان ویرایش شرط ثبت شده
💥
برداشت سریع با روش های ارزی و دلاری
💵
شرط بندی بدون محدودیت، بردهای نامحدود
🎁
با هر واریزی
🤩
🤩
🤩
هدیه ورزشی شرط‌بندی میکس دریافت کنید
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
r29
🔗
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/30109" target="_blank">📅 11:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30108">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇮🇹
در هفته پنجم سری‌آ؛ دیدار تماشایی و مهیج دو تیم آاس رم
🆚
اینترمیلان بانتیجه مساوی 2 بر 2 به پایان رسید. گرگ‌ها در نیمه اول دو هیچ‌ جلو افتادند اما در نیمه دوم افعی‌‌ها به خودشون اومدند و با دبل لائوتارو مارتینز سه امتیاز گاسپرینی رو پر پر کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/30108" target="_blank">📅 10:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30107">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KlwsaxS_1SzKFkTxzaatLm_-sTkBaATDCOcVUPcc0tgRmz_ohzioNpTfCAue4rswZ4gXb64wmw8wvP_RyA0uE7XUW1vXOF5WEe6s6I2g_UOxG5ErfY6W1M8Ua-b81hyqr2oiSAhvFyFZMR46-Aox9XqFrmFmbH28NLDbZOHSCRb0Gn9nDZcDHflpafYwX7IhKylVgVxOzNkY30pjj8uAvlrfFD0bQYSnZe42AY4xO1IK_eyx025jr8yLml2isoQ2areo79NsI4OqnQz5A1q9KZUXKWqcflfbpDlKFK4xO-JRYFYi4GSt1HIGz1Sp2wgnRHTWvbS6YJhOL-d9ivcWUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
شرکت EA پیش‌بینی جدید خود را برای جام جهانی منتشر کرده و بر این باوره که اسپانیا جام را به خانه میبرد‌. این شرکتم تاکنون دقت 100% داشته‌. ببینیم کدومشون درست درمیاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/30107" target="_blank">📅 10:13 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30106">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s0kRh2S0MYCqJJkP9k8nMxL9wZ8SMiT1UqghME8fi_uLWwWzk0JXQQ62_2JZ35rOMoyKSfEblTFZPYhSMVIUiTDsYkOGnf3iyC64f5lLo15Sw7xq8r4oGo6QjvRwM56g_Uq7T2yfoaHthhPBEgIoSfAMcVahQdTpfpq1z4eNOx-I97IPevJ9qxd83CcbMUdlGHuk6dLIrgrur3-EW2UTfr_i75Cpa6zoluedznUet4_bAc7ODtqFTI6JFYMK51CJnfyNYOOL-ioOhuA5BVPvEyeJMVuVXtbvaraySm9WZ5FhjhY350mbiBx-Fk1mKHittyvRJVG1y_EeSlNNoMhjUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ژاوی اسپارت فولبک‌راست‌بارساکه‌دیروز به لوانته گل زد شروعی خیره کننده در این فصل را ثبت کرده. هزینه صفر و خودکفایی از سوی لاماسیا عاملی‌ست که شرایط اقتصادی بارسا را در سه سال اخیر بهبود داده است.  قرارداد بازیکن تا ۲۰۲۸؛ دستمزد بازیکن، هفتگی ۶ هزار یورو؛…</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/30106" target="_blank">📅 10:00 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30105">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZhQCWv7cI5GNX5l8Q-pCAo74e3xqCQy6h3hgX-GS3zH9nCB5dyEA_6BjZ8sioG5xNtFIoiXCus5CT7EIVuhY9i0Qm45f4fFR6hrJwmWzKR1PYYmZkwyFYqJLVwPljLxWH0Ccdo5O2rtKZ9sUF7SyN6_skf5CpvsPznx89pNoF8y6jD63F8ea3wDCT-SQEnqSyZnuBegLTih0WhXB0pHDKS_ihcMB9W6EnpvMfu6KMAcdnn0_dHlW3fMydL8okVlK6TzzG9NqmMrUMW_xNwvsYIK3mOfTExuZbTuRyXGfvmUUbPXvczqmxTVq3pjDH0FrTK3-lFTd5RAOWUhhrrnrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ محمد مهدی زارع مدافع میانی تیم پرسپولیس که‌هشت روزپیش پاش هشت بخیه خورد از اواخرهفته‌آینده به تمرینات سرخپوشان باز خواهد گشت و مشکلی برای همراهی تیم تارتار در بازی روز جمعه 17 مهر ماه با صنعت نفت نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/30105" target="_blank">📅 09:25 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30104">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bka3hgFYKSmAZVDoMRqSfCCE6ep1s2V_3kYU-rcii0zUzToDq61cttnaYr2uaJYwnP2FgUqGMTHvq0AkZGSXhFhP4Gbn2TBIXu7I0dN7Blm9z542bkNx43RGvSKSHUhWHrhe3PfKc0d4Se-VPzT-WGZPH1NrYoCc-aJX90Lj439aExUyyNDziXpWwGmiQ1V7TQrHqTGSpX5hpeZszheBwDl4r5ub0Jgc9dqhBW5ZUMAFBmm4YWlEkARPx81oe_Z9kL488c7bQDRp6rAV1NeimUSk7guOw0pFyYuBleue-UjvM-qkUsecIUV0XrmiXX0y3byxyWUjlhvQh1LjkmAAJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ماخاچ‌قلعه‌روسیه به ایجنت‌ محمدجواد حسین‌نژاد اعلام کرده که در پنجره نقل و انتقالات ژانویه "نیم فصل" بادریافت یک میلیون دلار رضایت‌نامه حسین‌نژاد روصادر خواهند کرد. سعادتی این موضوع به مدیران استقلال و هلدینگ رسانده. حسین نژاد درپایان فصل…</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/30104" target="_blank">📅 01:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30102">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5OlfeP1Yl7oZhp8y1oVatY8DpeSGXctpLi6J3JH-mLoIgOIwB3-hI6mudGjPY462opnhMm6tM4IRCehr_g2yB-f7LyDX201-otjna8IhRlNpuvnR3V2IKJHZHn0Wtk8zBJiO4ZZfD68UjoXZffO-wmiM-HnHnkl-WWdsYjmqsUCtd9k6N6ELYsEg2Zyf-xH6b6X3JG4bn2Djyw0AcGTisqZh5N_poWyad1TOi19MFeYyS_twzS-bChaIYDFiFj5vnwS_TtgDH4pTPZwo9wDBJnAXrKw9sIERXfCHf82BkLrVIXjourmAOrA8o9cS5TItHYO_6zaO1JCl6zOyJu2yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز
؛ از تقابل مارسی و PSG در لیگ فرانسه تا دوئل حساس مورینیو
🆚
سیمئونه پس از 12 سال؛ اختلاف با صدر زیاد میشود؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/30102" target="_blank">📅 01:28 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30101">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VNqkR91-JXVaF3j2uXWNmlVoyEyOphumrxadWCh6MQjO9P1Zh7EdAPAJpVHhVHNrpQ-dnsEpbto5UDu_Y1wKyRm0MJNNDUt9i7o0TfslK6gWFX1CTGRAZn96VnYUccME0C5_bX7jS-9Ng9y_xl40cVRt2FGs9i0Tak-Awe-Om9eFBuPpDS0oQNj6FNr1JNNtlfkY25Q25bqzSex2cadepBda2-DGEtk5JKHac_OZf_IdkjmhBmtpimg8RjyOMmzyOA9S_XdLpgEySaQEqWJIGRwZvdLo_buGsf8FPicJE46YoY68CYw4QPHd8k2VERoiReOnChpdqtghyRsK1iGNdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
از برد بارسایی‌ها با هتریک رافینیا تا تساوی در دوئل آماده‌ترین تیم‌های سری‌آ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30101" target="_blank">📅 01:28 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30099">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XvsKrwPa9Wy6k_vqhNdh2xSVgyMi5P0nfMvj0EVdPifhnrlQzUgRmIRbinCk1fe5-78N4Hqy8nIfA9U1WH0HhcJ_EOVzHsKkuKVh42s7MlYMPfB61HvkkNoYSDDa_VbAregVITn40OO2Eat1Mp4-b4Z4ZlF3W7YnlKsWWffm0hGMtQ9JkHoaI-TFj6LvVgfq9AriVj69QqF1f1VDUFFwc1CnchsjlrkzU45ftPZGyIKH5aNKvEq-H5MjzBTddHpT8I419V3ePLMDS1lJdFSHpI5RACoWev1YSXP1RwKzSh49Ez2JZ6hFvO-xVvVvQ9jMNF_dW-b-SdTFTZT4dJ-jWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k7hg6Ar_lVnaGQCKPCBAV03jw0h039sBKzghO9ApcNju6gbdC8L9k5EyQ8gf-fLrGrHJhvzQi9K4RqxVeObL5jbz6BzwUuBXb16cNPIwgAg49EXJlSHLDt09mxtqa-QZAqOa0CkRI6k5CxRqIIil04aRhbHonLiDnxF7hNsUWmFUquCk5EIrW_yvaKpd0zo3xwrryffo6sY8eCgcNq2wBaFOL0jAtk-o93S6V7TE3_IXo0HHCORTcrKWM9UHn3UC4F7oJofWYD4Q4BLeqz5Ulijdb4pUvqf5Wy5eK4ypbAf4nV_yIdqo5GYT5zZLvFhHue6z2ZzJqd_Z4HNFZ4YUdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
عملکرد فوق‌العاده بارسلونا در این فصل در لالیگا و چمپیونزلیگ: 8 مسابقه، 8 پیروزی، 36 گل زده.
🇧🇷
عملکرد رافینیا این فصل درتمام‌مسابقات: 14 گل زده، 3 پاس گل، میانگین نمره 9.5 از فوتموب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/30099" target="_blank">📅 01:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30098">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bMxdFqynVWFsnnzl5K_D15i6Hzh7uZj1V3oBe6hWC382P2L9edfvyQMGa_bsreX5cVY_7FxOrH0nRzM2iPP96XTVE_w_uzbdzVbuSfwP-NqgA_Ppuo0DCq0TIOTfU4wo098WmZ3KzaSAxNqWriH_2ANhc91s4NvRni1W6WPa9VrAxRX-4Hj6D-G04SEvmeTD2wpFihdUWgrUYz8k4_oPyBGSb3H18EDKT_PLpfjLx3-puk0WFbJX1X7xR2f0d1ZbInbh-gvkY8ozmIDraW0A6QVqJZ4kCvcLGVT-CkiPcgH8rdXD62_bwEjupDKU6DSVldDjkTHJmILyjGlARShw-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
عملکرد فوق‌العاده بارسلونا در این فصل در لالیگا و چمپیونزلیگ: 8 مسابقه، 8 پیروزی، 36 گل زده.
🇧🇷
عملکرد رافینیا این فصل درتمام‌مسابقات: 14 گل زده، 3 پاس گل، میانگین نمره 9.5 از فوتموب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/30098" target="_blank">📅 01:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30096">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5hQq4ZpXIgULgQW_S7KG8xisk41b9ZR4popmNt7qGHJuoJL7pi6LRlrOo3FsJAWSb_82uLQrsQy7ATLw6g8NFQs3mvx81vfW3xrWT7ERXYzpEG2sRBWIwGGtyQIKsrpmM-EsUxsK-XQTFyrZ4IqlKrenPz6GMUFi5kroVadIH0ia_6aK46B2A_zi1tZ278oWc6OcD8T4pgEFh3N4Wv2u-B63mDtBHrZy9-DRvIaFouOU5E69GoVYCJBJyOgqMryiYtnY0rjIH_r200XZoT4iU-Gp3teGDZysQEKKuLe-l3zI1s_MQMaiZbqWzI85JKT8LN97SNhh_fYDlKoZCL3sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هفتم‌لالیگا|پیروزی شیرین شاگردان هانسی فلیک درشب درخشش خیره‌کننده غایب بزرگ لیست توپ طلا؛ رافینیا دیاز یه تنه با هتریک‌اش سه امتیاز مهم بازی رو برای آبی اناری‌ها به ارمغان آورد؛ هفت مسابقه، 21 امتیاز، 31 گل زده در لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/30096" target="_blank">📅 00:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30095">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LcyBdXhgvNbhPrzDJgfxKEC8F2OBP_bpkdq0HQMzXZni8wIYuMooo0wBtQBygCt7ccaO8Rfi-hCxR3R70QNRHzQrvaxlznyuRX-GGmPsZUw0yETI6Z5c5pb9npxPOdNJ-kA-ZDNn8EHG5QFhHsOgKaNEln97Sm8dW8pGJmmNJjRYHshPig178JZqhaea4a1jDE6ztKTpt5QR_LQwKy0dXZrNZMOJQ7MQti0bVFFDOMIAVF6lnxmOLi9DigmonaJBiRHkvI2AS9RuUyynSWGVdOHfDyxj_luC8P5nkg-D6Gz0NsTaRjfZ_ER4DfQ9D_n2pBYy7a9GbzRVKMkRqQS0lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یه‌بنده خدایی تو سایت پلی مارکت ۶۴ هزار دلار بی زبون روی پیروزنشدن بارسلونا مقابل سویا شرط بسته. اگه‌این‌اتفاق بیوفته ۳۰۲ هزار دلار برنده میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30095" target="_blank">📅 00:29 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30093">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YavETOwIWJbv787BKcAfkVbtQ1MYDrngaPK2iZk1q9MfxS-P96ubND02byqyEG2RFRocLsReXfWlqYWEsYkJyZNRaYyLu71mqlv1VI5wuuapj5zoKF-KPmUuw2Fsf5PEE6SrPlRCOxnu4oIz1qKY1vwylf4tFaTSjJecxLppVmRrPdkO-G5-KKCzvRdbINq-GPG4k1fBsfwJ5xXr1vQzhVvXH8dFFLzt6ZwmUFUfKWshr36wE0gn5DzoASMGE1iZE5KJpggz06p0WZQs1IcBk6w12VgjkpYKEUSa_N1gJMnMMCn5Hb7DuPFL-kRaj7J69XtIQXHan_HH10tOfc1FpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
گلزنی دنیس درگاهی دربازی‌امشب استاندارد لیژ مقابل  سرکل‌بروخه درسوپرلیگ بلژیک؛ قلعه نویی تو جام جهانی 2026 میخ کوبش کرده بود رو نیمکت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30093" target="_blank">📅 00:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30092">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GYZ4ql8uBxG7nqCVv-V7Egx28Ymu1me0GVLcWUI_OlUKeGoFudD7N-CgllJT0jmRc7dH5Bup_8DfCMsGMmP5Op2B3J2-Wtmrs4RD7Q-OQkqR7XWbaywEj0E2HZfzB8pHnNqNb3iM8uhwANHQRhfcmkX8I-aUUaBdDg53HoDUcQUbT4Wad4Xn9V0FmBB-6QdWge_1Et86EK2OOvMeM14kT3sasC_Vmog4YE04_W1MAAKfAQpVUs37tPjRk_TZk9qK5-czwjjgwBD8SqoLSUiKakLkNRRiUHv8PiG-dexWqNxRt3XZMuZ2kg83r5Icm_J0c-e7_Co5hMLfbgN6_PHHBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یگانه اکبری و آیتک سلامت دو خرید جدید باشگاه استقلال برای تیم والیبال آبی‌ها هستند.  @Persiana_Pluss</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30092" target="_blank">📅 23:39 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30091">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRpllZ4ChsPw_lQGf7KbRU4lW4vXTxAdvsoQiiolQlJxVTrMJauPxtfNPmfSKhr_V0J_ATfZj7R0nrIFEF9Xb0MJZPX5iCBgm8fiRODvNveo0ulGvKS7NQOT5yi82kcVU6OvF3s9WJGDC40qgsu5-FvbhU01AlzOYV6Lyffb3xLpd0tY2Cp8BXcdLV81GpxLaIj9opBXkoNzXmixd8_52T_f-M9lABHdVxYZmY2f5bgurUNGp5V5ynSkbQum60VdS-d3Wrx47ZT52B2Ng9ARoQ0s5UixFs5fet2M8pTiZ7e8lib2sURo6Z4uOjtab7TsxIcPGnGvQ-9wSGiH-YI3_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سه مسابقه فوق العاده حساس در انتظار فوتبال دوستان همراه بامراسم داغ و جذاب فرانس فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/30091" target="_blank">📅 23:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30090">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇹🇷
🇪🇬
درشب پیروزی پر گل تیم تزابزون اسپور در سوپرلیگ‌ترکیه؛ محمد صلاح ستاره 34 ساله مصری این باشگاه باثبت یک‌گل و یک پاس گل و نمره فوق العاده 8.7 ازسایت فوتموب‌بهترین‌بازیکن‌زمین شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/30090" target="_blank">📅 23:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30089">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/af6dBtqWRFMZxVtGkx1HhX_Xxclj_vchityArL6GzPPNUa4Mhw4aCkpscy21X_lnpsuTxO8zx23vA8wFZdTy5YUMKH4KBDCXJIf4Zxyy-goQwN3v-_KHZglPPcF0NEDQGByHC8-9Z0k-V50xMNI9iofOtgnq3RkHu7reirMyVVUGEf6BQx0DhoXlwbcONAVB355S3AzfvjwqkItMUVSbnF1pAO_Bfjjru_88zLN63nYc6hZaDOqUvtzQMd-r_7RzaWaVorDjrfRtkh_9gUUEHhiMX3w5rRmADbmAMzVgpV6X5mM4K1cJayEbSjF27ijJ6XOX72ujdFBraL8grxB-Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ مجتبی حسینی باعملکرد دوبرد، دو مساوی و سه‌باخت‌از هدایت تیم نساجی استعفا داد و بین محمد ربیعی و سعید دقیقی یکی‌بعنوان سرمربی جدید این باشگاه قائمشهری انتخاب خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30089" target="_blank">📅 23:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30088">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ty456aXqkWQUUVyvfTNM7dijfTR1-u12oDUn5elUyooN-rNxf2fNlWML64LfPAjYCnsfkBoYi_xRN7nQv1tAGFhTGRl18MHYPvCDvLnPzZF14bVqH3ohvyGrEUK3KYE1Eor-XqbVp7aQU7_X2w8gF87grhN_P_Eqnj38B6iiSHtMZbkslqFAuO-3VfQas4J9HVswx3Jjp5dl0vWEJ984F40Oz08VO0qYNimRz3o-z3zpd8ODxBwzoIfMfFW_Ytge7Nr9EhZkOLDCRVGIwwYRuiWGYTn60VvcK_rXj23mARKK-ma6GSfpg98_2peLTpscPLC01jfaj7gWhuk9tsv3Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درهفته‌چهارم‌بوندسلیگا؛بایرن‌مونیخ‌با درخشش اولیسه آتش‌بازی به راه‌انداخت و با هفت گل یونیون برلین درهم‌کوبید. هری‌کین‌به رکوردتاریخی 100 گل زده تنها در 98 مسابقه با پیراهن این تیم رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30088" target="_blank">📅 22:49 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30087">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V9LOu4_CBe5ihuo90C2yQGOY1AISx3CD3EZY2QH4NV2M4h6qWJPh_T52BWwFaX6TQCWro9iroBTw3tz5Yw9zU3xwqoY92Vqj4WmPMgu_-aq6b3KTNwr-u0kkfAg0fSzwgh6v8s3EgNXEkpsl4Bf4AmVm7kVfmhPVfJ3lVy9jBE69YFlLRqZU5JcBBFiFlcZEbUOEKq2OdVpPy7vs9MOtbJcnOuZfYeMW5zeC8TeAxi-cZTDaySq7HBuX1V61uZOwDN_X_Mbg0o6NiQzUznwgDuDrSWOXHPZ7UinXDB8UXtnGFu1rU6VuHTrAOddGanS1fOcJES58PSOV1U8uOdGyfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نگاهی‌بیندازیم‌ به‌ نتایج مرگبار حریفان بارسلونا مقابل تیم‌خوفناک‌هانسی‌فلیک؛ شش مسابقه، 34 گل زده خیلی‌خطریه‌خیلی! 38 روز دیگه الکلاسیکوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/30087" target="_blank">📅 22:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30086">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/epXasYOEhSIjnRnINbGX97zQT91n1X_696xGvrWK4Dl1CxmD0EPmHQrd-8y0gFBjCHOY_96dz39qGA14vjRC4LkfbUpF9W6PsxNdGhKPkzocjnlF4ek_Vc_FQLpVdBmKYDAA4CNKaAdjth_VQUJDNVHPYEE5dkMWvfaJrev3zP-ahIhTZj6Q9QnCyRyBc0kMUlhOjdF4sP4M-vi_Wsmh4ZsziqFDvXYqRKMGxOjf-Rvb0gybk9FdxoKtV9ajDDbhatPxhZxuV3KLoyenKH91UG0_9cS5VKLicrMDm-1W9iPotV6vmiSC2BiQr_aq409x2_P5e4Y1FxeADL_20yd3Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هفتم‌لالیگا|شماتیک‌ترکیب‌تیم بارسلونا برای دیدار امشب مقابل سویا؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30086" target="_blank">📅 22:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30085">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c9-iLZnpGEL7FC8GinRAqRiyTBd7vjbatEGPYMUnWJ-F-SG-Hgo2vX_khFWYEFjj2L8H2rXp32Xrxs0aLVfsMelo_FsAqn6bObyjh5opwDNdQAZGVRk8UWpwzwudo6wLygE22U4cp-8KjqoP2lfLvpdVJbP3k9UXif2XtVJdyORWvi8K2YD_72rdxwQ9X7oLZs8IEtNLptjiBIjRPpw4RzHCqU4S4O5ODT3WJTXcJfGOy6yVu8e7jdpn-eWliWQD32RnQ7sIR26gVgKp_mVy6xMCJcXPfvhWybhXMkZhFddiIi2n4Eo8tSiWhYFmXUS7d_0MriFd4DiZnfPDbJrG_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
دومین گل مهدی طارمی با پیراهن الوصل؛ درحالی الوصل امشب دردیداری خانگی دو بر صفر از العین پر قدرت عقب بود مهدی طارمی به این شکل از روی نقطه پنالتی گل اول تیمش رو به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30085" target="_blank">📅 21:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30084">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lUNw2jC6xRjEDYxMY2NPjvjzJ8I_0_oqEz-E1vS5DXrmXuQfqrW6xEJ3KrrKWiDChkL81igDfQaOlJYjjg-l_I60ClkuUWsIK1WQbzji4Cbv9Ko7VIG5FDnpLm6usy193MIj-PerdC8gon2cTzyDETQUN6cLRTXsRRr0hMEbgfhX0-1o3_3BKs3sA2oFLPLso8AdmnvTgAcsElIXhtNgG5e6kLkbzbl4V6613NXAM--psN9zHdwxGLSgxK7zmnrWxwvs0b1c4hGxp-6LCof_puCbSQw8K1kg16FzjndDjySAr-PpVIbifcAmwFZ-qBdlja-gN21aFY5mx8LLLfYq1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
در هفته پنجم سری‌آ؛
دیدار تماشایی و مهیج دو تیم آاس رم
🆚
اینترمیلان بانتیجه مساوی 2 بر 2 به پایان رسید. گرگ‌ها در نیمه اول دو هیچ‌ جلو افتادند اما در نیمه دوم افعی‌‌ها به خودشون اومدند و با دبل لائوتارو مارتینز سه امتیاز گاسپرینی رو پر پر کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/30084" target="_blank">📅 21:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30083">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8o5eWTVPLtQKO2lJdnzRMpS5VdnXi6G_JAsc6s4nYUkVQgHjeLkk_oaHd4Or4JrNzuMdpr67xA98gB88A_vE5ossSCxUt2H9H5tKXZ1tBcH4x94AXzqlDpJIecG18cDegqqfFqYsKfulHSftyAqED0-bFR4okwtAk3-FOJ7gHuSg4MAoDEw1duLW8njZHKHzq_3DQ_oR3s-qeFFqJaN4mrrCFRzMFhzLNsLslQWvy8VY3f6PUfJc6cvTCnjgtAO1Fd8-XbeT3wLmdeU3BeItDsX7IUCcs6Lq0TbPbH8W4UAn0YlQ1dMer6mDKqFERY2DLc3ygpTWrhAUlyKwhNZYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هفتم‌لالیگا
|شماتیک‌ترکیب‌تیم بارسلونا برای دیدار امشب مقابل سویا؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/30083" target="_blank">📅 21:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30082">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FJYjRbPyjIoorg_fmUqm1qTTSn5YaZjplJVC0mCVsaCHHcY15g1PZID2cacTihq7MjD3fFoROuO5c5ci8Wn7g5TXmRCiJk9ZrTjOucq5c7BZ8rx65Rs0mISQrkEj0J9z16Zu76TLCka2Fpli9Ec6fXWIGYW5C5E-ueWTUqkC67VapZqz9oiVLif5kxwfuEscsIll00_WzhdVx6xpzqJqs0Gwqpkd9E4I0lapUXMumjm7Cie6jBWEQ55cpOAG_EOHK-zw60brIWjtqG88vQtgOwHAsrZHp6gEujkL72z179xnB0msDkUn5l4KBZAycGCHlLIidkHZ_C3Qs7eqni2z9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
ویدیویی‌جالب‌درباره زهرا گونش ستاره تیم ملی والیبال بانوان ترکیه و یکی از بهترین‌های تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/30082" target="_blank">📅 21:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30081">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c7LqqpurcUFCacvb9iXBDNz0-nGyhl2Do0IcfDtXosHexIxT9blmRA2ujSC_ScPiqaffiRo-UmrGeswvfMMac3-8s8SpSPGS1rcGsQF3p_lVlE2KCUOWWx2h_7Vgl5TNpe79Hn0UMDh9hh6nd7WWC8yDVwQpdyg4fkp5HpcQHASQxj6C4GX47yR6Ymavhx3mosnpvm5kxvrVYlHvOd0X4Y2N80WoioQQQ2kncTryxhOX10DC7hkgamCMhvxJp21oB22C-raXcL91-Kg0EZkCpAOI8iObryjwxc5o87eqjBCC48orGp3FdLWzCTeuP3NMS5iqLonvGLzuGnyNGqiJ5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمدرضااحمدی مجری فوتبال برتر از صداوسما انصراف داد و به مجموعه آپارات اسپرت اضافه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/30081" target="_blank">📅 20:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30080">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d622da65b6.mp4?token=WGYZqdUpnsaO8uZ4FP8tfb9PHgRWdcOprNoBhz1r2joEdYoOlCYFCzQjp1KNswfiQwt7JE9YYHjL3i7RYNnbZwJai_K48J0EnvJ8YzvlCs8zfKFhfltofneB20qLRhDfI8fkV2JeSnaqMq-yCIq1x41PNONlrlYVvZR2JWJi1RtOsgTwmIV01Wm_yfT7CfNfiXY9AZboIUJ16Z0-erm0AhyEqjqrfUSxanwZzdb4D0MrCN5Td1MjVnWM7aoXdy1MDGt0xDFYjAOSMffm1Y3N85EhY8b_YyJ25NrZBNGbUIbjCMjoe_IdUDRzqMXcckJN1kAcSNpekZz2SsQcFrCY9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d622da65b6.mp4?token=WGYZqdUpnsaO8uZ4FP8tfb9PHgRWdcOprNoBhz1r2joEdYoOlCYFCzQjp1KNswfiQwt7JE9YYHjL3i7RYNnbZwJai_K48J0EnvJ8YzvlCs8zfKFhfltofneB20qLRhDfI8fkV2JeSnaqMq-yCIq1x41PNONlrlYVvZR2JWJi1RtOsgTwmIV01Wm_yfT7CfNfiXY9AZboIUJ16Z0-erm0AhyEqjqrfUSxanwZzdb4D0MrCN5Td1MjVnWM7aoXdy1MDGt0xDFYjAOSMffm1Y3N85EhY8b_YyJ25NrZBNGbUIbjCMjoe_IdUDRzqMXcckJN1kAcSNpekZz2SsQcFrCY9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
اولین‌گل مهدی طارمی با پیراهن الوصل با یک ضربه سر دیدنی؛ گلزنی ستاره ایرانی الوصل در بازی امشب این تیم مقابل العین در لیگ برتر امارات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30080" target="_blank">📅 20:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30079">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oWoTI2c9JswV24y_-WOV7K_xcZuZ4VWpvj9W2XYPCeJiBmjzFuVOlpK9J4f-hj6Byon1pVXDK-JhpZzqriSSAfc6XQEfPEr0C1nROQ25U77WdG5rvJ4-6Ol_xlWD4FHbDzL-QXdyE0dgvIOQOHzP5LN2IEVTfiDPUcOcejCjYkdsPyqkwdNxHMcFoQcG1S2tgyF52sSGwxKBLO12wWF097_A0thAxT2eOWAREoBSenk7PpH85hURJd8_pnDa-Xpjf15oEN-WqJeIvEVLca8VkMI9jFFerB0cGhRynOgwSE7Gw62TRWLmG6i60tQVRd0DR11xmLK6od6uemU_jt5xvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
شنیده‌میشود میلاد محمدی از وضعیت خود در لیگ بلاروس‌ راضی‌نیست و ازطریق نزدیکان خود در باشگاه پرسپولیس پالس‌های مثبتی نشون داده تا درصورت موافقت مهدی تارتار به این تیم برگردد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30079" target="_blank">📅 20:37 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30078">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BskDjZ_Kp66kRR9Ee1_3LcOsFYH0-ibe10EYBggu0D5UIMY_4uqH20MqvEeR0koOiprDvuH8wJWFYNh8qAH6Oyxhj-WNDPAbXGbKH0DJ2Q-PweBbwruBMEcrykE_WFXWjGfh38iR0a_mhJ5pC2j4qN4N5iH2yAh_gjSAAtdU4IHv5GB0yUsPGfiikMPnCtZwW3j6tc7zrwzEYJjHPpwdmudeYqrvpfZ1t7iDUXp5znptBZWW0839w_N_16us0VdyvURdoxY4xYHTO-zXQP8rsUUv6NDodd2h4kQn0ZAyeKDm6ZGk_sFOhI1QiKK5-KltPIXkyqq8ZRtrHVPiD_7A6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
ستاره‌جوان رئالی‌هانیومده صدرنشین شد؛ چهار بازیکن‌رکورددار بیشترین‌تعداد دریبل موفق در 90 دقیقه در رقابت‌های این فصل لالیگا. نکته جالب درباره دیومانده 19 ساله اینه که مورینیو فعلا زیاد بهش بازی نمیده اما این رکورد رو ثبت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/30078" target="_blank">📅 20:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30077">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tz6Y7BcwH8gT21JXUncqyXnCZMmFVim1-O1gSbRVU5GV0iZxoFrDPK4Kn1EfpzOw0L0_d_qGKbRW_cTCW2xrGlykK59sHn61HJZPA0g3p9gyJNNuRZjWgbCuTStTRIbhlvNCcqBg9EWQ8hbagLDM7UJ7bjV7zUN63cRUzj2tUtn1wMv-TOTfT8n4NdAQXkSoyC8Nhuvs-l2ZTUp_1IHA3attpfVvLcaOt53UaOzQu58EUfCfG3sSiqRjEOOWldg32Y1L2GiB7UoLqaEXB0dAXpu93Yhx_amqCYog7-dXd-2jLYhnAoyezXY2Ts5Q79Q0-EOyeDPkPcRsUxddWHhdKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درآمد لیگ‌های معتبر اروپا از فروش حق پخش تلویزیونی در فصل جدید؛ نوار سبز میزان درآمد از فروش داخلی و نوار آبی درآمد از فروش خارجی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/30077" target="_blank">📅 19:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30076">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🟣
در هفته پنجم لیگ برتر؛ شاگردان ژابی الونسو در در دیداری یک‌طرفه‌متحمل‌شکست سنگین سه بر صفر مقابل برنتفورد شدند. برنتفورد برای‌اولین‌بار بعداز 88 سال، تونست توی زمین‌خودش چلسی روشکست بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/30076" target="_blank">📅 19:28 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30075">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FlT7cuChYvt_1V-toW0wsr74CqwyoA7YUwb8BsD-Q0VAGUD83i5_s1lLo-I-gbonrLK41tnwOcGRJ6rKMptHCz655shBZH3Jl-CzSvkgQinQgFdBuXCdYCk_roQUCSF4zMwbGM5OBfjkLxxfgEofCYqM3toVnspU2i4zc6jUJu6SKDgAzZUE7qfPw5ihI1rZYnCTTWDa25Oi2H8UYH19lMwP12rg-NVtw7KkB1embPNJ4oEVsGhGoV8lTu7mOwmgj9CDcXvCs_WoOj_-JO8NEaJtQ_boYMtoqQBBaMF9q96TrtlOzVhIHsKX-WGhXESwkm8rFRSzKjGV2aAdvPexsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام دیوید اورنشتاین و رومانو؛ بعد از منتفی شدن حضور ژاکا در چلسی حالا این باشگاه به درخواست ژابی آلونسو درپی جذب جردن هندرسون کاپیتان 36 ساله سابق تیم ملی انگلیس است‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30075" target="_blank">📅 19:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30074">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5018b3d28.mp4?token=lDyjU4FCWMDtOutHxUjbAO7A6eQsJSytAk8eiDfUm4wmXyitLwQ93MoYp7A8v_z8W8ItgmMpcEaqm_IlNyTErH7BPi3_S9y5hBOYlz4JiDJ-3kg1d6SXkQzc1X70ZcsQo-S5Qt_0ogbMy9BpDFPhx_zxm-yI_lkA0SilKSuNXeLstUdEEM1-377RR64hvzQZXSnksyzlTRyULXEeEpkB_Jr1PwCFgU1yX2J7fpbpMqDXDw0KZWRl7nnhegze8jvLKyyU40qB1yih6GIT8Hj5a_Mb_Zo0p4VJtvs-zNG6pwnhJR2PCgvIWji6mw-ICdfzdWcsRFXuwTrJ-nbezAMNkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5018b3d28.mp4?token=lDyjU4FCWMDtOutHxUjbAO7A6eQsJSytAk8eiDfUm4wmXyitLwQ93MoYp7A8v_z8W8ItgmMpcEaqm_IlNyTErH7BPi3_S9y5hBOYlz4JiDJ-3kg1d6SXkQzc1X70ZcsQo-S5Qt_0ogbMy9BpDFPhx_zxm-yI_lkA0SilKSuNXeLstUdEEM1-377RR64hvzQZXSnksyzlTRyULXEeEpkB_Jr1PwCFgU1yX2J7fpbpMqDXDw0KZWRl7nnhegze8jvLKyyU40qB1yih6GIT8Hj5a_Mb_Zo0p4VJtvs-zNG6pwnhJR2PCgvIWji6mw-ICdfzdWcsRFXuwTrJ-nbezAMNkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
گلزنی‌سامان‌قدوس‌ستاره33ساله الاتحاد کلبا دربازی‌امروز این تیم مقابل خورفکان در لیگ امارات؛ در پیش فصل باشگاه پرسپولیس خیلی تلاش کرد که قدوس رو به این‌تیم‌بیاره اما مخالفت همسر او باعث شد که این انتقال انجام نشود. همانند مخالف همسر مونیر الحدادی برای بازگشت…</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/30074" target="_blank">📅 18:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30073">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KEV9YecTYh26O03ljg9VmxxEZy-AOdTf_KoqDKG7JKwa3XAMqhwpHW0k-6jJ5XAOTyOou8BMS6nIKLi_3lB8iyq-_aa0SdxMxSgly9hXzz51Awk5nLoHdePSOjq2e8FrYwwFtZRP_3GOk9fTLbok9v80f4SwMOw2GFPUGDmTli2ti5JHnenC32HvrUaxNvjOcNlLSk8A6FDMtWhkPA7VuZEg22kc8nNjc2eppVzo0Qsci87uaKZdf9jT1F2x6-0t0viAFcivTIWajnQEJ1pY7OcAF2S24ifRauuXGAr7QyEAPrrWHIo9hWTf5WaWWSZJjT9L1sH9uSwrWe1n8FN9yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ دستمزد بشار رسن در پاختاکور سالانه 600 هزاردلار بود. این‌بازیکن در نیم فصل قراردادش به‌پایان‌میرسه و علی‌رغم اینکه پاختاکور دنبال تمدید قراردادشه اما گفته علاقمندم که به تیم پرسپولیس برگردم و اگه باشگاه بخواهد حاضرم مذاکره کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30073" target="_blank">📅 18:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30072">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9989fc3781.mp4?token=bxx2G49g56tLAbL9f5CnudHoyni-Ds6U3nZnFthCL2qa6MCwfuw3Fz2R52UlIhjWnn4Rjeu5iSJWfTb1EfkGALRT061h8cNQFi0ElPMxQnOTv3X5U1j7gPvU_J2IckJMEJU0LXgNFnzqi8N6JZKjACcmRx-RA6SqLLV6SzN_JKI5DSCXuApZb626cgil3_v1aR40Xbvwc96SqKyuYLmlHzP51T1RpuQ6WvQ5Suj7OszcpSkhI_f4tWmuvj60QhLdukvGSQbkk4nYredIrdkk9XKg0aE8MLjRvrc_ot5K-NiS4SrfSmJQvbtxmt93mJEsrxewWy2BMrwUdmxNnKuB_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9989fc3781.mp4?token=bxx2G49g56tLAbL9f5CnudHoyni-Ds6U3nZnFthCL2qa6MCwfuw3Fz2R52UlIhjWnn4Rjeu5iSJWfTb1EfkGALRT061h8cNQFi0ElPMxQnOTv3X5U1j7gPvU_J2IckJMEJU0LXgNFnzqi8N6JZKjACcmRx-RA6SqLLV6SzN_JKI5DSCXuApZb626cgil3_v1aR40Xbvwc96SqKyuYLmlHzP51T1RpuQ6WvQ5Suj7OszcpSkhI_f4tWmuvj60QhLdukvGSQbkk4nYredIrdkk9XKg0aE8MLjRvrc_ot5K-NiS4SrfSmJQvbtxmt93mJEsrxewWy2BMrwUdmxNnKuB_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
نتایج الطلبه و دهوک که تحت هدایت علی رضا منصوریان و گلمحمدی اند در فصل جدید لیگ عراق.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/30072" target="_blank">📅 18:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30071">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q1-dkDT4MZirgZWNXOQmONxAegneRs3NE-GKmVQ3xfyJk8w4pb80B-8CXilGJw4MyH8A8GPxL2WQqGd56xl2QbF-sLFO9qrUFAgmIg3SXTkh0sna3vFjaG2TbOc93DvUTYzh6NzxHdlx4duNu0MzaYGxmGWqrfQJcdvkyrw0f-7hyoaTkCFqLKuARLIf52NvXPsXgKJQnPw6fnP7dGHUv6dNcuRvjanlyI93Sc6--KjJVYDUlv9jKqzrcI1uVM8FFwRwTA6nIa9SpeL_w6ar7CyNfHd_XhPShgu1gaD97X7e1kJyLT7-TL-kA4FAgO5WE-VykLGhH96QNwXXSwvYrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
احسان حاج صفی کاپیتان‌فعلی‌تیم ملی تنها دوبازی برای شکست رکورد بیشترین تعداد بازی در تیم ملی که دست جواد نکونامه فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/30071" target="_blank">📅 18:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30070">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPDry7oI9hYfdgdjYRLUb2Eg0cbgG3YhXL60cMF1vOKhozsTH13wWuNNydk43n_J7dJmhGgi2iCXPFlfrYOGmjeuE0NHsG8VyXEm20Oc0ZoWoX7P8Wd9GSvmHt7RXTXR_-Fl2OqKVK6GjOc5n_-lIYIcaZXKgiA3AE3pRbVmu99eg-mXT04enxUMarxneuCzWr5uq5z45OkbI9GPi1vJgBAvaWGUdTO2fH4K1GYv_8EBhne-9h-nGkSBUpkQFSTBrxp1MpiOfzjQTiJ7Fcry-hJcPz1LtXqA6Mgn2Up9kGyOhsyFGV1FKk6IhxPE431FXmoVXV_s5ZOy7Qr2JP4_qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روشنک مسئول مسابقات لیگ: یه چند روز صبر کنید مشخص می‌شود استقلال قهرمان‌ اعلام‌ میشود یاخیر! احتمالا امسال جام حذفی رو برگذار نکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/30070" target="_blank">📅 18:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30069">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h51wo-afA4wTyslLp4Rnmsrf6UKMGJ1Cqd70lnAOPwO2nFQ8M0ItaMHTRIdqPGgHFnDiKJpnjyoZWWzuDhtvaoaEyyi6vBuz-4cebgmYHy15skSqObzUw_kC3rrQWY5BsUU1Oi4531JJp9jhgKRvUYzMbDaZulOT3sawzyt_UqCJyBUjOOd1u5illbcFkb8hlM8o9qptIvSK6X7g98Rv5pOin6qg3OVWUci5Bw6qzt5HQ4EYblE5ogj6pLcJUGtGC0-nI78o0hBgS9wmvgQbsNNpetYzg11YLbCRF25i_9cRqeRijrJKAtQ_9I8jJ9-KTS5s7GSxEhw-xFkLZZYdsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی Yekbet
💎
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🔔
فرصت ویژه اولین واریز دلاری در یک بت
⭐️
یک واریز
🤩
دو جایزه
🎁
⚠️
یک انتخاب هوشمند، دو هدیه ویژه
تجربه متفاوت با اولین شارژ دلار
ی
🤩
🤩
🤩
فری‌بت ورزشی +
🤩
🤩
فری‌اسپین کازینو
👀
با اولین شارژ حساب از طریق ارز دیجیتال، یوتوپیا ووچر یا پرمیوم ووچر، هر دو جایزه رو دریافت کن
🗓
شرایط استفاده
🤩
⭐️
فری‌بت:شرط میکس حداقل ۲ مسابقه با ضریب حداقل ۱.۸۰ برای هر انتخاب
⭐️
فری‌اسپین:قابل استفاده در بازی Yummy از POPOK
﻿
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
g28
🔗
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30069" target="_blank">📅 18:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30068">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/841d5e76bb.mp4?token=AjXpE6dHnQl-QpwIMvGzAzfFlFxr5VpeIXTcWQ-NEkyTQID4u0WrHACXq7ZB6zDL2E9ab0N0Ed2wAEs-CztHPtbGtPOcETCL69rMEi4js_7RvFC90Ed6fjepmGGYp-dmwYmLfepOcJVYRtvINBLMKdBJzvSVsQpIAzFueq7NcR78xTUz4gXglFwHP-SIbK1mKtwSdo9Fgx8TNMjC_-RKDOOE3rU-RmqtmuG9mrXXHpymg2XKfrTaVqG_z9nafNiJX0dRE9sQlapYd2NCNpl7_HKl-76opwaEMJrCGab6puyQ9PbeHrOikyKT2jxQRqnwNAUoNnA48gMnNQvjIZOt0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/841d5e76bb.mp4?token=AjXpE6dHnQl-QpwIMvGzAzfFlFxr5VpeIXTcWQ-NEkyTQID4u0WrHACXq7ZB6zDL2E9ab0N0Ed2wAEs-CztHPtbGtPOcETCL69rMEi4js_7RvFC90Ed6fjepmGGYp-dmwYmLfepOcJVYRtvINBLMKdBJzvSVsQpIAzFueq7NcR78xTUz4gXglFwHP-SIbK1mKtwSdo9Fgx8TNMjC_-RKDOOE3rU-RmqtmuG9mrXXHpymg2XKfrTaVqG_z9nafNiJX0dRE9sQlapYd2NCNpl7_HKl-76opwaEMJrCGab6puyQ9PbeHrOikyKT2jxQRqnwNAUoNnA48gMnNQvjIZOt0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
عملکرد لژیونرها در رقابت‌های باشگاهی امشب:
🔴
الشمال
2️⃣
-
1️⃣
السیلیه؛ پیروزی‌مهم یاران امید ابراهیمی مقابل حریف خود با گلزنی بغداد بونجاح!
🟡
اتحاد کلبا
1️⃣
-
1️⃣
العین؛توقف‌اتحاد کلبایی‌ها با وجود درخشش ستاره‌های‌ایرانی خود؛ سامان‌قدوس ستاره تیم ملی ایران زمینه‌ساز…</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/30068" target="_blank">📅 17:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30067">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HegY-gP7QG0wbymbQ9AP7jyLCBshCngyiVc5DvURemdt61yb8EIx46XfgQQnrBMo4c3TiWpe2z76dspjZJBomwoVSnZDxeLvDpQCFJP218f_eW5amUYOHPgOSUkkWo29II-xOZP04rGO7sd8kqD3JG_BDk5vLNNqkSipq6TWn7YPP-Y9qcCv9IkM74lZl1JizpAdPAUE46lfSd3MhHsRq4vxnKhHwfp5cYbnZG2PILZukccphqiLSwUFe8HuPoNkpN5bmfG-ElEcdXw2J7HzoWCEkpMoZbU86bX0LDX2JpzgUQlBQqOFYoAr7ZxoFpBRdMFsMJMF4Tg21wEJH4aLAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
🇧🇷
#تکمیلی؛ مدیران باشگاه بارسلونا بزودی مذاکرات خود را برای تمدید قرارداد رافینیا دیاز فوق ستاره برزیلی خود تا سال 2030 آغاز خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/30067" target="_blank">📅 17:47 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30066">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKTTJtZYB1tr6SgjLdcTJ_yYpGBZYljjTQMHxKpVpCJgpQaCk9tVVzsW_9LusLgZWc3e5geHGTWg0HQbUsanrY5L1nrI5a6NZcvvBrf3FqtoR58ilzKBTFT477uXTxjZAlB4JEM3pfZGp4yTt4gSPHDW23C6NCSEDWfebNiWIiqJn3OOoViJHoFh6r3WRFc6NJSEYoz67XxxKi2WIWWa6me9MEiWV9fiKm6Ff7HeS1abvCY_SWwj6KP36uoSqK_Qcjqdc6AzJFxQFfQ8ep0CuBsykZk3-1TXcImh8z41TLAzteBMh6aSWi3v-z6Tb4w2k71GZlb47lhq41yxdKogPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
به مناسبت دعوت دوباره CR7 به پرتغال؛ نگاهی‌بیندازیم به‌عملکرد فوق العاده کریس رونالدو در تیم ملی پرتغال؛ نکته‌جالب اینه که پرتغال تموم افتخاراتش رو با حضور CR7 به دست آورده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/30066" target="_blank">📅 17:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30065">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i_DyNG67KY-11AiqzbbQZnYsJiPx7ss-Q2Um2CYSJJAr1c-DRf6He98o2-OlxVnDyEk2Xq2WLedHhqcJXaGsq8VeQXOCv-KfZwFAOcyQaxOy3gIDGQhIiaWfZwOIm87OuCKDhjRBjYZES3EIKt1RVZYsh0BIX9ERbIVwMwe9cdFeWKD7tJYafyAEbl7Pu11ozdg6dS2VwfRdvYcHINVtfO7G5aYXzzsX2bJtEtyDfbMt_iogqRXdlY58lAZ7RN_6ljF3GIAIeOXQCh87pXxB35ayPI4cRpfEGjh5-HHEj-G-OZSaEv4llrxpLFenwAZ3QKl2XemyeF3yOlo6VgoLrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عملکردفاجعه تاتنهام دی‌زربی در این فصل لیگ جزیره: 5 مسابقه، 3 شکست، 2 مساوی، 0 پیروزی، 8 گل خورده و تنها 2 گل زده در این فصل!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/30065" target="_blank">📅 17:18 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30064">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/am6CfccBkPEG0E5wbx1GMZK7bTh6-3NP1SJKWj5xLeflScLL8BvIhJofRkgKnPvBzrDLs-A5RfszbVsZGgjSEarsWuUZwfKWmfRJ8DRBGH3ZeFCbuyoQxCnjPeyC906IZwYAo_yNoDUe93mBX-EEEFJfit0XljHLya_apsXSreabus5-3yHhUtCzAjniLvV33zCtYkpvLps2fZCWcgtr53LLrEQtj4zlDPLJGUnhHo78BqbmqvQLuTIHB55OtB0iwP3DjTM0Mp1yjB4uE_xyXg8ZoXVXrOJHNUHsnREHzb6M3uFwGgGvcH1clcwN-me4isMl9ZMbEKaQ7aKJXO9LVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی شب گذشته پرشیانا
◽️
مجتبی حسینی سرمربی آلومینیوم با عقد قرار دادی دوساله سرمربی تیم‌نساجی شد. درحالی گفته بودن بافجر امضا کرده گفتیم فقط مذاکرات مثبتی انجام شده که دیشب مالک نساجی پیشنهاد خیلی سنگینی به حسینی داد و مستقیم رفت نساجی.
⚪️
…</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/30064" target="_blank">📅 17:10 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30063">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a224e3381a.mp4?token=GhnfYJRpVIkJC29ZUPGARaXSo0zYdLJBZzcfoRYUntevAmvRKxFjkBPYsm4BN3HvvL23IvsAHBMMlh8E6XRAIPb1CuAGZjCGcQLQ16znPVSXQiwvYlcZCnwxzQcP48Y_dZKYrKhe2I7O6sjE1wy2we8jUgiDQqzjOUP7goHrOtGYI8lWkL1gwsQxO8QcOKz0GbweQgIveSMK1giLEdRZcJOLaZnBf2B3FrRGswI4nnzBa7bKb5Wra9_dEndqi-os_cKHFzNlQfVtgYQD3fPHskh_Rl9X2HrApgZJt5IwhQeP11Sgpz66uYERtzvjj__kAI_lp4gbmLmBaxah616YWzflfJ3tuwLEkIY9OPUYslVOARwlSHQcSDX3g72EJBPOqsdqUUT-9DjeqH4ktGoPMzOCzOe5lJwIe2noE33XStyV8h-VP5ftZ90yI-jjo5fiXSu4Bohdpj8RT2dc-T4XuEbeDaqt4x4AwjkhMnt00Bd2lZaq97RKXmCrsGz0FnADKS-KhPeMNLcH74zdr0_ZWcKynAF5iyl4_xVEWEKtuY_lwU-PDS7Z8HfsztH4-pebd1f5B1nMyLTQoRMO7DmdBLvOfu5K84mQAHe3YeFOSnk6E0U6-AHBSyIPXkS9gtHmaxQxIhrRgRl8fB4YWMTtcHTt-GyIjxTk8drgI-Gj1F4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a224e3381a.mp4?token=GhnfYJRpVIkJC29ZUPGARaXSo0zYdLJBZzcfoRYUntevAmvRKxFjkBPYsm4BN3HvvL23IvsAHBMMlh8E6XRAIPb1CuAGZjCGcQLQ16znPVSXQiwvYlcZCnwxzQcP48Y_dZKYrKhe2I7O6sjE1wy2we8jUgiDQqzjOUP7goHrOtGYI8lWkL1gwsQxO8QcOKz0GbweQgIveSMK1giLEdRZcJOLaZnBf2B3FrRGswI4nnzBa7bKb5Wra9_dEndqi-os_cKHFzNlQfVtgYQD3fPHskh_Rl9X2HrApgZJt5IwhQeP11Sgpz66uYERtzvjj__kAI_lp4gbmLmBaxah616YWzflfJ3tuwLEkIY9OPUYslVOARwlSHQcSDX3g72EJBPOqsdqUUT-9DjeqH4ktGoPMzOCzOe5lJwIe2noE33XStyV8h-VP5ftZ90yI-jjo5fiXSu4Bohdpj8RT2dc-T4XuEbeDaqt4x4AwjkhMnt00Bd2lZaq97RKXmCrsGz0FnADKS-KhPeMNLcH74zdr0_ZWcKynAF5iyl4_xVEWEKtuY_lwU-PDS7Z8HfsztH4-pebd1f5B1nMyLTQoRMO7DmdBLvOfu5K84mQAHe3YeFOSnk6E0U6-AHBSyIPXkS9gtHmaxQxIhrRgRl8fB4YWMTtcHTt-GyIjxTk8drgI-Gj1F4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
لامین‌یامال زیراین ویدیو که یکی از فن پیج هاش گذاشته گفته همین‌کلیپ‌مشخص میکنه که من در حال حاضر بهترین بازیکن جهان هستم و مستحق بردن توپ طلا فوتبال جهان در سال 2026.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30063" target="_blank">📅 16:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30061">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjjo2U-T5OZuafyB_T1lj7PPgqvX-6K47Nk3l0rRDWDVVOoOhZ9hMgyyJzceHfKUvJp-fiYZoG5sOzJGivUSOp0sPmLvmgFxnq2_JgIINbANLXgif66CX6AH8BGSw_SIVrOxNu2wqEXgw_62JcaPGGpj3Nwxd9azC0VKEOodr_3K_qnGzhaWuxSucvVpFjC_Z25Kv2YVeFv9gojOmpjeAe7w2KKhZOPKdnLTNlDYNy3Vb2rqqdIrl1bZCwtOD3Uu_qKyXQ-lWR7HvSoVoutm4zJVwFG8zbj2H-SszwtW8CBlb19zlj7wLlrR296RaxyzIq30gEULCF3YQxY-dfgqcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ باشگاه فولاد برای فروش یوسف مزرعه وینگر جوان این تیم در نقل و انتقالات نیم فصل 150 میلیارد درخواست کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/30061" target="_blank">📅 15:58 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30060">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rD24Drv20c9Bh8zni1mpVJJ18oi78VGzzKVecfiI51c2XjsWpWB7AxQPO86Gw1yhE3ZCX3D7eltytPDEx6SCFsSVL7ETFmdalVnSAP7h2Zuyo9nBQBhxxOzy-pGbB-aGeEVaKXiyiip3Ic73_Y5uHUUrPlECGlgYglslw8-GsSxu-Z15jEtW5Y27-uE54aoeCHZkQlyB--9ji57ALfk3aiFpk2L2U9htGdtkk1oKYj1k8GQ7O5xAkWLTakUmFAq_5Ll_DMVq4xddrE417JSC63jIHkJfYL7m389fatQzN2XC5ret2nDDqmezzbO7oRwQa7bUkCzvbKtLwLz6tGkqKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛طبق‌اخباردریافتی‌پرشیانا؛رقم رضایت نامه عباس کهریزی 20ساله150 میلیاردتومان تعیین شده. حال‌باشگاه پرسپولیس میخواد که با رقم 110 میلیارد رضایت‌نامه کهریزی روقبل از پایان نیم فصل بگیره. کهریزی از استقلال نیز آفر دریافت کرده.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/30060" target="_blank">📅 15:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30059">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TD4MeglYeEPDnz1fhlxh-308z-Ni-lNmMAu8sIPSVUobBVQGkcm8Kfvt4TxMB99naGSoDn_oJ08S8Kzkg9Y_5J8NjW5x5IUfn18pOsbLmhnh7GnAeY3aly4EOoPnE0Gf0ipo8fWZHaBMWF8QUNO8zbqUsWF6NixMYIQF8FeD3nKeT_6PPSaekCGhPgZGY4hEOM1dLKRo4IKRNYdbwdQmZX4pBPlY9pAhPfPTMWPFqR5PwhmzDNWhv7vsXAe4KmVvwvduOXycgDEdXLiaREhnisj5oTv3U1q1Td8kh0fZ78pJ9Q66HyteJEJbFw9esslLET603P8obNI6wjUPE0eL7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
👤
خبرنگارت: بین کریس‌رونالدو
🆚
لیونل مسی انتخاب‌توکدومه؟ مارسلو: کریس‌رونالدو تا ابد. بنظرم بهترین بازیکن تاریخ بدون تعصب کریس رونالدوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30059" target="_blank">📅 15:29 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30058">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tzz5Tz3QpoPGskRucQDlClolcdJkTRWR2gs6BikZRa42Echb1jwwe1SqZC5kNomNPCd_kkJw8cXvi77JHhFsTcBkFX9JhDv20cA9SxwTXbL6D5t6ufyIMKsaq9NvefuRxXDifS_PZz7A9l3HKSSbnVi1Eq_XHv5uNbN6vDpXPKvinEsbnkHFV-dOVo_KTie8CJiEPCy1HPJ7dgSL20gv6UcESzHAbWMhYYscS7QJPL0Iw3xtSGd1cdDVDnnrwMh8G5mdA4PIpCwSS145r4aJdpg_h8YR1tiUnv9WYvyXdGNrLX3S8nU3Bn1auyikUcTdhGGig9IqODbNZ3ACjOitUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه پرسپولیس امروز مدارک جدیدی درباره قرارداد یاسر آسانی به کمیته استیناف ارائه کرده و قراره تا اواسط آبان حکم این کمیته اعلام بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/30058" target="_blank">📅 14:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30057">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q10Jldk-YB8oydlpJK264C55HTHUx3y0y4FM7icJmIaJmX_-ozDBRyUcIqaXgw41pOfQB1ZjkBE5Ad-SCdkx9dux2O25ByyGbkL2fslAo5DJpRiXqcdVrv4qj3Wp_g1M5SsjR1zeYS8oAnmkrQVxwcMH2Ubq7tBWJfVszMMN5xhcraVkBu0B0VXq21RjMmzNWeUvQynrFoAArUuvoXdSKfU93wbGfKtclf-PHUY0B0Paxci6oX-g6IWjN_dJnoNcjeb-QQTqzm22Vi7ol_Ngh-gcIIcGLR2-zxC6TOBN0V6iOmSx9rQ8wqgddPmCYebbo6lct_5EKTbQuA5J8pw5rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بیانیه‌رسمی‌کمیته‌انضباطی‌درباره شکایت باشگاه پرسپولیس از یاسر آسانی و رد شدن این شکایت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30057" target="_blank">📅 14:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30056">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K4jefzURIj7GGpFuN4Zp7GeW0cmPEBA9nfhpobMuimpCnvimLbUdKcsp9PIsaww-iJlFWNKuc0KKV2Ppibq4gHuIZ6SrsYBH9WW690vZfZCTlRwFvgFVv_KBMbnppDQfv9bEnYzrkCpJimMOHRVH6tomQHZ603UuURA5oJBT3KJNcSBO0fXPlNFOSDlbuqOMvM5z0BNdtiN0mossZtdc2hLHrNW2uIB_XQIiAaYVfK_SoK1OEs0jA1WsO2zWV4Juh9cRW4qSycj-cRastbF0-QBmNQ0UOYXcGiy8vZVjodqzzLIOFNCAAwHRAR_hxSdQt9WSJgocbtFrr_2xPmJwQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛مهدی‌تارتار سرمربی پرسپولیس در دوهفته‌اخیر بارها به مدیریت این باشگاه اعلام کرده بود بین امیر جعفری مدافع چپ گل گهر و ابوذر صفر زاده یکی رو جذب کنند که انتقال جعفری حدود 100 میلیارد تومان برای سرخ‌ها هزینه در برخواهد داشت اما انتقال صفرزاده به شکل…</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/30056" target="_blank">📅 14:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30055">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
🇫🇷
در پایان بازی شب گذشته بایرن مونیخ که با هتریک مایکل اولیسه همراه شد بعد بازی ستاره فرانسوی باواریایی‌ها حسابی سورپرایز شد. نیمارجونیور کیت‌خودش رو برای اولیسه فرستاد و باعث‌شد‌ بالاخره اون هم یه بخندی بزنه و چند جمله‌ای با خبرنگار صحبت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30055" target="_blank">📅 13:52 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30054">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/la4nV6_TYhaUVz6TykqgsYX4yVjnDAhrAuPIhOozI7G6yP1VlHSZFufi07MEFipjUlhIFatwo4MHN8X3f9dp88BUsyM-RSkebqsFD2H9ELsxuX3ALSoM3618bAxfKY0cpldwqZJmLCh-T_kuw_gmi8o64o5dhLoFZfhXW-xzedwKN0lVLQEwy1kuFxwVGpor0CATN1sYosQ600sIeOP1KzHQooMbOZvKHbhVm-P-R_c5HuLUzy1b7hJcbBW4oeCbNjddY93a5wpJKYQKS3lqR39kxcedueY9BqZt4mjA4ca4qha4C2lhzweEoDi7eKMKgoEzApZVrc-LGacYxHQyfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇳🇱
وسلی اسنایدر سه گنجینه گرانبها از تاریخ حضورش در تیم هلند را برای مزایده گذاشت! توپ نقره‌ای جام جهانی ۲۰۱۰؛ مدال رتبه سوم سال ۲۰۱۴؛ توپ بازی هلند-برزیل درمرحله‌یک‌چهارم نهایی ۲۰۱۰
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30054" target="_blank">📅 13:28 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30052">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/knTyEQYxsPA-BL3qCH2gCcj0rSa7slQ9-Hqrfe9cz5kxm3QM5ea1DEF37NYoqVaGX7Q0MnrO6cGR2LJ8GDMFFTgyNRuOAhJNpcpF48BzmKzWA9t-dwMd7E0uQ9ancROQWD3GFPYfgonumqfg9smsXuF35jVkA_4gsdrLlzclQ3mvdlnqhzg3LqxV2ijzUlYSGrTYP-3J4pNnTWzrWww5bZtiYLWtz8FvUIJ0yeu7yuq5-XjyMnQzs5-ml6kLGKPHrrMOgjlhIwWVIRgqOx1S2raV4eOG13gHt_swXn65yqMtSbButrKcD1JE984GJsSlLfkJKEp3i_7MbsaCH2c_XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df5ef3d951.mp4?token=S10-jjuClmosEvupTUBPi0MTzNTAmEDQ0N2_OJ1396PpN3it-yRschc2VEFJp0FmFV1RlgcAzNE00l6TkCavYyQM4ln185Y4EKM1fjz-kBgkynSPrnj36JHtuL8eREgpZcpxDT3aVxhYHZCHVw_O7_MowtYJ9ga2flf3WOEQSk9ruL8TdKVScBVM1uzRhOA_gTQvQzDRCBB8saHOaLV563pCDCA8Or1wm4Rujcy6tNxfrwm2XWPALCs61gsFSfu0cRhmvaWbTWeCa49_S3tdVNvI_BwMZqtudBjZCYKGiPfypX55vVSPk7TsU06LdGWdQkaMPJYj13rAMsTZXJJLsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df5ef3d951.mp4?token=S10-jjuClmosEvupTUBPi0MTzNTAmEDQ0N2_OJ1396PpN3it-yRschc2VEFJp0FmFV1RlgcAzNE00l6TkCavYyQM4ln185Y4EKM1fjz-kBgkynSPrnj36JHtuL8eREgpZcpxDT3aVxhYHZCHVw_O7_MowtYJ9ga2flf3WOEQSk9ruL8TdKVScBVM1uzRhOA_gTQvQzDRCBB8saHOaLV563pCDCA8Or1wm4Rujcy6tNxfrwm2XWPALCs61gsFSfu0cRhmvaWbTWeCa49_S3tdVNvI_BwMZqtudBjZCYKGiPfypX55vVSPk7TsU06LdGWdQkaMPJYj13rAMsTZXJJLsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🇫🇷
در پایان بازی شب گذشته بایرن مونیخ که با هتریک مایکل اولیسه همراه شد بعد بازی ستاره فرانسوی باواریایی‌ها حسابی سورپرایز شد. نیمارجونیور کیت‌خودش رو برای اولیسه فرستاد و باعث‌شد‌ بالاخره اون هم یه بخندی بزنه و چند جمله‌ای با خبرنگار صحبت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30052" target="_blank">📅 13:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30051">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LU-v5WtHQX4qmufJy5OUHGNwE5dl17Hp29FWE3DOqg-GNEImC6tZkipreLTLX_kZj4FTEFzI5XS_pQBdO7_mDRX7yWU33Ska-0MJczUnV3mBy4oaUpQMspl3t8hoJ2v-rOLvKmdn6CmtQDbq5XU3AEqahNbsFME9IFJkiu1mu_BRhtzxpN60tqjxJWXRhgqZezNaZ54x7J5D0lueYWpMzy17nZI7JmtkGhsHOFWxz-Ieh-W3CjR1zIywq7HDcMCXIMHSCnXnK3m9FFm0Q89diSiDlsSZL36QjZDwW9j67rJjg-snL4hKm4LKbetzPdo1_KLAwwMCy1axDCNq6KUVkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
هایلایتی‌ازعملکرددرخشان کریم آدیمی وینگر فوق‌العاده سرعتی‌ بارسا باپیراهن این‌تیم؛ آبی‌اناری‌ها برای جذب آدیمی تنها 20 میلیون یورو هزینه کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30051" target="_blank">📅 12:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30050">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6111cc9977.mp4?token=n0CS4g4PJNAildbYXHVGuUtqnjqDsw4U0gY1fqaC4n1T5Tn16f1_jdlEPsWKynQU8ZWF2ngvX1XBcmg7AwuyYtOXfd-zua60hmo6HuWkPVdIXipVTiCMSUkvX9k3d6skKY3qWQVG21K1R_FBpA1VlKz7Ckjk78ftfJ05EZYVH9EKP1aTc5_ZsauZq2oMQ-krrKi1l58FpmoE8M2MJQbz2qWyYmMDKZoyDVQyKWpER4UUEiMvCzMQRqldKu-zQ1jJd_ZZDmMIDu8nZXqAxEt34W26U4kmpu5dn3Zts2J2winqclcOczwZROZBAQ8aI9u6IxVcdgYVNBsQEZvfvt6YLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6111cc9977.mp4?token=n0CS4g4PJNAildbYXHVGuUtqnjqDsw4U0gY1fqaC4n1T5Tn16f1_jdlEPsWKynQU8ZWF2ngvX1XBcmg7AwuyYtOXfd-zua60hmo6HuWkPVdIXipVTiCMSUkvX9k3d6skKY3qWQVG21K1R_FBpA1VlKz7Ckjk78ftfJ05EZYVH9EKP1aTc5_ZsauZq2oMQ-krrKi1l58FpmoE8M2MJQbz2qWyYmMDKZoyDVQyKWpER4UUEiMvCzMQRqldKu-zQ1jJd_ZZDmMIDu8nZXqAxEt34W26U4kmpu5dn3Zts2J2winqclcOczwZROZBAQ8aI9u6IxVcdgYVNBsQEZvfvt6YLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟢
سوپرگل‌دیدنی‌فرانسیسکو ترینکائو ستاره الاهلی بعنوان بهترین گل هفته لیگ عربستان انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30050" target="_blank">📅 12:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30049">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N55w79VjHARX_Bu4cy9iAWZIMQHYI9Aj6O2k2kdsMX0vDDenAMTyf05TFWSoarddRPZG3ZF4ILMOqTpOFNaX7lkxjkpv7oskQyK_3u7p4rYYLBCIhxjPNedhsPSn6HTU1GdJKEvm2nQIGouZHG7Qu-0KdbTF4SA3KXPpK2SHuanRWiBAcA8PFQGnX6RlGlSIzcbsZ2iPkMU-a4AAyDboYWcxhdwP5lkIHigcUO4u4bzHygNGZigEHi74KsYtxJDsDlZvTrzOlyrxAMoDQ-gdNItC6ylPQOwY3LPSylQBy1Vn6qMhd-E-xixiNsGhT8wl7Pbm6NJw3G569C6WTk89Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آندرانیک تیموریان دستیار قلعه نویی در تیم ملی بعد از سه سال کار با او از کادرفنی تیم ملی جدا شد.
طبق شنیده‌ های پرشیانا؛ در صورت موافقت سهراب بختیاری زاده آندو به کادر استقلال اضافه میشود‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/30049" target="_blank">📅 11:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30048">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eTPEERFg8vVso9EFbUhdxBBUMKAfHdaHxZ0YKEe8OFql3Zt3K17wPGrWl8miQ2HtNtuvzf41VbPo6ko3vp9p3vcPO3o5GJTtK-OIrJl_HqXxlqIut8d65BWvTLmH_TFB8zYBmjMhXBZZrbzSewPVQm15PCG__6x9j6C2TsuTR2tVfHpy3gQLoAx3XCVIXskFTaI-c8kwTutnyG2WwVOu80XSaofoJHOmMPurI4B__fB56H22S_QOcii6Ne0I8VyGWpKSHs5mF4cRlhSOUL-OQtSD_zynaOToWxoKZKq2f88q2aRNJ-_kL071PMKIv0KaKPEZHIxkgZz29zBdZ1TGJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توییت جالب یونیون برلین بعدِ گل هفتم بایرن؛ کاش این پسر 19 ساله بارسلونا دهنشو ببنده! کین و اولیسه امروز واقعاً روی فرم هستن و ثابت کردن که شایستگی قرار گرفتن تو جمع مدعیان توپ طلا رو دارن. واکنش اکانت بایرن مونیخ هم ببینید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/30048" target="_blank">📅 11:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30047">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i5hvRZJ3pg2b6WOSsH0zTJ3jLTccF-1GIlm_BcifhGhvBMfo3-_xUrw_DH-AtsbQ9eP8ucUMfT1h8OXaOzaWV_iW3MJ515hmEk7M3IYS3a7Rtr2oUENnDRIafN75xb7Cqjw6tHH2eER4zGCyQiLD8J7DwH58ZVxJmmBAP19191zBmqCBwYBmTlkK4yWywzdX1dwb1mU14XZ-5hCNg2EjJZQwfluxbZB8d3mGRVTa9jgXjMrGRncru7ihISMwqcNUEbDmjIqogHdzhly-k_XIkIr8fUDUSAl7ZH6n5yWcdjmESgbx1sjC-u23NcpjECajyco-Jz3ANUUrWDA0guEhdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
یه فلش‌بک بزنیم به زمانی که ژوزه مورینیو سرمربی‌پرتغالی‌رئال‌مادرید برای اینکه خشونت بازی پپه را کم بکنه. فرستادش با تیم زنان تمرین کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30047" target="_blank">📅 11:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30046">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aG5fe_gKBwxJKYa3QZpiXtbnooLgDNETDVrU8GdB0fdrKiOIVeeDqdhzpLZEpBzfu01X2xzxFEsvPi4V5xJmOFIASIGnKWiki000RZo4DVAuIYBqpSKzw7OtQ4hN9WaDuRXdFc9ZB8sI11O9VWDk5ZtzoelV3nvqMLSRRyZ6EsVQFTSVrSvxtkG12g5-H1fQSYpEP5ylDMul_jGzL5T1_Ro4-9Fja0dVsBxgt4KahjbMyzL_m5rIGj4q6QyaUFlN0Dc8VjnfrDdDllU3MWJtBadHtGdnpedfAz9ZKFLW1WCxRN10pFpiFUAB_kx4AzTmdFuzu_k4KL1tmHSbONAKdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کری سنگین مارسلو ستاره سابق رئال مادرید: خودم به تنهایی اندازه بارسلونا، چمپیونزلیگ دارم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/30046" target="_blank">📅 10:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30045">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1e-yUdtsJypbPezcHb4hvhSq1R28l9ibakFn0xwJ3HAIt8lWmDUfBGFguXq_oskMwUEieoXtcWRFsERei9U4NAmlPJdxBvjNWzF0Yb0p0zVVDKEUPiIPiu0vabh-L0YNYMt1GV9wkByFWacxisJjaVA5vlQSoKjGiZ23qV7B9eWaooqhKLC29lGLH7rCgsrg8PbIu6R9CxWHWdF25n1OHMxFgY_7jL0ayGaJ3zHMIHQl42I1dfEaz68f0LHmq-74zpd6Sa3BRAjHJM92dhPmTfxmpTgzNIIlLCJkJ-6GYczZIq37Owo-X6tZhF6yKB2jBjsgqv2_sHlYmesx9n3jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌تعدادفصل‌های‌الکس‌فرگوسن و لئو مسی برای رسیدن به 49 جام در کل دوران حرفه‌ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30045" target="_blank">📅 10:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30043">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83a5244f7f.mp4?token=dVjH0yzXULoBU9JKoBobhKw0gsQdjXpQCXkI5tVOK7p0bMLTZWY-Qy7LiWUqtQ5u72-MfqT7tH46t16kJcMEe8zqQCd619QwNc43zYY50rqYlTYEEcAmUPz3eWIQahR3Rp8RyaSnvh322vAtvQfny8BjZ0a3us0DOiCrRUuEZU-Bo-xpGYJQ4yJxowpupXsR186RpKjieICtBV5R5YqErQUhfk2YWOfy4__em7in8F50RnGzl8sj3Uc_ZCAieGFEVMeclUrL9L3Xr-CBGb5mqVpZSM9aXCT175imEycc6bhjFDwbQT8oC33hWEFtJlAtJ2KVkCtS4isbh6k-7zmwkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83a5244f7f.mp4?token=dVjH0yzXULoBU9JKoBobhKw0gsQdjXpQCXkI5tVOK7p0bMLTZWY-Qy7LiWUqtQ5u72-MfqT7tH46t16kJcMEe8zqQCd619QwNc43zYY50rqYlTYEEcAmUPz3eWIQahR3Rp8RyaSnvh322vAtvQfny8BjZ0a3us0DOiCrRUuEZU-Bo-xpGYJQ4yJxowpupXsR186RpKjieICtBV5R5YqErQUhfk2YWOfy4__em7in8F50RnGzl8sj3Uc_ZCAieGFEVMeclUrL9L3Xr-CBGb5mqVpZSM9aXCT175imEycc6bhjFDwbQT8oC33hWEFtJlAtJ2KVkCtS4isbh6k-7zmwkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اولین واکنش امید عالیشاه به فحاشی ناموسی خداداد: وقتی گوش دادم. دچار شرم نیابتی شدم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/30043" target="_blank">📅 10:39 · 28 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
