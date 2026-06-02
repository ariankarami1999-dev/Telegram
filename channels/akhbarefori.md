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
<img src="https://cdn4.telesco.pe/file/Jx89lhYv5oG-8bZc6YxvVyFZS09K52PAJ0wE6dVsAmjr3E-OJQf95fRsheSoai4WNlYJxQSQe6m5onuPjOaQ8WwCn5AVAYyOnucHM79zGQ3mZOZzCBGgylDSv3U2nP6NoP6WbE_uGDb_Q3kS46THm_OsqvEjMygqjoG61IT3L_gz8uSPcF3-ITxILdFumLwKLGonrj0tg8DJRHxAZ3cAX3N01MkhSzkmQTBXAybUfq0gATpNVKxgzDB7m7BcAeqHnsKUioIbTMBEDVOvgaou9W5t0rs2birIqdF6FjvGob_1inBAyimuA4_JUbxq1B0IYJA-LMqgMOEXF417OHLlhA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.02M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-12 13:15:45</div>
<hr>

<div class="tg-post" id="msg-655429">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ioMzcNqmVv_nsWMZS8W8JqxtfRzi6CiYz0uQ93DZ-H7hUwax7_yjQsaEPYv3yNta2t7KSdoEEHFLp48uw-wbxsOa7ehyiXTEyXIbczies2Bf9DQSf5idirjRyHGc5Nlq0PR5QdmNRLgNCnA8SleXvvJgBXDHXyfeEQM4HWo767gHjwjBcBXpuEs4w2LKO9UuuDcXG5JkVFJSsphlx_UuabbY-fu4hpJXMMQxgS9Yuv3pc8tKc1JytIpOL59Jezx5EgHwxPPE5KPR91mPUazXHWcr3LG5pm4Et01XNMCItbgnRhRHukEMkL0ICmbfZakFtsfd2DIZFaiTSfwAckW76g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میانگین سنی تیم ملی ایران در جام‌های جهانی
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/655429" target="_blank">📅 13:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655428">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef7a3d1bc9.mp4?token=Z92M5U1uAg_4EAJSm68X6GEsArGJ4ho_HwkJGC82xZ5zzC8C51OvOqq0LI3J4J3WFbH7TqH32kSej6vHQsVl8XkEU9tp8rm4ghIQvX8wGawz_gU-ZCt7TjDsFrzr1sgeWYiYRjPc4_aOH6389On-XiJ9kTK83aHV56lmkdjHLIvBkXLINr40Rk-ggi6xo9P_k6-NeY-6SYKsoHIn2LqcDxGJdfeqlLkT4zFfayxv4uI-5yeFeFRgCwkYFtTXtaOUH0e9wZtORNV7FAfJWwlUls_B3dwd5S2U1O9LWLzcbz4W0qiky2GwyUm99sjJlhcFOI_IUlLjX4SMLtl9i6cZ_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef7a3d1bc9.mp4?token=Z92M5U1uAg_4EAJSm68X6GEsArGJ4ho_HwkJGC82xZ5zzC8C51OvOqq0LI3J4J3WFbH7TqH32kSej6vHQsVl8XkEU9tp8rm4ghIQvX8wGawz_gU-ZCt7TjDsFrzr1sgeWYiYRjPc4_aOH6389On-XiJ9kTK83aHV56lmkdjHLIvBkXLINr40Rk-ggi6xo9P_k6-NeY-6SYKsoHIn2LqcDxGJdfeqlLkT4zFfayxv4uI-5yeFeFRgCwkYFtTXtaOUH0e9wZtORNV7FAfJWwlUls_B3dwd5S2U1O9LWLzcbz4W0qiky2GwyUm99sjJlhcFOI_IUlLjX4SMLtl9i6cZ_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجری مشهور آمریکایی: ۱۶ میلیارد دلار به اسرائیل می‌دهیم در حالی که مردم پول خواروبار و بنزین ندارند
مگان کلی، مجری مشهور آمریکایی:
🔹
آن‌ها (آمریکایی‌ها) توانایی خرید خواروبار را ندارند، توانایی پرداخت قیمت بنزین را ندارند، توانایی خرید خانه را ندارند، توانایی پرداخت هزینه درمان را ندارند، و ما ۱۶.۲ میلیارد دلار فقط برای یکی از همین ردیف‌های بودجه به اسرائیل می‌دهیم.
🔹
آن‌هم در کنار هزینه‌ای که برای جنگ اسرائیل علیه ایران کرده‌ایم، جنگی که هیچ کس نمی‌خواهد. هیچ کس.
🔹
در عوض به مردم خودمان کمک نمی‌کنیم. آن مصرف‌کنندگان یارانه‌بگیر بیمه «اوباماکر» متضرر خواهند شد، چون ما اولویت‌های دیگری داریم؛ این واقعاً خشم‌آور است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/akhbarefori/655428" target="_blank">📅 13:11 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655427">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54688560ff.mp4?token=KUePslwK9fa3rOJutOp9380wo5LNlOoWRvnQGiezCRyBAsvKTFWqY_05ak9b_IpbGCfBR-RfXcb6RGASuTSkkqW7mNg1qb6ZKqpARkR-tNT4kV6vg5W4n1KI_aVufg2ujXd8O-xYZy_vfTSdOHAEFFhR60UMV1kKMvIbhGOvo78JZhKvi4vJetbsl26Qw8fybAWr5EdDb1xwNzXc2j_a5e7JVcunaAeqvobC5bvLH4DDvWLRGGi6l2Wl5xtiY0M_5H_kjkq5FjzEaXD34e6CGt_gp40NQvnZMgzZdwDoFeojY_HQNkPcDpBvcwfN6oNr9BBGTb1rzv5J3Jwu13ttdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54688560ff.mp4?token=KUePslwK9fa3rOJutOp9380wo5LNlOoWRvnQGiezCRyBAsvKTFWqY_05ak9b_IpbGCfBR-RfXcb6RGASuTSkkqW7mNg1qb6ZKqpARkR-tNT4kV6vg5W4n1KI_aVufg2ujXd8O-xYZy_vfTSdOHAEFFhR60UMV1kKMvIbhGOvo78JZhKvi4vJetbsl26Qw8fybAWr5EdDb1xwNzXc2j_a5e7JVcunaAeqvobC5bvLH4DDvWLRGGi6l2Wl5xtiY0M_5H_kjkq5FjzEaXD34e6CGt_gp40NQvnZMgzZdwDoFeojY_HQNkPcDpBvcwfN6oNr9BBGTb1rzv5J3Jwu13ttdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ده سال تراپی خلاصه در یک‌دقیقه #سلامت_روان
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/akhbarefori/655427" target="_blank">📅 13:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655425">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KWe-i7LhmKbLurz2I6eYS8VDQbouf7Vxr5CM44QOLZD8L8fbuTvLFRhveJ4gCNzHWzpMHopat8H4o4Pq5dxtQkaZ3uMKdBdByHsM3o4p2K3OgO0WEFEPycwMCu9cw85RSPhuFAo09tXVB9iIw_s2Kq2QuiLkgn6npHEmuj1elIDzbdqPJJ89KnLziUwkXCnCc_TGx1DUBqlLpPK8T15LcWt-Wb99Y7V6e3qAqZ_A43rXPT1GBAGgSF2vAm7Jm6LJKyBdLsSYtk5B4Kk3K_mEQ77xiPJfrU621BQc2HuS3J11eenor1gJ7CnCjOALu565MjY20UFlPOdqmgPHBJVOng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a4_yI2B70egX4d-jsqvoNK27t9_E7lmBybFRrWqGRvuHHbufBaY2dpckwY5qT5UmBgDS4BKsrZXE8vdf8fIP6oBPDEEeZiblaEPc-_13VnhUKtkN7sn3omemywkRoptGWYYDctqYxalwXglIulJhCciTdMW4YhXAWh91SmqXyGBMze4PXEht6IunngmTablX19h6VHHzaHo5eOLeocpF_Ud1Mdpv2ejMctqZsjSU4rULEWSqOWl4Gh7iH8b-bqMoqTN0bGdqQRylUSRf9hE4Tx7uD-jakgwL-J905yturKnwo9uvl6HtKn-DaVn62VaVNcaqF-yczsjbCFACM3oX2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اولین پرواز آزمایشی تاکسی پرنده در قزاقستان
🔹
این تاکسی پرواز آزمایشی بدون سرنشین خود را به مدت ۱۰ دقیقه‌ توسط خدمه زمینی به پایان رساند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/akhbarefori/655425" target="_blank">📅 12:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655424">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
امتحانات دانشگاه شهید بهشتی در روز پنجشنبه ۱۸ تیر به علت تداخل با کنکور ارشد، به شنبه ۲۷ تیر موکول شد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/akhbarefori/655424" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655423">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
عبور ۲۴ فروند کشتی پس از کسب مجوز با هماهنگی سپاه از تنگه هرمز در شبانه روز گذشته
سپاه پاسداران انقلاب اسلامی:
🔹
طی شبانه روز گذشته ۲۴ فروند کشتی پس از کسب مجوز با هماهنگی و تامین امنیت نیروی دریایی سپاه از تنگه هرمز عبور کردند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/akhbarefori/655423" target="_blank">📅 12:38 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655422">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HjY3NJmF-9udCEkAigN8Rj8FR6J0qS-IBMaEbVaqLnHGcXmEQzT6whZ5e3MszrRk-x2QpvdzPiW1Y5OW2ubEsRDVetDU0d4qxVQfYjeygV4-p8V0IZ5Jr4l12NeLgU7vjqE8HqbaOk3AwKQPakkLcdWmQWHE3lwgBTc4iEmy1Eyc1gueLcH2pdDN_JLB9sVFzv0yHnTSBnCbRXXhbbEqf7NLDT3DHsToOKWQ1SFS_ZpksGBFnG4KZrx0BJ9U3kv1pH3ojyDoVc7lbAD1qVM23oPRdxnoegFzwMzI1bqLYw-RnlTfWaKJ5DHwk3-WCANkSTN6Kg2NoFSAYAzz5oRh4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معاون حقوقی وزارت خارجه: ادعای ترامپ دربارهٔ منصرف‌کردن نتانیاهو از حمله به بیروت، نشان‌دهندهٔ نقش مستقیم آمریکا در تجاوزات رژیم صهیونیستی است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/655422" target="_blank">📅 12:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655421">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_af4aVwqPf70jHLsjipaIyJaqysczTdDH7s8WZ5UvEa5J3UHK1WFmWLlRQu0CZvv3Rywbku3rjQ53dRnPQDfc1JJqjEyTGRYL8wTjDjKL803ez9wsJYcoqAkvF-mAaF2KEYRPI_20nwzRBT-X7gMogGqWghT0NsL2P-o_Xb5T8zsAPBKhPQMjQF-Ku4Tdcjc203VGi9-I0Ap3JXe3MZnZZrwFcYScFgawld7InQbYT-ccrPeeNOo7HTlMoF54JHV-dBxMWAC3N5m2IkyW0SsSejSqqETj3BtVovtW1xQ8JHb1dMvf1RhEWagHJuGV77L4rmJ57bEqIVmT82aeQMEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رویترز: ایالات متحده سلاح هسته‌ای خود را در اروپا مستقر می‌کند
رویترز به نقل از فایننشال‌تایمز:
🔹
ایالات متحده در حال بررسی استقرار جنگنده‌های قادر به حمل سلاح هسته‌ای در کشورهای ناتو است.
🔹
این اقدام در زمانی صورت می‌گیرد که دونالد ترامپ، رئیس جمهور آمریکا و بسیاری از دستیارانش از متحدان اروپایی به دلیل عدم صرف بودجه کافی برای ارتش‌هایشان و اتکا به ایالات متحده برای دفاع از خود انتقاد می‌کنند.
🔹
این تصمیم پس از گفته رئیس کمیته نظامی ناتو که در صورت فراهم شدن شرایط در مساله تنگه هرمز مداخله خواهد کرد صورت می‌گیرد
./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/655421" target="_blank">📅 12:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655420">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
تکذیب خبر معافیات مالیاتی فروش تا ۶۰ میلیارد در سال ١۴٠۵
🔹
سازمان امور مالیاتی کشور در واکنش به انتشار خبر نادرست در خبرگزاری ایسنا، ضمن تکذیب شایعه «معافیت مالیاتی تا سقف ۶۰ میلیارد تومان»، تاکید کرد: موضوع برداشت اشتباه خبرگزاری ایسنا از سقف بهره‌مندی از «تسهیلات تبصره ماده ۱۰۰» بوده است
🔹
به گزارش رسانه مالیاتی ایران، سازمان امور مالیاتی کشور شفاف‌سازی کرد:
برای سال ۱۴۰۵، مشاغلی که مجموع فروش سالانه آن‌ها تا سقف ۷۲ میلیارد تومان باشد، می‌توانند از امکانات و تسهیلات مقرر در تبصره ماده ۱۰۰ قانون مالیات‌های مستقیم استفاده کنند؛
در این صورت، این مودیان از مزیت «عدم نیاز به ارائه اسناد و مدارک و اظهارنامه مالیاتی» برخوردار خواهند بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/655420" target="_blank">📅 12:16 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655419">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
پنتاگون ورود خبرنگاران به دفتر مطبوعاتی این نهاد را منع کرد.
🔹
انتخابات هیات ‌رئیسه کمیسیون‌های تخصصی مجلس، ظرف ۳ هفتۀ آینده حضوری برگزار می‌شود.
🔹
سینماهای سراسر کشور در روزهای ۱۴ و ۱۵ خرداد تا ساعت ۱۸ تعطیل خواهند بود.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/655419" target="_blank">📅 12:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655418">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YjzanW3KeZGVjgL1O-A6-zR2uUU3t7fyLASoV5Zp5SRzxMEEL-30WnXLR-wshczSJIDMiggtnK4go2grZXOnN2NTgVTglyQIrQaRkFoFpq0xn6f4mtfarUrympkUBgR01vz88t5DfCpacUReCRS40K6ROE8LZAo2haUa6-ECC6Wx7zZWxSnlh0a0xgg45E0TqngqQUTO7bkcry8ZeP5b-2s1vJOiE9Fl9-fpm7-nFL4nWfXpjqMj7D1pO_GmcFLs5o54KvFGQH2jnulBD51NtvrYMOK62Hwy3jDuwl4tbfBFqz4rjV60eVpfHDGEaabyYq6uecTBIa81I73jnWrmKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا مردم اخبار جعلی را باور می‌کنند؟ #آگاهی_رسانه‌ای
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/akhbarefori/655418" target="_blank">📅 12:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655413">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UJYqx2xXp_IqhwK0UhWNPzDWug03dPzAixoL8IurvPrngLGZ6Nfk09P1FM9D8q4fI35IVDEE-Yn_ZyMIJ08q0GDew6g7q7abOqjEmPqZnpDOhPzb1v0m0OSDYo76FIhKLOIW0mQIUuq9kjVx_QrGS3WmxH8_M5vQegEivJm_sPlG6vXqX49WvmUeaKbDtwdG2eOPE14EriF81WLIE-CyEpb9FBHMgUntYyYTS5BJ2OZk0kN9wGgHDlm5XwI7e3DHmu7djYb3Sy3f3hYLw2ZoSzB7kwm0Quq6LfT01F70yaoj4kh10QSrx_XM489dFsDh7v25V-i5XKW_ZeI3J8CcmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r3KfVMJkbIOZKRay0hv9XAswqAxEO92j4e3DynulJNIV9aMhS4LaGlYlCj_6K8yUjdAr-4jguJFzSK5SOJGknJCZ_5kAYQDRYEfO43dZREEe6y8bdOwvSxPY3UyYVqDj3_gCv-gudj_lgwefGSqfTUAHVjEkK9eq-40CUAsh4hvcjR2MDaccKYhMGyGLU1vhdEhE5-qpbc5bh9yh6g_mAVzbAJNzUapRNckeDwVSOl0x3iv-j8Cgg6iQIcLvWQW7hFJBkqCdU8gHPO058twTwOKexa1dngAprSL-UfaxI3sVFuFKBwP93mKBqs8mzBWD8uhxOwfosu6GgBPGlXFNqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jlSiwdXw4bZqZcZBh_kAeO5-EB-4-o31IBZGslTY5kX_Y-If120OqeAMf0s9-VJUPA_6lranSu_VkW59gRemIwOo5ZpHu0wjnrtBq3YW8BlfkkbpzLqZoNCKUgNSj3le3kBY9jnzKJUuqpcnQXc2LEzTis4hTKiTUkv6bPsDD_3Cw0qIwveqXmbIajL379I354nf6hUxM1gb9NpMaN98m69N0-67Tqu63EukbEgZxbqAXKBmnJv3h2zmF9DlInhi1Aq-T7slVKLWVjZslMcsXEX8Fd8dDabIkk4cvZz_3XLUfgeClK5oIbWW4ccgokr5ssVOAC8gUscjWob15Brdlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JUGiOqN_bk22ktzzHPQZzAj_0t2X5ga5IET8a8f5Tekp5t58bQYM_aMYHfXang2kF6BOxABDzh3uoxOXEuV2hYUV4kFP1vvuDMT-QJ2Yhis2JxchGfz3ghQKpWiKvwHjVW_b1eA_gcJVYDLyeEoUqyxcz2U9lBenZx2xfNJv40H7tJHis21xcOYqNl1naH8XdYSlTegSHxehWKgutXJXqEQeXm_sKGvQFr6xcPHAGtDK7psawhNOmZ4ncFeyvtguFImz9-LrTQTFJSZLyV95MqDv7tcyWb7VGhuM1N8kIwmtokwhfgU2cgCYzHq86TFp7OLm0FalXyDcqFe0Gy6bGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jLGnqEcUYTsd1gpwton0IEzC1uZNkUXysnoXfx1khW9HjtLP4FnEMRujNBA9qImcz0sVZXu2UQIb4TnXrDULUJhrJawj8ARoWO3OUJdLtTUuldxSeuLx5Z9cHsIYTBSz_bdsSGjdO2kVE5JceBMwv0zc7I2gvaVYa1DOCp-PVsmoW6L48isg0BM6DLAzOknGfEmKl4QQ5WXgIteCJZPUSNfKtEPXIYU_IWkgj59HCQy4OKZtoa-xWIDaQXxUTDwN0pnQG2Brc49cFFauBXsaxYRuRNgtlIvjhvtRdYCdlu4sW8du69BHIxlTDNhUaSq2XjhocKMo2W5J6VvLatID0A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
شگفتی سراسر جهان از طلوع زیبای «ماه آبی»
🔹
دومین ماه کامل ماه مه ۲۰۲۶ شب گذشته نمایشی دیدنی برپا کرد.
🔹
ماه آبی کامل ماه مه، نمایش خیره‌کننده‌ای داشت و آسمان شب را غرق در نور ماه کرد، در حالی که ستاره غول سرخ کژدم‌دل(آنتارس) در نزدیکی آن می‌درخشید.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/655413" target="_blank">📅 11:55 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655411">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQE5-Sn0Rt7uwiOJvlxeFo8nBiUdGkqOswKqI873AnkVZP5cACGIMWZSkOoIIWX-gTTiNxJVq3L8lkWDEovF7nOxklUBqCoL29pTGv380Gb7TKR9YU8sqoU7aGIP6k6xq-AbhTb7ZWbllvNYH8wM1lrZ2NhSWLUMzjR422pa-hpq-sDbkZuBA3CGDRiE3wSUvrN3gDKL1o7yg_xhAJt1a7S-YgAAxH5BA1n590JWKCZcAz4BV6KuI_RtlgbV9Vmxl-vbSvTasFzSTpXuFADXxY2SbQ8SZwvJJJoraCokDS9J7xeaDy6utm8rBJn4NsjL1NXeY0gDJe0Bnneye52SNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سرعت رشد اجاره‌بها کم شد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/akhbarefori/655411" target="_blank">📅 11:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655410">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/319da7afec.mp4?token=jyteRk2SITl5PPfVYh9CnWF3oAAfUp3uBhCKZA4_XXR7PzDGhD5IVEE6czhKspinOvaq19v2bPIA4ksCnX8UEhljrecTnCKCVd8rMs1JhixAKPUbD1UmS4-1e6l3VKbzCwHv59ApWjRQWD8VcL-ZscKnfLDEJtxhsOv-6NJPTpwWmwBFYw7HmIKq3p_YrTQ8PS-bILGYOklY8zdpVAWo35dA1ksWggeiYQ8-ZE2JxCtfWkUNN2aUosDjPXQJF66CK90Sb9l29uUsmvuymuz2wA5mVat8eUZhF_VZWVI3WDQKHqEc19Gniebp5GTa4C6wfAkII6lJMxRFzzAIcJ3zHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/319da7afec.mp4?token=jyteRk2SITl5PPfVYh9CnWF3oAAfUp3uBhCKZA4_XXR7PzDGhD5IVEE6czhKspinOvaq19v2bPIA4ksCnX8UEhljrecTnCKCVd8rMs1JhixAKPUbD1UmS4-1e6l3VKbzCwHv59ApWjRQWD8VcL-ZscKnfLDEJtxhsOv-6NJPTpwWmwBFYw7HmIKq3p_YrTQ8PS-bILGYOklY8zdpVAWo35dA1ksWggeiYQ8-ZE2JxCtfWkUNN2aUosDjPXQJF66CK90Sb9l29uUsmvuymuz2wA5mVat8eUZhF_VZWVI3WDQKHqEc19Gniebp5GTa4C6wfAkII6lJMxRFzzAIcJ3zHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از دوربین مداربسته در یک فروشگاه لباس در ویتنام وایرال شده است: این تصاویر نشان می‌دهند که فروشنده فروشگاه و یک مشتری، به مدت یک دقیقه به دور خود می‌چرخند و سعی می‌کنند یکدیگر را پیدا کنند
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/akhbarefori/655410" target="_blank">📅 11:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655409">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
مدیران خودرو، اجازه فروش ندارد
رئیس سازمان حمایت از مصرف‌کنندگان:
🔹
به شرکت مدیران خودرو اخطار کتبی داده شده تا هیچگونه فروشی با قیمت‌های خودسرانه انجام ندهد و مردم از خرید محصولات مدیران خودرو تا تعیین قیمت‌های قانونی اجتناب کنند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/655409" target="_blank">📅 11:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655407">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9956f384c1.mp4?token=SOwUtynC8vQ_M3Qx5_d96FobsutkHANcX6JgU7_DvaUEoUV8Kxvq1YS5y76hsH1U1iTEcmk0638DrUbyOBKHF-lFTAEJo1jxuHJFdzHdHf0P3EHJg5GaTI2nmtz6vHQ9FlE7bC1iWAA_rt4LqTGkUlf6OvR5xKaNlkuYE7wnXTD8fCWOwBGxux4sXjQI3MCSZbq4KVUCH9ZV-bUC9aNuu8ascwDiLEkFYUECEInMGXrSOF4PDzG3tKaW8yBsk6wxUz94MtNQykq7j6JBIqcdECN89hROI_E9Ae3bFsFiTsQPRN3v5wzh92kiGCh7g7lgO0YSQwMwiGCRD0rNUrGULw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9956f384c1.mp4?token=SOwUtynC8vQ_M3Qx5_d96FobsutkHANcX6JgU7_DvaUEoUV8Kxvq1YS5y76hsH1U1iTEcmk0638DrUbyOBKHF-lFTAEJo1jxuHJFdzHdHf0P3EHJg5GaTI2nmtz6vHQ9FlE7bC1iWAA_rt4LqTGkUlf6OvR5xKaNlkuYE7wnXTD8fCWOwBGxux4sXjQI3MCSZbq4KVUCH9ZV-bUC9aNuu8ascwDiLEkFYUECEInMGXrSOF4PDzG3tKaW8yBsk6wxUz94MtNQykq7j6JBIqcdECN89hROI_E9Ae3bFsFiTsQPRN3v5wzh92kiGCh7g7lgO0YSQwMwiGCRD0rNUrGULw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مولودی خوانی غدیر به زبان انگلیسی
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/akhbarefori/655407" target="_blank">📅 11:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655406">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgojGgHQbcmt19YsQLRGIeOJhyjYHo9vu-g3sbgkhhKgCTwjLAeZ_vR3SJNRqnkwSSxoT4dRPmn2lSw_jBRCjkuMMnMV9hYcflUIkvcp7zXFjT45uZwHaoQscMXVhYIGaT458qYfQXJRlUnzbIRzwyMwwXcs_1ZuxP-1Ejj-rx3DqeB-b3uZlnEmu_JWirfnF20ZW7J_cxTDNVfV05li8zE-mI8QmwXRH94wFsjUxBZsGQtqFgKo-u8iZideXGSlpAG1s2FZb7nbIlb6Pqkh1znEeYoFhrerki9Z8UJi-kTk5HIYmzEQUSFK9NSpq0Caat-1qmnUMOspW-OwF53ItA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پردرآمدترین ورزشکاران جهان/کریستیانو رونالدو در صدر این فهرست با درآمد تخمینی ۳۰۰ میلیون دلار
🔹
رونالدو تنها ورزشکاری بود که در یک فصل از ۲۰۰ میلیون دلار عبور کرد.
🔹
این مهاجم پرتغالی ۲۳۵ میلیون دلار از درآمد درون زمین را از قرارداد خود در لیگ حرفه‌ای عربستان به دست آورد و ۶۵ میلیون دلار نیز از فعالیت‌های بیرون زمین کسب کرد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/655406" target="_blank">📅 11:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655405">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IqNGkIqsCuMmZUd6w3FQA5VDBo3w_65uzVjcd_b184_AP5sGELp4ThwWs78Y1DVcXue9EA-avSVj_zCetg3eVVBHM8d1wegM1lbCc36wzgH4ulCXl0u5_SQoyS8Shcr8G6bovCZhcaJ2v9_x7BRdz7DWpIVd8CzFKvuDGuHEcTsjNkPppCDQ_sgq8bFfIdyl02bUAYPr-Vfy_EODNIcPvSG3ilzS9gqcAh8f3Cr_zhfi06bh7T1vClEW4FfyTRgqIEMhwCP8EHQbbFM-4kCwvfHU8JVGszVRBZ-zxJdwmkxKshF51S-4_B9Q2ZoeeGH6q9Wf09Lixht7ppgUDompRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سردار اسدی: هنوز برگ‌های برنده را رو نکرده‌ایم
معاون بازرسی قرارگاه مرکزی خاتم‌الانبیا:
🔹
بارها گفته‌ایم که هنوز همه برگ‌های برنده خود را رو نکرده‌ایم و برگ‌های زیادی وجود دارد که اگر لازم شود، از آن‌ها استفاده خواهیم کرد.
🔹
آمریکا فقط خواهان تسلیم کامل ما است و ملت ایران هم هرگز تسلیم نخواهد شد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/akhbarefori/655405" target="_blank">📅 11:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655404">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgtuZuWVCK4d1T243BLcI6XT-ik2jJJIDajJ7RfGp4XC8W3tKYdOvr1xQF8bbCD32ozruOyDZvuun2JqsvXeyy578lZ3bMpuQG6GsLOqka2wd-WN-cgDTGfm4ywPY_T_oMLQ7ADsxwWcWKeB0BC5J_Yh7vqDlby6VPq1YxEWW_i1T62214jkj9r-xYWYhwyE4UOlIDQPCYtg1UZltPx76RET2m_a3IUF6atYZz-0LwOpxrP8sFqMpVhYGQOInpB8Z0VA3UFR56v5DSb-EeFB4UVM56vN1msVimjpTg7Sl4rE6DqcttxPeZvVVbW1JPDvyEB-nWPGTwvwkESbOYQNFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الگوی مصرف دخانیات در ایران، چه می‌گوید؟
🔸
در این نظرسنجی بیش از ۴۹ هزار نفر شرکت کردند که سهم روبیکا حدود ۵۳٪، بله ۳۷٪ و تلگرام ۹٪ بوده است.
🔸
بیش از نیمی از شرکت‌کنندگان تا به حال هیچ‌گونه مصرف دخانیاتی نداشته‌اند و ۲۲٪ هم به طور مستمر و روزانه دخانیات مصرف می‌کنند.
🔸
با وجود فراگیر نبودن مصرف دخانیات، مصرف دخانیات همچنان در بخشی از جامعه رفتاری پایدار و ریشه‌دار است.
@amarfact</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/655404" target="_blank">📅 10:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655403">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
چه کسانی از ثبت ادعا در سامانه ساماندهی اسناد غیررسمی معاف هستند؟
سخنگوی سازمان ثبت اسناد:
🔹
افرادی که دارای سند مالکیت حدنگار یا تک‌برگ هستند، نیازی به ثبت ادعا در سامانه ندارند و مالکیت آنان پیش‌تر در دفتر الکترونیک املاک کشور تثبیت شده است.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/655403" target="_blank">📅 10:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655402">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwwYqQCZlvNA6iCuSOt_3hAj7zU_i0lwFmvfOHg9hE_ZHNAT8uuRwAohsm7IyjDu00ti5OHiThZbnVBN-iT1xLLMPy1d5z99AADiJ36AwBPhRBDUwzdlbWxaqAwT6jCQFGexCmlj4yxXzrGP73-1-1Qy4dJqUFgqsMSUe4vuFG50jnVCaEqCHxkX2p-OJzPKgAoq7HihjMz66JQXR0EcUnLrZxiY8vM9IwCRStOFBgO2xbpUau-wQhAwpLZn2b-c_LvBJpbQstakxcanR0DeoHTE_G5AckHdtVIY_q-ZK9WNap9XgfAJ1GVF1v4x2yGKmiENNYUJrXSdMvfc0TXUfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
چرا رقبایتان همیشه جلوترند؟
چون از قدرت خبرفوری استفاده می‌کنند.
✅
تبلیغات در پربازدیدترین کانال‌های خبری
✅
پوشش همزمان سراسر کشور و استان‌ها
جای شما خالی نباشد.
همین حالا پیام دهید
👇
👇
👇
@newsadmin</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/655402" target="_blank">📅 10:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655401">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
ایران در هر ۳ بازی جام جهانی سفید می‌پوشد
🔹
بر اساس برنامه اعلام شده از سوی فیفا درباره لباس تیم‌ها در جام جهانی، ایران در هر ۳ بازی خود در مرحله گروهی جام جهانی با پیراهن سفید به میدان می‌رود./ایسنا
#جام_جهانی_۲٠۲۶
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/akhbarefori/655401" target="_blank">📅 10:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655400">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
لینک یاب فایل های صوتی گنجینه معنوی کانال
:
🔹
زندگی پس از زندگی
فصل یک | فصل دو
| فصل سوم
| فصل ششم
🔹
چله علم و نور  "یک"
،
چله"دوم"
،
چله"سوم"
🔹
مستند شنود
🔹
آن ۳۱۳ نفر
🔹
تفسیر سوره‌های صف
|
مسد
🔹
سنت‌های الهی خداوند
🔹
شرح به وقت شام ۱
و
شرح به وقت ایران ۲
🔹
پادکست کسب‌وکار رادیو کار نکن
🔹
ادعیه روزهای هفته
🔹
برنامه کتاب‌باز
🔹
شرح و تفسیر کتب:
"سه دقیقه در قیامت"
،
"آن سوی مرگ"
🔹
چگونه با عبادت تفریح کنیم؟
🔹
حال خوش معنوی در زندگی
🔹
چله جوشن کبیر اول
و
چله دوم
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/655400" target="_blank">📅 10:23 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655399">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FhC1XnLExRt3si-OZ5beAR6B7Of1ZxLZvz1WW1OhFyeK0PyS0AQYEX_z05pnGamxoERHn6BVVCgHTLZyiBsQwnjUfPWhiqS6uixmtmcV3BhEOf435-iafIZJju8fCFPdF-kdH63ykprPml3sYje5Jpg6ImiDIuAzs3SbzkwZGWWhnl_JIyc9WbK5ZRVCPwqcEGcXw7SibTMaeKreuRmRZDtHmPy5ETUPBwJzk4mfIgLI3Axu5gc3B2Z7TYO0lmaF4i5zXcLQd0UBS2HIbXlT3h6VSlXTnEWEyluOm5zptO01HX48exkSrAC78fyXo06i_Ibc3qYvzJ8Xkv1Mud1ElA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکا در بیش از نیمی از کشورهای جهان سفیر ندارد
🔹
به گزارش NBC News، آمریکا در ۵۶٪ کشورهای جهان، سفیر ندارد.
🔹
همچنین حدود ۲هزار دیپلمات آمریکایی در یک سال گذشته از خدمت در وزارت خارجه کنار گذاشته شده‌اند؛ چه از طریق تعدیل نیرو و چه بازنشستگی اجباری.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/655399" target="_blank">📅 10:14 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655398">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
منبع آگاه: متن نهایی ایران همچنان در حال گفتگو در تهران است و هنوز پاسخی ارسال نشده است./ مهر
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/655398" target="_blank">📅 10:09 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655397">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a96d4703e7.mp4?token=UO87cwkrXKa_IXeJNXtAqL2apweh_NsUfczqjdDg0GtghiniR-eDND4Nj2ZRg2_NWUlvfH-9_imKbxRErx_A6zJMRceVCzhMne62mYr8-CGa2idQKS3lhhFjWPtPn44nlrm-Wx4CFldkOHkG0DHEPhnIMhj-djXgUqhGeHEqil7efTd0YTioU4Wlb1L5fP-uEFA4FptRtTMv_aYYnLriuptNbJSt_JxLBivrR2dKv8L8jy1NoJ_CLNjeI1IV1dF3lDZxdQigTH06DKXy0cdOV5SLDdijztaiY-PipXlCujkiCjMHVCL3ntsl4-fz3vLGETfdQNf9Cma9_bPKx-ebKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a96d4703e7.mp4?token=UO87cwkrXKa_IXeJNXtAqL2apweh_NsUfczqjdDg0GtghiniR-eDND4Nj2ZRg2_NWUlvfH-9_imKbxRErx_A6zJMRceVCzhMne62mYr8-CGa2idQKS3lhhFjWPtPn44nlrm-Wx4CFldkOHkG0DHEPhnIMhj-djXgUqhGeHEqil7efTd0YTioU4Wlb1L5fP-uEFA4FptRtTMv_aYYnLriuptNbJSt_JxLBivrR2dKv8L8jy1NoJ_CLNjeI1IV1dF3lDZxdQigTH06DKXy0cdOV5SLDdijztaiY-PipXlCujkiCjMHVCL3ntsl4-fz3vLGETfdQNf9Cma9_bPKx-ebKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
التماس علی‌نژاد برای حمله به ایران
🔹
شما یهودیان صهیونیست هستید که می‌توانید هم دموکرات و هم جمهوری‌خواه را در آمریکا متحد کنید پس چرا در مورد ایران مردد هستید و حمله نمی‌کنید؟!
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/655397" target="_blank">📅 10:07 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655396">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">✅
مجتمع فنی تهران - نمايندگی استان البرز (کرج و فردیس) در حوزه های زیر دوره های آموزشی و تخصصی برگزار می نماید و می توانید ثبت نام کنید:
@mftalborz
🔸
شبکه،برنامه نویسی و هوش مصنوعی ، طراحی سایت ، اسمبل و راه اندازی کامپیوتر ، ICDL
🔹
معماری،طراحی لباس و خیاطی وگرافیگ
🔸
حسابداری،مالیاتی،معامله گری ارز دیجیتال و طلا و نقره و مس، فارکس
🔹
زبان های خارجی و IELTS
🔸
عکاسی، تدوین فیلم، ادمین اینستاگرام، تولید محتوا
🔹
نرم افزارهای فنی و مهندسی, تراشکاری، فرز، جوشکاری، تعمیر پکیج و کولرگازی،برق صنعتی
🔸
برق و الکترونیک، برق خودرو،تعمیرات موبایل و برد، PLC
🔹
تربیت کارشناس منابع انسانی، فروش، مدیریت عالی کسب و کار(MBA)،فن بیان
🔸
مراقبت از پوست(فیشال)،گریم، آرایش و پیرایش،دوره های زیبایی(ساختمان مجزا)،تکنسین داروخانه
🔹
دوره های تشریفات و آشپزی(پخت نان، شکلات دست ساز، کافی شاپ و باریستا، آشپزی ملل و سنتی )
🔸
مهارتهای دانش آموزی(۷ تا ۱۷ سال)
🔹
عمومی و خصوصی، حضوری و  آنلاین در رده های سنی مجزا و مختلف
مرکز مشاوره و ثبت نام:
☎️
026-34127
@mftalborz
✔
كرج پل آزادگان ، فرديس فلكه سوم
🎯
آماده عقد قرارداد با سازمانها، نهادها، شرکتها و مدارس
📱
صفحه اینستاگرام:
https://www.instagram.com/mftalborz/
🎒
ثبت نام اينترنتي و اطلاعات دوره ها
🌐
www.mftalborz.ir
مشاوره تلگرامی و پاسخگویی به سوالات:
@alborzmft</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/655396" target="_blank">📅 10:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655395">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
وال‌استریت‌ژورنال: آمریکا عمان را برای قطع روابط با ایران تحت فشار گذاشت
روزنامه وال‌استریت ژورنال:
🔹
اگرچه عمان در مذاکرات ایران و آمریکا نقش میانجی را ایفا کرد و در اوایل جنگ اخیر برای حفظ کانال ارتباطی کوشید، اما دولت ترامپ اخیرا رویکرد عمان در قبال ایران را به عنوان رویکردی خصمانه در قبال آمریکا دانسته و مسقط را برای انتخاب میان تهران و واشنگتن تحت فشار گذاشته است.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/655395" target="_blank">📅 09:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655394">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
رئیس پارلمان لبنان: هیچکس جز دونالد ترامپ نمی‌تواند آتش‌بس واقعی امضا کند و او تنها راه برای این کار است/ حزب‌الله آماده آتش‌بس واقعی است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/655394" target="_blank">📅 09:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655393">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OMbfH0OiJ6qb0HGTKfdHJrkiBnmGJ_6NTwhYPmcBx2yIdlQSnaNeafLenOkX5JrBMo1KGoOrWy4D4lxY0UE9XWRKBPOo53lg8tBB3wo5X3jNrj4XaZGcx75J7P1PiheIcbSXih36wL9-YM2EHF_l-4cuOo3cBhWm5nObKzlOj3YKUEgBtkGBN2LrnpZDxsKR5epqZ3WBQv1tR7R21XCt82ko7ZKo-eUe-hLcMoeBUudnhBoMFXg7m-cmvOkvxdlDZP1ClMiZEH7GlEv5FKNJAr3mTxaifDy1EyoHMJ1w7ax2rxg-0MOEHcpYIrMJI-XWd9bhmFYmQn10X0Hu_md4Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پست جدید اکانت ایکس سفارت ایران در ارمنستان: طولانی‌ترین دوره ریاست جمهوری ایالات متحده
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/655393" target="_blank">📅 09:30 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655392">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c3e885240.mp4?token=C_i-4tfFNZmC_4Sa1z1OgIhuH5uYIWUOsA4XuAoWNhhFSeHdu-USLSabyJW-YCSG2YuX1jPWG4NN8WQzp7D2Qm-vqPG2_P70TjHGwiP4ru3Aqtr8lI0rlkUbc2fIz8ItuBDbkSjXhZe3x9tSlxQjQWijbk3fABP6kKkj5nFL8jBAnv5Mqu_C-ujgFxoKO_qfLYFyMoBqywWIYOqXLTxLFlRiFnG0DK_UXEHoIWFc3i6u2rgBqwZ4Z52Ia44_z4OpfH1DopFAKdI88mbm2XEuF1vCD4uk8ATNZhljYiDX6NIpwkAq-gH6TVmkY8O3CvrU2U440z6PJjM8Jck2H5skEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c3e885240.mp4?token=C_i-4tfFNZmC_4Sa1z1OgIhuH5uYIWUOsA4XuAoWNhhFSeHdu-USLSabyJW-YCSG2YuX1jPWG4NN8WQzp7D2Qm-vqPG2_P70TjHGwiP4ru3Aqtr8lI0rlkUbc2fIz8ItuBDbkSjXhZe3x9tSlxQjQWijbk3fABP6kKkj5nFL8jBAnv5Mqu_C-ujgFxoKO_qfLYFyMoBqywWIYOqXLTxLFlRiFnG0DK_UXEHoIWFc3i6u2rgBqwZ4Z52Ia44_z4OpfH1DopFAKdI88mbm2XEuF1vCD4uk8ATNZhljYiDX6NIpwkAq-gH6TVmkY8O3CvrU2U440z6PJjM8Jck2H5skEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
املت سوسیس و قارچ
یک صبحانه یا شام خوشمزه و مقوی که در کمترین زمان آماده میشه!
😋
‌
🔹
اول پیاز را خورد می‌کنیم با کره تفت میدیم بعد فلفل دلمه و سیر با پیاز داغ تفت میدیم بعد زردچوبه میریزیم و قارچ‌های اسلایس شده را به مواد اضافه میکنیم تا پخته بشه و در آخر سوسیس و تخم‌‌مرغ را اضافه میکنیم
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/655392" target="_blank">📅 09:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655391">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-lgwAJZ7qB3_8aIJLtxrGNcUY2wgpw-eI15XP7-nkJ7OwiVSvnPF6knktgG2mbxMoeXRdfC2w0UFzFoglCXxkoMtNXq5w_jQqbC89lkOFYrQZ0mH6wYEBRbApQPUjA3lS4Xhi-N3Rr1SfoH25AeCKbApJX4vllII77ua0lSdr8mppAPFV5BVsbx-T-FAhkFWI2KEDRFSYV72TguYmzVo0Y8JZNf3Sfzf0gcmeyjYaXiPobzWt99tRf8lFsV_lqL9OkOXnD5FeXpYiHN5z28TFqRuBuOkpxEltVudQcTXlolfsjTGSQpE3plvwgVQj-f4lxUm7A1pxVUNd05qkqKwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدترین لحظه در سرمایه‌گذاری طلا: فروش به خاطر نیاز به پول نقد!
🔹
بدترین لحظه برای فروختن طلا، همان لحظه‌ای است که به آن نیاز داری. چون مجبوری، عجله داری و فرصت چونه زدن نیست.
🔹
خیلی‌ها توی این یک سال، فقط برای پوشش یک هزینهٔ کوتاه‌مدت، طلاشون رو فروختن. الان که قیمتش سه برابر شده، تازه می‌فهمن چقدر ضرر کردن.
🔹
حالا فکر کن می‌شد طلات رو نگه داری و در همون لحظه، پول لازمت هم به دستت برسه. این همون کاریه که
وال‌گلد
می‌کنه.
۳ مدل اعتبار با وثیقهٔ طلای خودت داری:
اعتبار فوری تا ۱۵۰ میلیون تومن برای ۳۰ روز/ وام بانکی ۱۲ ماهه از طریق های‌بانک/ اعتبار خرید کالای تارا برای ۱۱ هزار فروشگاه.
هیچ‌کدام نیازی به چک و ضامن ندارن و طلا همون‌جا می‌مونه و همون‌طور که داره ارزشش حفظ می‌شه، سودش برای خودته و فقط مبلغی که وام گرفتی رو پس می‌دی
جزئیات و شروع
👇
-استفاده از اعتبار فوری  -
وال‌گلد به کارت میاد٬ تا بدون ضامن وام بگیری</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/655391" target="_blank">📅 09:21 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655387">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pKyJ3mfNSZIBgc83UxrK4_eORSLd2YE6C7LBkF_b5rjOWSxdyiMeVSJj2qin-dacXXbHP8SndXzEbxO7dAygrsHXCN7N-XymcqT68puFiuyrIdjPeAo7M5y9S6imUwxRrTYGHPp-QSfZR_O4axHeX-Eyn8Zrn2Cbgpx8OVyYMOjGWn091ShElhHvBV71NcTxxgrXvHeTTl8J7TDaBpg2Kk5K1Pt50cBoN57xo3pIiKGYaaVPkcfnpXpx10cWfC5EoziYw1F1nHiN9QxBtkY5nLMopHeCX6NuVRqoZ9iIpfSB-BUnzI-D6-hAbWogqMOezhk3DlMRNR0yHFZ-3t79_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YF8G-howhDQJy3NJ8foGXd62xak9kHz7aO9E_2pzlo-gL66dtTTL-oA-5HAJnAHMHUK2A1HDlLqRMwkx4vc_mp5iJEL45rk-_sHJc7pUZWBRZoIHDaPPqm-QgmgiepEobu5Wg-hbtZFUiwGixTLMtpBr61mvQ4pfk4YPbG9mhRxPqfmnRmCWCz_M2ekJck-e6ZJskhg_oZWXF3aSshQZeeS0Sh2WYXUthKxkQfw9tlL2SR-8SmBpz0PoRVnRoEKJ5kP66rfm50ubc4RviLSQyUHVUuOKKFDjerg8SRHddtbDmgJf6H11u9vvjOdMPiIyEEcvnboNoJ5qYqTS4-9e5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dh_e5_R57IYLDvJlKXAf4PMa_mu5tZZbi_aye4rIlqS5wP2NIrk2WyA47Al9aoBRwUMXo7La3OOSW67XJprrIo3fsA1DH05WMBMzV7coU0QUhd-_NeQtLcSI7mB2wH9P8_ZbJPZbioLmt5Y_jEUsqr-ndKg1FViCS5dVRq5LxKXXA9JKQiEAO1m_8BgfLIaRusVFrt8gRNk9ybMcN-yV4qt7pBgfEIAzdO8cHB0nNMWCsHu5mSGzP98quuOLmGq4OLrlu1YLWii1lpNNuVHCXj_J7ZIu4BaSjn-gA4JG5LDWogVH0_iPwH3NGzyAtO076yy5HUng2COhhUi2hum44w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uL7d3HvgDKZuWYxz0PO8Yt_1_T29g-I-5WtGcTf_HXKfvsJBQVHjAZpRAzXXDogvlbLMwqB479BmZTIJZj4Ux7XNhGuBB2zK_fBmOyngv_FFY5KqEkr4CXdq5IDWmRSIwMO4eUSD-DSbf70M713jpkloJCr0j8FBuoYRsIh7tOmMV60DgnJ8qFkxxUqqQeqgBkzah4mnhrSkUkjtXFB7Vvv4GCF14s4hnsdkUxU4kTml5vl7UF6hEDIdV-OBPd2mLvCuCEvAByviEelhpb8EnJRL9WANCLDYeYFK1we9tPcTa6yAC6rjX1JdSAiwN9iWsa9vXsx7_boX3WfernMACg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
رنگِ "آبی درخشان" یا "Luminous Blue" با کد «۳۸-۲۸-۱۲۵» به عنوان رنگ سال ۲۰۲۷ انتخاب شد
‌
🔹
این رنگ به عنوان ترکیبی از "تکنولوژی، طبیعت، انرژی و آرامش" توصیف شده که گذشته، حال و آینده را به هم پیوند می‌زند و یادآور رنگ‌های سُنتی‌ای هستند که از گذشته تا الان همراهمان بوده است.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/655387" target="_blank">📅 09:16 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655386">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DikUaQOgSUTS8a11v3-QbDnjqW7_qnGrJe83buw9ufcVmXhJd3lhKTAfxXABWxtU7b6nvNSgYd9Cs8yYttREpEplfZAKv-dwMkFiwWACzhG8Cff157Piv6cgUQLZYlek9IjVlSe3o1ZG3gwtmMY0tkG-FLka6hiNbdkiAaGnmOtDYPHswtSm50TvVKRQR6G-8MLsLlqBa980LCehsigca3hkQi-gB4WqFDL6LnRdwYpxIXphSq5Hc1RbsJni1S-U6io28QnxyfcT-Q7lzIDAQKLwsj9Gz3mEXMJo4IiLKLyvCHd8dQBmzfrNEa6RibihMJ2MalJfb7K1jjCp_b9HnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آیا پدافند جدید ایران قواعد نبرد هوایی را تغییر می‌دهد؟ | شکارچی خاموش؛ پایان عصر پروازهای بدون دردسر
🔹
برای دهه‌ها، برتری مطلق هوایی یکی از پایه‌های اصلی راهبرد نظامی غرب و به‌ویژه آمریکا به شمار می‌رفت.
ترجمه گزارش میدل ایست مانیتور را در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3219663</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/655386" target="_blank">📅 09:14 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655385">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RizwCarb8eA2DJ-LbQFfmZrzlXXER9dp4a9eIilMZnpX6WZnyWlUHSJ8BfxATIh9gES3v-LeLvM3eiiQ-9j2gZy68oR9IoOZdEQXLxwjJqL8P13KuqdI8GHU4A0p_k5DpFPzsz0YwBxx0RRf9Mv10z4l0bvXoBgGJ8nQ3Sbyx8E37HWOUpDUTMCvOCq7um9pR4B1WG53djLmVG9qeEOovxmmmSAT3Wy6XFRYkmSnZnS9gDOEOxNR7cQh_M9WbODCV755pSt0iwvBVJRrHxL2s5q6EQRTkCRNSLmjgRfzhGsnoBr2HB47qwBClFc-rLfS7NXQXg2KTvrcVByEtF-rPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آخرین قیمت نفت: ۹۴ دلار
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/655385" target="_blank">📅 09:13 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655384">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
یمن: اجازه نمی‌دهیم حزب‌الله به‌تنهایی بجنگد
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/655384" target="_blank">📅 09:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655383">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzQLaOdiO-MVCpul6jXmm2Tru7-veQeDgiDkz1WBnMBM2mUMkYQSxdjz9H2gmOxY1s39JHDxOY7WP4T6Ore0pcrWKmkn2R4iJilk0yBCpOYFWBx2J4OVnxfA5TrSE_0qIWZz3twz2CPqy4XyHDicwBIZiKa43CUJmTGtWxPNoEXKN_5E3Uelp3_xn__ePWJ5RxjFrFKroQPdD1WmL2oM8WCqvG5utQ9GU4pDOGpsIrhzqEhbTFRHH-BRqOI_8me6jPADwiQWoewzKikivU9W1mcVGM9dwCEsliQoAKAVim4yJVe6asiRrRXlybH0fbBN-pk-L6zOWNM52Pb8-Fsxjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا سرطان در میانسالی خطرناک تر از پیری است؟
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/655383" target="_blank">📅 08:55 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655382">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
وزیر آموزش‌وپرورش: ‌امتحانات نهایی پس از تأیید مراجع ذی‌صلاح برای فراهم بودن شرایط حضور دانش‌آموزان در حوزه‌های آزمون، برگزار می‌شود
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/655382" target="_blank">📅 08:54 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655381">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b3f80a299.mp4?token=CLlC4NWqVPAYd2BK3szjAnf1YwZHqqROsKzeDGbkZ4EHyGy1vKcWYyBfOpXYb7Vci-_eE6HhpjFO0v5HBSqcHDoLdIgxa61OSVQEZmB5uZk4BoaXZGIY56eQ0nm4QOq-euvlxtRY8LTf5pLgOvsDwwNDu_zR4cx3xzhuNgnyGyGwqQFLlV7skIbkAciTKqidDYCz4v3bCHBdx0VVsir0U_snhPxyUPUkXDMGGjtJ745GCdNmq8rlBH_CcuKVQzssoDMTIr2B2Qzm84SjeIHBWLc37HNmuZHrobjO8-lv6h_Pkelogjg9ER3RM7eSH4dhc7vTNIitIGbt6dVb4DsyTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b3f80a299.mp4?token=CLlC4NWqVPAYd2BK3szjAnf1YwZHqqROsKzeDGbkZ4EHyGy1vKcWYyBfOpXYb7Vci-_eE6HhpjFO0v5HBSqcHDoLdIgxa61OSVQEZmB5uZk4BoaXZGIY56eQ0nm4QOq-euvlxtRY8LTf5pLgOvsDwwNDu_zR4cx3xzhuNgnyGyGwqQFLlV7skIbkAciTKqidDYCz4v3bCHBdx0VVsir0U_snhPxyUPUkXDMGGjtJ745GCdNmq8rlBH_CcuKVQzssoDMTIr2B2Qzm84SjeIHBWLc37HNmuZHrobjO8-lv6h_Pkelogjg9ER3RM7eSH4dhc7vTNIitIGbt6dVb4DsyTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراف مقام سابق پنتاگون به قدرت نظامی ایران: بمباران‌ها بی‌فایده بود، ایران از حملات جان سالم به در برده و در حال بازسازی لانچرهای موشکی برای دور بعدی جنگ است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/655381" target="_blank">📅 08:53 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655380">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">قسمت بیست‌و‌هفتم - پادکست کافئین</div>
  <div class="tg-doc-extra">خواجه نظام الملک طوسی</div>
</div>
<a href="https://t.me/akhbarefori/655380" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
پادکست
#کافئین
🎧
▶️
خواجه نظام‌الملک طوسی
🔹
چرا در مسیر توسعه فردی و کسب‌وکار، تکیه بر «انگیزه» و «اراده‌ی فردی» دیر یا زود به شکست ختم می‌شود؟ وقت آن رسیده که توهمِ منتظر ماندن برای یک ناجی را کنار بگذاریم و یاد بگیریم برنده‌ها چگونه در سکوت، «سیستم» می‌سازند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/655380" target="_blank">📅 08:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655379">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62860bc349.mp4?token=JQEJUjCEqgJ5E4Bn4J5JB9NyU1h-x1r07lvuZZM_g5F88Vy4H_o0Sz5dcCFfp0snT4eZu1dsQTVwFeadltdqOR4C8O0aO_hry-p4mFjxqYyGGFpjieuKHiZb-sN16Vz2BmQHYPvQiEBzKIPyLMu0y4F_IQYP8pTZ5toa0Lpf8NFz744f7D9F5Htj_CKOS1esn5FmfI9AYM3uAgAG32I6s86l5dpsuZP4yuH62qY9d-S-taI8oUbgr0Xybg9NthbXgMmnOP7qCAbrO0fHYFsTRWHqUlslXHAw5T3EJO0U5NhS3BIgUuzhuJJK2IALQ7zZg0bf_sruyO8zQGYdPEPIRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62860bc349.mp4?token=JQEJUjCEqgJ5E4Bn4J5JB9NyU1h-x1r07lvuZZM_g5F88Vy4H_o0Sz5dcCFfp0snT4eZu1dsQTVwFeadltdqOR4C8O0aO_hry-p4mFjxqYyGGFpjieuKHiZb-sN16Vz2BmQHYPvQiEBzKIPyLMu0y4F_IQYP8pTZ5toa0Lpf8NFz744f7D9F5Htj_CKOS1esn5FmfI9AYM3uAgAG32I6s86l5dpsuZP4yuH62qY9d-S-taI8oUbgr0Xybg9NthbXgMmnOP7qCAbrO0fHYFsTRWHqUlslXHAw5T3EJO0U5NhS3BIgUuzhuJJK2IALQ7zZg0bf_sruyO8zQGYdPEPIRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رویاروییِ خونینِ خواجه نظام‌الملک طوسی و حشاشین
#پادکست_کافئین
| قسمت بیست‌و‌هفتم
☕️
🔹
در این اپیزود به سراغ مردی رفتیم که امپراتوری خشن و پهناور سلجوقی را نه با شمشیر، بلکه با قلم و دیوان‌سالاری اداره کرد. او به تاریخ ثابت کرد که انگیزه‌ها فروکش می‌کنند و قهرمان‌ها می‌میرند؛ تنها چیزی که در طوفانِ بحران‌ها شما را از فروپاشی نجات می‌دهد، «سیستم» است.
هر روز صبح با یک شات غلیظ از تاریخ، آمادهٔ شروع روزتان باشید!
از اینجا ببینید و بشنوید
👇
https://www.aparat.com/v/lah9ra3
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/655379" target="_blank">📅 08:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655378">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
الجزیره: آتش‌بس لبنان مدیون تلاش ایران، قطر و نبیه بری است
🔹
بر اساس ماده ۱۳۳ آئین نامه اجرایی مدارس ثبت نام در مدارس دولتی هزینه ندارد
🔹
اداره هواشناسی مازندران: دریای مازندران تا پنجشنبه مواج و تعطیل است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/655378" target="_blank">📅 08:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655377">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
انگلیس موشک ذخیره می‌کند
نشریه تایمز:
🔹
انگلیس در بحبوحه خطر فزاینده حمله ایران یا نیروهای نیابتی‌اش به پایگاه‌های متحدانش در خاورمیانه، در حال ذخیره‌سازی موشک‌های چندمنظوره برای مقابله احتمالی با پهپادهای ایرانی است.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/655377" target="_blank">📅 08:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655376">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25cca25161.mp4?token=i1QKCdic410cWjSWBQht352LWXpCBUUzMHGdL4ttwKBcUo1RAFh3vYCyX-t9UlXxrsQhw6-O5QuYHFu-7ZXAzZlVxlrhn20MW_jRIHuXruU56x81l0YkemVOvqhvOtwHfdo1nHm2xZO5_yqdfGOHKazXEQm4qeWj_FklyWRgVd2g8vAydOgKfj68vX6c7MciKDO-8bAagclrJaPBB1s72DR63d4J4tLbrlECUEh4Dh_PlZtVrFrD3Z2Ag1zQePU7vvCANEDOvImNMEwYHNMun1jP-kZzX-jtKQClnlzWi9q69dp6VFghf7QsIoMnEXnMGG6G_auR2yTZ_WDBSVoehA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25cca25161.mp4?token=i1QKCdic410cWjSWBQht352LWXpCBUUzMHGdL4ttwKBcUo1RAFh3vYCyX-t9UlXxrsQhw6-O5QuYHFu-7ZXAzZlVxlrhn20MW_jRIHuXruU56x81l0YkemVOvqhvOtwHfdo1nHm2xZO5_yqdfGOHKazXEQm4qeWj_FklyWRgVd2g8vAydOgKfj68vX6c7MciKDO-8bAagclrJaPBB1s72DR63d4J4tLbrlECUEh4Dh_PlZtVrFrD3Z2Ag1zQePU7vvCANEDOvImNMEwYHNMun1jP-kZzX-jtKQClnlzWi9q69dp6VFghf7QsIoMnEXnMGG6G_auR2yTZ_WDBSVoehA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی گسترده در پایتخت اندونزی | بیش از ۲۰۰ خانه طعمه حریق شد
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/655376" target="_blank">📅 08:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655375">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I41_w7SIMbU0LLwZyX8bZIk6pOgCXJqkE_DASyweFwBayaYNmjyWO5_t8IWBV7bbyyHGQPaaCg4SRvnmnob8KESLpBWsTt00wJd_5aUXZzG179TEWgGCZVf0AlN3PbjDEtuaUjVhkeDSs4Icy0buQg8mKTVgW_wq7dRz6mJZMlC1yS6LZBM-fkfHFKWJ-CbipAULSUpX6o_YuBXR3s6EahwLXN_L2p02iJi5yceUdUkskMJD5Fo1laojO367NXy8G7eQoMa5W4xAObWQYuJLRZ7XsQ0BIJ3RnvmaA4dK_kELiHMaILpnX17TFAYBcZsKw_v91mZI_lAV47RZX1wicg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی: روزهای تاریکی در انتظار آمریکا و اسرائیل است
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/655375" target="_blank">📅 08:07 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655374">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/784e30ec43.mp4?token=TtSXpqYRCUMkrZXPbaEWSnNVqP7yyGIHpsAnQ_DUqLZJnndVFqPcCk0BdqxBcYeJnWlKEp4YKZGFXPDJdGf5aVRfX3bwZs777I2FlRjExmWDKCEtaQvuLQUmxiRkzoxFD-ZUyw6CijS4E1iQ4n-6osHyEODcgoae9ANnG3YHzvTC-p6u2UEMRJTZFmJNxS66hYyPb5yh20w-9q3IqgF-STCXPn69dRSHCmuGLxHnbEYNwbhpmLKL4Fz-Z_DETh0apTxaPxrTMUJoSPN-TY18ajqDVENlkM6P27nJuLlpItbQN3qQtk4FMN6F4tdfFlSclRrjeQ7rXz1HZJs7lFaYDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/784e30ec43.mp4?token=TtSXpqYRCUMkrZXPbaEWSnNVqP7yyGIHpsAnQ_DUqLZJnndVFqPcCk0BdqxBcYeJnWlKEp4YKZGFXPDJdGf5aVRfX3bwZs777I2FlRjExmWDKCEtaQvuLQUmxiRkzoxFD-ZUyw6CijS4E1iQ4n-6osHyEODcgoae9ANnG3YHzvTC-p6u2UEMRJTZFmJNxS66hYyPb5yh20w-9q3IqgF-STCXPn69dRSHCmuGLxHnbEYNwbhpmLKL4Fz-Z_DETh0apTxaPxrTMUJoSPN-TY18ajqDVENlkM6P27nJuLlpItbQN3qQtk4FMN6F4tdfFlSclRrjeQ7rXz1HZJs7lFaYDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تقویت عضلات شکم و و میان تنه با این حرکات #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/655374" target="_blank">📅 08:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655373">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
گروسی: خروج اورانیوم غنی شده ایران غیرممکن نیست!
گروسی:
🔹
خروج اورانیوم غنی‌شده ایران غیرممکن نیست، اما آسان نیست چون به شکل گاز و بسیار آلاینده است. گزینه‌های جایگزین شامل رقیق‌سازی است.
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/655373" target="_blank">📅 08:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655372">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2ac1f166.mp4?token=iW2umE5uVG_b-eyTmT2kTKLGjgE6gc7kOQLqWp0Egu_mOljW3IBVYMudB6DUDxzx4xEHVEztX8RmoKLy85DU0NcPm9rlwqL-Gun0ipBwe2sAMZrEE6v7CuQuQHw3flV5QwD52R6B-xTWKyThBhaaHsuPNrBnIk9MekjbZHwr4o4WRKmbpebmvaQNiEMmD5Ds6LCWRJ_nPcL9DCfLZ2gzx9bMYR9by1k0a7NTNCs0DsW4jEaddrEXzeTehLfi5EueFflbLaGs6khR2FoUh7vqbnuq2e_1I-_lXXQIjJMq0EBAmP4GQ9LMAXwIsn0wLmOtNrecE9lh8wIZwEgvBcclzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2ac1f166.mp4?token=iW2umE5uVG_b-eyTmT2kTKLGjgE6gc7kOQLqWp0Egu_mOljW3IBVYMudB6DUDxzx4xEHVEztX8RmoKLy85DU0NcPm9rlwqL-Gun0ipBwe2sAMZrEE6v7CuQuQHw3flV5QwD52R6B-xTWKyThBhaaHsuPNrBnIk9MekjbZHwr4o4WRKmbpebmvaQNiEMmD5Ds6LCWRJ_nPcL9DCfLZ2gzx9bMYR9by1k0a7NTNCs0DsW4jEaddrEXzeTehLfi5EueFflbLaGs6khR2FoUh7vqbnuq2e_1I-_lXXQIjJMq0EBAmP4GQ9LMAXwIsn0wLmOtNrecE9lh8wIZwEgvBcclzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تیخوانا امنیت دارد یا تیم ملی با کارتل‌های مواد مخدر در مکزیک روبه‌رو می‌شود؟ پاسخ‌های جالب مهدی تاج را درباره کمپ تیم ملی ببینید
😁
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/655372" target="_blank">📅 07:49 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655371">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32d79d9343.mp4?token=UC6xTLeVoq4Kf_YbN2CF6PxRIHRoC0G_v25amV7Wb11wdFY3LelaiKL9Q3q-dypvkv3BDErxiIBU1MiNJjij98fNVNgwVRmmsIwkMow2HEH3hYF5RzoIq70tlv8UJAFeJUZJVNWvtekHDX9mcWYy81M9aU0yvwIsQD59vVFFDzRfkk6AgD54y888F2wO0lZyLpPr0DIOqGf7Yg4indR6ilX04L3TeS9IdIj9UOQtQpYWaYmGOkfnfiNxzpfaWkbNDy0VE95lkdr56AJ-flGDDHKGwMv7aseraYFk5YSY_ETR3EK9g86vtWC4ijdcwPNVYuzCfYQtBZcpRfnt2unEwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32d79d9343.mp4?token=UC6xTLeVoq4Kf_YbN2CF6PxRIHRoC0G_v25amV7Wb11wdFY3LelaiKL9Q3q-dypvkv3BDErxiIBU1MiNJjij98fNVNgwVRmmsIwkMow2HEH3hYF5RzoIq70tlv8UJAFeJUZJVNWvtekHDX9mcWYy81M9aU0yvwIsQD59vVFFDzRfkk6AgD54y888F2wO0lZyLpPr0DIOqGf7Yg4indR6ilX04L3TeS9IdIj9UOQtQpYWaYmGOkfnfiNxzpfaWkbNDy0VE95lkdr56AJ-flGDDHKGwMv7aseraYFk5YSY_ETR3EK9g86vtWC4ijdcwPNVYuzCfYQtBZcpRfnt2unEwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویری از کشتی اسرائیلی که هدف موشک‌های ایران قرار گرفت
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/655371" target="_blank">📅 07:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655370">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
آکسیوس: تماس ترامپ و نتانیاهو سرشار از الفاظ رکیک بود/ ترامپ به نتانیاهو: واقعا دیوانه‌ای، اگر من نبودم الان در زندان بودی  پایگاه خبری آکسیوس به نقل از یک مقام آگاه:
🔹
تماس تلفنی روز دوشنبه دونالد ترامپ، رئیس جمهوری آمریکا و بنیامین نتانیاهو، نخست وزیر…</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/655370" target="_blank">📅 07:45 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655369">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
قالیباف: اگر جنایت رژیم صهیونی در لبنان ادامه یابد در مقابل رژیم خواهیم ایستاد
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/655369" target="_blank">📅 07:42 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655368">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
ادعای ترامپ متوهم به ای‌بی‌سی: فکر می‌کنم طی یکی دو هفته آینده با ایران به توافق برسیم، آتش‌بس را تمدید کنیم و تنگه هرمز هم دوباره باز شود  ‌
🔹
من هنوز با این توافق موافقت نکرده‌ام و هنوز باید چند امتیاز دیگر بگیرم. #Devil
📲
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/655368" target="_blank">📅 07:42 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655367">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
ادعای ترامپ متوهم به ای‌بی‌سی: فکر می‌کنم طی یکی دو هفته آینده با ایران به توافق برسیم، آتش‌بس را تمدید کنیم و تنگه هرمز هم دوباره باز شود
‌
🔹
من هنوز با این توافق موافقت نکرده‌ام و هنوز باید چند امتیاز دیگر بگیرم.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/655367" target="_blank">📅 07:42 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655366">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LoiwkAuLa_9KK0TTb4bBVfSpJahrlK_WiAVma7vCeJSeqwSfrA4-o5hwx8aCiCwfPElZTRYBI_yvt8Lg6Apvo6Cr0LSJgRoipP4TlcCLsly7hw_PavczCwo7mjfNlTb4cgQqeXy8FWKsNxFl4_z7prCcNq-nH9ouvW_KQ2xQ1-VJo2aeOXuAmwEBTQiSO82HA8VU5Gjj-6eUlhCxo9UlZxYf8Sfu-PoBDVgh1rC-rG-ioGqgZFCUrsbo0G6NaqEyWydnxb05GT_608wjTD-4c5RlVsF0Bhad9IAgWn1rATNJWjnKZDekTdlYtYon1EGAO01wKmiFebjUxp4SaS2_og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: اگر جنایت رژیم صهیونی در لبنان ادامه یابد در مقابل رژیم خواهیم ایستاد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/655366" target="_blank">📅 07:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655365">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
ترامپ متوهم مدعی شد: من تماس بسیار سازنده‌ای با نخست‌وزیر اسرائیل داشتم و هیچ نیرویی به بیروت فرستاده نخواهد شد، و هر نیرویی که در راه باشد، قبلاً بازگردانده شده است
🔹
همچنین، از طریق نمایندگان بسیار عالی‌رتبه، تماس بسیار خوبی با حزب‌الله داشتم و آنها موافقت…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/655365" target="_blank">📅 07:33 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655364">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UwdHkE0nE9z6yNyn78VVs_hGgE4jMojzeCv5k-_FjqMTbB55n5XOF2LxBVGz1kEz6eRZd3oHo5CChoPFpnM4d3WZ4yNvObu0Vr9VRa7Abpxa93ANz6RFQuyd3sMlMKqHIUWLh-CI1Ln9kT-_n3Gqr-pj6BT0tcwpH22cxaU3d_AVV9JpnEta6UFqHZKy9X3n2pj9DN-aJd_xhc7Amf0vlLRZ4BT9AR3bld6zRhQtJgZLhjXXgrCjGhnRkYtIdWuZwLfM8DqPSjzt7hsHcPLtPpjny0MsRJB6_waIOsvUinZFe1uR1PgmdYUbu6XtSMJwwnMP6MkeprUlGJaxNfMjgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز سه‌شنبه
۱۲ خرداد ماه
۱۶ ذی‌الحجه ‌۱۴۴۷
۲ ژوئن ۲۰۲۶
سه‌شنبه‌ها
#دعای_توسل
بخوانیم
⬅️
متن و صوت دعای توسل
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/655364" target="_blank">📅 07:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655363">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQR5onQ1wNHOXcc9m8af_7rEixxvN3iDnvNwV_gXS1cNNt_YbnuwKDs90U5RUgnQP3jPQOlXR3fyeKTeKN1j-NxgdxlAYRFKnJc3UhcZxUm5-SNFROFkBfHdd-UUx_GTWPPh98uLKYIllrI0ndZh1ddV4E2CCHZafY3EemdcthEZGhP-L7_wsj61NzyMc7FnwzrXbGD_JV0SrmXYROU9aZHnrWniaBm1FRTKDm-JVutXaT2yqYcE8sEtuXlTTNxES1fv-PSwae7blvvLeeVvDObmN9xG7rMbsO9Bsta93Q72zWJYtOqHEEdE1HNecxYgWVX7mT55xfSVGNACnql_iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
دریافت ویزای کاری و اقامت دائم استرالیا و اروپا برای انواع مشاغل و حرفه
✅
مشاوره کاملا رایگان و بدون هزینه
✅
تضمین دریافت ارزیابی شغلی از استرالیا
✅
دریافت کارت اقامت اروپا در کمتر از 6 ماه
✅
پرداخت چند مرحله‌ای (اقساط)
با 19 سال سابقه موفق در امور اخذ ویزا و اقامت دائم استرالیا و اروپا.
✨
برای دریافت مشاوره رایگان لینک زیر را باز کنید:
https://persianmigrant.com/فرم-مشاوره
☎️
02196862626
🌐
persianmigrant.com
-
www.bmcvisa.com
@PersianMigrant</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/655363" target="_blank">📅 00:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655362">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sdRM8JtxVHziTs2dd-VAYWJ1gw_u63fYAOsQO9qHoD1s-paHgaQ31JlcoOK4aKUOuhOfzhpJ3YaODH8A_vccMDmR0rGEmFnF8Jl2avCgucTohybCGqz9LsvhMb11aGUq3yMZxF9_NH3ih_lOCTHsJqAlUSHczyjZ4Zb_QqWN1H60CcOWTMUIbcxAT2P2bopF9eomZTHk3hUkifXbBc7FrQN_AmVqT9u9Fs7pCS_TueSkUydL60OcDAhc0o_xlUJGoCB41WU2po1XIcygJsz_-m9VF_5-IpPl6UcxLNG7fBjkQ3ZhTob3XzIBUaOfCQCCJ9LKXU456whYSxJs0l0Eog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/655362" target="_blank">📅 00:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655359">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pk1eowzb6y5Ho4RQschlUbaJlP1CRj0xlHK8JozubORzt8O5waDbRx_4cKav4PdPrW6y0UUj8mHJA3R4g71rdMNRKxXlmzhzlIn34W64E4aK5aq4eQhjVxExKHRSAvaYaPPj66-xJ4v1iyn3jGALy8dkmvg5YVK8GIBMKnl8p2NSOqTExNwIGI_2APDhW9I4yvTjVL8ceH1GHjkgsjxClIwqcrZYJq2rQ8uW7nIlCOKMdVVJd6FYErzsmiJ5F8--tNxfi-HdUND-wU3G5jP3qhrW6gwTzET0emcsSl4sPXMQ4yDuXIshsag2S3xH62j7SCkPCRzdJcAjCvSKpx6Z0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بدن در هنگام خواب چه اتفاقی را تجربه می‌کند؟
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/655359" target="_blank">📅 23:43 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655358">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
شروط حزب الله برای پذیرش آتش‌بس با رژیم صهیونیستی
حسن فضل‌الله، عضو فراکسیون حزب‌الله در پارلمان لبنان:
🔹
حزب‌الله و نبیه بری، رئیس پارلمان لبنان، مواضع یکسانی را در خصوص آتش‌بس اتخاذ کرده‌اند.
🔹
طرف آمریکایی در تماس‌های اخیر خود پیشنهادی مطرح کرد که بر اساس آن حزب‌الله حملاتش را متوقف کند و در مقابل، «اسرائیل» نیز از هدف قرار دادن ضاحیه بیروت و بیروت خودداری نماید؛ پیشنهادی که حزب‌الله آن را غیرقابل قبول دانست.
🔹
با اصل «آزادی عمل رژیم صهیونیستی در حملات تجاوزکارانه به لبنان» قاطعانه مخالفت کردیم و  چنین چیزی هرگز نمی‌تواند بخشی از هیچ توافقی باشد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/655358" target="_blank">📅 23:43 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655357">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBz6CkTsSQHCs7cuW4xxuI35eo-MUdq0iN6Kv2rNRl_hVjMwlZHeB5lH-561SRH7xEh3jVJdmQtc7S81Kon_7PEPatnL1maSH6_1U24YqbaRTBoi76xN1GEphJHBIKtJIT6BkKwrhyxQAoRzmsf9a9GQ38VulU80yrL2AIEfs1dS_lpp2GbTqQMImD_rLM2VXbctDzLUAL53eI853WEI48GfNEHWGCIyPhdjF2dt8WXTnEVsnCcU7RQ-p6U_aDhq-1uVaUktFSxVuEeDXJsejJ9_HDRH3DBWDHRxvSqZPW6LdWzEKc1zqa81Ja23GE-yIwm3WiSpdfCMCGIrrO313Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اسپانیا دوباره ترسناک شده است | بازگشت لاروخا به جمع مدعیان جهان | لاروخای جوان؛ ترکیب مرگبار استعداد و فوتبال مالکانه + ویدئو
🔹
تیم ملی اسپانیا بار دیگر در آستانه جام جهانی قرار گرفته؛ تیمی که حالا نه فقط با خاطره نسل طلایی ۲۰۱۰، بلکه با ترکیبی از استعدادهای جوان و تجربه قهرمانی اروپا، یکی از مدعیان اصلی جام جهانی ۲۰۲۶ محسوب می‌شود. اسپانیا پس از سال‌ها نوسان و ناکامی در جام‌های جهانی، اکنون دوباره به نقطه‌ای رسیده که بسیاری از تحلیلگران از آن به عنوان «بازگشت لاروخا» یاد می‌کنند.
معرفی تیم‌های جام‌جهانی؛ اینجا درباره اسپانیا نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3218741</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/655357" target="_blank">📅 23:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655355">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60a5f71e6e.mp4?token=ARoQ5u60LzrLRNyk1BU078yIYrGD_ZhNJO5htF0MbgSCmL2Mfbk0j1H1vv9F_Nj6_aNFr_TlOl_q_yqtextZbdYfpLdkxi4nf0kFd8-u9eKXKHmT7A-9rnRCIR2Vg2GOoxtP-7Na8Rai8SOkPbRzI36YcBSLe8LNXRCimM5FJqaxyTj9Aa9fkln-Pqr-NQxgKmiHlsAi3Qb7eA8nrgztxGO29PqfJ78azmtlNNktPjrl9-h6RqOptFyepWHdaovrcVactCKnnuwFzgsUXqx4le5PyORJXlSxHd7QcpKbIjqHcPqLBGYGxcro9vbv_P6YPkFT2F_EPjpWq45ahndnJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60a5f71e6e.mp4?token=ARoQ5u60LzrLRNyk1BU078yIYrGD_ZhNJO5htF0MbgSCmL2Mfbk0j1H1vv9F_Nj6_aNFr_TlOl_q_yqtextZbdYfpLdkxi4nf0kFd8-u9eKXKHmT7A-9rnRCIR2Vg2GOoxtP-7Na8Rai8SOkPbRzI36YcBSLe8LNXRCimM5FJqaxyTj9Aa9fkln-Pqr-NQxgKmiHlsAi3Qb7eA8nrgztxGO29PqfJ78azmtlNNktPjrl9-h6RqOptFyepWHdaovrcVactCKnnuwFzgsUXqx4le5PyORJXlSxHd7QcpKbIjqHcPqLBGYGxcro9vbv_P6YPkFT2F_EPjpWq45ahndnJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نیروی دریایی سپاه کشتی «msc. sariska» با مالکیت دشمن امریکایی صهیونی را هدف قرار داد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/655355" target="_blank">📅 23:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655354">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔹
خبرهای داغ امروز و امشب را از دست ندهید
🔹
🔹
ادعای ترامپ درباره موافقت نتانیاهو برای حمله نکردن به بیروت و موافقت حزب الله برای توقف تیراندازی ها
👇
khabarfoori.com/fa/tiny/news-3219643
🔹
مشاور احمدی‌نژاد: حال او خوب است، نگران نباشید
👇
khabarfoori.com/fa/tiny/news-3219653
🔹
چرا همسر این فوتبالیست مشهور همیشه صورت خود را می‌پوشاند؟
👇
khabarfoori.com/fa/tiny/news-3219630
🔹
وضعیت میرحسین موسوی و زهرا رهنورد پس از بمباران پاستور
👇
khabarfoori.com/fa/tiny/news-3219593
🔹
تازه‌ترین تصویر از چهره تغییر کرده حسین فریدون
👇
khabarfoori.com/fa/tiny/news-3219567
🔹
ویدئو‌های جذاب را در آپارات ما ببینید
🔹
http://aparat.com/Akhbar.Fori</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/655354" target="_blank">📅 23:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655353">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eH5EOLrMx_cnB87okhz2nBTVe4DXFkW0kgIVMn23eA6tuLP7anVXZDsCGsm9Rl5OjvYm8A1m93avtpu8jIhg3tCz0MR8DpuXjvNS_vJ_SNebBEkcgc14gbhRIEF6ixqOmKFfmbTluV2RjLceNy3J12GhNE-CXYMXcttiV3MhIGFY_vOMJu6zFwuTZv6nk-ifwh0tXLntdug5hn8O4UTgWbxUM7ypS1XUp4H6RWzdDGXQCct8458wKUPRNSlAl-5AK39JKRwxRgSHXrHb8CXqT-axAL-tkvvdIwbdg_-jvKyA7qbxMvlAr53iwuyYPHDhGmg9_nIsiYYmtJ2HG6-0ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آخرین قیمت طلا و سکه
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/655353" target="_blank">📅 23:17 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655352">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
حاجی‌صادقی: نباید به دشمن اعتماد کرد
‌
نماینده ولی‌فقیه در سپاه پاسداران:
🔹
آنچه دشمن را در همه صحنه‌ها شکست داده، حضور مردم در میدان و ایستادگی ملت ایران بوده است.
🔹
مذاکره زمانی قابل قبول است که در تعارض با این دو اصل نباشد و در امتداد همان مسیر حرکت کند.
🔹
حتی اگر مذاکره‌ای صورت گیرد، هدف آن آشتی با آمریکا نیست، بلکه احقاق حقوق ملت ایران است و جمهوری اسلامی هرگز از اصول و مبانی خود در مواجهه با دشمنان عقب‌نشینی نخواهد کرد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/655352" target="_blank">📅 23:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655351">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPjLp_6SFV4oGmnPnaw61TrkL3mF7J6X9Ulk2vL6MCZn2ojggTweQe08L1nZc6obRLv2oYywX8RgMEWk6syMIIT2ZsPdnG2KmR1uWWQw5EniNIIoSjRbhNO7N8AV1ACBJjBWbZpTgtDxgRP-aUxc3Gj57bojYyy4kQODzGoyBqwFJ3VnwXGzsGZne_iibkaT1gp_r-ZXHqTEORlKApRjtEFWcyKVp65PVIb6jteLe_jEg5GZPUpZwR3BsdBfGOQErBE2EXHR5XJA01ImR8rFmOq8Or2bWAafZ5cHQf7JIhezt35FKyNuuWF0Gw6oF7wKQgsLZHhxL0t-BrBvEHQI9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر کمتر دیده شده از رهبر انقلاب آیت الله سید مجتبی حسینی خامنه‌ای
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/655351" target="_blank">📅 23:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655350">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gvstcg3CLtcZKk1W_LiJwCpBvPIjtGeABrteaLW57ntjeeEyaQ-1cYxiGtxn_IP5I_LCl_cxv46EBdX3WdoLo9kYkmWQLeX9Co7Oyjd0XS0QP4Xx9FUYAZsAEpxwuObCHHSphROw8Y9qzJAdktdBkIo9jgzVvgiNxd62Y-X3NqE7_M-EOMLulLuVSVxoTtK7MVQBUGjjKuQJ_6PFt7nzHvCx2R76E_K_5gmw-mGuXfG-iUIMqMkzqz30vhawf9OMnilxHyuUBbUrR9s0X9d2nLK66B89K-S0ENGf640oeS6B0LjCwVmwr2h12Ko81vuuwD0jOXMgUYfClPKQ3me3Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بزرگ‌ترین آپارتمان چاپ سه‌بعدی اروپا در ۳۴ روز ساخته شد
🔹
بزرگ‌ترین ساختمان آپارتمانی چاپ سه‌بعدی اروپا در فرانسه تکمیل شد. این مجتمع سه‌طبقه با ۱۲ واحد مسکونی، تنها در ۳۴ روز چاپ شده است؛ فرآیندی که در روش‌های سنتی بیش از چهار ماه زمان می‌برد.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/655350" target="_blank">📅 23:07 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655349">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBPf7pg2HWZjhdbMka3fMnTAYDxYbYnnX2THBNyAM0UhSDyVqfNWjVuOzCVjQGogvlOAV6W2ug7jGlWDQvG1xGhtmleK4oZOhEPHM-LKfWImGZLe37FpcZUF81ljFmNiOj_kyyw1pPoIaGgW0I0vEUlbI6-CF-bkQL8prNp5Os7fN32hs1acli8VJe9028XBVUU5_9WFseFVJTbd4WNdy1DWjQ6EoB4S0fI3OC5A8nX9BgPYH3JZBusATpM-rhMyPrsBr8oYhqWs3xqBTc3kS1YBlaf_vz0bVEfiMm4x2EFSzYMTE19LTN96efF1lztEOPT5Vqjeck0UT9dIdbk5zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#WillPayThePrice
#هزینه_خواهید_داد
با یک کلیک به ویراستی خبرفوری بپیوندید
👇🏻
https://virasty.com/r/BWcv</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/655349" target="_blank">📅 22:57 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655348">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aMCyQBhc18J-qM-H5SJXmes6OUgb7SqIHyv2mH-_RllUSxf95aWeN2nsQyVg-xH33-wsQvNF9XUQiwFSyGS5M79N9xDmsi99Y8YJDmdAs9T-61VIk6d13aAWrY2607d1SNxFSRBHWbs3fwmHX2CG2BtdkhGqy-m0BTXBFMUs_edvtp5ahlRf-5iFEB7ayrMowD2kZNrGaIWSbKkI0kVt07endyuMu5CW2xQBPAFUa4VUEmL_C6Ku7m23x7kLV3ja3-y18lHE8b4lsjIGb5ovTy5L9g_Z4_tTFeu8rwe5b4wM7wFXOw2Fo_qwe_DlEch5ZlnVO7XN8Mf8SKbU5jOZnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیام سردار قاآنی درباره باب‌المندب و شرارت جدید صهیونیست‌ها
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/655348" target="_blank">📅 22:44 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655347">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
سفارت لبنان در واشنگتن: دولت لبنان در دور کردن لبنان از تشدید تنش‌های بیشتر موفق عمل کرد
🔹
ترامپ به سفیر ما اعلام کرد که نتانیاهو با آتش‌بس موافقت کرده است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/655347" target="_blank">📅 22:43 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655346">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
ترامپ قمارباز: ناتو درباره ایران به ما کمک کند
🔹
رئیس جمهوری آمریکا علی رغم عدم مشارکت ناتو در حمله به ایران، بار دیگر از اعضای این پیمان خواست درباره تهران به او کمک کنند.
🔹
ترامپ روز دوشنبه به وقت محلی در گفت و گو با شبکه سی ان بی سی نیوز افزود: متحدان ایالات متحده در ناتو «باید وارد عمل شوند و به ما کمک کنند» زیرا آنها بیش از ایالات متحده به نفتی که از تنگه هرمز عبور می‌کند، متکی هستند.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/655346" target="_blank">📅 22:34 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655345">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">شیخ حسین انصاریان: حضور میلیونی شما در مهمونی کیلومتری غدیر امسال ضربه ای کاری تر به دشمن سست و نحیف خواهد زد؛ ان‌شالله
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/655345" target="_blank">📅 22:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655344">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
راهکار طب سنتی برای کاهش عطسه و خارش گلو در فصل بهار
🔹
حدود ۵ گرم گل بنفشه و ۵ گرم شکرتیغال را در دو لیوان آب ریخته و روی حرارت ملایم بجوشانید تا یک لیوان از آن باقی بماند. دمنوش باقی مانده را صاف کرده و شب قبل از خواب بنوشید.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/655344" target="_blank">📅 22:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655343">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
استقبال گروه‌های مقاومت از تصمیم ایران برای تعلیق مذاکرات با دشمن صهیونیستی
🔹
گروه‌های مقاومت فلسطین با انتشار بیانیه‌ای، موضع اصولی جمهوری اسلامی ایران مبنی بر تعلیق مذاکرات آتش‌بس با محور «صهیو-آمریکایی» را ستودند و از آن حمایت کردند.
🔹
گروه‌های مقاومت، این اقدام تهران را پاسخی قاطع به سیاست‌های تجاوزکارانه رژیم صهیونیستی و حامیان غربی آن دانستند.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/655343" target="_blank">📅 22:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655342">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBenelli Motor Iran</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vh35EG5GCVR0lXDFKgRTVmfBJJaNwXHDPePw1Tp8bHwC6X2DzLsnEpeq2r5F9z2GgovYv-Z0kEXgJzHj_myY8Kcuw_B1woEttT60pgOXUGiupiuOYZykRHzYEfBELKbthX_If18UM0mjNsTjjsaET4fsV7v6r8ef1qWbDCzoVOtsHKaR5XDfI39V1O2yLrTcO1HiPnk3_tIAvpVr476mVLsq0km8fr-Nf74azwHJj_Wkfd68vQbdsA_Q_iVugrtriz_Blm1Cx56eANKdMDmyR89xoOqmBI0i2LKRW0vEYbaM3a0QqQOzRqFmC8TdSILGEoEMe_yYtrDQt2-EMGrbZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎖️
موتورسیکلت کی‌وِی K249N
موتورسیکلتی که لذت یک سواری هیجان‌انگیز را به شما هدیه می‌دهد.
🔹
249 سی‌سی
🔹
چهار زمانه، چهار سوپاپ
🔗
برای مشاهده قیمت و سایر مشخصات فنی، روی لینک زیر کلیک نمائید:
https://l.nikrun.com/og2
🏍️</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/655342" target="_blank">📅 22:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655341">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
مقام اسرائیلی: در حال حاضر به بیروت حمله نمی‌کنیم اما نیروهای ما در جنوب لبنان خواهند ماند
🔹
دو نیروی سپاه قم در انفجار پرتابه‌های باقی‌مانده از جنگ رمضان به شهادت رسیدند
‌
🔹
برخورد مرگبار قطار با ۲ عابر در شیرگاه
🔹
عراق پروازهای خود به بیروت را متوقف کرد
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/655341" target="_blank">📅 22:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655339">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سخنرانی استاد رائفی پور</div>
  <div class="tg-doc-extra">مراسم دعای ندبه_جلسه 62</div>
</div>
<a href="https://t.me/akhbarefori/655339" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
مراسم دعای ندبه - جلسه شصت‌ودوم
رائفی‌پور:
🔹
0:03:00 اشاره به ازدواج حضرت علی در تورات
🔹
0:14:20 رفتار پیامبر در مواجه شدن حضرت زهرا (ص)
🔹
0:18:00 بی آبرویی عاقبت حسودان در دنیا است
🔹
0:28:30 دو رازی که حضرت محمد به حضرت زهرا(ص) فرمودند
🔹
0:39:50 اولین شخصی که وارد بهشت می‌شود
🔹
0:55:10 تذکر خداوند به پیامبر در مورد قرآن
🔹
1:07:30 نشانه‌های ظهور برای برخی از افراد قابل درک است
#دعای_ندبه
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/655339" target="_blank">📅 22:10 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655338">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
بن‌گویر به نتانیاهو: وقت آن رسیده که به ترامپ «نه» بگویید
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/655338" target="_blank">📅 22:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655337">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gjtd0X_hyBKQQ3T9bb4WGJxtuLHMffCmOZyf0gUGoiENltdDsuU5chTFPiTSF5UEVC0cqBTCdhK2-zPKSsvf8U-lbHXTY_OPe6lfTLj99nnCZhl8eqxcCBbv0OfhWzddbHelK5pO2d9fkCuGHogWoM5bjWogNHzSurF-udHHIviWeKfEXniHIF__HiK6UUSdOVtekD_oGy0yhNJRcjq_l1OsBvz9kzmr5eoLwQdUrL9OmmmLScZS14w39JXYi_-AJJESPoJpXIk8n4tBODxQmZWBecNBWpRWzCkHldQy3zESOhbad1pJwRSKmnHdv33WwaPZPT56n0IE4P7Magk51w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فارغ از نتیجه مذاکرات، به هیچ عنوان اتفاقات تلخ اسفندماه را فراموش نخواهیم کرد؛ منتظر باشید؛ خون رهبر شهید، مسببان این عمل را در خود غرق خواهد کرد
#WillPayThePrice
#هزینه_خواهید_داد
با یک کلیک به توییتر خبرفوری بپیوندید
👇🏻
https://x.com/Akhbare_Fori</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/655337" target="_blank">📅 22:03 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655335">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
فرمانده نیروی زمینی سپاه: برای مقابله با هرگونه تهدید و نبرد زمینی در آمادگی کامل هستیم و سطح آمادگی امروز حتی از آغاز جنگ تحمیلی سوم هم فراتر رفته است
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/655335" target="_blank">📅 21:54 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655334">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UVYGivUKBxfKrzTtZexho4XsTnNhYdaO4TPNAtOZX-FCDHzn9qczuv0R1NKpAA7ncxJPrXMG5jF8F4_9t83hPk_1cLJv0rDnuamaxCQFAwhFQfsg59qBbHKDZlbuySjWUcviMk-DoxPACSHishyJAlSnR2I55qf0REQ3dc13nKT8oByBOcep35s2fasOII5L2Zke2WqLVFNDUHJndi7yA9K48KyE9sc19SejGItGH0Yq_JuyDAliUNTeT55ISZbS3KsLK6rxZT16Www7Y0xB-gfzktq9EhKPI_X24zDkoR3mL8utouwx-_NS26DvQz7CklkszTGuq1Z1fFL8RYYrCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازار خودرو؛ بزرگ‌ترین بازنده احتمالی توافق ایران و آمریکا
🔹
کارشناسان معتقدند بازار خودرو می‌تواند یکی از اصلی‌ترین بازندگان توافق احتمالی ایران و آمریکا باشد.
🔹
کاهش انتظارات تورمی، تقاضای سرمایه‌ای برای خودرو را به‌ طور محسوسی کاهش می‌دهد؛ موضوعی که به باور برخی تحلیلگران، تاکنون عامل حدود ۵۰ درصد از رشد قیمت خودرو بوده است.
🔹
از سوی دیگر، توافق می‌تواند مسیر آزادسازی واردات خودرو را هموار کند. دولت نیز با هدف کاهش ناترازی سوخت، تمایل بیشتری به واردات خودروهای باکیفیت و کم‌مصرف نشان داده است.
🔹
در یک سناریوی خوش‌بینانه، قیمت دلاری خودرو در بازار ایران حتی می‌تواند تا یک‌سوم سطح فعلی کاهش یابد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/655334" target="_blank">📅 21:53 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655333">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">تنها رمز پیروزی</div>
  <div class="tg-doc-extra">ostad_shojae</div>
</div>
<a href="https://t.me/akhbarefori/655333" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
پیروزی فقط دست خداست و فقط به واسطه‌ ملائکه رقم می‌خورد
۱. امداد ملائکه در جنگ چیز عجیبی نیست؛ چرا که تمام زندگی ما با قدرت غیب رقم می‌خورد.
03:45
۲. پیروزی فقط از جانب خدا و فقط به‌واسطه ملائکه رقم می‌خورد.
05:20
۳. پیروزی، در سازش با دشمنِ بدعهد نیست!
07:15
۴. قواعد پیروزی فقط در دست خداست؛ به خدا اعتماد کنیم.
08:30
۵. امدادهای غیبی خدا:
_خوار شدن دشمن در چشم مومنین
_ بزرگ شدن مومنین در چشم دشمن (ترس در دل دشمن)
_ کوچک شدن مومنین در چشم دشمن (مغرور شدن دشمن)
09:58
۶. ویژگی مومنان: افزایش ایمان در رویارویی با اجتماع دشمنان
15:10
۷. غیب دائماً در کنار ما و در حال امدادرسانی به ماست.
16:22
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/655333" target="_blank">📅 21:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655332">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
خبرنگار کانال ۱۳ اسرائیل: در دفتر نخست‌وزیری سکوت حاکم است و اینکه رئیس‌جمهور آمریکا عملاً اداره اوضاع را در دست دارد، باید برای همه نگران‌کننده باشد
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/655332" target="_blank">📅 21:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655330">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_76QNzAvqgmXV6m0jN-beOrfFHucrhHxFl98BI5p_Ytu4Xyvr_Eidmqbzw3lPg5pGDG57IxgaXPDMrwK4nyBm7TLfTpQBdU0B5QDBDKVU0U8gs_GoPMaK8z4Sqi87Ox48T0sI9jCl4ifvGZ_hsllZUhjmGhCJd8V2W01tAkcFSnZJ_Z6fQbqqmjUphzehBujyiyaiijF42WEhPIQ3tEsl82PD5iJwdfLGOtpV9WRVdAzdcgvxG76ObxtO-GELlFZZDjMc4BdsHzCOYClxCM5vTn-iovnQgiEWV4CvVPUS5S6C_AxZU71IOdzNdgUlLzgvlDBPb7E6WOL4fbHCGmzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ متوهم مدعی شد: من تماس بسیار سازنده‌ای با نخست‌وزیر اسرائیل داشتم و هیچ نیرویی به بیروت فرستاده نخواهد شد، و هر نیرویی که در راه باشد، قبلاً بازگردانده شده است
🔹
همچنین، از طریق نمایندگان بسیار عالی‌رتبه، تماس بسیار خوبی با حزب‌الله داشتم و آنها موافقت…</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/655330" target="_blank">📅 21:17 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655329">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBimebazar</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQAgL2HXllyCdsGCjf_9YLkVarRMDwlfYFImEaPzNNk9wTB7XTZ8ww_WubkIp8-YmkKvJM2vzvSNjMVReomOFK-S5faCRh_n9XXtd7NgAZIfVHLt0bTwx1q_euZCCec35ZJoB-PfyALoPmfPY4qYrvjCAyRbWA6kdmmvw8vx3kmZBXZxkqW3-OwZoMd99bu_AR-60hjzb0hqN03RQ9diVseLU3UICE-vVlNfBTk1wzAN26EvRpaaG0V5_45Ap6h67F7hs4JFAvI1SmW4vAU37rDt2haXtLXt3nGqGvH2VmPph7iYOXnu5uKKA-GEoZ8HxezuyB37Jy_NG916xQ3AsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
اعلام برنده قرعه‌کشی برگشت پول 10 خرداد
🎉
تبریک به برنده خوش‌شانس،
•
آقای غلامرضا رضائی
کافیه بیمه‌تون رو از
اپلیکیشن بیمه‌بازار
بخرید تا وارد قرعه‌کشی روزانه بشید.
✅
شاید این‌بار مبلغ بیمه‌ شما تا سقف
۱۰ میلیون تومان
به حسابتون برگرده!
⏳
فقط تا ۲۰‌ ام فرصت داری
❗️
📲
نصب کن و تو قرعه‌کشی شرکت کن
👉
#بیمه_بازار
🟡
@bimebazarco</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/655329" target="_blank">📅 21:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655328">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZgdaZ1v6Cv1gO6xOCCeaD67ZXd0A_SywV3RTmutGfoSHDHu2cDzxGlfuRDmCVCAiVEEmnf9gxw05ACUKUVcOquoSZSNhhrvVBTRpkeX7uUe0SugQ6Y9hA6L5_VLWpbGCm1jc40uIT32Gvx1xH8d04tGMkIUd3orOVbQIO5lEyq6egXygQxfYEZMsQkSIMilDJ0j3PPnjNytOg9prAlYOPpyYA6QaT95tar8KLz_lemwqyo7f6xw-RFIVoTX-5giq-bUyPvI2VGzAdUMXmYdlTenI7hFGCUFjQiOTqcPXsczDIiWd0e0tbN8BEDlFzdziji5u8rugIno9raf7KTmlmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ اعلام کرد که حملات رژیم صهیونیستی به بیروت متوقف شده است
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/655328" target="_blank">📅 21:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655327">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
ادعای دونالد ترامپ در واکنش به احتمال فروپاشی مذاکرات صلح با ایران: «راستش، برام مهم نیست اگر این مذاکرات تمام بشود» #Devil
📲
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/akhbarefori/655327" target="_blank">📅 21:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655326">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltPKdDDVern8HIE7RvP26BZ37FywhrVf3-uIt4Ot5yqAw63HhU-qWXxqrRmGLSWkInxd54owzXCyw6736IWkp_qrK3JHLoMpwcoRKlFqWTUMFQVsUQAq_lqSZD1ptjjYaFE24VDL6BH7cFUOptcAl5H0XyzWGVrgR_tNCUmFlVMPku2O4ZXFB8nRERjC5s92FyT79kEQ0Kne3FVLaIYaqDoWUR7_ZCwtEZBsmPd0LPbMfwMwfzjyMuysSAuPxwdPPWBvhoj0BwPYGzjklUzI7f2ehvSsk0W5eLyUO1ItVTImkfqFT5QKytZBAPD0ZRM7QGk8ParkC4_OBqghgKEj0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ولایتی: بمباران ضاحیه ونقض آتش‌بس عجلۀ رژیم جعلی برای پایان دادن به تاریخ نحس خویش است
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/655326" target="_blank">📅 21:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655325">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
هشدار برای توجه بیشتر به اعمال، حق‌الناس و سبک زندگی
🔹
00:24:30 مشرف بودن به گفتگو و رفتارهای اطرافیان در حالت کما
🔹
00:31:35 حال خوب من با التماس دعاهای پدرم و صلوات‌های خانواده‌ام
🔹
00:41:15  ورود به تاریکی مطلق همراه با ترس و اضطراب
🔹
00:46:30 همهمه بین انسان‌هایی با ظاهری سم و دم دار
🔹
00:52:00 لحظه سخت برگشت روح به جسم
🔹
00:57:20 به حسابرسی در آخرت اعتقاد و باور نداشتم
🔹
00:59:00 تغییرات رفتاری تجربه‌گر بعد تجربه
🔹
قسمت چهارم، (ورود به مردن)، فصل چهارم
🔹
#تجربه‌گر
: سید ابوالقاسم احمدی
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/655325" target="_blank">📅 20:53 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655324">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZMcaWGUGlc6oVuBa8jyOmpEo2uKal73EVTQ5WHOu0loDkMWWuRFzHzhY8S628QPCiNSsSgRfdtlInWEwBHMXygCynYKQTOxTmz4gal9oPDob4hNy7wK7xdu0DeBlQsRF0qmq389_91PVo7kCRlTih0a9PeB_R7vEWziXhXxnMZw76ZXM9hWzryUhXh1SL8gtfCSNYK0mmpWqjqX5ADF2Xgen8iQ28adVrnoyxbHP3TSan5kMv-sKodCGEBqstcCXJ6x-9GcdmGlRHJuftbYCBZarSACdL1_2tS8RWkRHZqrTSthN20zXArqxynxOx4cJ60pyqamxno7tB6OdFuFqJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیانیه وزارت خارجه در خصوص نقض مستمر آتش‌بس توسط رژیم صهیونیستی و آمریکا
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/655324" target="_blank">📅 20:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655323">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
ترامپ ادعا کرد اگر گزارش‌ها مبنی بر تعلیق مذاکرات ایران با آمریکا درست باشد، «اشکالی ندارد»
🔹
فکر می‌کنم ما زیادی حرف زده‌ایم
🔹
این به آن معنا نیست که ما برویم و شروع به انداختن بمب کنیم، ما فقط سکوت می‌کنیم؛ محاصره را حفظ می‌کنیم/انتخاب #Devil
📲
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/655323" target="_blank">📅 20:43 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655322">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LhA42wMxanCW6maaqe0LLewLipTOXFgq9V4wmtEQzdwzMjYbH8qbYc3Rt-_a9N4-S82jdMytlWZuNAky-10xC9T9FS01qdgJsF8EpxqIMOddDhF733AH7RHHfS_TOnWkFqO42Ft5o8wY90uaHdMFLjqJ1UcSuoJCxN_fMPZ8sp8xiU4PZOPEs_4RsAIszbuZl_ADMXz4doveIh9O1wRH738KXpWRlbEL-XVsAC10rmg8eMxUHwZGV-7Hlw3p4PY9kufgi2D281iajqsErzD2oYFQ2zaSbv-4jN4zdR6SupTP5Q-4XFSI2zTV7mQOh0hW_C7uKinsE_cCa0o8iSWNMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕
بیش از ٣٠٪ کاهش وزن با داروی جدید داروسازی دکتر عبیدی
اپلیکیشن تخصصی «مان»
با همکاری داروسازی دکتر عبیدی، با استفاده از دارودرمانی زیر نظر پزشک و ارائه روش های ساده برای بهبود کیفیت زندگی، توانسته برای بیماران خود
بیش از ٣٠٪ کاهش وزن
به همراه داشته باشد.
آمپول لاغری زیکورپا (ZCorpa)
به‌صورت تزریق زیرجلدی هفته‌ای یک بار استفاده می‌شود و مصرف آن باید همراه با رژیم غذایی کم‌کالری ، ورزش منظم و زیر نظر پزشک باشد تا نتایج مؤثر و پایدار حاصل شود.
📌
فرآیند درمان به صورت کاملا آنلاین در اپلیکیشن
«مان»
و تجویز دارو تنها با تشخیص و تجویز پزشک انجام خواهد شد.
🔻
مشاوره رایگان با پزشک</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/655322" target="_blank">📅 20:42 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655321">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1Xve8rmvR6phGsfs8uyGIeoZ-ifXQbpAohN7RC25_GZoljKHplPsUCcUhblqZe2zmwdaK0lK7pqxwfx2rzeXUEzK1OQaC2vlNlg2rnRjlg5n8dTjy_8I-hEAwl6eRD2kZF4VzUJSckAJS6rVEpk8VUUIZ_q9IfZV1j4cDAvfQX79cMcxHu_-0lltBMnxRxeKXosfinkjqiXN8U0AvjMZ0405gG0nFz72UBeBeenKSNrK-_yarVmLrD5G117mrFrlVFmZxXTfrYLKirEu2hI2HsDopw6cOdo4DEbXAJADiwUUUtTwKXMTtyPX77Fw-LY-luGEt8nYmRFo0tl44v7yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کفایت مذاکرات
🔹
بر اساس اخبار منتشر شده تیم مذاکره‌کننده ایران در واکنش به تداوم حملات و نقض آتش‌بس از سوی رژیم صهیونیستی روند گفت و گوها و تبادل پیام ها از طریق میانجی‌ها را متوقف کرده است. گفته شده که توقف تجاوزات در لبنان و پایبندی کامل به مفاد آتش بس از شروط اصلی بازگشت به مسیر مذاکرات به شمار می رود. در همین حال ایران و جریان های مقاومت اعلام کرده‌اند تا زمان تأمین این مطالبات گزینه های میدانی و راهبردی خود را حفظ خواهند کرد. گزارش‌ها همچنین از بررسی اقداماتی نظیر تشدید فشار بر مسیرهای راهبردی دریایی از جمله تنگه هرمز و باب المندب خبر می‌دهند.
🔹
هفتصدوشصت‌وچهارمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/655321" target="_blank">📅 20:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655320">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
ادعای شبکه کان اسرائیل: حمله به حومه جنوبی (بیروت) به دنبال دخالت آمریکا به تعویق افتاد/انتخاب
📲
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/655320" target="_blank">📅 20:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655319">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
ادعای شبکه کان اسرائیل: حمله به حومه جنوبی (بیروت) به دنبال دخالت آمریکا به تعویق افتاد/انتخاب
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/655319" target="_blank">📅 20:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655317">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DSHRdeexpF32jgHrzvWW5SGBC0vDHyC7TFZiPQeCMu5u50xhb0K0_PLAkaybVCyNzbWgwWZAHf1tw4nzUdfNqm2e8WCCw3ztzr5ay7X3OY3Ql1weFavc_WoMfeSYIrYRK_ELaXtok0w8PFezWx9z90UIMG0F2drrNLduQPVDcBiYdthtwASwfvI1cXMlHgPAU5CrLXRwT2bJzCmWDs9B2kMVMYkY7iUKtcB1oLUPL3TtUpJZ5r3y9ls_IcZxXhQHtGDA3z8ZV_Nui2Q4MX9Gae4iFbBjt-OrWVbuwXkdzU1sCOBnom8H8WMHAboJPRoKBa-0jbvewsrvM3oQwKyPXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gs8iYfECbliXxwy5BX6YdiYAEZ3S0JcxKKbOt3xHCvHXukaaRajNJtBzXdBWuhLOiT9BkfMIsRrzD6sgzrKhvqb_LNGLwNhRsnzVGGcWdGZ44K4Pu1fS_u_r1OOSoGgh_E3_PGNfU7BCKb93SiqfcKMVEbxuEzngMAKfTgA3yjxpbs499FLLKAS-IwzZnjOsqL8XlaM7bD_rK1tU1-HbVTiIO7ozpPNJSQ0YposPTS7-ijtL0tGUPEOkvFS-veeW-WeBPdi2MAiSKxiEVLh0AxQECcXM1ULzY4wHyp9CljnOxUTELWlhCxf6cpiFyF9k1wIUEyherYF6L5NPen2EIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📚
نام کتاب: ته کلاس، ردیف آخر، صندلی آخر
🖋
نویسنده: لوئیس سکر
🔹
اگر فکر می‌کنید مدرسه فقط جایی برای درس خواندن است، «ته کلاس ردیف آخر صندلی آخر» نظرتان را عوض می‌کند؛ روایتی طنز، صمیمی و پرماجرا از نوجوانی، دوستی و روزهایی که هرگز فراموش نمی‌شوند.
🔹
این کتاب به نوجوانانی که می‌خواهند کتابی روان، سرگرم‌کننده و درعین‌حال تأمل‌برانگیز بخوانند به شدت پیشنهاد می‌شود.
#فوری_کتاب
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/655317" target="_blank">📅 20:29 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655316">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/082de9a0a2.mp4?token=d-T7_QRlQ8zUv0cLKRZSDfZG4gPdGCwqav5KqBAP2g2oO6F28-f1HItLiGcpjObLThfBdEjqGuTzar4UKAGL-sg9MLnMIO-uVRkvl6zkdDSytFgUHes24mOAukjAbvr0oeT7-K9lqUZ2iGQ5uCJUB40Y8liYdacrJG-NWq-QhTn2i9019_-yz9vEF5pjfaMzpeYgWEVqBcNOnH6hrIIMYjyFBJfpYkB_v3fmWNXBT5gAqjNqTpuyHQwgGcdoR_ZbCxqYxQVsV4SE9-jARkKCuxIDC5oGTPK_Vudc0OiNcPg79bN3LJ3oKqfzIW5eYgRARJah6KRZ3IhQwaoOjpcdqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/082de9a0a2.mp4?token=d-T7_QRlQ8zUv0cLKRZSDfZG4gPdGCwqav5KqBAP2g2oO6F28-f1HItLiGcpjObLThfBdEjqGuTzar4UKAGL-sg9MLnMIO-uVRkvl6zkdDSytFgUHes24mOAukjAbvr0oeT7-K9lqUZ2iGQ5uCJUB40Y8liYdacrJG-NWq-QhTn2i9019_-yz9vEF5pjfaMzpeYgWEVqBcNOnH6hrIIMYjyFBJfpYkB_v3fmWNXBT5gAqjNqTpuyHQwgGcdoR_ZbCxqYxQVsV4SE9-jARkKCuxIDC5oGTPK_Vudc0OiNcPg79bN3LJ3oKqfzIW5eYgRARJah6KRZ3IhQwaoOjpcdqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شری بیگز، نماینده کنگره خطاب به منقدان جنگ ایران: ایران نباید سلاح هسته‌ای داشته باشد و ترامپ آمریکا را در اولویت قرار می‌دهد؛ اگر این کشور را دوست ندارید، بروید بیرون
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/655316" target="_blank">📅 20:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655315">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
شبکه ۱۲ رژیم صهیونیستی: نتانیاهو و ترامپ طی تماس تلفنی در حال مکالمه درباره مذاکرات و  اتفاقات اخیر در لبنان و ایران هستن
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/655315" target="_blank">📅 20:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655314">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
ادعای ترامپ موهم به خبرنگار ان‌بی‌سی نیوز در مورد ایران ادعا کرد که در مورد گزارش‌ها مبنی بر تعلیق مذاکرات از طرف ایران چیزی نشنیده است #Devil
📲
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/655314" target="_blank">📅 20:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655313">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
ادعای ترامپ موهم به خبرنگار ان‌بی‌سی نیوز در مورد ایران ادعا کرد که در مورد گزارش‌ها مبنی بر تعلیق مذاکرات از طرف ایران چیزی نشنیده است
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/655313" target="_blank">📅 19:57 · 11 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
