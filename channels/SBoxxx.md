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
<img src="https://cdn4.telesco.pe/file/G32i1L-CwRDauijByrqUHRckxnw3ihRQ8QjFdgp88XPK8_MYbxroweIDAx3LenJx-nq-iKEFzQF0OgRVeCOzahfsZRzZrE5wiDJXcqrNrU79IwxvHzwZt2bloFL3o71BRVHE2kcE1nUpz80jGUWm5wyf5Fky3tfsY7_DdJ2WMZPN5riFoY4YLupZywAZbTh47gIjrVGfeUgWsgsjtqw4eCnCaKDpp52c9-y97a7keEQbU0rr6-4_wWEMGSt402EA4PwrwKidSNn3Q44UNLbbgm1XTwg9s6bhgNoUwlgMfS6yFiKdnJEOMO0xKJdKUX_h8qPEqpoq4igOz-TD_0VmYA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 9.88K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-04 06:08:37</div>
<hr>

<div class="tg-post" id="msg-16614">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ترامپ حاضر نیست هزینه خرید اشتراک هوش مصنوعی پرمیوم را بدهد آن وقت میلیاردها دلار پول بلوکه شده ایران را بدون دریافت تضمینهای لازم آزاد کند؟!  سبحان الله!</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/SBoxxx/16614" target="_blank">📅 23:39 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16613">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mRyl524JoqFp6dVX4T7Eu86kfz0EQ3ST8j2gIKwMtpKXn1_vDDeRfA04kaeGMwh1LatS5lI7KkVXNtabOBPvcrpUKi27EJx4Idv0Z1U8kBcyB8t7-BAUQZDj_BUcWkA2sctyoh8wC0zhfLD2aBt1ubhsM_C_CKcsAeU_c2PsX9Frn1VhzjZC6z7stBr7-3GK8RoWCd1Vp3U7luYcj-_CR4vJDO5FImAj_cqe3GZeXbb76omSpW09VBkagNP8M8PCZRRioLcmgTLJyJ_flP9OHmF5sX6jjwDpLLT7Jf8i7OUg5T0ArGnQfNbrcSPJyS7nCj3OZPwszzSS4EFDgNOPTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت جدید ترامپ !</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/SBoxxx/16613" target="_blank">📅 23:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16612">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">اسرائیل تنها.pdf</div>
  <div class="tg-doc-extra">347.2 KB</div>
</div>
<a href="https://t.me/SBoxxx/16612" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">پیشتر گفته بودم که یکی از انگیزه های اسراییل از تعقیب پروژه تغییر رژیم در ایران ایجاد یک کریدور داوود بزرگ است که او را از امتداد آویزان بودن به آمریکا برای تامین امنیت ملی اش بی نیاز کند.</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/SBoxxx/16612" target="_blank">📅 22:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16611">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bg2J63tniX_INvV01wJEFIyW17cQIpME48rpvtSYoWuh_t-1FRdETyOoMqkvMpmoAKg1Od5eyKcAWfQZlbehZDFKdHYBDq0LZXpIgToLMHO6xcj27jq5D1bQHOQRx32WduZ3oD4t890TJNHVXWvLu4Kb3QjtcmprebbVB_kb4ftz9sw0gcpEWeagCA0m_4hsKbl3F53F_neODi5lSjFx8jQjUzlgo9GsCck9d__I_ltIGfMbTZR0Yr_Y4SMOwEp3kc_VR65SL7UT9q1LzSBumfQ3RMYig6ijPKSP-rGBO9_64DmS-jmEInz6VwkirwMJcaVcYmjco_hcEEIElv3HuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/SBoxxx/16611" target="_blank">📅 22:08 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16610">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec50a6a754.mp4?token=TR4LYf5jUvmvpY-Oa09KzYoS4eC2miBQWZjqEPU82Rf3cjKxHi1YYUR-3DqaPzCTUUxQoPDQH93wdVbiWqHVsSBylUxbxt-uX0wbrNsXZ6zKokhuOTVcXZ-6cDamIYkZXquAowtcNzZ1gwteQA3ZFTXksOEODVxvrvpkvgd66EK_dmnhksj91PRvCcZX0oQnzPcXaxItpB-rX0iiKjbmNhGzpbU_MLEgz0SnpRutjZV8JvTgbZASMBgkxT6E6bMe2ZZDF36atJOKzI3k95hlA7CHUux1QZPTCQiIZ_mUFu7bmHGecfBtRDpiXau55w7snocjaYP--YDaROko__RLNoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec50a6a754.mp4?token=TR4LYf5jUvmvpY-Oa09KzYoS4eC2miBQWZjqEPU82Rf3cjKxHi1YYUR-3DqaPzCTUUxQoPDQH93wdVbiWqHVsSBylUxbxt-uX0wbrNsXZ6zKokhuOTVcXZ-6cDamIYkZXquAowtcNzZ1gwteQA3ZFTXksOEODVxvrvpkvgd66EK_dmnhksj91PRvCcZX0oQnzPcXaxItpB-rX0iiKjbmNhGzpbU_MLEgz0SnpRutjZV8JvTgbZASMBgkxT6E6bMe2ZZDF36atJOKzI3k95hlA7CHUux1QZPTCQiIZ_mUFu7bmHGecfBtRDpiXau55w7snocjaYP--YDaROko__RLNoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گویا توافق در حال ولی خب شدن است...</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/SBoxxx/16610" target="_blank">📅 22:08 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16609">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ترامپ
:
اگر با ایران معامله‌ای انجام دهم، معامله‌ای خوب و درست خواهد بود، نه مثل معامله‌ای که اوباما انجام داد و به ایران مقادیر زیادی پول نقد و راهی واضح و باز به سمت سلاح هسته‌ای داد. معامله ما کاملاً برعکس است، اما هیچ‌کس آن را ندیده یا نمی‌داند چیست. حتی هنوز به طور کامل مذاکره نشده است. پس به بازندگان گوش ندهید که درباره چیزی که هیچ نمی‌دانند انتقاد می‌کنند. برخلاف کسانی که قبل از من باید سال‌ها پیش این مشکل را حل می‌کردند، من معامله‌های بد نمی‌کنم!
رئیس‌جمهور DJT</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/SBoxxx/16609" target="_blank">📅 21:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16608">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AxL1DkdOjq8K--5w62UvMKmOE1Cpr1_-BQGynOWwc1bQsWbs8x1GXzSFdszsgM7Z0KosfqHLfSiXP1XbZR-I7rtccL6NOEuuPErDxT7irA1q54iM7XvJrtSpvsena19I5jQAkBXB4yonPpyV65YG1NlxdWsTuvpJTpZVVV3-ONHYYIGn4mfHXpqgpm6BhIAUOf1moUHFmQ1s7kHPP9TJzy8_3YLGeWC6PBdMzcnsx7MoByMCS6q36si8sIJJv-2TYOUJ6uUwKn0_dtJA0XzEG1UxRZo5akSMgTZ5GtWiehCBr6n5zYLhrAOtEt4syBP2jT9k6WGYul2ojmrH627-HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/SBoxxx/16608" target="_blank">📅 21:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16607">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvl5pNJrCmKJv6gkFN-SC2qEJttbWagMVFtXSWdrCT1akiZpYALnnKAUsAiJ46KeUSbxJIIs6OFu0XcONTzpfRfVaUxl-nxcxKYJ1qpH3IhaUHbWuj4bl2TbUOw0J0i3qbU0jLvkINioV51_jYgVU-JnaHBkUM6EBalF51OwhLLokSAIG7JAVxhVjgm_nCw3m21ujjh7ESCYbvL82VmL4m-3xVlBd-Wl97gqTNjw4j9WyyxcXOM3KDltyttNnuQgdK3-WGAR_x_FF_eitxtXr_uoRYtodkYr4vSdp5Z3uLUBSXflH0AZAaIhiM5uuzp4gahaPSKb71Nm337yYULQqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بند جوری تنظیم شده که به اسراییل هر لحظه فرصت حمله به حزب الله می‌دهد.  با شناختی که از نتانیاهو هست، تقریبا محال است که این بند رعایت بشود و باید گفت همان معاوضه ای که پیشتر گفته شد برقرار است و بعید است حملات اسراییل متوقف بشود</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/SBoxxx/16607" target="_blank">📅 21:44 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16606">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">قیمت کنونی ۱۶۹</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/SBoxxx/16606" target="_blank">📅 21:30 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16605">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">رئیس ستاد ارتش اسرائیل، عیال زامیر:
«ما آماده‌ایم تا بلافاصله به درگیری‌های شدید بازگردیم تا حکومت  ایران را تضعیف کنیم».</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/SBoxxx/16605" target="_blank">📅 20:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16604">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e42b23612d.mp4?token=RUql1nBfTRdochj8QV22wHwvUGZdtqtOYq9bvWctahEjm7shGi5wG_CzasD0VTByZQ0MYhLRhPtC5AXTDIy__KerqgcKYw8TqHQh9FKiJqmZWGvNDcZXFb6-1yHGiU5iwvMCr4NhB2aClwku1P8Qq7Ba8EbbeWnblKPbBTEiCNdh7IC-5i64LmHUYPy3zTMbw5kSv9QZxKDJDj3YFWX_X5nt8hlrqV6CNjuvmY75AfMIk3LAQ201kSEIaYjVW4QHcN8SZ3aRC1RMMgEN67aVn0sGr3wel-IIJ08waKPwTJoWAPhYjDV877FpmAwicNoqHxdioaDF1-NfTmolBEkb-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e42b23612d.mp4?token=RUql1nBfTRdochj8QV22wHwvUGZdtqtOYq9bvWctahEjm7shGi5wG_CzasD0VTByZQ0MYhLRhPtC5AXTDIy__KerqgcKYw8TqHQh9FKiJqmZWGvNDcZXFb6-1yHGiU5iwvMCr4NhB2aClwku1P8Qq7Ba8EbbeWnblKPbBTEiCNdh7IC-5i64LmHUYPy3zTMbw5kSv9QZxKDJDj3YFWX_X5nt8hlrqV6CNjuvmY75AfMIk3LAQ201kSEIaYjVW4QHcN8SZ3aRC1RMMgEN67aVn0sGr3wel-IIJ08waKPwTJoWAPhYjDV877FpmAwicNoqHxdioaDF1-NfTmolBEkb-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
ولادیمیر پوتین جزئیات جدیدی درباره عملکرد موشک "اورشنیک" روسیه اعلام کرد:
🔶
کلاهک این موشک به دمای ۴۰۰۰ درجه سانتی‌گراد می‌رسد که آن را به سلاحی با تخریب بالا تبدیل می‌کند.
🔶
هر چیزی که در منطقه انفجار باشد، به ذرات ابتدایی تجزیه شده و عملاً به گرد و غبار…</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/SBoxxx/16604" target="_blank">📅 18:36 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16603">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">-طبق گزارش آکسیوس، یک مقام ارشد در دولت ترامپ اعلام کرد که امضای توافق امروز مورد انتظار نیست و هنوز چندین جزئیات باید حل و فصل شود. هنوز در مورد برخی جزئیات رفت و برگشت وجود دارد، برخی کلمات که برای ما مهم هستند و برخی کلمات که برای آنها مهم است،»
این مقام ادعا کرد که سیستم ایرانی در پیکربندی فعلی خود به سرعت حرکت نمی‌کند و برای طی کردن تمام تأییدیه‌های لازم، چند روز طول خواهد کشید تا توافق نهایی شود.</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/SBoxxx/16603" target="_blank">📅 18:29 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16602">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">یادداشت تفاهم آمریکا و ایران، طبق Axios:
تمدید آتش‌بس به مدت ۶۰ روز
عدم دریافت عوارض ایرانی در تنگه هرمز
ایران ابتدا تمام مین‌ها را پاکسازی کرده و محاصره خود را برمی‌دارد
آمریکا پس از برآورده شدن این خواسته‌ها توسط ایران، محاصره خود را پایان می‌دهد
آمریکا برخی معافیت‌های تحریمی مرتبط با صنعت نفت ایران را صادر خواهد کرد
تعهد ایران به هرگز دنبال کردن سلاح‌های هسته‌ای
ایران متعهد می‌شود مذاکراتی درباره تعلیق کامل برنامه غنی‌سازی هسته‌ای و حذف ذخایر اورانیوم غنی‌شده خود برگزار کند
آمریکا متعهد می‌شود مذاکراتی برای رفع تدریجی تحریم‌ها علیه ایران و بحث درباره دارایی‌های مسدود شده ایران برگزار کند
آمریکا هیچ نیرویی را از اطراف ایران خارج نخواهد کرد.</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/SBoxxx/16602" target="_blank">📅 18:21 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16601">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">دونالد ترامپ در تروث سوشال:
یکی از بدترین قراردادهایی که کشور ما هرگز منعقد کرد، توافق هسته‌ای با ایران بود که توسط باراک حسین اوباما و آماتوران رده‌بندی شده در دولت اوباما ارائه و به وجود آمد.
این یک مسیر مستقیم برای توسعه سلاح هسته‌ای توسط ایران بود. اما نه در مورد معامله‌ای که در حال حاضر توسط دولت ترامپ با ایران در حال مذاکره است - دقیقاً برعکس! مذاکرات به شیوه‌ای منظم و سازنده در حال پیشرفت است و من به نمایندگان خود اطلاع داده‌ام که در آن زمان که زمان به نفع ماست، به سرعت وارد معامله‌ای نشوند.
محاصره تا زمانی که توافقی حاصل، تأیید و امضا شود، با تمام قدرت و اثر باقی خواهد ماند. هر دو طرف باید زمان خود را بگیرند و آن را درست انجام دهند. نباید خطایی رخ دهد! روابط ما با ایران به یک رابطه بسیار حرفه‌ای‌تر و پربارتر تبدیل می‌شود.
با این حال، آن‌ها باید درک کنند که نمی‌توانند سلاح یا بمب هسته‌ای توسعه یا تهیه کنند. من می‌خواهم تاکنون از تمام کشورهای خاورمیانه بابت حمایت و همکاری آن‌ها تشکر کنم که با پیوستن آن‌ها به ملت‌های توافق‌نامه‌های تاریخی ابراهیم، بیشتر تقویت و تقویت خواهد شد و چه کسی می‌داند، شاید جمهوری اسلامی ایران نیز بخواهد به آن بپیوندد!
بابت توجه شما به این موضوع سپاسگزارم. رئیس‌جمهور دونالد جی. ترامپ</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/SBoxxx/16601" target="_blank">📅 18:03 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16600">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">خبرگزاری فارس اکنون گزارش می‌دهد که اختلافی در مورد دو بند از تفاهم‌نامه وجود دارد.  به نظر می‌رسد یکی از این بندها مربوط به رفع مسدودی دارایی‌های مسدود شده ایران است. ایالات متحده قبلاً توافق کرده بود که بخشی از آن را از پیش آزاد کند و بقیه را بعداً از طریق…</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/SBoxxx/16600" target="_blank">📅 15:34 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16599">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSirus</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZhiCwl0ankj6t72P5yRlZGxzAcW1z7jQR0FuyH_zFB2c0gVgLcAc-kqvlIjTUHEJvx3VoIjkrLVDt8_2ADiNXKg8Vx-hSheqnqZiBP5K5z8wWIgVtYaVTEJaI-hq6k00eG6zfe91NF6Z9hbHgfs0NIYsxCmGLHpAwdqVRS887jde57B7-V0fSk1KQisA9kiioTqqATgTq_BQ95eMqkGZNDpJyF_W4zeX98Yc0LViC30O8z0m469tybuNxkycLPvr9-N5kER4vwfQsVODn18hO_ie6thEvQ9G_j059gM8UDs-OzjqgbSbaavAOyn-jfyDo-N8DEvPtMH2QjbGoGwmiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خرمشهر چقدر مظلوم بود و هست، چند سال پیش رفتم و هنوز آثار جنگ با صدام باقی بود!
یاد تکاوران ارتش و نیروهای مردمی گرامی
و یاد زنده یاد سرگرد خلبان محمود اسکندری و کابین عقبش ستوان اکبر زمانی که با انهدام پل اروند عقبه لجستیکی صدام رو قطع کرد و مهمترین نقش در آزادی خرمشهر داشت؛
خرمشهر را خدای محمود اسکندری آزاد کرد...</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/SBoxxx/16599" target="_blank">📅 15:16 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16598">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">مسئول اسرائیلی:   ترامپ به نتانیاهو گفت که توافق نهایی با ایران منجر به خلع سلاح برنامه هسته‌ای و حذف تمام اورانیوم غنی‌شده خواهد شد</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/SBoxxx/16598" target="_blank">📅 15:14 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16597">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">این بند جوری تنظیم شده که به اسراییل هر لحظه فرصت حمله به حزب الله می‌دهد.  با شناختی که از نتانیاهو هست، تقریبا محال است که این بند رعایت بشود و باید گفت همان معاوضه ای که پیشتر گفته شد برقرار است و بعید است حملات اسراییل متوقف بشود</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/SBoxxx/16597" target="_blank">📅 15:10 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16596">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">قیمت کنونی ۱۶۹</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/SBoxxx/16596" target="_blank">📅 14:45 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16595">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">دلار خرید دارد همینجا با تارگت ۲۴۰ الی ۲۶۰ هزار تومان</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/SBoxxx/16595" target="_blank">📅 14:44 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16594">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">خبرگزاری فارس اکنون گزارش می‌دهد که اختلافی در مورد دو بند از تفاهم‌نامه وجود دارد.
به نظر می‌رسد یکی از این بندها مربوط به رفع مسدودی دارایی‌های مسدود شده ایران است. ایالات متحده قبلاً توافق کرده بود که بخشی از آن را از پیش آزاد کند و بقیه را بعداً از طریق یک مکانیزم آزاد سازد، اما اکنون از هرگونه پرداخت از پیش خودداری می‌کند.
تسنیم هم گفته  که اگر مانع‌تراشی ایالات متحده ادامه یابد، هیچ تفاهم‌نامه‌ای امضا نخواهد شد.</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/SBoxxx/16594" target="_blank">📅 14:44 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16593">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اگر حادثه تیراندازی چند هفته پیش در آن سالن را هم حساب کنیم، ترامپ دو‌ بار خودش مورد سوقصد قرار گرفته و یک بار هم افشاگری درباره ترور دخترش مطرح شده!</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/SBoxxx/16593" target="_blank">📅 14:30 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16592">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">در ۳ روز گذشته:  — افشای طرح ترور ایوانکا ترامپ از سوی یک عضو حشدالشعبی   — تیراندازی و ترور در اطراف کاخ سفید  — دو حادثه تروریستی در بلوچستان(جنوب شرق) و مناطق پشتون نشین (شمال و شمال غرب) پاکستان</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/SBoxxx/16592" target="_blank">📅 14:30 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16591">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
اعتراض نتانیاهو به دو بند از توافق ایران و آمریکا
🔹
نتانیاهو جلسه‌ای در مورد توافق احتمالی آمریکا و ایران برگزار کرد.
🔹
به گفته شبکه تلویزیونی کان اسرائیل، نتانیاهو به ترامپ گفته است که نگران دو بند از این توافق است.
🔹
یکی از بندها مربوط به آتش‌بس در لبنان…</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/SBoxxx/16591" target="_blank">📅 14:28 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16590">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M36RHxHZd5UkR5jo8whUGpPK0Ow19IbQ6qfinVp5wJO8yJGhOaC-rOnZMUrh9n2MTfKU0LR7t_88Os2aejR2_kItwRM2O2ndty8Z8q3UYCBTRMky08gTTW17qW7-ObhttDgP8ndnykUAGKgwx_YISI65EAC9uETLyOpWFw43ckH7dL86GwdRvRsTBKjpVZo48gzPQpVWftX_JQMoZ13sK8ZQrvR3mPBqkw_MZts7ErA9_2zL4HDN_aZbKok4990Ce1bUa11vz_CZyr9AV7rjyi2Y6dfZGVCC8du-6h5I8HEiqkXE7IB4GHM6puCi3hH9eyM_vps3Mk3LgNh8NOxnmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تیراندازی در نزدیکی کاخ سفید و اعلام وضیعت هشدار امنیتی
🔻
منبع : ABC NEWS</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/SBoxxx/16590" target="_blank">📅 14:12 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16589">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">این بند جوری تنظیم شده که به اسراییل هر لحظه فرصت حمله به حزب الله می‌دهد.  با شناختی که از نتانیاهو هست، تقریبا محال است که این بند رعایت بشود و باید گفت همان معاوضه ای که پیشتر گفته شد برقرار است و بعید است حملات اسراییل متوقف بشود</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/SBoxxx/16589" target="_blank">📅 13:55 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16588">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">یک مقام ارشد ایرانی روز یکشنبه به رویترز گفت که تهران با انتقال ذخایر اورانیوم غنی‌شده با خلوص بالا به خارج از کشور موافقت نکرده است.</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/SBoxxx/16588" target="_blank">📅 13:50 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16587">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/SBoxxx/16587" target="_blank">📅 11:39 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16586">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">خب در توافق بحث پایان جنگ در لبنان هم مطرح شده و لذا میتوان گفت این بندش هیچ وقت اجرا نخواهدشد.</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/SBoxxx/16586" target="_blank">📅 10:59 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16585">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">گزارش موسسه مطالعات جنگ از روند مذاکرات
توجه کنید که این گزارش پیش از توییت شب گذشته ترامپ منتشر شده است
آخرین پیشنهاد متقابل ایران
تمام خواسته‌های کلیدی ایران از جمله برداشتن «تهدید آمریکا علیه ایران»، تسکین مالی، و «حق» ایران برای مدیریت تنگه هرمز را در اولویت قرار می‌دهد، در حالی که تلاش می‌کند مذاکره درباره برنامه هسته‌ای ایران را به تأخیر بیندازد. پیشنهاد ایران ارزیابی مرکز مطالعاتی (CTP-ISW) را تأیید می‌کند که حکومت ایران معتقد است در حال برنده شدن در جنگ است و از موضع قدرت مذاکره می‌کند.
آژانس خبری تسنیم، وابسته به سپاه پاسداران انقلاب اسلامی (IRGC)، در ۲۳ مه ۲۰۲۶ گزارش داد که پیشنهاد ایران به میانجی‌های پاکستانی ارسال شده است. ایران خواستار پایان جنگ در تمام جبهه‌ها، از جمله در لبنان، و خروج نیروهای آمریکایی از «منطقه جنگ» شده است. برداشتن «تهدیدهای آمریکا علیه ایران» به معنای خروج آمریکا از منطقه خواهد بود که هم اهرم نظامی آمریکا را حذف می‌کند و هم یکی از اهداف کلیدی ایران، یعنی اخراج نیروهای آمریکایی از منطقه، را محقق می‌سازد.
در این پیشنهاد، ایران درخواست کرده است که تا زمانی که جنگ پایان نیابد، برنامه هسته‌ای خود را مورد بحث قرار ندهد، از انتقال ذخایر اورانیوم غنی‌سازی‌شده (HEU) خود به ایالات متحده خودداری می‌کند و تعهدی برای برچیدن تأسیسات هسته‌ای خود نخواهد داد؛ همه این موارد از خواسته‌های کلیدی آمریکا هستند. آمریکا در فاز اول هر توافقی، اهرم قابل‌توجهی را از دست خواهد داد، قبل از اینکه حتی درباره موضوع هسته‌ای مذاکره کند. این پیشنهاد همچنین شامل خواسته‌های ایران مبنی بر لغو تمام تحریم‌ها علیه ایران و آزادسازی تمام دارایی‌های مسدود شده ایران در فاز اول است.
ایران در این پیشنهاد تأکید کرده است که تنگه هرمز تحت نوعی کنترل ایرانی باقی خواهد ماند و اگر آمریکا محاصره بنادر و کشتی‌های ایرانی را پایان ندهد، مذاکرات را ادامه نخواهد داد. شرایط ماکسیمالیست در این پیشنهاد نشان می‌دهد که حکومت ایران معتقد است از موضع قدرت مذاکره می‌کند، زیرا خود را پیروز جنگ می‌داند.
مقامات ایرانی
همچنان بر مدیریت ایران بر تنگه هرمز به عنوان یکی از نقاط چالش‌برانگیز در مذاکرات تأکید می‌کنند. سخنگوی وزارت امور خارجه ایران، اسماعیل بقایی، در ۲۳ مه اعلام کرد که تنگه هرمز «به آمریکا ارتباطی ندارد» و ایران و عمان باید به عنوان کشورهای ساحلی مکانیسمی برای این آبراه تعریف کنند. روزنامه نیویورک تایمز در ۲۱ مه گزارش داد که ایران و عمان درباره سیستمی برای دریافت هزینه از کشتی‌ها به عنوان «خدمات دریایی» به جای عوارض عبور بحث کرده‌اند. این اقدام بر اساس قانون بین‌المللی دریاها غیرقانونی است.
آژانس خبری تسنیم، وابسته به سپاه پاسداران، در ۲۳ مه گزارش داد که ایران خواستار شده است که تنگه هرمز به مکانیسم و «رژیم حقوقی» پیش از جنگ بازنگردد. تسنیم اضافه کرد که ایران خواستار پایان محاصره دریایی آمریکا شده و اعلام کرده است که مذاکرات تا زمانی که این محاصره برقرار باشد، پیش نخواهد رفت. آژانس خبری فارس، وابسته به سپاه پاسداران، نیز گزارش داد که ایران تنها متعهد به بازگرداندن تعداد کشتی‌هایی خواهد شد که از تنگه عبور می‌کنند به سطح پیش از جنگ است، در حالی که ایران تعیین خواهد کرد کدام کشتی‌ها مجوز دریافت می‌کنند و باید از کدام مسیر عبور کنند.
ناوگان سپاه پاسداران در ۲۳ مه اعلام کرد که ۲۵ کشتی در ۲۴ ساعت گذشته با دریافت مجوز و تحت هماهنگی و تأمین امنیت ناوگان سپاه از تنگه عبور کرده‌اند، که نشان می‌دهد ایران سعی دارد خود را به عنوان مدیر و تأمین‌کننده امنیت عبور از تنگه معرفی کند.
دونالد ترامپ، رئیس‌جمهور آمریکا
، در ۲۳ مه اعلام کرد که تا ۲۴ مه تصمیم خواهد گرفت آیا حمله به ایران را از سر بگیرد یا خیر. یک مقام آمریکایی آشنا با مذاکرات به آکسیوس گفت که مذاکره‌کنندگان هر روز پیش‌نویس‌ها را رد و بدل می‌کنند، اما پیشرفتی حاصل نشده است. ترامپ گفت که شانس رسیدن به توافق با ایران یا از سرگیری حملات «پنجاه-پنجاه» است. ترامپ در ۲۳ مه با رهبران منطقه‌ای برای بحث درباره آخرین پیشنهاد ایران گفتگو کرد. یک منبع نزدیک به مذاکرات به واشینگتن تایمز گفت که انتظار می‌رود آمریکا و ایران تا بعدازظهر ۲۴ مه اعلام نهایی پیش‌نویس توافق برای پایان جنگ در تمام جبهه‌ها را اعلام کنند. ترامپ گفت که او تنها توافقی را خواهد پذیرفت که به مسائل کلیدی از جمله غنی‌سازی اورانیوم ایران و ذخایر اورانیوم غنی‌سازی‌شده آن بپردازد.</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/SBoxxx/16585" target="_blank">📅 10:21 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16584">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">در ۳ روز گذشته:  — افشای طرح ترور ایوانکا ترامپ از سوی یک عضو حشدالشعبی   — تیراندازی و ترور در اطراف کاخ سفید  — دو حادثه تروریستی در بلوچستان(جنوب شرق) و مناطق پشتون نشین (شمال و شمال غرب) پاکستان</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/SBoxxx/16584" target="_blank">📅 09:24 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16583">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">در ۳ روز گذشته:
— افشای طرح ترور ایوانکا ترامپ از سوی یک عضو حشدالشعبی
— تیراندازی و ترور در اطراف کاخ سفید
— دو حادثه تروریستی در بلوچستان(جنوب شرق) و مناطق پشتون نشین (شمال و شمال غرب) پاکستان</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/SBoxxx/16583" target="_blank">📅 09:23 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16582">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">حمله انتحاری در ‌کویته پاکستان  ۸ نفر کشته و ۳۰ تن دیگر زخمی شدند  انفجار قوی در نزدیکی یک مرکز امنیتی که مشرف به ایستگاه قطار است، شهر کویته را لرزاند.  منابع بیمارستانی گفتند که ۸ جسد از محل حادثه انتقال داده شده و ۳۰ نفر دیگر نیز زخمی هستند.</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/SBoxxx/16582" target="_blank">📅 09:21 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16581">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
تیراندازی در نزدیکی کاخ سفید و اعلام وضیعت هشدار امنیتی
🔻
منبع : ABC NEWS</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/SBoxxx/16581" target="_blank">📅 09:14 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16580">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AniK6UZVx711IE_5kgcvHBDg1aS8vsMyeWRKf4WU4XUxGaHlkcMuBXY97IVgtJnJHITCEQXlzolIbi634rKeGcDUaDYNv7zut1lu7eJqKz6zwz8u-Y5WgWJf5V4EJXkcYuAKR8DatOqsOfzRTfR8jQ2aN1OeDn457I8xEOsA-iWFyyAqQbgqveMlJsySMDg5W9r8kPvo5pBizJhM1UqxeVDoc6RB6DNDdYO-PMfDqk9OquIP7VvKyxad19qIv4xq3umgaWC8X-dpunyETuMcUdxMtvRGI0UmGP-Byb-cFxEIYb1uLNSKJCUeaypVZtfE7KmsgTKAGVC4ysF7dCpRxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاهک موشک اورشنیک روسیه تا 4000 درجه حرارت می‌گیرد که می تواند فلز را ذوب و بتن را تبخیر کند و خودروهای زرهی را فوراً نابود کند.   برای اینکه دید بهتری از قدرت ویرانگری این دما بدست آورید اینجا میگویم که چگونه این دما با سایر منابع گرمای شدید مقایسه می شود؟…</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/SBoxxx/16580" target="_blank">📅 06:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16579">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">تحلیل من این است که ترامپ فعلا میخواهد یک دور کوتاه از حملات شدید را انجام داده و سپس اعلام پیروزی و پایان جنگ کند تا در آستانه جام جهانی، کمتر زیر فشار افکار عمومی باشد.  اما جنگ اصلی برای چند ماه بعد خواهدبود.  در واقع این جنگ کوتاه را می‌توان یک موج B درنظر…</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/SBoxxx/16579" target="_blank">📅 06:39 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16578">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LA806WybTYfgE9xyNqG23G5WfjHbtvBOTasPa3nDzzU7B_2dwGJLVR8sgYY0VVl303OuRCW7R5uzhFi-GpqojeGyXpqaFfmnh3curxgZH9ABfa14lTnpmgFL61tkX5xA3xbaHNLkOosZOS2xxd9JNW_6penefMwCXyNhB9S6ichX8yXBap8RXvXHGJzvrz9NFUaadBhqvL0wPtGgcWBGJwpBWJBhcNLSBsOtCkl-bA8EsgQabx-l2cGNGxYdAddGxgpthpxl-jsKyiFeGRNGvkUKV276H7SjG9AUNSazNV1QLZ6mZrBDa9JzuyVjw5l8-U10FYnktW8gAODLnlfDcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرویس مخفی ایالات متحده بیانیه‌ای در مورد حادثه تیراندازی در اوایل بعدازظهر امروز در نزدیکی کاخ سفید در خیابان ۱۷ شمال غربی و خیابان پنسیلوانیا شمال غربی در واشنگتن دی‌سی صادر کرده است:   پس از اینکه فردی سلاحی را از کیف خود بیرون کشید و شروع به شلیک کرد،…</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/SBoxxx/16578" target="_blank">📅 06:35 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16577">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
تیراندازی در نزدیکی کاخ سفید و اعلام وضیعت هشدار امنیتی
🔻
منبع : ABC NEWS</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/SBoxxx/16577" target="_blank">📅 06:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16576">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">هاآرتص درباره افسرانی که در لبنان می‌جنگند:   وضعیت ناامیدی در میان ارتش به دلیل افزایش تعداد تلفات ناشی از تجمعات حزب‌الله گسترده شده آن هم در حالی که ترامپ اجازه عملیات در بیروت و دره بقاع را نمیدهد و عملا ما فقط خانه های روستایی را منفجر می‌کنیم!</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/SBoxxx/16576" target="_blank">📅 06:26 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16575">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">انتشار داستان طرح ترور ایوانکا ترامپ و همینطور حادثه دیشب نوعی پیام هشدار به ترامپ است.</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/SBoxxx/16575" target="_blank">📅 06:20 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16574">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">واقعاً طرح پروفسور شریعتمداری جواب داد؛  اکنون که تنگه باز شده دیگر وقت ترور ترامپ است.</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/SBoxxx/16574" target="_blank">📅 02:00 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16573">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
تیراندازی در نزدیکی کاخ سفید و اعلام وضیعت هشدار امنیتی
🔻
منبع : ABC NEWS</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/SBoxxx/16573" target="_blank">📅 01:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16572">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">توافق صلح آمریکا با ایران شامل بازگشایی تنگه هرمز، پایان محاصره، آزادسازی ۶ میلیارد دلار از دارایی‌های مسدودشده ایران و خروج نیروهای دریایی آمریکا از اطراف ایران است</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/SBoxxx/16572" target="_blank">📅 01:39 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16571">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">خیلی شرط منطقی است، پیشنهاد می شود حتما در شرایط توافق گنجانده بشود</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/SBoxxx/16571" target="_blank">📅 01:13 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16570">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">خب در توافق بحث پایان جنگ در لبنان هم مطرح شده و لذا میتوان گفت این بندش هیچ وقت اجرا نخواهدشد.</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/SBoxxx/16570" target="_blank">📅 01:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16569">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SYT7HX5AnWpV6dTPKvrsB0C867LxzYcPEpLtNfDmAtZ2dAIurcWH4uDuMEpNvC1rJ51kxCgpCplFZxlJ6VFgXG0EwYZEW_DjCkh0Z0563HdQbusVpU8NiVBdbV3tlcDbAM35cSyH5Z_AtF3ZekV0qNOicUnOKuw9w1yQuHE86Y0hF1NoYIkYXgD8v9Tt2KT2hne1K-HRG54vuda7cypWB32E2YqA7x-n2rxDvIlsRGfpV-Pqhydu8A7y_PAxWGhvxPRpPh0l3f_Mr-TgDEw2WxdarxhGE5SWEfFBS1rekJrgLRGNHCOWfPbEkaHlw5fgQjz8Wyyl7dj9KWapy7UX3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تصویر هم اکنون در کانالهای جانفدایان دست به دست می شود...  سبحان الله!</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/SBoxxx/16569" target="_blank">📅 00:59 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16568">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uD6XppaX0uIxT41qU3FE9sLYhzfjYfysZ2k1iSyetTEvqTryYqs7WXoyc6Ycxlchnc7tRcEnzbhvU89xIoPOQf_n77ZElNP9g4kELMasms579g5fvn1YvJ2TbgGzRyeIESI0RN-VfZNNb-Qj8Uc_svxhnLdc9bjQ3chUYIk9J1sAKxCZFrg0fP_Chng1wboDOmmkgqXjDolMRZ_Yc2nvyK7f8XVWS7uhk4BcPsQbKyeABUzXApIHBFiA6PBXK_ilTRcytO6HPlKofQxAcVnrbxAPsoqLGgw0c0OxxTeOyq2yr81dn-7_bRyLD51BnXsKsMH3NmJEhYb8LMVl_jXIcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تصویر هم اکنون در کانالهای جانفدایان دست به دست می شود...
سبحان الله!</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/SBoxxx/16568" target="_blank">📅 00:56 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16567">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✅
متن کامل توئیت ترامپ در مورد توافق با ایران:  من در دفتر بیضی شکل کاخ سفید هستم جایی که به تازگی تماس بسیار خوبی با رئیس‌جمهور محمد بن سلمان آل سعود از عربستان سعودی، محمد بن زاید آل نهیان از امارات متحده عربی، امیر تمیم بن حمد بن خلیفه آل ثانی، نخست‌وزیر…</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/SBoxxx/16567" target="_blank">📅 00:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16566">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">✅
متن کامل توئیت ترامپ در مورد توافق با ایران:
من در دفتر بیضی شکل کاخ سفید هستم جایی که به تازگی تماس بسیار خوبی با رئیس‌جمهور محمد بن سلمان آل سعود از عربستان سعودی، محمد بن زاید آل نهیان از امارات متحده عربی، امیر تمیم بن حمد بن خلیفه آل ثانی، نخست‌وزیر محمد بن عبدالرحمن بن جاسم بن جابر آل ثانی و وزیر علی الثوادی از قطر، فیلد مارشال سید عاصم منیر احمد شاه از پاکستان، رئیس‌جمهور رجب طیب اردوغان از ترکیه، رئیس‌جمهور عبدالفتاح السیسی از مصر، پادشاه عبدالله دوم از اردن و پادشاه حمد بن عیسی آل خلیفه از بحرین، درباره جمهوری اسلامی ایران و همه موارد مربوط به تفاهم‌نامه‌ای درباره صلح داشتیم.
یک توافق تا حد زیادی مذاکره شده است که منوط به نهایی شدن بین ایالات متحده آمریکا، جمهوری اسلامی ایران و کشورهای مختلف دیگر ذکر شده است. به طور جداگانه، من تماسی با نخست‌وزیر بیبی نتانیاهو از اسرائیل داشتم که به همان اندازه خوب پیش رفت. جنبه‌ها و جزئیات نهایی توافق در حال حاضر در حال بحث است و به زودی اعلام خواهد شد.
علاوه بر بسیاری از عناصر دیگر توافق، تنگه هرمز باز خواهد شد.</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/SBoxxx/16566" target="_blank">📅 00:06 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16564">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❌
۶۰ روز تاریکی
❌
🟠
۶۰ روز از شروع عملیات نظامی ایالات متحده و اسرائیل گذشت و اینترنت که از ساعتی بعد از آغاز تهاجم قطع شده بود ، کماکان در خاموشی مطلق به سر می‌برد و با طبقاتی شدن روند استفاده آن ، شکل و شمایل یک اینترنت با حیات نباتی را به خود گرفته است…</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/SBoxxx/16564" target="_blank">📅 23:40 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16563">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔻
ثابتی ؛ نماینده مجلس
:
جنگ نظامی مجدد قطعی است ،  حتی اگر آمریکا تسلیم شود</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/SBoxxx/16563" target="_blank">📅 22:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16562">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">—مقامات اسرائیلی به آکسیوس:
« نتانیاهو نگران توافق مورد بحث است و از ترامپ خواسته است تا دور دیگری از حملات را آغاز کند».</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/SBoxxx/16562" target="_blank">📅 20:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16561">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ادعای جدید روبیو درباره مذاکرات:   شاید خبری باشد، شاید نباشد!</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/SBoxxx/16561" target="_blank">📅 20:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16560">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👽
ذکر نام "ایران" در اسناد جدیدی که وزارت دفاع آمریکا از پرونده های UFO منتشر کرده است :
4 شیء ناشناس پرنده به صورت گروهی 26 آگوست 2022، روی آبهای ایران مشاهده شدند</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/SBoxxx/16560" target="_blank">📅 19:46 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16559">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
تقی پور ؛ نماینده مجلس
:
جمهوری اسلامی ایران می‌تواند کابل‌های حیاتی فیبرنوری جهان را قطع کند</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/SBoxxx/16559" target="_blank">📅 19:40 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16558">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/idhTsmsOIO-_s1ccpEE_n18rEKGBsY4plm--Vgn1ApGvuTVOT_4J9Xwzjx6vyp9DhMtj65Xrij_4ywoDAqHxkpGxB76A0wEoqcPQtjQXebl_Ggg_OHFFanhlNK4xBWLBL-8Fq0WQGjqYwMhHY5lZr18LfXpwGrgTIOPPWRQHE_W6um7sCSS4D-Yhb_hW0EI1q90zY011B7p-YYe0zLplsXCqCGg74qK8SQ4xl18OxhzAxFaNFLmZpJOVcYcKFSNTc6obi7AoILjgDskN_brwJ0z6iTQtrIn6fkJfmBLgvg0zrxH-2VDCAl4S5VnNVtGRPcva_3BiVQh9QKuRduoKFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/SBoxxx/16558" target="_blank">📅 18:58 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16557">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">سخنگوی وزارت خارجه:   ما به توافق خیلی دور و خیلی نزدیک هستیم</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/SBoxxx/16557" target="_blank">📅 17:42 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16556">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">سخنگوی وزارت امور خارجه ایران، اسماعیل بقایی، به زبان عربی:   اگر دندان‌های {آرواره}  یک شیر را باز کرده ببینید، فرض نکنید که شیر در حال لبخند زدن است.</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/SBoxxx/16556" target="_blank">📅 17:38 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16555">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pifb16BUE6qD_rK9mImYmig7xJjX_46Q7xPlywZPoBYe_99h-5bAW-KCz8jxzA4Jz_ufQrGH72zE4A7LmkBg-NXR2bAWcyNOBbiiJyWWQV3-pWxXdVcj3O6XB7UQN3nkUoRMmiCSMvUzGH-BEDKvzSYdlvubv9SyzkaUXPafzaifcBP27yNhM0vfO2I_6ZZoqEzNERkQeKcnknPYvCuVersqi5QdyQjJF9NUKmf1SWPpCJGEYxo_TvToaMqgu7jwJ3I8VilxFBV5fB-kZfM0g0LX_5jgofu1ODTkcKJgm9RuHxaKc3bPfaN9TcHeETbK4KGeXpcSYcS5fR9T68k4VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه:   ما به توافق خیلی دور و خیلی نزدیک هستیم</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/SBoxxx/16555" target="_blank">📅 17:35 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16554">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">سخنگوی وزارت خارجه:   ما به توافق خیلی دور و خیلی نزدیک هستیم</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/SBoxxx/16554" target="_blank">📅 17:33 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16553">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">سخنگوی وزارت خارجه:
ما به توافق خیلی دور و خیلی نزدیک هستیم</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/SBoxxx/16553" target="_blank">📅 17:31 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16552">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">—یک مقام ایرانی به الجزیره:
«ما با میانجی پاکستانی به یک تفاهم‌نامه رسیده‌ایم و در انتظار پاسخ آمریکایی هستیم.
تفاهم‌نامه شامل پایان جنگ، برداشتن محاصره، باز شدن تنگه هرمز و خروج نیروهای آمریکایی از منطقه جنگی است.
تفاهم‌نامه مسائل هسته‌ای را شامل نمی‌شود زیرا پیچیده هستند و زمان کافی برای مذاکره نیاز دارند. پس از ۳۰ روز از توافق، دربی برای مذاکرات هسته‌ای می‌تواند باز شود.
پیش‌بینی شده بود که رئیس ستاد ارتش پاکستان تفاهم‌نامه را در تهران اعلام کند، اما برای هماهنگی با واشنگتن رفت.
برای ایران امکان‌پذیر نیست که امتیازات بیشتری نسبت به آنچه در تفاهم‌نامه مقرر شده است، بدهد».</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/SBoxxx/16552" target="_blank">📅 17:28 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16551">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hl2hORowzXQHAQL44temLipJh3judMODpRv_i9pSzdMGfyoTVMwLfgOb_RGo9qprag8M9eMCHwSGIfc5uhsIOci3WzTlio9hDe9Hn-shM_vq_LILCBTqTddVmmAKEAA0oy11evGWmyeMq9D9J5RG9Q98ktRCUOTa3AvlogZzPb-Tt3MJFMXIuTc6Wl2NW5gw5WJUhw4nsEPY_RGuMet3BAcOhs5ecfpmICE2YQhgnFXkIauUZtHp8f_Ffn9ODtFrmjIT807MF2eFGXOyVgXYnXh7ffJEwqyaJPxBFoSXTXwyoP4SOqOidVBD-xNffIPE3kvPTC8NzpoUVLgF10hu1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سبحان الله!  نکشی مون آبجی!  انشالله فقط کاربرد نظامی دارد دیگر؟!</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/SBoxxx/16551" target="_blank">📅 17:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16550">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVEnWld6d8Eup6glp-wT9kLGuGYAwO0UrGI4ZCKcsUMPtNFPIL7V06OUQOr2rBIVFvb60Dtj77AVSFn2E1qeVBjXKnt8xJ5GBKHNrlVrDl4GQNSNS5KCVOw74JrUFcL268Nlzs8XdLIHDhgLPv7PSAH5ti-lpiRmJHxyhncMBD_D2NX0_SDeBPwGLjOXFTrFsdwCd6aunGkDLAFng48W9BYh_qGQW01tRO86MnarHLksZmoz3Lw13VAp9noRFeVIl_k4tj3aQp0fghmUA1KM-41rj7mVxYthxNtqKzdXBTptgyuL5yO8FtdtKAv-2wWgyr_TRBoJLNgjgqTrd-eebw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
تایید واگرایی میان اقتصاد اروپا با آمریکا پس از جنگ ایران
داده‌های اخیر PMI نشان می‌دهد اقتصاد آمریکا همچنان در محدوده رشد باقی مانده، در حالی که اقتصاد منطقه یورو به‌ویژه در بخش خدمات وارد فاز انقباض شده است. این واگرایی می‌تواند در ماه‌های آینده به یکی از عوامل اصلی جهت‌دهنده بازار ارز، سهام و اوراق قرضه تبدیل شود.
در شرایط افزایش تنش‌های ژئوپلیتیکی و رشد هزینه انرژی، آمریکا به دلیل استقلال انرژی و عمق بازار داخلی مقاومت بیشتری نشان داده، اما اروپا به‌دلیل وابستگی بالاتر به واردات انرژی آسیب‌پذیرتر شده است. تداوم این روند می‌تواند به تقویت دلار، فشار بر یورو و تغییر مسیر سیاست‌های پولی بانک‌های مرکزی منجر شود.
🔗
ادامه یادداشت را از اینجا بخوانید!
💬
ارتباط با پشتیبانی :
@cyclicalwavessupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/SBoxxx/16550" target="_blank">📅 15:50 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16549">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/SBoxxx/16549" target="_blank">📅 15:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16548">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">کارمای اجدادمان که سهل است، کارمای قابیل دیوث را هم سوزاندیم در این زندگی</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/SBoxxx/16548" target="_blank">📅 15:22 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16547">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">صبح تا شب این وضعیت مجریان ماست در سداوصیما ، در ماهواره هم که فقط صحبت جنگ و حمله است، نت هم با گیگ ۵۰۰ هزار تومانی باید برویم تانکرترکرز و فلایت رادار و اکانت کله زرد پفیوز و حساب محمد something های وطنی را چک کنیم ببینیم کی جنگ بعدی می‌شود!
بعد این نکبتهای انگیزشی میگویند بیدار که شدی به دنیا لبخند بزن!
به … عمه تان لبخند بزنید قرمساق ها</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/SBoxxx/16547" target="_blank">📅 15:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16546">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سبحان الله!  نکشی مون آبجی!  انشالله فقط کاربرد نظامی دارد دیگر؟!</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/SBoxxx/16546" target="_blank">📅 15:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16545">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlDr9_0EDM81gcUOTpp6QmyuSNJX9P-ibf11o3T9LnE0bW9AP2tTy0MlMsMCH1XQObI5YVQUUePT3N20WTusyzCdljV8JMbMRLGif5YKoJCeVyVnE7pmeZV7MWYJVbXy3dsJr1z-BtreQfK3JVp2ZZFod0k0BON2E5yCtsmHpHSbsKioaOCUViExsrBxnACunM2RX4tazBR7DVXI-iQlFrxtNRTe2e709-_iixkE6p8bPuDDUH5NF0KsT30k5gRqE1IEWpWAPa5WtBX_C6SSNqZgM3ivqiipUSd2TaPVVJYnZWdALpiD2BGqwec4uQmL7xGFeUhXHDHJMy1GK0okPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سبحان الله!</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/SBoxxx/16545" target="_blank">📅 15:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16544">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ترامپ اسرائیل را از مذاکرات ایران حذف کرده است!
به گزارش نیویورک تایمز، این واقعیت که اسرائیل «تقریباً به طور کامل از حلقه مذاکرات آتش‌بس» بین ایالات متحده و ایران خارج شده است، به یک «شکست خوارکننده» برای بنیامین نتانیاهو، نخست‌وزیر اسرائیل تبدیل شده است
نکات کلیدی:
🌏
دونالد ترامپ بیبی را به عنوان متحدی از ایالات متحده می‌بیند، اما نه به عنوان یک شریک نزدیک در مذاکرات با ایرانیان
🌏
اسرائیل از شریک برابر کاخ سفید به «چیزی شبیه به یک پیمانکار فرعی برای ارتش ایالات متحده» تنزل یافته است</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/SBoxxx/16544" target="_blank">📅 14:54 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16543">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ژاپنی‌ها آمپولی ساخته‌اند که می‌تواند عمر گربه‌ها را تا ۳۰ سال افزایش دهد.
یکی از دلایل اصلی مرگ‌ومیر حیوانات خانگی پیر، بیماری مزمن کلیوی است. به مرور زمان، پروتئین AIM که باید بدن را از زباله‌های سلولی تصفیه کند، به سادگی از کار می‌افتد.
اما دانشمندان تزریق‌هایی با AIM مصنوعی ساخته‌اند که مستقیماً تصفیه کلیه را تحریک کرده و با سموم مبارزه می‌کنند. این تکنیک حتی در گربه‌های بسیار بیمار نتایج قدرتمندی نشان داد.
انتشار جهانی این دارو تا سال ۲۰۲۷ پیش‌بینی می‌شود.</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/SBoxxx/16543" target="_blank">📅 14:37 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16542">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">📡
وزیر ارتباطات دولت
:
این نگاه قیم مابانه که اینترنت را خلاصه در ۲ پیام‌رسان داخلی می‌داند و برای مسیر اینترنت مردم خط کشی می‌سازد ، نگاه قوه عاقله حکومت نیست</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/SBoxxx/16542" target="_blank">📅 13:06 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16541">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ایران یک اطلاعیه نوتام صادر کرده است که پروازها را تا صبح روز دوشنبه در بخش غربی فضای هوایی خود محدود می‌کند.  البته خب منظور پروازهایی است که می‌شود ممنوع کرد ولی خب  از توجه شما به این موضوع سپاسگزارم!</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/SBoxxx/16541" target="_blank">📅 12:28 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16540">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">استعفای تولسی گابارد: ایستادگی در برابر از سرگیری جنگ با ایران؟
تولسی گابارد ممکن است به دلیل سرطان همسرش استعفا نداده باشد، بلکه به گفته مجری TYT، چنک اویغور، به خاطر امتناع از همراهی با برنامه‌های ترامپ برای از سرگیری جنگ با ایران این تصمیم را گرفته است.
ت.</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/SBoxxx/16540" target="_blank">📅 10:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16539">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">هیئت قطری که انتظار می‌رفت حداقل تا روز یکشنبه در ایران بماند، دیشب پس از دریافت دستور فوری، ایران را ترک کرد.</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/SBoxxx/16539" target="_blank">📅 09:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16538">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ایران یک اطلاعیه نوتام صادر کرده است که پروازها را تا صبح روز دوشنبه در بخش غربی فضای هوایی خود محدود می‌کند.
البته خب منظور پروازهایی است که می‌شود ممنوع کرد ولی خب
از توجه شما به این موضوع سپاسگزارم!</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/SBoxxx/16538" target="_blank">📅 08:45 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16537">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">تحلیل من این است که ترامپ فعلا میخواهد یک دور کوتاه از حملات شدید را انجام داده و سپس اعلام پیروزی و پایان جنگ کند تا در آستانه جام جهانی، کمتر زیر فشار افکار عمومی باشد.
اما جنگ اصلی برای چند ماه بعد خواهدبود.
در واقع این جنگ کوتاه را می‌توان یک موج B درنظر گرفت که از سقف موج ۳ ظاهرا فراتر می‌رود اما هنوز بخشی از موج ۴ است
سبحان الله!
این هم نتیجه مکاشفات و مطالعات ما با گیگ ۵۰۰ هزار تومنی در روزهای مثلا تعطیلات!</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/SBoxxx/16537" target="_blank">📅 08:10 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16536">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rqR9jqmspVQ-GT5X6Nz0q0-NfRjZ_3iiZMyRcs99uplwqufXKEnt-2x_Bqz8B4rtfeiIDiMfm_X9xIqRP1r8upW0o3xfQh4kxriAlSMJV3ZdBLdST-Reo83qW4kUGOYr10yAh79cg0BX4MaZNlkovQAZbpcPJ_W3tsg3Tn6XKwToVYxWevFBZRjqRZ3Ykkcs8QsOJqk2vuJ052gN-HNTTX7oXp67ypWUdhT6SrUEOh8gF6EglgDKl0Wy40S-pjPHYlrzaJf059iuKmadr8Cl15rJc9SLH7cPnshtTpXDVFh5wFr4YQDN20L1QelNWntTYNZ_jrk8BmaWboIB3XddCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت دادگستری ایالات متحده دستگیری محمد باقر الصعادی، چهره ارشد در گروه شبه‌نظامی عراقی کتائب حزب‌الله که توسط ایران حمایت می‌شود، و انتقال او به خاک آمریکا را اعلام کرد.  طبق این بیانیه، الصعادی حملات علیه منافع ایالات متحده و اسرائیل را هم در داخل ایالات…</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/SBoxxx/16536" target="_blank">📅 07:54 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16535">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mM08AJ8sag0VC1Dxh8V8COW1TPMJqIxVHPOF2SmvF-l1gvdTpFdIkrTUE25QVHPRL4uh7h8SR6I3kG36m-EztOFjuWV6qh93V_q0NYQXTS1sMPusonguUSoofwetQX7xAg4XMRhpJWxDtypzauRgsm3G6HltZzkvI1hMEEWKUIAHzGnTnNSzceNxJV9PbVH7SHta66wnCwOHb93QAPXsXZFERwFcmrMbIln2G4Mf3QrX2GN-PDUWuBQ1gdM-GFvtYUKNtohyHgkCxRe2vsFJixF_e1JgkkV62zCVLTRLWeLAZuODY7YMHw_jAlMvm584r3Gyb0vLb3aSHPVQZ0tLQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری سی‌بی‌اس در یک پیام فوری اعلام کرد که دولت ترامپ در حال آماده‌ سازی برای احتمال دور جدیدی از حملات علیه ایران است.</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/SBoxxx/16535" target="_blank">📅 05:10 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16534">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">یک مقام آمریکایی که در جریان تلاش‌های دیپلماتیک قرار دارد، مذاکرات را «رنج‌آور» توصیف کرد. این مقام گفت پیش‌نویس‌ها «هر روز رفت و برگشت می‌کنند» بدون اینکه پیشرفت قابل توجهی روی بدهد.
یک منبع نزدیک به رئیس‌جمهور آمریکا، ترامپ، گفت که ترامپ در چند روز گذشته به طور فزاینده‌ای ناامید شده و احتمال یک عملیات نظامی بزرگ نهایی را مطرح کرده است، پس از آن ممکن است پیروزی اعلام کند و جنگ را پایان دهد.
میانجی‌ها در تلاشند تا یک توافق موقت بین ایران و آمریکا را تضمین کنند تا از حملات جدید آمریکا و اسرائیل که مقامات هشدار داده‌اند ممکن است ظرف چند روز رخ دهد، جلوگیری کنند.
پاکستان، قطر و دیگر بازیگران منطقه‌ای در تلاشند تا اختلافات درباره برنامه هسته‌ای ایران، رفع تحریم‌ها و مسائل امنیت منطقه‌ای را کاهش بدهند.
هدف، توافق جامع نیست، بلکه چارچوب موقتی است که آتش‌بس را تمدید کند و اجازه دهد مذاکرات گسترده‌تر ادامه یابد.</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/SBoxxx/16534" target="_blank">📅 00:41 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16533">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OnWhsPTgONkdtNjZHbANl7qSXw6ok6hdt1QmyBtQKlO2X5YKDZ2wTAglU1QfwuG1ofJj7mHgsY9mHgElKb-AtX4ItlUBOw3ElnlmIVl_-bA_17z2kWfxH7St2e0PcXSsRrRSun5JbFBleWgPD7uGuTacOIhdzHd9e72GqsDX-8RluYsjc8MwpYCo9734jHL1zxDpsVzXbdqfiFBUnhaA9oxmgrDJlFO82VLYJjMDweHS6Q-MHsWbYK8txhY7Wq7C9vgunpRG2Weiwcn6vdV2gMyzekJtkPpW89vT2hqbANrSdaxOradOmGAKEc-VAAPcFjUIPuVjrK9I-sw5I-aP5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کوین وارش رسماً به عنوان رئیس جدید فدرال رزرو ایالات متحده سوگند یاد کرد</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/SBoxxx/16533" target="_blank">📅 00:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16532">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">خب به صورت رسمی از این طرح رونمایی شد.  در واقع در این طرح که حریم دریایی نهاد تنگه خلیج فارس نام دارد، عملا بخش‌هایی از دریای عمان هم شامل می‌شود که اساسا ربطی نه به خلیج فارس دارد نه تنگه هرمز و صرفا برای فشار خفه کننده بر امارات طراحی شده است.</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/SBoxxx/16532" target="_blank">📅 23:25 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16531">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ایران: آخر هفته‌ای بر لبه تیغ
۲۲ مه ۲۰۲۶ | پیترو باتاکی
مذاکرات درباره ایران همچنان ادامه دارد، اما اختلافات اصلی همچنان پابرجاست. قرار بود امروز ژنرال عاصم منیر، که بسیاری او را «حاکم واقعی پاکستان» می‌دانند، به تهران سفر کند، اما بنا بر برخی گزارش‌ها این سفر لغو شده است.
شکاف میان ایران و ایالات متحده همچنان بسیار عمیق است؛ به‌ویژه در موضوع برنامه هسته‌ای، انتقال ذخایر اورانیوم به خارج از کشور و همچنین مسئله کنترل تنگه هرمز. طی روزهای اخیر گزارش‌های متعددی درباره اختلاف‌نظرهای احتمالی میان واشنگتن و تل‌آویو منتشر شده است؛ گزارش‌هایی که حاکی از آن هستند که بنیامین نتانیاهو برای حمله مجدد به ایران بی‌صبرانه فشار می‌آورد، در حالی که دونالد ترامپ با احتیاط بیشتری عمل کرده و در تلاش است از طریق مذاکره به توافقی با تهران دست یابد.
با این حال، این احتمال نیز وجود دارد که چنین گزارش‌هایی صرفاً بخشی از یک عملیات فریب و انحراف افکار عمومی باشد؛ تلاشی برای پنهان کردن اهداف واقعی آمریکا و اسرائیل و فراهم کردن عنصر غافلگیری برای موج جدیدی از حملات که این بار قرار است سرنوشت‌ساز و تعیین‌کننده باشد. از این رو، به نظر می‌رسد آخر هفته‌ای بسیار پرتنش در پیش باشد.
در میدان نیز وضعیت تغییر محسوسی نکرده است. آرایش نیروهای دریایی و هوایی آمریکا نه تنها کاهش نیافته، بلکه در هفته‌های اخیر ده‌ها پرواز باری تجهیزات و تسلیحات جدید را به منطقه عملیات منتقل کرده‌اند. این جنگ هزینه‌های سنگینی به همراه داشته و فشار قابل توجهی بر ذخایر تسلیحاتی وارد کرده است. تنها در شانزده روز نخست درگیری‌ها، بیش از ۲۵ درصد از ذخایر موشک‌های تاماهاوک و حدود ۴۰ درصد از موشک‌های رهگیر تالون مورد استفاده در سامانه‌های دفاع موشکی تاد مصرف شده‌اند.
بر اساس گزارش اخیر مرکز پژوهش‌های کنگره آمریکا، تنها یک ماه جنگ حدود ۳۰ میلیارد دلار هزینه در برداشته است. همچنین ۴۲ فروند هواپیما، بالگرد و پهپاد یا نابود شده‌اند یا آسیب دیده‌اند که ارزش مجموع آن‌ها حدود ۲.۶ میلیارد دلار برآورد می‌شود؛ هرچند نویسنده معتقد است ارقام واقعی احتمالاً از این میزان نیز بیشتر است.
در سوی مقابل، ایران همچنان بخشی از توان فرسایشی خود را حفظ کرده و گزارش‌ها حاکی از آن است که در طول هفته‌های آتش‌بس، چندین شهر موشکی زیرزمینی را دوباره فعال کرده است. در چنین شرایطی، اگر جنگ وارد مرحله جدیدی شود، نمی‌تواند برای مدت طولانی ادامه پیدا کند و باید ماهیتی قاطع و تعیین‌کننده داشته باشد. در غیر این صورت، طرفین ناچار خواهند بود برای مدت نامحدودی با وضعیت کنونی کنار بیایند؛ نوعی «جنگ سرد» که در حوزه‌های اقتصادی، مالی و شناختی جریان دارد.
کنترل تنگه هرمز همچنان مورد مناقشه است و حجم تردد دریایی هنوز فاصله زیادی با شرایط عادی دارد. همچنین محاصره بنادر ایران که از ۱۳ آوریل توسط آمریکا آغاز شده، همچنان ادامه دارد. محاسبه ترامپ این است که ترکیب تحریم‌ها، محاصره اقتصادی و فشار نظامی در نهایت موقعیت مذاکره‌ای تهران را تضعیف کرده و ایران را وادار به عقب‌نشینی خواهد کرد.
محاصره دریایی به‌ویژه فشار قابل توجهی بر اقتصاد از پیش آسیب‌دیده ایران وارد کرده است. ظرفیت مخازن ذخیره‌سازی داخل کشور به حدود ۷۰ درصد رسیده و همین موضوع تهران را ناچار کرده است برخی نفتکش‌های قدیمی را به انبارهای شناور نفت تبدیل کند. طبق گزارش‌ها، دست‌کم ۵۰ نفتکش ایرانی در حال حاضر برای ذخیره‌سازی نفت مورد استفاده قرار می‌گیرند که نسبت به آغاز محاصره، حدود ۶۵ درصد افزایش نشان می‌دهد.
ترامپ بر موفقیت این راهبرد حساب باز کرده است، اما این رویکرد ریسک‌های قابل توجهی نیز به همراه دارد. زیرا تداوم این وضعیتِ «جنگی که رسماً جنگ نیست» می‌تواند پیامدهای گسترده‌ای برای ثبات اقتصاد و نظام مالی جهانی داشته باشد و در نهایت هزینه آن نه تنها بر دوش بازیگران منطقه، بلکه بر دوش شهروندان عادی آمریکایی نیز قرار خواهد گرفت.</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/SBoxxx/16531" target="_blank">📅 23:20 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16530">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HLl7OePfW01zZh15BNJl7wGzYYwyEoRF2IfCS5p_AI04MrAz7v_iLh-VZJ7TX9omz-874E_MEO7PseIYzIx7wdwDEGdZXAocllaxtSxfQ5xLk2BQ5rgaQGhkfH6yNztD8hHsiYSYev-kFzByMUhkeJSmU05BEHppyjWWJY582YpSpPm4xnguHV1wzwobxr3DdTeyKQTZitinUEzOGM7XXxLG0sOjuUohOolfHr4R4xYGI-kGyQVScgWarlc4AZqgGU0o92JU_4fc8KU-FScU7Jgisu5uHeIJ06kqRYCWMclj5wxu8UrePlOVg7kS3lIrU9nUFTCB0oFOeyqtq7gnSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ فرزندآوری در کشورهای جهان
نکات کلیدی:
حدود
۷۱ درصد
از جمعیت جهان اکنون در کشورهایی زندگی می‌کنند که نرخ زاد و ولد در آن‌ها پایین‌تر از
سطح جایگزینی
مورد نیاز برای حفظ اندازه جمعیت است.
نرخ باروری چین به تنها
۱٫۰ تولد به ازای هر زن
کاهش یافته است، در حالی که هند نیز با
۱٫۹
پایین‌تر از سطح جایگزینی قرار گرفته است.
آفریقای زیرصحرا دارای بالاترین نرخ‌های زاد و ولد جهان است که به ترتیب توسط
چاد، سومالی و کنگوی دموکراتیک
رهبری می‌شود.</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/SBoxxx/16530" target="_blank">📅 23:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16529">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26ffd0c130.mp4?token=mzpQoAFQfdcZByZjU6TeYEnJEcYygSten2X_-XPr5pbddhmuZ11BI9SOboqCMyALc8SfvyvxO4NwyF3otd14Wp3rhL8Z1o_hUaEf34rPdiZbp5WXjMiij7pvmdlrdiBi-ykmnPPjP-JShA63vp8mEy564289om0UXoY_xIx6JgI-Ji7Ij-rnYSffP0EoT2MKA7Qs40x90MOq33o_b12K8-ZPL2hHpnozJc2IOpzCONLGALwIFG9b-aGAsUvRqDorh0R81ccoYc6fDX8WoZhjjLEQh0TIPKvisaouThyV0X4gA6_Vfq4nCxu_x-N4EcXj00Y2lwKI3zhJTNaP35ecgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26ffd0c130.mp4?token=mzpQoAFQfdcZByZjU6TeYEnJEcYygSten2X_-XPr5pbddhmuZ11BI9SOboqCMyALc8SfvyvxO4NwyF3otd14Wp3rhL8Z1o_hUaEf34rPdiZbp5WXjMiij7pvmdlrdiBi-ykmnPPjP-JShA63vp8mEy564289om0UXoY_xIx6JgI-Ji7Ij-rnYSffP0EoT2MKA7Qs40x90MOq33o_b12K8-ZPL2hHpnozJc2IOpzCONLGALwIFG9b-aGAsUvRqDorh0R81ccoYc6fDX8WoZhjjLEQh0TIPKvisaouThyV0X4gA6_Vfq4nCxu_x-N4EcXj00Y2lwKI3zhJTNaP35ecgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭕️
آزمایش و رونمایی گسترده چین از نسل جدیدی ربات‌های انسان‌نمای پیشرفته با قابلیت‌های نظامی و امنیتی
این ربات‌ها در نمایش‌های عمومی شامل حرکات رزمی، تعادل پیشرفته، پرش، و تعامل مستقل با محیط هستند و توسط چند شرکت رباتیک چینی به‌عنوان نمونه‌های «آماده کاربردهای میدانی» معرفی شدند
فیلم ارسال شده مربوط به رونمایی حرفه ای یکی از ربات های انسان نمای بومی در آنتن زنده صدا و سیما است:</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/SBoxxx/16529" target="_blank">📅 16:59 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16528">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🍆
طبق ادعای برخی منابع ، عاصم منیر ، بلندپایه ترین فرمانده ارتش پاکستان به زودی راهی تهران می‌شود
🔻
رسانه ها این امر را نشانه ای از پیشرفت قابل توجه مذاکرات می دانند</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/SBoxxx/16528" target="_blank">📅 16:43 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16527">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
الجزیره به نقل از منبع پاکستانی
:
بالا رفتن سقف خواسته های جمهوری اسلامی ایران و دولت ترامپ در بحث تنگه هرمز و اورانیوم های غنی شده ، منجر به بن بست در مذاکرات شده است . ما همچنان به حصول توافقی واقعی خوشبین هستیم</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/SBoxxx/16527" target="_blank">📅 12:45 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16526">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jtul1R4essefPT8zxEehKp5_s8xsRkGNkRZ5G4_jN4WpAJrl87VJ3q2-HMcDBEO45qdSOIhRefl4QBVWHOaM8WJN4pDqjo88EWazFGClBpPiJNuia-_YU1i35jSjXVRTHGnu5SiH4DYaSpfs-itC9mJvi86lIFt7y9y6OE45CfVgi1vraV5TLwnEltAipcp8Sg4yCfSHiS9VXLUYjT-CPK4SJreVzpy7ap08b9N_s4yno6hIy8ybn7ogH_dXP9wCVdnnxXHKWhtvKKKNo9BSjI1BbYk89XDX4Dh5blrRwZZlVIaCfgGeSkhL-5oLac2vnKg791CHVHW1y7sOCyUoYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#TUR — D  عیناً طبق مسیر می تواند با تکمیل این سروشانه که همسو با پایان یک رالی 5-موجی است یک افت سنگین اصلاحی داشته باشد و سپس رشد اصلی طبق مسیر پست ریپلای شده محقق بشود.</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/SBoxxx/16526" target="_blank">📅 10:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16525">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FXF5EM01wANZiWbYeWOkAdhCxhcMS1jEnOV2Ua7IblpzWU1-IOEE1DlooA1--YVOrGNBd-eVxtbyZcIXXVutnpHDbAoCfAwx2IltRMRebu8vPx9nwhMf2JYA1WtBSbRpwPqXEF8xsXlBOdoUssQ3wbzKE5DlTnh1ssYdkeCM2tFphKJQgLWIFhKRa0VWfUIoa9WG7HR1P62N-kN8w6fw2oq8bAOa0qH-KKQZRkjrNwl7cWdxbnyibKYC1ceszIh8_4ZVYLSy3q6XLAHr9Xtv1FswkSakrN5lURXCM0xMS8lFI5YB3gc02hrC16k19ILiRN_LcK8TiJ6jqM995w0awg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#TUR #Turkey
🖊
با داده هایی که اخیراً منتشر شد (موافقت ترکیه با پیوستن سوئد به ناتو و انعقاد قرارداد خرید تسلیحات 23 میلیارد دلاری بین ترکیه و آمریکا) به نظر می رسد سناریویی که اینجا گفته بودیم (نزدیکی دوباره ترکیه به غرب) در حال تحقق باشد.  این نموداری که…</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/SBoxxx/16525" target="_blank">📅 10:50 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16524">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fShAujtrok_s4GWGFGEiEPhLYfksTmTLINaZzY8c_7wlsMBsO46rTsKgG2qFkoV-5l_iYRWJzjmkAen6DFRbejCn5QkT-byBuTuix_gD1yh9vfpUG0MofWi_2MI2lU39VRndnMuiTqluEQ0pBMLf5uarki3Hjmv78S1bTH2v-djUj77UQQp8jMdJikeTRr6jKaHbYbM0WiE3kqcr7gefa82AK5u4yF_f3qECDI5Fwvo5O8Y8SFn9qgWTcY9k0sZgDPM2bupcb8HkHoftpdRouhw81HgP5vCmIy5WO3_AWAT3ddsulVdK0L_iQ7MdbcvEqWDYPLjwh0Ze8qUgX4Mp6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سقوط آزاد شاخص بورس استانبول در پی صدور حکم دادگاهی درباره ابطال نتایج رقابتهای درون حزبی حزب اپوزیسیون جمهوریواه خلق</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/SBoxxx/16524" target="_blank">📅 10:46 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16523">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">دولت ترامپ فروش ۱۴ میلیارد دلاری سلاح به تایوان را متوقف کرد  بر اساس اظهارات هونگ کائو، سرپرست وزارت نیروی دریایی آمریکا، دولت ترامپ فروش ۱۴ میلیارد دلار سلاح به تایوان را موقتا متوقف کرده تا ذخایر تسلیحاتی آمریکا برای جنگ با ایران حفظ شود.</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/SBoxxx/16523" target="_blank">📅 10:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16522">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">به نظر معامله بزرگی در راه است.</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/SBoxxx/16522" target="_blank">📅 10:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16521">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">انفجار در ابوظبی!</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/SBoxxx/16521" target="_blank">📅 10:04 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16520">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">وقتی صحبت از عقب ماندگی ذهنی میکنیم منظور ما این است!  رفته با دیوار سفارت آمریکا در ترکیه عکس سلفی گرفته!</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/SBoxxx/16520" target="_blank">📅 10:04 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16519">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QFnv3uzxfwidbTmf0AtSu2cBxNooxoTtRyB0OodlDOBLIG-mp3BtkWgM7m3x86Aal78V6A-CMYvhGm8obykNLsBUo0VIX3p1gyOW4XPuWloZWIgqmSdbbCz05KKhy6lbfATDM-reprviBt_ouPFZiC0008JTBa4Ae4pAoaiwg0Cgf3JRiWbGR9dXDILuyUDbFH1KdhYnku_JapJVYOAJnHvQTunxMH_4vUPweeAU2SWMRwYaHUliHg8vjCZ46RVHwEZE572T74fyS87V_hX8lDSIjnapo_gvD-6N3pqYrtZxt1sziDMhB06Kc3apa7ODYRyohLwZkTLPNdruINBYjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۸۰ درصد هم عقب ماندنی ذهنی داشتیم که ۱ درصد آن را جبران کردیم ولی خب هنوز خیلی کار داریم و نباید بهانه بیاوریم.</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/SBoxxx/16519" target="_blank">📅 09:30 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16518">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jgvy0CIDYfvB9wrHDwVW84C2rin4uEfVlyAYIisbEWVhBhkDbr3P-bOIkFspu7O54Aa_XZHZ7GyiAH4Nsgivj-2SoqDVaI2yj1pbHBHbAXSdFXic3iKyRW3uLbSiuEnF4-vjDkkpn1DHFvJ3HNOhClhZ6TPyriXsbvKVvYRonXdg7GDcqk8vHj7rh2kBBGfYFIEBgMLZ4V4xK5kNt_y9OIP9CHs2L1k_dsvshrPkmkg9m-IgcYfZViyGRy3TZBma_FMSE5T1q4aR65739w6bF0NxBqUGGtrUflCxYJsftWcZOuNJjOfg7ImGFVomVoBURS5lss4Sf0u1z8OugnQ-hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت سهام چین</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/SBoxxx/16518" target="_blank">📅 09:17 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16517">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">رئیس کمیته نظامی ناتو:
پهپادها نوعی مسئله انقلابی در میدان نبرد هستند. آن‌ها تنها سلاح نیستند، اما احتمالاً برجسته‌ترین سلاح خواهند بود و بر کل فضای نبرد تأثیر می‌گذارند.
احتمالاً در درگیری‌های آینده، آن‌ها اولین چیزی خواهند بود که در جنگ درگیر می‌شوند. آنچه اساساً آموخته‌ایم این است که آن‌ها به‌طور چشمگیری زمان چرخه کشتار را کاهش می‌دهند.
این موضوع به دقیقه‌ها — یا حتی ثانیه‌ها — برای شناسایی، ردیابی، تحلیل، کشف (شناسایی)، شلیک، ارزیابی خسارت و تغذیه اطلاعات به عملیات بعدی تبدیل می‌شود.</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/SBoxxx/16517" target="_blank">📅 07:50 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16516">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XgoTdW0tvHsCvANQEFe3N_2t6dXCDcdhxqt6hQi8R6IhRkQbnUr1CynMUR64oj1pdQVDEfvChqXt3CVNXzOjZo4pBpTN54JehqVJknNy0Nv4QSsCtm7_PTVTNlzDVdSw2nX9T0GYvjFzGN8ev_oYxUPqQAxZQ-BYUkspxGg7CzUVSn75-eYzx0gE0rC26CmFU9oLdtOg_gCLn5Yvb1UhpnTE5GEMqyEm6QKtYcQyLX09ipOZUa21j2BMONxskPL4SNwRWUNadOeIj3YLEPDTq1aXQwViML4H9hyqBSKPyFUVMP_j1_arW74W610QOxgPalzd41peNpMNDfvvGMKdlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/SBoxxx/16516" target="_blank">📅 01:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16515">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">این جنگنده ایرانی هم امروز در تهران مشاهده شده که ولی خب.</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/SBoxxx/16515" target="_blank">📅 01:39 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-16514">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">شماها چرا شب جمعه اینقدر میخند؟!</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/SBoxxx/16514" target="_blank">📅 00:14 · 01 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
