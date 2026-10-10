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
<img src="https://cdn4.telesco.pe/file/Max4xZCaw2eu5CrsAEMtDcsIFEwbGh2jBREciEy66DkSj-2aBeNQqpcHuIcrS2VtjgqtT6BxfwJF3gPv20BVVNF-9HOiibPYeBaTWT29bsXmVl_ukHSCcTac0DCz0zWiQ6s1-Per4TVXbO0SawLoN_L2O_fvy1_WLKQiut8cE0JHPNvqyU6aRoz12InSxvVmcOo4TAXcsRJ9LRN-A6qWHdGJsS2mRJViFO9fs_obcGZlqV7yXdmWLYcQ-E4DpAJTBi5WIptMK9CNVVFAPgQNjBsv-xvQUXI0Gxi4EsYQrQ-6Lo6t5aa_W0dz7Wimk55u0hy61tdSvpo9RAeFI99ewg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 104K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-18 21:02:44</div>
<hr>

<div class="tg-post" id="msg-73070">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2bf843dd2a.mp4?token=WmfNCHslyN7Qz9N4tgU-tsvL9lvRnxpHm4nv4urux2YtzrzE0SVAQp5o8SLkH2_LPCflQGgaCEYfQ_Up4qouIv8TmhzDliKF-fwYK9Va1eUUXmmYtS4bc6HWzu8h1R2vB-WJ-ux0Ucx9-yyQKNoTnumDOHQfiAqAZh_nP4voS349Q89v2ps5DfStUwuHWZMluu7XWTCABlwfwVRq7Ij7EJVdaDbPwaCBPDlyOkbYbNub4jZfU25TSseozglAdSHT-YiY98HGAC6J-9xQBlWfc0r3HqKED7HhmFGmuYPogcybXmGBa5lzQ7VlmlGQXz8s9kA5tGJP6n4Czeil77_2pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2bf843dd2a.mp4?token=WmfNCHslyN7Qz9N4tgU-tsvL9lvRnxpHm4nv4urux2YtzrzE0SVAQp5o8SLkH2_LPCflQGgaCEYfQ_Up4qouIv8TmhzDliKF-fwYK9Va1eUUXmmYtS4bc6HWzu8h1R2vB-WJ-ux0Ucx9-yyQKNoTnumDOHQfiAqAZh_nP4voS349Q89v2ps5DfStUwuHWZMluu7XWTCABlwfwVRq7Ij7EJVdaDbPwaCBPDlyOkbYbNub4jZfU25TSseozglAdSHT-YiY98HGAC6J-9xQBlWfc0r3HqKED7HhmFGmuYPogcybXmGBa5lzQ7VlmlGQXz8s9kA5tGJP6n4Czeil77_2pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه تصاویری از آتش‌سوزی گسترده و نشت نفت از یک نفتکش منتشر کرده که به گفته این نیرو، بر اثر برخورد با مین دریایی در تنگه هرمز آسیب دیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 888 · <a href="https://t.me/news_hut/73070" target="_blank">📅 21:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73069">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3875ef3f4f.mp4?token=fJhMP5n7bk9K_RAXPgEe62UrpqSTRb6hLFObDvAtpQVjroFv2GSO0bOdbSGjILiF-hCpdUffdIzZOB7PB5Kjjf98dIygDpJhWgNmlw33THmu6ti8DE67HVQLVBd3O4H813Y15L6znFNVhbUmdZGplZDqbNSygZrBCDK3hp5ZR11wPcNvdlV_KvxpKcpxvkUMVRoGYAtMWxQniEIlc3oWGKD11tn3j6kGHisy4I5kcKh1nXrpv_o0wuPqCeZhIzoAfL-YzajDplCpdvkUEYfi-kvsDKU-pEjgsaacW2jzVTuFYMIiP7hm2KZl0u0h6c4ETPwmzedu74EfnOZhRztQGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3875ef3f4f.mp4?token=fJhMP5n7bk9K_RAXPgEe62UrpqSTRb6hLFObDvAtpQVjroFv2GSO0bOdbSGjILiF-hCpdUffdIzZOB7PB5Kjjf98dIygDpJhWgNmlw33THmu6ti8DE67HVQLVBd3O4H813Y15L6znFNVhbUmdZGplZDqbNSygZrBCDK3hp5ZR11wPcNvdlV_KvxpKcpxvkUMVRoGYAtMWxQniEIlc3oWGKD11tn3j6kGHisy4I5kcKh1nXrpv_o0wuPqCeZhIzoAfL-YzajDplCpdvkUEYfi-kvsDKU-pEjgsaacW2jzVTuFYMIiP7hm2KZl0u0h6c4ETPwmzedu74EfnOZhRztQGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: شما گفته بودید تا بعد از انتخابات میان‌دوره‌ای به ایران حمله نمی‌کنید. حمله اخیر در عربستان باعث شده نظرتون عوض بشه؟
ترامپ: «بررسیش می‌کنیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/news_hut/73069" target="_blank">📅 20:58 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73068">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ba9c18ae3.mp4?token=sV2erhyZ1ZYbduww1A3mp-4JOYG3XTGUzk9HtoLuX9wArqLn9GbJrYAwbtxSE7EA3HlS7Jb5rUhUItw72jvjKn1JBnuxn75vDVWugs3nwPTq9oimdBKiGd2FkB53VjHxHQn3kk2-MimQ4pc6iTHogs3BVfA0k4Xxr8f0RB5oJ04r-m3gwDVQv_Bm9VsfO5nP-RAnv9wZyfO77LXCpb6F9p24GLGLOgeRJ__mCc9m3rou9Ee-5ViBSRNTVHKOmUMW0Mivbsvi673Mn_4UZCmW42q2lpPTxVHRYfBBMuX9Q1kmiFm8o9ZqeDxNB3i8lK8_afbEQ0-DMLy4fVOhLs69vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ba9c18ae3.mp4?token=sV2erhyZ1ZYbduww1A3mp-4JOYG3XTGUzk9HtoLuX9wArqLn9GbJrYAwbtxSE7EA3HlS7Jb5rUhUItw72jvjKn1JBnuxn75vDVWugs3nwPTq9oimdBKiGd2FkB53VjHxHQn3kk2-MimQ4pc6iTHogs3BVfA0k4Xxr8f0RB5oJ04r-m3gwDVQv_Bm9VsfO5nP-RAnv9wZyfO77LXCpb6F9p24GLGLOgeRJ__mCc9m3rou9Ee-5ViBSRNTVHKOmUMW0Mivbsvi673Mn_4UZCmW42q2lpPTxVHRYfBBMuX9Q1kmiFm8o9ZqeDxNB3i8lK8_afbEQ0-DMLy4fVOhLs69vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در ویدیویی جدید که در تیک‌تاک منتشر کرده، در حال ورزش کردن در باشگاه دیده می‌شه.
@News_Hut</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/news_hut/73068" target="_blank">📅 20:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73067">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f89266c981.mp4?token=A7vNA1rpT1oqfMxSLvchlIKEE6C3mdNmbTd6Wmri2a2LdtUhbLrkkQfDdDDJxv7mwFcKtGeUNEdW0ksUd9nrmL4ff90QTkPkdb9TRKQra81L2KlNXCxMrDYxnqsKAAL6_ahtAxcqBrxrBHX3t7zSxaCu9P1rDN70oJdwpnAcujXAZ3P7ZCNieZK3UW6KdOddyYygpXo6Ci8n6kATmPlv5bo1FHvCWTaQB5usgFrFV3oFvNhuLv7qInS8dRnCALkGq9WyuC0zA07mDEVtmQ6iLm6CMk15wBB4ZBHvbukQKvLMM-LzMQzoSSjirtkywU7KuDnqfPp230kSbWjcglQVWYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f89266c981.mp4?token=A7vNA1rpT1oqfMxSLvchlIKEE6C3mdNmbTd6Wmri2a2LdtUhbLrkkQfDdDDJxv7mwFcKtGeUNEdW0ksUd9nrmL4ff90QTkPkdb9TRKQra81L2KlNXCxMrDYxnqsKAAL6_ahtAxcqBrxrBHX3t7zSxaCu9P1rDN70oJdwpnAcujXAZ3P7ZCNieZK3UW6KdOddyYygpXo6Ci8n6kATmPlv5bo1FHvCWTaQB5usgFrFV3oFvNhuLv7qInS8dRnCALkGq9WyuC0zA07mDEVtmQ6iLm6CMk15wBB4ZBHvbukQKvLMM-LzMQzoSSjirtkywU7KuDnqfPp230kSbWjcglQVWYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رائفی‌پور: آمریکا را پایین کشیدن کاری ندارد.روسیه باید پالایشگاه‌های آمریکا را هدف بگیرد تا حملات اوکراین متوقف شود.
@News_Hut</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/news_hut/73067" target="_blank">📅 20:02 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73066">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gmc9qyr64tkq-eAgpYoVYDocsLsSSq2qOLYPlY-ueQUel2iesLr3GtegyMBZ49bhNYpGSbJmMBydE1ZnSVSTQJYDRVj1K8knGSbfEn5RtgzzauqR5bO2rhjOcwhw3VQKJSyyZOZhxAZfgBGUZnAjmFUn4ED7zuMZz4Nb3_xyjSncNUAnFWPL3YLSlKldv6mY4eGjiO2LHjDjQSJ3tpcGBouEX8FP6kZolptVr1n707Mipry6caTFOHfIg1owEmqP1adiKPY0K4SUlZHITn63JLM06QciQmnRwdpJvNaJrpt_6HJay2lYo_fYPnA6ldpQT91yz4s0TI5aZb9RTgzJXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین محموله گازوئیل روسیه به مقصد آمریکا حرکت کرد؛ قبل از اعلام توافق ترامپ!
اولین محموله گازوئیل روسیه که راهی آمریکاست، ۲۲ سپتامبر از بندر سن‌پترزبورگ حرکت کرده؛ یعنی دو هفته قبل از اینکه ترامپ توافق رو اعلام کنه.
این نفتکش یونانی با نام MINERVA ZEN حدود ۲۷۵ هزار بشکه گازوئیل حمل می‌کنه و پیش‌بینی می‌شه ۱۱ یا ۱۲ اکتبر به سواحل شرقی آمریکا برسه.
تحلیلگران می‌گن حجم این محموله‌ها در مقایسه با مصرف گازوئیل و سایر سوخت‌های تقطیری آمریکا، فقط برای چند روز کافیه. از طرفی، حملات اوکراین به پالایشگاه‌های روسیه هم باعث کاهش تولید گازوئیل این کشور شده.
@News_Hut
| Clash Report</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/news_hut/73066" target="_blank">📅 19:21 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73065">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3e4a880ec.mp4?token=VE1k6ra7PSe9kA1VDXN6BfG-bYdh8UTcCDAwqIrPKrbH_bbv3rDAFm70hMhTMDCBEpTxmjDT3z4Ns12a1pwMtzLr_OBCplQOqBVO0xWr_vXCdHpeg7ipp6TOCQh9qdCHmUrlZNTfXpkTsZb4Ap1GxltrXr6Suvvusy9fEqYH_HdKgGUZJwny7SGTWk3TI9LRF88m3Vo9M1jQiaV29x3NzoV8QQ1IRLPVbBxA5AM8vCHQLzXbupJkl5FvUayP4gFkQpAsaymtvab-W0Txn-jnTTP7LIYVFaaetWtguSRMaKLYJeeKAHnY8gmPaqTggIXcpGHMzSo5_xh0ZwsNe9M58Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3e4a880ec.mp4?token=VE1k6ra7PSe9kA1VDXN6BfG-bYdh8UTcCDAwqIrPKrbH_bbv3rDAFm70hMhTMDCBEpTxmjDT3z4Ns12a1pwMtzLr_OBCplQOqBVO0xWr_vXCdHpeg7ipp6TOCQh9qdCHmUrlZNTfXpkTsZb4Ap1GxltrXr6Suvvusy9fEqYH_HdKgGUZJwny7SGTWk3TI9LRF88m3Vo9M1jQiaV29x3NzoV8QQ1IRLPVbBxA5AM8vCHQLzXbupJkl5FvUayP4gFkQpAsaymtvab-W0Txn-jnTTP7LIYVFaaetWtguSRMaKLYJeeKAHnY8gmPaqTggIXcpGHMzSo5_xh0ZwsNe9M58Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در جریان اجرای ارکسترال «آرش» در سالن اسپیناس تهران، در شامگاه جمعه ۱۷ مهر، تماشاگران در واکنش به صحبت‌های اسماعیل بقایی، سخنگوی وزارت امور خارجه جمهوری اسلامی، او را هو کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/news_hut/73065" target="_blank">📅 19:14 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73064">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">برآوردهای اولیه از تلفات حمله به فرودگاه ریاض:
بر اساس برآوردهای فعلی، در پی اصابت یک تا دو موشک بالستیک انصارالله به ترمینال ۳ فرودگاه بین‌المللی ملک خالد در ریاض:
مجروحان: حدود ۴۰ تا ۷۰ نفر
کشته‌شدگان: حدود ۳ تا ۵ نفر
این آمار در حد برآورد اولیه است و هنوز تأیید رسمی آن مشخص نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/news_hut/73064" target="_blank">📅 18:26 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73062">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23f8abc61b.mp4?token=kbIatt-86O2qcSzykFr9rxi1KdQQfudQ5-dPTT5WP418JYH14yK9U2kXNg8rXI_rSbYXr3I13rpxbt205mftEfGu-iTPJrHEQ_H1IeyzhJ20cflNnH62GC21kkMyVK1opBmuckBT-hg36hIv-Vjs964HyCb2TaHofHiTBTDfIhkRUgXWi3-06pf7T4Q-97PHf3rtxga4zLqy-qi-XJjYdx2zNMz6-WAMLJJbt38hUTw7ZPZHp9P8tr0UH7hiThprWzEzQTN3St0mcrr2ilVirk67r_MV3Ki9vE2WNQp-VBLdxG0NOXBlf3H85mDgrOX-hC2G1a-pF46luj0KHPI36g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23f8abc61b.mp4?token=kbIatt-86O2qcSzykFr9rxi1KdQQfudQ5-dPTT5WP418JYH14yK9U2kXNg8rXI_rSbYXr3I13rpxbt205mftEfGu-iTPJrHEQ_H1IeyzhJ20cflNnH62GC21kkMyVK1opBmuckBT-hg36hIv-Vjs964HyCb2TaHofHiTBTDfIhkRUgXWi3-06pf7T4Q-97PHf3rtxga4zLqy-qi-XJjYdx2zNMz6-WAMLJJbt38hUTw7ZPZHp9P8tr0UH7hiThprWzEzQTN3St0mcrr2ilVirk67r_MV3Ki9vE2WNQp-VBLdxG0NOXBlf3H85mDgrOX-hC2G1a-pF46luj0KHPI36g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از فرودگاه بین‌المللی ملک خالد در ریاض پس از حمله منتسب به حوثی‌ها (انصارالله)
در این تصاویر، آثار خون روی زمین دیده می‌شه و نیروهای امدادی گسترده‌ای در محل حضور دارن.
@News_Hut</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/news_hut/73062" target="_blank">📅 18:21 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73061">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">گزارش‌ها از وقوع حادثه‌ای بزرگ در فرودگاه ریاض؛
گزارش‌ها حاکی از وقوع حادثه‌ای جدی در فرودگاه بین‌المللی ملک خالد در ریاضه. احتمال داده می‌شه یک موشک بالستیک حوثی‌ها (انصارالله) به این فرودگاه اصابت کرده باشه.
تعداد زیادی از نیروهای امدادی و اورژانسی به محل حادثه اعزام شدن.
@News_Hut</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/73061" target="_blank">📅 18:18 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73060">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">#فوری
؛ خبرگزاری فرانسه (AFP):
خبرگزاری فرانسه به نقل از سه شاهد عینی گزارش داده که در حال تخلیه افراد از فرودگاه بین‌المللی ملک خالد در ریاض، پایتخت عربستان سعودی، هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/73060" target="_blank">📅 18:16 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73059">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc0bb8954.mp4?token=O6LF9Wcrlz3N9M9yAZNWIMA_yd1m1F1aptoNrcf5xJMmLy2kuGg-49dQecyo_VFdZh6Z5oEZbfCNLl_kxXO_jWcNkvn9_CHd60aNUIXllFr543GyjmVgLWgjqg7HNGS5Plx175dUY0FPZO2EHV-axOErf8zMVgUOvwz8e2o74u3tPAS6BwfhhP9IS3LA1DNsPLMwdQRYSq-TgLT4HodCrAGUbcNLoJruDO1ZGT29sY-1Fu8aLb-kL0O4pVmmsYuV-INOUACPDyss1qDJonBa_hLUzzcnTwF-z9WuLpAEDJcVI0BkpdFJuZF-i3rZpavSxhO2a8zOMpAJHuPjg_UMgXhWhMVGv1QXIUatf-LlCkNb-Qq0A4G8ArzNDQpwCcWWOiTwjP_mleIwX7MDHvnjhoT_HSOm9Ey3N4nmIhs77lv9_TO-lwvvhAq-Oc6QPauvlJ3glJYVR-_659xx0nFYs6Kd6iPVf1WnqFho32Se9drdSsHIz1deYm0Kqv-1TKov9LOyYul0HeZ_KpJxP2BaXRDh0SnN_BnuGIOISCDUt7o18EY_rTvRQv687I22tFyzeSvDap6EYfChPWcjwQNNnibF4Xn6IJJ9xAjyWH9V5vLo7t_aBNU-H_wS3zThL6Tg6D-IJCivUWx1jWda38njJ7ws1SJm-Hvts28FG9CdsKI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc0bb8954.mp4?token=O6LF9Wcrlz3N9M9yAZNWIMA_yd1m1F1aptoNrcf5xJMmLy2kuGg-49dQecyo_VFdZh6Z5oEZbfCNLl_kxXO_jWcNkvn9_CHd60aNUIXllFr543GyjmVgLWgjqg7HNGS5Plx175dUY0FPZO2EHV-axOErf8zMVgUOvwz8e2o74u3tPAS6BwfhhP9IS3LA1DNsPLMwdQRYSq-TgLT4HodCrAGUbcNLoJruDO1ZGT29sY-1Fu8aLb-kL0O4pVmmsYuV-INOUACPDyss1qDJonBa_hLUzzcnTwF-z9WuLpAEDJcVI0BkpdFJuZF-i3rZpavSxhO2a8zOMpAJHuPjg_UMgXhWhMVGv1QXIUatf-LlCkNb-Qq0A4G8ArzNDQpwCcWWOiTwjP_mleIwX7MDHvnjhoT_HSOm9Ey3N4nmIhs77lv9_TO-lwvvhAq-Oc6QPauvlJ3glJYVR-_659xx0nFYs6Kd6iPVf1WnqFho32Se9drdSsHIz1deYm0Kqv-1TKov9LOyYul0HeZ_KpJxP2BaXRDh0SnN_BnuGIOISCDUt7o18EY_rTvRQv687I22tFyzeSvDap6EYfChPWcjwQNNnibF4Xn6IJJ9xAjyWH9V5vLo7t_aBNU-H_wS3zThL6Tg6D-IJCivUWx1jWda38njJ7ws1SJm-Hvts28FG9CdsKI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ملکه تایلند برای نخستین بار به تنهایی هدایت یک جنگنده گریپن سوئدی رو بر عهده گرفت و پس از فرود موفق، از پادشاه مدال دریافت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/73059" target="_blank">📅 18:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73058">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73058" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/news_hut/73058" target="_blank">📅 18:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73057">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/btxcEOtKHmb8OvvbQxh8eNScT5YxIGCOcJ5xzGR3edgNfkPJ2g0lbGgU9gt6f2VX-cKNjJWIo19WG01SpZFKssdCX3RJuujHvmgYKZ7zzloroqQfZfSikh1MnOttuZqpBwy7msPIteGRRoi7xwXTTxWd-ciWp65SAUslCC8EeEs9_VwePBI1li9Ap-uawldGUDhZI6nzNB6BV_sW_WClodWCaqik7sORz2hiSTOg-9q9eKLOFkqFz9RXFMMBltqGyaIdGyg_bJ34T8tGl5IEeQcEj3Hnzo0Vfptsdllg564NsowN8DRU4lC-IxYgPc1bF3SOXrWMpQh3Kd4vQVLxMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز ویارئال
🆚
رئال مادرید رو در
TrexBet
از دست نده!
📉
نگاهی به آمار ۲ تیم در ۵ رویارویی اخیر:
ویارئال: ۲ برد، ۳ شکست و ۱۱ گل زده
رئال مادرید: ۳ برد، ۲ شکست و ۱۰ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/73057" target="_blank">📅 18:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73056">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c52e5fb32c.mp4?token=Q6HeNdRA-H_-NOwIJxjyfI6qiiRshSs8hDsmRfzoND10Yy5KN1JkrLRFDDtTqxbhqwf6ZENadR5xgCQT3zOnZtvImRaTRy1lBXEfpYQPsIj9bMHht5BfdP-djqtyWaNwTQLyPA__Xsb9sQunFhL6U1M3aWFTeAAq6abIACM2237YPw7rZSmNDouBAPWnZINa9bDM4ZVCjyxMf8LiDBsqJIG2mO0ve0qBuZyjjiBxDsTFGJoaGq_J0CCwWINC_7Nzr_KOTptPL1bJ-vEv-fLlwcRjfdkRgzwSTzf1lekt9QXoP5clNW-GWZAFt0uo8upGNxAqmkGLxoIAnvbzuEQSg7rzgj7FzZRxmFz6mw-meTiDAwmSBNyrZ4wUZqpco0WjdJrigb4mF_14foRf2j_MwDa553tuA9ac52-ODGUwzXMfwW7W7hMy3-JMZ0V1diFBP7QMB4jayLpe36nerRyFA11gtaMGDeZQPKkqtaG125qEt5n6GfNR8LxPaYQjoVLjVZxe2wwu9ZbTkcd2vOS6zBx7yvzeZ8AjfHdX-8JicLv0F0OQIu5ENilGlmEYcBXYcfORdh2NRl85LrXeKc6er02dar7AJoUL3kBn4A8A_52KzSHQO5XoHWTltNTRhTKANK3CHwvo6vR3qZ34BqhAr6XwSkjsd5h9V8zUt6XRKg0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c52e5fb32c.mp4?token=Q6HeNdRA-H_-NOwIJxjyfI6qiiRshSs8hDsmRfzoND10Yy5KN1JkrLRFDDtTqxbhqwf6ZENadR5xgCQT3zOnZtvImRaTRy1lBXEfpYQPsIj9bMHht5BfdP-djqtyWaNwTQLyPA__Xsb9sQunFhL6U1M3aWFTeAAq6abIACM2237YPw7rZSmNDouBAPWnZINa9bDM4ZVCjyxMf8LiDBsqJIG2mO0ve0qBuZyjjiBxDsTFGJoaGq_J0CCwWINC_7Nzr_KOTptPL1bJ-vEv-fLlwcRjfdkRgzwSTzf1lekt9QXoP5clNW-GWZAFt0uo8upGNxAqmkGLxoIAnvbzuEQSg7rzgj7FzZRxmFz6mw-meTiDAwmSBNyrZ4wUZqpco0WjdJrigb4mF_14foRf2j_MwDa553tuA9ac52-ODGUwzXMfwW7W7hMy3-JMZ0V1diFBP7QMB4jayLpe36nerRyFA11gtaMGDeZQPKkqtaG125qEt5n6GfNR8LxPaYQjoVLjVZxe2wwu9ZbTkcd2vOS6zBx7yvzeZ8AjfHdX-8JicLv0F0OQIu5ENilGlmEYcBXYcfORdh2NRl85LrXeKc6er02dar7AJoUL3kBn4A8A_52KzSHQO5XoHWTltNTRhTKANK3CHwvo6vR3qZ34BqhAr6XwSkjsd5h9V8zUt6XRKg0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این دختر خانوم با این پسره تو رابطه اس و که علاوه بره پسره، سگ دوست پسرش هم عاشق دوست دختر پسره شده.
@News_Hut</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/73056" target="_blank">📅 17:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73055">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/502e54151d.mp4?token=eAIgWvJtr5AbkAwA3I3KfN4QQpktp0SElHGuXSlw_0g6rezawUYMRo8gAY-FtquvC1n1Q8C-JCL2VKXFKG6_BRdGmiTymH9WWOXhUzCK6XysBLypsR1MovHhrBpcyIB5A8WXFL5_emTQ5Z5CES0xbJLcfqCdvlz5G4kcsH-KZGqIiIS7AyapvH0KqREZYtEH17q41Y8iFw0V1W8scL_VfzoTh_iULyE7Vv6wQejlnym4k8AV3vC6BdQhlPkWYhaCFh667R7KAivGRs7q1uqxpVNaXj2zA4p7dxVqhxu_0cMmxbljNumRYzTPQStLoXlYGhEvmghmzRKWZJ9o9kaBjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/502e54151d.mp4?token=eAIgWvJtr5AbkAwA3I3KfN4QQpktp0SElHGuXSlw_0g6rezawUYMRo8gAY-FtquvC1n1Q8C-JCL2VKXFKG6_BRdGmiTymH9WWOXhUzCK6XysBLypsR1MovHhrBpcyIB5A8WXFL5_emTQ5Z5CES0xbJLcfqCdvlz5G4kcsH-KZGqIiIS7AyapvH0KqREZYtEH17q41Y8iFw0V1W8scL_VfzoTh_iULyE7Vv6wQejlnym4k8AV3vC6BdQhlPkWYhaCFh667R7KAivGRs7q1uqxpVNaXj2zA4p7dxVqhxu_0cMmxbljNumRYzTPQStLoXlYGhEvmghmzRKWZJ9o9kaBjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از بمباران پادگان سپاه در خرم‌آباد، استان لرستان، در جریان جنگ ۴۰روزه:
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/73055" target="_blank">📅 17:02 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73054">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZfG1KRD7JlQMdAKxP8XKfrziNhdlY6BbedofaYyOxKvZYlePaR_4TfTqeDdtw2YJ0dhsUuF1w_PggCQ8Sz3tyI_iCSZ7fQE5PFMlUuyW9ngEyDtJnI0rsjIPdopW4XLuT9STEphreekVBDMSJW4pPk7UzDhFgfNRfYN4ZF2Dj-UlAZ4mxT3iL3IfO3Osr92uMAtK1niKVBjLhpmufoWfC_NmOK4py9-68CwhMx3dqmyGuRCR_mjETnqeEO2jK7yhpEwJZLGN38dakgjtMLYmnqQG_wYSs03tjYJwUT3Yk9fQFVtpcZioK5EkVk451kMJ911BP8_jim693GiPiJZXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛
معاریو: آمریکا از اسرائیل خواسته به‌تنهایی به ایران حمله کنه!
طبق این گزارش، واشنگتن توی مذاکرات دو هفته اخیر از اسرائیل خواسته بود بدون مشارکت مستقیم آمریکا، حمله نظامی به ایران رو انجام بده.
هدف آمریکا این بوده که پیش از انتخابات میان‌دوره‌ای نوامبر، هزینه سیاسی حمله به ایران متوجه ترامپ نشه؛ درحالی‌که چنین حمله‌ای می‌تونست از نظر سیاسی به نفع نتانیاهو، پیش از انتخابات اسرائیل در ۲۷ اکتبر، تموم بشه.
ایال زامیر، رئیس ستاد ارتش اسرائیل، هشدار داده بود که ازسرگیری جنگ می‌تونه باعث تعویق انتخابات اسرائیل بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/73054" target="_blank">📅 16:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73053">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fca26fcca.mp4?token=JLQmOGQCqFTK_faKuGl1Mhgp6XgEnaqA6cbhnvAo44WWiZgQTYroq4cuRAS8tAxUFNzlqU1szoGIpSIXnayM1lwvMrv1RqB9fq9DR6sGkxkAInUJKs4vr-LoOFojU50JmvD8wGS78YKyXoe75SPXtaJ6Ix9N-Uv1OO84Cq5mSnM0Tnr9Urij6ow5mJnxdxOj0hW8TGdMYgBFB2AFUgKnsTyWdeOK4SC4BOCk8rBnVMkJwIMerz7szVQfHIN0SurODY7_LLnR-sW0dK3Q0DmghOHcojcQsOJEglQdTeInrviv4IG1CaZ4Rq1Lyqxm3dk_vlx1dh3stiNTNICuA5q-aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fca26fcca.mp4?token=JLQmOGQCqFTK_faKuGl1Mhgp6XgEnaqA6cbhnvAo44WWiZgQTYroq4cuRAS8tAxUFNzlqU1szoGIpSIXnayM1lwvMrv1RqB9fq9DR6sGkxkAInUJKs4vr-LoOFojU50JmvD8wGS78YKyXoe75SPXtaJ6Ix9N-Uv1OO84Cq5mSnM0Tnr9Urij6ow5mJnxdxOj0hW8TGdMYgBFB2AFUgKnsTyWdeOK4SC4BOCk8rBnVMkJwIMerz7szVQfHIN0SurODY7_LLnR-sW0dK3Q0DmghOHcojcQsOJEglQdTeInrviv4IG1CaZ4Rq1Lyqxm3dk_vlx1dh3stiNTNICuA5q-aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظاتی ترسناک و باورنکردنی که امواج عظیم زیر رعد و برق یک کشتی باری غول‌پیکر را ناچیز نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/73053" target="_blank">📅 16:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73052">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0VEBoa4HupZNwW7iNEVRR1snvlC7PyN942W8Abn-mx56wgpbF-U0EhJ1Acc9IumuZKqylaC-Ija1rGq-NCOapW4_KiSH-jmChFn32mdvfw6WV9C20w7c72OrPUtO539TZu2hC7tlNV1EU9dt9m6f0T_2vOa9E2kzURptTQS2NZK1RiLRe4axL6CYaaNltIJPgfL5XTQLdbDLMQxleZ8veao-FF9XYOhBtBF-9YHzhdB1JAzwyGKkcSWrudiWlqKNH7Gijl0rQwMGDV8TqSRLYwXvsxCjCTFnb7cNPfxLMWN7JMwrpOILdze3IFs3sgh_AtOG6TdJrsNbb9QYqTdtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:«من به ۸ جنگ پایان دادم و به پایان دادن یا حل‌وفصل ۲ جنگ دیگه هم نزدیکم.
همه گروگان‌های اسرائیلی، از جمله ۲۸ نفر آخر رو، چه زنده و چه کشته‌شده، برگردوندم.
صدها گروگان از کشورهای مختلف جهان رو آزاد کردم و به خونه‌هاشون برگردوندم.
در ونزوئلا در جنگ پیروز شدم و دیکتاتور خشنی رو که با بی‌رحمی اون کشور رو اداره می‌کرد، دستگیر کردم.
همچنین جلوی جمهوری اسلامی ایران، بزرگ‌ترین حامی دولتی تروریسم در جهان، رو گرفتم تا به سلاح هسته‌ای دست پیدا نکنه؛ و خیلی کارهای دیگه!
با وجود همه این کارها، نه من و نه ایالات متحده آمریکا جایزه صلح نوبل رو نگرفتیم. عجب!»
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/73052" target="_blank">📅 15:43 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73051">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f583eac4a.mp4?token=jJ2U36hHxM0O7IKoJXD4r9cena-Ku2BZMHvqZziC-qRGaNm_wFTH9gHtHZCXLaftItJE5aMOfba2UkImANsPT7q7SFhVDksVOUZtmr6mPjrzjnFfTN2_TGVJhT3GaVcbUlKEcGP46fiSglv3FFBShsVDHeKjz4EJvXdm9Qu9S853ZBYtMyrnqD1CrcKdYb04r3KckyWW3saC4AnAOSygemSDtuAfBGPZLHw6NdnbQzQqoFbcUNFxUh3SO2dIDUaTqnD1CwfXmJOs7uaBw-sFvoOr_WFzBYAYuNii8xJ-Xq1bg0GL1hJfWAo0J-_75cAk8DXj_YxDNGQZtOmQB5VYrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f583eac4a.mp4?token=jJ2U36hHxM0O7IKoJXD4r9cena-Ku2BZMHvqZziC-qRGaNm_wFTH9gHtHZCXLaftItJE5aMOfba2UkImANsPT7q7SFhVDksVOUZtmr6mPjrzjnFfTN2_TGVJhT3GaVcbUlKEcGP46fiSglv3FFBShsVDHeKjz4EJvXdm9Qu9S853ZBYtMyrnqD1CrcKdYb04r3KckyWW3saC4AnAOSygemSDtuAfBGPZLHw6NdnbQzQqoFbcUNFxUh3SO2dIDUaTqnD1CwfXmJOs7uaBw-sFvoOr_WFzBYAYuNii8xJ-Xq1bg0GL1hJfWAo0J-_75cAk8DXj_YxDNGQZtOmQB5VYrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شهرداری خرمشهر دیده یه سرسره تو پارک شکسته، با خودشون گفتن چکارکنیم چکارنکنیم؟؟
که این نیمه شاهکار رو پیاده کردن :
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/73051" target="_blank">📅 15:32 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73050">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76ef585e24.mp4?token=eHumTd4P476xchtk89T9aUAU6AYiTygSVKuJeObU6Bx5oURhRfwQ_fgEtMcfaOdO2_O2qI6z_AsPjbvOVSlaTq8uXQKbjILq_2oIylVcT-7VbCNbaaTlNPb0cNPmNsNOyNVcVP1-pAEvYITQ46VRjnACGT0yjtRYm6SeaszRGgI5ZM3ccU25e1uEVZdBMX4qJiu6Wo99ljMqsiG0aUxzR8xY_d0wEn8plPABcuut8KakawDzFiSr3FqxgJTPOXnpzVCnapGh_SQDEwMZ9RNNrYbQXrTUSpJyDyBkasb4rAEOdm5MQ9se9DIeA36r1RuSpKe8iMUbS42-82oA77bkog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76ef585e24.mp4?token=eHumTd4P476xchtk89T9aUAU6AYiTygSVKuJeObU6Bx5oURhRfwQ_fgEtMcfaOdO2_O2qI6z_AsPjbvOVSlaTq8uXQKbjILq_2oIylVcT-7VbCNbaaTlNPb0cNPmNsNOyNVcVP1-pAEvYITQ46VRjnACGT0yjtRYm6SeaszRGgI5ZM3ccU25e1uEVZdBMX4qJiu6Wo99ljMqsiG0aUxzR8xY_d0wEn8plPABcuut8KakawDzFiSr3FqxgJTPOXnpzVCnapGh_SQDEwMZ9RNNrYbQXrTUSpJyDyBkasb4rAEOdm5MQ9se9DIeA36r1RuSpKe8iMUbS42-82oA77bkog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میرسلیم:
نفت ایران مال مردم نیست و متعلق به خدا و پیامبره
مردم  حکومتو انتخاب میکنن فقط و اون حکومته که تصمیم میگیره چطوری نفت استفاده بشه
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/73050" target="_blank">📅 15:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73049">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/520264f117.mp4?token=dSIb1Btb5a6fdzuRhaCd3KfteCMSL_okfJn2dTse-Xa0uUnmX_rTALfCX6_9hgJ18g61HeLp5A2fsLkYcLh8p12Df9yms_BFLlHfOrF6RE32RKBQValbMgdQzHKke_A-F8PyxfG5Wck_tcgB_qVrBk4L6Pb9wVmaddPhe3SwrMK6OY9Rb3TZs2m1CfbGCuHY5ogkLLRVq3vL1eIhWpdhZp0buXNCXke-4oXMMhxNY4yfkMp83f1ihrf8cYAP30pxXZCLEBiQxIsyeeDDzV-dvOG9KYOBzgUtUOIupsvQqCcDcuZGaIBdKG4nEwLwcFe41TGOa-9PRyx_scY67qk94Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/520264f117.mp4?token=dSIb1Btb5a6fdzuRhaCd3KfteCMSL_okfJn2dTse-Xa0uUnmX_rTALfCX6_9hgJ18g61HeLp5A2fsLkYcLh8p12Df9yms_BFLlHfOrF6RE32RKBQValbMgdQzHKke_A-F8PyxfG5Wck_tcgB_qVrBk4L6Pb9wVmaddPhe3SwrMK6OY9Rb3TZs2m1CfbGCuHY5ogkLLRVq3vL1eIhWpdhZp0buXNCXke-4oXMMhxNY4yfkMp83f1ihrf8cYAP30pxXZCLEBiQxIsyeeDDzV-dvOG9KYOBzgUtUOIupsvQqCcDcuZGaIBdKG4nEwLwcFe41TGOa-9PRyx_scY67qk94Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی وایرال شده از اجرای امیرمحمد، نوجوون ارومیه‌ای داخل برنامه Kaos Show ترکیه:
+ این برنامه، عقب‌افتاده‌هایی که تو فضای مجازی معروف شدن رو دعوت میکنه تا مردم بهشون بخندن.
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/73049" target="_blank">📅 14:32 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73048">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/983154ebcc.mp4?token=FY73p_8-8f9sLdBrQit76CXeuAbVl-cUCkHPWj0oQ69AHPKR97HqRwoBMK9mJCOIqwQmBQZKZedu5_dJBjaRtcG_jPeMVGacjTatHQ9XBQ89xePduInMnlUUATkwRSfvQJoxdqhwsYx40pIg1xQfSJkr7ga-WHz6jGtR-7yYEMfmPKsPjFUL2G3ZzxXZtFPL60r2vAmcvxrMbvZpZao-CfOiM7EvNRMBiAL3WDU6MVhYX--NG3vjen98CNfMQi4S7niE4-AEgp4oAVMt_kpiWu4GaiPV06HXuqFLwwJwQ3NwqQ0TZ_ca2XGDz1Pkzn57fLiyVyiuFTogXwcmnwWKmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/983154ebcc.mp4?token=FY73p_8-8f9sLdBrQit76CXeuAbVl-cUCkHPWj0oQ69AHPKR97HqRwoBMK9mJCOIqwQmBQZKZedu5_dJBjaRtcG_jPeMVGacjTatHQ9XBQ89xePduInMnlUUATkwRSfvQJoxdqhwsYx40pIg1xQfSJkr7ga-WHz6jGtR-7yYEMfmPKsPjFUL2G3ZzxXZtFPL60r2vAmcvxrMbvZpZao-CfOiM7EvNRMBiAL3WDU6MVhYX--NG3vjen98CNfMQi4S7niE4-AEgp4oAVMt_kpiWu4GaiPV06HXuqFLwwJwQ3NwqQ0TZ_ca2XGDz1Pkzn57fLiyVyiuFTogXwcmnwWKmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن نصرالله، رهبر کتلت شده حزب‌الله لبنان، ۲۷ خرداد ۱۳۸۸:
امروز در ایران چیزی به اسم تمدن پارسی وجود ندارد.
آن‌چه در ایران وجود دارد، دین محمدِ عرب است.
موسس جمهوری اسلامی هم عرب بود و عرب‌زاده. امام خامنه‌ای هم عرب است.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/73048" target="_blank">📅 13:45 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73046">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/97e3d7ab08.mov?token=MqpKLzV03ZtHnKhJXrSzVewj5TsuGe9yIzPP5FqQW5A-sGA9vdPhfQ-D0mqXdH_qR0FKEqKhmjQ44xTy4QMbL0QWQbvAIwhsL1uyp32wu_N9p6DkO0OGk7WTGxgA7SlNeun1ZVDcnTUwy7RxcQkS-x0n9DPIZJBV2d2oR4zuHo6c-6mG96zj8U9sZdmEICchNJDEA7nhb9G9C8FYDnxqy3Kh4nPYDVygi4Ciksi30p7HZxkhZRl8HlC4g6Wjf6ueff4QOSY-H6quhWnHNZvxFNLa5h28Q85VJkTUbkpQmrZjW9OLHxLxuHpZw52VbhNjz1TjNyGvP6iu-rMoo-Pi2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/97e3d7ab08.mov?token=MqpKLzV03ZtHnKhJXrSzVewj5TsuGe9yIzPP5FqQW5A-sGA9vdPhfQ-D0mqXdH_qR0FKEqKhmjQ44xTy4QMbL0QWQbvAIwhsL1uyp32wu_N9p6DkO0OGk7WTGxgA7SlNeun1ZVDcnTUwy7RxcQkS-x0n9DPIZJBV2d2oR4zuHo6c-6mG96zj8U9sZdmEICchNJDEA7nhb9G9C8FYDnxqy3Kh4nPYDVygi4Ciksi30p7HZxkhZRl8HlC4g6Wjf6ueff4QOSY-H6quhWnHNZvxFNLa5h28Q85VJkTUbkpQmrZjW9OLHxLxuHpZw52VbhNjz1TjNyGvP6iu-rMoo-Pi2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب صدای این انفجارها توی شرق تهران شنیده شد که گویا تست پدافند بوده!
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/73046" target="_blank">📅 12:51 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73043">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/351194ef56.mp4?token=I2vCocKnxINi6GqXQo0bw3pIH13gnqN5BaJcKbLTKQVinUuCQm1Ej0rX8cmR2-fmhX7eSbvw-YuEqN-IumCt0lQZYtpq0M88hAlnuIWdTRTYIHpEuBwDHjD-MzIBT5tEjqnC8brgUVsOf4cB1Rdsvz-gwffLppncEICywViDUKr1MbFlAl0ZdoQWuZp6BdVSzJlvNSP1giAwuwYjZhwjFwBDtchnlTWy33stX2VSjW5-gfpbpaaVYSjxevZPh7vUbtQDEZJ2SPNRkDsYf57e2gCg6kD0E1OAFy4SxhJj2msmxb_LA_uapNae457H_PQ8jMA1p7L_Kr5H0hmxB5ljtA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/351194ef56.mp4?token=I2vCocKnxINi6GqXQo0bw3pIH13gnqN5BaJcKbLTKQVinUuCQm1Ej0rX8cmR2-fmhX7eSbvw-YuEqN-IumCt0lQZYtpq0M88hAlnuIWdTRTYIHpEuBwDHjD-MzIBT5tEjqnC8brgUVsOf4cB1Rdsvz-gwffLppncEICywViDUKr1MbFlAl0ZdoQWuZp6BdVSzJlvNSP1giAwuwYjZhwjFwBDtchnlTWy33stX2VSjW5-gfpbpaaVYSjxevZPh7vUbtQDEZJ2SPNRkDsYf57e2gCg6kD0E1OAFy4SxhJj2msmxb_LA_uapNae457H_PQ8jMA1p7L_Kr5H0hmxB5ljtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیشرو و هیچکس بعد از ۱۰ سال قهر و دعوا، دوباره باهم داداشی شدن و دیشب کنار هم روی استیج رفتن!
نکته جالب ماجرا این بود که سروش هیچکس فریاد «جاوید شاه» سر می‌داد و سالن رو به لرزه درآورده بود!
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/73043" target="_blank">📅 12:14 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73042">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73042" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/73042" target="_blank">📅 12:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73041">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cE-zT-B1M6RiadRq8ZvBSDcnadgHnAYkvz-DqM8wQcPdThpu8kBICDJCYo-nG5q0ZG3ocGuUCaH_CqM0fPU5AQ2ZdkQnKefoZo7oAd5HkegphMh1XNhY5PXjhMMy64SXDMtBkPZxbBUlE_-lFj45DdGjhbrifNf6dvGfFdTPUlLqkEgOKBqmGPJoHgWsCBFlh_hx2pXWvLeIr8lYg24nfRuSMu7imDqE1Cf35C1IK4P25r3dK1LIr6P-Y9iuW2mfY57ymtLgdVVn4gnNOk16fWHEWs87qST_4auBlq2V6WuQ_7zhGu3_MlAYo_eBcYmRCJBXNcuYmFwHT0xWIq2DOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
لیدز
🆚
آرسنال
بورنموث
🆚
چلسی
تاتنهام
🆚
منچستر یونایتد
ختافه
🆚
بارسلونا
ویارئال
🆚
رئال مادرید
بایرن مونیخ
🆚
آگزبورگ
پارما
🆚
اینتر
فروزینونه
🆚
ناپولی
لومان
🆚
پاریسن‌ژرمن
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/73041" target="_blank">📅 12:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73040">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e742ff38d.mp4?token=VnDeahdFkX_Q2ghsSUqvxG_mhx0B1dO0E-US3LQoA7JvXQO5NcNp65WXuY-P06BG-OqmxcNyDwd6dSu0VPXuVWMw0cO643j-sQ-mMHnMcEJA69p8FrYtRrBI0n0VRYuF2S0EBDN0swppPhPWpB-T9cKd8KYeaBMx9NOLzxD0B76elChdDt9EttMaJUTn4TXDnoWjzG_8OHo2foNniYF1Kzn2TzV2UQ4moVGfcTCZmlTdd2Fb0VM3JQKEbH13vIWWBobUuvLuFATsxBKFyn0qguzJdPGjs6wm0-3MVCaFMD7kcdqXMyMC2vzVrdbZTXN7VGgyw5FDjjQmNWS7uO9c6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e742ff38d.mp4?token=VnDeahdFkX_Q2ghsSUqvxG_mhx0B1dO0E-US3LQoA7JvXQO5NcNp65WXuY-P06BG-OqmxcNyDwd6dSu0VPXuVWMw0cO643j-sQ-mMHnMcEJA69p8FrYtRrBI0n0VRYuF2S0EBDN0swppPhPWpB-T9cKd8KYeaBMx9NOLzxD0B76elChdDt9EttMaJUTn4TXDnoWjzG_8OHo2foNniYF1Kzn2TzV2UQ4moVGfcTCZmlTdd2Fb0VM3JQKEbH13vIWWBobUuvLuFATsxBKFyn0qguzJdPGjs6wm0-3MVCaFMD7kcdqXMyMC2vzVrdbZTXN7VGgyw5FDjjQmNWS7uO9c6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میرسلیم:
مرگ مردم در تصادفات رانندگی به علت رانندگی بد آن‌ها است و ارتباطی به کیفیت خودروهای داخلی ندارد.
واردات خودرو خارجی باعث می‌شود کشور پیشرفت نکند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/73040" target="_blank">📅 11:27 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73039">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e55bfab16d.mp4?token=TXo8YAsAOjHq4PYmd7uakw6mq-PzW81diI1ZUdZV3gNMjRv15X_VE8O53pXiKoloWvlIYTQAE-rjfh0Yfk_dYX9oJpdq7WIpcLm5SzIpPwNbPcyIEbO6JC0RzNKVADfs36rK3RDY2QyN-tthB7vXUjr_ItV3xG7XUezbSOqFVIcANCE8_EA9Tum-LBSn4p0QYwFar2TzA9lkIfN4-CVMEQljOZElZ_cDPsL8Ty4Tn1xyO_XkYy4V6jDowGppze7RwqektAkbS10BQhcjDC1tUdO1TVqs_xOPokMz2eBcn6_h0ubWu-EzOeDlwpAtYJHwfisIQgygrKN6EM65aNxdNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e55bfab16d.mp4?token=TXo8YAsAOjHq4PYmd7uakw6mq-PzW81diI1ZUdZV3gNMjRv15X_VE8O53pXiKoloWvlIYTQAE-rjfh0Yfk_dYX9oJpdq7WIpcLm5SzIpPwNbPcyIEbO6JC0RzNKVADfs36rK3RDY2QyN-tthB7vXUjr_ItV3xG7XUezbSOqFVIcANCE8_EA9Tum-LBSn4p0QYwFar2TzA9lkIfN4-CVMEQljOZElZ_cDPsL8Ty4Tn1xyO_XkYy4V6jDowGppze7RwqektAkbS10BQhcjDC1tUdO1TVqs_xOPokMz2eBcn6_h0ubWu-EzOeDlwpAtYJHwfisIQgygrKN6EM65aNxdNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مایک تایسون، بوکسور افسانه‌ای:
«اگر رئیس‌جمهوری مثل دونالد ترامپ وجود نداشت، به‌هیچ‌وجه امکان نداشت امروز اینجا باشم. متشکرم.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/73039" target="_blank">📅 10:40 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73038">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d334669b16.mp4?token=eyBHO3KBslp8F-vXV9NXDulkMx6-WME_IXSkj3Ka1PbRMW74wFN2A22-DBlOqSaBurSs7NVGH0zPY6fWW--klKBkZ2rx-QikxVmpRjRaIjpWgs_3HtSNuydVXTqSRWNmksCwZY9R74MBbO4tbfAlHJs48kppFJ0bF5TkP28vKPfuXzu_U9tYEgpUqCKwBsGlvWzlZlcOkeUHMtiWLxRPL_chjSLAjSdg89WXFyogW8sELuz47W81ePtZuYdlP9WZTLDDHAs5PdsGZPtoVyRWdu1M0dSyxgSfG1AybGb1RDcFqwhMn8P26CkKyl6hP2GYV5qjHap8THe2wX9dLLYcWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d334669b16.mp4?token=eyBHO3KBslp8F-vXV9NXDulkMx6-WME_IXSkj3Ka1PbRMW74wFN2A22-DBlOqSaBurSs7NVGH0zPY6fWW--klKBkZ2rx-QikxVmpRjRaIjpWgs_3HtSNuydVXTqSRWNmksCwZY9R74MBbO4tbfAlHJs48kppFJ0bF5TkP28vKPfuXzu_U9tYEgpUqCKwBsGlvWzlZlcOkeUHMtiWLxRPL_chjSLAjSdg89WXFyogW8sELuz47W81ePtZuYdlP9WZTLDDHAs5PdsGZPtoVyRWdu1M0dSyxgSfG1AybGb1RDcFqwhMn8P26CkKyl6hP2GYV5qjHap8THe2wX9dLLYcWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوووری
؛ پرزیدنت ترامپ:
«ایران یا همه‌چیز رو به ما می‌ده، یا دیگه وجود نخواهد داشت. خودشون اینو می‌دونن.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/73038" target="_blank">📅 10:14 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73037">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">میرسلیم:
تیبا با خودروهای خارجی ظرفیت رقابت داره
واردات خودرو باید یک در هزار بشه هموناییم که وارد میشن برای این باشه که ببینیم چطوری ساخته شدن
مجری:
الان چرا کشورای حوزه خلیج فارس همه بنز و ماشینای خارجی سوار میشن ولی ما سمند و تیبا و دنا با این قیمتای بالا سوار بشیم...؟
میرسلیم:
میل و انتخاب خودتونه دیگه
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/73037" target="_blank">📅 10:03 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73036">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">سپاه  تصاویری از حملات پهپادهای «شاهد» و موشک‌های کروز به شناورها در تنگه هرمز منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/73036" target="_blank">📅 09:31 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73034">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ویدئو های وایرال شده از دعوای پشت پارک یه مدرسه دخترونه در تهرانپارس که دو تا اکیپ با دوس پسراشون رفتن داخل پارک بخاطر اینکه یکی از دخترا همزمان با 4 تا دوس پسرِ دوستاش داشته خیانت میکرده به رفیقاش و گرفتن چند نفری زدنش و دوستای دختره هم برای دفاع ازش اومدن!
نکته جالبم اینجاس که چرا دوس پسراشون ایستادن کنار نگاه میکننو نمیرن جلو جداشون کنن و گاهی تشویق هم میکنن که بیشتر بزن هم دیگه رو!
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/73034" target="_blank">📅 09:02 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73033">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/73033" target="_blank">📅 01:55 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73032">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C34zYLVVwAG1dKuiuo1FAaWal0pWPQ-IXHgHsNoSu7n9P-dncrJ_2tnZthalWO4sOJHAwcl-Q-v2KnxvcjksgJjE6QFbKv2Eqm_on8VsYztMYXWScJ45Zjihhd-hmtuBFpW9EmAYnlNz2RCJOCG3hLsZI9uoOiqsIRJQBhu2GTBhMCDV3DKpVglJMW2e89eKrmESTWKe93OPcmu84esHnKF3e35slrJTfUq6McdSBz_ozFJYpac_j_EbfLdtk2UN3DVKnSwDfqdrgVx2GyWE-enq4LVXmLGfYgl6pj0myA_s2UBKHBHJlFGHHUhXtscobGtxM40eOJB_iZkw14Nf4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/73032" target="_blank">📅 01:55 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73031">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d4fabef22.mp4?token=WPUTh7pYdUcQj8TacZ2aOM5Axsc55EgjbtrfKJK3rqOtHyz3pnrwHXmxzXDDv0TZUjP6vkHWUpGyjIVICkxlgy8wRuSQWt6qMzq5JBOFDlLWiXesV3iQi4bUPDVPZRpdLDdgc94ttYcQS3R9hC72-BE2rmkV6A-BEyXo5kEz2sYJJ-MqAT0o6Vza3CudW7TpsmUEUzJEuMOKGaC7U9PIE2D_p5h9njcvx0ZOkVvq8l5Qj3YX6I5kaWDmtPcITbetU4fN2e7ZRvEo0awMMjVBpEwd0tWUHrkrnPNplyUy3N4Y87twMSm65uERb_DjNr8DhfVufyyJrDmo8m32DZzDZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d4fabef22.mp4?token=WPUTh7pYdUcQj8TacZ2aOM5Axsc55EgjbtrfKJK3rqOtHyz3pnrwHXmxzXDDv0TZUjP6vkHWUpGyjIVICkxlgy8wRuSQWt6qMzq5JBOFDlLWiXesV3iQi4bUPDVPZRpdLDdgc94ttYcQS3R9hC72-BE2rmkV6A-BEyXo5kEz2sYJJ-MqAT0o6Vza3CudW7TpsmUEUzJEuMOKGaC7U9PIE2D_p5h9njcvx0ZOkVvq8l5Qj3YX6I5kaWDmtPcITbetU4fN2e7ZRvEo0awMMjVBpEwd0tWUHrkrnPNplyUy3N4Y87twMSm65uERb_DjNr8DhfVufyyJrDmo8m32DZzDZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ما در هیچ زمانی پیش از انتخابات میان‌دوره‌ای آمریکا در ۳ نوامبر به ایران حمله نخواهیم کرد.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/73031" target="_blank">📅 01:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73030">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pexSqocsVCm1SihSTTo_nH3TYywK9gkTCP-thgZ5Qg2MmV-DlymBrwiLeAqVNzSuqNDbBDcT51406YHTyDC2oXdaDPner5xP2ACSJLdA7rm1C1xcrBsxa7FpsY7MZtrAJ_LSSEbeGqnUH9HTzTbxddPI0rX5prtEBYO_5K6xJDYNmkOWbbUxukrzLZcmOz_XlWGkmo0cZ5hnOmPC0HIP1fegKSjRSbmYDIqUULvmt95fNmwUhIa0p04q_7ABy5EyqD6JbC2ilUgciGavFynRA0I9HXUZr2hfyGGFg-__BcSvsl4qqYibeg_aatzGjQa0xfb3TQ5ofRWE3R3da9m9Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛
هشدار امنیتیِ وزارت امور خارجه آمریکا:
به شهروندان آمریکایی هشدار می‌دیم که فورا ایران رو ترک کنن و به هیچ عنوان به این کشور سفر نکنن!
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/73030" target="_blank">📅 01:14 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73029">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">از سیریک چندین پهباد/موشک به سمت شناورها در تنگه هرمز شلیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/73029" target="_blank">📅 01:05 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73028">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0925073180.mp4?token=V8tRqR3NGB6F33FynfGrCPsEVSZVb29pO_G32e19HlUdLVVbDrJyiEgCWzQhhA0ybNVf0pIbnv67-RtL_skt2BSsm4-INnQx9dBQrndqTpQQ0cbr0Y6ejpsfmM6krFFP1_S62IsWEf9ZYsKRdsTGmG8vn11mM6QFQvJoY0bbbwChZO23pbtuqyjgnhUXxJ1-brpDDtVtRFnBnTph2ra2ZstgEf8HOdfidXogT_7HWLsl6Ol82XdkOyC0BjsWnJPtXRoaN6NpvfEZtzRWagLU-SabjFbqp5ZPNkOgmfocQ2_oLeqqynQGc6ysZQz6mRRw0ZCClfmU-RiMjja5eilSPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0925073180.mp4?token=V8tRqR3NGB6F33FynfGrCPsEVSZVb29pO_G32e19HlUdLVVbDrJyiEgCWzQhhA0ybNVf0pIbnv67-RtL_skt2BSsm4-INnQx9dBQrndqTpQQ0cbr0Y6ejpsfmM6krFFP1_S62IsWEf9ZYsKRdsTGmG8vn11mM6QFQvJoY0bbbwChZO23pbtuqyjgnhUXxJ1-brpDDtVtRFnBnTph2ra2ZstgEf8HOdfidXogT_7HWLsl6Ol82XdkOyC0BjsWnJPtXRoaN6NpvfEZtzRWagLU-SabjFbqp5ZPNkOgmfocQ2_oLeqqynQGc6ysZQz6mRRw0ZCClfmU-RiMjja5eilSPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: زلنسکی گفته توافق نفتی شما با پوتین نشونه ضعف شماست.
ترامپ: کی اینو گفته؟
خبرنگار: زلنسکی.
ترامپ: باشه!
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/73028" target="_blank">📅 00:52 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73027">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bebfa1213.mp4?token=UluhMGCXIclbGnseEzyq5hjq-LOPyOHmWd4hlbgTuDkyBPPCMzW8IO1ypgA4DKF4TloyvfZFMdrg7Kc69uAMgqQKDmXEo7p5m86mObW84HhySpbSBLI3lvm0M7vJBbIOZBBkWVKVIEqYyTtCNY1AY9AJc_0-UJ1oaNsivhahFKpopecFlhlncwkDeWnVc7bhBBqCs64fxnnEph-r772iHWubB2i4iEcVWa0B6CKsy2mZVzVpwLTcQyHaU-otMx-W1oXiq1RJfiTe6Z0kQUgdrzUM3z59V6qd_Unmla7aTt_WvqFlS2PtqhyhcDaGzSTh6FsWsGuRFLBRH4MTUZrhOrZjD1xdkG5-x7UUOiHKx3KpS1zp8eKw9iW-4dDqn62DIKcaq3sG7f77Ngw_PEss_FKr3FKyJN0gXXndscoU3R7DEvw4IBgcVXiAv-ARINCPUP1jZ7aLV3nA4IGh10uUArauJppr07rl26GYEoJb06FCchyy6N0RnIpMzydOVE3b6QNIVSFDdj3G7jS3Vd4PXfLgWXQZ32Jjc2q_6xsitMQDH4pbqwsFwGGP95H36p_MTDtYYmlDIb1L_0ODyjfIAtMbk6TBIxk4WxVEdGNiitg3nWzh7mcOVEJEO1E8uuCnXiIqSZQ0jv4Be4CUmFtVrSurYwhDNoj6xHV7vERmJy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bebfa1213.mp4?token=UluhMGCXIclbGnseEzyq5hjq-LOPyOHmWd4hlbgTuDkyBPPCMzW8IO1ypgA4DKF4TloyvfZFMdrg7Kc69uAMgqQKDmXEo7p5m86mObW84HhySpbSBLI3lvm0M7vJBbIOZBBkWVKVIEqYyTtCNY1AY9AJc_0-UJ1oaNsivhahFKpopecFlhlncwkDeWnVc7bhBBqCs64fxnnEph-r772iHWubB2i4iEcVWa0B6CKsy2mZVzVpwLTcQyHaU-otMx-W1oXiq1RJfiTe6Z0kQUgdrzUM3z59V6qd_Unmla7aTt_WvqFlS2PtqhyhcDaGzSTh6FsWsGuRFLBRH4MTUZrhOrZjD1xdkG5-x7UUOiHKx3KpS1zp8eKw9iW-4dDqn62DIKcaq3sG7f77Ngw_PEss_FKr3FKyJN0gXXndscoU3R7DEvw4IBgcVXiAv-ARINCPUP1jZ7aLV3nA4IGh10uUArauJppr07rl26GYEoJb06FCchyy6N0RnIpMzydOVE3b6QNIVSFDdj3G7jS3Vd4PXfLgWXQZ32Jjc2q_6xsitMQDH4pbqwsFwGGP95H36p_MTDtYYmlDIb1L_0ODyjfIAtMbk6TBIxk4WxVEdGNiitg3nWzh7mcOVEJEO1E8uuCnXiIqSZQ0jv4Be4CUmFtVrSurYwhDNoj6xHV7vERmJy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
«توافق نفتی با روسیه خیلی مهمه؛ حجم عظیمی نفت وارد کشورمون می‌شه.
راستش رو بخواید، می‌خوام از رئیس‌جمهور پوتین تشکر کنم.
این نفت هم گازوئیله؛ همون چیزی که ما می‌خوایم. پس ازش تشکر می‌کنم.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/73027" target="_blank">📅 00:50 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73026">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffadaf48ae.mp4?token=Vq8JfloKOnxnkx_MP9h3V63QjWOKQiheoYG851d_l7wcZutWatb5BGpLzQFba3BWz4ZYIR7wbXe2j28eGZa40sAU6jNh-CmE7tTwEqb6uuuqkRR-Z1ez2tii62XR56muyvdnCHq3TwubcUjO9Qn3m90X0Di4FwpqGRi_RNehi-lkTLdCNspa-13PEjBBJqJtIycUbV20bwSAJUDXdv-mWwEjApRljxS7x3VXVbWOUmEe5ttvT5ueO3UTGN7geaujqiPVIrYQe4ZhdIn0eMIsjawfPKRLh680i9BBSGZ-xlB_2BpGn7MbRU97C89L5ZJia8ZDFj4kRY13PnB1EULZ7DZePwBmU5E1e3mrTnBDwwIDAgxOx1ooh7bnrUgaIVqeK95LZP_uYllbWxyQe1zczsRzA1zP4oxOOa-JtIEMZxEW1rmM4r5xR-J4lPPdHoYhCngp_J1KFnbgKKAYCYLvU8dlUPE3rMejU8ixB9gOFRDY_5fm7Dp2kFqX9QSV-mDwEn2Et24rEMZyoUU_b8rRLPe2tzV3PK8Ua1C3Zq9QQ2Q5Awn8em0N6MM9PE4-UxYDTSat_G28YwT6nChIdSt4u12fzJBAFvMvq1Qks6_MgZY0fpG_Nzjbo5DEco0STzK101xdUrN0fuz3bC_jNvydJ5hGaYG4tv-Uo1ooKjB_PH4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffadaf48ae.mp4?token=Vq8JfloKOnxnkx_MP9h3V63QjWOKQiheoYG851d_l7wcZutWatb5BGpLzQFba3BWz4ZYIR7wbXe2j28eGZa40sAU6jNh-CmE7tTwEqb6uuuqkRR-Z1ez2tii62XR56muyvdnCHq3TwubcUjO9Qn3m90X0Di4FwpqGRi_RNehi-lkTLdCNspa-13PEjBBJqJtIycUbV20bwSAJUDXdv-mWwEjApRljxS7x3VXVbWOUmEe5ttvT5ueO3UTGN7geaujqiPVIrYQe4ZhdIn0eMIsjawfPKRLh680i9BBSGZ-xlB_2BpGn7MbRU97C89L5ZJia8ZDFj4kRY13PnB1EULZ7DZePwBmU5E1e3mrTnBDwwIDAgxOx1ooh7bnrUgaIVqeK95LZP_uYllbWxyQe1zczsRzA1zP4oxOOa-JtIEMZxEW1rmM4r5xR-J4lPPdHoYhCngp_J1KFnbgKKAYCYLvU8dlUPE3rMejU8ixB9gOFRDY_5fm7Dp2kFqX9QSV-mDwEn2Et24rEMZyoUU_b8rRLPe2tzV3PK8Ua1C3Zq9QQ2Q5Awn8em0N6MM9PE4-UxYDTSat_G28YwT6nChIdSt4u12fzJBAFvMvq1Qks6_MgZY0fpG_Nzjbo5DEco0STzK101xdUrN0fuz3bC_jNvydJ5hGaYG4tv-Uo1ooKjB_PH4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در کنار مایک تایسون در کاخ سفید:
«امروز قرار نیست باهاش مبارزه کنم، اما مدت‌هاست که طرفدارشم. مدت‌هاست با هم دوستیم. هیچ‌کس مثل اون نیست.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/73026" target="_blank">📅 00:46 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73025">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUHerEzyIFuJAHDf7k0N6Qd46R3nUcRmWPBlcYmqFxnhnUcjQvs8RyK3E0L_9Gr8DYA14IUQW5jbOgCI6c54rdN9Yuo9FThU29xYn2-8eAmlSomsuh1-QjGNkfYWqgrAKRc64BH-JEA4pwzyQqaK9DOrJrplErxVoUqH77YJeO3zd-M9-GYhmydbZXr6ekyaQ49SzB5z9k_a4TbMo6tj9Pm2MAwWChkjv0jyxCex-5F9WCNTm6muCNQdVk6xrpajp3PPOvH48qYwnOE8-z1qrvdlcAFOQGlPDm-7Hrz_qs6aoLG-UZijNzhoqqqzhrPWnXsz8XBBz-6PoH9JfRvhwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛وزارت خزانه‌داری ایالات متحده انجام تراکنش‌های مربوط به فروش، تحویل، تخلیه و واردات سوخت دیزل با منشأ روسیه — از جمله واردات به ایالات متحده — را تا ۷ آوریل ۲۰۲۷ به‌طور موقت مجاز اعلام کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/73025" target="_blank">📅 00:25 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73024">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e6f11119a.mp4?token=vHK1F93Tam8jMgSiTOn0XlbWAsvNmfDurZXvx4P6gCO6gXE4TYBdo7TF1ecDhOfyInudq-4J-lBtTGt3o8nzojiAQ9Wc5u4FFtNlHgOWNLRelRb2SnFZzUPFBIcBsnHz7fNUFtA3d-lTg4Bv8_o65atE7eEVNM5D9Lhq6nj06tXlVAda-aT04c1xRNjW48Dxs8XmU25SwG3BfCp66D41aOBuZARpNbc6ttKGHhGAGWM2eare_UOD7DBMWYcw65r6IcYu0-nZsC1vIv6JmrRQR8aJ16oB0ahlpS0S-4J_LGTfafnoApLR-Ua-1WXUkZqhJ16-kRCdmox_VCfOnZB9xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e6f11119a.mp4?token=vHK1F93Tam8jMgSiTOn0XlbWAsvNmfDurZXvx4P6gCO6gXE4TYBdo7TF1ecDhOfyInudq-4J-lBtTGt3o8nzojiAQ9Wc5u4FFtNlHgOWNLRelRb2SnFZzUPFBIcBsnHz7fNUFtA3d-lTg4Bv8_o65atE7eEVNM5D9Lhq6nj06tXlVAda-aT04c1xRNjW48Dxs8XmU25SwG3BfCp66D41aOBuZARpNbc6ttKGHhGAGWM2eare_UOD7DBMWYcw65r6IcYu0-nZsC1vIv6JmrRQR8aJ16oB0ahlpS0S-4J_LGTfafnoApLR-Ua-1WXUkZqhJ16-kRCdmox_VCfOnZB9xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سال ۱۹۵۴ بمب‌افکن B-57B Canberra نیروی هوایی آمریکا از آزمایش هسته‌ای Castle Bravo فیلم‌برداری کرد
این انفجار در آب‌سنگ مرجانی بیکینی در اقیانوس آرام با قدرت ۱۵ مگاتن انجام شد، حدود هزار برابر قوی‌تر از بمب اتمی هیروشیما.
قدرت انفجار موجب آلودگی رادیواکتیو گسترده در منطقه شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/73024" target="_blank">📅 23:58 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73023">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aFHJVFPPhF9DLe3QtBzNtBpG0ov6IE9EM0HTMJvGZHeiNOxnLKz8t-MGGPKVk9QsQJAuFS7NsyFe9eGB6HETZgxwP7X4T4nBG5QeIIGnU9xtlZxp9ieb4jgbkixjZS-ZisJje-uJ3YpGP37wGC-X3P5d3Oe-IPXa9z_9SPddxFnChoUGRxI1EoIedI6absaKFQmPAabBr3I6u-GVH3DPudahD1nh-D5lfjc2bk6zIPdijZHIZ1klhnWaaYmnDcb-zPMiBYaCRGuRnH3bCYB7uDcEa55XjrZOJPFk62-1AXciasPT4vHvYH0Thkqfxne3jLlLMAVYK69FWoEtUtjKNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
من به‌تازگی گفتگویی بسیار موفقیت‌آمیز با ولادیمیر پوتین، رئیس‌جمهور روسیه، داشتم که طی آن توافق شد روسیه بلافاصله بیش از ۳۰۰ هزار تن سوخت دیزل برای بازار آمریکا و جهان تأمین کند؛ همچنین ۵۰۰ هزار تن دیگر در ماه نوامبر و یک میلیون تن بلافاصله پس از آن تحویل داده شود.
علاوه بر این، با توجه به وضعیت پالایشگاه‌های دیزل روسیه، این کشور در مدت‌زمانی کوتاه، ۳ میلیون تن دیگر سوخت دیزل تحویل خواهد داد. با در نظر گرفتن «کنترل کامل» ما بر تنگه هرمز و این خبر عالی درباره انرژی روسیه، قیمت دیزل برای آمریکایی‌ها و در واقع برای تمام جهان، با سرعتی بالا و به شکلی بی‌سابقه کاهش خواهد یافت!
کاهش قیمت‌ها برای آمریکایی‌ها، به‌ویژه کشاورزان، دامداران و رانندگان کامیونِ فوق‌العاده ما، بزرگ‌ترین اولویت من است. این خبری بسیار بزرگ و مهم است. همچنین باید دانست که ایران هرگز به سلاح هسته‌ای دست نخواهد یافت! از توجه شما به این موضوع سپاسگزارم.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/73023" target="_blank">📅 23:06 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73022">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5846d15ad4.mp4?token=srqIEyiCzXMBmrzXIF3hnUtVumkQxqmlxHYJpBtsEE-rOG_VH0n2gswEIVV_MSOdyWMI957yTrs_wcWkwBAtC3yWxbOdUb8luNvgnaDsvsn4jSoaFpyyi0_nC3VXnQ5-tzOw9NsJRyJA5qB8YYFeXC2WOkWPVNkqpbG94YthHLXZ6QDQgQppTZ7mp6p1sfJPB5TPUjaw5yPAztsAzG87XqEBc7EcpA-jvHkmg0kNjUhbPA7xkj37sKQyhmarGTzrFapbbtXc2yTUBikz2ccMfZkRu0_pgtLY9i5qVeeNNnRTh6FHF3kBNohZDI35bBWi49MQbNKISvCOx0pewmuK9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5846d15ad4.mp4?token=srqIEyiCzXMBmrzXIF3hnUtVumkQxqmlxHYJpBtsEE-rOG_VH0n2gswEIVV_MSOdyWMI957yTrs_wcWkwBAtC3yWxbOdUb8luNvgnaDsvsn4jSoaFpyyi0_nC3VXnQ5-tzOw9NsJRyJA5qB8YYFeXC2WOkWPVNkqpbG94YthHLXZ6QDQgQppTZ7mp6p1sfJPB5TPUjaw5yPAztsAzG87XqEBc7EcpA-jvHkmg0kNjUhbPA7xkj37sKQyhmarGTzrFapbbtXc2yTUBikz2ccMfZkRu0_pgtLY9i5qVeeNNnRTh6FHF3kBNohZDI35bBWi49MQbNKISvCOx0pewmuK9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیده شدن پلنگ ایرانی در جاده عسلویه:
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/73022" target="_blank">📅 22:47 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73021">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ec656b26d.mp4?token=DE2U7w_ucN-zqYfeR-qr66Sj3SgZzMfFQRZ7TDr9fTbS0rH751amvFOn3N3CTPutP7w3qOoMUH3RA3RSqHIxpcQCxPwSCgBLRbnLoHSVvsW3DNMGrCP9ZcXrpna2iew5dPzOd5hfhMISlwOxCvZ_g-b9x2uk7LSFYlyhBr9glS4gMhKZNeo0U119hAUsXrGUnfaAAa1XX0Vu6GFDpYMU0oPb0_QbhBuZ8jnFtWgibyJyhEAJsZlkBgyoxAbFHYj3cbZoKePAPNoTF1ffztGcjy-ERS0u7xBKX23ueZhWnRelps6yOPquSbeNs7nx7RGkT9CmmGVK8mk2_Q1G2VV4ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ec656b26d.mp4?token=DE2U7w_ucN-zqYfeR-qr66Sj3SgZzMfFQRZ7TDr9fTbS0rH751amvFOn3N3CTPutP7w3qOoMUH3RA3RSqHIxpcQCxPwSCgBLRbnLoHSVvsW3DNMGrCP9ZcXrpna2iew5dPzOd5hfhMISlwOxCvZ_g-b9x2uk7LSFYlyhBr9glS4gMhKZNeo0U119hAUsXrGUnfaAAa1XX0Vu6GFDpYMU0oPb0_QbhBuZ8jnFtWgibyJyhEAJsZlkBgyoxAbFHYj3cbZoKePAPNoTF1ffztGcjy-ERS0u7xBKX23ueZhWnRelps6yOPquSbeNs7nx7RGkT9CmmGVK8mk2_Q1G2VV4ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گروه حامی حمید رسایی، سران نظام رو تهدید کرده و این‌بار گفته‌ «کاری نکنید مهرآباد را برایتان ناامن کنیم»
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/73021" target="_blank">📅 22:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73020">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/852188e7d7.mp4?token=DWtGGYrXo1C8HMy7ef8egDv60V34XNOVioUPD-5nLoGGU3uPv5VziTBxMEnhWWol0qqlxbf5GmRDCyiS-NC7fTAXAgwAbJX16yvV1X6AkTyeMUf54alw3wWoIyKcI7u7tE2-RwoG_iXRQ9eIWT4DnIeT9pErSTWDne7K3QswLSpll8sH5nm9_uqbYW9cKk0LfOnq_RO5rzFyjDPR9X90B3l_L4VGemnAarDnlH_fcKVSLrQorAQeDhKqAM6w3eqHwOd47xFfLVi00S6cVlZKVMMfkGGAWMQ622QvDHt6JS5Sgi85d9HYTs4v28-ODofPUFIuyDdSjVNFrmPu4FnpbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/852188e7d7.mp4?token=DWtGGYrXo1C8HMy7ef8egDv60V34XNOVioUPD-5nLoGGU3uPv5VziTBxMEnhWWol0qqlxbf5GmRDCyiS-NC7fTAXAgwAbJX16yvV1X6AkTyeMUf54alw3wWoIyKcI7u7tE2-RwoG_iXRQ9eIWT4DnIeT9pErSTWDne7K3QswLSpll8sH5nm9_uqbYW9cKk0LfOnq_RO5rzFyjDPR9X90B3l_L4VGemnAarDnlH_fcKVSLrQorAQeDhKqAM6w3eqHwOd47xFfLVi00S6cVlZKVMMfkGGAWMQ622QvDHt6JS5Sgi85d9HYTs4v28-ODofPUFIuyDdSjVNFrmPu4FnpbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ناوگروه آماده آبی‌خاکی «مکین آیلند | Makin Island» نیروی دریایی آمریکا وارد پرل‌هاربر تو هاوایی شده؛
این ناوگروه بعد از یه توقف کوتاه تو هاوایی، مسیرش رو به سمت غرب ادامه میده و راهی خاورمیانه و منطقه تحت فرماندهی سنتکام میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/73020" target="_blank">📅 21:14 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73019">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">فشار اقتصادی آمریکا علیه ایران؛ واشینگتن به‌دنبال قطع مسیرهای تجاری تهران؛
اسکات بسنت، وزیر خزانه‌داری آمریکا، در گفت‌وگو با شبکه نیوزمکس اعلام کرده که دولت ترامپ قصد دارد فشار اقتصادی بر ایران را به سطحی بی‌سابقه برساند. او از تشدید انزوای اقتصادی ایران و ادامه محاصره بنادر این کشور سخن گفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/73019" target="_blank">📅 21:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73018">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55ac3d9705.mp4?token=r1jDYi3HWPrlQW6WwcbmPLHikYzlKfSXlVIF0S9rF-ZxQnQex-SXLQz0TqZwpcegp_Bdm5bn4EIL9E4EBrfmoQ1UI43Y1MScxOa6W1NF8PPDzdOXKI47dgeP-teOzxQwYF4KOfeZEJCAA5cuGI9gOAaWvxJ9IjO0fvYmrcoHfQCslCQPEpIH1ZdXnxCx_5JYBe7i8E7Bp7fwpp5X8avYGAojaSTmoSsV-n9FdWpqOrLx1zyAznHOXfaQ_z4H2SEuogH6L-LTWwzFE5HTh7HdLxxPbEIn4NH1y7-rsNoqTd3i-xBWXTOQkJB4YOBzZ21XSK9fEYHkpNpD0S4AGl_DQ39JTb3BWnMc2mW6Wq4SQAiK4XZ4Dw9EIQJOexTpTM753UnyB5uOiRYrS_7RShWzdDAgf_QxgjQiT2EjzcoklH2YmC2Ya3BJEeocUxINXcVwjtElh9LffJ-Ts7HtxfEtlvlKgZRc8fSRpK4GAmdQYQtaFgEXuZD-uXX-2zDB2dm3dtRhhJRm7T7mkfct6I1IP2ADWO9TNrRs8SL2W9rOfJa8DLpzdU1uzycAG3eYpPmVzvZYsE8BETpXPi-hElRA0vsy1KYscqDWHF8lQFVs6cTl6VSTSp5Z7zg_KkuLJYHJC5fUdeSiE-bD9qX8X3gJlh5SLs2ovb9qt9os8uhW5V8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55ac3d9705.mp4?token=r1jDYi3HWPrlQW6WwcbmPLHikYzlKfSXlVIF0S9rF-ZxQnQex-SXLQz0TqZwpcegp_Bdm5bn4EIL9E4EBrfmoQ1UI43Y1MScxOa6W1NF8PPDzdOXKI47dgeP-teOzxQwYF4KOfeZEJCAA5cuGI9gOAaWvxJ9IjO0fvYmrcoHfQCslCQPEpIH1ZdXnxCx_5JYBe7i8E7Bp7fwpp5X8avYGAojaSTmoSsV-n9FdWpqOrLx1zyAznHOXfaQ_z4H2SEuogH6L-LTWwzFE5HTh7HdLxxPbEIn4NH1y7-rsNoqTd3i-xBWXTOQkJB4YOBzZ21XSK9fEYHkpNpD0S4AGl_DQ39JTb3BWnMc2mW6Wq4SQAiK4XZ4Dw9EIQJOexTpTM753UnyB5uOiRYrS_7RShWzdDAgf_QxgjQiT2EjzcoklH2YmC2Ya3BJEeocUxINXcVwjtElh9LffJ-Ts7HtxfEtlvlKgZRc8fSRpK4GAmdQYQtaFgEXuZD-uXX-2zDB2dm3dtRhhJRm7T7mkfct6I1IP2ADWO9TNrRs8SL2W9rOfJa8DLpzdU1uzycAG3eYpPmVzvZYsE8BETpXPi-hElRA0vsy1KYscqDWHF8lQFVs6cTl6VSTSp5Z7zg_KkuLJYHJC5fUdeSiE-bD9qX8X3gJlh5SLs2ovb9qt9os8uhW5V8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افزایش چشمگیر پروازهای ترابری آمریکا در ارتباط با خاورمیانه
طی ۲۴ ساعت گذشته تا همین لحظات، تحرکات گسترده هواپیماهای ترابری آمریکا در ارتباط با خاورمیانه ادامه داشته است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/73018" target="_blank">📅 20:26 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73017">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">وزیر آموزش‌وپرورش: تعطیلی احتمالی مدارس بر اساس شرایط هر منطقه تعیین می‌شود
.
کاظمی:
در الگوی جدید بازگشایی مدارس، شرایط هر منطقه به‌صورت جداگانه بررسی می‌شود و در مناطقی که خطری دانش‌آموزان و کادر آموزشی را تهدید نمی‌کند، آموزش حضوری در اولویت خواهد بود!
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/73017" target="_blank">📅 20:10 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73016">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">#فوری
؛نحوه فعالیت مدارس هرمزگان از یکشنبه ۱۹ مهرماه ۱۴۰۵
بر اساس تصمیم جدید:
- شنبه ۱۸ مهر:
همه مقاطع در هرمزگان غیرحضوری.
از یکشنبه ۱۹ مهر به بعد:
قشم، سیریک و جاسک:
- شهرها: ترکیبی از حضوری و غیرحضوری (تعیین‌شده توسط مدیر مدرسه).
- روستاها:
حضوری اقتضایی.
بندرعباس:
- سه روز حضوری و دو روز غیرحضوری در هفته (برنامه توسط مدیر مدرسه اعلام می‌شود).
سایر شهرستان‌ها:
- حضوری.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/73016" target="_blank">📅 19:41 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73015">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8de0455f4c.mp4?token=nWysx6TKGiwbGjhN7yB41r7tokIabUiMAEIAlr8UfVyRSoxoXB3EWKjJ0uxabf11PPrauOAy5gxjyUOhZJ2qrVrE7RfgT-vk7uE_10J62xPUtG6t0DLmz0RQped4UDTzNsVlChL0r0NUbVF30khqsbfloaiaBNygpOLNAMs5gvQ8rBnxl3asW6IWz6FASCUl3ZbZWk4gyWQ9jYjghtxCl40rcPj_MD12Ic6tdz60M_Mk1FDGCk1UN-ZYVoYsWl6RRmLzoj0eR1ttaZFe5icp4Xc6TqUrMwnQOO-0YOaFpWacK3VoibhjdJk2_muYRIbjL-U68GEGN5QGMuJ7vs59Koi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8de0455f4c.mp4?token=nWysx6TKGiwbGjhN7yB41r7tokIabUiMAEIAlr8UfVyRSoxoXB3EWKjJ0uxabf11PPrauOAy5gxjyUOhZJ2qrVrE7RfgT-vk7uE_10J62xPUtG6t0DLmz0RQped4UDTzNsVlChL0r0NUbVF30khqsbfloaiaBNygpOLNAMs5gvQ8rBnxl3asW6IWz6FASCUl3ZbZWk4gyWQ9jYjghtxCl40rcPj_MD12Ic6tdz60M_Mk1FDGCk1UN-ZYVoYsWl6RRmLzoj0eR1ttaZFe5icp4Xc6TqUrMwnQOO-0YOaFpWacK3VoibhjdJk2_muYRIbjL-U68GEGN5QGMuJ7vs59Koi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استاد دانشگاه امام صادق:
دیگه هیچی برای دفاع و حمله نداریم هرچی داشتیمو زدن؛جمهوری اسلامی هیچی نداره دیگه برای حاکمیت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/73015" target="_blank">📅 19:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73012">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DM28rRr724vUEPm6VZwoxPPKWa_N1Teda-yrDChy12CIP3mdn4qWA_t3ohSSkvCKdVAVq_DutEvX3mUNVyB4upq7bC7fi9yl6R7N8Fo0NObUsnYwKHhv1TlcFeHbNvYugzY70PF0Uc9UKMqtaosXYSgIKWJI-uIKg4bkPB4z-cA7OFyQvph2ouLq6pupzVCJgwQ3b4tNSgeYeO4JDlZ3mMzzlT0VlVYM4tdM2iPt44DX8GKbe0NAfuX91y7XB-3VGD8Y-oFGp1FS9lUYGPhxIT7iTcHXZ_L9K7kBF8H_f3LF0TQ3eyFoWgs593Pls0kYlebNGpUpQXkE1hhKLOl3GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fX-6dJoBWGTkLDxP9GT3uJeC3fSB34mhdCoQygebKQNWgc2i1d1sYbU0iV25SjWHDZOXk2c-89hCjDnnPLUI1KKsBWI0Ff8MaOa_-jC_KTbuwGaYQ1Fg5idopDIMu0uFnBlspcXGJ9Fe9sjA46C2NpP3a33LPapthHF2zDtD_RcHfF7zO3t62atxVkaCdbu_O8JopnZi5TWNtyBtKoCCze6KWcrOY8WWfJJSXhz2Yln0fDP2fc7d4prXes-1DV3tc5qUpyDbs-zwBfZeP29NQjeuTYeypfRW7wqwE-PgmRD8CJye3-Tumtu20hQPZs3DgssuBUUfqfK9i6sWhlTFsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/305d802103.mp4?token=Z6y-ijF2pgFF2Deir756qXVEvOSIgZ_5G0NbFet15fFe73drC1vfd6SWvMa7L-xuuMVUZM7F3WvBxEQs3U8Po3EAfxGSw5MTtKl2nj_-Op_wB6U_2TtY9Fm_1GcDz4ew7vNp6RyEn71nRbdWRqPrm73zDggIfi1pmaOJO1pBsjoY03caCzEknuzH99TB0Q8i0B9BiD4uLKUIrbEMkdiCIxAremlpCIrb4jSgxruUjMIHyj5PiQOGagzUgYBcE-7kPa8cUGObRcy-NY4PCms1yglhXNY_JJuVF6Eb1NAM63yZjLQCfbrfQiXsBGvesca6M6qgbVuNqkqIbujnvTDKFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/305d802103.mp4?token=Z6y-ijF2pgFF2Deir756qXVEvOSIgZ_5G0NbFet15fFe73drC1vfd6SWvMa7L-xuuMVUZM7F3WvBxEQs3U8Po3EAfxGSw5MTtKl2nj_-Op_wB6U_2TtY9Fm_1GcDz4ew7vNp6RyEn71nRbdWRqPrm73zDggIfi1pmaOJO1pBsjoY03caCzEknuzH99TB0Q8i0B9BiD4uLKUIrbEMkdiCIxAremlpCIrb4jSgxruUjMIHyj5PiQOGagzUgYBcE-7kPa8cUGObRcy-NY4PCms1yglhXNY_JJuVF6Eb1NAM63yZjLQCfbrfQiXsBGvesca6M6qgbVuNqkqIbujnvTDKFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو و تصاویر وایرال شده از آخوندفدا‌ها تو شهرستان بابل:
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/73012" target="_blank">📅 18:23 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73009">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O7e6Wn_uDMOK9gKjpIbzMLrWWtgc50WFrjz0qfBIcrZCNm4PIKVPsGVElnjgwOkKQB74Ye6GsAO6f1L4mVWIRjDWWySvrlPMREKT5xlUEQFOrfv8r9s0-dprQB7Tj2GVdYW4QOQVtMMdKWIz5o-6yogtG0KgMjn11hGQASRzfbUDCEQR22OsXiUKgeRxrwEUSbglz3aTtRJ7W_qa1MyS7SBFWpjIXbB2LTMQV52qgzSaJjuybQOcJqbuSM-MQKTx8qUcaxQDzCZiQJrRjAdkyWsi4J87v3q_GlRJ1LqoS0OPC_e4CDEK9bb_TL8FzgS1Zrg0pCwRi7sLd52V2wOxqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jkbUveLgjesoG7UnTTf1pvObq_Wce1wla_YmxbLytqzQQnQ-sf-83Ci3B6wee_gdS9sFjWnIf4MwLed9uP7mzsccA8B_9PVvfJLeqGl8aqmDduCSiD6LaHbGkwcW8Ev8EbwjX08mT-_OTuEmygE3iT0VU2Qyp7VguAkmklaGXGO1-SEtkDU4z8qxoPWqIMPHpfDJk_a0CVJhgEeoPDQ573lHP8OMCQUue2AKhpRHEjXabQDYOij4qReL709t1iA_Eid9xS_-7BXPS2AdTjN9fg_SbMBj4-KEgxapKQU3yC3b9DOfqYqn8sdEZUpYpicfv0GLq8zTPFFfkG5eKt0BxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c93bb666a.mp4?token=OjhFsljFfbP3PNz8WmtqXGsFV6aWHBwHhhFQg09fEdr4rwgrLq0ur0BV8XhaPI5E3i_dBrPpBaD-O3AY61Tg69wGdAUCqNoV-_BL2uLJP4lyO-5Dv89NBB7-nmKI33evxse62zxC7uteEHVY7td9IvCN0bl0TKoa_eAlic843_7b2Bazjr6SGimIWgo26lTwf8rxtwOUcesF5nmrGHG5m7ojlTciXwz3kI7gthpJ8aDQgCTXNbHgTw7W71uGwAXrQ17aes0492ZFzJ_qCBWIO9uVRqX884GACRN9jHoYxdKC8dg38jW2t0o-uaMxjiol4BTGL2NOiQL11fh7uZ2u9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c93bb666a.mp4?token=OjhFsljFfbP3PNz8WmtqXGsFV6aWHBwHhhFQg09fEdr4rwgrLq0ur0BV8XhaPI5E3i_dBrPpBaD-O3AY61Tg69wGdAUCqNoV-_BL2uLJP4lyO-5Dv89NBB7-nmKI33evxse62zxC7uteEHVY7td9IvCN0bl0TKoa_eAlic843_7b2Bazjr6SGimIWgo26lTwf8rxtwOUcesF5nmrGHG5m7ojlTciXwz3kI7gthpJ8aDQgCTXNbHgTw7W71uGwAXrQ17aes0492ZFzJ_qCBWIO9uVRqX884GACRN9jHoYxdKC8dg38jW2t0o-uaMxjiol4BTGL2NOiQL11fh7uZ2u9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات هوایی عربستان به صنعا پایتخت یمن:
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/73009" target="_blank">📅 17:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73008">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TUGg7e27_azaIUmmj6euuA6IBTdoLMp7aYIFDEvGgRv5YGxJSQqjSspVnNMwjKEHgQi-Q5MBqIgm8oVYyGmJ-FsYyn8QMiPAMbJihHVKXiKarfAEnBdRm2Ty7-OjnTNSlyKg5LqyqDivacKzhXfk05PHj_4tFHovuWDqiM-7025BjBfDVy2sXoQS-hbik7itl_qlX_n_AOcw7r3A0J_RvXClbjKZfILvb-LAAWjhifsnJJqQG4GvC_c4TREdvz_RarYgwBU3crOVGFTORPJ2nHB0CNx9qaiOBDv3UrIrOIFnx6LF6XCvGQhANdRxQhoLrzVkt_LzZP49YTJyh0CbMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران:
از الان به بعد برخورد با شناورهای متخلف محدود به تنگه هرمز نخواهد بود و هر شناوری که از مسیر غیرمجاز تنگه هرمز عبور کنه در سراسر منطقه تحت تعقیب قرار‌می‌گیره و حتما تنبیه می‌شه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/73008" target="_blank">📅 17:46 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73007">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73007" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/73007" target="_blank">📅 17:46 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73006">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VyiuMPQy9LNMQ9MQNq5lzGVZjenT8DUt6_gpjP_qKvPhGyeL-b8hKA3Ombh1gnUhuAmacjE7XiGxAAXOLvZgfALJbQHTzFQzQCnOQcMPUFCSNowOgiQquf6n8oUVjF-I2-Y4QaJZdXBdUzgM_Rja2PpRgAUSBvbNNxgmqaBBa4xtNFhmrVpQPJKB4ybJ21vZ7bzmjOxnUOgou_ML3VoKlAzopmwNpNNfRwl3c__fO7nDkB8fe9QCOs1s2bqt8CZgSocMynER154zCV4r_nPEnQQJF8DEn3FnRSX3hE57D5k2f95tke5kTlylsbR2W4Rluy9WW6wNmln3GA4oJC4GDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
🦖
قوانین رو در سایت مطالعه کنید
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/73006" target="_blank">📅 17:46 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73005">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0f7d86e64.mp4?token=Yq6cEbkfM4t3T6-wfGdYDY4ZE0YXZ5T7HMdXe5hlp9-t9N60SQaGf95ldWRBwvV6Z1eygkowloEIISuTfhBOzsm45FsWs2uHWxUaj_gC6-4Qj2Lb6GkHmzwBz2M_MmIHHcv_6JXS9yZkPJFfc86msZTIUlbTbgRpuFbA90X9A0CYbjAUx2Xx--YRevnKBoFKTE-iZ0F57--TkhYtFtzwLEzfc97bXw0t4C_efRvxfqWxI1f5ucvO0zmr2QY7q5QndB5EjTf7RKttBc1GcqjWim3fc9Z7yYNb3mzUwu3-q5lA8N-AXORXepn6ocqGg6Dvh3X5xWTFBeCQO7Ahy98bTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0f7d86e64.mp4?token=Yq6cEbkfM4t3T6-wfGdYDY4ZE0YXZ5T7HMdXe5hlp9-t9N60SQaGf95ldWRBwvV6Z1eygkowloEIISuTfhBOzsm45FsWs2uHWxUaj_gC6-4Qj2Lb6GkHmzwBz2M_MmIHHcv_6JXS9yZkPJFfc86msZTIUlbTbgRpuFbA90X9A0CYbjAUx2Xx--YRevnKBoFKTE-iZ0F57--TkhYtFtzwLEzfc97bXw0t4C_efRvxfqWxI1f5ucvO0zmr2QY7q5QndB5EjTf7RKttBc1GcqjWim3fc9Z7yYNb3mzUwu3-q5lA8N-AXORXepn6ocqGg6Dvh3X5xWTFBeCQO7Ahy98bTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از هواداران حکومت : رفتم تو گونی!
رفتیم جلوی مجلس تجمع کردیم پرایوت نامبر بهمون زنگ زدن
با یه شماره به من زنگ زدن از اطلاعات سپاه بهم گفتن بیا اطلاعات باید توضیح بدی
هیچکس با کسایی که هنجار شکنی میکنن و پست های زشت میزارن و کاریکاتور های زشت و زننده میزارن کاری نداره
بعد من که براساس قران عمل کردم ، منو خواستن احضار بشم
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/73005" target="_blank">📅 17:43 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73003">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86531200e8.mp4?token=i7j_y-m4ZcO2oc-fS7MLDNN8cfZH6SU6h5suPtZ63QaPDwKDkwoRBKtJSmtJC_8Bp1AkK8kghejJQRHraIol-OXUknZFn7m3g7nsB1vA9LIVsIPdTUjr8aGwOf0tUOZ5z6HkoNxljpCbvdWt5eirV2nQC5hJbuhe3O6ZjvLZohfNOWqpNm96XeHKaazzKPUn9awlMmNRqZnkjxRvkrQY7bLLelDhX8gnegUSUE6q-06m4t91u5KKaZa9BXxwDODnGSI0g71UvWctKvBoVbjpXInA5vXAKVasC9W0eQhOn4ebnR79km9Yi-fTDlwn_5SSorLPVkInylRcSdWt0u6QKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86531200e8.mp4?token=i7j_y-m4ZcO2oc-fS7MLDNN8cfZH6SU6h5suPtZ63QaPDwKDkwoRBKtJSmtJC_8Bp1AkK8kghejJQRHraIol-OXUknZFn7m3g7nsB1vA9LIVsIPdTUjr8aGwOf0tUOZ5z6HkoNxljpCbvdWt5eirV2nQC5hJbuhe3O6ZjvLZohfNOWqpNm96XeHKaazzKPUn9awlMmNRqZnkjxRvkrQY7bLLelDhX8gnegUSUE6q-06m4t91u5KKaZa9BXxwDODnGSI0g71UvWctKvBoVbjpXInA5vXAKVasC9W0eQhOn4ebnR79km9Yi-fTDlwn_5SSorLPVkInylRcSdWt0u6QKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛درگیری مسلحانه در چشم‌زیارت زاهدان؛ اعزام گسترده نیروهای نظامی؛
به گزارش حال‌وش، در پی حمله مسلحانه به یک خودروی حامل نیروهای نظامی در منطقه چشم‌زیارت زاهدان، ده‌ها خودروی نظامی و امنیتی به منطقه اعزام شده‌اند و پرواز یک بالگرد نظامی نیز گزارش شده است.
هم‌زمان، رسانه‌های حکومتی از انفجار بمب کنار جاده‌ای در مسیر یکی از خودروهای انتظامی استان خبر داده‌اند. برخی منابع محلی نیز از کشته‌شدن معاون اجتماعی انتظامی استان در این حادثه خبر داده‌اند؛ با این حال، جزئیات و آمار تلفات هنوز به‌طور مستقل تأیید نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/73003" target="_blank">📅 17:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73002">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAX19l9qcDY-8hMpxq6dJr3C6rqs90Rhy5NOg--92baq6_mk6tKmlvEcRgOhmrXdUVz3VtTfPiA99kN4hjQkWuBJK0LMfxG1eL6unQAjTXNkjY54y0P3zHX5aIwJI_Y7cgl3E_iokreFlgSfGbO0s2mYztB-TWpCmqgYGTfx1Xu9g0HwX0iKeUWUjEErspUqCAEmNUuhUMtn_IDm0I3BHMxCZe7WnuVy9NA1FMaKk3QDpiG12kaH3d4li9JN7w7NCZCQYsAPcUjtBYXP7d6LjVDAdQRF8t_jpgW_qjRtopWjTZGfzElBYsmsVKiPpyE0BTVgH42igi3J5RMaJFkm4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حال‌وش: کشته‌شدن ۱۲ نیروی نظامی در حملات ۴۸ ساعت گذشته
به گزارش حال‌وش، در حملات مسلحانه اخیر در سیستان‌وبلوچستان، ۱۲ نیروی نظامی کشته شده‌اند. در حمله به دو خودروی نظامی در منطقه کرین‌دوک نیکشهر، محمدرضا اوکاتی کشته و پنج نفر مجروح شدند. همچنین سرگرد مهدی جمشیدی در فاریاب و ستوان‌سوم وحید عنایت و عباس آقایی در محور لخشک زاهدان کشته شدند.
هویت سایر کشته‌شدگان هنوز احراز نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/73002" target="_blank">📅 16:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73001">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/487ed2a10b.mp4?token=A6bnlT9REC7sWlYCsd7J5aNvT83lznns1bTTQyZIBDqHW_hqcxxzaeQ5X2Plksyqxk7uKqOtnUu6ZNxAaXIdBb1deplPgZry1P2L5u8ZOd6mVPnVQUwZ211b3vWE9d13id9D9EL8fobAW1JnTccr92UdaTDvxQKya9sNfH1GfsZGci7mvyqdJgoewOseXRRJMKwMKt5nF-gjnjwiMfDjROvmciolfyELQSPUFIWJr90wa1GdPnevrqg06jfmoU5W7P2gXPFL5UAogpxFqr2LelMui9qypI7zh-mEJZ5cpsaSfNq7HJ7fqCO2g8EvkDrjB2LRgkYkjwf6ZBobW4t4tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/487ed2a10b.mp4?token=A6bnlT9REC7sWlYCsd7J5aNvT83lznns1bTTQyZIBDqHW_hqcxxzaeQ5X2Plksyqxk7uKqOtnUu6ZNxAaXIdBb1deplPgZry1P2L5u8ZOd6mVPnVQUwZ211b3vWE9d13id9D9EL8fobAW1JnTccr92UdaTDvxQKya9sNfH1GfsZGci7mvyqdJgoewOseXRRJMKwMKt5nF-gjnjwiMfDjROvmciolfyELQSPUFIWJr90wa1GdPnevrqg06jfmoU5W7P2gXPFL5UAogpxFqr2LelMui9qypI7zh-mEJZ5cpsaSfNq7HJ7fqCO2g8EvkDrjB2LRgkYkjwf6ZBobW4t4tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرف برای نامزدش یه شب رویایی رمانتیک ساخته واسش گل خریده کنارش یه ایفون 18 پرومکس ۲۵۶ گیگ هم بهش هدیه داده، دختره همون لحظه میگه ۲۵۶ گیگ چیه اخه ۱ ترابایت میخواستم!
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/73001" target="_blank">📅 16:31 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73000">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb6da5f21.mp4?token=DnYduxlujDpdZ3_EqrRJ6aF9ATQ5uz_JxlpovRYxiI9bG0sIy3SzXOL-WaadvU8bAYmpsQ6hlIgYxGCGq_05YzQskKK7Qjj3PUEdW06Ib9goHY0CUu54EH7uiaHfvp8eEYXIEvLqSyk2uQqHOv5IScuRIjtUeAEXVYzk5MFMz1jX52yemiikTom4PtDT886uW9-owNkh88ecHLje_Ai763IOMgrSJhy7ywkyjfXaH_fmeEoG1QFQljp5lbUbl530Nzqii0HZF9MtAkAeqTC_QQTQ2HWEbgSvjA4OnfLGga-UDvNuiGpVkS1ptwGoQwVKjCHVpfMUbJb6esM90tPoLqE6OO-yLhF-3QVfTJO2KDI3_yn7U1WO8JX2dwOXx5PGPTWYSgs3Uwl_jk7m4YWvuNsTM53ZiHFEy67xniRcyNglyv5Au34eSrMnM_nAC-9cfFkzH82_sSIbRc4wMLCrzKOsf3gNVP3VvYmfFNnbKbAPeJWsnc9woj13DHvVmT0e_tkAZbfgn_877BBCtu9Dv3I6lFyzc8DRhoUitml0KCQa1ijDH9uA3pN4sMGvk8aQTv7z6WCy8gOE6NfhCZ4rI2jqI8YbAqNEXznvN7UZ3DniLstFViF7VpRn78r2O559ppf_IRDD1IRjOI--VYVQQW8CZp7Hcbgl3b73qTyqEF8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb6da5f21.mp4?token=DnYduxlujDpdZ3_EqrRJ6aF9ATQ5uz_JxlpovRYxiI9bG0sIy3SzXOL-WaadvU8bAYmpsQ6hlIgYxGCGq_05YzQskKK7Qjj3PUEdW06Ib9goHY0CUu54EH7uiaHfvp8eEYXIEvLqSyk2uQqHOv5IScuRIjtUeAEXVYzk5MFMz1jX52yemiikTom4PtDT886uW9-owNkh88ecHLje_Ai763IOMgrSJhy7ywkyjfXaH_fmeEoG1QFQljp5lbUbl530Nzqii0HZF9MtAkAeqTC_QQTQ2HWEbgSvjA4OnfLGga-UDvNuiGpVkS1ptwGoQwVKjCHVpfMUbJb6esM90tPoLqE6OO-yLhF-3QVfTJO2KDI3_yn7U1WO8JX2dwOXx5PGPTWYSgs3Uwl_jk7m4YWvuNsTM53ZiHFEy67xniRcyNglyv5Au34eSrMnM_nAC-9cfFkzH82_sSIbRc4wMLCrzKOsf3gNVP3VvYmfFNnbKbAPeJWsnc9woj13DHvVmT0e_tkAZbfgn_877BBCtu9Dv3I6lFyzc8DRhoUitml0KCQa1ijDH9uA3pN4sMGvk8aQTv7z6WCy8gOE6NfhCZ4rI2jqI8YbAqNEXznvN7UZ3DniLstFViF7VpRn78r2O559ppf_IRDD1IRjOI--VYVQQW8CZp7Hcbgl3b73qTyqEF8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌های یه جراح و متخصص زنان :
این خانم 16 ساله بعد اولین رابطه‌اش تو شب اول ازدواج (شب زفاف) دچار خونریزی شدید شده ولی چون فکر می‌کرده بخاطر پارگی پرده‌‌شه، نیومده پیش دکتر و الان هموگلوبینش چندین واحد افت کرده!
در واقع شوهرش فکر می‌کرده داره کابینت نصب می‌کنه و بی‌دین زده همزمان پرده، پرینه و فورشت رو باهم پاره کرده.
اصلا پارگی پرده خونریزی زیادی نداره، هرگونه خون‌ریزی بعد رابطه رو لطفا جدی بگیرید...
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/73000" target="_blank">📅 16:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72999">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bae6808a3e.mp4?token=tJsz1kgu8NWJwX_NIxvd7ZMJWI0G1IyaHnwfo4aRGP8pN08T90HKrkaZK5djXJEUmkKzsU-EYZC8TB2e_ANGsgyU_PYGBLFlCplNVn5W1-_iPjU4-BNBJpccycgDNzfRL--Qh3lPLCHxHOatDBiOsuxaUQyDlRQKfIxMwDtbX-lSQE4t9CbK4ahSM_m-ROI5P12p0J7cqeYpqX0-jK_LwbzcL6h-JdQXFHBDYtMr4AbXn2PcD7JTrH0YYxP-RvCEJ_swigew48Ar4NngPZsXnGLBGH_SL18EbRWbup5aSs_tI-1R9gldML4gpUOOsveXVt3rOvAsHTNfAR9M5qwIxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bae6808a3e.mp4?token=tJsz1kgu8NWJwX_NIxvd7ZMJWI0G1IyaHnwfo4aRGP8pN08T90HKrkaZK5djXJEUmkKzsU-EYZC8TB2e_ANGsgyU_PYGBLFlCplNVn5W1-_iPjU4-BNBJpccycgDNzfRL--Qh3lPLCHxHOatDBiOsuxaUQyDlRQKfIxMwDtbX-lSQE4t9CbK4ahSM_m-ROI5P12p0J7cqeYpqX0-jK_LwbzcL6h-JdQXFHBDYtMr4AbXn2PcD7JTrH0YYxP-RvCEJ_swigew48Ar4NngPZsXnGLBGH_SL18EbRWbup5aSs_tI-1R9gldML4gpUOOsveXVt3rOvAsHTNfAR9M5qwIxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حزب‌الله حدود ۲۰۰ میلیون دلار از ایران گرفته تا بین لبنانی‌هایی که در جنگ امسال با اسرائیل آواره شدن، کمک مالی توزیع کنه!!!</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72999" target="_blank">📅 15:32 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72998">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed5ddc3810.mp4?token=BHxkeV8HXqLS-BGgqSXYTgGqPRTUX77Ou0vamiRBt8xp1ige2WXDiig0b5B8DhDYzMd4VP3xzy7FIbzYbP11V27y_T2mDJLh0AXXdHLRgJTIWKDhv7trmkuShVO0nTClBia71CtGIy8zDHQBw2GNod2QawO0U4enw8zc7udd8jMwOwNtsybF-kA3z9q_a72urkwBzGxV8NKftVjG3dOTXJ0pqTOfzMvElXYfYNdAtPigiz6J1e2Va4S7eNExYMBjqhSycdGMRH3kiUO4287BR9pKnG2CpUsRWvLq634KSObjV9Ukm5yTT_St9QOk5PnjrL83Ec3AHJ5Qy1Blm08spg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed5ddc3810.mp4?token=BHxkeV8HXqLS-BGgqSXYTgGqPRTUX77Ou0vamiRBt8xp1ige2WXDiig0b5B8DhDYzMd4VP3xzy7FIbzYbP11V27y_T2mDJLh0AXXdHLRgJTIWKDhv7trmkuShVO0nTClBia71CtGIy8zDHQBw2GNod2QawO0U4enw8zc7udd8jMwOwNtsybF-kA3z9q_a72urkwBzGxV8NKftVjG3dOTXJ0pqTOfzMvElXYfYNdAtPigiz6J1e2Va4S7eNExYMBjqhSycdGMRH3kiUO4287BR9pKnG2CpUsRWvLq634KSObjV9Ukm5yTT_St9QOk5PnjrL83Ec3AHJ5Qy1Blm08spg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه حمله پهپاد هرمس هرون تی پی اسرائیل به نیروهای گردان پدافند لشکر3 حمزه سیدالشهدا سپاه در آذربایجان غربی در جنگ ۴۰ روزه
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72998" target="_blank">📅 15:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72997">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8rPfSGIUAVqU_27s7AHn23FrgReMKvefjjO1mC6wQYtxAtzXrYEpe111GX8MsUfnrcZYEy4CYEc8sqrQBxRFM0tsgsuS3xmYqFSTJ8-AmiDjnJxxbVIPET_sgHA053xgNqXI6EDU1vle50bzUjQ8etouhTOGsC8lP8tFY77yXzBFDsceJdxb59JJmE2LdsAniDbPZdLoPe--851k0Ic14hsUHNfnQntyp7xSR0ukd45VgkRBk9ShtdbZBbISTMVWIpglONIyFkGV_urk-0YubeS-oxWZ3No3dK3b8Uhmj5LgJreEz8K9kyE8L1-4CDJUjLbwn3gSClM1V28qDxatw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار امنیتی جدید سفارت آمریکا در اردن درباره احتمال اختلال در پروازهای منطقه
؛
سفارت آمریکا در اَمان بار دیگر به شهروندان آمریکایی در خاورمیانه هشدار داد و با اشاره به احتمال تشدید تنش‌های منطقه‌ای، درباره لغو پروازها، بسته‌شدن حریم هوایی و اختلال در سفرهای هوایی هشدار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72997" target="_blank">📅 14:16 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72996">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a562a527a7.mp4?token=C5CVhRLau28CPex5vYqcRelVpvBQUp1vEbYuOvZqxrlLx0DlpFIbjSa0gBuClfKVRGPI8LaywLR5q5bjohb08rbzFUeot7BG9KpeRdDDONj5xttr3jltcNhMRvGes8q_NDxG0tujtFMt3PK27UZTkn3L8jITslYWtVJiQwQ3c0v6hWcSIVgWCDRJKhCBRx2OCcjsGHklAe_kCQ15OZ20LrW2mkBc-inugiIwaoXOCTy86dGo20M3OZIXa8ZdJ7ResYQF4_z2CEKMmYZfJ8_EKwA7PyZ1rASfW0Nqc2ekh0--VPDnRsPT0c5QvQjhAu2voeqOXG8FCGFHD__SAPyANTcr6s16PI92iW7EDp4j-Fev-YxN3-0ceJGFJdRg3OPE2kbiHskwpt70K-M8UPTtRY4fiZCYAb1UH_m2zAoR1pJ1QGgfvru21_tVtYRiacP8z9kSpMFQWNqi-HdArgAZ5sWe2n8df4d31xt_DNnz4PQdGrvhTv2m9gYbmMDyzRFWEig9SiNBUWoCOvC6oHPidtBePjrCEiUNT29odg6usnuavAaFkHc0hu68UlsNdGknSA8iBjlmKvquRMBi9XLCADMLqEeaiYEqUF4dK2mkIhqDnjtZFc35DMYJKqKSbxHNGIy4qRU_wXuafVqxSAuNy4tEMJxqYPcRrpmqGuOKf8o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a562a527a7.mp4?token=C5CVhRLau28CPex5vYqcRelVpvBQUp1vEbYuOvZqxrlLx0DlpFIbjSa0gBuClfKVRGPI8LaywLR5q5bjohb08rbzFUeot7BG9KpeRdDDONj5xttr3jltcNhMRvGes8q_NDxG0tujtFMt3PK27UZTkn3L8jITslYWtVJiQwQ3c0v6hWcSIVgWCDRJKhCBRx2OCcjsGHklAe_kCQ15OZ20LrW2mkBc-inugiIwaoXOCTy86dGo20M3OZIXa8ZdJ7ResYQF4_z2CEKMmYZfJ8_EKwA7PyZ1rASfW0Nqc2ekh0--VPDnRsPT0c5QvQjhAu2voeqOXG8FCGFHD__SAPyANTcr6s16PI92iW7EDp4j-Fev-YxN3-0ceJGFJdRg3OPE2kbiHskwpt70K-M8UPTtRY4fiZCYAb1UH_m2zAoR1pJ1QGgfvru21_tVtYRiacP8z9kSpMFQWNqi-HdArgAZ5sWe2n8df4d31xt_DNnz4PQdGrvhTv2m9gYbmMDyzRFWEig9SiNBUWoCOvC6oHPidtBePjrCEiUNT29odg6usnuavAaFkHc0hu68UlsNdGknSA8iBjlmKvquRMBi9XLCADMLqEeaiYEqUF4dK2mkIhqDnjtZFc35DMYJKqKSbxHNGIy4qRU_wXuafVqxSAuNy4tEMJxqYPcRrpmqGuOKf8o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قرار شده ۱۱۰ هکتار از چابهار رو بدیم به مردم افغانستان تا بتونن یه سرزمین متعلق به خودشون داشته باشن</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72996" target="_blank">📅 13:32 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72994">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pWRvLSCkuDk143Qj7PV71_JXVit-wkdgfpN8uRp0DYV9WyjT8qCmBw3nh-NbOnptc5QxU8L4XEDcvayiASdB3MZAUXFuSQHezL2VMuzn3MJKDm60lmF_clGLCbMoknV85S9oXVyMv9z9jV5AdHb1nnqdOOa3M6gbhFzv0qrZMwmvpGXHkoPPfaKlODSU7UXEhRE8hypoaImLw3LpLzlhCgAca4hmwRgUibvShULtsZ8zkWCQtNhBzSBmf7uZThaOK0qSICHnMwsC6R5s563fIwKBLEX97pbJF5sld5dJ_MHqQG66CO63TzsobNswWvZZjoTegnA2ioVZCGjW_a383g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n_t6-wl0AGzYKVT5Ft1NkHbBSyPuq5sT2JnKdL_lQtkVKIdJPWfHAQsTxwMEbDEFKr5-l45Lr_J2vaRN2RvRD80lF_2ffB3Hv-7MYIlaMLJIcyydZ34mjGsaMJqkoEtqBN61XX9HuBZcOPp0ziliS7xgO5dJNv_9XQvTtCak57dJhBMaBS2DHJoz2X5qKbq8pse2Gz3Hkz_QMdqHvXNgmRcmjvCoinLpWFOsC7svL66M09VhbsdInqemlqc_F0ranlcQPu-LOa0WMVLWA-xZGAT9Gvxn5oMaOKzbTzdbR2bgVsaweEM8z7TWlqNpM2B7uUnIbDZWyRTvJkHzXCGqNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ناو هواپیمابر آبراهام لینکلن پس از ۳۲۱ روز به خانه برگشت؛ در حالی که بدنه جزیره فرماندهی اون با نشانه‌های ثبت‌شده از اهداف منهدم‌شده در جنگ با ایران پوشیده شده.
تحلیلگران دست‌کم ۱۰۳ نماد پهپاد و ۳۴ نماد کشتی رو روی سازه بالای عرشه ناو شمردن.
گروه رزمی این ناو در جریان عملیات «خشم حماسی» (Operation Epic Fury) و محاصره بنادر ایران، ۳۶۹۳ سورتی پرواز رزمی انجام داده و ۴۵۰ موشک تاماهاوک شلیک کرده.
این گروه همچنین رکورد ۲۶۴ روز متوالی در دریا، بدون پهلو گرفتن در هیچ بندری رو ثبت کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72994" target="_blank">📅 13:06 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72993">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57fcb1ffcb.mp4?token=GiE7txAU3JM90bNumFjjhDmJUsqq3thf_YdFXgkvVIA6f3MVDYIXTz9hY8ydApfEYqgxeVceIdedQEpJhDSQw6XYaCDTgaTd2fQinmHpLgZ5NaARI3AhlMKAkRlQHFXb9ZG67heF-DVIarF403wqiHSjWGhnNX6taxAIzZ676rF-n2TEDG_EMOqSjHQDncmTwxfg1OkKta3Pb-emoPMVjfq6iiK6HiyGbgqrpz-imAnQuTPYr_psAKMfh3x0RP26yUFxNb7LC235IPI8yI_Bm1-TwaNK_00-QXdpjVsVl2QbjHhhflgv90wNObO3KGtIzk11R519jmUqZOq_PDu1I4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57fcb1ffcb.mp4?token=GiE7txAU3JM90bNumFjjhDmJUsqq3thf_YdFXgkvVIA6f3MVDYIXTz9hY8ydApfEYqgxeVceIdedQEpJhDSQw6XYaCDTgaTd2fQinmHpLgZ5NaARI3AhlMKAkRlQHFXb9ZG67heF-DVIarF403wqiHSjWGhnNX6taxAIzZ676rF-n2TEDG_EMOqSjHQDncmTwxfg1OkKta3Pb-emoPMVjfq6iiK6HiyGbgqrpz-imAnQuTPYr_psAKMfh3x0RP26yUFxNb7LC235IPI8yI_Bm1-TwaNK_00-QXdpjVsVl2QbjHhhflgv90wNObO3KGtIzk11R519jmUqZOq_PDu1I4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اسلامی، رئیس سازمان انرژی اتمی ایران:
ایران هرگز از حق غنی‌سازی اورانیوم خود صرف‌نظر نخواهد کرد و ذخایر اورانیوم خود را نیز تحویل نخواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72993" target="_blank">📅 12:52 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72992">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a317d9a3a1.mp4?token=TU1GNGmRRXPkik1qIeSfEkBHpAWpXzOKUHNG4SQvHq3aFk6aFFh0Cvw4T-SvTIWYio3iIimhA4EI8XJPegtGcDf8ZlmTA73qnRNB23Ppg3kPAMzS2npa5nRkWCNezsYNB4L7EBh_r3-KYxyZ-LYb9MEpYgjuH1AIJ74Nnz0Wa0b_PXlAyDFf3Hb37EWbq5EkqK0RMvvuOk03vWqr6ZpiwFvVrT9cyizRJ60ZO764JeqZ8W3TyA3ufrm-XjPs8FJa8zSOO2dHLG6iF2yH2jBFD9vhhcYhwSYPe1SYvoWwU4Q3iY2YZTU8P14DBLPSbnoH4R9kQf9SaWwp4EOTm22AxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a317d9a3a1.mp4?token=TU1GNGmRRXPkik1qIeSfEkBHpAWpXzOKUHNG4SQvHq3aFk6aFFh0Cvw4T-SvTIWYio3iIimhA4EI8XJPegtGcDf8ZlmTA73qnRNB23Ppg3kPAMzS2npa5nRkWCNezsYNB4L7EBh_r3-KYxyZ-LYb9MEpYgjuH1AIJ74Nnz0Wa0b_PXlAyDFf3Hb37EWbq5EkqK0RMvvuOk03vWqr6ZpiwFvVrT9cyizRJ60ZO764JeqZ8W3TyA3ufrm-XjPs8FJa8zSOO2dHLG6iF2yH2jBFD9vhhcYhwSYPe1SYvoWwU4Q3iY2YZTU8P14DBLPSbnoH4R9kQf9SaWwp4EOTm22AxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه پاسداران در حال آزمایش مین‌های جهنده با انفجار هوایی است؛ مین‌هایی که برای پرتاب شدن به هوا و انفجار در ارتفاع طراحی شدن.
هدف از توسعه این فناوری، جلوگیری از عملیات هلیکوپترها و سایر هواگردهای کم‌ارتفاع برای پیاده کردن نیروهاست.
@News_Hut
| C14 News</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72992" target="_blank">📅 12:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72991">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a66d8a6ead.mp4?token=opJx1Qvp1kbp5uRCL_50BOrDCz-uXWBcw3nvSL8lVKMUde2-zvui1mAZmon5AUwI2aLnJ22n6_9U5y7ufBoJFQV8YbDBu-4NUTJ06xrbTkheHxrnPJ7FOqA34T3DVsbgJbDz39zw4iS-i6X_hwza4epbTwJhOxX9LlHHWxNzhgnU0a9U_wJeqF2EDYgCKF0i-MlJE0asFo93yQ8gvuaL8gCkeZ3c5t5595ZXr0cisz5diRxRj-7cosXYcI9A4hM_BeP0FepgD3bsxaOJcy7nlSd-YZWcO7zJS_lcMaJY4PZzpt4vd_9Wm2UNgFvbgOBzxebKvfNTeA5H_X1sR67Ktg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a66d8a6ead.mp4?token=opJx1Qvp1kbp5uRCL_50BOrDCz-uXWBcw3nvSL8lVKMUde2-zvui1mAZmon5AUwI2aLnJ22n6_9U5y7ufBoJFQV8YbDBu-4NUTJ06xrbTkheHxrnPJ7FOqA34T3DVsbgJbDz39zw4iS-i6X_hwza4epbTwJhOxX9LlHHWxNzhgnU0a9U_wJeqF2EDYgCKF0i-MlJE0asFo93yQ8gvuaL8gCkeZ3c5t5595ZXr0cisz5diRxRj-7cosXYcI9A4hM_BeP0FepgD3bsxaOJcy7nlSd-YZWcO7zJS_lcMaJY4PZzpt4vd_9Wm2UNgFvbgOBzxebKvfNTeA5H_X1sR67Ktg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی وایرال شده از سروش هیچکس، رضا‌ پیشرو و حسین تهی از قدیمی های رپ‌فارس در لندن:
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72991" target="_blank">📅 11:33 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72987">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JBH-ErFKmL5oR8E0PwI3kt70wok_e2CG4k09sE2Y9AxWGEQ090qEDDBFHHH0P8I7or__S-sx6cRRRaHdwp7dfP_vK2avSPHjS38n8BhWr1JUTzyTTwlZXvJYVgI5M_z-uxxt2cCO-khrdOmLxjLqgANEHc8i1D5BgVwVEZAr-17Z9s5c-o_-j_m7tvvX-42GFW8BXvNwE8Twie6AKzXNJzLqUBMAu3JGvfbpRX-_4F5MzMiMuZSWadkDploPP2cL7zOo1zFAV-0gV-8a0LSbnN9cDmLnZS7ndRxrelY19BM2l9gY1pV5HEoM_IEcsYJx8ESJHVZanZS23TfDqPKLXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sMDc3zTIoLuEPXL66yZWRMndjAPMWi3xWXhxCjqgpgn9Su2ymURlrtRx-xgDUpdl5-qeZ6EKIBO3sQyiaE4S2ysgXi0rrJIoP5aNtQRQNyWIZrK3vdi72xj6HMzaXhUSp_m9df1BpJJLegOMOg4gDSWevmBmjblADElP6RXDJ5d9jGp9YsHKQ-xmJvaMbaa9RSvYC9PCy7hEnl24lpuGCNVBjGNLW9YycO1VET4JOll5lX4z9mgHoTMXtBKo4UEJ-8zX9mcNNyx2GSPlP70OTE45rJPcg4obZA10r7Cx0s54VYgu0uz5bZ-SF1x8wXFdEkSQwvdV5_MXBjrwwJjHIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vNADk5whmQD5vM5mLpLayFY_NF02QdxHyk3X8GpFt2ck32FqaCGxphaYzRrcBrTNt-zVlQ-TSElV0Vk5lzPx-YdNry92kNI_QVy8KxSpWaPiNvhDnshEl4XEN2DvO13aXQdYvT5PGLN5ckPWZ7aHrcv9s9TotHLXU1i7Z5NV3OG_J_zlPIWmDVj3MGLdliZVd34vD_t1Q9nFJ1rLjiZChCwEPFgWilMRC36Im1m5F-W1_Hf48uzQMVWdVXRpklGlhe670c1GySfdmNK9sWq07y_38guE8AIhjePXD60H-HxW9XDQ7wGK_UJc2GabU2NuQRxS3Ew-zLpXjGeMVtkITA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78275c1097.mp4?token=uwkQ9-vIiP1iz5_CM5KKUnOOYI6Ga34VPJ--R6kbV9alk7O7eWQzu9kyTppJIxI1LmHxx_msglwmWBmnjAsPQ3DEg384PDS3eXdvcHjDoyitt9d7p6ZTxiKNRYZBDO1rTRmxT0HTlt-tNEiA92gXKR_oulFke_rNMA9zyRkN39oIURQVXxmS1iIrcn4RD0Tx9zUH92N2bwUvndrL_oNpPntfhxAN-K1qTjitgLVNHfdMK_Nu-A6OUHAJl9bm-JjvYhTETexvFzXGTTiIoV2yfCgEkd2udZMnJ5shAwB8NRevOB1fD0YBAkl_0wXSdTisBCOBQrEAelMSqgJXwTFUnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78275c1097.mp4?token=uwkQ9-vIiP1iz5_CM5KKUnOOYI6Ga34VPJ--R6kbV9alk7O7eWQzu9kyTppJIxI1LmHxx_msglwmWBmnjAsPQ3DEg384PDS3eXdvcHjDoyitt9d7p6ZTxiKNRYZBDO1rTRmxT0HTlt-tNEiA92gXKR_oulFke_rNMA9zyRkN39oIURQVXxmS1iIrcn4RD0Tx9zUH92N2bwUvndrL_oNpPntfhxAN-K1qTjitgLVNHfdMK_Nu-A6OUHAJl9bm-JjvYhTETexvFzXGTTiIoV2yfCgEkd2udZMnJ5shAwB8NRevOB1fD0YBAkl_0wXSdTisBCOBQrEAelMSqgJXwTFUnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو اعتراضات فرانسه از یه نیروی پلیس که خیلی شبیه امباپه‌ست فیلم گرفتن که خیلی وایرال شده:
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72987" target="_blank">📅 11:27 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72986">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72986" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/72986" target="_blank">📅 11:27 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72985">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GLZ__5r1AjHRIifJt49kD6ZDQvbSDKKUU0RerI5qEoHdU34nndUwkyhaJ9YEpID7VU1Hpk0x-7v_hvwYGqXlD3BEcG8ZxJ5AxpkPRUvrV73ko5v_LI6OyHVw8JOXmLP3Tcrw2pmI-uHxSf-0rI3Y0bcBne8HQ3pWeyx9rUSHhCzG6mG-XyV1SDyHVrDOkY8_Xgm-Fjo39aTpQz_vEQyp_KGlFIOSz8hkWSwgYZW4XU0wlbc-OYZi7xOgLAcDI-WAqCo3J5t0qFW-jsYnFUB4TsxHtnSYXqM5RpXKBmdi76bAcs1kH--9W4H8dAQXY1LCPja2r--VGwD6lI4djCWZZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
اسپانیول
🆚
مالاگا
وردربرمن
🆚
دورتموند
لیون
🆚
لنس
صنعت نفت
🆚
پرسپولیس
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72985" target="_blank">📅 11:27 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72984">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb4384f768.mp4?token=pxZGMsxjt111te7CycNDVwRR7IcRphjswCDSSuB70QHvGlAN9PUmemWe0miOz344eAPjH9qooP-Dk5jiBrXtolBpX335aRcwNQewgIbTaQdmVu1mC8yqWvTSwyW8SbOm91GgDoTutgNsKXbe7RAjSG6FNTAT3Z6V927rA4GFQsUZRgulfJA2jnLJdjlDan2_ItAfKZxAwqvKF1-T-e2Hc0trJwkbvsigPj0l3uVX3jLaPhkihNOdg0yXGd9MJo5SJXyXSqj_D75-3fyqEk55I9F3kSVbwAzGFXMejKExYoozyVSOM2AZUBsdxlEIkw6MQVMPtwzsdsCOusmMv5eWJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb4384f768.mp4?token=pxZGMsxjt111te7CycNDVwRR7IcRphjswCDSSuB70QHvGlAN9PUmemWe0miOz344eAPjH9qooP-Dk5jiBrXtolBpX335aRcwNQewgIbTaQdmVu1mC8yqWvTSwyW8SbOm91GgDoTutgNsKXbe7RAjSG6FNTAT3Z6V927rA4GFQsUZRgulfJA2jnLJdjlDan2_ItAfKZxAwqvKF1-T-e2Hc0trJwkbvsigPj0l3uVX3jLaPhkihNOdg0yXGd9MJo5SJXyXSqj_D75-3fyqEk55I9F3kSVbwAzGFXMejKExYoozyVSOM2AZUBsdxlEIkw6MQVMPtwzsdsCOusmMv5eWJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری
:
زنوزی پول‌هاش رو از کجا آورده؟ رانت؟
نادر قاضی‌پور ، نمایند سابق مجلس
:
بشین سرجات مصطفی، حق نداری به شیرمرد آذربایجان توهین کنی.
شما مردم آذربایجان رو نمی‌تونی مسخره کنی، حواست جمع باشه ما ستارخان باقرخان داریم.
الغدیر مال کیه؟ به ترک‌ها توهین کنی من بلند می‌شم میرم.
سپاه، تراکتور رو هدیه داد به زنوزی! من واسطه‌ی این کار شدم.
شما تو روز روشن داری حق ما رو میخوری.
تراکتور پرطرفدارترین تیم جهانه.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72984" target="_blank">📅 11:01 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72983">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf1beb1a36.mp4?token=EQewbmTcaAl3V_pprXrTtCvETlgvN-M_Vh4E10yyQnk91PbdaJrF3-Jq8aMvfB-6nIW8YLr25xQZ34u4LLVClA66VD7SCqPbS5uj70oUcnCWM2sYp_diA5dElu2Ajo6G8QKInZPrRhRkD4hlYJ-x_JAsVkaE7zjNXKOBsvggUDacnFIkkHfWXKSIKBQ1yj2xPkqf2NJNy34G14emhCK4w60ouCk_ir7qWKNrrhfKZ9n7F-cJ3fCNbu71pnX_XIX8l3zcnDPB16bbHIQ4IuTKkP_rZsd5QKwiZqDBjJ5MQU7FuwAfFGvItBgXyL7MnzoxHvx_8iOjvs2sHdpibOg7pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf1beb1a36.mp4?token=EQewbmTcaAl3V_pprXrTtCvETlgvN-M_Vh4E10yyQnk91PbdaJrF3-Jq8aMvfB-6nIW8YLr25xQZ34u4LLVClA66VD7SCqPbS5uj70oUcnCWM2sYp_diA5dElu2Ajo6G8QKInZPrRhRkD4hlYJ-x_JAsVkaE7zjNXKOBsvggUDacnFIkkHfWXKSIKBQ1yj2xPkqf2NJNy34G14emhCK4w60ouCk_ir7qWKNrrhfKZ9n7F-cJ3fCNbu71pnX_XIX8l3zcnDPB16bbHIQ4IuTKkP_rZsd5QKwiZqDBjJ5MQU7FuwAfFGvItBgXyL7MnzoxHvx_8iOjvs2sHdpibOg7pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری: گاو که دلار نمی‌خورد، چرا شیر گران می‌شود؟
مدیرعامل اتحادیه لبنی: اتفاقاً دلار می‌خورد!
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/72983" target="_blank">📅 10:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72982">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afdc8b6d86.mp4?token=FM5X-zpyPWeL10QGGDhigMQ_tV-ltWkcm5EHDFwPt-RLp03qoWsl-ssk82iNzKo27DOhytMXVlNTGhk2P2-azqUvEgYQQ3UI_s7NH-pq8QLIaoxuQ_rKC8tnMSAZVv0nH98BX8nTMQ7ZwqholFUIZgg0bSjbOnZj7VGnX8O5xhX6qS-aBXGOnWdaI7Idu15Cbu0rdLkXjoDHsFwDB8qKxRJIappGTJMuOvkb3qgf1qHl4ihJ1nTBG4wCm9MnTJibJdrwb_9kPfUUTZP2CbRk7nU3lg3yCf9ERqcdgApgb8qYcJnzK8f7qKbAiuORNLwczSXgNFzVBo706bK1okY7AjDtC-HxuNFOCV_4qNua5QxkR6dL81X8j5mCoBzH6RBMP0l7Tie6DAKYilJ5-wOCMQtpbhVxOJ58EVeonEWL4h68x8Uk9Cldxx7GBSND0GTUMvK64jM2ek8TUhBA6vmq9V6_CEoqrfBK2wIcyoWIHD4pIpduQIheU_cEQ2fG5dAkPCgEOGGt8tmQCGk88NPUNKVS_wB9lh9ETOnXTsDfxS19xdYeaSzyu94B-_5uz23jfih4GLfJxbVCSSVo47x086E4LStrbAyQiVfv-s1exMNb1seJG5cnsZq-UmxdYYIQhhwGQAxpSqNLEUHsqosHyHT47fPlPoEnAEjlJgMTtEk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afdc8b6d86.mp4?token=FM5X-zpyPWeL10QGGDhigMQ_tV-ltWkcm5EHDFwPt-RLp03qoWsl-ssk82iNzKo27DOhytMXVlNTGhk2P2-azqUvEgYQQ3UI_s7NH-pq8QLIaoxuQ_rKC8tnMSAZVv0nH98BX8nTMQ7ZwqholFUIZgg0bSjbOnZj7VGnX8O5xhX6qS-aBXGOnWdaI7Idu15Cbu0rdLkXjoDHsFwDB8qKxRJIappGTJMuOvkb3qgf1qHl4ihJ1nTBG4wCm9MnTJibJdrwb_9kPfUUTZP2CbRk7nU3lg3yCf9ERqcdgApgb8qYcJnzK8f7qKbAiuORNLwczSXgNFzVBo706bK1okY7AjDtC-HxuNFOCV_4qNua5QxkR6dL81X8j5mCoBzH6RBMP0l7Tie6DAKYilJ5-wOCMQtpbhVxOJ58EVeonEWL4h68x8Uk9Cldxx7GBSND0GTUMvK64jM2ek8TUhBA6vmq9V6_CEoqrfBK2wIcyoWIHD4pIpduQIheU_cEQ2fG5dAkPCgEOGGt8tmQCGk88NPUNKVS_wB9lh9ETOnXTsDfxS19xdYeaSzyu94B-_5uz23jfih4GLfJxbVCSSVo47x086E4LStrbAyQiVfv-s1exMNb1seJG5cnsZq-UmxdYYIQhhwGQAxpSqNLEUHsqosHyHT47fPlPoEnAEjlJgMTtEk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه میخوای بدونی رضاشاه و محمدرضا شاه پهلوی چه کشوری تحویل گرفتن و چه خدمت بزرگی برای این مملکت انجام دادن،
حتما وقت بذار و این کلیپ رو ببین.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72982" target="_blank">📅 10:01 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72981">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a22f39a3d.mp4?token=f4bNr4GYUZa68NYD07uLpmMUvSpAFLkT8Fv98bwnKMi_ifqrAy63b1W9UIgSiHQ6dcR-xbXX6q5afiQeuxY26QCpaAlUM37-sE0jCYnE_-cK3PFK4DUHh7nH5pTTXkbAutAE7lr03FCiI9RP8HL2cyR7HhQOnCkNtMmrx6MXZxIglCWLUmqgVA2bwfcrFGEoKGz0NhY7MgHzzcPKmc7lfMWhnCS39hDPr3PA53Tlgxo8VmE-fpr9LNg9YCIVu-AWZqbXfGsdXKyzptpexOTfoNhm95r93oeU7WdevhbZD7XDa6kox5xpKhCPksbz6LFjYdOqDaeArdjUhY18v0G9yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a22f39a3d.mp4?token=f4bNr4GYUZa68NYD07uLpmMUvSpAFLkT8Fv98bwnKMi_ifqrAy63b1W9UIgSiHQ6dcR-xbXX6q5afiQeuxY26QCpaAlUM37-sE0jCYnE_-cK3PFK4DUHh7nH5pTTXkbAutAE7lr03FCiI9RP8HL2cyR7HhQOnCkNtMmrx6MXZxIglCWLUmqgVA2bwfcrFGEoKGz0NhY7MgHzzcPKmc7lfMWhnCS39hDPr3PA53Tlgxo8VmE-fpr9LNg9YCIVu-AWZqbXfGsdXKyzptpexOTfoNhm95r93oeU7WdevhbZD7XDa6kox5xpKhCPksbz6LFjYdOqDaeArdjUhY18v0G9yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب تو گیلان، یه نیسان گاوی و موتوری باهم درگیری لفظی پیدا میکنن و بعد اینجوری موتوره چپ و نیسانه راست میکنن :
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72981" target="_blank">📅 09:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72980">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BAEgpjjdaRAtmAzsUWxrB57MHSi3qZ48k0x0DDeLtfqilCvW9llwhMlv2-XIpHbA9LS01oEqM_ZJxw2FdvpFU2RW7Jknjel3k5xsRDnMGqVZsFredn-yzSZBfR9vc2xIOjBkN2XFHJFXauGkpY27TEKRQKDhQJA57V_OT3t_mj7cn8uaVhbTEQsAT3d83WWfMQdImMnJ7o4oYOCXZo9F16pR5xVnLBMBxhsqLIIyzBLumGc7tx-MHkJakzhzqyLn2YCl5BLknLp4kK8ykj33FhVEiSqnecLRiQoVfLvoBJZu5S4stqT-zNnyKaJcv5Ie0bIwaelTynC4rzqrdmBDAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک‌تایمز به نقل از مقام‌های آمریکایی: پنتاگون طرح‌هایی برای احتمال اجرای یک عملیات سه‌روزه با حملات شدید علیه ایران آماده کرده که شامل هدف قرار دادن زرادخانه بازسازی‌شده موشکی و پهپادی ایران، زیرساخت‌های انرژی، مراکز فرماندهی سپاه پاسداران و تأسیسات نظامی می‌شه.
انتظار می‌ره سه ناو هواپیمابر آمریکایی در خاورمیانه مستقر بشن؛ هم‌زمان واشنگتن خودش رو برای احتمال ازسرگیری عملیات نظامی گسترده آماده می‌کنه.
با این حال، ترامپ هنوز تمایلی به ازسرگیری جنگ نداره و در ماه‌های اخیر پنج پیشنهاد برای عملیات گسترده علیه ایران یا حوثی‌ها رو رد کرده. او گفته پیش از انتخابات میان‌دوره‌ای آمریکا، مجوز حمله رو صادر نخواهد کرد.
مشاوران ترامپ درباره حملات احتمالی اختلاف‌نظر دارن؛ برخی تردید دارن که حملات بیشتر بتونه موضع تهران رو تغییر بده، اما برخی دیگه معتقدن یک عملیات محدود می‌تونه فشار بر اقتصاد بحران‌زده ایران رو افزایش بده.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72980" target="_blank">📅 09:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72979">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HuRaU37p0WcAFAFIXJNCNyjYSqUpg1caPlRFHZU7d0BAaM8f5derMXwQDsdOiYuchbotYmclq9Lyh0rePx4hJMjpMEyin-funW4Dcs8IV2LZ5KR8_sWRMLC4iNIK_u7J5iLuCI6sxIhhueV6zy0ZrNWkWynct53KWfixRME7hpGVASuyYSbMCCMtGVfuJdylWM0cjv3NlpCBrh55w6NwBL_zVBNd_mjsXbJqgp4udyPe1ZnHtljKf2_VjlRZoOVF_AGboyayuV9YV9QQhWWLUe3sPIVAdrg6SR1UA0Gy4KzV1tNouwpvAUU6mADX56syj4EtKN9Zc59duwVcHFufiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا:
«وزارت خزانه‌داری با قطع منابع مالی، رژیم استبدادی تهران رو از پولی که برای جنگ‌افروزی در منطقه استفاده می‌کنه، محروم می‌کنه و به افشای افرادی که به فروش نفت این رژیم کمک می‌کنن، ادامه می‌دیم.
هیچ‌کس که به ایران برای دور زدن تحریم‌ها کمک کنه، از تمام قدرت و اختیارات وزارت خزانه‌داری آمریکا در امان نخواهد بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72979" target="_blank">📅 07:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72978">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ei9ZPNEf5GIdSo6JJc-jZiISgNlNmbRcd3lh_KEM_B4113Yv5r9AKygZH_YtKIzNMAiCuQAf65SkOYuD8xG0Uio2VdjVoAjDKWBxH6DkQ1vKXNx7yhrFa7IFmXdixwxGvPPFsKoASX-qzIZ-NuScjjrKb9KbhMURW4lKJV8dA06w76P5RoFY_dm__GOXqFhel1vOz6pWPRLd6jadmHkJkO-jI-0uWSD_zioG3yMx4J6R4RvKY3uWIoQVoNrsRgmecYrayjyTxAzfc1KNwFG66MRIONfWDLElUtFsq5ZkhgZ0BvYUBEcglhYt1XFtw5lFr3UKqk1haeDeak3PDk8SZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحریم‌های جدید آمریکا علیه شبکه ناوگان سایه ایران
وزارت خزانه‌داری آمریکا از دور جدید تحریم‌ها علیه شبکه باقی‌مانده ناوگان سایه ایران خبر داد؛ این تحریم‌ها در چارچوب کارزار «عملیات مطرود اقتصادی» (Operation Economic Outcast) اعمال شدن.
در این دور از تحریم‌ها، ۲۲ کشتی، ۲۶ شرکت و ۶ فرد مرتبط با شبکه حمل‌ونقل نفت و محصولات پتروشیمی ایران هدف قرار گرفتن.
این تحریم‌ها اپراتورها و شرکت‌هایی در هند، ترکیه، چین، هنگ‌کنگ، امارات متحده عربی و بریتانیا رو هم شامل می‌شن.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72978" target="_blank">📅 07:35 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72977">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72977" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72977" target="_blank">📅 01:57 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72976">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhikv-X8OLtGPY_UobpEx7VXlYPftnU9EzOAHEYmEB3AgQEL0_awR4-u75WgxmEAC1YPye89_CIJDW9T_ZiDka1xQYwTCaqFOw_uKb68zP5Y-Pw0lydLdXztil7haRPhttxH0m0IC7_DE2oJBa40wVqP4HHdKQWnNLOVW7DW0pZwse_9wbNGkXy8demBl_xl8hUp3gcOzWI_QVtdDehQb3CD8HW9G68KGxO8yj7pEGMrIe73DoxnAdJcWHAoZScM4SXOgJ_GSzVQ3xoi06sLwskUmElnmKgjNe-2xLIIou4jI2SlamR8t4H6CrMpQcK1dEhXFHSx1dTag5ywNcoelA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول: ۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم: ۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم: ۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم: ۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72976" target="_blank">📅 01:57 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72975">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLW2Yf_OK-fBN6HjcHrPkCcWl_SrrGWcjo32hM0Yx8YuKvDyVysLPd9ru7ZQByZG9psOtqi2p_-q0AJpa4NMnwTGMVNZwFhZb4hXvoaSIjHw3LXez3tU4FARQEfXSalD1TGnT_KcPXhvW5YdPMf7ME3y7zPDhqaPTfy52NpMwa8IIy7eyWjs9hAwoTvdzYgXWNEvxB8KkppS8zCUrcmCc-sQYztMIYymYzNuD5C7BE1fCpLkNOXZMbyOCLWpVLptyEydosIpRZAB3ze-X2Mw9F8EXPtlSfIO0J4p2OtjcpKJnDc2dUqZXjIoq-cwyMnbSga5ce10UcOHksyoCmyAxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی لشکر ۸۸ زرهی نیروی زمینی ارتش:
روز پنجشنبه ۱۶ مهر، مینی‌بوس حامل کارکنان این لشکر در محدوده نیکشهر، سیستان‌ و بلوچستان، هدف حمله مسلحانه قرار گرفت.
بر اساس اطلاعیه رسمی، در این حمله محمدرضا اوکاتی کشته و سه نفر دیگر مجروح شدند.
حال‌وش از تفلات بیشتر خبر داده اما هنوز تایید رسمی نشده.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72975" target="_blank">📅 01:25 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72974">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mE-zwHyJ1eQp63rpdC_-89eU-ZZ5tmFQMQp2M3xOR_lB2JM74LCPlh4gQf_DiigBi-CyknLtrXf-sxMngtdzAoWMGGQBVuik1Af1Dzg0aR4igftPw5lOiW_E-SndKpLKXmY1R2TLAvpSBhWV3jgV-eOoLyDEt3EXxiVX_XdU60KZUvL_m_dXRHt6EQbO_NexDW5fmSGkrdGhHuEECPhwAIRuQoiXiHRUcEm361LNNfBc6tBLcIocrDjYP7vXapMJ8m_kLF7eS2TdUBKT2sMwQrb3dAL5UPrEeSx6IkJF5gdS5GoBSLlAe4mQWYVsqTMufErLBNvgrzw92cI3vBEaeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در هیچ زمانی پیش از انتخابات میان‌دوره‌ای آمریکا در ۳ نوامبر به ایران حمله نخواهیم کرد.
ایران سلاح هسته‌ای نخواهد داشت!»</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72974" target="_blank">📅 01:17 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72972">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f430f2b57.mp4?token=I_qdcyyuBo77d0fj8R4Oi-Ymhq7t-6bBsYCWzw3XPRIHyHok4yRQUtan0qsjJZWdLiO-3kIa-X6EZcPyGy5hF_UGxcmeyNNiBQC7YD7Dv1DH3n830j--lhkkLDDbQBeNsz16WxmViYAYxtGGRlNxHMMlMu9Il1nHBlBVgfDyljtmf7hKG1PiIPkbzEYdaxvT5b5yoUk6iHB708SZC99YCC-diGyRFWu-Fn1gFQLIc39KpjpEyjxBMkwla9feoILBEta1Ijwu2h0DYZlrpbCJHMj8abMqy2dWuwDMSYX7eJ3Z2aVwrV_DhNcaA15LdBJLBeAkUxe-hYbxvhcolxEe950yeTF29xIZEe01zfkgn3K_Y9Ruv_YbTHQV1FlTnm3j-3yUkcqTMK96dpEcuARjySjQ8lyj1x8oJeaOI8Nz_O7UeL2r4V6WEim4zguakAWCVLxbs-46QQiXbzMFkx-0pscHcWGflXymie8Z8pLhljfXw3ixEqFKL2iuPjEKvTSDl7v-AMP2miMpafXkCP8uqX3Td_Bc7qIq2Q1KR66Bbn--FZrE2db-bmN6uyA7wc7EHSH_aaJ0pokXGQZfHv57TOzac79aZ_EFioXzsLeeLJUfa8Peyj4RFvZTS8IZ6XiwoqRf2uoLDlbETS_oQRFOM19dyoFkr0y1enR-NPEh01c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f430f2b57.mp4?token=I_qdcyyuBo77d0fj8R4Oi-Ymhq7t-6bBsYCWzw3XPRIHyHok4yRQUtan0qsjJZWdLiO-3kIa-X6EZcPyGy5hF_UGxcmeyNNiBQC7YD7Dv1DH3n830j--lhkkLDDbQBeNsz16WxmViYAYxtGGRlNxHMMlMu9Il1nHBlBVgfDyljtmf7hKG1PiIPkbzEYdaxvT5b5yoUk6iHB708SZC99YCC-diGyRFWu-Fn1gFQLIc39KpjpEyjxBMkwla9feoILBEta1Ijwu2h0DYZlrpbCJHMj8abMqy2dWuwDMSYX7eJ3Z2aVwrV_DhNcaA15LdBJLBeAkUxe-hYbxvhcolxEe950yeTF29xIZEe01zfkgn3K_Y9Ruv_YbTHQV1FlTnm3j-3yUkcqTMK96dpEcuARjySjQ8lyj1x8oJeaOI8Nz_O7UeL2r4V6WEim4zguakAWCVLxbs-46QQiXbzMFkx-0pscHcWGflXymie8Z8pLhljfXw3ixEqFKL2iuPjEKvTSDl7v-AMP2miMpafXkCP8uqX3Td_Bc7qIq2Q1KR66Bbn--FZrE2db-bmN6uyA7wc7EHSH_aaJ0pokXGQZfHv57TOzac79aZ_EFioXzsLeeLJUfa8Peyj4RFvZTS8IZ6XiwoqRf2uoLDlbETS_oQRFOM19dyoFkr0y1enR-NPEh01c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه به مواضع گروه‌های کرد در اقلیم کردستان عراق حملات پهبادی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72972" target="_blank">📅 01:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72971">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">نیویورک تایمز: انتظار می‌ره سه ناو هواپیمابر آمریکایی در خاورمیانه مستقر بشن؛ هم‌زمان واشنگتن خودش رو برای احتمال ازسرگیری عملیات‌های نظامی گسترده آماده می‌کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72971" target="_blank">📅 00:49 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72970">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l8zs49_iTwZgBzD9d1OCrJIw-1FhVw6M2r4721KG2Jw5FAl5-HW2cQoMpYOaAojjKE_VuRQ4XQMnWxGw5tiCwDlHBv8i9LBTQS77RtDghRnQn204KFbfiUvfYAifs_xEpF2vnW7-Qd1kVsyFi17vwkx52Rk6FIQaqL_3f4j1zwXYK2umcgq12xFhIGi3aFlIERzQ5JgYnFWP94HvyyI2yfn7RePief2mtaozk1Pi_08xP7FZUGRnzp5AFnM9gpZVNZguJtV3lLTItqQMNUPzhmaXzMr5dYjleakYO0UBR6KpR_8Ua17PVeNkZ2i5IBw_ePrxSQh9VYcz_TRPw7inFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
«رسانه‌های جعلی و دروغ‌پرداز دارن این‌طور القا می‌کنن که من از دشمن دعوت کردم به سن‌دیگو و لس‌آنجلس حمله کنه؛ در حالی که منظور من این بود که افزایش موقت قیمت بنزین، بهای کمیه که باید برای نداشتن سلاح هسته‌ای توسط ایران پرداخت کنیم.
حالا اگه می‌خواید بدونید بهای واقعی و سنگین چیه، تصور کنید اگه ایران به سن‌دیگو و/یا لس‌آنجلس حمله می‌کرد، چه اتفاقی می‌افتاد؟
تمام حرف من فقط مقایسه بین کمی بیشتر پول دادن برای بنزین، آن هم برای مدت کوتاه، با حمله به شهرهای بزرگمون بود.
همه اینو می‌دونستن؛ رسانه‌های جعلی هم می‌دونستن، اما بازم ادامه می‌دن و می‌گن من از دشمن خواستم به دو شهری که دوستشون دارم حمله کنه.
حرف من کاملاً روشنه، اما این آدم‌ها منحرف و فاسدن و فکر می‌کنن می‌تونن مدام به انتشار اخبار جعلی ادامه بدن و از زیرش در برن!»
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72970" target="_blank">📅 00:35 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72969">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DyV-KMM08E-5wQcCTvnJor5bF22o5_zdPOp5zpwfehKH-GCoxlrJgNd7cH0WGhIQyH_knRY0JqChGZWEuScxV8R2z4zNbLHBDvutCpY_cJTt7SeGf8qal4sEXvBSrIGC5IXmZOdJ1xN3hbNL2AIv-QV6uUsNIE800WmWBerb4QSsconjU1-Q1vF_B98O8xbeVJTZxvAYjAACgBAdGlcTLeu5rj3d00t4pe_FpyTDf5Cg3SxgvL67SZ9XLb_mjai0bF8U4uxh26u16_j8vWmn89ffAkpZ8uFplWXAI5xyzrHUeZOTGjWauOcvGfHOp9EaZDmyCn3zOta-RmJvwpkA3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز 8 October روز جهانی لزبین‌ها بود که به اساتید اهل فن تبریک میگیم
🐸
🐸
🐸
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72969" target="_blank">📅 00:16 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72968">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a1b884ba8.mp4?token=dYuveN5vVDAoKzWXNj5l0h8HwPOPToMtMmUEA5joHfDQsKEdUIVy4dA-x1MiyVYFWBtSQO_WR6AbOsBlcz0YHjZXUijUHn1kNhF3jI1YkKZ_q2E-FMNOD-l8PPV6CVvChPqskZ9uJI32jcxSgVK_sTsVXQ-xId9DccZdQ4ENSOu--yQzkn6KYiTgTQauunygQLiEsFRaim9ng3IPMTRFOrraxlrr4rGoxAuIhImipioo7HPCQ891NlDMgPEWVaI9ZRtSnSilK1duxfQDOgNh22ss5biv8P4RoG8EozcUybL2toF1WUzS4OfLekDYUagWmHHMdVwxQWylWSgg_3r19w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a1b884ba8.mp4?token=dYuveN5vVDAoKzWXNj5l0h8HwPOPToMtMmUEA5joHfDQsKEdUIVy4dA-x1MiyVYFWBtSQO_WR6AbOsBlcz0YHjZXUijUHn1kNhF3jI1YkKZ_q2E-FMNOD-l8PPV6CVvChPqskZ9uJI32jcxSgVK_sTsVXQ-xId9DccZdQ4ENSOu--yQzkn6KYiTgTQauunygQLiEsFRaim9ng3IPMTRFOrraxlrr4rGoxAuIhImipioo7HPCQ891NlDMgPEWVaI9ZRtSnSilK1duxfQDOgNh22ss5biv8P4RoG8EozcUybL2toF1WUzS4OfLekDYUagWmHHMdVwxQWylWSgg_3r19w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به تازگی دخترا برای پسر خوشگله زندگیشون این حرکتارو میزنن تا دلشو بدست بیارن:
بخاطرت همه پسرا رو آنفالو میکنم.
ساعت کاریتو هم درک میکنم.
حتی عکس دو نفریمون رو میذارم بک گراندم، کی دلش میاد اذیتت کنه خوشگله؟
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72968" target="_blank">📅 23:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72967">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9487485a01.mp4?token=fadDv9f5uyk1P7HTlRL75WAzjlihZ1N-bLMAMh9pQ9Y7cTbXmPbJ0UuiiverlYJY40I3kpEfGmx_e9G8KV6IPOQUFgvRXZ8rrKi2N5BdXB0IEmtzKZsU4JiSNJZ88NGB6h0KhiLNHEdC6QfwTh3kHhLTsaQCJRvF_rqT3n9tuR0wphJP0eAYA_HmPdw8CYueVMt8jwpQ94HjJInludMb8_Cnq9gN5F_Vu30RXPAC7OfisW-5b0sZObHOBMEU7hBUNKFDPCWnNCWfITYRgtbIAnHW71irueR65fCDBdqKviFLhkmWHDa_8pZMIfSXpfg9WnAZM0esVSN4yeJeQ1PaXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9487485a01.mp4?token=fadDv9f5uyk1P7HTlRL75WAzjlihZ1N-bLMAMh9pQ9Y7cTbXmPbJ0UuiiverlYJY40I3kpEfGmx_e9G8KV6IPOQUFgvRXZ8rrKi2N5BdXB0IEmtzKZsU4JiSNJZ88NGB6h0KhiLNHEdC6QfwTh3kHhLTsaQCJRvF_rqT3n9tuR0wphJP0eAYA_HmPdw8CYueVMt8jwpQ94HjJInludMb8_Cnq9gN5F_Vu30RXPAC7OfisW-5b0sZObHOBMEU7hBUNKFDPCWnNCWfITYRgtbIAnHW71irueR65fCDBdqKviFLhkmWHDa_8pZMIfSXpfg9WnAZM0esVSN4yeJeQ1PaXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مطهرنیا: آمریکا هدفش تغییر رژیم هست اما یواش یواش چون نمیخواد مثل عراق بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72967" target="_blank">📅 22:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72966">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f19a7b8871.mp4?token=ACAn3CiTM58Cp2gvmcO_7IOciEItMEbbWzLBg3hhCrYUeprRvSg2CdasJh2ZzUTqNKorZSW4OHV2SE0brEzOCQN8gTDtcIQGxwqmmMY-SehnypAMmCS8hefzq8Y4mqO-dPpiVnUOcmonAi9qwQ-5XzU6jcNzZi17IsaK15Wyr4vVldj2Dow3TG0xcNaS8fd0GRAX6ndeV-oVMvTTdEtB_GLURxoK1MooBXut5-JHuZvxLmYM8YsDuHzqPcJiPENXgZvLIq-ZLLhBCG1g921tp4ebtbrxmRnM7OV7ww5CSR-ytaOI802i3gFG3wbakmWIjND9pREuA5rL3LptASJBzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f19a7b8871.mp4?token=ACAn3CiTM58Cp2gvmcO_7IOciEItMEbbWzLBg3hhCrYUeprRvSg2CdasJh2ZzUTqNKorZSW4OHV2SE0brEzOCQN8gTDtcIQGxwqmmMY-SehnypAMmCS8hefzq8Y4mqO-dPpiVnUOcmonAi9qwQ-5XzU6jcNzZi17IsaK15Wyr4vVldj2Dow3TG0xcNaS8fd0GRAX6ndeV-oVMvTTdEtB_GLURxoK1MooBXut5-JHuZvxLmYM8YsDuHzqPcJiPENXgZvLIq-ZLLhBCG1g921tp4ebtbrxmRnM7OV7ww5CSR-ytaOI802i3gFG3wbakmWIjND9pREuA5rL3LptASJBzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست، وزیر جنگ آمریکا درباره ایران:
«ترامپ رئیس‌جمهوری نیست که بازی دربیاره. رئیس‌جمهوری نیست که زمان زیادی رو تلف کنه.
ترامپ دنبال صلحه، اما حاضره برای رسیدن به صلح، به شکل واقعی و تاریخی، هر کاری که لازم باشه انجام بده.
ایران با داشتن بمب هسته‌ای، اتفاق بدیه؛ نه فقط برای ما، بلکه برای کل جهان.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72966" target="_blank">📅 22:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72965">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1432e3f5f.mp4?token=cV3C_VOQeTdiXlZ8L6H_EoRWO0UXdNnm8D4ooe1O7KpgOC3n7u2EtrKCa_OB_hs6z6Nh3Tdd7EAmpX3yz7XEUFYjdEGbNSLrCTlN4w1Ki7ni10Y86XxWjsEDdJG7SN1L09GlB98npt18KRHYkE_nj0xP6QRLovP3diW1nZLfX-waeBrDWQUzc2zgIEWi-NKFLP1FRe73ZX78Ckn2vUSVAstaMOnJEBhp3OGA70jhI92M6-7vOlj64nB781CcsNj_6asiABBTi1gxVSqFDcjWBj4iev52UH2Ps4-_expvDu7kHAdPW4yV3DKbp6oj_v7SuPMtYVHvs-IJpi2Nrjb0wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1432e3f5f.mp4?token=cV3C_VOQeTdiXlZ8L6H_EoRWO0UXdNnm8D4ooe1O7KpgOC3n7u2EtrKCa_OB_hs6z6Nh3Tdd7EAmpX3yz7XEUFYjdEGbNSLrCTlN4w1Ki7ni10Y86XxWjsEDdJG7SN1L09GlB98npt18KRHYkE_nj0xP6QRLovP3diW1nZLfX-waeBrDWQUzc2zgIEWi-NKFLP1FRe73ZX78Ckn2vUSVAstaMOnJEBhp3OGA70jhI92M6-7vOlj64nB781CcsNj_6asiABBTi1gxVSqFDcjWBj4iev52UH2Ps4-_expvDu7kHAdPW4yV3DKbp6oj_v7SuPMtYVHvs-IJpi2Nrjb0wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست، وزیر جنگ آمریکا درباره ایران:
«ما دنبال ملت‌سازی در ایران نیستیم. نمی‌خوایم تعداد زیادی نیروی زمینی وارد ایران کنیم و کنترل مناطق رو به دست بگیریم.
ما فقط می‌خوایم به اون
رژیم، رژیم اسلام‌گرای دیوانه،
بگیم که شما هیچ‌وقت سلاح هسته‌ای نخواهید داشت.
حالا اینکه این اتفاق از راه آسون بیفته یا راه سخت، انتخاب با ایرانه؛ اما در نهایت این
رئیس‌جمهور ترامپه که تصمیم می‌گیره.
و می‌تونم بهتون تضمین بدم که اگر اون لحظه فرا برسه،
اقدام آمریکا سریع و قاطع خواهد بود.
»
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72965" target="_blank">📅 22:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72964">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ea8ff8855.mp4?token=h0zZ1upZuPOZF8_WNKj74PhXVdc0qwsWZgbEWZHkTLs_-b2HyKDrGBhkitA90zoJXXXekb14VVDHf171WUPIYqgJn_c0299daGgnKTlk4CpwS958ePJnLoNaFpb8Z-CWHU-0YPhp9tn04flaJou-RUiH_QtsZCRCIzrji57RfVRZg3tjgD7CkzoATYgTDW8IwWfoqdSTrV0tYZx92XK7XEdb8BNcgc6gkgnSBmvG2kDz6oCOD8uRMgVK5VJ01n_zElsmFX8YkEfeDRld2YvEDviAlJuNNcMR9V0xqy5NCvA7TEu8VReEL7w3Bfkq1Emq-hXu3PF6oXXlWqoYN3dSng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ea8ff8855.mp4?token=h0zZ1upZuPOZF8_WNKj74PhXVdc0qwsWZgbEWZHkTLs_-b2HyKDrGBhkitA90zoJXXXekb14VVDHf171WUPIYqgJn_c0299daGgnKTlk4CpwS958ePJnLoNaFpb8Z-CWHU-0YPhp9tn04flaJou-RUiH_QtsZCRCIzrji57RfVRZg3tjgD7CkzoATYgTDW8IwWfoqdSTrV0tYZx92XK7XEdb8BNcgc6gkgnSBmvG2kDz6oCOD8uRMgVK5VJ01n_zElsmFX8YkEfeDRld2YvEDviAlJuNNcMR9V0xqy5NCvA7TEu8VReEL7w3Bfkq1Emq-hXu3PF6oXXlWqoYN3dSng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگست درباره ایران:
«ایرانی‌ها فکر می‌کردن توی تنگه هرمز اهرم فشار دارن؛ ما این اهرم رو ازشون گرفتیم. دیگه چنین اهرمی ندارن.
ما کنترل تنگه هرمز رو در اختیار داریم.
»
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72964" target="_blank">📅 22:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72963">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0b0e0a9c6.mp4?token=WV9mYhoOvXy4jsu96mdnSE16od7YmsigNl0aFEDLbOgMI8T_-U0XWTbmAegcC4E7NsXuCcRBqXsvHoHjwU0N_tgAFt30Sn9AUpij3C5n9cW2NehTdDXxMNX7bXryG1nSQLAdXIi2vyengts22JPld74gycs2Awm3dP9eT8H9Ud-PnNeewJbZb30M1ycUdRjs4NAZa4BBOoC6_pqlvNLpXD3_Z8Yox_-8cFfbJZnWXMtVZVanwI1I2R71jtdjpqq80oAl5zGXi-0fHYJrphLbrInKNEkMO3sQGS27jra28UcJ1KEsUURQ_ITU27FMNAgQ4oMSVlpubZKgdBHKettIog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0b0e0a9c6.mp4?token=WV9mYhoOvXy4jsu96mdnSE16od7YmsigNl0aFEDLbOgMI8T_-U0XWTbmAegcC4E7NsXuCcRBqXsvHoHjwU0N_tgAFt30Sn9AUpij3C5n9cW2NehTdDXxMNX7bXryG1nSQLAdXIi2vyengts22JPld74gycs2Awm3dP9eT8H9Ud-PnNeewJbZb30M1ycUdRjs4NAZa4BBOoC6_pqlvNLpXD3_Z8Yox_-8cFfbJZnWXMtVZVanwI1I2R71jtdjpqq80oAl5zGXi-0fHYJrphLbrInKNEkMO3sQGS27jra28UcJ1KEsUURQ_ITU27FMNAgQ4oMSVlpubZKgdBHKettIog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایلان ماسک:
«ایلان،
توماس ادیسونِ دوران ماست.
»
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72963" target="_blank">📅 22:01 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72962">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B13O2ycNmI8rHBgDecUvEULcXsLTFzvER6NZEVcuITss84Pz7po5NLhy6OkpjbLECQBcnZoNFkkIpx-KxDMdrBFCK2-BM2ybLtC2IM0IPRZXWaouLrwXcgKj2srAQfmJOfvwA52QoQEVc0VRnOgGOR2vAo2U4rHuEblxIJSxIdbnJggAldOUGJcCvN5O0vWVbzB1wax0ZMGpVA0YtZXuMy0M-gekztN_8JQG_Hxl3JfZADR0Lemk4nWtzcvQX0VsMASgehGpVqXt-9LbsFVuHF40fefBRHqyM5LiUOq9fkJnAj7CLJFqIdgQqNvnTxYpvmZ7uwbtGPq9LkpcOJkxSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد ارتش اسرائیل، ژنرال ایال زمیر، روز سه‌شنبه به مقام‌های ارشد آمریکایی هشدار داد که ازسرگیری جنگ با ایران طی سه هفته آینده ممکنه اسرائیل رو مجبور کنه انتخابات ۲۷ اکتبر رو به تعویق بندازه.
«زمیر نگران بود که ایران در واکنش، اسرائیل رو با حملات موشکی هدف قرار بده. این هشدار بعد از اون مطرح شد که مقام‌های آمریکایی او رو در جریان آماده‌سازی‌ها برای ازسرگیری عملیات نظامی علیه ایران قرار دادن.»
«ترامپ از اون زمان اعلام کرده که آمریکا پیش از انتخابات میان‌دوره‌ای ۳ نوامبر به ایران حمله نخواهد کرد.»
@News_Hut
| Axios</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72962" target="_blank">📅 21:50 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72961">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f999e97f3.mp4?token=WkoiABdpoqBxsa-q1Y8ah4LSPqtUURTfRfMPcp2zDYNEGJXcM9odKvEGlniqAF4mmCbA0BHpD4Xtb7bCejA3x32-Gz4JikwGf4Gsk-tmeC5cmRLIxhnJghAiz5ex0J-ixxvemiZI1go06_IX0NhhGtPVrpu-l-sITYrfod1hjUZjLBisI2Wh9OfReqbhpmdsCNlg0Y7g8LCfQU_74OfwCaDjuKDBs4jYRvA9DcAFPg-4C5TAUCOe60pt9MYeuQgM-ttQfKDohySC6UDqbVWJhB8GHlWXU65UlQl5JqEmIKtKiYTVX0iMDZ2eWZlrZ9P3J8MFyjHzC7MKZXRJp0m3ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f999e97f3.mp4?token=WkoiABdpoqBxsa-q1Y8ah4LSPqtUURTfRfMPcp2zDYNEGJXcM9odKvEGlniqAF4mmCbA0BHpD4Xtb7bCejA3x32-Gz4JikwGf4Gsk-tmeC5cmRLIxhnJghAiz5ex0J-ixxvemiZI1go06_IX0NhhGtPVrpu-l-sITYrfod1hjUZjLBisI2Wh9OfReqbhpmdsCNlg0Y7g8LCfQU_74OfwCaDjuKDBs4jYRvA9DcAFPg-4C5TAUCOe60pt9MYeuQgM-ttQfKDohySC6UDqbVWJhB8GHlWXU65UlQl5JqEmIKtKiYTVX0iMDZ2eWZlrZ9P3J8MFyjHzC7MKZXRJp0m3ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیلی معلم به دانش‌آموز در هنرستان؛ سقوط اخلاق در نظام آموزشی.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72961" target="_blank">📅 21:35 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72960">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">در هیچ زمانی پیش از انتخابات میان‌دوره‌ای آمریکا در ۳ نوامبر به ایران حمله نخواهیم کرد.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72960" target="_blank">📅 20:43 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72959">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G2KPj_8xzx92aPoWLItOtuFP0kQQp-YB2z8iSr-U4V9JhL-PhVdnqmyNQJYdmUJ5yFNVfAuSDCEbNhohvmiKtEhgrKB3VdTu5mdddxVoXP_ZvqTthWHAYUH_x9R0nL0L_CBfsr6TBW9m8ZSNiVrSCy9PzA8LD_2r5bIzEvVH58kVEZSZeu4kAyqLhSjnH45Yu4jhYZUZuUrXkbToX_1_al6tcXyO0weTnZP5DzKKhW1lGALER99P01t8alji64HD5Z5ZKtJlaI1pAaZj8ui9FnGWu-Cg1NIbjqPzY4p5Zr1wHju1tcxJLZ_pcE7-F8VJk1VdyCAk1GlHwkj9sNuiFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوووری
؛
ترامپ درباره ایران:
«ما در حال انجام مذاکرات سازنده‌ای با جمهوری اسلامی ایران هستیم.
می‌خوام برای همه روشن کنم که با وجود اینکه ایران هم از نظر اقتصادی و هم نظامی در وضعیت بسیار بدی قرار داره، و با اینکه محاصره همچنان با قدرت ادامه خواهد داشت، نفت با رکورد بی‌سابقه‌ای از تنگه هرمز عبور می‌کنه؛ فقط دیشب ۲۲ میلیون بشکه نفت از هرمز عبور کرد، بدون اینکه حتی یک بشکه از ایران وارد یا به ایران ارسال بشه!
ما در هیچ زمانی پیش از انتخابات میان‌دوره‌ای آمریکا در ۳ نوامبر به ایران حمله نخواهیم کرد.
ایران سلاح هسته‌ای نخواهد داشت!»
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72959" target="_blank">📅 20:32 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72957">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SrfBIoAaANWeiMUTo87h0aITz7A5wBwW6dJ80HN6Mxwvd6TmlsUbC3fFJKBYGihGEmNxl-r1Ugs-kLtVRgkekUMtDGt2aIfAO7XEd362uqKPOGzrDcGXlxEoEJytWrLkLfB-mGYlv7E8wOfedZvDMv04VXGeVV1Xm5ElM7-GeU3izGe1aw0LsUxAa2KCWtT-hUc8os_dwUmKrHTyd7921zPDkevIQkiWyjdaKUeRl6MhvR-xSKNnf-NRAxn_x2Wz9fO_Fezp3EfZQY9JcIwx76B2lWqDQRKvMlexizs1gu5AxNXChOTxcz5q2DDbAlE7vpTldvfENA8mS4jkawObJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b78d43505d.mp4?token=YVGg8BRpD9vnFq9u3gpclX3NshgwnGyFPzd38UzQznzGat_R9UYiJ2cI6HEGB9BAldas7QzC8NmyHuoXZWErdsrj8Uf7O8mz6wwWX16jybOt1qcyAydoCUfQ4G5jVpgWw4dKrwKAnUMAimYz0wgguRMzCL5O-ryAhmPlMyF3CX55TUOM9skB_EjHy8yMsl266NRefDultuveSqvv4uMjN2YkMIiolGO0teRUtgjZpBo4QI8WEpgEzE5BBXWoGI92IsH3tW23pN6meUzld7L388tacKks8Zn5K1j9Y8ZdRFdnByfuOSaC6-7D0PdA-lhXnSxOWeokrLJ3E8fmI4c6-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b78d43505d.mp4?token=YVGg8BRpD9vnFq9u3gpclX3NshgwnGyFPzd38UzQznzGat_R9UYiJ2cI6HEGB9BAldas7QzC8NmyHuoXZWErdsrj8Uf7O8mz6wwWX16jybOt1qcyAydoCUfQ4G5jVpgWw4dKrwKAnUMAimYz0wgguRMzCL5O-ryAhmPlMyF3CX55TUOM9skB_EjHy8yMsl266NRefDultuveSqvv4uMjN2YkMIiolGO0teRUtgjZpBo4QI8WEpgEzE5BBXWoGI92IsH3tW23pN6meUzld7L388tacKks8Zn5K1j9Y8ZdRFdnByfuOSaC6-7D0PdA-lhXnSxOWeokrLJ3E8fmI4c6-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر تأیید می‌کنن که یک هواپیمای شرکت هواپیمایی سعودی (Saudia) که در فرودگاه بین‌المللی ملک خالد ریاض متوقف بوده، در حمله موشکی اخیر حوثی‌ها (انصارالله) هدف قرار گرفته.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72957" target="_blank">📅 20:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72956">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fee1bad71e.mp4?token=GRMKqluM8FliqMC-rVes7iNX5WkkNcHxM5THIIcUZzNFaV31hiCWZa0sSDxYuwYlWzLvQM7WPLQoXabzHe17yyZfWw8GzpdmXJJRNW_r3fA6riaCQjPccThV1Y_DQBVaMF6AGE90cZBQdNc64zRsUCbL2Z54Zu3PBhZOvhQqlwjMPN7X4tuKgXY3BJmKAlr-kRFwEXmpiSaq5YSfagcHc7CKj92o1gqoJvap58wsIl7ckviTn7RsD2f_jGhDj-moCEip9IV6XeQ_SgMep6Z4GnRmm-ad3o-ZcRDQtP6rcrpA55WGALZmdnVHFDZS7ad3rqT-QwA1tbOwbSoy5udsrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fee1bad71e.mp4?token=GRMKqluM8FliqMC-rVes7iNX5WkkNcHxM5THIIcUZzNFaV31hiCWZa0sSDxYuwYlWzLvQM7WPLQoXabzHe17yyZfWw8GzpdmXJJRNW_r3fA6riaCQjPccThV1Y_DQBVaMF6AGE90cZBQdNc64zRsUCbL2Z54Zu3PBhZOvhQqlwjMPN7X4tuKgXY3BJmKAlr-kRFwEXmpiSaq5YSfagcHc7CKj92o1gqoJvap58wsIl7ckviTn7RsD2f_jGhDj-moCEip9IV6XeQ_SgMep6Z4GnRmm-ad3o-ZcRDQtP6rcrpA55WGALZmdnVHFDZS7ad3rqT-QwA1tbOwbSoy5udsrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:اقای همتی قرار بود وضعیت دلار بهتر بشه پس چیشد؟
همتی کله کیری: فقط به اقای بسنت بگید 3 روز بیشتر وقت نداری
😐
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72956" target="_blank">📅 19:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72955">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3c124bf523.mp4?token=Gx2ed-9Rw1G0xP06YUab3eBqyh0cNq0k5JLUhwUwFOcIZUCkbDSAxoQ-9Y-uUmJBq1ZLxQjgaKYyEfY4KVL7CwY2wNTuNhqGHN_7_4pI3FxSxzbv0jqDW2lV7oe0uwsP6P7mguy-foM3VqPO1JKJ8DISKCtkgTdukzMSu41Sn9BEsPA1uLudJQHRp7WG7TX8VfKIvwRsUy-T5JNh3Ti5mlfGkErQqIKp4pH1h-oM-kBxNyiuC7OboTBPK7k0kH6_C9B8ARoBkBCPbJTrN5XF4RVbTGljPQoc3PVGHV9ONORcGEayrbUybfwOYGXxERFprbQF2Ox2BaaiK-KEo4psuw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3c124bf523.mp4?token=Gx2ed-9Rw1G0xP06YUab3eBqyh0cNq0k5JLUhwUwFOcIZUCkbDSAxoQ-9Y-uUmJBq1ZLxQjgaKYyEfY4KVL7CwY2wNTuNhqGHN_7_4pI3FxSxzbv0jqDW2lV7oe0uwsP6P7mguy-foM3VqPO1JKJ8DISKCtkgTdukzMSu41Sn9BEsPA1uLudJQHRp7WG7TX8VfKIvwRsUy-T5JNh3Ti5mlfGkErQqIKp4pH1h-oM-kBxNyiuC7OboTBPK7k0kH6_C9B8ARoBkBCPbJTrN5XF4RVbTGljPQoc3PVGHV9ONORcGEayrbUybfwOYGXxERFprbQF2Ox2BaaiK-KEo4psuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن زنگنه نماینده کاکولد‌زاده مجلس:
قرار شده ۱۱۰ هکتار از چابهار رو بدیم به مردم افغانستان تا بتونن یه سرزمین متعلق به خودشون داشته باشن.
البته قرار بود سهم بیشتری بهشون بدین اما یه سری محدودیت هست و اینکار مشکله، ولی حتما پیگیری میکنیم که حلش کنیم!
@News_Hut
😐</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72955" target="_blank">📅 18:49 · 16 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
