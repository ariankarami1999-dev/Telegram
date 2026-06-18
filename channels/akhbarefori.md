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
<img src="https://cdn4.telesco.pe/file/OmnSSnxanoCXCxHJckNwsPtokqW-sErO63vLTsE7iUJHcjh_x8CWZ7lqy8f-gmdUANYH0KEJsmXrM9vS2H3eIHvUruRnhVpWsbiglnCnCdlnOvOKn14kJ902aRBg_Ht3dNXuBY4hzjRlI6UAzfKGbnAMUuRk7VlcoN2rXHZv1CUBwzluD2tU4tlbp7zQFNniYy_6YCINDjH-ZTOfr2DtCvyULJ4dJfxUPHqf0PeBHyqZry3o6tCqCpUPToR1DFp-e0R6qpiUNQTwngh2nfU_i0EZVADl36EHeFOC3b_tsrw2EU58js78A1qSKgznmf-LqsemhfzobkIsRfYhdoauzg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.49M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-28 10:27:23</div>
<hr>

<div class="tg-post" id="msg-660727">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AdrfYEx-kU-HBRD5YfUYERbG490Uz522Eb0wh7LedgwcDZu6fjiw7lptxTVuuna-Emay-E67-bqMyO77UtvHQiSvw3mB4M9h32vyQkuIpQWdZaw5IKpIUzd_ossgD9Uaj9mmgGn4DYvtJ_EDW5707wHDyBF2f7dsxI1246IhhUBHAtZTHRdNFg-Lqcc4tHKnZWcOd6LvXvjSNsOJ6StIr-UrrMxYojkXYOs98yLFui7kVUFAjXMieUa2bEfHjdee-QTUUVHs38h5kJis0vgTGfDPkKdxeTEnQuL7ncCMXh4kwQj9QKhYuIEqENeq3JFMSzkRQr2RT5CikVELwMKxYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سوزان رایس، مشاور امنیت ملی دولت باراک اوباما در دوره امضای توافق برجام: این یک سند تسلیم وحشتناک و حیرت‌انگیز است که با صدها میلیارد دلار غرامت تکمیل شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/akhbarefori/660727" target="_blank">📅 10:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660726">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4254c932f0.mp4?token=h_X5IJCF2jVl6Sl_CTZId5FKl2kK-NGcR42dauB7XMvCnKwwSsWWyQUuYYp4IPWMHkRxVqbZFtJNQLpBH299qZFnC6Zavpp_duF1FIdGFEPkrehcl2lqj89Fo2EBniXJi3brDjhy14feIq2otK4jCKLVwmOL7oZx2yCHVbj8oJBczGuzesRaJCx7B2XxGoh6RqzUZNmIPr-reYkjQpQrSrPEcSutNvJg_1Crc5U-EXgX9YJg24XFgEE406m3QPNVt7DKxn92UbYb8vPUGVlnHtYhmVvHvedlXCkX2K4i8wTCoOKWZR4J8itaT6NwS5W1x3wO_O5eQEhTpQMwmpEoIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4254c932f0.mp4?token=h_X5IJCF2jVl6Sl_CTZId5FKl2kK-NGcR42dauB7XMvCnKwwSsWWyQUuYYp4IPWMHkRxVqbZFtJNQLpBH299qZFnC6Zavpp_duF1FIdGFEPkrehcl2lqj89Fo2EBniXJi3brDjhy14feIq2otK4jCKLVwmOL7oZx2yCHVbj8oJBczGuzesRaJCx7B2XxGoh6RqzUZNmIPr-reYkjQpQrSrPEcSutNvJg_1Crc5U-EXgX9YJg24XFgEE406m3QPNVt7DKxn92UbYb8vPUGVlnHtYhmVvHvedlXCkX2K4i8wTCoOKWZR4J8itaT6NwS5W1x3wO_O5eQEhTpQMwmpEoIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۱۰ گل برتر دور اول مرحله گروهی جام جهانی ۲۰۲۶ به انتخاب FOX
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/akhbarefori/660726" target="_blank">📅 10:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660725">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/238281eef9.mp4?token=plGp15okGyPS7Y8VQuVWnsAi-XTVCTZY7eR6oiT8RpwPbCbCHFR5YQAqRUaeW82SAGIU5bmhRCCsxlv_SmMwOUk3452UQ_1omydANH16Dq4e569bH7he0w3l0xvkvMln3-BskS4ii9XWYrPBYtFhUi-a260d-E94mN6C-9GSMZDnk-SFU8hLqTJjXclHGbj3qwQCD_zDqAgWRpOAx20yehw5N7e3llNxlxWvVdJ_U4Sg6Yso82iMLuves9L-comlhL1nWl_P45M88BALFpnHtoEgm1UsiT5oQhsSeI8t8ZwOLMF9Qv8M9YZIOv5YbrLUGD9tyqa-t9OL2v4rr7VHMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/238281eef9.mp4?token=plGp15okGyPS7Y8VQuVWnsAi-XTVCTZY7eR6oiT8RpwPbCbCHFR5YQAqRUaeW82SAGIU5bmhRCCsxlv_SmMwOUk3452UQ_1omydANH16Dq4e569bH7he0w3l0xvkvMln3-BskS4ii9XWYrPBYtFhUi-a260d-E94mN6C-9GSMZDnk-SFU8hLqTJjXclHGbj3qwQCD_zDqAgWRpOAx20yehw5N7e3llNxlxWvVdJ_U4Sg6Yso82iMLuves9L-comlhL1nWl_P45M88BALFpnHtoEgm1UsiT5oQhsSeI8t8ZwOLMF9Qv8M9YZIOv5YbrLUGD9tyqa-t9OL2v4rr7VHMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سناتور کریس مورفی: این توافق جنون‌آمیز است، ترامپ تسلیم شد و ایران پیروز شد!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/akhbarefori/660725" target="_blank">📅 10:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660724">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f359529c05.mp4?token=kFNXvkKQ5DCIMzUjVN4ZOvE6Lmya5_1e3I7GSkXcfQtKNK2RiT2uyCWE9odOL2-4a5tDxwKvpc02NRzobAdiuoPJ41f5ZAU0BUcxA2-KqfotIT5rI4xdWXMCFn0Ni4Z4EqQd238HygqmkNiNeHdOxn-SEt-M8IngNjJYqCRGL4LFU5mWVg8MsHJxP-bqCdLB7dnpVEXBXuS-tkuxObUAKg11S-UZ0VvcSU4ULBDNATQs5I_3K1zOZP9tL74yq6plDuFZkwVCHaCQQOzdPd8xq6j7VvUb04t124hPhQ-wv76ZA5JtKRXlccPb4E4_EqEiAenpMD5Kphb0JtNa534S5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f359529c05.mp4?token=kFNXvkKQ5DCIMzUjVN4ZOvE6Lmya5_1e3I7GSkXcfQtKNK2RiT2uyCWE9odOL2-4a5tDxwKvpc02NRzobAdiuoPJ41f5ZAU0BUcxA2-KqfotIT5rI4xdWXMCFn0Ni4Z4EqQd238HygqmkNiNeHdOxn-SEt-M8IngNjJYqCRGL4LFU5mWVg8MsHJxP-bqCdLB7dnpVEXBXuS-tkuxObUAKg11S-UZ0VvcSU4ULBDNATQs5I_3K1zOZP9tL74yq6plDuFZkwVCHaCQQOzdPd8xq6j7VvUb04t124hPhQ-wv76ZA5JtKRXlccPb4E4_EqEiAenpMD5Kphb0JtNa534S5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کنایه نماینده اسپانیا به ترامپ: تولدت مبارک آقای نسل‌کش!
🔹
نماینده اسپانیا در پارلمان اروپا در اظهاراتی آتشین و کنایه‌آمیز، ضمن گرامیداشت تولد دونالد ترامپ، او را «آقای نسل‌کش» خطاب کرد و با لحنی گزنده، انفعال اروپا در برابر تحولات منطقه را به باد انتقاد گرفت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/akhbarefori/660724" target="_blank">📅 10:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660723">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s-g-SRPt2Wl92uA1-FIya35AxBFmMkXxOcpPEPjWaj0SPc7e1wSwCo3ZV0yl0hmhD6xf1eCH4Ds3o8tgHP545an-dc3ezprC2B95AnbzPaLTqrjPVXoDE2XfzahuKOp6lA-Yx_XtS1LeiderxSBjdVsHqSr5GoDRtyVI6ps2tcpuyKhEkvbr4wA_Q79X_BlzPZei8OFKkMVv9FdHD6QtoDocxNsqUoLaECxU_JS09IJm5IKOD5c3j7NVm_Qeglk53_bcxq2U8Hgb-2UbsvR0upRfJr1FP1DX2o68WqtUsyRnY38aHriOPMRMbubmiGwtzReh9T5G1xrqwiFqsqyiuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش ابطحی به امضای توافق ایران و آمریکا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/akhbarefori/660723" target="_blank">📅 10:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660722">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/igNwrZO8OU9h5Nuv7qcF6vSRWp4kAg9gN3g2I9VjftD1u1GEpOujoGwCC-uER2uDAYTa_eL2ZECS8To0xRK6jBqbGebLu3LG_DHxbmWAD1N7cm38lvlYZhYcX7RNBWWUzD4m4RMNMA2jOrV8pIRQmyJfgGxi5McdbeN8QgWMvW4nIzm-wepiyRWsovm9eA0oG09S_Msps73YYLk53ZogCepgQ3Sm9GrqDXcFimrP22Jx_f_sVm-1oE9Xai-D0trVz_dpECcMYgur_476PynMs40ajA4JK2-DXl6EGXBQbf8HunD044Qc5HVFZqQ-SYQ4Fsm0E54Ec-k7Y_hsjCgCWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاری که کمال‌گرایی با آدم می‌کنه #سلامت_روان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/akhbarefori/660722" target="_blank">📅 10:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660721">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WqhNPX0YHPqmMmRWjJ752e3QlV1thW4JsdaCdFDqvcMeRPuLEgP_gczbDAjqvFz4007YjJmywJC9rCQuw7EI6UEqmgEsXlcIHAUUlnHG06UmBIj4p10FyiTeDPGOb8GLLiQ5WQWxPeBPaBODIiQp4s9zmX1yIVHJ92pErps62PyErcncSxFqNRpmfn9vBvSCa7wDd01zFuTG6AwcpjR8FItmpY8voz7-XPN5_Rw3ogEayIdPYOsckxwOFJ_pXwXM1w-GLHpeR4rzNtey-XzFPmjsqNFsxvbK_KPp6n4kcA745cW0HbsxlBW3WR9Pht5bJJOpIuwKhthOJaFe5WyQfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگر به‌دنبال تبلیغاتی مؤثر و دیده‌شدن واقعی هستید
این کانال آماده همکاری با مجموعه‌ها و برندها و تیم های تبلیغاتی بزرگ است
🎯
مخاطب فعال |
📊
بازدید بالا |
💼
همکاری حرفه‌ای
📩
برای رزرو و هماهنگی پیام دهید
👇
@newsadmin</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/akhbarefori/660721" target="_blank">📅 09:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660720">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eLrKVAE_KxfTTF9kYGVEVcXYURss-Z1PRyxYFH3L4V0UFMTCBR4Woq0aKRnFXkkvFvBf84w9obDGioCgna5mwgxbNiumW05AmTqapH9AXzwIU3pfG0DuMBxV39yaELz0NHOfNU8imseq5_Q9WBwyUDKcK0XGtPaGubfJFfZJ9cN3W62o3lTn_E3vA-stfKsL4G4aDKEdsbtLnbCR3l4I9WxltGOE3sis2Ea1hi0-2fEqfnr0lkW90qK-3tHl-aS7RIm6c5325OwJMfnbYt6ui04nP7jJpvGkxTu06hI2zyfAFUds2DmAZg3WbsNhizrQN_lO2qroGzbyat7PtrvdJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
بازی پاناما و غنا با ۴۲ هزار و ۹۴۲ تماشاگر، کمترین تعداد تماشاگر را در دور اول جام جهانی ۲۰۲۶ ثبت کرد
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/akhbarefori/660720" target="_blank">📅 09:56 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660719">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
سوئیس از برگزاری دور اولیه مذاکرات ایران و آمریکا در روز جمعه خبر داد
🔹
سوئیس از برگزاری نشستی با حضور نمایندگانی از آمریکا، ایران، پاکستان، قطر و دیگر کشورهای مربوطه در روز جمعه برای مذاکرات اولیه خبر داد./ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/akhbarefori/660719" target="_blank">📅 09:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660718">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ifd7pNgXax7cY4RyuBmbjcewD8tgzEzCdcNcOTeg8PBlIrG8F-2P_sL7qXbG2RJ7pCU3d1FesR9UB6w9nnifZtKGHSG1mDMpfTrssOXZvwv0FVUGKE2virfXnGrrBm0DznUrlxS1rabSDta6EiaKJ4fbVFA_kEscp4Sp5viAZKe_mOaN6qgZeq72B2F65BCIBx4ZbQCxaOGF9xfEOPDK8vUTYfpM0RbZRFwC3uNyYSKaUftganZ939q79M--b0kTIJh4ObBP-uHEKjszp81UnEiPN3CxddKvHev_Vdr54vin7xJ5x-grbMVbnNI-VfLWk5M1BeKDL89d4lhuJbCO2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ثروتمندترین کشورهای جهان در ۲۰۲۶؛ لوکزامبورگ در صدر
🔹
بر اساس گزارش صندوق بین‌المللی پول (IMF)، ایرلند و سوئیس در رتبه‌های دوم و سوم و سنگاپور نیز با ۱۰۷,۷۶۰ دلار، ثروتمندترین اقتصاد آسیا شناخته شد.
🔹
آمریکا در جایگاه هفتم و ماکائو در رتبه دهم این فهرست قرار دارند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/660718" target="_blank">📅 09:49 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660717">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
پلیس: مخدوش کردن پلاک حبس دارد
پلیس راهور تهران:
🔹
هرگونه دستکاری یا تغییر در ارقام و حروف پلاک، جرم قطعی محسوب میشود و هر مالک یا متصرف خودرویی که در مشخصات پلاک وسیله نقلیه موتوری تغییر ایجاد کند، پلاک وسیله نقلیه دیگری را الصاق نماید یا از پلاک جعلی استفاده کند، به حبس از شش ماه تا یک سال محکوم خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/660717" target="_blank">📅 09:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660716">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cK78Xm1snz1Gou3O4eiMlLHR869ok2gW_Z0jTNAwr0O0LIF6ygXi43bZzg0nAyCY1B78aNpL_WkLC9ObGBBdG6wN7dR5GOOZ1NqNQu_xAa_rx0Rp_--TLoBrc8Pp3x81sgyHE_WAB59jp4F6o1qDU8axAtm0ye00zajAUenx1mnrbHpoD3X6_oJxO5r-TV87q1_UW46kl5oq_j0vOn-iR3QE-mqSCkLsvt9xUN7nCcQNXJFqvZqTTLdTabFVfcTpn1vdp29XclI7lqjwDMPlwI9XkVnn8sV4XeHkDnirw65_QeestHCMo-oKCQlNVarcNJEUEGuwVFhsya3tv54kHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویری متفاوت از ترامپ و مکرون در ورسای
🔹
دونالد ترامپ شامگاه چهارشنبه به دعوت امانوئل مکرون، رئیس‌جمهور فرانسه، در کاخ ورسای حاضر شد و تفاهم‌نامه پایان جنگ با ایران را امضا کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/660716" target="_blank">📅 09:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660715">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwAIl_NaYjESlD8O-W_4Tire4iLmllfFlWQEN8t4CmlqX83xmIqAhFb3Hdc9NrTBy9rmIAUsGV_Ngn10zO_F-574isG2wPt9HTTYlZsMJAoBjCUqw_ctcxBGIiEurf6m3G5FUIJofnSYXOPh1zngblIhGx3ypn_ElmzyBs0p-UVHfg_rOejnViIay5zA5pLtiouq1SFBtoa9-seBdanZ5taem6xNnvCmhfYfMsJ2BcejrwRMPol9L9-DhNEdtwGtsHR3c-lQ7WwPqCjC9K8zOe2UMI7cQQ1m2j85dUocPW915wpL3AJ4G2e4jNqlk6lzHTX3zocR4wo6RpuXHjWqxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برنامه بازی‌‌‌‌‌‌‌‌‌‌‌‌‌‌های امروز؛
پنج‌شنبه ۲۸ خرداد ۱۴۰۵
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/660715" target="_blank">📅 09:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660714">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/avEHlpyBgw88d0RLgoJRD1txFWFR3ANBe-W61g2mYfgWcxv6Kho6Ve_eFymz5wNZwYl70Le65kRWcHK_lHNwPqRXX5coteFxedn6wEBXHos4bK-eN10MbwWcCaYPP8R_uvaNwKtLsljio-J6RuKwNgJROmNKIWzLLdFHpPDi20biRlbGnehpH2RX0l-IlsSHNOfjU4A0Kdvg9jSOp2VCSB9Xr9j0Vs_ENmdNE1kpb2BTYfpMfstTIqRaut9b5ggydz_UlN_NK9fT3ytlu9eAnn1yd9gLr7laFwTvwNLRN9AYF0D7pYGrCL1mfsm7IHRL5LW8S08Ia0tVxfgHacK-Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وال استریت ژورنال: ترامپ در حال از دست دادن تندروهایی است که زمانی از جنگ ایران دفاع می‌کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/660714" target="_blank">📅 09:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660713">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GqaoMoQ1zj2RC6c-OO4lG0qoRHL_L3JQ_HjAX48FR8MH5cCvPYpZJcMsGfBVfv818tQ7LG8RHemH-IUTlWgqgAgIwZ-zeZnFF5hqkbK3WKaRjvRa9c70R9oQCuMGM4KkdK7CxCwaB3om8C2PnOjraWtqDzvpgfi3pAsEjHPB1AORTFIH1jwjNQ0aVWGdn1uVaaReK1043Cq5QVmwGv44DY4aXpwj_sUCeBOeyATINp44qH_Biwd9mPF0VGt-bTk8TU-_whEarw6EaRVxMmDo3OaRWQltqm-45OtsutVTleKNLxr55TBE7POmzLHmeTtSOkQoCoqlS24xEJwmghqpIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طلسم بزرگ؛ رونالدو در ۱۰ بازی اخیرش در تورنمنت‌های بزرگ گل نزده است
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/660713" target="_blank">📅 09:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660712">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d0572ec6d.mp4?token=WmicQv0q9itw_3Kdo2Eqily6B6vDcsnKJFRUgIAmEc9lWwo7ELkJHR_v3TOyHai1ak2C0YeeXSThR-FLNM7vCgNIuzj-qatIFRsAsX2SRpF5or0ZgFL9_c2D4z8MEc96ti8vTn3kVEXoaw1b8UNRRRXpQcSt27s73dpF-uw-ug0JhaGX-tktJnOwiBg0V0sqZEpDDNHJbSVIWV1OwTJaViPtjaPS8HT_-wizHpSxNUi8iCkf5MekCzBFIvXWSz-hk358Pz_2HAlMbEMbFL3Oz4Q6ldIGPbk24mzLZUP-L8iY-pUARGp4GsMjZVCW5NjlaECkYH7E9HrqFFaGlIH6YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d0572ec6d.mp4?token=WmicQv0q9itw_3Kdo2Eqily6B6vDcsnKJFRUgIAmEc9lWwo7ELkJHR_v3TOyHai1ak2C0YeeXSThR-FLNM7vCgNIuzj-qatIFRsAsX2SRpF5or0ZgFL9_c2D4z8MEc96ti8vTn3kVEXoaw1b8UNRRRXpQcSt27s73dpF-uw-ug0JhaGX-tktJnOwiBg0V0sqZEpDDNHJbSVIWV1OwTJaViPtjaPS8HT_-wizHpSxNUi8iCkf5MekCzBFIvXWSz-hk358Pz_2HAlMbEMbFL3Oz4Q6ldIGPbk24mzLZUP-L8iY-pUARGp4GsMjZVCW5NjlaECkYH7E9HrqFFaGlIH6YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فریاد«فلسطین آزاد» هوادار تیم فوتبال انگلیس روی آنتن زنده بی‌بی‌سی؛ خبرنگار بی‌بی‌سی برآشفته شد!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/660712" target="_blank">📅 09:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660711">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aA3gr-51IneqhezGCXaIFwwxPt2vlpyI7CWIwu8vxmmptc8f-rwlBKzcQkH6a851g_NgmbWXg3DCZBMdtM7cLmfRRQgQz-SWGjk3vimSuiAkV_TlPwiCRjtKXBZqoYfDa_3pZ8EbL3kZUA7D-LSaMF8jcty4y0WwQQvdtc-0xgPVUPmNDf6Jj1oq2Bxc1gEva1gSFE2ttM6tpu0s6iymjAY4jqaKPHOVq0ftPYFhBWiD5a97wPeaQ8tp10vh42lgkTgh1Ce1dhn99utdP4ZH8tpfOEDa9uOYy0AnFTO_LNZ0VfG2QgZ6cQJQxts4avpJ867qKgwlN9S3LfbPh14l4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
عکس روز ناسا از نمایش رنگارنگ یک ابرنواختر
🔹
ستاره‌شناسان معتقدند لکه آبی پایین سمت راست مرکز عکس نشان می‌دهد که یک ستاره بزرگ منفجر شده و یک ابرنواختر را پدید آورده که نور آن ۱۷۰۰ سال پیش به زمین رسیده است.
🔹
اگر تأیید شود که لکه آبی بقایای یک ابرنواختر است، یکی از نزدیکترین اجرام کشف‌شده به مرکز کهکشان خواهد بود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/660711" target="_blank">📅 09:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660710">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78bd638263.mp4?token=aTh2I7AL7_m7BgZNE1u7mIMAWTGnf5TvGoENAzTmxsLN0oIdIbuL7a8FBHyLa7_PTW118HZylpcnir2vb_CV85ZR1nAKYrmfWziYI4dRqX9TYV_Q3UfEB00iEeKsZpXTwZvn4qEReJ_smF3Gtj_TIPK5WVPb37pMIO8z3GcntNopqTqgU-ec4epS4owO98LtRvTith0yEdvThguJpSblCinEb6szs6rUzEKJQcb7klotEqe7v2PpmNpDBXl5IiDxlZN7ghtYLt24sb0FsyeAEMKHcUysEASy2kojUmTgoQ1hwjOT7TKQpSaPvM7pzXhuIyf4wI_R7wqrJ2hfwXKX3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd638263.mp4?token=aTh2I7AL7_m7BgZNE1u7mIMAWTGnf5TvGoENAzTmxsLN0oIdIbuL7a8FBHyLa7_PTW118HZylpcnir2vb_CV85ZR1nAKYrmfWziYI4dRqX9TYV_Q3UfEB00iEeKsZpXTwZvn4qEReJ_smF3Gtj_TIPK5WVPb37pMIO8z3GcntNopqTqgU-ec4epS4owO98LtRvTith0yEdvThguJpSblCinEb6szs6rUzEKJQcb7klotEqe7v2PpmNpDBXl5IiDxlZN7ghtYLt24sb0FsyeAEMKHcUysEASy2kojUmTgoQ1hwjOT7TKQpSaPvM7pzXhuIyf4wI_R7wqrJ2hfwXKX3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: اگر به بمباران ایران ادامه می دادیم، کشتی‌ها دیگر نمی‌توانستند تردد کنند
🔹
ذخایر نفت ما هم حدود ۴ هفته دیگر تمام می‌شد. ذخایر جهان واقعاً تمام می‌شد.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/660710" target="_blank">📅 09:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660709">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2666505efe.mp4?token=BPpA4YyLSg-oMY3F8zNhYxoGjuhgIC-Kk8jPWVtNv5MRrHUOo79FwN2l6MnZOk5FlAEmpk7BC7ztBc4XK6Jq5naIJHO95RR11hb780f4Ai2AWPLhTWjiD8UNU-GvK1DQaU65872UAbomaA5LIx_WRdcyskxtfxwTKlwrIyrulu-pI_NzdY5hqm_wWcENqMo023oRu8UyYzolpWruFazrjELCRJuMfIfL7JXHXWHEkepMCvL6Qdx2Sy-rul66OW638QWVxn856csB44Yeo_v6fM-VpYRAPR8RBDMt9caOq3DUdMUUO2_kqALt-PscgEo11jrb8oQkmoF2t17q33Z7_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2666505efe.mp4?token=BPpA4YyLSg-oMY3F8zNhYxoGjuhgIC-Kk8jPWVtNv5MRrHUOo79FwN2l6MnZOk5FlAEmpk7BC7ztBc4XK6Jq5naIJHO95RR11hb780f4Ai2AWPLhTWjiD8UNU-GvK1DQaU65872UAbomaA5LIx_WRdcyskxtfxwTKlwrIyrulu-pI_NzdY5hqm_wWcENqMo023oRu8UyYzolpWruFazrjELCRJuMfIfL7JXHXWHEkepMCvL6Qdx2Sy-rul66OW638QWVxn856csB44Yeo_v6fM-VpYRAPR8RBDMt9caOq3DUdMUUO2_kqALt-PscgEo11jrb8oQkmoF2t17q33Z7_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوشحالی کیروش از پیروزی غنا در اولین مسابقه خود در جام‌جهانی
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/660709" target="_blank">📅 09:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660708">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9508847445.mp4?token=dLS0OnyWzPDgvpmBURzojKiunRyxCEqWQXNQiQK5A8uGXFJhbjoANgAwiUaK7a8VnGGfytfXqzlDSrS5Hagx-rNZcMg7VCGsE8gAJ_varELnbRe8cXW7pL-BHaMDLYyVdPw_Xyb_C2nBlULRYhLtJEjFEDophMejSvPRPpeFL41nhhbqlzr6DxPvh7gbcBYbgBMNUU-dLnWBUIboLCf8iTRKsjExOvBo3u-on-vuid-AzrfQXLAVby83PFb73tP59Enx5Q4c6bPL4vRxaE6BEf2ExQBKF3s5evZPXDw6ZtSJ_4lTSEYK1qUL3ezxyc9JM4AV-IixXeEme4CU6jc6EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9508847445.mp4?token=dLS0OnyWzPDgvpmBURzojKiunRyxCEqWQXNQiQK5A8uGXFJhbjoANgAwiUaK7a8VnGGfytfXqzlDSrS5Hagx-rNZcMg7VCGsE8gAJ_varELnbRe8cXW7pL-BHaMDLYyVdPw_Xyb_C2nBlULRYhLtJEjFEDophMejSvPRPpeFL41nhhbqlzr6DxPvh7gbcBYbgBMNUU-dLnWBUIboLCf8iTRKsjExOvBo3u-on-vuid-AzrfQXLAVby83PFb73tP59Enx5Q4c6bPL4vRxaE6BEf2ExQBKF3s5evZPXDw6ZtSJ_4lTSEYK1qUL3ezxyc9JM4AV-IixXeEme4CU6jc6EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه امضای تفاهم‌نامه ایران توسط ترامپ
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/660708" target="_blank">📅 09:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660707">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
کشف ۶ هزار میلیاردی مواد احتکار شده لاستیک‌سازی
پلیس چهارمحال‌وبختیاری:
🔹
بیش از ۱۴ هزار و ۵۰۰ تن مواد اولیۀ کارخانجات تولیدی به‌ویژه صنعت لاستیک‌سازی، با ارزش ۶ هزار میلیارد تومان کشف و متهم برای سیر مراحل قانونی به دستگاه قضائی معرفی شد.
#اخبار_چهار_محال_و_بختیاری
در فضای مجازی
👇
@akhbarchaharmahalvabakhtiari</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/660707" target="_blank">📅 08:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660706">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
نتانیاهو: اسرائیل به بند لبنان در توافق ایران و آمریکا پایبند نیست
مشاور نخست وزیر رژیم صهیونیستی:
🔹
ما خود را ملزم به بخش مربوط به لبنان در یادداشت تفاهم ایران و آمریکا نمی‌دانیم و تا زمان خلع سلاح حزب الله از جنوب لبنان عقب‌نشینی نخواهیم کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/660706" target="_blank">📅 08:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660705">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
شهریه کودکستان‌ها چه زمانی اعلام می‌شود؟
رئیس سازمان تعلیم‌ و تربیت کودک:
🔹
فرایند تعیین شهریه از ۱۵ خرداد آغاز شده است و تا پیش از مهرماه شهریه کودکستان‌ها و مراکز تعیین خواهد شد و اعلام درصد افزایش شهریه‌ها مورد تأیید نیست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/660705" target="_blank">📅 08:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660704">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/875b08b05b.mp4?token=jhFIvc2HsJiPjcaxFa1kmpysC0pRHwCQ41WR1WL-hIFo5e8U-ONH_zrpFftx2IOt-PzHldnIRJXw_3_24qx5QRhZzxQEWEIUd8k-KK7SSyt4xCSjm_qlP90pg_UsCxfNiGeB2JLN28lSToBHTsJclsgKU3HXURJnKu3jyTx7L7mx3Tzt7rv7JQIQyA33it7GHT0D2i-0L9F47sRh8aV3CMUZy2kykmzdaJ-EkolW0H9dV0iodhh_qZEa5SDhHLy4-JSspOSMy9_skGyR48T7TkDr8Fo1PW-FfZQmqy64QVJqkkxEsq3F-kfhMwM2pB4OFuzrzRiTC3RM7xZ8eAQt-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/875b08b05b.mp4?token=jhFIvc2HsJiPjcaxFa1kmpysC0pRHwCQ41WR1WL-hIFo5e8U-ONH_zrpFftx2IOt-PzHldnIRJXw_3_24qx5QRhZzxQEWEIUd8k-KK7SSyt4xCSjm_qlP90pg_UsCxfNiGeB2JLN28lSToBHTsJclsgKU3HXURJnKu3jyTx7L7mx3Tzt7rv7JQIQyA33it7GHT0D2i-0L9F47sRh8aV3CMUZy2kykmzdaJ-EkolW0H9dV0iodhh_qZEa5SDhHLy4-JSspOSMy9_skGyR48T7TkDr8Fo1PW-FfZQmqy64QVJqkkxEsq3F-kfhMwM2pB4OFuzrzRiTC3RM7xZ8eAQt-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عبدالباری عطوان، تحلیلگر مشهور جهان عرب: سرانجام آمریکا تسلیم قدرت ایران شد!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/660704" target="_blank">📅 08:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660703">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
وام‌گرفتن گران‌تر می‌شود
🔹
بانک مرکزی قصد دارد نرخ سود سپرده و نرخ سود تسهیلات را در ۲ مرحله و در هر مرحله ۵ درصد افزایش دهد.
🔹
با این حال این امکان نیز وجود دارد به یکباره ۱۰ درصد افزایش را اعمال کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/660703" target="_blank">📅 08:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660702">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
«میر تاج الدینی»، معاون امور مراسم و استان‌های شورای هماهنگی تبلیغات اسلامی: آیین جهانی شیرخوارگان حسینی فردا همزمان در ایران و ۴۵ کشور برگزار خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/660702" target="_blank">📅 08:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660701">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
فردا؛ آزمون سمپاد و نمونه دولتی برگزار می‌شود
🔹
آزمون‌های ورودی پایۀ هفتم مدارس (سمپاد) و پایۀ دهم مدارس نمونه دولتی و تکمیل ظرفیت مدارس (سمپاد) دورۀ دوم متوسطه سال ۱۴۰۵ فردا برگزار می‌شود.
🔹
این آزمون صبح فردا جمعه در ۴۷۹ حوزه اصلی آموزش و پرورش و ۲۸۳۷ حوزه فرعی مدارس در ۴۱۸ شهرستان در سراسر کشور برگزار می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/660701" target="_blank">📅 08:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660700">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
قدردانی نخست‌وزیر پاکستان از رهبری ایران
🔹
«شهباز شریف» نخست‌وزیر پاکستان روز پنج‌شنبه با اشاره به امضای تفاهم‌نامه ایران و آمریکا با میانجی‌گری اسلام‌آباد، از آیت‌الله سید مجتبی خامنه‌ای، رهبر انقلاب اسلامی و همچنین مسعود پزشکیان، رئیس‌جمهور برای انتخاب مسیر صلح تشکر و قدردانی کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/660700" target="_blank">📅 08:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660699">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/204da3dd8c.mp4?token=JSSIkF7bP1DG7cdEZA9t_BXavZ0VapZFM6pfbjori-DqJbiDOTfEzDumJCFklbjDqRrym3bZZ_QfCEG6qokjN_GMJF-f-2KBMebvYPMAU3HXv-sdol80oH1hO41nPLuEY1h3sqIrqLJdLNZuVnYyA-fnT1vHIshO4ozl2iC_nInx5EClDPoGHHzMU8I5YvBAazZqrjBvh9bIdE2C3R55u6ziBYxUBjDiS2y0oOTYj1bpzsoqa43arPOTnsqrH9-LSHleghLTcJirbpQ92n8ikcTdkgBhmqlFtabrseljg3kZV1Vnb0077xBGauEsxWOuqbq9Vqm6cIslPQt-wOfYQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/204da3dd8c.mp4?token=JSSIkF7bP1DG7cdEZA9t_BXavZ0VapZFM6pfbjori-DqJbiDOTfEzDumJCFklbjDqRrym3bZZ_QfCEG6qokjN_GMJF-f-2KBMebvYPMAU3HXv-sdol80oH1hO41nPLuEY1h3sqIrqLJdLNZuVnYyA-fnT1vHIshO4ozl2iC_nInx5EClDPoGHHzMU8I5YvBAazZqrjBvh9bIdE2C3R55u6ziBYxUBjDiS2y0oOTYj1bpzsoqa43arPOTnsqrH9-LSHleghLTcJirbpQ92n8ikcTdkgBhmqlFtabrseljg3kZV1Vnb0077xBGauEsxWOuqbq9Vqm6cIslPQt-wOfYQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرکات مناسب گودی کمر  #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/660699" target="_blank">📅 08:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660698">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3009c87001.mp4?token=lKfzEqE4hKGVzemUs4IfQOkGbZv3S-1k2TdyjxvpNRg0cWOrGN5r1yIb1VOwmR8ZQ_6dSfOzPoy1mhnbutwOXywTMeJR0QcyfhBeeHWW22FsN1JkIjU5B2Krg3FGLIrt4qN5VFERJ5e8usaTbRRjfJuyO8hqdad_DwzYKEgIxIGSZWtbLskmKN_OgBGI0i6ESM0xA-X2_T1nUxea0RmXFFHCpUn9m-9_CRzMkF3zq56HkWsupjK4aNuYbgQA6r1tCke-snWtXSp5NwhQLDhRSc-2GzpaN4ChXIW-1oEpyvKWVxEdCi1-mwoe13BMf0MuZ4DjLy1RH6C4VGGMj6L-wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3009c87001.mp4?token=lKfzEqE4hKGVzemUs4IfQOkGbZv3S-1k2TdyjxvpNRg0cWOrGN5r1yIb1VOwmR8ZQ_6dSfOzPoy1mhnbutwOXywTMeJR0QcyfhBeeHWW22FsN1JkIjU5B2Krg3FGLIrt4qN5VFERJ5e8usaTbRRjfJuyO8hqdad_DwzYKEgIxIGSZWtbLskmKN_OgBGI0i6ESM0xA-X2_T1nUxea0RmXFFHCpUn9m-9_CRzMkF3zq56HkWsupjK4aNuYbgQA6r1tCke-snWtXSp5NwhQLDhRSc-2GzpaN4ChXIW-1oEpyvKWVxEdCi1-mwoe13BMf0MuZ4DjLy1RH6C4VGGMj6L-wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برخورد شدید بازیکن ازبکستانی به فیلمبردار مسابقات، در بازی با کلمبیا
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/660698" target="_blank">📅 07:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660697">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
مکرون: امضای تفاهم‌نامه راه را برای صلح پایدار هموار کرد.
🔹
هلاکت یک نظامی صهیونیست و زخمی شدن ۷ نظامی دیگر در لبنان
🔹
سازمان ملل، حمله اوکراین به اتوبوس حامل کودکان در منطقه بریانسک را محکوم کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/660697" target="_blank">📅 07:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660696">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
ستاد مرکزی اربعین: ثبت‌نام زائران اربعین از ۹ تیر آغاز می‌شود و نام‌نویسی در سامانه سماح برای همه متقاضیان الزامی است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/660696" target="_blank">📅 07:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660695">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
نفت خام برنت ۷۸ دلار شد
🔹
پس از اعلام امضای یادداشت تفاهم بین تهران و واشنگتن، قیمت نفت خام برنت به ۷۸ دلار و ۶۶ سنت در هر بشکه کاهش یافت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/660695" target="_blank">📅 07:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660694">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Siuan1bXcD3BbXM3mkPfyNc0kNJWzjWfzcEZ7YV5vnb5Ksj33iPv_Vz0YTsfJBwbsQmLVTr5eaRkIlRI1SIMMGQ-16ljS07Mwl7p_0mHRVMZ50AB3-5JWby_Va5NMJnJQ_372IkD8ubIyPgs8Fa_2iG2Enp5DUZ8Z7TjpMtt6M8XdQVZbezptbzShGduDnEbS0F-5_PzFj2T2HAJ6iro4vCEbbWk_p8uGVXUpQmnmxfyALrao2HTYzlf_gBJ6s7BASoCKUnLNB6n5FgmpXADG2U1KdTBhCmU9SNVQ8zaIhD2B0pvU857uKuTVopXT4vgy9_E4SweMZ2iI4l8U9LzxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جدول رسمی تمام گروه‌های جام جهانی بعد از پایان دور اول رقابت‌‌ها
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/660694" target="_blank">📅 07:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660693">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
هشدار روزنامه کیهان: بعضی سخنران‌های تجمعات شبانه، در پوشش انقلابیگری تفرقه افکنی می‌کنند
روزنامه کیهان:
🔹
متاسفانه در این شب‌ها، هر چند اندک برخی سخنرانان هیجانی در پوشش انقلابی‌گری و با نادیده گرفتن اوامر رهبر انقلاب در حفظ وحدت و انسجام ملی، اقدام به پراکندن بذر انشقاق و تفرقه در میان مردم می‌کنند.
🔹
لازم است نهادهای برگزارکننده در راستای امر رهبری بر این تریبون‌ها نظارت داشته باشند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/660693" target="_blank">📅 07:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660692">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf019f3a86.mp4?token=D04PQ9fSSFoZ2nLzj43LRyJL-ALh-SsYNxm5kXPFo7rantAjXvIWPMVCawiir70XH6_gvQxXrY3aWsvN9I4V0ynHtsj6nKa0pRGeLP6uvt78TRa6k8nXceCNE56pT2k30teKJ0lra6CXiOqZ9e4h-jHel9QCBgiC09iIjbbfnfhE838bPThvKdqthisF_1biDz3vpy_uSh1W-l-Mq6Sp2jEVx9ZKyvjMLbV335VPPZ-ilae4A8m4rAB96U5JS9sqj4epnH7Q5WhLkBy2kNhH7zdEsa31BaOYJ7ILGRNKxb4RDMAfiLBfN8IftCw_6F0v4BG5Xa_MQhmEgttTLcOW3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf019f3a86.mp4?token=D04PQ9fSSFoZ2nLzj43LRyJL-ALh-SsYNxm5kXPFo7rantAjXvIWPMVCawiir70XH6_gvQxXrY3aWsvN9I4V0ynHtsj6nKa0pRGeLP6uvt78TRa6k8nXceCNE56pT2k30teKJ0lra6CXiOqZ9e4h-jHel9QCBgiC09iIjbbfnfhE838bPThvKdqthisF_1biDz3vpy_uSh1W-l-Mq6Sp2jEVx9ZKyvjMLbV335VPPZ-ilae4A8m4rAB96U5JS9sqj4epnH7Q5WhLkBy2kNhH7zdEsa31BaOYJ7ILGRNKxb4RDMAfiLBfN8IftCw_6F0v4BG5Xa_MQhmEgttTLcOW3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: یادداشت تفاهم با ایران، امضا شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/660692" target="_blank">📅 07:41 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660691">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
کاخ سفید: مراسم امضای تفاهم‌نامه در ژنو برگزار نمی‌شود
شبکه «فاکس نیوز:
🔹
«امضای رسمی [تفاهم‌نامه] که قرار بود در ژنو انجام شود، پس از امضای آن [توسط ترامپ در] ورسای لغو شد».
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/660691" target="_blank">📅 07:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660690">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
ضرب‌الاجل دولت به قایق‌ها برای نصب ردیاب
🔹
سازمان شیلات به صیادان یک ماه مهلت داد تا روی قایق خود ردیاب نصب کنند، در غیر این صورت سوخت گران‌تر دریافت می‌کنند.
🔹
این اقدام برای سنجش واقعی پیمایش و تلاش قایق‌های صیادی، انجام می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/660690" target="_blank">📅 07:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660685">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/toU1WWUelVztSLG00uakHDsNw5hXscRe2f_0rEgDavC48wUS5UObJl78dgGEkcG6YfOFe_TP_xBpyHkXCeAK2qJXHGBoLB9eKy9wi7cQQhulrAU33b-ILZZ4-OJxRFasN2ApAWLo6hGOie5eGjXvSmGoP_xjAnj8tI6-GWQYKZzXURHkLigM64aHYyl0iVIk68oSySxcSbyg5OvJC86OW-aqVyhu3TNVR0df3bySE6tzBD2PQD7NLorFRawDXjGkMZ3RUGY_s1nBbDrKizNwqHg5hPW4AMscnGbvnct6Odx2JVTwFplb-x18UMTQyCE5wEpLuXVdlHTJlc_RtCj1sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cxcGH20HsGbpsuanXz4HfZ2f31MoUV7ayDbeUshXgpBS_Gpma9DhSNpW-9i66Z5HUGLLmc6PDf475eDgyqOeVY1fb_Iu9UJEzmx5V2UPsAzxdq94gGWjjPWHaet9wgdYi0V3t-5CrRRu8bYPDyvC84ALU5WD3S9S4SmNw5gu5kb87Eik8Nod5A9xHuqRlVs6csYlaBjnMpQ496M1_7Sq8Z4vZx6RS13fJ9er1MyvJVYVvKkG-Ocd454mebYHCPHVfg5kqInJE342joumBrQJ4Kei-SudIaROI4Yt8Dtc4MjiRGubyb9Yfdh1ZiHiJBdj1hEGvUNtNkiJ-t6WKBxA8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TEhvykU-c5Iri59Wevji1Oa3DtoeGAvl5ZQwyt9h4_GCUK7oJT_QdUWZkDcRkKDxKeBAANu4LrCzEqDGDsEE4bQ3pT5jYpCD79D-sTstZBWFSxxzxAAY-atsm0P-tSOVWUBJA8nxa2kgrAWbe93KrAJ3gb2fpsf4DcOpXZxrAqV8_loSYFYovpyh1sRTXfeVZu6gE6wqycfKpcjASFTt6dvn2AK6OM30SdZSMu5xwOhNGA59hHAA7n7XSNWoZGYuEbwWcl-HCX-EbOd4h3wstdDhqOnhH81xnUocwBrQ1GODLorLyII0irTqhEU2Y7d76PPbWlPcfgtdPb0riMezFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hkAzF4NpuNXWNDnX3UWuJgCm_b8BpOthWOEQ59H2KunATAxh1z9k0z_Cs5MPdFRAwKSMnuyrWQtDP1mnRA3Lm_CerGQp1hgv_GAyoMJa55qJ-HIneZaWlnxd4DeuLj_-0oHEsRySB1GzIKYqfP0s42pzNIWK0jONPeTh0GEFxSGjfzufdgtud2vq0vSBzLgpEgUqwwAIpsYKrq4pniq4ycYiOm8GuLKo1BqHR1hulz-Pj_BKtKGJz7OHE4fyhomOFARGk2mq52A_49Vqz-RgGsAo2585XCd0heOVwkwHugtLRCd68vD8ykjtmeKWmnp5D9dRu4dz3RGAQzil-FwGFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oHIeSeQlXiqvkRFiqzdC3hbFZurmsB4E_LNjmedf_gfA7UyTVgX8HXpOd86pP3CF0mxLC3PQp5oyOyFevkK2gJ4A8Wg9EXVcGwU4VJJONFOLC_GftRRGPUDBg5H2_ZTHlCUvPUiM0b1o9I8k6r9eJjtHIHUiHsKMKzoaocZP1AMOlCkA_9r0YWhd6k5WMNK3RCf10CfUe2u5Kk6XjDQfgKaFrf-SbySJl8e-rcBqYmZtnxDIOPz3bPnA6BWIcUb4cxgZL2TLYs6_y4q-oWKVQ3fZSfFUsoMMkSbWbrkRlaY5k5W6dMZFbxJCp6ZXYzeG9Bmr01KXHT3iGpPkZ7GCRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بقایی: همین الان که در حال صحبت هستیم متن توافق رسما به امضا رئیس جمهور های دو طرف رسیده است
🔹
قرار بود که بامداد روز ۲۸ خرداد ماه رئیس جمهور دو کشور این متن و توافق رو امضا کنند. @AkhbareFori</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/660685" target="_blank">📅 07:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660683">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14db2b6199.mp4?token=u2F7RYNSVdXkeqHXKS2mE3XSFlHuacasnUVjvWDR2AcLdstMgbcy6TpXuJrb6ZL2tilZC36rBBE6CxkTQNfJOuv77Y1cMjLu5DnT0H1TrFnm_9dIcKACuBye75asIfWZBmfxSZbZ7YbqSEpXXJyQeP5ohLi2lv1PZSnYq2RRWwG-6C9Y_Hp4l7zDpAJmStx794sh2EHxc90h1g-X63JsA_EJOopfDsjJuT59OF4ZES1MKJu9viozQZsG-FpmX3ZMENr5fRt5kTwcidkd5mlQrYjzapmE5g1LY7Dz4LzJP3iz058dlrJ2xbMLJ9aPv1S9JcBD8r_NG2Et4Pcr-1-7-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14db2b6199.mp4?token=u2F7RYNSVdXkeqHXKS2mE3XSFlHuacasnUVjvWDR2AcLdstMgbcy6TpXuJrb6ZL2tilZC36rBBE6CxkTQNfJOuv77Y1cMjLu5DnT0H1TrFnm_9dIcKACuBye75asIfWZBmfxSZbZ7YbqSEpXXJyQeP5ohLi2lv1PZSnYq2RRWwG-6C9Y_Hp4l7zDpAJmStx794sh2EHxc90h1g-X63JsA_EJOopfDsjJuT59OF4ZES1MKJu9viozQZsG-FpmX3ZMENr5fRt5kTwcidkd5mlQrYjzapmE5g1LY7Dz4LzJP3iz058dlrJ2xbMLJ9aPv1S9JcBD8r_NG2Et4Pcr-1-7-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ در پاریس تفاهم‌نامه ایران را امضا کرد  آکسیوس به نقل از مقام‌های آمریکایی نوشت:
🔹
ترامپ شخصاً نسخه‌ای از این توافق را در جریان ضیافت شام با رئیس جمهور فرانسه در کاخ ورسای امضا کرد. عکسی از توافق امضا شده برای ایرانی‌ها و کشورهای میانجی ارسال شد»./فارس…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/660683" target="_blank">📅 07:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660682">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">پادکست کافئین | فصل‌دو،قسمت‌سوم</div>
  <div class="tg-doc-extra">ابونصر فارابی</div>
</div>
<a href="https://t.me/akhbarefori/660682" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
پادکست
#کافئین
🎧
▶️
ابونصر فارابی (معمارِ سیستم‌ها)
🗓
در این قسمت، بزرگترین کلاس درس تاریخ را برای «خروج از تفکر جزیره‌ای»، «طراحی زیرساختِ روابط انسانی» و «آرمان‌گراییِ عمل‌گرایانه در محیط‌های آشفته» مرور کرده‌ایم. تا زمانی که نگاه سیستمیک نداشته باشید، تغییراتِ شما فقط مثل دستمال کشیدن روی شیشه‌ی کثیفه!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/660682" target="_blank">📅 07:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660681">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16162bd5bf.mp4?token=d1iLlDe9ZFT8aOjXBqmcWLBv63ugUtwhIGJjj5NtdV-5OiZQj8syraWnC6LWQc08BTVO8fhrmbHaanEJsf4jTayOQdJOkSdKVV3_kCU57OrtM7ljwtT3y1Rz9l_wXESNabLih2TPbpjaHOKW88zpD3ZTh8-eIIVS4bfo66jw4Exv5Z5tPARGY60A-YO5ABknzP-b-v33rIeX5dK7P1Jwi9Z8I49UOYkDa4BabihPg563qMC2LMZX8BMzM1ol_dyc8vLQl9bouvLcfPbmkcA3u5bebgC2aYogNm6OSo2mRhD5ZSMiUhkmo9Ih_NntORAE7Qeyf8NZVZpDWAng3QTKBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16162bd5bf.mp4?token=d1iLlDe9ZFT8aOjXBqmcWLBv63ugUtwhIGJjj5NtdV-5OiZQj8syraWnC6LWQc08BTVO8fhrmbHaanEJsf4jTayOQdJOkSdKVV3_kCU57OrtM7ljwtT3y1Rz9l_wXESNabLih2TPbpjaHOKW88zpD3ZTh8-eIIVS4bfo66jw4Exv5Z5tPARGY60A-YO5ABknzP-b-v33rIeX5dK7P1Jwi9Z8I49UOYkDa4BabihPg563qMC2LMZX8BMzM1ol_dyc8vLQl9bouvLcfPbmkcA3u5bebgC2aYogNm6OSo2mRhD5ZSMiUhkmo9Ih_NntORAE7Qeyf8NZVZpDWAng3QTKBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ابونصر فارابی و «تفکر سیستماتیک و فرار از آنارشی»
#پادکست_کافئین
| فصل‌دو،قسمت‌سوم
☕️
متفکری که هزار و صد سال پیش، در دل آشوبِ خاورمیانه، ایستاد و چارت سازمانیِ یک تمدن توسعه‌یافته را کشید و به تاریخ نشان داد: «اگر نابغه‌ترین مهره‌ها را هم داشته باشی، بدونِ تفکر سیستماتیک، خروجیِ سازمانت چیزی جز یک آشفتگیِ مطلق نیست!»
هر روز صبح با یک شات غلیظ از تاریخ، آمادهٔ شروع روزتان باشید!
از اینجا ببینید و بشنوید
👇
https://youtu.be/C6Est5_k60c?si=3R0oBCMYwrbR7QfX
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/660681" target="_blank">📅 07:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660680">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t7lJy5dq8vj8mg5ypHDLCqfJwjOQK8RpuKqAYkVTMqnrYbl1h3FNsDPNCwHm3dmQuTYdZUgPvC8tgqOEKHmhj3dxRelTmTDQRzIhAOi7AtMFizMoiEH-LjRqI_7PeUxvPtItkKzrkOtxpBSu5gHqevxYyNwwT3YA-bxQE2s8tZe_TnGIswRNNi46OflZTSFMWCQ4k-VFKFT1KKFiwEHunJ0DGjslzPgpnOAW9SqKyKOld8dNsINTFJ7F9sxT4nfvUxmogicODbh6rSYrNybnPXxn4xnwX1GsILyszh8GzumLH-0Zq_XfaQBSgmGkFBmL39pkGWbyVlPvQwdQrJ9crQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز پنج‌شنبه
۲۸ خرداد ماه
۳ محرم ۱۴۴۷
۱۸ ژوئن ۲۰۲۶
پنج‌شنبه‌ها
#دعای_کمیل
بخوانیم
⬅️
متن و صوت دعای کمیل
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/660680" target="_blank">📅 07:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660679">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8pfN5WPERRgI3dxXzY0yK9ZfNzCwTUdBk60nDXpDGp7XKyAZ6tIGTdz-Q6dNtIJHnMBcny6uNGAB-Y0vJ5WBgjVifgtgpZUNcpNZJ7mLpqBAHtkqbqjLBx-nMREDGRZfxOXUYx-L9qUwaezcueQBn9A2m8VAamKtwHNJDbMa-7ydKUjiFJDas2WWF3X3OOwhFDZaDS2lkO-W407j5PN3HMeQD860UTgaUyA7ufjAi79U2PYL6lbKO2PxZKulSqQP6nYlyxmbO2uN6XcyzDVH1IISMPL8zOPTK6QfGhZPevIdQBCGg-P42mnqX9r_0z9AMOv21WnouNYBpcqgaqB_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/akhbarefori/660679" target="_blank">📅 02:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660677">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
بقائی دربارهٔ مرحلهٔ پیش‌روی تیم مذاکره‌کننده ایرانی: کار ما به عنوان دیپلمات‌، قطعاً از کار مدافعان وطن پای لانچرها و پشت سنگرها ساده‌تر نیست. شاید دشوارتر هم باشد، چون باید چشم در چشم دشمنانی بدوزیم که می‌دانیم مرتکب چه جنایاتی شدند و برای احقاق حق مردم و تثبیت دستاوردها با آنان مذاکره کنیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/660677" target="_blank">📅 01:56 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660676">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
بقائی: مردم ما، بغضشان از غم فقدان عزیزانمان -از دانش‌آموزان تا رهبر شهیدمان- را، تبدیل به یک «خشم حماسی» برای دفاع از ایران کردند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/660676" target="_blank">📅 01:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660675">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
بقائی: ابرقدرت بودن ایران یک شعار نیست؛ ما دو قدرت اتمی را شکست دادیم
سخنگوی وزارت خارجه:
🔹
ایران ۲ قدرت اتمی که برخی کشورهای دیگر هم همراهی‌شان می‌کردند را شکست داد. ما شعار نمی‌دهیم بلکه واقعاً ابرقدرت هستیم.
🔹
جمهوری اسلامی ایران پوست ایران است و دشمنان می‌خواستند پوست ایران را بکنند. هر انسان وطن‌دوستی فهمید که این تفکیک (میان ایران و جمهوری اسلامی) تفکیک موهومی است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/660675" target="_blank">📅 01:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660674">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
بقائی درباره تفاوت ایران امروز با ۶۰ روز پیش رو: لن یضروکم الی اذی و ان یقاتلوکم یولوکم الادبار ثم لا ینصرون
آن‌ها جز آزارهایی اندک به شما نمی‌توانند رساند واگر با شما پیکار کنند با عقب‌گردی، از شما روی برمی‌تابند و شکست می‌خورند، سپس یاری نخواهند شد
این وعده خداوند است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/660674" target="_blank">📅 01:49 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660673">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
بقائی: ما شعار نمی‌دهیم
🔹
ما با دو قدرت اتمی و بسیاری از دولت‌هایی که حمایتشان می‌کردند و هدفشان فروپاشی ایران بود، جنگیدیم و یک وجب از خاکمان را ندادیم. هر انسان وطن‌دوستی فهمید که تفکیک جمهوری اسلامی و ایران از یکدیگر موهوم است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/660673" target="_blank">📅 01:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660672">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
بقائی: احساس اقتداری که امروز تک تک ایرانیان دارند، بی‌سابقه است. جنگی که علیه ما به راه انداختند، ما را مقتدرتر کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/660672" target="_blank">📅 01:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660671">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
بقائی: همه امید ما این است که همانطور که مردم در صدوده روز نشان دادند، در میدان ادامه دهند و به مسئولان خودشان اعتماد کنند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/660671" target="_blank">📅 01:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660670">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
بقایی: تازه ابتدای کار هستیم، مدافعین وطن در عرصه دیپلماسی به اندازه مدافعین وطن در عرصه نظامی نیازمند حمایت هستند
🔹
کار ما تمام نشده تازه در ابتدای کار هستیم، مدافعین وطن در عرصه دیپلماسی به اندازه مدافعین وطن در عرصه نظامی نیازمند حمایت و انگیزه بخشی از جانب مردم هستند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/660670" target="_blank">📅 01:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660669">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
مذاکرات جمعه ایران و آمریکا در سوئیس الان قطعی نیست
بقایی، سخنگوی وزارت خارجه:
🔹
جلسه جمعه تا چند ساعت قبل قطعی بود ولی وقتی قرار شد روسای جمهور دو طرف (ایران و آمریکا) تفاهمنامه را امضا کنند، قرار شد درباره جلسه جمعه فعلاً تامل شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/660669" target="_blank">📅 01:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660668">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
بقائی، با اشاره به تجربهٔ برجام، دربارهٔ بند ۱۴ توافق اینطور توضیح داد: ما برای پذیرفته شده این تفاهم‌نامه از سوی بازیگران بین‌المللی، به یک قاب حقوقی نیاز داریم و آن، «قطعنامه شورای امنیت سازمان ملل» است
🔹
اما در عین حال، می‌دانیم که آمریکا به تعهدات بین‌المللی خود پایبند نیست. با این وجود، با استفاده از همان سازوکار خیلی از کشورها را مورد تهاجم و تحریم قرار داده.
ضمانت اجرای این تفاهم، قدرت ماست؛ اهرم‌هایی است که ملت ایران در این مدت تولید کرده
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/660668" target="_blank">📅 01:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660667">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
بقائی: ضمانت اجرای این تفاهم قدرت ماست، اهرم‌هایی که ملت ایران در این مدت تولید کرده
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/660667" target="_blank">📅 01:41 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660666">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8KdIPQfg2ehomozqJHnvZ9wT941VUttoLppMEdxrx8cJX6rhtXhITRSxocRjKVVWpqO1SpsA0rx88sBwMhR00vSofGFquS6_1yMcmLP-D5-_OPPMDBeVdW2wju35kJB0Bt0DeTG3z55iBMUMW6Bc50C-zMoC71nZhwfWDWsAuipw4wvGetGH9UF_eISI5fs15Ha4ja5CYXlsU5eQmhjGghMFpX52JZ0L-tiGTI-FaTriSNb_pgLXe8jXxeXj2X5n6rRSGKcodkHDqPm7ojz5iEXJuXtXOBE-SaweqnV3WYgOZqpHBPRgd-UPk6si08_VOLExive167s4CaO9XHXrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اینفلوئنسر آمریکایی؛ آنچه ایران به دست آورد
🔹
۳۰۰ میلیارد دلار
🔹
برداشته شدن تحریم‌ها
🔹
کنترل تنگه هرمز
🔹
حفظ برنامه موشکی
🔹
عدم تخریب برنامه هسته‌ای
🔹
آنچه ایالات متحده به دست آورد:
🔹
افزایش قیمت بنزین
🔹
میلیاردها دلار هزینه
🔹
عدم دستیابی به اهداف اصلی
🔹
آمریکایی‌های کشته‌شده
🔹
ما فریب خوردیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/660666" target="_blank">📅 01:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660665">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
اگر تعرضات اسرائیل در لبنان ادامه یابد، نقض تعهدات آمریکا محسوب می‌شود
بقایی، سخنگوی وزارت خارجه:
🔹
اگر تعرضات رژیم صهیونیستی به لبنان ادامه یابد، نقض تعهدات طرف مقابل در تفاهمنامه خواهد بود
🔹
ما آمریکا و رژیم صهیونیستی را از هم جدا نمی‌کنیم اما در شیوه‌ها و روش‌ها اختلا‌ف‌نظرهایشان کاملاً مشهود است.
🔹
رژیم صهیونیستی نمی‌خواهد کوچکترین فرصتی به هر روند دیپلماتیکی بدهد. اما این مسئولیت آمریکاست که رژیم صهیونیستی را وادار به احترام به تعهدات آمریکا به ایران در این سند کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/660665" target="_blank">📅 01:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660664">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
بقائی: بند ۱۳ مشخص کرده که شروع مذاکرات درباره توافق نهایی زمانی انجام خواهد شد که مطمئن شویم اجرای بندهای ۱، ۴، ۱۰ و ۱۱ شروع شده و تداوم پیدا کرده
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/660664" target="_blank">📅 01:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660663">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
بقائی درباره بند ۱۳ یادداشت تفاهم: ما فقط در این بازه ۶۰ روزه راجع به بحث هسته‌ای و رفع تحریم‌ها و سازوکار اجرای بقیه بندها صحبت‌ خواهیم کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/660663" target="_blank">📅 01:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660662">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpkgmew9w7ny5PtBVN65r4dIl569bgGAkPXxpIbDhbrOu6cn83PIupyzacTifq1AUanPwNMCy99p6Tc3I7kd2Lnpzs312RYGYxpuVTfkB67FghBUISlQlVmjL5deQ_z8VEY-WsPgVpC5YE8WlAJtcDRewqPRhU5EzWzEA0Vz6wxauS97NBIJ-IgAKMlyWurhc9v83J6iVRdHgFqJOh0kSzNkC_01ux3uVjp6GOvo8IrhA1a7pvkCVrsq1fY4Nm9WNYNfuDO5I_fmxZ7ZT3yUXldo-SfL5gLKl5uOpYftBvJttGCRRhELRXe8BIlGPWIaCa571R7XlcOTxXT42x-E1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گل چهارم انگلیس به کرواسی توسط رشفورد ۸۵
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/660662" target="_blank">📅 01:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660661">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cHTxfvN8Xs7wdRbG3KqwghzYUbQpK1BZzCftomjvDW00wocqkAxCP05AS8M1vvUJep_c6qVqA5EivAWxTH4Cje0lc_c1bkRod5CPARQYAWcG2qxdpc7ga_he4aYiNpMeORdlXUs4QmiExc3ib6acjnYm8Y1c7YwQQLfsSTRAGC3uyuYxlGBFEq-NXM08X56Lunrh9HifLPUp8r0fKhbiw1zX1MPVtubxNTE4LeZzIPjTSFia8aJJEstoOBw4t-R491vgeEpZPN-5GC0KGS7Al-piCkThK2ZEMInmjLEgQiU1IwpDIIBYhktX9nIlMnWjnCciQVTBuJuOQpt7PYnnXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اوپن سورس: در تمام عمرم معامله‌ای یک‌طرفه‌تر از این ندیده‌ام. کاملاً شوکه شده‌ام
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/660661" target="_blank">📅 01:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660660">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
بقائی درباره بند ۱۱ یادداشت تفاهم: ما تجارب گران‌سنگی درباره مذاکرات با آمریکا داریم تلاش برای تعهدات متقابل است. احتمالا یک کارگروه تخصصی راجع به این موضوع خاص تشکیل شود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/660660" target="_blank">📅 01:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660659">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
بقائی درباره بند ۱۱ تفاهم: مهم این است که بتوانیم هرگاه اراده کنیم از اموال بلوکه شده استفاده کنیم، سازوکارهایش هم دیده شده، آمریکا متعهد هست همه موانع را برطرف نماید
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/660659" target="_blank">📅 01:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660658">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
بقائی: در جریان مذاکرات، همه تجارب تلخ از بدعهدی آمریکایی‌ها طی سال‌های گذشته را مد نظر داشتیم تا نتیجه بهتری حاصل شود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/660658" target="_blank">📅 01:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660657">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
همزمان با تفاهمنامه، درباره ۳ موضوع دیگر هم مذاکره شد
بقایی، سخنگوی وزارت خارجه:
🔹
فقط درباره تفاهمنامه مذاکره نکردیم؛ همزمان با متن، درباره آزادسازی دارایی های مسدود شده ایران، درباره بحث بازسازی خسارت و لغو تحریم‌های نفتی به صورت مجزا مذاکره کردیم.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/660657" target="_blank">📅 01:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660656">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
بقائی: این تعهدی است که از امروز شروع می‌شود در همین حین نظارت هم باید ادامه پیدا کند تا رسیدن به توافق نهایی
بقایی:
🔹
ما فقط روی قول طرف روی کاغذ حساب نمی‌کنیم
🔹
ما فقط درباره این متن مذاکره نکردیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/660656" target="_blank">📅 01:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660655">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
بقایی: تحریم نفتی ایران باید برداشته شود، نه روی کاغذ بلکه با همه ملزومات آن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/660655" target="_blank">📅 01:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660654">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
بقائی درباره بند ۱۰: یکی از تحریم‌های آمریکا، تحریم فروش نفت بوده که هزینه‌هایی برای ما ایجاد کرده، طرف مقابل متعهد شده همه را لغو کند نه روی کاغذ
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/660654" target="_blank">📅 01:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660653">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
بقائی: در این بازه ۶۰ روزه نباید طرف مقابل حضور نظامی خود را در منطقه تقویت کند و نقض تفاهم به حساب می‌آید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/660653" target="_blank">📅 01:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660652">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5af3d26a8.mp4?token=JyvcB66z8L2ot5MhAagQh4dbvn7kYprUbUGk3PdAZLvd6cPQXlk9NEcmG7U9Tm3hI2o47lqQfVvq-pxNx9FR443Y_TZ915CeFVPseXn1IGc_DjYy0aa78lorInTi_Egj0_rN37_DhPOXyETfc3tbf0LTnaJUuqmt3aQF7E2ZrdoiCis8n8OFHxd-Ix9mCcD28D9TrkPGoEM8ydLceJkFeSFBGiBHi6uSTby29HnfDVt-lr0CWG4D4OUEJDUnCdeyqL086kroMUJhBx-xLfnzbEpaLr3BjBln1gaq9nnAd4T4HccAY8ofWiMz-qBkXmuR2vr09m6SZUSeCfvqhKDCaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5af3d26a8.mp4?token=JyvcB66z8L2ot5MhAagQh4dbvn7kYprUbUGk3PdAZLvd6cPQXlk9NEcmG7U9Tm3hI2o47lqQfVvq-pxNx9FR443Y_TZ915CeFVPseXn1IGc_DjYy0aa78lorInTi_Egj0_rN37_DhPOXyETfc3tbf0LTnaJUuqmt3aQF7E2ZrdoiCis8n8OFHxd-Ix9mCcD28D9TrkPGoEM8ydLceJkFeSFBGiBHi6uSTby29HnfDVt-lr0CWG4D4OUEJDUnCdeyqL086kroMUJhBx-xLfnzbEpaLr3BjBln1gaq9nnAd4T4HccAY8ofWiMz-qBkXmuR2vr09m6SZUSeCfvqhKDCaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل چهارم انگلیس به کرواسی توسط رشفورد ۸۵
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/660652" target="_blank">📅 01:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660651">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
آمریکا متن تفاهم‌نامه با ایران را منتشر کرد
🔹
یک مقام ارشد کاخ سفید آمریکا متن این سند ۱۴ ماده‌ای را برای رسانه‌ها قرائت کرده است.
🔹
این سند با عنوان
«تفاهم‌نامه اسلام‌آباد میان ایالات متحده آمریکا و جمهوری اسلامی ایران»
منتشر شده است.
🔹
بررسی‌های اولیه نشان می‌دهد که متن منتشره توسط ایالات متحده با متن تفاهم‌نامه منتشر شده از سوی ایران مطابقت دارد./ایسنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/660651" target="_blank">📅 01:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660650">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
بقایی: تعداد بند های توافق ملاک نیست مهم منافع ملی کشور که در توافق گنجانده شود، برای ما دستور عمل های شورای امنیت ملی که صادر کرده بود بعد آتش بس ملاک بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/660650" target="_blank">📅 01:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660649">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
بقائی: متن تفاهم به دو زبان امضا شده؛ این اوج شفافیت ما در اطلاع‌رسانی است. اگر فقط متن انگلیسی بود دچار تفسیر سلیقه‌ای می‌شدیم. این متن کاملا منطبق بر متن انگلیسی است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/660649" target="_blank">📅 01:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660648">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
بقائی: رقیق‌سازی مواد غنی شده، موضوع جدیدی نیست و برای این مطرح شده که راه بر گزینه‌هایی که به هیچ عنوان برای ما قابل قبول نیست، بسته شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/660648" target="_blank">📅 01:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660647">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
بقائی: ما از ابتدا گفتیم مواد غنی‌شده ایران به خارج منتقل نخواهد شد؛ در صورتی که طرف مقابل دائم مطالبات زیاده‌خواهانه‌ای داشت که درنهایت به نتیجه نرسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/660647" target="_blank">📅 01:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660646">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
بقائی درباره بند ۸ تفاهم: ما تنها در بندی از موضوعات هسته‌ای که صحبت کردیم درباره رفع تحریم‌ها در بازه ۶۰ روزه بوده
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/660646" target="_blank">📅 01:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660645">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
سازمان ملل: از توافق ایران و آمریکا و بازگشت دیپلماسی استقبال می‌کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/660645" target="_blank">📅 01:17 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660644">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
بقایی، سخنگوی وزارت خارجه: بدون هرگونه مماشاتی، اجرای تعهدات طرف مقابل را رصد می‌کنیم. در صورتی تعهداتمان را انجام می‌دهیم که طرف مقابل به تعهدش عمل کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/660644" target="_blank">📅 01:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660640">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
واشنگتن امضای تفاهم‌نامه با ایران را تایید کرد
🔹
دو مقام آمریکایی بامداد پنجشنبه به وبگاه «آکسیوس» گفتند که واشنگتن و تهران، یادداشت تفاهم برای پایان جنگ را امضا کرده و اکنون اجرایی شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/660640" target="_blank">📅 01:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660639">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
بقائی درباره بند ۷ تفاهم: متن تصریح کرده همه تحریم‌های یک‌جانبه آمریکا اعم از اولیه و ثانویه برداشته شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/660639" target="_blank">📅 01:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660638">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
بقائی:  از هیچ فرصتی برای مستندسازی و پیگیری و تبیین جنایاتی که علیه ملت ایران اتفاق افتاد نخواهیم گذاشت
🔹
از هر سازوکار و نهاد و فرصت بین‌المللی برای احقاق حق استفاده خواهیم کرد. اینها خارج از این یادداشت تفاهم است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/660638" target="_blank">📅 01:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660637">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
بقائی: قاعدتا از هر سازوکاری استفاده خواهیم کرد که این تعهد صورت بگیرد برای ما منبع آن مهم نیست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/660637" target="_blank">📅 01:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660636">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
بقائی: بعضی از آسیب‌هایی که به ما زدند به عدد و رقم درنمی‌آید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/660636" target="_blank">📅 01:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660635">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
بقائی: بازسازی خسارات ناشی از جنگ برای ما فوق‌العاده مهم است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/660635" target="_blank">📅 01:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660634">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
بقائی در پاسخ به این سؤال که چرا برداشتن محاصره دریایی در متن نیامده: چون زودتر این اتفاق افتاد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/660634" target="_blank">📅 01:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660633">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
بقایی: اگر متن را مبنا قرار می‌دادیم باید رفع محاصره از امروز انجام می‌شد اما رفع محاصره زودتر انجام شد. باید در عمل شاهد این اتفاق می‌بودیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/660633" target="_blank">📅 01:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660632">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
بقایی، سخنگوی وزارت خارجه: موضوع تنگه هرمز به عهده ایران و عمان است. فقط ایران و عمان ۲ دولت ساحلی تنگه هرمز هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/660632" target="_blank">📅 01:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660630">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
بقایی: با عمان تا حدود زیادی به سازوکار مشخص درباره تنگه هرمز با حفظ حاکمیت ایران رسیده‌ایم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/660630" target="_blank">📅 01:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660629">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
بقایی: تصمیم داریم برای اطمینان از تردد ایمن کشتی‌ها تدابیری اتخاذ کنیم قاعدتا خدماتی ارائه خواهیم داد و هزینه‌اش دریافت خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/660629" target="_blank">📅 01:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660628">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
بقایی: ما برای دهه‌ها نگهبان تنگه هرمز بودیم اما سواستفاده شد و ایران طبق حقوق بین‌الملل تدابیری اتخاذ کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/660628" target="_blank">📅 01:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660627">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
موشک‌های ایران فقط برای شلیک شدن هستند نه برای مذاکره
بقایی، سخنگوی وزارت خارجه:
🔹
موشک‌های ما اصلاً دوست ندارند که کسی درباره‌شان حرف بزند.
🔹
موشک‌های ایران فقط برای شلیک شدن هستند نه برای مذاکره.
🔹
درباره توانایی دفاعی ایران در هیچ روندی و با هیچ طرفی صحبت نخواهد شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/660627" target="_blank">📅 01:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660626">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
بقایی، سخنگوی وزارت خارجه: قرار بود طی ۳۰ روز محاصره برداشته شود و متقابلاً ایران هم درباره تنگه هرمز این کار را انجام دهیم. اما بعد از تحولات مربوط به حمله رژیم صهیونیستی به ضاحیه و تهدیدات جدی که از سوی ایران انجام گرفت، مذاکرات فوری انجام گرفت و قرار شد آمریکا تعهداتش را فوری انجام دهد
🔹
در رصدی که انجام شد مشخص شد کشتی‌های ما بدون هیچ مشکلی وارد بنادر شدند و خارج شدند و این تعهد {آمریکا به رفع محاصره} شروع شد. تعهدات ما پس از امضای این سند شروع خواهد شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/660626" target="_blank">📅 01:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660625">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
متن فارسی تفاهمنامه نیز به عنوان سند رسمی به امضای ایران و آمریکا رسیده است
🔹
با پیگیری و پافشاری ایران، متن فارسی تفاهمنامه اسلام آباد میان ایران و آمریکا نیز به عنوان یک سند رسمی به امضای دو طرف آمریکا و ایران رسیده است. /تسنیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/660625" target="_blank">📅 00:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660624">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jUIS4aPCK7HlgE1womJNvZZ6MdTOcnJfgBVf58khcYxTe0kHcQWzjE4BrreSasJFprrmbkbTSl-1wAcVXeQa8xBr-KAysR2dBnWFUp3Fp21jh_VRxiQuydrJr1kFQ2ncJexbic6i2ZVT6xqW1xfqydqEZJTfLylqlbiuV8yHiTdbA9Fh0CsY-ElRvT6_C6wXa-FRs5YrnH9XsVHBl1Uv7WFM8rPHBHwKHWv3z4_NdAYm84h6LVhYqtezkGuGKcY_504eZ_fL4sIaX_aKfOp0or3CJd7nQmgPWXWqdxRCbd8bHBGCr2MYcjoNCfXUErskplhyVb0-z-ncQcCSLFMvbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واشنگتن امضای تفاهم‌نامه با ایران را تایید کرد
🔹
دو مقام آمریکایی بامداد پنجشنبه به وبگاه «آکسیوس» گفتند که واشنگتن و تهران، یادداشت تفاهم برای پایان جنگ را امضا کرده و اکنون اجرایی شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/660624" target="_blank">📅 00:57 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660623">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
بقایی، سخنگوی وزارت خارجه: تصمیم حکیمانه جمهوری اسلامی این بود که در این مرحله درباره موضوع هسته‌ای مذاکره نکنیم. قرار شد تمرکز بر خاتمه جنگ باشد و این کار را انجام دادیم
🔹
از زمان اجرای تفاهمنامه، که الان است، ظرف ۶۰ روز درباره موضوع هسته‌ای و تحریم‌ها مذاکره کنیم. اگر زودتر هم مذاکره به نتیجه برسد، بهتر است. ولی با توجه به پیچیدگی موضوع، عدد ۶۰ روز منطقی است  و اگر لازم باشد، این زمان تمدید می‌شود.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/660623" target="_blank">📅 00:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660622">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔹
خبرهای داغ امروز را از دست ندهید
🔹
🔹
متن کامل تفاهم نامه ایران و آمریکا منتشر شد
👇
khabarfoori.com/fa/tiny/news-3223896
🔹
فاجعه اختلال بانکی / در این بانکها پول نگه ندارید!
👇
khabarfoori.com/fa/tiny/news-3223880
🔹
پزشکیان و ترامپ، جمعه تفاهمنامه را امضا می کنند؟
👇
khabarfoori.com/fa/tiny/news-3223875
🔹
حماس با تحویل سلاح خود موافقت کرد
👇
khabarfoori.com/fa/tiny/news-3223690
🔹
تصویری از همسر زیبای نیمار
👇
khabarfoori.com/fa/tiny/news-3223828
🔹
ویدئوهای جذاب ما را در وبسایت خبرفوری کلیک کنید
🔹
http://aparat.com/akhbar.fori/videos</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/660622" target="_blank">📅 00:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660618">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
بقایی: تفاهمنامه ایران و آمریکا قرار شد که به صورت دیجیتال امضا شود
🔹
وقتی تفاهمنامه به امضای روسای جمهور دو کشور برسد نقض آن هزینه بیشتری خواهد داشت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/660618" target="_blank">📅 00:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660617">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
بقایی، سخنگوی وزارت خارجه: کار ما پایان نیافته بلکه کار تازه آغاز شده است. هم باید مراقب اجرای آن توسط طرف مقابل باشیم. و هم درباره موضوع هسته‌ای و رفع تحریم‌ها مذاکره کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/660617" target="_blank">📅 00:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660616">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
بقایی، سخنگوی وزارت خارجه: اینکه در این مرحله یک توافق خاتمه جنگ را امضا کرده‌ایم به این معنا نیست که گذشته را فراموش کرده باشیم و درسهایی که به بهای گزاف آموخته‌ایم را از یاد برده باشیم
🔹
الان کار ما سخت‌تر از قبل است؛ چون همیشه اجرای توافقهای بین المللی…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/660616" target="_blank">📅 00:49 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-660615">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
بقایی: الان اگر متن را مرور کنیم خواهیم دید که چیز ناگفته‌ای را در این مدت نداشته‌ایم؛ همه موارد را کم و بیش بیان کرده‌ بودیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/660615" target="_blank">📅 00:48 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
