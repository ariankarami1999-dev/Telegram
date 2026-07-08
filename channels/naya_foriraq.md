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
<img src="https://cdn4.telesco.pe/file/C-1Yd3f7YCI70nFMCb8CrNyNgR_Kqjo4pQwP2Rv-5DcuIGy7M0d7aOtoiVGk4JYHUAJlj5N2pATuIQRTOmpfPWCM1-WX4UYTYJuGMXEYIw3yWU7NtVtXkJXMV92Tz1QI6o2uhahxKlMmfdrYqhvgC8YwOc3JrIRmieeVMfvLGTJCIH4FzghrgGCIbxwRJTCuedT7TPSoDBMJN-aCKXGXXfIaQVp-KIqB-fdGR6pqpEN6fD-PV0ly0t6wCXDS4b_vlQhAhAHSX-Czu7XLAZ2i1mWMlPplFDLQgPqAhNLg_ghftyVbjMY-c3BWhhbWtCHbugdwgud16iLL9D3LuMgfFA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 255K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 19:55:01</div>
<hr>

<div class="tg-post" id="msg-81843">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rtcprfHJV2pDPI7n48KqJ8Hd-YHezpe8bCpZFb-43r67mM-LVQLJUINFG-x2OiM-VIS4NO4wKeLi28Slw3jzXq6lF11dAk7dMbdaz7PPRTXZi7fpCIBJE7_pIw_lnUayggMjwdVkvVrqCjvt2OmVRhR5yAJ4-as0vsMhvrQQZ1cFSzt5hS-Wq4fVzJ1kZUoyznQMrO-SU60PNGZiT8YRmraobsV6gSkBzDjCMfu6iOb5QnWkETXERfAVTDUi-khUmJogAD7807Gyt_qdibOJ1ZvfDZOH8sm90aye7G_Wa7bIOamFCwH6vsyxaDtKsFPXEYuRJO9u1x1uUFhT6tpIMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AWXdXSRKsZvF3sHzgmBKGcVx2g97ZHokWagdpjzt9Dkvo1Bfm2Ni-1JSnpHpWGExhMcoF2Qrk8EELRuS7rm-xFV10q6-0AqOW0lJwnlZKcV_W6jfAAfNDHOt3Ngl9WKmj-JE6kI6ruxKn0xOsLSZsVwCvJUj0aRlO8DDOeGQVei8eJvDsK5p4HzSdyLYj9BOd___fULY-IR4t7pR_EUQhP9DYn03Pdj-W1U-Uv3MJV-aEvDEk3b7qG8r71_RVHr_-O_cjgfnSOLZlzzrEtKvmV0-b-uDDbgKk86LmIPIYS0J43DCgIrm79ysy2AwxU482oAuus8QdwtnePzfWtueQw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من لقاء أبناء المرجع الأعلى في العراق السيد علي السيستاني دام ظله بابن السيد الشهيد علي الخامنئي.</div>
<div class="tg-footer">👁️ 644 · <a href="https://t.me/naya_foriraq/81843" target="_blank">📅 19:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81842">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30cd79c3b1.mp4?token=KY8BSsA5U6drkJiPm-Wy58BdUNNCaEZlGmi9kixyCYaVnfQk6uS3VuI-WtDGYptMQzI2E3I5zBGlHa-3gUNQrTxJnRQByhG4tRkNq_datk7dXIElq1tUODdy_r6rYwP1_TWIo8vFBlGgYXyxnNZCLw9DzbzugaaCiPUCwDQRSetIBlaYL1U87_2DcwTPIt56GAmZKD8UUS4aLgfV5orzDd5fkNMKWtEakxiAc58ZK-mvThdwOf7faJeuz3tQ7sCzvXPJLm3v4X9V4XuVAgP7F1vQd8RVFy-XSFAO_GCGrIVgVp5TSdoRLkbbrnSCs_oIBpI_i-9NAtIsUvWGDapS-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30cd79c3b1.mp4?token=KY8BSsA5U6drkJiPm-Wy58BdUNNCaEZlGmi9kixyCYaVnfQk6uS3VuI-WtDGYptMQzI2E3I5zBGlHa-3gUNQrTxJnRQByhG4tRkNq_datk7dXIElq1tUODdy_r6rYwP1_TWIo8vFBlGgYXyxnNZCLw9DzbzugaaCiPUCwDQRSetIBlaYL1U87_2DcwTPIt56GAmZKD8UUS4aLgfV5orzDd5fkNMKWtEakxiAc58ZK-mvThdwOf7faJeuz3tQ7sCzvXPJLm3v4X9V4XuVAgP7F1vQd8RVFy-XSFAO_GCGrIVgVp5TSdoRLkbbrnSCs_oIBpI_i-9NAtIsUvWGDapS-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد مباشرة من صحن الامام الحسين عليه السلام</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/naya_foriraq/81842" target="_blank">📅 19:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81841">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ANpATfyADxgAWDxtlaiRYQdnHBI2mu78ZN6cHhjyFp-QAnG14pBtO5eNbr7BiEznKEcD8Q6nKKvEo26IEoXrOWRqniH2nkJ0SPHBMyuanHg1s3xgBX2XFXiYCIyIrpauL03PlmHSY7GJcfT6COB3hmNwG9k4UmfczqXhG5Yd2ak9FgMv5TTHRypCo93GFxbcWSJPG-jeq4o1-adOYw64-4oijp6NXgbwaAEmdLtyiNAbYQMKInjdTWdicFspoMYafpBXhgxEENkNceRjuq_WkU3DDGMIXeg-KXwRMQ-hK4OAjh_X0qDef4ladAtW0Fbxl2iF5Bz97Vg6_nszd6Crew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراسل نايا في كربلاء المقدسة: قطع شارع الشيخ عبد الزهرة الكعبي بانتظار وصول السيد الولي وسط انتشار واسع لقوات الحشد الشعبي.</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/naya_foriraq/81841" target="_blank">📅 19:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81840">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/114bd7b9a2.mp4?token=uTPiQMHAzsmYEYACeG7hjZl_Kz8mUGjG-rKJcUYECuxUj2UWSNf-B3XslHXlm9hr1_-3ARs5dwXMEFUJmC6Fdfa9ML9wIq_jE5ZCeSgbigVDXO-3pUjSmNwwxhx8SXpNsWcwwJK5a0Hh6NeQiAMnNk2iNQ6SODtPwgwJ1nbMPSf1s6UHE1erYR8IHccUIoJFvTFB9dIi-eE-Fu0VXdn8HkjYnHPzW4iKLckGRegGTIZjmgPU11J-lkFdxLVHLASz95nHP-DZtulrLDP0s-9bbl1LqBqcnxWyfraaRph6GuhwtYtYgQIVrSQiy9V5OGzkZLh68VZfi78LoDs4D9zcjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/114bd7b9a2.mp4?token=uTPiQMHAzsmYEYACeG7hjZl_Kz8mUGjG-rKJcUYECuxUj2UWSNf-B3XslHXlm9hr1_-3ARs5dwXMEFUJmC6Fdfa9ML9wIq_jE5ZCeSgbigVDXO-3pUjSmNwwxhx8SXpNsWcwwJK5a0Hh6NeQiAMnNk2iNQ6SODtPwgwJ1nbMPSf1s6UHE1erYR8IHccUIoJFvTFB9dIi-eE-Fu0VXdn8HkjYnHPzW4iKLckGRegGTIZjmgPU11J-lkFdxLVHLASz95nHP-DZtulrLDP0s-9bbl1LqBqcnxWyfraaRph6GuhwtYtYgQIVrSQiy9V5OGzkZLh68VZfi78LoDs4D9zcjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عامود 1096</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/naya_foriraq/81840" target="_blank">📅 19:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81839">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNTKtewQIWM_kuuiPTLElhazicoSpXV2tPq4D7TrlpSYTYWbWZ7-JZyt1i-4ujhkBlx6OmkfYV2KC4dxDLWXYG2_pvcsnYQC2fl12weFx2lpkg9KMU5u2oyk1foxtiVhgs7qJ5Bs-q81u93DY9BtiPRiEEfzaLpAABa9hU0sAmzJ622NRIkGHygeLEntuKsEu3_gUdq5jtrxZ0McpgnbuyPGwhqqS3iIseJp0BCGhSsB0bRU15iRNd2UKMoXaLOrrEgJMwG9dbFELXxPLV8-uQ4lp1OQUzV7jGMzRttjFfRbnCuEPBq6_XQxr87UwwEUdlAD5LbBCE733PaP4quNMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابناء المرجع الأعلى في العراق السيد محمد باقر السيستاني والسيد محمد رضا السيستاني حاضرون في كربلاء المقدسة للمشاركة بتشييع السيد الشهيد علي الخامنئي</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/naya_foriraq/81839" target="_blank">📅 19:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81838">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56ca63dcb4.mp4?token=u5L1O0JxylbLcyEezgYJIMpTAbhIkHxdN7eJbx4bjNzZj0J0Ymmnu32C6l-iJxN1If840elXGgaC3P1OBgZ8qoDJVr2th5dM_JJYlwWfLGj6xyHKPLJWsS-dNopH4IPxGVAiSDDWK4XI5rxeFhXFjOvdNfuqRaZWzo92JWVBRJLxyPlR94zvbjDQPXchioqb8w9wlDTAyHrZDb3uOl76wJteLn9X4tSz2pz9at6o313bFbAFIzDHNIj1RrfmRdROzhzspuVisUKk2wSqXgbQ6D7krZob7AMcXMJT0V92goFyjErETIrbf4h3cGGr3NdzXbR7CgRyXrQwfBuFFtn-lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56ca63dcb4.mp4?token=u5L1O0JxylbLcyEezgYJIMpTAbhIkHxdN7eJbx4bjNzZj0J0Ymmnu32C6l-iJxN1If840elXGgaC3P1OBgZ8qoDJVr2th5dM_JJYlwWfLGj6xyHKPLJWsS-dNopH4IPxGVAiSDDWK4XI5rxeFhXFjOvdNfuqRaZWzo92JWVBRJLxyPlR94zvbjDQPXchioqb8w9wlDTAyHrZDb3uOl76wJteLn9X4tSz2pz9at6o313bFbAFIzDHNIj1RrfmRdROzhzspuVisUKk2wSqXgbQ6D7krZob7AMcXMJT0V92goFyjErETIrbf4h3cGGr3NdzXbR7CgRyXrQwfBuFFtn-lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ممثل السيد مقتدى الصدر وسط المعزين في كربلاء المقدسة بانتظار وصول جثمان السيد الشهيد</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/naya_foriraq/81838" target="_blank">📅 19:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81837">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a98467fd50.mp4?token=TzBwuLTVHqyb7F3Kn7GET_GdRW3jkkB1h4Yw_hDkbGAHJcU0BFsqooIVvaPjbrku0lM4GYwb3Ytl9lrLwuKQFtelxth1O7pjT-TioIDJ_7k7FVhWqQKbxnWS5-gUN8TPV5JDh2OmvZxCNvlViU3iVRl-g3FeLbN1ouUmlSelVrAUDOlBEUMfD2oRgAG_DfK72eu9E_68BhUB_hdarxLEMaFeNECfBTReVCPXSMbXhs3UpqT6yoMIQAKHzPUW0751xa0jNRgQdrK38pCiuUVaFYQdbup6XpL2bXnf6VLmGZISYyVQIakOjGYOT-T3lIyiLGxhacjnYzfUlO66i2usDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a98467fd50.mp4?token=TzBwuLTVHqyb7F3Kn7GET_GdRW3jkkB1h4Yw_hDkbGAHJcU0BFsqooIVvaPjbrku0lM4GYwb3Ytl9lrLwuKQFtelxth1O7pjT-TioIDJ_7k7FVhWqQKbxnWS5-gUN8TPV5JDh2OmvZxCNvlViU3iVRl-g3FeLbN1ouUmlSelVrAUDOlBEUMfD2oRgAG_DfK72eu9E_68BhUB_hdarxLEMaFeNECfBTReVCPXSMbXhs3UpqT6yoMIQAKHzPUW0751xa0jNRgQdrK38pCiuUVaFYQdbup6XpL2bXnf6VLmGZISYyVQIakOjGYOT-T3lIyiLGxhacjnYzfUlO66i2usDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">المكان المخصص لوضع النعش الطاهر في مرقد الامام الحسين عليه السلام.</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/naya_foriraq/81837" target="_blank">📅 19:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81836">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3622436047.mp4?token=BoeiVxxXXELyiW3MjZFgHAWtX6oLVP6pVIU_qcavs7Is6rHMysBBHEXByo4nTbElr_-RJN2us1MONUVu3QDbW0Od4QWHB_CMx5iY7RM_iGkma-kOolTlem8zkwBWrF_N5WydJLngLw-xrG1xE2k_uZFfhJ3ZbSYhrRu0_ytPFAHA6eaRvzL6d9buH74QV-JFLwlD75UH9SmCnJ9Jg8LuK3FdoYyF1Shr-uBZmpMQ1Oai4itlOEZpcY1xZMIq3AsaATqqCyMUPcd14espxZggomEtUuSxoGb1nVWwerAzckxjJpbNhOP6r79_dOqTKbGlW-sps2Y2N1EPQU-GOPNm0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3622436047.mp4?token=BoeiVxxXXELyiW3MjZFgHAWtX6oLVP6pVIU_qcavs7Is6rHMysBBHEXByo4nTbElr_-RJN2us1MONUVu3QDbW0Od4QWHB_CMx5iY7RM_iGkma-kOolTlem8zkwBWrF_N5WydJLngLw-xrG1xE2k_uZFfhJ3ZbSYhrRu0_ytPFAHA6eaRvzL6d9buH74QV-JFLwlD75UH9SmCnJ9Jg8LuK3FdoYyF1Shr-uBZmpMQ1Oai4itlOEZpcY1xZMIq3AsaATqqCyMUPcd14espxZggomEtUuSxoGb1nVWwerAzckxjJpbNhOP6r79_dOqTKbGlW-sps2Y2N1EPQU-GOPNm0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جثمان السيد الشهيد يصل إلى عامود 1096</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/naya_foriraq/81836" target="_blank">📅 19:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81835">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b49bf1997.mp4?token=YsU-xZHpivc3HeG2Q1rSAAfk_r5xkCI7C61x9OLLX0I6GOc9kS-E8LKSvBaAeACdh_ymh0Roc-QJ8TtEqhZafKUfYgHjt_Scax-bHHDW7aEYuVclWdLiO7yrVbfJ_l_jF_UMKIzXsgyemFrFghLqy1dC9i4GDCT1bH4wHNH8R14vZcAw_8jYluYaO059MY0VLEuorLCkbQlHc0v-RRjrqvW6yplJAze1CVlcNe5YuN26YIu6_tAP2k1a1U8CHdfU-9ZWAuRrHPqj6mmEMG1oZWqt4AUROLGFM_-C1XgsvRaexWMmN0PF3ARTAZaEBT-cUUhQFFAYfLysKR3v7Bq6Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b49bf1997.mp4?token=YsU-xZHpivc3HeG2Q1rSAAfk_r5xkCI7C61x9OLLX0I6GOc9kS-E8LKSvBaAeACdh_ymh0Roc-QJ8TtEqhZafKUfYgHjt_Scax-bHHDW7aEYuVclWdLiO7yrVbfJ_l_jF_UMKIzXsgyemFrFghLqy1dC9i4GDCT1bH4wHNH8R14vZcAw_8jYluYaO059MY0VLEuorLCkbQlHc0v-RRjrqvW6yplJAze1CVlcNe5YuN26YIu6_tAP2k1a1U8CHdfU-9ZWAuRrHPqj6mmEMG1oZWqt4AUROLGFM_-C1XgsvRaexWMmN0PF3ARTAZaEBT-cUUhQFFAYfLysKR3v7Bq6Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تجمعات هائلة من امام مرقد الامام العباس عليه السلام</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/naya_foriraq/81835" target="_blank">📅 19:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81832">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b41d2542f.mp4?token=tiQ5PFgdNVs7u9F4z0UkaDawN4qI0TC0psfFF-E_jv3Cj6I-NdHtRpxXnx4NX-C6lT9wmtjoMvTNwT1qgrY8QNG_-n0UT_A4rDbZqgYeKq8jpDVHI0dm2sbQ85VP6m7oBIrZ_2FzHaDtiKido9_cODTm8roEeQKcrIfRLGbbG4yRlWdgpQ7L109UijCoireJDgbLl36sQnegAa5Bugd1z6vxvM0kCIoStCDlqAt2bLd387BbRzT2lNfV82zmG15YrmIP_JD26KRUieucy-t6eJbe7KEZzqtYPSJK0UcP89VJjivspiVL9h-aGzMN9DT0JmrzodCOKJERTAbvD5_QJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b41d2542f.mp4?token=tiQ5PFgdNVs7u9F4z0UkaDawN4qI0TC0psfFF-E_jv3Cj6I-NdHtRpxXnx4NX-C6lT9wmtjoMvTNwT1qgrY8QNG_-n0UT_A4rDbZqgYeKq8jpDVHI0dm2sbQ85VP6m7oBIrZ_2FzHaDtiKido9_cODTm8roEeQKcrIfRLGbbG4yRlWdgpQ7L109UijCoireJDgbLl36sQnegAa5Bugd1z6vxvM0kCIoStCDlqAt2bLd387BbRzT2lNfV82zmG15YrmIP_JD26KRUieucy-t6eJbe7KEZzqtYPSJK0UcP89VJjivspiVL9h-aGzMN9DT0JmrzodCOKJERTAbvD5_QJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطقة مابين الحرمين الشريفين تشهد تجمعات هائلة لتشييع السيد الشهيد علي الخامنئي</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/naya_foriraq/81832" target="_blank">📅 19:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81831">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">جثمان السيد الشهيد يصل إلى عامود 1096</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/naya_foriraq/81831" target="_blank">📅 19:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81830">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">منطقة مابين الحرمين الشريفين تشهد تجمعات هائلة لتشييع السيد الشهيد علي الخامنئي</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/naya_foriraq/81830" target="_blank">📅 19:08 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81829">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/235484d88c.mp4?token=M_5gLCm7Z5bGJpBfC4sykxwrEAyfGM-pztpqlwJYqXK8hZXlmspETkNV2jqOew8ur6Xx2Zdl4PqxsBmomYh9yu2sSQj5r8b93dcoxdZieaPNyQ15akiXFGJpTfvCphA_8JaFZhoXACYVyF8ohK6jz5ucZc1j9PqIywjkfUngXL_SPffykyQkosDoBr8cE25lAQ_bEQSjzBCqhXGg8k19RbVh3l2QsPBNDIBRTq1azMLaZk_0YnV2cGPP6C7MkqeN3rH2eU8gJG8Tb7ms7b2kkPTpSEpUEfsLIIsGmPlVnxTqMtTkNI1Af7qsIfi5B3s0cZ-O7y8N3gkgqyR5A2aAmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/235484d88c.mp4?token=M_5gLCm7Z5bGJpBfC4sykxwrEAyfGM-pztpqlwJYqXK8hZXlmspETkNV2jqOew8ur6Xx2Zdl4PqxsBmomYh9yu2sSQj5r8b93dcoxdZieaPNyQ15akiXFGJpTfvCphA_8JaFZhoXACYVyF8ohK6jz5ucZc1j9PqIywjkfUngXL_SPffykyQkosDoBr8cE25lAQ_bEQSjzBCqhXGg8k19RbVh3l2QsPBNDIBRTq1azMLaZk_0YnV2cGPP6C7MkqeN3rH2eU8gJG8Tb7ms7b2kkPTpSEpUEfsLIIsGmPlVnxTqMtTkNI1Af7qsIfi5B3s0cZ-O7y8N3gkgqyR5A2aAmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نعش السيد الولي يصل قرب تقاطع الدرة</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/naya_foriraq/81829" target="_blank">📅 19:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81828">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc00f4ecfd.mp4?token=an-ILfKsYnljGLzFhxdIPl4Wa_VDe4XBWP8HtLkOmDppdsHHYTy6GHVLMb-fkIDQ_8wda3oRnvurf-OxYJ07owXjmMmFrpMLDpg22cMEUwguDtUL9oPUAb35qzYjd3XraQRtAVMIX4WW6Q0PfhqMO_sumO8SgW4FtkwolHVEddmsHlXy03jflyfc6xqVnupG1373MGHT1rXfs0r-9dvwKmN_bjrfkpaZGEkkGFrE830EBPB09K33rN14_cz9FybIP3zG9it4-DGBaWL6fvqcV2O10rr2JqHBiMH8242eThJvXF68DlnwnMzYjTdzoOuDw-dcsirJPTC1kHHGixPW5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc00f4ecfd.mp4?token=an-ILfKsYnljGLzFhxdIPl4Wa_VDe4XBWP8HtLkOmDppdsHHYTy6GHVLMb-fkIDQ_8wda3oRnvurf-OxYJ07owXjmMmFrpMLDpg22cMEUwguDtUL9oPUAb35qzYjd3XraQRtAVMIX4WW6Q0PfhqMO_sumO8SgW4FtkwolHVEddmsHlXy03jflyfc6xqVnupG1373MGHT1rXfs0r-9dvwKmN_bjrfkpaZGEkkGFrE830EBPB09K33rN14_cz9FybIP3zG9it4-DGBaWL6fvqcV2O10rr2JqHBiMH8242eThJvXF68DlnwnMzYjTdzoOuDw-dcsirJPTC1kHHGixPW5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جثمان السيد القائد يصل إلى محافظة كربلاء</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/naya_foriraq/81828" target="_blank">📅 19:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81825">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f1a1de273.mp4?token=lqEcwlP8SxcElBbmCmT-0jjELOGy91-JVRUP3xf5pGfjWvvEiQQocFGKq26q1FetomVMjbfKz0k2gQM1vrSS1mUlhNShRrvDyP43I06qTWQ6A6maQBHHGEQCB26CP9YN9hWeCZLzJW-0J3vUmSV3rMh1KXMd-mw-toYojkB-ddjFYEgGivaRK5OrTkejf8nk9lMSBHbuZ0vS8Oy5Mieptir11FQdJKC5BFZ2rX3AQJfiyUwRFKPELqIp-xd6YlbHKe7UJ6DrO1uj6yKQ8WI7daADok6ocbFUGoa2ILHsZS2IF2xanZqWkCGB23ro2PxYFJ8LMeqRcTpv4v9-xoW45AiB7_KARYBDGaWfJ03y1M2rlTAer2lcSBc7ytiA_qnunYFSD5JTesAgELzS3hDq9uc6vbT9phTN8H9Zk0WOczrbaq1ljnvm3cva8MIL8ffoSE0m1vi6_yPx55nUswL2RDjgjO91IoeBjj2mCH-M9Y_vQs7L_7Wgia3qHtXhQbfeflatL0gqfX19JLC52xRzitZGGNUEa00z3Ntp8q8xrapHzFKp0UAGkhgd5N2Qi8jz5gLSS2C2SPEIQjlIO7PLRYMY0NqpKPX1UHfMHmSqrxbZlrvxsscrUiaff9MNLnjK9rBkxRy5Q_FT2hr3Mqh00EtziBg6oA3kAQVgLpSSjCM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f1a1de273.mp4?token=lqEcwlP8SxcElBbmCmT-0jjELOGy91-JVRUP3xf5pGfjWvvEiQQocFGKq26q1FetomVMjbfKz0k2gQM1vrSS1mUlhNShRrvDyP43I06qTWQ6A6maQBHHGEQCB26CP9YN9hWeCZLzJW-0J3vUmSV3rMh1KXMd-mw-toYojkB-ddjFYEgGivaRK5OrTkejf8nk9lMSBHbuZ0vS8Oy5Mieptir11FQdJKC5BFZ2rX3AQJfiyUwRFKPELqIp-xd6YlbHKe7UJ6DrO1uj6yKQ8WI7daADok6ocbFUGoa2ILHsZS2IF2xanZqWkCGB23ro2PxYFJ8LMeqRcTpv4v9-xoW45AiB7_KARYBDGaWfJ03y1M2rlTAer2lcSBc7ytiA_qnunYFSD5JTesAgELzS3hDq9uc6vbT9phTN8H9Zk0WOczrbaq1ljnvm3cva8MIL8ffoSE0m1vi6_yPx55nUswL2RDjgjO91IoeBjj2mCH-M9Y_vQs7L_7Wgia3qHtXhQbfeflatL0gqfX19JLC52xRzitZGGNUEa00z3Ntp8q8xrapHzFKp0UAGkhgd5N2Qi8jz5gLSS2C2SPEIQjlIO7PLRYMY0NqpKPX1UHfMHmSqrxbZlrvxsscrUiaff9MNLnjK9rBkxRy5Q_FT2hr3Mqh00EtziBg6oA3kAQVgLpSSjCM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
عدسة نايا ترصد التجمع الهائل للمعزين بالسيد الولي داخل حرم الامام الحسين عليه السلام</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/naya_foriraq/81825" target="_blank">📅 19:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81824">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fec731f577.mp4?token=uuV78cvv9DEJzjI5YoMxqHHl--Mm_OLvsUceC04EKY6v9rzVduhWCBKTK-Uho2n1IBjibzLgifErO1djv8Eg8fi0dZmho3xpGf7R_X_A-dJTMY14hmf-BIvOJ3jeSdiY6dXdSjXWRqc-5HcL60dQ0wjpGiXBMUGChPRc2BdrRIbpqhGbKWxzhupsLzJ03jFsCvkwQhlwrr5Y4vuVvXCwgIfMZI-wevAQ2YO0dmoMJjpqhLuSNGr-lMGGjuuC0iXmmNzhR8-W7qPo1iehVnNobq147F65VuRFtS7GsCtx_7-815y3po-F5CaRp6X0vOFTsenVuewOBwyOmjsVprp-1C9WKCJZ9LheSrEsTBkGqKYux4X7Iagd-8ciD-Vr5Xd3cUwA_9KHuFMB1A0cgQgSR6Z11K3ZjCYQJfiUtED7vhp7IKkhqHFh8xG90bNkoqksT6RHAabKkLa-G5F8j9Gyf8XYcvVChayaxwhIGrtweYzzwHDCKXgU4QwW6fQUQ5ETgBmkayjhWTbx1ZRQDJhXIoJdDMS1FgvvC9qbpP-V948Y7LnBE_syJwadWTIXI0kDJ4ontnQDyQUzdxr1tDO9smaf9Yn8z05OpfB9geK3hmjb1KvI-L9_3vc_OYLtr9pifit8fSyzOTXxTpZ_i1G8AM-hmd_ko0ha6Xz0UoS8QbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fec731f577.mp4?token=uuV78cvv9DEJzjI5YoMxqHHl--Mm_OLvsUceC04EKY6v9rzVduhWCBKTK-Uho2n1IBjibzLgifErO1djv8Eg8fi0dZmho3xpGf7R_X_A-dJTMY14hmf-BIvOJ3jeSdiY6dXdSjXWRqc-5HcL60dQ0wjpGiXBMUGChPRc2BdrRIbpqhGbKWxzhupsLzJ03jFsCvkwQhlwrr5Y4vuVvXCwgIfMZI-wevAQ2YO0dmoMJjpqhLuSNGr-lMGGjuuC0iXmmNzhR8-W7qPo1iehVnNobq147F65VuRFtS7GsCtx_7-815y3po-F5CaRp6X0vOFTsenVuewOBwyOmjsVprp-1C9WKCJZ9LheSrEsTBkGqKYux4X7Iagd-8ciD-Vr5Xd3cUwA_9KHuFMB1A0cgQgSR6Z11K3ZjCYQJfiUtED7vhp7IKkhqHFh8xG90bNkoqksT6RHAabKkLa-G5F8j9Gyf8XYcvVChayaxwhIGrtweYzzwHDCKXgU4QwW6fQUQ5ETgBmkayjhWTbx1ZRQDJhXIoJdDMS1FgvvC9qbpP-V948Y7LnBE_syJwadWTIXI0kDJ4ontnQDyQUzdxr1tDO9smaf9Yn8z05OpfB9geK3hmjb1KvI-L9_3vc_OYLtr9pifit8fSyzOTXxTpZ_i1G8AM-hmd_ko0ha6Xz0UoS8QbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شوارع كربلاء المقدسة تكتظ بالملايين المشيعين لجثمان السيد علي الخامنئي</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/naya_foriraq/81824" target="_blank">📅 18:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81823">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">جثمان السيد القائد يصل إلى محافظة كربلاء</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/naya_foriraq/81823" target="_blank">📅 18:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81822">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33e4f47a54.mp4?token=MIG4qmWFAt7qhloYxJjF8vpZZ_LKob5BueGVV8p4ar-SPt32YJAeQf6YZd3hDEb46jaN4f8zHxfY5aoB1Rov9xzeLm9GOI3ZWTsJqNHoMO-MzCdn2CydD-JGiAWHzrG3dzm4cpbzP6N1EsFtwXGWXD1XaNJclL1Tfjw7WJWwqFNFd9XKLV3WE4YPfIPhbAMzNo5tDmfxIDw3PHvjCLPXAH34Y1WuxWGicYgt2cCMknChExYsfn4ZYzlQnrgRr60U8U9TliSujp62sz6V3WJnjmoouj7OvmijFkugGLpHrLWafxpZJHBFf_gCRLU5H1PSTsEXxJhkzPXBAkjJ2GN4sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33e4f47a54.mp4?token=MIG4qmWFAt7qhloYxJjF8vpZZ_LKob5BueGVV8p4ar-SPt32YJAeQf6YZd3hDEb46jaN4f8zHxfY5aoB1Rov9xzeLm9GOI3ZWTsJqNHoMO-MzCdn2CydD-JGiAWHzrG3dzm4cpbzP6N1EsFtwXGWXD1XaNJclL1Tfjw7WJWwqFNFd9XKLV3WE4YPfIPhbAMzNo5tDmfxIDw3PHvjCLPXAH34Y1WuxWGicYgt2cCMknChExYsfn4ZYzlQnrgRr60U8U9TliSujp62sz6V3WJnjmoouj7OvmijFkugGLpHrLWafxpZJHBFf_gCRLU5H1PSTsEXxJhkzPXBAkjJ2GN4sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">المعزين في فلكة جودة بانتظار تشييع جثمان السيد الشهيد</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/naya_foriraq/81822" target="_blank">📅 18:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81821">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">بعد حوادث انفجار صهاريج النفط العراقية على الأراضي السورية.. حادث جديد يطال 3 شاحنات عراقية مما أدى إلى احتراقهن في منفذ اليعربية الحدودي بين العراق وسوريا.</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/naya_foriraq/81821" target="_blank">📅 18:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81820">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d57c3e2f71.mp4?token=XqM1vgfgoTVz8H5YbEP5Y7yFudUjB6eMBezQ7MaiFE7sRui-rSaCDp4Y3em_PMz7jlRwkKDp6ETCMFzPtJcdT422QdAtZmdtbJifJww0a1OIlWz8bIcLC3IccrSeBFn_-aKhU3ECcZHX5Fh7muMrPchwyY7knut54Li-xFeRo2X1A6oDoSf5FAWNSCupxY7H746FZh7DHi-gHaB8aLYV1ziukvCVfk3hbtF2r1rxQCGBfya7fo35a7zQS9all4zrf7jsH4NsDFSi52TQDyd7wj_TwFQXkuWloJ4AU-44rNTCeAySzjxrABthPLjygRaCGMvFX8Tbv02Gef-2FURWpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d57c3e2f71.mp4?token=XqM1vgfgoTVz8H5YbEP5Y7yFudUjB6eMBezQ7MaiFE7sRui-rSaCDp4Y3em_PMz7jlRwkKDp6ETCMFzPtJcdT422QdAtZmdtbJifJww0a1OIlWz8bIcLC3IccrSeBFn_-aKhU3ECcZHX5Fh7muMrPchwyY7knut54Li-xFeRo2X1A6oDoSf5FAWNSCupxY7H746FZh7DHi-gHaB8aLYV1ziukvCVfk3hbtF2r1rxQCGBfya7fo35a7zQS9all4zrf7jsH4NsDFSi52TQDyd7wj_TwFQXkuWloJ4AU-44rNTCeAySzjxrABthPLjygRaCGMvFX8Tbv02Gef-2FURWpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">العراقيين يفترشون الأرض في منطقة مابين الحرمين الشريفين بانتظار وصول السيد القائد لتشييعه</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/naya_foriraq/81820" target="_blank">📅 18:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81819">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45f76af383.mp4?token=CvNJXnbKgIBt9A8hQvwMdv7hmwUG7uIkmjjwh8f84OTTq9wHFl649Ibx7xvrXhbWq8aqU3eF0wG4lSRJn4gzBtuQDjmj07-tTU_NoCSFhJnffXjlQIM7Sw65LiVZHBMRkCU00dNTgyK7jUfwO-A-uTH1ee_QP03L8ZjL96TtEhUI6NCktGReSWyWvhseUTi0ahJWbIIB0Mb8zMGLWoL3F_ymJbS4XC28qIsPTAl7CFh3zN0iNXf78PBM5o6dm2qlkJ3trNP7_XbNBPRF1j9cNbfiImrTrk20uco2YP8SGZnWEvIN27bQjfCgva-HoUlh9MoLLLGas6O6OJCOAMaTgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45f76af383.mp4?token=CvNJXnbKgIBt9A8hQvwMdv7hmwUG7uIkmjjwh8f84OTTq9wHFl649Ibx7xvrXhbWq8aqU3eF0wG4lSRJn4gzBtuQDjmj07-tTU_NoCSFhJnffXjlQIM7Sw65LiVZHBMRkCU00dNTgyK7jUfwO-A-uTH1ee_QP03L8ZjL96TtEhUI6NCktGReSWyWvhseUTi0ahJWbIIB0Mb8zMGLWoL3F_ymJbS4XC28qIsPTAl7CFh3zN0iNXf78PBM5o6dm2qlkJ3trNP7_XbNBPRF1j9cNbfiImrTrk20uco2YP8SGZnWEvIN27bQjfCgva-HoUlh9MoLLLGas6O6OJCOAMaTgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مراسل نايا: ازدحام شديد وتوافد مليوني مستمر منذ الرابعة عصراً في شارع العباس (قطع المحكمة) بكربلاء، للمشاركة في تشييع جثمان السيد علي الخامنئي، وسط بدء المشيعين بافتراش الأرض انتظاراً لوصول النعش المطهر</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/naya_foriraq/81819" target="_blank">📅 18:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81818">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">يأتوك رجالا وعلى كل ضامر يأتين من كل فج عميق
الحيد في الميدان</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/naya_foriraq/81818" target="_blank">📅 18:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81817">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">الحشد الشعبي: تشير التقديرات الأولية حتى الآن إلى أن عدد المشاركين في مراسم التشييع تجاوز أربعة ملايين مشيّع، فيما لم يدخل النعش المقدس بعد إلى الشارع المخصص لإقامة مراسم التشييع .</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/naya_foriraq/81817" target="_blank">📅 18:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81816">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">الحشود العشائرية الهائلة تنتظر وصول الجثامين في سيطرة مدخل كربلاء المقدسة</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/naya_foriraq/81816" target="_blank">📅 18:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81815">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">وصول النعش إلى عامود 888 في كربلاء المقدسة</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/naya_foriraq/81815" target="_blank">📅 18:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81814">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9fb0cff28.mp4?token=KEdkam7Wuj6LAk2jWID_hshtR191PDczYHP9ekyB1c1CTrqcbsaxJUGRtOOHPqwH2t9WEwQGD0Ylk1aRb4os_xNNQCHtAyI3wLjX8sos6eRLE_gFfzQOWWifAlROLyGqwciBISTETGrku-_5KJETV3pk5Kngwwtzqs33il2CbvcT52i3vCzuQsPnEQqi6UC3EONlv1dMJVW1-ytzo_tLpcwccL9B53FbYLvhKEI9d9CkXpdncF8djzXPtJAEKoZzA4A_NS1ukvjehZZfVt1TGm_JcZqYkPGM0RedHO0tO4wgTq9b5UQf554DRw8OFrNfCIRiR-uS0GJ1XmttW9qwgzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9fb0cff28.mp4?token=KEdkam7Wuj6LAk2jWID_hshtR191PDczYHP9ekyB1c1CTrqcbsaxJUGRtOOHPqwH2t9WEwQGD0Ylk1aRb4os_xNNQCHtAyI3wLjX8sos6eRLE_gFfzQOWWifAlROLyGqwciBISTETGrku-_5KJETV3pk5Kngwwtzqs33il2CbvcT52i3vCzuQsPnEQqi6UC3EONlv1dMJVW1-ytzo_tLpcwccL9B53FbYLvhKEI9d9CkXpdncF8djzXPtJAEKoZzA4A_NS1ukvjehZZfVt1TGm_JcZqYkPGM0RedHO0tO4wgTq9b5UQf554DRw8OFrNfCIRiR-uS0GJ1XmttW9qwgzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شارع ابو مهدي المهندس</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/naya_foriraq/81814" target="_blank">📅 18:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81813">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31c4c42142.mp4?token=NbA-K_i6ZcNy1M70ElSbmGAj2DXO4bgCI2ZbNKI9btXQ46cyZqPzXCQYJCWW106Zd93L1yTEC0kn1C-qrFOuiYsqOtbMmXSOmBBzktq7pQRN32J2GTUtKxLlukoY8NB3tlaL0Kd8uy12DHwBHkYKe2k7ttwSANbhW1yeJ3WCGKhnRSbJGQk_bQu6JzT-SIHagMVUjhnEdLjjw44-4FSCWISG8H6nlVQs5mfRgGXckhv96jUFiZ5_IL9o79hN2uGn0n1Q_NrGdahtGIs3Bv7vqsrZAoGy1AKdzZtTOFr8OnIwlOujeFkeyLbIOFvDpgEurlhBm1UZkiLvRDLm7OQs3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31c4c42142.mp4?token=NbA-K_i6ZcNy1M70ElSbmGAj2DXO4bgCI2ZbNKI9btXQ46cyZqPzXCQYJCWW106Zd93L1yTEC0kn1C-qrFOuiYsqOtbMmXSOmBBzktq7pQRN32J2GTUtKxLlukoY8NB3tlaL0Kd8uy12DHwBHkYKe2k7ttwSANbhW1yeJ3WCGKhnRSbJGQk_bQu6JzT-SIHagMVUjhnEdLjjw44-4FSCWISG8H6nlVQs5mfRgGXckhv96jUFiZ5_IL9o79hN2uGn0n1Q_NrGdahtGIs3Bv7vqsrZAoGy1AKdzZtTOFr8OnIwlOujeFkeyLbIOFvDpgEurlhBm1UZkiLvRDLm7OQs3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باب القبله للإمام الحسين عليه السلام بانتظار الإمام القائد</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/naya_foriraq/81813" target="_blank">📅 18:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81812">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdffb3ca0f.mp4?token=sWt0M3RTe-LXG1AXWm6NOIRJtqe4d0D2B2_KafhvxtMVpE5859KWYz5xpj7tvALPAAbBhJZoxbLMJcrXkxUCgCx7nO643OwmrNc7RcVcsQ8mD1Dv3unH61C5NlkWOcNSRES40OwcjSUCjNNVnnQ2KbB-ZO9UGckqFX2DI2-n_ssxRDcZwqMZ9kCLqlPgK2NLHVYehuOnlx8FKIyrs8_1E_1vCVYg_RVa8uXZsvlRZnYDCyB_UDjmCrWAlP5FjqEDmrX3b0Ps8FTvA9w6bJQ0qouAIMgpvVrZzraaij6FF2nzfa8X8d6u9XkCPZUu4S45p6u-KS_cFdueGQ5m2gfKIq1NYavSQZ8xC5GXpjptbWHOqiKUgjDB2hXcj_nd64bLHd7gVfUCthjYmxxaKLA6j_eY2GP7snvmZ9SlCWxQ6dk41aCrN8NGdNrgHhuNoC9Jqyhjy9cQ7CMttzdhYd8jNLJDQMDjueIuOeG2fkzPBBeSX6xKPtXXfiOHRVhKyVIMZb20CzM7KSO9U5xPdtwp9tkmW4f0IMR0h8GfMbz57Zvgqhgpc2JXALQNGkBZDYLwhYQl4yiutbgPODNvh6GT_WXQ5aE05is0L3wtLuBB2kSZSE83_BzfsAlewqaRmjyDb9Z4ztCLd4zrdvk56oQmvqFMTB3tGM8Xx7Z_Y5AgxnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdffb3ca0f.mp4?token=sWt0M3RTe-LXG1AXWm6NOIRJtqe4d0D2B2_KafhvxtMVpE5859KWYz5xpj7tvALPAAbBhJZoxbLMJcrXkxUCgCx7nO643OwmrNc7RcVcsQ8mD1Dv3unH61C5NlkWOcNSRES40OwcjSUCjNNVnnQ2KbB-ZO9UGckqFX2DI2-n_ssxRDcZwqMZ9kCLqlPgK2NLHVYehuOnlx8FKIyrs8_1E_1vCVYg_RVa8uXZsvlRZnYDCyB_UDjmCrWAlP5FjqEDmrX3b0Ps8FTvA9w6bJQ0qouAIMgpvVrZzraaij6FF2nzfa8X8d6u9XkCPZUu4S45p6u-KS_cFdueGQ5m2gfKIq1NYavSQZ8xC5GXpjptbWHOqiKUgjDB2hXcj_nd64bLHd7gVfUCthjYmxxaKLA6j_eY2GP7snvmZ9SlCWxQ6dk41aCrN8NGdNrgHhuNoC9Jqyhjy9cQ7CMttzdhYd8jNLJDQMDjueIuOeG2fkzPBBeSX6xKPtXXfiOHRVhKyVIMZb20CzM7KSO9U5xPdtwp9tkmW4f0IMR0h8GfMbz57Zvgqhgpc2JXALQNGkBZDYLwhYQl4yiutbgPODNvh6GT_WXQ5aE05is0L3wtLuBB2kSZSE83_BzfsAlewqaRmjyDb9Z4ztCLd4zrdvk56oQmvqFMTB3tGM8Xx7Z_Y5AgxnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: ربما سنفعل بعض الأشياء التي سترفع أسعار النفط. عندما نهاجم إيران، يرتفع سعر النفط. لا بأس بذلك.</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/81812" target="_blank">📅 18:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81811">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ترامب: أعتقد أن إسرائيل ستنسحب من جنوب لبنان.</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/naya_foriraq/81811" target="_blank">📅 18:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81810">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6b458bf5b.mp4?token=H871PzjGPwGU0nuzvRkBlHls11seqUGQ2jeoPvX66PyAWgltUqUrv_cqVDhGvuiwrMt5u2WyOtmLyLjY31s2IPs9VSLuc8uyOtewZirDDPW8q3IauKD8DK8XFG69xvAvm3ovxbS6TAM9fOH-P1xlFr4tf8gIvKo2JruFXWR5ElG1NrDFQVy6RkR9cs-Vz6j8pC-YWwAJKN7I08ycUp_OTxtv16uyvVEWCNJN1mHR5JoaTDXF9GLSO-Fv3DGMI3--n_dlmpoxRbmB8v7MoLKZ2ogE4PwA56nrcFGvVFumKjB9gZ8axUb0OJ9NUdM3TVpyGcmrRx19JiCswKpl9Btpbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6b458bf5b.mp4?token=H871PzjGPwGU0nuzvRkBlHls11seqUGQ2jeoPvX66PyAWgltUqUrv_cqVDhGvuiwrMt5u2WyOtmLyLjY31s2IPs9VSLuc8uyOtewZirDDPW8q3IauKD8DK8XFG69xvAvm3ovxbS6TAM9fOH-P1xlFr4tf8gIvKo2JruFXWR5ElG1NrDFQVy6RkR9cs-Vz6j8pC-YWwAJKN7I08ycUp_OTxtv16uyvVEWCNJN1mHR5JoaTDXF9GLSO-Fv3DGMI3--n_dlmpoxRbmB8v7MoLKZ2ogE4PwA56nrcFGvVFumKjB9gZ8axUb0OJ9NUdM3TVpyGcmrRx19JiCswKpl9Btpbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: أعتقد أن إسرائيل ستنسحب من جنوب لبنان.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/81810" target="_blank">📅 18:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81809">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔻
مصدر أمني لنايا في كربلاء المقدسة: تم توجيه سائقي النعش بالاسراع لتلافي حدوث خلل في وقت الاستقبال.
النعش الآن أمام عامود 808 بسرعة 60 كم</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/naya_foriraq/81809" target="_blank">📅 18:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81807">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3702b717cb.mp4?token=t9TVYempMWiXfjQXdFWfiRg3TasaRqqnN3bI4eop6laDdL6Wp2jv_5eig7J9xFLSUdoGjSW33IweauSe68YyFu_zsihxutd8yp999fskSvGH2qi43NlhclwhqZDWi8xiUg2SRsRXU-dqAGS_vGR4C89kBHaxCzF1ZNUF5w28-_HMJPnjMerOim9AV5Xv6N07-aYakOrQ8dTMMCIcQ2AK8DBlXeFowGVB5hn_tcLuj8wbpWo_ESgPGwp3pjfgKQtqI3V_3BhI4y4DByeUFFO2M5WzQyC7T54WQnfN7UlRWK8SoRbyQAdgPj4fMaFS0x0NPy7PeFG8VTedw2JhKLx1SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3702b717cb.mp4?token=t9TVYempMWiXfjQXdFWfiRg3TasaRqqnN3bI4eop6laDdL6Wp2jv_5eig7J9xFLSUdoGjSW33IweauSe68YyFu_zsihxutd8yp999fskSvGH2qi43NlhclwhqZDWi8xiUg2SRsRXU-dqAGS_vGR4C89kBHaxCzF1ZNUF5w28-_HMJPnjMerOim9AV5Xv6N07-aYakOrQ8dTMMCIcQ2AK8DBlXeFowGVB5hn_tcLuj8wbpWo_ESgPGwp3pjfgKQtqI3V_3BhI4y4DByeUFFO2M5WzQyC7T54WQnfN7UlRWK8SoRbyQAdgPj4fMaFS0x0NPy7PeFG8VTedw2JhKLx1SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
عدسة نايا
ترصد الحشود البشرية الهائلة التي تستعد لاستقبال جثمان الشهيد</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/naya_foriraq/81807" target="_blank">📅 18:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81806">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53dd552cc7.mp4?token=JNKubcs_FT2BsCF3bRPIvkBkro9HZFg9MFYal16kRiPG88GW1oSvlJt1_wH3HC4pcKPkhOI5fID5Xf_JykAXN42md6KSQGT4OUEVVOJT_5LhIXkTilQk06fOXnUqLbORLHu7pnJtUndCdqMDVZnxhWLLGQOZhtZ9LxMokA-Rz7pMQ0so_MumA9QhmT0F1t0Ui4qtSzXfr13oIayRnPCnWKgy2TmU7pXHrUAwPa4ZSfkJweLcTHNRxXMYiaTpDpUHAeJlSKItVM5XfrUHPa_EQ2wyPAz_h-BvCoCPjwPctj8KTnlvQsQy1W2GpiRfXn1OcYPRM_lc5qifqRQjM3tSfmPw_oIpMcw5_4YASLZMnkJYjQimGWrdedJwIpWqIsIifP3pgxFVccXYOYlmkvl_GeYxFqvH7AcT-OCrbzIyW4b56eAERwzVK2wQuXUUI_RuIsujzz66gvpE--yuCjzjHTLzO71BCO0PxIaPX26czQ5Rgf7hUdFjQt5CbH3vLPr3hILimlL0YG_TQgN393_15L5HuFMeg-EH6KZBT8I26Hx2zrFJzbCIIU4fn5gjzqmiew2UUrFapnk614dUjLBb5v2H063heuQ6MrbFOa9locmzYTDTk5D2t5-qY5SWnA_5nRkoIwQ-4DRfr4Q7Mz8d2w3JuoTxye9kkOqGuS1aTm8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53dd552cc7.mp4?token=JNKubcs_FT2BsCF3bRPIvkBkro9HZFg9MFYal16kRiPG88GW1oSvlJt1_wH3HC4pcKPkhOI5fID5Xf_JykAXN42md6KSQGT4OUEVVOJT_5LhIXkTilQk06fOXnUqLbORLHu7pnJtUndCdqMDVZnxhWLLGQOZhtZ9LxMokA-Rz7pMQ0so_MumA9QhmT0F1t0Ui4qtSzXfr13oIayRnPCnWKgy2TmU7pXHrUAwPa4ZSfkJweLcTHNRxXMYiaTpDpUHAeJlSKItVM5XfrUHPa_EQ2wyPAz_h-BvCoCPjwPctj8KTnlvQsQy1W2GpiRfXn1OcYPRM_lc5qifqRQjM3tSfmPw_oIpMcw5_4YASLZMnkJYjQimGWrdedJwIpWqIsIifP3pgxFVccXYOYlmkvl_GeYxFqvH7AcT-OCrbzIyW4b56eAERwzVK2wQuXUUI_RuIsujzz66gvpE--yuCjzjHTLzO71BCO0PxIaPX26czQ5Rgf7hUdFjQt5CbH3vLPr3hILimlL0YG_TQgN393_15L5HuFMeg-EH6KZBT8I26Hx2zrFJzbCIIU4fn5gjzqmiew2UUrFapnk614dUjLBb5v2H063heuQ6MrbFOa9locmzYTDTk5D2t5-qY5SWnA_5nRkoIwQ-4DRfr4Q7Mz8d2w3JuoTxye9kkOqGuS1aTm8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترمب: بإمكان سوريا المساعدة في مجابهة حزب الله
‏سأرفع سوريا من قائمة الدول الراعية للإرهاب</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/81806" target="_blank">📅 17:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81805">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/618ee3ed71.mp4?token=LMOA89gBz_Fvd-n1rVdI_adtv6d_eb9GsutoX9-dPoqAA86S-jjOBu70_O7WzAY26IHaxaZ7qpeKUHKsh65R-8z_jhC7qtkRkLK1eNIKMa1WdaryGuk8ygt1id5V0H3mlGxPMj3V6iTT_AHynHSaAjPVFbRTujGtbkolw5ky18h9Cj95CBSLyNr0n-9RFnEjjriNS4j_ggfSEU-zZDNBMaOvVao0Oy_Fw45lYWh8ORGScwNcEdSHOg_3CbidZVwYKxh7wsEzXN6MlB-dj4RQP6PJE1IkS4mxnqyUhAthXnVru9UtxjBlK58lgLUnRYHsrzmTJ-RtlYFuW95zSFxmJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/618ee3ed71.mp4?token=LMOA89gBz_Fvd-n1rVdI_adtv6d_eb9GsutoX9-dPoqAA86S-jjOBu70_O7WzAY26IHaxaZ7qpeKUHKsh65R-8z_jhC7qtkRkLK1eNIKMa1WdaryGuk8ygt1id5V0H3mlGxPMj3V6iTT_AHynHSaAjPVFbRTujGtbkolw5ky18h9Cj95CBSLyNr0n-9RFnEjjriNS4j_ggfSEU-zZDNBMaOvVao0Oy_Fw45lYWh8ORGScwNcEdSHOg_3CbidZVwYKxh7wsEzXN6MlB-dj4RQP6PJE1IkS4mxnqyUhAthXnVru9UtxjBlK58lgLUnRYHsrzmTJ-RtlYFuW95zSFxmJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حشود ضخمة جداً من المعزين بانتظار النعش في كربلاء المقدسة.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/81805" target="_blank">📅 17:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81804">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGy9hTwFJcCfnCLzcZZVq6jK7Mr6lJfZn-owbB8TEQcyeGMgeXcksSYINOA--_oQVf2hWK9P4ujnb9Ol0qxTAJOYLRzYvpxsXkLhpOh44vktVG5wJaVN637juEUyqJ3OSH-wjiDudEyK3yrCbQdl80lIA2vAfXU10AqGwNsKxMtw_AZLG6MQZIod2PoMzcaycpvSEOxll18kOP1E6zg7EzQ69WgMiQwHO4tglcPapH5gu0K1X9jZOtJX1dMblb2c-1a2LnWJp67rh3BQjh6mZ4Sj5vDoUsFn0G6hIYbelcrup7wYmwvbPUKv-cBOrVCH3bGbATiybUvtjQMSih5iSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الأمين العام لكتائب سيد الشهداء، الحاج أبو آلاء الولائي، ينتظر وصول النعش الطاهر للإمام الشهيد السيد علي الخامنئي، قدّس سرّه، مودّعًا قائدًا ووليًّا وقدوةً.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/81804" target="_blank">📅 17:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81803">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">وصول النعش الطاهر الان الی سيطرة 52 عند مدخل كربلاء المقدسة بالقرب من المطار</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/81803" target="_blank">📅 17:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81802">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UyiBo7IKGFyeTiZebO01glEEir-eJ99IIB7SzYFCR1crIw1sIt_wd4PxtzlxVSHuaYS37FHZQCxl_lvCP_yi7cX41znc2txj78MPkbYA6iAGm5GTaNE9tnuJtwC3emdSLDcgbuD-3Z_HnblfreUa_WQxWpBG0B-tIk_eeu_eTSFA1oDxxIi8_j0nQqm2KZBb8HrX-bUhqatU2DyggFkvFqgSGbIjgiSlFI8nureLQGy9kRy7y9qotGNqGZiW77HoWD0bqEsLqGwMmmFSdFrcEXxlip8YQv0o9ovgYkfAAHE_6EcDJpqaoq8mYDy0Eh5rJwTfZzko_IhGFc9rJnndzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجمعات بشرية حاشدة في الطريق بين النجف الأشرف و كربلاء المقدسة</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/81802" target="_blank">📅 17:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81801">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a39050c29.mp4?token=RkvbVKahx4ZT7njAcJ_rlChjwzdmPlzey5WwBATS5SblZBNVGKj83yQd5NQZWfs9rYGf1iUDY-EasWRkp9HpRC-C5DPGugc3RAe3jJVx0JbPuesx95aGzuSHcF23AuYYH8i418O-83yHIrUUDsxiFMOpHwY2Wq8TNM8URdBGQ-ilxVHzRpqy5GYy_93brCpbClQU8y6kZ3pE3UussI6VR0hoNgPw-bPWxufrhGd-CfIjXkcRA62no8j7aKBtC9Bf5Yeeol-662aicsh0gny_WT_B_9ZbvMg6OVu99Fu1e4FZkDJqkFlk1pPyZAtr5RFqM2ifXrJlQGvhGCZCskQKFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a39050c29.mp4?token=RkvbVKahx4ZT7njAcJ_rlChjwzdmPlzey5WwBATS5SblZBNVGKj83yQd5NQZWfs9rYGf1iUDY-EasWRkp9HpRC-C5DPGugc3RAe3jJVx0JbPuesx95aGzuSHcF23AuYYH8i418O-83yHIrUUDsxiFMOpHwY2Wq8TNM8URdBGQ-ilxVHzRpqy5GYy_93brCpbClQU8y6kZ3pE3UussI6VR0hoNgPw-bPWxufrhGd-CfIjXkcRA62no8j7aKBtC9Bf5Yeeol-662aicsh0gny_WT_B_9ZbvMg6OVu99Fu1e4FZkDJqkFlk1pPyZAtr5RFqM2ifXrJlQGvhGCZCskQKFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من داخل الصحن الحسيني الشريف</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/81801" target="_blank">📅 17:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81800">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">مشاهد من داخل الصحن الحسيني الشريف</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/81800" target="_blank">📅 17:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81799">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">موكب النعش الطاهر يصل عمود 367 في كربلاء المقدسة</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/81799" target="_blank">📅 17:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81798">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">حلف الناتو:
لن نهاجم أي دولة، حلفنا دفاعي.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/81798" target="_blank">📅 17:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81797">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">موفدنا : النعش متوقف بالحيدرية وهي ناحية تابعة للنجف الأشرف
بسبب تجمهر العشائر و أهالي الناحية</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/81797" target="_blank">📅 17:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81796">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‏ترامب: وزير الحرب هيغسيث كان معجبا بفكرة قتل قادة إيران خلال جنازة خامنئي</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/81796" target="_blank">📅 17:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81795">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ترامب يتراجع رسميا: يمكن للمفاوضين مواصلة المفاوضات مع إيران، سنرى ما سيحدث.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/81795" target="_blank">📅 17:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81794">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50d76304db.mp4?token=lcDN6MXcudFkDw3gaUavOc1OV1h-lOu82lnAHjoAF3UefVvAkKFi2r-ZevUxqYsjQOuyW7KPgTJ8GV-1HBaRdhN2RwXznBBL_CfCpHnUmuydQMZPbkbAOzI5yIxm8P4qr6iRqS7pyYEy_XZS_aHBYL4z7fIDG4E3Pm0fNg2fovAOI56PNm8Tg8YfyedI102gH9B4pvV2_u84080V-W5udUEZ2ZWwgVQw_-ZoQ2QBbtQb7qvKfFJQ0cPufeqSupk_1_IFUtm9D_iSTRIZgNmSCn3hz65LogWjMiNiqqx-yHG7Ez4YUcyMlw2Q-hKo-ABzLVSdDaxG4kjuhL26B5dVdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50d76304db.mp4?token=lcDN6MXcudFkDw3gaUavOc1OV1h-lOu82lnAHjoAF3UefVvAkKFi2r-ZevUxqYsjQOuyW7KPgTJ8GV-1HBaRdhN2RwXznBBL_CfCpHnUmuydQMZPbkbAOzI5yIxm8P4qr6iRqS7pyYEy_XZS_aHBYL4z7fIDG4E3Pm0fNg2fovAOI56PNm8Tg8YfyedI102gH9B4pvV2_u84080V-W5udUEZ2ZWwgVQw_-ZoQ2QBbtQb7qvKfFJQ0cPufeqSupk_1_IFUtm9D_iSTRIZgNmSCn3hz65LogWjMiNiqqx-yHG7Ez4YUcyMlw2Q-hKo-ABzLVSdDaxG4kjuhL26B5dVdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من السيارة التي تحمل النعش الطاهر وهي تدخل المدينة المقدسة</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/81794" target="_blank">📅 16:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81793">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">مشاهد من السيارة التي تحمل النعش الطاهر والتي دخلت كربلاء المقدسة قبل قليل</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/81793" target="_blank">📅 16:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81792">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc4620fbc4.mp4?token=HgndpbNSiI9okzAdbxjknUh8g_T1sMpIVBujoTINwIbSDny4HG2GFmvPBrcUUATb50w8nteQeHYZptVdfmdwNJIO3xLAOpjqQD0mSbZsdA-smxMnc7tGoNhcCw9xUpXZE4aIPVOXAlhqBC4sZErPmn1cxU2GPukenh5jLM-ceaZSMQ12jVwMjy4xYNKTcw7R22AtBjCv0gkZd-OUSlh3RjUUdPTiJFTCfURAnVy22GV50XkV1XsUKsCZc2eBQPK8kl-pe5t0nratnLu5iT0v_mmKVcz4tZ7WpPPZfpfhzzHw6h-y_nfgmMMVASUJGvdqxLbpSvyg7PZ3oFZ18Q41BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc4620fbc4.mp4?token=HgndpbNSiI9okzAdbxjknUh8g_T1sMpIVBujoTINwIbSDny4HG2GFmvPBrcUUATb50w8nteQeHYZptVdfmdwNJIO3xLAOpjqQD0mSbZsdA-smxMnc7tGoNhcCw9xUpXZE4aIPVOXAlhqBC4sZErPmn1cxU2GPukenh5jLM-ceaZSMQ12jVwMjy4xYNKTcw7R22AtBjCv0gkZd-OUSlh3RjUUdPTiJFTCfURAnVy22GV50XkV1XsUKsCZc2eBQPK8kl-pe5t0nratnLu5iT0v_mmKVcz4tZ7WpPPZfpfhzzHw6h-y_nfgmMMVASUJGvdqxLbpSvyg7PZ3oFZ18Q41BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وصول الجثمان الطاهر لمنطقة الحيدرية</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/81792" target="_blank">📅 16:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81791">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dfffea463.mp4?token=POBYe9ayXYf-5vYSeeNKQXjmpNFkTyTErrtmrncwuJ0ddfMOFKL883IbD6Ov_pTyf1LzKgvXNnZlXXFw16UWztAZaWfVZJ9u_odQbguQep4Dvpwc2RW6wK8yKuIJmjv7x-tfnQgUFOlGBh_yXCJN3xzFnTBLXP9nDxRhLVpKi7Jq4YhM5oQh5lP4zjz0nVgT0FWfCQRJfM4P--KfgMc_BuZcTYgFLFDw9tl1rMz5Zcos0Y4kA4KvgHZNSF_rdrv4Aiw3sCWIYT8jA343OHVvViNl-smswCFskxawz-bP6eGvKWIzc9vWAOXYZNK407GvmenG971xHdqDSxGsyy6ryHTytjb9SkbEs1Up7DUKURFj2yBAsLdy34oMC5zrFxfByNB7oO5brNToaqp6B4bq3LNVFCtJVq1mUHauMitvOqd8xXbwJjiSFZ54eaOfPOjoUKqk-Wv_FSXqR4TqqUz837IqMEkzLVTEYdnykm_vi19JiJMSVn_27TYLcwpYktspTNvbi-YHM41ylnd5Cnvm49KRkExosU436JXYGbf6QNKF03yc7A2Mu2pOZfe30FLYhOl2bQDQhPdJpSictUNr6IiBwvGlBJckrPsPfmw_BL7pPg8mHyZXPs7FW55qzFEXsL-TcSeasdOJyKQXWSBqf2RvY790rghkaq6BDSiAmBM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dfffea463.mp4?token=POBYe9ayXYf-5vYSeeNKQXjmpNFkTyTErrtmrncwuJ0ddfMOFKL883IbD6Ov_pTyf1LzKgvXNnZlXXFw16UWztAZaWfVZJ9u_odQbguQep4Dvpwc2RW6wK8yKuIJmjv7x-tfnQgUFOlGBh_yXCJN3xzFnTBLXP9nDxRhLVpKi7Jq4YhM5oQh5lP4zjz0nVgT0FWfCQRJfM4P--KfgMc_BuZcTYgFLFDw9tl1rMz5Zcos0Y4kA4KvgHZNSF_rdrv4Aiw3sCWIYT8jA343OHVvViNl-smswCFskxawz-bP6eGvKWIzc9vWAOXYZNK407GvmenG971xHdqDSxGsyy6ryHTytjb9SkbEs1Up7DUKURFj2yBAsLdy34oMC5zrFxfByNB7oO5brNToaqp6B4bq3LNVFCtJVq1mUHauMitvOqd8xXbwJjiSFZ54eaOfPOjoUKqk-Wv_FSXqR4TqqUz837IqMEkzLVTEYdnykm_vi19JiJMSVn_27TYLcwpYktspTNvbi-YHM41ylnd5Cnvm49KRkExosU436JXYGbf6QNKF03yc7A2Mu2pOZfe30FLYhOl2bQDQhPdJpSictUNr6IiBwvGlBJckrPsPfmw_BL7pPg8mHyZXPs7FW55qzFEXsL-TcSeasdOJyKQXWSBqf2RvY790rghkaq6BDSiAmBM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من السيارة التي تحمل النعش الطاهر والتي دخلت كربلاء المقدسة قبل قليل</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/81791" target="_blank">📅 16:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81787">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q80W8eJveBiw8GNRkqQ4s5cciYTGb5GvusBABm4psBfamwomq9fyT-EEu_-Q-3DrK9DVYnMS8yiaK63A6xe57HEoYHzxpHF5mYi-rvTTL7Re4MMX0jA5FVG3YTQGPftnsJqcLO2UT7FjBo5_WPk180suM0Tf-YpMVDfK6Y4a9FvHOEEmjRpeUQGRdkf24sO6j3jNFj9xqrrv1iCzb-gqb1ppHDrnNWQaubTLghPHBUkzC538Kru7UaVNdqX14tK0L6cFnU2ucuiVwSKB3tEc6L7SF1Qw09AifBWavSfzphMcyrCYl8Gg23w2QvxMRMexl2RX2p35DI0HDTf7w_HOSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hXGPvHDLJK8ySOVVIY1MKa7QHyjF8GfNl97mipXWg7cup9t2vijAZCpU4CmaWce4E9EOk-jS1WUtdwh26do0SVIh-yQLEB4FFq_YbB-0depc8uKmIJIR2jkEJJBKb4iHhGxgeujb9nKRj23c9SM2i5zU93HR3wUuQcqXTwyrVsnUx4e0pxSjynxda0PeUCpROurjc5NllxWj1uAn8_vcEBdvscvU9JANXLVjW8QFVx5Mct91bu4plc1Po_2STPrdBfE2mLVO3er7TyPpEqm7OtYSRijL8dkTdzsf4M2vNew1VQYOvNIz3s2nL-hKXMHd18rBdhl-4-P7ltclRSDnsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rPZYW8GARlXp-qSI_7xaJcgs6ECYCyOh4j6ahN2LtPTTd4kkbj_gTBdEF1P_uGMfSIAlR9oBs0KRuzNKK-VvMRvnIzQu8lp8tcTM9Vj9sSKuHBi6ZJAxGQ67XK1l5pIfr8qCGYPPfMowrOfLnWattR15jevbV9DpE10m_HqH4Kvwwpjg6GnVaTjofSfZ-Ok9sET_Gun0Cin2NJUHn4yPz9ieJP_FQwNdfDSHOY02ce8v6CoWxo6cCWnyNaWG4naIJrWQUEUkqfOxsoYcs3vATclNbf4-tgGo2YZOk5dhReV2GJLJqnpYEYl8KI5kVoZhO80fjNqIe6yRGIKZxKWWsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uL0cyMFUtGo3rnLMH4m9FoGva1YIPa-SS4GL0awLOZcRKWze8RtHXZJvf04IHgBCjM3IsxtF2PFBsNM6rTb0envw0VPrTKLq_sdheDeUDq7vnnEcjwibUvcQ0JrmW46M7ZNBFE_IZLSA1jmYeG4slO8ScJxx6OM6ZbxPmRGbiHkOMKJKQw2EuI34rijrhwdvs3FXbi0RfEre1D4UT59oxqrGufLIEXjaU6P1n0onfPPfq1bhLfp77FuqMRaJV5_uUvztGJ0UeX0msBynKjVdBenCWlXy3_Wj8R7EZRtzKfv0D55uxOn4FATL4d-r1NN1TOMA9F3INxQwOcsp3Q5CTQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">كربلاء المقدسة تترقب وصول النعش الطاهر الى موقع التشييع</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/81787" target="_blank">📅 16:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81786">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b580d54816.mp4?token=bIss9XroI1tM-ShWhDR1-A5M4Se_vNVO6MlimhkH492QqmJYVEpC1JvVKdg03zK5_F9fg0eJ8_jUCR_KZAy7y65kFhM8KTdLQLp0PAc_DKX1wtQnMvRKMgtf27Rb7zltK4bwx5W9EdjpNPNDrC4DF57utUy0ga1P-H8dadFQygK5PEVKATiXU3mvA3PyMPBUCO7XuVEYe1RM7NLxuDn76VgE6-jZiNREH1skBAsjz4RZalM3dDc3FYBOaCMDE50jIeggKzmOiQ1R1H-lI9EzoWpJHv02XzIYTH_Ru7d24yGXu4m_Q-TNqEurY0SDifjAvF9DV_ERNyzyI-QgidcETw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b580d54816.mp4?token=bIss9XroI1tM-ShWhDR1-A5M4Se_vNVO6MlimhkH492QqmJYVEpC1JvVKdg03zK5_F9fg0eJ8_jUCR_KZAy7y65kFhM8KTdLQLp0PAc_DKX1wtQnMvRKMgtf27Rb7zltK4bwx5W9EdjpNPNDrC4DF57utUy0ga1P-H8dadFQygK5PEVKATiXU3mvA3PyMPBUCO7XuVEYe1RM7NLxuDn76VgE6-jZiNREH1skBAsjz4RZalM3dDc3FYBOaCMDE50jIeggKzmOiQ1R1H-lI9EzoWpJHv02XzIYTH_Ru7d24yGXu4m_Q-TNqEurY0SDifjAvF9DV_ERNyzyI-QgidcETw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إغلاق حرم مرقد الإمام الحسين (عليه السلام) استعداداً لاستقبال جثمان السيد علي الخامنئي</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/81786" target="_blank">📅 16:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81785">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ترامب: لا أعرف ما إذا كنا سنصل إلى اتفاق مع إيران.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/81785" target="_blank">📅 16:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81784">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ترامب: قد نضرب إيران مجددا الليلة</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/81784" target="_blank">📅 16:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81783">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">كربلاء المقدسة تتأهب لاستقبال النعش الطاهر في موقع التشييع.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/81783" target="_blank">📅 16:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81782">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ترامب: الإيرانيون يتصرفون بشكل سيئ جدا مثل ما يفعلون ذلك منذ 47 عاما وقمنا بقصفهم بعدما استهدفوا سفنا في مضيق هرمز، لست سعيدا بما يفعله الإيرانيون والأمر لا يتعلق بتغيير النظام لكن لا نريد أن يحصلوا على سلاح نووي</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/81782" target="_blank">📅 16:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81781">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ترامب: الإيرانيون يتصرفون بشكل سيئ جدا مثل ما يفعلون ذلك منذ 47 عاما وقمنا بقصفهم بعدما استهدفوا سفنا في مضيق هرمز، لست سعيدا بما يفعله الإيرانيون والأمر لا يتعلق بتغيير النظام لكن لا نريد أن يحصلوا على سلاح نووي</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/81781" target="_blank">📅 16:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81780">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8046f9590f.mp4?token=gxDq6qvTSrmYushxQVR-j6hSOZwsDEEgbgr4di3xbeARrPUXDRHOPAf6iSHk9D3BCeJs6BiEBvgYRsGJDKpHtoRo73jtgM6c4mQAfX2wcy46tlbDySSmgzCjEnzejtfNJN4VNS0kGACLu-0OCxqeGpASLk40_xHxTpCaBVTMnDjkJGib5iKQkkQ41-z4XkA5g26d1ns_1bq4qvFNTxA0-V2aH2M_nqxGkXGTCbXio7bOZx2VJZTheWFgNkMhwZeskm9Yf1-K4GzuWQwlo5n78TkJ0M6KzY22CBKgmjkCuuEonxY6J1TEq4PiinnC3ec9LjsCejAXkGkujITQF-9FSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8046f9590f.mp4?token=gxDq6qvTSrmYushxQVR-j6hSOZwsDEEgbgr4di3xbeARrPUXDRHOPAf6iSHk9D3BCeJs6BiEBvgYRsGJDKpHtoRo73jtgM6c4mQAfX2wcy46tlbDySSmgzCjEnzejtfNJN4VNS0kGACLu-0OCxqeGpASLk40_xHxTpCaBVTMnDjkJGib5iKQkkQ41-z4XkA5g26d1ns_1bq4qvFNTxA0-V2aH2M_nqxGkXGTCbXio7bOZx2VJZTheWFgNkMhwZeskm9Yf1-K4GzuWQwlo5n78TkJ0M6KzY22CBKgmjkCuuEonxY6J1TEq4PiinnC3ec9LjsCejAXkGkujITQF-9FSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطقة بين الحرمين الشريفين في محافظة كربلاء المقدسة تترقب وصول النعش الطاهر</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/81780" target="_blank">📅 16:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81779">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6b194f5cc.mp4?token=ec9L581K1jALHtWcXtiJTXFELDlMhAbTreYfJs_EOOJSwnOOPSsqmS1x6j-RI0AsJC-VdDkw0EnRgnZYWzmfJ7yXRp1-MZOQHZ0cLginZyR2bawtQoQixpq3x8Y6tiWvn89jHmrwXtlNPuwX8AHhB1L3Wd3G_beYgvqNQHCpHJh3wI4GpQrp2h6AAFUotHI_4EXfhBPBEHlxbuEvcbO-KgMTVErKzETsyX5vJAq9x8RFTD9O73G0Olj1PzP_Ly8yESxpWfCTpEWtEAcBdO8xTfFFoSnzwV1gpvsRnHX6Jfo_gHAxRkz6WgqDoxIy7J22TsM_cQZcy6V_BTm1Kmrcerjlmb-SA_-X_R2m_EHT1pdWIUP1t_y-CZDe5PdykMB4sXxCx5ULoR6nCWr_NAKVV9ioY8yaetwPMlaUO2eESoDE_avwXeMP-9MVEVI4_3skAde5RxpyzCIF7VHsEv8lF5PD_ZUC21rRGIiEfFSgqZRm-UimVwXpTPoXE9JJWHWSXS3jzaufoEF1FzTC0cPUJh6gTM6coCrrdhOsZFlBrOcPXVZy00ebKpw9WlcxV_PxnwLEt66FQL0FaPBKSa77imKFT9oVmJN4bCsfmSAUvitJwysmA6lNDz716I7bcqiLbDJG-NPSHsOWFBa6UI26V3PXPkU__aVbebaosUpL4RM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6b194f5cc.mp4?token=ec9L581K1jALHtWcXtiJTXFELDlMhAbTreYfJs_EOOJSwnOOPSsqmS1x6j-RI0AsJC-VdDkw0EnRgnZYWzmfJ7yXRp1-MZOQHZ0cLginZyR2bawtQoQixpq3x8Y6tiWvn89jHmrwXtlNPuwX8AHhB1L3Wd3G_beYgvqNQHCpHJh3wI4GpQrp2h6AAFUotHI_4EXfhBPBEHlxbuEvcbO-KgMTVErKzETsyX5vJAq9x8RFTD9O73G0Olj1PzP_Ly8yESxpWfCTpEWtEAcBdO8xTfFFoSnzwV1gpvsRnHX6Jfo_gHAxRkz6WgqDoxIy7J22TsM_cQZcy6V_BTm1Kmrcerjlmb-SA_-X_R2m_EHT1pdWIUP1t_y-CZDe5PdykMB4sXxCx5ULoR6nCWr_NAKVV9ioY8yaetwPMlaUO2eESoDE_avwXeMP-9MVEVI4_3skAde5RxpyzCIF7VHsEv8lF5PD_ZUC21rRGIiEfFSgqZRm-UimVwXpTPoXE9JJWHWSXS3jzaufoEF1FzTC0cPUJh6gTM6coCrrdhOsZFlBrOcPXVZy00ebKpw9WlcxV_PxnwLEt66FQL0FaPBKSa77imKFT9oVmJN4bCsfmSAUvitJwysmA6lNDz716I7bcqiLbDJG-NPSHsOWFBa6UI26V3PXPkU__aVbebaosUpL4RM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طيران الجيش العراقي يقوم بتأمين مراسم تشييع القائد الشهيد</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/81779" target="_blank">📅 16:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81778">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">موفدنا في محافظة كربلاء المقدسة : النعش النقدس سوف يتأخر بالوصول ؛ الإنطلاق من مستشفى شهيد ابو مهدي المهندس باتجاه فلكة سيد جودة وصولا لباب القلبة مقام الإمام الحسين حوالي ٥ كم.</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/naya_foriraq/81778" target="_blank">📅 16:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81777">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇮🇶
هيئة الحشد الشعبي:
تشير التقديرات الأولية إلى أن عدد المشاركين في مراسم التشييع، الممتدة من مجسّر مستشفى الصدر وصولًا إلى صحن فاطمة (عليها السلام) والحرم العلوي المطهّر، مع احتساب الشوارع الفرعية والتجمعات الأخرى، وانتهاءً بمنطقة خان النص حيث تجمّع بضعة آلاف من المشيعين، قد بلغ قرابة ثلاثة ملايين وثمانمئة ألف مشيّع.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/81777" target="_blank">📅 16:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81774">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd0bf44c67.mp4?token=sVUu9JjntO-xZxc47ezfbmVlv2Pmdh-MVTFarGK8xiyOSzcBV2mK0r4eImMs4XzrMhTvndLsM_Z7XGCbltGaQUsVJcGmL6l5QACY7S4OxI-p1m9n26elDPfHEPERP770J1SPtTpEzOMQbGT20mOkGx0izLC6nnRVBekr8E737j5jtYhZiDbNISONT-8exW_vyOeYviklQstX7gu-8GltmdBMx5YQ1s98XFx_TEZpnHDrMvEzxGxHdD6wnwawDZLrQH8ggrTfFCPoavB4aYgeOwQ54T1zvhDCHzJeFmAV1wKMf3_ewfSy1V08VwW4Lh6lXmTaBMfNpFZssTugzXnFQG38R6YzKrvW26pLFqQzQbhgE_PUM-HkHXIo1odZaincsVoAFhW3hBhhTBGF0yN_7Qks_MD0O2JLocekTuZLUtLddBCWMCUkyg3fwrFpHFRWjXlqvZb4yNA0IsjCfmx6Chx228Oy0elCrO3V4mWrB0cwGJDFi8fY3IRDnGXY_53t8pr5gnrtjCgHKr8p4qAHkdeInKhOMHFRiN3GA5ckRVKFtPRBDPqqYF8FIJ8gfaALwGa3uAN6tAATIeSKNuyC8-wlYuehKTaXa6D3kmLi7HVtJs23ogaAaEk7RDTZJ_-ptSvcpe88boQa_UhVRHtJLkYDNsYfLnbYuWhF-SNO__g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd0bf44c67.mp4?token=sVUu9JjntO-xZxc47ezfbmVlv2Pmdh-MVTFarGK8xiyOSzcBV2mK0r4eImMs4XzrMhTvndLsM_Z7XGCbltGaQUsVJcGmL6l5QACY7S4OxI-p1m9n26elDPfHEPERP770J1SPtTpEzOMQbGT20mOkGx0izLC6nnRVBekr8E737j5jtYhZiDbNISONT-8exW_vyOeYviklQstX7gu-8GltmdBMx5YQ1s98XFx_TEZpnHDrMvEzxGxHdD6wnwawDZLrQH8ggrTfFCPoavB4aYgeOwQ54T1zvhDCHzJeFmAV1wKMf3_ewfSy1V08VwW4Lh6lXmTaBMfNpFZssTugzXnFQG38R6YzKrvW26pLFqQzQbhgE_PUM-HkHXIo1odZaincsVoAFhW3hBhhTBGF0yN_7Qks_MD0O2JLocekTuZLUtLddBCWMCUkyg3fwrFpHFRWjXlqvZb4yNA0IsjCfmx6Chx228Oy0elCrO3V4mWrB0cwGJDFi8fY3IRDnGXY_53t8pr5gnrtjCgHKr8p4qAHkdeInKhOMHFRiN3GA5ckRVKFtPRBDPqqYF8FIJ8gfaALwGa3uAN6tAATIeSKNuyC8-wlYuehKTaXa6D3kmLi7HVtJs23ogaAaEk7RDTZJ_-ptSvcpe88boQa_UhVRHtJLkYDNsYfLnbYuWhF-SNO__g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">كربلاء المقدسة تترقب وصول النعش الطاهر للقائد الشهيد للثورة الاسلامية</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/81774" target="_blank">📅 16:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81773">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">اعداد هائلة تواصل التوافد لموقع التشييع في محافظة كربلاء المقدسة</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/81773" target="_blank">📅 16:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81772">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14026246d6.mp4?token=Ra4eFTBKH2fFNwpCpmoNwR94oUYlUjCUaO0z40iJtFd6T-YdnwFXcz9wOWNUOP2RLH0UJlNXT-F0IyielWz5ZA1rY_C2p0lWQ7UujuXRtkDnA93VZStNP6LwkaevjO2R15EV8J0_hUfxx2Pw2bH5eOQPElnhe2JVaTUNMn2q-EHsvu7IQfSROmDo7giWScO0ApqU6WKacqFOB9LzZHLQJIEK2qkuiEvTIotBUC6mFhuIXo9CaGeGII8STXOB60lrQ0mIxs-FBzj1fokPOOJxbii-WQsn42ZXWQ9NJk5z6LxZHpV_RJ8cRKyjRu_3rQU3lKinx7qxaHudAW8cvdzffA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14026246d6.mp4?token=Ra4eFTBKH2fFNwpCpmoNwR94oUYlUjCUaO0z40iJtFd6T-YdnwFXcz9wOWNUOP2RLH0UJlNXT-F0IyielWz5ZA1rY_C2p0lWQ7UujuXRtkDnA93VZStNP6LwkaevjO2R15EV8J0_hUfxx2Pw2bH5eOQPElnhe2JVaTUNMn2q-EHsvu7IQfSROmDo7giWScO0ApqU6WKacqFOB9LzZHLQJIEK2qkuiEvTIotBUC6mFhuIXo9CaGeGII8STXOB60lrQ0mIxs-FBzj1fokPOOJxbii-WQsn42ZXWQ9NJk5z6LxZHpV_RJ8cRKyjRu_3rQU3lKinx7qxaHudAW8cvdzffA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فخرنا رجال الحاج ابو الاء من كربلاء المقدسة الرجل الشجاع والهمام الذي لم يسلم سلاحه</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/81772" target="_blank">📅 16:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81771">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef88af686b.mp4?token=VlO5YjS2mBANuCWf9fQOicJ70XI6bh1lF3wbm_YgCsyBP6wyWUIJBr6p5V_svg-YdIs4VQfGdpozyUfzbu6BIe8-2bHCcGo5e25YeSHk7ftPdqbWOY4i4kqmdVqHlFsx1WV3AlFIktcByyUxkSE5N1OXutVOCSDufC7KG-_shN4ogyoWzMkPW5c6WjYQ2NpW1426oV9Ea_X6Y3IxB1TcUsPUKewcVDt7BRrAuN1KahpSSx7cB6soIJ9kygPN9Q-tYTaesXw1B-wA1W6cklp4Gi4kvUllwZpFPHqkPJp-6voSPkgypMf3BRZx8AHPvDChp-bz9Evy__dBXFRBDJiWpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef88af686b.mp4?token=VlO5YjS2mBANuCWf9fQOicJ70XI6bh1lF3wbm_YgCsyBP6wyWUIJBr6p5V_svg-YdIs4VQfGdpozyUfzbu6BIe8-2bHCcGo5e25YeSHk7ftPdqbWOY4i4kqmdVqHlFsx1WV3AlFIktcByyUxkSE5N1OXutVOCSDufC7KG-_shN4ogyoWzMkPW5c6WjYQ2NpW1426oV9Ea_X6Y3IxB1TcUsPUKewcVDt7BRrAuN1KahpSSx7cB6soIJ9kygPN9Q-tYTaesXw1B-wA1W6cklp4Gi4kvUllwZpFPHqkPJp-6voSPkgypMf3BRZx8AHPvDChp-bz9Evy__dBXFRBDJiWpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعداد هائلة تواصل التوافد لموقع التشييع في محافظة كربلاء المقدسة</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/81771" target="_blank">📅 15:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81770">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">تنويه هام
جمهورنا العزيز النعش يصل بعد ساعة إلى ساعة ونصف لذلك اقتضى التنويه</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/81770" target="_blank">📅 15:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81769">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bf0fc8628.mp4?token=s9eB24ymKq-JAfSICLMIe7l7rhdZZgFGlNFhMtIa4tStLv3sz0dHgaE1xMdrYiYYuU-a6pj53s07i3Vo6ku2hXJiqoFZw3h2nsfx8raY9dJBeDJv0_jFmptF0nnWLtV93Jg1px7L_5J8zf0MNwTt6trbKNvJSEBD66250ZCQg-2_m--Vo8NUYKZgocxIHGm4qzb-5zkil3ck1GZAGlKZIC9twHtyR7JfCnU05INvfR4Hx-SBCgWxnLyWvSXEJ-49fJIh2wmMFi6GDfTnBEHnuDMQ9gf9BMDYr6z9IOQ1Yfhh0JTtC0GEe_2fUXLLd1n20ViXQSwYBQsnamG4gvxbmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bf0fc8628.mp4?token=s9eB24ymKq-JAfSICLMIe7l7rhdZZgFGlNFhMtIa4tStLv3sz0dHgaE1xMdrYiYYuU-a6pj53s07i3Vo6ku2hXJiqoFZw3h2nsfx8raY9dJBeDJv0_jFmptF0nnWLtV93Jg1px7L_5J8zf0MNwTt6trbKNvJSEBD66250ZCQg-2_m--Vo8NUYKZgocxIHGm4qzb-5zkil3ck1GZAGlKZIC9twHtyR7JfCnU05INvfR4Hx-SBCgWxnLyWvSXEJ-49fJIh2wmMFi6GDfTnBEHnuDMQ9gf9BMDYr6z9IOQ1Yfhh0JTtC0GEe_2fUXLLd1n20ViXQSwYBQsnamG4gvxbmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعداد غفيرة تتوافد الى كربلاء المقدسة للمشاركة في تشييع قائد الثورة الشهيد</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/81769" target="_blank">📅 15:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81768">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edb89f2c55.mp4?token=fOkl8ZLTAJodK5n6jcjme6LAopJ4Vd6QPmf-EssX_InGCfcruKM4GRxnsVqp3O6OoIc_QFrQgM7T_sneCnYlkNsgmIsGBHe6Fwe-20KOdH75gM9XZOfvenmOj-6_b5FUTExAOUKCiTEehf5Khpak_wpUGXQhKoX1Kun4LSxV876USegP6zJYSPdDSVYazT_LpOfDnPXrDBR_tHq3bdE_bHVVtiwlXpaSvfxKvF1ejdW9PuridUfDCJtJK3GMlWzGzeF2Sc6UiSsF5OfAYfzqreP3FJG_8b3bRHrqiaeyDvKPsjBkL4TCeNWzHQ5o20AdyUyHYJAEGj1YMW_XVZT4_44_pfOh-VD8Rt_vtll1LhJXQW1bzUzbTYoVCvmDPCPcfWKnlleVLlWmY4GI9KmxS1EZC6-K55wySJkHgiHGiA_XCth_W6enUJTPb-X1MjiE2azerkilkD25qVONFc1VmXwii-c5dpXVfVlMnA-RcrZ6rEVoV2FkIrtNLowRGBaXM2YcCVG1fxg1O2iyEYQS6N1sLBtL6A_n_0qfNXhLtZVutYUjCCEbPwhYOj-gGWN__WMaEbaEYe16uwvh6LGL7X4Gv36z3VsggxyWY6NH_k6jGZPhh3rVkdUOIyrpJj7FK4vUKZZMZeducAU4aYu6FNhhePrGPA6gk4Hgg4N-LxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edb89f2c55.mp4?token=fOkl8ZLTAJodK5n6jcjme6LAopJ4Vd6QPmf-EssX_InGCfcruKM4GRxnsVqp3O6OoIc_QFrQgM7T_sneCnYlkNsgmIsGBHe6Fwe-20KOdH75gM9XZOfvenmOj-6_b5FUTExAOUKCiTEehf5Khpak_wpUGXQhKoX1Kun4LSxV876USegP6zJYSPdDSVYazT_LpOfDnPXrDBR_tHq3bdE_bHVVtiwlXpaSvfxKvF1ejdW9PuridUfDCJtJK3GMlWzGzeF2Sc6UiSsF5OfAYfzqreP3FJG_8b3bRHrqiaeyDvKPsjBkL4TCeNWzHQ5o20AdyUyHYJAEGj1YMW_XVZT4_44_pfOh-VD8Rt_vtll1LhJXQW1bzUzbTYoVCvmDPCPcfWKnlleVLlWmY4GI9KmxS1EZC6-K55wySJkHgiHGiA_XCth_W6enUJTPb-X1MjiE2azerkilkD25qVONFc1VmXwii-c5dpXVfVlMnA-RcrZ6rEVoV2FkIrtNLowRGBaXM2YcCVG1fxg1O2iyEYQS6N1sLBtL6A_n_0qfNXhLtZVutYUjCCEbPwhYOj-gGWN__WMaEbaEYe16uwvh6LGL7X4Gv36z3VsggxyWY6NH_k6jGZPhh3rVkdUOIyrpJj7FK4vUKZZMZeducAU4aYu6FNhhePrGPA6gk4Hgg4N-LxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعداد غفيرة تتوافد الى كربلاء المقدسة للمشاركة في تشييع قائد الثورة الشهيد</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/81768" target="_blank">📅 15:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81767">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">الاعلام الغربي عن مصدر: ترامب لم يؤكد إلغاء الاتفاق مع إيران خلال قمة حلف الناتو</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/81767" target="_blank">📅 15:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81766">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">البنك المركزي العراقي: تحديد سقف الحصة النقدية للمسافر البالغ بمبلغ (2000) دولار أمريكي شهرياً بدلاً من (3000) دولار، وذلك في إطار تطوير إدارة عمليات بيع النقد الأجنبي</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/81766" target="_blank">📅 15:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81765">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/613440993d.mp4?token=uDn75JKdbGoRmAweANdeainHcm5Vdwh0nEeF6yr1Tpniz_SK39cfsf41-MKlANIvlMzbiAbH9BFIMPwUftvmXCE7F6FnsNj8LHCFJR1NXzng2nXVBf7Q7xVB73v2_rLr7SRCFkX3QI30E6MGPMS0t3idSA6PVVQcDNVZZ1ONo7-tnb8Hw3DrmlMlpcbnKHbfTjvToo2GTWikzd4UnDafNY0eeXllDXKHKfsJzrwdffNV-lOzhRNlXZ47q2KC34Ro7NikdG9gBNY21hZGYQOpqKXapPNWyufhKP-IJmQhnueS9WoYVzYFt_SdswYgT2fT6CMtlQG-xx4ZQhjzdPD284WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/613440993d.mp4?token=uDn75JKdbGoRmAweANdeainHcm5Vdwh0nEeF6yr1Tpniz_SK39cfsf41-MKlANIvlMzbiAbH9BFIMPwUftvmXCE7F6FnsNj8LHCFJR1NXzng2nXVBf7Q7xVB73v2_rLr7SRCFkX3QI30E6MGPMS0t3idSA6PVVQcDNVZZ1ONo7-tnb8Hw3DrmlMlpcbnKHbfTjvToo2GTWikzd4UnDafNY0eeXllDXKHKfsJzrwdffNV-lOzhRNlXZ47q2KC34Ro7NikdG9gBNY21hZGYQOpqKXapPNWyufhKP-IJmQhnueS9WoYVzYFt_SdswYgT2fT6CMtlQG-xx4ZQhjzdPD284WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعداد حاشدة في محافظة كربلاء المقدسة تنتظر وصول الجثمان الطاهر للسيد القائد</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/81765" target="_blank">📅 15:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81764">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13a42e7b63.mp4?token=QG-jjGpj-hmUKYFdelHlHtsugk3oJKkunOOLlOe16Hjm9m0aKfnbVVzD5x4OS1xZqfydYCQcG6DQqAcvHjzv8zoRYyjFWyXw0Qs864xx_WbLqcNAm1WaSLFnm2_SCmKpDZdufoteapGTDMJ7EwQm5_4D_kG87ko4Urz5WjPZ6ewg3HjhcCcGINnNZlmEP4F9SH_oFrSsAoEpV27LSsuMjGM1AhFcsTMJOmR79Vb1fZZwKtObrSg0Zpr5XMqi_SFBLJdhJsD3YpyyjPHZEH38X0zXCwCi5E7ZxNx76_v5HNgCzUmEGxpcKXtXXLnIsbdoHmru4KLh3unhoTKgu4D_6TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13a42e7b63.mp4?token=QG-jjGpj-hmUKYFdelHlHtsugk3oJKkunOOLlOe16Hjm9m0aKfnbVVzD5x4OS1xZqfydYCQcG6DQqAcvHjzv8zoRYyjFWyXw0Qs864xx_WbLqcNAm1WaSLFnm2_SCmKpDZdufoteapGTDMJ7EwQm5_4D_kG87ko4Urz5WjPZ6ewg3HjhcCcGINnNZlmEP4F9SH_oFrSsAoEpV27LSsuMjGM1AhFcsTMJOmR79Vb1fZZwKtObrSg0Zpr5XMqi_SFBLJdhJsD3YpyyjPHZEH38X0zXCwCi5E7ZxNx76_v5HNgCzUmEGxpcKXtXXLnIsbdoHmru4KLh3unhoTKgu4D_6TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قائد عمليات الفرات الأوسط حشد شعبي اللواء علي الحمداني يوجه نداء لقطعات كربلاء المقدسة استعداداً لاستقبال النعش الطاهر</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/81764" target="_blank">📅 15:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81763">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">طريق تشيع السيد القائد للتوضيح في محافظة كربلاء المقدسة</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/81763" target="_blank">📅 14:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81762">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">دويلة البحرين: تصدينا واعترضنا عددا من الاعتداءات الجوية الإيرانية الغادرة</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/81762" target="_blank">📅 14:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81761">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c49d1f85a2.mp4?token=SZLTSA66RyIHNsfggOOXX-9witX3GQgYA8bQx8jB9oDmQlpdE_QU7WYC1J5oEtFO7AAenxOxJwbtXfDxE-JAsVzzysfFg9tGjhAo4JDLFcxPH1XkZD7AsgC5jER4D3E0FzgDqu9KNH2iN5caR7L-_TxeszRdv22d45OotVGHIkPu_B8q9bZ74ZyFvqaLJWnTnDVBygURXPIZTtjrPXFvtYC_Gma-iiUbdnQWZMsdB0eM3vWURbxPza83CrFx8PuCN-wpligLQ8ORcMQSCzLcDVo_WybLrjQreO0j3NqJQ1HTT7hHPbCMdXTCug1wuYVqfegRd6F7jTSMZP71LYTEWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c49d1f85a2.mp4?token=SZLTSA66RyIHNsfggOOXX-9witX3GQgYA8bQx8jB9oDmQlpdE_QU7WYC1J5oEtFO7AAenxOxJwbtXfDxE-JAsVzzysfFg9tGjhAo4JDLFcxPH1XkZD7AsgC5jER4D3E0FzgDqu9KNH2iN5caR7L-_TxeszRdv22d45OotVGHIkPu_B8q9bZ74ZyFvqaLJWnTnDVBygURXPIZTtjrPXFvtYC_Gma-iiUbdnQWZMsdB0eM3vWURbxPza83CrFx8PuCN-wpligLQ8ORcMQSCzLcDVo_WybLrjQreO0j3NqJQ1HTT7hHPbCMdXTCug1wuYVqfegRd6F7jTSMZP71LYTEWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الأمين العام لكتائب سيد الشهداء الحاج أبو آلاء الولائي يصل إلى المراقد المقدّسة في كربلاء المقدّسة للمشاركة في مراسم تشييع الإمام الشهيد السيد علي الخامنئي قدّس سرّه</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/81761" target="_blank">📅 14:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81760">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">منطقة بين الحرمين الشريفين في كربلاء تضج باهازيج العراقيين قبيل وصول الجثمان الطاهر لقائد الثورة الاسلامية</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/81760" target="_blank">📅 14:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81757">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JeKH_sEHvtQjIU2p-u7WHiGcemQmD6zXIliznQ60CiONGKY8HISc-JpgMkoweod-izPHkNUImTUCcgSXg0_wrAo98xw06_N-y335ScJm75enG9v74N7yr7Ixfcx3_ZB7z3F1MJjUgKc0fCXvERGLIhyUe9xnKoewX4-5IjUfZH-_UQ3rZxPTe-8Qu1sCHbdxYjUGabuuMqE0YT84MO-hSlLNYD2O1IQT72XxxEcIxgJwaCxNck8iAbu5V2PYxdgml0lfCt6MkyUl8LOPTvAByZa-MWvx0DW1bBiWpgPJACJlse-k2GUP9vL9h8vmweosSq0fa-JB51pARWBaA_0scw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fDhMoJ0FB7XWri5U2fFpWYMjHsPFFtTRSDC3DWrhBeuUCgyAC91WaXxuUSfCCTFtdvP7WsN3kpnNoMxT8YEZVfqse1OlNkDgcDWSr0-IRDfEG6UGTTVZv-bhX7VGDMK-KA9g6jaaIizJxhLr4AmdP6Lkt7aX4HLfOOG7ssoZpaeSWFWd8EzH0mAYl0E4JnStGxjqmPd5qLMP5r-dFazuLgxnF3EAvM3L6VvbwQyk4gW5EIBbusGiSvf91ZOSuESkk-HrQyIluU5ceQt1DO1V2GPjsVVPYi-xXF6MA7THKphkSw1Mk6JwaxDSYp36Ah42zGKatePbVmZOfA0wtdbSsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E9vp9tnUif2Dhze2WERuwOfdQbQcPtcb34phgOgogiuIkPckx1ZsXc-pvP5yivSHsmxE47CdHgVfVfIVvCfTC-9cpbW2U0oEvSMFmIorF5MANxHHFYdIDDVXB5VtKoRzde1sgwYUij01CV4svbuQ4wiKADkXrGiM0i901ZZw4dk-e_uL9mc3V0BFZp02hYPYQy0xTqeGzAoF8mLTzz5NUAMG7wHJcGgobt2FkHWhdAe3M3Sjjq6KXqorBpC79jJRyoRVzSe2Ul9cdzdcfc_O_0r1biFIk-11DT7amDFWTGLUTZO66wp7TSFiFL8ivK8SH68-sbHj1zBy2wlMRlFK7w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صور من عدسة مسيرة
خاص نايا _ تشيع السيد القائد 2026</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/81757" target="_blank">📅 14:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81756">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64551946c5.mp4?token=eqVDl51MENcmF2p4DO_-tgN8IzzLtIxh4mANhMN64KEe9KnAEAsHB6z8R1XfCeXWfIbtriHhNEKwkVTMUTwc3XpGNcyTjaBcv0UfymKhfY7zRtMeAhPOSG9namrk_OMApUPZfkO3itjokxEa-4_nyvblyM0zGtNjxIt9H9YQNsBglFeWFR3haS3hTi3WTMhM3Xx02p1xntypXlUmDkuK5aOwu-ESQ3-2zjvp3HonpvP-h_UA2Goe6qEhHYx3a76Fu_ApTYdfwqCV06atYlBobHJoRO5w5fGBgBRcjVcDhTq-TNzTu4wKaqN5dGSR8BCOGjKa81B2RVnoic_nzfaCaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64551946c5.mp4?token=eqVDl51MENcmF2p4DO_-tgN8IzzLtIxh4mANhMN64KEe9KnAEAsHB6z8R1XfCeXWfIbtriHhNEKwkVTMUTwc3XpGNcyTjaBcv0UfymKhfY7zRtMeAhPOSG9namrk_OMApUPZfkO3itjokxEa-4_nyvblyM0zGtNjxIt9H9YQNsBglFeWFR3haS3hTi3WTMhM3Xx02p1xntypXlUmDkuK5aOwu-ESQ3-2zjvp3HonpvP-h_UA2Goe6qEhHYx3a76Fu_ApTYdfwqCV06atYlBobHJoRO5w5fGBgBRcjVcDhTq-TNzTu4wKaqN5dGSR8BCOGjKa81B2RVnoic_nzfaCaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الأمين العام لكتائب سيد الشهداء الحاج أبو آلاء الولائي يصل إلى المراقد المقدّسة في كربلاء المقدّسة للمشاركة في مراسم تشييع الإمام الشهيد السيد علي الخامنئي قدّس سرّه</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/81756" target="_blank">📅 14:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81755">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6a2f95c28.mp4?token=gC41a6XUB2exkYhshfZTeLbNYhHhlMpORH7fRBDxNvVeDyVtNR08mQMZaNxyFz8Y7DKyG-mxMfoVfjXtb49XangzaPmPTDslBMwmyQUBnos_mZ1iYeNGmUBMNhw6w1NoA0G9CrN0AxLiGAIuGXe6itU3NxPWOol2TGXfcSS6z7_qkX2zAYv4MXzwW2WO6h4tM9WhDQnlhEfOKvYbF7wm8sOMeL67EzNhzerJ8tt6rsbLi3wVAEjnkKjnNw_w1M_Wfl522wnwxeb_gH3b7-MFzCMHdMEgPET_88PfeFII3xdHDnsBOUSePhSD8up_C38vB8SfA-HAom4FK2zFTx52Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6a2f95c28.mp4?token=gC41a6XUB2exkYhshfZTeLbNYhHhlMpORH7fRBDxNvVeDyVtNR08mQMZaNxyFz8Y7DKyG-mxMfoVfjXtb49XangzaPmPTDslBMwmyQUBnos_mZ1iYeNGmUBMNhw6w1NoA0G9CrN0AxLiGAIuGXe6itU3NxPWOol2TGXfcSS6z7_qkX2zAYv4MXzwW2WO6h4tM9WhDQnlhEfOKvYbF7wm8sOMeL67EzNhzerJ8tt6rsbLi3wVAEjnkKjnNw_w1M_Wfl522wnwxeb_gH3b7-MFzCMHdMEgPET_88PfeFII3xdHDnsBOUSePhSD8up_C38vB8SfA-HAom4FK2zFTx52Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عشائر خان النص بانتظار نعش السيد الشهيد في طريق نجف كربلاء علما ان درجة الحرارة تتجاوز ٤٥ سليزية</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/81755" target="_blank">📅 14:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81752">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SQDqYXKLqW6HbELMh1P8ByyduYVCVZssQ57Kyz6yrE8h6XQV5i-z0hha2f0rwndSKlojA3dlI6oqLRmaCfKt7AKMbej9GIML9e-LVAHN8AvozlJ16Ctac1DeufunhnFOaoSNGGi_OndKnI1zcbo2AEpuvC6B-2rmpbjUTWNdtYe9eTO4cy-ADDHxBA1CzWoAwfectMbBshRxmlQ1B2ezYOjDZ8SfeBdUa_qUJZzbjYgLVbfaodTh-LSIZEBH_fV29hhVcrTs2DzrRQTgAA3WwLrmOqMaiznfp-CKBzop2yle0TfD_grMv5e747-qNWZ7FtvE8wbcsnHHbt6LmesROg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tjfDA-Eo_akXKz0_Jq9TlTWw3ifr4-f1dSVCQF6OgZlE5AuW3pClDnAUeySDRrq-ggu_yEos3CTo1vDLYdBmXv3ckara1FkSifbZNZdNoVJWmSUsl_ysz2zhkohXM89nGozti_NsXTHGMxg2MtV0b7c9jBLes0Q9TR71soVC-4RfuQGvnlbVG2mVenaHGSro_Fli3XR2IW6zFIP9IfluoeJSgz02VPmD9QBoVbulK3Ur4PrwQZkYoWvu4YZjtbK0bBBK7JgHv0pTXSplhQLo3552Vc_C6d6miCUsrPBLhBQGFhpjMGujRCYwoFv4bh4IU1bK2bR2UTfERhlY2GajgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dTthO201aJvR7sWyMoK0nXf9ddZwz7LXsUTWNGW5n8AksG2EvMmdWilZf8OBwhqZBofRVhUAxmXV9l2TSVWEHUFeFDMvFEUmXh0t-ki1bJnGSKBZzcTeLoJSMA7cBX8unj73J0CDvIZXhxhNlZVMxPOzy5qVrZDa3CJ_Lhcxndd9grNRLy7z-aXzgmrBBNg4sbRrvRuq2L1uqp1nDNUqYuwRiqGSUkrwv2U7IpSKfV-tJE4vcc9p0Su8NyayeNGNBFtlP4EuT5GqKb25HfPkqpaSOqP1YGb8BdJiyqLgjanjl1ZW1YqIZAL82-X3QyrM6f6nZTtA2iuIPlKfrbY-sg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Inside Hthrat imam Ali drone Picture Mavic 4
Naya team</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/81752" target="_blank">📅 14:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81751">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">Naya drone over Alnajif city
1:00 Baghdad time
8 July 2026</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/81751" target="_blank">📅 14:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81750">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/30da01e5e6.mp4?token=ZAE3zTBjcljRtk_5wT00aiByneGCySgyx1cXp6HC7Paaaq3IHXvaVMY4xyYSzLRr3JA-kSQUzHXvaBS68vlqZN9sMlFZ4ic1i3UL0xn6OPpOCMZ-9ShgRlmfX3I85Hn4qWa1KHaAU2vRJZXjDXLiSWmpJI_K-VyAYaN2IR5ZIhWKZtKPVf0y0TvLrqnPXhMaAu7QrHrYDSyZlA5f0EWcnqwJVl9DckKuMtbYjSarQSV-FvW3u-Y8rcp1DKlhvUfHw9tuQT3QC3GyB8sEzpvPCMrszRmj9S2HF32ZcNmluyNvYd8Jog8GJQAvTDz_2lcu29eRQ1NUZHolOvq6qDAVMg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/30da01e5e6.mp4?token=ZAE3zTBjcljRtk_5wT00aiByneGCySgyx1cXp6HC7Paaaq3IHXvaVMY4xyYSzLRr3JA-kSQUzHXvaBS68vlqZN9sMlFZ4ic1i3UL0xn6OPpOCMZ-9ShgRlmfX3I85Hn4qWa1KHaAU2vRJZXjDXLiSWmpJI_K-VyAYaN2IR5ZIhWKZtKPVf0y0TvLrqnPXhMaAu7QrHrYDSyZlA5f0EWcnqwJVl9DckKuMtbYjSarQSV-FvW3u-Y8rcp1DKlhvUfHw9tuQT3QC3GyB8sEzpvPCMrszRmj9S2HF32ZcNmluyNvYd8Jog8GJQAvTDz_2lcu29eRQ1NUZHolOvq6qDAVMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرس الثورة الاسلامية ينشر مشاهد من الرد الايراني على المصالح الامريكية فجر اليوم</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/81750" target="_blank">📅 14:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81749">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">‏المنظمة البحرية الدولية: 6000 بحار ما زالوا عالقين في مضيق هرمز</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/81749" target="_blank">📅 14:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81748">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">كربلاء المقدسة تستعد لاحتضان الجثمان الطاهر للقائد للشهيد للثورة الاسلامية</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/81748" target="_blank">📅 14:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81747">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">اللهم إنا لا نعلم عنه إلا خيرًا.
مقطع فيديو كامل لإقامة صلاة الجنازة على جثمان الإمام المجاهد الشهيد آية الله العظمى السيد علي الخامنئي بامامة العلامة آية الله السيد محمد تقي الحكيم في حرم الإمام علي بن أبي طالب عليه السلام.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/81747" target="_blank">📅 13:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81746">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8dd49b252.mp4?token=aAORy2QB-wt0tM_qh-UVn-mU7ToN_bAGIqeOX97_fFAVfnjtsYv4yrUxzEXhHAh2QPG9qoPr92QKHheGWHXCG-flXgL1XQXtFVnM6OyeR7zqnjqThCvpIbgdj1Mqknsf2u2geID0aVQfrWWyIJxFIswyhPnFG8Q2Ab-bkonS4aUuc8_U1h6GfGu-_7lmMDWUZSVNJh422f5Htm0Dmy7Fn-mCIxh_W6Kn50ZFAWSar7k621N41hBgBGimEP2IAZ8_0rTfgNffIqLiXYAkKJlgfUGBhHN5J-_HaSSkuuxcCpRfCmVeCLMbcgoL-dZpvrCVHICqTuQGio3b-ns26N_Fk0c-Cizb7GLhv4mCWQLopEj78yGW8niTnD72WSUnXng3x-V5h_NVffV_iU55O2jFE8EnO2r4dMHZHL8TU10hNb0pQBPWH8BouNsqgcar_iU7WP5k1soxxqRjSO4ASwD36QFbMnlSbZsxmY6SjaW2jbNSzwantTAh6jxeTggTLuf5ZExwGAO-PM_jdLImmci2O5pcqqgRESqhFQPDmwRiU5u44JvY86kkkIE4PWY-doFAL0UHJ_ZfbPV1LEi0Vadxwjb2f-xrk0vboB1MI6A8KJMhuVLuYl3lfoprtx6-YJlLM1v8wynhlQC3Zjxd6DS97dEBlcyliDntMbzAAGqfC-0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8dd49b252.mp4?token=aAORy2QB-wt0tM_qh-UVn-mU7ToN_bAGIqeOX97_fFAVfnjtsYv4yrUxzEXhHAh2QPG9qoPr92QKHheGWHXCG-flXgL1XQXtFVnM6OyeR7zqnjqThCvpIbgdj1Mqknsf2u2geID0aVQfrWWyIJxFIswyhPnFG8Q2Ab-bkonS4aUuc8_U1h6GfGu-_7lmMDWUZSVNJh422f5Htm0Dmy7Fn-mCIxh_W6Kn50ZFAWSar7k621N41hBgBGimEP2IAZ8_0rTfgNffIqLiXYAkKJlgfUGBhHN5J-_HaSSkuuxcCpRfCmVeCLMbcgoL-dZpvrCVHICqTuQGio3b-ns26N_Fk0c-Cizb7GLhv4mCWQLopEj78yGW8niTnD72WSUnXng3x-V5h_NVffV_iU55O2jFE8EnO2r4dMHZHL8TU10hNb0pQBPWH8BouNsqgcar_iU7WP5k1soxxqRjSO4ASwD36QFbMnlSbZsxmY6SjaW2jbNSzwantTAh6jxeTggTLuf5ZExwGAO-PM_jdLImmci2O5pcqqgRESqhFQPDmwRiU5u44JvY86kkkIE4PWY-doFAL0UHJ_ZfbPV1LEi0Vadxwjb2f-xrk0vboB1MI6A8KJMhuVLuYl3lfoprtx6-YJlLM1v8wynhlQC3Zjxd6DS97dEBlcyliDntMbzAAGqfC-0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نعش القائد الشهيد يتجه لضريح الامام علي (ع)</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/81746" target="_blank">📅 13:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81745">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">📰
‏
رويترز:
هجوم بمسيرة على ناقلة نفط لشيفرون الأميركية في البحر الأسود</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/81745" target="_blank">📅 13:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81744">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">نعش القائد الشهيد يتجه لضريح الامام علي (ع)</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/81744" target="_blank">📅 13:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81743">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">انتهاء مراسم تشييع السيد الشهيد علي الخامنئي في النجف الأشرف</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/81743" target="_blank">📅 13:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81742">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gGWeGzS6BJFqLa9AlrHmgZZY0A1Ljaw27Bw_3x1xh48Ptq5JFV0QJQRWh8HaxC3sVUXMmX1cKLV_GJ0bYsSDeF8PwRXLJh_wzUnVZ46T2O5r6cZMb_PuWjtw4vYNx4CwQhNeyrQ6GTOzRlMips6UykMANN81BTA0e4EuhUQtOAaJnmURedJH7xWCjCHbfepVqk9vy5kYFrsqQCo8DqHcjex2SA2bRSQUye1rIY8Zbln_AIYI45qed9QrO6nvcMvVXKeUw0KCJRHgqr8BMz_W3eTLe0vdDxWmPg6v0_mahZhUrVP_IYb15ftytJOTHQUSbws-qm9SHkKf8vSRdR5AcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🇮🇷
النائب الاول للرئيس الايراني:
التشييع المهيب لجثمان الإمام الشهيد في النجف وكربلاء، هو رمز لامع للأخوة والروابط الثقافية والدينية العميقة بين شعبي إيران والعراق. أتقدم من أعماق قلبي بالشكر إلى المراجع العظام، والعلماء، والطوائف الشريفة، والمجموعات والتجمعات الشعبية، والحكومة العراقية الموقرة على هذا الاستقبال المهيب. هذا الرابط المقدس لا يمكن أن ينقطع.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/81742" target="_blank">📅 13:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81741">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03147dbc51.mp4?token=efRpTbfciUYY--rkULQsWh3OXpyGW1YVp9wCfxjIc8zd-qx6TT2Mb-jAdaeD0gJ7XLeAd8jCjZ-2n61KmGb_V31zxb9QLgXE6nIbpR3m1s6mb2Ks1TBPK66dMYsYPt0Nkc0VaslgWd_EXUPGT0eEKnApUXvAASewPnzrkPwF3PWZZyyYyThKrhsMJdK5fZlBPmoDomGHXRmA7hVKXC6_oXFCGBWhbv7UzHsQ2TU7oNC79Rq-QbWdt3u2xXlZdncEieQRpywyQNmGdwpG1gxgBoft214boHuzUd_6XrtYigBVNw-BxWX89494O3qLY9mrcj2BfT8nBJAtmoDkjcEz1Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03147dbc51.mp4?token=efRpTbfciUYY--rkULQsWh3OXpyGW1YVp9wCfxjIc8zd-qx6TT2Mb-jAdaeD0gJ7XLeAd8jCjZ-2n61KmGb_V31zxb9QLgXE6nIbpR3m1s6mb2Ks1TBPK66dMYsYPt0Nkc0VaslgWd_EXUPGT0eEKnApUXvAASewPnzrkPwF3PWZZyyYyThKrhsMJdK5fZlBPmoDomGHXRmA7hVKXC6_oXFCGBWhbv7UzHsQ2TU7oNC79Rq-QbWdt3u2xXlZdncEieQRpywyQNmGdwpG1gxgBoft214boHuzUd_6XrtYigBVNw-BxWX89494O3qLY9mrcj2BfT8nBJAtmoDkjcEz1Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هتافات الموت لامريكا تهز الحرم العلوي المطهر</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/81741" target="_blank">📅 13:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81740">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d11479656a.mp4?token=vJsGGuoNRGp7DycfJN2lgC2RCZTIfBd7jgDq2sR6DflnZVW-OXIJn8LGcwhjjFrUXJp2Nk5RNeVXlwkalGxu__9b968cxfUeR4KZA95t92Tc84ek73vl6m0BHTUPvisl1SMKzOhh5XPnSLKqnGF31k0S9SqZ0zr8lwdY2evEdTATgDNjZ4U_6JdyXjxQuZnZ9zWB1uZB5ny6OfvfjWVxa_p9eDQyfVL9tarAqYxIe757KYWWUD4b8ISG_KtVmN3chUrVm_3WHsEmdFxwt_lmszH3DILyCOLJOr9pyGtcMdbIYoRWKYU1vatE3AkGoEYTkKE8jwGDTAfDIndVOzrO7EJai9KMqspfnuOaO1Xlp08v3dz1k3NH4-pi_I_86M87aDAWa8rp540_-yEDkF3Btdn87HA9cmRTCs0gsvWzE8bx8UeKZpJtCZrr6clhsFym_VZXOtKbqcy9xt9OcEdKqj9tuPoBRa4axBoiBrNkqZmenjC4GKHvChX8qPXpsux39nJKRkq35WIcewQTu4Tj9yejP2OIB8lPPftYeAravL2gIY9mROQ7lBz7sXETOB_ynMGxz-_ScXQMix5WPmCXbyhewgLZsPO9fKTOLeYM3ORYHj-7qcGRKyrRslB0xaPcFR3sQeHDUWcO5QhE2g7P8fZABrg9RBdpcKMz2kjyqX8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d11479656a.mp4?token=vJsGGuoNRGp7DycfJN2lgC2RCZTIfBd7jgDq2sR6DflnZVW-OXIJn8LGcwhjjFrUXJp2Nk5RNeVXlwkalGxu__9b968cxfUeR4KZA95t92Tc84ek73vl6m0BHTUPvisl1SMKzOhh5XPnSLKqnGF31k0S9SqZ0zr8lwdY2evEdTATgDNjZ4U_6JdyXjxQuZnZ9zWB1uZB5ny6OfvfjWVxa_p9eDQyfVL9tarAqYxIe757KYWWUD4b8ISG_KtVmN3chUrVm_3WHsEmdFxwt_lmszH3DILyCOLJOr9pyGtcMdbIYoRWKYU1vatE3AkGoEYTkKE8jwGDTAfDIndVOzrO7EJai9KMqspfnuOaO1Xlp08v3dz1k3NH4-pi_I_86M87aDAWa8rp540_-yEDkF3Btdn87HA9cmRTCs0gsvWzE8bx8UeKZpJtCZrr6clhsFym_VZXOtKbqcy9xt9OcEdKqj9tuPoBRa4axBoiBrNkqZmenjC4GKHvChX8qPXpsux39nJKRkq35WIcewQTu4Tj9yejP2OIB8lPPftYeAravL2gIY9mROQ7lBz7sXETOB_ynMGxz-_ScXQMix5WPmCXbyhewgLZsPO9fKTOLeYM3ORYHj-7qcGRKyrRslB0xaPcFR3sQeHDUWcO5QhE2g7P8fZABrg9RBdpcKMz2kjyqX8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لبيك يا علي
الجثمان الطاهر يزور مرقد علي ابن ابي طالب</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/81740" target="_blank">📅 13:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81739">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W7f-eChNe-gk10uFKU9fyDLApNLQlcJgSXpjqYX9E1tb__Z48_K9RzfcOnzrtx1WyAPPrHTCyTnedtGZsrM2xYzYsB3AskyJ_gvQwJyaHw704gqmaV1Ljs0ZOjighHYYgoT89L7qEgyzCZhfHbpNJJ2mnyXT-MW3Juw8c1Sbd4lhcXxmT4zQobKAmpKqLeZvoh-R5enNWlNTiYvjrJlY9x7sgt83jWz6kall4ee_xoRJW9u70s1vux-UIewX0knIqS6k9Cg8ajDPY19l7gysAD7y5em4lQtBGibc-JakQma7OyRUGSAzTdn2diE_i2710VamVzfNVNIiHV9SdwGoJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجثمان الطاهر للسيد الولي الشهيد يدخل مقام الإمام علي</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/81739" target="_blank">📅 13:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81738">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">علماء حوزة النجف العلمية يتوافدون الى الحرم العلوي لاقامة صلاة الجنازة على جثمان قائد الثورة</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/81738" target="_blank">📅 13:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81737">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c0bba8588.mp4?token=VMIIE4s0k820koL_hSM0aL8Rtj95-RgO84pXFspaCDbNnPow3TcE-wbhFSz9jkLQa0NrvWkexzKqAAxPNHSZUD6oUgxaeQ7TY8M8uvCW8i2u-UQtxvZj_ubGl5ndToJhq9unHNQYrvzYHh122gpXopqeWO9TiZmQvA1tmzayJoUuCuLElOissblhK4eDrIyQyVP0-ubtP85IcNNCaMxUr2zdKO03jwzsvTRKqQOCqLsd7KGAtAfZICeJZi5OQUi2mHAumsYJzkWKe5UyrvyybzDtbM3ORKmNsEyyfByzbq86uwA-keV4VyPC6-gTTzxqgpdXy9bDJY2bg7vWWq5S0yebnRftrYKRwT1XCkk-pd4qi6FJb8PJoSnlTwufmtUcbZsOYOisUG12PmFZ2VBruOgjN71wjSlGucmKA_jwo9Aj6s7hLfqCFYYA1VPxfz2P1CZYEkqmtBROFVGhOU3KoVtLuSjd4R21SFFSqhFtq5-nRO8r2NMe3pUgfLnNmMxXTg3i-qoGIvLdkFiNPBBYJUrKZ5L1auPaFs3cA1Py-hRIp6b6f61Wz0xhy6WxD8_d1hv9ZLsknfRPNhVemWTbXAFX2J9EKpLDVO2mZsWz6w7K2ioMRVlPwuf_7TBxeBu1GZyvsLsxREpAosHJYjzhllFGnSS7Smt4rys9QcYbuMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c0bba8588.mp4?token=VMIIE4s0k820koL_hSM0aL8Rtj95-RgO84pXFspaCDbNnPow3TcE-wbhFSz9jkLQa0NrvWkexzKqAAxPNHSZUD6oUgxaeQ7TY8M8uvCW8i2u-UQtxvZj_ubGl5ndToJhq9unHNQYrvzYHh122gpXopqeWO9TiZmQvA1tmzayJoUuCuLElOissblhK4eDrIyQyVP0-ubtP85IcNNCaMxUr2zdKO03jwzsvTRKqQOCqLsd7KGAtAfZICeJZi5OQUi2mHAumsYJzkWKe5UyrvyybzDtbM3ORKmNsEyyfByzbq86uwA-keV4VyPC6-gTTzxqgpdXy9bDJY2bg7vWWq5S0yebnRftrYKRwT1XCkk-pd4qi6FJb8PJoSnlTwufmtUcbZsOYOisUG12PmFZ2VBruOgjN71wjSlGucmKA_jwo9Aj6s7hLfqCFYYA1VPxfz2P1CZYEkqmtBROFVGhOU3KoVtLuSjd4R21SFFSqhFtq5-nRO8r2NMe3pUgfLnNmMxXTg3i-qoGIvLdkFiNPBBYJUrKZ5L1auPaFs3cA1Py-hRIp6b6f61Wz0xhy6WxD8_d1hv9ZLsknfRPNhVemWTbXAFX2J9EKpLDVO2mZsWz6w7K2ioMRVlPwuf_7TBxeBu1GZyvsLsxREpAosHJYjzhllFGnSS7Smt4rys9QcYbuMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدء إقامة الصلاة على جثمان القائد الشهيد السيد علي خامنئي في حرم الإمام علي في النجف الأشرف</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/81737" target="_blank">📅 13:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81736">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">مشاهد من تشييع جثمان قائد الثورة الاسلامية الشهيد داخل حرم امير المؤمنين</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/81736" target="_blank">📅 12:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81735">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c82fc0f43.mp4?token=dHgQDUnbupLhWEQPj0bs4KHr_3kqO46WvdftfNEPOIy-_P2bOCjG-PYzMRZNDyyGJApSrtfg46S643tiXvFD646PFfuqz4L5No-nqO9sO6SLT3Vk5e3I3MJpJFvUnQ9kZh1fnNZM3iuCGmgnProHyeUfWwGNT4Y1rA0MLIkUOEyZY2jlWIp2xlysd-Pmja-dwlPrYXU6YkX623MFd3gk0hOKxDmINOAW8bKVQvlWs9EaX4Ifdx2A0Q04Gb_hfaN18YmDphbkX3o29sUSaCeK0s55MmqZ6Vsvbz2CxsOWzgeHlx2uXSw-KEBK-OY1Lb8_R_MTrVzUmM8z-XuU7bxSuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c82fc0f43.mp4?token=dHgQDUnbupLhWEQPj0bs4KHr_3kqO46WvdftfNEPOIy-_P2bOCjG-PYzMRZNDyyGJApSrtfg46S643tiXvFD646PFfuqz4L5No-nqO9sO6SLT3Vk5e3I3MJpJFvUnQ9kZh1fnNZM3iuCGmgnProHyeUfWwGNT4Y1rA0MLIkUOEyZY2jlWIp2xlysd-Pmja-dwlPrYXU6YkX623MFd3gk0hOKxDmINOAW8bKVQvlWs9EaX4Ifdx2A0Q04Gb_hfaN18YmDphbkX3o29sUSaCeK0s55MmqZ6Vsvbz2CxsOWzgeHlx2uXSw-KEBK-OY1Lb8_R_MTrVzUmM8z-XuU7bxSuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جثمان القائد الشهيد محمولا على الاكتف في حرم امير المؤمنين (ع)</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/81735" target="_blank">📅 12:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81734">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a72ee1425a.mp4?token=INnpTqf0dABMz-PtFtAooIEnBq1cO0Mo6jd_s1FCWAYmbMD2kN8vgPdNFmYlWGUAGwmYnSQk8NkHh1-DvGbGPWPDRm-mBSRByaeOmwVwA0D1CzS2oeKuB_LEgie2q9X15ct0-wzvAqgx5I8RPnhtCQpB0r5nhGSSjvNG2Gu4sh3SqFVSVS33nLx-kgQ8Et5wi6Aw2IxU1CDI-I7a4HZKyUA0fHlZSSqeSbL21sBH0_CLoraGhkx6dhkvUmfW0aY9UFdSzbmni3G2zo2ambORqzzCDT15xUlbryUhHbsjo6eiAtOmPGq41s0MPMSO-asw8waU6AzPPAMc7hOF2eSSpw1Q0jpUFk2Cbb6Q0rrlrbPptPk29jQyQP8swcEd61DXmsSOxK80pJ7JuJAJ3NeOn9FETJBtzswZz5yo5Fx-ZKxd0_j1ppsskWkSc00gcjR9Mlc2rDXwx7C3wNoF_dL49DV7NzfzGIIN5MIlzo6y8qTku3oMYMccyIgK7XKg9xTotXPuI4BIG3nBGd2cHkRDQboDHnQuN3Vtx0Pvq4vd0zYTsDNEA_jXDpApAeVOpjIoOOdvxQkKDvtArBJSZ5SkLBJdzWmsX24xF-HtoRvhBx8BG1fhnbTumyzC1VYcRiY6kPgiFzass0G7b9-edQAS_T0CFrsyAuhrZLlYiED4XTY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a72ee1425a.mp4?token=INnpTqf0dABMz-PtFtAooIEnBq1cO0Mo6jd_s1FCWAYmbMD2kN8vgPdNFmYlWGUAGwmYnSQk8NkHh1-DvGbGPWPDRm-mBSRByaeOmwVwA0D1CzS2oeKuB_LEgie2q9X15ct0-wzvAqgx5I8RPnhtCQpB0r5nhGSSjvNG2Gu4sh3SqFVSVS33nLx-kgQ8Et5wi6Aw2IxU1CDI-I7a4HZKyUA0fHlZSSqeSbL21sBH0_CLoraGhkx6dhkvUmfW0aY9UFdSzbmni3G2zo2ambORqzzCDT15xUlbryUhHbsjo6eiAtOmPGq41s0MPMSO-asw8waU6AzPPAMc7hOF2eSSpw1Q0jpUFk2Cbb6Q0rrlrbPptPk29jQyQP8swcEd61DXmsSOxK80pJ7JuJAJ3NeOn9FETJBtzswZz5yo5Fx-ZKxd0_j1ppsskWkSc00gcjR9Mlc2rDXwx7C3wNoF_dL49DV7NzfzGIIN5MIlzo6y8qTku3oMYMccyIgK7XKg9xTotXPuI4BIG3nBGd2cHkRDQboDHnQuN3Vtx0Pvq4vd0zYTsDNEA_jXDpApAeVOpjIoOOdvxQkKDvtArBJSZ5SkLBJdzWmsX24xF-HtoRvhBx8BG1fhnbTumyzC1VYcRiY6kPgiFzass0G7b9-edQAS_T0CFrsyAuhrZLlYiED4XTY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نعش القائد الشهيد يدخل مرقد الامام علي (ع)</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/81734" target="_blank">📅 12:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81733">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b245887808.mp4?token=UBCAnTmx58r9c1revJSqkFoHVmUxtq2vtKJKIDemRWG4UaUaRxFwclv_JHwY41LfmPn_jd8oggymTPVQ1RLtkUnw8fD73m-cASoCXyyubkIBUCHokHHYlJq6EiTBzH0DcMqdpurvEsHH6ygxE4OhsNJKwOh2uYsBSJd0GB-eGcOFsbxKAk82AMb9QaH7pJ_ejGun4fpoKAF1trxq6mtStl8k3Fu2LsMROwr_WCYbefvOFXwwk1ZhpLpuW-HuQIMDFX9IxORCV5uyDOMf0eyMkNIZo5ewLfXxH_ExXazj-XUrbjGRF9001F6fnDT54QuWGqIpM82DgS3BccfPwQBZtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b245887808.mp4?token=UBCAnTmx58r9c1revJSqkFoHVmUxtq2vtKJKIDemRWG4UaUaRxFwclv_JHwY41LfmPn_jd8oggymTPVQ1RLtkUnw8fD73m-cASoCXyyubkIBUCHokHHYlJq6EiTBzH0DcMqdpurvEsHH6ygxE4OhsNJKwOh2uYsBSJd0GB-eGcOFsbxKAk82AMb9QaH7pJ_ejGun4fpoKAF1trxq6mtStl8k3Fu2LsMROwr_WCYbefvOFXwwk1ZhpLpuW-HuQIMDFX9IxORCV5uyDOMf0eyMkNIZo5ewLfXxH_ExXazj-XUrbjGRF9001F6fnDT54QuWGqIpM82DgS3BccfPwQBZtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نعش القائد الشهيد يدخل مرقد الامام علي (ع)</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/81733" target="_blank">📅 12:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81732">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇮🇷
رئيس الاركان الايراني:
سنحوّل سواحل إيران إلى جحيم بالنسبة للعدو</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/81732" target="_blank">📅 12:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81731">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e16f90049a.mp4?token=pRs5eg394JNrJpsY76Z55j_DOc11a6uNBZec7VCXdsLsaVmTIYTQ2vqkY5EqDBZw6vFEpfPyDtFAqijRG3BKvwKMl66KT9C2VBpMGOPsru0o660eJiZqtghRRynzKqKl4iTP683UQ3tUdK54WNhMzMUGezaSGgL0Ib_sa0GnAqbXUVu8Eb1oBfW1G-I8j83OMtFbzcbUCwfFK3FrCcvvcIp-osVgQxrd7YwEVae4RNXllCYftsYl0g1aStpidQol3rbCzlgGEZKbFQb6ofMiYIRfLXXumeN2qqh9GkPJ1uzQ-t12FX7-sOfQGZKMttxDUFZZYSleoz8lph5S_bcKFYx0YC6TnPqPXrslGP03UsGkFynMijQbCYOPhTxtvIoj8UT9bbrD9_leBk7ky8C8eau934n75hHF2S1nXr-YrvNrczTlTNL_fW742qgOBq3zgMZ9tWLJ3pQ_vUHlTHCfMhg1i4Hz5g1IZxyOjYitOsiv1dvZclwgZIfP55QEhR0GdRbYiKj72BDalQWmtoQOmJATjHZr7-L2yg5_VyuaM2V2f8F-lRu_YPQSSZhgF1LLKbQSmyO5NgwW-ceqQW4c3cnqXe0tRjp7JPbr4zbCdGPZkz4L2bEixi9TBR-Q6tL983B5Cx-qXa7ksrFTPDA51nnFNU7pvLac_b5ocpMPXo8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e16f90049a.mp4?token=pRs5eg394JNrJpsY76Z55j_DOc11a6uNBZec7VCXdsLsaVmTIYTQ2vqkY5EqDBZw6vFEpfPyDtFAqijRG3BKvwKMl66KT9C2VBpMGOPsru0o660eJiZqtghRRynzKqKl4iTP683UQ3tUdK54WNhMzMUGezaSGgL0Ib_sa0GnAqbXUVu8Eb1oBfW1G-I8j83OMtFbzcbUCwfFK3FrCcvvcIp-osVgQxrd7YwEVae4RNXllCYftsYl0g1aStpidQol3rbCzlgGEZKbFQb6ofMiYIRfLXXumeN2qqh9GkPJ1uzQ-t12FX7-sOfQGZKMttxDUFZZYSleoz8lph5S_bcKFYx0YC6TnPqPXrslGP03UsGkFynMijQbCYOPhTxtvIoj8UT9bbrD9_leBk7ky8C8eau934n75hHF2S1nXr-YrvNrczTlTNL_fW742qgOBq3zgMZ9tWLJ3pQ_vUHlTHCfMhg1i4Hz5g1IZxyOjYitOsiv1dvZclwgZIfP55QEhR0GdRbYiKj72BDalQWmtoQOmJATjHZr7-L2yg5_VyuaM2V2f8F-lRu_YPQSSZhgF1LLKbQSmyO5NgwW-ceqQW4c3cnqXe0tRjp7JPbr4zbCdGPZkz4L2bEixi9TBR-Q6tL983B5Cx-qXa7ksrFTPDA51nnFNU7pvLac_b5ocpMPXo8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وصول السيد محمد تقي الحكيم إلى حرم الإمام علي (عليه السلام) لإقامة صلاة الجنازة على جثمان القائد الشهيد
للثورة</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/81731" target="_blank">📅 12:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81730">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kh4K4pfUs59Nf2uN--DTf93TybvHGj934J6wnVi-s1tJ_D4eJLihpgNfvyyetSKOqzPFr_hqjgVGplmWHH8qOqM2567YtFwSismRhHB_3-u3VMiUxE-F210OauH5bAtlXX-yURrfZgUBsp8IxDst0WpMgoKz-F3XAXnoQvz-g6kmcBLWJdJxmgUYVtEyZ9zhT8W8jeAFsn2Wv5hexYuosMTdXQxzs52OrdIjDNiKGQpWzCr0NyI-EPN4Z2guqhu6erNWHEs6qAHy7SP-y4gQlAkcfGs92OV1FQ2LXlnyEIUgdIvENyNHJMVWluJiCU5hhyseDhMpnrywNXT1uBkifA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نهاية الفراق.. علي في حضرة علي</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/81730" target="_blank">📅 12:33 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
