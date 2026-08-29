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
<img src="https://cdn4.telesco.pe/file/UByV2a-t6w3YeXu1ZRlVUdIWFFjva2Thc-sFF3MjeiyhdqTe-CMg0k2OnAA0d0f7w7JF6L_f_447-LfZ7MwCkM7aL049ON4OKCnw_VtvvaaeipqCTW8HLJ6a7YFphPiNwD63wg7KOLwXrsargPEqsJ0rhkGRDM215YvYDacShNSqHnTOYl6ljTtLnhr0H4e7GAsHY7ZuBEO6O6tigv0ScqiZ3rXnoHeQqEtdCCY6rfj-tzT3a2hq5l9gMASwJpNzq8wIbPnrUU704gw3vGyPdhMgil5IHfQwEdwOVUw_4nuPJ88agp7s46tDf-ZZxvWDyOTIH0hy2WhtCYlLRsydPQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-07 19:12:14</div>
<hr>

<div class="tg-post" id="msg-139169">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WNhojw7Q7Ih8B60zbscYANBYLkHon8KKaJUVXMtJDDHQejQ6EZUUUFcSBCgnzn4YYrL8B1h61H7g9WyaJJxwvsE7Rc1wOH20dL98WFDsGAeCMjCpq0h9U3lt5OwDbEfOUyXQLdu3eY1CVUt0i_jhmzi_HPYXS0y67HJHyb25jW8_8PcG62aBTERRmUWaE4M4tJ9GUzlzaIeoCH60FDlkj-9UHc-DiPr4mJkGVM_dz7KPY6K3XAbbcVWKmuyBxAscXXL5izfi6Okhh3eOOksSK2ajUm3Vg8bB9cWT1c4OmxqUh0OLFCv1aj5SSfyKuFVeKL6o_riSpYpNDf3vNBYHDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟥
ورود کاروان پرسپولیس به ورزشگاه شهدای شهر قدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/SorkhTimes/139169" target="_blank">📅 18:37 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139168">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78df0f8e05.mp4?token=XRmiRO2sbB7bqPKLlc4fjUJst0iaC-Xhvry7HO3681-NLigmGGBpGNLiB18KaRHjqTy8-1BlsEq2lJ5DeJ_WS3ziWnn8BVZnuJNz-dd16F2JgMH-mJoYT7G-jxPO2KdrZ8FC-BLCsa9m4hpyOfp7onN0lun49IsU-ehijWJ2U4uC-Yg0JXmKgfh36CX23W7PCYUEo5L3ubZGZMYtOMKMHl4xZLbc4EtXdoGxFAsFF_3yjnQWp3phpHOqNSmMp1ogOhVJJxjn4E07cGvwzfpZijbJpiwFJtMZLwrwSc1H75tjWC_zWHQUJARJuw3rsbNTFsdUpcwW2zY3mNNxG6PJr5N-cQS7ptZKQgFifWjXZIPGwW7_iy8UBzfwzUPrI9KvDTs0B7bndXLrar76dN8Jou-ypSVeVAZ3ObU46q7tucubEMnsLuSjCXYlYEUW6G2LtITHdnWuD-fAA6c7r1JdaHq6kYRtq5KXhDGcXvee-8-5VEKUQdxSTGYI67LUHycMqD4VRRXUYvg2FtiMmdMerZeVDoC5J_LnBjO53hw7A3hPPCR4xNhfJ4O6cu9tvlBf7WBJosf35l83xz4CFm1BBdQIt0CCt8MH6wSS04qnrkrTOndUSuFGEF_b6VYBCBMlZWFmt7IxTQnvCiLjZ4QGnQQw1Ar-xRTghenwgYaP6J4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78df0f8e05.mp4?token=XRmiRO2sbB7bqPKLlc4fjUJst0iaC-Xhvry7HO3681-NLigmGGBpGNLiB18KaRHjqTy8-1BlsEq2lJ5DeJ_WS3ziWnn8BVZnuJNz-dd16F2JgMH-mJoYT7G-jxPO2KdrZ8FC-BLCsa9m4hpyOfp7onN0lun49IsU-ehijWJ2U4uC-Yg0JXmKgfh36CX23W7PCYUEo5L3ubZGZMYtOMKMHl4xZLbc4EtXdoGxFAsFF_3yjnQWp3phpHOqNSmMp1ogOhVJJxjn4E07cGvwzfpZijbJpiwFJtMZLwrwSc1H75tjWC_zWHQUJARJuw3rsbNTFsdUpcwW2zY3mNNxG6PJr5N-cQS7ptZKQgFifWjXZIPGwW7_iy8UBzfwzUPrI9KvDTs0B7bndXLrar76dN8Jou-ypSVeVAZ3ObU46q7tucubEMnsLuSjCXYlYEUW6G2LtITHdnWuD-fAA6c7r1JdaHq6kYRtq5KXhDGcXvee-8-5VEKUQdxSTGYI67LUHycMqD4VRRXUYvg2FtiMmdMerZeVDoC5J_LnBjO53hw7A3hPPCR4xNhfJ4O6cu9tvlBf7WBJosf35l83xz4CFm1BBdQIt0CCt8MH6wSS04qnrkrTOndUSuFGEF_b6VYBCBMlZWFmt7IxTQnvCiLjZ4QGnQQw1Ar-xRTghenwgYaP6J4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟥
ورود کاروان پرسپولیس به ورزشگاه شهدای شهر قدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/SorkhTimes/139168" target="_blank">📅 18:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139167">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/153ca3a7ea.mp4?token=EIEBrOCdV9TAsU8ShxWNEEbPNyIBJgNpUhG8QAlAFm4wy8a8ALMG7xggjGkT5blM0iqloz8iNBBje2e7qQtAHTSNEqb5JNFjqqsAfv_vXE1DoMb0QJqLVYZ5Apo7eRpy89j9AkIkxORV60Qel6zQYjIGeX0WJPkEIS0_Qtjx4hrBY7qpcLnT7tyMWRfiD_lK2fz46wXfOBaOTPYS3Q_q7UUo1lAV_5fX5EDF4z0Pw9gPb9aEoN71K9E2F_KgtmjrJBtsdaCPlZB4ZHRTw_NDq1g5OGTXxyQJAuf6pU8Vw8yOioSALyx9tvEXx_hjNPzOY-fBGdp8N3dYDbGhJt6K6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/153ca3a7ea.mp4?token=EIEBrOCdV9TAsU8ShxWNEEbPNyIBJgNpUhG8QAlAFm4wy8a8ALMG7xggjGkT5blM0iqloz8iNBBje2e7qQtAHTSNEqb5JNFjqqsAfv_vXE1DoMb0QJqLVYZ5Apo7eRpy89j9AkIkxORV60Qel6zQYjIGeX0WJPkEIS0_Qtjx4hrBY7qpcLnT7tyMWRfiD_lK2fz46wXfOBaOTPYS3Q_q7UUo1lAV_5fX5EDF4z0Pw9gPb9aEoN71K9E2F_KgtmjrJBtsdaCPlZB4ZHRTw_NDq1g5OGTXxyQJAuf6pU8Vw8yOioSALyx9tvEXx_hjNPzOY-fBGdp8N3dYDbGhJt6K6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
کری سنگین هوادار پرسپولیس: آخرین باری که استقلال دربی رو برد دلار ٣۵٠٠ بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/SorkhTimes/139167" target="_blank">📅 18:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139166">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c76c3af39e.mp4?token=YX5utmyG4bl6LXAPgFrri2VnItof-DX1VWWWapvGdArMx6HED4LN_KjFbeVKOOhV_Ai0sCE9HuhNQL8X4l3vpMNKwOEPC2n7WXLO_eqsTQD0dtal6stbctJft78OMhYfK4Q-7R6koD18P-pQmouJvcB76q8yjUkkWJb7cZ8AaSzsSh3psXgxkRHrrTmHXcU_KnPtbUWHDm9466RVzMiQhs3X-l3_4jFj77RtB4LShGb0OeFjrlrEK0nFAfIJvcL8VFKiJr7XneRBxx-YlJ-FQx7QsWtiPe06YKXCf8mLpxNxHt4kTKfr9unqDfBtd8N2h8JbLfR-4hp_9cRwsKwZ9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c76c3af39e.mp4?token=YX5utmyG4bl6LXAPgFrri2VnItof-DX1VWWWapvGdArMx6HED4LN_KjFbeVKOOhV_Ai0sCE9HuhNQL8X4l3vpMNKwOEPC2n7WXLO_eqsTQD0dtal6stbctJft78OMhYfK4Q-7R6koD18P-pQmouJvcB76q8yjUkkWJb7cZ8AaSzsSh3psXgxkRHrrTmHXcU_KnPtbUWHDm9466RVzMiQhs3X-l3_4jFj77RtB4LShGb0OeFjrlrEK0nFAfIJvcL8VFKiJr7XneRBxx-YlJ-FQx7QsWtiPe06YKXCf8mLpxNxHt4kTKfr9unqDfBtd8N2h8JbLfR-4hp_9cRwsKwZ9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
⚽
ورود طرفداران پرسپولیس به استادیوم شهدای شهر قدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/SorkhTimes/139166" target="_blank">📅 18:07 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139165">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76152fe425.mp4?token=kPZ6oyRwB47JeTrEYFzaBsQloLm9LNKN7hoI3plYRq6vGKlMyIdgGbxiElS2AjFV9ddvv8RbKUyZCqBqoxnGknMKP3Zps-YdoT93FmbyL12ycEBmDhOYvH9XkCgWTh2sdFWigy_Mj8zzc87iP-hf94r4XfeFPD927FtlJQ7mKMQ-0Dbmnq87ipwGyPSFmg1ZQ-3N1sfM2TGaDBlfzsp8GE--k3m8331axcOxS4oxOQNOG6iJiinW8MH78ALOf7kEljjUbmDCwwcJrYG1NDnxiii0MVnEsvmiO1PTnDtXYtg5sDfDYKD6D1lx_vdZLyiH3ISc7zel4x-sNDl38vpwOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76152fe425.mp4?token=kPZ6oyRwB47JeTrEYFzaBsQloLm9LNKN7hoI3plYRq6vGKlMyIdgGbxiElS2AjFV9ddvv8RbKUyZCqBqoxnGknMKP3Zps-YdoT93FmbyL12ycEBmDhOYvH9XkCgWTh2sdFWigy_Mj8zzc87iP-hf94r4XfeFPD927FtlJQ7mKMQ-0Dbmnq87ipwGyPSFmg1ZQ-3N1sfM2TGaDBlfzsp8GE--k3m8331axcOxS4oxOQNOG6iJiinW8MH78ALOf7kEljjUbmDCwwcJrYG1NDnxiii0MVnEsvmiO1PTnDtXYtg5sDfDYKD6D1lx_vdZLyiH3ISc7zel4x-sNDl38vpwOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
روش جدید ورود هواداران به ورزشگاه شهرقدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/SorkhTimes/139165" target="_blank">📅 18:05 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139164">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d95e62021f.mp4?token=EtvRbuG1mDxv1qwtk5jGvixzScfIy3ziMHQHTGFEN6peQjhyN24_LrqkgdFn4buvBri8GKl6Kerv787fzfI1ESx6uq8YZSs3KKr6A-VSjLNPxz3P-m7Z5WuKcL0TNXZl2hWdfhfE7ozRaN8Y8SNw0GMCWfhW99hcJ2z-03gZrqATqZeKAhD9wGaA0HbQcRwGN4qG3pYdWrSo2zlwAk0vbUf8SVpzQYFA6VljaJ53PhGO2MZt5cy_NaHTHNXlGnnZnFRKnbliC8W2WcM64fQueooljLcbDuSz3ZsV8STrmytdmTxG36jYE-TFKnoTSwf9QF1iobKgOuyawq4xqwMrVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d95e62021f.mp4?token=EtvRbuG1mDxv1qwtk5jGvixzScfIy3ziMHQHTGFEN6peQjhyN24_LrqkgdFn4buvBri8GKl6Kerv787fzfI1ESx6uq8YZSs3KKr6A-VSjLNPxz3P-m7Z5WuKcL0TNXZl2hWdfhfE7ozRaN8Y8SNw0GMCWfhW99hcJ2z-03gZrqATqZeKAhD9wGaA0HbQcRwGN4qG3pYdWrSo2zlwAk0vbUf8SVpzQYFA6VljaJ53PhGO2MZt5cy_NaHTHNXlGnnZnFRKnbliC8W2WcM64fQueooljLcbDuSz3ZsV8STrmytdmTxG36jYE-TFKnoTSwf9QF1iobKgOuyawq4xqwMrVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
چمن ورزشگاه قلعه‌حسن‌خان کوتاه و آماده میزبانی از دیدار پرسپولیس و ملوان است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/SorkhTimes/139164" target="_blank">📅 17:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139163">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❌
❌
کلیپ باشگاه برای بازی امروز
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/SorkhTimes/139163" target="_blank">📅 17:00 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139162">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✔️
🎙
روشنک مسئول مسابقات لیگ برتر:
✔️
✔️
شاید جام حذفی را امسال نتوانیم برگزار کنیم، هدفمان این نیست ولی شما ببنید چقدر امسال برنامه‌ها فشرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/SorkhTimes/139162" target="_blank">📅 16:58 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139161">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5fbb7cadc.mp4?token=ZX4ahh1OPsW9G88e2XpAxmlhZK8JoicvmzlOTDdskUkpWUm14qngnaOoOc-Zg4Rcxkg9fYEP8K7QpwdLA9Dyy8birdrOTQX9o3pWYph1-3kFjyliRm8gPLr-RgYDVCdfIhMuvBX-W65tYbfngdp7FYJqxWIQnpT2CsVVf30c0_wbbtKqDBYR96KXtBCCJ4SOBUfaijDX8r7-YzlyhK19wl0x87Hpf7gBa6krsnl5EvXrqX0kKA2iFjJ__vEwcT4198nYN3BiHNY21o4-Or-SBSklND_Rx7HaiwZS4Ksiqou6f326wBf8Tb0VnJ1x6StjmvRTl7Jnk07bQscqtSRmuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5fbb7cadc.mp4?token=ZX4ahh1OPsW9G88e2XpAxmlhZK8JoicvmzlOTDdskUkpWUm14qngnaOoOc-Zg4Rcxkg9fYEP8K7QpwdLA9Dyy8birdrOTQX9o3pWYph1-3kFjyliRm8gPLr-RgYDVCdfIhMuvBX-W65tYbfngdp7FYJqxWIQnpT2CsVVf30c0_wbbtKqDBYR96KXtBCCJ4SOBUfaijDX8r7-YzlyhK19wl0x87Hpf7gBa6krsnl5EvXrqX0kKA2iFjJ__vEwcT4198nYN3BiHNY21o4-Or-SBSklND_Rx7HaiwZS4Ksiqou6f326wBf8Tb0VnJ1x6StjmvRTl7Jnk07bQscqtSRmuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
▶️
این وسط یهو یاد برد ۳بر۰ پرسپولیس جلوی نسف قارشی ازبکستان افتادم، جهنم آزادی، پرسپولیس مخوف و گادوین منشا ‌بی‌رحم
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SorkhTimes/139161" target="_blank">📅 15:54 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139160">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❌
❌
باشگاه فولاد امروز بار دیگر تمام پیشنهادات پرسپولیس برای جذب رزاق پور را رد کرد و این بازیکن در فولاد ماندنی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SorkhTimes/139160" target="_blank">📅 15:51 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139159">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
خبرگزاری فارس: تارتار دلش می‌خواست سرکیف رو جلوی تراکتور بفرسته داخل ولی تو ذهنش یه تصمیم تاکتیکی گرفت و فکر می‌کرد شهرآبادی می‌تونه بازی رو دربیاره
🚨
تارتار همچنین علاقه‌مند به سبک بازی سرگیف هست اما تعدد بازیکن تو تیم‌ باعث شده به همه بازی نرسه
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SorkhTimes/139159" target="_blank">📅 15:48 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139158">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WkhImQSR1WY0Moa35Yra_FrT9k1ycTnxQ-5pjuyDK6U1SYKF8SjZl3X3vzoyTsZSz_bVOs-3RyZ7ZOTL8rnaBZDIQMIhPyDFfrGD__rCeOIS0YIH204RjX9uvtXxPKDd5Xz7sVU-_WFcaAdDSoE_K9CgH-YdRZKyQEWaHB-xXQ8DD7lGSVEBSvQHaFYBKu2mmTlMIizb08m-bJR6ZF9ct_PML0rcb94zY3b2lk4iCAqgWIkAewFMPNyhBGrUdFVqAM-UL6M-0_VkU4KcgVqYnJsMTI5D6wjAHuPL43wYjh2kPzsYdvJiCQoM61SHF8AI7EVXiWVmdVpPVsBOidOihA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
جریمه 50 میلیون تومانی باشگاه پرسپولیس بدلیل توهین علیه مقام رسمی مسابقه توسط تماشاگران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SorkhTimes/139158" target="_blank">📅 15:46 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139157">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5667f8b6b4.mp4?token=RZrHT7TYrAFUsoSPAx0qrijDAOKs3ULjI0pR-FpkNqedFfasSX_w-zoibwscQTZ3I6FCGoNPj2xakID0a15jJlrJF8XZek_UeNLW8caeBceMdRHqbTA1iqWn2C0KADC0ni4fthCG0HzpGkcZH88dsLN_kmEHOST5F2xIe54Ct0rarBwFhGNfyVb6QBXrh9t7wfSAT0SIWzQ_vLa5aEARGF6944P7JCyhSjl7fyTJcJ_J99nVYAd-QSfrfCH-s5d5kQ-RGSBDil6EejqWIy8mo-mMLVFQbFpuud4-niH7VjNLZAALaGVAOZtVWY4LrFf3tDpADyqvmFn1wp649ywfow4bslRWmTC7ZqkzaLVkCpW6LCyE7STUSYqTOTJm6tveq1h_0Q1MqpDPaQYssWWa0MDjARRXBAvUraoQMVCllb79km-ibZTfqTwAwhfcnh7x4VnObSi476xZ6Jo7PGu2p_CEvkzLBzMYfyRz2GeHMDrKz4iKqLBg3QYQ9wN3ovVbd9t31PMbFebIZgtuPlkAT_LZGKhtQotlKxa8r0iwPGosMNR10o88EbFi9ojwm8LkQ4D3GzOtQcIv9vrGxLtJ9x92xGuCf3TCCB6K6xC4Il6WbPoi2dZyROCX0p-RHhIfNKJgIPhLMCKHcVUD4c0ft6bm5ql7KMt2VFtCxZM72SI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5667f8b6b4.mp4?token=RZrHT7TYrAFUsoSPAx0qrijDAOKs3ULjI0pR-FpkNqedFfasSX_w-zoibwscQTZ3I6FCGoNPj2xakID0a15jJlrJF8XZek_UeNLW8caeBceMdRHqbTA1iqWn2C0KADC0ni4fthCG0HzpGkcZH88dsLN_kmEHOST5F2xIe54Ct0rarBwFhGNfyVb6QBXrh9t7wfSAT0SIWzQ_vLa5aEARGF6944P7JCyhSjl7fyTJcJ_J99nVYAd-QSfrfCH-s5d5kQ-RGSBDil6EejqWIy8mo-mMLVFQbFpuud4-niH7VjNLZAALaGVAOZtVWY4LrFf3tDpADyqvmFn1wp649ywfow4bslRWmTC7ZqkzaLVkCpW6LCyE7STUSYqTOTJm6tveq1h_0Q1MqpDPaQYssWWa0MDjARRXBAvUraoQMVCllb79km-ibZTfqTwAwhfcnh7x4VnObSi476xZ6Jo7PGu2p_CEvkzLBzMYfyRz2GeHMDrKz4iKqLBg3QYQ9wN3ovVbd9t31PMbFebIZgtuPlkAT_LZGKhtQotlKxa8r0iwPGosMNR10o88EbFi9ojwm8LkQ4D3GzOtQcIv9vrGxLtJ9x92xGuCf3TCCB6K6xC4Il6WbPoi2dZyROCX0p-RHhIfNKJgIPhLMCKHcVUD4c0ft6bm5ql7KMt2VFtCxZM72SI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
کلیپ باشگاه برای بازی امروز
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/139157" target="_blank">📅 15:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139150">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kr_Nk5fPEDCFTknQdgVIHU8NOzj7gxsgIyiW7Gga2tWbNxFVdDsxG3Ir7Gvxl_OnLFqHRmHXFcOmJk2iVrbJh3AsDDLgLysQilha4kIl02GpDdB12Q-7Kv0zVTVfobNLhRs7wst7vNef9VOG3jM_tDDfnEO24cAB2sW3D_TQrL2RPIxM8DYAa-_9lzVlJ0L6N8xcyIbYZhMLHKMBFMPW5tWFCGs1M9-BLtiwGRbJedMhNYDqL5GOl97mxCwSyGw2fPHmv4aZBi0I2Z7Gw_kUwhH8vCXR1WI8Mh6iAg_jKS-Ic55KQwcmPX-1JJqKdF-ewRuGf8vCQfSGjw71vG_ouw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nJC7ju6MmHPgDast6Dy6zG6TNzBfLWCM6VM-b1IQQfjGWkUDbRIOQKCQp9L2W29mmIJBKVQEABS7C4lDHrVMrQpKgcRdL1za8wLoyTa7KUiDNVdWv6RpJdSmtlU46mLC-eqIxhRe_gChITBpY2fl62xzmV1S2kPoadoNvnKFfg53oWcJF_adFQVwc53rZdKUTddc6LqASWN-yubuvmGAX9IGQ9YAgBvmAA-3CkLc9XStP6X3evut0854YsZxCmBtctlTb85ZkJVqaLT-S3SSRMixTQi2iCFhGotpKu9dNNRwzR4LH3wykmijTgSmVfG6TmSFenxJQj_uAiqCsW9sbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GhM6DMbC3i3rg2Y2tvEaII_PSAX8jvLRiZNvNrxWwEAAZ_ZHIN3KCSFOsCv2gKTzrq96CZXOA6Acu87i95y4fYCtapcCwzk8HrZooZVOuYfRD2lQeXMYCFjJUMhKROCWQ6kClgYZnmm4ld3h4eu5rWj_9_ManLP5kmFR4n7mg9q3fFNkYinwB26fB0hOqIupoj6Uzpa6Yso0GKjI6r3LnOqTLUWbhr0bMmDq1LfX0soA7nDq707NH3i5IHiDGC3FspRX1vywFeiQqw6HYSXH27eg14IEE_J0etJfas0_INdlAB9V5ZDsJd7jiTjXsKUDNlp_MylQBzBAZtW5yb_cUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kizTqJCZ9LxXrEfh1sJJ2C9AtJ1-qwc68EMX4O9V-b3qDUnThn4eZwHQvLGSwCFCYnY1odMsnvUpGGI6iLVy-rFELAsk7wrWEPabUG4CMDT8uSPbce_CBZ4s0c5Wlvh-qBJqiM96Tpfs1Baw-mecw4gtA8Nwp7he2ilUTdgUJyu_DqmDkwz2qrJ5-p5j6axke1uFSbU32oZTzaqSxU6d6dxV_oJ8Q0dW1OTtozDnaUwhOjsDbySy5jzTK6dYu42qhCRYR3DO0-H1v8xRC9NykxJFJWvomwLejAtnUBCP5-gqwooOgWZbDzQhpT5cLKdLeSgyE0yo-0Odz5fhQfJ_zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CWARraiU1tHSL3TB4YybKCBDD7XQskPX_rNFCD0QN91060UbuO5sPzJjf4JX5Fve-YG7slBU1hJ8Z2FjYjnStEO8zijpvxQV1nGD4yHJnB7PIpc6SkL2VqQ-IAmYqIc-aK_tcPffYyeSfAwWhFgqjkBPYuJaMieLFCZWxB7TrPS-0cGKStoxLvD3UZCWyr_xXQFQVUHlnGo9a9i1L3YhDJDKKglAnoW6rrFKQNGqiv_-eQ_CTV-lIcAuODP3gxdac_xhA-RHc5lpDUdWmO--BDsK5a_uqTW6PFfpUWL9OeLn35okmYdkvMnoBNu2x-GaiAbrIUaKSo4nqW8qCEkNVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jI2IgU5wWzBU5iCpofAPHzOL0yEt1amOqE2jc3hf5oq_z8gxvo5JbCqLT-XVnd1haOCIR6I7h1C8mV4c3qePOZPLHgnhwOSs2Q7J8HSeMURMep1Ma7BIHuuNCH7myqouJOQ_uhChxBwMA04mtgAMNOTE_WaVbTKvi0RoBPoZ5qzXf3wp89VuIvCLooxSLqK0dxpkjP8E2Nk3EZC6paM48E5u85ntC3TSxghAg4U_dAKzer5w7nqa6VtNnagJJB60_vSyrBSKTuQ6StODcLNeSD2jH-QGcOw0_d0V5KsMK6REZW1phd4Mmy4yG-C4JpJObec0-aeVBLu8_dZeY-VZgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lUGzlZ6NmLHX-tq_LniKFXoQ9IE1JqzOOsvMhRMby82VgjyEO9TvXotmcRK0YmrWVuPsbKB8FJW1wSW_lLeTRwRhe0NQG9XxUQ46SL3_syZPwhi7YNtqX-6-djhrCkrLpb66K2L2mCLwCuow8HU1C4CMPHK_6ATz_nGq3EQRlX4AtOmRQoFwdX_9wq022xDKTI-XdHIA_LoKG-i5XMxEyYZiIWmGen8KZUgO-bS_A-ThY0HlCxZQCZEiPvXSFTqGSCM8PTA8YLZlP_nWEhSWf0OgCDe_FmMLXxlXbacbectrvXPDpf2z945BnyVClBBY0ldkQEA8bE3PaS_1yrCeEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⭕️
⛔️
حواشی نا تمام هوادار متمول؛گادفادر متوهم ول کن نیست
‼️
🔽
رشته استوری هارا بخوانید…رامین پوکر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SorkhTimes/139150" target="_blank">📅 15:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139149">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s8tNH1Wbyr5nA2C0b9sUcC37jn5rXzCkHguArlcdOWkgB8SPkRaAH1UOJEXKi82tYY5mtE05Gwl4waEaYpB3O40OfEClcpW1-a_lan6Er9oghmzyC2ILjN5i-zomieATDSHyuLHNymDSqQhyZCy-57QuWV3TFZM1-FvYYybgmYYsAdf40I8D4GLfskfMNtZMLW69Bg5lykl4ucnFsLb1_idMPoVTWWtJVPHp-Vwdg1G4aZnkzuws_-YG-qxIe_wecP4gsL1KprxBVJ3cxJsznid3biVUzCnLIOBGy9kySBGo_13NMtYNRPjBdiftPXGl4Ow8wrYffYQtmk1fc4_yMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پایتخت آماده یک شب داغ!
🔥
پرسپولیس دنبال شکار ملوان؛ قویِ انزلی برای غافلگیری به‌میدان میاد!
امشب نوبت کدوم تیمه که حرف آخر رو بزنه؟
[
پرسپولیس
⚽
🆚
⚽
ملوان
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SorkhTimes/139149" target="_blank">📅 14:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139148">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dJkmMg07xqm-DfotVNW7w_Q098-fUd6_zvTYLFpuoIKlsIFn6tQscNpOZjAN7AUc5IqMMrMA5NIs1XDiIwWC9g7w131mZZNOsnS11lr56TWPWseEdnenX9dUVy3zWRMqhlxQykhSNcrDtokSwqi0VrXc7EIB5ho8wBIWlO-noxQPso2Yon2o_gTjSWpZzvVXPBzfIfoNGhJOZ3MmbMVZN-S1TWG8Fw2XytXuBOmMFutMZbUnZrZS4KcXt3yfqaeib4fH7oVvLJaL1MxxXg80h-2OrbLeWRyoLtfqZxcpvR1ZHNnfoK9QFs3IeKrmVZ-bmIlfKqNRv9B23F6BzjKLAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
🔻
رضاییان در توجیه رفتنش به استقلال میگفت هواداران استقلال جنتلمن و با فرهنگ هستند اما دیروز هرچی فحش توهین بود بارش کردند وسط بازی هم کلی بطری سنگ و ... سمتش پرتاپ شد !
🔻
🔻
بله آقای رضاییان اینا همون هواداران جنتلمن و بزرگ استقلال هستند که به مادربزرگ مرحوم جلالی هم رحم نکردن!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/139148" target="_blank">📅 13:16 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139147">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">✔️
✔️
✔️
حجت کریمی مدیرعامل تراکتورسازی: چون دلار شده ۲۰۰ هزار تومان کسی نباید در مورد بیرانوند صحبت کنه. مردم به فکر مشکلات اقتصادی باشند نه بیرانوند
😐
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/139147" target="_blank">📅 13:13 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139146">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✔️
✔️
✔️
دنیل گرا مصدومیتش برطرف شده اما تارتار بهش اجازه شرکت در تمرینات رو نمی‌ده و باشگاه هم گرا رو نمی‌خواد ولی تا پایان قراردادش در پرسپولیس میمونه/ فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SorkhTimes/139146" target="_blank">📅 13:12 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139145">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ghypa6cncYggC53U_K07RqRFUmZd62aUnhcubYNOXkOB4IAoWN-XLYHY9Rwl5MexmsNQ3DIoyx_CXzil3MJTD9Ab_zkWk4CV8Ey1bWNxySELJPXl3K_yv6UvzdANts-M-XAsqcZ-bPnOtB7BtW_mJzjJshN_3KrZI1Pq_UpPV4EJfIzNs3Lfa02EEojlof6EUHcVSltCPtD_bzj_X1LYmUy242jsuJ43pA-aNaLFHNB2HRpcZdZR9_pzsBPb8PELW66f5ju-AMFU1FV5TpKjakYMg8sRWQpJoS-emuaQv-PR79w_WegLHGqTg13Y7jaPbD1-Rs3BAd9wRcPNnikpmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
اتفاق عجیب در لیگ عربستان؛ از هوش رفتن ۵۰ تماشاگر!
🔻
در دیدار الهلال و الخلیج بیش از ۵۰ تماشاگر به دلیل گرما و رطوبت شدید هوا بیهوش شدند.‌ بسیاری از هواداران نیز پیش از پایان نیمه اول ورزشگاه را ترک کردند. الهلال این دیدار را با نتیجه ۵-۱ به سود خود به پایان رساند.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/139145" target="_blank">📅 13:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139144">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">✔️
✔️
گفته میشه مدیران باشگاه گل گهر برای شکایت از باشگاه سپاهان بخاطر بازی دادن به کسری طاهری از تیم حقوقی پرسپولیس قبل از شروع مسابقه مشورت گرفتن!   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/139144" target="_blank">📅 11:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139143">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
فووووووووووری
❌
❌
یک سری شایعات پخش شده امسال بخاطر فشردگی تقویم لیگ خبری از جام حذفی نیست و قراره سهیمه آسیایی جام حذفی به چادرملو داده بشه
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/139143" target="_blank">📅 09:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139142">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🌬
پایان بازی  نساجی
0⃣
-
2⃣
شمس آذر
🔴
👔
اولین حیا کن، رها کن فصل در قائمشهر؛ روزهای سخت در انتظار مجتبی حسینی!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/139142" target="_blank">📅 09:02 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139141">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">✔️
✔️
✔️
حجت کریمی مدیرعامل تراکتورسازی: چون دلار شده ۲۰۰ هزار تومان کسی نباید در مورد بیرانوند صحبت کنه. مردم به فکر مشکلات اقتصادی باشند نه بیرانوند
😐
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/139141" target="_blank">📅 08:58 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139140">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
صبحی که ی بازی سخت و حساسی  داریم بخیر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/139140" target="_blank">📅 08:56 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139139">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZ_b3DFBnQ3lRPnAhZmwf9vjVdbOL2hvrrlgqit0R56F43nfjBsxKPNR931qwjuNsGagAtZCB8zZudKlDUZXiIuzdbkN9JnY2Cm0m4jxaJPrFYaWNKLxgEuN7p3euKIoaGOIm-CyN3fGz5Mh-79KRntA8SWJFzRb4bPrCEya2bUdUrE9TwdRTT9Jk-HnkmLr1D7PObMA4tuha80CBOEfGha7qKCXm-pAK2NUKRc86dHeLzIF7FLUklR6cWuMdWtKJ04TXlhzKycXNeP9KNDHtP6jjVsazdB8zYKamyqIYxsJt1EeqSwl2oQV1XALr9tmm9c2tt_lAGsEgdBs0cvR3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
ورود به اسپورت‌نود؛ ساده‌تر از همیشه!
🔗
دنبال یه راه سریع و بدون دردسر برای ورود به اسپورت‌نود هستی؟
🔵
با مینی‌اپ ربات رسمی اسپورت‌نود، مسیر دسترسی ساده و یکپارچه شده؛ بدون لینک‌های متعدد و مراحل اضافی، مستقیماً وارد محیط کاربری شو و از امکانات سایت استفاده کن.
🔗
ربات رسمی اسپورت‌نود:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت‌نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/139139" target="_blank">📅 02:24 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139138">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/241731bcb2.mp4?token=qmPsaYKMYhZ8jDHIkHfP-AWQYqM4vBBCZnnveEWOwmjfa0XSvSqK1OGy8p4ntxZOPJ9BFG9-ZzMi3zs4bGdUwvuMv2tj7tBaaombnivPJYZ01aaJYeAoBv8zkLwq4N-2VX2FdH3bjSOvgsl6alTe6mYRtmxtDuc3PZgWhOSZaba_Bo8DGutRhqydSRydGdYyrMvpwRktC25Z16cKJxPWwKIC-ZHmvhBKrEvrWVX4OJ3wXRLO3c4qckAt-zjpPmJHLLm3E4oZwjuEse16EEplwfk3gluq-XbbO4sNzbaRKfZnb0Rl7HvsTV23xWmNFjv7pPIfeuXNM7b-YW7LAAHnQDTCkwnvS4IcAEArTRliVZCiH3z5nWjIchwLr5hmaJW6W_WyA4AXlZ3IsMEKG80hrYoleJFCgNOVzrA5tvh28ggj5tor4UrKSLEgiPqUwMZRSLwnf1vLoRucFjWY1zA3LjxkIoimjY95qGlwsP30e5QjTd-84DDsjO-L2TBa2bj98JUX8vlSlBfws6e3nvc5W3gbzmFxHcIz-i341QyI84idSqky29vqYHWGTRQ37e58KsxxvWXRwxlKHQiiH0IlvkhMUKoZ18Ust-UorHpe2zVcvor4gTqWs3DwGFQqKEWaXp6btzLUGS6jKcmS_hjehDHAWqJCfPKDKSDHevu8Mpk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/241731bcb2.mp4?token=qmPsaYKMYhZ8jDHIkHfP-AWQYqM4vBBCZnnveEWOwmjfa0XSvSqK1OGy8p4ntxZOPJ9BFG9-ZzMi3zs4bGdUwvuMv2tj7tBaaombnivPJYZ01aaJYeAoBv8zkLwq4N-2VX2FdH3bjSOvgsl6alTe6mYRtmxtDuc3PZgWhOSZaba_Bo8DGutRhqydSRydGdYyrMvpwRktC25Z16cKJxPWwKIC-ZHmvhBKrEvrWVX4OJ3wXRLO3c4qckAt-zjpPmJHLLm3E4oZwjuEse16EEplwfk3gluq-XbbO4sNzbaRKfZnb0Rl7HvsTV23xWmNFjv7pPIfeuXNM7b-YW7LAAHnQDTCkwnvS4IcAEArTRliVZCiH3z5nWjIchwLr5hmaJW6W_WyA4AXlZ3IsMEKG80hrYoleJFCgNOVzrA5tvh28ggj5tor4UrKSLEgiPqUwMZRSLwnf1vLoRucFjWY1zA3LjxkIoimjY95qGlwsP30e5QjTd-84DDsjO-L2TBa2bj98JUX8vlSlBfws6e3nvc5W3gbzmFxHcIz-i341QyI84idSqky29vqYHWGTRQ37e58KsxxvWXRwxlKHQiiH0IlvkhMUKoZ18Ust-UorHpe2zVcvor4gTqWs3DwGFQqKEWaXp6btzLUGS6jKcmS_hjehDHAWqJCfPKDKSDHevu8Mpk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#منهای_پرسپولیس
👤
فراز فاطمی سرپرست چادرملو:
❌
آقای حیدری فکر کرده ما خریم. قشنگ بگید میخواید یه تیم ببازه دیگه اینجور قضاوت کردن بخاطر چیه. امیرحسین حسین‌زاده با تکلی که زد دوبار باید اخراج میشد ولی حتی صحنه به وار
هم نرفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/139138" target="_blank">📅 01:20 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139137">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">✔️
✔️
براساس‌صحبت‌های‌مهدی‌تارتار؛ سرگیف از بازی فردا مقابل ملوان به ترکیب سرخ‌ها برمیگرده و تارتار میخواد زوج علیپور - سرگیف استفاده کنه اما اوستون اورونوف همچنان نیمکت نشین خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/139137" target="_blank">📅 00:57 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139136">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❌
❌
استقلال فولاد مساوی تموم شد.کیسه خیلی خسته و کوفته شد و واسه دربی قانونا خسته میاد تیمش امیدوارم استفاده کنیم   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/139136" target="_blank">📅 00:29 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139135">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
کشاله‌درد دوباره شجاع خلیل‌زاده در بازی امشب مقابل هواداران یزدی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/139135" target="_blank">📅 00:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139134">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
کشاله‌درد دوباره شجاع خلیل‌زاده در بازی امشب مقابل هواداران یزدی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/139134" target="_blank">📅 00:13 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139133">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32fe7cb793.mp4?token=nX66md2mEsmMa0jgqaT4Hnvrv8fsOUNr8fP8Q6-4HDVJmCrG22bVdT-DvFpuZcLmkuFTgAUF-VKLACIBTGjRu9VIqsp69yby5PankxYxTH6fghEWGdQqmEUn99RoBXdQXJeuMOFG2bu51AvjvrJq2KpTmJszmQCkDQcZ0EMF9qyixFZSE5VUEddEcPZqSlSAKXxzzDcB6tlQmUQYFgEL4yb_tDgUrdlSzJBdf48T3GRv7Ggi8NMTKlQA4VtySNjULSTHwmY2qYB8usmwlu5vYozrMMEe5j6zvvixN98OzxGHBhcg3WrNtRcPkn-QFS6nsnV0XgS4PSvCxzMIyueWPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32fe7cb793.mp4?token=nX66md2mEsmMa0jgqaT4Hnvrv8fsOUNr8fP8Q6-4HDVJmCrG22bVdT-DvFpuZcLmkuFTgAUF-VKLACIBTGjRu9VIqsp69yby5PankxYxTH6fghEWGdQqmEUn99RoBXdQXJeuMOFG2bu51AvjvrJq2KpTmJszmQCkDQcZ0EMF9qyixFZSE5VUEddEcPZqSlSAKXxzzDcB6tlQmUQYFgEL4yb_tDgUrdlSzJBdf48T3GRv7Ggi8NMTKlQA4VtySNjULSTHwmY2qYB8usmwlu5vYozrMMEe5j6zvvixN98OzxGHBhcg3WrNtRcPkn-QFS6nsnV0XgS4PSvCxzMIyueWPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
کشاله‌درد دوباره شجاع خلیل‌زاده در بازی امشب مقابل هواداران
یزدی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/139133" target="_blank">📅 00:13 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139132">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/867c2d8104.mp4?token=YT2W3kdDVbTARlzJdUMoEv0H27F7Tdz2vpPtmLiz_uIXzHsnuhMLD4HWvOeSldWIi7oWAd9eihYvyJ8fmoaqEwEYh73jT45dvDWmG23Exd65jlKMCEPJRPwB_xiYdpu_iN4CGkv3iOrFySM7ZwqMkyu6-r6w8GI9wj5IQEAAjDzuI-nmcSP88Cx9xGOxLK1lxQOUb4My1DCqYWkmzbty1rF177I0wBx2QRKQwT31t0J6OKeitH7ihScLrnggeuYNP0tWhg3rnSeTi0h7gNfYdL8Da5yhMKK2Jlacb7-paxs4w5z_ig_C9vwxCxFqzyXB3cUlM2FdCURfceq94BttIUiNeiiN-6zl4Hy77fcVv5tud0L4YVXHKm6aVFAsFbsYmUTlu30_ZgJh-kZ5zD87ouLGg4mXO6QItjGvBrURn5kDRiL7K28vX7uS-A4b2bahnqJ6bqqHoQGaV9oODXyKEjOVSGxvSOIlLsCmLk8FwSsI9BemIgvTdlk4L9wLgrGeYLGJOCauvToN_a5iEB3uXKiPWA5547eD6H8H8NbEqas0zGf1WCqF9YMgjjJOejA5mayXyYugruor9W1b7P43yG0JMKkmy-NFdYhF_qdxp6VWTh4ax0W8jv_e31LPCq3m_235r4FQrIcDBsvQnIAOqRyHyM6EgE59Ex27zTXDht8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/867c2d8104.mp4?token=YT2W3kdDVbTARlzJdUMoEv0H27F7Tdz2vpPtmLiz_uIXzHsnuhMLD4HWvOeSldWIi7oWAd9eihYvyJ8fmoaqEwEYh73jT45dvDWmG23Exd65jlKMCEPJRPwB_xiYdpu_iN4CGkv3iOrFySM7ZwqMkyu6-r6w8GI9wj5IQEAAjDzuI-nmcSP88Cx9xGOxLK1lxQOUb4My1DCqYWkmzbty1rF177I0wBx2QRKQwT31t0J6OKeitH7ihScLrnggeuYNP0tWhg3rnSeTi0h7gNfYdL8Da5yhMKK2Jlacb7-paxs4w5z_ig_C9vwxCxFqzyXB3cUlM2FdCURfceq94BttIUiNeiiN-6zl4Hy77fcVv5tud0L4YVXHKm6aVFAsFbsYmUTlu30_ZgJh-kZ5zD87ouLGg4mXO6QItjGvBrURn5kDRiL7K28vX7uS-A4b2bahnqJ6bqqHoQGaV9oODXyKEjOVSGxvSOIlLsCmLk8FwSsI9BemIgvTdlk4L9wLgrGeYLGJOCauvToN_a5iEB3uXKiPWA5547eD6H8H8NbEqas0zGf1WCqF9YMgjjJOejA5mayXyYugruor9W1b7P43yG0JMKkmy-NFdYhF_qdxp6VWTh4ax0W8jv_e31LPCq3m_235r4FQrIcDBsvQnIAOqRyHyM6EgE59Ex27zTXDht8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎤
بخش دوم صحبت های تند خداداد عزیزی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/139132" target="_blank">📅 23:59 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139131">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🎙
درگیری شدید خداداد با خبرنگاران یزدی
!
پ.ن باز شروع شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/139131" target="_blank">📅 23:58 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139130">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">✔️
✔️
✔️
منهای ورزش :همراه اول تو جدیدترین شاهکارش، سقف مصرف بسته اینترنت ۷ روزه «نامحدود» شبانه رو از ۱۰۰ گیگ رسونده به ۲۰ گیگ!
✔️
اینترنت نامحدود تو ایران = ۲۰ گیگابایت!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/139130" target="_blank">📅 23:53 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139129">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❌
سپاهان از استقلال شکایت می‌کند
❌
❌
باشگاه سپاهان به دلیل استفاده از یاسر آسانی در دیدار مقابل استقلال از آبی‌های تهران شکایت خواهد کرد.
❌
❌
این در حالی است که چند روز قبل سخنگوی سازمان لیگ استفاده استقلال از یاسر آسانی را قانونی دانسته بود.
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/139129" target="_blank">📅 23:39 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139128">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">✔️
✔️
گل‌گهر از سپاهان به خاطر کسری شکایت کرد   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/139128" target="_blank">📅 23:36 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139127">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">📷
جدول لیگ برتر پس از پایان روز اول از هفته چهارم  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/139127" target="_blank">📅 23:31 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139126">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jq6qFwwKtTH9b67hTnXzULZrJXKlnYTXO_l-eEvf6Q-UcH5djKl44C_P2tOPW3DRoWNzHASIuws6WVE4mTyZTBx-F1E4KNV6EPlgsCtS9LB96WOpn2CI0rVsFh13G5m80K1iDeh3zeu9boeRVTVZkKpOHdsb2jzR9cKvFRconPeik3PV2TnHrBSMA_ARs-lmvl-LUpNLVMklsN6MmJ2dY1POZ6Cx1AM3nIm9evrVUgGi0BOQ-pS4o23Z9yDoigS3z3NAWrS8hxKUgb4Odzki6oZTPUxrlHWVjR0gvSUqZg1fZBtUiylu5gZdRlib7nS_ooPdAKwuxai1HRNNWptj3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
جدول لیگ برتر پس از پایان روز اول از هفته چهارم
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/139126" target="_blank">📅 23:29 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139125">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDH3kJt0E7N0knsf7gLqrtlJqYxlquY6hCI8DSpGdErIMOUGKCDd7H17TOGkkx5sZ2IexgWLCf2m88IxIWa3wTjY-Zwn3d9i89ktm6EiWF6rvaclV0dvPwihAxDi5Mf0CMuqekMlbcc33zsMtYPW5jKd2dcXeiluHNelZR9xLySFi8O-cvLnuZ1i0mYuwVUH1B07cSsIRGWo1j_-LBDjcVBat5ZQ_FpyOz-cHLhuzmL9bqpzRepxBV1tI-d_rJ4Vw-6-QKkKfu8unZ73cGElXV-xqndb7Nc81-kiB-c8RpGpQPLWMeOjMNaZw3MonKYn0-Jxc_PCLk15VwoOHlyD0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شرکت یوسف جامه اسپانسر جدید پرسپولیس شد و قراره ۵۵۰ میلیارد تومان در سه مرحله به حساب باشگاه واریز کنه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/139125" target="_blank">📅 23:27 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139123">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">✅
✅
سپاهان هم با دو گل کسری طاهری .گل گهر و دو هیچ برد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/139123" target="_blank">📅 23:25 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139122">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❌
❌
❌
آغاسی اخراج شد ولی قبلش آفساید بود و شانس آورد که دربی و از دست نداد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/139122" target="_blank">📅 23:24 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139120">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
آخرین تمرین تیم قبل از بازی ملوان؛ با حضور محمدحسین صادقی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/139120" target="_blank">📅 22:24 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139119">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">✔️
✔️
بند 500 هزار دلاری در انتقال بازیکن پرسپولیس به نساجی
❌
❌
در بندی از تفاهم نامه انتقال قرضی براجعه از پرسپولیس به نساجی عنوان شده است در صورتی که باشگاه مازندرانی خواستار دائمی کردن قرارداد براجعه باشد، می تواند با پرداخت 500 هزار دلار به پرسپولیس، قرارداد…</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/139119" target="_blank">📅 22:22 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139118">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🌬
پایان بازی
نساجی
0⃣
-
2⃣
شمس آذر
🔴
👔
اولین حیا کن، رها کن فصل در قائمشهر؛ روزهای سخت در انتظار مجتبی حسینی!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/139118" target="_blank">📅 22:20 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139117">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
🟡
احتمالا طارمی و سردار امشب برای اولین بار مقابل همدیگه قرار میگیرن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/139117" target="_blank">📅 22:17 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139113">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L5ZyfUvOLKxvtkEEgPPH7MZ7MFLogvZQSt3ZKel7iVXiNFn8oI_V31HCV5HegMbjjC4ZWOFOpcuxJn7gZyzSnDz_EZMyYyKw3yA2TyqI4hIRubN5vFAr0GZU7413QHxqKCUDX-LYpe78QjkZc04yvyIwKlQenS65vuuYNgfOSa8ptX3UPtfMAdyr3soH2lke9ERfiL4fGpDe5CBcXZsJbU0cYvhZAFRwC2t67dNMWmzWVPpq0lbVLys8dDCmO2ujZWfWlxfctoL7u4dyYUuH3xTQqKufnexZOEyEMi2DeO3SvCy0SqZdtfD-ogpBkNadoOdqpZWIK3rQyCakQkT_qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QArk360OJ4M6wUGLDF-LE2srrvymwJ_7lG_yBgOsx5rbv-Ha-cW4aTF624wcqLUBIU6OhKtl9PVbgVWAYiLUKIJwiP3MNx_FDd_49fZHRAycmD7Bo86qx8F18DXiR1QoV_kzFUlhz5HNQmeog03T8bF5IuFm-YiuiYcWHObk3iiYT4tehYxxQuUiU3V-Ymg2eGaDG11mmSFa1_QLY9QE0Xt2IV_0tjw2I8N7qnV1XASUvs7voNto3Rr_SRFPEJQDfsR7U0PUXctheWUT06CO-QO1ZzpW7pXIiHtPVlmUS8VDo976YoKNOWnSdHRp3q5G1CgBYeYZOTIqZxrnGt8Fxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KUkSOn8gYr78FRTt4PQrq_zwPpDxJPjTmeNrhPDU5WxJS2xa5pbAfXbtu9gaQ52q8Ec72znWhmwEMnffx4xvUch7xFCOQeqPV7QhV-Humy9uCA5Z9wIXc23fBdvO_fArB3wYUsfvwG_5K0pCkKymHD7MARQwjzWlzzLL87SpflOl9fUTOIBl6epMGEPvT88MupzNKW4bcLmsoS78L_443MHFE-P2ksQ40_ytCFj-mWiVkZiaGJNbOHJh30Jag5-HkEP3Uta9Je2WNMAS5AXxwzj9_M3-1NF1pIaKik-ubixARB_e1dDo0yzrgqxi2DcNPkIe0xlJuh_Jf4pTxF8KZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cDak6HDiD4T76UmS_rl1IY8-DXJynNEl1NJvZ8K4WFXvEw3mykBWiISUuE01QRXLEuCVSGOj5dLELV9sbdFRfHTrzB_DtpKB24h7NghQNmsJZw_fof_seTrH3oYs6Ag7ETKzwQilmGAuMkzo9D-Yj0bf7hC63zmHLWgBaMjf7iDiCOg8cy--HEMapwR9abZ3ToyjRddcyLZGTjPhEz_qyxi5fjwDwZEg34X_-i5Oy6oEsW53fmrwzUNPdgL3UsTGMBih1pzDxhWn8JZ9_dfd-Ir3KHPeihGpktWZYIUH7-xfWlzNXFKKVPRM9VxdaH8H8mrlplXIGZKAHyV7Ah1yfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽
🤩
پیمان حدادی، مدیرعامل باشگاه پرسپولیس، به همراه ناصر محمدخانی، بهروز سلطانی و مرتضی فنونی‌زاد رفتن سر تمرین امروز
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/139113" target="_blank">📅 22:11 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139112">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
خبرگزاری فارس: تارتار دلش می‌خواست سرکیف رو جلوی تراکتور بفرسته داخل ولی تو ذهنش یه تصمیم تاکتیکی گرفت و فکر می‌کرد شهرآبادی می‌تونه بازی رو دربیاره
🚨
تارتار همچنین علاقه‌مند به سبک بازی سرگیف هست اما تعدد بازیکن تو تیم‌ باعث شده به همه بازی نرسه
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/139112" target="_blank">📅 22:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139111">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✔️
فرصت‌سوزی باورنکردنی فرشاد احمدزاده مقابل کیسه
😐
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/139111" target="_blank">📅 21:53 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139110">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cS3rMuDtfYMDg32qLQAlKwDmQdWW4sBDNue6HQIWtm_eI00qyrt3lBRb3NVHuL_1zNGMYegjwX5OFgOBEu40GBkj5Y5E1s2bxIdEvPb-bL-3qnD0adnbo_OJa160PUj6RyQ0GfVDej47mkfYzKTIhbYdnQLTRSJw--eMekwC6NGzm6vqsKSn2xiPt9ik1pLs87kOBk_t9BuGcUY6P4bMiJAt0g_66O2CBr-qPsTRlGWQ8A532vLSIawsNVcCBpxrMJ8phijNtBYxj2r79sS-MQ9OOYV1Y-4FuXAn2GdmFZU2rS6WuYVCH1GJoclyR4Y2-dBAWOK1NZxT0DQibu4-YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
حسین کنعانی ، دانیال ایری ، مجید عیدی ، پویا پورعلی و محمد عمری پنج بازیکن تیم پرسپولیس که سابقه پوشیدن پیراهن تیم ملوان دارن
✔️
فرزین معامله‌گری هم که برای سربازی منتقل شده به ملوان تنها بازیکنی که سابقه پوشیدن لباس پرسپولیس داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/139110" target="_blank">📅 21:36 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139109">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">✅
✅
تراکتور دو بر هیچ برد و چهارمین برد تراکتور رقم خورد ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/139109" target="_blank">📅 21:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139108">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAk87NjO3ZwZhqns3739c8ZlSqXE8_HetCcm2qWejPy4u2nyyF_OoXSFPGf2kyg5etLa4BrCl5Jz9SN9zXDKmUQirSdjhYaVSEkt2o0QHxy0AFPNT7CvBAo3M10qj0T7nn_Y6tUTez6uAQV4_b1mFgQIrbNFUdVE1ivebNdnBrYZM-EtoYW47_lpDj0mqrv4xxqisfE3RNjKX-Ib0C-avdiE-hpDCF0SuYGqEp10SIodKKNu4VIIt2EZp4PHaIn14yYZCyXfeIgg3VrJQvVFJbVSvmWCQufYzOSJtEvZBeZ62DlvaVjVtrYke5YWQ-tHM3vu5UJLYfjyCOAyCpkPZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
تراکتور دو بر هیچ برد و چهارمین برد تراکتور رقم خورد ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/139108" target="_blank">📅 21:19 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139107">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cbe495b77.mp4?token=N70a1iYfN66SEn0qhlWpisOVQECeMG1tq8ejzHYVueeS5RV-FWkarmjGSoMQc6QtYI1lrJJw4UvZWYb_eZknsVuz9PUkIWJs6HL_FP5-2lRnEfZpQTMCAyx4peiyAQboPnFYopzQIg0f6wyll1k-OJD7B59yvV4d6gX-E6FT1iFiUfZBLXmXjwTSaxT69fhQGTHum4_B6swSlEBqLGsMqgxpqUu5lcflMcsW3-fF6nIkV7lxZEEJZvkdGa4WYvFi6ffnsWKKUiw1CZTJVEjfzjvGEKNM410Tpi7IYtvxiNzajBH7InHdwqjhRWJX65u_aYfGdZH8-9NJUyxw_tD18g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cbe495b77.mp4?token=N70a1iYfN66SEn0qhlWpisOVQECeMG1tq8ejzHYVueeS5RV-FWkarmjGSoMQc6QtYI1lrJJw4UvZWYb_eZknsVuz9PUkIWJs6HL_FP5-2lRnEfZpQTMCAyx4peiyAQboPnFYopzQIg0f6wyll1k-OJD7B59yvV4d6gX-E6FT1iFiUfZBLXmXjwTSaxT69fhQGTHum4_B6swSlEBqLGsMqgxpqUu5lcflMcsW3-fF6nIkV7lxZEEJZvkdGa4WYvFi6ffnsWKKUiw1CZTJVEjfzjvGEKNM410Tpi7IYtvxiNzajBH7InHdwqjhRWJX65u_aYfGdZH8-9NJUyxw_tD18g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
فرصت‌سوزی باورنکردنی فرشاد احمدزاده مقابل کیسه
😐
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/139107" target="_blank">📅 21:11 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139106">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❌
❌
❌
ترتر گل اول و زد و الکی الکی سبک مجیدی یک هیچ یک هیچ داره می‌بره همه رو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/139106" target="_blank">📅 21:08 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139105">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f35N2cm8dh82fjfWVFJnKjuQFXETfSpfFIKR7nbjWvex51f9dOHRbtcu99X9zmf-GKyJKkg-yKNBLAv2RCcuqpKb3r6zj1gFZQiJ_G596oyODrwzB4dtB4Rzk6MmsLweumd8eS7F3wKofHrNmCaRifAZ0H1rZuZjqqDPS8hxoaWiWr9WDvPtLzeWiQXvGxoq6As-6bGz36O07DZm1gt1OL2kTCxfwneLs5_JKPJKimc1TMniLzQZQe4AhEhGtOZR78mWMBdzpsgT3NUx8IhA9z74RLkvgFpQs7eBrZN3uk1hOHlHmJoyqY0_GT0inx7jMUJKBshMt_Y7aoBJxmkndw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
آخرین تمرین تیم قبل از بازی ملوان؛ با حضور محمدحسین صادقی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/139105" target="_blank">📅 21:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139097">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">✅
حالا که حوصلمون سر رفته تو عصر جمعه میتونیم بشینیم پای بازی ترتر و چادرملو رو ببینیم که انشالله مساوی یا باخت ترتر و شاهد باشیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/139097" target="_blank">📅 20:18 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139096">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QSm6M-wJdowiw4yTU5qzlONKH5pfQ-HGpEUuQGreACI8w9OHZpXr0bNdwc1c06C7inKbGEKlPUQj948um-pTDi0yJ7lz7M4t-v6_YwOYqL9FkOvmKcyUakcvLvnenpkUHqh-fJD7utqyXBxWujRyNLTKinv8idIgyAW1PNm2utZbFSvLfEOgHBW9EDcjectPbmvaMlh6Ph7iPdMSs9E12CHEO1g0nzkEqG3_eQlXo72nbeE2Ris1LoV6dHjXep6RalMZ4JZagBXz6QxXvzT4o9_PnBCELrTMCqfpR-lcz8r-98s97YvEXEj4yaDgj4hn3IQ8w-NhDuz-3DMtqkBtCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
دو مدعی، یک زمین، ۹۰ دقیقه نفسگیر
جنگ امشب در اهواز کفه‌ی ترازو رو به نفع کدوم تیم سنگین میکند؟ همین حالا میتونید این دیدار حساس رو در اسپورت‌نود پیش‌بینی کنید.
[
فولاد
🇮🇷
🆚
⚽
استقلال
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/139096" target="_blank">📅 20:15 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139095">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">✅
حالا که حوصلمون سر رفته تو عصر جمعه میتونیم بشینیم پای بازی ترتر و چادرملو رو ببینیم که انشالله مساوی یا باخت ترتر و شاهد باشیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/139095" target="_blank">📅 18:58 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139094">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">✅
حالا که حوصلمون سر رفته تو عصر جمعه میتونیم بشینیم پای بازی ترتر و چادرملو رو ببینیم که انشالله مساوی یا باخت ترتر و شاهد باشیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/139094" target="_blank">📅 18:57 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139093">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
بازی تیم های مدعی در هفته چهارم
❌
چادرملو - تراکتورسازی امروز ساعت ۱۹:۰۰
❌
سپاهان - گل گهر امروز ساعت ۱۹:۳۰
❌
فولاد - کیسه امروز ساعت ۲۱:۰۰
✔️
پرسپولیس - ملوان فردا ساعت ۱۹:۱۵
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/139093" target="_blank">📅 18:54 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139092">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">⭕️
⭕️
فوری/ آکسیوس : طبق گفته مقامات آمریکایی فشار اقتصادی به ایران تا بعد از انتخابات کنگره و سنا آمریکا (۱۲ آبان ماه) ادامه خواهد داشت و بعد از اون دوباره میرن سراغ بمباران و حمله نظامی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/139092" target="_blank">📅 18:50 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139091">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❌
❌
فوری/ با اعلام مهدی تارتار باشگاه تا 22 شهریور بازیکنی به تیم ملی امید نخواهد داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/139091" target="_blank">📅 17:36 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139090">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
فووووری/ با اعلام فدراسیون فوتبال بازیکنان دعوت شده به اردو تیم ملی باید تا پایان روز شنبه هفتم شهریور خودشون رو به اردو تیم ملی امید معرفی کنن
😐
❌
❌
اگه پرسپولیس بازیکن بده عملا ایری، شهرآبادی و لطیفی فر رو برای دربی نداریم
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/139090" target="_blank">📅 17:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139089">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa7be285b4.mp4?token=JUjEKKO81gQcDHxZeU39XTgSkqGCVX2JbC7Dek53zHlH4d1pB6Z81Q1oT3mjL00tx9gw7uR_ayyITq_f2JQj7uRkNodnRkS2gk582hWIgIfTuRpnh4ZJ6gTmw9xRQrdaQABHat6lzkOlq62aP0jl9Q9B6_IlmDiEqGY6umnBAJyyQSikx8K4dqKo5qKhF42S3sA3gSUOgw1IDwb0LOC5017STm-D6ssjM0EWNzWJBHk1NuVDNL98-yeqXWgCapelu8TX_pjpx5WbaGyb0ENvCvrayskSNLaNF3Mmv0Nm4twBMk_q7MRudy5dW63alPzG5vJxJJgDV5ezuGa-6zXN4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa7be285b4.mp4?token=JUjEKKO81gQcDHxZeU39XTgSkqGCVX2JbC7Dek53zHlH4d1pB6Z81Q1oT3mjL00tx9gw7uR_ayyITq_f2JQj7uRkNodnRkS2gk582hWIgIfTuRpnh4ZJ6gTmw9xRQrdaQABHat6lzkOlq62aP0jl9Q9B6_IlmDiEqGY6umnBAJyyQSikx8K4dqKo5qKhF42S3sA3gSUOgw1IDwb0LOC5017STm-D6ssjM0EWNzWJBHk1NuVDNL98-yeqXWgCapelu8TX_pjpx5WbaGyb0ENvCvrayskSNLaNF3Mmv0Nm4twBMk_q7MRudy5dW63alPzG5vJxJJgDV5ezuGa-6zXN4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
مهدی تارتار: واقعا یک تیم نمی تواند 90 دقیقه تهاجمی بازی کند. ما باید طوری برنامه ریزی کنیم که بتوانیم به شکل خوبی 90 دقیقه را به پایان برسانیم
. زمین چمن یادگار امام تبریز واقعا استاندارد نبود و کار را سخت کرده بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/139089" target="_blank">📅 17:08 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139088">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f04141bbb0.mp4?token=PSc28AN-V1jo33UnCJ0bhL5m3cQo_rHi06I8yZ--188PEQdHYliNDUIPIJsoOzFns2gwnhMpOtLUfIordbQkz0DzS0QnaswdlYfWkpSwjrGsG-XM_u0Pu0WsmBVDPBLmHnH1m8PyDUbSuihsl_KsXWgsGyuj1rDgo1g_LuYudKQmJmwAF7m7huwv1IDhsyLbfDucAN6sKVPKx8mQPdLnp590HiJhE5M6au6hCADqy2qGKKxvxeiv7Kg07vHl3gJocpouLT5O1HVNuGEiFIQNeYHKduuvtzaHhdU6RmbiqPPF9KcRCLVPi8LNdMPBfm4hls2HwcdX0qcE-K8fidbJSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f04141bbb0.mp4?token=PSc28AN-V1jo33UnCJ0bhL5m3cQo_rHi06I8yZ--188PEQdHYliNDUIPIJsoOzFns2gwnhMpOtLUfIordbQkz0DzS0QnaswdlYfWkpSwjrGsG-XM_u0Pu0WsmBVDPBLmHnH1m8PyDUbSuihsl_KsXWgsGyuj1rDgo1g_LuYudKQmJmwAF7m7huwv1IDhsyLbfDucAN6sKVPKx8mQPdLnp590HiJhE5M6au6hCADqy2qGKKxvxeiv7Kg07vHl3gJocpouLT5O1HVNuGEiFIQNeYHKduuvtzaHhdU6RmbiqPPF9KcRCLVPi8LNdMPBfm4hls2HwcdX0qcE-K8fidbJSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
مهدی تارتار:واقعا از شکست پرسپولیس مقابل تراکتور ناراحت هستم اما این هجمه علیه ما طبیعی نیست. ما اینقدر در ۲ بازی اول خوب کار کردیم که رقبا ترسیده‌اند. احساس خطر کرده‌اند از بازی‌های خوب پرسپولیس!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/139088" target="_blank">📅 17:00 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139087">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ef45c0a06.mp4?token=A-Lng72GHrkpBHxSEKWsKDvR8-3egAtUf562Fsv2B9oWZNvUNDnCaiFZmIhSkSRWsqsGYt2IdFHbgMG2zIV-JnJcHGAACQWaCXHR_xNtS6i63LZ-Kt2BnDpPtuL4ixqE0JWI19yIJLv-u_fmhP8RqJiUSL3Se1vq4pwcm7EXrt2uq6JY5cjW2Qi6nm6BBc2gbsDTM6IQ_g7UhMWaRUR_4lwReBoBJyraA8GBfpKuQ_voXpJaSVK6EbwCGn5la9xKfz3lqb8aEgQ_PjrJqdF9JS_K9Z3Lto5s9YbgJ7uTMx4Z68aTYRvECXEj2qBL9nbCdYOLL1Q8fx2uHhWQLXmLCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ef45c0a06.mp4?token=A-Lng72GHrkpBHxSEKWsKDvR8-3egAtUf562Fsv2B9oWZNvUNDnCaiFZmIhSkSRWsqsGYt2IdFHbgMG2zIV-JnJcHGAACQWaCXHR_xNtS6i63LZ-Kt2BnDpPtuL4ixqE0JWI19yIJLv-u_fmhP8RqJiUSL3Se1vq4pwcm7EXrt2uq6JY5cjW2Qi6nm6BBc2gbsDTM6IQ_g7UhMWaRUR_4lwReBoBJyraA8GBfpKuQ_voXpJaSVK6EbwCGn5la9xKfz3lqb8aEgQ_PjrJqdF9JS_K9Z3Lto5s9YbgJ7uTMx4Z68aTYRvECXEj2qBL9nbCdYOLL1Q8fx2uHhWQLXmLCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تارتار سرمربی پرسپولیس:
🔹
ارونوف یکی از بازیکنان خوب تیم ماست اما دیر به تمرینات اضافه شده است. بحث مصدومیت ارونوف جدی
نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/139087" target="_blank">📅 16:59 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139086">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7eb7a5402.mp4?token=LATpvEQZj4mOkgtt8Ftr7UsYsuVcMKEUoNs8mI_vEbNcLItHvZKABoGuG7x9SrtEVI92DoLlDaJLxF3pRjAVQW4BzAEIuborz3q0X96EETu-yFlOZ0T55Oj7tlVTzPRO5XCqQPo1kgvuidNOHgRf9mGZgsRnhWRBrnlCGr1V_hflMVCZJcly_lIV3v2eQzANyGqjK_aQ2RLsUAXlJiwKkHI4RokcEUBZl5nyP0IQw53HKEUQg_g-cOh3Rrm_l6EZIMr2Lh4q0hxuTy3fSTDBLhdRlfxhKEhj-7q_znBzBOiBmODh_v53ntuUPLtgKZJdMEnl91g6sjQF0Fm--7v5Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7eb7a5402.mp4?token=LATpvEQZj4mOkgtt8Ftr7UsYsuVcMKEUoNs8mI_vEbNcLItHvZKABoGuG7x9SrtEVI92DoLlDaJLxF3pRjAVQW4BzAEIuborz3q0X96EETu-yFlOZ0T55Oj7tlVTzPRO5XCqQPo1kgvuidNOHgRf9mGZgsRnhWRBrnlCGr1V_hflMVCZJcly_lIV3v2eQzANyGqjK_aQ2RLsUAXlJiwKkHI4RokcEUBZl5nyP0IQw53HKEUQg_g-cOh3Rrm_l6EZIMr2Lh4q0hxuTy3fSTDBLhdRlfxhKEhj-7q_znBzBOiBmODh_v53ntuUPLtgKZJdMEnl91g6sjQF0Fm--7v5Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تارتار
:
❌
• وضعیت ابوالفضل جلالی بهتر شده است/ بازی فردا مقابل ملوان را فدای دربی نخواهیم کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/139086" target="_blank">📅 16:57 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139085">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/587e6b7701.mp4?token=ZY4oaKVVHE6y9pEOvemtn3f7Z9IhwZ5jWeELuUn2fevTE_L_HgW6bw-Ahh15RBS384wL3VJmVx9dPMMAL7XezPzmeq_GsuftOiG2dhiCRVNBjCdrkeJqhCDh7QQAAgxItD02v3dKGWmhfLVQcGgtpBmr3aKGfc_eoRUjJlj_Ff5lXM13jrw-bLkTk8wIZMDjkRzMN74H_nlQYRL6iSKQQ7fivnYbnf-hEtToWQ7qmf71wkx37nfJt4PC9mRpjVIA_I14pWmVVkq-MLMy52GGHPQvRUrRRHX7S3NpaZAESV1839d3p52YZU3a5vcAINOGvxaFJoYrErCxIxxOHaqThHaz9cWSq8qmWGftP_ApEX9w1U4CZjPynmjm9FghgFqEdwBDBXfnxBVYXZIlst73jFZ0jXB38MmsZ0laIMSduc6u1Nn9NXG2z5Nw2-EExwKk8TMWe-k6aaVKzHw5ps2FOEOkJdEEVVs76JaOVXMPTWBLBSHzSKt6eikCJF4W4hSX1DDdb6a8oRfcAKgqTZpQpmxUUdy42pO9orpRfbNhkRqmm5FKrxKI1DMR6YCC98Fz2w62qiZDDJ83Yrq8KbWyLi4zE12ZZ5RZxow6FllW5qr1V9Ey1z6jZNZlORdK3DdwRnW1TIDkbQ4pBRkC0uRvOfu80MCnQTVmilIyjNG8WdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/587e6b7701.mp4?token=ZY4oaKVVHE6y9pEOvemtn3f7Z9IhwZ5jWeELuUn2fevTE_L_HgW6bw-Ahh15RBS384wL3VJmVx9dPMMAL7XezPzmeq_GsuftOiG2dhiCRVNBjCdrkeJqhCDh7QQAAgxItD02v3dKGWmhfLVQcGgtpBmr3aKGfc_eoRUjJlj_Ff5lXM13jrw-bLkTk8wIZMDjkRzMN74H_nlQYRL6iSKQQ7fivnYbnf-hEtToWQ7qmf71wkx37nfJt4PC9mRpjVIA_I14pWmVVkq-MLMy52GGHPQvRUrRRHX7S3NpaZAESV1839d3p52YZU3a5vcAINOGvxaFJoYrErCxIxxOHaqThHaz9cWSq8qmWGftP_ApEX9w1U4CZjPynmjm9FghgFqEdwBDBXfnxBVYXZIlst73jFZ0jXB38MmsZ0laIMSduc6u1Nn9NXG2z5Nw2-EExwKk8TMWe-k6aaVKzHw5ps2FOEOkJdEEVVs76JaOVXMPTWBLBSHzSKt6eikCJF4W4hSX1DDdb6a8oRfcAKgqTZpQpmxUUdy42pO9orpRfbNhkRqmm5FKrxKI1DMR6YCC98Fz2w62qiZDDJ83Yrq8KbWyLi4zE12ZZ5RZxow6FllW5qr1V9Ey1z6jZNZlORdK3DdwRnW1TIDkbQ4pBRkC0uRvOfu80MCnQTVmilIyjNG8WdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مازیار زارع سرمربی ملوان:
🚨
پرسپولیس پرمهره ترین تیم ایران است و کادرفنی خوبی دارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/139085" target="_blank">📅 16:04 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139084">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
بازی تیم های مدعی در هفته چهارم
❌
چادرملو - تراکتورسازی امروز ساعت ۱۹:۰۰
❌
سپاهان - گل گهر امروز ساعت ۱۹:۳۰
❌
فولاد - کیسه امروز ساعت ۲۱:۰۰
✔️
پرسپولیس - ملوان فردا ساعت ۱۹:۱۵
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/139084" target="_blank">📅 16:00 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139083">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
بازی تیم های مدعی در هفته چهارم
❌
چادرملو - تراکتورسازی امروز ساعت ۱۹:۰۰
❌
سپاهان - گل گهر امروز ساعت ۱۹:۳۰
❌
فولاد - کیسه امروز ساعت ۲۱:۰۰
✔️
پرسپولیس - ملوان فردا ساعت ۱۹:۱۵
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/139083" target="_blank">📅 15:57 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139082">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ypeg10V5iQoXE11Cl4BVdHBSINnBmvBuoZBORmL45iScoIK73xiCiXc020RZWX8bKM4tjreUKqnjMU3qHaD8bYV97U7ylvE0U78ZjEFzrfvEo6PfndROMEo3aURf4SImjD4nAvGGBlYCvtiAZtsGQfnjFeTRTA-yPO6cEVBJid6jR8iJDij3-kmrjB3SMiDhqBnofGl4AO-OqQctFtl8Ae9cCxJ8dFujJMaGgiH9MKy7HonxaQnpfMdfMQfc2WH4cpMSESt4YRqGLj1b3lYspJkGHJvxpMR626auss4LubIjyWf4vGV4k6hzJhqQcOGihnSpJIgqcQDRzE5lcUeETA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خبرگزاری فارس: تارتار دلش می‌خواست سرکیف رو جلوی تراکتور بفرسته داخل ولی تو ذهنش یه تصمیم تاکتیکی گرفت و فکر می‌کرد شهرآبادی می‌تونه بازی رو دربیاره
🚨
تارتار همچنین علاقه‌مند به سبک بازی سرگیف هست اما تعدد بازیکن تو تیم‌ باعث شده به همه بازی نرسه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/139082" target="_blank">📅 15:52 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139081">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cCiagZXfcyrpsJf4B9klawKjt6ZY7s0XrqMQxq6ZOv0vspO9P-ShFPKTmPyvn3kvYlTna-DWhGFmFs4NJYuz8LAaHoBr3O0bum1ztkuofpDxTDy4d52-aavrAWuIcf-oKi_RQp5QlRnyutv-nvLHI23wAMk3ScoAH7sscROnaWaDBqI_ArI84L99JMhZU9bJtKZclr9q7k68t1aM3iBbUM9KvZLnTALPF5GQBZp5lOvcXrIoEfQK2zby3vZlnoPxAhEzy-dFVF19MOvJS6W-VuTl_uhsFzM4OVU2EXb1N1UTDQZGjYyPMQ9g51sMdWWw90fbHUMCJYdFeT9CGkg6rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🟡
احتمالا طارمی و سردار امشب برای اولین بار مقابل همدیگه قرار میگیرن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/139081" target="_blank">📅 15:52 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139080">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ua00xS_pfjDQlIn5qGGZ-sqzs7DyBqu0MPZyO12Bz2DmjP47s_aV3Shaq2sekMvMBWJ_5AOEyN_B2p94H-kGczdKKkHNh3H6uxT1Djetp0ZmpoqEdE8-KdWOJpRNUf7hYZOlOPptzZdLSjAn6VFVOHV_raJ7VJwvQllh76VSb5yGeJUD6gIclllTg21EqkCc7sbHAmXMXJd28y1yFHCsFR9nyjsawiczMzuaOrDSORjgRJyZ61D9PvYPofK0Fk-uTl5Ybf6Bh84dGYdW9x-RGudSATqy1oeUAYWPwrls67gMeMP5Ogwam_zdS3h5FV5WQG6A3seCTrs9ru-DmC64nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😀
💵
مهمترین بازیکنان آزاد ایران و ارزش آنها در ترانسفرمارکت تا این لحظه:
🔻
محمد محبی
- 2.5 میلیون یورو
😀
مجید حسینی
- 700 هزار یورو
🔻
رضا اسدی
-  500 هزار یورو
🔻
فراز امامعلی
- 450 هزار یورو
🔻
علی کریمی
- 350 هزار یورو
🔻
مهدی مهدی‌پور
- 350 هزار یورو
🔻
ایمان سلیمی
- 250 هزار یورو
🔻
امیر عابدزاده
- 200 هزار یورو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/139080" target="_blank">📅 15:51 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139079">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WMxoLAS57qxisXtbWdOOjEPgC7UzrfDRMU6K1BpD8Z2cpm-sVZSJYT8C8ITvwypj_TqtsoDflNuwOUnGrHWnBrZaXw8NO38WZoQ_6mJivdGXDKWe6vxkHYFjMOzJKs20z1D_hIiIOy8IsRnYvk_FwyMnb8JHAGT9_x8wEEjsiujaztXRnGyL1j00bZjZxq5GniAZ0oQe2j6B9fVmMoHsf4aqouB1noZwejy2htouI4W4f8Tv4_Ct5Kb_3EQSXbcXjfpzvYok27UX8-0G8da7f7aAnPoVQifYIht7glP_pvMpqqqm-3z52-F9sUmjVuGEROChQcLS3VpG6dAHOu1KPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
چادرملو برای فرار از روزهای سخت، امروز باید مقابل تراکتورِ آماده دست به کار بزرگی بزند؛ تراکتور با شروع قدرتمندش، برای حفظ روند خوب و اضافه کردن یک برد دیگر به کارنامه‌اش به میدان می‌آید.
[
چادرملو
🇮🇷
🆚
⚽
تراکتور
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/139079" target="_blank">📅 15:47 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139078">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❤️
فووووووووووووری
🔴
گفته میشه محمدحسین صادقی دیروز تو تمرین پرسپولیس با یک بازیکن درگیری لفظی داشته و توسط مهدی تارتار از تمرین پرسپولیس اخراج شده / هفت صبح
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/139078" target="_blank">📅 15:43 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139076">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❌
❌
تصاویری از تمرین امروز عصر سرخ ها پس از یک روز استراحت؛ارونوف بدون مشکل در تمرین گروهی/گرا و جلالی مصدومان پرسپولیس
❌
کنفرانس مطبوعاتی تارتار و مازیار زارع فردا ساعت 16:00 در هتل المپیک
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/139076" target="_blank">📅 14:22 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139075">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">✔️
✔️
✔️
بی انصافیه اگه از عملکرد خوب مهدی تیکدری نگیم!
✔️
برای اولین بار تو عمرش اومد پست غیر تخصصی دفاع چپ بازی کرد و هم در دفاع و هم در حمله موثر و خوب بود
✔️
✔️
پر تلاش و انگیزه از دقیقه اول تا آخرین دقیقه ظاهر شد و امیدوار مون کرد
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/139075" target="_blank">📅 11:42 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139074">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
امید عالیشاه به علت مصدومیت چهار هفته از میادین دور خواهد بود
💔
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/139074" target="_blank">📅 11:41 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139073">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🔵
🔴
کشوری فرد دبیر سازمان لیگ فوتبال ایران:
🔴
سهمیه هواداران در دربی استقلال و پرسپولیس ۵۰-۵۰ است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/139073" target="_blank">📅 11:39 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139072">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">❌
❌
ادعای هفت ورزشی: محمدحسین صادقی به علت درگیری با دو بازیکن پرسپولیس از حضور در تمرینات منع شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/139072" target="_blank">📅 11:38 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139071">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
مهدی تارتار سرمربی پرسپولیس، محمد حسین صادقی وینگر جوان خود را به صورت کامل از تیم کنار گذاشته است و هیچ قصدی برای استفاده از وی ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/139071" target="_blank">📅 10:26 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139070">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❌
❌
هادی چوپان مستر المپیا را از دست داد
✔️
✔️
هادی چوپان، پس از غیرفعال شدن ویزای طلایی امارات و از دست دادن مصاحبه سفارت آمریکا، از حضور در مستر المپیا ۲۰۲۶ انصراف داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/SorkhTimes/139070" target="_blank">📅 09:17 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139069">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❤️
صبح آدینه تون بخیر و شادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/SorkhTimes/139069" target="_blank">📅 09:10 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139068">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔵
ورود به اسپورت‌نود، فقط با یه کلیک!
📌
هنوز برای ورود، دنبال لینک و مسیرهای مختلف می‌گردی؟
📌
وقتشه راه ساده‌تر رو انتخاب کنی!
🔗
با مینی‌اپ رسمی اسپورت‌نود، همه‌چیز یکجا و آماده‌ست؛ ربات رو باز کن، وارد شو و مستقیم به امکانات اسپورت‌نود دسترسی داشته باش.
1⃣
-  بدون لینک‌های سرگردان
2⃣
-  بدون مراحل اضافه
3⃣
-  سریع، ساده و یکپارچه
🔗
مسیر ورودت رو کوتاه کن؛ اسپورت‌نود همینجاست:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
📌
کانال رسمی اسپورت‌نود:
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/139068" target="_blank">📅 01:23 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139067">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❌
❌
تارتار با حضور بازیکنا در تیم ملی امید خارج از فیفادی مخالفت کرد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/139067" target="_blank">📅 00:47 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139066">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">⚠️
یایا امپرور بعداز نتایج درخشانش تو عراق میخاد برگرده ایران…سپاهان هم یه نیم نگاهی بهش داره؛فورا باید اسپند دود کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/SorkhTimes/139066" target="_blank">📅 00:39 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139065">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
فووووووووووری
❌
❌
یک سری شایعات پخش شده امسال بخاطر فشردگی تقویم لیگ خبری از جام حذفی نیست و قراره سهیمه آسیایی جام حذفی به چادرملو داده بشه
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/SorkhTimes/139065" target="_blank">📅 00:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139064">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">✖️
✖️
بهمنی رییس سازمان لیگ: فکر نمی‌کنم بتوانیم به خاطر فشردگی بازی ها امسال جام حذفی برگزار کنیم
🙁
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/139064" target="_blank">📅 00:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139063">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromشــًٍـٍؓـٍ۪ـ۪ؔـٍ℘ًًیــًٍـٍؓـٍ۪ـ۪ؔـٍ℘ًًد۪ؔاٍؓ℘ًً</strong></div>
<div class="tg-text">تا میتونی اورنوف تشویق کنید و سرگیف اینا ستاره تیمند ارزو هرتیمی ک این بازیکن داشته باشند و ایری هم تشویق کنید روحیه اش برگرد</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/139063" target="_blank">📅 00:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139062">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🅼🅴🅷🅳🅸</strong></div>
<div class="tg-text">پاس هایی ک باکیچ میندازه رو هیچ بازیکنی نمیتونه تو پرسپولیس بندازه بعد کلا یارو رو نیمکته</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/139062" target="_blank">📅 00:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139061">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HIxxF6MyU5QyDdOSXah-nXHVrPWahtHuQX-AAq0q-2ovo3a6dZNbh8LhIPwkElYstcpHd14x7tS0xxgN2JT6_CbAdsaoth9lNRmUe8SGiJsomIag02GlgAXOtyqp0rV-IloWhKw-oVGMBphPymU2hJrFNhwFln_3BfuePHr9eSR50rYczULvH2N4695rufvsPxBL0PKG1fTOkWnnhE5J3bSkFrGkVpVH3iWYWJhaaXAy0c0HSATMLqehGhyQq3lUAJVLP_1IcKUDSIIwI7LWFcz6aHSXTanuo9M-jRVnRfTREmcUMBL9Tpxu7g1NuPVabl0-g02teU58mlQfvkFhlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فارس:
⌛
مدیریت پرسپولیس تصمیمی برای تغییر در کادر فنی ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/139061" target="_blank">📅 00:30 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139060">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d099f34763.mp4?token=SMDlO4kJXFPetmha9LuhDo4WcXPe6yzRM8Fe4V6scmSIa5nLpPAB4hhPLhwdiaLBZMfntWFUFKfFYKbxdkE6aOwZJAYuJHhuB37EwUNpitsGFqfbICRkiSvha20XlM0CLUhFAgVLGd10irTz9uZN1w6sGNPDocnE_G6H0sk8aQiPmZspT3hO8LiIilt69JTCkxwZAtmn1FWa3ZTKqVFaitYpfMsEHfxJOcVKNRjUEyEIvPh9IXRCWfX1ZDrm0eMLPLxmPySQA9ziwmqYaXJL0NROS62TjfVTibcFGS68olAlKh3xojx2JJiIf98ClrEA3xQMkfXRIFpk-cFzjzIOfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d099f34763.mp4?token=SMDlO4kJXFPetmha9LuhDo4WcXPe6yzRM8Fe4V6scmSIa5nLpPAB4hhPLhwdiaLBZMfntWFUFKfFYKbxdkE6aOwZJAYuJHhuB37EwUNpitsGFqfbICRkiSvha20XlM0CLUhFAgVLGd10irTz9uZN1w6sGNPDocnE_G6H0sk8aQiPmZspT3hO8LiIilt69JTCkxwZAtmn1FWa3ZTKqVFaitYpfMsEHfxJOcVKNRjUEyEIvPh9IXRCWfX1ZDrm0eMLPLxmPySQA9ziwmqYaXJL0NROS62TjfVTibcFGS68olAlKh3xojx2JJiIf98ClrEA3xQMkfXRIFpk-cFzjzIOfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انتشار تیزر رسمی سریال کمدی «مرد سه‌ هزار چهره»؛
آغاز پخش از جمعه ۱۳ شهریور از شبکه سه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/139060" target="_blank">📅 00:30 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139059">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‼️
👤
آقا مهدی فرمودن دستیار خارجی نمیخان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/139059" target="_blank">📅 00:03 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139058">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‼️
👤
آقا مهدی فرمودن دستیار خارجی نمیخان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/139058" target="_blank">📅 23:51 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139057">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">✔️
✔️
⚡️
⚡️
⚡️
علیرضا همایی‌فر، یعقوب براجعه و محمدحسین صادقی از جمله بازیکنانی هستند که احتمال دارد در ساعات پایانی نقل‌وانتقالات از پرسپولیس جدا شوند و به صورت قرضی راهی تیم‌های دیگر شوند
✍️
🗞
خبرورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/139057" target="_blank">📅 23:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139056">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❌
❌
قدوسی: اورونوف تو بازی با ملوان هم روی نیمکته!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/139056" target="_blank">📅 23:06 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139055">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">✔️
✔️
✔️
✔️
ارونوف از امروز در تمرین پرسپولیس
🔴
اورونوف که در بازی تدارکاتی پرسپولیس مقابل امیدهای این باشگاه بار دیگر احساس ناراحتی کرده بود، با پیگیری کادر پزشکی و انجام بررسی‌های لازم، ظاهراً شرایط مطلوبی پیدا کرده است.
🔴
این بازیکن از امروز در تمرینات گروهی…</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/139055" target="_blank">📅 22:59 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139054">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔄
❌
اسماعیل کارتال با فنرباغچه در مجموع 3-2 تیم لیون رو تو فرانسه شکست داد و به لیگ قهرمانان اروپا صعود کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/139054" target="_blank">📅 22:55 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139053">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FV7EC8yDEOq0zoSyjNiPZzR5--Cim2QSGr6OdBK8f5ueqT04_JaMJLWpiFkGYKuHfDsXlKYmSIEa6zaYBR4fn8i6C2bLd7eseelg-WXVXSV_iwPke1AMoRv8h6oLhgz37BcfirvANPh-31zX2kgut5XUgdBBSw_8u70EqyzN3FEhAFlMiVKe2lNq2S4o5R7WnfkVllqYyo_DRxol-jLr0iyOzNVmsDLykliDNgLHnRGPVAnBFxVoORC7K8Kzk40adg5dceQ4fgkxBRLv9yz6TH1PBMiVF8msp3zYK_iHOnnXcpFRiaaDYfAUdc9L15SgXPO35oMQlKcPMxz6QMJ4zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
آبی‌ها آماده‌ی شکار؛ لوتون سد راه چلسی!
نبردی که می‌تونه از همون سوت اول بازی غافلگیرکننده باشه.
[
چلسی
🔹
🆚
🔹
لوتون
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/139053" target="_blank">📅 22:46 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139052">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✔️
✔️
✔️
✔️
ارونوف از امروز در تمرین پرسپولیس
🔴
اورونوف که در بازی تدارکاتی پرسپولیس مقابل امیدهای این باشگاه بار دیگر احساس ناراحتی کرده بود، با پیگیری کادر پزشکی و انجام بررسی‌های لازم، ظاهراً شرایط مطلوبی پیدا کرده است.
🔴
این بازیکن از امروز در تمرینات گروهی…</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/139052" target="_blank">📅 22:42 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139051">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔹
🔹
فووووری
🔹
فراز امامعلی : به عنوان دفاع چپ با پرسپولیس به توافق رسیدم و منتظر جلسه نهایی عقد قرارداد هستم. دفاع چپ و وینگر چپ میتوانم بازی کنم. آقای تارتار و باشگاه پرسپولیس به من لطف داشتند و برای پست دفاع چپ من را انتخاب کردند.
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/139051" target="_blank">📅 22:40 · 05 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
